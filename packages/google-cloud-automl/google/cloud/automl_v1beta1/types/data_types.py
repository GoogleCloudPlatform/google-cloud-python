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
    package="google.cloud.automl.v1beta1",
    manifest={
        "TypeCode",
        "DataType",
        "StructType",
    },
)


class TypeCode(proto.Enum):
    r"""``TypeCode`` is used as a part of
    [DataType][google.cloud.automl.v1beta1.DataType].

    Values:
        TYPE_CODE_UNSPECIFIED (0):
            Not specified. Should not be used.
        FLOAT64 (3):
            Encoded as ``number``, or the strings ``"NaN"``,
            ``"Infinity"``, or ``"-Infinity"``.
        TIMESTAMP (4):
            Must be between 0AD and 9999AD. Encoded as ``string``
            according to
            [time_format][google.cloud.automl.v1beta1.DataType.time_format],
            or, if that format is not set, then in RFC 3339
            ``date-time`` format, where ``time-offset`` = ``"Z"`` (e.g.
            1985-04-12T23:20:50.52Z).
        STRING (6):
            Encoded as ``string``.
        ARRAY (8):
            Encoded as ``list``, where the list elements are represented
            according to

            [list_element_type][google.cloud.automl.v1beta1.DataType.list_element_type].
        STRUCT (9):
            Encoded as ``struct``, where field values are represented
            according to
            [struct_type][google.cloud.automl.v1beta1.DataType.struct_type].
        CATEGORY (10):
            Values of this type are not further understood by AutoML,
            e.g. AutoML is unable to tell the order of values (as it
            could with FLOAT64), or is unable to say if one value
            contains another (as it could with STRING). Encoded as
            ``string`` (bytes should be base64-encoded, as described in
            RFC 4648, section 4).
    """

    TYPE_CODE_UNSPECIFIED = 0
    FLOAT64 = 3
    TIMESTAMP = 4
    STRING = 6
    ARRAY = 8
    STRUCT = 9
    CATEGORY = 10


class DataType(proto.Message):
    r"""Indicated the type of data that can be stored in a structured
    data entity (e.g. a table).

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        list_element_type (google.cloud.automl_v1beta1.types.DataType):
            If
            [type_code][google.cloud.automl.v1beta1.DataType.type_code]
            == [ARRAY][google.cloud.automl.v1beta1.TypeCode.ARRAY], then
            ``list_element_type`` is the type of the elements.

            This field is a member of `oneof`_ ``details``.
        struct_type (google.cloud.automl_v1beta1.types.StructType):
            If
            [type_code][google.cloud.automl.v1beta1.DataType.type_code]
            == [STRUCT][google.cloud.automl.v1beta1.TypeCode.STRUCT],
            then ``struct_type`` provides type information for the
            struct's fields.

            This field is a member of `oneof`_ ``details``.
        time_format (str):
            If
            [type_code][google.cloud.automl.v1beta1.DataType.type_code]
            ==
            [TIMESTAMP][google.cloud.automl.v1beta1.TypeCode.TIMESTAMP]
            then ``time_format`` provides the format in which that time
            field is expressed. The time_format must either be one of:

            - ``UNIX_SECONDS``
            - ``UNIX_MILLISECONDS``
            - ``UNIX_MICROSECONDS``
            - ``UNIX_NANOSECONDS`` (for respectively number of seconds,
              milliseconds, microseconds and nanoseconds since start of
              the Unix epoch); or be written in ``strftime`` syntax. If
              time_format is not set, then the default format as
              described on the type_code is used.

            This field is a member of `oneof`_ ``details``.
        type_code (google.cloud.automl_v1beta1.types.TypeCode):
            Required. The
            [TypeCode][google.cloud.automl.v1beta1.TypeCode] for this
            type.
        nullable (bool):
            If true, this DataType can also be ``NULL``. In .CSV files
            ``NULL`` value is expressed as an empty string.
    """

    list_element_type: "DataType" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="details",
        message="DataType",
    )
    struct_type: "StructType" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="details",
        message="StructType",
    )
    time_format: str = proto.Field(
        proto.STRING,
        number=5,
        oneof="details",
    )
    type_code: "TypeCode" = proto.Field(
        proto.ENUM,
        number=1,
        enum="TypeCode",
    )
    nullable: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class StructType(proto.Message):
    r"""``StructType`` defines the DataType-s of a
    [STRUCT][google.cloud.automl.v1beta1.TypeCode.STRUCT] type.

    Attributes:
        fields (MutableMapping[str, google.cloud.automl_v1beta1.types.DataType]):
            Unordered map of struct field names to their
            data types. Fields cannot be added or removed
            via Update. Their names and data types are still
            mutable.
    """

    fields: MutableMapping[str, "DataType"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=1,
        message="DataType",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
