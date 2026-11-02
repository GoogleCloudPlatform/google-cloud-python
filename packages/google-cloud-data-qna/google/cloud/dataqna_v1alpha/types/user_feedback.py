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

__protobuf__ = proto.module(
    package="google.cloud.dataqna.v1alpha",
    manifest={
        "UserFeedback",
    },
)


class UserFeedback(proto.Message):
    r"""Feedback provided by a user.

    Attributes:
        name (str):
            Required. The unique identifier for the user feedback. User
            feedback is a singleton resource on a Question. Example:
            ``projects/foo/locations/bar/questions/1234/userFeedback``
        free_form_feedback (str):
            Free form user feedback, such as a text box.
        rating (google.cloud.dataqna_v1alpha.types.UserFeedback.UserFeedbackRating):
            The user feedback rating
    """

    class UserFeedbackRating(proto.Enum):
        r"""Enumeration of feedback ratings.

        Values:
            USER_FEEDBACK_RATING_UNSPECIFIED (0):
                No rating was specified.
            POSITIVE (1):
                The user provided positive feedback.
            NEGATIVE (2):
                The user provided negative feedback.
        """

        USER_FEEDBACK_RATING_UNSPECIFIED = 0
        POSITIVE = 1
        NEGATIVE = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    free_form_feedback: str = proto.Field(
        proto.STRING,
        number=2,
    )
    rating: UserFeedbackRating = proto.Field(
        proto.ENUM,
        number=3,
        enum=UserFeedbackRating,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
