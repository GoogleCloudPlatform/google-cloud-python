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

import datetime
import queue
import time
from unittest import mock

import pytest
from google.api_core import datetime_helpers
from google.protobuf import timestamp_pb2
from opentelemetry import trace
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator

from google.cloud.pubsub_v1.open_telemetry.context_propagation import (
    OpenTelemetryContextSetter,
)
from google.cloud.pubsub_v1.open_telemetry.subscribe_opentelemetry import (
    SubscribeOpenTelemetry,
)
from google.cloud.pubsub_v1.subscriber.message import Message
from google.cloud.pubsub_v1.types import PubsubMessage

RECEIVED = datetime.datetime(2012, 4, 21, 15, 0, tzinfo=datetime.timezone.utc)
RECEIVED_SECONDS = datetime_helpers.to_milliseconds(RECEIVED) // 1000
PUBLISHED_MICROS = 123456
PUBLISHED = RECEIVED + datetime.timedelta(days=1, microseconds=PUBLISHED_MICROS)
PUBLISHED_SECONDS = datetime_helpers.to_milliseconds(PUBLISHED) // 1000


def create_message(
    data,
    ack_id="ACKID",
    delivery_attempt=0,
    ordering_key="",
    exactly_once_delivery_enabled=False,
    **attrs,
):  # pragma: NO COVER
    with mock.patch.object(time, "time") as time_:
        time_.return_value = RECEIVED_SECONDS
        gapic_pubsub_message = PubsubMessage(
            attributes=attrs,
            data=data,
            message_id="message_id",
            publish_time=timestamp_pb2.Timestamp(
                seconds=PUBLISHED_SECONDS, nanos=PUBLISHED_MICROS * 1000
            ),
            ordering_key=ordering_key,
        )
        msg = Message(
            # The code under test uses a raw protobuf PubsubMessage, i.e. w/o additional
            # Python class wrappers, hence the "_pb"
            message=gapic_pubsub_message._pb,
            ack_id=ack_id,
            delivery_attempt=delivery_attempt,
            request_queue=queue.Queue(),
            exactly_once_delivery_enabled_func=lambda: exactly_once_delivery_enabled,
        )
        return msg


def test_opentelemetry_set_subscribe_span_result(span_exporter):
    msg = create_message(b"foo")
    opentelemetry_data = SubscribeOpenTelemetry(msg)
    opentelemetry_data.start_subscribe_span(
        subscription="projects/projectId/subscriptions/subscriptionID",
        exactly_once_enabled=False,
        ack_id="ack_id",
        delivery_attempt=4,
    )
    msg.opentelemetry_data = opentelemetry_data
    opentelemetry_data.set_subscribe_span_result("acked")
    opentelemetry_data.end_subscribe_span()
    spans = span_exporter.get_finished_spans()

    assert len(spans) == 1

    assert "messaging.gcp_pubsub.result" in spans[0].attributes
    assert spans[0].attributes["messaging.gcp_pubsub.result"] == "acked"


def test_opentelemetry_set_subscribe_span_result_assert_error():
    msg = create_message(b"foo")
    opentelemetry_data = SubscribeOpenTelemetry(msg)
    with pytest.raises(AssertionError):
        opentelemetry_data.set_subscribe_span_result("hi")


def test_opentelemetry_start_subscribe_concurrency_control_span_no_subscribe_span():
    msg = create_message(b"foo")
    opentelemetry_data = SubscribeOpenTelemetry(msg)
    with pytest.raises(AssertionError):
        opentelemetry_data.start_subscribe_concurrency_control_span()


def test_opentelemetry_end_subscribe_concurrency_control_span_assertion_error():
    msg = create_message(b"foo")
    opentelemetry_data = SubscribeOpenTelemetry(msg)
    with pytest.raises(AssertionError):
        opentelemetry_data.end_subscribe_concurrency_control_span()


def test_opentelemetry_start_subscribe_scheduler_span_assertion_error():
    msg = create_message(b"foo")
    opentelemetry_data = SubscribeOpenTelemetry(msg)
    with pytest.raises(AssertionError):
        opentelemetry_data.start_subscribe_scheduler_span()


def test_opentelemetry_end_subscribe_scheduler_span_assertion_error():
    msg = create_message(b"foo")
    opentelemetry_data = SubscribeOpenTelemetry(msg)
    with pytest.raises(AssertionError):
        opentelemetry_data.end_subscribe_scheduler_span()


def test_opentelemetry_start_process_span_assertion_error():
    msg = create_message(b"foo")
    opentelemetry_data = SubscribeOpenTelemetry(msg)
    with pytest.raises(AssertionError):
        opentelemetry_data.start_process_span()


def test_opentelemetry_end_process_span_assertion_error():
    msg = create_message(b"foo")
    opentelemetry_data = SubscribeOpenTelemetry(msg)
    with pytest.raises(AssertionError):
        opentelemetry_data.end_process_span()


def test_opentelemetry_start_process_span_publisher_link():
    msg = create_message(b"foo")
    opentelemetry_data = SubscribeOpenTelemetry(msg)
    msg.opentelemetry_data = opentelemetry_data
    tracer = trace.get_tracer("foo")
    publisher_create_span = None
    with tracer.start_as_current_span(name="name") as span:
        publisher_create_span = span
        TraceContextTextMapPropagator().inject(
            carrier=msg._message,
            setter=OpenTelemetryContextSetter(),
        )
        opentelemetry_data.start_subscribe_span(
            subscription="projects/projectId/subscriptions/subscriptionID",
            exactly_once_enabled=False,
            ack_id="ack_id",
            delivery_attempt=4,
        )
    opentelemetry_data.start_process_span()
    assert len(opentelemetry_data._process_span.links) == 1
    assert (
        opentelemetry_data._process_span.links[0].context.span_id
        == publisher_create_span.get_span_context().span_id
    )


def test_opentelemetry_start_process_span_no_publisher_span():
    msg = create_message(b"foo")
    opentelemetry_data = SubscribeOpenTelemetry(msg)
    msg.opentelemetry_data = opentelemetry_data
    opentelemetry_data.start_subscribe_span(
        subscription="projects/projectId/subscriptions/subscriptionID",
        exactly_once_enabled=False,
        ack_id="ack_id",
        delivery_attempt=4,
    )
    opentelemetry_data.start_process_span()
    # Assert that when no context is propagated, the subscriber span has no parent.
    assert opentelemetry_data._subscribe_span.parent is None
    # Assert that when there is no publisher create span context propagated,
    # There are no links created in the process span.
    assert len(opentelemetry_data._process_span.links) == 0


def test_opentelemetry_project_id_set_after_create_subscribe_span():
    msg = create_message(b"foo")
    opentelemetry_data = SubscribeOpenTelemetry(msg)
    msg.opentelemetry_data = opentelemetry_data
    opentelemetry_data.start_subscribe_span(
        subscription="projects/projectId/subscriptions/subscriptionID",
        exactly_once_enabled=False,
        ack_id="ack_id",
        delivery_attempt=4,
    )
    assert opentelemetry_data.project_id == "projectId"
