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
import google.type.datetime_pb2 as datetime_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.oracledatabase_v1.types import database as gco_database

__protobuf__ = proto.module(
    package="google.cloud.oracledatabase.v1",
    manifest={
        "DbSystem",
        "DbSystemProperties",
        "DataCollectionOptionsDbSystem",
        "DbSystemOptions",
        "DbHome",
        "CreateDbSystemRequest",
        "DeleteDbSystemRequest",
        "GetDbSystemRequest",
        "ListDbSystemsRequest",
        "ListDbSystemsResponse",
    },
)


class DbSystem(proto.Message):
    r"""Details of the DbSystem (BaseDB) resource.
    https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/DbSystem/

    Attributes:
        name (str):
            Identifier. The name of the DbSystem resource in the
            following format:
            projects/{project}/locations/{region}/dbSystems/{db_system}
        properties (google.cloud.oracledatabase_v1.types.DbSystemProperties):
            Optional. The properties of the DbSystem.
        gcp_oracle_zone (str):
            Optional. The GCP Oracle zone where Oracle
            DbSystem is hosted. Example: us-east4-b-r2.
            If not specified, the system will pick a zone
            based on availability.
        labels (MutableMapping[str, str]):
            Optional. The labels or tags associated with
            the DbSystem.
        odb_network (str):
            Optional. The name of the OdbNetwork associated with the
            DbSystem. Format:
            projects/{project}/locations/{location}/odbNetworks/{odb_network}
            It is optional but if specified, this should match the
            parent ODBNetwork of the OdbSubnet.
        odb_subnet (str):
            Required. The name of the OdbSubnet associated with the
            DbSystem for IP allocation. Format:
            projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet}
        entitlement_id (str):
            Output only. The ID of the subscription
            entitlement associated with the DbSystem
        display_name (str):
            Required. The display name for the System db.
            The name does not have to be unique within your
            project.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The date and time that the
            DbSystem was created.
        oci_url (str):
            Output only. HTTPS link to OCI resources
            exposed to Customer via UI Interface.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    properties: "DbSystemProperties" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DbSystemProperties",
    )
    gcp_oracle_zone: str = proto.Field(
        proto.STRING,
        number=3,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    odb_network: str = proto.Field(
        proto.STRING,
        number=5,
    )
    odb_subnet: str = proto.Field(
        proto.STRING,
        number=6,
    )
    entitlement_id: str = proto.Field(
        proto.STRING,
        number=7,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=8,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    oci_url: str = proto.Field(
        proto.STRING,
        number=10,
    )


class DbSystemProperties(proto.Message):
    r"""The properties of a DbSystem.

    Attributes:
        shape (str):
            Required. Shape of DB System.
        compute_count (int):
            Required. The number of CPU cores to enable
            for the DbSystem.
        initial_data_storage_size_gb (int):
            Required. The initial data storage size in
            GB.
        database_edition (google.cloud.oracledatabase_v1.types.DbSystemProperties.DbSystemDatabaseEdition):
            Required. The database edition of the
            DbSystem.
        license_model (google.cloud.oracledatabase_v1.types.DbSystemProperties.LicenseModel):
            Required. The license model of the DbSystem.
        ssh_public_keys (MutableSequence[str]):
            Required. SSH public keys to be stored with
            the DbSystem.
        hostname_prefix (str):
            Optional. Prefix for DB System host names.
        hostname (str):
            Output only. The hostname of the DbSystem.
        private_ip (str):
            Optional. The private IP address of the
            DbSystem.
        data_collection_options (google.cloud.oracledatabase_v1.types.DataCollectionOptionsDbSystem):
            Optional. Data collection options for
            diagnostics.
        time_zone (google.type.datetime_pb2.TimeZone):
            Optional. Time zone of the DbSystem.
        lifecycle_state (google.cloud.oracledatabase_v1.types.DbSystemProperties.DbSystemLifecycleState):
            Output only. State of the DbSystem.
        db_home (google.cloud.oracledatabase_v1.types.DbHome):
            Optional. Details for creating a Database
            Home.
        ocid (str):
            Output only. OCID of the DbSystem.
        memory_size_gb (int):
            Optional. The memory size in GB. This value
            can not be set and is automatically calculated
            based on the number of ECPUs allocated to the
            DbSystem.
        compute_model (google.cloud.oracledatabase_v1.types.DbSystemProperties.ComputeModel):
            Optional. The compute model of the DbSystem.
        data_storage_size_gb (int):
            Optional. The data storage size in GB that is currently
            available to DbSystems. The value is same as
            initial_data_storage_size_gb. This can be modified from OCI
            console.
        reco_storage_size_gb (int):
            Optional. The reco/redo storage size in GB.
            The value for recovery storage size is based on
            the available data storage size.
        domain (str):
            Optional. The host domain name of the
            DbSystem.
        node_count (int):
            Optional. The number of nodes to launch for a
            virtual machine DbSystem. By default this will
            be set to 1.
        db_system_options (google.cloud.oracledatabase_v1.types.DbSystemOptions):
            Optional. The options for the DbSystem.
    """

    class DbSystemDatabaseEdition(proto.Enum):
        r"""The editions available for DbSystem.

        Values:
            DB_SYSTEM_DATABASE_EDITION_UNSPECIFIED (0):
                The database edition is unspecified.
            STANDARD_EDITION (1):
                The database edition is Standard.
            ENTERPRISE_EDITION (2):
                The database edition is Enterprise.
            ENTERPRISE_EDITION_HIGH_PERFORMANCE (3):
                The database edition is Enterprise Edition.
        """

        DB_SYSTEM_DATABASE_EDITION_UNSPECIFIED = 0
        STANDARD_EDITION = 1
        ENTERPRISE_EDITION = 2
        ENTERPRISE_EDITION_HIGH_PERFORMANCE = 3

    class LicenseModel(proto.Enum):
        r"""The license model of the DbSystem.

        Values:
            LICENSE_MODEL_UNSPECIFIED (0):
                The license model is unspecified.
            LICENSE_INCLUDED (1):
                The license model is included.
            BRING_YOUR_OWN_LICENSE (2):
                The license model is bring your own license.
        """

        LICENSE_MODEL_UNSPECIFIED = 0
        LICENSE_INCLUDED = 1
        BRING_YOUR_OWN_LICENSE = 2

    class DbSystemLifecycleState(proto.Enum):
        r"""The various lifecycle states of the DbSystem.

        Values:
            DB_SYSTEM_LIFECYCLE_STATE_UNSPECIFIED (0):
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
            TERMINATING (4):
                Indicates that the resource is in terminating
                state.
            TERMINATED (5):
                Indicates that the resource is in terminated
                state.
            FAILED (6):
                Indicates that the resource is in failed
                state.
            MIGRATED (7):
                Indicates that the resource has been
                migrated.
            MAINTENANCE_IN_PROGRESS (8):
                Indicates that the resource is in maintenance
                in progress state.
            NEEDS_ATTENTION (9):
                Indicates that the resource needs attention.
            UPGRADING (10):
                Indicates that the resource is upgrading.
        """

        DB_SYSTEM_LIFECYCLE_STATE_UNSPECIFIED = 0
        PROVISIONING = 1
        AVAILABLE = 2
        UPDATING = 3
        TERMINATING = 4
        TERMINATED = 5
        FAILED = 6
        MIGRATED = 7
        MAINTENANCE_IN_PROGRESS = 8
        NEEDS_ATTENTION = 9
        UPGRADING = 10

    class ComputeModel(proto.Enum):
        r"""The compute model of the DbSystem.

        Values:
            COMPUTE_MODEL_UNSPECIFIED (0):
                The compute model is unspecified.
            ECPU (1):
                The compute model is virtual.
            OCPU (2):
                Deprecated: This option is not supported.
                Please use ECPU instead. The compute model is
                physical.
        """

        COMPUTE_MODEL_UNSPECIFIED = 0
        ECPU = 1
        OCPU = 2

    shape: str = proto.Field(
        proto.STRING,
        number=1,
    )
    compute_count: int = proto.Field(
        proto.INT32,
        number=2,
    )
    initial_data_storage_size_gb: int = proto.Field(
        proto.INT32,
        number=3,
    )
    database_edition: DbSystemDatabaseEdition = proto.Field(
        proto.ENUM,
        number=4,
        enum=DbSystemDatabaseEdition,
    )
    license_model: LicenseModel = proto.Field(
        proto.ENUM,
        number=5,
        enum=LicenseModel,
    )
    ssh_public_keys: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    hostname_prefix: str = proto.Field(
        proto.STRING,
        number=7,
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=8,
    )
    private_ip: str = proto.Field(
        proto.STRING,
        number=9,
    )
    data_collection_options: "DataCollectionOptionsDbSystem" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="DataCollectionOptionsDbSystem",
    )
    time_zone: datetime_pb2.TimeZone = proto.Field(
        proto.MESSAGE,
        number=11,
        message=datetime_pb2.TimeZone,
    )
    lifecycle_state: DbSystemLifecycleState = proto.Field(
        proto.ENUM,
        number=12,
        enum=DbSystemLifecycleState,
    )
    db_home: "DbHome" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="DbHome",
    )
    ocid: str = proto.Field(
        proto.STRING,
        number=14,
    )
    memory_size_gb: int = proto.Field(
        proto.INT32,
        number=15,
    )
    compute_model: ComputeModel = proto.Field(
        proto.ENUM,
        number=16,
        enum=ComputeModel,
    )
    data_storage_size_gb: int = proto.Field(
        proto.INT32,
        number=17,
    )
    reco_storage_size_gb: int = proto.Field(
        proto.INT32,
        number=18,
    )
    domain: str = proto.Field(
        proto.STRING,
        number=19,
    )
    node_count: int = proto.Field(
        proto.INT32,
        number=20,
    )
    db_system_options: "DbSystemOptions" = proto.Field(
        proto.MESSAGE,
        number=21,
        message="DbSystemOptions",
    )


class DataCollectionOptionsDbSystem(proto.Message):
    r"""Data collection options for DbSystem.

    Attributes:
        is_diagnostics_events_enabled (bool):
            Optional. Indicates whether to enable data
            collection for diagnostics.
        is_incident_logs_enabled (bool):
            Optional. Indicates whether to enable
            incident logs and trace collection.
    """

    is_diagnostics_events_enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    is_incident_logs_enabled: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class DbSystemOptions(proto.Message):
    r"""Details of the DbSystem Options.

    Attributes:
        storage_management (google.cloud.oracledatabase_v1.types.DbSystemOptions.StorageManagement):
            Optional. The storage option used in DB
            system.
    """

    class StorageManagement(proto.Enum):
        r"""The storage option used in DB system.

        Values:
            STORAGE_MANAGEMENT_UNSPECIFIED (0):
                The storage management is unspecified.
            ASM (1):
                Automatic storage management. This option is
                not supported. Only LVM is supported.
            LVM (2):
                Logical Volume management.
        """

        STORAGE_MANAGEMENT_UNSPECIFIED = 0
        ASM = 1
        LVM = 2

    storage_management: StorageManagement = proto.Field(
        proto.ENUM,
        number=1,
        enum=StorageManagement,
    )


class DbHome(proto.Message):
    r"""Details of the Database Home resource.

    Attributes:
        display_name (str):
            Optional. The display name for the Database
            Home. The name does not have to be unique within
            your project.
        db_version (str):
            Required. A valid Oracle Database version.
            For a list of supported versions, use the
            ListDbVersions operation.
        database (google.cloud.oracledatabase_v1.types.Database):
            Required. The Database resource.
        is_unified_auditing_enabled (bool):
            Optional. Whether unified auditing is enabled
            for the Database Home.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    db_version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    database: gco_database.Database = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gco_database.Database,
    )
    is_unified_auditing_enabled: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class CreateDbSystemRequest(proto.Message):
    r"""The request for ``DbSystem.Create``.

    Attributes:
        parent (str):
            Required. The value for parent of the
            DbSystem in the following format:
            projects/{project}/locations/{location}.
        db_system_id (str):
            Required. The ID of the DbSystem to create. This value is
            restricted to (^\ `a-z <[a-z0-9-]{0,61}[a-z0-9]>`__?$) and
            must be a maximum of 63 characters in length. The value must
            start with a letter and end with a letter or a number.
        db_system (google.cloud.oracledatabase_v1.types.DbSystem):
            Required. The resource being created.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    db_system_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    db_system: "DbSystem" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DbSystem",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteDbSystemRequest(proto.Message):
    r"""The request for ``DbSystem.Delete``.

    Attributes:
        name (str):
            Required. The name of the DbSystem in the following format:
            projects/{project}/locations/{location}/dbSystems/{db_system}.
        request_id (str):
            Optional. An optional ID to identify the
            request. This value is used to identify
            duplicate requests. If you make a request with
            the same request ID and the original request is
            still in progress or completed, the server
            ignores the second request. This prevents
            clients from accidentally creating duplicate
            commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetDbSystemRequest(proto.Message):
    r"""The request for ``DbSystem.Get``.

    Attributes:
        name (str):
            Required. The name of the DbSystem in the following format:
            projects/{project}/locations/{location}/dbSystems/{db_system}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDbSystemsRequest(proto.Message):
    r"""The request for ``DbSystem.List``.

    Attributes:
        parent (str):
            Required. The parent value for DbSystems in
            the following format:
            projects/{project}/locations/{location}.
        page_size (int):
            Optional. The maximum number of items to
            return. If unspecified, at most 50 DbSystems
            will be returned. The maximum value is 1000;
            values above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. An expression for filtering the
            results of the request.
        order_by (str):
            Optional. An expression for ordering the
            results of the request.
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
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListDbSystemsResponse(proto.Message):
    r"""The response for ``DbSystem.List``.

    Attributes:
        db_systems (MutableSequence[google.cloud.oracledatabase_v1.types.DbSystem]):
            The list of DbSystems.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Unreachable locations when listing resources
            across all locations using wildcard location
            '-'.
    """

    @property
    def raw_page(self):
        return self

    db_systems: MutableSequence["DbSystem"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DbSystem",
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
