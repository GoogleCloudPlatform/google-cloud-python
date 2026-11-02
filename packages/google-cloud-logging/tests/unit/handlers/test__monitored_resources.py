# Copyright 2021 Google LLC All Rights Reserved.
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

import functools
import logging
import os
import unittest

import mock
import pytest

from google.cloud.logging_v2.handlers import _monitored_resources
from google.cloud.logging_v2.handlers._monitored_resources import (
    _create_app_engine_resource,
    _create_cloud_run_job_resource,
    _create_cloud_run_service_resource,
    _create_compute_resource,
    _create_functions_resource,
    _create_global_resource,
    _create_kubernetes_resource,
    add_resource_labels,
    detect_resource,
)
from google.cloud.logging_v2.resource import Resource


class Test_Create_Resources(unittest.TestCase):
    PROJECT = "test-project"
    LOCATION = "test-location"
    NAME = "test-name"
    CLUSTER = "test-cluster"
    VERSION = "1"
    CONFIG = "test-config"

    def _mock_metadata(self, endpoint):
        if (
            endpoint == _monitored_resources._ZONE_ID
            or endpoint == _monitored_resources._REGION_ID
            or endpoint == _monitored_resources._GKE_CLUSTER_LOCATION
        ):
            return self.LOCATION
        elif (
            endpoint == _monitored_resources._GKE_CLUSTER_NAME
            or endpoint == _monitored_resources._GCE_INSTANCE_ID
        ):
            return self.NAME
        elif endpoint == _monitored_resources._PROJECT_NAME:
            return self.PROJECT
        else:
            return None

    def _mock_metadata_no_project(self, endpoint):
        if (
            endpoint == _monitored_resources._ZONE_ID
            or endpoint == _monitored_resources._REGION_ID
        ):
            return self.LOCATION
        elif (
            endpoint == _monitored_resources._GKE_CLUSTER_NAME
            or endpoint == _monitored_resources._GCE_INSTANCE_ID
        ):
            return self.NAME
        else:
            return None

    def setUp(self):
        os.environ.clear()

    def test_create_legacy_functions_resource(self):
        patch = mock.patch(
            "google.cloud.logging_v2.handlers._monitored_resources.retrieve_metadata_server",
            wraps=self._mock_metadata,
        )

        os.environ[_monitored_resources._CLOUD_RUN_SERVICE_ID] = self.NAME
        with patch:
            legacy_func_resource = _create_functions_resource()

            self.assertIsInstance(legacy_func_resource, Resource)
            self.assertEqual(legacy_func_resource.type, "cloud_function")
            self.assertEqual(legacy_func_resource.labels["project_id"], self.PROJECT)
            self.assertEqual(legacy_func_resource.labels["function_name"], self.NAME)
            self.assertEqual(legacy_func_resource.labels["region"], self.LOCATION)

    def test_create_modern_functions_resource(self):
        patch = mock.patch(
            "google.cloud.logging_v2.handlers._monitored_resources.retrieve_metadata_server",
            wraps=self._mock_metadata,
        )
        os.environ[_monitored_resources._FUNCTION_NAME] = self.NAME
        with patch:
            func_resource = _create_functions_resource()

            self.assertIsInstance(func_resource, Resource)
            self.assertEqual(func_resource.type, "cloud_function")
            self.assertEqual(func_resource.labels["project_id"], self.PROJECT)
            self.assertEqual(func_resource.labels["function_name"], self.NAME)
            self.assertEqual(func_resource.labels["region"], self.LOCATION)

    def test_functions_resource_no_name(self):
        """
        Simulate functions environment with function name returned as None
        https://github.com/googleapis/python-logging/pull/718
        """
        patch = mock.patch(
            "google.cloud.logging_v2.handlers._monitored_resources.retrieve_metadata_server",
            wraps=self._mock_metadata_no_project,
        )
        with patch:
            func_resource = _create_functions_resource()

            self.assertIsInstance(func_resource, Resource)
            self.assertEqual(func_resource.type, "cloud_function")
            self.assertEqual(func_resource.labels["project_id"], "")
            self.assertEqual(func_resource.labels["function_name"], "")

    def test_create_kubernetes_resource(self):
        patch = mock.patch(
            "google.cloud.logging_v2.handlers._monitored_resources.retrieve_metadata_server",
            wraps=self._mock_metadata,
        )
        with patch:
            resource = _create_kubernetes_resource()

            self.assertIsInstance(resource, Resource)
            self.assertEqual(resource.type, "k8s_container")
            self.assertEqual(resource.labels["project_id"], self.PROJECT)
            self.assertEqual(resource.labels["cluster_name"], self.NAME)
            self.assertEqual(resource.labels["location"], self.LOCATION)

    def test_compute_resource(self):
        patch = mock.patch(
            "google.cloud.logging_v2.handlers._monitored_resources.retrieve_metadata_server",
            wraps=self._mock_metadata,
        )

        with patch:
            resource = _create_compute_resource()
            self.assertIsInstance(resource, Resource)
            self.assertEqual(resource.type, "gce_instance")
            self.assertEqual(resource.labels["project_id"], self.PROJECT)
            self.assertEqual(resource.labels["instance_id"], self.NAME)
            self.assertEqual(resource.labels["zone"], self.LOCATION)

    def test_cloud_run_service_resource(self):
        patch = mock.patch(
            "google.cloud.logging_v2.handlers._monitored_resources.retrieve_metadata_server",
            wraps=self._mock_metadata,
        )
        os.environ[_monitored_resources._CLOUD_RUN_SERVICE_ID] = self.NAME
        os.environ[_monitored_resources._CLOUD_RUN_REVISION_ID] = self.VERSION
        os.environ[_monitored_resources._CLOUD_RUN_CONFIGURATION_ID] = self.CONFIG
        with patch:
            resource = _create_cloud_run_service_resource()
            self.assertIsInstance(resource, Resource)
            self.assertEqual(resource.type, "cloud_run_revision")
            self.assertEqual(resource.labels["project_id"], self.PROJECT)
            self.assertEqual(resource.labels["service_name"], self.NAME)
            self.assertEqual(resource.labels["revision_name"], self.VERSION)
            self.assertEqual(resource.labels["configuration_name"], self.CONFIG)
            self.assertEqual(resource.labels["location"], self.LOCATION)

    def test_cloud_run_job_resource(self):
        patch = mock.patch(
            "google.cloud.logging_v2.handlers._monitored_resources.retrieve_metadata_server",
            wraps=self._mock_metadata,
        )
        os.environ[_monitored_resources._CLOUD_RUN_JOB_ID] = self.NAME
        os.environ[_monitored_resources._CLOUD_RUN_EXECUTION_ID] = self.VERSION
        os.environ[_monitored_resources._CLOUD_RUN_TASK_INDEX] = self.CONFIG
        os.environ[_monitored_resources._CLOUD_RUN_TASK_ATTEMPT] = self.CLUSTER
        with patch:
            resource = _create_cloud_run_job_resource()
            self.assertIsInstance(resource, Resource)
            self.assertEqual(resource.type, "cloud_run_job")
            self.assertEqual(resource.labels["project_id"], self.PROJECT)
            self.assertEqual(resource.labels["job_name"], self.NAME)
            self.assertEqual(resource.labels["location"], self.LOCATION)

    def test_app_engine_resource(self):
        patch = mock.patch(
            "google.cloud.logging_v2.handlers._monitored_resources.retrieve_metadata_server",
            wraps=self._mock_metadata,
        )
        os.environ[_monitored_resources._GAE_SERVICE_ENV] = self.NAME
        os.environ[_monitored_resources._GAE_VERSION_ENV] = self.VERSION
        with patch:
            resource = _create_app_engine_resource()
            self.assertIsInstance(resource, Resource)
            self.assertEqual(resource.type, "gae_app")
            self.assertEqual(resource.labels["project_id"], self.PROJECT)
            self.assertEqual(resource.labels["module_id"], self.NAME)
            self.assertEqual(resource.labels["version_id"], self.VERSION)
            self.assertEqual(resource.labels["zone"], self.LOCATION)

    def test_global_resource(self):
        resource = _create_global_resource(self.PROJECT)
        self.assertIsInstance(resource, Resource)
        self.assertEqual(resource.type, "global")
        self.assertEqual(resource.labels["project_id"], self.PROJECT)

    def test_with_no_project_from_server(self):
        """
        Ensure project_id uses an empty string if not known
        https://github.com/googleapis/python-logging/issues/710
        """
        patch = mock.patch(
            "google.cloud.logging_v2.handlers._monitored_resources.retrieve_metadata_server",
            wraps=self._mock_metadata_no_project,
        )
        with patch:
            _global_resource_patched = functools.partial(_create_global_resource, None)
            resource_fns = [
                _global_resource_patched,
                _create_app_engine_resource,
                _create_cloud_run_service_resource,
                _create_cloud_run_job_resource,
                _create_compute_resource,
                _create_kubernetes_resource,
                _create_functions_resource,
            ]
            for fn in resource_fns:
                resource = fn()
                self.assertEqual(resource.labels["project_id"], "")


class Test_Resource_Detection(unittest.TestCase):
    PROJECT = "test-project"

    def _mock_k8s_metadata(self, endpoint):
        if (
            endpoint == _monitored_resources._GKE_CLUSTER_NAME
            or endpoint == _monitored_resources._GCE_INSTANCE_ID
        ):
            return "TRUE"
        else:
            return None

    def _mock_gce_metadata(self, endpoint):
        if endpoint == _monitored_resources._GCE_INSTANCE_ID:
            return "TRUE"
        else:
            return None

    def _mock_partial_metadata(self, endpoint):
        if endpoint == _monitored_resources._ZONE_ID:
            return "ZONE"
        elif endpoint == _monitored_resources._GCE_INSTANCE_ID:
            return "instance"
        else:
            return None

    def setUp(self):
        os.environ.clear()

    def test_detect_appengine(self):
        for env in _monitored_resources._GAE_ENV_VARS:
            os.environ[env] = "TRUE"
        resource = detect_resource(self.PROJECT)
        self.assertIsInstance(resource, Resource)
        self.assertEqual(resource.type, "gae_app")

    def test_detect_kubernetes(self):
        patch = mock.patch(
            "google.cloud.logging_v2.handlers._monitored_resources.retrieve_metadata_server",
            wraps=self._mock_k8s_metadata,
        )
        with patch:
            resource = detect_resource(self.PROJECT)
            self.assertIsInstance(resource, Resource)
            self.assertEqual(resource.type, "k8s_container")

    def test_detect_functions(self):
        for env in _monitored_resources._FUNCTION_ENV_VARS:
            os.environ[env] = "TRUE"
        resource = detect_resource(self.PROJECT)
        self.assertIsInstance(resource, Resource)
        self.assertEqual(resource.type, "cloud_function")

    def test_detect_legacy_functions(self):
        for env in _monitored_resources._LEGACY_FUNCTION_ENV_VARS:
            os.environ[env] = "TRUE"
        resource = detect_resource(self.PROJECT)
        self.assertIsInstance(resource, Resource)
        self.assertEqual(resource.type, "cloud_function")

    def test_detect_cloud_run_service(self):
        for env in _monitored_resources._CLOUD_RUN_SERVICE_ENV_VARS:
            os.environ[env] = "TRUE"
        resource = detect_resource(self.PROJECT)
        self.assertIsInstance(resource, Resource)
        self.assertEqual(resource.type, "cloud_run_revision")

    def test_detect_cloud_run_job(self):
        for env in _monitored_resources._CLOUD_RUN_JOB_ENV_VARS:
            os.environ[env] = "TRUE"
        resource = detect_resource(self.PROJECT)
        self.assertIsInstance(resource, Resource)
        self.assertEqual(resource.type, "cloud_run_job")

    def test_detect_compute_engine(self):
        patch = mock.patch(
            "google.cloud.logging_v2.handlers._monitored_resources.retrieve_metadata_server",
            wraps=self._mock_gce_metadata,
        )
        with patch:
            resource = detect_resource(self.PROJECT)
            self.assertIsInstance(resource, Resource)
            self.assertEqual(resource.type, "gce_instance")

    def test_detection_unknown(self):
        patch = mock.patch(
            "google.cloud.logging_v2.handlers._monitored_resources.retrieve_metadata_server",
            return_value=None,
        )
        with patch:
            resource = detect_resource(self.PROJECT)
            self.assertIsInstance(resource, Resource)
            self.assertEqual(resource.type, "global")

    def test_detect_partial_data(self):
        """
        Test case where the metadata server returns partial data
        """
        patch = mock.patch(
            "google.cloud.logging_v2.handlers._monitored_resources.retrieve_metadata_server",
            wraps=self._mock_partial_metadata,
        )
        with patch:
            resource = detect_resource(self.PROJECT)
            self.assertIsInstance(resource, Resource)
            self.assertEqual(resource.type, "gce_instance")
            # project id not returned from metadata serve
            # should be empty string
            self.assertEqual(resource.labels["project_id"], "")


@pytest.mark.parametrize(
    "resource_type,os_environ,record_attrs,expected_labels",
    [
        (
            _monitored_resources._GAE_RESOURCE_TYPE,
            {},
            {"_trace": "trace_id"},
            {_monitored_resources._GAE_TRACE_ID_LABEL: "trace_id"},
        ),
        (
            _monitored_resources._CLOUD_RUN_JOB_RESOURCE_TYPE,
            {
                _monitored_resources._CLOUD_RUN_EXECUTION_ID: "test_job_12345",
                _monitored_resources._CLOUD_RUN_TASK_INDEX: "1",
                _monitored_resources._CLOUD_RUN_TASK_ATTEMPT: "12",
            },
            {},
            {
                _monitored_resources._CLOUD_RUN_JOBS_EXECUTION_NAME_LABEL: "test_job_12345",
                _monitored_resources._CLOUD_RUN_JOBS_TASK_INDEX_LABEL: "1",
                _monitored_resources._CLOUD_RUN_JOBS_TASK_ATTEMPT_LABEL: "12",
            },
        ),
        ("global", {}, {}, {}),
    ],
)
def test_add_resource_labels(resource_type, os_environ, record_attrs, expected_labels):
    os.environ.clear()
    record = logging.LogRecord("logname", None, None, None, "test", None, None)

    resource = Resource(type=resource_type, labels={})

    for attr, val in record_attrs.items():
        setattr(record, attr, val)

    os.environ.update(os_environ)

    labels = add_resource_labels(resource, record)

    assert expected_labels == labels
