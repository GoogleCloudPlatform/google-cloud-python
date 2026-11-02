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

from google.cloud.asset_v1p1beta1.types import assets

__protobuf__ = proto.module(
    package="google.cloud.asset.v1p1beta1",
    manifest={
        "SearchAllResourcesRequest",
        "SearchAllResourcesResponse",
        "SearchAllIamPoliciesRequest",
        "SearchAllIamPoliciesResponse",
    },
)


class SearchAllResourcesRequest(proto.Message):
    r"""Search all resources request.

    Attributes:
        scope (str):
            Required. The relative name of an asset. The search is
            limited to the resources within the ``scope``. The allowed
            value must be:

            - Organization number (such as "organizations/123")
            - Folder number (such as "folders/1234")
            - Project number (such as "projects/12345")
            - Project ID (such as "projects/abc")
        query (str):
            Optional. The query statement.
        asset_types (MutableSequence[str]):
            Optional. A list of asset types that this
            request searches for. If empty, it will search
            all the supported asset types.
        page_size (int):
            Optional. The page size for search result pagination. Page
            size is capped at 500 even if a larger value is given. If
            set to zero, server will pick an appropriate default.
            Returned results may be fewer than requested. When this
            happens, there could be more results as long as
            ``next_page_token`` is returned.
        page_token (str):
            Optional. If present, then retrieve the next batch of
            results from the preceding call to this method.
            ``page_token`` must be the value of ``next_page_token`` from
            the previous response. The values of all other method
            parameters, must be identical to those in the previous call.
        order_by (str):
            Optional. A comma separated list of fields specifying the
            sorting order of the results. The default order is
            ascending. Add ``DESC`` after the field name to indicate
            descending order. Redundant space characters are ignored.
            For example, ``location DESC ,  name``.
    """

    scope: str = proto.Field(
        proto.STRING,
        number=1,
    )
    query: str = proto.Field(
        proto.STRING,
        number=2,
    )
    asset_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=5,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=10,
    )


class SearchAllResourcesResponse(proto.Message):
    r"""Search all resources response.

    Attributes:
        results (MutableSequence[google.cloud.asset_v1p1beta1.types.StandardResourceMetadata]):
            A list of resource that match the search
            query.
        next_page_token (str):
            If there are more results than those appearing in this
            response, then ``next_page_token`` is included. To get the
            next set of results, call this method again using the value
            of ``next_page_token`` as ``page_token``.
    """

    @property
    def raw_page(self):
        return self

    results: MutableSequence[assets.StandardResourceMetadata] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=assets.StandardResourceMetadata,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SearchAllIamPoliciesRequest(proto.Message):
    r"""Search all IAM policies request.

    Attributes:
        scope (str):
            Required. The relative name of an asset. The search is
            limited to the resources within the ``scope``. The allowed
            value must be:

            - Organization number (such as "organizations/123")
            - Folder number (such as "folders/1234")
            - Project number (such as "projects/12345")
            - Project ID (such as "projects/abc")
        query (str):
            Optional. The query statement. Examples:

            - "policy:myuser@mydomain.com"
            - "policy:(myuser@mydomain.com viewer)".
        page_size (int):
            Optional. The page size for search result pagination. Page
            size is capped at 500 even if a larger value is given. If
            set to zero, server will pick an appropriate default.
            Returned results may be fewer than requested. When this
            happens, there could be more results as long as
            ``next_page_token`` is returned.
        page_token (str):
            Optional. If present, retrieve the next batch of results
            from the preceding call to this method. ``page_token`` must
            be the value of ``next_page_token`` from the previous
            response. The values of all other method parameters must be
            identical to those in the previous call.
    """

    scope: str = proto.Field(
        proto.STRING,
        number=1,
    )
    query: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SearchAllIamPoliciesResponse(proto.Message):
    r"""Search all IAM policies response.

    Attributes:
        results (MutableSequence[google.cloud.asset_v1p1beta1.types.IamPolicySearchResult]):
            A list of IAM policies that match the search
            query. Related information such as the
            associated resource is returned along with the
            policy.
        next_page_token (str):
            Set if there are more results than those appearing in this
            response; to get the next set of results, call this method
            again, using this value as the ``page_token``.
    """

    @property
    def raw_page(self):
        return self

    results: MutableSequence[assets.IamPolicySearchResult] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=assets.IamPolicySearchResult,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
