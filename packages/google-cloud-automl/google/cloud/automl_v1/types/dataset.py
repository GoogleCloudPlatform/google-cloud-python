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

from google.cloud.automl_v1.types import image, text, translation

__protobuf__ = proto.module(
    package="google.cloud.automl.v1",
    manifest={
        "Dataset",
    },
)


class Dataset(proto.Message):
    r"""A workspace for solving a single, particular machine learning
    (ML) problem. A workspace contains examples that may be
    annotated.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        translation_dataset_metadata (google.cloud.automl_v1.types.TranslationDatasetMetadata):
            Metadata for a dataset used for translation.

            This field is a member of `oneof`_ ``dataset_metadata``.
        image_classification_dataset_metadata (google.cloud.automl_v1.types.ImageClassificationDatasetMetadata):
            Metadata for a dataset used for image
            classification.

            This field is a member of `oneof`_ ``dataset_metadata``.
        text_classification_dataset_metadata (google.cloud.automl_v1.types.TextClassificationDatasetMetadata):
            Metadata for a dataset used for text
            classification.

            This field is a member of `oneof`_ ``dataset_metadata``.
        image_object_detection_dataset_metadata (google.cloud.automl_v1.types.ImageObjectDetectionDatasetMetadata):
            Metadata for a dataset used for image object
            detection.

            This field is a member of `oneof`_ ``dataset_metadata``.
        text_extraction_dataset_metadata (google.cloud.automl_v1.types.TextExtractionDatasetMetadata):
            Metadata for a dataset used for text
            extraction.

            This field is a member of `oneof`_ ``dataset_metadata``.
        text_sentiment_dataset_metadata (google.cloud.automl_v1.types.TextSentimentDatasetMetadata):
            Metadata for a dataset used for text
            sentiment.

            This field is a member of `oneof`_ ``dataset_metadata``.
        name (str):
            Output only. The resource name of the dataset. Form:
            ``projects/{project_id}/locations/{location_id}/datasets/{dataset_id}``
        display_name (str):
            Required. The name of the dataset to show in the interface.
            The name can be up to 32 characters long and can consist
            only of ASCII Latin letters A-Z and a-z, underscores (\_),
            and ASCII digits 0-9.
        description (str):
            User-provided description of the dataset. The
            description can be up to 25000 characters long.
        example_count (int):
            Output only. The number of examples in the
            dataset.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp when this dataset was
            created.
        etag (str):
            Used to perform consistent read-modify-write
            updates. If not set, a blind "overwrite" update
            happens.
        labels (MutableMapping[str, str]):
            Optional. The labels with user-defined
            metadata to organize your dataset.
            Label keys and values can be no longer than 64
            characters (Unicode codepoints), can only
            contain lowercase letters, numeric characters,
            underscores and dashes. International characters
            are allowed. Label values are optional. Label
            keys must start with a letter.

            See https://goo.gl/xmQnxf for more information
            on and examples of labels.
    """

    translation_dataset_metadata: translation.TranslationDatasetMetadata = proto.Field(
        proto.MESSAGE,
        number=23,
        oneof="dataset_metadata",
        message=translation.TranslationDatasetMetadata,
    )
    image_classification_dataset_metadata: image.ImageClassificationDatasetMetadata = (
        proto.Field(
            proto.MESSAGE,
            number=24,
            oneof="dataset_metadata",
            message=image.ImageClassificationDatasetMetadata,
        )
    )
    text_classification_dataset_metadata: text.TextClassificationDatasetMetadata = (
        proto.Field(
            proto.MESSAGE,
            number=25,
            oneof="dataset_metadata",
            message=text.TextClassificationDatasetMetadata,
        )
    )
    image_object_detection_dataset_metadata: image.ImageObjectDetectionDatasetMetadata = proto.Field(
        proto.MESSAGE,
        number=26,
        oneof="dataset_metadata",
        message=image.ImageObjectDetectionDatasetMetadata,
    )
    text_extraction_dataset_metadata: text.TextExtractionDatasetMetadata = proto.Field(
        proto.MESSAGE,
        number=28,
        oneof="dataset_metadata",
        message=text.TextExtractionDatasetMetadata,
    )
    text_sentiment_dataset_metadata: text.TextSentimentDatasetMetadata = proto.Field(
        proto.MESSAGE,
        number=30,
        oneof="dataset_metadata",
        message=text.TextSentimentDatasetMetadata,
    )
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
    example_count: int = proto.Field(
        proto.INT32,
        number=21,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=14,
        message=timestamp_pb2.Timestamp,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=17,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=39,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
