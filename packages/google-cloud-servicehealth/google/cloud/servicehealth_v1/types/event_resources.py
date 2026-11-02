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
    package="google.cloud.servicehealth.v1",
    manifest={
        "EventView",
        "OrganizationEventView",
        "Event",
        "OrganizationEvent",
        "EventUpdate",
        "Location",
        "Product",
        "EventImpact",
        "OrganizationImpact",
        "Asset",
        "ListEventsRequest",
        "ListEventsResponse",
        "GetEventRequest",
        "ListOrganizationEventsRequest",
        "ListOrganizationEventsResponse",
        "GetOrganizationEventRequest",
        "ListOrganizationImpactsRequest",
        "ListOrganizationImpactsResponse",
        "GetOrganizationImpactRequest",
    },
)


class EventView(proto.Enum):
    r"""The event fields to include in ListEvents API response. This
    enum lists all possible event views.

    Values:
        EVENT_VIEW_UNSPECIFIED (0):
            Unspecified event view. Default to ``EVENT_VIEW_BASIC``.
        EVENT_VIEW_BASIC (1):
            Includes all fields except ``updates``. This view is the
            default for ListEvents API.
        EVENT_VIEW_FULL (2):
            Includes all event fields.
    """

    EVENT_VIEW_UNSPECIFIED = 0
    EVENT_VIEW_BASIC = 1
    EVENT_VIEW_FULL = 2


class OrganizationEventView(proto.Enum):
    r"""The organization event fields to include in
    ListOrganizationEvents API response. This enum lists all
    possible organization event views.

    Values:
        ORGANIZATION_EVENT_VIEW_UNSPECIFIED (0):
            Unspecified event view. Default to
            ``ORGANIZATION_EVENT_VIEW_BASIC``.
        ORGANIZATION_EVENT_VIEW_BASIC (1):
            Includes all organization event fields except ``updates``.
            This view is the default for ListOrganizationEvents API.
        ORGANIZATION_EVENT_VIEW_FULL (2):
            Includes all organization event fields.
    """

    ORGANIZATION_EVENT_VIEW_UNSPECIFIED = 0
    ORGANIZATION_EVENT_VIEW_BASIC = 1
    ORGANIZATION_EVENT_VIEW_FULL = 2


class Event(proto.Message):
    r"""Represents service health events that may affect Google Cloud
    products. Event resource is a read-only view and does not allow
    any modifications. All fields are output only.

    Attributes:
        name (str):
            Output only. Identifier. Name of the event. Unique name of
            the event in this scope including project and location using
            the form
            ``projects/{project_id}/locations/{location}/events/{event_id}``.
        title (str):
            Output only. Brief description for the event.
        description (str):
            Output only. Free-form, human-readable
            description.
        category (google.cloud.servicehealth_v1.types.Event.EventCategory):
            Output only. The category of the event.
        detailed_category (google.cloud.servicehealth_v1.types.Event.DetailedCategory):
            Output only. The detailed category of the
            event.
        state (google.cloud.servicehealth_v1.types.Event.State):
            Output only. The current state of the event.
        detailed_state (google.cloud.servicehealth_v1.types.Event.DetailedState):
            Output only. The current detailed state of
            the incident.
        event_impacts (MutableSequence[google.cloud.servicehealth_v1.types.EventImpact]):
            Google Cloud products and locations impacted
            by the event.
        relevance (google.cloud.servicehealth_v1.types.Event.Relevance):
            Output only. Communicates why a given event
            is deemed relevant in the context of a given
            project.
        updates (MutableSequence[google.cloud.servicehealth_v1.types.EventUpdate]):
            Output only. Event updates are correspondence
            from Google.
        parent_event (str):
            Output only. When ``detailed_state``\ =\ ``MERGED``,
            ``parent_event`` contains the name of the parent event. All
            further updates will be published to the parent event.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the event was last
            modified.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The start time of the event, if
            applicable.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The end time of the event, if
            applicable.
        next_update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the next update
            can be expected.
    """

    class EventCategory(proto.Enum):
        r"""The category of the event. This enum lists all possible
        categories of event.

        Values:
            EVENT_CATEGORY_UNSPECIFIED (0):
                Unspecified category.
            INCIDENT (2):
                Event category for service outage or
                degradation.
        """

        EVENT_CATEGORY_UNSPECIFIED = 0
        INCIDENT = 2

    class DetailedCategory(proto.Enum):
        r"""The detailed category of an event. Contains all possible
        states for all event categories.

        Values:
            DETAILED_CATEGORY_UNSPECIFIED (0):
                Unspecified detailed category.
            CONFIRMED_INCIDENT (1):
                Indicates an event with category INCIDENT has
                a confirmed impact to at least one Google Cloud
                product.
            EMERGING_INCIDENT (2):
                Indicates an event with category INCIDENT is
                under investigation to determine if it has a
                confirmed impact on any Google Cloud products.
        """

        DETAILED_CATEGORY_UNSPECIFIED = 0
        CONFIRMED_INCIDENT = 1
        EMERGING_INCIDENT = 2

    class State(proto.Enum):
        r"""The state of the event. This enum lists all possible states
        of event.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state.
            ACTIVE (1):
                Event is actively affecting a Google Cloud
                product and will continue to receive updates.
            CLOSED (2):
                Event is no longer affecting the Google Cloud
                product or has been merged with another event.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        CLOSED = 2

    class DetailedState(proto.Enum):
        r"""The detailed state of the incident. This enum lists all
        possible detailed states of an incident.

        Values:
            DETAILED_STATE_UNSPECIFIED (0):
                Unspecified detail state.
            EMERGING (1):
                Google engineers are actively investigating
                the event to determine the impact.
            CONFIRMED (2):
                The incident is confirmed and impacting at
                least one Google Cloud product. Ongoing status
                updates will be provided until it is resolved.
            RESOLVED (3):
                The incident is no longer affecting any
                Google Cloud product, and there will be no
                further updates.
            MERGED (4):
                The incident was merged into a parent incident. All further
                updates will be published to the parent only. The
                ``parent_event`` field contains the name of the parent.
            AUTO_CLOSED (9):
                The incident was automatically closed because of the
                following reasons:

                - The impact of the incident could not be confirmed.
                - The incident was intermittent or resolved itself.

                The incident does not have a resolution because no action or
                investigation happened. If it is intermittent, the incident
                may reopen.
            FALSE_POSITIVE (10):
                Upon investigation, Google engineers
                concluded that the incident is not affecting a
                Google Cloud product. This state can change if
                the incident is reviewed again.
        """

        DETAILED_STATE_UNSPECIFIED = 0
        EMERGING = 1
        CONFIRMED = 2
        RESOLVED = 3
        MERGED = 4
        AUTO_CLOSED = 9
        FALSE_POSITIVE = 10

    class Relevance(proto.Enum):
        r"""Communicates why a given incident is deemed relevant in the
        context of a given project. This enum lists all possible
        detailed states of relevance.

        Values:
            RELEVANCE_UNSPECIFIED (0):
                Unspecified relevance.
            UNKNOWN (2):
                The relevance of the incident to the project
                is unknown.
            NOT_IMPACTED (6):
                The incident does not impact the project.
            PARTIALLY_RELATED (7):
                The incident is associated with a Google
                Cloud product your project uses, but the
                incident may not be impacting your project. For
                example, the incident may be impacting a Google
                Cloud product that your project uses, but in a
                location that your project does not use.
            RELATED (8):
                The incident has a direct connection with
                your project and impacts a Google Cloud product
                in a location your project uses.
            IMPACTED (9):
                The incident is verified to be impacting your
                project.
        """

        RELEVANCE_UNSPECIFIED = 0
        UNKNOWN = 2
        NOT_IMPACTED = 6
        PARTIALLY_RELATED = 7
        RELATED = 8
        IMPACTED = 9

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    title: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    category: EventCategory = proto.Field(
        proto.ENUM,
        number=4,
        enum=EventCategory,
    )
    detailed_category: DetailedCategory = proto.Field(
        proto.ENUM,
        number=21,
        enum=DetailedCategory,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    detailed_state: DetailedState = proto.Field(
        proto.ENUM,
        number=19,
        enum=DetailedState,
    )
    event_impacts: MutableSequence["EventImpact"] = proto.RepeatedField(
        proto.MESSAGE,
        number=20,
        message="EventImpact",
    )
    relevance: Relevance = proto.Field(
        proto.ENUM,
        number=8,
        enum=Relevance,
    )
    updates: MutableSequence["EventUpdate"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="EventUpdate",
    )
    parent_event: str = proto.Field(
        proto.STRING,
        number=10,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        message=timestamp_pb2.Timestamp,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=13,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=14,
        message=timestamp_pb2.Timestamp,
    )
    next_update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=15,
        message=timestamp_pb2.Timestamp,
    )


class OrganizationEvent(proto.Message):
    r"""Represents service health events that may affect Google Cloud
    products used across the organization. It is a read-only view
    and does not allow any modifications.

    Attributes:
        name (str):
            Output only. Identifier. Name of the event. Unique name of
            the event in this scope including organization ID and
            location using the form
            ``organizations/{organization_id}/locations/{location}/organizationEvents/{event_id}``.

            ``organization_id`` - see `Getting your organization
            resource
            ID <https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id>`__.
            ``location`` - The location to get the service health events
            from. ``event_id`` - Organization event ID to retrieve.
        title (str):
            Output only. Brief description for the event.
        description (str):
            Output only. Free-form, human-readable
            description.
        category (google.cloud.servicehealth_v1.types.OrganizationEvent.EventCategory):
            Output only. The category of the event.
        detailed_category (google.cloud.servicehealth_v1.types.OrganizationEvent.DetailedCategory):
            Output only. The detailed category of the
            event.
        state (google.cloud.servicehealth_v1.types.OrganizationEvent.State):
            Output only. The current state of the event.
        detailed_state (google.cloud.servicehealth_v1.types.OrganizationEvent.DetailedState):
            Output only. The current detailed state of
            the incident.
        event_impacts (MutableSequence[google.cloud.servicehealth_v1.types.EventImpact]):
            Output only. Represents the Google Cloud
            products and locations impacted by the event.
        updates (MutableSequence[google.cloud.servicehealth_v1.types.EventUpdate]):
            Output only. Incident-only field. Event
            updates are correspondence from Google.
        parent_event (str):
            Output only. When ``detailed_state``\ =\ ``MERGED``,
            ``parent_event`` contains the name of the parent event. All
            further updates will be published to the parent event.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the update was posted.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The start time of the event, if
            applicable.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The end time of the event, if
            applicable.
        next_update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Incident-only field. The time
            when the next update can be expected.
    """

    class EventCategory(proto.Enum):
        r"""The category of the event. This enum lists all possible
        categories of event.

        Values:
            EVENT_CATEGORY_UNSPECIFIED (0):
                Unspecified category.
            INCIDENT (2):
                Event category for service outage or
                degradation.
        """

        EVENT_CATEGORY_UNSPECIFIED = 0
        INCIDENT = 2

    class DetailedCategory(proto.Enum):
        r"""The detailed category of an event. Contains all possible
        states for all event categories.

        Values:
            DETAILED_CATEGORY_UNSPECIFIED (0):
                Unspecified detailed category.
            CONFIRMED_INCIDENT (1):
                Indicates an event with category INCIDENT has
                a confirmed impact to at least one Google Cloud
                product.
            EMERGING_INCIDENT (2):
                Indicates an event with category INCIDENT is
                under investigation to determine if it has a
                confirmed impact on any Google Cloud products.
        """

        DETAILED_CATEGORY_UNSPECIFIED = 0
        CONFIRMED_INCIDENT = 1
        EMERGING_INCIDENT = 2

    class State(proto.Enum):
        r"""The state of the organization event. This enum lists all
        possible states of event.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state.
            ACTIVE (1):
                Event is actively affecting a Google Cloud
                product and will continue to receive updates.
            CLOSED (2):
                Event is no longer affecting the Google Cloud
                product or has been merged with another event.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        CLOSED = 2

    class DetailedState(proto.Enum):
        r"""The detailed state of the incident. This enum lists all
        possible detailed states of an incident.

        Values:
            DETAILED_STATE_UNSPECIFIED (0):
                Unspecified detail state.
            EMERGING (1):
                Google engineers are actively investigating
                the incident to determine the impact.
            CONFIRMED (2):
                The incident is confirmed and impacting at
                least one Google Cloud product. Ongoing status
                updates will be provided until it is resolved.
            RESOLVED (3):
                The incident is no longer affecting any
                Google Cloud product, and there will be no
                further updates.
            MERGED (4):
                The incident was merged into a parent event. All further
                updates will be published to the parent only. The
                ``parent_event`` contains the name of the parent.
            AUTO_CLOSED (9):
                The incident was automatically closed because of the
                following reasons:

                - The impact of the incident could not be confirmed.
                - The incident was intermittent or resolved itself.

                The incident does not have a resolution because no action or
                investigation happened. If it is intermittent, the incident
                may reopen.
            FALSE_POSITIVE (10):
                Upon investigation, Google engineers
                concluded that the incident is not affecting a
                Google Cloud product. This state can change if
                the incident is reviewed again.
        """

        DETAILED_STATE_UNSPECIFIED = 0
        EMERGING = 1
        CONFIRMED = 2
        RESOLVED = 3
        MERGED = 4
        AUTO_CLOSED = 9
        FALSE_POSITIVE = 10

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    title: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    category: EventCategory = proto.Field(
        proto.ENUM,
        number=4,
        enum=EventCategory,
    )
    detailed_category: DetailedCategory = proto.Field(
        proto.ENUM,
        number=17,
        enum=DetailedCategory,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    detailed_state: DetailedState = proto.Field(
        proto.ENUM,
        number=16,
        enum=DetailedState,
    )
    event_impacts: MutableSequence["EventImpact"] = proto.RepeatedField(
        proto.MESSAGE,
        number=15,
        message="EventImpact",
    )
    updates: MutableSequence["EventUpdate"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="EventUpdate",
    )
    parent_event: str = proto.Field(
        proto.STRING,
        number=9,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=13,
        message=timestamp_pb2.Timestamp,
    )
    next_update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=14,
        message=timestamp_pb2.Timestamp,
    )


class EventUpdate(proto.Message):
    r"""Records an update made to the event.

    Attributes:
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the update was posted.
        title (str):
            Output only. Brief title for the event.
        description (str):
            Output only. Free-form, human-readable
            description.
        symptom (str):
            Output only. Symptoms of the event, if
            available.
        workaround (str):
            Output only. Workaround steps to remediate
            the event impact, if available.
    """

    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    title: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    symptom: str = proto.Field(
        proto.STRING,
        number=4,
    )
    workaround: str = proto.Field(
        proto.STRING,
        number=5,
    )


class Location(proto.Message):
    r"""Represents the locations impacted by the event.

    Attributes:
        location_name (str):
            Location impacted by the event. Example: ``"us-central1"``
    """

    location_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Product(proto.Message):
    r"""Represents the Google Cloud product impacted by the event.

    Attributes:
        product_name (str):
            Google Cloud product impacted by the event. Example:
            ``"Google Cloud SQL"``
        id (str):
            Unique identifier for the product.
    """

    product_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class EventImpact(proto.Message):
    r"""Represents the Google Cloud products and locations impacted
    by the event.

    Attributes:
        product (google.cloud.servicehealth_v1.types.Product):
            Google Cloud product impacted by the event.
        location (google.cloud.servicehealth_v1.types.Location):
            Location impacted by the event.
    """

    product: "Product" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Product",
    )
    location: "Location" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Location",
    )


class OrganizationImpact(proto.Message):
    r"""Represents impact to assets at organizational level. It is a
    read-only view and does not allow any modifications.

    Attributes:
        name (str):
            Output only. Identifier. Unique name of the organization
            impact in this scope including organization and location
            using the form
            ``organizations/{organization_id}/locations/{location}/organizationImpacts/{organization_impact_id}``.

            ``organization_id`` - ID (number) of the organization that
            contains the event. To get your ``organization_id``, see
            `Getting your organization resource
            ID <https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id>`__.
            ``organization_impact_id`` - ID of the `OrganizationImpact
            resource </service-health/docs/reference/rest/v1beta/organizations.locations.organizationImpacts#OrganizationImpact>`__.
        events (MutableSequence[str]):
            Output only. A list of event names impacting
            the asset.
        asset (google.cloud.servicehealth_v1.types.Asset):
            Output only. Google Cloud asset possibly
            impacted by the specified events.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the affected
            project was last modified.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    events: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    asset: "Asset" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Asset",
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class Asset(proto.Message):
    r"""Represents the asset impacted by the events.

    Attributes:
        asset_name (str):
            Output only. Full name of the resource as defined in
            `Resource
            Names <https://cloud.google.com/apis/design/resource_names#full_resource_name>`__.
        asset_type (str):
            Output only. Type of the asset. Example:
            ``"cloudresourcemanager.googleapis.com/Project"``
    """

    asset_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    asset_type: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListEventsRequest(proto.Message):
    r"""Requests list of events.

    Attributes:
        parent (str):
            Required. Parent value using the form
            ``projects/{project_id}/locations/{location}/events``.

            ``project_id`` - ID of the project for which to list service
            health events. ``location`` - The location to get the
            service health events from. To retrieve service health
            events of category = INCIDENT, use ``location`` =
            ``global``.
        page_size (int):
            Optional. The maximum number of events that should be
            returned. Acceptable values are 1 to 100, inclusive. (The
            default value is 10.) If more results are available, the
            service returns a next_page_token that you can use to get
            the next page of results in subsequent list requests. The
            service may return fewer events than the requested
            page_size.
        page_token (str):
            Optional. A token identifying a page of results the server
            should return. Provide Page token returned by a previous
            ``ListEvents`` call to retrieve the next page of results.
            When paginating, all other parameters provided to
            ``ListEvents`` must match the call that provided the page
            token.
        filter (str):
            Optional. A filter expression that filters resources listed
            in the response. The expression takes the following forms:

            - field=value for ``category`` and ``state``\
            - field <, >, <=, or >= value for ``update_time`` Examples:
              ``category=INCIDENT``,
              ``update_time>="2000-01-01T11:30:00-04:00"``,
              ``event_impacts.product.product_name:"Eventarc"``

            .. raw:: html

                <br>

            Multiple filter queries are separated by spaces. Example:
            ``category=INCIDENT state=ACTIVE``.

            By default, each expression is an AND expression. However,
            you can include AND and OR expressions explicitly.

            Filter is supported for the following fields: ``category``,
            ``state``, ``update_time``,
            ``event_impacts.product.product_name``
        view (google.cloud.servicehealth_v1.types.EventView):
            Optional. Event fields to include in
            response.
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
    view: "EventView" = proto.Field(
        proto.ENUM,
        number=6,
        enum="EventView",
    )


class ListEventsResponse(proto.Message):
    r"""Response to request for listing events.

    Attributes:
        events (MutableSequence[google.cloud.servicehealth_v1.types.Event]):
            Output only. List of events.
        next_page_token (str):
            Output only. The continuation token, used to page through
            large result sets. Provide this value in a subsequent
            request as page_token to retrieve the next page.

            If this field is not present, there are no subsequent
            results.
        unreachable (MutableSequence[str]):
            Output only. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    events: MutableSequence["Event"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Event",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetEventRequest(proto.Message):
    r"""Gets information about a specific event.

    Attributes:
        name (str):
            Required. Unique name of the event in this scope including
            project and location using the form
            ``projects/{project_id}/locations/{location}/events/{event_id}``.

            ``project_id`` - Project ID of the project that contains the
            event. ``location`` - The location to get the service health
            events from. ``event_id`` - Event ID to retrieve.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListOrganizationEventsRequest(proto.Message):
    r"""Requests list of events that affect an organization.

    Attributes:
        parent (str):
            Required. Parent value using the form
            ``organizations/{organization_id}/locations/{location}/organizationEvents``.

            ``organization_id`` - ID (number) of the project that
            contains the event. To get your ``organization_id``, see
            `Getting your organization resource
            ID <https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id>`__.
            ``location`` - The location to get the service health events
            from. To retrieve service health events of category =
            INCIDENT, use ``location`` = ``global``.
        page_size (int):
            Optional. The maximum number of events that should be
            returned. Acceptable values are ``1`` to ``100``, inclusive.
            (The default value is ``10``.) If more results are
            available, the service returns a ``next_page_token`` that
            you can use to get the next page of results in subsequent
            list requests. The service may return fewer events than the
            requested ``page_size``.
        page_token (str):
            Optional. A token identifying a page of results the server
            should return.

            Provide Page token returned by a previous
            ``ListOrganizationEvents`` call to retrieve the next page of
            results.

            When paginating, all other parameters provided to
            ``ListOrganizationEvents`` must match the call that provided
            the page token.
        filter (str):
            Optional. A filter expression that filters resources listed
            in the response. The expression takes the following forms:

            - field=value for ``category`` and ``state``
            - field <, >, <=, or >= value for ``update_time``

            Examples: ``category=INCIDENT``,
            ``update_time>="2000-01-01T11:30:00-04:00"``

            Multiple filter queries are space-separated. Example:
            ``category=INCIDENT state=ACTIVE``.

            By default, each expression is an AND expression. However,
            you can include AND and OR expressions explicitly.

            Filter is supported for the following fields: ``category``,
            ``state``, ``update_time``
        view (google.cloud.servicehealth_v1.types.OrganizationEventView):
            Optional. OrganizationEvent fields to include
            in response.
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
    view: "OrganizationEventView" = proto.Field(
        proto.ENUM,
        number=6,
        enum="OrganizationEventView",
    )


class ListOrganizationEventsResponse(proto.Message):
    r"""Response to request for listing organization events.

    Attributes:
        organization_events (MutableSequence[google.cloud.servicehealth_v1.types.OrganizationEvent]):
            Output only. List of organization events
            affecting an organization.
        next_page_token (str):
            Output only. The continuation token, used to page through
            large result sets. Provide this value in a subsequent
            request as ``page_token`` to retrieve the next page.

            If this field is not present, there are no subsequent
            results.
        unreachable (MutableSequence[str]):
            Output only. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    organization_events: MutableSequence["OrganizationEvent"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="OrganizationEvent",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetOrganizationEventRequest(proto.Message):
    r"""Gets information about a specific event affecting an
    organization.

    Attributes:
        name (str):
            Required. Unique name of the event in this scope including
            organization and event ID using the form
            ``organizations/{organization_id}/locations/locations/global/organizationEvents/{event_id}``.

            ``organization_id`` - ID (number) of the project that
            contains the event. To get your ``organization_id``, see
            `Getting your organization resource
            ID <https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id>`__.
            ``event_id`` - Organization event ID to retrieve.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListOrganizationImpactsRequest(proto.Message):
    r"""Requests list of projects under an organization affected by
    an event.

    Attributes:
        parent (str):
            Required. Parent value using the form
            ``organizations/{organization_id}/locations/{location}/organizationImpacts``.

            ``organization_id`` - ID (number) of the project that
            contains the event. To get your ``organization_id``, see
            `Getting your organization resource
            ID <https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id>`__.
        page_size (int):
            Optional. The maximum number of events that should be
            returned. Acceptable values are ``1`` to ``100``, inclusive.
            The default value is ``10``.

            If more results are available, the service returns a
            ``next_page_token`` that can be used to get the next page of
            results in subsequent list requests. The service may return
            fewer
            `impacts </service-health/docs/reference/rest/v1beta/organizations.locations.organizationImpacts#OrganizationImpact>`__
            than the requested ``page_size``.
        page_token (str):
            Optional. A token identifying a page of results the server
            should return.

            Provide ``page_token`` returned by a previous
            ``ListOrganizationImpacts`` call to retrieve the next page
            of results.

            When paginating, all other parameters provided to
            ``ListOrganizationImpacts`` must match the call that
            provided the page token.
        filter (str):
            Optional. A filter expression that filters resources listed
            in the response. The expression is in the form of
            ``field:value`` for checking if a repeated field contains a
            value.

            Example:
            ``events:organizations%2F{organization_id}%2Flocations%2Fglobal%2ForganizationEvents%2Fevent-id``

            To get your ``{organization_id}``, see `Getting your
            organization resource
            ID <https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id>`__.

            Multiple filter queries are separated by spaces.

            By default, each expression is an AND expression. However,
            you can include AND and OR expressions explicitly. Filter is
            supported for the following fields: ``events``.
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


class ListOrganizationImpactsResponse(proto.Message):
    r"""Response to request for listing projects under an
    organization affected by an event.

    Attributes:
        organization_impacts (MutableSequence[google.cloud.servicehealth_v1.types.OrganizationImpact]):
            Output only. List of
            `impacts </service-health/docs/reference/rest/v1beta/organizations.locations.organizationImpacts#OrganizationImpact>`__
            for an organization affected by service health events.
        next_page_token (str):
            Output only. The continuation token, used to page through
            large result sets. Provide this value in a subsequent
            request as ``page_token`` to retrieve the next page.

            If this field is not present, there are no subsequent
            results.
        unreachable (MutableSequence[str]):
            Output only. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    organization_impacts: MutableSequence["OrganizationImpact"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="OrganizationImpact",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetOrganizationImpactRequest(proto.Message):
    r"""Gets information about an event that affects a project under
    an organization.

    Attributes:
        name (str):
            Required. Name of the resource using the form
            ``organizations/{organization_id}/locations/global/organizationImpacts/{organization_impact_id}``.

            ``organization_id`` - ID (number) of the organization that
            contains the event. To get your ``organization_id``, see
            `Getting your organization resource
            ID <https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id>`__.
            ``organization_impact_id`` - ID of the `OrganizationImpact
            resource </service-health/docs/reference/rest/v1beta/organizations.locations.organizationImpacts#OrganizationImpact>`__.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
