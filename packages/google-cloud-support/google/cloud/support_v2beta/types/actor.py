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
    package="google.cloud.support.v2beta",
    manifest={
        "Actor",
    },
)


class Actor(proto.Message):
    r"""An Actor represents an entity that performed an action. For
    example, an actor could be a user who posted a comment on a
    support case, a user who uploaded an attachment, or a service
    account that created a support case.

    Attributes:
        display_name (str):
            The name to display for the actor. If not
            provided, it is inferred from credentials
            supplied during case creation. When an email is
            provided, a display name must also be provided.
            This will be obfuscated if the user is a Google
            Support agent.
        email (str):
            The email address of the actor. If not provided, it is
            inferred from the credentials supplied during case creation.
            When a name is provided, an email must also be provided. If
            the user is a Google Support agent, this is obfuscated.

            This field is deprecated. Use ``username`` instead.
        google_support (bool):
            Output only. Whether the actor is a Google
            support actor.
        username (str):
            Output only. The username of the actor. It
            may look like an email or other format provided
            by the identity provider. If not provided, it is
            inferred from the credentials supplied. When a
            name is provided, a username must also be
            provided. If the user is a Google Support agent,
            this will not be set.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    email: str = proto.Field(
        proto.STRING,
        number=2,
    )
    google_support: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    username: str = proto.Field(
        proto.STRING,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
