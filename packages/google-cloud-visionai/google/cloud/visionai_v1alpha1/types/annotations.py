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

import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.visionai.v1alpha1",
    manifest={
        "StreamAnnotationType",
        "PersonalProtectiveEquipmentDetectionOutput",
        "ObjectDetectionPredictionResult",
        "ImageObjectDetectionPredictionResult",
        "ClassificationPredictionResult",
        "ImageSegmentationPredictionResult",
        "VideoActionRecognitionPredictionResult",
        "VideoObjectTrackingPredictionResult",
        "VideoClassificationPredictionResult",
        "OccupancyCountingPredictionResult",
        "StreamAnnotation",
        "StreamAnnotations",
        "NormalizedPolygon",
        "NormalizedPolyline",
        "NormalizedVertex",
        "AppPlatformMetadata",
        "AppPlatformCloudFunctionRequest",
        "AppPlatformCloudFunctionResponse",
        "AppPlatformEventBody",
    },
)


class StreamAnnotationType(proto.Enum):
    r"""Enum describing all possible types of a stream annotation.

    Values:
        STREAM_ANNOTATION_TYPE_UNSPECIFIED (0):
            Type UNSPECIFIED.
        STREAM_ANNOTATION_TYPE_ACTIVE_ZONE (1):
            active_zone annotation defines a polygon on top of the
            content from an image/video based stream, following
            processing will only focus on the content inside the active
            zone.
        STREAM_ANNOTATION_TYPE_CROSSING_LINE (2):
            crossing_line annotation defines a polyline on top of the
            content from an image/video based Vision AI stream, events
            happening across the line will be captured. For example, the
            counts of people who goes acroos the line in Occupancy
            Analytic Processor.
    """

    STREAM_ANNOTATION_TYPE_UNSPECIFIED = 0
    STREAM_ANNOTATION_TYPE_ACTIVE_ZONE = 1
    STREAM_ANNOTATION_TYPE_CROSSING_LINE = 2


class PersonalProtectiveEquipmentDetectionOutput(proto.Message):
    r"""Output format for Personal Protective Equipment Detection
    Operator.

    Attributes:
        current_time (google.protobuf.timestamp_pb2.Timestamp):
            Current timestamp.
        detected_persons (MutableSequence[google.cloud.visionai_v1alpha1.types.PersonalProtectiveEquipmentDetectionOutput.DetectedPerson]):
            A list of DetectedPersons.
    """

    class PersonEntity(proto.Message):
        r"""The entity info for annotations from person detection
        prediction result.

        Attributes:
            person_entity_id (int):
                Entity id.
        """

        person_entity_id: int = proto.Field(
            proto.INT64,
            number=1,
        )

    class PPEEntity(proto.Message):
        r"""The entity info for annotations from PPE detection prediction
        result.

        Attributes:
            ppe_label_id (int):
                Label id.
            ppe_label_string (str):
                Human readable string of the label (Examples:
                helmet, glove, mask).
            ppe_supercategory_label_string (str):
                Human readable string of the super category label (Examples:
                head_cover, hands_cover, face_cover).
            ppe_entity_id (int):
                Entity id.
        """

        ppe_label_id: int = proto.Field(
            proto.INT64,
            number=1,
        )
        ppe_label_string: str = proto.Field(
            proto.STRING,
            number=2,
        )
        ppe_supercategory_label_string: str = proto.Field(
            proto.STRING,
            number=3,
        )
        ppe_entity_id: int = proto.Field(
            proto.INT64,
            number=4,
        )

    class NormalizedBoundingBox(proto.Message):
        r"""Bounding Box in the normalized coordinates.

        Attributes:
            xmin (float):
                Min in x coordinate.
            ymin (float):
                Min in y coordinate.
            width (float):
                Width of the bounding box.
            height (float):
                Height of the bounding box.
        """

        xmin: float = proto.Field(
            proto.FLOAT,
            number=1,
        )
        ymin: float = proto.Field(
            proto.FLOAT,
            number=2,
        )
        width: float = proto.Field(
            proto.FLOAT,
            number=3,
        )
        height: float = proto.Field(
            proto.FLOAT,
            number=4,
        )

    class PersonIdentifiedBox(proto.Message):
        r"""PersonIdentified box contains the location and the entity
        info of the person.

        Attributes:
            box_id (int):
                An unique id for this box.
            normalized_bounding_box (google.cloud.visionai_v1alpha1.types.PersonalProtectiveEquipmentDetectionOutput.NormalizedBoundingBox):
                Bounding Box in the normalized coordinates.
            confidence_score (float):
                Confidence score associated with this box.
            person_entity (google.cloud.visionai_v1alpha1.types.PersonalProtectiveEquipmentDetectionOutput.PersonEntity):
                Person entity info.
        """

        box_id: int = proto.Field(
            proto.INT64,
            number=1,
        )
        normalized_bounding_box: "PersonalProtectiveEquipmentDetectionOutput.NormalizedBoundingBox" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="PersonalProtectiveEquipmentDetectionOutput.NormalizedBoundingBox",
        )
        confidence_score: float = proto.Field(
            proto.FLOAT,
            number=3,
        )
        person_entity: "PersonalProtectiveEquipmentDetectionOutput.PersonEntity" = (
            proto.Field(
                proto.MESSAGE,
                number=4,
                message="PersonalProtectiveEquipmentDetectionOutput.PersonEntity",
            )
        )

    class PPEIdentifiedBox(proto.Message):
        r"""PPEIdentified box contains the location and the entity info
        of the PPE.

        Attributes:
            box_id (int):
                An unique id for this box.
            normalized_bounding_box (google.cloud.visionai_v1alpha1.types.PersonalProtectiveEquipmentDetectionOutput.NormalizedBoundingBox):
                Bounding Box in the normalized coordinates.
            confidence_score (float):
                Confidence score associated with this box.
            ppe_entity (google.cloud.visionai_v1alpha1.types.PersonalProtectiveEquipmentDetectionOutput.PPEEntity):
                PPE entity info.
        """

        box_id: int = proto.Field(
            proto.INT64,
            number=1,
        )
        normalized_bounding_box: "PersonalProtectiveEquipmentDetectionOutput.NormalizedBoundingBox" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="PersonalProtectiveEquipmentDetectionOutput.NormalizedBoundingBox",
        )
        confidence_score: float = proto.Field(
            proto.FLOAT,
            number=3,
        )
        ppe_entity: "PersonalProtectiveEquipmentDetectionOutput.PPEEntity" = (
            proto.Field(
                proto.MESSAGE,
                number=4,
                message="PersonalProtectiveEquipmentDetectionOutput.PPEEntity",
            )
        )

    class DetectedPerson(proto.Message):
        r"""Detected Person contains the detected person and their
        associated ppes and their protecting information.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            person_id (int):
                The id of detected person.
            detected_person_identified_box (google.cloud.visionai_v1alpha1.types.PersonalProtectiveEquipmentDetectionOutput.PersonIdentifiedBox):
                The info of detected person identified box.
            detected_ppe_identified_boxes (MutableSequence[google.cloud.visionai_v1alpha1.types.PersonalProtectiveEquipmentDetectionOutput.PPEIdentifiedBox]):
                The info of detected person associated ppe
                identified boxes.
            face_coverage_score (float):
                Coverage score for each body part.
                Coverage score for face.

                This field is a member of `oneof`_ ``_face_coverage_score``.
            eyes_coverage_score (float):
                Coverage score for eyes.

                This field is a member of `oneof`_ ``_eyes_coverage_score``.
            head_coverage_score (float):
                Coverage score for head.

                This field is a member of `oneof`_ ``_head_coverage_score``.
            hands_coverage_score (float):
                Coverage score for hands.

                This field is a member of `oneof`_ ``_hands_coverage_score``.
            body_coverage_score (float):
                Coverage score for body.

                This field is a member of `oneof`_ ``_body_coverage_score``.
            feet_coverage_score (float):
                Coverage score for feet.

                This field is a member of `oneof`_ ``_feet_coverage_score``.
        """

        person_id: int = proto.Field(
            proto.INT64,
            number=1,
        )
        detected_person_identified_box: "PersonalProtectiveEquipmentDetectionOutput.PersonIdentifiedBox" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="PersonalProtectiveEquipmentDetectionOutput.PersonIdentifiedBox",
        )
        detected_ppe_identified_boxes: MutableSequence[
            "PersonalProtectiveEquipmentDetectionOutput.PPEIdentifiedBox"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="PersonalProtectiveEquipmentDetectionOutput.PPEIdentifiedBox",
        )
        face_coverage_score: float = proto.Field(
            proto.FLOAT,
            number=4,
            optional=True,
        )
        eyes_coverage_score: float = proto.Field(
            proto.FLOAT,
            number=5,
            optional=True,
        )
        head_coverage_score: float = proto.Field(
            proto.FLOAT,
            number=6,
            optional=True,
        )
        hands_coverage_score: float = proto.Field(
            proto.FLOAT,
            number=7,
            optional=True,
        )
        body_coverage_score: float = proto.Field(
            proto.FLOAT,
            number=8,
            optional=True,
        )
        feet_coverage_score: float = proto.Field(
            proto.FLOAT,
            number=9,
            optional=True,
        )

    current_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    detected_persons: MutableSequence[DetectedPerson] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=DetectedPerson,
    )


class ObjectDetectionPredictionResult(proto.Message):
    r"""Prediction output format for Generic Object Detection.

    Attributes:
        current_time (google.protobuf.timestamp_pb2.Timestamp):
            Current timestamp.
        identified_boxes (MutableSequence[google.cloud.visionai_v1alpha1.types.ObjectDetectionPredictionResult.IdentifiedBox]):
            A list of identified boxes.
    """

    class Entity(proto.Message):
        r"""The entity info for annotations from object detection
        prediction result.

        Attributes:
            label_id (int):
                Label id.
            label_string (str):
                Human readable string of the label.
        """

        label_id: int = proto.Field(
            proto.INT64,
            number=1,
        )
        label_string: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class IdentifiedBox(proto.Message):
        r"""Identified box contains location and the entity of the
        object.

        Attributes:
            box_id (int):
                An unique id for this box.
            normalized_bounding_box (google.cloud.visionai_v1alpha1.types.ObjectDetectionPredictionResult.IdentifiedBox.NormalizedBoundingBox):
                Bounding Box in the normalized coordinates.
            confidence_score (float):
                Confidence score associated with this box.
            entity (google.cloud.visionai_v1alpha1.types.ObjectDetectionPredictionResult.Entity):
                Entity of this box.
        """

        class NormalizedBoundingBox(proto.Message):
            r"""Bounding Box in the normalized coordinates.

            Attributes:
                xmin (float):
                    Min in x coordinate.
                ymin (float):
                    Min in y coordinate.
                width (float):
                    Width of the bounding box.
                height (float):
                    Height of the bounding box.
            """

            xmin: float = proto.Field(
                proto.FLOAT,
                number=1,
            )
            ymin: float = proto.Field(
                proto.FLOAT,
                number=2,
            )
            width: float = proto.Field(
                proto.FLOAT,
                number=3,
            )
            height: float = proto.Field(
                proto.FLOAT,
                number=4,
            )

        box_id: int = proto.Field(
            proto.INT64,
            number=1,
        )
        normalized_bounding_box: "ObjectDetectionPredictionResult.IdentifiedBox.NormalizedBoundingBox" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="ObjectDetectionPredictionResult.IdentifiedBox.NormalizedBoundingBox",
        )
        confidence_score: float = proto.Field(
            proto.FLOAT,
            number=3,
        )
        entity: "ObjectDetectionPredictionResult.Entity" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="ObjectDetectionPredictionResult.Entity",
        )

    current_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    identified_boxes: MutableSequence[IdentifiedBox] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=IdentifiedBox,
    )


class ImageObjectDetectionPredictionResult(proto.Message):
    r"""Prediction output format for Image Object Detection.

    Attributes:
        ids (MutableSequence[int]):
            The resource IDs of the AnnotationSpecs that
            had been identified, ordered by the confidence
            score descendingly. It is the id segment instead
            of full resource name.
        display_names (MutableSequence[str]):
            The display names of the AnnotationSpecs that
            had been identified, order matches the IDs.
        confidences (MutableSequence[float]):
            The Model's confidences in correctness of the
            predicted IDs, higher value means higher
            confidence. Order matches the Ids.
        bboxes (MutableSequence[google.protobuf.struct_pb2.ListValue]):
            Bounding boxes, i.e. the rectangles over the image, that
            pinpoint the found AnnotationSpecs. Given in order that
            matches the IDs. Each bounding box is an array of 4 numbers
            ``xMin``, ``xMax``, ``yMin``, and ``yMax``, which represent
            the extremal coordinates of the box. They are relative to
            the image size, and the point 0,0 is in the top left of the
            image.
    """

    ids: MutableSequence[int] = proto.RepeatedField(
        proto.INT64,
        number=1,
    )
    display_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    confidences: MutableSequence[float] = proto.RepeatedField(
        proto.FLOAT,
        number=3,
    )
    bboxes: MutableSequence[struct_pb2.ListValue] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=struct_pb2.ListValue,
    )


class ClassificationPredictionResult(proto.Message):
    r"""Prediction output format for Image and Text Classification.

    Attributes:
        ids (MutableSequence[int]):
            The resource IDs of the AnnotationSpecs that
            had been identified.
        display_names (MutableSequence[str]):
            The display names of the AnnotationSpecs that
            had been identified, order matches the IDs.
        confidences (MutableSequence[float]):
            The Model's confidences in correctness of the
            predicted IDs, higher value means higher
            confidence. Order matches the Ids.
    """

    ids: MutableSequence[int] = proto.RepeatedField(
        proto.INT64,
        number=1,
    )
    display_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    confidences: MutableSequence[float] = proto.RepeatedField(
        proto.FLOAT,
        number=3,
    )


class ImageSegmentationPredictionResult(proto.Message):
    r"""Prediction output format for Image Segmentation.

    Attributes:
        category_mask (str):
            A PNG image where each pixel in the mask
            represents the category in which the pixel in
            the original image was predicted to belong to.
            The size of this image will be the same as the
            original image. The mapping between the
            AnntoationSpec and the color can be found in
            model's metadata. The model will choose the most
            likely category and if none of the categories
            reach the confidence threshold, the pixel will
            be marked as background.
        confidence_mask (str):
            A one channel image which is encoded as an
            8bit lossless PNG. The size of the image will be
            the same as the original image. For a specific
            pixel, darker color means less confidence in
            correctness of the cateogry in the categoryMask
            for the corresponding pixel. Black means no
            confidence and white means complete confidence.
    """

    category_mask: str = proto.Field(
        proto.STRING,
        number=1,
    )
    confidence_mask: str = proto.Field(
        proto.STRING,
        number=2,
    )


class VideoActionRecognitionPredictionResult(proto.Message):
    r"""Prediction output format for Video Action Recognition.

    Attributes:
        segment_start_time (google.protobuf.timestamp_pb2.Timestamp):
            The beginning, inclusive, of the video's time
            segment in which the actions have been
            identified.
        segment_end_time (google.protobuf.timestamp_pb2.Timestamp):
            The end, inclusive, of the video's time
            segment in which the actions have been
            identified. Particularly, if the end is the same
            as the start, it means the identification
            happens on a specific video frame.
        actions (MutableSequence[google.cloud.visionai_v1alpha1.types.VideoActionRecognitionPredictionResult.IdentifiedAction]):
            All of the actions identified in the time
            range.
    """

    class IdentifiedAction(proto.Message):
        r"""Each IdentifiedAction is one particular identification of an action
        specified with the AnnotationSpec id, display_name and the
        associated confidence score.

        Attributes:
            id (str):
                The resource ID of the AnnotationSpec that
                had been identified.
            display_name (str):
                The display name of the AnnotationSpec that
                had been identified.
            confidence (float):
                The Model's confidence in correction of this
                identification, higher value means higher
                confidence.
        """

        id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        display_name: str = proto.Field(
            proto.STRING,
            number=2,
        )
        confidence: float = proto.Field(
            proto.FLOAT,
            number=3,
        )

    segment_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    segment_end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    actions: MutableSequence[IdentifiedAction] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=IdentifiedAction,
    )


class VideoObjectTrackingPredictionResult(proto.Message):
    r"""Prediction output format for Video Object Tracking.

    Attributes:
        segment_start_time (google.protobuf.timestamp_pb2.Timestamp):
            The beginning, inclusive, of the video's time
            segment in which the current identifications
            happens.
        segment_end_time (google.protobuf.timestamp_pb2.Timestamp):
            The end, inclusive, of the video's time
            segment in which the current identifications
            happen. Particularly, if the end is the same as
            the start, it means the identifications happen
            on a specific video frame.
        objects (MutableSequence[google.cloud.visionai_v1alpha1.types.VideoObjectTrackingPredictionResult.DetectedObject]):
            All of the objects detected in the specified
            time range.
    """

    class BoundingBox(proto.Message):
        r"""Boundingbox for detected object. I.e. the rectangle over the
        video frame pinpointing the found AnnotationSpec. The
        coordinates are relative to the frame size, and the point 0,0 is
        in the top left of the frame.

        Attributes:
            x_min (float):
                The leftmost coordinate of the bounding box.
            x_max (float):
                The rightmost coordinate of the bounding box.
            y_min (float):
                The topmost coordinate of the bounding box.
            y_max (float):
                The bottommost coordinate of the bounding
                box.
        """

        x_min: float = proto.Field(
            proto.FLOAT,
            number=1,
        )
        x_max: float = proto.Field(
            proto.FLOAT,
            number=2,
        )
        y_min: float = proto.Field(
            proto.FLOAT,
            number=3,
        )
        y_max: float = proto.Field(
            proto.FLOAT,
            number=4,
        )

    class DetectedObject(proto.Message):
        r"""Each DetectedObject is one particular identification of an object
        specified with the AnnotationSpec id and display_name, the bounding
        box, the associated confidence score and the corresponding track_id.

        Attributes:
            id (str):
                The resource ID of the AnnotationSpec that
                had been identified.
            display_name (str):
                The display name of the AnnotationSpec that
                had been identified.
            bounding_box (google.cloud.visionai_v1alpha1.types.VideoObjectTrackingPredictionResult.BoundingBox):
                Boundingbox.
            confidence (float):
                The Model's confidence in correction of this
                identification, higher value means higher
                confidence.
            track_id (int):
                The same object may be identified on muitiple frames which
                are typical adjacent. The set of frames where a particular
                object has been detected form a track. This track_id can be
                used to trace down all frames for an detected object.
        """

        id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        display_name: str = proto.Field(
            proto.STRING,
            number=2,
        )
        bounding_box: "VideoObjectTrackingPredictionResult.BoundingBox" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="VideoObjectTrackingPredictionResult.BoundingBox",
        )
        confidence: float = proto.Field(
            proto.FLOAT,
            number=4,
        )
        track_id: int = proto.Field(
            proto.INT64,
            number=5,
        )

    segment_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    segment_end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    objects: MutableSequence[DetectedObject] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=DetectedObject,
    )


class VideoClassificationPredictionResult(proto.Message):
    r"""Prediction output format for Video Classification.

    Attributes:
        segment_start_time (google.protobuf.timestamp_pb2.Timestamp):
            The beginning, inclusive, of the video's time
            segment in which the classifications have been
            identified.
        segment_end_time (google.protobuf.timestamp_pb2.Timestamp):
            The end, inclusive, of the video's time
            segment in which the classifications have been
            identified. Particularly, if the end is the same
            as the start, it means the identification
            happens on a specific video frame.
        classifications (MutableSequence[google.cloud.visionai_v1alpha1.types.VideoClassificationPredictionResult.IdentifiedClassification]):
            All of the classifications identified in the
            time range.
    """

    class IdentifiedClassification(proto.Message):
        r"""Each IdentifiedClassification is one particular identification of an
        classification specified with the AnnotationSpec id and
        display_name, and the associated confidence score.

        Attributes:
            id (str):
                The resource ID of the AnnotationSpec that
                had been identified.
            display_name (str):
                The display name of the AnnotationSpec that
                had been identified.
            confidence (float):
                The Model's confidence in correction of this
                identification, higher value means higher
                confidence.
        """

        id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        display_name: str = proto.Field(
            proto.STRING,
            number=2,
        )
        confidence: float = proto.Field(
            proto.FLOAT,
            number=3,
        )

    segment_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    segment_end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    classifications: MutableSequence[IdentifiedClassification] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=IdentifiedClassification,
    )


class OccupancyCountingPredictionResult(proto.Message):
    r"""The prediction result proto for occupancy counting.

    Attributes:
        current_time (google.protobuf.timestamp_pb2.Timestamp):
            Current timestamp.
        identified_boxes (MutableSequence[google.cloud.visionai_v1alpha1.types.OccupancyCountingPredictionResult.IdentifiedBox]):
            A list of identified boxes.
        stats (google.cloud.visionai_v1alpha1.types.OccupancyCountingPredictionResult.Stats):
            Detection statistics.
        track_info (MutableSequence[google.cloud.visionai_v1alpha1.types.OccupancyCountingPredictionResult.TrackInfo]):
            Track related information. All the tracks
            that are live at this timestamp. It only exists
            if tracking is enabled.
        dwell_time_info (MutableSequence[google.cloud.visionai_v1alpha1.types.OccupancyCountingPredictionResult.DwellTimeInfo]):
            Dwell time related information. All the
            tracks that are live in a given zone with a
            start and end dwell time timestamp
    """

    class Entity(proto.Message):
        r"""The entity info for annotations from occupancy counting
        operator.

        Attributes:
            label_id (int):
                Label id.
            label_string (str):
                Human readable string of the label.
        """

        label_id: int = proto.Field(
            proto.INT64,
            number=1,
        )
        label_string: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class IdentifiedBox(proto.Message):
        r"""Identified box contains location and the entity of the
        object.

        Attributes:
            box_id (int):
                An unique id for this box.
            normalized_bounding_box (google.cloud.visionai_v1alpha1.types.OccupancyCountingPredictionResult.IdentifiedBox.NormalizedBoundingBox):
                Bounding Box in the normalized coordinates.
            score (float):
                Confidence score associated with this box.
            entity (google.cloud.visionai_v1alpha1.types.OccupancyCountingPredictionResult.Entity):
                Entity of this box.
            track_id (int):
                An unique id to identify a track. It should
                be consistent across frames. It only exists if
                tracking is enabled.
        """

        class NormalizedBoundingBox(proto.Message):
            r"""Bounding Box in the normalized coordinates.

            Attributes:
                xmin (float):
                    Min in x coordinate.
                ymin (float):
                    Min in y coordinate.
                width (float):
                    Width of the bounding box.
                height (float):
                    Height of the bounding box.
            """

            xmin: float = proto.Field(
                proto.FLOAT,
                number=1,
            )
            ymin: float = proto.Field(
                proto.FLOAT,
                number=2,
            )
            width: float = proto.Field(
                proto.FLOAT,
                number=3,
            )
            height: float = proto.Field(
                proto.FLOAT,
                number=4,
            )

        box_id: int = proto.Field(
            proto.INT64,
            number=1,
        )
        normalized_bounding_box: "OccupancyCountingPredictionResult.IdentifiedBox.NormalizedBoundingBox" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="OccupancyCountingPredictionResult.IdentifiedBox.NormalizedBoundingBox",
        )
        score: float = proto.Field(
            proto.FLOAT,
            number=3,
        )
        entity: "OccupancyCountingPredictionResult.Entity" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="OccupancyCountingPredictionResult.Entity",
        )
        track_id: int = proto.Field(
            proto.INT64,
            number=5,
        )

    class Stats(proto.Message):
        r"""The statistics info for annotations from occupancy counting
        operator.

        Attributes:
            full_frame_count (MutableSequence[google.cloud.visionai_v1alpha1.types.OccupancyCountingPredictionResult.Stats.ObjectCount]):
                Counts of the full frame.
            crossing_line_counts (MutableSequence[google.cloud.visionai_v1alpha1.types.OccupancyCountingPredictionResult.Stats.CrossingLineCount]):
                Crossing line counts.
            active_zone_counts (MutableSequence[google.cloud.visionai_v1alpha1.types.OccupancyCountingPredictionResult.Stats.ActiveZoneCount]):
                Active zone counts.
        """

        class ObjectCount(proto.Message):
            r"""The object info and instant count for annotations from
            occupancy counting operator.

            Attributes:
                entity (google.cloud.visionai_v1alpha1.types.OccupancyCountingPredictionResult.Entity):
                    Entity of this object.
                count (int):
                    Count of the object.
            """

            entity: "OccupancyCountingPredictionResult.Entity" = proto.Field(
                proto.MESSAGE,
                number=1,
                message="OccupancyCountingPredictionResult.Entity",
            )
            count: int = proto.Field(
                proto.INT32,
                number=2,
            )

        class AccumulatedObjectCount(proto.Message):
            r"""The object info and accumulated count for annotations from
            occupancy counting operator.

            Attributes:
                start_time (google.protobuf.timestamp_pb2.Timestamp):
                    The start time of the accumulated count.
                object_count (google.cloud.visionai_v1alpha1.types.OccupancyCountingPredictionResult.Stats.ObjectCount):
                    The object count for the accumulated count.
            """

            start_time: timestamp_pb2.Timestamp = proto.Field(
                proto.MESSAGE,
                number=1,
                message=timestamp_pb2.Timestamp,
            )
            object_count: "OccupancyCountingPredictionResult.Stats.ObjectCount" = (
                proto.Field(
                    proto.MESSAGE,
                    number=2,
                    message="OccupancyCountingPredictionResult.Stats.ObjectCount",
                )
            )

        class CrossingLineCount(proto.Message):
            r"""Message for Crossing line count.

            Attributes:
                annotation (google.cloud.visionai_v1alpha1.types.StreamAnnotation):
                    Line annotation from the user.
                positive_direction_counts (MutableSequence[google.cloud.visionai_v1alpha1.types.OccupancyCountingPredictionResult.Stats.ObjectCount]):
                    The direction that follows the right hand
                    rule.
                negative_direction_counts (MutableSequence[google.cloud.visionai_v1alpha1.types.OccupancyCountingPredictionResult.Stats.ObjectCount]):
                    The direction that is opposite to the right
                    hand rule.
                accumulated_positive_direction_counts (MutableSequence[google.cloud.visionai_v1alpha1.types.OccupancyCountingPredictionResult.Stats.AccumulatedObjectCount]):
                    The accumulated positive count.
                accumulated_negative_direction_counts (MutableSequence[google.cloud.visionai_v1alpha1.types.OccupancyCountingPredictionResult.Stats.AccumulatedObjectCount]):
                    The accumulated negative count.
            """

            annotation: "StreamAnnotation" = proto.Field(
                proto.MESSAGE,
                number=1,
                message="StreamAnnotation",
            )
            positive_direction_counts: MutableSequence[
                "OccupancyCountingPredictionResult.Stats.ObjectCount"
            ] = proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="OccupancyCountingPredictionResult.Stats.ObjectCount",
            )
            negative_direction_counts: MutableSequence[
                "OccupancyCountingPredictionResult.Stats.ObjectCount"
            ] = proto.RepeatedField(
                proto.MESSAGE,
                number=3,
                message="OccupancyCountingPredictionResult.Stats.ObjectCount",
            )
            accumulated_positive_direction_counts: MutableSequence[
                "OccupancyCountingPredictionResult.Stats.AccumulatedObjectCount"
            ] = proto.RepeatedField(
                proto.MESSAGE,
                number=4,
                message="OccupancyCountingPredictionResult.Stats.AccumulatedObjectCount",
            )
            accumulated_negative_direction_counts: MutableSequence[
                "OccupancyCountingPredictionResult.Stats.AccumulatedObjectCount"
            ] = proto.RepeatedField(
                proto.MESSAGE,
                number=5,
                message="OccupancyCountingPredictionResult.Stats.AccumulatedObjectCount",
            )

        class ActiveZoneCount(proto.Message):
            r"""Message for the active zone count.

            Attributes:
                annotation (google.cloud.visionai_v1alpha1.types.StreamAnnotation):
                    Active zone annotation from the user.
                counts (MutableSequence[google.cloud.visionai_v1alpha1.types.OccupancyCountingPredictionResult.Stats.ObjectCount]):
                    Counts in the zone.
            """

            annotation: "StreamAnnotation" = proto.Field(
                proto.MESSAGE,
                number=1,
                message="StreamAnnotation",
            )
            counts: MutableSequence[
                "OccupancyCountingPredictionResult.Stats.ObjectCount"
            ] = proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="OccupancyCountingPredictionResult.Stats.ObjectCount",
            )

        full_frame_count: MutableSequence[
            "OccupancyCountingPredictionResult.Stats.ObjectCount"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="OccupancyCountingPredictionResult.Stats.ObjectCount",
        )
        crossing_line_counts: MutableSequence[
            "OccupancyCountingPredictionResult.Stats.CrossingLineCount"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="OccupancyCountingPredictionResult.Stats.CrossingLineCount",
        )
        active_zone_counts: MutableSequence[
            "OccupancyCountingPredictionResult.Stats.ActiveZoneCount"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="OccupancyCountingPredictionResult.Stats.ActiveZoneCount",
        )

    class TrackInfo(proto.Message):
        r"""The track info for annotations from occupancy counting
        operator.

        Attributes:
            track_id (str):
                An unique id to identify a track. It should
                be consistent across frames.
            start_time (google.protobuf.timestamp_pb2.Timestamp):
                Start timestamp of this track.
        """

        track_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
        )

    class DwellTimeInfo(proto.Message):
        r"""The dwell time info for annotations from occupancy counting
        operator.

        Attributes:
            track_id (str):
                An unique id to identify a track. It should
                be consistent across frames.
            zone_id (str):
                The unique id for the zone in which the
                object is dwelling/waiting.
            dwell_start_time (google.protobuf.timestamp_pb2.Timestamp):
                The beginning time when a dwelling object has
                been identified in a zone.
            dwell_end_time (google.protobuf.timestamp_pb2.Timestamp):
                The end time when a dwelling object has
                exited in a zone.
        """

        track_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        zone_id: str = proto.Field(
            proto.STRING,
            number=2,
        )
        dwell_start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=3,
            message=timestamp_pb2.Timestamp,
        )
        dwell_end_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=4,
            message=timestamp_pb2.Timestamp,
        )

    current_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    identified_boxes: MutableSequence[IdentifiedBox] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=IdentifiedBox,
    )
    stats: Stats = proto.Field(
        proto.MESSAGE,
        number=3,
        message=Stats,
    )
    track_info: MutableSequence[TrackInfo] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=TrackInfo,
    )
    dwell_time_info: MutableSequence[DwellTimeInfo] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=DwellTimeInfo,
    )


class StreamAnnotation(proto.Message):
    r"""message about annotations about Vision AI stream resource.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        active_zone (google.cloud.visionai_v1alpha1.types.NormalizedPolygon):
            Annotation for type ACTIVE_ZONE

            This field is a member of `oneof`_ ``annotation_payload``.
        crossing_line (google.cloud.visionai_v1alpha1.types.NormalizedPolyline):
            Annotation for type CROSSING_LINE

            This field is a member of `oneof`_ ``annotation_payload``.
        id (str):
            ID of the annotation. It must be unique when
            used in the certain context. For example, all
            the annotations to one input streams of a Vision
            AI application.
        display_name (str):
            User-friendly name for the annotation.
        source_stream (str):
            The Vision AI stream resource name.
        type_ (google.cloud.visionai_v1alpha1.types.StreamAnnotationType):
            The actual type of Annotation.
    """

    active_zone: "NormalizedPolygon" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="annotation_payload",
        message="NormalizedPolygon",
    )
    crossing_line: "NormalizedPolyline" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="annotation_payload",
        message="NormalizedPolyline",
    )
    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    source_stream: str = proto.Field(
        proto.STRING,
        number=3,
    )
    type_: "StreamAnnotationType" = proto.Field(
        proto.ENUM,
        number=4,
        enum="StreamAnnotationType",
    )


class StreamAnnotations(proto.Message):
    r"""A wrapper of repeated StreamAnnotation.

    Attributes:
        stream_annotations (MutableSequence[google.cloud.visionai_v1alpha1.types.StreamAnnotation]):
            Multiple annotations.
    """

    stream_annotations: MutableSequence["StreamAnnotation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="StreamAnnotation",
    )


class NormalizedPolygon(proto.Message):
    r"""Normalized Polygon.

    Attributes:
        normalized_vertices (MutableSequence[google.cloud.visionai_v1alpha1.types.NormalizedVertex]):
            The bounding polygon normalized vertices. Top left corner of
            the image will be [0, 0].
    """

    normalized_vertices: MutableSequence["NormalizedVertex"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="NormalizedVertex",
    )


class NormalizedPolyline(proto.Message):
    r"""Normalized Pplyline, which represents a curve consisting of
    connected straight-line segments.

    Attributes:
        normalized_vertices (MutableSequence[google.cloud.visionai_v1alpha1.types.NormalizedVertex]):
            A sequence of vertices connected by straight
            lines.
    """

    normalized_vertices: MutableSequence["NormalizedVertex"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="NormalizedVertex",
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


class AppPlatformMetadata(proto.Message):
    r"""Message of essential metadata of App Platform.
    This message is usually attached to a certain processor output
    annotation for customer to identify the source of the data.

    Attributes:
        application (str):
            The application resource name.
        instance_id (str):
            The instance resource id. Instance is the
            nested resource of application under collection
            'instances'.
        node (str):
            The node name of the application graph.
        processor (str):
            The referred processor resource name of the
            application node.
    """

    application: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    node: str = proto.Field(
        proto.STRING,
        number=3,
    )
    processor: str = proto.Field(
        proto.STRING,
        number=4,
    )


class AppPlatformCloudFunctionRequest(proto.Message):
    r"""For any cloud function based customer processing logic,
    customer's cloud function is expected to receive
    AppPlatformCloudFunctionRequest as request and send back
    AppPlatformCloudFunctionResponse as response. Message of request
    from AppPlatform to Cloud Function.

    Attributes:
        app_platform_metadata (google.cloud.visionai_v1alpha1.types.AppPlatformMetadata):
            The metadata of the AppPlatform for customer
            to identify the source of the payload.
        annotations (MutableSequence[google.cloud.visionai_v1alpha1.types.AppPlatformCloudFunctionRequest.StructedInputAnnotation]):
            The actual annotations to be processed by the
            customized Cloud Function.
    """

    class StructedInputAnnotation(proto.Message):
        r"""A general annotation message that uses struct format to
        represent different concrete annotation protobufs.

        Attributes:
            ingestion_time_micros (int):
                The ingestion time of the current annotation.
            annotation (google.protobuf.struct_pb2.Struct):
                The struct format of the actual annotation.
        """

        ingestion_time_micros: int = proto.Field(
            proto.INT64,
            number=1,
        )
        annotation: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=2,
            message=struct_pb2.Struct,
        )

    app_platform_metadata: "AppPlatformMetadata" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="AppPlatformMetadata",
    )
    annotations: MutableSequence[StructedInputAnnotation] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=StructedInputAnnotation,
    )


class AppPlatformCloudFunctionResponse(proto.Message):
    r"""Message of the response from customer's Cloud Function to
    AppPlatform.

    Attributes:
        annotations (MutableSequence[google.cloud.visionai_v1alpha1.types.AppPlatformCloudFunctionResponse.StructedOutputAnnotation]):
            The modified annotations that is returned
            back to AppPlatform. If the annotations fields
            are empty, then those annotations will be
            dropped by AppPlatform.
        annotation_passthrough (bool):
            If set to true, AppPlatform will use original
            annotations instead of dropping them, even if it
            is empty in the annotations filed.
        events (MutableSequence[google.cloud.visionai_v1alpha1.types.AppPlatformEventBody]):
            The event notifications that is returned back
            to AppPlatform. Typically it will then be
            configured to be consumed/forwared to a operator
            that handles events, such as Pub/Sub operator.
    """

    class StructedOutputAnnotation(proto.Message):
        r"""A general annotation message that uses struct format to
        represent different concrete annotation protobufs.

        Attributes:
            annotation (google.protobuf.struct_pb2.Struct):
                The struct format of the actual annotation.
        """

        annotation: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=1,
            message=struct_pb2.Struct,
        )

    annotations: MutableSequence[StructedOutputAnnotation] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=StructedOutputAnnotation,
    )
    annotation_passthrough: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    events: MutableSequence["AppPlatformEventBody"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="AppPlatformEventBody",
    )


class AppPlatformEventBody(proto.Message):
    r"""Message of content of appPlatform event

    Attributes:
        event_message (str):
            Human readable string of the event like
            "There are more than 6 people in the scene". or
            "Shelf is empty!".
        payload (google.protobuf.struct_pb2.Struct):
            For the case of Pub/Sub, it will be stored in
            the message attributes. ​​pubsub.proto
        event_id (str):
            User defined Event Id, used to classify event, within a
            delivery interval, events from the same application instance
            with the same id will be de-duplicated & only first one will
            be sent out. Empty event_id will be treated as "".
    """

    event_message: str = proto.Field(
        proto.STRING,
        number=1,
    )
    payload: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Struct,
    )
    event_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
