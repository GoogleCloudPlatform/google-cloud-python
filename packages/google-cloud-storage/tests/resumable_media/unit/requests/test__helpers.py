# Copyright 2017 Google Inc.
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
from unittest import mock

from google.cloud.storage._media.requests import _request_helpers

EXPECTED_TIMEOUT = (61, 60)


class TestRequestsMixin(object):
    def test__get_status_code(self):
        status_code = int(http.client.OK)
        response = _make_response(status_code)
        assert status_code == _request_helpers.RequestsMixin._get_status_code(response)

    def test__get_headers(self):
        headers = {"fruit": "apple"}
        response = mock.Mock(headers=headers, spec=["headers"])
        assert headers == _request_helpers.RequestsMixin._get_headers(response)

    def test__get_body(self):
        body = b"This is the payload."
        response = mock.Mock(content=body, spec=["content"])
        assert body == _request_helpers.RequestsMixin._get_body(response)


class TestRawRequestsMixin(object):
    def test__get_body_wo_content_consumed(self):
        body = b"This is the payload."
        raw = mock.Mock(spec=["stream"])
        raw.stream.return_value = iter([body])
        response = mock.Mock(raw=raw, _content=False, spec=["raw", "_content"])
        assert body == _request_helpers.RawRequestsMixin._get_body(response)
        raw.stream.assert_called_once_with(
            _request_helpers._SINGLE_GET_CHUNK_SIZE, decode_content=False
        )

    def test__get_body_w_content_consumed(self):
        body = b"This is the payload."
        response = mock.Mock(_content=body, spec=["_content"])
        assert body == _request_helpers.RawRequestsMixin._get_body(response)


def _make_response(status_code):
    return mock.Mock(status_code=status_code, spec=["status_code"])
