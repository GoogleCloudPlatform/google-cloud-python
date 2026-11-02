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

import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.type.latlng_pb2 as latlng_pb2  # type: ignore
import google.type.localized_text_pb2 as localized_text_pb2  # type: ignore
import google.type.postal_address_pb2 as postal_address_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.maps.geocode.v4",
    manifest={
        "SearchDestinationsRequest",
        "SearchDestinationsResponse",
        "Destination",
        "PlaceView",
        "Entrance",
        "NavigationPoint",
        "Landmark",
    },
)


class SearchDestinationsRequest(proto.Message):
    r"""Request message for DestinationService.SearchDestinations.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        place (str):
            The resource name of a place, in ``places/{place_id}``
            format.

            This field is a member of `oneof`_ ``primary_query``.
        address_query (google.maps.geocode_v4.types.SearchDestinationsRequest.AddressQuery):
            A street address.

            This field is a member of `oneof`_ ``primary_query``.
        location_query (google.maps.geocode_v4.types.SearchDestinationsRequest.LocationQuery):
            A precise location.

            This field is a member of `oneof`_ ``primary_query``.
        travel_modes (MutableSequence[google.maps.geocode_v4.types.NavigationPoint.TravelMode]):
            Optional. The travel modes to filter navigation points for.
            This influences the ``navigation_points`` field returned in
            the response. If empty, navigation points of all travel
            modes are returned.
        language_code (str):
            Optional. Language in which the results
            should be returned.
        region_code (str):
            Optional. Region code. The region code,
            specified as a ccTLD ("top-level domain")
            two-character value. The parameter affects
            results based on applicable law. This parameter
            also influences, but not fully restricts,
            results from the service.
    """

    class AddressQuery(proto.Message):
        r"""The street address that you want to search for. Specify
        addresses in accordance with the format used by the national
        postal service of the country concerned.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            address (google.type.postal_address_pb2.PostalAddress):
                A street address in postal address format.

                This field is a member of `oneof`_ ``kind``.
            address_query (str):
                A street address formatted as a single line.

                This field is a member of `oneof`_ ``kind``.
        """

        address: postal_address_pb2.PostalAddress = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="kind",
            message=postal_address_pb2.PostalAddress,
        )
        address_query: str = proto.Field(
            proto.STRING,
            number=2,
            oneof="kind",
        )

    class LocationQuery(proto.Message):
        r"""A location query to identify a nearby primary destination.

        Note: if the location query is within a building that contains
        subpremises, it is possible that the returned primary place is a
        subpremise. In these cases, the ``containing_places`` field will
        include the building.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            location (google.type.latlng_pb2.LatLng):
                A precise LatLng location.

                This field is a member of `oneof`_ ``kind``.
            place_filter (google.maps.geocode_v4.types.SearchDestinationsRequest.LocationQuery.PlaceFilter):
                Optional. Filters to apply to destination
                candidates.
        """

        class PlaceFilter(proto.Message):
            r"""Filters to apply to destination candidates.

            Attributes:
                structure_type (google.maps.geocode_v4.types.PlaceView.StructureType):
                    Optional. If specified, all destinations are guaranteed to
                    have a primary place with this structure type. This can
                    result in filtering out some destinations, or in
                    coarsening/refining the returned destinations.

                    For example, if ``GROUNDS`` is specified, all returned
                    destinations will have a primary place with the ``GROUNDS``
                    structure type. This can result in filtering out some
                    destinations that are not part of a grounds, or in
                    coarsening the returned destinations to the grounds level.

                    Another use of this field is to more easily extract building
                    display polygons. For example, if ``BUILDING`` is specified,
                    the primary place's display polygon will be for the building
                    at the specified location.
                addressability (google.maps.geocode_v4.types.SearchDestinationsRequest.LocationQuery.PlaceFilter.Addressability):
                    Optional. If specified, only returns
                    destinations that meet the corresponding
                    addressability criteria.
            """

            class Addressability(proto.Enum):
                r"""Defines options for addressability filtering. New values may
                be added in the future.

                Values:
                    ADDRESSABILITY_UNSPECIFIED (0):
                        When unspecified, the service will choose a
                        sensible default.
                    ANY (1):
                        Addressability is not a filtering criteria.
                        Destinations are returned regardless of their
                        addressability.
                    PRIMARY (2):
                        All destinations returned will have a primary
                        place with a street level address or name.
                    WEAK (3):
                        All destinations returned will have either a
                        primary place or a subdestination with a street
                        level address or name.
                """

                ADDRESSABILITY_UNSPECIFIED = 0
                ANY = 1
                PRIMARY = 2
                WEAK = 3

            structure_type: "PlaceView.StructureType" = proto.Field(
                proto.ENUM,
                number=2,
                enum="PlaceView.StructureType",
            )
            addressability: "SearchDestinationsRequest.LocationQuery.PlaceFilter.Addressability" = proto.Field(
                proto.ENUM,
                number=3,
                enum="SearchDestinationsRequest.LocationQuery.PlaceFilter.Addressability",
            )

        location: latlng_pb2.LatLng = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="kind",
            message=latlng_pb2.LatLng,
        )
        place_filter: "SearchDestinationsRequest.LocationQuery.PlaceFilter" = (
            proto.Field(
                proto.MESSAGE,
                number=2,
                message="SearchDestinationsRequest.LocationQuery.PlaceFilter",
            )
        )

    place: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="primary_query",
    )
    address_query: AddressQuery = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="primary_query",
        message=AddressQuery,
    )
    location_query: LocationQuery = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="primary_query",
        message=LocationQuery,
    )
    travel_modes: MutableSequence["NavigationPoint.TravelMode"] = proto.RepeatedField(
        proto.ENUM,
        number=5,
        enum="NavigationPoint.TravelMode",
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=6,
    )
    region_code: str = proto.Field(
        proto.STRING,
        number=7,
    )


class SearchDestinationsResponse(proto.Message):
    r"""Response message for DestinationService.SearchDestinations.

    Attributes:
        destinations (MutableSequence[google.maps.geocode_v4.types.Destination]):
            A list of destinations.

            The service returns one result if a primary
            destination can be unambiguously identified from
            the primary query. Otherwise, the service might
            return multiple results for disambiguation or
            zero results.
    """

    destinations: MutableSequence["Destination"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Destination",
    )


class Destination(proto.Message):
    r"""A destination. This includes the primary place, related
    places, entrances, and navigation points.

    Attributes:
        primary (google.maps.geocode_v4.types.PlaceView):
            The primary place identified by the ``primary_query`` in the
            request.
        containing_places (MutableSequence[google.maps.geocode_v4.types.PlaceView]):
            The less precise places that the primary
            place is contained by. For example, the
            apartment complex that contains this building.
        sub_destinations (MutableSequence[google.maps.geocode_v4.types.PlaceView]):
            More precise sub-destinations of the primary place. For
            example, units contained in a building.

            Note: compared to the
            `SubDestination </maps/documentation/places/web-service/reference/rest/v1/places#SubDestination>`__
            returned by the Places API, this list of sub-destinations is
            more exhaustive, and each sub-destination contains more
            information.
        landmarks (MutableSequence[google.maps.geocode_v4.types.Landmark]):
            Landmarks that can be used to communicate
            where the destination is or help with arrival.
        entrances (MutableSequence[google.maps.geocode_v4.types.Entrance]):
            Entrances for this destination.
        navigation_points (MutableSequence[google.maps.geocode_v4.types.NavigationPoint]):
            Navigation points for this destination.
    """

    primary: "PlaceView" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="PlaceView",
    )
    containing_places: MutableSequence["PlaceView"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="PlaceView",
    )
    sub_destinations: MutableSequence["PlaceView"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="PlaceView",
    )
    landmarks: MutableSequence["Landmark"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="Landmark",
    )
    entrances: MutableSequence["Entrance"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="Entrance",
    )
    navigation_points: MutableSequence["NavigationPoint"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="NavigationPoint",
    )


class PlaceView(proto.Message):
    r"""Represents a view of a
    `Place <https://developers.google.com/maps/documentation/places/web-service/reference/rest/v1/places#resource:-place>`__
    in the Places API. It also provides additional information specific
    to destinations, such as the structure type and the display polygon.

    In some cases, a ``PlaceView`` with the same place ID might differ
    from what is being returned by the Places API for the ``types`` and
    ``display_name`` fields.

    Attributes:
        place (str):
            This Place's resource name, in ``places/{placeId}`` format.
            Can be used to look up the Place.
        place_id (str):
            The unique identifier of a place.
        display_name (google.type.localized_text_pb2.LocalizedText):
            Human readable place description. For
            example, "Gate B", "McDonalds".
        primary_type (str):
            The primary place type of this place. See
            https://developers.google.com/maps/documentation/places/web-service/place-types
            for the list of possible values.

            Note: This field is not always populated. Be prepared to use
            the ``types`` field in such situations.
        types (MutableSequence[str]):
            All associated place types of this place. See
            https://developers.google.com/maps/documentation/places/web-service/place-types
            for the list of possible values.
        formatted_address (str):
            One line address.
        postal_address (google.type.postal_address_pb2.PostalAddress):
            Structured address.
        structure_type (google.maps.geocode_v4.types.PlaceView.StructureType):
            The type of structure corresponding to this
            place.
        location (google.type.latlng_pb2.LatLng):
            The location of this place. For places with
            display polygons, this can represent a good spot
            to put a marker on the map.
        display_polygon (google.protobuf.struct_pb2.Struct):
            The polygon outline of the place in GeoJSON format, using
            the RFC 7946 format:
            https://datatracker.ietf.org/doc/html/rfc7946#section-3.1.6.

            Note: The RFC 7946 format supports MultiPolygons, so one
            ``display_polygon`` object can represent multiple polygons.
    """

    class StructureType(proto.Enum):
        r"""The type of structure that this place represents.

        Values:
            STRUCTURE_TYPE_UNSPECIFIED (0):
                Not used.
            POINT (1):
                A point location.
            SECTION (2):
                A sub-section of a building.
            BUILDING (3):
                A building.
            GROUNDS (4):
                A large area that typically contains multiple
                buildings, such as a university campus, an
                apartment complex, or a shopping mall.
        """

        STRUCTURE_TYPE_UNSPECIFIED = 0
        POINT = 1
        SECTION = 2
        BUILDING = 3
        GROUNDS = 4

    place: str = proto.Field(
        proto.STRING,
        number=1,
    )
    place_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: localized_text_pb2.LocalizedText = proto.Field(
        proto.MESSAGE,
        number=3,
        message=localized_text_pb2.LocalizedText,
    )
    primary_type: str = proto.Field(
        proto.STRING,
        number=4,
    )
    types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    formatted_address: str = proto.Field(
        proto.STRING,
        number=6,
    )
    postal_address: postal_address_pb2.PostalAddress = proto.Field(
        proto.MESSAGE,
        number=7,
        message=postal_address_pb2.PostalAddress,
    )
    structure_type: StructureType = proto.Field(
        proto.ENUM,
        number=8,
        enum=StructureType,
    )
    location: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=9,
        message=latlng_pb2.LatLng,
    )
    display_polygon: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=10,
        message=struct_pb2.Struct,
    )


class Entrance(proto.Message):
    r"""An entrance is a single latitude/longitude coordinate pair
    that defines the location of an entry and exit point for a
    place.

    Attributes:
        location (google.type.latlng_pb2.LatLng):
            The location of the entrance.
        tags (MutableSequence[google.maps.geocode_v4.types.Entrance.Tag]):
            A list of tags that describe the entrance.
        place (str):
            The structure this entrance is physically located on, in
            ``places/{place_id}`` format.
    """

    class Tag(proto.Enum):
        r"""Characteristics that describe an entrance.

        Values:
            TAG_UNSPECIFIED (0):
                Not used.
            PREFERRED (1):
                The entrance likely provides physical access to the primary
                place in the returned destination. A place can have multiple
                preferred entrances. If an entrance does not have this tag,
                it means the entrance is physically on the same building as
                the primary place, but does not necessarily provide access
                to the place.

                For example, if the primary place is a restaurant in a strip
                mall, the "PREFERRED" entrances will be the ones that likely
                lead into the restaurant itself, while the other returned
                entrances will be other entrances for the building, such as
                entrances into other restaurants in the strip mall.

                If the primary place is a building itself, the ``PREFERRED``
                entrances will be the ones that lead into the "main" part of
                the building. For example, in a shopping center the
                ``PREFERRED`` entrances will be the ones that allow access
                to the main foyer area, but if an entrance only provides
                access to a store on the side of the building, it won't be a
                ``PREFERRED`` entrance.

                Note: a ``PREFERRED`` entrance might not provide access to
                the primary place, and a non-``PREFERRED`` entrance might
                provide access to the primary place.
        """

        TAG_UNSPECIFIED = 0
        PREFERRED = 1

    location: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=2,
        message=latlng_pb2.LatLng,
    )
    tags: MutableSequence[Tag] = proto.RepeatedField(
        proto.ENUM,
        number=3,
        enum=Tag,
    )
    place: str = proto.Field(
        proto.STRING,
        number=4,
    )


class NavigationPoint(proto.Message):
    r"""A navigation point is a location next to a road where
    navigation can end.

    Attributes:
        navigation_point_token (str):
            Output only. A token that can be used to
            identify this navigation point.
        display_name (google.type.localized_text_pb2.LocalizedText):
            The display name of this navigation point.
            For example, "5th Ave" or "Gate B".
        location (google.type.latlng_pb2.LatLng):
            A point next to the road segment where
            navigation should end. The point is
            intentionally slightly offset from the road's
            centerline to clearly mark the side of the road
            where the place is located.
        travel_modes (MutableSequence[google.maps.geocode_v4.types.NavigationPoint.TravelMode]):
            Travel modes that are appropriate for this
            navigation point.
        usages (MutableSequence[google.maps.geocode_v4.types.NavigationPoint.Usage]):
            Lists ``usages`` supported by this navigation point. If
            empty, it does not necessarily mean its usage is restricted
            in any way. All navigation points can be used for general
            navigation.
    """

    class TravelMode(proto.Enum):
        r"""Travel modes that are appropriate for this navigation point.

        Values:
            TRAVEL_MODE_UNSPECIFIED (0):
                Not used.
            DRIVE (1):
                Suitable for driving.
            WALK (2):
                Suitable for walking.
        """

        TRAVEL_MODE_UNSPECIFIED = 0
        DRIVE = 1
        WALK = 2

    class Usage(proto.Enum):
        r"""Usages supported by this navigation point.
        New values may be added in the future.

        Values:
            USAGE_UNSPECIFIED (0):
                Not used.
            UNKNOWN (1):
                Indicates that the usage type is unknown.
            DROPOFF (2):
                Suitable for dropping off a passenger. For
                example, a rideshare drop off location.
            PICKUP (3):
                Suitable for picking up a passenger. For
                example, a rideshare pick up location.
            PARKING (4):
                Suitable for parking. For example, within a
                parking lot.
        """

        USAGE_UNSPECIFIED = 0
        UNKNOWN = 1
        DROPOFF = 2
        PICKUP = 3
        PARKING = 4

    navigation_point_token: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: localized_text_pb2.LocalizedText = proto.Field(
        proto.MESSAGE,
        number=2,
        message=localized_text_pb2.LocalizedText,
    )
    location: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=3,
        message=latlng_pb2.LatLng,
    )
    travel_modes: MutableSequence[TravelMode] = proto.RepeatedField(
        proto.ENUM,
        number=4,
        enum=TravelMode,
    )
    usages: MutableSequence[Usage] = proto.RepeatedField(
        proto.ENUM,
        number=5,
        enum=Usage,
    )


class Landmark(proto.Message):
    r"""Landmarks are used to communicate where the destination is or
    help with arriving at the destination.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        place (google.maps.geocode_v4.types.PlaceView):
            The place that represents this landmark.

            This field is a member of `oneof`_ ``landmark``.
        relational_description (google.type.localized_text_pb2.LocalizedText):
            A human-readable description of how the
            destination relates to the landmark. For
            example: "Near the Empire State Building" or
            "Across from the White House".
        tags (MutableSequence[google.maps.geocode_v4.types.Landmark.Tag]):
            Tags that describe how the landmark can be
            used in the context of the destination.
        straight_line_distance_meters (float):
            Output only. The straight-line distance from
            this landmark to the destination in meters.
        travel_distance_meters (float):
            Output only. The road-network distance from
            this landmark to the destination in meters.
    """

    class Tag(proto.Enum):
        r"""The list of all possible tags that describe how a landmark can be
        used in the context of a destination.

        If an address has both the ``ADDRESS`` and ``ARRIVAL`` tags, it
        means the landmark is both locally prominent and close to the
        destination.

        Values:
            TAG_UNSPECIFIED (0):
                Not used.
            ADDRESS (1):
                A locally prominent place that can be used to
                identify the general location of the
                destination. Typically within a few hundred
                meters of the destination. These are similar to
                the landmarks returned by the Address
                Descriptors feature of the Geocoding API:

                https://developers.google.com/maps/documentation/geocoding/address-descriptors/requests-address-descriptors.
            ARRIVAL (2):
                A place that can be used to help arrive at the destination.
                Useful for navigation once you are close to the destination.
                For example, this landmark might be a place that is across
                the street from the destination. A landmark with this tag is
                typically closer to the destination than landmarks with the
                ``ADDRESS`` tag.
        """

        TAG_UNSPECIFIED = 0
        ADDRESS = 1
        ARRIVAL = 2

    place: "PlaceView" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="landmark",
        message="PlaceView",
    )
    relational_description: localized_text_pb2.LocalizedText = proto.Field(
        proto.MESSAGE,
        number=2,
        message=localized_text_pb2.LocalizedText,
    )
    tags: MutableSequence[Tag] = proto.RepeatedField(
        proto.ENUM,
        number=3,
        enum=Tag,
    )
    straight_line_distance_meters: float = proto.Field(
        proto.DOUBLE,
        number=4,
    )
    travel_distance_meters: float = proto.Field(
        proto.DOUBLE,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
