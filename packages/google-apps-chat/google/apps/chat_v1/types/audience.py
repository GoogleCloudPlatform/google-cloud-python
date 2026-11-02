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
    package="google.chat.v1",
    manifest={
        "Audience",
    },
)


class Audience(proto.Message):
    r"""A target audience in Google Chat. A target audience represents a
    group of users within a Google Workspace organization, defined by an
    administrator. Target audiences are used to configure access and
    visibility settings for resources, such as making a space
    discoverable to a specific group of users.

    For more details, see `Target
    audiences <https://support.google.com/a/answer/9934697>`__ and `Make
    a space discoverable to a target
    audience <https://developers.google.com/workspace/chat/space-target-audience>`__.

    Attributes:
        name (str):
            The resource name of the `target
            audience <https://support.google.com/a/answer/9934697>`__
            who can discover or join the space. For details, see `Make a
            space discoverable to a target
            audience <https://developers.google.com/workspace/chat/space-target-audience>`__.
            Format: ``audiences/{audience}``

            To use the default target audience for the Google Workspace
            organization, set to ``audiences/default``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
