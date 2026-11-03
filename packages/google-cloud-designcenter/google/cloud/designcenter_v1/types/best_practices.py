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

from google.cloud.designcenter_v1.types import assessment, parameters

__protobuf__ = proto.module(
    package="google.cloud.designcenter.v1",
    manifest={
        "AssessmentReport",
        "Policy",
    },
)


class AssessmentReport(proto.Message):
    r"""Aggregated assessment report from all domains.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        adc_application_uri (str):
            Output only. Application URI.

            This field is a member of `oneof`_ ``adc_resource_uri``.
        adc_application_template_uri (str):
            Output only. Application Template URI.

            This field is a member of `oneof`_ ``adc_resource_uri``.
        adc_catalog_template_uri (str):
            Output only. Catalog Template URI.

            This field is a member of `oneof`_ ``adc_resource_uri``.
        adc_space_uri (str):
            Output only. Space URI.

            This field is a member of `oneof`_ ``adc_resource_uri``.
        domain_assessment_reports (MutableSequence[google.cloud.designcenter_v1.types.DomainAssessmentReport]):
            Output only. Generated best practice reports.
        skipped_domains (MutableSequence[google.cloud.designcenter_v1.types.SkippedDomain]):
            Output only. Skipped domains.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the report was
            created.
    """

    adc_application_uri: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="adc_resource_uri",
    )
    adc_application_template_uri: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="adc_resource_uri",
    )
    adc_catalog_template_uri: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="adc_resource_uri",
    )
    adc_space_uri: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="adc_resource_uri",
    )
    domain_assessment_reports: MutableSequence[assessment.DomainAssessmentReport] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message=assessment.DomainAssessmentReport,
        )
    )
    skipped_domains: MutableSequence[assessment.SkippedDomain] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=assessment.SkippedDomain,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )


class Policy(proto.Message):
    r"""A Policy is a resource within an Application Template that
    refers to a Policy that you author outside of Application Design
    Center and attach to an application template.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        policy_uri (str):
            Optional. URI of the policy.

            This field is a member of `oneof`_ ``uri``.
        policy_revision_uri (str):
            Optional. URI of the policy revision.

            This field is a member of `oneof`_ ``uri``.
        name (str):
            Identifier. The policy name in the following format:
            ``projects/$project/locations/$location/spaces/$space/applicationTemplates/$applicationTemplate/policies/$policy``
        display_name (str):
            Optional. The policy display name.
        description (str):
            Optional. The policy description.
        policy_type (google.cloud.designcenter_v1.types.Policy.PolicyType):
            Required. The policy type.
            Policy type is used to determine the domain of
            the policy.
        apply_conditions (MutableSequence[google.cloud.designcenter_v1.types.ApplyCondition]):
            Optional. Conditions for applying the policy. Condition
            accepts the ``criticality`` and ``environment`` parameters
            from the application template.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The policy creation timestamp.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The policy update timestamp.
        cloud_control_configs (MutableSequence[google.cloud.designcenter_v1.types.CloudControlConfig]):
            Optional. Input only. Parameter values for the cloud
            controls of the policy's framework, grouped by cloud
            control. Only honored when framework parameter support is
            enabled for the project; ignored otherwise.

            The values are saved with the application template and are
            not returned on the policy. On update, they replace the
            saved values. If they are empty, the saved values are
            cleared if ``cloud_control_configs`` is named in the update
            mask. Otherwise, the saved values are kept, unless the
            policy's framework changes.
    """

    class PolicyType(proto.Enum):
        r"""The policy type.

        Values:
            POLICY_TYPE_UNSPECIFIED (0):
                Default.
            COMPLIANCE_FRAMEWORK (1):
                Compliance framework policy.
        """

        POLICY_TYPE_UNSPECIFIED = 0
        COMPLIANCE_FRAMEWORK = 1

    policy_uri: str = proto.Field(
        proto.STRING,
        number=5,
        oneof="uri",
    )
    policy_revision_uri: str = proto.Field(
        proto.STRING,
        number=6,
        oneof="uri",
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
    policy_type: PolicyType = proto.Field(
        proto.ENUM,
        number=4,
        enum=PolicyType,
    )
    apply_conditions: MutableSequence[assessment.ApplyCondition] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=assessment.ApplyCondition,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    cloud_control_configs: MutableSequence[parameters.CloudControlConfig] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=10,
            message=parameters.CloudControlConfig,
        )
    )


__all__ = tuple(sorted(__protobuf__.manifest))
