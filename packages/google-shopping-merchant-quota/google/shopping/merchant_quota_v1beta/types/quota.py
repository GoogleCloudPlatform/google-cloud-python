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
    package="google.shopping.merchant.quota.v1beta",
    manifest={
        "QuotaGroup",
        "MethodDetails",
        "ListQuotaGroupsRequest",
        "ListQuotaGroupsResponse",
    },
)


class QuotaGroup(proto.Message):
    r"""The group information for methods in the Merchant API. The
    quota is shared between all methods in the group. Even if none
    of the methods within the group have usage the information for
    the group is returned.

    Attributes:
        name (str):
            Identifier. The resource name of the quota
            group. Format: accounts/{account}/quotas/{group}
            Note: There is no guarantee on the format of
            {group}
        quota_usage (int):
            Output only. The current quota usage, meaning
            the number of calls already made on a given day
            to the methods in the group. The daily quota
            limits reset at at 12:00 PM midday UTC.
        quota_limit (int):
            Output only. The maximum number of calls
            allowed per day for the group.
        quota_minute_limit (int):
            Output only. The maximum number of calls
            allowed per minute for the group.
        method_details (MutableSequence[google.shopping.merchant_quota_v1beta.types.MethodDetails]):
            Output only. List of all methods group quota
            applies to.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    quota_usage: int = proto.Field(
        proto.INT64,
        number=2,
    )
    quota_limit: int = proto.Field(
        proto.INT64,
        number=3,
    )
    quota_minute_limit: int = proto.Field(
        proto.INT64,
        number=5,
    )
    method_details: MutableSequence["MethodDetails"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="MethodDetails",
    )


class MethodDetails(proto.Message):
    r"""The method details per method in the Merchant API.

    Attributes:
        method (str):
            Output only. The name of the method for example
            ``products.list``.
        version (str):
            Output only. The API version that the method
            belongs to.
        subapi (str):
            Output only. The sub-API that the method
            belongs to.
        path (str):
            Output only. The path for the method such as
            ``products/v1/productInputs.insert``
    """

    method: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    subapi: str = proto.Field(
        proto.STRING,
        number=3,
    )
    path: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListQuotaGroupsRequest(proto.Message):
    r"""Request message for the ListQuotaGroups method.

    Attributes:
        parent (str):
            Required. The merchant account who owns the
            collection of method quotas Format:
            accounts/{account}
        page_size (int):
            Optional. The maximum number of quotas to
            return in the response, used for paging.
            Defaults to 500; values above 1000 will be
            coerced to 1000.
        page_token (str):
            Optional. Token (if provided) to retrieve the
            subsequent page. All other parameters must match
            the original call that provided the page token.
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


class ListQuotaGroupsResponse(proto.Message):
    r"""Response message for the ListMethodGroups method.

    Attributes:
        quota_groups (MutableSequence[google.shopping.merchant_quota_v1beta.types.QuotaGroup]):
            The methods, current quota usage and limits per each group.
            The quota is shared between all methods in the group. The
            groups are sorted in descending order based on
            [quotaUsage][google.shopping.merchant.quota.v1main.QuotaGroup.quota_usage].
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    quota_groups: MutableSequence["QuotaGroup"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="QuotaGroup",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
