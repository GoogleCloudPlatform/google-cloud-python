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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.datalabeling_v1beta1.types import annotation_spec_set

__protobuf__ = proto.module(
    package="google.cloud.datalabeling.v1beta1",
    manifest={
        "AnnotationSource",
        "AnnotationSentiment",
        "AnnotationType",
        "Annotation",
        "AnnotationValue",
        "ImageClassificationAnnotation",
        "Vertex",
        "NormalizedVertex",
        "BoundingPoly",
        "NormalizedBoundingPoly",
        "ImageBoundingPolyAnnotation",
        "Polyline",
        "NormalizedPolyline",
        "ImagePolylineAnnotation",
        "ImageSegmentationAnnotation",
        "TextClassificationAnnotation",
        "TextEntityExtractionAnnotation",
        "SequentialSegment",
        "TimeSegment",
        "VideoClassificationAnnotation",
        "ObjectTrackingFrame",
        "VideoObjectTrackingAnnotation",
        "VideoEventAnnotation",
        "AnnotationMetadata",
        "OperatorMetadata",
    },
)


class AnnotationSource(proto.Enum):
    r"""Specifies where the annotation comes from (whether it was
    provided by a human labeler or a different source).

    Values:
        ANNOTATION_SOURCE_UNSPECIFIED (0):
            No description available.
        OPERATOR (3):
            Answer is provided by a human contributor.
    """

    ANNOTATION_SOURCE_UNSPECIFIED = 0
    OPERATOR = 3


class AnnotationSentiment(proto.Enum):
    r"""

    Values:
        ANNOTATION_SENTIMENT_UNSPECIFIED (0):
            No description available.
        NEGATIVE (1):
            This annotation describes negatively about
            the data.
        POSITIVE (2):
            This label describes positively about the
            data.
    """

    ANNOTATION_SENTIMENT_UNSPECIFIED = 0
    NEGATIVE = 1
    POSITIVE = 2


class AnnotationType(proto.Enum):
    r"""

    Values:
        ANNOTATION_TYPE_UNSPECIFIED (0):
            No description available.
        IMAGE_CLASSIFICATION_ANNOTATION (1):
            Classification annotations in an image.
            Allowed for continuous evaluation.
        IMAGE_BOUNDING_BOX_ANNOTATION (2):
            Bounding box annotations in an image. A form
            of image object detection. Allowed for
            continuous evaluation.
        IMAGE_ORIENTED_BOUNDING_BOX_ANNOTATION (13):
            Oriented bounding box. The box does not have
            to be parallel to horizontal line.
        IMAGE_BOUNDING_POLY_ANNOTATION (10):
            Bounding poly annotations in an image.
        IMAGE_POLYLINE_ANNOTATION (11):
            Polyline annotations in an image.
        IMAGE_SEGMENTATION_ANNOTATION (12):
            Segmentation annotations in an image.
        VIDEO_SHOTS_CLASSIFICATION_ANNOTATION (3):
            Classification annotations in video shots.
        VIDEO_OBJECT_TRACKING_ANNOTATION (4):
            Video object tracking annotation.
        VIDEO_OBJECT_DETECTION_ANNOTATION (5):
            Video object detection annotation.
        VIDEO_EVENT_ANNOTATION (6):
            Video event annotation.
        TEXT_CLASSIFICATION_ANNOTATION (8):
            Classification for text. Allowed for
            continuous evaluation.
        TEXT_ENTITY_EXTRACTION_ANNOTATION (9):
            Entity extraction for text.
        GENERAL_CLASSIFICATION_ANNOTATION (14):
            General classification. Allowed for
            continuous evaluation.
    """

    ANNOTATION_TYPE_UNSPECIFIED = 0
    IMAGE_CLASSIFICATION_ANNOTATION = 1
    IMAGE_BOUNDING_BOX_ANNOTATION = 2
    IMAGE_ORIENTED_BOUNDING_BOX_ANNOTATION = 13
    IMAGE_BOUNDING_POLY_ANNOTATION = 10
    IMAGE_POLYLINE_ANNOTATION = 11
    IMAGE_SEGMENTATION_ANNOTATION = 12
    VIDEO_SHOTS_CLASSIFICATION_ANNOTATION = 3
    VIDEO_OBJECT_TRACKING_ANNOTATION = 4
    VIDEO_OBJECT_DETECTION_ANNOTATION = 5
    VIDEO_EVENT_ANNOTATION = 6
    TEXT_CLASSIFICATION_ANNOTATION = 8
    TEXT_ENTITY_EXTRACTION_ANNOTATION = 9
    GENERAL_CLASSIFICATION_ANNOTATION = 14


class Annotation(proto.Message):
    r"""Annotation for Example. Each example may have one or more
    annotations. For example in image classification problem, each
    image might have one or more labels. We call labels binded with
    this image an Annotation.

    Attributes:
        name (str):
            Output only. Unique name of this annotation, format is:

            projects/{project_id}/datasets/{dataset_id}/annotatedDatasets/{annotated_dataset}/examples/{example_id}/annotations/{annotation_id}
        annotation_source (google.cloud.datalabeling_v1beta1.types.AnnotationSource):
            Output only. The source of the annotation.
        annotation_value (google.cloud.datalabeling_v1beta1.types.AnnotationValue):
            Output only. This is the actual annotation
            value, e.g classification, bounding box values
            are stored here.
        annotation_metadata (google.cloud.datalabeling_v1beta1.types.AnnotationMetadata):
            Output only. Annotation metadata, including
            information like votes for labels.
        annotation_sentiment (google.cloud.datalabeling_v1beta1.types.AnnotationSentiment):
            Output only. Sentiment for this annotation.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    annotation_source: "AnnotationSource" = proto.Field(
        proto.ENUM,
        number=2,
        enum="AnnotationSource",
    )
    annotation_value: "AnnotationValue" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AnnotationValue",
    )
    annotation_metadata: "AnnotationMetadata" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="AnnotationMetadata",
    )
    annotation_sentiment: "AnnotationSentiment" = proto.Field(
        proto.ENUM,
        number=6,
        enum="AnnotationSentiment",
    )


class AnnotationValue(proto.Message):
    r"""Annotation value for an example.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        image_classification_annotation (google.cloud.datalabeling_v1beta1.types.ImageClassificationAnnotation):
            Annotation value for image classification
            case.

            This field is a member of `oneof`_ ``value_type``.
        image_bounding_poly_annotation (google.cloud.datalabeling_v1beta1.types.ImageBoundingPolyAnnotation):
            Annotation value for image bounding box,
            oriented bounding box and polygon cases.

            This field is a member of `oneof`_ ``value_type``.
        image_polyline_annotation (google.cloud.datalabeling_v1beta1.types.ImagePolylineAnnotation):
            Annotation value for image polyline cases.
            Polyline here is different from BoundingPoly. It
            is formed by line segments connected to each
            other but not closed form(Bounding Poly). The
            line segments can cross each other.

            This field is a member of `oneof`_ ``value_type``.
        image_segmentation_annotation (google.cloud.datalabeling_v1beta1.types.ImageSegmentationAnnotation):
            Annotation value for image segmentation.

            This field is a member of `oneof`_ ``value_type``.
        text_classification_annotation (google.cloud.datalabeling_v1beta1.types.TextClassificationAnnotation):
            Annotation value for text classification
            case.

            This field is a member of `oneof`_ ``value_type``.
        text_entity_extraction_annotation (google.cloud.datalabeling_v1beta1.types.TextEntityExtractionAnnotation):
            Annotation value for text entity extraction
            case.

            This field is a member of `oneof`_ ``value_type``.
        video_classification_annotation (google.cloud.datalabeling_v1beta1.types.VideoClassificationAnnotation):
            Annotation value for video classification
            case.

            This field is a member of `oneof`_ ``value_type``.
        video_object_tracking_annotation (google.cloud.datalabeling_v1beta1.types.VideoObjectTrackingAnnotation):
            Annotation value for video object detection
            and tracking case.

            This field is a member of `oneof`_ ``value_type``.
        video_event_annotation (google.cloud.datalabeling_v1beta1.types.VideoEventAnnotation):
            Annotation value for video event case.

            This field is a member of `oneof`_ ``value_type``.
    """

    image_classification_annotation: "ImageClassificationAnnotation" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="value_type",
        message="ImageClassificationAnnotation",
    )
    image_bounding_poly_annotation: "ImageBoundingPolyAnnotation" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="value_type",
        message="ImageBoundingPolyAnnotation",
    )
    image_polyline_annotation: "ImagePolylineAnnotation" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="value_type",
        message="ImagePolylineAnnotation",
    )
    image_segmentation_annotation: "ImageSegmentationAnnotation" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="value_type",
        message="ImageSegmentationAnnotation",
    )
    text_classification_annotation: "TextClassificationAnnotation" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="value_type",
        message="TextClassificationAnnotation",
    )
    text_entity_extraction_annotation: "TextEntityExtractionAnnotation" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="value_type",
        message="TextEntityExtractionAnnotation",
    )
    video_classification_annotation: "VideoClassificationAnnotation" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="value_type",
        message="VideoClassificationAnnotation",
    )
    video_object_tracking_annotation: "VideoObjectTrackingAnnotation" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="value_type",
        message="VideoObjectTrackingAnnotation",
    )
    video_event_annotation: "VideoEventAnnotation" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="value_type",
        message="VideoEventAnnotation",
    )


class ImageClassificationAnnotation(proto.Message):
    r"""Image classification annotation definition.

    Attributes:
        annotation_spec (google.cloud.datalabeling_v1beta1.types.AnnotationSpec):
            Label of image.
    """

    annotation_spec: annotation_spec_set.AnnotationSpec = proto.Field(
        proto.MESSAGE,
        number=1,
        message=annotation_spec_set.AnnotationSpec,
    )


class Vertex(proto.Message):
    r"""A vertex represents a 2D point in the image.
    NOTE: the vertex coordinates are in the same scale as the
    original image.

    Attributes:
        x (int):
            X coordinate.
        y (int):
            Y coordinate.
    """

    x: int = proto.Field(
        proto.INT32,
        number=1,
    )
    y: int = proto.Field(
        proto.INT32,
        number=2,
    )


class NormalizedVertex(proto.Message):
    r"""A vertex represents a 2D point in the image.
    NOTE: the normalized vertex coordinates are relative to the
    original image and range from 0 to 1.

    Attributes:
        x (float):
            X coordinate.
        y (float):
            Y coordinate.
    """

    x: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    y: float = proto.Field(
        proto.FLOAT,
        number=2,
    )


class BoundingPoly(proto.Message):
    r"""A bounding polygon in the image.

    Attributes:
        vertices (MutableSequence[google.cloud.datalabeling_v1beta1.types.Vertex]):
            The bounding polygon vertices.
    """

    vertices: MutableSequence["Vertex"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Vertex",
    )


class NormalizedBoundingPoly(proto.Message):
    r"""Normalized bounding polygon.

    Attributes:
        normalized_vertices (MutableSequence[google.cloud.datalabeling_v1beta1.types.NormalizedVertex]):
            The bounding polygon normalized vertices.
    """

    normalized_vertices: MutableSequence["NormalizedVertex"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="NormalizedVertex",
    )


class ImageBoundingPolyAnnotation(proto.Message):
    r"""Image bounding poly annotation. It represents a polygon
    including bounding box in the image.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        bounding_poly (google.cloud.datalabeling_v1beta1.types.BoundingPoly):

            This field is a member of `oneof`_ ``bounded_area``.
        normalized_bounding_poly (google.cloud.datalabeling_v1beta1.types.NormalizedBoundingPoly):

            This field is a member of `oneof`_ ``bounded_area``.
        annotation_spec (google.cloud.datalabeling_v1beta1.types.AnnotationSpec):
            Label of object in this bounding polygon.
    """

    bounding_poly: "BoundingPoly" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="bounded_area",
        message="BoundingPoly",
    )
    normalized_bounding_poly: "NormalizedBoundingPoly" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="bounded_area",
        message="NormalizedBoundingPoly",
    )
    annotation_spec: annotation_spec_set.AnnotationSpec = proto.Field(
        proto.MESSAGE,
        number=1,
        message=annotation_spec_set.AnnotationSpec,
    )


class Polyline(proto.Message):
    r"""A line with multiple line segments.

    Attributes:
        vertices (MutableSequence[google.cloud.datalabeling_v1beta1.types.Vertex]):
            The polyline vertices.
    """

    vertices: MutableSequence["Vertex"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Vertex",
    )


class NormalizedPolyline(proto.Message):
    r"""Normalized polyline.

    Attributes:
        normalized_vertices (MutableSequence[google.cloud.datalabeling_v1beta1.types.NormalizedVertex]):
            The normalized polyline vertices.
    """

    normalized_vertices: MutableSequence["NormalizedVertex"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="NormalizedVertex",
    )


class ImagePolylineAnnotation(proto.Message):
    r"""A polyline for the image annotation.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        polyline (google.cloud.datalabeling_v1beta1.types.Polyline):

            This field is a member of `oneof`_ ``poly``.
        normalized_polyline (google.cloud.datalabeling_v1beta1.types.NormalizedPolyline):

            This field is a member of `oneof`_ ``poly``.
        annotation_spec (google.cloud.datalabeling_v1beta1.types.AnnotationSpec):
            Label of this polyline.
    """

    polyline: "Polyline" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="poly",
        message="Polyline",
    )
    normalized_polyline: "NormalizedPolyline" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="poly",
        message="NormalizedPolyline",
    )
    annotation_spec: annotation_spec_set.AnnotationSpec = proto.Field(
        proto.MESSAGE,
        number=1,
        message=annotation_spec_set.AnnotationSpec,
    )


class ImageSegmentationAnnotation(proto.Message):
    r"""Image segmentation annotation.

    Attributes:
        annotation_colors (MutableMapping[str, google.cloud.datalabeling_v1beta1.types.AnnotationSpec]):
            The mapping between rgb color and annotation
            spec. The key is the rgb color represented in
            format of rgb(0, 0, 0). The value is the
            AnnotationSpec.
        mime_type (str):
            Image format.
        image_bytes (bytes):
            A byte string of a full image's color map.
    """

    annotation_colors: MutableMapping[str, annotation_spec_set.AnnotationSpec] = (
        proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=1,
            message=annotation_spec_set.AnnotationSpec,
        )
    )
    mime_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    image_bytes: bytes = proto.Field(
        proto.BYTES,
        number=3,
    )


class TextClassificationAnnotation(proto.Message):
    r"""Text classification annotation.

    Attributes:
        annotation_spec (google.cloud.datalabeling_v1beta1.types.AnnotationSpec):
            Label of the text.
    """

    annotation_spec: annotation_spec_set.AnnotationSpec = proto.Field(
        proto.MESSAGE,
        number=1,
        message=annotation_spec_set.AnnotationSpec,
    )


class TextEntityExtractionAnnotation(proto.Message):
    r"""Text entity extraction annotation.

    Attributes:
        annotation_spec (google.cloud.datalabeling_v1beta1.types.AnnotationSpec):
            Label of the text entities.
        sequential_segment (google.cloud.datalabeling_v1beta1.types.SequentialSegment):
            Position of the entity.
    """

    annotation_spec: annotation_spec_set.AnnotationSpec = proto.Field(
        proto.MESSAGE,
        number=1,
        message=annotation_spec_set.AnnotationSpec,
    )
    sequential_segment: "SequentialSegment" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="SequentialSegment",
    )


class SequentialSegment(proto.Message):
    r"""Start and end position in a sequence (e.g. text segment).

    Attributes:
        start (int):
            Start position (inclusive).
        end (int):
            End position (exclusive).
    """

    start: int = proto.Field(
        proto.INT32,
        number=1,
    )
    end: int = proto.Field(
        proto.INT32,
        number=2,
    )


class TimeSegment(proto.Message):
    r"""A time period inside of an example that has a time dimension
    (e.g. video).

    Attributes:
        start_time_offset (google.protobuf.duration_pb2.Duration):
            Start of the time segment (inclusive),
            represented as the duration since the example
            start.
        end_time_offset (google.protobuf.duration_pb2.Duration):
            End of the time segment (exclusive),
            represented as the duration since the example
            start.
    """

    start_time_offset: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )
    end_time_offset: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )


class VideoClassificationAnnotation(proto.Message):
    r"""Video classification annotation.

    Attributes:
        time_segment (google.cloud.datalabeling_v1beta1.types.TimeSegment):
            The time segment of the video to which the
            annotation applies.
        annotation_spec (google.cloud.datalabeling_v1beta1.types.AnnotationSpec):
            Label of the segment specified by time_segment.
    """

    time_segment: "TimeSegment" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="TimeSegment",
    )
    annotation_spec: annotation_spec_set.AnnotationSpec = proto.Field(
        proto.MESSAGE,
        number=2,
        message=annotation_spec_set.AnnotationSpec,
    )


class ObjectTrackingFrame(proto.Message):
    r"""Video frame level annotation for object detection and
    tracking.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        bounding_poly (google.cloud.datalabeling_v1beta1.types.BoundingPoly):

            This field is a member of `oneof`_ ``bounded_area``.
        normalized_bounding_poly (google.cloud.datalabeling_v1beta1.types.NormalizedBoundingPoly):

            This field is a member of `oneof`_ ``bounded_area``.
        time_offset (google.protobuf.duration_pb2.Duration):
            The time offset of this frame relative to the
            beginning of the video.
    """

    bounding_poly: "BoundingPoly" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="bounded_area",
        message="BoundingPoly",
    )
    normalized_bounding_poly: "NormalizedBoundingPoly" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="bounded_area",
        message="NormalizedBoundingPoly",
    )
    time_offset: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )


class VideoObjectTrackingAnnotation(proto.Message):
    r"""Video object tracking annotation.

    Attributes:
        annotation_spec (google.cloud.datalabeling_v1beta1.types.AnnotationSpec):
            Label of the object tracked in this
            annotation.
        time_segment (google.cloud.datalabeling_v1beta1.types.TimeSegment):
            The time segment of the video to which object
            tracking applies.
        object_tracking_frames (MutableSequence[google.cloud.datalabeling_v1beta1.types.ObjectTrackingFrame]):
            The list of frames where this object track
            appears.
    """

    annotation_spec: annotation_spec_set.AnnotationSpec = proto.Field(
        proto.MESSAGE,
        number=1,
        message=annotation_spec_set.AnnotationSpec,
    )
    time_segment: "TimeSegment" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="TimeSegment",
    )
    object_tracking_frames: MutableSequence["ObjectTrackingFrame"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="ObjectTrackingFrame",
        )
    )


class VideoEventAnnotation(proto.Message):
    r"""Video event annotation.

    Attributes:
        annotation_spec (google.cloud.datalabeling_v1beta1.types.AnnotationSpec):
            Label of the event in this annotation.
        time_segment (google.cloud.datalabeling_v1beta1.types.TimeSegment):
            The time segment of the video to which the
            annotation applies.
    """

    annotation_spec: annotation_spec_set.AnnotationSpec = proto.Field(
        proto.MESSAGE,
        number=1,
        message=annotation_spec_set.AnnotationSpec,
    )
    time_segment: "TimeSegment" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="TimeSegment",
    )


class AnnotationMetadata(proto.Message):
    r"""Additional information associated with the annotation.

    Attributes:
        operator_metadata (google.cloud.datalabeling_v1beta1.types.OperatorMetadata):
            Metadata related to human labeling.
    """

    operator_metadata: "OperatorMetadata" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="OperatorMetadata",
    )


class OperatorMetadata(proto.Message):
    r"""General information useful for labels coming from
    contributors.

    Attributes:
        score (float):
            Confidence score corresponding to a label.
            For examle, if 3 contributors have answered the
            question and 2 of them agree on the final label,
            the confidence score will be 0.67 (2/3).
        total_votes (int):
            The total number of contributors that answer
            this question.
        label_votes (int):
            The total number of contributors that choose
            this label.
        comments (MutableSequence[str]):
            Comments from contributors.
    """

    score: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    total_votes: int = proto.Field(
        proto.INT32,
        number=2,
    )
    label_votes: int = proto.Field(
        proto.INT32,
        number=3,
    )
    comments: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
