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
    package="google.cloud.securitycenter.v2",
    manifest={
        "IamBinding",
    },
)


class IamBinding(proto.Message):
    r"""Represents a particular IAM binding, which captures a
    member's role addition, removal, or state.

    Attributes:
        action (google.cloud.securitycenter_v2.types.IamBinding.Action):
            The action that was performed on a Binding.
        role (str):
            Role that is assigned to "members".
            For example, "roles/viewer", "roles/editor", or
            "roles/owner".
        member (str):
            A single identity requesting access for a
            Cloud Platform resource, for example,
            "foo@google.com".
    """

    class Action(proto.Enum):
        r"""The type of action performed on a Binding in a policy.

        Values:
            ACTION_UNSPECIFIED (0):
                Unspecified.
            ADD (1):
                Addition of a Binding.
            REMOVE (2):
                Removal of a Binding.
        """

        ACTION_UNSPECIFIED = 0
        ADD = 1
        REMOVE = 2

    action: Action = proto.Field(
        proto.ENUM,
        number=1,
        enum=Action,
    )
    role: str = proto.Field(
        proto.STRING,
        number=2,
    )
    member: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
