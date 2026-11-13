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

import os
import time
from unittest import mock

from google.api_core.client_options import ClientOptions
from google.auth.credentials import AnonymousCredentials
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import InMemoryMetricReader

import google.cloud.spanner_v1.client as client_mod
from google.cloud.spanner_v1 import (
    Client,
    FixedSizePool,
    KeySet,
    TypeCode,
)
from google.cloud.spanner_v1.metrics.metrics_interceptor import MetricsInterceptor
from google.cloud.spanner_v1.metrics.spanner_metrics_tracer_factory import (
    SpannerMetricsTracerFactory,
)
from google.cloud.spanner_v1.testing.mock_spanner import SpannerServicer
from tests.mockserver_tests.mock_server_test_base import (
    MockServerTestBase,
    _make_partial_result_sets,
    add_error,
    add_execute_streaming_sql_results,
    add_select1_result,
    unavailable_status,
)


class TestOperationMetricsIntegration(MockServerTestBase):
    def setUp(self):
        super().setUp()
        os.environ["SPANNER_DISABLE_BUILTIN_METRICS"] = "false"
        SpannerMetricsTracerFactory._metrics_tracer_factory = None
        client_mod._metrics_monitor_initialized = False

    def tearDown(self):
        super().tearDown()
        os.environ["SPANNER_DISABLE_BUILTIN_METRICS"] = "true"
        SpannerMetricsTracerFactory._metrics_tracer_factory = None
        client_mod._metrics_monitor_initialized = False

    def _setup_client_and_database(self):
        client = Client(
            project="p",
            credentials=AnonymousCredentials(),
            client_options=ClientOptions(
                api_endpoint="localhost:" + str(MockServerTestBase.port),
            ),
        )
        instance = client.instance("test-instance")
        database = instance.database(
            "test-database",
            pool=FixedSizePool(size=10),
            enable_interceptors_in_tests=True,
        )
        database._interceptors.append(MetricsInterceptor())
        database._spanner_api = None
        # Pre-initialize pool sessions so they don't produce metric noise during queries
        session = database._pool.get()
        database._pool.put(session)
        return client, database

    def _extract_metrics(self, reader, method=None):
        metric_data = reader.get_metrics_data()
        if not metric_data:
            return {}
        metrics = {}
        for rm in metric_data.resource_metrics:
            for sm in rm.scope_metrics:
                for metric in sm.metrics:
                    points = list(metric.data.data_points)
                    if method:
                        points = [
                            p for p in points if p.attributes.get("method") == method
                        ]
                    if points:
                        metrics[metric.name] = points
        return metrics

    def test_operation_latency_not_recorded_before_stream_consumed(self):
        fields = [("col1", TypeCode.INT64)]
        partials = _make_partial_result_sets(
            fields,
            [
                {"values": ["1"], "last": True},
            ],
        )
        add_execute_streaming_sql_results("select 1", partials)
        reader = InMemoryMetricReader()
        meter_provider = MeterProvider(metric_readers=[reader])

        with (
            mock.patch(
                "google.cloud.spanner_v1.metrics.metrics_tracer_factory.get_meter_provider",
                return_value=meter_provider,
            ),
            mock.patch(
                "google.cloud.spanner_v1.client.MeterProvider",
                return_value=meter_provider,
            ),
            mock.patch(
                "google.cloud.spanner_v1.client._get_spanner_emulator_host",
                return_value=None,
            ),
        ):
            _, database = self._setup_client_and_database()
            with database.snapshot() as snapshot:
                results = snapshot.execute_sql("select 1")

                # Verify that operational metrics for ExecuteStreamingSql have NOT been recorded yet
                metrics_before = self._extract_metrics(
                    reader, method="Spanner.ExecuteStreamingSql"
                )
                self.assertNotIn("operation_latencies", metrics_before)
                self.assertNotIn("operation_count", metrics_before)

                # Consume the results while keeping `results` alive in local scope
                rows = list(results)
                self.assertEqual(len(rows), 1)

                # Verify that operational metrics are recorded immediately upon stream completion
                # even while `results` is still alive in scope (regression test for last=True).
                metrics_after = self._extract_metrics(
                    reader, method="Spanner.ExecuteStreamingSql"
                )
                self.assertIn(
                    "operation_latencies",
                    metrics_after,
                    f"Metrics: {list(metrics_after.keys())}",
                )
                points = metrics_after["operation_latencies"]
                self.assertEqual(len(points), 1)
                self.assertEqual(points[0].count, 1)

                self.assertIn("operation_count", metrics_after)
                cnt_points = metrics_after["operation_count"]
                self.assertEqual(len(cnt_points), 1)
                self.assertEqual(cnt_points[0].value, 1)

    def test_operation_latency_measures_full_stream_duration(self):
        fields = [("col1", TypeCode.INT64)]
        results_cfg = [
            {"values": ["1"], "last": False},
            {"values": ["2"], "last": False},
            {"values": ["3"], "last": False},
        ]
        partials = _make_partial_result_sets(fields, results_cfg)
        add_execute_streaming_sql_results("select 1", partials)

        orig_get = MockServerTestBase.spanner_service.mock_spanner.get_execute_streaming_sql_results

        def delayed_get_results(sql, started_transaction):
            for msg in orig_get(sql, started_transaction):
                time.sleep(
                    0.03
                )  # 30ms server-side streaming delay per chunk (~90ms total)
                yield msg

        reader = InMemoryMetricReader()
        meter_provider = MeterProvider(metric_readers=[reader])

        with (
            mock.patch.object(
                MockServerTestBase.spanner_service.mock_spanner,
                "get_execute_streaming_sql_results",
                side_effect=delayed_get_results,
            ),
            mock.patch(
                "google.cloud.spanner_v1.metrics.metrics_tracer_factory.get_meter_provider",
                return_value=meter_provider,
            ),
            mock.patch(
                "google.cloud.spanner_v1.client.MeterProvider",
                return_value=meter_provider,
            ),
            mock.patch(
                "google.cloud.spanner_v1.client._get_spanner_emulator_host",
                return_value=None,
            ),
        ):
            _, database = self._setup_client_and_database()
            with database.snapshot() as snapshot:
                results = snapshot.execute_sql("select 1")
                rows = iter(results)
                first_row = next(rows)
                self.assertEqual(first_row, [1])

                # Since _make_partial_result_sets doesn't set resume tokens, the
                # entire stream (~90ms across 3 chunks) is buffered before the
                # first row is yielded, and operation_latencies is already recorded.
                metrics = self._extract_metrics(
                    reader, method="Spanner.ExecuteStreamingSql"
                )
                self.assertIn("operation_latencies", metrics)
                point = metrics["operation_latencies"][0]
                self.assertEqual(point.count, 1)
                self.assertGreaterEqual(point.sum, 75)
                recorded_sum = point.sum

                # Consuming the remaining rows does not record a second time
                remaining_rows = list(rows)
                self.assertEqual(remaining_rows, [[2], [3]])
                metrics_after = self._extract_metrics(
                    reader, method="Spanner.ExecuteStreamingSql"
                )
                point_after = metrics_after["operation_latencies"][0]
                self.assertEqual(point_after.count, 1)
                self.assertEqual(point_after.sum, recorded_sum)

    def test_operation_latency_last_true_and_last_false_consistency(self):
        """Verifies last=True and last=False both record operation_latencies
        before yielding buffered rows and include the full stream duration."""
        fields = [("col1", TypeCode.INT64)]
        partials_no_last = _make_partial_result_sets(
            fields,
            [
                {"values": ["1"], "last": False},
                {"values": ["2"], "last": False},
                {"values": ["3"], "last": False},
            ],
        )
        partials_with_last = _make_partial_result_sets(
            fields,
            [
                {"values": ["1"], "last": False},
                {"values": ["2"], "last": False},
                {"values": ["3"], "last": True},
            ],
        )
        add_execute_streaming_sql_results("select no_last", partials_no_last)
        add_execute_streaming_sql_results("select with_last", partials_with_last)

        orig_get = MockServerTestBase.spanner_service.mock_spanner.get_execute_streaming_sql_results

        def delayed_get_results(sql, started_transaction):
            for msg in orig_get(sql, started_transaction):
                time.sleep(0.025)  # 25ms server streaming delay per chunk (~75ms total)
                yield msg

        def run_query_and_get_latency(sql):
            SpannerMetricsTracerFactory._metrics_tracer_factory = None
            client_mod._metrics_monitor_initialized = False
            reader = InMemoryMetricReader()
            meter_provider = MeterProvider(metric_readers=[reader])
            with (
                mock.patch.object(
                    MockServerTestBase.spanner_service.mock_spanner,
                    "get_execute_streaming_sql_results",
                    side_effect=delayed_get_results,
                ),
                mock.patch(
                    "google.cloud.spanner_v1.metrics.metrics_tracer_factory.get_meter_provider",
                    return_value=meter_provider,
                ),
                mock.patch(
                    "google.cloud.spanner_v1.client.MeterProvider",
                    return_value=meter_provider,
                ),
                mock.patch(
                    "google.cloud.spanner_v1.client._get_spanner_emulator_host",
                    return_value=None,
                ),
            ):
                _, database = self._setup_client_and_database()
                with database.snapshot() as snapshot:
                    results = snapshot.execute_sql(sql)
                    rows = iter(results)
                    first_row = next(rows)
                    self.assertEqual(first_row, [1])

                    # Operation completion is recorded as soon as the stream finishes
                    # buffering, before the remaining rows are consumed.
                    metrics = self._extract_metrics(
                        reader, method="Spanner.ExecuteStreamingSql"
                    )
                    self.assertIn("operation_latencies", metrics)
                    point = metrics["operation_latencies"][0]
                    self.assertEqual(point.count, 1)
                    recorded_sum = point.sum

                    remaining_rows = list(rows)
                    self.assertEqual(remaining_rows, [[2], [3]])
                    metrics_after = self._extract_metrics(
                        reader, method="Spanner.ExecuteStreamingSql"
                    )
                    point_after = metrics_after["operation_latencies"][0]
                    self.assertEqual(point_after.count, 1)
                    self.assertEqual(point_after.sum, recorded_sum)
                    return recorded_sum

        lat_no_last = run_query_and_get_latency("select no_last")
        lat_with_last = run_query_and_get_latency("select with_last")

        # Both must reflect the ~75ms server streaming duration
        self.assertGreaterEqual(lat_no_last, 60)
        self.assertGreaterEqual(lat_with_last, 60)

    def test_operation_latency_with_retries(self):
        add_select1_result()
        add_error(SpannerServicer.ExecuteStreamingSql.__name__, unavailable_status())
        reader = InMemoryMetricReader()
        meter_provider = MeterProvider(metric_readers=[reader])

        with (
            mock.patch(
                "google.cloud.spanner_v1.metrics.metrics_tracer_factory.get_meter_provider",
                return_value=meter_provider,
            ),
            mock.patch(
                "google.cloud.spanner_v1.client.MeterProvider",
                return_value=meter_provider,
            ),
            mock.patch(
                "google.cloud.spanner_v1.client._get_spanner_emulator_host",
                return_value=None,
            ),
        ):
            _, database = self._setup_client_and_database()
            with database.snapshot() as snapshot:
                results = snapshot.execute_sql("select 1")
                rows = list(results)
                self.assertEqual(len(rows), 1)

            metrics = self._extract_metrics(
                reader, method="Spanner.ExecuteStreamingSql"
            )
            # Should record 1 logical operation but 2 attempts
            self.assertIn("operation_count", metrics)
            op_cnt_point = metrics["operation_count"][0]
            self.assertEqual(op_cnt_point.value, 1)

            self.assertIn("attempt_count", metrics)
            att_cnt_point = metrics["attempt_count"][0]
            self.assertEqual(att_cnt_point.value, 2)

            self.assertIn("operation_latencies", metrics)
            op_lat_point = metrics["operation_latencies"][0]
            self.assertEqual(op_lat_point.count, 1)

    def test_session_ping_emits_operation_metrics(self):
        add_select1_result()
        reader = InMemoryMetricReader()
        meter_provider = MeterProvider(metric_readers=[reader])

        with (
            mock.patch(
                "google.cloud.spanner_v1.metrics.metrics_tracer_factory.get_meter_provider",
                return_value=meter_provider,
            ),
            mock.patch(
                "google.cloud.spanner_v1.client.MeterProvider",
                return_value=meter_provider,
            ),
            mock.patch(
                "google.cloud.spanner_v1.client._get_spanner_emulator_host",
                return_value=None,
            ),
        ):
            _, database = self._setup_client_and_database()
            session = database._pool.get()
            try:
                session.ping()
            finally:
                database._pool.put(session)

            metrics = self._extract_metrics(reader, method="Spanner.ExecuteSql")
            self.assertIn("operation_latencies", metrics)
            self.assertEqual(metrics["operation_latencies"][0].count, 1)
            self.assertIn("operation_count", metrics)
            self.assertEqual(metrics["operation_count"][0].value, 1)

    def test_operation_latency_streaming_read(self):
        reader = InMemoryMetricReader()
        meter_provider = MeterProvider(metric_readers=[reader])

        with (
            mock.patch(
                "google.cloud.spanner_v1.metrics.metrics_tracer_factory.get_meter_provider",
                return_value=meter_provider,
            ),
            mock.patch(
                "google.cloud.spanner_v1.client.MeterProvider",
                return_value=meter_provider,
            ),
            mock.patch(
                "google.cloud.spanner_v1.client._get_spanner_emulator_host",
                return_value=None,
            ),
        ):
            _, database = self._setup_client_and_database()
            with database.snapshot() as snapshot:
                results = snapshot.read(
                    table="citizens",
                    columns=["email", "first_name"],
                    keyset=KeySet(all_=True),
                )
                # Before consumption
                metrics_before = self._extract_metrics(
                    reader, method="Spanner.StreamingRead"
                )
                self.assertNotIn("operation_latencies", metrics_before)

                # Consume
                list(results)

            metrics = self._extract_metrics(reader, method="Spanner.StreamingRead")
            self.assertIn("operation_latencies", metrics)
            op_lat_point = metrics["operation_latencies"][0]
            self.assertEqual(op_lat_point.count, 1)
