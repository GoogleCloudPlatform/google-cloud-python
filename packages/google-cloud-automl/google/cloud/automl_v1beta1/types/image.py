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

from google.cloud.automl_v1beta1.types import classification

__protobuf__ = proto.module(
    package="google.cloud.automl.v1beta1",
    manifest={
        "ImageClassificationDatasetMetadata",
        "ImageObjectDetectionDatasetMetadata",
        "ImageClassificationModelMetadata",
        "ImageObjectDetectionModelMetadata",
        "ImageClassificationModelDeploymentMetadata",
        "ImageObjectDetectionModelDeploymentMetadata",
    },
)


class ImageClassificationDatasetMetadata(proto.Message):
    r"""Dataset metadata that is specific to image classification.

    Attributes:
        classification_type (google.cloud.automl_v1beta1.types.ClassificationType):
            Required. Type of the classification problem.
    """

    classification_type: classification.ClassificationType = proto.Field(
        proto.ENUM,
        number=1,
        enum=classification.ClassificationType,
    )


class ImageObjectDetectionDatasetMetadata(proto.Message):
    r"""Dataset metadata specific to image object detection."""


class ImageClassificationModelMetadata(proto.Message):
    r"""Model metadata for image classification.

    Attributes:
        base_model_id (str):
            Optional. The ID of the ``base`` model. If it is specified,
            the new model will be created based on the ``base`` model.
            Otherwise, the new model will be created from scratch. The
            ``base`` model must be in the same ``project`` and
            ``location`` as the new model to create, and have the same
            ``model_type``.
        train_budget (int):
            Required. The train budget of creating this model, expressed
            in hours. The actual ``train_cost`` will be equal or less
            than this value.
        train_cost (int):
            Output only. The actual train cost of creating this model,
            expressed in hours. If this model is created from a ``base``
            model, the train cost used to create the ``base`` model are
            not included.
        stop_reason (str):
            Output only. The reason that this create model operation
            stopped, e.g. ``BUDGET_REACHED``, ``MODEL_CONVERGED``.
        model_type (str):
            Optional. Type of the model. The available values are:

            - ``cloud`` - Model to be used via prediction calls to
              AutoML API. This is the default value.
            - ``mobile-low-latency-1`` - A model that, in addition to
              providing prediction via AutoML API, can also be exported
              (see
              [AutoMl.ExportModel][google.cloud.automl.v1beta1.AutoMl.ExportModel])
              and used on a mobile or edge device with TensorFlow
              afterwards. Expected to have low latency, but may have
              lower prediction quality than other models.
            - ``mobile-versatile-1`` - A model that, in addition to
              providing prediction via AutoML API, can also be exported
              (see
              [AutoMl.ExportModel][google.cloud.automl.v1beta1.AutoMl.ExportModel])
              and used on a mobile or edge device with TensorFlow
              afterwards.
            - ``mobile-high-accuracy-1`` - A model that, in addition to
              providing prediction via AutoML API, can also be exported
              (see
              [AutoMl.ExportModel][google.cloud.automl.v1beta1.AutoMl.ExportModel])
              and used on a mobile or edge device with TensorFlow
              afterwards. Expected to have a higher latency, but should
              also have a higher prediction quality than other models.
            - ``mobile-core-ml-low-latency-1`` - A model that, in
              addition to providing prediction via AutoML API, can also
              be exported (see
              [AutoMl.ExportModel][google.cloud.automl.v1beta1.AutoMl.ExportModel])
              and used on a mobile device with Core ML afterwards.
              Expected to have low latency, but may have lower
              prediction quality than other models.
            - ``mobile-core-ml-versatile-1`` - A model that, in addition
              to providing prediction via AutoML API, can also be
              exported (see
              [AutoMl.ExportModel][google.cloud.automl.v1beta1.AutoMl.ExportModel])
              and used on a mobile device with Core ML afterwards.
            - ``mobile-core-ml-high-accuracy-1`` - A model that, in
              addition to providing prediction via AutoML API, can also
              be exported (see
              [AutoMl.ExportModel][google.cloud.automl.v1beta1.AutoMl.ExportModel])
              and used on a mobile device with Core ML afterwards.
              Expected to have a higher latency, but should also have a
              higher prediction quality than other models.
        node_qps (float):
            Output only. An approximate number of online
            prediction QPS that can be supported by this
            model per each node on which it is deployed.
        node_count (int):
            Output only. The number of nodes this model is deployed on.
            A node is an abstraction of a machine resource, which can
            handle online prediction QPS as given in the node_qps field.
    """

    base_model_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    train_budget: int = proto.Field(
        proto.INT64,
        number=2,
    )
    train_cost: int = proto.Field(
        proto.INT64,
        number=3,
    )
    stop_reason: str = proto.Field(
        proto.STRING,
        number=5,
    )
    model_type: str = proto.Field(
        proto.STRING,
        number=7,
    )
    node_qps: float = proto.Field(
        proto.DOUBLE,
        number=13,
    )
    node_count: int = proto.Field(
        proto.INT64,
        number=14,
    )


class ImageObjectDetectionModelMetadata(proto.Message):
    r"""Model metadata specific to image object detection.

    Attributes:
        model_type (str):
            Optional. Type of the model. The available values are:

            - ``cloud-high-accuracy-1`` - (default) A model to be used
              via prediction calls to AutoML API. Expected to have a
              higher latency, but should also have a higher prediction
              quality than other models.
            - ``cloud-low-latency-1`` - A model to be used via
              prediction calls to AutoML API. Expected to have low
              latency, but may have lower prediction quality than other
              models.
            - ``mobile-low-latency-1`` - A model that, in addition to
              providing prediction via AutoML API, can also be exported
              (see
              [AutoMl.ExportModel][google.cloud.automl.v1beta1.AutoMl.ExportModel])
              and used on a mobile or edge device with TensorFlow
              afterwards. Expected to have low latency, but may have
              lower prediction quality than other models.
            - ``mobile-versatile-1`` - A model that, in addition to
              providing prediction via AutoML API, can also be exported
              (see
              [AutoMl.ExportModel][google.cloud.automl.v1beta1.AutoMl.ExportModel])
              and used on a mobile or edge device with TensorFlow
              afterwards.
            - ``mobile-high-accuracy-1`` - A model that, in addition to
              providing prediction via AutoML API, can also be exported
              (see
              [AutoMl.ExportModel][google.cloud.automl.v1beta1.AutoMl.ExportModel])
              and used on a mobile or edge device with TensorFlow
              afterwards. Expected to have a higher latency, but should
              also have a higher prediction quality than other models.
        node_count (int):
            Output only. The number of nodes this model is deployed on.
            A node is an abstraction of a machine resource, which can
            handle online prediction QPS as given in the qps_per_node
            field.
        node_qps (float):
            Output only. An approximate number of online
            prediction QPS that can be supported by this
            model per each node on which it is deployed.
        stop_reason (str):
            Output only. The reason that this create model operation
            stopped, e.g. ``BUDGET_REACHED``, ``MODEL_CONVERGED``.
        train_budget_milli_node_hours (int):
            The train budget of creating this model, expressed in milli
            node hours i.e. 1,000 value in this field means 1 node hour.
            The actual ``train_cost`` will be equal or less than this
            value. If further model training ceases to provide any
            improvements, it will stop without using full budget and the
            stop_reason will be ``MODEL_CONVERGED``. Note, node_hour =
            actual_hour \* number_of_nodes_invovled. For model type
            ``cloud-high-accuracy-1``\ (default) and
            ``cloud-low-latency-1``, the train budget must be between
            20,000 and 900,000 milli node hours, inclusive. The default
            value is 216, 000 which represents one day in wall time. For
            model type ``mobile-low-latency-1``, ``mobile-versatile-1``,
            ``mobile-high-accuracy-1``,
            ``mobile-core-ml-low-latency-1``,
            ``mobile-core-ml-versatile-1``,
            ``mobile-core-ml-high-accuracy-1``, the train budget must be
            between 1,000 and 100,000 milli node hours, inclusive. The
            default value is 24, 000 which represents one day in wall
            time.
        train_cost_milli_node_hours (int):
            Output only. The actual train cost of
            creating this model, expressed in milli node
            hours, i.e. 1,000 value in this field means 1
            node hour. Guaranteed to not exceed the train
            budget.
    """

    model_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    node_count: int = proto.Field(
        proto.INT64,
        number=3,
    )
    node_qps: float = proto.Field(
        proto.DOUBLE,
        number=4,
    )
    stop_reason: str = proto.Field(
        proto.STRING,
        number=5,
    )
    train_budget_milli_node_hours: int = proto.Field(
        proto.INT64,
        number=6,
    )
    train_cost_milli_node_hours: int = proto.Field(
        proto.INT64,
        number=7,
    )


class ImageClassificationModelDeploymentMetadata(proto.Message):
    r"""Model deployment metadata specific to Image Classification.

    Attributes:
        node_count (int):
            Input only. The number of nodes to deploy the model on. A
            node is an abstraction of a machine resource, which can
            handle online prediction QPS as given in the model's

            [node_qps][google.cloud.automl.v1beta1.ImageClassificationModelMetadata.node_qps].
            Must be between 1 and 100, inclusive on both ends.
    """

    node_count: int = proto.Field(
        proto.INT64,
        number=1,
    )


class ImageObjectDetectionModelDeploymentMetadata(proto.Message):
    r"""Model deployment metadata specific to Image Object Detection.

    Attributes:
        node_count (int):
            Input only. The number of nodes to deploy the model on. A
            node is an abstraction of a machine resource, which can
            handle online prediction QPS as given in the model's

            [qps_per_node][google.cloud.automl.v1beta1.ImageObjectDetectionModelMetadata.qps_per_node].
            Must be between 1 and 100, inclusive on both ends.
    """

    node_count: int = proto.Field(
        proto.INT64,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
