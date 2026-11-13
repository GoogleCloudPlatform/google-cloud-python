#!/usr/bin/env python3
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Package-aware Ruff runner for pre-commit in google-cloud-python monorepo.

Because google-cloud-python contains 280+ packages that share the `google`
namespace, running Ruff from the monorepo root causes `isort` (I001) to
misidentify package-local modules as third-party.

This runner groups staged files by their package directory (e.g.
`packages/<package-name>`) and executes Ruff inside each package directory,
matching the exact execution environment used by `nox -s lint` in CI.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from collections import defaultdict
from pathlib import Path


def find_package_root(filepath: Path, repo_root: Path) -> Path:
    """Find the enclosing package directory for a file, relative to repo_root.

    Returns the path to `packages/<pkg>` or `preview-packages/<pkg>` if the
    file is located inside a package, otherwise returns `repo_root`.
    """
    try:
        rel_path = filepath.resolve().relative_to(repo_root.resolve())
    except ValueError:
        return repo_root

    parts = rel_path.parts
    for i, part in enumerate(parts):
        if part in ("packages", "preview-packages") and i + 1 < len(parts):
            return repo_root / Path(*parts[: i + 2])
    return repo_root


def run_ruff_for_package(
    command: str,
    pkg_root: Path,
    files: list[Path],
    extra_args: list[str],
) -> int:
    """Run ruff check or ruff format inside a package directory."""
    rel_files = [str(f.resolve().relative_to(pkg_root.resolve())) for f in files]

    if command == "check":
        cmd = [
            "ruff",
            "check",
            "--select",
            "I",
            "--fix",
            "--target-version=py310",
            "--line-length=88",
            *extra_args,
            *rel_files,
        ]
    elif command == "format":
        cmd = [
            "ruff",
            "format",
            "--target-version=py310",
            "--line-length=88",
            *extra_args,
            *rel_files,
        ]
    else:
        cmd = ["ruff", command, *extra_args, *rel_files]

    try:
        res = subprocess.run(cmd, cwd=str(pkg_root))
        return res.returncode
    except FileNotFoundError:
        print(
            "Error: 'ruff' command not found. Please ensure Ruff is installed and available in your PATH.",
            file=sys.stderr,
        )
        return 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Package-aware Ruff runner for pre-commit."
    )
    parser.add_argument(
        "command",
        choices=["check", "format"],
        help="Ruff subcommand to execute ('check' or 'format')",
    )
    parser.add_argument(
        "files",
        nargs="*",
        type=Path,
        help="List of files to lint/format",
    )
    args, unknown = parser.parse_known_args(argv)

    if not args.files:
        return 0

    repo_root = Path.cwd()
    try:
        git_root_out = subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
        if git_root_out:
            repo_root = Path(git_root_out)
    except Exception:
        pass

    # Group python files by package root
    package_groups: dict[Path, list[Path]] = defaultdict(list)
    for f in args.files:
        if not f.exists():
            continue
        if f.suffix not in (".py", ".pyi", ".ipynb"):
            continue
        pkg_root = find_package_root(f, repo_root)
        package_groups[pkg_root].append(f)

    overall_rc = 0
    for pkg_root, files in package_groups.items():
        rc = run_ruff_for_package(args.command, pkg_root, files, unknown)
        if rc != 0:
            overall_rc = rc

    return overall_rc


if __name__ == "__main__":
    sys.exit(main())
