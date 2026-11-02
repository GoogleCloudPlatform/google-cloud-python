# Copyright 2017, Google LLC All rights reserved.
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

import sys
from datetime import datetime
from typing import Optional

from opentelemetry import trace
from opentelemetry.trace.propagation import set_span_in_context
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator

from google.cloud.pubsub_v1.open_telemetry.context_propagation import (
    OpenTelemetryContextSetter,
)
from google.pubsub_v1 import types as gapic_types


class PublishMessageWrapper:
    _OPEN_TELEMETRY_TRACER_NAME: str = "google.cloud.pubsub_v1"
    _OPEN_TELEMETRY_MESSAGING_SYSTEM: str = "gcp_pubsub"
    _OPEN_TELEMETRY_PUBLISHER_BATCHING = "publisher batching"

    _PUBLISH_START_EVENT: str = "publish start"
    _PUBLISH_FLOW_CONTROL: str = "publisher flow control"

    def __init__(self, message: gapic_types.PubsubMessage):
        self._message: gapic_types.PubsubMessage = message
        self._create_span: Optional[trace.Span] = None
        self._flow_control_span: Optional[trace.Span] = None
        self._batching_span: Optional[trace.Span] = None

    @property
    def message(self):
        return self._message

    @message.setter  # type: ignore[no-redef]  # resetting message value is intentional here
    def message(self, message: gapic_types.PubsubMessage):
        self._message = message

    @property
    def create_span(self):
        return self._create_span

    def __eq__(self, other):  # pragma: NO COVER
        """Used for pytest asserts to compare two PublishMessageWrapper objects with the same message"""
        if isinstance(self, other.__class__):
            return self.message == other.message
        return False

    def start_create_span(self, topic: str, ordering_key: str) -> None:
        tracer = trace.get_tracer(self._OPEN_TELEMETRY_TRACER_NAME)
        assert len(topic.split("/")) == 4
        topic_short_name = topic.split("/")[3]
        with (
            tracer.start_as_current_span(
                name=f"{topic_short_name} create",
                attributes={
                    "messaging.system": self._OPEN_TELEMETRY_MESSAGING_SYSTEM,
                    "messaging.destination.name": topic_short_name,
                    "code.function": "publish",
                    "messaging.gcp_pubsub.message.ordering_key": ordering_key,
                    "messaging.operation": "create",
                    "gcp.project_id": topic.split("/")[1],
                    "messaging.message.body.size": sys.getsizeof(
                        self._message.data
                    ),  # sys.getsizeof() used since the attribute expects size of message body in bytes
                },
                kind=trace.SpanKind.PRODUCER,
                end_on_exit=False,
            ) as create_span
        ):
            create_span.add_event(
                name=self._PUBLISH_START_EVENT,
                attributes={
                    "timestamp": str(datetime.now()),
                },
            )
            self._create_span = create_span
            TraceContextTextMapPropagator().inject(
                carrier=self._message,
                setter=OpenTelemetryContextSetter(),
            )

    def end_create_span(self, exc: Optional[BaseException] = None) -> None:
        assert self._create_span is not None
        if exc:
            self._create_span.record_exception(exception=exc)
            self._create_span.set_status(
                trace.Status(status_code=trace.StatusCode.ERROR)
            )
        self._create_span.end()

    def start_publisher_flow_control_span(self) -> None:
        tracer = trace.get_tracer(self._OPEN_TELEMETRY_TRACER_NAME)
        assert self._create_span is not None
        with tracer.start_as_current_span(
            name=self._PUBLISH_FLOW_CONTROL,
            kind=trace.SpanKind.INTERNAL,
            context=set_span_in_context(self._create_span),
            end_on_exit=False,
        ) as flow_control_span:
            self._flow_control_span = flow_control_span

    def end_publisher_flow_control_span(
        self, exc: Optional[BaseException] = None
    ) -> None:
        assert self._flow_control_span is not None
        if exc:
            self._flow_control_span.record_exception(exception=exc)
            self._flow_control_span.set_status(
                trace.Status(status_code=trace.StatusCode.ERROR)
            )
        self._flow_control_span.end()

    def start_publisher_batching_span(self) -> None:
        assert self._create_span is not None
        tracer = trace.get_tracer(self._OPEN_TELEMETRY_TRACER_NAME)
        with tracer.start_as_current_span(
            name=self._OPEN_TELEMETRY_PUBLISHER_BATCHING,
            kind=trace.SpanKind.INTERNAL,
            context=set_span_in_context(self._create_span),
            end_on_exit=False,
        ) as batching_span:
            self._batching_span = batching_span

    def end_publisher_batching_span(self, exc: Optional[BaseException] = None) -> None:
        assert self._batching_span is not None
        if exc:
            self._batching_span.record_exception(exception=exc)
            self._batching_span.set_status(
                trace.Status(status_code=trace.StatusCode.ERROR)
            )
        self._batching_span.end()
