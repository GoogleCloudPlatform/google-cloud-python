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
    package="google.cloud.securitycenter.v1",
    manifest={
        "SecurityPosture",
    },
)


class SecurityPosture(proto.Message):
    r"""Represents a posture that is deployed on Google Cloud by the
    Security Command Center Posture Management service. A posture
    contains one or more policy sets. A policy set is a group of
    policies that enforce a set of security rules on Google Cloud.

    Attributes:
        name (str):
            Name of the posture, for example, ``CIS-Posture``.
        revision_id (str):
            The version of the posture, for example, ``c7cfa2a8``.
        posture_deployment_resource (str):
            The project, folder, or organization on which the posture is
            deployed, for example, ``projects/{project_number}``.
        posture_deployment (str):
            The name of the posture deployment, for example,
            ``organizations/{org_id}/posturedeployments/{posture_deployment_id}``.
        changed_policy (str):
            The name of the updated policy, for example,
            ``projects/{project_id}/policies/{constraint_name}``.
        policy_set (str):
            The name of the updated policyset, for example,
            ``cis-policyset``.
        policy (str):
            The ID of the updated policy, for example,
            ``compute-policy-1``.
        policy_drift_details (MutableSequence[google.cloud.securitycenter_v1.types.SecurityPosture.PolicyDriftDetails]):
            The details about a change in an updated
            policy that violates the deployed posture.
    """

    class PolicyDriftDetails(proto.Message):
        r"""The policy field that violates the deployed posture and its
        expected and detected values.

        Attributes:
            field (str):
                The name of the updated field, for example
                constraint.implementation.policy_rules[0].enforce
            expected_value (str):
                The value of this field that was configured in a posture,
                for example, ``true`` or
                ``allowed_values={"projects/29831892"}``.
            detected_value (str):
                The detected value that violates the deployed posture, for
                example, ``false`` or
                ``allowed_values={"projects/22831892"}``.
        """

        field: str = proto.Field(
            proto.STRING,
            number=1,
        )
        expected_value: str = proto.Field(
            proto.STRING,
            number=2,
        )
        detected_value: str = proto.Field(
            proto.STRING,
            number=3,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    revision_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    posture_deployment_resource: str = proto.Field(
        proto.STRING,
        number=3,
    )
    posture_deployment: str = proto.Field(
        proto.STRING,
        number=4,
    )
    changed_policy: str = proto.Field(
        proto.STRING,
        number=5,
    )
    policy_set: str = proto.Field(
        proto.STRING,
        number=6,
    )
    policy: str = proto.Field(
        proto.STRING,
        number=7,
    )
    policy_drift_details: MutableSequence[PolicyDriftDetails] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message=PolicyDriftDetails,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
