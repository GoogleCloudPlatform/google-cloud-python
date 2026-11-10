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

from google.cloud.oracledatabase_v1.types import common

__protobuf__ = proto.module(
    package="google.cloud.oracledatabase.v1",
    manifest={
        "FlexComponent",
        "FlexComponentProperties",
        "ListFlexComponentsRequest",
        "ListFlexComponentsResponse",
    },
)


class FlexComponent(proto.Message):
    r"""Details of the Flex Component resource.

    Attributes:
        name (str):
            Identifier. Specifies the name of the Flex Component
            resource with the format:
            projects/{project}/locations/{region}/flexComponents/{flex_component}
        properties (google.cloud.oracledatabase_v1.types.FlexComponentProperties):
            Output only. The properties of the Flex
            Component.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    properties: "FlexComponentProperties" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="FlexComponentProperties",
    )


class FlexComponentProperties(proto.Message):
    r"""The properties of the Flex Component.

    Attributes:
        name (str):
            Output only. The name of the Flex Component
            used for the DB system.
        hardware_type (google.cloud.oracledatabase_v1.types.FlexComponentProperties.HardwareType):
            Output only. The hardware type of the DB
            (Compute) or Storage (Cell) Server for this Flex
            Component.
        shape (str):
            Output only. The name of the DB system shape
            for this Flex Component.
        available_core_count (int):
            Output only. The maximum number of CPU cores
            that can be enabled on the DB system for this
            shape.
        available_memory_gb (int):
            Output only. The maximum memory size that can
            be enabled on the DB Server for this Flex
            Component.
        available_local_storage_gb (int):
            Output only. The maximum local storage that
            can be enabled on the DB Server for this Flex
            Component.
        available_db_node_storage_per_node_gb (int):
            Output only. The maximum storage that can be
            enabled on the Storage Server for this Flex
            Component.
        minimum_core_count (int):
            Output only. The minimum number of CPU cores
            that can be enabled on the DB Server for this
            Flex Component.
        runtime_minimum_core_count (int):
            Output only. The runtime minimum number of
            CPU cores that can be enabled for this Flex
            Component.
        description_summary (str):
            Output only. The description summary for this
            Flex Component.
        compute_model (google.cloud.oracledatabase_v1.types.ComputeModel):
            Output only. The compute model of the DB
            Server for this Flex Component.
    """

    class HardwareType(proto.Enum):
        r"""HardwareType enum

        Values:
            HARDWARE_TYPE_UNSPECIFIED (0):
                Unspecified default
            COMPUTE (1):
                COMPUTE
            CELL (2):
                CELL
        """

        HARDWARE_TYPE_UNSPECIFIED = 0
        COMPUTE = 1
        CELL = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    hardware_type: HardwareType = proto.Field(
        proto.ENUM,
        number=2,
        enum=HardwareType,
    )
    shape: str = proto.Field(
        proto.STRING,
        number=3,
    )
    available_core_count: int = proto.Field(
        proto.INT32,
        number=4,
    )
    available_memory_gb: int = proto.Field(
        proto.INT32,
        number=5,
    )
    available_local_storage_gb: int = proto.Field(
        proto.INT32,
        number=6,
    )
    available_db_node_storage_per_node_gb: int = proto.Field(
        proto.INT32,
        number=7,
    )
    minimum_core_count: int = proto.Field(
        proto.INT32,
        number=8,
    )
    runtime_minimum_core_count: int = proto.Field(
        proto.INT32,
        number=9,
    )
    description_summary: str = proto.Field(
        proto.STRING,
        number=10,
    )
    compute_model: common.ComputeModel = proto.Field(
        proto.ENUM,
        number=11,
        enum=common.ComputeModel,
    )


class ListFlexComponentsRequest(proto.Message):
    r"""Message for listing FlexComponents.

    Attributes:
        parent (str):
            Required. Parent value for
            ListFlexComponentsRequest Format:
            projects/{project}/locations/{location}
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. An expression for filtering the results of the
            request. Only the ``shape`` field is supported in the
            following format: ``shape="{shape}"``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListFlexComponentsResponse(proto.Message):
    r"""Message for response to listing FlexComponents

    Attributes:
        flex_components (MutableSequence[google.cloud.oracledatabase_v1.types.FlexComponent]):
            The list of FlexComponent
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    flex_components: MutableSequence["FlexComponent"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="FlexComponent",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
