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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.bare_metal_solution_v2.types import common, network

__protobuf__ = proto.module(
    package="google.cloud.baremetalsolution.v2",
    manifest={
        "ProvisioningConfig",
        "SubmitProvisioningConfigRequest",
        "SubmitProvisioningConfigResponse",
        "ProvisioningQuota",
        "ListProvisioningQuotasRequest",
        "ListProvisioningQuotasResponse",
        "InstanceConfig",
        "VolumeConfig",
        "NetworkConfig",
        "InstanceQuota",
        "GetProvisioningConfigRequest",
        "CreateProvisioningConfigRequest",
        "UpdateProvisioningConfigRequest",
    },
)


class ProvisioningConfig(proto.Message):
    r"""A provisioning configuration.

    Attributes:
        name (str):
            Output only. The system-generated name of the
            provisioning config. This follows the UUID
            format.
        instances (MutableSequence[google.cloud.bare_metal_solution_v2.types.InstanceConfig]):
            Instances to be created.
        networks (MutableSequence[google.cloud.bare_metal_solution_v2.types.NetworkConfig]):
            Networks to be created.
        volumes (MutableSequence[google.cloud.bare_metal_solution_v2.types.VolumeConfig]):
            Volumes to be created.
        ticket_id (str):
            A generated ticket id to track provisioning
            request.
        handover_service_account (str):
            A service account to enable customers to
            access instance credentials upon handover.
        email (str):
            Email provided to send a confirmation with
            provisioning config to. Deprecated in favour of
            email field in request messages.
        state (google.cloud.bare_metal_solution_v2.types.ProvisioningConfig.State):
            Output only. State of ProvisioningConfig.
        location (str):
            Optional. Location name of this
            ProvisioningConfig. It is optional only for
            Intake UI transition period.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last update timestamp.
        cloud_console_uri (str):
            Output only. URI to Cloud Console UI view of
            this provisioning config.
        vpc_sc_enabled (bool):
            If true, VPC SC is enabled for the cluster.
        status_message (str):
            Optional status messages associated with the
            FAILED state.
        custom_id (str):
            Optional. The user-defined identifier of the
            provisioning config.
    """

    class State(proto.Enum):
        r"""The possible states for this ProvisioningConfig.

        Values:
            STATE_UNSPECIFIED (0):
                State wasn't specified.
            DRAFT (1):
                ProvisioningConfig is a draft and can be
                freely modified.
            SUBMITTED (2):
                ProvisioningConfig was already submitted and
                cannot be modified.
            PROVISIONING (3):
                ProvisioningConfig was in the provisioning
                state.  Initially this state comes from the work
                order table in big query when SNOW is used.
                Later this field can be set by the work order
                API.
            PROVISIONED (4):
                ProvisioningConfig was provisioned, meaning
                the resources exist.
            VALIDATED (5):
                ProvisioningConfig was validated.  A
                validation tool will be run to set this state.
            CANCELLED (6):
                ProvisioningConfig was canceled.
            FAILED (7):
                The request is submitted for provisioning,
                with error return.
        """

        STATE_UNSPECIFIED = 0
        DRAFT = 1
        SUBMITTED = 2
        PROVISIONING = 3
        PROVISIONED = 4
        VALIDATED = 5
        CANCELLED = 6
        FAILED = 7

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instances: MutableSequence["InstanceConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="InstanceConfig",
    )
    networks: MutableSequence["NetworkConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="NetworkConfig",
    )
    volumes: MutableSequence["VolumeConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="VolumeConfig",
    )
    ticket_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    handover_service_account: str = proto.Field(
        proto.STRING,
        number=6,
    )
    email: str = proto.Field(
        proto.STRING,
        number=7,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=8,
        enum=State,
    )
    location: str = proto.Field(
        proto.STRING,
        number=9,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    cloud_console_uri: str = proto.Field(
        proto.STRING,
        number=11,
    )
    vpc_sc_enabled: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    status_message: str = proto.Field(
        proto.STRING,
        number=13,
    )
    custom_id: str = proto.Field(
        proto.STRING,
        number=14,
    )


class SubmitProvisioningConfigRequest(proto.Message):
    r"""Request for SubmitProvisioningConfig.

    Attributes:
        parent (str):
            Required. The parent project and location
            containing the ProvisioningConfig.
        provisioning_config (google.cloud.bare_metal_solution_v2.types.ProvisioningConfig):
            Required. The ProvisioningConfig to create.
        email (str):
            Optional. Email provided to send a
            confirmation with provisioning config to.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    provisioning_config: "ProvisioningConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ProvisioningConfig",
    )
    email: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SubmitProvisioningConfigResponse(proto.Message):
    r"""Response for SubmitProvisioningConfig.

    Attributes:
        provisioning_config (google.cloud.bare_metal_solution_v2.types.ProvisioningConfig):
            The submitted provisioning config.
    """

    provisioning_config: "ProvisioningConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ProvisioningConfig",
    )


class ProvisioningQuota(proto.Message):
    r"""A provisioning quota for a given project.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. The name of the provisioning
            quota.
        asset_type (google.cloud.bare_metal_solution_v2.types.ProvisioningQuota.AssetType):
            The asset type of this provisioning quota.
        gcp_service (str):
            The gcp service of the provisioning quota.
        location (str):
            The specific location of the provisioining
            quota.
        available_count (int):
            The available count of the provisioning
            quota.
        instance_quota (google.cloud.bare_metal_solution_v2.types.InstanceQuota):
            Instance quota.

            This field is a member of `oneof`_ ``quota``.
        server_count (int):
            Server count.

            This field is a member of `oneof`_ ``availability``.
        network_bandwidth (int):
            Network bandwidth, Gbps

            This field is a member of `oneof`_ ``availability``.
        storage_gib (int):
            Storage size (GB).

            This field is a member of `oneof`_ ``availability``.
    """

    class AssetType(proto.Enum):
        r"""The available asset types for intake.

        Values:
            ASSET_TYPE_UNSPECIFIED (0):
                The unspecified type.
            ASSET_TYPE_SERVER (1):
                The server asset type.
            ASSET_TYPE_STORAGE (2):
                The storage asset type.
            ASSET_TYPE_NETWORK (3):
                The network asset type.
        """

        ASSET_TYPE_UNSPECIFIED = 0
        ASSET_TYPE_SERVER = 1
        ASSET_TYPE_STORAGE = 2
        ASSET_TYPE_NETWORK = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    asset_type: AssetType = proto.Field(
        proto.ENUM,
        number=2,
        enum=AssetType,
    )
    gcp_service: str = proto.Field(
        proto.STRING,
        number=3,
    )
    location: str = proto.Field(
        proto.STRING,
        number=4,
    )
    available_count: int = proto.Field(
        proto.INT32,
        number=5,
    )
    instance_quota: "InstanceQuota" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="quota",
        message="InstanceQuota",
    )
    server_count: int = proto.Field(
        proto.INT64,
        number=7,
        oneof="availability",
    )
    network_bandwidth: int = proto.Field(
        proto.INT64,
        number=8,
        oneof="availability",
    )
    storage_gib: int = proto.Field(
        proto.INT64,
        number=9,
        oneof="availability",
    )


class ListProvisioningQuotasRequest(proto.Message):
    r"""Message for requesting the list of provisioning quotas.

    Attributes:
        parent (str):
            Required. Parent value for
            ListProvisioningQuotasRequest.
        page_size (int):
            Requested page size. The server might return fewer items
            than requested. If unspecified, server will pick an
            appropriate default. Notice that page_size field is not
            supported and won't be respected in the API request for now,
            will be updated when pagination is supported.
        page_token (str):
            A token identifying a page of results from
            the server.
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


class ListProvisioningQuotasResponse(proto.Message):
    r"""Response message for the list of provisioning quotas.

    Attributes:
        provisioning_quotas (MutableSequence[google.cloud.bare_metal_solution_v2.types.ProvisioningQuota]):
            The provisioning quotas registered in this
            project.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    provisioning_quotas: MutableSequence["ProvisioningQuota"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ProvisioningQuota",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class InstanceConfig(proto.Message):
    r"""Configuration parameters for a new instance.

    Attributes:
        name (str):
            Output only. The name of the instance config.
        id (str):
            A transient unique identifier to idenfity an
            instance within an ProvisioningConfig request.
        instance_type (str):
            Instance type. `Available
            types <https://cloud.google.com/bare-metal/docs/bms-planning#server_configurations>`__
        hyperthreading (bool):
            Whether the instance should be provisioned
            with Hyperthreading enabled.
        os_image (str):
            OS image to initialize the instance. `Available
            images <https://cloud.google.com/bare-metal/docs/bms-planning#server_configurations>`__
        client_network (google.cloud.bare_metal_solution_v2.types.InstanceConfig.NetworkAddress):
            Client network address. Filled if
            InstanceConfig.multivlan_config is false.
        private_network (google.cloud.bare_metal_solution_v2.types.InstanceConfig.NetworkAddress):
            Private network address, if any. Filled if
            InstanceConfig.multivlan_config is false.
        user_note (str):
            User note field, it can be used by customers
            to add additional information for the BMS Ops
            team .
        account_networks_enabled (bool):
            If true networks can be from different
            projects of the same vendor account.
        network_config (google.cloud.bare_metal_solution_v2.types.InstanceConfig.NetworkConfig):
            The type of network configuration on the
            instance.
        network_template (str):
            Server network template name. Filled if
            InstanceConfig.multivlan_config is true.
        logical_interfaces (MutableSequence[google.cloud.bare_metal_solution_v2.types.LogicalInterface]):
            List of logical interfaces for the instance. The number of
            logical interfaces will be the same as number of hardware
            bond/nic on the chosen network template. Filled if
            InstanceConfig.multivlan_config is true.
        ssh_key_names (MutableSequence[str]):
            List of names of ssh keys used to provision
            the instance.
    """

    class NetworkConfig(proto.Enum):
        r"""The network configuration of the instance.

        Values:
            NETWORKCONFIG_UNSPECIFIED (0):
                The unspecified network configuration.
            SINGLE_VLAN (1):
                Instance part of single client network and
                single private network.
            MULTI_VLAN (2):
                Instance part of multiple (or single) client
                networks and private networks.
        """

        NETWORKCONFIG_UNSPECIFIED = 0
        SINGLE_VLAN = 1
        MULTI_VLAN = 2

    class NetworkAddress(proto.Message):
        r"""A network.

        Attributes:
            network_id (str):
                Id of the network to use, within the same
                ProvisioningConfig request.
            address (str):
                IPv4 address to be assigned to the server.
            existing_network_id (str):
                Name of the existing network to use.
        """

        network_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        address: str = proto.Field(
            proto.STRING,
            number=2,
        )
        existing_network_id: str = proto.Field(
            proto.STRING,
            number=3,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    instance_type: str = proto.Field(
        proto.STRING,
        number=3,
    )
    hyperthreading: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    os_image: str = proto.Field(
        proto.STRING,
        number=5,
    )
    client_network: NetworkAddress = proto.Field(
        proto.MESSAGE,
        number=6,
        message=NetworkAddress,
    )
    private_network: NetworkAddress = proto.Field(
        proto.MESSAGE,
        number=7,
        message=NetworkAddress,
    )
    user_note: str = proto.Field(
        proto.STRING,
        number=8,
    )
    account_networks_enabled: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    network_config: NetworkConfig = proto.Field(
        proto.ENUM,
        number=10,
        enum=NetworkConfig,
    )
    network_template: str = proto.Field(
        proto.STRING,
        number=11,
    )
    logical_interfaces: MutableSequence[network.LogicalInterface] = proto.RepeatedField(
        proto.MESSAGE,
        number=12,
        message=network.LogicalInterface,
    )
    ssh_key_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=13,
    )


class VolumeConfig(proto.Message):
    r"""Configuration parameters for a new volume.

    Attributes:
        name (str):
            Output only. The name of the volume config.
        id (str):
            A transient unique identifier to identify a
            volume within an ProvisioningConfig request.
        snapshots_enabled (bool):
            Whether snapshots should be enabled.
        type_ (google.cloud.bare_metal_solution_v2.types.VolumeConfig.Type):
            The type of this Volume.
        protocol (google.cloud.bare_metal_solution_v2.types.VolumeConfig.Protocol):
            Volume protocol.
        size_gb (int):
            The requested size of this volume, in GB.
        lun_ranges (MutableSequence[google.cloud.bare_metal_solution_v2.types.VolumeConfig.LunRange]):
            LUN ranges to be configured. Set only when protocol is
            PROTOCOL_FC.
        machine_ids (MutableSequence[str]):
            Machine ids connected to this volume. Set only when protocol
            is PROTOCOL_FC.
        nfs_exports (MutableSequence[google.cloud.bare_metal_solution_v2.types.VolumeConfig.NfsExport]):
            NFS exports. Set only when protocol is PROTOCOL_NFS.
        user_note (str):
            User note field, it can be used by customers
            to add additional information for the BMS Ops
            team .
        gcp_service (str):
            The GCP service of the storage volume. Available gcp_service
            are in
            https://cloud.google.com/bare-metal/docs/bms-planning.
        performance_tier (google.cloud.bare_metal_solution_v2.types.VolumePerformanceTier):
            Performance tier of the Volume.
            Default is SHARED.
    """

    class Type(proto.Enum):
        r"""The types of Volumes.

        Values:
            TYPE_UNSPECIFIED (0):
                The unspecified type.
            FLASH (1):
                This Volume is on flash.
            DISK (2):
                This Volume is on disk.
        """

        TYPE_UNSPECIFIED = 0
        FLASH = 1
        DISK = 2

    class Protocol(proto.Enum):
        r"""The protocol used to access the volume.

        Values:
            PROTOCOL_UNSPECIFIED (0):
                Unspecified value.
            PROTOCOL_FC (1):
                Fibre channel.
            PROTOCOL_NFS (2):
                Network file system.
        """

        PROTOCOL_UNSPECIFIED = 0
        PROTOCOL_FC = 1
        PROTOCOL_NFS = 2

    class LunRange(proto.Message):
        r"""A LUN(Logical Unit Number) range.

        Attributes:
            quantity (int):
                Number of LUNs to create.
            size_gb (int):
                The requested size of each LUN, in GB.
        """

        quantity: int = proto.Field(
            proto.INT32,
            number=1,
        )
        size_gb: int = proto.Field(
            proto.INT32,
            number=2,
        )

    class NfsExport(proto.Message):
        r"""A NFS export entry.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            network_id (str):
                Network to use to publish the export.
            machine_id (str):
                Either a single machine, identified by an ID,
                or a comma-separated list of machine IDs.

                This field is a member of `oneof`_ ``client``.
            cidr (str):
                A CIDR range.

                This field is a member of `oneof`_ ``client``.
            permissions (google.cloud.bare_metal_solution_v2.types.VolumeConfig.NfsExport.Permissions):
                Export permissions.
            no_root_squash (bool):
                Disable root squashing, which is a feature of
                NFS. Root squash is a special mapping of the
                remote superuser (root) identity when using
                identity authentication.
            allow_suid (bool):
                Allow the setuid flag.
            allow_dev (bool):
                Allow dev flag in NfsShare
                AllowedClientsRequest.
        """

        class Permissions(proto.Enum):
            r"""Permissions that can granted for an export.

            Values:
                PERMISSIONS_UNSPECIFIED (0):
                    Unspecified value.
                READ_ONLY (1):
                    Read-only permission.
                READ_WRITE (2):
                    Read-write permission.
            """

            PERMISSIONS_UNSPECIFIED = 0
            READ_ONLY = 1
            READ_WRITE = 2

        network_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        machine_id: str = proto.Field(
            proto.STRING,
            number=2,
            oneof="client",
        )
        cidr: str = proto.Field(
            proto.STRING,
            number=3,
            oneof="client",
        )
        permissions: "VolumeConfig.NfsExport.Permissions" = proto.Field(
            proto.ENUM,
            number=4,
            enum="VolumeConfig.NfsExport.Permissions",
        )
        no_root_squash: bool = proto.Field(
            proto.BOOL,
            number=5,
        )
        allow_suid: bool = proto.Field(
            proto.BOOL,
            number=6,
        )
        allow_dev: bool = proto.Field(
            proto.BOOL,
            number=7,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    snapshots_enabled: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=4,
        enum=Type,
    )
    protocol: Protocol = proto.Field(
        proto.ENUM,
        number=5,
        enum=Protocol,
    )
    size_gb: int = proto.Field(
        proto.INT32,
        number=6,
    )
    lun_ranges: MutableSequence[LunRange] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=LunRange,
    )
    machine_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    nfs_exports: MutableSequence[NfsExport] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=NfsExport,
    )
    user_note: str = proto.Field(
        proto.STRING,
        number=10,
    )
    gcp_service: str = proto.Field(
        proto.STRING,
        number=11,
    )
    performance_tier: common.VolumePerformanceTier = proto.Field(
        proto.ENUM,
        number=12,
        enum=common.VolumePerformanceTier,
    )


class NetworkConfig(proto.Message):
    r"""Configuration parameters for a new network.

    Attributes:
        name (str):
            Output only. The name of the network config.
        id (str):
            A transient unique identifier to identify a
            volume within an ProvisioningConfig request.
        type_ (google.cloud.bare_metal_solution_v2.types.NetworkConfig.Type):
            The type of this network, either Client or
            Private.
        bandwidth (google.cloud.bare_metal_solution_v2.types.NetworkConfig.Bandwidth):
            Interconnect bandwidth. Set only when type is
            CLIENT.
        vlan_attachments (MutableSequence[google.cloud.bare_metal_solution_v2.types.NetworkConfig.IntakeVlanAttachment]):
            List of VLAN attachments. As of now there are
            always 2 attachments, but it is going to change
            in  the future (multi vlan).
        cidr (str):
            CIDR range of the network.
        service_cidr (google.cloud.bare_metal_solution_v2.types.NetworkConfig.ServiceCidr):
            Service CIDR, if any.
        user_note (str):
            User note field, it can be used by customers
            to add additional information for the BMS Ops
            team .
        gcp_service (str):
            The GCP service of the network. Available gcp_service are in
            https://cloud.google.com/bare-metal/docs/bms-planning.
        vlan_same_project (bool):
            Whether the VLAN attachment pair is located
            in the same project.
        jumbo_frames_enabled (bool):
            The JumboFramesEnabled option for customer to
            set.
    """

    class Type(proto.Enum):
        r"""Network type.

        Values:
            TYPE_UNSPECIFIED (0):
                Unspecified value.
            CLIENT (1):
                Client network, that is a network peered to a
                GCP VPC.
            PRIVATE (2):
                Private network, that is a network local to
                the BMS POD.
        """

        TYPE_UNSPECIFIED = 0
        CLIENT = 1
        PRIVATE = 2

    class Bandwidth(proto.Enum):
        r"""Interconnect bandwidth.

        Values:
            BANDWIDTH_UNSPECIFIED (0):
                Unspecified value.
            BW_1_GBPS (1):
                1 Gbps.
            BW_2_GBPS (2):
                2 Gbps.
            BW_5_GBPS (3):
                5 Gbps.
            BW_10_GBPS (4):
                10 Gbps.
        """

        BANDWIDTH_UNSPECIFIED = 0
        BW_1_GBPS = 1
        BW_2_GBPS = 2
        BW_5_GBPS = 3
        BW_10_GBPS = 4

    class ServiceCidr(proto.Enum):
        r"""Service network block.

        Values:
            SERVICE_CIDR_UNSPECIFIED (0):
                Unspecified value.
            DISABLED (1):
                Services are disabled for the given network.
            HIGH_26 (2):
                Use the highest /26 block of the network to
                host services.
            HIGH_27 (3):
                Use the highest /27 block of the network to
                host services.
            HIGH_28 (4):
                Use the highest /28 block of the network to
                host services.
        """

        SERVICE_CIDR_UNSPECIFIED = 0
        DISABLED = 1
        HIGH_26 = 2
        HIGH_27 = 3
        HIGH_28 = 4

    class IntakeVlanAttachment(proto.Message):
        r"""A GCP vlan attachment.

        Attributes:
            id (str):
                Identifier of the VLAN attachment.
            pairing_key (str):
                Attachment pairing key.
        """

        id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        pairing_key: str = proto.Field(
            proto.STRING,
            number=2,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=3,
        enum=Type,
    )
    bandwidth: Bandwidth = proto.Field(
        proto.ENUM,
        number=4,
        enum=Bandwidth,
    )
    vlan_attachments: MutableSequence[IntakeVlanAttachment] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=IntakeVlanAttachment,
    )
    cidr: str = proto.Field(
        proto.STRING,
        number=6,
    )
    service_cidr: ServiceCidr = proto.Field(
        proto.ENUM,
        number=7,
        enum=ServiceCidr,
    )
    user_note: str = proto.Field(
        proto.STRING,
        number=8,
    )
    gcp_service: str = proto.Field(
        proto.STRING,
        number=9,
    )
    vlan_same_project: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    jumbo_frames_enabled: bool = proto.Field(
        proto.BOOL,
        number=11,
    )


class InstanceQuota(proto.Message):
    r"""A resource budget.

    Attributes:
        name (str):
            Output only. The name of the instance quota.
        instance_type (str):
            Instance type. Deprecated: use gcp_service.
        gcp_service (str):
            The gcp service of the provisioning quota.
        location (str):
            Location where the quota applies.
        available_machine_count (int):
            Number of machines than can be created for the given
            location and instance_type.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    gcp_service: str = proto.Field(
        proto.STRING,
        number=5,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )
    available_machine_count: int = proto.Field(
        proto.INT32,
        number=4,
    )


class GetProvisioningConfigRequest(proto.Message):
    r"""Request for GetProvisioningConfig.

    Attributes:
        name (str):
            Required. Name of the ProvisioningConfig.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateProvisioningConfigRequest(proto.Message):
    r"""Request for CreateProvisioningConfig.

    Attributes:
        parent (str):
            Required. The parent project and location
            containing the ProvisioningConfig.
        provisioning_config (google.cloud.bare_metal_solution_v2.types.ProvisioningConfig):
            Required. The ProvisioningConfig to create.
        email (str):
            Optional. Email provided to send a
            confirmation with provisioning config to.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    provisioning_config: "ProvisioningConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ProvisioningConfig",
    )
    email: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateProvisioningConfigRequest(proto.Message):
    r"""Message for updating a ProvisioningConfig.

    Attributes:
        provisioning_config (google.cloud.bare_metal_solution_v2.types.ProvisioningConfig):
            Required. The ProvisioningConfig to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to update.
        email (str):
            Optional. Email provided to send a
            confirmation with provisioning config to.
    """

    provisioning_config: "ProvisioningConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ProvisioningConfig",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    email: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
