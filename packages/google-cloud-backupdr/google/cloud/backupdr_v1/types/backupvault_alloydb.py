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
    package="google.cloud.backupdr.v1",
    manifest={
        "AlloyDBClusterDataSourceProperties",
        "AlloyDbClusterBackupProperties",
        "AlloyDBClusterBackupPlanAssociationProperties",
    },
)


class AlloyDBClusterDataSourceProperties(proto.Message):
    r"""AlloyDBClusterDataSourceProperties represents the properties
    of a AlloyDB cluster resource that are stored in the DataSource.
    .

    Attributes:
        name (str):
            Output only. Name of the AlloyDB cluster
            backed up by the datasource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AlloyDbClusterBackupProperties(proto.Message):
    r"""AlloyDbClusterBackupProperties represents AlloyDB cluster
    backup properties.
    .


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        description (str):
            An optional text description for the backup.

            This field is a member of `oneof`_ ``_description``.
        stored_bytes (int):
            Output only. Storage usage of this particular
            backup
        chain_id (str):
            Output only. The chain id of this backup.
            Backups belonging to the same chain are sharing
            the same chain id. This property is calculated
            and maintained by BackupDR.
        database_version (str):
            Output only. The PostgreSQL major version of
            the AlloyDB cluster when the backup was taken.
    """

    description: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    stored_bytes: int = proto.Field(
        proto.INT64,
        number=2,
    )
    chain_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    database_version: str = proto.Field(
        proto.STRING,
        number=4,
    )


class AlloyDBClusterBackupPlanAssociationProperties(proto.Message):
    r"""Properties for an AlloyDB cluster backup plan association.

    Attributes:
        cluster_uid (str):
            Output only. The cluster UID of the AlloyDB
            cluster.
    """

    cluster_uid: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
