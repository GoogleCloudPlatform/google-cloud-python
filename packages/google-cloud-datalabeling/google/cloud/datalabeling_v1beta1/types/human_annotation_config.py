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

__protobuf__ = proto.module(
    package="google.cloud.datalabeling.v1beta1",
    manifest={
        "StringAggregationType",
        "HumanAnnotationConfig",
        "ImageClassificationConfig",
        "BoundingPolyConfig",
        "PolylineConfig",
        "SegmentationConfig",
        "VideoClassificationConfig",
        "ObjectDetectionConfig",
        "ObjectTrackingConfig",
        "EventConfig",
        "TextClassificationConfig",
        "SentimentConfig",
        "TextEntityExtractionConfig",
    },
)


class StringAggregationType(proto.Enum):
    r"""

    Values:
        STRING_AGGREGATION_TYPE_UNSPECIFIED (0):
            No description available.
        MAJORITY_VOTE (1):
            Majority vote to aggregate answers.
        UNANIMOUS_VOTE (2):
            Unanimous answers will be adopted.
        NO_AGGREGATION (3):
            Preserve all answers by crowd compute.
    """

    STRING_AGGREGATION_TYPE_UNSPECIFIED = 0
    MAJORITY_VOTE = 1
    UNANIMOUS_VOTE = 2
    NO_AGGREGATION = 3


class HumanAnnotationConfig(proto.Message):
    r"""Configuration for how human labeling task should be done.

    Attributes:
        instruction (str):
            Required. Instruction resource name.
        annotated_dataset_display_name (str):
            Required. A human-readable name for
            AnnotatedDataset defined by users. Maximum of 64
            characters .
        annotated_dataset_description (str):
            Optional. A human-readable description for
            AnnotatedDataset. The description can be up to
            10000 characters long.
        label_group (str):
            Optional. A human-readable label used to logically group
            labeling tasks. This string must match the regular
            expression ``[a-zA-Z\\d_-]{0,128}``.
        language_code (str):
            Optional. The Language of this question, as a
            `BCP-47 <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>`__.
            Default value is en-US. Only need to set this when task is
            language related. For example, French text classification.
        replica_count (int):
            Optional. Replication of questions. Each
            question will be sent to up to this number of
            contributors to label. Aggregated answers will
            be returned. Default is set to 1.
            For image related labeling, valid values are 1,
            3, 5.
        question_duration (google.protobuf.duration_pb2.Duration):
            Optional. Maximum duration for contributors
            to answer a question. Maximum is 3600 seconds.
            Default is 3600 seconds.
        contributor_emails (MutableSequence[str]):
            Optional. If you want your own labeling
            contributors to manage and work on this labeling
            request, you can set these contributors here. We
            will give them access to the question types in
            crowdcompute. Note that these emails must be
            registered in crowdcompute worker UI:

            https://crowd-compute.appspot.com/
        user_email_address (str):
            Email of the user who started the labeling
            task and should be notified by email. If empty
            no notification will be sent.
    """

    instruction: str = proto.Field(
        proto.STRING,
        number=1,
    )
    annotated_dataset_display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    annotated_dataset_description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    label_group: str = proto.Field(
        proto.STRING,
        number=4,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=5,
    )
    replica_count: int = proto.Field(
        proto.INT32,
        number=6,
    )
    question_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=7,
        message=duration_pb2.Duration,
    )
    contributor_emails: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=9,
    )
    user_email_address: str = proto.Field(
        proto.STRING,
        number=10,
    )


class ImageClassificationConfig(proto.Message):
    r"""Config for image classification human labeling task.

    Attributes:
        annotation_spec_set (str):
            Required. Annotation spec set resource name.
        allow_multi_label (bool):
            Optional. If allow_multi_label is true, contributors are
            able to choose multiple labels for one image.
        answer_aggregation_type (google.cloud.datalabeling_v1beta1.types.StringAggregationType):
            Optional. The type of how to aggregate
            answers.
    """

    annotation_spec_set: str = proto.Field(
        proto.STRING,
        number=1,
    )
    allow_multi_label: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    answer_aggregation_type: "StringAggregationType" = proto.Field(
        proto.ENUM,
        number=3,
        enum="StringAggregationType",
    )


class BoundingPolyConfig(proto.Message):
    r"""Config for image bounding poly (and bounding box) human
    labeling task.

    Attributes:
        annotation_spec_set (str):
            Required. Annotation spec set resource name.
        instruction_message (str):
            Optional. Instruction message showed on
            contributors UI.
    """

    annotation_spec_set: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instruction_message: str = proto.Field(
        proto.STRING,
        number=2,
    )


class PolylineConfig(proto.Message):
    r"""Config for image polyline human labeling task.

    Attributes:
        annotation_spec_set (str):
            Required. Annotation spec set resource name.
        instruction_message (str):
            Optional. Instruction message showed on
            contributors UI.
    """

    annotation_spec_set: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instruction_message: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SegmentationConfig(proto.Message):
    r"""Config for image segmentation

    Attributes:
        annotation_spec_set (str):
            Required. Annotation spec set resource name. format:
            projects/{project_id}/annotationSpecSets/{annotation_spec_set_id}
        instruction_message (str):
            Instruction message showed on labelers UI.
    """

    annotation_spec_set: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instruction_message: str = proto.Field(
        proto.STRING,
        number=2,
    )


class VideoClassificationConfig(proto.Message):
    r"""Config for video classification human labeling task.
    Currently two types of video classification are supported:

    1. Assign labels on the entire video.
    2. Split the video into multiple video clips based on camera
        shot, and assign labels on each video clip.

    Attributes:
        annotation_spec_set_configs (MutableSequence[google.cloud.datalabeling_v1beta1.types.VideoClassificationConfig.AnnotationSpecSetConfig]):
            Required. The list of annotation spec set
            configs. Since watching a video clip takes much
            longer time than an image, we support label with
            multiple AnnotationSpecSet at the same time.
            Labels in each AnnotationSpecSet will be shown
            in a group to contributors. Contributors can
            select one or more (depending on whether to
            allow multi label) from each group.
        apply_shot_detection (bool):
            Optional. Option to apply shot detection on
            the video.
    """

    class AnnotationSpecSetConfig(proto.Message):
        r"""Annotation spec set with the setting of allowing multi labels
        or not.

        Attributes:
            annotation_spec_set (str):
                Required. Annotation spec set resource name.
            allow_multi_label (bool):
                Optional. If allow_multi_label is true, contributors are
                able to choose multiple labels from one annotation spec set.
        """

        annotation_spec_set: str = proto.Field(
            proto.STRING,
            number=1,
        )
        allow_multi_label: bool = proto.Field(
            proto.BOOL,
            number=2,
        )

    annotation_spec_set_configs: MutableSequence[AnnotationSpecSetConfig] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=AnnotationSpecSetConfig,
        )
    )
    apply_shot_detection: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class ObjectDetectionConfig(proto.Message):
    r"""Config for video object detection human labeling task.
    Object detection will be conducted on the images extracted from
    the video, and those objects will be labeled with bounding
    boxes. User need to specify the number of images to be extracted
    per second as the extraction frame rate.

    Attributes:
        annotation_spec_set (str):
            Required. Annotation spec set resource name.
        extraction_frame_rate (float):
            Required. Number of frames per second to be
            extracted from the video.
    """

    annotation_spec_set: str = proto.Field(
        proto.STRING,
        number=1,
    )
    extraction_frame_rate: float = proto.Field(
        proto.DOUBLE,
        number=3,
    )


class ObjectTrackingConfig(proto.Message):
    r"""Config for video object tracking human labeling task.

    Attributes:
        annotation_spec_set (str):
            Required. Annotation spec set resource name.
    """

    annotation_spec_set: str = proto.Field(
        proto.STRING,
        number=1,
    )


class EventConfig(proto.Message):
    r"""Config for video event human labeling task.

    Attributes:
        annotation_spec_sets (MutableSequence[str]):
            Required. The list of annotation spec set
            resource name. Similar to video classification,
            we support selecting event from multiple
            AnnotationSpecSet at the same time.
    """

    annotation_spec_sets: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class TextClassificationConfig(proto.Message):
    r"""Config for text classification human labeling task.

    Attributes:
        allow_multi_label (bool):
            Optional. If allow_multi_label is true, contributors are
            able to choose multiple labels for one text segment.
        annotation_spec_set (str):
            Required. Annotation spec set resource name.
        sentiment_config (google.cloud.datalabeling_v1beta1.types.SentimentConfig):
            Optional. Configs for sentiment selection.
    """

    allow_multi_label: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    annotation_spec_set: str = proto.Field(
        proto.STRING,
        number=2,
    )
    sentiment_config: "SentimentConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="SentimentConfig",
    )


class SentimentConfig(proto.Message):
    r"""Config for setting up sentiments.

    Attributes:
        enable_label_sentiment_selection (bool):
            If set to true, contributors will have the
            option to select sentiment of the label they
            selected, to mark it as negative or positive
            label. Default is false.
    """

    enable_label_sentiment_selection: bool = proto.Field(
        proto.BOOL,
        number=1,
    )


class TextEntityExtractionConfig(proto.Message):
    r"""Config for text entity extraction human labeling task.

    Attributes:
        annotation_spec_set (str):
            Required. Annotation spec set resource name.
    """

    annotation_spec_set: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
