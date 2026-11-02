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
import google.type.expr_pb2 as expr_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.devtools.artifactregistry.v1",
    manifest={
        "Rule",
        "ListRulesRequest",
        "ListRulesResponse",
        "GetRuleRequest",
        "CreateRuleRequest",
        "UpdateRuleRequest",
        "DeleteRuleRequest",
    },
)


class Rule(proto.Message):
    r"""A rule defines the deny or allow action of the operation it
    applies to and the conditions required for the rule to apply.
    You can set one rule for an entire repository and one rule for
    each package within.

    Attributes:
        name (str):
            The name of the rule, for example:
            ``projects/p1/locations/us-central1/repositories/repo1/rules/rule1``.
        action (google.cloud.artifactregistry_v1.types.Rule.Action):
            The action this rule takes.
        operation (google.cloud.artifactregistry_v1.types.Rule.Operation):

        condition (google.type.expr_pb2.Expr):
            Optional. A CEL expression for conditions
            that must be met in order for the rule to apply.
            If not provided, the rule matches all objects.
        package_id (str):
            The package ID the rule applies to.
            If empty, this rule applies to all packages
            inside the repository.
    """

    class Action(proto.Enum):
        r"""Defines the action of the rule.

        Values:
            ACTION_UNSPECIFIED (0):
                Action not specified.
            ALLOW (1):
                Allow the operation.
            DENY (2):
                Deny the operation.
        """

        ACTION_UNSPECIFIED = 0
        ALLOW = 1
        DENY = 2

    class Operation(proto.Enum):
        r"""The operation the rule applies to.

        Values:
            OPERATION_UNSPECIFIED (0):
                Operation not specified.
            DOWNLOAD (1):
                Download operation.
        """

        OPERATION_UNSPECIFIED = 0
        DOWNLOAD = 1

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    action: Action = proto.Field(
        proto.ENUM,
        number=2,
        enum=Action,
    )
    operation: Operation = proto.Field(
        proto.ENUM,
        number=3,
        enum=Operation,
    )
    condition: expr_pb2.Expr = proto.Field(
        proto.MESSAGE,
        number=4,
        message=expr_pb2.Expr,
    )
    package_id: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListRulesRequest(proto.Message):
    r"""The request to list rules.

    Attributes:
        parent (str):
            Required. The name of the parent repository whose rules will
            be listed. For example:
            ``projects/p1/locations/us-central1/repositories/repo1``.
        page_size (int):
            The maximum number of rules to return.
            Maximum page size is 1,000.
        page_token (str):
            The next_page_token value returned from a previous list
            request, if any.
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


class ListRulesResponse(proto.Message):
    r"""The response from listing rules.

    Attributes:
        rules (MutableSequence[google.cloud.artifactregistry_v1.types.Rule]):
            The rules returned.
        next_page_token (str):
            The token to retrieve the next page of rules,
            or empty if there are no more rules to return.
    """

    @property
    def raw_page(self):
        return self

    rules: MutableSequence["Rule"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Rule",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetRuleRequest(proto.Message):
    r"""The request to retrieve a rule.

    Attributes:
        name (str):
            Required. The name of the rule to retrieve.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateRuleRequest(proto.Message):
    r"""The request to create a new rule.

    Attributes:
        parent (str):
            Required. The name of the parent resource
            where the rule will be created.
        rule_id (str):
            The rule id to use for this repository.
        rule (google.cloud.artifactregistry_v1.types.Rule):
            The rule to be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rule_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    rule: "Rule" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Rule",
    )


class UpdateRuleRequest(proto.Message):
    r"""The request to update a rule.

    Attributes:
        rule (google.cloud.artifactregistry_v1.types.Rule):
            The rule that replaces the resource on the
            server.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The update mask applies to the resource. For the
            ``FieldMask`` definition, see
            https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask
    """

    rule: "Rule" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Rule",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteRuleRequest(proto.Message):
    r"""The request to delete a rule.

    Attributes:
        name (str):
            Required. The name of the rule to delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
