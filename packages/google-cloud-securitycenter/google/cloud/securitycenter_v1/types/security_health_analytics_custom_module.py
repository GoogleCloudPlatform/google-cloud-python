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

from google.cloud.securitycenter_v1.types import security_health_analytics_custom_config

__protobuf__ = proto.module(
    package="google.cloud.securitycenter.v1",
    manifest={
        "SecurityHealthAnalyticsCustomModule",
    },
)


class SecurityHealthAnalyticsCustomModule(proto.Message):
    r"""Represents an instance of a Security Health Analytics custom
    module, including its full module name, display name, enablement
    state, and last updated time. You can create a custom module at
    the organization, folder, or project level. Custom modules that
    you create at the organization or folder level are inherited by
    the child folders and projects.

    Attributes:
        name (str):
            Immutable. The resource name of the custom
            module. Its format is
            "organizations/{organization}/securityHealthAnalyticsSettings/customModules/{customModule}",
            or
            "folders/{folder}/securityHealthAnalyticsSettings/customModules/{customModule}",
            or
            "projects/{project}/securityHealthAnalyticsSettings/customModules/{customModule}"

            The id {customModule} is server-generated and is
            not user settable. It will be a numeric id
            containing 1-20 digits.
        display_name (str):
            The display name of the Security Health
            Analytics custom module. This display name
            becomes the finding category for all findings
            that are returned by this custom module. The
            display name must be between 1 and 128
            characters, start with a lowercase letter, and
            contain alphanumeric characters or underscores
            only.
        enablement_state (google.cloud.securitycenter_v1.types.SecurityHealthAnalyticsCustomModule.EnablementState):
            The enablement state of the custom module.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the custom
            module was last updated.
        last_editor (str):
            Output only. The editor that last updated the
            custom module.
        ancestor_module (str):
            Output only. If empty, indicates that the custom module was
            created in the organization, folder, or project in which you
            are viewing the custom module. Otherwise,
            ``ancestor_module`` specifies the organization or folder
            from which the custom module is inherited.
        custom_config (google.cloud.securitycenter_v1.types.CustomConfig):
            The user specified custom configuration for
            the module.
    """

    class EnablementState(proto.Enum):
        r"""Possible enablement states of a custom module.

        Values:
            ENABLEMENT_STATE_UNSPECIFIED (0):
                Unspecified enablement state.
            ENABLED (1):
                The module is enabled at the given CRM
                resource.
            DISABLED (2):
                The module is disabled at the given CRM
                resource.
            INHERITED (3):
                State is inherited from an ancestor module.
                The module will either be effectively ENABLED or
                DISABLED based on its closest non-inherited
                ancestor module in the CRM hierarchy.
        """

        ENABLEMENT_STATE_UNSPECIFIED = 0
        ENABLED = 1
        DISABLED = 2
        INHERITED = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    enablement_state: EnablementState = proto.Field(
        proto.ENUM,
        number=4,
        enum=EnablementState,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    last_editor: str = proto.Field(
        proto.STRING,
        number=6,
    )
    ancestor_module: str = proto.Field(
        proto.STRING,
        number=7,
    )
    custom_config: security_health_analytics_custom_config.CustomConfig = proto.Field(
        proto.MESSAGE,
        number=8,
        message=security_health_analytics_custom_config.CustomConfig,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
