from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from case_file import CASE_FILE_FACTORIES, create_case_file


def main() -> None:
    for case_key in CASE_FILE_FACTORIES:
        case_file = create_case_file(case_key)
        print(f"## {case_file.label} ({case_file.key})")
        print("Public summary:")
        print(case_file.public_summary())
        print("Hidden summary:")
        print(case_file.hidden_summary())
        print()


if __name__ == "__main__":
    main()
