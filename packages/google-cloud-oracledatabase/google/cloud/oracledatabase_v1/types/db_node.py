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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.oracledatabase.v1",
    manifest={
        "DbNode",
        "DbNodeProperties",
    },
)


class DbNode(proto.Message):
    r"""Details of the database node resource.
    https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/DbNode/

    Attributes:
        name (str):
            Identifier. The name of the database node resource in the
            following format:
            projects/{project}/locations/{location}/cloudVmClusters/{cloud_vm_cluster}/dbNodes/{db_node}
        properties (google.cloud.oracledatabase_v1.types.DbNodeProperties):
            Optional. Various properties of the database
            node.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    properties: "DbNodeProperties" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DbNodeProperties",
    )


class DbNodeProperties(proto.Message):
    r"""Various properties and settings associated with Db node.

    Attributes:
        ocid (str):
            Output only. OCID of database node.
        ocpu_count (int):
            Optional. OCPU count per database node.
        memory_size_gb (int):
            Memory allocated in GBs.
        db_node_storage_size_gb (int):
            Optional. Local storage per database node.
        db_server_ocid (str):
            Optional. Database server OCID.
        hostname (str):
            Optional. DNS
        state (google.cloud.oracledatabase_v1.types.DbNodeProperties.State):
            Output only. State of the database node.
        total_cpu_core_count (int):
            Total CPU core count of the database node.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The date and time that the
            database node was created.
    """

    class State(proto.Enum):
        r"""The various lifecycle states of the database node.

        Values:
            STATE_UNSPECIFIED (0):
                Default unspecified value.
            PROVISIONING (1):
                Indicates that the resource is in
                provisioning state.
            AVAILABLE (2):
                Indicates that the resource is in available
                state.
            UPDATING (3):
                Indicates that the resource is in updating
                state.
            STOPPING (4):
                Indicates that the resource is in stopping
                state.
            STOPPED (5):
                Indicates that the resource is in stopped
                state.
            STARTING (6):
                Indicates that the resource is in starting
                state.
            TERMINATING (7):
                Indicates that the resource is in terminating
                state.
            TERMINATED (8):
                Indicates that the resource is in terminated
                state.
            FAILED (9):
                Indicates that the resource is in failed
                state.
        """

        STATE_UNSPECIFIED = 0
        PROVISIONING = 1
        AVAILABLE = 2
        UPDATING = 3
        STOPPING = 4
        STOPPED = 5
        STARTING = 6
        TERMINATING = 7
        TERMINATED = 8
        FAILED = 9

    ocid: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ocpu_count: int = proto.Field(
        proto.INT32,
        number=2,
    )
    memory_size_gb: int = proto.Field(
        proto.INT32,
        number=3,
    )
    db_node_storage_size_gb: int = proto.Field(
        proto.INT32,
        number=4,
    )
    db_server_ocid: str = proto.Field(
        proto.STRING,
        number=5,
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=8,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=9,
        enum=State,
    )
    total_cpu_core_count: int = proto.Field(
        proto.INT32,
        number=10,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
