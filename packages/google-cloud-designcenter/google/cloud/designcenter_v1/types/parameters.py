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
    package="google.cloud.designcenter.v1",
    manifest={
        "ComponentVariable",
        "SaaSRuntimeContext",
        "ConnectionParameters",
        "ComponentParameterSchema",
        "Parameter",
        "CloudControlConfig",
    },
)


class ComponentVariable(proto.Message):
    r"""The details of an input/output variable: the variable and the
    component Uri. name.

    Attributes:
        variable (str):
            Required. Name of the variable.
        component_uri (str):
            Required. Component to which this variable
            belongs.
    """

    variable: str = proto.Field(
        proto.STRING,
        number=1,
    )
    component_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SaaSRuntimeContext(proto.Message):
    r"""SaaS runtime context.

    Attributes:
        saas_names (MutableSequence[str]):
            Optional. The SaaS names. Format for each
            SaaS:
            projects/{project}/locations/{location}/saas/{saas}
    """

    saas_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class ConnectionParameters(proto.Message):
    r"""Connection level parameters associated with each component
    within an application.

    Attributes:
        connection (str):
            Required. The name of the connection
            parameter.
        parameters (MutableSequence[google.cloud.designcenter_v1.types.Parameter]):
            Optional. A list of parameters associated
            with the connection.
    """

    connection: str = proto.Field(
        proto.STRING,
        number=1,
    )
    parameters: MutableSequence["Parameter"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Parameter",
    )


class ComponentParameterSchema(proto.Message):
    r"""Component parameter schema, which contains a list of all
    component parameters.

    Attributes:
        key (str):
            Output only. The key of the parameter.
        default_value (google.protobuf.struct_pb2.Value):
            Output only. The default value of the
            parameter.
        is_required (bool):
            Output only. Whether the parameter is
            required.
        type_ (str):
            Output only. The type of the parameter.
    """

    key: str = proto.Field(
        proto.STRING,
        number=1,
    )
    default_value: struct_pb2.Value = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Value,
    )
    is_required: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=4,
    )


class Parameter(proto.Message):
    r"""Parameter resource.

    Attributes:
        key (str):
            Required. The key of the parameter.
        value (google.protobuf.struct_pb2.Value):
            Optional. The value of the parameter.
        read_only (bool):
            Output only. Indicates if the parameter is
            read-only (driven by expression).
    """

    key: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: struct_pb2.Value = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Value,
    )
    read_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class CloudControlConfig(proto.Message):
    r"""Parameter values stored for a single cloud control of a
    policy.

    Attributes:
        cloud_control (str):
            Required. Resource name of the cloud control that these
            parameter values apply to. Format:
            organizations/{organization}/locations/{location}/cloudControls/{cloud_control}
            or
            projects/{project}/locations/{location}/cloudControls/{cloud_control}
        parameters (MutableSequence[google.cloud.designcenter_v1.types.Parameter]):
            Optional. Parameter values for this specific
            control.
    """

    cloud_control: str = proto.Field(
        proto.STRING,
        number=1,
    )
    parameters: MutableSequence["Parameter"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Parameter",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
