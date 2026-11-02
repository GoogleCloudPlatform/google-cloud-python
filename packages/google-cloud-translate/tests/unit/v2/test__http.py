# Copyright 2016 Google LLC
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


class TestConnection(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.translate_v2._http import Connection

        return Connection

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_build_api_url_no_extra_query_params(self):
        from urllib.parse import parse_qsl, urlsplit

        conn = self._make_one(object())
        uri = conn.build_api_url("/foo")
        scheme, netloc, path, qs, _ = urlsplit(uri)
        self.assertEqual("%s://%s" % (scheme, netloc), conn.API_BASE_URL)
        self.assertEqual(
            path, "/".join(["", "language", "translate", conn.API_VERSION, "foo"])
        )
        parms = dict(parse_qsl(qs))
        pretty_print = parms.pop("prettyPrint", "false")
        self.assertEqual(pretty_print, "false")
        self.assertEqual(parms, {})

    def test_build_api_url_w_custom_endpoint(self):
        from urllib.parse import parse_qsl, urlsplit

        custom_endpoint = "https://foo-translation.googleapis.com"
        conn = self._make_one(object(), api_endpoint=custom_endpoint)
        uri = conn.build_api_url("/foo")
        scheme, netloc, path, qs, _ = urlsplit(uri)
        self.assertEqual("%s://%s" % (scheme, netloc), custom_endpoint)
        self.assertEqual(
            path, "/".join(["", "language", "translate", conn.API_VERSION, "foo"])
        )
        parms = dict(parse_qsl(qs))
        pretty_print = parms.pop("prettyPrint", "false")
        self.assertEqual(pretty_print, "false")
        self.assertEqual(parms, {})

    def test_build_api_url_w_extra_query_params(self):
        from urllib.parse import parse_qsl, urlsplit

        conn = self._make_one(object())
        uri = conn.build_api_url("/foo", {"bar": "baz"})
        scheme, netloc, path, qs, _ = urlsplit(uri)
        self.assertEqual("%s://%s" % (scheme, netloc), conn.API_BASE_URL)
        self.assertEqual(
            path, "/".join(["", "language", "translate", conn.API_VERSION, "foo"])
        )
        parms = dict(parse_qsl(qs))
        self.assertEqual(parms["bar"], "baz")

    def test_build_api_url_w_extra_query_params_tuple(self):
        from urllib.parse import parse_qsl, urlsplit

        conn = self._make_one(object())
        query_params = [("q", "val1"), ("q", "val2")]
        uri = conn.build_api_url("/foo", query_params=query_params)
        scheme, netloc, path, qs, _ = urlsplit(uri)
        self.assertEqual("%s://%s" % (scheme, netloc), conn.API_BASE_URL)
        expected_path = "/".join(["", "language", "translate", conn.API_VERSION, "foo"])
        self.assertEqual(path, expected_path)
        params = list(
            sorted(param for param in parse_qsl(qs) if param[0] != "prettyPrint")
        )
        expected_params = [("q", "val1"), ("q", "val2")]
        self.assertEqual(params, expected_params)

    def test_extra_headers(self):
        import requests

        from google.cloud import _http as base_http

        http = mock.create_autospec(requests.Session, instance=True)
        response = requests.Response()
        response.status_code = 200
        data = b"brent-spiner"
        response._content = data
        http.request.return_value = response
        client = mock.Mock(_http=http, spec=["_http"])

        conn = self._make_one(client)
        req_data = "req-data-boring"
        result = conn.api_request("GET", "/rainbow", data=req_data, expect_json=False)
        self.assertEqual(result, data)

        expected_headers = {
            "Accept-Encoding": "gzip",
            base_http.CLIENT_INFO_HEADER: conn.user_agent,
            "User-Agent": conn.user_agent,
        }
        expected_uri = conn.build_api_url("/rainbow")
        http.request.assert_called_once_with(
            data=req_data,
            headers=expected_headers,
            method="GET",
            url=expected_uri,
            timeout=60,
        )
