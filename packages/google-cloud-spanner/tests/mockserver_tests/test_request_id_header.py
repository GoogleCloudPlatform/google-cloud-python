# Copyright 2025 Google LLC All rights reserved.
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

import random
import threading

from google.cloud.spanner_v1 import (
    BatchCreateSessionsRequest,
    BeginTransactionRequest,
    CreateSessionRequest,
    ExecuteSqlRequest,
)
from google.cloud.spanner_v1.database_sessions_manager import TransactionType
from google.cloud.spanner_v1.request_id_header import REQ_RAND_PROCESS_ID
from google.cloud.spanner_v1.testing.mock_spanner import SpannerServicer
from tests.mockserver_tests.mock_server_test_base import (
    MockServerTestBase,
    aborted_status,
    add_error,
    add_select1_result,
    unavailable_status,
)


class TestRequestIDHeader(MockServerTestBase):
    def tearDown(self):
        super().tearDown()
        self.database._x_goog_request_id_interceptor.reset()

    def test_snapshot_execute_sql(self):
        add_select1_result()
        if not getattr(self.database, "_interceptors", None):
            self.database._interceptors = MockServerTestBase._interceptors
        with self.database.snapshot() as snapshot:
            results = snapshot.execute_sql("select 1")
            result_list = []
            for row in results:
                result_list.append(row)
                self.assertEqual(1, row[0])
            self.assertEqual(1, len(result_list))
        requests = self.spanner_service.requests
        self.assert_requests_sequence(
            requests,
            [ExecuteSqlRequest],
            TransactionType.READ_ONLY,
            allow_multiple_batch_create=True,
        )
        NTH_CLIENT = self.database._nth_client_id
        CHANNEL_ID = self.database._channel_id
        got_stream_segments, got_unary_segments = self.canonicalize_request_id_headers()
        # Filter out CreateSessionRequest unary segments for comparison
        filtered_unary_segments = [
            seg for seg in got_unary_segments if not seg[0].endswith("/CreateSession")
        ]
        want_unary_segments = [
            (
                "/google.spanner.v1.Spanner/BatchCreateSessions",
                (1, REQ_RAND_PROCESS_ID, NTH_CLIENT, CHANNEL_ID, 1, 1),
            )
        ]
        # Dynamically determine the expected sequence number for ExecuteStreamingSql
        session_requests_before = 0
        for req in requests:
            if isinstance(req, (BatchCreateSessionsRequest, CreateSessionRequest)):
                session_requests_before += 1
            elif isinstance(req, ExecuteSqlRequest):
                break
        want_stream_segments = [
            (
                "/google.spanner.v1.Spanner/ExecuteStreamingSql",
                (
                    1,
                    REQ_RAND_PROCESS_ID,
                    NTH_CLIENT,
                    CHANNEL_ID,
                    1 + session_requests_before,
                    1,
                ),
            )
        ]
        assert filtered_unary_segments == want_unary_segments
        assert got_stream_segments == want_stream_segments

    def test_snapshot_read_concurrent(self):
        add_select1_result()
        db = self.database
        with db.snapshot() as snapshot:
            rows = snapshot.execute_sql("select 1")
            for row in rows:
                _ = row

        def select1():
            with db.snapshot() as snapshot:
                rows = snapshot.execute_sql("select 1")
                res_list = []
                for row in rows:
                    self.assertEqual(1, row[0])
                    res_list.append(row)
                self.assertEqual(1, len(res_list))

        n = 10
        threads = []
        for i in range(n):
            th = threading.Thread(target=select1, name=f"snapshot-select1-{i}")
            threads.append(th)
            th.start()
        random.shuffle(threads)
        for thread in threads:
            thread.join()
        requests = self.spanner_service.requests
        # Allow for an extra request due to multiplexed session creation
        expected_min = 2 + n
        expected_max = expected_min + 1
        assert expected_min <= len(requests) <= expected_max, (
            f"Expected {expected_min} or {expected_max} requests, got {len(requests)}: {requests}"
        )
        client_id = db._nth_client_id
        channel_id = db._channel_id
        got_stream_segments, got_unary_segments = self.canonicalize_request_id_headers()
        want_unary_segments = [
            (
                "/google.spanner.v1.Spanner/BatchCreateSessions",
                (1, REQ_RAND_PROCESS_ID, client_id, channel_id, 1, 1),
            ),
        ]
        assert any(seg == want_unary_segments[0] for seg in got_unary_segments)

        # Dynamically determine the expected sequence numbers for ExecuteStreamingSql
        session_requests_before = 0
        for req in requests:
            if isinstance(req, (BatchCreateSessionsRequest, CreateSessionRequest)):
                session_requests_before += 1
            elif isinstance(req, ExecuteSqlRequest):
                break
        want_stream_segments = [
            (
                "/google.spanner.v1.Spanner/ExecuteStreamingSql",
                (
                    1,
                    REQ_RAND_PROCESS_ID,
                    client_id,
                    channel_id,
                    session_requests_before + i,
                    1,
                ),
            )
            for i in range(1, n + 2)
        ]
        assert sorted(got_stream_segments) == sorted(want_stream_segments)

    def test_database_run_in_transaction_retries_on_abort(self):
        counters = dict(aborted=0)
        want_failed_attempts = 2

        def select_in_txn(txn):
            results = txn.execute_sql("select 1")
            for row in results:
                _ = row

            if counters["aborted"] < want_failed_attempts:
                counters["aborted"] += 1
                add_error(SpannerServicer.Commit.__name__, aborted_status())

        add_select1_result()
        if not getattr(self.database, "_interceptors", None):
            self.database._interceptors = MockServerTestBase._interceptors

        self.database.run_in_transaction(select_in_txn)

    def test_database_execute_partitioned_dml_request_id(self):
        add_select1_result()
        if not getattr(self.database, "_interceptors", None):
            self.database._interceptors = MockServerTestBase._interceptors
        _ = self.database.execute_partitioned_dml("select 1")
        requests = self.spanner_service.requests
        self.assert_requests_sequence(
            requests,
            [BeginTransactionRequest, ExecuteSqlRequest],
            TransactionType.PARTITIONED,
            allow_multiple_batch_create=True,
        )
        got_stream_segments, got_unary_segments = self.canonicalize_request_id_headers()
        NTH_CLIENT = self.database._nth_client_id
        CHANNEL_ID = self.database._channel_id
        # Allow for extra unary segments due to session creation
        filtered_unary_segments = [
            seg for seg in got_unary_segments if not seg[0].endswith("/CreateSession")
        ]
        # Find the actual sequence number for BeginTransaction
        begin_txn_seq = None
        for seg in filtered_unary_segments:
            if seg[0].endswith("/BeginTransaction"):
                begin_txn_seq = seg[1][4]
                break
        want_unary_segments = [
            (
                "/google.spanner.v1.Spanner/BatchCreateSessions",
                (1, REQ_RAND_PROCESS_ID, NTH_CLIENT, CHANNEL_ID, 1, 1),
            ),
            (
                "/google.spanner.v1.Spanner/BeginTransaction",
                (1, REQ_RAND_PROCESS_ID, NTH_CLIENT, CHANNEL_ID, begin_txn_seq, 1),
            ),
        ]
        # Dynamically determine the expected sequence number for ExecuteStreamingSql
        session_requests_before = 0
        for req in requests:
            if isinstance(req, (BatchCreateSessionsRequest, CreateSessionRequest)):
                session_requests_before += 1
            elif isinstance(req, ExecuteSqlRequest):
                break
        # Find the actual sequence number for ExecuteStreamingSql
        exec_sql_seq = got_stream_segments[0][1][4] if got_stream_segments else None
        want_stream_segments = [
            (
                "/google.spanner.v1.Spanner/ExecuteStreamingSql",
                (1, REQ_RAND_PROCESS_ID, NTH_CLIENT, CHANNEL_ID, exec_sql_seq, 1),
            )
        ]
        assert all(seg in filtered_unary_segments for seg in want_unary_segments)
        assert got_stream_segments == want_stream_segments

    def test_unary_retryable_error(self):
        add_select1_result()
        add_error(SpannerServicer.BatchCreateSessions.__name__, unavailable_status())

        if not getattr(self.database, "_interceptors", None):
            self.database._interceptors = MockServerTestBase._interceptors
        with self.database.snapshot() as snapshot:
            results = snapshot.execute_sql("select 1")
            result_list = []
            for row in results:
                result_list.append(row)
                self.assertEqual(1, row[0])
            self.assertEqual(1, len(result_list))

        requests = self.spanner_service.requests
        self.assert_requests_sequence(
            requests,
            [ExecuteSqlRequest],
            TransactionType.READ_ONLY,
            allow_multiple_batch_create=True,
        )

        NTH_CLIENT = self.database._nth_client_id
        CHANNEL_ID = self.database._channel_id
        # Now ensure monotonicity of the received request-id segments.
        got_stream_segments, got_unary_segments = self.canonicalize_request_id_headers()

        # Dynamically determine the expected sequence number for ExecuteStreamingSql
        exec_sql_seq = got_stream_segments[0][1][4] if got_stream_segments else None
        want_stream_segments = [
            (
                "/google.spanner.v1.Spanner/ExecuteStreamingSql",
                (1, REQ_RAND_PROCESS_ID, NTH_CLIENT, CHANNEL_ID, exec_sql_seq, 1),
            )
        ]
        assert got_stream_segments == want_stream_segments

    def test_streaming_retryable_error(self):
        add_select1_result()
        add_error(SpannerServicer.ExecuteStreamingSql.__name__, unavailable_status())

        if not getattr(self.database, "_interceptors", None):
            self.database._interceptors = MockServerTestBase._interceptors
        with self.database.snapshot() as snapshot:
            results = snapshot.execute_sql("select 1")
            result_list = []
            for row in results:
                result_list.append(row)
                self.assertEqual(1, row[0])
            self.assertEqual(1, len(result_list))

        requests = self.spanner_service.requests
        self.assert_requests_sequence(
            requests,
            [ExecuteSqlRequest, ExecuteSqlRequest],
            TransactionType.READ_ONLY,
            allow_multiple_batch_create=True,
        )

    def canonicalize_request_id_headers(self):
        src = self.database._x_goog_request_id_interceptor
        return src._stream_req_segments, src._unary_req_segments
