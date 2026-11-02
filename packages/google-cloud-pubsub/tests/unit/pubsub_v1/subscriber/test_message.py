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

import datetime
import queue
import time
from unittest import mock

from google.api_core import datetime_helpers
from google.protobuf import timestamp_pb2

from google.cloud.pubsub_v1.open_telemetry.subscribe_opentelemetry import (
    SubscribeOpenTelemetry,
)
from google.cloud.pubsub_v1.subscriber import message
from google.cloud.pubsub_v1.subscriber._protocol import requests
from google.cloud.pubsub_v1.subscriber.exceptions import AcknowledgeStatus
from google.pubsub_v1 import types as gapic_types

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
):
    with mock.patch.object(time, "time") as time_:
        time_.return_value = RECEIVED_SECONDS
        gapic_pubsub_message = gapic_types.PubsubMessage(
            attributes=attrs,
            data=data,
            message_id="message_id",
            publish_time=timestamp_pb2.Timestamp(
                seconds=PUBLISHED_SECONDS, nanos=PUBLISHED_MICROS * 1000
            ),
            ordering_key=ordering_key,
        )
        msg = message.Message(
            # The code under test uses a raw protobuf PubsubMessage, i.e. w/o additional
            # Python class wrappers, hence the "_pb"
            message=gapic_pubsub_message._pb,
            ack_id=ack_id,
            delivery_attempt=delivery_attempt,
            request_queue=queue.Queue(),
            exactly_once_delivery_enabled_func=lambda: exactly_once_delivery_enabled,
        )
        return msg


def test_attributes():
    msg = create_message(b"foo", baz="bacon", spam="eggs")
    assert msg.attributes == {"baz": "bacon", "spam": "eggs"}


def test_data():
    msg = create_message(b"foo")
    assert msg.data == b"foo"


def test_size():
    msg = create_message(b"foo")
    assert msg.size == 30  # payload + protobuf overhead


def test_ack_id():
    ack_id = "MY-ACK-ID"
    msg = create_message(b"foo", ack_id=ack_id)
    assert msg.ack_id == ack_id


def test_delivery_attempt():
    delivery_attempt = 10
    msg = create_message(b"foo", delivery_attempt=delivery_attempt)
    assert msg.delivery_attempt == delivery_attempt


def test_delivery_attempt_is_none():
    msg = create_message(b"foo", delivery_attempt=0)
    assert msg.delivery_attempt is None


def test_publish_time():
    msg = create_message(b"foo")
    assert msg.publish_time == PUBLISHED


def test_ordering_key():
    msg = create_message(b"foo", ordering_key="key1")
    assert msg.ordering_key == "key1"


def check_call_types(mock, *args, **kwargs):
    """Checks a mock's call types.

    Args:
        mock: The mock to check.
        args: The types of the positional arguments.
        kwargs: The names of the keyword args to check and their respective
            types.

    Raises:
        AssertionError: if any of the types don't match, or if the number of
            arguments does not match.
    """
    for call in mock.mock_calls:
        _, call_args, call_kwargs = call
        assert len(call_args) == len(args)
        for n, argtype in enumerate(args):
            assert isinstance(call_args[n], argtype)


def test_opentelemetry_ack(span_exporter):
    SUBSCRIPTION = "projects/projectID/subscriptions/subscriptionID"
    msg = create_message(b"data", ack_id="ack_id")
    opentelemetry_data = SubscribeOpenTelemetry(msg)
    opentelemetry_data.start_subscribe_span(
        subscription=SUBSCRIPTION,
        exactly_once_enabled=False,
        ack_id="ack_id",
        delivery_attempt=2,
    )
    opentelemetry_data.start_process_span()
    msg.opentelemetry_data = opentelemetry_data
    msg.ack()
    opentelemetry_data.end_subscribe_span()

    spans = span_exporter.get_finished_spans()
    assert len(spans) == 2
    process_span, subscribe_span = spans

    assert subscribe_span.name == "subscriptionID subscribe"
    assert len(subscribe_span.events) == 0

    assert process_span.name == "subscriptionID process"
    assert len(process_span.events) == 1
    assert process_span.events[0].name == "ack called"


def test_opentelemetry_ack_with_response(span_exporter):
    SUBSCRIPTION = "projects/projectID/subscriptions/subscriptionID"
    msg = create_message(b"data", ack_id="ack_id")
    opentelemetry_data = SubscribeOpenTelemetry(msg)
    opentelemetry_data.start_subscribe_span(
        subscription=SUBSCRIPTION,
        exactly_once_enabled=False,
        ack_id="ack_id",
        delivery_attempt=2,
    )
    opentelemetry_data.start_process_span()
    msg.opentelemetry_data = opentelemetry_data
    msg.ack_with_response()
    opentelemetry_data.end_subscribe_span()

    spans = span_exporter.get_finished_spans()
    assert len(spans) == 2
    process_span, subscribe_span = spans

    assert subscribe_span.name == "subscriptionID subscribe"
    assert len(subscribe_span.events) == 0

    assert process_span.name == "subscriptionID process"
    assert len(process_span.events) == 1
    assert process_span.events[0].name == "ack called"


def test_opentelemetry_nack(span_exporter):
    SUBSCRIPTION = "projects/projectID/subscriptions/subscriptionID"
    msg = create_message(b"data", ack_id="ack_id")
    opentelemetry_data = SubscribeOpenTelemetry(msg)
    opentelemetry_data.start_subscribe_span(
        subscription=SUBSCRIPTION,
        exactly_once_enabled=False,
        ack_id="ack_id",
        delivery_attempt=2,
    )
    opentelemetry_data.start_process_span()
    msg.opentelemetry_data = opentelemetry_data
    msg.nack()
    opentelemetry_data.end_subscribe_span()

    spans = span_exporter.get_finished_spans()
    assert len(spans) == 2
    process_span, subscribe_span = spans

    assert subscribe_span.name == "subscriptionID subscribe"
    assert len(subscribe_span.events) == 0

    assert process_span.name == "subscriptionID process"
    assert len(process_span.events) == 1
    assert process_span.events[0].name == "nack called"


def test_opentelemetry_nack_with_response(span_exporter):
    SUBSCRIPTION = "projects/projectID/subscriptions/subscriptionID"
    msg = create_message(b"data", ack_id="ack_id")
    opentelemetry_data = SubscribeOpenTelemetry(msg)
    opentelemetry_data.start_subscribe_span(
        subscription=SUBSCRIPTION,
        exactly_once_enabled=False,
        ack_id="ack_id",
        delivery_attempt=2,
    )
    opentelemetry_data.start_process_span()
    msg.opentelemetry_data = opentelemetry_data
    msg.nack_with_response()
    opentelemetry_data.end_subscribe_span()

    spans = span_exporter.get_finished_spans()
    assert len(spans) == 2

    process_span, subscribe_span = spans

    assert subscribe_span.name == "subscriptionID subscribe"
    assert len(subscribe_span.events) == 0

    assert process_span.name == "subscriptionID process"
    assert len(process_span.events) == 1
    assert process_span.events[0].name == "nack called"


def test_opentelemetry_modack(span_exporter):
    SUBSCRIPTION = "projects/projectID/subscriptions/subscriptionID"
    msg = create_message(b"data", ack_id="ack_id")
    opentelemetry_data = SubscribeOpenTelemetry(msg)
    opentelemetry_data.start_subscribe_span(
        subscription=SUBSCRIPTION,
        exactly_once_enabled=False,
        ack_id="ack_id",
        delivery_attempt=2,
    )
    msg.opentelemetry_data = opentelemetry_data
    msg.modify_ack_deadline(3)
    opentelemetry_data.end_subscribe_span()

    spans = span_exporter.get_finished_spans()
    assert len(spans) == 1

    assert len(spans[0].events) == 0


def test_opentelemetry_modack_with_response(span_exporter):
    SUBSCRIPTION = "projects/projectID/subscriptions/subscriptionID"
    msg = create_message(b"data", ack_id="ack_id")
    opentelemetry_data = SubscribeOpenTelemetry(msg)
    opentelemetry_data.start_subscribe_span(
        subscription=SUBSCRIPTION,
        exactly_once_enabled=False,
        ack_id="ack_id",
        delivery_attempt=2,
    )
    msg.opentelemetry_data = opentelemetry_data
    msg.modify_ack_deadline_with_response(3)
    opentelemetry_data.end_subscribe_span()

    spans = span_exporter.get_finished_spans()
    assert len(spans) == 1

    assert len(spans[0].events) == 0


def test_ack():
    msg = create_message(b"foo", ack_id="bogus_ack_id")
    with mock.patch.object(msg._request_queue, "put") as put:
        msg.ack()
        put.assert_called_once_with(
            requests.AckRequest(
                message_id=msg.message_id,
                ack_id="bogus_ack_id",
                byte_size=30,
                time_to_ack=mock.ANY,
                ordering_key="",
                future=None,
            )
        )
        check_call_types(put, requests.AckRequest)


def test_ack_with_response_exactly_once_delivery_disabled():
    msg = create_message(b"foo", ack_id="bogus_ack_id")
    with mock.patch.object(msg._request_queue, "put") as put:
        future = msg.ack_with_response()
        put.assert_called_once_with(
            requests.AckRequest(
                message_id=msg.message_id,
                ack_id="bogus_ack_id",
                byte_size=30,
                time_to_ack=mock.ANY,
                ordering_key="",
                future=None,
            )
        )
        assert future.result() == AcknowledgeStatus.SUCCESS
        assert future == message._SUCCESS_FUTURE
        check_call_types(put, requests.AckRequest)


def test_ack_with_response_exactly_once_delivery_enabled():
    msg = create_message(
        b"foo", ack_id="bogus_ack_id", exactly_once_delivery_enabled=True
    )
    with mock.patch.object(msg._request_queue, "put") as put:
        future = msg.ack_with_response()
        put.assert_called_once_with(
            requests.AckRequest(
                message_id=msg.message_id,
                ack_id="bogus_ack_id",
                byte_size=30,
                time_to_ack=mock.ANY,
                ordering_key="",
                future=future,
            )
        )
        check_call_types(put, requests.AckRequest)


def test_drop():
    msg = create_message(b"foo", ack_id="bogus_ack_id")
    with mock.patch.object(msg._request_queue, "put") as put:
        msg.drop()
        put.assert_called_once_with(
            requests.DropRequest(ack_id="bogus_ack_id", byte_size=30, ordering_key="")
        )
        check_call_types(put, requests.DropRequest)


def test_modify_ack_deadline():
    msg = create_message(b"foo", ack_id="bogus_ack_id")
    with mock.patch.object(msg._request_queue, "put") as put:
        msg.modify_ack_deadline(60)
        put.assert_called_once_with(
            requests.ModAckRequest(
                message_id=msg.message_id,
                ack_id="bogus_ack_id",
                seconds=60,
                future=None,
            )
        )
        check_call_types(put, requests.ModAckRequest)


def test_modify_ack_deadline_with_response_exactly_once_delivery_disabled():
    msg = create_message(b"foo", ack_id="bogus_ack_id")
    with mock.patch.object(msg._request_queue, "put") as put:
        future = msg.modify_ack_deadline_with_response(60)
        put.assert_called_once_with(
            requests.ModAckRequest(
                message_id=msg.message_id,
                ack_id="bogus_ack_id",
                seconds=60,
                future=None,
            )
        )
        assert future.result() == AcknowledgeStatus.SUCCESS
        assert future == message._SUCCESS_FUTURE
        check_call_types(put, requests.ModAckRequest)


def test_modify_ack_deadline_with_response_exactly_once_delivery_enabled():
    msg = create_message(
        b"foo", ack_id="bogus_ack_id", exactly_once_delivery_enabled=True
    )
    with mock.patch.object(msg._request_queue, "put") as put:
        future = msg.modify_ack_deadline_with_response(60)
        put.assert_called_once_with(
            requests.ModAckRequest(
                message_id=msg.message_id,
                ack_id="bogus_ack_id",
                seconds=60,
                future=future,
            )
        )
        check_call_types(put, requests.ModAckRequest)


def test_nack():
    msg = create_message(b"foo", ack_id="bogus_ack_id")
    with mock.patch.object(msg._request_queue, "put") as put:
        msg.nack()
        put.assert_called_once_with(
            requests.NackRequest(
                ack_id="bogus_ack_id", byte_size=30, ordering_key="", future=None
            )
        )
        check_call_types(put, requests.NackRequest)


def test_nack_with_response_exactly_once_delivery_disabled():
    msg = create_message(b"foo", ack_id="bogus_ack_id")
    with mock.patch.object(msg._request_queue, "put") as put:
        future = msg.nack_with_response()
        put.assert_called_once_with(
            requests.NackRequest(
                ack_id="bogus_ack_id", byte_size=30, ordering_key="", future=None
            )
        )
        assert future.result() == AcknowledgeStatus.SUCCESS
        assert future == message._SUCCESS_FUTURE
        check_call_types(put, requests.NackRequest)


def test_nack_with_response_exactly_once_delivery_enabled():
    msg = create_message(
        b"foo", ack_id="bogus_ack_id", exactly_once_delivery_enabled=True
    )
    with mock.patch.object(msg._request_queue, "put") as put:
        future = msg.nack_with_response()
        put.assert_called_once_with(
            requests.NackRequest(
                ack_id="bogus_ack_id", byte_size=30, ordering_key="", future=future
            )
        )
        check_call_types(put, requests.NackRequest)


def test_repr():
    data = b"foo"
    ordering_key = "ord_key"
    msg = create_message(data, ordering_key=ordering_key, snow="cones", orange="juice")
    data_line = "  data: {!r}".format(data)
    ordering_key_line = "  ordering_key: {!r}".format(ordering_key)
    expected_repr = "\n".join(
        (
            "Message {",
            data_line,
            ordering_key_line,
            "  attributes: {",
            '    "orange": "juice",',
            '    "snow": "cones"',
            "  }",
            "}",
        )
    )
    assert repr(msg) == expected_repr
