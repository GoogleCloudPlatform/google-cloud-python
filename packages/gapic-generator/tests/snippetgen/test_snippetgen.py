# -*- coding: utf-8 -*-
# Copyright 2021 Google LLC
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
#
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

import pytest


CURRENT_DIRECTORY = Path(__file__).parent.absolute()
REPO_ROOT = CURRENT_DIRECTORY.parent.parent

GOLDEN_SNIPPETS = CURRENT_DIRECTORY / "goldens"
GENERATED_SNIPPETS = CURRENT_DIRECTORY / ".test_output"


def setup_module(module):
    """Run protoc on modules and copy the output samples into .test_output"""

    # Delete any existing content in .test_output
    # We intentionally preserve this directory between test runs to make
    # it easier to inspect generated samples.
    shutil.rmtree(GENERATED_SNIPPETS, ignore_errors=True)

    protos = {str(p) for p in CURRENT_DIRECTORY.glob("*.proto")}
    api_common_protos = Path(REPO_ROOT / "api-common-protos").absolute()

    with tempfile.TemporaryDirectory() as tmp_dir:
        # Write out a client library and samples
        subprocess.check_output(
            [
                "python",
                "-m",
                "grpc_tools.protoc",
                f"--experimental_allow_proto3_optional",
                "--python_gapic_opt=autogen-snippets",
                f"--proto_path={CURRENT_DIRECTORY}",
                f"--proto_path={api_common_protos}",
                f"--python_gapic_out={tmp_dir}",
                *protos,
            ]
        )

        # We only care about the auto-generated samples
        generated_samples = Path(tmp_dir) / "samples" / "generated_samples"

        shutil.copytree(generated_samples, GENERATED_SNIPPETS)


def test_files_exist():
    # The golden directory and .test_output directory
    # should have exactly the same number of entries
    golden_files = {p.name for p in GOLDEN_SNIPPETS.glob("*.py")}
    test_output_files = {p.name for p in GENERATED_SNIPPETS.glob("*.py")}

    assert golden_files == test_output_files


def test_goldens():
    # Loop through the goldens directory and assert that each file
    # exists in output directory and has the same code.
    golden_files = GOLDEN_SNIPPETS.glob("*.py")
    for golden in golden_files:
        output_file = GENERATED_SNIPPETS / golden.name
        assert output_file.exists()
        assert golden.read_text() == output_file.read_text()
