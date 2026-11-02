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

from google.cloud.alloydb_v1alpha.types import csql_resources, resources

__protobuf__ = proto.module(
    package="google.cloud.alloydb.v1alpha",
    manifest={
        "RestoreFromCloudSQLRequest",
    },
)


class RestoreFromCloudSQLRequest(proto.Message):
    r"""Message for registering Restoring from CloudSQL resource.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        cloudsql_backup_run_source (google.cloud.alloydb_v1alpha.types.CloudSQLBackupRunSource):
            Cluster created from CloudSQL backup run.

            This field is a member of `oneof`_ ``source``.
        parent (str):
            Required. The location of the new cluster.
            For the required format, see the comment on
            Cluster.name field.
        cluster_id (str):
            Required. ID of the requesting object.
        cluster (google.cloud.alloydb_v1alpha.types.Cluster):
            Required. The resource being created
    """

    cloudsql_backup_run_source: csql_resources.CloudSQLBackupRunSource = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="source",
        message=csql_resources.CloudSQLBackupRunSource,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cluster_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cluster: resources.Cluster = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.Cluster,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
