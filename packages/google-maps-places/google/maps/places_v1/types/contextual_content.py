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

import proto  # type: ignore

from google.maps.places_v1.types import photo
from google.maps.places_v1.types import review as gmp_review

__protobuf__ = proto.module(
    package="google.maps.places.v1",
    manifest={
        "ContextualContent",
    },
)


class ContextualContent(proto.Message):
    r"""Experimental: See
    https://developers.google.com/maps/documentation/places/web-service/experimental/places-generative
    for more details.

    Content that is contextual to the place query.

    Attributes:
        reviews (MutableSequence[google.maps.places_v1.types.Review]):
            List of reviews about this place, contextual
            to the place query.
        photos (MutableSequence[google.maps.places_v1.types.Photo]):
            Information (including references) about
            photos of this place, contextual to the place
            query.
        justifications (MutableSequence[google.maps.places_v1.types.ContextualContent.Justification]):
            Experimental: See
            https://developers.google.com/maps/documentation/places/web-service/experimental/places-generative
            for more details.

            Justifications for the place.
    """

    class Justification(proto.Message):
        r"""Experimental: See
        https://developers.google.com/maps/documentation/places/web-service/experimental/places-generative
        for more details.

        Justifications for the place. Justifications answers the
        question of why a place could interest an end user.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            review_justification (google.maps.places_v1.types.ContextualContent.Justification.ReviewJustification):
                Experimental: See
                https://developers.google.com/maps/documentation/places/web-service/experimental/places-generative
                for more details.

                This field is a member of `oneof`_ ``justification``.
            business_availability_attributes_justification (google.maps.places_v1.types.ContextualContent.Justification.BusinessAvailabilityAttributesJustification):
                Experimental: See
                https://developers.google.com/maps/documentation/places/web-service/experimental/places-generative
                for more details.

                This field is a member of `oneof`_ ``justification``.
        """

        class ReviewJustification(proto.Message):
            r"""Experimental: See
            https://developers.google.com/maps/documentation/places/web-service/experimental/places-generative
            for more details.

            User review justifications. This highlights a section of the
            user review that would interest an end user. For instance, if
            the search query is "firewood pizza", the review justification
            highlights the text relevant to the search query.

            Attributes:
                highlighted_text (google.maps.places_v1.types.ContextualContent.Justification.ReviewJustification.HighlightedText):

                review (google.maps.places_v1.types.Review):
                    The review that the highlighted text is
                    generated from.
            """

            class HighlightedText(proto.Message):
                r"""The text highlighted by the justification. This is a subset
                of the review itself. The exact word to highlight is marked by
                the HighlightedTextRange. There could be several words in the
                text being highlighted.

                Attributes:
                    text (str):

                    highlighted_text_ranges (MutableSequence[google.maps.places_v1.types.ContextualContent.Justification.ReviewJustification.HighlightedText.HighlightedTextRange]):
                        The list of the ranges of the highlighted
                        text.
                """

                class HighlightedTextRange(proto.Message):
                    r"""The range of highlighted text.

                    Attributes:
                        start_index (int):

                        end_index (int):

                    """

                    start_index: int = proto.Field(
                        proto.INT32,
                        number=1,
                    )
                    end_index: int = proto.Field(
                        proto.INT32,
                        number=2,
                    )

                text: str = proto.Field(
                    proto.STRING,
                    number=1,
                )
                highlighted_text_ranges: MutableSequence[
                    "ContextualContent.Justification.ReviewJustification.HighlightedText.HighlightedTextRange"
                ] = proto.RepeatedField(
                    proto.MESSAGE,
                    number=2,
                    message="ContextualContent.Justification.ReviewJustification.HighlightedText.HighlightedTextRange",
                )

            highlighted_text: "ContextualContent.Justification.ReviewJustification.HighlightedText" = proto.Field(
                proto.MESSAGE,
                number=1,
                message="ContextualContent.Justification.ReviewJustification.HighlightedText",
            )
            review: gmp_review.Review = proto.Field(
                proto.MESSAGE,
                number=2,
                message=gmp_review.Review,
            )

        class BusinessAvailabilityAttributesJustification(proto.Message):
            r"""Experimental: See
            https://developers.google.com/maps/documentation/places/web-service/experimental/places-generative
            for more details.
            BusinessAvailabilityAttributes justifications. This shows some
            attributes a business has that could interest an end user.

            Attributes:
                takeout (bool):
                    If a place provides takeout.
                delivery (bool):
                    If a place provides delivery.
                dine_in (bool):
                    If a place provides dine-in.
            """

            takeout: bool = proto.Field(
                proto.BOOL,
                number=1,
            )
            delivery: bool = proto.Field(
                proto.BOOL,
                number=2,
            )
            dine_in: bool = proto.Field(
                proto.BOOL,
                number=3,
            )

        review_justification: "ContextualContent.Justification.ReviewJustification" = (
            proto.Field(
                proto.MESSAGE,
                number=1,
                oneof="justification",
                message="ContextualContent.Justification.ReviewJustification",
            )
        )
        business_availability_attributes_justification: "ContextualContent.Justification.BusinessAvailabilityAttributesJustification" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="justification",
            message="ContextualContent.Justification.BusinessAvailabilityAttributesJustification",
        )

    reviews: MutableSequence[gmp_review.Review] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gmp_review.Review,
    )
    photos: MutableSequence[photo.Photo] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=photo.Photo,
    )
    justifications: MutableSequence[Justification] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=Justification,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
