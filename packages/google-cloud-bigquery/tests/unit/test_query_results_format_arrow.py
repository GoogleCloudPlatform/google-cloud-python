# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import base64
import unittest
from unittest import mock
import warnings

import google.api_core.exceptions as core_exceptions
import packaging.version
import pytest

from google.cloud.bigquery import _arrow_query
from google.cloud.bigquery import _job_helpers
from google.cloud.bigquery import _versions_helpers
from google.cloud.bigquery import exceptions
from google.cloud.bigquery.client import Client
from google.cloud.bigquery.enums import QueryResultsCompressionCodec
from google.cloud.bigquery.enums import TimestampPrecision
from google.cloud.bigquery.enums import WriteDisposition
from google.cloud.bigquery.job import QueryJobConfig
from google.cloud.bigquery.table import RowIterator, TableReference, _EmptyRowIterator

from .helpers import make_client

# The Arrow serialization options that jobs.query and ReadRows get when the
# caller sets none.
_DEFAULT_QUERY_OPTIONS = {
    "bufferCompression": "COMPRESSION_UNSPECIFIED",
    "picosTimestampPrecision": "TIMESTAMP_PRECISION_MICROS",
}
_DEFAULT_READ_OPTIONS = {
    "buffer_compression": "COMPRESSION_UNSPECIFIED",
    "picos_timestamp_precision": "TIMESTAMP_PRECISION_MICROS",
}

# The real check, saved before the autouse fixture below replaces it.
_check_dependencies = _arrow_query._check_dependencies


@pytest.fixture(autouse=True)
def check_dependencies():
    """Skip the ARROW dependency check, which depends on installed packages."""
    with mock.patch.object(_arrow_query, "_check_dependencies") as check:
        yield check


class TestQueryResultsFormatOption1(unittest.TestCase):
    def test_supported_by_jobs_query_includes_query_results_format(self):
        body = {"query": "SELECT 1", "queryResultsFormat": "ARROW"}
        self.assertTrue(_job_helpers._supported_by_jobs_query(body))

    def test_job_helpers_query_and_wait_sets_request_body(self):
        client = mock.MagicMock(spec=Client)
        client._call_api.return_value = {
            "jobReference": {"projectId": "p", "jobId": "j", "location": "us"},
            "jobComplete": True,
            "rows": [],
            "schema": {"fields": []},
        }

        row_iterator = _job_helpers.query_and_wait(
            client=client,
            query="SELECT 1",
            project="p",
            location="us",
            job_config=None,
            retry=None,
            job_retry=None,
            query_results_format="ARROW",
        )

        self.assertEqual(row_iterator._query_results_format, "ARROW")
        call_args = client._call_api.call_args
        self.assertIn("queryResultsFormat", call_args.kwargs["data"])
        self.assertEqual(call_args.kwargs["data"]["queryResultsFormat"], "ARROW")

    def test_job_helpers_query_and_wait_sets_compression_codec(self):
        client = mock.MagicMock(spec=Client)
        client._call_api.return_value = {
            "jobReference": {"projectId": "p", "jobId": "j", "location": "us"},
            "jobComplete": True,
            "rows": [],
            "schema": {"fields": []},
        }

        _job_helpers.query_and_wait(
            client=client,
            query="SELECT 1",
            project="p",
            location="us",
            job_config=None,
            retry=None,
            job_retry=None,
            query_results_format="ARROW",
            compression_codec="LZ4_FRAME",
        )

        call_args = client._call_api.call_args
        self.assertNotIn(
            "arrowSerializationOptions", call_args.kwargs["data"]["formatOptions"]
        )
        self.assertEqual(
            call_args.kwargs["data"]["arrowSerializationOptions"],
            {
                "bufferCompression": "LZ4_FRAME",
                "picosTimestampPrecision": "TIMESTAMP_PRECISION_MICROS",
            },
        )

    def test_job_helpers_query_and_wait_fallback_preserves_query_results_format(self):
        client = mock.MagicMock(spec=Client)
        unsupported_body = {"unsupportedKey": "val"}
        job_mock = mock.MagicMock()
        fake_iterator = mock.MagicMock(spec=RowIterator)
        job_mock.result.return_value = fake_iterator

        with mock.patch.object(
            _job_helpers, "_to_query_request", return_value=unsupported_body
        ), mock.patch.object(_job_helpers, "query_jobs_insert", return_value=job_mock):
            res_iterator = _job_helpers.query_and_wait(
                client=client,
                query="SELECT 1",
                project="p",
                location="us",
                job_config=None,
                retry=None,
                job_retry=None,
                query_results_format="ARROW",
            )
            self.assertEqual(res_iterator._query_results_format, "ARROW")

    def test_row_iterator_non_arrow_iteration_raises_value_error(self):
        iterator = RowIterator(
            client=mock.MagicMock(),
            api_request=mock.MagicMock(),
            path=None,
            schema=(),
            query_results_format="ARROW",
        )

        with self.assertRaises(ValueError) as ctx:
            iter(iterator)
        self.assertIn("Cannot iterate over non-arrow results", str(ctx.exception))

        with self.assertRaises(ValueError) as ctx:
            next(iterator)
        self.assertIn("Cannot iterate over non-arrow results", str(ctx.exception))

        with self.assertRaises(ValueError) as ctx:
            _ = iterator.pages
        self.assertIn("Cannot iterate over non-arrow results", str(ctx.exception))

    def test_empty_row_iterator_non_arrow_iteration_raises_value_error(self):
        iterator = _EmptyRowIterator(query_results_format="ARROW")

        with self.assertRaises(ValueError) as ctx:
            iter(iterator)
        self.assertIn("Cannot iterate over non-arrow results", str(ctx.exception))

        with self.assertRaises(ValueError) as ctx:
            next(iterator)
        self.assertIn("Cannot iterate over non-arrow results", str(ctx.exception))

        with self.assertRaises(ValueError) as ctx:
            _ = iterator.pages
        self.assertIn("Cannot iterate over non-arrow results", str(ctx.exception))

    def test_row_iterator_standard_format_allows_iteration(self):
        iterator = RowIterator(
            client=mock.MagicMock(),
            api_request=mock.MagicMock(),
            path=None,
            schema=(),
            query_results_format=None,
        )
        self.assertIsNotNone(iterator.pages)

    def test_row_iterator_to_arrow_iterable_delegates_when_format_is_arrow(self):
        iterator = RowIterator(
            client=mock.MagicMock(),
            api_request=mock.MagicMock(),
            path=None,
            schema=(),
            project="proj",
            location="loc",
            job_id="job123",
            query_results_format="ARROW",
        )

        with mock.patch.object(
            iterator,
            "_download_arrow_from_job_id",
            return_value=iter(["batch1", "batch2"]),
        ) as mock_download:
            res = list(iterator.to_arrow_iterable(timeout=10.0))
            self.assertEqual(res, ["batch1", "batch2"])
            mock_download.assert_called_once_with(bqstorage_client=None, timeout=10.0)

    def test_download_arrow_from_job_id_constructs_stream_and_reads(self):
        mock_client = mock.MagicMock()
        mock_bqstorage = mock.MagicMock()
        mock_client._get_shared_bqstorage_client.return_value = mock_bqstorage

        iterator = RowIterator(
            client=mock_client,
            api_request=mock.MagicMock(),
            path=None,
            schema=(),
            project="test-proj",
            location="US",
            job_id="test-job-456",
            query_results_format="ARROW",
        )

        mock_response = mock.MagicMock()
        mock_response.arrow_schema = None
        mock_response.arrow_record_batch = None
        mock_bqstorage.read_rows.return_value = [mock_response]

        with mock.patch("google.cloud.bigquery._arrow_query.pyarrow") as mock_pyarrow:
            mock_pyarrow.py_buffer = lambda x: x
            batches = list(iterator._download_arrow_from_job_id(timeout=5.0))
            # No rows and no schema: one empty batch without columns.
            self.assertEqual(
                batches, [mock_pyarrow.RecordBatch.from_arrays.return_value]
            )
            mock_pyarrow.schema.assert_called_once_with([])

            expected_stream_name = (
                "projects/test-proj/locations/US/jobs/test-job-456/streams/_default"
            )
            mock_bqstorage.read_rows.assert_called_once_with(
                expected_stream_name,
                offset=0,
                timeout=5.0,
                arrow_serialization_options=_DEFAULT_READ_OPTIONS,
            )

    def test_download_arrow_from_job_id_with_first_page_response(self):
        mock_client = mock.MagicMock()
        mock_bqstorage = mock.MagicMock()
        mock_client._get_shared_bqstorage_client.return_value = mock_bqstorage

        raw_schema_bytes = b"schema_bytes_123"
        raw_batch_bytes = b"batch_bytes_123"
        b64_schema = base64.b64encode(raw_schema_bytes).decode("ascii")
        b64_batch = base64.b64encode(raw_batch_bytes).decode("ascii")

        first_page_response = {
            "arrowSchema": {"serializedSchema": b64_schema},
            "arrowRecordBatch": {"serializedRecordBatch": b64_batch},
        }

        iterator = RowIterator(
            client=mock_client,
            api_request=mock.MagicMock(),
            path=None,
            schema=(),
            project="test-proj",
            location="US",
            job_id="test-job-sync",
            query_results_format="ARROW",
            first_page_response=first_page_response,
        )

        mock_first_batch = mock.MagicMock()
        mock_first_batch.num_rows = 10

        mock_second_batch = mock.MagicMock()
        mock_second_batch.num_rows = 5

        # Subsequent ReadRows response chunk without arrow_schema
        mock_response = mock.MagicMock()
        mock_response.arrow_schema = None
        mock_batch_msg = mock.MagicMock()
        mock_batch_msg.serialized_record_batch = b"stream_batch_bytes"
        mock_response.arrow_record_batch = mock_batch_msg

        mock_bqstorage.read_rows.return_value = [mock_response]

        with mock.patch("google.cloud.bigquery._arrow_query.pyarrow") as mock_pyarrow:
            mock_pyarrow.py_buffer = lambda x: x
            mock_pyarrow.ipc.read_schema.return_value = "deserialized_schema"
            mock_pyarrow.ipc.read_record_batch.side_effect = [
                mock_first_batch,
                mock_second_batch,
            ]

            batches = list(iterator._download_arrow_from_job_id(timeout=5.0))

            self.assertEqual(batches, [mock_first_batch, mock_second_batch])
            # The first page is kept for the next read.
            self.assertIsNotNone(iterator._first_page_response)

            mock_pyarrow.ipc.read_schema.assert_called_once_with(raw_schema_bytes)
            mock_pyarrow.ipc.read_record_batch.assert_has_calls(
                [
                    mock.call(raw_batch_bytes, "deserialized_schema"),
                    mock.call(b"stream_batch_bytes", "deserialized_schema"),
                ]
            )

            expected_stream_name = (
                "projects/test-proj/locations/US/jobs/test-job-sync/streams/_default"
            )
            mock_bqstorage.read_rows.assert_called_once_with(
                expected_stream_name,
                offset=10,
                timeout=5.0,
                arrow_serialization_options=_DEFAULT_READ_OPTIONS,
            )

    def test_download_arrow_from_job_id_with_first_page_response_schema_only(self):
        mock_client = mock.MagicMock()
        mock_bqstorage = mock.MagicMock()
        mock_client._get_shared_bqstorage_client.return_value = mock_bqstorage

        raw_schema_bytes = b"schema_bytes_456"
        first_page_response = {
            "arrowSchema": {"serializedSchema": raw_schema_bytes},
        }

        iterator = RowIterator(
            client=mock_client,
            api_request=mock.MagicMock(),
            path=None,
            schema=(),
            project="test-proj",
            location="US",
            job_id="test-job-schema-only",
            query_results_format="ARROW",
            first_page_response=first_page_response,
        )

        mock_stream_batch = mock.MagicMock()
        mock_response = mock.MagicMock()
        mock_response.arrow_schema = None
        mock_batch_msg = mock.MagicMock()
        mock_batch_msg.serialized_record_batch = b"stream_batch_bytes"
        mock_response.arrow_record_batch = mock_batch_msg

        mock_bqstorage.read_rows.return_value = [mock_response]

        with mock.patch("google.cloud.bigquery._arrow_query.pyarrow") as mock_pyarrow:
            mock_pyarrow.py_buffer = lambda x: x
            mock_pyarrow.ipc.read_schema.return_value = "deserialized_schema"
            mock_pyarrow.ipc.read_record_batch.return_value = mock_stream_batch

            batches = list(iterator._download_arrow_from_job_id(timeout=5.0))

            self.assertEqual(batches, [mock_stream_batch])
            # The first page is kept for the next read.
            self.assertIsNotNone(iterator._first_page_response)
            mock_pyarrow.ipc.read_schema.assert_called_once_with(raw_schema_bytes)
            mock_pyarrow.ipc.read_record_batch.assert_called_once_with(
                b"stream_batch_bytes", "deserialized_schema"
            )
            expected_stream_name = "projects/test-proj/locations/US/jobs/test-job-schema-only/streams/_default"
            mock_bqstorage.read_rows.assert_called_once_with(
                expected_stream_name,
                offset=0,
                timeout=5.0,
                arrow_serialization_options=_DEFAULT_READ_OPTIONS,
            )

    def test_download_arrow_from_job_id_missing_storage_client_raises_value_error(self):
        mock_client = mock.MagicMock()
        mock_client._get_shared_bqstorage_client.return_value = None

        iterator = RowIterator(
            client=mock_client,
            api_request=mock.MagicMock(),
            path=None,
            schema=(),
            project="test-proj",
            location="US",
            job_id="test-job-456",
            query_results_format="ARROW",
        )

        with mock.patch("google.cloud.bigquery._arrow_query.pyarrow"):
            with self.assertRaises(ValueError) as ctx:
                list(iterator._download_arrow_from_job_id())
            self.assertIn(
                "The google-cloud-bigquery-storage library is required",
                str(ctx.exception),
            )

    def test_download_arrow_from_job_id_with_schema_and_batch(self):
        mock_client = mock.MagicMock()
        mock_bqstorage = mock.MagicMock()
        mock_client._get_shared_bqstorage_client.return_value = mock_bqstorage

        iterator = RowIterator(
            client=mock_client,
            api_request=mock.MagicMock(),
            path=None,
            schema=(),
            project="test-proj",
            location="US",
            job_id="test-job-789",
            query_results_format="ARROW",
        )

        mock_schema_msg = mock.MagicMock()
        mock_schema_msg.serialized_schema = b"schema_bytes"
        mock_batch_msg = mock.MagicMock()
        mock_batch_msg.serialized_record_batch = b"batch_bytes"

        mock_response = mock.MagicMock()
        mock_response.arrow_schema = mock_schema_msg
        mock_response.arrow_record_batch = mock_batch_msg

        mock_bqstorage.read_rows.return_value = [mock_response]

        with mock.patch("google.cloud.bigquery._arrow_query.pyarrow") as mock_pyarrow:
            mock_pyarrow.py_buffer = lambda x: x
            mock_pyarrow.ipc.read_schema.return_value = "fake_schema"
            mock_pyarrow.ipc.read_record_batch.return_value = "fake_batch"

            batches = list(iterator._download_arrow_from_job_id(timeout=5.0))
            self.assertEqual(batches, ["fake_batch"])
            mock_pyarrow.ipc.read_schema.assert_called_once_with(b"schema_bytes")
            mock_pyarrow.ipc.read_record_batch.assert_called_once_with(
                b"batch_bytes", "fake_schema"
            )

    def test_download_arrow_from_job_id_first_page_batch_without_schema_raises(self):
        mock_client = mock.MagicMock()
        mock_bqstorage = mock.MagicMock()
        mock_client._get_shared_bqstorage_client.return_value = mock_bqstorage

        b64_batch = base64.b64encode(b"batch_bytes").decode("ascii")
        iterator = RowIterator(
            client=mock_client,
            api_request=mock.MagicMock(),
            path=None,
            schema=(),
            project="test-proj",
            location="US",
            job_id="test-job-no-schema",
            query_results_format="ARROW",
            first_page_response={
                "jobComplete": True,
                "arrowRecordBatch": {"serializedRecordBatch": b64_batch},
            },
        )

        with mock.patch("google.cloud.bigquery._arrow_query.pyarrow") as mock_pyarrow:
            with self.assertRaisesRegex(ValueError, "before its schema"):
                list(iterator._download_arrow_from_job_id(timeout=5.0))

        mock_pyarrow.ipc.read_record_batch.assert_not_called()
        mock_bqstorage.read_rows.assert_not_called()

    def test_download_arrow_from_job_id_read_rows_batch_without_schema_raises(self):
        mock_client = mock.MagicMock()
        mock_bqstorage = mock.MagicMock()
        mock_client._get_shared_bqstorage_client.return_value = mock_bqstorage

        iterator = RowIterator(
            client=mock_client,
            api_request=mock.MagicMock(),
            path=None,
            schema=(),
            project="test-proj",
            location="US",
            job_id="test-job-no-schema",
            query_results_format="ARROW",
        )

        mock_response = mock.MagicMock()
        mock_response.arrow_schema = None
        mock_response.arrow_record_batch.serialized_record_batch = b"batch_bytes"
        reader = mock.MagicMock()
        reader.__iter__.return_value = iter([mock_response])
        mock_bqstorage.read_rows.return_value = reader

        with mock.patch("google.cloud.bigquery._arrow_query.pyarrow") as mock_pyarrow:
            with self.assertRaisesRegex(ValueError, "before its schema"):
                list(iterator._download_arrow_from_job_id(timeout=5.0))

        mock_pyarrow.ipc.read_record_batch.assert_not_called()
        reader.cancel.assert_called_once_with()

    def test_empty_row_iterator_to_arrow_iterable_checks_pyarrow(self):
        iterator = _EmptyRowIterator(query_results_format="ARROW")
        with mock.patch("google.cloud.bigquery.table.pyarrow", None):
            with self.assertRaises(ValueError) as ctx:
                iterator.to_arrow_iterable()
            self.assertIn("pyarrow", str(ctx.exception).lower())

    def test_download_arrow_from_job_id_avoids_read_rows_when_all_rows_present(self):
        mock_client = mock.MagicMock()
        raw_schema_bytes = b"schema_bytes_789"
        raw_batch_bytes = b"batch_bytes_789"
        b64_schema = base64.b64encode(raw_schema_bytes).decode("ascii")
        b64_batch = base64.b64encode(raw_batch_bytes).decode("ascii")

        first_page_response = {
            "jobComplete": True,
            "totalRows": "10",
            "arrowSchema": {"serializedSchema": b64_schema},
            "arrowRecordBatch": {"serializedRecordBatch": b64_batch},
        }

        iterator = RowIterator(
            client=mock_client,
            api_request=mock.MagicMock(),
            path=None,
            schema=(),
            project="test-proj",
            location="US",
            job_id="test-job-complete",
            query_results_format="ARROW",
            first_page_response=first_page_response,
        )

        mock_first_batch = mock.MagicMock()
        mock_first_batch.num_rows = 10

        with mock.patch("google.cloud.bigquery._arrow_query.pyarrow") as mock_pyarrow:
            mock_pyarrow.py_buffer = lambda x: x
            mock_pyarrow.ipc.read_schema.return_value = "deserialized_schema"
            mock_pyarrow.ipc.read_record_batch.return_value = mock_first_batch

            batches = list(iterator._download_arrow_from_job_id(timeout=5.0))
            self.assertEqual(batches, [mock_first_batch])
            mock_client._get_shared_bqstorage_client.assert_not_called()
            batches_second = list(iterator._download_arrow_from_job_id(timeout=5.0))
            self.assertEqual(batches_second, [mock_first_batch])

    def test_download_arrow_from_job_id_page_token_calls_read_rows(self):
        mock_client = mock.MagicMock()
        mock_bqstorage = mock.MagicMock()
        mock_client._get_shared_bqstorage_client.return_value = mock_bqstorage

        # A cache hit too large to return inline: the job is complete and
        # totalRows is 0, but the pageToken says rows remain.
        first_page_response = {
            "jobComplete": True,
            "totalRows": "0",
            "pageToken": "next",
            "arrowSchema": {"serializedSchema": b"schema_bytes"},
            "arrowRecordBatch": {},
        }

        iterator = RowIterator(
            client=mock_client,
            api_request=mock.MagicMock(),
            path=None,
            schema=(),
            project="test-proj",
            location="US",
            job_id="test-job-cached",
            query_results_format="ARROW",
            first_page_response=first_page_response,
        )

        mock_response = mock.MagicMock()
        mock_response.arrow_schema = None
        mock_response.arrow_record_batch.serialized_record_batch = b"stream_batch"
        mock_bqstorage.read_rows.return_value = [mock_response]

        with mock.patch("google.cloud.bigquery._arrow_query.pyarrow") as mock_pyarrow:
            mock_pyarrow.py_buffer = lambda x: x
            mock_pyarrow.ipc.read_schema.return_value = "deserialized_schema"
            mock_pyarrow.ipc.read_record_batch.return_value = "stream_batch"

            batches = list(iterator._download_arrow_from_job_id(timeout=5.0))

        self.assertEqual(batches, ["stream_batch"])
        mock_bqstorage.read_rows.assert_called_once_with(
            "projects/test-proj/locations/US/jobs/test-job-cached/streams/_default",
            offset=0,
            timeout=5.0,
            arrow_serialization_options=_DEFAULT_READ_OPTIONS,
        )

    def test_download_arrow_from_job_id_calls_read_rows_when_job_not_complete(self):
        mock_client = mock.MagicMock()
        mock_bqstorage = mock.MagicMock()
        mock_client._get_shared_bqstorage_client.return_value = mock_bqstorage

        raw_schema_bytes = b"schema_bytes_789"
        raw_batch_bytes = b"batch_bytes_789"
        b64_schema = base64.b64encode(raw_schema_bytes).decode("ascii")
        b64_batch = base64.b64encode(raw_batch_bytes).decode("ascii")

        first_page_response = {
            "jobComplete": False,
            "totalRows": "10",
            "arrowSchema": {"serializedSchema": b64_schema},
            "arrowRecordBatch": {"serializedRecordBatch": b64_batch},
        }

        iterator = RowIterator(
            client=mock_client,
            api_request=mock.MagicMock(),
            path=None,
            schema=(),
            project="test-proj",
            location="US",
            job_id="test-job-incomplete",
            query_results_format="ARROW",
            first_page_response=first_page_response,
        )

        mock_first_batch = mock.MagicMock()
        mock_first_batch.num_rows = 10
        mock_bqstorage.read_rows.return_value = []

        with mock.patch("google.cloud.bigquery._arrow_query.pyarrow") as mock_pyarrow:
            mock_pyarrow.py_buffer = lambda x: x
            mock_pyarrow.ipc.read_schema.return_value = "deserialized_schema"
            mock_pyarrow.ipc.read_record_batch.return_value = mock_first_batch

            batches = list(iterator._download_arrow_from_job_id(timeout=5.0))
            self.assertEqual(batches, [mock_first_batch])
            mock_client._get_shared_bqstorage_client.assert_called_once_with()
            expected_stream = "projects/test-proj/locations/US/jobs/test-job-incomplete/streams/_default"
            mock_bqstorage.read_rows.assert_called_once_with(
                expected_stream,
                offset=10,
                timeout=5.0,
                arrow_serialization_options=_DEFAULT_READ_OPTIONS,
            )

    def test_enums_values(self):
        from google.cloud.bigquery.enums import (
            QueryResultsFormat,
            QueryResultsCompressionCodec,
        )

        self.assertEqual(QueryResultsFormat.ARROW, "ARROW")
        self.assertEqual(QueryResultsCompressionCodec.LZ4_FRAME, "LZ4_FRAME")
        self.assertEqual(QueryResultsCompressionCodec.ZSTD, "ZSTD")

    def test_job_helpers_query_and_wait_accepts_enums(self):
        from google.cloud.bigquery.enums import (
            QueryResultsFormat,
            QueryResultsCompressionCodec,
        )

        client = mock.MagicMock(spec=Client)
        client._call_api.return_value = {
            "jobReference": {"projectId": "p", "jobId": "j", "location": "us"},
            "jobComplete": True,
            "rows": [],
            "schema": {"fields": []},
        }

        row_iterator = _job_helpers.query_and_wait(
            client=client,
            query="SELECT 1",
            project="p",
            location="us",
            job_config=None,
            retry=None,
            job_retry=None,
            query_results_format=QueryResultsFormat.ARROW,
            compression_codec=QueryResultsCompressionCodec.LZ4_FRAME,
        )
        self.assertEqual(row_iterator._query_results_format, "ARROW")

        call_args = client._call_api.call_args
        self.assertEqual(call_args.kwargs["data"]["queryResultsFormat"], "ARROW")
        self.assertEqual(
            call_args.kwargs["data"]["arrowSerializationOptions"]["bufferCompression"],
            "LZ4_FRAME",
        )

    def test_row_iterator_to_dataframe_iterable_when_format_is_arrow(self):
        pytest.importorskip("pandas")
        mock_client = mock.MagicMock()
        mock_client._get_shared_bqstorage_client.return_value = mock.MagicMock()

        iterator = RowIterator(
            client=mock_client,
            api_request=mock.MagicMock(),
            path=None,
            schema=(),
            query_results_format="ARROW",
        )

        mock_batch = mock.MagicMock()
        mock_batch.to_pandas.return_value = "df_chunk"

        with mock.patch.object(
            iterator, "to_arrow_iterable", return_value=[mock_batch]
        ):
            with mock.patch("google.cloud.bigquery.table._pandas_helpers"):
                dfs = list(iterator.to_dataframe_iterable())
                self.assertEqual(dfs, ["df_chunk"])

    def test_row_iterator_to_dataframe_when_format_is_arrow(self):
        pytest.importorskip("pandas")
        mock_client = mock.MagicMock()
        mock_client._get_shared_bqstorage_client.return_value = mock.MagicMock()

        iterator = RowIterator(
            client=mock_client,
            api_request=mock.MagicMock(),
            path=None,
            schema=(),
            query_results_format="ARROW",
        )

        mock_table = mock.MagicMock()
        mock_table.__iter__.return_value = iter([])
        mock_table.to_pandas.return_value = "full_df"

        with mock.patch.object(iterator, "to_arrow", return_value=mock_table):
            with mock.patch("google.cloud.bigquery.table._pandas_helpers"):
                df = iterator.to_dataframe()
                self.assertEqual(df, "full_df")


def _query_and_wait(client, **kwargs):
    return _job_helpers.query_and_wait(
        client,
        "SELECT 1",
        project="p",
        location="us",
        retry=None,
        job_retry=None,
        **{"job_config": None, **kwargs},
    )


def test_query_and_wait_compression_codec_requires_arrow(check_dependencies):
    client = mock.MagicMock(spec=Client)

    with pytest.raises(ValueError, match="compression_codec requires"):
        _query_and_wait(client, compression_codec="LZ4_FRAME")

    client._call_api.assert_not_called()
    check_dependencies.assert_not_called()


def test_query_and_wait_without_arrow_skips_dependency_check(check_dependencies):
    client = mock.MagicMock(spec=Client)
    client._call_api.return_value = {
        "jobReference": {"projectId": "p", "jobId": "j", "location": "us"},
        "jobComplete": True,
        "rows": [],
        "schema": {"fields": []},
    }

    _query_and_wait(client)

    check_dependencies.assert_not_called()


def test_query_and_wait_arrow_allows_write_append(check_dependencies):
    client = make_client(
        default_query_job_config=QueryJobConfig(
            destination="p.d.t", write_disposition=WriteDisposition.WRITE_APPEND
        )
    )
    client._call_api = mock.Mock(side_effect=RuntimeError("sent"))

    with pytest.raises(RuntimeError, match="sent"):
        client.query_and_wait("SELECT 1", query_results_format="ARROW")

    check_dependencies.assert_called_once_with()
    client._call_api.assert_called_once()


def test_query_and_wait_arrow_checks_dependencies_before_sending(check_dependencies):
    check_dependencies.side_effect = exceptions.BigQueryStorageNotFoundError("missing")
    client = mock.MagicMock(spec=Client)

    with pytest.raises(exceptions.BigQueryStorageNotFoundError):
        _query_and_wait(client, query_results_format="ARROW")

    client._call_api.assert_not_called()


def test_check_dependencies_requires_pyarrow():
    error = exceptions.LegacyPyarrowError("pyarrow is not installed")
    with mock.patch.object(
        _versions_helpers.PYARROW_VERSIONS, "try_import", side_effect=error
    ) as try_import:
        with pytest.raises(exceptions.LegacyPyarrowError):
            _check_dependencies()

    try_import.assert_called_once_with(raise_if_error=True)


def test_check_dependencies_requires_bigquery_storage():
    error = exceptions.BigQueryStorageNotFoundError("not installed")
    with (
        mock.patch.object(_versions_helpers.PYARROW_VERSIONS, "try_import"),
        mock.patch.object(
            _versions_helpers.BQ_STORAGE_VERSIONS, "try_import", side_effect=error
        ) as try_import,
    ):
        with pytest.raises(exceptions.BigQueryStorageNotFoundError):
            _check_dependencies()

    try_import.assert_called_once_with(raise_if_error=True)


@pytest.mark.parametrize("supported", [True, False])
def test_check_dependencies_requires_read_rows_arrow_options(supported):
    versions_type = type(_versions_helpers.BQ_STORAGE_VERSIONS)
    with (
        mock.patch.object(_versions_helpers.PYARROW_VERSIONS, "try_import"),
        mock.patch.object(_versions_helpers.BQ_STORAGE_VERSIONS, "try_import"),
        mock.patch.object(
            versions_type,
            "supports_arrow_serialization_options",
            new_callable=mock.PropertyMock,
            return_value=supported,
        ),
        mock.patch.object(
            versions_type,
            "installed_version",
            new_callable=mock.PropertyMock,
            return_value=packaging.version.Version("2.42.0"),
        ),
    ):
        if supported:
            _check_dependencies()
        else:
            with pytest.raises(
                exceptions.LegacyBigQueryStorageError,
                match=r'pip install "google-cloud-bigquery\[bqstorage\]".*'
                r"\(version found: 2\.42\.0\)",
            ):
                _check_dependencies()


def test_query_and_wait_arrow_sends_default_serialization_options():
    client = mock.MagicMock(spec=Client)
    client._call_api.return_value = {
        "jobReference": {"projectId": "p", "jobId": "j", "location": "us"},
        "jobComplete": True,
        "schema": {"fields": []},
    }

    row_iterator = _query_and_wait(client, query_results_format="ARROW")

    data = client._call_api.call_args.kwargs["data"]
    assert data["arrowSerializationOptions"] == _DEFAULT_QUERY_OPTIONS
    assert "arrowSerializationOptions" not in data["formatOptions"]
    assert row_iterator._arrow_serialization_options == _DEFAULT_QUERY_OPTIONS


def test_query_and_wait_without_arrow_sends_no_serialization_options():
    client = mock.MagicMock(spec=Client)
    client._call_api.return_value = {
        "jobReference": {"projectId": "p", "jobId": "j", "location": "us"},
        "jobComplete": True,
        "rows": [],
        "schema": {"fields": []},
    }

    row_iterator = _query_and_wait(client)

    assert "arrowSerializationOptions" not in client._call_api.call_args.kwargs["data"]
    assert row_iterator._arrow_serialization_options is None


def test_query_and_wait_arrow_waits_with_the_same_options():
    client = mock.MagicMock(spec=Client)
    client._call_api.return_value = {
        "jobReference": {"projectId": "p", "jobId": "j", "location": "us"},
        "jobComplete": False,
    }

    with (
        mock.patch.object(_job_helpers, "_to_query_job") as to_query_job,
        mock.patch.object(_job_helpers, "_wait_or_cancel") as wait_or_cancel,
    ):
        _query_and_wait(client, query_results_format="ARROW", compression_codec="ZSTD")

    wait_or_cancel.assert_called_once_with(
        to_query_job.return_value,
        api_timeout=mock.ANY,
        wait_timeout=mock.ANY,
        retry=mock.ANY,
        page_size=mock.ANY,
        max_results=mock.ANY,
        query_results_format="ARROW",
        arrow_serialization_options={
            "bufferCompression": "ZSTD",
            "picosTimestampPrecision": "TIMESTAMP_PRECISION_MICROS",
        },
        callback=mock.ANY,
    )


def test_wait_or_cancel_sets_arrow_serialization_options():
    job = mock.MagicMock(dry_run=False)
    job.result.return_value = RowIterator(
        client=mock.MagicMock(), api_request=mock.MagicMock(), path=None, schema=()
    )

    expected = dict(_DEFAULT_QUERY_OPTIONS)

    rows = _job_helpers._wait_or_cancel(
        job,
        api_timeout=None,
        wait_timeout=None,
        retry=None,
        page_size=None,
        max_results=None,
        query_results_format="ARROW",
        arrow_serialization_options=_DEFAULT_QUERY_OPTIONS,
    )

    assert rows._query_results_format == "ARROW"
    assert rows._arrow_serialization_options == expected


def test_query_and_wait_arrow_jobs_insert_omits_arrow_fields():
    client = make_client()
    client._call_api = mock.Mock(
        return_value={
            "jobReference": {"projectId": "PROJECT", "jobId": "j", "location": "US"},
            "configuration": {"query": {"query": "SELECT 1"}},
            "status": {"state": "RUNNING"},
        }
    )
    # jobs.query doesn't accept a destination table, so this uses jobs.insert.
    job_config = QueryJobConfig(destination="PROJECT.dataset.table")

    with mock.patch.object(_job_helpers, "_wait_or_cancel") as wait_or_cancel:
        client.query_and_wait(
            "SELECT 1", job_config=job_config, query_results_format="ARROW"
        )

    (insert_call,) = client._call_api.call_args_list
    assert insert_call.kwargs["path"] == "/projects/PROJECT/jobs"
    query_config = insert_call.kwargs["data"]["configuration"]["query"]
    assert "queryResultsFormat" not in query_config
    assert "arrowSerializationOptions" not in query_config
    wait_or_cancel.assert_called_once_with(
        mock.ANY,
        api_timeout=mock.ANY,
        wait_timeout=mock.ANY,
        retry=mock.ANY,
        page_size=mock.ANY,
        max_results=mock.ANY,
        query_results_format="ARROW",
        arrow_serialization_options=_DEFAULT_QUERY_OPTIONS,
        explicit_destination=True,
        callback=mock.ANY,
    )
    assert wait_or_cancel.call_args.kwargs["page_size"] == 0


def test_supported_by_jobs_query_includes_arrow_serialization_options():
    body = {
        "query": "SELECT 1",
        "queryResultsFormat": "ARROW",
        "arrowSerializationOptions": _DEFAULT_QUERY_OPTIONS,
    }

    assert _job_helpers._supported_by_jobs_query(body)


@pytest.mark.parametrize("codec", ["LZ4_FRAME", QueryResultsCompressionCodec.LZ4_FRAME])
def test_serialization_options_accepts_str_and_enum(codec):
    assert _arrow_query.serialization_options(codec) == {
        "bufferCompression": "LZ4_FRAME",
        "picosTimestampPrecision": "TIMESTAMP_PRECISION_MICROS",
    }


def test_read_rows_options():
    assert _arrow_query._read_rows_options(None) == _DEFAULT_READ_OPTIONS
    assert _arrow_query._read_rows_options(
        {
            "bufferCompression": "ZSTD",
            "picosTimestampPrecision": "TIMESTAMP_PRECISION_PICOS",
        }
    ) == {
        "buffer_compression": "ZSTD",
        "picos_timestamp_precision": "TIMESTAMP_PRECISION_PICOS",
    }


def test_download_arrow_from_job_id_sends_query_options_on_read_rows():
    bqstorage_client = mock.MagicMock()
    bqstorage_client.read_rows.return_value = []
    iterator = RowIterator(
        client=mock.MagicMock(),
        api_request=mock.MagicMock(),
        path=None,
        schema=(),
        project="p",
        location="US",
        job_id="j",
        query_results_format="ARROW",
        arrow_serialization_options={
            "bufferCompression": "LZ4_FRAME",
            "picosTimestampPrecision": "TIMESTAMP_PRECISION_MICROS",
        },
    )

    with mock.patch("google.cloud.bigquery._arrow_query.pyarrow"):
        list(iterator._download_arrow_from_job_id(bqstorage_client=bqstorage_client))

    bqstorage_client.read_rows.assert_called_once_with(
        "projects/p/locations/US/jobs/j/streams/_default",
        offset=0,
        timeout=None,
        arrow_serialization_options={
            "buffer_compression": "LZ4_FRAME",
            "picos_timestamp_precision": "TIMESTAMP_PRECISION_MICROS",
        },
    )


@pytest.mark.parametrize(
    "timestamp_precision",
    [TimestampPrecision.MICROSECOND, TimestampPrecision.PICOSECOND],
)
def test_query_and_wait_timestamp_precision_requires_arrow(
    check_dependencies, timestamp_precision
):
    client = mock.MagicMock(spec=Client)

    with pytest.raises(ValueError, match="timestamp_precision requires"):
        _query_and_wait(client, timestamp_precision=timestamp_precision)

    client._call_api.assert_not_called()
    check_dependencies.assert_not_called()


@pytest.mark.parametrize(
    ("timestamp_precision", "expected"),
    [
        (None, "TIMESTAMP_PRECISION_MICROS"),
        (TimestampPrecision.MICROSECOND, "TIMESTAMP_PRECISION_MICROS"),
        (TimestampPrecision.PICOSECOND, "TIMESTAMP_PRECISION_PICOS"),
    ],
)
def test_client_query_and_wait_arrow_timestamp_precision(timestamp_precision, expected):
    client = make_client()
    client._call_api = mock.Mock(
        return_value={
            "jobReference": {"projectId": "PROJECT", "jobId": "j", "location": "US"},
            "jobComplete": True,
            "schema": {"fields": []},
        }
    )

    rows = client.query_and_wait(
        "SELECT 1",
        query_results_format="ARROW",
        timestamp_precision=timestamp_precision,
    )

    data = client._call_api.call_args.kwargs["data"]
    assert data["arrowSerializationOptions"]["picosTimestampPrecision"] == expected
    assert rows._arrow_serialization_options["picosTimestampPrecision"] == expected
    # formatOptions only shapes STRUCT_ENCODING rows, which ARROW doesn't return.
    assert "timestampOutputFormat" not in data["formatOptions"]


def _arrow_query_response(**fields):
    return {
        "jobReference": {"projectId": "p", "jobId": "j", "location": "us"},
        "jobComplete": True,
        "arrowSchema": {"serializedSchema": "c2NoZW1h"},
        **fields,
    }


@pytest.mark.parametrize(
    "response",
    [
        _arrow_query_response(pageRowCount="10", totalRows="25", pageToken="next"),
        _arrow_query_response(jobComplete=False),
        # A cache hit too large to return inline has no pageRowCount and
        # totalRows is 0, but it still has a pageToken.
        _arrow_query_response(totalRows="0", pageToken="next"),
    ],
    ids=["some_rows_inline", "no_rows_inline", "cache_hit_no_rows_inline"],
)
def test_query_and_wait_arrow_waits_without_fetching_rows(response):
    client = mock.MagicMock(spec=Client)
    client._call_api.return_value = response

    with (
        mock.patch.object(_job_helpers, "_to_query_job") as to_query_job,
        mock.patch.object(_job_helpers, "_wait_or_cancel") as wait_or_cancel,
    ):
        rows = _query_and_wait(client, query_results_format="ARROW", page_size=10)

    assert rows is wait_or_cancel.return_value
    assert wait_or_cancel.call_args.args[0] is to_query_job.return_value
    assert wait_or_cancel.call_args.kwargs["page_size"] == 0
    # page_size still sets the size of the first page from jobs.query.
    assert client._call_api.call_args.kwargs["data"]["maxResults"] == 10


def test_query_and_wait_arrow_all_rows_inline_doesnt_wait():
    client = mock.MagicMock(spec=Client)
    client._call_api.return_value = _arrow_query_response(
        pageRowCount="25", totalRows="25"
    )

    with mock.patch.object(_job_helpers, "_wait_or_cancel") as wait_or_cancel:
        rows = _query_and_wait(client, query_results_format="ARROW")

    wait_or_cancel.assert_not_called()
    assert rows._first_page_response["pageRowCount"] == "25"


def test_query_and_wait_without_arrow_waits_with_page_size():
    client = mock.MagicMock(spec=Client)
    client._call_api.return_value = {
        "jobReference": {"projectId": "p", "jobId": "j", "location": "us"},
        "jobComplete": True,
        "rows": [],
        "schema": {"fields": []},
        "pageToken": "next",
    }

    with (
        mock.patch.object(_job_helpers, "_to_query_job"),
        mock.patch.object(_job_helpers, "_wait_or_cancel") as wait_or_cancel,
    ):
        _query_and_wait(client, page_size=10)

    assert wait_or_cancel.call_args.kwargs["page_size"] == 10


def _arrow_pages(*row_counts):
    """Serialize an Arrow schema and record batches of consecutive x values."""
    pyarrow = pytest.importorskip("pyarrow")
    schema = pyarrow.schema([("x", pyarrow.int64())])
    batches, start = [], 1
    for count in row_counts:
        values = pyarrow.array(range(start, start + count), type=pyarrow.int64())
        batch = pyarrow.record_batch([values], schema=schema)
        batches.append(batch.serialize().to_pybytes())
        start += count
    return schema.serialize().to_pybytes(), batches


def _stream_response(batch):
    return mock.Mock(
        arrow_schema=None,
        arrow_record_batch=mock.Mock(serialized_record_batch=batch),
    )


def _limited_iterator(row_counts, total_rows, max_results):
    """A RowIterator whose first page has row_counts[0] rows and whose stream
    returns the rest, plus its mock BigQuery Storage client and stream.
    """
    schema, batches = _arrow_pages(*row_counts)
    reader = mock.MagicMock()
    reader.__iter__.return_value = iter(
        [_stream_response(batch) for batch in batches[1:]]
    )
    bqstorage_client = mock.MagicMock()
    bqstorage_client.read_rows.return_value = reader
    first_page_response = {
        "jobComplete": True,
        "totalRows": str(total_rows),
        "arrowSchema": {"serializedSchema": base64.b64encode(schema).decode()},
        "arrowRecordBatch": {
            "serializedRecordBatch": base64.b64encode(batches[0]).decode()
        },
    }
    # BigQuery sends a pageToken whenever rows remain after the first page.
    if row_counts[0] < total_rows:
        first_page_response["pageToken"] = "next"
    iterator = RowIterator(
        client=mock.MagicMock(),
        api_request=mock.MagicMock(),
        path=None,
        schema=(),
        max_results=max_results,
        project="p",
        location="US",
        job_id="j",
        query_results_format="ARROW",
        first_page_response=first_page_response,
    )
    return iterator, bqstorage_client, reader


def _values(batches):
    return [value for batch in batches for value in batch.column(0).to_pylist()]


def test_download_arrow_max_results_within_first_page_skips_stream():
    iterator, bqstorage_client, _ = _limited_iterator([10, 15], 25, max_results=4)

    batches = list(iterator._download_arrow_from_job_id(bqstorage_client))

    assert _values(batches) == [1, 2, 3, 4]
    bqstorage_client.read_rows.assert_not_called()


def test_download_arrow_max_results_across_stream_cancels_it():
    iterator, bqstorage_client, reader = _limited_iterator(
        [10, 10, 5], 25, max_results=15
    )

    batches = list(iterator._download_arrow_from_job_id(bqstorage_client))

    assert _values(batches) == list(range(1, 16))
    assert bqstorage_client.read_rows.call_args.kwargs["offset"] == 10
    reader.cancel.assert_called_once_with()


def test_download_arrow_max_results_past_last_row_reads_everything():
    iterator, bqstorage_client, reader = _limited_iterator(
        [10, 10, 5], 25, max_results=100
    )

    batches = list(iterator._download_arrow_from_job_id(bqstorage_client))

    assert _values(batches) == list(range(1, 26))
    reader.cancel.assert_not_called()


def test_download_arrow_cancels_stream_when_closed_early():
    iterator, bqstorage_client, reader = _limited_iterator(
        [10, 10, 5], 25, max_results=None
    )
    batches = iterator._download_arrow_from_job_id(bqstorage_client)

    next(batches)  # first page
    next(batches)  # first stream batch
    batches.close()

    reader.cancel.assert_called_once_with()


def test_download_arrow_raises_stream_errors_after_earlier_batches():
    iterator, bqstorage_client, reader = _limited_iterator(
        [10, 10, 5], 25, max_results=None
    )
    first_stream_response = next(reader.__iter__.return_value)

    def fail_after_one_response():
        yield first_stream_response
        raise core_exceptions.PermissionDenied("stream failed")

    reader.__iter__.return_value = fail_after_one_response()
    received = []

    with pytest.raises(core_exceptions.PermissionDenied):
        for batch in iterator._download_arrow_from_job_id(bqstorage_client):
            received.append(batch)

    # The caller gets the error after the batches that arrived before it, so
    # a partial result never looks complete.
    assert _values(received) == list(range(1, 21))
    reader.cancel.assert_called_once_with()


def test_query_and_wait_arrow_first_page_reaching_max_results_doesnt_wait():
    client = mock.MagicMock(spec=Client)
    client._call_api.return_value = _arrow_query_response(
        pageRowCount="10", totalRows="25", pageToken="next"
    )

    with mock.patch.object(_job_helpers, "_wait_or_cancel") as wait_or_cancel:
        rows = _query_and_wait(client, query_results_format="ARROW", max_results=10)

    wait_or_cancel.assert_not_called()
    assert rows.max_results == 10
    assert client._call_api.call_args.kwargs["data"]["maxResults"] == 10


def test_to_arrow_with_arrow_format_and_max_results_keeps_bqstorage_client():
    pyarrow = pytest.importorskip("pyarrow")
    bqstorage_client = mock.MagicMock()
    iterator = RowIterator(
        client=mock.MagicMock(),
        api_request=mock.MagicMock(),
        path=None,
        schema=(),
        max_results=5,
        query_results_format="ARROW",
    )
    batch = pyarrow.record_batch([pyarrow.array([1, 2])], names=["x"])

    with (
        mock.patch.object(
            iterator, "to_arrow_iterable", return_value=iter([batch])
        ) as to_arrow_iterable,
        warnings.catch_warnings(record=True) as caught,
    ):
        warnings.simplefilter("always")
        table = iterator.to_arrow(bqstorage_client=bqstorage_client)

    to_arrow_iterable.assert_called_once_with(
        bqstorage_client=bqstorage_client, timeout=None
    )
    assert table.num_rows == 2
    # ARROW results apply max_results while streaming, so there's no warning
    # about falling back to the REST API.
    assert not [w for w in caught if "max_results" in str(w.message)]


def test_download_arrow_uses_passed_client_and_leaves_it_open():
    iterator, bqstorage_client, _ = _limited_iterator([10, 15], 25, max_results=None)

    batches = list(iterator._download_arrow_from_job_id(bqstorage_client))

    assert _values(batches) == list(range(1, 26))
    iterator.client._get_shared_bqstorage_client.assert_not_called()
    bqstorage_client._transport.close.assert_not_called()


def test_download_arrow_needs_a_client_only_to_stream():
    iterator, _, _ = _limited_iterator([10, 15], 25, max_results=None)
    iterator.client = None
    batches = iterator._download_arrow_from_job_id()

    assert next(batches).num_rows == 10
    with pytest.raises(ValueError, match="RowIterator client is None"):
        next(batches)


def test_to_arrow_with_arrow_format_reads_with_the_shared_client():
    pyarrow = pytest.importorskip("pyarrow")
    client = mock.MagicMock()
    iterator = RowIterator(
        client=client,
        api_request=mock.MagicMock(),
        path=None,
        schema=(),
        query_results_format="ARROW",
    )
    batch = pyarrow.record_batch([pyarrow.array([1, 2])], names=["x"])

    with mock.patch.object(
        iterator, "to_arrow_iterable", return_value=iter([batch])
    ) as to_arrow_iterable:
        table = iterator.to_arrow()

    assert table.num_rows == 2
    # to_arrow() doesn't create (and then close) a client of its own; the
    # stream uses the BigQuery client's shared one.
    client._ensure_bqstorage_client.assert_not_called()
    assert to_arrow_iterable.call_args.kwargs["bqstorage_client"] is None


@pytest.mark.parametrize(
    ("job_config", "expected"),
    [
        (QueryJobConfig(destination="p.d.t"), True),
        # jobs.query doesn't accept a priority either, so this also runs
        # through jobs.insert, without a destination.
        (QueryJobConfig(priority="INTERACTIVE"), False),
    ],
    ids=["destination", "no_destination"],
)
def test_query_and_wait_arrow_marks_explicit_destination(job_config, expected):
    client = mock.MagicMock(spec=Client)

    with (
        mock.patch.object(_job_helpers, "query_jobs_insert") as query_jobs_insert,
        mock.patch.object(_job_helpers, "_wait_or_cancel") as wait_or_cancel,
    ):
        _query_and_wait(client, job_config=job_config, query_results_format="ARROW")

    wait_or_cancel.assert_called_once_with(
        query_jobs_insert.return_value,
        api_timeout=mock.ANY,
        wait_timeout=mock.ANY,
        retry=mock.ANY,
        page_size=mock.ANY,
        max_results=mock.ANY,
        query_results_format="ARROW",
        arrow_serialization_options=mock.ANY,
        explicit_destination=expected,
        callback=mock.ANY,
    )


def test_wait_or_cancel_sets_explicit_destination():
    job = mock.MagicMock(dry_run=False)
    job.result.return_value = RowIterator(
        client=mock.MagicMock(), api_request=mock.MagicMock(), path=None, schema=()
    )
    assert not job.result.return_value._explicit_destination

    rows = _job_helpers._wait_or_cancel(
        job,
        api_timeout=None,
        wait_timeout=None,
        retry=None,
        page_size=0,
        max_results=None,
        explicit_destination=True,
    )

    assert rows._explicit_destination


def _destination_iterator(row_counts, serialized_schema=None):
    """A RowIterator for a query with an explicit destination table, plus its
    mock BigQuery Storage client.
    """
    bigquery_storage = pytest.importorskip("google.cloud.bigquery_storage")
    options = bigquery_storage.types.ArrowSerializationOptions
    if "picos_timestamp_precision" not in options.meta.fields:
        # query_and_wait() rejects ARROW with this release before it runs.
        pytest.skip("google-cloud-bigquery-storage has no timestamp precision")
    schema, batches = _arrow_pages(*row_counts)
    reader = mock.MagicMock()
    reader.__iter__.return_value = iter([_stream_response(batch) for batch in batches])
    stream = mock.Mock()
    stream.name = "projects/p/locations/us/sessions/s/streams/0"
    session = mock.Mock(streams=[stream] if row_counts else [])
    session.arrow_schema.serialized_schema = (
        schema if serialized_schema is None else serialized_schema
    )
    bqstorage_client = mock.MagicMock()
    bqstorage_client.create_read_session.return_value = session
    bqstorage_client.read_rows.return_value = reader
    iterator = RowIterator(
        client=mock.MagicMock(project="billing-project"),
        api_request=mock.MagicMock(),
        path=None,
        schema=(),
        table=TableReference.from_string("p.d.t"),
        project="p",
        location="US",
        job_id="j",
        query_results_format="ARROW",
    )
    iterator._explicit_destination = True
    return iterator, bqstorage_client


def test_download_arrow_explicit_destination_reads_a_read_session():
    iterator, bqstorage_client = _destination_iterator([10, 15])
    from google.cloud import bigquery_storage

    batches = list(iterator._download_arrow_from_job_id(bqstorage_client))

    assert _values(batches) == list(range(1, 26))
    bqstorage_client.create_read_session.assert_called_once_with(
        parent="projects/billing-project",
        read_session=bigquery_storage.types.stream.ReadSession(
            table="projects/p/datasets/d/tables/t",
            data_format=bigquery_storage.types.stream.DataFormat.ARROW,
            read_options=bigquery_storage.types.stream.ReadSession.TableReadOptions(
                arrow_serialization_options=_DEFAULT_READ_OPTIONS
            ),
        ),
        max_stream_count=1,
        timeout=None,
    )
    # The read session carries the serialization options, so ReadRows doesn't.
    bqstorage_client.read_rows.assert_called_once_with(
        "projects/p/locations/us/sessions/s/streams/0", offset=0, timeout=None
    )


@pytest.mark.parametrize(
    ("serialized_schema", "expected_names"),
    [(None, ["x"]), (b"", [])],
    ids=["with_schema", "without_schema"],
)
def test_download_arrow_explicit_destination_without_rows(
    serialized_schema, expected_names
):
    iterator, bqstorage_client = _destination_iterator(
        [], serialized_schema=serialized_schema
    )

    (batch,) = iterator._download_arrow_from_job_id(bqstorage_client)

    assert batch.num_rows == 0
    assert batch.schema.names == expected_names
    bqstorage_client.read_rows.assert_not_called()


def _zero_row_iterator():
    """A RowIterator whose jobs.query response has a schema and no rows."""
    schema, _ = _arrow_pages()
    return RowIterator(
        client=mock.MagicMock(),
        api_request=mock.MagicMock(),
        path=None,
        schema=(),
        project="p",
        location="US",
        job_id="j",
        query_results_format="ARROW",
        first_page_response={
            "jobComplete": True,
            "totalRows": "0",
            "arrowSchema": {"serializedSchema": base64.b64encode(schema).decode()},
            # A response without rows carries no serialized batch.
            "arrowRecordBatch": {},
        },
    )


def test_download_arrow_zero_rows_inline_keep_the_schema():
    iterator = _zero_row_iterator()

    (batch,) = iterator._download_arrow_from_job_id()

    assert batch.num_rows == 0
    assert batch.schema.names == ["x"]
    iterator.client._get_shared_bqstorage_client.assert_not_called()


def test_to_arrow_zero_rows_keep_the_schema():
    table = _zero_row_iterator().to_arrow()

    assert table.num_rows == 0
    assert table.schema.names == ["x"]


def test_download_arrow_zero_rows_streamed_use_the_query_results_schema():
    pyarrow = pytest.importorskip("pyarrow")
    from google.cloud.bigquery.schema import SchemaField

    bqstorage_client = mock.MagicMock()
    # The default job stream sends no responses for zero rows.
    bqstorage_client.read_rows.return_value = []
    iterator = RowIterator(
        client=mock.MagicMock(),
        api_request=mock.MagicMock(),
        path=None,
        schema=[SchemaField("x", "INTEGER")],
        project="p",
        location="US",
        job_id="j",
        query_results_format="ARROW",
        first_page_response={"jobComplete": False},
    )

    (batch,) = iterator._download_arrow_from_job_id(bqstorage_client)

    assert batch.num_rows == 0
    assert batch.schema.names == ["x"]
    assert batch.schema.field("x").type == pyarrow.int64()


def test_download_arrow_rows_yield_no_extra_empty_batch():
    schema, batches = _arrow_pages(3)
    iterator = RowIterator(
        client=mock.MagicMock(),
        api_request=mock.MagicMock(),
        path=None,
        schema=(),
        project="p",
        location="US",
        job_id="j",
        query_results_format="ARROW",
        first_page_response={
            "jobComplete": True,
            "totalRows": "3",
            "arrowSchema": {"serializedSchema": base64.b64encode(schema).decode()},
            "arrowRecordBatch": {
                "serializedRecordBatch": base64.b64encode(batches[0]).decode()
            },
        },
    )

    (batch,) = iterator._download_arrow_from_job_id()

    assert batch.num_rows == 3


def test_to_arrow_iterable_reads_inline_result_twice():
    # With JOB_CREATION_OPTIONAL and every row inline there's no job to
    # stream from, so the first page has to stay on the iterator for the
    # result to be read again.
    pyarrow = pytest.importorskip("pyarrow")
    batch = pyarrow.record_batch([pyarrow.array([1, 2, 3])], names=["x"])
    first_page = {
        "jobComplete": True,
        "totalRows": "3",
        "pageRowCount": "3",
        "arrowSchema": {
            "serializedSchema": base64.b64encode(
                batch.schema.serialize().to_pybytes()
            ).decode()
        },
        "arrowRecordBatch": {
            "serializedRecordBatch": base64.b64encode(
                batch.serialize().to_pybytes()
            ).decode()
        },
    }
    iterator = RowIterator(
        client=mock.MagicMock(),
        api_request=mock.MagicMock(),
        path=None,
        schema=(),
        first_page_response=first_page,
        project="p",
        location="US",
        job_id=None,
        query_results_format="ARROW",
    )
    bqstorage_client = mock.MagicMock()

    first_read = list(iterator.to_arrow_iterable(bqstorage_client=bqstorage_client))
    second_read = list(iterator.to_arrow_iterable(bqstorage_client=bqstorage_client))

    assert first_read == [batch]
    assert second_read == [batch]
    bqstorage_client.read_rows.assert_not_called()


if __name__ == "__main__":
    unittest.main()
