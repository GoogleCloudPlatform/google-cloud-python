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
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.datalabeling_v1beta1.types import dataset, evaluation
from google.cloud.datalabeling_v1beta1.types import (
    human_annotation_config as gcd_human_annotation_config,
)

__protobuf__ = proto.module(
    package="google.cloud.datalabeling.v1beta1",
    manifest={
        "EvaluationJob",
        "EvaluationJobConfig",
        "EvaluationJobAlertConfig",
        "Attempt",
    },
)


class EvaluationJob(proto.Message):
    r"""Defines an evaluation job that runs periodically to generate
    [Evaluations][google.cloud.datalabeling.v1beta1.Evaluation].
    `Creating an evaluation
    job </ml-engine/docs/continuous-evaluation/create-job>`__ is the
    starting point for using continuous evaluation.

    Attributes:
        name (str):
            Output only. After you create a job, Data Labeling Service
            assigns a name to the job with the following format:

            "projects/{project_id}/evaluationJobs/{evaluation_job_id}".
        description (str):
            Required. Description of the job. The
            description can be up to 25,000 characters long.
        state (google.cloud.datalabeling_v1beta1.types.EvaluationJob.State):
            Output only. Describes the current state of
            the job.
        schedule (str):
            Required. Describes the interval at which the job runs. This
            interval must be at least 1 day, and it is rounded to the
            nearest day. For example, if you specify a 50-hour interval,
            the job runs every 2 days.

            You can provide the schedule in `crontab
            format </scheduler/docs/configuring/cron-job-schedules>`__
            or in an `English-like
            format </appengine/docs/standard/python/config/cronref#schedule_format>`__.

            Regardless of what you specify, the job will run at 10:00 AM
            UTC. Only the interval from this schedule is used, not the
            specific time of day.
        model_version (str):
            Required. The `AI Platform Prediction model
            version </ml-engine/docs/prediction-overview>`__ to be
            evaluated. Prediction input and output is sampled from this
            model version. When creating an evaluation job, specify the
            model version in the following format:

            "projects/{project_id}/models/{model_name}/versions/{version_name}"

            There can only be one evaluation job per model version.
        evaluation_job_config (google.cloud.datalabeling_v1beta1.types.EvaluationJobConfig):
            Required. Configuration details for the
            evaluation job.
        annotation_spec_set (str):
            Required. Name of the
            [AnnotationSpecSet][google.cloud.datalabeling.v1beta1.AnnotationSpecSet]
            describing all the labels that your machine learning model
            outputs. You must create this resource before you create an
            evaluation job and provide its name in the following format:

            "projects/{project_id}/annotationSpecSets/{annotation_spec_set_id}".
        label_missing_ground_truth (bool):
            Required. Whether you want Data Labeling Service to provide
            ground truth labels for prediction input. If you want the
            service to assign human labelers to annotate your data, set
            this to ``true``. If you want to provide your own ground
            truth labels in the evaluation job's BigQuery table, set
            this to ``false``.
        attempts (MutableSequence[google.cloud.datalabeling_v1beta1.types.Attempt]):
            Output only. Every time the evaluation job
            runs and an error occurs, the failed attempt is
            appended to this array.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp of when this
            evaluation job was created.
    """

    class State(proto.Enum):
        r"""State of the job.

        Values:
            STATE_UNSPECIFIED (0):
                No description available.
            SCHEDULED (1):
                The job is scheduled to run at the [configured
                interval][google.cloud.datalabeling.v1beta1.EvaluationJob.schedule].
                You can
                [pause][google.cloud.datalabeling.v1beta1.DataLabelingService.PauseEvaluationJob]
                or
                [delete][google.cloud.datalabeling.v1beta1.DataLabelingService.DeleteEvaluationJob]
                the job.

                When the job is in this state, it samples prediction input
                and output from your model version into your BigQuery table
                as predictions occur.
            RUNNING (2):
                The job is currently running. When the job runs, Data
                Labeling Service does several things:

                1. If you have configured your job to use Data Labeling
                   Service for ground truth labeling, the service creates a
                   [Dataset][google.cloud.datalabeling.v1beta1.Dataset] and
                   a labeling task for all data sampled since the last time
                   the job ran. Human labelers provide ground truth labels
                   for your data. Human labeling may take hours, or even
                   days, depending on how much data has been sampled. The
                   job remains in the ``RUNNING`` state during this time,
                   and it can even be running multiple times in parallel if
                   it gets triggered again (for example 24 hours later)
                   before the earlier run has completed. When human labelers
                   have finished labeling the data, the next step occurs. If
                   you have configured your job to provide your own ground
                   truth labels, Data Labeling Service still creates a
                   [Dataset][google.cloud.datalabeling.v1beta1.Dataset] for
                   newly sampled data, but it expects that you have already
                   added ground truth labels to the BigQuery table by this
                   time. The next step occurs immediately.

                2. Data Labeling Service creates an
                   [Evaluation][google.cloud.datalabeling.v1beta1.Evaluation]
                   by comparing your model version's predictions with the
                   ground truth labels.

                If the job remains in this state for a long time, it
                continues to sample prediction data into your BigQuery table
                and will run again at the next interval, even if it causes
                the job to run multiple times in parallel.
            PAUSED (3):
                The job is not sampling prediction input and output into
                your BigQuery table and it will not run according to its
                schedule. You can
                [resume][google.cloud.datalabeling.v1beta1.DataLabelingService.ResumeEvaluationJob]
                the job.
            STOPPED (4):
                The job has this state right before it is
                deleted.
        """

        STATE_UNSPECIFIED = 0
        SCHEDULED = 1
        RUNNING = 2
        PAUSED = 3
        STOPPED = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    schedule: str = proto.Field(
        proto.STRING,
        number=4,
    )
    model_version: str = proto.Field(
        proto.STRING,
        number=5,
    )
    evaluation_job_config: "EvaluationJobConfig" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="EvaluationJobConfig",
    )
    annotation_spec_set: str = proto.Field(
        proto.STRING,
        number=7,
    )
    label_missing_ground_truth: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    attempts: MutableSequence["Attempt"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="Attempt",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )


class EvaluationJobConfig(proto.Message):
    r"""Configures specific details of how a continuous evaluation
    job works. Provide this configuration when you create an
    EvaluationJob.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        image_classification_config (google.cloud.datalabeling_v1beta1.types.ImageClassificationConfig):
            Specify this field if your model version performs image
            classification or general classification.

            ``annotationSpecSet`` in this configuration must match
            [EvaluationJob.annotationSpecSet][google.cloud.datalabeling.v1beta1.EvaluationJob.annotation_spec_set].
            ``allowMultiLabel`` in this configuration must match
            ``classificationMetadata.isMultiLabel`` in
            [input_config][google.cloud.datalabeling.v1beta1.EvaluationJobConfig.input_config].

            This field is a member of `oneof`_ ``human_annotation_request_config``.
        bounding_poly_config (google.cloud.datalabeling_v1beta1.types.BoundingPolyConfig):
            Specify this field if your model version performs image
            object detection (bounding box detection).

            ``annotationSpecSet`` in this configuration must match
            [EvaluationJob.annotationSpecSet][google.cloud.datalabeling.v1beta1.EvaluationJob.annotation_spec_set].

            This field is a member of `oneof`_ ``human_annotation_request_config``.
        text_classification_config (google.cloud.datalabeling_v1beta1.types.TextClassificationConfig):
            Specify this field if your model version performs text
            classification.

            ``annotationSpecSet`` in this configuration must match
            [EvaluationJob.annotationSpecSet][google.cloud.datalabeling.v1beta1.EvaluationJob.annotation_spec_set].
            ``allowMultiLabel`` in this configuration must match
            ``classificationMetadata.isMultiLabel`` in
            [input_config][google.cloud.datalabeling.v1beta1.EvaluationJobConfig.input_config].

            This field is a member of `oneof`_ ``human_annotation_request_config``.
        input_config (google.cloud.datalabeling_v1beta1.types.InputConfig):
            Rquired. Details for the sampled prediction input. Within
            this configuration, there are requirements for several
            fields:

            - ``dataType`` must be one of ``IMAGE``, ``TEXT``, or
              ``GENERAL_DATA``.
            - ``annotationType`` must be one of
              ``IMAGE_CLASSIFICATION_ANNOTATION``,
              ``TEXT_CLASSIFICATION_ANNOTATION``,
              ``GENERAL_CLASSIFICATION_ANNOTATION``, or
              ``IMAGE_BOUNDING_BOX_ANNOTATION`` (image object
              detection).
            - If your machine learning model performs classification,
              you must specify ``classificationMetadata.isMultiLabel``.
            - You must specify ``bigquerySource`` (not ``gcsSource``).
        evaluation_config (google.cloud.datalabeling_v1beta1.types.EvaluationConfig):
            Required. Details for calculating evaluation metrics and
            creating
            [Evaulations][google.cloud.datalabeling.v1beta1.Evaluation].
            If your model version performs image object detection, you
            must specify the ``boundingBoxEvaluationOptions`` field
            within this configuration. Otherwise, provide an empty
            object for this configuration.
        human_annotation_config (google.cloud.datalabeling_v1beta1.types.HumanAnnotationConfig):
            Optional. Details for human annotation of your data. If you
            set
            [labelMissingGroundTruth][google.cloud.datalabeling.v1beta1.EvaluationJob.label_missing_ground_truth]
            to ``true`` for this evaluation job, then you must specify
            this field. If you plan to provide your own ground truth
            labels, then omit this field.

            Note that you must create an
            [Instruction][google.cloud.datalabeling.v1beta1.Instruction]
            resource before you can specify this field. Provide the name
            of the instruction resource in the ``instruction`` field
            within this configuration.
        bigquery_import_keys (MutableMapping[str, str]):
            Required. Prediction keys that tell Data Labeling Service
            where to find the data for evaluation in your BigQuery
            table. When the service samples prediction input and output
            from your model version and saves it to BigQuery, the data
            gets stored as JSON strings in the BigQuery table. These
            keys tell Data Labeling Service how to parse the JSON.

            You can provide the following entries in this field:

            - ``data_json_key``: the data key for prediction input. You
              must provide either this key or ``reference_json_key``.
            - ``reference_json_key``: the data reference key for
              prediction input. You must provide either this key or
              ``data_json_key``.
            - ``label_json_key``: the label key for prediction output.
              Required.
            - ``label_score_json_key``: the score key for prediction
              output. Required.
            - ``bounding_box_json_key``: the bounding box key for
              prediction output. Required if your model version perform
              image object detection.

            Learn `how to configure prediction
            keys </ml-engine/docs/continuous-evaluation/create-job#prediction-keys>`__.
        example_count (int):
            Required. The maximum number of predictions to sample and
            save to BigQuery during each [evaluation
            interval][google.cloud.datalabeling.v1beta1.EvaluationJob.schedule].
            This limit overrides ``example_sample_percentage``: even if
            the service has not sampled enough predictions to fulfill
            ``example_sample_perecentage`` during an interval, it stops
            sampling predictions when it meets this limit.
        example_sample_percentage (float):
            Required. Fraction of predictions to sample and save to
            BigQuery during each [evaluation
            interval][google.cloud.datalabeling.v1beta1.EvaluationJob.schedule].
            For example, 0.1 means 10% of predictions served by your
            model version get saved to BigQuery.
        evaluation_job_alert_config (google.cloud.datalabeling_v1beta1.types.EvaluationJobAlertConfig):
            Optional. Configuration details for
            evaluation job alerts. Specify this field if you
            want to receive email alerts if the evaluation
            job finds that your predictions have low mean
            average precision during a run.
    """

    image_classification_config: gcd_human_annotation_config.ImageClassificationConfig = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="human_annotation_request_config",
        message=gcd_human_annotation_config.ImageClassificationConfig,
    )
    bounding_poly_config: gcd_human_annotation_config.BoundingPolyConfig = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="human_annotation_request_config",
        message=gcd_human_annotation_config.BoundingPolyConfig,
    )
    text_classification_config: gcd_human_annotation_config.TextClassificationConfig = (
        proto.Field(
            proto.MESSAGE,
            number=8,
            oneof="human_annotation_request_config",
            message=gcd_human_annotation_config.TextClassificationConfig,
        )
    )
    input_config: dataset.InputConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=dataset.InputConfig,
    )
    evaluation_config: evaluation.EvaluationConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=evaluation.EvaluationConfig,
    )
    human_annotation_config: gcd_human_annotation_config.HumanAnnotationConfig = (
        proto.Field(
            proto.MESSAGE,
            number=3,
            message=gcd_human_annotation_config.HumanAnnotationConfig,
        )
    )
    bigquery_import_keys: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=9,
    )
    example_count: int = proto.Field(
        proto.INT32,
        number=10,
    )
    example_sample_percentage: float = proto.Field(
        proto.DOUBLE,
        number=11,
    )
    evaluation_job_alert_config: "EvaluationJobAlertConfig" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="EvaluationJobAlertConfig",
    )


class EvaluationJobAlertConfig(proto.Message):
    r"""Provides details for how an evaluation job sends email alerts
    based on the results of a run.

    Attributes:
        email (str):
            Required. An email address to send alerts to.
        min_acceptable_mean_average_precision (float):
            Required. A number between 0 and 1 that describes a minimum
            mean average precision threshold. When the evaluation job
            runs, if it calculates that your model version's predictions
            from the recent interval have
            [meanAveragePrecision][google.cloud.datalabeling.v1beta1.PrCurve.mean_average_precision]
            below this threshold, then it sends an alert to your
            specified email.
    """

    email: str = proto.Field(
        proto.STRING,
        number=1,
    )
    min_acceptable_mean_average_precision: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )


class Attempt(proto.Message):
    r"""Records a failed evaluation job run.

    Attributes:
        attempt_time (google.protobuf.timestamp_pb2.Timestamp):

        partial_failures (MutableSequence[google.rpc.status_pb2.Status]):
            Details of errors that occurred.
    """

    attempt_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    partial_failures: MutableSequence[status_pb2.Status] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=status_pb2.Status,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
