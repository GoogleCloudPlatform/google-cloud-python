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

from google.ads.datamanager_v1.types import (
    user_list_license_client_account_type,
    user_list_license_metrics,
    user_list_license_pricing,
    user_list_license_status,
)

__protobuf__ = proto.module(
    package="google.ads.datamanager.v1",
    manifest={
        "UserListDirectLicense",
    },
)


class UserListDirectLicense(proto.Message):
    r"""A user list direct license.

    This feature is only available to data partners.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the user
            list direct license.
        user_list_id (int):
            Immutable. ID of the user list being
            licensed.

            This field is a member of `oneof`_ ``_user_list_id``.
        user_list_display_name (str):
            Output only. Name of the user list being
            licensed.
            This field is read-only.
        client_account_type (google.ads.datamanager_v1.types.UserListLicenseClientAccountType):
            Immutable. Account type of client customer
            which the user list is being licensed to.

            This field is a member of `oneof`_ ``_client_account_type``.
        client_account_id (int):
            Immutable. ID of client customer which the
            user list is being licensed to.

            This field is a member of `oneof`_ ``_client_account_id``.
        client_account_display_name (str):
            Output only. Name of client customer which
            the user list is being licensed to.

            This field is read-only.
        status (google.ads.datamanager_v1.types.UserListLicenseStatus):
            Optional. Status of UserListDirectLicense -
            ENABLED or DISABLED.

            This field is a member of `oneof`_ ``_status``.
        pricing (google.ads.datamanager_v1.types.UserListLicensePricing):
            Optional. UserListDirectLicense pricing.
        historical_pricings (MutableSequence[google.ads.datamanager_v1.types.UserListLicensePricing]):
            Output only. Pricing history of this user
            list license.
            This field is read-only.
        metrics (google.ads.datamanager_v1.types.UserListLicenseMetrics):
            Output only. Metrics related to this license

            This field is read-only and only populated if
            the start and end dates are set in the
            ListUserListDirectLicenses call
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    user_list_id: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )
    user_list_display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    client_account_type: user_list_license_client_account_type.UserListLicenseClientAccountType = proto.Field(
        proto.ENUM,
        number=4,
        optional=True,
        enum=user_list_license_client_account_type.UserListLicenseClientAccountType,
    )
    client_account_id: int = proto.Field(
        proto.INT64,
        number=5,
        optional=True,
    )
    client_account_display_name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    status: user_list_license_status.UserListLicenseStatus = proto.Field(
        proto.ENUM,
        number=7,
        optional=True,
        enum=user_list_license_status.UserListLicenseStatus,
    )
    pricing: user_list_license_pricing.UserListLicensePricing = proto.Field(
        proto.MESSAGE,
        number=8,
        message=user_list_license_pricing.UserListLicensePricing,
    )
    historical_pricings: MutableSequence[
        user_list_license_pricing.UserListLicensePricing
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=user_list_license_pricing.UserListLicensePricing,
    )
    metrics: user_list_license_metrics.UserListLicenseMetrics = proto.Field(
        proto.MESSAGE,
        number=10,
        message=user_list_license_metrics.UserListLicenseMetrics,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
