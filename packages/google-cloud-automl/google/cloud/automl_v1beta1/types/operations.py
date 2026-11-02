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

from google.cloud.automl_v1beta1.types import io

__protobuf__ = proto.module(
    package="google.cloud.automl.v1beta1",
    manifest={
        "OperationMetadata",
        "DeleteOperationMetadata",
        "DeployModelOperationMetadata",
        "UndeployModelOperationMetadata",
        "CreateModelOperationMetadata",
        "ImportDataOperationMetadata",
        "ExportDataOperationMetadata",
        "BatchPredictOperationMetadata",
        "ExportModelOperationMetadata",
        "ExportEvaluatedExamplesOperationMetadata",
    },
)


class OperationMetadata(proto.Message):
    r"""Metadata used across all long running operations returned by
    AutoML API.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        delete_details (google.cloud.automl_v1beta1.types.DeleteOperationMetadata):
            Details of a Delete operation.

            This field is a member of `oneof`_ ``details``.
        deploy_model_details (google.cloud.automl_v1beta1.types.DeployModelOperationMetadata):
            Details of a DeployModel operation.

            This field is a member of `oneof`_ ``details``.
        undeploy_model_details (google.cloud.automl_v1beta1.types.UndeployModelOperationMetadata):
            Details of an UndeployModel operation.

            This field is a member of `oneof`_ ``details``.
        create_model_details (google.cloud.automl_v1beta1.types.CreateModelOperationMetadata):
            Details of CreateModel operation.

            This field is a member of `oneof`_ ``details``.
        import_data_details (google.cloud.automl_v1beta1.types.ImportDataOperationMetadata):
            Details of ImportData operation.

            This field is a member of `oneof`_ ``details``.
        batch_predict_details (google.cloud.automl_v1beta1.types.BatchPredictOperationMetadata):
            Details of BatchPredict operation.

            This field is a member of `oneof`_ ``details``.
        export_data_details (google.cloud.automl_v1beta1.types.ExportDataOperationMetadata):
            Details of ExportData operation.

            This field is a member of `oneof`_ ``details``.
        export_model_details (google.cloud.automl_v1beta1.types.ExportModelOperationMetadata):
            Details of ExportModel operation.

            This field is a member of `oneof`_ ``details``.
        export_evaluated_examples_details (google.cloud.automl_v1beta1.types.ExportEvaluatedExamplesOperationMetadata):
            Details of ExportEvaluatedExamples operation.

            This field is a member of `oneof`_ ``details``.
        progress_percent (int):
            Output only. Progress of operation. Range: [0, 100]. Not
            used currently.
        partial_failures (MutableSequence[google.rpc.status_pb2.Status]):
            Output only. Partial failures encountered.
            E.g. single files that couldn't be read.
            This field should never exceed 20 entries.
            Status details field will contain standard GCP
            error details.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the operation was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the operation was
            updated for the last time.
    """

    delete_details: "DeleteOperationMetadata" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="details",
        message="DeleteOperationMetadata",
    )
    deploy_model_details: "DeployModelOperationMetadata" = proto.Field(
        proto.MESSAGE,
        number=24,
        oneof="details",
        message="DeployModelOperationMetadata",
    )
    undeploy_model_details: "UndeployModelOperationMetadata" = proto.Field(
        proto.MESSAGE,
        number=25,
        oneof="details",
        message="UndeployModelOperationMetadata",
    )
    create_model_details: "CreateModelOperationMetadata" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="details",
        message="CreateModelOperationMetadata",
    )
    import_data_details: "ImportDataOperationMetadata" = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof="details",
        message="ImportDataOperationMetadata",
    )
    batch_predict_details: "BatchPredictOperationMetadata" = proto.Field(
        proto.MESSAGE,
        number=16,
        oneof="details",
        message="BatchPredictOperationMetadata",
    )
    export_data_details: "ExportDataOperationMetadata" = proto.Field(
        proto.MESSAGE,
        number=21,
        oneof="details",
        message="ExportDataOperationMetadata",
    )
    export_model_details: "ExportModelOperationMetadata" = proto.Field(
        proto.MESSAGE,
        number=22,
        oneof="details",
        message="ExportModelOperationMetadata",
    )
    export_evaluated_examples_details: "ExportEvaluatedExamplesOperationMetadata" = (
        proto.Field(
            proto.MESSAGE,
            number=26,
            oneof="details",
            message="ExportEvaluatedExamplesOperationMetadata",
        )
    )
    progress_percent: int = proto.Field(
        proto.INT32,
        number=13,
    )
    partial_failures: MutableSequence[status_pb2.Status] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=status_pb2.Status,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class DeleteOperationMetadata(proto.Message):
    r"""Details of operations that perform deletes of any entities."""


class DeployModelOperationMetadata(proto.Message):
    r"""Details of DeployModel operation."""


class UndeployModelOperationMetadata(proto.Message):
    r"""Details of UndeployModel operation."""


class CreateModelOperationMetadata(proto.Message):
    r"""Details of CreateModel operation."""


class ImportDataOperationMetadata(proto.Message):
    r"""Details of ImportData operation."""


class ExportDataOperationMetadata(proto.Message):
    r"""Details of ExportData operation.

    Attributes:
        output_info (google.cloud.automl_v1beta1.types.ExportDataOperationMetadata.ExportDataOutputInfo):
            Output only. Information further describing
            this export data's output.
    """

    class ExportDataOutputInfo(proto.Message):
        r"""Further describes this export data's output. Supplements
        [OutputConfig][google.cloud.automl.v1beta1.OutputConfig].

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            gcs_output_directory (str):
                The full path of the Google Cloud Storage
                directory created, into which the exported data
                is written.

                This field is a member of `oneof`_ ``output_location``.
            bigquery_output_dataset (str):
                The path of the BigQuery dataset created, in
                bq://projectId.bqDatasetId format, into which
                the exported data is written.

                This field is a member of `oneof`_ ``output_location``.
        """

        gcs_output_directory: str = proto.Field(
            proto.STRING,
            number=1,
            oneof="output_location",
        )
        bigquery_output_dataset: str = proto.Field(
            proto.STRING,
            number=2,
            oneof="output_location",
        )

    output_info: ExportDataOutputInfo = proto.Field(
        proto.MESSAGE,
        number=1,
        message=ExportDataOutputInfo,
    )


class BatchPredictOperationMetadata(proto.Message):
    r"""Details of BatchPredict operation.

    Attributes:
        input_config (google.cloud.automl_v1beta1.types.BatchPredictInputConfig):
            Output only. The input config that was given
            upon starting this batch predict operation.
        output_info (google.cloud.automl_v1beta1.types.BatchPredictOperationMetadata.BatchPredictOutputInfo):
            Output only. Information further describing
            this batch predict's output.
    """

    class BatchPredictOutputInfo(proto.Message):
        r"""Further describes this batch predict's output. Supplements

        [BatchPredictOutputConfig][google.cloud.automl.v1beta1.BatchPredictOutputConfig].

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            gcs_output_directory (str):
                The full path of the Google Cloud Storage
                directory created, into which the prediction
                output is written.

                This field is a member of `oneof`_ ``output_location``.
            bigquery_output_dataset (str):
                The path of the BigQuery dataset created, in
                bq://projectId.bqDatasetId format, into which
                the prediction output is written.

                This field is a member of `oneof`_ ``output_location``.
        """

        gcs_output_directory: str = proto.Field(
            proto.STRING,
            number=1,
            oneof="output_location",
        )
        bigquery_output_dataset: str = proto.Field(
            proto.STRING,
            number=2,
            oneof="output_location",
        )

    input_config: io.BatchPredictInputConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=io.BatchPredictInputConfig,
    )
    output_info: BatchPredictOutputInfo = proto.Field(
        proto.MESSAGE,
        number=2,
        message=BatchPredictOutputInfo,
    )


class ExportModelOperationMetadata(proto.Message):
    r"""Details of ExportModel operation.

    Attributes:
        output_info (google.cloud.automl_v1beta1.types.ExportModelOperationMetadata.ExportModelOutputInfo):
            Output only. Information further describing
            the output of this model export.
    """

    class ExportModelOutputInfo(proto.Message):
        r"""Further describes the output of model export. Supplements

        [ModelExportOutputConfig][google.cloud.automl.v1beta1.ModelExportOutputConfig].

        Attributes:
            gcs_output_directory (str):
                The full path of the Google Cloud Storage
                directory created, into which the model will be
                exported.
        """

        gcs_output_directory: str = proto.Field(
            proto.STRING,
            number=1,
        )

    output_info: ExportModelOutputInfo = proto.Field(
        proto.MESSAGE,
        number=2,
        message=ExportModelOutputInfo,
    )


class ExportEvaluatedExamplesOperationMetadata(proto.Message):
    r"""Details of EvaluatedExamples operation.

    Attributes:
        output_info (google.cloud.automl_v1beta1.types.ExportEvaluatedExamplesOperationMetadata.ExportEvaluatedExamplesOutputInfo):
            Output only. Information further describing
            the output of this evaluated examples export.
    """

    class ExportEvaluatedExamplesOutputInfo(proto.Message):
        r"""Further describes the output of the evaluated examples export.
        Supplements

        [ExportEvaluatedExamplesOutputConfig][google.cloud.automl.v1beta1.ExportEvaluatedExamplesOutputConfig].

        Attributes:
            bigquery_output_dataset (str):
                The path of the BigQuery dataset created, in
                bq://projectId.bqDatasetId format, into which
                the output of export evaluated examples is
                written.
        """

        bigquery_output_dataset: str = proto.Field(
            proto.STRING,
            number=2,
        )

    output_info: ExportEvaluatedExamplesOutputInfo = proto.Field(
        proto.MESSAGE,
        number=2,
        message=ExportEvaluatedExamplesOutputInfo,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
