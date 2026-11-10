# Copyright 2016 Google LLC All rights reserved.
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
from datetime import datetime, timedelta
from threading import Event, Lock, Thread
from typing import Mapping

import mock
from google.api_core import gapic_v1
from google.api_core.exceptions import Aborted, InternalServerError, NotFound
from google.api_core.retry import Retry

from google.cloud.spanner_admin_database_v1 import Database
from google.cloud.spanner_v1 import (
    BeginTransactionRequest,
    DirectedReadOptions,
    RequestOptions,
    TransactionOptions,
    TransactionSelector,
    _opentelemetry_tracing,
)
from google.cloud.spanner_v1._helpers import (
    AtomicCounter,
    _augment_errors_with_request_id,
    _metadata_with_request_id,
    _metadata_with_request_id_and_req_id,
)
from google.cloud.spanner_v1.param_types import INT64
from google.cloud.spanner_v1.request_id_header import (
    REQ_RAND_PROCESS_ID,
    build_request_id,
)
from google.cloud.spanner_v1.snapshot import _SnapshotBase
from tests._builders import (
    build_precommit_token_pb,
    build_session,
    build_snapshot,
    build_spanner_api,
    build_transaction_pb,
)
from tests._helpers import (
    HAS_OPENTELEMETRY_INSTALLED,
    LIB_VERSION,
    OpenTelemetryBase,
    StatusCode,
    enrich_with_otel_scope,
)

TABLE_NAME = "citizens"
COLUMNS = ["email", "first_name", "last_name", "age"]
_DEFAULT_EXPECTED_REQUEST_OPTIONS = object()
SQL_QUERY = """\
SELECT first_name, last_name, age FROM citizens ORDER BY age"""
SQL_QUERY_WITH_PARAM = """
SELECT first_name, last_name, email FROM citizens WHERE age <= @max_age"""
PARAMS = {"max_age": 30}
PARAM_TYPES = {"max_age": INT64}
SQL_QUERY_WITH_BYTES_PARAM = """\
SELECT image_name FROM images WHERE @bytes IN image_data"""
PARAMS_WITH_BYTES = {"bytes": b"FACEDACE"}
RESUME_TOKEN = b"DEADBEEF"
TXN_ID = b"DEAFBEAD"
SECONDS = 3
MICROS = 123456
DURATION = timedelta(seconds=SECONDS, microseconds=MICROS)
TIMESTAMP = datetime.now()

BASE_ATTRIBUTES = {
    "db.type": "spanner",
    "db.url": "spanner.googleapis.com",
    "db.instance": "testing",
    "net.host.name": "spanner.googleapis.com",
    "cloud.region": "global",
    "gcp.client.service": "spanner",
    "gcp.client.version": LIB_VERSION,
    "gcp.client.repo": "googleapis/python-spanner",
    "gcp.resource.name": _opentelemetry_tracing.GCP_RESOURCE_NAME_PREFIX + "testing",
}
enrich_with_otel_scope(BASE_ATTRIBUTES)

DIRECTED_READ_OPTIONS = {
    "include_replicas": {
        "replica_selections": [
            {
                "location": "us-west1",
                "type_": DirectedReadOptions.ReplicaSelection.Type.READ_ONLY,
            },
        ],
        "auto_failover_disabled": True,
    },
}
DIRECTED_READ_OPTIONS_FOR_CLIENT = {
    "include_replicas": {
        "replica_selections": [
            {
                "location": "us-east1",
            },
        ],
    },
}

PRECOMMIT_TOKEN_1 = build_precommit_token_pb(precommit_token=b"1", seq_num=1)
PRECOMMIT_TOKEN_2 = build_precommit_token_pb(precommit_token=b"2", seq_num=2)

# Common errors for testing.
INTERNAL_SERVER_ERROR_UNEXPECTED_EOS = InternalServerError(
    "Received unexpected EOS on DATA frame from server"
)


class _Derived(_SnapshotBase):
    """A minimally-implemented _SnapshotBase-derived class for testing"""

    transaction_tag = None

    # Use a simplified implementation of _build_transaction_options_pb
    # that always returns the same transaction options.
    TRANSACTION_OPTIONS = TransactionOptions()

    def _build_transaction_options_pb(self) -> TransactionOptions:
        return self.TRANSACTION_OPTIONS


class Test_restart_on_unavailable(OpenTelemetryBase):
    def build_spanner_api(self):
        from google.cloud.spanner_v1 import SpannerClient

        return mock.create_autospec(SpannerClient, instance=True)

    def _call_fut(
        self,
        derived,
        restart,
        request,
        span_name=None,
        session=None,
        attributes=None,
        metadata=None,
    ):
        from google.cloud.spanner_v1.snapshot import _restart_on_unavailable

        return _restart_on_unavailable(
            restart,
            request,
            metadata,
            span_name,
            session,
            attributes,
            transaction=derived,
            request_id_manager=None if not session else session._database,
        )

    def _make_item(self, value, resume_token=b"", metadata=None, last=False):
        return mock.Mock(
            value=value,
            resume_token=resume_token,
            metadata=metadata,
            precommit_token=None,
            last=last,
            _pb=None,
            spec=["value", "resume_token", "metadata", "precommit_token", "last"],
        )

    def test_iteration_w_empty_raw(self):
        raw = _MockIterator()
        request = mock.Mock(test="test", spec=["test", "resume_token"])
        restart = mock.Mock(spec=[], return_value=raw)
        database = _Database()
        database.spanner_api = build_spanner_api()
        session = _Session(database)
        derived = _build_snapshot_derived(session)
        resumable = self._call_fut(derived, restart, request, session=session)
        self.assertEqual(list(resumable), [])
        restart.assert_called_once_with(
            request=request,
            metadata=[
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                )
            ],
        )
        self.assertNoSpans()

    def test_iteration_w_non_empty_raw(self):
        ITEMS = (self._make_item(0), self._make_item(1))
        raw = _MockIterator(*ITEMS)
        request = mock.Mock(test="test", spec=["test", "resume_token"])
        restart = mock.Mock(spec=[], return_value=raw)
        database = _Database()
        database.spanner_api = build_spanner_api()
        session = _Session(database)
        derived = _build_snapshot_derived(session)
        resumable = self._call_fut(derived, restart, request, session=session)
        self.assertEqual(list(resumable), list(ITEMS))
        restart.assert_called_once_with(
            request=request,
            metadata=[
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                )
            ],
        )
        self.assertNoSpans()

    def test_restart_on_unavailable_last(self):
        item_last = self._make_item(0, last=True)
        trailing_item = self._make_item(1)

        raw = _MockIterator(item_last, trailing_item)
        restart = mock.Mock(return_value=raw)
        request = mock.Mock(test="test", spec=["test", "resume_token"])
        database = _Database()
        database.spanner_api = build_spanner_api()
        session = _Session(database)
        derived = _build_snapshot_derived(session)

        with mock.patch("google.cloud.spanner_v1.snapshot._drain_stream") as mock_drain:
            resumable = self._call_fut(derived, restart, request, session=session)
            items = list(resumable)

            mock_drain.assert_called_once_with(raw)
            self.assertEqual(len(items), 1)
            self.assertEqual(items[0], item_last)

    def test_restart_on_unavailable_finally_cancels_on_early_termination(self):
        item = self._make_item(0, last=False)
        raw = _MockIterator(item)
        raw.cancel = mock.Mock()
        restart = mock.Mock(return_value=raw)
        request = mock.Mock(test="test", spec=["test", "resume_token"])
        database = _Database()
        database.spanner_api = build_spanner_api()
        session = _Session(database)
        derived = _build_snapshot_derived(session)

        resumable = self._call_fut(derived, restart, request, session=session)
        for received_item in resumable:
            break
        resumable.close()

        raw.cancel.assert_called_once()

    def test_restart_on_unavailable_item_without_last_attribute(self):
        item = mock.Mock(
            value=0,
            resume_token=b"",
            metadata=None,
            precommit_token=None,
            _pb=None,
            spec=["value", "resume_token", "metadata", "precommit_token"],
        )
        raw = _MockIterator(item)
        restart = mock.Mock(return_value=raw)
        request = mock.Mock(test="test", spec=["test", "resume_token"])
        database = _Database()
        database.spanner_api = build_spanner_api()
        session = _Session(database)
        derived = _build_snapshot_derived(session)

        resumable = self._call_fut(derived, restart, request, session=session)
        items = list(resumable)
        self.assertEqual(items, [item])

    def test_restart_on_unavailable_finally_handles_cancel_exception(self):
        item = self._make_item(0, last=False)
        raw = _MockIterator(item)
        raw.cancel = mock.Mock(side_effect=RuntimeError("cancel failed"))
        restart = mock.Mock(return_value=raw)
        request = mock.Mock(test="test", spec=["test", "resume_token"])
        database = _Database()
        database.spanner_api = build_spanner_api()
        session = _Session(database)
        derived = _build_snapshot_derived(session)

        resumable = self._call_fut(derived, restart, request, session=session)
        for _ in resumable:
            break
        resumable.close()
        raw.cancel.assert_called_once()

    def test_restart_on_unavailable_last_does_not_cancel_iterator_in_finally(self):
        item_last = self._make_item(0, last=True)
        raw = _MockIterator(item_last)
        raw.cancel = mock.Mock()
        restart = mock.Mock(return_value=raw)
        request = mock.Mock(test="test", spec=["test", "resume_token"])
        database = _Database()
        database.spanner_api = build_spanner_api()
        session = _Session(database)
        derived = _build_snapshot_derived(session)

        with mock.patch("google.cloud.spanner_v1.snapshot._drain_stream"):
            resumable = self._call_fut(derived, restart, request, session=session)
            list(resumable)

        raw.cancel.assert_not_called()

    def test_streamed_result_set_with_last(self):
        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1.streamed import StreamedResultSet
        from google.cloud.spanner_v1.types.result_set import (
            PartialResultSet,
            ResultSetMetadata,
        )
        from google.cloud.spanner_v1.types.type import StructType, Type, TypeCode

        fields = [StructType.Field(name="greeting", type_=Type(code=TypeCode.STRING))]
        metadata_pb = ResultSetMetadata(row_type=StructType(fields=fields))
        item = PartialResultSet(metadata=metadata_pb, last=True)
        item.values.append(Value(string_value="hello"))

        raw = _MockIterator(item)
        streamed_result_set = StreamedResultSet(raw)
        rows = list(streamed_result_set)

        self.assertEqual(rows, [["hello"]])
        self.assertTrue(streamed_result_set._done)

    def test_restart_on_unavailable_multi_chunk_with_last(self):
        from google.protobuf.struct_pb2 import Value

        from google.cloud.spanner_v1.streamed import StreamedResultSet
        from google.cloud.spanner_v1.types.result_set import (
            PartialResultSet,
            ResultSetMetadata,
            ResultSetStats,
        )
        from google.cloud.spanner_v1.types.type import StructType, Type, TypeCode

        fields = [StructType.Field(name="greeting", type_=Type(code=TypeCode.STRING))]
        metadata_pb = ResultSetMetadata(row_type=StructType(fields=fields))
        stats_pb = ResultSetStats(row_count_exact=2)

        chunk_one = PartialResultSet(
            metadata=metadata_pb, last=False, resume_token=b"token_1"
        )
        chunk_one.values.append(Value(string_value="hello"))

        chunk_two = PartialResultSet(last=True, stats=stats_pb)
        chunk_two.values.append(Value(string_value="world"))

        raw = _MockIterator(chunk_one, chunk_two)
        restart = mock.Mock(return_value=raw)
        request = mock.Mock(test="test", spec=["test", "resume_token"])
        database = _Database()
        database.spanner_api = build_spanner_api()
        session = _Session(database)
        derived = _build_snapshot_derived(session)

        with mock.patch("google.cloud.spanner_v1.snapshot._drain_stream") as mock_drain:
            resumable = self._call_fut(derived, restart, request, session=session)
            streamed_result_set = StreamedResultSet(resumable)
            rows = list(streamed_result_set)

            mock_drain.assert_called_once_with(raw)
            self.assertEqual(rows, [["hello"], ["world"]])
            self.assertEqual(streamed_result_set.metadata, metadata_pb)
            self.assertEqual(streamed_result_set.stats, stats_pb)
            self.assertTrue(streamed_result_set._done)

    def test_restart_on_unavailable_zero_rows_with_last(self):
        from google.cloud.spanner_v1.streamed import StreamedResultSet
        from google.cloud.spanner_v1.types.result_set import (
            PartialResultSet,
            ResultSetMetadata,
            ResultSetStats,
        )
        from google.cloud.spanner_v1.types.type import StructType, Type, TypeCode

        fields = [StructType.Field(name="greeting", type_=Type(code=TypeCode.STRING))]
        metadata_pb = ResultSetMetadata(row_type=StructType(fields=fields))
        stats_pb = ResultSetStats(row_count_exact=0)

        chunk = PartialResultSet(metadata=metadata_pb, last=True, stats=stats_pb)

        raw = _MockIterator(chunk)
        restart = mock.Mock(return_value=raw)
        request = mock.Mock(test="test", spec=["test", "resume_token"])
        database = _Database()
        database.spanner_api = build_spanner_api()
        session = _Session(database)
        derived = _build_snapshot_derived(session)

        with mock.patch("google.cloud.spanner_v1.snapshot._drain_stream") as mock_drain:
            resumable = self._call_fut(derived, restart, request, session=session)
            streamed_result_set = StreamedResultSet(resumable)
            rows = list(streamed_result_set)

            mock_drain.assert_called_once_with(raw)
            self.assertEqual(rows, [])
            self.assertEqual(streamed_result_set.metadata, metadata_pb)
            self.assertEqual(streamed_result_set.stats, stats_pb)
            self.assertTrue(streamed_result_set._done)

    def test_restart_on_unavailable_retry_before_last(self):
        from google.api_core.exceptions import ServiceUnavailable

        chunk_one = self._make_item(0, resume_token=RESUME_TOKEN, last=False)
        chunk_two = self._make_item(1, last=True)

        stream_one = _MockIterator(
            chunk_one, fail_after=True, error=ServiceUnavailable("transient")
        )
        stream_two = _MockIterator(chunk_two)
        stream_two.cancel = mock.Mock()

        restart = mock.Mock(side_effect=[stream_one, stream_two])
        request = mock.Mock(test="test", spec=["test", "resume_token"])
        database = _Database()
        database.spanner_api = build_spanner_api()
        session = _Session(database)
        derived = _build_snapshot_derived(session)

        with mock.patch("google.cloud.spanner_v1.snapshot._drain_stream") as mock_drain:
            resumable = self._call_fut(derived, restart, request, session=session)
            items = list(resumable)

            self.assertEqual(items, [chunk_one, chunk_two])
            self.assertEqual(len(restart.mock_calls), 2)
            self.assertEqual(request.resume_token, RESUME_TOKEN)
            mock_drain.assert_called_once_with(stream_two)
            stream_two.cancel.assert_not_called()

    def test_iteration_w_raw_w_resume_token(self):
        ITEMS = (
            self._make_item(0),
            self._make_item(1, resume_token=RESUME_TOKEN),
            self._make_item(2),
            self._make_item(3),
        )
        raw = _MockIterator(*ITEMS)
        request = mock.Mock(test="test", spec=["test", "resume_token"])
        restart = mock.Mock(spec=[], return_value=raw)
        database = _Database()
        database.spanner_api = build_spanner_api()
        session = _Session(database)
        derived = _build_snapshot_derived(session)
        resumable = self._call_fut(derived, restart, request, session=session)
        self.assertEqual(list(resumable), list(ITEMS))
        restart.assert_called_once_with(
            request=request,
            metadata=[
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                )
            ],
        )
        self.assertNoSpans()

    def test_iteration_w_raw_raising_unavailable_no_token(self):
        from google.api_core.exceptions import ServiceUnavailable

        ITEMS = (
            self._make_item(0),
            self._make_item(1, resume_token=RESUME_TOKEN),
            self._make_item(2),
        )
        before = _MockIterator(fail_after=True, error=ServiceUnavailable("testing"))
        after = _MockIterator(*ITEMS)
        request = mock.Mock(test="test", spec=["test", "resume_token"])
        restart = mock.Mock(spec=[], side_effect=[before, after])
        database = _Database()
        database.spanner_api = build_spanner_api()
        session = _Session(database)
        derived = _build_snapshot_derived(session)
        resumable = self._call_fut(derived, restart, request, session=session)
        self.assertEqual(list(resumable), list(ITEMS))
        self.assertEqual(len(restart.mock_calls), 2)
        self.assertEqual(request.resume_token, b"")
        self.assertNoSpans()

    def test_iteration_w_raw_raising_retryable_internal_error_no_token(self):
        ITEMS = (
            self._make_item(0),
            self._make_item(1, resume_token=RESUME_TOKEN),
            self._make_item(2),
        )
        before = _MockIterator(
            fail_after=True,
            error=INTERNAL_SERVER_ERROR_UNEXPECTED_EOS,
        )
        after = _MockIterator(*ITEMS)
        request = mock.Mock(test="test", spec=["test", "resume_token"])
        restart = mock.Mock(spec=[], side_effect=[before, after])
        database = _Database()
        database.spanner_api = build_spanner_api()
        session = _Session(database)
        derived = _build_snapshot_derived(session)
        resumable = self._call_fut(derived, restart, request, session=session)
        self.assertEqual(list(resumable), list(ITEMS))
        self.assertEqual(len(restart.mock_calls), 2)
        self.assertEqual(request.resume_token, b"")
        self.assertNoSpans()

    def test_iteration_w_raw_raising_non_retryable_internal_error_no_token(self):
        from google.api_core.exceptions import InternalServerError

        ITEMS = (
            self._make_item(0),
            self._make_item(1, resume_token=RESUME_TOKEN),
            self._make_item(2),
        )
        before = _MockIterator(fail_after=True, error=InternalServerError("testing"))
        after = _MockIterator(*ITEMS)
        request = mock.Mock(spec=["resume_token"])
        restart = mock.Mock(spec=[], side_effect=[before, after])
        database = _Database()
        database.spanner_api = build_spanner_api()
        session = _Session(database)
        derived = _build_snapshot_derived(session)
        resumable = self._call_fut(derived, restart, request, session=session)
        # Exception has request_id attribute added
        with self.assertRaises(InternalServerError) as context:
            list(resumable)
        self.assertTrue(hasattr(context.exception, "request_id"))
        restart.assert_called_once_with(
            request=request,
            metadata=[
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                )
            ],
        )
        self.assertNoSpans()

    def test_iteration_w_raw_raising_unavailable(self):
        from google.api_core.exceptions import ServiceUnavailable

        FIRST = (self._make_item(0), self._make_item(1, resume_token=RESUME_TOKEN))
        SECOND = (self._make_item(2),)  # discarded after 503
        LAST = (self._make_item(3),)
        before = _MockIterator(
            *(FIRST + SECOND), fail_after=True, error=ServiceUnavailable("testing")
        )
        after = _MockIterator(*LAST)
        request = mock.Mock(test="test", spec=["test", "resume_token"])
        restart = mock.Mock(spec=[], side_effect=[before, after])
        database = _Database()
        database.spanner_api = build_spanner_api()
        session = _Session(database)
        derived = _build_snapshot_derived(session)
        resumable = self._call_fut(derived, restart, request, session=session)
        self.assertEqual(list(resumable), list(FIRST + LAST))
        self.assertEqual(len(restart.mock_calls), 2)
        self.assertEqual(request.resume_token, RESUME_TOKEN)
        self.assertNoSpans()

    def test_iteration_w_raw_raising_retryable_internal_error(self):
        FIRST = (self._make_item(0), self._make_item(1, resume_token=RESUME_TOKEN))
        SECOND = (self._make_item(2),)  # discarded after 503
        LAST = (self._make_item(3),)
        before = _MockIterator(
            *(FIRST + SECOND),
            fail_after=True,
            error=INTERNAL_SERVER_ERROR_UNEXPECTED_EOS,
        )
        after = _MockIterator(*LAST)
        request = mock.Mock(test="test", spec=["test", "resume_token"])
        restart = mock.Mock(spec=[], side_effect=[before, after])
        database = _Database()
        database.spanner_api = build_spanner_api()
        session = _Session(database)
        derived = _build_snapshot_derived(session)
        resumable = self._call_fut(derived, restart, request, session=session)
        self.assertEqual(list(resumable), list(FIRST + LAST))
        self.assertEqual(len(restart.mock_calls), 2)
        self.assertEqual(request.resume_token, RESUME_TOKEN)
        self.assertNoSpans()

    def test_iteration_w_raw_raising_non_retryable_internal_error(self):
        from google.api_core.exceptions import InternalServerError

        FIRST = (self._make_item(0), self._make_item(1, resume_token=RESUME_TOKEN))
        SECOND = (self._make_item(2),)  # discarded after 503
        LAST = (self._make_item(3),)
        before = _MockIterator(
            *(FIRST + SECOND), fail_after=True, error=InternalServerError("testing")
        )
        after = _MockIterator(*LAST)
        request = mock.Mock(test="test", spec=["test", "resume_token"])
        restart = mock.Mock(spec=[], side_effect=[before, after])
        database = _Database()
        database.spanner_api = build_spanner_api()
        session = _Session(database)
        derived = _build_snapshot_derived(session)
        resumable = self._call_fut(derived, restart, request, session=session)
        # Exception has request_id attribute added
        with self.assertRaises(InternalServerError) as context:
            list(resumable)
        self.assertTrue(hasattr(context.exception, "request_id"))
        restart.assert_called_once_with(
            request=request,
            metadata=[
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                )
            ],
        )
        self.assertNoSpans()

    def test_iteration_w_raw_raising_unavailable_after_token(self):
        from google.api_core.exceptions import ServiceUnavailable

        FIRST = (self._make_item(0), self._make_item(1, resume_token=RESUME_TOKEN))
        SECOND = (self._make_item(2), self._make_item(3))
        before = _MockIterator(
            *FIRST, fail_after=True, error=ServiceUnavailable("testing")
        )
        after = _MockIterator(*SECOND)
        request = mock.Mock(test="test", spec=["test", "resume_token"])
        restart = mock.Mock(spec=[], side_effect=[before, after])
        database = _Database()
        database.spanner_api = build_spanner_api()
        session = _Session(database)
        derived = _build_snapshot_derived(session)
        resumable = self._call_fut(derived, restart, request, session=session)
        self.assertEqual(list(resumable), list(FIRST + SECOND))
        self.assertEqual(len(restart.mock_calls), 2)
        self.assertEqual(request.resume_token, RESUME_TOKEN)
        self.assertNoSpans()

    def test_iteration_w_raw_raising_unavailable_during_restart(self):
        from google.api_core.exceptions import ServiceUnavailable

        FIRST = (self._make_item(0), self._make_item(1, resume_token=RESUME_TOKEN))
        LAST = (self._make_item(2),)
        before = _MockIterator(
            *FIRST, fail_after=True, error=ServiceUnavailable("testing")
        )
        after = _MockIterator(*LAST)
        request = mock.Mock(test="test", spec=["test", "resume_token"])
        # The second call (the first retry) raises ServiceUnavailable immediately.
        # The third call (the second retry) succeeds.
        restart = mock.Mock(
            spec=[],
            side_effect=[before, ServiceUnavailable("retry failed"), after],
        )
        database = _Database()
        database.spanner_api = build_spanner_api()
        session = _Session(database)
        derived = _build_snapshot_derived(session)
        resumable = self._call_fut(derived, restart, request, session=session)
        self.assertEqual(list(resumable), list(FIRST + LAST))
        self.assertEqual(len(restart.mock_calls), 3)
        self.assertEqual(request.resume_token, RESUME_TOKEN)
        self.assertNoSpans()

    def test_iteration_w_raw_raising_resumable_internal_error_during_restart(self):
        FIRST = (self._make_item(0), self._make_item(1, resume_token=RESUME_TOKEN))
        LAST = (self._make_item(2),)
        before = _MockIterator(
            *FIRST,
            fail_after=True,
            error=INTERNAL_SERVER_ERROR_UNEXPECTED_EOS,
        )
        after = _MockIterator(*LAST)
        request = mock.Mock(test="test", spec=["test", "resume_token"])
        restart = mock.Mock(
            spec=[],
            side_effect=[before, INTERNAL_SERVER_ERROR_UNEXPECTED_EOS, after],
        )
        database = _Database()
        database.spanner_api = build_spanner_api()
        session = _Session(database)
        derived = _build_snapshot_derived(session)
        resumable = self._call_fut(derived, restart, request, session=session)
        self.assertEqual(list(resumable), list(FIRST + LAST))
        self.assertEqual(len(restart.mock_calls), 3)
        self.assertEqual(request.resume_token, RESUME_TOKEN)
        self.assertNoSpans()

    def test_iteration_w_raw_w_multiuse(self):
        from google.cloud.spanner_v1 import ReadRequest

        FIRST = (
            self._make_item(0),
            self._make_item(1),
        )
        before = _MockIterator(*FIRST)
        request = ReadRequest(transaction=None)
        restart = mock.Mock(spec=[], return_value=before)
        database = _Database()
        database.spanner_api = build_spanner_api()
        session = _Session(database)
        derived = _build_snapshot_derived(session, multi_use=True)
        resumable = self._call_fut(derived, restart, request, session=session)
        self.assertEqual(list(resumable), list(FIRST))
        self.assertEqual(len(restart.mock_calls), 1)
        begin_count = sum(
            [1 for args in restart.call_args_list if "begin" in args.kwargs.__str__()]
        )
        self.assertEqual(begin_count, 1)
        self.assertNoSpans()

    def test_iteration_w_raw_raising_unavailable_w_multiuse(self):
        from google.api_core.exceptions import ServiceUnavailable

        from google.cloud.spanner_v1 import ReadRequest

        FIRST = (
            self._make_item(0),
            self._make_item(1),
        )
        SECOND = (self._make_item(2), self._make_item(3))
        before = _MockIterator(
            *FIRST, fail_after=True, error=ServiceUnavailable("testing")
        )
        after = _MockIterator(*SECOND)
        request = ReadRequest(transaction=None)
        restart = mock.Mock(spec=[], side_effect=[before, after])
        database = _Database()
        database.spanner_api = build_spanner_api()
        session = _Session(database)
        derived = _build_snapshot_derived(session, multi_use=True)
        resumable = self._call_fut(derived, restart, request, session=session)
        self.assertEqual(list(resumable), list(SECOND))
        self.assertEqual(len(restart.mock_calls), 2)
        begin_count = sum(
            [1 for args in restart.call_args_list if "begin" in args.kwargs.__str__()]
        )

        # Since the transaction id was not set before the Unavailable error, the statement will be retried with inline begin.
        self.assertEqual(begin_count, 2)
        self.assertNoSpans()

    def test_iteration_w_raw_raising_unavailable_after_token_w_multiuse(self):
        from google.api_core.exceptions import ServiceUnavailable

        from google.cloud.spanner_v1 import ReadRequest, ResultSetMetadata
        from google.cloud.spanner_v1 import Transaction as TransactionPB

        transaction_pb = TransactionPB(id=TXN_ID)
        metadata_pb = ResultSetMetadata(transaction=transaction_pb)
        FIRST = (
            self._make_item(0),
            self._make_item(1, resume_token=RESUME_TOKEN, metadata=metadata_pb),
        )
        SECOND = (self._make_item(2), self._make_item(3))
        before = _MockIterator(
            *FIRST, fail_after=True, error=ServiceUnavailable("testing")
        )
        after = _MockIterator(*SECOND)
        request = ReadRequest(transaction=None)
        restart = mock.Mock(spec=[], side_effect=[before, after])
        database = _Database()
        database.spanner_api = build_spanner_api()
        session = _Session(database)
        derived = _build_snapshot_derived(session, multi_use=True)

        resumable = self._call_fut(derived, restart, request, session=session)

        self.assertEqual(list(resumable), list(FIRST + SECOND))
        self.assertEqual(len(restart.mock_calls), 2)
        self.assertEqual(request.resume_token, RESUME_TOKEN)
        transaction_id_selector_count = sum(
            [
                1
                for args in restart.call_args_list
                if 'id: "DEAFBEAD"' in args.kwargs.__str__()
            ]
        )

        # Statement will be retried with Transaction id.
        self.assertEqual(transaction_id_selector_count, 2)
        self.assertNoSpans()

    def test_iteration_w_raw_raising_retryable_internal_error_after_token(self):
        FIRST = (self._make_item(0), self._make_item(1, resume_token=RESUME_TOKEN))
        SECOND = (self._make_item(2), self._make_item(3))
        before = _MockIterator(
            *FIRST,
            fail_after=True,
            error=INTERNAL_SERVER_ERROR_UNEXPECTED_EOS,
        )
        after = _MockIterator(*SECOND)
        request = mock.Mock(test="test", spec=["test", "resume_token"])
        restart = mock.Mock(spec=[], side_effect=[before, after])
        database = _Database()
        database.spanner_api = build_spanner_api()
        session = _Session(database)
        derived = _build_snapshot_derived(session)
        resumable = self._call_fut(derived, restart, request, session=session)
        self.assertEqual(list(resumable), list(FIRST + SECOND))
        self.assertEqual(len(restart.mock_calls), 2)
        self.assertEqual(request.resume_token, RESUME_TOKEN)
        self.assertNoSpans()

    def test_iteration_w_raw_raising_non_retryable_internal_error_after_token(self):
        from google.api_core.exceptions import InternalServerError

        FIRST = (self._make_item(0), self._make_item(1, resume_token=RESUME_TOKEN))
        SECOND = (self._make_item(2), self._make_item(3))
        before = _MockIterator(
            *FIRST, fail_after=True, error=InternalServerError("testing")
        )
        after = _MockIterator(*SECOND)
        request = mock.Mock(test="test", spec=["test", "resume_token"])
        restart = mock.Mock(spec=[], side_effect=[before, after])
        database = _Database()
        database.spanner_api = build_spanner_api()
        session = _Session(database)
        derived = _build_snapshot_derived(session)
        resumable = self._call_fut(derived, restart, request, session=session)
        # Exception has request_id attribute added
        with self.assertRaises(InternalServerError) as context:
            list(resumable)
        self.assertTrue(hasattr(context.exception, "request_id"))
        restart.assert_called_once_with(
            request=request,
            metadata=[
                (
                    "x-goog-spanner-request-id",
                    f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1",
                )
            ],
        )
        self.assertNoSpans()

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_iteration_w_span_creation(self, mock_region):
        name = "TestSpan"
        extra_atts = {"test_att": 1}
        raw = _MockIterator()
        request = mock.Mock(test="test", spec=["test", "resume_token"])
        restart = mock.Mock(spec=[], return_value=raw)
        database = _Database()
        database.spanner_api = build_spanner_api()
        session = _Session(database)
        derived = _build_snapshot_derived(session)
        resumable = self._call_fut(
            derived, restart, request, name, _Session(_Database()), extra_atts
        )
        self.assertEqual(list(resumable), [])
        req_id = f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1"
        self.assertSpanAttributes(
            name,
            attributes=dict(
                BASE_ATTRIBUTES, test_att=1, x_goog_spanner_request_id=req_id
            ),
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_iteration_w_multiple_span_creation(self, mock_region):
        from google.api_core.exceptions import ServiceUnavailable

        if HAS_OPENTELEMETRY_INSTALLED:
            FIRST = (self._make_item(0), self._make_item(1, resume_token=RESUME_TOKEN))
            SECOND = (self._make_item(2),)  # discarded after 503
            LAST = (self._make_item(3),)
            before = _MockIterator(
                *(FIRST + SECOND), fail_after=True, error=ServiceUnavailable("testing")
            )
            after = _MockIterator(*LAST)
            request = mock.Mock(test="test", spec=["test", "resume_token"])
            restart = mock.Mock(spec=[], side_effect=[before, after])
            name = "TestSpan"
            database = _Database()
            database.spanner_api = build_spanner_api()
            session = _Session(database)
            derived = _build_snapshot_derived(session)
            resumable = self._call_fut(
                derived, restart, request, name, _Session(_Database())
            )
            self.assertEqual(list(resumable), list(FIRST + LAST))
            self.assertEqual(len(restart.mock_calls), 2)
            self.assertEqual(request.resume_token, RESUME_TOKEN)

            span_list = self.ot_exporter.get_finished_spans()
            self.assertEqual(len(span_list), 2)
            for i, span in enumerate(span_list):
                self.assertEqual(span.name, name)
                req_id = f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.{i + 1}"
                self.assertEqual(
                    dict(span.attributes),
                    dict(
                        enrich_with_otel_scope(BASE_ATTRIBUTES),
                        x_goog_spanner_request_id=req_id,
                    ),
                )

    def test_restart_on_unavailable_metrics_tracer_lifecycle(self):
        from google.cloud.spanner_v1.metrics.metrics_tracer_factory import (
            MetricsTracerFactory,
        )
        from google.cloud.spanner_v1.metrics.spanner_metrics_tracer_factory import (
            SpannerMetricsTracerFactory,
        )
        from google.cloud.spanner_v1.snapshot import _restart_on_unavailable

        mock_tracer = mock.Mock()

        item = self._make_item(0)
        raw = _MockIterator(item)
        tracer_during_call = []

        def restart(*args, **kwargs):
            tracer_during_call.append(SpannerMetricsTracerFactory.get_current_tracer())
            return raw

        request = mock.Mock(test="test", spec=["test", "resume_token"])
        database = _Database()
        database.spanner_api = build_spanner_api()
        session = _Session(database)
        derived = _build_snapshot_derived(session)
        resource_info = {"project": "p", "instance": "i", "database": "d"}

        with mock.patch.object(
            MetricsTracerFactory, "create_metrics_tracer", return_value=mock_tracer
        ) as mock_create_tracer:
            resumable = _restart_on_unavailable(
                restart,
                request,
                session=session,
                transaction=derived,
                request_id_manager=session._database,
                resource_info=resource_info,
            )

            # Not started before iteration begins (lazy generator)
            mock_tracer.record_operation_start.assert_not_called()

            items = []
            for it in resumable:
                # During row iteration, ambient contextvar must NOT be contaminated
                self.assertIsNone(SpannerMetricsTracerFactory.get_current_tracer())
                items.append(it)

            self.assertEqual(items, [item])
            # Tracer factory was called with resource info
            mock_create_tracer.assert_called_once_with(resource_info)
            # Operation was started once
            mock_tracer.record_operation_start.assert_called_once()
            # Contextvar was active during RPC invocation
            self.assertEqual(tracer_during_call, [mock_tracer])
            # Operation completion recorded once
            mock_tracer.record_operation_completion.assert_called_once()
            # Context is clean after completion
            self.assertIsNone(SpannerMetricsTracerFactory.get_current_tracer())

    def test_restart_on_unavailable_metrics_tracer_spans_retries(self):
        from google.api_core.exceptions import ServiceUnavailable

        from google.cloud.spanner_v1.metrics.metrics_tracer_factory import (
            MetricsTracerFactory,
        )
        from google.cloud.spanner_v1.metrics.spanner_metrics_tracer_factory import (
            SpannerMetricsTracerFactory,
        )
        from google.cloud.spanner_v1.snapshot import _restart_on_unavailable

        mock_tracer = mock.Mock()

        FIRST = (self._make_item(0), self._make_item(1, resume_token=RESUME_TOKEN))
        SECOND = (self._make_item(2),)
        before = _MockIterator(
            *FIRST, fail_after=True, error=ServiceUnavailable("testing")
        )
        after = _MockIterator(*SECOND)
        tracers_during_calls = []

        def restart(*args, **kwargs):
            tracers_during_calls.append(
                SpannerMetricsTracerFactory.get_current_tracer()
            )
            if len(tracers_during_calls) == 1:
                return before
            return after

        request = mock.Mock(test="test", spec=["test", "resume_token"])
        database = _Database()
        database.spanner_api = build_spanner_api()
        session = _Session(database)
        derived = _build_snapshot_derived(session)
        resource_info = {"project": "p", "instance": "i", "database": "d"}

        with mock.patch.object(
            MetricsTracerFactory, "create_metrics_tracer", return_value=mock_tracer
        ):
            resumable = _restart_on_unavailable(
                restart,
                request,
                session=session,
                transaction=derived,
                request_id_manager=session._database,
                resource_info=resource_info,
            )

            items = list(resumable)
            self.assertEqual(items, list(FIRST + SECOND))
            self.assertEqual(len(tracers_during_calls), 2)
            # Both attempts used the same metrics tracer
            self.assertEqual(tracers_during_calls, [mock_tracer, mock_tracer])
            mock_tracer.record_operation_start.assert_called_once()
            mock_tracer.record_operation_completion.assert_called_once()
            self.assertIsNone(SpannerMetricsTracerFactory.get_current_tracer())

    def test_restart_on_unavailable_early_break_no_context_error(self):
        from google.cloud.spanner_v1.metrics.metrics_tracer_factory import (
            MetricsTracerFactory,
        )
        from google.cloud.spanner_v1.metrics.spanner_metrics_tracer_factory import (
            SpannerMetricsTracerFactory,
        )
        from google.cloud.spanner_v1.snapshot import _restart_on_unavailable

        mock_tracer = mock.Mock()

        FIRST = (self._make_item(0), self._make_item(1))
        raw = _MockIterator(*FIRST)
        restart = mock.Mock(return_value=raw)
        request = mock.Mock(test="test", spec=["test", "resume_token"])
        database = _Database()
        database.spanner_api = build_spanner_api()
        session = _Session(database)
        derived = _build_snapshot_derived(session)
        resource_info = {"project": "p", "instance": "i", "database": "d"}

        with mock.patch.object(
            MetricsTracerFactory, "create_metrics_tracer", return_value=mock_tracer
        ):
            resumable = _restart_on_unavailable(
                restart,
                request,
                session=session,
                transaction=derived,
                request_id_manager=session._database,
                resource_info=resource_info,
            )

            for it in resumable:
                self.assertEqual(it, FIRST[0])
                break
            resumable.close()

            mock_tracer.record_operation_completion.assert_called_once()
            self.assertIsNone(SpannerMetricsTracerFactory.get_current_tracer())

    def test_restart_on_unavailable_real_factory_early_break_no_context_error(self):
        from google.cloud.spanner_v1.metrics.spanner_metrics_tracer_factory import (
            SpannerMetricsTracerFactory,
        )
        from google.cloud.spanner_v1.snapshot import _restart_on_unavailable

        FIRST = (self._make_item(0), self._make_item(1))
        raw = _MockIterator(*FIRST)
        restart = mock.Mock(return_value=raw)
        request = mock.Mock(test="test", spec=["test", "resume_token"])
        database = _Database()
        database.spanner_api = build_spanner_api()
        session = _Session(database)
        derived = _build_snapshot_derived(session)
        resource_info = {"project": "p", "instance": "i", "database": "d"}

        resumable = _restart_on_unavailable(
            restart,
            request,
            session=session,
            transaction=derived,
            request_id_manager=session._database,
            resource_info=resource_info,
        )

        for it in resumable:
            self.assertEqual(it, FIRST[0])
            break
        resumable.close()

        self.assertIsNone(SpannerMetricsTracerFactory.get_current_tracer())

    def test_restart_on_unavailable_metrics_tracer_partial_resource_info_and_disabled(
        self,
    ):
        from google.cloud.spanner_v1.metrics.metrics_tracer_factory import (
            MetricsTracerFactory,
        )
        from google.cloud.spanner_v1.metrics.spanner_metrics_tracer_factory import (
            SpannerMetricsTracerFactory,
        )
        from google.cloud.spanner_v1.snapshot import _restart_on_unavailable

        mock_tracer = mock.Mock()
        item = self._make_item(0)
        request = mock.Mock(test="test", spec=["test", "resume_token"])
        database = _Database()
        database.spanner_api = build_spanner_api()
        session = _Session(database)
        derived = _build_snapshot_derived(session)

        # 1. resource_info is None
        with mock.patch.object(
            MetricsTracerFactory, "create_metrics_tracer", return_value=mock_tracer
        ):
            resumable = _restart_on_unavailable(
                mock.Mock(return_value=_MockIterator(item)),
                request,
                session=session,
                transaction=derived,
                request_id_manager=session._database,
                resource_info=None,
            )
            for it in resumable:
                pass
            mock_tracer.record_operation_start.assert_called_once()
            mock_tracer.record_operation_completion.assert_called_once()

        # 2. partial resource_info (only project, only instance, only database)
        for partial_info in [{"project": "p"}, {"instance": "i"}, {"database": "d"}]:
            mock_tracer.reset_mock()
            with mock.patch.object(
                MetricsTracerFactory, "create_metrics_tracer", return_value=mock_tracer
            ) as mock_create_tracer:
                resumable = _restart_on_unavailable(
                    mock.Mock(return_value=_MockIterator(item)),
                    request,
                    session=session,
                    transaction=derived,
                    request_id_manager=session._database,
                    resource_info=partial_info,
                )
                for it in resumable:
                    pass
                mock_create_tracer.assert_called_once_with(partial_info)

        # 3. metrics factory disabled
        SpannerMetricsTracerFactory(enabled=False)
        try:
            with mock.patch.object(
                MetricsTracerFactory, "create_metrics_tracer"
            ) as mock_create:
                resumable = _restart_on_unavailable(
                    mock.Mock(return_value=_MockIterator(item)),
                    request,
                    session=session,
                    transaction=derived,
                    request_id_manager=session._database,
                    resource_info={"project": "p"},
                )
                items = []
                for it in resumable:
                    items.append(it)
                self.assertEqual(items, [item])
                mock_create.assert_not_called()
                self.assertIsNone(SpannerMetricsTracerFactory.get_current_tracer())
        finally:
            SpannerMetricsTracerFactory(enabled=True)

        # 4. create_metrics_tracer returns None
        with mock.patch.object(
            MetricsTracerFactory, "create_metrics_tracer", return_value=None
        ):
            resumable = _restart_on_unavailable(
                mock.Mock(return_value=_MockIterator(item)),
                request,
                session=session,
                transaction=derived,
                request_id_manager=session._database,
                resource_info={"project": "p"},
            )
            items = []
            for it in resumable:
                items.append(it)
            self.assertEqual(items, [item])
            self.assertIsNone(SpannerMetricsTracerFactory.get_current_tracer())

    def test_restart_on_unavailable_metrics_completion_error_handled(self):
        from google.cloud.spanner_v1.metrics.metrics_tracer_factory import (
            MetricsTracerFactory,
        )
        from google.cloud.spanner_v1.snapshot import _restart_on_unavailable

        mock_tracer = mock.Mock()
        mock_tracer.record_operation_completion.side_effect = RuntimeError(
            "metrics export failure"
        )

        item = mock.Mock(
            value=0,
            resume_token=b"",
            metadata=None,
            precommit_token=None,
            last=False,
            _pb=None,
            spec=["value", "resume_token", "metadata", "precommit_token", "last"],
        )
        mock_iterator = _MockIterator(item)
        mock_iterator.cancel = mock.Mock()
        request = mock.Mock(test="test", spec=["test", "resume_token"])
        database = _Database()
        database.spanner_api = build_spanner_api()
        session = _Session(database)
        derived = _build_snapshot_derived(session)

        with mock.patch.object(
            MetricsTracerFactory, "create_metrics_tracer", return_value=mock_tracer
        ):
            resumable = _restart_on_unavailable(
                mock.Mock(return_value=mock_iterator),
                request,
                session=session,
                transaction=derived,
                request_id_manager=session._database,
                resource_info={"project": "p"},
            )
            items = []
            for it in resumable:
                items.append(it)
                break
            resumable.close()

            self.assertEqual(items, [item])
            mock_tracer.record_operation_completion.assert_called_once()
            mock_iterator.cancel.assert_called_once()

    def test_restart_on_unavailable_metrics_completion_error_preserves_query_error(
        self,
    ):
        from google.cloud.spanner_v1.metrics.metrics_tracer_factory import (
            MetricsTracerFactory,
        )
        from google.cloud.spanner_v1.snapshot import _restart_on_unavailable

        mock_tracer = mock.Mock()
        mock_tracer.record_operation_completion.side_effect = RuntimeError(
            "metrics export failure"
        )

        item = mock.Mock(
            value=0,
            resume_token=b"",
            metadata=None,
            precommit_token=None,
            last=False,
            _pb=None,
            spec=["value", "resume_token", "metadata", "precommit_token", "last"],
        )
        mock_iterator = _MockIterator(
            item, fail_after=True, error=NotFound("table not found")
        )
        mock_iterator.cancel = mock.Mock()
        request = mock.Mock(test="test", spec=["test", "resume_token"])
        database = _Database()
        database.spanner_api = build_spanner_api()
        session = _Session(database)
        derived = _build_snapshot_derived(session)

        with mock.patch.object(
            MetricsTracerFactory, "create_metrics_tracer", return_value=mock_tracer
        ):
            resumable = _restart_on_unavailable(
                mock.Mock(return_value=mock_iterator),
                request,
                session=session,
                transaction=derived,
                request_id_manager=session._database,
                resource_info={"project": "p"},
            )
            with self.assertRaises(NotFound):
                for _ in resumable:
                    pass

            mock_tracer.record_operation_completion.assert_called_once()
            mock_iterator.cancel.assert_called_once()


class Test_SnapshotBase(OpenTelemetryBase):
    def test_ctor(self):
        session = build_session()
        derived = _Derived(session=session)

        # Attributes from _SessionWrapper.
        self.assertIs(derived._session, session)

        # Attributes from _SnapshotBase.
        self.assertTrue(derived._read_only)
        self.assertFalse(derived._multi_use)
        self.assertEqual(derived._execute_sql_request_count, 0)
        self.assertEqual(derived._read_request_count, 0)
        self.assertFalse(derived._begin_request_sent)
        self.assertIsNone(derived._transaction_id)
        self.assertIsNone(derived._precommit_token)
        self.assertIsNone(derived._lock)
        self.assertIsNone(derived._transaction_begin_event)

        self.assertNoSpans()

    def test_derived_constructor_multi_use(self):
        session = build_session()
        derived = _Derived(session=session, multi_use=True)

        self.assertTrue(derived._read_only)
        self.assertTrue(derived._multi_use)
        self.assertIsInstance(derived._lock, type(Lock()))
        self.assertFalse(derived._transaction_begin_event.is_set())

    def test_resource_info_fallback_when_database_lacks_resource_info(self):
        database = mock.Mock(spec=["_instance", "database_id"])
        database.database_id = "test-db"
        instance = mock.Mock(spec=["_client", "instance_id"])
        instance.instance_id = "test-inst"
        client = mock.Mock(spec=["project"])
        client.project = "test-proj"
        instance._client = client
        database._instance = instance

        session = mock.Mock()
        session._database = database
        derived = _build_snapshot_derived(session=session)
        self.assertEqual(
            derived._resource_info,
            {"project": "test-proj", "instance": "test-inst", "database": "test-db"},
        )

        derived._session = None
        self.assertIsNone(derived._resource_info)

    def test__wait_for_transaction_begin_claims_inline_begin(self):
        derived = _build_snapshot_derived(multi_use=True)

        derived._wait_for_transaction_begin()

        # The first request is the one that begins the transaction inline.
        self.assertTrue(derived._begin_request_sent)

    def test__wait_for_transaction_begin_wo_multi_use(self):
        derived = _build_snapshot_derived(multi_use=False)
        derived._read_request_count = 1

        with self.assertRaisesRegex(ValueError, "Cannot re-use single-use snapshot."):
            derived._wait_for_transaction_begin()

    def test__wait_for_transaction_begin_twice_wo_multi_use(self):
        derived = _build_snapshot_derived(multi_use=False)
        derived._wait_for_transaction_begin()
        self.assertTrue(derived._begin_request_sent)

        with self.assertRaisesRegex(ValueError, "Cannot re-use single-use snapshot."):
            derived._wait_for_transaction_begin()

    def test__wait_for_transaction_begin_waits_for_concurrent_begin(self):
        """A concurrent request must wait for the in-flight inline begin.

        Regression test: without the begin event, the second request observes
        ``_transaction_id is None`` and wrongly raises "Transaction has not begun."
        """

        from google.cloud.spanner_v1 import Transaction as TransactionPB

        derived = _build_snapshot_derived(multi_use=True)

        # First request claims the inline begin, but has not completed yet, so
        # no transaction id is available.
        derived._wait_for_transaction_begin()

        errors = []
        released = Event()

        def concurrent_request():
            try:
                derived._wait_for_transaction_begin()
            except Exception as exc:  # pragma: no cover - only on regression
                errors.append(exc)
            finally:
                released.set()

        thread = Thread(target=concurrent_request, daemon=True)
        thread.start()

        # The concurrent request blocks while the transaction id is unknown.
        self.assertFalse(released.wait(timeout=0.1))

        # Completing the inline begin releases it.
        derived._update_for_transaction_pb(TransactionPB(id=TXN_ID))
        self.assertTrue(released.wait(timeout=10))

        thread.join(timeout=10)
        self.assertFalse(thread.is_alive())
        self.assertEqual(errors, [])

    def test__build_transaction_selector_pb_single_use(self):
        derived = _build_snapshot_derived(multi_use=False)

        actual_selector = derived._build_transaction_selector_pb()

        expected_selector = TransactionSelector(single_use=_Derived.TRANSACTION_OPTIONS)
        self.assertEqual(actual_selector, expected_selector)

    def test__build_transaction_selector_pb_multi_use(self):
        derived = _build_snapshot_derived(multi_use=True)

        # Select new transaction.
        expected_options = _Derived.TRANSACTION_OPTIONS
        expected_selector = TransactionSelector(begin=expected_options)
        self.assertEqual(expected_selector, derived._build_transaction_selector_pb())

        # Select existing transaction.
        transaction_id = b"transaction-id"
        begin_transaction = derived._session._database.spanner_api.begin_transaction
        begin_transaction.return_value = build_transaction_pb(id=transaction_id)

        derived.begin()

        expected_selector = TransactionSelector(id=transaction_id)
        self.assertEqual(expected_selector, derived._build_transaction_selector_pb())

    def test_begin_error_not_multi_use(self):
        derived = _build_snapshot_derived(multi_use=False)

        with self.assertRaises(ValueError):
            derived.begin()

        self.assertNoSpans()

    def test_begin_error_already_begun(self):
        derived = _build_snapshot_derived(multi_use=True)
        derived.begin()

        self.reset()
        with self.assertRaises(ValueError):
            derived.begin()

        self.assertNoSpans()

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_begin_error_other(self, mock_region):
        derived = _build_snapshot_derived(multi_use=True)

        database = derived._session._database
        begin_transaction = database.spanner_api.begin_transaction
        begin_transaction.side_effect = RuntimeError()

        with self.assertRaises(RuntimeError):
            derived.begin()

        if not HAS_OPENTELEMETRY_INSTALLED:
            return

        self.assertSpanAttributes(
            name="CloudSpanner._Derived.begin",
            status=StatusCode.ERROR,
            attributes=_build_span_attributes(database),
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_begin_read_write(self, mock_region):
        derived = _build_snapshot_derived(multi_use=True, read_only=False)

        begin_transaction = derived._session._database.spanner_api.begin_transaction
        begin_transaction.return_value = build_transaction_pb()

        self._execute_begin(derived)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_begin_read_only(self, mock_region):
        derived = _build_snapshot_derived(multi_use=True, read_only=True)

        begin_transaction = derived._session._database.spanner_api.begin_transaction
        begin_transaction.return_value = build_transaction_pb()

        self._execute_begin(derived)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_begin_precommit_token(self, mock_region):
        derived = _build_snapshot_derived(multi_use=True)

        begin_transaction = derived._session._database.spanner_api.begin_transaction
        begin_transaction.return_value = build_transaction_pb(
            precommit_token=PRECOMMIT_TOKEN_1
        )

        self._execute_begin(derived)

    @mock.patch("google.cloud.spanner_v1._helpers.time.sleep")
    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_begin_retry_for_internal_server_error(self, mock_region, mock_sleep):
        derived = _build_snapshot_derived(multi_use=True)

        begin_transaction = derived._session._database.spanner_api.begin_transaction
        begin_transaction.side_effect = [
            INTERNAL_SERVER_ERROR_UNEXPECTED_EOS,
            build_transaction_pb(),
        ]

        self._execute_begin(derived, attempts=2)
        mock_sleep.assert_called_once_with(2)

        expected_statuses = [
            (
                "Transaction Begin Attempt Failed. Retrying",
                {"attempt": 1, "sleep_seconds": 4},
            )
        ]
        actual_statuses = self.finished_spans_events_statuses()
        self.assertEqual(expected_statuses, actual_statuses)

    @mock.patch("google.cloud.spanner_v1._helpers.time.sleep")
    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_begin_retry_for_aborted(self, mock_region, mock_sleep):
        derived = _build_snapshot_derived(multi_use=True)

        begin_transaction = derived._session._database.spanner_api.begin_transaction
        begin_transaction.side_effect = [
            Aborted("test"),
            build_transaction_pb(),
        ]

        self._execute_begin(derived, attempts=2)
        mock_sleep.assert_called_once_with(2)

        expected_statuses = [
            (
                "Transaction Begin Attempt Failed. Retrying",
                {"attempt": 1, "sleep_seconds": 4},
            )
        ]
        actual_statuses = self.finished_spans_events_statuses()
        self.assertEqual(expected_statuses, actual_statuses)

    def _execute_begin(self, derived: _Derived, attempts: int = 1):
        """Helper for testing _SnapshotBase.begin(). Executes method and verifies
        transaction state, begin transaction API call, and span attributes and events.
        """

        session = derived._session
        database = session._database

        transaction_id = derived.begin()

        # Verify transaction state.
        begin_transaction = database.spanner_api.begin_transaction
        expected_transaction_id = begin_transaction.return_value.id or None
        expected_precommit_token = (
            begin_transaction.return_value.precommit_token or None
        )

        self.assertEqual(transaction_id, expected_transaction_id)
        self.assertEqual(derived._transaction_id, expected_transaction_id)
        self.assertEqual(derived._precommit_token, expected_precommit_token)

        # Verify begin transaction API call.
        self.assertEqual(begin_transaction.call_count, attempts)

        expected_metadata = [
            ("google-cloud-resource-prefix", database.name),
            ("x-goog-spanner-request-id", _build_request_id(database, attempts)),
        ]
        if not derived._read_only and database._route_to_leader_enabled:
            expected_metadata.insert(-1, ("x-goog-spanner-route-to-leader", "true"))

        database.spanner_api.begin_transaction.assert_called_with(
            request=BeginTransactionRequest(
                session=session.name, options=_Derived.TRANSACTION_OPTIONS
            ),
            metadata=expected_metadata,
        )

        if not HAS_OPENTELEMETRY_INSTALLED:
            return

        # Verify span attributes.
        expected_span_name = "CloudSpanner._Derived.begin"
        self.assertSpanAttributes(
            name=expected_span_name,
            attributes=_build_span_attributes(database, attempt=attempts),
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_read_other_error(self, mock_region):
        from google.cloud.spanner_v1.keyset import KeySet

        keyset = KeySet(all_=True)
        database = _Database()
        database.spanner_api = build_spanner_api()
        database.spanner_api.streaming_read.side_effect = RuntimeError()
        session = _Session(database)
        derived = _build_snapshot_derived(session)

        with self.assertRaises(RuntimeError):
            list(derived.read(TABLE_NAME, COLUMNS, keyset))

        req_id = f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1"
        self.assertSpanAttributes(
            "CloudSpanner._Derived.read",
            status=StatusCode.ERROR,
            attributes=dict(
                BASE_ATTRIBUTES,
                table_id=TABLE_NAME,
                columns=tuple(COLUMNS),
                x_goog_spanner_request_id=req_id,
            ),
        )

    def _execute_read(
        self,
        multi_use,
        first=True,
        count=0,
        partition=None,
        timeout=gapic_v1.method.DEFAULT,
        retry=gapic_v1.method.DEFAULT,
        request_options=None,
        directed_read_options=None,
        directed_read_options_at_client_level=None,
        use_multiplexed=False,
        read_only=True,
        transaction_tag=None,
        expected_request_options=_DEFAULT_EXPECTED_REQUEST_OPTIONS,
    ):
        """Helper for testing _SnapshotBase.read(). Executes method and verifies
        transaction state, begin transaction API call, and span attributes and events.
        """

        from google.protobuf.struct_pb2 import Struct

        from google.cloud.spanner_v1 import (
            PartialResultSet,
            ReadRequest,
            ResultSetMetadata,
            ResultSetStats,
            StructType,
            Type,
            TypeCode,
        )
        from google.cloud.spanner_v1._helpers import _make_value_pb
        from google.cloud.spanner_v1.keyset import KeySet

        VALUES = [["bharney", 31], ["phred", 32]]
        VALUE_PBS = [[_make_value_pb(item) for item in row] for row in VALUES]
        struct_type_pb = StructType(
            fields=[
                StructType.Field(name="name", type_=Type(code=TypeCode.STRING)),
                StructType.Field(name="age", type_=Type(code=TypeCode.INT64)),
            ]
        )

        # If the transaction had not already begun, the first result
        # set will include metadata with information about the transaction.
        transaction_pb = build_transaction_pb(id=TXN_ID) if first else None
        metadata_pb = ResultSetMetadata(
            row_type=struct_type_pb,
            transaction=transaction_pb,
        )

        stats_pb = ResultSetStats(
            query_stats=Struct(fields={"rows_returned": _make_value_pb(2)})
        )

        # Precommit tokens will be included in the result sets if the transaction is on
        # a multiplexed session. Precommit tokens may be returned out of order.
        partial_result_set_1_args = {"metadata": metadata_pb}
        if use_multiplexed:
            partial_result_set_1_args["precommit_token"] = PRECOMMIT_TOKEN_2
        partial_result_set_1 = PartialResultSet(**partial_result_set_1_args)

        partial_result_set_2_args = {"stats": stats_pb}
        if use_multiplexed:
            partial_result_set_2_args["precommit_token"] = PRECOMMIT_TOKEN_1
        partial_result_set_2 = PartialResultSet(**partial_result_set_2_args)

        result_sets = [partial_result_set_1, partial_result_set_2]

        for i in range(len(result_sets)):
            result_sets[i].values.extend(VALUE_PBS[i])
        KEYS = [["bharney@example.com"], ["phred@example.com"]]
        keyset = KeySet(keys=KEYS)
        INDEX = "email-address-index"
        LIMIT = 20
        database = _Database(
            directed_read_options=directed_read_options_at_client_level
        )

        api = database.spanner_api = build_spanner_api()
        api.streaming_read.return_value = _MockIterator(*result_sets)
        session = _Session(database)
        derived = _build_snapshot_derived(
            session, multi_use=multi_use, read_only=read_only
        )
        derived.transaction_tag = transaction_tag
        derived._read_request_count = count

        if not first:
            derived._transaction_id = TXN_ID

        if expected_request_options is not _DEFAULT_EXPECTED_REQUEST_OPTIONS:
            actual_expected_request_options = expected_request_options
        elif request_options is not None:
            actual_expected_request_options = RequestOptions(request_options)
            if read_only:
                actual_expected_request_options.transaction_tag = None
            elif transaction_tag is not None:
                actual_expected_request_options.transaction_tag = transaction_tag
        elif not read_only and transaction_tag is not None:
            actual_expected_request_options = RequestOptions(
                transaction_tag=transaction_tag
            )
        else:
            actual_expected_request_options = None

        transaction_selector_pb = derived._build_transaction_selector_pb()

        if partition is not None:  # 'limit' and 'partition' incompatible
            result_set = derived.read(
                TABLE_NAME,
                COLUMNS,
                keyset,
                index=INDEX,
                partition=partition,
                retry=retry,
                timeout=timeout,
                request_options=request_options,
                directed_read_options=directed_read_options,
            )
        else:
            result_set = derived.read(
                TABLE_NAME,
                COLUMNS,
                keyset,
                index=INDEX,
                limit=LIMIT,
                retry=retry,
                timeout=timeout,
                request_options=request_options,
                directed_read_options=directed_read_options,
            )

        self.assertEqual(derived._read_request_count, count + 1)

        self.assertEqual(list(result_set), VALUES)
        self.assertEqual(result_set.metadata, metadata_pb)
        self.assertEqual(result_set.stats, stats_pb)

        if partition is not None:
            expected_limit = 0
        else:
            expected_limit = LIMIT

        expected_directed_read_options = (
            directed_read_options
            if directed_read_options is not None
            else directed_read_options_at_client_level
        )

        expected_request = ReadRequest(
            session=session.name,
            table=TABLE_NAME,
            columns=COLUMNS,
            key_set=keyset._to_pb(),
            transaction=transaction_selector_pb,
            index=INDEX,
            limit=expected_limit,
            partition_token=partition,
            request_options=actual_expected_request_options,
            directed_read_options=expected_directed_read_options,
        )
        req_id = f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1"
        expected_metadata = [
            ("google-cloud-resource-prefix", database.name),
        ]
        if not read_only:
            expected_metadata.append(("x-goog-spanner-route-to-leader", "true"))
        expected_metadata.append(("x-goog-spanner-request-id", req_id))
        api.streaming_read.assert_called_once_with(
            request=expected_request,
            metadata=expected_metadata,
            # Retries are handled by _restart_on_unavailable, not the GAPIC call.
            retry=None,
            timeout=timeout,
        )
        expected_attributes = dict(
            BASE_ATTRIBUTES,
            table_id=TABLE_NAME,
            columns=tuple(COLUMNS),
            x_goog_spanner_request_id=req_id,
        )
        request_tag = (
            request_options.get("request_tag")
            if isinstance(request_options, dict)
            else getattr(request_options, "request_tag", None)
        )
        if request_tag:
            expected_attributes["request.tag"] = request_tag
        self.assertSpanAttributes(
            "CloudSpanner._Derived.read", attributes=expected_attributes
        )

        if first:
            self.assertEqual(derived._transaction_id, TXN_ID)

        if use_multiplexed:
            self.assertEqual(derived._precommit_token, PRECOMMIT_TOKEN_2)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_read_wo_multi_use(self, mock_region):
        self._execute_read(multi_use=False)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_read_w_request_tag_success(self, mock_region):
        request_options = {"request_tag": "tag-1"}
        self._execute_read(
            multi_use=False,
            request_options=request_options,
            expected_request_options=RequestOptions(request_tag="tag-1"),
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_read_w_transaction_tag_success(self, mock_region):
        request_options = {"transaction_tag": "tag-1-1"}
        self._execute_read(
            multi_use=False,
            request_options=request_options,
            expected_request_options=RequestOptions(),
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_read_w_request_and_transaction_tag_success(self, mock_region):
        request_options = {"request_tag": "tag-1", "transaction_tag": "tag-1-1"}
        self._execute_read(
            multi_use=False,
            request_options=request_options,
            expected_request_options=RequestOptions(request_tag="tag-1"),
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_read_w_request_and_transaction_tag_dictionary_success(self, mock_region):
        request_options = {"request_tag": "tag-1", "transaction_tag": "tag-1-1"}
        self._execute_read(
            multi_use=False,
            request_options=request_options,
            expected_request_options=RequestOptions(request_tag="tag-1"),
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_read_in_read_write_transaction_with_tag(self, mock_region):
        self._execute_read(
            multi_use=False,
            read_only=False,
            transaction_tag="tx-tag",
            expected_request_options=RequestOptions(transaction_tag="tx-tag"),
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_read_in_read_write_transaction_caller_tag_preserved(self, mock_region):
        self._execute_read(
            multi_use=False,
            read_only=False,
            transaction_tag=None,
            request_options={
                "request_tag": "r-tag",
                "transaction_tag": "caller-tx-tag",
            },
            expected_request_options=RequestOptions(
                request_tag="r-tag", transaction_tag="caller-tx-tag"
            ),
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_read_w_incorrect_tag_dictionary_error(self, mock_region):
        request_options = {"incorrect_tag": "tag-1-1"}
        with self.assertRaises(ValueError):
            self._execute_read(multi_use=False, request_options=request_options)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_read_wo_multi_use_w_read_request_count_gt_0(self, mock_region):
        with self.assertRaises(ValueError):
            self._execute_read(multi_use=False, count=1)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_read_w_multi_use_w_first(self, mock_region):
        self._execute_read(multi_use=True, first=True)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_read_w_multi_use_wo_first(self, mock_region):
        self._execute_read(multi_use=True, first=False)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_read_w_multi_use_wo_first_w_count_gt_0(self, mock_region):
        self._execute_read(multi_use=True, first=False, count=1)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_read_w_multi_use_w_first_w_partition(self, mock_region):
        PARTITION = b"FADEABED"
        self._execute_read(multi_use=True, first=True, partition=PARTITION)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    @mock.patch(
        "google.cloud.spanner_v1.snapshot._TRANSACTION_BEGIN_TIMEOUT_SECONDS", 0.01
    )
    def test_read_w_multi_use_w_first_w_count_gt_0(self, mock_region):
        # No concurrent request ever begins the transaction, so this request
        # waits for the begin timeout to expire before giving up.
        with self.assertRaisesRegex(
            ValueError, "Timed out waiting for transaction to begin."
        ):
            self._execute_read(multi_use=True, first=True, count=1)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_read_w_timeout_param(self, mock_region):
        self._execute_read(multi_use=True, first=False, timeout=2.0)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_read_w_retry_param(self, mock_region):
        self._execute_read(multi_use=True, first=False, retry=Retry(deadline=60))

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_read_w_timeout_and_retry_params(self, mock_region):
        self._execute_read(
            multi_use=True, first=False, retry=Retry(deadline=60), timeout=2.0
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_read_w_directed_read_options(self, mock_region):
        self._execute_read(multi_use=False, directed_read_options=DIRECTED_READ_OPTIONS)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_read_w_directed_read_options_at_client_level(self, mock_region):
        self._execute_read(
            multi_use=False,
            directed_read_options_at_client_level=DIRECTED_READ_OPTIONS_FOR_CLIENT,
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_read_w_directed_read_options_override(self, mock_region):
        self._execute_read(
            multi_use=False,
            directed_read_options=DIRECTED_READ_OPTIONS,
            directed_read_options_at_client_level=DIRECTED_READ_OPTIONS_FOR_CLIENT,
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_read_w_precommit_tokens(self, mock_region):
        self._execute_read(multi_use=True, use_multiplexed=True)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_execute_sql_other_error(self, mock_region):
        database = _Database()
        database.spanner_api = build_spanner_api()
        database.spanner_api.execute_streaming_sql.side_effect = RuntimeError()
        session = _Session(database)
        derived = _build_snapshot_derived(session)

        with self.assertRaises(RuntimeError):
            list(derived.execute_sql(SQL_QUERY))

        self.assertEqual(derived._execute_sql_request_count, 1)

        req_id = f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1"
        self.assertSpanAttributes(
            "CloudSpanner._Derived.execute_sql",
            status=StatusCode.ERROR,
            attributes=dict(
                BASE_ATTRIBUTES,
                **{"db.statement": SQL_QUERY, "x_goog_spanner_request_id": req_id},
            ),
        )

    def _execute_sql_helper(
        self,
        multi_use,
        first=True,
        count=0,
        partition=None,
        sql_count=0,
        query_options=None,
        request_options=None,
        timeout=gapic_v1.method.DEFAULT,
        retry=gapic_v1.method.DEFAULT,
        directed_read_options=None,
        directed_read_options_at_client_level=None,
        use_multiplexed=False,
        read_only=True,
        transaction_tag=None,
        expected_request_options=_DEFAULT_EXPECTED_REQUEST_OPTIONS,
    ):
        """Helper for testing _SnapshotBase.execute_sql(). Executes method and verifies
        transaction state, begin transaction API call, and span attributes and events.
        """

        from google.protobuf.struct_pb2 import Struct

        from google.cloud.spanner_v1 import (
            ExecuteSqlRequest,
            PartialResultSet,
            ResultSetMetadata,
            ResultSetStats,
            StructType,
            Type,
            TypeCode,
        )
        from google.cloud.spanner_v1._helpers import (
            _make_value_pb,
            _merge_query_options,
        )

        VALUES = [["bharney", "rhubbyl", 31], ["phred", "phlyntstone", 32]]
        VALUE_PBS = [[_make_value_pb(item) for item in row] for row in VALUES]
        MODE = 2  # PROFILE
        struct_type_pb = StructType(
            fields=[
                StructType.Field(name="first_name", type_=Type(code=TypeCode.STRING)),
                StructType.Field(name="last_name", type_=Type(code=TypeCode.STRING)),
                StructType.Field(name="age", type_=Type(code=TypeCode.INT64)),
            ]
        )

        # If the transaction has not already begun, the first result set will
        # include metadata with information about the newly-begun transaction.
        transaction_pb = build_transaction_pb(id=TXN_ID) if first else None
        metadata_pb = ResultSetMetadata(
            row_type=struct_type_pb,
            transaction=transaction_pb,
        )

        stats_pb = ResultSetStats(
            query_stats=Struct(fields={"rows_returned": _make_value_pb(2)})
        )

        # Precommit tokens will be included in the result sets if the transaction is on
        # a multiplexed session. Return the precommit tokens out of order to verify that
        # the transaction tracks the one with the highest sequence number.
        partial_result_set_1_args = {"metadata": metadata_pb}
        if use_multiplexed:
            partial_result_set_1_args["precommit_token"] = PRECOMMIT_TOKEN_2
        partial_result_set_1 = PartialResultSet(**partial_result_set_1_args)

        partial_result_set_2_args = {"stats": stats_pb}
        if use_multiplexed:
            partial_result_set_2_args["precommit_token"] = PRECOMMIT_TOKEN_1
        partial_result_set_2 = PartialResultSet(**partial_result_set_2_args)

        result_sets = [partial_result_set_1, partial_result_set_2]

        for i in range(len(result_sets)):
            result_sets[i].values.extend(VALUE_PBS[i])
        iterator = _MockIterator(*result_sets)
        database = _Database(
            directed_read_options=directed_read_options_at_client_level
        )
        api = database.spanner_api = build_spanner_api()
        api.execute_streaming_sql.return_value = iterator
        session = _Session(database)
        derived = _build_snapshot_derived(
            session, multi_use=multi_use, read_only=read_only
        )
        derived.transaction_tag = transaction_tag
        derived._read_request_count = count
        derived._execute_sql_request_count = sql_count
        if not first:
            derived._transaction_id = TXN_ID

        if expected_request_options is not _DEFAULT_EXPECTED_REQUEST_OPTIONS:
            actual_expected_request_options = expected_request_options
        elif request_options is not None:
            actual_expected_request_options = RequestOptions(request_options)
            if read_only:
                actual_expected_request_options.transaction_tag = None
            elif transaction_tag is not None:
                actual_expected_request_options.transaction_tag = transaction_tag
        elif not read_only and transaction_tag is not None:
            actual_expected_request_options = RequestOptions(
                transaction_tag=transaction_tag
            )
        else:
            actual_expected_request_options = None

        transaction_selector_pb = derived._build_transaction_selector_pb()

        result_set = derived.execute_sql(
            SQL_QUERY_WITH_PARAM,
            PARAMS,
            PARAM_TYPES,
            query_mode=MODE,
            query_options=query_options,
            request_options=request_options,
            partition=partition,
            retry=retry,
            timeout=timeout,
            directed_read_options=directed_read_options,
        )

        self.assertEqual(derived._read_request_count, count + 1)

        self.assertEqual(list(result_set), VALUES)
        self.assertEqual(result_set.metadata, metadata_pb)
        self.assertEqual(result_set.stats, stats_pb)

        expected_params = Struct(
            fields={key: _make_value_pb(value) for (key, value) in PARAMS.items()}
        )

        expected_query_options = database._instance._client._query_options
        if query_options:
            expected_query_options = _merge_query_options(
                expected_query_options, query_options
            )

        expected_directed_read_options = (
            directed_read_options
            if directed_read_options is not None
            else directed_read_options_at_client_level
        )

        expected_request = ExecuteSqlRequest(
            session=session.name,
            sql=SQL_QUERY_WITH_PARAM,
            transaction=transaction_selector_pb,
            params=expected_params,
            param_types=PARAM_TYPES,
            query_mode=MODE,
            query_options=expected_query_options,
            request_options=actual_expected_request_options,
            partition_token=partition,
            seqno=sql_count,
            directed_read_options=expected_directed_read_options,
        )
        req_id = f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1"
        expected_metadata = [
            ("google-cloud-resource-prefix", database.name),
        ]
        if not read_only:
            expected_metadata.append(("x-goog-spanner-route-to-leader", "true"))
        expected_metadata.append(("x-goog-spanner-request-id", req_id))
        api.execute_streaming_sql.assert_called_once_with(
            request=expected_request,
            metadata=expected_metadata,
            timeout=timeout,
            # Retries are handled by _restart_on_unavailable, not the GAPIC call.
            retry=None,
        )

        self.assertEqual(derived._execute_sql_request_count, sql_count + 1)

        expected_attributes = dict(
            BASE_ATTRIBUTES,
            **{
                "db.statement": SQL_QUERY_WITH_PARAM,
                "x_goog_spanner_request_id": req_id,
            },
        )
        request_tag = (
            request_options.get("request_tag")
            if isinstance(request_options, dict)
            else getattr(request_options, "request_tag", None)
        )
        if request_tag:
            expected_attributes["request.tag"] = request_tag

        self.assertSpanAttributes(
            "CloudSpanner._Derived.execute_sql",
            status=StatusCode.OK,
            attributes=expected_attributes,
        )

        if first:
            self.assertEqual(derived._transaction_id, TXN_ID)

        if use_multiplexed:
            self.assertEqual(derived._precommit_token, PRECOMMIT_TOKEN_2)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_execute_sql_wo_multi_use(self, mock_region):
        self._execute_sql_helper(multi_use=False)

    def test_execute_sql_wo_multi_use_w_read_request_count_gt_0(self):
        with self.assertRaises(ValueError):
            self._execute_sql_helper(multi_use=False, count=1)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_execute_sql_w_multi_use_wo_first(self, mock_region):
        self._execute_sql_helper(multi_use=True, first=False, sql_count=1)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_execute_sql_w_multi_use_wo_first_w_count_gt_0(self, mock_region):
        self._execute_sql_helper(multi_use=True, first=False, count=1)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_execute_sql_w_multi_use_w_first(self, mock_region):
        self._execute_sql_helper(multi_use=True, first=True)

    @mock.patch(
        "google.cloud.spanner_v1.snapshot._TRANSACTION_BEGIN_TIMEOUT_SECONDS", 0.01
    )
    def test_execute_sql_w_multi_use_w_first_w_count_gt_0(self):
        # No concurrent request ever begins the transaction, so this request
        # waits for the begin timeout to expire before giving up.
        with self.assertRaisesRegex(
            ValueError, "Timed out waiting for transaction to begin."
        ):
            self._execute_sql_helper(multi_use=True, first=True, count=1)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_execute_sql_w_retry(self, mock_region):
        self._execute_sql_helper(multi_use=False, retry=None)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_execute_sql_w_timeout(self, mock_region):
        self._execute_sql_helper(multi_use=False, timeout=None)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_execute_sql_w_query_options(self, mock_region):
        from google.cloud.spanner_v1 import ExecuteSqlRequest

        self._execute_sql_helper(
            multi_use=False,
            query_options=ExecuteSqlRequest.QueryOptions(optimizer_version="3"),
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_execute_sql_w_request_options(self, mock_region):
        self._execute_sql_helper(
            multi_use=False,
            request_options=RequestOptions(
                priority=RequestOptions.Priority.PRIORITY_MEDIUM
            ),
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_execute_sql_w_request_tag_success(self, mock_region):
        request_options = {"request_tag": "tag-1"}
        self._execute_sql_helper(
            multi_use=False,
            request_options=request_options,
            expected_request_options=RequestOptions(request_tag="tag-1"),
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_execute_sql_w_transaction_tag_success(self, mock_region):
        request_options = {"transaction_tag": "tag-1-1"}
        self._execute_sql_helper(
            multi_use=False,
            request_options=request_options,
            expected_request_options=RequestOptions(),
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_execute_sql_w_request_and_transaction_tag_success(self, mock_region):
        request_options = {"request_tag": "tag-1", "transaction_tag": "tag-1-1"}
        self._execute_sql_helper(
            multi_use=False,
            request_options=request_options,
            expected_request_options=RequestOptions(request_tag="tag-1"),
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_execute_sql_w_request_and_transaction_tag_dictionary_success(
        self, mock_region
    ):
        request_options = {"request_tag": "tag-1", "transaction_tag": "tag-1-1"}
        self._execute_sql_helper(
            multi_use=False,
            request_options=request_options,
            expected_request_options=RequestOptions(request_tag="tag-1"),
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_execute_sql_in_read_write_transaction_with_tag(self, mock_region):
        self._execute_sql_helper(
            multi_use=False,
            read_only=False,
            transaction_tag="tx-tag",
            expected_request_options=RequestOptions(transaction_tag="tx-tag"),
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_execute_sql_in_read_write_transaction_caller_tag_preserved(
        self, mock_region
    ):
        self._execute_sql_helper(
            multi_use=False,
            read_only=False,
            transaction_tag=None,
            request_options={
                "request_tag": "r-tag",
                "transaction_tag": "caller-tx-tag",
            },
            expected_request_options=RequestOptions(
                request_tag="r-tag", transaction_tag="caller-tx-tag"
            ),
        )

    def test_execute_sql_w_incorrect_tag_dictionary_error(self):
        request_options = {"incorrect_tag": "tag-1-1"}
        with self.assertRaises(ValueError):
            self._execute_sql_helper(multi_use=False, request_options=request_options)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_execute_sql_w_directed_read_options(self, mock_region):
        self._execute_sql_helper(
            multi_use=False, directed_read_options=DIRECTED_READ_OPTIONS
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_execute_sql_w_directed_read_options_at_client_level(self, mock_region):
        self._execute_sql_helper(
            multi_use=False,
            directed_read_options_at_client_level=DIRECTED_READ_OPTIONS_FOR_CLIENT,
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_execute_sql_w_directed_read_options_override(self, mock_region):
        self._execute_sql_helper(
            multi_use=False,
            directed_read_options=DIRECTED_READ_OPTIONS,
            directed_read_options_at_client_level=DIRECTED_READ_OPTIONS_FOR_CLIENT,
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_execute_sql_w_precommit_tokens(self, mock_region):
        self._execute_sql_helper(multi_use=True, use_multiplexed=True)

    def _partition_read_helper(
        self,
        multi_use,
        w_txn,
        size=None,
        max_partitions=None,
        index=None,
        retry=gapic_v1.method.DEFAULT,
        timeout=gapic_v1.method.DEFAULT,
    ):
        from google.cloud.spanner_v1 import (
            Partition,
            PartitionOptions,
            PartitionReadRequest,
            PartitionResponse,
            Transaction,
        )
        from google.cloud.spanner_v1.keyset import KeySet

        keyset = KeySet(all_=True)
        new_txn_id = b"ABECAB91"
        token_1 = b"FACE0FFF"
        token_2 = b"BADE8CAF"
        response = PartitionResponse(
            partitions=[
                Partition(partition_token=token_1),
                Partition(partition_token=token_2),
            ],
            transaction=Transaction(id=new_txn_id),
        )
        database = _Database()
        api = database.spanner_api = build_spanner_api()
        api.partition_read.return_value = response
        session = _Session(database)
        derived = _build_snapshot_derived(session, multi_use=multi_use)

        if w_txn:
            derived._transaction_id = TXN_ID

        transaction_selector_pb = derived._build_transaction_selector_pb()

        tokens = list(
            derived.partition_read(
                TABLE_NAME,
                COLUMNS,
                keyset,
                index=index,
                partition_size_bytes=size,
                max_partitions=max_partitions,
                retry=retry,
                timeout=timeout,
            )
        )

        self.assertEqual(tokens, [token_1, token_2])

        expected_partition_options = PartitionOptions(
            partition_size_bytes=size, max_partitions=max_partitions
        )

        expected_request = PartitionReadRequest(
            session=session.name,
            table=TABLE_NAME,
            columns=COLUMNS,
            key_set=keyset._to_pb(),
            transaction=transaction_selector_pb,
            index=index,
            partition_options=expected_partition_options,
        )
        req_id = f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1"
        api.partition_read.assert_called_once_with(
            request=expected_request,
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    req_id,
                ),
            ],
            retry=retry,
            timeout=timeout,
        )

        want_span_attributes = dict(
            BASE_ATTRIBUTES,
            table_id=TABLE_NAME,
            columns=tuple(COLUMNS),
            x_goog_spanner_request_id=req_id,
        )
        if index:
            want_span_attributes["index"] = index
        self.assertSpanAttributes(
            "CloudSpanner._Derived.partition_read",
            status=StatusCode.OK,
            attributes=want_span_attributes,
        )

    def test_partition_read_single_use_raises(self):
        with self.assertRaises(ValueError):
            self._partition_read_helper(multi_use=False, w_txn=True)

    def test_partition_read_wo_existing_transaction_raises(self):
        with self.assertRaises(ValueError):
            self._partition_read_helper(multi_use=True, w_txn=False)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_partition_read_other_error(self, mock_region):
        from google.cloud.spanner_v1.keyset import KeySet

        keyset = KeySet(all_=True)
        database = _Database()
        database.spanner_api = build_spanner_api()
        database.spanner_api.partition_read.side_effect = RuntimeError()
        session = _Session(database)
        derived = _build_snapshot_derived(session, multi_use=True)
        derived._transaction_id = TXN_ID

        with self.assertRaises(RuntimeError):
            list(derived.partition_read(TABLE_NAME, COLUMNS, keyset))

        req_id = f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1"
        self.assertSpanAttributes(
            "CloudSpanner._Derived.partition_read",
            status=StatusCode.ERROR,
            attributes=dict(
                BASE_ATTRIBUTES,
                table_id=TABLE_NAME,
                columns=tuple(COLUMNS),
                x_goog_spanner_request_id=req_id,
            ),
        )

    @mock.patch("google.cloud.spanner_v1._helpers.time.sleep")
    def test_partition_read_w_retry(self, mock_sleep):
        from google.cloud.spanner_v1 import Partition, PartitionResponse, Transaction
        from google.cloud.spanner_v1.keyset import KeySet

        keyset = KeySet(all_=True)
        database = _Database()
        api = database.spanner_api = build_spanner_api()
        new_txn_id = b"ABECAB91"
        token_1 = b"FACE0FFF"
        token_2 = b"BADE8CAF"
        response = PartitionResponse(
            partitions=[
                Partition(partition_token=token_1),
                Partition(partition_token=token_2),
            ],
            transaction=Transaction(id=new_txn_id),
        )
        database.spanner_api.partition_read.side_effect = [
            INTERNAL_SERVER_ERROR_UNEXPECTED_EOS,
            response,
        ]

        session = _Session(database)
        derived = _build_snapshot_derived(session, multi_use=True)
        derived._transaction_id = TXN_ID

        list(derived.partition_read(TABLE_NAME, COLUMNS, keyset))

        self.assertEqual(api.partition_read.call_count, 2)
        mock_sleep.assert_called_once_with(2)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_partition_read_ok_w_index_no_options(self, mock_region):
        self._partition_read_helper(multi_use=True, w_txn=True, index="index")

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_partition_read_ok_w_size(self, mock_region):
        self._partition_read_helper(multi_use=True, w_txn=True, size=2000)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_partition_read_ok_w_max_partitions(self, mock_region):
        self._partition_read_helper(multi_use=True, w_txn=True, max_partitions=4)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_partition_read_ok_w_timeout_param(self, mock_region):
        self._partition_read_helper(multi_use=True, w_txn=True, timeout=2.0)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_partition_read_ok_w_retry_param(self, mock_region):
        self._partition_read_helper(
            multi_use=True, w_txn=True, retry=Retry(deadline=60)
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_partition_read_ok_w_timeout_and_retry_params(self, mock_region):
        self._partition_read_helper(
            multi_use=True, w_txn=True, retry=Retry(deadline=60), timeout=2.0
        )

    def _partition_query_helper(
        self,
        multi_use,
        w_txn,
        size=None,
        max_partitions=None,
        retry=gapic_v1.method.DEFAULT,
        timeout=gapic_v1.method.DEFAULT,
    ):
        """Helper for testing _SnapshotBase.partition_query(). Executes method and verifies
        transaction state, begin transaction API call, and span attributes and events.
        """

        from google.protobuf.struct_pb2 import Struct

        from google.cloud.spanner_v1 import (
            Partition,
            PartitionOptions,
            PartitionQueryRequest,
            PartitionResponse,
            Transaction,
        )
        from google.cloud.spanner_v1._helpers import _make_value_pb

        new_txn_id = b"ABECAB91"
        token_1 = b"FACE0FFF"
        token_2 = b"BADE8CAF"
        response = PartitionResponse(
            partitions=[
                Partition(partition_token=token_1),
                Partition(partition_token=token_2),
            ],
            transaction=Transaction(id=new_txn_id),
        )
        database = _Database()
        api = database.spanner_api = build_spanner_api()
        api.partition_query.return_value = response
        session = _Session(database)
        derived = _build_snapshot_derived(session, multi_use=multi_use)
        if w_txn:
            derived._transaction_id = TXN_ID

        transaction_selector_pb = derived._build_transaction_selector_pb()

        tokens = list(
            derived.partition_query(
                SQL_QUERY_WITH_PARAM,
                PARAMS,
                PARAM_TYPES,
                partition_size_bytes=size,
                max_partitions=max_partitions,
                retry=retry,
                timeout=timeout,
            )
        )

        self.assertEqual(tokens, [token_1, token_2])

        expected_params = Struct(
            fields={key: _make_value_pb(value) for (key, value) in PARAMS.items()}
        )

        expected_partition_options = PartitionOptions(
            partition_size_bytes=size, max_partitions=max_partitions
        )

        expected_request = PartitionQueryRequest(
            session=session.name,
            sql=SQL_QUERY_WITH_PARAM,
            transaction=transaction_selector_pb,
            params=expected_params,
            param_types=PARAM_TYPES,
            partition_options=expected_partition_options,
        )
        req_id = f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1"
        api.partition_query.assert_called_once_with(
            request=expected_request,
            metadata=[
                ("google-cloud-resource-prefix", database.name),
                ("x-goog-spanner-route-to-leader", "true"),
                (
                    "x-goog-spanner-request-id",
                    req_id,
                ),
            ],
            retry=retry,
            timeout=timeout,
        )

        self.assertSpanAttributes(
            "CloudSpanner._Derived.partition_query",
            status=StatusCode.OK,
            attributes=dict(
                BASE_ATTRIBUTES,
                **{
                    "db.statement": SQL_QUERY_WITH_PARAM,
                    "x_goog_spanner_request_id": req_id,
                },
            ),
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_partition_query_other_error(self, mock_region):
        database = _Database()
        database.spanner_api = build_spanner_api()
        database.spanner_api.partition_query.side_effect = RuntimeError()
        session = _Session(database)
        derived = _build_snapshot_derived(session, multi_use=True)
        derived._transaction_id = TXN_ID

        with self.assertRaises(RuntimeError):
            list(derived.partition_query(SQL_QUERY))

        req_id = f"1.{REQ_RAND_PROCESS_ID}.{database._nth_client_id}.{database._channel_id}.1.1"
        self.assertSpanAttributes(
            "CloudSpanner._Derived.partition_query",
            status=StatusCode.ERROR,
            attributes=dict(
                BASE_ATTRIBUTES,
                **{"db.statement": SQL_QUERY, "x_goog_spanner_request_id": req_id},
            ),
        )

    def test_partition_query_single_use_raises(self):
        with self.assertRaises(ValueError):
            self._partition_query_helper(multi_use=False, w_txn=True)

    def test_partition_query_wo_transaction_raises(self):
        with self.assertRaises(ValueError):
            self._partition_query_helper(multi_use=True, w_txn=False)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_partition_query_ok_w_index_no_options(self, mock_region):
        self._partition_query_helper(multi_use=True, w_txn=True)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_partition_query_ok_w_size(self, mock_region):
        self._partition_query_helper(multi_use=True, w_txn=True, size=2000)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_partition_query_ok_w_max_partitions(self, mock_region):
        self._partition_query_helper(multi_use=True, w_txn=True, max_partitions=4)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_partition_query_ok_w_timeout_param(self, mock_region):
        self._partition_query_helper(multi_use=True, w_txn=True, timeout=2.0)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_partition_query_ok_w_retry_param(self, mock_region):
        self._partition_query_helper(
            multi_use=True, w_txn=True, retry=Retry(deadline=30)
        )

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_partition_query_ok_w_timeout_and_retry_params(self, mock_region):
        self._partition_query_helper(
            multi_use=True, w_txn=True, retry=Retry(deadline=60), timeout=2.0
        )


class TestSnapshot(OpenTelemetryBase):
    PROJECT_ID = "project-id"
    INSTANCE_ID = "instance-id"
    INSTANCE_NAME = "projects/" + PROJECT_ID + "/instances/" + INSTANCE_ID
    DATABASE_ID = "database-id"
    DATABASE_NAME = INSTANCE_NAME + "/databases/" + DATABASE_ID
    SESSION_ID = "session-id"
    SESSION_NAME = DATABASE_NAME + "/sessions/" + SESSION_ID

    def _getTargetClass(self):
        from google.cloud.spanner_v1.snapshot import Snapshot

        return Snapshot

    def _make_one(self, *args, **kwargs):
        return self._getTargetClass()(*args, **kwargs)

    def _makeDuration(self, seconds=1, microseconds=0):
        import datetime

        return datetime.timedelta(seconds=seconds, microseconds=microseconds)

    def test_ctor_defaults(self):
        session = build_session()
        snapshot = build_snapshot(session=session)

        # Attributes from _SessionWrapper.
        self.assertIs(snapshot._session, session)

        # Attributes from _SnapshotBase.
        self.assertTrue(snapshot._read_only)
        self.assertFalse(snapshot._multi_use)
        self.assertEqual(snapshot._execute_sql_request_count, 0)
        self.assertEqual(snapshot._read_request_count, 0)
        self.assertIsNone(snapshot._transaction_id)
        self.assertIsNone(snapshot._precommit_token)
        self.assertIsNone(snapshot._lock)
        self.assertIsNone(snapshot._transaction_begin_event)

        # Attributes from Snapshot.
        self.assertTrue(snapshot._strong)
        self.assertIsNone(snapshot._read_timestamp)
        self.assertIsNone(snapshot._min_read_timestamp)
        self.assertIsNone(snapshot._max_staleness)
        self.assertIsNone(snapshot._exact_staleness)

    def test_ctor_multi_use(self):
        session = build_session()
        snapshot = build_snapshot(session=session, multi_use=True)

        self.assertIs(snapshot._session, session)
        self.assertTrue(snapshot._read_only)
        self.assertTrue(snapshot._multi_use)
        self.assertIsNone(snapshot._transaction_id)
        self.assertIsInstance(snapshot._lock, type(Lock()))
        self.assertIsInstance(snapshot._transaction_begin_event, type(Event()))

    def test_ctor_single_use_no_lock(self):
        session = build_session()
        snapshot = build_snapshot(session=session, multi_use=False)
        self.assertFalse(snapshot._multi_use)
        self.assertIsNone(snapshot._lock)
        self.assertIsNone(snapshot._transaction_begin_event)

    def test_update_for_precommit_token_pb_multi_use(self):
        token = build_precommit_token_pb(seq_num=1)
        snapshot = self._make_one(_Session(), multi_use=True)
        snapshot._update_for_precommit_token_pb(token)
        self.assertEqual(snapshot._precommit_token, token)

    def test_update_for_precommit_token_pb_single_use(self):
        token = build_precommit_token_pb(seq_num=1)
        snapshot = self._make_one(_Session(), multi_use=False)
        snapshot._update_for_precommit_token_pb(token)
        self.assertEqual(snapshot._precommit_token, token)

    def test__update_for_transaction_pb(self):
        from datetime import timezone

        from google.cloud.spanner_v1.types.transaction import (
            Transaction as TransactionPB,
        )

        timestamp = datetime.now(timezone.utc)
        snapshot = self._make_one(_Session(), multi_use=False)
        pb = TransactionPB(id=TXN_ID, read_timestamp=timestamp)
        snapshot._update_for_transaction_pb(pb)
        self.assertEqual(snapshot._transaction_id, TXN_ID)
        self.assertEqual(snapshot._transaction_read_timestamp, timestamp)

    def test__update_for_transaction_pb_multi_use(self):
        from datetime import timezone

        from google.cloud.spanner_v1.types.transaction import (
            Transaction as TransactionPB,
        )

        timestamp = datetime.now(timezone.utc)
        snapshot = self._make_one(_Session(), multi_use=True)
        self.assertFalse(snapshot._transaction_begin_event.is_set())
        pb = TransactionPB(id=TXN_ID, read_timestamp=timestamp)
        snapshot._update_for_transaction_pb(pb)
        self.assertEqual(snapshot._transaction_id, TXN_ID)
        self.assertEqual(snapshot._transaction_read_timestamp, timestamp)
        self.assertTrue(snapshot._transaction_begin_event.is_set())

    def test_execute_sql_twice_single_use_fails(self):
        from google.cloud.spanner_v1 import PartialResultSet

        database = _Database()
        database.spanner_api = build_spanner_api()
        database.spanner_api.execute_streaming_sql.return_value = _MockIterator(
            PartialResultSet()
        )
        session = _Session(database)
        snapshot = self._make_one(session=session, multi_use=False)
        list(snapshot.execute_sql(SQL_QUERY))
        with self.assertRaisesRegex(ValueError, "Cannot re-use single-use snapshot."):
            list(snapshot.execute_sql(SQL_QUERY))

    def test_read_twice_single_use_fails(self):
        from google.cloud.spanner_v1 import PartialResultSet
        from google.cloud.spanner_v1.keyset import KeySet

        database = _Database()
        database.spanner_api = build_spanner_api()
        database.spanner_api.streaming_read.return_value = _MockIterator(
            PartialResultSet()
        )
        session = _Session(database)
        snapshot = self._make_one(session=session, multi_use=False)
        keyset = KeySet(all_=True)
        list(snapshot.read(TABLE_NAME, COLUMNS, keyset))
        with self.assertRaisesRegex(ValueError, "Cannot re-use single-use snapshot."):
            list(snapshot.read(TABLE_NAME, COLUMNS, keyset))

    def test_ctor_w_multiple_options(self):
        with self.assertRaises(ValueError):
            build_snapshot(read_timestamp=datetime.min, max_staleness=timedelta())

    def test_ctor_w_read_timestamp(self):
        snapshot = build_snapshot(read_timestamp=TIMESTAMP)
        self.assertEqual(snapshot._read_timestamp, TIMESTAMP)

    def test_ctor_w_min_read_timestamp(self):
        snapshot = build_snapshot(min_read_timestamp=TIMESTAMP)
        self.assertEqual(snapshot._min_read_timestamp, TIMESTAMP)

    def test_ctor_w_max_staleness(self):
        snapshot = build_snapshot(max_staleness=DURATION)
        self.assertEqual(snapshot._max_staleness, DURATION)

    def test_ctor_w_exact_staleness(self):
        snapshot = build_snapshot(exact_staleness=DURATION)
        self.assertEqual(snapshot._exact_staleness, DURATION)

    def test_ctor_w_multi_use(self):
        snapshot = build_snapshot(multi_use=True)
        self.assertTrue(snapshot._multi_use)

    def test_ctor_w_multi_use_and_read_timestamp(self):
        snapshot = build_snapshot(multi_use=True, read_timestamp=TIMESTAMP)
        self.assertTrue(snapshot._multi_use)
        self.assertEqual(snapshot._read_timestamp, TIMESTAMP)

    def test_ctor_w_multi_use_and_min_read_timestamp(self):
        with self.assertRaises(ValueError):
            build_snapshot(multi_use=True, min_read_timestamp=TIMESTAMP)

    def test_ctor_w_multi_use_and_max_staleness(self):
        with self.assertRaises(ValueError):
            build_snapshot(multi_use=True, max_staleness=DURATION)

    def test_ctor_w_multi_use_and_exact_staleness(self):
        snapshot = build_snapshot(multi_use=True, exact_staleness=DURATION)
        self.assertTrue(snapshot._multi_use)
        self.assertEqual(snapshot._exact_staleness, DURATION)

    def test__build_transaction_options_strong(self):
        snapshot = build_snapshot()
        options = snapshot._build_transaction_options_pb()

        self.assertEqual(
            options,
            TransactionOptions(
                read_only=TransactionOptions.ReadOnly(
                    strong=True, return_read_timestamp=True
                )
            ),
        )

    def test__build_transaction_options_w_read_timestamp(self):
        snapshot = build_snapshot(read_timestamp=TIMESTAMP)
        options = snapshot._build_transaction_options_pb()

        self.assertEqual(
            options,
            TransactionOptions(
                read_only=TransactionOptions.ReadOnly(
                    read_timestamp=TIMESTAMP, return_read_timestamp=True
                )
            ),
        )

    def test__build_transaction_options_w_min_read_timestamp(self):
        snapshot = build_snapshot(min_read_timestamp=TIMESTAMP)
        options = snapshot._build_transaction_options_pb()

        self.assertEqual(
            options,
            TransactionOptions(
                read_only=TransactionOptions.ReadOnly(
                    min_read_timestamp=TIMESTAMP, return_read_timestamp=True
                )
            ),
        )

    def test__build_transaction_options_w_max_staleness(self):
        snapshot = build_snapshot(max_staleness=DURATION)
        options = snapshot._build_transaction_options_pb()

        self.assertEqual(
            options,
            TransactionOptions(
                read_only=TransactionOptions.ReadOnly(
                    max_staleness=DURATION, return_read_timestamp=True
                )
            ),
        )

    def test__build_transaction_options_w_exact_staleness(self):
        snapshot = build_snapshot(exact_staleness=DURATION)
        options = snapshot._build_transaction_options_pb()

        self.assertEqual(
            options,
            TransactionOptions(
                read_only=TransactionOptions.ReadOnly(
                    exact_staleness=DURATION, return_read_timestamp=True
                )
            ),
        )


class _Client(object):
    NTH_CLIENT = AtomicCounter()

    def __init__(self):
        from google.cloud.spanner_v1 import ExecuteSqlRequest

        self.project = "project-id"
        self._query_options = ExecuteSqlRequest.QueryOptions(optimizer_version="1")
        self._client_context = None
        self._nth_client_id = _Client.NTH_CLIENT.increment()
        self._nth_request = AtomicCounter()

    @property
    def _next_nth_request(self):
        return self._nth_request.increment()


class _Instance(object):
    def __init__(self):
        self._client = _Client()
        self.instance_id = "instance-id"
        self.experimental_host = None


class _Database(object):
    def __init__(self, directed_read_options=None):
        self.name = "testing"
        self.database_id = "testing"
        self._nth_request = 0
        self._instance = _Instance()
        self._route_to_leader_enabled = True
        self._directed_read_options = directed_read_options

    @property
    def observability_options(self):
        return dict(db_name=self.name)

    @property
    def _next_nth_request(self):
        self._nth_request += 1
        return self._nth_request

    @property
    def _nth_client_id(self):
        return 1

    def metadata_with_request_id(
        self, nth_request, nth_attempt, prior_metadata=[], span=None
    ):
        return _metadata_with_request_id(
            self._nth_client_id,
            self._channel_id,
            nth_request,
            nth_attempt,
            prior_metadata,
            span,
        )

    def metadata_and_request_id(
        self, nth_request, nth_attempt, prior_metadata=[], span=None
    ):
        return _metadata_with_request_id_and_req_id(
            self._nth_client_id,
            self._channel_id,
            nth_request,
            nth_attempt,
            prior_metadata,
            span,
        )

    def with_error_augmentation(
        self, nth_request, nth_attempt, prior_metadata=[], span=None
    ):
        metadata, request_id = _metadata_with_request_id_and_req_id(
            self._nth_client_id,
            self._channel_id,
            nth_request,
            nth_attempt,
            prior_metadata,
            span,
        )
        return metadata, _augment_errors_with_request_id(request_id)

    @property
    def _channel_id(self):
        return 1


class _Session(object):
    def __init__(self, database=None, name=TestSnapshot.SESSION_NAME):
        self._database = database
        self.name = name

    @property
    def session_id(self):
        return self.name


class _MockIterator(object):
    def __init__(self, *values, **kw):
        self._iter_values = iter(values)
        self._fail_after = kw.pop("fail_after", False)
        self._error = kw.pop("error", Exception)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self._iter_values)
        except StopIteration:
            if self._fail_after:
                raise self._error
            raise

    next = __next__


def _build_snapshot_derived(session=None, multi_use=False, read_only=True) -> _Derived:
    """Builds and returns an instance of a minimally-
    implemented _Derived class for testing."""

    session = session or build_session()
    if session.session_id is None:
        session._session_id = "session-id"

    derived = _Derived(session=session, multi_use=multi_use)
    derived._read_only = read_only

    return derived


def _build_span_attributes(
    database: Database, attempt: int = 1, **extra_attributes
) -> Mapping[str, str]:
    """Builds the attributes for spans using the given database and extra attributes."""

    attributes = {
        "db.type": "spanner",
        "db.url": "spanner.googleapis.com",
        "db.instance": database.name,
        "net.host.name": "spanner.googleapis.com",
        "cloud.region": "global",
        "gcp.client.service": "spanner",
        "gcp.client.version": LIB_VERSION,
        "gcp.client.repo": "googleapis/python-spanner",
        "gcp.resource.name": _opentelemetry_tracing.GCP_RESOURCE_NAME_PREFIX
        + database.name,
        "x_goog_spanner_request_id": _build_request_id(database, attempt),
    }
    attributes.update(extra_attributes)
    return enrich_with_otel_scope(attributes)


def _build_request_id(database: Database, attempt: int) -> str:
    """Builds a request ID for an Spanner Client API request with the given database and attempt number."""

    client = database._instance._client
    return build_request_id(
        client_id=client._nth_client_id,
        channel_id=database._channel_id,
        nth_request=client._nth_request.value,
        attempt=attempt,
    )
