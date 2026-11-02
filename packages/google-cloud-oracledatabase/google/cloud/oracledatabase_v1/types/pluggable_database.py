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
        "PluggableDatabase",
        "PluggableDatabaseProperties",
        "PluggableDatabaseConnectionStrings",
        "PluggableDatabaseNodeLevelDetails",
        "DatabaseManagementConfig",
        "GetPluggableDatabaseRequest",
        "ListPluggableDatabasesRequest",
        "ListPluggableDatabasesResponse",
    },
)


class PluggableDatabase(proto.Message):
    r"""The PluggableDatabase resource.
    https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/PluggableDatabase/

    Attributes:
        name (str):
            Identifier. The name of the PluggableDatabase resource in
            the following format:
            projects/{project}/locations/{region}/pluggableDatabases/{pluggable_database}
        properties (google.cloud.oracledatabase_v1.types.PluggableDatabaseProperties):
            Optional. The properties of the
            PluggableDatabase.
        oci_url (str):
            Output only. HTTPS link to OCI resources
            exposed to Customer via UI Interface.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The date and time that the
            PluggableDatabase was created.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    properties: "PluggableDatabaseProperties" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="PluggableDatabaseProperties",
    )
    oci_url: str = proto.Field(
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class PluggableDatabaseProperties(proto.Message):
    r"""The properties of a PluggableDatabase.

    Attributes:
        compartment_id (str):
            Required. The OCID of the compartment.
        connection_strings (google.cloud.oracledatabase_v1.types.PluggableDatabaseConnectionStrings):
            Optional. The Connection strings used to
            connect to the Oracle Database.
        container_database_ocid (str):
            Required. The OCID of the CDB.
        defined_tags (MutableMapping[str, google.cloud.oracledatabase_v1.types.PluggableDatabaseProperties.DefinedTagValue]):
            Optional. Defined tags for this resource.
            Each key is predefined and scoped to a
            namespace.
        freeform_tags (MutableMapping[str, str]):
            Optional. Free-form tags for this resource.
            Each tag is a simple key-value pair with no
            predefined name, type, or namespace.
        ocid (str):
            Output only. The OCID of the pluggable
            database.
        is_restricted (bool):
            Optional. The restricted mode of the
            pluggable database. If a pluggable database is
            opened in restricted mode, the user needs both
            create a session and have restricted session
            privileges to connect to it.
        lifecycle_details (str):
            Output only. Additional information about the
            current lifecycle state.
        lifecycle_state (google.cloud.oracledatabase_v1.types.PluggableDatabaseProperties.PluggableDatabaseLifecycleState):
            Output only. The current state of the
            pluggable database.
        pdb_name (str):
            Required. The database name.
        pdb_node_level_details (MutableSequence[google.cloud.oracledatabase_v1.types.PluggableDatabaseNodeLevelDetails]):
            Optional. Pluggable Database Node Level
            Details
        database_management_config (google.cloud.oracledatabase_v1.types.DatabaseManagementConfig):
            Output only. The configuration of the
            Database Management service.
        operations_insights_state (google.cloud.oracledatabase_v1.types.PluggableDatabaseProperties.OperationsInsightsState):
            Output only. The status of Operations
            Insights for this Database.
    """

    class PluggableDatabaseLifecycleState(proto.Enum):
        r"""The various lifecycle states of the PluggableDatabase.

        Values:
            PLUGGABLE_DATABASE_LIFECYCLE_STATE_UNSPECIFIED (0):
                The lifecycle state is unspecified.
            PROVISIONING (1):
                The pluggable database is provisioning.
            AVAILABLE (2):
                The pluggable database is available.
            TERMINATING (3):
                The pluggable database is terminating.
            TERMINATED (4):
                The pluggable database is terminated.
            UPDATING (5):
                The pluggable database is updating.
            FAILED (6):
                The pluggable database is in a failed state.
            RELOCATING (7):
                The pluggable database is relocating.
            RELOCATED (8):
                The pluggable database is relocated.
            REFRESHING (9):
                The pluggable database is refreshing.
            RESTORE_IN_PROGRESS (10):
                The pluggable database is restoring.
            RESTORE_FAILED (11):
                The pluggable database restore failed.
            BACKUP_IN_PROGRESS (12):
                The pluggable database is backing up.
            DISABLED (13):
                The pluggable database is disabled.
        """

        PLUGGABLE_DATABASE_LIFECYCLE_STATE_UNSPECIFIED = 0
        PROVISIONING = 1
        AVAILABLE = 2
        TERMINATING = 3
        TERMINATED = 4
        UPDATING = 5
        FAILED = 6
        RELOCATING = 7
        RELOCATED = 8
        REFRESHING = 9
        RESTORE_IN_PROGRESS = 10
        RESTORE_FAILED = 11
        BACKUP_IN_PROGRESS = 12
        DISABLED = 13

    class OperationsInsightsState(proto.Enum):
        r"""The status of Operations Insights for this Database.

        Values:
            OPERATIONS_INSIGHTS_STATE_UNSPECIFIED (0):
                The status is not specified.
            ENABLING (1):
                Operations Insights is enabling.
            ENABLED (2):
                Operations Insights is enabled.
            DISABLING (3):
                Operations Insights is disabling.
            NOT_ENABLED (4):
                Operations Insights is not enabled.
            FAILED_ENABLING (5):
                Operations Insights failed to enable.
            FAILED_DISABLING (6):
                Operations Insights failed to disable.
        """

        OPERATIONS_INSIGHTS_STATE_UNSPECIFIED = 0
        ENABLING = 1
        ENABLED = 2
        DISABLING = 3
        NOT_ENABLED = 4
        FAILED_ENABLING = 5
        FAILED_DISABLING = 6

    class DefinedTagValue(proto.Message):
        r"""Wrapper message for the value of a defined tag.

        Attributes:
            tags (MutableMapping[str, str]):
                The tags within the namespace.
        """

        tags: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=1,
        )

    compartment_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    connection_strings: "PluggableDatabaseConnectionStrings" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="PluggableDatabaseConnectionStrings",
    )
    container_database_ocid: str = proto.Field(
        proto.STRING,
        number=3,
    )
    defined_tags: MutableMapping[str, DefinedTagValue] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=4,
        message=DefinedTagValue,
    )
    freeform_tags: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    ocid: str = proto.Field(
        proto.STRING,
        number=6,
    )
    is_restricted: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    lifecycle_details: str = proto.Field(
        proto.STRING,
        number=8,
    )
    lifecycle_state: PluggableDatabaseLifecycleState = proto.Field(
        proto.ENUM,
        number=9,
        enum=PluggableDatabaseLifecycleState,
    )
    pdb_name: str = proto.Field(
        proto.STRING,
        number=10,
    )
    pdb_node_level_details: MutableSequence["PluggableDatabaseNodeLevelDetails"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=11,
            message="PluggableDatabaseNodeLevelDetails",
        )
    )
    database_management_config: "DatabaseManagementConfig" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="DatabaseManagementConfig",
    )
    operations_insights_state: OperationsInsightsState = proto.Field(
        proto.ENUM,
        number=14,
        enum=OperationsInsightsState,
    )


class PluggableDatabaseConnectionStrings(proto.Message):
    r"""The connection strings used to connect to the Oracle
    Database.

    Attributes:
        all_connection_strings (MutableMapping[str, str]):
            Optional. All connection strings to use to
            connect to the pluggable database.
        pdb_default (str):
            Optional. The default connection string to
            use to connect to the pluggable database.
        pdb_ip_default (str):
            Optional. The default connection string to
            use to connect to the pluggable database using
            IP.
    """

    all_connection_strings: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=1,
    )
    pdb_default: str = proto.Field(
        proto.STRING,
        number=2,
    )
    pdb_ip_default: str = proto.Field(
        proto.STRING,
        number=3,
    )


class PluggableDatabaseNodeLevelDetails(proto.Message):
    r"""The Pluggable Database Node Level Details.

    Attributes:
        node_name (str):
            Required. The Node name of the Database home.
        open_mode (google.cloud.oracledatabase_v1.types.PluggableDatabaseNodeLevelDetails.PluggableDatabaseOpenMode):
            Required. The mode that the pluggable
            database is in to open it.
        pluggable_database_id (str):
            Required. The OCID of the Pluggable Database.
    """

    class PluggableDatabaseOpenMode(proto.Enum):
        r"""The mode that the pluggable database is in to open it.

        Values:
            PLUGGABLE_DATABASE_OPEN_MODE_UNSPECIFIED (0):
                The open mode is unspecified.
            READ_ONLY (1):
                The pluggable database is opened in read-only
                mode.
            READ_WRITE (2):
                The pluggable database is opened in
                read-write mode.
            MOUNTED (3):
                The pluggable database is mounted.
            MIGRATE (4):
                The pluggable database is migrated.
        """

        PLUGGABLE_DATABASE_OPEN_MODE_UNSPECIFIED = 0
        READ_ONLY = 1
        READ_WRITE = 2
        MOUNTED = 3
        MIGRATE = 4

    node_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    open_mode: PluggableDatabaseOpenMode = proto.Field(
        proto.ENUM,
        number=2,
        enum=PluggableDatabaseOpenMode,
    )
    pluggable_database_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DatabaseManagementConfig(proto.Message):
    r"""The configuration of the Database Management service.

    Attributes:
        management_state (google.cloud.oracledatabase_v1.types.DatabaseManagementConfig.ManagementState):
            Output only. The status of the Database
            Management service.
        management_type (google.cloud.oracledatabase_v1.types.DatabaseManagementConfig.ManagementType):
            Output only. The Database Management type.
    """

    class ManagementState(proto.Enum):
        r"""The status of the Database Management service.

        Values:
            MANAGEMENT_STATE_UNSPECIFIED (0):
                The status is not specified.
            ENABLING (1):
                The Database Management service is enabling.
            ENABLED (2):
                The Database Management service is enabled.
            DISABLING (3):
                The Database Management service is disabling.
            DISABLED (4):
                The Database Management service is disabled.
            UPDATING (5):
                The Database Management service is updating.
            FAILED_ENABLING (6):
                The Database Management service failed to
                enable.
            FAILED_DISABLING (7):
                The Database Management service failed to
                disable.
            FAILED_UPDATING (8):
                The Database Management service failed to
                update.
        """

        MANAGEMENT_STATE_UNSPECIFIED = 0
        ENABLING = 1
        ENABLED = 2
        DISABLING = 3
        DISABLED = 4
        UPDATING = 5
        FAILED_ENABLING = 6
        FAILED_DISABLING = 7
        FAILED_UPDATING = 8

    class ManagementType(proto.Enum):
        r"""The Database Management type.

        Values:
            MANAGEMENT_TYPE_UNSPECIFIED (0):
                The type is not specified.
            BASIC (1):
                Basic Database Management.
            ADVANCED (2):
                Advanced Database Management.
        """

        MANAGEMENT_TYPE_UNSPECIFIED = 0
        BASIC = 1
        ADVANCED = 2

    management_state: ManagementState = proto.Field(
        proto.ENUM,
        number=1,
        enum=ManagementState,
    )
    management_type: ManagementType = proto.Field(
        proto.ENUM,
        number=2,
        enum=ManagementType,
    )


class GetPluggableDatabaseRequest(proto.Message):
    r"""The request for ``PluggableDatabase.Get``.

    Attributes:
        name (str):
            Required. The name of the PluggableDatabase resource in the
            following format:
            projects/{project}/locations/{region}/pluggableDatabases/{pluggable_database}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListPluggableDatabasesRequest(proto.Message):
    r"""The request for ``PluggableDatabase.List``.

    Attributes:
        parent (str):
            Required. The parent, which owns this
            collection of PluggableDatabases. Format:
            projects/{project}/locations/{location}
        page_size (int):
            Optional. The maximum number of
            PluggableDatabases to return. The service may
            return fewer than this value.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListPluggableDatabases`` call. Provide this to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``ListPluggableDatabases`` must match the call that provided
            the page token.
        filter (str):
            Optional. An expression for filtering the results of the
            request. List for pluggable databases is supported only with
            a valid container database (full resource name) filter in
            this format:
            ``database="projects/{project}/locations/{location}/databases/{database}"``
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


class ListPluggableDatabasesResponse(proto.Message):
    r"""The response for ``PluggableDatabase.List``.

    Attributes:
        pluggable_databases (MutableSequence[google.cloud.oracledatabase_v1.types.PluggableDatabase]):
            The list of PluggableDatabases.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    pluggable_databases: MutableSequence["PluggableDatabase"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="PluggableDatabase",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
