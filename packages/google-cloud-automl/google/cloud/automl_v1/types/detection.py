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

from google.cloud.automl_v1.types import geometry

__protobuf__ = proto.module(
    package="google.cloud.automl.v1",
    manifest={
        "ImageObjectDetectionAnnotation",
        "BoundingBoxMetricsEntry",
        "ImageObjectDetectionEvaluationMetrics",
    },
)


class ImageObjectDetectionAnnotation(proto.Message):
    r"""Annotation details for image object detection.

    Attributes:
        bounding_box (google.cloud.automl_v1.types.BoundingPoly):
            Output only. The rectangle representing the
            object location.
        score (float):
            Output only. The confidence that this annotation is positive
            for the parent example, value in [0, 1], higher means higher
            positivity confidence.
    """

    bounding_box: geometry.BoundingPoly = proto.Field(
        proto.MESSAGE,
        number=1,
        message=geometry.BoundingPoly,
    )
    score: float = proto.Field(
        proto.FLOAT,
        number=2,
    )


class BoundingBoxMetricsEntry(proto.Message):
    r"""Bounding box matching model metrics for a single
    intersection-over-union threshold and multiple label match
    confidence thresholds.

    Attributes:
        iou_threshold (float):
            Output only. The intersection-over-union
            threshold value used to compute this metrics
            entry.
        mean_average_precision (float):
            Output only. The mean average precision, most often close to
            au_prc.
        confidence_metrics_entries (MutableSequence[google.cloud.automl_v1.types.BoundingBoxMetricsEntry.ConfidenceMetricsEntry]):
            Output only. Metrics for each label-match
            confidence_threshold from
            0.05,0.10,...,0.95,0.96,0.97,0.98,0.99. Precision-recall
            curve is derived from them.
    """

    class ConfidenceMetricsEntry(proto.Message):
        r"""Metrics for a single confidence threshold.

        Attributes:
            confidence_threshold (float):
                Output only. The confidence threshold value
                used to compute the metrics.
            recall (float):
                Output only. Recall under the given
                confidence threshold.
            precision (float):
                Output only. Precision under the given
                confidence threshold.
            f1_score (float):
                Output only. The harmonic mean of recall and
                precision.
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

    iou_threshold: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    mean_average_precision: float = proto.Field(
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


class ImageObjectDetectionEvaluationMetrics(proto.Message):
    r"""Model evaluation metrics for image object detection problems.
    Evaluates prediction quality of labeled bounding boxes.

    Attributes:
        evaluated_bounding_box_count (int):
            Output only. The total number of bounding
            boxes (i.e. summed over all images) the ground
            truth used to create this evaluation had.
        bounding_box_metrics_entries (MutableSequence[google.cloud.automl_v1.types.BoundingBoxMetricsEntry]):
            Output only. The bounding boxes match metrics
            for each Intersection-over-union threshold
            0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and each
            label confidence threshold
            0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 pair.
        bounding_box_mean_average_precision (float):
            Output only. The single metric for bounding boxes
            evaluation: the mean_average_precision averaged over all
            bounding_box_metrics_entries.
    """

    evaluated_bounding_box_count: int = proto.Field(
        proto.INT32,
        number=1,
    )
    bounding_box_metrics_entries: MutableSequence["BoundingBoxMetricsEntry"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="BoundingBoxMetricsEntry",
        )
    )
    bounding_box_mean_average_precision: float = proto.Field(
        proto.FLOAT,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
