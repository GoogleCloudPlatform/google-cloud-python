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
echo "BUILDING ON LINUX"
export BUILD_PYTHON=${BUILD_PYTHON}

MANYLINUX_DIR=$(echo $(cd $(dirname ${0}); pwd))
SCRIPTS_DIR=$(dirname ${MANYLINUX_DIR})
REPO_ROOT=$(dirname ${SCRIPTS_DIR})

cd $REPO_ROOT
# Add directory as safe to avoid "detected dubious ownership" fatal issue1
git config --global --add safe.directory '*'
git submodule update --init --recursive

docker pull quay.io/pypa/manylinux2014_x86_64
docker run \
    --rm \
    --interactive \
    --volume ${REPO_ROOT}:/var/code/python-crc32c/ \
    --env BUILD_PYTHON=${BUILD_PYTHON} \
    --env CRC32C_PURE_PYTHON=0 \
    quay.io/pypa/manylinux2014_x86_64 \
    /var/code/python-crc32c/scripts/manylinux/build_on_centos.sh

docker run --rm --privileged hypriot/qemu-register
docker pull quay.io/pypa/manylinux2014_aarch64
docker run \
    --rm \
    --interactive \
    --volume ${REPO_ROOT}:/var/code/python-crc32c/ \
    --env BUILD_PYTHON=${BUILD_PYTHON} \
    --env CRC32C_PURE_PYTHON=0 \
    quay.io/pypa/manylinux2014_aarch64 \
    /var/code/python-crc32c/scripts/manylinux/build_on_centos.sh

docker run \
    --rm \
    --interactive \
    --volume "${REPO_ROOT}:/var/code/python-crc32c/" \
    --env REPO_ROOT=/var/code/python-crc32c \
    --env BUILD_PYTHON \
    quay.io/pypa/manylinux2014_x86_64 \
    /var/code/python-crc32c/scripts/manylinux/publish_python_wheel.sh
