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

import pytest

from google.cloud.pubsub_v1.open_telemetry.publish_message_wrapper import (
    PublishMessageWrapper,
)
from google.pubsub_v1 import types as gapic_types


def test_message_setter():
    wrapper = PublishMessageWrapper(message=gapic_types.PubsubMessage(data=b"foo"))
    another_message = gapic_types.PubsubMessage(data=b"bar")
    wrapper.message = another_message

    assert wrapper.message == another_message


def test_eq():
    wrapper1 = PublishMessageWrapper(message=gapic_types.PubsubMessage(data=b"foo"))
    wrapper2 = PublishMessageWrapper(message=gapic_types.PubsubMessage(data=b"bar"))
    wrapper3 = PublishMessageWrapper(message=gapic_types.PubsubMessage(data=b"foo"))

    assert wrapper1.__eq__(wrapper2) is False
    assert wrapper1.__eq__(wrapper3) is True


def test_end_create_span():
    wrapper = PublishMessageWrapper(message=gapic_types.PubsubMessage(data=b"foo"))
    with pytest.raises(AssertionError):
        wrapper.end_create_span()


def test_end_publisher_flow_control_span():
    wrapper = PublishMessageWrapper(message=gapic_types.PubsubMessage(data=b"foo"))
    with pytest.raises(AssertionError):
        wrapper.end_publisher_flow_control_span()


def test_end_publisher_batching_span():
    wrapper = PublishMessageWrapper(message=gapic_types.PubsubMessage(data=b"foo"))
    with pytest.raises(AssertionError):
        wrapper.end_publisher_batching_span()
