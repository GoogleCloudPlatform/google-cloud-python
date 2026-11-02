# Copyright 2017 Google LLC
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

import pytest

try:
    import grpc  # noqa: F401
except ImportError:
    pytest.skip("No GRPC", allow_module_level=True)

from google.api_core import exceptions
from google.api_core.gapic_v1 import config

INTERFACE_CONFIG = {
    "retry_codes": {
        "idempotent": ["DEADLINE_EXCEEDED", "UNAVAILABLE"],
        "other": ["FAILED_PRECONDITION"],
        "non_idempotent": [],
    },
    "retry_params": {
        "default": {
            "initial_retry_delay_millis": 1000,
            "retry_delay_multiplier": 2.5,
            "max_retry_delay_millis": 120000,
            "initial_rpc_timeout_millis": 120000,
            "rpc_timeout_multiplier": 1.0,
            "max_rpc_timeout_millis": 120000,
            "total_timeout_millis": 600000,
        },
        "other": {
            "initial_retry_delay_millis": 1000,
            "retry_delay_multiplier": 1,
            "max_retry_delay_millis": 1000,
            "initial_rpc_timeout_millis": 1000,
            "rpc_timeout_multiplier": 1,
            "max_rpc_timeout_millis": 1000,
            "total_timeout_millis": 1000,
        },
    },
    "methods": {
        "AnnotateVideo": {
            "timeout_millis": 60000,
            "retry_codes_name": "idempotent",
            "retry_params_name": "default",
        },
        "Other": {
            "timeout_millis": 60000,
            "retry_codes_name": "other",
            "retry_params_name": "other",
        },
        "Plain": {"timeout_millis": 30000},
    },
}


def test_create_method_configs():
    method_configs = config.parse_method_configs(INTERFACE_CONFIG)

    retry, timeout = method_configs["AnnotateVideo"]
    assert retry._predicate(exceptions.DeadlineExceeded(None))
    assert retry._predicate(exceptions.ServiceUnavailable(None))
    assert retry._initial == 1.0
    assert retry._multiplier == 2.5
    assert retry._maximum == 120.0
    assert retry._deadline == 600.0
    assert timeout._initial == 120.0
    assert timeout._multiplier == 1.0
    assert timeout._maximum == 120.0

    retry, timeout = method_configs["Other"]
    assert retry._predicate(exceptions.FailedPrecondition(None))
    assert retry._initial == 1.0
    assert retry._multiplier == 1.0
    assert retry._maximum == 1.0
    assert retry._deadline == 1.0
    assert timeout._initial == 1.0
    assert timeout._multiplier == 1.0
    assert timeout._maximum == 1.0

    retry, timeout = method_configs["Plain"]
    assert retry is None
    assert timeout._timeout == 30.0
