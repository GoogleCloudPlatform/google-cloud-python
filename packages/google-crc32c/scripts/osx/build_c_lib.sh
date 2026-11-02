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

# Build and install `libcrc32c`

set -e -x

# Check that the install prefix is set. Exit early if the
# directory already exists.
if [[ -z "${CRC32C_INSTALL_PREFIX}" ]]; then
    echo "CRC32C_INSTALL_PREFIX environment variable should be set by the caller."
    exit 1
fi
if [[ -d "${CRC32C_INSTALL_PREFIX}" ]]; then
    echo "CRC32C_INSTALL_PREFIX=${CRC32C_INSTALL_PREFIX} already exists."
    exit 0
fi

# Check that the REPO_ROOT and PY_BIN environment variables are set.
if [[ -z "${REPO_ROOT}" ]]; then
    echo "REPO_ROOT environment variable should be set by the caller."
    exit 1
fi

if [[ -z "${PY_BIN}" ]]; then
    echo "PY_BIN environment variable should be set by the caller."
    exit 1
fi

# Precreate install directories for crc32 lib.
mkdir -p ${CRC32C_INSTALL_PREFIX}
mkdir -p ${CRC32C_INSTALL_PREFIX}/lib

# Create a virtualenv where we can install `cmake`.
VENV=${REPO_ROOT}/venv_build_libcrc32c
${PY_BIN} -m venv ${VENV}
${VENV}/bin/python -m pip install --upgrade pip
${VENV}/bin/python -m pip install "cmake >= 3.12.0"

# Build `libcrc32c`
cd ${REPO_ROOT}/google_crc32c
mkdir -p build
cd build
ls

# We don't build i386 anymore as XCode no longer supports.
${VENV}/bin/cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_OSX_DEPLOYMENT_TARGET=10.9 \
    -DCMAKE_OSX_ARCHITECTURES="x86_64;arm64" \
    -DCRC32C_BUILD_TESTS=no \
    -DCRC32C_BUILD_BENCHMARKS=no \
    -DBUILD_SHARED_LIBS=yes \
    -DCMAKE_INSTALL_PREFIX:PATH=${CRC32C_INSTALL_PREFIX} \
    -DCMAKE_INSTALL_NAME_DIR:PATH=${CRC32C_INSTALL_PREFIX}/lib \
    -DCMAKE_POLICY_VERSION_MINIMUM=3.12 \
    ..

# Install `libcrc32c` into CRC32C_INSTALL_PREFIX.
make all install

# Clean up.
cd ..
rm -fr ${REPO_ROOT}/google_crc32c/build
rm -fr ${VENV}
