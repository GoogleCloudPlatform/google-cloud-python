# Copyright 2019, Google LLC All rights reserved.
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

import concurrent.futures as futures
from unittest import mock

import pytest
from google.auth import credentials

from google.cloud.pubsub_v1 import publisher
from google.cloud.pubsub_v1.open_telemetry.publish_message_wrapper import (
    PublishMessageWrapper,
)
from google.cloud.pubsub_v1.publisher._sequencer import ordered_sequencer
from google.pubsub_v1 import types as gapic_types

_ORDERING_KEY = "ordering_key_1"


def create_message():
    return PublishMessageWrapper(
        message=gapic_types.PubsubMessage(data=b"foo", attributes={"bar": "baz"})
    )


def create_client():
    return publisher.Client(credentials=credentials.AnonymousCredentials())


def create_ordered_sequencer(client):
    return ordered_sequencer.OrderedSequencer(client, "topic_name", _ORDERING_KEY)


def test_stop_makes_sequencer_invalid():
    client = create_client()
    message = create_message()

    sequencer = create_ordered_sequencer(client)

    sequencer.stop()

    # Publish after stop() throws
    with pytest.raises(RuntimeError):
        sequencer.publish(message)

    # Commit after stop() throws
    with pytest.raises(RuntimeError):
        sequencer.commit()

    # Stop after stop() throws
    with pytest.raises(RuntimeError):
        sequencer.stop()


def test_stop_no_batches():
    client = create_client()

    sequencer = create_ordered_sequencer(client)

    # No exceptions thrown if there are no batches.
    sequencer.stop()


def test_stop_one_batch():
    client = create_client()

    sequencer = create_ordered_sequencer(client)

    batch1 = mock.Mock(spec=client._batch_class)
    sequencer._set_batches([batch1])

    sequencer.stop()

    # Assert that the first batch is committed.
    assert batch1.commit.call_count == 1
    assert batch1.cancel.call_count == 0


def test_stop_many_batches():
    client = create_client()

    sequencer = create_ordered_sequencer(client)

    batch1 = mock.Mock(spec=client._batch_class)
    batch2 = mock.Mock(spec=client._batch_class)
    sequencer._set_batches([batch1, batch2])

    sequencer.stop()

    # Assert that the first batch is committed and the rest cancelled.
    assert batch1.commit.call_count == 1
    assert batch1.cancel.call_count == 0
    assert batch2.commit.call_count == 0
    assert batch2.cancel.call_count == 1


def test_commit():
    client = create_client()

    sequencer = create_ordered_sequencer(client)

    batch1 = mock.Mock(spec=client._batch_class)
    batch2 = mock.Mock(spec=client._batch_class)
    sequencer._set_batches([batch1, batch2])

    sequencer.commit()
    # Only commit the first batch.
    assert batch1.commit.call_count == 1
    assert batch2.commit.call_count == 0


def test_commit_empty_batch_list():
    client = create_client()

    sequencer = create_ordered_sequencer(client)

    # Test nothing bad happens.
    sequencer.commit()


def test_no_commit_when_paused():
    client = create_client()
    batch = mock.Mock(spec=client._batch_class)

    sequencer = create_ordered_sequencer(client)
    sequencer._set_batch(batch)

    sequencer._pause()

    sequencer.commit()
    assert batch.commit.call_count == 0


def test_pause_and_unpause():
    client = create_client()
    message = create_message()
    sequencer = create_ordered_sequencer(client)

    # Unpausing without pausing throws.
    with pytest.raises(RuntimeError):
        sequencer.unpause()

    sequencer._pause()

    # Publishing while paused returns a future with an exception.
    future = sequencer.publish(message)
    assert future.exception().ordering_key == _ORDERING_KEY

    sequencer.unpause()

    # Assert publish does not set exception after unpause().
    future = sequencer.publish(message)
    with pytest.raises(futures._base.TimeoutError):
        future.exception(timeout=0)


def test_basic_publish():
    client = create_client()
    message = create_message()
    batch = mock.Mock(spec=client._batch_class)

    sequencer = create_ordered_sequencer(client)
    sequencer._set_batch(batch)

    sequencer.publish(message)
    batch.publish.assert_called_once_with(message)


def test_publish_custom_retry():
    client = create_client()
    message = create_message()
    sequencer = create_ordered_sequencer(client)

    sequencer.publish(message, retry=mock.sentinel.custom_retry)

    assert sequencer._ordered_batches  # batch exists
    batch = sequencer._ordered_batches[0]
    assert batch._commit_retry is mock.sentinel.custom_retry


def test_publish_custom_timeout():
    client = create_client()
    message = create_message()
    sequencer = create_ordered_sequencer(client)

    sequencer.publish(message, timeout=mock.sentinel.custom_timeout)

    assert sequencer._ordered_batches  # batch exists
    batch = sequencer._ordered_batches[0]
    assert batch._commit_timeout is mock.sentinel.custom_timeout


def test_publish_batch_full():
    client = create_client()
    message = create_message()
    batch = mock.Mock(spec=client._batch_class)
    # Make batch full.
    batch.publish.return_value = None

    sequencer = create_ordered_sequencer(client)
    sequencer._set_batch(batch)

    # Will create a new batch since the old one is full, and return a future.
    future = sequencer.publish(message)
    batch.publish.assert_called_once_with(message)
    assert future is not None

    # There's now the old and the new batches.
    assert len(sequencer._get_batches()) == 2


def test_batch_done_successfully():
    client = create_client()
    batch = mock.Mock(spec=client._batch_class)

    sequencer = ordered_sequencer.OrderedSequencer(client, "topic_name", _ORDERING_KEY)
    sequencer._set_batch(batch)

    sequencer._batch_done_callback(success=True)

    # One batch is done, so the OrderedSequencer has no more work, and should
    # return true for is_finished().
    assert sequencer.is_finished()

    # No batches remain in the batches list.
    assert len(sequencer._get_batches()) == 0


def test_batch_done_successfully_one_batch_remains():
    client = create_client()
    batch1 = mock.Mock(spec=client._batch_class)
    batch2 = mock.Mock(spec=client._batch_class)

    sequencer = ordered_sequencer.OrderedSequencer(client, "topic_name", _ORDERING_KEY)
    sequencer._set_batches([batch1, batch2])

    sequencer._batch_done_callback(success=True)

    # One batch is done, but the OrderedSequencer has more work, so is_finished()
    # should return false.
    assert not sequencer.is_finished()

    # Second batch should be not be committed since the it may still be able to
    # accept messages.
    assert batch2.commit.call_count == 0

    # Only the second batch remains in the batches list.
    assert len(sequencer._get_batches()) == 1


def test_batch_done_successfully_many_batches_remain():
    client = create_client()
    batch1 = mock.Mock(spec=client._batch_class)
    batch2 = mock.Mock(spec=client._batch_class)
    batch3 = mock.Mock(spec=client._batch_class)

    sequencer = ordered_sequencer.OrderedSequencer(client, "topic_name", _ORDERING_KEY)
    sequencer._set_batches([batch1, batch2, batch3])

    sequencer._batch_done_callback(success=True)

    # One batch is done, but the OrderedSequencer has more work, so DO NOT
    # return true for is_finished().
    assert not sequencer.is_finished()

    # Second batch should be committed since it is full. We know it's full
    # because there exists a third batch. Batches are created only if the
    # previous one can't accept messages any more / is full.
    assert batch2.commit.call_count == 1

    # Both the second and third batches remain in the batches list.
    assert len(sequencer._get_batches()) == 2


def test_batch_done_unsuccessfully():
    client = create_client()
    message = create_message()
    batch1 = mock.Mock(spec=client._batch_class)
    batch2 = mock.Mock(spec=client._batch_class)
    batch3 = mock.Mock(spec=client._batch_class)

    sequencer = ordered_sequencer.OrderedSequencer(client, "topic_name", _ORDERING_KEY)
    sequencer._set_batches([batch1, batch2, batch3])

    # Make the batch fail.
    sequencer._batch_done_callback(success=False)

    # Sequencer should remain as a sentinel to indicate this ordering key is
    # paused. Therefore, don't call the cleanup callback.
    assert not sequencer.is_finished()

    # Cancel the remaining batches.
    assert batch2.cancel.call_count == 1
    assert batch3.cancel.call_count == 1

    # Remove all the batches.
    assert len(sequencer._get_batches()) == 0

    # Verify that the sequencer is paused. Publishing while paused returns a
    # future with an exception.
    future = sequencer.publish(message)
    assert future.exception().ordering_key == _ORDERING_KEY


def test_publish_after_finish():
    client = create_client()
    batch = mock.Mock(spec=client._batch_class)

    sequencer = ordered_sequencer.OrderedSequencer(client, "topic_name", _ORDERING_KEY)
    sequencer._set_batch(batch)

    sequencer._batch_done_callback(success=True)

    # One batch is done, so the OrderedSequencer has no more work, and should
    # return true for is_finished().
    assert sequencer.is_finished()

    message = create_message()
    # It's legal to publish after being finished.
    sequencer.publish(message)

    # Go back to accepting-messages mode.
    assert not sequencer.is_finished()
