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

from google.cloud.securitycenter_v1.types import security_health_analytics_custom_config

__protobuf__ = proto.module(
    package="google.cloud.securitycenter.v1",
    manifest={
        "EffectiveSecurityHealthAnalyticsCustomModule",
    },
)


class EffectiveSecurityHealthAnalyticsCustomModule(proto.Message):
    r"""An EffectiveSecurityHealthAnalyticsCustomModule is the
    representation of a Security Health Analytics custom module at a
    specified level of the resource hierarchy: organization, folder, or
    project. If a custom module is inherited from a parent organization
    or folder, the value of the ``enablementState`` property in
    EffectiveSecurityHealthAnalyticsCustomModule is set to the value
    that is effective in the parent, instead of ``INHERITED``. For
    example, if the module is enabled in a parent organization or
    folder, the effective enablement_state for the module in all child
    folders or projects is also ``enabled``.
    EffectiveSecurityHealthAnalyticsCustomModule is read-only.

    Attributes:
        name (str):
            Output only. The resource name of the custom
            module. Its format is
            "organizations/{organization}/securityHealthAnalyticsSettings/effectiveCustomModules/{customModule}",
            or
            "folders/{folder}/securityHealthAnalyticsSettings/effectiveCustomModules/{customModule}",
            or
            "projects/{project}/securityHealthAnalyticsSettings/effectiveCustomModules/{customModule}".
        custom_config (google.cloud.securitycenter_v1.types.CustomConfig):
            Output only. The user-specified configuration
            for the module.
        enablement_state (google.cloud.securitycenter_v1.types.EffectiveSecurityHealthAnalyticsCustomModule.EnablementState):
            Output only. The effective state of
            enablement for the module at the given level of
            the hierarchy.
        display_name (str):
            Output only. The display name for the custom
            module. The name must be between 1 and 128
            characters, start with a lowercase letter, and
            contain alphanumeric characters or underscores
            only.
    """

    class EnablementState(proto.Enum):
        r"""The enablement state of the module.

        Values:
            ENABLEMENT_STATE_UNSPECIFIED (0):
                Unspecified enablement state.
            ENABLED (1):
                The module is enabled at the given level.
            DISABLED (2):
                The module is disabled at the given level.
        """

        ENABLEMENT_STATE_UNSPECIFIED = 0
        ENABLED = 1
        DISABLED = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    custom_config: security_health_analytics_custom_config.CustomConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=security_health_analytics_custom_config.CustomConfig,
    )
    enablement_state: EnablementState = proto.Field(
        proto.ENUM,
        number=3,
        enum=EnablementState,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
