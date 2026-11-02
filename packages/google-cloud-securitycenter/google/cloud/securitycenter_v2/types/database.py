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
        "Database",
    },
)


class Database(proto.Message):
    r"""Represents database access information, such as queries. A database
    may be a sub-resource of an instance (as in the case of Cloud SQL
    instances or Cloud Spanner instances), or the database instance
    itself. Some database resources might not have the `full resource
    name <https://google.aip.dev/122#full-resource-names>`__ populated
    because these resource types, such as Cloud SQL databases, are not
    yet supported by Cloud Asset Inventory. In these cases only the
    display name is provided.

    Attributes:
        name (str):
            Some database resources may not have the `full resource
            name <https://google.aip.dev/122#full-resource-names>`__
            populated because these resource types are not yet supported
            by Cloud Asset Inventory (e.g. Cloud SQL databases). In
            these cases only the display name will be provided. The
            `full resource
            name <https://google.aip.dev/122#full-resource-names>`__ of
            the database that the user connected to, if it is supported
            by Cloud Asset Inventory.
        display_name (str):
            The human-readable name of the database that
            the user connected to.
        user_name (str):
            The username used to connect to the database.
            The username might not be an IAM principal and
            does not have a set format.
        query (str):
            The SQL statement that is associated with the
            database access.
        grantees (MutableSequence[str]):
            The target usernames, roles, or groups of an
            SQL privilege grant, which is not an IAM policy
            change.
        version (str):
            The version of the database, for example, POSTGRES_14. See
            `the complete
            list <https://cloud.google.com/sql/docs/mysql/admin-api/rest/v1/SqlDatabaseVersion>`__.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    user_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    query: str = proto.Field(
        proto.STRING,
        number=4,
    )
    grantees: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    version: str = proto.Field(
        proto.STRING,
        number=6,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
