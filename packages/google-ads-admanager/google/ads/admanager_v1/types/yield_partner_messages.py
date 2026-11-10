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

from google.ads.admanager_v1.types import (
    yield_enums,
    yield_environment_type_enum,
    yield_format_enum,
)

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "YieldPartner",
        "YieldPartnerSettings",
    },
)


class YieldPartner(proto.Message):
    r"""Represents a third-party ad network or exchange, configured
    within the context of a Company, that publishers partner with to
    monetize their ad inventory.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the ``YieldPartner``.
            Format:
            ``networks/{network_code}/yieldPartners/{yieldPartnerId}``
        display_name (str):
            Optional. The name of the yield partner. This
            refers to the name of the company associated
            with the partner, if there is one.

            This field is a member of `oneof`_ ``_display_name``.
        company (str):
            Output only. The company associated with this
            yield partner.

            This field is a member of `oneof`_ ``_company``.
        settings (MutableSequence[google.ads.admanager_v1.types.YieldPartnerSettings]):
            Optional. The settings of the partner,
            representing its capabilities.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    company: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    settings: MutableSequence["YieldPartnerSettings"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="YieldPartnerSettings",
    )


class YieldPartnerSettings(proto.Message):
    r"""Settings for a yield partner.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        status (google.ads.admanager_v1.types.YieldPartnerSettingStatusEnum.YieldPartnerSettingStatus):
            Output only. The status of this yield partner
            setting.

            This field is a member of `oneof`_ ``_status``.
        environment (google.ads.admanager_v1.types.YieldEnvironmentTypeEnum.YieldEnvironmentType):
            Output only. The environment of this yield
            partner setting.

            This field is a member of `oneof`_ ``_environment``.
        format_ (google.ads.admanager_v1.types.YieldFormatEnum.YieldFormat):
            Output only. The format of this yield partner
            setting.

            This field is a member of `oneof`_ ``_format``.
        integration_type (google.ads.admanager_v1.types.YieldIntegrationTypeEnum.YieldIntegrationType):
            Output only. The integration type of this
            yield partner setting.

            This field is a member of `oneof`_ ``_integration_type``.
        parameters (MutableSequence[google.ads.admanager_v1.types.YieldPartnerSettings.YieldParameter]):
            Output only. The parameters of this yield
            partner setting.
        platform (google.ads.admanager_v1.types.YieldPlatformEnum.YieldPlatform):
            Output only. The platform of this yield
            partner setting.

            This field is a member of `oneof`_ ``_platform``.
    """

    class YieldParameter(proto.Message):
        r"""Describes a field used by a mobile adapter to call an ad network.
        For example, ``pubid``.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            key (str):
                Output only. Identifier of the parameter.

                This field is a member of `oneof`_ ``_key``.
            optional (bool):
                Output only. Whether or not this parameter is
                optional.

                This field is a member of `oneof`_ ``_optional``.
        """

        key: str = proto.Field(
            proto.STRING,
            number=1,
            optional=True,
        )
        optional: bool = proto.Field(
            proto.BOOL,
            number=2,
            optional=True,
        )

    status: yield_enums.YieldPartnerSettingStatusEnum.YieldPartnerSettingStatus = (
        proto.Field(
            proto.ENUM,
            number=1,
            optional=True,
            enum=yield_enums.YieldPartnerSettingStatusEnum.YieldPartnerSettingStatus,
        )
    )
    environment: yield_environment_type_enum.YieldEnvironmentTypeEnum.YieldEnvironmentType = proto.Field(
        proto.ENUM,
        number=2,
        optional=True,
        enum=yield_environment_type_enum.YieldEnvironmentTypeEnum.YieldEnvironmentType,
    )
    format_: yield_format_enum.YieldFormatEnum.YieldFormat = proto.Field(
        proto.ENUM,
        number=3,
        optional=True,
        enum=yield_format_enum.YieldFormatEnum.YieldFormat,
    )
    integration_type: yield_enums.YieldIntegrationTypeEnum.YieldIntegrationType = (
        proto.Field(
            proto.ENUM,
            number=4,
            optional=True,
            enum=yield_enums.YieldIntegrationTypeEnum.YieldIntegrationType,
        )
    )
    parameters: MutableSequence[YieldParameter] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=YieldParameter,
    )
    platform: yield_enums.YieldPlatformEnum.YieldPlatform = proto.Field(
        proto.ENUM,
        number=6,
        optional=True,
        enum=yield_enums.YieldPlatformEnum.YieldPlatform,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
