# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import subprocess
import sys


def test_namespace_package_compat(tmp_path):
    # The ``google`` namespace package should not be masked
    # by the presence of ``google-cloud-logging``.

    google = tmp_path / "google"
    google.mkdir()
    google.joinpath("othermod.py").write_text("")

    google_otherpkg = tmp_path / "google" / "otherpkg"
    google_otherpkg.mkdir()
    google_otherpkg.joinpath("__init__.py").write_text("")

    # The ``google.cloud`` namespace package should not be masked
    # by the presence of ``google-cloud-logging``.
    google_cloud = tmp_path / "google" / "cloud"
    google_cloud.mkdir()
    google_cloud.joinpath("othermod.py").write_text("")

    google_cloud_otherpkg = tmp_path / "google" / "cloud" / "otherpkg"
    google_cloud_otherpkg.mkdir()
    google_cloud_otherpkg.joinpath("__init__.py").write_text("")

    env = dict(os.environ, PYTHONPATH=str(tmp_path))

    for pkg in [
        "google.othermod",
        "google.cloud.othermod",
        "google.otherpkg",
        "google.cloud.otherpkg",
        "google.cloud.logging",
    ]:
        cmd = [sys.executable, "-c", f"import {pkg}"]
        subprocess.check_output(cmd, env=env)

    for module in ["google.othermod", "google.cloud.othermod"]:
        cmd = [sys.executable, "-m", module]
        subprocess.check_output(cmd, env=env)
