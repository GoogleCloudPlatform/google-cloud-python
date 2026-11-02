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

import unittest
from unittest.mock import MagicMock, Mock, patch

from google.api.metric_pb2 import MetricDescriptor
from google.auth.credentials import AnonymousCredentials
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import (
    AggregationTemporality,
    Gauge,
    Histogram,
    HistogramDataPoint,
    InMemoryMetricReader,
    NumberDataPoint,
    Sum,
)

from google.cloud.spanner_v1.metrics.constants import METRIC_NAME_OPERATION_COUNT
from google.cloud.spanner_v1.metrics.metrics_exporter import (
    CloudMonitoringMetricsExporter,
    _normalize_label_key,
)
from tests._helpers import HAS_OPENTELEMETRY_INSTALLED

# Test Constants
PROJECT_ID = "fake-project-id"
INSTANCE_ID = "fake-instance-id"
DATABASE_ID = "fake-database-id"
SCOPE_NAME = "gax-python"

# Skip tests if opentelemetry is not installed
if HAS_OPENTELEMETRY_INSTALLED:

    class TestMetricsExporter(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            cls.metric_attributes = {
                "project_id": PROJECT_ID,
                "instance_id": INSTANCE_ID,
                "instance_config": "test_config",
                "location": "test_location",
                "client_hash": "test_hash",
                "client_uid": "test_uid",
                "client_name": "test_name",
                "database": DATABASE_ID,
                "method": "test_method",
                "status": "test_status",
                "directpath_enabled": "true",
                "directpath_used": "false",
                "other": "ignored",
            }

        def setUp(self):
            self.metric_reader = InMemoryMetricReader()
            self.provider = MeterProvider(metric_readers=[self.metric_reader])
            self.meter = self.provider.get_meter(SCOPE_NAME)
            self.operation_count = self.meter.create_counter(
                name=METRIC_NAME_OPERATION_COUNT,
                description="A test counter",
                unit="counts",
            )

        def test_normalize_label_key(self):
            """Test label key normalization"""
            test_cases = [
                ("simple", "simple"),
                ("with space", "with_space"),
                ("with-dash", "with_dash"),
                ("123_number_prefix", "key_123_number_prefix"),
                ("special!characters@", "special_characters_"),
            ]

            for input_key, expected_output in test_cases:
                self.assertEqual(_normalize_label_key(input_key), expected_output)

        def test_to_metric_kind(self):
            """Test conversion of different metric types to GCM metric kinds"""
            # Test monotonic Sum returns CUMULATIVE
            metric_sum = Mock(
                data=Sum(
                    data_points=[],
                    aggregation_temporality=AggregationTemporality.UNSPECIFIED,
                    is_monotonic=True,
                )
            )
            self.assertEqual(
                CloudMonitoringMetricsExporter._to_metric_kind(metric_sum),
                MetricDescriptor.MetricKind.CUMULATIVE,
            )

            # Test non-monotonic Sum returns GAUGE
            metric_sum_non_monotonic = Mock(
                data=Sum(
                    data_points=[],
                    aggregation_temporality=AggregationTemporality.UNSPECIFIED,
                    is_monotonic=False,
                )
            )
            self.assertEqual(
                CloudMonitoringMetricsExporter._to_metric_kind(
                    metric_sum_non_monotonic
                ),
                MetricDescriptor.MetricKind.GAUGE,
            )

            # Test Gauge returns GAUGE
            metric_gauge = Mock(data=Gauge(data_points=[]))
            self.assertEqual(
                CloudMonitoringMetricsExporter._to_metric_kind(metric_gauge),
                MetricDescriptor.MetricKind.GAUGE,
            )

            # Test Histogram returns CUMULATIVE
            metric_histogram = Mock(
                data=Histogram(
                    data_points=[],
                    aggregation_temporality=AggregationTemporality.UNSPECIFIED,
                )
            )
            self.assertEqual(
                CloudMonitoringMetricsExporter._to_metric_kind(metric_histogram),
                MetricDescriptor.MetricKind.CUMULATIVE,
            )

            # Test Unknown data type warns
            metric_unknown = Mock(data=Mock())
            with self.assertLogs(
                "google.cloud.spanner_v1.metrics.metrics_exporter", level="WARNING"
            ) as log:
                self.assertIsNone(
                    CloudMonitoringMetricsExporter._to_metric_kind(metric_unknown)
                )
                self.assertIn(
                    "WARNING:google.cloud.spanner_v1.metrics.metrics_exporter:Unsupported metric data type Mock, ignoring it",
                    log.output,
                )

        def test_extract_metric_labels(self):
            """Test extraction of metric and resource labels"""
            import time

            data_point = NumberDataPoint(
                attributes={
                    # Metric labels
                    "client_uid": "test-client-uid",
                    "client_name": "test-client-name",
                    "database": "test-db",
                    "method": "test-method",
                    "status": "test-status",
                    "directpath_enabled": "test-directpath-enabled",
                    "directpath_used": "test-directpath-used",
                    # Monitored Resource label
                    "project_id": "test-project-id",
                    "instance_id": "test-instance-id",
                    "instance_config": "test-instance-config",
                    "location": "test-location",
                    "client_hash": "test-client-hash",
                    # All other labels ignored
                    "unknown": "ignored",
                    "Client_UID": "ignored",
                },
                start_time_unix_nano=time.time_ns(),
                time_unix_nano=time.time_ns(),
                value=0,
            )

            (
                metric_labels,
                resource_labels,
            ) = CloudMonitoringMetricsExporter._extract_metric_labels(data_point)

            # Verify that the attributes are properly distributed and reassigned

            ## Metric Labels
            self.assertIn("client_uid", metric_labels)
            self.assertEqual(metric_labels["client_uid"], "test-client-uid")
            self.assertIn("client_name", metric_labels)
            self.assertEqual(metric_labels["client_name"], "test-client-name")
            self.assertIn("database", metric_labels)
            self.assertEqual(metric_labels["database"], "test-db")
            self.assertIn("method", metric_labels)
            self.assertEqual(metric_labels["method"], "test-method")
            self.assertIn("status", metric_labels)
            self.assertEqual(metric_labels["status"], "test-status")
            self.assertIn("directpath_enabled", metric_labels)
            self.assertEqual(
                metric_labels["directpath_enabled"], "test-directpath-enabled"
            )
            self.assertIn("directpath_used", metric_labels)
            self.assertEqual(metric_labels["directpath_used"], "test-directpath-used")

            ## Metric Resource Labels
            self.assertIn("project_id", resource_labels)
            self.assertEqual(resource_labels["project_id"], "test-project-id")
            self.assertIn("instance_id", resource_labels)
            self.assertEqual(resource_labels["instance_id"], "test-instance-id")
            self.assertIn("instance_config", resource_labels)
            self.assertEqual(resource_labels["instance_config"], "test-instance-config")
            self.assertIn("location", resource_labels)
            self.assertEqual(resource_labels["location"], "test-location")
            self.assertIn("client_hash", resource_labels)
            self.assertEqual(resource_labels["client_hash"], "test-client-hash")

            # Other attributes are ignored
            self.assertNotIn("unknown", metric_labels)
            self.assertNotIn("unknown", resource_labels)
            ## including case sensitive keys
            self.assertNotIn("Client_UID", metric_labels)
            self.assertNotIn("Client_UID", resource_labels)

        def test_metric_timeseries_conversion(self):
            """Test to verify conversion from OTEL Metrics to GCM Time Series."""
            # Add metrics
            self.operation_count.add(1, attributes=self.metric_attributes)
            self.operation_count.add(2, attributes=self.metric_attributes)

            # Export metrics
            metrics = self.metric_reader.get_metrics_data()
            self.assertTrue(metrics is not None)

            exporter = CloudMonitoringMetricsExporter(
                PROJECT_ID, credentials=AnonymousCredentials()
            )
            timeseries = exporter._resource_metrics_to_timeseries_pb(metrics)

            # Both counter values should be summed together
            self.assertEqual(len(timeseries), 1)
            self.assertEqual(timeseries[0].points.pop(0).value.int64_value, 3)

        def test_metric_timeseries_scope_filtering(self):
            """Test to verify that metrics without the `gax-python` scope are filtered out."""
            # Create metric instruments
            meter = self.provider.get_meter("WRONG_SCOPE")
            counter = meter.create_counter(
                name="operation_latencies", description="A test counter", unit="ms"
            )

            # Add metrics
            counter.add(1, attributes=self.metric_attributes)
            counter.add(2, attributes=self.metric_attributes)

            # Export metrics
            metrics = self.metric_reader.get_metrics_data()
            exporter = CloudMonitoringMetricsExporter(
                PROJECT_ID, credentials=AnonymousCredentials()
            )
            timeseries = exporter._resource_metrics_to_timeseries_pb(metrics)

            # Metris with incorrect sope should be filtered out
            self.assertEqual(len(timeseries), 0)

        def test_batch_write(self):
            """Verify that writes happen in batches of 200"""
            import random

            from google.api.metric_pb2 import Metric as GMetric
            from google.api.monitored_resource_pb2 import MonitoredResource
            from google.cloud.monitoring_v3 import (
                MetricServiceClient,
                Point,
                TimeInterval,
                TimeSeries,
                TypedValue,
            )
            from google.protobuf.timestamp_pb2 import Timestamp

            mockClient = MagicMock(spec=MetricServiceClient)
            mockClient.create_service_time_series = Mock(return_value=None)
            exporter = CloudMonitoringMetricsExporter(PROJECT_ID, mockClient)

            # Create timestamps for the time series
            start_time = Timestamp()
            start_time.FromSeconds(1234567890)
            end_time = Timestamp()
            end_time.FromSeconds(1234567900)

            # Create test time series
            timeseries = []
            for i in range(400):
                timeseries.append(
                    TimeSeries(
                        metric=GMetric(
                            type=f"custom.googleapis.com/spanner/test_metric_{i}",
                            labels={"client_uid": "test-client", "database": "test-db"},
                        ),
                        resource=MonitoredResource(
                            type="spanner_instance",
                            labels={
                                "project_id": PROJECT_ID,
                                "instance_id": INSTANCE_ID,
                                "location": "test-location",
                            },
                        ),
                        metric_kind=MetricDescriptor.MetricKind.CUMULATIVE,
                        points=[
                            Point(
                                interval=TimeInterval(
                                    start_time=start_time, end_time=end_time
                                ),
                                value=TypedValue(int64_value=random.randint(1, 100)),
                            )
                        ],
                    ),
                )

            # Define a side effect to extract time series data passed to mocked CreatetimeSeriesRquest
            tsr_timeseries = []

            def create_tsr_side_effect(name, time_series):
                nonlocal tsr_timeseries
                tsr_timeseries = time_series

            patch_path = "google.cloud.spanner_v1.metrics.metrics_exporter.CreateTimeSeriesRequest"
            with patch(patch_path, side_effect=create_tsr_side_effect):
                exporter._batch_write(timeseries, 10000)
                # Verify that the Create Time Series calls happen in batches of max 200 elements
                self.assertTrue(len(tsr_timeseries) > 0 and len(tsr_timeseries) <= 200)

            # Verify the mock was called with the correct arguments
            self.assertEqual(len(mockClient.create_service_time_series.mock_calls), 2)

        @patch(
            "google.cloud.spanner_v1.metrics.metrics_exporter.HAS_OPENTELEMETRY_INSTALLED",
            False,
        )
        def test_export_early_exit_if_extras_not_installed(self):
            """Verify that Export will early exit and return None if OpenTelemetry and/or Google Cloud Monitoring extra modules are not installed."""
            # Suppress expected warning log
            with self.assertLogs(
                "google.cloud.spanner_v1.metrics.metrics_exporter", level="WARNING"
            ) as log:
                exporter = CloudMonitoringMetricsExporter(
                    PROJECT_ID, credentials=AnonymousCredentials()
                )
                self.assertFalse(exporter.export([]))
                self.assertIn(
                    "WARNING:google.cloud.spanner_v1.metrics.metrics_exporter:Metric exporter called without dependencies installed.",
                    log.output,
                )

        def test_export(self):
            """Verify that the export call will convert and send the requests out."""
            # Create metric instruments
            meter = self.provider.get_meter("gax-python")
            counter = meter.create_counter(
                name="attempt_count", description="A test counter", unit="count"
            )
            latency = meter.create_counter(
                name="attempt_latencies", description="test latencies", unit="ms"
            )

            # Add metrics
            counter.add(10, attributes=self.metric_attributes)
            counter.add(25, attributes=self.metric_attributes)
            latency.add(30, attributes=self.metric_attributes)
            latency.add(45, attributes=self.metric_attributes)

            # Export metrics
            metrics = self.metric_reader.get_metrics_data()
            mock_client = Mock()
            exporter = CloudMonitoringMetricsExporter(PROJECT_ID, mock_client)
            patch_path = "google.cloud.spanner_v1.metrics.metrics_exporter.CloudMonitoringMetricsExporter._batch_write"
            with patch(patch_path) as mock_batch_write:
                exporter.export(metrics)

            # Verify metrics passed to be sent to Google Cloud Monitoring
            mock_batch_write.assert_called_once()
            batch_args, _ = mock_batch_write.call_args
            timeseries = batch_args[0]
            self.assertEqual(len(timeseries), 2)

        def test_force_flush(self):
            """Verify that the unimplemented force flush can be called."""
            exporter = CloudMonitoringMetricsExporter(
                PROJECT_ID, credentials=AnonymousCredentials()
            )
            self.assertTrue(exporter.force_flush())

        def test_shutdown(self):
            """Verify that the unimplemented shutdown can be called."""
            exporter = CloudMonitoringMetricsExporter(
                project_id="test", credentials=AnonymousCredentials()
            )
            try:
                exporter.shutdown()
            except Exception as e:
                self.fail(f"Shutdown() raised an exception: {e}")

        def test_data_point_to_timeseries_early_exit(self):
            """Early exit function if an unknown metric name is supplied."""
            metric = Mock(name="TestMetricName")
            self.assertIsNone(
                CloudMonitoringMetricsExporter._data_point_to_timeseries_pb(
                    None, metric, None, None
                )
            )

        @patch(
            "google.cloud.spanner_v1.metrics.metrics_exporter.CloudMonitoringMetricsExporter._data_point_to_timeseries_pb"
        )
        def test_metrics_to_time_series_empty_input(
            self, mocked_data_point_to_timeseries_pb
        ):
            """Verify that metric entries with no timeseries data do not return a time series entry."""
            exporter = CloudMonitoringMetricsExporter(
                project_id="test", credentials=AnonymousCredentials()
            )
            data_point = Mock()
            metric = Mock(data_points=[data_point])
            scope_metric = Mock(
                metrics=[metric], scope=Mock(name="operation_latencies")
            )
            resource_metric = Mock(scope_metrics=[scope_metric])
            metrics_data = Mock(resource_metrics=[resource_metric])

            exporter._resource_metrics_to_timeseries_pb(metrics_data)

        def test_to_point(self):
            """Verify conversion of datapoints."""
            exporter = CloudMonitoringMetricsExporter(
                project_id="test", credentials=AnonymousCredentials()
            )

            number_point = NumberDataPoint(
                attributes=[], start_time_unix_nano=0, time_unix_nano=0, value=9
            )

            # Test that provided int number point values are set to the converted int data point
            converted_num_point = exporter._to_point(
                MetricDescriptor.MetricKind.CUMULATIVE, number_point
            )

            self.assertEqual(converted_num_point.value.int64_value, 9)

            # Test that provided float number point values are set to converted double data point
            float_number_point = NumberDataPoint(
                attributes=[], start_time_unix_nano=0, time_unix_nano=0, value=12.20
            )
            converted_float_num_point = exporter._to_point(
                MetricDescriptor.MetricKind.CUMULATIVE, float_number_point
            )
            self.assertEqual(converted_float_num_point.value.double_value, 12.20)

            hist_point = HistogramDataPoint(
                attributes=[],
                start_time_unix_nano=123,
                time_unix_nano=456,
                count=1,
                sum=2,
                bucket_counts=[3],
                explicit_bounds=[4],
                min=5.0,
                max=6.0,
            )

            # Test that provided histogram point values are set to the converted data point
            converted_hist_point = exporter._to_point(
                MetricDescriptor.MetricKind.CUMULATIVE, hist_point
            )
            self.assertEqual(converted_hist_point.value.distribution_value.count, 1)
            self.assertEqual(converted_hist_point.value.distribution_value.mean, 2)

            hist_point_missing_count = HistogramDataPoint(
                attributes=[],
                start_time_unix_nano=123,
                time_unix_nano=456,
                count=None,
                sum=2,
                bucket_counts=[3],
                explicit_bounds=[4],
                min=5.0,
                max=6.0,
            )

            # Test that histogram points missing a count value has mean defaulted to 0
            # and that non cmulative / delta kinds default to single timepoint interval
            converted_hist_point_no_count = exporter._to_point(
                MetricDescriptor.MetricKind.METRIC_KIND_UNSPECIFIED,
                hist_point_missing_count,
            )
            self.assertEqual(
                converted_hist_point_no_count.value.distribution_value.mean, 0
            )
            self.assertIsNone(converted_hist_point_no_count.interval.start_time)
            self.assertIsNotNone(converted_hist_point_no_count.interval.end_time)
