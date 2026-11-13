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

import asyncio
import gc
import os
from contextlib import contextmanager
from unittest import mock

import grpc
from google.api_core.client_options import ClientOptions
from google.auth.credentials import AnonymousCredentials
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import InMemoryMetricReader
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.sdk.trace.export.in_memory_span_exporter import InMemorySpanExporter
from opentelemetry.trace.status import StatusCode

import google.cloud.spanner_v1._async.client as async_client_mod
import google.cloud.spanner_v1.client as client_mod
from google.cloud.spanner_v1 import (
    Client,
    PartialResultSet,
    ResultSetMetadata,
    StructType,
    Type,
    TypeCode,
    _helpers,
)
from google.cloud.spanner_v1._async.client import Client as AsyncClient
from google.cloud.spanner_v1._async.pool import FixedSizePool as AsyncFixedSizePool
from google.cloud.spanner_v1._helpers import _make_value_pb
from google.cloud.spanner_v1.metrics.metrics_interceptor import MetricsInterceptor
from google.cloud.spanner_v1.metrics.spanner_metrics_tracer_factory import (
    SpannerMetricsTracerFactory,
)
from google.cloud.spanner_v1.pool import FixedSizePool
from google.cloud.spanner_v1.services.spanner.async_client import SpannerAsyncClient
from google.cloud.spanner_v1.services.spanner.transports.grpc_asyncio import (
    SpannerGrpcAsyncIOTransport,
)
from tests.mockserver_tests.mock_server_test_base import (
    AsyncMockServerTestBase,
    MockServerTestBase,
    add_execute_streaming_sql_results,
    add_header,
    add_select1_result,
)

_SPANNER_METRIC_NAMES = {
    "attempt_latencies",
    "operation_latencies",
    "attempt_count",
    "operation_count",
    "gfe_latencies",
    "afe_latencies",
    "gfe_connectivity_error_count",
    "afe_connectivity_error_count",
}


class TestFrontendMetricsIntegration(MockServerTestBase):
    def setUp(self):
        super().setUp()
        self._orig_disable_builtin_metrics = os.environ.get(
            "SPANNER_DISABLE_BUILTIN_METRICS"
        )
        self._orig_disable_afe_server_timing = os.environ.get(
            "SPANNER_DISABLE_AFE_SERVER_TIMING"
        )
        self._orig_enable_afe_server_timing = _helpers.ENABLE_AFE_SERVER_TIMING

        os.environ["SPANNER_DISABLE_BUILTIN_METRICS"] = "false"
        os.environ["SPANNER_DISABLE_AFE_SERVER_TIMING"] = "false"
        _helpers.ENABLE_AFE_SERVER_TIMING = True
        SpannerMetricsTracerFactory._metrics_tracer_factory = None
        client_mod._metrics_monitor_initialized = False
        async_client_mod._metrics_monitor_initialized = False

    def tearDown(self):
        super().tearDown()
        if self._orig_disable_builtin_metrics is None:
            os.environ.pop("SPANNER_DISABLE_BUILTIN_METRICS", None)
        else:
            os.environ["SPANNER_DISABLE_BUILTIN_METRICS"] = (
                self._orig_disable_builtin_metrics
            )

        if self._orig_disable_afe_server_timing is None:
            os.environ.pop("SPANNER_DISABLE_AFE_SERVER_TIMING", None)
        else:
            os.environ["SPANNER_DISABLE_AFE_SERVER_TIMING"] = (
                self._orig_disable_afe_server_timing
            )

        _helpers.ENABLE_AFE_SERVER_TIMING = self._orig_enable_afe_server_timing
        SpannerMetricsTracerFactory._metrics_tracer_factory = None
        client_mod._metrics_monitor_initialized = False
        async_client_mod._metrics_monitor_initialized = False

    def test_gfe_metrics_exported(self):
        add_select1_result()
        add_header(
            "ExecuteStreamingSql",
            "server-timing",
            "gfet4t7; dur=55, afe; dur=23",
        )
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
            database._spanner_api = None  # Force recreation with the new interceptor

            with database.snapshot() as snapshot:
                results = snapshot.execute_sql("select 1")
                # Consume the streaming results to complete the stream
                list(results)

        metric_data = reader.get_metrics_data()
        self.assertIsNotNone(metric_data)
        metrics = {
            metric.name: metric
            for rm in metric_data.resource_metrics
            for sm in rm.scope_metrics
            for metric in sm.metrics
        }

        self.assertIn("gfe_latencies", metrics, f"Metrics: {list(metrics.keys())}")
        gfe_metric = metrics["gfe_latencies"]
        point = next(iter(gfe_metric.data.data_points))
        self.assertEqual(point.sum, 55)

        self.assertIn("afe_latencies", metrics, f"Metrics: {list(metrics.keys())}")
        afe_metric = metrics["afe_latencies"]
        point = next(iter(afe_metric.data.data_points))
        self.assertEqual(point.sum, 23)

    def test_gfe_missing_header_count_exported(self):
        add_select1_result()
        reader = InMemoryMetricReader()
        meter_provider = MeterProvider(metric_readers=[reader])

        try:
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
                database._spanner_api = (
                    None  # Force recreation with the new interceptor
                )

                with database.snapshot() as snapshot:
                    results = snapshot.execute_sql("select 1")
                    list(results)

            metric_data = reader.get_metrics_data()
            self.assertIsNotNone(metric_data)
            metrics = {
                metric.name: metric
                for rm in metric_data.resource_metrics
                for sm in rm.scope_metrics
                for metric in sm.metrics
            }

            self.assertIn(
                "gfe_connectivity_error_count",
                metrics,
                f"Metrics: {list(metrics.keys())}",
            )
            missing_metric = metrics["gfe_connectivity_error_count"]
            point = next(iter(missing_metric.data.data_points))
            self.assertGreaterEqual(point.value, 1)

            self.assertIn(
                "afe_connectivity_error_count",
                metrics,
                f"Metrics: {list(metrics.keys())}",
            )
            afe_missing_metric = metrics["afe_connectivity_error_count"]
            afe_point = next(iter(afe_missing_metric.data.data_points))
            self.assertGreaterEqual(afe_point.value, 1)
        finally:
            pass

    def test_operation_metrics_no_duplicates(self):
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
            database._spanner_api = None  # Force recreation with the new interceptor

            with database.snapshot() as snapshot:
                results = snapshot.execute_sql("select 1")
                list(results)

        metric_data = reader.get_metrics_data()
        self.assertIsNotNone(metric_data)
        metrics = {
            metric.name: metric
            for resource_metric in metric_data.resource_metrics
            for scope_metric in resource_metric.scope_metrics
            for metric in scope_metric.metrics
        }

        self.assertIn("operation_count", metrics)
        self.assertIn("operation_latencies", metrics)

        operation_count_metric = metrics["operation_count"]
        streaming_points = [
            point
            for point in operation_count_metric.data.data_points
            if point.attributes.get("method") == "Spanner.ExecuteStreamingSql"
        ]
        self.assertEqual(
            len(streaming_points),
            1,
            f"Expected exactly 1 ExecuteStreamingSql data point, found {len(streaming_points)}",
        )
        self.assertEqual(streaming_points[0].value, 1)
        self.assertEqual(streaming_points[0].attributes.get("project_id"), "p")
        self.assertEqual(
            streaming_points[0].attributes.get("instance_id"), "test-instance"
        )
        self.assertEqual(
            streaming_points[0].attributes.get("database"), "test-database"
        )

        for point in operation_count_metric.data.data_points:
            self.assertEqual(point.attributes.get("project_id"), "p")
            self.assertEqual(point.attributes.get("instance_id"), "test-instance")
            self.assertEqual(point.attributes.get("database"), "test-database")

        operation_latencies_metric = metrics["operation_latencies"]
        streaming_latency_points = [
            point
            for point in operation_latencies_metric.data.data_points
            if point.attributes.get("method") == "Spanner.ExecuteStreamingSql"
        ]
        self.assertEqual(
            len(streaming_latency_points),
            1,
            f"Expected exactly 1 ExecuteStreamingSql latency point, found {len(streaming_latency_points)}",
        )
        self.assertEqual(streaming_latency_points[0].count, 1)
        self.assertEqual(streaming_latency_points[0].attributes.get("project_id"), "p")
        self.assertEqual(
            streaming_latency_points[0].attributes.get("instance_id"), "test-instance"
        )
        self.assertEqual(
            streaming_latency_points[0].attributes.get("database"), "test-database"
        )

    def test_operation_metrics_disabled_no_metrics_exported(self):
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
            SpannerMetricsTracerFactory(enabled=False)
            try:
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

                with database.snapshot() as snapshot:
                    results = snapshot.execute_sql("select 1")
                    rows = list(results)
                    self.assertEqual(len(rows), 1)
            finally:
                SpannerMetricsTracerFactory(enabled=True)

        metric_data = reader.get_metrics_data()
        if metric_data is not None:
            metrics = {
                metric.name: metric
                for resource_metric in metric_data.resource_metrics
                for scope_metric in resource_metric.scope_metrics
                for metric in scope_metric.metrics
            }
            if "operation_count" in metrics:
                self.assertEqual(len(metrics["operation_count"].data.data_points), 0)
            if "operation_latencies" in metrics:
                self.assertEqual(
                    len(metrics["operation_latencies"].data.data_points), 0
                )

    def test_operation_metrics_completion_error_does_not_fail_query(self):
        from google.cloud.spanner_v1.metrics.metrics_tracer import MetricsTracer

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
            mock.patch.object(
                MetricsTracer,
                "record_operation_completion",
                side_effect=RuntimeError("telemetry export error"),
            ),
        ):
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

            with database.snapshot() as snapshot:
                results = snapshot.execute_sql("select 1")
                rows = list(results)
                self.assertEqual(len(rows), 1)

    @contextmanager
    def _mock_metrics_environment(self, meter_provider):
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
            yield

    def _create_client_and_database(self, tracer_provider=None):
        client = Client(
            project="p",
            credentials=AnonymousCredentials(),
            client_options=ClientOptions(
                api_endpoint="localhost:" + str(MockServerTestBase.port),
            ),
            observability_options=(
                dict(tracer_provider=tracer_provider) if tracer_provider else None
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
        return client, database

    def test_sync_query_happy_path_status_ok_and_spans(self):
        add_select1_result()
        reader = InMemoryMetricReader()
        meter_provider = MeterProvider(metric_readers=[reader])
        span_exporter = InMemorySpanExporter()
        tracer_provider = TracerProvider()
        tracer_provider.add_span_processor(SimpleSpanProcessor(span_exporter))

        with self._mock_metrics_environment(meter_provider):
            client, database = self._create_client_and_database(
                tracer_provider=tracer_provider
            )

            with database.snapshot() as snapshot:
                results = snapshot.execute_sql("select 1")
                rows = list(results)
                self.assertEqual(len(rows), 1)

            # Deleting results and snapshot afterwards should not change status to CANCELLED
            del results
            del snapshot
            gc.collect()

        metric_data = reader.get_metrics_data()
        self.assertIsNotNone(metric_data)
        metrics = {
            metric.name: metric
            for resource_metric in metric_data.resource_metrics
            for scope_metric in resource_metric.scope_metrics
            for metric in scope_metric.metrics
        }
        self.assertIn("attempt_latencies", metrics)
        attempt_latencies_metric = metrics["attempt_latencies"]
        streaming_points = [
            point
            for point in attempt_latencies_metric.data.data_points
            if point.attributes.get("method") == "Spanner.ExecuteStreamingSql"
        ]
        self.assertEqual(len(streaming_points), 1)
        self.assertEqual(streaming_points[0].attributes.get("status"), "OK")

        spans = span_exporter.get_finished_spans()
        query_spans = [
            span for span in spans if span.name == "CloudSpanner.Snapshot.execute_sql"
        ]
        self.assertEqual(len(query_spans), 1)
        self.assertEqual(query_spans[0].status.status_code, StatusCode.OK)

    def test_sync_query_cancelled_during_iteration(self):
        partial_result_set_1 = PartialResultSet()
        partial_result_set_1.metadata = ResultSetMetadata(
            row_type=StructType(
                fields=[
                    StructType.Field(name="ID", type_=Type(code=TypeCode.INT64)),
                ]
            )
        )
        partial_result_set_1.values.append(_make_value_pb(1))
        partial_result_set_1.resume_token = b"token_1"

        partial_result_set_2 = PartialResultSet()
        partial_result_set_2.values.append(_make_value_pb(2))
        partial_result_set_2.last = True

        sql = "select id from my_table"
        add_execute_streaming_sql_results(
            sql, [partial_result_set_1, partial_result_set_2]
        )

        reader = InMemoryMetricReader()
        meter_provider = MeterProvider(metric_readers=[reader])

        with self._mock_metrics_environment(meter_provider):
            client, database = self._create_client_and_database()

            with database.snapshot() as snapshot:
                results = snapshot.execute_sql(sql)
                row_iterator = iter(results)
                first_row = next(row_iterator)
                self.assertEqual(first_row[0], 1)
                # Caller cancels/closes generator before stream is exhausted
                results._response_iterator.close()

        metric_data = reader.get_metrics_data()
        self.assertIsNotNone(metric_data)
        metrics = {
            metric.name: metric
            for resource_metric in metric_data.resource_metrics
            for scope_metric in resource_metric.scope_metrics
            for metric in scope_metric.metrics
        }
        self.assertIn("attempt_latencies", metrics)
        attempt_latencies_metric = metrics["attempt_latencies"]
        streaming_points = [
            point
            for point in attempt_latencies_metric.data.data_points
            if point.attributes.get("method") == "Spanner.ExecuteStreamingSql"
        ]
        self.assertEqual(len(streaming_points), 1)
        self.assertEqual(streaming_points[0].attributes.get("status"), "CANCELLED")

    def test_sync_query_garbage_collected_during_iteration(self):
        partial_result_set_1 = PartialResultSet()
        partial_result_set_1.metadata = ResultSetMetadata(
            row_type=StructType(
                fields=[
                    StructType.Field(name="ID", type_=Type(code=TypeCode.INT64)),
                ]
            )
        )
        partial_result_set_1.values.append(_make_value_pb(1))
        partial_result_set_1.resume_token = b"token_1"

        partial_result_set_2 = PartialResultSet()
        partial_result_set_2.values.append(_make_value_pb(2))
        partial_result_set_2.last = True

        sql = "select id from my_table"
        add_execute_streaming_sql_results(
            sql, [partial_result_set_1, partial_result_set_2]
        )

        reader = InMemoryMetricReader()
        meter_provider = MeterProvider(metric_readers=[reader])

        with self._mock_metrics_environment(meter_provider):
            client, database = self._create_client_and_database()

            with database.snapshot() as snapshot:
                results = snapshot.execute_sql(sql)
                row_iterator = iter(results)
                first_row = next(row_iterator)
                self.assertEqual(first_row[0], 1)
                # Abandon stream without exhausting it
                del row_iterator
                del results
                gc.collect()

        metric_data = reader.get_metrics_data()
        self.assertIsNotNone(metric_data)
        metrics = {
            metric.name: metric
            for resource_metric in metric_data.resource_metrics
            for scope_metric in resource_metric.scope_metrics
            for metric in scope_metric.metrics
        }
        self.assertIn("attempt_latencies", metrics)
        attempt_latencies_metric = metrics["attempt_latencies"]
        streaming_points = [
            point
            for point in attempt_latencies_metric.data.data_points
            if point.attributes.get("method") == "Spanner.ExecuteStreamingSql"
        ]
        self.assertEqual(len(streaming_points), 1)
        self.assertEqual(streaming_points[0].attributes.get("status"), "CANCELLED")

    def test_sync_metrics_disabled(self):
        add_select1_result()
        try:
            os.environ["SPANNER_DISABLE_BUILTIN_METRICS"] = "true"
            SpannerMetricsTracerFactory._metrics_tracer_factory = None
            client_mod._metrics_monitor_initialized = False

            reader = InMemoryMetricReader()
            meter_provider = MeterProvider(metric_readers=[reader])

            with self._mock_metrics_environment(meter_provider):
                client, database = self._create_client_and_database()

                with database.snapshot() as snapshot:
                    results = snapshot.execute_sql("select 1")
                    rows = list(results)
                    self.assertEqual(len(rows), 1)

            metric_data = reader.get_metrics_data()
            if metric_data is not None:
                recorded_metric_names = {
                    metric.name
                    for resource_metric in metric_data.resource_metrics
                    for scope_metric in resource_metric.scope_metrics
                    for metric in scope_metric.metrics
                }
                intersection = recorded_metric_names & _SPANNER_METRIC_NAMES
                self.assertEqual(
                    len(intersection),
                    0,
                    f"Metrics should not be recorded when disabled, found: {intersection}",
                )
        finally:
            os.environ["SPANNER_DISABLE_BUILTIN_METRICS"] = "false"
            SpannerMetricsTracerFactory._metrics_tracer_factory = None
            client_mod._metrics_monitor_initialized = False

    def test_sync_unary_happy_path(self):
        reader = InMemoryMetricReader()
        meter_provider = MeterProvider(metric_readers=[reader])

        with self._mock_metrics_environment(meter_provider):
            client, database = self._create_client_and_database()
            session = database.session()
            session.create()

        metric_data = reader.get_metrics_data()
        self.assertIsNotNone(metric_data)
        metrics = {
            metric.name: metric
            for resource_metric in metric_data.resource_metrics
            for scope_metric in resource_metric.scope_metrics
            for metric in scope_metric.metrics
        }
        self.assertIn("attempt_latencies", metrics)
        attempt_latencies_metric = metrics["attempt_latencies"]
        session_points = [
            point
            for point in attempt_latencies_metric.data.data_points
            if point.attributes.get("method") == "Spanner.CreateSession"
        ]
        self.assertTrue(len(session_points) > 0)
        self.assertEqual(session_points[0].attributes.get("status"), "OK")

    def test_sync_server_timing_regex_boundary_safe_from_false_positives(self):
        add_select1_result()
        add_header(
            "ExecuteStreamingSql",
            "server-timing",
            "safe; dur=99, x-gfet4t7; dur=88, afe; dur=23, gfet4t7; dur=55",
        )
        reader = InMemoryMetricReader()
        meter_provider = MeterProvider(metric_readers=[reader])

        with self._mock_metrics_environment(meter_provider):
            client, database = self._create_client_and_database()
            with database.snapshot() as snapshot:
                results = snapshot.execute_sql("select 1")
                list(results)

        metric_data = reader.get_metrics_data()
        self.assertIsNotNone(metric_data)
        metrics = {
            metric.name: metric
            for resource_metric in metric_data.resource_metrics
            for scope_metric in resource_metric.scope_metrics
            for metric in scope_metric.metrics
        }
        self.assertIn("gfe_latencies", metrics)
        self.assertIn("afe_latencies", metrics)
        gfe_point = next(iter(metrics["gfe_latencies"].data.data_points))
        afe_point = next(iter(metrics["afe_latencies"].data.data_points))
        self.assertEqual(gfe_point.sum, 55)
        self.assertEqual(afe_point.sum, 23)

    def test_sync_streaming_read_metrics(self):
        from google.cloud.spanner_v1.keyset import KeySet

        add_header(
            "StreamingRead",
            "server-timing",
            "gfet4t7; dur=40, afe; dur=15",
        )
        reader = InMemoryMetricReader()
        meter_provider = MeterProvider(metric_readers=[reader])

        with self._mock_metrics_environment(meter_provider):
            client, database = self._create_client_and_database()
            with database.snapshot() as snapshot:
                results = snapshot.read(
                    table="my_table",
                    columns=["id"],
                    keyset=KeySet(all_=True),
                )
                list(results)

        metric_data = reader.get_metrics_data()
        self.assertIsNotNone(metric_data)
        metrics = {
            metric.name: metric
            for resource_metric in metric_data.resource_metrics
            for scope_metric in resource_metric.scope_metrics
            for metric in scope_metric.metrics
        }
        self.assertIn("gfe_latencies", metrics)
        self.assertIn("afe_latencies", metrics)
        self.assertIn("attempt_latencies", metrics)
        streaming_points = [
            point
            for point in metrics["attempt_latencies"].data.data_points
            if point.attributes.get("method") == "Spanner.StreamingRead"
        ]
        self.assertEqual(len(streaming_points), 1)
        self.assertEqual(streaming_points[0].attributes.get("status"), "OK")


class TestFrontendMetricsAsyncIntegration(AsyncMockServerTestBase):
    def setUp(self):
        super().setUp()
        self._orig_disable_builtin_metrics = os.environ.get(
            "SPANNER_DISABLE_BUILTIN_METRICS"
        )
        self._orig_disable_afe_server_timing = os.environ.get(
            "SPANNER_DISABLE_AFE_SERVER_TIMING"
        )
        self._orig_enable_afe_server_timing = _helpers.ENABLE_AFE_SERVER_TIMING

        os.environ["SPANNER_DISABLE_BUILTIN_METRICS"] = "false"
        os.environ["SPANNER_DISABLE_AFE_SERVER_TIMING"] = "false"
        _helpers.ENABLE_AFE_SERVER_TIMING = True
        SpannerMetricsTracerFactory._metrics_tracer_factory = None
        client_mod._metrics_monitor_initialized = False
        async_client_mod._metrics_monitor_initialized = False

    def tearDown(self):
        super().tearDown()
        if self._orig_disable_builtin_metrics is None:
            os.environ.pop("SPANNER_DISABLE_BUILTIN_METRICS", None)
        else:
            os.environ["SPANNER_DISABLE_BUILTIN_METRICS"] = (
                self._orig_disable_builtin_metrics
            )

        if self._orig_disable_afe_server_timing is None:
            os.environ.pop("SPANNER_DISABLE_AFE_SERVER_TIMING", None)
        else:
            os.environ["SPANNER_DISABLE_AFE_SERVER_TIMING"] = (
                self._orig_disable_afe_server_timing
            )

        _helpers.ENABLE_AFE_SERVER_TIMING = self._orig_enable_afe_server_timing
        SpannerMetricsTracerFactory._metrics_tracer_factory = None
        client_mod._metrics_monitor_initialized = False
        async_client_mod._metrics_monitor_initialized = False

    async def asyncSetUp(self):
        await super().asyncSetUp()
        if AsyncMockServerTestBase.spanner_service:
            AsyncMockServerTestBase.spanner_service.clear_results()

    async def asyncTearDown(self):
        await super().asyncTearDown()
        if AsyncMockServerTestBase.spanner_service:
            AsyncMockServerTestBase.spanner_service.clear_results()

    async def test_async_gfe_metrics_exported(self):
        add_select1_result()
        add_header(
            "ExecuteStreamingSql",
            "server-timing",
            "gfet4t7; dur=55, afe; dur=23",
        )
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
                "google.cloud.spanner_v1._async.client.MeterProvider",
                return_value=meter_provider,
            ),
            mock.patch(
                "google.cloud.spanner_v1.client._get_spanner_emulator_host",
                return_value=None,
            ),
            mock.patch(
                "google.cloud.spanner_v1._async.client._get_spanner_emulator_host",
                return_value=None,
            ),
        ):
            client = AsyncClient(
                project="p",
                credentials=AnonymousCredentials(),
                client_options=ClientOptions(
                    api_endpoint="localhost:" + str(AsyncMockServerTestBase.port),
                ),
            )
            instance = client.instance("test-instance")
            database = await instance.database(
                "test-database",
                pool=AsyncFixedSizePool(size=10),
            )
            async with grpc.aio.insecure_channel(
                "localhost:" + str(AsyncMockServerTestBase.port),
            ) as channel:
                transport = SpannerGrpcAsyncIOTransport(
                    channel=channel,
                    metrics_interceptor=MetricsInterceptor(),
                )
                database._spanner_api = SpannerAsyncClient(
                    client_info=client._client_info,
                    transport=transport,
                )

                async with database.snapshot() as snapshot:
                    results = await snapshot.execute_sql("select 1")
                    # Consume the async streaming results to complete the stream
                    async for _ in results:
                        pass

        metric_data = reader.get_metrics_data()
        self.assertIsNotNone(metric_data)
        metrics = {
            metric.name: metric
            for resource_metric in metric_data.resource_metrics
            for scope_metric in resource_metric.scope_metrics
            for metric in scope_metric.metrics
        }

        self.assertIn("gfe_latencies", metrics, f"Metrics: {list(metrics.keys())}")
        gfe_metric = metrics["gfe_latencies"]
        gfe_point = next(iter(gfe_metric.data.data_points))
        self.assertEqual(gfe_point.sum, 55)

        self.assertIn("afe_latencies", metrics, f"Metrics: {list(metrics.keys())}")
        afe_metric = metrics["afe_latencies"]
        afe_point = next(iter(afe_metric.data.data_points))
        self.assertEqual(afe_point.sum, 23)

        self.assertIn("attempt_latencies", metrics, f"Metrics: {list(metrics.keys())}")
        attempt_latencies_metric = metrics["attempt_latencies"]
        streaming_points = [
            point
            for point in attempt_latencies_metric.data.data_points
            if point.attributes.get("method") == "Spanner.ExecuteStreamingSql"
        ]
        self.assertTrue(len(streaming_points) > 0)
        self.assertEqual(streaming_points[0].attributes.get("status"), "OK")

    async def test_async_gfe_missing_header_count_exported(self):
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
                "google.cloud.spanner_v1._async.client.MeterProvider",
                return_value=meter_provider,
            ),
            mock.patch(
                "google.cloud.spanner_v1.client._get_spanner_emulator_host",
                return_value=None,
            ),
            mock.patch(
                "google.cloud.spanner_v1._async.client._get_spanner_emulator_host",
                return_value=None,
            ),
        ):
            client = AsyncClient(
                project="p",
                credentials=AnonymousCredentials(),
                client_options=ClientOptions(
                    api_endpoint="localhost:" + str(AsyncMockServerTestBase.port),
                ),
            )
            instance = client.instance("test-instance")
            database = await instance.database(
                "test-database",
                pool=AsyncFixedSizePool(size=10),
            )
            async with grpc.aio.insecure_channel(
                "localhost:" + str(AsyncMockServerTestBase.port),
            ) as channel:
                transport = SpannerGrpcAsyncIOTransport(
                    channel=channel,
                    metrics_interceptor=MetricsInterceptor(),
                )
                database._spanner_api = SpannerAsyncClient(
                    client_info=client._client_info,
                    transport=transport,
                )

                async with database.snapshot() as snapshot:
                    results = await snapshot.execute_sql("select 1")
                    async for _ in results:
                        pass

        metric_data = reader.get_metrics_data()
        self.assertIsNotNone(metric_data)
        metrics = {
            metric.name: metric
            for resource_metric in metric_data.resource_metrics
            for scope_metric in resource_metric.scope_metrics
            for metric in scope_metric.metrics
        }

        self.assertIn(
            "gfe_connectivity_error_count",
            metrics,
            f"Metrics: {list(metrics.keys())}",
        )
        missing_metric = metrics["gfe_connectivity_error_count"]
        streaming_points = [
            point
            for point in missing_metric.data.data_points
            if point.attributes.get("method") == "Spanner.ExecuteStreamingSql"
        ]
        self.assertTrue(len(streaming_points) > 0)
        self.assertGreaterEqual(streaming_points[0].value, 1)

        self.assertIn(
            "afe_connectivity_error_count",
            metrics,
            f"Metrics: {list(metrics.keys())}",
        )
        afe_missing_metric = metrics["afe_connectivity_error_count"]
        streaming_points = [
            point
            for point in afe_missing_metric.data.data_points
            if point.attributes.get("method") == "Spanner.ExecuteStreamingSql"
        ]
        self.assertTrue(len(streaming_points) > 0)
        self.assertGreaterEqual(streaming_points[0].value, 1)

    async def test_async_operation_metrics_no_duplicates(self):
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
                "google.cloud.spanner_v1._async.client.MeterProvider",
                return_value=meter_provider,
            ),
            mock.patch(
                "google.cloud.spanner_v1.client._get_spanner_emulator_host",
                return_value=None,
            ),
            mock.patch(
                "google.cloud.spanner_v1._async.client._get_spanner_emulator_host",
                return_value=None,
            ),
        ):
            client = AsyncClient(
                project="p",
                credentials=AnonymousCredentials(),
                client_options=ClientOptions(
                    api_endpoint="localhost:" + str(AsyncMockServerTestBase.port),
                ),
            )
            instance = client.instance("test-instance")
            database = await instance.database(
                "test-database",
                pool=AsyncFixedSizePool(size=10),
            )
            async with grpc.aio.insecure_channel(
                "localhost:" + str(AsyncMockServerTestBase.port),
            ) as channel:
                transport = SpannerGrpcAsyncIOTransport(
                    channel=channel,
                    metrics_interceptor=MetricsInterceptor(),
                )
                database._spanner_api = SpannerAsyncClient(
                    client_info=client._client_info,
                    transport=transport,
                )

                async with database.snapshot() as snapshot:
                    results = await snapshot.execute_sql("select 1")
                    async for _ in results:
                        pass

        metric_data = reader.get_metrics_data()
        self.assertIsNotNone(metric_data)
        metrics = {
            metric.name: metric
            for resource_metric in metric_data.resource_metrics
            for scope_metric in resource_metric.scope_metrics
            for metric in scope_metric.metrics
        }

        self.assertIn("operation_count", metrics)
        self.assertIn("operation_latencies", metrics)

        operation_count_metric = metrics["operation_count"]
        streaming_points = [
            point
            for point in operation_count_metric.data.data_points
            if point.attributes.get("method") == "Spanner.ExecuteStreamingSql"
        ]
        self.assertEqual(
            len(streaming_points),
            1,
            f"Expected exactly 1 ExecuteStreamingSql data point, found {len(streaming_points)}",
        )
        self.assertEqual(streaming_points[0].value, 1)
        self.assertEqual(streaming_points[0].attributes.get("project_id"), "p")
        self.assertEqual(
            streaming_points[0].attributes.get("instance_id"), "test-instance"
        )
        self.assertEqual(
            streaming_points[0].attributes.get("database"), "test-database"
        )

        for point in operation_count_metric.data.data_points:
            self.assertEqual(point.attributes.get("project_id"), "p")
            self.assertEqual(point.attributes.get("instance_id"), "test-instance")
            self.assertEqual(point.attributes.get("database"), "test-database")

        operation_latencies_metric = metrics["operation_latencies"]
        streaming_latency_points = [
            point
            for point in operation_latencies_metric.data.data_points
            if point.attributes.get("method") == "Spanner.ExecuteStreamingSql"
        ]
        self.assertEqual(
            len(streaming_latency_points),
            1,
            f"Expected exactly 1 ExecuteStreamingSql latency point, found {len(streaming_latency_points)}",
        )
        self.assertEqual(streaming_latency_points[0].count, 1)
        self.assertEqual(streaming_latency_points[0].attributes.get("project_id"), "p")
        self.assertEqual(
            streaming_latency_points[0].attributes.get("instance_id"), "test-instance"
        )
        self.assertEqual(
            streaming_latency_points[0].attributes.get("database"), "test-database"
        )

    async def test_async_operation_metrics_disabled_no_metrics_exported(self):
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
                "google.cloud.spanner_v1._async.client.MeterProvider",
                return_value=meter_provider,
            ),
            mock.patch(
                "google.cloud.spanner_v1.client._get_spanner_emulator_host",
                return_value=None,
            ),
            mock.patch(
                "google.cloud.spanner_v1._async.client._get_spanner_emulator_host",
                return_value=None,
            ),
        ):
            SpannerMetricsTracerFactory(enabled=False)
            try:
                client = AsyncClient(
                    project="p",
                    credentials=AnonymousCredentials(),
                    client_options=ClientOptions(
                        api_endpoint="localhost:" + str(AsyncMockServerTestBase.port),
                    ),
                )
                instance = client.instance("test-instance")
                database = await instance.database(
                    "test-database",
                    pool=AsyncFixedSizePool(size=10),
                )
                async with grpc.aio.insecure_channel(
                    "localhost:" + str(AsyncMockServerTestBase.port),
                ) as channel:
                    transport = SpannerGrpcAsyncIOTransport(
                        channel=channel,
                        metrics_interceptor=MetricsInterceptor(),
                    )
                    database._spanner_api = SpannerAsyncClient(
                        client_info=client._client_info,
                        transport=transport,
                    )

                    async with database.snapshot() as snapshot:
                        results = await snapshot.execute_sql("select 1")
                        async for _ in results:
                            pass
            finally:
                SpannerMetricsTracerFactory(enabled=True)

        metric_data = reader.get_metrics_data()
        if metric_data is not None:
            metrics = {
                metric.name: metric
                for resource_metric in metric_data.resource_metrics
                for scope_metric in resource_metric.scope_metrics
                for metric in scope_metric.metrics
            }
            if "operation_count" in metrics:
                self.assertEqual(len(metrics["operation_count"].data.data_points), 0)
            if "operation_latencies" in metrics:
                self.assertEqual(
                    len(metrics["operation_latencies"].data.data_points), 0
                )

    async def test_async_operation_metrics_completion_error_does_not_fail_query(self):
        from google.cloud.spanner_v1.metrics.metrics_tracer import MetricsTracer

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
                "google.cloud.spanner_v1._async.client.MeterProvider",
                return_value=meter_provider,
            ),
            mock.patch(
                "google.cloud.spanner_v1.client._get_spanner_emulator_host",
                return_value=None,
            ),
            mock.patch(
                "google.cloud.spanner_v1._async.client._get_spanner_emulator_host",
                return_value=None,
            ),
            mock.patch.object(
                MetricsTracer,
                "record_operation_completion",
                side_effect=RuntimeError("telemetry export error"),
            ),
        ):
            client = AsyncClient(
                project="p",
                credentials=AnonymousCredentials(),
                client_options=ClientOptions(
                    api_endpoint="localhost:" + str(AsyncMockServerTestBase.port),
                ),
            )
            instance = client.instance("test-instance")
            database = await instance.database(
                "test-database",
                pool=AsyncFixedSizePool(size=10),
            )
            async with grpc.aio.insecure_channel(
                "localhost:" + str(AsyncMockServerTestBase.port),
            ) as channel:
                transport = SpannerGrpcAsyncIOTransport(
                    channel=channel,
                    metrics_interceptor=MetricsInterceptor(),
                )
                database._spanner_api = SpannerAsyncClient(
                    client_info=client._client_info,
                    transport=transport,
                )

                async with database.snapshot() as snapshot:
                    results = await snapshot.execute_sql("select 1")
                    async for _ in results:
                        pass

    @contextmanager
    def _mock_async_metrics_environment(self, meter_provider):
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
                "google.cloud.spanner_v1._async.client.MeterProvider",
                return_value=meter_provider,
            ),
            mock.patch(
                "google.cloud.spanner_v1.client._get_spanner_emulator_host",
                return_value=None,
            ),
            mock.patch(
                "google.cloud.spanner_v1._async.client._get_spanner_emulator_host",
                return_value=None,
            ),
        ):
            yield

    async def _create_async_client_and_database(self, tracer_provider=None):
        client = AsyncClient(
            project="p",
            credentials=AnonymousCredentials(),
            client_options=ClientOptions(
                api_endpoint="localhost:" + str(AsyncMockServerTestBase.port),
            ),
            observability_options=(
                dict(tracer_provider=tracer_provider) if tracer_provider else None
            ),
        )
        instance = client.instance("test-instance")
        database = await instance.database(
            "test-database",
            pool=AsyncFixedSizePool(size=10),
        )
        return client, database

    def _create_async_transport(self, channel, client):
        return SpannerAsyncClient(
            client_info=client._client_info,
            transport=SpannerGrpcAsyncIOTransport(
                channel=channel,
                metrics_interceptor=MetricsInterceptor(),
            ),
        )

    async def test_async_query_happy_path_status_ok_and_spans(self):
        add_select1_result()
        reader = InMemoryMetricReader()
        meter_provider = MeterProvider(metric_readers=[reader])
        span_exporter = InMemorySpanExporter()
        tracer_provider = TracerProvider()
        tracer_provider.add_span_processor(SimpleSpanProcessor(span_exporter))

        with self._mock_async_metrics_environment(meter_provider):
            client, database = await self._create_async_client_and_database(
                tracer_provider=tracer_provider
            )
            async with grpc.aio.insecure_channel(
                "localhost:" + str(AsyncMockServerTestBase.port),
            ) as channel:
                database._spanner_api = self._create_async_transport(channel, client)

                async with database.snapshot() as snapshot:
                    results = await snapshot.execute_sql("select 1")
                    rows = []
                    async for row in results:
                        rows.append(row)
                    self.assertEqual(len(rows), 1)

            # Deleting results and snapshot afterwards should not change status to CANCELLED
            del results
            del snapshot
            gc.collect()

        metric_data = reader.get_metrics_data()
        self.assertIsNotNone(metric_data)
        metrics = {
            metric.name: metric
            for resource_metric in metric_data.resource_metrics
            for scope_metric in resource_metric.scope_metrics
            for metric in scope_metric.metrics
        }
        self.assertIn("attempt_latencies", metrics)
        attempt_latencies_metric = metrics["attempt_latencies"]
        streaming_points = [
            point
            for point in attempt_latencies_metric.data.data_points
            if point.attributes.get("method") == "Spanner.ExecuteStreamingSql"
        ]
        self.assertEqual(len(streaming_points), 1)
        self.assertEqual(streaming_points[0].attributes.get("status"), "OK")

        spans = span_exporter.get_finished_spans()
        query_spans = [
            span for span in spans if span.name == "CloudSpanner.Snapshot.execute_sql"
        ]
        self.assertEqual(len(query_spans), 1)
        self.assertEqual(query_spans[0].status.status_code, StatusCode.OK)

    async def test_async_query_cancelled_during_iteration(self):
        partial_result_set_1 = PartialResultSet()
        partial_result_set_1.metadata = ResultSetMetadata(
            row_type=StructType(
                fields=[
                    StructType.Field(name="ID", type_=Type(code=TypeCode.INT64)),
                ]
            )
        )
        partial_result_set_1.values.append(_make_value_pb(1))
        partial_result_set_1.resume_token = b"token_1"

        partial_result_set_2 = PartialResultSet()
        partial_result_set_2.values.append(_make_value_pb(2))
        partial_result_set_2.last = True

        sql = "select id from my_table"
        add_execute_streaming_sql_results(
            sql, [partial_result_set_1, partial_result_set_2]
        )

        reader = InMemoryMetricReader()
        meter_provider = MeterProvider(metric_readers=[reader])

        with self._mock_async_metrics_environment(meter_provider):
            client, database = await self._create_async_client_and_database()
            async with grpc.aio.insecure_channel(
                "localhost:" + str(AsyncMockServerTestBase.port),
            ) as channel:
                database._spanner_api = self._create_async_transport(channel, client)

                async with database.snapshot() as snapshot:
                    results = await snapshot.execute_sql(sql)
                    row_iterator = results.__aiter__()
                    first_row = await row_iterator.__anext__()
                    self.assertEqual(first_row[0], 1)
                    # Caller cancels/closes stream early
                    await results._response_iterator.aclose()

        metric_data = reader.get_metrics_data()
        self.assertIsNotNone(metric_data)
        metrics = {
            metric.name: metric
            for resource_metric in metric_data.resource_metrics
            for scope_metric in resource_metric.scope_metrics
            for metric in scope_metric.metrics
        }
        self.assertIn("attempt_latencies", metrics)
        attempt_latencies_metric = metrics["attempt_latencies"]
        streaming_points = [
            point
            for point in attempt_latencies_metric.data.data_points
            if point.attributes.get("method") == "Spanner.ExecuteStreamingSql"
        ]
        self.assertEqual(len(streaming_points), 1)
        self.assertEqual(streaming_points[0].attributes.get("status"), "CANCELLED")

    async def test_async_query_task_cancellation(self):
        partial_result_set_1 = PartialResultSet()
        partial_result_set_1.metadata = ResultSetMetadata(
            row_type=StructType(
                fields=[
                    StructType.Field(name="ID", type_=Type(code=TypeCode.INT64)),
                ]
            )
        )
        partial_result_set_1.values.append(_make_value_pb(1))
        partial_result_set_1.resume_token = b"token_1"

        partial_result_set_2 = PartialResultSet()
        partial_result_set_2.values.append(_make_value_pb(2))
        partial_result_set_2.last = True

        sql = "select id from my_table"
        add_execute_streaming_sql_results(
            sql, [partial_result_set_1, partial_result_set_2]
        )

        reader = InMemoryMetricReader()
        meter_provider = MeterProvider(metric_readers=[reader])

        with self._mock_async_metrics_environment(meter_provider):
            client, database = await self._create_async_client_and_database()
            async with grpc.aio.insecure_channel(
                "localhost:" + str(AsyncMockServerTestBase.port),
            ) as channel:
                database._spanner_api = self._create_async_transport(channel, client)

                row_consumed_event = asyncio.Event()

                async def consume_query():
                    async with database.snapshot() as snapshot:
                        results = await snapshot.execute_sql(sql)
                        async for row in results:
                            row_consumed_event.set()
                            # Block deterministically until cancelled
                            await asyncio.Event().wait()

                task = asyncio.create_task(consume_query())
                try:
                    await asyncio.wait_for(row_consumed_event.wait(), timeout=5.0)
                finally:
                    task.cancel()
                    try:
                        await task
                    except asyncio.CancelledError:
                        pass

        metric_data = reader.get_metrics_data()
        self.assertIsNotNone(metric_data)
        metrics = {
            metric.name: metric
            for resource_metric in metric_data.resource_metrics
            for scope_metric in resource_metric.scope_metrics
            for metric in scope_metric.metrics
        }
        self.assertIn("attempt_latencies", metrics)
        attempt_latencies_metric = metrics["attempt_latencies"]
        streaming_points = [
            point
            for point in attempt_latencies_metric.data.data_points
            if point.attributes.get("method") == "Spanner.ExecuteStreamingSql"
        ]
        self.assertEqual(len(streaming_points), 1)
        self.assertEqual(streaming_points[0].attributes.get("status"), "CANCELLED")

    async def test_async_query_garbage_collected_during_iteration(self):
        partial_result_set_1 = PartialResultSet()
        partial_result_set_1.metadata = ResultSetMetadata(
            row_type=StructType(
                fields=[
                    StructType.Field(name="ID", type_=Type(code=TypeCode.INT64)),
                ]
            )
        )
        partial_result_set_1.values.append(_make_value_pb(1))
        partial_result_set_1.resume_token = b"token_1"

        partial_result_set_2 = PartialResultSet()
        partial_result_set_2.values.append(_make_value_pb(2))
        partial_result_set_2.last = True

        sql = "select id from my_table"
        add_execute_streaming_sql_results(
            sql, [partial_result_set_1, partial_result_set_2]
        )

        reader = InMemoryMetricReader()
        meter_provider = MeterProvider(metric_readers=[reader])

        with self._mock_async_metrics_environment(meter_provider):
            client, database = await self._create_async_client_and_database()
            async with grpc.aio.insecure_channel(
                "localhost:" + str(AsyncMockServerTestBase.port),
            ) as channel:
                database._spanner_api = self._create_async_transport(channel, client)

                async with database.snapshot() as snapshot:
                    results = await snapshot.execute_sql(sql)
                    row_iterator = results.__aiter__()
                    first_row = await row_iterator.__anext__()
                    self.assertEqual(first_row[0], 1)
                    del row_iterator
                    del results
                    gc.collect()

        metric_data = reader.get_metrics_data()
        self.assertIsNotNone(metric_data)
        metrics = {
            metric.name: metric
            for resource_metric in metric_data.resource_metrics
            for scope_metric in resource_metric.scope_metrics
            for metric in scope_metric.metrics
        }
        self.assertIn("attempt_latencies", metrics)
        attempt_latencies_metric = metrics["attempt_latencies"]
        streaming_points = [
            point
            for point in attempt_latencies_metric.data.data_points
            if point.attributes.get("method") == "Spanner.ExecuteStreamingSql"
        ]
        self.assertEqual(len(streaming_points), 1)
        self.assertEqual(streaming_points[0].attributes.get("status"), "CANCELLED")

    async def test_async_metrics_disabled(self):
        add_select1_result()
        try:
            os.environ["SPANNER_DISABLE_BUILTIN_METRICS"] = "true"
            SpannerMetricsTracerFactory._metrics_tracer_factory = None
            async_client_mod._metrics_monitor_initialized = False

            reader = InMemoryMetricReader()
            meter_provider = MeterProvider(metric_readers=[reader])

            with self._mock_async_metrics_environment(meter_provider):
                client, database = await self._create_async_client_and_database()
                async with grpc.aio.insecure_channel(
                    "localhost:" + str(AsyncMockServerTestBase.port),
                ) as channel:
                    database._spanner_api = self._create_async_transport(
                        channel, client
                    )

                    async with database.snapshot() as snapshot:
                        results = await snapshot.execute_sql("select 1")
                        rows = []
                        async for row in results:
                            rows.append(row)
                        self.assertEqual(len(rows), 1)

            metric_data = reader.get_metrics_data()
            if metric_data is not None:
                recorded_metric_names = {
                    metric.name
                    for resource_metric in metric_data.resource_metrics
                    for scope_metric in resource_metric.scope_metrics
                    for metric in scope_metric.metrics
                }
                intersection = recorded_metric_names & _SPANNER_METRIC_NAMES
                self.assertEqual(
                    len(intersection),
                    0,
                    f"Metrics should not be recorded when disabled, found: {intersection}",
                )
        finally:
            os.environ["SPANNER_DISABLE_BUILTIN_METRICS"] = "false"
            SpannerMetricsTracerFactory._metrics_tracer_factory = None
            async_client_mod._metrics_monitor_initialized = False

    async def test_async_unary_happy_path(self):
        reader = InMemoryMetricReader()
        meter_provider = MeterProvider(metric_readers=[reader])

        with self._mock_async_metrics_environment(meter_provider):
            client, database = await self._create_async_client_and_database()
            async with grpc.aio.insecure_channel(
                "localhost:" + str(AsyncMockServerTestBase.port),
            ) as channel:
                database._spanner_api = self._create_async_transport(channel, client)

                session = database.session()
                await session.create()

        metric_data = reader.get_metrics_data()
        self.assertIsNotNone(metric_data)
        metrics = {
            metric.name: metric
            for resource_metric in metric_data.resource_metrics
            for scope_metric in resource_metric.scope_metrics
            for metric in scope_metric.metrics
        }
        self.assertIn("attempt_latencies", metrics)
        attempt_latencies_metric = metrics["attempt_latencies"]
        session_points = [
            point
            for point in attempt_latencies_metric.data.data_points
            if point.attributes.get("method") == "Spanner.CreateSession"
        ]
        self.assertTrue(len(session_points) > 0)
        self.assertEqual(session_points[0].attributes.get("status"), "OK")

    async def test_async_server_timing_regex_boundary_safe_from_false_positives(self):
        add_select1_result()
        add_header(
            "ExecuteStreamingSql",
            "server-timing",
            "safe; dur=99, x-gfet4t7; dur=88, afe; dur=23, gfet4t7; dur=55",
        )
        reader = InMemoryMetricReader()
        meter_provider = MeterProvider(metric_readers=[reader])

        with self._mock_async_metrics_environment(meter_provider):
            client, database = await self._create_async_client_and_database()
            async with grpc.aio.insecure_channel(
                "localhost:" + str(AsyncMockServerTestBase.port),
            ) as channel:
                database._spanner_api = self._create_async_transport(channel, client)
                async with database.snapshot() as snapshot:
                    results = await snapshot.execute_sql("select 1")
                    async for _ in results:
                        pass

        metric_data = reader.get_metrics_data()
        self.assertIsNotNone(metric_data)
        metrics = {
            metric.name: metric
            for resource_metric in metric_data.resource_metrics
            for scope_metric in resource_metric.scope_metrics
            for metric in scope_metric.metrics
        }
        self.assertIn("gfe_latencies", metrics)
        self.assertIn("afe_latencies", metrics)
        gfe_point = next(iter(metrics["gfe_latencies"].data.data_points))
        afe_point = next(iter(metrics["afe_latencies"].data.data_points))
        self.assertEqual(gfe_point.sum, 55)
        self.assertEqual(afe_point.sum, 23)

    async def test_async_streaming_read_metrics(self):
        from google.cloud.spanner_v1.keyset import KeySet

        add_header(
            "StreamingRead",
            "server-timing",
            "gfet4t7; dur=40, afe; dur=15",
        )
        reader = InMemoryMetricReader()
        meter_provider = MeterProvider(metric_readers=[reader])

        with self._mock_async_metrics_environment(meter_provider):
            client, database = await self._create_async_client_and_database()
            async with grpc.aio.insecure_channel(
                "localhost:" + str(AsyncMockServerTestBase.port),
            ) as channel:
                database._spanner_api = self._create_async_transport(channel, client)
                async with database.snapshot() as snapshot:
                    results = await snapshot.read(
                        table="my_table",
                        columns=["id"],
                        keyset=KeySet(all_=True),
                    )
                    async for _ in results:
                        pass

        metric_data = reader.get_metrics_data()
        self.assertIsNotNone(metric_data)
        metrics = {
            metric.name: metric
            for resource_metric in metric_data.resource_metrics
            for scope_metric in resource_metric.scope_metrics
            for metric in scope_metric.metrics
        }
        self.assertIn("gfe_latencies", metrics)
        self.assertIn("afe_latencies", metrics)
        self.assertIn("attempt_latencies", metrics)
        streaming_points = [
            point
            for point in metrics["attempt_latencies"].data.data_points
            if point.attributes.get("method") == "Spanner.StreamingRead"
        ]
        self.assertEqual(len(streaming_points), 1)
        self.assertEqual(streaming_points[0].attributes.get("status"), "OK")
