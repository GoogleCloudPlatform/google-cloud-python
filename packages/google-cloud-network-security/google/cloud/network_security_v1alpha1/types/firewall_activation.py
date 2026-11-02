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
        "FirewallEndpoint",
        "ListFirewallEndpointsRequest",
        "ListFirewallEndpointsResponse",
        "GetFirewallEndpointRequest",
        "CreateFirewallEndpointRequest",
        "UpdateFirewallEndpointRequest",
        "DeleteFirewallEndpointRequest",
        "FirewallEndpointAssociation",
        "ListFirewallEndpointAssociationsRequest",
        "ListFirewallEndpointAssociationsResponse",
        "GetFirewallEndpointAssociationRequest",
        "CreateFirewallEndpointAssociationRequest",
        "DeleteFirewallEndpointAssociationRequest",
        "UpdateFirewallEndpointAssociationRequest",
    },
)


class FirewallEndpoint(proto.Message):
    r"""Message describing Endpoint object.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Immutable. Identifier. Name of resource.
        description (str):
            Optional. Description of the firewall
            endpoint. Max length 2048 characters.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time stamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update time stamp
        labels (MutableMapping[str, str]):
            Optional. Labels as key value pairs
        state (google.cloud.network_security_v1alpha1.types.FirewallEndpoint.State):
            Output only. Current state of the endpoint.
        reconciling (bool):
            Output only. Whether reconciling is in
            progress, recommended per
            https://google.aip.dev/128.
        associated_networks (MutableSequence[str]):
            Output only. List of networks that are
            associated with this endpoint in the local zone.
            This is a projection of the
            FirewallEndpointAssociations pointing at this
            endpoint. A network will only appear in this
            list after traffic routing is fully configured.
            Format:

            projects/{project}/global/networks/{name}.
        associations (MutableSequence[google.cloud.network_security_v1alpha1.types.FirewallEndpoint.AssociationReference]):
            Output only. List of
            FirewallEndpointAssociations that are associated
            to this endpoint. An association will only
            appear in this list after traffic routing is
            fully configured.
        satisfies_pzs (bool):
            Output only. [Output Only] Reserved for future use.

            This field is a member of `oneof`_ ``_satisfies_pzs``.
        satisfies_pzi (bool):
            Output only. [Output Only] Reserved for future use.

            This field is a member of `oneof`_ ``_satisfies_pzi``.
        billing_project_id (str):
            Required. Project to bill on endpoint uptime
            usage.
        endpoint_settings (google.cloud.network_security_v1alpha1.types.FirewallEndpoint.EndpointSettings):
            Optional. Settings for the endpoint.
    """

    class State(proto.Enum):
        r"""Endpoint state.

        Values:
            STATE_UNSPECIFIED (0):
                Not set.
            CREATING (1):
                Being created.
            ACTIVE (2):
                Processing configuration updates.
            DELETING (3):
                Being deleted.
            INACTIVE (4):
                Down or in an error state.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        DELETING = 3
        INACTIVE = 4

    class AssociationReference(proto.Message):
        r"""This is a subset of the FirewallEndpointAssociation message,
        containing fields to be used by the consumer.

        Attributes:
            name (str):
                Output only. The resource name of the
                FirewallEndpointAssociation. Format:

                projects/{project}/locations/{location}/firewallEndpointAssociations/{id}
            network (str):
                Output only. The VPC network associated.
                Format:
                projects/{project}/global/networks/{name}.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        network: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class EndpointSettings(proto.Message):
        r"""Settings for the endpoint.

        Attributes:
            jumbo_frames_enabled (bool):
                Optional. Immutable. Indicates whether Jumbo
                Frames are enabled. Default value is false.
        """

        jumbo_frames_enabled: bool = proto.Field(
            proto.BOOL,
            number=1,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=9,
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
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    reconciling: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    associated_networks: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    associations: MutableSequence[AssociationReference] = proto.RepeatedField(
        proto.MESSAGE,
        number=13,
        message=AssociationReference,
    )
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=14,
        optional=True,
    )
    satisfies_pzi: bool = proto.Field(
        proto.BOOL,
        number=15,
        optional=True,
    )
    billing_project_id: str = proto.Field(
        proto.STRING,
        number=8,
    )
    endpoint_settings: EndpointSettings = proto.Field(
        proto.MESSAGE,
        number=19,
        message=EndpointSettings,
    )


class ListFirewallEndpointsRequest(proto.Message):
    r"""Message for requesting list of Endpoints

    Attributes:
        parent (str):
            Required. Parent value for
            ListEndpointsRequest
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Optional. Filtering results
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


class ListFirewallEndpointsResponse(proto.Message):
    r"""Message for response to listing Endpoints

    Attributes:
        firewall_endpoints (MutableSequence[google.cloud.network_security_v1alpha1.types.FirewallEndpoint]):
            The list of Endpoint
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    firewall_endpoints: MutableSequence["FirewallEndpoint"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="FirewallEndpoint",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetFirewallEndpointRequest(proto.Message):
    r"""Message for getting a Endpoint

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateFirewallEndpointRequest(proto.Message):
    r"""Message for creating a Endpoint

    Attributes:
        parent (str):
            Required. Value for parent.
        firewall_endpoint_id (str):
            Required. Id of the requesting object. If auto-generating Id
            server-side, remove this field and firewall_endpoint_id from
            the method_signature of Create RPC.
        firewall_endpoint (google.cloud.network_security_v1alpha1.types.FirewallEndpoint):
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
    firewall_endpoint_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    firewall_endpoint: "FirewallEndpoint" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="FirewallEndpoint",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateFirewallEndpointRequest(proto.Message):
    r"""Message for updating a Endpoint

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the Endpoint resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        firewall_endpoint (google.cloud.network_security_v1alpha1.types.FirewallEndpoint):
            Required. The resource being updated
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

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    firewall_endpoint: "FirewallEndpoint" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="FirewallEndpoint",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteFirewallEndpointRequest(proto.Message):
    r"""Message for deleting a Endpoint

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


class FirewallEndpointAssociation(proto.Message):
    r"""Message describing Association object

    Attributes:
        name (str):
            Immutable. Identifier. name of resource
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time stamp
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Update time stamp
        labels (MutableMapping[str, str]):
            Optional. Labels as key value pairs
        state (google.cloud.network_security_v1alpha1.types.FirewallEndpointAssociation.State):
            Output only. Current state of the
            association.
        network (str):
            Required. The URL of the network that is
            being associated.
        firewall_endpoint (str):
            Required. The URL of the FirewallEndpoint
            that is being associated.
        tls_inspection_policy (str):
            Optional. The URL of the TlsInspectionPolicy
            that is being associated.
        reconciling (bool):
            Output only. Whether reconciling is in
            progress, recommended per
            https://google.aip.dev/128.
        disabled (bool):
            Optional. Whether the association is
            disabled. True indicates that traffic won't be
            intercepted
    """

    class State(proto.Enum):
        r"""Association state.

        Values:
            STATE_UNSPECIFIED (0):
                Not set.
            CREATING (1):
                Being created.
            ACTIVE (2):
                Active and ready for traffic.
            DELETING (3):
                Being deleted.
            INACTIVE (4):
                Down or in an error state.
            ORPHAN (5):
                The project that housed the association has
                been deleted.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        DELETING = 3
        INACTIVE = 4
        ORPHAN = 5

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
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    network: str = proto.Field(
        proto.STRING,
        number=6,
    )
    firewall_endpoint: str = proto.Field(
        proto.STRING,
        number=7,
    )
    tls_inspection_policy: str = proto.Field(
        proto.STRING,
        number=8,
    )
    reconciling: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    disabled: bool = proto.Field(
        proto.BOOL,
        number=10,
    )


class ListFirewallEndpointAssociationsRequest(proto.Message):
    r"""Message for requesting list of Associations

    Attributes:
        parent (str):
            Required. Parent value for
            ListAssociationsRequest
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Optional. Filtering results
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


class ListFirewallEndpointAssociationsResponse(proto.Message):
    r"""Message for response to listing Associations

    Attributes:
        firewall_endpoint_associations (MutableSequence[google.cloud.network_security_v1alpha1.types.FirewallEndpointAssociation]):
            The list of Association
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    firewall_endpoint_associations: MutableSequence["FirewallEndpointAssociation"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="FirewallEndpointAssociation",
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


class GetFirewallEndpointAssociationRequest(proto.Message):
    r"""Message for getting a Association

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateFirewallEndpointAssociationRequest(proto.Message):
    r"""Message for creating a Association

    Attributes:
        parent (str):
            Required. Value for parent.
        firewall_endpoint_association_id (str):
            Optional. Id of the requesting object. If auto-generating Id
            server-side, remove this field and
            firewall_endpoint_association_id from the method_signature
            of Create RPC.
        firewall_endpoint_association (google.cloud.network_security_v1alpha1.types.FirewallEndpointAssociation):
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
    firewall_endpoint_association_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    firewall_endpoint_association: "FirewallEndpointAssociation" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="FirewallEndpointAssociation",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteFirewallEndpointAssociationRequest(proto.Message):
    r"""Message for deleting a Association

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


class UpdateFirewallEndpointAssociationRequest(proto.Message):
    r"""Message for updating an Association

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the Association resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        firewall_endpoint_association (google.cloud.network_security_v1alpha1.types.FirewallEndpointAssociation):
            Required. The resource being updated
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

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    firewall_endpoint_association: "FirewallEndpointAssociation" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="FirewallEndpointAssociation",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
