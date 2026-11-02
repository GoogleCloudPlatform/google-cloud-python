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

from google.cloud.datalabeling_v1beta1.types import annotation, data_payloads
from google.cloud.datalabeling_v1beta1.types import (
    human_annotation_config as gcd_human_annotation_config,
)

__protobuf__ = proto.module(
    package="google.cloud.datalabeling.v1beta1",
    manifest={
        "DataType",
        "Dataset",
        "InputConfig",
        "TextMetadata",
        "ClassificationMetadata",
        "GcsSource",
        "BigQuerySource",
        "OutputConfig",
        "GcsDestination",
        "GcsFolderDestination",
        "DataItem",
        "AnnotatedDataset",
        "LabelStats",
        "AnnotatedDatasetMetadata",
        "Example",
    },
)


class DataType(proto.Enum):
    r"""

    Values:
        DATA_TYPE_UNSPECIFIED (0):
            No description available.
        IMAGE (1):
            Allowed for continuous evaluation.
        VIDEO (2):
            No description available.
        TEXT (4):
            Allowed for continuous evaluation.
        GENERAL_DATA (6):
            Allowed for continuous evaluation.
    """

    DATA_TYPE_UNSPECIFIED = 0
    IMAGE = 1
    VIDEO = 2
    TEXT = 4
    GENERAL_DATA = 6


class Dataset(proto.Message):
    r"""Dataset is the resource to hold your data. You can request
    multiple labeling tasks for a dataset while each one will
    generate an AnnotatedDataset.

    Attributes:
        name (str):
            Output only. Dataset resource name, format is:
            projects/{project_id}/datasets/{dataset_id}
        display_name (str):
            Required. The display name of the dataset.
            Maximum of 64 characters.
        description (str):
            Optional. User-provided description of the
            annotation specification set. The description
            can be up to 10000 characters long.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time the dataset is created.
        input_configs (MutableSequence[google.cloud.datalabeling_v1beta1.types.InputConfig]):
            Output only. This is populated with the
            original input configs where ImportData is
            called. It is available only after the clients
            import data to this dataset.
        blocking_resources (MutableSequence[str]):
            Output only. The names of any related
            resources that are blocking changes to the
            dataset.
        data_item_count (int):
            Output only. The number of data items in the
            dataset.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    input_configs: MutableSequence["InputConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="InputConfig",
    )
    blocking_resources: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    data_item_count: int = proto.Field(
        proto.INT64,
        number=7,
    )


class InputConfig(proto.Message):
    r"""The configuration of input data, including data type,
    location, etc.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text_metadata (google.cloud.datalabeling_v1beta1.types.TextMetadata):
            Required for text import, as language code
            must be specified.

            This field is a member of `oneof`_ ``data_type_metadata``.
        gcs_source (google.cloud.datalabeling_v1beta1.types.GcsSource):
            Source located in Cloud Storage.

            This field is a member of `oneof`_ ``source``.
        bigquery_source (google.cloud.datalabeling_v1beta1.types.BigQuerySource):
            Source located in BigQuery. You must specify this field if
            you are using this InputConfig in an
            [EvaluationJob][google.cloud.datalabeling.v1beta1.EvaluationJob].

            This field is a member of `oneof`_ ``source``.
        data_type (google.cloud.datalabeling_v1beta1.types.DataType):
            Required. Data type must be specifed when
            user tries to import data.
        annotation_type (google.cloud.datalabeling_v1beta1.types.AnnotationType):
            Optional. The type of annotation to be performed on this
            data. You must specify this field if you are using this
            InputConfig in an
            [EvaluationJob][google.cloud.datalabeling.v1beta1.EvaluationJob].
        classification_metadata (google.cloud.datalabeling_v1beta1.types.ClassificationMetadata):
            Optional. Metadata about annotations for the input. You must
            specify this field if you are using this InputConfig in an
            [EvaluationJob][google.cloud.datalabeling.v1beta1.EvaluationJob]
            for a model version that performs classification.
    """

    text_metadata: "TextMetadata" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="data_type_metadata",
        message="TextMetadata",
    )
    gcs_source: "GcsSource" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="source",
        message="GcsSource",
    )
    bigquery_source: "BigQuerySource" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="source",
        message="BigQuerySource",
    )
    data_type: "DataType" = proto.Field(
        proto.ENUM,
        number=1,
        enum="DataType",
    )
    annotation_type: annotation.AnnotationType = proto.Field(
        proto.ENUM,
        number=3,
        enum=annotation.AnnotationType,
    )
    classification_metadata: "ClassificationMetadata" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="ClassificationMetadata",
    )


class TextMetadata(proto.Message):
    r"""Metadata for the text.

    Attributes:
        language_code (str):
            The language of this text, as a
            `BCP-47 <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>`__.
            Default value is en-US.
    """

    language_code: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ClassificationMetadata(proto.Message):
    r"""Metadata for classification annotations.

    Attributes:
        is_multi_label (bool):
            Whether the classification task is
            multi-label or not.
    """

    is_multi_label: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class GcsSource(proto.Message):
    r"""Source of the Cloud Storage file to be imported.

    Attributes:
        input_uri (str):
            Required. The input URI of source file. This must be a Cloud
            Storage path (``gs://...``).
        mime_type (str):
            Required. The format of the source file. Only
            "text/csv" is supported.
    """

    input_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    mime_type: str = proto.Field(
        proto.STRING,
        number=2,
    )


class BigQuerySource(proto.Message):
    r"""The BigQuery location for input data. If used in an
    [EvaluationJob][google.cloud.datalabeling.v1beta1.EvaluationJob],
    this is where the service saves the prediction input and output
    sampled from the model version.

    Attributes:
        input_uri (str):
            Required. BigQuery URI to a table, up to 2,000 characters
            long. If you specify the URI of a table that does not exist,
            Data Labeling Service creates a table at the URI with the
            correct schema when you create your
            [EvaluationJob][google.cloud.datalabeling.v1beta1.EvaluationJob].
            If you specify the URI of a table that already exists, it
            must have the `correct
            schema </ml-engine/docs/continuous-evaluation/create-job#table-schema>`__.

            Provide the table URI in the following format:

            "bq://{your_project_id}/{your_dataset_name}/{your_table_name}"

            `Learn
            more </ml-engine/docs/continuous-evaluation/create-job#table-schema>`__.
    """

    input_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


class OutputConfig(proto.Message):
    r"""The configuration of output data.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_destination (google.cloud.datalabeling_v1beta1.types.GcsDestination):
            Output to a file in Cloud Storage. Should be
            used for labeling output other than image
            segmentation.

            This field is a member of `oneof`_ ``destination``.
        gcs_folder_destination (google.cloud.datalabeling_v1beta1.types.GcsFolderDestination):
            Output to a folder in Cloud Storage. Should
            be used for image segmentation labeling output.

            This field is a member of `oneof`_ ``destination``.
    """

    gcs_destination: "GcsDestination" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="destination",
        message="GcsDestination",
    )
    gcs_folder_destination: "GcsFolderDestination" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="destination",
        message="GcsFolderDestination",
    )


class GcsDestination(proto.Message):
    r"""Export destination of the data.Only gcs path is allowed in
    output_uri.

    Attributes:
        output_uri (str):
            Required. The output uri of destination file.
        mime_type (str):
            Required. The format of the gcs destination.
            Only "text/csv" and "application/json"
            are supported.
    """

    output_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    mime_type: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GcsFolderDestination(proto.Message):
    r"""Export folder destination of the data.

    Attributes:
        output_folder_uri (str):
            Required. Cloud Storage directory to export
            data to.
    """

    output_folder_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DataItem(proto.Message):
    r"""DataItem is a piece of data, without annotation. For example,
    an image.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        image_payload (google.cloud.datalabeling_v1beta1.types.ImagePayload):
            The image payload, a container of the image
            bytes/uri.

            This field is a member of `oneof`_ ``payload``.
        text_payload (google.cloud.datalabeling_v1beta1.types.TextPayload):
            The text payload, a container of text
            content.

            This field is a member of `oneof`_ ``payload``.
        video_payload (google.cloud.datalabeling_v1beta1.types.VideoPayload):
            The video payload, a container of the video
            uri.

            This field is a member of `oneof`_ ``payload``.
        name (str):
            Output only. Name of the data item, in format of:
            projects/{project_id}/datasets/{dataset_id}/dataItems/{data_item_id}
    """

    image_payload: data_payloads.ImagePayload = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="payload",
        message=data_payloads.ImagePayload,
    )
    text_payload: data_payloads.TextPayload = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="payload",
        message=data_payloads.TextPayload,
    )
    video_payload: data_payloads.VideoPayload = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="payload",
        message=data_payloads.VideoPayload,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AnnotatedDataset(proto.Message):
    r"""AnnotatedDataset is a set holding annotations for data in a
    Dataset. Each labeling task will generate an AnnotatedDataset
    under the Dataset that the task is requested for.

    Attributes:
        name (str):
            Output only. AnnotatedDataset resource name in format of:
            projects/{project_id}/datasets/{dataset_id}/annotatedDatasets/
            {annotated_dataset_id}
        display_name (str):
            Output only. The display name of the
            AnnotatedDataset. It is specified in
            HumanAnnotationConfig when user starts a
            labeling task. Maximum of 64 characters.
        description (str):
            Output only. The description of the
            AnnotatedDataset. It is specified in
            HumanAnnotationConfig when user starts a
            labeling task. Maximum of 10000 characters.
        annotation_source (google.cloud.datalabeling_v1beta1.types.AnnotationSource):
            Output only. Source of the annotation.
        annotation_type (google.cloud.datalabeling_v1beta1.types.AnnotationType):
            Output only. Type of the annotation. It is
            specified when starting labeling task.
        example_count (int):
            Output only. Number of examples in the
            annotated dataset.
        completed_example_count (int):
            Output only. Number of examples that have
            annotation in the annotated dataset.
        label_stats (google.cloud.datalabeling_v1beta1.types.LabelStats):
            Output only. Per label statistics.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time the AnnotatedDataset was
            created.
        metadata (google.cloud.datalabeling_v1beta1.types.AnnotatedDatasetMetadata):
            Output only. Additional information about
            AnnotatedDataset.
        blocking_resources (MutableSequence[str]):
            Output only. The names of any related
            resources that are blocking changes to the
            annotated dataset.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=9,
    )
    annotation_source: annotation.AnnotationSource = proto.Field(
        proto.ENUM,
        number=3,
        enum=annotation.AnnotationSource,
    )
    annotation_type: annotation.AnnotationType = proto.Field(
        proto.ENUM,
        number=8,
        enum=annotation.AnnotationType,
    )
    example_count: int = proto.Field(
        proto.INT64,
        number=4,
    )
    completed_example_count: int = proto.Field(
        proto.INT64,
        number=5,
    )
    label_stats: "LabelStats" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="LabelStats",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    metadata: "AnnotatedDatasetMetadata" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="AnnotatedDatasetMetadata",
    )
    blocking_resources: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=11,
    )


class LabelStats(proto.Message):
    r"""Statistics about annotation specs.

    Attributes:
        example_count (MutableMapping[str, int]):
            Map of each annotation spec's example count.
            Key is the annotation spec name and value is the
            number of examples for that annotation spec. If
            the annotated dataset does not have annotation
            spec, the map will return a pair where the key
            is empty string and value is the total number of
            annotations.
    """

    example_count: MutableMapping[str, int] = proto.MapField(
        proto.STRING,
        proto.INT64,
        number=1,
    )


class AnnotatedDatasetMetadata(proto.Message):
    r"""Metadata on AnnotatedDataset.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        image_classification_config (google.cloud.datalabeling_v1beta1.types.ImageClassificationConfig):
            Configuration for image classification task.

            This field is a member of `oneof`_ ``annotation_request_config``.
        bounding_poly_config (google.cloud.datalabeling_v1beta1.types.BoundingPolyConfig):
            Configuration for image bounding box and
            bounding poly task.

            This field is a member of `oneof`_ ``annotation_request_config``.
        polyline_config (google.cloud.datalabeling_v1beta1.types.PolylineConfig):
            Configuration for image polyline task.

            This field is a member of `oneof`_ ``annotation_request_config``.
        segmentation_config (google.cloud.datalabeling_v1beta1.types.SegmentationConfig):
            Configuration for image segmentation task.

            This field is a member of `oneof`_ ``annotation_request_config``.
        video_classification_config (google.cloud.datalabeling_v1beta1.types.VideoClassificationConfig):
            Configuration for video classification task.

            This field is a member of `oneof`_ ``annotation_request_config``.
        object_detection_config (google.cloud.datalabeling_v1beta1.types.ObjectDetectionConfig):
            Configuration for video object detection
            task.

            This field is a member of `oneof`_ ``annotation_request_config``.
        object_tracking_config (google.cloud.datalabeling_v1beta1.types.ObjectTrackingConfig):
            Configuration for video object tracking task.

            This field is a member of `oneof`_ ``annotation_request_config``.
        event_config (google.cloud.datalabeling_v1beta1.types.EventConfig):
            Configuration for video event labeling task.

            This field is a member of `oneof`_ ``annotation_request_config``.
        text_classification_config (google.cloud.datalabeling_v1beta1.types.TextClassificationConfig):
            Configuration for text classification task.

            This field is a member of `oneof`_ ``annotation_request_config``.
        text_entity_extraction_config (google.cloud.datalabeling_v1beta1.types.TextEntityExtractionConfig):
            Configuration for text entity extraction
            task.

            This field is a member of `oneof`_ ``annotation_request_config``.
        human_annotation_config (google.cloud.datalabeling_v1beta1.types.HumanAnnotationConfig):
            HumanAnnotationConfig used when requesting
            the human labeling task for this
            AnnotatedDataset.
    """

    image_classification_config: gcd_human_annotation_config.ImageClassificationConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="annotation_request_config",
        message=gcd_human_annotation_config.ImageClassificationConfig,
    )
    bounding_poly_config: gcd_human_annotation_config.BoundingPolyConfig = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="annotation_request_config",
        message=gcd_human_annotation_config.BoundingPolyConfig,
    )
    polyline_config: gcd_human_annotation_config.PolylineConfig = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="annotation_request_config",
        message=gcd_human_annotation_config.PolylineConfig,
    )
    segmentation_config: gcd_human_annotation_config.SegmentationConfig = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="annotation_request_config",
        message=gcd_human_annotation_config.SegmentationConfig,
    )
    video_classification_config: gcd_human_annotation_config.VideoClassificationConfig = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="annotation_request_config",
        message=gcd_human_annotation_config.VideoClassificationConfig,
    )
    object_detection_config: gcd_human_annotation_config.ObjectDetectionConfig = (
        proto.Field(
            proto.MESSAGE,
            number=7,
            oneof="annotation_request_config",
            message=gcd_human_annotation_config.ObjectDetectionConfig,
        )
    )
    object_tracking_config: gcd_human_annotation_config.ObjectTrackingConfig = (
        proto.Field(
            proto.MESSAGE,
            number=8,
            oneof="annotation_request_config",
            message=gcd_human_annotation_config.ObjectTrackingConfig,
        )
    )
    event_config: gcd_human_annotation_config.EventConfig = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="annotation_request_config",
        message=gcd_human_annotation_config.EventConfig,
    )
    text_classification_config: gcd_human_annotation_config.TextClassificationConfig = (
        proto.Field(
            proto.MESSAGE,
            number=10,
            oneof="annotation_request_config",
            message=gcd_human_annotation_config.TextClassificationConfig,
        )
    )
    text_entity_extraction_config: gcd_human_annotation_config.TextEntityExtractionConfig = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="annotation_request_config",
        message=gcd_human_annotation_config.TextEntityExtractionConfig,
    )
    human_annotation_config: gcd_human_annotation_config.HumanAnnotationConfig = (
        proto.Field(
            proto.MESSAGE,
            number=1,
            message=gcd_human_annotation_config.HumanAnnotationConfig,
        )
    )


class Example(proto.Message):
    r"""An Example is a piece of data and its annotation. For
    example, an image with label "house".

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        image_payload (google.cloud.datalabeling_v1beta1.types.ImagePayload):
            The image payload, a container of the image
            bytes/uri.

            This field is a member of `oneof`_ ``payload``.
        text_payload (google.cloud.datalabeling_v1beta1.types.TextPayload):
            The text payload, a container of the text
            content.

            This field is a member of `oneof`_ ``payload``.
        video_payload (google.cloud.datalabeling_v1beta1.types.VideoPayload):
            The video payload, a container of the video
            uri.

            This field is a member of `oneof`_ ``payload``.
        name (str):
            Output only. Name of the example, in format of:
            projects/{project_id}/datasets/{dataset_id}/annotatedDatasets/
            {annotated_dataset_id}/examples/{example_id}
        annotations (MutableSequence[google.cloud.datalabeling_v1beta1.types.Annotation]):
            Output only. Annotations for the piece of
            data in Example. One piece of data can have
            multiple annotations.
    """

    image_payload: data_payloads.ImagePayload = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="payload",
        message=data_payloads.ImagePayload,
    )
    text_payload: data_payloads.TextPayload = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="payload",
        message=data_payloads.TextPayload,
    )
    video_payload: data_payloads.VideoPayload = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="payload",
        message=data_payloads.VideoPayload,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    annotations: MutableSequence[annotation.Annotation] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=annotation.Annotation,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
