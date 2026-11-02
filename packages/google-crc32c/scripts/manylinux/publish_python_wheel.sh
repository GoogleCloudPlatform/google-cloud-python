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

REPO_ROOT="${REPO_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"

# This script runs as a container entrypoint in quay.io/pypa/manylinux2014_x86_64.
# The venv is load-bearing: `releasetool publish-reporter-script` emits bash that
# hardcodes `python3`, which does not exist in this image outside a venv.
PYTHON_BIN="/opt/python/cp312-cp312/bin/python"
if [[ ! -x "${PYTHON_BIN}" ]]; then
    echo "ERROR: ${PYTHON_BIN} not found; run this inside manylinux2014_x86_64." >&2
    exit 1
fi

PUBLISH_VENV="$(mktemp -d)/venv"
"${PYTHON_BIN}" -m venv "${PUBLISH_VENV}"
source "${PUBLISH_VENV}/bin/activate"

python -m pip install --upgrade "setuptools<71" twine wheel pkginfo

echo "Built wheels in ${REPO_ROOT}/wheels/:"
ls -la "${REPO_ROOT}/wheels/"

# If BUILD_PYTHON is specified (single version build), only validate wheels for that version.
# Otherwise, validate wheels for all versions listed in python_versions.yaml.
VERSIONS_TO_CHECK=""
if [[ -n "${BUILD_PYTHON}" ]]; then
    VERSIONS_TO_CHECK="${BUILD_PYTHON}"
else
    VERSIONS_TO_CHECK=$(awk -F': ' '/^versions:/ {print $2}' "${REPO_ROOT}/scripts/python_versions.yaml")
fi

for VER in ${VERSIONS_TO_CHECK}; do
    SHORT=$(echo "$VER" | cut -d. -f1,2)
    ABI="cp${SHORT//.}-cp${SHORT//.}"
    for ARCH in x86_64 aarch64; do
        ls "${REPO_ROOT}/wheels/"*${ABI}*${ARCH}*.whl >/dev/null || {
            echo "ERROR: Missing Linux wheel for ${ABI} (${ARCH})!"
            exit 1
        }
    done
done

python -m twine check "${REPO_ROOT}/wheels/"*

if [[ "${PUBLISH_WHEELS}" == "true" ]]; then
    # Start the releasetool reporter
    python -m pip install --upgrade gcp-releasetool
    python -m releasetool publish-reporter-script > /tmp/publisher-script; source /tmp/publisher-script

    # Disable logging
    set +x
    TWINE_PASSWORD=$(cat "${KOKORO_KEYSTORE_DIR}/73713_google-cloud-pypi-token-keystore-3")
    python -m twine upload --skip-existing --username __token__ --password "${TWINE_PASSWORD}" "${REPO_ROOT}/wheels/"*
else
    echo "PUBLISH_WHEELS is not 'true'; skipping PyPI upload after twine check."
fi
