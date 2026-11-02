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
import mock
import pytest
from grpc import StatusCode

from google.cloud.bigtable.data._metrics.data_model import (
    ActiveOperationMetric,
    CompletedAttemptMetric,
    CompletedOperationMetric,
    OperationType,
)
from google.cloud.bigtable.data._metrics.handlers.opentelemetry import (
    OpenTelemetryMetricsHandler,
    _OpenTelemetryInstruments,
)


class TestOpentelemetryInstruments:
    EXPECTED_METRICS = [
        "operation_latencies",
        "first_response_latencies",
        "attempt_latencies",
        "server_latencies",
        "application_latencies",
        "throttling_latencies",
        "retry_count",
        "connectivity_error_count",
    ]

    def _make_one(self, meter_provider=None):
        return _OpenTelemetryInstruments(meter_provider)

    def test_meter_name(self):
        expected_name = "bigtable.googleapis.com"
        mock_meter_provider = mock.Mock()
        self._make_one(mock_meter_provider)
        mock_meter_provider.get_meter.assert_called_once_with(expected_name)

    @pytest.mark.parametrize(
        "metric_name", [m for m in EXPECTED_METRICS if "latencies" in m]
    )
    def test_histogram_creation(self, metric_name):
        mock_meter_provider = mock.Mock()
        instruments = self._make_one(mock_meter_provider)
        mock_meter = mock_meter_provider.get_meter()
        assert any(
            [
                call.kwargs["name"] == metric_name
                for call in mock_meter.create_histogram.call_args_list
            ]
        )
        assert all(
            [
                call.kwargs["unit"] == "ms"
                for call in mock_meter.create_histogram.call_args_list
            ]
        )
        assert all(
            [
                call.kwargs["description"] is not None
                for call in mock_meter.create_histogram.call_args_list
            ]
        )
        assert getattr(instruments, metric_name) is not None

    @pytest.mark.parametrize(
        "metric_name", [m for m in EXPECTED_METRICS if "count" in m]
    )
    def test_counter_creation(self, metric_name):
        mock_meter_provider = mock.Mock()
        instruments = self._make_one(mock_meter_provider)
        mock_meter = mock_meter_provider.get_meter()
        assert any(
            [
                call.kwargs["name"] == metric_name
                for call in mock_meter.create_counter.call_args_list
            ]
        )
        assert all(
            [
                call.kwargs["description"] is not None
                for call in mock_meter.create_histogram.call_args_list
            ]
        )
        assert getattr(instruments, metric_name) is not None

    def test_global_provider(self):
        instruments = self._make_one()
        # wait to import otel until after creating instance
        import opentelemetry

        for metric_name in self.EXPECTED_METRICS:
            metric = getattr(instruments, metric_name)
            assert metric is not None
            if "latencies" in metric_name:
                assert isinstance(metric, opentelemetry.metrics.Histogram)
            else:
                assert isinstance(metric, opentelemetry.metrics.Counter)


class TestOpentelemetryMetricsHandler:
    def _make_one(self, **kwargs):
        return OpenTelemetryMetricsHandler(**kwargs)

    def test_ctor_defaults(self):
        from google.cloud.bigtable import __version__ as CLIENT_VERSION

        with mock.patch.object(
            OpenTelemetryMetricsHandler, "_generate_client_uid"
        ) as uid_mock:
            handler = self._make_one()
        assert isinstance(handler.otel, _OpenTelemetryInstruments)
        assert (
            handler.shared_labels["client_name"] == f"python-bigtable/{CLIENT_VERSION}"
        )
        assert handler.shared_labels["client_uid"] == uid_mock()

    def test_ctor_explicit(self):
        expected_version = "my_version"
        expected_uid = "my_uid"
        expected_instruments = object()
        handler = self._make_one(
            client_uid=expected_uid,
            client_version=expected_version,
            instruments=expected_instruments,
        )
        assert handler.otel == expected_instruments
        assert (
            handler.shared_labels["client_name"]
            == f"python-bigtable/{expected_version}"
        )
        assert handler.shared_labels["client_uid"] == expected_uid

    @mock.patch("socket.gethostname", return_value="hostname")
    @mock.patch("os.getpid", return_value="pid")
    @mock.patch("uuid.uuid4", return_value="uid")
    def test_generate_client_uid_mock(self, socket_mock, os_mock, uuid_mock):
        uid = OpenTelemetryMetricsHandler._generate_client_uid()
        assert uid == "python-uid-pid@hostname"

    @mock.patch("socket.gethostname", side_effect=[ValueError("fail")])
    @mock.patch("os.getpid", side_effect=[ValueError("fail")])
    @mock.patch("uuid.uuid4", return_value="uid")
    def test_generate_client_uid_mock_with_exceptions(
        self, socket_mock, os_mock, uuid_mock
    ):
        uid = OpenTelemetryMetricsHandler._generate_client_uid()
        assert uid == "python-uid-@localhost"

    def test_generate_client_uid(self):
        import re

        uid = OpenTelemetryMetricsHandler._generate_client_uid()
        # The expected pattern is python-<uuid>-<pid>@<hostname>
        expected_pattern = (
            r"python-[\da-f]{8}-[\da-f]{4}-[\da-f]{4}-[\da-f]{4}-[\da-f]{12}-\d+@.+"
        )
        assert re.match(expected_pattern, uid)

    def test_on_operation_complete_operation_latencies(self):
        mock_instruments = mock.Mock(operation_latencies=mock.Mock())
        handler = self._make_one(instruments=mock_instruments)
        op = CompletedOperationMetric(
            op_type=OperationType.READ_ROWS,
            duration_ns=1234567,
            completed_attempts=[],
            final_status=StatusCode.OK,
            cluster_id="cluster",
            zone="zone",
            is_streaming=True,
        )
        handler.on_operation_complete(op)
        expected_labels = {
            "method": op.op_type.value,
            "status": op.final_status.name,
            "resource_zone": op.zone,
            "resource_cluster": op.cluster_id,
            "app_profile": "default",
            **handler.shared_labels,
        }
        mock_instruments.operation_latencies.record.assert_called_once_with(
            op.duration_ns / 1e6,
            {"streaming": str(op.is_streaming), **expected_labels},
        )

    def test_on_operation_complete_dynamic_labels(self):
        mock_instruments = mock.Mock(operation_latencies=mock.Mock())
        handler = self._make_one(instruments=mock_instruments)
        op = CompletedOperationMetric(
            op_type=OperationType.READ_ROWS,
            duration_ns=1234567,
            completed_attempts=[],
            final_status=StatusCode.OK,
            cluster_id="cluster",
            zone="zone",
            is_streaming=True,
            instance_id="dynamic_inst",
            table_id="dynamic_table",
            app_profile_id="dynamic_app",
        )
        handler.on_operation_complete(op)
        expected_labels = {
            "method": op.op_type.value,
            "status": op.final_status.name,
            "resource_zone": op.zone,
            "resource_cluster": op.cluster_id,
            "resource_instance": "dynamic_inst",
            "resource_table": "dynamic_table",
            "app_profile": "dynamic_app",
            **handler.shared_labels,
        }
        mock_instruments.operation_latencies.record.assert_called_once_with(
            op.duration_ns / 1e6,
            {"streaming": str(op.is_streaming), **expected_labels},
        )

    @pytest.mark.parametrize(
        "op_type,first_response_latency_ns,should_record",
        [
            (OperationType.READ_ROWS, 12345, True),
            (OperationType.READ_ROWS, None, False),
            (OperationType.MUTATE_ROW, 12345, False),
        ],
    )
    def test_on_operation_complete_first_response_latencies(
        self, op_type, first_response_latency_ns, should_record
    ):
        mock_instruments = mock.Mock(first_response_latencies=mock.Mock())
        handler = self._make_one(instruments=mock_instruments)
        op = CompletedOperationMetric(
            op_type=op_type,
            duration_ns=1234567,
            completed_attempts=[],
            final_status=StatusCode.OK,
            cluster_id="cluster",
            zone="zone",
            is_streaming=True,
            first_response_latency_ns=first_response_latency_ns,
        )
        handler.on_operation_complete(op)
        if should_record:
            expected_labels = {
                "method": op.op_type.value,
                "status": op.final_status.name,
                "resource_zone": op.zone,
                "resource_cluster": op.cluster_id,
                "app_profile": "default",
                **handler.shared_labels,
            }
            mock_instruments.first_response_latencies.record.assert_called_once_with(
                first_response_latency_ns / 1e6, expected_labels
            )
        else:
            mock_instruments.first_response_latencies.record.assert_not_called()

    @pytest.mark.parametrize("attempts_count", [0, 1, 5])
    def test_on_operation_complete_retry_count(self, attempts_count):
        mock_instruments = mock.Mock(retry_count=mock.Mock())
        handler = self._make_one(instruments=mock_instruments)
        attempts = [mock.Mock()] * attempts_count
        op = CompletedOperationMetric(
            op_type=OperationType.READ_ROWS,
            duration_ns=1234567,
            completed_attempts=attempts,
            final_status=StatusCode.OK,
            cluster_id="cluster",
            zone="zone",
            is_streaming=True,
        )
        handler.on_operation_complete(op)
        if attempts:
            expected_labels = {
                "method": op.op_type.value,
                "status": op.final_status.name,
                "resource_zone": op.zone,
                "resource_cluster": op.cluster_id,
                "app_profile": "default",
                **handler.shared_labels,
            }
            mock_instruments.retry_count.add.assert_called_once_with(
                len(attempts) - 1, expected_labels
            )
        else:
            mock_instruments.retry_count.add.assert_not_called()

    def test_on_attempt_complete_attempt_latencies(self):
        mock_instruments = mock.Mock(attempt_latencies=mock.Mock())
        handler = self._make_one(instruments=mock_instruments)
        attempt = CompletedAttemptMetric(duration_ns=1234567, end_status=StatusCode.OK)
        op = ActiveOperationMetric(
            op_type=OperationType.READ_ROWS,
            zone="zone",
            cluster_id="cluster",
            is_streaming=True,
        )
        handler.on_attempt_complete(attempt, op)
        expected_labels = {
            "method": op.op_type.value,
            "resource_zone": op.zone,
            "resource_cluster": op.cluster_id,
            "app_profile": "default",
            **handler.shared_labels,
        }
        mock_instruments.attempt_latencies.record.assert_called_once_with(
            attempt.duration_ns / 1e6,
            {
                "streaming": str(op.is_streaming),
                "status": attempt.end_status.name,
                **expected_labels,
            },
        )

    @pytest.mark.parametrize(
        "op_type,flow_throttling_ns,should_record",
        [
            (OperationType.BULK_MUTATE_ROWS, 54321, True),
            (OperationType.BULK_MUTATE_ROWS, 0, False),
            (OperationType.READ_ROWS, 54321, False),
        ],
    )
    def test_on_operation_complete_throttling_latencies(
        self, op_type, flow_throttling_ns, should_record
    ):
        mock_instruments = mock.Mock(throttling_latencies=mock.Mock())
        handler = self._make_one(instruments=mock_instruments)
        op = CompletedOperationMetric(
            op_type=op_type,
            duration_ns=1234567,
            completed_attempts=[],
            final_status=StatusCode.OK,
            cluster_id="cluster",
            zone="zone",
            is_streaming=False,
            flow_throttling_time_ns=flow_throttling_ns,
        )
        handler.on_operation_complete(op)
        if should_record:
            # throttling_latencies must not carry a status label; Cloud Monitoring
            # rejects the series with "unrecognized metric labels [status]".
            expected_labels = {
                "method": op.op_type.value,
                "resource_zone": op.zone,
                "resource_cluster": op.cluster_id,
                "app_profile": "default",
                **handler.shared_labels,
            }
            mock_instruments.throttling_latencies.record.assert_called_once_with(
                pytest.approx(flow_throttling_ns / 1e6), expected_labels
            )
        else:
            mock_instruments.throttling_latencies.record.assert_not_called()

    def test_on_attempt_complete_application_latencies(self):
        mock_instruments = mock.Mock(application_latencies=mock.Mock())
        handler = self._make_one(instruments=mock_instruments)
        attempt = CompletedAttemptMetric(
            duration_ns=1234567,
            end_status=StatusCode.OK,
            application_blocking_time_ns=234567,
            backoff_before_attempt_ns=345678,
        )
        op = ActiveOperationMetric(op_type=OperationType.READ_ROWS)
        handler.on_attempt_complete(attempt, op)
        mock_instruments.application_latencies.record.assert_called_once_with(
            attempt.application_blocking_time_ns / 1e6,
            mock.ANY,
        )

    @pytest.mark.parametrize(
        "gfe_latency_ns,should_record_server_latency",
        [(12345, True), (None, False), (0, True)],
    )
    def test_on_attempt_complete_server_latencies_and_connectivity_error(
        self, gfe_latency_ns, should_record_server_latency
    ):
        mock_instruments = mock.Mock(
            server_latencies=mock.Mock(), connectivity_error_count=mock.Mock()
        )
        handler = self._make_one(instruments=mock_instruments)
        attempt = CompletedAttemptMetric(
            duration_ns=1234567,
            end_status=StatusCode.OK,
            gfe_latency_ns=gfe_latency_ns,
        )
        op = ActiveOperationMetric(
            op_type=OperationType.READ_ROWS,
            zone="zone",
            cluster_id="cluster",
            is_streaming=True,
        )
        handler.on_attempt_complete(attempt, op)
        if should_record_server_latency:
            mock_instruments.server_latencies.record.assert_called_once_with(
                gfe_latency_ns / 1e6, mock.ANY
            )
            mock_instruments.connectivity_error_count.add.assert_not_called()
        else:
            mock_instruments.server_latencies.record.assert_not_called()
            mock_instruments.connectivity_error_count.add.assert_called_once_with(
                1, mock.ANY
            )
