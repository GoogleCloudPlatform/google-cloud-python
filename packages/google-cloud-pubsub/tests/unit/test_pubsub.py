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

from google.cloud import pubsub, pubsub_v1


def test_exported_things():
    assert pubsub.PublisherClient is pubsub_v1.PublisherClient
    assert pubsub.SubscriberClient is pubsub_v1.SubscriberClient
    assert pubsub.types is pubsub_v1.types
