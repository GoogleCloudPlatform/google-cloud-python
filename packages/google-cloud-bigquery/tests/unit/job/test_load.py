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

import copy
from unittest import mock

from ..helpers import make_connection

from .helpers import _Base
from .helpers import _make_client
from google.cloud.bigquery.enums import SourceColumnMatch


class TestLoadJob(_Base):
    JOB_TYPE = "load"

    @staticmethod
    def _get_target_class():
        from google.cloud.bigquery.job import LoadJob

        return LoadJob

    def _setUpConstants(self):
        super(TestLoadJob, self)._setUpConstants()
        self.INPUT_FILES = 2
        self.INPUT_BYTES = 12345
        self.OUTPUT_BYTES = 23456
        self.OUTPUT_ROWS = 345
        self.REFERENCE_FILE_SCHEMA_URI = "gs://path/to/reference"
        self.SOURCE_COLUMN_MATCH = "NAME"
        self.DATE_FORMAT = "%Y-%m-%d"
        self.DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S"
        self.TIME_ZONE = "UTC"
        self.TIME_FORMAT = "%H:%M:%S"
        self.TIMESTAMP_FORMAT = "YYYY-MM-DD HH:MM:SS.SSSSSSZ"
        self.NULL_MARKERS = ["", "NA"]

    def _make_resource(self, started=False, ended=False):
        resource = super(TestLoadJob, self)._make_resource(started, ended)
        config = resource["configuration"]["load"]
        config["sourceUris"] = [self.SOURCE1]
        config["sourceColumnMatch"] = self.SOURCE_COLUMN_MATCH
        config["dateFormat"] = self.DATE_FORMAT
        config["datetimeFormat"] = self.DATETIME_FORMAT
        config["timeZone"] = self.TIME_ZONE
        config["timeFormat"] = self.TIME_FORMAT
        config["timestampFormat"] = self.TIMESTAMP_FORMAT
        config["nullMarkers"] = self.NULL_MARKERS

        config["destinationTable"] = {
            "projectId": self.PROJECT,
            "datasetId": self.DS_ID,
            "tableId": self.TABLE_ID,
        }
        config["referenceFileSchemaUri"] = self.REFERENCE_FILE_SCHEMA_URI

        if ended:
            resource["status"] = {"state": "DONE"}
            resource["statistics"]["load"]["inputFiles"] = self.INPUT_FILES
            resource["statistics"]["load"]["inputFileBytes"] = self.INPUT_BYTES
            resource["statistics"]["load"]["outputBytes"] = self.OUTPUT_BYTES
            resource["statistics"]["load"]["outputRows"] = self.OUTPUT_ROWS

        return resource

    def _verifyBooleanConfigProperties(self, job, config):
        if "allowJaggedRows" in config:
            self.assertEqual(job.allow_jagged_rows, config["allowJaggedRows"])
        else:
            self.assertIsNone(job.allow_jagged_rows)
        if "allowQuotedNewlines" in config:
            self.assertEqual(job.allow_quoted_newlines, config["allowQuotedNewlines"])
        else:
            self.assertIsNone(job.allow_quoted_newlines)
        if "autodetect" in config:
            self.assertEqual(job.autodetect, config["autodetect"])
        else:
            self.assertIsNone(job.autodetect)
        if "ignoreUnknownValues" in config:
            self.assertEqual(job.ignore_unknown_values, config["ignoreUnknownValues"])
        else:
            self.assertIsNone(job.ignore_unknown_values)
        if "useAvroLogicalTypes" in config:
            self.assertEqual(job.use_avro_logical_types, config["useAvroLogicalTypes"])
        else:
            self.assertIsNone(job.use_avro_logical_types)

    def _verifyEnumConfigProperties(self, job, config):
        if "createDisposition" in config:
            self.assertEqual(job.create_disposition, config["createDisposition"])
        else:
            self.assertIsNone(job.create_disposition)
        if "encoding" in config:
            self.assertEqual(job.encoding, config["encoding"])
        else:
            self.assertIsNone(job.encoding)
        if "sourceFormat" in config:
            self.assertEqual(job.source_format, config["sourceFormat"])
        else:
            self.assertIsNone(job.source_format)
        if "writeDisposition" in config:
            self.assertEqual(job.write_disposition, config["writeDisposition"])
        else:
            self.assertIsNone(job.write_disposition)
        if "schemaUpdateOptions" in config:
            self.assertEqual(job.schema_update_options, config["schemaUpdateOptions"])
        else:
            self.assertIsNone(job.schema_update_options)

    def _verifyResourceProperties(self, job, resource):
        self._verifyReadonlyResourceProperties(job, resource)

        config = resource.get("configuration", {}).get("load")

        self._verifyBooleanConfigProperties(job, config)
        self._verifyEnumConfigProperties(job, config)

        self.assertEqual(job.source_uris, config["sourceUris"])

        table_ref = config["destinationTable"]
        self.assertEqual(job.destination.project, table_ref["projectId"])
        self.assertEqual(job.destination.dataset_id, table_ref["datasetId"])
        self.assertEqual(job.destination.table_id, table_ref["tableId"])

        if "fieldDelimiter" in config:
            self.assertEqual(job.field_delimiter, config["fieldDelimiter"])
        else:
            self.assertIsNone(job.field_delimiter)
        if "maxBadRecords" in config:
            self.assertEqual(job.max_bad_records, config["maxBadRecords"])
        else:
            self.assertIsNone(job.max_bad_records)
        if "nullMarker" in config:
            self.assertEqual(job.null_marker, config["nullMarker"])
        else:
            self.assertIsNone(job.null_marker)
        if "nullMarkers" in config:
            self.assertEqual(job.null_markers, config["nullMarkers"])
        else:
            self.assertIsNone(job.null_markers)
        if "quote" in config:
            self.assertEqual(job.quote_character, config["quote"])
        else:
            self.assertIsNone(job.quote_character)
        if "skipLeadingRows" in config:
            self.assertEqual(str(job.skip_leading_rows), config["skipLeadingRows"])
        else:
            self.assertIsNone(job.skip_leading_rows)
        if "referenceFileSchemaUri" in config:
            self.assertEqual(
                job.reference_file_schema_uri, config["referenceFileSchemaUri"]
            )
        else:
            self.assertIsNone(job.reference_file_schema_uri)
        if "destinationEncryptionConfiguration" in config:
            self.assertIsNotNone(job.destination_encryption_configuration)
            self.assertEqual(
                job.destination_encryption_configuration.kms_key_name,
                config["destinationEncryptionConfiguration"]["kmsKeyName"],
            )
        else:
            self.assertIsNone(job.destination_encryption_configuration)
        if "dateFormat" in config:
            self.assertEqual(job.date_format, config["dateFormat"])
        else:
            self.assertIsNone(job.date_format)
        if "datetimeFormat" in config:
            self.assertEqual(job.datetime_format, config["datetimeFormat"])
        else:
            self.assertIsNone(job.datetime_format)
        if "timeZone" in config:
            self.assertEqual(job.time_zone, config["timeZone"])
        else:
            self.assertIsNone(job.time_zone)
        if "timeFormat" in config:
            self.assertEqual(job.time_format, config["timeFormat"])
        else:
            self.assertIsNone(job.time_format)
        if "timestampFormat" in config:
            self.assertEqual(job.timestamp_format, config["timestampFormat"])
        else:
            self.assertIsNone(job.timestamp_format)

        if "sourceColumnMatch" in config:
            # job.source_column_match will be an Enum, config[...] is a string
            self.assertEqual(
                job.source_column_match.value,
                config["sourceColumnMatch"],
            )
        else:
            self.assertIsNone(job.source_column_match)

    def test_ctor(self):
        client = _make_client(project=self.PROJECT)
        job = self._make_one(self.JOB_ID, [self.SOURCE1], self.TABLE_REF, client)
        self.assertEqual(job.destination, self.TABLE_REF)
        self.assertEqual(list(job.source_uris), [self.SOURCE1])
        self.assertIs(job._client, client)
        self.assertEqual(job.job_type, self.JOB_TYPE)
        self.assertEqual(job.path, "/projects/%s/jobs/%s" % (self.PROJECT, self.JOB_ID))

        self._verifyInitialReadonlyProperties(job)

        # derived from resource['statistics']['load']
        self.assertIsNone(job.input_file_bytes)
        self.assertIsNone(job.input_files)
        self.assertIsNone(job.output_bytes)
        self.assertIsNone(job.output_rows)

        # set/read from resource['configuration']['load']
        self.assertIsNone(job.schema)
        self.assertIsNone(job.allow_jagged_rows)
        self.assertIsNone(job.allow_quoted_newlines)
        self.assertIsNone(job.autodetect)
        self.assertIsNone(job.create_disposition)
        self.assertIsNone(job.encoding)
        self.assertIsNone(job.field_delimiter)
        self.assertIsNone(job.ignore_unknown_values)
        self.assertIsNone(job.max_bad_records)
        self.assertIsNone(job.null_marker)
        self.assertIsNone(job.null_markers)
        self.assertIsNone(job.quote_character)
        self.assertIsNone(job.skip_leading_rows)
        self.assertIsNone(job.source_format)
        self.assertIsNone(job.write_disposition)
        self.assertIsNone(job.destination_encryption_configuration)
        self.assertIsNone(job.destination_table_description)
        self.assertIsNone(job.destination_table_friendly_name)
        self.assertIsNone(job.range_partitioning)
        self.assertIsNone(job.time_partitioning)
        self.assertIsNone(job.use_avro_logical_types)
        self.assertIsNone(job.clustering_fields)
        self.assertIsNone(job.schema_update_options)
        self.assertIsNone(job.reference_file_schema_uri)
        self.assertIsNone(job.source_column_match)
        self.assertIsNone(job.date_format)
        self.assertIsNone(job.datetime_format)
        self.assertIsNone(job.time_zone)
        self.assertIsNone(job.time_format)
        self.assertIsNone(job.timestamp_format)

    def test_ctor_w_config(self):
        from google.cloud.bigquery.schema import SchemaField
        from google.cloud.bigquery.job import LoadJobConfig

        client = _make_client(project=self.PROJECT)
        full_name = SchemaField("full_name", "STRING", mode="REQUIRED")
        age = SchemaField("age", "INTEGER", mode="REQUIRED")
        config = LoadJobConfig()
        config.schema = [full_name, age]
        job = self._make_one(
            self.JOB_ID, [self.SOURCE1], self.TABLE_REF, client, config
        )
        self.assertEqual(job.schema, [full_name, age])
        config.destination_table_description = "Description"
        expected = {"description": "Description"}
        self.assertEqual(
            config._properties["load"]["destinationTableProperties"], expected
        )
        friendly_name = "Friendly Name"
        config._properties["load"]["destinationTableProperties"] = {
            "friendlyName": friendly_name
        }
        self.assertEqual(config.destination_table_friendly_name, friendly_name)

    def test_ctor_w_job_reference(self):
        from google.cloud.bigquery import job

        client = _make_client(project=self.PROJECT)
        job_ref = job._JobReference(self.JOB_ID, "alternative-project", "US")
        load_job = self._make_one(job_ref, [self.SOURCE1], self.TABLE_REF, client)
        self.assertEqual(load_job.project, "alternative-project")
        self.assertEqual(load_job.location, "US")

    def test_done(self):
        client = _make_client(project=self.PROJECT)
        resource = self._make_resource(ended=True)
        job = self._get_target_class().from_api_repr(resource, client)
        self.assertTrue(job.done())

    def test_result(self):
        client = _make_client(project=self.PROJECT)
        resource = self._make_resource(ended=True)
        job = self._get_target_class().from_api_repr(resource, client)

        result = job.result()

        self.assertIs(result, job)

    def test_result_invokes_begin(self):
        begun_resource = self._make_resource()
        done_resource = copy.deepcopy(begun_resource)
        done_resource["status"] = {"state": "DONE"}
        connection = make_connection(begun_resource, done_resource)
        client = _make_client(self.PROJECT)
        client._connection = connection

        job = self._make_one(self.JOB_ID, [self.SOURCE1], self.TABLE_REF, client)
        job.result()

        self.assertEqual(len(connection.api_request.call_args_list), 2)
        begin_request, reload_request = connection.api_request.call_args_list
        self.assertEqual(begin_request[1]["method"], "POST")
        self.assertEqual(reload_request[1]["method"], "GET")

    def test_schema_setter_non_list(self):
        from google.cloud.bigquery.job import LoadJobConfig

        config = LoadJobConfig()
        with self.assertRaises(TypeError):
            config.schema = object()

    def test_schema_setter_invalid_field(self):
        from google.cloud.bigquery.job import LoadJobConfig
        from google.cloud.bigquery.schema import SchemaField

        config = LoadJobConfig()
        full_name = SchemaField("full_name", "STRING", mode="REQUIRED")
        with self.assertRaises(TypeError):
            config.schema = [full_name, object()]

    def test_schema_setter(self):
        from google.cloud.bigquery.job import LoadJobConfig
        from google.cloud.bigquery.schema import SchemaField

        config = LoadJobConfig()
        full_name = SchemaField("full_name", "STRING", mode="REQUIRED")
        age = SchemaField("age", "INTEGER", mode="REQUIRED")
        config.schema = [full_name, age]
        self.assertEqual(config.schema, [full_name, age])

    def test_props_set_by_server(self):
        import datetime
        from google.cloud._helpers import UTC
        from google.cloud._helpers import _millis

        CREATED = datetime.datetime(2015, 8, 11, 12, 13, 22, tzinfo=UTC)
        STARTED = datetime.datetime(2015, 8, 11, 13, 47, 15, tzinfo=UTC)
        ENDED = datetime.datetime(2015, 8, 11, 14, 47, 15, tzinfo=UTC)
        FULL_JOB_ID = "%s:%s" % (self.PROJECT, self.JOB_ID)
        URL = "http://example.com/projects/%s/jobs/%s" % (self.PROJECT, self.JOB_ID)
        EMAIL = "phred@example.com"
        ERROR_RESULT = {
            "debugInfo": "DEBUG",
            "location": "LOCATION",
            "message": "MESSAGE",
            "reason": "REASON",
        }

        client = _make_client(project=self.PROJECT)
        job = self._make_one(self.JOB_ID, [self.SOURCE1], self.TABLE_REF, client)
        job._properties["etag"] = "ETAG"
        job._properties["id"] = FULL_JOB_ID
        job._properties["selfLink"] = URL
        job._properties["user_email"] = EMAIL

        statistics = job._properties["statistics"] = {}
        statistics["creationTime"] = _millis(CREATED)
        statistics["startTime"] = _millis(STARTED)
        statistics["endTime"] = _millis(ENDED)

        self.assertEqual(job.etag, "ETAG")
        self.assertEqual(job.self_link, URL)
        self.assertEqual(job.user_email, EMAIL)

        self.assertEqual(job.created, CREATED)
        self.assertEqual(job.started, STARTED)
        self.assertEqual(job.ended, ENDED)

        # running jobs have no load stats not yet set.
        self.assertIsNone(job.output_bytes)

        load_stats = statistics["load"] = {}
        load_stats["inputFileBytes"] = 12345
        load_stats["inputFiles"] = 1
        load_stats["outputBytes"] = 23456
        load_stats["outputRows"] = 345

        self.assertEqual(job.input_file_bytes, 12345)
        self.assertEqual(job.input_files, 1)
        self.assertEqual(job.output_bytes, 23456)
        self.assertEqual(job.output_rows, 345)

        status = job._properties["status"] = {}

        self.assertIsNone(job.error_result)
        self.assertIsNone(job.errors)
        self.assertIsNone(job.state)

        status["errorResult"] = ERROR_RESULT
        status["errors"] = [ERROR_RESULT]
        status["state"] = "STATE"

        self.assertEqual(job.error_result, ERROR_RESULT)
        self.assertEqual(job.errors, [ERROR_RESULT])
        self.assertEqual(job.state, "STATE")

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
            "id": "%s:%s" % (self.PROJECT, self.JOB_ID),
            "jobReference": {"projectId": self.PROJECT, "jobId": self.JOB_ID},
        }
        klass = self._get_target_class()
        with self.assertRaises(KeyError):
            klass.from_api_repr(RESOURCE, client=client)

    def test_from_api_repr_bare(self):
        self._setUpConstants()
        client = _make_client(project=self.PROJECT)
        RESOURCE = {
            "id": self.FULL_JOB_ID,
            "jobReference": {"projectId": self.PROJECT, "jobId": self.JOB_ID},
            "configuration": {
                "load": {
                    "sourceUris": [self.SOURCE1],
                    "destinationTable": {
                        "projectId": self.PROJECT,
                        "datasetId": self.DS_ID,
                        "tableId": self.TABLE_ID,
                    },
                }
            },
        }
        klass = self._get_target_class()
        job = klass.from_api_repr(RESOURCE, client=client)
        self.assertIs(job._client, client)
        self._verifyResourceProperties(job, RESOURCE)
        self.assertEqual(len(job.connection_properties), 0)
        self.assertIsNone(job.create_session)

    def test_from_api_with_encryption(self):
        self._setUpConstants()
        client = _make_client(project=self.PROJECT)
        RESOURCE = {
            "id": self.FULL_JOB_ID,
            "jobReference": {"projectId": self.PROJECT, "jobId": self.JOB_ID},
            "configuration": {
                "load": {
                    "sourceUris": [self.SOURCE1],
                    "destinationTable": {
                        "projectId": self.PROJECT,
                        "datasetId": self.DS_ID,
                        "tableId": self.TABLE_ID,
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

    def test_from_api_repr_w_properties(self):
        from google.cloud.bigquery.job import CreateDisposition

        client = _make_client(project=self.PROJECT)
        RESOURCE = self._make_resource()
        load_config = RESOURCE["configuration"]["load"]
        load_config["createDisposition"] = CreateDisposition.CREATE_IF_NEEDED
        klass = self._get_target_class()
        job = klass.from_api_repr(RESOURCE, client=client)
        self.assertIs(job._client, client)
        self._verifyResourceProperties(job, RESOURCE)

    def test_to_api_repr(self):
        self._setUpConstants()
        client = _make_client(project=self.PROJECT)
        RESOURCE = self._make_resource(ended=False)

        klass = self._get_target_class()
        job = klass.from_api_repr(RESOURCE, client)
        api_repr = job.to_api_repr()

        # as per the documentation in load.py -> LoadJob.to_api_repr(),
        # the return value from to_api_repr should not include statistics
        expected = {
            "jobReference": RESOURCE["jobReference"],
            "configuration": RESOURCE["configuration"],
        }

        self.assertEqual(api_repr, expected)

    def test_begin_w_already_running(self):
        conn = make_connection()
        client = _make_client(project=self.PROJECT, connection=conn)
        job = self._make_one(self.JOB_ID, [self.SOURCE1], self.TABLE_REF, client)
        job._properties["status"] = {"state": "RUNNING"}

        with self.assertRaises(ValueError):
            job._begin()

    def test_begin_w_bound_client(self):
        RESOURCE = self._make_resource()
        # Ensure None for missing server-set props
        del RESOURCE["statistics"]["creationTime"]
        del RESOURCE["etag"]
        del RESOURCE["selfLink"]
        del RESOURCE["user_email"]
        conn = make_connection(RESOURCE)
        client = _make_client(project=self.PROJECT, connection=conn)
        job = self._make_one(self.JOB_ID, [self.SOURCE1], self.TABLE_REF, client)
        job.configuration.reference_file_schema_uri = self.REFERENCE_FILE_SCHEMA_URI
        path = "/projects/{}/jobs".format(self.PROJECT)
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            job._begin()

        final_attributes.assert_called_with({"path": path}, client, job)

        conn.api_request.assert_called_once_with(
            method="POST",
            path=path,
            data={
                "jobReference": {"projectId": self.PROJECT, "jobId": self.JOB_ID},
                "configuration": {
                    "load": {
                        "sourceUris": [self.SOURCE1],
                        "destinationTable": {
                            "projectId": self.PROJECT,
                            "datasetId": self.DS_ID,
                            "tableId": self.TABLE_ID,
                        },
                        "referenceFileSchemaUri": self.REFERENCE_FILE_SCHEMA_URI,
                    }
                },
            },
            timeout=None,
        )
        self._verifyResourceProperties(job, RESOURCE)

    def test_begin_w_autodetect(self):
        from google.cloud.bigquery.job import LoadJobConfig

        path = "/projects/{}/jobs".format(self.PROJECT)
        resource = self._make_resource()
        resource["configuration"]["load"]["autodetect"] = True
        # Ensure None for missing server-set props
        del resource["statistics"]["creationTime"]
        del resource["etag"]
        del resource["selfLink"]
        del resource["user_email"]
        conn = make_connection(resource)
        client = _make_client(project=self.PROJECT, connection=conn)
        config = LoadJobConfig()
        config.autodetect = True
        job = self._make_one(
            self.JOB_ID, [self.SOURCE1], self.TABLE_REF, client, config
        )
        job.configuration.reference_file_schema_uri = self.REFERENCE_FILE_SCHEMA_URI
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            job._begin()

        final_attributes.assert_called_with({"path": path}, client, job)

        sent = {
            "jobReference": {"projectId": self.PROJECT, "jobId": self.JOB_ID},
            "configuration": {
                "load": {
                    "sourceUris": [self.SOURCE1],
                    "destinationTable": {
                        "projectId": self.PROJECT,
                        "datasetId": self.DS_ID,
                        "tableId": self.TABLE_ID,
                    },
                    "referenceFileSchemaUri": self.REFERENCE_FILE_SCHEMA_URI,
                    "autodetect": True,
                }
            },
        }
        conn.api_request.assert_called_once_with(
            method="POST", path=path, data=sent, timeout=None
        )
        self._verifyResourceProperties(job, resource)

    def test_begin_w_alternate_client(self):
        from google.cloud.bigquery.job import CreateDisposition
        from google.cloud.bigquery.job import LoadJobConfig
        from google.cloud.bigquery.job import SchemaUpdateOption
        from google.cloud.bigquery.job import WriteDisposition
        from google.cloud.bigquery.schema import SchemaField

        PATH = "/projects/%s/jobs" % (self.PROJECT,)
        RESOURCE = self._make_resource(ended=True)
        LOAD_CONFIGURATION = {
            "sourceUris": [self.SOURCE1],
            "destinationTable": {
                "projectId": self.PROJECT,
                "datasetId": self.DS_ID,
                "tableId": self.TABLE_ID,
            },
            "allowJaggedRows": True,
            "allowQuotedNewlines": True,
            "createDisposition": CreateDisposition.CREATE_NEVER,
            "encoding": "ISO-8559-1",
            "fieldDelimiter": "|",
            "ignoreUnknownValues": True,
            "maxBadRecords": 100,
            "nullMarker": r"\N",
            "quote": "'",
            "skipLeadingRows": "1",
            "sourceFormat": "CSV",
            "useAvroLogicalTypes": True,
            "writeDisposition": WriteDisposition.WRITE_TRUNCATE,
            "referenceFileSchemaUri": "gs://path/to/reference",
            "schema": {
                "fields": [
                    {
                        "name": "full_name",
                        "type": "STRING",
                        "mode": "REQUIRED",
                    },
                    {
                        "name": "age",
                        "type": "INTEGER",
                        "mode": "REQUIRED",
                    },
                ]
            },
            "schemaUpdateOptions": [SchemaUpdateOption.ALLOW_FIELD_ADDITION],
            "sourceColumnMatch": self.SOURCE_COLUMN_MATCH,
            "dateFormat": self.DATE_FORMAT,
            "datetimeFormat": self.DATETIME_FORMAT,
            "timeZone": self.TIME_ZONE,
            "timeFormat": self.TIME_FORMAT,
            "timestampFormat": self.TIMESTAMP_FORMAT,
        }

        RESOURCE["configuration"]["load"] = LOAD_CONFIGURATION
        conn1 = make_connection()
        client1 = _make_client(project=self.PROJECT, connection=conn1)
        conn2 = make_connection(RESOURCE)
        client2 = _make_client(project=self.PROJECT, connection=conn2)
        full_name = SchemaField("full_name", "STRING", mode="REQUIRED")
        age = SchemaField("age", "INTEGER", mode="REQUIRED")
        config = LoadJobConfig()
        config.schema = [full_name, age]
        job = self._make_one(
            self.JOB_ID, [self.SOURCE1], self.TABLE_REF, client1, config
        )
        config.allow_jagged_rows = True
        config.allow_quoted_newlines = True
        config.create_disposition = CreateDisposition.CREATE_NEVER
        config.encoding = "ISO-8559-1"
        config.field_delimiter = "|"
        config.ignore_unknown_values = True
        config.max_bad_records = 100
        config.null_marker = r"\N"
        config.quote_character = "'"
        config.skip_leading_rows = 1
        config.source_format = "CSV"
        config.use_avro_logical_types = True
        config.write_disposition = WriteDisposition.WRITE_TRUNCATE
        config.schema_update_options = [SchemaUpdateOption.ALLOW_FIELD_ADDITION]
        config.reference_file_schema_uri = "gs://path/to/reference"
        config.source_column_match = SourceColumnMatch(self.SOURCE_COLUMN_MATCH)
        config.date_format = self.DATE_FORMAT
        config.datetime_format = self.DATETIME_FORMAT
        config.time_zone = self.TIME_ZONE
        config.time_format = self.TIME_FORMAT
        config.timestamp_format = self.TIMESTAMP_FORMAT

        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            job._begin(client=client2)

        final_attributes.assert_called_with({"path": PATH}, client2, job)

        conn1.api_request.assert_not_called()
        self.assertEqual(len(conn2.api_request.call_args_list), 1)
        req = conn2.api_request.call_args_list[0]
        self.assertEqual(req[1]["method"], "POST")
        self.assertEqual(req[1]["path"], PATH)
        SENT = {
            "jobReference": {"projectId": self.PROJECT, "jobId": self.JOB_ID},
            "configuration": {"load": LOAD_CONFIGURATION},
        }
        self.maxDiff = None
        self.assertEqual(req[1]["data"], SENT)
        self._verifyResourceProperties(job, RESOURCE)

    def test_begin_w_job_reference(self):
        from google.cloud.bigquery import job

        resource = self._make_resource()
        resource["jobReference"]["projectId"] = "alternative-project"
        resource["jobReference"]["location"] = "US"
        job_ref = job._JobReference(self.JOB_ID, "alternative-project", "US")
        conn = make_connection(resource)
        client = _make_client(project=self.PROJECT, connection=conn)
        load_job = self._make_one(job_ref, [self.SOURCE1], self.TABLE_REF, client)
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            load_job._begin()
        final_attributes.assert_called_with(
            {"path": "/projects/alternative-project/jobs"}, client, load_job
        )

        conn.api_request.assert_called_once()
        _, request = conn.api_request.call_args
        self.assertEqual(request["method"], "POST")
        self.assertEqual(request["path"], "/projects/alternative-project/jobs")
        self.assertEqual(
            request["data"]["jobReference"]["projectId"], "alternative-project"
        )
        self.assertEqual(request["data"]["jobReference"]["location"], "US")
        self.assertEqual(request["data"]["jobReference"]["jobId"], self.JOB_ID)

    def test_exists_miss_w_bound_client(self):
        PATH = "/projects/%s/jobs/%s" % (self.PROJECT, self.JOB_ID)
        conn = make_connection()
        client = _make_client(project=self.PROJECT, connection=conn)
        job = self._make_one(self.JOB_ID, [self.SOURCE1], self.TABLE_REF, client)
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            self.assertFalse(job.exists())

        final_attributes.assert_called_with(
            {"path": "/projects/{}/jobs/{}".format(self.PROJECT, self.JOB_ID)},
            client,
            job,
        )

        conn.api_request.assert_called_once_with(
            method="GET", path=PATH, query_params={"fields": "id"}, timeout=None
        )

    def test_exists_hit_w_alternate_client(self):
        PATH = "/projects/%s/jobs/%s" % (self.PROJECT, self.JOB_ID)
        conn1 = make_connection()
        client1 = _make_client(project=self.PROJECT, connection=conn1)
        conn2 = make_connection({})
        client2 = _make_client(project=self.PROJECT, connection=conn2)
        job = self._make_one(self.JOB_ID, [self.SOURCE1], self.TABLE_REF, client1)
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            self.assertTrue(job.exists(client=client2))

        final_attributes.assert_called_with(
            {"path": "/projects/{}/jobs/{}".format(self.PROJECT, self.JOB_ID)},
            client2,
            job,
        )

        conn1.api_request.assert_not_called()
        conn2.api_request.assert_called_once_with(
            method="GET", path=PATH, query_params={"fields": "id"}, timeout=None
        )

    def test_exists_miss_w_job_reference(self):
        from google.cloud.bigquery import job

        job_ref = job._JobReference("my-job-id", "other-project", "US")
        conn = make_connection()
        client = _make_client(project=self.PROJECT, connection=conn)
        load_job = self._make_one(job_ref, [self.SOURCE1], self.TABLE_REF, client)
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            self.assertFalse(load_job.exists())

        final_attributes.assert_called_with(
            {"path": "/projects/other-project/jobs/my-job-id"}, client, load_job
        )

        conn.api_request.assert_called_once_with(
            method="GET",
            path="/projects/other-project/jobs/my-job-id",
            query_params={"fields": "id", "location": "US"},
            timeout=None,
        )

    def test_reload_w_bound_client(self):
        from google.cloud.bigquery.retry import DEFAULT_GET_JOB_TIMEOUT

        PATH = "/projects/%s/jobs/%s" % (self.PROJECT, self.JOB_ID)
        RESOURCE = self._make_resource()
        conn = make_connection(RESOURCE)
        client = _make_client(project=self.PROJECT, connection=conn)
        job = self._make_one(self.JOB_ID, [self.SOURCE1], self.TABLE_REF, client)
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
        job = self._make_one(self.JOB_ID, [self.SOURCE1], self.TABLE_REF, client1)
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

    def test_reload_w_job_reference(self):
        from google.cloud.bigquery import job
        from google.cloud.bigquery.retry import DEFAULT_GET_JOB_TIMEOUT

        resource = self._make_resource(ended=True)
        resource["jobReference"]["projectId"] = "alternative-project"
        resource["jobReference"]["location"] = "US"
        job_ref = job._JobReference(self.JOB_ID, "alternative-project", "US")
        conn = make_connection(resource)
        client = _make_client(project=self.PROJECT, connection=conn)
        load_job = self._make_one(job_ref, [self.SOURCE1], self.TABLE_REF, client)
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            load_job.reload()

        final_attributes.assert_called_with(
            {
                "path": "/projects/alternative-project/jobs/{}".format(self.JOB_ID),
                "job_id": self.JOB_ID,
                "location": "US",
            },
            client,
            None,
        )

        conn.api_request.assert_called_once_with(
            method="GET",
            path="/projects/alternative-project/jobs/{}".format(self.JOB_ID),
            query_params={"projection": "full", "location": "US"},
            timeout=DEFAULT_GET_JOB_TIMEOUT,
        )

    def test_cancel_w_bound_client(self):
        PATH = "/projects/%s/jobs/%s/cancel" % (self.PROJECT, self.JOB_ID)
        RESOURCE = self._make_resource(ended=True)
        RESPONSE = {"job": RESOURCE}
        conn = make_connection(RESPONSE)
        client = _make_client(project=self.PROJECT, connection=conn)
        job = self._make_one(self.JOB_ID, [self.SOURCE1], self.TABLE_REF, client)
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            job.cancel()

        final_attributes.assert_called_with({"path": PATH}, client, job)

        conn.api_request.assert_called_once_with(
            method="POST", path=PATH, query_params={}, timeout=None
        )
        self._verifyResourceProperties(job, RESOURCE)

    def test_cancel_w_alternate_client(self):
        PATH = "/projects/%s/jobs/%s/cancel" % (self.PROJECT, self.JOB_ID)
        RESOURCE = self._make_resource(ended=True)
        RESPONSE = {"job": RESOURCE}
        conn1 = make_connection()
        client1 = _make_client(project=self.PROJECT, connection=conn1)
        conn2 = make_connection(RESPONSE)
        client2 = _make_client(project=self.PROJECT, connection=conn2)
        job = self._make_one(self.JOB_ID, [self.SOURCE1], self.TABLE_REF, client1)
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            job.cancel(client=client2)

        final_attributes.assert_called_with({"path": PATH}, client2, job)

        conn1.api_request.assert_not_called()
        conn2.api_request.assert_called_once_with(
            method="POST", path=PATH, query_params={}, timeout=None
        )
        self._verifyResourceProperties(job, RESOURCE)

    def test_cancel_w_job_reference(self):
        from google.cloud.bigquery import job

        resource = self._make_resource(ended=True)
        resource["jobReference"]["projectId"] = "alternative-project"
        resource["jobReference"]["location"] = "US"
        job_ref = job._JobReference(self.JOB_ID, "alternative-project", "US")
        conn = make_connection({"job": resource})
        client = _make_client(project=self.PROJECT, connection=conn)
        load_job = self._make_one(job_ref, [self.SOURCE1], self.TABLE_REF, client)
        with mock.patch(
            "google.cloud.bigquery.opentelemetry_tracing._get_final_span_attributes"
        ) as final_attributes:
            load_job.cancel()

        final_attributes.assert_called_with(
            {
                "path": "/projects/alternative-project/jobs/{}/cancel".format(
                    self.JOB_ID
                )
            },
            client,
            load_job,
        )
        conn.api_request.assert_called_once_with(
            method="POST",
            path="/projects/alternative-project/jobs/{}/cancel".format(self.JOB_ID),
            query_params={"location": "US"},
            timeout=None,
        )
