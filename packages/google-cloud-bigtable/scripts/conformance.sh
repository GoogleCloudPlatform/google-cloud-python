#!/bin/bash

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

set -eo pipefail

## cd to the parent directory, i.e. the root of the git repo
cd $(dirname $0)/..

# Build and start the proxy in a separate process
pushd test_proxy
nohup python test_proxy.py --port $PROXY_PORT --client_type=$CLIENT_TYPE &
proxyPID=$!
popd

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
