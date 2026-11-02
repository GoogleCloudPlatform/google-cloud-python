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
    package="google.cloud.datacatalog.v1",
    manifest={
        "BigQueryConnectionSpec",
        "CloudSqlBigQueryConnectionSpec",
        "BigQueryRoutineSpec",
    },
)


class BigQueryConnectionSpec(proto.Message):
    r"""Specification for the BigQuery connection.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        connection_type (google.cloud.datacatalog_v1.types.BigQueryConnectionSpec.ConnectionType):
            The type of the BigQuery connection.
        cloud_sql (google.cloud.datacatalog_v1.types.CloudSqlBigQueryConnectionSpec):
            Specification for the BigQuery connection to
            a Cloud SQL instance.

            This field is a member of `oneof`_ ``connection_spec``.
        has_credential (bool):
            True if there are credentials attached to the
            BigQuery connection; false otherwise.
    """

    class ConnectionType(proto.Enum):
        r"""The type of the BigQuery connection.

        Values:
            CONNECTION_TYPE_UNSPECIFIED (0):
                Unspecified type.
            CLOUD_SQL (1):
                Cloud SQL connection.
        """

        CONNECTION_TYPE_UNSPECIFIED = 0
        CLOUD_SQL = 1

    connection_type: ConnectionType = proto.Field(
        proto.ENUM,
        number=1,
        enum=ConnectionType,
    )
    cloud_sql: "CloudSqlBigQueryConnectionSpec" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="connection_spec",
        message="CloudSqlBigQueryConnectionSpec",
    )
    has_credential: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class CloudSqlBigQueryConnectionSpec(proto.Message):
    r"""Specification for the BigQuery connection to a Cloud SQL
    instance.

    Attributes:
        instance_id (str):
            Cloud SQL instance ID in the format of
            ``project:location:instance``.
        database (str):
            Database name.
        type_ (google.cloud.datacatalog_v1.types.CloudSqlBigQueryConnectionSpec.DatabaseType):
            Type of the Cloud SQL database.
    """

    class DatabaseType(proto.Enum):
        r"""Supported Cloud SQL database types.

        Values:
            DATABASE_TYPE_UNSPECIFIED (0):
                Unspecified database type.
            POSTGRES (1):
                Cloud SQL for PostgreSQL.
            MYSQL (2):
                Cloud SQL for MySQL.
        """

        DATABASE_TYPE_UNSPECIFIED = 0
        POSTGRES = 1
        MYSQL = 2

    instance_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    database: str = proto.Field(
        proto.STRING,
        number=2,
    )
    type_: DatabaseType = proto.Field(
        proto.ENUM,
        number=3,
        enum=DatabaseType,
    )


class BigQueryRoutineSpec(proto.Message):
    r"""Fields specific for BigQuery routines.

    Attributes:
        imported_libraries (MutableSequence[str]):
            Paths of the imported libraries.
    """

    imported_libraries: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
