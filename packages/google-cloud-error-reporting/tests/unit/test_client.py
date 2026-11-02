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


import os
import unittest

import mock


def _make_credentials():
    import google.auth.credentials

    return mock.Mock(spec=google.auth.credentials.Credentials)


class TestClient(unittest.TestCase):
    PROJECT = "PROJECT"
    SERVICE = "SERVICE"
    VERSION = "myversion"

    @staticmethod
    def _get_target_class():
        from google.cloud.error_reporting.client import Client

        return Client

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def _make_http(self, *args, **kw):
        from google.cloud.error_reporting.client import HTTPContext

        return HTTPContext(*args, **kw)

    def _get_report_payload(self, error_api):
        self.assertEqual(error_api.report_error_event.call_count, 1)
        call = error_api.report_error_event.mock_calls[0]
        _, positional, kwargs = call
        self.assertEqual(kwargs, {})
        self.assertEqual(len(positional), 1)
        return positional[0]

    @mock.patch.dict(os.environ, clear=True)
    @mock.patch("google.cloud.client._determine_default_project")
    def test_ctor_defaults(self, default_mock):
        from google.api_core.client_info import ClientInfo

        credentials = _make_credentials()
        default_mock.return_value = "foo"
        client = self._make_one(credentials=credentials)
        self.assertEqual(client.service, client.DEFAULT_SERVICE)
        self.assertEqual(client.version, None)
        self.assertIsInstance(client._client_info, ClientInfo)
        default_mock.assert_called_once_with(None)

    def test_ctor_explicit(self):
        credentials = _make_credentials()
        client_info = mock.Mock()
        client_options = mock.Mock()
        client = self._make_one(
            project=self.PROJECT,
            credentials=credentials,
            service=self.SERVICE,
            version=self.VERSION,
            client_info=client_info,
            client_options=client_options,
        )
        self.assertEqual(client.service, self.SERVICE)
        self.assertEqual(client.version, self.VERSION)
        self.assertIs(client._client_info, client_info)
        self.assertIs(client._client_options, client_options)

    def test_report_errors_api_already(self):
        credentials = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=credentials)
        client._report_errors_api = already = mock.Mock()
        self.assertIs(client.report_errors_api, already)

    def test_report_errors_api_wo_grpc(self):
        credentials = _make_credentials()
        client_info = mock.Mock()
        client_options = mock.Mock()
        http = mock.Mock()
        client = self._make_one(
            project=self.PROJECT,
            credentials=credentials,
            client_info=client_info,
            client_options=client_options,
            _http=http,
            _use_grpc=False,
        )
        patch = mock.patch(
            "google.cloud.error_reporting.client._ErrorReportingLoggingAPI"
        )

        with patch as patched:
            api = client.report_errors_api

        self.assertIs(api, patched.return_value)
        patched.assert_called_once_with(
            self.PROJECT, credentials, http, client_info, client_options
        )

    def test_report_errors_api_w_grpc(self):
        credentials = _make_credentials()
        client = self._make_one(
            project=self.PROJECT, credentials=credentials, _use_grpc=True
        )
        patch = mock.patch("google.cloud.error_reporting.client.make_report_error_api")

        with patch as patched:
            api = client.report_errors_api

        self.assertIs(api, patched.return_value)
        patched.assert_called_once_with(client)

    def test_report_exception_with_grpc(self):
        credentials = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=credentials)

        patch = mock.patch("google.cloud.error_reporting.client.make_report_error_api")
        with patch as make_api:
            try:
                raise NameError
            except NameError:
                client.report_exception()
            payload = make_api.return_value.report_error_event.call_args[0][0]
            make_api.assert_called_once_with(client)

        self.assertEqual(payload["serviceContext"], {"service": client.DEFAULT_SERVICE})
        self.assertIn("test_report", payload["message"])
        self.assertIn("test_client.py", payload["message"])

    def test_report_exception_wo_grpc(self):
        credentials = _make_credentials()
        client = self._make_one(
            project=self.PROJECT, credentials=credentials, _use_grpc=False
        )
        patch = mock.patch(
            "google.cloud.error_reporting.client._ErrorReportingLoggingAPI"
        )
        with patch as _error_api:
            try:
                raise NameError
            except NameError:
                client.report_exception()
            mock_report = _error_api.return_value.report_error_event
            payload = mock_report.call_args[0][0]

        self.assertEqual(payload["serviceContext"], {"service": client.DEFAULT_SERVICE})
        self.assertIn("test_report", payload["message"])
        self.assertIn("test_client.py", payload["message"])
        self.assertIsNotNone(client.report_errors_api)

    @mock.patch("google.cloud.error_reporting.client.make_report_error_api")
    def test_report_exception_with_service_version_in_constructor(self, make_api):
        credentials = _make_credentials()
        service = "notdefault"
        version = "notdefaultversion"
        client = self._make_one(
            project=self.PROJECT,
            credentials=credentials,
            service=service,
            version=version,
        )

        http_context = self._make_http(method="GET", response_status_code=500)
        user = "user@gmail.com"

        error_api = mock.Mock(spec=["report_error_event"])
        make_api.return_value = error_api

        try:
            raise NameError
        except NameError:
            client.report_exception(http_context=http_context, user=user)

        make_api.assert_called_once_with(client)

        payload = self._get_report_payload(error_api)
        self.assertEqual(
            payload["serviceContext"], {"service": service, "version": version}
        )
        self.assertIn(
            "test_report_exception_with_service_version_in_constructor",
            payload["message"],
        )
        self.assertIn("test_client.py", payload["message"])
        self.assertEqual(payload["context"]["httpRequest"]["responseStatusCode"], 500)
        self.assertEqual(payload["context"]["httpRequest"]["method"], "GET")
        self.assertEqual(payload["context"]["user"], user)

    @mock.patch("google.cloud.error_reporting.client.make_report_error_api")
    def test_report(self, make_api):
        credentials = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=credentials)

        error_api = mock.Mock(spec=["report_error_event"])
        make_api.return_value = error_api

        message = "this is an error"
        client.report(message)

        payload = self._get_report_payload(error_api)

        self.assertEqual(payload["message"], message)
        report_location = payload["context"]["reportLocation"]
        self.assertIn("test_client.py", report_location["filePath"])
        self.assertEqual(report_location["functionName"], "test_report")
        self.assertGreater(report_location["lineNumber"], 100)
        self.assertLess(report_location["lineNumber"], 250)
