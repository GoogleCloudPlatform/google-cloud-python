# Copyright 2011 Google LLC
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

from datetime import datetime, timezone

import grpc
from google.api_core import exceptions
from test_utils import retry

from google.cloud import exceptions as core_exceptions

retry_429 = retry.RetryErrors(exceptions.TooManyRequests, max_tries=9)
retry_504 = retry.RetryErrors(exceptions.DeadlineExceeded)
retry_until_true = retry.RetryResult(lambda result: result)
retry_until_false = retry.RetryResult(lambda result: not result)


def _retry_on_unavailable(exc):
    """Retry only errors whose status code is 'UNAVAILABLE'."""
    return exc.code() == grpc.StatusCode.UNAVAILABLE


retry_grpc_unavailable = retry.RetryErrors(
    core_exceptions.GrpcRendezvous,
    error_predicate=_retry_on_unavailable,
    max_tries=9,
)


def label_stamp():
    return (
        datetime.now(timezone.utc).replace(microsecond=0).strftime("%Y-%m-%dt%H-%M-%S")
    )
