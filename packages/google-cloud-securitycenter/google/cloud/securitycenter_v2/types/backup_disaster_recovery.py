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
    package="google.cloud.securitycenter.v2",
    manifest={
        "BackupDisasterRecovery",
    },
)


class BackupDisasterRecovery(proto.Message):
    r"""Information related to Google Cloud Backup and DR Service
    findings.

    Attributes:
        backup_template (str):
            The name of a Backup and DR template which comprises one or
            more backup policies. See the `Backup and DR
            documentation <https://cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan#temp>`__
            for more information. For example, ``snap-ov``.
        policies (MutableSequence[str]):
            The names of Backup and DR policies that are associated with
            a template and that define when to run a backup, how
            frequently to run a backup, and how long to retain the
            backup image. For example, ``onvaults``.
        host (str):
            The name of a Backup and DR host, which is managed by the
            backup and recovery appliance and known to the management
            console. The host can be of type Generic (for example,
            Compute Engine, SQL Server, Oracle DB, SMB file system,
            etc.), vCenter, or an ESX server. See the `Backup and DR
            documentation on
            hosts <https://cloud.google.com/backup-disaster-recovery/docs/configuration/manage-hosts-and-their-applications>`__
            for more information. For example, ``centos7-01``.
        applications (MutableSequence[str]):
            The names of Backup and DR applications. An application is a
            VM, database, or file system on a managed host monitored by
            a backup and recovery appliance. For example,
            ``centos7-01-vol00``, ``centos7-01-vol01``,
            ``centos7-01-vol02``.
        storage_pool (str):
            The name of the Backup and DR storage pool that the backup
            and recovery appliance is storing data in. The storage pool
            could be of type Cloud, Primary, Snapshot, or OnVault. See
            the `Backup and DR documentation on storage
            pools <https://cloud.google.com/backup-disaster-recovery/docs/concepts/storage-pools>`__.
            For example, ``DiskPoolOne``.
        policy_options (MutableSequence[str]):
            The names of Backup and DR advanced policy options of a
            policy applying to an application. See the `Backup and DR
            documentation on policy
            options <https://cloud.google.com/backup-disaster-recovery/docs/create-plan/policy-settings>`__.
            For example, ``skipofflineappsincongrp, nounmap``.
        profile (str):
            The name of the Backup and DR resource profile that
            specifies the storage media for backups of application and
            VM data. See the `Backup and DR documentation on
            profiles <https://cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan#profile>`__.
            For example, ``GCP``.
        appliance (str):
            The name of the Backup and DR appliance that captures,
            moves, and manages the lifecycle of backup data. For
            example, ``backup-server-57137``.
        backup_type (str):
            The backup type of the Backup and DR image. For example,
            ``Snapshot``, ``Remote Snapshot``, ``OnVault``.
        backup_create_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp at which the Backup and DR
            backup was created.
    """

    backup_template: str = proto.Field(
        proto.STRING,
        number=1,
    )
    policies: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    host: str = proto.Field(
        proto.STRING,
        number=3,
    )
    applications: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    storage_pool: str = proto.Field(
        proto.STRING,
        number=5,
    )
    policy_options: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    profile: str = proto.Field(
        proto.STRING,
        number=7,
    )
    appliance: str = proto.Field(
        proto.STRING,
        number=8,
    )
    backup_type: str = proto.Field(
        proto.STRING,
        number=9,
    )
    backup_create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
