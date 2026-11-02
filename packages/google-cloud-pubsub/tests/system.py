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

from __future__ import absolute_import

import concurrent.futures
import datetime
import itertools
import operator as op
import os
import threading
import time
from typing import Any, Callable, TypeVar, cast
from unittest import mock

import google.auth
import psutil
import pytest
from flaky import flaky
from google.api_core import exceptions as core_exceptions
from test_utils.system import unique_resource_id

from google.cloud import pubsub_v1
from google.cloud.pubsub_v1 import exceptions, futures, types
from google.pubsub_v1 import types as gapic_types

C = TypeVar("C", bound=Callable[..., Any])
typed_flaky = cast(Callable[[C], C], flaky(max_runs=5, min_passes=1))


@pytest.fixture(scope="module")
def project():
    _, default_project = google.auth.default()
    yield default_project


@pytest.fixture(params=["grpc", "rest"])
def publisher(request):
    yield pubsub_v1.PublisherClient(transport=request.param)


@pytest.fixture(params=["grpc", "rest"])
def subscriber(request):
    yield pubsub_v1.SubscriberClient(transport=request.param)


@pytest.fixture
def topic_path_base(project, publisher):
    topic_name = "t" + unique_resource_id("-")
    yield publisher.topic_path(project, topic_name)


@pytest.fixture
def subscription_path_base(project, subscriber):
    sub_name = "s" + unique_resource_id("-")
    yield subscriber.subscription_path(project, sub_name)


@pytest.fixture
def cleanup():
    registry = []
    yield registry

    # Perform all clean up.
    for to_call, args, kwargs in registry:
        try:
            to_call(*args, **kwargs)
        except core_exceptions.NotFound:
            pass


def test_publish_messages(publisher, topic_path_base, cleanup):
    # Customize topic path to test.
    topic_path = topic_path_base + "-publish-messages"
    # Make sure the topic gets deleted.
    cleanup.append((publisher.delete_topic, (), {"topic": topic_path}))

    publisher.create_topic(name=topic_path)

    futures = [
        publisher.publish(
            topic_path, b"The hail in Wales falls mainly on the snails.", num=str(i)
        )
        for i in range(500)
    ]

    for future in futures:
        result = future.result()
        assert isinstance(result, str)


def test_publish_large_messages(topic_path_base, cleanup):
    publisher = pubsub_v1.PublisherClient(transport="grpc")
    # Customize topic path to test.
    topic_path = topic_path_base + "-publish-large-messages"
    # Make sure the topic gets deleted.
    cleanup.append((publisher.delete_topic, (), {"topic": topic_path}))

    # Each message should be smaller than 10**7 bytes (the server side limit for
    # PublishRequest), but all messages combined in a PublishRequest should
    # slightly exceed that threshold to make sure the publish code handles these
    # cases well.
    # Mind that the total PublishRequest size must still be smaller than
    # 10 * 1024 * 1024 bytes in order to not exceed the max request body size limit.
    msg_data = b"x" * (2 * 10**6)

    publisher.batch_settings = types.BatchSettings(
        max_bytes=11 * 1000 * 1000,  # more than the server limit of 10 ** 7
        max_latency=2.0,  # so that autocommit happens after publishing all messages
        max_messages=100,
    )
    publisher.create_topic(name=topic_path)

    futures = [publisher.publish(topic_path, msg_data, num=str(i)) for i in range(5)]

    # If the publishing logic correctly split all messages into more than a
    # single batch despite a high BatchSettings.max_bytes limit, there should
    # be no "InvalidArgument: request_size is too large" error.
    for future in futures:
        result = future.result(timeout=10)
        assert isinstance(result, str)  # the message ID


def test_subscribe_to_messages(
    publisher, topic_path_base, subscription_path_base, cleanup
):
    subscriber = pubsub_v1.SubscriberClient(transport="grpc")
    # Customize topic path to test.
    topic_path = topic_path_base + "-subscribe-to-messages"
    subscription_path = subscription_path_base + "-subscribe-to-messages"
    # Make sure the topic and subscription get deleted.
    cleanup.append((publisher.delete_topic, (), {"topic": topic_path}))
    cleanup.append(
        (subscriber.delete_subscription, (), {"subscription": subscription_path})
    )

    # Create a topic.
    publisher.create_topic(name=topic_path)

    # Subscribe to the topic. This must happen before the messages
    # are published.
    subscriber.create_subscription(name=subscription_path, topic=topic_path)

    # Publish some messages.
    futures = [
        publisher.publish(topic_path, b"Wooooo! The claaaaaw!", num=str(index))
        for index in range(50)
    ]

    # Make sure the publish completes.
    for future in futures:
        future.result()

    # Actually open the subscription and hold it open for a few seconds.
    # The callback should process the message numbers to prove
    # that we got everything at least once.
    callback = AckCallback()
    future = subscriber.subscribe(subscription_path, callback)
    for second in range(10):
        time.sleep(1)

        # The callback should have fired at least fifty times, but it
        # may take some time.
        if callback.calls >= 50:
            return

    # Okay, we took too long; fail out.
    assert callback.calls >= 50

    future.cancel()


def test_subscribe_to_messages_async_callbacks(
    publisher, topic_path_base, subscription_path_base, cleanup
):
    subscriber = pubsub_v1.SubscriberClient(transport="grpc")
    # Customize topic path to test.
    custom_str = "-subscribe-to-messages-async-callback"
    topic_path = topic_path_base + custom_str
    subscription_path = subscription_path_base + custom_str
    # Make sure the topic and subscription get deleted.
    cleanup.append((publisher.delete_topic, (), {"topic": topic_path}))
    cleanup.append(
        (subscriber.delete_subscription, (), {"subscription": subscription_path})
    )

    # Create a topic.
    publisher.create_topic(name=topic_path)

    # Subscribe to the topic. This must happen before the messages
    # are published.
    subscriber.create_subscription(name=subscription_path, topic=topic_path)

    # Publish some messages.
    futures = [
        publisher.publish(topic_path, b"Wooooo! The claaaaaw!", num=str(index))
        for index in range(2)
    ]

    # Make sure the publish completes.
    for future in futures:
        future.result()

    # We want to make sure that the callback was called asynchronously. So
    # track when each call happened and make sure below.
    callback = TimesCallback(2)

    # Actually open the subscription and hold it open for a few seconds.
    future = subscriber.subscribe(subscription_path, callback)
    for second in range(5):
        time.sleep(4)

        # The callback should have fired at least two times, but it may
        # take some time.
        if callback.calls >= 2:
            first, last = sorted(callback.call_times[:2])
            diff = last - first
            # "Ensure" the first two callbacks were executed asynchronously
            # (sequentially would have resulted in a difference of 2+
            # seconds).
            assert diff.days == 0
            assert diff.seconds < callback.sleep_time

    # Okay, we took too long; fail out.
    assert callback.calls >= 2

    future.cancel()


def test_creating_subscriptions_with_non_default_settings(
    publisher, subscriber, project, topic_path_base, subscription_path_base, cleanup
):
    # Customize topic path to test.
    custom_str = "-creating-subscriptions-with-non-default-settings"
    topic_path = topic_path_base + custom_str
    subscription_path = subscription_path_base + custom_str
    # Make sure the topic and subscription get deleted.
    cleanup.append((publisher.delete_topic, (), {"topic": topic_path}))
    cleanup.append(
        (subscriber.delete_subscription, (), {"subscription": subscription_path})
    )

    # create a topic and a subscription, customize the latter's policy
    publisher.create_topic(name=topic_path)

    request = {
        "name": subscription_path,
        "topic": topic_path,
        "ack_deadline_seconds": 30,
        "retain_acked_messages": True,
        "message_retention_duration": {"seconds": 911},
        "expiration_policy": {"ttl": {"seconds": 90210}},  # 1 day, 3810 seconds
    }
    new_subscription = subscriber.create_subscription(request)

    # fetch the subscription and check its settings
    project_path = f"projects/{project}"
    subscriptions = subscriber.list_subscriptions(project=project_path)

    subscriptions = [sub for sub in subscriptions if sub.topic == topic_path]
    assert len(subscriptions) == 1
    subscription = subscriptions[0]

    assert subscription == new_subscription
    assert subscription.ack_deadline_seconds == 30
    assert subscription.retain_acked_messages
    assert subscription.message_retention_duration.seconds == 911
    assert subscription.expiration_policy.ttl == datetime.timedelta(
        days=1, seconds=3810
    )


def test_listing_project_topics(publisher, project, cleanup):
    topic_paths = [
        publisher.topic_path(project, "topic-{}".format(i) + unique_resource_id("."))
        for i in range(1, 4)
    ]
    for topic in topic_paths:
        cleanup.append((publisher.delete_topic, (), {"topic": topic}))
        publisher.create_topic(name=topic)

    project_path = f"projects/{project}"
    project_topics = publisher.list_topics(project=project_path)
    project_topics = set(t.name for t in project_topics)

    # there might be other topics in the project, thus do a "is subset" check
    assert set(topic_paths) <= project_topics


def test_listing_project_subscriptions(publisher, subscriber, project, cleanup):
    # create topics
    topic_paths = [
        publisher.topic_path(project, "topic-1" + unique_resource_id(".")),
        publisher.topic_path(project, "topic-2" + unique_resource_id(".")),
    ]
    for topic in topic_paths:
        cleanup.append((publisher.delete_topic, (), {"topic": topic}))
        publisher.create_topic(name=topic)

    # create subscriptions
    subscription_paths = [
        subscriber.subscription_path(
            project, "sub-{}".format(i) + unique_resource_id(".")
        )
        for i in range(1, 4)
    ]
    for i, subscription in enumerate(subscription_paths):
        topic = topic_paths[i % 2]
        cleanup.append(
            (subscriber.delete_subscription, (), {"subscription": subscription})
        )
        subscriber.create_subscription(name=subscription, topic=topic)

    # retrieve subscriptions and check that the list matches the expected
    project_path = f"projects/{project}"
    subscriptions = subscriber.list_subscriptions(project=project_path)
    subscriptions = set(s.name for s in subscriptions)

    # there might be other subscriptions in the project, thus do a "is subset" check
    assert set(subscription_paths) <= subscriptions


def test_listing_topic_subscriptions(publisher, subscriber, project, cleanup):
    # create topics
    topic_paths = [
        publisher.topic_path(project, "topic-1" + unique_resource_id(".")),
        publisher.topic_path(project, "topic-2" + unique_resource_id(".")),
    ]
    for topic in topic_paths:
        cleanup.append((publisher.delete_topic, (), {"topic": topic}))
        publisher.create_topic(name=topic)

    # create subscriptions
    subscription_paths = [
        subscriber.subscription_path(
            project, "sub-{}".format(i) + unique_resource_id(".")
        )
        for i in range(1, 4)
    ]
    for i, subscription in enumerate(subscription_paths):
        topic = topic_paths[i % 2]
        cleanup.append(
            (subscriber.delete_subscription, (), {"subscription": subscription})
        )
        subscriber.create_subscription(name=subscription, topic=topic)

    # retrieve subscriptions and check that the list matches the expected
    response = publisher.list_topic_subscriptions(topic=topic_paths[0])
    subscriptions = set(response)

    assert subscriptions == {subscription_paths[0], subscription_paths[2]}


def test_managing_topic_iam_policy(topic_path_base, cleanup):
    publisher = pubsub_v1.PublisherClient(transport="grpc")
    topic_path = topic_path_base + "-managing-topic-iam-policy"
    cleanup.append((publisher.delete_topic, (), {"topic": topic_path}))
    # create a topic and customize its policy
    publisher.create_topic(name=topic_path)
    topic_policy = publisher.get_iam_policy(request={"resource": topic_path})

    topic_policy.bindings.add(role="roles/pubsub.editor", members=["domain:google.com"])
    topic_policy.bindings.add(
        role="roles/pubsub.viewer", members=["group:cloud-logs@google.com"]
    )
    new_policy = publisher.set_iam_policy(
        request={"resource": topic_path, "policy": topic_policy}
    )

    # fetch the topic policy again and check its values
    topic_policy = publisher.get_iam_policy(request={"resource": topic_path})
    assert topic_policy.bindings == new_policy.bindings
    assert len(topic_policy.bindings) == 2

    bindings = sorted(topic_policy.bindings, key=op.attrgetter("role"))
    assert bindings[0].role == "roles/pubsub.editor"
    assert bindings[0].members == ["domain:google.com"]

    assert bindings[1].role == "roles/pubsub.viewer"
    assert bindings[1].members == ["group:cloud-logs@google.com"]


def test_managing_subscription_iam_policy(
    publisher, topic_path_base, subscription_path_base, cleanup
):
    subscriber = pubsub_v1.SubscriberClient(transport="grpc")
    custom_str = "-managing-subscription-iam-policy"
    topic_path = topic_path_base + custom_str
    subscription_path = subscription_path_base + custom_str
    # Make sure the topic and subscription get deleted.
    cleanup.append((publisher.delete_topic, (), {"topic": topic_path}))
    cleanup.append(
        (subscriber.delete_subscription, (), {"subscription": subscription_path})
    )

    # create a topic and a subscription, customize the latter's policy
    publisher.create_topic(name=topic_path)
    subscriber.create_subscription(name=subscription_path, topic=topic_path)
    sub_policy = subscriber.get_iam_policy(request={"resource": subscription_path})

    sub_policy.bindings.add(role="roles/pubsub.editor", members=["domain:google.com"])
    sub_policy.bindings.add(
        role="roles/pubsub.viewer", members=["group:cloud-logs@google.com"]
    )
    new_policy = subscriber.set_iam_policy(
        request={"resource": subscription_path, "policy": sub_policy}
    )

    # fetch the subscription policy again and check its values
    sub_policy = subscriber.get_iam_policy(request={"resource": subscription_path})
    assert sub_policy.bindings == new_policy.bindings
    assert len(sub_policy.bindings) == 2

    bindings = sorted(sub_policy.bindings, key=op.attrgetter("role"))
    assert bindings[0].role == "roles/pubsub.editor"
    assert bindings[0].members == ["domain:google.com"]

    assert bindings[1].role == "roles/pubsub.viewer"
    assert bindings[1].members == ["group:cloud-logs@google.com"]


@pytest.mark.parametrize("transport", ["grpc", "rest"])
def test_subscriber_not_leaking_open_sockets(
    publisher, topic_path_base, subscription_path_base, cleanup, transport
):
    # Make sure the topic and the supscription get deleted.
    # NOTE: Since subscriber client will be closed in the test, we should not
    # use the shared `subscriber` fixture, but instead construct a new client
    # in this test.
    # Also, since the client will get closed, we need another subscriber client
    # to clean up the subscription. We also need to make sure that auxiliary
    # subscriber releases the sockets, too.
    custom_str = "-not-leaking-open-sockets"
    subscription_path = subscription_path_base + custom_str
    topic_path = topic_path_base + custom_str
    subscriber = pubsub_v1.SubscriberClient(transport="grpc")
    subscriber_2 = pubsub_v1.SubscriberClient(transport="grpc")

    # Construct a secondary publisher client to clean up the topic,
    # so we can safely close the main publisher client inside the test.
    if "Rest" in type(publisher._transport).__name__:
        publisher_2 = pubsub_v1.PublisherClient(transport="rest")
    else:
        publisher_2 = pubsub_v1.PublisherClient(transport="grpc")

    cleanup.append(
        (subscriber_2.delete_subscription, (), {"subscription": subscription_path})
    )
    cleanup.append((subscriber_2.close, (), {}))
    cleanup.append((publisher_2.delete_topic, (), {"topic": topic_path}))
    cleanup.append((publisher_2._transport.close, (), {}))

    # Create topic before starting to track connection count (any sockets opened
    # by the publisher client are not counted by this test).
    publisher.create_topic(name=topic_path)

    current_process = psutil.Process()
    conn_count_start = len(current_process.net_connections())

    # Publish a few messages, then synchronously pull them and check that
    # no sockets are leaked.
    with subscriber:
        subscriber.create_subscription(name=subscription_path, topic=topic_path)

        # Publish a few messages, wait for the publish to succeed.
        publish_futures = [
            publisher.publish(topic_path, "message {}".format(i).encode())
            for i in range(1, 4)
        ]
        for future in publish_futures:
            future.result()

        # Synchronously pull messages.
        response = subscriber.pull(subscription=subscription_path, max_messages=3)
        assert len(response.received_messages) == 3

    # Close the publisher client's transport used in the test to ensure all its socket connections
    # (including any opened asynchronously on the background publisher threads) are closed.
    publisher._transport.close()

    # Wait a bit for the asynchronous channel teardown to complete and the socket to be closed.
    for _ in range(30):
        conn_count_end = len(current_process.net_connections())
        if conn_count_end <= conn_count_start:
            break
        time.sleep(0.1)

    # To avoid flakiness, use <= in the assertion, since on rare occasions additional
    # sockets are closed, causing the == assertion to fail.
    # https://github.com/googleapis/python-pubsub/issues/483#issuecomment-910122086
    assert conn_count_end <= conn_count_start


def test_synchronous_pull_no_deadline_error_if_no_messages(
    publisher, topic_path_base, subscriber, subscription_path_base, cleanup
):
    custom_str = "-synchronous-pull-deadline-error-if-no-messages"
    topic_path = topic_path_base + custom_str
    subscription_path = subscription_path_base + custom_str
    # Make sure the topic and subscription get deleted.
    cleanup.append((publisher.delete_topic, (), {"topic": topic_path}))
    cleanup.append(
        (subscriber.delete_subscription, (), {"subscription": subscription_path})
    )

    # Create a topic and subscribe to it.
    publisher.create_topic(name=topic_path)
    subscriber.create_subscription(name=subscription_path, topic=topic_path)

    try:
        response = subscriber.pull(subscription=subscription_path, max_messages=2)
    except core_exceptions.DeadlineExceeded:
        pytest.fail(
            "Unexpected DeadlineExceeded error on synchronous pull when no "
            "messages published to the topic."
        )
    else:
        assert list(response.received_messages) == []


class TestStreamingPull(object):
    def test_streaming_pull_callback_error_propagation(
        self, publisher, topic_path_base, subscription_path_base, cleanup
    ):
        subscriber = pubsub_v1.SubscriberClient(transport="grpc")
        custom_str = "-streaming-pull-callback-error-propagation"
        topic_path = topic_path_base + custom_str
        subscription_path = subscription_path_base + custom_str
        # Make sure the topic and subscription get deleted.
        cleanup.append((publisher.delete_topic, (), {"topic": topic_path}))
        cleanup.append(
            (subscriber.delete_subscription, (), {"subscription": subscription_path})
        )

        # create a topic and subscribe to it
        publisher.create_topic(name=topic_path)
        subscriber.create_subscription(name=subscription_path, topic=topic_path)

        # publish a messages and wait until published
        future = publisher.publish(topic_path, b"hello!")
        future.result(timeout=30)

        # Now subscribe to the topic and verify that an error in the callback
        # is propagated through the streaming pull future.
        class CallbackError(Exception):
            pass

        callback = mock.Mock(side_effect=CallbackError)
        future = subscriber.subscribe(subscription_path, callback)

        with pytest.raises(CallbackError):
            future.result(timeout=30)

    @typed_flaky
    def test_streaming_pull_ack_deadline(
        self,
        publisher,
        project,
        topic_path_base,
        subscription_path_base,
        cleanup,
    ):
        subscriber = pubsub_v1.SubscriberClient(transport="grpc")
        custom_str = "-streaming-pull-ack-deadline"
        topic_path = topic_path_base + custom_str
        subscription_path = subscription_path_base + custom_str
        # Make sure the topic and subscription get deleted.
        cleanup.append((publisher.delete_topic, (), {"topic": topic_path}))
        cleanup.append(
            (subscriber.delete_subscription, (), {"subscription": subscription_path})
        )

        # Create a topic and a subscription, then subscribe to the topic. This
        # must happen before the messages are published.
        publisher.create_topic(name=topic_path)

        # Subscribe to the topic. This must happen before the messages
        # are published.
        subscriber.create_subscription(
            name=subscription_path, topic=topic_path, ack_deadline_seconds=45
        )

        # publish some messages and wait for completion
        _publish_messages(publisher, topic_path, batch_sizes=[2])

        # subscribe to the topic
        callback = StreamingPullCallback(
            processing_time=13,  # more than the default stream ACK deadline (10s)
            resolve_at_msg_count=3,  # one more than the published messages count
        )
        flow_control = types.FlowControl(max_messages=1)
        subscription_future = subscriber.subscribe(
            subscription_path, callback, flow_control=flow_control
        )

        # We expect to process the first two messages in 2 * 13 seconds, and
        # any duplicate message that is re-sent by the backend in additional
        # 13 seconds, totalling 39 seconds (+ overhead) --> if there have been
        # no duplicates in 60 seconds, we can reasonably assume that there
        # won't be any.
        try:
            callback.done_future.result(timeout=60)
        except exceptions.TimeoutError:
            # future timed out, because we received no excessive messages
            assert sorted(callback.seen_message_ids) == [1, 2]
        else:
            pytest.fail(
                "Expected to receive 2 messages, but got at least {}.".format(
                    len(callback.seen_message_ids)
                )
            )
        finally:
            subscription_future.cancel()

    @typed_flaky
    def test_streaming_pull_max_messages(
        self, publisher, topic_path_base, subscription_path_base, cleanup
    ):
        subscriber = pubsub_v1.SubscriberClient(transport="grpc")
        custom_str = "-streaming-pull-max-messages"
        topic_path = topic_path_base + custom_str
        subscription_path = subscription_path_base + custom_str
        # Make sure the topic and subscription get deleted.
        cleanup.append((publisher.delete_topic, (), {"topic": topic_path}))
        cleanup.append(
            (subscriber.delete_subscription, (), {"subscription": subscription_path})
        )

        # create a topic and subscribe to it
        publisher.create_topic(name=topic_path)
        subscriber.create_subscription(name=subscription_path, topic=topic_path)

        batch_sizes = (7, 4, 8, 2, 10, 1, 3, 8, 6, 1)  # total: 50
        _publish_messages(publisher, topic_path, batch_sizes=batch_sizes)

        # now subscribe and do the main part, check for max pending messages
        total_messages = sum(batch_sizes)
        flow_control = types.FlowControl(max_messages=5)
        callback = StreamingPullCallback(
            processing_time=1, resolve_at_msg_count=total_messages
        )

        subscription_future = subscriber.subscribe(
            subscription_path, callback, flow_control=flow_control
        )

        # Expected time to process all messages in ideal case:
        #     (total_messages / FlowControl.max_messages) * processing_time
        #
        # With total=50, max messages=5, and processing_time=1 this amounts to
        # 10 seconds (+ overhead), thus a full minute should be more than enough
        # for the processing to complete. If not, fail the test with a timeout.
        try:
            callback.done_future.result(timeout=60)
        except exceptions.TimeoutError:
            pytest.fail(
                "Timeout: receiving/processing streamed messages took too long."
            )

        # The callback future gets resolved once total_messages have been processed,
        # but we want to wait for just a little bit longer to possibly catch cases
        # when the callback gets invoked *more* than total_messages times.
        time.sleep(3)

        try:
            # All messages should have been processed exactly once, and no more
            # than max_messages simultaneously at any time.
            assert callback.completed_calls == total_messages
            assert sorted(callback.seen_message_ids) == list(
                range(1, total_messages + 1)
            )
            assert callback.max_pending_ack <= flow_control.max_messages
        finally:
            subscription_future.cancel()  # trigger clean shutdown

    @typed_flaky
    def test_streaming_pull_blocking_shutdown(
        self, publisher, topic_path_base, subscription_path_base, cleanup
    ):
        subscriber = pubsub_v1.SubscriberClient(transport="grpc")
        custom_str = "-streaming-pull-blocking-shutdown"
        topic_path = topic_path_base + custom_str
        subscription_path = subscription_path_base + custom_str
        # Make sure the topic and subscription get deleted.
        cleanup.append((publisher.delete_topic, (), {"topic": topic_path}))
        cleanup.append(
            (subscriber.delete_subscription, (), {"subscription": subscription_path})
        )

        # The ACK-s are only persisted if *all* messages published in the same batch
        # are ACK-ed. We thus publish each message in its own batch so that the backend
        # treats all messages' ACKs independently of each other.
        publisher.create_topic(name=topic_path)
        subscriber.create_subscription(name=subscription_path, topic=topic_path)
        _publish_messages(publisher, topic_path, batch_sizes=[1] * 10)

        # Artificially delay message processing, gracefully shutdown the streaming pull
        # in the meantime, then verify that those messages were nevertheless processed.
        processed_messages = []

        def callback(message):
            time.sleep(15)
            processed_messages.append(message.data)
            message.ack()

        # Flow control limits should exceed the number of worker threads, so that some
        # of the messages will be blocked on waiting for free scheduler threads.
        flow_control = pubsub_v1.types.FlowControl(max_messages=5)
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=3)
        scheduler = pubsub_v1.subscriber.scheduler.ThreadScheduler(executor=executor)
        subscription_future = subscriber.subscribe(
            subscription_path,
            callback=callback,
            flow_control=flow_control,
            scheduler=scheduler,
            await_callbacks_on_shutdown=True,
        )

        try:
            subscription_future.result(timeout=10)  # less than the sleep in callback
        except exceptions.TimeoutError:
            subscription_future.cancel()
            subscription_future.result()  # block until shutdown completes

        # Blocking om shutdown should have waited for the already executing
        # callbacks to finish.
        assert len(processed_messages) == 3

        # The messages that were not processed should have been NACK-ed and we should
        # receive them again quite soon.
        all_done = threading.Barrier(7 + 1, timeout=5)  # +1 because of the main thread
        remaining = []

        def callback2(message):
            remaining.append(message.data)
            message.ack()
            all_done.wait()

        subscription_future = subscriber.subscribe(
            subscription_path, callback=callback2, await_callbacks_on_shutdown=False
        )

        try:
            all_done.wait()
        except threading.BrokenBarrierError:  # PRAGMA: no cover
            pytest.fail("The remaining messages have not been re-delivered in time.")
        finally:
            subscription_future.cancel()
            subscription_future.result()  # block until shutdown completes

        # There should be 7 messages left that were not yet processed and none of them
        # should be a message that should have already been sucessfully processed in the
        # first streaming pull.
        assert len(remaining) == 7
        assert not (set(processed_messages) & set(remaining))  # no re-delivery


@pytest.mark.skipif(
    "KOKORO_GFILE_DIR" not in os.environ,
    reason="Requires Kokoro environment with a service account with limited role.",
)
class TestBasicRBAC(object):
    def test_streaming_pull_subscriber_permissions_sufficient(
        self, publisher, topic_path_base, subscription_path_base, cleanup
    ):
        subscriber = pubsub_v1.SubscriberClient(transport="grpc")
        custom_str = "-streaming-pull-subscriber-permissions-sufficient"
        topic_path = topic_path_base + custom_str
        subscription_path = subscription_path_base + custom_str
        # Make sure the topic and subscription get deleted.
        cleanup.append((publisher.delete_topic, (), {"topic": topic_path}))
        cleanup.append(
            (subscriber.delete_subscription, (), {"subscription": subscription_path})
        )

        # create a topic and subscribe to it
        publisher.create_topic(name=topic_path)
        subscriber.create_subscription(name=subscription_path, topic=topic_path)

        # A service account granting only the pubsub.subscriber role must be used.
        filename = os.path.join(
            os.environ["KOKORO_GFILE_DIR"], "pubsub-subscriber-service-account.json"
        )
        streaming_pull_subscriber = type(subscriber).from_service_account_file(filename)

        # Subscribe to the topic, publish a message, and verify that subscriber
        # successfully pulls and processes it.
        callback = StreamingPullCallback(processing_time=0.01, resolve_at_msg_count=1)
        future = streaming_pull_subscriber.subscribe(subscription_path, callback)
        _publish_messages(publisher, topic_path, batch_sizes=[1])

        try:
            callback.done_future.result(timeout=10)
        except exceptions.TimeoutError:
            pytest.fail(
                "Timeout: receiving/processing streamed messages took too long."
            )
        else:
            assert 1 in callback.seen_message_ids
        finally:
            future.cancel()

    def test_publisher_role_can_publish_messages(
        self, publisher, topic_path_base, subscriber, subscription_path_base, cleanup
    ):
        custom_str = "-publisher-role-can-publish-messages"
        topic_path = topic_path_base + custom_str
        subscription_path = subscription_path_base + custom_str
        # Make sure the topic and subscription get deleted.
        cleanup.append((publisher.delete_topic, (), {"topic": topic_path}))
        cleanup.append(
            (subscriber.delete_subscription, (), {"subscription": subscription_path})
        )

        # Create a topic and subscribe to it.
        publisher.create_topic(name=topic_path)
        subscriber.create_subscription(name=subscription_path, topic=topic_path)

        # Create a publisher client with only the publisher role only.
        filename = os.path.join(
            os.environ["KOKORO_GFILE_DIR"], "pubsub-publisher-service-account.json"
        )
        publisher_only_client = type(publisher).from_service_account_file(filename)

        _publish_messages(publisher_only_client, topic_path, batch_sizes=[2])

        response = subscriber.pull(subscription=subscription_path, max_messages=2)
        assert len(response.received_messages) == 2

    @pytest.mark.skip(
        "Snapshot creation is not instant on the backend, causing test falkiness."
    )
    def test_snapshot_seek_subscriber_permissions_sufficient(
        self,
        project,
        publisher,
        topic_path_base,
        subscriber,
        subscription_path_base,
        cleanup,
    ):
        custom_str = "-snapshot-seek-subscriber-permissions-sufficient"
        topic_path = topic_path_base + custom_str
        subscription_path = subscription_path_base + custom_str
        snapshot_name = "snap" + unique_resource_id("-")
        snapshot_path = "projects/{}/snapshots/{}".format(project, snapshot_name)

        # Make sure the topic and subscription get deleted.
        cleanup.append((publisher.delete_topic, (), {"topic": topic_path}))
        cleanup.append(
            (subscriber.delete_subscription, (), {"subscription": subscription_path})
        )
        cleanup.append((subscriber.delete_snapshot, (), {"snapshot": snapshot_path}))

        # Create a topic and subscribe to it.
        publisher.create_topic(name=topic_path)
        subscriber.create_subscription(
            name=subscription_path, topic=topic_path, retain_acked_messages=True
        )

        # A service account granting only the pubsub.subscriber role must be used.
        filename = os.path.join(
            os.environ["KOKORO_GFILE_DIR"], "pubsub-subscriber-service-account.json"
        )
        subscriber_only_client = type(subscriber).from_service_account_file(filename)

        # Publish two messages and create a snapshot inbetween.
        _publish_messages(publisher, topic_path, batch_sizes=[1])
        response = subscriber.pull(subscription=subscription_path, max_messages=10)
        assert len(response.received_messages) == 1

        subscriber.create_snapshot(name=snapshot_path, subscription=subscription_path)

        _publish_messages(publisher, topic_path, batch_sizes=[1])
        response = subscriber.pull(subscription=subscription_path, max_messages=10)
        assert len(response.received_messages) == 1

        # A subscriber-only client should be allowed to seek to a snapshot.
        seek_request = gapic_types.SeekRequest(
            subscription=subscription_path, snapshot=snapshot_path
        )
        subscriber_only_client.seek(seek_request)

        # We should receive one message again, since we sought back to a snapshot.
        response = subscriber.pull(subscription=subscription_path, max_messages=10)
        assert len(response.received_messages) == 1

    def test_viewer_role_can_list_resources(
        self, project, publisher, topic_path_base, subscriber, cleanup
    ):
        project_path = "projects/" + project
        topic_path = topic_path_base + "-viewer-role-can-list-resources"
        # Make sure the created topic gets deleted.
        cleanup.append((publisher.delete_topic, (), {"topic": topic_path}))

        publisher.create_topic(name=topic_path)

        # A service account granting only the pubsub.viewer role must be used.
        filename = os.path.join(
            os.environ["KOKORO_GFILE_DIR"], "pubsub-viewer-service-account.json"
        )
        viewer_only_subscriber = type(subscriber).from_service_account_file(filename)
        viewer_only_publisher = type(publisher).from_service_account_file(filename)

        # The following operations should not raise permission denied errors.
        # NOTE: At least one topic exists.
        topic = next(iter(viewer_only_publisher.list_topics(project=project_path)))

        next(
            iter(viewer_only_publisher.list_topic_subscriptions(topic=topic.name)), None
        )

        next(
            iter(viewer_only_subscriber.list_subscriptions(project=project_path)), None
        )

        next(iter(viewer_only_subscriber.list_snapshots(project=project_path)), None)

    def test_editor_role_can_create_resources(
        self,
        project,
        publisher,
        topic_path_base,
        subscriber,
        subscription_path_base,
        cleanup,
    ):
        custom_str = "-editor-role-can-create-resources"
        topic_path = topic_path_base + custom_str
        subscription_path = subscription_path_base + custom_str
        snapshot_name = "snap" + unique_resource_id("-")
        snapshot_path = "projects/{}/snapshots/{}".format(project, snapshot_name)

        # Make sure the created resources get deleted.
        cleanup.append((subscriber.delete_snapshot, (), {"snapshot": snapshot_path}))
        cleanup.append(
            (subscriber.delete_subscription, (), {"subscription": subscription_path})
        )
        cleanup.append((publisher.delete_topic, (), {"topic": topic_path}))

        # A service account granting only the pubsub.editor role must be used.
        filename = os.path.join(
            os.environ["KOKORO_GFILE_DIR"], "pubsub-editor-service-account.json"
        )
        editor_subscriber = type(subscriber).from_service_account_file(filename)
        editor_publisher = type(publisher).from_service_account_file(filename)

        # The following operations should not raise permission denied errors.
        editor_publisher.create_topic(name=topic_path)
        editor_subscriber.create_subscription(name=subscription_path, topic=topic_path)
        editor_subscriber.create_snapshot(
            name=snapshot_path, subscription=subscription_path
        )


def _publish_messages(publisher, topic_path, batch_sizes):
    """Publish ``count`` messages in batches and wait until completion."""
    publish_futures = []
    msg_counter = itertools.count(start=1)

    for batch_num, batch_size in enumerate(batch_sizes, start=1):
        msg_batch = _make_messages(count=batch_size, batch_num=batch_num)
        for msg in msg_batch:
            future = publisher.publish(topic_path, msg, seq_num=str(next(msg_counter)))
            publish_futures.append(future)
        time.sleep(0.1)

    # wait untill all messages have been successfully published
    for future in publish_futures:
        future.result(timeout=30)


def _make_messages(count, batch_num):
    messages = [
        f"message {i}/{count} of batch {batch_num}".encode("utf-8")
        for i in range(1, count + 1)
    ]
    return messages


class AckCallback(object):
    def __init__(self):
        self.calls = 0
        self.lock = threading.Lock()

    def __call__(self, message):
        message.ack()
        # Only increment the number of calls **after** finishing.
        with self.lock:
            self.calls += 1


class TimesCallback(object):
    def __init__(self, sleep_time):
        self.sleep_time = sleep_time
        self.calls = 0
        self.call_times = []
        self.lock = threading.Lock()

    def __call__(self, message):
        now = datetime.datetime.now()
        time.sleep(self.sleep_time)
        message.ack()
        # Only increment the number of calls **after** finishing.
        with self.lock:
            # list.append() is thread-safe, but we still wait until
            # ``calls`` is incremented to do it.
            self.call_times.append(now)
            self.calls += 1


class StreamingPullCallback(object):
    def __init__(self, processing_time, resolve_at_msg_count):
        self._lock = threading.Lock()
        self._processing_time = processing_time
        self._pending_ack = 0
        self.max_pending_ack = 0
        self.completed_calls = 0
        self.seen_message_ids = []

        self._resolve_at_msg_count = resolve_at_msg_count
        self.done_future = futures.Future()

    def __call__(self, message):
        with self._lock:
            self._pending_ack += 1
            self.max_pending_ack = max(self.max_pending_ack, self._pending_ack)
            self.seen_message_ids.append(int(message.attributes["seq_num"]))

        time.sleep(self._processing_time)

        with self._lock:
            self._pending_ack -= 1
            message.ack()
            self.completed_calls += 1

            if self.completed_calls >= self._resolve_at_msg_count:
                if not self.done_future.done():
                    self.done_future.set_result(None)
