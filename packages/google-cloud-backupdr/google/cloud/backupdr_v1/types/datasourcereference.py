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

from google.cloud.backupdr_v1.types import backupvault, backupvault_cloudsql

__protobuf__ = proto.module(
    package="google.cloud.backupdr.v1",
    manifest={
        "DataSourceReference",
        "DataSourceBackupConfigInfo",
        "DataSourceGcpResourceInfo",
        "GetDataSourceReferenceRequest",
        "ListDataSourceReferencesRequest",
        "ListDataSourceReferencesResponse",
        "FetchDataSourceReferencesForResourceTypeRequest",
        "FetchDataSourceReferencesForResourceTypeResponse",
    },
)


class DataSourceReference(proto.Message):
    r"""DataSourceReference is a reference to a DataSource resource.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the DataSourceReference.
            Format:
            projects/{project}/locations/{location}/dataSourceReferences/{data_source_reference}
        data_source (str):
            Output only. The resource name of the
            DataSource. Format:

            projects/{project}/locations/{location}/backupVaults/{backupVault}/dataSources/{dataSource}
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the
            DataSourceReference was created.
        data_source_backup_config_state (google.cloud.backupdr_v1.types.BackupConfigState):
            Output only. The backup configuration state
            of the DataSource.
        data_source_backup_count (int):
            Output only. Number of backups in the
            DataSource.
        data_source_backup_config_info (google.cloud.backupdr_v1.types.DataSourceBackupConfigInfo):
            Output only. Information of backup
            configuration on the DataSource.
        data_source_gcp_resource_info (google.cloud.backupdr_v1.types.DataSourceGcpResourceInfo):
            Output only. The GCP resource that the
            DataSource is associated with.
        total_stored_bytes (int):
            Output only. Total size of the storage used
            by all backup resources for the referenced
            datasource.

            This field is a member of `oneof`_ ``_total_stored_bytes``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_source: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    data_source_backup_config_state: backupvault.BackupConfigState = proto.Field(
        proto.ENUM,
        number=4,
        enum=backupvault.BackupConfigState,
    )
    data_source_backup_count: int = proto.Field(
        proto.INT64,
        number=5,
    )
    data_source_backup_config_info: "DataSourceBackupConfigInfo" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="DataSourceBackupConfigInfo",
    )
    data_source_gcp_resource_info: "DataSourceGcpResourceInfo" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="DataSourceGcpResourceInfo",
    )
    total_stored_bytes: int = proto.Field(
        proto.INT64,
        number=8,
        optional=True,
    )


class DataSourceBackupConfigInfo(proto.Message):
    r"""Information of backup configuration on the DataSource.

    Attributes:
        last_backup_state (google.cloud.backupdr_v1.types.BackupConfigInfo.LastBackupState):
            Output only. The status of the last backup in
            this DataSource
        last_successful_backup_consistency_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp of the last successful
            backup to this DataSource.
    """

    last_backup_state: backupvault.BackupConfigInfo.LastBackupState = proto.Field(
        proto.ENUM,
        number=1,
        enum=backupvault.BackupConfigInfo.LastBackupState,
    )
    last_successful_backup_consistency_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class DataSourceGcpResourceInfo(proto.Message):
    r"""The GCP resource that the DataSource is associated with.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcp_resourcename (str):
            Output only. The resource name of the GCP
            resource. Ex:
            projects/{project}/zones/{zone}/instances/{instance}
        type_ (str):
            Output only. The type of the GCP resource.
            Ex: compute.googleapis.com/Instance
        location (str):
            Output only. The location of the GCP
            resource. Ex:
            <region>/<zone>/"global"/"unspecified".
        cloud_sql_instance_properties (google.cloud.backupdr_v1.types.CloudSqlInstanceDataSourceReferenceProperties):
            Output only. The properties of the Cloud SQL
            instance.

            This field is a member of `oneof`_ ``resource_properties``.
    """

    gcp_resourcename: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )
    cloud_sql_instance_properties: backupvault_cloudsql.CloudSqlInstanceDataSourceReferenceProperties = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="resource_properties",
        message=backupvault_cloudsql.CloudSqlInstanceDataSourceReferenceProperties,
    )


class GetDataSourceReferenceRequest(proto.Message):
    r"""Request for the GetDataSourceReference method.

    Attributes:
        name (str):
            Required. The name of the DataSourceReference to retrieve.
            Format:
            projects/{project}/locations/{location}/dataSourceReferences/{data_source_reference}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDataSourceReferencesRequest(proto.Message):
    r"""Request for the ListDataSourceReferences method.

    Attributes:
        parent (str):
            Required. The parent resource name.
            Format: projects/{project}/locations/{location}
        page_size (int):
            Optional. The maximum number of
            DataSourceReferences to return. The service may
            return fewer than this value. If unspecified, at
            most 50 DataSourceReferences will be returned.
            The maximum value is 100; values above 100 will
            be coerced to 100.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListDataSourceReferences`` call. Provide this to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``ListDataSourceReferences`` must match the call that
            provided the page token.
        filter (str):
            Optional. A filter expression that filters the results
            listed in the response. The expression must specify the
            field name, a comparison operator, and the value that you
            want to use for filtering.

            The following field and operator combinations are supported:

            - data_source_gcp_resource_info.gcp_resourcename with ``=``,
              ``!=``
            - data_source_gcp_resource_info.type with ``=``, ``!=``
        order_by (str):
            Optional. A comma-separated list of fields to order by,
            sorted in ascending order. Use "desc" after a field name for
            descending.

            Supported fields:

            - data_source
            - data_source_gcp_resource_info.gcp_resourcename
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
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListDataSourceReferencesResponse(proto.Message):
    r"""Response for the ListDataSourceReferences method.

    Attributes:
        data_source_references (MutableSequence[google.cloud.backupdr_v1.types.DataSourceReference]):
            The DataSourceReferences from the specified
            parent.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    data_source_references: MutableSequence["DataSourceReference"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="DataSourceReference",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class FetchDataSourceReferencesForResourceTypeRequest(proto.Message):
    r"""Request for the FetchDataSourceReferencesForResourceType
    method.

    Attributes:
        parent (str):
            Required. The parent resource name.
            Format: projects/{project}/locations/{location}
        resource_type (str):
            Required. The type of the GCP resource.
            Ex: sql.googleapis.com/Instance
        page_size (int):
            Optional. The maximum number of
            DataSourceReferences to return. The service may
            return fewer than this value. If unspecified, at
            most 50 DataSourceReferences will be returned.
            The maximum value is 100; values above 100 will
            be coerced to 100.
        page_token (str):
            Optional. A page token, received from a previous call of
            ``FetchDataSourceReferencesForResourceType``. Provide this
            to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``FetchDataSourceReferencesForResourceType`` must match the
            call that provided the page token.
        filter (str):
            Optional. A filter expression that filters the results
            fetched in the response. The expression must specify the
            field name, a comparison operator, and the value that you
            want to use for filtering. Supported fields:

            - data_source
            - data_source_gcp_resource_info.gcp_resourcename
            - data_source_backup_config_state
            - data_source_backup_count
            - data_source_backup_config_info.last_backup_state
            - data_source_gcp_resource_info.gcp_resourcename
            - data_source_gcp_resource_info.type
            - data_source_gcp_resource_info.location
            - data_source_gcp_resource_info.cloud_sql_instance_properties.instance_create_time
        order_by (str):
            Optional. A comma-separated list of fields to order by,
            sorted in ascending order. Use "desc" after a field name for
            descending.

            Supported fields:

            - name
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    resource_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=6,
    )


class FetchDataSourceReferencesForResourceTypeResponse(proto.Message):
    r"""Response for the FetchDataSourceReferencesForResourceType
    method.

    Attributes:
        data_source_references (MutableSequence[google.cloud.backupdr_v1.types.DataSourceReference]):
            The DataSourceReferences from the specified
            parent.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    data_source_references: MutableSequence["DataSourceReference"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="DataSourceReference",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
