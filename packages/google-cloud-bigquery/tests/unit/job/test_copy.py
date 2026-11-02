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

from unittest import mock

from ..helpers import make_connection

from .helpers import _Base
from .helpers import _make_client

import datetime


class TestCopyJobConfig(_Base):
    JOB_TYPE = "copy"

    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.job import CopyJobConfig

        return CopyJobConfig

    def test_ctor_defaults(self):
        from google.cloud.bigquery.job import OperationType

        config = self._make_one()

        assert config.create_disposition is None
        assert config.write_disposition is None
        assert config.destination_expiration_time is None
        assert config.destination_encryption_configuration is None
        assert config.operation_type == OperationType.OPERATION_TYPE_UNSPECIFIED

    def test_ctor_w_properties(self):
        from google.cloud.bigquery.job import CreateDisposition
        from google.cloud.bigquery.job import OperationType
        from google.cloud.bigquery.job import WriteDisposition

        create_disposition = CreateDisposition.CREATE_NEVER
        write_disposition = WriteDisposition.WRITE_TRUNCATE
        snapshot_operation = OperationType.SNAPSHOT

        today = datetime.date.today()
        destination_expiration_time = f"{today.year + 1}-01-01T00:00:00Z"

        config = self._get_target_class()(
            create_disposition=create_disposition,
            write_disposition=write_disposition,
            operation_type=snapshot_operation,
            destination_expiration_time=destination_expiration_time,
        )

        self.assertEqual(config.create_disposition, create_disposition)
        self.assertEqual(config.write_disposition, write_disposition)
        self.assertEqual(config.operation_type, snapshot_operation)
        self.assertEqual(
            config.destination_expiration_time, destination_expiration_time
        )

    def test_to_api_repr_with_encryption(self):
        from google.cloud.bigquery.encryption_configuration import (
            EncryptionConfiguration,
        )

        config = self._make_one()
        config.destination_encryption_configuration = EncryptionConfiguration(
            kms_key_name=self.KMS_KEY_NAME
        )
        resource = config.to_api_repr()
        self.assertEqual(
            resource,
            {
                "copy": {
                    "destinationEncryptionConfiguration": {
                        "kmsKeyName": self.KMS_KEY_NAME
                    }
                }
            },
        )

    def test_to_api_repr_with_encryption_none(self):
        config = self._make_one()
        config.destination_encryption_configuration = None
        resource = config.to_api_repr()
        self.assertEqual(
            resource, {"copy": {"destinationEncryptionConfiguration": None}}
        )

    def test_operation_type_setting_none(self):
        from google.cloud.bigquery.job import OperationType

        config = self._make_one(operation_type=OperationType.SNAPSHOT)

        # Setting it to None is the same as setting it to OPERATION_TYPE_UNSPECIFIED.
        config.operation_type = None
        assert config.operation_type == OperationType.OPERATION_TYPE_UNSPECIFIED

    def test_operation_type_setting_non_none(self):
        from google.cloud.bigquery.job import OperationType

        config = self._make_one(operation_type=None)
        config.operation_type = OperationType.RESTORE
        assert config.operation_type == OperationType.RESTORE


class TestCopyJob(_Base):
    JOB_TYPE = "copy"
    SOURCE_TABLE = "source_table"
    DESTINATION_TABLE = "destination_table"

    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.job import CopyJob

        return CopyJob

    def _make_resource(self, started=False, ended=False):
        resource = super(TestCopyJob, self)._make_resource(started, ended)
        config = resource["configuration"]["copy"]
        config["sourceTables"] = [
            {
                "projectId": self.PROJECT,
                "datasetId": self.DS_ID,
                "tableId": self.SOURCE_TABLE,
            }
        ]
        config["destinationTable"] = {
            "projectId": self.PROJECT,
            "datasetId": self.DS_ID,
            "tableId": self.DESTINATION_TABLE,
        }

        return resource

    def _verifyResourceProperties(self, job, resource):
        self._verifyReadonlyResourceProperties(job, resource)

        config = resource.get("configuration", {}).get("copy")
        table_ref = config["destinationTable"]
        self.assertEqual(job.destination.project, table_ref["projectId"])
        self.assertEqual(job.destination.dataset_id, table_ref["datasetId"])
        self.assertEqual(job.destination.table_id, table_ref["tableId"])

        sources = config.get("sourceTables")
        if sources is None:
            sources = [config["sourceTable"]]
        self.assertEqual(len(sources), len(job.sources))
        for table_ref, table in zip(sources, job.sources):
            self.assertEqual(table.project, table_ref["projectId"])
            self.assertEqual(table.dataset_id, table_ref["datasetId"])
            self.assertEqual(table.table_id, table_ref["tableId"])

        if "createDisposition" in config:
            self.assertEqual(job.create_disposition, config["createDisposition"])
        else:
            self.assertIsNone(job.create_disposition)

        if "writeDisposition" in config:
            self.assertEqual(job.write_disposition, config["writeDisposition"])
        else:
            self.assertIsNone(job.write_disposition)

        if "destinationEncryptionConfiguration" in config:
            self.assertIsNotNone(job.destination_encryption_configuration)
            self.assertEqual(
                job.destination_encryption_configuration.kms_key_name,
                config["destinationEncryptionConfiguration"]["kmsKeyName"],
            )
        else:
            self.assertIsNone(job.destination_encryption_configuration)

    def test_ctor(self):
        client = _make_client(project=self.PROJECT)
        source = self._table_ref(self.SOURCE_TABLE)
        destination = self._table_ref(self.DESTINATION_TABLE)
        job = self._make_one(self.JOB_ID, [source], destination, client)
        self.assertEqual(job.destination, destination)
        self.assertEqual(job.sources, [source])
        self.assertIs(job._client, client)
        self.assertEqual(job.job_type, self.JOB_TYPE)
        self.assertEqual(job.path, "/projects/%s/jobs/%s" % (self.PROJECT, self.JOB_ID))

        self._verifyInitialReadonlyProperties(job)

        # set/read from resource['configuration']['copy']
        self.assertIsNone(job.create_disposition)
        self.assertIsNone(job.write_disposition)
        self.assertIsNone(job.destination_encryption_configuration)

    def test_from_api_repr_missing_identity(self):
        self._setUpConstants()
        client = _make_client(project=self.PROJECT)
        RESOURCE = {}
        klass = self._get_target_class()
        with self.assertRaises(KeyError):
            klass.from_api_repr(RESOURCE, client=client)

    def test_from_api_repr_missing_config(self):
        self._setUpConstants()
        client = _make_client(project=self.PROJECT)
        RESOURCE = {
            "id": "%s:%s" % (self.PROJECT, self.DS_ID),
            "jobReference": {"projectId": self.PROJECT, "jobId": self.JOB_ID},
        }
        klass = self._get_target_class()
        with self.assertRaises(KeyError):
            klass.from_api_repr(RESOURCE, client=client)

    def test_from_api_repr_bare(self):
        self._setUpConstants()
        client = _make_client(project=self.PROJECT)
        RESOURCE = {
            "id": self.JOB_ID,
            "jobReference": {"projectId": self.PROJECT, "jobId": self.JOB_ID},
            "configuration": {
                "copy": {
                    "sourceTables": [
                        {
                            "projectId": self.PROJECT,
                            "datasetId": self.DS_ID,
                            "tableId": self.SOURCE_TABLE,
                        }
                    ],
                    "destinationTable": {
                        "projectId": self.PROJECT,
                        "datasetId": self.DS_ID,
                        "tableId": self.DESTINATION_TABLE,
                    },
                }
            },
        }
        klass = self._get_target_class()
        job = klass.from_api_repr(RESOURCE, client=client)
        self.assertIs(job._client, client)
        self._verifyResourceProperties(job, RESOURCE)

    def test_from_api_with_encryption(self):
        self._setUpConstants()
        client = _make_client(project=self.PROJECT)
        RESOURCE = {
            "id": self.JOB_ID,
            "jobReference": {"projectId": self.PROJECT, "jobId": self.JOB_ID},
            "configuration": {
                "copy": {
                    "sourceTables": [
                        {
                            "projectId": self.PROJECT,
                            "datasetId": self.DS_ID,
                            "tableId": self.SOURCE_TABLE,
                        }
                    ],
                    "destinationTable": {
                        "projectId": self.PROJECT,
                        "datasetId": self.DS_ID,
                        "tableId": self.DESTINATION_TABLE,
                    },
                    "destinationEncryptionConfiguration": {
                        "kmsKeyName": self.KMS_KEY_NAME
                    },
                }
            },
        }
        klass = self._get_target_class()
        job = klass.from_api_repr(RESOURCE, client=client)
        self.assertIs(job._client, client)
        self._verifyResourceProperties(job, RESOURCE)

    def test_from_api_repr_w_sourcetable(self):
        self._setUpConstants()
        client = _make_client(project=self.PROJECT)
        RESOURCE = {
            "id": self.JOB_ID,
            "jobReference": {"projectId": self.PROJECT, "jobId": self.JOB_ID},
            "configuration": {
                "copy": {
                    "sourceTable": {
                        "projectId": self.PROJECT,
                        "datasetId": self.DS_ID,
                        "tableId": self.SOURCE_TABLE,
                    },
                    "destinationTable": {
                        "projectId": self.PROJECT,
                        "datasetId": self.DS_ID,
                        "tableId": self.DESTINATION_TABLE,
                    },
                }
            },
        }
        klass = self._get_target_class()
        job = klass.from_api_repr(RESOURCE, client=client)
        self.assertIs(job._client, client)
        self._verifyResourceProperties(job, RESOURCE)

    def test_from_api_repr_wo_sources(self):
        self._setUpConstants()
        client = _make_client(project=self.PROJECT)
        RESOURCE = {
            "id": self.JOB_ID,
            "jobReference": {"projectId": self.PROJECT, "jobId": self.JOB_ID},
            "configuration": {
                "copy": {
                    "destinationTable": {
                        "projectId": self.PROJECT,
                        "datasetId": self.DS_ID,
                        "tableId": self.DESTINATION_TABLE,
                    }
                }
            },
        }
        klass = self._get_target_class()
        job = klass.from_api_repr(RESOURCE, client=client)
        with self.assertRaises(KeyError):
            _ = job.sources

    def test_from_api_repr_w_properties(self):
        from google.cloud.bigquery.job import CreateDisposition

        client = _make_client(project=self.PROJECT)
        RESOURCE = self._make_resource()
        copy_config = RESOURCE["configuration"]["copy"]
        copy_config["createDisposition"] = CreateDisposition.CREATE_IF_NEEDED
        klass = self._get_target_class()
        job = klass.from_api_repr(RESOURCE, client=client)
        self.assertIs(job._client, client)
        self._verifyResourceProperties(job, RESOURCE)

    def test_begin_w_bound_client(self):
        PATH = "/projects/%s/jobs" % (self.PROJECT,)
        RESOURCE = self._make_resource()
        # Ensure None for missing server-set props
        del RESOURCE["statistics"]["creationTime"]
        del RESOURCE["etag"]
        del RESOURCE["selfLink"]
        del RESOURCE["user_email"]
        conn = make_connection(RESOURCE)
        client = _make_client(project=self.PROJECT, connection=conn)
        source = self._table_ref(self.SOURCE_TABLE)
        destination = self._table_ref(self.DESTINATION_TABLE)
        job = self._make_one(self.JOB_ID, [source], destination, client)
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            job._begin()

        final_attributes.assert_called_with({"path": PATH}, client, job)

        conn.api_request.assert_called_once_with(
            method="POST",
            path=PATH,
            data={
                "jobReference": {"projectId": self.PROJECT, "jobId": self.JOB_ID},
                "configuration": {
                    "copy": {
                        "sourceTables": [
                            {
                                "projectId": self.PROJECT,
                                "datasetId": self.DS_ID,
                                "tableId": self.SOURCE_TABLE,
                            }
                        ],
                        "destinationTable": {
                            "projectId": self.PROJECT,
                            "datasetId": self.DS_ID,
                            "tableId": self.DESTINATION_TABLE,
                        },
                    }
                },
            },
            timeout=None,
        )
        self._verifyResourceProperties(job, RESOURCE)

    def test_begin_w_alternate_client(self):
        from google.cloud.bigquery.job import CopyJobConfig

        from google.cloud.bigquery.job import CreateDisposition
        from google.cloud.bigquery.job import WriteDisposition

        PATH = "/projects/%s/jobs" % (self.PROJECT,)
        RESOURCE = self._make_resource(ended=True)
        COPY_CONFIGURATION = {
            "sourceTables": [
                {
                    "projectId": self.PROJECT,
                    "datasetId": self.DS_ID,
                    "tableId": self.SOURCE_TABLE,
                }
            ],
            "destinationTable": {
                "projectId": self.PROJECT,
                "datasetId": self.DS_ID,
                "tableId": self.DESTINATION_TABLE,
            },
            "createDisposition": CreateDisposition.CREATE_NEVER,
            "writeDisposition": WriteDisposition.WRITE_TRUNCATE,
        }
        RESOURCE["configuration"]["copy"] = COPY_CONFIGURATION
        conn1 = make_connection()
        client1 = _make_client(project=self.PROJECT, connection=conn1)
        conn2 = make_connection(RESOURCE)
        client2 = _make_client(project=self.PROJECT, connection=conn2)
        source = self._table_ref(self.SOURCE_TABLE)
        destination = self._table_ref(self.DESTINATION_TABLE)
        config = CopyJobConfig()
        config.create_disposition = CreateDisposition.CREATE_NEVER
        config.write_disposition = WriteDisposition.WRITE_TRUNCATE
        job = self._make_one(self.JOB_ID, [source], destination, client1, config)
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            job._begin(client=client2)

        final_attributes.assert_called_with({"path": PATH}, client2, job)

        conn1.api_request.assert_not_called()
        conn2.api_request.assert_called_once_with(
            method="POST",
            path=PATH,
            data={
                "jobReference": {"projectId": self.PROJECT, "jobId": self.JOB_ID},
                "configuration": {"copy": COPY_CONFIGURATION},
            },
            timeout=None,
        )
        self._verifyResourceProperties(job, RESOURCE)

    def test_exists_miss_w_bound_client(self):
        PATH = "/projects/%s/jobs/%s" % (self.PROJECT, self.JOB_ID)
        conn = make_connection()
        client = _make_client(project=self.PROJECT, connection=conn)

        source = self._table_ref(self.SOURCE_TABLE)
        destination = self._table_ref(self.DESTINATION_TABLE)
        job = self._make_one(self.JOB_ID, [source], destination, client)
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            self.assertFalse(job.exists())

        final_attributes.assert_called_with({"path": PATH}, client, job)

        conn.api_request.assert_called_once_with(
            method="GET", path=PATH, query_params={"fields": "id"}, timeout=None
        )

    def test_exists_hit_w_alternate_client(self):
        PATH = "/projects/%s/jobs/%s" % (self.PROJECT, self.JOB_ID)
        conn1 = make_connection()
        client1 = _make_client(project=self.PROJECT, connection=conn1)
        conn2 = make_connection({})
        client2 = _make_client(project=self.PROJECT, connection=conn2)
        source = self._table_ref(self.SOURCE_TABLE)
        destination = self._table_ref(self.DESTINATION_TABLE)
        job = self._make_one(self.JOB_ID, [source], destination, client1)
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            self.assertTrue(job.exists(client=client2))

        final_attributes.assert_called_with({"path": PATH}, client2, job)

        conn1.api_request.assert_not_called()
        conn2.api_request.assert_called_once_with(
            method="GET", path=PATH, query_params={"fields": "id"}, timeout=None
        )

    def test_reload_w_bound_client(self):
        from google.cloud.bigquery.retry import DEFAULT_GET_JOB_TIMEOUT

        PATH = "/projects/%s/jobs/%s" % (self.PROJECT, self.JOB_ID)
        RESOURCE = self._make_resource()
        conn = make_connection(RESOURCE)
        client = _make_client(project=self.PROJECT, connection=conn)
        source = self._table_ref(self.SOURCE_TABLE)
        destination = self._table_ref(self.DESTINATION_TABLE)
        job = self._make_one(self.JOB_ID, [source], destination, client)
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            job.reload()

        final_attributes.assert_called_with(
            {
                "path": PATH,
                "job_id": self.JOB_ID,
                "location": None,
            },
            client,
            None,
        )

        conn.api_request.assert_called_once_with(
            method="GET",
            path=PATH,
            query_params={"projection": "full"},
            timeout=DEFAULT_GET_JOB_TIMEOUT,
        )
        self._verifyResourceProperties(job, RESOURCE)

    def test_reload_w_alternate_client(self):
        from google.cloud.bigquery.retry import DEFAULT_GET_JOB_TIMEOUT

        PATH = "/projects/%s/jobs/%s" % (self.PROJECT, self.JOB_ID)
        RESOURCE = self._make_resource()
        conn1 = make_connection()
        client1 = _make_client(project=self.PROJECT, connection=conn1)
        conn2 = make_connection(RESOURCE)
        client2 = _make_client(project=self.PROJECT, connection=conn2)
        source = self._table_ref(self.SOURCE_TABLE)
        destination = self._table_ref(self.DESTINATION_TABLE)
        job = self._make_one(self.JOB_ID, [source], destination, client1)
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            job.reload(client=client2)

        final_attributes.assert_called_with(
            {
                "path": PATH,
                "job_id": self.JOB_ID,
                "location": None,
            },
            client2,
            None,
        )

        conn1.api_request.assert_not_called()
        conn2.api_request.assert_called_once_with(
            method="GET",
            path=PATH,
            query_params={"projection": "full"},
            timeout=DEFAULT_GET_JOB_TIMEOUT,
        )
        self._verifyResourceProperties(job, RESOURCE)
