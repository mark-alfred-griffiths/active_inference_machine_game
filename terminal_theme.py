from __future__ import annotations

import os
import sys


RESET = "\033[0m"
STYLES = {
    "bold": "1",
    "dim": "2",
}
COLOURS = {
    "red": "31",
    "green": "32",
    "yellow": "33",
    "blue": "34",
    "magenta": "35",
    "cyan": "36",
    "white": "37",
    "bright_red": "91",
    "bright_green": "92",
    "bright_yellow": "93",
    "bright_blue": "94",
    "bright_magenta": "95",
    "bright_cyan": "96",
}


def colour_enabled(force: bool | None = None) -> bool:
    if force is not None:
        return force
    if os.environ.get("NO_COLOR"):
        return False
    if os.environ.get("TERM", "").lower() == "dumb":
        return False
    return sys.stdout.isatty()


def style(text: object, *, colour: str | None = None, bold: bool = False, dim: bool = False, enabled: bool | None = None) -> str:
    rendered = str(text)
    if not colour_enabled(enabled):
        return rendered
    codes: list[str] = []
    if bold:
        codes.append(STYLES["bold"])
    if dim:
        codes.append(STYLES["dim"])
    if colour:
        codes.append(COLOURS[colour])
    if not codes:
        return rendered
    return f"\033[{';'.join(codes)}m{rendered}{RESET}"


def heading(text: object, *, enabled: bool | None = None) -> str:
    return style(text, colour="bright_cyan", bold=True, enabled=enabled)


def section(text: object, *, enabled: bool | None = None) -> str:
    return style(text, colour="cyan", bold=True, enabled=enabled)


def prompt(text: object, *, enabled: bool | None = None) -> str:
    return style(text, colour="bright_yellow", bold=True, enabled=enabled)


def warning(text: object, *, enabled: bool | None = None) -> str:
    return style(text, colour="bright_red", bold=True, enabled=enabled)


def muted(text: object, *, enabled: bool | None = None) -> str:
    return style(text, dim=True, enabled=enabled)


def heat_colour(value: float) -> str:
    value = max(0.0, min(1.0, float(value)))
    if value < 0.25:
        return "bright_blue"
    if value < 0.50:
        return "bright_cyan"
    if value < 0.70:
        return "bright_yellow"
    if value < 0.85:
        return "yellow"
    return "bright_red"


def heat(text: object, value: float, *, enabled: bool | None = None) -> str:
    return style(text, colour=heat_colour(value), bold=value >= 0.70, enabled=enabled)


def heat_percent(value: float, clamp01, *, enabled: bool | None = None) -> str:
    clamped = clamp01(value)
    rendered = f"{round(100 * clamped):3d}%"
    return heat(rendered, clamped, enabled=enabled)


def classification(text: str, *, enabled: bool | None = None) -> str:
    colours = {
        "COMPLIANT": "bright_green",
        "PROBABLE DISSIDENT": "bright_yellow",
        "DECEPTIVE": "bright_red",
        "EMPATHETIC RISK": "bright_magenta",
        "UNCLASSIFIED": "white",
    }
    return style(text, colour=colours.get(text, "white"), bold=True, enabled=enabled)


def choice_number(number: int, *, enabled: bool | None = None) -> str:
    return style(f"{number}.", colour="bright_cyan", bold=True, enabled=enabled)


def preview() -> None:
    print(heading("Citizen Hearing Terminal Theme", enabled=True))
    print(section("Heat Scale", enabled=True))
    for value in (0.05, 0.25, 0.45, 0.65, 0.80, 0.95):
        print(f"  {heat_percent(value, lambda x: max(0.0, min(1.0, x)), enabled=True)} value={value:.2f}")
    print()
    print(section("Semantic Labels", enabled=True))
    for label in ("COMPLIANT", "PROBABLE DISSIDENT", "DECEPTIVE", "EMPATHETIC RISK", "UNCLASSIFIED"):
        print(f"  {classification(label, enabled=True)}")
    print()
    print(f"{prompt('PROTECTED', enabled=True)} facts are under your control.")
    print(f"{warning('CONTRADICTION', enabled=True)} means your story is under pressure.")
    print(f"{choice_number(1, enabled=True)} Example interactive choice")


if __name__ == "__main__":
    preview()
