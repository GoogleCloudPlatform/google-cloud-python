# Copyright 2020, Google LLC All rights reserved.
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

from __future__ import absolute_import

import threading
import time
from typing import Callable, Sequence, Union

import pytest

import google
from google.cloud.pubsub_v1 import types
from google.cloud.pubsub_v1.publisher import exceptions
from google.cloud.pubsub_v1.publisher.flow_controller import FlowController
from google.pubsub_v1 import types as grpc_types


def _run_in_daemon(
    action: Callable[["google.cloud.pubsub_v1.types.PubsubMessage"], None],
    messages: Sequence["google.cloud.pubsub_v1.types.PubsubMessage"],
    all_done_event: threading.Event,
    error_event: threading.Event = None,
    action_pause: Union[int, float] = None,
):
    """Run flow controller action (add or remove messages) in a daemon thread."""

    def run_me():
        try:
            for msg in messages:
                if action_pause is not None:
                    time.sleep(action_pause)
                action(msg)
        except Exception:
            if error_event is not None:  # pragma: NO COVER
                error_event.set()
        else:
            all_done_event.set()

    thread = threading.Thread(target=run_me)
    thread.daemon = True
    thread.start()


def test_no_overflow_no_error():
    settings = types.PublishFlowControl(
        message_limit=100,
        byte_limit=10000,
        limit_exceeded_behavior=types.LimitExceededBehavior.ERROR,
    )
    flow_controller = FlowController(settings)

    # there should be no errors
    for data in (b"foo", b"bar", b"baz"):
        msg = grpc_types.PubsubMessage(data=data)
        flow_controller.add(msg)


def test_overflow_no_error_on_ignore():
    settings = types.PublishFlowControl(
        message_limit=1,
        byte_limit=2,
        limit_exceeded_behavior=types.LimitExceededBehavior.IGNORE,
    )
    flow_controller = FlowController(settings)

    # there should be no overflow errors
    flow_controller.add(grpc_types.PubsubMessage(data=b"foo"))
    flow_controller.add(grpc_types.PubsubMessage(data=b"bar"))


def test_message_count_overflow_error():
    settings = types.PublishFlowControl(
        message_limit=1,
        byte_limit=10000,
        limit_exceeded_behavior=types.LimitExceededBehavior.ERROR,
    )
    flow_controller = FlowController(settings)

    flow_controller.add(grpc_types.PubsubMessage(data=b"foo"))
    with pytest.raises(exceptions.FlowControlLimitError) as error:
        flow_controller.add(grpc_types.PubsubMessage(data=b"bar"))

    assert "messages: 2 / 1" in str(error.value)


def test_byte_size_overflow_error():
    settings = types.PublishFlowControl(
        message_limit=10000,
        byte_limit=199,
        limit_exceeded_behavior=types.LimitExceededBehavior.ERROR,
    )
    flow_controller = FlowController(settings)

    # Since the message data itself occupies 100 bytes, it means that both
    # messages combined will exceed the imposed byte limit of 199, but a single
    # message will not (the message size overhead is way lower than data size).
    msg1 = grpc_types.PubsubMessage(data=b"x" * 100)
    msg2 = grpc_types.PubsubMessage(data=b"y" * 100)

    flow_controller.add(msg1)
    with pytest.raises(exceptions.FlowControlLimitError) as error:
        flow_controller.add(msg2)

    total_size = msg1._pb.ByteSize() + msg2._pb.ByteSize()
    expected_info = "bytes: {} / 199".format(total_size)
    assert expected_info in str(error.value)


def test_no_error_on_moderate_message_flow():
    settings = types.PublishFlowControl(
        message_limit=2,
        byte_limit=250,
        limit_exceeded_behavior=types.LimitExceededBehavior.ERROR,
    )
    flow_controller = FlowController(settings)

    msg1 = grpc_types.PubsubMessage(data=b"x" * 100)
    msg2 = grpc_types.PubsubMessage(data=b"y" * 100)
    msg3 = grpc_types.PubsubMessage(data=b"z" * 100)

    # The flow control settings will accept two in-flight messages, but not three.
    # If releasing messages works correctly, the sequence below will not raise errors.
    flow_controller.add(msg1)
    flow_controller.add(msg2)
    flow_controller.release(msg1)
    flow_controller.add(msg3)
    flow_controller.release(msg2)
    flow_controller.release(msg3)


def test_rejected_messages_do_not_increase_total_load():
    settings = types.PublishFlowControl(
        message_limit=1,
        byte_limit=150,
        limit_exceeded_behavior=types.LimitExceededBehavior.ERROR,
    )
    flow_controller = FlowController(settings)

    msg1 = grpc_types.PubsubMessage(data=b"x" * 100)
    msg2 = grpc_types.PubsubMessage(data=b"y" * 100)

    flow_controller.add(msg1)

    for _ in range(5):
        with pytest.raises(exceptions.FlowControlLimitError):
            flow_controller.add(grpc_types.PubsubMessage(data=b"z" * 100))

    # After releasing a message we should again be able to add another one, despite
    # previously trying to add a lot of other messages.
    flow_controller.release(msg1)
    flow_controller.add(msg2)


def test_incorrectly_releasing_too_many_messages():
    settings = types.PublishFlowControl(
        message_limit=1,
        byte_limit=150,
        limit_exceeded_behavior=types.LimitExceededBehavior.ERROR,
    )
    flow_controller = FlowController(settings)

    msg1 = grpc_types.PubsubMessage(data=b"x" * 100)
    msg2 = grpc_types.PubsubMessage(data=b"y" * 100)
    msg3 = grpc_types.PubsubMessage(data=b"z" * 100)

    # Releasing a message that would make the load negative should result in a warning.
    with pytest.warns(
        RuntimeWarning,
        match="Releasing a message that was never added or already released",
    ) as warned:
        flow_controller.release(msg1)

    assert len(warned) == 1
    assert issubclass(warned[0].category, RuntimeWarning)
    warning_msg = str(warned[0].message)
    assert "never added or already released" in warning_msg

    # Incorrectly removing a message does not mess up internal stats, we can
    # still only add a single message at a time to this flow.
    flow_controller.add(msg2)

    with pytest.raises(exceptions.FlowControlLimitError) as error:
        flow_controller.add(msg3)

    error_msg = str(error.value)
    assert "messages: 2 / 1" in error_msg
    total_size = msg2._pb.ByteSize() + msg3._pb.ByteSize()
    expected_size_info = "bytes: {} / 150".format(total_size)
    assert expected_size_info in error_msg


def test_blocking_on_overflow_until_free_capacity():
    settings = types.PublishFlowControl(
        message_limit=1,
        byte_limit=150,
        limit_exceeded_behavior=types.LimitExceededBehavior.BLOCK,
    )
    flow_controller = FlowController(settings)

    msg1 = grpc_types.PubsubMessage(data=b"x" * 100)
    msg2 = grpc_types.PubsubMessage(data=b"y" * 100)
    msg3 = grpc_types.PubsubMessage(data=b"z" * 100)
    msg4 = grpc_types.PubsubMessage(data=b"w" * 100)

    # If there is a concurrency bug in FlowController, we do not want to block
    # the main thread running the tests, thus we delegate all add/release
    # operations to daemon threads and check the outcome (blocked/not blocked)
    # through Events.
    adding_1_done = threading.Event()
    adding_2_done = threading.Event()
    adding_3_done = threading.Event()
    adding_4_done = threading.Event()
    releasing_1_done = threading.Event()
    releasing_x_done = threading.Event()

    # Adding a message with free capacity should not block.
    _run_in_daemon(flow_controller.add, [msg1], adding_1_done)
    if not adding_1_done.wait(timeout=0.1):
        pytest.fail(  # pragma: NO COVER
            "Adding a message with enough flow capacity blocked or errored."
        )

    # Adding messages when there is not enough capacity should block, even if
    # added through multiple threads.
    _run_in_daemon(flow_controller.add, [msg2], adding_2_done)
    if adding_2_done.wait(timeout=0.1):
        pytest.fail("Adding a message on overflow did not block.")  # pragma: NO COVER

    _run_in_daemon(flow_controller.add, [msg3], adding_3_done)
    if adding_3_done.wait(timeout=0.1):
        pytest.fail("Adding a message on overflow did not block.")  # pragma: NO COVER

    _run_in_daemon(flow_controller.add, [msg4], adding_4_done)
    if adding_4_done.wait(timeout=0.1):
        pytest.fail("Adding a message on overflow did not block.")  # pragma: NO COVER

    # After releasing one message, there should be room for a new message, which
    # should result in unblocking one of the waiting threads.
    _run_in_daemon(flow_controller.release, [msg1], releasing_1_done)
    if not releasing_1_done.wait(timeout=0.1):
        pytest.fail("Releasing a message blocked or errored.")  # pragma: NO COVER

    done_status = [
        adding_2_done.wait(timeout=0.1),
        adding_3_done.wait(timeout=0.1),
        adding_4_done.wait(timeout=0.1),
    ]

    # In sum() we use the fact that True==1 and False==0, and that Event.wait()
    # returns False only if it times out, i.e. its internal flag has not been set.
    done_count = sum(done_status)
    assert done_count == 1, "Exactly one thread should have been unblocked."

    # Release another message and verify that yet another thread gets unblocked.
    added_msg = [msg2, msg3, msg4][done_status.index(True)]
    _run_in_daemon(flow_controller.release, [added_msg], releasing_x_done)

    if not releasing_x_done.wait(timeout=0.1):
        pytest.fail("Releasing messages blocked or errored.")  # pragma: NO COVER

    released_count = sum(
        (
            adding_2_done.wait(timeout=0.1),
            adding_3_done.wait(timeout=0.1),
            adding_4_done.wait(timeout=0.1),
        )
    )
    assert released_count == 2, "Exactly two threads should have been unblocked."


def test_error_if_mesage_would_block_indefinitely():
    settings = types.PublishFlowControl(
        message_limit=0,  # simulate non-sane settings
        byte_limit=1,
        limit_exceeded_behavior=types.LimitExceededBehavior.BLOCK,
    )
    flow_controller = FlowController(settings)

    msg = grpc_types.PubsubMessage(data=b"xyz")
    adding_done = threading.Event()
    error_event = threading.Event()

    _run_in_daemon(flow_controller.add, [msg], adding_done, error_event=error_event)

    assert error_event.wait(timeout=0.1), "No error on adding too large a message."

    # Now that we know that an error occurs, we can check its type directly
    # without the fear of blocking indefinitely.
    flow_controller = FlowController(settings)  # we want a fresh controller
    with pytest.raises(exceptions.FlowControlLimitError) as error_info:
        flow_controller.add(msg)

    error_msg = str(error_info.value)
    assert "would block forever" in error_msg
    assert "messages: 1 / 0" in error_msg
    assert "bytes: {} / 1".format(msg._pb.ByteSize()) in error_msg


def test_threads_posting_large_messages_do_not_starve():
    settings = types.PublishFlowControl(
        message_limit=100,
        byte_limit=110,
        limit_exceeded_behavior=types.LimitExceededBehavior.BLOCK,
    )
    flow_controller = FlowController(settings)

    large_msg = grpc_types.PubsubMessage(data=b"x" * 100)  # close to entire byte limit

    adding_initial_done = threading.Event()
    adding_large_done = threading.Event()
    adding_busy_done = threading.Event()
    releasing_busy_done = threading.Event()
    releasing_large_done = threading.Event()

    # Occupy some of the flow capacity, then try to add a large message. Releasing
    # enough messages should eventually allow the large message to come through, even
    # if more messages are added after it (those should wait for the large message).
    initial_messages = [grpc_types.PubsubMessage(data=b"x" * 10)] * 5
    _run_in_daemon(flow_controller.add, initial_messages, adding_initial_done)
    assert adding_initial_done.wait(timeout=0.1)

    _run_in_daemon(flow_controller.add, [large_msg], adding_large_done)

    # Continuously keep adding more messages after the large one.
    messages = [grpc_types.PubsubMessage(data=b"x" * 10)] * 10
    _run_in_daemon(flow_controller.add, messages, adding_busy_done, action_pause=0.1)

    # At the same time, gradually keep releasing the messages - the freeed up
    # capacity should be consumed by the large message, not the other small messages
    # being added after it.
    _run_in_daemon(
        flow_controller.release, messages, releasing_busy_done, action_pause=0.1
    )

    # Sanity check - releasing should have completed by now.
    if not releasing_busy_done.wait(timeout=1.1):
        pytest.fail("Releasing messages blocked or errored.")  # pragma: NO COVER

    # Enough messages released, the large message should have come through in
    # the meantime.
    if not adding_large_done.wait(timeout=0.1):
        pytest.fail("A thread adding a large message starved.")  # pragma: NO COVER

    if adding_busy_done.wait(timeout=0.1):
        pytest.fail("Adding multiple small messages did not block.")  # pragma: NO COVER

    # Releasing the large message should unblock adding the remaining "busy" messages
    # that have not been added yet.
    _run_in_daemon(flow_controller.release, [large_msg], releasing_large_done)
    if not releasing_large_done.wait(timeout=0.1):
        pytest.fail("Releasing a message blocked or errored.")  # pragma: NO COVER

    if not adding_busy_done.wait(timeout=1.0):
        pytest.fail("Adding messages blocked or errored.")  # pragma: NO COVER


def test_blocked_messages_are_accepted_in_fifo_order():
    settings = types.PublishFlowControl(
        message_limit=1,
        byte_limit=1_000_000,  # Unlimited for practical purposes in the test.
        limit_exceeded_behavior=types.LimitExceededBehavior.BLOCK,
    )
    flow_controller = FlowController(settings)

    # It's OK if the message instance is shared, as flow controlelr is only concerned
    # with byte sizes and counts, and not with particular message instances.
    message = grpc_types.PubsubMessage(data=b"x")

    adding_done_events = [threading.Event() for _ in range(10)]
    releasing_done_events = [threading.Event() for _ in adding_done_events]

    # Add messages. The first one will be accepted, and the rest should queue behind.
    for adding_done in adding_done_events:
        _run_in_daemon(flow_controller.add, [message], adding_done)
        time.sleep(0.1)

    if not adding_done_events[0].wait(timeout=0.1):  # pragma: NO COVER
        pytest.fail("The first message unexpectedly got blocked on adding.")

    # For each message, check that it has indeed been added to the flow controller.
    # Then release it to make room for the next message in line, and repeat the check.
    enumeration = enumerate(zip(adding_done_events, releasing_done_events))
    for i, (adding_done, releasing_done) in enumeration:
        if not adding_done.wait(timeout=0.1):  # pragma: NO COVER
            pytest.fail(f"Queued message still blocked on adding (i={i}).")

        _run_in_daemon(flow_controller.release, [message], releasing_done)
        if not releasing_done.wait(timeout=0.1):  # pragma: NO COVER
            pytest.fail(f"Queued message was not released in time (i={i}).")


def test_warning_on_internal_reservation_stats_error_when_unblocking():
    settings = types.PublishFlowControl(
        message_limit=1,
        byte_limit=150,
        limit_exceeded_behavior=types.LimitExceededBehavior.BLOCK,
    )
    flow_controller = FlowController(settings)

    msg1 = grpc_types.PubsubMessage(data=b"x" * 100)
    msg2 = grpc_types.PubsubMessage(data=b"y" * 100)

    # If there is a concurrency bug in FlowController, we do not want to block
    # the main thread running the tests, thus we delegate all add/release
    # operations to daemon threads and check the outcome (blocked/not blocked)
    # through Events.
    adding_1_done = threading.Event()
    adding_2_done = threading.Event()
    releasing_1_done = threading.Event()

    # Adding a message with free capacity should not block.
    _run_in_daemon(flow_controller.add, [msg1], adding_1_done)
    if not adding_1_done.wait(timeout=0.1):
        pytest.fail(  # pragma: NO COVER
            "Adding a message with enough flow capacity blocked or errored."
        )

    # Adding messages when there is not enough capacity should block, even if
    # added through multiple threads.
    _run_in_daemon(flow_controller.add, [msg2], adding_2_done)
    if adding_2_done.wait(timeout=0.1):
        pytest.fail("Adding a message on overflow did not block.")  # pragma: NO COVER

    # Intentionally corrupt internal stats
    reservation = next(iter(flow_controller._waiting.values()), None)
    assert reservation is not None, "No messages blocked by flow controller."
    reservation.bytes_reserved = reservation.bytes_needed + 1

    with pytest.warns(RuntimeWarning, match="Too many bytes reserved.") as warned:
        _run_in_daemon(flow_controller.release, [msg1], releasing_1_done)
        if not releasing_1_done.wait(timeout=0.1):
            pytest.fail("Releasing a message blocked or errored.")  # pragma: NO COVER

    matches = [warning for warning in warned if warning.category is RuntimeWarning]
    assert len(matches) == 1
    assert "too many bytes reserved" in str(matches[0].message).lower()
