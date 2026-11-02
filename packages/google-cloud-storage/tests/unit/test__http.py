# Copyright 2014 Google LLC
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
from unittest.mock import patch

import mock

from google.cloud.storage import _helpers

GCCL_INVOCATION_TEST_CONST = "gccl-invocation-id/test-invocation-123"


class TestConnection(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.storage._http import Connection

        return Connection

    def _make_one(self, *args, **kw):
        if "api_endpoint" not in kw:
            kw["api_endpoint"] = "https://storage.googleapis.com"
        return self._get_target_class()(*args, **kw)

    def test_extra_headers(self):
        import requests

        from google.cloud import _http as base_http
        from google.cloud.storage.constants import _DEFAULT_TIMEOUT

        http = mock.create_autospec(requests.Session, instance=True)
        response = requests.Response()
        response.status_code = 200
        data = b"brent-spiner"
        response._content = data
        http.request.return_value = response
        client = mock.Mock(_http=http, spec=["_http"])

        conn = self._make_one(client)
        req_data = "hey-yoooouuuuu-guuuuuyyssss"
        with patch.object(
            _helpers, "_get_invocation_id", return_value=GCCL_INVOCATION_TEST_CONST
        ):
            result = conn.api_request(
                "GET", "/rainbow", data=req_data, expect_json=False
            )
        self.assertEqual(result, data)

        expected_headers = {
            "Accept-Encoding": "gzip",
            base_http.CLIENT_INFO_HEADER: f"{conn.user_agent} {GCCL_INVOCATION_TEST_CONST}",
            "User-Agent": conn.user_agent,
        }
        expected_uri = conn.build_api_url("/rainbow")
        http.request.assert_called_once_with(
            data=req_data,
            headers=expected_headers,
            method="GET",
            url=expected_uri,
            timeout=_DEFAULT_TIMEOUT,
        )

    def test_metadata_op_has_client_custom_headers(self):
        import google.auth.credentials
        import requests

        from google.cloud import _http as base_http
        from google.cloud.storage import Client
        from google.cloud.storage.constants import _DEFAULT_TIMEOUT

        custom_headers = {
            "x-goog-custom-audit-foo": "bar",
            "x-goog-custom-audit-user": "baz",
        }
        http = mock.create_autospec(requests.Session, instance=True)
        response = requests.Response()
        response.status_code = 200
        data = b"brent-spiner"
        response._content = data
        http.is_mtls = False
        http.request.return_value = response
        credentials = mock.Mock(
            spec=google.auth.credentials.Credentials,
            universe_domain=_helpers._DEFAULT_UNIVERSE_DOMAIN,
        )
        client = Client(
            project="project",
            credentials=credentials,
            _http=http,
            extra_headers=custom_headers,
        )
        req_data = "hey-yoooouuuuu-guuuuuyyssss"
        with patch.object(
            _helpers, "_get_invocation_id", return_value=GCCL_INVOCATION_TEST_CONST
        ):
            result = client._connection.api_request(
                "GET", "/rainbow", data=req_data, expect_json=False
            )
        self.assertEqual(result, data)

        expected_headers = {
            **custom_headers,
            "Accept-Encoding": "gzip",
            base_http.CLIENT_INFO_HEADER: f"{client._connection.user_agent} {GCCL_INVOCATION_TEST_CONST}",
            "User-Agent": client._connection.user_agent,
        }
        expected_uri = client._connection.build_api_url("/rainbow")
        http.request.assert_called_once_with(
            data=req_data,
            headers=expected_headers,
            method="GET",
            url=expected_uri,
            timeout=_DEFAULT_TIMEOUT,
        )

    def test_build_api_url_no_extra_query_params(self):
        from urllib.parse import parse_qsl, urlsplit

        conn = self._make_one(object())
        uri = conn.build_api_url("/foo")
        scheme, netloc, path, qs, _ = urlsplit(uri)
        self.assertEqual(f"{scheme}://{netloc}", conn.API_BASE_URL)
        self.assertEqual(path, "/".join(["", "storage", conn.API_VERSION, "foo"]))
        parms = dict(parse_qsl(qs))
        pretty_print = parms.pop("prettyPrint", "false")
        self.assertEqual(pretty_print, "false")
        self.assertEqual(parms, {})

    def test_build_api_url_w_custom_endpoint(self):
        from urllib.parse import parse_qsl, urlsplit

        custom_endpoint = "https://foo-storage.googleapis.com"
        conn = self._make_one(object(), api_endpoint=custom_endpoint)
        uri = conn.build_api_url("/foo")
        scheme, netloc, path, qs, _ = urlsplit(uri)
        self.assertEqual(f"{scheme}://{netloc}", custom_endpoint)
        self.assertEqual(path, "/".join(["", "storage", conn.API_VERSION, "foo"]))
        parms = dict(parse_qsl(qs))
        pretty_print = parms.pop("prettyPrint", "false")
        self.assertEqual(pretty_print, "false")
        self.assertEqual(parms, {})

    def test_build_api_url_w_extra_query_params(self):
        from urllib.parse import parse_qsl, urlsplit

        conn = self._make_one(object())
        uri = conn.build_api_url("/foo", {"bar": "baz"})
        scheme, netloc, path, qs, _ = urlsplit(uri)
        self.assertEqual(f"{scheme}://{netloc}", conn.API_BASE_URL)
        self.assertEqual(path, "/".join(["", "storage", conn.API_VERSION, "foo"]))
        parms = dict(parse_qsl(qs))
        self.assertEqual(parms["bar"], "baz")

    def test_api_request_no_retry(self):
        import requests

        http = mock.create_autospec(requests.Session, instance=True)
        client = mock.Mock(_http=http, spec=["_http"])

        conn = self._make_one(client)
        response = requests.Response()
        response.status_code = 200
        data = b"brent-spiner"
        response._content = data
        http.request.return_value = response

        req_data = "hey-yoooouuuuu-guuuuuyyssss"
        conn.api_request("GET", "/rainbow", data=req_data, expect_json=False)
        http.request.assert_called_once()

    def test_api_request_basic_retry(self):
        # For this test, the "retry" function will just short-circuit.
        FAKE_RESPONSE_STRING = "fake_response"

        def retry(_):
            def fake_response():
                return FAKE_RESPONSE_STRING

            return fake_response

        import requests

        http = mock.create_autospec(requests.Session, instance=True)
        client = mock.Mock(_http=http, spec=["_http"])

        # Some of this is unnecessary if the test succeeds, but we'll leave it
        # to ensure a failure produces a less confusing error message.
        conn = self._make_one(client)
        response = requests.Response()
        response.status_code = 200
        data = b"brent-spiner"
        response._content = data
        http.request.return_value = response

        req_data = "hey-yoooouuuuu-guuuuuyyssss"
        result = conn.api_request(
            "GET", "/rainbow", data=req_data, expect_json=False, retry=retry
        )
        http.request.assert_not_called()
        self.assertEqual(result, FAKE_RESPONSE_STRING)

    def test_api_request_conditional_retry(self):
        # For this test, the "retry" function will short-circuit.
        FAKE_RESPONSE_STRING = "fake_response"

        def retry(_):
            def fake_response():
                return FAKE_RESPONSE_STRING

            return fake_response

        conditional_retry_mock = mock.MagicMock()
        conditional_retry_mock.get_retry_policy_if_conditions_met.return_value = retry

        import requests

        http = mock.create_autospec(requests.Session, instance=True)
        client = mock.Mock(_http=http, spec=["_http"])

        # Some of this is unnecessary if the test succeeds, but we'll leave it
        # to ensure a failure produces a less confusing error message.
        conn = self._make_one(client)
        response = requests.Response()
        response.status_code = 200
        data = b"brent-spiner"
        response._content = data
        http.request.return_value = response

        req_data = "hey-yoooouuuuu-guuuuuyyssss"
        result = conn.api_request(
            "GET",
            "/rainbow",
            data=req_data,
            expect_json=False,
            retry=conditional_retry_mock,
        )
        http.request.assert_not_called()
        self.assertEqual(result, FAKE_RESPONSE_STRING)

    def test_api_request_conditional_retry_failed(self):
        conditional_retry_mock = mock.MagicMock()
        conditional_retry_mock.get_retry_policy_if_conditions_met.return_value = None

        import requests

        http = mock.create_autospec(requests.Session, instance=True)
        client = mock.Mock(_http=http, spec=["_http"])

        # Some of this is unnecessary if the test succeeds, but we'll leave it
        # to ensure a failure produces a less confusing error message.
        conn = self._make_one(client)
        response = requests.Response()
        response.status_code = 200
        data = b"brent-spiner"
        response._content = data
        http.request.return_value = response

        req_data = "hey-yoooouuuuu-guuuuuyyssss"
        conn.api_request(
            "GET",
            "/rainbow",
            data=req_data,
            expect_json=False,
            retry=conditional_retry_mock,
        )
        http.request.assert_called_once()

    def test_mtls(self):
        client = object()

        conn = self._make_one(client, api_endpoint=None)
        self.assertEqual(conn.ALLOW_AUTO_SWITCH_TO_MTLS_URL, True)
        self.assertEqual(conn.API_BASE_URL, "https://storage.googleapis.com")
        self.assertEqual(conn.API_BASE_MTLS_URL, "https://storage.mtls.googleapis.com")

        conn = self._make_one(client, api_endpoint="http://foo")
        self.assertEqual(conn.ALLOW_AUTO_SWITCH_TO_MTLS_URL, False)
        self.assertEqual(conn.API_BASE_URL, "http://foo")
        self.assertEqual(conn.API_BASE_MTLS_URL, "https://storage.mtls.googleapis.com")

    def test_duplicate_user_agent(self):
        # Regression test for issue #565
        from google.cloud._http import ClientInfo

        from google.cloud.storage import __version__
        from google.cloud.storage.batch import Batch

        client_info = ClientInfo(user_agent="test/123")
        conn = self._make_one(object(), client_info=client_info)
        expected_user_agent = f"test/123 gcloud-python/{__version__} "
        self.assertEqual(conn._client_info.user_agent, expected_user_agent)

        client = mock.Mock(_connection=conn, spec=["_connection"])
        batch = Batch(client)
        self.assertEqual(batch._client_info.user_agent, expected_user_agent)
