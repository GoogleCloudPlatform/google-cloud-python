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

from google.cloud.discoveryengine_v1beta.types import (
    license_config as gcd_license_config,
)

__protobuf__ = proto.module(
    package="google.cloud.discoveryengine.v1beta",
    manifest={
        "CreateLicenseConfigRequest",
        "UpdateLicenseConfigRequest",
        "GetLicenseConfigRequest",
        "ListLicenseConfigsRequest",
        "ListLicenseConfigsResponse",
        "DistributeLicenseConfigRequest",
        "DistributeLicenseConfigResponse",
        "RetractLicenseConfigRequest",
        "RetractLicenseConfigResponse",
    },
)


class CreateLicenseConfigRequest(proto.Message):
    r"""Request message for
    [LicenseConfigService.CreateLicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfigService.CreateLicenseConfig]
    method.

    Attributes:
        parent (str):
            Required. The parent resource name, such as
            ``projects/{project}/locations/{location}``.
        license_config (google.cloud.discoveryengine_v1beta.types.LicenseConfig):
            Required. The
            [LicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfig]
            to create.
        license_config_id (str):
            Optional. The ID to use for the
            [LicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfig],
            which will become the final component of the
            [LicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfig]'s
            resource name. We are using the tier (product edition) name
            as the license config id such as ``search`` or
            ``search_and_assistant``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    license_config: gcd_license_config.LicenseConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcd_license_config.LicenseConfig,
    )
    license_config_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateLicenseConfigRequest(proto.Message):
    r"""Request message for
    [LicenseConfigService.UpdateLicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfigService.UpdateLicenseConfig]
    method.

    Attributes:
        license_config (google.cloud.discoveryengine_v1beta.types.LicenseConfig):
            Required. The
            [LicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfig]
            to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Indicates which fields in the provided
            [LicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfig]
            to update.

            If an unsupported or unknown field is provided, an
            INVALID_ARGUMENT error is returned.
    """

    license_config: gcd_license_config.LicenseConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcd_license_config.LicenseConfig,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetLicenseConfigRequest(proto.Message):
    r"""Request message for
    [LicenseConfigService.GetLicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfigService.GetLicenseConfig]
    method.

    Attributes:
        name (str):
            Required. Full resource name of
            [LicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfig],
            such as
            ``projects/{project}/locations/{location}/licenseConfigs/*``.

            If the caller does not have permission to access the
            [LicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfig],
            regardless of whether or not it exists, a PERMISSION_DENIED
            error is returned.

            If the requested
            [LicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfig]
            does not exist, a NOT_FOUND error is returned.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListLicenseConfigsRequest(proto.Message):
    r"""Request message for
    [LicenseConfigService.ListLicenseConfigs][google.cloud.discoveryengine.v1beta.LicenseConfigService.ListLicenseConfigs]
    method.

    Attributes:
        parent (str):
            Required. The parent branch resource name, such as
            ``projects/{project}/locations/{location}``.
        page_size (int):
            Optional. Not supported.
        page_token (str):
            Optional. Not supported.
        filter (str):
            Optional. The filter to apply to the list results.

            The supported fields are:

            - ``subscription_tier``
            - ``state``

            Examples:

            - ``subscription_tier=SUBSCRIPTION_TIER_SEARCH,state=ACTIVE``
              - Lists all active search license configs.
            - ``state=ACTIVE`` - Lists all active license configs.

            The filter string should be a comma-separated list of
            field=value pairs.
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


class ListLicenseConfigsResponse(proto.Message):
    r"""Response message for
    [LicenseConfigService.ListLicenseConfigs][google.cloud.discoveryengine.v1beta.LicenseConfigService.ListLicenseConfigs]
    method.

    Attributes:
        license_configs (MutableSequence[google.cloud.discoveryengine_v1beta.types.LicenseConfig]):
            All the customer's
            [LicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfig]s.
        next_page_token (str):
            Not supported.
    """

    @property
    def raw_page(self):
        return self

    license_configs: MutableSequence[gcd_license_config.LicenseConfig] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=gcd_license_config.LicenseConfig,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DistributeLicenseConfigRequest(proto.Message):
    r"""Request message for
    [LicenseConfigService.DistributeLicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfigService.DistributeLicenseConfig]
    method.

    Attributes:
        billing_account_license_config (str):
            Required. Full resource name of
            [BillingAccountLicenseConfig][].

            Format:
            ``billingAccounts/{billing_account}/billingAccountLicenseConfigs/{billing_account_license_config_id}``.
        project_number (int):
            Required. The target GCP project number to
            distribute the license config to.
        location (str):
            Required. The target GCP project region to
            distribute the license config to.
        license_count (int):
            Required. The number of licenses to
            distribute.
        license_config_id (str):
            Optional. Distribute seats to this license
            config instead of creating a new one. If not
            specified, a new license config will be created
            from the billing account license config.
    """

    billing_account_license_config: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project_number: int = proto.Field(
        proto.INT64,
        number=2,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )
    license_count: int = proto.Field(
        proto.INT64,
        number=4,
    )
    license_config_id: str = proto.Field(
        proto.STRING,
        number=5,
    )


class DistributeLicenseConfigResponse(proto.Message):
    r"""Response message for
    [LicenseConfigService.DistributeLicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfigService.DistributeLicenseConfig]
    method.

    Attributes:
        license_config (google.cloud.discoveryengine_v1beta.types.LicenseConfig):
            The updated or created LicenseConfig.
    """

    license_config: gcd_license_config.LicenseConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcd_license_config.LicenseConfig,
    )


class RetractLicenseConfigRequest(proto.Message):
    r"""Request message for
    [LicenseConfigService.RetractLicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfigService.RetractLicenseConfig]
    method.

    Attributes:
        billing_account_license_config (str):
            Required. Full resource name of
            [BillingAccountLicenseConfig][].

            Format:
            ``billingAccounts/{billing_account}/billingAccountLicenseConfigs/{billing_account_license_config_id}``.
        license_config (str):
            Required. Full resource name of
            [LicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfig].

            Format:
            ``projects/{project}/locations/{location}/licenseConfigs/{license_config_id}``.
        full_retract (bool):
            Optional. If set to true, retract the entire
            license config. Otherwise, retract the specified
            license count.
        license_count (int):
            Optional. The number of licenses to retract. Only used when
            full_retract is false.
    """

    billing_account_license_config: str = proto.Field(
        proto.STRING,
        number=1,
    )
    license_config: str = proto.Field(
        proto.STRING,
        number=2,
    )
    full_retract: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    license_count: int = proto.Field(
        proto.INT64,
        number=4,
    )


class RetractLicenseConfigResponse(proto.Message):
    r"""Response message for
    [LicenseConfigService.RetractLicenseConfig][google.cloud.discoveryengine.v1beta.LicenseConfigService.RetractLicenseConfig]
    method.

    Attributes:
        license_config (google.cloud.discoveryengine_v1beta.types.LicenseConfig):
            The updated LicenseConfig.
    """

    license_config: gcd_license_config.LicenseConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcd_license_config.LicenseConfig,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
