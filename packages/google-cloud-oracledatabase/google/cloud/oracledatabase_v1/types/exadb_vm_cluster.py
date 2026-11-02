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

from google.cloud.oracledatabase_v1.types import common

__protobuf__ = proto.module(
    package="google.cloud.oracledatabase.v1",
    manifest={
        "ExadbVmCluster",
        "ExadbVmClusterStorageDetails",
        "ExadbVmClusterProperties",
    },
)


class ExadbVmCluster(proto.Message):
    r"""ExadbVmCluster represents a cluster of VMs that are used to
    run Exadata workloads.
    https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/ExadbVmCluster/

    Attributes:
        name (str):
            Identifier. The name of the ExadbVmCluster resource in the
            following format:
            projects/{project}/locations/{region}/exadbVmClusters/{exadb_vm_cluster}
        properties (google.cloud.oracledatabase_v1.types.ExadbVmClusterProperties):
            Required. The properties of the
            ExadbVmCluster.
        gcp_oracle_zone (str):
            Output only. Immutable. The GCP Oracle zone
            where Oracle ExadbVmCluster is hosted. Example:
            us-east4-b-r2. During creation, the system will
            pick the zone assigned to the
            ExascaleDbStorageVault.
        labels (MutableMapping[str, str]):
            Optional. The labels or tags associated with
            the ExadbVmCluster.
        odb_network (str):
            Optional. Immutable. The name of the OdbNetwork associated
            with the ExadbVmCluster. Format:
            projects/{project}/locations/{location}/odbNetworks/{odb_network}
            It is optional but if specified, this should match the
            parent ODBNetwork of the OdbSubnet.
        odb_subnet (str):
            Required. Immutable. The name of the OdbSubnet associated
            with the ExadbVmCluster for IP allocation. Format:
            projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet}
        backup_odb_subnet (str):
            Required. Immutable. The name of the backup OdbSubnet
            associated with the ExadbVmCluster. Format:
            projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet}
        display_name (str):
            Required. Immutable. The display name for the
            ExadbVmCluster. The name does not have to be
            unique within your project. The name must be
            1-255 characters long and can only contain
            alphanumeric characters.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The date and time that the
            ExadbVmCluster was created.
        entitlement_id (str):
            Output only. The ID of the subscription
            entitlement associated with the ExadbVmCluster.
        identity_connector (google.cloud.oracledatabase_v1.types.IdentityConnector):
            Output only. The identity connector details
            which will allow OCI to securely access the
            resources in the customer project.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    properties: "ExadbVmClusterProperties" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ExadbVmClusterProperties",
    )
    gcp_oracle_zone: str = proto.Field(
        proto.STRING,
        number=3,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    odb_network: str = proto.Field(
        proto.STRING,
        number=6,
    )
    odb_subnet: str = proto.Field(
        proto.STRING,
        number=7,
    )
    backup_odb_subnet: str = proto.Field(
        proto.STRING,
        number=8,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=9,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    entitlement_id: str = proto.Field(
        proto.STRING,
        number=11,
    )
    identity_connector: common.IdentityConnector = proto.Field(
        proto.MESSAGE,
        number=12,
        message=common.IdentityConnector,
    )


class ExadbVmClusterStorageDetails(proto.Message):
    r"""The storage allocation for the exadbvmcluster, in gigabytes
    (GB).

    Attributes:
        size_in_gbs_per_node (int):
            Required. The storage allocation for the
            exadbvmcluster per node, in gigabytes (GB). This
            field is used to calculate the total storage
            allocation for the exadbvmcluster.
    """

    size_in_gbs_per_node: int = proto.Field(
        proto.INT32,
        number=2,
    )


class ExadbVmClusterProperties(proto.Message):
    r"""The properties of an ExadbVmCluster.

    Attributes:
        cluster_name (str):
            Optional. Immutable. The cluster name for Exascale vm
            cluster. The cluster name must begin with an alphabetic
            character and may contain hyphens(-) but can not contain
            underscores(\_). It should be not more than 11 characters
            and is not case sensitive. OCI Cluster name.
        grid_image_id (str):
            Required. Immutable. Grid Infrastructure
            Version.
        node_count (int):
            Required. The number of nodes/VMs in the
            ExadbVmCluster.
        enabled_ecpu_count_per_node (int):
            Required. Immutable. The number of ECPUs
            enabled per node for an exadata vm cluster on
            exascale infrastructure.
        additional_ecpu_count_per_node (int):
            Optional. Immutable. The number of additional
            ECPUs per node for an Exadata VM cluster on
            exascale infrastructure.
        vm_file_system_storage (google.cloud.oracledatabase_v1.types.ExadbVmClusterStorageDetails):
            Required. Immutable. Total storage details
            for the ExadbVmCluster.
        license_model (google.cloud.oracledatabase_v1.types.ExadbVmClusterProperties.LicenseModel):
            Optional. Immutable. The license type of the
            ExadbVmCluster.
        exascale_db_storage_vault (str):
            Required. Immutable. The name of ExascaleDbStorageVault
            associated with the ExadbVmCluster. It can refer to an
            existing ExascaleDbStorageVault. Or a new one can be created
            during the ExadbVmCluster creation (requires
            storage_vault_properties to be set). Format:
            projects/{project}/locations/{location}/exascaleDbStorageVaults/{exascale_db_storage_vault}
        hostname_prefix (str):
            Required. Immutable. Prefix for VM cluster
            host names.
        hostname (str):
            Output only. The hostname of the
            ExadbVmCluster.
        ssh_public_keys (MutableSequence[str]):
            Required. Immutable. The SSH public keys for
            the ExadbVmCluster.
        data_collection_options (google.cloud.oracledatabase_v1.types.DataCollectionOptionsCommon):
            Optional. Immutable. Indicates user
            preference for data collection options.
        time_zone (google.type.datetime_pb2.TimeZone):
            Optional. Immutable. The time zone of the
            ExadbVmCluster.
        lifecycle_state (google.cloud.oracledatabase_v1.types.ExadbVmClusterProperties.ExadbVmClusterLifecycleState):
            Output only. State of the cluster.
        shape_attribute (google.cloud.oracledatabase_v1.types.ExadbVmClusterProperties.ShapeAttribute):
            Required. Immutable. The shape attribute of the VM cluster.
            The type of Exascale storage used for Exadata VM cluster.
            The default is SMART_STORAGE which supports Oracle Database
            23ai and later
        memory_size_gb (int):
            Output only. Memory per VM (GB) (Read-only):
            Shows the amount of memory allocated to each VM.
            Memory is calculated based on 2.75 GB per Total
            ECPUs.
        scan_listener_port_tcp (int):
            Optional. Immutable. SCAN listener port - TCP
        oci_uri (str):
            Output only. Deep link to the OCI console to
            view this resource.
        gi_version (str):
            Output only. The Oracle Grid Infrastructure
            (GI) software version.
    """

    class LicenseModel(proto.Enum):
        r"""The Oracle license model that applies to the ExaScale VM
        cluster

        Values:
            LICENSE_MODEL_UNSPECIFIED (0):
                Unspecified.
            LICENSE_INCLUDED (1):
                Default is license included.
            BRING_YOUR_OWN_LICENSE (2):
                Bring your own license.
        """

        LICENSE_MODEL_UNSPECIFIED = 0
        LICENSE_INCLUDED = 1
        BRING_YOUR_OWN_LICENSE = 2

    class ExadbVmClusterLifecycleState(proto.Enum):
        r"""The various lifecycle states of the VM cluster.

        Values:
            EXADB_VM_CLUSTER_LIFECYCLE_STATE_UNSPECIFIED (0):
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
            MAINTENANCE_IN_PROGRESS (7):
                Indicates that the resource is in maintenance
                in progress state.
        """

        EXADB_VM_CLUSTER_LIFECYCLE_STATE_UNSPECIFIED = 0
        PROVISIONING = 1
        AVAILABLE = 2
        UPDATING = 3
        TERMINATING = 4
        TERMINATED = 5
        FAILED = 6
        MAINTENANCE_IN_PROGRESS = 7

    class ShapeAttribute(proto.Enum):
        r"""The shape attribute of the VM cluster. The type of Exascale storage
        used for Exadata VM cluster. The default is SMART_STORAGE which
        supports Oracle Database 23ai and later

        Values:
            SHAPE_ATTRIBUTE_UNSPECIFIED (0):
                Default unspecified value.
            SMART_STORAGE (1):
                Indicates that the resource is in smart
                storage.
            BLOCK_STORAGE (2):
                Indicates that the resource is in block
                storage.
        """

        SHAPE_ATTRIBUTE_UNSPECIFIED = 0
        SMART_STORAGE = 1
        BLOCK_STORAGE = 2

    cluster_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    grid_image_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    node_count: int = proto.Field(
        proto.INT32,
        number=3,
    )
    enabled_ecpu_count_per_node: int = proto.Field(
        proto.INT32,
        number=20,
    )
    additional_ecpu_count_per_node: int = proto.Field(
        proto.INT32,
        number=21,
    )
    vm_file_system_storage: "ExadbVmClusterStorageDetails" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="ExadbVmClusterStorageDetails",
    )
    license_model: LicenseModel = proto.Field(
        proto.ENUM,
        number=7,
        enum=LicenseModel,
    )
    exascale_db_storage_vault: str = proto.Field(
        proto.STRING,
        number=8,
    )
    hostname_prefix: str = proto.Field(
        proto.STRING,
        number=9,
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=10,
    )
    ssh_public_keys: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=11,
    )
    data_collection_options: common.DataCollectionOptionsCommon = proto.Field(
        proto.MESSAGE,
        number=12,
        message=common.DataCollectionOptionsCommon,
    )
    time_zone: datetime_pb2.TimeZone = proto.Field(
        proto.MESSAGE,
        number=13,
        message=datetime_pb2.TimeZone,
    )
    lifecycle_state: ExadbVmClusterLifecycleState = proto.Field(
        proto.ENUM,
        number=14,
        enum=ExadbVmClusterLifecycleState,
    )
    shape_attribute: ShapeAttribute = proto.Field(
        proto.ENUM,
        number=15,
        enum=ShapeAttribute,
    )
    memory_size_gb: int = proto.Field(
        proto.INT32,
        number=16,
    )
    scan_listener_port_tcp: int = proto.Field(
        proto.INT32,
        number=17,
    )
    oci_uri: str = proto.Field(
        proto.STRING,
        number=18,
    )
    gi_version: str = proto.Field(
        proto.STRING,
        number=19,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
