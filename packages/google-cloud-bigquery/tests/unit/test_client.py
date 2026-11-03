# Copyright 2015 Google LLC
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

import collections
import copy
import datetime
import decimal
import gzip
import http.client
import io
import itertools
import json
import operator
import os
import unittest
import warnings
from unittest import mock

import packaging
import pytest
import requests

try:
    import opentelemetry.sdk as opentelemetry
except ImportError:
    opentelemetry = None

if opentelemetry is not None:
    try:
        from opentelemetry import trace
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import SimpleSpanProcessor
        from opentelemetry.sdk.trace.export.in_memory_span_exporter import (
            InMemorySpanExporter,
        )
    except (ImportError, AttributeError) as exc:  # pragma: NO COVER
        msg = "Error importing from opentelemetry, is the installed version compatible?"
        raise ImportError(msg) from exc

import google.api_core.exceptions
import google.cloud._helpers
import google.cloud.bigquery.retry
import google.cloud.bigquery.table
from google.api_core import client_info
from google.cloud import bigquery
from google.cloud.bigquery import ParquetOptions, exceptions, version
from google.cloud.bigquery.dataset import Dataset, DatasetReference
from google.cloud.bigquery.enums import DatasetView, TimestampPrecision, UpdateMode
from google.cloud.bigquery.retry import DEFAULT_TIMEOUT
from test_utils.imports import maybe_fail_import

from tests.unit.helpers import make_connection


def _make_credentials():
    import google.auth.credentials

    return mock.Mock(spec=google.auth.credentials.Credentials)


def _make_list_partitons_meta_info(project, dataset_id, table_id, num_rows=0):
    return {
        "tableReference": {
            "projectId": project,
            "datasetId": dataset_id,
            "tableId": "{}$__PARTITIONS_SUMMARY__".format(table_id),
        },
        "schema": {
            "fields": [
                {"name": "project_id", "type": "STRING", "mode": "NULLABLE"},
                {"name": "dataset_id", "type": "STRING", "mode": "NULLABLE"},
                {"name": "table_id", "type": "STRING", "mode": "NULLABLE"},
                {"name": "partition_id", "type": "STRING", "mode": "NULLABLE"},
            ]
        },
        "etag": "ETAG",
        "numRows": num_rows,
    }


class TestClient(unittest.TestCase):
    PROJECT = "PROJECT"
    DS_ID = "DATASET_ID"
    TABLE_ID = "TABLE_ID"
    MODEL_ID = "MODEL_ID"
    TABLE_REF = DatasetReference(PROJECT, DS_ID).table(TABLE_ID)
    KMS_KEY_NAME = "projects/1/locations/us/keyRings/1/cryptoKeys/1"
    LOCATION = "us-central"

    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.client import Client

        return Client

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def _make_table_resource(self):
        return {
            "id": "%s:%s:%s" % (self.PROJECT, self.DS_ID, self.TABLE_ID),
            "tableReference": {
                "projectId": self.PROJECT,
                "datasetId": self.DS_ID,
                "tableId": self.TABLE_ID,
            },
        }

    def test_ctor_defaults(self):
        from google.cloud.bigquery._http import Connection

        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        self.assertIsInstance(client._connection, Connection)
        self.assertIs(client._connection.credentials, creds)
        self.assertIs(client._connection.http, http)
        self.assertIsNone(client.location)
        self.assertEqual(
            client._connection.API_BASE_URL, Connection.DEFAULT_API_ENDPOINT
        )

    def test_ctor_w_empty_client_options(self):
        from google.api_core.client_options import ClientOptions

        creds = _make_credentials()
        http = object()
        client_options = ClientOptions()
        client = self._make_one(
            project=self.PROJECT,
            credentials=creds,
            _http=http,
            client_options=client_options,
        )
        self.assertEqual(
            client._connection.API_BASE_URL, client._connection.DEFAULT_API_ENDPOINT
        )

    @mock.patch.dict(os.environ, {"GOOGLE_CLOUD_UNIVERSE_DOMAIN": "foo.com"})
    def test_ctor_w_only_env_universe(self):
        creds = _make_credentials()
        http = object()
        client = self._make_one(
            project=self.PROJECT,
            credentials=creds,
            _http=http,
        )
        self.assertEqual(client._connection.API_BASE_URL, "https://bigquery.foo.com")

    def test_ctor_w_client_options_dict(self):
        creds = _make_credentials()
        http = object()
        client_options = {"api_endpoint": "https://www.foo-googleapis.com"}
        client = self._make_one(
            project=self.PROJECT,
            credentials=creds,
            _http=http,
            client_options=client_options,
        )
        self.assertEqual(
            client._connection.API_BASE_URL, "https://www.foo-googleapis.com"
        )

    def test_ctor_w_client_options_object(self):
        from google.api_core.client_options import ClientOptions

        creds = _make_credentials()
        http = object()
        client_options = ClientOptions(api_endpoint="https://www.foo-googleapis.com")
        client = self._make_one(
            project=self.PROJECT,
            credentials=creds,
            _http=http,
            client_options=client_options,
        )
        self.assertEqual(
            client._connection.API_BASE_URL, "https://www.foo-googleapis.com"
        )

    @pytest.mark.skipif(
        packaging.version.parse(getattr(google.api_core, "__version__", "0.0.0"))
        < packaging.version.Version("2.15.0"),
        reason="universe_domain not supported with google-api-core < 2.15.0",
    )
    def test_ctor_w_client_options_universe(self):
        creds = _make_credentials()
        http = object()
        client_options = {"universe_domain": "foo.com"}
        client = self._make_one(
            project=self.PROJECT,
            credentials=creds,
            _http=http,
            client_options=client_options,
        )
        self.assertEqual(client._connection.API_BASE_URL, "https://bigquery.foo.com")

    def test_ctor_w_job_creation_mode(self):
        creds = _make_credentials()
        http = object()
        client = self._make_one(
            project=self.PROJECT,
            credentials=creds,
            _http=http,
            default_job_creation_mode="foo",
        )
        self.assertEqual(client.default_job_creation_mode, "foo")

    def test_ctor_w_location(self):
        from google.cloud.bigquery._http import Connection

        creds = _make_credentials()
        http = object()
        location = "us-central"
        client = self._make_one(
            project=self.PROJECT, credentials=creds, _http=http, location=location
        )
        self.assertIsInstance(client._connection, Connection)
        self.assertIs(client._connection.credentials, creds)
        self.assertIs(client._connection.http, http)
        self.assertEqual(client.location, location)

    def test_ctor_w_query_job_config(self):
        from google.cloud.bigquery import QueryJobConfig
        from google.cloud.bigquery._http import Connection

        creds = _make_credentials()
        http = object()
        location = "us-central"
        job_config = QueryJobConfig()
        job_config.dry_run = True

        client = self._make_one(
            project=self.PROJECT,
            credentials=creds,
            _http=http,
            location=location,
            default_query_job_config=job_config,
        )
        self.assertIsInstance(client._connection, Connection)
        self.assertIs(client._connection.credentials, creds)
        self.assertIs(client._connection.http, http)
        self.assertEqual(client.location, location)

        self.assertIsInstance(client._default_query_job_config, QueryJobConfig)
        self.assertTrue(client._default_query_job_config.dry_run)

    def test_ctor_w_load_job_config(self):
        from google.cloud.bigquery import LoadJobConfig
        from google.cloud.bigquery._http import Connection

        creds = _make_credentials()
        http = object()
        location = "us-central"
        job_config = LoadJobConfig()
        job_config.create_session = True

        client = self._make_one(
            project=self.PROJECT,
            credentials=creds,
            _http=http,
            location=location,
            default_load_job_config=job_config,
        )
        self.assertIsInstance(client._connection, Connection)
        self.assertIs(client._connection.credentials, creds)
        self.assertIs(client._connection.http, http)
        self.assertEqual(client.location, location)

        self.assertIsInstance(client._default_load_job_config, LoadJobConfig)
        self.assertTrue(client._default_load_job_config.create_session)

    def test__call_api_extra_headers(self):
        # Note: We test at a lower layer to ensure that extra headers are
        # populated when we actually make the call in requests.
        # Arrange
        http = mock.create_autospec(requests.Session, instance=True)
        http.is_mtls = False
        response = mock.create_autospec(requests.Response, instance=True)
        response.status_code = 200
        http.request.return_value = response
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)

        # Act
        client._connection.extra_headers = {"x-goog-request-reason": "because-friday"}
        client._call_api(
            retry=None, method="GET", path="/bigquery/v2/projects/my-proj/jobs/my-job"
        )

        # Assert
        http.request.assert_called_once()
        _, kwargs = http.request.call_args
        headers = kwargs["headers"]
        assert headers["x-goog-request-reason"] == "because-friday"

    def test__call_api_span_creator_not_called(self):
        from concurrent.futures import TimeoutError

        from google.cloud.bigquery.retry import DEFAULT_RETRY

        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)

        api_request_patcher = mock.patch.object(
            client._connection,
            "api_request",
            side_effect=[TimeoutError, "result"],
        )
        retry = DEFAULT_RETRY.with_deadline(1).with_predicate(
            lambda exc: isinstance(exc, TimeoutError)
        )

        with api_request_patcher:
            with mock.patch(
                "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
            ) as final_attributes:
                client._call_api(retry)

            final_attributes.assert_not_called()

    def test__call_api_span_creator_called(self):
        from concurrent.futures import TimeoutError

        from google.cloud.bigquery.retry import DEFAULT_RETRY

        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)

        api_request_patcher = mock.patch.object(
            client._connection,
            "api_request",
            side_effect=[TimeoutError, "result"],
        )
        retry = DEFAULT_RETRY.with_deadline(1).with_predicate(
            lambda exc: isinstance(exc, TimeoutError)
        )

        with api_request_patcher:
            with mock.patch(
                "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
            ) as final_attributes:
                client._call_api(
                    retry,
                    span_name="test_name",
                    span_attributes={"test_attribute": "test_attribute-value"},
                )

            final_attributes.assert_called_once()

    def test__get_query_results_miss_w_explicit_project_and_timeout(self):
        from google.cloud.exceptions import NotFound

        creds = _make_credentials()
        client = self._make_one(self.PROJECT, creds)
        conn = client._connection = make_connection()
        path = "/projects/other-project/queries/nothere"
        with self.assertRaises(NotFound):
            with mock.patch(
                "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
            ) as final_attributes:
                client._get_query_results(
                    "nothere",
                    None,
                    project="other-project",
                    location=self.LOCATION,
                    timeout_ms=500,
                    timeout=420,
                )

        final_attributes.assert_called_once_with({"path": path}, client, None)

        conn.api_request.assert_called_once_with(
            method="GET",
            path=path,
            query_params={"maxResults": 0, "timeoutMs": 500, "location": self.LOCATION},
            timeout=420,
        )

    def test__get_query_results_miss_w_short_timeout(self):
        import google.cloud.bigquery.client
        from google.cloud.exceptions import NotFound

        creds = _make_credentials()
        client = self._make_one(self.PROJECT, creds)
        conn = client._connection = make_connection()
        path = "/projects/other-project/queries/nothere"
        with self.assertRaises(NotFound):
            client._get_query_results(
                "nothere",
                None,
                project="other-project",
                location=self.LOCATION,
                timeout_ms=500,
                timeout=1,
            )

        conn.api_request.assert_called_once_with(
            method="GET",
            path=path,
            query_params={"maxResults": 0, "timeoutMs": 500, "location": self.LOCATION},
            timeout=google.cloud.bigquery.client._MIN_GET_QUERY_RESULTS_TIMEOUT,
        )

    def test__get_query_results_miss_w_default_timeout(self):
        import google.cloud.bigquery.client
        from google.cloud.exceptions import NotFound

        creds = _make_credentials()
        client = self._make_one(self.PROJECT, creds)
        conn = client._connection = make_connection()
        path = "/projects/other-project/queries/nothere"
        with self.assertRaises(NotFound):
            client._get_query_results(
                "nothere",
                None,
                project="other-project",
                location=self.LOCATION,
                timeout_ms=500,
                timeout=object(),  # the api core default timeout
            )

        conn.api_request.assert_called_once_with(
            method="GET",
            path=path,
            query_params={"maxResults": 0, "timeoutMs": 500, "location": self.LOCATION},
            timeout=google.cloud.bigquery.client._MIN_GET_QUERY_RESULTS_TIMEOUT,
        )

    def test__get_query_results_miss_w_client_location(self):
        from google.cloud.exceptions import NotFound

        creds = _make_credentials()
        client = self._make_one(self.PROJECT, creds, location=self.LOCATION)
        conn = client._connection = make_connection()

        with self.assertRaises(NotFound):
            client._get_query_results("nothere", None)

        conn.api_request.assert_called_once_with(
            method="GET",
            path="/projects/PROJECT/queries/nothere",
            query_params={"maxResults": 0, "location": self.LOCATION},
            timeout=DEFAULT_TIMEOUT,
        )

    def test__get_query_results_hit(self):
        job_id = "query_job"
        data = {
            "kind": "bigquery#getQueryResultsResponse",
            "etag": "some-tag",
            "schema": {
                "fields": [
                    {"name": "title", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "unique_words", "type": "INTEGER", "mode": "NULLABLE"},
                ]
            },
            "jobReference": {"projectId": self.PROJECT, "jobId": job_id},
            "totalRows": "10",
            "totalBytesProcessed": "2464625",
            "jobComplete": True,
            "cacheHit": False,
        }

        creds = _make_credentials()
        client = self._make_one(self.PROJECT, creds)
        client._connection = make_connection(data)
        query_results = client._get_query_results(job_id, None)

        self.assertEqual(query_results.total_rows, 10)
        self.assertTrue(query_results.complete)

    def test__list_rows_from_query_results_w_none_timeout(self):
        from google.cloud.bigquery.schema import SchemaField
        from google.cloud.exceptions import NotFound

        creds = _make_credentials()
        client = self._make_one(self.PROJECT, creds)
        conn = client._connection = make_connection()
        path = "/projects/project/queries/nothere"
        iterator = client._list_rows_from_query_results(
            "nothere",
            location=None,
            project="project",
            schema=[
                SchemaField("f1", "STRING", mode="REQUIRED"),
                SchemaField("f2", "INTEGER", mode="REQUIRED"),
            ],
            timeout=None,
        )

        # trigger the iterator to request data
        with self.assertRaises(NotFound):
            iterator._get_next_page_response()

        conn.api_request.assert_called_once_with(
            method="GET",
            path=path,
            query_params={
                "fields": "jobReference,totalRows,pageToken,rows",
                "location": None,
                "formatOptions.useInt64Timestamp": True,
            },
            timeout=None,
        )

    def test__list_rows_from_query_results_w_default_timeout(self):
        import google.cloud.bigquery.client
        from google.cloud.bigquery.schema import SchemaField
        from google.cloud.exceptions import NotFound

        creds = _make_credentials()
        client = self._make_one(self.PROJECT, creds)
        conn = client._connection = make_connection()
        path = "/projects/project/queries/nothere"
        iterator = client._list_rows_from_query_results(
            "nothere",
            location=None,
            project="project",
            schema=[
                SchemaField("f1", "STRING", mode="REQUIRED"),
                SchemaField("f2", "INTEGER", mode="REQUIRED"),
            ],
            timeout=object(),
        )

        # trigger the iterator to request data
        with self.assertRaises(NotFound):
            iterator._get_next_page_response()

        conn.api_request.assert_called_once_with(
            method="GET",
            path=path,
            query_params={
                "fields": "jobReference,totalRows,pageToken,rows",
                "location": None,
                "formatOptions.useInt64Timestamp": True,
            },
            timeout=google.cloud.bigquery.client._MIN_GET_QUERY_RESULTS_TIMEOUT,
        )

    def test_default_query_job_config(self):
        from google.cloud.bigquery import QueryJobConfig

        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        self.assertIsNone(client.default_query_job_config)

        job_config = QueryJobConfig()
        job_config.dry_run = True
        client.default_query_job_config = job_config
        self.assertIsInstance(client.default_query_job_config, QueryJobConfig)

    def test_default_load_job_config(self):
        from google.cloud.bigquery import LoadJobConfig

        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        self.assertIsNone(client.default_load_job_config)

        job_config = LoadJobConfig()
        job_config.create_session = True
        client.default_load_job_config = job_config
        self.assertIsInstance(client.default_load_job_config, LoadJobConfig)

    def test_get_service_account_email(self):
        path = "/projects/%s/serviceAccount" % (self.PROJECT,)
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        email = "bq-123@bigquery-encryption.iam.gserviceaccount.com"
        resource = {"kind": "bigquery#getServiceAccountResponse", "email": email}
        conn = client._connection = make_connection(resource)
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            service_account_email = client.get_service_account_email(timeout=7.5)

        final_attributes.assert_called_once_with({"path": path}, client, None)
        conn.api_request.assert_called_once_with(method="GET", path=path, timeout=7.5)
        self.assertEqual(service_account_email, email)

    def test_get_service_account_email_w_alternate_project(self):
        project = "my-alternate-project"
        path = "/projects/%s/serviceAccount" % (project,)
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        email = "bq-123@bigquery-encryption.iam.gserviceaccount.com"
        resource = {"kind": "bigquery#getServiceAccountResponse", "email": email}
        conn = client._connection = make_connection(resource)
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            service_account_email = client.get_service_account_email(project=project)

        final_attributes.assert_called_once_with({"path": path}, client, None)
        conn.api_request.assert_called_once_with(
            method="GET", path=path, timeout=DEFAULT_TIMEOUT
        )
        self.assertEqual(service_account_email, email)

    def test_dataset_with_specified_project(self):
        from google.cloud.bigquery.dataset import DatasetReference

        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        catch_warnings = warnings.catch_warnings(record=True)

        with catch_warnings as warned:
            dataset = client.dataset(self.DS_ID, self.PROJECT)

        matches = [
            warning
            for warning in warned
            if warning.category in (DeprecationWarning, PendingDeprecationWarning)
            and "Client.dataset" in str(warning)
            and "my_project.my_dataset" in str(warning)
        ]
        assert matches, "A Client.dataset deprecation warning was not raised."
        self.assertIsInstance(dataset, DatasetReference)
        self.assertEqual(dataset.dataset_id, self.DS_ID)
        self.assertEqual(dataset.project, self.PROJECT)

    def test_dataset_with_default_project(self):
        from google.cloud.bigquery.dataset import DatasetReference

        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        catch_warnings = warnings.catch_warnings(record=True)

        with catch_warnings as warned:
            dataset = client.dataset(self.DS_ID)

        matches = [
            warning
            for warning in warned
            if warning.category in (DeprecationWarning, PendingDeprecationWarning)
            and "Client.dataset" in str(warning)
            and "my_project.my_dataset" in str(warning)
        ]
        assert matches, "A Client.dataset deprecation warning was not raised."
        self.assertIsInstance(dataset, DatasetReference)
        self.assertEqual(dataset.dataset_id, self.DS_ID)
        self.assertEqual(dataset.project, self.PROJECT)

    def test_get_dataset(self):
        from google.cloud.exceptions import ServerError

        path = "projects/%s/datasets/%s" % (self.PROJECT, self.DS_ID)
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        resource = {
            "id": "%s:%s" % (self.PROJECT, self.DS_ID),
            "datasetReference": {"projectId": self.PROJECT, "datasetId": self.DS_ID},
        }
        conn = client._connection = make_connection(resource)
        dataset_ref = DatasetReference(self.PROJECT, self.DS_ID)
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            dataset = client.get_dataset(dataset_ref, timeout=7.5)

        final_attributes.assert_called_once_with({"path": "/%s" % path}, client, None)

        conn.api_request.assert_called_once_with(
            method="GET", path="/%s" % path, timeout=7.5, query_params={}
        )
        self.assertEqual(dataset.dataset_id, self.DS_ID)

        # Test retry.

        # Not a cloud API exception (missing 'errors' field).
        client._connection = make_connection(Exception(""), resource)
        with self.assertRaises(Exception):
            with mock.patch(
                "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
            ) as final_attributes:
                client.get_dataset(dataset_ref)

        final_attributes.assert_called_once_with({"path": "/%s" % path}, client, None)

        # Zero-length errors field.
        client._connection = make_connection(ServerError(""), resource)
        with self.assertRaises(ServerError):
            with mock.patch(
                "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
            ) as final_attributes:
                client.get_dataset(dataset_ref)

        final_attributes.assert_called_once_with({"path": "/%s" % path}, client, None)

        # Non-retryable reason.
        client._connection = make_connection(
            ServerError("", errors=[{"reason": "serious"}]), resource
        )
        with self.assertRaises(ServerError):
            with mock.patch(
                "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
            ) as final_attributes:
                client.get_dataset(dataset_ref)

        final_attributes.assert_called_once_with({"path": "/%s" % path}, client, None)

        # Retryable reason, but retry is disabled.
        client._connection = make_connection(
            ServerError("", errors=[{"reason": "backendError"}]), resource
        )
        with self.assertRaises(ServerError):
            with mock.patch(
                "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
            ) as final_attributes:
                client.get_dataset(dataset_ref, retry=None)

        final_attributes.assert_called_once_with({"path": "/%s" % path}, client, None)

        # Retryable reason, default retry: success.
        client._connection = make_connection(
            ServerError("", errors=[{"reason": "backendError"}]), resource
        )
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            dataset = client.get_dataset(
                # Test with a string for dataset ID.
                dataset_ref.dataset_id
            )

        final_attributes.assert_called_once_with({"path": "/%s" % path}, client, None)

        self.assertEqual(dataset.dataset_id, self.DS_ID)

    def test_get_dataset_with_dataset_view(self):
        path = "projects/%s/datasets/%s" % (self.PROJECT, self.DS_ID)
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        resource = {
            "id": "%s:%s" % (self.PROJECT, self.DS_ID),
            "datasetReference": {"projectId": self.PROJECT, "datasetId": self.DS_ID},
        }
        dataset_ref = DatasetReference(self.PROJECT, self.DS_ID)

        test_cases = [
            (None, None),
            (DatasetView.DATASET_VIEW_UNSPECIFIED, "DATASET_VIEW_UNSPECIFIED"),
            (DatasetView.METADATA, "METADATA"),
            (DatasetView.ACL, "ACL"),
            (DatasetView.FULL, "FULL"),
        ]

        for dataset_view_arg, expected_param_value in test_cases:
            with self.subTest(
                dataset_view_arg=str(dataset_view_arg),
                expected_param_value=expected_param_value,
            ):
                # Re-initialize the connection mock for each sub-test to reset side_effect
                conn = client._connection = make_connection(resource)

                dataset = client.get_dataset(dataset_ref, dataset_view=dataset_view_arg)

                self.assertEqual(dataset.dataset_id, self.DS_ID)

                if expected_param_value:
                    expected_query_params = {"datasetView": expected_param_value}
                else:
                    expected_query_params = {}

                conn.api_request.assert_called_once_with(
                    method="GET",
                    path="/%s" % path,
                    timeout=DEFAULT_TIMEOUT,
                    query_params=expected_query_params if expected_query_params else {},
                )

    def test_get_dataset_with_invalid_dataset_view(self):
        invalid_view_values = [
            "INVALID_STRING",
            123,
            123.45,
            object(),
        ]
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        resource = {
            "id": "%s:%s" % (self.PROJECT, self.DS_ID),
            "datasetReference": {"projectId": self.PROJECT, "datasetId": self.DS_ID},
        }
        conn = client._connection = make_connection(resource)
        dataset_ref = DatasetReference(self.PROJECT, self.DS_ID)

        for invalid_view_value in invalid_view_values:
            with self.subTest(invalid_view_value=str(invalid_view_value)):
                conn.api_request.reset_mock()  # Reset mock for each sub-test
                with self.assertRaises(AttributeError):
                    client.get_dataset(dataset_ref, dataset_view=invalid_view_value)

    def test_ensure_bqstorage_client_creating_new_instance(self):
        bigquery_storage = pytest.importorskip("google.cloud.bigquery_storage")
        import google.api_core.gapic_v1.client_info

        mock_client = mock.create_autospec(bigquery_storage.BigQueryReadClient)
        mock_client_instance = object()
        mock_client.return_value = mock_client_instance
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)

        client_info = google.api_core.gapic_v1.client_info.ClientInfo(
            user_agent="test-agent"
        )

        with mock.patch(
            "google.cloud.bigquery_storage.BigQueryReadClient", mock_client
        ):
            bqstorage_client = client._ensure_bqstorage_client(
                client_options=mock.sentinel.client_options,
                client_info=client_info,
            )

        self.assertIs(bqstorage_client, mock_client_instance)
        mock_client.assert_called_once()
        _, kwargs = mock_client.call_args
        self.assertIs(kwargs["credentials"], creds)
        self.assertIs(kwargs["client_options"], mock.sentinel.client_options)
        self.assertIn("test-agent", kwargs["client_info"].user_agent)
        self.assertIn("pandas-gbq", kwargs["client_info"].user_agent)
        self.assertIn(
            f"legacy-gcb/{version.__version__}", kwargs["client_info"].user_agent
        )

    def test_ensure_bqstorage_client_default_universe(self):
        bigquery_storage = pytest.importorskip("google.cloud.bigquery_storage")

        mock_client = mock.create_autospec(bigquery_storage.BigQueryReadClient)
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)

        with mock.patch(
            "google.cloud.bigquery_storage.BigQueryReadClient", mock_client
        ):
            client._ensure_bqstorage_client()

        _, kwargs = mock_client.call_args
        self.assertIsNone(kwargs["client_options"])

    def test_ensure_bqstorage_client_uses_client_universe(self):
        bigquery_storage = pytest.importorskip("google.cloud.bigquery_storage")

        mock_client = mock.create_autospec(bigquery_storage.BigQueryReadClient)
        creds = _make_credentials()
        client = self._make_one(
            project=self.PROJECT,
            credentials=creds,
            client_options={"universe_domain": "foo.com"},
        )

        with mock.patch(
            "google.cloud.bigquery_storage.BigQueryReadClient", mock_client
        ):
            client._ensure_bqstorage_client()

        _, kwargs = mock_client.call_args
        self.assertEqual(kwargs["client_options"].universe_domain, "foo.com")

    def test_ensure_bqstorage_client_keeps_given_client_options(self):
        bigquery_storage = pytest.importorskip("google.cloud.bigquery_storage")

        mock_client = mock.create_autospec(bigquery_storage.BigQueryReadClient)
        creds = _make_credentials()
        client = self._make_one(
            project=self.PROJECT,
            credentials=creds,
            client_options={"universe_domain": "foo.com"},
        )

        with mock.patch(
            "google.cloud.bigquery_storage.BigQueryReadClient", mock_client
        ):
            client._ensure_bqstorage_client(client_options=mock.sentinel.client_options)

        _, kwargs = mock_client.call_args
        self.assertIs(kwargs["client_options"], mock.sentinel.client_options)

    def test_ensure_bqstorage_client_pandas_gbq_installed(self):
        bigquery_storage = pytest.importorskip("google.cloud.bigquery_storage")
        import sys

        import google.api_core.gapic_v1.client_info

        mock_client = mock.create_autospec(bigquery_storage.BigQueryReadClient)
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        client_info = google.api_core.gapic_v1.client_info.ClientInfo(
            user_agent="app-agent"
        )

        mock_pandas = mock.Mock()
        mock_pandas.__version__ = "0.13.0"

        with (
            mock.patch("google.cloud.bigquery_storage.BigQueryReadClient", mock_client),
            mock.patch.dict(sys.modules, {"pandas_gbq": mock_pandas}),
        ):
            client._ensure_bqstorage_client(client_info=client_info)

        mock_client.assert_called_once()
        _, kwargs = mock_client.call_args
        self.assertEqual(
            kwargs["client_info"].user_agent,
            f"app-agent legacy-gcb/{version.__version__} pandas-gbq/0.13.0",
        )

    def test_ensure_bqstorage_client_pandas_gbq_not_installed(self):
        bigquery_storage = pytest.importorskip("google.cloud.bigquery_storage")
        import sys

        import google.api_core.gapic_v1.client_info

        mock_client = mock.create_autospec(bigquery_storage.BigQueryReadClient)
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        client_info = google.api_core.gapic_v1.client_info.ClientInfo(
            user_agent="app-agent"
        )

        with (
            mock.patch("google.cloud.bigquery_storage.BigQueryReadClient", mock_client),
            mock.patch.dict(sys.modules, {"pandas_gbq": None}),
        ):
            client._ensure_bqstorage_client(client_info=client_info)

        mock_client.assert_called_once()
        _, kwargs = mock_client.call_args
        self.assertEqual(
            kwargs["client_info"].user_agent,
            f"app-agent legacy-gcb/{version.__version__} pandas-gbq/0.0.0",
        )

    def test_ensure_bqstorage_client_client_info_none(self):
        bigquery_storage = pytest.importorskip("google.cloud.bigquery_storage")
        import sys

        mock_client = mock.create_autospec(bigquery_storage.BigQueryReadClient)
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)

        with (
            mock.patch("google.cloud.bigquery_storage.BigQueryReadClient", mock_client),
            mock.patch.dict(sys.modules, {"pandas_gbq": None}),
        ):
            client._ensure_bqstorage_client(client_info=None)

        mock_client.assert_called_once()
        _, kwargs = mock_client.call_args
        self.assertEqual(
            kwargs["client_info"].user_agent,
            f"legacy-gcb/{version.__version__} pandas-gbq/0.0.0",
        )

    def test_ensure_bqstorage_client_client_info_user_agent_none(self):
        bigquery_storage = pytest.importorskip("google.cloud.bigquery_storage")
        import sys

        import google.api_core.gapic_v1.client_info

        mock_client = mock.create_autospec(bigquery_storage.BigQueryReadClient)
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)

        client_info = google.api_core.gapic_v1.client_info.ClientInfo(user_agent=None)

        with (
            mock.patch("google.cloud.bigquery_storage.BigQueryReadClient", mock_client),
            mock.patch.dict(sys.modules, {"pandas_gbq": None}),
        ):
            client._ensure_bqstorage_client(client_info=client_info)

        mock_client.assert_called_once()
        _, kwargs = mock_client.call_args
        self.assertEqual(
            kwargs["client_info"].user_agent,
            f"legacy-gcb/{version.__version__} pandas-gbq/0.0.0",
        )

    def test_ensure_bqstorage_client_missing_dependency(self):
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)

        def fail_bqstorage_import(name, globals, locals, fromlist, level):
            # NOTE: *very* simplified, assuming a straightforward absolute import
            return "bigquery_storage" in name or (
                fromlist is not None and "bigquery_storage" in fromlist
            )

        no_bqstorage = maybe_fail_import(predicate=fail_bqstorage_import)

        with no_bqstorage, warnings.catch_warnings(record=True) as warned:
            bqstorage_client = client._ensure_bqstorage_client()

        self.assertIsNone(bqstorage_client)
        matching_warnings = [
            warning
            for warning in warned
            if "not installed" in str(warning)
            and "google-cloud-bigquery-storage" in str(warning)
        ]
        assert matching_warnings, "Missing dependency warning not raised."

    def test_ensure_bqstorage_client_obsolete_dependency(self):
        pytest.importorskip("google.cloud.bigquery_storage")
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)

        patcher = mock.patch(
            "google.cloud.bigquery.client._versions_helpers.BQ_STORAGE_VERSIONS.try_import",
            side_effect=exceptions.LegacyBigQueryStorageError("BQ Storage too old"),
        )
        with patcher, warnings.catch_warnings(record=True) as warned:
            bqstorage_client = client._ensure_bqstorage_client()

        self.assertIsNone(bqstorage_client)
        matching_warnings = [
            warning for warning in warned if "BQ Storage too old" in str(warning)
        ]
        assert matching_warnings, "Obsolete dependency warning not raised."

    def test_ensure_bqstorage_client_existing_client_check_passes(self):
        pytest.importorskip("google.cloud.bigquery_storage")
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        mock_storage_client = mock.sentinel.mock_storage_client

        bqstorage_client = client._ensure_bqstorage_client(
            bqstorage_client=mock_storage_client
        )

        self.assertIs(bqstorage_client, mock_storage_client)

    def test_ensure_bqstorage_client_is_none(self):
        pytest.importorskip("google.cloud.bigquery_storage")
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        bqstorage_client = None

        assert bqstorage_client is None
        bqstorage_client = client._ensure_bqstorage_client(
            bqstorage_client=bqstorage_client,
        )

        assert isinstance(
            bqstorage_client, google.cloud.bigquery_storage_v1.BigQueryReadClient
        )

    def test_ensure_bqstorage_client_existing_client_check_fails(self):
        pytest.importorskip("google.cloud.bigquery_storage")
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        mock_storage_client = mock.sentinel.mock_storage_client

        patcher = mock.patch(
            "google.cloud.bigquery.client._versions_helpers.BQ_STORAGE_VERSIONS.try_import",
            side_effect=exceptions.LegacyBigQueryStorageError("BQ Storage too old"),
        )
        with patcher, warnings.catch_warnings(record=True) as warned:
            bqstorage_client = client._ensure_bqstorage_client(mock_storage_client)

        self.assertIsNone(bqstorage_client)
        matching_warnings = [
            warning for warning in warned if "BQ Storage too old" in str(warning)
        ]
        assert matching_warnings, "Obsolete dependency warning not raised."

    def test_get_shared_bqstorage_client_creates_one_client(self):
        bigquery_storage = pytest.importorskip("google.cloud.bigquery_storage")
        from google.cloud.bigquery import client as client_module

        mock_client = mock.create_autospec(bigquery_storage.BigQueryReadClient)
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)

        with mock.patch(
            "google.cloud.bigquery_storage.BigQueryReadClient", mock_client
        ):
            first = client._get_shared_bqstorage_client()
            second = client._get_shared_bqstorage_client()

        self.assertIs(first, mock_client.return_value)
        self.assertIs(second, first)
        mock_client.assert_called_once_with(
            credentials=creds,
            client_options=None,
            client_info=mock.ANY,
            transport=client_module._create_bqstorage_transport,
        )

    @pytest.mark.skipif(
        packaging.version.parse(getattr(google.api_core, "__version__", "0.0.0"))
        < packaging.version.Version("2.15.0"),
        reason="universe_domain not supported with google-api-core < 2.15.0",
    )
    def test_get_shared_bqstorage_client_uses_universe_domain(self):
        bigquery_storage = pytest.importorskip("google.cloud.bigquery_storage")

        mock_client = mock.create_autospec(bigquery_storage.BigQueryReadClient)
        creds = _make_credentials()
        client = self._make_one(
            project=self.PROJECT,
            credentials=creds,
            client_options={"universe_domain": "foo.com"},
        )

        with mock.patch(
            "google.cloud.bigquery_storage.BigQueryReadClient", mock_client
        ):
            client._get_shared_bqstorage_client()

        _, kwargs = mock_client.call_args
        self.assertEqual(kwargs["client_options"].universe_domain, "foo.com")

    def test_get_shared_bqstorage_client_tries_again_if_unavailable(self):
        from google.cloud.bigquery import client as client_module

        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)

        with mock.patch.object(
            client, "_ensure_bqstorage_client", return_value=None
        ) as ensure:
            self.assertIsNone(client._get_shared_bqstorage_client())
            self.assertIsNone(client._get_shared_bqstorage_client())

        expected = mock.call(transport=client_module._create_bqstorage_transport)
        self.assertEqual(ensure.call_args_list, [expected, expected])

    def test_get_shared_bqstorage_client_creates_one_client_across_threads(self):
        import threading
        import time

        from google.cloud.bigquery import client as client_module

        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)

        def slow_create(**kwargs):
            time.sleep(0.05)
            return mock.Mock()

        results = []

        def get_client():
            results.append(client._get_shared_bqstorage_client())

        with mock.patch.object(
            client, "_ensure_bqstorage_client", side_effect=slow_create
        ) as ensure:
            threads = [threading.Thread(target=get_client) for _ in range(5)]
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join()

        ensure.assert_called_once_with(
            transport=client_module._create_bqstorage_transport
        )
        self.assertEqual(len(results), 5)
        self.assertTrue(all(result is results[0] for result in results))

    def test_get_shared_bqstorage_client_channel_sends_keepalive_pings(self):
        bigquery_storage = pytest.importorskip("google.cloud.bigquery_storage")
        import google.auth.credentials
        import grpc

        transport_class = bigquery_storage.BigQueryReadClient.get_transport_class(
            "grpc"
        )
        creds = google.auth.credentials.AnonymousCredentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        channel = grpc.insecure_channel("localhost:1")

        with mock.patch.object(
            transport_class, "create_channel", return_value=channel
        ) as create_channel:
            bqstorage_client = client._get_shared_bqstorage_client()
        channel.close()

        self.assertIsInstance(bqstorage_client._transport, transport_class)
        options = create_channel.call_args.kwargs["options"]
        self.assertIn(("grpc.keepalive_time_ms", 60000), options)
        self.assertIn(("grpc.keepalive_timeout_ms", 60000), options)
        # The transport's own options are kept.
        self.assertIn(("grpc.max_receive_message_length", -1), options)

    def test_create_routine_w_minimal_resource(self):
        from google.cloud.bigquery.routine import Routine, RoutineReference

        creds = _make_credentials()
        path = "/projects/test-routine-project/datasets/test_routines/routines"
        resource = {
            "routineReference": {
                "projectId": "test-routine-project",
                "datasetId": "test_routines",
                "routineId": "minimal_routine",
            }
        }
        client = self._make_one(project=self.PROJECT, credentials=creds)
        conn = client._connection = make_connection(resource)
        full_routine_id = "test-routine-project.test_routines.minimal_routine"
        routine = Routine(full_routine_id)
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            actual_routine = client.create_routine(routine, timeout=7.5)

        final_attributes.assert_called_once_with({"path": path}, client, None)

        conn.api_request.assert_called_once_with(
            method="POST",
            path=path,
            data=resource,
            timeout=7.5,
        )
        self.assertEqual(
            actual_routine.reference, RoutineReference.from_string(full_routine_id)
        )

    def test_create_routine_w_conflict(self):
        from google.cloud.bigquery.routine import Routine

        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        conn = client._connection = make_connection(
            google.api_core.exceptions.AlreadyExists("routine already exists")
        )
        path = "/projects/test-routine-project/datasets/test_routines/routines"
        full_routine_id = "test-routine-project.test_routines.minimal_routine"
        routine = Routine(full_routine_id)

        with pytest.raises(google.api_core.exceptions.AlreadyExists):
            with mock.patch(
                "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
            ) as final_attributes:
                client.create_routine(routine)

        final_attributes.assert_called_once_with({"path": path}, client, None)

        resource = {
            "routineReference": {
                "projectId": "test-routine-project",
                "datasetId": "test_routines",
                "routineId": "minimal_routine",
            }
        }
        conn.api_request.assert_called_once_with(
            method="POST",
            path=path,
            data=resource,
            timeout=DEFAULT_TIMEOUT,
        )

    def test_span_status_is_set(self):
        pytest.importorskip("opentelemetry.sdk")
        from google.cloud.bigquery.routine import Routine

        tracer_provider = TracerProvider()
        memory_exporter = InMemorySpanExporter()
        span_processor = SimpleSpanProcessor(memory_exporter)
        tracer_provider.add_span_processor(span_processor)

        # OpenTelemetry API >= 0.12b0 does not allow overriding the tracer once
        # initialized, thus directly override the internal global var.
        tracer_patcher = mock.patch.object(trace, "_TRACER_PROVIDER", tracer_provider)

        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        conn = client._connection = make_connection(
            google.api_core.exceptions.AlreadyExists("routine already exists")
        )
        path = "/projects/test-routine-project/datasets/test_routines/routines"
        full_routine_id = "test-routine-project.test_routines.minimal_routine"
        routine = Routine(full_routine_id)

        with pytest.raises(google.api_core.exceptions.AlreadyExists), tracer_patcher:
            client.create_routine(routine)

        span_list = memory_exporter.get_finished_spans()
        self.assertTrue(span_list[0].status is not None)

        resource = {
            "routineReference": {
                "projectId": "test-routine-project",
                "datasetId": "test_routines",
                "routineId": "minimal_routine",
            }
        }
        conn.api_request.assert_called_once_with(
            method="POST",
            path=path,
            data=resource,
            timeout=DEFAULT_TIMEOUT,
        )

    def test_create_routine_w_conflict_exists_ok(self):
        from google.cloud.bigquery.routine import Routine

        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        resource = {
            "routineReference": {
                "projectId": "test-routine-project",
                "datasetId": "test_routines",
                "routineId": "minimal_routine",
            }
        }
        path = "/projects/test-routine-project/datasets/test_routines/routines"

        conn = client._connection = make_connection(
            google.api_core.exceptions.AlreadyExists("routine already exists"), resource
        )
        full_routine_id = "test-routine-project.test_routines.minimal_routine"
        routine = Routine(full_routine_id)
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            actual_routine = client.create_routine(routine, exists_ok=True)

        final_attributes.assert_called_with(
            {"path": "%s/minimal_routine" % path}, client, None
        )

        self.assertEqual(actual_routine.project, "test-routine-project")
        self.assertEqual(actual_routine.dataset_id, "test_routines")
        self.assertEqual(actual_routine.routine_id, "minimal_routine")
        conn.api_request.assert_has_calls(
            [
                mock.call(
                    method="POST",
                    path=path,
                    data=resource,
                    timeout=DEFAULT_TIMEOUT,
                ),
                mock.call(
                    method="GET",
                    path="/projects/test-routine-project/datasets/test_routines/routines/minimal_routine",
                    timeout=DEFAULT_TIMEOUT,
                ),
            ]
        )

    def test_create_table_w_day_partition(self):
        from google.cloud.bigquery.table import Table, TimePartitioning

        path = "projects/%s/datasets/%s/tables" % (self.PROJECT, self.DS_ID)
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        resource = self._make_table_resource()
        conn = client._connection = make_connection(resource)
        table = Table(self.TABLE_REF)
        table.time_partitioning = TimePartitioning()
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            got = client.create_table(table, timeout=7.5)

        final_attributes.assert_called_once_with(
            {"path": "/%s" % path, "dataset_id": table.dataset_id}, client, None
        )

        conn.api_request.assert_called_once_with(
            method="POST",
            path="/%s" % path,
            data={
                "tableReference": {
                    "projectId": self.PROJECT,
                    "datasetId": self.DS_ID,
                    "tableId": self.TABLE_ID,
                },
                "timePartitioning": {"type": "DAY"},
                "labels": {},
            },
            timeout=7.5,
        )
        self.assertEqual(table.time_partitioning.type_, "DAY")
        self.assertEqual(got.table_id, self.TABLE_ID)

    def test_create_table_w_custom_property(self):
        # The library should handle sending properties to the API that are not
        # yet part of the library
        from google.cloud.bigquery.table import Table

        path = "projects/%s/datasets/%s/tables" % (self.PROJECT, self.DS_ID)
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        resource = self._make_table_resource()
        resource["newAlphaProperty"] = "unreleased property"
        conn = client._connection = make_connection(resource)
        table = Table(self.TABLE_REF)
        table._properties["newAlphaProperty"] = "unreleased property"
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            got = client.create_table(table)

        final_attributes.assert_called_once_with(
            {"path": "/%s" % path, "dataset_id": table.dataset_id}, client, None
        )

        conn.api_request.assert_called_once_with(
            method="POST",
            path="/%s" % path,
            data={
                "tableReference": {
                    "projectId": self.PROJECT,
                    "datasetId": self.DS_ID,
                    "tableId": self.TABLE_ID,
                },
                "newAlphaProperty": "unreleased property",
                "labels": {},
            },
            timeout=DEFAULT_TIMEOUT,
        )
        self.assertEqual(got._properties["newAlphaProperty"], "unreleased property")
        self.assertEqual(got.table_id, self.TABLE_ID)

    def test_create_table_w_encryption_configuration(self):
        from google.cloud.bigquery.encryption_configuration import (
            EncryptionConfiguration,
        )
        from google.cloud.bigquery.table import Table

        path = "projects/%s/datasets/%s/tables" % (self.PROJECT, self.DS_ID)
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        resource = self._make_table_resource()
        conn = client._connection = make_connection(resource)
        table = Table(self.TABLE_REF)
        table.encryption_configuration = EncryptionConfiguration(
            kms_key_name=self.KMS_KEY_NAME
        )
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            got = client.create_table(table)

        final_attributes.assert_called_once_with(
            {"path": "/%s" % path, "dataset_id": table.dataset_id}, client, None
        )

        conn.api_request.assert_called_once_with(
            method="POST",
            path="/%s" % path,
            data={
                "tableReference": {
                    "projectId": self.PROJECT,
                    "datasetId": self.DS_ID,
                    "tableId": self.TABLE_ID,
                },
                "labels": {},
                "encryptionConfiguration": {"kmsKeyName": self.KMS_KEY_NAME},
            },
            timeout=DEFAULT_TIMEOUT,
        )
        self.assertEqual(got.table_id, self.TABLE_ID)

    def test_create_table_w_day_partition_and_expire(self):
        from google.cloud.bigquery.table import Table, TimePartitioning

        path = "projects/%s/datasets/%s/tables" % (self.PROJECT, self.DS_ID)
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        resource = self._make_table_resource()
        conn = client._connection = make_connection(resource)
        table = Table(self.TABLE_REF)
        table.time_partitioning = TimePartitioning(expiration_ms=100)
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            got = client.create_table(table)

        final_attributes.assert_called_once_with(
            {"path": "/%s" % path, "dataset_id": table.dataset_id}, client, None
        )

        conn.api_request.assert_called_once_with(
            method="POST",
            path="/%s" % path,
            data={
                "tableReference": {
                    "projectId": self.PROJECT,
                    "datasetId": self.DS_ID,
                    "tableId": self.TABLE_ID,
                },
                "timePartitioning": {"type": "DAY", "expirationMs": "100"},
                "labels": {},
            },
            timeout=DEFAULT_TIMEOUT,
        )
        self.assertEqual(table.time_partitioning.type_, "DAY")
        self.assertEqual(table.time_partitioning.expiration_ms, 100)
        self.assertEqual(got.table_id, self.TABLE_ID)

    def test_create_table_w_schema_and_query(self):
        from google.cloud.bigquery.schema import SchemaField
        from google.cloud.bigquery.table import Table

        path = "projects/%s/datasets/%s/tables" % (self.PROJECT, self.DS_ID)
        query = "SELECT * from %s:%s" % (self.DS_ID, self.TABLE_ID)
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        resource = self._make_table_resource()
        resource.update(
            {
                "schema": {
                    "fields": [
                        {"name": "full_name", "type": "STRING", "mode": "REQUIRED"},
                        {"name": "age", "type": "INTEGER", "mode": "REQUIRED"},
                    ]
                },
                "view": {"query": query},
            }
        )
        schema = [
            SchemaField("full_name", "STRING", mode="REQUIRED"),
            SchemaField("age", "INTEGER", mode="REQUIRED"),
        ]
        conn = client._connection = make_connection(resource)
        table = Table(self.TABLE_REF, schema=schema)
        table.view_query = query

        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            got = client.create_table(table)

        final_attributes.assert_called_once_with(
            {"path": "/%s" % path, "dataset_id": table.dataset_id}, client, None
        )

        conn.api_request.assert_called_once_with(
            method="POST",
            path="/%s" % path,
            data={
                "tableReference": {
                    "projectId": self.PROJECT,
                    "datasetId": self.DS_ID,
                    "tableId": self.TABLE_ID,
                },
                "schema": {
                    "fields": [
                        {"name": "full_name", "type": "STRING", "mode": "REQUIRED"},
                        {"name": "age", "type": "INTEGER", "mode": "REQUIRED"},
                    ]
                },
                "view": {"query": query, "useLegacySql": False},
                "labels": {},
            },
            timeout=DEFAULT_TIMEOUT,
        )
        self.assertEqual(got.table_id, self.TABLE_ID)
        self.assertEqual(got.project, self.PROJECT)
        self.assertEqual(got.dataset_id, self.DS_ID)
        self.assertEqual(got.schema, schema)
        self.assertEqual(got.view_query, query)

    def test_create_table_w_external(self):
        from google.cloud.bigquery.external_config import ExternalConfig
        from google.cloud.bigquery.job import SourceFormat
        from google.cloud.bigquery.table import Table

        path = "projects/%s/datasets/%s/tables" % (self.PROJECT, self.DS_ID)
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        resource = self._make_table_resource()
        resource.update(
            {
                "externalDataConfiguration": {
                    "sourceFormat": SourceFormat.CSV,
                    "autodetect": True,
                }
            }
        )
        conn = client._connection = make_connection(resource)
        table = Table(self.TABLE_REF)
        ec = ExternalConfig("CSV")
        ec.autodetect = True
        table.external_data_configuration = ec

        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            got = client.create_table(table)

        final_attributes.assert_called_once_with(
            {"path": "/%s" % path, "dataset_id": table.dataset_id}, client, None
        )

        conn.api_request.assert_called_once_with(
            method="POST",
            path="/%s" % path,
            data={
                "tableReference": {
                    "projectId": self.PROJECT,
                    "datasetId": self.DS_ID,
                    "tableId": self.TABLE_ID,
                },
                "externalDataConfiguration": {
                    "sourceFormat": SourceFormat.CSV,
                    "autodetect": True,
                },
                "labels": {},
            },
            timeout=DEFAULT_TIMEOUT,
        )
        self.assertEqual(got.table_id, self.TABLE_ID)
        self.assertEqual(got.project, self.PROJECT)
        self.assertEqual(got.dataset_id, self.DS_ID)
        self.assertEqual(
            got.external_data_configuration.source_format, SourceFormat.CSV
        )
        self.assertEqual(got.external_data_configuration.autodetect, True)

    def test_create_table_w_reference(self):
        path = "projects/%s/datasets/%s/tables" % (self.PROJECT, self.DS_ID)
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        resource = self._make_table_resource()
        conn = client._connection = make_connection(resource)

        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            got = client.create_table(self.TABLE_REF)

        final_attributes.assert_called_once_with(
            {"path": "/%s" % path, "dataset_id": self.TABLE_REF.dataset_id},
            client,
            None,
        )

        conn.api_request.assert_called_once_with(
            method="POST",
            path="/%s" % path,
            data={
                "tableReference": {
                    "projectId": self.PROJECT,
                    "datasetId": self.DS_ID,
                    "tableId": self.TABLE_ID,
                },
                "labels": {},
            },
            timeout=DEFAULT_TIMEOUT,
        )
        self.assertEqual(got.table_id, self.TABLE_ID)

    def test_create_table_w_fully_qualified_string(self):
        path = "projects/%s/datasets/%s/tables" % (self.PROJECT, self.DS_ID)
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        resource = self._make_table_resource()
        conn = client._connection = make_connection(resource)
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            got = client.create_table(
                "{}.{}.{}".format(self.PROJECT, self.DS_ID, self.TABLE_ID)
            )

        final_attributes.assert_called_once_with(
            {"path": "/%s" % path, "dataset_id": self.TABLE_REF.dataset_id},
            client,
            None,
        )

        conn.api_request.assert_called_once_with(
            method="POST",
            path="/%s" % path,
            data={
                "tableReference": {
                    "projectId": self.PROJECT,
                    "datasetId": self.DS_ID,
                    "tableId": self.TABLE_ID,
                },
                "labels": {},
            },
            timeout=DEFAULT_TIMEOUT,
        )
        self.assertEqual(got.table_id, self.TABLE_ID)

    def test_create_table_w_string(self):
        path = "projects/%s/datasets/%s/tables" % (self.PROJECT, self.DS_ID)
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        resource = self._make_table_resource()
        conn = client._connection = make_connection(resource)
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            got = client.create_table("{}.{}".format(self.DS_ID, self.TABLE_ID))

        final_attributes.assert_called_once_with(
            {"path": "/%s" % path, "dataset_id": self.TABLE_REF.dataset_id},
            client,
            None,
        )

        conn.api_request.assert_called_once_with(
            method="POST",
            path="/%s" % path,
            data={
                "tableReference": {
                    "projectId": self.PROJECT,
                    "datasetId": self.DS_ID,
                    "tableId": self.TABLE_ID,
                },
                "labels": {},
            },
            timeout=DEFAULT_TIMEOUT,
        )
        self.assertEqual(got.table_id, self.TABLE_ID)

    def test_create_table_alreadyexists_w_exists_ok_false(self):
        post_path = "/projects/{}/datasets/{}/tables".format(self.PROJECT, self.DS_ID)
        creds = _make_credentials()
        client = self._make_one(
            project=self.PROJECT, credentials=creds, location=self.LOCATION
        )
        conn = client._connection = make_connection(
            google.api_core.exceptions.AlreadyExists("table already exists")
        )

        with pytest.raises(google.api_core.exceptions.AlreadyExists):
            with mock.patch(
                "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
            ) as final_attributes:
                client.create_table("{}.{}".format(self.DS_ID, self.TABLE_ID))

        final_attributes.assert_called_with(
            {"path": post_path, "dataset_id": self.TABLE_REF.dataset_id},
            client,
            None,
        )

        conn.api_request.assert_called_once_with(
            method="POST",
            path=post_path,
            data={
                "tableReference": {
                    "projectId": self.PROJECT,
                    "datasetId": self.DS_ID,
                    "tableId": self.TABLE_ID,
                },
                "labels": {},
            },
            timeout=DEFAULT_TIMEOUT,
        )

    def test_create_table_alreadyexists_w_exists_ok_true(self):
        post_path = "/projects/{}/datasets/{}/tables".format(self.PROJECT, self.DS_ID)
        get_path = "/projects/{}/datasets/{}/tables/{}".format(
            self.PROJECT, self.DS_ID, self.TABLE_ID
        )
        resource = self._make_table_resource()
        creds = _make_credentials()
        client = self._make_one(
            project=self.PROJECT, credentials=creds, location=self.LOCATION
        )
        conn = client._connection = make_connection(
            google.api_core.exceptions.AlreadyExists("table already exists"), resource
        )

        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            got = client.create_table(
                "{}.{}".format(self.DS_ID, self.TABLE_ID), exists_ok=True
            )

        final_attributes.assert_called_with({"path": get_path}, client, None)

        self.assertEqual(got.project, self.PROJECT)
        self.assertEqual(got.dataset_id, self.DS_ID)
        self.assertEqual(got.table_id, self.TABLE_ID)

        conn.api_request.assert_has_calls(
            [
                mock.call(
                    method="POST",
                    path=post_path,
                    data={
                        "tableReference": {
                            "projectId": self.PROJECT,
                            "datasetId": self.DS_ID,
                            "tableId": self.TABLE_ID,
                        },
                        "labels": {},
                    },
                    timeout=DEFAULT_TIMEOUT,
                ),
                mock.call(method="GET", path=get_path, timeout=DEFAULT_TIMEOUT),
            ]
        )

    def test_close(self):
        creds = _make_credentials()
        http = mock.Mock()
        http._auth_request.session = mock.Mock()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)

        client.close()

        http.close.assert_called_once()
        http._auth_request.session.close.assert_called_once()

    def test_close_closes_shared_bqstorage_client(self):
        creds = _make_credentials()
        http = mock.Mock()
        http._auth_request.session = mock.Mock()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        first, second = mock.Mock(), mock.Mock()

        with mock.patch.object(
            client, "_ensure_bqstorage_client", side_effect=[first, second]
        ):
            self.assertIs(client._get_shared_bqstorage_client(), first)
            client.close()
            self.assertIs(client._get_shared_bqstorage_client(), second)

        first._transport.close.assert_called_once_with()
        second._transport.close.assert_not_called()

    def test_get_model(self):
        path = "projects/%s/datasets/%s/models/%s" % (
            self.PROJECT,
            self.DS_ID,
            self.MODEL_ID,
        )
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        resource = {
            "modelReference": {
                "projectId": self.PROJECT,
                "datasetId": self.DS_ID,
                "modelId": self.MODEL_ID,
            }
        }
        conn = client._connection = make_connection(resource)

        model_ref = DatasetReference(self.PROJECT, self.DS_ID).model(self.MODEL_ID)
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            got = client.get_model(model_ref, timeout=7.5)

        final_attributes.assert_called_once_with({"path": "/%s" % path}, client, None)

        conn.api_request.assert_called_once_with(
            method="GET", path="/%s" % path, timeout=7.5
        )
        self.assertEqual(got.model_id, self.MODEL_ID)

    def test_get_model_w_string(self):
        path = "projects/%s/datasets/%s/models/%s" % (
            self.PROJECT,
            self.DS_ID,
            self.MODEL_ID,
        )
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        resource = {
            "modelReference": {
                "projectId": self.PROJECT,
                "datasetId": self.DS_ID,
                "modelId": self.MODEL_ID,
            }
        }
        conn = client._connection = make_connection(resource)

        model_id = "{}.{}.{}".format(self.PROJECT, self.DS_ID, self.MODEL_ID)
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            got = client.get_model(model_id)

        final_attributes.assert_called_once_with({"path": "/%s" % path}, client, None)

        conn.api_request.assert_called_once_with(
            method="GET", path="/%s" % path, timeout=DEFAULT_TIMEOUT
        )
        self.assertEqual(got.model_id, self.MODEL_ID)

    def test_get_routine(self):
        from google.cloud.bigquery.routine import Routine, RoutineReference

        full_routine_id = "test-routine-project.test_routines.minimal_routine"
        routines = [
            full_routine_id,
            Routine(full_routine_id),
            RoutineReference.from_string(full_routine_id),
        ]
        for routine in routines:
            creds = _make_credentials()
            resource = {
                "etag": "im-an-etag",
                "routineReference": {
                    "projectId": "test-routine-project",
                    "datasetId": "test_routines",
                    "routineId": "minimal_routine",
                },
                "routineType": "SCALAR_FUNCTION",
            }
            path = "/projects/test-routine-project/datasets/test_routines/routines/minimal_routine"

            client = self._make_one(project=self.PROJECT, credentials=creds)
            conn = client._connection = make_connection(resource)

            with mock.patch(
                "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
            ) as final_attributes:
                actual_routine = client.get_routine(routine, timeout=7.5)

            final_attributes.assert_called_once_with({"path": path}, client, None)

            conn.api_request.assert_called_once_with(
                method="GET",
                path=path,
                timeout=7.5,
            )
            self.assertEqual(
                actual_routine.reference,
                RoutineReference.from_string(full_routine_id),
                msg="routine={}".format(repr(routine)),
            )
            self.assertEqual(
                actual_routine.etag,
                "im-an-etag",
                msg="routine={}".format(repr(routine)),
            )
            self.assertEqual(
                actual_routine.type_,
                "SCALAR_FUNCTION",
                msg="routine={}".format(repr(routine)),
            )

    def test_get_table(self):
        path = "projects/%s/datasets/%s/tables/%s" % (
            self.PROJECT,
            self.DS_ID,
            self.TABLE_ID,
        )
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        resource = self._make_table_resource()
        conn = client._connection = make_connection(resource)
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            table = client.get_table(self.TABLE_REF, timeout=7.5)

        final_attributes.assert_called_once_with({"path": "/%s" % path}, client, None)

        conn.api_request.assert_called_once_with(
            method="GET", path="/%s" % path, timeout=7.5
        )
        self.assertEqual(table.table_id, self.TABLE_ID)

    def test_get_table_sets_user_agent(self):
        creds = _make_credentials()
        http = mock.create_autospec(requests.Session)
        mock_response = http.request(
            url=mock.ANY, method=mock.ANY, headers=mock.ANY, data=mock.ANY
        )
        http.reset_mock()
        http.is_mtls = False
        mock_response.status_code = 200
        mock_response.json.return_value = self._make_table_resource()
        user_agent_override = client_info.ClientInfo(user_agent="my-application/1.2.3")
        client = self._make_one(
            project=self.PROJECT,
            credentials=creds,
            client_info=user_agent_override,
            _http=http,
        )

        client.get_table(self.TABLE_REF)

        expected_user_agent = user_agent_override.to_user_agent()
        http.request.assert_called_once_with(
            url=mock.ANY,
            method="GET",
            headers=mock.ANY,
            data=mock.ANY,
            timeout=DEFAULT_TIMEOUT,
        )
        _, kwargs = http.request.call_args
        actual_headers = {k.lower(): v for k, v in kwargs["headers"].items()}
        self.assertEqual(
            actual_headers,
            {
                "x-goog-api-client": expected_user_agent,
                "accept-encoding": "gzip",
                "user-agent": expected_user_agent,
            },
        )
        self.assertIn("my-application/1.2.3", expected_user_agent)

    def test_get_iam_policy(self):
        from google.api_core.iam import Policy
        from google.cloud.bigquery.iam import (
            BIGQUERY_DATA_EDITOR_ROLE,
            BIGQUERY_DATA_OWNER_ROLE,
            BIGQUERY_DATA_VIEWER_ROLE,
        )

        PATH = "/projects/{}/datasets/{}/tables/{}:getIamPolicy".format(
            self.PROJECT,
            self.DS_ID,
            self.TABLE_ID,
        )
        BODY = {"options": {"requestedPolicyVersion": 1}}
        ETAG = "CARDI"
        VERSION = 1
        OWNER1 = "user:phred@example.com"
        OWNER2 = "group:cloud-logs@google.com"
        EDITOR1 = "domain:google.com"
        EDITOR2 = "user:phred@example.com"
        VIEWER1 = "serviceAccount:1234-abcdef@service.example.com"
        VIEWER2 = "user:phred@example.com"
        RETURNED = {
            "resourceId": PATH,
            "etag": ETAG,
            "version": VERSION,
            "bindings": [
                {"role": BIGQUERY_DATA_OWNER_ROLE, "members": [OWNER1, OWNER2]},
                {"role": BIGQUERY_DATA_EDITOR_ROLE, "members": [EDITOR1, EDITOR2]},
                {"role": BIGQUERY_DATA_VIEWER_ROLE, "members": [VIEWER1, VIEWER2]},
            ],
        }
        EXPECTED = {
            binding["role"]: set(binding["members"]) for binding in RETURNED["bindings"]
        }

        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(RETURNED)
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            policy = client.get_iam_policy(self.TABLE_REF, timeout=7.5)

        final_attributes.assert_called_once_with({"path": PATH}, client, None)

        conn.api_request.assert_called_once_with(
            method="POST", path=PATH, data=BODY, timeout=7.5
        )

        self.assertIsInstance(policy, Policy)
        self.assertEqual(policy.etag, RETURNED["etag"])
        self.assertEqual(policy.version, RETURNED["version"])
        self.assertEqual(dict(policy), EXPECTED)

    def test_get_iam_policy_w_invalid_table(self):
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)

        table_resource_string = "projects/{}/datasets/{}/tables/{}".format(
            self.PROJECT,
            self.DS_ID,
            self.TABLE_ID,
        )

        with self.assertRaises(ValueError):
            client.get_iam_policy(table_resource_string)

    def test_get_iam_policy_w_invalid_version(self):
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)

        with self.assertRaises(ValueError):
            client.get_iam_policy(self.TABLE_REF, requested_policy_version=2)

    def test_set_iam_policy(self):
        from google.api_core.iam import Policy
        from google.cloud.bigquery.iam import (
            BIGQUERY_DATA_EDITOR_ROLE,
            BIGQUERY_DATA_OWNER_ROLE,
            BIGQUERY_DATA_VIEWER_ROLE,
        )

        PATH = "/projects/%s/datasets/%s/tables/%s:setIamPolicy" % (
            self.PROJECT,
            self.DS_ID,
            self.TABLE_ID,
        )
        ETAG = "foo"
        VERSION = 1
        OWNER1 = "user:phred@example.com"
        OWNER2 = "group:cloud-logs@google.com"
        EDITOR1 = "domain:google.com"
        EDITOR2 = "user:phred@example.com"
        VIEWER1 = "serviceAccount:1234-abcdef@service.example.com"
        VIEWER2 = "user:phred@example.com"
        BINDINGS = [
            {"role": BIGQUERY_DATA_OWNER_ROLE, "members": [OWNER1, OWNER2]},
            {"role": BIGQUERY_DATA_EDITOR_ROLE, "members": [EDITOR1, EDITOR2]},
            {"role": BIGQUERY_DATA_VIEWER_ROLE, "members": [VIEWER1, VIEWER2]},
        ]
        FIELDS = ("bindings", "etag")
        RETURNED = {"etag": ETAG, "version": VERSION, "bindings": BINDINGS}

        policy = Policy()
        for binding in BINDINGS:
            policy[binding["role"]] = binding["members"]

        BODY = {"policy": policy.to_api_repr(), "updateMask": "bindings,etag"}

        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(RETURNED)

        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            returned_policy = client.set_iam_policy(
                self.TABLE_REF, policy, fields=FIELDS, timeout=7.5
            )

        final_attributes.assert_called_once_with({"path": PATH}, client, None)

        conn.api_request.assert_called_once_with(
            method="POST", path=PATH, data=BODY, timeout=7.5
        )
        self.assertEqual(returned_policy.etag, ETAG)
        self.assertEqual(returned_policy.version, VERSION)
        self.assertEqual(dict(returned_policy), dict(policy))

    def test_set_iam_policy_updateMask(self):
        from google.api_core.iam import Policy
        from google.cloud.bigquery.iam import (
            BIGQUERY_DATA_EDITOR_ROLE,
            BIGQUERY_DATA_OWNER_ROLE,
            BIGQUERY_DATA_VIEWER_ROLE,
        )

        PATH = "/projects/%s/datasets/%s/tables/%s:setIamPolicy" % (
            self.PROJECT,
            self.DS_ID,
            self.TABLE_ID,
        )
        ETAG = "foo"
        VERSION = 1
        OWNER1 = "user:phred@example.com"
        OWNER2 = "group:cloud-logs@google.com"
        EDITOR1 = "domain:google.com"
        EDITOR2 = "user:phred@example.com"
        VIEWER1 = "serviceAccount:1234-abcdef@service.example.com"
        VIEWER2 = "user:phred@example.com"
        BINDINGS = [
            {"role": BIGQUERY_DATA_OWNER_ROLE, "members": [OWNER1, OWNER2]},
            {"role": BIGQUERY_DATA_EDITOR_ROLE, "members": [EDITOR1, EDITOR2]},
            {"role": BIGQUERY_DATA_VIEWER_ROLE, "members": [VIEWER1, VIEWER2]},
        ]
        MASK = "bindings,etag"
        RETURNED = {"etag": ETAG, "version": VERSION, "bindings": BINDINGS}

        policy = Policy()
        for binding in BINDINGS:
            policy[binding["role"]] = binding["members"]

        BODY = {"policy": policy.to_api_repr(), "updateMask": MASK}

        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(RETURNED)

        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            returned_policy = client.set_iam_policy(
                self.TABLE_REF, policy, updateMask=MASK, timeout=7.5
            )

        final_attributes.assert_called_once_with({"path": PATH}, client, None)

        conn.api_request.assert_called_once_with(
            method="POST", path=PATH, data=BODY, timeout=7.5
        )
        self.assertEqual(returned_policy.etag, ETAG)
        self.assertEqual(returned_policy.version, VERSION)
        self.assertEqual(dict(returned_policy), dict(policy))

    def test_set_iam_policy_no_mask(self):
        from google.api_core.iam import Policy

        PATH = "/projects/%s/datasets/%s/tables/%s:setIamPolicy" % (
            self.PROJECT,
            self.DS_ID,
            self.TABLE_ID,
        )
        RETURNED = {"etag": "foo", "version": 1, "bindings": []}

        policy = Policy()
        BODY = {"policy": policy.to_api_repr()}

        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(RETURNED)
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            client.set_iam_policy(self.TABLE_REF, policy, timeout=7.5)

        final_attributes.assert_called_once_with({"path": PATH}, client, None)

        conn.api_request.assert_called_once_with(
            method="POST", path=PATH, data=BODY, timeout=7.5
        )

    def test_set_ia_policy_updateMask_and_fields(self):
        from google.api_core.iam import Policy

        policy = Policy()
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)

        with pytest.raises(ValueError, match="updateMask"):
            client.set_iam_policy(
                self.TABLE_REF, policy, updateMask="bindings", fields=("bindings",)
            )

    def test_set_iam_policy_invalid_policy(self):
        from google.api_core.iam import Policy

        policy = Policy()
        invalid_policy_repr = policy.to_api_repr()

        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)

        with self.assertRaises(TypeError):
            client.set_iam_policy(self.TABLE_REF, invalid_policy_repr)

    def test_set_iam_policy_w_invalid_table(self):
        from google.api_core.iam import Policy

        policy = Policy()

        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)

        table_resource_string = "projects/%s/datasets/%s/tables/%s" % (
            self.PROJECT,
            self.DS_ID,
            self.TABLE_ID,
        )

        with self.assertRaises(ValueError):
            client.set_iam_policy(table_resource_string, policy)

    def test_test_iam_permissions(self):
        PATH = "/projects/%s/datasets/%s/tables/%s:testIamPermissions" % (
            self.PROJECT,
            self.DS_ID,
            self.TABLE_ID,
        )

        PERMISSIONS = ["bigquery.tables.get", "bigquery.tables.update"]
        BODY = {"permissions": PERMISSIONS}
        RETURNED = {"permissions": PERMISSIONS}

        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(RETURNED)
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            client.test_iam_permissions(self.TABLE_REF, PERMISSIONS, timeout=7.5)

        final_attributes.assert_called_once_with({"path": PATH}, client, None)

        conn.api_request.assert_called_once_with(
            method="POST", path=PATH, data=BODY, timeout=7.5
        )

    def test_test_iam_permissions_w_invalid_table(self):
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)

        table_resource_string = "projects/%s/datasets/%s/tables/%s" % (
            self.PROJECT,
            self.DS_ID,
            self.TABLE_ID,
        )

        PERMISSIONS = ["bigquery.tables.get", "bigquery.tables.update"]

        with self.assertRaises(ValueError):
            client.test_iam_permissions(table_resource_string, PERMISSIONS)

    def test_update_dataset_w_invalid_field(self):
        from google.cloud.bigquery.dataset import Dataset

        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        with self.assertRaises(ValueError):
            client.update_dataset(
                Dataset("{}.{}".format(self.PROJECT, self.DS_ID)), ["foo"]
            )

    def test_update_dataset(self):
        from google.cloud.bigquery.dataset import AccessEntry, Dataset

        PATH = "projects/%s/datasets/%s" % (self.PROJECT, self.DS_ID)
        DESCRIPTION = "DESCRIPTION"
        FRIENDLY_NAME = "TITLE"
        LOCATION = "loc"
        LABELS = {"priority": "high"}
        ACCESS = [{"role": "OWNER", "userByEmail": "phred@example.com"}]
        EXP = 17
        RESOURCE_TAGS = {"123456789012/key": "value"}
        RESOURCE = {
            "datasetReference": {"projectId": self.PROJECT, "datasetId": self.DS_ID},
            "etag": "etag",
            "description": DESCRIPTION,
            "friendlyName": FRIENDLY_NAME,
            "location": LOCATION,
            "defaultTableExpirationMs": EXP,
            "labels": LABELS,
            "access": ACCESS,
            "resourceTags": RESOURCE_TAGS,
        }
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        conn = client._connection = make_connection(RESOURCE, RESOURCE)
        ds = Dataset(DatasetReference(self.PROJECT, self.DS_ID))
        ds.description = DESCRIPTION
        ds.friendly_name = FRIENDLY_NAME
        ds.location = LOCATION
        ds.default_table_expiration_ms = EXP
        ds.labels = LABELS
        ds.access_entries = [AccessEntry("OWNER", "userByEmail", "phred@example.com")]
        ds.resource_tags = RESOURCE_TAGS
        filter_fields = [
            "description",
            "friendly_name",
            "location",
            "labels",
            "access_entries",
            "resource_tags",
        ]

        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            ds2 = client.update_dataset(
                ds,
                fields=filter_fields,
                timeout=7.5,
            )

        final_attributes.assert_called_once_with(
            {"path": "/%s" % PATH, "fields": filter_fields}, client, None
        )

        conn.api_request.assert_called_once_with(
            method="PATCH",
            data={
                "description": DESCRIPTION,
                "friendlyName": FRIENDLY_NAME,
                "location": LOCATION,
                "labels": LABELS,
                "access": ACCESS,
                "resourceTags": RESOURCE_TAGS,
            },
            path="/" + PATH,
            timeout=7.5,
            query_params={},
        )
        self.assertEqual(ds2.description, ds.description)
        self.assertEqual(ds2.friendly_name, ds.friendly_name)
        self.assertEqual(ds2.location, ds.location)
        self.assertEqual(ds2.labels, ds.labels)
        self.assertEqual(ds2.access_entries, ds.access_entries)
        self.assertEqual(ds2.resource_tags, ds.resource_tags)

        # ETag becomes If-Match header.
        ds._properties["etag"] = "etag"
        client.update_dataset(ds, [])
        req = conn.api_request.call_args
        self.assertEqual(req[1]["headers"]["If-Match"], "etag")
        self.assertEqual(req[1].get("query_params"), {})

    def test_update_dataset_w_update_mode(self):
        PATH = f"projects/{self.PROJECT}/datasets/{self.DS_ID}"
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)

        DESCRIPTION = "DESCRIPTION"
        RESOURCE = {
            "datasetReference": {"projectId": self.PROJECT, "datasetId": self.DS_ID},
            "etag": "etag",
            "description": DESCRIPTION,
        }
        dataset_ref = DatasetReference(self.PROJECT, self.DS_ID)
        orig_dataset = Dataset(dataset_ref)
        orig_dataset.description = DESCRIPTION
        filter_fields = ["description"]

        test_cases = [
            (None, None),
            (UpdateMode.UPDATE_MODE_UNSPECIFIED, "UPDATE_MODE_UNSPECIFIED"),
            (UpdateMode.UPDATE_METADATA, "UPDATE_METADATA"),
            (UpdateMode.UPDATE_ACL, "UPDATE_ACL"),
            (UpdateMode.UPDATE_FULL, "UPDATE_FULL"),
        ]

        for update_mode_arg, expected_param_value in test_cases:
            with self.subTest(
                update_mode_arg=str(update_mode_arg),
                expected_param_value=expected_param_value,
            ):
                conn = client._connection = make_connection(RESOURCE, RESOURCE)

                new_dataset = client.update_dataset(
                    orig_dataset,
                    fields=filter_fields,
                    update_mode=update_mode_arg,
                )
                self.assertEqual(orig_dataset.description, new_dataset.description)

                if expected_param_value:
                    expected_query_params = {"updateMode": expected_param_value}
                else:
                    expected_query_params = {}

                conn.api_request.assert_called_once_with(
                    method="PATCH",
                    path="/" + PATH,
                    data={"description": DESCRIPTION},
                    timeout=DEFAULT_TIMEOUT,
                    query_params=expected_query_params if expected_query_params else {},
                )

    def test_update_dataset_w_invalid_update_mode(self):
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)

        DESCRIPTION = "DESCRIPTION"
        resource = {
            "datasetReference": {"projectId": self.PROJECT, "datasetId": self.DS_ID},
            "etag": "etag",
        }

        dataset_ref = DatasetReference(self.PROJECT, self.DS_ID)
        orig_dataset = Dataset(dataset_ref)
        orig_dataset.description = DESCRIPTION
        filter_fields = ["description"]  # A non-empty list of fields is required

        # Mock the connection to prevent actual API calls
        # and to provide a minimal valid response if the call were to proceed.
        conn = client._connection = make_connection(resource)

        test_cases = [
            "INVALID_STRING",
            123,
            123.45,
            object(),
        ]

        for invalid_update_mode in test_cases:
            with self.subTest(invalid_update_mode=str(invalid_update_mode)):
                conn.api_request.reset_mock()  # Reset mock for each sub-test
                with self.assertRaises(AttributeError):
                    client.update_dataset(
                        orig_dataset,
                        fields=filter_fields,
                        update_mode=invalid_update_mode,
                    )

    def test_update_dataset_w_custom_property(self):
        # The library should handle sending properties to the API that are not
        # yet part of the library
        from google.cloud.bigquery.dataset import Dataset

        path = "/projects/%s/datasets/%s" % (self.PROJECT, self.DS_ID)
        resource = {
            "datasetReference": {"projectId": self.PROJECT, "datasetId": self.DS_ID},
            "newAlphaProperty": "unreleased property",
        }
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        conn = client._connection = make_connection(resource)
        dataset = Dataset(DatasetReference(self.PROJECT, self.DS_ID))
        dataset._properties["newAlphaProperty"] = "unreleased property"

        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            dataset = client.update_dataset(dataset, ["newAlphaProperty"])

        final_attributes.assert_called_once_with(
            {"path": path, "fields": ["newAlphaProperty"]}, client, None
        )

        conn.api_request.assert_called_once_with(
            method="PATCH",
            data={"newAlphaProperty": "unreleased property"},
            path=path,
            timeout=DEFAULT_TIMEOUT,
            query_params={},
        )

        self.assertEqual(dataset.dataset_id, self.DS_ID)
        self.assertEqual(dataset.project, self.PROJECT)
        self.assertEqual(dataset._properties["newAlphaProperty"], "unreleased property")

    def test_update_model(self):
        from google.cloud.bigquery.model import Model

        path = "projects/%s/datasets/%s/models/%s" % (
            self.PROJECT,
            self.DS_ID,
            self.MODEL_ID,
        )
        description = "description"
        title = "title"
        expires = datetime.datetime(
            2012, 12, 21, 16, 0, 0, tzinfo=google.cloud._helpers.UTC
        )
        resource = {
            "modelReference": {
                "projectId": self.PROJECT,
                "datasetId": self.DS_ID,
                "modelId": self.MODEL_ID,
            },
            "description": description,
            "etag": "etag",
            "expirationTime": str(google.cloud._helpers._millis(expires)),
            "friendlyName": title,
            "labels": {"x": "y"},
        }
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        conn = client._connection = make_connection(resource, resource)
        model_id = "{}.{}.{}".format(self.PROJECT, self.DS_ID, self.MODEL_ID)
        model = Model(model_id)
        model.description = description
        model.friendly_name = title
        model.expires = expires
        model.labels = {"x": "y"}
        fields = ["description", "friendly_name", "labels", "expires"]
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            updated_model = client.update_model(model, fields, timeout=7.5)

        final_attributes.assert_called_once_with(
            {"path": "/%s" % path, "fields": fields}, client, None
        )

        sent = {
            "description": description,
            "expirationTime": str(google.cloud._helpers._millis(expires)),
            "friendlyName": title,
            "labels": {"x": "y"},
        }
        conn.api_request.assert_called_once_with(
            method="PATCH", data=sent, path="/" + path, timeout=7.5
        )
        self.assertEqual(updated_model.model_id, model.model_id)
        self.assertEqual(updated_model.description, model.description)
        self.assertEqual(updated_model.friendly_name, model.friendly_name)
        self.assertEqual(updated_model.labels, model.labels)
        self.assertEqual(updated_model.expires, model.expires)

        # ETag becomes If-Match header.
        model._properties["etag"] = "etag"
        client.update_model(model, [])
        req = conn.api_request.call_args
        self.assertEqual(req[1]["headers"]["If-Match"], "etag")

    def test_update_routine(self):
        from google.cloud.bigquery.routine import Routine, RoutineArgument

        full_routine_id = "routines-project.test_routines.updated_routine"
        resource = {
            "routineReference": {
                "projectId": "routines-project",
                "datasetId": "test_routines",
                "routineId": "updated_routine",
            },
            "routineType": "SCALAR_FUNCTION",
            "language": "SQL",
            "definitionBody": "x * 3",
            "arguments": [{"name": "x", "dataType": {"typeKind": "INT64"}}],
            "returnType": None,
            "someNewField": "someValue",
        }
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        conn = client._connection = make_connection(resource, resource)
        routine = Routine(full_routine_id)
        routine.arguments = [
            RoutineArgument(
                name="x",
                data_type=bigquery.standard_sql.StandardSqlDataType(
                    type_kind=bigquery.StandardSqlTypeNames.INT64
                ),
            )
        ]
        routine.body = "x * 3"
        routine.language = "SQL"
        routine.type_ = "SCALAR_FUNCTION"
        routine._properties["someNewField"] = "someValue"
        fields = [
            "arguments",
            "language",
            "body",
            "type_",
            "return_type",
            "someNewField",
        ]

        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            actual_routine = client.update_routine(
                routine,
                fields,
                timeout=7.5,
            )

        final_attributes.assert_called_once_with(
            {"path": routine.path, "fields": fields}, client, None
        )

        # TODO: routineReference isn't needed when the Routines API supports
        #       partial updates.
        sent = resource
        conn.api_request.assert_called_once_with(
            method="PUT",
            data=sent,
            path="/projects/routines-project/datasets/test_routines/routines/updated_routine",
            timeout=7.5,
        )
        self.assertEqual(actual_routine.arguments, routine.arguments)
        self.assertEqual(actual_routine.body, routine.body)
        self.assertEqual(actual_routine.language, routine.language)
        self.assertEqual(actual_routine.type_, routine.type_)

        # ETag becomes If-Match header.
        routine._properties["etag"] = "im-an-etag"
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            client.update_routine(routine, [])

        final_attributes.assert_called_once_with(
            {"path": routine.path, "fields": []}, client, None
        )

        req = conn.api_request.call_args
        self.assertEqual(req[1]["headers"]["If-Match"], "im-an-etag")

    def test_update_table(self):
        from google.cloud.bigquery.schema import PolicyTagList, SchemaField
        from google.cloud.bigquery.table import Table

        path = "projects/%s/datasets/%s/tables/%s" % (
            self.PROJECT,
            self.DS_ID,
            self.TABLE_ID,
        )
        description = "description"
        title = "title"
        resource = self._make_table_resource()
        resource.update(
            {
                "schema": {
                    "fields": [
                        {
                            "name": "full_name",
                            "type": "STRING",
                            "mode": "REQUIRED",
                            "description": None,
                            "policyTags": {"names": []},
                        },
                        {
                            "name": "age",
                            "type": "INTEGER",
                            "mode": "REQUIRED",
                            "description": "New field description",
                        },
                    ]
                },
                "etag": "etag",
                "description": description,
                "friendlyName": title,
                "labels": {"x": "y"},
                "resourceTags": {"123456789012/key": "value"},
            }
        )
        schema = [
            # Explicly setting policyTags to no names should be included in the sent resource.
            # https://github.com/googleapis/python-bigquery/issues/981
            SchemaField(
                "full_name",
                "STRING",
                mode="REQUIRED",
                description=None,
                policy_tags=PolicyTagList(names=()),
            ),
            SchemaField(
                "age", "INTEGER", mode="REQUIRED", description="New field description"
            ),
        ]
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        conn = client._connection = make_connection(resource, resource)
        table = Table(self.TABLE_REF, schema=schema)
        table.description = description
        table.friendly_name = title
        table.labels = {"x": "y"}
        table.resource_tags = {"123456789012/key": "value"}
        fields = ["schema", "description", "friendly_name", "labels", "resource_tags"]
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            updated_table = client.update_table(table, fields, timeout=7.5)
        span_path = "/%s" % path

        final_attributes.assert_called_once_with(
            {"path": span_path, "fields": fields}, client, None
        )

        sent = {
            "schema": {
                "fields": [
                    {
                        "name": "full_name",
                        "type": "STRING",
                        "mode": "REQUIRED",
                        "description": None,
                        "policyTags": {"names": []},
                    },
                    {
                        "name": "age",
                        "type": "INTEGER",
                        "mode": "REQUIRED",
                        "description": "New field description",
                    },
                ]
            },
            "description": description,
            "friendlyName": title,
            "labels": {"x": "y"},
            "resourceTags": {"123456789012/key": "value"},
        }
        conn.api_request.assert_called_once_with(
            method="PATCH", data=sent, path="/" + path, timeout=7.5, query_params={}
        )
        self.assertEqual(updated_table.description, table.description)
        self.assertEqual(updated_table.friendly_name, table.friendly_name)
        self.assertEqual(updated_table.schema, table.schema)
        self.assertEqual(updated_table.labels, table.labels)
        self.assertEqual(updated_table.resource_tags, table.resource_tags)

        # ETag becomes If-Match header.
        table._properties["etag"] = "etag"
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            client.update_table(table, [])

        final_attributes.assert_called_once_with(
            {"path": "/%s" % path, "fields": []}, client, None
        )

        req = conn.api_request.call_args
        self.assertEqual(req[1]["headers"]["If-Match"], "etag")

    def test_update_table_w_custom_property(self):
        from google.cloud.bigquery.table import Table

        path = "projects/%s/datasets/%s/tables/%s" % (
            self.PROJECT,
            self.DS_ID,
            self.TABLE_ID,
        )
        resource = self._make_table_resource()
        resource["newAlphaProperty"] = "unreleased property"
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        conn = client._connection = make_connection(resource)
        table = Table(self.TABLE_REF)
        table._properties["newAlphaProperty"] = "unreleased property"

        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            updated_table = client.update_table(table, ["newAlphaProperty"])

        final_attributes.assert_called_once_with(
            {"path": "/%s" % path, "fields": ["newAlphaProperty"]},
            client,
            None,
        )

        conn.api_request.assert_called_once_with(
            method="PATCH",
            path="/%s" % path,
            data={"newAlphaProperty": "unreleased property"},
            timeout=DEFAULT_TIMEOUT,
            query_params={},
        )
        self.assertEqual(
            updated_table._properties["newAlphaProperty"], "unreleased property"
        )

    def test_update_table_only_use_legacy_sql(self):
        from google.cloud.bigquery.table import Table

        path = "projects/%s/datasets/%s/tables/%s" % (
            self.PROJECT,
            self.DS_ID,
            self.TABLE_ID,
        )
        resource = self._make_table_resource()
        resource["view"] = {"useLegacySql": True}
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        conn = client._connection = make_connection(resource)
        table = Table(self.TABLE_REF)
        table.view_use_legacy_sql = True
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            updated_table = client.update_table(table, ["view_use_legacy_sql"])

        final_attributes.assert_called_once_with(
            {"path": "/%s" % path, "fields": ["view_use_legacy_sql"]},
            client,
            None,
        )

        conn.api_request.assert_called_once_with(
            method="PATCH",
            path="/%s" % path,
            data={"view": {"useLegacySql": True}},
            timeout=DEFAULT_TIMEOUT,
            query_params={},
        )
        self.assertEqual(updated_table.view_use_legacy_sql, table.view_use_legacy_sql)

    def test_update_table_w_query(self):
        import datetime

        from google.cloud._helpers import UTC, _millis
        from google.cloud.bigquery.schema import SchemaField
        from google.cloud.bigquery.table import Table

        path = "projects/%s/datasets/%s/tables/%s" % (
            self.PROJECT,
            self.DS_ID,
            self.TABLE_ID,
        )
        query = "select fullname, age from person_ages"
        location = "EU"
        exp_time = datetime.datetime(2015, 8, 1, 23, 59, 59, tzinfo=UTC)
        schema_resource = {
            "fields": [
                {
                    "name": "full_name",
                    "type": "STRING",
                    "mode": "REQUIRED",
                    "description": None,
                },
                {
                    "name": "age",
                    "type": "INTEGER",
                    "mode": "REQUIRED",
                    "description": "this is a column",
                },
                {"name": "country", "type": "STRING", "mode": "NULLABLE"},
            ]
        }
        schema = [
            SchemaField(
                "full_name",
                "STRING",
                mode="REQUIRED",
                # Explicitly unset the description.
                description=None,
            ),
            SchemaField(
                "age", "INTEGER", mode="REQUIRED", description="this is a column"
            ),
            # Omit the description to not make updates to it.
            SchemaField("country", "STRING"),
        ]
        resource = self._make_table_resource()
        resource.update(
            {
                "schema": schema_resource,
                "view": {"query": query, "useLegacySql": True},
                "location": location,
                "expirationTime": _millis(exp_time),
            }
        )
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        conn = client._connection = make_connection(resource)
        table = Table(self.TABLE_REF, schema=schema)
        table.expires = exp_time
        table.view_query = query
        table.view_use_legacy_sql = True
        updated_properties = ["schema", "view_query", "expires", "view_use_legacy_sql"]
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            updated_table = client.update_table(table, updated_properties)

        final_attributes.assert_called_once_with(
            {"path": "/%s" % path, "fields": updated_properties},
            client,
            None,
        )

        self.assertEqual(updated_table.schema, table.schema)
        self.assertEqual(updated_table.view_query, table.view_query)
        self.assertEqual(updated_table.expires, table.expires)
        self.assertEqual(updated_table.view_use_legacy_sql, table.view_use_legacy_sql)
        self.assertEqual(updated_table.location, location)

        conn.api_request.assert_called_once_with(
            method="PATCH",
            path="/%s" % path,
            data={
                "view": {"query": query, "useLegacySql": True},
                "expirationTime": str(_millis(exp_time)),
                "schema": schema_resource,
            },
            timeout=DEFAULT_TIMEOUT,
            query_params={},
        )

    def test_update_table_w_schema_None_autodetect_schema(self):
        # Simulate deleting schema:  not sure if back-end will actually
        # allow this operation, but the spec says it is optional.
        path = "projects/%s/datasets/%s/tables/%s" % (
            self.PROJECT,
            self.DS_ID,
            self.TABLE_ID,
        )
        resource1 = self._make_table_resource()
        resource1.update(
            {
                "schema": {
                    "fields": [
                        {"name": "full_name", "type": "STRING", "mode": "REQUIRED"},
                        {"name": "age", "type": "INTEGER", "mode": "REQUIRED"},
                    ]
                }
            }
        )
        resource2 = self._make_table_resource()
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        conn = client._connection = make_connection(resource1, resource2)
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            table = client.get_table(
                # Test with string for table ID
                "{}.{}.{}".format(
                    self.TABLE_REF.project,
                    self.TABLE_REF.dataset_id,
                    self.TABLE_REF.table_id,
                )
            )

        final_attributes.assert_called_once_with({"path": "/%s" % path}, client, None)

        table.schema = None

        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            updated_table = client.update_table(
                table, ["schema"], autodetect_schema=True
            )

        final_attributes.assert_called_once_with(
            {"path": "/%s" % path, "fields": ["schema"]}, client, None
        )

        self.assertEqual(len(conn.api_request.call_args_list), 2)
        req = conn.api_request.call_args_list[1]
        self.assertEqual(req[1]["method"], "PATCH")
        sent = {"schema": {"fields": None}}
        self.assertEqual(req[1]["data"], sent)
        self.assertEqual(req[1]["path"], "/%s" % path)
        self.assertEqual(req[1]["query_params"], {"autodetect_schema": True})
        self.assertEqual(len(updated_table.schema), 0)

    def test_update_table_delete_property(self):
        from google.cloud.bigquery.table import Table

        description = "description"
        title = "title"
        path = "projects/%s/datasets/%s/tables/%s" % (
            self.PROJECT,
            self.DS_ID,
            self.TABLE_ID,
        )
        resource1 = self._make_table_resource()
        resource1.update({"description": description, "friendlyName": title})
        resource2 = self._make_table_resource()
        resource2["description"] = None
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        conn = client._connection = make_connection(resource1, resource2)
        table = Table(self.TABLE_REF)
        table.description = description
        table.friendly_name = title

        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            table2 = client.update_table(table, ["description", "friendly_name"])

        final_attributes.assert_called_once_with(
            {"path": "/%s" % path, "fields": ["description", "friendly_name"]},
            client,
            None,
        )

        self.assertEqual(table2.description, table.description)
        table2.description = None

        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            table3 = client.update_table(table2, ["description"])

        final_attributes.assert_called_once_with(
            {"path": "/%s" % path, "fields": ["description"]}, client, None
        )

        self.assertEqual(len(conn.api_request.call_args_list), 2)
        req = conn.api_request.call_args_list[1]
        self.assertEqual(req[1]["method"], "PATCH")
        self.assertEqual(req[1]["path"], "/%s" % path)
        sent = {"description": None}
        self.assertEqual(req[1]["data"], sent)
        self.assertIsNone(table3.description)

    def test_delete_job_metadata_not_found(self):
        creds = _make_credentials()
        client = self._make_one("client-proj", creds, location="client-loc")
        conn = client._connection = make_connection(
            google.api_core.exceptions.NotFound("job not found"),
            google.api_core.exceptions.NotFound("job not found"),
        )

        with self.assertRaises(google.api_core.exceptions.NotFound):
            client.delete_job_metadata("my-job")

        conn.api_request.reset_mock()
        client.delete_job_metadata("my-job", not_found_ok=True)

        conn.api_request.assert_called_once_with(
            method="DELETE",
            path="/projects/client-proj/jobs/my-job/delete",
            query_params={"location": "client-loc"},
            timeout=DEFAULT_TIMEOUT,
        )

    def test_delete_job_metadata_with_id(self):
        creds = _make_credentials()
        client = self._make_one(self.PROJECT, creds)
        conn = client._connection = make_connection({})

        client.delete_job_metadata("my-job", project="param-proj", location="param-loc")

        conn.api_request.assert_called_once_with(
            method="DELETE",
            path="/projects/param-proj/jobs/my-job/delete",
            query_params={"location": "param-loc"},
            timeout=DEFAULT_TIMEOUT,
        )

    def test_delete_job_metadata_with_resource(self):
        from google.cloud.bigquery.job import QueryJob

        query_resource = {
            "jobReference": {
                "projectId": "job-based-proj",
                "jobId": "query_job",
                "location": "us-east1",
            },
            "configuration": {"query": {}},
        }
        creds = _make_credentials()
        client = self._make_one(self.PROJECT, creds)
        conn = client._connection = make_connection(query_resource)
        job_from_resource = QueryJob.from_api_repr(query_resource, client)

        client.delete_job_metadata(job_from_resource)

        conn.api_request.assert_called_once_with(
            method="DELETE",
            path="/projects/job-based-proj/jobs/query_job/delete",
            query_params={"location": "us-east1"},
            timeout=DEFAULT_TIMEOUT,
        )

    def test_delete_model(self):
        from google.cloud.bigquery.model import Model

        path = "projects/%s/datasets/%s/models/%s" % (
            self.PROJECT,
            self.DS_ID,
            self.MODEL_ID,
        )
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        model_id = "{}.{}.{}".format(self.PROJECT, self.DS_ID, self.MODEL_ID)
        models = (
            model_id,
            DatasetReference(self.PROJECT, self.DS_ID).model(self.MODEL_ID),
            Model(model_id),
        )
        conn = client._connection = make_connection(*([{}] * len(models)))

        for arg in models:
            with mock.patch(
                "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
            ) as final_attributes:
                client.delete_model(arg, timeout=7.5)

            final_attributes.assert_called_once_with(
                {"path": "/%s" % path}, client, None
            )
            conn.api_request.assert_called_with(
                method="DELETE", path="/%s" % path, timeout=7.5
            )

    def test_delete_model_w_wrong_type(self):
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        with self.assertRaises(TypeError):
            client.delete_model(DatasetReference(self.PROJECT, self.DS_ID))

    def test_delete_model_w_not_found_ok_false(self):
        path = "/projects/{}/datasets/{}/models/{}".format(
            self.PROJECT, self.DS_ID, self.MODEL_ID
        )
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(
            google.api_core.exceptions.NotFound("model not found")
        )

        with self.assertRaises(google.api_core.exceptions.NotFound):
            client.delete_model("{}.{}".format(self.DS_ID, self.MODEL_ID))

        conn.api_request.assert_called_with(
            method="DELETE", path=path, timeout=DEFAULT_TIMEOUT
        )

    def test_delete_model_w_not_found_ok_true(self):
        path = "/projects/{}/datasets/{}/models/{}".format(
            self.PROJECT, self.DS_ID, self.MODEL_ID
        )
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(
            google.api_core.exceptions.NotFound("model not found")
        )
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            client.delete_model(
                "{}.{}".format(self.DS_ID, self.MODEL_ID), not_found_ok=True
            )

        final_attributes.assert_called_once_with({"path": path}, client, None)

        conn.api_request.assert_called_with(
            method="DELETE", path=path, timeout=DEFAULT_TIMEOUT
        )

    def test_delete_routine(self):
        from google.cloud.bigquery.routine import Routine, RoutineReference

        full_routine_id = "test-routine-project.test_routines.minimal_routine"
        routines = [
            full_routine_id,
            Routine(full_routine_id),
            RoutineReference.from_string(full_routine_id),
        ]
        creds = _make_credentials()
        http = object()
        path = "/projects/test-routine-project/datasets/test_routines/routines/minimal_routine"
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(*([{}] * len(routines)))

        for routine in routines:
            with mock.patch(
                "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
            ) as final_attributes:
                client.delete_routine(routine, timeout=7.5)

            final_attributes.assert_called_once_with({"path": path}, client, None)

            conn.api_request.assert_called_with(
                method="DELETE",
                path=path,
                timeout=7.5,
            )

    def test_delete_routine_w_wrong_type(self):
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        with self.assertRaises(TypeError):
            client.delete_routine(DatasetReference(self.PROJECT, self.DS_ID))

    def test_delete_routine_w_not_found_ok_false(self):
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(
            google.api_core.exceptions.NotFound("routine not found")
        )
        path = "/projects/routines-project/datasets/test_routines/routines/test_routine"

        with self.assertRaises(google.api_core.exceptions.NotFound):
            with mock.patch(
                "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
            ) as final_attributes:
                client.delete_routine("routines-project.test_routines.test_routine")

        final_attributes.assert_called_once_with({"path": path}, client, None)

        conn.api_request.assert_called_with(
            method="DELETE",
            path=path,
            timeout=DEFAULT_TIMEOUT,
        )

    def test_delete_routine_w_not_found_ok_true(self):
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(
            google.api_core.exceptions.NotFound("routine not found")
        )
        path = "/projects/routines-project/datasets/test_routines/routines/test_routine"

        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            client.delete_routine(
                "routines-project.test_routines.test_routine", not_found_ok=True
            )

        final_attributes.assert_called_once_with({"path": path}, client, None)

        conn.api_request.assert_called_with(
            method="DELETE",
            path=path,
            timeout=DEFAULT_TIMEOUT,
        )

    def test_delete_table(self):
        from google.cloud.bigquery.table import Table

        tables = (
            self.TABLE_REF,
            Table(self.TABLE_REF),
            "{}.{}.{}".format(
                self.TABLE_REF.project,
                self.TABLE_REF.dataset_id,
                self.TABLE_REF.table_id,
            ),
        )
        path = "projects/%s/datasets/%s/tables/%s" % (
            self.PROJECT,
            self.DS_ID,
            self.TABLE_ID,
        )
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(*([{}] * len(tables)))

        for arg in tables:
            with mock.patch(
                "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
            ) as final_attributes:
                client.delete_table(arg, timeout=7.5)

            final_attributes.assert_called_once_with(
                {"path": "/%s" % path}, client, None
            )

            conn.api_request.assert_called_with(
                method="DELETE", path="/%s" % path, timeout=7.5
            )

    def test_delete_table_w_wrong_type(self):
        creds = _make_credentials()
        client = self._make_one(project=self.PROJECT, credentials=creds)
        with self.assertRaises(TypeError):
            client.delete_table(DatasetReference(self.PROJECT, self.DS_ID))

    def test_delete_table_w_not_found_ok_false(self):
        path = "/projects/{}/datasets/{}/tables/{}".format(
            self.PROJECT, self.DS_ID, self.TABLE_ID
        )
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(
            google.api_core.exceptions.NotFound("table not found")
        )

        with self.assertRaises(google.api_core.exceptions.NotFound):
            with mock.patch(
                "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
            ) as final_attributes:
                client.delete_table("{}.{}".format(self.DS_ID, self.TABLE_ID))

        final_attributes.assert_called_once_with({"path": path}, client, None)

        conn.api_request.assert_called_with(
            method="DELETE", path=path, timeout=DEFAULT_TIMEOUT
        )

    def test_delete_table_w_not_found_ok_true(self):
        path = "/projects/{}/datasets/{}/tables/{}".format(
            self.PROJECT, self.DS_ID, self.TABLE_ID
        )
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(
            google.api_core.exceptions.NotFound("table not found")
        )

        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            client.delete_table(
                "{}.{}".format(self.DS_ID, self.TABLE_ID), not_found_ok=True
            )

        final_attributes.assert_called_once_with({"path": path}, client, None)

        conn.api_request.assert_called_with(
            method="DELETE", path=path, timeout=DEFAULT_TIMEOUT
        )

    def _create_job_helper(self, job_config):
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)

        resource = {
            "jobReference": {"projectId": self.PROJECT, "jobId": "random-id"},
            "configuration": job_config,
        }
        expected = {
            "jobReference": {"projectId": self.PROJECT, "jobId": mock.ANY},
            "configuration": job_config,
        }
        conn = client._connection = make_connection(resource)
        client.create_job(job_config=job_config)

        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/%s/jobs" % self.PROJECT,
            data=expected,
            timeout=DEFAULT_TIMEOUT,
        )

    def test_create_job_load_config(self):
        configuration = {
            "load": {
                "destinationTable": {
                    "projectId": self.PROJECT,
                    "datasetId": self.DS_ID,
                    "tableId": "source_table",
                },
                "sourceUris": ["gs://test_bucket/src_object*"],
            }
        }

        self._create_job_helper(configuration)

    def test_create_job_copy_config(self):
        configuration = {
            "copy": {
                "sourceTables": [
                    {
                        "projectId": self.PROJECT,
                        "datasetId": self.DS_ID,
                        "tableId": "source_table",
                    }
                ],
                "destinationTable": {
                    "projectId": self.PROJECT,
                    "datasetId": self.DS_ID,
                    "tableId": "destination_table",
                },
            }
        }

        self._create_job_helper(configuration)

    def test_create_job_copy_config_w_single_source(self):
        configuration = {
            "copy": {
                "sourceTable": {
                    "projectId": self.PROJECT,
                    "datasetId": self.DS_ID,
                    "tableId": "source_table",
                },
                "destinationTable": {
                    "projectId": self.PROJECT,
                    "datasetId": self.DS_ID,
                    "tableId": "destination_table",
                },
            }
        }

        self._create_job_helper(configuration)

    def test_create_job_extract_config(self):
        configuration = {
            "extract": {
                "sourceTable": {
                    "projectId": self.PROJECT,
                    "datasetId": self.DS_ID,
                    "tableId": "source_table",
                },
                "destinationUris": ["gs://test_bucket/dst_object*"],
            }
        }
        self._create_job_helper(configuration)

    def test_create_job_extract_config_for_model(self):
        configuration = {
            "extract": {
                "sourceModel": {
                    "projectId": self.PROJECT,
                    "datasetId": self.DS_ID,
                    "modelId": "source_model",
                },
                "destinationUris": ["gs://test_bucket/dst_object*"],
            }
        }
        self._create_job_helper(configuration)

    def test_create_job_query_config(self):
        configuration = {
            "query": {
                "query": "query",
                "destinationTable": {"tableId": "table_id"},
                "useLegacySql": False,
            }
        }
        self._create_job_helper(configuration)

    def test_create_job_query_config_w_rateLimitExceeded_error(self):
        from google.cloud.bigquery.retry import DEFAULT_RETRY
        from google.cloud.exceptions import Forbidden

        query = "select count(*) from persons"
        configuration = {
            "query": {
                "query": query,
                "useLegacySql": False,
                "destinationTable": {"tableId": "table_id"},
            }
        }
        resource = {
            "jobReference": {"projectId": self.PROJECT, "jobId": mock.ANY},
            "configuration": {
                "query": {
                    "query": query,
                    "useLegacySql": False,
                    "destinationTable": {
                        "projectId": self.PROJECT,
                        "datasetId": self.DS_ID,
                        "tableId": "query_destination_table",
                    },
                }
            },
        }
        data_without_destination = {
            "jobReference": {"projectId": self.PROJECT, "jobId": mock.ANY},
            "configuration": configuration,
        }

        creds = _make_credentials()
        http = object()
        retry = DEFAULT_RETRY.with_deadline(1).with_predicate(
            lambda exc: isinstance(exc, Forbidden)
        )
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)

        api_request_patcher = mock.patch.object(
            client._connection,
            "api_request",
            side_effect=[
                Forbidden("", errors=[{"reason": "rateLimitExceeded"}]),
                resource,
            ],
        )

        with api_request_patcher as fake_api_request:
            job = client.create_job(job_config=configuration, retry=retry)

        self.assertEqual(job.destination.table_id, "query_destination_table")
        self.assertEqual(len(fake_api_request.call_args_list), 2)  # was retried once
        self.assertEqual(
            fake_api_request.call_args_list[1],
            mock.call(
                method="POST",
                path="/projects/PROJECT/jobs",
                data=data_without_destination,
                timeout=DEFAULT_TIMEOUT,
            ),
        )

    def test_create_job_w_invalid_job_config(self):
        configuration = {"unknown": {}}
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)

        with self.assertRaises(TypeError) as exc:
            client.create_job(job_config=configuration)

        self.assertIn("Invalid job configuration", exc.exception.args[0])

    def test_job_from_resource_unknown_type(self):
        from google.cloud.bigquery.job import UnknownJob

        creds = _make_credentials()
        client = self._make_one(self.PROJECT, creds)
        got = client.job_from_resource({})  # Can parse redacted job.
        self.assertIsInstance(got, UnknownJob)
        self.assertEqual(got.project, self.PROJECT)

    def test_get_job_miss_w_explict_project(self):
        from google.cloud.bigquery.retry import DEFAULT_GET_JOB_TIMEOUT
        from google.cloud.exceptions import NotFound

        OTHER_PROJECT = "OTHER_PROJECT"
        JOB_ID = "NONESUCH"
        creds = _make_credentials()
        client = self._make_one(self.PROJECT, creds)
        conn = client._connection = make_connection()

        with self.assertRaises(NotFound):
            client.get_job(JOB_ID, project=OTHER_PROJECT)

        conn.api_request.assert_called_once_with(
            method="GET",
            path="/projects/OTHER_PROJECT/jobs/NONESUCH",
            query_params={"projection": "full"},
            timeout=DEFAULT_GET_JOB_TIMEOUT,
        )

    def test_get_job_miss_w_client_location(self):
        from google.cloud.bigquery.retry import DEFAULT_GET_JOB_TIMEOUT
        from google.cloud.exceptions import NotFound

        JOB_ID = "NONESUCH"
        creds = _make_credentials()
        client = self._make_one("client-proj", creds, location="client-loc")
        conn = client._connection = make_connection()

        with self.assertRaises(NotFound):
            client.get_job(JOB_ID)

        conn.api_request.assert_called_once_with(
            method="GET",
            path="/projects/client-proj/jobs/NONESUCH",
            query_params={"projection": "full", "location": "client-loc"},
            timeout=DEFAULT_GET_JOB_TIMEOUT,
        )

    def test_get_job_hit_w_timeout(self):
        from google.cloud.bigquery.job import (
            CreateDisposition,
            QueryJob,
            WriteDisposition,
        )

        JOB_ID = "query_job"
        QUERY_DESTINATION_TABLE = "query_destination_table"
        QUERY = "SELECT * from test_dataset:test_table"
        ASYNC_QUERY_DATA = {
            "id": "{}:{}".format(self.PROJECT, JOB_ID),
            "jobReference": {
                "projectId": "resource-proj",
                "jobId": "query_job",
                "location": "us-east1",
            },
            "state": "DONE",
            "configuration": {
                "query": {
                    "query": QUERY,
                    "destinationTable": {
                        "projectId": self.PROJECT,
                        "datasetId": self.DS_ID,
                        "tableId": QUERY_DESTINATION_TABLE,
                    },
                    "createDisposition": CreateDisposition.CREATE_IF_NEEDED,
                    "writeDisposition": WriteDisposition.WRITE_TRUNCATE,
                }
            },
        }
        creds = _make_credentials()
        client = self._make_one(self.PROJECT, creds)
        conn = client._connection = make_connection(ASYNC_QUERY_DATA)
        job_from_resource = QueryJob.from_api_repr(ASYNC_QUERY_DATA, client)

        job = client.get_job(job_from_resource, timeout=7.5)

        self.assertIsInstance(job, QueryJob)
        self.assertEqual(job.job_id, JOB_ID)
        self.assertEqual(job.project, "resource-proj")
        self.assertEqual(job.location, "us-east1")
        self.assertEqual(job.create_disposition, CreateDisposition.CREATE_IF_NEEDED)
        self.assertEqual(job.write_disposition, WriteDisposition.WRITE_TRUNCATE)

        conn.api_request.assert_called_once_with(
            method="GET",
            path="/projects/resource-proj/jobs/query_job",
            query_params={"projection": "full", "location": "us-east1"},
            timeout=7.5,
        )

    def test_cancel_job_miss_w_explict_project(self):
        from google.cloud.exceptions import NotFound

        OTHER_PROJECT = "OTHER_PROJECT"
        JOB_ID = "NONESUCH"
        creds = _make_credentials()
        client = self._make_one(self.PROJECT, creds)
        conn = client._connection = make_connection()

        with self.assertRaises(NotFound):
            client.cancel_job(JOB_ID, project=OTHER_PROJECT, location=self.LOCATION)

        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/OTHER_PROJECT/jobs/NONESUCH/cancel",
            query_params={"projection": "full", "location": self.LOCATION},
            timeout=DEFAULT_TIMEOUT,
        )

    def test_cancel_job_miss_w_client_location(self):
        from google.cloud.exceptions import NotFound

        OTHER_PROJECT = "OTHER_PROJECT"
        JOB_ID = "NONESUCH"
        creds = _make_credentials()
        client = self._make_one(self.PROJECT, creds, location=self.LOCATION)
        conn = client._connection = make_connection()

        with self.assertRaises(NotFound):
            client.cancel_job(JOB_ID, project=OTHER_PROJECT)

        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/OTHER_PROJECT/jobs/NONESUCH/cancel",
            query_params={"projection": "full", "location": self.LOCATION},
            timeout=DEFAULT_TIMEOUT,
        )

    def test_cancel_job_hit(self):
        from google.cloud.bigquery.job import QueryJob

        JOB_ID = "query_job"
        QUERY = "SELECT * from test_dataset:test_table"
        QUERY_JOB_RESOURCE = {
            "id": "{}:{}".format(self.PROJECT, JOB_ID),
            "jobReference": {
                "projectId": "job-based-proj",
                "jobId": "query_job",
                "location": "asia-northeast1",
            },
            "state": "RUNNING",
            "configuration": {"query": {"query": QUERY}},
        }
        RESOURCE = {"job": QUERY_JOB_RESOURCE}
        creds = _make_credentials()
        client = self._make_one(self.PROJECT, creds)
        conn = client._connection = make_connection(RESOURCE)
        job_from_resource = QueryJob.from_api_repr(QUERY_JOB_RESOURCE, client)

        job = client.cancel_job(job_from_resource)

        self.assertIsInstance(job, QueryJob)
        self.assertEqual(job.job_id, JOB_ID)
        self.assertEqual(job.project, "job-based-proj")
        self.assertEqual(job.location, "asia-northeast1")
        self.assertEqual(job.query, QUERY)

        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/job-based-proj/jobs/query_job/cancel",
            query_params={"projection": "full", "location": "asia-northeast1"},
            timeout=DEFAULT_TIMEOUT,
        )

    def test_cancel_job_w_timeout(self):
        JOB_ID = "query_job"
        QUERY = "SELECT * from test_dataset:test_table"
        QUERY_JOB_RESOURCE = {
            "id": "{}:{}".format(self.PROJECT, JOB_ID),
            "jobReference": {"projectId": self.PROJECT, "jobId": "query_job"},
            "state": "RUNNING",
            "configuration": {"query": {"query": QUERY}},
        }
        RESOURCE = {"job": QUERY_JOB_RESOURCE}

        creds = _make_credentials()
        client = self._make_one(self.PROJECT, creds)
        conn = client._connection = make_connection(RESOURCE)

        client.cancel_job(JOB_ID, timeout=7.5)

        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/{}/jobs/query_job/cancel".format(self.PROJECT),
            query_params={"projection": "full"},
            timeout=7.5,
        )

    def test_load_table_from_uri(self):
        from google.cloud.bigquery.job import LoadJob, LoadJobConfig

        JOB = "job_name"
        DESTINATION = "destination_table"
        SOURCE_URI = "http://example.com/source.csv"
        RESOURCE = {
            "jobReference": {"projectId": self.PROJECT, "jobId": JOB},
            "configuration": {
                "load": {
                    "sourceUris": [SOURCE_URI],
                    "destinationTable": {
                        "projectId": self.PROJECT,
                        "datasetId": self.DS_ID,
                        "tableId": DESTINATION,
                    },
                }
            },
        }
        creds = _make_credentials()
        http = object()
        job_config = LoadJobConfig()
        original_config_copy = copy.deepcopy(job_config)

        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(RESOURCE)
        destination = DatasetReference(self.PROJECT, self.DS_ID).table(DESTINATION)

        job = client.load_table_from_uri(
            SOURCE_URI, destination, job_id=JOB, job_config=job_config, timeout=7.5
        )

        # Check that load_table_from_uri actually starts the job.
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/%s/jobs" % self.PROJECT,
            data=RESOURCE,
            timeout=7.5,
        )

        # the original config object should not have been modified
        self.assertEqual(job_config.to_api_repr(), original_config_copy.to_api_repr())

        self.assertIsInstance(job, LoadJob)
        self.assertIsInstance(job.configuration, LoadJobConfig)
        self.assertIs(job._client, client)
        self.assertEqual(job.job_id, JOB)
        self.assertEqual(list(job.source_uris), [SOURCE_URI])
        self.assertEqual(job.destination, destination)

        conn = client._connection = make_connection(RESOURCE)

        job = client.load_table_from_uri([SOURCE_URI], destination, job_id=JOB)
        self.assertIsInstance(job, LoadJob)
        self.assertIs(job._client, client)
        self.assertEqual(job.job_id, JOB)
        self.assertEqual(list(job.source_uris), [SOURCE_URI])
        self.assertEqual(job.destination, destination)

    def test_load_table_from_uri_w_explicit_project(self):
        job_id = "this-is-a-job-id"
        destination_id = "destination_table"
        source_uri = "gs://example/source.csv"
        resource = {
            "jobReference": {
                "projectId": "other-project",
                "location": self.LOCATION,
                "jobId": job_id,
            },
            "configuration": {
                "load": {
                    "sourceUris": [source_uri],
                    "destinationTable": {
                        "projectId": self.PROJECT,
                        "datasetId": self.DS_ID,
                        "tableId": destination_id,
                    },
                }
            },
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(resource)
        destination = DatasetReference(self.PROJECT, self.DS_ID).table(destination_id)

        client.load_table_from_uri(
            source_uri,
            destination,
            job_id=job_id,
            project="other-project",
            location=self.LOCATION,
        )

        # Check that load_table_from_uri actually starts the job.
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/other-project/jobs",
            data=resource,
            timeout=DEFAULT_TIMEOUT,
        )

    def test_load_table_from_uri_w_client_location(self):
        job_id = "this-is-a-job-id"
        destination_id = "destination_table"
        source_uri = "gs://example/source.csv"
        resource = {
            "jobReference": {
                "projectId": "other-project",
                "location": self.LOCATION,
                "jobId": job_id,
            },
            "configuration": {
                "load": {
                    "sourceUris": [source_uri],
                    "destinationTable": {
                        "projectId": self.PROJECT,
                        "datasetId": self.DS_ID,
                        "tableId": destination_id,
                    },
                }
            },
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(
            project=self.PROJECT, credentials=creds, _http=http, location=self.LOCATION
        )
        conn = client._connection = make_connection(resource)

        client.load_table_from_uri(
            source_uri,
            # Test with string for table ID.
            "{}.{}".format(self.DS_ID, destination_id),
            job_id=job_id,
            project="other-project",
        )

        # Check that load_table_from_uri actually starts the job.
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/other-project/jobs",
            data=resource,
            timeout=DEFAULT_TIMEOUT,
        )

    def test_load_table_from_uri_w_invalid_job_config(self):
        from google.cloud.bigquery import job

        JOB = "job_name"
        DESTINATION = "destination_table"
        SOURCE_URI = "http://example.com/source.csv"

        creds = _make_credentials()
        http = object()
        job_config = job.CopyJobConfig()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        destination = DatasetReference(self.PROJECT, self.DS_ID).table(DESTINATION)

        with self.assertRaises(TypeError) as exc:
            client.load_table_from_uri(
                SOURCE_URI, destination, job_id=JOB, job_config=job_config
            )

        self.assertIn("Expected an instance of LoadJobConfig", exc.exception.args[0])

    def test_load_table_from_uri_w_explicit_job_config(self):
        from google.cloud.bigquery.job import LoadJobConfig

        JOB = "job_name"
        DESTINATION = "destination_table"
        SOURCE_URI = "http://example.com/source.csv"
        RESOURCE = {
            "jobReference": {"jobId": JOB, "projectId": self.PROJECT},
            "configuration": {
                "load": {
                    "sourceUris": [SOURCE_URI],
                    "destinationTable": {
                        "projectId": self.PROJECT,
                        "datasetId": self.DS_ID,
                        "tableId": DESTINATION,
                    },
                    "createSession": True,
                    "encoding": "UTF-8",
                }
            },
        }

        creds = _make_credentials()
        http = object()

        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(RESOURCE)
        destination = DatasetReference(self.PROJECT, self.DS_ID).table(DESTINATION)

        job_config = LoadJobConfig()
        job_config.create_session = True
        job_config.encoding = "UTF-8"
        client.load_table_from_uri(
            SOURCE_URI, destination, job_id=JOB, job_config=job_config
        )

        # Check that load_table_from_uri actually starts the job.
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/%s/jobs" % self.PROJECT,
            data=RESOURCE,
            timeout=DEFAULT_TIMEOUT,
        )

    def test_load_table_from_uri_w_explicit_job_config_override(self):
        from google.cloud.bigquery.job import LoadJobConfig

        JOB = "job_name"
        DESTINATION = "destination_table"
        SOURCE_URI = "http://example.com/source.csv"
        RESOURCE = {
            "jobReference": {"jobId": JOB, "projectId": self.PROJECT},
            "configuration": {
                "load": {
                    "sourceUris": [SOURCE_URI],
                    "destinationTable": {
                        "projectId": self.PROJECT,
                        "datasetId": self.DS_ID,
                        "tableId": DESTINATION,
                    },
                    "createSession": False,
                    "encoding": "ISO-8859-1",
                }
            },
        }

        creds = _make_credentials()
        http = object()
        default_job_config = LoadJobConfig()
        default_job_config.create_session = True
        default_job_config.encoding = "ISO-8859-1"

        client = self._make_one(
            project=self.PROJECT,
            credentials=creds,
            _http=http,
            default_load_job_config=default_job_config,
        )
        conn = client._connection = make_connection(RESOURCE)
        destination = DatasetReference(self.PROJECT, self.DS_ID).table(DESTINATION)

        job_config = LoadJobConfig()
        job_config.create_session = False
        client.load_table_from_uri(
            SOURCE_URI, destination, job_id=JOB, job_config=job_config
        )

        # Check that load_table_from_uri actually starts the job.
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/%s/jobs" % self.PROJECT,
            data=RESOURCE,
            timeout=DEFAULT_TIMEOUT,
        )

    def test_load_table_from_uri_w_default_load_config(self):
        from google.cloud.bigquery.job import LoadJobConfig

        JOB = "job_name"
        DESTINATION = "destination_table"
        SOURCE_URI = "http://example.com/source.csv"
        RESOURCE = {
            "jobReference": {"jobId": JOB, "projectId": self.PROJECT},
            "configuration": {
                "load": {
                    "sourceUris": [SOURCE_URI],
                    "destinationTable": {
                        "projectId": self.PROJECT,
                        "datasetId": self.DS_ID,
                        "tableId": DESTINATION,
                    },
                    "encoding": "ISO-8859-1",
                }
            },
        }

        creds = _make_credentials()
        http = object()
        default_job_config = LoadJobConfig()
        default_job_config.encoding = "ISO-8859-1"

        client = self._make_one(
            project=self.PROJECT,
            credentials=creds,
            _http=http,
            default_load_job_config=default_job_config,
        )
        conn = client._connection = make_connection(RESOURCE)
        destination = DatasetReference(self.PROJECT, self.DS_ID).table(DESTINATION)

        client.load_table_from_uri(SOURCE_URI, destination, job_id=JOB)

        # Check that load_table_from_uri actually starts the job.
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/%s/jobs" % self.PROJECT,
            data=RESOURCE,
            timeout=DEFAULT_TIMEOUT,
        )

    def test_copy_table(self):
        from google.cloud.bigquery.job import CopyJob

        JOB = "job_name"
        SOURCE = "source_table"
        DESTINATION = "destination_table"
        RESOURCE = {
            "jobReference": {"projectId": self.PROJECT, "jobId": JOB},
            "configuration": {
                "copy": {
                    "sourceTables": [
                        {
                            "projectId": self.PROJECT,
                            "datasetId": self.DS_ID,
                            "tableId": SOURCE,
                        }
                    ],
                    "destinationTable": {
                        "projectId": self.PROJECT,
                        "datasetId": self.DS_ID,
                        "tableId": DESTINATION,
                    },
                }
            },
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(RESOURCE)
        dataset = DatasetReference(self.PROJECT, self.DS_ID)
        source = dataset.table(SOURCE)
        destination = dataset.table(DESTINATION)

        job = client.copy_table(source, destination, job_id=JOB, timeout=7.5)

        # Check that copy_table actually starts the job.
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/%s/jobs" % self.PROJECT,
            data=RESOURCE,
            timeout=7.5,
        )

        self.assertIsInstance(job, CopyJob)
        self.assertIs(job._client, client)
        self.assertEqual(job.job_id, JOB)
        self.assertEqual(list(job.sources), [source])
        self.assertEqual(job.destination, destination)

    def test_copy_table_w_multiple_sources(self):
        from google.cloud.bigquery.job import CopyJob
        from google.cloud.bigquery.table import TableReference

        job_id = "job_name"
        source_id = "my-project.my_dataset.source_table"
        source_id2 = "my-project.my_dataset.source_table2"
        destination_id = "my-other-project.another_dataset.destination_table"
        expected_resource = {
            "jobReference": {"projectId": self.PROJECT, "jobId": job_id},
            "configuration": {
                "copy": {
                    "sourceTables": [
                        {
                            "projectId": "my-project",
                            "datasetId": "my_dataset",
                            "tableId": "source_table",
                        },
                        {
                            "projectId": "my-project",
                            "datasetId": "my_dataset",
                            "tableId": "source_table2",
                        },
                    ],
                    "destinationTable": {
                        "projectId": "my-other-project",
                        "datasetId": "another_dataset",
                        "tableId": "destination_table",
                    },
                }
            },
        }
        returned_resource = expected_resource.copy()
        returned_resource["statistics"] = {}
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(returned_resource)

        job = client.copy_table([source_id, source_id2], destination_id, job_id=job_id)

        # Check that copy_table actually starts the job.
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/%s/jobs" % self.PROJECT,
            data=expected_resource,
            timeout=DEFAULT_TIMEOUT,
        )
        self.assertIsInstance(job, CopyJob)
        self.assertIs(job._client, client)
        self.assertEqual(job.job_id, job_id)
        self.assertEqual(
            list(sorted(job.sources, key=lambda tbl: tbl.table_id)),
            [
                TableReference.from_string(source_id),
                TableReference.from_string(source_id2),
            ],
        )
        self.assertEqual(job.destination, TableReference.from_string(destination_id))

    def test_copy_table_w_explicit_project(self):
        job_id = "this-is-a-job-id"
        source_id = "source_table"
        destination_id = "destination_table"
        resource = {
            "jobReference": {
                "projectId": "other-project",
                "location": self.LOCATION,
                "jobId": job_id,
            },
            "configuration": {
                "copy": {
                    "sourceTables": [
                        {
                            "projectId": self.PROJECT,
                            "datasetId": self.DS_ID,
                            "tableId": source_id,
                        }
                    ],
                    "destinationTable": {
                        "projectId": self.PROJECT,
                        "datasetId": self.DS_ID,
                        "tableId": destination_id,
                    },
                }
            },
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(resource)
        dataset = DatasetReference(self.PROJECT, self.DS_ID)
        source = dataset.table(source_id)
        destination = dataset.table(destination_id)

        client.copy_table(
            source,
            destination,
            job_id=job_id,
            project="other-project",
            location=self.LOCATION,
        )

        # Check that copy_table actually starts the job.
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/other-project/jobs",
            data=resource,
            timeout=DEFAULT_TIMEOUT,
        )

    def test_copy_table_w_client_location(self):
        job_id = "this-is-a-job-id"
        source_id = "source_table"
        destination_id = "destination_table"
        resource = {
            "jobReference": {
                "projectId": "other-project",
                "location": self.LOCATION,
                "jobId": job_id,
            },
            "configuration": {
                "copy": {
                    "sourceTables": [
                        {
                            "projectId": self.PROJECT,
                            "datasetId": self.DS_ID,
                            "tableId": source_id,
                        }
                    ],
                    "destinationTable": {
                        "projectId": self.PROJECT,
                        "datasetId": self.DS_ID,
                        "tableId": destination_id,
                    },
                }
            },
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(
            project=self.PROJECT, credentials=creds, _http=http, location=self.LOCATION
        )
        conn = client._connection = make_connection(resource)

        client.copy_table(
            # Test with string for table IDs.
            "{}.{}".format(self.DS_ID, source_id),
            "{}.{}".format(self.DS_ID, destination_id),
            job_id=job_id,
            project="other-project",
        )

        # Check that copy_table actually starts the job.
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/other-project/jobs",
            data=resource,
            timeout=DEFAULT_TIMEOUT,
        )

    def test_copy_table_w_source_strings(self):
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection({})
        sources = [
            "dataset_wo_proj.some_table",
            "other_project.other_dataset.other_table",
            DatasetReference(client.project, "dataset_from_ref").table(
                "table_from_ref"
            ),
        ]
        destination = "some_project.some_dataset.destination_table"

        job = client.copy_table(sources, destination)

        # Replace job with the request instead of response so we can verify those properties.
        _, kwargs = conn.api_request.call_args
        request = kwargs["data"]
        job._properties = request

        expected_sources = [
            DatasetReference(client.project, "dataset_wo_proj").table("some_table"),
            DatasetReference("other_project", "other_dataset").table("other_table"),
            DatasetReference(client.project, "dataset_from_ref").table(
                "table_from_ref"
            ),
        ]
        self.assertEqual(list(job.sources), expected_sources)
        expected_destination = DatasetReference("some_project", "some_dataset").table(
            "destination_table"
        )
        self.assertEqual(job.destination, expected_destination)

    def test_copy_table_w_invalid_job_config(self):
        from google.cloud.bigquery import job

        JOB = "job_name"
        SOURCE = "source_table"
        DESTINATION = "destination_table"

        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        job_config = job.ExtractJobConfig()
        dataset = DatasetReference(self.PROJECT, self.DS_ID)
        source = dataset.table(SOURCE)
        destination = dataset.table(DESTINATION)
        with self.assertRaises(TypeError) as exc:
            client.copy_table(source, destination, job_id=JOB, job_config=job_config)

        self.assertIn("Expected an instance of CopyJobConfig", exc.exception.args[0])

    def test_copy_table_w_valid_job_config(self):
        from google.cloud.bigquery.job import CopyJobConfig

        JOB = "job_name"
        SOURCE = "source_table"
        DESTINATION = "destination_table"
        RESOURCE = {
            "jobReference": {"projectId": self.PROJECT, "jobId": JOB},
            "configuration": {
                "copy": {
                    "sourceTables": [
                        {
                            "projectId": self.PROJECT,
                            "datasetId": self.DS_ID,
                            "tableId": SOURCE,
                        }
                    ],
                    "destinationTable": {
                        "projectId": self.PROJECT,
                        "datasetId": self.DS_ID,
                        "tableId": DESTINATION,
                    },
                }
            },
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(RESOURCE)
        dataset = DatasetReference(self.PROJECT, self.DS_ID)
        source = dataset.table(SOURCE)
        destination = dataset.table(DESTINATION)

        job_config = CopyJobConfig()
        original_config_copy = copy.deepcopy(job_config)
        job = client.copy_table(source, destination, job_id=JOB, job_config=job_config)

        # Check that copy_table actually starts the job.
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/%s/jobs" % self.PROJECT,
            data=RESOURCE,
            timeout=DEFAULT_TIMEOUT,
        )
        self.assertIsInstance(job.configuration, CopyJobConfig)

        # the original config object should not have been modified
        assert job_config.to_api_repr() == original_config_copy.to_api_repr()

    def test_extract_table(self):
        from google.cloud.bigquery.job import ExtractJob

        JOB = "job_id"
        SOURCE = "source_table"
        DESTINATION = "gs://bucket_name/object_name"
        RESOURCE = {
            "jobReference": {"projectId": self.PROJECT, "jobId": JOB},
            "configuration": {
                "extract": {
                    "sourceTable": {
                        "projectId": self.PROJECT,
                        "datasetId": self.DS_ID,
                        "tableId": SOURCE,
                    },
                    "destinationUris": [DESTINATION],
                }
            },
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(RESOURCE)
        dataset = DatasetReference(self.PROJECT, self.DS_ID)
        source = dataset.table(SOURCE)

        job = client.extract_table(source, DESTINATION, job_id=JOB, timeout=7.5)

        # Check that extract_table actually starts the job.
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/PROJECT/jobs",
            data=RESOURCE,
            timeout=7.5,
        )

        # Check the job resource.
        self.assertIsInstance(job, ExtractJob)
        self.assertIs(job._client, client)
        self.assertEqual(job.job_id, JOB)
        self.assertEqual(job.source, source)
        self.assertEqual(list(job.destination_uris), [DESTINATION])

    def test_extract_table_w_invalid_job_config(self):
        from google.cloud.bigquery import job

        JOB = "job_id"
        SOURCE = "source_table"
        DESTINATION = "gs://bucket_name/object_name"

        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        dataset = DatasetReference(self.PROJECT, self.DS_ID)
        source = dataset.table(SOURCE)
        job_config = job.LoadJobConfig()
        with self.assertRaises(TypeError) as exc:
            client.extract_table(source, DESTINATION, job_id=JOB, job_config=job_config)

        self.assertIn("Expected an instance of ExtractJobConfig", exc.exception.args[0])

    def test_extract_table_w_explicit_project(self):
        job_id = "job_id"
        source_id = "source_table"
        destination = "gs://bucket_name/object_name"
        resource = {
            "jobReference": {
                "projectId": "other-project",
                "location": self.LOCATION,
                "jobId": job_id,
            },
            "configuration": {
                "extract": {
                    "sourceTable": {
                        "projectId": self.PROJECT,
                        "datasetId": self.DS_ID,
                        "tableId": source_id,
                    },
                    "destinationUris": [destination],
                }
            },
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(resource)
        dataset = DatasetReference(self.PROJECT, self.DS_ID)
        source = dataset.table(source_id)

        client.extract_table(
            source,
            destination,
            job_id=job_id,
            project="other-project",
            location=self.LOCATION,
        )

        # Check that extract_table actually starts the job.
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/other-project/jobs",
            data=resource,
            timeout=DEFAULT_TIMEOUT,
        )

    def test_extract_table_w_client_location(self):
        job_id = "job_id"
        source_id = "source_table"
        destination = "gs://bucket_name/object_name"
        resource = {
            "jobReference": {
                "projectId": "other-project",
                "location": self.LOCATION,
                "jobId": job_id,
            },
            "configuration": {
                "extract": {
                    "sourceTable": {
                        "projectId": self.PROJECT,
                        "datasetId": self.DS_ID,
                        "tableId": source_id,
                    },
                    "destinationUris": [destination],
                }
            },
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(
            project=self.PROJECT, credentials=creds, _http=http, location=self.LOCATION
        )
        conn = client._connection = make_connection(resource)

        client.extract_table(
            # Test with string for table ID.
            "{}.{}".format(self.DS_ID, source_id),
            destination,
            job_id=job_id,
            project="other-project",
        )

        # Check that extract_table actually starts the job.
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/other-project/jobs",
            data=resource,
            timeout=DEFAULT_TIMEOUT,
        )

    def test_extract_table_generated_job_id(self):
        from google.cloud.bigquery.job import (
            DestinationFormat,
            ExtractJob,
            ExtractJobConfig,
        )

        JOB = "job_id"
        SOURCE = "source_table"
        DESTINATION = "gs://bucket_name/object_name"
        RESOURCE = {
            "jobReference": {"projectId": self.PROJECT, "jobId": JOB},
            "configuration": {
                "extract": {
                    "sourceTable": {
                        "projectId": self.PROJECT,
                        "datasetId": self.DS_ID,
                        "tableId": SOURCE,
                    },
                    "destinationUris": [DESTINATION],
                    "destinationFormat": "NEWLINE_DELIMITED_JSON",
                }
            },
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(RESOURCE)
        dataset = DatasetReference(self.PROJECT, self.DS_ID)
        source = dataset.table(SOURCE)
        job_config = ExtractJobConfig()
        job_config.destination_format = DestinationFormat.NEWLINE_DELIMITED_JSON
        original_config_copy = copy.deepcopy(job_config)

        job = client.extract_table(source, DESTINATION, job_config=job_config)

        # Check that extract_table actually starts the job.
        conn.api_request.assert_called_once()
        _, req = conn.api_request.call_args
        self.assertEqual(req["method"], "POST")
        self.assertEqual(req["path"], "/projects/PROJECT/jobs")
        self.assertIsInstance(req["data"]["jobReference"]["jobId"], str)
        self.assertEqual(req["timeout"], DEFAULT_TIMEOUT)

        # Check the job resource.
        self.assertIsInstance(job, ExtractJob)
        self.assertIs(job._client, client)
        self.assertEqual(job.source, source)
        self.assertEqual(list(job.destination_uris), [DESTINATION])

        # the original config object should not have been modified
        assert job_config.to_api_repr() == original_config_copy.to_api_repr()

    def test_extract_table_w_destination_uris(self):
        from google.cloud.bigquery.job import ExtractJob

        JOB = "job_id"
        SOURCE = "source_table"
        DESTINATION1 = "gs://bucket_name/object_one"
        DESTINATION2 = "gs://bucket_name/object_two"
        RESOURCE = {
            "jobReference": {"projectId": self.PROJECT, "jobId": JOB},
            "configuration": {
                "extract": {
                    "sourceTable": {
                        "projectId": self.PROJECT,
                        "datasetId": self.DS_ID,
                        "tableId": SOURCE,
                    },
                    "destinationUris": [DESTINATION1, DESTINATION2],
                }
            },
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(RESOURCE)
        dataset = DatasetReference(self.PROJECT, self.DS_ID)
        source = dataset.table(SOURCE)

        job = client.extract_table(source, [DESTINATION1, DESTINATION2], job_id=JOB)

        # Check that extract_table actually starts the job.
        conn.api_request.assert_called_once()
        _, req = conn.api_request.call_args
        self.assertEqual(req["method"], "POST")
        self.assertEqual(req["path"], "/projects/PROJECT/jobs")
        self.assertEqual(req["timeout"], DEFAULT_TIMEOUT)

        # Check the job resource.
        self.assertIsInstance(job, ExtractJob)
        self.assertIs(job._client, client)
        self.assertEqual(job.job_id, JOB)
        self.assertEqual(job.source, source)
        self.assertEqual(list(job.destination_uris), [DESTINATION1, DESTINATION2])

    def test_extract_table_for_source_type_model(self):
        from google.cloud.bigquery.job import ExtractJob

        JOB = "job_id"
        SOURCE = "source_model"
        DESTINATION = "gs://bucket_name/object_name"
        RESOURCE = {
            "jobReference": {"projectId": self.PROJECT, "jobId": JOB},
            "configuration": {
                "extract": {
                    "sourceModel": {
                        "projectId": self.PROJECT,
                        "datasetId": self.DS_ID,
                        "modelId": SOURCE,
                    },
                    "destinationUris": [DESTINATION],
                }
            },
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(RESOURCE)
        dataset = DatasetReference(self.PROJECT, self.DS_ID)
        source = dataset.model(SOURCE)

        job = client.extract_table(
            source, DESTINATION, job_id=JOB, timeout=7.5, source_type="Model"
        )

        # Check that extract_table actually starts the job.
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/PROJECT/jobs",
            data=RESOURCE,
            timeout=7.5,
        )

        # Check the job resource.
        self.assertIsInstance(job, ExtractJob)
        self.assertIs(job._client, client)
        self.assertEqual(job.job_id, JOB)
        self.assertEqual(job.source, source)
        self.assertEqual(list(job.destination_uris), [DESTINATION])

    def test_extract_table_for_source_type_model_w_string_model_id(self):
        JOB = "job_id"
        source_id = "source_model"
        DESTINATION = "gs://bucket_name/object_name"
        RESOURCE = {
            "jobReference": {"projectId": self.PROJECT, "jobId": JOB},
            "configuration": {
                "extract": {
                    "sourceModel": {
                        "projectId": self.PROJECT,
                        "datasetId": self.DS_ID,
                        "modelId": source_id,
                    },
                    "destinationUris": [DESTINATION],
                }
            },
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(RESOURCE)

        client.extract_table(
            # Test with string for model ID.
            "{}.{}".format(self.DS_ID, source_id),
            DESTINATION,
            job_id=JOB,
            timeout=7.5,
            source_type="Model",
        )

        # Check that extract_table actually starts the job.
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/PROJECT/jobs",
            data=RESOURCE,
            timeout=7.5,
        )

    def test_extract_table_for_source_type_model_w_model_object(self):
        from google.cloud.bigquery.model import Model

        JOB = "job_id"
        DESTINATION = "gs://bucket_name/object_name"
        model_id = "{}.{}.{}".format(self.PROJECT, self.DS_ID, self.MODEL_ID)
        model = Model(model_id)
        RESOURCE = {
            "jobReference": {"projectId": self.PROJECT, "jobId": JOB},
            "configuration": {
                "extract": {
                    "sourceModel": {
                        "projectId": self.PROJECT,
                        "datasetId": self.DS_ID,
                        "modelId": self.MODEL_ID,
                    },
                    "destinationUris": [DESTINATION],
                }
            },
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(RESOURCE)

        client.extract_table(
            # Test with Model class object.
            model,
            DESTINATION,
            job_id=JOB,
            timeout=7.5,
            source_type="Model",
        )

        # Check that extract_table actually starts the job.
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/PROJECT/jobs",
            data=RESOURCE,
            timeout=7.5,
        )

    def test_extract_table_for_invalid_source_type_model(self):
        JOB = "job_id"
        SOURCE = "source_model"
        DESTINATION = "gs://bucket_name/object_name"
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        dataset = DatasetReference(self.PROJECT, self.DS_ID)
        source = dataset.model(SOURCE)

        with self.assertRaises(ValueError) as exc:
            client.extract_table(
                source, DESTINATION, job_id=JOB, timeout=7.5, source_type="foo"
            )

        self.assertIn("Cannot pass", exc.exception.args[0])

    def test_query_defaults(self):
        from google.cloud.bigquery.job import QueryJob

        QUERY = "select count(*) from persons"
        RESOURCE = {
            "jobReference": {"projectId": self.PROJECT, "jobId": "some-random-id"},
            "configuration": {"query": {"query": QUERY, "useLegacySql": False}},
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(RESOURCE)

        job = client.query(QUERY)

        self.assertIsInstance(job, QueryJob)
        self.assertIsInstance(job.job_id, str)
        self.assertIs(job._client, client)
        self.assertEqual(job.query, QUERY)
        self.assertEqual(job.udf_resources, [])
        self.assertEqual(job.query_parameters, [])

        # Check that query actually starts the job.
        conn.api_request.assert_called_once()
        _, req = conn.api_request.call_args
        self.assertEqual(req["method"], "POST")
        self.assertEqual(req["path"], "/projects/PROJECT/jobs")
        self.assertEqual(req["timeout"], DEFAULT_TIMEOUT)
        sent = req["data"]
        self.assertIsInstance(sent["jobReference"]["jobId"], str)
        sent_config = sent["configuration"]["query"]
        self.assertEqual(sent_config["query"], QUERY)
        self.assertFalse(sent_config["useLegacySql"])

    def test_query_w_api_method_query(self):
        query = "select count(*) from persons"
        response = {
            "jobReference": {
                "projectId": self.PROJECT,
                "location": "EU",
                "jobId": "abcd",
            },
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(response)

        job = client.query(query, location="EU", api_method="QUERY")

        self.assertEqual(job.query, query)
        self.assertEqual(job.job_id, "abcd")
        self.assertEqual(job.location, "EU")

        # Check that query actually starts the job.
        expected_resource = {
            "query": query,
            "useLegacySql": False,
            "location": "EU",
            "formatOptions": {"useInt64Timestamp": True},
            "requestId": mock.ANY,
        }
        conn.api_request.assert_called_once_with(
            method="POST",
            path=f"/projects/{self.PROJECT}/queries",
            data=expected_resource,
            timeout=None,
        )

    def test_query_w_api_method_query_legacy_sql(self):
        from google.cloud.bigquery import QueryJobConfig

        query = "select count(*) from persons"
        response = {
            "jobReference": {
                "projectId": self.PROJECT,
                "location": "EU",
                "jobId": "abcd",
            },
        }
        job_config = QueryJobConfig()
        job_config.use_legacy_sql = True
        job_config.maximum_bytes_billed = 100
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(response)

        job = client.query(
            query, location="EU", job_config=job_config, api_method="QUERY"
        )

        self.assertEqual(job.query, query)
        self.assertEqual(job.job_id, "abcd")
        self.assertEqual(job.location, "EU")

        # Check that query actually starts the job.
        expected_resource = {
            "query": query,
            "useLegacySql": True,
            "location": "EU",
            "formatOptions": {"useInt64Timestamp": True},
            "requestId": mock.ANY,
            "maximumBytesBilled": "100",
        }
        conn.api_request.assert_called_once_with(
            method="POST",
            path=f"/projects/{self.PROJECT}/queries",
            data=expected_resource,
            timeout=None,
        )

    def test_query_w_api_method_query_parameters(self):
        from google.cloud.bigquery import QueryJobConfig, ScalarQueryParameter

        query = "select count(*) from persons"
        response = {
            "jobReference": {
                "projectId": self.PROJECT,
                "location": "EU",
                "jobId": "abcd",
            },
        }
        job_config = QueryJobConfig()
        job_config.dry_run = True
        job_config.query_parameters = [ScalarQueryParameter("param1", "INTEGER", 123)]
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(response)

        job = client.query(
            query, location="EU", job_config=job_config, api_method="QUERY"
        )

        self.assertEqual(job.query, query)
        self.assertEqual(job.job_id, "abcd")
        self.assertEqual(job.location, "EU")

        # Check that query actually starts the job.
        expected_resource = {
            "query": query,
            "dryRun": True,
            "useLegacySql": False,
            "location": "EU",
            "formatOptions": {"useInt64Timestamp": True},
            "requestId": mock.ANY,
            "parameterMode": "NAMED",
            "queryParameters": [
                {
                    "name": "param1",
                    "parameterType": {"type": "INTEGER"},
                    "parameterValue": {"value": "123"},
                },
            ],
        }
        conn.api_request.assert_called_once_with(
            method="POST",
            path=f"/projects/{self.PROJECT}/queries",
            data=expected_resource,
            timeout=None,
        )

    def test_query_w_api_method_query_and_job_id_fails(self):
        query = "select count(*) from persons"
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        client._connection = make_connection({})

        with self.assertRaises(TypeError) as exc:
            client.query(query, job_id="abcd", api_method="QUERY", job_retry=None)
        self.assertIn(
            "`job_id` was provided, but the 'QUERY' `api_method` was requested",
            exc.exception.args[0],
        )

    def test_query_w_api_method_unknown(self):
        query = "select count(*) from persons"
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        client._connection = make_connection({})

        with self.assertRaises(ValueError) as exc:
            client.query(query, api_method="UNKNOWN")
        self.assertIn("Got unexpected value for api_method: ", exc.exception.args[0])

    def test_query_w_explicit_timeout(self):
        query = "select count(*) from persons"
        resource = {
            "jobReference": {"projectId": self.PROJECT, "jobId": mock.ANY},
            "configuration": {"query": {"query": query, "useLegacySql": False}},
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(resource)

        client.query(query, timeout=7.5)

        # Check that query actually starts the job.
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/{}/jobs".format(self.PROJECT),
            data=resource,
            timeout=7.5,
        )

    def test_query_w_explicit_project(self):
        job_id = "some-job-id"
        query = "select count(*) from persons"
        resource = {
            "jobReference": {
                "projectId": "other-project",
                "location": self.LOCATION,
                "jobId": job_id,
            },
            "configuration": {"query": {"query": query, "useLegacySql": False}},
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(resource)

        client.query(
            query,
            job_id=job_id,
            project="other-project",
            location=self.LOCATION,
            job_retry=None,
        )

        # Check that query actually starts the job.
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/other-project/jobs",
            data=resource,
            timeout=DEFAULT_TIMEOUT,
        )

    def test_query_w_explicit_job_config(self):
        job_id = "some-job-id"
        query = "select count(*) from persons"
        resource = {
            "jobReference": {
                "jobId": job_id,
                "projectId": self.PROJECT,
                "location": self.LOCATION,
            },
            "configuration": {
                "query": {
                    "query": query,
                    "defaultDataset": {
                        "projectId": self.PROJECT,
                        "datasetId": "some-dataset",
                    },
                    "useLegacySql": False,
                    "useQueryCache": True,
                    "maximumBytesBilled": "2000",
                }
            },
        }

        creds = _make_credentials()
        http = object()

        from google.cloud.bigquery import DatasetReference, QueryJobConfig

        default_job_config = QueryJobConfig()
        default_job_config.default_dataset = DatasetReference(
            self.PROJECT, "some-dataset"
        )
        default_job_config.maximum_bytes_billed = 1000

        client = self._make_one(
            project=self.PROJECT,
            credentials=creds,
            _http=http,
            default_query_job_config=default_job_config,
        )
        conn = client._connection = make_connection(resource)

        job_config = QueryJobConfig()
        job_config.use_query_cache = True
        job_config.maximum_bytes_billed = 2000
        original_config_copy = copy.deepcopy(job_config)

        client.query(
            query,
            job_id=job_id,
            location=self.LOCATION,
            job_config=job_config,
            job_retry=None,
        )

        # Check that query actually starts the job.
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/PROJECT/jobs",
            data=resource,
            timeout=DEFAULT_TIMEOUT,
        )

        # the original config object should not have been modified
        assert job_config.to_api_repr() == original_config_copy.to_api_repr()

    def test_query_preserving_explicit_job_config(self):
        job_id = "some-job-id"
        query = "select count(*) from persons"
        resource = {
            "jobReference": {
                "jobId": job_id,
                "projectId": self.PROJECT,
                "location": self.LOCATION,
            },
            "configuration": {
                "query": {
                    "query": query,
                    "useLegacySql": False,
                    "useQueryCache": True,
                    "maximumBytesBilled": "2000",
                }
            },
        }

        creds = _make_credentials()
        http = object()

        from google.cloud.bigquery import QueryJobConfig

        client = self._make_one(
            project=self.PROJECT,
            credentials=creds,
            _http=http,
        )
        conn = client._connection = make_connection(resource)

        job_config = QueryJobConfig()
        job_config.use_query_cache = True
        job_config.maximum_bytes_billed = 2000
        original_config_copy = copy.deepcopy(job_config)

        client.query(
            query,
            job_id=job_id,
            location=self.LOCATION,
            job_config=job_config,
            job_retry=None,
        )

        # Check that query actually starts the job.
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/PROJECT/jobs",
            data=resource,
            timeout=DEFAULT_TIMEOUT,
        )

        # the original config object should not have been modified
        assert job_config.to_api_repr() == original_config_copy.to_api_repr()

    def test_query_preserving_explicit_default_job_config(self):
        job_id = "some-job-id"
        query = "select count(*) from persons"
        resource = {
            "jobReference": {
                "jobId": job_id,
                "projectId": self.PROJECT,
                "location": self.LOCATION,
            },
            "configuration": {
                "query": {
                    "query": query,
                    "defaultDataset": {
                        "projectId": self.PROJECT,
                        "datasetId": "some-dataset",
                    },
                    "useLegacySql": False,
                    "maximumBytesBilled": "1000",
                }
            },
        }

        creds = _make_credentials()
        http = object()

        from google.cloud.bigquery import DatasetReference, QueryJobConfig

        default_job_config = QueryJobConfig()
        default_job_config.default_dataset = DatasetReference(
            self.PROJECT, "some-dataset"
        )
        default_job_config.maximum_bytes_billed = 1000
        default_config_copy = copy.deepcopy(default_job_config)

        client = self._make_one(
            project=self.PROJECT,
            credentials=creds,
            _http=http,
            default_query_job_config=default_job_config,
        )
        conn = client._connection = make_connection(resource)

        client.query(
            query,
            job_id=job_id,
            location=self.LOCATION,
            job_config=None,
            job_retry=None,
        )

        # Check that query actually starts the job.
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/PROJECT/jobs",
            data=resource,
            timeout=DEFAULT_TIMEOUT,
        )

        # the original default config object should not have been modified
        assert default_job_config.to_api_repr() == default_config_copy.to_api_repr()

    def test_query_w_invalid_job_config(self):
        from google.cloud.bigquery import DatasetReference, QueryJobConfig, job

        job_id = "some-job-id"
        query = "select count(*) from persons"
        creds = _make_credentials()
        http = object()
        default_job_config = QueryJobConfig()
        default_job_config.default_dataset = DatasetReference(
            self.PROJECT, "some-dataset"
        )
        default_job_config.maximum_bytes_billed = 1000

        client = self._make_one(
            project=self.PROJECT,
            credentials=creds,
            _http=http,
            default_query_job_config=default_job_config,
        )

        job_config = job.LoadJobConfig()

        with self.assertRaises(TypeError) as exc:
            client.query(
                query,
                job_id=job_id,
                location=self.LOCATION,
                job_config=job_config,
                job_retry=None,
            )
        self.assertIn("Expected an instance of QueryJobConfig", exc.exception.args[0])

    def test_query_w_explicit_job_config_override(self):
        job_id = "some-job-id"
        query = "select count(*) from persons"
        resource = {
            "jobReference": {
                "jobId": job_id,
                "projectId": self.PROJECT,
                "location": self.LOCATION,
            },
            "configuration": {
                "query": {
                    "query": query,
                    "defaultDataset": None,
                    "useLegacySql": False,
                    "useQueryCache": True,
                    "maximumBytesBilled": "2000",
                }
            },
        }

        creds = _make_credentials()
        http = object()

        from google.cloud.bigquery import DatasetReference, QueryJobConfig

        default_job_config = QueryJobConfig()
        default_job_config.default_dataset = DatasetReference(
            self.PROJECT, "some-dataset"
        )
        default_job_config.maximum_bytes_billed = 1000

        client = self._make_one(
            project=self.PROJECT,
            credentials=creds,
            _http=http,
            default_query_job_config=default_job_config,
        )
        conn = client._connection = make_connection(resource)

        job_config = QueryJobConfig()
        job_config.use_query_cache = True
        job_config.maximum_bytes_billed = 2000
        job_config.default_dataset = None

        client.query(
            query,
            job_id=job_id,
            location=self.LOCATION,
            job_config=job_config,
            job_retry=None,
        )

        # Check that query actually starts the job.
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/PROJECT/jobs",
            data=resource,
            timeout=DEFAULT_TIMEOUT,
        )

    def test_query_w_client_default_config_no_incoming(self):
        job_id = "some-job-id"
        query = "select count(*) from persons"
        resource = {
            "jobReference": {
                "jobId": job_id,
                "projectId": self.PROJECT,
                "location": self.LOCATION,
            },
            "configuration": {
                "query": {
                    "query": query,
                    "useLegacySql": False,
                    "maximumBytesBilled": "1000",
                }
            },
        }

        creds = _make_credentials()
        http = object()

        from google.cloud.bigquery import QueryJobConfig

        default_job_config = QueryJobConfig()
        default_job_config.maximum_bytes_billed = 1000

        client = self._make_one(
            project=self.PROJECT,
            credentials=creds,
            _http=http,
            default_query_job_config=default_job_config,
        )
        conn = client._connection = make_connection(resource)

        client.query(query, job_id=job_id, location=self.LOCATION, job_retry=None)

        # Check that query actually starts the job.
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/PROJECT/jobs",
            data=resource,
            timeout=DEFAULT_TIMEOUT,
        )

    def test_query_w_invalid_default_job_config(self):
        creds = _make_credentials()
        http = object()
        default_job_config = object()

        with self.assertRaises(TypeError) as exc:
            self._make_one(
                project=self.PROJECT,
                credentials=creds,
                _http=http,
                default_query_job_config=default_job_config,
            )
        self.assertIn("Expected an instance of QueryJobConfig", exc.exception.args[0])

    def test_query_w_client_location(self):
        job_id = "some-job-id"
        query = "select count(*) from persons"
        resource = {
            "jobReference": {
                "projectId": "other-project",
                "location": self.LOCATION,
                "jobId": job_id,
            },
            "configuration": {"query": {"query": query, "useLegacySql": False}},
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(
            project=self.PROJECT, credentials=creds, _http=http, location=self.LOCATION
        )
        conn = client._connection = make_connection(resource)

        client.query(query, job_id=job_id, project="other-project", job_retry=None)

        # Check that query actually starts the job.
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/other-project/jobs",
            data=resource,
            timeout=DEFAULT_TIMEOUT,
        )

    def test_query_detect_location(self):
        query = "select count(*) from persons"
        resource_location = "EU"
        resource = {
            "jobReference": {
                "projectId": self.PROJECT,
                # Location not set in request, but present in the response.
                "location": resource_location,
                "jobId": "some-random-id",
            },
            "configuration": {"query": {"query": query, "useLegacySql": False}},
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(resource)

        job = client.query(query)

        self.assertEqual(job.location, resource_location)

        # Check that request did not contain a location.
        conn.api_request.assert_called_once()
        _, req = conn.api_request.call_args
        sent = req["data"]
        self.assertIsNone(sent["jobReference"].get("location"))

    def test_query_w_udf_resources(self):
        from google.cloud.bigquery.job import QueryJob, QueryJobConfig
        from google.cloud.bigquery.query import UDFResource

        RESOURCE_URI = "gs://some-bucket/js/lib.js"
        JOB = "job_name"
        QUERY = "select count(*) from persons"
        RESOURCE = {
            "jobReference": {"projectId": self.PROJECT, "jobId": JOB},
            "configuration": {
                "query": {
                    "query": QUERY,
                    "useLegacySql": True,
                    "userDefinedFunctionResources": [{"resourceUri": RESOURCE_URI}],
                }
            },
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(RESOURCE)
        udf_resources = [UDFResource("resourceUri", RESOURCE_URI)]
        config = QueryJobConfig()
        config.udf_resources = udf_resources
        config.use_legacy_sql = True

        job = client.query(QUERY, job_config=config, job_id=JOB, job_retry=None)

        self.assertIsInstance(job, QueryJob)
        self.assertIs(job._client, client)
        self.assertEqual(job.job_id, JOB)
        self.assertEqual(job.query, QUERY)
        self.assertEqual(job.udf_resources, udf_resources)
        self.assertEqual(job.query_parameters, [])

        # Check that query actually starts the job.
        conn.api_request.assert_called_once()
        _, req = conn.api_request.call_args
        self.assertEqual(req["method"], "POST")
        self.assertEqual(req["path"], "/projects/PROJECT/jobs")
        self.assertEqual(req["timeout"], DEFAULT_TIMEOUT)
        sent = req["data"]
        self.assertIsInstance(sent["jobReference"]["jobId"], str)
        sent_config = sent["configuration"]["query"]
        self.assertEqual(sent_config["query"], QUERY)
        self.assertTrue(sent_config["useLegacySql"])
        self.assertEqual(
            sent_config["userDefinedFunctionResources"][0],
            {"resourceUri": RESOURCE_URI},
        )

    def test_query_w_query_parameters(self):
        from google.cloud.bigquery.job import QueryJob, QueryJobConfig
        from google.cloud.bigquery.query import ScalarQueryParameter

        JOB = "job_name"
        QUERY = "select count(*) from persons"
        RESOURCE = {
            "jobReference": {"projectId": self.PROJECT, "jobId": JOB},
            "configuration": {
                "query": {
                    "query": QUERY,
                    "useLegacySql": False,
                    "queryParameters": [
                        {
                            "name": "foo",
                            "parameterType": {"type": "INT64"},
                            "parameterValue": {"value": "123"},
                        }
                    ],
                }
            },
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(RESOURCE)
        query_parameters = [ScalarQueryParameter("foo", "INT64", 123)]
        config = QueryJobConfig()
        config.query_parameters = query_parameters

        job = client.query(QUERY, job_config=config, job_id=JOB, job_retry=None)

        self.assertIsInstance(job, QueryJob)
        self.assertIs(job._client, client)
        self.assertEqual(job.job_id, JOB)
        self.assertEqual(job.query, QUERY)
        self.assertEqual(job.udf_resources, [])
        self.assertEqual(job.query_parameters, query_parameters)

        # Check that query actually starts the job.
        conn.api_request.assert_called_once()
        _, req = conn.api_request.call_args
        self.assertEqual(req["method"], "POST")
        self.assertEqual(req["path"], "/projects/PROJECT/jobs")
        self.assertEqual(req["timeout"], DEFAULT_TIMEOUT)
        sent = req["data"]
        self.assertEqual(sent["jobReference"]["jobId"], JOB)
        sent_config = sent["configuration"]["query"]
        self.assertEqual(sent_config["query"], QUERY)
        self.assertFalse(sent_config["useLegacySql"])
        self.assertEqual(
            sent_config["queryParameters"][0],
            {
                "name": "foo",
                "parameterType": {"type": "INT64"},
                "parameterValue": {"value": "123"},
            },
        )

    def test_query_pico_timestamp(self):
        query = "select *;"
        response = {
            "jobReference": {
                "projectId": self.PROJECT,
                "location": "EU",
                "jobId": "abcd",
            },
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(response)

        client.query(
            query,
            location="EU",
            api_method="QUERY",
            timestamp_precision=TimestampPrecision.PICOSECOND,
        )

        # Check that query actually starts the job.
        expected_resource = {
            "query": query,
            "useLegacySql": False,
            "location": "EU",
            "formatOptions": {"timestampOutputFormat": "ISO8601_STRING"},
            "requestId": mock.ANY,
        }
        conn.api_request.assert_called_once_with(
            method="POST",
            path=f"/projects/{self.PROJECT}/queries",
            data=expected_resource,
            timeout=None,
        )

    def test_query_pico_timestamp_insert_error(self):
        query = "select *;"
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)

        with pytest.raises(ValueError, match="Picosecond Timestamp is only"):
            client.query(
                query,
                location="EU",
                api_method="INSERT",
                timestamp_precision=TimestampPrecision.PICOSECOND,
            )

    def test_query_job_rpc_fail_w_random_error(self):
        from google.api_core.exceptions import Unknown
        from google.cloud.bigquery.job import QueryJob

        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)

        job_create_error = Unknown("Not sure what went wrong.")
        job_begin_patcher = mock.patch.object(
            QueryJob, "_begin", side_effect=job_create_error
        )
        with job_begin_patcher:
            with pytest.raises(Unknown, match="Not sure what went wrong."):
                client.query("SELECT 1;", job_id="123", job_retry=None)

    def test_query_job_rpc_fail_w_conflict_job_id_given(self):
        from google.api_core.exceptions import Conflict
        from google.cloud.bigquery.job import QueryJob

        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)

        job_create_error = Conflict("Job already exists.")
        job_begin_patcher = mock.patch.object(
            QueryJob, "_begin", side_effect=job_create_error
        )
        with job_begin_patcher:
            with pytest.raises(Conflict, match="Job already exists."):
                client.query("SELECT 1;", job_id="123", job_retry=None)

    def test_query_job_rpc_fail_w_conflict_random_id_job_fetch_fails(self):
        from google.api_core.exceptions import Conflict, DataLoss
        from google.cloud.bigquery.job import QueryJob

        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)

        job_create_error = Conflict("Job already exists.")
        job_begin_patcher = mock.patch.object(
            QueryJob, "_begin", side_effect=job_create_error
        )
        get_job_patcher = mock.patch.object(
            client, "get_job", side_effect=DataLoss("we lost your job, sorry")
        )

        with job_begin_patcher, get_job_patcher:
            # If get job request fails but supposedly there does exist a job
            # with this ID already, raise the exception explaining why we
            # couldn't recover the job.
            with pytest.raises(DataLoss, match="we lost your job, sorry"):
                client.query("SELECT 1;", job_id=None)

    def test_query_job_rpc_fail_w_conflict_random_id_job_fetch_fails_no_retries(self):
        from google.api_core.exceptions import Conflict, DataLoss
        from google.cloud.bigquery.job import QueryJob

        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)

        job_create_error = Conflict("Job already exists.")
        job_begin_patcher = mock.patch.object(
            QueryJob, "_begin", side_effect=job_create_error
        )
        get_job_patcher = mock.patch.object(
            client, "get_job", side_effect=DataLoss("we lost your job, sorry")
        )

        with job_begin_patcher, get_job_patcher:
            # If get job request fails but supposedly there does exist a job
            # with this ID already, raise the exception explaining why we
            # couldn't recover the job.
            with pytest.raises(DataLoss, match="we lost your job, sorry"):
                client.query(
                    "SELECT 1;",
                    job_id=None,
                    # Explicitly test with no retries to make sure those branches are covered.
                    retry=None,
                    job_retry=None,
                )

    def test_query_job_rpc_fail_w_conflict_random_id_job_fetch_succeeds(self):
        from google.api_core.exceptions import Conflict
        from google.cloud.bigquery.job import QueryJob

        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)

        job_create_error = Conflict("Job already exists.")
        job_begin_patcher = mock.patch.object(
            QueryJob, "_begin", side_effect=job_create_error
        )
        get_job_patcher = mock.patch.object(
            client, "get_job", return_value=mock.sentinel.query_job
        )

        with job_begin_patcher, get_job_patcher:
            result = client.query("SELECT 1;", job_id=None)

        assert result is mock.sentinel.query_job

    def test_query_and_wait_defaults(self):
        query = "select count(*) from `bigquery-public-data.usa_names.usa_1910_2013`"
        jobs_query_response = {
            "jobComplete": True,
            "schema": {
                "fields": [
                    {
                        "name": "f0_",
                        "type": "INTEGER",
                        "mode": "NULLABLE",
                    },
                ],
            },
            "totalRows": "1",
            "rows": [{"f": [{"v": "5552452"}]}],
            "queryId": "job_abcDEF_",
            "totalBytesProcessed": 1234,
            "totalSlotMs": 5678,
            "creationTime": "1437767599006",
            "startTime": "1437767600007",
            "endTime": "1437767601008",
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(jobs_query_response)

        rows = client.query_and_wait(query)

        self.assertIsInstance(rows, google.cloud.bigquery.table.RowIterator)
        self.assertEqual(rows.query_id, "job_abcDEF_")
        self.assertEqual(rows.total_rows, 1)
        # No job reference in the response should be OK for completed query.
        self.assertIsNone(rows.job_id)
        self.assertIsNone(rows.project)
        self.assertIsNone(rows.location)
        self.assertEqual(rows.query, query)
        self.assertEqual(rows.total_bytes_processed, 1234)
        self.assertEqual(rows.slot_millis, 5678)
        self.assertEqual(rows.created.timestamp() * 1000, 1437767599006)
        self.assertEqual(rows.started.timestamp() * 1000, 1437767600007)
        self.assertEqual(rows.ended.timestamp() * 1000, 1437767601008)

        # Verify the request we send is to jobs.query.
        conn.api_request.assert_called_once()
        _, req = conn.api_request.call_args
        self.assertEqual(req["method"], "POST")
        self.assertEqual(req["path"], "/projects/PROJECT/queries")
        self.assertEqual(req["timeout"], DEFAULT_TIMEOUT)
        sent = req["data"]
        self.assertEqual(sent["query"], query)
        self.assertFalse(sent["useLegacySql"])

    def test_query_and_wait_w_default_query_job_config(self):
        from google.cloud.bigquery import job

        query = "select count(*) from `bigquery-public-data.usa_names.usa_1910_2013`"
        jobs_query_response = {
            "jobComplete": True,
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(
            project=self.PROJECT,
            credentials=creds,
            _http=http,
            default_query_job_config=job.QueryJobConfig(
                labels={
                    "default-label": "default-value",
                },
            ),
        )
        conn = client._connection = make_connection(jobs_query_response)

        _ = client.query_and_wait(query)

        # Verify the request we send is to jobs.query.
        conn.api_request.assert_called_once()
        _, req = conn.api_request.call_args
        self.assertEqual(req["method"], "POST")
        self.assertEqual(req["path"], f"/projects/{self.PROJECT}/queries")
        sent = req["data"]
        self.assertEqual(sent["labels"], {"default-label": "default-value"})

    def test_query_and_wait_w_job_config(self):
        from google.cloud.bigquery import job

        query = "select count(*) from `bigquery-public-data.usa_names.usa_1910_2013`"
        jobs_query_response = {
            "jobComplete": True,
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(
            project=self.PROJECT,
            credentials=creds,
            _http=http,
        )
        conn = client._connection = make_connection(jobs_query_response)

        _ = client.query_and_wait(
            query,
            job_config=job.QueryJobConfig(
                labels={
                    "job_config-label": "job_config-value",
                },
            ),
        )

        # Verify the request we send is to jobs.query.
        conn.api_request.assert_called_once()
        _, req = conn.api_request.call_args
        self.assertEqual(req["method"], "POST")
        self.assertEqual(req["path"], f"/projects/{self.PROJECT}/queries")
        sent = req["data"]
        self.assertEqual(sent["labels"], {"job_config-label": "job_config-value"})

    def test_query_and_wait_w_location(self):
        query = "select count(*) from `bigquery-public-data.usa_names.usa_1910_2013`"
        jobs_query_response = {
            "jobComplete": True,
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(jobs_query_response)

        _ = client.query_and_wait(query, location="not-the-client-location")

        # Verify the request we send is to jobs.query.
        conn.api_request.assert_called_once()
        _, req = conn.api_request.call_args
        self.assertEqual(req["method"], "POST")
        self.assertEqual(req["path"], f"/projects/{self.PROJECT}/queries")
        sent = req["data"]
        self.assertEqual(sent["location"], "not-the-client-location")

    def test_query_and_wait_w_max_results(self):
        query = "select count(*) from `bigquery-public-data.usa_names.usa_1910_2013`"
        jobs_query_response = {
            "jobComplete": True,
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(jobs_query_response)

        _ = client.query_and_wait(query, max_results=11)

        # Verify the request we send is to jobs.query.
        conn.api_request.assert_called_once()
        _, req = conn.api_request.call_args
        self.assertEqual(req["method"], "POST")
        self.assertEqual(req["path"], f"/projects/{self.PROJECT}/queries")
        sent = req["data"]
        self.assertTrue(sent["formatOptions"]["useInt64Timestamp"])
        self.assertTrue(sent["maxResults"], 11)

    def test_query_and_wait_w_page_size(self):
        query = "select count(*) from `bigquery-public-data.usa_names.usa_1910_2013`"
        jobs_query_response = {
            "jobComplete": True,
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(jobs_query_response)

        _ = client.query_and_wait(query, page_size=11)

        # Verify the request we send is to jobs.query.
        conn.api_request.assert_called_once()
        _, req = conn.api_request.call_args
        self.assertEqual(req["method"], "POST")
        self.assertEqual(req["path"], f"/projects/{self.PROJECT}/queries")
        sent = req["data"]
        self.assertTrue(sent["formatOptions"]["useInt64Timestamp"])
        self.assertTrue(sent["maxResults"], 11)

    def test_query_and_wait_w_page_size_multiple_requests(self):
        """
        For queries that last longer than the intial (about 10s) call to
        jobs.query, we should still pass through the page size to the
        subsequent calls to jobs.getQueryResults.

        See internal issue 344008814.
        """
        query = "select count(*) from `bigquery-public-data.usa_names.usa_1910_2013`"
        job_reference = {
            "projectId": "my-jobs-project",
            "location": "my-jobs-location",
            "jobId": "my-jobs-id",
        }
        jobs_query_response = {
            "jobComplete": False,
            "jobReference": job_reference,
        }
        jobs_get_response = {
            "jobReference": job_reference,
            "status": {"state": "DONE"},
        }
        get_query_results_response = {
            "jobComplete": True,
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(
            jobs_query_response,
            jobs_get_response,
            get_query_results_response,
        )

        _ = client.query_and_wait(query, page_size=11)

        conn.api_request.assert_has_calls(
            [
                # Verify the request we send is to jobs.query.
                mock.call(
                    method="POST",
                    path=f"/projects/{self.PROJECT}/queries",
                    data={
                        "useLegacySql": False,
                        "query": query,
                        "formatOptions": {"useInt64Timestamp": True},
                        "maxResults": 11,
                        "requestId": mock.ANY,
                    },
                    timeout=None,
                ),
                # jobs.get: Check if the job has finished.
                mock.call(
                    method="GET",
                    path="/projects/my-jobs-project/jobs/my-jobs-id",
                    query_params={
                        "projection": "full",
                        "location": "my-jobs-location",
                    },
                    timeout=google.cloud.bigquery.retry.DEFAULT_GET_JOB_TIMEOUT,
                ),
                # jobs.getQueryResults: wait for the query / fetch first page
                mock.call(
                    method="GET",
                    path="/projects/my-jobs-project/queries/my-jobs-id",
                    query_params={
                        # We should still pass through the page size to the
                        # subsequent calls to jobs.getQueryResults.
                        #
                        # See internal issue 344008814.
                        "maxResults": 11,
                        "formatOptions.useInt64Timestamp": True,
                        "location": "my-jobs-location",
                    },
                    timeout=None,
                ),
            ]
        )

    def test_query_and_wait_w_project(self):
        query = "select count(*) from `bigquery-public-data.usa_names.usa_1910_2013`"
        jobs_query_response = {
            "jobComplete": True,
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(jobs_query_response)

        _ = client.query_and_wait(query, project="not-the-client-project")

        # Verify the request we send is to jobs.query.
        conn.api_request.assert_called_once()
        _, req = conn.api_request.call_args
        self.assertEqual(req["method"], "POST")
        self.assertEqual(req["path"], "/projects/not-the-client-project/queries")

    def test_insert_rows_w_timeout(self):
        from google.cloud.bigquery.schema import SchemaField
        from google.cloud.bigquery.table import Table

        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection({})
        table = Table(self.TABLE_REF)

        ROWS = [
            ("Phred Phlyntstone", 32),
            ("Bharney Rhubble", 33),
        ]
        schema = [
            SchemaField("full_name", "STRING", mode="REQUIRED"),
            SchemaField("age", "INTEGER", mode="REQUIRED"),
        ]

        client.insert_rows(table, ROWS, selected_fields=schema, timeout=7.5)

        conn.api_request.assert_called_once()
        _, req = conn.api_request.call_args
        self.assertEqual(req.get("timeout"), 7.5)

    def test_insert_rows_wo_schema(self):
        from google.cloud.bigquery.table import Table

        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        table = Table(self.TABLE_REF)
        ROWS = [
            ("Phred Phlyntstone", 32),
            ("Bharney Rhubble", 33),
            ("Wylma Phlyntstone", 29),
            ("Bhettye Rhubble", 27),
        ]

        with self.assertRaises(ValueError) as exc:
            client.insert_rows(table, ROWS)

        self.assertIn("Could not determine schema for table", exc.exception.args[0])

    def test_insert_rows_w_schema(self):
        import datetime

        from google.cloud._helpers import _RFC3339_MICROS, UTC, _datetime_to_rfc3339
        from google.cloud.bigquery.schema import SchemaField

        WHEN_TS = 1437767599.006
        WHEN = datetime.datetime.fromtimestamp(WHEN_TS, UTC).replace(tzinfo=UTC)
        PATH = "projects/%s/datasets/%s/tables/%s/insertAll" % (
            self.PROJECT,
            self.DS_ID,
            self.TABLE_ID,
        )
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection({})
        schema = [
            SchemaField("full_name", "STRING", mode="REQUIRED"),
            SchemaField("age", "INTEGER", mode="REQUIRED"),
            SchemaField("joined", "TIMESTAMP", mode="NULLABLE"),
        ]
        ROWS = [
            ("Phred Phlyntstone", 32, _datetime_to_rfc3339(WHEN)),
            ("Bharney Rhubble", 33, WHEN + datetime.timedelta(seconds=1)),
            ("Wylma Phlyntstone", 29, WHEN + datetime.timedelta(seconds=2)),
            ("Bhettye Rhubble", 27, None),
        ]

        def _row_data(row):
            result = {"full_name": row[0], "age": str(row[1])}
            joined = row[2]
            if isinstance(joined, datetime.datetime):
                joined = joined.strftime(_RFC3339_MICROS)
            if joined is not None:
                result["joined"] = joined
            return result

        SENT = {
            "rows": [
                {"json": _row_data(row), "insertId": str(i)}
                for i, row in enumerate(ROWS)
            ]
        }

        with mock.patch("uuid.uuid4", side_effect=map(str, range(len(ROWS)))):
            # Test with using string IDs for the table.
            errors = client.insert_rows(
                "{}.{}".format(self.DS_ID, self.TABLE_ID), ROWS, selected_fields=schema
            )

        self.assertEqual(len(errors), 0)
        conn.api_request.assert_called_once()
        _, req = conn.api_request.call_args
        self.assertEqual(req["method"], "POST")
        self.assertEqual(req["path"], "/%s" % PATH)
        self.assertEqual(req["data"], SENT)
        self.assertEqual(req["timeout"], DEFAULT_TIMEOUT)

    def test_insert_rows_w_list_of_dictionaries(self):
        import datetime

        from google.cloud._helpers import _RFC3339_MICROS, UTC, _datetime_to_rfc3339
        from google.cloud.bigquery.schema import SchemaField
        from google.cloud.bigquery.table import Table

        WHEN_TS = 1437767599.006
        WHEN = datetime.datetime.fromtimestamp(WHEN_TS, UTC).replace(tzinfo=UTC)
        PATH = "projects/%s/datasets/%s/tables/%s/insertAll" % (
            self.PROJECT,
            self.DS_ID,
            self.TABLE_ID,
        )
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection({})
        schema = [
            SchemaField("full_name", "STRING", mode="REQUIRED"),
            SchemaField("age", "INTEGER", mode="REQUIRED"),
            SchemaField("joined", "TIMESTAMP", mode="NULLABLE"),
        ]
        table = Table(self.TABLE_REF, schema=schema)
        ROWS = [
            {
                "full_name": "Phred Phlyntstone",
                "age": 32,
                "joined": _datetime_to_rfc3339(WHEN),
            },
            {
                "full_name": "Bharney Rhubble",
                "age": 33,
                "joined": WHEN + datetime.timedelta(seconds=1),
            },
            {
                "full_name": "Wylma Phlyntstone",
                "age": 29,
                "joined": WHEN + datetime.timedelta(seconds=2),
            },
            {"full_name": "Bhettye Rhubble", "age": 27, "joined": None},
        ]

        def _row_data(row):
            joined = row["joined"]
            if joined is None:
                row = copy.deepcopy(row)
                del row["joined"]
            elif isinstance(joined, datetime.datetime):
                row["joined"] = joined.strftime(_RFC3339_MICROS)
            row["age"] = str(row["age"])
            return row

        SENT = {
            "rows": [
                {"json": _row_data(row), "insertId": str(i)}
                for i, row in enumerate(ROWS)
            ]
        }

        with mock.patch("uuid.uuid4", side_effect=map(str, range(len(ROWS)))):
            errors = client.insert_rows(table, ROWS)

        self.assertEqual(len(errors), 0)
        conn.api_request.assert_called_once_with(
            method="POST", path="/%s" % PATH, data=SENT, timeout=DEFAULT_TIMEOUT
        )

    def test_insert_rows_w_list_of_Rows(self):
        from google.cloud.bigquery.schema import SchemaField
        from google.cloud.bigquery.table import Row, Table

        PATH = "projects/%s/datasets/%s/tables/%s/insertAll" % (
            self.PROJECT,
            self.DS_ID,
            self.TABLE_ID,
        )
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection({})
        schema = [
            SchemaField("full_name", "STRING", mode="REQUIRED"),
            SchemaField("age", "INTEGER", mode="REQUIRED"),
        ]
        table = Table(self.TABLE_REF, schema=schema)
        f2i = {"full_name": 0, "age": 1}
        ROWS = [
            Row(("Phred Phlyntstone", 32), f2i),
            Row(("Bharney Rhubble", 33), f2i),
            Row(("Wylma Phlyntstone", 29), f2i),
            Row(("Bhettye Rhubble", 27), f2i),
        ]

        def _row_data(row):
            return {"full_name": row[0], "age": str(row[1])}

        SENT = {
            "rows": [
                {"json": _row_data(row), "insertId": str(i)}
                for i, row in enumerate(ROWS)
            ]
        }

        with mock.patch("uuid.uuid4", side_effect=map(str, range(len(ROWS)))):
            errors = client.insert_rows(table, ROWS)

        self.assertEqual(len(errors), 0)
        conn.api_request.assert_called_once_with(
            method="POST", path="/%s" % PATH, data=SENT, timeout=DEFAULT_TIMEOUT
        )

    def test_insert_rows_w_skip_invalid_and_ignore_unknown(self):
        from google.cloud.bigquery.schema import SchemaField
        from google.cloud.bigquery.table import Table

        PATH = "projects/%s/datasets/%s/tables/%s/insertAll" % (
            self.PROJECT,
            self.DS_ID,
            self.TABLE_ID,
        )
        RESPONSE = {
            "insertErrors": [
                {
                    "index": 1,
                    "errors": [
                        {
                            "reason": "REASON",
                            "location": "LOCATION",
                            "debugInfo": "INFO",
                            "message": "MESSAGE",
                        }
                    ],
                }
            ]
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(RESPONSE)
        schema = [
            SchemaField("full_name", "STRING", mode="REQUIRED"),
            SchemaField("age", "INTEGER", mode="REQUIRED"),
            SchemaField("voter", "BOOLEAN", mode="NULLABLE"),
        ]
        table = Table(self.TABLE_REF, schema=schema)
        ROWS = [
            ("Phred Phlyntstone", 32, True),
            ("Bharney Rhubble", 33, False),
            ("Wylma Phlyntstone", 29, True),
            ("Bhettye Rhubble", 27, True),
        ]

        def _row_data(row):
            return {
                "full_name": row[0],
                "age": str(row[1]),
                "voter": row[2] and "true" or "false",
            }

        SENT = {
            "skipInvalidRows": True,
            "ignoreUnknownValues": True,
            "templateSuffix": "20160303",
            "rows": [
                {"insertId": index, "json": _row_data(row)}
                for index, row in enumerate(ROWS)
            ],
        }

        errors = client.insert_rows(
            table,
            ROWS,
            row_ids=[index for index, _ in enumerate(ROWS)],
            skip_invalid_rows=True,
            ignore_unknown_values=True,
            template_suffix="20160303",
        )

        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0]["index"], 1)
        self.assertEqual(len(errors[0]["errors"]), 1)
        self.assertEqual(
            errors[0]["errors"][0], RESPONSE["insertErrors"][0]["errors"][0]
        )
        conn.api_request.assert_called_once_with(
            method="POST", path="/%s" % PATH, data=SENT, timeout=DEFAULT_TIMEOUT
        )

    def test_insert_rows_w_repeated_fields(self):
        from google.cloud._helpers import UTC
        from google.cloud.bigquery.schema import SchemaField
        from google.cloud.bigquery.table import Table

        PATH = "projects/%s/datasets/%s/tables/%s/insertAll" % (
            self.PROJECT,
            self.DS_ID,
            self.TABLE_ID,
        )
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection({})
        color = SchemaField("color", "STRING", mode="REPEATED")
        items = SchemaField("items", "INTEGER", mode="REPEATED")
        score = SchemaField("score", "INTEGER")
        times = SchemaField("times", "TIMESTAMP", mode="REPEATED")
        distances = SchemaField("distances", "FLOAT", mode="REPEATED")
        structs = SchemaField(
            "structs", "RECORD", mode="REPEATED", fields=[score, times, distances]
        )
        table = Table(self.TABLE_REF, schema=[color, items, structs])
        ROWS = [
            (
                ["red", "green"],
                [1, 2],
                [
                    (
                        12,
                        [
                            datetime.datetime(2018, 12, 1, 12, 0, 0, tzinfo=UTC),
                            datetime.datetime(2018, 12, 1, 13, 0, 0, tzinfo=UTC),
                        ],
                        [1.25, 2.5],
                    ),
                    {
                        "score": 13,
                        "times": [
                            datetime.datetime(
                                2018, 12, 2, 12, 0, 0, tzinfo=datetime.timezone.utc
                            ),
                            datetime.datetime(
                                2018, 12, 2, 13, 0, 0, tzinfo=datetime.timezone.utc
                            ),
                        ],
                        "distances": [-1.25, -2.5],
                    },
                ],
            ),
            {"color": None, "items": [], "structs": [(None, [], [3.5])]},
        ]

        SENT = {
            "rows": [
                {
                    "json": {
                        "color": ["red", "green"],
                        "items": ["1", "2"],
                        "structs": [
                            {
                                "score": "12",
                                "times": [
                                    "2018-12-01T12:00:00.000000Z",
                                    "2018-12-01T13:00:00.000000Z",
                                ],
                                "distances": [1.25, 2.5],
                            },
                            {
                                "score": "13",
                                "times": [
                                    "2018-12-02T12:00:00.000000Z",
                                    "2018-12-02T13:00:00.000000Z",
                                ],
                                "distances": [-1.25, -2.5],
                            },
                        ],
                    },
                    "insertId": "0",
                },
                {
                    "json": {
                        "items": [],
                        "structs": [{"times": [], "distances": [3.5]}],
                    },
                    "insertId": "1",
                },
            ]
        }

        with mock.patch("uuid.uuid4", side_effect=map(str, range(len(ROWS)))):
            errors = client.insert_rows(table, ROWS)

        self.assertEqual(len(errors), 0)
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/%s" % PATH,
            data=SENT,
            timeout=DEFAULT_TIMEOUT,
        )

    def test_insert_rows_w_record_schema(self):
        from google.cloud.bigquery.schema import SchemaField

        PATH = "projects/%s/datasets/%s/tables/%s/insertAll" % (
            self.PROJECT,
            self.DS_ID,
            self.TABLE_ID,
        )
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection({})
        full_name = SchemaField("full_name", "STRING", mode="REQUIRED")
        area_code = SchemaField("area_code", "STRING", "REQUIRED")
        local_number = SchemaField("local_number", "STRING", "REQUIRED")
        rank = SchemaField("rank", "INTEGER", "REQUIRED")
        phone = SchemaField(
            "phone", "RECORD", mode="NULLABLE", fields=[area_code, local_number, rank]
        )
        ROWS = [
            (
                "Phred Phlyntstone",
                {"area_code": "800", "local_number": "555-1212", "rank": 1},
            ),
            ("Bharney Rhubble", ("877", "768-5309", 2)),
            ("Wylma Phlyntstone", None),
        ]

        SENT = {
            "rows": [
                {
                    "json": {
                        "full_name": "Phred Phlyntstone",
                        "phone": {
                            "area_code": "800",
                            "local_number": "555-1212",
                            "rank": "1",
                        },
                    },
                    "insertId": "0",
                },
                {
                    "json": {
                        "full_name": "Bharney Rhubble",
                        "phone": {
                            "area_code": "877",
                            "local_number": "768-5309",
                            "rank": "2",
                        },
                    },
                    "insertId": "1",
                },
                {"json": {"full_name": "Wylma Phlyntstone"}, "insertId": "2"},
            ]
        }

        with mock.patch("uuid.uuid4", side_effect=map(str, range(len(ROWS)))):
            errors = client.insert_rows(
                self.TABLE_REF, ROWS, selected_fields=[full_name, phone]
            )

        self.assertEqual(len(errors), 0)
        conn.api_request.assert_called_once_with(
            method="POST", path="/%s" % PATH, data=SENT, timeout=DEFAULT_TIMEOUT
        )

    def test_insert_rows_w_explicit_none_insert_ids(self):
        from google.cloud.bigquery.schema import SchemaField
        from google.cloud.bigquery.table import Table

        PATH = "projects/{}/datasets/{}/tables/{}/insertAll".format(
            self.PROJECT,
            self.DS_ID,
            self.TABLE_ID,
        )
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection({})
        schema = [
            SchemaField("full_name", "STRING", mode="REQUIRED"),
            SchemaField("age", "INTEGER", mode="REQUIRED"),
        ]
        table = Table(self.TABLE_REF, schema=schema)
        ROWS = [
            {"full_name": "Phred Phlyntstone", "age": 32},
            {"full_name": "Bharney Rhubble", "age": 33},
        ]

        def _row_data(row):
            row["age"] = str(row["age"])
            return row

        SENT = {"rows": [{"json": _row_data(row), "insertId": None} for row in ROWS]}

        errors = client.insert_rows(table, ROWS, row_ids=[None] * len(ROWS))

        self.assertEqual(len(errors), 0)
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/{}".format(PATH),
            data=SENT,
            timeout=DEFAULT_TIMEOUT,
        )

    def test_insert_rows_errors(self):
        from google.cloud.bigquery.schema import SchemaField
        from google.cloud.bigquery.table import Table

        ROWS = [
            ("Phred Phlyntstone", 32, True),
            ("Bharney Rhubble", 33, False),
            ("Wylma Phlyntstone", 29, True),
            ("Bhettye Rhubble", 27, True),
        ]
        creds = _make_credentials()
        http = object()

        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)

        # table ref with no selected fields
        with self.assertRaises(ValueError):
            client.insert_rows(self.TABLE_REF, ROWS)

        # table with no schema
        with self.assertRaises(ValueError):
            client.insert_rows(Table(self.TABLE_REF), ROWS)

        # neither Table nor TableReference
        with self.assertRaises(TypeError):
            client.insert_rows(1, ROWS)

        schema = [
            SchemaField("full_name", "STRING", mode="REQUIRED"),
        ]
        table = Table(self.TABLE_REF, schema=schema)

        # rows is just a dict
        with self.assertRaises(TypeError):
            client.insert_rows(table, {"full_name": "value"})

    def test_insert_rows_w_numeric(self):
        from google.cloud.bigquery import table
        from google.cloud.bigquery.schema import SchemaField

        project = "PROJECT"
        ds_id = "DS_ID"
        table_id = "TABLE_ID"
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=project, credentials=creds, _http=http)
        table_ref = DatasetReference(project, ds_id).table(table_id)
        rows = [
            ("Savings", decimal.Decimal("23.47")),
            ("Checking", decimal.Decimal("1.98")),
            ("Mortgage", decimal.Decimal("-12345678909.87654321")),
        ]
        schemas = [
            [SchemaField("account", "STRING"), SchemaField("balance", "NUMERIC")],
            [SchemaField("account", "STRING"), SchemaField("balance", "BIGNUMERIC")],
        ]

        for schema in schemas:
            conn = client._connection = make_connection({})

            insert_table = table.Table(table_ref, schema=schema)
            with mock.patch("uuid.uuid4", side_effect=map(str, range(len(rows)))):
                errors = client.insert_rows(insert_table, rows)

            self.assertEqual(len(errors), 0)
            rows_json = [
                {"account": "Savings", "balance": "23.47"},
                {"account": "Checking", "balance": "1.98"},
                {"account": "Mortgage", "balance": "-12345678909.87654321"},
            ]
            sent = {
                "rows": [
                    {"json": row, "insertId": str(i)} for i, row in enumerate(rows_json)
                ]
            }
            conn.api_request.assert_called_once_with(
                method="POST",
                path="/projects/{}/datasets/{}/tables/{}/insertAll".format(
                    project, ds_id, table_id
                ),
                data=sent,
                timeout=DEFAULT_TIMEOUT,
            )

    def test_insert_rows_from_dataframe(self):
        pandas = pytest.importorskip("pandas")
        from google.cloud.bigquery.schema import SchemaField
        from google.cloud.bigquery.table import Table

        API_PATH = "/projects/{}/datasets/{}/tables/{}/insertAll".format(
            self.PROJECT, self.DS_ID, self.TABLE_REF.table_id
        )

        data = [
            {
                "name": "Little One",
                "age": 10,
                "adult": False,
                "bdate": datetime.date(2011, 1, 2),
                "btime": datetime.time(19, 1, 10),
            },
            {
                "name": "Young Gun",
                "age": 20,
                "adult": True,
                "bdate": datetime.date(2001, 1, 2),
                "btime": datetime.time(19, 1, 20),
            },
            {
                "name": "Dad",
                "age": 30,
                "adult": True,
                "bdate": datetime.date(1991, 1, 2),
                "btime": datetime.time(19, 1, 30),
            },
            {
                "name": "Stranger",
                "age": 40,
                "adult": True,
                "bdate": datetime.date(1981, 1, 2),
                "btime": datetime.time(19, 1, 40),
            },
        ]
        dataframe = pandas.DataFrame(data)
        dataframe["bdate"] = dataframe["bdate"].astype("dbdate")
        dataframe["btime"] = dataframe["btime"].astype("dbtime")

        # create client
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection({}, {})

        # create table
        schema = [
            SchemaField("name", "STRING", mode="REQUIRED"),
            SchemaField("age", "INTEGER", mode="REQUIRED"),
            SchemaField("adult", "BOOLEAN", mode="REQUIRED"),
            SchemaField("bdata", "DATE", mode="REQUIRED"),
            SchemaField("btime", "TIME", mode="REQUIRED"),
        ]
        table = Table(self.TABLE_REF, schema=schema)

        with mock.patch("uuid.uuid4", side_effect=map(str, range(len(dataframe)))):
            error_info = client.insert_rows_from_dataframe(
                table, dataframe, chunk_size=3, timeout=7.5
            )

        self.assertEqual(len(error_info), 2)
        for chunk_errors in error_info:
            assert chunk_errors == []

        for row in data:
            row["age"] = str(row["age"])
            row["adult"] = str(row["adult"]).lower()
            row["bdate"] = row["bdate"].isoformat()
            row["btime"] = row["btime"].isoformat()

        rows = [dict(insertId=str(i), json=row) for i, row in enumerate(data)]
        EXPECTED_SENT_DATA = [dict(rows=rows[:3]), dict(rows=rows[3:])]

        actual_calls = conn.api_request.call_args_list

        for call, expected_data in itertools.zip_longest(
            actual_calls, EXPECTED_SENT_DATA
        ):
            expected_call = mock.call(
                method="POST", path=API_PATH, data=expected_data, timeout=7.5
            )
            assert call == expected_call

    def test_insert_rows_from_dataframe_nan(self):
        pandas = pytest.importorskip("pandas")
        from google.cloud.bigquery.schema import SchemaField
        from google.cloud.bigquery.table import Table

        API_PATH = "/projects/{}/datasets/{}/tables/{}/insertAll".format(
            self.PROJECT, self.DS_ID, self.TABLE_REF.table_id
        )

        dataframe = pandas.DataFrame(
            {
                "str_col": ["abc", "def", float("NaN"), "jkl"],
                "int_col": [1, float("NaN"), 3, 4],
                "float_col": [float("NaN"), 0.25, 0.5, 0.125],
            }
        )

        # create client
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection({}, {})

        # create table
        schema = [
            SchemaField("str_col", "STRING"),
            SchemaField("int_col", "INTEGER"),
            SchemaField("float_col", "FLOAT"),
        ]
        table = Table(self.TABLE_REF, schema=schema)

        with mock.patch("uuid.uuid4", side_effect=map(str, range(len(dataframe)))):
            error_info = client.insert_rows_from_dataframe(
                table, dataframe, chunk_size=3, timeout=7.5
            )

        self.assertEqual(len(error_info), 2)
        for chunk_errors in error_info:
            assert chunk_errors == []

        EXPECTED_SENT_DATA = [
            {
                "rows": [
                    {"insertId": "0", "json": {"str_col": "abc", "int_col": 1}},
                    {"insertId": "1", "json": {"str_col": "def", "float_col": 0.25}},
                    {"insertId": "2", "json": {"int_col": 3, "float_col": 0.5}},
                ]
            },
            {
                "rows": [
                    {
                        "insertId": "3",
                        "json": {"str_col": "jkl", "int_col": 4, "float_col": 0.125},
                    }
                ]
            },
        ]

        actual_calls = conn.api_request.call_args_list

        for call, expected_data in itertools.zip_longest(
            actual_calls, EXPECTED_SENT_DATA
        ):
            expected_call = mock.call(
                method="POST", path=API_PATH, data=expected_data, timeout=7.5
            )
            assert call == expected_call

    def test_insert_rows_from_dataframe_many_columns(self):
        pandas = pytest.importorskip("pandas")
        from google.cloud.bigquery.schema import SchemaField
        from google.cloud.bigquery.table import Table

        API_PATH = "/projects/{}/datasets/{}/tables/{}/insertAll".format(
            self.PROJECT, self.DS_ID, self.TABLE_REF.table_id
        )
        N_COLUMNS = 256  # should be >= 256

        dataframe = pandas.DataFrame(
            [{"foo_{}".format(i): "bar_{}".format(i) for i in range(N_COLUMNS)}]
        )

        # create client
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection({}, {})

        # create table
        schema = [SchemaField("foo_{}".format(i), "STRING") for i in range(N_COLUMNS)]
        table = Table(self.TABLE_REF, schema=schema)

        with mock.patch("uuid.uuid4", side_effect=map(str, range(len(dataframe)))):
            error_info = client.insert_rows_from_dataframe(
                table, dataframe, chunk_size=3
            )

        assert len(error_info) == 1
        assert error_info[0] == []

        EXPECTED_SENT_DATA = {
            "rows": [
                {
                    "insertId": "0",
                    "json": {
                        "foo_{}".format(i): "bar_{}".format(i) for i in range(N_COLUMNS)
                    },
                }
            ]
        }
        expected_call = mock.call(
            method="POST",
            path=API_PATH,
            data=EXPECTED_SENT_DATA,
            timeout=DEFAULT_TIMEOUT,
        )

        actual_calls = conn.api_request.call_args_list
        assert len(actual_calls) == 1
        assert actual_calls[0] == expected_call

    def test_insert_rows_from_dataframe_w_explicit_none_insert_ids(self):
        pandas = pytest.importorskip("pandas")
        from google.cloud.bigquery.schema import SchemaField
        from google.cloud.bigquery.table import Table

        API_PATH = "/projects/{}/datasets/{}/tables/{}/insertAll".format(
            self.PROJECT, self.DS_ID, self.TABLE_REF.table_id
        )

        dataframe = pandas.DataFrame(
            [
                {"name": "Little One", "adult": False},
                {"name": "Young Gun", "adult": True},
            ]
        )

        # create client
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection({}, {})

        # create table
        schema = [
            SchemaField("name", "STRING", mode="REQUIRED"),
            SchemaField("adult", "BOOLEAN", mode="REQUIRED"),
        ]
        table = Table(self.TABLE_REF, schema=schema)

        error_info = client.insert_rows_from_dataframe(
            table, dataframe, row_ids=[None] * len(dataframe)
        )

        self.assertEqual(len(error_info), 1)
        assert error_info[0] == []  # no chunk errors

        EXPECTED_SENT_DATA = {
            "rows": [
                {"insertId": None, "json": {"name": "Little One", "adult": "false"}},
                {"insertId": None, "json": {"name": "Young Gun", "adult": "true"}},
            ]
        }

        actual_calls = conn.api_request.call_args_list
        assert len(actual_calls) == 1
        assert actual_calls[0] == mock.call(
            method="POST",
            path=API_PATH,
            data=EXPECTED_SENT_DATA,
            timeout=DEFAULT_TIMEOUT,
        )

    def test_insert_rows_from_dataframe_emits_pending_deprecation_warning(self):
        pandas = pytest.importorskip("pandas")
        from google.cloud.bigquery.schema import SchemaField
        from google.cloud.bigquery.table import Table

        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        client._connection = make_connection({}, {})

        schema = [SchemaField("name", "STRING", mode="REQUIRED")]
        table = Table(self.TABLE_REF, schema=schema)
        dataframe = pandas.DataFrame([{"name": "Alice"}])

        with pytest.warns(
            PendingDeprecationWarning,
            match="Inserting rows from DataFrames via google-cloud-bigquery is deprecated",
        ):
            client.insert_rows_from_dataframe(table, dataframe)

    def test_insert_rows_json_default_behavior(self):
        from google.cloud.bigquery.dataset import DatasetReference
        from google.cloud.bigquery.schema import SchemaField
        from google.cloud.bigquery.table import Table

        PROJECT = "PROJECT"
        DS_ID = "DS_ID"
        TABLE_ID = "TABLE_ID"
        PATH = "projects/%s/datasets/%s/tables/%s/insertAll" % (
            PROJECT,
            DS_ID,
            TABLE_ID,
        )
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection({})
        table_ref = DatasetReference(PROJECT, DS_ID).table(TABLE_ID)
        schema = [
            SchemaField("full_name", "STRING", mode="REQUIRED"),
            SchemaField("age", "INTEGER", mode="REQUIRED"),
            SchemaField("joined", "TIMESTAMP", mode="NULLABLE"),
        ]
        table = Table(table_ref, schema=schema)
        ROWS = [
            {
                "full_name": "Phred Phlyntstone",
                "age": "32",
                "joined": "2015-07-24T19:53:19.006000Z",
            },
            {"full_name": "Bharney Rhubble", "age": "33", "joined": 1437767600.006},
            {"full_name": "Wylma Phlyntstone", "age": "29", "joined": 1437767601.006},
            {"full_name": "Bhettye Rhubble", "age": "27", "joined": None},
        ]

        SENT = {
            "rows": [{"json": row, "insertId": str(i)} for i, row in enumerate(ROWS)]
        }

        with mock.patch("uuid.uuid4", side_effect=map(str, range(len(ROWS)))):
            errors = client.insert_rows_json(table, ROWS, timeout=7.5)

        self.assertEqual(len(errors), 0)
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/%s" % PATH,
            data=SENT,
            timeout=7.5,
        )

    def test_insert_rows_json_w_explicitly_requested_autogenerated_insert_ids(self):
        from google.cloud.bigquery import AutoRowIDs

        rows = [{"col1": "val1"}, {"col2": "val2"}]
        creds = _make_credentials()
        http = object()
        client = self._make_one(
            project="default-project", credentials=creds, _http=http
        )
        conn = client._connection = make_connection({})

        uuid_patcher = mock.patch("uuid.uuid4", side_effect=map(str, range(len(rows))))
        with uuid_patcher:
            errors = client.insert_rows_json(
                "proj.dset.tbl", rows, row_ids=AutoRowIDs.GENERATE_UUID
            )

        self.assertEqual(len(errors), 0)

        # Check row data sent to the backend.
        expected_row_data = {
            "rows": [
                {"json": {"col1": "val1"}, "insertId": "0"},
                {"json": {"col2": "val2"}, "insertId": "1"},
            ]
        }
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/proj/datasets/dset/tables/tbl/insertAll",
            data=expected_row_data,
            timeout=DEFAULT_TIMEOUT,
        )

    def test_insert_rows_json_w_explicitly_disabled_insert_ids(self):
        from google.cloud.bigquery import AutoRowIDs

        rows = [{"col1": "val1"}, {"col2": "val2"}]
        creds = _make_credentials()
        http = object()
        client = self._make_one(
            project="default-project", credentials=creds, _http=http
        )
        conn = client._connection = make_connection({})

        errors = client.insert_rows_json(
            "proj.dset.tbl",
            rows,
            row_ids=AutoRowIDs.DISABLED,
        )

        self.assertEqual(len(errors), 0)

        expected_row_data = {
            "rows": [
                {"json": {"col1": "val1"}, "insertId": None},
                {"json": {"col2": "val2"}, "insertId": None},
            ]
        }
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/proj/datasets/dset/tables/tbl/insertAll",
            data=expected_row_data,
            timeout=DEFAULT_TIMEOUT,
        )

    def test_insert_rows_json_with_iterator_row_ids(self):
        rows = [{"col1": "val1"}, {"col2": "val2"}, {"col3": "val3"}]
        creds = _make_credentials()
        http = object()
        client = self._make_one(
            project="default-project", credentials=creds, _http=http
        )
        conn = client._connection = make_connection({})

        row_ids_iter = map(str, itertools.count(42))
        errors = client.insert_rows_json("proj.dset.tbl", rows, row_ids=row_ids_iter)

        self.assertEqual(len(errors), 0)
        expected_row_data = {
            "rows": [
                {"json": {"col1": "val1"}, "insertId": "42"},
                {"json": {"col2": "val2"}, "insertId": "43"},
                {"json": {"col3": "val3"}, "insertId": "44"},
            ]
        }
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/proj/datasets/dset/tables/tbl/insertAll",
            data=expected_row_data,
            timeout=DEFAULT_TIMEOUT,
        )

    def test_insert_rows_json_with_non_iterable_row_ids(self):
        rows = [{"col1": "val1"}]
        creds = _make_credentials()
        http = object()
        client = self._make_one(
            project="default-project", credentials=creds, _http=http
        )
        client._connection = make_connection({})

        with self.assertRaises(TypeError) as exc:
            client.insert_rows_json("proj.dset.tbl", rows, row_ids=object())

        err_msg = str(exc.exception)
        self.assertIn("row_ids", err_msg)
        self.assertIn("iterable", err_msg)

    def test_insert_rows_json_with_too_few_row_ids(self):
        rows = [{"col1": "val1"}, {"col2": "val2"}, {"col3": "val3"}]
        creds = _make_credentials()
        http = object()
        client = self._make_one(
            project="default-project", credentials=creds, _http=http
        )
        client._connection = make_connection({})

        insert_ids = ["10", "20"]

        error_msg_pattern = "row_ids did not generate enough IDs.*index 2"
        with self.assertRaisesRegex(ValueError, error_msg_pattern):
            client.insert_rows_json("proj.dset.tbl", rows, row_ids=insert_ids)

    def test_insert_rows_json_w_explicit_none_insert_ids(self):
        rows = [{"col1": "val1"}, {"col2": "val2"}]
        creds = _make_credentials()
        http = object()
        client = self._make_one(
            project="default-project", credentials=creds, _http=http
        )
        conn = client._connection = make_connection({})

        errors = client.insert_rows_json(
            "proj.dset.tbl",
            rows,
            row_ids=[None] * len(rows),
        )

        self.assertEqual(len(errors), 0)
        expected = {"rows": [{"json": row, "insertId": None} for row in rows]}
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/proj/datasets/dset/tables/tbl/insertAll",
            data=expected,
            timeout=DEFAULT_TIMEOUT,
        )

    def test_insert_rows_json_w_none_insert_ids_sequence(self):
        rows = [{"col1": "val1"}, {"col2": "val2"}]
        creds = _make_credentials()
        http = object()
        client = self._make_one(
            project="default-project", credentials=creds, _http=http
        )
        conn = client._connection = make_connection({})

        uuid_patcher = mock.patch("uuid.uuid4", side_effect=map(str, range(len(rows))))
        with warnings.catch_warnings(record=True) as warned, uuid_patcher:
            errors = client.insert_rows_json("proj.dset.tbl", rows, row_ids=None)

        self.assertEqual(len(errors), 0)

        # Passing row_ids=None should have resulted in a deprecation warning.
        matches = [
            warning
            for warning in warned
            if issubclass(warning.category, DeprecationWarning)
            and "row_ids" in str(warning)
            and "AutoRowIDs.GENERATE_UUID" in str(warning)
        ]
        assert matches, "The expected deprecation warning was not raised."

        # Check row data sent to the backend.
        expected_row_data = {
            "rows": [
                {"json": {"col1": "val1"}, "insertId": "0"},
                {"json": {"col2": "val2"}, "insertId": "1"},
            ]
        }
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/proj/datasets/dset/tables/tbl/insertAll",
            data=expected_row_data,
            timeout=DEFAULT_TIMEOUT,
        )

    def test_insert_rows_w_wrong_arg(self):
        from google.cloud.bigquery.dataset import DatasetReference
        from google.cloud.bigquery.schema import SchemaField
        from google.cloud.bigquery.table import Table

        PROJECT = "PROJECT"
        DS_ID = "DS_ID"
        TABLE_ID = "TABLE_ID"
        ROW = {"full_name": "Bhettye Rhubble", "age": "27", "joined": None}

        creds = _make_credentials()
        client = self._make_one(project=PROJECT, credentials=creds, _http=object())
        client._connection = make_connection({})

        table_ref = DatasetReference(PROJECT, DS_ID).table(TABLE_ID)
        schema = [
            SchemaField("full_name", "STRING", mode="REQUIRED"),
            SchemaField("age", "INTEGER", mode="REQUIRED"),
            SchemaField("joined", "TIMESTAMP", mode="NULLABLE"),
        ]
        table = Table(table_ref, schema=schema)

        with self.assertRaises(TypeError):
            client.insert_rows_json(table, ROW)

    def test_insert_rows_json_w_ssl_error(self):
        import requests.exceptions
        from google.cloud.bigquery.dataset import DatasetReference
        from google.cloud.bigquery.schema import SchemaField
        from google.cloud.bigquery.table import Table

        PROJECT = "PROJECT"
        DS_ID = "DS_ID"
        TABLE_ID = "TABLE_ID"
        ROWS = [{"full_name": "Bhettye Rhubble", "age": "27", "joined": None}]

        creds = _make_credentials()
        client = self._make_one(project=PROJECT, credentials=creds, _http=object())
        conn = client._connection = make_connection({})

        # Make the connection raise an SSLError
        conn.api_request.side_effect = requests.exceptions.SSLError("EOF occurred")

        table_ref = DatasetReference(PROJECT, DS_ID).table(TABLE_ID)
        schema = [
            SchemaField("full_name", "STRING", mode="REQUIRED"),
            SchemaField("age", "INTEGER", mode="REQUIRED"),
            SchemaField("joined", "TIMESTAMP", mode="NULLABLE"),
        ]
        table = Table(table_ref, schema=schema)

        with self.assertRaises(requests.exceptions.SSLError) as context:
            client.insert_rows_json(table, ROWS)

        self.assertIn("invalid table schema", str(context.exception))
        self.assertIn("SSL/Connection error occurred", str(context.exception))

    def test_list_partitions(self):
        from google.cloud.bigquery.table import Table

        rows = 3
        meta_info = _make_list_partitons_meta_info(
            self.PROJECT, self.DS_ID, self.TABLE_ID, rows
        )

        data = {
            "totalRows": str(rows),
            "rows": [
                {"f": [{"v": "20180101"}]},
                {"f": [{"v": "20180102"}]},
                {"f": [{"v": "20180103"}]},
            ],
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        client._connection = make_connection(meta_info, data)
        table = Table(self.TABLE_REF)

        partition_list = client.list_partitions(table)
        self.assertEqual(len(partition_list), rows)
        self.assertIn("20180102", partition_list)

    def test_list_partitions_with_string_id(self):
        meta_info = _make_list_partitons_meta_info(
            self.PROJECT, self.DS_ID, self.TABLE_ID, 0
        )

        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        client._connection = make_connection(meta_info, {})

        partition_list = client.list_partitions(
            "{}.{}".format(self.DS_ID, self.TABLE_ID)
        )

        self.assertEqual(len(partition_list), 0)

    def test_list_rows(self):
        import datetime

        from google.cloud._helpers import UTC
        from google.cloud.bigquery.schema import SchemaField
        from google.cloud.bigquery.table import Row, Table

        PATH = "projects/%s/datasets/%s/tables/%s/data" % (
            self.PROJECT,
            self.DS_ID,
            self.TABLE_ID,
        )
        WHEN_TS = 1437767599006000

        WHEN = datetime.datetime.fromtimestamp(
            WHEN_TS / 1e6, datetime.timezone.utc
        ).replace(tzinfo=UTC)
        WHEN_1 = WHEN + datetime.timedelta(microseconds=1)
        WHEN_2 = WHEN + datetime.timedelta(microseconds=2)
        ROWS = 1234
        TOKEN = "TOKEN"

        DATA = {
            "totalRows": str(ROWS),
            "pageToken": TOKEN,
            "rows": [
                {"f": [{"v": "Phred Phlyntstone"}, {"v": "32"}, {"v": WHEN_TS}]},
                {"f": [{"v": "Bharney Rhubble"}, {"v": "33"}, {"v": WHEN_TS + 1}]},
                {"f": [{"v": "Wylma Phlyntstone"}, {"v": "29"}, {"v": WHEN_TS + 2}]},
                {"f": [{"v": "Bhettye Rhubble"}, {"v": None}, {"v": None}]},
            ],
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(DATA, DATA)
        full_name = SchemaField("full_name", "STRING", mode="REQUIRED")
        age = SchemaField("age", "INTEGER", mode="NULLABLE")
        joined = SchemaField("joined", "TIMESTAMP", mode="NULLABLE")
        table = Table(self.TABLE_REF, schema=[full_name, age, joined])
        table._properties["location"] = "us-central1"
        table._properties["numRows"] = 7

        iterator = client.list_rows(table, timeout=7.5)

        # Check that initial RowIterator is populated from the table metadata.
        self.assertIsNone(iterator.job_id)
        self.assertEqual(iterator.location, "us-central1")
        self.assertEqual(iterator.project, table.project)
        self.assertIsNone(iterator.query_id)
        self.assertEqual(iterator.total_rows, 7)
        page = next(iterator.pages)
        rows = list(page)

        # Check that total_rows is updated based on API response.
        self.assertEqual(iterator.total_rows, ROWS)

        f2i = {"full_name": 0, "age": 1, "joined": 2}
        self.assertEqual(len(rows), 4)
        self.assertEqual(rows[0], Row(("Phred Phlyntstone", 32, WHEN), f2i))
        self.assertEqual(rows[1], Row(("Bharney Rhubble", 33, WHEN_1), f2i))
        self.assertEqual(rows[2], Row(("Wylma Phlyntstone", 29, WHEN_2), f2i))
        self.assertEqual(rows[3], Row(("Bhettye Rhubble", None, None), f2i))
        self.assertEqual(iterator.next_page_token, TOKEN)

        conn.api_request.assert_called_once_with(
            method="GET",
            path="/%s" % PATH,
            query_params={"formatOptions.useInt64Timestamp": True},
            timeout=7.5,
        )

    def test_list_rows_pico_timestamp(self):
        from google.cloud.bigquery.schema import SchemaField
        from google.cloud.bigquery.table import Table

        PATH = "projects/%s/datasets/%s/tables/%s/data" % (
            self.PROJECT,
            self.DS_ID,
            self.TABLE_ID,
        )
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection({}, {})
        pico_col = SchemaField(
            "full_name",
            "TIMESTAMP",
            mode="REQUIRED",
            timestamp_precision=TimestampPrecision.PICOSECOND,
        )
        table = Table(self.TABLE_REF, schema=[pico_col])

        iterator = client.list_rows(
            table, timestamp_precision=TimestampPrecision.PICOSECOND
        )
        next(iterator.pages)

        conn.api_request.assert_called_once_with(
            method="GET",
            path="/%s" % PATH,
            query_params={"formatOptions.timestampOutputFormat": "ISO8601_STRING"},
            timeout=None,
        )

    def test_list_rows_w_start_index_w_page_size(self):
        from google.cloud.bigquery.schema import SchemaField
        from google.cloud.bigquery.table import Row, Table

        PATH = "projects/%s/datasets/%s/tables/%s/data" % (
            self.PROJECT,
            self.DS_ID,
            self.TABLE_ID,
        )

        page_1 = {
            "totalRows": 4,
            "pageToken": "some-page-token",
            "rows": [
                {"f": [{"v": "Phred Phlyntstone"}]},
                {"f": [{"v": "Bharney Rhubble"}]},
            ],
        }
        page_2 = {
            "totalRows": 4,
            "rows": [
                {"f": [{"v": "Wylma Phlyntstone"}]},
                {"f": [{"v": "Bhettye Rhubble"}]},
            ],
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(page_1, page_2)
        full_name = SchemaField("full_name", "STRING", mode="REQUIRED")
        table = Table(self.TABLE_REF, schema=[full_name])
        iterator = client.list_rows(table, max_results=4, page_size=2, start_index=1)
        pages = iterator.pages
        rows = list(next(pages))
        extra_params = iterator.extra_params
        f2i = {"full_name": 0}
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0], Row(("Phred Phlyntstone",), f2i))
        self.assertEqual(rows[1], Row(("Bharney Rhubble",), f2i))

        rows = list(next(pages))

        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0], Row(("Wylma Phlyntstone",), f2i))
        self.assertEqual(rows[1], Row(("Bhettye Rhubble",), f2i))
        self.assertEqual(
            extra_params, {"startIndex": 1, "formatOptions.useInt64Timestamp": True}
        )

        conn.api_request.assert_has_calls(
            [
                mock.call(
                    method="GET",
                    path="/%s" % PATH,
                    query_params={
                        "startIndex": 1,
                        "maxResults": 2,
                        "formatOptions.useInt64Timestamp": True,
                    },
                    timeout=DEFAULT_TIMEOUT,
                ),
                mock.call(
                    method="GET",
                    path="/%s" % PATH,
                    query_params={
                        "pageToken": "some-page-token",
                        "maxResults": 2,
                        "formatOptions.useInt64Timestamp": True,
                    },
                    timeout=DEFAULT_TIMEOUT,
                ),
            ]
        )

    def test_list_rows_empty_table(self):
        response = {"totalRows": "0", "rows": []}
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        client._connection = make_connection(response, response)

        # Table that has no schema because it's an empty table.
        rows = client.list_rows(
            # Test with using a string for the table ID.
            "{}.{}.{}".format(
                self.TABLE_REF.project,
                self.TABLE_REF.dataset_id,
                self.TABLE_REF.table_id,
            ),
            selected_fields=[],
        )

        self.assertIsNone(rows.job_id)
        self.assertIsNone(rows.location)
        self.assertEqual(rows.project, self.TABLE_REF.project)
        self.assertIsNone(rows.query_id)
        # When a table reference / string and selected_fields is provided,
        # total_rows can't be populated until iteration starts.
        self.assertIsNone(rows.total_rows)
        self.assertEqual(tuple(rows), ())
        self.assertEqual(rows.total_rows, 0)

    def test_list_rows_query_params(self):
        from google.cloud.bigquery.schema import SchemaField
        from google.cloud.bigquery.table import Table

        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        table = Table(
            self.TABLE_REF, schema=[SchemaField("age", "INTEGER", mode="NULLABLE")]
        )
        tests = [
            ({}, {}),
            ({"start_index": 1}, {"startIndex": 1}),
            ({"max_results": 2}, {"maxResults": 2}),
            ({"start_index": 1, "max_results": 2}, {"startIndex": 1, "maxResults": 2}),
        ]
        conn = client._connection = make_connection(*len(tests) * [{}])
        for i, test in enumerate(tests):
            iterator = client.list_rows(table, **test[0])
            next(iterator.pages)
            req = conn.api_request.call_args_list[i]
            test[1]["formatOptions.useInt64Timestamp"] = True
            self.assertEqual(req[1]["query_params"], test[1], "for kwargs %s" % test[0])

    def test_list_rows_w_numeric(self):
        from google.cloud.bigquery.schema import SchemaField
        from google.cloud.bigquery.table import Table

        resource = {
            "totalRows": 3,
            "rows": [
                {"f": [{"v": "-1.23456789"}, {"v": "-123456789.987654321"}]},
                {"f": [{"v": None}, {"v": "3.141592653589793238462643383279502884"}]},
                {"f": [{"v": "2718281828459045235360287471.352662497"}, {"v": None}]},
            ],
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        client._connection = make_connection(resource)
        schema = [
            SchemaField("num", "NUMERIC"),
            SchemaField("bignum", "BIGNUMERIC"),
        ]
        table = Table(self.TABLE_REF, schema=schema)

        iterator = client.list_rows(table)
        rows = list(iterator)

        self.assertEqual(len(rows), 3)
        self.assertEqual(rows[0]["num"], decimal.Decimal("-1.23456789"))
        self.assertEqual(rows[0]["bignum"], decimal.Decimal("-123456789.987654321"))
        self.assertIsNone(rows[1]["num"])
        self.assertEqual(
            rows[1]["bignum"], decimal.Decimal("3.141592653589793238462643383279502884")
        )
        self.assertEqual(
            rows[2]["num"], decimal.Decimal("2718281828459045235360287471.352662497")
        )
        self.assertIsNone(rows[2]["bignum"])

    def test_list_rows_repeated_fields(self):
        from google.cloud.bigquery.schema import SchemaField

        PATH = "projects/%s/datasets/%s/tables/%s/data" % (
            self.PROJECT,
            self.DS_ID,
            self.TABLE_ID,
        )
        ROWS = 1234
        TOKEN = "TOKEN"
        DATA = {
            "totalRows": ROWS,
            "pageToken": TOKEN,
            "rows": [
                {
                    "f": [
                        {"v": [{"v": "red"}, {"v": "green"}]},
                        {
                            "v": [
                                {
                                    "v": {
                                        "f": [
                                            {"v": [{"v": "1"}, {"v": "2"}]},
                                            {"v": [{"v": "3.1415"}, {"v": "1.414"}]},
                                        ]
                                    }
                                }
                            ]
                        },
                    ]
                }
            ],
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(DATA)
        color = SchemaField("color", "STRING", mode="REPEATED")
        index = SchemaField("index", "INTEGER", "REPEATED")
        score = SchemaField("score", "FLOAT", "REPEATED")
        struct = SchemaField("struct", "RECORD", mode="REPEATED", fields=[index, score])

        iterator = client.list_rows(self.TABLE_REF, selected_fields=[color, struct])
        page = next(iterator.pages)
        rows = list(page)
        total_rows = iterator.total_rows
        page_token = iterator.next_page_token

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], ["red", "green"])
        self.assertEqual(rows[0][1], [{"index": [1, 2], "score": [3.1415, 1.414]}])
        self.assertEqual(total_rows, ROWS)
        self.assertEqual(page_token, TOKEN)

        conn.api_request.assert_called_once_with(
            method="GET",
            path="/%s" % PATH,
            query_params={
                "selectedFields": "color,struct",
                "formatOptions.useInt64Timestamp": True,
            },
            timeout=DEFAULT_TIMEOUT,
        )

    def test_list_rows_w_record_schema(self):
        from google.cloud.bigquery.schema import SchemaField
        from google.cloud.bigquery.table import Table

        PATH = "projects/%s/datasets/%s/tables/%s/data" % (
            self.PROJECT,
            self.DS_ID,
            self.TABLE_ID,
        )
        ROWS = 1234
        TOKEN = "TOKEN"
        DATA = {
            "totalRows": ROWS,
            "pageToken": TOKEN,
            "rows": [
                {
                    "f": [
                        {"v": "Phred Phlyntstone"},
                        {"v": {"f": [{"v": "800"}, {"v": "555-1212"}, {"v": 1}]}},
                    ]
                },
                {
                    "f": [
                        {"v": "Bharney Rhubble"},
                        {"v": {"f": [{"v": "877"}, {"v": "768-5309"}, {"v": 2}]}},
                    ]
                },
                {"f": [{"v": "Wylma Phlyntstone"}, {"v": None}]},
            ],
        }
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        conn = client._connection = make_connection(DATA)
        full_name = SchemaField("full_name", "STRING", mode="REQUIRED")
        area_code = SchemaField("area_code", "STRING", "REQUIRED")
        local_number = SchemaField("local_number", "STRING", "REQUIRED")
        rank = SchemaField("rank", "INTEGER", "REQUIRED")
        phone = SchemaField(
            "phone", "RECORD", mode="NULLABLE", fields=[area_code, local_number, rank]
        )
        table = Table(self.TABLE_REF, schema=[full_name, phone])

        iterator = client.list_rows(table)
        page = next(iterator.pages)
        rows = list(page)
        total_rows = iterator.total_rows
        page_token = iterator.next_page_token

        self.assertEqual(len(rows), 3)
        self.assertEqual(rows[0][0], "Phred Phlyntstone")
        self.assertEqual(
            rows[0][1], {"area_code": "800", "local_number": "555-1212", "rank": 1}
        )
        self.assertEqual(rows[1][0], "Bharney Rhubble")
        self.assertEqual(
            rows[1][1], {"area_code": "877", "local_number": "768-5309", "rank": 2}
        )
        self.assertEqual(rows[2][0], "Wylma Phlyntstone")
        self.assertIsNone(rows[2][1])
        self.assertEqual(total_rows, ROWS)
        self.assertEqual(page_token, TOKEN)

        conn.api_request.assert_called_once_with(
            method="GET",
            path="/%s" % PATH,
            query_params={"formatOptions.useInt64Timestamp": True},
            timeout=DEFAULT_TIMEOUT,
        )

    def test_list_rows_with_missing_schema(self):
        from google.cloud.bigquery.table import Table, TableListItem

        table_path = "/projects/{}/datasets/{}/tables/{}".format(
            self.PROJECT, self.DS_ID, self.TABLE_ID
        )
        tabledata_path = "{}/data".format(table_path)

        table_list_item_data = {
            "id": "%s:%s:%s" % (self.PROJECT, self.DS_ID, self.TABLE_ID),
            "tableReference": {
                "projectId": self.PROJECT,
                "datasetId": self.DS_ID,
                "tableId": self.TABLE_ID,
            },
        }
        table_data = copy.deepcopy(table_list_item_data)
        # Intentionally make wrong, since total_rows can update during iteration.
        table_data["numRows"] = 2
        table_data["schema"] = {
            "fields": [
                {"name": "name", "type": "STRING"},
                {"name": "age", "type": "INTEGER"},
            ]
        }
        rows_data = {
            "totalRows": 3,
            "pageToken": None,
            "rows": [
                {"f": [{"v": "Phred Phlyntstone"}, {"v": "32"}]},
                {"f": [{"v": "Bharney Rhubble"}, {"v": "31"}]},
                {"f": [{"v": "Wylma Phlyntstone"}, {"v": None}]},
            ],
        }

        creds = _make_credentials()
        http = object()

        schemaless_tables = (
            "{}.{}".format(self.DS_ID, self.TABLE_ID),
            self.TABLE_REF,
            Table(self.TABLE_REF),
            TableListItem(table_list_item_data),
        )

        for table in schemaless_tables:
            client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
            conn = client._connection = make_connection(table_data, rows_data)

            row_iter = client.list_rows(table)

            conn.api_request.assert_called_once_with(
                method="GET", path=table_path, timeout=DEFAULT_TIMEOUT
            )
            conn.api_request.reset_mock()
            self.assertEqual(row_iter.total_rows, 2, msg=repr(table))

            rows = list(row_iter)
            conn.api_request.assert_called_once_with(
                method="GET",
                path=tabledata_path,
                query_params={"formatOptions.useInt64Timestamp": True},
                timeout=DEFAULT_TIMEOUT,
            )
            self.assertEqual(row_iter.total_rows, 3, msg=repr(table))
            self.assertEqual(rows[0].name, "Phred Phlyntstone", msg=repr(table))
            self.assertEqual(rows[1].age, 31, msg=repr(table))
            self.assertIsNone(rows[2].age, msg=repr(table))

    def test_list_rows_error(self):
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)

        # neither Table nor TableReference
        with self.assertRaises(TypeError):
            client.list_rows(1)

    def test_context_manager_enter_returns_itself(self):
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)

        with mock.patch.object(client, "close"), client as context_var:
            pass

        self.assertIs(client, context_var)

    def test_context_manager_exit_closes_client(self):
        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)

        fake_close = mock.Mock()
        with mock.patch.object(client, "close", fake_close):
            with client:
                pass

        fake_close.assert_called_once()


class TestClientUpload(object):
    # NOTE: This is a "partner" to `TestClient` meant to test some of the
    #       "load_table_from_file" portions of `Client`. It also uses
    #       `pytest`-style tests rather than `unittest`-style.
    from google.cloud.bigquery.job import SourceFormat

    PROJECT = "project_id"
    TABLE_REF = DatasetReference(PROJECT, "test_dataset").table("test_table")

    LOCATION = "us-central"

    @classmethod
    def _make_client(cls, transport=None, location=None):
        from google.cloud.bigquery import _http, client

        cl = client.Client(
            project=cls.PROJECT,
            credentials=_make_credentials(),
            _http=transport,
            location=location,
        )
        cl._connection = mock.create_autospec(_http.Connection, instance=True)
        return cl

    @staticmethod
    def _make_response(status_code, content="", headers={}):
        """Make a mock HTTP response."""
        import requests

        response = requests.Response()
        response.request = requests.Request("POST", "http://example.com").prepare()
        response._content = content.encode("utf-8")
        response.headers.update(headers)
        response.status_code = status_code
        return response

    @classmethod
    def _make_do_upload_patch(cls, client, method, resource={}, side_effect=None):
        """Patches the low-level upload helpers."""
        if side_effect is None:
            side_effect = [
                cls._make_response(
                    http.client.OK,
                    json.dumps(resource),
                    {"Content-Type": "application/json"},
                )
            ]
        return mock.patch.object(client, method, side_effect=side_effect, autospec=True)

    EXPECTED_CONFIGURATION = {
        "jobReference": {"projectId": PROJECT, "jobId": "job_id"},
        "configuration": {
            "load": {
                "sourceFormat": SourceFormat.CSV,
                "destinationTable": {
                    "projectId": PROJECT,
                    "datasetId": "test_dataset",
                    "tableId": "test_table",
                },
            }
        },
    }

    @staticmethod
    def _make_file_obj():
        return io.BytesIO(b"hello, is it me you're looking for?")

    def _make_gzip_file_obj(self, writable):
        if writable:
            return gzip.GzipFile(mode="w", fileobj=io.BytesIO())
        else:
            return gzip.GzipFile(mode="r", fileobj=self._make_file_obj())

    @staticmethod
    def _make_config():
        from google.cloud.bigquery.job import LoadJobConfig, SourceFormat

        config = LoadJobConfig()
        config.source_format = SourceFormat.CSV
        return config

    # High-level tests

    def test_load_table_from_file_resumable(self):
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES

        client = self._make_client()
        file_obj = self._make_file_obj()
        job_config = self._make_config()
        original_config_copy = copy.deepcopy(job_config)

        do_upload_patch = self._make_do_upload_patch(
            client, "_do_resumable_upload", self.EXPECTED_CONFIGURATION
        )
        with do_upload_patch as do_upload:
            client.load_table_from_file(
                file_obj,
                self.TABLE_REF,
                job_id="job_id",
                job_config=job_config,
            )

        do_upload.assert_called_once_with(
            file_obj,
            self.EXPECTED_CONFIGURATION,
            _DEFAULT_NUM_RETRIES,
            DEFAULT_TIMEOUT,
            project=self.EXPECTED_CONFIGURATION["jobReference"]["projectId"],
        )

        # the original config object should not have been modified
        assert job_config.to_api_repr() == original_config_copy.to_api_repr()

    def test_load_table_from_file_w_explicit_project(self):
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES

        client = self._make_client()
        file_obj = self._make_file_obj()

        do_upload_patch = self._make_do_upload_patch(
            client, "_do_resumable_upload", self.EXPECTED_CONFIGURATION
        )
        with do_upload_patch as do_upload:
            client.load_table_from_file(
                file_obj,
                self.TABLE_REF,
                job_id="job_id",
                project="other-project",
                location=self.LOCATION,
                job_config=self._make_config(),
            )

        expected_resource = copy.deepcopy(self.EXPECTED_CONFIGURATION)
        expected_resource["jobReference"]["location"] = self.LOCATION
        expected_resource["jobReference"]["projectId"] = "other-project"
        do_upload.assert_called_once_with(
            file_obj,
            expected_resource,
            _DEFAULT_NUM_RETRIES,
            DEFAULT_TIMEOUT,
            project="other-project",
        )

    def test_load_table_from_file_w_client_location(self):
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES

        client = self._make_client(location=self.LOCATION)
        file_obj = self._make_file_obj()

        do_upload_patch = self._make_do_upload_patch(
            client, "_do_resumable_upload", self.EXPECTED_CONFIGURATION
        )
        with do_upload_patch as do_upload:
            client.load_table_from_file(
                file_obj,
                # Test with string for table ID.
                "{}.{}.{}".format(
                    self.TABLE_REF.project,
                    self.TABLE_REF.dataset_id,
                    self.TABLE_REF.table_id,
                ),
                job_id="job_id",
                project="other-project",
                job_config=self._make_config(),
            )

        expected_resource = copy.deepcopy(self.EXPECTED_CONFIGURATION)
        expected_resource["jobReference"]["location"] = self.LOCATION
        expected_resource["jobReference"]["projectId"] = "other-project"
        do_upload.assert_called_once_with(
            file_obj,
            expected_resource,
            _DEFAULT_NUM_RETRIES,
            DEFAULT_TIMEOUT,
            project="other-project",
        )

    def test_load_table_from_file_resumable_metadata(self):
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES
        from google.cloud.bigquery.job import CreateDisposition, WriteDisposition

        client = self._make_client()
        file_obj = self._make_file_obj()

        config = self._make_config()
        config.allow_jagged_rows = False
        config.allow_quoted_newlines = False
        config.create_disposition = CreateDisposition.CREATE_IF_NEEDED
        config.encoding = "utf8"
        config.field_delimiter = ","
        config.ignore_unknown_values = False
        config.max_bad_records = 0
        config.quote_character = '"'
        config.skip_leading_rows = 1
        config.write_disposition = WriteDisposition.WRITE_APPEND
        config.null_marker = r"\N"

        expected_config = {
            "jobReference": {"projectId": self.PROJECT, "jobId": "job_id"},
            "configuration": {
                "load": {
                    "destinationTable": {
                        "projectId": self.TABLE_REF.project,
                        "datasetId": self.TABLE_REF.dataset_id,
                        "tableId": self.TABLE_REF.table_id,
                    },
                    "sourceFormat": config.source_format,
                    "allowJaggedRows": config.allow_jagged_rows,
                    "allowQuotedNewlines": config.allow_quoted_newlines,
                    "createDisposition": config.create_disposition,
                    "encoding": config.encoding,
                    "fieldDelimiter": config.field_delimiter,
                    "ignoreUnknownValues": config.ignore_unknown_values,
                    "maxBadRecords": config.max_bad_records,
                    "quote": config.quote_character,
                    "skipLeadingRows": str(config.skip_leading_rows),
                    "writeDisposition": config.write_disposition,
                    "nullMarker": config.null_marker,
                }
            },
        }

        do_upload_patch = self._make_do_upload_patch(
            client, "_do_resumable_upload", expected_config
        )
        with do_upload_patch as do_upload:
            client.load_table_from_file(
                file_obj, self.TABLE_REF, job_id="job_id", job_config=config
            )

        do_upload.assert_called_once_with(
            file_obj,
            expected_config,
            _DEFAULT_NUM_RETRIES,
            DEFAULT_TIMEOUT,
            project=self.EXPECTED_CONFIGURATION["jobReference"]["projectId"],
        )

    def test_load_table_from_file_multipart(self):
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES

        client = self._make_client()
        file_obj = self._make_file_obj()
        file_obj_size = 10
        config = self._make_config()

        do_upload_patch = self._make_do_upload_patch(
            client, "_do_multipart_upload", self.EXPECTED_CONFIGURATION
        )
        with do_upload_patch as do_upload:
            client.load_table_from_file(
                file_obj,
                self.TABLE_REF,
                job_id="job_id",
                job_config=config,
                size=file_obj_size,
            )

        do_upload.assert_called_once_with(
            file_obj,
            self.EXPECTED_CONFIGURATION,
            file_obj_size,
            _DEFAULT_NUM_RETRIES,
            DEFAULT_TIMEOUT,
            project=self.PROJECT,
        )

    def test_load_table_from_file_with_retries(self):
        client = self._make_client()
        file_obj = self._make_file_obj()
        num_retries = 20

        do_upload_patch = self._make_do_upload_patch(
            client, "_do_resumable_upload", self.EXPECTED_CONFIGURATION
        )
        with do_upload_patch as do_upload:
            client.load_table_from_file(
                file_obj,
                self.TABLE_REF,
                num_retries=num_retries,
                job_id="job_id",
                job_config=self._make_config(),
            )

        do_upload.assert_called_once_with(
            file_obj,
            self.EXPECTED_CONFIGURATION,
            num_retries,
            DEFAULT_TIMEOUT,
            project=self.EXPECTED_CONFIGURATION["jobReference"]["projectId"],
        )

    def test_load_table_from_file_with_rewind(self):
        client = self._make_client()
        file_obj = self._make_file_obj()
        file_obj.seek(2)

        with self._make_do_upload_patch(
            client, "_do_resumable_upload", self.EXPECTED_CONFIGURATION
        ):
            client.load_table_from_file(file_obj, self.TABLE_REF, rewind=True)

        assert file_obj.tell() == 0

    def test_load_table_from_file_with_readable_gzip(self):
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES

        client = self._make_client()
        gzip_file = self._make_gzip_file_obj(writable=False)

        do_upload_patch = self._make_do_upload_patch(
            client, "_do_resumable_upload", self.EXPECTED_CONFIGURATION
        )
        with do_upload_patch as do_upload:
            client.load_table_from_file(
                gzip_file,
                self.TABLE_REF,
                job_id="job_id",
                job_config=self._make_config(),
            )

        do_upload.assert_called_once_with(
            gzip_file,
            self.EXPECTED_CONFIGURATION,
            _DEFAULT_NUM_RETRIES,
            DEFAULT_TIMEOUT,
            project=self.EXPECTED_CONFIGURATION["jobReference"]["projectId"],
        )

    def test_load_table_from_file_with_writable_gzip(self):
        client = self._make_client()
        gzip_file = self._make_gzip_file_obj(writable=True)

        with pytest.raises(ValueError):
            client.load_table_from_file(
                gzip_file,
                self.TABLE_REF,
                job_id="job_id",
                job_config=self._make_config(),
            )

    def test_load_table_from_file_failure(self):
        from google.cloud import exceptions
        from google.resumable_media import InvalidResponse

        client = self._make_client()
        file_obj = self._make_file_obj()

        response = self._make_response(
            content="Someone is already in this spot.", status_code=http.client.CONFLICT
        )

        do_upload_patch = self._make_do_upload_patch(
            client, "_do_resumable_upload", side_effect=InvalidResponse(response)
        )

        with do_upload_patch, pytest.raises(exceptions.Conflict) as exc_info:
            client.load_table_from_file(file_obj, self.TABLE_REF, rewind=True)

        assert response.text in exc_info.value.message
        assert exc_info.value.errors == []

    def test_load_table_from_file_bad_mode(self):
        client = self._make_client()
        file_obj = mock.Mock(spec=["mode"])
        file_obj.mode = "x"

        with pytest.raises(ValueError):
            client.load_table_from_file(file_obj, self.TABLE_REF)

    def test_load_table_from_file_w_invalid_job_config(self):
        from google.cloud.bigquery import job

        client = self._make_client()
        gzip_file = self._make_gzip_file_obj(writable=True)
        config = job.QueryJobConfig()
        with pytest.raises(TypeError) as exc:
            client.load_table_from_file(
                gzip_file, self.TABLE_REF, job_id="job_id", job_config=config
            )
        err_msg = str(exc.value)
        assert "Expected an instance of LoadJobConfig" in err_msg

    def test_load_table_from_file_w_explicit_job_config(self):
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES

        client = self._make_client()
        file_obj = self._make_file_obj()

        job_config = self._make_config()
        job_config.create_session = True
        job_config.encoding = "UTF-8"
        do_upload_patch = self._make_do_upload_patch(
            client, "_do_resumable_upload", self.EXPECTED_CONFIGURATION
        )
        with do_upload_patch as do_upload:
            client.load_table_from_file(
                file_obj,
                self.TABLE_REF,
                job_id="job_id",
                project=self.PROJECT,
                location=self.LOCATION,
                job_config=job_config,
            )

        expected_resource = copy.deepcopy(self.EXPECTED_CONFIGURATION)
        expected_resource["jobReference"]["location"] = self.LOCATION
        expected_resource["jobReference"]["projectId"] = self.PROJECT
        expected_resource["configuration"]["load"]["createSession"] = True
        expected_resource["configuration"]["load"]["encoding"] = "UTF-8"
        do_upload.assert_called_once_with(
            file_obj,
            expected_resource,
            _DEFAULT_NUM_RETRIES,
            DEFAULT_TIMEOUT,
            project=self.PROJECT,
        )

    def test_load_table_from_file_w_explicit_job_config_override(self):
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES
        from google.cloud.bigquery.job import LoadJobConfig

        client = self._make_client()
        file_obj = self._make_file_obj()

        default_job_config = LoadJobConfig()
        default_job_config.create_session = True
        default_job_config.encoding = "ISO-8859-1"
        client.default_load_job_config = default_job_config

        job_config = self._make_config()
        job_config.create_session = False
        do_upload_patch = self._make_do_upload_patch(
            client, "_do_resumable_upload", self.EXPECTED_CONFIGURATION
        )
        with do_upload_patch as do_upload:
            client.load_table_from_file(
                file_obj,
                self.TABLE_REF,
                job_id="job_id",
                project=self.PROJECT,
                location=self.LOCATION,
                job_config=job_config,
            )

        expected_resource = copy.deepcopy(self.EXPECTED_CONFIGURATION)
        expected_resource["jobReference"]["location"] = self.LOCATION
        expected_resource["jobReference"]["projectId"] = self.PROJECT
        expected_resource["configuration"]["load"]["createSession"] = False
        expected_resource["configuration"]["load"]["encoding"] = "ISO-8859-1"
        do_upload.assert_called_once_with(
            file_obj,
            expected_resource,
            _DEFAULT_NUM_RETRIES,
            DEFAULT_TIMEOUT,
            project=self.PROJECT,
        )

    def test_load_table_from_file_w_default_load_config(self):
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES
        from google.cloud.bigquery.job import LoadJobConfig

        client = self._make_client()
        file_obj = self._make_file_obj()

        default_job_config = LoadJobConfig()
        default_job_config.encoding = "ISO-8859-1"
        client.default_load_job_config = default_job_config

        job_config = self._make_config()
        do_upload_patch = self._make_do_upload_patch(
            client, "_do_resumable_upload", self.EXPECTED_CONFIGURATION
        )
        with do_upload_patch as do_upload:
            client.load_table_from_file(
                file_obj,
                self.TABLE_REF,
                job_id="job_id",
                project=self.PROJECT,
                location=self.LOCATION,
                job_config=job_config,
            )

        expected_resource = copy.deepcopy(self.EXPECTED_CONFIGURATION)
        expected_resource["jobReference"]["location"] = self.LOCATION
        expected_resource["jobReference"]["projectId"] = self.PROJECT
        expected_resource["configuration"]["load"]["encoding"] = "ISO-8859-1"
        do_upload.assert_called_once_with(
            file_obj,
            expected_resource,
            _DEFAULT_NUM_RETRIES,
            DEFAULT_TIMEOUT,
            project=self.PROJECT,
        )

    def test_load_table_from_dataframe(self):
        pandas = pytest.importorskip("pandas")
        pytest.importorskip("pyarrow")
        from google.cloud.bigquery import job
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES
        from google.cloud.bigquery.schema import PolicyTagList, SchemaField

        client = self._make_client()
        records = [
            {"id": 1, "age": 100, "accounts": [2, 3]},
            {"id": 2, "age": 60, "accounts": [5]},
            {"id": 3, "age": 40, "accounts": []},
        ]
        # Mixup column order so that we can verify sent schema matches the
        # serialized order, not the table column order.
        column_order = ["age", "accounts", "id"]
        dataframe = pandas.DataFrame(records, columns=column_order)
        table_fields = {
            "id": SchemaField(
                "id",
                "INTEGER",
                mode="REQUIRED",
                description="integer column",
                policy_tags=PolicyTagList(names=("foo", "bar")),
            ),
            "age": SchemaField(
                "age",
                "INTEGER",
                mode="NULLABLE",
                description="age column",
                policy_tags=PolicyTagList(names=("baz",)),
            ),
            "accounts": SchemaField(
                "accounts",
                "INTEGER",
                mode="REPEATED",
                description="array column",
            ),
        }
        get_table_schema = [
            table_fields["id"],
            table_fields["age"],
            table_fields["accounts"],
        ]

        get_table_patch = mock.patch(
            "google.cloud.bigquery.client.Client.get_table",
            autospec=True,
            return_value=mock.Mock(schema=get_table_schema),
        )
        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )
        with load_patch as load_table_from_file, get_table_patch:
            client.load_table_from_dataframe(dataframe, self.TABLE_REF)

        load_table_from_file.assert_called_once_with(
            client,
            mock.ANY,
            self.TABLE_REF,
            num_retries=_DEFAULT_NUM_RETRIES,
            rewind=True,
            size=mock.ANY,
            job_id=mock.ANY,
            job_id_prefix=None,
            location=None,
            project=None,
            job_config=mock.ANY,
            timeout=DEFAULT_TIMEOUT,
        )

        sent_file = load_table_from_file.mock_calls[0][1][1]
        assert sent_file.closed

        sent_config = load_table_from_file.mock_calls[0][2]["job_config"].to_api_repr()[
            "load"
        ]
        assert sent_config["sourceFormat"] == job.SourceFormat.PARQUET
        for field_index, field in enumerate(sent_config["schema"]["fields"]):
            assert field["name"] == column_order[field_index]
            table_field = table_fields[field["name"]]
            assert field["name"] == table_field.name
            assert field["type"] == table_field.field_type
            assert field["mode"] == table_field.mode
            assert len(field.get("fields", [])) == len(table_field.fields)
            # Avoid accidentally updating policy tags when not explicitly included.
            # https://github.com/googleapis/python-bigquery/issues/981
            # Also, avoid 403 if someone has permission to write to table but
            # not update policy tags by omitting policy tags we might have
            # received from a get table request.
            # https://github.com/googleapis/python-bigquery/pull/557
            assert "policyTags" not in field
            # Omit unnecessary fields when they come from getting the table
            # (not passed in via job_config)
            assert "description" not in field

    def test_load_table_from_dataframe_w_client_location(self):
        pandas = pytest.importorskip("pandas")
        pytest.importorskip("pyarrow")
        from google.cloud.bigquery import job
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES
        from google.cloud.bigquery.schema import SchemaField

        client = self._make_client(location=self.LOCATION)
        records = [{"id": 1, "age": 100}, {"id": 2, "age": 60}]
        dataframe = pandas.DataFrame(records)

        get_table_patch = mock.patch(
            "google.cloud.bigquery.client.Client.get_table",
            autospec=True,
            return_value=mock.Mock(
                schema=[SchemaField("id", "INTEGER"), SchemaField("age", "INTEGER")]
            ),
        )
        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )
        with load_patch as load_table_from_file, get_table_patch:
            client.load_table_from_dataframe(dataframe, self.TABLE_REF)

        load_table_from_file.assert_called_once_with(
            client,
            mock.ANY,
            self.TABLE_REF,
            num_retries=_DEFAULT_NUM_RETRIES,
            rewind=True,
            size=mock.ANY,
            job_id=mock.ANY,
            job_id_prefix=None,
            location=self.LOCATION,
            project=None,
            job_config=mock.ANY,
            timeout=DEFAULT_TIMEOUT,
        )

        sent_file = load_table_from_file.mock_calls[0][1][1]
        assert sent_file.closed

        sent_config = load_table_from_file.mock_calls[0][2]["job_config"]
        assert sent_config.source_format == job.SourceFormat.PARQUET

    def test_load_table_from_dataframe_w_custom_job_config_wihtout_source_format(self):
        pandas = pytest.importorskip("pandas")
        pytest.importorskip("pyarrow")
        from google.cloud.bigquery import job
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES
        from google.cloud.bigquery.schema import SchemaField

        client = self._make_client()
        records = [{"id": 1, "age": 100}, {"id": 2, "age": 60}]
        dataframe = pandas.DataFrame(records)
        job_config = job.LoadJobConfig(
            write_disposition=job.WriteDisposition.WRITE_TRUNCATE,
        )
        original_config_copy = copy.deepcopy(job_config)

        get_table_patch = mock.patch(
            "google.cloud.bigquery.client.Client.get_table",
            autospec=True,
            return_value=mock.Mock(
                schema=[SchemaField("id", "INTEGER"), SchemaField("age", "INTEGER")]
            ),
        )
        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )
        with load_patch as load_table_from_file, get_table_patch as get_table:
            client.load_table_from_dataframe(
                dataframe, self.TABLE_REF, job_config=job_config, location=self.LOCATION
            )

        # no need to fetch and inspect table schema for WRITE_TRUNCATE jobs
        assert not get_table.called

        load_table_from_file.assert_called_once_with(
            client,
            mock.ANY,
            self.TABLE_REF,
            num_retries=_DEFAULT_NUM_RETRIES,
            rewind=True,
            size=mock.ANY,
            job_id=mock.ANY,
            job_id_prefix=None,
            location=self.LOCATION,
            project=None,
            job_config=mock.ANY,
            timeout=DEFAULT_TIMEOUT,
        )

        sent_config = load_table_from_file.mock_calls[0][2]["job_config"]
        assert sent_config.source_format == job.SourceFormat.PARQUET
        assert sent_config.write_disposition == job.WriteDisposition.WRITE_TRUNCATE

        # the original config object should not have been modified
        assert job_config.to_api_repr() == original_config_copy.to_api_repr()

    def test_load_table_from_dataframe_w_custom_job_config_w_source_format(self):
        pandas = pytest.importorskip("pandas")
        pytest.importorskip("pyarrow")
        from google.cloud.bigquery import job
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES
        from google.cloud.bigquery.schema import SchemaField

        client = self._make_client()
        records = [{"id": 1, "age": 100}, {"id": 2, "age": 60}]
        dataframe = pandas.DataFrame(records)
        job_config = job.LoadJobConfig(
            write_disposition=job.WriteDisposition.WRITE_TRUNCATE,
            source_format=job.SourceFormat.PARQUET,
        )
        original_config_copy = copy.deepcopy(job_config)

        get_table_patch = mock.patch(
            "google.cloud.bigquery.client.Client.get_table",
            autospec=True,
            return_value=mock.Mock(
                schema=[SchemaField("id", "INTEGER"), SchemaField("age", "INTEGER")]
            ),
        )
        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )
        with load_patch as load_table_from_file, get_table_patch as get_table:
            client.load_table_from_dataframe(
                dataframe, self.TABLE_REF, job_config=job_config, location=self.LOCATION
            )

        # no need to fetch and inspect table schema for WRITE_TRUNCATE jobs
        assert not get_table.called

        load_table_from_file.assert_called_once_with(
            client,
            mock.ANY,
            self.TABLE_REF,
            num_retries=_DEFAULT_NUM_RETRIES,
            rewind=True,
            size=mock.ANY,
            job_id=mock.ANY,
            job_id_prefix=None,
            location=self.LOCATION,
            project=None,
            job_config=mock.ANY,
            timeout=DEFAULT_TIMEOUT,
        )

        sent_config = load_table_from_file.mock_calls[0][2]["job_config"]
        assert sent_config.source_format == job.SourceFormat.PARQUET
        assert sent_config.write_disposition == job.WriteDisposition.WRITE_TRUNCATE

        # the original config object should not have been modified
        assert job_config.to_api_repr() == original_config_copy.to_api_repr()

    def test_load_table_from_dataframe_w_parquet_options_none(self):
        pandas = pytest.importorskip("pandas")
        pytest.importorskip("pyarrow")
        from google.cloud.bigquery import job
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES
        from google.cloud.bigquery.schema import SchemaField

        client = self._make_client()
        records = [{"id": 1, "age": 100}, {"id": 2, "age": 60}]
        dataframe = pandas.DataFrame(records)

        job_config = job.LoadJobConfig(
            write_disposition=job.WriteDisposition.WRITE_TRUNCATE,
            source_format=job.SourceFormat.PARQUET,
        )

        get_table_patch = mock.patch(
            "google.cloud.bigquery.client.Client.get_table",
            autospec=True,
            return_value=mock.Mock(
                schema=[SchemaField("id", "INTEGER"), SchemaField("age", "INTEGER")]
            ),
        )
        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )
        with load_patch as load_table_from_file, get_table_patch as get_table:
            client.load_table_from_dataframe(
                dataframe, self.TABLE_REF, job_config=job_config, location=self.LOCATION
            )

        # no need to fetch and inspect table schema for WRITE_TRUNCATE jobs
        assert not get_table.called

        load_table_from_file.assert_called_once_with(
            client,
            mock.ANY,
            self.TABLE_REF,
            num_retries=_DEFAULT_NUM_RETRIES,
            rewind=True,
            size=mock.ANY,
            job_id=mock.ANY,
            job_id_prefix=None,
            location=self.LOCATION,
            project=None,
            job_config=mock.ANY,
            timeout=DEFAULT_TIMEOUT,
        )

        sent_config = load_table_from_file.mock_calls[0][2]["job_config"]
        assert sent_config.parquet_options.enable_list_inference is True

    def test_load_table_from_dataframe_w_list_inference_none(self):
        pandas = pytest.importorskip("pandas")
        pytest.importorskip("pyarrow")
        from google.cloud.bigquery import job
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES
        from google.cloud.bigquery.schema import SchemaField

        client = self._make_client()
        records = [{"id": 1, "age": 100}, {"id": 2, "age": 60}]
        dataframe = pandas.DataFrame(records)

        parquet_options = ParquetOptions()

        job_config = job.LoadJobConfig(
            write_disposition=job.WriteDisposition.WRITE_TRUNCATE,
            source_format=job.SourceFormat.PARQUET,
        )
        job_config.parquet_options = parquet_options

        original_config_copy = copy.deepcopy(job_config)

        get_table_patch = mock.patch(
            "google.cloud.bigquery.client.Client.get_table",
            autospec=True,
            return_value=mock.Mock(
                schema=[SchemaField("id", "INTEGER"), SchemaField("age", "INTEGER")]
            ),
        )
        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )
        with load_patch as load_table_from_file, get_table_patch as get_table:
            client.load_table_from_dataframe(
                dataframe, self.TABLE_REF, job_config=job_config, location=self.LOCATION
            )

        # no need to fetch and inspect table schema for WRITE_TRUNCATE jobs
        assert not get_table.called

        load_table_from_file.assert_called_once_with(
            client,
            mock.ANY,
            self.TABLE_REF,
            num_retries=_DEFAULT_NUM_RETRIES,
            rewind=True,
            size=mock.ANY,
            job_id=mock.ANY,
            job_id_prefix=None,
            location=self.LOCATION,
            project=None,
            job_config=mock.ANY,
            timeout=DEFAULT_TIMEOUT,
        )

        sent_config = load_table_from_file.mock_calls[0][2]["job_config"]
        assert sent_config.parquet_options.enable_list_inference is None

        # the original config object should not have been modified
        assert job_config.to_api_repr() == original_config_copy.to_api_repr()

    def test_load_table_from_dataframe_w_explicit_job_config_override(self):
        pandas = pytest.importorskip("pandas")
        pytest.importorskip("pyarrow")
        from google.cloud.bigquery import job
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES
        from google.cloud.bigquery.schema import SchemaField

        client = self._make_client()
        records = [{"id": 1, "age": 100}, {"id": 2, "age": 60}]
        dataframe = pandas.DataFrame(records)

        client.default_load_job_config = job.LoadJobConfig(
            encoding="ISO-8859-1",
            write_disposition=job.WriteDisposition.WRITE_TRUNCATE,
            source_format=job.SourceFormat.PARQUET,
        )

        job_config = job.LoadJobConfig(
            write_disposition=job.WriteDisposition.WRITE_APPEND,
            source_format=job.SourceFormat.PARQUET,
        )
        original_config_copy = copy.deepcopy(job_config)

        get_table_patch = mock.patch(
            "google.cloud.bigquery.client.Client.get_table",
            autospec=True,
            return_value=mock.Mock(
                schema=[SchemaField("id", "INTEGER"), SchemaField("age", "INTEGER")]
            ),
        )
        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )
        with load_patch as load_table_from_file, get_table_patch:
            client.load_table_from_dataframe(
                dataframe, self.TABLE_REF, job_config=job_config, location=self.LOCATION
            )

        load_table_from_file.assert_called_once_with(
            client,
            mock.ANY,
            self.TABLE_REF,
            num_retries=_DEFAULT_NUM_RETRIES,
            rewind=True,
            size=mock.ANY,
            job_id=mock.ANY,
            job_id_prefix=None,
            location=self.LOCATION,
            project=None,
            job_config=mock.ANY,
            timeout=DEFAULT_TIMEOUT,
        )

        sent_config = load_table_from_file.mock_calls[0][2]["job_config"]
        assert sent_config.write_disposition == job.WriteDisposition.WRITE_APPEND
        assert sent_config.source_format == job.SourceFormat.PARQUET
        assert sent_config.encoding == "ISO-8859-1"

        # the original config object should not have been modified
        assert job_config.to_api_repr() == original_config_copy.to_api_repr()

    def test_load_table_from_dataframe_w_default_load_config(self):
        pandas = pytest.importorskip("pandas")
        pytest.importorskip("pyarrow")
        from google.cloud.bigquery import job
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES
        from google.cloud.bigquery.schema import SchemaField

        client = self._make_client()
        records = [{"id": 1, "age": 100}, {"id": 2, "age": 60}]
        dataframe = pandas.DataFrame(records)

        client.default_load_job_config = job.LoadJobConfig(
            write_disposition=job.WriteDisposition.WRITE_TRUNCATE,
            source_format=job.SourceFormat.PARQUET,
        )

        get_table_patch = mock.patch(
            "google.cloud.bigquery.client.Client.get_table",
            autospec=True,
            return_value=mock.Mock(
                schema=[SchemaField("id", "INTEGER"), SchemaField("age", "INTEGER")]
            ),
        )
        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )
        with load_patch as load_table_from_file, get_table_patch:
            client.load_table_from_dataframe(
                dataframe, self.TABLE_REF, location=self.LOCATION
            )

        load_table_from_file.assert_called_once_with(
            client,
            mock.ANY,
            self.TABLE_REF,
            num_retries=_DEFAULT_NUM_RETRIES,
            rewind=True,
            size=mock.ANY,
            job_id=mock.ANY,
            job_id_prefix=None,
            location=self.LOCATION,
            project=None,
            job_config=mock.ANY,
            timeout=DEFAULT_TIMEOUT,
        )

        sent_config = load_table_from_file.mock_calls[0][2]["job_config"]
        assert sent_config.write_disposition == job.WriteDisposition.WRITE_TRUNCATE
        assert sent_config.source_format == job.SourceFormat.PARQUET

    def test_load_table_from_dataframe_w_list_inference_false(self):
        pandas = pytest.importorskip("pandas")
        pytest.importorskip("pyarrow")
        from google.cloud.bigquery import job
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES
        from google.cloud.bigquery.schema import SchemaField

        client = self._make_client()
        records = [{"id": 1, "age": 100}, {"id": 2, "age": 60}]
        dataframe = pandas.DataFrame(records)

        parquet_options = ParquetOptions()
        parquet_options.enable_list_inference = False

        job_config = job.LoadJobConfig(
            write_disposition=job.WriteDisposition.WRITE_TRUNCATE,
            source_format=job.SourceFormat.PARQUET,
        )
        job_config.parquet_options = parquet_options

        original_config_copy = copy.deepcopy(job_config)

        get_table_patch = mock.patch(
            "google.cloud.bigquery.client.Client.get_table",
            autospec=True,
            return_value=mock.Mock(
                schema=[SchemaField("id", "INTEGER"), SchemaField("age", "INTEGER")]
            ),
        )
        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )
        with load_patch as load_table_from_file, get_table_patch as get_table:
            client.load_table_from_dataframe(
                dataframe, self.TABLE_REF, job_config=job_config, location=self.LOCATION
            )

        # no need to fetch and inspect table schema for WRITE_TRUNCATE jobs
        assert not get_table.called

        load_table_from_file.assert_called_once_with(
            client,
            mock.ANY,
            self.TABLE_REF,
            num_retries=_DEFAULT_NUM_RETRIES,
            rewind=True,
            size=mock.ANY,
            job_id=mock.ANY,
            job_id_prefix=None,
            location=self.LOCATION,
            project=None,
            job_config=mock.ANY,
            timeout=DEFAULT_TIMEOUT,
        )

        sent_config = load_table_from_file.mock_calls[0][2]["job_config"]
        assert sent_config.parquet_options.enable_list_inference is False

        # the original config object should not have been modified
        assert job_config.to_api_repr() == original_config_copy.to_api_repr()

    def test_load_table_from_dataframe_w_custom_job_config_w_wrong_source_format(self):
        pandas = pytest.importorskip("pandas")
        pytest.importorskip("pyarrow")
        from google.cloud.bigquery import job

        client = self._make_client()
        records = [{"id": 1, "age": 100}, {"id": 2, "age": 60}]
        dataframe = pandas.DataFrame(records)
        job_config = job.LoadJobConfig(
            write_disposition=job.WriteDisposition.WRITE_TRUNCATE,
            source_format=job.SourceFormat.ORC,
        )

        with pytest.raises(ValueError) as exc:
            client.load_table_from_dataframe(
                dataframe, self.TABLE_REF, job_config=job_config, location=self.LOCATION
            )

        assert "Got unexpected source_format:" in str(exc.value)

    def test_load_table_from_dataframe_w_automatic_schema(self):
        pandas = pytest.importorskip("pandas")
        pytest.importorskip("pyarrow")
        from google.cloud.bigquery import job
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES
        from google.cloud.bigquery.schema import SchemaField

        client = self._make_client()
        df_data = collections.OrderedDict(
            [
                ("int_col", [1, 2, 3]),
                ("float_col", [1.0, 2.0, 3.0]),
                ("bool_col", [True, False, True]),
                (
                    "dt_col",
                    pandas.Series(
                        [
                            datetime.datetime(2010, 1, 2, 3, 44, 50),
                            datetime.datetime(2011, 2, 3, 14, 50, 59),
                            datetime.datetime(2012, 3, 14, 15, 16),
                        ],
                        dtype="datetime64[ns]",
                    ),
                ),
                (
                    "ts_col",
                    pandas.Series(
                        [
                            datetime.datetime(2010, 1, 2, 3, 44, 50),
                            datetime.datetime(2011, 2, 3, 14, 50, 59),
                            datetime.datetime(2012, 3, 14, 15, 16),
                        ],
                        dtype="datetime64[ns]",
                    ).dt.tz_localize(datetime.timezone.utc),
                ),
                (
                    "date_col",
                    pandas.Series(
                        [
                            datetime.date(2010, 1, 2),
                            datetime.date(2011, 2, 3),
                            datetime.date(2012, 3, 14),
                        ],
                        dtype="dbdate",
                    ),
                ),
                (
                    "time_col",
                    pandas.Series(
                        [
                            datetime.time(3, 44, 50),
                            datetime.time(14, 50, 59),
                            datetime.time(15, 16),
                        ],
                        dtype="dbtime",
                    ),
                ),
            ]
        )
        dataframe = pandas.DataFrame(df_data, columns=df_data.keys())
        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )

        get_table_patch = mock.patch(
            "google.cloud.bigquery.client.Client.get_table",
            autospec=True,
            side_effect=google.api_core.exceptions.NotFound("Table not found"),
        )
        with load_patch as load_table_from_file, get_table_patch:
            client.load_table_from_dataframe(
                dataframe, self.TABLE_REF, location=self.LOCATION
            )

        load_table_from_file.assert_called_once_with(
            client,
            mock.ANY,
            self.TABLE_REF,
            num_retries=_DEFAULT_NUM_RETRIES,
            rewind=True,
            size=mock.ANY,
            job_id=mock.ANY,
            job_id_prefix=None,
            location=self.LOCATION,
            project=None,
            job_config=mock.ANY,
            timeout=DEFAULT_TIMEOUT,
        )

        sent_config = load_table_from_file.mock_calls[0][2]["job_config"]
        assert sent_config.source_format == job.SourceFormat.PARQUET
        assert tuple(sent_config.schema) == (
            SchemaField("int_col", "INTEGER"),
            SchemaField("float_col", "FLOAT"),
            SchemaField("bool_col", "BOOLEAN"),
            SchemaField("dt_col", "DATETIME"),
            SchemaField("ts_col", "TIMESTAMP"),
            SchemaField("date_col", "DATE"),
            SchemaField("time_col", "TIME"),
        )

    def test_load_table_from_dataframe_w_automatic_schema_detection_fails(self):
        pandas = pytest.importorskip("pandas")
        pytest.importorskip("pyarrow")
        from google.cloud.bigquery import job
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES

        client = self._make_client()

        df_data = [
            [[{"name": "n1.1", "value": 1.1}, {"name": "n1.2", "value": 1.2}]],
            [[{"name": "n2.1", "value": 2.1}, {"name": "n2.2", "value": 2.2}]],
        ]
        dataframe = pandas.DataFrame(df_data, columns=["col_record_list"])

        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )
        get_table_patch = mock.patch(
            "google.cloud.bigquery.client.Client.get_table",
            autospec=True,
            side_effect=google.api_core.exceptions.NotFound("Table not found"),
        )
        pandas_gbq_patch = mock.patch(
            "google.cloud.bigquery._pandas_helpers.pandas_gbq",
            new=None,
        )

        with load_patch as load_table_from_file, get_table_patch, pandas_gbq_patch:
            with warnings.catch_warnings(record=True) as warned:
                client.load_table_from_dataframe(
                    dataframe, self.TABLE_REF, location=self.LOCATION
                )

        # There should be a warning that schema detection failed.
        expected_warnings = [
            warning
            for warning in warned
            if "schema could not be detected" in str(warning).lower()
        ]
        assert len(expected_warnings) == 1
        assert issubclass(
            expected_warnings[0].category,
            (DeprecationWarning, PendingDeprecationWarning),
        )

        load_table_from_file.assert_called_once_with(
            client,
            mock.ANY,
            self.TABLE_REF,
            num_retries=_DEFAULT_NUM_RETRIES,
            rewind=True,
            size=mock.ANY,
            job_id=mock.ANY,
            job_id_prefix=None,
            location=self.LOCATION,
            project=None,
            job_config=mock.ANY,
            timeout=DEFAULT_TIMEOUT,
        )

        sent_config = load_table_from_file.mock_calls[0][2]["job_config"]
        assert sent_config.source_format == job.SourceFormat.PARQUET
        assert sent_config.schema is None

    def test_load_table_from_dataframe_w_index_and_auto_schema(self):
        pandas = pytest.importorskip("pandas")
        pytest.importorskip("pyarrow")
        from google.cloud.bigquery import job
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES
        from google.cloud.bigquery.schema import SchemaField

        client = self._make_client()
        df_data = collections.OrderedDict(
            [("int_col", [10, 20, 30]), ("float_col", [1.0, 2.0, 3.0])]
        )
        dataframe = pandas.DataFrame(
            df_data,
            index=pandas.Index(name="unique_name", data=["one", "two", "three"]),
        )

        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )
        get_table_patch = mock.patch(
            "google.cloud.bigquery.client.Client.get_table",
            autospec=True,
            return_value=mock.Mock(
                schema=[
                    SchemaField("int_col", "INTEGER"),
                    SchemaField("float_col", "FLOAT"),
                    SchemaField("unique_name", "STRING"),
                ]
            ),
        )

        with load_patch as load_table_from_file, get_table_patch:
            client.load_table_from_dataframe(
                dataframe, self.TABLE_REF, location=self.LOCATION
            )

        load_table_from_file.assert_called_once_with(
            client,
            mock.ANY,
            self.TABLE_REF,
            num_retries=_DEFAULT_NUM_RETRIES,
            rewind=True,
            size=mock.ANY,
            job_id=mock.ANY,
            job_id_prefix=None,
            location=self.LOCATION,
            project=None,
            job_config=mock.ANY,
            timeout=DEFAULT_TIMEOUT,
        )

        sent_config = load_table_from_file.mock_calls[0][2]["job_config"]
        assert sent_config.source_format == job.SourceFormat.PARQUET

        sent_schema = sorted(sent_config.schema, key=operator.attrgetter("name"))
        expected_sent_schema = [
            SchemaField("float_col", "FLOAT"),
            SchemaField("int_col", "INTEGER"),
            SchemaField("unique_name", "STRING"),
        ]
        assert sent_schema == expected_sent_schema

    def test_load_table_from_dataframe_unknown_table(self):
        pandas = pytest.importorskip("pandas")
        pytest.importorskip("pyarrow")
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES

        client = self._make_client()
        records = [{"id": 1, "age": 100}, {"id": 2, "age": 60}]
        dataframe = pandas.DataFrame(records)

        get_table_patch = mock.patch(
            "google.cloud.bigquery.client.Client.get_table",
            autospec=True,
            side_effect=google.api_core.exceptions.NotFound("Table not found"),
        )
        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )
        with load_patch as load_table_from_file, get_table_patch:
            # there should be no error
            client.load_table_from_dataframe(dataframe, self.TABLE_REF)

        load_table_from_file.assert_called_once_with(
            client,
            mock.ANY,
            self.TABLE_REF,
            num_retries=_DEFAULT_NUM_RETRIES,
            rewind=True,
            size=mock.ANY,
            job_id=mock.ANY,
            job_id_prefix=None,
            location=None,
            project=None,
            job_config=mock.ANY,
            timeout=DEFAULT_TIMEOUT,
        )

    def test_load_table_from_dataframe_w_nullable_int64_datatype(self):
        pandas = pytest.importorskip("pandas")
        pytest.importorskip("pyarrow")
        from google.cloud.bigquery import job
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES
        from google.cloud.bigquery.schema import SchemaField

        client = self._make_client()
        dataframe = pandas.DataFrame({"x": [1, 2, None, 4]}, dtype="Int64")
        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )

        get_table_patch = mock.patch(
            "google.cloud.bigquery.client.Client.get_table",
            autospec=True,
            return_value=mock.Mock(schema=[SchemaField("x", "INT64", "NULLABLE")]),
        )

        with load_patch as load_table_from_file, get_table_patch:
            client.load_table_from_dataframe(
                dataframe, self.TABLE_REF, location=self.LOCATION
            )

        load_table_from_file.assert_called_once_with(
            client,
            mock.ANY,
            self.TABLE_REF,
            num_retries=_DEFAULT_NUM_RETRIES,
            rewind=True,
            size=mock.ANY,
            job_id=mock.ANY,
            job_id_prefix=None,
            location=self.LOCATION,
            project=None,
            job_config=mock.ANY,
            timeout=DEFAULT_TIMEOUT,
        )

        sent_config = load_table_from_file.mock_calls[0][2]["job_config"]
        assert sent_config.source_format == job.SourceFormat.PARQUET
        assert tuple(sent_config.schema) == (
            SchemaField("x", "INT64", "NULLABLE", None),
        )

    def test_load_table_from_dataframe_w_nullable_int64_datatype_automatic_schema(self):
        pandas = pytest.importorskip("pandas")
        from google.cloud.bigquery import job
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES
        from google.cloud.bigquery.schema import SchemaField

        client = self._make_client()
        dataframe = pandas.DataFrame({"x": [1, 2, None, 4]}, dtype="Int64")

        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )
        get_table_patch = mock.patch(
            "google.cloud.bigquery.client.Client.get_table",
            autospec=True,
            side_effect=google.api_core.exceptions.NotFound("Table not found"),
        )

        with load_patch as load_table_from_file, get_table_patch:
            client.load_table_from_dataframe(
                dataframe, self.TABLE_REF, location=self.LOCATION
            )

        load_table_from_file.assert_called_once_with(
            client,
            mock.ANY,
            self.TABLE_REF,
            num_retries=_DEFAULT_NUM_RETRIES,
            rewind=True,
            size=mock.ANY,
            job_id=mock.ANY,
            job_id_prefix=None,
            location=self.LOCATION,
            project=None,
            job_config=mock.ANY,
            timeout=DEFAULT_TIMEOUT,
        )

        sent_config = load_table_from_file.mock_calls[0][2]["job_config"]
        assert sent_config.source_format == job.SourceFormat.PARQUET
        assert (
            # Accept either the GoogleSQL or legacy SQL type name from pandas-gbq.
            tuple(sent_config.schema) == (SchemaField("x", "INT64", "NULLABLE", None),)
            or tuple(sent_config.schema)
            == (SchemaField("x", "INTEGER", "NULLABLE", None),)
        )

    def test_load_table_from_dataframe_struct_fields(self):
        pandas = pytest.importorskip("pandas")
        pytest.importorskip("pyarrow")
        from google.cloud.bigquery import job
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES
        from google.cloud.bigquery.schema import SchemaField

        client = self._make_client()

        records = [(3.14, {"foo": 1, "bar": 1})]
        dataframe = pandas.DataFrame(
            data=records, columns=["float_column", "struct_column"]
        )

        schema = [
            SchemaField("float_column", "FLOAT"),
            SchemaField(
                "struct_column",
                "RECORD",
                fields=[SchemaField("foo", "INTEGER"), SchemaField("bar", "INTEGER")],
            ),
        ]
        job_config = job.LoadJobConfig(schema=schema)

        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )

        get_table_patch = mock.patch(
            "google.cloud.bigquery.client.Client.get_table",
            autospec=True,
            side_effect=google.api_core.exceptions.NotFound("Table not found"),
        )
        with load_patch as load_table_from_file, get_table_patch:
            client.load_table_from_dataframe(
                dataframe,
                self.TABLE_REF,
                job_config=job_config,
                location=self.LOCATION,
            )

        load_table_from_file.assert_called_once_with(
            client,
            mock.ANY,
            self.TABLE_REF,
            num_retries=_DEFAULT_NUM_RETRIES,
            rewind=True,
            size=mock.ANY,
            job_id=mock.ANY,
            job_id_prefix=None,
            location=self.LOCATION,
            project=None,
            job_config=mock.ANY,
            timeout=DEFAULT_TIMEOUT,
        )

        sent_config = load_table_from_file.mock_calls[0][2]["job_config"]
        assert sent_config.source_format == job.SourceFormat.PARQUET
        assert sent_config.schema == schema

    def test_load_table_from_dataframe_array_fields(self):
        """Test that a DataFrame with array columns can be uploaded correctly.

        See: https://github.com/googleapis/python-bigquery/issues/19
        """
        pandas = pytest.importorskip("pandas")
        pytest.importorskip("pyarrow")
        from google.cloud.bigquery import job
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES
        from google.cloud.bigquery.schema import SchemaField

        client = self._make_client()

        records = [(3.14, [1, 2])]
        dataframe = pandas.DataFrame(
            data=records, columns=["float_column", "array_column"]
        )

        schema = [
            SchemaField("float_column", "FLOAT"),
            SchemaField(
                "array_column",
                "INTEGER",
                mode="REPEATED",
            ),
        ]
        job_config = job.LoadJobConfig(schema=schema)

        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )

        get_table_patch = mock.patch(
            "google.cloud.bigquery.client.Client.get_table",
            autospec=True,
            side_effect=google.api_core.exceptions.NotFound("Table not found"),
        )

        with load_patch as load_table_from_file, get_table_patch:
            client.load_table_from_dataframe(
                dataframe,
                self.TABLE_REF,
                job_config=job_config,
                location=self.LOCATION,
            )

        load_table_from_file.assert_called_once_with(
            client,
            mock.ANY,
            self.TABLE_REF,
            num_retries=_DEFAULT_NUM_RETRIES,
            rewind=True,
            size=mock.ANY,
            job_id=mock.ANY,
            job_id_prefix=None,
            location=self.LOCATION,
            project=None,
            job_config=mock.ANY,
            timeout=DEFAULT_TIMEOUT,
        )

        sent_config = load_table_from_file.mock_calls[0][2]["job_config"]
        assert sent_config.source_format == job.SourceFormat.PARQUET
        assert sent_config.schema == schema

    def test_load_table_from_dataframe_array_fields_w_auto_schema(self):
        """Test that a DataFrame with array columns can be uploaded correctly.

        See: https://github.com/googleapis/python-bigquery/issues/19
        """
        pandas = pytest.importorskip("pandas")
        pytest.importorskip("pyarrow")
        from google.cloud.bigquery import job
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES
        from google.cloud.bigquery.schema import SchemaField

        client = self._make_client()

        records = [(3.14, [1, 2])]
        dataframe = pandas.DataFrame(
            data=records, columns=["float_column", "array_column"]
        )

        expected_schema_googlesql = [
            SchemaField("float_column", "FLOAT"),
            SchemaField(
                "array_column",
                "INT64",
                mode="REPEATED",
            ),
        ]
        expected_schema_legacy_sql = [
            SchemaField("float_column", "FLOAT"),
            SchemaField(
                "array_column",
                "INTEGER",
                mode="REPEATED",
            ),
        ]

        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )

        get_table_patch = mock.patch(
            "google.cloud.bigquery.client.Client.get_table",
            autospec=True,
            side_effect=google.api_core.exceptions.NotFound("Table not found"),
        )

        with load_patch as load_table_from_file, get_table_patch:
            client.load_table_from_dataframe(
                dataframe,
                self.TABLE_REF,
                location=self.LOCATION,
            )

        load_table_from_file.assert_called_once_with(
            client,
            mock.ANY,
            self.TABLE_REF,
            num_retries=_DEFAULT_NUM_RETRIES,
            rewind=True,
            size=mock.ANY,
            job_id=mock.ANY,
            job_id_prefix=None,
            location=self.LOCATION,
            project=None,
            job_config=mock.ANY,
            timeout=DEFAULT_TIMEOUT,
        )

        sent_config = load_table_from_file.mock_calls[0][2]["job_config"]
        assert sent_config.source_format == job.SourceFormat.PARQUET
        assert (
            sent_config.schema == expected_schema_googlesql
            or sent_config.schema == expected_schema_legacy_sql
        )

    def test_load_table_from_dataframe_w_partial_schema(self):
        pandas = pytest.importorskip("pandas")
        pytest.importorskip("pyarrow")
        from google.cloud.bigquery import job
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES
        from google.cloud.bigquery.schema import SchemaField

        client = self._make_client()
        df_data = collections.OrderedDict(
            [
                ("int_col", [1, 2, 3]),
                ("int_as_float_col", [1.0, float("nan"), 3.0]),
                ("float_col", [1.0, 2.0, 3.0]),
                ("bool_col", [True, False, True]),
                (
                    "dt_col",
                    pandas.Series(
                        [
                            datetime.datetime(2010, 1, 2, 3, 44, 50),
                            datetime.datetime(2011, 2, 3, 14, 50, 59),
                            datetime.datetime(2012, 3, 14, 15, 16),
                        ],
                        dtype="datetime64[ns]",
                    ),
                ),
                (
                    "ts_col",
                    pandas.Series(
                        [
                            datetime.datetime(2010, 1, 2, 3, 44, 50),
                            datetime.datetime(2011, 2, 3, 14, 50, 59),
                            datetime.datetime(2012, 3, 14, 15, 16),
                        ],
                        dtype="datetime64[ns]",
                    ).dt.tz_localize(datetime.timezone.utc),
                ),
                ("string_col", ["abc", None, "def"]),
                ("bytes_col", [b"abc", b"def", None]),
            ]
        )
        dataframe = pandas.DataFrame(df_data, columns=df_data.keys())
        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )

        schema = (
            SchemaField("int_as_float_col", "INTEGER"),
            SchemaField("string_col", "STRING"),
            SchemaField("bytes_col", "BYTES"),
        )
        job_config = job.LoadJobConfig(schema=schema)
        with load_patch as load_table_from_file:
            client.load_table_from_dataframe(
                dataframe, self.TABLE_REF, job_config=job_config, location=self.LOCATION
            )

        load_table_from_file.assert_called_once_with(
            client,
            mock.ANY,
            self.TABLE_REF,
            num_retries=_DEFAULT_NUM_RETRIES,
            rewind=True,
            size=mock.ANY,
            job_id=mock.ANY,
            job_id_prefix=None,
            location=self.LOCATION,
            project=None,
            job_config=mock.ANY,
            timeout=DEFAULT_TIMEOUT,
        )

        sent_config = load_table_from_file.mock_calls[0][2]["job_config"]
        assert sent_config.source_format == job.SourceFormat.PARQUET
        assert tuple(sent_config.schema) == (
            SchemaField("int_col", "INTEGER"),
            SchemaField("int_as_float_col", "INTEGER"),
            SchemaField("float_col", "FLOAT"),
            SchemaField("bool_col", "BOOLEAN"),
            SchemaField("dt_col", "DATETIME"),
            SchemaField("ts_col", "TIMESTAMP"),
            SchemaField("string_col", "STRING"),
            SchemaField("bytes_col", "BYTES"),
        )

    def test_load_table_from_dataframe_w_partial_schema_extra_types(self):
        pandas = pytest.importorskip("pandas")
        pytest.importorskip("pyarrow")
        from google.cloud.bigquery import job
        from google.cloud.bigquery.schema import SchemaField

        client = self._make_client()
        df_data = collections.OrderedDict(
            [
                ("int_col", [1, 2, 3]),
                ("int_as_float_col", [1.0, float("nan"), 3.0]),
                ("string_col", ["abc", None, "def"]),
            ]
        )
        dataframe = pandas.DataFrame(df_data, columns=df_data.keys())
        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )

        schema = (
            SchemaField("int_as_float_col", "INTEGER"),
            SchemaField("string_col", "STRING"),
            SchemaField("unknown_col", "BYTES"),
        )
        job_config = job.LoadJobConfig(schema=schema)
        with (
            load_patch as load_table_from_file,
            pytest.raises(ValueError) as exc_context,
        ):
            client.load_table_from_dataframe(
                dataframe, self.TABLE_REF, job_config=job_config, location=self.LOCATION
            )

        load_table_from_file.assert_not_called()
        message = str(exc_context.value)
        assert "unknown_col" in message

    def test_load_table_from_dataframe_w_schema_arrow_custom_compression(self):
        pandas = pytest.importorskip("pandas")
        pytest.importorskip("pyarrow")
        from google.cloud.bigquery import job
        from google.cloud.bigquery.schema import SchemaField

        client = self._make_client()
        records = [{"name": "Monty", "age": 100}, {"name": "Python", "age": 60}]
        dataframe = pandas.DataFrame(records)
        schema = (SchemaField("name", "STRING"), SchemaField("age", "INTEGER"))
        job_config = job.LoadJobConfig(schema=schema)

        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )
        to_parquet_patch = mock.patch(
            "google.cloud.bigquery.client._pandas_helpers.dataframe_to_parquet",
            autospec=True,
        )

        with load_patch, to_parquet_patch as fake_to_parquet:
            client.load_table_from_dataframe(
                dataframe,
                self.TABLE_REF,
                job_config=job_config,
                location=self.LOCATION,
                parquet_compression="LZ4",
            )

        call_args = fake_to_parquet.call_args[1]
        assert call_args is not None
        assert call_args.get("parquet_compression") == "LZ4"

    def test_load_table_from_dataframe_wo_pyarrow_raises_error(self):
        pandas = pytest.importorskip("pandas")
        pytest.importorskip("pyarrow")
        client = self._make_client()
        records = [{"id": 1, "age": 100}, {"id": 2, "age": 60}]
        dataframe = pandas.DataFrame(records)

        get_table_patch = mock.patch(
            "google.cloud.bigquery.client.Client.get_table",
            autospec=True,
            side_effect=google.api_core.exceptions.NotFound("Table not found"),
        )
        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )
        pyarrow_patch = mock.patch("google.cloud.bigquery.client.pyarrow", None)
        to_parquet_patch = mock.patch.object(
            dataframe, "to_parquet", wraps=dataframe.to_parquet
        )

        with load_patch, get_table_patch, pyarrow_patch, to_parquet_patch:
            with pytest.raises(ValueError):
                client.load_table_from_dataframe(
                    dataframe,
                    self.TABLE_REF,
                    location=self.LOCATION,
                    parquet_compression="gzip",
                )

    def test_load_table_from_dataframe_w_bad_pyarrow_issues_warning(self):
        pandas = pytest.importorskip("pandas")
        pytest.importorskip("pyarrow")

        client = self._make_client()
        records = [{"id": 1, "age": 100}, {"id": 2, "age": 60}]
        dataframe = pandas.DataFrame(records)

        pyarrow_version_patch = mock.patch(
            "google.cloud.bigquery._versions_helpers.PYARROW_VERSIONS._installed_version",
            packaging.version.parse("2.0.0"),  # A known bad version of pyarrow.
        )
        get_table_patch = mock.patch(
            "google.cloud.bigquery.client.Client.get_table",
            autospec=True,
            side_effect=google.api_core.exceptions.NotFound("Table not found"),
        )
        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )

        with load_patch, get_table_patch, pyarrow_version_patch:
            with pytest.raises(exceptions.LegacyPyarrowError):
                client.load_table_from_dataframe(
                    dataframe,
                    self.TABLE_REF,
                    location=self.LOCATION,
                )

    def test_load_table_from_dataframe_w_nulls(self):
        """Test that a DataFrame with null columns can be uploaded if a
        BigQuery schema is specified.

        See: https://github.com/googleapis/google-cloud-python/issues/7370
        """
        pandas = pytest.importorskip("pandas")
        pytest.importorskip("pyarrow")
        from google.cloud.bigquery import job
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES
        from google.cloud.bigquery.schema import SchemaField

        client = self._make_client()
        records = [{"name": None, "age": None}, {"name": None, "age": None}]
        dataframe = pandas.DataFrame(records, columns=["name", "age"])
        schema = [SchemaField("name", "STRING"), SchemaField("age", "INTEGER")]
        job_config = job.LoadJobConfig(schema=schema)

        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )
        with load_patch as load_table_from_file:
            client.load_table_from_dataframe(
                dataframe, self.TABLE_REF, job_config=job_config, location=self.LOCATION
            )

        load_table_from_file.assert_called_once_with(
            client,
            mock.ANY,
            self.TABLE_REF,
            num_retries=_DEFAULT_NUM_RETRIES,
            rewind=True,
            size=mock.ANY,
            job_id=mock.ANY,
            job_id_prefix=None,
            location=self.LOCATION,
            project=None,
            job_config=mock.ANY,
            timeout=DEFAULT_TIMEOUT,
        )

        sent_config = load_table_from_file.mock_calls[0][2]["job_config"]
        assert sent_config.schema == schema
        assert sent_config.source_format == job.SourceFormat.PARQUET

    def test_load_table_from_dataframe_w_invaild_job_config(self):
        pandas = pytest.importorskip("pandas")
        from google.cloud.bigquery import job

        client = self._make_client()

        records = [{"float_column": 3.14, "struct_column": [{"foo": 1}, {"bar": -1}]}]
        dataframe = pandas.DataFrame(data=records)
        job_config = job.CopyJobConfig()

        with pytest.raises(TypeError) as exc:
            client.load_table_from_dataframe(
                dataframe, self.TABLE_REF, job_config=job_config, location=self.LOCATION
            )

        err_msg = str(exc.value)
        assert "Expected an instance of LoadJobConfig" in err_msg

    def test_load_table_from_dataframe_with_csv_source_format(self):
        pandas = pytest.importorskip("pandas")
        from google.cloud.bigquery import job
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES
        from google.cloud.bigquery.schema import SchemaField

        client = self._make_client()
        records = [{"id": 1, "age": 100}, {"id": 2, "age": 60}]
        dataframe = pandas.DataFrame(records)
        job_config = job.LoadJobConfig(
            write_disposition=job.WriteDisposition.WRITE_TRUNCATE,
            source_format=job.SourceFormat.CSV,
        )

        get_table_patch = mock.patch(
            "google.cloud.bigquery.client.Client.get_table",
            autospec=True,
            return_value=mock.Mock(
                schema=[SchemaField("id", "INTEGER"), SchemaField("age", "INTEGER")]
            ),
        )
        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )
        with load_patch as load_table_from_file, get_table_patch:
            client.load_table_from_dataframe(
                dataframe, self.TABLE_REF, job_config=job_config
            )

        load_table_from_file.assert_called_once_with(
            client,
            mock.ANY,
            self.TABLE_REF,
            num_retries=_DEFAULT_NUM_RETRIES,
            rewind=True,
            size=mock.ANY,
            job_id=mock.ANY,
            job_id_prefix=None,
            location=None,
            project=None,
            job_config=mock.ANY,
            timeout=DEFAULT_TIMEOUT,
        )

        sent_file = load_table_from_file.mock_calls[0][1][1]
        assert sent_file.closed

        sent_config = load_table_from_file.mock_calls[0][2]["job_config"]
        assert sent_config.source_format == job.SourceFormat.CSV

    def test_load_table_from_dataframe_with_csv_source_format_datetime_objects(self):
        pandas = pytest.importorskip("pandas")
        from google.cloud.bigquery import job
        from google.cloud.bigquery.schema import SchemaField

        client = self._make_client()
        schema = [
            SchemaField("dt_col", "DATETIME"),
            SchemaField("ts_col", "TIMESTAMP"),
            SchemaField("str_col", "STRING"),
        ]
        dataframe = pandas.DataFrame(
            {
                "dt_col": [
                    datetime.datetime(1, 1, 1, 0, 0, 0),
                    None,
                    pandas.NaT,
                    datetime.datetime(9999, 12, 31, 23, 59, 59, 999999),
                ],
                "ts_col": [
                    datetime.datetime(1, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc),
                    None,
                    "0002-01-01 00:00:00+00:00",
                    datetime.datetime(
                        9999, 12, 31, 23, 59, 59, 999999, tzinfo=datetime.timezone.utc
                    ),
                ],
                "str_col": ["a", None, "b", "c"],
            },
            dtype="object",
        )
        job_config = job.LoadJobConfig(
            schema=schema,
            source_format=job.SourceFormat.CSV,
        )

        captured_csv = []

        def fake_load_table_from_file(self_client, file_obj, *args, **kwargs):
            captured_csv.append(file_obj.read().decode("utf-8"))
            return mock.Mock()

        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file",
            autospec=True,
            side_effect=fake_load_table_from_file,
        )
        with load_patch:
            client.load_table_from_dataframe(
                dataframe, self.TABLE_REF, job_config=job_config
            )

        assert captured_csv == [
            "0001-01-01 00:00:00,0001-01-01 00:00:00+00:00,a\n"
            ",,\n"
            ",0002-01-01 00:00:00+00:00,b\n"
            "9999-12-31 23:59:59.999999,9999-12-31 23:59:59.999999+00:00,c\n"
        ]

    def test_load_table_from_dataframe_with_csv_source_format_no_schema(self):
        pandas = pytest.importorskip("pandas")
        from google.cloud.bigquery import job

        client = self._make_client()
        dataframe = pandas.DataFrame({"x": [object(), object()]})
        job_config = job.LoadJobConfig(
            write_disposition=job.WriteDisposition.WRITE_TRUNCATE,
            source_format=job.SourceFormat.CSV,
        )

        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )
        schema_patch = mock.patch(
            "google.cloud.bigquery._pandas_helpers.dataframe_to_bq_schema",
            autospec=True,
            return_value=None,
        )
        with (
            load_patch as load_table_from_file,
            schema_patch,
            pytest.warns(
                PendingDeprecationWarning,
                match="Schema could not be detected for all columns",
            ),
        ):
            client.load_table_from_dataframe(
                dataframe, self.TABLE_REF, job_config=job_config
            )

        load_table_from_file.assert_called_once()
        sent_config = load_table_from_file.mock_calls[0][2]["job_config"]
        assert sent_config.schema is None
        assert sent_config.source_format == job.SourceFormat.CSV

    def test_load_table_from_dataframe_w_higher_scale_decimal128_datatype(self):
        pandas = pytest.importorskip("pandas")
        pytest.importorskip("pyarrow")
        from decimal import Decimal

        from google.cloud.bigquery import job
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES
        from google.cloud.bigquery.schema import SchemaField

        client = self._make_client()
        dataframe = pandas.DataFrame({"x": [Decimal("0.1234567891")]})
        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )

        get_table_patch = mock.patch(
            "google.cloud.bigquery.client.Client.get_table", autospec=True
        )
        with load_patch as load_table_from_file, get_table_patch:
            client.load_table_from_dataframe(
                dataframe, self.TABLE_REF, location=self.LOCATION
            )

        load_table_from_file.assert_called_once_with(
            client,
            mock.ANY,
            self.TABLE_REF,
            num_retries=_DEFAULT_NUM_RETRIES,
            rewind=True,
            size=mock.ANY,
            job_id=mock.ANY,
            job_id_prefix=None,
            location=self.LOCATION,
            project=None,
            job_config=mock.ANY,
            timeout=DEFAULT_TIMEOUT,
        )

        sent_config = load_table_from_file.mock_calls[0][2]["job_config"]
        assert sent_config.source_format == job.SourceFormat.PARQUET
        assert tuple(sent_config.schema) == (
            SchemaField("x", "BIGNUMERIC", "NULLABLE", None),
        )

    def test_load_table_from_dataframe_emits_pending_deprecation_warning(self):
        pandas = pytest.importorskip("pandas")
        pytest.importorskip("pyarrow")

        client = self._make_client()
        dataframe = pandas.DataFrame({"x": [1, 2, 3]})

        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )
        get_table_patch = mock.patch(
            "google.cloud.bigquery.client.Client.get_table", autospec=True
        )
        with (
            load_patch,
            get_table_patch,
            pytest.warns(
                PendingDeprecationWarning,
                match="Loading DataFrames via google-cloud-bigquery is deprecated",
            ),
        ):
            client.load_table_from_dataframe(dataframe, self.TABLE_REF)

    # With autodetect specified, we pass the value as is. For more info, see
    # https://github.com/googleapis/python-bigquery/issues/1228#issuecomment-1910946297
    def test_load_table_from_json_basic_use(self):
        from google.cloud.bigquery import job
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES

        client = self._make_client()

        json_rows = [
            {"name": "One", "age": 11, "birthday": "2008-09-10", "adult": False},
            {"name": "Two", "age": 22, "birthday": "1997-08-09", "adult": True},
        ]

        job_config = job.LoadJobConfig(autodetect=True)

        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )

        # mock: remote table already exists
        get_table_reference = {
            "projectId": "project_id",
            "datasetId": "test_dataset",
            "tableId": "test_table",
        }
        get_table_patch = mock.patch(
            "google.cloud.bigquery.client.Client.get_table",
            autospec=True,
            return_value=mock.Mock(table_reference=get_table_reference),
        )

        with load_patch as load_table_from_file, get_table_patch:
            client.load_table_from_json(
                json_rows, self.TABLE_REF, job_config=job_config
            )

        load_table_from_file.assert_called_once_with(
            client,
            mock.ANY,
            self.TABLE_REF,
            size=mock.ANY,
            num_retries=_DEFAULT_NUM_RETRIES,
            job_id=mock.ANY,
            job_id_prefix=None,
            location=client.location,
            project=client.project,
            job_config=mock.ANY,
            timeout=DEFAULT_TIMEOUT,
        )

        sent_config = load_table_from_file.mock_calls[0][2]["job_config"]
        assert sent_config.source_format == job.SourceFormat.NEWLINE_DELIMITED_JSON
        assert sent_config.schema is None
        assert sent_config.autodetect

    def test_load_table_from_json_non_default_args(self):
        from google.cloud.bigquery import job
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES
        from google.cloud.bigquery.schema import SchemaField

        client = self._make_client()

        json_rows = [
            {"name": "One", "age": 11, "birthday": "2008-09-10", "adult": False},
            {"name": "Two", "age": 22, "birthday": "1997-08-09", "adult": True},
        ]

        schema = [
            SchemaField("name", "STRING"),
            SchemaField("age", "INTEGER"),
            SchemaField("adult", "BOOLEAN"),
        ]
        job_config = job.LoadJobConfig(schema=schema)
        job_config._properties["load"]["unknown_field"] = "foobar"
        original_config_copy = copy.deepcopy(job_config)

        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )

        with load_patch as load_table_from_file:
            client.load_table_from_json(
                json_rows,
                self.TABLE_REF,
                job_config=job_config,
                project="project-x",
                location="EU",
            )

        load_table_from_file.assert_called_once_with(
            client,
            mock.ANY,
            self.TABLE_REF,
            size=mock.ANY,
            num_retries=_DEFAULT_NUM_RETRIES,
            job_id=mock.ANY,
            job_id_prefix=None,
            location="EU",
            project="project-x",
            job_config=mock.ANY,
            timeout=DEFAULT_TIMEOUT,
        )

        sent_config = load_table_from_file.mock_calls[0][2]["job_config"]
        assert sent_config.source_format == job.SourceFormat.NEWLINE_DELIMITED_JSON
        assert sent_config.schema == schema
        assert not sent_config.autodetect
        # all properties should have been cloned and sent to the backend
        assert sent_config._properties.get("load", {}).get("unknown_field") == "foobar"

        # the original config object should not have been modified
        assert job_config.to_api_repr() == original_config_copy.to_api_repr()

    def test_load_table_from_json_w_invalid_job_config(self):
        from google.cloud.bigquery import job

        client = self._make_client()
        json_rows = [
            {"name": "One", "age": 11, "birthday": "2008-09-10", "adult": False},
            {"name": "Two", "age": 22, "birthday": "1997-08-09", "adult": True},
        ]
        job_config = job.CopyJobConfig()
        with pytest.raises(TypeError) as exc:
            client.load_table_from_json(
                json_rows,
                self.TABLE_REF,
                job_config=job_config,
                project="project-x",
                location="EU",
            )
        err_msg = str(exc.value)
        assert "Expected an instance of LoadJobConfig" in err_msg

    # When all following are true:
    # (1) no schema provided;
    # (2) no autodetect value provided;
    # (3) writeDisposition == WRITE_APPEND or None;
    # (4) table already exists,
    # client sets autodetect == False
    # For more details, see https://github.com/googleapis/python-bigquery/issues/1228#issuecomment-1910946297
    def test_load_table_from_json_wo_schema_wo_autodetect_write_append_w_table(self):
        from google.cloud.bigquery import job
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES
        from google.cloud.bigquery.job import WriteDisposition

        client = self._make_client()

        json_rows = [
            {"name": "One", "age": 11, "birthday": "2008-09-10", "adult": False},
            {"name": "Two", "age": 22, "birthday": "1997-08-09", "adult": True},
        ]

        job_config = job.LoadJobConfig(write_disposition=WriteDisposition.WRITE_APPEND)

        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )

        # mock: remote table already exists
        get_table_reference = {
            "projectId": "project_id",
            "datasetId": "test_dataset",
            "tableId": "test_table",
        }
        get_table_patch = mock.patch(
            "google.cloud.bigquery.client.Client.get_table",
            autospec=True,
            return_value=mock.Mock(table_reference=get_table_reference),
        )

        with load_patch as load_table_from_file, get_table_patch:
            client.load_table_from_json(
                json_rows, self.TABLE_REF, job_config=job_config
            )

        load_table_from_file.assert_called_once_with(
            client,
            mock.ANY,
            self.TABLE_REF,
            size=mock.ANY,
            num_retries=_DEFAULT_NUM_RETRIES,
            job_id=mock.ANY,
            job_id_prefix=None,
            location=client.location,
            project=client.project,
            job_config=mock.ANY,
            timeout=DEFAULT_TIMEOUT,
        )

        sent_config = load_table_from_file.mock_calls[0][2]["job_config"]
        assert sent_config.source_format == job.SourceFormat.NEWLINE_DELIMITED_JSON
        assert sent_config.schema is None
        assert not sent_config.autodetect

    # When all following are true:
    # (1) no schema provided;
    # (2) no autodetect value provided;
    # (3) writeDisposition == WRITE_APPEND or None;
    # (4) table does NOT exist,
    # client sets autodetect == True
    # For more details, see https://github.com/googleapis/python-bigquery/issues/1228#issuecomment-1910946297
    def test_load_table_from_json_wo_schema_wo_autodetect_write_append_wo_table(self):
        import google.api_core.exceptions as core_exceptions
        from google.cloud.bigquery import job
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES
        from google.cloud.bigquery.job import WriteDisposition

        client = self._make_client()

        json_rows = [
            {"name": "One", "age": 11, "birthday": "2008-09-10", "adult": False},
            {"name": "Two", "age": 22, "birthday": "1997-08-09", "adult": True},
        ]

        job_config = job.LoadJobConfig(write_disposition=WriteDisposition.WRITE_APPEND)

        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )

        # mock: remote table doesn't exist
        get_table_patch = mock.patch(
            "google.cloud.bigquery.client.Client.get_table",
            autospec=True,
            side_effect=core_exceptions.NotFound(""),
        )

        with load_patch as load_table_from_file, get_table_patch:
            client.load_table_from_json(
                json_rows, self.TABLE_REF, job_config=job_config
            )

        load_table_from_file.assert_called_once_with(
            client,
            mock.ANY,
            self.TABLE_REF,
            size=mock.ANY,
            num_retries=_DEFAULT_NUM_RETRIES,
            job_id=mock.ANY,
            job_id_prefix=None,
            location=client.location,
            project=client.project,
            job_config=mock.ANY,
            timeout=DEFAULT_TIMEOUT,
        )

        sent_config = load_table_from_file.mock_calls[0][2]["job_config"]
        assert sent_config.source_format == job.SourceFormat.NEWLINE_DELIMITED_JSON
        assert sent_config.schema is None
        assert sent_config.autodetect

    # When all following are true:
    # (1) no schema provided;
    # (2) no autodetect value provided;
    # (3) writeDisposition == WRITE_TRUNCATE or WRITE_EMPTY;
    # client sets autodetect == True
    # For more details, see https://github.com/googleapis/python-bigquery/issues/1228#issuecomment-1910946297
    def test_load_table_from_json_wo_schema_wo_autodetect_others(self):
        from google.cloud.bigquery import job
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES
        from google.cloud.bigquery.job import WriteDisposition

        client = self._make_client()

        json_rows = [
            {"name": "One", "age": 11, "birthday": "2008-09-10", "adult": False},
            {"name": "Two", "age": 22, "birthday": "1997-08-09", "adult": True},
        ]

        job_config = job.LoadJobConfig(
            write_disposition=WriteDisposition.WRITE_TRUNCATE
        )

        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )

        with load_patch as load_table_from_file:
            client.load_table_from_json(
                json_rows, self.TABLE_REF, job_config=job_config
            )

        load_table_from_file.assert_called_once_with(
            client,
            mock.ANY,
            self.TABLE_REF,
            size=mock.ANY,
            num_retries=_DEFAULT_NUM_RETRIES,
            job_id=mock.ANY,
            job_id_prefix=None,
            location=client.location,
            project=client.project,
            job_config=mock.ANY,
            timeout=DEFAULT_TIMEOUT,
        )

        sent_config = load_table_from_file.mock_calls[0][2]["job_config"]
        assert sent_config.source_format == job.SourceFormat.NEWLINE_DELIMITED_JSON
        assert sent_config.schema is None
        assert sent_config.autodetect

    def test_load_table_from_json_w_explicit_job_config_override(self):
        from google.cloud.bigquery import job
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES
        from google.cloud.bigquery.schema import SchemaField

        client = self._make_client()

        json_rows = [
            {"name": "One", "age": 11, "birthday": "2008-09-10", "adult": False},
            {"name": "Two", "age": 22, "birthday": "1997-08-09", "adult": True},
        ]

        schema = [
            SchemaField("name", "STRING"),
            SchemaField("age", "INTEGER"),
            SchemaField("adult", "BOOLEAN"),
        ]
        client.default_load_job_config = job.LoadJobConfig(
            schema=schema, encoding="ISO-8859-1"
        )

        override_schema = schema
        override_schema[0] = SchemaField("username", "STRING")
        job_config = job.LoadJobConfig(schema=override_schema)
        original_config_copy = copy.deepcopy(job_config)

        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )

        with load_patch as load_table_from_file:
            client.load_table_from_json(
                json_rows,
                self.TABLE_REF,
                job_config=job_config,
                project="project-x",
                location="EU",
            )

        load_table_from_file.assert_called_once_with(
            client,
            mock.ANY,
            self.TABLE_REF,
            size=mock.ANY,
            num_retries=_DEFAULT_NUM_RETRIES,
            job_id=mock.ANY,
            job_id_prefix=None,
            location="EU",
            project="project-x",
            job_config=mock.ANY,
            timeout=DEFAULT_TIMEOUT,
        )

        sent_config = load_table_from_file.mock_calls[0][2]["job_config"]
        assert sent_config.source_format == job.SourceFormat.NEWLINE_DELIMITED_JSON
        assert sent_config.schema == override_schema
        assert sent_config.encoding == "ISO-8859-1"
        assert not sent_config.autodetect

        # the original config object should not have been modified
        assert job_config.to_api_repr() == original_config_copy.to_api_repr()

    def test_load_table_from_json_w_default_job_config(self):
        from google.cloud.bigquery import job
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES
        from google.cloud.bigquery.schema import SchemaField

        client = self._make_client()

        json_rows = [
            {"name": "One", "age": 11, "birthday": "2008-09-10", "adult": False},
            {"name": "Two", "age": 22, "birthday": "1997-08-09", "adult": True},
        ]

        schema = [
            SchemaField("name", "STRING"),
            SchemaField("age", "INTEGER"),
            SchemaField("adult", "BOOLEAN"),
        ]
        client.default_load_job_config = job.LoadJobConfig(schema=schema)

        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )

        with load_patch as load_table_from_file:
            client.load_table_from_json(
                json_rows,
                self.TABLE_REF,
                job_config=None,
                project="project-x",
                location="EU",
            )

        load_table_from_file.assert_called_once_with(
            client,
            mock.ANY,
            self.TABLE_REF,
            size=mock.ANY,
            num_retries=_DEFAULT_NUM_RETRIES,
            job_id=mock.ANY,
            job_id_prefix=None,
            location="EU",
            project="project-x",
            job_config=mock.ANY,
            timeout=DEFAULT_TIMEOUT,
        )

        sent_config = load_table_from_file.mock_calls[0][2]["job_config"]
        assert sent_config.source_format == job.SourceFormat.NEWLINE_DELIMITED_JSON
        assert sent_config.schema == schema

    def test_load_table_from_json_unicode_emoji_data_case(self):
        from google.cloud.bigquery.client import _DEFAULT_NUM_RETRIES

        client = self._make_client()

        emoji = "\U0001f3e6"
        json_row = {"emoji": emoji}
        json_rows = [json_row]

        load_patch = mock.patch(
            "google.cloud.bigquery.client.Client.load_table_from_file", autospec=True
        )
        # mock: remote table already exists
        get_table_reference = {
            "projectId": "project_id",
            "datasetId": "test_dataset",
            "tableId": "test_table",
        }
        get_table_patch = mock.patch(
            "google.cloud.bigquery.client.Client.get_table",
            autospec=True,
            return_value=mock.Mock(table_reference=get_table_reference),
        )

        with load_patch as load_table_from_file, get_table_patch:
            client.load_table_from_json(json_rows, self.TABLE_REF)

        load_table_from_file.assert_called_once_with(
            client,
            mock.ANY,
            self.TABLE_REF,
            size=mock.ANY,
            num_retries=_DEFAULT_NUM_RETRIES,
            job_id=mock.ANY,
            job_id_prefix=None,
            location=client.location,
            project=client.project,
            job_config=mock.ANY,
            timeout=DEFAULT_TIMEOUT,
        )

        sent_data_file = load_table_from_file.mock_calls[0][1][1]

        # make sure json_row's unicode characters are only encoded one time
        expected_bytes = b'{"emoji": "' + emoji.encode("utf8") + b'"}'
        assert sent_data_file.getvalue() == expected_bytes

    # Low-level tests
    def test_schema_from_json_with_file_object(self):
        from google.cloud.bigquery.schema import SchemaField

        file_content = """[
          {
            "description": "quarter",
            "mode": "REQUIRED",
            "name": "qtr",
            "type": "STRING"
          },
          {
            "description": "sales representative",
            "mode": "NULLABLE",
            "name": "rep",
            "type": "STRING"
          },
          {
            "description": "total sales",
            "mode": "NULLABLE",
            "name": "sales",
            "type": "FLOAT"
          }
        ]"""

        expected = [
            SchemaField("qtr", "STRING", "REQUIRED", description="quarter"),
            SchemaField(
                "rep", "STRING", "NULLABLE", description="sales representative"
            ),
            SchemaField("sales", "FLOAT", "NULLABLE", description="total sales"),
        ]

        client = self._make_client()
        fake_file = io.StringIO(file_content)
        actual = client.schema_from_json(fake_file)

        assert expected == actual

    def test_schema_to_json_with_file_path(self):
        from google.cloud.bigquery.schema import SchemaField

        file_content = [
            {
                "description": "quarter",
                "mode": "REQUIRED",
                "name": "qtr",
                "type": "STRING",
            },
            {
                "description": "sales representative",
                "mode": "NULLABLE",
                "name": "rep",
                "type": "STRING",
            },
            {
                "description": "total sales",
                "mode": "NULLABLE",
                "name": "sales",
                "type": "FLOAT",
            },
        ]

        schema_list = [
            SchemaField("qtr", "STRING", "REQUIRED", description="quarter"),
            SchemaField(
                "rep", "STRING", "NULLABLE", description="sales representative"
            ),
            SchemaField("sales", "FLOAT", "NULLABLE", description="total sales"),
        ]

        client = self._make_client()
        mock_file_path = "/mocked/file.json"
        open_patch = mock.patch("builtins.open", mock.mock_open())

        with open_patch as mock_file, mock.patch("json.dump") as mock_dump:
            client.schema_to_json(schema_list, mock_file_path)
            mock_file.assert_called_once_with(mock_file_path, mode="w")
            # This assert is to make sure __exit__ is called in the context
            # manager that opens the file in the function
            mock_file().__exit__.assert_called_once()
            mock_dump.assert_called_with(
                file_content, mock_file.return_value, indent=2, sort_keys=True
            )

    def test_schema_to_json_with_file_object(self):
        from google.cloud.bigquery.schema import SchemaField

        file_content = [
            {
                "description": "quarter",
                "mode": "REQUIRED",
                "name": "qtr",
                "type": "STRING",
            },
            {
                "description": "sales representative",
                "mode": "NULLABLE",
                "name": "rep",
                "type": "STRING",
            },
            {
                "description": "total sales",
                "mode": "NULLABLE",
                "name": "sales",
                "type": "FLOAT",
            },
        ]

        schema_list = [
            SchemaField("qtr", "STRING", "REQUIRED", description="quarter"),
            SchemaField(
                "rep", "STRING", "NULLABLE", description="sales representative"
            ),
            SchemaField("sales", "FLOAT", "NULLABLE", description="total sales"),
        ]

        fake_file = io.StringIO()

        client = self._make_client()

        client.schema_to_json(schema_list, fake_file)
        assert file_content == json.loads(fake_file.getvalue())


def test_upload_chunksize(client):
    with mock.patch("google.cloud.bigquery.client.ResumableUpload") as RU:
        upload = RU.return_value

        upload.finished = False

        def transmit_next_chunk(transport, *args, **kwargs):
            upload.finished = True
            result = mock.MagicMock()
            result.json.return_value = {}
            return result

        upload.transmit_next_chunk = transmit_next_chunk
        f = io.BytesIO()
        client.load_table_from_file(f, "foo.bar")

        chunk_size = RU.call_args_list[0][0][1]
        assert chunk_size == 100 * (1 << 20)


@pytest.mark.enable_add_server_timeout_header
@pytest.mark.parametrize("headers", [None, {}])
def test__call_api_add_server_timeout_w_timeout(client, headers):
    client._connection = make_connection({})
    client._call_api(None, method="GET", path="/", headers=headers, timeout=42)
    client._connection.api_request.assert_called_with(
        method="GET", path="/", timeout=42, headers={"X-Server-Timeout": "42"}
    )


@pytest.mark.enable_add_server_timeout_header
def test__call_api_no_add_server_timeout_wo_timeout(client):
    client._connection = make_connection({})
    client._call_api(None, method="GET", path="/")
    client._connection.api_request.assert_called_with(method="GET", path="/")
