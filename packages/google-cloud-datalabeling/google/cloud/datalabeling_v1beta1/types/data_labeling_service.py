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

from google.cloud.datalabeling_v1beta1.types import (
    annotation_spec_set as gcd_annotation_spec_set,
)
from google.cloud.datalabeling_v1beta1.types import dataset as gcd_dataset
from google.cloud.datalabeling_v1beta1.types import evaluation, human_annotation_config
from google.cloud.datalabeling_v1beta1.types import evaluation_job as gcd_evaluation_job
from google.cloud.datalabeling_v1beta1.types import instruction as gcd_instruction

__protobuf__ = proto.module(
    package="google.cloud.datalabeling.v1beta1",
    manifest={
        "CreateDatasetRequest",
        "GetDatasetRequest",
        "ListDatasetsRequest",
        "ListDatasetsResponse",
        "DeleteDatasetRequest",
        "ImportDataRequest",
        "ExportDataRequest",
        "GetDataItemRequest",
        "ListDataItemsRequest",
        "ListDataItemsResponse",
        "GetAnnotatedDatasetRequest",
        "ListAnnotatedDatasetsRequest",
        "ListAnnotatedDatasetsResponse",
        "DeleteAnnotatedDatasetRequest",
        "LabelImageRequest",
        "LabelVideoRequest",
        "LabelTextRequest",
        "GetExampleRequest",
        "ListExamplesRequest",
        "ListExamplesResponse",
        "CreateAnnotationSpecSetRequest",
        "GetAnnotationSpecSetRequest",
        "ListAnnotationSpecSetsRequest",
        "ListAnnotationSpecSetsResponse",
        "DeleteAnnotationSpecSetRequest",
        "CreateInstructionRequest",
        "GetInstructionRequest",
        "DeleteInstructionRequest",
        "ListInstructionsRequest",
        "ListInstructionsResponse",
        "GetEvaluationRequest",
        "SearchEvaluationsRequest",
        "SearchEvaluationsResponse",
        "SearchExampleComparisonsRequest",
        "SearchExampleComparisonsResponse",
        "CreateEvaluationJobRequest",
        "UpdateEvaluationJobRequest",
        "GetEvaluationJobRequest",
        "PauseEvaluationJobRequest",
        "ResumeEvaluationJobRequest",
        "DeleteEvaluationJobRequest",
        "ListEvaluationJobsRequest",
        "ListEvaluationJobsResponse",
    },
)


class CreateDatasetRequest(proto.Message):
    r"""Request message for CreateDataset.

    Attributes:
        parent (str):
            Required. Dataset resource parent, format:
            projects/{project_id}
        dataset (google.cloud.datalabeling_v1beta1.types.Dataset):
            Required. The dataset to be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dataset: gcd_dataset.Dataset = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcd_dataset.Dataset,
    )


class GetDatasetRequest(proto.Message):
    r"""Request message for GetDataSet.

    Attributes:
        name (str):
            Required. Dataset resource name, format:
            projects/{project_id}/datasets/{dataset_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDatasetsRequest(proto.Message):
    r"""Request message for ListDataset.

    Attributes:
        parent (str):
            Required. Dataset resource parent, format:
            projects/{project_id}
        filter (str):
            Optional. Filter on dataset is not supported
            at this moment.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer results than requested. Default
            value is 100.
        page_token (str):
            Optional. A token identifying a page of results for the
            server to return. Typically obtained by
            [ListDatasetsResponse.next_page_token][google.cloud.datalabeling.v1beta1.ListDatasetsResponse.next_page_token]
            of the previous [DataLabelingService.ListDatasets] call.
            Returns the first page if empty.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListDatasetsResponse(proto.Message):
    r"""Results of listing datasets within a project.

    Attributes:
        datasets (MutableSequence[google.cloud.datalabeling_v1beta1.types.Dataset]):
            The list of datasets to return.
        next_page_token (str):
            A token to retrieve next page of results.
    """

    @property
    def raw_page(self):
        return self

    datasets: MutableSequence[gcd_dataset.Dataset] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcd_dataset.Dataset,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteDatasetRequest(proto.Message):
    r"""Request message for DeleteDataset.

    Attributes:
        name (str):
            Required. Dataset resource name, format:
            projects/{project_id}/datasets/{dataset_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ImportDataRequest(proto.Message):
    r"""Request message for ImportData API.

    Attributes:
        name (str):
            Required. Dataset resource name, format:
            projects/{project_id}/datasets/{dataset_id}
        input_config (google.cloud.datalabeling_v1beta1.types.InputConfig):
            Required. Specify the input source of the
            data.
        user_email_address (str):
            Email of the user who started the import task
            and should be notified by email. If empty no
            notification will be sent.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    input_config: gcd_dataset.InputConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcd_dataset.InputConfig,
    )
    user_email_address: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ExportDataRequest(proto.Message):
    r"""Request message for ExportData API.

    Attributes:
        name (str):
            Required. Dataset resource name, format:
            projects/{project_id}/datasets/{dataset_id}
        annotated_dataset (str):
            Required. Annotated dataset resource name. DataItem in
            Dataset and their annotations in specified annotated dataset
            will be exported. It's in format of
            projects/{project_id}/datasets/{dataset_id}/annotatedDatasets/
            {annotated_dataset_id}
        filter (str):
            Optional. Filter is not supported at this
            moment.
        output_config (google.cloud.datalabeling_v1beta1.types.OutputConfig):
            Required. Specify the output destination.
        user_email_address (str):
            Email of the user who started the export task
            and should be notified by email. If empty no
            notification will be sent.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    annotated_dataset: str = proto.Field(
        proto.STRING,
        number=2,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=3,
    )
    output_config: gcd_dataset.OutputConfig = proto.Field(
        proto.MESSAGE,
        number=4,
        message=gcd_dataset.OutputConfig,
    )
    user_email_address: str = proto.Field(
        proto.STRING,
        number=5,
    )


class GetDataItemRequest(proto.Message):
    r"""Request message for GetDataItem.

    Attributes:
        name (str):
            Required. The name of the data item to get, format:
            projects/{project_id}/datasets/{dataset_id}/dataItems/{data_item_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDataItemsRequest(proto.Message):
    r"""Request message for ListDataItems.

    Attributes:
        parent (str):
            Required. Name of the dataset to list data items, format:
            projects/{project_id}/datasets/{dataset_id}
        filter (str):
            Optional. Filter is not supported at this
            moment.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer results than requested. Default
            value is 100.
        page_token (str):
            Optional. A token identifying a page of results for the
            server to return. Typically obtained by
            [ListDataItemsResponse.next_page_token][google.cloud.datalabeling.v1beta1.ListDataItemsResponse.next_page_token]
            of the previous [DataLabelingService.ListDataItems] call.
            Return first page if empty.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListDataItemsResponse(proto.Message):
    r"""Results of listing data items in a dataset.

    Attributes:
        data_items (MutableSequence[google.cloud.datalabeling_v1beta1.types.DataItem]):
            The list of data items to return.
        next_page_token (str):
            A token to retrieve next page of results.
    """

    @property
    def raw_page(self):
        return self

    data_items: MutableSequence[gcd_dataset.DataItem] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcd_dataset.DataItem,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetAnnotatedDatasetRequest(proto.Message):
    r"""Request message for GetAnnotatedDataset.

    Attributes:
        name (str):
            Required. Name of the annotated dataset to get, format:
            projects/{project_id}/datasets/{dataset_id}/annotatedDatasets/
            {annotated_dataset_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAnnotatedDatasetsRequest(proto.Message):
    r"""Request message for ListAnnotatedDatasets.

    Attributes:
        parent (str):
            Required. Name of the dataset to list annotated datasets,
            format: projects/{project_id}/datasets/{dataset_id}
        filter (str):
            Optional. Filter is not supported at this
            moment.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer results than requested. Default
            value is 100.
        page_token (str):
            Optional. A token identifying a page of results for the
            server to return. Typically obtained by
            [ListAnnotatedDatasetsResponse.next_page_token][google.cloud.datalabeling.v1beta1.ListAnnotatedDatasetsResponse.next_page_token]
            of the previous [DataLabelingService.ListAnnotatedDatasets]
            call. Return first page if empty.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListAnnotatedDatasetsResponse(proto.Message):
    r"""Results of listing annotated datasets for a dataset.

    Attributes:
        annotated_datasets (MutableSequence[google.cloud.datalabeling_v1beta1.types.AnnotatedDataset]):
            The list of annotated datasets to return.
        next_page_token (str):
            A token to retrieve next page of results.
    """

    @property
    def raw_page(self):
        return self

    annotated_datasets: MutableSequence[gcd_dataset.AnnotatedDataset] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=gcd_dataset.AnnotatedDataset,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteAnnotatedDatasetRequest(proto.Message):
    r"""Request message for DeleteAnnotatedDataset.

    Attributes:
        name (str):
            Required. Name of the annotated dataset to delete, format:
            projects/{project_id}/datasets/{dataset_id}/annotatedDatasets/
            {annotated_dataset_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class LabelImageRequest(proto.Message):
    r"""Request message for starting an image labeling task.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        image_classification_config (google.cloud.datalabeling_v1beta1.types.ImageClassificationConfig):
            Configuration for image classification task. One of
            image_classification_config, bounding_poly_config,
            polyline_config and segmentation_config are required.

            This field is a member of `oneof`_ ``request_config``.
        bounding_poly_config (google.cloud.datalabeling_v1beta1.types.BoundingPolyConfig):
            Configuration for bounding box and bounding poly task. One
            of image_classification_config, bounding_poly_config,
            polyline_config and segmentation_config are required.

            This field is a member of `oneof`_ ``request_config``.
        polyline_config (google.cloud.datalabeling_v1beta1.types.PolylineConfig):
            Configuration for polyline task. One of
            image_classification_config, bounding_poly_config,
            polyline_config and segmentation_config are required.

            This field is a member of `oneof`_ ``request_config``.
        segmentation_config (google.cloud.datalabeling_v1beta1.types.SegmentationConfig):
            Configuration for segmentation task. One of
            image_classification_config, bounding_poly_config,
            polyline_config and segmentation_config are required.

            This field is a member of `oneof`_ ``request_config``.
        parent (str):
            Required. Name of the dataset to request labeling task,
            format: projects/{project_id}/datasets/{dataset_id}
        basic_config (google.cloud.datalabeling_v1beta1.types.HumanAnnotationConfig):
            Required. Basic human annotation config.
        feature (google.cloud.datalabeling_v1beta1.types.LabelImageRequest.Feature):
            Required. The type of image labeling task.
    """

    class Feature(proto.Enum):
        r"""Image labeling task feature.

        Values:
            FEATURE_UNSPECIFIED (0):
                No description available.
            CLASSIFICATION (1):
                Label whole image with one or more of labels.
            BOUNDING_BOX (2):
                Label image with bounding boxes for labels.
            ORIENTED_BOUNDING_BOX (6):
                Label oriented bounding box. The box does not
                have to be parallel to horizontal line.
            BOUNDING_POLY (3):
                Label images with bounding poly. A bounding
                poly is a plane figure that is bounded by a
                finite chain of straight line segments closing
                in a loop.
            POLYLINE (4):
                Label images with polyline. Polyline is
                formed by connected line segments which are not
                in closed form.
            SEGMENTATION (5):
                Label images with segmentation. Segmentation
                is different from bounding poly since it is more
                fine-grained, pixel level annotation.
        """

        FEATURE_UNSPECIFIED = 0
        CLASSIFICATION = 1
        BOUNDING_BOX = 2
        ORIENTED_BOUNDING_BOX = 6
        BOUNDING_POLY = 3
        POLYLINE = 4
        SEGMENTATION = 5

    image_classification_config: human_annotation_config.ImageClassificationConfig = (
        proto.Field(
            proto.MESSAGE,
            number=4,
            oneof="request_config",
            message=human_annotation_config.ImageClassificationConfig,
        )
    )
    bounding_poly_config: human_annotation_config.BoundingPolyConfig = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="request_config",
        message=human_annotation_config.BoundingPolyConfig,
    )
    polyline_config: human_annotation_config.PolylineConfig = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="request_config",
        message=human_annotation_config.PolylineConfig,
    )
    segmentation_config: human_annotation_config.SegmentationConfig = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="request_config",
        message=human_annotation_config.SegmentationConfig,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    basic_config: human_annotation_config.HumanAnnotationConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=human_annotation_config.HumanAnnotationConfig,
    )
    feature: Feature = proto.Field(
        proto.ENUM,
        number=3,
        enum=Feature,
    )


class LabelVideoRequest(proto.Message):
    r"""Request message for LabelVideo.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        video_classification_config (google.cloud.datalabeling_v1beta1.types.VideoClassificationConfig):
            Configuration for video classification task. One of
            video_classification_config, object_detection_config,
            object_tracking_config and event_config is required.

            This field is a member of `oneof`_ ``request_config``.
        object_detection_config (google.cloud.datalabeling_v1beta1.types.ObjectDetectionConfig):
            Configuration for video object detection task. One of
            video_classification_config, object_detection_config,
            object_tracking_config and event_config is required.

            This field is a member of `oneof`_ ``request_config``.
        object_tracking_config (google.cloud.datalabeling_v1beta1.types.ObjectTrackingConfig):
            Configuration for video object tracking task. One of
            video_classification_config, object_detection_config,
            object_tracking_config and event_config is required.

            This field is a member of `oneof`_ ``request_config``.
        event_config (google.cloud.datalabeling_v1beta1.types.EventConfig):
            Configuration for video event task. One of
            video_classification_config, object_detection_config,
            object_tracking_config and event_config is required.

            This field is a member of `oneof`_ ``request_config``.
        parent (str):
            Required. Name of the dataset to request labeling task,
            format: projects/{project_id}/datasets/{dataset_id}
        basic_config (google.cloud.datalabeling_v1beta1.types.HumanAnnotationConfig):
            Required. Basic human annotation config.
        feature (google.cloud.datalabeling_v1beta1.types.LabelVideoRequest.Feature):
            Required. The type of video labeling task.
    """

    class Feature(proto.Enum):
        r"""Video labeling task feature.

        Values:
            FEATURE_UNSPECIFIED (0):
                No description available.
            CLASSIFICATION (1):
                Label whole video or video segment with one
                or more labels.
            OBJECT_DETECTION (2):
                Label objects with bounding box on image
                frames extracted from the video.
            OBJECT_TRACKING (3):
                Label and track objects in video.
            EVENT (4):
                Label the range of video for the specified
                events.
        """

        FEATURE_UNSPECIFIED = 0
        CLASSIFICATION = 1
        OBJECT_DETECTION = 2
        OBJECT_TRACKING = 3
        EVENT = 4

    video_classification_config: human_annotation_config.VideoClassificationConfig = (
        proto.Field(
            proto.MESSAGE,
            number=4,
            oneof="request_config",
            message=human_annotation_config.VideoClassificationConfig,
        )
    )
    object_detection_config: human_annotation_config.ObjectDetectionConfig = (
        proto.Field(
            proto.MESSAGE,
            number=5,
            oneof="request_config",
            message=human_annotation_config.ObjectDetectionConfig,
        )
    )
    object_tracking_config: human_annotation_config.ObjectTrackingConfig = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="request_config",
        message=human_annotation_config.ObjectTrackingConfig,
    )
    event_config: human_annotation_config.EventConfig = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="request_config",
        message=human_annotation_config.EventConfig,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    basic_config: human_annotation_config.HumanAnnotationConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=human_annotation_config.HumanAnnotationConfig,
    )
    feature: Feature = proto.Field(
        proto.ENUM,
        number=3,
        enum=Feature,
    )


class LabelTextRequest(proto.Message):
    r"""Request message for LabelText.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text_classification_config (google.cloud.datalabeling_v1beta1.types.TextClassificationConfig):
            Configuration for text classification task. One of
            text_classification_config and text_entity_extraction_config
            is required.

            This field is a member of `oneof`_ ``request_config``.
        text_entity_extraction_config (google.cloud.datalabeling_v1beta1.types.TextEntityExtractionConfig):
            Configuration for entity extraction task. One of
            text_classification_config and text_entity_extraction_config
            is required.

            This field is a member of `oneof`_ ``request_config``.
        parent (str):
            Required. Name of the data set to request labeling task,
            format: projects/{project_id}/datasets/{dataset_id}
        basic_config (google.cloud.datalabeling_v1beta1.types.HumanAnnotationConfig):
            Required. Basic human annotation config.
        feature (google.cloud.datalabeling_v1beta1.types.LabelTextRequest.Feature):
            Required. The type of text labeling task.
    """

    class Feature(proto.Enum):
        r"""Text labeling task feature.

        Values:
            FEATURE_UNSPECIFIED (0):
                No description available.
            TEXT_CLASSIFICATION (1):
                Label text content to one of more labels.
            TEXT_ENTITY_EXTRACTION (2):
                Label entities and their span in text.
        """

        FEATURE_UNSPECIFIED = 0
        TEXT_CLASSIFICATION = 1
        TEXT_ENTITY_EXTRACTION = 2

    text_classification_config: human_annotation_config.TextClassificationConfig = (
        proto.Field(
            proto.MESSAGE,
            number=4,
            oneof="request_config",
            message=human_annotation_config.TextClassificationConfig,
        )
    )
    text_entity_extraction_config: human_annotation_config.TextEntityExtractionConfig = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="request_config",
        message=human_annotation_config.TextEntityExtractionConfig,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    basic_config: human_annotation_config.HumanAnnotationConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=human_annotation_config.HumanAnnotationConfig,
    )
    feature: Feature = proto.Field(
        proto.ENUM,
        number=6,
        enum=Feature,
    )


class GetExampleRequest(proto.Message):
    r"""Request message for GetExample

    Attributes:
        name (str):
            Required. Name of example, format:
            projects/{project_id}/datasets/{dataset_id}/annotatedDatasets/
            {annotated_dataset_id}/examples/{example_id}
        filter (str):
            Optional. An expression for filtering Examples. Filter by
            annotation_spec.display_name is supported. Format
            "annotation_spec.display_name = {display_name}".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListExamplesRequest(proto.Message):
    r"""Request message for ListExamples.

    Attributes:
        parent (str):
            Required. Example resource parent.
        filter (str):
            Optional. An expression for filtering Examples. For
            annotated datasets that have annotation spec set, filter by
            annotation_spec.display_name is supported. Format
            "annotation_spec.display_name = {display_name}".
        page_size (int):
            Optional. Requested page size. Server may
            return fewer results than requested. Default
            value is 100.
        page_token (str):
            Optional. A token identifying a page of results for the
            server to return. Typically obtained by
            [ListExamplesResponse.next_page_token][google.cloud.datalabeling.v1beta1.ListExamplesResponse.next_page_token]
            of the previous [DataLabelingService.ListExamples] call.
            Return first page if empty.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListExamplesResponse(proto.Message):
    r"""Results of listing Examples in and annotated dataset.

    Attributes:
        examples (MutableSequence[google.cloud.datalabeling_v1beta1.types.Example]):
            The list of examples to return.
        next_page_token (str):
            A token to retrieve next page of results.
    """

    @property
    def raw_page(self):
        return self

    examples: MutableSequence[gcd_dataset.Example] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcd_dataset.Example,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateAnnotationSpecSetRequest(proto.Message):
    r"""Request message for CreateAnnotationSpecSet.

    Attributes:
        parent (str):
            Required. AnnotationSpecSet resource parent, format:
            projects/{project_id}
        annotation_spec_set (google.cloud.datalabeling_v1beta1.types.AnnotationSpecSet):
            Required. Annotation spec set to create. Annotation specs
            must be included. Only one annotation spec will be accepted
            for annotation specs with same display_name.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    annotation_spec_set: gcd_annotation_spec_set.AnnotationSpecSet = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcd_annotation_spec_set.AnnotationSpecSet,
    )


class GetAnnotationSpecSetRequest(proto.Message):
    r"""Request message for GetAnnotationSpecSet.

    Attributes:
        name (str):
            Required. AnnotationSpecSet resource name, format:
            projects/{project_id}/annotationSpecSets/{annotation_spec_set_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAnnotationSpecSetsRequest(proto.Message):
    r"""Request message for ListAnnotationSpecSets.

    Attributes:
        parent (str):
            Required. Parent of AnnotationSpecSet resource, format:
            projects/{project_id}
        filter (str):
            Optional. Filter is not supported at this
            moment.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer results than requested. Default
            value is 100.
        page_token (str):
            Optional. A token identifying a page of results for the
            server to return. Typically obtained by
            [ListAnnotationSpecSetsResponse.next_page_token][google.cloud.datalabeling.v1beta1.ListAnnotationSpecSetsResponse.next_page_token]
            of the previous [DataLabelingService.ListAnnotationSpecSets]
            call. Return first page if empty.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListAnnotationSpecSetsResponse(proto.Message):
    r"""Results of listing annotation spec set under a project.

    Attributes:
        annotation_spec_sets (MutableSequence[google.cloud.datalabeling_v1beta1.types.AnnotationSpecSet]):
            The list of annotation spec sets.
        next_page_token (str):
            A token to retrieve next page of results.
    """

    @property
    def raw_page(self):
        return self

    annotation_spec_sets: MutableSequence[gcd_annotation_spec_set.AnnotationSpecSet] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=gcd_annotation_spec_set.AnnotationSpecSet,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteAnnotationSpecSetRequest(proto.Message):
    r"""Request message for DeleteAnnotationSpecSet.

    Attributes:
        name (str):
            Required. AnnotationSpec resource name, format:
            ``projects/{project_id}/annotationSpecSets/{annotation_spec_set_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateInstructionRequest(proto.Message):
    r"""Request message for CreateInstruction.

    Attributes:
        parent (str):
            Required. Instruction resource parent, format:
            projects/{project_id}
        instruction (google.cloud.datalabeling_v1beta1.types.Instruction):
            Required. Instruction of how to perform the
            labeling task.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instruction: gcd_instruction.Instruction = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcd_instruction.Instruction,
    )


class GetInstructionRequest(proto.Message):
    r"""Request message for GetInstruction.

    Attributes:
        name (str):
            Required. Instruction resource name, format:
            projects/{project_id}/instructions/{instruction_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteInstructionRequest(proto.Message):
    r"""Request message for DeleteInstruction.

    Attributes:
        name (str):
            Required. Instruction resource name, format:
            projects/{project_id}/instructions/{instruction_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListInstructionsRequest(proto.Message):
    r"""Request message for ListInstructions.

    Attributes:
        parent (str):
            Required. Instruction resource parent, format:
            projects/{project_id}
        filter (str):
            Optional. Filter is not supported at this
            moment.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer results than requested. Default
            value is 100.
        page_token (str):
            Optional. A token identifying a page of results for the
            server to return. Typically obtained by
            [ListInstructionsResponse.next_page_token][google.cloud.datalabeling.v1beta1.ListInstructionsResponse.next_page_token]
            of the previous [DataLabelingService.ListInstructions] call.
            Return first page if empty.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListInstructionsResponse(proto.Message):
    r"""Results of listing instructions under a project.

    Attributes:
        instructions (MutableSequence[google.cloud.datalabeling_v1beta1.types.Instruction]):
            The list of Instructions to return.
        next_page_token (str):
            A token to retrieve next page of results.
    """

    @property
    def raw_page(self):
        return self

    instructions: MutableSequence[gcd_instruction.Instruction] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcd_instruction.Instruction,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetEvaluationRequest(proto.Message):
    r"""Request message for GetEvaluation.

    Attributes:
        name (str):
            Required. Name of the evaluation. Format:

            "projects/{project_id}/datasets/{dataset_id}/evaluations/{evaluation_id}'
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SearchEvaluationsRequest(proto.Message):
    r"""Request message for SearchEvaluation.

    Attributes:
        parent (str):
            Required. Evaluation search parent (project ID). Format:
            "projects/{project_id}".
        filter (str):
            Optional. To search evaluations, you can filter by the
            following:

            - evaluation\_job.evaluation_job_id (the last part of
              [EvaluationJob.name][google.cloud.datalabeling.v1beta1.EvaluationJob.name])
            - evaluation\_job.model_id (the {model_name} portion of
              [EvaluationJob.modelVersion][google.cloud.datalabeling.v1beta1.EvaluationJob.model_version])
            - evaluation\_job.evaluation_job_run_time_start (Minimum
              threshold for the
              [evaluationJobRunTime][google.cloud.datalabeling.v1beta1.Evaluation.evaluation_job_run_time]
              that created the evaluation)
            - evaluation\_job.evaluation_job_run_time_end (Maximum
              threshold for the
              [evaluationJobRunTime][google.cloud.datalabeling.v1beta1.Evaluation.evaluation_job_run_time]
              that created the evaluation)
            - evaluation\_job.job_state
              ([EvaluationJob.state][google.cloud.datalabeling.v1beta1.EvaluationJob.state])
            - annotation\_spec.display_name (the Evaluation contains a
              metric for the annotation spec with this
              [displayName][google.cloud.datalabeling.v1beta1.AnnotationSpec.display_name])

            To filter by multiple critiera, use the ``AND`` operator or
            the ``OR`` operator. The following examples shows a string
            that filters by several critiera:

            "evaluation\ *job.evaluation_job_id = {evaluation_job_id}
            AND evaluation*\ job.model_id = {model_name} AND
            evaluation\ *job.evaluation_job_run_time_start =
            {timestamp_1} AND
            evaluation*\ job.evaluation_job_run_time_end = {timestamp_2}
            AND annotation\_spec.display_name = {display_name}".
        page_size (int):
            Optional. Requested page size. Server may
            return fewer results than requested. Default
            value is 100.
        page_token (str):
            Optional. A token identifying a page of results for the
            server to return. Typically obtained by the
            [nextPageToken][google.cloud.datalabeling.v1beta1.SearchEvaluationsResponse.next_page_token]
            of the response to a previous search request.

            If you don't specify this field, the API call requests the
            first page of the search.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SearchEvaluationsResponse(proto.Message):
    r"""Results of searching evaluations.

    Attributes:
        evaluations (MutableSequence[google.cloud.datalabeling_v1beta1.types.Evaluation]):
            The list of evaluations matching the search.
        next_page_token (str):
            A token to retrieve next page of results.
    """

    @property
    def raw_page(self):
        return self

    evaluations: MutableSequence[evaluation.Evaluation] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=evaluation.Evaluation,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SearchExampleComparisonsRequest(proto.Message):
    r"""Request message of SearchExampleComparisons.

    Attributes:
        parent (str):
            Required. Name of the
            [Evaluation][google.cloud.datalabeling.v1beta1.Evaluation]
            resource to search for example comparisons from. Format:

            "projects/{project_id}/datasets/{dataset_id}/evaluations/{evaluation_id}".
        page_size (int):
            Optional. Requested page size. Server may
            return fewer results than requested. Default
            value is 100.
        page_token (str):
            Optional. A token identifying a page of results for the
            server to return. Typically obtained by the
            [nextPageToken][SearchExampleComparisons.next_page_token] of
            the response to a previous search rquest.

            If you don't specify this field, the API call requests the
            first page of the search.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SearchExampleComparisonsResponse(proto.Message):
    r"""Results of searching example comparisons.

    Attributes:
        example_comparisons (MutableSequence[google.cloud.datalabeling_v1beta1.types.SearchExampleComparisonsResponse.ExampleComparison]):
            A list of example comparisons matching the
            search criteria.
        next_page_token (str):
            A token to retrieve next page of results.
    """

    class ExampleComparison(proto.Message):
        r"""Example comparisons comparing ground truth output and
        predictions for a specific input.

        Attributes:
            ground_truth_example (google.cloud.datalabeling_v1beta1.types.Example):
                The ground truth output for the input.
            model_created_examples (MutableSequence[google.cloud.datalabeling_v1beta1.types.Example]):
                Predictions by the model for the input.
        """

        ground_truth_example: gcd_dataset.Example = proto.Field(
            proto.MESSAGE,
            number=1,
            message=gcd_dataset.Example,
        )
        model_created_examples: MutableSequence[gcd_dataset.Example] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message=gcd_dataset.Example,
            )
        )

    @property
    def raw_page(self):
        return self

    example_comparisons: MutableSequence[ExampleComparison] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=ExampleComparison,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateEvaluationJobRequest(proto.Message):
    r"""Request message for CreateEvaluationJob.

    Attributes:
        parent (str):
            Required. Evaluation job resource parent. Format:
            "projects/{project_id}".
        job (google.cloud.datalabeling_v1beta1.types.EvaluationJob):
            Required. The evaluation job to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    job: gcd_evaluation_job.EvaluationJob = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcd_evaluation_job.EvaluationJob,
    )


class UpdateEvaluationJobRequest(proto.Message):
    r"""Request message for UpdateEvaluationJob.

    Attributes:
        evaluation_job (google.cloud.datalabeling_v1beta1.types.EvaluationJob):
            Required. Evaluation job that is going to be
            updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Mask for which fields to update. You can only
            provide the following fields:

            - ``evaluationJobConfig.humanAnnotationConfig.instruction``
            - ``evaluationJobConfig.exampleCount``
            - ``evaluationJobConfig.exampleSamplePercentage``

            You can provide more than one of these fields by separating
            them with commas.
    """

    evaluation_job: gcd_evaluation_job.EvaluationJob = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcd_evaluation_job.EvaluationJob,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetEvaluationJobRequest(proto.Message):
    r"""Request message for GetEvaluationJob.

    Attributes:
        name (str):
            Required. Name of the evaluation job. Format:

            "projects/{project_id}/evaluationJobs/{evaluation_job_id}".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class PauseEvaluationJobRequest(proto.Message):
    r"""Request message for PauseEvaluationJob.

    Attributes:
        name (str):
            Required. Name of the evaluation job that is going to be
            paused. Format:

            "projects/{project_id}/evaluationJobs/{evaluation_job_id}".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ResumeEvaluationJobRequest(proto.Message):
    r"""Request message ResumeEvaluationJob.

    Attributes:
        name (str):
            Required. Name of the evaluation job that is going to be
            resumed. Format:

            "projects/{project_id}/evaluationJobs/{evaluation_job_id}".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteEvaluationJobRequest(proto.Message):
    r"""Request message DeleteEvaluationJob.

    Attributes:
        name (str):
            Required. Name of the evaluation job that is going to be
            deleted. Format:

            "projects/{project_id}/evaluationJobs/{evaluation_job_id}".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListEvaluationJobsRequest(proto.Message):
    r"""Request message for ListEvaluationJobs.

    Attributes:
        parent (str):
            Required. Evaluation job resource parent. Format:
            "projects/{project_id}".
        filter (str):
            Optional. You can filter the jobs to list by model_id (also
            known as model_name, as described in
            [EvaluationJob.modelVersion][google.cloud.datalabeling.v1beta1.EvaluationJob.model_version])
            or by evaluation job state (as described in
            [EvaluationJob.state][google.cloud.datalabeling.v1beta1.EvaluationJob.state]).
            To filter by both criteria, use the ``AND`` operator or the
            ``OR`` operator. For example, you can use the following
            string for your filter: "evaluation\ *job.model_id =
            {model_name} AND evaluation*\ job.state =
            {evaluation_job_state}".
        page_size (int):
            Optional. Requested page size. Server may
            return fewer results than requested. Default
            value is 100.
        page_token (str):
            Optional. A token identifying a page of results for the
            server to return. Typically obtained by the
            [nextPageToken][google.cloud.datalabeling.v1beta1.ListEvaluationJobsResponse.next_page_token]
            in the response to the previous request. The request returns
            the first page if this is empty.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListEvaluationJobsResponse(proto.Message):
    r"""Results for listing evaluation jobs.

    Attributes:
        evaluation_jobs (MutableSequence[google.cloud.datalabeling_v1beta1.types.EvaluationJob]):
            The list of evaluation jobs to return.
        next_page_token (str):
            A token to retrieve next page of results.
    """

    @property
    def raw_page(self):
        return self

    evaluation_jobs: MutableSequence[gcd_evaluation_job.EvaluationJob] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=gcd_evaluation_job.EvaluationJob,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
