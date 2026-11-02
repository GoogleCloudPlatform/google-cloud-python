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

__protobuf__ = proto.module(
    package="google.cloud.securitycenter.v2",
    manifest={
        "AiModel",
    },
)


class AiModel(proto.Message):
    r"""Contains information about the AI model associated with the
    finding.

    Attributes:
        name (str):
            The name of the AI model, for example,
            "gemini:1.0.0".
        domain (str):
            The domain of the model, for example,
            “image-classification”.
        library (str):
            The name of the model library, for example,
            “transformers”.
        location (str):
            The region in which the model is used, for
            example, “us-central1”.
        publisher (str):
            The publisher of the model, for example,
            “google” or “nvidia”.
        deployment_platform (google.cloud.securitycenter_v2.types.AiModel.DeploymentPlatform):
            The platform on which the model is deployed.
        display_name (str):
            The user defined display name of model. Ex.
            baseline-classification-model
    """

    class DeploymentPlatform(proto.Enum):
        r"""The platform on which the model is deployed.

        Values:
            DEPLOYMENT_PLATFORM_UNSPECIFIED (0):
                Unspecified deployment platform.
            VERTEX_AI (1):
                Vertex AI.
            GKE (2):
                Google Kubernetes Engine.
            GCE (3):
                Google Compute Engine.
            FINE_TUNED_MODEL (4):
                Fine tuned model.
        """

        DEPLOYMENT_PLATFORM_UNSPECIFIED = 0
        VERTEX_AI = 1
        GKE = 2
        GCE = 3
        FINE_TUNED_MODEL = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    domain: str = proto.Field(
        proto.STRING,
        number=2,
    )
    library: str = proto.Field(
        proto.STRING,
        number=3,
    )
    location: str = proto.Field(
        proto.STRING,
        number=4,
    )
    publisher: str = proto.Field(
        proto.STRING,
        number=5,
    )
    deployment_platform: DeploymentPlatform = proto.Field(
        proto.ENUM,
        number=6,
        enum=DeploymentPlatform,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=7,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
