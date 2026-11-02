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
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.securitycenter.v1",
    manifest={
        "EffectiveEventThreatDetectionCustomModule",
    },
)


class EffectiveEventThreatDetectionCustomModule(proto.Message):
    r"""An EffectiveEventThreatDetectionCustomModule is the representation
    of an Event Threat Detection custom module at a specified level of
    the resource hierarchy: organization, folder, or project. If a
    custom module is inherited from a parent organization or folder, the
    value of the ``enablement_state`` property in
    EffectiveEventThreatDetectionCustomModule is set to the value that
    is effective in the parent, instead of ``INHERITED``. For example,
    if the module is enabled in a parent organization or folder, the
    effective ``enablement_state`` for the module in all child folders
    or projects is also ``enabled``.
    EffectiveEventThreatDetectionCustomModule is read-only.

    Attributes:
        name (str):
            Output only. The resource name of the effective ETD custom
            module.

            Its format is:

            - ``organizations/{organization}/eventThreatDetectionSettings/effectiveCustomModules/{module}``.
            - ``folders/{folder}/eventThreatDetectionSettings/effectiveCustomModules/{module}``.
            - ``projects/{project}/eventThreatDetectionSettings/effectiveCustomModules/{module}``.
        config (google.protobuf.struct_pb2.Struct):
            Output only. Config for the effective module.
        enablement_state (google.cloud.securitycenter_v1.types.EffectiveEventThreatDetectionCustomModule.EnablementState):
            Output only. The effective state of
            enablement for the module at the given level of
            the hierarchy.
        type_ (str):
            Output only. Type for the module. e.g. CONFIGURABLE_BAD_IP.
        display_name (str):
            Output only. The human readable name to be
            displayed for the module.
        description (str):
            Output only. The description for the module.
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
    config: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Struct,
    )
    enablement_state: EnablementState = proto.Field(
        proto.ENUM,
        number=3,
        enum=EnablementState,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=4,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    description: str = proto.Field(
        proto.STRING,
        number=6,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
