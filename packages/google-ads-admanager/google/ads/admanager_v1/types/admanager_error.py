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

import google.protobuf.any_pb2 as any_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "AdManagerError",
    },
)


class AdManagerError(proto.Message):
    r"""/ AdManagerError contains all the information required for
    processing a / particular error thrown by the AdManager API. /
    / At least one AdManagerError should be included in all error
    messages sent to / the client.

    Attributes:
        error_code (str):
            The unique identifying string for this error.
        message (str):
            A publisher appropriate explanation of this
            error.
        field_path (str):
            The field path that triggered this error.
        trigger (str):
            The value that triggered this error.
        stack_trace (str):
            The stack trace that accompanies this error.
        details (MutableSequence[google.protobuf.any_pb2.Any]):
            A list of messages that carry any additional
            error details.
    """

    error_code: str = proto.Field(
        proto.STRING,
        number=1,
    )
    message: str = proto.Field(
        proto.STRING,
        number=2,
    )
    field_path: str = proto.Field(
        proto.STRING,
        number=3,
    )
    trigger: str = proto.Field(
        proto.STRING,
        number=4,
    )
    stack_trace: str = proto.Field(
        proto.STRING,
        number=5,
    )
    details: MutableSequence[any_pb2.Any] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=any_pb2.Any,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
