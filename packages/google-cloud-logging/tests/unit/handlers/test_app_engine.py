# Copyright 2016 Google LLC All Rights Reserved.
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

import logging
import unittest

import mock
import pytest


class TestAppEngineHandler(unittest.TestCase):
    PROJECT = "PROJECT"

    def _get_target_class(self):
        from google.cloud.logging.handlers import AppEngineHandler

        return AppEngineHandler

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_constructor_w_gae_standard_env(self):
        import sys

        from google.cloud.logging_v2.handlers import app_engine

        client = mock.Mock(project=self.PROJECT, spec=["project"])

        # Verify that project/service/version are picked up from the
        # environment.
        with (
            mock.patch(
                "os.environ",
                new={
                    app_engine._GAE_SERVICE_ENV: "test_service",
                    app_engine._GAE_VERSION_ENV: "test_version",
                },
            ),
            mock.patch(
                "google.cloud.logging_v2.handlers._monitored_resources.retrieve_metadata_server",
                return_value=self.PROJECT,
            ),
            pytest.warns(
                DeprecationWarning,
                match="AppEngineHandler is deprecated. Use CloudLoggingHandler instead",
            ),
        ):
            handler = self._make_one(client, transport=_Transport)

        self.assertIs(handler.client, client)
        self.assertEqual(handler.name, app_engine._DEFAULT_GAE_LOGGER_NAME)
        self.assertEqual(handler.resource.type, "gae_app")
        self.assertEqual(handler.resource.labels["project_id"], self.PROJECT)
        self.assertEqual(handler.resource.labels["module_id"], "test_service")
        self.assertEqual(handler.resource.labels["version_id"], "test_version")
        self.assertIs(handler.stream, sys.stderr)

    def test_constructor_w_gae_flex_env(self):
        import io

        from google.cloud.logging_v2.handlers import app_engine

        client = mock.Mock(project=self.PROJECT, spec=["project"])
        name = "test-logger"
        stream = io.BytesIO()

        # Verify that _GAE_PROJECT_ENV_FLEX environment variable takes
        # precedence over _GAE_PROJECT_ENV_STANDARD.
        with (
            mock.patch(
                "os.environ",
                new={
                    app_engine._GAE_PROJECT_ENV_FLEX: "test_project_2",
                    app_engine._GAE_PROJECT_ENV_STANDARD: "test_project_should_be_overridden",
                    app_engine._GAE_SERVICE_ENV: "test_service_2",
                    app_engine._GAE_VERSION_ENV: "test_version_2",
                },
            ),
            mock.patch(
                "google.cloud.logging_v2.handlers._monitored_resources.retrieve_metadata_server",
                return_value=self.PROJECT,
            ),
            pytest.warns(
                DeprecationWarning,
                match="AppEngineHandler is deprecated. Use CloudLoggingHandler instead",
            ),
        ):
            handler = self._make_one(
                client, name=name, transport=_Transport, stream=stream
            )

        self.assertIs(handler.client, client)
        self.assertEqual(handler.name, name)
        self.assertEqual(handler.resource.type, "gae_app")
        self.assertEqual(handler.resource.labels["project_id"], self.PROJECT)
        self.assertEqual(handler.resource.labels["module_id"], "test_service_2")
        self.assertEqual(handler.resource.labels["version_id"], "test_version_2")
        self.assertIs(handler.stream, stream)

    def test_emit(self):
        expected_http_request = {"request_url": "test"}
        trace_id = "trace-test"
        expected_trace_id = f"projects/{self.PROJECT}/traces/{trace_id}"
        get_request_patch = mock.patch(
            "google.cloud.logging_v2.handlers.app_engine.get_request_data",
            return_value=(expected_http_request, trace_id, None, None),
        )
        with (
            get_request_patch,
            pytest.warns(
                DeprecationWarning,
                match="AppEngineHandler is deprecated. Use CloudLoggingHandler instead",
            ),
        ):
            # library integrations mocked to return test data
            client = mock.Mock(project=self.PROJECT, spec=["project"])
            handler = self._make_one(client, transport=_Transport)
            gae_resource = handler.get_gae_resource()
            gae_labels = handler.get_gae_labels()
            logname = "app"
            message = "hello world"
            record = logging.LogRecord(
                logname, logging, None, None, message, None, None
            )
            handler.project_id = self.PROJECT
            handler.emit(record)

            self.assertIs(handler.transport.client, client)
            self.assertEqual(handler.transport.name, logname)
            self.assertEqual(
                handler.transport.send_called_with,
                (
                    record,
                    message,
                    gae_resource,
                    gae_labels,
                    expected_trace_id,
                    None,
                    expected_http_request,
                ),
            )

    def test_emit_manual_field_override(self):
        from google.cloud.logging_v2.resource import Resource

        inferred_http_request = {"request_url": "test"}
        inferred_trace_id = "trace-test"
        get_request_patch = mock.patch(
            "google.cloud.logging_v2.handlers.app_engine.get_request_data",
            return_value=(inferred_http_request, inferred_trace_id, None, None),
        )
        with (
            get_request_patch,
            pytest.warns(
                DeprecationWarning,
                match="AppEngineHandler is deprecated. Use CloudLoggingHandler instead",
            ),
        ):
            # library integrations mocked to return test data
            client = mock.Mock(project=self.PROJECT, spec=["project"])
            handler = self._make_one(client, transport=_Transport)
            gae_labels = handler.get_gae_labels()
            logname = "app"
            message = "hello world"
            record = logging.LogRecord(
                logname, logging, None, None, message, None, None
            )
            handler.project_id = self.PROJECT
            # set attributes manually
            expected_trace = "123"
            setattr(record, "trace", expected_trace)
            expected_span = "456"
            setattr(record, "span_id", expected_span)
            expected_http = {"request_url": "manual"}
            setattr(record, "http_request", expected_http)
            expected_resource = Resource(type="test", labels={})
            setattr(record, "resource", expected_resource)
            additional_labels = {"test-label": "manual"}
            expected_labels = dict(gae_labels)
            expected_labels.update(additional_labels)
            setattr(record, "labels", additional_labels)
            handler.emit(record)
            self.assertIs(handler.transport.client, client)
            self.assertEqual(handler.transport.name, logname)
            self.assertEqual(
                handler.transport.send_called_with,
                (
                    record,
                    message,
                    expected_resource,
                    expected_labels,
                    expected_trace,
                    expected_span,
                    expected_http,
                ),
            )

    def _get_gae_labels_helper(self, trace_id):
        get_request_patch = mock.patch(
            "google.cloud.logging_v2.handlers.app_engine.get_request_data",
            return_value=(None, trace_id, None, None),
        )

        client = mock.Mock(project=self.PROJECT, spec=["project"])
        # The handler actually calls ``get_gae_labels()``.
        with get_request_patch as mock_get_request:
            handler = self._make_one(client, transport=_Transport)

            gae_labels = handler.get_gae_labels()
            self.assertEqual(mock_get_request.mock_calls, [mock.call()])

        return gae_labels

    def test_get_gae_labels_with_label(self):
        from google.cloud.logging_v2.handlers import app_engine

        trace_id = "test-gae-trace-id"
        with pytest.warns(
            DeprecationWarning,
            match="AppEngineHandler is deprecated. Use CloudLoggingHandler instead",
        ):
            gae_labels = self._get_gae_labels_helper(trace_id)
        expected_labels = {app_engine._TRACE_ID_LABEL: trace_id}
        self.assertEqual(gae_labels, expected_labels)

    def test_get_gae_labels_without_label(self):
        with pytest.warns(
            DeprecationWarning,
            match="AppEngineHandler is deprecated. Use CloudLoggingHandler instead",
        ):
            gae_labels = self._get_gae_labels_helper(None)
        self.assertEqual(gae_labels, {})


class _Transport(object):
    def __init__(self, client, name):
        self.client = client
        self.name = name

    def send(self, record, message, resource, labels, trace, span_id, http_request):
        self.send_called_with = (
            record,
            message,
            resource,
            labels,
            trace,
            span_id,
            http_request,
        )
