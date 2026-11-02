# Copyright 2018, Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import logging
import math
import queue
import threading
import time
import types as stdlib_types
from unittest import mock

import grpc
import pytest
from google.api_core import bidi, datetime_helpers, exceptions
from google.protobuf import timestamp_pb2
from google.rpc import code_pb2, error_details_pb2, status_pb2
from opentelemetry import trace

from google.cloud.pubsub_v1 import types
from google.cloud.pubsub_v1.open_telemetry.subscribe_opentelemetry import (
    SubscribeOpenTelemetry,
)
from google.cloud.pubsub_v1.subscriber import client, futures, message, scheduler
from google.cloud.pubsub_v1.subscriber import exceptions as subscriber_exceptions
from google.cloud.pubsub_v1.subscriber._protocol import (
    dispatcher,
    heartbeater,
    leaser,
    messages_on_hold,
    requests,
    streaming_pull_manager,
)
from google.cloud.pubsub_v1.subscriber.message import Message
from google.cloud.pubsub_v1.types import PubsubMessage
from google.pubsub_v1 import types as gapic_types


def create_mock_message(**kwargs):
    _message_mock = mock.create_autospec(message.Message, instance=True)
    msg = _message_mock.return_value
    for k, v in kwargs.items():
        setattr(msg, k, v)

    return msg


@pytest.mark.parametrize(
    "exception,expected_cls",
    [
        (ValueError("meep"), ValueError),
        (
            mock.create_autospec(grpc.RpcError, instance=True),
            exceptions.GoogleAPICallError,
        ),
        ({"error": "RPC terminated"}, Exception),
        ("something broke", Exception),
    ],
)
def test__wrap_as_exception(exception, expected_cls):
    assert isinstance(
        streaming_pull_manager._wrap_as_exception(exception), expected_cls
    )


def test__wrap_callback_errors_no_error():
    msg = create_mock_message()
    callback = mock.Mock()
    on_callback_error = mock.Mock()

    streaming_pull_manager._wrap_callback_errors(callback, on_callback_error, msg)

    callback.assert_called_once_with(msg)
    msg.nack.assert_not_called()
    on_callback_error.assert_not_called()


@pytest.mark.parametrize(
    "callback_error",
    [
        (ValueError("ValueError")),
        (BaseException("BaseException")),
    ],
)
def test__wrap_callback_errors_error(callback_error):
    msg = create_mock_message()
    callback = mock.Mock(side_effect=callback_error)
    on_callback_error = mock.Mock()

    streaming_pull_manager._wrap_callback_errors(callback, on_callback_error, msg)

    msg.nack.assert_called_once()
    on_callback_error.assert_called_once_with(callback_error)


def test_constructor_and_default_state():
    mock.sentinel.subscription = str()
    manager = streaming_pull_manager.StreamingPullManager(
        mock.sentinel.client, mock.sentinel.subscription
    )

    # Public state
    assert manager.is_active is False
    assert manager.flow_control == types.FlowControl()
    assert manager.dispatcher is None
    assert manager.leaser is None
    assert manager.ack_histogram is not None
    assert manager.ack_deadline == 10
    assert manager.load == 0

    # Private state
    assert manager._client == mock.sentinel.client
    assert manager._subscription == mock.sentinel.subscription
    assert manager._scheduler is not None
    assert manager._messages_on_hold is not None
    assert manager._client_id is not None


def test_constructor_with_default_options():
    mock.sentinel.subscription = str()
    flow_control_ = types.FlowControl()
    manager = streaming_pull_manager.StreamingPullManager(
        mock.sentinel.client,
        mock.sentinel.subscription,
        flow_control=flow_control_,
        scheduler=mock.sentinel.scheduler,
    )

    assert manager.flow_control == flow_control_
    assert manager._scheduler == mock.sentinel.scheduler
    assert manager._ack_deadline == 10
    assert manager._stream_ack_deadline == 60


def test_constructor_with_min_and_max_duration_per_lease_extension_():
    mock.sentinel.subscription = str()
    flow_control_ = types.FlowControl(
        min_duration_per_lease_extension=15, max_duration_per_lease_extension=20
    )
    manager = streaming_pull_manager.StreamingPullManager(
        mock.sentinel.client,
        mock.sentinel.subscription,
        flow_control=flow_control_,
        scheduler=mock.sentinel.scheduler,
    )
    assert manager._ack_deadline == 15
    assert manager._stream_ack_deadline == 20


def test_constructor_with_min_duration_per_lease_extension_too_low():
    mock.sentinel.subscription = str()
    flow_control_ = types.FlowControl(
        min_duration_per_lease_extension=9, max_duration_per_lease_extension=9
    )
    manager = streaming_pull_manager.StreamingPullManager(
        mock.sentinel.client,
        mock.sentinel.subscription,
        flow_control=flow_control_,
        scheduler=mock.sentinel.scheduler,
    )
    assert manager._ack_deadline == 10
    assert manager._stream_ack_deadline == 10


def test_constructor_with_max_duration_per_lease_extension_too_high():
    mock.sentinel.subscription = str()
    flow_control_ = types.FlowControl(
        max_duration_per_lease_extension=601, min_duration_per_lease_extension=601
    )
    manager = streaming_pull_manager.StreamingPullManager(
        mock.sentinel.client,
        mock.sentinel.subscription,
        flow_control=flow_control_,
        scheduler=mock.sentinel.scheduler,
    )
    assert manager._ack_deadline == 600
    assert manager._stream_ack_deadline == 600


def make_manager(
    enable_open_telemetry: bool = False,
    subscription_name: str = "subscription-name",
    **kwargs,
):
    client_ = mock.create_autospec(client.Client, instance=True)
    client_.open_telemetry_enabled = enable_open_telemetry
    scheduler_ = mock.create_autospec(scheduler.Scheduler, instance=True)
    return streaming_pull_manager.StreamingPullManager(
        client_, subscription_name, scheduler=scheduler_, **kwargs
    )


def complete_modify_ack_deadline_calls(dispatcher):
    def complete_futures(*args, **kwargs):
        modack_requests = args[0]
        for req in modack_requests:
            if req.future:
                req.future.set_result(subscriber_exceptions.AcknowledgeStatus.SUCCESS)

    dispatcher.modify_ack_deadline.side_effect = complete_futures


def fake_leaser_add(leaser, init_msg_count=0, assumed_msg_size=10):
    """Add a simplified fake add() method to a leaser instance.

    The fake add() method actually increases the leaser's internal message count
    by one for each message, and the total bytes by ``assumed_msg_size`` for
    each message (regardless of the actual message size).
    """

    def fake_add(self, items):
        self.message_count += len(items)
        self.bytes += len(items) * assumed_msg_size

    leaser.message_count = init_msg_count
    leaser.bytes = init_msg_count * assumed_msg_size
    leaser.add = stdlib_types.MethodType(fake_add, leaser)


def test__obtain_ack_deadline_no_custom_flow_control_setting():
    from google.cloud.pubsub_v1.subscriber._protocol import histogram

    manager = make_manager()

    # Make sure that min_duration_per_lease_extension and
    # max_duration_per_lease_extension is disabled.
    manager._flow_control = types.FlowControl(
        min_duration_per_lease_extension=0, max_duration_per_lease_extension=0
    )
    assert manager._stream_ack_deadline == 60
    assert manager._ack_deadline == 10
    assert manager._obtain_ack_deadline(maybe_update=False) == 10

    deadline = manager._obtain_ack_deadline(maybe_update=True)
    assert deadline == histogram.MIN_ACK_DEADLINE
    assert manager._stream_ack_deadline == 60

    # When we get some historical data, the deadline is adjusted.
    manager.ack_histogram.add(histogram.MIN_ACK_DEADLINE * 2)
    deadline = manager._obtain_ack_deadline(maybe_update=True)
    assert deadline == histogram.MIN_ACK_DEADLINE * 2

    # Adding just a single additional data point does not yet change the deadline.
    manager.ack_histogram.add(histogram.MIN_ACK_DEADLINE)
    deadline = manager._obtain_ack_deadline(maybe_update=True)
    assert deadline == histogram.MIN_ACK_DEADLINE * 2


def test__obtain_ack_deadline_with_max_duration_per_lease_extension():
    from google.cloud.pubsub_v1.subscriber._protocol import histogram

    manager = make_manager()
    manager._flow_control = types.FlowControl(
        max_duration_per_lease_extension=histogram.MIN_ACK_DEADLINE + 1
    )
    assert manager._ack_deadline == 10

    manager.ack_histogram.add(histogram.MIN_ACK_DEADLINE * 3)  # make p99 value large

    # The deadline configured in flow control should prevail.
    deadline = manager._obtain_ack_deadline(maybe_update=True)
    assert deadline == histogram.MIN_ACK_DEADLINE + 1
    assert manager._stream_ack_deadline == 60


def test__obtain_ack_deadline_with_min_duration_per_lease_extension():
    from google.cloud.pubsub_v1.subscriber._protocol import histogram

    manager = make_manager()
    manager._flow_control = types.FlowControl(
        min_duration_per_lease_extension=histogram.MAX_ACK_DEADLINE
    )
    manager.ack_histogram.add(histogram.MIN_ACK_DEADLINE)  # make p99 value small

    # The deadline configured in flow control should prevail.
    deadline = manager._obtain_ack_deadline(maybe_update=True)
    assert deadline == histogram.MAX_ACK_DEADLINE
    assert manager._stream_ack_deadline == histogram.MAX_ACK_DEADLINE


def test__obtain_ack_deadline_with_max_duration_per_lease_extension_too_low():
    from google.cloud.pubsub_v1.subscriber._protocol import histogram

    manager = make_manager()
    manager._flow_control = types.FlowControl(
        max_duration_per_lease_extension=histogram.MIN_ACK_DEADLINE - 1
    )

    # The deadline configured in flow control should be adjusted to the minimum allowed.
    deadline = manager._obtain_ack_deadline(maybe_update=True)
    assert deadline == histogram.MIN_ACK_DEADLINE


def test__obtain_ack_deadline_with_min_duration_per_lease_extension_too_high():
    from google.cloud.pubsub_v1.subscriber._protocol import histogram

    manager = make_manager()
    manager._flow_control = types.FlowControl(
        min_duration_per_lease_extension=histogram.MAX_ACK_DEADLINE + 1
    )

    # The deadline configured in flow control should be adjusted to the maximum allowed.
    deadline = manager._obtain_ack_deadline(maybe_update=True)
    assert deadline == histogram.MAX_ACK_DEADLINE
    assert manager._stream_ack_deadline == histogram.MAX_ACK_DEADLINE


def test__obtain_ack_deadline_with_exactly_once_enabled():
    manager = make_manager()
    manager._flow_control = types.FlowControl(
        min_duration_per_lease_extension=0  # leave as default value
    )
    manager._exactly_once_enabled = True
    manager.ack_histogram.add(
        10
    )  # reduce p99 value below 60s min for exactly_once subscriptions

    deadline = manager._obtain_ack_deadline(maybe_update=True)
    # Since the 60-second min ack_deadline value for exactly_once subscriptions
    # seconds is higher than the histogram value, the deadline should be 60 sec.
    assert deadline == 60
    assert manager._stream_ack_deadline == 60


def test__obtain_ack_deadline_with_min_duration_per_lease_extension_with_exactly_once_enabled():
    from google.cloud.pubsub_v1.subscriber._protocol import histogram

    manager = make_manager()
    manager._flow_control = types.FlowControl(
        min_duration_per_lease_extension=histogram.MAX_ACK_DEADLINE
    )
    manager._exactly_once_enabled = True
    manager.ack_histogram.add(histogram.MIN_ACK_DEADLINE)  # make p99 value small

    # The deadline configured in flow control should prevail.
    deadline = manager._obtain_ack_deadline(maybe_update=True)
    # User-defined custom min ack_deadline value takes precedence over
    # exactly_once default of 60 seconds.
    assert deadline == histogram.MAX_ACK_DEADLINE
    assert manager._stream_ack_deadline == histogram.MAX_ACK_DEADLINE


def test__obtain_ack_deadline_no_value_update():
    manager = make_manager()

    # Make sure that max_duration_per_lease_extension is disabled.
    manager._flow_control = types.FlowControl(max_duration_per_lease_extension=0)

    manager.ack_histogram.add(21)
    deadline = manager._obtain_ack_deadline(maybe_update=True)
    assert deadline == 21

    for _ in range(5):
        manager.ack_histogram.add(35)  # Gather some new ACK data.

    deadline = manager._obtain_ack_deadline(maybe_update=False)
    assert deadline == 21  # still the same

    # Accessing the value through the ack_deadline property has no side effects either.
    assert manager.ack_deadline == 21

    # Updating the ack deadline is reflected on ack_deadline wrapper, too.
    deadline = manager._obtain_ack_deadline(maybe_update=True)
    assert manager.ack_deadline == deadline == 35


def test_client_id():
    manager1 = make_manager()
    request1 = manager1._get_initial_request(stream_ack_deadline_seconds=60)
    client_id_1 = request1.client_id
    assert client_id_1

    manager2 = make_manager()
    request2 = manager2._get_initial_request(stream_ack_deadline_seconds=60)
    client_id_2 = request2.client_id
    assert client_id_2

    assert client_id_1 != client_id_2


def test_streaming_flow_control():
    manager = make_manager(
        flow_control=types.FlowControl(max_messages=10, max_bytes=1000)
    )
    request = manager._get_initial_request(stream_ack_deadline_seconds=60)
    assert request.max_outstanding_messages == 10
    assert request.max_outstanding_bytes == 1000


def test_streaming_flow_control_use_legacy_flow_control():
    manager = make_manager(
        flow_control=types.FlowControl(max_messages=10, max_bytes=1000),
        use_legacy_flow_control=True,
    )
    request = manager._get_initial_request(stream_ack_deadline_seconds=60)
    assert request.max_outstanding_messages == 0
    assert request.max_outstanding_bytes == 0


def test_maybe_pause_consumer_wo_consumer_set():
    manager = make_manager(
        flow_control=types.FlowControl(max_messages=10, max_bytes=1000)
    )
    manager.maybe_pause_consumer()  # no raise
    # Ensure load > 1
    _leaser = manager._leaser = mock.create_autospec(leaser.Leaser)
    _leaser.message_count = 100
    _leaser.bytes = 10000
    manager.maybe_pause_consumer()  # no raise


def test_lease_load_and_pause():
    manager = make_manager(
        flow_control=types.FlowControl(max_messages=10, max_bytes=1000)
    )
    manager._leaser = leaser.Leaser(manager)
    manager._consumer = mock.create_autospec(bidi.BackgroundConsumer, instance=True)
    manager._consumer.is_paused = False

    # This should mean that our messages count is at 10%, and our bytes
    # are at 15%; load should return the higher (0.15), and shouldn't cause
    # the consumer to pause.
    manager.leaser.add(
        [requests.LeaseRequest(ack_id="one", byte_size=150, ordering_key="")]
    )
    assert manager.load == 0.15
    manager.maybe_pause_consumer()
    manager._consumer.pause.assert_not_called()

    # After this message is added, the messages should be higher at 20%
    # (versus 16% for bytes).
    manager.leaser.add(
        [requests.LeaseRequest(ack_id="two", byte_size=10, ordering_key="")]
    )
    assert manager.load == 0.2

    # Returning a number above 100% is fine, and it should cause this to pause.
    manager.leaser.add(
        [requests.LeaseRequest(ack_id="three", byte_size=1000, ordering_key="")]
    )
    assert manager.load == 1.16
    manager.maybe_pause_consumer()
    manager._consumer.pause.assert_called_once()


def test_drop_and_resume():
    manager = make_manager(
        flow_control=types.FlowControl(max_messages=10, max_bytes=1000)
    )
    manager._leaser = leaser.Leaser(manager)
    manager._consumer = mock.create_autospec(bidi.BackgroundConsumer, instance=True)
    manager._consumer.is_paused = True

    # Add several messages until we're over the load threshold.
    manager.leaser.add(
        [
            requests.LeaseRequest(ack_id="one", byte_size=750, ordering_key=""),
            requests.LeaseRequest(ack_id="two", byte_size=250, ordering_key=""),
        ]
    )

    assert manager.load == 1.0

    # Trying to resume now should have no effect as we're over the threshold.
    manager.maybe_resume_consumer()
    manager._consumer.resume.assert_not_called()

    # Drop the 200 byte message, which should put us under the resume
    # threshold.
    manager.leaser.remove(
        [requests.DropRequest(ack_id="two", byte_size=250, ordering_key="")]
    )
    manager.maybe_resume_consumer()
    manager._consumer.resume.assert_called_once()


def test_resume_not_paused():
    manager = make_manager()
    manager._consumer = mock.create_autospec(bidi.BackgroundConsumer, instance=True)
    manager._consumer.is_paused = False

    # Resuming should have no effect is the consumer is not actually paused.
    manager.maybe_resume_consumer()
    manager._consumer.resume.assert_not_called()


def test_maybe_resume_consumer_wo_consumer_set():
    manager = make_manager(
        flow_control=types.FlowControl(max_messages=10, max_bytes=1000)
    )
    manager.maybe_resume_consumer()  # no raise


def test__maybe_release_messages_on_overload():
    manager = make_manager(
        flow_control=types.FlowControl(max_messages=10, max_bytes=1000)
    )
    msg = create_mock_message(ack_id="ack", size=11)

    manager._messages_on_hold.put(msg)
    manager._on_hold_bytes = msg.size

    # Ensure load is exactly 1.0 (to verify that >= condition is used)
    _leaser = manager._leaser = mock.create_autospec(leaser.Leaser)
    _leaser.message_count = 10
    _leaser.bytes = 1000 + msg.size

    manager._maybe_release_messages()

    assert manager._messages_on_hold.size == 1
    manager._leaser.add.assert_not_called()
    manager._scheduler.schedule.assert_not_called()


def test_opentelemetry__maybe_release_messages_subscribe_scheduler_span(span_exporter):
    manager = make_manager(
        flow_control=types.FlowControl(max_messages=10, max_bytes=1000)
    )
    manager._callback = mock.sentinel.callback

    # Init leaser message count to 11, so that when subtracting the 3 messages
    # that are on hold, there is still room for another 2 messages before the
    # max load is hit.
    _leaser = manager._leaser = mock.create_autospec(leaser.Leaser)
    fake_leaser_add(_leaser, init_msg_count=8, assumed_msg_size=10)
    msg = create_mock_message(ack_id="ack_foo", size=10)

    msg.message_id = 3
    opentelemetry_data = SubscribeOpenTelemetry(msg)
    msg.opentelemetry_data = opentelemetry_data
    opentelemetry_data.start_subscribe_span(
        subscription="projects/projectId/subscriptions/subscriptionID",
        exactly_once_enabled=False,
        ack_id="ack_id",
        delivery_attempt=4,
    )
    manager._messages_on_hold.put(msg)
    manager._maybe_release_messages()
    opentelemetry_data.end_subscribe_span()
    spans = span_exporter.get_finished_spans()

    assert len(spans) == 2

    subscriber_scheduler_span, subscribe_span = spans

    assert subscriber_scheduler_span.name == "subscriber scheduler"
    assert subscribe_span.name == "subscriptionID subscribe"

    assert subscriber_scheduler_span.parent == subscribe_span.context
    assert subscriber_scheduler_span.kind == trace.SpanKind.INTERNAL


def test__maybe_release_messages_below_overload():
    manager = make_manager(
        flow_control=types.FlowControl(max_messages=10, max_bytes=1000)
    )
    manager._callback = mock.sentinel.callback

    # Init leaser message count to 11, so that when subtracting the 3 messages
    # that are on hold, there is still room for another 2 messages before the
    # max load is hit.
    _leaser = manager._leaser = mock.create_autospec(leaser.Leaser)
    fake_leaser_add(_leaser, init_msg_count=11, assumed_msg_size=10)

    messages = [
        mock.create_autospec(message.Message, instance=True, ack_id="ack_foo", size=10),
        mock.create_autospec(message.Message, instance=True, ack_id="ack_bar", size=10),
        mock.create_autospec(message.Message, instance=True, ack_id="ack_baz", size=10),
    ]
    for msg in messages:
        manager._messages_on_hold.put(msg)
        manager._on_hold_bytes = 3 * 10

    # the actual call of MUT
    manager._maybe_release_messages()

    assert manager._messages_on_hold.size == 1
    msg = manager._messages_on_hold.get()
    assert msg.ack_id == "ack_baz"

    schedule_calls = manager._scheduler.schedule.mock_calls
    assert len(schedule_calls) == 2
    for _, call_args, _ in schedule_calls:
        assert call_args[0] == mock.sentinel.callback
        assert isinstance(call_args[1], message.Message)
        assert call_args[1].ack_id in ("ack_foo", "ack_bar")


def test__maybe_release_messages_negative_on_hold_bytes_warning(
    caplog, modify_google_logger_propagation
):
    manager = make_manager(
        flow_control=types.FlowControl(max_messages=10, max_bytes=1000)
    )
    manager._callback = lambda msg: msg  # pragma: NO COVER

    msg = create_mock_message(ack_id="ack", size=17)
    manager._messages_on_hold.put(msg)
    manager._on_hold_bytes = 5  # too low for some reason

    _leaser = manager._leaser = mock.create_autospec(leaser.Leaser)
    _leaser.message_count = 3
    _leaser.bytes = 150

    with caplog.at_level(logging.WARNING):
        manager._maybe_release_messages()

    expected_warnings = [
        record.message.lower()
        for record in caplog.records
        if "unexpectedly negative" in record.message
    ]
    assert len(expected_warnings) == 1
    assert "on hold bytes" in expected_warnings[0]
    assert "-12" in expected_warnings[0]

    assert manager._on_hold_bytes == 0  # should be auto-corrected


@pytest.mark.parametrize(
    "receipt_modack",
    [
        True,
        False,
    ],
)
def test_opentelemetry__send_lease_modacks(span_exporter, receipt_modack):
    manager, _, _, _, _, _ = make_running_manager(
        enable_open_telemetry=True,
        subscription_name="projects/projectID/subscriptions/subscriptionID",
    )
    data1 = SubscribeOpenTelemetry(
        message=gapic_types.PubsubMessage(data=b"foo", message_id="1")
    )
    data2 = SubscribeOpenTelemetry(
        message=gapic_types.PubsubMessage(data=b"bar", message_id="2")
    )

    data1.start_subscribe_span(
        subscription="projects/projectID/subscriptions/subscriptionID",
        exactly_once_enabled=False,
        ack_id="ack_id1",
        delivery_attempt=2,
    )
    data2.start_subscribe_span(
        subscription="projects/projectID/subscriptions/subscriptionID",
        exactly_once_enabled=True,
        ack_id="ack_id1",
        delivery_attempt=2,
    )
    mock_span_context = mock.Mock(spec=trace.SpanContext)
    mock_span_context.trace_flags.sampled = False
    with mock.patch.object(
        data1._subscribe_span, "get_span_context", return_value=mock_span_context
    ):
        manager._send_lease_modacks(
            ack_ids=["ack_id1", "ack_id2"],
            ack_deadline=20,
            opentelemetry_data=[data1, data2],
            receipt_modack=receipt_modack,
        )
    data1.end_subscribe_span()
    data2.end_subscribe_span()
    spans = span_exporter.get_finished_spans()
    assert len(spans) == 3
    modack_span, subscribe_span1, subscribe_span2 = spans

    assert len(subscribe_span1.events) == 0
    assert len(subscribe_span2.events) == 0

    assert len(subscribe_span1.links) == 0
    assert len(subscribe_span2.links) == 1
    assert subscribe_span2.links[0].context == modack_span.context
    assert subscribe_span2.links[0].attributes["messaging.operation.name"] == "modack"

    assert modack_span.name == "subscriptionID modack"
    assert modack_span.parent is None
    assert modack_span.kind == trace.SpanKind.CLIENT
    assert len(modack_span.links) == 1
    modack_span_attributes = modack_span.attributes
    assert modack_span_attributes["messaging.system"] == "gcp_pubsub"
    assert modack_span_attributes["messaging.batch.message_count"] == 2
    assert math.isclose(
        modack_span_attributes["messaging.gcp_pubsub.message.ack_deadline"], 20
    )
    assert modack_span_attributes["messaging.destination.name"] == "subscriptionID"
    assert modack_span_attributes["gcp.project_id"] == "projectID"
    assert modack_span_attributes["messaging.operation.name"] == "modack"
    assert modack_span_attributes["code.function"] == "_send_lease_modacks"
    assert (
        modack_span_attributes["messaging.gcp_pubsub.is_receipt_modack"]
        == receipt_modack
    )


def test_send_unary_ack():
    manager = make_manager()

    ack_reqs_dict = {
        "ack_id1": requests.AckRequest(
            ack_id="ack_id1", byte_size=0, time_to_ack=20, ordering_key="", future=None
        ),
        "ack_id2": requests.AckRequest(
            ack_id="ack_id2", byte_size=0, time_to_ack=20, ordering_key="", future=None
        ),
    }
    manager.send_unary_ack(ack_ids=["ack_id1", "ack_id2"], ack_reqs_dict=ack_reqs_dict)

    manager._client.acknowledge.assert_called_once_with(
        subscription=manager._subscription, ack_ids=["ack_id1", "ack_id2"]
    )


def test_send_unary_ack_exactly_once_enabled_with_futures():
    manager = make_manager()
    manager._exactly_once_enabled = True

    future1 = futures.Future()
    future2 = futures.Future()
    ack_reqs_dict = {
        "ack_id1": requests.AckRequest(
            ack_id="ack_id1",
            byte_size=0,
            time_to_ack=20,
            ordering_key="",
            future=future1,
        ),
        "ack_id2": requests.AckRequest(
            ack_id="ack_id2",
            byte_size=0,
            time_to_ack=20,
            ordering_key="",
            future=future2,
        ),
    }
    manager.send_unary_ack(ack_ids=["ack_id1", "ack_id2"], ack_reqs_dict=ack_reqs_dict)

    manager._client.acknowledge.assert_called_once_with(
        subscription=manager._subscription, ack_ids=["ack_id1", "ack_id2"]
    )
    assert future1.result() == subscriber_exceptions.AcknowledgeStatus.SUCCESS
    assert future2.result() == subscriber_exceptions.AcknowledgeStatus.SUCCESS


def test_send_unary_ack_exactly_once_disabled_with_futures():
    manager = make_manager()

    future1 = futures.Future()
    future2 = futures.Future()
    ack_reqs_dict = {
        "ack_id1": requests.AckRequest(
            ack_id="ack_id1",
            byte_size=0,
            time_to_ack=20,
            ordering_key="",
            future=future1,
        ),
        "ack_id2": requests.AckRequest(
            ack_id="ack_id2",
            byte_size=0,
            time_to_ack=20,
            ordering_key="",
            future=future2,
        ),
    }
    manager.send_unary_ack(ack_ids=["ack_id1", "ack_id2"], ack_reqs_dict=ack_reqs_dict)

    manager._client.acknowledge.assert_called_once_with(
        subscription=manager._subscription, ack_ids=["ack_id1", "ack_id2"]
    )
    assert future1.result() == subscriber_exceptions.AcknowledgeStatus.SUCCESS
    assert future2.result() == subscriber_exceptions.AcknowledgeStatus.SUCCESS


def test_send_unary_modack():
    manager = make_manager()

    ack_reqs_dict = {
        "ack_id3": requests.ModAckRequest(ack_id="ack_id3", seconds=60, future=None),
        "ack_id4": requests.ModAckRequest(ack_id="ack_id4", seconds=60, future=None),
        "ack_id5": requests.ModAckRequest(ack_id="ack_id5", seconds=60, future=None),
    }
    manager.send_unary_modack(
        modify_deadline_ack_ids=["ack_id3", "ack_id4", "ack_id5"],
        modify_deadline_seconds=[10, 20, 20],
        ack_reqs_dict=ack_reqs_dict,
    )

    manager._client.modify_ack_deadline.assert_has_calls(
        [
            mock.call(
                subscription=manager._subscription,
                ack_ids=["ack_id3"],
                ack_deadline_seconds=10,
            ),
            mock.call(
                subscription=manager._subscription,
                ack_ids=["ack_id4", "ack_id5"],
                ack_deadline_seconds=20,
            ),
        ],
        any_order=True,
    )


def test_send_unary_modack_default_deadline():
    manager = make_manager()

    ack_reqs_dict = {
        "ack_id3": requests.ModAckRequest(ack_id="ack_id3", seconds=60, future=None),
        "ack_id4": requests.ModAckRequest(ack_id="ack_id4", seconds=60, future=None),
        "ack_id5": requests.ModAckRequest(ack_id="ack_id5", seconds=60, future=None),
    }
    manager.send_unary_modack(
        modify_deadline_ack_ids=["ack_id3", "ack_id4", "ack_id5"],
        modify_deadline_seconds=None,
        ack_reqs_dict=ack_reqs_dict,
        default_deadline=10,
    )

    manager._client.modify_ack_deadline.assert_has_calls(
        [
            mock.call(
                subscription=manager._subscription,
                ack_ids=["ack_id3", "ack_id4", "ack_id5"],
                ack_deadline_seconds=10,
            ),
        ],
        any_order=True,
    )


def test_send_unary_modack_exactly_once_enabled_with_futures():
    manager = make_manager()
    manager._exactly_once_enabled = True

    future1 = futures.Future()
    future2 = futures.Future()
    future3 = futures.Future()
    ack_reqs_dict = {
        "ack_id3": requests.ModAckRequest(ack_id="ack_id3", seconds=60, future=future1),
        "ack_id4": requests.ModAckRequest(ack_id="ack_id4", seconds=60, future=future2),
        "ack_id5": requests.ModAckRequest(ack_id="ack_id5", seconds=60, future=future3),
    }
    manager.send_unary_modack(
        modify_deadline_ack_ids=["ack_id3", "ack_id4", "ack_id5"],
        modify_deadline_seconds=[10, 20, 20],
        ack_reqs_dict=ack_reqs_dict,
    )

    manager._client.modify_ack_deadline.assert_has_calls(
        [
            mock.call(
                subscription=manager._subscription,
                ack_ids=["ack_id3"],
                ack_deadline_seconds=10,
            ),
            mock.call(
                subscription=manager._subscription,
                ack_ids=["ack_id4", "ack_id5"],
                ack_deadline_seconds=20,
            ),
        ],
        any_order=True,
    )
    assert future1.result() == subscriber_exceptions.AcknowledgeStatus.SUCCESS
    assert future2.result() == subscriber_exceptions.AcknowledgeStatus.SUCCESS
    assert future3.result() == subscriber_exceptions.AcknowledgeStatus.SUCCESS


def test_send_unary_modack_exactly_once_disabled_with_futures():
    manager = make_manager()

    future1 = futures.Future()
    future2 = futures.Future()
    future3 = futures.Future()
    ack_reqs_dict = {
        "ack_id3": requests.ModAckRequest(ack_id="ack_id3", seconds=60, future=future1),
        "ack_id4": requests.ModAckRequest(ack_id="ack_id4", seconds=60, future=future2),
        "ack_id5": requests.ModAckRequest(ack_id="ack_id5", seconds=60, future=future3),
    }
    manager.send_unary_modack(
        modify_deadline_ack_ids=["ack_id3", "ack_id4", "ack_id5"],
        modify_deadline_seconds=[10, 20, 20],
        ack_reqs_dict=ack_reqs_dict,
    )

    manager._client.modify_ack_deadline.assert_has_calls(
        [
            mock.call(
                subscription=manager._subscription,
                ack_ids=["ack_id3"],
                ack_deadline_seconds=10,
            ),
            mock.call(
                subscription=manager._subscription,
                ack_ids=["ack_id4", "ack_id5"],
                ack_deadline_seconds=20,
            ),
        ],
        any_order=True,
    )
    assert future1.result() == subscriber_exceptions.AcknowledgeStatus.SUCCESS
    assert future2.result() == subscriber_exceptions.AcknowledgeStatus.SUCCESS
    assert future3.result() == subscriber_exceptions.AcknowledgeStatus.SUCCESS


def test_send_unary_ack_api_call_error(caplog, modify_google_logger_propagation):
    caplog.set_level(logging.DEBUG)

    manager = make_manager()

    error = exceptions.GoogleAPICallError("The front fell off")
    manager._client.acknowledge.side_effect = error

    ack_reqs_dict = {
        "ack_id1": requests.AckRequest(
            ack_id="ack_id1", byte_size=0, time_to_ack=20, ordering_key="", future=None
        ),
        "ack_id2": requests.AckRequest(
            ack_id="ack_id2", byte_size=0, time_to_ack=20, ordering_key="", future=None
        ),
    }
    manager.send_unary_ack(ack_ids=["ack_id1", "ack_id2"], ack_reqs_dict=ack_reqs_dict)

    assert "The front fell off" in caplog.text


def test_send_unary_modack_api_call_error(caplog, modify_google_logger_propagation):
    caplog.set_level(logging.DEBUG)

    manager = make_manager()

    error = exceptions.GoogleAPICallError("The front fell off")
    manager._client.modify_ack_deadline.side_effect = error

    ack_reqs_dict = {
        "ack_id1": requests.AckRequest(
            ack_id="ack_id1",
            byte_size=0,
            time_to_ack=20,
            ordering_key="",
            future=futures.Future(),
        ),
        "ack_id2": requests.AckRequest(
            ack_id="ack_id2",
            byte_size=0,
            time_to_ack=20,
            ordering_key="",
            future=futures.Future(),
        ),
    }
    manager.send_unary_modack(
        modify_deadline_ack_ids=["ack_id_string"],
        modify_deadline_seconds=[0],
        ack_reqs_dict=ack_reqs_dict,
    )

    assert "The front fell off" in caplog.text


def test_send_unary_ack_retry_error_exactly_once_disabled_no_futures(
    caplog, modify_google_logger_propagation
):
    caplog.set_level(logging.DEBUG)

    manager, _, _, _, _, _ = make_running_manager()
    manager._exactly_once_enabled = False

    error = exceptions.RetryError(
        "Too long a transient error", cause=Exception("Out of time!")
    )
    manager._client.acknowledge.side_effect = error

    ack_reqs_dict = {
        "ack_id1": requests.AckRequest(
            ack_id="ack_id1",
            byte_size=0,
            time_to_ack=20,
            ordering_key="",
            future=None,
        ),
        "ack_id2": requests.AckRequest(
            ack_id="ack_id2",
            byte_size=0,
            time_to_ack=20,
            ordering_key="",
            future=None,
        ),
    }
    with pytest.raises(exceptions.RetryError):
        manager.send_unary_ack(
            ack_ids=["ack_id1", "ack_id2"], ack_reqs_dict=ack_reqs_dict
        )

    assert "RetryError while sending ack RPC" in caplog.text
    assert "signaled streaming pull manager shutdown" in caplog.text


def test_send_unary_ack_retry_error_exactly_once_disabled_with_futures(
    caplog, modify_google_logger_propagation
):
    caplog.set_level(logging.DEBUG)

    manager, _, _, _, _, _ = make_running_manager()
    manager._exactly_once_enabled = False

    error = exceptions.RetryError(
        "Too long a transient error", cause=Exception("Out of time!")
    )
    manager._client.acknowledge.side_effect = error

    future1 = futures.Future()
    future2 = futures.Future()
    ack_reqs_dict = {
        "ack_id1": requests.AckRequest(
            ack_id="ack_id1",
            byte_size=0,
            time_to_ack=20,
            ordering_key="",
            future=future1,
        ),
        "ack_id2": requests.AckRequest(
            ack_id="ack_id2",
            byte_size=0,
            time_to_ack=20,
            ordering_key="",
            future=future2,
        ),
    }
    with pytest.raises(exceptions.RetryError):
        manager.send_unary_ack(
            ack_ids=["ack_id1", "ack_id2"], ack_reqs_dict=ack_reqs_dict
        )

    assert "RetryError while sending ack RPC" in caplog.text
    assert "signaled streaming pull manager shutdown" in caplog.text
    assert future1.result() == subscriber_exceptions.AcknowledgeStatus.SUCCESS
    assert future2.result() == subscriber_exceptions.AcknowledgeStatus.SUCCESS


def test_send_unary_ack_retry_error_exactly_once_enabled_no_futures(
    caplog, modify_google_logger_propagation
):
    caplog.set_level(logging.DEBUG)

    manager, _, _, _, _, _ = make_running_manager()
    manager._exactly_once_enabled = True

    error = exceptions.RetryError(
        "Too long a transient error", cause=Exception("Out of time!")
    )
    manager._client.acknowledge.side_effect = error

    ack_reqs_dict = {
        "ack_id1": requests.AckRequest(
            ack_id="ack_id1",
            byte_size=0,
            time_to_ack=20,
            ordering_key="",
            future=None,
        ),
        "ack_id2": requests.AckRequest(
            ack_id="ack_id2",
            byte_size=0,
            time_to_ack=20,
            ordering_key="",
            future=None,
        ),
    }
    with pytest.raises(exceptions.RetryError):
        manager.send_unary_ack(
            ack_ids=["ack_id1", "ack_id2"], ack_reqs_dict=ack_reqs_dict
        )

    assert "RetryError while sending ack RPC" in caplog.text
    assert "signaled streaming pull manager shutdown" in caplog.text


def test_send_unary_ack_retry_error_exactly_once_enabled_with_futures(
    caplog, modify_google_logger_propagation
):
    caplog.set_level(logging.DEBUG)

    manager, _, _, _, _, _ = make_running_manager()
    manager._exactly_once_enabled = True

    error = exceptions.RetryError(
        "Too long a transient error", cause=Exception("Out of time!")
    )
    manager._client.acknowledge.side_effect = error

    future1 = futures.Future()
    future2 = futures.Future()
    ack_reqs_dict = {
        "ack_id1": requests.AckRequest(
            ack_id="ack_id1",
            byte_size=0,
            time_to_ack=20,
            ordering_key="",
            future=future1,
        ),
        "ack_id2": requests.AckRequest(
            ack_id="ack_id2",
            byte_size=0,
            time_to_ack=20,
            ordering_key="",
            future=future2,
        ),
    }
    with pytest.raises(exceptions.RetryError):
        manager.send_unary_ack(
            ack_ids=["ack_id1", "ack_id2"], ack_reqs_dict=ack_reqs_dict
        )

    assert "RetryError while sending ack RPC" in caplog.text
    assert "signaled streaming pull manager shutdown" in caplog.text
    assert isinstance(future1.exception(), subscriber_exceptions.AcknowledgeError)
    assert (
        future1.exception().error_code is subscriber_exceptions.AcknowledgeStatus.OTHER
    )
    assert isinstance(future2.exception(), subscriber_exceptions.AcknowledgeError)
    assert (
        future2.exception().error_code is subscriber_exceptions.AcknowledgeStatus.OTHER
    )


def test_send_unary_modack_retry_error_exactly_once_disabled_no_future(
    caplog, modify_google_logger_propagation
):
    caplog.set_level(logging.DEBUG)

    manager, _, _, _, _, _ = make_running_manager()
    manager._exactly_once_enabled = False

    error = exceptions.RetryError(
        "Too long a transient error", cause=Exception("Out of time!")
    )
    manager._client.modify_ack_deadline.side_effect = error

    ack_reqs_dict = {
        "ackid1": requests.ModAckRequest(ack_id="ackid1", seconds=60, future=None)
    }
    with pytest.raises(exceptions.RetryError):
        manager.send_unary_modack(
            modify_deadline_ack_ids=["ackid1"],
            modify_deadline_seconds=[0],
            ack_reqs_dict=ack_reqs_dict,
        )

    assert "RetryError while sending modack RPC" in caplog.text
    assert "signaled streaming pull manager shutdown" in caplog.text


def test_send_unary_modack_retry_error_exactly_once_disabled_with_futures(
    caplog, modify_google_logger_propagation
):
    caplog.set_level(logging.DEBUG)

    manager, _, _, _, _, _ = make_running_manager()
    manager._exactly_once_enabled = False

    error = exceptions.RetryError(
        "Too long a transient error", cause=Exception("Out of time!")
    )
    manager._client.modify_ack_deadline.side_effect = error

    future = futures.Future()
    ack_reqs_dict = {
        "ackid1": requests.ModAckRequest(ack_id="ackid1", seconds=60, future=future)
    }
    with pytest.raises(exceptions.RetryError):
        manager.send_unary_modack(
            modify_deadline_ack_ids=["ackid1"],
            modify_deadline_seconds=[0],
            ack_reqs_dict=ack_reqs_dict,
        )

    assert "RetryError while sending modack RPC" in caplog.text
    assert "signaled streaming pull manager shutdown" in caplog.text
    assert future.result() == subscriber_exceptions.AcknowledgeStatus.SUCCESS


def test_send_unary_modack_retry_error_exactly_once_enabled_no_futures(
    caplog, modify_google_logger_propagation
):
    caplog.set_level(logging.DEBUG)

    manager, _, _, _, _, _ = make_running_manager()
    manager._exactly_once_enabled = True

    error = exceptions.RetryError(
        "Too long a transient error", cause=Exception("Out of time!")
    )
    manager._client.modify_ack_deadline.side_effect = error

    ack_reqs_dict = {
        "ackid1": requests.ModAckRequest(ack_id="ackid1", seconds=60, future=None)
    }
    with pytest.raises(exceptions.RetryError):
        manager.send_unary_modack(
            modify_deadline_ack_ids=["ackid1"],
            modify_deadline_seconds=[0],
            ack_reqs_dict=ack_reqs_dict,
        )

    assert "RetryError while sending modack RPC" in caplog.text
    assert "signaled streaming pull manager shutdown" in caplog.text


def test_send_unary_modack_retry_error_exactly_once_enabled_with_futures(
    caplog, modify_google_logger_propagation
):
    caplog.set_level(logging.DEBUG)

    manager, _, _, _, _, _ = make_running_manager()
    manager._exactly_once_enabled = True

    error = exceptions.RetryError(
        "Too long a transient error", cause=Exception("Out of time!")
    )
    manager._client.modify_ack_deadline.side_effect = error

    future = futures.Future()
    ack_reqs_dict = {
        "ackid1": requests.ModAckRequest(ack_id="ackid1", seconds=60, future=future)
    }
    with pytest.raises(exceptions.RetryError):
        manager.send_unary_modack(
            modify_deadline_ack_ids=["ackid1"],
            modify_deadline_seconds=[0],
            ack_reqs_dict=ack_reqs_dict,
        )

    assert "RetryError while sending modack RPC" in caplog.text
    assert "signaled streaming pull manager shutdown" in caplog.text
    assert isinstance(future.exception(), subscriber_exceptions.AcknowledgeError)
    assert (
        future.exception().error_code is subscriber_exceptions.AcknowledgeStatus.OTHER
    )


def test_heartbeat():
    manager = make_manager()
    manager._rpc = mock.create_autospec(bidi.BidiRpc, instance=True)
    manager._rpc.is_active = True

    result = manager.heartbeat()

    manager._rpc.send.assert_called_once_with(gapic_types.StreamingPullRequest())
    assert result


def test_heartbeat_inactive():
    manager = make_manager()
    manager._rpc = mock.create_autospec(bidi.BidiRpc, instance=True)
    manager._rpc.is_active = False

    manager.heartbeat()

    result = manager._rpc.send.assert_not_called()
    assert not result


def test_heartbeat_stream_ack_deadline_seconds(
    caplog, modify_google_logger_propagation
):
    caplog.set_level(logging.DEBUG)
    manager = make_manager()
    manager._rpc = mock.create_autospec(bidi.BidiRpc, instance=True)
    manager._rpc.is_active = True
    # Send new ack deadline with next heartbeat.
    manager._send_new_ack_deadline = True

    result = manager.heartbeat()

    manager._rpc.send.assert_called_once_with(
        gapic_types.StreamingPullRequest(stream_ack_deadline_seconds=60)
    )
    assert result
    # Set to false after a send is initiated.
    assert not manager._send_new_ack_deadline
    assert "Sending new ack_deadline of 60 seconds." in caplog.text


@mock.patch("google.api_core.bidi.ResumableBidiRpc", autospec=True)
@mock.patch("google.api_core.bidi.BackgroundConsumer", autospec=True)
@mock.patch("google.cloud.pubsub_v1.subscriber._protocol.leaser.Leaser", autospec=True)
@mock.patch(
    "google.cloud.pubsub_v1.subscriber._protocol.dispatcher.Dispatcher", autospec=True
)
@mock.patch(
    "google.cloud.pubsub_v1.subscriber._protocol.heartbeater.Heartbeater", autospec=True
)
def test_open(heartbeater, dispatcher, leaser, background_consumer, resumable_bidi_rpc):
    manager = make_manager()

    with mock.patch.object(
        type(manager), "ack_deadline", new=mock.PropertyMock(return_value=18)
    ):
        manager.open(mock.sentinel.callback, mock.sentinel.on_callback_error)

    heartbeater.assert_called_once_with(manager)
    heartbeater.return_value.start.assert_called_once()
    assert manager._heartbeater == heartbeater.return_value

    dispatcher.assert_called_once_with(manager, manager._scheduler.queue)
    dispatcher.return_value.start.assert_called_once()
    assert manager._dispatcher == dispatcher.return_value

    leaser.assert_called_once_with(manager)
    leaser.return_value.start.assert_called_once()
    assert manager.leaser == leaser.return_value

    if streaming_pull_manager._SHOULD_USE_ON_FATAL_ERROR_CALLBACK:
        background_consumer.assert_called_once_with(
            manager._rpc, manager._on_response, manager._on_fatal_exception
        )
    else:
        background_consumer.assert_called_once_with(manager._rpc, manager._on_response)

    background_consumer.return_value.start.assert_called_once()
    assert manager._consumer == background_consumer.return_value

    resumable_bidi_rpc.assert_called_once_with(
        start_rpc=manager._client.streaming_pull,
        initial_request=mock.ANY,
        should_recover=manager._should_recover,
        should_terminate=manager._should_terminate,
        metadata=manager._stream_metadata,
        throttle_reopen=True,
    )
    initial_request_arg = resumable_bidi_rpc.call_args.kwargs["initial_request"]
    assert initial_request_arg.func == manager._get_initial_request
    assert initial_request_arg.args[0] == 60
    assert not manager._client.get_subscription.called

    resumable_bidi_rpc.return_value.add_done_callback.assert_called_once_with(
        manager._on_rpc_done
    )
    assert manager._rpc == resumable_bidi_rpc.return_value

    manager._consumer.is_active = True
    assert manager.is_active is True


def test_open_already_active():
    manager = make_manager()
    manager._consumer = mock.create_autospec(bidi.BackgroundConsumer, instance=True)
    manager._consumer.is_active = True

    with pytest.raises(ValueError, match="already open"):
        manager.open(mock.sentinel.callback, mock.sentinel.on_callback_error)


def test_open_has_been_closed():
    manager = make_manager()
    manager._closed = True

    with pytest.raises(ValueError, match="closed"):
        manager.open(mock.sentinel.callback, mock.sentinel.on_callback_error)


def make_running_manager(
    enable_open_telemetry: bool = False,
    subscription_name: str = "subscription-name",
    **kwargs,
):
    manager = make_manager(enable_open_telemetry, subscription_name, **kwargs)
    manager._consumer = mock.create_autospec(bidi.BackgroundConsumer, instance=True)
    manager._consumer.is_active = True
    manager._dispatcher = mock.create_autospec(dispatcher.Dispatcher, instance=True)
    manager._leaser = mock.create_autospec(leaser.Leaser, instance=True)
    manager._heartbeater = mock.create_autospec(heartbeater.Heartbeater, instance=True)
    return (
        manager,
        manager._consumer,
        manager._dispatcher,
        manager._leaser,
        manager._heartbeater,
        manager._scheduler,
    )


def await_manager_shutdown(manager, timeout=None):
    # NOTE: This method should be called after manager.close(), i.e. after the shutdown
    # thread has been created and started.
    shutdown_thread = manager._regular_shutdown_thread

    if shutdown_thread is None:  # pragma: NO COVER
        raise Exception("Shutdown thread does not exist on the manager instance.")

    shutdown_thread.join(timeout=timeout)
    if shutdown_thread.is_alive():  # pragma: NO COVER
        pytest.fail("Shutdown not completed in time.")


def test_close():
    (
        manager,
        consumer,
        dispatcher,
        leaser,
        heartbeater,
        scheduler,
    ) = make_running_manager()

    manager.close()
    await_manager_shutdown(manager, timeout=3)

    consumer.stop.assert_called_once()
    leaser.stop.assert_called_once()
    dispatcher.stop.assert_called_once()
    heartbeater.stop.assert_called_once()
    scheduler.shutdown.assert_called_once()

    assert manager.is_active is False


def test_closes_on_fatal_consumer_error():
    (
        manager,
        consumer,
        dispatcher,
        leaser,
        heartbeater,
        scheduler,
    ) = make_running_manager()

    if streaming_pull_manager._SHOULD_USE_ON_FATAL_ERROR_CALLBACK:
        error = ValueError("some fatal exception")
        manager._on_fatal_exception(error)

        await_manager_shutdown(manager, timeout=3)

        consumer.stop.assert_called_once()
        leaser.stop.assert_called_once()
        dispatcher.stop.assert_called_once()
        heartbeater.stop.assert_called_once()
        scheduler.shutdown.assert_called_once()

        assert manager.is_active is False


def test_close_inactive_consumer():
    (
        manager,
        consumer,
        dispatcher,
        leaser,
        heartbeater,
        scheduler,
    ) = make_running_manager()
    consumer.is_active = False

    manager.close()
    await_manager_shutdown(manager, timeout=3)

    consumer.stop.assert_not_called()
    leaser.stop.assert_called_once()
    dispatcher.stop.assert_called_once()
    heartbeater.stop.assert_called_once()
    scheduler.shutdown.assert_called_once()


def test_close_idempotent():
    manager, _, _, _, _, scheduler = make_running_manager()

    manager.close()
    manager.close()
    await_manager_shutdown(manager, timeout=3)

    assert scheduler.shutdown.call_count == 1


class FakeDispatcher(object):
    def __init__(self, manager, error_callback):
        self._manager = manager
        self._error_callback = error_callback
        self._thread = None
        self._stop = False

    def start(self):
        self._thread = threading.Thread(target=self._do_work)
        self._thread.daemon = True
        self._thread.start()

    def stop(self):
        self._stop = True
        self._thread.join()
        self._thread = None

    def _do_work(self):
        while not self._stop:
            try:
                self._manager.leaser.add([mock.Mock()])
            except Exception as exc:  # pragma: NO COVER
                self._error_callback(exc)
            time.sleep(0.1)

        # also try to interact with the leaser after the stop flag has been set
        try:
            self._manager.leaser.remove([mock.Mock()])
        except Exception as exc:  # pragma: NO COVER
            self._error_callback(exc)


def test_close_no_dispatcher_error():
    manager, _, _, _, _, _ = make_running_manager()
    error_callback = mock.Mock(name="error_callback")
    dispatcher = FakeDispatcher(manager=manager, error_callback=error_callback)
    manager._dispatcher = dispatcher
    dispatcher.start()

    manager.close()
    await_manager_shutdown(manager, timeout=3)

    error_callback.assert_not_called()


def test_close_callbacks():
    manager, _, _, _, _, _ = make_running_manager()

    callback = mock.Mock()

    manager.add_close_callback(callback)
    manager.close(reason="meep")
    await_manager_shutdown(manager, timeout=3)

    callback.assert_called_once_with(manager, "meep")


def test_close_blocking_scheduler_shutdown():
    manager, _, _, _, _, _ = make_running_manager(await_callbacks_on_shutdown=True)
    scheduler = manager._scheduler

    manager.close()
    await_manager_shutdown(manager, timeout=3)

    scheduler.shutdown.assert_called_once_with(await_msg_callbacks=True)


def test__on_response_none_scheduler():
    manager, _, _, _, _, _ = make_running_manager()

    manager._callback = mock.sentinel.callback
    manager._scheduler = None
    # Set up the messages.
    response = gapic_types.StreamingPullResponse(
        received_messages=[
            gapic_types.ReceivedMessage(
                ack_id="ack1",
                message=gapic_types.PubsubMessage(data=b"foo", message_id="1"),
            ),
            gapic_types.ReceivedMessage(
                ack_id="ack2",
                message=gapic_types.PubsubMessage(data=b"bar", message_id="2"),
                delivery_attempt=6,
            ),
        ]
    )

    manager._maybe_release_messages = mock.Mock()

    # adjust message bookkeeping in leaser
    fake_leaser_add(leaser, init_msg_count=0, assumed_msg_size=42)
    manager._on_response(response)

    manager._maybe_release_messages.assert_not_called


def test__on_response_none_leaser():
    manager, _, _, _, _, _ = make_running_manager()

    manager._callback = mock.sentinel.callback
    manager._leaser = None
    # Set up the messages.
    response = gapic_types.StreamingPullResponse(
        received_messages=[
            gapic_types.ReceivedMessage(
                ack_id="ack1",
                message=gapic_types.PubsubMessage(data=b"foo", message_id="1"),
            ),
            gapic_types.ReceivedMessage(
                ack_id="ack2",
                message=gapic_types.PubsubMessage(data=b"bar", message_id="2"),
                delivery_attempt=6,
            ),
        ]
    )

    manager._maybe_release_messages = mock.Mock()

    manager._on_response(response)

    manager._maybe_release_messages.assert_not_called


def test_close_nonblocking_scheduler_shutdown():
    manager, _, _, _, _, _ = make_running_manager(await_callbacks_on_shutdown=False)
    scheduler = manager._scheduler

    manager.close()
    await_manager_shutdown(manager, timeout=3)

    scheduler.shutdown.assert_called_once_with(await_msg_callbacks=False)


def test_close_nacks_internally_queued_messages():
    nacked_messages = []

    def fake_nack(self):
        nacked_messages.append(self.data)

    messages = [
        create_message(data=b"msg1"),
        create_message(data=b"msg2"),
        create_message(data=b"msg3"),
    ]
    for msg in messages:
        msg.nack = stdlib_types.MethodType(fake_nack, msg)

    manager, _, _, _, _, _ = make_running_manager()
    dropped_by_scheduler = messages[:2]
    manager._scheduler.shutdown.return_value = dropped_by_scheduler
    manager._messages_on_hold._messages_on_hold.append(messages[2])

    manager.close()
    await_manager_shutdown(manager, timeout=3)

    assert sorted(nacked_messages) == [b"msg1", b"msg2", b"msg3"]


def test__get_initial_request():
    manager = make_manager()
    manager._leaser = mock.create_autospec(leaser.Leaser, instance=True)
    manager._leaser.ack_ids = ["1", "2"]

    initial_request = manager._get_initial_request(123)

    assert isinstance(initial_request, gapic_types.StreamingPullRequest)
    assert initial_request.subscription == "subscription-name"
    assert initial_request.stream_ack_deadline_seconds == 123
    assert initial_request.modify_deadline_ack_ids == []
    assert initial_request.modify_deadline_seconds == []


def test__get_initial_request_wo_leaser():
    manager = make_manager()
    manager._leaser = None

    initial_request = manager._get_initial_request(123)

    assert isinstance(initial_request, gapic_types.StreamingPullRequest)
    assert initial_request.subscription == "subscription-name"
    assert initial_request.stream_ack_deadline_seconds == 123
    assert initial_request.modify_deadline_ack_ids == []
    assert initial_request.modify_deadline_seconds == []


def test__on_response_delivery_attempt():
    manager, _, dispatcher, leaser, _, scheduler = make_running_manager()
    manager._callback = mock.sentinel.callback

    # Set up the messages.
    response = gapic_types.StreamingPullResponse(
        received_messages=[
            gapic_types.ReceivedMessage(
                ack_id="fack",
                message=gapic_types.PubsubMessage(data=b"foo", message_id="1"),
            ),
            gapic_types.ReceivedMessage(
                ack_id="back",
                message=gapic_types.PubsubMessage(data=b"bar", message_id="2"),
                delivery_attempt=6,
            ),
        ]
    )

    # adjust message bookkeeping in leaser
    fake_leaser_add(leaser, init_msg_count=0, assumed_msg_size=42)

    manager._on_response(response)

    schedule_calls = scheduler.schedule.mock_calls
    assert len(schedule_calls) == 2
    msg1 = schedule_calls[0][1][1]
    assert msg1.delivery_attempt is None
    msg2 = schedule_calls[1][1][1]
    assert msg2.delivery_attempt == 6


def test__on_response_modifies_ack_deadline():
    manager, _, dispatcher, leaser, _, scheduler = make_running_manager()
    manager._callback = mock.sentinel.callback

    # Set up the messages.
    response = gapic_types.StreamingPullResponse(
        received_messages=[
            gapic_types.ReceivedMessage(
                ack_id="ack_1",
                message=gapic_types.PubsubMessage(data=b"foo", message_id="1"),
            ),
            gapic_types.ReceivedMessage(
                ack_id="ack_2",
                message=gapic_types.PubsubMessage(data=b"bar", message_id="2"),
            ),
        ]
    )

    # adjust message bookkeeping in leaser
    fake_leaser_add(leaser, init_msg_count=0, assumed_msg_size=80)

    # Actually run the method and chack that correct MODACK value is used.
    with mock.patch.object(
        type(manager), "ack_deadline", new=mock.PropertyMock(return_value=18)
    ):
        manager._on_response(response)

    dispatcher.modify_ack_deadline.assert_called_once_with(
        [
            requests.ModAckRequest("ack_1", 18, None),
            requests.ModAckRequest("ack_2", 18, None),
        ],
        18,
    )


def test__on_response_modifies_ack_deadline_with_exactly_once_min_lease():
    # exactly_once is disabled by default.
    manager, _, dispatcher, leaser, _, scheduler = make_running_manager()
    manager._callback = mock.sentinel.callback
    complete_modify_ack_deadline_calls(dispatcher)

    # make p99 value smaller than exactly_once min lease
    manager.ack_histogram.add(10)

    # adjust message bookkeeping in leaser
    fake_leaser_add(leaser, init_msg_count=0, assumed_msg_size=42)

    # Set up the response with the first set of messages and exactly_once not
    # enabled.
    response1 = gapic_types.StreamingPullResponse(
        received_messages=[
            gapic_types.ReceivedMessage(
                ack_id="ack_1",
                message=gapic_types.PubsubMessage(data=b"foo", message_id="1"),
            ),
            gapic_types.ReceivedMessage(
                ack_id="ack_2",
                message=gapic_types.PubsubMessage(data=b"bar", message_id="2"),
            ),
        ],
        subscription_properties=gapic_types.StreamingPullResponse.SubscriptionProperties(
            exactly_once_delivery_enabled=False
        ),
    )

    # Set up the response with the second set of messages and exactly_once enabled.
    response2 = gapic_types.StreamingPullResponse(
        received_messages=[
            gapic_types.ReceivedMessage(
                ack_id="ack_3",
                message=gapic_types.PubsubMessage(data=b"foo", message_id="1"),
            ),
            gapic_types.ReceivedMessage(
                ack_id="ack_4",
                message=gapic_types.PubsubMessage(data=b"bar", message_id="2"),
            ),
        ],
        subscription_properties=gapic_types.StreamingPullResponse.SubscriptionProperties(
            exactly_once_delivery_enabled=True
        ),
    )

    # exactly_once is still disabled b/c subscription_properties says so
    manager._on_response(response1)

    # expect mod-acks are called with histogram-based lease value
    assert len(dispatcher.modify_ack_deadline.mock_calls) == 1
    call = dispatcher.modify_ack_deadline.mock_calls[0]
    assert call.args[0] == [
        requests.ModAckRequest("ack_1", 10, None),
        requests.ModAckRequest("ack_2", 10, None),
    ]
    assert call.args[1] == 10

    # exactly_once should be enabled after this request b/c subscription_properties says so
    manager._on_response(response2)

    # expect mod-acks called with 60 sec min lease value for exactly_once subscriptions
    # ignore the futures here
    assert len(dispatcher.modify_ack_deadline.mock_calls) == 2
    call = dispatcher.modify_ack_deadline.mock_calls[1]
    modack_reqs = call.args[0]
    assert modack_reqs[0].ack_id == "ack_3"
    assert modack_reqs[0].seconds == 60
    assert modack_reqs[1].ack_id == "ack_4"
    assert modack_reqs[1].seconds == 60
    modack_deadline = call.args[1]
    assert modack_deadline == 60


def test__on_response_send_ack_deadline_after_enabling_exactly_once():
    # exactly_once is disabled by default.
    manager, _, dispatcher, leaser, _, scheduler = make_running_manager()
    manager._callback = mock.sentinel.callback
    complete_modify_ack_deadline_calls(dispatcher)

    # set up an active RPC
    manager._rpc = mock.create_autospec(bidi.BidiRpc, instance=True)
    manager._rpc.is_active = True

    # make p99 value smaller than exactly_once min lease
    manager.ack_histogram.add(10)

    # adjust message bookkeeping in leaser
    fake_leaser_add(leaser, init_msg_count=0, assumed_msg_size=42)

    # Set up the response with the a message and exactly_once enabled.
    response2 = gapic_types.StreamingPullResponse(
        received_messages=[
            gapic_types.ReceivedMessage(
                ack_id="ack_1",
                message=gapic_types.PubsubMessage(data=b"foo", message_id="1"),
            )
        ],
        subscription_properties=gapic_types.StreamingPullResponse.SubscriptionProperties(
            exactly_once_delivery_enabled=True
        ),
    )

    # exactly_once should be enabled after this request b/c subscription_properties says so
    # when exactly_once is enabled or disabled, we send a new ack_deadline via
    # the heartbeat
    # should satisfy assertion 1
    manager._on_response(response2)

    # simulate periodic heartbeat trigger
    heartbeat_request_sent = manager.heartbeat()
    assert heartbeat_request_sent

    # heartbeat request is sent with the 60 sec min lease value for exactly_once subscriptions
    manager._rpc.send.assert_called_once_with(
        gapic_types.StreamingPullRequest(stream_ack_deadline_seconds=60)
    )


def test__on_response_no_leaser_overload():
    manager, _, dispatcher, leaser, _, scheduler = make_running_manager()
    manager._callback = mock.sentinel.callback

    # Set up the messages.
    response = gapic_types.StreamingPullResponse(
        received_messages=[
            gapic_types.ReceivedMessage(
                ack_id="fack",
                message=gapic_types.PubsubMessage(data=b"foo", message_id="1"),
            ),
            gapic_types.ReceivedMessage(
                ack_id="back",
                message=gapic_types.PubsubMessage(data=b"bar", message_id="2"),
            ),
        ]
    )

    # adjust message bookkeeping in leaser
    fake_leaser_add(leaser, init_msg_count=0, assumed_msg_size=42)

    # Actually run the method and prove that modack and schedule
    # are called in the expected way.
    manager._on_response(response)

    dispatcher.modify_ack_deadline.assert_called_once_with(
        [
            requests.ModAckRequest("fack", 10, None),
            requests.ModAckRequest("back", 10, None),
        ],
        10,
    )

    schedule_calls = scheduler.schedule.mock_calls
    assert len(schedule_calls) == 2
    for call in schedule_calls:
        assert call[1][0] == mock.sentinel.callback
        assert isinstance(call[1][1], message.Message)

    # the leaser load limit not hit, no messages had to be put on hold
    assert manager._messages_on_hold.size == 0


def test__on_response_with_leaser_overload():
    manager, _, dispatcher, leaser, _, scheduler = make_running_manager()
    manager._callback = mock.sentinel.callback

    # Set up the messages.
    response = gapic_types.StreamingPullResponse(
        received_messages=[
            gapic_types.ReceivedMessage(
                ack_id="fack",
                message=gapic_types.PubsubMessage(data=b"foo", message_id="1"),
            ),
            gapic_types.ReceivedMessage(
                ack_id="back",
                message=gapic_types.PubsubMessage(data=b"bar", message_id="2"),
            ),
            gapic_types.ReceivedMessage(
                ack_id="zack",
                message=gapic_types.PubsubMessage(data=b"baz", message_id="3"),
            ),
        ]
    )

    # Adjust message bookkeeping in leaser. Pick 999 messages, which is just below
    # the default FlowControl.max_messages limit.
    fake_leaser_add(leaser, init_msg_count=999, assumed_msg_size=10)

    # Actually run the method and prove that modack and schedule
    # are called in the expected way.
    manager._on_response(response)

    # all messages should be added to the lease management and have their ACK
    # deadline extended, even those not dispatched to callbacks
    dispatcher.modify_ack_deadline.assert_called_once_with(
        [
            requests.ModAckRequest("fack", 10, None),
            requests.ModAckRequest("back", 10, None),
            requests.ModAckRequest("zack", 10, None),
        ],
        10,
    )

    # one message should be scheduled, the flow control limits allow for it
    schedule_calls = scheduler.schedule.mock_calls
    assert len(schedule_calls) == 1
    call_args = schedule_calls[0][1]
    assert call_args[0] == mock.sentinel.callback
    assert isinstance(call_args[1], message.Message)
    assert call_args[1].message_id == "1"

    # the rest of the messages should have been put on hold
    assert manager._messages_on_hold.size == 2
    while True:
        msg = manager._messages_on_hold.get()
        if msg is None:
            break
        else:
            assert isinstance(msg, message.Message)
            assert msg.message_id in ("2", "3")


def test__on_response_none_data(caplog, modify_google_logger_propagation):
    caplog.set_level(logging.DEBUG)

    manager, _, dispatcher, leaser, _, scheduler = make_running_manager()
    manager._callback = mock.sentinel.callback

    # adjust message bookkeeping in leaser
    fake_leaser_add(leaser, init_msg_count=0, assumed_msg_size=10)

    manager._on_response(response=None)

    scheduler.schedule.assert_not_called()
    assert "callback invoked with None" in caplog.text


def test__on_response_with_ordering_keys():
    manager, _, dispatcher, leaser, _, scheduler = make_running_manager()
    manager._callback = mock.sentinel.callback

    # Set up the messages.
    response = gapic_types.StreamingPullResponse(
        received_messages=[
            gapic_types.ReceivedMessage(
                ack_id="fack",
                message=gapic_types.PubsubMessage(
                    data=b"foo", message_id="1", ordering_key=""
                ),
            ),
            gapic_types.ReceivedMessage(
                ack_id="back",
                message=gapic_types.PubsubMessage(
                    data=b"bar", message_id="2", ordering_key="key1"
                ),
            ),
            gapic_types.ReceivedMessage(
                ack_id="zack",
                message=gapic_types.PubsubMessage(
                    data=b"baz", message_id="3", ordering_key="key1"
                ),
            ),
        ]
    )

    # Make leaser with zero initial messages, so we don't test lease management
    # behavior.
    fake_leaser_add(leaser, init_msg_count=0, assumed_msg_size=10)

    # Actually run the method and prove that modack and schedule are called in
    # the expected way.
    manager._on_response(response)

    # All messages should be added to the lease management and have their ACK
    # deadline extended, even those not dispatched to callbacks.
    dispatcher.modify_ack_deadline.assert_called_once_with(
        [
            requests.ModAckRequest("fack", 10, None),
            requests.ModAckRequest("back", 10, None),
            requests.ModAckRequest("zack", 10, None),
        ],
        10,
    )

    # The first two messages should be scheduled, The third should be put on
    # hold because it's blocked by the completion of the second, which has the
    # same ordering key.
    schedule_calls = scheduler.schedule.mock_calls
    assert len(schedule_calls) == 2
    call_args = schedule_calls[0][1]
    assert call_args[0] == mock.sentinel.callback
    assert isinstance(call_args[1], message.Message)
    assert call_args[1].message_id == "1"

    call_args = schedule_calls[1][1]
    assert call_args[0] == mock.sentinel.callback
    assert isinstance(call_args[1], message.Message)
    assert call_args[1].message_id == "2"

    # Message 3 should have been put on hold.
    assert manager._messages_on_hold.size == 1
    # No messages available because message 2 (with "key1") has not completed yet.
    assert manager._messages_on_hold.get() is None

    # Complete message 2 (with "key1").
    manager.activate_ordering_keys(["key1"])

    # Completing message 2 should release message 3.
    schedule_calls = scheduler.schedule.mock_calls
    assert len(schedule_calls) == 3
    call_args = schedule_calls[2][1]
    assert call_args[0] == mock.sentinel.callback
    assert isinstance(call_args[1], message.Message)
    assert call_args[1].message_id == "3"

    # No messages available in the queue.
    assert manager._messages_on_hold.get() is None


def test__on_response_enable_exactly_once():
    manager, _, dispatcher, leaser, _, scheduler = make_running_manager()
    manager._callback = mock.sentinel.callback
    complete_modify_ack_deadline_calls(dispatcher)

    # Set up the messages.
    response = gapic_types.StreamingPullResponse(
        received_messages=[
            gapic_types.ReceivedMessage(
                ack_id="fack",
                message=gapic_types.PubsubMessage(data=b"foo", message_id="1"),
            )
        ],
        subscription_properties=gapic_types.StreamingPullResponse.SubscriptionProperties(
            exactly_once_delivery_enabled=True
        ),
    )

    # adjust message bookkeeping in leaser
    fake_leaser_add(leaser, init_msg_count=0, assumed_msg_size=42)

    # exactly_once should be enabled
    manager._on_response(response)

    assert manager._exactly_once_delivery_enabled()
    # new deadline for exactly_once subscriptions should be used
    assert manager.ack_deadline == 60


def test__on_response_disable_exactly_once():
    from google.cloud.pubsub_v1.subscriber._protocol import histogram

    manager, _, dispatcher, leaser, _, scheduler = make_running_manager()
    manager._callback = mock.sentinel.callback

    manager._flow_control = types.FlowControl(
        min_duration_per_lease_extension=histogram.MIN_ACK_DEADLINE
    )
    # enable exactly_once
    manager._exactly_once_enabled = True

    # Set up the messages.
    response = gapic_types.StreamingPullResponse(
        received_messages=[
            gapic_types.ReceivedMessage(
                ack_id="fack",
                message=gapic_types.PubsubMessage(data=b"foo", message_id="1"),
            )
        ],
        subscription_properties=gapic_types.StreamingPullResponse.SubscriptionProperties(
            exactly_once_delivery_enabled=False
        ),
    )

    # adjust message bookkeeping in leaser
    fake_leaser_add(leaser, init_msg_count=0, assumed_msg_size=42)

    # exactly_once should be disabled
    manager._on_response(response)

    assert not manager._exactly_once_enabled
    # The deadline configured in flow control should be used, not the
    # exactly_once minimum since exactly_once has been disabled.
    deadline = manager._obtain_ack_deadline(maybe_update=True)
    assert deadline == histogram.MIN_ACK_DEADLINE
    assert manager._stream_ack_deadline == 60


def test__on_response_exactly_once_immediate_modacks_fail(
    caplog,
    modify_google_logger_propagation,
):
    manager, _, dispatcher, leaser, _, scheduler = make_running_manager()
    manager._callback = mock.sentinel.callback

    def complete_futures_with_error(*args, **kwargs):
        modack_requests = args[0]
        for req in modack_requests:
            if req.ack_id == "fack":
                req.future.set_exception(
                    subscriber_exceptions.AcknowledgeError(
                        subscriber_exceptions.AcknowledgeStatus.INVALID_ACK_ID, None
                    )
                )
            else:
                req.future.set_exception(
                    subscriber_exceptions.AcknowledgeError(
                        subscriber_exceptions.AcknowledgeStatus.SUCCESS, None
                    )
                )

    dispatcher.modify_ack_deadline.side_effect = complete_futures_with_error

    # Set up the messages.
    response = gapic_types.StreamingPullResponse(
        received_messages=[
            gapic_types.ReceivedMessage(
                ack_id="fack",
                message=gapic_types.PubsubMessage(data=b"foo", message_id="1"),
            ),
            gapic_types.ReceivedMessage(
                ack_id="good",
                message=gapic_types.PubsubMessage(data=b"foo", message_id="2"),
            ),
        ],
        subscription_properties=gapic_types.StreamingPullResponse.SubscriptionProperties(
            exactly_once_delivery_enabled=True
        ),
    )

    # Actually run the method and prove that modack and schedule are called in
    # the expected way.

    fake_leaser_add(leaser, init_msg_count=0, assumed_msg_size=10)

    with caplog.at_level(logging.WARNING):
        manager._on_response(response)

    # The second messages should be scheduled, and not the first.

    schedule_calls = scheduler.schedule.mock_calls
    assert len(schedule_calls) == 1
    call_args = schedule_calls[0][1]
    assert call_args[0] == mock.sentinel.callback
    assert isinstance(call_args[1], message.Message)
    assert call_args[1].message_id == "2"

    assert manager._messages_on_hold.size == 0

    expected_warnings = [
        record.message.lower()
        for record in caplog.records
        if "AcknowledgeError when lease-modacking a message." in record.message
    ]
    assert len(expected_warnings) == 1

    # No messages available
    assert manager._messages_on_hold.get() is None

    # do not add message
    assert manager.load == 0.001


def test__on_response_exactly_once_immediate_modacks_fail_non_invalid(
    caplog, modify_google_logger_propagation
):
    manager, _, dispatcher, leaser, _, scheduler = make_running_manager()
    manager._callback = mock.sentinel.callback

    def complete_futures_with_error(*args, **kwargs):
        modack_requests = args[0]
        for req in modack_requests:
            if req.ack_id == "fack":
                req.future.set_exception(
                    subscriber_exceptions.AcknowledgeError(
                        subscriber_exceptions.AcknowledgeStatus.OTHER, None
                    )
                )
            else:
                req.future.set_exception(
                    subscriber_exceptions.AcknowledgeError(
                        subscriber_exceptions.AcknowledgeStatus.SUCCESS, None
                    )
                )

    dispatcher.modify_ack_deadline.side_effect = complete_futures_with_error

    # Set up the messages.
    response = gapic_types.StreamingPullResponse(
        received_messages=[
            gapic_types.ReceivedMessage(
                ack_id="fack",
                message=gapic_types.PubsubMessage(data=b"foo", message_id="1"),
            ),
            gapic_types.ReceivedMessage(
                ack_id="good",
                message=gapic_types.PubsubMessage(data=b"foo", message_id="2"),
            ),
        ],
        subscription_properties=gapic_types.StreamingPullResponse.SubscriptionProperties(
            exactly_once_delivery_enabled=True
        ),
    )

    # Actually run the method and prove that modack and schedule are called in
    # the expected way.

    fake_leaser_add(leaser, init_msg_count=0, assumed_msg_size=10)

    with caplog.at_level(logging.WARNING):
        manager._on_response(response)

    # The second messages should be scheduled, and not the first.

    schedule_calls = scheduler.schedule.mock_calls
    assert len(schedule_calls) == 2
    call_args = schedule_calls[0][1]
    assert call_args[0] == mock.sentinel.callback
    assert isinstance(call_args[1], message.Message)
    assert call_args[1].message_id == "1"

    assert manager._messages_on_hold.size == 0

    expected_warnings = [
        record.message.lower()
        for record in caplog.records
        if "AcknowledgeError when lease-modacking a message." in record.message
    ]
    assert len(expected_warnings) == 2

    # No messages available
    assert manager._messages_on_hold.get() is None

    # do not add message
    assert manager.load == 0.002


def test__should_recover_true():
    manager = make_manager()

    details = "UNAVAILABLE. Service taking nap."
    exc = exceptions.ServiceUnavailable(details)

    assert manager._should_recover(exc) is True


def test__should_recover_false():
    manager = make_manager()

    exc = TypeError("wahhhhhh")

    assert manager._should_recover(exc) is False


def test__should_terminate_true():
    manager = make_manager()

    for exc in [
        exceptions.Cancelled(""),
        exceptions.PermissionDenied(""),
        TypeError(),
        ValueError(),
    ]:
        assert manager._should_terminate(exc)


def test__should_terminate_false():
    manager = make_manager()

    for exc in [
        exceptions.ResourceExhausted(""),
        exceptions.ServiceUnavailable(""),
        exceptions.DeadlineExceeded(""),
    ]:
        assert not manager._should_terminate(exc)


@mock.patch("threading.Thread", autospec=True)
def test__on_rpc_done(thread):
    manager = make_manager()

    manager._on_rpc_done(mock.sentinel.error)

    thread.assert_called_once_with(
        name=mock.ANY, target=manager._shutdown, kwargs={"reason": mock.ANY}
    )
    _, kwargs = thread.call_args
    reason = kwargs["kwargs"]["reason"]
    assert isinstance(reason, Exception)
    assert reason.args == (mock.sentinel.error,)  # Exception wraps the original error


def test_activate_ordering_keys():
    manager = make_manager()
    manager._messages_on_hold = mock.create_autospec(
        messages_on_hold.MessagesOnHold, instance=True
    )

    manager.activate_ordering_keys(["key1", "key2"])

    manager._messages_on_hold.activate_ordering_keys.assert_called_once_with(
        ["key1", "key2"], mock.ANY
    )


def test_activate_ordering_keys_stopped_scheduler():
    manager = make_manager()
    manager._messages_on_hold = mock.create_autospec(
        messages_on_hold.MessagesOnHold, instance=True
    )
    manager._scheduler = None

    manager.activate_ordering_keys(["key1", "key2"])

    manager._messages_on_hold.activate_ordering_keys.assert_not_called()


@mock.patch("grpc_status.rpc_status.from_call")
@mock.patch("google.protobuf.any_pb2.Any.Unpack")
def test_get_ack_errors_unable_to_unpack(from_call, unpack):
    st = status_pb2.Status()
    st.code = code_pb2.Code.INTERNAL
    st.message = "qmsg"
    error_info = error_details_pb2.ErrorInfo()
    error_info.metadata["ack_1"] = "error1"
    st.details.add().Pack(error_info)
    mock_gprc_call = mock.Mock(spec=grpc.Call)
    exception = exceptions.InternalServerError(
        "msg", errors=(), response=mock_gprc_call
    )
    from_call.return_value = st
    # Unpack() failed
    unpack.return_value = None

    assert not streaming_pull_manager._get_ack_errors(exception)


@mock.patch("grpc_status.rpc_status.from_call")
def test_get_ack_errors_no_response_obj(from_call):
    exception = exceptions.InternalServerError("msg", errors=(), response=None)
    # No response obj
    assert not streaming_pull_manager._get_ack_errors(exception)


@mock.patch("grpc_status.rpc_status.from_call")
def test_get_ack_errors_from_call_returned_none(from_call):
    mock_gprc_call = mock.Mock(spec=grpc.Call)
    exception = exceptions.InternalServerError(
        "msg", errors=(), response=mock_gprc_call
    )
    from_call.return_value = None
    # rpc_status.from_call() returned None
    assert not streaming_pull_manager._get_ack_errors(exception)


@mock.patch("grpc_status.rpc_status.from_call")
def test_get_ack_errors_value_error_thrown(from_call):
    mock_gprc_call = mock.Mock(spec=grpc.Call)
    exception = exceptions.InternalServerError(
        "msg", errors=(), response=mock_gprc_call
    )
    from_call.side_effect = ValueError("val error msg")
    # ValueError thrown, so return None
    assert not streaming_pull_manager._get_ack_errors(exception)


@mock.patch("grpc_status.rpc_status.from_call")
def test_get_ack_errors_no_error_details(from_call):
    st = status_pb2.Status()
    st.code = code_pb2.Code.INTERNAL
    st.message = "qmsg"
    mock_gprc_call = mock.Mock(spec=grpc.Call)
    exception = exceptions.InternalServerError(
        "msg", errors=(), response=mock_gprc_call
    )
    from_call.side_effect = None
    from_call.return_value = st
    # status has no details to extract exactly-once error info from
    assert not streaming_pull_manager._get_ack_errors(exception)


@mock.patch("grpc_status.rpc_status.from_call")
def test_get_ack_errors_detail_not_error_info(from_call):
    st = status_pb2.Status()
    st.code = code_pb2.Code.INTERNAL
    st.message = "qmsg"
    # pack a dummy status instead of an ErrorInfo
    dummy_status = status_pb2.Status()
    st.details.add().Pack(dummy_status)
    mock_gprc_call = mock.Mock(spec=grpc.Call)
    exception = exceptions.InternalServerError(
        "msg", errors=(), response=mock_gprc_call
    )
    from_call.side_effect = None
    from_call.return_value = st
    assert not streaming_pull_manager._get_ack_errors(exception)


@mock.patch("grpc_status.rpc_status.from_call")
def test_get_ack_errors_happy_case(from_call):
    st = status_pb2.Status()
    st.code = code_pb2.Code.INTERNAL
    st.message = "qmsg"
    error_info = error_details_pb2.ErrorInfo()
    error_info.metadata["ack_1"] = "error1"
    st.details.add().Pack(error_info)
    mock_gprc_call = mock.Mock(spec=grpc.Call)
    exception = exceptions.InternalServerError(
        "msg", errors=(), response=mock_gprc_call
    )
    from_call.side_effect = None
    from_call.return_value = st
    # happy case - errors returned in a map
    ack_errors = streaming_pull_manager._get_ack_errors(exception)
    assert ack_errors
    assert ack_errors["ack_1"] == "error1"


def test_process_requests_no_requests():
    # no requests so no items in results lists
    ack_reqs_dict = {}
    errors_dict = {}
    requests_completed, requests_to_retry = streaming_pull_manager._process_requests(
        None, ack_reqs_dict, errors_dict
    )
    assert not requests_completed
    assert not requests_to_retry


def test_process_requests_error_dict_is_none():
    # it's valid to pass in `None` for `errors_dict`
    ack_reqs_dict = {}
    errors_dict = None
    requests_completed, requests_to_retry = streaming_pull_manager._process_requests(
        None, ack_reqs_dict, errors_dict
    )
    assert not requests_completed
    assert not requests_to_retry


def test_process_requests_no_errors_has_no_future():
    # no errors so request should be completed, even with no future
    ack_reqs_dict = {
        "ackid1": requests.AckRequest(
            ack_id="ackid1", byte_size=0, time_to_ack=20, ordering_key="", future=None
        )
    }
    errors_dict = {}
    requests_completed, requests_to_retry = streaming_pull_manager._process_requests(
        None, ack_reqs_dict, errors_dict
    )
    assert requests_completed[0].ack_id == "ackid1"
    assert not requests_to_retry


def test_process_requests_no_errors():
    # no errors so request and its future should be completed
    future = futures.Future()
    ack_reqs_dict = {
        "ackid1": requests.AckRequest(
            ack_id="ackid1", byte_size=0, time_to_ack=20, ordering_key="", future=future
        )
    }
    errors_dict = {}
    requests_completed, requests_to_retry = streaming_pull_manager._process_requests(
        None, ack_reqs_dict, errors_dict
    )
    assert requests_completed[0].ack_id == "ackid1"
    assert future.result() == subscriber_exceptions.AcknowledgeStatus.SUCCESS
    assert not requests_to_retry


def test_process_requests_no_errors_no_future():
    # no errors, request should be completed, even when future is None.
    ack_reqs_dict = {
        "ackid1": requests.AckRequest(
            ack_id="ackid1", byte_size=0, time_to_ack=20, ordering_key="", future=None
        )
    }
    errors_dict = {}
    requests_completed, requests_to_retry = streaming_pull_manager._process_requests(
        None, ack_reqs_dict, errors_dict
    )
    assert requests_completed[0].ack_id == "ackid1"
    assert not requests_to_retry


def test_process_requests_permanent_error_raises_exception():
    # a permanent error raises an exception
    future = futures.Future()
    ack_reqs_dict = {
        "ackid1": requests.AckRequest(
            ack_id="ackid1", byte_size=0, time_to_ack=20, ordering_key="", future=future
        )
    }
    errors_dict = {"ackid1": "PERMANENT_FAILURE_INVALID_ACK_ID"}
    requests_completed, requests_to_retry = streaming_pull_manager._process_requests(
        None, ack_reqs_dict, errors_dict
    )
    assert requests_completed[0].ack_id == "ackid1"
    with pytest.raises(subscriber_exceptions.AcknowledgeError) as exc_info:
        future.result()
    assert (
        exc_info.value.error_code
        == subscriber_exceptions.AcknowledgeStatus.INVALID_ACK_ID
    )
    assert not requests_to_retry


def test_process_requests_permanent_error_other_raises_exception():
    # a permanent error of other raises an exception
    future = futures.Future()
    ack_reqs_dict = {
        "ackid1": requests.AckRequest(
            ack_id="ackid1", byte_size=0, time_to_ack=20, ordering_key="", future=future
        )
    }
    errors_dict = {"ackid1": "PERMANENT_FAILURE_OTHER"}
    requests_completed, requests_to_retry = streaming_pull_manager._process_requests(
        None, ack_reqs_dict, errors_dict
    )
    assert requests_completed[0].ack_id == "ackid1"
    with pytest.raises(subscriber_exceptions.AcknowledgeError) as exc_info:
        future.result()
    assert exc_info.value.error_code == subscriber_exceptions.AcknowledgeStatus.OTHER
    assert not requests_to_retry


def test_process_requests_permanent_error_other_raises_exception_no_future():
    # with a permanent error, request is completed even when future is None.
    ack_reqs_dict = {
        "ackid1": requests.AckRequest(
            ack_id="ackid1", byte_size=0, time_to_ack=20, ordering_key="", future=None
        )
    }
    errors_dict = {"ackid1": "PERMANENT_FAILURE_OTHER"}
    requests_completed, requests_to_retry = streaming_pull_manager._process_requests(
        None, ack_reqs_dict, errors_dict
    )
    assert requests_completed[0].ack_id == "ackid1"
    assert not requests_to_retry


def test_process_requests_transient_error_returns_request_for_retrying():
    # a transient error returns the request in `requests_to_retry`
    future = futures.Future()
    ack_reqs_dict = {
        "ackid1": requests.AckRequest(
            ack_id="ackid1", byte_size=0, time_to_ack=20, ordering_key="", future=future
        )
    }
    errors_dict = {"ackid1": "TRANSIENT_FAILURE_INVALID_ACK_ID"}
    requests_completed, requests_to_retry = streaming_pull_manager._process_requests(
        None, ack_reqs_dict, errors_dict
    )
    assert not requests_completed
    assert requests_to_retry[0].ack_id == "ackid1"
    assert not future.done()


def test_process_requests_unknown_error_raises_exception():
    # an unknown error raises an exception
    future = futures.Future()
    ack_reqs_dict = {
        "ackid1": requests.AckRequest(
            ack_id="ackid1", byte_size=0, time_to_ack=20, ordering_key="", future=future
        )
    }
    errors_dict = {"ackid1": "unknown_error"}
    requests_completed, requests_to_retry = streaming_pull_manager._process_requests(
        None, ack_reqs_dict, errors_dict
    )
    assert requests_completed[0].ack_id == "ackid1"
    with pytest.raises(subscriber_exceptions.AcknowledgeError) as exc_info:
        future.result()
    assert exc_info.value.error_code == subscriber_exceptions.AcknowledgeStatus.OTHER
    assert exc_info.value.info == "unknown_error"
    assert not requests_to_retry


def test_process_requests_retriable_error_status_returns_request_for_retrying():
    # a retriable error status returns the request in `requests_to_retry`
    retriable_errors = [
        code_pb2.DEADLINE_EXCEEDED,
        code_pb2.RESOURCE_EXHAUSTED,
        code_pb2.ABORTED,
        code_pb2.INTERNAL,
        code_pb2.UNAVAILABLE,
    ]

    for retriable_error in retriable_errors:
        future = futures.Future()
        ack_reqs_dict = {
            "ackid1": requests.AckRequest(
                ack_id="ackid1",
                byte_size=0,
                time_to_ack=20,
                ordering_key="",
                future=future,
            )
        }
        st = status_pb2.Status()
        st.code = retriable_error
        (
            requests_completed,
            requests_to_retry,
        ) = streaming_pull_manager._process_requests(st, ack_reqs_dict, None)
        assert not requests_completed
        assert requests_to_retry[0].ack_id == "ackid1"
        assert not future.done()


def test_process_requests_permission_denied_error_status_raises_exception():
    # a permission-denied error status raises an exception
    future = futures.Future()
    ack_reqs_dict = {
        "ackid1": requests.AckRequest(
            ack_id="ackid1", byte_size=0, time_to_ack=20, ordering_key="", future=future
        )
    }
    st = status_pb2.Status()
    st.code = code_pb2.Code.PERMISSION_DENIED
    requests_completed, requests_to_retry = streaming_pull_manager._process_requests(
        st, ack_reqs_dict, None
    )
    assert requests_completed[0].ack_id == "ackid1"
    with pytest.raises(subscriber_exceptions.AcknowledgeError) as exc_info:
        future.result()
    assert (
        exc_info.value.error_code
        == subscriber_exceptions.AcknowledgeStatus.PERMISSION_DENIED
    )
    assert exc_info.value.info is None
    assert not requests_to_retry


def test_process_requests_failed_precondition_error_status_raises_exception():
    # a failed-precondition error status raises an exception
    future = futures.Future()
    ack_reqs_dict = {
        "ackid1": requests.AckRequest(
            ack_id="ackid1", byte_size=0, time_to_ack=20, ordering_key="", future=future
        )
    }
    st = status_pb2.Status()
    st.code = code_pb2.Code.FAILED_PRECONDITION
    requests_completed, requests_to_retry = streaming_pull_manager._process_requests(
        st, ack_reqs_dict, None
    )
    assert requests_completed[0].ack_id == "ackid1"
    with pytest.raises(subscriber_exceptions.AcknowledgeError) as exc_info:
        future.result()
    assert (
        exc_info.value.error_code
        == subscriber_exceptions.AcknowledgeStatus.FAILED_PRECONDITION
    )
    assert exc_info.value.info is None
    assert not requests_to_retry


def test_process_requests_other_error_status_raises_exception():
    # an unrecognized error status raises an exception
    future = futures.Future()
    ack_reqs_dict = {
        "ackid1": requests.AckRequest(
            ack_id="ackid1", byte_size=0, time_to_ack=20, ordering_key="", future=future
        )
    }
    st = status_pb2.Status()
    st.code = code_pb2.Code.OUT_OF_RANGE
    requests_completed, requests_to_retry = streaming_pull_manager._process_requests(
        st, ack_reqs_dict, None
    )
    assert requests_completed[0].ack_id == "ackid1"
    with pytest.raises(subscriber_exceptions.AcknowledgeError) as exc_info:
        future.result()
    assert exc_info.value.error_code == subscriber_exceptions.AcknowledgeStatus.OTHER
    assert not requests_to_retry


def test_process_requests_other_error_status_raises_exception_no_future():
    # with an unrecognized error status, requests are completed, even when
    # future is None.
    ack_reqs_dict = {
        "ackid1": requests.AckRequest(
            ack_id="ackid1", byte_size=0, time_to_ack=20, ordering_key="", future=None
        )
    }
    st = status_pb2.Status()
    st.code = code_pb2.Code.OUT_OF_RANGE
    requests_completed, requests_to_retry = streaming_pull_manager._process_requests(
        st, ack_reqs_dict, None
    )
    assert requests_completed[0].ack_id == "ackid1"
    assert not requests_to_retry


def test_process_requests_mixed_success_and_failure_acks():
    # mixed success and failure (acks)
    future1 = futures.Future()
    future2 = futures.Future()
    future3 = futures.Future()
    ack_reqs_dict = {
        "ackid1": requests.AckRequest(
            ack_id="ackid1",
            byte_size=0,
            time_to_ack=20,
            ordering_key="",
            future=future1,
        ),
        "ackid2": requests.AckRequest(
            ack_id="ackid2",
            byte_size=0,
            time_to_ack=20,
            ordering_key="",
            future=future2,
        ),
        "ackid3": requests.AckRequest(
            ack_id="ackid3",
            byte_size=0,
            time_to_ack=20,
            ordering_key="",
            future=future3,
        ),
    }
    errors_dict = {
        "ackid1": "PERMANENT_FAILURE_INVALID_ACK_ID",
        "ackid2": "TRANSIENT_FAILURE_INVALID_ACK_ID",
    }
    requests_completed, requests_to_retry = streaming_pull_manager._process_requests(
        None, ack_reqs_dict, errors_dict
    )
    # message with ack_id 'ackid1' fails with an exception
    assert requests_completed[0].ack_id == "ackid1"
    with pytest.raises(subscriber_exceptions.AcknowledgeError) as exc_info:
        future1.result()
    assert (
        exc_info.value.error_code
        == subscriber_exceptions.AcknowledgeStatus.INVALID_ACK_ID
    )
    # message with ack_id 'ackid2' is to be retried
    assert requests_to_retry[0].ack_id == "ackid2"
    assert not requests_to_retry[0].future.done()
    # message with ack_id 'ackid3' succeeds
    assert requests_completed[1].ack_id == "ackid3"
    assert future3.result() == subscriber_exceptions.AcknowledgeStatus.SUCCESS


def test_process_requests_mixed_success_and_failure_modacks():
    # mixed success and failure (modacks)
    future1 = futures.Future()
    future2 = futures.Future()
    future3 = futures.Future()
    ack_reqs_dict = {
        "ackid1": requests.ModAckRequest(ack_id="ackid1", seconds=60, future=future1),
        "ackid2": requests.ModAckRequest(ack_id="ackid2", seconds=60, future=future2),
        "ackid3": requests.ModAckRequest(ack_id="ackid3", seconds=60, future=future3),
    }
    errors_dict = {
        "ackid1": "PERMANENT_FAILURE_INVALID_ACK_ID",
        "ackid2": "TRANSIENT_FAILURE_INVALID_ACK_ID",
    }
    requests_completed, requests_to_retry = streaming_pull_manager._process_requests(
        None, ack_reqs_dict, errors_dict
    )
    # message with ack_id 'ackid1' fails with an exception
    assert requests_completed[0].ack_id == "ackid1"
    with pytest.raises(subscriber_exceptions.AcknowledgeError) as exc_info:
        future1.result()
    assert (
        exc_info.value.error_code
        == subscriber_exceptions.AcknowledgeStatus.INVALID_ACK_ID
    )
    # message with ack_id 'ackid2' is to be retried
    assert requests_to_retry[0].ack_id == "ackid2"
    assert not requests_to_retry[0].future.done()
    # message with ack_id 'ackid3' succeeds
    assert requests_completed[1].ack_id == "ackid3"
    assert future3.result() == subscriber_exceptions.AcknowledgeStatus.SUCCESS


def test_opentelemetry__on_response_subscribe_span_create(span_exporter):
    manager, _, _, leaser, _, _ = make_running_manager(
        enable_open_telemetry=True,
        subscription_name="projects/projectID/subscriptions/subscriptionID",
    )

    fake_leaser_add(leaser, init_msg_count=0, assumed_msg_size=42)
    manager._callback = mock.sentinel.callback

    response = gapic_types.StreamingPullResponse(
        received_messages=[
            gapic_types.ReceivedMessage(
                ack_id="ack1",
                message=gapic_types.PubsubMessage(data=b"foo", message_id="1"),
            ),
            gapic_types.ReceivedMessage(
                ack_id="ack2",
                message=gapic_types.PubsubMessage(data=b"bar", message_id="2"),
                delivery_attempt=6,
            ),
        ]
    )

    manager._on_response(response)

    spans = span_exporter.get_finished_spans()

    # Subscribe span is still active, hence unexported.
    # Subscriber scheduler spans corresponding to the two messages would be started in `messages_on_hold.put()``
    # and ended in `_maybe_release_messages`
    assert len(spans) == 3
    modack_span = spans[0]

    for span in spans[1:]:
        assert span.name == "subscriber scheduler"
        assert span.kind == trace.SpanKind.INTERNAL
        assert span.parent is not None
        assert len(span.attributes) == 0

    assert modack_span.name == "subscriptionID modack"
    assert modack_span.kind == trace.SpanKind.CLIENT
    assert modack_span.parent is None
    assert len(modack_span.links) == 2


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


def test_opentelemetry_subscriber_concurrency_control_span(span_exporter):
    manager, _, _, leaser, _, _ = make_running_manager(
        enable_open_telemetry=True,
        subscription_name="projects/projectID/subscriptions/subscriptionID",
    )
    manager._callback = mock.Mock()
    msg = create_message(b"foo")
    opentelemetry_data = SubscribeOpenTelemetry(msg)
    opentelemetry_data.start_subscribe_span(
        subscription="projects/projectId/subscriptions/subscriptionID",
        exactly_once_enabled=False,
        ack_id="ack_id",
        delivery_attempt=4,
    )
    msg.opentelemetry_data = opentelemetry_data
    manager._schedule_message_on_hold(msg)
    opentelemetry_data.end_subscribe_concurrency_control_span()
    opentelemetry_data.end_subscribe_span()

    spans = span_exporter.get_finished_spans()
    assert len(spans) == 2

    concurrency_control_span, subscribe_span = spans
    assert concurrency_control_span.name == "subscriber concurrency control"
    assert subscribe_span.name == "subscriptionID subscribe"
    assert opentelemetry_data.subscription_id == "subscriptionID"

    assert concurrency_control_span.parent == subscribe_span.context


def test_opentelemetry_subscriber_concurrency_control_span_end(span_exporter):
    msg = create_message(b"foo")
    opentelemetry_data = SubscribeOpenTelemetry(msg)
    opentelemetry_data.start_subscribe_span(
        subscription="projects/projectId/subscriptions/subscriptionID",
        exactly_once_enabled=False,
        ack_id="ack_id",
        delivery_attempt=4,
    )
    opentelemetry_data.start_subscribe_concurrency_control_span()
    msg.opentelemetry_data = opentelemetry_data
    streaming_pull_manager._wrap_callback_errors(mock.Mock(), mock.Mock(), msg)

    spans = span_exporter.get_finished_spans()
    assert len(spans) == 2

    concurrency_control_span = spans[0]
    assert concurrency_control_span.name == "subscriber concurrency control"


def test_opentelemetry_wrap_callback_error(span_exporter):
    msg = create_message(b"foo")
    streaming_pull_manager._wrap_callback_errors(mock.Mock(), mock.Mock(), msg)

    spans = span_exporter.get_finished_spans()
    assert len(spans) == 0
