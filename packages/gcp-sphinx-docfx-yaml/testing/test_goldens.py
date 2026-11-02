"""Temporarily disabled, moved over to unblock the repository."""
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import difflib
import filecmp
import os
import shutil
import sys
from pathlib import Path

import pytest
from docuploader import shell
from sphinx.application import Sphinx


@pytest.mark.parametrize(
    "test_dir", ["handwritten", "gapic-combo", "gapic-auto", "non-cloud", "auth"]
)
def test_goldens(update_goldens, test_dir):
    source_dir = Path("tests/testdata") / test_dir
    golden_dir = Path("tests/testdata/goldens") / test_dir

    docs_dir = source_dir / "docs"
    build_dir = docs_dir / "_build"

    if build_dir.exists():
        shutil.rmtree(build_dir)

    out_dir = build_dir / "html/docfx_yaml"

    # Install dependencies.
    try:
        shell.run(
            [
                sys.executable,
                "-m",
                "pip",
                "install",
                "-e",
                ".[all]",
                "recommonmark",
            ],
            cwd=source_dir,
            hide_output=False,
        )
    except Exception as e:
        pytest.fail(f"build raised an exception: {e}")

    # Generate!
    try:
        shell.run(
            [
                "sphinx-build",
                # Settings to be used for sphinx-build
                "-D",
                # Extensions to be added
                (
                    "extensions=sphinx.ext.autodoc,"
                    "sphinx.ext.autosummary,"
                    "docfx_yaml.extension,"
                    "sphinx.ext.intersphinx,"
                    "sphinx.ext.coverage,"
                    "sphinx.ext.napoleon,"
                    "sphinx.ext.todo,"
                    "sphinx.ext.viewcode,"
                    "recommonmark"
                ),
                # builder to use
                "-b",
                "html",
                # cache directory path
                "-d",
                "docs/_build/doctrees/",
                # source directory
                "docs/",
                # output directory for HTML
                "docs/_build/html",
            ],
            cwd=source_dir,
            hide_output=False,
        )
    except Exception as e:
        pytest.fail(f"build raised an exception: {e}")

    if update_goldens:
        shutil.rmtree(golden_dir, ignore_errors=True)
        shutil.copytree(out_dir, golden_dir, dirs_exist_ok=True)
        pytest.skip(
            "Updated goldens! Re-run the test without the --update-goldens flag."
        )

    got_files = [os.path.relpath(f, out_dir) for f in out_dir.rglob("*")]
    golden_files = [os.path.relpath(f, golden_dir) for f in golden_dir.rglob("*")]

    nl = "\n"
    extra = "Extra:\n" + "\n+ ".join([f for f in got_files if f not in golden_files])
    missing = "Missing:\n" + "\n- ".join(
        [f for f in golden_files if f not in got_files]
    )

    assert len(got_files) == len(golden_files), (
        f"got {len(got_files)} files, want {len(golden_files)}:{nl}{extra}{nl}{missing}"
    )

    (eq, neq, other) = filecmp.cmpfiles(out_dir, golden_dir, got_files, shallow=False)
    other = [(out_dir / f).as_posix() for f in other]

    if other:
        pytest.fail(f"found unknown files (should never happen): {other}")
    if neq:
        diff = ""
        for f in neq:
            with open(out_dir / f) as out:
                with open(golden_dir / f) as gold:
                    out_lines = out.readlines()
                    gold_lines = gold.readlines()
                    diff = "\n" + "\n".join(
                        difflib.context_diff(
                            gold_lines,
                            out_lines,
                            fromfile=str(golden_dir / f),
                            tofile=str(out_dir / f),
                        )
                    )

        pytest.fail(f"got files that don't match goldens: {diff}")
