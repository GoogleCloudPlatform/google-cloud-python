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

__protobuf__ = proto.module(
    package="google.cloud.billing.v1",
    manifest={
        "BillingAccount",
        "ProjectBillingInfo",
        "GetBillingAccountRequest",
        "ListBillingAccountsRequest",
        "ListBillingAccountsResponse",
        "CreateBillingAccountRequest",
        "UpdateBillingAccountRequest",
        "ListProjectBillingInfoRequest",
        "ListProjectBillingInfoResponse",
        "GetProjectBillingInfoRequest",
        "UpdateProjectBillingInfoRequest",
        "MoveBillingAccountRequest",
    },
)


class BillingAccount(proto.Message):
    r"""A billing account in the `Google Cloud
    Console <https://console.cloud.google.com/>`__. You can assign a
    billing account to one or more projects.

    Attributes:
        name (str):
            Output only. The resource name of the billing account. The
            resource name has the form
            ``billingAccounts/{billing_account_id}``. For example,
            ``billingAccounts/012345-567890-ABCDEF`` would be the
            resource name for billing account ``012345-567890-ABCDEF``.
        open_ (bool):
            Output only. True if the billing account is
            open, and will therefore be charged for any
            usage on associated projects. False if the
            billing account is closed, and therefore
            projects associated with it are unable to use
            paid services.
        display_name (str):
            The display name given to the billing account, such as
            ``My Billing Account``. This name is displayed in the Google
            Cloud Console.
        master_billing_account (str):
            If this account is a
            `subaccount <https://cloud.google.com/billing/docs/concepts>`__,
            then this will be the resource name of the parent billing
            account that it is being resold through. Otherwise this will
            be empty.
        parent (str):
            Output only. The billing account's parent resource
            identifier. Use the ``MoveBillingAccount`` method to update
            the account's parent resource if it is a organization.
            Format:

            - ``organizations/{organization_id}``, for example,
              ``organizations/12345678``
            - ``billingAccounts/{billing_account_id}``, for example,
              ``billingAccounts/012345-567890-ABCDEF``
        currency_code (str):
            Optional. The currency in which the billing account is
            billed and charged, represented as an ISO 4217 code such as
            ``USD``.

            Billing account currency is determined at the time of
            billing account creation and cannot be updated subsequently,
            so this field should not be set on update requests. In
            addition, a subaccount always matches the currency of its
            parent billing account, so this field should not be set on
            subaccount creation requests. Clients can read this field to
            determine the currency of an existing billing account.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    open_: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    master_billing_account: str = proto.Field(
        proto.STRING,
        number=4,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=6,
    )
    currency_code: str = proto.Field(
        proto.STRING,
        number=7,
    )


class ProjectBillingInfo(proto.Message):
    r"""Encapsulation of billing information for a Google Cloud
    Console project. A project has at most one associated billing
    account at a time (but a billing account can be assigned to
    multiple projects).

    Attributes:
        name (str):
            Output only. The resource name for the
            ``ProjectBillingInfo``; has the form
            ``projects/{project_id}/billingInfo``. For example, the
            resource name for the billing information for project
            ``tokyo-rain-123`` would be
            ``projects/tokyo-rain-123/billingInfo``.
        project_id (str):
            Output only. The ID of the project that this
            ``ProjectBillingInfo`` represents, such as
            ``tokyo-rain-123``. This is a convenience field so that you
            don't need to parse the ``name`` field to obtain a project
            ID.
        billing_account_name (str):
            The resource name of the billing account associated with the
            project, if any. For example,
            ``billingAccounts/012345-567890-ABCDEF``.
        billing_enabled (bool):
            Output only. True if the project is
            associated with an open billing account, to
            which usage on the project is charged. False if
            the project is associated with a closed billing
            account, or no billing account at all, and
            therefore cannot use paid services.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    billing_account_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    billing_enabled: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class GetBillingAccountRequest(proto.Message):
    r"""Request message for ``GetBillingAccount``.

    Attributes:
        name (str):
            Required. The resource name of the billing account to
            retrieve. For example,
            ``billingAccounts/012345-567890-ABCDEF``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListBillingAccountsRequest(proto.Message):
    r"""Request message for ``ListBillingAccounts``.

    Attributes:
        page_size (int):
            Requested page size. The maximum page size is
            100; this is also the default.
        page_token (str):
            A token identifying a page of results to return. This should
            be a ``next_page_token`` value returned from a previous
            ``ListBillingAccounts`` call. If unspecified, the first page
            of results is returned.
        filter (str):
            Options for how to filter the returned billing accounts.
            This only supports filtering for
            `subaccounts <https://cloud.google.com/billing/docs/concepts>`__
            under a single provided parent billing account. (for
            example,
            ``master_billing_account=billingAccounts/012345-678901-ABCDEF``).
            Boolean algebra and other fields are not currently
            supported.
        parent (str):
            Optional. The parent resource to list billing accounts from.
            Format:

            - ``organizations/{organization_id}``, for example,
              ``organizations/12345678``
            - ``billingAccounts/{billing_account_id}``, for example,
              ``billingAccounts/012345-567890-ABCDEF``
    """

    page_size: int = proto.Field(
        proto.INT32,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=3,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListBillingAccountsResponse(proto.Message):
    r"""Response message for ``ListBillingAccounts``.

    Attributes:
        billing_accounts (MutableSequence[google.cloud.billing_v1.types.BillingAccount]):
            A list of billing accounts.
        next_page_token (str):
            A token to retrieve the next page of results. To retrieve
            the next page, call ``ListBillingAccounts`` again with the
            ``page_token`` field set to this value. This field is empty
            if there are no more results to retrieve.
    """

    @property
    def raw_page(self):
        return self

    billing_accounts: MutableSequence["BillingAccount"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="BillingAccount",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateBillingAccountRequest(proto.Message):
    r"""Request message for ``CreateBillingAccount``.

    Attributes:
        billing_account (google.cloud.billing_v1.types.BillingAccount):
            Required. The billing account resource to
            create. Currently CreateBillingAccount only
            supports subaccount creation, so any created
            billing accounts must be under a provided parent
            billing account.
        parent (str):
            Optional. The parent to create a billing account from.
            Format:

            - ``billingAccounts/{billing_account_id}``, for example,
              ``billingAccounts/012345-567890-ABCDEF``
    """

    billing_account: "BillingAccount" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="BillingAccount",
    )
    parent: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateBillingAccountRequest(proto.Message):
    r"""Request message for ``UpdateBillingAccount``.

    Attributes:
        name (str):
            Required. The name of the billing account
            resource to be updated.
        account (google.cloud.billing_v1.types.BillingAccount):
            Required. The billing account resource to
            replace the resource on the server.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The update mask applied to the resource. Only "display_name"
            is currently supported.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    account: "BillingAccount" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="BillingAccount",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


class ListProjectBillingInfoRequest(proto.Message):
    r"""Request message for ``ListProjectBillingInfo``.

    Attributes:
        name (str):
            Required. The resource name of the billing account
            associated with the projects that you want to list. For
            example, ``billingAccounts/012345-567890-ABCDEF``.
        page_size (int):
            Requested page size. The maximum page size is
            100; this is also the default.
        page_token (str):
            A token identifying a page of results to be returned. This
            should be a ``next_page_token`` value returned from a
            previous ``ListProjectBillingInfo`` call. If unspecified,
            the first page of results is returned.
    """

    name: str = proto.Field(
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


class ListProjectBillingInfoResponse(proto.Message):
    r"""Request message for ``ListProjectBillingInfoResponse``.

    Attributes:
        project_billing_info (MutableSequence[google.cloud.billing_v1.types.ProjectBillingInfo]):
            A list of ``ProjectBillingInfo`` resources representing the
            projects associated with the billing account.
        next_page_token (str):
            A token to retrieve the next page of results. To retrieve
            the next page, call ``ListProjectBillingInfo`` again with
            the ``page_token`` field set to this value. This field is
            empty if there are no more results to retrieve.
    """

    @property
    def raw_page(self):
        return self

    project_billing_info: MutableSequence["ProjectBillingInfo"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ProjectBillingInfo",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetProjectBillingInfoRequest(proto.Message):
    r"""Request message for ``GetProjectBillingInfo``.

    Attributes:
        name (str):
            Required. The resource name of the project for which billing
            information is retrieved. For example,
            ``projects/tokyo-rain-123``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateProjectBillingInfoRequest(proto.Message):
    r"""Request message for ``UpdateProjectBillingInfo``.

    Attributes:
        name (str):
            Required. The resource name of the project associated with
            the billing information that you want to update. For
            example, ``projects/tokyo-rain-123``.
        project_billing_info (google.cloud.billing_v1.types.ProjectBillingInfo):
            The new billing information for the project. Output-only
            fields are ignored; thus, you can leave empty all fields
            except ``billing_account_name``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project_billing_info: "ProjectBillingInfo" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ProjectBillingInfo",
    )


class MoveBillingAccountRequest(proto.Message):
    r"""Request message for ``MoveBillingAccount`` RPC.

    Attributes:
        name (str):
            Required. The resource name of the billing account to move.
            Must be of the form
            ``billingAccounts/{billing_account_id}``. The specified
            billing account cannot be a subaccount, since a subaccount
            always belongs to the same organization as its parent
            account.
        destination_parent (str):
            Required. The resource name of the Organization to move the
            billing account under. Must be of the form
            ``organizations/{organization_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    destination_parent: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
