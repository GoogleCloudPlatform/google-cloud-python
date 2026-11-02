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
        "DatabaseCharacterSet",
        "ListDatabaseCharacterSetsRequest",
        "ListDatabaseCharacterSetsResponse",
    },
)


class DatabaseCharacterSet(proto.Message):
    r"""Details of the Database character set resource.

    Attributes:
        name (str):
            Identifier. The name of the Database Character Set resource
            in the following format:
            projects/{project}/locations/{region}/databaseCharacterSets/{database_character_set}
        character_set_type (google.cloud.oracledatabase_v1.types.DatabaseCharacterSet.CharacterSetType):
            Output only. The character set type for the
            Database.
        character_set (str):
            Output only. The character set name for the
            Database which is the ID in the resource name.
    """

    class CharacterSetType(proto.Enum):
        r"""The type of character set a Database can have.

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


class ListDatabaseCharacterSetsRequest(proto.Message):
    r"""The request for ``DatabaseCharacterSet.List``.

    Attributes:
        parent (str):
            Required. The parent value for
            DatabaseCharacterSets in the following format:
            projects/{project}/locations/{location}.
        page_size (int):
            Optional. The maximum number of
            DatabaseCharacterSets to return. The service may
            return fewer than this value. If unspecified, at
            most 50 DatabaseCharacterSets will be returned.
            The maximum value is 1000; values above 1000
            will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListDatabaseCharacterSets`` call. Provide this to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``ListDatabaseCharacterSets`` must match the call that
            provided the page token.
        filter (str):
            Optional. An expression for filtering the results of the
            request. Only the **character_set_type** field is supported
            in the following format:
            ``character_set_type="{characterSetType}"``. Accepted values
            include ``DATABASE`` and ``NATIONAL``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListDatabaseCharacterSetsResponse(proto.Message):
    r"""The response for ``DatabaseCharacterSet.List``.

    Attributes:
        database_character_sets (MutableSequence[google.cloud.oracledatabase_v1.types.DatabaseCharacterSet]):
            The list of DatabaseCharacterSets.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    database_character_sets: MutableSequence["DatabaseCharacterSet"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="DatabaseCharacterSet",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
