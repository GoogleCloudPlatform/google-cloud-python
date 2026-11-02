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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.vmwareengine.v1",
    manifest={
        "NetworkConfig",
        "NodeTypeConfig",
        "StretchedClusterConfig",
        "PrivateCloud",
        "Cluster",
        "Node",
        "ExternalAddress",
        "Subnet",
        "ExternalAccessRule",
        "LoggingServer",
        "NodeType",
        "Credentials",
        "HcxActivationKey",
        "Hcx",
        "Nsx",
        "Vcenter",
        "AutoscalingSettings",
        "DnsForwarding",
        "NetworkPeering",
        "PeeringRoute",
        "NetworkPolicy",
        "ManagementDnsZoneBinding",
        "VmwareEngineNetwork",
        "PrivateConnection",
        "LocationMetadata",
        "DnsBindPermission",
        "Principal",
    },
)


class NetworkConfig(proto.Message):
    r"""Network configuration in the consumer project
    with which the peering has to be done.

    Attributes:
        management_cidr (str):
            Required. Management CIDR used by VMware
            management appliances.
        vmware_engine_network (str):
            Optional. The relative resource name of the VMware Engine
            network attached to the private cloud. Specify the name in
            the following form:
            ``projects/{project}/locations/{location}/vmwareEngineNetworks/{vmware_engine_network_id}``
            where ``{project}`` can either be a project number or a
            project ID.
        vmware_engine_network_canonical (str):
            Output only. The canonical name of the VMware Engine network
            in the form:
            ``projects/{project_number}/locations/{location}/vmwareEngineNetworks/{vmware_engine_network_id}``
        management_ip_address_layout_version (int):
            Output only. The IP address layout version of the management
            IP address range. Possible versions include:

            - ``managementIpAddressLayoutVersion=1``: Indicates the
              legacy IP address layout used by some existing private
              clouds. This is no longer supported for new private clouds
              as it does not support all features.
            - ``managementIpAddressLayoutVersion=2``: Indicates the
              latest IP address layout used by all newly created private
              clouds. This version supports all current features.
        dns_server_ip (str):
            Output only. DNS Server IP of the Private
            Cloud. All DNS queries can be forwarded to this
            address for name resolution of Private Cloud's
            management entities like vCenter, NSX-T Manager
            and ESXi hosts.
    """

    management_cidr: str = proto.Field(
        proto.STRING,
        number=4,
    )
    vmware_engine_network: str = proto.Field(
        proto.STRING,
        number=5,
    )
    vmware_engine_network_canonical: str = proto.Field(
        proto.STRING,
        number=6,
    )
    management_ip_address_layout_version: int = proto.Field(
        proto.INT32,
        number=8,
    )
    dns_server_ip: str = proto.Field(
        proto.STRING,
        number=9,
    )


class NodeTypeConfig(proto.Message):
    r"""Information about the type and number of nodes associated
    with the cluster.

    Attributes:
        node_count (int):
            Required. The number of nodes of this type in
            the cluster
        custom_core_count (int):
            Optional. Customized number of cores available to each node
            of the type. This number must always be one of
            ``nodeType.availableCustomCoreCounts``. If zero is provided
            max value from ``nodeType.availableCustomCoreCounts`` will
            be used.
    """

    node_count: int = proto.Field(
        proto.INT32,
        number=1,
    )
    custom_core_count: int = proto.Field(
        proto.INT32,
        number=2,
    )


class StretchedClusterConfig(proto.Message):
    r"""Configuration of a stretched cluster.

    Attributes:
        preferred_location (str):
            Required. Zone that will remain operational when connection
            between the two zones is lost. Specify the resource name of
            a zone that belongs to the region of the private cloud. For
            example: ``projects/{project}/locations/europe-west3-a``
            where ``{project}`` can either be a project number or a
            project ID.
        secondary_location (str):
            Required. Additional zone for a higher level of availability
            and load balancing. Specify the resource name of a zone that
            belongs to the region of the private cloud. For example:
            ``projects/{project}/locations/europe-west3-b`` where
            ``{project}`` can either be a project number or a project
            ID.
    """

    preferred_location: str = proto.Field(
        proto.STRING,
        number=1,
    )
    secondary_location: str = proto.Field(
        proto.STRING,
        number=2,
    )


class PrivateCloud(proto.Message):
    r"""Represents a private cloud resource. Private clouds of type
    ``STANDARD`` and ``TIME_LIMITED`` are zonal resources, ``STRETCHED``
    private clouds are regional.

    Attributes:
        name (str):
            Output only. The resource name of this private cloud.
            Resource names are schemeless URIs that follow the
            conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation time of this resource.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last update time of this
            resource.
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the resource was
            scheduled for deletion.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the resource will be
            irreversibly deleted.
        state (google.cloud.vmwareengine_v1.types.PrivateCloud.State):
            Output only. State of the resource. New
            values may be added to this enum when
            appropriate.
        network_config (google.cloud.vmwareengine_v1.types.NetworkConfig):
            Required. Network configuration of the
            private cloud.
        management_cluster (google.cloud.vmwareengine_v1.types.PrivateCloud.ManagementCluster):
            Required. Input only. The management cluster for this
            private cloud. This field is required during creation of the
            private cloud to provide details for the default cluster.

            The following fields can't be changed after private cloud
            creation: ``ManagementCluster.clusterId``,
            ``ManagementCluster.nodeTypeId``.
        description (str):
            User-provided description for this private
            cloud.
        hcx (google.cloud.vmwareengine_v1.types.Hcx):
            Output only. HCX appliance.
        nsx (google.cloud.vmwareengine_v1.types.Nsx):
            Output only. NSX appliance.
        vcenter (google.cloud.vmwareengine_v1.types.Vcenter):
            Output only. Vcenter appliance.
        uid (str):
            Output only. System-generated unique
            identifier for the resource.
        type_ (google.cloud.vmwareengine_v1.types.PrivateCloud.Type):
            Optional. Type of the private cloud. Defaults
            to STANDARD.
    """

    class State(proto.Enum):
        r"""Enum State defines possible states of private clouds.

        Values:
            STATE_UNSPECIFIED (0):
                The default value. This value should never be
                used.
            ACTIVE (1):
                The private cloud is ready.
            CREATING (2):
                The private cloud is being created.
            UPDATING (3):
                The private cloud is being updated.
            FAILED (5):
                The private cloud is in failed state.
            DELETED (6):
                The private cloud is scheduled for deletion.
                The deletion process can be cancelled by using
                the corresponding undelete method.
            PURGING (7):
                The private cloud is irreversibly deleted and
                is being removed from the system.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        CREATING = 2
        UPDATING = 3
        FAILED = 5
        DELETED = 6
        PURGING = 7

    class Type(proto.Enum):
        r"""Enum Type defines private cloud type.

        Values:
            STANDARD (0):
                Standard private is a zonal resource, with 3+
                nodes. Default type.
            TIME_LIMITED (1):
                Time limited private cloud is a zonal
                resource, can have only 1 node and has limited
                life span. Will be deleted after defined period
                of time, can be converted into standard private
                cloud by expanding it up to 3 or more nodes.
            STRETCHED (2):
                Stretched private cloud is a regional
                resource with redundancy, with a minimum of 6
                nodes, nodes count has to be even.
        """

        STANDARD = 0
        TIME_LIMITED = 1
        STRETCHED = 2

    class ManagementCluster(proto.Message):
        r"""Management cluster configuration.

        Attributes:
            cluster_id (str):
                Required. The user-provided identifier of the new
                ``Cluster``. The identifier must meet the following
                requirements:

                - Only contains 1-63 alphanumeric characters and hyphens
                - Begins with an alphabetical character
                - Ends with a non-hyphen character
                - Not formatted as a UUID
                - Complies with `RFC
                  1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
                  (section 3.5)
            node_type_configs (MutableMapping[str, google.cloud.vmwareengine_v1.types.NodeTypeConfig]):
                Required. The map of cluster node types in this cluster,
                where the key is canonical identifier of the node type
                (corresponds to the ``NodeType``).
            stretched_cluster_config (google.cloud.vmwareengine_v1.types.StretchedClusterConfig):
                Optional. Configuration of a stretched
                cluster. Required for STRETCHED private clouds.
        """

        cluster_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        node_type_configs: MutableMapping[str, "NodeTypeConfig"] = proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=7,
            message="NodeTypeConfig",
        )
        stretched_cluster_config: "StretchedClusterConfig" = proto.Field(
            proto.MESSAGE,
            number=8,
            message="StretchedClusterConfig",
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
    delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=8,
        enum=State,
    )
    network_config: "NetworkConfig" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="NetworkConfig",
    )
    management_cluster: ManagementCluster = proto.Field(
        proto.MESSAGE,
        number=10,
        message=ManagementCluster,
    )
    description: str = proto.Field(
        proto.STRING,
        number=11,
    )
    hcx: "Hcx" = proto.Field(
        proto.MESSAGE,
        number=17,
        message="Hcx",
    )
    nsx: "Nsx" = proto.Field(
        proto.MESSAGE,
        number=18,
        message="Nsx",
    )
    vcenter: "Vcenter" = proto.Field(
        proto.MESSAGE,
        number=19,
        message="Vcenter",
    )
    uid: str = proto.Field(
        proto.STRING,
        number=20,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=22,
        enum=Type,
    )


class Cluster(proto.Message):
    r"""A cluster in a private cloud.

    Attributes:
        name (str):
            Output only. The resource name of this cluster. Resource
            names are schemeless URIs that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud/clusters/my-cluster``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation time of this resource.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last update time of this
            resource.
        state (google.cloud.vmwareengine_v1.types.Cluster.State):
            Output only. State of the resource.
        management (bool):
            Output only. True if the cluster is a
            management cluster; false otherwise. There can
            only be one management cluster in a private
            cloud and it has to be the first one.
        autoscaling_settings (google.cloud.vmwareengine_v1.types.AutoscalingSettings):
            Optional. Configuration of the autoscaling
            applied to this cluster.
        uid (str):
            Output only. System-generated unique
            identifier for the resource.
        node_type_configs (MutableMapping[str, google.cloud.vmwareengine_v1.types.NodeTypeConfig]):
            Required. The map of cluster node types in this cluster,
            where the key is canonical identifier of the node type
            (corresponds to the ``NodeType``).
        stretched_cluster_config (google.cloud.vmwareengine_v1.types.StretchedClusterConfig):
            Optional. Configuration of a stretched
            cluster. Required for clusters that belong to a
            STRETCHED private cloud.
    """

    class State(proto.Enum):
        r"""Enum State defines possible states of private cloud clusters.

        Values:
            STATE_UNSPECIFIED (0):
                The default value. This value should never be
                used.
            ACTIVE (1):
                The Cluster is operational and can be used by
                the user.
            CREATING (2):
                The Cluster is being deployed.
            UPDATING (3):
                Adding or removing of a node to the cluster,
                any other cluster specific updates.
            DELETING (4):
                The Cluster is being deleted.
            REPAIRING (5):
                The Cluster is undergoing maintenance, for
                example: a failed node is getting replaced.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        CREATING = 2
        UPDATING = 3
        DELETING = 4
        REPAIRING = 5

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
    state: State = proto.Field(
        proto.ENUM,
        number=6,
        enum=State,
    )
    management: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    autoscaling_settings: "AutoscalingSettings" = proto.Field(
        proto.MESSAGE,
        number=18,
        message="AutoscalingSettings",
    )
    uid: str = proto.Field(
        proto.STRING,
        number=14,
    )
    node_type_configs: MutableMapping[str, "NodeTypeConfig"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=16,
        message="NodeTypeConfig",
    )
    stretched_cluster_config: "StretchedClusterConfig" = proto.Field(
        proto.MESSAGE,
        number=17,
        message="StretchedClusterConfig",
    )


class Node(proto.Message):
    r"""Node in a cluster.

    Attributes:
        name (str):
            Output only. The resource name of this node. Resource names
            are schemeless URIs that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            projects/my-project/locations/us-central1-a/privateClouds/my-cloud/clusters/my-cluster/nodes/my-node
        fqdn (str):
            Output only. Fully qualified domain name of
            the node.
        internal_ip (str):
            Output only. Internal IP address of the node.
        node_type_id (str):
            Output only. The canonical identifier of the node type
            (corresponds to the ``NodeType``). For example: standard-72.
        version (str):
            Output only. The version number of the VMware
            ESXi management component in this cluster.
        custom_core_count (int):
            Output only. Customized number of cores
        state (google.cloud.vmwareengine_v1.types.Node.State):
            Output only. The state of the appliance.
    """

    class State(proto.Enum):
        r"""Enum State defines possible states of a node in a cluster.

        Values:
            STATE_UNSPECIFIED (0):
                The default value. This value should never be
                used.
            ACTIVE (1):
                Node is operational and can be used by the
                user.
            CREATING (2):
                Node is being provisioned.
            FAILED (3):
                Node is in a failed state.
            UPGRADING (4):
                Node is undergoing maintenance, e.g.: during
                private cloud upgrade.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        CREATING = 2
        FAILED = 3
        UPGRADING = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    fqdn: str = proto.Field(
        proto.STRING,
        number=2,
    )
    internal_ip: str = proto.Field(
        proto.STRING,
        number=3,
    )
    node_type_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    version: str = proto.Field(
        proto.STRING,
        number=5,
    )
    custom_core_count: int = proto.Field(
        proto.INT64,
        number=6,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=7,
        enum=State,
    )


class ExternalAddress(proto.Message):
    r"""Represents an allocated external IP address and its
    corresponding internal IP address in a private cloud.

    Attributes:
        name (str):
            Output only. The resource name of this external IP address.
            Resource names are schemeless URIs that follow the
            conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud/externalAddresses/my-address``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation time of this resource.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last update time of this
            resource.
        internal_ip (str):
            The internal IP address of a workload VM.
        external_ip (str):
            Output only. The external IP address of a
            workload VM.
        state (google.cloud.vmwareengine_v1.types.ExternalAddress.State):
            Output only. The state of the resource.
        uid (str):
            Output only. System-generated unique
            identifier for the resource.
        description (str):
            User-provided description for this resource.
    """

    class State(proto.Enum):
        r"""Enum State defines possible states of external addresses.

        Values:
            STATE_UNSPECIFIED (0):
                The default value. This value should never be
                used.
            ACTIVE (1):
                The address is ready.
            CREATING (2):
                The address is being created.
            UPDATING (3):
                The address is being updated.
            DELETING (4):
                The address is being deleted.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        CREATING = 2
        UPDATING = 3
        DELETING = 4

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
    internal_ip: str = proto.Field(
        proto.STRING,
        number=6,
    )
    external_ip: str = proto.Field(
        proto.STRING,
        number=7,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=8,
        enum=State,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=9,
    )
    description: str = proto.Field(
        proto.STRING,
        number=11,
    )


class Subnet(proto.Message):
    r"""Subnet in a private cloud. Either ``management`` subnets (such as
    vMotion) that are read-only, or ``userDefined``, which can also be
    updated.

    Attributes:
        name (str):
            Output only. The resource name of this subnet. Resource
            names are schemeless URIs that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud/subnets/my-subnet``
        ip_cidr_range (str):
            The IP address range of the subnet in CIDR
            format '10.0.0.0/24'.
        gateway_ip (str):
            The IP address of the gateway of this subnet.
            Must fall within the IP prefix defined above.
        type_ (str):
            Output only. The type of the subnet. For
            example "management" or "userDefined".
        state (google.cloud.vmwareengine_v1.types.Subnet.State):
            Output only. The state of the resource.
        vlan_id (int):
            Output only. VLAN ID of the VLAN on which the
            subnet is configured
    """

    class State(proto.Enum):
        r"""Defines possible states of subnets.

        Values:
            STATE_UNSPECIFIED (0):
                The default value. This value should never be
                used.
            ACTIVE (1):
                The subnet is ready.
            CREATING (2):
                The subnet is being created.
            UPDATING (3):
                The subnet is being updated.
            DELETING (4):
                The subnet is being deleted.
            RECONCILING (5):
                Changes requested in the last operation are
                being propagated.
            FAILED (6):
                Last operation on the subnet did not succeed.
                Subnet's payload is reverted back to its most
                recent working state.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        CREATING = 2
        UPDATING = 3
        DELETING = 4
        RECONCILING = 5
        FAILED = 6

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ip_cidr_range: str = proto.Field(
        proto.STRING,
        number=7,
    )
    gateway_ip: str = proto.Field(
        proto.STRING,
        number=8,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=11,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=13,
        enum=State,
    )
    vlan_id: int = proto.Field(
        proto.INT32,
        number=16,
    )


class ExternalAccessRule(proto.Message):
    r"""External access firewall rules for filtering incoming traffic
    destined to ``ExternalAddress`` resources.

    Attributes:
        name (str):
            Output only. The resource name of this external access rule.
            Resource names are schemeless URIs that follow the
            conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1/networkPolicies/my-policy/externalAccessRules/my-rule``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation time of this resource.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last update time of this
            resource.
        description (str):
            User-provided description for this external
            access rule.
        priority (int):
            External access rule priority, which determines the external
            access rule to use when multiple rules apply. If multiple
            rules have the same priority, their ordering is
            non-deterministic. If specific ordering is required, assign
            unique priorities to enforce such ordering. The external
            access rule priority is an integer from 100 to 4096, both
            inclusive. Lower integers indicate higher precedence. For
            example, a rule with priority ``100`` has higher precedence
            than a rule with priority ``101``.
        action (google.cloud.vmwareengine_v1.types.ExternalAccessRule.Action):
            The action that the external access rule
            performs.
        ip_protocol (str):
            The IP protocol to which the external access rule applies.
            This value can be one of the following three protocol
            strings (not case-sensitive): ``tcp``, ``udp``, or ``icmp``.
        source_ip_ranges (MutableSequence[google.cloud.vmwareengine_v1.types.ExternalAccessRule.IpRange]):
            If source ranges are specified, the external access rule
            applies only to traffic that has a source IP address in
            these ranges. These ranges can either be expressed in the
            CIDR format or as an IP address. As only inbound rules are
            supported, ``ExternalAddress`` resources cannot be the
            source IP addresses of an external access rule. To match all
            source addresses, specify ``0.0.0.0/0``.
        source_ports (MutableSequence[str]):
            A list of source ports to which the external access rule
            applies. This field is only applicable for the UDP or TCP
            protocol. Each entry must be either an integer or a range.
            For example: ``["22"]``, ``["80","443"]``, or
            ``["12345-12349"]``. To match all source ports, specify
            ``["0-65535"]``.
        destination_ip_ranges (MutableSequence[google.cloud.vmwareengine_v1.types.ExternalAccessRule.IpRange]):
            If destination ranges are specified, the external access
            rule applies only to the traffic that has a destination IP
            address in these ranges. The specified IP addresses must
            have reserved external IP addresses in the scope of the
            parent network policy. To match all external IP addresses in
            the scope of the parent network policy, specify
            ``0.0.0.0/0``. To match a specific external IP address,
            specify it using the ``IpRange.external_address`` property.
        destination_ports (MutableSequence[str]):
            A list of destination ports to which the external access
            rule applies. This field is only applicable for the UDP or
            TCP protocol. Each entry must be either an integer or a
            range. For example: ``["22"]``, ``["80","443"]``, or
            ``["12345-12349"]``. To match all destination ports, specify
            ``["0-65535"]``.
        state (google.cloud.vmwareengine_v1.types.ExternalAccessRule.State):
            Output only. The state of the resource.
        uid (str):
            Output only. System-generated unique
            identifier for the resource.
    """

    class Action(proto.Enum):
        r"""Action determines whether the external access rule permits or
        blocks traffic, subject to the other components of the rule
        matching the traffic.

        Values:
            ACTION_UNSPECIFIED (0):
                Defaults to allow.
            ALLOW (1):
                Allows connections that match the other
                specified components.
            DENY (2):
                Blocks connections that match the other
                specified components.
        """

        ACTION_UNSPECIFIED = 0
        ALLOW = 1
        DENY = 2

    class State(proto.Enum):
        r"""Defines possible states of external access firewall rules.

        Values:
            STATE_UNSPECIFIED (0):
                The default value. This value is used if the
                state is omitted.
            ACTIVE (1):
                The rule is ready.
            CREATING (2):
                The rule is being created.
            UPDATING (3):
                The rule is being updated.
            DELETING (4):
                The rule is being deleted.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        CREATING = 2
        UPDATING = 3
        DELETING = 4

    class IpRange(proto.Message):
        r"""An IP range provided in any one of the supported formats.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            ip_address (str):
                A single IP address. For example: ``10.0.0.5``.

                This field is a member of `oneof`_ ``ip_range``.
            ip_address_range (str):
                An IP address range in the CIDR format. For example:
                ``10.0.0.0/24``.

                This field is a member of `oneof`_ ``ip_range``.
            external_address (str):
                The name of an ``ExternalAddress`` resource. The external
                address must have been reserved in the scope of this
                external access rule's parent network policy. Provide the
                external address name in the form of
                ``projects/{project}/locations/{location}/privateClouds/{private_cloud}/externalAddresses/{external_address}``.
                For example:
                ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud/externalAddresses/my-address``.

                This field is a member of `oneof`_ ``ip_range``.
        """

        ip_address: str = proto.Field(
            proto.STRING,
            number=1,
            oneof="ip_range",
        )
        ip_address_range: str = proto.Field(
            proto.STRING,
            number=2,
            oneof="ip_range",
        )
        external_address: str = proto.Field(
            proto.STRING,
            number=3,
            oneof="ip_range",
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
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    priority: int = proto.Field(
        proto.INT32,
        number=6,
    )
    action: Action = proto.Field(
        proto.ENUM,
        number=7,
        enum=Action,
    )
    ip_protocol: str = proto.Field(
        proto.STRING,
        number=8,
    )
    source_ip_ranges: MutableSequence[IpRange] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=IpRange,
    )
    source_ports: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10,
    )
    destination_ip_ranges: MutableSequence[IpRange] = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message=IpRange,
    )
    destination_ports: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=12,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=13,
        enum=State,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=14,
    )


class LoggingServer(proto.Message):
    r"""Logging server to receive vCenter or ESXi logs.

    Attributes:
        name (str):
            Output only. The resource name of this logging server.
            Resource names are schemeless URIs that follow the
            conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud/loggingServers/my-logging-server``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation time of this resource.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last update time of this
            resource.
        hostname (str):
            Required. Fully-qualified domain name (FQDN)
            or IP Address of the logging server.
        port (int):
            Required. Port number at which the logging
            server receives logs.
        protocol (google.cloud.vmwareengine_v1.types.LoggingServer.Protocol):
            Required. Protocol used by vCenter to send
            logs to a logging server.
        source_type (google.cloud.vmwareengine_v1.types.LoggingServer.SourceType):
            Required. The type of component that produces
            logs that will be forwarded to this logging
            server.
        uid (str):
            Output only. System-generated unique
            identifier for the resource.
    """

    class Protocol(proto.Enum):
        r"""Defines possible protocols used to send logs to
        a logging server.

        Values:
            PROTOCOL_UNSPECIFIED (0):
                Unspecified communications protocol. This is
                the default value.
            UDP (1):
                UDP
            TCP (2):
                TCP
            TLS (3):
                TLS
            SSL (4):
                SSL
            RELP (5):
                RELP
        """

        PROTOCOL_UNSPECIFIED = 0
        UDP = 1
        TCP = 2
        TLS = 3
        SSL = 4
        RELP = 5

    class SourceType(proto.Enum):
        r"""Defines possible types of component that produces logs.

        Values:
            SOURCE_TYPE_UNSPECIFIED (0):
                The default value. This value should never be
                used.
            ESXI (1):
                Logs produced by ESXI hosts
            VCSA (2):
                Logs produced by vCenter server
        """

        SOURCE_TYPE_UNSPECIFIED = 0
        ESXI = 1
        VCSA = 2

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
    hostname: str = proto.Field(
        proto.STRING,
        number=5,
    )
    port: int = proto.Field(
        proto.INT32,
        number=7,
    )
    protocol: Protocol = proto.Field(
        proto.ENUM,
        number=6,
        enum=Protocol,
    )
    source_type: SourceType = proto.Field(
        proto.ENUM,
        number=10,
        enum=SourceType,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=8,
    )


class NodeType(proto.Message):
    r"""Describes node type.

    Attributes:
        name (str):
            Output only. The resource name of this node type. Resource
            names are schemeless URIs that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-proj/locations/us-central1-a/nodeTypes/standard-72``
        node_type_id (str):
            Output only. The canonical identifier of the node type
            (corresponds to the ``NodeType``). For example: standard-72.
        display_name (str):
            Output only. The friendly name for this node
            type. For example: ve1-standard-72
        virtual_cpu_count (int):
            Output only. The total number of virtual CPUs
            in a single node.
        total_core_count (int):
            Output only. The total number of CPU cores in
            a single node.
        memory_gb (int):
            Output only. The amount of physical memory
            available, defined in GB.
        disk_size_gb (int):
            Output only. The amount of storage available,
            defined in GB.
        available_custom_core_counts (MutableSequence[int]):
            Output only. List of possible values of
            custom core count.
        kind (google.cloud.vmwareengine_v1.types.NodeType.Kind):
            Output only. The type of the resource.
        families (MutableSequence[str]):
            Output only. Families of the node type. For node types to be
            in the same cluster they must share at least one element in
            the ``families``.
        capabilities (MutableSequence[google.cloud.vmwareengine_v1.types.NodeType.Capability]):
            Output only. Capabilities of this node type.
    """

    class Kind(proto.Enum):
        r"""Enum Kind defines possible types of a NodeType.

        Values:
            KIND_UNSPECIFIED (0):
                The default value. This value should never be
                used.
            STANDARD (1):
                Standard HCI node.
            STORAGE_ONLY (2):
                Storage only Node.
        """

        KIND_UNSPECIFIED = 0
        STANDARD = 1
        STORAGE_ONLY = 2

    class Capability(proto.Enum):
        r"""Capability of a node type.

        Values:
            CAPABILITY_UNSPECIFIED (0):
                The default value. This value is used if the
                capability is omitted or unknown.
            STRETCHED_CLUSTERS (1):
                This node type supports stretch clusters.
        """

        CAPABILITY_UNSPECIFIED = 0
        STRETCHED_CLUSTERS = 1

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    node_type_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    virtual_cpu_count: int = proto.Field(
        proto.INT32,
        number=4,
    )
    total_core_count: int = proto.Field(
        proto.INT32,
        number=5,
    )
    memory_gb: int = proto.Field(
        proto.INT32,
        number=7,
    )
    disk_size_gb: int = proto.Field(
        proto.INT32,
        number=8,
    )
    available_custom_core_counts: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=11,
    )
    kind: Kind = proto.Field(
        proto.ENUM,
        number=12,
        enum=Kind,
    )
    families: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=13,
    )
    capabilities: MutableSequence[Capability] = proto.RepeatedField(
        proto.ENUM,
        number=14,
        enum=Capability,
    )


class Credentials(proto.Message):
    r"""Credentials for a private cloud.

    Attributes:
        username (str):
            Initial username.
        password (str):
            Initial password.
    """

    username: str = proto.Field(
        proto.STRING,
        number=1,
    )
    password: str = proto.Field(
        proto.STRING,
        number=2,
    )


class HcxActivationKey(proto.Message):
    r"""HCX activation key. A default key is created during private cloud
    provisioning, but this behavior is subject to change and you should
    always verify active keys. Use
    [VmwareEngine.ListHcxActivationKeys][google.cloud.vmwareengine.v1.VmwareEngine.ListHcxActivationKeys]
    to retrieve existing keys and
    [VmwareEngine.CreateHcxActivationKey][google.cloud.vmwareengine.v1.VmwareEngine.CreateHcxActivationKey]
    to create new ones.

    Attributes:
        name (str):
            Output only. The resource name of this HcxActivationKey.
            Resource names are schemeless URIs that follow the
            conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1/privateClouds/my-cloud/hcxActivationKeys/my-key``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation time of HCX activation
            key.
        state (google.cloud.vmwareengine_v1.types.HcxActivationKey.State):
            Output only. State of HCX activation key.
        activation_key (str):
            Output only. HCX activation key.
        uid (str):
            Output only. System-generated unique
            identifier for the resource.
    """

    class State(proto.Enum):
        r"""State of HCX activation key

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state.
            AVAILABLE (1):
                State of a newly generated activation key.
            CONSUMED (2):
                State of key when it has been used to
                activate HCX appliance.
            CREATING (3):
                State of key when it is being created.
        """

        STATE_UNSPECIFIED = 0
        AVAILABLE = 1
        CONSUMED = 2
        CREATING = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    activation_key: str = proto.Field(
        proto.STRING,
        number=4,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=5,
    )


class Hcx(proto.Message):
    r"""Details about a HCX Cloud Manager appliance.

    Attributes:
        internal_ip (str):
            Internal IP address of the appliance.
        version (str):
            Version of the appliance.
        state (google.cloud.vmwareengine_v1.types.Hcx.State):
            Output only. The state of the appliance.
        fqdn (str):
            Fully qualified domain name of the appliance.
    """

    class State(proto.Enum):
        r"""State of the appliance

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified appliance state. This is the
                default value.
            ACTIVE (1):
                The appliance is operational and can be used.
            CREATING (2):
                The appliance is being deployed.
            ACTIVATING (3):
                The appliance is being activated.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        CREATING = 2
        ACTIVATING = 3

    internal_ip: str = proto.Field(
        proto.STRING,
        number=2,
    )
    version: str = proto.Field(
        proto.STRING,
        number=4,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    fqdn: str = proto.Field(
        proto.STRING,
        number=6,
    )


class Nsx(proto.Message):
    r"""Details about a NSX Manager appliance.

    Attributes:
        internal_ip (str):
            Internal IP address of the appliance.
        version (str):
            Version of the appliance.
        state (google.cloud.vmwareengine_v1.types.Nsx.State):
            Output only. The state of the appliance.
        fqdn (str):
            Fully qualified domain name of the appliance.
    """

    class State(proto.Enum):
        r"""State of the appliance

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified appliance state. This is the
                default value.
            ACTIVE (1):
                The appliance is operational and can be used.
            CREATING (2):
                The appliance is being deployed.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        CREATING = 2

    internal_ip: str = proto.Field(
        proto.STRING,
        number=2,
    )
    version: str = proto.Field(
        proto.STRING,
        number=4,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    fqdn: str = proto.Field(
        proto.STRING,
        number=6,
    )


class Vcenter(proto.Message):
    r"""Details about a vCenter Server management appliance.

    Attributes:
        internal_ip (str):
            Internal IP address of the appliance.
        version (str):
            Version of the appliance.
        state (google.cloud.vmwareengine_v1.types.Vcenter.State):
            Output only. The state of the appliance.
        fqdn (str):
            Fully qualified domain name of the appliance.
    """

    class State(proto.Enum):
        r"""State of the appliance

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified appliance state. This is the
                default value.
            ACTIVE (1):
                The appliance is operational and can be used.
            CREATING (2):
                The appliance is being deployed.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        CREATING = 2

    internal_ip: str = proto.Field(
        proto.STRING,
        number=2,
    )
    version: str = proto.Field(
        proto.STRING,
        number=4,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    fqdn: str = proto.Field(
        proto.STRING,
        number=6,
    )


class AutoscalingSettings(proto.Message):
    r"""Autoscaling settings define the rules used by VMware Engine
    to automatically scale-out and scale-in the clusters in a
    private cloud.

    Attributes:
        autoscaling_policies (MutableMapping[str, google.cloud.vmwareengine_v1.types.AutoscalingSettings.AutoscalingPolicy]):
            Required. The map with autoscaling policies applied to the
            cluster. The key is the identifier of the policy. It must
            meet the following requirements:

            - Only contains 1-63 alphanumeric characters and hyphens
            - Begins with an alphabetical character
            - Ends with a non-hyphen character
            - Not formatted as a UUID
            - Complies with `RFC
              1034 <https://datatracker.ietf.org/doc/html/rfc1034>`__
              (section 3.5)

            Currently there map must contain only one element that
            describes the autoscaling policy for compute nodes.
        min_cluster_node_count (int):
            Optional. Minimum number of nodes of any type
            in a cluster. If not specified the default
            limits apply.
        max_cluster_node_count (int):
            Optional. Maximum number of nodes of any type
            in a cluster. If not specified the default
            limits apply.
        cool_down_period (google.protobuf.duration_pb2.Duration):
            Optional. The minimum duration between
            consecutive autoscale operations. It starts once
            addition or removal of nodes is fully completed.
            Defaults to 30 minutes if not specified. Cool
            down period must be in whole minutes (for
            example, 30, 31, 50, 180 minutes).
    """

    class Thresholds(proto.Message):
        r"""Thresholds define the utilization of resources triggering
        scale-out and scale-in operations.

        Attributes:
            scale_out (int):
                Required. The utilization triggering the
                scale-out operation in percent.
            scale_in (int):
                Required. The utilization triggering the
                scale-in operation in percent.
        """

        scale_out: int = proto.Field(
            proto.INT32,
            number=1,
        )
        scale_in: int = proto.Field(
            proto.INT32,
            number=2,
        )

    class AutoscalingPolicy(proto.Message):
        r"""Autoscaling policy describes the behavior of the autoscaling
        with respect to the resource utilization.
        The scale-out operation is initiated if the utilization exceeds
        ANY of the respective thresholds.
        The scale-in operation is initiated if the utilization is below
        ALL of the respective thresholds.

        Attributes:
            node_type_id (str):
                Required. The canonical identifier of the node type to add
                or remove. Corresponds to the ``NodeType``.
            scale_out_size (int):
                Required. Number of nodes to add to a cluster
                during a scale-out operation. Must be divisible
                by 2 for stretched clusters. During a scale-in
                operation only one node (or 2 for stretched
                clusters) are removed in a single iteration.
            cpu_thresholds (google.cloud.vmwareengine_v1.types.AutoscalingSettings.Thresholds):
                Optional. Utilization thresholds pertaining
                to CPU utilization.
            granted_memory_thresholds (google.cloud.vmwareengine_v1.types.AutoscalingSettings.Thresholds):
                Optional. Utilization thresholds pertaining
                to amount of granted memory.
            consumed_memory_thresholds (google.cloud.vmwareengine_v1.types.AutoscalingSettings.Thresholds):
                Optional. Utilization thresholds pertaining
                to amount of consumed memory.
            storage_thresholds (google.cloud.vmwareengine_v1.types.AutoscalingSettings.Thresholds):
                Optional. Utilization thresholds pertaining
                to amount of consumed storage.
        """

        node_type_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        scale_out_size: int = proto.Field(
            proto.INT32,
            number=2,
        )
        cpu_thresholds: "AutoscalingSettings.Thresholds" = proto.Field(
            proto.MESSAGE,
            number=11,
            message="AutoscalingSettings.Thresholds",
        )
        granted_memory_thresholds: "AutoscalingSettings.Thresholds" = proto.Field(
            proto.MESSAGE,
            number=12,
            message="AutoscalingSettings.Thresholds",
        )
        consumed_memory_thresholds: "AutoscalingSettings.Thresholds" = proto.Field(
            proto.MESSAGE,
            number=13,
            message="AutoscalingSettings.Thresholds",
        )
        storage_thresholds: "AutoscalingSettings.Thresholds" = proto.Field(
            proto.MESSAGE,
            number=14,
            message="AutoscalingSettings.Thresholds",
        )

    autoscaling_policies: MutableMapping[str, AutoscalingPolicy] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=1,
        message=AutoscalingPolicy,
    )
    min_cluster_node_count: int = proto.Field(
        proto.INT32,
        number=2,
    )
    max_cluster_node_count: int = proto.Field(
        proto.INT32,
        number=3,
    )
    cool_down_period: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        message=duration_pb2.Duration,
    )


class DnsForwarding(proto.Message):
    r"""DNS forwarding config.
    This config defines a list of domain to name server mappings,
    and is attached to the private cloud for custom domain
    resolution.

    Attributes:
        name (str):
            Output only. The resource name of this DNS profile. Resource
            names are schemeless URIs that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud/dnsForwarding``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation time of this resource.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last update time of this
            resource.
        forwarding_rules (MutableSequence[google.cloud.vmwareengine_v1.types.DnsForwarding.ForwardingRule]):
            Required. List of domain mappings to
            configure
    """

    class ForwardingRule(proto.Message):
        r"""A forwarding rule is a mapping of a ``domain`` to ``name_servers``.
        This mapping allows VMware Engine to resolve domains for attached
        private clouds by forwarding DNS requests for a given domain to the
        specified nameservers.

        Attributes:
            domain (str):
                Required. Domain used to resolve a ``name_servers`` list.
            name_servers (MutableSequence[str]):
                Required. List of DNS servers to use for
                domain resolution
        """

        domain: str = proto.Field(
            proto.STRING,
            number=1,
        )
        name_servers: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
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
    forwarding_rules: MutableSequence[ForwardingRule] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=ForwardingRule,
    )


class NetworkPeering(proto.Message):
    r"""Details of a network peering.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. The resource name of the network peering.
            NetworkPeering is a global resource and location can only be
            global. Resource names are scheme-less URIs that follow the
            conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/global/networkPeerings/my-peering``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation time of this resource.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last update time of this
            resource.
        peer_network (str):
            Required. The relative resource name of the network to peer
            with a standard VMware Engine network. The provided network
            can be a consumer VPC network or another standard VMware
            Engine network. If the ``peer_network_type`` is
            VMWARE_ENGINE_NETWORK, specify the name in the form:
            ``projects/{project}/locations/global/vmwareEngineNetworks/{vmware_engine_network_id}``.
            Otherwise specify the name in the form:
            ``projects/{project}/global/networks/{network_id}``, where
            ``{project}`` can either be a project number or a project
            ID.
        export_custom_routes (bool):
            Optional. True if custom routes are exported
            to the peered network; false otherwise. The
            default value is true.

            This field is a member of `oneof`_ ``_export_custom_routes``.
        import_custom_routes (bool):
            Optional. True if custom routes are imported
            from the peered network; false otherwise. The
            default value is true.

            This field is a member of `oneof`_ ``_import_custom_routes``.
        exchange_subnet_routes (bool):
            Optional. True if full mesh connectivity is
            created and managed automatically between peered
            networks; false otherwise. Currently this field
            is always true because Google Compute Engine
            automatically creates and manages subnetwork
            routes between two VPC networks when peering
            state is 'ACTIVE'.

            This field is a member of `oneof`_ ``_exchange_subnet_routes``.
        export_custom_routes_with_public_ip (bool):
            Optional. True if all subnet routes with a public IP address
            range are exported; false otherwise. The default value is
            true. IPv4 special-use ranges
            (https://en.wikipedia.org/wiki/IPv4#Special_addresses) are
            always exported to peers and are not controlled by this
            field.

            This field is a member of `oneof`_ ``_export_custom_routes_with_public_ip``.
        import_custom_routes_with_public_ip (bool):
            Optional. True if all subnet routes with public IP address
            range are imported; false otherwise. The default value is
            true. IPv4 special-use ranges
            (https://en.wikipedia.org/wiki/IPv4#Special_addresses) are
            always imported to peers and are not controlled by this
            field.

            This field is a member of `oneof`_ ``_import_custom_routes_with_public_ip``.
        state (google.cloud.vmwareengine_v1.types.NetworkPeering.State):
            Output only. State of the network peering.
            This field has a value of 'ACTIVE' when there's
            a matching configuration in the peer network.
            New values may be added to this enum when
            appropriate.
        state_details (str):
            Output only. Output Only. Details about the
            current state of the network peering.
        peer_mtu (int):
            Optional. Maximum transmission unit (MTU) in bytes. The
            default value is ``1500``. If a value of ``0`` is provided
            for this field, VMware Engine uses the default value
            instead.
        peer_network_type (google.cloud.vmwareengine_v1.types.NetworkPeering.PeerNetworkType):
            Required. The type of the network to peer
            with the VMware Engine network.
        uid (str):
            Output only. System-generated unique
            identifier for the resource.
        vmware_engine_network (str):
            Required. The relative resource name of the VMware Engine
            network. Specify the name in the following form:
            ``projects/{project}/locations/{location}/vmwareEngineNetworks/{vmware_engine_network_id}``
            where ``{project}`` can either be a project number or a
            project ID.
        description (str):
            Optional. User-provided description for this
            network peering.
    """

    class State(proto.Enum):
        r"""Possible states of a network peering.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified network peering state. This is
                the default value.
            INACTIVE (1):
                The peering is not active.
            ACTIVE (2):
                The peering is active.
            CREATING (3):
                The peering is being created.
            DELETING (4):
                The peering is being deleted.
        """

        STATE_UNSPECIFIED = 0
        INACTIVE = 1
        ACTIVE = 2
        CREATING = 3
        DELETING = 4

    class PeerNetworkType(proto.Enum):
        r"""Type or purpose of the network peering connection.

        Values:
            PEER_NETWORK_TYPE_UNSPECIFIED (0):
                Unspecified
            STANDARD (1):
                Peering connection used for connecting to
                another VPC network established by the same
                user. For example, a peering connection to
                another VPC network in the same project or to an
                on-premises network.
            VMWARE_ENGINE_NETWORK (2):
                Peering connection used for connecting to
                another VMware Engine network.
            PRIVATE_SERVICES_ACCESS (3):
                Peering connection used for establishing `private services
                access <https://cloud.google.com/vpc/docs/private-services-access>`__.
            NETAPP_CLOUD_VOLUMES (4):
                Peering connection used for connecting to
                NetApp Cloud Volumes.
            THIRD_PARTY_SERVICE (5):
                Peering connection used for connecting to
                third-party services. Most third-party services
                require manual setup of reverse peering on the
                VPC network associated with the third-party
                service.
            DELL_POWERSCALE (6):
                Peering connection used for connecting to
                Dell PowerScale Filers
            GOOGLE_CLOUD_NETAPP_VOLUMES (7):
                Peering connection used for connecting to
                Google Cloud NetApp Volumes.
        """

        PEER_NETWORK_TYPE_UNSPECIFIED = 0
        STANDARD = 1
        VMWARE_ENGINE_NETWORK = 2
        PRIVATE_SERVICES_ACCESS = 3
        NETAPP_CLOUD_VOLUMES = 4
        THIRD_PARTY_SERVICE = 5
        DELL_POWERSCALE = 6
        GOOGLE_CLOUD_NETAPP_VOLUMES = 7

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
    peer_network: str = proto.Field(
        proto.STRING,
        number=5,
    )
    export_custom_routes: bool = proto.Field(
        proto.BOOL,
        number=8,
        optional=True,
    )
    import_custom_routes: bool = proto.Field(
        proto.BOOL,
        number=9,
        optional=True,
    )
    exchange_subnet_routes: bool = proto.Field(
        proto.BOOL,
        number=10,
        optional=True,
    )
    export_custom_routes_with_public_ip: bool = proto.Field(
        proto.BOOL,
        number=11,
        optional=True,
    )
    import_custom_routes_with_public_ip: bool = proto.Field(
        proto.BOOL,
        number=12,
        optional=True,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=13,
        enum=State,
    )
    state_details: str = proto.Field(
        proto.STRING,
        number=7,
    )
    peer_mtu: int = proto.Field(
        proto.INT32,
        number=14,
    )
    peer_network_type: PeerNetworkType = proto.Field(
        proto.ENUM,
        number=16,
        enum=PeerNetworkType,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=17,
    )
    vmware_engine_network: str = proto.Field(
        proto.STRING,
        number=20,
    )
    description: str = proto.Field(
        proto.STRING,
        number=21,
    )


class PeeringRoute(proto.Message):
    r"""Exchanged network peering route.

    Attributes:
        dest_range (str):
            Output only. Destination range of the peering
            route in CIDR notation.
        type_ (google.cloud.vmwareengine_v1.types.PeeringRoute.Type):
            Output only. Type of the route in the peer
            VPC network.
        next_hop_region (str):
            Output only. Region containing the next hop
            of the peering route. This field only applies to
            dynamic routes in the peer VPC network.
        priority (int):
            Output only. The priority of the peering
            route.
        imported (bool):
            Output only. True if the peering route has been imported
            from a peered VPC network; false otherwise. The import
            happens if the field ``NetworkPeering.importCustomRoutes``
            is true for this network,
            ``NetworkPeering.exportCustomRoutes`` is true for the peer
            VPC network, and the import does not result in a route
            conflict.
        direction (google.cloud.vmwareengine_v1.types.PeeringRoute.Direction):
            Output only. Direction of the routes exchanged with the peer
            network, from the VMware Engine network perspective:

            - Routes of direction ``INCOMING`` are imported from the
              peer network.
            - Routes of direction ``OUTGOING`` are exported from the
              intranet VPC network of the VMware Engine network.
    """

    class Type(proto.Enum):
        r"""The type of the peering route.

        Values:
            TYPE_UNSPECIFIED (0):
                Unspecified peering route type. This is the
                default value.
            DYNAMIC_PEERING_ROUTE (1):
                Dynamic routes in the peer network.
            STATIC_PEERING_ROUTE (2):
                Static routes in the peer network.
            SUBNET_PEERING_ROUTE (3):
                Created, updated, and removed automatically
                by Google Cloud when subnets are created,
                modified, or deleted in the peer network.
        """

        TYPE_UNSPECIFIED = 0
        DYNAMIC_PEERING_ROUTE = 1
        STATIC_PEERING_ROUTE = 2
        SUBNET_PEERING_ROUTE = 3

    class Direction(proto.Enum):
        r"""The direction of the exchanged routes.

        Values:
            DIRECTION_UNSPECIFIED (0):
                Unspecified exchanged routes direction. This
                is default.
            INCOMING (1):
                Routes imported from the peer network.
            OUTGOING (2):
                Routes exported to the peer network.
        """

        DIRECTION_UNSPECIFIED = 0
        INCOMING = 1
        OUTGOING = 2

    dest_range: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=2,
        enum=Type,
    )
    next_hop_region: str = proto.Field(
        proto.STRING,
        number=3,
    )
    priority: int = proto.Field(
        proto.INT64,
        number=4,
    )
    imported: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    direction: Direction = proto.Field(
        proto.ENUM,
        number=6,
        enum=Direction,
    )


class NetworkPolicy(proto.Message):
    r"""Represents a network policy resource. Network policies are
    regional resources. You can use a network policy to enable or
    disable internet access and external IP access. Network policies
    are associated with a VMware Engine network, which might span
    across regions. For a given region, a network policy applies to
    all private clouds in the VMware Engine network associated with
    the policy.

    Attributes:
        name (str):
            Output only. The resource name of this network policy.
            Resource names are schemeless URIs that follow the
            conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1/networkPolicies/my-network-policy``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation time of this resource.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last update time of this
            resource.
        internet_access (google.cloud.vmwareengine_v1.types.NetworkPolicy.NetworkService):
            Network service that allows VMware workloads
            to access the internet.
        external_ip (google.cloud.vmwareengine_v1.types.NetworkPolicy.NetworkService):
            Network service that allows External IP addresses to be
            assigned to VMware workloads. This service can only be
            enabled when ``internet_access`` is also enabled.
        edge_services_cidr (str):
            Required. IP address range in CIDR notation
            used to create internet access and external IP
            access. An RFC 1918 CIDR block, with a "/26"
            prefix, is required. The range cannot overlap
            with any prefixes either in the consumer VPC
            network or in use by the private clouds attached
            to that VPC network.
        uid (str):
            Output only. System-generated unique
            identifier for the resource.
        vmware_engine_network (str):
            Optional. The relative resource name of the VMware Engine
            network. Specify the name in the following form:
            ``projects/{project}/locations/{location}/vmwareEngineNetworks/{vmware_engine_network_id}``
            where ``{project}`` can either be a project number or a
            project ID.
        description (str):
            Optional. User-provided description for this
            network policy.
        vmware_engine_network_canonical (str):
            Output only. The canonical name of the VMware Engine network
            in the form:
            ``projects/{project_number}/locations/{location}/vmwareEngineNetworks/{vmware_engine_network_id}``
    """

    class NetworkService(proto.Message):
        r"""Represents a network service that is managed by a ``NetworkPolicy``
        resource. A network service provides a way to control an aspect of
        external access to VMware workloads. For example, whether the VMware
        workloads in the private clouds governed by a network policy can
        access or be accessed from the internet.

        Attributes:
            enabled (bool):
                True if the service is enabled; false
                otherwise.
            state (google.cloud.vmwareengine_v1.types.NetworkPolicy.NetworkService.State):
                Output only. State of the service. New values
                may be added to this enum when appropriate.
        """

        class State(proto.Enum):
            r"""Enum State defines possible states of a network policy
            controlled service.

            Values:
                STATE_UNSPECIFIED (0):
                    Unspecified service state. This is the
                    default value.
                UNPROVISIONED (1):
                    Service is not provisioned.
                RECONCILING (2):
                    Service is in the process of being
                    provisioned/deprovisioned.
                ACTIVE (3):
                    Service is active.
            """

            STATE_UNSPECIFIED = 0
            UNPROVISIONED = 1
            RECONCILING = 2
            ACTIVE = 3

        enabled: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        state: "NetworkPolicy.NetworkService.State" = proto.Field(
            proto.ENUM,
            number=2,
            enum="NetworkPolicy.NetworkService.State",
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
    internet_access: NetworkService = proto.Field(
        proto.MESSAGE,
        number=6,
        message=NetworkService,
    )
    external_ip: NetworkService = proto.Field(
        proto.MESSAGE,
        number=7,
        message=NetworkService,
    )
    edge_services_cidr: str = proto.Field(
        proto.STRING,
        number=9,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=10,
    )
    vmware_engine_network: str = proto.Field(
        proto.STRING,
        number=12,
    )
    description: str = proto.Field(
        proto.STRING,
        number=13,
    )
    vmware_engine_network_canonical: str = proto.Field(
        proto.STRING,
        number=14,
    )


class ManagementDnsZoneBinding(proto.Message):
    r"""Represents a binding between a network and the management DNS
    zone. A management DNS zone is the Cloud DNS cross-project
    binding zone that VMware Engine creates for each private cloud.
    It contains FQDNs and corresponding IP addresses for the private
    cloud's ESXi hosts and management VM appliances like vCenter and
    NSX Manager.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. The resource name of this binding. Resource
            names are schemeless URIs that follow the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1-a/privateClouds/my-cloud/managementDnsZoneBindings/my-management-dns-zone-binding``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation time of this resource.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last update time of this
            resource.
        state (google.cloud.vmwareengine_v1.types.ManagementDnsZoneBinding.State):
            Output only. The state of the resource.
        description (str):
            User-provided description for this resource.
        vpc_network (str):
            Network to bind is a standard consumer VPC. Specify the name
            in the following form for consumer VPC network:
            ``projects/{project}/global/networks/{network_id}``.
            ``{project}`` can either be a project number or a project
            ID.

            This field is a member of `oneof`_ ``bind_network``.
        vmware_engine_network (str):
            Network to bind is a VMware Engine network. Specify the name
            in the following form for VMware engine network:
            ``projects/{project}/locations/global/vmwareEngineNetworks/{vmware_engine_network_id}``.
            ``{project}`` can either be a project number or a project
            ID.

            This field is a member of `oneof`_ ``bind_network``.
        uid (str):
            Output only. System-generated unique
            identifier for the resource.
    """

    class State(proto.Enum):
        r"""Enum State defines possible states of binding between the
        consumer VPC network and the management DNS zone.

        Values:
            STATE_UNSPECIFIED (0):
                The default value. This value should never be
                used.
            ACTIVE (1):
                The binding is ready.
            CREATING (2):
                The binding is being created.
            UPDATING (3):
                The binding is being updated.
            DELETING (4):
                The binding is being deleted.
            FAILED (5):
                The binding has failed.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        CREATING = 2
        UPDATING = 3
        DELETING = 4
        FAILED = 5

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
    state: State = proto.Field(
        proto.ENUM,
        number=8,
        enum=State,
    )
    description: str = proto.Field(
        proto.STRING,
        number=13,
    )
    vpc_network: str = proto.Field(
        proto.STRING,
        number=14,
        oneof="bind_network",
    )
    vmware_engine_network: str = proto.Field(
        proto.STRING,
        number=15,
        oneof="bind_network",
    )
    uid: str = proto.Field(
        proto.STRING,
        number=9,
    )


class VmwareEngineNetwork(proto.Message):
    r"""VMware Engine network resource that provides connectivity for
    VMware Engine private clouds.

    Attributes:
        name (str):
            Output only. The resource name of the VMware Engine network.
            Resource names are schemeless URIs that follow the
            conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/global/vmwareEngineNetworks/my-network``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation time of this resource.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last update time of this
            resource.
        description (str):
            User-provided description for this VMware
            Engine network.
        vpc_networks (MutableSequence[google.cloud.vmwareengine_v1.types.VmwareEngineNetwork.VpcNetwork]):
            Output only. VMware Engine service VPC
            networks that provide connectivity from a
            private cloud to customer projects, the
            internet, and other Google Cloud services.
        state (google.cloud.vmwareengine_v1.types.VmwareEngineNetwork.State):
            Output only. State of the VMware Engine
            network.
        type_ (google.cloud.vmwareengine_v1.types.VmwareEngineNetwork.Type):
            Required. VMware Engine network type.
        uid (str):
            Output only. System-generated unique
            identifier for the resource.
        etag (str):
            Checksum that may be sent on update and
            delete requests to ensure that the user-provided
            value is up to date before the server processes
            a request. The server computes checksums based
            on the value of other fields in the request.
    """

    class State(proto.Enum):
        r"""Enum State defines possible states of VMware Engine network.

        Values:
            STATE_UNSPECIFIED (0):
                The default value. This value is used if the
                state is omitted.
            CREATING (1):
                The VMware Engine network is being created.
            ACTIVE (2):
                The VMware Engine network is ready.
            UPDATING (3):
                The VMware Engine network is being updated.
            DELETING (4):
                The VMware Engine network is being deleted.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        UPDATING = 3
        DELETING = 4

    class Type(proto.Enum):
        r"""Enum Type defines possible types of VMware Engine network.

        Values:
            TYPE_UNSPECIFIED (0):
                The default value. This value should never be
                used.
            LEGACY (1):
                Network type used by private clouds created in projects
                without a network of type ``STANDARD``. This network type is
                no longer used for new VMware Engine private cloud
                deployments.
            STANDARD (2):
                Standard network type used for private cloud
                connectivity.
        """

        TYPE_UNSPECIFIED = 0
        LEGACY = 1
        STANDARD = 2

    class VpcNetwork(proto.Message):
        r"""Represents a VMware Engine VPC network that is managed by a
        VMware Engine network resource.

        Attributes:
            type_ (google.cloud.vmwareengine_v1.types.VmwareEngineNetwork.VpcNetwork.Type):
                Output only. Type of VPC network (INTRANET, INTERNET, or
                GOOGLE_CLOUD)
            network (str):
                Output only. The relative resource name of the service VPC
                network this VMware Engine network is attached to. For
                example: ``projects/123123/global/networks/my-network``
        """

        class Type(proto.Enum):
            r"""Enum Type defines possible types of a VMware Engine network
            controlled service.

            Values:
                TYPE_UNSPECIFIED (0):
                    The default value. This value should never be
                    used.
                INTRANET (1):
                    VPC network that will be peered with a
                    consumer VPC network or the intranet VPC of
                    another VMware Engine network. Access a private
                    cloud through Compute Engine VMs on a peered VPC
                    network or an on-premises resource connected to
                    a peered consumer VPC network.
                INTERNET (2):
                    VPC network used for internet access to and
                    from a private cloud.
                GOOGLE_CLOUD (3):
                    VPC network used for access to Google Cloud
                    services like Cloud Storage.
            """

            TYPE_UNSPECIFIED = 0
            INTRANET = 1
            INTERNET = 2
            GOOGLE_CLOUD = 3

        type_: "VmwareEngineNetwork.VpcNetwork.Type" = proto.Field(
            proto.ENUM,
            number=1,
            enum="VmwareEngineNetwork.VpcNetwork.Type",
        )
        network: str = proto.Field(
            proto.STRING,
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
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    vpc_networks: MutableSequence[VpcNetwork] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=VpcNetwork,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=7,
        enum=State,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=8,
        enum=Type,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=9,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=10,
    )


class PrivateConnection(proto.Message):
    r"""Private connection resource that provides connectivity for
    VMware Engine private clouds.

    Attributes:
        name (str):
            Output only. The resource name of the private connection.
            Resource names are schemeless URIs that follow the
            conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/us-central1/privateConnections/my-connection``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation time of this resource.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last update time of this
            resource.
        description (str):
            Optional. User-provided description for this
            private connection.
        state (google.cloud.vmwareengine_v1.types.PrivateConnection.State):
            Output only. State of the private connection.
        vmware_engine_network (str):
            Required. The relative resource name of Legacy VMware Engine
            network. Specify the name in the following form:
            ``projects/{project}/locations/{location}/vmwareEngineNetworks/{vmware_engine_network_id}``
            where ``{project}``, ``{location}`` will be same as
            specified in private connection resource name and
            ``{vmware_engine_network_id}`` will be in the form of
            ``{location}``-default e.g.
            projects/project/locations/us-central1/vmwareEngineNetworks/us-central1-default.
        vmware_engine_network_canonical (str):
            Output only. The canonical name of the VMware Engine network
            in the form:
            ``projects/{project_number}/locations/{location}/vmwareEngineNetworks/{vmware_engine_network_id}``
        type_ (google.cloud.vmwareengine_v1.types.PrivateConnection.Type):
            Required. Private connection type.
        peering_id (str):
            Output only. VPC network peering id between
            given network VPC and VMwareEngineNetwork.
        routing_mode (google.cloud.vmwareengine_v1.types.PrivateConnection.RoutingMode):
            Optional. Routing Mode. Default value is set to GLOBAL. For
            type = PRIVATE_SERVICE_ACCESS, this field can be set to
            GLOBAL or REGIONAL, for other types only GLOBAL is
            supported.
        uid (str):
            Output only. System-generated unique
            identifier for the resource.
        service_network (str):
            Required. Service network to create private connection.
            Specify the name in the following form:
            ``projects/{project}/global/networks/{network_id}`` For type
            = PRIVATE_SERVICE_ACCESS, this field represents
            servicenetworking VPC, e.g.
            projects/project-tp/global/networks/servicenetworking. For
            type = NETAPP_CLOUD_VOLUME, this field represents NetApp
            service VPC, e.g.
            projects/project-tp/global/networks/netapp-tenant-vpc. For
            type = DELL_POWERSCALE, this field represent Dell service
            VPC, e.g.
            projects/project-tp/global/networks/dell-tenant-vpc. For
            type= THIRD_PARTY_SERVICE, this field could represent a
            consumer VPC or any other producer VPC to which the VMware
            Engine Network needs to be connected, e.g.
            projects/project/global/networks/vpc.
        peering_state (google.cloud.vmwareengine_v1.types.PrivateConnection.PeeringState):
            Output only. Peering state between service
            network and VMware Engine network.
    """

    class State(proto.Enum):
        r"""Enum State defines possible states of private connection.

        Values:
            STATE_UNSPECIFIED (0):
                The default value. This value is used if the
                state is omitted.
            CREATING (1):
                The private connection is being created.
            ACTIVE (2):
                The private connection is ready.
            UPDATING (3):
                The private connection is being updated.
            DELETING (4):
                The private connection is being deleted.
            UNPROVISIONED (5):
                The private connection is not provisioned,
                since no private cloud is present for which this
                private connection is needed.
            FAILED (6):
                The private connection is in failed state.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        UPDATING = 3
        DELETING = 4
        UNPROVISIONED = 5
        FAILED = 6

    class Type(proto.Enum):
        r"""Enum Type defines possible types of private connection.

        Values:
            TYPE_UNSPECIFIED (0):
                The default value. This value should never be
                used.
            PRIVATE_SERVICE_ACCESS (1):
                Connection used for establishing `private services
                access <https://cloud.google.com/vpc/docs/private-services-access>`__.
            NETAPP_CLOUD_VOLUMES (2):
                Connection used for connecting to NetApp
                Cloud Volumes.
            DELL_POWERSCALE (3):
                Connection used for connecting to Dell
                PowerScale.
            THIRD_PARTY_SERVICE (4):
                Connection used for connecting to third-party
                services.
        """

        TYPE_UNSPECIFIED = 0
        PRIVATE_SERVICE_ACCESS = 1
        NETAPP_CLOUD_VOLUMES = 2
        DELL_POWERSCALE = 3
        THIRD_PARTY_SERVICE = 4

    class RoutingMode(proto.Enum):
        r"""Possible types for RoutingMode

        Values:
            ROUTING_MODE_UNSPECIFIED (0):
                The default value. This value should never be
                used.
            GLOBAL (1):
                Global Routing Mode
            REGIONAL (2):
                Regional Routing Mode
        """

        ROUTING_MODE_UNSPECIFIED = 0
        GLOBAL = 1
        REGIONAL = 2

    class PeeringState(proto.Enum):
        r"""Enum PeeringState defines the possible states of peering
        between service network and the vpc network peered to service
        network

        Values:
            PEERING_STATE_UNSPECIFIED (0):
                The default value. This value is used if the
                peering state is omitted or unknown.
            PEERING_ACTIVE (1):
                The peering is in active state.
            PEERING_INACTIVE (2):
                The peering is in inactive state.
        """

        PEERING_STATE_UNSPECIFIED = 0
        PEERING_ACTIVE = 1
        PEERING_INACTIVE = 2

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
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    vmware_engine_network: str = proto.Field(
        proto.STRING,
        number=8,
    )
    vmware_engine_network_canonical: str = proto.Field(
        proto.STRING,
        number=9,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=10,
        enum=Type,
    )
    peering_id: str = proto.Field(
        proto.STRING,
        number=12,
    )
    routing_mode: RoutingMode = proto.Field(
        proto.ENUM,
        number=13,
        enum=RoutingMode,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=14,
    )
    service_network: str = proto.Field(
        proto.STRING,
        number=16,
    )
    peering_state: PeeringState = proto.Field(
        proto.ENUM,
        number=17,
        enum=PeeringState,
    )


class LocationMetadata(proto.Message):
    r"""VmwareEngine specific metadata for the given
    [google.cloud.location.Location][google.cloud.location.Location]. It
    is returned as a content of the
    ``google.cloud.location.Location.metadata`` field.

    Attributes:
        capabilities (MutableSequence[google.cloud.vmwareengine_v1.types.LocationMetadata.Capability]):
            Output only. Capabilities of this location.
    """

    class Capability(proto.Enum):
        r"""Capability of a location.

        Values:
            CAPABILITY_UNSPECIFIED (0):
                The default value. This value is used if the
                capability is omitted or unknown.
            STRETCHED_CLUSTERS (1):
                Stretch clusters are supported in this
                location.
        """

        CAPABILITY_UNSPECIFIED = 0
        STRETCHED_CLUSTERS = 1

    capabilities: MutableSequence[Capability] = proto.RepeatedField(
        proto.ENUM,
        number=1,
        enum=Capability,
    )


class DnsBindPermission(proto.Message):
    r"""DnsBindPermission resource that contains the accounts having
    the consumer DNS bind permission on the corresponding intranet
    VPC of the consumer project.

    Attributes:
        name (str):
            Required. Output only. The name of the resource which stores
            the users/service accounts having the permission to bind to
            the corresponding intranet VPC of the consumer project.
            DnsBindPermission is a global resource and location can only
            be global. Resource names are schemeless URIs that follow
            the conventions in
            https://cloud.google.com/apis/design/resource_names. For
            example:
            ``projects/my-project/locations/global/dnsBindPermission``
        principals (MutableSequence[google.cloud.vmwareengine_v1.types.Principal]):
            Output only. Users/Service accounts which
            have access for binding on the intranet VPC
            project corresponding to the consumer project.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    principals: MutableSequence["Principal"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Principal",
    )


class Principal(proto.Message):
    r"""Users/Service accounts which have access for DNS binding on
    the intranet VPC corresponding to the consumer project.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        user (str):
            The user who needs to be granted permission.

            This field is a member of `oneof`_ ``principal``.
        service_account (str):
            The service account which needs to be granted
            the permission.

            This field is a member of `oneof`_ ``principal``.
    """

    user: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="principal",
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="principal",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
