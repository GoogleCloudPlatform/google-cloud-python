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

__protobuf__ = proto.module(
    package="google.maps.areainsights.v1",
    manifest={
        "Insight",
        "OperatingStatus",
        "PriceLevel",
        "ComputeInsightsRequest",
        "ComputeInsightsResponse",
        "PlaceInsight",
        "Filter",
        "LocationFilter",
        "TypeFilter",
        "RatingFilter",
    },
)


class Insight(proto.Enum):
    r"""Supported insights.

    Values:
        INSIGHT_UNSPECIFIED (0):
            Not Specified.
        INSIGHT_COUNT (1):
            Count insight.

            When this insight is specified ComputeInsights returns the
            number of places that match the specified filter criteria.

            Example request:

            ::

               {
                 "insights": ["INSIGHT_COUNT"],
                 "filter": {
                   "locationFilter": {
                     "region": {
                       "place": "places/ChIJPV4oX_65j4ARVW8IJ6IJUYs"
                     }
                   },
                   "typeFilter": {
                     "includedTypes": ["restaurant"]
                   },
                   "operatingStatus": ["OPERATING_STATUS_OPERATIONAL"],
                   "priceLevels": [
                     "PRICE_LEVEL_FREE",
                     "PRICE_LEVEL_INEXPENSIVE"
                   ],
                   "ratingFilter": {
                     "minRating": 4.0
                   }
                 }
               }

            Example response:

            ::

               {
                 "count": 1234
               }
        INSIGHT_PLACES (2):
            Return Places

            When this insight is specified ComputeInsights returns
            places IDs that match the specified filter criteria.

            Example request:

            ::

               {
                 "insights": ["INSIGHT_PLACES"],
                 "filter": {
                   "locationFilter": {
                     "region": {
                       "place": "places/ChIJPV4oX_65j4ARVW8IJ6IJUYs"
                     }
                   },
                   "typeFilter": {
                     "includedTypes": ["restaurant"]
                   },
                   "operatingStatus": ["OPERATING_STATUS_OPERATIONAL"],
                   "priceLevels": [
                     "PRICE_LEVEL_FREE",
                     "PRICE_LEVEL_INEXPENSIVE"
                   ],
                   "ratingFilter": {
                     "minRating": 4.0
                   }
                 }
               }

            Example response:

            ::

               {
                 "placeInsights": [
                   {"place": "places/ABC"},
                   {"place": "places/PQR"},
                   {"place": "places/XYZ"}
                 ]
               }
    """

    INSIGHT_UNSPECIFIED = 0
    INSIGHT_COUNT = 1
    INSIGHT_PLACES = 2


class OperatingStatus(proto.Enum):
    r"""Operating status of the place.

    Values:
        OPERATING_STATUS_UNSPECIFIED (0):
            Not specified. This value should not be used.
        OPERATING_STATUS_OPERATIONAL (1):
            The place is operational and its open during
            its defined hours.
        OPERATING_STATUS_PERMANENTLY_CLOSED (3):
            The Place is no longer in business.
        OPERATING_STATUS_TEMPORARILY_CLOSED (4):
            The place is temporarily closed and expected
            to reopen in the future.
    """

    OPERATING_STATUS_UNSPECIFIED = 0
    OPERATING_STATUS_OPERATIONAL = 1
    OPERATING_STATUS_PERMANENTLY_CLOSED = 3
    OPERATING_STATUS_TEMPORARILY_CLOSED = 4


class PriceLevel(proto.Enum):
    r"""Price level of the place.

    Values:
        PRICE_LEVEL_UNSPECIFIED (0):
            Not specified. This value should not be used.
        PRICE_LEVEL_FREE (1):
            Place provides free services.
        PRICE_LEVEL_INEXPENSIVE (2):
            Place provides inexpensive services.
        PRICE_LEVEL_MODERATE (3):
            Place provides moderately priced services.
        PRICE_LEVEL_EXPENSIVE (4):
            Place provides expensive services.
        PRICE_LEVEL_VERY_EXPENSIVE (5):
            Place provides very expensive services.
    """

    PRICE_LEVEL_UNSPECIFIED = 0
    PRICE_LEVEL_FREE = 1
    PRICE_LEVEL_INEXPENSIVE = 2
    PRICE_LEVEL_MODERATE = 3
    PRICE_LEVEL_EXPENSIVE = 4
    PRICE_LEVEL_VERY_EXPENSIVE = 5


class ComputeInsightsRequest(proto.Message):
    r"""Request for the ComputeInsights RPC.

    Attributes:
        insights (MutableSequence[google.maps.areainsights_v1.types.Insight]):
            Required. Insights to compute. Currently only INSIGHT_COUNT
            and INSIGHT_PLACES are supported.
        filter (google.maps.areainsights_v1.types.Filter):
            Required. Insight filter.
    """

    insights: MutableSequence["Insight"] = proto.RepeatedField(
        proto.ENUM,
        number=4,
        enum="Insight",
    )
    filter: "Filter" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="Filter",
    )


class ComputeInsightsResponse(proto.Message):
    r"""Response for the ComputeInsights RPC.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        count (int):
            Result for Insights.INSIGHT_COUNT.

            This field is a member of `oneof`_ ``_count``.
        place_insights (MutableSequence[google.maps.areainsights_v1.types.PlaceInsight]):
            Result for Insights.INSIGHT_PLACES.
    """

    count: int = proto.Field(
        proto.INT64,
        number=1,
        optional=True,
    )
    place_insights: MutableSequence["PlaceInsight"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="PlaceInsight",
    )


class PlaceInsight(proto.Message):
    r"""Holds information about a place

    Attributes:
        place (str):
            The unique identifier of the place. This resource name can
            be used to retrieve details about the place using the
            `Places
            API <https://developers.google.com/maps/documentation/places/web-service/reference/rest/v1/places/get>`__.
    """

    place: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Filter(proto.Message):
    r"""Filters for the ComputeInsights RPC.

    Attributes:
        location_filter (google.maps.areainsights_v1.types.LocationFilter):
            Required. Restricts results to places which
            are located in the area specified by location
            filters.
        type_filter (google.maps.areainsights_v1.types.TypeFilter):
            Required. Place type filters.
        operating_status (MutableSequence[google.maps.areainsights_v1.types.OperatingStatus]):
            Optional. Restricts results to places whose operating status
            is included on this list. If operating_status is not set,
            OPERATING_STATUS_OPERATIONAL is used as default.
        price_levels (MutableSequence[google.maps.areainsights_v1.types.PriceLevel]):
            Optional. Restricts results to places whose price level is
            included on this list. If ``price_levels`` is not set, all
            price levels are included in the results.
        rating_filter (google.maps.areainsights_v1.types.RatingFilter):
            Optional. Restricts results to places whose average user
            ratings are in the range specified by rating_filter. If
            rating_filter is not set, all ratings are included in the
            result.
    """

    location_filter: "LocationFilter" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="LocationFilter",
    )
    type_filter: "TypeFilter" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="TypeFilter",
    )
    operating_status: MutableSequence["OperatingStatus"] = proto.RepeatedField(
        proto.ENUM,
        number=3,
        enum="OperatingStatus",
    )
    price_levels: MutableSequence["PriceLevel"] = proto.RepeatedField(
        proto.ENUM,
        number=4,
        enum="PriceLevel",
    )
    rating_filter: "RatingFilter" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="RatingFilter",
    )


class LocationFilter(proto.Message):
    r"""Location filters.

    Specifies the area of interest for the insight.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        circle (google.maps.areainsights_v1.types.LocationFilter.Circle):
            Area as a circle.

            This field is a member of `oneof`_ ``area``.
        region (google.maps.areainsights_v1.types.LocationFilter.Region):
            Area as region.

            This field is a member of `oneof`_ ``area``.
        custom_area (google.maps.areainsights_v1.types.LocationFilter.CustomArea):
            Custom area specified by a polygon.

            This field is a member of `oneof`_ ``area``.
    """

    class Circle(proto.Message):
        r"""A circle is defined by a center point and radius in meters.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            lat_lng (google.type.latlng_pb2.LatLng):
                The latitude and longitude of the center of
                the circle.

                This field is a member of `oneof`_ ``center``.
            place (str):
                **Format:** Must be in the format ``places/PLACE_ID``, where
                ``PLACE_ID`` is the unique identifier of a place. For
                example: ``places/ChIJgUbEo8cfqokR5lP9_Wh_DaM``.

                This field is a member of `oneof`_ ``center``.
            radius (int):
                Optional. The radius of the circle in meters
        """

        lat_lng: latlng_pb2.LatLng = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="center",
            message=latlng_pb2.LatLng,
        )
        place: str = proto.Field(
            proto.STRING,
            number=2,
            oneof="center",
        )
        radius: int = proto.Field(
            proto.INT32,
            number=3,
        )

    class Region(proto.Message):
        r"""A region is a geographic boundary such as: cities, postal
        codes, counties, states, etc.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            place (str):
                The `place
                ID <https://developers.google.com/maps/documentation/places/web-service/place-id>`__
                of the geographic region. Not all region types are
                supported; see documentation for details.

                **Format:** Must be in the format ``places/PLACE_ID``, where
                ``PLACE_ID`` is the unique identifier of a place. For
                example: ``places/ChIJPV4oX_65j4ARVW8IJ6IJUYs``.

                This field is a member of `oneof`_ ``region``.
        """

        place: str = proto.Field(
            proto.STRING,
            number=1,
            oneof="region",
        )

    class CustomArea(proto.Message):
        r"""Custom Area.

        Attributes:
            polygon (google.maps.areainsights_v1.types.LocationFilter.CustomArea.Polygon):
                Required. The custom area represented as a
                polygon
        """

        class Polygon(proto.Message):
            r"""A polygon is represented by a series of connected coordinates
            in an counterclockwise ordered sequence. The coordinates form a
            closed loop and define a filled region. The first and last
            coordinates are equivalent, and they must contain identical
            values. The format is a simplified version of GeoJSON polygons
            (we only support one counterclockwise exterior ring).

            Attributes:
                coordinates (MutableSequence[google.type.latlng_pb2.LatLng]):
                    Optional. The coordinates that define the
                    polygon.
            """

            coordinates: MutableSequence[latlng_pb2.LatLng] = proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message=latlng_pb2.LatLng,
            )

        polygon: "LocationFilter.CustomArea.Polygon" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="LocationFilter.CustomArea.Polygon",
        )

    circle: Circle = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="area",
        message=Circle,
    )
    region: Region = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="area",
        message=Region,
    )
    custom_area: CustomArea = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="area",
        message=CustomArea,
    )


class TypeFilter(proto.Message):
    r"""Place type filters.

    Only Place types from `Table
    a <https://developers.google.com/maps/documentation/places/web-service/place-types#table-a>`__
    are supported.

    A place can only have a single primary type associated with it. For
    example, the primary type might be "mexican_restaurant" or
    "steak_house". Use included_primary_types and excluded_primary_types
    to filter the results on a place's primary type.

    A place can also have multiple type values associated with it. For
    example a restaurant might have the following types:
    "seafood_restaurant", "restaurant", "food", "point_of_interest",
    "establishment". Use included_types and excluded_types to filter the
    results on the list of types associated with a place.

    If a search is specified with multiple type restrictions, only
    places that satisfy all of the restrictions are returned. For
    example, if you specify {"included_types": ["restaurant"],
    "excluded_primary_types": ["steak_house"]}, the returned places
    provide "restaurant" related services but do not operate primarily
    as a "steak_house".

    If there are any conflicting types, i.e. a type appears in both
    included_types and excluded_types types or included_primary_types
    and excluded_primary_types, an INVALID_ARGUMENT error is returned.

    One of included_types or included_primary_types must be set.

    Attributes:
        included_types (MutableSequence[str]):
            Optional. Included Place types.
        excluded_types (MutableSequence[str]):
            Optional. Excluded Place types.
        included_primary_types (MutableSequence[str]):
            Optional. Included primary Place types.
        excluded_primary_types (MutableSequence[str]):
            Optional. Excluded primary Place types.
    """

    included_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    excluded_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    included_primary_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    excluded_primary_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


class RatingFilter(proto.Message):
    r"""Average user rating filters.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        min_rating (float):
            Optional. Restricts results to places whose average user
            rating is greater than or equal to min_rating. Values must
            be between 1.0 and 5.0.

            This field is a member of `oneof`_ ``_min_rating``.
        max_rating (float):
            Optional. Restricts results to places whose average user
            rating is strictly less than or equal to max_rating. Values
            must be between 1.0 and 5.0.

            This field is a member of `oneof`_ ``_max_rating``.
    """

    min_rating: float = proto.Field(
        proto.FLOAT,
        number=5,
        optional=True,
    )
    max_rating: float = proto.Field(
        proto.FLOAT,
        number=6,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
