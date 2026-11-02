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

import json
from unittest import mock

from ..helpers import make_connection

from .helpers import _Base
from .helpers import _make_client


class TestExtractJobConfig(_Base):
    JOB_TYPE = "extract"

    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.job import ExtractJobConfig

        return ExtractJobConfig

    def test_ctor_w_properties(self):
        config = self._get_target_class()(field_delimiter="\t", print_header=True)

        self.assertEqual(config.field_delimiter, "\t")
        self.assertTrue(config.print_header)

    def test_to_api_repr(self):
        from google.cloud.bigquery import job

        config = self._make_one()
        config.compression = job.Compression.SNAPPY
        config.destination_format = job.DestinationFormat.AVRO
        config.field_delimiter = "ignored for avro"
        config.print_header = False
        config._properties["extract"]["someNewField"] = "some-value"
        config.use_avro_logical_types = True
        resource = json.dumps(config.to_api_repr(), sort_keys=True)
        expected = json.dumps(
            {
                "extract": {
                    "compression": "SNAPPY",
                    "destinationFormat": "AVRO",
                    "fieldDelimiter": "ignored for avro",
                    "printHeader": False,
                    "someNewField": "some-value",
                    "useAvroLogicalTypes": True,
                }
            },
            sort_keys=True,
        )

        self.assertEqual(
            resource,
            expected,
        )

    def test_from_api_repr(self):
        cls = self._get_target_class()
        config = cls.from_api_repr(
            {
                "extract": {
                    "compression": "NONE",
                    "destinationFormat": "CSV",
                    "fieldDelimiter": "\t",
                    "printHeader": True,
                    "someNewField": "some-value",
                    "useAvroLogicalTypes": False,
                }
            }
        )
        self.assertEqual(config.compression, "NONE")
        self.assertEqual(config.destination_format, "CSV")
        self.assertEqual(config.field_delimiter, "\t")
        self.assertEqual(config.print_header, True)
        self.assertEqual(config._properties["extract"]["someNewField"], "some-value")
        self.assertEqual(config.use_avro_logical_types, False)


class TestExtractJob(_Base):
    JOB_TYPE = "extract"
    SOURCE_TABLE = "source_table"
    DESTINATION_URI = "gs://bucket_name/object_name"

    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.job import ExtractJob

        return ExtractJob

    def _make_resource(self, started=False, ended=False):
        resource = super(TestExtractJob, self)._make_resource(started, ended)
        config = resource["configuration"]["extract"]
        config["sourceTable"] = {
            "projectId": self.PROJECT,
            "datasetId": self.DS_ID,
            "tableId": self.SOURCE_TABLE,
        }
        config["destinationUris"] = [self.DESTINATION_URI]
        return resource

    def _verifyResourceProperties(self, job, resource):
        self._verifyReadonlyResourceProperties(job, resource)

        config = resource.get("configuration", {}).get("extract")

        self.assertEqual(job.destination_uris, config["destinationUris"])

        if "sourceTable" in config:
            table_ref = config["sourceTable"]
            self.assertEqual(job.source.project, table_ref["projectId"])
            self.assertEqual(job.source.dataset_id, table_ref["datasetId"])
            self.assertEqual(job.source.table_id, table_ref["tableId"])
        else:
            model_ref = config["sourceModel"]
            self.assertEqual(job.source.project, model_ref["projectId"])
            self.assertEqual(job.source.dataset_id, model_ref["datasetId"])
            self.assertEqual(job.source.model_id, model_ref["modelId"])

        if "compression" in config:
            self.assertEqual(job.compression, config["compression"])
        else:
            self.assertIsNone(job.compression)

        if "destinationFormat" in config:
            self.assertEqual(job.destination_format, config["destinationFormat"])
        else:
            self.assertIsNone(job.destination_format)

        if "fieldDelimiter" in config:
            self.assertEqual(job.field_delimiter, config["fieldDelimiter"])
        else:
            self.assertIsNone(job.field_delimiter)

        if "printHeader" in config:
            self.assertEqual(job.print_header, config["printHeader"])
        else:
            self.assertIsNone(job.print_header)

    def test_ctor(self):
        from google.cloud.bigquery.table import Table

        client = _make_client(project=self.PROJECT)
        source = Table(self.TABLE_REF)
        job = self._make_one(self.JOB_ID, source, [self.DESTINATION_URI], client)
        self.assertEqual(job.source.project, self.PROJECT)
        self.assertEqual(job.source.dataset_id, self.DS_ID)
        self.assertEqual(job.source.table_id, self.TABLE_ID)
        self.assertEqual(job.destination_uris, [self.DESTINATION_URI])
        self.assertIs(job._client, client)
        self.assertEqual(job.job_type, self.JOB_TYPE)
        self.assertEqual(job.path, "/projects/%s/jobs/%s" % (self.PROJECT, self.JOB_ID))

        self._verifyInitialReadonlyProperties(job)

        # set/read from resource['configuration']['extract']
        self.assertIsNone(job.compression)
        self.assertIsNone(job.destination_format)
        self.assertIsNone(job.field_delimiter)
        self.assertIsNone(job.print_header)

    def test_destination_uri_file_counts(self):
        file_counts = 23
        client = _make_client(project=self.PROJECT)
        job = self._make_one(
            self.JOB_ID, self.TABLE_REF, [self.DESTINATION_URI], client
        )
        self.assertIsNone(job.destination_uri_file_counts)

        statistics = job._properties["statistics"] = {}
        self.assertIsNone(job.destination_uri_file_counts)

        extract_stats = statistics["extract"] = {}
        self.assertIsNone(job.destination_uri_file_counts)

        extract_stats["destinationUriFileCounts"] = [str(file_counts)]
        self.assertEqual(job.destination_uri_file_counts, [file_counts])

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
                "extract": {
                    "sourceTable": {
                        "projectId": self.PROJECT,
                        "datasetId": self.DS_ID,
                        "tableId": self.SOURCE_TABLE,
                    },
                    "destinationUris": [self.DESTINATION_URI],
                }
            },
        }
        klass = self._get_target_class()
        job = klass.from_api_repr(RESOURCE, client=client)
        self.assertIs(job._client, client)
        self._verifyResourceProperties(job, RESOURCE)

    def test_from_api_repr_for_model(self):
        self._setUpConstants()
        client = _make_client(project=self.PROJECT)
        RESOURCE = {
            "id": self.JOB_ID,
            "jobReference": {"projectId": self.PROJECT, "jobId": self.JOB_ID},
            "configuration": {
                "extract": {
                    "sourceModel": {
                        "projectId": self.PROJECT,
                        "datasetId": self.DS_ID,
                        "modelId": "model_id",
                    },
                    "destinationUris": [self.DESTINATION_URI],
                }
            },
        }
        klass = self._get_target_class()
        job = klass.from_api_repr(RESOURCE, client=client)
        self.assertIs(job._client, client)
        self._verifyResourceProperties(job, RESOURCE)

    def test_from_api_repr_w_properties(self):
        from google.cloud.bigquery.job import Compression

        client = _make_client(project=self.PROJECT)
        RESOURCE = self._make_resource()
        extract_config = RESOURCE["configuration"]["extract"]
        extract_config["compression"] = Compression.GZIP
        klass = self._get_target_class()
        job = klass.from_api_repr(RESOURCE, client=client)
        self.assertIs(job._client, client)
        self._verifyResourceProperties(job, RESOURCE)

    def test_begin_w_bound_client(self):
        from google.cloud.bigquery.dataset import DatasetReference

        PATH = "/projects/%s/jobs" % (self.PROJECT,)
        RESOURCE = self._make_resource()
        # Ensure None for missing server-set props
        del RESOURCE["statistics"]["creationTime"]
        del RESOURCE["etag"]
        del RESOURCE["selfLink"]
        del RESOURCE["user_email"]
        conn = make_connection(RESOURCE)
        client = _make_client(project=self.PROJECT, connection=conn)
        source_dataset = DatasetReference(self.PROJECT, self.DS_ID)
        source = source_dataset.table(self.SOURCE_TABLE)
        job = self._make_one(self.JOB_ID, source, [self.DESTINATION_URI], client)
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
                    "extract": {
                        "sourceTable": {
                            "projectId": self.PROJECT,
                            "datasetId": self.DS_ID,
                            "tableId": self.SOURCE_TABLE,
                        },
                        "destinationUris": [self.DESTINATION_URI],
                    }
                },
            },
            timeout=None,
        )
        self._verifyResourceProperties(job, RESOURCE)

    def test_begin_w_alternate_client(self):
        from google.cloud.bigquery.dataset import DatasetReference
        from google.cloud.bigquery.job import Compression
        from google.cloud.bigquery.job import DestinationFormat
        from google.cloud.bigquery.job import ExtractJobConfig

        PATH = "/projects/%s/jobs" % (self.PROJECT,)
        RESOURCE = self._make_resource(ended=True)
        EXTRACT_CONFIGURATION = {
            "sourceTable": {
                "projectId": self.PROJECT,
                "datasetId": self.DS_ID,
                "tableId": self.SOURCE_TABLE,
            },
            "destinationUris": [self.DESTINATION_URI],
            "compression": Compression.GZIP,
            "destinationFormat": DestinationFormat.NEWLINE_DELIMITED_JSON,
            "fieldDelimiter": "|",
            "printHeader": False,
        }
        RESOURCE["configuration"]["extract"] = EXTRACT_CONFIGURATION
        conn1 = make_connection()
        client1 = _make_client(project=self.PROJECT, connection=conn1)
        conn2 = make_connection(RESOURCE)
        client2 = _make_client(project=self.PROJECT, connection=conn2)
        source_dataset = DatasetReference(self.PROJECT, self.DS_ID)
        source = source_dataset.table(self.SOURCE_TABLE)
        config = ExtractJobConfig()
        config.compression = Compression.GZIP
        config.destination_format = DestinationFormat.NEWLINE_DELIMITED_JSON
        config.field_delimiter = "|"
        config.print_header = False
        job = self._make_one(
            self.JOB_ID, source, [self.DESTINATION_URI], client1, config
        )
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
                "configuration": {"extract": EXTRACT_CONFIGURATION},
            },
            timeout=None,
        )
        self._verifyResourceProperties(job, RESOURCE)

    def test_exists_miss_w_bound_client(self):
        PATH = "/projects/%s/jobs/%s" % (self.PROJECT, self.JOB_ID)
        conn = make_connection()
        client = _make_client(project=self.PROJECT, connection=conn)
        job = self._make_one(
            self.JOB_ID, self.TABLE_REF, [self.DESTINATION_URI], client
        )
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
        job = self._make_one(
            self.JOB_ID, self.TABLE_REF, [self.DESTINATION_URI], client1
        )
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
        from google.cloud.bigquery.dataset import DatasetReference
        from google.cloud.bigquery.retry import DEFAULT_GET_JOB_TIMEOUT

        PATH = "/projects/%s/jobs/%s" % (self.PROJECT, self.JOB_ID)
        RESOURCE = self._make_resource()
        conn = make_connection(RESOURCE)
        client = _make_client(project=self.PROJECT, connection=conn)
        source_dataset = DatasetReference(self.PROJECT, self.DS_ID)
        source = source_dataset.table(self.SOURCE_TABLE)
        job = self._make_one(self.JOB_ID, source, [self.DESTINATION_URI], client)
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
        from google.cloud.bigquery.dataset import DatasetReference
        from google.cloud.bigquery.retry import DEFAULT_GET_JOB_TIMEOUT

        PATH = "/projects/%s/jobs/%s" % (self.PROJECT, self.JOB_ID)
        RESOURCE = self._make_resource()
        conn1 = make_connection()
        client1 = _make_client(project=self.PROJECT, connection=conn1)
        conn2 = make_connection(RESOURCE)
        client2 = _make_client(project=self.PROJECT, connection=conn2)
        source_dataset = DatasetReference(self.PROJECT, self.DS_ID)
        source = source_dataset.table(self.SOURCE_TABLE)
        job = self._make_one(self.JOB_ID, source, [self.DESTINATION_URI], client1)
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
