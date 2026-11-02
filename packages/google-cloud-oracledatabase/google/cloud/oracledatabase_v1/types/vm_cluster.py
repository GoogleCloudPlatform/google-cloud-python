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
        "CloudVmCluster",
        "CloudVmClusterProperties",
        "DataCollectionOptions",
    },
)


class CloudVmCluster(proto.Message):
    r"""Details of the Cloud VM Cluster resource.
    https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/CloudVmCluster/

    Attributes:
        name (str):
            Identifier. The name of the VM Cluster resource with the
            format:
            projects/{project}/locations/{region}/cloudVmClusters/{cloud_vm_cluster}
        exadata_infrastructure (str):
            Required. The name of the Exadata Infrastructure resource on
            which VM cluster resource is created, in the following
            format:
            projects/{project}/locations/{region}/cloudExadataInfrastuctures/{cloud_extradata_infrastructure}
        display_name (str):
            Optional. User friendly name for this
            resource.
        properties (google.cloud.oracledatabase_v1.types.CloudVmClusterProperties):
            Optional. Various properties of the VM
            Cluster.
        labels (MutableMapping[str, str]):
            Optional. Labels or tags associated with the
            VM Cluster.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The date and time that the VM
            cluster was created.
        cidr (str):
            Optional. Network settings. CIDR to use for
            cluster IP allocation.
        backup_subnet_cidr (str):
            Optional. CIDR range of the backup subnet.
        network (str):
            Optional. The name of the VPC network.
            Format:
            projects/{project}/global/networks/{network}
        gcp_oracle_zone (str):
            Output only. The GCP Oracle zone where Oracle CloudVmCluster
            is hosted. This will be the same as the gcp_oracle_zone of
            the CloudExadataInfrastructure. Example: us-east4-b-r2.
        odb_network (str):
            Optional. The name of the OdbNetwork associated with the VM
            Cluster. Format:
            projects/{project}/locations/{location}/odbNetworks/{odb_network}
            It is optional but if specified, this should match the
            parent ODBNetwork of the odb_subnet and backup_odb_subnet.
        odb_subnet (str):
            Optional. The name of the OdbSubnet associated with the VM
            Cluster for IP allocation. Format:
            projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet}
        backup_odb_subnet (str):
            Optional. The name of the backup OdbSubnet associated with
            the VM Cluster. Format:
            projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbSubnets/{odb_subnet}
        odb_dns_zone (str):
            Optional. Immutable. The name of the OdbDnsZone for using
            custom domain name for the VM Cluster. Format:
            projects/{project}/locations/{location}/odbNetworks/{odb_network}/odbDnsZones/{odb_dns_zone}
        identity_connector (google.cloud.oracledatabase_v1.types.IdentityConnector):
            Output only. The identity connector details
            which will allow OCI to securely access the
            resources in the customer project.
        exascale_db_storage_vault (str):
            Optional. The name of ExascaleDbStorageVault associated with
            the VM Cluster. Format:
            projects/{project}/locations/{location}/exascaleDbStorageVaults/{exascale_db_storage_vault}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    exadata_infrastructure: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    properties: "CloudVmClusterProperties" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="CloudVmClusterProperties",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    cidr: str = proto.Field(
        proto.STRING,
        number=9,
    )
    backup_subnet_cidr: str = proto.Field(
        proto.STRING,
        number=10,
    )
    network: str = proto.Field(
        proto.STRING,
        number=11,
    )
    gcp_oracle_zone: str = proto.Field(
        proto.STRING,
        number=12,
    )
    odb_network: str = proto.Field(
        proto.STRING,
        number=13,
    )
    odb_subnet: str = proto.Field(
        proto.STRING,
        number=14,
    )
    backup_odb_subnet: str = proto.Field(
        proto.STRING,
        number=15,
    )
    odb_dns_zone: str = proto.Field(
        proto.STRING,
        number=18,
    )
    identity_connector: common.IdentityConnector = proto.Field(
        proto.MESSAGE,
        number=16,
        message=common.IdentityConnector,
    )
    exascale_db_storage_vault: str = proto.Field(
        proto.STRING,
        number=17,
    )


class CloudVmClusterProperties(proto.Message):
    r"""Various properties and settings associated with Exadata VM
    cluster.

    Attributes:
        ocid (str):
            Output only. Oracle Cloud Infrastructure ID
            of VM Cluster.
        license_type (google.cloud.oracledatabase_v1.types.CloudVmClusterProperties.LicenseType):
            Required. License type of VM Cluster.
        gi_version (str):
            Optional. Grid Infrastructure Version.
        time_zone (google.type.datetime_pb2.TimeZone):
            Optional. Time zone of VM Cluster to set.
            Defaults to UTC if not specified.
        ssh_public_keys (MutableSequence[str]):
            Optional. SSH public keys to be stored with
            cluster.
        node_count (int):
            Optional. Number of database servers.
        shape (str):
            Output only. Shape of VM Cluster.
        ocpu_count (float):
            Optional. OCPU count per VM. Minimum is 0.1.
        memory_size_gb (int):
            Optional. Memory allocated in GBs.
        db_node_storage_size_gb (int):
            Optional. Local storage per VM.
        storage_size_gb (int):
            Output only. The storage allocation for the
            disk group, in gigabytes (GB).
        data_storage_size_tb (float):
            Optional. The data disk group size to be
            allocated in TBs.
        disk_redundancy (google.cloud.oracledatabase_v1.types.CloudVmClusterProperties.DiskRedundancy):
            Optional. The type of redundancy.
        sparse_diskgroup_enabled (bool):
            Optional. Use exadata sparse snapshots.
        local_backup_enabled (bool):
            Optional. Use local backup.
        hostname_prefix (str):
            Optional. Prefix for VM cluster host names.
        diagnostics_data_collection_options (google.cloud.oracledatabase_v1.types.DataCollectionOptions):
            Optional. Data collection options for
            diagnostics.
        state (google.cloud.oracledatabase_v1.types.CloudVmClusterProperties.State):
            Output only. State of the cluster.
        scan_listener_port_tcp (int):
            Optional. SCAN listener port - TCP
        scan_listener_port_tcp_ssl (int):
            Optional. SCAN listener port - TLS
        domain (str):
            Output only. Parent DNS domain where SCAN DNS
            and hosts names are qualified. ex:
            ocispdelegated.ocisp10jvnet.oraclevcn.com
        scan_dns (str):
            Output only. SCAN DNS name.
            ex:
            sp2-yi0xq-scan.ocispdelegated.ocisp10jvnet.oraclevcn.com
        hostname (str):
            Output only. host name without domain. format:
            "<hostname_prefix>-" with some suffix. ex: sp2-yi0xq where
            "sp2" is the hostname_prefix.
        cpu_core_count (int):
            Required. Number of enabled CPU cores.
        system_version (str):
            Optional. Operating system version of the
            image.
        scan_ip_ids (MutableSequence[str]):
            Output only. OCIDs of scan IPs.
        scan_dns_record_id (str):
            Output only. OCID of scan DNS record.
        oci_url (str):
            Output only. Deep link to the OCI console to
            view this resource.
        db_server_ocids (MutableSequence[str]):
            Optional. OCID of database servers.
        compartment_id (str):
            Output only. Compartment ID of cluster.
        dns_listener_ip (str):
            Output only. DNS listener IP.
        cluster_name (str):
            Optional. OCI Cluster name.
        compute_model (google.cloud.oracledatabase_v1.types.ComputeModel):
            Output only. The compute model of the VM
            Cluster.
        storage_management_type (google.cloud.oracledatabase_v1.types.CloudVmClusterProperties.StorageManagementType):
            Output only. The storage management type of
            the VM Cluster.
        vm_file_system_storage_type (google.cloud.oracledatabase_v1.types.CloudVmClusterProperties.VmFileSystemStorageType):
            Optional. Specifies whether VM file system
            storage / VM images are stored on local DB
            server storage or Exascale storage.
        vm_backup_storage_type (google.cloud.oracledatabase_v1.types.CloudVmClusterProperties.VmBackupStorageType):
            Optional. Specifies whether VM backups are
            stored on local DB server storage or Exascale
            storage.
    """

    class LicenseType(proto.Enum):
        r"""Different licenses supported.

        Values:
            LICENSE_TYPE_UNSPECIFIED (0):
                Unspecified
            LICENSE_INCLUDED (1):
                License included part of offer
            BRING_YOUR_OWN_LICENSE (2):
                Bring your own license
        """

        LICENSE_TYPE_UNSPECIFIED = 0
        LICENSE_INCLUDED = 1
        BRING_YOUR_OWN_LICENSE = 2

    class DiskRedundancy(proto.Enum):
        r"""Types of disk redundancy provided by Oracle.

        Values:
            DISK_REDUNDANCY_UNSPECIFIED (0):
                Unspecified.
            HIGH (1):
                High -  3 way mirror.
            NORMAL (2):
                Normal - 2 way mirror.
        """

        DISK_REDUNDANCY_UNSPECIFIED = 0
        HIGH = 1
        NORMAL = 2

    class State(proto.Enum):
        r"""The various lifecycle states of the VM cluster.

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

        STATE_UNSPECIFIED = 0
        PROVISIONING = 1
        AVAILABLE = 2
        UPDATING = 3
        TERMINATING = 4
        TERMINATED = 5
        FAILED = 6
        MAINTENANCE_IN_PROGRESS = 7

    class StorageManagementType(proto.Enum):
        r"""The type of storage management for the Cloud VM Cluster.

        Values:
            STORAGE_MANAGEMENT_TYPE_UNSPECIFIED (0):
                Unspecified storage management type.
            ASM (1):
                Automatic Storage Management.
            EXASCALE (2):
                Exascale storage management.
        """

        STORAGE_MANAGEMENT_TYPE_UNSPECIFIED = 0
        ASM = 1
        EXASCALE = 2

    class VmFileSystemStorageType(proto.Enum):
        r"""Storage types for VM File System.

        Values:
            VM_FILE_SYSTEM_STORAGE_TYPE_UNSPECIFIED (0):
                Unspecified storage type.
            VM_FILE_SYSTEM_STORAGE_TYPE_LOCAL (1):
                Local DB server storage.
            VM_FILE_SYSTEM_STORAGE_TYPE_EXASCALE (2):
                Exascale storage.
        """

        VM_FILE_SYSTEM_STORAGE_TYPE_UNSPECIFIED = 0
        VM_FILE_SYSTEM_STORAGE_TYPE_LOCAL = 1
        VM_FILE_SYSTEM_STORAGE_TYPE_EXASCALE = 2

    class VmBackupStorageType(proto.Enum):
        r"""Storage types for VM Backup.

        Values:
            VM_BACKUP_STORAGE_TYPE_UNSPECIFIED (0):
                Unspecified storage type.
            VM_BACKUP_STORAGE_TYPE_LOCAL (1):
                Local DB server storage.
            VM_BACKUP_STORAGE_TYPE_EXASCALE (2):
                Exascale storage.
        """

        VM_BACKUP_STORAGE_TYPE_UNSPECIFIED = 0
        VM_BACKUP_STORAGE_TYPE_LOCAL = 1
        VM_BACKUP_STORAGE_TYPE_EXASCALE = 2

    ocid: str = proto.Field(
        proto.STRING,
        number=1,
    )
    license_type: LicenseType = proto.Field(
        proto.ENUM,
        number=2,
        enum=LicenseType,
    )
    gi_version: str = proto.Field(
        proto.STRING,
        number=3,
    )
    time_zone: datetime_pb2.TimeZone = proto.Field(
        proto.MESSAGE,
        number=4,
        message=datetime_pb2.TimeZone,
    )
    ssh_public_keys: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    node_count: int = proto.Field(
        proto.INT32,
        number=6,
    )
    shape: str = proto.Field(
        proto.STRING,
        number=7,
    )
    ocpu_count: float = proto.Field(
        proto.FLOAT,
        number=8,
    )
    memory_size_gb: int = proto.Field(
        proto.INT32,
        number=9,
    )
    db_node_storage_size_gb: int = proto.Field(
        proto.INT32,
        number=10,
    )
    storage_size_gb: int = proto.Field(
        proto.INT32,
        number=11,
    )
    data_storage_size_tb: float = proto.Field(
        proto.DOUBLE,
        number=12,
    )
    disk_redundancy: DiskRedundancy = proto.Field(
        proto.ENUM,
        number=13,
        enum=DiskRedundancy,
    )
    sparse_diskgroup_enabled: bool = proto.Field(
        proto.BOOL,
        number=14,
    )
    local_backup_enabled: bool = proto.Field(
        proto.BOOL,
        number=15,
    )
    hostname_prefix: str = proto.Field(
        proto.STRING,
        number=16,
    )
    diagnostics_data_collection_options: "DataCollectionOptions" = proto.Field(
        proto.MESSAGE,
        number=19,
        message="DataCollectionOptions",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=20,
        enum=State,
    )
    scan_listener_port_tcp: int = proto.Field(
        proto.INT32,
        number=21,
    )
    scan_listener_port_tcp_ssl: int = proto.Field(
        proto.INT32,
        number=22,
    )
    domain: str = proto.Field(
        proto.STRING,
        number=23,
    )
    scan_dns: str = proto.Field(
        proto.STRING,
        number=24,
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=25,
    )
    cpu_core_count: int = proto.Field(
        proto.INT32,
        number=26,
    )
    system_version: str = proto.Field(
        proto.STRING,
        number=27,
    )
    scan_ip_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=28,
    )
    scan_dns_record_id: str = proto.Field(
        proto.STRING,
        number=29,
    )
    oci_url: str = proto.Field(
        proto.STRING,
        number=30,
    )
    db_server_ocids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=31,
    )
    compartment_id: str = proto.Field(
        proto.STRING,
        number=32,
    )
    dns_listener_ip: str = proto.Field(
        proto.STRING,
        number=35,
    )
    cluster_name: str = proto.Field(
        proto.STRING,
        number=36,
    )
    compute_model: common.ComputeModel = proto.Field(
        proto.ENUM,
        number=37,
        enum=common.ComputeModel,
    )
    storage_management_type: StorageManagementType = proto.Field(
        proto.ENUM,
        number=38,
        enum=StorageManagementType,
    )
    vm_file_system_storage_type: VmFileSystemStorageType = proto.Field(
        proto.ENUM,
        number=39,
        enum=VmFileSystemStorageType,
    )
    vm_backup_storage_type: VmBackupStorageType = proto.Field(
        proto.ENUM,
        number=40,
        enum=VmBackupStorageType,
    )


class DataCollectionOptions(proto.Message):
    r"""Data collection options for diagnostics.

    Attributes:
        diagnostics_events_enabled (bool):
            Optional. Indicates whether diagnostic
            collection is enabled for the VM cluster
        health_monitoring_enabled (bool):
            Optional. Indicates whether health monitoring
            is enabled for the VM cluster
        incident_logs_enabled (bool):
            Optional. Indicates whether incident logs and
            trace collection are enabled for the VM cluster
    """

    diagnostics_events_enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    health_monitoring_enabled: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    incident_logs_enabled: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
