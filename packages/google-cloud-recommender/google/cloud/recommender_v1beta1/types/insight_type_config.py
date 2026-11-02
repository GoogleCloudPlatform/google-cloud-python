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
    package="google.cloud.recommender.v1beta1",
    manifest={
        "InsightTypeConfig",
        "InsightTypeGenerationConfig",
    },
)


class InsightTypeConfig(proto.Message):
    r"""Configuration for an InsightType.

    Attributes:
        name (str):
            Name of insight type config. Eg,
            projects/[PROJECT_NUMBER]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]/config
        insight_type_generation_config (google.cloud.recommender_v1beta1.types.InsightTypeGenerationConfig):
            InsightTypeGenerationConfig which configures
            the generation of insights for this insight
            type.
        etag (str):
            Fingerprint of the InsightTypeConfig.
            Provides optimistic locking when updating.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Last time when the config was updated.
        revision_id (str):
            Output only. Immutable. The revision ID of
            the config. A new revision is committed whenever
            the config is changed in any way. The format is
            an 8-character hexadecimal string.
        annotations (MutableMapping[str, str]):
            Allows clients to store small amounts of arbitrary data.
            Annotations must follow the Kubernetes syntax. The total
            size of all keys and values combined is limited to 256k. Key
            can have 2 segments: prefix (optional) and name (required),
            separated by a slash (/). Prefix must be a DNS subdomain.
            Name must be 63 characters or less, begin and end with
            alphanumerics, with dashes (-), underscores (\_), dots (.),
            and alphanumerics between.
        display_name (str):
            A user-settable field to provide a
            human-readable name to be used in user
            interfaces.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    insight_type_generation_config: "InsightTypeGenerationConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="InsightTypeGenerationConfig",
    )
    etag: str = proto.Field(
        proto.STRING,
        number=3,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    revision_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=7,
    )


class InsightTypeGenerationConfig(proto.Message):
    r"""A configuration to customize the generation of insights.
    Eg, customizing the lookback period considered when generating a
    insight.

    Attributes:
        params (google.protobuf.struct_pb2.Struct):
            Parameters for this
            InsightTypeGenerationConfig. These configs can
            be used by or are applied to all subtypes.
    """

    params: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=1,
        message=struct_pb2.Struct,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
