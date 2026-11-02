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

import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.ces.v1beta",
    manifest={
        "Schema",
    },
)


class Schema(proto.Message):
    r"""Represents a select subset of an OpenAPI 3.0 schema object.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        type_ (google.cloud.ces_v1beta.types.Schema.Type):
            Required. The type of the data.
        properties (MutableMapping[str, google.cloud.ces_v1beta.types.Schema]):
            Optional. Properties of Type.OBJECT.
        required (MutableSequence[str]):
            Optional. Required properties of Type.OBJECT.
        description (str):
            Optional. The description of the data.
        items (google.cloud.ces_v1beta.types.Schema):
            Optional. Schema of the elements of
            Type.ARRAY.
        nullable (bool):
            Optional. Indicates if the value may be null.
        unique_items (bool):
            Optional. Indicate the items in the array
            must be unique. Only applies to TYPE.ARRAY.
        prefix_items (MutableSequence[google.cloud.ces_v1beta.types.Schema]):
            Optional. Schemas of initial elements of
            Type.ARRAY.
        additional_properties (google.cloud.ces_v1beta.types.Schema):
            Optional. Can either be a boolean or an
            object, controls the presence of additional
            properties.
        any_of (MutableSequence[google.cloud.ces_v1beta.types.Schema]):
            Optional. The value should be validated
            against any (one or more) of the subschemas in
            the list.
        enum (MutableSequence[str]):
            Optional. Possible values of the element of primitive type
            with enum format. Examples:

            1. We can define direction as : {type:STRING, format:enum,
               enum:["EAST", NORTH", "SOUTH", "WEST"]}
            2. We can define apartment number as : {type:INTEGER,
               format:enum, enum:["101", "201", "301"]}
        default (google.protobuf.struct_pb2.Value):
            Optional. Default value of the data.
        ref (str):
            Optional. Allows indirect references between schema nodes.
            The value should be a valid reference to a child of the root
            ``defs``.

            For example, the following schema defines a reference to a
            schema node named "Pet":

            ::

               type: object
               properties:
                 pet:
                   ref: #/defs/Pet
               defs:
                 Pet:
                   type: object
                   properties:
                     name:
                       type: string

            The value of the "pet" property is a reference to the schema
            node named "Pet". See details in
            https://json-schema.org/understanding-json-schema/structuring.
        defs (MutableMapping[str, google.cloud.ces_v1beta.types.Schema]):
            Optional. A map of definitions for use by ``ref``. Only
            allowed at the root of the schema.
        title (str):
            Optional. The title of the schema.
        min_items (int):
            Optional. Minimum number of the elements for
            Type.ARRAY.
        max_items (int):
            Optional. Maximum number of the elements for
            Type.ARRAY.
        minimum (float):
            Optional. Minimum value for Type.INTEGER and
            Type.NUMBER.

            This field is a member of `oneof`_ ``_minimum``.
        maximum (float):
            Optional. Maximum value for Type.INTEGER and
            Type.NUMBER.

            This field is a member of `oneof`_ ``_maximum``.
    """

    class Type(proto.Enum):
        r"""OpenAPI data types.

        Values:
            TYPE_UNSPECIFIED (0):
                Type unspecified.
            STRING (1):
                String type.
            INTEGER (2):
                Integer type.
            NUMBER (3):
                Number type.
            BOOLEAN (4):
                Boolean type.
            OBJECT (5):
                Object type.
            ARRAY (6):
                Array type.
        """

        TYPE_UNSPECIFIED = 0
        STRING = 1
        INTEGER = 2
        NUMBER = 3
        BOOLEAN = 4
        OBJECT = 5
        ARRAY = 6

    type_: Type = proto.Field(
        proto.ENUM,
        number=1,
        enum=Type,
    )
    properties: MutableMapping[str, "Schema"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=2,
        message="Schema",
    )
    required: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    items: "Schema" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="Schema",
    )
    nullable: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    unique_items: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    prefix_items: MutableSequence["Schema"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="Schema",
    )
    additional_properties: "Schema" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="Schema",
    )
    any_of: MutableSequence["Schema"] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message="Schema",
    )
    enum: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=11,
    )
    default: struct_pb2.Value = proto.Field(
        proto.MESSAGE,
        number=12,
        message=struct_pb2.Value,
    )
    ref: str = proto.Field(
        proto.STRING,
        number=13,
    )
    defs: MutableMapping[str, "Schema"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=14,
        message="Schema",
    )
    title: str = proto.Field(
        proto.STRING,
        number=15,
    )
    min_items: int = proto.Field(
        proto.INT64,
        number=16,
    )
    max_items: int = proto.Field(
        proto.INT64,
        number=17,
    )
    minimum: float = proto.Field(
        proto.DOUBLE,
        number=18,
        optional=True,
    )
    maximum: float = proto.Field(
        proto.DOUBLE,
        number=19,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
