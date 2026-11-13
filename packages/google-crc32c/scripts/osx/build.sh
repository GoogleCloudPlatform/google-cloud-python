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
echo "BUILDING FOR OSX"

export CRC32C_PURE_PYTHON=0
# set deployment target
export MACOSX_DEPLOYMENT_TARGET=12

# ``readlink -f`` is not our friend on OS X. This relies on **some**
# ``python`` being installed.
SCRIPT_FI=$(python3 -c "import os; print(os.path.realpath('${0}'))")
OSX_DIR=$(dirname ${SCRIPT_FI})
SCRIPTS_DIR=$(dirname ${OSX_DIR})
export REPO_ROOT=$(dirname ${SCRIPTS_DIR})

# Build and install `libcrc32c`
export PY_BIN="python3"
export CRC32C_INSTALL_PREFIX="${REPO_ROOT}/usr"

cd ${REPO_ROOT}
# Add directory as safe to avoid "detected dubious ownership" fatal issue
git config --global --add safe.directory '*'
git submodule update --init --recursive

${OSX_DIR}/build_c_lib.sh

for VER in $(awk -F': ' '/^versions:/ {print $2}' "${SCRIPTS_DIR}/python_versions.yaml"); do
    PYTHON_VERSION=$(echo "$VER" | cut -d. -f1,2)
    echo "Build wheel for Python ${VER} (${PYTHON_VERSION})"
    export PY_VERSION="${VER}"
    export PY_BIN="${PYTHON_VERSION}"
    export PY_TAG="cp${PYTHON_VERSION//.}-cp${PYTHON_VERSION//.}"
    . /${OSX_DIR}/build_python_wheel.sh
done

. /${OSX_DIR}/publish_python_wheel.sh

# Clean up.
rm -fr ${CRC32C_INSTALL_PREFIX}
