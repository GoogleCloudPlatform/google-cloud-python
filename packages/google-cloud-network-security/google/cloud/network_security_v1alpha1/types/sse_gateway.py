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

__protobuf__ = proto.module(
    package="google.cloud.networksecurity.v1alpha1",
    manifest={
        "PartnerSSEGateway",
        "ListPartnerSSEGatewaysRequest",
        "ListPartnerSSEGatewaysResponse",
        "GetPartnerSSEGatewayRequest",
        "CreatePartnerSSEGatewayRequest",
        "DeletePartnerSSEGatewayRequest",
        "UpdatePartnerSSEGatewayRequest",
        "SSEGatewayReference",
        "ListSSEGatewayReferencesRequest",
        "ListSSEGatewayReferencesResponse",
        "GetSSEGatewayReferenceRequest",
    },
)


class PartnerSSEGateway(proto.Message):
    r"""Message describing PartnerSSEGateway object

    Attributes:
        name (str):
            Immutable. name of resource
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time stamp
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update time stamp
        labels (MutableMapping[str, str]):
            Optional. Labels as key value pairs
        sse_vpc_subnet_range (str):
            Output only. Subnet range of the subnet where partner
            traffic is routed. This field is deprecated. Use
            sse_subnet_range instead.
        sse_vpc_target_ip (str):
            Output only. This is the IP where the partner traffic should
            be routed to. This field is deprecated. Use sse_target_ip
            instead.
        sse_gateway_reference_id (str):
            Required. ID of the SSEGatewayReference that
            pairs with this PartnerSSEGateway
        sse_bgp_ips (MutableSequence[str]):
            Output only. IP of SSE BGP
        sse_bgp_asn (int):
            Output only. ASN of SSE BGP
        partner_vpc_subnet_range (str):
            Optional. Subnet range of the partner_vpc This field is
            deprecated. Use partner_subnet_range instead.
        partner_sse_realm (str):
            Output only. name of PartnerSSERealm owning
            the PartnerSSEGateway
        sse_subnet_range (str):
            Optional. Subnet range where SSE GW instances
            are deployed. Default value is set to
            "100.88.255.0/24". The CIDR suffix should be
            less than or equal to 25.
        sse_target_ip (str):
            Output only. Target IP that belongs to sse_subnet_range
            where partner should send the traffic to reach the customer
            networks.
        partner_subnet_range (str):
            Optional. Subnet range of the partner-owned
            subnet.
        vni (int):
            Optional. Virtual Network Identifier to use
            in NCG. Today the only partner that depends on
            it is Symantec.
        symantec_options (google.cloud.network_security_v1alpha1.types.PartnerSSEGateway.PartnerSSEGatewaySymantecOptions):
            Optional. Required iff Partner is Symantec.
        sse_project (str):
            Output only. The project owning partner_facing_network. Only
            filled for PartnerSSEGateways associated with Symantec
            today.
        sse_network (str):
            Output only. The ID of the network in sse_project containing
            sse_subnet_range. This is also known as the
            partnerFacingNetwork. Only filled for PartnerSSEGateways
            associated with Symantec today.
        partner_sse_environment (str):
            Output only. Full URI of the partner
            environment this PartnerSSEGateway is connected
            to. Filled from the customer SSEGateway, and
            only for PartnerSSEGateways associated with
            Symantec today.
        country (str):
            Output only. ISO-3166 alpha 2 country code
            used for localization. Filled from the customer
            SSEGateway, and only for PartnerSSEGateways
            associated with Symantec today.
        timezone (str):
            Output only. tzinfo identifier used for
            localization. Filled from the customer
            SSEGateway, and only for PartnerSSEGateways
            associated with Symantec today.
        capacity_bps (int):
            Output only. Copied from the associated NCC
            resource in Symantec NCCGW flows. Used by
            Symantec API.
        state (google.cloud.network_security_v1alpha1.types.PartnerSSEGateway.State):
            Output only. State of the gateway.
        prober_subnet_ranges (MutableSequence[str]):
            Output only. Subnet ranges for Google-issued
            probe packets. It's populated only for Prisma
            Access partners.
    """

    class State(proto.Enum):
        r"""State of the gateway.

        Values:
            STATE_UNSPECIFIED (0):
                No state specified. This should not be used.
            CUSTOMER_ATTACHED (1):
                Attached to a customer. This is the default
                state when a gateway is successfully created.
            CUSTOMER_DETACHED (2):
                No longer attached to a customer. This state
                arises when the customer attachment is deleted.
        """

        STATE_UNSPECIFIED = 0
        CUSTOMER_ATTACHED = 1
        CUSTOMER_DETACHED = 2

    class PartnerSSEGatewaySymantecOptions(proto.Message):
        r"""Options specific to gateways connected to Symantec.

        Attributes:
            symantec_location_uuid (str):
                Output only. UUID of the Symantec Location
                created on the customer's behalf.
            symantec_site_target_host (str):
                Optional. Target for the NCGs to send traffic
                to on the Symantec side. Only supports IP
                address today.
            symantec_site (str):
                Output only. Symantec data center identifier
                that this SSEGW will connect to. Filled from the
                customer SSEGateway, and only for
                PartnerSSEGateways associated with Symantec
                today.
        """

        symantec_location_uuid: str = proto.Field(
            proto.STRING,
            number=1,
        )
        symantec_site_target_host: str = proto.Field(
            proto.STRING,
            number=2,
        )
        symantec_site: str = proto.Field(
            proto.STRING,
            number=3,
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
    sse_vpc_subnet_range: str = proto.Field(
        proto.STRING,
        number=5,
    )
    sse_vpc_target_ip: str = proto.Field(
        proto.STRING,
        number=6,
    )
    sse_gateway_reference_id: str = proto.Field(
        proto.STRING,
        number=7,
    )
    sse_bgp_ips: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    sse_bgp_asn: int = proto.Field(
        proto.INT32,
        number=9,
    )
    partner_vpc_subnet_range: str = proto.Field(
        proto.STRING,
        number=11,
    )
    partner_sse_realm: str = proto.Field(
        proto.STRING,
        number=12,
    )
    sse_subnet_range: str = proto.Field(
        proto.STRING,
        number=17,
    )
    sse_target_ip: str = proto.Field(
        proto.STRING,
        number=18,
    )
    partner_subnet_range: str = proto.Field(
        proto.STRING,
        number=19,
    )
    vni: int = proto.Field(
        proto.INT32,
        number=20,
    )
    symantec_options: PartnerSSEGatewaySymantecOptions = proto.Field(
        proto.MESSAGE,
        number=21,
        message=PartnerSSEGatewaySymantecOptions,
    )
    sse_project: str = proto.Field(
        proto.STRING,
        number=22,
    )
    sse_network: str = proto.Field(
        proto.STRING,
        number=23,
    )
    partner_sse_environment: str = proto.Field(
        proto.STRING,
        number=24,
    )
    country: str = proto.Field(
        proto.STRING,
        number=25,
    )
    timezone: str = proto.Field(
        proto.STRING,
        number=26,
    )
    capacity_bps: int = proto.Field(
        proto.INT64,
        number=28,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=29,
        enum=State,
    )
    prober_subnet_ranges: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=30,
    )


class ListPartnerSSEGatewaysRequest(proto.Message):
    r"""Message for requesting list of PartnerSSEGateways

    Attributes:
        parent (str):
            Required. Parent value for
            ListPartnerSSEGatewaysRequest
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Filtering results
        order_by (str):
            Hint for how to order the results
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


class ListPartnerSSEGatewaysResponse(proto.Message):
    r"""Message for response to listing PartnerSSEGateways

    Attributes:
        partner_sse_gateways (MutableSequence[google.cloud.network_security_v1alpha1.types.PartnerSSEGateway]):
            The list of PartnerSSEGateway
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    partner_sse_gateways: MutableSequence["PartnerSSEGateway"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="PartnerSSEGateway",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetPartnerSSEGatewayRequest(proto.Message):
    r"""Message for getting a PartnerSSEGateway

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreatePartnerSSEGatewayRequest(proto.Message):
    r"""Message for creating a PartnerSSEGateway

    Attributes:
        parent (str):
            Required. Value for parent.
        partner_sse_gateway_id (str):
            Required. Id of the requesting object If auto-generating Id
            server-side, remove this field and partner_sse_gateway_id
            from the method_signature of Create RPC
        partner_sse_gateway (google.cloud.network_security_v1alpha1.types.PartnerSSEGateway):
            Required. The resource being created
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
    partner_sse_gateway_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    partner_sse_gateway: "PartnerSSEGateway" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="PartnerSSEGateway",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeletePartnerSSEGatewayRequest(proto.Message):
    r"""Message for deleting a PartnerSSEGateway

    Attributes:
        name (str):
            Required. Name of the resource
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

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

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdatePartnerSSEGatewayRequest(proto.Message):
    r"""Message for deleting a PartnerSSEGateway

    Attributes:
        partner_sse_gateway (google.cloud.network_security_v1alpha1.types.PartnerSSEGateway):
            Required. The resource being created
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to update
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

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

    partner_sse_gateway: "PartnerSSEGateway" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="PartnerSSEGateway",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SSEGatewayReference(proto.Message):
    r"""Message describing SSEGatewayReference object

    Attributes:
        name (str):
            Immutable. name of resource
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time stamp
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update time stamp
        labels (MutableMapping[str, str]):
            Optional. Labels as key value pairs
        partner_sse_realm (str):
            Output only. PartnerSSERealm owning the
            PartnerSSEGateway that this SSEGateway intends
            to connect with
        prober_subnet_ranges (MutableSequence[str]):
            Output only. Subnet ranges for Google probe
            packets.
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
    partner_sse_realm: str = proto.Field(
        proto.STRING,
        number=5,
    )
    prober_subnet_ranges: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )


class ListSSEGatewayReferencesRequest(proto.Message):
    r"""Message for requesting list of SSEGatewayReferences

    Attributes:
        parent (str):
            Required. Parent value for
            ListSSEGatewayReferencesRequest
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Filtering results
        order_by (str):
            Hint for how to order the results
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


class ListSSEGatewayReferencesResponse(proto.Message):
    r"""Message for response to listing SSEGatewayReferences

    Attributes:
        sse_gateway_references (MutableSequence[google.cloud.network_security_v1alpha1.types.SSEGatewayReference]):
            The list of SSEGatewayReference
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    sse_gateway_references: MutableSequence["SSEGatewayReference"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="SSEGatewayReference",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetSSEGatewayReferenceRequest(proto.Message):
    r"""Message for getting a SSEGatewayReference

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
