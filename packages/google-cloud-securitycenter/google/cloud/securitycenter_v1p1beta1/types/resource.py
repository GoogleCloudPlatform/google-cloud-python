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

from google.cloud.securitycenter_v1p1beta1.types import folder

__protobuf__ = proto.module(
    package="google.cloud.securitycenter.v1p1beta1",
    manifest={
        "Resource",
    },
)


class Resource(proto.Message):
    r"""Information related to the Google Cloud resource.

    Attributes:
        name (str):
            The full resource name of the resource. See:
            https://cloud.google.com/apis/design/resource_names#full_resource_name
        project (str):
            The full resource name of project that the
            resource belongs to.
        project_display_name (str):
            The human readable name of project that the
            resource belongs to.
        parent (str):
            The full resource name of resource's parent.
        parent_display_name (str):
            The human readable name of resource's parent.
        folders (MutableSequence[google.cloud.securitycenter_v1p1beta1.types.Folder]):
            Output only. Contains a Folder message for
            each folder in the assets ancestry. The first
            folder is the deepest nested folder, and the
            last folder is the folder directly under the
            Organization.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    project_display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=4,
    )
    parent_display_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    folders: MutableSequence[folder.Folder] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=folder.Folder,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
