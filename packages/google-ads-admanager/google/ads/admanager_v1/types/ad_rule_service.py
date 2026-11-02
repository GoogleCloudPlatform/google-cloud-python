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
import proto  # type: ignore

from google.ads.admanager_v1.types import ad_rule_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetAdRuleRequest",
        "ListAdRulesRequest",
        "ListAdRulesResponse",
        "CreateAdRuleRequest",
        "BatchCreateAdRulesRequest",
        "BatchCreateAdRulesResponse",
        "UpdateAdRuleRequest",
        "BatchUpdateAdRulesRequest",
        "BatchUpdateAdRulesResponse",
        "BatchActivateAdRulesRequest",
        "BatchActivateAdRulesResponse",
        "BatchDeactivateAdRulesRequest",
        "BatchDeactivateAdRulesResponse",
        "BatchDeleteAdRulesRequest",
    },
)


class GetAdRuleRequest(proto.Message):
    r"""Request object for ``GetAdRule`` method.

    Attributes:
        name (str):
            Required. The resource name of the AdRule. Format:
            ``networks/{network_code}/adRules/{ad_rule_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAdRulesRequest(proto.Message):
    r"""Request object for ``ListAdRules`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of AdRules.
            Format: ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of ``AdRules`` to return. The
            service may return fewer than this value. If unspecified, at
            most 50 ``AdRules`` will be returned. The maximum value is
            1000; values greater than 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListAdRules`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListAdRules`` must match the call that provided the page
            token.
        filter (str):
            Optional. Expression to filter the response. See syntax
            details at
            https://developers.google.com/ad-manager/api/beta/filters

            **Filterable fields:**

            - ``displayName``
            - ``name``
            - ``priority``
            - ``status``
        order_by (str):
            Optional. Expression to specify sorting
            order. See syntax details at
            https://developers.google.com/ad-manager/api/beta/filters#order
        skip (int):
            Optional. Number of individual resources to
            skip while paginating.
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
    skip: int = proto.Field(
        proto.INT32,
        number=6,
    )


class ListAdRulesResponse(proto.Message):
    r"""Response object for ``ListAdRulesRequest`` containing matching
    ``AdRule`` objects.

    Attributes:
        ad_rules (MutableSequence[google.ads.admanager_v1.types.AdRule]):
            The ``AdRule`` objects from the specified network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of ``AdRule`` objects. If a filter was included
            in the request, this reflects the total number after the
            filtering is applied.

            ``total_size`` won't be calculated in the response unless it
            has been included in a response field mask. The response
            field mask can be provided to the method by using the URL
            parameter ``$fields`` or ``fields``, or by using the
            HTTP/gRPC header ``X-Goog-FieldMask``.

            For more information, see
            https://developers.google.com/ad-manager/api/beta/field-masks
    """

    @property
    def raw_page(self):
        return self

    ad_rules: MutableSequence[ad_rule_messages.AdRule] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=ad_rule_messages.AdRule,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CreateAdRuleRequest(proto.Message):
    r"""Request object for ``CreateAdRule`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this ``AdRule`` will be
            created. Format: ``networks/{network_code}``
        ad_rule (google.ads.admanager_v1.types.AdRule):
            Required. The ``AdRule`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ad_rule: ad_rule_messages.AdRule = proto.Field(
        proto.MESSAGE,
        number=2,
        message=ad_rule_messages.AdRule,
    )


class BatchCreateAdRulesRequest(proto.Message):
    r"""Request object for ``BatchCreateAdRules`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``AdRules`` will be
            created. Format: ``networks/{network_code}`` The parent
            field in the CreateAdRuleRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.CreateAdRuleRequest]):
            Required. The ``AdRule`` objects to create. A maximum of 100
            objects can be created in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateAdRuleRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateAdRuleRequest",
    )


class BatchCreateAdRulesResponse(proto.Message):
    r"""Response object for ``BatchCreateAdRules`` method.

    Attributes:
        ad_rules (MutableSequence[google.ads.admanager_v1.types.AdRule]):
            The ``AdRule`` objects created.
    """

    ad_rules: MutableSequence[ad_rule_messages.AdRule] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=ad_rule_messages.AdRule,
    )


class UpdateAdRuleRequest(proto.Message):
    r"""Request object for ``UpdateAdRule`` method.

    Attributes:
        ad_rule (google.ads.admanager_v1.types.AdRule):
            Required. The ``AdRule`` to update.

            The ``AdRule``'s ``name`` is used to identify the ``AdRule``
            to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    ad_rule: ad_rule_messages.AdRule = proto.Field(
        proto.MESSAGE,
        number=1,
        message=ad_rule_messages.AdRule,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateAdRulesRequest(proto.Message):
    r"""Request object for ``BatchUpdateAdRules`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``AdRules`` will be
            updated. Format: ``networks/{network_code}`` The parent
            field in the UpdateAdRuleRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.UpdateAdRuleRequest]):
            Required. The ``AdRule`` objects to update. A maximum of 100
            objects can be updated in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateAdRuleRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdateAdRuleRequest",
    )


class BatchUpdateAdRulesResponse(proto.Message):
    r"""Response object for ``BatchUpdateAdRules`` method.

    Attributes:
        ad_rules (MutableSequence[google.ads.admanager_v1.types.AdRule]):
            The ``AdRule`` objects updated.
    """

    ad_rules: MutableSequence[ad_rule_messages.AdRule] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=ad_rule_messages.AdRule,
    )


class BatchActivateAdRulesRequest(proto.Message):
    r"""Request object for ``BatchActivateAdRules`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. Resource names for the AdRule. Format:
            ``networks/{network_code}/adRules/{ad_rule}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchActivateAdRulesResponse(proto.Message):
    r"""Response object for ``BatchActivateAdRules`` method."""


class BatchDeactivateAdRulesRequest(proto.Message):
    r"""Request object for ``BatchDeactivateAdRules`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. Resource names for the AdRule. Format:
            ``networks/{network_code}/adRules/{ad_rule}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchDeactivateAdRulesResponse(proto.Message):
    r"""Response object for ``BatchDeactivateAdRules`` method."""


class BatchDeleteAdRulesRequest(proto.Message):
    r"""Request object for ``BatchDeleteAdRules`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. Resource names for the AdRule. Format:
            ``networks/{network_code}/adRules/{ad_rule}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
