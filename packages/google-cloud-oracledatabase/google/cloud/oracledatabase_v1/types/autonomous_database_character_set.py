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
    package="google.cloud.oracledatabase.v1",
    manifest={
        "AutonomousDatabaseCharacterSet",
    },
)


class AutonomousDatabaseCharacterSet(proto.Message):
    r"""Details of the Autonomous Database character set resource.
    https://docs.oracle.com/en-us/iaas/api/#/en/database/20160918/AutonomousDatabaseCharacterSets/

    Attributes:
        name (str):
            Identifier. The name of the Autonomous Database Character
            Set resource in the following format:
            projects/{project}/locations/{region}/autonomousDatabaseCharacterSets/{autonomous_database_character_set}
        character_set_type (google.cloud.oracledatabase_v1.types.AutonomousDatabaseCharacterSet.CharacterSetType):
            Output only. The character set type for the
            Autonomous Database.
        character_set (str):
            Output only. The character set name for the
            Autonomous Database which is the ID in the
            resource name.
    """

    class CharacterSetType(proto.Enum):
        r"""The type of character set an Autonomous Database can have.

        Values:
            CHARACTER_SET_TYPE_UNSPECIFIED (0):
                Character set type is not specified.
            DATABASE (1):
                Character set type is set to database.
            NATIONAL (2):
                Character set type is set to national.
        """

        CHARACTER_SET_TYPE_UNSPECIFIED = 0
        DATABASE = 1
        NATIONAL = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    character_set_type: CharacterSetType = proto.Field(
        proto.ENUM,
        number=2,
        enum=CharacterSetType,
    )
    character_set: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
