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
    package="google.cloud.networkconnectivity.v1",
    manifest={
        "PolicyBasedRoute",
        "ListPolicyBasedRoutesRequest",
        "ListPolicyBasedRoutesResponse",
        "GetPolicyBasedRouteRequest",
        "CreatePolicyBasedRouteRequest",
        "DeletePolicyBasedRouteRequest",
    },
)


class PolicyBasedRoute(proto.Message):
    r"""Policy-based routes route L4 network traffic based on not
    just destination IP address, but also source IP address,
    protocol, and more. If a policy-based route conflicts with other
    types of routes, the policy-based route always takes precedence.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        virtual_machine (google.cloud.networkconnectivity_v1.types.PolicyBasedRoute.VirtualMachine):
            Optional. VM instances that this policy-based
            route applies to.

            This field is a member of `oneof`_ ``target``.
        interconnect_attachment (google.cloud.networkconnectivity_v1.types.PolicyBasedRoute.InterconnectAttachment):
            Optional. The interconnect attachments that
            this policy-based route applies to.

            This field is a member of `oneof`_ ``target``.
        next_hop_ilb_ip (str):
            Optional. The IP address of a
            global-access-enabled L4 ILB that is the next
            hop for matching packets. For this version, only
            nextHopIlbIp is supported.

            This field is a member of `oneof`_ ``next_hop``.
        next_hop_other_routes (google.cloud.networkconnectivity_v1.types.PolicyBasedRoute.OtherRoutes):
            Optional. Other routes that will be
            referenced to determine the next hop of the
            packet.

            This field is a member of `oneof`_ ``next_hop``.
        name (str):
            Immutable. A unique name of the resource in the form of
            ``projects/{project_number}/locations/global/PolicyBasedRoutes/{policy_based_route_id}``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the policy-based route
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the policy-based route
            was updated.
        labels (MutableMapping[str, str]):
            User-defined labels.
        description (str):
            Optional. An optional description of this
            resource. Provide this field when you create the
            resource.
        network (str):
            Required. Fully-qualified URL of the network
            that this route applies to, for example:
            projects/my-project/global/networks/my-network.
        filter (google.cloud.networkconnectivity_v1.types.PolicyBasedRoute.Filter):
            Required. The filter to match L4 traffic.
        priority (int):
            Optional. The priority of this policy-based
            route. Priority is used to break ties in cases
            where there are more than one matching
            policy-based routes found. In cases where
            multiple policy-based routes are matched, the
            one with the lowest-numbered priority value
            wins. The default value is
            1000. The priority value must be from 1 to
                65535, inclusive.
        warnings (MutableSequence[google.cloud.networkconnectivity_v1.types.PolicyBasedRoute.Warnings]):
            Output only. If potential misconfigurations
            are detected for this route, this field will be
            populated with warning messages.
        self_link (str):
            Output only. Server-defined fully-qualified
            URL for this resource.
        kind (str):
            Output only. Type of this resource. Always
            networkconnectivity#policyBasedRoute for
            policy-based Route resources.
    """

    class OtherRoutes(proto.Enum):
        r"""The other routing cases.

        Values:
            OTHER_ROUTES_UNSPECIFIED (0):
                Default value.
            DEFAULT_ROUTING (1):
                Use the routes from the default routing
                tables (system-generated routes, custom routes,
                peering route) to determine the next hop. This
                effectively excludes matching packets being
                applied on other PBRs with a lower priority.
        """

        OTHER_ROUTES_UNSPECIFIED = 0
        DEFAULT_ROUTING = 1

    class VirtualMachine(proto.Message):
        r"""VM instances that this policy-based route applies to.

        Attributes:
            tags (MutableSequence[str]):
                Optional. A list of VM instance tags that
                this policy-based route applies to. VM instances
                that have ANY of tags specified here installs
                this PBR.
        """

        tags: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    class InterconnectAttachment(proto.Message):
        r"""InterconnectAttachment that this route applies to.

        Attributes:
            region (str):
                Optional. Cloud region to install this policy-based route on
                interconnect attachment. Use ``all`` to install it on all
                interconnect attachments.
        """

        region: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class Filter(proto.Message):
        r"""Filter matches L4 traffic.

        Attributes:
            ip_protocol (str):
                Optional. The IP protocol that this
                policy-based route applies to. Valid values are
                'TCP', 'UDP', and 'ALL'. Default is 'ALL'.
            src_range (str):
                Optional. The source IP range of outgoing
                packets that this policy-based route applies to.
                Default is "0.0.0.0/0" if protocol version is
                IPv4.
            dest_range (str):
                Optional. The destination IP range of
                outgoing packets that this policy-based route
                applies to. Default is "0.0.0.0/0" if protocol
                version is IPv4.
            protocol_version (google.cloud.networkconnectivity_v1.types.PolicyBasedRoute.Filter.ProtocolVersion):
                Required. Internet protocol versions this
                policy-based route applies to. For this version,
                only IPV4 is supported. IPV6 is supported in
                preview.
        """

        class ProtocolVersion(proto.Enum):
            r"""The internet protocol version.

            Values:
                PROTOCOL_VERSION_UNSPECIFIED (0):
                    Default value.
                IPV4 (1):
                    The PBR is for IPv4 internet protocol
                    traffic.
            """

            PROTOCOL_VERSION_UNSPECIFIED = 0
            IPV4 = 1

        ip_protocol: str = proto.Field(
            proto.STRING,
            number=1,
        )
        src_range: str = proto.Field(
            proto.STRING,
            number=2,
        )
        dest_range: str = proto.Field(
            proto.STRING,
            number=3,
        )
        protocol_version: "PolicyBasedRoute.Filter.ProtocolVersion" = proto.Field(
            proto.ENUM,
            number=6,
            enum="PolicyBasedRoute.Filter.ProtocolVersion",
        )

    class Warnings(proto.Message):
        r"""Informational warning message.

        Attributes:
            code (google.cloud.networkconnectivity_v1.types.PolicyBasedRoute.Warnings.Code):
                Output only. A warning code, if applicable.
            data (MutableMapping[str, str]):
                Output only. Metadata about this warning in
                key: value format. The key should provides more
                detail on the warning being returned. For
                example, for warnings where there are no results
                in a list request for a particular zone, this
                key might be scope and the key value might be
                the zone name. Other examples might be a key
                indicating a deprecated resource and a suggested
                replacement.
            warning_message (str):
                Output only. A human-readable description of
                the warning code.
        """

        class Code(proto.Enum):
            r"""Warning code for policy-based routing. Expect to add values
            in the future.

            Values:
                WARNING_UNSPECIFIED (0):
                    Default value.
                RESOURCE_NOT_ACTIVE (1):
                    The policy-based route is not active and
                    functioning. Common causes are that the
                    dependent network was deleted or the resource
                    project was turned off.
                RESOURCE_BEING_MODIFIED (2):
                    The policy-based route is being modified
                    (e.g. created/deleted) at this time.
            """

            WARNING_UNSPECIFIED = 0
            RESOURCE_NOT_ACTIVE = 1
            RESOURCE_BEING_MODIFIED = 2

        code: "PolicyBasedRoute.Warnings.Code" = proto.Field(
            proto.ENUM,
            number=1,
            enum="PolicyBasedRoute.Warnings.Code",
        )
        data: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=2,
        )
        warning_message: str = proto.Field(
            proto.STRING,
            number=3,
        )

    virtual_machine: VirtualMachine = proto.Field(
        proto.MESSAGE,
        number=18,
        oneof="target",
        message=VirtualMachine,
    )
    interconnect_attachment: InterconnectAttachment = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="target",
        message=InterconnectAttachment,
    )
    next_hop_ilb_ip: str = proto.Field(
        proto.STRING,
        number=12,
        oneof="next_hop",
    )
    next_hop_other_routes: OtherRoutes = proto.Field(
        proto.ENUM,
        number=21,
        oneof="next_hop",
        enum=OtherRoutes,
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
    filter: Filter = proto.Field(
        proto.MESSAGE,
        number=10,
        message=Filter,
    )
    priority: int = proto.Field(
        proto.INT32,
        number=11,
    )
    warnings: MutableSequence[Warnings] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message=Warnings,
    )
    self_link: str = proto.Field(
        proto.STRING,
        number=15,
    )
    kind: str = proto.Field(
        proto.STRING,
        number=16,
    )


class ListPolicyBasedRoutesRequest(proto.Message):
    r"""Request for
    [PolicyBasedRoutingService.ListPolicyBasedRoutes][google.cloud.networkconnectivity.v1.PolicyBasedRoutingService.ListPolicyBasedRoutes]
    method.

    Attributes:
        parent (str):
            Required. The parent resource's name.
        page_size (int):
            The maximum number of results per page that
            should be returned.
        page_token (str):
            The page token.
        filter (str):
            A filter expression that filters the results
            listed in the response.
        order_by (str):
            Sort the results by a certain order.
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


class ListPolicyBasedRoutesResponse(proto.Message):
    r"""Response for
    [PolicyBasedRoutingService.ListPolicyBasedRoutes][google.cloud.networkconnectivity.v1.PolicyBasedRoutingService.ListPolicyBasedRoutes]
    method.

    Attributes:
        policy_based_routes (MutableSequence[google.cloud.networkconnectivity_v1.types.PolicyBasedRoute]):
            Policy-based routes to be returned.
        next_page_token (str):
            The next pagination token in the List response. It should be
            used as page_token for the following request. An empty value
            means no more result.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    policy_based_routes: MutableSequence["PolicyBasedRoute"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="PolicyBasedRoute",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetPolicyBasedRouteRequest(proto.Message):
    r"""Request for
    [PolicyBasedRoutingService.GetPolicyBasedRoute][google.cloud.networkconnectivity.v1.PolicyBasedRoutingService.GetPolicyBasedRoute]
    method.

    Attributes:
        name (str):
            Required. Name of the PolicyBasedRoute
            resource to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreatePolicyBasedRouteRequest(proto.Message):
    r"""Request for
    [PolicyBasedRoutingService.CreatePolicyBasedRoute][google.cloud.networkconnectivity.v1.PolicyBasedRoutingService.CreatePolicyBasedRoute]
    method.

    Attributes:
        parent (str):
            Required. The parent resource's name of the
            PolicyBasedRoute.
        policy_based_route_id (str):
            Required. Unique id for the policy-based route to create.
            Provided by the client when the resource is created. The
            name must comply with
            https://google.aip.dev/122#resource-id-segments.
            Specifically, the name must be 1-63 characters long and
            match the regular expression `a-z <[a-z0-9-]*[a-z0-9]>`__?.
            The first character must be a lowercase letter, and all
            following characters (except for the last character) must be
            a dash, lowercase letter, or digit. The last character must
            be a lowercase letter or digit.
        policy_based_route (google.cloud.networkconnectivity_v1.types.PolicyBasedRoute):
            Required. Initial values for a new
            policy-based route.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server knows to
            ignore the request if it has already been
            completed. The server guarantees that for at
            least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, ignores the second request. This prevents
            clients from accidentally creating duplicate
            commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    policy_based_route_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    policy_based_route: "PolicyBasedRoute" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="PolicyBasedRoute",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeletePolicyBasedRouteRequest(proto.Message):
    r"""Request for
    [PolicyBasedRoutingService.DeletePolicyBasedRoute][google.cloud.networkconnectivity.v1.PolicyBasedRoutingService.DeletePolicyBasedRoute]
    method.

    Attributes:
        name (str):
            Required. Name of the policy-based route
            resource to delete.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server knows to
            ignore the request if it has already been
            completed. The server guarantees that for at
            least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, ignores the second request. This prevents
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


__all__ = tuple(sorted(__protobuf__.manifest))
