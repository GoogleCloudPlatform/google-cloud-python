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
    package="google.cloud.networkservices.v1",
    manifest={
        "AgentGateway",
        "ListAgentGatewaysRequest",
        "ListAgentGatewaysResponse",
        "GetAgentGatewayRequest",
        "CreateAgentGatewayRequest",
        "UpdateAgentGatewayRequest",
        "DeleteAgentGatewayRequest",
    },
)


class AgentGateway(proto.Message):
    r"""AgentGateway represents the agent gateway resource.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        google_managed (google.cloud.network_services_v1.types.AgentGateway.GoogleManaged):
            Optional. Proxy is orchestrated and managed
            by GoogleCloud in a tenant project.

            This field is a member of `oneof`_ ``deployment_mode``.
        self_managed (google.cloud.network_services_v1.types.AgentGateway.SelfManaged):
            Optional. Attach to existing Application Load
            Balancers or Secure Web Proxies.

            This field is a member of `oneof`_ ``deployment_mode``.
        name (str):
            Identifier. Name of the AgentGateway resource. It matches
            pattern
            ``projects/*/locations/*/agentGateways/<agent_gateway>``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was updated.
        labels (MutableMapping[str, str]):
            Optional. Set of label tags associated with
            the AgentGateway resource.
        description (str):
            Optional. A free-text description of the
            resource. Max length 1024 characters.
        etag (str):
            Optional. Etag of the resource.
            If this is provided, it must match the server's
            etag. If the provided etag does not match the
            server's etag, the request will fail with a 409
            ABORTED error.
        protocols (MutableSequence[google.cloud.network_services_v1.types.AgentGateway.Protocol]):
            Optional. Deprecated.
        registries (MutableSequence[str]):
            Optional. A list of Agent registries containing the agents,
            MCP servers and tools governed by the Agent Gateway. Note:
            Currently limited to project-scoped registries Must be of
            format
            ``//agentregistry.googleapis.com/projects/{project}/locations/{location}/``
        network_config (google.cloud.network_services_v1.types.AgentGateway.NetworkConfig):
            Optional. Network configuration for the
            AgentGateway.
        agent_gateway_card (google.cloud.network_services_v1.types.AgentGateway.AgentGatewayOutputCard):
            Output only. Field for populated AgentGateway
            card.
    """

    class Protocol(proto.Enum):
        r"""Enums of all supported protocols

        Values:
            PROTOCOL_UNSPECIFIED (0):
                Unspecified protocol.
            MCP (1):
                Message Control Plane protocol.
        """

        PROTOCOL_UNSPECIFIED = 0
        MCP = 1

    class GoogleManaged(proto.Message):
        r"""Configuration for Google Managed deployment mode.
        Proxy is orchestrated and managed by GoogleCloud in a tenant
        project.

        Attributes:
            governed_access_path (google.cloud.network_services_v1.types.AgentGateway.GoogleManaged.GovernedAccessPath):
                Optional. Operating Mode of Agent Gateway.
        """

        class GovernedAccessPath(proto.Enum):
            r"""GovernedAccessPath defines the type of access to protect.

            Values:
                GOVERNED_ACCESS_PATH_UNSPECIFIED (0):
                    Governed access path is not specified.
                AGENT_TO_ANYWHERE (1):
                    Govern agent conections to destinations.
                CLIENT_TO_AGENT (2):
                    Protect connection to Agent or Tool.
            """

            GOVERNED_ACCESS_PATH_UNSPECIFIED = 0
            AGENT_TO_ANYWHERE = 1
            CLIENT_TO_AGENT = 2

        governed_access_path: "AgentGateway.GoogleManaged.GovernedAccessPath" = (
            proto.Field(
                proto.ENUM,
                number=1,
                enum="AgentGateway.GoogleManaged.GovernedAccessPath",
            )
        )

    class SelfManaged(proto.Message):
        r"""Configuration for Self Managed deployment mode.
        Attach to existing Application Load Balancers or Secure Web
        Proxies.

        Attributes:
            resource_uri (str):
                Optional. A supported Google Cloud networking
                proxy in the Project and Location
            resource_uris (MutableSequence[str]):
                Optional. List of supported Google Cloud networking proxies
                in the Project and Location. resource_uris is mutually
                exclusive with resource_uri.
        """

        resource_uri: str = proto.Field(
            proto.STRING,
            number=1,
        )
        resource_uris: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )

    class NetworkConfig(proto.Message):
        r"""NetworkConfig contains network configurations for the
        AgentGateway.

        Attributes:
            egress (google.cloud.network_services_v1.types.AgentGateway.NetworkConfig.Egress):
                Optional. Optional PSC-Interface network
                attachment for connectivity to your private VPCs
                network.
            dns_peering_config (google.cloud.network_services_v1.types.AgentGateway.NetworkConfig.DnsPeeringConfig):
                Optional. Optional DNS peering configuration
                for connectivity to your private VPC network.
        """

        class Egress(proto.Message):
            r"""Configuration for Egress

            Attributes:
                network_attachment (str):
                    Optional. The URI of the Network Attachment
                    resource.
                trust_config (google.cloud.network_services_v1.types.AgentGateway.NetworkConfig.Egress.TrustConfig):
                    Optional. TrustConfig defines the trust
                    configuration for egress.
            """

            class TrustConfig(proto.Message):
                r"""TrustConfig defines the trust configuration for egress.

                Attributes:
                    pem_certificates (MutableSequence[str]):
                        Required. PEM encoded root certificates used
                        to validate the identity of the upstream
                        servers/destinations during egress connections.
                """

                pem_certificates: MutableSequence[str] = proto.RepeatedField(
                    proto.STRING,
                    number=1,
                )

            network_attachment: str = proto.Field(
                proto.STRING,
                number=1,
            )
            trust_config: "AgentGateway.NetworkConfig.Egress.TrustConfig" = proto.Field(
                proto.MESSAGE,
                number=2,
                message="AgentGateway.NetworkConfig.Egress.TrustConfig",
            )

        class DnsPeeringConfig(proto.Message):
            r"""DNS peering config for the user VPC network.

            Attributes:
                domains (MutableSequence[str]):
                    Required. Domain names for which DNS queries
                    should be forwarded to the target network.
                target_project (str):
                    Required. Target project ID to which DNS
                    queries should be forwarded to. This can be the
                    same project that contains the AgentGateway or a
                    different project.
                target_network (str):
                    Required. Target network in 'target project' to which DNS
                    queries should be forwarded to. Must be in format of
                    ``projects/{project}/global/networks/{network}``.
            """

            domains: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=1,
            )
            target_project: str = proto.Field(
                proto.STRING,
                number=2,
            )
            target_network: str = proto.Field(
                proto.STRING,
                number=3,
            )

        egress: "AgentGateway.NetworkConfig.Egress" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="AgentGateway.NetworkConfig.Egress",
        )
        dns_peering_config: "AgentGateway.NetworkConfig.DnsPeeringConfig" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="AgentGateway.NetworkConfig.DnsPeeringConfig",
        )

    class AgentGatewayOutputCard(proto.Message):
        r"""AgentGatewayOutputCard contains informational output-only
        fields

        Attributes:
            mtls_endpoint (str):
                Output only. mTLS Endpoint associated with
                this AgentGateway
            root_certificates (MutableSequence[str]):
                Output only. Root Certificates for Agents to
                validate this AgentGateway
            service_extensions_service_account (str):
                Output only. Service Account used by Service
                Extensions to operate.
        """

        mtls_endpoint: str = proto.Field(
            proto.STRING,
            number=1,
        )
        root_certificates: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=5,
        )
        service_extensions_service_account: str = proto.Field(
            proto.STRING,
            number=4,
        )

    google_managed: GoogleManaged = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="deployment_mode",
        message=GoogleManaged,
    )
    self_managed: SelfManaged = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="deployment_mode",
        message=SelfManaged,
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
    etag: str = proto.Field(
        proto.STRING,
        number=6,
    )
    protocols: MutableSequence[Protocol] = proto.RepeatedField(
        proto.ENUM,
        number=12,
        enum=Protocol,
    )
    registries: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=13,
    )
    network_config: NetworkConfig = proto.Field(
        proto.MESSAGE,
        number=10,
        message=NetworkConfig,
    )
    agent_gateway_card: AgentGatewayOutputCard = proto.Field(
        proto.MESSAGE,
        number=11,
        message=AgentGatewayOutputCard,
    )


class ListAgentGatewaysRequest(proto.Message):
    r"""Request used with the ListAgentGateways method.

    Attributes:
        parent (str):
            Required. The project and location from which the
            AgentGateways should be listed, specified in the format
            ``projects/*/locations/*``.
        page_size (int):
            Optional. Maximum number of AgentGateways to
            return per call.
        page_token (str):
            Optional. The value returned by the last
            ``ListAgentGatewaysResponse`` Indicates that this is a
            continuation of a prior ``ListAgentGateways`` call, and that
            the system should return the next page of data.
        return_partial_success (bool):
            Optional. If true, allow partial responses
            for multi-regional Aggregated List requests.
            Otherwise if one of the locations is down or
            unreachable, the Aggregated List request will
            fail.
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
    return_partial_success: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class ListAgentGatewaysResponse(proto.Message):
    r"""Response returned by the ListAgentGateways method.

    Attributes:
        agent_gateways (MutableSequence[google.cloud.network_services_v1.types.AgentGateway]):
            List of AgentGateway resources.
        next_page_token (str):
            If there might be more results than those appearing in this
            response, then ``next_page_token`` is included. To get the
            next set of results, call this method again using the value
            of ``next_page_token`` as ``page_token``.
        unreachable (MutableSequence[str]):
            Unreachable resources. Populated when the
            request attempts to list all resources across
            all supported locations, while some locations
            are temporarily unavailable.
    """

    @property
    def raw_page(self):
        return self

    agent_gateways: MutableSequence["AgentGateway"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AgentGateway",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetAgentGatewayRequest(proto.Message):
    r"""Request used by the GetAgentGateway method.

    Attributes:
        name (str):
            Required. A name of the AgentGateway to get. Must be in the
            format ``projects/*/locations/*/agentGateways/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateAgentGatewayRequest(proto.Message):
    r"""Request used by the CreateAgentGateway method.

    Attributes:
        parent (str):
            Required. The parent resource of the AgentGateway. Must be
            in the format ``projects/*/locations/*``.
        agent_gateway_id (str):
            Required. Short name of the AgentGateway
            resource to be created.
        agent_gateway (google.cloud.network_services_v1.types.AgentGateway):
            Required. AgentGateway resource to be
            created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    agent_gateway_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    agent_gateway: "AgentGateway" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AgentGateway",
    )


class UpdateAgentGatewayRequest(proto.Message):
    r"""Request used by the UpdateAgentGateway method.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the AgentGateway resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        agent_gateway (google.cloud.network_services_v1.types.AgentGateway):
            Required. Updated AgentGateway resource.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    agent_gateway: "AgentGateway" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="AgentGateway",
    )


class DeleteAgentGatewayRequest(proto.Message):
    r"""Request used by the DeleteAgentGateway method.

    Attributes:
        name (str):
            Required. A name of the AgentGateway to delete. Must be in
            the format ``projects/*/locations/*/agentGateways/*``.
        etag (str):
            Optional. The etag of the AgentGateway to
            delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
