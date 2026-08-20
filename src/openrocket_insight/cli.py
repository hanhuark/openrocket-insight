"""Command-line entry point for the pre-alpha workflow."""

from __future__ import annotations

import argparse

from .summary import format_summary, read_runs


def main() -> None:
    parser = argparse.ArgumentParser(prog="openrocket-insight")
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command in ("validate", "summarize"):
        command_parser = subparsers.add_parser(command)
        command_parser.add_argument("input_csv")
    args = parser.parse_args()

    try:
        runs = read_runs(args.input_csv)
    except (OSError, ValueError) as error:
        parser.error(str(error))

    if args.command == "validate":
        print(f"Valid normalized summary CSV: {len(runs)} run(s).")
    else:
        print(format_summary(runs))


if __name__ == "__main__":
    main()
