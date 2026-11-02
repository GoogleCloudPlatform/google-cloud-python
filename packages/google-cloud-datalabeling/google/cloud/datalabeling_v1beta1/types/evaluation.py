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

from google.cloud.datalabeling_v1beta1.types import annotation, annotation_spec_set

__protobuf__ = proto.module(
    package="google.cloud.datalabeling.v1beta1",
    manifest={
        "Evaluation",
        "EvaluationConfig",
        "BoundingBoxEvaluationOptions",
        "EvaluationMetrics",
        "ClassificationMetrics",
        "ObjectDetectionMetrics",
        "PrCurve",
        "ConfusionMatrix",
    },
)


class Evaluation(proto.Message):
    r"""Describes an evaluation between a machine learning model's
    predictions and ground truth labels. Created when an
    [EvaluationJob][google.cloud.datalabeling.v1beta1.EvaluationJob]
    runs successfully.

    Attributes:
        name (str):
            Output only. Resource name of an evaluation. The name has
            the following format:

            "projects/{project_id}/datasets/{dataset_id}/evaluations/{evaluation_id}'
        config (google.cloud.datalabeling_v1beta1.types.EvaluationConfig):
            Output only. Options used in the evaluation
            job that created this evaluation.
        evaluation_job_run_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp for when the
            evaluation job that created this evaluation ran.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp for when this
            evaluation was created.
        evaluation_metrics (google.cloud.datalabeling_v1beta1.types.EvaluationMetrics):
            Output only. Metrics comparing predictions to
            ground truth labels.
        annotation_type (google.cloud.datalabeling_v1beta1.types.AnnotationType):
            Output only. Type of task that the model version being
            evaluated performs, as defined in the

            [evaluationJobConfig.inputConfig.annotationType][google.cloud.datalabeling.v1beta1.EvaluationJobConfig.input_config]
            field of the evaluation job that created this evaluation.
        evaluated_item_count (int):
            Output only. The number of items in the
            ground truth dataset that were used for this
            evaluation. Only populated when the evaulation
            is for certain AnnotationTypes.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    config: "EvaluationConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="EvaluationConfig",
    )
    evaluation_job_run_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    evaluation_metrics: "EvaluationMetrics" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="EvaluationMetrics",
    )
    annotation_type: annotation.AnnotationType = proto.Field(
        proto.ENUM,
        number=6,
        enum=annotation.AnnotationType,
    )
    evaluated_item_count: int = proto.Field(
        proto.INT64,
        number=7,
    )


class EvaluationConfig(proto.Message):
    r"""Configuration details used for calculating evaluation metrics and
    creating an
    [Evaluation][google.cloud.datalabeling.v1beta1.Evaluation].


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        bounding_box_evaluation_options (google.cloud.datalabeling_v1beta1.types.BoundingBoxEvaluationOptions):
            Only specify this field if the related model performs image
            object detection (``IMAGE_BOUNDING_BOX_ANNOTATION``).
            Describes how to evaluate bounding boxes.

            This field is a member of `oneof`_ ``vertical_option``.
    """

    bounding_box_evaluation_options: "BoundingBoxEvaluationOptions" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="vertical_option",
        message="BoundingBoxEvaluationOptions",
    )


class BoundingBoxEvaluationOptions(proto.Message):
    r"""Options regarding evaluation between bounding boxes.

    Attributes:
        iou_threshold (float):
            Minimum [intersection-over-union

            (IOU)](/vision/automl/object-detection/docs/evaluate#intersection-over-union)
            required for 2 bounding boxes to be considered a match. This
            must be a number between 0 and 1.
    """

    iou_threshold: float = proto.Field(
        proto.FLOAT,
        number=1,
    )


class EvaluationMetrics(proto.Message):
    r"""

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        classification_metrics (google.cloud.datalabeling_v1beta1.types.ClassificationMetrics):

            This field is a member of `oneof`_ ``metrics``.
        object_detection_metrics (google.cloud.datalabeling_v1beta1.types.ObjectDetectionMetrics):

            This field is a member of `oneof`_ ``metrics``.
    """

    classification_metrics: "ClassificationMetrics" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="metrics",
        message="ClassificationMetrics",
    )
    object_detection_metrics: "ObjectDetectionMetrics" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="metrics",
        message="ObjectDetectionMetrics",
    )


class ClassificationMetrics(proto.Message):
    r"""Metrics calculated for a classification model.

    Attributes:
        pr_curve (google.cloud.datalabeling_v1beta1.types.PrCurve):
            Precision-recall curve based on ground truth
            labels, predicted labels, and scores for the
            predicted labels.
        confusion_matrix (google.cloud.datalabeling_v1beta1.types.ConfusionMatrix):
            Confusion matrix of predicted labels vs.
            ground truth labels.
    """

    pr_curve: "PrCurve" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="PrCurve",
    )
    confusion_matrix: "ConfusionMatrix" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ConfusionMatrix",
    )


class ObjectDetectionMetrics(proto.Message):
    r"""Metrics calculated for an image object detection (bounding
    box) model.

    Attributes:
        pr_curve (google.cloud.datalabeling_v1beta1.types.PrCurve):
            Precision-recall curve.
    """

    pr_curve: "PrCurve" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="PrCurve",
    )


class PrCurve(proto.Message):
    r"""

    Attributes:
        annotation_spec (google.cloud.datalabeling_v1beta1.types.AnnotationSpec):
            The annotation spec of the label for which
            the precision-recall curve calculated. If this
            field is empty, that means the precision-recall
            curve is an aggregate curve for all labels.
        area_under_curve (float):
            Area under the precision-recall curve. Not to
            be confused with area under a receiver operating
            characteristic (ROC) curve.
        confidence_metrics_entries (MutableSequence[google.cloud.datalabeling_v1beta1.types.PrCurve.ConfidenceMetricsEntry]):
            Entries that make up the precision-recall graph. Each entry
            is a "point" on the graph drawn for a different
            ``confidence_threshold``.
        mean_average_precision (float):
            Mean average prcision of this curve.
    """

    class ConfidenceMetricsEntry(proto.Message):
        r"""

        Attributes:
            confidence_threshold (float):
                Threshold used for this entry.

                For classification tasks, this is a classification
                threshold: a predicted label is categorized as positive or
                negative (in the context of this point on the PR curve)
                based on whether the label's score meets this threshold.

                For image object detection (bounding box) tasks, this is the
                [intersection-over-union

                (IOU)](/vision/automl/object-detection/docs/evaluate#intersection-over-union)
                threshold for the context of this point on the PR curve.
            recall (float):
                Recall value.
            precision (float):
                Precision value.
            f1_score (float):
                Harmonic mean of recall and precision.
            recall_at1 (float):
                Recall value for entries with label that has
                highest score.
            precision_at1 (float):
                Precision value for entries with label that
                has highest score.
            f1_score_at1 (float):
                The harmonic mean of
                [recall_at1][google.cloud.datalabeling.v1beta1.PrCurve.ConfidenceMetricsEntry.recall_at1]
                and
                [precision_at1][google.cloud.datalabeling.v1beta1.PrCurve.ConfidenceMetricsEntry.precision_at1].
            recall_at5 (float):
                Recall value for entries with label that has
                highest 5 scores.
            precision_at5 (float):
                Precision value for entries with label that
                has highest 5 scores.
            f1_score_at5 (float):
                The harmonic mean of
                [recall_at5][google.cloud.datalabeling.v1beta1.PrCurve.ConfidenceMetricsEntry.recall_at5]
                and
                [precision_at5][google.cloud.datalabeling.v1beta1.PrCurve.ConfidenceMetricsEntry.precision_at5].
        """

        confidence_threshold: float = proto.Field(
            proto.FLOAT,
            number=1,
        )
        recall: float = proto.Field(
            proto.FLOAT,
            number=2,
        )
        precision: float = proto.Field(
            proto.FLOAT,
            number=3,
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
        f1_score_at1: float = proto.Field(
            proto.FLOAT,
            number=7,
        )
        recall_at5: float = proto.Field(
            proto.FLOAT,
            number=8,
        )
        precision_at5: float = proto.Field(
            proto.FLOAT,
            number=9,
        )
        f1_score_at5: float = proto.Field(
            proto.FLOAT,
            number=10,
        )

    annotation_spec: annotation_spec_set.AnnotationSpec = proto.Field(
        proto.MESSAGE,
        number=1,
        message=annotation_spec_set.AnnotationSpec,
    )
    area_under_curve: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    confidence_metrics_entries: MutableSequence[ConfidenceMetricsEntry] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message=ConfidenceMetricsEntry,
        )
    )
    mean_average_precision: float = proto.Field(
        proto.FLOAT,
        number=4,
    )


class ConfusionMatrix(proto.Message):
    r"""Confusion matrix of the model running the classification.
    Only applicable when the metrics entry aggregates multiple
    labels. Not applicable when the entry is for a single label.

    Attributes:
        row (MutableSequence[google.cloud.datalabeling_v1beta1.types.ConfusionMatrix.Row]):

    """

    class ConfusionMatrixEntry(proto.Message):
        r"""

        Attributes:
            annotation_spec (google.cloud.datalabeling_v1beta1.types.AnnotationSpec):
                The annotation spec of a predicted label.
            item_count (int):
                Number of items predicted to have this label. (The ground
                truth label for these items is the ``Row.annotationSpec`` of
                this entry's parent.)
        """

        annotation_spec: annotation_spec_set.AnnotationSpec = proto.Field(
            proto.MESSAGE,
            number=1,
            message=annotation_spec_set.AnnotationSpec,
        )
        item_count: int = proto.Field(
            proto.INT32,
            number=2,
        )

    class Row(proto.Message):
        r"""A row in the confusion matrix. Each entry in this row has the
        same ground truth label.

        Attributes:
            annotation_spec (google.cloud.datalabeling_v1beta1.types.AnnotationSpec):
                The annotation spec of the ground truth label
                for this row.
            entries (MutableSequence[google.cloud.datalabeling_v1beta1.types.ConfusionMatrix.ConfusionMatrixEntry]):
                A list of the confusion matrix entries. One
                entry for each possible predicted label.
        """

        annotation_spec: annotation_spec_set.AnnotationSpec = proto.Field(
            proto.MESSAGE,
            number=1,
            message=annotation_spec_set.AnnotationSpec,
        )
        entries: MutableSequence["ConfusionMatrix.ConfusionMatrixEntry"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="ConfusionMatrix.ConfusionMatrixEntry",
            )
        )

    row: MutableSequence[Row] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=Row,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
