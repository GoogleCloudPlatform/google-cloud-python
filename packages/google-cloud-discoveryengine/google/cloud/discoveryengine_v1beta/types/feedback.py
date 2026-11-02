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

from google.cloud.discoveryengine_v1beta.types import session as gcd_session

__protobuf__ = proto.module(
    package="google.cloud.discoveryengine.v1beta",
    manifest={
        "Feedback",
    },
)


class Feedback(proto.Message):
    r"""Information about the user feedback. This information will be
    used for logging and metrics purpose.

    Attributes:
        feedback_type (google.cloud.discoveryengine_v1beta.types.Feedback.FeedbackType):
            Required. Indicate whether the user gives a
            positive or negative feedback. If the user gives
            a negative feedback, there might be more
            feedback details.
        reasons (MutableSequence[google.cloud.discoveryengine_v1beta.types.Feedback.Reason]):
            Optional. The reason if user gives a thumb
            down.
        comment (str):
            Optional. The additional user comment of the
            feedback if user gives a thumb down.
        conversation_info (google.cloud.discoveryengine_v1beta.types.Feedback.ConversationInfo):
            The related conversation information when
            user gives feedback.
        llm_model_version (str):
            The version of the LLM model that was used to
            generate the response.
        feedback_source (google.cloud.discoveryengine_v1beta.types.Feedback.FeedbackSource):
            Optional. The UI component the user feedback comes from,
            which could be GOOGLE_CONSOLE, GOOGLE_WIDGET, GOOGLE_WEBAPP.
        component_version (str):
            Optional. The version of the component that
            this report is being sent from.
        data_terms_accepted (bool):
            Optional. Whether the customer accepted data
            use terms.
    """

    class FeedbackType(proto.Enum):
        r"""The type of the feedback user gives.

        Values:
            FEEDBACK_TYPE_UNSPECIFIED (0):
                Unspecified feedback type.
            LIKE (1):
                The user gives a positive feedback.
            DISLIKE (2):
                The user gives a negative feedback.
        """

        FEEDBACK_TYPE_UNSPECIFIED = 0
        LIKE = 1
        DISLIKE = 2

    class Reason(proto.Enum):
        r"""The reason why user gives a negative feedback.

        Values:
            REASON_UNSPECIFIED (0):
                Unspecified reason.
            INACCURATE_RESPONSE (1):
                The response is inaccurate.
            NOT_RELEVANT (2):
                The response is not relevant.
            INCOMPREHENSIVE (3):
                The response is incomprehensive.
            OFFENSIVE_OR_UNSAFE (4):
                The response is offensive or unsafe.
            FORMAT_AND_STYLES (6):
                The response is not well-formatted.
            BAD_CITATION (7):
                The response is not well-associated with the
                query.
            CANVAS_NOT_GENERATED (8):
                The expected canvas was not generated for the
                response.
            CANVAS_QUALITY_BAD (9):
                The generated canvas is of bad quality (e.g.
                inaccurate, incomplete, poorly formatted).
            CANVAS_EXPORT_FAILED (10):
                Exporting the generated canvas failed (e.g.
                download or external export action did not
                complete successfully).
        """

        REASON_UNSPECIFIED = 0
        INACCURATE_RESPONSE = 1
        NOT_RELEVANT = 2
        INCOMPREHENSIVE = 3
        OFFENSIVE_OR_UNSAFE = 4
        FORMAT_AND_STYLES = 6
        BAD_CITATION = 7
        CANVAS_NOT_GENERATED = 8
        CANVAS_QUALITY_BAD = 9
        CANVAS_EXPORT_FAILED = 10

    class FeedbackSource(proto.Enum):
        r"""Source of the feedback as per integration.

        Values:
            FEEDBACK_SOURCE_UNSPECIFIED (0):
                Unspecified feedback source.
            GOOGLE_CONSOLE (1):
                Feedback source is Google Console.
            GOOGLE_WIDGET (2):
                Feedback source is Google Widget.
            GOOGLE_WEBAPP (3):
                Feedback source is Google Webapp.
            GOOGLE_AGENTSPACE_MOBILE (4):
                Feedback source is Google AgentSpace Mobile
                app.
        """

        FEEDBACK_SOURCE_UNSPECIFIED = 0
        GOOGLE_CONSOLE = 1
        GOOGLE_WIDGET = 2
        GOOGLE_WEBAPP = 3
        GOOGLE_AGENTSPACE_MOBILE = 4

    class ConversationInfo(proto.Message):
        r"""The conversation information such as the question index and
        session name.

        Attributes:
            question_index (int):
                The index of the user input within the
                conversation messages.
            session (str):
                Name of the newly generated or continued
                session.
            query (google.cloud.discoveryengine_v1beta.types.Query):
                Required. The user's search query.
            assist_token (str):
                Optional. The token which could be used to
                fetch the assistant log.
            answer_query_token (str):
                Optional. The token which could be used to
                fetch the answer log.
        """

        question_index: int = proto.Field(
            proto.INT32,
            number=1,
        )
        session: str = proto.Field(
            proto.STRING,
            number=2,
        )
        query: gcd_session.Query = proto.Field(
            proto.MESSAGE,
            number=3,
            message=gcd_session.Query,
        )
        assist_token: str = proto.Field(
            proto.STRING,
            number=4,
        )
        answer_query_token: str = proto.Field(
            proto.STRING,
            number=5,
        )

    feedback_type: FeedbackType = proto.Field(
        proto.ENUM,
        number=1,
        enum=FeedbackType,
    )
    reasons: MutableSequence[Reason] = proto.RepeatedField(
        proto.ENUM,
        number=2,
        enum=Reason,
    )
    comment: str = proto.Field(
        proto.STRING,
        number=3,
    )
    conversation_info: ConversationInfo = proto.Field(
        proto.MESSAGE,
        number=4,
        message=ConversationInfo,
    )
    llm_model_version: str = proto.Field(
        proto.STRING,
        number=5,
    )
    feedback_source: FeedbackSource = proto.Field(
        proto.ENUM,
        number=6,
        enum=FeedbackSource,
    )
    component_version: str = proto.Field(
        proto.STRING,
        number=7,
    )
    data_terms_accepted: bool = proto.Field(
        proto.BOOL,
        number=8,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
