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
    package="google.firestore.v1",
    manifest={
        "ExplainStats",
    },
)


class ExplainStats(proto.Message):
    r"""Pipeline explain stats.

    Depending on the explain options in the original request, this
    can contain the optimized plan and / or execution stats.

    Attributes:
        data (google.protobuf.any_pb2.Any):
            The format depends on the ``output_format`` options in the
            request.

            Currently there are two supported options: ``TEXT`` and
            ``JSON``. Both supply a ``google.protobuf.StringValue``.
    """

    data: any_pb2.Any = proto.Field(
        proto.MESSAGE,
        number=1,
        message=any_pb2.Any,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
