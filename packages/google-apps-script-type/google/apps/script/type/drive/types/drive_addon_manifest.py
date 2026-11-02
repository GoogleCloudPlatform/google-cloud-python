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

from google.apps.script.type.types import extension_point

__protobuf__ = proto.module(
    package="google.apps.script.type.drive",
    manifest={
        "DriveAddOnManifest",
        "DriveExtensionPoint",
    },
)


class DriveAddOnManifest(proto.Message):
    r"""Drive add-on manifest.

    Attributes:
        homepage_trigger (google.apps.script.type.types.HomepageExtensionPoint):
            If present, this overrides the configuration from
            ``addOns.common.homepageTrigger``.
        on_items_selected_trigger (google.apps.script.type.drive.types.DriveExtensionPoint):
            Corresponds to behvior that should execute
            when items are selected in relevant Drive view
            (e.g. the My Drive Doclist).
    """

    homepage_trigger: extension_point.HomepageExtensionPoint = proto.Field(
        proto.MESSAGE,
        number=1,
        message=extension_point.HomepageExtensionPoint,
    )
    on_items_selected_trigger: "DriveExtensionPoint" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DriveExtensionPoint",
    )


class DriveExtensionPoint(proto.Message):
    r"""A generic extension point with common features, e.g.
    something that simply needs a corresponding run function to
    work.

    Attributes:
        run_function (str):
            Required. The endpoint to execute when this
            extension point is activated.
    """

    run_function: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
