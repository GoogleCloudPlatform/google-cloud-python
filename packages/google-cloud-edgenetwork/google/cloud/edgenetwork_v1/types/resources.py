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
    package="google.cloud.edgenetwork.v1",
    manifest={
        "ResourceState",
        "RemotePeeringNetworkType",
        "Zone",
        "Network",
        "Subnet",
        "Interconnect",
        "InterconnectAttachment",
        "Router",
        "LinkLayerAddress",
        "SubnetStatus",
        "InterconnectDiagnostics",
        "RouterStatus",
    },
)


class ResourceState(proto.Enum):
    r"""ResourceState describes the state the resource.
    A normal lifecycle of a new resource being created would be:
    PENDING -> PROVISIONING -> RUNNING. A normal lifecycle of an
    existing resource being deleted would be: RUNNING -> DELETING.
    Any failures during processing will result the resource to be in
    a SUSPENDED state.

    Values:
        STATE_UNKNOWN (0):
            Unspecified state.
        STATE_PENDING (1):
            The resource is being prepared to be applied
            to the rack.
        STATE_PROVISIONING (2):
            The resource has started being applied to the
            rack.
        STATE_RUNNING (3):
            The resource has been pushed to the rack.
        STATE_SUSPENDED (4):
            The resource failed to push to the rack.
        STATE_DELETING (5):
            The resource is under deletion.
    """

    STATE_UNKNOWN = 0
    STATE_PENDING = 1
    STATE_PROVISIONING = 2
    STATE_RUNNING = 3
    STATE_SUSPENDED = 4
    STATE_DELETING = 5


class RemotePeeringNetworkType(proto.Enum):
    r"""Defines the remote peering destination for the interface. It
    is required when peering separation is enabled.

    Values:
        REMOTE_PEERING_NETWORK_TYPE_UNSPECIFIED (0):
            Unspecified.
        REMOTE_PEERING_NETWORK_TYPE_CUSTOMER_INTERNAL (1):
            Customer's trusted internal network.
        REMOTE_PEERING_NETWORK_TYPE_CUSTOMER_INTERNET (2):
            Customer's untrust network that has internet
            access.
    """

    REMOTE_PEERING_NETWORK_TYPE_UNSPECIFIED = 0
    REMOTE_PEERING_NETWORK_TYPE_CUSTOMER_INTERNAL = 1
    REMOTE_PEERING_NETWORK_TYPE_CUSTOMER_INTERNET = 2


class Zone(proto.Message):
    r"""A Google Edge Cloud zone.

    Attributes:
        name (str):
            Required. The resource name of the zone.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the zone was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the zone was last
            updated.
        labels (MutableMapping[str, str]):
            Deprecated: not implemented.
            Labels as key value pairs.
        layout_name (str):
            Deprecated: not implemented.
            The deployment layout type.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    layout_name: str = proto.Field(
        proto.STRING,
        number=5,
    )


class Network(proto.Message):
    r"""Message describing Network object

    Attributes:
        name (str):
            Required. The canonical resource name of the
            network.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the network was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the network was
            last updated.
        labels (MutableMapping[str, str]):
            Labels associated with this resource.
        description (str):
            Optional. A free-text description of the
            resource. Max length 1024 characters.
        mtu (int):
            IP (L3) MTU value of the network.
            Valid values are: 1500 and 9000.
            Default to 1500 if not set.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    mtu: int = proto.Field(
        proto.INT32,
        number=6,
    )


class Subnet(proto.Message):
    r"""Message describing Subnet object

    Attributes:
        name (str):
            Required. The canonical resource name of the
            subnet.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the subnet was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the subnet was
            last updated.
        labels (MutableMapping[str, str]):
            Labels associated with this resource.
        description (str):
            Optional. A free-text description of the
            resource. Max length 1024 characters.
        network (str):
            Required. The network that this subnetwork
            belongs to.
        ipv4_cidr (MutableSequence[str]):
            The ranges of ipv4 addresses that are owned
            by this subnetwork.
        ipv6_cidr (MutableSequence[str]):
            The ranges of ipv6 addresses that are owned
            by this subnetwork.
        vlan_id (int):
            Optional. VLAN id provided by user. If not
            specified we assign one automatically.
        bonding_type (google.cloud.edgenetwork_v1.types.Subnet.BondingType):
            Optional. A bonding type in the subnet
            creation specifies whether a VLAN being created
            will be present on Bonded or Non-Bonded or Both
            port types. In addition, this flag is to be used
            to set the specific network configuration which
            clusters can then use for their workloads based
            on the bonding choice.
        state (google.cloud.edgenetwork_v1.types.ResourceState):
            Output only. Current stage of the resource to
            the device by config push.
    """

    class BondingType(proto.Enum):
        r"""Bonding type in the subnet.

        Values:
            BONDING_TYPE_UNSPECIFIED (0):
                Unspecified
                Bonding type will be unspecified by default and
                if the user chooses to not specify a bonding
                type at time of creating the VLAN. This will be
                treated as mixed bonding where the VLAN will
                have both bonded and non-bonded connectivity to
                machines.
            BONDED (1):
                Multi homed.
            NON_BONDED (2):
                Single homed.
        """

        BONDING_TYPE_UNSPECIFIED = 0
        BONDED = 1
        NON_BONDED = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    network: str = proto.Field(
        proto.STRING,
        number=6,
    )
    ipv4_cidr: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    ipv6_cidr: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    vlan_id: int = proto.Field(
        proto.INT32,
        number=9,
    )
    bonding_type: BondingType = proto.Field(
        proto.ENUM,
        number=11,
        enum=BondingType,
    )
    state: "ResourceState" = proto.Field(
        proto.ENUM,
        number=10,
        enum="ResourceState",
    )


class Interconnect(proto.Message):
    r"""Message describing Interconnect object

    Attributes:
        name (str):
            Required. The canonical resource name of the
            interconnect.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the subnet was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the subnet was
            last updated.
        labels (MutableMapping[str, str]):
            Labels associated with this resource.
        description (str):
            Optional. A free-text description of the
            resource. Max length 1024 characters.
        interconnect_type (google.cloud.edgenetwork_v1.types.Interconnect.InterconnectType):
            Optional. Type of interconnect, which takes
            only the value 'DEDICATED' for now.
        uuid (str):
            Output only. Unique identifier for the link.
        device_cloud_resource_name (str):
            Output only. Cloud resource name of the
            switch device.
        physical_ports (MutableSequence[str]):
            Output only. Physical ports (e.g.,
            TenGigE0/0/0/1) that form the interconnect.
        remote_peering_network_type (google.cloud.edgenetwork_v1.types.RemotePeeringNetworkType):
            Optional. The remote peering network type of
            the interconnect. It is required when peering
            separation is enabled.
    """

    class InterconnectType(proto.Enum):
        r"""Type of interconnect.

        Values:
            INTERCONNECT_TYPE_UNSPECIFIED (0):
                Unspecified.
            DEDICATED (1):
                Dedicated Interconnect.
        """

        INTERCONNECT_TYPE_UNSPECIFIED = 0
        DEDICATED = 1

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    interconnect_type: InterconnectType = proto.Field(
        proto.ENUM,
        number=6,
        enum=InterconnectType,
    )
    uuid: str = proto.Field(
        proto.STRING,
        number=7,
    )
    device_cloud_resource_name: str = proto.Field(
        proto.STRING,
        number=8,
    )
    physical_ports: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=9,
    )
    remote_peering_network_type: "RemotePeeringNetworkType" = proto.Field(
        proto.ENUM,
        number=10,
        enum="RemotePeeringNetworkType",
    )


class InterconnectAttachment(proto.Message):
    r"""Message describing InterconnectAttachment object

    Attributes:
        name (str):
            Required. The canonical resource name of the
            interconnect attachment.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the interconnect
            attachment was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the interconnect
            attachment was last updated.
        labels (MutableMapping[str, str]):
            Labels associated with this resource.
        description (str):
            Optional. A free-text description of the
            resource. Max length 1024 characters.
        interconnect (str):
            Required. The canonical name of underlying Interconnect
            object that this attachment's traffic will traverse through.
            The name is in the form of
            ``projects/{project}/locations/{location}/zones/{zone}/interconnects/{interconnect}``.
        network (str):
            Optional. The canonical Network name in the form of
            ``projects/{project}/locations/{location}/zones/{zone}/networks/{network}``.
        vlan_id (int):
            Required. VLAN id provided by user. Must be
            site-wise unique.
        mtu (int):
            IP (L3) MTU value of the virtual edge cloud.
            Valid values are: 1500 and 9000.
            Default to 1500 if not set.
        state (google.cloud.edgenetwork_v1.types.ResourceState):
            Output only. Current stage of the resource to
            the device by config push.
        peering_type (google.cloud.edgenetwork_v1.types.RemotePeeringNetworkType):
            Optional. The remote peering network type of
            the underlying interconnect. It is required when
            peering separation is enabled.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    interconnect: str = proto.Field(
        proto.STRING,
        number=6,
    )
    network: str = proto.Field(
        proto.STRING,
        number=11,
    )
    vlan_id: int = proto.Field(
        proto.INT32,
        number=8,
    )
    mtu: int = proto.Field(
        proto.INT32,
        number=9,
    )
    state: "ResourceState" = proto.Field(
        proto.ENUM,
        number=10,
        enum="ResourceState",
    )
    peering_type: "RemotePeeringNetworkType" = proto.Field(
        proto.ENUM,
        number=12,
        enum="RemotePeeringNetworkType",
    )


class Router(proto.Message):
    r"""Message describing Router object

    Attributes:
        name (str):
            Required. The canonical resource name of the
            router.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the router was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the router was
            last updated.
        labels (MutableMapping[str, str]):
            Labels associated with this resource.
        description (str):
            Optional. A free-text description of the
            resource. Max length 1024 characters.
        network (str):
            Required. The canonical name of the network to which this
            router belongs. The name is in the form of
            ``projects/{project}/locations/{location}/zones/{zone}/networks/{network}``.
        interface (MutableSequence[google.cloud.edgenetwork_v1.types.Router.Interface]):
            Router interfaces.
        bgp_peer (MutableSequence[google.cloud.edgenetwork_v1.types.Router.BgpPeer]):
            BGP peers.
        bgp (google.cloud.edgenetwork_v1.types.Router.Bgp):
            BGP information specific to this router.
        state (google.cloud.edgenetwork_v1.types.ResourceState):
            Output only. Current stage of the resource to
            the device by config push.
        route_advertisements (MutableSequence[str]):
            Optional. A list of CIDRs in IP/Length format
            to advertise northbound as static routes from
            this router.
    """

    class Interface(proto.Message):
        r"""Router Interface defines the GDCE zone side layer-3
        information for building the BGP session.

        Attributes:
            name (str):
                Name of this interface entry. Unique within
                the Zones resource.
            ipv4_cidr (str):
                IP address and range of the interface.
            ipv6_cidr (str):
                IPv6 address and range of the interface.
            linked_interconnect_attachment (str):
                The canonical name of the linked Interconnect
                attachment.
            subnetwork (str):
                The canonical name of the subnetwork resource
                that this interface belongs to.
            loopback_ip_addresses (MutableSequence[str]):
                Create loopback interface in the router when
                specified. The number of IP addresses must match
                the number of TOR devices.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        ipv4_cidr: str = proto.Field(
            proto.STRING,
            number=3,
        )
        ipv6_cidr: str = proto.Field(
            proto.STRING,
            number=6,
        )
        linked_interconnect_attachment: str = proto.Field(
            proto.STRING,
            number=2,
        )
        subnetwork: str = proto.Field(
            proto.STRING,
            number=4,
        )
        loopback_ip_addresses: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=5,
        )

    class BgpPeer(proto.Message):
        r"""BGPPeer defines the peer side layer-3 information for
        building the BGP session.

        Attributes:
            name (str):
                Name of this BGP peer. Unique within the
                Zones resource.
            interface (str):
                Name of the RouterInterface the BGP peer is
                associated with.
            interface_ipv4_cidr (str):
                IP range of the interface within Google.
            interface_ipv6_cidr (str):
                IPv6 range of the interface within Google.
            peer_ipv4_cidr (str):
                IP range of the BGP interface outside Google.
            peer_ipv6_cidr (str):
                IPv6 range of the BGP interface outside
                Google.
            peer_asn (int):
                Peer BGP Autonomous System Number (ASN). Each
                BGP interface may use a different value.
            local_asn (int):
                Output only. Local BGP Autonomous System Number (ASN). This
                field is ST_NOT_REQUIRED because it stores private ASNs,
                which are meaningless outside the zone in which they are
                being used.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        interface: str = proto.Field(
            proto.STRING,
            number=2,
        )
        interface_ipv4_cidr: str = proto.Field(
            proto.STRING,
            number=3,
        )
        interface_ipv6_cidr: str = proto.Field(
            proto.STRING,
            number=7,
        )
        peer_ipv4_cidr: str = proto.Field(
            proto.STRING,
            number=4,
        )
        peer_ipv6_cidr: str = proto.Field(
            proto.STRING,
            number=6,
        )
        peer_asn: int = proto.Field(
            proto.UINT32,
            number=5,
        )
        local_asn: int = proto.Field(
            proto.UINT32,
            number=8,
        )

    class Bgp(proto.Message):
        r"""BGP information specific to this router.

        Attributes:
            asn (int):
                Locally assigned BGP ASN.
            keepalive_interval_in_seconds (int):
                The interval in seconds between BGP keepalive
                messages that are sent to the peer. Default is
                20 with value between 20 and 60.
        """

        asn: int = proto.Field(
            proto.UINT32,
            number=1,
        )
        keepalive_interval_in_seconds: int = proto.Field(
            proto.UINT32,
            number=2,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    network: str = proto.Field(
        proto.STRING,
        number=6,
    )
    interface: MutableSequence[Interface] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=Interface,
    )
    bgp_peer: MutableSequence[BgpPeer] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message=BgpPeer,
    )
    bgp: Bgp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=Bgp,
    )
    state: "ResourceState" = proto.Field(
        proto.ENUM,
        number=10,
        enum="ResourceState",
    )
    route_advertisements: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=11,
    )


class LinkLayerAddress(proto.Message):
    r"""LinkLayerAddress contains an IP address and corresponding
    link-layer address.

    Attributes:
        mac_address (str):
            The MAC address of this neighbor.
        ip_address (str):
            The IP address of this neighbor.
    """

    mac_address: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ip_address: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SubnetStatus(proto.Message):
    r"""SubnetStatus contains detailed and current technical
    information about this subnet resource.

    Attributes:
        name (str):
            The name of CCFE subnet resource.
        mac_address (str):
            BVI MAC address.
        link_layer_addresses (MutableSequence[google.cloud.edgenetwork_v1.types.LinkLayerAddress]):
            A list of LinkLayerAddress, describing the ip
            address and corresponding link-layer address of
            the neighbors for this subnet.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    mac_address: str = proto.Field(
        proto.STRING,
        number=2,
    )
    link_layer_addresses: MutableSequence["LinkLayerAddress"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="LinkLayerAddress",
    )


class InterconnectDiagnostics(proto.Message):
    r"""Diagnostics information about interconnect, contains detailed
    and current technical information about Google's side of the
    connection.

    Attributes:
        mac_address (str):
            The MAC address of the Interconnect's bundle
            interface.
        link_layer_addresses (MutableSequence[google.cloud.edgenetwork_v1.types.LinkLayerAddress]):
            A list of LinkLayerAddress, describing the ip
            address and corresponding link-layer address of
            the neighbors for this interconnect.
        links (MutableSequence[google.cloud.edgenetwork_v1.types.InterconnectDiagnostics.LinkStatus]):
            A list of LinkStatus objects, used to
            describe the status for each link on the
            Interconnect.
    """

    class LinkStatus(proto.Message):
        r"""Describing the status for each link on the Interconnect.

        Attributes:
            circuit_id (str):
                The unique ID for this link assigned during
                turn up by Google.
            lacp_status (google.cloud.edgenetwork_v1.types.InterconnectDiagnostics.LinkLACPStatus):
                Describing the state of a LACP link.
            lldp_statuses (MutableSequence[google.cloud.edgenetwork_v1.types.InterconnectDiagnostics.LinkLLDPStatus]):
                A list of LinkLLDPStatus objects, used to
                describe LLDP status of each peer for each link
                on the Interconnect.
            packet_counts (google.cloud.edgenetwork_v1.types.InterconnectDiagnostics.PacketCounts):
                Packet counts specific statistics for this
                link.
        """

        circuit_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        lacp_status: "InterconnectDiagnostics.LinkLACPStatus" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="InterconnectDiagnostics.LinkLACPStatus",
        )
        lldp_statuses: MutableSequence["InterconnectDiagnostics.LinkLLDPStatus"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=3,
                message="InterconnectDiagnostics.LinkLLDPStatus",
            )
        )
        packet_counts: "InterconnectDiagnostics.PacketCounts" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="InterconnectDiagnostics.PacketCounts",
        )

    class PacketCounts(proto.Message):
        r"""Containing a collection of interface-related statistics
        objects.

        Attributes:
            inbound_unicast (int):
                The number of packets that are delivered.
            inbound_errors (int):
                The number of inbound packets that contained
                errors.
            inbound_discards (int):
                The number of inbound packets that were
                chosen to be discarded even though no errors had
                been detected to prevent their being
                deliverable.
            outbound_unicast (int):
                The total number of packets that are
                requested be transmitted.
            outbound_errors (int):
                The number of outbound packets that could not
                be transmitted because of errors.
            outbound_discards (int):
                The number of outbound packets that were
                chosen to be discarded even though no errors had
                been detected to prevent their being
                transmitted.
        """

        inbound_unicast: int = proto.Field(
            proto.INT64,
            number=1,
        )
        inbound_errors: int = proto.Field(
            proto.INT64,
            number=2,
        )
        inbound_discards: int = proto.Field(
            proto.INT64,
            number=3,
        )
        outbound_unicast: int = proto.Field(
            proto.INT64,
            number=4,
        )
        outbound_errors: int = proto.Field(
            proto.INT64,
            number=5,
        )
        outbound_discards: int = proto.Field(
            proto.INT64,
            number=6,
        )

    class LinkLACPStatus(proto.Message):
        r"""Describing the status of a LACP link.

        Attributes:
            state (google.cloud.edgenetwork_v1.types.InterconnectDiagnostics.LinkLACPStatus.State):
                The state of a LACP link.
            google_system_id (str):
                System ID of the port on Google's side of the
                LACP exchange.
            neighbor_system_id (str):
                System ID of the port on the neighbor's side
                of the LACP exchange.
            aggregatable (bool):
                A true value indicates that the participant
                will allow the link to be used as part of the
                aggregate. A false value indicates the link
                should be used as an individual link.
            collecting (bool):
                If true, the participant is collecting
                incoming frames on the link, otherwise false
            distributing (bool):
                When true, the participant is distributing
                outgoing frames; when false, distribution is
                disabled
        """

        class State(proto.Enum):
            r"""State enum for LACP link.

            Values:
                UNKNOWN (0):
                    The default state indicating state is in
                    unknown state.
                ACTIVE (1):
                    The link is configured and active within the
                    bundle.
                DETACHED (2):
                    The link is not configured within the bundle,
                    this means the rest of the object should be
                    empty.
            """

            UNKNOWN = 0
            ACTIVE = 1
            DETACHED = 2

        state: "InterconnectDiagnostics.LinkLACPStatus.State" = proto.Field(
            proto.ENUM,
            number=1,
            enum="InterconnectDiagnostics.LinkLACPStatus.State",
        )
        google_system_id: str = proto.Field(
            proto.STRING,
            number=2,
        )
        neighbor_system_id: str = proto.Field(
            proto.STRING,
            number=3,
        )
        aggregatable: bool = proto.Field(
            proto.BOOL,
            number=4,
        )
        collecting: bool = proto.Field(
            proto.BOOL,
            number=5,
        )
        distributing: bool = proto.Field(
            proto.BOOL,
            number=6,
        )

    class LinkLLDPStatus(proto.Message):
        r"""Describing a LLDP link.

        Attributes:
            peer_system_name (str):
                The peer system's administratively assigned
                name.
            peer_system_description (str):
                The textual description of the network entity
                of LLDP peer.
            peer_chassis_id (str):
                The peer chassis component of the endpoint
                identifier associated with the transmitting LLDP
                agent.
            peer_chassis_id_type (str):
                The format and source of the peer chassis
                identifier string.
            peer_port_id (str):
                The port component of the endpoint identifier
                associated with the transmitting LLDP agent. If
                the specified port is an IEEE 802.3 Repeater
                port, then this TLV is optional.
            peer_port_id_type (str):
                The format and source of the peer port
                identifier string.
        """

        peer_system_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        peer_system_description: str = proto.Field(
            proto.STRING,
            number=2,
        )
        peer_chassis_id: str = proto.Field(
            proto.STRING,
            number=3,
        )
        peer_chassis_id_type: str = proto.Field(
            proto.STRING,
            number=4,
        )
        peer_port_id: str = proto.Field(
            proto.STRING,
            number=5,
        )
        peer_port_id_type: str = proto.Field(
            proto.STRING,
            number=6,
        )

    mac_address: str = proto.Field(
        proto.STRING,
        number=1,
    )
    link_layer_addresses: MutableSequence["LinkLayerAddress"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="LinkLayerAddress",
    )
    links: MutableSequence[LinkStatus] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=LinkStatus,
    )


class RouterStatus(proto.Message):
    r"""Describing the current status of a router.

    Attributes:
        network (str):
            The canonical name of the network to which
            this router belongs.
        bgp_peer_status (MutableSequence[google.cloud.edgenetwork_v1.types.RouterStatus.BgpPeerStatus]):
            A list of BgpPeerStatus objects, describing
            all BGP peers related to this router.
    """

    class BgpPeerStatus(proto.Message):
        r"""Status of a BGP peer.

        Attributes:
            name (str):
                Name of this BGP peer. Unique within the
                Routers resource.
            ip_address (str):
                IP address of the local BGP interface.
            peer_ip_address (str):
                IP address of the remote BGP interface.
            status (google.cloud.edgenetwork_v1.types.RouterStatus.BgpPeerStatus.BgpStatus):
                The current status of BGP.
            state (str):
                BGP state as specified in RFC1771.
            uptime (str):
                Time this session has been up.
                Format:

                 14 years, 51 weeks, 6 days, 23 hours, 59
                minutes, 59 seconds
            uptime_seconds (int):
                Time this session has been up, in seconds.
            prefix_counter (google.cloud.edgenetwork_v1.types.RouterStatus.PrefixCounter):
                A collection of counts for prefixes.
        """

        class BgpStatus(proto.Enum):
            r"""Status of the BGP peer: {UP, DOWN}

            Values:
                UNKNOWN (0):
                    The default status indicating BGP session is
                    in unknown state.
                UP (1):
                    The UP status indicating BGP session is
                    established.
                DOWN (2):
                    The DOWN state indicating BGP session is not
                    established yet.
            """

            UNKNOWN = 0
            UP = 1
            DOWN = 2

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        ip_address: str = proto.Field(
            proto.STRING,
            number=2,
        )
        peer_ip_address: str = proto.Field(
            proto.STRING,
            number=3,
        )
        status: "RouterStatus.BgpPeerStatus.BgpStatus" = proto.Field(
            proto.ENUM,
            number=4,
            enum="RouterStatus.BgpPeerStatus.BgpStatus",
        )
        state: str = proto.Field(
            proto.STRING,
            number=5,
        )
        uptime: str = proto.Field(
            proto.STRING,
            number=6,
        )
        uptime_seconds: int = proto.Field(
            proto.INT64,
            number=7,
        )
        prefix_counter: "RouterStatus.PrefixCounter" = proto.Field(
            proto.MESSAGE,
            number=8,
            message="RouterStatus.PrefixCounter",
        )

    class PrefixCounter(proto.Message):
        r"""PrefixCounter contains a collection of prefixes related
        counts.

        Attributes:
            advertised (int):
                Number of prefixes advertised.
            denied (int):
                Number of prefixes denied.
            received (int):
                Number of prefixes received.
            sent (int):
                Number of prefixes sent.
            suppressed (int):
                Number of prefixes suppressed.
            withdrawn (int):
                Number of prefixes withdrawn.
        """

        advertised: int = proto.Field(
            proto.INT64,
            number=1,
        )
        denied: int = proto.Field(
            proto.INT64,
            number=2,
        )
        received: int = proto.Field(
            proto.INT64,
            number=3,
        )
        sent: int = proto.Field(
            proto.INT64,
            number=4,
        )
        suppressed: int = proto.Field(
            proto.INT64,
            number=5,
        )
        withdrawn: int = proto.Field(
            proto.INT64,
            number=6,
        )

    network: str = proto.Field(
        proto.STRING,
        number=1,
    )
    bgp_peer_status: MutableSequence[BgpPeerStatus] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=BgpPeerStatus,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
