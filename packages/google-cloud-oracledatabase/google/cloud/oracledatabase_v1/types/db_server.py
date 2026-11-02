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
        "DbServer",
        "DbServerProperties",
    },
)


class DbServer(proto.Message):
    r"""Details of the database server resource.
    https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/DbServer/

    Attributes:
        name (str):
            Identifier. The name of the database server resource with
            the format:
            projects/{project}/locations/{location}/cloudExadataInfrastructures/{cloud_exadata_infrastructure}/dbServers/{db_server}
        display_name (str):
            Optional. User friendly name for this
            resource.
        properties (google.cloud.oracledatabase_v1.types.DbServerProperties):
            Optional. Various properties of the database
            server.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    properties: "DbServerProperties" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DbServerProperties",
    )


class DbServerProperties(proto.Message):
    r"""Various properties and settings associated with Exadata
    database server.

    Attributes:
        ocid (str):
            Output only. OCID of database server.
        ocpu_count (int):
            Optional. OCPU count per database.
        max_ocpu_count (int):
            Optional. Maximum OCPU count per database.
        memory_size_gb (int):
            Optional. Memory allocated in GBs.
        max_memory_size_gb (int):
            Optional. Maximum memory allocated in GBs.
        db_node_storage_size_gb (int):
            Optional. Local storage per VM.
        max_db_node_storage_size_gb (int):
            Optional. Maximum local storage per VM.
        vm_count (int):
            Optional. Vm count per database.
        state (google.cloud.oracledatabase_v1.types.DbServerProperties.State):
            Output only. State of the database server.
        db_node_ids (MutableSequence[str]):
            Output only. OCID of database nodes
            associated with the database server.
    """

    class State(proto.Enum):
        r"""The various lifecycle states of the database server.

        Values:
            STATE_UNSPECIFIED (0):
                Default unspecified value.
            CREATING (1):
                Indicates that the resource is in creating
                state.
            AVAILABLE (2):
                Indicates that the resource is in available
                state.
            UNAVAILABLE (3):
                Indicates that the resource is in unavailable
                state.
            DELETING (4):
                Indicates that the resource is in deleting
                state.
            DELETED (5):
                Indicates that the resource is in deleted
                state.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        AVAILABLE = 2
        UNAVAILABLE = 3
        DELETING = 4
        DELETED = 5

    ocid: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ocpu_count: int = proto.Field(
        proto.INT32,
        number=2,
    )
    max_ocpu_count: int = proto.Field(
        proto.INT32,
        number=3,
    )
    memory_size_gb: int = proto.Field(
        proto.INT32,
        number=4,
    )
    max_memory_size_gb: int = proto.Field(
        proto.INT32,
        number=5,
    )
    db_node_storage_size_gb: int = proto.Field(
        proto.INT32,
        number=6,
    )
    max_db_node_storage_size_gb: int = proto.Field(
        proto.INT32,
        number=7,
    )
    vm_count: int = proto.Field(
        proto.INT32,
        number=8,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=9,
        enum=State,
    )
    db_node_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
