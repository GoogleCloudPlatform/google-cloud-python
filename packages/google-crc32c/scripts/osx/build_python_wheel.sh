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

# Build a **single** Python wheel for a specified version. The version and
# associated paths should be set as environment variables; the expected
# environment variables will be verified below.

set -e -x

# Check that the REPO_ROOT, PY_BIN and PY_TAG environment variables are set.
if [[ -z "${REPO_ROOT}" ]]; then
    echo "REPO_ROOT environment variable should be set by the caller."
    exit 1
fi
if [[ -z "${PY_BIN}" ]]; then
    echo "PY_BIN environment variable should be set by the caller."
    exit 1
fi
if [[ -z "${PY_TAG}" ]]; then
    echo "PY_TAG environment variable should be set by the caller."
    exit 1
fi

if [[ -z "${PY_VERSION}" ]]; then
    echo "PY_VERSION environment variable should be set by the caller."
    exit 1
fi

# Install the official python.org universal2 build if it isn't already present.
# These are pre-compiled, so (unlike pyenv) we never build CPython from source,
# and they are configured with a macOS 11 deployment target, which keeps our
# wheels compatible with older macOS releases.
PYTHON_EXE="/Library/Frameworks/Python.framework/Versions/${PY_BIN}/bin/python${PY_BIN}"
if [[ ! -x "${PYTHON_EXE}" ]]; then
    if command -v "python${PY_BIN}" >/dev/null 2>&1; then
        PYTHON_EXE=$(command -v "python${PY_BIN}")
    else
        PKG_NAME="python-${PY_VERSION}-macos11.pkg"
        # Pre-releases (a1/b1/rc1) are placed under the base version directory on python.org (e.g. 3.15.0a1 -> 3.15.0)
        FTP_DIR="${PY_VERSION%%[a-z]*}"
        echo "Installing Python ${PY_VERSION} from python.org (${PKG_NAME})..."
        curl --fail --show-error --location --retry 5 --retry-delay 5 --retry-all-errors \
            --output "/tmp/${PKG_NAME}" \
            "https://www.python.org/ftp/python/${FTP_DIR}/${PKG_NAME}"
        sudo installer -pkg "/tmp/${PKG_NAME}" -target /
        rm -f "/tmp/${PKG_NAME}"
    fi
fi
"${PYTHON_EXE}" --version

# The python.org builds are universal2. Pin the build to the host architecture so
# we keep publishing separate x86_64 and arm64 wheels (one per Kokoro macOS job)
# rather than two identical universal2 wheels.
ARCH=$(uname -m)
export ARCHFLAGS="-arch ${ARCH}"
export _PYTHON_HOST_PLATFORM="macosx-${MACOSX_DEPLOYMENT_TARGET}.0-${ARCH}"

# Rely on the REPO_ROOT already provided by the parent script
OSX_DIR="${REPO_ROOT}/scripts/osx"

# Create a virtualenv where we can install Python build dependencies.
VENV=${REPO_ROOT}/venv${PY_BIN}
"${PYTHON_EXE}" -m venv ${VENV}

${VENV}/bin/python -m pip install --upgrade pip
${VENV}/bin/python -m pip install \
    --requirement ${REPO_ROOT}/scripts/dev-requirements.txt

# Create the wheel.
DIST_WHEELS="${REPO_ROOT}/dist_wheels"
mkdir -p ${DIST_WHEELS}
cd ${REPO_ROOT}
${VENV}/bin/python setup.py build_ext \
    --include-dirs=${REPO_ROOT}/usr/include \
    --library-dirs=${REPO_ROOT}/usr/lib \
    --rpath=${REPO_ROOT}/usr/lib
${VENV}/bin/python -m pip wheel ${REPO_ROOT} --wheel-dir ${DIST_WHEELS}

# Delocate the wheel.
FIXED_WHEELS="${REPO_ROOT}/wheels"
mkdir -p ${FIXED_WHEELS}
${VENV}/bin/delocate-wheel \
    --wheel-dir ${FIXED_WHEELS} \
    --verbose \
    --check-archs \
    ${DIST_WHEELS}/google_crc32c*${PY_TAG}*.whl

# test wheel
${VENV}/bin/pip install \
  --no-index --find-links=${REPO_ROOT}/wheels google-crc32c --force-reinstall
${VENV}/bin/pip install pytest
${VENV}/bin/py.test ${REPO_ROOT}/tests --junitxml="${REPO_ROOT}/${PY_TAG}_sponge_log.xml"
${VENV}/bin/python ${REPO_ROOT}/scripts/check_crc32c_extension.py

ls ${REPO_ROOT}/wheels/

# Clean up.
rm -fr ${DIST_WHEELS}
rm -fr ${VENV}
