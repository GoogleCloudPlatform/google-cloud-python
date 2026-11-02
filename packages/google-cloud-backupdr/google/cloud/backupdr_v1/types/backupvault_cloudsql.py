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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.backupdr.v1",
    manifest={
        "CloudSqlInstanceDataSourceProperties",
        "CloudSqlInstanceBackupProperties",
        "CloudSqlInstanceDataSourceReferenceProperties",
        "CloudSqlInstanceInitializationConfig",
        "CloudSqlInstanceBackupPlanAssociationProperties",
    },
)


class CloudSqlInstanceDataSourceProperties(proto.Message):
    r"""CloudSqlInstanceDataSourceProperties represents the
    properties of a Cloud SQL resource that are stored in the
    DataSource.

    Attributes:
        name (str):
            Output only. Name of the Cloud SQL instance
            backed up by the datasource. Format:

            projects/{project}/instances/{instance}
        database_installed_version (str):
            Output only. The installed database version
            of the Cloud SQL instance.
        instance_create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The instance creation timestamp.
        instance_tier (str):
            Output only. The tier (or machine type) for this instance.
            Example: ``db-custom-1-3840``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    database_installed_version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    instance_create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    instance_tier: str = proto.Field(
        proto.STRING,
        number=5,
    )


class CloudSqlInstanceBackupProperties(proto.Message):
    r"""CloudSqlInstanceBackupProperties represents Cloud SQL
    Instance Backup properties.

    Attributes:
        database_installed_version (str):
            Output only. The installed database version
            of the Cloud SQL instance when the backup was
            taken.
        final_backup (bool):
            Output only. Whether the backup is a final
            backup.
        source_instance (str):
            Output only. The source instance of the
            backup. Format:

            projects/{project}/instances/{instance}
        instance_create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The instance creation timestamp.
        instance_tier (str):
            Output only. The tier (or machine type) for this instance.
            Example: ``db-custom-1-3840``
        instance_delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The instance delete timestamp.
    """

    database_installed_version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    final_backup: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    source_instance: str = proto.Field(
        proto.STRING,
        number=4,
    )
    instance_create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    instance_tier: str = proto.Field(
        proto.STRING,
        number=6,
    )
    instance_delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )


class CloudSqlInstanceDataSourceReferenceProperties(proto.Message):
    r"""CloudSqlInstanceDataSourceReferenceProperties represents the
    properties of a Cloud SQL resource that are stored in the
    DataSourceReference.

    Attributes:
        name (str):
            Output only. Name of the Cloud SQL instance
            backed up by the datasource. Format:

            projects/{project}/instances/{instance}
        database_installed_version (str):
            Output only. The installed database version
            of the Cloud SQL instance.
        instance_create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The instance creation timestamp.
        instance_tier (str):
            Output only. The tier (or machine type) for this instance.
            Example: ``db-custom-1-3840``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    database_installed_version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    instance_create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    instance_tier: str = proto.Field(
        proto.STRING,
        number=5,
    )


class CloudSqlInstanceInitializationConfig(proto.Message):
    r"""CloudSqlInstanceInitializationConfig contains the
    configuration for initializing a Cloud SQL instance.

    Attributes:
        edition (google.cloud.backupdr_v1.types.CloudSqlInstanceInitializationConfig.Edition):
            Required. The edition of the Cloud SQL
            instance.
    """

    class Edition(proto.Enum):
        r"""The edition of the Cloud SQL instance. For details, see
        https://cloud.google.com/sql/docs/editions-intro.

        Values:
            EDITION_UNSPECIFIED (0):
                Unspecified edition.
            ENTERPRISE (1):
                Enterprise edition.
            ENTERPRISE_PLUS (2):
                Enterprise Plus edition.
        """

        EDITION_UNSPECIFIED = 0
        ENTERPRISE = 1
        ENTERPRISE_PLUS = 2

    edition: Edition = proto.Field(
        proto.ENUM,
        number=1,
        enum=Edition,
    )


class CloudSqlInstanceBackupPlanAssociationProperties(proto.Message):
    r"""Cloud SQL instance's BPA properties.

    Attributes:
        instance_create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the instance was
            created.
    """

    instance_create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
