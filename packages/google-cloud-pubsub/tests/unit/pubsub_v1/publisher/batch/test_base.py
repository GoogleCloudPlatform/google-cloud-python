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

from google.auth import credentials

from google.cloud.pubsub_v1 import publisher, types
from google.cloud.pubsub_v1.open_telemetry.publish_message_wrapper import (
    PublishMessageWrapper,
)
from google.cloud.pubsub_v1.publisher._batch.base import BatchStatus
from google.cloud.pubsub_v1.publisher._batch.thread import Batch
from google.pubsub_v1 import types as gapic_types


def create_batch(status, settings=types.BatchSettings()):
    """Create a batch object, which does not commit.

    Args:
        status (str): The batch's internal status will be set to the provided status.

    Returns:
        ~.pubsub_v1.publisher.batch.thread.Batch: The batch object
    """
    client = publisher.Client(credentials=credentials.AnonymousCredentials())
    batch = Batch(client, "topic_name", settings)
    batch._status = status
    return batch


def test_len():
    batch = create_batch(status=BatchStatus.ACCEPTING_MESSAGES)
    assert len(batch) == 0
    batch.publish(PublishMessageWrapper(message=gapic_types.PubsubMessage(data=b"foo")))
    assert len(batch) == 1
