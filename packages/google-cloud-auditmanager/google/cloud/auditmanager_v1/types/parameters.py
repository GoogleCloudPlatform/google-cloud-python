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
    package="google.cloud.auditmanager.v1",
    manifest={
        "Parameter",
        "StringList",
        "ParamValue",
        "ParameterOverrides",
        "ParameterState",
        "CloudControlParameterStates",
    },
)


class Parameter(proto.Message):
    r"""Parameters are key-value pairs that let you provide your
    custom location requirements, environment requirements, or other
    settings that are relevant to the cloud control.

    Attributes:
        name (str):
            Required. The name or key of the parameter.
        parameter_value (google.cloud.auditmanager_v1.types.ParamValue):
            Required. The value of the parameter.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    parameter_value: "ParamValue" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ParamValue",
    )


class StringList(proto.Message):
    r"""A list of strings for the parameter value.

    Attributes:
        values (MutableSequence[str]):
            Required. The strings in the list.
    """

    values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class ParamValue(proto.Message):
    r"""The possible parameter value types.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        string_value (str):
            Optional. A string value.

            This field is a member of `oneof`_ ``kind``.
        bool_value (bool):
            Optional. A boolean value.

            This field is a member of `oneof`_ ``kind``.
        string_list_value (google.cloud.auditmanager_v1.types.StringList):
            Optional. A repeated string.

            This field is a member of `oneof`_ ``kind``.
        number_value (float):
            Optional. A double value.

            This field is a member of `oneof`_ ``kind``.
        oneof_value (google.cloud.auditmanager_v1.types.Parameter):
            Optional. Sub-parameter values.

            This field is a member of `oneof`_ ``kind``.
    """

    string_value: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="kind",
    )
    bool_value: bool = proto.Field(
        proto.BOOL,
        number=4,
        oneof="kind",
    )
    string_list_value: "StringList" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="kind",
        message="StringList",
    )
    number_value: float = proto.Field(
        proto.DOUBLE,
        number=6,
        oneof="kind",
    )
    oneof_value: "Parameter" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="kind",
        message="Parameter",
    )


class ParameterOverrides(proto.Message):
    r"""Wrapper message to associate a list of CSC internal parameter
    overrides with a control name.

    Attributes:
        parameters (MutableSequence[google.cloud.auditmanager_v1.types.Parameter]):
            The list of parameter overrides.
    """

    parameters: MutableSequence["Parameter"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Parameter",
    )


class ParameterState(proto.Message):
    r"""State of a parameter for a cloud control.

    Attributes:
        parameter (google.cloud.auditmanager_v1.types.Parameter):
            Output only. The parameter key and value.
        is_overridden (bool):
            Output only. Whether this parameter was
            overridden by the user.
    """

    parameter: "Parameter" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Parameter",
    )
    is_overridden: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class CloudControlParameterStates(proto.Message):
    r"""Collection of parameter states for a cloud control.

    Attributes:
        parameter_states (MutableSequence[google.cloud.auditmanager_v1.types.ParameterState]):
            Output only. The parameter states for the
            cloud control.
    """

    parameter_states: MutableSequence["ParameterState"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ParameterState",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
