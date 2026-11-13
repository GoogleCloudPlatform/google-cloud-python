#!/bin/bash
# Copyright 2024 Google LLC
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

set -eo pipefail

# Reuse the first Python from python_versions.yaml, which build.sh has already
# installed from python.org into /Library/Frameworks.
PUBLISH_PY=$(awk -F': ' '/^versions:/ {print $2}' "${REPO_ROOT}/scripts/python_versions.yaml" | awk '{print $1}' | cut -d. -f1,2)
PYTHON_EXE="/Library/Frameworks/Python.framework/Versions/${PUBLISH_PY}/bin/python${PUBLISH_PY}"

"${PYTHON_EXE}" -m pip install --upgrade "setuptools<71" twine wheel pkginfo

echo "Built wheels in ${REPO_ROOT}/wheels/:"
ls -la "${REPO_ROOT}/wheels/"

for VER in $(awk -F': ' '/^versions:/ {print $2}' "${REPO_ROOT}/scripts/python_versions.yaml"); do
    SHORT=$(echo "$VER" | cut -d. -f1,2)
    ABI="cp${SHORT//.}-cp${SHORT//.}"
    ls "${REPO_ROOT}/wheels/"*${ABI}*.whl >/dev/null || {
        echo "ERROR: Missing macOS wheel for ${ABI}!"
        exit 1
    }
done

"${PYTHON_EXE}" -m twine check "${REPO_ROOT}/wheels/"*
echo "macOS wheels are ready for Kokoro / OSS Exit Gate aggregation."
