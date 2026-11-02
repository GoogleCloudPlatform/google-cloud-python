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
        "MirroringEndpointGroup",
        "ListMirroringEndpointGroupsRequest",
        "ListMirroringEndpointGroupsResponse",
        "GetMirroringEndpointGroupRequest",
        "CreateMirroringEndpointGroupRequest",
        "UpdateMirroringEndpointGroupRequest",
        "DeleteMirroringEndpointGroupRequest",
        "MirroringEndpointGroupAssociation",
        "ListMirroringEndpointGroupAssociationsRequest",
        "ListMirroringEndpointGroupAssociationsResponse",
        "GetMirroringEndpointGroupAssociationRequest",
        "CreateMirroringEndpointGroupAssociationRequest",
        "UpdateMirroringEndpointGroupAssociationRequest",
        "DeleteMirroringEndpointGroupAssociationRequest",
        "MirroringDeploymentGroup",
        "ListMirroringDeploymentGroupsRequest",
        "ListMirroringDeploymentGroupsResponse",
        "GetMirroringDeploymentGroupRequest",
        "CreateMirroringDeploymentGroupRequest",
        "UpdateMirroringDeploymentGroupRequest",
        "DeleteMirroringDeploymentGroupRequest",
        "MirroringDeployment",
        "ListMirroringDeploymentsRequest",
        "ListMirroringDeploymentsResponse",
        "GetMirroringDeploymentRequest",
        "CreateMirroringDeploymentRequest",
        "UpdateMirroringDeploymentRequest",
        "DeleteMirroringDeploymentRequest",
        "MirroringLocation",
    },
)


class MirroringEndpointGroup(proto.Message):
    r"""An endpoint group is a consumer frontend for a deployment
    group (backend). In order to configure mirroring for a network,
    consumers must create:

    - An association between their network and the endpoint group.
    - A security profile that points to the endpoint group.
    - A mirroring rule that references the security profile (group).

    Attributes:
        name (str):
            Immutable. Identifier. The resource name of this endpoint
            group, for example:
            ``projects/123456789/locations/global/mirroringEndpointGroups/my-eg``.
            See https://google.aip.dev/122 for more details.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created. See
            https://google.aip.dev/148#timestamps.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was most recently updated. See
            https://google.aip.dev/148#timestamps.
        labels (MutableMapping[str, str]):
            Optional. Labels are key/value pairs that
            help to organize and filter resources.
        mirroring_deployment_group (str):
            Immutable. The deployment group that this DIRECT endpoint
            group is connected to, for example:
            ``projects/123456789/locations/global/mirroringDeploymentGroups/my-dg``.
            See https://google.aip.dev/124.
        connected_deployment_groups (MutableSequence[google.cloud.network_security_v1alpha1.types.MirroringEndpointGroup.ConnectedDeploymentGroup]):
            Output only. List of details about the
            connected deployment groups to this endpoint
            group.
        state (google.cloud.network_security_v1alpha1.types.MirroringEndpointGroup.State):
            Output only. The current state of the
            endpoint group. See https://google.aip.dev/216.
        reconciling (bool):
            Output only. The current state of the
            resource does not match the user's intended
            state, and the system is working to reconcile
            them. This is part of the normal operation (e.g.
            adding a new association to the group). See
            https://google.aip.dev/128.
        type_ (google.cloud.network_security_v1alpha1.types.MirroringEndpointGroup.Type):
            Immutable. The type of the endpoint group.
            If left unspecified, defaults to DIRECT.
        associations (MutableSequence[google.cloud.network_security_v1alpha1.types.MirroringEndpointGroup.AssociationDetails]):
            Output only. List of associations to this
            endpoint group.
        description (str):
            Optional. User-provided description of the
            endpoint group. Used as additional context for
            the endpoint group.
    """

    class State(proto.Enum):
        r"""The current state of the endpoint group.

        Values:
            STATE_UNSPECIFIED (0):
                State not set (this is not a valid state).
            ACTIVE (1):
                The endpoint group is ready and in sync with
                the target deployment group.
            CLOSED (2):
                The deployment group backing this endpoint
                group has been force-deleted. This endpoint
                group cannot be used and mirroring is
                effectively disabled.
            CREATING (3):
                The endpoint group is being created.
            DELETING (4):
                The endpoint group is being deleted.
            OUT_OF_SYNC (5):
                The endpoint group is out of sync with the
                backing deployment group. In most cases, this is
                a result of a transient issue within the system
                (e.g. an inaccessible location) and the system
                is expected to recover automatically. See the
                associations field for details per network and
                location.
            DELETE_FAILED (6):
                An attempt to delete the endpoint group has
                failed. This is a terminal state and the
                endpoint group is not expected to recover. The
                only permitted operation is to retry deleting
                the endpoint group.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        CLOSED = 2
        CREATING = 3
        DELETING = 4
        OUT_OF_SYNC = 5
        DELETE_FAILED = 6

    class Type(proto.Enum):
        r"""The type of the endpoint group.

        Values:
            TYPE_UNSPECIFIED (0):
                Not set.
            DIRECT (1):
                An endpoint group that sends packets to a
                single deployment group.
        """

        TYPE_UNSPECIFIED = 0
        DIRECT = 1

    class ConnectedDeploymentGroup(proto.Message):
        r"""The endpoint group's view of a connected deployment group.

        Attributes:
            name (str):
                Output only. The connected deployment group's resource name,
                for example:
                ``projects/123456789/locations/global/mirroringDeploymentGroups/my-dg``.
                See https://google.aip.dev/124.
            locations (MutableSequence[google.cloud.network_security_v1alpha1.types.MirroringLocation]):
                Output only. The list of locations where the
                deployment group is present.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        locations: MutableSequence["MirroringLocation"] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="MirroringLocation",
        )

    class AssociationDetails(proto.Message):
        r"""The endpoint group's view of a connected association.

        Attributes:
            name (str):
                Output only. The connected association's resource name, for
                example:
                ``projects/123456789/locations/global/mirroringEndpointGroupAssociations/my-ega``.
                See https://google.aip.dev/124.
            network (str):
                Output only. The associated network, for
                example:
                projects/123456789/global/networks/my-network.
                See https://google.aip.dev/124.
            state (google.cloud.network_security_v1alpha1.types.MirroringEndpointGroupAssociation.State):
                Output only. Most recent known state of the
                association.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        network: str = proto.Field(
            proto.STRING,
            number=2,
        )
        state: "MirroringEndpointGroupAssociation.State" = proto.Field(
            proto.ENUM,
            number=3,
            enum="MirroringEndpointGroupAssociation.State",
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
    mirroring_deployment_group: str = proto.Field(
        proto.STRING,
        number=5,
    )
    connected_deployment_groups: MutableSequence[ConnectedDeploymentGroup] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=13,
            message=ConnectedDeploymentGroup,
        )
    )
    state: State = proto.Field(
        proto.ENUM,
        number=7,
        enum=State,
    )
    reconciling: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=11,
        enum=Type,
    )
    associations: MutableSequence[AssociationDetails] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=AssociationDetails,
    )
    description: str = proto.Field(
        proto.STRING,
        number=10,
    )


class ListMirroringEndpointGroupsRequest(proto.Message):
    r"""Request message for ListMirroringEndpointGroups.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of endpoint
            groups. Example: ``projects/123456789/locations/global``.
            See https://google.aip.dev/132 for more details.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default. See https://google.aip.dev/158 for more
            details.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListMirroringEndpointGroups`` call. Provide this to
            retrieve the subsequent page. When paginating, all other
            parameters provided to ``ListMirroringEndpointGroups`` must
            match the call that provided the page token. See
            https://google.aip.dev/158 for more details.
        filter (str):
            Optional. Filter expression.
            See https://google.aip.dev/160#filtering for
            more details.
        order_by (str):
            Optional. Sort expression.
            See https://google.aip.dev/132#ordering for more
            details.
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


class ListMirroringEndpointGroupsResponse(proto.Message):
    r"""Response message for ListMirroringEndpointGroups.

    Attributes:
        mirroring_endpoint_groups (MutableSequence[google.cloud.network_security_v1alpha1.types.MirroringEndpointGroup]):
            The endpoint groups from the specified
            parent.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages. See https://google.aip.dev/158 for more details.
    """

    @property
    def raw_page(self):
        return self

    mirroring_endpoint_groups: MutableSequence["MirroringEndpointGroup"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="MirroringEndpointGroup",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetMirroringEndpointGroupRequest(proto.Message):
    r"""Request message for GetMirroringEndpointGroup.

    Attributes:
        name (str):
            Required. The name of the endpoint group to retrieve.
            Format:
            projects/{project}/locations/{location}/mirroringEndpointGroups/{mirroring_endpoint_group}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateMirroringEndpointGroupRequest(proto.Message):
    r"""Request message for CreateMirroringEndpointGroup.

    Attributes:
        parent (str):
            Required. The parent resource where this
            endpoint group will be created. Format:
            projects/{project}/locations/{location}
        mirroring_endpoint_group_id (str):
            Required. The ID to use for the endpoint
            group, which will become the final component of
            the endpoint group's resource name.
        mirroring_endpoint_group (google.cloud.network_security_v1alpha1.types.MirroringEndpointGroup):
            Required. The endpoint group to create.
        request_id (str):
            Optional. A unique identifier for this request. Must be a
            UUID4. This request is only idempotent if a ``request_id``
            is provided. See https://google.aip.dev/155 for more
            details.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    mirroring_endpoint_group_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    mirroring_endpoint_group: "MirroringEndpointGroup" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="MirroringEndpointGroup",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateMirroringEndpointGroupRequest(proto.Message):
    r"""Request message for UpdateMirroringEndpointGroup.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update. Fields are specified
            relative to the endpoint group (e.g. ``description``; *not*
            ``mirroring_endpoint_group.description``). See
            https://google.aip.dev/161 for more details.
        mirroring_endpoint_group (google.cloud.network_security_v1alpha1.types.MirroringEndpointGroup):
            Required. The endpoint group to update.
        request_id (str):
            Optional. A unique identifier for this request. Must be a
            UUID4. This request is only idempotent if a ``request_id``
            is provided. See https://google.aip.dev/155 for more
            details.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    mirroring_endpoint_group: "MirroringEndpointGroup" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="MirroringEndpointGroup",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteMirroringEndpointGroupRequest(proto.Message):
    r"""Request message for DeleteMirroringEndpointGroup.

    Attributes:
        name (str):
            Required. The endpoint group to delete.
        request_id (str):
            Optional. A unique identifier for this request. Must be a
            UUID4. This request is only idempotent if a ``request_id``
            is provided. See https://google.aip.dev/155 for more
            details.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class MirroringEndpointGroupAssociation(proto.Message):
    r"""An endpoint group association represents a link between a
    network and an endpoint group in the organization.

    Creating an association creates the networking infrastructure
    linking the network to the endpoint group, but does not enable
    mirroring by itself. To enable mirroring, the user must also
    create a network firewall policy containing mirroring rules and
    associate it with the network.

    Attributes:
        name (str):
            Immutable. Identifier. The resource name of this endpoint
            group association, for example:
            ``projects/123456789/locations/global/mirroringEndpointGroupAssociations/my-eg-association``.
            See https://google.aip.dev/122 for more details.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created. See
            https://google.aip.dev/148#timestamps.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was most recently updated. See
            https://google.aip.dev/148#timestamps.
        labels (MutableMapping[str, str]):
            Optional. Labels are key/value pairs that
            help to organize and filter resources.
        mirroring_endpoint_group (str):
            Immutable. The endpoint group that this association is
            connected to, for example:
            ``projects/123456789/locations/global/mirroringEndpointGroups/my-eg``.
            See https://google.aip.dev/124.
        network (str):
            Immutable. The VPC network that is associated. for example:
            ``projects/123456789/global/networks/my-network``. See
            https://google.aip.dev/124.
        locations_details (MutableSequence[google.cloud.network_security_v1alpha1.types.MirroringEndpointGroupAssociation.LocationDetails]):
            Output only. The list of locations where the
            association is present. This information is
            retrieved from the linked endpoint group, and
            not configured as part of the association
            itself.
        state (google.cloud.network_security_v1alpha1.types.MirroringEndpointGroupAssociation.State):
            Output only. Current state of the endpoint
            group association.
        reconciling (bool):
            Output only. The current state of the
            resource does not match the user's intended
            state, and the system is working to reconcile
            them. This part of the normal operation (e.g.
            adding a new location to the target deployment
            group). See https://google.aip.dev/128.
        locations (MutableSequence[google.cloud.network_security_v1alpha1.types.MirroringLocation]):
            Output only. The list of locations where the
            association is configured. This information is
            retrieved from the linked endpoint group.
    """

    class State(proto.Enum):
        r"""The state of the association.

        Values:
            STATE_UNSPECIFIED (0):
                Not set.
            ACTIVE (1):
                The association is ready and in sync with the
                linked endpoint group.
            CREATING (3):
                The association is being created.
            DELETING (4):
                The association is being deleted.
            CLOSED (5):
                The association is disabled due to a breaking
                change in another resource.
            OUT_OF_SYNC (6):
                The association is out of sync with the linked endpoint
                group. In most cases, this is a result of a transient issue
                within the system (e.g. an inaccessible location) and the
                system is expected to recover automatically. Check the
                ``locations_details`` field for more details.
            DELETE_FAILED (7):
                An attempt to delete the association has
                failed. This is a terminal state and the
                association is not expected to be usable as some
                of its resources have been deleted.
                The only permitted operation is to retry
                deleting the association.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        CREATING = 3
        DELETING = 4
        CLOSED = 5
        OUT_OF_SYNC = 6
        DELETE_FAILED = 7

    class LocationDetails(proto.Message):
        r"""Contains details about the state of an association in a
        specific cloud location.

        Attributes:
            location (str):
                Output only. The cloud location, e.g.
                "us-central1-a" or "asia-south1".
            state (google.cloud.network_security_v1alpha1.types.MirroringEndpointGroupAssociation.LocationDetails.State):
                Output only. The current state of the
                association in this location.
        """

        class State(proto.Enum):
            r"""The state of association.

            Values:
                STATE_UNSPECIFIED (0):
                    Not set.
                ACTIVE (1):
                    The association is ready and in sync with the
                    linked endpoint group.
                OUT_OF_SYNC (2):
                    The association is out of sync with the
                    linked endpoint group. In most cases, this is a
                    result of a transient issue within the system
                    (e.g. an inaccessible location) and the system
                    is expected to recover automatically.
            """

            STATE_UNSPECIFIED = 0
            ACTIVE = 1
            OUT_OF_SYNC = 2

        location: str = proto.Field(
            proto.STRING,
            number=1,
        )
        state: "MirroringEndpointGroupAssociation.LocationDetails.State" = proto.Field(
            proto.ENUM,
            number=2,
            enum="MirroringEndpointGroupAssociation.LocationDetails.State",
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
    mirroring_endpoint_group: str = proto.Field(
        proto.STRING,
        number=5,
    )
    network: str = proto.Field(
        proto.STRING,
        number=6,
    )
    locations_details: MutableSequence[LocationDetails] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=LocationDetails,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=8,
        enum=State,
    )
    reconciling: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    locations: MutableSequence["MirroringLocation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message="MirroringLocation",
    )


class ListMirroringEndpointGroupAssociationsRequest(proto.Message):
    r"""Request message for ListMirroringEndpointGroupAssociations.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            associations. Example:
            ``projects/123456789/locations/global``. See
            https://google.aip.dev/132 for more details.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default. See https://google.aip.dev/158 for more
            details.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListMirroringEndpointGroups`` call. Provide this to
            retrieve the subsequent page. When paginating, all other
            parameters provided to ``ListMirroringEndpointGroups`` must
            match the call that provided the page token. See
            https://google.aip.dev/158 for more details.
        filter (str):
            Optional. Filter expression.
            See https://google.aip.dev/160#filtering for
            more details.
        order_by (str):
            Optional. Sort expression.
            See https://google.aip.dev/132#ordering for more
            details.
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


class ListMirroringEndpointGroupAssociationsResponse(proto.Message):
    r"""Response message for ListMirroringEndpointGroupAssociations.

    Attributes:
        mirroring_endpoint_group_associations (MutableSequence[google.cloud.network_security_v1alpha1.types.MirroringEndpointGroupAssociation]):
            The associations from the specified parent.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages. See https://google.aip.dev/158 for more details.
    """

    @property
    def raw_page(self):
        return self

    mirroring_endpoint_group_associations: MutableSequence[
        "MirroringEndpointGroupAssociation"
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="MirroringEndpointGroupAssociation",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetMirroringEndpointGroupAssociationRequest(proto.Message):
    r"""Request message for GetMirroringEndpointGroupAssociation.

    Attributes:
        name (str):
            Required. The name of the association to retrieve. Format:
            projects/{project}/locations/{location}/mirroringEndpointGroupAssociations/{mirroring_endpoint_group_association}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateMirroringEndpointGroupAssociationRequest(proto.Message):
    r"""Request message for CreateMirroringEndpointGroupAssociation.

    Attributes:
        parent (str):
            Required. The parent resource where this
            association will be created. Format:
            projects/{project}/locations/{location}
        mirroring_endpoint_group_association_id (str):
            Optional. The ID to use for the new
            association, which will become the final
            component of the endpoint group's resource name.
            If not provided, the server will generate a
            unique ID.
        mirroring_endpoint_group_association (google.cloud.network_security_v1alpha1.types.MirroringEndpointGroupAssociation):
            Required. The association to create.
        request_id (str):
            Optional. A unique identifier for this request. Must be a
            UUID4. This request is only idempotent if a ``request_id``
            is provided. See https://google.aip.dev/155 for more
            details.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    mirroring_endpoint_group_association_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    mirroring_endpoint_group_association: "MirroringEndpointGroupAssociation" = (
        proto.Field(
            proto.MESSAGE,
            number=3,
            message="MirroringEndpointGroupAssociation",
        )
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateMirroringEndpointGroupAssociationRequest(proto.Message):
    r"""Request message for UpdateMirroringEndpointGroupAssociation.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update. Fields are specified
            relative to the association (e.g. ``description``; *not*
            ``mirroring_endpoint_group_association.description``). See
            https://google.aip.dev/161 for more details.
        mirroring_endpoint_group_association (google.cloud.network_security_v1alpha1.types.MirroringEndpointGroupAssociation):
            Required. The association to update.
        request_id (str):
            Optional. A unique identifier for this request. Must be a
            UUID4. This request is only idempotent if a ``request_id``
            is provided. See https://google.aip.dev/155 for more
            details.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    mirroring_endpoint_group_association: "MirroringEndpointGroupAssociation" = (
        proto.Field(
            proto.MESSAGE,
            number=2,
            message="MirroringEndpointGroupAssociation",
        )
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteMirroringEndpointGroupAssociationRequest(proto.Message):
    r"""Request message for DeleteMirroringEndpointGroupAssociation.

    Attributes:
        name (str):
            Required. The association to delete.
        request_id (str):
            Optional. A unique identifier for this request. Must be a
            UUID4. This request is only idempotent if a ``request_id``
            is provided. See https://google.aip.dev/155 for more
            details.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class MirroringDeploymentGroup(proto.Message):
    r"""A deployment group aggregates many zonal mirroring backends
    (deployments) into a single global mirroring service. Consumers
    can connect this service using an endpoint group.

    Attributes:
        name (str):
            Immutable. Identifier. The resource name of this deployment
            group, for example:
            ``projects/123456789/locations/global/mirroringDeploymentGroups/my-dg``.
            See https://google.aip.dev/122 for more details.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created. See
            https://google.aip.dev/148#timestamps.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was most recently updated. See
            https://google.aip.dev/148#timestamps.
        labels (MutableMapping[str, str]):
            Optional. Labels are key/value pairs that
            help to organize and filter resources.
        network (str):
            Required. Immutable. The network that will be used for all
            child deployments, for example:
            ``projects/{project}/global/networks/{network}``. See
            https://google.aip.dev/124.
        connected_endpoint_groups (MutableSequence[google.cloud.network_security_v1alpha1.types.MirroringDeploymentGroup.ConnectedEndpointGroup]):
            Output only. The list of endpoint groups that
            are connected to this resource.
        nested_deployments (MutableSequence[google.cloud.network_security_v1alpha1.types.MirroringDeploymentGroup.Deployment]):
            Output only. The list of Mirroring
            Deployments that belong to this group.
        state (google.cloud.network_security_v1alpha1.types.MirroringDeploymentGroup.State):
            Output only. The current state of the
            deployment group. See
            https://google.aip.dev/216.
        reconciling (bool):
            Output only. The current state of the
            resource does not match the user's intended
            state, and the system is working to reconcile
            them. This is part of the normal operation (e.g.
            adding a new deployment to the group) See
            https://google.aip.dev/128.
        description (str):
            Optional. User-provided description of the
            deployment group. Used as additional context for
            the deployment group.
        locations (MutableSequence[google.cloud.network_security_v1alpha1.types.MirroringLocation]):
            Output only. The list of locations where the
            deployment group is present.
    """

    class State(proto.Enum):
        r"""The current state of the deployment group.

        Values:
            STATE_UNSPECIFIED (0):
                State not set (this is not a valid state).
            ACTIVE (1):
                The deployment group is ready.
            CREATING (2):
                The deployment group is being created.
            DELETING (3):
                The deployment group is being deleted.
            CLOSED (4):
                The deployment group is being wiped out
                (project deleted).
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        CREATING = 2
        DELETING = 3
        CLOSED = 4

    class ConnectedEndpointGroup(proto.Message):
        r"""An endpoint group connected to this deployment group.

        Attributes:
            name (str):
                Output only. The connected endpoint group's resource name,
                for example:
                ``projects/123456789/locations/global/mirroringEndpointGroups/my-eg``.
                See https://google.aip.dev/124.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class Deployment(proto.Message):
        r"""A deployment belonging to this deployment group.

        Attributes:
            name (str):
                Output only. The name of the Mirroring Deployment, in the
                format:
                ``projects/{project}/locations/{location}/mirroringDeployments/{mirroring_deployment}``.
            state (google.cloud.network_security_v1alpha1.types.MirroringDeployment.State):
                Output only. Most recent known state of the
                deployment.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        state: "MirroringDeployment.State" = proto.Field(
            proto.ENUM,
            number=2,
            enum="MirroringDeployment.State",
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
    network: str = proto.Field(
        proto.STRING,
        number=5,
    )
    connected_endpoint_groups: MutableSequence[ConnectedEndpointGroup] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=6,
            message=ConnectedEndpointGroup,
        )
    )
    nested_deployments: MutableSequence[Deployment] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message=Deployment,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=7,
        enum=State,
    )
    reconciling: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    description: str = proto.Field(
        proto.STRING,
        number=9,
    )
    locations: MutableSequence["MirroringLocation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message="MirroringLocation",
    )


class ListMirroringDeploymentGroupsRequest(proto.Message):
    r"""Request message for ListMirroringDeploymentGroups.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            deployment groups. Example:
            ``projects/123456789/locations/global``. See
            https://google.aip.dev/132 for more details.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default. See https://google.aip.dev/158 for more
            details.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListMirroringDeploymentGroups`` call. Provide this to
            retrieve the subsequent page. When paginating, all other
            parameters provided to ``ListMirroringDeploymentGroups``
            must match the call that provided the page token. See
            https://google.aip.dev/158 for more details.
        filter (str):
            Optional. Filter expression.
            See https://google.aip.dev/160#filtering for
            more details.
        order_by (str):
            Optional. Sort expression.
            See https://google.aip.dev/132#ordering for more
            details.
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


class ListMirroringDeploymentGroupsResponse(proto.Message):
    r"""Response message for ListMirroringDeploymentGroups.

    Attributes:
        mirroring_deployment_groups (MutableSequence[google.cloud.network_security_v1alpha1.types.MirroringDeploymentGroup]):
            The deployment groups from the specified
            parent.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages. See https://google.aip.dev/158 for more details.
    """

    @property
    def raw_page(self):
        return self

    mirroring_deployment_groups: MutableSequence["MirroringDeploymentGroup"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="MirroringDeploymentGroup",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetMirroringDeploymentGroupRequest(proto.Message):
    r"""Request message for GetMirroringDeploymentGroup.

    Attributes:
        name (str):
            Required. The name of the deployment group to retrieve.
            Format:
            projects/{project}/locations/{location}/mirroringDeploymentGroups/{mirroring_deployment_group}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateMirroringDeploymentGroupRequest(proto.Message):
    r"""Request message for CreateMirroringDeploymentGroup.

    Attributes:
        parent (str):
            Required. The parent resource where this
            deployment group will be created. Format:
            projects/{project}/locations/{location}
        mirroring_deployment_group_id (str):
            Required. The ID to use for the new
            deployment group, which will become the final
            component of the deployment group's resource
            name.
        mirroring_deployment_group (google.cloud.network_security_v1alpha1.types.MirroringDeploymentGroup):
            Required. The deployment group to create.
        request_id (str):
            Optional. A unique identifier for this request. Must be a
            UUID4. This request is only idempotent if a ``request_id``
            is provided. See https://google.aip.dev/155 for more
            details.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    mirroring_deployment_group_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    mirroring_deployment_group: "MirroringDeploymentGroup" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="MirroringDeploymentGroup",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateMirroringDeploymentGroupRequest(proto.Message):
    r"""Request message for UpdateMirroringDeploymentGroup.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update. Fields are specified
            relative to the deployment group (e.g. ``description``;
            *not* ``mirroring_deployment_group.description``). See
            https://google.aip.dev/161 for more details.
        mirroring_deployment_group (google.cloud.network_security_v1alpha1.types.MirroringDeploymentGroup):
            Required. The deployment group to update.
        request_id (str):
            Optional. A unique identifier for this request. Must be a
            UUID4. This request is only idempotent if a ``request_id``
            is provided. See https://google.aip.dev/155 for more
            details.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    mirroring_deployment_group: "MirroringDeploymentGroup" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="MirroringDeploymentGroup",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteMirroringDeploymentGroupRequest(proto.Message):
    r"""Request message for DeleteMirroringDeploymentGroup.

    Attributes:
        name (str):
            Required. The deployment group to delete.
        request_id (str):
            Optional. A unique identifier for this request. Must be a
            UUID4. This request is only idempotent if a ``request_id``
            is provided. See https://google.aip.dev/155 for more
            details.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class MirroringDeployment(proto.Message):
    r"""A deployment represents a zonal mirroring backend ready to
    accept GENEVE-encapsulated replica traffic, e.g. a zonal
    instance group fronted by an internal passthrough load balancer.
    Deployments are always part of a global deployment group which
    represents a global mirroring service.

    Attributes:
        name (str):
            Immutable. Identifier. The resource name of this deployment,
            for example:
            ``projects/123456789/locations/us-central1-a/mirroringDeployments/my-dep``.
            See https://google.aip.dev/122 for more details.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created. See
            https://google.aip.dev/148#timestamps.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was most recently updated. See
            https://google.aip.dev/148#timestamps.
        labels (MutableMapping[str, str]):
            Optional. Labels are key/value pairs that
            help to organize and filter resources.
        forwarding_rule (str):
            Required. Immutable. The regional forwarding rule that
            fronts the mirroring collectors, for example:
            ``projects/123456789/regions/us-central1/forwardingRules/my-rule``.
            See https://google.aip.dev/124.
        mirroring_deployment_group (str):
            Required. Immutable. The deployment group that this
            deployment is a part of, for example:
            ``projects/123456789/locations/global/mirroringDeploymentGroups/my-dg``.
            See https://google.aip.dev/124.
        state (google.cloud.network_security_v1alpha1.types.MirroringDeployment.State):
            Output only. The current state of the
            deployment. See https://google.aip.dev/216.
        reconciling (bool):
            Output only. The current state of the
            resource does not match the user's intended
            state, and the system is working to reconcile
            them. This part of the normal operation (e.g.
            linking a new association to the parent group).
            See https://google.aip.dev/128.
        description (str):
            Optional. User-provided description of the
            deployment. Used as additional context for the
            deployment.
    """

    class State(proto.Enum):
        r"""The current state of the deployment.

        Values:
            STATE_UNSPECIFIED (0):
                State not set (this is not a valid state).
            ACTIVE (1):
                The deployment is ready and in sync with the
                parent group.
            CREATING (2):
                The deployment is being created.
            DELETING (3):
                The deployment is being deleted.
            OUT_OF_SYNC (4):
                The deployment is out of sync with the parent
                group. In most cases, this is a result of a
                transient issue within the system (e.g. a
                delayed data-path config) and the system is
                expected to recover automatically. See the
                parent deployment group's state for more
                details.
            DELETE_FAILED (5):
                An attempt to delete the deployment has
                failed. This is a terminal state and the
                deployment is not expected to recover. The only
                permitted operation is to retry deleting the
                deployment.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        CREATING = 2
        DELETING = 3
        OUT_OF_SYNC = 4
        DELETE_FAILED = 5

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
    forwarding_rule: str = proto.Field(
        proto.STRING,
        number=5,
    )
    mirroring_deployment_group: str = proto.Field(
        proto.STRING,
        number=6,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=7,
        enum=State,
    )
    reconciling: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    description: str = proto.Field(
        proto.STRING,
        number=9,
    )


class ListMirroringDeploymentsRequest(proto.Message):
    r"""Request message for ListMirroringDeployments.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            deployments. Example:
            ``projects/123456789/locations/us-central1-a``. See
            https://google.aip.dev/132 for more details.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default. See https://google.aip.dev/158 for more
            details.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListMirroringDeployments`` call. Provide this to retrieve
            the subsequent page. When paginating, all other parameters
            provided to ``ListMirroringDeployments`` must match the call
            that provided the page token. See https://google.aip.dev/158
            for more details.
        filter (str):
            Optional. Filter expression.
            See https://google.aip.dev/160#filtering for
            more details.
        order_by (str):
            Optional. Sort expression.
            See https://google.aip.dev/132#ordering for more
            details.
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


class ListMirroringDeploymentsResponse(proto.Message):
    r"""Response message for ListMirroringDeployments.

    Attributes:
        mirroring_deployments (MutableSequence[google.cloud.network_security_v1alpha1.types.MirroringDeployment]):
            The deployments from the specified parent.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages. See https://google.aip.dev/158 for more details.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    mirroring_deployments: MutableSequence["MirroringDeployment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="MirroringDeployment",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetMirroringDeploymentRequest(proto.Message):
    r"""Request message for GetMirroringDeployment.

    Attributes:
        name (str):
            Required. The name of the deployment to retrieve. Format:
            projects/{project}/locations/{location}/mirroringDeployments/{mirroring_deployment}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateMirroringDeploymentRequest(proto.Message):
    r"""Request message for CreateMirroringDeployment.

    Attributes:
        parent (str):
            Required. The parent resource where this
            deployment will be created. Format:
            projects/{project}/locations/{location}
        mirroring_deployment_id (str):
            Required. The ID to use for the new
            deployment, which will become the final
            component of the deployment's resource name.
        mirroring_deployment (google.cloud.network_security_v1alpha1.types.MirroringDeployment):
            Required. The deployment to create.
        request_id (str):
            Optional. A unique identifier for this request. Must be a
            UUID4. This request is only idempotent if a ``request_id``
            is provided. See https://google.aip.dev/155 for more
            details.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    mirroring_deployment_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    mirroring_deployment: "MirroringDeployment" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="MirroringDeployment",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateMirroringDeploymentRequest(proto.Message):
    r"""Request message for UpdateMirroringDeployment.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update. Fields are specified
            relative to the deployment (e.g. ``description``; *not*
            ``mirroring_deployment.description``). See
            https://google.aip.dev/161 for more details.
        mirroring_deployment (google.cloud.network_security_v1alpha1.types.MirroringDeployment):
            Required. The deployment to update.
        request_id (str):
            Optional. A unique identifier for this request. Must be a
            UUID4. This request is only idempotent if a ``request_id``
            is provided. See https://google.aip.dev/155 for more
            details.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    mirroring_deployment: "MirroringDeployment" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="MirroringDeployment",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteMirroringDeploymentRequest(proto.Message):
    r"""Request message for DeleteMirroringDeployment.

    Attributes:
        name (str):
            Required. Name of the resource
        request_id (str):
            Optional. A unique identifier for this request. Must be a
            UUID4. This request is only idempotent if a ``request_id``
            is provided. See https://google.aip.dev/155 for more
            details.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class MirroringLocation(proto.Message):
    r"""Details about mirroring in a specific cloud location.

    Attributes:
        location (str):
            Output only. The cloud location, e.g.
            "us-central1-a" or "asia-south1".
        state (google.cloud.network_security_v1alpha1.types.MirroringLocation.State):
            Output only. The current state of the
            association in this location.
    """

    class State(proto.Enum):
        r"""The current state of a resource in the location.

        Values:
            STATE_UNSPECIFIED (0):
                State not set (this is not a valid state).
            ACTIVE (1):
                The resource is ready and in sync in the
                location.
            OUT_OF_SYNC (2):
                The resource is out of sync in the location.
                In most cases, this is a result of a transient
                issue within the system (e.g. an inaccessible
                location) and the system is expected to recover
                automatically.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        OUT_OF_SYNC = 2

    location: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
