# -*- coding: utf-8 -*-
# Copyright 2026 Google LLC
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
#
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.batch.v1alpha",
    manifest={
        "Notification",
    },
)


class Notification(proto.Message):
    r"""Notification on resource state change.

    Attributes:
        pubsub_topic (str):
            Required. The Pub/Sub topic where notifications like the
            resource allowance state changes will be published. The
            topic must exist in the same project as the job and billings
            will be charged to this project. If not specified, no
            Pub/Sub messages will be sent. Topic format:
            ``projects/{project}/topics/{topic}``.
    """

    pubsub_topic: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
