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
import google.type.date_pb2 as date_pb2  # type: ignore
import google.type.localized_text_pb2 as localized_text_pb2  # type: ignore
import proto  # type: ignore

from google.maps.places_v1.types import attribution

__protobuf__ = proto.module(
    package="google.maps.places.v1",
    manifest={
        "Review",
    },
)


class Review(proto.Message):
    r"""Information about a review of a place.

    Attributes:
        name (str):
            A reference representing this place review which may be used
            to look up this place review again (also called the API
            "resource" name: ``places/{place_id}/reviews/{review}``).
        relative_publish_time_description (str):
            A string of formatted recent time, expressing
            the review time relative to the current time in
            a form appropriate for the language and country.
        text (google.type.localized_text_pb2.LocalizedText):
            The localized text of the review.
        original_text (google.type.localized_text_pb2.LocalizedText):
            The review text in its original language.
        rating (float):
            A number between 1.0 and 5.0, also called the
            number of stars.
        author_attribution (google.maps.places_v1.types.AuthorAttribution):
            This review's author.
        publish_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp for the review.
        flag_content_uri (str):
            A link where users can flag a problem with
            the review.
        google_maps_uri (str):
            A link to show the review on Google Maps.
        visit_date (google.type.date_pb2.Date):
            The date when the author visited the place.
            This is truncated to the year and month of the
            visit.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    relative_publish_time_description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    text: localized_text_pb2.LocalizedText = proto.Field(
        proto.MESSAGE,
        number=9,
        message=localized_text_pb2.LocalizedText,
    )
    original_text: localized_text_pb2.LocalizedText = proto.Field(
        proto.MESSAGE,
        number=12,
        message=localized_text_pb2.LocalizedText,
    )
    rating: float = proto.Field(
        proto.DOUBLE,
        number=7,
    )
    author_attribution: attribution.AuthorAttribution = proto.Field(
        proto.MESSAGE,
        number=13,
        message=attribution.AuthorAttribution,
    )
    publish_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=14,
        message=timestamp_pb2.Timestamp,
    )
    flag_content_uri: str = proto.Field(
        proto.STRING,
        number=15,
    )
    google_maps_uri: str = proto.Field(
        proto.STRING,
        number=16,
    )
    visit_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=17,
        message=date_pb2.Date,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
