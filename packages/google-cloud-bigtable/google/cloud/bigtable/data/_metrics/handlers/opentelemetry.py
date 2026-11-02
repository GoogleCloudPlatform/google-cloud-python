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

import os
import socket
import uuid

from google.cloud.bigtable.data._metrics.data_model import (
    DEFAULT_CLUSTER_ID,
    DEFAULT_ZONE,
    ActiveOperationMetric,
    CompletedAttemptMetric,
    CompletedOperationMetric,
    OperationType,
)
from google.cloud.bigtable.data._metrics.handlers._base import MetricsHandler
from google.cloud.bigtable.gapic_version import __version__ as bigtable_version

# conversion factor for converting from nanoseconds to milliseconds
NS_TO_MS = 1e6


class _OpenTelemetryInstruments:
    """
    class that holds OpenTelelmetry instrument objects
    """

    def __init__(self, meter_provider=None):
        if meter_provider is None:
            # use global meter provider
            from opentelemetry import metrics

            meter_provider = metrics
        # grab meter for this module
        meter = meter_provider.get_meter("bigtable.googleapis.com")
        # create instruments
        self.operation_latencies = meter.create_histogram(
            name="operation_latencies",
            description="""
            The total end-to-end latency across all RPC attempts associated with a Bigtable operation.
            This metric measures an operation's round trip from the client to Bigtable and back to the client and includes all retries.

            For ReadRows requests, the operation latencies include the application processing time for each returned message.
            """,
            unit="ms",
        )
        self.first_response_latencies = meter.create_histogram(
            name="first_response_latencies",
            description="Latencies from when a client sends a request and receives the first row of the response.",
            unit="ms",
        )
        self.attempt_latencies = meter.create_histogram(
            name="attempt_latencies",
            description="""
            The latencies of a client RPC attempt.

            Under normal circumstances, this value is identical to operation_latencies.
            If the client receives transient errors, however, then operation_latencies is the sum of all attempt_latencies and the exponential delays.
            """,
            unit="ms",
        )
        self.retry_count = meter.create_counter(
            name="retry_count",
            description="""
            A counter that records the number of attempts that an operation required to complete.
            Under normal circumstances, this value is empty.
            """,
        )
        self.server_latencies = meter.create_histogram(
            name="server_latencies",
            description="Latencies between the time when the Google frontend receives an RPC and when it sends the first byte of the response.",
            unit="ms",
        )
        self.connectivity_error_count = meter.create_counter(
            name="connectivity_error_count",
            description="""
            The number of requests that failed to reach Google's network.
            In normal cases, this number is 0. When the number is not 0, it can indicate connectivity issues between the application and the Google network.
            """,
        )
        self.application_latencies = meter.create_histogram(
            name="application_latencies",
            description="""
            The time from when the client receives the response to a request until the application reads the response.
            This metric is most relevant for ReadRows requests.
            The start and stop times for this metric depend on the way that you send the read request; see Application blocking latencies timer examples for details.
            """,
            unit="ms",
        )
        self.throttling_latencies = meter.create_histogram(
            name="throttling_latencies",
            description="Latencies introduced when the client blocks the sending of more requests to the server because of too many pending requests in a bulk operation.",
            unit="ms",
        )


class OpenTelemetryMetricsHandler(MetricsHandler):
    """
    Maintains a set of OpenTelemetry metrics for the Bigtable client library,
    and updates them with each completed operation and attempt.

    The OpenTelemetry metrics that are tracked are as follows:
      - operation_latencies: latency of each client method call, over all of it's attempts.
      - first_response_latencies: latency of receiving the first row in a ReadRows operation.
      - attempt_latencies: latency of each client attempt RPC.
      - retry_count: Number of additional RPCs sent after the initial attempt.
      - server_latencies: latency recorded on the server side for each attempt.
      - connectivity_error_count: number of attempts that failed to reach Google's network.
      - application_latencies: the time spent waiting for the application to process the next response.
      - throttling_latencies: latency introduced by waiting when there are too many outstanding requests in a bulk operation.
    """

    def __init__(
        self,
        *,
        client_uid: str | None = None,
        client_version: str | None = None,
        instruments: _OpenTelemetryInstruments | None = None,
    ):
        super().__init__()
        self.otel = instruments or _OpenTelemetryInstruments()
        client_version = client_version or bigtable_version
        # fixed labels sent with each metric update
        self.shared_labels = {
            "client_name": f"python-bigtable/{client_version}",
            "client_uid": client_uid or self._generate_client_uid(),
        }

    def _get_operation_labels(
        self, op: ActiveOperationMetric | CompletedOperationMetric
    ) -> dict[str, str]:
        project_id = getattr(op, "project_id", None)
        instance_id = getattr(op, "instance_id", None)
        table_id = getattr(op, "table_id", None)
        app_profile = getattr(op, "app_profile_id", None) or "default"
        operation_labels = {
            "resource_project": project_id,
            "resource_instance": instance_id,
            "resource_table": table_id,
            "app_profile": app_profile,
        }
        return {
            **self.shared_labels,
            **{k: v for k, v in operation_labels.items() if v},
        }

    @staticmethod
    def _generate_client_uid():
        """
        client_uid will take the format `python-<uuid><pid>@<hostname>` where uuid is a
        random value, pid is the process id, and hostname is the hostname of the machine.

        If not found, localhost will be used in place of hostname, and a random number
        will be used in place of pid.
        """
        try:
            hostname = socket.gethostname() or "localhost"
        except Exception:
            hostname = "localhost"
        try:
            pid = os.getpid() or ""
        except Exception:
            pid = ""
        return f"python-{uuid.uuid4()}-{pid}@{hostname}"

    def on_operation_complete(self, op: CompletedOperationMetric) -> None:
        """
        Update the metrics associated with a completed operation:
          - operation_latencies
          - retry_count
          - first_response_latencies
          - throttling_latencies
        """
        labels = {
            "method": op.op_type.value,
            "resource_zone": op.zone,
            "resource_cluster": op.cluster_id,
            **self._get_operation_labels(op),
        }
        status = op.final_status.name
        is_streaming = str(op.is_streaming)

        self.otel.operation_latencies.record(
            op.duration_ns / NS_TO_MS,
            {"streaming": is_streaming, "status": status, **labels},
        )
        if (
            op.op_type == OperationType.READ_ROWS
            and op.first_response_latency_ns is not None
        ):
            self.otel.first_response_latencies.record(
                op.first_response_latency_ns / NS_TO_MS, {"status": status, **labels}
            )
        # only record completed attempts if there were retries
        if op.completed_attempts:
            self.otel.retry_count.add(
                len(op.completed_attempts) - 1, {"status": status, **labels}
            )
        if (
            op.op_type == OperationType.BULK_MUTATE_ROWS
            and op.flow_throttling_time_ns > 0
        ):
            # throttling happens before any attempt is made, so this metric
            # has no status label
            self.otel.throttling_latencies.record(
                op.flow_throttling_time_ns / NS_TO_MS, labels
            )

    def on_attempt_complete(
        self, attempt: CompletedAttemptMetric, op: ActiveOperationMetric
    ):
        """
        Update the metrics associated with a completed attempt:
          - attempt_latencies
          - server_latencies
          - connectivity_error_count
          - application_latencies
        """
        labels = {
            "method": op.op_type.value,
            "resource_zone": op.zone or DEFAULT_ZONE,  # fallback to default if unset
            "resource_cluster": op.cluster_id or DEFAULT_CLUSTER_ID,
            **self._get_operation_labels(op),
        }
        status = attempt.end_status.name
        is_streaming = str(op.is_streaming)

        self.otel.attempt_latencies.record(
            attempt.duration_ns / NS_TO_MS,
            {"streaming": is_streaming, "status": status, **labels},
        )
        self.otel.application_latencies.record(
            attempt.application_blocking_time_ns / NS_TO_MS,
            labels,
        )
        if attempt.gfe_latency_ns is not None:
            self.otel.server_latencies.record(
                attempt.gfe_latency_ns / NS_TO_MS,
                {"streaming": is_streaming, "status": status, **labels},
            )
        else:
            # gfe headers not attached. Record a connectivity error.
            # TODO: this should not be recorded as an error when direct path is enabled
            self.otel.connectivity_error_count.add(1, {"status": status, **labels})
