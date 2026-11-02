# Copyright 2017, Google LLC
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

import logging
import threading
from unittest import mock

import pytest

from google.cloud.pubsub_v1 import types
from google.cloud.pubsub_v1.open_telemetry.subscribe_opentelemetry import (
    SubscribeOpenTelemetry,
)
from google.cloud.pubsub_v1.subscriber import message
from google.cloud.pubsub_v1.subscriber._protocol import (
    dispatcher,
    histogram,
    leaser,
    requests,
    streaming_pull_manager,
)


def test_add_and_remove():
    leaser_ = leaser.Leaser(mock.sentinel.manager)

    leaser_.add([requests.LeaseRequest(ack_id="ack1", byte_size=50, ordering_key="")])
    leaser_.add([requests.LeaseRequest(ack_id="ack2", byte_size=25, ordering_key="")])

    assert leaser_.message_count == 2
    assert set(leaser_.ack_ids) == set(["ack1", "ack2"])
    assert leaser_.bytes == 75

    leaser_.remove([requests.DropRequest(ack_id="ack1", byte_size=50, ordering_key="")])

    assert leaser_.message_count == 1
    assert set(leaser_.ack_ids) == set(["ack2"])
    assert leaser_.bytes == 25


def test_add_already_managed(caplog, modify_google_logger_propagation):
    caplog.set_level(logging.DEBUG)

    leaser_ = leaser.Leaser(mock.sentinel.manager)

    leaser_.add([requests.LeaseRequest(ack_id="ack1", byte_size=50, ordering_key="")])
    leaser_.add([requests.LeaseRequest(ack_id="ack1", byte_size=50, ordering_key="")])

    assert "already lease managed" in caplog.text


def test_remove_not_managed(caplog, modify_google_logger_propagation):
    caplog.set_level(logging.DEBUG)

    leaser_ = leaser.Leaser(mock.sentinel.manager)

    leaser_.remove([requests.DropRequest(ack_id="ack1", byte_size=50, ordering_key="")])

    assert "not managed" in caplog.text


def test_remove_negative_bytes(caplog, modify_google_logger_propagation):
    caplog.set_level(logging.DEBUG)

    leaser_ = leaser.Leaser(mock.sentinel.manager)

    leaser_.add([requests.LeaseRequest(ack_id="ack1", byte_size=50, ordering_key="")])
    leaser_.remove([requests.DropRequest(ack_id="ack1", byte_size=75, ordering_key="")])

    assert leaser_.bytes == 0
    assert "unexpectedly negative" in caplog.text


def create_manager(flow_control=types.FlowControl()):
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    manager.dispatcher = mock.create_autospec(dispatcher.Dispatcher, instance=True)
    manager.is_active = True
    manager.flow_control = flow_control
    manager.ack_histogram = histogram.Histogram()
    manager._obtain_ack_deadline.return_value = 10
    return manager


def test_maintain_leases_inactive_manager(caplog, modify_google_logger_propagation):
    caplog.set_level(logging.DEBUG)
    manager = create_manager()
    manager.is_active = False

    leaser_ = leaser.Leaser(manager)
    make_sleep_mark_event_as_done(leaser_)
    leaser_.add(
        [requests.LeaseRequest(ack_id="my_ack_ID", byte_size=42, ordering_key="")]
    )

    manager._send_lease_modacks.return_value = set()
    leaser_.maintain_leases()

    # Leases should still be maintained even if the manager is inactive.
    manager._send_lease_modacks.assert_called()
    assert "exiting" in caplog.text


def test_maintain_leases_stopped(caplog, modify_google_logger_propagation):
    caplog.set_level(logging.DEBUG)
    manager = create_manager()

    leaser_ = leaser.Leaser(manager)
    leaser_.stop()

    manager._send_lease_modacks.return_value = set()
    leaser_.maintain_leases()

    assert "exiting" in caplog.text


def make_sleep_mark_event_as_done(leaser):
    # Make sleep actually trigger the done event so that heartbeat()
    # exits at the end of the first run.
    def trigger_done(timeout):
        assert 0 < timeout < 10
        leaser._stop_event.set()

    leaser._stop_event.wait = trigger_done


def test_opentelemetry_dropped_message_process_span(span_exporter):
    manager = create_manager()
    leaser_ = leaser.Leaser(manager)
    make_sleep_mark_event_as_done(leaser_)
    msg = mock.create_autospec(
        message.Message, instance=True, ack_id="ack_foo", size=10
    )
    msg.message_id = 3
    opentelemetry_data = SubscribeOpenTelemetry(msg)
    opentelemetry_data.start_subscribe_span(
        subscription="projects/projectId/subscriptions/subscriptionID",
        exactly_once_enabled=False,
        ack_id="ack_id",
        delivery_attempt=4,
    )
    opentelemetry_data.start_process_span()
    leaser_.add(
        [
            requests.LeaseRequest(
                ack_id="my ack id",
                byte_size=50,
                ordering_key="",
                opentelemetry_data=opentelemetry_data,
            )
        ]
    )
    leased_messages_dict = leaser_._leased_messages

    # Setting the `sent_time`` to be less than `cutoff` in order to make the leased message expire.
    # This will exercise the code path where the message would be dropped from the leaser
    leased_messages_dict["my ack id"] = leased_messages_dict["my ack id"]._replace(
        sent_time=0
    )

    manager._send_lease_modacks.return_value = set()
    leaser_.maintain_leases()

    opentelemetry_data.end_subscribe_span()
    spans = span_exporter.get_finished_spans()
    assert len(spans) == 2
    process_span, subscribe_span = spans

    assert process_span.name == "subscriptionID process"
    assert subscribe_span.name == "subscriptionID subscribe"

    assert len(process_span.events) == 1
    assert process_span.events[0].name == "expired"

    assert process_span.parent == subscribe_span.context


def test_opentelemetry_expired_message_exactly_once_process_span(span_exporter):
    manager = create_manager()
    leaser_ = leaser.Leaser(manager)
    make_sleep_mark_event_as_done(leaser_)
    msg = mock.create_autospec(
        message.Message, instance=True, ack_id="ack_foo", size=10
    )
    msg.message_id = 3
    opentelemetry_data = SubscribeOpenTelemetry(msg)
    opentelemetry_data.start_subscribe_span(
        subscription="projects/projectId/subscriptions/subscriptionID",
        exactly_once_enabled=True,
        ack_id="ack_id",
        delivery_attempt=4,
    )
    opentelemetry_data.start_process_span()
    leaser_.add(
        [
            requests.LeaseRequest(
                ack_id="my ack id",
                byte_size=50,
                ordering_key="",
                opentelemetry_data=opentelemetry_data,
            )
        ]
    )

    manager._send_lease_modacks.return_value = ["my ack id"]
    leaser_.maintain_leases()

    opentelemetry_data.end_subscribe_span()
    spans = span_exporter.get_finished_spans()
    assert len(spans) == 2
    process_span, subscribe_span = spans

    assert process_span.name == "subscriptionID process"
    assert subscribe_span.name == "subscriptionID subscribe"

    assert len(process_span.events) == 1
    assert process_span.events[0].name == "expired"

    assert process_span.parent == subscribe_span.context


def test_maintain_leases_ack_ids():
    manager = create_manager()
    leaser_ = leaser.Leaser(manager)
    make_sleep_mark_event_as_done(leaser_)
    leaser_.add(
        [requests.LeaseRequest(ack_id="my ack id", byte_size=50, ordering_key="")]
    )

    manager._send_lease_modacks.return_value = set()
    leaser_.maintain_leases()

    assert len(manager._send_lease_modacks.mock_calls) == 1
    call = manager._send_lease_modacks.mock_calls[0]
    ack_ids = list(call.args[0])
    assert ack_ids == ["my ack id"]
    assert call.args[1] == 10


def test_maintain_leases_expired_ack_ids_ignored():
    manager = create_manager()
    leaser_ = leaser.Leaser(manager)
    make_sleep_mark_event_as_done(leaser_)
    leaser_.add(
        [requests.LeaseRequest(ack_id="my ack id", byte_size=50, ordering_key="")]
    )
    manager._exactly_once_delivery_enabled.return_value = False
    manager._send_lease_modacks.return_value = set(["my ack id"])
    leaser_.maintain_leases()

    assert len(manager._send_lease_modacks.mock_calls) == 1

    call = manager._send_lease_modacks.mock_calls[0]
    ack_ids = list(call.args[0])
    assert ack_ids == ["my ack id"]
    assert call.args[1] == 10


def test_maintain_leases_expired_ack_ids_exactly_once():
    manager = create_manager()
    leaser_ = leaser.Leaser(manager)
    make_sleep_mark_event_as_done(leaser_)
    leaser_.add(
        [requests.LeaseRequest(ack_id="my ack id", byte_size=50, ordering_key="")]
    )
    manager._exactly_once_delivery_enabled.return_value = True
    manager._send_lease_modacks.return_value = set(["my ack id"])
    leaser_.maintain_leases()

    assert len(manager._send_lease_modacks.mock_calls) == 1

    call = manager._send_lease_modacks.mock_calls[0]
    ack_ids = list(call.args[0])
    assert ack_ids == ["my ack id"]
    assert call.args[1] == 10

    assert len(manager.dispatcher.drop.mock_calls) == 1
    call = manager.dispatcher.drop.mock_calls[0]
    drop_requests = list(call.args[0])
    assert drop_requests[0].ack_id == "my ack id"
    assert drop_requests[0].byte_size == 50
    assert drop_requests[0].ordering_key == ""


def test_maintain_leases_no_ack_ids():
    manager = create_manager()
    leaser_ = leaser.Leaser(manager)
    make_sleep_mark_event_as_done(leaser_)

    leaser_.maintain_leases()

    manager.dispatcher.modify_ack_deadline.assert_not_called()


@mock.patch("time.time", autospec=True)
def test_maintain_leases_outdated_items(time):
    manager = create_manager()
    leaser_ = leaser.Leaser(manager)
    make_sleep_mark_event_as_done(leaser_)

    # Add and start expiry timer at the beginning of the timeline.
    time.return_value = 0
    leaser_.add([requests.LeaseRequest(ack_id="ack1", byte_size=50, ordering_key="")])
    leaser_.start_lease_expiry_timer(["ack1"])

    # Add a message but don't start the lease expiry timer.
    leaser_.add([requests.LeaseRequest(ack_id="ack2", byte_size=50, ordering_key="")])

    # Add a message and start expiry timer towards the end of the timeline.
    time.return_value = manager.flow_control.max_lease_duration - 1
    leaser_.add([requests.LeaseRequest(ack_id="ack3", byte_size=50, ordering_key="")])
    leaser_.start_lease_expiry_timer(["ack3"])

    # Add a message towards the end of the timeline, but DO NOT start expiry
    # timer.
    leaser_.add([requests.LeaseRequest(ack_id="ack4", byte_size=50, ordering_key="")])

    # Now make sure time reports that we are past the end of our timeline.
    time.return_value = manager.flow_control.max_lease_duration + 1

    manager._send_lease_modacks.return_value = set()
    leaser_.maintain_leases()

    # ack2, ack3, and ack4 should be renewed. ack1 should've been dropped
    assert len(manager._send_lease_modacks.mock_calls) == 1
    call = manager._send_lease_modacks.mock_calls[0]
    ack_ids = list(call.args[0])
    assert ack_ids == ["ack2", "ack3", "ack4"]
    assert call.args[1] == 10

    manager.dispatcher.drop.assert_called_once_with(
        [requests.DropRequest(ack_id="ack1", byte_size=50, ordering_key="")]
    )


def test_start_lease_expiry_timer_unknown_ack_id():
    manager = create_manager()
    leaser_ = leaser.Leaser(manager)

    # Nothing happens when this method is called with an ack-id that hasn't been
    # added yet.
    leaser_.start_lease_expiry_timer(["ack1"])


@mock.patch("threading.Thread", autospec=True)
def test_start(thread):
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    leaser_ = leaser.Leaser(manager)

    leaser_.start()

    thread.assert_called_once_with(
        name=leaser._LEASE_WORKER_NAME, target=leaser_.maintain_leases
    )

    thread.return_value.start.assert_called_once()

    assert leaser_._thread is not None


@mock.patch("threading.Thread", autospec=True)
def test_start_already_started(thread):
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    leaser_ = leaser.Leaser(manager)
    leaser_._thread = mock.sentinel.thread

    with pytest.raises(ValueError):
        leaser_.start()

    thread.assert_not_called()


def test_stop():
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    leaser_ = leaser.Leaser(manager)
    thread = mock.create_autospec(threading.Thread, instance=True)
    leaser_._thread = thread

    leaser_.stop()

    assert leaser_._stop_event.is_set()
    thread.join.assert_called_once()
    assert leaser_._thread is None


def test_stop_no_join():
    leaser_ = leaser.Leaser(mock.sentinel.manager)

    leaser_.stop()
