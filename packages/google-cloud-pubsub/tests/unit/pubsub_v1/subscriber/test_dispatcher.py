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

import collections
import queue
import threading
from unittest import mock

import pytest
from opentelemetry import trace

from google.cloud.pubsub_v1.open_telemetry.subscribe_opentelemetry import (
    SubscribeOpenTelemetry,
)
from google.cloud.pubsub_v1.subscriber import futures
from google.cloud.pubsub_v1.subscriber._protocol import (
    dispatcher,
    helper_threads,
    requests,
    streaming_pull_manager,
)
from google.cloud.pubsub_v1.subscriber.exceptions import (
    AcknowledgeStatus,
)
from google.pubsub_v1.types import PubsubMessage


@pytest.mark.parametrize(
    "item,method_name",
    [
        (requests.AckRequest("0", 0, 0, "", None), "ack"),
        (requests.DropRequest("0", 0, ""), "drop"),
        (requests.LeaseRequest("0", 0, ""), "lease"),
        (requests.ModAckRequest("0", 0, None), "modify_ack_deadline"),
        (requests.NackRequest("0", 0, "", None), "nack"),
    ],
)
def test_dispatch_callback_active_manager(item, method_name):
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    dispatcher_ = dispatcher.Dispatcher(manager, mock.sentinel.queue)

    items = [item]

    with mock.patch.object(dispatcher_, method_name) as method:
        dispatcher_.dispatch_callback(items)

    method.assert_called_once_with([item])
    manager._exactly_once_delivery_enabled.assert_called()


@pytest.mark.parametrize(
    "item,method_name",
    [
        (requests.AckRequest("0", 0, 0, "", None), "ack"),
        (requests.DropRequest("0", 0, ""), "drop"),
        (requests.LeaseRequest("0", 0, ""), "lease"),
        (requests.ModAckRequest("0", 0, None), "modify_ack_deadline"),
        (requests.NackRequest("0", 0, "", None), "nack"),
    ],
)
def test_dispatch_callback_inactive_manager(item, method_name):
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    manager.is_active = False
    dispatcher_ = dispatcher.Dispatcher(manager, mock.sentinel.queue)

    items = [item]

    with mock.patch.object(dispatcher_, method_name) as method:
        dispatcher_.dispatch_callback(items)

    method.assert_called_once_with([item])
    manager._exactly_once_delivery_enabled.assert_called()


@pytest.mark.parametrize(
    "items,method_name",
    [
        (
            [
                requests.AckRequest("0", 0, 0, "", None),
                requests.AckRequest("0", 0, 1, "", None),
            ],
            "ack",
        ),
        (
            [
                requests.DropRequest("0", 0, ""),
                requests.DropRequest("0", 1, ""),
            ],
            "drop",
        ),
        (
            [
                requests.LeaseRequest("0", 0, ""),
                requests.LeaseRequest("0", 1, ""),
            ],
            "lease",
        ),
        (
            [
                requests.ModAckRequest("0", 0, None),
                requests.ModAckRequest("0", 1, None),
            ],
            "modify_ack_deadline",
        ),
        (
            [
                requests.NackRequest("0", 0, "", None),
                requests.NackRequest("0", 1, "", None),
            ],
            "nack",
        ),
    ],
)
def test_dispatch_duplicate_items_callback_active_manager_no_futures(
    items, method_name
):
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    dispatcher_ = dispatcher.Dispatcher(manager, mock.sentinel.queue)

    manager._exactly_once_delivery_enabled.return_value = False
    with mock.patch.object(dispatcher_, method_name) as method:
        dispatcher_.dispatch_callback(items)

    method.assert_called_once_with([items[0]])
    manager._exactly_once_delivery_enabled.assert_called()


@pytest.mark.parametrize(
    "items,method_name",
    [
        (
            [
                requests.AckRequest("0", 0, 0, "", None),
                requests.AckRequest("0", 0, 1, "", futures.Future()),
            ],
            "ack",
        ),
        (
            [
                requests.DropRequest("0", 0, ""),
                requests.DropRequest("0", 1, ""),
            ],
            "drop",
        ),
        (
            [
                requests.LeaseRequest("0", 0, ""),
                requests.LeaseRequest("0", 1, ""),
            ],
            "lease",
        ),
        (
            [
                requests.ModAckRequest("0", 0, None),
                requests.ModAckRequest("0", 1, futures.Future()),
            ],
            "modify_ack_deadline",
        ),
        (
            [
                requests.NackRequest("0", 0, "", None),
                requests.NackRequest("0", 1, "", futures.Future()),
            ],
            "nack",
        ),
    ],
)
def test_dispatch_duplicate_items_callback_active_manager_with_futures_no_eod(
    items, method_name
):
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    dispatcher_ = dispatcher.Dispatcher(manager, mock.sentinel.queue)

    manager._exactly_once_delivery_enabled.return_value = False
    with mock.patch.object(dispatcher_, method_name) as method:
        dispatcher_.dispatch_callback(items)

    method.assert_called_once_with([items[0]])
    manager._exactly_once_delivery_enabled.assert_called()

    if method_name != "drop" and method_name != "lease":
        assert items[1].future.result() == AcknowledgeStatus.SUCCESS


@pytest.mark.parametrize(
    "items,method_name",
    [
        (
            [
                requests.AckRequest("0", 0, 0, "", None),
                requests.AckRequest("0", 0, 1, "", futures.Future()),
            ],
            "ack",
        ),
        (
            [
                requests.DropRequest("0", 0, ""),
                requests.DropRequest("0", 1, ""),
            ],
            "drop",
        ),
        (
            [
                requests.LeaseRequest("0", 0, ""),
                requests.LeaseRequest("0", 1, ""),
            ],
            "lease",
        ),
        (
            [
                requests.ModAckRequest("0", 0, None),
                requests.ModAckRequest("0", 1, futures.Future()),
            ],
            "modify_ack_deadline",
        ),
        (
            [
                requests.NackRequest("0", 0, "", None),
                requests.NackRequest("0", 1, "", futures.Future()),
            ],
            "nack",
        ),
    ],
)
def test_dispatch_duplicate_items_callback_active_manager_with_futures_eod(
    items, method_name
):
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    dispatcher_ = dispatcher.Dispatcher(manager, mock.sentinel.queue)

    manager._exactly_once_delivery_enabled.return_value = True
    with mock.patch.object(dispatcher_, method_name) as method:
        dispatcher_.dispatch_callback(items)

    method.assert_called_once_with([items[0]])
    manager._exactly_once_delivery_enabled.assert_called()

    if method_name != "drop" and method_name != "lease":
        with pytest.raises(ValueError) as err:
            items[1].future.result()
            assert err.errisinstance(ValueError)


def test_dispatch_duplicate_items_diff_types_callback_active_manager_with_futures_eod():
    ack_future = futures.Future()
    ack_request = requests.AckRequest("0", 0, 1, "", ack_future)
    drop_request = requests.DropRequest("0", 1, "")
    lease_request = requests.LeaseRequest("0", 1, "")
    nack_future = futures.Future()
    nack_request = requests.NackRequest("0", 1, "", nack_future)
    modack_future = futures.Future()
    modack_request = requests.ModAckRequest("0", 1, modack_future)

    items = [ack_request, drop_request, lease_request, nack_request, modack_request]

    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    dispatcher_ = dispatcher.Dispatcher(manager, mock.sentinel.queue)

    manager._exactly_once_delivery_enabled.return_value = True
    with mock.patch.multiple(
        dispatcher_,
        ack=mock.DEFAULT,
        nack=mock.DEFAULT,
        drop=mock.DEFAULT,
        lease=mock.DEFAULT,
        modify_ack_deadline=mock.DEFAULT,
    ):
        dispatcher_.dispatch_callback(items)
        manager._exactly_once_delivery_enabled.assert_called()
        dispatcher_.ack.assert_called_once_with([ack_request])
        dispatcher_.drop.assert_called_once_with([drop_request])
        dispatcher_.lease.assert_called_once_with([lease_request])
        dispatcher_.nack.assert_called_once_with([nack_request])
        dispatcher_.modify_ack_deadline.assert_called_once_with([modack_request])


@pytest.mark.parametrize(
    "items,method_name",
    [
        (
            [
                requests.AckRequest("0", 0, 0, "", None),
                requests.AckRequest("0", 0, 1, "", None),
            ],
            "ack",
        ),
        (
            [
                requests.DropRequest("0", 0, ""),
                requests.DropRequest("0", 1, ""),
            ],
            "drop",
        ),
        (
            [
                requests.LeaseRequest("0", 0, ""),
                requests.LeaseRequest("0", 1, ""),
            ],
            "lease",
        ),
        (
            [
                requests.ModAckRequest("0", 0, None),
                requests.ModAckRequest("0", 1, None),
            ],
            "modify_ack_deadline",
        ),
        (
            [
                requests.NackRequest("0", 0, "", None),
                requests.NackRequest("0", 1, "", None),
            ],
            "nack",
        ),
    ],
)
def test_dispatch_duplicate_items_callback_active_manager_no_futures_eod(
    items, method_name
):
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    dispatcher_ = dispatcher.Dispatcher(manager, mock.sentinel.queue)

    manager._exactly_once_delivery_enabled.return_value = True
    with mock.patch.object(dispatcher_, method_name) as method:
        dispatcher_.dispatch_callback(items)

    method.assert_called_once_with([items[0]])
    manager._exactly_once_delivery_enabled.assert_called()


def test_unknown_request_type():
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    dispatcher_ = dispatcher.Dispatcher(manager, mock.sentinel.queue)

    items = ["a random string, not a known request type"]
    manager.send_unary_ack.return_value = (items, [])
    with pytest.warns(RuntimeWarning, match="Skipping unknown request item of type"):
        dispatcher_.dispatch_callback(items)


def test_opentelemetry_modify_ack_deadline(span_exporter):
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    dispatcher_ = dispatcher.Dispatcher(manager, mock.sentinel.queue)
    opentelemetry_data = SubscribeOpenTelemetry(message=PubsubMessage(data=b"foo"))
    opentelemetry_data.start_subscribe_span(
        subscription="projects/projectID/subscriptions/subscriptionID",
        exactly_once_enabled=True,
        ack_id="ack_id",
        delivery_attempt=5,
    )

    items = [
        requests.ModAckRequest(
            ack_id="ack_id_string",
            seconds=60,
            future=None,
            opentelemetry_data=opentelemetry_data,
        )
    ]
    manager.send_unary_modack.return_value = (items, [])
    dispatcher_.modify_ack_deadline(items)

    # Subscribe span would not have ended as part of a modack. So, end it
    # in the test, so that we can export and assert its contents.
    opentelemetry_data.end_subscribe_span()
    spans = span_exporter.get_finished_spans()
    assert len(spans) == 1
    subscribe_span = spans[0]

    assert len(subscribe_span.events) == 2
    assert subscribe_span.events[0].name == "modack start"
    assert subscribe_span.events[1].name == "modack end"


def test_opentelemetry_ack(span_exporter):
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    dispatcher_ = dispatcher.Dispatcher(manager, mock.sentinel.queue)

    data1 = SubscribeOpenTelemetry(message=PubsubMessage(data=b"foo"))
    data1.start_subscribe_span(
        subscription="projects/projectID/subscriptions/subscriptionID",
        exactly_once_enabled=True,
        ack_id="ack_id",
        delivery_attempt=5,
    )
    data2 = SubscribeOpenTelemetry(message=PubsubMessage(data=b"foo"))
    data2.start_subscribe_span(
        subscription="projects/projectID/subscriptions/subscriptionID",
        exactly_once_enabled=True,
        ack_id="ack_id",
        delivery_attempt=5,
    )
    items = [
        requests.AckRequest(
            ack_id="ack_id_string",
            byte_size=0,
            time_to_ack=20,
            ordering_key="",
            future=None,
            opentelemetry_data=data1,
        ),
        requests.AckRequest(
            ack_id="ack_id_string2",
            byte_size=0,
            time_to_ack=20,
            ordering_key="",
            future=None,
            opentelemetry_data=data2,
        ),
    ]
    manager.send_unary_ack.return_value = (items, [])
    mock_span_context = mock.Mock(spec=trace.SpanContext)
    mock_span_context.trace_flags.sampled = False
    with mock.patch.object(
        data2._subscribe_span, "get_span_context", return_value=mock_span_context
    ):
        dispatcher_.ack(items)

    spans = span_exporter.get_finished_spans()

    assert len(spans) == 3
    ack_span = spans[0]

    for subscribe_span in spans[1:]:
        assert subscribe_span.attributes["messaging.gcp_pubsub.result"] == "acked"
        assert len(subscribe_span.events) == 2
        assert subscribe_span.events[0].name == "ack start"
        assert subscribe_span.events[1].name == "ack end"

    # This subscribe span is sampled, so we expect it to be linked to the ack
    # span.
    assert len(spans[1].links) == 1
    assert spans[1].links[0].context == ack_span.context
    assert len(spans[1].links[0].attributes) == 1
    assert spans[1].links[0].attributes["messaging.operation.name"] == "ack"
    # This subscribe span is not sampled, so we expect it to not be linked to
    # the ack span
    assert len(spans[2].links) == 0

    assert ack_span.name == "subscriptionID ack"
    assert ack_span.kind == trace.SpanKind.CLIENT
    assert ack_span.parent is None
    assert len(ack_span.links) == 1
    assert ack_span.attributes["messaging.system"] == "gcp_pubsub"
    assert ack_span.attributes["messaging.batch.message_count"] == 2
    assert ack_span.attributes["messaging.operation"] == "ack"
    assert ack_span.attributes["gcp.project_id"] == "projectID"
    assert ack_span.attributes["messaging.destination.name"] == "subscriptionID"
    assert ack_span.attributes["code.function"] == "ack"


def test_ack():
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    dispatcher_ = dispatcher.Dispatcher(manager, mock.sentinel.queue)

    items = [
        requests.AckRequest(
            ack_id="ack_id_string",
            byte_size=0,
            time_to_ack=20,
            ordering_key="",
            future=None,
        )
    ]
    manager.send_unary_ack.return_value = (items, [])
    dispatcher_.ack(items)

    manager.send_unary_ack.assert_called_once_with(
        ack_ids=["ack_id_string"], ack_reqs_dict={"ack_id_string": items[0]}
    )

    manager.leaser.remove.assert_called_once_with(items)
    manager.maybe_resume_consumer.assert_called_once()
    manager.ack_histogram.add.assert_called_once_with(20)


def test_ack_no_time():
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    dispatcher_ = dispatcher.Dispatcher(manager, mock.sentinel.queue)

    items = [
        requests.AckRequest(
            ack_id="ack_id_string",
            byte_size=0,
            time_to_ack=None,
            ordering_key="",
            future=None,
        )
    ]
    manager.send_unary_ack.return_value = (items, [])
    dispatcher_.ack(items)

    manager.send_unary_ack.assert_called_once_with(
        ack_ids=["ack_id_string"], ack_reqs_dict={"ack_id_string": items[0]}
    )

    manager.ack_histogram.add.assert_not_called()


def test_ack_splitting_large_payload():
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    dispatcher_ = dispatcher.Dispatcher(manager, mock.sentinel.queue)

    items = [
        # use realistic lengths for ACK IDs (max 176 bytes)
        requests.AckRequest(
            ack_id=str(i).zfill(176),
            byte_size=0,
            time_to_ack=20,
            ordering_key="",
            future=None,
        )
        for i in range(5001)
    ]
    manager.send_unary_ack.return_value = (items, [])
    dispatcher_.ack(items)

    calls = manager.send_unary_ack.call_args_list
    assert len(calls) == 6

    all_ack_ids = {item.ack_id for item in items}
    sent_ack_ids = collections.Counter()

    for call in calls:
        ack_ids = call[1]["ack_ids"]
        assert len(ack_ids) <= dispatcher._ACK_IDS_BATCH_SIZE
        sent_ack_ids.update(ack_ids)

    assert set(sent_ack_ids) == all_ack_ids  # all messages should have been ACK-ed
    assert sent_ack_ids.most_common(1)[0][1] == 1  # each message ACK-ed exactly once


def test_retry_acks_in_new_thread():
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    dispatcher_ = dispatcher.Dispatcher(manager, mock.sentinel.queue)

    f = futures.Future()
    items = [
        requests.AckRequest(
            ack_id="ack_id_string",
            byte_size=0,
            time_to_ack=20,
            ordering_key="",
            future=f,
        )
    ]
    # failure triggers creation of new retry thread
    manager.send_unary_ack.side_effect = [([], items)]
    with mock.patch("time.sleep", return_value=None):
        with mock.patch.object(threading, "Thread", autospec=True) as Thread:
            dispatcher_.ack(items)

            assert len(Thread.mock_calls) == 2
            ctor_call = Thread.mock_calls[0]
            assert ctor_call.kwargs["name"] == "Thread-RetryAcks"
            assert ctor_call.kwargs["target"].args[0] == items
            assert ctor_call.kwargs["daemon"]


def test_opentelemetry_retry_acks(span_exporter):
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    dispatcher_ = dispatcher.Dispatcher(manager, mock.sentinel.queue)
    data1 = SubscribeOpenTelemetry(message=PubsubMessage(data=b"foo"))
    data1.start_subscribe_span(
        subscription="projects/projectID/subscriptions/subscriptionID",
        exactly_once_enabled=True,
        ack_id="ack_id",
        delivery_attempt=5,
    )
    data2 = SubscribeOpenTelemetry(message=PubsubMessage(data=b"foo"))
    data2.start_subscribe_span(
        subscription="projects/projectID/subscriptions/subscriptionID",
        exactly_once_enabled=True,
        ack_id="ack_id",
        delivery_attempt=5,
    )

    f = futures.Future()
    items = [
        requests.AckRequest(
            ack_id="ack_id_string",
            byte_size=0,
            time_to_ack=20,
            ordering_key="",
            future=f,
            opentelemetry_data=data1,
        ),
        requests.AckRequest(
            ack_id="ack_id_string2",
            byte_size=0,
            time_to_ack=20,
            ordering_key="",
            future=f,
            opentelemetry_data=data2,
        ),
    ]
    manager.send_unary_ack.side_effect = [(items, [])]
    mock_span_context = mock.Mock(spec=trace.SpanContext)
    mock_span_context.trace_flags.sampled = False
    with mock.patch("time.sleep", return_value=None):
        with mock.patch.object(
            data2._subscribe_span, "get_span_context", return_value=mock_span_context
        ):
            dispatcher_._retry_acks(items)

    spans = span_exporter.get_finished_spans()

    assert len(spans) == 3
    ack_span = spans[0]

    for subscribe_span in spans[1:]:
        assert "messaging.gcp_pubsub.result" in subscribe_span.attributes
        assert subscribe_span.attributes["messaging.gcp_pubsub.result"] == "acked"
        assert len(subscribe_span.events) == 2
        assert subscribe_span.events[0].name == "ack start"
        assert subscribe_span.events[1].name == "ack end"

    # This subscribe span is sampled, so we expect it to be linked to the ack
    # span.
    assert len(spans[1].links) == 1
    assert spans[1].links[0].context == ack_span.context
    assert len(spans[1].links[0].attributes) == 1
    assert spans[1].links[0].attributes["messaging.operation.name"] == "ack"
    # This subscribe span is not sampled, so we expect it to not be linked to
    # the ack span
    assert len(spans[2].links) == 0

    assert ack_span.name == "subscriptionID ack"
    assert ack_span.kind == trace.SpanKind.CLIENT
    assert ack_span.parent is None
    assert len(ack_span.links) == 1
    assert ack_span.attributes["messaging.system"] == "gcp_pubsub"
    assert ack_span.attributes["messaging.batch.message_count"] == 2
    assert ack_span.attributes["messaging.operation"] == "ack"
    assert ack_span.attributes["gcp.project_id"] == "projectID"
    assert ack_span.attributes["messaging.destination.name"] == "subscriptionID"
    assert ack_span.attributes["code.function"] == "ack"


def test_retry_acks():
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    dispatcher_ = dispatcher.Dispatcher(manager, mock.sentinel.queue)

    f = futures.Future()
    items = [
        requests.AckRequest(
            ack_id="ack_id_string",
            byte_size=0,
            time_to_ack=20,
            ordering_key="",
            future=f,
        )
    ]
    # first and second `send_unary_ack` calls fail, third one succeeds
    manager.send_unary_ack.side_effect = [([], items), ([], items), (items, [])]
    with mock.patch("time.sleep", return_value=None):
        dispatcher_._retry_acks(items)

    manager.send_unary_ack.assert_has_calls(
        [
            mock.call(
                ack_ids=["ack_id_string"], ack_reqs_dict={"ack_id_string": items[0]}
            ),
            mock.call(
                ack_ids=["ack_id_string"], ack_reqs_dict={"ack_id_string": items[0]}
            ),
            mock.call(
                ack_ids=["ack_id_string"], ack_reqs_dict={"ack_id_string": items[0]}
            ),
        ]
    )


def test_retry_modacks_in_new_thread():
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    dispatcher_ = dispatcher.Dispatcher(manager, mock.sentinel.queue)

    f = futures.Future()
    items = [
        requests.ModAckRequest(
            ack_id="ack_id_string",
            seconds=20,
            future=f,
        )
    ]
    # failure triggers creation of new retry thread
    manager.send_unary_modack.side_effect = [([], items)]
    with mock.patch("time.sleep", return_value=None):
        with mock.patch.object(threading, "Thread", autospec=True) as Thread:
            dispatcher_.modify_ack_deadline(items)

            assert len(Thread.mock_calls) == 2
            ctor_call = Thread.mock_calls[0]
            assert ctor_call.kwargs["name"] == "Thread-RetryModAcks"
            assert ctor_call.kwargs["target"].args[0] == items
            assert ctor_call.kwargs["daemon"]


def test_opentelemetry_retry_modacks(span_exporter):
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    dispatcher_ = dispatcher.Dispatcher(manager, mock.sentinel.queue)

    opentelemetry_data = SubscribeOpenTelemetry(message=PubsubMessage(data=b"foo"))
    opentelemetry_data.start_subscribe_span(
        subscription="projects/projectID/subscriptions/subscriptionID",
        exactly_once_enabled=True,
        ack_id="ack_id",
        delivery_attempt=5,
    )

    f = futures.Future()
    items = [
        requests.ModAckRequest(
            ack_id="ack_id_string",
            seconds=20,
            future=f,
            opentelemetry_data=opentelemetry_data,
        )
    ]
    manager.send_unary_modack.side_effect = [(items, [])]
    with mock.patch("time.sleep", return_value=None):
        dispatcher_._retry_modacks(items)

    # Subscribe span wouldn't be ended for modacks. So, end it in the test, so
    # that we can export and assert its contents.
    opentelemetry_data.end_subscribe_span()
    spans = span_exporter.get_finished_spans()
    assert len(spans) == 1
    subscribe_span = spans[0]

    assert len(subscribe_span.events) == 1
    assert subscribe_span.events[0].name == "modack end"


def test_opentelemetry_retry_nacks(span_exporter):
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    dispatcher_ = dispatcher.Dispatcher(manager, mock.sentinel.queue)

    data1 = SubscribeOpenTelemetry(message=PubsubMessage(data=b"foo"))
    data1.start_subscribe_span(
        subscription="projects/projectID/subscriptions/subscriptionID",
        exactly_once_enabled=True,
        ack_id="ack_id1",
        delivery_attempt=5,
    )
    data2 = SubscribeOpenTelemetry(message=PubsubMessage(data=b"foo"))
    data2.start_subscribe_span(
        subscription="projects/projectID/subscriptions/subscriptionID",
        exactly_once_enabled=True,
        ack_id="ack_id2",
        delivery_attempt=5,
    )

    f = futures.Future()
    items = [
        requests.ModAckRequest(
            ack_id="ack_id1",
            seconds=0,
            future=f,
            opentelemetry_data=data1,
        ),
        requests.ModAckRequest(
            ack_id="ack_id2",
            seconds=0,
            future=f,
            opentelemetry_data=data2,
        ),
    ]
    manager.send_unary_modack.side_effect = [(items, [])]
    mock_span_context = mock.Mock(spec=trace.SpanContext)
    mock_span_context.trace_flags.sampled = False
    with mock.patch("time.sleep", return_value=None):
        with mock.patch.object(
            data2._subscribe_span, "get_span_context", return_value=mock_span_context
        ):
            dispatcher_._retry_modacks(items)

    spans = span_exporter.get_finished_spans()
    assert len(spans) == 3
    nack_span = spans[0]

    for subscribe_span in spans[1:]:
        assert "messaging.gcp_pubsub.result" in subscribe_span.attributes
        assert subscribe_span.attributes["messaging.gcp_pubsub.result"] == "nacked"
        assert len(subscribe_span.events) == 1
        assert subscribe_span.events[0].name == "nack end"

    # This subscribe span is sampled, so we expect it to be linked to the nack
    # span.
    assert len(spans[1].links) == 1
    assert spans[1].links[0].context == nack_span.context
    assert len(spans[1].links[0].attributes) == 1
    assert spans[1].links[0].attributes["messaging.operation.name"] == "nack"
    # This subscribe span is not sampled, so we expect it to not be linked to
    # the nack span
    assert len(spans[2].links) == 0

    assert nack_span.name == "subscriptionID nack"
    assert nack_span.kind == trace.SpanKind.CLIENT
    assert nack_span.parent is None
    assert len(nack_span.links) == 1
    assert nack_span.attributes["messaging.system"] == "gcp_pubsub"
    assert nack_span.attributes["messaging.batch.message_count"] == 2
    assert nack_span.attributes["messaging.operation"] == "nack"
    assert nack_span.attributes["gcp.project_id"] == "projectID"
    assert nack_span.attributes["messaging.destination.name"] == "subscriptionID"
    assert nack_span.attributes["code.function"] == "modify_ack_deadline"


def test_retry_modacks():
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    dispatcher_ = dispatcher.Dispatcher(manager, mock.sentinel.queue)

    f = futures.Future()
    items = [
        requests.ModAckRequest(
            ack_id="ack_id_string",
            seconds=20,
            future=f,
        )
    ]
    # first and second calls fail, third one succeeds
    manager.send_unary_modack.side_effect = [([], items), ([], items), (items, [])]
    with mock.patch("time.sleep", return_value=None):
        dispatcher_._retry_modacks(items)

    manager.send_unary_modack.assert_has_calls(
        [
            mock.call(
                modify_deadline_ack_ids=["ack_id_string"],
                modify_deadline_seconds=[20],
                ack_reqs_dict={"ack_id_string": items[0]},
            ),
            mock.call(
                modify_deadline_ack_ids=["ack_id_string"],
                modify_deadline_seconds=[20],
                ack_reqs_dict={"ack_id_string": items[0]},
            ),
            mock.call(
                modify_deadline_ack_ids=["ack_id_string"],
                modify_deadline_seconds=[20],
                ack_reqs_dict={"ack_id_string": items[0]},
            ),
        ]
    )


def test_lease():
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    dispatcher_ = dispatcher.Dispatcher(manager, mock.sentinel.queue)

    items = [
        requests.LeaseRequest(ack_id="ack_id_string", byte_size=10, ordering_key="")
    ]
    dispatcher_.lease(items)

    manager.leaser.add.assert_called_once_with(items)
    manager.maybe_pause_consumer.assert_called_once()


def test_drop_unordered_messages():
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    dispatcher_ = dispatcher.Dispatcher(manager, mock.sentinel.queue)

    items = [
        requests.DropRequest(ack_id="ack_id_string", byte_size=10, ordering_key="")
    ]
    dispatcher_.drop(items)

    manager.leaser.remove.assert_called_once_with(items)
    assert list(manager.activate_ordering_keys.call_args.args[0]) == []
    manager.maybe_resume_consumer.assert_called_once()


def test_drop_ordered_messages():
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    dispatcher_ = dispatcher.Dispatcher(manager, mock.sentinel.queue)

    items = [
        requests.DropRequest(ack_id="ack_id_string", byte_size=10, ordering_key=""),
        requests.DropRequest(ack_id="ack_id_string", byte_size=10, ordering_key="key1"),
        requests.DropRequest(ack_id="ack_id_string", byte_size=10, ordering_key="key2"),
    ]
    dispatcher_.drop(items)

    manager.leaser.remove.assert_called_once_with(items)
    assert list(manager.activate_ordering_keys.call_args.args[0]) == ["key1", "key2"]
    manager.maybe_resume_consumer.assert_called_once()


def test_opentelemetry_nack(span_exporter):
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    dispatcher_ = dispatcher.Dispatcher(manager, mock.sentinel.queue)

    data1 = SubscribeOpenTelemetry(message=PubsubMessage(data=b"foo"))
    data1.start_subscribe_span(
        subscription="projects/projectID/subscriptions/subscriptionID",
        exactly_once_enabled=True,
        ack_id="ack_id",
        delivery_attempt=5,
    )
    data2 = SubscribeOpenTelemetry(message=PubsubMessage(data=b"foo"))
    data2.start_subscribe_span(
        subscription="projects/projectID/subscriptions/subscriptionID",
        exactly_once_enabled=True,
        ack_id="ack_id2",
        delivery_attempt=5,
    )

    items = [
        requests.NackRequest(
            ack_id="ack_id",
            byte_size=10,
            ordering_key="",
            future=None,
            opentelemetry_data=data1,
        ),
        requests.NackRequest(
            ack_id="ack_id2",
            byte_size=10,
            ordering_key="",
            future=None,
            opentelemetry_data=data2,
        ),
    ]
    response_items = [
        requests.ModAckRequest(
            ack_id="ack_id",
            seconds=0,
            future=None,
            opentelemetry_data=data1,
        ),
        requests.ModAckRequest(
            ack_id="ack_id2",
            seconds=0,
            future=None,
            opentelemetry_data=data2,
        ),
    ]
    manager.send_unary_modack.return_value = (response_items, [])

    mock_span_context = mock.Mock(spec=trace.SpanContext)
    mock_span_context.trace_flags.sampled = False
    with mock.patch.object(
        data2._subscribe_span, "get_span_context", return_value=mock_span_context
    ):
        dispatcher_.nack(items)

    spans = span_exporter.get_finished_spans()

    assert len(spans) == 3
    nack_span = spans[0]
    for subscribe_span in spans[1:]:
        assert "messaging.gcp_pubsub.result" in subscribe_span.attributes
        assert subscribe_span.attributes["messaging.gcp_pubsub.result"] == "nacked"
        assert len(subscribe_span.events) == 2
        assert subscribe_span.events[0].name == "nack start"
        assert subscribe_span.events[1].name == "nack end"

    # This subscribe span is sampled, so we expect it to be linked to the nack
    # span.
    assert len(spans[1].links) == 1
    assert spans[1].links[0].context == nack_span.context
    assert len(spans[1].links[0].attributes) == 1
    assert spans[1].links[0].attributes["messaging.operation.name"] == "nack"
    # This subscribe span is not sampled, so we expect it to not be linked to
    # the nack span
    assert len(spans[2].links) == 0

    assert nack_span.name == "subscriptionID nack"
    assert nack_span.kind == trace.SpanKind.CLIENT
    assert nack_span.parent is None
    assert len(nack_span.links) == 1
    assert nack_span.attributes["messaging.system"] == "gcp_pubsub"
    assert nack_span.attributes["messaging.batch.message_count"] == 2
    assert nack_span.attributes["messaging.operation"] == "nack"
    assert nack_span.attributes["gcp.project_id"] == "projectID"
    assert nack_span.attributes["messaging.destination.name"] == "subscriptionID"
    assert nack_span.attributes["code.function"] == "modify_ack_deadline"


def test_nack():
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    dispatcher_ = dispatcher.Dispatcher(manager, mock.sentinel.queue)

    items = [
        requests.NackRequest(
            ack_id="ack_id_string", byte_size=10, ordering_key="", future=None
        )
    ]
    manager.send_unary_modack.return_value = (items, [])
    dispatcher_.nack(items)
    calls = manager.send_unary_modack.call_args_list
    assert len(calls) == 1

    for call in calls:
        modify_deadline_ack_ids = call[1]["modify_deadline_ack_ids"]
        assert list(modify_deadline_ack_ids) == ["ack_id_string"]
        modify_deadline_seconds = call[1]["modify_deadline_seconds"]
        assert list(modify_deadline_seconds) == [0]
        ack_reqs_dict = call[1]["ack_reqs_dict"]
        assert ack_reqs_dict == {
            "ack_id_string": requests.ModAckRequest(
                ack_id="ack_id_string", seconds=0, future=None
            )
        }


def test_modify_ack_deadline():
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    dispatcher_ = dispatcher.Dispatcher(manager, mock.sentinel.queue)

    items = [requests.ModAckRequest(ack_id="ack_id_string", seconds=60, future=None)]
    manager.send_unary_modack.return_value = (items, [])
    dispatcher_.modify_ack_deadline(items)
    calls = manager.send_unary_modack.call_args_list
    assert len(calls) == 1

    for call in calls:
        modify_deadline_ack_ids = call[1]["modify_deadline_ack_ids"]
        assert list(modify_deadline_ack_ids) == ["ack_id_string"]
        modify_deadline_seconds = call[1]["modify_deadline_seconds"]
        assert list(modify_deadline_seconds) == [60]
        ack_reqs_dict = call[1]["ack_reqs_dict"]
        assert ack_reqs_dict == {"ack_id_string": items[0]}


def test_modify_ack_deadline_splitting_large_payload():
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    dispatcher_ = dispatcher.Dispatcher(manager, mock.sentinel.queue)

    items = [
        # use realistic lengths for ACK IDs (max 176 bytes)
        requests.ModAckRequest(ack_id=str(i).zfill(176), seconds=60, future=None)
        for i in range(5001)
    ]
    manager.send_unary_modack.return_value = (items, [])
    dispatcher_.modify_ack_deadline(items)

    calls = manager.send_unary_modack.call_args_list
    assert len(calls) == 6

    all_ack_ids = {item.ack_id for item in items}
    sent_ack_ids = collections.Counter()

    for call in calls:
        modack_ackids = list(call[1]["modify_deadline_ack_ids"])
        assert len(modack_ackids) <= dispatcher._ACK_IDS_BATCH_SIZE
        sent_ack_ids.update(modack_ackids)

    assert set(sent_ack_ids) == all_ack_ids  # all messages should have been MODACK-ed
    assert sent_ack_ids.most_common(1)[0][1] == 1  # each message MODACK-ed exactly once


def test_modify_ack_deadline_splitting_large_payload_with_default_deadline():
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    dispatcher_ = dispatcher.Dispatcher(manager, mock.sentinel.queue)

    items = [
        # use realistic lengths for ACK IDs (max 176 bytes)
        requests.ModAckRequest(ack_id=str(i).zfill(176), seconds=60, future=None)
        for i in range(5001)
    ]
    manager.send_unary_modack.return_value = (items, [])
    dispatcher_.modify_ack_deadline(items, 60)

    calls = manager.send_unary_modack.call_args_list
    assert len(calls) == 6

    all_ack_ids = {item.ack_id for item in items}
    sent_ack_ids = collections.Counter()

    for call in calls:
        modack_ackids = list(call[1]["modify_deadline_ack_ids"])
        modack_deadline_seconds = call[1]["modify_deadline_seconds"]
        default_deadline = call[1]["default_deadline"]
        assert len(list(modack_ackids)) <= dispatcher._ACK_IDS_BATCH_SIZE
        assert modack_deadline_seconds is None
        assert default_deadline == 60
        sent_ack_ids.update(modack_ackids)

    assert set(sent_ack_ids) == all_ack_ids  # all messages should have been MODACK-ed
    assert sent_ack_ids.most_common(1)[0][1] == 1  # each message MODACK-ed exactly once


@mock.patch("threading.Thread", autospec=True)
def test_start(thread):
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    dispatcher_ = dispatcher.Dispatcher(manager, mock.sentinel.queue)

    dispatcher_.start()

    thread.assert_called_once_with(
        name=dispatcher._CALLBACK_WORKER_NAME, target=mock.ANY
    )

    thread.return_value.start.assert_called_once()

    assert dispatcher_._thread is not None


@mock.patch("threading.Thread", autospec=True)
def test_start_already_started(thread):
    manager = mock.create_autospec(
        streaming_pull_manager.StreamingPullManager, instance=True
    )
    dispatcher_ = dispatcher.Dispatcher(manager, mock.sentinel.queue)
    dispatcher_._thread = mock.sentinel.thread

    with pytest.raises(ValueError):
        dispatcher_.start()

    thread.assert_not_called()


def test_stop():
    queue_ = queue.Queue()
    dispatcher_ = dispatcher.Dispatcher(mock.sentinel.manager, queue_)
    thread = mock.create_autospec(threading.Thread, instance=True)
    dispatcher_._thread = thread

    dispatcher_.stop()

    assert queue_.get() is helper_threads.STOP
    thread.join.assert_called_once()
    assert dispatcher_._thread is None


def test_stop_no_join():
    dispatcher_ = dispatcher.Dispatcher(mock.sentinel.manager, mock.sentinel.queue)

    dispatcher_.stop()
