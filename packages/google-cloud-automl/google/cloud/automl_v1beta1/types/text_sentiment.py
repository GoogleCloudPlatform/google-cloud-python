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

from google.cloud.automl_v1beta1.types import classification

__protobuf__ = proto.module(
    package="google.cloud.automl.v1beta1",
    manifest={
        "TextSentimentAnnotation",
        "TextSentimentEvaluationMetrics",
    },
)


class TextSentimentAnnotation(proto.Message):
    r"""Contains annotation details specific to text sentiment.

    Attributes:
        sentiment (int):
            Output only. The sentiment with the semantic, as given to
            the
            [AutoMl.ImportData][google.cloud.automl.v1beta1.AutoMl.ImportData]
            when populating the dataset from which the model used for
            the prediction had been trained. The sentiment values are
            between 0 and
            Dataset.text_sentiment_dataset_metadata.sentiment_max
            (inclusive), with higher value meaning more positive
            sentiment. They are completely relative, i.e. 0 means least
            positive sentiment and sentiment_max means the most positive
            from the sentiments present in the train data. Therefore
            e.g. if train data had only negative sentiment, then
            sentiment_max, would be still negative (although least
            negative). The sentiment shouldn't be confused with "score"
            or "magnitude" from the previous Natural Language Sentiment
            Analysis API.
    """

    sentiment: int = proto.Field(
        proto.INT32,
        number=1,
    )


class TextSentimentEvaluationMetrics(proto.Message):
    r"""Model evaluation metrics for text sentiment problems.

    Attributes:
        precision (float):
            Output only. Precision.
        recall (float):
            Output only. Recall.
        f1_score (float):
            Output only. The harmonic mean of recall and
            precision.
        mean_absolute_error (float):
            Output only. Mean absolute error. Only set
            for the overall model evaluation, not for
            evaluation of a single annotation spec.
        mean_squared_error (float):
            Output only. Mean squared error. Only set for
            the overall model evaluation, not for evaluation
            of a single annotation spec.
        linear_kappa (float):
            Output only. Linear weighted kappa. Only set
            for the overall model evaluation, not for
            evaluation of a single annotation spec.
        quadratic_kappa (float):
            Output only. Quadratic weighted kappa. Only
            set for the overall model evaluation, not for
            evaluation of a single annotation spec.
        confusion_matrix (google.cloud.automl_v1beta1.types.ClassificationEvaluationMetrics.ConfusionMatrix):
            Output only. Confusion matrix of the
            evaluation. Only set for the overall model
            evaluation, not for evaluation of a single
            annotation spec.
        annotation_spec_id (MutableSequence[str]):
            Output only. The annotation spec ids used for
            this evaluation. Deprecated .
    """

    precision: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    recall: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    f1_score: float = proto.Field(
        proto.FLOAT,
        number=3,
    )
    mean_absolute_error: float = proto.Field(
        proto.FLOAT,
        number=4,
    )
    mean_squared_error: float = proto.Field(
        proto.FLOAT,
        number=5,
    )
    linear_kappa: float = proto.Field(
        proto.FLOAT,
        number=6,
    )
    quadratic_kappa: float = proto.Field(
        proto.FLOAT,
        number=7,
    )
    confusion_matrix: classification.ClassificationEvaluationMetrics.ConfusionMatrix = (
        proto.Field(
            proto.MESSAGE,
            number=8,
            message=classification.ClassificationEvaluationMetrics.ConfusionMatrix,
        )
    )
    annotation_spec_id: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=9,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
