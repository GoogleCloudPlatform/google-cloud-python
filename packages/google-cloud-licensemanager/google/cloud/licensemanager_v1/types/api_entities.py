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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.licensemanager.v1",
    manifest={
        "LicenseType",
        "ActivationState",
        "Configuration",
        "BillingInfo",
        "UserCountBillingInfo",
        "UserCountUsage",
        "Product",
        "Instance",
        "Usage",
    },
)


class LicenseType(proto.Enum):
    r"""Different types of licenses that are supported.

    Values:
        LICENSE_TYPE_UNSPECIFIED (0):
            unspecified.
        LICENSE_TYPE_PER_MONTH_PER_USER (1):
            Billing will be based on number of users
            listed per month.
        LICENSE_TYPE_BRING_YOUR_OWN_LICENSE (2):
            Bring your own license.
    """

    LICENSE_TYPE_UNSPECIFIED = 0
    LICENSE_TYPE_PER_MONTH_PER_USER = 1
    LICENSE_TYPE_BRING_YOUR_OWN_LICENSE = 2


class ActivationState(proto.Enum):
    r"""State of the License Key activation on the instance.

    Values:
        ACTIVATION_STATE_UNSPECIFIED (0):
            The Status of the activation is unspecified
        ACTIVATION_STATE_KEY_REQUESTED (1):
            Activation key (MAK) requested for the
            instance.
        ACTIVATION_STATE_ACTIVATING (2):
            License activation process is running on the
            instance.
        ACTIVATION_STATE_ACTIVATED (3):
            License activation is complete on the
            instance.
        ACTIVATION_STATE_DEACTIVATING (4):
            License Key is deactivating on the instance.
        ACTIVATION_STATE_DEACTIVATED (5):
            License Key is deactivated on the instance.
        ACTIVATION_STATE_TERMINATED (6):
            License Key activation failed on the
            instance.
    """

    ACTIVATION_STATE_UNSPECIFIED = 0
    ACTIVATION_STATE_KEY_REQUESTED = 1
    ACTIVATION_STATE_ACTIVATING = 2
    ACTIVATION_STATE_ACTIVATED = 3
    ACTIVATION_STATE_DEACTIVATING = 4
    ACTIVATION_STATE_DEACTIVATED = 5
    ACTIVATION_STATE_TERMINATED = 6


class Configuration(proto.Message):
    r"""Configuration for a Google SPLA product

    Attributes:
        name (str):
            Identifier. name of resource
        display_name (str):
            Required. User given name.
        product (str):
            Required. Name field (with URL) of the
            Product offered for SPLA.
        license_type (google.cloud.licensemanager_v1.types.LicenseType):
            Required. LicenseType to be applied for
            billing
        current_billing_info (google.cloud.licensemanager_v1.types.BillingInfo):
            Required. Billing information applicable till
            end of the current month.
        next_billing_info (google.cloud.licensemanager_v1.types.BillingInfo):
            Required. Billing information applicable for
            next month.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Create time stamp
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Update time stamp
        labels (MutableMapping[str, str]):
            Optional. Labels as key value pairs
        state (google.cloud.licensemanager_v1.types.Configuration.State):
            Output only. State of the configuration.
    """

    class State(proto.Enum):
        r"""State of the configuration.

        Values:
            STATE_UNSPECIFIED (0):
                The Status of the configuration is
                unspecified
            STATE_ACTIVE (1):
                Configuration is in active state.
            STATE_SUSPENDED (2):
                Configuration is in deactivated state.
            STATE_DELETED (3):
                Configuration is in deleted state.
        """

        STATE_UNSPECIFIED = 0
        STATE_ACTIVE = 1
        STATE_SUSPENDED = 2
        STATE_DELETED = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    product: str = proto.Field(
        proto.STRING,
        number=6,
    )
    license_type: "LicenseType" = proto.Field(
        proto.ENUM,
        number=7,
        enum="LicenseType",
    )
    current_billing_info: "BillingInfo" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="BillingInfo",
    )
    next_billing_info: "BillingInfo" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="BillingInfo",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=10,
        enum=State,
    )


class BillingInfo(proto.Message):
    r"""Billing Information.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        user_count_billing (google.cloud.licensemanager_v1.types.UserCountBillingInfo):
            Required. This type of billing uses user
            count for computing total charge.

            This field is a member of `oneof`_ ``current_billing_info``.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the billing starts.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the billing ends.
    """

    user_count_billing: "UserCountBillingInfo" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="current_billing_info",
        message="UserCountBillingInfo",
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class UserCountBillingInfo(proto.Message):
    r"""This approach uses total unique user count for billing.

    Attributes:
        user_count (int):
            Required. Number of users to bill for.
    """

    user_count: int = proto.Field(
        proto.INT32,
        number=1,
    )


class UserCountUsage(proto.Message):
    r"""Message representing usage for license configurations which
    use user-count billing.

    Attributes:
        unique_user_count (int):
            Required. Unique number of licensed users.
    """

    unique_user_count: int = proto.Field(
        proto.INT32,
        number=1,
    )


class Product(proto.Message):
    r"""Products for Google SPLA.

    Attributes:
        name (str):
            Identifier. Full name of the product
            resource. ex
            "projects/1/locations/us-central1/products/office-2021".
        version (str):
            Required. Version of the product.
        product_company (str):
            Required. Company that released the product.
        state (google.cloud.licensemanager_v1.types.Product.State):
            Output only. State of the product.
        sku (str):
            Required. SKU for mapping to the
            Billing/Subscription resource.
        description (str):
            Required. Human-readable, detailed
            description of the Product
        display_name (str):
            Required. Human-readable name of the Product
    """

    class State(proto.Enum):
        r"""State of the product.

        Values:
            STATE_UNSPECIFIED (0):
                The Status of the product is unknown.
            STATE_PROVISIONING (1):
                Product is under provisioning stage.
            STATE_RUNNING (2):
                Product is ok to run on instances.
            STATE_TERMINATING (3):
                The product is about to terminate or has been
                announced for termination.
            STATE_TERMINATED (4):
                The product has been terminated.
        """

        STATE_UNSPECIFIED = 0
        STATE_PROVISIONING = 1
        STATE_RUNNING = 2
        STATE_TERMINATING = 3
        STATE_TERMINATED = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    product_company: str = proto.Field(
        proto.STRING,
        number=3,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    sku: str = proto.Field(
        proto.STRING,
        number=5,
    )
    description: str = proto.Field(
        proto.STRING,
        number=6,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=7,
    )


class Instance(proto.Message):
    r"""Message describing Instance object

    Attributes:
        name (str):
            Identifier. name of resource
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Create time stamp
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Update time stamp
        labels (MutableMapping[str, str]):
            Optional. Labels as key value pairs
        state (google.cloud.licensemanager_v1.types.Instance.State):
            Output only. The state of the VM.
        region (str):
            Output only. The location of the VM.
        product_activation (MutableMapping[str, google.cloud.licensemanager_v1.types.ActivationState]):
            Output only. Map with Product_Name and Activation State of
            the VM.
        license_version_id (str):
            Output only. license version id.
        compute_instance (str):
            Required. Compute Instance resource name,
            i.e.
            projects/{project}/zones/{zone}/instances/{instance}
    """

    class State(proto.Enum):
        r"""VM status enum.

        Values:
            STATE_UNSPECIFIED (0):
                The Status of the VM is unspecified.
            PROVISIONING (1):
                Resources are being allocated for the
                instance.
            STAGING (2):
                All required resources have been allocated
                and the instance is being started.
            RUNNING (3):
                The instance is running.
            STOPPING (4):
                The instance is currently stopping (either
                being deleted or terminated).
            STOPPED (5):
                The instance has stopped due to various
                reasons (user request, VM preemption, project
                freezing, etc.).
            TERMINATED (6):
                The instance has failed in some way.
            REPAIRING (7):
                The instance is in repair.
        """

        STATE_UNSPECIFIED = 0
        PROVISIONING = 1
        STAGING = 2
        RUNNING = 3
        STOPPING = 4
        STOPPED = 5
        TERMINATED = 6
        REPAIRING = 7

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    region: str = proto.Field(
        proto.STRING,
        number=6,
    )
    product_activation: MutableMapping[str, "ActivationState"] = proto.MapField(
        proto.STRING,
        proto.ENUM,
        number=7,
        enum="ActivationState",
    )
    license_version_id: str = proto.Field(
        proto.STRING,
        number=8,
    )
    compute_instance: str = proto.Field(
        proto.STRING,
        number=9,
    )


class Usage(proto.Message):
    r"""Message describing total counts of users who accessed a VM.

    Attributes:
        lima_instance (str):
            LiMa Instance resource name, i.e.
            projects/{project}/locations/{location}/instances/{instance}
        users (int):
            Number of unique users accessing the VM.
    """

    lima_instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    users: int = proto.Field(
        proto.INT32,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
