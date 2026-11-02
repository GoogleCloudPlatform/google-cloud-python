# Copyright 2020, Google LLC
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

import queue

from opentelemetry import trace

from google.cloud.pubsub_v1.open_telemetry.subscribe_opentelemetry import (
    SubscribeOpenTelemetry,
)
from google.cloud.pubsub_v1.subscriber import message
from google.cloud.pubsub_v1.subscriber._protocol import messages_on_hold
from google.pubsub_v1 import types as gapic_types


def make_message(ack_id, ordering_key):
    proto_msg = gapic_types.PubsubMessage(data=b"Q", ordering_key=ordering_key)
    return message.Message(
        proto_msg._pb,
        ack_id,
        0,
        queue.Queue(),
        exactly_once_delivery_enabled_func=lambda: False,  # pragma: NO COVER
    )


def test_init():
    moh = messages_on_hold.MessagesOnHold()

    assert moh.size == 0
    assert moh.get() is None


def test_opentelemetry_subscriber_scheduler_span(span_exporter):
    moh = messages_on_hold.MessagesOnHold()
    msg = make_message(ack_id="ack1", ordering_key="")
    opentelemetry_data = SubscribeOpenTelemetry(msg)
    msg.opentelemetry_data = opentelemetry_data
    opentelemetry_data.start_subscribe_span(
        subscription="projects/projectId/subscriptions/subscriptionID",
        exactly_once_enabled=False,
        ack_id="ack_id",
        delivery_attempt=4,
    )
    moh.put(msg)
    opentelemetry_data.end_subscribe_scheduler_span()
    opentelemetry_data.end_subscribe_span()

    spans = span_exporter.get_finished_spans()

    assert len(spans) == 2

    subscribe_scheduler_span, subscribe_span = spans

    assert subscribe_scheduler_span.name == "subscriber scheduler"
    assert subscribe_scheduler_span.kind == trace.SpanKind.INTERNAL
    assert subscribe_scheduler_span.parent == subscribe_span.context


def test_put_and_get_unordered_messages():
    moh = messages_on_hold.MessagesOnHold()

    msg1 = make_message(ack_id="ack1", ordering_key="")
    moh.put(msg1)
    assert moh.size == 1

    msg2 = make_message(ack_id="ack2", ordering_key="")
    moh.put(msg2)
    assert moh.size == 2

    assert moh.get() == msg1
    assert moh.size == 1
    assert moh.get() == msg2
    assert moh.size == 0
    assert moh.get() is None


class ScheduleMessageCallbackTracker(object):
    def __init__(self):
        self.called = False
        self.message = ""

    def __call__(self, message):
        self.called = True
        self.message = message


def test_ordered_messages_one_key():
    moh = messages_on_hold.MessagesOnHold()

    msg1 = make_message(ack_id="ack1", ordering_key="key1")
    moh.put(msg1)
    assert moh.size == 1

    msg2 = make_message(ack_id="ack2", ordering_key="key1")
    moh.put(msg2)
    assert moh.size == 2

    # Get first message for "key1"
    assert moh.get() == msg1
    assert moh.size == 1

    # Still waiting on the previously-sent message for "key1", and there are no
    # other messages, so return None.
    assert moh.get() is None
    assert moh.size == 1

    # Activate "key1" to release the second message with that key.
    callback_tracker = ScheduleMessageCallbackTracker()
    moh.activate_ordering_keys(["key1"], callback_tracker)
    assert callback_tracker.called
    assert callback_tracker.message == msg2
    assert moh.size == 0
    assert len(moh._pending_ordered_messages) == 1

    # Activate "key1" again. There are no other messages for that key, so clean
    # up state for that key.
    callback_tracker = ScheduleMessageCallbackTracker()
    moh.activate_ordering_keys(["key1"], callback_tracker)
    assert not callback_tracker.called

    # Check that clean-up happened.
    assert moh.size == 0
    assert len(moh._messages_on_hold) == 0
    assert len(moh._pending_ordered_messages) == 0

    # No messages left.
    assert moh.get() is None
    assert moh.size == 0


def test_ordered_messages_drop_duplicate_keys(caplog, modify_google_logger_propagation):
    moh = messages_on_hold.MessagesOnHold()

    msg1 = make_message(ack_id="ack1", ordering_key="key1")
    moh.put(msg1)
    assert moh.size == 1

    msg2 = make_message(ack_id="ack2", ordering_key="key1")
    moh.put(msg2)
    assert moh.size == 2

    # Get first message for "key1"
    assert moh.get() == msg1
    assert moh.size == 1

    # Still waiting on the previously-sent message for "key1", and there are no
    # other messages, so return None.
    assert moh.get() is None
    assert moh.size == 1

    # Activate "key1".
    callback_tracker = ScheduleMessageCallbackTracker()
    moh.activate_ordering_keys(["key1", "key1"], callback_tracker)
    assert callback_tracker.called
    assert callback_tracker.message == msg2
    assert moh.size == 0
    assert len(moh._pending_ordered_messages) == 0

    # Activate "key1" again
    callback_tracker = ScheduleMessageCallbackTracker()
    moh.activate_ordering_keys(["key1"], callback_tracker)
    assert not callback_tracker.called

    # Activate "key1" again. There are no other messages for that key, so clean
    # up state for that key.
    callback_tracker = ScheduleMessageCallbackTracker()
    moh.activate_ordering_keys(["key1"], callback_tracker)
    assert not callback_tracker.called

    msg3 = make_message(ack_id="ack3", ordering_key="key1")
    moh.put(msg3)
    assert moh.size == 1

    # Get next message for "key1"
    assert moh.get() == msg3
    assert moh.size == 0

    # Activate "key1".
    callback_tracker = ScheduleMessageCallbackTracker()
    moh.activate_ordering_keys(["key1"], callback_tracker)
    assert not callback_tracker.called

    # Activate "key1" again. There are no other messages for that key, so clean
    # up state for that key.
    callback_tracker = ScheduleMessageCallbackTracker()
    moh.activate_ordering_keys(["key1"], callback_tracker)
    assert not callback_tracker.called

    # Activate "key1" again after being cleaned up. There are no other messages for that key, so clean
    # up state for that key.
    callback_tracker = ScheduleMessageCallbackTracker()
    moh.activate_ordering_keys(["key1"], callback_tracker)
    assert not callback_tracker.called
    assert "No message queue exists for message ordering key: key1" in caplog.text


def test_ordered_messages_two_keys():
    moh = messages_on_hold.MessagesOnHold()

    # Put message with "key1".
    msg1 = make_message(ack_id="ack1", ordering_key="key1")
    moh.put(msg1)
    assert moh.size == 1

    # Put second message with "key1".
    msg2 = make_message(ack_id="ack2", ordering_key="key1")
    moh.put(msg2)
    assert moh.size == 2

    # Put message with another key: "key2".
    msg3 = make_message(ack_id="ack3", ordering_key="key2")
    moh.put(msg3)
    assert moh.size == 3

    # Get first message for "key1"
    assert moh.get() == msg1
    assert moh.size == 2

    # Get another message. Still waiting on the previously-sent message for
    # "key1", so release msg3 with key "key2".
    assert moh.get() is msg3
    assert moh.size == 1

    # Activate "key1" to release the second message with that key.
    callback_tracker = ScheduleMessageCallbackTracker()
    moh.activate_ordering_keys(["key1"], callback_tracker)
    assert callback_tracker.called
    assert callback_tracker.message == msg2
    assert moh.size == 0

    # Activate "key2" and release no messages because there are none left for
    # that key. State for "key2" should be cleaned up.
    callback_tracker = ScheduleMessageCallbackTracker()
    moh.activate_ordering_keys(["key2"], callback_tracker)
    assert not callback_tracker.called
    assert moh.size == 0

    # Activate "key1" again to mark msg2 as complete. Since there are no other
    # messages for that key, clean up state for both keys.
    callback_tracker = ScheduleMessageCallbackTracker()
    moh.activate_ordering_keys(["key1"], callback_tracker)
    assert not callback_tracker.called

    # Check that clean-up happened.
    assert moh.size == 0
    assert len(moh._messages_on_hold) == 0
    assert len(moh._pending_ordered_messages) == 0

    # No messages left.
    assert moh.get() is None
    assert moh.size == 0


def test_ordered_messages_two_keys_interleaved():
    moh = messages_on_hold.MessagesOnHold()

    # Put message with "key1".
    msg1 = make_message(ack_id="ack1", ordering_key="key1")
    moh.put(msg1)
    assert moh.size == 1

    # Put message with another key: "key2".
    msg2 = make_message(ack_id="ack2", ordering_key="key2")
    moh.put(msg2)
    assert moh.size == 2

    # Put second message with "key1".
    msg3 = make_message(ack_id="ack3", ordering_key="key1")
    moh.put(msg3)
    assert moh.size == 3

    # Get first message for "key1"
    assert moh.get() == msg1
    assert moh.size == 2

    # Get another message. msg2 with "key2" is next in line in the queue.
    assert moh.get() is msg2
    assert moh.size == 1

    # Activate "key1". Clean up state for "key1" because another message with
    # the same key (msg3) hasn't been sorted into _pending_ordered_messages yet
    # through a call to get().
    callback_tracker = ScheduleMessageCallbackTracker()
    moh.activate_ordering_keys(["key1"], callback_tracker)
    assert not callback_tracker.called
    assert moh.size == 1

    # Get another message. msg3 is next in line in the queue.
    assert moh.get() is msg3
    assert moh.size == 0

    # Activate "key2" to mark msg2 as complete. Release no messages because
    # there are none left for that key. State for "key2" should be cleaned up.
    callback_tracker = ScheduleMessageCallbackTracker()
    moh.activate_ordering_keys(["key2"], callback_tracker)
    assert not callback_tracker.called
    assert moh.size == 0

    # Activate "key1" to mark msg3 as complete. Release no messages because
    # there are none left for that key. State for "key1" should be cleaned up.
    callback_tracker = ScheduleMessageCallbackTracker()
    moh.activate_ordering_keys(["key1"], callback_tracker)
    assert not callback_tracker.called

    # Check that clean-up happened.
    assert moh.size == 0
    assert len(moh._messages_on_hold) == 0
    assert len(moh._pending_ordered_messages) == 0

    # No messages left.
    assert moh.get() is None
    assert moh.size == 0


def test_ordered_and_unordered_messages_interleaved():
    moh = messages_on_hold.MessagesOnHold()

    # Put message with "key1".
    msg1 = make_message(ack_id="ack1", ordering_key="key1")
    moh.put(msg1)
    assert moh.size == 1

    # Put another message "key1"
    msg2 = make_message(ack_id="ack2", ordering_key="key1")
    moh.put(msg2)
    assert moh.size == 2

    # Put a message with no ordering key.
    msg3 = make_message(ack_id="ack3", ordering_key="")
    moh.put(msg3)
    assert moh.size == 3

    # Get first message for "key1"
    assert moh.get() == msg1
    assert moh.size == 2

    # Get another message. msg2 will be skipped because another message with the
    # same key (msg1) is in flight.
    assert moh.get() is msg3
    assert moh.size == 1

    # Activate "key1". Send msg2, the next in line for the same ordering key.
    callback_tracker = ScheduleMessageCallbackTracker()
    moh.activate_ordering_keys(["key1"], callback_tracker)
    assert callback_tracker.called
    assert callback_tracker.message == msg2
    assert moh.size == 0

    # No more messages left.
    assert moh.get() is None

    # Activate "key1" to mark msg2 as complete. Release no messages because
    # there are none left for that key. State for "key1" should be cleaned up.
    callback_tracker = ScheduleMessageCallbackTracker()
    moh.activate_ordering_keys(["key1"], callback_tracker)
    assert not callback_tracker.called

    # Check that clean-up happened.
    assert moh.size == 0
    assert len(moh._messages_on_hold) == 0
    assert len(moh._pending_ordered_messages) == 0

    # No messages left.
    assert moh.get() is None
    assert moh.size == 0


def test_cleanup_nonexistent_key(caplog, modify_google_logger_propagation):
    moh = messages_on_hold.MessagesOnHold()
    moh._clean_up_ordering_key("non-existent-key")
    assert (
        "Tried to clean up ordering key that does not exist: non-existent-key"
        in caplog.text
    )


def test_cleanup_key_with_messages(caplog, modify_google_logger_propagation):
    moh = messages_on_hold.MessagesOnHold()

    # Put message with "key1".
    msg1 = make_message(ack_id="ack1", ordering_key="key1")
    moh.put(msg1)
    assert moh.size == 1

    # Put another message "key1"
    msg2 = make_message(ack_id="ack2", ordering_key="key1")
    moh.put(msg2)
    assert moh.size == 2

    # Get first message for "key1"
    assert moh.get() == msg1
    assert moh.size == 1

    # Get first message for "key1"
    assert moh.get() is None
    assert moh.size == 1

    moh._clean_up_ordering_key("key1")
    assert (
        "Tried to clean up ordering key: key1 with 1 messages remaining." in caplog.text
    )
