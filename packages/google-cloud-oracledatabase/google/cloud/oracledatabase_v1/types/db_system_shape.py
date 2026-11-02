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
    package="google.cloud.oracledatabase.v1",
    manifest={
        "DbSystemShape",
    },
)


class DbSystemShape(proto.Message):
    r"""Details of the Database System Shapes resource.
    https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/DbSystemShapeSummary/

    Attributes:
        name (str):
            Identifier. The name of the Database System Shape resource
            with the format:
            projects/{project}/locations/{region}/dbSystemShapes/{db_system_shape}
        shape (str):
            Optional. shape
        min_node_count (int):
            Optional. Minimum number of database servers.
        max_node_count (int):
            Optional. Maximum number of database servers.
        min_storage_count (int):
            Optional. Minimum number of storage servers.
        max_storage_count (int):
            Optional. Maximum number of storage servers.
        available_core_count_per_node (int):
            Optional. Number of cores per node.
        available_memory_per_node_gb (int):
            Optional. Memory per database server node in
            gigabytes.
        available_data_storage_tb (int):
            Optional. Storage per storage server in
            terabytes.
        min_core_count_per_node (int):
            Optional. Minimum core count per node.
        min_memory_per_node_gb (int):
            Optional. Minimum memory per node in
            gigabytes.
        min_db_node_storage_per_node_gb (int):
            Optional. Minimum node storage per database
            server in gigabytes.
        minimum_core_count (int):
            Optional. Minimum core count per node.
        available_core_count (int):
            Optional. Available core count.
        core_count_increment (int):
            Optional. Core count increment.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    shape: str = proto.Field(
        proto.STRING,
        number=2,
    )
    min_node_count: int = proto.Field(
        proto.INT32,
        number=3,
    )
    max_node_count: int = proto.Field(
        proto.INT32,
        number=4,
    )
    min_storage_count: int = proto.Field(
        proto.INT32,
        number=5,
    )
    max_storage_count: int = proto.Field(
        proto.INT32,
        number=6,
    )
    available_core_count_per_node: int = proto.Field(
        proto.INT32,
        number=7,
    )
    available_memory_per_node_gb: int = proto.Field(
        proto.INT32,
        number=8,
    )
    available_data_storage_tb: int = proto.Field(
        proto.INT32,
        number=9,
    )
    min_core_count_per_node: int = proto.Field(
        proto.INT32,
        number=10,
    )
    min_memory_per_node_gb: int = proto.Field(
        proto.INT32,
        number=11,
    )
    min_db_node_storage_per_node_gb: int = proto.Field(
        proto.INT32,
        number=12,
    )
    minimum_core_count: int = proto.Field(
        proto.INT32,
        number=13,
    )
    available_core_count: int = proto.Field(
        proto.INT32,
        number=14,
    )
    core_count_increment: int = proto.Field(
        proto.INT32,
        number=15,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
