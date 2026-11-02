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

__protobuf__ = proto.module(
    package="google.cloud.securitycenter.v1",
    manifest={
        "OrganizationSettings",
    },
)


class OrganizationSettings(proto.Message):
    r"""User specified settings that are attached to the Security
    Command Center organization.

    Attributes:
        name (str):
            The relative resource name of the settings. See:
            https://cloud.google.com/apis/design/resource_names#relative_resource_name
            Example:
            "organizations/{organization_id}/organizationSettings".
        enable_asset_discovery (bool):
            A flag that indicates if Asset Discovery should be enabled.
            If the flag is set to ``true``, then discovery of assets
            will occur. If it is set to ``false``, all historical assets
            will remain, but discovery of future assets will not occur.
        asset_discovery_config (google.cloud.securitycenter_v1.types.OrganizationSettings.AssetDiscoveryConfig):
            The configuration used for Asset Discovery
            runs.
    """

    class AssetDiscoveryConfig(proto.Message):
        r"""The configuration used for Asset Discovery runs.

        Attributes:
            project_ids (MutableSequence[str]):
                The project ids to use for filtering asset
                discovery.
            inclusion_mode (google.cloud.securitycenter_v1.types.OrganizationSettings.AssetDiscoveryConfig.InclusionMode):
                The mode to use for filtering asset
                discovery.
            folder_ids (MutableSequence[str]):
                The folder ids to use for filtering asset
                discovery. It consists of only digits, e.g.,
                756619654966.
        """

        class InclusionMode(proto.Enum):
            r"""The mode of inclusion when running Asset Discovery. Asset discovery
            can be limited by explicitly identifying projects to be included or
            excluded. If INCLUDE_ONLY is set, then only those projects within
            the organization and their children are discovered during asset
            discovery. If EXCLUDE is set, then projects that don't match those
            projects are discovered during asset discovery. If neither are set,
            then all projects within the organization are discovered during
            asset discovery.

            Values:
                INCLUSION_MODE_UNSPECIFIED (0):
                    Unspecified. Setting the mode with this value
                    will disable inclusion/exclusion filtering for
                    Asset Discovery.
                INCLUDE_ONLY (1):
                    Asset Discovery will capture only the
                    resources within the projects specified. All
                    other resources will be ignored.
                EXCLUDE (2):
                    Asset Discovery will ignore all resources
                    under the projects specified. All other
                    resources will be retrieved.
            """

            INCLUSION_MODE_UNSPECIFIED = 0
            INCLUDE_ONLY = 1
            EXCLUDE = 2

        project_ids: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        inclusion_mode: "OrganizationSettings.AssetDiscoveryConfig.InclusionMode" = (
            proto.Field(
                proto.ENUM,
                number=2,
                enum="OrganizationSettings.AssetDiscoveryConfig.InclusionMode",
            )
        )
        folder_ids: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    enable_asset_discovery: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    asset_discovery_config: AssetDiscoveryConfig = proto.Field(
        proto.MESSAGE,
        number=3,
        message=AssetDiscoveryConfig,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
