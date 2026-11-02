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
    package="google.cloud.automl.v1",
    manifest={
        "ClassificationType",
        "ClassificationAnnotation",
        "ClassificationEvaluationMetrics",
    },
)


class ClassificationType(proto.Enum):
    r"""Type of the classification problem.

    Values:
        CLASSIFICATION_TYPE_UNSPECIFIED (0):
            An un-set value of this enum.
        MULTICLASS (1):
            At most one label is allowed per example.
        MULTILABEL (2):
            Multiple labels are allowed for one example.
    """

    CLASSIFICATION_TYPE_UNSPECIFIED = 0
    MULTICLASS = 1
    MULTILABEL = 2


class ClassificationAnnotation(proto.Message):
    r"""Contains annotation details specific to classification.

    Attributes:
        score (float):
            Output only. A confidence estimate between
            0.0 and 1.0. A higher value means greater
            confidence that the annotation is positive. If a
            user approves an annotation as negative or
            positive, the score value remains unchanged. If
            a user creates an annotation, the score is 0 for
            negative or 1 for positive.
    """

    score: float = proto.Field(
        proto.FLOAT,
        number=1,
    )


class ClassificationEvaluationMetrics(proto.Message):
    r"""Model evaluation metrics for classification problems. Note: For
    Video Classification this metrics only describe quality of the Video
    Classification predictions of "segment_classification" type.

    Attributes:
        au_prc (float):
            Output only. The Area Under Precision-Recall
            Curve metric. Micro-averaged for the overall
            evaluation.
        au_roc (float):
            Output only. The Area Under Receiver
            Operating Characteristic curve metric.
            Micro-averaged for the overall evaluation.
        log_loss (float):
            Output only. The Log Loss metric.
        confidence_metrics_entry (MutableSequence[google.cloud.automl_v1.types.ClassificationEvaluationMetrics.ConfidenceMetricsEntry]):
            Output only. Metrics for each confidence_threshold in
            0.00,0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and
            position_threshold = INT32_MAX_VALUE. ROC and
            precision-recall curves, and other aggregated metrics are
            derived from them. The confidence metrics entries may also
            be supplied for additional values of position_threshold, but
            from these no aggregated metrics are computed.
        confusion_matrix (google.cloud.automl_v1.types.ClassificationEvaluationMetrics.ConfusionMatrix):
            Output only. Confusion matrix of the
            evaluation. Only set for MULTICLASS
            classification problems where number of labels
            is no more than 10.
            Only set for model level evaluation, not for
            evaluation per label.
        annotation_spec_id (MutableSequence[str]):
            Output only. The annotation spec ids used for
            this evaluation.
    """

    class ConfidenceMetricsEntry(proto.Message):
        r"""Metrics for a single confidence threshold.

        Attributes:
            confidence_threshold (float):
                Output only. Metrics are computed with an
                assumption that the model never returns
                predictions with score lower than this value.
            position_threshold (int):
                Output only. Metrics are computed with an assumption that
                the model always returns at most this many predictions
                (ordered by their score, descendingly), but they all still
                need to meet the confidence_threshold.
            recall (float):
                Output only. Recall (True Positive Rate) for
                the given confidence threshold.
            precision (float):
                Output only. Precision for the given
                confidence threshold.
            false_positive_rate (float):
                Output only. False Positive Rate for the
                given confidence threshold.
            f1_score (float):
                Output only. The harmonic mean of recall and
                precision.
            recall_at1 (float):
                Output only. The Recall (True Positive Rate)
                when only considering the label that has the
                highest prediction score and not below the
                confidence threshold for each example.
            precision_at1 (float):
                Output only. The precision when only
                considering the label that has the highest
                prediction score and not below the confidence
                threshold for each example.
            false_positive_rate_at1 (float):
                Output only. The False Positive Rate when
                only considering the label that has the highest
                prediction score and not below the confidence
                threshold for each example.
            f1_score_at1 (float):
                Output only. The harmonic mean of
                [recall_at1][google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry.recall_at1]
                and
                [precision_at1][google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfidenceMetricsEntry.precision_at1].
            true_positive_count (int):
                Output only. The number of model created
                labels that match a ground truth label.
            false_positive_count (int):
                Output only. The number of model created
                labels that do not match a ground truth label.
            false_negative_count (int):
                Output only. The number of ground truth
                labels that are not matched by a model created
                label.
            true_negative_count (int):
                Output only. The number of labels that were
                not created by the model, but if they would,
                they would not match a ground truth label.
        """

        confidence_threshold: float = proto.Field(
            proto.FLOAT,
            number=1,
        )
        position_threshold: int = proto.Field(
            proto.INT32,
            number=14,
        )
        recall: float = proto.Field(
            proto.FLOAT,
            number=2,
        )
        precision: float = proto.Field(
            proto.FLOAT,
            number=3,
        )
        false_positive_rate: float = proto.Field(
            proto.FLOAT,
            number=8,
        )
        f1_score: float = proto.Field(
            proto.FLOAT,
            number=4,
        )
        recall_at1: float = proto.Field(
            proto.FLOAT,
            number=5,
        )
        precision_at1: float = proto.Field(
            proto.FLOAT,
            number=6,
        )
        false_positive_rate_at1: float = proto.Field(
            proto.FLOAT,
            number=9,
        )
        f1_score_at1: float = proto.Field(
            proto.FLOAT,
            number=7,
        )
        true_positive_count: int = proto.Field(
            proto.INT64,
            number=10,
        )
        false_positive_count: int = proto.Field(
            proto.INT64,
            number=11,
        )
        false_negative_count: int = proto.Field(
            proto.INT64,
            number=12,
        )
        true_negative_count: int = proto.Field(
            proto.INT64,
            number=13,
        )

    class ConfusionMatrix(proto.Message):
        r"""Confusion matrix of the model running the classification.

        Attributes:
            annotation_spec_id (MutableSequence[str]):
                Output only. IDs of the annotation specs used in the
                confusion matrix. For Tables CLASSIFICATION
                [prediction_type][google.cloud.automl.v1p1beta.TablesModelMetadata.prediction_type]
                only list of [annotation_spec_display_name-s][] is
                populated.
            display_name (MutableSequence[str]):
                Output only. Display name of the annotation specs used in
                the confusion matrix, as they were at the moment of the
                evaluation. For Tables CLASSIFICATION
                [prediction_type-s][google.cloud.automl.v1p1beta.TablesModelMetadata.prediction_type],
                distinct values of the target column at the moment of the
                model evaluation are populated here.
            row (MutableSequence[google.cloud.automl_v1.types.ClassificationEvaluationMetrics.ConfusionMatrix.Row]):
                Output only. Rows in the confusion matrix. The number of
                rows is equal to the size of ``annotation_spec_id``.
                ``row[i].example_count[j]`` is the number of examples that
                have ground truth of the ``annotation_spec_id[i]`` and are
                predicted as ``annotation_spec_id[j]`` by the model being
                evaluated.
        """

        class Row(proto.Message):
            r"""Output only. A row in the confusion matrix.

            Attributes:
                example_count (MutableSequence[int]):
                    Output only. Value of the specific cell in the confusion
                    matrix. The number of values each row has (i.e. the length
                    of the row) is equal to the length of the
                    ``annotation_spec_id`` field or, if that one is not
                    populated, length of the
                    [display_name][google.cloud.automl.v1.ClassificationEvaluationMetrics.ConfusionMatrix.display_name]
                    field.
            """

            example_count: MutableSequence[int] = proto.RepeatedField(
                proto.INT32,
                number=1,
            )

        annotation_spec_id: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        display_name: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )
        row: MutableSequence["ClassificationEvaluationMetrics.ConfusionMatrix.Row"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="ClassificationEvaluationMetrics.ConfusionMatrix.Row",
            )
        )

    au_prc: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    au_roc: float = proto.Field(
        proto.FLOAT,
        number=6,
    )
    log_loss: float = proto.Field(
        proto.FLOAT,
        number=7,
    )
    confidence_metrics_entry: MutableSequence[ConfidenceMetricsEntry] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message=ConfidenceMetricsEntry,
        )
    )
    confusion_matrix: ConfusionMatrix = proto.Field(
        proto.MESSAGE,
        number=4,
        message=ConfusionMatrix,
    )
    annotation_spec_id: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
