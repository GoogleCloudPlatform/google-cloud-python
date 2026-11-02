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

import google.type.latlng_pb2 as latlng_pb2  # type: ignore
import proto  # type: ignore
from google.geo.type.types import viewport

from google.maps.places_v1.types import (
    contextual_content,
    ev_charging,
    geometry,
    routing_summary,
)
from google.maps.places_v1.types import place as gmp_place
from google.maps.places_v1.types import polyline as gmp_polyline
from google.maps.places_v1.types import route_modifiers as gmp_route_modifiers
from google.maps.places_v1.types import routing_preference as gmp_routing_preference
from google.maps.places_v1.types import travel_mode as gmp_travel_mode

__protobuf__ = proto.module(
    package="google.maps.places.v1",
    manifest={
        "RoutingParameters",
        "SearchNearbyRequest",
        "SearchNearbyResponse",
        "SearchTextRequest",
        "SearchTextResponse",
        "GetPhotoMediaRequest",
        "PhotoMedia",
        "GetPlaceRequest",
        "AutocompletePlacesRequest",
        "AutocompletePlacesResponse",
    },
)


class RoutingParameters(proto.Message):
    r"""Parameters to configure the routing calculations to the
    places in the response, both along a route (where result ranking
    will be influenced) and for calculating travel times on results.

    Attributes:
        origin (google.type.latlng_pb2.LatLng):
            Optional. An explicit routing origin that
            overrides the origin defined in the polyline. By
            default, the polyline origin is used.
        travel_mode (google.maps.places_v1.types.TravelMode):
            Optional. The travel mode.
        route_modifiers (google.maps.places_v1.types.RouteModifiers):
            Optional. The route modifiers.
        routing_preference (google.maps.places_v1.types.RoutingPreference):
            Optional. Specifies how to compute the routing summaries.
            The server attempts to use the selected routing preference
            to compute the route. The traffic aware routing preference
            is only available for the ``DRIVE`` or ``TWO_WHEELER``
            ``travelMode``.
    """

    origin: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=1,
        message=latlng_pb2.LatLng,
    )
    travel_mode: gmp_travel_mode.TravelMode = proto.Field(
        proto.ENUM,
        number=2,
        enum=gmp_travel_mode.TravelMode,
    )
    route_modifiers: gmp_route_modifiers.RouteModifiers = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gmp_route_modifiers.RouteModifiers,
    )
    routing_preference: gmp_routing_preference.RoutingPreference = proto.Field(
        proto.ENUM,
        number=4,
        enum=gmp_routing_preference.RoutingPreference,
    )


class SearchNearbyRequest(proto.Message):
    r"""Request proto for Search Nearby.

    Attributes:
        language_code (str):
            Place details will be displayed with the
            preferred language if available. If the language
            code is unspecified or unrecognized, place
            details of any language may be returned, with a
            preference for English if such details exist.

            Current list of supported languages:

            https://developers.google.com/maps/faq#languagesupport.
        region_code (str):
            The Unicode country/region code (CLDR) of the location where
            the request is coming from. This parameter is used to
            display the place details, like region-specific place name,
            if available. The parameter can affect results based on
            applicable law.

            For more information, see
            https://www.unicode.org/cldr/charts/latest/supplemental/territory_language_information.html.

            Note that 3-digit region codes are not currently supported.
        included_types (MutableSequence[str]):
            Included Place type (eg, "restaurant" or "gas_station") from
            https://developers.google.com/maps/documentation/places/web-service/place-types.

            Up to 50 types from `Table
            A <https://developers.google.com/maps/documentation/places/web-service/place-types#table-a>`__
            may be specified.

            If there are any conflicting types, i.e. a type appears in
            both included_types and excluded_types, an INVALID_ARGUMENT
            error is returned.

            If a Place type is specified with multiple type
            restrictions, only places that satisfy all of the
            restrictions are returned. For example, if we have
            {included_types = ["restaurant"], excluded_primary_types =
            ["restaurant"]}, the returned places provide "restaurant"
            related services but do not operate primarily as
            "restaurants".
        excluded_types (MutableSequence[str]):
            Excluded Place type (eg, "restaurant" or "gas_station") from
            https://developers.google.com/maps/documentation/places/web-service/place-types.

            Up to 50 types from `Table
            A <https://developers.google.com/maps/documentation/places/web-service/place-types#table-a>`__
            may be specified.

            If the client provides both included_types (e.g. restaurant)
            and excluded_types (e.g. cafe), then the response should
            include places that are restaurant but not cafe. The
            response includes places that match at least one of the
            included_types and none of the excluded_types.

            If there are any conflicting types, i.e. a type appears in
            both included_types and excluded_types, an INVALID_ARGUMENT
            error is returned.

            If a Place type is specified with multiple type
            restrictions, only places that satisfy all of the
            restrictions are returned. For example, if we have
            {included_types = ["restaurant"], excluded_primary_types =
            ["restaurant"]}, the returned places provide "restaurant"
            related services but do not operate primarily as
            "restaurants".
        included_primary_types (MutableSequence[str]):
            Included primary Place type (e.g. "restaurant" or
            "gas_station") from
            https://developers.google.com/maps/documentation/places/web-service/place-types.
            A place can only have a single primary type from the
            supported types table associated with it.

            Up to 50 types from `Table
            A <https://developers.google.com/maps/documentation/places/web-service/place-types#table-a>`__
            may be specified.

            If there are any conflicting primary types, i.e. a type
            appears in both included_primary_types and
            excluded_primary_types, an INVALID_ARGUMENT error is
            returned.

            If a Place type is specified with multiple type
            restrictions, only places that satisfy all of the
            restrictions are returned. For example, if we have
            {included_types = ["restaurant"], excluded_primary_types =
            ["restaurant"]}, the returned places provide "restaurant"
            related services but do not operate primarily as
            "restaurants".
        excluded_primary_types (MutableSequence[str]):
            Excluded primary Place type (e.g. "restaurant" or
            "gas_station") from
            https://developers.google.com/maps/documentation/places/web-service/place-types.

            Up to 50 types from `Table
            A <https://developers.google.com/maps/documentation/places/web-service/place-types#table-a>`__
            may be specified.

            If there are any conflicting primary types, i.e. a type
            appears in both included_primary_types and
            excluded_primary_types, an INVALID_ARGUMENT error is
            returned.

            If a Place type is specified with multiple type
            restrictions, only places that satisfy all of the
            restrictions are returned. For example, if we have
            {included_types = ["restaurant"], excluded_primary_types =
            ["restaurant"]}, the returned places provide "restaurant"
            related services but do not operate primarily as
            "restaurants".
        max_result_count (int):
            Maximum number of results to return. It must be between 1
            and 20 (default), inclusively. If the number is unset, it
            falls back to the upper limit. If the number is set to
            negative or exceeds the upper limit, an INVALID_ARGUMENT
            error is returned.
        location_restriction (google.maps.places_v1.types.SearchNearbyRequest.LocationRestriction):
            Required. The region to search.
        rank_preference (google.maps.places_v1.types.SearchNearbyRequest.RankPreference):
            How results will be ranked in the response.
        routing_parameters (google.maps.places_v1.types.RoutingParameters):
            Optional. Parameters that affect the routing
            to the search results.
        include_future_opening_businesses (bool):
            Optional. If true, include businesses that
            are not yet open but will open in the future.
    """

    class RankPreference(proto.Enum):
        r"""How results will be ranked in the response.

        Values:
            RANK_PREFERENCE_UNSPECIFIED (0):
                RankPreference value not set. Will use rank
                by POPULARITY by default.
            DISTANCE (1):
                Ranks results by distance.
            POPULARITY (2):
                Ranks results by popularity.
        """

        RANK_PREFERENCE_UNSPECIFIED = 0
        DISTANCE = 1
        POPULARITY = 2

    class LocationRestriction(proto.Message):
        r"""The region to search.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            circle (google.maps.places_v1.types.Circle):
                A circle defined by center point and radius.

                This field is a member of `oneof`_ ``type``.
        """

        circle: geometry.Circle = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="type",
            message=geometry.Circle,
        )

    language_code: str = proto.Field(
        proto.STRING,
        number=1,
    )
    region_code: str = proto.Field(
        proto.STRING,
        number=2,
    )
    included_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    excluded_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    included_primary_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    excluded_primary_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    max_result_count: int = proto.Field(
        proto.INT32,
        number=7,
    )
    location_restriction: LocationRestriction = proto.Field(
        proto.MESSAGE,
        number=8,
        message=LocationRestriction,
    )
    rank_preference: RankPreference = proto.Field(
        proto.ENUM,
        number=9,
        enum=RankPreference,
    )
    routing_parameters: "RoutingParameters" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="RoutingParameters",
    )
    include_future_opening_businesses: bool = proto.Field(
        proto.BOOL,
        number=15,
    )


class SearchNearbyResponse(proto.Message):
    r"""Response proto for Search Nearby.

    Attributes:
        places (MutableSequence[google.maps.places_v1.types.Place]):
            A list of places that meets user's
            requirements like places types, number of places
            and specific location restriction.
        routing_summaries (MutableSequence[google.maps.places_v1.types.RoutingSummary]):
            A list of routing summaries where each entry associates to
            the corresponding place in the same index in the ``places``
            field. If the routing summary is not available for one of
            the places, it will contain an empty entry. This list should
            have as many entries as the list of places if requested.
    """

    places: MutableSequence[gmp_place.Place] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gmp_place.Place,
    )
    routing_summaries: MutableSequence[routing_summary.RoutingSummary] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message=routing_summary.RoutingSummary,
        )
    )


class SearchTextRequest(proto.Message):
    r"""Request proto for SearchText.

    Attributes:
        text_query (str):
            Required. The text query for textual search.
        language_code (str):
            Place details will be displayed with the
            preferred language if available. If the language
            code is unspecified or unrecognized, place
            details of any language may be returned, with a
            preference for English if such details exist.

            Current list of supported languages:

            https://developers.google.com/maps/faq#languagesupport.
        region_code (str):
            The Unicode country/region code (CLDR) of the location where
            the request is coming from. This parameter is used to
            display the place details, like region-specific place name,
            if available. The parameter can affect results based on
            applicable law.

            For more information, see
            https://www.unicode.org/cldr/charts/latest/supplemental/territory_language_information.html.

            Note that 3-digit region codes are not currently supported.
        rank_preference (google.maps.places_v1.types.SearchTextRequest.RankPreference):
            How results will be ranked in the response.
        included_type (str):
            The requested place type. Full list of types
            supported:
            https://developers.google.com/maps/documentation/places/web-service/place-types.
            Only support one included type.
        open_now (bool):
            Used to restrict the search to places that
            are currently open.  The default is false.
        min_rating (float):
            Filter out results whose average user rating is strictly
            less than this limit. A valid value must be a float between
            0 and 5 (inclusively) at a 0.5 cadence i.e. [0, 0.5, 1.0,
            ... , 5.0] inclusively. The input rating will round up to
            the nearest 0.5(ceiling). For instance, a rating of 0.6 will
            eliminate all results with a less than 1.0 rating.
        max_result_count (int):
            Maximum number of results to return. It must be between 1
            and 20, inclusively. The default is 20. If the number is
            unset, it falls back to the upper limit. If the number is
            set to negative or exceeds the upper limit, an
            INVALID_ARGUMENT error is returned.
        price_levels (MutableSequence[google.maps.places_v1.types.PriceLevel]):
            Used to restrict the search to places that
            are marked as certain price levels. Users can
            choose any combinations of price levels. Default
            to select all price levels.
        strict_type_filtering (bool):
            Used to set strict type filtering for included_type. If set
            to true, only results of the same type will be returned.
            Default to false.
        location_bias (google.maps.places_v1.types.SearchTextRequest.LocationBias):
            The region to search. This location serves as a bias which
            means results around given location might be returned.
            Cannot be set along with location_restriction.
        location_restriction (google.maps.places_v1.types.SearchTextRequest.LocationRestriction):
            The region to search. This location serves as a restriction
            which means results outside given location will not be
            returned. Cannot be set along with location_bias.
        ev_options (google.maps.places_v1.types.SearchTextRequest.EVOptions):
            Optional. Set the searchable EV options of a
            place search request.
        routing_parameters (google.maps.places_v1.types.RoutingParameters):
            Optional. Additional parameters for routing
            to results.
        search_along_route_parameters (google.maps.places_v1.types.SearchTextRequest.SearchAlongRouteParameters):
            Optional. Additional parameters proto for
            searching along a route.
        include_pure_service_area_businesses (bool):
            Optional. Include pure service area businesses if the field
            is set to true. Pure service area business is a business
            that visits or delivers to customers directly but does not
            serve customers at their business address. For example,
            businesses like cleaning services or plumbers. Those
            businesses do not have a physical address or location on
            Google Maps. Places will not return fields including
            ``location``, ``plus_code``, and other location related
            fields for these businesses.
        include_future_opening_businesses (bool):
            Optional. If true, include businesses that
            are not yet open but will open in the future.
    """

    class RankPreference(proto.Enum):
        r"""How results will be ranked in the response.

        Values:
            RANK_PREFERENCE_UNSPECIFIED (0):
                For a categorical query such as "Restaurants
                in New York City", RELEVANCE is the default. For
                non-categorical queries such as "Mountain View,
                CA" we recommend that you leave rankPreference
                unset.
            DISTANCE (1):
                Ranks results by distance.
            RELEVANCE (2):
                Ranks results by relevance. Sort order
                determined by normal ranking stack.
        """

        RANK_PREFERENCE_UNSPECIFIED = 0
        DISTANCE = 1
        RELEVANCE = 2

    class LocationBias(proto.Message):
        r"""The region to search. This location serves as a bias which
        means results around given location might be returned.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            rectangle (google.geo.type.types.Viewport):
                A rectangle box defined by northeast and southwest corner.
                ``rectangle.high()`` must be the northeast point of the
                rectangle viewport. ``rectangle.low()`` must be the
                southwest point of the rectangle viewport.
                ``rectangle.low().latitude()`` cannot be greater than
                ``rectangle.high().latitude()``. This will result in an
                empty latitude range. A rectangle viewport cannot be wider
                than 180 degrees.

                This field is a member of `oneof`_ ``type``.
            circle (google.maps.places_v1.types.Circle):
                A circle defined by center point and radius.

                This field is a member of `oneof`_ ``type``.
        """

        rectangle: viewport.Viewport = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="type",
            message=viewport.Viewport,
        )
        circle: geometry.Circle = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="type",
            message=geometry.Circle,
        )

    class LocationRestriction(proto.Message):
        r"""The region to search. This location serves as a restriction
        which means results outside given location will not be returned.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            rectangle (google.geo.type.types.Viewport):
                A rectangle box defined by northeast and southwest corner.
                ``rectangle.high()`` must be the northeast point of the
                rectangle viewport. ``rectangle.low()`` must be the
                southwest point of the rectangle viewport.
                ``rectangle.low().latitude()`` cannot be greater than
                ``rectangle.high().latitude()``. This will result in an
                empty latitude range. A rectangle viewport cannot be wider
                than 180 degrees.

                This field is a member of `oneof`_ ``type``.
        """

        rectangle: viewport.Viewport = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="type",
            message=viewport.Viewport,
        )

    class EVOptions(proto.Message):
        r"""Searchable EV options of a place search request.

        Attributes:
            minimum_charging_rate_kw (float):
                Optional. Minimum required charging rate in
                kilowatts. A place with a charging rate less
                than the specified rate is filtered out.
            connector_types (MutableSequence[google.maps.places_v1.types.EVConnectorType]):
                Optional. The list of preferred EV connector
                types. A place that does not support any of the
                listed connector types is filtered out.
        """

        minimum_charging_rate_kw: float = proto.Field(
            proto.DOUBLE,
            number=1,
        )
        connector_types: MutableSequence[ev_charging.EVConnectorType] = (
            proto.RepeatedField(
                proto.ENUM,
                number=2,
                enum=ev_charging.EVConnectorType,
            )
        )

    class SearchAlongRouteParameters(proto.Message):
        r"""Specifies a precalculated polyline from the `Routes
        API <https://developers.google.com/maps/documentation/routes>`__
        defining the route to search. Searching along a route is similar to
        using the ``locationBias`` or ``locationRestriction`` request option
        to bias the search results. However, while the ``locationBias`` and
        ``locationRestriction`` options let you specify a region to bias the
        search results, this option lets you bias the results along a trip
        route.

        Results are not guaranteed to be along the route provided, but
        rather are ranked within the search area defined by the polyline
        and, optionally, by the ``locationBias`` or ``locationRestriction``
        based on minimal detour times from origin to destination. The
        results might be along an alternate route, especially if the
        provided polyline does not define an optimal route from origin to
        destination.

        Attributes:
            polyline (google.maps.places_v1.types.Polyline):
                Required. The route polyline.
        """

        polyline: gmp_polyline.Polyline = proto.Field(
            proto.MESSAGE,
            number=1,
            message=gmp_polyline.Polyline,
        )

    text_query: str = proto.Field(
        proto.STRING,
        number=1,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=2,
    )
    region_code: str = proto.Field(
        proto.STRING,
        number=3,
    )
    rank_preference: RankPreference = proto.Field(
        proto.ENUM,
        number=4,
        enum=RankPreference,
    )
    included_type: str = proto.Field(
        proto.STRING,
        number=6,
    )
    open_now: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    min_rating: float = proto.Field(
        proto.DOUBLE,
        number=9,
    )
    max_result_count: int = proto.Field(
        proto.INT32,
        number=10,
    )
    price_levels: MutableSequence[gmp_place.PriceLevel] = proto.RepeatedField(
        proto.ENUM,
        number=11,
        enum=gmp_place.PriceLevel,
    )
    strict_type_filtering: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    location_bias: LocationBias = proto.Field(
        proto.MESSAGE,
        number=13,
        message=LocationBias,
    )
    location_restriction: LocationRestriction = proto.Field(
        proto.MESSAGE,
        number=14,
        message=LocationRestriction,
    )
    ev_options: EVOptions = proto.Field(
        proto.MESSAGE,
        number=15,
        message=EVOptions,
    )
    routing_parameters: "RoutingParameters" = proto.Field(
        proto.MESSAGE,
        number=16,
        message="RoutingParameters",
    )
    search_along_route_parameters: SearchAlongRouteParameters = proto.Field(
        proto.MESSAGE,
        number=17,
        message=SearchAlongRouteParameters,
    )
    include_pure_service_area_businesses: bool = proto.Field(
        proto.BOOL,
        number=20,
    )
    include_future_opening_businesses: bool = proto.Field(
        proto.BOOL,
        number=21,
    )


class SearchTextResponse(proto.Message):
    r"""Response proto for SearchText.

    Attributes:
        places (MutableSequence[google.maps.places_v1.types.Place]):
            A list of places that meet the user's text
            search criteria.
        routing_summaries (MutableSequence[google.maps.places_v1.types.RoutingSummary]):
            A list of routing summaries where each entry associates to
            the corresponding place in the same index in the ``places``
            field. If the routing summary is not available for one of
            the places, it will contain an empty entry. This list will
            have as many entries as the list of places if requested.
        contextual_contents (MutableSequence[google.maps.places_v1.types.ContextualContent]):
            Experimental: See
            https://developers.google.com/maps/documentation/places/web-service/experimental/places-generative
            for more details.

            A list of contextual contents where each entry associates to
            the corresponding place in the same index in the places
            field. The contents that are relevant to the ``text_query``
            in the request are preferred. If the contextual content is
            not available for one of the places, it will return
            non-contextual content. It will be empty only when the
            content is unavailable for this place. This list will have
            as many entries as the list of places if requested.
    """

    places: MutableSequence[gmp_place.Place] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gmp_place.Place,
    )
    routing_summaries: MutableSequence[routing_summary.RoutingSummary] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message=routing_summary.RoutingSummary,
        )
    )
    contextual_contents: MutableSequence[contextual_content.ContextualContent] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message=contextual_content.ContextualContent,
        )
    )


class GetPhotoMediaRequest(proto.Message):
    r"""Request for fetching a photo of a place using a photo
    resource name.

    Attributes:
        name (str):
            Required. The resource name of a photo media in the format:
            ``places/{place_id}/photos/{photo_reference}/media``.

            The resource name of a photo as returned in a Place object's
            ``photos.name`` field comes with the format
            ``places/{place_id}/photos/{photo_reference}``. You need to
            append ``/media`` at the end of the photo resource to get
            the photo media resource name.
        max_width_px (int):
            Optional. Specifies the maximum desired width, in pixels, of
            the image. If the image is smaller than the values
            specified, the original image will be returned. If the image
            is larger in either dimension, it will be scaled to match
            the smaller of the two dimensions, restricted to its
            original aspect ratio. Both the max_height_px and
            max_width_px properties accept an integer between 1 and
            4800, inclusively. If the value is not within the allowed
            range, an INVALID_ARGUMENT error will be returned.

            At least one of max_height_px or max_width_px needs to be
            specified. If neither max_height_px nor max_width_px is
            specified, an INVALID_ARGUMENT error will be returned.
        max_height_px (int):
            Optional. Specifies the maximum desired height, in pixels,
            of the image. If the image is smaller than the values
            specified, the original image will be returned. If the image
            is larger in either dimension, it will be scaled to match
            the smaller of the two dimensions, restricted to its
            original aspect ratio. Both the max_height_px and
            max_width_px properties accept an integer between 1 and
            4800, inclusively. If the value is not within the allowed
            range, an INVALID_ARGUMENT error will be returned.

            At least one of max_height_px or max_width_px needs to be
            specified. If neither max_height_px nor max_width_px is
            specified, an INVALID_ARGUMENT error will be returned.
        skip_http_redirect (bool):
            Optional. If set, skip the default HTTP
            redirect behavior and render a text format (for
            example, in JSON format for HTTP use case)
            response. If not set, an HTTP redirect will be
            issued to redirect the call to the image media.
            This option is ignored for non-HTTP requests.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    max_width_px: int = proto.Field(
        proto.INT32,
        number=2,
    )
    max_height_px: int = proto.Field(
        proto.INT32,
        number=3,
    )
    skip_http_redirect: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class PhotoMedia(proto.Message):
    r"""A photo media from Places API.

    Attributes:
        name (str):
            The resource name of a photo media in the format:
            ``places/{place_id}/photos/{photo_reference}/media``.
        photo_uri (str):
            A short-lived uri that can be used to render
            the photo.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    photo_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetPlaceRequest(proto.Message):
    r"""Request for fetching a Place based on its resource name, which is a
    string in the ``places/{place_id}`` format.

    Attributes:
        name (str):
            Required. The resource name of a place, in the
            ``places/{place_id}`` format.
        language_code (str):
            Optional. Place details will be displayed
            with the preferred language if available.

            Current list of supported languages:

            https://developers.google.com/maps/faq#languagesupport.
        region_code (str):
            Optional. The Unicode country/region code (CLDR) of the
            location where the request is coming from. This parameter is
            used to display the place details, like region-specific
            place name, if available. The parameter can affect results
            based on applicable law. For more information, see
            https://www.unicode.org/cldr/charts/latest/supplemental/territory_language_information.html.

            Note that 3-digit region codes are not currently supported.
        session_token (str):
            Optional. A string which identifies an Autocomplete session
            for billing purposes. Must be a URL and filename safe base64
            string with at most 36 ASCII characters in length. Otherwise
            an INVALID_ARGUMENT error is returned.

            The session begins when the user starts typing a query, and
            concludes when they select a place and a call to Place
            Details or Address Validation is made. Each session can have
            multiple queries, followed by one Place Details or Address
            Validation request. The credentials used for each request
            within a session must belong to the same Google Cloud
            Console project. Once a session has concluded, the token is
            no longer valid; your app must generate a fresh token for
            each session. If the ``session_token`` parameter is omitted,
            or if you reuse a session token, the session is charged as
            if no session token was provided (each request is billed
            separately).

            We recommend the following guidelines:

            - Use session tokens for all Place Autocomplete calls.
            - Generate a fresh token for each session. Using a version 4
              UUID is recommended.
            - Ensure that the credentials used for all Place
              Autocomplete, Place Details, and Address Validation
              requests within a session belong to the same Cloud Console
              project.
            - Be sure to pass a unique session token for each new
              session. Using the same token for more than one session
              will result in each request being billed individually.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=2,
    )
    region_code: str = proto.Field(
        proto.STRING,
        number=3,
    )
    session_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class AutocompletePlacesRequest(proto.Message):
    r"""Request proto for AutocompletePlaces.

    Attributes:
        input (str):
            Required. The text string on which to search.
        location_bias (google.maps.places_v1.types.AutocompletePlacesRequest.LocationBias):
            Optional. Bias results to a specified location.

            At most one of ``location_bias`` or ``location_restriction``
            should be set. If neither are set, the results will be
            biased by IP address, meaning the IP address will be mapped
            to an imprecise location and used as a biasing signal.
        location_restriction (google.maps.places_v1.types.AutocompletePlacesRequest.LocationRestriction):
            Optional. Restrict results to a specified location.

            At most one of ``location_bias`` or ``location_restriction``
            should be set. If neither are set, the results will be
            biased by IP address, meaning the IP address will be mapped
            to an imprecise location and used as a biasing signal.
        included_primary_types (MutableSequence[str]):
            Optional. Included primary Place type (for example,
            "restaurant" or "gas_station") in Place Types
            (https://developers.google.com/maps/documentation/places/web-service/place-types),
            or only ``(regions)``, or only ``(cities)``. A Place is only
            returned if its primary type is included in this list. Up to
            5 values can be specified. If no types are specified, all
            Place types are returned.
        included_region_codes (MutableSequence[str]):
            Optional. Only include results in the specified regions,
            specified as up to 15 CLDR two-character region codes. An
            empty set will not restrict the results. If both
            ``location_restriction`` and ``included_region_codes`` are
            set, the results will be located in the area of
            intersection.
        language_code (str):
            Optional. The language in which to return results. Defaults
            to en-US. The results may be in mixed languages if the
            language used in ``input`` is different from
            ``language_code`` or if the returned Place does not have a
            translation from the local language to ``language_code``.
        region_code (str):
            Optional. The region code, specified as a CLDR two-character
            region code. This affects address formatting, result
            ranking, and may influence what results are returned. This
            does not restrict results to the specified region. To
            restrict results to a region, use
            ``region_code_restriction``.
        origin (google.type.latlng_pb2.LatLng):
            Optional. The origin point from which to calculate geodesic
            distance to the destination (returned as
            ``distance_meters``). If this value is omitted, geodesic
            distance will not be returned.
        input_offset (int):
            Optional. A zero-based Unicode character offset of ``input``
            indicating the cursor position in ``input``. The cursor
            position may influence what predictions are returned.

            If empty, defaults to the length of ``input``.
        include_query_predictions (bool):
            Optional. If true, the response will include
            both Place and query predictions. Otherwise the
            response will only return Place predictions.
        session_token (str):
            Optional. A string which identifies an Autocomplete session
            for billing purposes. Must be a URL and filename safe base64
            string with at most 36 ASCII characters in length. Otherwise
            an INVALID_ARGUMENT error is returned.

            The session begins when the user starts typing a query, and
            concludes when they select a place and a call to Place
            Details or Address Validation is made. Each session can have
            multiple queries, followed by one Place Details or Address
            Validation request. The credentials used for each request
            within a session must belong to the same Google Cloud
            Console project. Once a session has concluded, the token is
            no longer valid; your app must generate a fresh token for
            each session. If the ``session_token`` parameter is omitted,
            or if you reuse a session token, the session is charged as
            if no session token was provided (each request is billed
            separately).

            We recommend the following guidelines:

            - Use session tokens for all Place Autocomplete calls.
            - Generate a fresh token for each session. Using a version 4
              UUID is recommended.
            - Ensure that the credentials used for all Place
              Autocomplete, Place Details, and Address Validation
              requests within a session belong to the same Cloud Console
              project.
            - Be sure to pass a unique session token for each new
              session. Using the same token for more than one session
              will result in each request being billed individually.
        include_pure_service_area_businesses (bool):
            Optional. Include pure service area businesses if the field
            is set to true. Pure service area business is a business
            that visits or delivers to customers directly but does not
            serve customers at their business address. For example,
            businesses like cleaning services or plumbers. Those
            businesses do not have a physical address or location on
            Google Maps. Places will not return fields including
            ``location``, ``plus_code``, and other location related
            fields for these businesses.
        include_future_opening_businesses (bool):
            Optional. If true, include businesses that
            are not yet open but will open in the future.
    """

    class LocationBias(proto.Message):
        r"""The region to search. The results may be biased around the
        specified region.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            rectangle (google.geo.type.types.Viewport):
                A viewport defined by a northeast and a
                southwest corner.

                This field is a member of `oneof`_ ``type``.
            circle (google.maps.places_v1.types.Circle):
                A circle defined by a center point and
                radius.

                This field is a member of `oneof`_ ``type``.
        """

        rectangle: viewport.Viewport = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="type",
            message=viewport.Viewport,
        )
        circle: geometry.Circle = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="type",
            message=geometry.Circle,
        )

    class LocationRestriction(proto.Message):
        r"""The region to search. The results will be restricted to the
        specified region.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            rectangle (google.geo.type.types.Viewport):
                A viewport defined by a northeast and a
                southwest corner.

                This field is a member of `oneof`_ ``type``.
            circle (google.maps.places_v1.types.Circle):
                A circle defined by a center point and
                radius.

                This field is a member of `oneof`_ ``type``.
        """

        rectangle: viewport.Viewport = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="type",
            message=viewport.Viewport,
        )
        circle: geometry.Circle = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="type",
            message=geometry.Circle,
        )

    input: str = proto.Field(
        proto.STRING,
        number=1,
    )
    location_bias: LocationBias = proto.Field(
        proto.MESSAGE,
        number=2,
        message=LocationBias,
    )
    location_restriction: LocationRestriction = proto.Field(
        proto.MESSAGE,
        number=3,
        message=LocationRestriction,
    )
    included_primary_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    included_region_codes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=6,
    )
    region_code: str = proto.Field(
        proto.STRING,
        number=7,
    )
    origin: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=8,
        message=latlng_pb2.LatLng,
    )
    input_offset: int = proto.Field(
        proto.INT32,
        number=9,
    )
    include_query_predictions: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    session_token: str = proto.Field(
        proto.STRING,
        number=11,
    )
    include_pure_service_area_businesses: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    include_future_opening_businesses: bool = proto.Field(
        proto.BOOL,
        number=13,
    )


class AutocompletePlacesResponse(proto.Message):
    r"""Response proto for AutocompletePlaces.

    Attributes:
        suggestions (MutableSequence[google.maps.places_v1.types.AutocompletePlacesResponse.Suggestion]):
            Contains a list of suggestions, ordered in
            descending order of relevance.
    """

    class Suggestion(proto.Message):
        r"""An Autocomplete suggestion result.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            place_prediction (google.maps.places_v1.types.AutocompletePlacesResponse.Suggestion.PlacePrediction):
                A prediction for a Place.

                This field is a member of `oneof`_ ``kind``.
            query_prediction (google.maps.places_v1.types.AutocompletePlacesResponse.Suggestion.QueryPrediction):
                A prediction for a query.

                This field is a member of `oneof`_ ``kind``.
        """

        class StringRange(proto.Message):
            r"""Identifies a substring within a given text.

            Attributes:
                start_offset (int):
                    Zero-based offset of the first Unicode
                    character of the string (inclusive).
                end_offset (int):
                    Zero-based offset of the last Unicode
                    character (exclusive).
            """

            start_offset: int = proto.Field(
                proto.INT32,
                number=1,
            )
            end_offset: int = proto.Field(
                proto.INT32,
                number=2,
            )

        class FormattableText(proto.Message):
            r"""Text representing a Place or query prediction. The text may
            be used as is or formatted.

            Attributes:
                text (str):
                    Text that may be used as is or formatted with ``matches``.
                matches (MutableSequence[google.maps.places_v1.types.AutocompletePlacesResponse.Suggestion.StringRange]):
                    A list of string ranges identifying where the input request
                    matched in ``text``. The ranges can be used to format
                    specific parts of ``text``. The substrings may not be exact
                    matches of ``input`` if the matching was determined by
                    criteria other than string matching (for example, spell
                    corrections or transliterations).

                    These values are Unicode character offsets of ``text``. The
                    ranges are guaranteed to be ordered in increasing offset
                    values.
            """

            text: str = proto.Field(
                proto.STRING,
                number=1,
            )
            matches: MutableSequence[
                "AutocompletePlacesResponse.Suggestion.StringRange"
            ] = proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="AutocompletePlacesResponse.Suggestion.StringRange",
            )

        class StructuredFormat(proto.Message):
            r"""Contains a breakdown of a Place or query prediction into main
            text and secondary text.

            For Place predictions, the main text contains the specific name
            of the Place. For query predictions, the main text contains the
            query.

            The secondary text contains additional disambiguating features
            (such as a city or region) to further identify the Place or
            refine the query.

            Attributes:
                main_text (google.maps.places_v1.types.AutocompletePlacesResponse.Suggestion.FormattableText):
                    Represents the name of the Place or query.
                secondary_text (google.maps.places_v1.types.AutocompletePlacesResponse.Suggestion.FormattableText):
                    Represents additional disambiguating features
                    (such as a city or region) to further identify
                    the Place or refine the query.
            """

            main_text: "AutocompletePlacesResponse.Suggestion.FormattableText" = (
                proto.Field(
                    proto.MESSAGE,
                    number=1,
                    message="AutocompletePlacesResponse.Suggestion.FormattableText",
                )
            )
            secondary_text: "AutocompletePlacesResponse.Suggestion.FormattableText" = (
                proto.Field(
                    proto.MESSAGE,
                    number=2,
                    message="AutocompletePlacesResponse.Suggestion.FormattableText",
                )
            )

        class PlacePrediction(proto.Message):
            r"""Prediction results for a Place Autocomplete prediction.

            Attributes:
                place (str):
                    The resource name of the suggested Place.
                    This name can be used in other APIs that accept
                    Place names.
                place_id (str):
                    The unique identifier of the suggested Place.
                    This identifier can be used in other APIs that
                    accept Place IDs.
                text (google.maps.places_v1.types.AutocompletePlacesResponse.Suggestion.FormattableText):
                    Contains the human-readable name for the returned result.
                    For establishment results, this is usually the business name
                    and address.

                    ``text`` is recommended for developers who wish to show a
                    single UI element. Developers who wish to show two separate,
                    but related, UI elements may want to use
                    ``structured_format`` instead. They are two different ways
                    to represent a Place prediction. Users should not try to
                    parse ``structured_format`` into ``text`` or vice versa.

                    This text may be different from the ``display_name``
                    returned by GetPlace.

                    May be in mixed languages if the request ``input`` and
                    ``language_code`` are in different languages or if the Place
                    does not have a translation from the local language to
                    ``language_code``.
                structured_format (google.maps.places_v1.types.AutocompletePlacesResponse.Suggestion.StructuredFormat):
                    A breakdown of the Place prediction into main text
                    containing the name of the Place and secondary text
                    containing additional disambiguating features (such as a
                    city or region).

                    ``structured_format`` is recommended for developers who wish
                    to show two separate, but related, UI elements. Developers
                    who wish to show a single UI element may want to use
                    ``text`` instead. They are two different ways to represent a
                    Place prediction. Users should not try to parse
                    ``structured_format`` into ``text`` or vice versa.
                types (MutableSequence[str]):
                    List of types that apply to this Place from
                    Table A or Table B in
                    https://developers.google.com/maps/documentation/places/web-service/place-types.

                    A type is a categorization of a Place. Places
                    with shared types will share similar
                    characteristics.
                distance_meters (int):
                    The length of the geodesic in meters from ``origin`` if
                    ``origin`` is specified. Certain predictions such as routes
                    may not populate this field.
            """

            place: str = proto.Field(
                proto.STRING,
                number=1,
            )
            place_id: str = proto.Field(
                proto.STRING,
                number=2,
            )
            text: "AutocompletePlacesResponse.Suggestion.FormattableText" = proto.Field(
                proto.MESSAGE,
                number=3,
                message="AutocompletePlacesResponse.Suggestion.FormattableText",
            )
            structured_format: "AutocompletePlacesResponse.Suggestion.StructuredFormat" = proto.Field(
                proto.MESSAGE,
                number=4,
                message="AutocompletePlacesResponse.Suggestion.StructuredFormat",
            )
            types: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=5,
            )
            distance_meters: int = proto.Field(
                proto.INT32,
                number=6,
            )

        class QueryPrediction(proto.Message):
            r"""Prediction results for a Query Autocomplete prediction.

            Attributes:
                text (google.maps.places_v1.types.AutocompletePlacesResponse.Suggestion.FormattableText):
                    The predicted text. This text does not represent a Place,
                    but rather a text query that could be used in a search
                    endpoint (for example, Text Search).

                    ``text`` is recommended for developers who wish to show a
                    single UI element. Developers who wish to show two separate,
                    but related, UI elements may want to use
                    ``structured_format`` instead. They are two different ways
                    to represent a query prediction. Users should not try to
                    parse ``structured_format`` into ``text`` or vice versa.

                    May be in mixed languages if the request ``input`` and
                    ``language_code`` are in different languages or if part of
                    the query does not have a translation from the local
                    language to ``language_code``.
                structured_format (google.maps.places_v1.types.AutocompletePlacesResponse.Suggestion.StructuredFormat):
                    A breakdown of the query prediction into main text
                    containing the query and secondary text containing
                    additional disambiguating features (such as a city or
                    region).

                    ``structured_format`` is recommended for developers who wish
                    to show two separate, but related, UI elements. Developers
                    who wish to show a single UI element may want to use
                    ``text`` instead. They are two different ways to represent a
                    query prediction. Users should not try to parse
                    ``structured_format`` into ``text`` or vice versa.
            """

            text: "AutocompletePlacesResponse.Suggestion.FormattableText" = proto.Field(
                proto.MESSAGE,
                number=1,
                message="AutocompletePlacesResponse.Suggestion.FormattableText",
            )
            structured_format: "AutocompletePlacesResponse.Suggestion.StructuredFormat" = proto.Field(
                proto.MESSAGE,
                number=2,
                message="AutocompletePlacesResponse.Suggestion.StructuredFormat",
            )

        place_prediction: "AutocompletePlacesResponse.Suggestion.PlacePrediction" = (
            proto.Field(
                proto.MESSAGE,
                number=1,
                oneof="kind",
                message="AutocompletePlacesResponse.Suggestion.PlacePrediction",
            )
        )
        query_prediction: "AutocompletePlacesResponse.Suggestion.QueryPrediction" = (
            proto.Field(
                proto.MESSAGE,
                number=2,
                oneof="kind",
                message="AutocompletePlacesResponse.Suggestion.QueryPrediction",
            )
        )

    suggestions: MutableSequence[Suggestion] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=Suggestion,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
