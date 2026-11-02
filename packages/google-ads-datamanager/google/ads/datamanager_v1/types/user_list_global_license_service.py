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

from google.ads.datamanager_v1.types import (
    user_list_global_license as gad_user_list_global_license,
)

__protobuf__ = proto.module(
    package="google.ads.datamanager.v1",
    manifest={
        "CreateUserListGlobalLicenseRequest",
        "UpdateUserListGlobalLicenseRequest",
        "GetUserListGlobalLicenseRequest",
        "ListUserListGlobalLicensesRequest",
        "ListUserListGlobalLicensesResponse",
        "ListUserListGlobalLicenseCustomerInfosRequest",
        "ListUserListGlobalLicenseCustomerInfosResponse",
    },
)


class CreateUserListGlobalLicenseRequest(proto.Message):
    r"""Request to create a
    [UserListGlobalLicense][google.ads.datamanager.v1.UserListGlobalLicense]
    resource.

    Attributes:
        parent (str):
            Required. The account that owns the user list being
            licensed. Should be in the format
            accountTypes/{ACCOUNT_TYPE}/accounts/{ACCOUNT_ID}
        user_list_global_license (google.ads.datamanager_v1.types.UserListGlobalLicense):
            Required. The user list global license to
            create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    user_list_global_license: gad_user_list_global_license.UserListGlobalLicense = (
        proto.Field(
            proto.MESSAGE,
            number=2,
            message=gad_user_list_global_license.UserListGlobalLicense,
        )
    )


class UpdateUserListGlobalLicenseRequest(proto.Message):
    r"""Request to update a
    [UserListGlobalLicense][google.ads.datamanager.v1.UserListGlobalLicense]
    resource.

    Attributes:
        user_list_global_license (google.ads.datamanager_v1.types.UserListGlobalLicense):
            Required. The licenses' ``name`` field is used to identify
            the license to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update. The special
            character ``*`` is not supported and an
            ``INVALID_UPDATE_MASK`` error will be thrown if used.
    """

    user_list_global_license: gad_user_list_global_license.UserListGlobalLicense = (
        proto.Field(
            proto.MESSAGE,
            number=1,
            message=gad_user_list_global_license.UserListGlobalLicense,
        )
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetUserListGlobalLicenseRequest(proto.Message):
    r"""Request to get a
    [UserListGlobalLicense][google.ads.datamanager.v1.UserListGlobalLicense]
    resource.

    Attributes:
        name (str):
            Required. The resource name of the user list
            global license.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListUserListGlobalLicensesRequest(proto.Message):
    r"""Request to list all
    [UserListGlobalLicense][google.ads.datamanager.v1.UserListGlobalLicense]
    resources for a given account.

    Attributes:
        parent (str):
            Required. The account whose licenses are being queried.
            Should be in the format
            accountTypes/{ACCOUNT_TYPE}/accounts/{ACCOUNT_ID}
        filter (str):
            Optional. A `filter string <https://google.aip.dev/160>`__
            to apply to the list request. All fields need to be on the
            left hand side of each condition (for example:
            ``user_list_id = 123``). Fields must be specified using
            either all `camel
            case <https://en.wikipedia.org/wiki/Camel_case>`__ or all
            `snake case <https://en.wikipedia.org/wiki/Snake_case>`__.
            Don't use a combination of camel case and snake case.

            **Supported Operations:**

            - ``AND``
            - ``=``
            - ``!=``
            - ``>``
            - ``>=``
            - ``<``
            - ``<=``

            **Supported Functions:**

            - ``IN(field, value1, value2, ...)``: returns true if the
              field matches any of the values. Example:
              ``IN(user_list_id, 123, 456)``

            **Unsupported Fields:**

            - ``name`` (use get method instead)
            - ``historical_pricings`` and all its subfields
            - ``pricing.start_time``
            - ``pricing.end_time``
        page_size (int):
            Optional. The maximum number of licenses to
            return. The service may return fewer than this
            value. If unspecified, at most 50 licenses will
            be returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListUserListGlobalLicense`` call. Provide this to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``ListUserListDirectLicense`` must match the call that
            provided the page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
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


class ListUserListGlobalLicensesResponse(proto.Message):
    r"""Response from the
    [ListUserListGlobalLicensesRequest][google.ads.datamanager.v1.ListUserListGlobalLicensesRequest].

    Attributes:
        user_list_global_licenses (MutableSequence[google.ads.datamanager_v1.types.UserListGlobalLicense]):
            The licenses for the given user list in the
            request.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    user_list_global_licenses: MutableSequence[
        gad_user_list_global_license.UserListGlobalLicense
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gad_user_list_global_license.UserListGlobalLicense,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListUserListGlobalLicenseCustomerInfosRequest(proto.Message):
    r"""Request to list all
    [UserListGlobalLicenseCustomerInfo][google.ads.datamanager.v1.UserListGlobalLicenseCustomerInfo]
    resources for a given user list global license.

    Attributes:
        parent (str):
            Required. The global license whose customer info are being
            queried. Should be in the format
            ``accountTypes/{ACCOUNT_TYPE}/accounts/{ACCOUNT_ID}/userListGlobalLicenses/{USER_LIST_GLOBAL_LICENSE_ID}``.
            To list all global license customer info under an account,
            replace the user list global license id with a '-' (for
            example,
            ``accountTypes/DATA_PARTNER/accounts/123/userListGlobalLicenses/-``)
        filter (str):
            Optional. A `filter string <https://google.aip.dev/160>`__
            to apply to the list request. All fields need to be on the
            left hand side of each condition (for example:
            ``user_list_id = 123``). Fields must be specified using
            either all `camel
            case <https://en.wikipedia.org/wiki/Camel_case>`__ or all
            `snake case <https://en.wikipedia.org/wiki/Snake_case>`__.
            Don't use a combination of camel case and snake case.

            **Supported Operations:**

            - ``AND``
            - ``=``
            - ``!=``
            - ``>``
            - ``>=``
            - ``<``
            - ``<=``

            **Supported Functions:**

            - ``IN(field, value1, value2, ...)``: returns true if the
              field matches any of the values. Example:
              ``IN(user_list_id, 123, 456)``

            **Unsupported Fields:**

            - ``name`` (use get method instead)
            - ``historical_pricings`` and all its subfields
            - ``pricing.start_time``
            - ``pricing.end_time``
        page_size (int):
            Optional. The maximum number of licenses to
            return. The service may return fewer than this
            value. If unspecified, at most 50 licenses will
            be returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListUserListDirectLicense`` call. Provide this to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``ListUserListDirectLicense`` must match the call that
            provided the page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
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


class ListUserListGlobalLicenseCustomerInfosResponse(proto.Message):
    r"""Response from the
    [ListUserListGlobalLicensesCustomerInfoRequest][google.ads.datamanager.v1.ListUserListGlobalLicensesCustomerInfoRequest].

    Attributes:
        user_list_global_license_customer_infos (MutableSequence[google.ads.datamanager_v1.types.UserListGlobalLicenseCustomerInfo]):
            The customer information for the given
            license in the request.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    user_list_global_license_customer_infos: MutableSequence[
        gad_user_list_global_license.UserListGlobalLicenseCustomerInfo
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gad_user_list_global_license.UserListGlobalLicenseCustomerInfo,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
