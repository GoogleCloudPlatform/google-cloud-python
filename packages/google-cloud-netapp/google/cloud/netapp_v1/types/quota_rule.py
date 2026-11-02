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
    package="google.cloud.netapp.v1",
    manifest={
        "ListQuotaRulesRequest",
        "ListQuotaRulesResponse",
        "GetQuotaRuleRequest",
        "CreateQuotaRuleRequest",
        "UpdateQuotaRuleRequest",
        "DeleteQuotaRuleRequest",
        "QuotaRule",
    },
)


class ListQuotaRulesRequest(proto.Message):
    r"""ListQuotaRulesRequest for listing quota rules.

    Attributes:
        parent (str):
            Required. Parent value for
            ListQuotaRulesRequest
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, the server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering results
        order_by (str):
            Optional. Hint for how to order the results
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


class ListQuotaRulesResponse(proto.Message):
    r"""ListQuotaRulesResponse is the response to a
    ListQuotaRulesRequest.

    Attributes:
        quota_rules (MutableSequence[google.cloud.netapp_v1.types.QuotaRule]):
            List of quota rules
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    quota_rules: MutableSequence["QuotaRule"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="QuotaRule",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetQuotaRuleRequest(proto.Message):
    r"""GetQuotaRuleRequest for getting a quota rule.

    Attributes:
        name (str):
            Required. Name of the quota rule
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateQuotaRuleRequest(proto.Message):
    r"""CreateQuotaRuleRequest for creating a quota rule.

    Attributes:
        parent (str):
            Required. Parent value for
            CreateQuotaRuleRequest
        quota_rule (google.cloud.netapp_v1.types.QuotaRule):
            Required. Fields of the to be created quota
            rule.
        quota_rule_id (str):
            Required. ID of the quota rule to create.
            Must be unique within the parent resource. Must
            contain only letters, numbers, underscore and
            hyphen, with the first character a letter or
            underscore, the last a letter or underscore or a
            number, and a 63 character maximum.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    quota_rule: "QuotaRule" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="QuotaRule",
    )
    quota_rule_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateQuotaRuleRequest(proto.Message):
    r"""UpdateQuotaRuleRequest for updating a quota rule.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the Quota Rule resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        quota_rule (google.cloud.netapp_v1.types.QuotaRule):
            Required. The quota rule being updated
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    quota_rule: "QuotaRule" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="QuotaRule",
    )


class DeleteQuotaRuleRequest(proto.Message):
    r"""DeleteQuotaRuleRequest for deleting a single quota rule.

    Attributes:
        name (str):
            Required. Name of the quota rule.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class QuotaRule(proto.Message):
    r"""QuotaRule specifies the maximum disk space a user or group
    can use within a volume. They can be used for creating default
    and individual quota rules.

    Attributes:
        name (str):
            Identifier. The resource name of the quota rule. Format:
            ``projects/{project_number}/locations/{location_id}/volumes/volumes/{volume_id}/quotaRules/{quota_rule_id}``.
        target (str):
            Optional. The quota rule applies to the
            specified user or group, identified by a Unix
            UID/GID, Windows SID, or null for default.
        type_ (google.cloud.netapp_v1.types.QuotaRule.Type):
            Required. The type of quota rule.
        disk_limit_mib (int):
            Required. The maximum allowed disk space in
            MiB.
        state (google.cloud.netapp_v1.types.QuotaRule.State):
            Output only. State of the quota rule
        state_details (str):
            Output only. State details of the quota rule
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time of the quota rule
        description (str):
            Optional. Description of the quota rule
        labels (MutableMapping[str, str]):
            Optional. Labels of the quota rule
    """

    class Type(proto.Enum):
        r"""Types of Quota Rule

        Values:
            TYPE_UNSPECIFIED (0):
                Unspecified type for quota rule
            INDIVIDUAL_USER_QUOTA (1):
                Individual user quota rule
            INDIVIDUAL_GROUP_QUOTA (2):
                Individual group quota rule
            DEFAULT_USER_QUOTA (3):
                Default user quota rule
            DEFAULT_GROUP_QUOTA (4):
                Default group quota rule
        """

        TYPE_UNSPECIFIED = 0
        INDIVIDUAL_USER_QUOTA = 1
        INDIVIDUAL_GROUP_QUOTA = 2
        DEFAULT_USER_QUOTA = 3
        DEFAULT_GROUP_QUOTA = 4

    class State(proto.Enum):
        r"""Quota Rule states

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state for quota rule
            CREATING (1):
                Quota rule is creating
            UPDATING (2):
                Quota rule is updating
            DELETING (3):
                Quota rule is deleting
            READY (4):
                Quota rule is ready
            ERROR (5):
                Quota rule is in error state.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        UPDATING = 2
        DELETING = 3
        READY = 4
        ERROR = 5

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target: str = proto.Field(
        proto.STRING,
        number=2,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=3,
        enum=Type,
    )
    disk_limit_mib: int = proto.Field(
        proto.INT32,
        number=4,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=6,
        enum=State,
    )
    state_details: str = proto.Field(
        proto.STRING,
        number=7,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    description: str = proto.Field(
        proto.STRING,
        number=9,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=10,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
