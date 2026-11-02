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
        "CloudDlpDataProfile",
        "InfoType",
        "SensitivityScore",
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
        parent_type (google.cloud.securitycenter_v1.types.CloudDlpDataProfile.ParentType):
            The resource hierarchy level at which the
            data profile was generated.
        info_types (MutableSequence[google.cloud.securitycenter_v1.types.InfoType]):
            Type of information detected by SDP.
            Info type includes name, version and sensitivity
            of the detected information type.
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
    info_types: MutableSequence["InfoType"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="InfoType",
    )


class InfoType(proto.Message):
    r"""Type of information detected by the API.

    Attributes:
        name (str):
            Name of the information type. Either a name of your choosing
            when creating a CustomInfoType, or one of the names listed
            at
            https://cloud.google.com/sensitive-data-protection/docs/infotypes-reference
            when specifying a built-in type. When sending Cloud DLP
            results to Data Catalog, infoType names should conform to
            the pattern ``[A-Za-z0-9$_-]{1,64}``.
        version (str):
            Optional version name for this InfoType.
        sensitivity_score (google.cloud.securitycenter_v1.types.SensitivityScore):
            Optional custom sensitivity for this
            InfoType. This only applies to data profiling.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    sensitivity_score: "SensitivityScore" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="SensitivityScore",
    )


class SensitivityScore(proto.Message):
    r"""Score is calculated from of all elements in the data profile.
    A higher level means the data is more sensitive.

    Attributes:
        score (google.cloud.securitycenter_v1.types.SensitivityScore.SensitivityScoreLevel):
            The sensitivity score applied to the
            resource.
    """

    class SensitivityScoreLevel(proto.Enum):
        r"""Various sensitivity score levels for resources.

        Values:
            SENSITIVITY_SCORE_LEVEL_UNSPECIFIED (0):
                Unused.
            SENSITIVITY_LOW (10):
                No sensitive information detected. The
                resource isn't publicly accessible.
            SENSITIVITY_UNKNOWN (12):
                Unable to determine sensitivity.
            SENSITIVITY_MODERATE (20):
                Medium risk. Contains personally identifiable
                information (PII), potentially sensitive data,
                or fields with free-text data that are at a
                higher risk of having intermittent sensitive
                data. Consider limiting access.
            SENSITIVITY_HIGH (30):
                High risk. Sensitive personally identifiable
                information (SPII) can be present. Exfiltration
                of data can lead to user data loss.
                Re-identification of users might be possible.
                Consider limiting usage and or removing SPII.
        """

        SENSITIVITY_SCORE_LEVEL_UNSPECIFIED = 0
        SENSITIVITY_LOW = 10
        SENSITIVITY_UNKNOWN = 12
        SENSITIVITY_MODERATE = 20
        SENSITIVITY_HIGH = 30

    score: SensitivityScoreLevel = proto.Field(
        proto.ENUM,
        number=1,
        enum=SensitivityScoreLevel,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
