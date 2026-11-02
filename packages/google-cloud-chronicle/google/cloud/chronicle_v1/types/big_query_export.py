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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.chronicle.v1",
    manifest={
        "BigQueryExportPackage",
        "LatestExportJobState",
        "BigQueryExport",
        "DataSourceExportSettings",
        "GetBigQueryExportRequest",
        "UpdateBigQueryExportRequest",
        "ProvisionBigQueryExportRequest",
    },
)


class BigQueryExportPackage(proto.Enum):
    r"""The BigQueryExportPackage entitled for the Chronicle
    instance.

    Values:
        BIG_QUERY_EXPORT_PACKAGE_UNSPECIFIED (0):
            The BigQueryExportPackage is unspecified.
        BIG_QUERY_EXPORT_PACKAGE_BYOBQ (1):
            The BigQueryExportPackage is Bring Your Own
            BigQuery.
        BIG_QUERY_EXPORT_PACKAGE_ADVANCED (2):
            The BigQueryExportPackage is Advanced
            BigQuery.
    """

    BIG_QUERY_EXPORT_PACKAGE_UNSPECIFIED = 0
    BIG_QUERY_EXPORT_PACKAGE_BYOBQ = 1
    BIG_QUERY_EXPORT_PACKAGE_ADVANCED = 2


class LatestExportJobState(proto.Enum):
    r"""The state of the latest data source export job.

    Values:
        LATEST_EXPORT_JOB_STATE_UNSPECIFIED (0):
            The latest export job state is unspecified.
        LATEST_EXPORT_JOB_STATE_SUCCESS (1):
            The latest export job state is successful.
        LATEST_EXPORT_JOB_STATE_FAILED (2):
            The latest export job state is failed.
    """

    LATEST_EXPORT_JOB_STATE_UNSPECIFIED = 0
    LATEST_EXPORT_JOB_STATE_SUCCESS = 1
    LATEST_EXPORT_JOB_STATE_FAILED = 2


class BigQueryExport(proto.Message):
    r"""This resource represents the BigQuery export configuration
    for a Chronicle instance which includes Google Cloud Platform
    resources like Cloud Storage buckets, BigQuery datasets etc and
    the export settings for each data source.

    Attributes:
        name (str):
            Identifier. The resource name of the
            BigQueryExport. Format:

            projects/{project}/locations/{location}/instances/{instance}/bigQueryExport
        provisioned (bool):
            Output only. Whether the BigQueryExport has
            been provisioned for the Chronicle instance.
        big_query_export_package (google.cloud.chronicle_v1.types.BigQueryExportPackage):
            Output only. The BigQueryExportPackage
            entitled for the Chronicle instance.
        entity_graph_settings (google.cloud.chronicle_v1.types.DataSourceExportSettings):
            Optional. The export settings for the Entity
            Graph data source.
        ioc_matches_settings (google.cloud.chronicle_v1.types.DataSourceExportSettings):
            Optional. The export settings for the IOC
            Matches data source.
        rule_detections_settings (google.cloud.chronicle_v1.types.DataSourceExportSettings):
            Optional. The export settings for the Rule
            Detections data source.
        udm_events_aggregates_settings (google.cloud.chronicle_v1.types.DataSourceExportSettings):
            Optional. The export settings for the UDM
            Events Aggregates data source.
        udm_events_settings (google.cloud.chronicle_v1.types.DataSourceExportSettings):
            Optional. The export settings for the UDM
            Events data source.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    provisioned: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    big_query_export_package: "BigQueryExportPackage" = proto.Field(
        proto.ENUM,
        number=3,
        enum="BigQueryExportPackage",
    )
    entity_graph_settings: "DataSourceExportSettings" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="DataSourceExportSettings",
    )
    ioc_matches_settings: "DataSourceExportSettings" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="DataSourceExportSettings",
    )
    rule_detections_settings: "DataSourceExportSettings" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="DataSourceExportSettings",
    )
    udm_events_aggregates_settings: "DataSourceExportSettings" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="DataSourceExportSettings",
    )
    udm_events_settings: "DataSourceExportSettings" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="DataSourceExportSettings",
    )


class DataSourceExportSettings(proto.Message):
    r"""The export settings for a data source.

    Attributes:
        enabled (bool):
            Required. Whether the data source is enabled
            for export.
        retention_days (int):
            Required. The retention period for the data
            source in days.
        latest_export_job_state (google.cloud.chronicle_v1.types.LatestExportJobState):
            Output only. The state of the latest data
            source export job.
        data_freshness_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The data freshness of the given
            export which represents the time bucket at which
            the latest event was exported.
        data_volume (int):
            Output only. The stored data volume of all
            the exports.
    """

    enabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    retention_days: int = proto.Field(
        proto.INT32,
        number=2,
    )
    latest_export_job_state: "LatestExportJobState" = proto.Field(
        proto.ENUM,
        number=3,
        enum="LatestExportJobState",
    )
    data_freshness_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    data_volume: int = proto.Field(
        proto.INT64,
        number=5,
    )


class GetBigQueryExportRequest(proto.Message):
    r"""The request message to fetch BigQuery Export configuration.

    Attributes:
        name (str):
            Required. The resource name of the
            BigqueryExport to retrieve. Format:

            projects/{project}/locations/{location}/instances/{instance}/bigQueryExport
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateBigQueryExportRequest(proto.Message):
    r"""The request message to update BigQuery Export configuration.

    Attributes:
        big_query_export (google.cloud.chronicle_v1.types.BigQueryExport):
            Required. The BigQueryExport settings to
            update. Format:

            projects/{project}/locations/{location}/instances/{instance}/bigQueryExport
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    big_query_export: "BigQueryExport" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="BigQueryExport",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class ProvisionBigQueryExportRequest(proto.Message):
    r"""The request message to provision BigQuery Export
    configuration.

    Attributes:
        parent (str):
            Required. The instance for which BigQuery
            export is being provisioned. Format:
            projects/{project}/locations/{location}/instances/{instance}
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
