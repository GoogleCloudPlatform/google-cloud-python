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

from google.cloud.network_services_v1.types import common

__protobuf__ = proto.module(
    package="google.cloud.networkservices.v1",
    manifest={
        "Gateway",
        "ListGatewaysRequest",
        "ListGatewaysResponse",
        "GetGatewayRequest",
        "CreateGatewayRequest",
        "UpdateGatewayRequest",
        "DeleteGatewayRequest",
    },
)


class Gateway(proto.Message):
    r"""Gateway represents the configuration for a proxy, typically a
    load balancer. It captures the ip:port over which the services
    are exposed by the proxy, along with any policy configurations.
    Routes have reference to to Gateways to dictate how requests
    should be routed by this Gateway.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. Name of the Gateway resource. It matches pattern
            ``projects/*/locations/*/gateways/<gateway_name>``.
        self_link (str):
            Output only. Server-defined URL of this
            resource
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was updated.
        labels (MutableMapping[str, str]):
            Optional. Set of label tags associated with
            the Gateway resource.
        description (str):
            Optional. A free-text description of the
            resource. Max length 1024 characters.
        type_ (google.cloud.network_services_v1.types.Gateway.Type):
            Immutable. The type of the customer managed
            gateway. This field is required. If unspecified,
            an error is returned.
        addresses (MutableSequence[str]):
            Optional. Zero or one IPv4 or IPv6 address on which the
            Gateway will receive the traffic. When no address is
            provided, an IP from the subnetwork is allocated

            This field only applies to gateways of type
            'SECURE_WEB_GATEWAY'. Gateways of type 'OPEN_MESH' listen on
            0.0.0.0 for IPv4 and :: for IPv6.
        ports (MutableSequence[int]):
            Required. One or more port numbers (1-65535), on which the
            Gateway will receive traffic. The proxy binds to the
            specified ports. Gateways of type 'SECURE_WEB_GATEWAY' are
            limited to 5 ports. Gateways of type 'OPEN_MESH' listen on
            0.0.0.0 for IPv4 and :: for IPv6 and support multiple ports.
        all_ports (bool):
            Optional. If true, the Gateway will listen on all ports.
            This is mutually exclusive with the ``ports`` field. This
            field only applies to gateways of type 'SECURE_WEB_GATEWAY'.
        scope (str):
            Optional. Scope determines how configuration
            across multiple Gateway instances are merged.
            The configuration for multiple Gateway instances
            with the same scope will be merged as presented
            as a single configuration to the proxy/load
            balancer.

            Max length 64 characters.
            Scope should start with a letter and can only
            have letters, numbers, hyphens.
        server_tls_policy (str):
            Optional. A fully-qualified ServerTLSPolicy
            URL reference. Specifies how TLS traffic is
            terminated. If empty, TLS termination is
            disabled.
        certificate_urls (MutableSequence[str]):
            Optional. A fully-qualified Certificates URL reference. The
            proxy presents a Certificate (selected based on SNI) when
            establishing a TLS connection. This feature only applies to
            gateways of type 'SECURE_WEB_GATEWAY'.
        gateway_security_policy (str):
            Optional. A fully-qualified GatewaySecurityPolicy URL
            reference. Defines how a server should apply security policy
            to inbound (VM to Proxy) initiated connections.

            For example:
            ``projects/*/locations/*/gatewaySecurityPolicies/swg-policy``.

            This policy is specific to gateways of type
            'SECURE_WEB_GATEWAY'.
        network (str):
            Optional. The relative resource name identifying the VPC
            network that is using this configuration. For example:
            ``projects/*/global/networks/network-1``.

            Currently, this field is specific to gateways of type
            'SECURE_WEB_GATEWAY'.
        subnetwork (str):
            Optional. The relative resource name identifying the
            subnetwork in which this SWG is allocated. For example:
            ``projects/*/regions/us-central1/subnetworks/network-1``

            Currently, this field is specific to gateways of type
            'SECURE_WEB_GATEWAY".
        ip_version (google.cloud.network_services_v1.types.Gateway.IpVersion):
            Optional. The IP Version that will be used by
            this gateway. Valid options are IPV4 or IPV6.
            Default is IPV4.
        envoy_headers (google.cloud.network_services_v1.types.EnvoyHeaders):
            Optional. Determines if envoy will insert
            internal debug headers into upstream requests.
            Other Envoy headers may still be injected. By
            default, envoy will not insert any debug
            headers.

            This field is a member of `oneof`_ ``_envoy_headers``.
        routing_mode (google.cloud.network_services_v1.types.Gateway.RoutingMode):
            Optional. The routing mode of the Gateway. This field is
            configurable only for gateways of type SECURE_WEB_GATEWAY.
            This field is required for gateways of type
            SECURE_WEB_GATEWAY.
        allow_global_access (bool):
            Optional. If true, the gateway will allow traffic from
            clients outside of the region where the gateway is located.
            This field is configurable only for gateways of type
            SECURE_WEB_GATEWAY.
    """

    class Type(proto.Enum):
        r"""The type of the customer-managed gateway. Possible values are:

        - OPEN_MESH
        - SECURE_WEB_GATEWAY

        Values:
            TYPE_UNSPECIFIED (0):
                The type of the customer managed gateway is
                unspecified.
            OPEN_MESH (1):
                The type of the customer managed gateway is
                TrafficDirector Open Mesh.
            SECURE_WEB_GATEWAY (2):
                The type of the customer managed gateway is
                SecureWebGateway (SWG).
        """

        TYPE_UNSPECIFIED = 0
        OPEN_MESH = 1
        SECURE_WEB_GATEWAY = 2

    class IpVersion(proto.Enum):
        r"""The types of IP version for the gateway. Possible values are:

        - IPV4
        - IPV6

        Values:
            IP_VERSION_UNSPECIFIED (0):
                The type when IP version is not specified.
                Defaults to IPV4.
            IPV4 (1):
                The type for IP version 4.
            IPV6 (2):
                The type for IP version 6.
        """

        IP_VERSION_UNSPECIFIED = 0
        IPV4 = 1
        IPV6 = 2

    class RoutingMode(proto.Enum):
        r"""The routing mode of the Gateway, to determine how the Gateway routes
        traffic. Today, this field only applies to Gateways of type
        SECURE_WEB_GATEWAY. Possible values are:

        - EXPLICIT_ROUTING_MODE
        - NEXT_HOP_ROUTING_MODE

        Values:
            EXPLICIT_ROUTING_MODE (0):
                The routing mode is explicit; clients are
                configured to send traffic through the gateway.
                This is the default routing mode.
            NEXT_HOP_ROUTING_MODE (1):
                The routing mode is next-hop. Clients are
                unaware of the gateway, and a route (advanced
                route or other route type) can be configured to
                direct traffic from client to gateway. The
                gateway then acts as a next-hop to the
                destination.
        """

        EXPLICIT_ROUTING_MODE = 0
        NEXT_HOP_ROUTING_MODE = 1

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    self_link: str = proto.Field(
        proto.STRING,
        number=13,
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
    type_: Type = proto.Field(
        proto.ENUM,
        number=6,
        enum=Type,
    )
    addresses: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    ports: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=11,
    )
    all_ports: bool = proto.Field(
        proto.BOOL,
        number=34,
    )
    scope: str = proto.Field(
        proto.STRING,
        number=8,
    )
    server_tls_policy: str = proto.Field(
        proto.STRING,
        number=9,
    )
    certificate_urls: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=14,
    )
    gateway_security_policy: str = proto.Field(
        proto.STRING,
        number=18,
    )
    network: str = proto.Field(
        proto.STRING,
        number=16,
    )
    subnetwork: str = proto.Field(
        proto.STRING,
        number=17,
    )
    ip_version: IpVersion = proto.Field(
        proto.ENUM,
        number=21,
        enum=IpVersion,
    )
    envoy_headers: common.EnvoyHeaders = proto.Field(
        proto.ENUM,
        number=28,
        optional=True,
        enum=common.EnvoyHeaders,
    )
    routing_mode: RoutingMode = proto.Field(
        proto.ENUM,
        number=32,
        enum=RoutingMode,
    )
    allow_global_access: bool = proto.Field(
        proto.BOOL,
        number=33,
    )


class ListGatewaysRequest(proto.Message):
    r"""Request used with the ListGateways method.

    Attributes:
        parent (str):
            Required. The project and location from which the Gateways
            should be listed, specified in the format
            ``projects/*/locations/*``.
        page_size (int):
            Maximum number of Gateways to return per
            call.
        page_token (str):
            The value returned by the last ``ListGatewaysResponse``
            Indicates that this is a continuation of a prior
            ``ListGateways`` call, and that the system should return the
            next page of data.
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


class ListGatewaysResponse(proto.Message):
    r"""Response returned by the ListGateways method.

    Attributes:
        gateways (MutableSequence[google.cloud.network_services_v1.types.Gateway]):
            List of Gateway resources.
        next_page_token (str):
            If there might be more results than those appearing in this
            response, then ``next_page_token`` is included. To get the
            next set of results, call this method again using the value
            of ``next_page_token`` as ``page_token``.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    gateways: MutableSequence["Gateway"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Gateway",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetGatewayRequest(proto.Message):
    r"""Request used by the GetGateway method.

    Attributes:
        name (str):
            Required. A name of the Gateway to get. Must be in the
            format ``projects/*/locations/*/gateways/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateGatewayRequest(proto.Message):
    r"""Request used by the CreateGateway method.

    Attributes:
        parent (str):
            Required. The parent resource of the Gateway. Must be in the
            format ``projects/*/locations/*``.
        gateway_id (str):
            Required. Short name of the Gateway resource
            to be created.
        gateway (google.cloud.network_services_v1.types.Gateway):
            Required. Gateway resource to be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    gateway_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    gateway: "Gateway" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Gateway",
    )


class UpdateGatewayRequest(proto.Message):
    r"""Request used by the UpdateGateway method.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the Gateway resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        gateway (google.cloud.network_services_v1.types.Gateway):
            Required. Updated Gateway resource.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    gateway: "Gateway" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Gateway",
    )


class DeleteGatewayRequest(proto.Message):
    r"""Request used by the DeleteGateway method.

    Attributes:
        name (str):
            Required. A name of the Gateway to delete. Must be in the
            format ``projects/*/locations/*/gateways/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
