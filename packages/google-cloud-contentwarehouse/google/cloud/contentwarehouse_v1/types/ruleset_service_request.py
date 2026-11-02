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

from google.cloud.contentwarehouse_v1.types import rule_engine

__protobuf__ = proto.module(
    package="google.cloud.contentwarehouse.v1",
    manifest={
        "CreateRuleSetRequest",
        "GetRuleSetRequest",
        "UpdateRuleSetRequest",
        "DeleteRuleSetRequest",
        "ListRuleSetsRequest",
        "ListRuleSetsResponse",
    },
)


class CreateRuleSetRequest(proto.Message):
    r"""Request message for RuleSetService.CreateRuleSet.

    Attributes:
        parent (str):
            Required. The parent name. Format:
            projects/{project_number}/locations/{location}.
        rule_set (google.cloud.contentwarehouse_v1.types.RuleSet):
            Required. The rule set to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rule_set: rule_engine.RuleSet = proto.Field(
        proto.MESSAGE,
        number=2,
        message=rule_engine.RuleSet,
    )


class GetRuleSetRequest(proto.Message):
    r"""Request message for RuleSetService.GetRuleSet.

    Attributes:
        name (str):
            Required. The name of the rule set to retrieve. Format:
            projects/{project_number}/locations/{location}/ruleSets/{rule_set_id}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateRuleSetRequest(proto.Message):
    r"""Request message for RuleSetService.UpdateRuleSet.

    Attributes:
        name (str):
            Required. The name of the rule set to update. Format:
            projects/{project_number}/locations/{location}/ruleSets/{rule_set_id}.
        rule_set (google.cloud.contentwarehouse_v1.types.RuleSet):
            Required. The rule set to update.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rule_set: rule_engine.RuleSet = proto.Field(
        proto.MESSAGE,
        number=2,
        message=rule_engine.RuleSet,
    )


class DeleteRuleSetRequest(proto.Message):
    r"""Request message for RuleSetService.DeleteRuleSet.

    Attributes:
        name (str):
            Required. The name of the rule set to delete. Format:
            projects/{project_number}/locations/{location}/ruleSets/{rule_set_id}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListRuleSetsRequest(proto.Message):
    r"""Request message for RuleSetService.ListRuleSets.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            document. Format:
            projects/{project_number}/locations/{location}.
        page_size (int):
            The maximum number of rule sets to return.
            The service may return fewer than this value. If
            unspecified, at most 50 rule sets will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            A page token, received from a previous ``ListRuleSets``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListRuleSets`` must match the call that provided the page
            token.
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


class ListRuleSetsResponse(proto.Message):
    r"""Response message for RuleSetService.ListRuleSets.

    Attributes:
        rule_sets (MutableSequence[google.cloud.contentwarehouse_v1.types.RuleSet]):
            The rule sets from the specified parent.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    rule_sets: MutableSequence[rule_engine.RuleSet] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=rule_engine.RuleSet,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
