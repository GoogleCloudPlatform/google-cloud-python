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
    package="google.ads.admanager.v1",
    manifest={
        "ReportValue",
    },
)


class ReportValue(proto.Message):
    r"""Represents a single value in a report.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        int_value (int):
            For integer values.

            This field is a member of `oneof`_ ``value``.
        double_value (float):
            For double values.

            This field is a member of `oneof`_ ``value``.
        string_value (str):
            For string values.

            This field is a member of `oneof`_ ``value``.
        bool_value (bool):
            For boolean values.

            This field is a member of `oneof`_ ``value``.
        int_list_value (google.ads.admanager_v1.types.ReportValue.IntList):
            For lists of integer values.

            This field is a member of `oneof`_ ``value``.
        string_list_value (google.ads.admanager_v1.types.ReportValue.StringList):
            For lists of string values.

            This field is a member of `oneof`_ ``value``.
        double_list_value (google.ads.admanager_v1.types.ReportValue.DoubleList):
            For lists of double values.

            This field is a member of `oneof`_ ``value``.
        bytes_value (bytes):
            For bytes values.

            This field is a member of `oneof`_ ``value``.
    """

    class IntList(proto.Message):
        r"""A list of integer values.

        Attributes:
            values (MutableSequence[int]):
                The values
        """

        values: MutableSequence[int] = proto.RepeatedField(
            proto.INT64,
            number=1,
        )

    class StringList(proto.Message):
        r"""A list of string values.

        Attributes:
            values (MutableSequence[str]):
                The values
        """

        values: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    class DoubleList(proto.Message):
        r"""A list of double values.

        Attributes:
            values (MutableSequence[float]):
                The values
        """

        values: MutableSequence[float] = proto.RepeatedField(
            proto.DOUBLE,
            number=1,
        )

    int_value: int = proto.Field(
        proto.INT64,
        number=1,
        oneof="value",
    )
    double_value: float = proto.Field(
        proto.DOUBLE,
        number=2,
        oneof="value",
    )
    string_value: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="value",
    )
    bool_value: bool = proto.Field(
        proto.BOOL,
        number=4,
        oneof="value",
    )
    int_list_value: IntList = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="value",
        message=IntList,
    )
    string_list_value: StringList = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="value",
        message=StringList,
    )
    double_list_value: DoubleList = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="value",
        message=DoubleList,
    )
    bytes_value: bytes = proto.Field(
        proto.BYTES,
        number=8,
        oneof="value",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
