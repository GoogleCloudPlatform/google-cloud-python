# Copyright 2018 Google LLC
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

import unittest
from unittest import mock

import requests.exceptions


class Test_should_retry(unittest.TestCase):
    def _call_fut(self, exc):
        from google.cloud.bigquery.retry import _should_retry

        return _should_retry(exc)

    def test_wo_errors_attribute(self):
        self.assertFalse(self._call_fut(object()))

    def test_w_empty_errors(self):
        exc = mock.Mock(errors=[], spec=["errors"])
        self.assertFalse(self._call_fut(exc))

    def test_w_non_matching_reason(self):
        exc = mock.Mock(errors=[{"reason": "bogus"}], spec=["errors"])
        self.assertFalse(self._call_fut(exc))

    def test_w_backendError(self):
        exc = mock.Mock(errors=[{"reason": "backendError"}], spec=["errors"])
        self.assertTrue(self._call_fut(exc))

    def test_w_rateLimitExceeded(self):
        exc = mock.Mock(errors=[{"reason": "rateLimitExceeded"}], spec=["errors"])
        self.assertTrue(self._call_fut(exc))

    def test_w_unstructured_connectionerror(self):
        exc = ConnectionError()
        self.assertTrue(self._call_fut(exc))

    def test_w_unstructured_requests_connectionerror(self):
        exc = requests.exceptions.ConnectionError()
        self.assertTrue(self._call_fut(exc))

    def test_w_unstructured_requests_sslerror(self):
        exc = requests.exceptions.SSLError()
        self.assertFalse(self._call_fut(exc))

    def test_w_unstructured_requests_chunked_encoding_error(self):
        exc = requests.exceptions.ChunkedEncodingError()
        self.assertTrue(self._call_fut(exc))

    def test_w_unstructured_requests_connecttimeout(self):
        exc = requests.exceptions.ConnectTimeout()
        self.assertTrue(self._call_fut(exc))

    def test_w_unstructured_requests_readtimeout(self):
        exc = requests.exceptions.ReadTimeout()
        self.assertTrue(self._call_fut(exc))

    def test_w_unstructured_requests_timeout(self):
        exc = requests.exceptions.Timeout()
        self.assertTrue(self._call_fut(exc))

    def test_w_auth_transporterror(self):
        from google.auth.exceptions import TransportError

        exc = TransportError("testing")
        self.assertTrue(self._call_fut(exc))

    def test_w_unstructured_too_many_requests(self):
        from google.api_core.exceptions import TooManyRequests

        exc = TooManyRequests("testing")
        self.assertTrue(self._call_fut(exc))

    def test_w_unstructured_service_unavailable(self):
        from google.api_core.exceptions import ServiceUnavailable

        exc = ServiceUnavailable("testing")
        self.assertTrue(self._call_fut(exc))

    def test_w_internalError(self):
        exc = mock.Mock(errors=[{"reason": "internalError"}], spec=["errors"])
        self.assertTrue(self._call_fut(exc))

    def test_w_unstructured_internal_server_error(self):
        from google.api_core.exceptions import InternalServerError

        exc = InternalServerError("testing")
        self.assertTrue(self._call_fut(exc))

    def test_w_badGateway(self):
        exc = mock.Mock(errors=[{"reason": "badGateway"}], spec=["errors"])
        self.assertTrue(self._call_fut(exc))

    def test_w_unstructured_bad_gateway(self):
        from google.api_core.exceptions import BadGateway

        exc = BadGateway("testing")
        self.assertTrue(self._call_fut(exc))


def test_DEFAULT_JOB_RETRY_predicate():
    from google.cloud.bigquery.retry import DEFAULT_JOB_RETRY
    from google.api_core.exceptions import ClientError

    assert not DEFAULT_JOB_RETRY._predicate(TypeError())
    assert not DEFAULT_JOB_RETRY._predicate(ClientError("fail"))
    assert not DEFAULT_JOB_RETRY._predicate(
        ClientError("fail", errors=[dict(reason="idk")])
    )

    assert DEFAULT_JOB_RETRY._predicate(
        ClientError("fail", errors=[dict(reason="rateLimitExceeded")])
    )
    assert DEFAULT_JOB_RETRY._predicate(
        ClientError("fail", errors=[dict(reason="backendError")])
    )


def test_DEFAULT_JOB_RETRY_deadline():
    from google.cloud.bigquery.retry import DEFAULT_JOB_RETRY, DEFAULT_RETRY

    # Make sure we can retry the job at least once.
    assert DEFAULT_JOB_RETRY._deadline > DEFAULT_RETRY._deadline


def test_DEFAULT_JOB_RETRY_job_rate_limit_exceeded_retry_predicate():
    """Tests the retry predicate specifically for jobRateLimitExceeded."""
    from google.cloud.bigquery.retry import DEFAULT_JOB_RETRY
    from google.api_core.exceptions import ClientError

    # Non-ClientError exceptions should never trigger a retry
    assert not DEFAULT_JOB_RETRY._predicate(TypeError())

    # ClientError without specific reason shouldn't trigger a retry
    assert not DEFAULT_JOB_RETRY._predicate(ClientError("fail"))

    # ClientError with generic reason "idk" shouldn't trigger a retry
    assert not DEFAULT_JOB_RETRY._predicate(
        ClientError("fail", errors=[dict(reason="idk")])
    )

    # ClientError with reason "jobRateLimitExceeded" should trigger a retry
    assert DEFAULT_JOB_RETRY._predicate(
        ClientError("fail", errors=[dict(reason="jobRateLimitExceeded")])
    )

    # Other retryable reasons should still work as expected
    assert DEFAULT_JOB_RETRY._predicate(
        ClientError("fail", errors=[dict(reason="backendError")])
    )
