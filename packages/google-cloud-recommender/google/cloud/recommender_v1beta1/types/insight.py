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
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.recommender.v1beta1",
    manifest={
        "Insight",
        "InsightStateInfo",
        "InsightType",
    },
)


class Insight(proto.Message):
    r"""An insight along with the information used to derive the
    insight. The insight may have associated recommendations as
    well.

    Attributes:
        name (str):
            Name of the insight.
        description (str):
            Free-form human readable summary in English.
            The maximum length is 500 characters.
        target_resources (MutableSequence[str]):
            Fully qualified resource names that this
            insight is targeting.
        insight_subtype (str):
            Insight subtype. Insight content schema will
            be stable for a given subtype.
        content (google.protobuf.struct_pb2.Struct):
            A struct of custom fields to explain the
            insight. Example: "grantedPermissionsCount":
            "1000".
        last_refresh_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp of the latest data used to generate
            the insight.
        observation_period (google.protobuf.duration_pb2.Duration):
            Observation period that led to the insight. The source data
            used to generate the insight ends at last_refresh_time and
            begins at (last_refresh_time - observation_period).
        state_info (google.cloud.recommender_v1beta1.types.InsightStateInfo):
            Information state and metadata.
        category (google.cloud.recommender_v1beta1.types.Insight.Category):
            Category being targeted by the insight.
        severity (google.cloud.recommender_v1beta1.types.Insight.Severity):
            Insight's severity.
        etag (str):
            Fingerprint of the Insight. Provides
            optimistic locking when updating states.
        associated_recommendations (MutableSequence[google.cloud.recommender_v1beta1.types.Insight.RecommendationReference]):
            Recommendations derived from this insight.
    """

    class Category(proto.Enum):
        r"""Insight category.

        Values:
            CATEGORY_UNSPECIFIED (0):
                Unspecified category.
            COST (1):
                The insight is related to cost.
            SECURITY (2):
                The insight is related to security.
            PERFORMANCE (3):
                The insight is related to performance.
            MANAGEABILITY (4):
                This insight is related to manageability.
        """

        CATEGORY_UNSPECIFIED = 0
        COST = 1
        SECURITY = 2
        PERFORMANCE = 3
        MANAGEABILITY = 4

    class Severity(proto.Enum):
        r"""Insight severity levels.

        Values:
            SEVERITY_UNSPECIFIED (0):
                Insight has unspecified severity.
            LOW (1):
                Insight has low severity.
            MEDIUM (2):
                Insight has medium severity.
            HIGH (3):
                Insight has high severity.
            CRITICAL (4):
                Insight has critical severity.
        """

        SEVERITY_UNSPECIFIED = 0
        LOW = 1
        MEDIUM = 2
        HIGH = 3
        CRITICAL = 4

    class RecommendationReference(proto.Message):
        r"""Reference to an associated recommendation.

        Attributes:
            recommendation (str):
                Recommendation resource name, e.g.
                projects/[PROJECT_NUMBER]/locations/[LOCATION]/recommenders/[RECOMMENDER_ID]/recommendations/[RECOMMENDATION_ID]
        """

        recommendation: str = proto.Field(
            proto.STRING,
            number=1,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    target_resources: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=9,
    )
    insight_subtype: str = proto.Field(
        proto.STRING,
        number=10,
    )
    content: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=3,
        message=struct_pb2.Struct,
    )
    last_refresh_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    observation_period: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=5,
        message=duration_pb2.Duration,
    )
    state_info: "InsightStateInfo" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="InsightStateInfo",
    )
    category: Category = proto.Field(
        proto.ENUM,
        number=7,
        enum=Category,
    )
    severity: Severity = proto.Field(
        proto.ENUM,
        number=15,
        enum=Severity,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=11,
    )
    associated_recommendations: MutableSequence[RecommendationReference] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=8,
            message=RecommendationReference,
        )
    )


class InsightStateInfo(proto.Message):
    r"""Information related to insight state.

    Attributes:
        state (google.cloud.recommender_v1beta1.types.InsightStateInfo.State):
            Insight state.
        state_metadata (MutableMapping[str, str]):
            A map of metadata for the state, provided by
            user or automations systems.
    """

    class State(proto.Enum):
        r"""Represents insight state.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state.
            ACTIVE (1):
                Insight is active. Content for ACTIVE
                insights can be updated by Google. ACTIVE
                insights can be marked DISMISSED OR ACCEPTED.
            ACCEPTED (2):
                Some action has been taken based on this
                insight. Insights become accepted when a
                recommendation derived from the insight has been
                marked CLAIMED, SUCCEEDED, or FAILED. ACTIVE
                insights can also be marked ACCEPTED explicitly.
                Content for ACCEPTED insights is immutable.
                ACCEPTED insights can only be marked ACCEPTED
                (which may update state metadata).
            DISMISSED (3):
                Insight is dismissed. Content for DISMISSED
                insights can be updated by Google. DISMISSED
                insights can be marked as ACTIVE.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        ACCEPTED = 2
        DISMISSED = 3

    state: State = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )
    state_metadata: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )


class InsightType(proto.Message):
    r"""The type of insight.

    Attributes:
        name (str):
            The insight_type’s name in format
            insightTypes/{insight_type} eg:
            insightTypes/google.iam.policy.Insight
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
