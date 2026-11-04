# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Repository-wide pytest configuration for google-cloud-storage tests."""

import os

_FORCE_FLAG = "--force-use-core-sdk"
_ENV_FORCE = "GOOGLE_CLOUD_STORAGE_FORCE_USE_CORE_SDK"


def pytest_addoption(parser):
    # `pytest ... --force-use-core-sdk` routes AsyncMultiRangeDownloader /
    # AsyncAppendableObjectWriter through the Rust Core SDK (gcs-core-server over a
    # Unix domain socket) and fails closed (CoreSdkUnavailableError) instead of ever
    # falling back to the pure-Python gRPC path. The SDK detects the flag from
    # sys.argv; registering it here only keeps pytest from rejecting it.
    parser.addoption(
        _FORCE_FLAG,
        action="store_true",
        default=False,
        dest="force_use_core_sdk",
        help="Use the Rust Core SDK (gRPC-over-UDS) backend with no GAPIC fallback.",
    )


def pytest_configure(config):
    if config.getoption("force_use_core_sdk", default=False):
        # Propagate to subprocesses / workers that do not see this process's argv.
        os.environ[_ENV_FORCE] = "1"
