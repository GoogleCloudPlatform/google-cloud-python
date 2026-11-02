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
    package="google.cloud.networkconnectivity.v1alpha1",
    manifest={
        "State",
        "Hub",
        "Spoke",
        "ListHubsRequest",
        "ListHubsResponse",
        "GetHubRequest",
        "CreateHubRequest",
        "UpdateHubRequest",
        "DeleteHubRequest",
        "ListSpokesRequest",
        "ListSpokesResponse",
        "GetSpokeRequest",
        "CreateSpokeRequest",
        "UpdateSpokeRequest",
        "DeleteSpokeRequest",
        "RouterApplianceInstance",
    },
)


class State(proto.Enum):
    r"""The State enum represents the lifecycle of a Network
    Connectivity Center resource.

    Values:
        STATE_UNSPECIFIED (0):
            No state information available
        CREATING (1):
            The resource's create operation is in
            progress
        ACTIVE (2):
            The resource is active
        DELETING (3):
            The resource's Delete operation is in
            progress
    """

    STATE_UNSPECIFIED = 0
    CREATING = 1
    ACTIVE = 2
    DELETING = 3


class Hub(proto.Message):
    r"""Network Connectivity Center is a hub-and-spoke abstraction
    for network connectivity management in Google Cloud. It reduces
    operational complexity through a simple, centralized
    connectivity management model. Following is the resource message
    of a hub.

    Attributes:
        name (str):
            Immutable. The name of a Hub resource.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Time when the Hub was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Time when the Hub was updated.
        labels (MutableMapping[str, str]):
            User-defined labels.
        description (str):
            Short description of the hub resource.
        spokes (MutableSequence[str]):
            Output only. A list of the URIs of all
            attached spokes
        unique_id (str):
            Output only. Google-generated UUID for this resource. This
            is unique across all Hub resources. If a Hub resource is
            deleted and another with the same name is created, it gets a
            different unique_id.
        state (google.cloud.networkconnectivity_v1alpha1.types.State):
            Output only. The current lifecycle state of
            this Hub.
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
    spokes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    unique_id: str = proto.Field(
        proto.STRING,
        number=8,
    )
    state: "State" = proto.Field(
        proto.ENUM,
        number=9,
        enum="State",
    )


class Spoke(proto.Message):
    r"""A Spoke is an  abstraction of a network attachment being
    attached to a Hub. A Spoke can be underlying a VPN tunnel, a
    VLAN (interconnect) attachment, a Router appliance, etc.

    Attributes:
        name (str):
            Immutable. The name of a Spoke resource.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the Spoke was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the Spoke was updated.
        labels (MutableMapping[str, str]):
            User-defined labels.
        description (str):
            Short description of the spoke resource
        hub (str):
            The resource URL of the hub resource that the
            spoke is attached to
        linked_vpn_tunnels (MutableSequence[str]):
            The URIs of linked VPN tunnel resources
        linked_interconnect_attachments (MutableSequence[str]):
            The URIs of linked interconnect attachment
            resources
        linked_router_appliance_instances (MutableSequence[google.cloud.networkconnectivity_v1alpha1.types.RouterApplianceInstance]):
            The URIs of linked Router appliance resources
        unique_id (str):
            Output only. Google-generated UUID for this resource. This
            is unique across all Spoke resources. If a Spoke resource is
            deleted and another with the same name is created, it gets a
            different unique_id.
        state (google.cloud.networkconnectivity_v1alpha1.types.State):
            Output only. The current lifecycle state of
            this Hub.
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
    hub: str = proto.Field(
        proto.STRING,
        number=6,
    )
    linked_vpn_tunnels: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=12,
    )
    linked_interconnect_attachments: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=13,
    )
    linked_router_appliance_instances: MutableSequence["RouterApplianceInstance"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=14,
            message="RouterApplianceInstance",
        )
    )
    unique_id: str = proto.Field(
        proto.STRING,
        number=11,
    )
    state: "State" = proto.Field(
        proto.ENUM,
        number=15,
        enum="State",
    )


class ListHubsRequest(proto.Message):
    r"""Request for
    [HubService.ListHubs][google.cloud.networkconnectivity.v1alpha1.HubService.ListHubs]
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


class ListHubsResponse(proto.Message):
    r"""Response for
    [HubService.ListHubs][google.cloud.networkconnectivity.v1alpha1.HubService.ListHubs]
    method.

    Attributes:
        hubs (MutableSequence[google.cloud.networkconnectivity_v1alpha1.types.Hub]):
            Hubs to be returned.
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

    hubs: MutableSequence["Hub"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Hub",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetHubRequest(proto.Message):
    r"""Request for
    [HubService.GetHub][google.cloud.networkconnectivity.v1alpha1.HubService.GetHub]
    method.

    Attributes:
        name (str):
            Required. Name of the Hub resource to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateHubRequest(proto.Message):
    r"""Request for
    [HubService.CreateHub][google.cloud.networkconnectivity.v1alpha1.HubService.CreateHub]
    method.

    Attributes:
        parent (str):
            Required. The parent resource's name of the
            Hub.
        hub_id (str):
            Optional. Unique id for the Hub to create.
        hub (google.cloud.networkconnectivity_v1alpha1.types.Hub):
            Required. Initial values for a new Hub.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and t he request times out.
            If you make the request again with the same
            request ID, the server can check if original
            operation with the same request ID was received,
            and if so, will ignore the second request. This
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
    hub_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    hub: "Hub" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Hub",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateHubRequest(proto.Message):
    r"""Request for
    [HubService.UpdateHub][google.cloud.networkconnectivity.v1alpha1.HubService.UpdateHub]
    method.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the Hub resource by the update. The fields
            specified in the update_mask are relative to the resource,
            not the full request. A field will be overwritten if it is
            in the mask. If the user does not provide a mask then all
            fields will be overwritten.
        hub (google.cloud.networkconnectivity_v1alpha1.types.Hub):
            Required. The state that the Hub should be in
            after the update.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and t he request times out.
            If you make the request again with the same
            request ID, the server can check if original
            operation with the same request ID was received,
            and if so, will ignore the second request. This
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
    hub: "Hub" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Hub",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteHubRequest(proto.Message):
    r"""The request for
    [HubService.DeleteHub][google.cloud.networkconnectivity.v1alpha1.HubService.DeleteHub].

    Attributes:
        name (str):
            Required. The name of the Hub to delete.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and t he request times out.
            If you make the request again with the same
            request ID, the server can check if original
            operation with the same request ID was received,
            and if so, will ignore the second request. This
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


class ListSpokesRequest(proto.Message):
    r"""The request for
    [HubService.ListSpokes][google.cloud.networkconnectivity.v1alpha1.HubService.ListSpokes].

    Attributes:
        parent (str):
            Required. The parent's resource name.
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


class ListSpokesResponse(proto.Message):
    r"""The response for
    [HubService.ListSpokes][google.cloud.networkconnectivity.v1alpha1.HubService.ListSpokes].

    Attributes:
        spokes (MutableSequence[google.cloud.networkconnectivity_v1alpha1.types.Spoke]):
            Spokes to be returned.
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

    spokes: MutableSequence["Spoke"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Spoke",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetSpokeRequest(proto.Message):
    r"""The request for
    [HubService.GetSpoke][google.cloud.networkconnectivity.v1alpha1.HubService.GetSpoke].

    Attributes:
        name (str):
            Required. The name of Spoke resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateSpokeRequest(proto.Message):
    r"""The request for
    [HubService.CreateSpoke][google.cloud.networkconnectivity.v1alpha1.HubService.CreateSpoke].

    Attributes:
        parent (str):
            Required. The parent's resource name of the
            Spoke.
        spoke_id (str):
            Optional. Unique id for the Spoke to create.
        spoke (google.cloud.networkconnectivity_v1alpha1.types.Spoke):
            Required. Initial values for a new Hub.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and t he request times out.
            If you make the request again with the same
            request ID, the server can check if original
            operation with the same request ID was received,
            and if so, will ignore the second request. This
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
    spoke_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    spoke: "Spoke" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Spoke",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateSpokeRequest(proto.Message):
    r"""Request for
    [HubService.UpdateSpoke][google.cloud.networkconnectivity.v1alpha1.HubService.UpdateSpoke]
    method.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the Spoke resource by the update. The fields
            specified in the update_mask are relative to the resource,
            not the full request. A field will be overwritten if it is
            in the mask. If the user does not provide a mask then all
            fields will be overwritten.
        spoke (google.cloud.networkconnectivity_v1alpha1.types.Spoke):
            Required. The state that the Spoke should be
            in after the update.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and t he request times out.
            If you make the request again with the same
            request ID, the server can check if original
            operation with the same request ID was received,
            and if so, will ignore the second request. This
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
    spoke: "Spoke" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Spoke",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteSpokeRequest(proto.Message):
    r"""The request for
    [HubService.DeleteSpoke][google.cloud.networkconnectivity.v1alpha1.HubService.DeleteSpoke].

    Attributes:
        name (str):
            Required. The name of the Spoke to delete.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and t he request times out.
            If you make the request again with the same
            request ID, the server can check if original
            operation with the same request ID was received,
            and if so, will ignore the second request. This
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


class RouterApplianceInstance(proto.Message):
    r"""RouterAppliance represents a Router appliance which is
    specified by a VM URI and a NIC address.

    Attributes:
        virtual_machine (str):
            The URI of the virtual machine resource
        ip_address (str):
            The IP address of the network interface to
            use for peering.
        network_interface (str):

    """

    virtual_machine: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ip_address: str = proto.Field(
        proto.STRING,
        number=3,
    )
    network_interface: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
