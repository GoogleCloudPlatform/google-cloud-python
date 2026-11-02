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

import google.rpc.status_pb2 as status_pb2  # type: ignore
import google.type.interval_pb2 as interval_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.chronicle.v1",
    manifest={
        "ListRuleExecutionErrorsRequest",
        "ListRuleExecutionErrorsResponse",
        "RuleExecutionError",
    },
)


class ListRuleExecutionErrorsRequest(proto.Message):
    r"""Request message for ListRuleExecutionErrors.

    Attributes:
        parent (str):
            Required. The instance to list rule execution
            errors from. Format:

            projects/{project}/locations/{location}/instances/{instance}
        page_size (int):
            The maximum number of rule execution errors
            to return. The service may return fewer than
            this value. If unspecified, at most 1000 rule
            execution errors will be returned. The maximum
            value is 10000; values above 10000 will be
            coerced to 10000.
        page_token (str):
            A page token, received from a previous
            ``ListRuleExecutionErrors`` call. Provide this to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``ListRuleExecutionErrors`` must match the call that
            provided the page token.
        filter (str):
            A filter that can be used to retrieve specific rule
            execution errors. Only the following filters are allowed:

            ::

                 rule = "{Rule.name}"
                 curated_rule = "{CuratedRule.name}"

            The value for rule or curated_rule must be a valid rule
            resource name or a valid curated rule resource name
            specified in quotes.

            For 'rule', an optional 'revision_id' can be specified which
            can be used to fetch errors for a given revision of the
            rule. A '-' is also allowed to fetch errors across all
            revisions of the rule. If unspecified, only errors
            corresponding to the most recent revision of the rule will
            be returned. So these variations are all allowed:

            ::

                 rule = "{Rule.name}"
                 rule = "{Rule.name}@{Rule.revision_id}"
                 rule = "{Rule.name}@-"

            Revision IDs are not supported for curated rules.
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


class ListRuleExecutionErrorsResponse(proto.Message):
    r"""Response message for ListRuleExecutionErrors.

    Attributes:
        rule_execution_errors (MutableSequence[google.cloud.chronicle_v1.types.RuleExecutionError]):
            List of rule execution errors.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    rule_execution_errors: MutableSequence["RuleExecutionError"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="RuleExecutionError",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RuleExecutionError(proto.Message):
    r"""The RuleExecutionError resource represents an error generated
    from running/deploying a rule.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        rule (str):
            Output only. The resource name of the rule
            that generated the rule execution error.

            This field is a member of `oneof`_ ``source``.
        curated_rule (str):
            Output only. The resource name of the curated
            rule that generated the rule execution error.

            This field is a member of `oneof`_ ``source``.
        name (str):
            Output only. The resource name of the rule execution error.
            Format:
            projects/{project}/locations/{location}/instances/{instance}/ruleExecutionErrors/{rule_execution_error}
        error (google.rpc.status_pb2.Status):
            Output only. The error status corresponding
            with the rule execution error.
        time_range (google.type.interval_pb2.Interval):
            Output only. The event time range that the
            rule execution error corresponds with.
    """

    rule: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="source",
    )
    curated_rule: str = proto.Field(
        proto.STRING,
        number=5,
        oneof="source",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=2,
        message=status_pb2.Status,
    )
    time_range: interval_pb2.Interval = proto.Field(
        proto.MESSAGE,
        number=3,
        message=interval_pb2.Interval,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
