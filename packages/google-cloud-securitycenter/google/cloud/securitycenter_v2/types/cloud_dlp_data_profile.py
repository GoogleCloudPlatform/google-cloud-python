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
    package="google.cloud.securitycenter.v2",
    manifest={
        "CloudDlpDataProfile",
    },
)


class CloudDlpDataProfile(proto.Message):
    r"""The `data
    profile <https://cloud.google.com/dlp/docs/data-profiles>`__
    associated with the finding.

    Attributes:
        data_profile (str):
            Name of the data profile, for example,
            ``projects/123/locations/europe/tableProfiles/8383929``.
        parent_type (google.cloud.securitycenter_v2.types.CloudDlpDataProfile.ParentType):
            The resource hierarchy level at which the
            data profile was generated.
    """

    class ParentType(proto.Enum):
        r"""Parents for configurations that produce data profile
        findings.

        Values:
            PARENT_TYPE_UNSPECIFIED (0):
                Unspecified parent type.
            ORGANIZATION (1):
                Organization-level configurations.
            PROJECT (2):
                Project-level configurations.
        """

        PARENT_TYPE_UNSPECIFIED = 0
        ORGANIZATION = 1
        PROJECT = 2

    data_profile: str = proto.Field(
        proto.STRING,
        number=1,
    )
    parent_type: ParentType = proto.Field(
        proto.ENUM,
        number=2,
        enum=ParentType,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
