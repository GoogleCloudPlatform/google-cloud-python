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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.type.interval_pb2 as interval_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.chronicle.v1",
    manifest={
        "FindingsRefinementType",
        "FindingsRefinement",
        "FindingsRefinementDeployment",
        "DetectionExclusionApplication",
        "FindingsRefinementActivity",
        "DetectionExclusionActivity",
        "GetFindingsRefinementRequest",
        "ListFindingsRefinementsRequest",
        "ListFindingsRefinementsResponse",
        "CreateFindingsRefinementRequest",
        "UpdateFindingsRefinementRequest",
        "GetFindingsRefinementDeploymentRequest",
        "UpdateFindingsRefinementDeploymentRequest",
        "ListAllFindingsRefinementDeploymentsRequest",
        "ListAllFindingsRefinementDeploymentsResponse",
        "OutcomeFilter",
        "ComputeFindingsRefinementActivityRequest",
        "ComputeFindingsRefinementActivityResponse",
        "ComputeAllFindingsRefinementActivitiesRequest",
        "ComputeAllFindingsRefinementActivitiesResponse",
    },
)


class FindingsRefinementType(proto.Enum):
    r"""The type of findings refinement, which determines what the
    findings refinement runs over and the mechanism by which it
    runs.

    Values:
        FINDINGS_REFINEMENT_TYPE_UNSPECIFIED (0):
            The findings refinement type is unspecified.
        DETECTION_EXCLUSION (1):
            Indicates that the findings refinement is a
            detection exclusion and should exclude matching
            detections.
    """

    FINDINGS_REFINEMENT_TYPE_UNSPECIFIED = 0
    DETECTION_EXCLUSION = 1


class FindingsRefinement(proto.Message):
    r"""Represents a set of logic conditions used to refine various
    types of findings such as curated rule detections.

    Attributes:
        name (str):
            Full resource name for the findings refinement. Format:
            projects/{project}/locations/{region}/instances/{instance}/findingsRefinements/{findings_refinement}
        display_name (str):
            Display name of the findings refinement.
        type_ (google.cloud.chronicle_v1.types.FindingsRefinementType):
            The type of findings refinement.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp of when the
            findings refinement was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp of when the
            findings refinement was last updated.
        query (str):
            The query for the findings refinement. Works
            in conjunction with the type field to determine
            the findings refinement behavior. The syntax of
            this query is the same as a UDM search string.
            See the following for more information:

            https://cloud.google.com/chronicle/docs/investigation/udm-search
        outcome_filters (MutableSequence[google.cloud.chronicle_v1.types.OutcomeFilter]):
            Optional. The outcome filters for the
            findings refinement. These allow you to specify
            filters that are applied to the outcome
            variables in the detection. All filters must be
            true for a detection to match the findings
            refinement.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    type_: "FindingsRefinementType" = proto.Field(
        proto.ENUM,
        number=3,
        enum="FindingsRefinementType",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    query: str = proto.Field(
        proto.STRING,
        number=7,
    )
    outcome_filters: MutableSequence["OutcomeFilter"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="OutcomeFilter",
    )


class FindingsRefinementDeployment(proto.Message):
    r"""The FindingsRefinementDeployment resource represents the
    deployment state of a findings refinement.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        detection_exclusion_application (google.cloud.chronicle_v1.types.DetectionExclusionApplication):
            The resources which the detection exclusion
            is applied to.

            This field is a member of `oneof`_ ``FindingsRefinementApplication``.
        name (str):
            Required. The resource name of the findings refinement
            deployment. Format:
            projects/{project}/locations/{location}/instances/{instance}/findingsRefinements/{findings_refinement}/deployment
        enabled (bool):
            Whether the findings refinement is currently
            deployed continuously against incoming findings.
        archived (bool):
            The archive state of the findings refinement
            deployment. Cannot be set to true unless enabled
            is set to false. If currently set to true,
            enabled cannot be updated to true.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the findings
            refinement deployment was last updated.
    """

    detection_exclusion_application: "DetectionExclusionApplication" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="FindingsRefinementApplication",
        message="DetectionExclusionApplication",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    enabled: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    archived: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class DetectionExclusionApplication(proto.Message):
    r"""Describes the detectors a detection exclusion is applied to.

    Attributes:
        curated_rule_sets (MutableSequence[str]):
            The CuratedRuleSets this detection exclusion applies to.
            Format:
            projects/{project}/locations/{location}/instances/{instance}/curatedRuleSetCategories/{category}/curatedRuleSets/{rule_set}
        curated_rules (MutableSequence[str]):
            The CuratedRules this detection exclusion
            applies to. Format:

            projects/{project}/locations/{location}/instances/{instance}/curatedRules/{rule}
        rules (MutableSequence[str]):
            Optional. The Rules this detection exclusion
            applies to. Format:

            projects/{project}/locations/{location}/instances/{instance}/rules/{rule}
        deleted_curated_rule_sets (MutableSequence[str]):
            Output only. The deleted CuratedRuleSets this detection
            exclusion applies to. Indicates to the customer that the
            detection exclusion no longer applies to the rule sets, so
            the detection exclusion should be updated. Format:
            projects/{project}/locations/{location}/instances/{instance}/curatedRuleSetCategories/{category}/curatedRuleSets/{rule_set}
    """

    curated_rule_sets: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    curated_rules: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    rules: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    deleted_curated_rule_sets: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


class FindingsRefinementActivity(proto.Message):
    r"""The activity for a specific findings refinement.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        detection_exclusion_activity (google.cloud.chronicle_v1.types.DetectionExclusionActivity):
            The activity for the detection exclusion.

            This field is a member of `oneof`_ ``Activity``.
        findings_refinement (str):
            Required. Full resource name for the findings refinement
            this activity corresponds to. Format:
            projects/{project}/locations/{region}/instances/{instance}/findingsRefinements/{findings_refinement}
    """

    detection_exclusion_activity: "DetectionExclusionActivity" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="Activity",
        message="DetectionExclusionActivity",
    )
    findings_refinement: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DetectionExclusionActivity(proto.Message):
    r"""The activity for a findings refinement that is a detection
    exclusion. The activity is broken down per detector.

    Attributes:
        detection_exclusion_detector_activities (MutableSequence[google.cloud.chronicle_v1.types.DetectionExclusionActivity.DetectionExclusionDetectorActivity]):
            The activity for the detection exclusion
            broken down by detector.
    """

    class DetectionExclusionDetectorActivity(proto.Message):
        r"""The activity for a findings refinement that is a detection
        exclusion broken down for one specific detector.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            curated_rule (str):
                Full resource name for the curated rule this
                activity corresponds to. Format:

                projects/{project}/locations/{location}/instances/{instance}/curatedRules/{rule}

                This field is a member of `oneof`_ ``detector_name``.
            curated_rule_set (str):
                Full resource name for the curated rule set this activity
                corresponds to. This field will only be set if the customer
                has access to the curated rule set the exclusion is applied
                to. Format:
                projects/{project}/locations/{location}/instances/{instance}/curatedRuleSetCategories/{curated_rule_set_category}/curatedRuleSets/{curated_rule_set}

                This field is a member of `oneof`_ ``detector_name``.
            rule (str):
                Full resource name for the rule this activity
                corresponds to. Format:

                projects/{project}/locations/{location}/instances/{instance}/rules/{rule}

                This field is a member of `oneof`_ ``detector_name``.
            deleted_curated_rule_set (str):
                Full resource name for the deleted curated rule set this
                activity corresponds to. This field will only be set if the
                customer does not have access to the curated rule set the
                exclusion is applied to. Format:
                projects/{project}/locations/{location}/instances/{instance}/curatedRuleSetCategories/{curated_rule_set_category}/curatedRuleSets/{curated_rule_set}

                This field is a member of `oneof`_ ``detector_name``.
            excluded_detection_count (int):
                The number of detections for the detector
                that were excluded by the detection exclusion.
            total_detection_count (int):
                The total number of detections found by the
                detector. This includes both excluded detections
                and non-excluded detections.
        """

        curated_rule: str = proto.Field(
            proto.STRING,
            number=1,
            oneof="detector_name",
        )
        curated_rule_set: str = proto.Field(
            proto.STRING,
            number=2,
            oneof="detector_name",
        )
        rule: str = proto.Field(
            proto.STRING,
            number=5,
            oneof="detector_name",
        )
        deleted_curated_rule_set: str = proto.Field(
            proto.STRING,
            number=6,
            oneof="detector_name",
        )
        excluded_detection_count: int = proto.Field(
            proto.INT64,
            number=3,
        )
        total_detection_count: int = proto.Field(
            proto.INT64,
            number=4,
        )

    detection_exclusion_detector_activities: MutableSequence[
        DetectionExclusionDetectorActivity
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=DetectionExclusionDetectorActivity,
    )


class GetFindingsRefinementRequest(proto.Message):
    r"""Request message for GetFindingsRefinement method.

    Attributes:
        name (str):
            Required. The name of the findings refinement to retrieve.
            Format:
            projects/{project}/locations/{location}/instances/{instance}/findingsRefinements/{findings_refinement}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListFindingsRefinementsRequest(proto.Message):
    r"""Request message for ListFindingsRefinements method.

    Attributes:
        parent (str):
            Required. The parent, which owns this
            collection of findings refinements. Format:

            projects/{project}/locations/{location}/instances/{instance}
        page_size (int):
            The maximum number of findings refinements to
            return. The service may return fewer than this
            value. If unspecified, at most 100 rules will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            A page token, received from a previous
            ``ListFindingsRefinements`` call. Provide this to retrieve
            the subsequent page.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListFindingsRefinementsResponse(proto.Message):
    r"""Response message for ListFindingsRefinements method.

    Attributes:
        findings_refinements (MutableSequence[google.cloud.chronicle_v1.types.FindingsRefinement]):
            List of findings refinements.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    findings_refinements: MutableSequence["FindingsRefinement"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="FindingsRefinement",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateFindingsRefinementRequest(proto.Message):
    r"""Request message for CreateFindingsRefinement method.

    Attributes:
        parent (str):
            Required. The parent resource where this
            findings refinement will be created. Format:

            projects/{project}/locations/{location}/instances/{instance}
        findings_refinement (google.cloud.chronicle_v1.types.FindingsRefinement):
            Required. The findings refinement to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    findings_refinement: "FindingsRefinement" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="FindingsRefinement",
    )


class UpdateFindingsRefinementRequest(proto.Message):
    r"""Request message for UpdateFindingsRefinement method.

    Attributes:
        findings_refinement (google.cloud.chronicle_v1.types.FindingsRefinement):
            Required. The findings refinement to update.

            The findings refinement's ``name`` field is used to identify
            the findings refinement to update. Format:
            projects/{project}/locations/{location}/instances/{instance}/findingsRefinements/{findings_refinement}
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update. If ``*`` is
            provided, all fields will be updated.
    """

    findings_refinement: "FindingsRefinement" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="FindingsRefinement",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetFindingsRefinementDeploymentRequest(proto.Message):
    r"""Request message for GetFindingsRefinementDeployment method.

    Attributes:
        name (str):
            Required. The name of the findings refinement to retrieve.
            Format:
            projects/{project}/locations/{location}/instances/{instance}/findingsRefinements/{findings_refinement}/deployment
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateFindingsRefinementDeploymentRequest(proto.Message):
    r"""Request message for UpdateFindingsRefinementDeployment
    method.

    Attributes:
        findings_refinement_deployment (google.cloud.chronicle_v1.types.FindingsRefinementDeployment):
            Required. The findings refinement deployment to update.

            The findings refinement deployment's ``name`` field is used
            to identify the findings refinement deployment to update.
            Format:
            projects/{project}/locations/{location}/instances/{instance}/findingsRefinements/{findings_refinement}/deployment
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to update. If ``*`` is
            provided, all fields will be updated.
    """

    findings_refinement_deployment: "FindingsRefinementDeployment" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="FindingsRefinementDeployment",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class ListAllFindingsRefinementDeploymentsRequest(proto.Message):
    r"""Request message for ListAllFindingsRefinementDeployments
    method.

    Attributes:
        instance (str):
            Required. The name of the parent resource,
            which is the SecOps instance to list all
            findings refinement deployments over. Format:

            projects/{project}/locations/{location}/instances/{instance}
        page_size (int):
            The maximum number of findings refinement
            deployments to return. The service may return
            fewer than this value. If unspecified, at most
            100 rule deployments will be returned. The
            maximum value is 1000; values above 1000 will be
            coerced to 1000.
        page_token (str):
            A page token, received from a previous
            ``ListAllFindingsRefinementDeployments`` call. Provide this
            to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListAllFindingsRefinementDeployments`` must match the call
            that provided the page token.
        filter (str):
            A filter that can be used to retrieve specific findings
            refinement deployments. Only the following filters are
            allowed:
            detection_exclusion_application.curated_rule_sets:"<curated_rule_set_name>"",
            detection_exclusion_application.curated_rules:"<curated_rule_name>".
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListAllFindingsRefinementDeploymentsResponse(proto.Message):
    r"""Response message for ListAllFindingsRefinementDeployments
    method.

    Attributes:
        all_findings_refinement_deployments (MutableSequence[google.cloud.chronicle_v1.types.FindingsRefinementDeployment]):
            List of all findings refinement deployments.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    all_findings_refinement_deployments: MutableSequence[
        "FindingsRefinementDeployment"
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="FindingsRefinementDeployment",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class OutcomeFilter(proto.Message):
    r"""Outcome filter for the findings refinement. This is used to
    filter the findings refinement based on the outcome variable
    values.

    Attributes:
        outcome_variable (str):
            Required. The outcome variable name.
        outcome_value (str):
            Required. The value of the outcome variable
            to match.
        outcome_filter_operator (google.cloud.chronicle_v1.types.OutcomeFilter.Operator):
            Required. The operator to be applied to the
            outcome variable.
    """

    class Operator(proto.Enum):
        r"""The operator to compare the outcome variable value with the
        outcome value in the outcome filter.

        Values:
            OPERATOR_UNSPECIFIED (0):
                The operator is unspecified.
            EQUAL (1):
                The outcome variable value must be equal to
                the outcome value in the outcome filter.
            CONTAINS (2):
                The outcome variable value must contain the
                outcome value in the outcome filter.
            MATCHES_REGEX (3):
                The outcome variable value must match the
                outcome value regex in the outcome filter.
            MATCHES_CIDR (4):
                The outcome variable value must be a valid IP
                address in the outcome filter value CIDR range.
        """

        OPERATOR_UNSPECIFIED = 0
        EQUAL = 1
        CONTAINS = 2
        MATCHES_REGEX = 3
        MATCHES_CIDR = 4

    outcome_variable: str = proto.Field(
        proto.STRING,
        number=1,
    )
    outcome_value: str = proto.Field(
        proto.STRING,
        number=2,
    )
    outcome_filter_operator: Operator = proto.Field(
        proto.ENUM,
        number=3,
        enum=Operator,
    )


class ComputeFindingsRefinementActivityRequest(proto.Message):
    r"""Request message for ComputeFindingsRefinementActivity method.

    Attributes:
        name (str):
            Required. Full resource name for the findings refinement to
            fetch the activity for. Format:
            projects/{project}/locations/{region}/instances/{instance}/findingsRefinements/{findings_refinement}
        interval (google.type.interval_pb2.Interval):
            The time interval the activity is measured
            over.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    interval: interval_pb2.Interval = proto.Field(
        proto.MESSAGE,
        number=2,
        message=interval_pb2.Interval,
    )


class ComputeFindingsRefinementActivityResponse(proto.Message):
    r"""Response message for ComputeFindingsRefinementActivity
    method.

    Attributes:
        activity (google.cloud.chronicle_v1.types.FindingsRefinementActivity):
            The activity for the findings refinement.
    """

    activity: "FindingsRefinementActivity" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="FindingsRefinementActivity",
    )


class ComputeAllFindingsRefinementActivitiesRequest(proto.Message):
    r"""Request message for ComputeAllFindingsRefinementActivities
    method.

    Attributes:
        instance (str):
            Required. The ID of the Instance to retrieve
            counts for. Format:

            projects/{project}/locations/{location}/instances/{instance}
        interval (google.type.interval_pb2.Interval):
            The time interval the activity is measured
            over.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    interval: interval_pb2.Interval = proto.Field(
        proto.MESSAGE,
        number=2,
        message=interval_pb2.Interval,
    )


class ComputeAllFindingsRefinementActivitiesResponse(proto.Message):
    r"""Response message for ComputeAllFindingsRefinementActivities
    method.

    Attributes:
        activities (MutableSequence[google.cloud.chronicle_v1.types.FindingsRefinementActivity]):
            The activities of all findings refinements.
    """

    activities: MutableSequence["FindingsRefinementActivity"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="FindingsRefinementActivity",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
