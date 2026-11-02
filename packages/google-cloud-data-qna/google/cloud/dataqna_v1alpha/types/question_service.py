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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.dataqna_v1alpha.types import question as gcd_question
from google.cloud.dataqna_v1alpha.types import user_feedback as gcd_user_feedback

__protobuf__ = proto.module(
    package="google.cloud.dataqna.v1alpha",
    manifest={
        "GetQuestionRequest",
        "CreateQuestionRequest",
        "ExecuteQuestionRequest",
        "GetUserFeedbackRequest",
        "UpdateUserFeedbackRequest",
    },
)


class GetQuestionRequest(proto.Message):
    r"""A request to get a previously created question.

    Attributes:
        name (str):
            Required. The unique identifier for the question. Example:
            ``projects/foo/locations/bar/questions/1234``
        read_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to be retrieved.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    read_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class CreateQuestionRequest(proto.Message):
    r"""Request to create a question resource.

    Attributes:
        parent (str):
            Required. The name of the project this data source reference
            belongs to. Example: ``projects/foo/locations/bar``
        question (google.cloud.dataqna_v1alpha.types.Question):
            Required. The question to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    question: gcd_question.Question = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcd_question.Question,
    )


class ExecuteQuestionRequest(proto.Message):
    r"""Request to execute an interpretation.

    Attributes:
        name (str):
            Required. The unique identifier for the question. Example:
            ``projects/foo/locations/bar/questions/1234``
        interpretation_index (int):
            Required. Index of the interpretation to
            execute.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    interpretation_index: int = proto.Field(
        proto.INT32,
        number=2,
    )


class GetUserFeedbackRequest(proto.Message):
    r"""Request to get user feedback.

    Attributes:
        name (str):
            Required. The unique identifier for the user feedback. User
            feedback is a singleton resource on a Question. Example:
            ``projects/foo/locations/bar/questions/1234/userFeedback``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateUserFeedbackRequest(proto.Message):
    r"""Request to updates user feedback.

    Attributes:
        user_feedback (google.cloud.dataqna_v1alpha.types.UserFeedback):
            Required. The user feedback to update. This
            can be called even if there is no user feedback
            so far. The feedback's name field is used to
            identify the user feedback (and the
            corresponding question) to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to be updated.
    """

    user_feedback: gcd_user_feedback.UserFeedback = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcd_user_feedback.UserFeedback,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
