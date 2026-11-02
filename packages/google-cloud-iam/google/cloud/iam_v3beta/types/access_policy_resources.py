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
import google.type.expr_pb2 as expr_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.iam.v3beta",
    manifest={
        "AccessPolicy",
        "AccessPolicyDetails",
        "AccessPolicyRule",
    },
)


class AccessPolicy(proto.Message):
    r"""An IAM access policy resource.

    Attributes:
        name (str):
            Identifier. The resource name of the access policy.

            The following formats are supported:

            - ``projects/{project_id}/locations/{location}/accessPolicies/{policy_id}``
            - ``projects/{project_number}/locations/{location}/accessPolicies/{policy_id}``
            - ``folders/{folder_id}/locations/{location}/accessPolicies/{policy_id}``
            - ``organizations/{organization_id}/locations/{location}/accessPolicies/{policy_id}``
        uid (str):
            Output only. The globally unique ID of the
            access policy.
        etag (str):
            Optional. The etag for the access policy.
            If this is provided on update, it must match the
            server's etag.
        display_name (str):
            Optional. The description of the access
            policy. Must be less than or equal to 63
            characters.
        annotations (MutableMapping[str, str]):
            Optional. User defined annotations. See
            https://google.aip.dev/148#annotations for more
            details such as format and size limitations
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the access policy
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the access policy
            was most recently updated.
        details (google.cloud.iam_v3beta.types.AccessPolicyDetails):
            Optional. The details for the access policy.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=3,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    annotations: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    details: "AccessPolicyDetails" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="AccessPolicyDetails",
    )


class AccessPolicyDetails(proto.Message):
    r"""Access policy details.

    Attributes:
        rules (MutableSequence[google.cloud.iam_v3beta.types.AccessPolicyRule]):
            Required. A list of access policy rules.
    """

    rules: MutableSequence["AccessPolicyRule"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AccessPolicyRule",
    )


class AccessPolicyRule(proto.Message):
    r"""Access Policy Rule that determines the behavior of the
    policy.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        description (str):
            Optional. Customer specified description of
            the rule. Must be less than or equal to 256
            characters.

            This field is a member of `oneof`_ ``_description``.
        effect (google.cloud.iam_v3beta.types.AccessPolicyRule.Effect):
            Required. The effect of the rule.

            This field is a member of `oneof`_ ``_effect``.
        principals (MutableSequence[str]):
            Required. The identities for which this rule's effect
            governs using one or more permissions on Google Cloud
            resources. This field can contain the following values:

            - ``principal://goog/subject/{email_id}``: A specific Google
              Account. Includes Gmail, Cloud Identity, and Google
              Workspace user accounts. For example,
              ``principal://goog/subject/alice@example.com``.

            - ``principal://iam.googleapis.com/projects/-/serviceAccounts/{service_account_id}``:
              A Google Cloud service account. For example,
              ``principal://iam.googleapis.com/projects/-/serviceAccounts/my-service-account@iam.gserviceaccount.com``.

            - ``principalSet://goog/group/{group_id}``: A Google group.
              For example,
              ``principalSet://goog/group/admins@example.com``.

            - ``principalSet://goog/cloudIdentityCustomerId/{customer_id}``:
              All of the principals associated with the specified Google
              Workspace or Cloud Identity customer ID. For example,
              ``principalSet://goog/cloudIdentityCustomerId/C01Abc35``.

            If an identifier that was previously set on a policy is soft
            deleted, then calls to read that policy will return the
            identifier with a deleted prefix. Users cannot set
            identifiers with this syntax.

            - ``deleted:principal://goog/subject/{email_id}?uid={uid}``:
              A specific Google Account that was deleted recently. For
              example,
              ``deleted:principal://goog/subject/alice@example.com?uid=1234567890``.
              If the Google Account is recovered, this identifier
              reverts to the standard identifier for a Google Account.

            - ``deleted:principalSet://goog/group/{group_id}?uid={uid}``:
              A Google group that was deleted recently. For example,
              ``deleted:principalSet://goog/group/admins@example.com?uid=1234567890``.
              If the Google group is restored, this identifier reverts
              to the standard identifier for a Google group.

            - ``deleted:principal://iam.googleapis.com/projects/-/serviceAccounts/{service_account_id}?uid={uid}``:
              A Google Cloud service account that was deleted recently.
              For example,
              ``deleted:principal://iam.googleapis.com/projects/-/serviceAccounts/my-service-account@iam.gserviceaccount.com?uid=1234567890``.
              If the service account is undeleted, this identifier
              reverts to the standard identifier for a service account.
        excluded_principals (MutableSequence[str]):
            Optional. The identities that are excluded from the access
            policy rule, even if they are listed in the ``principals``.
            For example, you could add a Google group to the
            ``principals``, then exclude specific users who belong to
            that group.
        operation (google.cloud.iam_v3beta.types.AccessPolicyRule.Operation):
            Required. Attributes that are used to
            determine whether this rule applies to a
            request.
        conditions (MutableMapping[str, google.type.expr_pb2.Expr]):
            Optional. The conditions that determine whether this rule
            applies to a request. Conditions are identified by their
            key, which is the FQDN of the service that they are relevant
            to. For example:

            ::

               "conditions": {
                "iam.googleapis.com": {
                 "expression": <cel expression>
                }
               }

            Each rule is evaluated independently. If this rule does not
            apply to a request, other rules might still apply. Currently
            supported keys are as follows:

            - ``eventarc.googleapis.com``: Can use ``CEL`` functions
              that evaluate resource fields.

            - ``iam.googleapis.com``: Can use ``CEL`` functions that
              evaluate `resource
              tags <https://cloud.google.com/iam/help/conditions/resource-tags>`__
              and combine them using boolean and logical operators.
              Other functions and operators are not supported.
    """

    class Effect(proto.Enum):
        r"""An effect to describe the access relationship.

        Values:
            EFFECT_UNSPECIFIED (0):
                The effect is unspecified.
            DENY (1):
                The policy will deny access if it evaluates
                to true.
            ALLOW (2):
                The policy will grant access if it evaluates
                to true.
        """

        EFFECT_UNSPECIFIED = 0
        DENY = 1
        ALLOW = 2

    class Operation(proto.Message):
        r"""Attributes that are used to determine whether this rule
        applies to a request.

        Attributes:
            permissions (MutableSequence[str]):
                Optional. The permissions that are explicitly affected by
                this rule. Each permission uses the format
                ``{service_fqdn}/{resource}.{verb}``, where
                ``{service_fqdn}`` is the fully qualified domain name for
                the service. Currently supported permissions are as follows:

                - ``eventarc.googleapis.com/messageBuses.publish``.
            excluded_permissions (MutableSequence[str]):
                Optional. Specifies the permissions that this rule excludes
                from the set of affected permissions given by
                ``permissions``. If a permission appears in ``permissions``
                *and* in ``excluded_permissions`` then it will *not* be
                subject to the policy effect.

                The excluded permissions can be specified using the same
                syntax as ``permissions``.
        """

        permissions: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        excluded_permissions: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )

    description: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    effect: Effect = proto.Field(
        proto.ENUM,
        number=2,
        optional=True,
        enum=Effect,
    )
    principals: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    excluded_principals: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    operation: Operation = proto.Field(
        proto.MESSAGE,
        number=10,
        message=Operation,
    )
    conditions: MutableMapping[str, expr_pb2.Expr] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=9,
        message=expr_pb2.Expr,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
