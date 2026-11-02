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

from google.cloud.errorreporting_v1beta1.types import common

__protobuf__ = proto.module(
    package="google.devtools.clouderrorreporting.v1beta1",
    manifest={
        "GetGroupRequest",
        "UpdateGroupRequest",
    },
)


class GetGroupRequest(proto.Message):
    r"""A request to return an individual group.

    Attributes:
        group_name (str):
            Required. The group resource name. Written as either
            ``projects/{projectID}/groups/{group_id}`` or
            ``projects/{projectID}/locations/{location}/groups/{group_id}``.
            Call [groupStats.list]
            [google.devtools.clouderrorreporting.v1beta1.ErrorStatsService.ListGroupStats]
            to return a list of groups belonging to this project.

            Examples: ``projects/my-project-123/groups/my-group``,
            ``projects/my-project-123/locations/global/groups/my-group``

            In the group resource name, the ``group_id`` is a unique
            identifier for a particular error group. The identifier is
            derived from key parts of the error-log content and is
            treated as Service Data. For information about how Service
            Data is handled, see `Google Cloud Privacy
            Notice <https://cloud.google.com/terms/cloud-privacy-notice>`__.

            For a list of supported locations, see `Supported
            Regions <https://cloud.google.com/logging/docs/region-support>`__.
            ``global`` is the default when unspecified.
    """

    group_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateGroupRequest(proto.Message):
    r"""A request to replace the existing data for the given group.

    Attributes:
        group (google.cloud.errorreporting_v1beta1.types.ErrorGroup):
            Required. The group which replaces the
            resource on the server.
    """

    group: common.ErrorGroup = proto.Field(
        proto.MESSAGE,
        number=1,
        message=common.ErrorGroup,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
