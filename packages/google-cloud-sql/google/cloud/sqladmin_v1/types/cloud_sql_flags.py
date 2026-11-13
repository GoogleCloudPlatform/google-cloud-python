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

import google.protobuf.wrappers_pb2 as wrappers_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.sqladmin_v1.types import cloud_sql_resources

__protobuf__ = proto.module(
    package="google.cloud.sql.v1",
    manifest={
        "SqlFlagType",
        "SqlFlagScope",
        "SqlFlagsListRequest",
        "FlagsListResponse",
        "Flag",
    },
)


class SqlFlagType(proto.Enum):
    r"""

    Values:
        SQL_FLAG_TYPE_UNSPECIFIED (0):
            This is an unknown flag type.
        BOOLEAN (1):
            Boolean type flag.
        STRING (2):
            String type flag.
        INTEGER (3):
            Integer type flag.
        NONE (4):
            Flag type used for a server startup option.
        MYSQL_TIMEZONE_OFFSET (5):
            Type introduced specially for MySQL TimeZone offset. Accept
            a string value with the format [-12:59, 13:00].
        FLOAT (6):
            Float type flag.
        REPEATED_STRING (7):
            Comma-separated list of the strings in a
            SqlFlagType enum.
    """

    SQL_FLAG_TYPE_UNSPECIFIED = 0
    BOOLEAN = 1
    STRING = 2
    INTEGER = 3
    NONE = 4
    MYSQL_TIMEZONE_OFFSET = 5
    FLOAT = 6
    REPEATED_STRING = 7


class SqlFlagScope(proto.Enum):
    r"""Scopes of a flag describe where the flag is used.

    Values:
        SQL_FLAG_SCOPE_UNSPECIFIED (0):
            Assume database flags if unspecified
        SQL_FLAG_SCOPE_DATABASE (1):
            database flags
        SQL_FLAG_SCOPE_CONNECTION_POOL (2):
            connection pool configuration flags
    """

    SQL_FLAG_SCOPE_UNSPECIFIED = 0
    SQL_FLAG_SCOPE_DATABASE = 1
    SQL_FLAG_SCOPE_CONNECTION_POOL = 2


class SqlFlagsListRequest(proto.Message):
    r"""Flags list request.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        database_version (str):
            Database type and version you want to
            retrieve flags for. By default, this method
            returns flags for all database types and
            versions.
        flag_scope (google.cloud.sqladmin_v1.types.SqlFlagScope):
            Optional. Specify the scope of flags to be
            returned by SqlFlagsListService. Return list of
            database flags if unspecified.

            This field is a member of `oneof`_ ``_flag_scope``.
    """

    database_version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    flag_scope: "SqlFlagScope" = proto.Field(
        proto.ENUM,
        number=3,
        optional=True,
        enum="SqlFlagScope",
    )


class FlagsListResponse(proto.Message):
    r"""Flags list response.

    Attributes:
        kind (str):
            This is always ``sql#flagsList``.
        items (MutableSequence[google.cloud.sqladmin_v1.types.Flag]):
            List of flags.
    """

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    items: MutableSequence["Flag"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Flag",
    )


class Flag(proto.Message):
    r"""A flag resource.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            This is the name of the flag. Flag names always use
            underscores, not hyphens, for example:
            ``max_allowed_packet``
        type_ (google.cloud.sqladmin_v1.types.SqlFlagType):
            The type of the flag. Flags are typed to being ``BOOLEAN``,
            ``STRING``, ``INTEGER`` or ``NONE``. ``NONE`` is used for
            flags that do not take a value, such as
            ``skip_grant_tables``.
        applies_to (MutableSequence[google.cloud.sqladmin_v1.types.SqlDatabaseVersion]):
            The database version this flag applies to. Can be MySQL
            instances: ``MYSQL_8_0``, ``MYSQL_8_0_18``,
            ``MYSQL_8_0_26``, ``MYSQL_5_7``, or ``MYSQL_5_6``.
            PostgreSQL instances: ``POSTGRES_9_6``, ``POSTGRES_10``,
            ``POSTGRES_11`` or ``POSTGRES_12``. SQL Server instances:
            ``SQLSERVER_2017_STANDARD``, ``SQLSERVER_2017_ENTERPRISE``,
            ``SQLSERVER_2017_EXPRESS``, ``SQLSERVER_2017_WEB``,
            ``SQLSERVER_2019_STANDARD``, ``SQLSERVER_2019_ENTERPRISE``,
            ``SQLSERVER_2019_EXPRESS``, or ``SQLSERVER_2019_WEB``. See
            `the complete
            list </sql/docs/mysql/admin-api/rest/v1/SqlDatabaseVersion>`__.
        allowed_string_values (MutableSequence[str]):
            For ``STRING`` flags, a list of strings that the value can
            be set to.
        min_value (google.protobuf.wrappers_pb2.Int64Value):
            For ``INTEGER`` flags, the minimum allowed value.
        max_value (google.protobuf.wrappers_pb2.Int64Value):
            For ``INTEGER`` flags, the maximum allowed value.
        requires_restart (google.protobuf.wrappers_pb2.BoolValue):
            Indicates whether changing this flag will
            trigger a database restart. Only applicable to
            Second Generation instances.
        kind (str):
            This is always ``sql#flag``.
        in_beta (google.protobuf.wrappers_pb2.BoolValue):
            Whether or not the flag is considered in
            beta.
        allowed_int_values (MutableSequence[int]):
            Use this field if only certain integers are accepted. Can be
            combined with min_value and max_value to add additional
            values.
        flag_scope (google.cloud.sqladmin_v1.types.SqlFlagScope):
            Scope of flag.
        recommended_string_value (str):
            Recommended string value in string format for
            UI display.

            This field is a member of `oneof`_ ``recommended_value``.
        recommended_int_value (google.protobuf.wrappers_pb2.Int64Value):
            Recommended int value in integer format for
            UI display.

            This field is a member of `oneof`_ ``recommended_value``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: "SqlFlagType" = proto.Field(
        proto.ENUM,
        number=2,
        enum="SqlFlagType",
    )
    applies_to: MutableSequence[cloud_sql_resources.SqlDatabaseVersion] = (
        proto.RepeatedField(
            proto.ENUM,
            number=3,
            enum=cloud_sql_resources.SqlDatabaseVersion,
        )
    )
    allowed_string_values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    min_value: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=5,
        message=wrappers_pb2.Int64Value,
    )
    max_value: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=6,
        message=wrappers_pb2.Int64Value,
    )
    requires_restart: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=7,
        message=wrappers_pb2.BoolValue,
    )
    kind: str = proto.Field(
        proto.STRING,
        number=8,
    )
    in_beta: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=9,
        message=wrappers_pb2.BoolValue,
    )
    allowed_int_values: MutableSequence[int] = proto.RepeatedField(
        proto.INT64,
        number=10,
    )
    flag_scope: "SqlFlagScope" = proto.Field(
        proto.ENUM,
        number=15,
        enum="SqlFlagScope",
    )
    recommended_string_value: str = proto.Field(
        proto.STRING,
        number=16,
        oneof="recommended_value",
    )
    recommended_int_value: wrappers_pb2.Int64Value = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="recommended_value",
        message=wrappers_pb2.Int64Value,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
