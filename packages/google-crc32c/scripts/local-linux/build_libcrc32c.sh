#!/bin/bash
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

PY_BIN=${PY_BIN:-python3.9}
REPO_ROOT=${REPO_ROOT:-$(pwd)}

CRC32C_INSTALL_PREFIX=${REPO_ROOT}/usr

# NOTE: This assumes the local install has an up-to-date `pip`.
# Create a virtualenv where we can install `cmake`.
VENV=${REPO_ROOT}/venv
${PY_BIN} -m venv ${VENV}
${VENV}/bin/python -m pip install --upgrade setuptools pip wheel
${VENV}/bin/python -m pip install "cmake >= 3.12.0"
rm -rf ${REPO_ROOT}/build
rm -rf ${CRC32C_INSTALL_PREFIX}
# Build `libcrc32c`
cd ${REPO_ROOT}/google_crc32c
rm -rf build
mkdir build
cd build/
${VENV}/bin/cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCRC32C_BUILD_TESTS=no \
    -DCRC32C_BUILD_BENCHMARKS=no \
    -DBUILD_SHARED_LIBS=yes \
    -DCMAKE_INSTALL_PREFIX:PATH=${CRC32C_INSTALL_PREFIX} \
    ..
# Install `libcrc32c` into CRC32C_INSTALL_PREFIX.
make all install

cd ${REPO_ROOT}

${VENV}/bin/python setup.py build_ext \
    --include-dirs=${REPO_ROOT}/usr/include \
    --library-dirs=${REPO_ROOT}/usr/lib \
    --rpath=${REPO_ROOT}/usr/lib
${VENV}/bin/python -m pip wheel . --wheel-dir=wheels

# Clean up.
rm -fr ${REPO_ROOT}/google_crc32c/build
rm -fr ${VENV}
