# Copyright 2025 Google LLC
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
import logging

import mock
import pytest
from google.api.distribution_pb2 import Distribution
from google.api_core import exceptions as api_exceptions
from google.cloud.monitoring_v3 import (
    Point,
    TimeSeries,
)
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import (
    AggregationTemporality,
    HistogramDataPoint,
    Metric,
    MetricExportResult,
    MetricsData,
    NumberDataPoint,
    ResourceMetrics,
    ScopeMetrics,
    Sum,
)

from google.cloud.bigtable.data._metrics.handlers.gcp_exporter import (
    BigtableMetricsExporter,
    GoogleCloudMetricsHandler,
)
from google.cloud.bigtable.data._metrics.handlers.opentelemetry import (
    _OpenTelemetryInstruments,
)

EXPORTER_LOGGER = "google.cloud.bigtable.data._metrics.handlers.gcp_exporter"


class TestGoogleCloudMetricsHandler:
    def _make_one(self, *args, **kwargs):
        return GoogleCloudMetricsHandler(*args, **kwargs)

    @mock.patch("google.auth.default", return_value=(mock.Mock(), "project"))
    def test_ctor_defaults(self, mock_auth):
        from google.cloud.bigtable import __version__ as CLIENT_VERSION

        expected_exporter = BigtableMetricsExporter()
        with mock.patch.object(
            GoogleCloudMetricsHandler, "_generate_client_uid"
        ) as uid_mock:
            handler = self._make_one(expected_exporter)
        assert isinstance(handler.meter_provider, MeterProvider)
        assert isinstance(handler.otel, _OpenTelemetryInstruments)
        assert (
            handler.shared_labels["client_name"] == f"python-bigtable/{CLIENT_VERSION}"
        )
        assert handler.shared_labels["client_uid"] == uid_mock()

    @mock.patch("google.auth.default", return_value=(mock.Mock(), "project"))
    def test_ctor_explicit(self, mock_auth):
        expected_version = "my_version"
        expected_uid = "my_uid"
        expected_exporter = BigtableMetricsExporter()
        handler = self._make_one(
            expected_exporter,
            client_uid=expected_uid,
            client_version=expected_version,
        )
        assert handler.otel == _OpenTelemetryInstruments() or handler.otel is not None
        assert (
            handler.shared_labels["client_name"]
            == f"python-bigtable/{expected_version}"
        )
        assert handler.shared_labels["client_uid"] == expected_uid

    @mock.patch(
        "google.cloud.bigtable.data._metrics.handlers.gcp_exporter.PeriodicExportingMetricReader"
    )
    @mock.patch(
        "google.cloud.bigtable.data._metrics.handlers.gcp_exporter.MeterProvider"
    )
    @mock.patch(
        "google.cloud.bigtable.data._metrics.handlers.gcp_exporter._OpenTelemetryInstruments"
    )
    @mock.patch(
        "google.cloud.bigtable.data._metrics.handlers.gcp_exporter.OpenTelemetryMetricsHandler.__init__"
    )
    def test_ctor_with_mocks(
        self, mock_super_init, mock_otel_instruments, mock_meter_provider, mock_reader
    ):
        from google.cloud.bigtable.data._metrics.handlers.gcp_exporter import (
            VIEW_LIST,
        )

        exporter = mock.Mock()
        export_interval = 90
        kwargs = {"instance_id": "test_instance", "table_id": "test_table"}
        handler = self._make_one(exporter, export_interval=export_interval, **kwargs)
        # check PeriodicExportingMetricReader
        mock_reader.assert_called_once_with(
            exporter, export_interval_millis=export_interval * 1000
        )
        # check MeterProvider
        mock_meter_provider.assert_called_once_with(
            metric_readers=[mock_reader.return_value], views=VIEW_LIST
        )
        # check _OpenTelemetryInstruments
        mock_otel_instruments.assert_called_once_with(
            meter_provider=mock_meter_provider.return_value
        )
        # check super().__init__ call
        mock_super_init.assert_called_once_with(
            instruments=mock_otel_instruments.return_value, **kwargs
        )
        assert handler.meter_provider == mock_meter_provider.return_value

    def test_close(self):
        mock_instance = mock.Mock()
        mock_instance._exporter.shutting_down = False

        def _shutdown():
            # the exporter must be flagged before shutdown runs the final export
            assert mock_instance._exporter.shutting_down is True

        mock_instance.meter_provider.shutdown.side_effect = _shutdown
        assert mock_instance.meter_provider.shutdown.call_count == 0
        GoogleCloudMetricsHandler.close(mock_instance)
        assert mock_instance.meter_provider.shutdown.call_count == 1
        assert mock_instance._exporter.shutting_down is True


BIGTABLE_DATA_SCOPE = "https://www.googleapis.com/auth/bigtable.data"
BIGTABLE_ADMIN_SCOPE = "https://www.googleapis.com/auth/bigtable.admin"
MONITORING_WRITE_SCOPE = "https://www.googleapis.com/auth/monitoring.write"


def _make_service_account_credentials(**kwargs):
    import google.auth.crypt
    from google.oauth2 import service_account

    return service_account.Credentials(
        mock.Mock(spec=google.auth.crypt.Signer),
        "sa@example.iam.gserviceaccount.com",
        "https://oauth2.googleapis.com/token",
        **kwargs,
    )


class Test_get_monitoring_credentials:
    @staticmethod
    def _call_fut(credentials):
        from google.cloud.bigtable.data._metrics.handlers.gcp_exporter import (
            _get_monitoring_credentials,
        )

        return _get_monitoring_credentials(credentials)

    def test_none(self):
        assert self._call_fut(None) is None

    def test_non_scopable_credentials(self):
        """credentials that can't be re-scoped (e.g. user credentials) pass through"""
        from google.auth.credentials import AnonymousCredentials
        from google.oauth2 import credentials as user_credentials

        anonymous = AnonymousCredentials()
        assert self._call_fut(anonymous) is anonymous
        user = user_credentials.Credentials(token="token")
        assert self._call_fut(user) is user

    def test_unscoped_credentials(self):
        """
        credentials that still accept default scopes are left alone;
        MetricServiceClient will apply its own defaults to them
        """
        credentials = _make_service_account_credentials()
        assert credentials.requires_scopes
        assert self._call_fut(credentials) is credentials

    @pytest.mark.parametrize(
        "pinned_scopes",
        [
            (BIGTABLE_DATA_SCOPE,),
            (BIGTABLE_DATA_SCOPE, BIGTABLE_ADMIN_SCOPE),
            ["https://www.googleapis.com/auth/bigtable.data.readonly"],
        ],
    )
    def test_credentials_pinned_to_bigtable_scopes(self, pinned_scopes):
        """
        credentials already pinned to non-monitoring scopes (e.g. by the legacy
        client) should be replaced by a copy that can write to Cloud Monitoring
        """
        credentials = _make_service_account_credentials(
            scopes=pinned_scopes, quota_project_id="quota-project"
        )
        result = self._call_fut(credentials)
        assert result is not credentials
        assert list(result.scopes) == [MONITORING_WRITE_SCOPE]
        # identity and other settings are preserved
        assert result.service_account_email == credentials.service_account_email
        assert result.quota_project_id == "quota-project"
        # original credentials are left untouched for bigtable traffic
        assert tuple(credentials.scopes) == tuple(pinned_scopes)

    def test_compute_engine_credentials_pinned_to_bigtable_scopes(self):
        from google.auth import compute_engine

        credentials = compute_engine.Credentials(scopes=[BIGTABLE_DATA_SCOPE])
        assert not credentials.requires_scopes
        result = self._call_fut(credentials)
        assert result is not credentials
        assert list(result.scopes) == [MONITORING_WRITE_SCOPE]
        assert list(credentials.scopes) == [BIGTABLE_DATA_SCOPE]

    @pytest.mark.parametrize(
        "scopes",
        [
            ["https://www.googleapis.com/auth/cloud-platform"],
            ["https://www.googleapis.com/auth/monitoring"],
            [MONITORING_WRITE_SCOPE],
            [BIGTABLE_DATA_SCOPE, MONITORING_WRITE_SCOPE],
            (BIGTABLE_DATA_SCOPE, "https://www.googleapis.com/auth/cloud-platform"),
        ],
    )
    def test_credentials_already_cover_monitoring(self, scopes):
        credentials = _make_service_account_credentials(scopes=scopes)
        assert not credentials.requires_scopes
        assert self._call_fut(credentials) is credentials


class TestBigtableMetricsExporter:
    def _make_one(self, *args, **kwargs):
        with mock.patch("google.auth.default", return_value=(mock.Mock(), "project")):
            return BigtableMetricsExporter(*args, **kwargs)

    def test__partition_attributes(self):
        from google.cloud.bigtable.data._metrics.handlers.gcp_exporter import (
            _partition_attributes,
        )

        attributes = {
            "resource_project": "proj-1",
            "resource_instance": "inst-1",
            "resource_cluster": "cls-1",
            "resource_table": "tbl-1",
            "resource_zone": "zone-1",
            "method": "ReadRows",
            "status_code": "OK",
            "resource_custom_unsupported": "should_be_stripped",
        }
        res_labels, metric_labels = _partition_attributes(attributes)
        assert res_labels == {
            "project_id": "proj-1",
            "instance": "inst-1",
            "cluster": "cls-1",
            "table": "tbl-1",
            "zone": "zone-1",
        }
        assert metric_labels == {
            "method": "ReadRows",
            "status_code": "OK",
        }

    def test_ctor_defaults(self):
        from google.cloud.monitoring_v3 import MetricServiceClient

        instance = self._make_one()
        assert instance.prefix == "bigtable.googleapis.com/internal/client"
        assert isinstance(instance.client, MetricServiceClient)
        assert instance._disabled is False
        assert instance.shutting_down is False

    def test_ctor_mocks(self):
        with mock.patch(
            "google.cloud.monitoring_v3.MetricServiceClient.__init__",
            return_value=None,
        ) as mock_client:
            args = [mock.Mock(), object()]
            kwargs = {"a": "b"}
            instance = self._make_one(*args, **kwargs)
            assert instance.prefix == "bigtable.googleapis.com/internal/client"
            mock_client.assert_called_once_with(*args, **kwargs)

    def test_ctor_rescopes_pinned_credentials(self):
        """
        credentials pinned to bigtable-only scopes (e.g. from the legacy client)
        should be re-scoped for Cloud Monitoring before building the client
        """
        credentials = _make_service_account_credentials(
            scopes=[BIGTABLE_DATA_SCOPE, BIGTABLE_ADMIN_SCOPE]
        )
        with mock.patch(
            "google.cloud.bigtable.data._metrics.handlers.gcp_exporter.MetricServiceClient"
        ) as mock_client:
            instance = self._make_one(credentials=credentials, client_options=None)
            assert instance.client is mock_client.return_value
            mock_client.assert_called_once()
            _, kwargs = mock_client.call_args
            assert kwargs["client_options"] is None
            monitoring_credentials = kwargs["credentials"]
            assert monitoring_credentials is not credentials
            assert list(monitoring_credentials.scopes) == [MONITORING_WRITE_SCOPE]
        # original credentials are untouched
        assert list(credentials.scopes) == [BIGTABLE_DATA_SCOPE, BIGTABLE_ADMIN_SCOPE]

    @pytest.mark.parametrize(
        "credentials",
        [
            None,
            _make_service_account_credentials(),
            _make_service_account_credentials(
                scopes=["https://www.googleapis.com/auth/cloud-platform"]
            ),
        ],
    )
    def test_ctor_passes_through_usable_credentials(self, credentials):
        """credentials that can already reach Cloud Monitoring are passed as-is"""
        with mock.patch(
            "google.cloud.bigtable.data._metrics.handlers.gcp_exporter.MetricServiceClient"
        ) as mock_client:
            self._make_one(credentials=credentials)
            mock_client.assert_called_once_with(credentials=credentials)

    @pytest.mark.parametrize(
        "value,expected_field",
        [
            (123, "int64_value"),
            (123.456, "double_value"),
        ],
    )
    def test__to_point_w_number(self, value, expected_field):
        """Test that NumberDataPoint is converted to a Point correctly."""
        instance = self._make_one()
        expected_start_time_nanos = 100
        expected_end_time_nanos = 200
        dp = NumberDataPoint(
            attributes={},
            start_time_unix_nano=expected_start_time_nanos,
            time_unix_nano=expected_end_time_nanos,
            value=value,
        )
        point = instance._to_point(dp)
        assert isinstance(point, Point)
        assert getattr(point.value, expected_field) == value
        assert (
            point.interval.start_time.second * 10**9
        ) + point.interval.start_time.nanosecond == expected_start_time_nanos
        assert (
            point.interval.end_time.second * 10**9
        ) + point.interval.end_time.nanosecond == expected_end_time_nanos

    def test__to_point_w_histogram(self):
        """Test that HistogramDataPoint is converted to a Point correctly."""
        instance = self._make_one()
        expected_start_time_nanos = 100
        expected_end_time_nanos = 200
        expected_count = 10
        expected_sum = 100.0
        expected_bucket_counts = [1, 2, 7]
        expected_explicit_bounds = [10, 20]
        dp = HistogramDataPoint(
            attributes={},
            start_time_unix_nano=expected_start_time_nanos,
            time_unix_nano=expected_end_time_nanos,
            count=expected_count,
            sum=expected_sum,
            bucket_counts=expected_bucket_counts,
            explicit_bounds=expected_explicit_bounds,
            min=0,
            max=50,
        )
        point = instance._to_point(dp)
        assert isinstance(point, Point)
        dist = point.value.distribution_value
        assert isinstance(dist, Distribution)
        assert dist.count == expected_count
        assert dist.mean == expected_sum / expected_count
        assert list(dist.bucket_counts) == expected_bucket_counts
        assert (
            list(dist.bucket_options.explicit_buckets.bounds)
            == expected_explicit_bounds
        )
        assert (
            point.interval.start_time.second * 10**9
        ) + point.interval.start_time.nanosecond == expected_start_time_nanos
        assert (
            point.interval.end_time.second * 10**9
        ) + point.interval.end_time.nanosecond == expected_end_time_nanos

    def test__to_point_w_histogram_zero_count(self):
        """Test that HistogramDataPoint with zero count is converted to a Point correctly."""
        instance = self._make_one()
        dp = HistogramDataPoint(
            attributes={},
            start_time_unix_nano=100,
            time_unix_nano=200,
            count=0,
            sum=0,
            bucket_counts=[],
            explicit_bounds=[],
            min=0,
            max=0,
        )
        point = instance._to_point(dp)
        assert isinstance(point, Point)
        dist = point.value.distribution_value
        assert isinstance(dist, Distribution)
        assert dist.count == 0
        assert dist.mean == 0.0

    @pytest.mark.parametrize(
        "num_series, batch_size, expected_calls, expected_batch_sizes",
        [
            (10, 200, 1, [10]),
            (200, 200, 1, [200]),
            (500, 200, 3, [200, 200, 100]),
            (0, 200, 0, []),
        ],
    )
    def test__batch_write(
        self, num_series, batch_size, expected_calls, expected_batch_sizes
    ):
        """Test that _batch_write splits series into batches correctly."""
        instance = self._make_one()
        instance.client = mock.Mock()
        series = [TimeSeries() for _ in range(num_series)]
        instance._batch_write("project", series, max_batch_size=batch_size)
        assert instance.client.create_service_time_series.call_count == expected_calls
        for i, call in enumerate(
            instance.client.create_service_time_series.call_args_list
        ):
            call_args, _ = call
            assert call_args[0].name == "projects/project"
            assert len(call_args[0].time_series) == expected_batch_sizes[i]

    def test__batch_write_with_deadline(self):
        """Test that _batch_write passes deadlines to gapic correctly."""
        import time

        from google.api_core import gapic_v1

        instance = self._make_one()
        instance.client = mock.Mock()
        series = [TimeSeries() for _ in range(10)]
        # test with deadline
        deadline = time.monotonic() + 10
        instance._batch_write("project", series, deadline=deadline)
        (
            call_args,
            call_kwargs,
        ) = instance.client.create_service_time_series.call_args_list[0]
        assert "timeout" in call_kwargs
        assert 9 < call_kwargs["timeout"] < 10
        # test without deadline
        instance.client.create_service_time_series.reset_mock()
        instance._batch_write("project", series, deadline=None)
        (
            call_args,
            call_kwargs,
        ) = instance.client.create_service_time_series.call_args_list[0]
        assert "timeout" in call_kwargs
        assert call_kwargs["timeout"] == gapic_v1.method.DEFAULT

    def test_export(self):
        """Test that export correctly converts metrics and calls _batch_write."""
        project_id = "project"
        instance = self._make_one()
        instance._batch_write = mock.Mock()
        # create mock metrics data
        expected_value = 123
        attributes = {
            "resource_project": project_id,
            "resource_instance": "instance1",
            "resource_cluster": "cluster1",
            "resource_table": "table1",
            "resource_zone": "zone1",
            "method": "ReadRows",
        }
        data_point = NumberDataPoint(
            attributes=attributes,
            start_time_unix_nano=100,
            time_unix_nano=200,
            value=expected_value,
        )
        metric = Metric(
            name="operation_latencies",
            description="",
            unit="ms",
            data=Sum(
                data_points=[data_point],
                aggregation_temporality=AggregationTemporality.CUMULATIVE,
                is_monotonic=False,
            ),
        )
        scope_metric = ScopeMetrics(
            scope=mock.Mock(), metrics=[metric], schema_url=None
        )
        resource_metric = ResourceMetrics(
            resource=mock.Mock(), scope_metrics=[scope_metric], schema_url=None
        )
        metrics_data = MetricsData(resource_metrics=[resource_metric])
        result = instance.export(metrics_data)
        assert result == MetricExportResult.SUCCESS
        instance._batch_write.assert_called_once()
        # check the TimeSeries passed to _batch_write
        call_args, call_kwargs = instance._batch_write.call_args_list[0]
        assert call_args[0] == project_id
        series_list = call_args[1]
        assert len(series_list) == 1
        series = series_list[0]
        assert series.metric.type == f"{instance.prefix}/operation_latencies"
        assert series.metric.labels["method"] == "ReadRows"
        assert "resource_instance" not in series.metric.labels
        assert series.resource.type == "bigtable_client_raw"
        assert series.resource.labels["project_id"] == project_id
        assert series.resource.labels["instance"] == "instance1"
        assert series.resource.labels["cluster"] == "cluster1"
        assert series.resource.labels["table"] == "table1"
        assert series.resource.labels["zone"] == "zone1"
        assert len(series.points) == 1
        point = series.points[0]
        assert point.value.int64_value == expected_value

    def test_export_no_attributes(self):
        """Test that export skips data points with no attributes."""
        instance = self._make_one()
        instance._batch_write = mock.Mock()
        data_point = NumberDataPoint(
            attributes={}, start_time_unix_nano=100, time_unix_nano=200, value=123
        )
        metric = Metric(
            name="operation_latencies",
            description="",
            unit="ms",
            data=Sum(
                data_points=[data_point],
                aggregation_temporality=AggregationTemporality.CUMULATIVE,
                is_monotonic=False,
            ),
        )
        scope_metric = ScopeMetrics(
            scope=mock.Mock(), metrics=[metric], schema_url=None
        )
        resource_metric = ResourceMetrics(
            resource=mock.Mock(), scope_metrics=[scope_metric], schema_url=None
        )
        metrics_data = MetricsData(resource_metrics=[resource_metric])
        result = instance.export(metrics_data)
        assert result == MetricExportResult.SUCCESS
        instance._batch_write.assert_not_called()

    def test_exception_in_export(self):
        """
        make sure exceptions don't raise
        """
        instance = self._make_one()
        instance._batch_write = mock.Mock(side_effect=Exception("test"))
        # create mock metrics data with one valid data point
        attributes = {
            "resource_project": "project",
            "resource_instance": "instance1",
            "resource_cluster": "cluster1",
            "resource_table": "table1",
            "resource_zone": "zone1",
        }
        data_point = NumberDataPoint(
            attributes=attributes,
            start_time_unix_nano=100,
            time_unix_nano=200,
            value=123,
        )
        metric = Metric(
            name="operation_latencies",
            description="",
            unit="ms",
            data=Sum(
                data_points=[data_point],
                aggregation_temporality=AggregationTemporality.CUMULATIVE,
                is_monotonic=False,
            ),
        )
        scope_metric = ScopeMetrics(
            scope=mock.Mock(), metrics=[metric], schema_url=None
        )
        resource_metric = ResourceMetrics(
            resource=mock.Mock(), scope_metrics=[scope_metric], schema_url=None
        )
        metrics_data = MetricsData(resource_metrics=[resource_metric])
        result = instance.export(metrics_data)
        assert result == MetricExportResult.FAILURE
        # generic errors may be transient; keep exporting on later intervals
        assert instance._disabled is False

    @staticmethod
    def _make_metrics_data(project_id="project"):
        """build a MetricsData object with one valid data point"""
        attributes = {
            "resource_project": project_id,
            "resource_instance": "instance1",
            "resource_cluster": "cluster1",
            "resource_table": "table1",
            "resource_zone": "zone1",
        }
        data_point = NumberDataPoint(
            attributes=attributes,
            start_time_unix_nano=100,
            time_unix_nano=200,
            value=123,
        )
        metric = Metric(
            name="operation_latencies",
            description="",
            unit="ms",
            data=Sum(
                data_points=[data_point],
                aggregation_temporality=AggregationTemporality.CUMULATIVE,
                is_monotonic=False,
            ),
        )
        scope_metric = ScopeMetrics(
            scope=mock.Mock(), metrics=[metric], schema_url=None
        )
        resource_metric = ResourceMetrics(
            resource=mock.Mock(), scope_metrics=[scope_metric], schema_url=None
        )
        return MetricsData(resource_metrics=[resource_metric])

    @pytest.mark.parametrize(
        "exc_type",
        [
            api_exceptions.Unauthenticated,
            api_exceptions.PermissionDenied,
        ],
    )
    def test_export_auth_error_disables_exporter(self, exc_type, caplog):
        """
        auth errors are not transient. The exporter should log a single, explanatory
        warning and stop exporting, without affecting the rest of the client
        """
        project_id = "my-project"
        exc = exc_type("Request had invalid authentication credentials.")
        instance = self._make_one()
        instance.client = mock.Mock()
        instance.client.create_service_time_series.side_effect = exc
        metrics_data = self._make_metrics_data(project_id)
        with caplog.at_level(logging.WARNING, logger=EXPORTER_LOGGER):
            result = instance.export(metrics_data)
        assert result == MetricExportResult.FAILURE
        assert instance._disabled is True
        assert instance.client.create_service_time_series.call_count == 1
        # one warning that explains the consequences
        warnings = [r for r in caplog.records if r.levelno == logging.WARNING]
        assert len(warnings) == 1
        message = warnings[0].getMessage()
        assert "Client-side metrics are now disabled" in message
        assert "Bigtable data operations are not affected" in message
        assert project_id in message
        assert "Request had invalid authentication credentials" in message
        # auth failures shouldn't dump a full traceback at warning level
        assert warnings[0].exc_info is None
        # later exports are skipped without touching the client or logging again
        caplog.clear()
        with caplog.at_level(logging.WARNING, logger=EXPORTER_LOGGER):
            result = instance.export(self._make_metrics_data(project_id))
        assert result == MetricExportResult.FAILURE
        assert instance.client.create_service_time_series.call_count == 1
        assert not caplog.records

    def test_export_when_disabled(self):
        """a disabled exporter should not attempt to convert or write metrics"""
        instance = self._make_one()
        instance._disabled = True
        instance._batch_write = mock.Mock()
        with mock.patch.object(instance, "_to_point") as to_point_mock:
            result = instance.export(self._make_metrics_data())
        assert result == MetricExportResult.FAILURE
        to_point_mock.assert_not_called()
        instance._batch_write.assert_not_called()

    @staticmethod
    def _make_sampling_period_error():
        return api_exceptions.FailedPrecondition(
            "One or more TimeSeries could not be written: One or more points "
            "were written more frequently than the maximum sampling period "
            "configured for the metric."
        )

    def test_export_failed_precondition_during_shutdown(self, caplog):
        """
        the final export triggered by shutdown is expected to be rejected for
        series written within the sampling period. That must not be logged as a
        warning, and must not disable the exporter
        """
        instance = self._make_one()
        instance.client = mock.Mock()
        instance.client.create_service_time_series.side_effect = (
            self._make_sampling_period_error()
        )
        instance.shutting_down = True
        with caplog.at_level(logging.DEBUG, logger=EXPORTER_LOGGER):
            result = instance.export(self._make_metrics_data())
        assert result == MetricExportResult.FAILURE
        assert instance._disabled is False
        assert instance.client.create_service_time_series.call_count == 1
        assert not [r for r in caplog.records if r.levelno >= logging.WARNING]
        debug_messages = [
            r.getMessage() for r in caplog.records if r.levelno == logging.DEBUG
        ]
        assert any("shutdown" in m and "sampling period" in m for m in debug_messages)

    def test_export_failed_precondition_while_running(self, caplog):
        """outside of shutdown, FAILED_PRECONDITION is still a warning"""
        instance = self._make_one()
        instance.client = mock.Mock()
        instance.client.create_service_time_series.side_effect = (
            self._make_sampling_period_error()
        )
        with caplog.at_level(logging.WARNING, logger=EXPORTER_LOGGER):
            result = instance.export(self._make_metrics_data())
        assert result == MetricExportResult.FAILURE
        assert instance._disabled is False
        warnings = [r for r in caplog.records if r.levelno == logging.WARNING]
        assert len(warnings) == 1
        assert "sampling period" in warnings[0].getMessage()
