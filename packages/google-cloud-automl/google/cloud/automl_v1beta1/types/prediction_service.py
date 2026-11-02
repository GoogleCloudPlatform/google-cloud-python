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

from google.cloud.automl_v1beta1.types import annotation_payload, data_items, io

__protobuf__ = proto.module(
    package="google.cloud.automl.v1beta1",
    manifest={
        "PredictRequest",
        "PredictResponse",
        "BatchPredictRequest",
        "BatchPredictResult",
    },
)


class PredictRequest(proto.Message):
    r"""Request message for
    [PredictionService.Predict][google.cloud.automl.v1beta1.PredictionService.Predict].

    Attributes:
        name (str):
            Required. Name of the model requested to
            serve the prediction.
        payload (google.cloud.automl_v1beta1.types.ExamplePayload):
            Required. Payload to perform a prediction on.
            The payload must match the problem type that the
            model was trained to solve.
        params (MutableMapping[str, str]):
            Additional domain-specific parameters, any string must be up
            to 25000 characters long.

            - For Image Classification:

              ``score_threshold`` - (float) A value from 0.0 to 1.0.
              When the model makes predictions for an image, it will
              only produce results that have at least this confidence
              score. The default is 0.5.

            - For Image Object Detection: ``score_threshold`` - (float)
              When Model detects objects on the image, it will only
              produce bounding boxes which have at least this confidence
              score. Value in 0 to 1 range, default is 0.5.
              ``max_bounding_box_count`` - (int64) No more than this
              number of bounding boxes will be returned in the response.
              Default is 100, the requested value may be limited by
              server.

            - For Tables: feature_importance - (boolean) Whether feature
              importance should be populated in the returned
              TablesAnnotation. The default is false.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    payload: data_items.ExamplePayload = proto.Field(
        proto.MESSAGE,
        number=2,
        message=data_items.ExamplePayload,
    )
    params: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )


class PredictResponse(proto.Message):
    r"""Response message for
    [PredictionService.Predict][google.cloud.automl.v1beta1.PredictionService.Predict].

    Attributes:
        payload (MutableSequence[google.cloud.automl_v1beta1.types.AnnotationPayload]):
            Prediction result.
            Translation and Text Sentiment will return
            precisely one payload.
        preprocessed_input (google.cloud.automl_v1beta1.types.ExamplePayload):
            The preprocessed example that AutoML actually makes
            prediction on. Empty if AutoML does not preprocess the input
            example.

            - For Text Extraction: If the input is a .pdf file, the
              OCR'ed text will be provided in
              [document_text][google.cloud.automl.v1beta1.Document.document_text].
        metadata (MutableMapping[str, str]):
            Additional domain-specific prediction response metadata.

            - For Image Object Detection: ``max_bounding_box_count`` -
              (int64) At most that many bounding boxes per image could
              have been returned.

            - For Text Sentiment: ``sentiment_score`` - (float,
              deprecated) A value between -1 and 1, -1 maps to least
              positive sentiment, while 1 maps to the most positive one
              and the higher the score, the more positive the sentiment
              in the document is. Yet these values are relative to the
              training data, so e.g. if all data was positive then -1
              will be also positive (though the least). The
              sentiment_score shouldn't be confused with "score" or
              "magnitude" from the previous Natural Language Sentiment
              Analysis API.
    """

    payload: MutableSequence[annotation_payload.AnnotationPayload] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=annotation_payload.AnnotationPayload,
        )
    )
    preprocessed_input: data_items.ExamplePayload = proto.Field(
        proto.MESSAGE,
        number=3,
        message=data_items.ExamplePayload,
    )
    metadata: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )


class BatchPredictRequest(proto.Message):
    r"""Request message for
    [PredictionService.BatchPredict][google.cloud.automl.v1beta1.PredictionService.BatchPredict].

    Attributes:
        name (str):
            Required. Name of the model requested to
            serve the batch prediction.
        input_config (google.cloud.automl_v1beta1.types.BatchPredictInputConfig):
            Required. The input configuration for batch
            prediction.
        output_config (google.cloud.automl_v1beta1.types.BatchPredictOutputConfig):
            Required. The Configuration specifying where
            output predictions should be written.
        params (MutableMapping[str, str]):
            Required. Additional domain-specific parameters for the
            predictions, any string must be up to 25000 characters long.

            - For Text Classification:

              ``score_threshold`` - (float) A value from 0.0 to 1.0.
              When the model makes predictions for a text snippet, it
              will only produce results that have at least this
              confidence score. The default is 0.5.

            - For Image Classification:

              ``score_threshold`` - (float) A value from 0.0 to 1.0.
              When the model makes predictions for an image, it will
              only produce results that have at least this confidence
              score. The default is 0.5.

            - For Image Object Detection:

              ``score_threshold`` - (float) When Model detects objects
              on the image, it will only produce bounding boxes which
              have at least this confidence score. Value in 0 to 1
              range, default is 0.5. ``max_bounding_box_count`` -
              (int64) No more than this number of bounding boxes will be
              produced per image. Default is 100, the requested value
              may be limited by server.

            - For Video Classification :

              ``score_threshold`` - (float) A value from 0.0 to 1.0.
              When the model makes predictions for a video, it will only
              produce results that have at least this confidence score.
              The default is 0.5. ``segment_classification`` - (boolean)
              Set to true to request segment-level classification.
              AutoML Video Intelligence returns labels and their
              confidence scores for the entire segment of the video that
              user specified in the request configuration. The default
              is "true". ``shot_classification`` - (boolean) Set to true
              to request shot-level classification. AutoML Video
              Intelligence determines the boundaries for each camera
              shot in the entire segment of the video that user
              specified in the request configuration. AutoML Video
              Intelligence then returns labels and their confidence
              scores for each detected shot, along with the start and
              end time of the shot. WARNING: Model evaluation is not
              done for this classification type, the quality of it
              depends on training data, but there are no metrics
              provided to describe that quality. The default is "false".
              ``1s_interval_classification`` - (boolean) Set to true to
              request classification for a video at one-second
              intervals. AutoML Video Intelligence returns labels and
              their confidence scores for each second of the entire
              segment of the video that user specified in the request
              configuration. WARNING: Model evaluation is not done for
              this classification type, the quality of it depends on
              training data, but there are no metrics provided to
              describe that quality. The default is "false".

            - For Tables:

              feature_importance - (boolean) Whether feature importance
              should be populated in the returned TablesAnnotations. The
              default is false.

            - For Video Object Tracking:

              ``score_threshold`` - (float) When Model detects objects
              on video frames, it will only produce bounding boxes which
              have at least this confidence score. Value in 0 to 1
              range, default is 0.5. ``max_bounding_box_count`` -
              (int64) No more than this number of bounding boxes will be
              returned per frame. Default is 100, the requested value
              may be limited by server. ``min_bounding_box_size`` -
              (float) Only bounding boxes with shortest edge at least
              that long as a relative value of video frame size will be
              returned. Value in 0 to 1 range. Default is 0.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    input_config: io.BatchPredictInputConfig = proto.Field(
        proto.MESSAGE,
        number=3,
        message=io.BatchPredictInputConfig,
    )
    output_config: io.BatchPredictOutputConfig = proto.Field(
        proto.MESSAGE,
        number=4,
        message=io.BatchPredictOutputConfig,
    )
    params: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )


class BatchPredictResult(proto.Message):
    r"""Result of the Batch Predict. This message is returned in
    [response][google.longrunning.Operation.response] of the operation
    returned by the
    [PredictionService.BatchPredict][google.cloud.automl.v1beta1.PredictionService.BatchPredict].

    Attributes:
        metadata (MutableMapping[str, str]):
            Additional domain-specific prediction response metadata.

            - For Image Object Detection: ``max_bounding_box_count`` -
              (int64) At most that many bounding boxes per image could
              have been returned.

            - For Video Object Tracking: ``max_bounding_box_count`` -
              (int64) At most that many bounding boxes per frame could
              have been returned.
    """

    metadata: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
