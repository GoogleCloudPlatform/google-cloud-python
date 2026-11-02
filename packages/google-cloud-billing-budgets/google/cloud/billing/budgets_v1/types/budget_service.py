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

from google.cloud.billing.budgets_v1.types import budget_model

__protobuf__ = proto.module(
    package="google.cloud.billing.budgets.v1",
    manifest={
        "CreateBudgetRequest",
        "UpdateBudgetRequest",
        "GetBudgetRequest",
        "ListBudgetsRequest",
        "ListBudgetsResponse",
        "DeleteBudgetRequest",
    },
)


class CreateBudgetRequest(proto.Message):
    r"""Request for CreateBudget

    Attributes:
        parent (str):
            Required. The name of the billing account to create the
            budget in. Values are of the form
            ``billingAccounts/{billingAccountId}``.
        budget (google.cloud.billing.budgets_v1.types.Budget):
            Required. Budget to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    budget: budget_model.Budget = proto.Field(
        proto.MESSAGE,
        number=2,
        message=budget_model.Budget,
    )


class UpdateBudgetRequest(proto.Message):
    r"""Request for UpdateBudget

    Attributes:
        budget (google.cloud.billing.budgets_v1.types.Budget):
            Required. The updated budget object.
            The budget to update is specified by the budget
            name in the budget.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Indicates which fields in the provided budget to
            update. Read-only fields (such as ``name``) cannot be
            changed. If this is not provided, then only fields with
            non-default values from the request are updated. See
            https://developers.google.com/protocol-buffers/docs/proto3#default
            for more details about default values.
    """

    budget: budget_model.Budget = proto.Field(
        proto.MESSAGE,
        number=1,
        message=budget_model.Budget,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetBudgetRequest(proto.Message):
    r"""Request for GetBudget

    Attributes:
        name (str):
            Required. Name of budget to get. Values are of the form
            ``billingAccounts/{billingAccountId}/budgets/{budgetId}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListBudgetsRequest(proto.Message):
    r"""Request for ListBudgets

    Attributes:
        parent (str):
            Required. Name of billing account to list budgets under.
            Values are of the form
            ``billingAccounts/{billingAccountId}``.
        scope (str):
            Optional. Set the scope of the budgets to be
            returned, in the format of the resource name.
            The scope of a budget is the cost that it
            tracks, such as costs for a single project, or
            the costs for all projects in a folder. Only
            project scope (in the format of
            "projects/project-id" or "projects/123") is
            supported in this field. When this field is set
            to a project's resource name, the budgets
            returned are tracking the costs for that
            project.
        page_size (int):
            Optional. The maximum number of budgets to
            return per page. The default and maximum value
            are 100.
        page_token (str):
            Optional. The value returned by the last
            ``ListBudgetsResponse`` which indicates that this is a
            continuation of a prior ``ListBudgets`` call, and that the
            system should return the next page of data.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    scope: str = proto.Field(
        proto.STRING,
        number=4,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListBudgetsResponse(proto.Message):
    r"""Response for ListBudgets

    Attributes:
        budgets (MutableSequence[google.cloud.billing.budgets_v1.types.Budget]):
            List of the budgets owned by the requested
            billing account.
        next_page_token (str):
            If not empty, indicates that there may be more budgets that
            match the request; this value should be passed in a new
            ``ListBudgetsRequest``.
    """

    @property
    def raw_page(self):
        return self

    budgets: MutableSequence[budget_model.Budget] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=budget_model.Budget,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteBudgetRequest(proto.Message):
    r"""Request for DeleteBudget

    Attributes:
        name (str):
            Required. Name of the budget to delete. Values are of the
            form
            ``billingAccounts/{billingAccountId}/budgets/{budgetId}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
