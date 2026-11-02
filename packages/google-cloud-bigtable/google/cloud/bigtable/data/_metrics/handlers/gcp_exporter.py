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

from __future__ import annotations

import logging
import time
from collections import defaultdict

import google.auth.credentials
from google.api.distribution_pb2 import Distribution
from google.api.metric_pb2 import Metric as GMetric
from google.api.metric_pb2 import MetricDescriptor
from google.api.monitored_resource_pb2 import MonitoredResource
from google.api_core import gapic_v1
from google.api_core.exceptions import (
    FailedPrecondition,
    PermissionDenied,
    Unauthenticated,
)
from google.cloud.monitoring_v3 import (
    CreateTimeSeriesRequest,
    MetricServiceClient,
    Point,
    TimeInterval,
    TimeSeries,
    TypedValue,
)
from google.protobuf.timestamp_pb2 import Timestamp
from opentelemetry.sdk.metrics import MeterProvider, view
from opentelemetry.sdk.metrics.export import (
    ExponentialHistogramDataPoint,
    HistogramDataPoint,
    MetricExporter,
    MetricExportResult,
    MetricsData,
    NumberDataPoint,
    PeriodicExportingMetricReader,
)
from opentelemetry.util.types import Attributes

from google.cloud.bigtable.data._metrics.handlers.opentelemetry import (
    OpenTelemetryMetricsHandler,
    _OpenTelemetryInstruments,
)

_LOGGER = logging.getLogger(__name__)

# create OpenTelemetry views for Bigtable metrics
# avoid reformatting into individual lines
# fmt: off
MILLIS_AGGREGATION = view.ExplicitBucketHistogramAggregation(
    [
        0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9,
        1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9,
        2, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9,
        3, 4, 5, 6, 8, 10, 13, 16, 20, 25, 30, 40, 50,
        65, 80, 100, 130, 160, 200, 250, 300, 400, 500,
        650, 800, 900, 1_000, 2_000, 3_000, 4_000,
        5_000, 6_000, 10_000, 20_000, 50_000,
        100_000, 200_000, 500_000,
        1_000_000, 2_000_000, 5_000_000,
    ]
)
# fmt: on
COUNT_AGGREGATION = view.SumAggregation()
INSTRUMENT_NAMES = (
    "operation_latencies",
    "first_response_latencies",
    "attempt_latencies",
    "retry_count",
    "server_latencies",
    "connectivity_error_count",
    "application_latencies",
    "throttling_latencies",
)
VIEW_LIST = [
    view.View(
        instrument_name=n,
        name=n,
        aggregation=MILLIS_AGGREGATION
        if n.endswith("latencies")
        else COUNT_AGGREGATION,
    )
    for n in INSTRUMENT_NAMES
]

# Maps OpenTelemetry data point resource attribute names to Cloud Monitoring MonitoredResource label names
_RESOURCE_KEY_MAP = {
    "resource_project": "project_id",
    "resource_instance": "instance",
    "resource_cluster": "cluster",
    "resource_table": "table",
    "resource_zone": "zone",
}


def _partition_attributes(
    attributes: Attributes,
) -> tuple[dict[str, str], dict[str, str]]:
    """Split data point attributes into monitored resource labels and metric labels."""
    resource_labels = {label_name: "" for label_name in _RESOURCE_KEY_MAP.values()}
    metric_labels = {}
    if attributes:
        for attr_key, attr_value in attributes.items():
            if attr_key in _RESOURCE_KEY_MAP:
                resource_labels[_RESOURCE_KEY_MAP[attr_key]] = str(attr_value)
            elif not attr_key.startswith("resource_"):
                metric_labels[attr_key] = str(attr_value)
    return resource_labels, metric_labels


# scope required to call CreateServiceTimeSeries
_MONITORING_WRITE_SCOPE = "https://www.googleapis.com/auth/monitoring.write"
# any one of these scopes is sufficient to write metrics to Cloud Monitoring
_MONITORING_SCOPES = frozenset(
    {
        "https://www.googleapis.com/auth/cloud-platform",
        "https://www.googleapis.com/auth/monitoring",
        _MONITORING_WRITE_SCOPE,
    }
)


def _get_monitoring_credentials(
    credentials: google.auth.credentials.Credentials | None,
) -> google.auth.credentials.Credentials | None:
    """
    Return credentials that are able to authenticate against Cloud Monitoring.

    The metrics exporter shares the credentials of the Bigtable client it belongs to.
    If those credentials are already pinned to a fixed set of scopes that doesn't
    cover Cloud Monitoring (for example, credentials created by the legacy
    ``google.cloud.bigtable.Client``, which only requests Bigtable scopes),
    ``MetricServiceClient`` can't add its own default scopes to them, and every
    export would be rejected as UNAUTHENTICATED. In that case, a copy of the
    credentials scoped to ``monitoring.write`` is returned instead. The original
    credentials object (and the scopes used for Bigtable traffic) are left untouched.

    Credentials that don't support scoping (e.g. end-user credentials), or that still
    accept default scopes, are returned unchanged.

    Args:
        credentials: the credentials used by the Bigtable client, or None to use
            application default credentials
    Returns:
        credentials suitable for the Cloud Monitoring client
    """
    if credentials is None:
        return None
    if (
        isinstance(credentials, google.auth.credentials.Scoped)
        and not credentials.requires_scopes
        and not _MONITORING_SCOPES.intersection(credentials.scopes or ())
    ):
        return credentials.with_scopes([_MONITORING_WRITE_SCOPE])
    return credentials


class GoogleCloudMetricsHandler(OpenTelemetryMetricsHandler):
    """
    Maintains an internal set of OpenTelemetry metrics for the Bigtable client library,
    and periodically exports them to Google Cloud Monitoring.

    The OpenTelemetry metrics that are tracked are as follows:
      - operation_latencies: latency of each client method call, over all of it's attempts.
      - first_response_latencies: latency of receiving the first row in a ReadRows operation.
      - attempt_latencies: latency of each client attempt RPC.
      - retry_count: Number of additional RPCs sent after the initial attempt.
      - server_latencies: latency recorded on the server side for each attempt.
      - connectivity_error_count: number of attempts that failed to reach Google's network.
      - application_latencies: the time spent waiting for the application to process the next response.
      - throttling_latencies: latency introduced by waiting when there are too many outstanding requests in a bulk operation.

    Args:
        exporter: The exporter object used to write metrics to Cloud Montitoring.
            Should correspond 1:1 with a bigtable client, and share auth configuration
        export_interval: The interval (in seconds) at which to export metrics to Cloud Monitoring.
        *args: configuration positional arguments passed down to super class
        *kwargs: configuration keyword arguments passed down to super class
    """

    def __init__(self, exporter, *args, export_interval=60, **kwargs):
        self._exporter = exporter
        # periodically executes exporter
        gcp_reader = PeriodicExportingMetricReader(
            exporter, export_interval_millis=export_interval * 1000
        )
        # use private meter provider to store instruments and views
        self.meter_provider = MeterProvider(
            metric_readers=[gcp_reader], views=VIEW_LIST
        )
        otel = _OpenTelemetryInstruments(meter_provider=self.meter_provider)
        super().__init__(*args, instruments=otel, **kwargs)

    def close(self):
        self._exporter.shutting_down = True
        self.meter_provider.shutdown()


class BigtableMetricsExporter(MetricExporter):
    """
    OpenTelemetry Exporter implementation for sending metrics to Google Cloud Monitoring.

    We must use a custom exporter because the public one doesn't support writing to internal
    metrics like `bigtable.googleapis.com/internal/client/`

    Each GoogleCloudMetricsHandler will maintain its own exporter instance.
    """

    def __init__(self, *client_args, **client_kwargs):
        super().__init__()
        if client_kwargs.get("credentials") is not None:
            # the exporter shares the Bigtable client's credentials. Make sure
            # they are able to authenticate against Cloud Monitoring
            client_kwargs["credentials"] = _get_monitoring_credentials(
                client_kwargs["credentials"]
            )
        self.client = MetricServiceClient(*client_args, **client_kwargs)
        self.prefix = "bigtable.googleapis.com/internal/client"
        # set after a non-retryable authentication/authorization failure.
        # Once disabled, exports are skipped instead of failing (and logging)
        # on every export interval
        self._disabled = False
        self.shutting_down = False

    def export(
        self, metrics_data: MetricsData, timeout_millis: float = 10_000, **kwargs
    ) -> MetricExportResult:
        """
        Write a set of metrics to Cloud Monitoring.
        This method is called by the OpenTelemetry SDK
        """
        if self._disabled:
            return MetricExportResult.FAILURE
        deadline = time.monotonic() + (timeout_millis / 1000)
        metric_kind = MetricDescriptor.MetricKind.CUMULATIVE
        series_by_project: dict[str, list[TimeSeries]] = defaultdict(list)
        # process each metric from OTel format into Cloud Monitoring format
        for resource_metric in metrics_data.resource_metrics:
            for scope_metric in resource_metric.scope_metrics:
                for metric in scope_metric.metrics:
                    for data_point in metric.data.data_points:
                        if data_point.attributes:
                            resource_labels, metric_labels = _partition_attributes(
                                data_point.attributes
                            )
                            project_id = resource_labels.get("project_id", "")
                            if not project_id:
                                _LOGGER.warning(
                                    "Missing resource_project attribute for metric %s",
                                    metric.name,
                                )
                                continue
                            monitored_resource = MonitoredResource(
                                type="bigtable_client_raw",
                                labels=resource_labels,
                            )
                            try:
                                point = self._to_point(data_point)
                            except Exception as e:
                                _LOGGER.warning(
                                    "Failed to convert data point for metric %s: %s",
                                    metric.name,
                                    e,
                                    exc_info=True,
                                )
                                continue
                            series = TimeSeries(
                                resource=monitored_resource,
                                metric_kind=metric_kind,
                                points=[point],
                                metric=GMetric(
                                    type=f"{self.prefix}/{metric.name}",
                                    labels=metric_labels,
                                ),
                                unit=metric.unit,
                            )
                            series_by_project[project_id].append(series)
        # send all metrics to Cloud Monitoring
        try:
            for project_id, series_list in series_by_project.items():
                _LOGGER.debug(
                    "Exporting %d time series to Cloud Monitoring for project %s",
                    len(series_list),
                    project_id,
                )
                self._batch_write(project_id, series_list, deadline)
            return MetricExportResult.SUCCESS
        except (Unauthenticated, PermissionDenied) as e:
            # authentication/authorization failures won't resolve on their own.
            # Stop exporting instead of failing again on every export interval
            self._disabled = True
            _LOGGER.warning(
                "Bigtable client-side metrics could not be exported to Cloud "
                "Monitoring for project(s) %s: %s. Client-side metrics are now "
                "disabled for this client; Bigtable data operations are not "
                "affected. To publish client-side metrics, make sure the Cloud "
                "Monitoring API is enabled and the client's credentials are "
                "allowed to write metrics to the project "
                "(e.g. roles/monitoring.metricWriter).",
                ", ".join(series_by_project),
                e,
            )
            _LOGGER.debug("Client-side metrics export failure details:", exc_info=True)
            return MetricExportResult.FAILURE
        except Exception as e:
            if self.shutting_down and isinstance(e, FailedPrecondition):
                # the final export on shutdown usually falls inside the sampling
                # period of the previous one, and is rejected. This is expected
                _LOGGER.debug("Final metrics export on shutdown rejected: %s", e)
            else:
                _LOGGER.warning(
                    "Failed to export metrics to Cloud Monitoring: %s", e, exc_info=True
                )
            return MetricExportResult.FAILURE

    def _batch_write(
        self,
        project_id: str,
        series: list[TimeSeries],
        deadline=None,
        max_batch_size=200,
    ) -> None:
        """
        Adapted from CloudMonitoringMetricsExporter
        https://github.com/GoogleCloudPlatform/opentelemetry-operations-python/blob/3668dfe7ce3b80dd01f42af72428de957b58b316/opentelemetry-exporter-gcp-monitoring/src/opentelemetry/exporter/cloud_monitoring/__init__.py#L82

        Args:
            project_id: GCP project ID to write metrics to
            series: list of TimeSeries to write. Will be split into batches if necessary
            deadline: designates the time.time() at which to stop writing. If None, uses API default
            max_batch_size: maximum number of time series to write at once.
                Cloud Monitoring allows up to 200 per request
        """
        write_ind = 0
        while write_ind < len(series):
            # find time left for next batch
            timeout = (
                max(0.0, deadline - time.monotonic())
                if deadline
                else gapic_v1.method.DEFAULT
            )
            # write next batch
            batch = series[write_ind : write_ind + max_batch_size]
            self.client.create_service_time_series(
                CreateTimeSeriesRequest(
                    name=f"projects/{project_id}",
                    time_series=batch,
                ),
                timeout=timeout,
            )
            _LOGGER.debug(
                "Successfully wrote batch of %d time series to projects/%s",
                len(batch),
                project_id,
            )
            write_ind += max_batch_size

    @staticmethod
    def _to_point(
        data_point: NumberDataPoint
        | HistogramDataPoint
        | ExponentialHistogramDataPoint,
    ) -> Point:
        """
        Adapted from CloudMonitoringMetricsExporter
        https://github.com/GoogleCloudPlatform/opentelemetry-operations-python/blob/3668dfe7ce3b80dd01f42af72428de957b58b316/opentelemetry-exporter-gcp-monitoring/src/opentelemetry/exporter/cloud_monitoring/__init__.py#L82
        """
        if isinstance(data_point, HistogramDataPoint):
            mean = data_point.sum / data_point.count if data_point.count else 0.0
            point_value = TypedValue(
                distribution_value=Distribution(
                    count=data_point.count,
                    mean=mean,
                    bucket_counts=data_point.bucket_counts,
                    bucket_options=Distribution.BucketOptions(
                        explicit_buckets=Distribution.BucketOptions.Explicit(
                            bounds=data_point.explicit_bounds,
                        )
                    ),
                )
            )
        elif isinstance(data_point, NumberDataPoint):
            if isinstance(data_point.value, int):
                point_value = TypedValue(int64_value=data_point.value)
            else:
                point_value = TypedValue(double_value=data_point.value)
        else:
            raise NotImplementedError(
                f"Unsupported OTel data point type: {type(data_point)}"
            )
        start_time = Timestamp()
        start_time.FromNanoseconds(data_point.start_time_unix_nano)
        end_time = Timestamp()
        end_time.FromNanoseconds(data_point.time_unix_nano)
        interval = TimeInterval(start_time=start_time, end_time=end_time)
        return Point(interval=interval, value=point_value)

    def shutdown(self, timeout_millis: float = 30_000, **kwargs):
        """
        Adapted from CloudMonitoringMetricsExporter
        https://github.com/GoogleCloudPlatform/opentelemetry-operations-python/blob/3668dfe7ce3b80dd01f42af72428de957b58b316/opentelemetry-exporter-gcp-monitoring/src/opentelemetry/exporter/cloud_monitoring/__init__.py#L82
        """
        pass

    def force_flush(self, timeout_millis: float = 10_000):
        """
        Adapted from CloudMonitoringMetricsExporter
        https://github.com/GoogleCloudPlatform/opentelemetry-operations-python/blob/3668dfe7ce3b80dd01f42af72428de957b58b316/opentelemetry-exporter-gcp-monitoring/src/opentelemetry/exporter/cloud_monitoring/__init__.py#L82
        """
        return True
