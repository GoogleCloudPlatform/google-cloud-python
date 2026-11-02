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
        "InterceptEndpointGroup",
        "ListInterceptEndpointGroupsRequest",
        "ListInterceptEndpointGroupsResponse",
        "GetInterceptEndpointGroupRequest",
        "CreateInterceptEndpointGroupRequest",
        "UpdateInterceptEndpointGroupRequest",
        "DeleteInterceptEndpointGroupRequest",
        "InterceptEndpointGroupAssociation",
        "ListInterceptEndpointGroupAssociationsRequest",
        "ListInterceptEndpointGroupAssociationsResponse",
        "GetInterceptEndpointGroupAssociationRequest",
        "CreateInterceptEndpointGroupAssociationRequest",
        "UpdateInterceptEndpointGroupAssociationRequest",
        "DeleteInterceptEndpointGroupAssociationRequest",
        "InterceptDeploymentGroup",
        "ListInterceptDeploymentGroupsRequest",
        "ListInterceptDeploymentGroupsResponse",
        "GetInterceptDeploymentGroupRequest",
        "CreateInterceptDeploymentGroupRequest",
        "UpdateInterceptDeploymentGroupRequest",
        "DeleteInterceptDeploymentGroupRequest",
        "InterceptDeployment",
        "ListInterceptDeploymentsRequest",
        "ListInterceptDeploymentsResponse",
        "GetInterceptDeploymentRequest",
        "CreateInterceptDeploymentRequest",
        "UpdateInterceptDeploymentRequest",
        "DeleteInterceptDeploymentRequest",
        "InterceptLocation",
    },
)


class InterceptEndpointGroup(proto.Message):
    r"""An endpoint group is a consumer frontend for a deployment
    group (backend). In order to configure intercept for a network,
    consumers must create:

    - An association between their network and the endpoint group.
    - A security profile that points to the endpoint group.
    - A firewall rule that references the security profile (group).

    Attributes:
        name (str):
            Immutable. Identifier. The resource name of this endpoint
            group, for example:
            ``projects/123456789/locations/global/interceptEndpointGroups/my-eg``.
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
        intercept_deployment_group (str):
            Required. Immutable. The deployment group that this endpoint
            group is connected to, for example:
            ``projects/123456789/locations/global/interceptDeploymentGroups/my-dg``.
            See https://google.aip.dev/124.
        connected_deployment_group (google.cloud.network_security_v1alpha1.types.InterceptEndpointGroup.ConnectedDeploymentGroup):
            Output only. Details about the connected
            deployment group to this endpoint group.
        state (google.cloud.network_security_v1alpha1.types.InterceptEndpointGroup.State):
            Output only. The current state of the
            endpoint group. See https://google.aip.dev/216.
        reconciling (bool):
            Output only. The current state of the
            resource does not match the user's intended
            state, and the system is working to reconcile
            them. This is part of the normal operation (e.g.
            adding a new association to the group). See
            https://google.aip.dev/128.
        associations (MutableSequence[google.cloud.network_security_v1alpha1.types.InterceptEndpointGroup.AssociationDetails]):
            Output only. List of associations to this
            endpoint group.
        description (str):
            Optional. User-provided description of the
            endpoint group. Used as additional context for
            the endpoint group.
    """

    class State(proto.Enum):
        r"""Endpoint group state.

        Values:
            STATE_UNSPECIFIED (0):
                State not set (this is not a valid state).
            ACTIVE (1):
                The endpoint group is ready and in sync with
                the target deployment group.
            CLOSED (2):
                The deployment group backing this endpoint
                group has been force-deleted. This endpoint
                group cannot be used and interception is
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

    class ConnectedDeploymentGroup(proto.Message):
        r"""The endpoint group's view of a connected deployment group.

        Attributes:
            name (str):
                Output only. The connected deployment group's resource name,
                for example:
                ``projects/123456789/locations/global/interceptDeploymentGroups/my-dg``.
                See https://google.aip.dev/124.
            locations (MutableSequence[google.cloud.network_security_v1alpha1.types.InterceptLocation]):
                Output only. The list of locations where the
                deployment group is present.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        locations: MutableSequence["InterceptLocation"] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="InterceptLocation",
        )

    class AssociationDetails(proto.Message):
        r"""The endpoint group's view of a connected association.

        Attributes:
            name (str):
                Output only. The connected association's resource name, for
                example:
                ``projects/123456789/locations/global/interceptEndpointGroupAssociations/my-ega``.
                See https://google.aip.dev/124.
            network (str):
                Output only. The associated network, for
                example:
                projects/123456789/global/networks/my-network.
                See https://google.aip.dev/124.
            state (google.cloud.network_security_v1alpha1.types.InterceptEndpointGroupAssociation.State):
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
        state: "InterceptEndpointGroupAssociation.State" = proto.Field(
            proto.ENUM,
            number=3,
            enum="InterceptEndpointGroupAssociation.State",
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
    intercept_deployment_group: str = proto.Field(
        proto.STRING,
        number=5,
    )
    connected_deployment_group: ConnectedDeploymentGroup = proto.Field(
        proto.MESSAGE,
        number=11,
        message=ConnectedDeploymentGroup,
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
    associations: MutableSequence[AssociationDetails] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=AssociationDetails,
    )
    description: str = proto.Field(
        proto.STRING,
        number=10,
    )


class ListInterceptEndpointGroupsRequest(proto.Message):
    r"""Request message for ListInterceptEndpointGroups.

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
            ``ListInterceptEndpointGroups`` call. Provide this to
            retrieve the subsequent page. When paginating, all other
            parameters provided to ``ListInterceptEndpointGroups`` must
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


class ListInterceptEndpointGroupsResponse(proto.Message):
    r"""Response message for ListInterceptEndpointGroups.

    Attributes:
        intercept_endpoint_groups (MutableSequence[google.cloud.network_security_v1alpha1.types.InterceptEndpointGroup]):
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

    intercept_endpoint_groups: MutableSequence["InterceptEndpointGroup"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="InterceptEndpointGroup",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetInterceptEndpointGroupRequest(proto.Message):
    r"""Request message for GetInterceptEndpointGroup.

    Attributes:
        name (str):
            Required. The name of the endpoint group to retrieve.
            Format:
            projects/{project}/locations/{location}/interceptEndpointGroups/{intercept_endpoint_group}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateInterceptEndpointGroupRequest(proto.Message):
    r"""Request message for CreateInterceptEndpointGroup.

    Attributes:
        parent (str):
            Required. The parent resource where this
            endpoint group will be created. Format:
            projects/{project}/locations/{location}
        intercept_endpoint_group_id (str):
            Required. The ID to use for the endpoint
            group, which will become the final component of
            the endpoint group's resource name.
        intercept_endpoint_group (google.cloud.network_security_v1alpha1.types.InterceptEndpointGroup):
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
    intercept_endpoint_group_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    intercept_endpoint_group: "InterceptEndpointGroup" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="InterceptEndpointGroup",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateInterceptEndpointGroupRequest(proto.Message):
    r"""Request message for UpdateInterceptEndpointGroup.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update. Fields are specified
            relative to the endpoint group (e.g. ``description``; *not*
            ``intercept_endpoint_group.description``). See
            https://google.aip.dev/161 for more details.
        intercept_endpoint_group (google.cloud.network_security_v1alpha1.types.InterceptEndpointGroup):
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
    intercept_endpoint_group: "InterceptEndpointGroup" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="InterceptEndpointGroup",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteInterceptEndpointGroupRequest(proto.Message):
    r"""Request message for DeleteInterceptEndpointGroup.

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


class InterceptEndpointGroupAssociation(proto.Message):
    r"""An endpoint group association represents a link between a
    network and an endpoint group in the organization.

    Creating an association creates the networking infrastructure
    linking the network to the endpoint group, but does not enable
    intercept by itself. To enable intercept, the user must also
    create a network firewall policy containing intercept rules and
    associate it with the network.

    Attributes:
        name (str):
            Immutable. Identifier. The resource name of this endpoint
            group association, for example:
            ``projects/123456789/locations/global/interceptEndpointGroupAssociations/my-eg-association``.
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
        intercept_endpoint_group (str):
            Required. Immutable. The endpoint group that this
            association is connected to, for example:
            ``projects/123456789/locations/global/interceptEndpointGroups/my-eg``.
            See https://google.aip.dev/124.
        network (str):
            Required. Immutable. The VPC network that is associated. for
            example: ``projects/123456789/global/networks/my-network``.
            See https://google.aip.dev/124.
        locations_details (MutableSequence[google.cloud.network_security_v1alpha1.types.InterceptEndpointGroupAssociation.LocationDetails]):
            Output only. The list of locations where the
            association is present. This information is
            retrieved from the linked endpoint group, and
            not configured as part of the association
            itself.
        state (google.cloud.network_security_v1alpha1.types.InterceptEndpointGroupAssociation.State):
            Output only. Current state of the endpoint
            group association.
        reconciling (bool):
            Output only. The current state of the
            resource does not match the user's intended
            state, and the system is working to reconcile
            them. This part of the normal operation (e.g.
            adding a new location to the target deployment
            group). See https://google.aip.dev/128.
        locations (MutableSequence[google.cloud.network_security_v1alpha1.types.InterceptLocation]):
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
            CREATING (2):
                The association is being created.
            DELETING (3):
                The association is being deleted.
            CLOSED (4):
                The association is disabled due to a breaking
                change in another resource.
            OUT_OF_SYNC (5):
                The association is out of sync with the linked endpoint
                group. In most cases, this is a result of a transient issue
                within the system (e.g. an inaccessible location) and the
                system is expected to recover automatically. Check the
                ``locations_details`` field for more details.
            DELETE_FAILED (6):
                An attempt to delete the association has
                failed. This is a terminal state and the
                association is not expected to be usable as some
                of its resources have been deleted.
                The only permitted operation is to retry
                deleting the association.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        CREATING = 2
        DELETING = 3
        CLOSED = 4
        OUT_OF_SYNC = 5
        DELETE_FAILED = 6

    class LocationDetails(proto.Message):
        r"""Contains details about the state of an association in a
        specific cloud location.

        Attributes:
            location (str):
                Output only. The cloud location, e.g.
                "us-central1-a" or "asia-south1".
            state (google.cloud.network_security_v1alpha1.types.InterceptEndpointGroupAssociation.LocationDetails.State):
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
        state: "InterceptEndpointGroupAssociation.LocationDetails.State" = proto.Field(
            proto.ENUM,
            number=2,
            enum="InterceptEndpointGroupAssociation.LocationDetails.State",
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
    intercept_endpoint_group: str = proto.Field(
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
    locations: MutableSequence["InterceptLocation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message="InterceptLocation",
    )


class ListInterceptEndpointGroupAssociationsRequest(proto.Message):
    r"""Request message for ListInterceptEndpointGroupAssociations.

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
            ``ListInterceptEndpointGroups`` call. Provide this to
            retrieve the subsequent page. When paginating, all other
            parameters provided to ``ListInterceptEndpointGroups`` must
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


class ListInterceptEndpointGroupAssociationsResponse(proto.Message):
    r"""Response message for ListInterceptEndpointGroupAssociations.

    Attributes:
        intercept_endpoint_group_associations (MutableSequence[google.cloud.network_security_v1alpha1.types.InterceptEndpointGroupAssociation]):
            The associations from the specified parent.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages. See https://google.aip.dev/158 for more details.
    """

    @property
    def raw_page(self):
        return self

    intercept_endpoint_group_associations: MutableSequence[
        "InterceptEndpointGroupAssociation"
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="InterceptEndpointGroupAssociation",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetInterceptEndpointGroupAssociationRequest(proto.Message):
    r"""Request message for GetInterceptEndpointGroupAssociation.

    Attributes:
        name (str):
            Required. The name of the association to retrieve. Format:
            projects/{project}/locations/{location}/interceptEndpointGroupAssociations/{intercept_endpoint_group_association}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateInterceptEndpointGroupAssociationRequest(proto.Message):
    r"""Request message for CreateInterceptEndpointGroupAssociation.

    Attributes:
        parent (str):
            Required. The parent resource where this
            association will be created. Format:
            projects/{project}/locations/{location}
        intercept_endpoint_group_association_id (str):
            Optional. The ID to use for the new
            association, which will become the final
            component of the endpoint group's resource name.
            If not provided, the server will generate a
            unique ID.
        intercept_endpoint_group_association (google.cloud.network_security_v1alpha1.types.InterceptEndpointGroupAssociation):
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
    intercept_endpoint_group_association_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    intercept_endpoint_group_association: "InterceptEndpointGroupAssociation" = (
        proto.Field(
            proto.MESSAGE,
            number=3,
            message="InterceptEndpointGroupAssociation",
        )
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateInterceptEndpointGroupAssociationRequest(proto.Message):
    r"""Request message for UpdateInterceptEndpointGroupAssociation.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update. Fields are specified
            relative to the association (e.g. ``description``; *not*
            ``intercept_endpoint_group_association.description``). See
            https://google.aip.dev/161 for more details.
        intercept_endpoint_group_association (google.cloud.network_security_v1alpha1.types.InterceptEndpointGroupAssociation):
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
    intercept_endpoint_group_association: "InterceptEndpointGroupAssociation" = (
        proto.Field(
            proto.MESSAGE,
            number=2,
            message="InterceptEndpointGroupAssociation",
        )
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteInterceptEndpointGroupAssociationRequest(proto.Message):
    r"""Request message for DeleteInterceptEndpointGroupAssociation.

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


class InterceptDeploymentGroup(proto.Message):
    r"""A deployment group aggregates many zonal intercept backends
    (deployments) into a single global intercept service. Consumers
    can connect this service using an endpoint group.

    Attributes:
        name (str):
            Immutable. Identifier. The resource name of this deployment
            group, for example:
            ``projects/123456789/locations/global/interceptDeploymentGroups/my-dg``.
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
        connected_endpoint_groups (MutableSequence[google.cloud.network_security_v1alpha1.types.InterceptDeploymentGroup.ConnectedEndpointGroup]):
            Output only. The list of endpoint groups that
            are connected to this resource.
        nested_deployments (MutableSequence[google.cloud.network_security_v1alpha1.types.InterceptDeploymentGroup.Deployment]):
            Output only. The list of Intercept
            Deployments that belong to this group.
        state (google.cloud.network_security_v1alpha1.types.InterceptDeploymentGroup.State):
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
        locations (MutableSequence[google.cloud.network_security_v1alpha1.types.InterceptLocation]):
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
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        CREATING = 2
        DELETING = 3

    class ConnectedEndpointGroup(proto.Message):
        r"""An endpoint group connected to this deployment group.

        Attributes:
            name (str):
                Output only. The connected endpoint group's resource name,
                for example:
                ``projects/123456789/locations/global/interceptEndpointGroups/my-eg``.
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
                Output only. The name of the Intercept Deployment, in the
                format:
                ``projects/{project}/locations/{location}/interceptDeployments/{intercept_deployment}``.
            state (google.cloud.network_security_v1alpha1.types.InterceptDeployment.State):
                Output only. Most recent known state of the
                deployment.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        state: "InterceptDeployment.State" = proto.Field(
            proto.ENUM,
            number=2,
            enum="InterceptDeployment.State",
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
    locations: MutableSequence["InterceptLocation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message="InterceptLocation",
    )


class ListInterceptDeploymentGroupsRequest(proto.Message):
    r"""Request message for ListInterceptDeploymentGroups.

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
            ``ListInterceptDeploymentGroups`` call. Provide this to
            retrieve the subsequent page. When paginating, all other
            parameters provided to ``ListInterceptDeploymentGroups``
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


class ListInterceptDeploymentGroupsResponse(proto.Message):
    r"""Response message for ListInterceptDeploymentGroups.

    Attributes:
        intercept_deployment_groups (MutableSequence[google.cloud.network_security_v1alpha1.types.InterceptDeploymentGroup]):
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

    intercept_deployment_groups: MutableSequence["InterceptDeploymentGroup"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="InterceptDeploymentGroup",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetInterceptDeploymentGroupRequest(proto.Message):
    r"""Request message for GetInterceptDeploymentGroup.

    Attributes:
        name (str):
            Required. The name of the deployment group to retrieve.
            Format:
            projects/{project}/locations/{location}/interceptDeploymentGroups/{intercept_deployment_group}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateInterceptDeploymentGroupRequest(proto.Message):
    r"""Request message for CreateInterceptDeploymentGroup.

    Attributes:
        parent (str):
            Required. The parent resource where this
            deployment group will be created. Format:
            projects/{project}/locations/{location}
        intercept_deployment_group_id (str):
            Required. The ID to use for the new
            deployment group, which will become the final
            component of the deployment group's resource
            name.
        intercept_deployment_group (google.cloud.network_security_v1alpha1.types.InterceptDeploymentGroup):
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
    intercept_deployment_group_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    intercept_deployment_group: "InterceptDeploymentGroup" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="InterceptDeploymentGroup",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateInterceptDeploymentGroupRequest(proto.Message):
    r"""Request message for UpdateInterceptDeploymentGroup.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update. Fields are specified
            relative to the deployment group (e.g. ``description``;
            *not* ``intercept_deployment_group.description``). See
            https://google.aip.dev/161 for more details.
        intercept_deployment_group (google.cloud.network_security_v1alpha1.types.InterceptDeploymentGroup):
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
    intercept_deployment_group: "InterceptDeploymentGroup" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="InterceptDeploymentGroup",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteInterceptDeploymentGroupRequest(proto.Message):
    r"""Request message for DeleteInterceptDeploymentGroup.

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


class InterceptDeployment(proto.Message):
    r"""A deployment represents a zonal intercept backend ready to
    accept GENEVE-encapsulated traffic, e.g. a zonal instance group
    fronted by an internal passthrough load balancer. Deployments
    are always part of a global deployment group which represents a
    global intercept service.

    Attributes:
        name (str):
            Immutable. Identifier. The resource name of this deployment,
            for example:
            ``projects/123456789/locations/us-central1-a/interceptDeployments/my-dep``.
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
            fronts the interceptors, for example:
            ``projects/123456789/regions/us-central1/forwardingRules/my-rule``.
            See https://google.aip.dev/124.
        intercept_deployment_group (str):
            Required. Immutable. The deployment group that this
            deployment is a part of, for example:
            ``projects/123456789/locations/global/interceptDeploymentGroups/my-dg``.
            See https://google.aip.dev/124.
        state (google.cloud.network_security_v1alpha1.types.InterceptDeployment.State):
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
    intercept_deployment_group: str = proto.Field(
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


class ListInterceptDeploymentsRequest(proto.Message):
    r"""Request message for ListInterceptDeployments.

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
            ``ListInterceptDeployments`` call. Provide this to retrieve
            the subsequent page. When paginating, all other parameters
            provided to ``ListInterceptDeployments`` must match the call
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


class ListInterceptDeploymentsResponse(proto.Message):
    r"""Response message for ListInterceptDeployments.

    Attributes:
        intercept_deployments (MutableSequence[google.cloud.network_security_v1alpha1.types.InterceptDeployment]):
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

    intercept_deployments: MutableSequence["InterceptDeployment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="InterceptDeployment",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetInterceptDeploymentRequest(proto.Message):
    r"""Request message for GetInterceptDeployment.

    Attributes:
        name (str):
            Required. The name of the deployment to retrieve. Format:
            projects/{project}/locations/{location}/interceptDeployments/{intercept_deployment}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateInterceptDeploymentRequest(proto.Message):
    r"""Request message for CreateInterceptDeployment.

    Attributes:
        parent (str):
            Required. The parent resource where this
            deployment will be created. Format:
            projects/{project}/locations/{location}
        intercept_deployment_id (str):
            Required. The ID to use for the new
            deployment, which will become the final
            component of the deployment's resource name.
        intercept_deployment (google.cloud.network_security_v1alpha1.types.InterceptDeployment):
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
    intercept_deployment_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    intercept_deployment: "InterceptDeployment" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="InterceptDeployment",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateInterceptDeploymentRequest(proto.Message):
    r"""Request message for UpdateInterceptDeployment.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update. Fields are specified
            relative to the deployment (e.g. ``description``; *not*
            ``intercept_deployment.description``). See
            https://google.aip.dev/161 for more details.
        intercept_deployment (google.cloud.network_security_v1alpha1.types.InterceptDeployment):
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
    intercept_deployment: "InterceptDeployment" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="InterceptDeployment",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteInterceptDeploymentRequest(proto.Message):
    r"""Request message for DeleteInterceptDeployment.

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


class InterceptLocation(proto.Message):
    r"""Details about intercept in a specific cloud location.

    Attributes:
        location (str):
            Output only. The cloud location, e.g.
            "us-central1-a" or "asia-south1".
        state (google.cloud.network_security_v1alpha1.types.InterceptLocation.State):
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
