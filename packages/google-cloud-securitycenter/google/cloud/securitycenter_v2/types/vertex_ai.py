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
        "VertexAi",
    },
)


class VertexAi(proto.Message):
    r"""Vertex AI-related information associated with the finding.

    Attributes:
        datasets (MutableSequence[google.cloud.securitycenter_v2.types.VertexAi.Dataset]):
            Datasets associated with the finding.
        pipelines (MutableSequence[google.cloud.securitycenter_v2.types.VertexAi.Pipeline]):
            Pipelines associated with the finding.
    """

    class Dataset(proto.Message):
        r"""Vertex AI dataset associated with the finding.

        Attributes:
            name (str):
                Resource name of the dataset, e.g.
                projects/{project}/locations/{location}/datasets/2094040236064505856
            display_name (str):
                The user defined display name of dataset,
                e.g. plants-dataset
            source (str):
                Data source, such as a BigQuery source URI,
                e.g. bq://scc-nexus-test.AIPPtest.gsod
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        display_name: str = proto.Field(
            proto.STRING,
            number=2,
        )
        source: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class Pipeline(proto.Message):
        r"""Vertex AI training pipeline associated with the finding.

        Attributes:
            name (str):
                Resource name of the pipeline, e.g.
                projects/{project}/locations/{location}/trainingPipelines/5253428229225578496
            display_name (str):
                The user-defined display name of pipeline,
                e.g. plants-classification
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        display_name: str = proto.Field(
            proto.STRING,
            number=2,
        )

    datasets: MutableSequence[Dataset] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=Dataset,
    )
    pipelines: MutableSequence[Pipeline] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=Pipeline,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
