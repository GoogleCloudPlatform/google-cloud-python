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

__protobuf__ = proto.module(
    package="google.cloud.documentai.v1beta3",
    manifest={
        "EvaluationReference",
        "Evaluation",
    },
)


class EvaluationReference(proto.Message):
    r"""Gives a short summary of an evaluation, and links to the
    evaluation itself.

    Attributes:
        operation (str):
            The resource name of the Long Running
            Operation for the evaluation.
        evaluation (str):
            The resource name of the evaluation.
        aggregate_metrics (google.cloud.documentai_v1beta3.types.Evaluation.Metrics):
            An aggregate of the statistics for the
            evaluation with fuzzy matching on.
        aggregate_metrics_exact (google.cloud.documentai_v1beta3.types.Evaluation.Metrics):
            An aggregate of the statistics for the
            evaluation with fuzzy matching off.
    """

    operation: str = proto.Field(
        proto.STRING,
        number=1,
    )
    evaluation: str = proto.Field(
        proto.STRING,
        number=2,
    )
    aggregate_metrics: "Evaluation.Metrics" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="Evaluation.Metrics",
    )
    aggregate_metrics_exact: "Evaluation.Metrics" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="Evaluation.Metrics",
    )


class Evaluation(proto.Message):
    r"""An evaluation of a ProcessorVersion's performance.

    Attributes:
        name (str):
            The resource name of the evaluation. Format:
            ``projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processor_version}/evaluations/{evaluation}``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time that the evaluation was created.
        document_counters (google.cloud.documentai_v1beta3.types.Evaluation.Counters):
            Counters for the documents used in the
            evaluation.
        all_entities_metrics (google.cloud.documentai_v1beta3.types.Evaluation.MultiConfidenceMetrics):
            Metrics for all the entities in aggregate.
        entity_metrics (MutableMapping[str, google.cloud.documentai_v1beta3.types.Evaluation.MultiConfidenceMetrics]):
            Metrics across confidence levels, for
            different entities.
        kms_key_name (str):
            The KMS key name used for encryption.
        kms_key_version_name (str):
            The KMS key version with which data is
            encrypted.
        revisions (MutableSequence[google.cloud.documentai_v1beta3.types.Evaluation.EvaluationRevision]):
            Contains all revisions of the evaluation,
            excluding the latest one.
    """

    class Counters(proto.Message):
        r"""Evaluation counters for the documents that were used.

        Attributes:
            input_documents_count (int):
                How many documents were sent for evaluation.
            invalid_documents_count (int):
                How many documents were not included in the
                evaluation as they didn't pass validation.
            failed_documents_count (int):
                How many documents were not included in the
                evaluation as Document AI failed to process
                them.
            evaluated_documents_count (int):
                How many documents were used in the
                evaluation.
        """

        input_documents_count: int = proto.Field(
            proto.INT32,
            number=1,
        )
        invalid_documents_count: int = proto.Field(
            proto.INT32,
            number=2,
        )
        failed_documents_count: int = proto.Field(
            proto.INT32,
            number=3,
        )
        evaluated_documents_count: int = proto.Field(
            proto.INT32,
            number=4,
        )

    class Metrics(proto.Message):
        r"""Evaluation metrics, either in aggregate or about a specific
        entity.

        Attributes:
            precision (float):
                The calculated precision.
            recall (float):
                The calculated recall.
            f1_score (float):
                The calculated F1 score.
            predicted_occurrences_count (int):
                The amount of occurrences in predicted
                documents.
            ground_truth_occurrences_count (int):
                The amount of occurrences in ground truth
                documents.
            predicted_document_count (int):
                The amount of documents with a predicted
                occurrence.
            ground_truth_document_count (int):
                The amount of documents with a ground truth
                occurrence.
            true_positives_count (int):
                The amount of true positives.
            false_positives_count (int):
                The amount of false positives.
            false_negatives_count (int):
                The amount of false negatives.
            total_documents_count (int):
                The amount of documents that had an
                occurrence of this label.
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
        predicted_occurrences_count: int = proto.Field(
            proto.INT32,
            number=4,
        )
        ground_truth_occurrences_count: int = proto.Field(
            proto.INT32,
            number=5,
        )
        predicted_document_count: int = proto.Field(
            proto.INT32,
            number=10,
        )
        ground_truth_document_count: int = proto.Field(
            proto.INT32,
            number=11,
        )
        true_positives_count: int = proto.Field(
            proto.INT32,
            number=6,
        )
        false_positives_count: int = proto.Field(
            proto.INT32,
            number=7,
        )
        false_negatives_count: int = proto.Field(
            proto.INT32,
            number=8,
        )
        total_documents_count: int = proto.Field(
            proto.INT32,
            number=9,
        )

    class ConfidenceLevelMetrics(proto.Message):
        r"""Evaluations metrics, at a specific confidence level.

        Attributes:
            confidence_level (float):
                The confidence level.
            metrics (google.cloud.documentai_v1beta3.types.Evaluation.Metrics):
                The metrics at the specific confidence level.
        """

        confidence_level: float = proto.Field(
            proto.FLOAT,
            number=1,
        )
        metrics: "Evaluation.Metrics" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="Evaluation.Metrics",
        )

    class MultiConfidenceMetrics(proto.Message):
        r"""Metrics across multiple confidence levels.

        Attributes:
            confidence_level_metrics (MutableSequence[google.cloud.documentai_v1beta3.types.Evaluation.ConfidenceLevelMetrics]):
                Metrics across confidence levels with fuzzy
                matching enabled.
            confidence_level_metrics_exact (MutableSequence[google.cloud.documentai_v1beta3.types.Evaluation.ConfidenceLevelMetrics]):
                Metrics across confidence levels with only
                exact matching.
            auprc (float):
                The calculated area under the precision
                recall curve (AUPRC), computed by integrating
                over all confidence thresholds.
            estimated_calibration_error (float):
                The Estimated Calibration Error (ECE) of the
                confidence of the predicted entities.
            auprc_exact (float):
                The AUPRC for metrics with fuzzy matching
                disabled, i.e., exact matching only.
            estimated_calibration_error_exact (float):
                The ECE for the predicted entities with fuzzy
                matching disabled, i.e., exact matching only.
            metrics_type (google.cloud.documentai_v1beta3.types.Evaluation.MultiConfidenceMetrics.MetricsType):
                The metrics type for the label.
        """

        class MetricsType(proto.Enum):
            r"""A type that determines how metrics should be interpreted.

            Values:
                METRICS_TYPE_UNSPECIFIED (0):
                    The metrics type is unspecified. By default,
                    metrics without a particular specification are
                    for leaf entity types (i.e., top-level entity
                    types without child types, or child types which
                    are not parent types themselves).
                AGGREGATE (1):
                    Indicates whether metrics for this particular
                    label type represent an aggregate of metrics for
                    other types instead of being based on actual
                    TP/FP/FN values for the label type. Metrics for
                    parent (i.e., non-leaf) entity types are an
                    aggregate of metrics for their children.
            """

            METRICS_TYPE_UNSPECIFIED = 0
            AGGREGATE = 1

        confidence_level_metrics: MutableSequence[
            "Evaluation.ConfidenceLevelMetrics"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="Evaluation.ConfidenceLevelMetrics",
        )
        confidence_level_metrics_exact: MutableSequence[
            "Evaluation.ConfidenceLevelMetrics"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message="Evaluation.ConfidenceLevelMetrics",
        )
        auprc: float = proto.Field(
            proto.FLOAT,
            number=2,
        )
        estimated_calibration_error: float = proto.Field(
            proto.FLOAT,
            number=3,
        )
        auprc_exact: float = proto.Field(
            proto.FLOAT,
            number=5,
        )
        estimated_calibration_error_exact: float = proto.Field(
            proto.FLOAT,
            number=6,
        )
        metrics_type: "Evaluation.MultiConfidenceMetrics.MetricsType" = proto.Field(
            proto.ENUM,
            number=7,
            enum="Evaluation.MultiConfidenceMetrics.MetricsType",
        )

    class EvaluationRevision(proto.Message):
        r"""A revision of the evaluation.

        Attributes:
            revision_id (str):
                Output only. The revision ID of the
                evaluation.
            document_counters (google.cloud.documentai_v1beta3.types.Evaluation.Counters):
                Output only. Counters for the documents used
                in the evaluation.
            all_entities_metrics (google.cloud.documentai_v1beta3.types.Evaluation.MultiConfidenceMetrics):
                Output only. Metrics for all the entities in
                aggregate.
            entity_metrics (MutableMapping[str, google.cloud.documentai_v1beta3.types.Evaluation.MultiConfidenceMetrics]):
                Output only. Metrics across confidence
                levels, for different entities.
        """

        revision_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        document_counters: "Evaluation.Counters" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="Evaluation.Counters",
        )
        all_entities_metrics: "Evaluation.MultiConfidenceMetrics" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="Evaluation.MultiConfidenceMetrics",
        )
        entity_metrics: MutableMapping[str, "Evaluation.MultiConfidenceMetrics"] = (
            proto.MapField(
                proto.STRING,
                proto.MESSAGE,
                number=4,
                message="Evaluation.MultiConfidenceMetrics",
            )
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    document_counters: Counters = proto.Field(
        proto.MESSAGE,
        number=5,
        message=Counters,
    )
    all_entities_metrics: MultiConfidenceMetrics = proto.Field(
        proto.MESSAGE,
        number=3,
        message=MultiConfidenceMetrics,
    )
    entity_metrics: MutableMapping[str, MultiConfidenceMetrics] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=4,
        message=MultiConfidenceMetrics,
    )
    kms_key_name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    kms_key_version_name: str = proto.Field(
        proto.STRING,
        number=7,
    )
    revisions: MutableSequence[EvaluationRevision] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=EvaluationRevision,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
