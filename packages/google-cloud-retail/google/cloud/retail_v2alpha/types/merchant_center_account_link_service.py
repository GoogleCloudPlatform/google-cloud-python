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

from google.cloud.retail_v2alpha.types import (
    merchant_center_account_link as gcr_merchant_center_account_link,
)

__protobuf__ = proto.module(
    package="google.cloud.retail.v2alpha",
    manifest={
        "ListMerchantCenterAccountLinksRequest",
        "ListMerchantCenterAccountLinksResponse",
        "CreateMerchantCenterAccountLinkRequest",
        "DeleteMerchantCenterAccountLinkRequest",
    },
)


class ListMerchantCenterAccountLinksRequest(proto.Message):
    r"""Request for
    [MerchantCenterAccountLinkService.ListMerchantCenterAccountLinks][google.cloud.retail.v2alpha.MerchantCenterAccountLinkService.ListMerchantCenterAccountLinks]
    method.

    Attributes:
        parent (str):
            Required. The parent Catalog of the resource. It must match
            this format:
            ``projects/{PROJECT_NUMBER}/locations/global/catalogs/{CATALOG_ID}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListMerchantCenterAccountLinksResponse(proto.Message):
    r"""Response for
    [MerchantCenterAccountLinkService.ListMerchantCenterAccountLinks][google.cloud.retail.v2alpha.MerchantCenterAccountLinkService.ListMerchantCenterAccountLinks]
    method.

    Attributes:
        merchant_center_account_links (MutableSequence[google.cloud.retail_v2alpha.types.MerchantCenterAccountLink]):
            The links.
    """

    merchant_center_account_links: MutableSequence[
        gcr_merchant_center_account_link.MerchantCenterAccountLink
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcr_merchant_center_account_link.MerchantCenterAccountLink,
    )


class CreateMerchantCenterAccountLinkRequest(proto.Message):
    r"""Request for
    [MerchantCenterAccountLinkService.CreateMerchantCenterAccountLink][google.cloud.retail.v2alpha.MerchantCenterAccountLinkService.CreateMerchantCenterAccountLink]
    method.

    Attributes:
        parent (str):
            Required. The branch resource where this
            MerchantCenterAccountLink will be created. Format:
            ``projects/{PROJECT_NUMBER}/locations/global/catalogs/{CATALOG_ID}``
        merchant_center_account_link (google.cloud.retail_v2alpha.types.MerchantCenterAccountLink):
            Required. The
            [MerchantCenterAccountLink][google.cloud.retail.v2alpha.MerchantCenterAccountLink]
            to create.

            If the caller does not have permission to create the
            [MerchantCenterAccountLink][google.cloud.retail.v2alpha.MerchantCenterAccountLink],
            regardless of whether or not it exists, a PERMISSION_DENIED
            error is returned.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    merchant_center_account_link: gcr_merchant_center_account_link.MerchantCenterAccountLink = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcr_merchant_center_account_link.MerchantCenterAccountLink,
    )


class DeleteMerchantCenterAccountLinkRequest(proto.Message):
    r"""Request for
    [MerchantCenterAccountLinkService.DeleteMerchantCenterAccountLink][google.cloud.retail.v2alpha.MerchantCenterAccountLinkService.DeleteMerchantCenterAccountLink]
    method.

    Attributes:
        name (str):
            Required. Full resource name. Format:
            ``projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/merchantCenterAccountLinks/{merchant_center_account_link_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
