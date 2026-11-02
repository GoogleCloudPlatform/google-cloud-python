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

from google.cloud.sqladmin_v1.types import cloud_sql_resources

__protobuf__ = proto.module(
    package="google.cloud.sql.v1",
    manifest={
        "SqlDatabasesDeleteRequest",
        "SqlDatabasesGetRequest",
        "SqlDatabasesInsertRequest",
        "SqlDatabasesListRequest",
        "SqlDatabasesUpdateRequest",
        "DatabasesListResponse",
    },
)


class SqlDatabasesDeleteRequest(proto.Message):
    r"""Database delete request.

    Attributes:
        database (str):
            Name of the database to be deleted in the
            instance.
        instance (str):
            Database instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    database: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance: str = proto.Field(
        proto.STRING,
        number=2,
    )
    project: str = proto.Field(
        proto.STRING,
        number=3,
    )
    location: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SqlDatabasesGetRequest(proto.Message):
    r"""Database get request.

    Attributes:
        database (str):
            Name of the database in the instance.
        instance (str):
            Database instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    database: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance: str = proto.Field(
        proto.STRING,
        number=2,
    )
    project: str = proto.Field(
        proto.STRING,
        number=3,
    )
    location: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SqlDatabasesInsertRequest(proto.Message):
    r"""Database insert request.

    Attributes:
        instance (str):
            Database instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        body (google.cloud.sqladmin_v1.types.Database):

        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    body: cloud_sql_resources.Database = proto.Field(
        proto.MESSAGE,
        number=100,
        message=cloud_sql_resources.Database,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlDatabasesListRequest(proto.Message):
    r"""Database list request.

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlDatabasesUpdateRequest(proto.Message):
    r"""Database update request.

    Attributes:
        database (str):
            Name of the database to be updated in the
            instance.
        instance (str):
            Database instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        body (google.cloud.sqladmin_v1.types.Database):

        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    database: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance: str = proto.Field(
        proto.STRING,
        number=2,
    )
    project: str = proto.Field(
        proto.STRING,
        number=3,
    )
    body: cloud_sql_resources.Database = proto.Field(
        proto.MESSAGE,
        number=100,
        message=cloud_sql_resources.Database,
    )
    location: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DatabasesListResponse(proto.Message):
    r"""Database list response.

    Attributes:
        kind (str):
            This is always ``sql#databasesList``.
        items (MutableSequence[google.cloud.sqladmin_v1.types.Database]):
            List of database resources in the instance.
    """

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    items: MutableSequence[cloud_sql_resources.Database] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=cloud_sql_resources.Database,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
