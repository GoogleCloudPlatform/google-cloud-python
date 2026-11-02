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


class TestClient(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.translate_v2 import Client

        return Client

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_constructor_defaults(self):
        from google.cloud._http import ClientInfo

        from google.cloud.translate_v2._http import Connection
        from google.cloud.translate_v2.client import ENGLISH_ISO_639

        http = object()
        client = self._make_one(_http=http)
        self.assertIsInstance(client._connection, Connection)
        self.assertIsNone(client._connection.credentials)
        self.assertIs(client._connection.http, http)
        self.assertEqual(client.target_language, ENGLISH_ISO_639)
        self.assertIsInstance(client._connection._client_info, ClientInfo)

    def test_constructor_explicit(self):
        from google.cloud._http import ClientInfo

        from google.cloud.translate_v2._http import Connection

        http = object()
        target = "es"
        client_info = ClientInfo()
        client = self._make_one(
            target_language=target,
            _http=http,
            client_info=client_info,
            client_options={"api_endpoint": "https://foo-translation.googleapis.com"},
        )
        self.assertIsInstance(client._connection, Connection)
        self.assertIsNone(client._connection.credentials)
        self.assertIs(client._connection.http, http)
        self.assertEqual(client.target_language, target)
        self.assertIs(client._connection._client_info, client_info)
        self.assertEqual(
            client._connection.API_BASE_URL, "https://foo-translation.googleapis.com"
        )

    def test_constructor_w_empty_client_options(self):
        from google.api_core.client_options import ClientOptions
        from google.cloud._http import ClientInfo

        http = object()
        target = "es"
        client_info = ClientInfo()
        client_options = ClientOptions()
        client = self._make_one(
            target_language=target,
            _http=http,
            client_info=client_info,
            client_options=client_options,
        )
        self.assertEqual(
            client._connection.API_BASE_URL, client._connection.DEFAULT_API_ENDPOINT
        )

    def test_constructor_w_client_options_object(self):
        from google.api_core.client_options import ClientOptions
        from google.cloud._http import ClientInfo

        http = object()
        target = "es"
        client_info = ClientInfo()
        client_options = ClientOptions(
            api_endpoint="https://foo-translation.googleapis.com"
        )
        client = self._make_one(
            target_language=target,
            _http=http,
            client_info=client_info,
            client_options=client_options,
        )
        self.assertEqual(
            client._connection.API_BASE_URL, "https://foo-translation.googleapis.com"
        )

    def test_get_languages(self):
        from google.cloud.translate_v2.client import ENGLISH_ISO_639

        client = self._make_one(_http=object())
        supported = [
            {"language": "en", "name": "English"},
            {"language": "af", "name": "Afrikaans"},
            {"language": "am", "name": "Amharic"},
        ]
        data = {"data": {"languages": supported}}
        conn = client._connection = _Connection(data)

        result = client.get_languages()
        self.assertEqual(result, supported)

        # Verify requested.
        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "GET")
        self.assertEqual(req["path"], "/languages")
        self.assertEqual(req["query_params"], {"target": ENGLISH_ISO_639})

    def test_get_languages_no_target(self):
        client = self._make_one(target_language=None, _http=object())
        supported = [{"language": "en"}, {"language": "af"}, {"language": "am"}]
        data = {"data": {"languages": supported}}
        conn = client._connection = _Connection(data)

        result = client.get_languages()
        self.assertEqual(result, supported)

        # Verify requested.
        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(len(req), 3)
        self.assertEqual(req["method"], "GET")
        self.assertEqual(req["path"], "/languages")
        self.assertEqual(req["query_params"], {})

    def test_get_languages_explicit_target(self):
        client = self._make_one(_http=object())
        target_language = "en"
        supported = [
            {"language": "en", "name": "Spanish"},
            {"language": "af", "name": "Afrikaans"},
            {"language": "am", "name": "Amharic"},
        ]
        data = {"data": {"languages": supported}}
        conn = client._connection = _Connection(data)

        result = client.get_languages(target_language)
        self.assertEqual(result, supported)

        # Verify requested.
        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "GET")
        self.assertEqual(req["path"], "/languages")
        self.assertEqual(req["query_params"], {"target": target_language})

    def test_detect_language_bad_result(self):
        client = self._make_one(_http=object())
        value = "takoy"
        conn = client._connection = _Connection({})

        with self.assertRaises(ValueError):
            client.detect_language(value)

        # Verify requested.
        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "POST")
        self.assertEqual(req["path"], "/detect")
        expected_data = {"q": [value]}
        self.assertEqual(req["data"], expected_data)

    def test_detect_language_single_value(self):
        client = self._make_one(_http=object())
        value = "takoy"
        detection = {
            "confidence": 1.0,
            "input": value,
            "language": "ru",
            "isReliable": False,
        }
        data = {"data": {"detections": [[detection]]}}
        conn = client._connection = _Connection(data)

        result = client.detect_language(value)
        self.assertEqual(result, detection)

        # Verify requested.
        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "POST")
        self.assertEqual(req["path"], "/detect")
        expected_data = {"q": [value]}
        self.assertEqual(req["data"], expected_data)

    def test_detect_language_multiple_values(self):
        client = self._make_one(_http=object())
        value1 = "fa\xe7ade"  # facade (with a cedilla)
        detection1 = {
            "confidence": 0.6166008,
            "input": value1,
            "isReliable": False,
            "language": "en",
        }
        value2 = "s'il vous plait"
        detection2 = {
            "confidence": 0.29728225,
            "input": value2,
            "isReliable": False,
            "language": "fr",
        }
        data = {"data": {"detections": [[detection1], [detection2]]}}
        conn = client._connection = _Connection(data)

        result = client.detect_language([value1, value2])
        self.assertEqual(result, [detection1, detection2])

        # Verify requested.
        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "POST")
        self.assertEqual(req["path"], "/detect")
        expected_data = {"q": [value1, value2]}
        self.assertEqual(req["data"], expected_data)

    def test_detect_language_multiple_results(self):
        client = self._make_one(_http=object())
        value = "soy"
        detection1 = {
            "confidence": 0.81496066,
            "input": value,
            "language": "es",
            "isReliable": False,
        }
        detection2 = {
            "confidence": 0.222,
            "input": value,
            "language": "en",
            "isReliable": False,
        }
        data = {"data": {"detections": [[detection1, detection2]]}}
        client._connection = _Connection(data)

        with self.assertRaises(ValueError):
            client.detect_language(value)

    def test_translate_bad_result(self):
        client = self._make_one(_http=object())
        value = "hvala ti"
        conn = client._connection = _Connection({})

        with self.assertRaises(ValueError):
            client.translate(value)

        # Verify requested.
        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "POST")
        self.assertEqual(req["path"], "")
        expected_data = {
            "target": "en",
            "q": [value],
            "cid": (),
            "source": None,
            "model": None,
            "format": None,
        }
        self.assertEqual(req["data"], expected_data)

    def test_translate_defaults(self):
        client = self._make_one(_http=object())
        value = "hvala ti"
        translation = {
            "detectedSourceLanguage": "hr",
            "translatedText": "thank you",
            "input": value,
        }
        data = {"data": {"translations": [translation]}}
        conn = client._connection = _Connection(data)

        result = client.translate(value)
        self.assertEqual(result, translation)

        # Verify requested.
        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "POST")
        self.assertEqual(req["path"], "")

        expected_data = {
            "target": "en",
            "q": [value],
            "cid": (),
            "source": None,
            "model": None,
            "format": None,
        }
        self.assertEqual(req["data"], expected_data)

    def test_translate_multiple(self):
        client = self._make_one(_http=object())
        value1 = "hvala ti"
        translation1 = {
            "detectedSourceLanguage": "hr",
            "translatedText": "thank you",
            "input": value1,
        }
        value2 = "Dankon"
        translation2 = {
            "detectedSourceLanguage": "eo",
            "translatedText": "thank you",
            "input": value2,
        }
        data = {"data": {"translations": [translation1, translation2]}}
        conn = client._connection = _Connection(data)

        result = client.translate([value1, value2])
        self.assertEqual(result, [translation1, translation2])

        # Verify requested.
        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "POST")
        self.assertEqual(req["path"], "")

        expected_data = {
            "target": "en",
            "q": [value1, value2],
            "cid": (),
            "source": None,
            "model": None,
            "format": None,
        }
        self.assertEqual(req["data"], expected_data)

    def test_translate_explicit(self):
        client = self._make_one(_http=object())
        value = "thank you"
        target_language = "eo"
        source_language = "en"
        translation = {"translatedText": "Dankon", "input": value}
        data = {"data": {"translations": [translation]}}
        conn = client._connection = _Connection(data)

        cid = "123"
        format_ = "text"
        model = "nmt"
        result = client.translate(
            value,
            target_language=target_language,
            source_language=source_language,
            format_=format_,
            customization_ids=cid,
            model=model,
        )
        self.assertEqual(result, translation)

        # Verify requested.
        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "POST")
        self.assertEqual(req["path"], "")

        expected_data = {
            "target": target_language,
            "q": [value],
            "cid": [cid],
            "source": source_language,
            "model": model,
            "format": format_,
        }
        self.assertEqual(req["data"], expected_data)


class _Connection(object):
    def __init__(self, *responses):
        self._responses = responses
        self._requested = []

    def api_request(self, **kw):
        self._requested.append(kw)
        response, self._responses = self._responses[0], self._responses[1:]
        return response
