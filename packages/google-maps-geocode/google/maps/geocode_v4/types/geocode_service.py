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
import google.type.localized_text_pb2 as localized_text_pb2  # type: ignore
import google.type.postal_address_pb2 as postal_address_pb2  # type: ignore
import proto  # type: ignore
from google.geo.type.types import viewport as ggt_viewport

__protobuf__ = proto.module(
    package="google.maps.geocode.v4",
    manifest={
        "GeocodeAddressRequest",
        "GeocodeLocationRequest",
        "GeocodePlaceRequest",
        "PlusCode",
        "GeocodeResult",
        "GeocodeAddressResponse",
        "GeocodeLocationResponse",
    },
)


class GeocodeAddressRequest(proto.Message):
    r"""Request message for GeocodeService.GeocodeAddress.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        address_query (str):
            The unstructured address to geocode.

            This field is a member of `oneof`_ ``address_input``.
        address (google.type.postal_address_pb2.PostalAddress):
            The structured address to geocode in postal
            address format.

            This field is a member of `oneof`_ ``address_input``.
        location_bias (google.maps.geocode_v4.types.GeocodeAddressRequest.LocationBias):
            Optional. The region to search. This location
            serves as a bias which means results around the
            given location are preferred.
        language_code (str):
            Optional. Language in which the results
            should be returned.
        region_code (str):
            Optional. Region code. The region code,
            specified as a ccTLD ("top-level domain")
            two-character value. The parameter affects
            results based on applicable law. This parameter
            will also influence, but not fully restrict,
            results from the service.
    """

    class LocationBias(proto.Message):
        r"""The region to search. This location serves as a bias which
        means results around the given location are preferred.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            rectangle (google.geo.type.types.Viewport):
                A rectangular box defined by northeast and southwest corner.
                ``rectangle.high()`` must be the northeast point of the
                rectangle viewport. ``rectangle.low()`` must be the
                southwest point of the rectangle viewport.
                ``rectangle.low().latitude()`` cannot be greater than
                ``rectangle.high().latitude()``. This will result in an
                empty latitude range. A rectangle viewport cannot be wider
                than 180 degrees.

                This field is a member of `oneof`_ ``type``.
        """

        rectangle: ggt_viewport.Viewport = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="type",
            message=ggt_viewport.Viewport,
        )

    address_query: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="address_input",
    )
    address: postal_address_pb2.PostalAddress = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="address_input",
        message=postal_address_pb2.PostalAddress,
    )
    location_bias: LocationBias = proto.Field(
        proto.MESSAGE,
        number=3,
        message=LocationBias,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=4,
    )
    region_code: str = proto.Field(
        proto.STRING,
        number=5,
    )


class GeocodeLocationRequest(proto.Message):
    r"""Request message for GeocodeService.GeocodeLocation.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        location_query (str):
            The location in the format of "lat,lng"
            string. For example, "64.7611872,-18.4705364".

            This field is a member of `oneof`_ ``location_input``.
        location (google.type.latlng_pb2.LatLng):
            The location in the structured format.

            This field is a member of `oneof`_ ``location_input``.
        language_code (str):
            Optional. Language in which the results
            should be returned.
        region_code (str):
            Optional. Region code. The region code,
            specified as a ccTLD ("top-level domain")
            two-character value. The parameter affects
            results based on applicable law.
        types (MutableSequence[str]):
            Optional. A set of type tags to restrict the
            results. Results that do not have any of the
            specified types are removed.

            For the complete list of possible values, see
            Table A and Table B at
            https://developers.google.com/maps/documentation/places/web-service/place-types.
        granularity (MutableSequence[google.maps.geocode_v4.types.GeocodeResult.Granularity]):
            Optional. A filter of one or more location
            granularity enums.
    """

    location_query: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="location_input",
    )
    location: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="location_input",
        message=latlng_pb2.LatLng,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=3,
    )
    region_code: str = proto.Field(
        proto.STRING,
        number=4,
    )
    types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    granularity: MutableSequence["GeocodeResult.Granularity"] = proto.RepeatedField(
        proto.ENUM,
        number=6,
        enum="GeocodeResult.Granularity",
    )


class GeocodePlaceRequest(proto.Message):
    r"""Request message for GeocodeService.GeocodePlace.

    Attributes:
        place (str):
            Required. Place identifier to geocode in the
            format of places/{place}.
        language_code (str):
            Optional. Language in which the results
            should be returned.
        region_code (str):
            Optional. Region code. The region code,
            specified as a ccTLD ("top-level domain")
            two-character value. The parameter affects
            results based on applicable law.
    """

    place: str = proto.Field(
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


class PlusCode(proto.Message):
    r"""Plus code (http://plus.codes) is a location reference with
    two formats: global code defining a 14mx14m (1/8000th of a
    degree) or smaller rectangle, and compound code, replacing the
    prefix with a reference location.

    Attributes:
        global_code (str):
            Place's global (full) code, such as
            "9FWM33GV+HQ", representing an 1/8000 by 1/8000
            degree area (~14 by 14 meters).
        compound_code (str):
            Place's compound code, such as "33GV+HQ,
            Ramberg, Norway", containing the suffix of the
            global code and replacing the prefix with a
            formatted name of a reference entity.
    """

    global_code: str = proto.Field(
        proto.STRING,
        number=1,
    )
    compound_code: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GeocodeResult(proto.Message):
    r"""A geocode result contains geographic information about a
    place.

    Attributes:
        place (str):
            This Place's resource name, in ``places/{placeId}`` format.
            Can be used to look up the Place.
        place_id (str):
            The unique identifier of a place.
        location (google.type.latlng_pb2.LatLng):
            The latlng of this address.
        granularity (google.maps.geocode_v4.types.GeocodeResult.Granularity):
            The granularity of the location.
        viewport (google.geo.type.types.Viewport):
            A viewport suitable for displaying the
            geocode result.
        bounds (google.geo.type.types.Viewport):
            A bounding box for the address.
        formatted_address (str):
            The one line formatted address.
        postal_address (google.type.postal_address_pb2.PostalAddress):
            The address in postal address format.
        address_components (MutableSequence[google.maps.geocode_v4.types.GeocodeResult.AddressComponent]):
            Repeated components for each locality level.
        postal_code_localities (MutableSequence[google.type.localized_text_pb2.LocalizedText]):
            Complete list of localities contained in the postal code.

            This is only populated when the result is of type
            "postal_code".
        types (MutableSequence[str]):
            A set of type tags for this result. For example, "political"
            and "administrative_area".

            For the complete list of possible values, see Table A and
            Table B at
            https://developers.google.com/maps/documentation/places/web-service/place-types.
        plus_code (google.maps.geocode_v4.types.PlusCode):
            Plus code of the location in this geocode.
    """

    class Granularity(proto.Enum):
        r"""The granularity of the location.

        Values:
            GRANULARITY_UNSPECIFIED (0):
                Do not use.
            ROOFTOP (1):
                The non-interpolated location of an actual
                plot of land corresponding to the matched
                address.
            RANGE_INTERPOLATED (2):
                Interpolated from a range of street numbers.
                For example, if we know that a segment of
                Amphitheatre Pkwy contains numbers 1600 - 1699,
                then 1650 might be placed halfway between its
                endpoints.
            GEOMETRIC_CENTER (3):
                The geometric center of a feature for which
                we have polygonal data.
            APPROXIMATE (4):
                Everything else.
        """

        GRANULARITY_UNSPECIFIED = 0
        ROOFTOP = 1
        RANGE_INTERPOLATED = 2
        GEOMETRIC_CENTER = 3
        APPROXIMATE = 4

    class AddressComponent(proto.Message):
        r"""The structured components that form the formatted address, if
        this information is available.

        Attributes:
            long_text (str):
                The full text description or name of the
                address component. For example, an address
                component for the country Australia may have a
                long name of "Australia".
            short_text (str):
                An abbreviated textual name for the address
                component, if available. For example, an address
                component for the country of Australia may have
                a short name of "AU".
            types (MutableSequence[str]):
                An array indicating the type(s) of the
                address component.
                See
                https://developers.google.com/maps/documentation/geocoding/requests-geocoding#Types
                for more details.
            language_code (str):
                The language used to format this component,
                in CLDR notation.
        """

        long_text: str = proto.Field(
            proto.STRING,
            number=1,
        )
        short_text: str = proto.Field(
            proto.STRING,
            number=2,
        )
        types: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )
        language_code: str = proto.Field(
            proto.STRING,
            number=4,
        )

    place: str = proto.Field(
        proto.STRING,
        number=1,
    )
    place_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=3,
        message=latlng_pb2.LatLng,
    )
    granularity: Granularity = proto.Field(
        proto.ENUM,
        number=4,
        enum=Granularity,
    )
    viewport: ggt_viewport.Viewport = proto.Field(
        proto.MESSAGE,
        number=5,
        message=ggt_viewport.Viewport,
    )
    bounds: ggt_viewport.Viewport = proto.Field(
        proto.MESSAGE,
        number=6,
        message=ggt_viewport.Viewport,
    )
    formatted_address: str = proto.Field(
        proto.STRING,
        number=7,
    )
    postal_address: postal_address_pb2.PostalAddress = proto.Field(
        proto.MESSAGE,
        number=8,
        message=postal_address_pb2.PostalAddress,
    )
    address_components: MutableSequence[AddressComponent] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=AddressComponent,
    )
    postal_code_localities: MutableSequence[localized_text_pb2.LocalizedText] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=11,
            message=localized_text_pb2.LocalizedText,
        )
    )
    types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=12,
    )
    plus_code: "PlusCode" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="PlusCode",
    )


class GeocodeAddressResponse(proto.Message):
    r"""Response message for
    [GeocodeService.GeocodeAddress][google.maps.geocode.v4.GeocodeService.GeocodeAddress].

    Attributes:
        results (MutableSequence[google.maps.geocode_v4.types.GeocodeResult]):
            The geocoding result.
    """

    results: MutableSequence["GeocodeResult"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="GeocodeResult",
    )


class GeocodeLocationResponse(proto.Message):
    r"""Response message for
    [GeocodeService.GeocodeLocation][google.maps.geocode.v4.GeocodeService.GeocodeLocation].

    Attributes:
        results (MutableSequence[google.maps.geocode_v4.types.GeocodeResult]):
            The geocoding result.
        plus_code (google.maps.geocode_v4.types.PlusCode):
            Plus code of the location in the request.
    """

    results: MutableSequence["GeocodeResult"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="GeocodeResult",
    )
    plus_code: "PlusCode" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="PlusCode",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
