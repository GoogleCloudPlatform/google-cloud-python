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

from google.cloud.deploy_v1.types import cloud_deploy

__protobuf__ = proto.module(
    package="google.cloud.deploy.v1",
    manifest={
        "DeployPolicyEvaluationEvent",
    },
)


class DeployPolicyEvaluationEvent(proto.Message):
    r"""Payload proto for
    "clouddeploy.googleapis.com/deploypolicy_evaluation" Platform Log
    event that describes the deploy policy evaluation event.

    Attributes:
        message (str):
            Debug message for when a deploy policy event
            occurs.
        rule_type (str):
            Rule type (e.g. Restrict Rollouts).
        rule (str):
            Rule id.
        pipeline_uid (str):
            Unique identifier of the ``Delivery Pipeline``.
        delivery_pipeline (str):
            The name of the ``Delivery Pipeline``.
        target_uid (str):
            Unique identifier of the ``Target``. This is an optional
            field, as a ``Target`` may not always be applicable to a
            policy.
        target (str):
            The name of the ``Target``. This is an optional field, as a
            ``Target`` may not always be applicable to a policy.
        invoker (google.cloud.deploy_v1.types.DeployPolicy.Invoker):
            What invoked the action (e.g. a user or
            automation).
        deploy_policy (str):
            The name of the ``DeployPolicy``.
        deploy_policy_uid (str):
            Unique identifier of the ``DeployPolicy``.
        allowed (bool):
            Whether the request is allowed. Allowed is
            set as true if: (1) the request complies with
            the policy; or (2) the request doesn't comply
            with the policy but the policy was overridden;
            or
            (3) the request doesn't comply with the policy
            but the policy was suspended
        verdict (google.cloud.deploy_v1.types.DeployPolicyEvaluationEvent.PolicyVerdict):
            The policy verdict of the request.
        overrides (MutableSequence[google.cloud.deploy_v1.types.DeployPolicyEvaluationEvent.PolicyVerdictOverride]):
            Things that could have overridden the policy
            verdict. Overrides together with verdict decide
            whether the request is allowed.
    """

    class PolicyVerdict(proto.Enum):
        r"""The policy verdict of the request.

        Values:
            POLICY_VERDICT_UNSPECIFIED (0):
                This should never happen.
            ALLOWED_BY_POLICY (1):
                Allowed by policy. This enum value is not
                currently used but may be used in the future.
                Currently logs are only generated when a request
                is denied by policy.
            DENIED_BY_POLICY (2):
                Denied by policy.
        """

        POLICY_VERDICT_UNSPECIFIED = 0
        ALLOWED_BY_POLICY = 1
        DENIED_BY_POLICY = 2

    class PolicyVerdictOverride(proto.Enum):
        r"""Things that could have overridden the policy verdict. When overrides
        are used, the request will be allowed even if it is
        DENIED_BY_POLICY.

        Values:
            POLICY_VERDICT_OVERRIDE_UNSPECIFIED (0):
                This should never happen.
            POLICY_OVERRIDDEN (1):
                The policy was overridden.
            POLICY_SUSPENDED (2):
                The policy was suspended.
        """

        POLICY_VERDICT_OVERRIDE_UNSPECIFIED = 0
        POLICY_OVERRIDDEN = 1
        POLICY_SUSPENDED = 2

    message: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rule_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    rule: str = proto.Field(
        proto.STRING,
        number=3,
    )
    pipeline_uid: str = proto.Field(
        proto.STRING,
        number=4,
    )
    delivery_pipeline: str = proto.Field(
        proto.STRING,
        number=5,
    )
    target_uid: str = proto.Field(
        proto.STRING,
        number=6,
    )
    target: str = proto.Field(
        proto.STRING,
        number=7,
    )
    invoker: cloud_deploy.DeployPolicy.Invoker = proto.Field(
        proto.ENUM,
        number=8,
        enum=cloud_deploy.DeployPolicy.Invoker,
    )
    deploy_policy: str = proto.Field(
        proto.STRING,
        number=9,
    )
    deploy_policy_uid: str = proto.Field(
        proto.STRING,
        number=10,
    )
    allowed: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    verdict: PolicyVerdict = proto.Field(
        proto.ENUM,
        number=12,
        enum=PolicyVerdict,
    )
    overrides: MutableSequence[PolicyVerdictOverride] = proto.RepeatedField(
        proto.ENUM,
        number=13,
        enum=PolicyVerdictOverride,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
