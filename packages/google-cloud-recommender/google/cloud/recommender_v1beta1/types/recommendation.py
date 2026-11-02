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
import google.type.money_pb2 as money_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.recommender.v1beta1",
    manifest={
        "Recommendation",
        "RecommendationContent",
        "OperationGroup",
        "Operation",
        "ValueMatcher",
        "CostProjection",
        "SecurityProjection",
        "SustainabilityProjection",
        "Impact",
        "RecommendationStateInfo",
        "RecommenderType",
    },
)


class Recommendation(proto.Message):
    r"""A recommendation along with a suggested action. E.g., a
    rightsizing recommendation for an underutilized VM, IAM role
    recommendations, etc

    Attributes:
        name (str):
            Name of recommendation.
        description (str):
            Free-form human readable summary in English.
            The maximum length is 500 characters.
        recommender_subtype (str):
            Contains an identifier for a subtype of recommendations
            produced for the same recommender. Subtype is a function of
            content and impact, meaning a new subtype might be added
            when significant changes to ``content`` or
            ``primary_impact.category`` are introduced. See the
            Recommenders section to see a list of subtypes for a given
            Recommender.

            Examples: For recommender = "google.iam.policy.Recommender",
            recommender_subtype can be one of
            "REMOVE_ROLE"/"REPLACE_ROLE".
        last_refresh_time (google.protobuf.timestamp_pb2.Timestamp):
            Last time this recommendation was refreshed
            by the system that created it in the first
            place.
        primary_impact (google.cloud.recommender_v1beta1.types.Impact):
            The primary impact that this recommendation
            can have while trying to optimize for one
            category.
        additional_impact (MutableSequence[google.cloud.recommender_v1beta1.types.Impact]):
            Optional set of additional impact that this
            recommendation may have when trying to optimize
            for the primary category. These may be positive
            or negative.
        priority (google.cloud.recommender_v1beta1.types.Recommendation.Priority):
            Recommendation's priority.
        content (google.cloud.recommender_v1beta1.types.RecommendationContent):
            Content of the recommendation describing
            recommended changes to resources.
        state_info (google.cloud.recommender_v1beta1.types.RecommendationStateInfo):
            Information for state. Contains state and
            metadata.
        etag (str):
            Fingerprint of the Recommendation. Provides
            optimistic locking when updating states.
        associated_insights (MutableSequence[google.cloud.recommender_v1beta1.types.Recommendation.InsightReference]):
            Insights that led to this recommendation.
        xor_group_id (str):
            Corresponds to a mutually exclusive group ID
            within a recommender. A non-empty ID indicates
            that the recommendation belongs to a mutually
            exclusive group. This means that only one
            recommendation within the group is suggested to
            be applied.
    """

    class Priority(proto.Enum):
        r"""Recommendation priority levels.

        Values:
            PRIORITY_UNSPECIFIED (0):
                Recommendation has unspecified priority.
            P4 (1):
                Recommendation has P4 priority (lowest
                priority).
            P3 (2):
                Recommendation has P3 priority (second lowest
                priority).
            P2 (3):
                Recommendation has P2 priority (second
                highest priority).
            P1 (4):
                Recommendation has P1 priority (highest
                priority).
        """

        PRIORITY_UNSPECIFIED = 0
        P4 = 1
        P3 = 2
        P2 = 3
        P1 = 4

    class InsightReference(proto.Message):
        r"""Reference to an associated insight.

        Attributes:
            insight (str):
                Insight resource name, e.g.
                projects/[PROJECT_NUMBER]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]/insights/[INSIGHT_ID]
        """

        insight: str = proto.Field(
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
    recommender_subtype: str = proto.Field(
        proto.STRING,
        number=12,
    )
    last_refresh_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    primary_impact: "Impact" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="Impact",
    )
    additional_impact: MutableSequence["Impact"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="Impact",
    )
    priority: Priority = proto.Field(
        proto.ENUM,
        number=17,
        enum=Priority,
    )
    content: "RecommendationContent" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="RecommendationContent",
    )
    state_info: "RecommendationStateInfo" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="RecommendationStateInfo",
    )
    etag: str = proto.Field(
        proto.STRING,
        number=11,
    )
    associated_insights: MutableSequence[InsightReference] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message=InsightReference,
    )
    xor_group_id: str = proto.Field(
        proto.STRING,
        number=18,
    )


class RecommendationContent(proto.Message):
    r"""Contains what resources are changing and how they are
    changing.

    Attributes:
        operation_groups (MutableSequence[google.cloud.recommender_v1beta1.types.OperationGroup]):
            Operations to one or more Google Cloud
            resources grouped in such a way that, all
            operations within one group are expected to be
            performed atomically and in an order.
        overview (google.protobuf.struct_pb2.Struct):
            Condensed overview information about the
            recommendation.
    """

    operation_groups: MutableSequence["OperationGroup"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="OperationGroup",
    )
    overview: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=3,
        message=struct_pb2.Struct,
    )


class OperationGroup(proto.Message):
    r"""Group of operations that need to be performed atomically.

    Attributes:
        operations (MutableSequence[google.cloud.recommender_v1beta1.types.Operation]):
            List of operations across one or more
            resources that belong to this group. Loosely
            based on RFC6902 and should be performed in the
            order they appear.
    """

    operations: MutableSequence["Operation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Operation",
    )


class Operation(proto.Message):
    r"""Contains an operation for a resource loosely based on the JSON-PATCH
    format with support for:

    - Custom filters for describing partial array patch.
    - Extended path values for describing nested arrays.
    - Custom fields for describing the resource for which the operation
      is being described.
    - Allows extension to custom operations not natively supported by
      RFC6902. See https://tools.ietf.org/html/rfc6902 for details on
      the original RFC.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        action (str):
            Type of this operation. Contains one of
            'add', 'remove', 'replace', 'move', 'copy',
            'test' and 'custom' operations. This field is
            case-insensitive and always populated.
        resource_type (str):
            Type of GCP resource being modified/tested.
            This field is always populated. Example:
            cloudresourcemanager.googleapis.com/Project,
            compute.googleapis.com/Instance
        resource (str):
            Contains the fully qualified resource name.
            This field is always populated. ex:
            //cloudresourcemanager.googleapis.com/projects/foo.
        path (str):
            Path to the target field being operated on.
            If the operation is at the resource level, then
            path should be "/". This field is always
            populated.
        source_resource (str):
            Can be set with action 'copy' to copy resource configuration
            across different resources of the same type. Example: A
            resource clone can be done via action = 'copy', path = "/",
            from = "/", source_resource = and resource_name = . This
            field is empty for all other values of ``action``.
        source_path (str):
            Can be set with action 'copy' or 'move' to indicate the
            source field within resource or source_resource, ignored if
            provided for other operation types.
        value (google.protobuf.struct_pb2.Value):
            Value for the ``path`` field. Will be set for
            actions:'add'/'replace'. Maybe set for action: 'test'.
            Either this or ``value_matcher`` will be set for 'test'
            operation. An exact match must be performed.

            This field is a member of `oneof`_ ``path_value``.
        value_matcher (google.cloud.recommender_v1beta1.types.ValueMatcher):
            Can be set for action 'test' for advanced matching for the
            value of 'path' field. Either this or ``value`` will be set
            for 'test' operation.

            This field is a member of `oneof`_ ``path_value``.
        path_filters (MutableMapping[str, google.protobuf.struct_pb2.Value]):
            Set of filters to apply if ``path`` refers to array elements
            or nested array elements in order to narrow down to a single
            unique element that is being tested/modified. This is
            intended to be an exact match per filter. To perform
            advanced matching, use path_value_matchers.

            - Example:

            ::

               {
                 "/versions/*/name" : "it-123"
                 "/versions/*/targetSize/percent": 20
               }

            - Example:

            ::

               {
                 "/bindings/*/role": "roles/owner"
                 "/bindings/*/condition" : null
               }

            - Example:

            ::

               {
                 "/bindings/*/role": "roles/owner"
                 "/bindings/*/members/*" : ["x@example.com", "y@example.com"]
               }

            When both path_filters and path_value_matchers are set, an
            implicit AND must be performed.
        path_value_matchers (MutableMapping[str, google.cloud.recommender_v1beta1.types.ValueMatcher]):
            Similar to path_filters, this contains set of filters to
            apply if ``path`` field refers to array elements. This is
            meant to support value matching beyond exact match. To
            perform exact match, use path_filters. When both
            path_filters and path_value_matchers are set, an implicit
            AND must be performed.
    """

    action: str = proto.Field(
        proto.STRING,
        number=1,
    )
    resource_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    resource: str = proto.Field(
        proto.STRING,
        number=3,
    )
    path: str = proto.Field(
        proto.STRING,
        number=4,
    )
    source_resource: str = proto.Field(
        proto.STRING,
        number=5,
    )
    source_path: str = proto.Field(
        proto.STRING,
        number=6,
    )
    value: struct_pb2.Value = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="path_value",
        message=struct_pb2.Value,
    )
    value_matcher: "ValueMatcher" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="path_value",
        message="ValueMatcher",
    )
    path_filters: MutableMapping[str, struct_pb2.Value] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=8,
        message=struct_pb2.Value,
    )
    path_value_matchers: MutableMapping[str, "ValueMatcher"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=11,
        message="ValueMatcher",
    )


class ValueMatcher(proto.Message):
    r"""Contains various matching options for values for a GCP
    resource field.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        matches_pattern (str):
            To be used for full regex matching. The
            regular expression is using the Google RE2
            syntax
            (https://github.com/google/re2/wiki/Syntax), so
            to be used with RE2::FullMatch

            This field is a member of `oneof`_ ``match_variant``.
    """

    matches_pattern: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="match_variant",
    )


class CostProjection(proto.Message):
    r"""Contains metadata about how much money a recommendation can
    save or incur.

    Attributes:
        cost (google.type.money_pb2.Money):
            An approximate projection on amount saved or
            amount incurred. Negative cost units indicate
            cost savings and positive cost units indicate
            increase. See google.type.Money documentation
            for positive/negative units.

            A user's permissions may affect whether the cost
            is computed using list prices or custom contract
            prices.
        duration (google.protobuf.duration_pb2.Duration):
            Duration for which this cost applies.
    """

    cost: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=1,
        message=money_pb2.Money,
    )
    duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )


class SecurityProjection(proto.Message):
    r"""Contains various ways of describing the impact on Security.

    Attributes:
        details (google.protobuf.struct_pb2.Struct):
            This field can be used by the recommender to
            define details specific to security impact.
    """

    details: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Struct,
    )


class SustainabilityProjection(proto.Message):
    r"""Contains metadata about how much sustainability a
    recommendation can save or incur.

    Attributes:
        kg_c_o2e (float):
            Carbon Footprint generated in kg of CO2 equivalent. Chose
            kg_c_o2e so that the name renders correctly in camelCase
            (kgCO2e).
        duration (google.protobuf.duration_pb2.Duration):
            Duration for which this sustanability
            applies.
    """

    kg_c_o2e: float = proto.Field(
        proto.DOUBLE,
        number=1,
    )
    duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )


class Impact(proto.Message):
    r"""Contains the impact a recommendation can have for a given
    category.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        category (google.cloud.recommender_v1beta1.types.Impact.Category):
            Category that is being targeted.
        cost_projection (google.cloud.recommender_v1beta1.types.CostProjection):
            Use with CategoryType.COST

            This field is a member of `oneof`_ ``projection``.
        security_projection (google.cloud.recommender_v1beta1.types.SecurityProjection):
            Use with CategoryType.SECURITY

            This field is a member of `oneof`_ ``projection``.
        sustainability_projection (google.cloud.recommender_v1beta1.types.SustainabilityProjection):
            Use with CategoryType.SUSTAINABILITY

            This field is a member of `oneof`_ ``projection``.
    """

    class Category(proto.Enum):
        r"""The category of the impact.

        Values:
            CATEGORY_UNSPECIFIED (0):
                Default unspecified category. Don't use
                directly.
            COST (1):
                Indicates a potential increase or decrease in
                cost.
            SECURITY (2):
                Indicates a potential increase or decrease in
                security.
            PERFORMANCE (3):
                Indicates a potential increase or decrease in
                performance.
            MANAGEABILITY (4):
                Indicates a potential increase or decrease in
                manageability.
            SUSTAINABILITY (5):
                Indicates a potential increase or decrease in
                sustainability.
        """

        CATEGORY_UNSPECIFIED = 0
        COST = 1
        SECURITY = 2
        PERFORMANCE = 3
        MANAGEABILITY = 4
        SUSTAINABILITY = 5

    category: Category = proto.Field(
        proto.ENUM,
        number=1,
        enum=Category,
    )
    cost_projection: "CostProjection" = proto.Field(
        proto.MESSAGE,
        number=100,
        oneof="projection",
        message="CostProjection",
    )
    security_projection: "SecurityProjection" = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="projection",
        message="SecurityProjection",
    )
    sustainability_projection: "SustainabilityProjection" = proto.Field(
        proto.MESSAGE,
        number=102,
        oneof="projection",
        message="SustainabilityProjection",
    )


class RecommendationStateInfo(proto.Message):
    r"""Information for state. Contains state and metadata.

    Attributes:
        state (google.cloud.recommender_v1beta1.types.RecommendationStateInfo.State):
            The state of the recommendation, Eg ACTIVE,
            SUCCEEDED, FAILED.
        state_metadata (MutableMapping[str, str]):
            A map of metadata for the state, provided by
            user or automations systems.
    """

    class State(proto.Enum):
        r"""Represents Recommendation State.

        Values:
            STATE_UNSPECIFIED (0):
                Default state. Don't use directly.
            ACTIVE (1):
                Recommendation is active and can be applied.
                Recommendations content can be updated by
                Google.

                ACTIVE recommendations can be marked as CLAIMED,
                SUCCEEDED, or FAILED.
            CLAIMED (6):
                Recommendation is in claimed state.
                Recommendations content is immutable and cannot
                be updated by Google.

                CLAIMED recommendations can be marked as
                CLAIMED, SUCCEEDED, or FAILED.
            SUCCEEDED (3):
                Recommendation is in succeeded state.
                Recommendations content is immutable and cannot
                be updated by Google.

                SUCCEEDED recommendations can be marked as
                SUCCEEDED, or FAILED.
            FAILED (4):
                Recommendation is in failed state.
                Recommendations content is immutable and cannot
                be updated by Google.

                FAILED recommendations can be marked as
                SUCCEEDED, or FAILED.
            DISMISSED (5):
                Recommendation is in dismissed state.
                Recommendation content can be updated by Google.

                DISMISSED recommendations can be marked as
                ACTIVE.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        CLAIMED = 6
        SUCCEEDED = 3
        FAILED = 4
        DISMISSED = 5

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


class RecommenderType(proto.Message):
    r"""The type of a recommender.

    Attributes:
        name (str):
            The recommender's name in format
            RecommenderTypes/{recommender_type} eg:
            recommenderTypes/google.iam.policy.Recommender
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
