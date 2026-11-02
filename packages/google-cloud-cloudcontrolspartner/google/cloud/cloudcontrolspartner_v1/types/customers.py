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

from google.cloud.cloudcontrolspartner_v1.types import (
    completion_state as gcc_completion_state,
)

__protobuf__ = proto.module(
    package="google.cloud.cloudcontrolspartner.v1",
    manifest={
        "Customer",
        "ListCustomersRequest",
        "ListCustomersResponse",
        "CreateCustomerRequest",
        "GetCustomerRequest",
        "CustomerOnboardingState",
        "CustomerOnboardingStep",
        "UpdateCustomerRequest",
        "DeleteCustomerRequest",
    },
)


class Customer(proto.Message):
    r"""Contains metadata around a Cloud Controls Partner Customer

    Attributes:
        name (str):
            Identifier. Format:
            ``organizations/{organization}/locations/{location}/customers/{customer}``
        display_name (str):
            Required. Display name for the customer
        customer_onboarding_state (google.cloud.cloudcontrolspartner_v1.types.CustomerOnboardingState):
            Output only. Container for customer
            onboarding steps
        is_onboarded (bool):
            Output only. Indicates whether a customer is
            fully onboarded
        organization_domain (str):
            Output only. The customer organization domain, extracted
            from CRM Organization’s display_name field. e.g.
            "google.com".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    customer_onboarding_state: "CustomerOnboardingState" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="CustomerOnboardingState",
    )
    is_onboarded: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    organization_domain: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListCustomersRequest(proto.Message):
    r"""Request to list customers

    Attributes:
        parent (str):
            Required. Parent resource Format:
            ``organizations/{organization}/locations/{location}``
        page_size (int):
            The maximum number of Customers to return.
            The service may return fewer than this value. If
            unspecified, at most 500 Customers will be
            returned.
        page_token (str):
            A page token, received from a previous ``ListCustomers``
            call. Provide this to retrieve the subsequent page.
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


class ListCustomersResponse(proto.Message):
    r"""Response message for list customer Customers requests

    Attributes:
        customers (MutableSequence[google.cloud.cloudcontrolspartner_v1.types.Customer]):
            List of customers
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    customers: MutableSequence["Customer"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Customer",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class CreateCustomerRequest(proto.Message):
    r"""Request to create a customer

    Attributes:
        parent (str):
            Required. Parent resource Format:
            ``organizations/{organization}/locations/{location}``
        customer (google.cloud.cloudcontrolspartner_v1.types.Customer):
            Required. The customer to create.
        customer_id (str):
            Required. The customer id to use for the
            customer, which will become the final component
            of the customer's resource name. The specified
            value must be a valid Google cloud organization
            id.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    customer: "Customer" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Customer",
    )
    customer_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GetCustomerRequest(proto.Message):
    r"""Message for getting a customer

    Attributes:
        name (str):
            Required. Format:
            ``organizations/{organization}/locations/{location}/customers/{customer}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CustomerOnboardingState(proto.Message):
    r"""Container for customer onboarding steps

    Attributes:
        onboarding_steps (MutableSequence[google.cloud.cloudcontrolspartner_v1.types.CustomerOnboardingStep]):
            List of customer onboarding steps
    """

    onboarding_steps: MutableSequence["CustomerOnboardingStep"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="CustomerOnboardingStep",
    )


class CustomerOnboardingStep(proto.Message):
    r"""Container for customer onboarding information

    Attributes:
        step (google.cloud.cloudcontrolspartner_v1.types.CustomerOnboardingStep.Step):
            The onboarding step
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The starting time of the onboarding step
        completion_time (google.protobuf.timestamp_pb2.Timestamp):
            The completion time of the onboarding step
        completion_state (google.cloud.cloudcontrolspartner_v1.types.CompletionState):
            Output only. Current state of the step
    """

    class Step(proto.Enum):
        r"""Enum for possible onboarding steps

        Values:
            STEP_UNSPECIFIED (0):
                Unspecified step
            KAJ_ENROLLMENT (1):
                KAJ Enrollment
            CUSTOMER_ENVIRONMENT (2):
                Customer Environment
        """

        STEP_UNSPECIFIED = 0
        KAJ_ENROLLMENT = 1
        CUSTOMER_ENVIRONMENT = 2

    step: Step = proto.Field(
        proto.ENUM,
        number=1,
        enum=Step,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    completion_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    completion_state: gcc_completion_state.CompletionState = proto.Field(
        proto.ENUM,
        number=4,
        enum=gcc_completion_state.CompletionState,
    )


class UpdateCustomerRequest(proto.Message):
    r"""Request to update a customer

    Attributes:
        customer (google.cloud.cloudcontrolspartner_v1.types.Customer):
            Required. The customer to update Format:
            ``organizations/{organization}/locations/{location}/customers/{customer}``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update
    """

    customer: "Customer" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Customer",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteCustomerRequest(proto.Message):
    r"""Message for deleting customer

    Attributes:
        name (str):
            Required. name of the resource to be deleted format:
            name=organizations/*/locations/*/customers/\*
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
