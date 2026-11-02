# Copyright 2024, Google LLC All rights reserved.
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

from datetime import datetime
from typing import List, Optional

from opentelemetry import context, trace
from opentelemetry.trace.propagation import set_span_in_context
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator

from google.cloud.pubsub_v1.open_telemetry.context_propagation import (
    OpenTelemetryContextGetter,
)
from google.pubsub_v1.types import PubsubMessage

_OPEN_TELEMETRY_TRACER_NAME: str = "google.cloud.pubsub_v1"
_OPEN_TELEMETRY_MESSAGING_SYSTEM: str = "gcp_pubsub"


class SubscribeOpenTelemetry:
    def __init__(self, message: PubsubMessage):
        self._message: PubsubMessage = message

        # subscribe span will be initialized by the `start_subscribe_span`
        # method.
        self._subscribe_span: Optional[trace.Span] = None

        # subscriber concurrency control span will be initialized by the
        # `start_subscribe_concurrency_control_span` method.
        self._concurrency_control_span: Optional[trace.Span] = None

        # scheduler span will be initialized by the
        # `start_subscribe_scheduler_span` method.
        self._scheduler_span: Optional[trace.Span] = None

        # This will be set by `start_subscribe_span` method and will be used
        # for other spans, such as process span.
        self._subscription_id: Optional[str] = None

        # This will be set by `start_process_span` method.
        self._process_span: Optional[trace.Span] = None

        # This will be set by `start_subscribe_span` method, if a publisher create span
        # context was extracted from trace propagation. And will be used by spans like
        # proces span to add links to the publisher create span.
        self._publisher_create_span_context: Optional[context.Context] = None

        # This will be set by `start_subscribe_span` method and will be used
        # for other spans, such as modack span.
        self._project_id: Optional[str] = None

    @property
    def subscription_id(self) -> Optional[str]:
        return self._subscription_id

    @property
    def project_id(self) -> Optional[str]:
        return self._project_id

    @property
    def subscribe_span(self) -> Optional[trace.Span]:
        return self._subscribe_span

    def start_subscribe_span(
        self,
        subscription: str,
        exactly_once_enabled: bool,
        ack_id: str,
        delivery_attempt: int,
    ) -> None:
        tracer = trace.get_tracer(_OPEN_TELEMETRY_TRACER_NAME)
        parent_span_context = TraceContextTextMapPropagator().extract(
            carrier=self._message,
            getter=OpenTelemetryContextGetter(),
        )
        self._publisher_create_span_context = parent_span_context
        split_subscription: List[str] = subscription.split("/")
        assert len(split_subscription) == 4
        subscription_short_name = split_subscription[3]
        self._project_id = split_subscription[1]
        self._subscription_id = subscription_short_name
        with tracer.start_as_current_span(
            name=f"{subscription_short_name} subscribe",
            context=parent_span_context if parent_span_context else None,
            kind=trace.SpanKind.CONSUMER,
            attributes={
                "messaging.system": _OPEN_TELEMETRY_MESSAGING_SYSTEM,
                "messaging.destination.name": subscription_short_name,
                "gcp.project_id": subscription.split("/")[1],
                "messaging.message.id": self._message.message_id,
                "messaging.message.body.size": len(self._message.data),
                "messaging.gcp_pubsub.message.ack_id": ack_id,
                "messaging.gcp_pubsub.message.ordering_key": self._message.ordering_key,
                "messaging.gcp_pubsub.message.exactly_once_delivery": exactly_once_enabled,
                "code.function": "_on_response",
                "messaging.gcp_pubsub.message.delivery_attempt": delivery_attempt,
            },
            end_on_exit=False,
        ) as subscribe_span:
            self._subscribe_span = subscribe_span

    def add_subscribe_span_event(self, event: str) -> None:
        assert self._subscribe_span is not None
        self._subscribe_span.add_event(
            name=event,
            attributes={
                "timestamp": str(datetime.now()),
            },
        )

    def end_subscribe_span(self) -> None:
        assert self._subscribe_span is not None
        self._subscribe_span.end()

    def set_subscribe_span_result(self, result: str) -> None:
        assert self._subscribe_span is not None
        self._subscribe_span.set_attribute(
            key="messaging.gcp_pubsub.result",
            value=result,
        )

    def start_subscribe_concurrency_control_span(self) -> None:
        assert self._subscribe_span is not None
        tracer = trace.get_tracer(_OPEN_TELEMETRY_TRACER_NAME)
        with tracer.start_as_current_span(
            name="subscriber concurrency control",
            kind=trace.SpanKind.INTERNAL,
            context=set_span_in_context(self._subscribe_span),
            end_on_exit=False,
        ) as concurrency_control_span:
            self._concurrency_control_span = concurrency_control_span

    def end_subscribe_concurrency_control_span(self) -> None:
        assert self._concurrency_control_span is not None
        self._concurrency_control_span.end()

    def start_subscribe_scheduler_span(self) -> None:
        assert self._subscribe_span is not None
        tracer = trace.get_tracer(_OPEN_TELEMETRY_TRACER_NAME)
        with tracer.start_as_current_span(
            name="subscriber scheduler",
            kind=trace.SpanKind.INTERNAL,
            context=set_span_in_context(self._subscribe_span),
            end_on_exit=False,
        ) as scheduler_span:
            self._scheduler_span = scheduler_span

    def end_subscribe_scheduler_span(self) -> None:
        assert self._scheduler_span is not None
        self._scheduler_span.end()

    def start_process_span(self) -> trace.Span:
        assert self._subscribe_span is not None
        tracer = trace.get_tracer(_OPEN_TELEMETRY_TRACER_NAME)
        publish_create_span_link: Optional[trace.Link] = None
        if self._publisher_create_span_context:
            publish_create_span: trace.Span = trace.get_current_span(
                self._publisher_create_span_context
            )
            span_context: Optional[trace.SpanContext] = (
                publish_create_span.get_span_context()
            )
            publish_create_span_link = (
                trace.Link(span_context) if span_context else None
            )

        with tracer.start_as_current_span(
            name=f"{self._subscription_id} process",
            attributes={
                "messaging.system": _OPEN_TELEMETRY_MESSAGING_SYSTEM,
            },
            kind=trace.SpanKind.INTERNAL,
            context=set_span_in_context(self._subscribe_span),
            links=[publish_create_span_link] if publish_create_span_link else None,
            end_on_exit=False,
        ) as process_span:
            self._process_span = process_span
            return process_span

    def end_process_span(self) -> None:
        assert self._process_span is not None
        self._process_span.end()

    def add_process_span_event(self, event: str) -> None:
        assert self._process_span is not None
        self._process_span.add_event(
            name=event,
            attributes={
                "timestamp": str(datetime.now()),
            },
        )

    def __enter__(self) -> trace.Span:
        return self.start_process_span()

    def __exit__(self, exc_type, exc_val, traceback):
        if self._process_span:
            self.end_process_span()


def start_modack_span(
    subscribe_span_links: List[trace.Link],
    subscription_id: Optional[str],
    message_count: int,
    deadline: float,
    project_id: Optional[str],
    code_function: str,
    receipt_modack: bool,
) -> trace.Span:
    assert subscription_id is not None
    assert project_id is not None
    tracer = trace.get_tracer(_OPEN_TELEMETRY_TRACER_NAME)
    with tracer.start_as_current_span(
        name=f"{subscription_id} modack",
        attributes={
            "messaging.system": _OPEN_TELEMETRY_MESSAGING_SYSTEM,
            "messaging.batch.message_count": message_count,
            "messaging.gcp_pubsub.message.ack_deadline": deadline,
            "messaging.destination.name": subscription_id,
            "gcp.project_id": project_id,
            "messaging.operation.name": "modack",
            "code.function": code_function,
            "messaging.gcp_pubsub.is_receipt_modack": receipt_modack,
        },
        links=subscribe_span_links,
        kind=trace.SpanKind.CLIENT,
        end_on_exit=False,
    ) as modack_span:
        return modack_span


def start_ack_span(
    subscription_id: str,
    message_count: int,
    project_id: str,
    links: List[trace.Link],
) -> trace.Span:
    tracer = trace.get_tracer(_OPEN_TELEMETRY_TRACER_NAME)
    with tracer.start_as_current_span(
        name=f"{subscription_id} ack",
        attributes={
            "messaging.system": _OPEN_TELEMETRY_MESSAGING_SYSTEM,
            "messaging.batch.message_count": message_count,
            "messaging.operation": "ack",
            "gcp.project_id": project_id,
            "messaging.destination.name": subscription_id,
            "code.function": "ack",
        },
        kind=trace.SpanKind.CLIENT,
        links=links,
        end_on_exit=False,
    ) as ack_span:
        return ack_span


def start_nack_span(
    subscription_id: str,
    message_count: int,
    project_id: str,
    links: List[trace.Link],
) -> trace.Span:
    tracer = trace.get_tracer(_OPEN_TELEMETRY_TRACER_NAME)
    with tracer.start_as_current_span(
        name=f"{subscription_id} nack",
        attributes={
            "messaging.system": _OPEN_TELEMETRY_MESSAGING_SYSTEM,
            "messaging.batch.message_count": message_count,
            "messaging.operation": "nack",
            "gcp.project_id": project_id,
            "messaging.destination.name": subscription_id,
            "code.function": "modify_ack_deadline",
        },
        kind=trace.SpanKind.CLIENT,
        links=links,
        end_on_exit=False,
    ) as nack_span:
        return nack_span
