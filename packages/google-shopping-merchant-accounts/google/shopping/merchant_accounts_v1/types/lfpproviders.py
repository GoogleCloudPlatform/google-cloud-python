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

import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.shopping.merchant.accounts.v1",
    manifest={
        "LfpProvider",
        "FindLfpProvidersRequest",
        "FindLfpProvidersResponse",
        "LinkLfpProviderRequest",
        "LinkLfpProviderResponse",
    },
)


class LfpProvider(proto.Message):
    r"""Collection of information related to a Local Feed Partnership
    (LFP) provider.

    Attributes:
        name (str):
            Identifier. The resource name of the LFP provider. Format:
            ``accounts/{account}/omnichannelSettings/{omnichannel_setting}/lfpProviders/{lfp_provider}``
        region_code (str):
            Output only. Region code defined by
            `CLDR <https://cldr.unicode.org/>`__.
        display_name (str):
            The display name of the LFP provider.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    region_code: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )


class FindLfpProvidersRequest(proto.Message):
    r"""Request message for the FindLfpProviders method.

    Attributes:
        parent (str):
            Required. The name of the parent resource under which the
            LFP providers are found. Format:
            ``accounts/{account}/omnichannelSettings/{omnichannel_setting}``.
        page_size (int):
            Optional. The maximum number of ``LfpProvider`` resources to
            return. The service returns fewer than this value if the
            number of lfp providers is less that than the ``pageSize``.
            The default value is 50. The maximum value is 1000; If a
            value higher than the maximum is specified, then the
            ``pageSize`` will default to the maximum.
        page_token (str):
            Optional. A page token, received from a previous
            ``FindLfpProviders`` call. Provide the page token to
            retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``FindLfpProviders`` must match the call that provided the
            page token.
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


class FindLfpProvidersResponse(proto.Message):
    r"""Response message for the FindLfpProviders method.

    Attributes:
        lfp_providers (MutableSequence[google.shopping.merchant_accounts_v1.types.LfpProvider]):
            The LFP providers from the specified merchant
            in the specified country.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    lfp_providers: MutableSequence["LfpProvider"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="LfpProvider",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class LinkLfpProviderRequest(proto.Message):
    r"""Request message for the LinkLfpProvider method.

    Attributes:
        name (str):
            Required. The name of the LFP provider resource to link.
            Format:
            ``accounts/{account}/omnichannelSettings/{omnichannel_setting}/lfpProviders/{lfp_provider}``.
            The ``lfp_provider`` is the LFP provider ID.
        external_account_id (str):
            Required. The external account ID by which
            this merchant is known to the LFP provider.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    external_account_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class LinkLfpProviderResponse(proto.Message):
    r"""Response message for the LinkLfpProvider method.

    Attributes:
        response (google.protobuf.empty_pb2.Empty):
            Empty response.
    """

    response: empty_pb2.Empty = proto.Field(
        proto.MESSAGE,
        number=1,
        message=empty_pb2.Empty,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
