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

import google.type.localized_text_pb2 as localized_text_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.maps.places.v1",
    manifest={
        "AddressDescriptor",
    },
)


class AddressDescriptor(proto.Message):
    r"""A relational description of a location. Includes a ranked set
    of nearby landmarks and precise containing areas and their
    relationship to the target location.

    Attributes:
        landmarks (MutableSequence[google.maps.places_v1.types.AddressDescriptor.Landmark]):
            A ranked list of nearby landmarks. The most
            recognizable and nearby landmarks are ranked
            first.
        areas (MutableSequence[google.maps.places_v1.types.AddressDescriptor.Area]):
            A ranked list of containing or adjacent
            areas. The most recognizable and precise areas
            are ranked first.
    """

    class Landmark(proto.Message):
        r"""Basic landmark information and the landmark's relationship
        with the target location.

        Landmarks are prominent places that can be used to describe a
        location.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            name (str):
                The landmark's resource name.
            place_id (str):
                The landmark's place id.
            display_name (google.type.localized_text_pb2.LocalizedText):
                The landmark's display name.
            types (MutableSequence[str]):
                A set of type tags for this landmark. For a
                complete list of possible values, see
                https://developers.google.com/maps/documentation/places/web-service/place-types.
            spatial_relationship (google.maps.places_v1.types.AddressDescriptor.Landmark.SpatialRelationship):
                Defines the spatial relationship between the
                target location and the landmark.
            straight_line_distance_meters (float):
                The straight line distance, in meters, between the center
                point of the target and the center point of the landmark. In
                some situations, this value can be longer than
                ``travel_distance_meters``.
            travel_distance_meters (float):
                The travel distance, in meters, along the
                road network from the target to the landmark, if
                known. This value does not take into account the
                mode of transportation, such as walking,
                driving, or biking.

                This field is a member of `oneof`_ ``_travel_distance_meters``.
        """

        class SpatialRelationship(proto.Enum):
            r"""Defines the spatial relationship between the target location
            and the landmark.

            Values:
                NEAR (0):
                    This is the default relationship when nothing
                    more specific below applies.
                WITHIN (1):
                    The landmark has a spatial geometry and the
                    target is within its bounds.
                BESIDE (2):
                    The target is directly adjacent to the
                    landmark.
                ACROSS_THE_ROAD (3):
                    The target is directly opposite the landmark
                    on the other side of the road.
                DOWN_THE_ROAD (4):
                    On the same route as the landmark but not
                    besides or across.
                AROUND_THE_CORNER (5):
                    Not on the same route as the landmark but a
                    single turn away.
                BEHIND (6):
                    Close to the landmark's structure but further
                    away from its street entrances.
            """

            NEAR = 0
            WITHIN = 1
            BESIDE = 2
            ACROSS_THE_ROAD = 3
            DOWN_THE_ROAD = 4
            AROUND_THE_CORNER = 5
            BEHIND = 6

        name: str = proto.Field(
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
        types: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=4,
        )
        spatial_relationship: "AddressDescriptor.Landmark.SpatialRelationship" = (
            proto.Field(
                proto.ENUM,
                number=5,
                enum="AddressDescriptor.Landmark.SpatialRelationship",
            )
        )
        straight_line_distance_meters: float = proto.Field(
            proto.FLOAT,
            number=6,
        )
        travel_distance_meters: float = proto.Field(
            proto.FLOAT,
            number=7,
            optional=True,
        )

    class Area(proto.Message):
        r"""Area information and the area's relationship with the target
        location.
        Areas includes precise sublocality, neighborhoods, and large
        compounds that are useful for describing a location.

        Attributes:
            name (str):
                The area's resource name.
            place_id (str):
                The area's place id.
            display_name (google.type.localized_text_pb2.LocalizedText):
                The area's display name.
            containment (google.maps.places_v1.types.AddressDescriptor.Area.Containment):
                Defines the spatial relationship between the
                target location and the area.
        """

        class Containment(proto.Enum):
            r"""Defines the spatial relationship between the target location
            and the area.

            Values:
                CONTAINMENT_UNSPECIFIED (0):
                    The containment is unspecified.
                WITHIN (1):
                    The target location is within the area
                    region, close to the center.
                OUTSKIRTS (2):
                    The target location is within the area
                    region, close to the edge.
                NEAR (3):
                    The target location is outside the area
                    region, but close by.
            """

            CONTAINMENT_UNSPECIFIED = 0
            WITHIN = 1
            OUTSKIRTS = 2
            NEAR = 3

        name: str = proto.Field(
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
        containment: "AddressDescriptor.Area.Containment" = proto.Field(
            proto.ENUM,
            number=4,
            enum="AddressDescriptor.Area.Containment",
        )

    landmarks: MutableSequence[Landmark] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=Landmark,
    )
    areas: MutableSequence[Area] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=Area,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
