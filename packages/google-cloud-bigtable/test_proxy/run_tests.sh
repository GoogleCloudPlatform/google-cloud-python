#!/bin/bash
# Copyright 2023 Google LLC
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

# attempt download golang if not found
if [[ ! -x "$(command -v go)" ]]; then
  echo "Downloading golang..."
  wget  https://go.dev/dl/go1.24.0.linux-amd64.tar.gz
  tar -xzf go1.24.0.linux-amd64.tar.gz
  export GOROOT=$(pwd)/go
  export PATH=$GOROOT/bin:$PATH
  export GOPATH=$HOME/go
  go version
fi

# ensure the working dir is the script's folder
SCRIPT_DIR=$(realpath $(dirname "$0"))
cd $SCRIPT_DIR

export PROXY_PORT=$(shuf -i 50000-60000 -n 1)

# download test suite
if [ ! -d "cloud-bigtable-clients-test" ]; then
  git clone https://github.com/googleapis/cloud-bigtable-clients-test.git
fi

# Build and start the proxy in a separate process
nohup python3 test_proxy.py --port $PROXY_PORT --client_type=$CLIENT_TYPE &
proxyPID=$!

# Kill proxy on exit
function cleanup() {
    echo "Cleanup testbench";
    kill $proxyPID
}
trap cleanup EXIT

# Run the conformance test
echo "running tests with args: $TEST_ARGS"
pushd cloud-bigtable-clients-test/tests
eval "go test -v -proxy_addr=:$PROXY_PORT $TEST_ARGS"
RETURN_CODE=$?
popd

echo "exiting with ${RETURN_CODE}"
exit ${RETURN_CODE}