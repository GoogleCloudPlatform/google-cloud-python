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

from google.cloud.retail_v2beta.types import generative_question

__protobuf__ = proto.module(
    package="google.cloud.retail.v2beta",
    manifest={
        "UpdateGenerativeQuestionsFeatureConfigRequest",
        "GetGenerativeQuestionsFeatureConfigRequest",
        "ListGenerativeQuestionConfigsRequest",
        "ListGenerativeQuestionConfigsResponse",
        "UpdateGenerativeQuestionConfigRequest",
        "BatchUpdateGenerativeQuestionConfigsRequest",
        "BatchUpdateGenerativeQuestionConfigsResponse",
    },
)


class UpdateGenerativeQuestionsFeatureConfigRequest(proto.Message):
    r"""Request for UpdateGenerativeQuestionsFeatureConfig method.

    Attributes:
        generative_questions_feature_config (google.cloud.retail_v2beta.types.GenerativeQuestionsFeatureConfig):
            Required. The configuration managing the
            feature state.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Indicates which fields in the provided
            [GenerativeQuestionsFeatureConfig][google.cloud.retail.v2beta.GenerativeQuestionsFeatureConfig]
            to update. If not set or empty, all supported fields are
            updated.
    """

    generative_questions_feature_config: generative_question.GenerativeQuestionsFeatureConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=generative_question.GenerativeQuestionsFeatureConfig,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=4,
        message=field_mask_pb2.FieldMask,
    )


class GetGenerativeQuestionsFeatureConfigRequest(proto.Message):
    r"""Request for GetGenerativeQuestionsFeatureConfig method.

    Attributes:
        catalog (str):
            Required. Resource name of the parent
            catalog. Format:
            projects/{project}/locations/{location}/catalogs/{catalog}
    """

    catalog: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListGenerativeQuestionConfigsRequest(proto.Message):
    r"""Request for ListQuestions method.

    Attributes:
        parent (str):
            Required. Resource name of the parent
            catalog. Format:
            projects/{project}/locations/{location}/catalogs/{catalog}
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListGenerativeQuestionConfigsResponse(proto.Message):
    r"""Response for ListQuestions method.

    Attributes:
        generative_question_configs (MutableSequence[google.cloud.retail_v2beta.types.GenerativeQuestionConfig]):
            All the questions for a given catalog.
    """

    generative_question_configs: MutableSequence[
        generative_question.GenerativeQuestionConfig
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=generative_question.GenerativeQuestionConfig,
    )


class UpdateGenerativeQuestionConfigRequest(proto.Message):
    r"""Request for UpdateGenerativeQuestionConfig method.

    Attributes:
        generative_question_config (google.cloud.retail_v2beta.types.GenerativeQuestionConfig):
            Required. The question to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Indicates which fields in the provided
            [GenerativeQuestionConfig][google.cloud.retail.v2beta.GenerativeQuestionConfig]
            to update. The following are NOT supported:

            - [GenerativeQuestionConfig.frequency][google.cloud.retail.v2beta.GenerativeQuestionConfig.frequency]

            If not set or empty, all supported fields are updated.
    """

    generative_question_config: generative_question.GenerativeQuestionConfig = (
        proto.Field(
            proto.MESSAGE,
            number=3,
            message=generative_question.GenerativeQuestionConfig,
        )
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=4,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateGenerativeQuestionConfigsRequest(proto.Message):
    r"""Request for BatchUpdateGenerativeQuestionConfig method.

    Attributes:
        parent (str):
            Optional. Resource name of the parent
            catalog. Format:
            projects/{project}/locations/{location}/catalogs/{catalog}
        requests (MutableSequence[google.cloud.retail_v2beta.types.UpdateGenerativeQuestionConfigRequest]):
            Required. The updates question configs.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateGenerativeQuestionConfigRequest"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="UpdateGenerativeQuestionConfigRequest",
        )
    )


class BatchUpdateGenerativeQuestionConfigsResponse(proto.Message):
    r"""Aggregated response for UpdateGenerativeQuestionConfig
    method.

    Attributes:
        generative_question_configs (MutableSequence[google.cloud.retail_v2beta.types.GenerativeQuestionConfig]):
            Optional. The updates question configs.
    """

    generative_question_configs: MutableSequence[
        generative_question.GenerativeQuestionConfig
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=generative_question.GenerativeQuestionConfig,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
