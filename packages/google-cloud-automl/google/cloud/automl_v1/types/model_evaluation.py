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
import proto  # type: ignore

from google.cloud.automl_v1.types import (
    classification,
    detection,
    text_extraction,
    text_sentiment,
    translation,
)

__protobuf__ = proto.module(
    package="google.cloud.automl.v1",
    manifest={
        "ModelEvaluation",
    },
)


class ModelEvaluation(proto.Message):
    r"""Evaluation results of a model.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        classification_evaluation_metrics (google.cloud.automl_v1.types.ClassificationEvaluationMetrics):
            Model evaluation metrics for image, text,
            video and tables classification.
            Tables problem is considered a classification
            when the target column is CATEGORY DataType.

            This field is a member of `oneof`_ ``metrics``.
        translation_evaluation_metrics (google.cloud.automl_v1.types.TranslationEvaluationMetrics):
            Model evaluation metrics for translation.

            This field is a member of `oneof`_ ``metrics``.
        image_object_detection_evaluation_metrics (google.cloud.automl_v1.types.ImageObjectDetectionEvaluationMetrics):
            Model evaluation metrics for image object
            detection.

            This field is a member of `oneof`_ ``metrics``.
        text_sentiment_evaluation_metrics (google.cloud.automl_v1.types.TextSentimentEvaluationMetrics):
            Evaluation metrics for text sentiment models.

            This field is a member of `oneof`_ ``metrics``.
        text_extraction_evaluation_metrics (google.cloud.automl_v1.types.TextExtractionEvaluationMetrics):
            Evaluation metrics for text extraction
            models.

            This field is a member of `oneof`_ ``metrics``.
        name (str):
            Output only. Resource name of the model evaluation. Format:
            ``projects/{project_id}/locations/{location_id}/models/{model_id}/modelEvaluations/{model_evaluation_id}``
        annotation_spec_id (str):
            Output only. The ID of the annotation spec that the model
            evaluation applies to. The The ID is empty for the overall
            model evaluation. For Tables annotation specs in the dataset
            do not exist and this ID is always not set, but for
            CLASSIFICATION
            [prediction_type-s][google.cloud.automl.v1.TablesModelMetadata.prediction_type]
            the
            [display_name][google.cloud.automl.v1.ModelEvaluation.display_name]
            field is used.
        display_name (str):
            Output only. The value of
            [display_name][google.cloud.automl.v1.AnnotationSpec.display_name]
            at the moment when the model was trained. Because this field
            returns a value at model training time, for different models
            trained from the same dataset, the values may differ, since
            display names could had been changed between the two model's
            trainings. For Tables CLASSIFICATION
            [prediction_type-s][google.cloud.automl.v1.TablesModelMetadata.prediction_type]
            distinct values of the target column at the moment of the
            model evaluation are populated here. The display_name is
            empty for the overall model evaluation.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when this model
            evaluation was created.
        evaluated_example_count (int):
            Output only. The number of examples used for model
            evaluation, i.e. for which ground truth from time of model
            creation is compared against the predicted annotations
            created by the model. For overall ModelEvaluation (i.e. with
            annotation_spec_id not set) this is the total number of all
            examples used for evaluation. Otherwise, this is the count
            of examples that according to the ground truth were
            annotated by the
            [annotation_spec_id][google.cloud.automl.v1.ModelEvaluation.annotation_spec_id].
    """

    classification_evaluation_metrics: classification.ClassificationEvaluationMetrics = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="metrics",
        message=classification.ClassificationEvaluationMetrics,
    )
    translation_evaluation_metrics: translation.TranslationEvaluationMetrics = (
        proto.Field(
            proto.MESSAGE,
            number=9,
            oneof="metrics",
            message=translation.TranslationEvaluationMetrics,
        )
    )
    image_object_detection_evaluation_metrics: detection.ImageObjectDetectionEvaluationMetrics = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="metrics",
        message=detection.ImageObjectDetectionEvaluationMetrics,
    )
    text_sentiment_evaluation_metrics: text_sentiment.TextSentimentEvaluationMetrics = (
        proto.Field(
            proto.MESSAGE,
            number=11,
            oneof="metrics",
            message=text_sentiment.TextSentimentEvaluationMetrics,
        )
    )
    text_extraction_evaluation_metrics: text_extraction.TextExtractionEvaluationMetrics = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="metrics",
        message=text_extraction.TextExtractionEvaluationMetrics,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    annotation_spec_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=15,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    evaluated_example_count: int = proto.Field(
        proto.INT32,
        number=6,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
