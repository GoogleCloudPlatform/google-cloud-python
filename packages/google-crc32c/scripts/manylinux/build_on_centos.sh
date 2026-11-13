#!/bin/bash
# Copyright 2018 Google LLC
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

set -e -x
export CRC32C_PURE_PYTHON=0
MAIN_PYTHON_BIN="/opt/python/cp312-cp312/bin"
echo "BUILD_PYTHON: ${BUILD_PYTHON}"
REPO_ROOT=/var/code/python-crc32c/

# Install `openssl-devel` so that `cmake` can be built.
yum install -y openssl-devel

# Upgrade `pip` before using it.
${MAIN_PYTHON_BIN}/python -m pip install --upgrade pip
# Install `cmake` (i.e. non-Python build dependency).
${MAIN_PYTHON_BIN}/python -m pip install "cmake >= 3.12.0"
# Install Python build dependencies.
${MAIN_PYTHON_BIN}/python -m pip install \
    --requirement ${REPO_ROOT}/scripts/dev-requirements.txt

# Build and install `crc32c`
cd ${REPO_ROOT}/google_crc32c/
rm -rf build
mkdir build
cd build/
cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCRC32C_BUILD_TESTS=no \
    -DCRC32C_BUILD_BENCHMARKS=no \
    -DBUILD_SHARED_LIBS=yes \
    -DCMAKE_POLICY_VERSION_MINIMUM=3.12 \
    ..
make all install

PYTHON_VERSIONS=""
if [[ -z ${BUILD_PYTHON} ]]; then
    for VER in $(awk -F': ' '/^versions:/ {print $2}' "${REPO_ROOT}/scripts/python_versions.yaml"); do
        SHORT=$(echo "$VER" | cut -d. -f1,2)
        ABI="cp${SHORT//.}-cp${SHORT//.}"
        PYTHON_BIN="/opt/python/${ABI}/bin"
        if [[ -d "${PYTHON_BIN}" ]]; then
            PYTHON_VERSIONS="${PYTHON_VERSIONS} ${PYTHON_BIN}"
        else
            echo "ERROR: Required Python version ${VER} (${PYTHON_BIN}) not found in container."
            exit 1
        fi
    done
else
    STRIPPED_PYTHON=$(echo ${BUILD_PYTHON} | sed -e "s/\.//g" | sed -e "s/-dev$//")
    PYTHON_BIN="/opt/python/cp${STRIPPED_PYTHON}-cp${STRIPPED_PYTHON}/bin"
    if [[ -d "${PYTHON_BIN}" ]]; then
        PYTHON_VERSIONS="${PYTHON_BIN}"
    else
        echo "ERROR: Requested BUILD_PYTHON ${BUILD_PYTHON} (${PYTHON_BIN}) not found in container."
        exit 1
    fi
fi

# Build the wheels.
cd ${REPO_ROOT}
for PYTHON_BIN in ${PYTHON_VERSIONS}; do
    ${PYTHON_BIN}/python -m pip install --upgrade pip
    ${PYTHON_BIN}/python -m pip install \
        --requirement ${REPO_ROOT}/scripts/dev-requirements.txt
    ${PYTHON_BIN}/python -m pip wheel . --wheel-dir dist_wheels/
done

# Bundle external shared libraries into the wheels
for whl in dist_wheels/google_crc32c*.whl; do
    "${MAIN_PYTHON_BIN}/auditwheel" repair "${whl}" --wheel-dir wheels/
done

# Install and test wheels
for PYTHON_BIN in ${PYTHON_VERSIONS}; do
    # Get the ABI tag from the Python binary's path, e.g., "cp310-cp310"
    ABI_TAG=$(basename $(dirname ${PYTHON_BIN}))
    ARCH=$(uname -m)
    # Create a virtual environment to install and test the wheel
    ${PYTHON_BIN}/python -m venv /tmp/venv

    # Find the correct wheel file using the precise ABI tag and architecture.
    WHEEL_FILE=$(ls ${REPO_ROOT}/wheels/google_crc32c-*-${ABI_TAG}-*manylinux*${ARCH}*.whl)
    # Install the wheel and pytest
    /tmp/venv/bin/pip install "${WHEEL_FILE}" pytest

    # Verify that the module is installed and peek at contents.
    /tmp/venv/bin/python ${REPO_ROOT}/scripts/check_crc32c_extension.py
    /tmp/venv/bin/pytest ${REPO_ROOT}/tests --junitxml="${REPO_ROOT}/${ABI_TAG}_${ARCH}_sponge_log.xml"

    # Clean up the virtual environment
    rm -rf /tmp/venv
done

# Clean up.
rm -fr ${REPO_ROOT}/google_crc32c/build/
rm -fr ${REPO_ROOT}/dist_wheels/
