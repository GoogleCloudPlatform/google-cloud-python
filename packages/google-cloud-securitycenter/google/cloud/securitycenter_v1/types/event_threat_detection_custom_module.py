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

import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.securitycenter.v1",
    manifest={
        "EventThreatDetectionCustomModule",
    },
)


class EventThreatDetectionCustomModule(proto.Message):
    r"""Represents an instance of an Event Threat Detection custom
    module, including its full module name, display name, enablement
    state, and last updated time. You can create a custom module at
    the organization, folder, or project level. Custom modules that
    you create at the organization or folder level are inherited by
    child folders and projects.

    Attributes:
        name (str):
            Immutable. The resource name of the Event Threat Detection
            custom module.

            Its format is:

            - ``organizations/{organization}/eventThreatDetectionSettings/customModules/{module}``.
            - ``folders/{folder}/eventThreatDetectionSettings/customModules/{module}``.
            - ``projects/{project}/eventThreatDetectionSettings/customModules/{module}``.
        config (google.protobuf.struct_pb2.Struct):
            Config for the module. For the resident
            module, its config value is defined at this
            level. For the inherited module, its config
            value is inherited from the ancestor module.
        ancestor_module (str):
            Output only. The closest ancestor module that
            this module inherits the enablement state from.
            The format is the same as the
            EventThreatDetectionCustomModule resource name.
        enablement_state (google.cloud.securitycenter_v1.types.EventThreatDetectionCustomModule.EnablementState):
            The state of enablement for the module at the
            given level of the hierarchy.
        type_ (str):
            Type for the module. e.g. CONFIGURABLE_BAD_IP.
        display_name (str):
            The human readable name to be displayed for
            the module.
        description (str):
            The description for the module.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the module was last
            updated.
        last_editor (str):
            Output only. The editor the module was last
            updated by.
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
            INHERITED (3):
                When the enablement state is inherited.
        """

        ENABLEMENT_STATE_UNSPECIFIED = 0
        ENABLED = 1
        DISABLED = 2
        INHERITED = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    config: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Struct,
    )
    ancestor_module: str = proto.Field(
        proto.STRING,
        number=3,
    )
    enablement_state: EnablementState = proto.Field(
        proto.ENUM,
        number=4,
        enum=EnablementState,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=5,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    description: str = proto.Field(
        proto.STRING,
        number=7,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    last_editor: str = proto.Field(
        proto.STRING,
        number=9,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
