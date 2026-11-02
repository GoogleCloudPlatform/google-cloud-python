# Copyright 2017 Google LLC All Rights Reserved.
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

import mock

from tests.unit.handlers import (
    _EXPECTED_OTEL_SPAN_ID,
    _EXPECTED_OTEL_TRACE_ID,
    _EXPECTED_OTEL_TRACESAMPLED,
    _setup_otel_span_context,
)

_FLASK_TRACE_ID = "flask0id"
_FLASK_SPAN_ID = "span0flask"
_FLASK_SPAN_ID_XCTC_DEC = "12345"
_FLASK_SPAN_ID_XCTC_HEX = "3039".zfill(16)
_FLASK_HTTP_REQUEST = {"requestUrl": "https://flask.palletsprojects.com/en/1.1.x/"}
_DJANGO_TRACE_ID = "django0id"
_DJANGO_SPAN_ID = "span0django"
_DJANGO_SPAN_ID_XCTC_DEC = "54321"
_DJANGO_SPAN_ID_XCTC_HEX = "d431".zfill(16)
_DJANGO_HTTP_REQUEST = {"requestUrl": "https://www.djangoproject.com/"}


class Test_get_request_data_from_flask(unittest.TestCase):
    @staticmethod
    def _call_fut():
        from google.cloud.logging_v2.handlers import _helpers

        http, trace, span, sampled = _helpers.get_request_data_from_flask()
        return http, trace, span, sampled

    @staticmethod
    def create_app():
        import flask

        app = flask.Flask(__name__)

        @app.route("/")
        def index():
            return "test flask trace"  # pragma: NO COVER

        return app

    def test_no_context_header(self):
        app = self.create_app()
        with app.test_request_context(path="/", headers={}):
            http_request, trace_id, span_id, sampled = self._call_fut()

        self.assertIsNone(trace_id)
        self.assertIsNone(span_id)
        self.assertEqual(sampled, False)
        self.assertEqual(http_request["requestMethod"], "GET")

    def test_xcloud_header(self):
        flask_trace_header = "X_CLOUD_TRACE_CONTEXT"
        expected_trace_id = _FLASK_TRACE_ID
        input_span_id = _FLASK_SPAN_ID_XCTC_DEC
        expected_span_id = _FLASK_SPAN_ID_XCTC_HEX
        flask_trace_id = f"{expected_trace_id}/{input_span_id};o=1"

        app = self.create_app()
        context = app.test_request_context(
            path="/", headers={flask_trace_header: flask_trace_id}
        )

        with context:
            http_request, trace_id, span_id, sampled = self._call_fut()

        self.assertEqual(trace_id, expected_trace_id)
        self.assertEqual(span_id, expected_span_id)
        self.assertEqual(sampled, True)
        self.assertEqual(http_request["requestMethod"], "GET")

    def test_traceparent_header(self):
        flask_trace_header = "TRACEPARENT"
        expected_trace_id = "4bf92f3577b34da6a3ce929d0e0e4736"
        expected_span_id = "00f067aa0ba902b7"
        flask_trace_id = f"00-{expected_trace_id}-{expected_span_id}-01"

        app = self.create_app()
        context = app.test_request_context(
            path="/", headers={flask_trace_header: flask_trace_id}
        )

        with context:
            http_request, trace_id, span_id, sampled = self._call_fut()

        self.assertEqual(trace_id, expected_trace_id)
        self.assertEqual(span_id, expected_span_id)
        self.assertEqual(sampled, True)
        self.assertEqual(http_request["requestMethod"], "GET")

    def test_http_request_populated(self):
        expected_path = "http://testserver/123"
        expected_agent = "Mozilla/5.0"
        expected_referrer = "self"
        expected_ip = "10.1.2.3"
        headers = {
            "User-Agent": expected_agent,
            "Referer": expected_referrer,
        }

        app = self.create_app()
        with app.test_request_context(
            expected_path, headers=headers, environ_base={"REMOTE_ADDR": expected_ip}
        ):
            http_request, *_ = self._call_fut()

        self.assertEqual(http_request["requestMethod"], "GET")
        self.assertEqual(http_request["requestUrl"], expected_path)
        self.assertEqual(http_request["userAgent"], expected_agent)
        self.assertEqual(http_request["protocol"], "HTTP/1.1")

    def test_http_request_sparse(self):
        expected_path = "http://testserver/123"
        app = self.create_app()
        with app.test_request_context(expected_path):
            http_request, *_ = self._call_fut()
        self.assertEqual(http_request["requestMethod"], "GET")
        self.assertEqual(http_request["requestUrl"], expected_path)
        self.assertEqual(http_request["protocol"], "HTTP/1.1")


class Test_get_request_data_from_django(unittest.TestCase):
    @staticmethod
    def _call_fut():
        from google.cloud.logging_v2.handlers import _helpers

        http, trace, span, sampled = _helpers.get_request_data_from_django()
        return http, trace, span, sampled

    def setUp(self):
        from django.conf import settings
        from django.test.utils import setup_test_environment

        if not settings.configured:
            settings.configure()
        setup_test_environment()

    def tearDown(self):
        from django.test.utils import teardown_test_environment

        from google.cloud.logging_v2.handlers.middleware import request

        teardown_test_environment()
        request._thread_locals.__dict__.clear()

    def test_no_context_header(self):
        from django.test import RequestFactory

        from google.cloud.logging_v2.handlers.middleware import request

        django_request = RequestFactory().get("/")

        middleware = request.RequestMiddleware(None)
        middleware(django_request)
        http_request, trace_id, span_id, sampled = self._call_fut()

        self.assertEqual(http_request["requestMethod"], "GET")
        self.assertIsNone(trace_id)
        self.assertIsNone(span_id)
        self.assertEqual(sampled, False)

    def test_xcloud_header(self):
        from django.test import RequestFactory

        from google.cloud.logging_v2.handlers.middleware import request

        django_trace_header = "HTTP_X_CLOUD_TRACE_CONTEXT"
        input_span_id = _DJANGO_SPAN_ID_XCTC_DEC
        expected_span_id = _DJANGO_SPAN_ID_XCTC_HEX
        expected_trace_id = _DJANGO_TRACE_ID
        django_trace_id = f"{expected_trace_id}/{input_span_id};o=1"

        django_request = RequestFactory().get(
            "/", **{django_trace_header: django_trace_id}
        )

        middleware = request.RequestMiddleware(None)
        middleware(django_request)
        http_request, trace_id, span_id, sampled = self._call_fut()

        self.assertEqual(trace_id, expected_trace_id)
        self.assertEqual(span_id, expected_span_id)
        self.assertEqual(sampled, True)
        self.assertEqual(http_request["requestMethod"], "GET")

    def test_traceparent_header(self):
        from django.test import RequestFactory

        from google.cloud.logging_v2.handlers.middleware import request

        django_trace_header = "HTTP_TRACEPARENT"
        expected_trace_id = "4bf92f3577b34da6a3ce929d0e0e4736"
        expected_span_id = "00f067aa0ba902b7"
        header = f"00-{expected_trace_id}-{expected_span_id}-01"

        django_request = RequestFactory().get("/", **{django_trace_header: header})

        middleware = request.RequestMiddleware(None)
        middleware(django_request)
        http_request, trace_id, span_id, sampled = self._call_fut()

        self.assertEqual(trace_id, expected_trace_id)
        self.assertEqual(span_id, expected_span_id)
        self.assertEqual(sampled, True)
        self.assertEqual(http_request["requestMethod"], "GET")

    def test_http_request_populated(self):
        from django.test import RequestFactory

        from google.cloud.logging_v2.handlers.middleware import request

        expected_path = "http://testserver/123"
        expected_agent = "Mozilla/5.0"
        expected_referrer = "self"
        body_content = "test"
        django_request = RequestFactory().put(
            expected_path,
            data=body_content,
            HTTP_USER_AGENT=expected_agent,
            HTTP_REFERER=expected_referrer,
        )
        # ensure test passes even after request has been read
        # context: https://github.com/googleapis/python-logging/issues/159
        django_request.read()

        middleware = request.RequestMiddleware(None)
        middleware(django_request)
        http_request, *_ = self._call_fut()
        self.assertEqual(http_request["requestMethod"], "PUT")
        self.assertEqual(http_request["requestUrl"], expected_path)
        self.assertEqual(http_request["userAgent"], expected_agent)
        self.assertEqual(http_request["protocol"], "HTTP/1.1")

    def test_http_request_sparse(self):
        from django.test import RequestFactory

        from google.cloud.logging_v2.handlers.middleware import request

        expected_path = "http://testserver/123"
        django_request = RequestFactory().put(expected_path)
        middleware = request.RequestMiddleware(None)
        middleware(django_request)
        http_request, *_ = self._call_fut()
        self.assertEqual(http_request["requestMethod"], "PUT")
        self.assertEqual(http_request["requestUrl"], expected_path)
        self.assertEqual(http_request["protocol"], "HTTP/1.1")

    def test_invalid_host_header(self):
        from django.test import RequestFactory

        from google.cloud.logging_v2.handlers.middleware import request

        invalid_http_host = "testserver%7d"
        django_request = RequestFactory().put("/", HTTP_HOST=invalid_http_host)
        middleware = request.RequestMiddleware(None)
        middleware(django_request)
        http_request, *_ = self._call_fut()
        self.assertEqual(http_request["requestMethod"], "PUT")
        self.assertIsNone(http_request["requestUrl"])
        self.assertEqual(http_request["protocol"], "HTTP/1.1")


class Test_get_request_data(unittest.TestCase):
    @staticmethod
    def _call_fut():
        from google.cloud.logging_v2.handlers import _helpers

        http, trace, span, sampled = _helpers.get_request_data()
        return http, trace, span, sampled

    def _helper(self, django_return, flask_return):
        django_patch = mock.patch(
            "google.cloud.logging_v2.handlers._helpers.get_request_data_from_django",
            return_value=django_return,
        )
        flask_patch = mock.patch(
            "google.cloud.logging_v2.handlers._helpers.get_request_data_from_flask",
            return_value=flask_return,
        )

        with django_patch as django_mock:
            with flask_patch as flask_mock:
                result = self._call_fut()

        return django_mock, flask_mock, result

    def test_from_django(self):
        django_expected = (
            _DJANGO_HTTP_REQUEST,
            _DJANGO_TRACE_ID,
            _DJANGO_SPAN_ID,
            False,
        )
        flask_expected = (None, None, None, False)
        django_mock, flask_mock, output = self._helper(django_expected, flask_expected)
        self.assertEqual(output, django_expected)

        django_mock.assert_called_once_with()
        flask_mock.assert_not_called()

    def test_from_flask(self):
        django_expected = (None, None, None, False)
        flask_expected = (_FLASK_HTTP_REQUEST, _FLASK_TRACE_ID, _FLASK_SPAN_ID, False)

        django_mock, flask_mock, output = self._helper(django_expected, flask_expected)
        self.assertEqual(output, flask_expected)

        django_mock.assert_called_once_with()
        flask_mock.assert_called_once_with()

    def test_from_django_and_flask(self):
        django_expected = (
            _DJANGO_HTTP_REQUEST,
            _DJANGO_TRACE_ID,
            _DJANGO_SPAN_ID,
            False,
        )
        flask_expected = (_FLASK_HTTP_REQUEST, _FLASK_TRACE_ID, _FLASK_SPAN_ID, False)

        django_mock, flask_mock, output = self._helper(django_expected, flask_expected)

        # Django wins.
        self.assertEqual(output, django_expected)

        django_mock.assert_called_once_with()
        flask_mock.assert_not_called()

    def test_missing_http_request(self):
        flask_expected = (None, _FLASK_TRACE_ID, _FLASK_SPAN_ID, True)
        django_expected = (None, _DJANGO_TRACE_ID, _DJANGO_TRACE_ID, True)
        django_mock, flask_mock, output = self._helper(django_expected, flask_expected)

        # function only returns trace if http_request data is present
        self.assertEqual(output, (None, None, None, False))

        django_mock.assert_called_once_with()
        flask_mock.assert_called_once_with()

    def test_missing_trace_id(self):
        flask_expected = (_FLASK_HTTP_REQUEST, None, None, False)
        django_expected = (None, _DJANGO_TRACE_ID, _DJANGO_SPAN_ID, True)
        django_mock, flask_mock, output = self._helper(django_expected, flask_expected)

        # trace_id is optional
        self.assertEqual(output, flask_expected)

        django_mock.assert_called_once_with()
        flask_mock.assert_called_once_with()

    def test_missing_both(self):
        flask_expected = (None, None, None, False)
        django_expected = (None, None, None, False)
        django_mock, flask_mock, output = self._helper(django_expected, flask_expected)
        self.assertEqual(output, (None, None, None, False))

        django_mock.assert_called_once_with()
        flask_mock.assert_called_once_with()

    def test_wo_libraries(self):
        output = self._call_fut()
        self.assertEqual(output, (None, None, None, False))

    def test_otel_span_exists_no_request(self):
        flask_expected = (None, None, None, False)
        django_expected = (None, None, None, False)

        with _setup_otel_span_context():
            _, _, output = self._helper(django_expected, flask_expected)
            self.assertEqual(
                output,
                (
                    None,
                    _EXPECTED_OTEL_TRACE_ID,
                    _EXPECTED_OTEL_SPAN_ID,
                    _EXPECTED_OTEL_TRACESAMPLED,
                ),
            )

    def test_otel_span_exists_django_request(self):
        django_expected = (
            _DJANGO_HTTP_REQUEST,
            _DJANGO_TRACE_ID,
            _DJANGO_SPAN_ID,
            False,
        )
        flask_expected = (None, None, None, False)

        with _setup_otel_span_context():
            _, _, output = self._helper(django_expected, flask_expected)
            self.assertEqual(
                output,
                (
                    _DJANGO_HTTP_REQUEST,
                    _EXPECTED_OTEL_TRACE_ID,
                    _EXPECTED_OTEL_SPAN_ID,
                    _EXPECTED_OTEL_TRACESAMPLED,
                ),
            )

    def test_otel_span_exists_flask_request(self):
        django_expected = (None, None, None, False)
        flask_expected = (_FLASK_HTTP_REQUEST, _FLASK_TRACE_ID, _FLASK_SPAN_ID, False)

        with _setup_otel_span_context():
            _, _, output = self._helper(django_expected, flask_expected)
            self.assertEqual(
                output,
                (
                    _FLASK_HTTP_REQUEST,
                    _EXPECTED_OTEL_TRACE_ID,
                    _EXPECTED_OTEL_SPAN_ID,
                    _EXPECTED_OTEL_TRACESAMPLED,
                ),
            )

    def test_otel_span_exists_both_django_and_flask(self):
        django_expected = (
            _DJANGO_HTTP_REQUEST,
            _DJANGO_TRACE_ID,
            _DJANGO_SPAN_ID,
            False,
        )
        flask_expected = (_FLASK_HTTP_REQUEST, _FLASK_TRACE_ID, _FLASK_SPAN_ID, False)

        with _setup_otel_span_context():
            _, _, output = self._helper(django_expected, flask_expected)

            # Django wins
            self.assertEqual(
                output,
                (
                    _DJANGO_HTTP_REQUEST,
                    _EXPECTED_OTEL_TRACE_ID,
                    _EXPECTED_OTEL_SPAN_ID,
                    _EXPECTED_OTEL_TRACESAMPLED,
                ),
            )

    def test_no_otel_span_no_requests(self):
        flask_expected = (None, None, None, False)
        django_expected = (None, None, None, False)
        _, _, output = self._helper(django_expected, flask_expected)
        self.assertEqual(output, (None, None, None, False))

    def test_no_otel_span_django_request(self):
        django_expected = (
            _DJANGO_HTTP_REQUEST,
            _DJANGO_TRACE_ID,
            _DJANGO_SPAN_ID,
            False,
        )
        flask_expected = (None, None, None, False)
        _, _, output = self._helper(django_expected, flask_expected)
        self.assertEqual(output, django_expected)

    def test_no_otel_span_flask_request(self):
        django_expected = (None, None, None, False)
        flask_expected = (_FLASK_HTTP_REQUEST, _FLASK_TRACE_ID, _FLASK_SPAN_ID, False)
        _, _, output = self._helper(django_expected, flask_expected)

        # Django wins
        self.assertEqual(output, flask_expected)

    def test_no_otel_span_both_django_and_flask(self):
        django_expected = (
            _DJANGO_HTTP_REQUEST,
            _DJANGO_TRACE_ID,
            _DJANGO_SPAN_ID,
            False,
        )
        flask_expected = (_FLASK_HTTP_REQUEST, _FLASK_TRACE_ID, _FLASK_SPAN_ID, False)
        _, _, output = self._helper(django_expected, flask_expected)

        # Django wins
        self.assertEqual(output, django_expected)


class Test__parse_xcloud_trace(unittest.TestCase):
    @staticmethod
    def _call_fut(header):
        from google.cloud.logging_v2.handlers import _helpers

        trace, span, sampled = _helpers._parse_xcloud_trace(header)
        return trace, span, sampled

    def test_empty_header(self):
        header = ""
        trace_id, span_id, sampled = self._call_fut(header)
        self.assertIsNone(trace_id)
        self.assertIsNone(span_id)
        self.assertEqual(sampled, False)

    def test_no_span(self):
        header = "12345"
        trace_id, span_id, sampled = self._call_fut(header)
        self.assertEqual(trace_id, header)
        self.assertIsNone(span_id)
        self.assertEqual(sampled, False)

    def test_no_trace(self):
        input_span = "12345"
        expected_span = "3039".zfill(16)
        header = f"/{input_span}"
        trace_id, span_id, sampled = self._call_fut(header)
        self.assertIsNone(trace_id)
        self.assertEqual(span_id, expected_span)
        self.assertEqual(sampled, False)

    def test_with_span(self):
        expected_trace = "12345"
        input_span = "67890"
        expected_span = "10932".zfill(16)
        header = f"{expected_trace}/{input_span}"
        trace_id, span_id, sampled = self._call_fut(header)
        self.assertEqual(trace_id, expected_trace)
        self.assertEqual(span_id, expected_span)
        self.assertEqual(sampled, False)

    def test_with_span_decimal_not_in_bounds(self):
        input_spans = ["0", "9" * 100]

        for input_span in input_spans:
            expected_trace = "12345"
            header = f"{expected_trace}/{input_span}"
            trace_id, span_id, sampled = self._call_fut(header)
            self.assertEqual(trace_id, expected_trace)
            self.assertIsNone(span_id)
            self.assertEqual(sampled, False)

    def test_with_extra_characters(self):
        expected_trace = "12345"
        input_span = "67890"
        expected_span = "10932".zfill(16)
        header = f"{expected_trace}/{input_span};abc"
        trace_id, span_id, sampled = self._call_fut(header)
        self.assertEqual(trace_id, expected_trace)
        self.assertEqual(span_id, expected_span)
        self.assertEqual(sampled, False)

    def test_with_explicit_no_sampled(self):
        expected_trace = "12345"
        input_span = "67890"
        expected_span = "10932".zfill(16)
        header = f"{expected_trace}/{input_span};o=0"
        trace_id, span_id, sampled = self._call_fut(header)
        self.assertEqual(trace_id, expected_trace)
        self.assertEqual(span_id, expected_span)
        self.assertEqual(sampled, False)

    def test_with__sampled(self):
        expected_trace = "12345"
        input_span = "67890"
        expected_span = "10932".zfill(16)
        header = f"{expected_trace}/{input_span};o=1"
        trace_id, span_id, sampled = self._call_fut(header)
        self.assertEqual(trace_id, expected_trace)
        self.assertEqual(span_id, expected_span)
        self.assertEqual(sampled, True)


class Test__parse_trace_parent(unittest.TestCase):
    @staticmethod
    def _call_fut(header):
        from google.cloud.logging_v2.handlers import _helpers

        trace, span, sampled = _helpers._parse_trace_parent(header)
        return trace, span, sampled

    def test_empty_header(self):
        header = ""
        trace_id, span_id, sampled = self._call_fut(header)
        self.assertIsNone(trace_id)
        self.assertIsNone(span_id)
        self.assertEqual(sampled, False)

    def test_valid_header(self):
        header = "00-0af7651916cd43dd8448eb211c80319c-b7ad6b7169203331-01"
        trace_id, span_id, sampled = self._call_fut(header)
        self.assertEqual(trace_id, "0af7651916cd43dd8448eb211c80319c")
        self.assertEqual(span_id, "b7ad6b7169203331")
        self.assertEqual(sampled, True)

    def test_not_sampled(self):
        header = "00-0af7651916cd43dd8448eb211c80319c-b7ad6b7169203331-00"
        trace_id, span_id, sampled = self._call_fut(header)
        self.assertEqual(trace_id, "0af7651916cd43dd8448eb211c80319c")
        self.assertEqual(span_id, "b7ad6b7169203331")
        self.assertEqual(sampled, False)

    def test_sampled_w_other_flags(self):
        header = "00-0af7651916cd43dd8448eb211c80319c-b7ad6b7169203331-09"
        trace_id, span_id, sampled = self._call_fut(header)
        self.assertEqual(trace_id, "0af7651916cd43dd8448eb211c80319c")
        self.assertEqual(span_id, "b7ad6b7169203331")
        self.assertEqual(sampled, True)

    def test_invalid_headers(self):
        invalid_headers = [
            "",
            "test"
            "ff-0af7651916cd43dd8448eb211c80319c-b7ad6b7169203331-01",  # invalid version
            "00-00000000000000000000000000000000-b7ad6b7169203331-01",  # invalid trace
            "00-0af7651916cd43dd8448eb211c80319c-0000000000000000-01",  # invalid span
            "00-af7651916cd43dd8448eb211c80319c-b7ad6b7169203331-00",
            "00-0af7651916cd43dd8448eb211c80319c-bad6b7169203331-00",
            "00-0af7651916cd43dd8448eb211c80319c-b7ad6b7169203331-0",
            "00-0af7651916cd43dd8448eb211c80319c-b7ad6b7169203331-",
            "00-0af7651916cd43dd8448eb211c80319c-00",
        ]
        for header in invalid_headers:
            trace_id, span_id, sampled = self._call_fut(header)
            self.assertIsNone(trace_id)
            self.assertIsNone(span_id)
            self.assertEqual(sampled, False)


class Test__parse_open_telemetry_data(unittest.TestCase):
    @staticmethod
    def _call_fut():
        from google.cloud.logging_v2.handlers import _helpers

        trace, span, sampled = _helpers._retrieve_current_open_telemetry_span()
        return trace, span, sampled

    def test_no_op(self):
        trace_id, span_id, sampled = self._call_fut()
        self.assertIsNone(trace_id)
        self.assertIsNone(span_id)
        self.assertEqual(sampled, False)

    def test_span_exists(self):
        with _setup_otel_span_context():
            trace_id, span_id, sampled = self._call_fut()
            self.assertEqual(trace_id, _EXPECTED_OTEL_TRACE_ID)
            self.assertEqual(span_id, _EXPECTED_OTEL_SPAN_ID)
            self.assertEqual(sampled, _EXPECTED_OTEL_TRACESAMPLED)
