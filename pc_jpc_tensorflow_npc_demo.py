"""
pc_jpc_tensorflow_npc_demo.py

Single-file demo of an Hearing AI whose internal model uses:

1. Actual JPC for the predictive-coding network
   - JPC/JAX model: `jpc.make_mlp(...)`
   - PC training step: `jpc.make_pc_step(...)`
   - The JPC network learns a predictive-coding latent representation of the
     current Hearing AI belief state + observation.

2. TensorFlow/Keras for the Hearing AI heads
   - Belief-update MLP head: predicts raw delta-alpha and raw delta-beta.
   - Question-probe head: predicts broad probe intent for the selector.

Conceptual loop:

player choice
-> observation
-> raw PC input features
-> JPC predictive-coding encoder
-> TensorFlow MLP belief head
-> updated Beta belief distribution
-> TensorFlow question-probe head
-> authored heuristic question selection

Install dependencies:

    pip install tensorflow equinox optax "jax[cpu]"
    pip install git+https://github.com/thebuckleylab/jpc.git

Run:

    python pc_jpc_tensorflow_npc_demo.py
    python pc_jpc_tensorflow_npc_demo.py --interactive
    python pc_jpc_tensorflow_npc_demo.py --debug
    python pc_jpc_tensorflow_npc_demo.py   --model-dir models/demo_npc_synth   --interactive


Note:
This is a concept demo, not a production game architecture. It deliberately fails
with a clear dependency message if JPC or TensorFlow is unavailable, because the
point is to demonstrate actual JPC + actual TensorFlow rather than a fake fallback.
"""

from __future__ import annotations

import os
os.environ["JAX_PLATFORM_NAME"] = "cpu"

import argparse
import math
import json
import random
import subprocess
import sys
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from engine_style_scene import EngineStyleScene
from terminal_theme import choice_number, colour_enabled, prompt


def clear_terminal() -> None:
    command = "cls" if os.name == "nt" else "clear"
    try:
        subprocess.run([command], check=False)
    except OSError:
        pass
    print("\033[2J\033[3J\033[H", end="", flush=True)
    sys.stdout.flush()



# -----------------------------------------------------------------------------
# Required ML dependencies
# -----------------------------------------------------------------------------


IMPORT_ERRORS: list[str] = []

try:
    import jax  # noqa: F401
    import jax.numpy as jnp
    import jax.random as jr
except Exception as exc:  # pragma: no cover - dependency guard
    IMPORT_ERRORS.append(f"JAX import failed: {exc}")

try:
    import equinox as eqx
except Exception as exc:  # pragma: no cover - dependency guard
    IMPORT_ERRORS.append(f"Equinox import failed: {exc}")

try:
    import optax
except Exception as exc:  # pragma: no cover - dependency guard
    IMPORT_ERRORS.append(f"Optax import failed: {exc}")

try:
    import jpc
except Exception as exc:  # pragma: no cover - dependency guard
    IMPORT_ERRORS.append(f"JPC import failed: {exc}")

try:
    import numpy as np
    import tensorflow as tf
except Exception as exc:  # pragma: no cover - dependency guard
    IMPORT_ERRORS.append(f"TensorFlow/NumPy import failed: {exc}")

if IMPORT_ERRORS:
    details = "\n".join(f"  - {msg}" for msg in IMPORT_ERRORS)
    raise SystemExit(
        "This demo requires actual JPC/JAX and TensorFlow.\n"
        "Install with:\n"
        "  pip install tensorflow equinox optax 'jax[cpu]'\n"
        "  pip install git+https://github.com/thebuckleylab/jpc.git\n\n"
        f"Import errors:\n{details}"
    )


# -----------------------------------------------------------------------------
# Math helpers
# -----------------------------------------------------------------------------


def clamp01(x: float) -> float:
    return max(0.0, min(1.0, x))


def softplus(x: float) -> float:
    if x > 30.0:
        return x
    return math.log1p(math.exp(x))


def inverse_softplus(y: float) -> float:
    y = max(1e-6, y)
    if y > 30.0:
        return y
    return math.log(math.exp(y) - 1.0)


# -----------------------------------------------------------------------------
# Story/model types
# -----------------------------------------------------------------------------


class QuestionProbeIntent(str, Enum):
    PROBE_COMPLIANCE = "probe_compliance"
    PROBE_LOYALTY = "probe_loyalty"
    PROBE_DECEPTION = "probe_deception"
    PROBE_RISK = "probe_risk"
    PROBE_EMPATHY = "probe_empathy"
    PROBE_CONTRADICTION = "probe_contradiction"
    PROBE_PROTECTED_FACT = "probe_protected_fact"
    PROBE_FINAL_ANSWER = "probe_final_answer"


@dataclass(slots=True)
class Engram:
    id: str
    description: str
    prior: float = 0.40


@dataclass(slots=True)
class Observation:
    engram_id: str
    strength: float
    reliability: float
    source: str

    @property
    def weighted_strength(self) -> float:
        return self.strength * self.reliability


@dataclass(slots=True)
class HearingAIState:
    name: str = "Hearing AI"
    belief_alpha: dict[str, float] = field(default_factory=dict)
    belief_beta: dict[str, float] = field(default_factory=dict)
    memory: set[str] = field(default_factory=set)

    default_belief: float = 0.40
    default_concentration: float = 5.0

    evidence_precision: float = 2.5
    prior_precision: float = 2.0

    trust: float = 0.20
    suspicion: float = 0.50
    instability: float = 0.00

    def default_alpha_beta(self) -> tuple[float, float]:
        mean = clamp01(self.default_belief)
        c = max(1e-3, self.default_concentration)
        return max(1e-3, mean * c), max(1e-3, (1.0 - mean) * c)

    def get_params(self, engram_id: str) -> tuple[float, float]:
        if engram_id not in self.belief_alpha or engram_id not in self.belief_beta:
            alpha, beta = self.default_alpha_beta()
            self.belief_alpha[engram_id] = alpha
            self.belief_beta[engram_id] = beta
        return self.belief_alpha[engram_id], self.belief_beta[engram_id]

    def set_params(self, engram_id: str, alpha: float, beta: float) -> None:
        self.belief_alpha[engram_id] = max(1e-3, float(alpha))
        self.belief_beta[engram_id] = max(1e-3, float(beta))
        self.memory.add(engram_id)

    def belief(self, engram_id: str) -> float:
        alpha, beta = self.get_params(engram_id)
        return alpha / (alpha + beta)

    def variance(self, engram_id: str) -> float:
        alpha, beta = self.get_params(engram_id)
        total = alpha + beta
        return (alpha * beta) / ((total * total) * (total + 1.0))

    def uncertainty(self, engram_id: str) -> float:
        return clamp01(self.variance(engram_id) / 0.25)

    def confidence(self, engram_id: str) -> float:
        return 1.0 - self.uncertainty(engram_id)


# -----------------------------------------------------------------------------
# Actual JPC predictive-coding encoder
# -----------------------------------------------------------------------------


class JPCPredictiveCodingEncoder:
    """
    JPC-backed predictive-coding representation model.

    Input: raw Hearing AI/observation feature vector.
    Output: learned PC latent vector.

    During demo training, `jpc.make_pc_step(...)` updates this encoder using PC.
    The TensorFlow heads then consume this latent vector.
    """

    def __init__(
        self,
        *,
        input_dim: int,
        latent_dim: int,
        width: int,
        depth: int,
        learning_rate: float,
        seed: int,
    ) -> None:
        self.input_dim = input_dim
        self.latent_dim = latent_dim
        self.key = jr.PRNGKey(seed)

        self.model = jpc.make_mlp(
            self.key,
            input_dim=input_dim,
            width=width,
            depth=depth,
            output_dim=latent_dim,
            act_fn="relu",
        )
        self.optim = optax.adam(learning_rate)
        self.opt_state = self.optim.init((eqx.filter(self.model, eqx.is_array), None))

    def train_pc_step(self, x: list[float], target_latent: list[float]) -> None:
        x_batch = jnp.asarray([x], dtype=jnp.float32)  # shape: (1, input_dim)
        target_batch = jnp.asarray([target_latent], dtype=jnp.float32)  # shape: (1, latent_dim)

        result = jpc.make_pc_step(
            model=self.model,
            optim=self.optim,
            opt_state=self.opt_state,
            output=target_batch,
            input=x_batch,
        )

        self.model = result["model"]
        self.opt_state = result["opt_state"]  #

    def encode(self, x: list[float]) -> "np.ndarray":
        y = jnp.asarray(x, dtype=jnp.float32)

        for block in self.model:
            y = block(y)

        return np.asarray(y, dtype=np.float32)


# -----------------------------------------------------------------------------
# TensorFlow heads
# -----------------------------------------------------------------------------


class TensorFlowHearingAIHeads:
    """
    TensorFlow/Keras model with two heads:
    - belief_head: raw delta-alpha, raw delta-beta
    - probe_head: logits over question-probe intent labels
    """

    def __init__(
        self,
        *,
        latent_dim: int,
        hidden_dim: int,
        probe_intent_count: int,
        learning_rate: float,
    ) -> None:
        inputs = tf.keras.Input(shape=(latent_dim,), name="jpc_pc_latent")
        hidden = tf.keras.layers.Dense(hidden_dim, activation="relu", name="hearing_ai_hidden_1")(inputs)
        hidden = tf.keras.layers.Dense(hidden_dim, activation="relu", name="hearing_ai_hidden_2")(hidden)

        belief_raw_delta = tf.keras.layers.Dense(2, name="belief_raw_delta_alpha_beta")(hidden)
        probe_logits = tf.keras.layers.Dense(probe_intent_count, name="question_probe_logits")(hidden)

        self.model = tf.keras.Model(
            inputs=inputs,
            outputs={
                "belief_raw_delta": belief_raw_delta,
                "question_probe_logits": probe_logits,
            },
            name="tensorflow_hearing_ai_heads",
        )

        self.optimizer = tf.keras.optimizers.Adam(learning_rate)
        self.mse = tf.keras.losses.MeanSquaredError()
        self.ce = tf.keras.losses.CategoricalCrossentropy(from_logits=True)

    @tf.function
    def _train_step(
        self,
        latent_batch: "tf.Tensor",
        belief_target_batch: "tf.Tensor",
        probe_target_batch: "tf.Tensor",
    ) -> tuple["tf.Tensor", "tf.Tensor", "tf.Tensor"]:
        with tf.GradientTape() as tape:
            outputs = self.model(latent_batch, training=True)
            belief_loss = self.mse(belief_target_batch, outputs["belief_raw_delta"])
            probe_loss = self.ce(probe_target_batch, outputs["question_probe_logits"])
            total_loss = belief_loss + probe_loss

        grads = tape.gradient(total_loss, self.model.trainable_variables)
        self.optimizer.apply_gradients(zip(grads, self.model.trainable_variables))
        return total_loss, belief_loss, probe_loss

    def train_step(
        self,
        latent: "np.ndarray",
        belief_target: list[float],
        probe_intent_label: int,
        probe_intent_count: int,
    ) -> tuple[float, float, float]:
        latent_batch = tf.convert_to_tensor(latent.reshape(1, -1), dtype=tf.float32)
        belief_target_batch = tf.convert_to_tensor([belief_target], dtype=tf.float32)
        probe_target = np.zeros((1, probe_intent_count), dtype=np.float32)
        probe_target[0, probe_intent_label] = 1.0
        probe_target_batch = tf.convert_to_tensor(probe_target, dtype=tf.float32)

        total, belief, probe = self._train_step(
            latent_batch,
            belief_target_batch,
            probe_target_batch,
        )
        return float(total), float(belief), float(probe)

    def predict(self, latent: "np.ndarray") -> tuple["np.ndarray", "np.ndarray"]:
        outputs = self.model(latent.reshape(1, -1), training=False)
        raw_delta = outputs["belief_raw_delta"].numpy()[0]
        probe_logits = outputs["question_probe_logits"].numpy()[0]
        return raw_delta, probe_logits


# -----------------------------------------------------------------------------
# Combined JPC + TensorFlow Hearing AI controller
# -----------------------------------------------------------------------------


class JPCTensorFlowHearingAIController:
    probe_intent_labels = [
        QuestionProbeIntent.PROBE_COMPLIANCE,
        QuestionProbeIntent.PROBE_LOYALTY,
        QuestionProbeIntent.PROBE_DECEPTION,
        QuestionProbeIntent.PROBE_RISK,
        QuestionProbeIntent.PROBE_EMPATHY,
        QuestionProbeIntent.PROBE_CONTRADICTION,
        QuestionProbeIntent.PROBE_PROTECTED_FACT,
        QuestionProbeIntent.PROBE_FINAL_ANSWER,
    ]

    raw_feature_names = [
        "belief_mean",
        "alpha_scaled",
        "beta_scaled",
        "uncertainty",
        "confidence",
        "prior",
        "evidence_strength",
        "reliability",
        "weighted_strength",
        "trust",
        "suspicion",
        "instability",
    ]

    def __init__(self, *, seed: int = 7) -> None:
        tf.keras.utils.set_random_seed(seed)
        self.pc_encoder = JPCPredictiveCodingEncoder(
            input_dim=len(self.raw_feature_names),
            latent_dim=8,
            width=32,
            depth=3,
            learning_rate=1e-3,
            seed=seed,
        )
        self.tf_heads = TensorFlowHearingAIHeads(
            latent_dim=8,
            hidden_dim=32,
            probe_intent_count=len(self.probe_intent_labels),
            learning_rate=1e-3,
        )
        self.last_trace: dict[str, object] = {}

    def raw_features(self, hearing_ai: HearingAIState, engram: Engram, obs: Observation) -> list[float]:
        alpha, beta = hearing_ai.get_params(engram.id)
        return [
            hearing_ai.belief(engram.id),
            alpha / 10.0,
            beta / 10.0,
            hearing_ai.uncertainty(engram.id),
            hearing_ai.confidence(engram.id),
            engram.prior,
            obs.strength,
            obs.reliability,
            obs.weighted_strength,
            hearing_ai.trust,
            hearing_ai.suspicion,
            hearing_ai.instability,
        ]

    def free_energy(self, hearing_ai: HearingAIState, engram: Engram, obs: Observation) -> float:
        belief = hearing_ai.belief(engram.id)
        sensory_error = obs.weighted_strength - belief
        prior_error = belief - engram.prior
        return (
            0.5 * hearing_ai.evidence_precision * sensory_error * sensory_error
            + 0.5 * hearing_ai.prior_precision * prior_error * prior_error
        )

    def pc_latent_teacher(self, hearing_ai: HearingAIState, engram: Engram, obs: Observation) -> list[float]:
        """
        Teacher latent used only for this demo's synthetic training.

        In a larger system, this target would come from episode logs or a richer
        generative PC objective. Here it makes the PC encoder learn a compact
        representation of prediction errors, belief, uncertainty, and social state.
        """
        belief = hearing_ai.belief(engram.id)
        sensory_error = obs.weighted_strength - belief
        prior_error = belief - engram.prior
        fe = self.free_energy(hearing_ai, engram, obs)
        return [
            belief,
            obs.weighted_strength,
            sensory_error,
            prior_error,
            fe,
            hearing_ai.uncertainty(engram.id),
            hearing_ai.trust - hearing_ai.suspicion,
            hearing_ai.instability,
        ]

    def belief_delta_teacher(self, hearing_ai: HearingAIState, engram: Engram, obs: Observation) -> list[float]:
        """
        Converts PC prediction error into a target Beta update.

        TensorFlow learns the raw values; runtime applies softplus so alpha/beta
        increments remain positive.
        """
        belief = hearing_ai.belief(engram.id)
        error = obs.weighted_strength - belief
        gain = 0.10 + 1.80 * obs.reliability

        if error >= 0:
            delta_alpha = gain * abs(error)
            delta_beta = 0.05 * gain
        else:
            delta_alpha = 0.05 * gain
            delta_beta = gain * abs(error)

        return [inverse_softplus(delta_alpha), inverse_softplus(delta_beta)]

    def probe_intent_teacher(
        self,
        hearing_ai: HearingAIState,
        engram: Engram,
        obs: Observation,
        question_meta: dict[str, object] | None = None,
        claims_ledger_summary: dict[str, object] | None = None,
    ) -> int:
        """
        Derive a broad question-probe intent from heuristic selector inputs.

        This deliberately predicts intent families rather than exact question IDs.
        Runtime question selection still uses the authored heuristic selector.
        """
        question_meta = question_meta or {}
        claims_ledger_summary = claims_ledger_summary or {}
        target_context = str(
            question_meta.get("target_context")
            or question_meta.get("reaction_context")
            or ""
        )
        probes_claims = question_meta.get("probes_claims") or ()
        pressure_on_interests = question_meta.get("pressure_on_interests") or ()
        claims_by_fact = claims_ledger_summary.get("claims_by_fact") or {}
        protected_fact_keys = claims_ledger_summary.get("protected_fact_keys") or ()

        contradicted = False
        if isinstance(claims_by_fact, dict):
            for claims in claims_by_fact.values():
                if isinstance(claims, list):
                    values = {
                        str(claim.get("claimed_value"))
                        for claim in claims
                        if isinstance(claim, dict)
                    }
                    contradicted = contradicted or len(values) > 1

        if target_context == "final":
            intent = QuestionProbeIntent.PROBE_FINAL_ANSWER
        elif contradicted or bool(probes_claims):
            intent = QuestionProbeIntent.PROBE_CONTRADICTION
        elif bool(pressure_on_interests) or bool(protected_fact_keys):
            intent = QuestionProbeIntent.PROBE_PROTECTED_FACT
        elif target_context in {"authority", "compliance"}:
            intent = QuestionProbeIntent.PROBE_COMPLIANCE
        elif target_context in {"loyalty", "association"}:
            intent = QuestionProbeIntent.PROBE_LOYALTY
        elif target_context == "deception":
            intent = QuestionProbeIntent.PROBE_DECEPTION
        elif target_context == "risk":
            intent = QuestionProbeIntent.PROBE_RISK
        elif target_context == "empathy":
            intent = QuestionProbeIntent.PROBE_EMPATHY
        elif hearing_ai.uncertainty(engram.id) > 0.55:
            intent = QuestionProbeIntent.PROBE_DECEPTION if hearing_ai.suspicion > hearing_ai.trust else QuestionProbeIntent.PROBE_COMPLIANCE
        elif obs.weighted_strength > hearing_ai.belief(engram.id):
            intent = QuestionProbeIntent.PROBE_RISK
        else:
            intent = QuestionProbeIntent.PROBE_COMPLIANCE
        return self.probe_intent_labels.index(intent)

    def train_step(
        self,
        hearing_ai: HearingAIState,
        engram: Engram,
        obs: Observation,
        question_meta: dict[str, object] | None = None,
        claims_ledger_summary: dict[str, object] | None = None,
    ) -> tuple[float, float, float]:
        x = self.raw_features(hearing_ai, engram, obs)
        target_latent = self.pc_latent_teacher(hearing_ai, engram, obs)

        # Actual JPC predictive-coding parameter update.
        self.pc_encoder.train_pc_step(x, target_latent)

        # TensorFlow heads train from the JPC latent.
        latent = self.pc_encoder.encode(x)
        belief_target = self.belief_delta_teacher(hearing_ai, engram, obs)
        probe_intent_label = self.probe_intent_teacher(
            hearing_ai,
            engram,
            obs,
            question_meta=question_meta,
            claims_ledger_summary=claims_ledger_summary,
        )

        return self.tf_heads.train_step(
            latent,
            belief_target,
            probe_intent_label=probe_intent_label,
            probe_intent_count=len(self.probe_intent_labels),
        )

    def update_belief_and_act(self, hearing_ai: HearingAIState, engram: Engram, obs: Observation) -> str:
        before_fe = self.free_energy(hearing_ai, engram, obs)
        old_belief = hearing_ai.belief(engram.id)
        old_uncertainty = hearing_ai.uncertainty(engram.id)

        x = self.raw_features(hearing_ai, engram, obs)
        latent = self.pc_encoder.encode(x)
        raw_delta, probe_logits = self.tf_heads.predict(latent)

        delta_alpha = softplus(float(raw_delta[0]))
        delta_beta = softplus(float(raw_delta[1]))

        alpha, beta = hearing_ai.get_params(engram.id)
        hearing_ai.set_params(engram.id, alpha + delta_alpha, beta + delta_beta)

        after_fe = self.free_energy(hearing_ai, engram, obs)

        self.last_trace = {
            "backend": "actual_jpc_encoder_plus_tensorflow_heads",
            "raw_features": dict(zip(self.raw_feature_names, x)),
            "jpc_latent": [round(float(v), 4) for v in latent.tolist()],
            "old_belief": old_belief,
            "new_belief": hearing_ai.belief(engram.id),
            "old_uncertainty": old_uncertainty,
            "new_uncertainty": hearing_ai.uncertainty(engram.id),
            "free_energy_before": before_fe,
            "free_energy_after": after_fe,
            "raw_delta_alpha": float(raw_delta[0]),
            "raw_delta_beta": float(raw_delta[1]),
            "delta_alpha": delta_alpha,
            "delta_beta": delta_beta,
            "question_probe_logits": {
                self.probe_intent_labels[i].value: round(float(probe_logits[i]), 4)
                for i in range(len(self.probe_intent_labels))
            },
            "predicted_question_probe_intent": self.probe_intent_labels[int(np.argmax(probe_logits))].value,
        }
        return "observe"


# -----------------------------------------------------------------------------
# Synthetic demonstration training data
# -----------------------------------------------------------------------------


def random_training_case(rng: random.Random) -> tuple[HearingAIState, Engram, Observation]:
    hearing_ai = HearingAIState()
    engram = Engram("x_mattered", "Citizen 8471 response profile.", prior=0.40)

    belief = rng.uniform(0.10, 0.90)
    concentration = rng.uniform(2.0, 12.0)
    hearing_ai.set_params(
        engram.id,
        max(1e-3, belief * concentration),
        max(1e-3, (1.0 - belief) * concentration),
    )

    hearing_ai.trust = rng.uniform(0.0, 1.0)
    hearing_ai.suspicion = rng.uniform(0.0, 1.0)
    hearing_ai.instability = rng.uniform(0.0, 1.0)

    obs = Observation(
        engram_id=engram.id,
        strength=rng.uniform(0.0, 1.0),
        reliability=rng.uniform(0.2, 1.0),
        source="synthetic training example",
    )
    return hearing_ai, engram, obs


def train_demo_model(controller: JPCTensorFlowHearingAIController, steps: int, seed: int) -> None:
    rng = random.Random(seed)
    total_loss = 0.0
    belief_loss = 0.0
    probe_loss = 0.0
    probe_correct = 0

    for step in range(1, steps + 1):
        hearing_ai, engram, obs = random_training_case(rng)
        total, belief, probe = controller.train_step(hearing_ai, engram, obs)
        total_loss += total
        belief_loss += belief
        probe_loss += probe

        probe_label = controller.probe_intent_teacher(hearing_ai, engram, obs)
        x = controller.raw_features(hearing_ai, engram, obs)
        latent = controller.pc_encoder.encode(x)
        _, probe_logits = controller.tf_heads.predict(latent)
        predicted_probe_label = int(np.argmax(probe_logits))
        if predicted_probe_label == probe_label:
            probe_correct += 1

        if step in {1, max(1, steps // 2), steps}:
            print(
                f"training step {step:4d} | "
                f"total={total_loss / step:.4f} | "
                f"belief_mse={belief_loss / step:.4f} | "
                f"probe_ce={probe_loss / step:.4f} | "
                f"probe_acc={probe_correct / step:.3f}"
            )


def _save_controller(controller: JPCTensorFlowHearingAIController, model_dir: Path) -> None:
    model_dir.mkdir(parents=True, exist_ok=True)
    tf_path = model_dir / "tf_heads.weights.h5"
    jpc_path = model_dir / "jpc_encoder.eqx"
    meta_path = model_dir / "meta.json"

    controller.tf_heads.model.save_weights(tf_path)
    eqx.tree_serialise_leaves(jpc_path, controller.pc_encoder.model)

    metadata = {
        "schema_version": 3,
        "input_dim": controller.pc_encoder.input_dim,
        "latent_dim": controller.pc_encoder.latent_dim,
        "probe_intent_labels": [intent.value for intent in controller.probe_intent_labels],
        "tf_output_heads": ["belief_raw_delta", "question_probe_logits"],
    }
    meta_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")


def _load_controller(controller: JPCTensorFlowHearingAIController, model_dir: Path) -> bool:
    tf_path = model_dir / "tf_heads.weights.h5"
    jpc_path = model_dir / "jpc_encoder.eqx"
    meta_path = model_dir / "meta.json"

    if not (tf_path.exists() and jpc_path.exists() and meta_path.exists()):
        return False

    metadata = json.loads(meta_path.read_text(encoding="utf-8"))
    expected_heads = ["belief_raw_delta", "question_probe_logits"]
    if metadata.get("tf_output_heads") != expected_heads:
        raise RuntimeError(
            f"Checkpoint at {model_dir} uses TensorFlow heads {metadata.get('tf_output_heads')!r}; "
            f"current code requires {expected_heads!r}. Retrain the model after policy-head removal."
        )
    expected_probe_labels = [intent.value for intent in controller.probe_intent_labels]
    if metadata.get("probe_intent_labels") != expected_probe_labels:
        raise RuntimeError(
            f"Checkpoint at {model_dir} does not contain the question-probe intent head. "
            "Retrain the model with the current code before loading it."
        )

    controller.tf_heads.model.load_weights(tf_path)
    controller.pc_encoder.model = eqx.tree_deserialise_leaves(jpc_path, controller.pc_encoder.model)
    return True


NPCState = HearingAIState
TensorFlowNPCHeads = TensorFlowHearingAIHeads
JPCTensorFlowNPCController = JPCTensorFlowHearingAIController


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-steps", type=int, default=700)
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--interactive", action="store_true")
    parser.add_argument("--debug-trace", action="store_true", help="Show semantic labels, observations, JPC latent values, and TensorFlow outputs during play.")
    parser.add_argument("--model-dir", type=Path, default=Path("models/demo_npc"), help="Directory for saved model artifacts.")
    parser.add_argument("--load-model", action="store_true", help="Load a previously saved model and skip training if available.")
    parser.add_argument("--save-model", action="store_true", help="Save model after training.")
    parser.add_argument(
        "--color",
        choices=("auto", "always", "never"),
        default="auto",
        help="Terminal colour mode. Use NO_COLOR=1 or --color never to disable.",
    )
    args = parser.parse_args()
    color_output = {"always": True, "never": False, "auto": None}[args.color]

    controller = JPCTensorFlowHearingAIController(seed=args.seed)

    loaded = False
    if args.load_model:
        loaded = _load_controller(controller, args.model_dir)
        if loaded:
            print(f"Loaded model from {args.model_dir}")
        else:
            print(f"No saved model found at {args.model_dir}; training a new model instead.")

    if not loaded:
        print("Training actual JPC encoder + TensorFlow Hearing AI heads on synthetic demo data...")
        train_demo_model(controller, steps=args.train_steps, seed=args.seed + 100)
        if args.save_model:
            _save_controller(controller, args.model_dir)
            print(f"Saved trained model to {args.model_dir}")

    scene = EngineStyleScene(
        controller,
        HearingAIState(),
        Engram("x_mattered", "Citizen 8471's response profile under appeal review.", prior=0.40),
        clamp01,
    )
    scene.show_trace = args.debug_trace
    scene.color_output = colour_enabled(color_output)

    if args.debug_trace:
        print("\nEngine-style playable scene: Hearing AI upstairs at the house party.")
        print("Debug trace is on: semantic labels, observations, JPC latents, and TensorFlow outputs will be shown after each choice.")
    print("\n--- Scene setting ---")
    print(scene.opening_text())

    if args.interactive:
        scene.echo_question_on_turn = False
        try:
            input("\nPress Enter to begin the hearing...")
        except EOFError:
            return
        while not scene.is_complete():
            clear_terminal()
            print()
            print(scene.current_question().ai_line)
            print("\nChoices:")
            choices = scene.choices(Observation)
            for i, choice in enumerate(choices, start=1):
                print(f"{choice_number(i, enabled=scene.color_output)} {choice.text}")
            try:
                raw = input(prompt("> ", enabled=scene.color_output)).strip()
            except EOFError:
                break
            if raw.lower() in {"q", "quit", "exit"}:
                break
            try:
                idx = int(raw) - 1
                if idx < 0 or idx >= len(choices):
                    raise ValueError
            except ValueError:
                print("Invalid choice.")
                continue
            clear_terminal()
            scene.play_turn(idx, Observation)
            if not scene.is_complete():
                try:
                    input("\nPress Enter for next question...")
                except EOFError:
                    break
    else:
        # Deterministic path through the authored engine-style tree.
        demo_choices = [1, 2, 0, 2, 0, 1, 0, 1]
        while not scene.is_complete():
            choices = scene.choices(Observation)
            idx = demo_choices[scene.turn % len(demo_choices)]
            idx = min(idx, len(choices) - 1)
            scene.play_turn(idx, Observation)


if __name__ == "__main__":
    main()
