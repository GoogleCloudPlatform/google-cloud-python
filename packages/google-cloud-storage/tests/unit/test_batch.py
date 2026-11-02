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

import http.client
import unittest
from http.client import NO_CONTENT, SERVICE_UNAVAILABLE

import mock
import requests

from google.cloud.storage._helpers import _DEFAULT_UNIVERSE_DOMAIN


def _make_credentials():
    import google.auth.credentials

    return mock.Mock(
        spec=google.auth.credentials.Credentials,
        universe_domain=_DEFAULT_UNIVERSE_DOMAIN,
    )


def _make_response(status=http.client.OK, content=b"", headers={}):
    response = requests.Response()
    response.status_code = status
    response._content = content
    response.headers = headers
    response.request = requests.Request()
    return response


def _make_requests_session(responses):
    session = mock.create_autospec(requests.Session, instance=True)
    session.request.side_effect = responses
    return session


class TestMIMEApplicationHTTP(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.storage.batch import MIMEApplicationHTTP

        return MIMEApplicationHTTP

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor_body_None(self):
        METHOD = "DELETE"
        PATH = "/path/to/api"
        LINES = ["DELETE /path/to/api HTTP/1.1", ""]
        mah = self._make_one(METHOD, PATH, {}, None)
        self.assertEqual(mah.get_content_type(), "application/http")
        self.assertEqual(mah.get_payload().splitlines(), LINES)

    def test_ctor_body_str(self):
        METHOD = "GET"
        PATH = "/path/to/api"
        BODY = "ABC"
        HEADERS = {"Content-Length": len(BODY), "Content-Type": "text/plain"}
        LINES = [
            "GET /path/to/api HTTP/1.1",
            "Content-Length: 3",
            "Content-Type: text/plain",
            "",
            "ABC",
        ]
        mah = self._make_one(METHOD, PATH, HEADERS, BODY)
        self.assertEqual(mah.get_payload().splitlines(), LINES)

    def test_ctor_body_dict(self):
        METHOD = "GET"
        PATH = "/path/to/api"
        BODY = {"foo": "bar"}
        HEADERS = {}
        LINES = [
            "GET /path/to/api HTTP/1.1",
            "Content-Length: 14",
            "Content-Type: application/json",
            "",
            '{"foo": "bar"}',
        ]
        mah = self._make_one(METHOD, PATH, HEADERS, BODY)
        self.assertEqual(mah.get_payload().splitlines(), LINES)


class TestBatch(unittest.TestCase):
    @staticmethod
    def _get_default_timeout():
        from google.cloud.storage.constants import _DEFAULT_TIMEOUT

        return _DEFAULT_TIMEOUT

    @staticmethod
    def _get_target_class():
        from google.cloud.storage.batch import Batch

        return Batch

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor(self):
        http = _make_requests_session([])
        connection = _Connection(http=http)
        client = _Client(connection)
        batch = self._make_one(client)
        self.assertIs(batch._client, client)
        self.assertEqual(len(batch._requests), 0)
        self.assertEqual(len(batch._target_objects), 0)

    def test_current(self):
        from google.cloud.storage.client import Client

        project = "PROJECT"
        credentials = _make_credentials()
        client = Client(project=project, credentials=credentials)
        batch1 = self._make_one(client)
        self.assertIsNone(batch1.current())

        client._push_batch(batch1)
        self.assertIs(batch1.current(), batch1)

        batch2 = self._make_one(client)
        client._push_batch(batch2)
        self.assertIs(batch1.current(), batch2)

    def test__make_request_GET_normal(self):
        from google.cloud.storage.batch import _FutureDict

        url = "http://example.com/api"
        http = _make_requests_session([])
        connection = _Connection(http=http)
        client = _Client(connection)
        batch = self._make_one(client)
        target = _MockObject()

        response = batch._make_request("GET", url, target_object=target)

        # Check the respone
        self.assertEqual(response.status_code, 204)
        self.assertIsInstance(response.json(), _FutureDict)
        self.assertIsInstance(response.content, _FutureDict)
        self.assertIs(target._properties, response.content)

        # The real http request should not have been called yet.
        http.request.assert_not_called()

        # Check the queued request
        self.assertEqual(len(batch._requests), 1)
        request = batch._requests[0]
        request_method, request_url, _, request_data, _ = request
        self.assertEqual(request_method, "GET")
        self.assertEqual(request_url, url)
        self.assertIsNone(request_data)

    def test__make_request_POST_normal(self):
        from google.cloud.storage.batch import _FutureDict

        url = "http://example.com/api"
        http = _make_requests_session([])
        connection = _Connection(http=http)
        client = _Client(connection)
        batch = self._make_one(client)
        data = {"foo": 1}
        target = _MockObject()

        response = batch._make_request(
            "POST", url, data={"foo": 1}, target_object=target
        )

        self.assertEqual(response.status_code, 204)
        self.assertIsInstance(response.content, _FutureDict)
        self.assertIs(target._properties, response.content)

        # The real http request should not have been called yet.
        http.request.assert_not_called()

        request = batch._requests[0]
        request_method, request_url, _, request_data, _ = request
        self.assertEqual(request_method, "POST")
        self.assertEqual(request_url, url)
        self.assertEqual(request_data, data)

    def test__make_request_PATCH_normal(self):
        from google.cloud.storage.batch import _FutureDict

        url = "http://example.com/api"
        http = _make_requests_session([])
        connection = _Connection(http=http)
        client = _Client(connection)
        batch = self._make_one(client)
        data = {"foo": 1}
        target = _MockObject()

        response = batch._make_request(
            "PATCH", url, data={"foo": 1}, target_object=target
        )

        self.assertEqual(response.status_code, 204)
        self.assertIsInstance(response.content, _FutureDict)
        self.assertIs(target._properties, response.content)

        # The real http request should not have been called yet.
        http.request.assert_not_called()

        request = batch._requests[0]
        request_method, request_url, _, request_data, _ = request
        self.assertEqual(request_method, "PATCH")
        self.assertEqual(request_url, url)
        self.assertEqual(request_data, data)

    def test__make_request_DELETE_normal(self):
        from google.cloud.storage.batch import _FutureDict

        url = "http://example.com/api"
        http = _make_requests_session([])
        connection = _Connection(http=http)
        client = _Client(connection)
        batch = self._make_one(client)
        target = _MockObject()

        response = batch._make_request("DELETE", url, target_object=target)

        # Check the respone
        self.assertEqual(response.status_code, 204)
        self.assertIsInstance(response.content, _FutureDict)
        self.assertIs(target._properties, response.content)

        # The real http request should not have been called yet.
        http.request.assert_not_called()

        # Check the queued request
        self.assertEqual(len(batch._requests), 1)
        request = batch._requests[0]
        request_method, request_url, _, request_data, _ = request
        self.assertEqual(request_method, "DELETE")
        self.assertEqual(request_url, url)
        self.assertIsNone(request_data)

    def test__make_request_POST_too_many_requests(self):
        url = "http://example.com/api"
        http = _make_requests_session([])
        connection = _Connection(http=http)
        client = _Client(connection)
        batch = self._make_one(client)

        batch._MAX_BATCH_SIZE = 1
        batch._requests.append(("POST", url, {}, {"bar": 2}))

        with self.assertRaises(ValueError):
            batch._make_request("POST", url, data={"foo": 1})

    def test_finish_empty(self):
        http = _make_requests_session([])
        connection = _Connection(http=http)
        client = _Client(connection)
        batch = self._make_one(client)

        with self.assertRaises(ValueError):
            batch.finish()

    def _get_payload_chunks(self, boundary, payload):
        divider = "--" + boundary[len('boundary="') : -1]
        chunks = payload.split(divider)[1:-1]  # discard prolog / epilog
        return chunks

    def _check_subrequest_no_payload(self, chunk, method, url):
        lines = chunk.splitlines()
        # blank + 2 headers + blank + request + blank + blank
        self.assertEqual(len(lines), 7)
        self.assertEqual(lines[0], "")
        self.assertEqual(lines[1], "Content-Type: application/http")
        self.assertEqual(lines[2], "MIME-Version: 1.0")
        self.assertEqual(lines[3], "")
        self.assertEqual(lines[4], f"{method} {url} HTTP/1.1")
        self.assertEqual(lines[5], "")
        self.assertEqual(lines[6], "")

    def _check_subrequest_payload(self, chunk, method, url, payload):
        import json

        lines = chunk.splitlines()
        # blank + 2 headers + blank + request + 2 headers + blank + body
        payload_str = json.dumps(payload)
        self.assertEqual(lines[0], "")
        self.assertEqual(lines[1], "Content-Type: application/http")
        self.assertEqual(lines[2], "MIME-Version: 1.0")
        self.assertEqual(lines[3], "")
        self.assertEqual(lines[4], f"{method} {url} HTTP/1.1")
        if method == "GET":
            self.assertEqual(len(lines), 7)
            self.assertEqual(lines[5], "")
            self.assertEqual(lines[6], "")
        else:
            self.assertEqual(len(lines), 9)
            self.assertEqual(lines[5], f"Content-Length: {len(payload_str)}")
            self.assertEqual(lines[6], "Content-Type: application/json")
            self.assertEqual(lines[7], "")
            self.assertEqual(json.loads(lines[8]), payload)

    def _get_mutlipart_request(self, http):
        request_call = http.request.mock_calls[0][2]
        request_headers = request_call["headers"]
        request_body = request_call["data"]
        content_type, boundary = [
            value.strip() for value in request_headers["Content-Type"].split(";")
        ]

        return request_headers, request_body, content_type, boundary

    def test_finish_nonempty(self):
        url = "http://api.example.com/other_api"
        expected_response = _make_response(
            content=_THREE_PART_MIME_RESPONSE,
            headers={"content-type": 'multipart/mixed; boundary="DEADBEEF="'},
        )
        http = _make_requests_session([expected_response])
        connection = _Connection(http=http)
        client = _Client(connection)
        batch = self._make_one(client)
        batch.API_BASE_URL = "http://api.example.com"

        batch._do_request("POST", url, {}, {"foo": 1, "bar": 2}, None)
        batch._do_request("PATCH", url, {}, {"bar": 3}, None)
        batch._do_request("DELETE", url, {}, None, None)
        result = batch.finish()

        self.assertEqual(len(result), len(batch._requests))
        self.assertEqual(len(result), len(batch._responses))

        response1, response2, response3 = result

        self.assertEqual(
            response1.headers,
            {"Content-Length": "20", "Content-Type": "application/json; charset=UTF-8"},
        )
        self.assertEqual(response1.json(), {"foo": 1, "bar": 2})

        self.assertEqual(
            response2.headers,
            {"Content-Length": "20", "Content-Type": "application/json; charset=UTF-8"},
        )
        self.assertEqual(response2.json(), {"foo": 1, "bar": 3})

        self.assertEqual(response3.headers, {"Content-Length": "0"})
        self.assertEqual(response3.status_code, NO_CONTENT)

        expected_url = f"{batch.API_BASE_URL}/batch/storage/v1"
        http.request.assert_called_once_with(
            method="POST",
            url=expected_url,
            headers=mock.ANY,
            data=mock.ANY,
            timeout=self._get_default_timeout(),
        )

        request_info = self._get_mutlipart_request(http)
        request_headers, request_body, content_type, boundary = request_info

        self.assertEqual(content_type, "multipart/mixed")
        self.assertTrue(boundary.startswith('boundary="=='))
        self.assertTrue(boundary.endswith('=="'))
        self.assertEqual(request_headers["MIME-Version"], "1.0")

        chunks = self._get_payload_chunks(boundary, request_body)
        self.assertEqual(len(chunks), 3)
        self._check_subrequest_payload(chunks[0], "POST", url, {"foo": 1, "bar": 2})
        self._check_subrequest_payload(chunks[1], "PATCH", url, {"bar": 3})
        self._check_subrequest_no_payload(chunks[2], "DELETE", url)

    def test_finish_responses_mismatch(self):
        url = "http://api.example.com/other_api"
        expected_response = _make_response(
            content=_TWO_PART_MIME_RESPONSE_WITH_FAIL,
            headers={"content-type": 'multipart/mixed; boundary="DEADBEEF="'},
        )
        http = _make_requests_session([expected_response])
        connection = _Connection(http=http)
        client = _Client(connection)
        batch = self._make_one(client)
        batch.API_BASE_URL = "http://api.example.com"

        batch._requests.append(("GET", url, {}, None))
        with self.assertRaises(ValueError):
            batch.finish()

    def test_finish_nonempty_with_status_failure(self):
        from google.cloud.exceptions import NotFound

        url = "http://api.example.com/other_api"
        expected_response = _make_response(
            content=_TWO_PART_MIME_RESPONSE_WITH_FAIL,
            headers={"content-type": 'multipart/mixed; boundary="DEADBEEF="'},
        )
        http = _make_requests_session([expected_response])
        connection = _Connection(http=http)
        client = _Client(connection)
        batch = self._make_one(client)
        batch.API_BASE_URL = "http://api.example.com"
        target1 = _MockObject()
        target2 = _MockObject()

        batch._do_request("GET", url, {}, None, target1, timeout=42)
        batch._do_request("GET", url, {}, None, target2, timeout=420)

        # Make sure futures are not populated.
        self.assertEqual(
            [future for future in batch._target_objects], [target1, target2]
        )
        target2_future_before = target2._properties

        with self.assertRaises(NotFound):
            batch.finish()

        self.assertEqual(target1._properties, {"foo": 1, "bar": 2})
        self.assertIs(target2._properties, target2_future_before)

        expected_url = f"{batch.API_BASE_URL}/batch/storage/v1"
        http.request.assert_called_once_with(
            method="POST",
            url=expected_url,
            headers=mock.ANY,
            data=mock.ANY,
            timeout=420,  # the last request timeout prevails
        )

        _, request_body, _, boundary = self._get_mutlipart_request(http)

        chunks = self._get_payload_chunks(boundary, request_body)
        self.assertEqual(len(chunks), 2)
        self._check_subrequest_payload(chunks[0], "GET", url, {})
        self._check_subrequest_payload(chunks[1], "GET", url, {})

    def test_finish_no_raise_exception(self):
        url = "http://api.example.com/other_api"
        expected_response = _make_response(
            content=_TWO_PART_MIME_RESPONSE_WITH_FAIL,
            headers={"content-type": 'multipart/mixed; boundary="DEADBEEF="'},
        )
        http = _make_requests_session([expected_response])
        connection = _Connection(http=http)
        client = _Client(connection)
        batch = self._make_one(client)
        batch.API_BASE_URL = "http://api.example.com"
        target1 = _MockObject()
        target2 = _MockObject()

        batch._do_request("GET", url, {}, None, target1, timeout=42)
        batch._do_request("GET", url, {}, None, target2, timeout=420)

        # Make sure futures are not populated.
        self.assertEqual(
            [future for future in batch._target_objects], [target1, target2]
        )

        batch.finish(raise_exception=False)

        self.assertEqual(len(batch._requests), 2)
        self.assertEqual(len(batch._responses), 2)

        # Make sure NotFound exception is added to responses and target2
        self.assertEqual(target1._properties, {"foo": 1, "bar": 2})
        self.assertEqual(target2._properties, {"error": {"message": "Not Found"}})

        expected_url = f"{batch.API_BASE_URL}/batch/storage/v1"
        http.request.assert_called_once_with(
            method="POST",
            url=expected_url,
            headers=mock.ANY,
            data=mock.ANY,
            timeout=420,  # the last request timeout prevails
        )

        _, request_body, _, boundary = self._get_mutlipart_request(http)

        chunks = self._get_payload_chunks(boundary, request_body)
        self.assertEqual(len(chunks), 2)
        self._check_subrequest_payload(chunks[0], "GET", url, {})
        self._check_subrequest_payload(chunks[1], "GET", url, {})
        self.assertEqual(batch._responses[0].status_code, 200)
        self.assertEqual(batch._responses[1].status_code, 404)

    def test_finish_nonempty_non_multipart_response(self):
        url = "http://api.example.com/other_api"
        http = _make_requests_session([_make_response()])
        connection = _Connection(http=http)
        client = _Client(connection)
        batch = self._make_one(client)
        batch._requests.append(("POST", url, {}, {"foo": 1, "bar": 2}))

        with self.assertRaises(ValueError):
            batch.finish()

    def test_finish_multipart_response_with_status_failure(self):
        from google.cloud.exceptions import ServiceUnavailable

        url = "http://api.example.com/other_api"
        expected_response = _make_response(
            status=SERVICE_UNAVAILABLE,
            headers={"content-type": 'multipart/mixed; boundary="DEADBEEF="'},
        )
        http = _make_requests_session([expected_response])
        connection = _Connection(http=http)
        client = _Client(connection)
        batch = self._make_one(client)
        batch.API_BASE_URL = "http://api.example.com"
        batch._requests.append(("POST", url, {}, {"foo": 1, "bar": 2}, None))

        with self.assertRaises(ServiceUnavailable):
            batch.finish()

    def test_as_context_mgr_wo_error(self):
        from google.cloud.storage.client import Client

        url = "http://example.com/api"
        expected_response = _make_response(
            content=_THREE_PART_MIME_RESPONSE,
            headers={"content-type": 'multipart/mixed; boundary="DEADBEEF="'},
        )
        http = _make_requests_session([expected_response])
        project = "PROJECT"
        credentials = _make_credentials()
        client = Client(project=project, credentials=credentials)
        client._http_internal = http

        self.assertEqual(list(client._batch_stack), [])

        target1 = _MockObject()
        target2 = _MockObject()
        target3 = _MockObject()

        with self._make_one(client) as batch:
            self.assertEqual(list(client._batch_stack), [batch])
            batch._make_request(
                "POST", url, {"foo": 1, "bar": 2}, target_object=target1
            )
            batch._make_request("PATCH", url, {"bar": 3}, target_object=target2)
            batch._make_request("DELETE", url, target_object=target3)

        self.assertEqual(list(client._batch_stack), [])
        self.assertEqual(len(batch._requests), 3)
        self.assertEqual(len(batch._responses), 3)
        self.assertEqual(batch._requests[0][0], "POST")
        self.assertEqual(batch._requests[1][0], "PATCH")
        self.assertEqual(batch._requests[2][0], "DELETE")
        self.assertEqual(batch._target_objects, [target1, target2, target3])
        self.assertEqual(target1._properties, {"foo": 1, "bar": 2})
        self.assertEqual(target2._properties, {"foo": 1, "bar": 3})
        self.assertEqual(target3._properties, b"")

    def test_as_context_mgr_no_raise_exception(self):
        from google.cloud.storage.client import Client

        url = "http://api.example.com/other_api"
        expected_response = _make_response(
            content=_TWO_PART_MIME_RESPONSE_WITH_FAIL,
            headers={"content-type": 'multipart/mixed; boundary="DEADBEEF="'},
        )
        http = _make_requests_session([expected_response])
        project = "PROJECT"
        credentials = _make_credentials()
        client = Client(project=project, credentials=credentials)
        client._http_internal = http

        self.assertEqual(list(client._batch_stack), [])

        target1 = _MockObject()
        target2 = _MockObject()

        with self._make_one(client, raise_exception=False) as batch:
            self.assertEqual(list(client._batch_stack), [batch])
            batch._make_request("GET", url, {}, target_object=target1)
            batch._make_request("GET", url, {}, target_object=target2)

        self.assertEqual(list(client._batch_stack), [])
        self.assertEqual(len(batch._requests), 2)
        self.assertEqual(len(batch._responses), 2)
        self.assertEqual(batch._requests[0][0], "GET")
        self.assertEqual(batch._requests[1][0], "GET")
        self.assertEqual(batch._target_objects, [target1, target2])

        # Make sure NotFound exception is added to responses and target2
        self.assertEqual(batch._responses[0].status_code, 200)
        self.assertEqual(batch._responses[1].status_code, 404)
        self.assertEqual(target1._properties, {"foo": 1, "bar": 2})
        self.assertEqual(target2._properties, {"error": {"message": "Not Found"}})

    def test_as_context_mgr_w_error(self):
        from google.cloud.storage.batch import _FutureDict
        from google.cloud.storage.client import Client

        URL = "http://example.com/api"
        http = _make_requests_session([])
        connection = _Connection(http=http)
        project = "PROJECT"
        credentials = _make_credentials()
        client = Client(project=project, credentials=credentials)
        client._base_connection = connection

        self.assertEqual(list(client._batch_stack), [])

        target1 = _MockObject()
        target2 = _MockObject()
        target3 = _MockObject()
        try:
            with self._make_one(client) as batch:
                self.assertEqual(list(client._batch_stack), [batch])
                batch._make_request(
                    "POST", URL, {"foo": 1, "bar": 2}, target_object=target1
                )
                batch._make_request("PATCH", URL, {"bar": 3}, target_object=target2)
                batch._make_request("DELETE", URL, target_object=target3)
                raise ValueError()
        except ValueError:
            pass

        http.request.assert_not_called()
        self.assertEqual(list(client._batch_stack), [])
        self.assertEqual(len(batch._requests), 3)
        self.assertEqual(batch._target_objects, [target1, target2, target3])
        # Since the context manager fails, finish will not get called and
        # the _properties will still be futures.
        self.assertIsInstance(target1._properties, _FutureDict)
        self.assertIsInstance(target2._properties, _FutureDict)
        self.assertIsInstance(target3._properties, _FutureDict)

    def test_respect_client_existing_connection(self):
        client_endpoint = "http://localhost:9023"
        http = _make_requests_session([])
        connection = _Connection(http=http, api_endpoint=client_endpoint)
        client = _Client(connection)
        batch = self._make_one(client)
        self.assertEqual(batch.API_BASE_URL, client_endpoint)
        self.assertEqual(batch._client._connection.API_BASE_URL, client_endpoint)

    def test_use_default_api_without_existing_connection(self):
        default_api_endpoint = "https://storage.googleapis.com"
        http = _make_requests_session([])
        connection = _Connection(http=http)
        client = _Client(connection)
        batch = self._make_one(client)
        self.assertEqual(batch.API_BASE_URL, default_api_endpoint)
        self.assertIsNone(batch._client._connection.API_BASE_URL)
        self.assertIsNone(batch._client._connection._client_info)


class Test__unpack_batch_response(unittest.TestCase):
    def _call_fut(self, headers, content):
        from google.cloud.storage.batch import _unpack_batch_response

        response = _make_response(content=content, headers=headers)

        return _unpack_batch_response(response)

    def _unpack_helper(self, response, content):
        result = list(self._call_fut(response, content))
        self.assertEqual(len(result), 3)

        self.assertEqual(result[0].status_code, http.client.OK)
        self.assertEqual(result[0].json(), {"bar": 2, "foo": 1})
        self.assertEqual(result[1].status_code, http.client.OK)
        self.assertEqual(result[1].json(), {"foo": 1, "bar": 3})
        self.assertEqual(result[2].status_code, http.client.NO_CONTENT)

    def test_bytes_headers(self):
        RESPONSE = {"content-type": b'multipart/mixed; boundary="DEADBEEF="'}
        CONTENT = _THREE_PART_MIME_RESPONSE
        self._unpack_helper(RESPONSE, CONTENT)

    def test_unicode_headers(self):
        RESPONSE = {"content-type": 'multipart/mixed; boundary="DEADBEEF="'}
        CONTENT = _THREE_PART_MIME_RESPONSE
        self._unpack_helper(RESPONSE, CONTENT)


_TWO_PART_MIME_RESPONSE_WITH_FAIL = b"""\
--DEADBEEF=
Content-Type: application/json
Content-ID: <response-8a09ca85-8d1d-4f45-9eb0-da8e8b07ec83+1>

HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
Content-Length: 20

{"foo": 1, "bar": 2}

--DEADBEEF=
Content-Type: application/json
Content-ID: <response-8a09ca85-8d1d-4f45-9eb0-da8e8b07ec83+2>

HTTP/1.1 404 Not Found
Content-Type: application/json; charset=UTF-8
Content-Length: 35

{"error": {"message": "Not Found"}}

--DEADBEEF=--
"""

_THREE_PART_MIME_RESPONSE = b"""\
--DEADBEEF=
Content-Type: application/json
Content-ID: <response-8a09ca85-8d1d-4f45-9eb0-da8e8b07ec83+1>

HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
Content-Length: 20

{"foo": 1, "bar": 2}

--DEADBEEF=
Content-Type: application/json
Content-ID: <response-8a09ca85-8d1d-4f45-9eb0-da8e8b07ec83+2>

HTTP/1.1 200 OK
Content-Type: application/json; charset=UTF-8
Content-Length: 20

{"foo": 1, "bar": 3}

--DEADBEEF=
Content-Type: text/plain
Content-ID: <response-8a09ca85-8d1d-4f45-9eb0-da8e8b07ec83+3>

HTTP/1.1 204 No Content
Content-Length: 0

--DEADBEEF=--
"""


class Test__FutureDict(unittest.TestCase):
    def _make_one(self, *args, **kw):
        from google.cloud.storage.batch import _FutureDict

        return _FutureDict(*args, **kw)

    def test_get(self):
        future = self._make_one()
        self.assertRaises(KeyError, future.get, None)

    def test___getitem__(self):
        future = self._make_one()
        value = orig_value = object()
        with self.assertRaises(KeyError):
            value = future[None]
        self.assertIs(value, orig_value)

    def test___setitem__(self):
        future = self._make_one()
        with self.assertRaises(KeyError):
            future[None] = None


class _Connection(object):
    project = "TESTING"

    def __init__(self, **kw):
        self.__dict__.update(kw)
        self._client_info = kw.get("client_info", None)
        self.API_BASE_URL = kw.get("api_endpoint", None)

    def _make_request(self, method, url, data=None, headers=None, timeout=None):
        return self.http.request(
            url=url, method=method, headers=headers, data=data, timeout=timeout
        )


class _MockObject(object):
    pass


class _Client(object):
    def __init__(self, connection):
        self._base_connection = connection
        self._connection = connection
