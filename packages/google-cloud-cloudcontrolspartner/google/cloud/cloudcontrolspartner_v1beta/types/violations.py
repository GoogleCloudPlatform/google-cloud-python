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
import google.type.interval_pb2 as interval_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.cloudcontrolspartner.v1beta",
    manifest={
        "Violation",
        "ListViolationsRequest",
        "ListViolationsResponse",
        "GetViolationRequest",
    },
)


class Violation(proto.Message):
    r"""Details of resource Violation

    Attributes:
        name (str):
            Identifier. Format:
            ``organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/violations/{violation}``
        description (str):
            Output only. Description for the Violation.
            e.g. OrgPolicy gcp.resourceLocations has non
            compliant value.
        begin_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time of the event which
            triggered the Violation.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last time when the Violation
            record was updated.
        resolve_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time of the event which fixed
            the Violation. If the violation is ACTIVE this
            will be empty.
        category (str):
            Output only. Category under which this
            violation is mapped. e.g. Location, Service
            Usage, Access, Encryption, etc.
        state (google.cloud.cloudcontrolspartner_v1beta.types.Violation.State):
            Output only. State of the violation
        non_compliant_org_policy (str):
            Output only. Immutable. Name of the OrgPolicy which was
            modified with non-compliant change and resulted this
            violation. Format:
            ``projects/{project_number}/policies/{constraint_name}``
            ``folders/{folder_id}/policies/{constraint_name}``
            ``organizations/{organization_id}/policies/{constraint_name}``
        folder_id (int):
            The folder_id of the violation
        remediation (google.cloud.cloudcontrolspartner_v1beta.types.Violation.Remediation):
            Output only. Compliance violation remediation
    """

    class State(proto.Enum):
        r"""Violation State Values

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state.
            RESOLVED (1):
                Violation is resolved.
            UNRESOLVED (2):
                Violation is Unresolved
            EXCEPTION (3):
                Violation is Exception
        """

        STATE_UNSPECIFIED = 0
        RESOLVED = 1
        UNRESOLVED = 2
        EXCEPTION = 3

    class Remediation(proto.Message):
        r"""Represents remediation guidance to resolve compliance
        violation for AssuredWorkload

        Attributes:
            instructions (google.cloud.cloudcontrolspartner_v1beta.types.Violation.Remediation.Instructions):
                Required. Remediation instructions to resolve
                violations
            compliant_values (MutableSequence[str]):
                Values that can resolve the violation
                For example: for list org policy violations,
                this will either be the list of allowed or
                denied values
            remediation_type (google.cloud.cloudcontrolspartner_v1beta.types.Violation.Remediation.RemediationType):
                Output only. Remediation type based on the
                type of org policy values violated
        """

        class RemediationType(proto.Enum):
            r"""Classifying remediation into various types based on the kind
            of violation. For example, violations caused due to changes in
            boolean org policy requires different remediation instructions
            compared to violation caused due to changes in allowed values of
            list org policy.

            Values:
                REMEDIATION_TYPE_UNSPECIFIED (0):
                    Unspecified remediation type
                REMEDIATION_BOOLEAN_ORG_POLICY_VIOLATION (1):
                    Remediation type for boolean org policy
                REMEDIATION_LIST_ALLOWED_VALUES_ORG_POLICY_VIOLATION (2):
                    Remediation type for list org policy which
                    have allowed values in the monitoring rule
                REMEDIATION_LIST_DENIED_VALUES_ORG_POLICY_VIOLATION (3):
                    Remediation type for list org policy which
                    have denied values in the monitoring rule
                REMEDIATION_RESTRICT_CMEK_CRYPTO_KEY_PROJECTS_ORG_POLICY_VIOLATION (4):
                    Remediation type for
                    gcp.restrictCmekCryptoKeyProjects
                REMEDIATION_RESOURCE_VIOLATION (5):
                    Remediation type for resource violation.
            """

            REMEDIATION_TYPE_UNSPECIFIED = 0
            REMEDIATION_BOOLEAN_ORG_POLICY_VIOLATION = 1
            REMEDIATION_LIST_ALLOWED_VALUES_ORG_POLICY_VIOLATION = 2
            REMEDIATION_LIST_DENIED_VALUES_ORG_POLICY_VIOLATION = 3
            REMEDIATION_RESTRICT_CMEK_CRYPTO_KEY_PROJECTS_ORG_POLICY_VIOLATION = 4
            REMEDIATION_RESOURCE_VIOLATION = 5

        class Instructions(proto.Message):
            r"""Instructions to remediate violation

            Attributes:
                gcloud_instructions (google.cloud.cloudcontrolspartner_v1beta.types.Violation.Remediation.Instructions.Gcloud):
                    Remediation instructions to resolve violation
                    via gcloud cli
                console_instructions (google.cloud.cloudcontrolspartner_v1beta.types.Violation.Remediation.Instructions.Console):
                    Remediation instructions to resolve violation
                    via cloud console
            """

            class Gcloud(proto.Message):
                r"""Remediation instructions to resolve violation via gcloud cli

                Attributes:
                    gcloud_commands (MutableSequence[str]):
                        Gcloud command to resolve violation
                    steps (MutableSequence[str]):
                        Steps to resolve violation via gcloud cli
                    additional_links (MutableSequence[str]):
                        Additional urls for more information about
                        steps
                """

                gcloud_commands: MutableSequence[str] = proto.RepeatedField(
                    proto.STRING,
                    number=1,
                )
                steps: MutableSequence[str] = proto.RepeatedField(
                    proto.STRING,
                    number=2,
                )
                additional_links: MutableSequence[str] = proto.RepeatedField(
                    proto.STRING,
                    number=3,
                )

            class Console(proto.Message):
                r"""Remediation instructions to resolve violation via cloud
                console

                Attributes:
                    console_uris (MutableSequence[str]):
                        Link to console page where violations can be
                        resolved
                    steps (MutableSequence[str]):
                        Steps to resolve violation via cloud console
                    additional_links (MutableSequence[str]):
                        Additional urls for more information about
                        steps
                """

                console_uris: MutableSequence[str] = proto.RepeatedField(
                    proto.STRING,
                    number=1,
                )
                steps: MutableSequence[str] = proto.RepeatedField(
                    proto.STRING,
                    number=2,
                )
                additional_links: MutableSequence[str] = proto.RepeatedField(
                    proto.STRING,
                    number=3,
                )

            gcloud_instructions: "Violation.Remediation.Instructions.Gcloud" = (
                proto.Field(
                    proto.MESSAGE,
                    number=1,
                    message="Violation.Remediation.Instructions.Gcloud",
                )
            )
            console_instructions: "Violation.Remediation.Instructions.Console" = (
                proto.Field(
                    proto.MESSAGE,
                    number=2,
                    message="Violation.Remediation.Instructions.Console",
                )
            )

        instructions: "Violation.Remediation.Instructions" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="Violation.Remediation.Instructions",
        )
        compliant_values: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        remediation_type: "Violation.Remediation.RemediationType" = proto.Field(
            proto.ENUM,
            number=3,
            enum="Violation.Remediation.RemediationType",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    begin_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    resolve_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    category: str = proto.Field(
        proto.STRING,
        number=6,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=7,
        enum=State,
    )
    non_compliant_org_policy: str = proto.Field(
        proto.STRING,
        number=8,
    )
    folder_id: int = proto.Field(
        proto.INT64,
        number=9,
    )
    remediation: Remediation = proto.Field(
        proto.MESSAGE,
        number=13,
        message=Remediation,
    )


class ListViolationsRequest(proto.Message):
    r"""Message for requesting list of Violations

    Attributes:
        parent (str):
            Required. Parent resource Format
            ``organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}``
        page_size (int):
            Optional. The maximum number of customers row
            to return. The service may return fewer than
            this value. If unspecified, at most 10 customers
            will be returned.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListViolations`` call. Provide this to retrieve the
            subsequent page.
        filter (str):
            Optional. Filtering results
        order_by (str):
            Optional. Hint for how to order the results
        interval (google.type.interval_pb2.Interval):
            Optional. Specifies the interval for
            retrieving violations. if unspecified, all
            violations will be returned.
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )
    interval: interval_pb2.Interval = proto.Field(
        proto.MESSAGE,
        number=6,
        message=interval_pb2.Interval,
    )


class ListViolationsResponse(proto.Message):
    r"""Response message for list customer violation requests

    Attributes:
        violations (MutableSequence[google.cloud.cloudcontrolspartner_v1beta.types.Violation]):
            List of violation
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Workloads that could not be reached due to
            permission errors or any other error. Ref:
            https://google.aip.dev/217
    """

    @property
    def raw_page(self):
        return self

    violations: MutableSequence["Violation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Violation",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetViolationRequest(proto.Message):
    r"""Message for getting a Violation

    Attributes:
        name (str):
            Required. Format:
            ``organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/violations/{violation}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
