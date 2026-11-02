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

import google.protobuf.any_pb2 as any_pb2  # type: ignore
import google.rpc.code_pb2 as code_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.showcase.v1beta1',
    manifest={
        'RestError',
    },
)


class RestError(proto.Message):
    r"""HTTP/JSON error representation as defined in
    https://google.aip.dev/193#http11json-representation,

    Attributes:
        error (google.showcase_v1beta1.types.RestError.Status):

    """

    class Status(proto.Message):
        r"""

        Attributes:
            code (int):
                The HTTP status code that corresponds to
                ``google.rpc.Status.code``.
            message (str):
                This corresponds to ``google.rpc.Status.message``.
            status (google.rpc.code_pb2.Code):
                This is the enum version for ``google.rpc.Status.code``.
            details (MutableSequence[google.protobuf.any_pb2.Any]):
                This corresponds to ``google.rpc.Status.details``.
        """

        code: int = proto.Field(
            proto.INT32,
            number=1,
        )
        message: str = proto.Field(
            proto.STRING,
            number=2,
        )
        status: code_pb2.Code = proto.Field(
            proto.ENUM,
            number=4,
            enum=code_pb2.Code,
        )
        details: MutableSequence[any_pb2.Any] = proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message=any_pb2.Any,
        )

    error: Status = proto.Field(
        proto.MESSAGE,
        number=1,
        message=Status,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
