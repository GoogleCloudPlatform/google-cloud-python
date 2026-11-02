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
    package="google.cloud.dialogflow.cx.v3",
    manifest={
        "DataType",
        "ParameterDefinition",
        "TypeSchema",
        "InlineSchema",
    },
)


class DataType(proto.Enum):
    r"""Defines data types that are supported for inlined schemas. These
    types are consistent with
    [google.protobuf.Value][google.protobuf.Value].

    Values:
        DATA_TYPE_UNSPECIFIED (0):
            Not specified.
        STRING (1):
            Represents any string value.
        NUMBER (2):
            Represents any number value.
        BOOLEAN (3):
            Represents a boolean value.
        ARRAY (6):
            Represents a repeated value.
    """

    DATA_TYPE_UNSPECIFIED = 0
    STRING = 1
    NUMBER = 2
    BOOLEAN = 3
    ARRAY = 6


class ParameterDefinition(proto.Message):
    r"""Defines the properties of a parameter.
    Used to define parameters used in the agent and the input /
    output parameters for each fulfillment.

    Attributes:
        name (str):
            Required. Name of parameter.
        type_ (google.cloud.dialogflowcx_v3.types.ParameterDefinition.ParameterType):
            Type of parameter.
        type_schema (google.cloud.dialogflowcx_v3.types.TypeSchema):
            Optional. Type schema of parameter.
        description (str):
            Human-readable description of the parameter.
            Limited to 300 characters.
    """

    class ParameterType(proto.Enum):
        r"""Parameter types are used for validation. These types are consistent
        with [google.protobuf.Value][google.protobuf.Value].

        Values:
            PARAMETER_TYPE_UNSPECIFIED (0):
                Not specified. No validation will be
                performed.
            STRING (1):
                Represents any string value.
            NUMBER (2):
                Represents any number value.
            BOOLEAN (3):
                Represents a boolean value.
            NULL (4):
                Represents a null value.
            OBJECT (5):
                Represents any object value.
            LIST (6):
                Represents a repeated value.
        """

        PARAMETER_TYPE_UNSPECIFIED = 0
        STRING = 1
        NUMBER = 2
        BOOLEAN = 3
        NULL = 4
        OBJECT = 5
        LIST = 6

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: ParameterType = proto.Field(
        proto.ENUM,
        number=2,
        enum=ParameterType,
    )
    type_schema: "TypeSchema" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="TypeSchema",
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )


class TypeSchema(proto.Message):
    r"""Encapsulates different type schema variations: either a
    reference to an a schema that's already defined by a tool, or an
    inline definition.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        inline_schema (google.cloud.dialogflowcx_v3.types.InlineSchema):
            Set if this is an inline schema definition.

            This field is a member of `oneof`_ ``schema``.
        schema_reference (google.cloud.dialogflowcx_v3.types.TypeSchema.SchemaReference):
            Set if this is a schema reference.

            This field is a member of `oneof`_ ``schema``.
    """

    class SchemaReference(proto.Message):
        r"""A reference to the schema of an existing tool.

        Attributes:
            tool (str):
                The tool that contains this schema definition. Format:
                ``projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/tools/<ToolID>``.
            schema (str):
                The name of the schema.
        """

        tool: str = proto.Field(
            proto.STRING,
            number=1,
        )
        schema: str = proto.Field(
            proto.STRING,
            number=2,
        )

    inline_schema: "InlineSchema" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="schema",
        message="InlineSchema",
    )
    schema_reference: SchemaReference = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="schema",
        message=SchemaReference,
    )


class InlineSchema(proto.Message):
    r"""A type schema object that's specified inline.

    Attributes:
        type_ (google.cloud.dialogflowcx_v3.types.DataType):
            Data type of the schema.
        items (google.cloud.dialogflowcx_v3.types.TypeSchema):
            Schema of the elements if this is an ARRAY
            type.
    """

    type_: "DataType" = proto.Field(
        proto.ENUM,
        number=1,
        enum="DataType",
    )
    items: "TypeSchema" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="TypeSchema",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
