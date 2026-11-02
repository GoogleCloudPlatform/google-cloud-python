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
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.networksecurity.v1",
    manifest={
        "GatewaySecurityPolicyRule",
        "CreateGatewaySecurityPolicyRuleRequest",
        "GetGatewaySecurityPolicyRuleRequest",
        "UpdateGatewaySecurityPolicyRuleRequest",
        "ListGatewaySecurityPolicyRulesRequest",
        "ListGatewaySecurityPolicyRulesResponse",
        "DeleteGatewaySecurityPolicyRuleRequest",
    },
)


class GatewaySecurityPolicyRule(proto.Message):
    r"""The GatewaySecurityPolicyRule resource is in a nested
    collection within a GatewaySecurityPolicy and represents a
    traffic matching condition and associated action to perform.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        basic_profile (google.cloud.network_security_v1.types.GatewaySecurityPolicyRule.BasicProfile):
            Required. Profile which tells what the
            primitive action should be.

            This field is a member of `oneof`_ ``profile``.
        name (str):
            Required. Immutable. Name of the resource. ame is the full
            resource name so
            projects/{project}/locations/{location}/gatewaySecurityPolicies/{gateway_security_policy}/rules/{rule}
            rule should match the pattern:
            (^\ `a-z <[a-z0-9-]{0,61}[a-z0-9]>`__?$).
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the rule was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the rule was updated.
        enabled (bool):
            Required. Whether the rule is enforced.
        priority (int):
            Required. Priority of the rule.
            Lower number corresponds to higher precedence.
        description (str):
            Optional. Free-text description of the
            resource.
        session_matcher (str):
            Required. CEL expression for matching on
            session criteria.
        application_matcher (str):
            Optional. CEL expression for matching on
            L7/application level criteria.
        tls_inspection_enabled (bool):
            Optional. Flag to enable TLS inspection of traffic matching
            on <session_matcher>, can only be true if the parent
            GatewaySecurityPolicy references a TLSInspectionConfig.
    """

    class BasicProfile(proto.Enum):
        r"""enum to define the primitive action.

        Values:
            BASIC_PROFILE_UNSPECIFIED (0):
                If there is not a mentioned action for the
                target.
            ALLOW (1):
                Allow the matched traffic.
            DENY (2):
                Deny the matched traffic.
        """

        BASIC_PROFILE_UNSPECIFIED = 0
        ALLOW = 1
        DENY = 2

    basic_profile: BasicProfile = proto.Field(
        proto.ENUM,
        number=9,
        oneof="profile",
        enum=BasicProfile,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    enabled: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    priority: int = proto.Field(
        proto.INT32,
        number=5,
    )
    description: str = proto.Field(
        proto.STRING,
        number=6,
    )
    session_matcher: str = proto.Field(
        proto.STRING,
        number=7,
    )
    application_matcher: str = proto.Field(
        proto.STRING,
        number=8,
    )
    tls_inspection_enabled: bool = proto.Field(
        proto.BOOL,
        number=10,
    )


class CreateGatewaySecurityPolicyRuleRequest(proto.Message):
    r"""Methods for GatewaySecurityPolicy
    RULES/GatewaySecurityPolicyRules. Request used by the
    CreateGatewaySecurityPolicyRule method.

    Attributes:
        parent (str):
            Required. The parent where this rule will be created. Format
            :
            projects/{project}/location/{location}/gatewaySecurityPolicies/\*
        gateway_security_policy_rule (google.cloud.network_security_v1.types.GatewaySecurityPolicyRule):
            Required. The rule to be created.
        gateway_security_policy_rule_id (str):
            The ID to use for the rule, which will become the final
            component of the rule's resource name. This value should be
            4-63 characters, and valid characters are /[a-z][0-9]-/.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    gateway_security_policy_rule: "GatewaySecurityPolicyRule" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="GatewaySecurityPolicyRule",
    )
    gateway_security_policy_rule_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GetGatewaySecurityPolicyRuleRequest(proto.Message):
    r"""Request used by the GetGatewaySecurityPolicyRule method.

    Attributes:
        name (str):
            Required. The name of the GatewaySecurityPolicyRule to
            retrieve. Format:
            projects/{project}/location/{location}/gatewaySecurityPolicies/*/rules/*
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateGatewaySecurityPolicyRuleRequest(proto.Message):
    r"""Request used by the UpdateGatewaySecurityPolicyRule method.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the GatewaySecurityPolicy resource by the
            update. The fields specified in the update_mask are relative
            to the resource, not the full request. A field will be
            overwritten if it is in the mask. If the user does not
            provide a mask then all fields will be overwritten.
        gateway_security_policy_rule (google.cloud.network_security_v1.types.GatewaySecurityPolicyRule):
            Required. Updated GatewaySecurityPolicyRule
            resource.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    gateway_security_policy_rule: "GatewaySecurityPolicyRule" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="GatewaySecurityPolicyRule",
    )


class ListGatewaySecurityPolicyRulesRequest(proto.Message):
    r"""Request used with the ListGatewaySecurityPolicyRules method.

    Attributes:
        parent (str):
            Required. The project, location and GatewaySecurityPolicy
            from which the GatewaySecurityPolicyRules should be listed,
            specified in the format
            ``projects/{project}/locations/{location}/gatewaySecurityPolicies/{gatewaySecurityPolicy}``.
        page_size (int):
            Maximum number of GatewaySecurityPolicyRules
            to return per call.
        page_token (str):
            The value returned by the last
            'ListGatewaySecurityPolicyRulesResponse'
            Indicates that this is a continuation of a prior
            'ListGatewaySecurityPolicyRules' call, and that
            the system should return the next page of data.
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


class ListGatewaySecurityPolicyRulesResponse(proto.Message):
    r"""Response returned by the ListGatewaySecurityPolicyRules
    method.

    Attributes:
        gateway_security_policy_rules (MutableSequence[google.cloud.network_security_v1.types.GatewaySecurityPolicyRule]):
            List of GatewaySecurityPolicyRule resources.
        next_page_token (str):
            If there might be more results than those appearing in this
            response, then 'next_page_token' is included. To get the
            next set of results, call this method again using the value
            of 'next_page_token' as 'page_token'.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    gateway_security_policy_rules: MutableSequence["GatewaySecurityPolicyRule"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="GatewaySecurityPolicyRule",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class DeleteGatewaySecurityPolicyRuleRequest(proto.Message):
    r"""Request used by the DeleteGatewaySecurityPolicyRule method.

    Attributes:
        name (str):
            Required. A name of the GatewaySecurityPolicyRule to delete.
            Must be in the format
            ``projects/{project}/locations/{location}/gatewaySecurityPolicies/{gatewaySecurityPolicy}/rules/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
