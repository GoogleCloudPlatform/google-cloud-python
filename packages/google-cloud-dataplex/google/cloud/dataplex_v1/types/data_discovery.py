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
    package="google.cloud.dataplex.v1",
    manifest={
        "DataDiscoverySpec",
        "DataDiscoveryResult",
    },
)


class DataDiscoverySpec(proto.Message):
    r"""Spec for a data discovery scan.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        bigquery_publishing_config (google.cloud.dataplex_v1.types.DataDiscoverySpec.BigQueryPublishingConfig):
            Optional. Configuration for metadata
            publishing.
        storage_config (google.cloud.dataplex_v1.types.DataDiscoverySpec.StorageConfig):
            Cloud Storage related configurations.

            This field is a member of `oneof`_ ``resource_config``.
    """

    class BigQueryPublishingConfig(proto.Message):
        r"""Describes BigQuery publishing configurations.

        Attributes:
            table_type (google.cloud.dataplex_v1.types.DataDiscoverySpec.BigQueryPublishingConfig.TableType):
                Optional. Determines whether to  publish
                discovered tables as BigLake external tables or
                non-BigLake external tables.
            connection (str):
                Optional. The BigQuery connection used to create BigLake
                tables. Must be in the form
                ``projects/{project_id}/locations/{location_id}/connections/{connection_id}``
            location (str):
                Optional. The location of the BigQuery dataset to publish
                BigLake external or non-BigLake external tables to.

                1. If the Cloud Storage bucket is located in a multi-region
                   bucket, then BigQuery dataset can be in the same
                   multi-region bucket or any single region that is included
                   in the same multi-region bucket. The datascan can be
                   created in any single region that is included in the same
                   multi-region bucket
                2. If the Cloud Storage bucket is located in a dual-region
                   bucket, then BigQuery dataset can be located in regions
                   that are included in the dual-region bucket, or in a
                   multi-region that includes the dual-region. The datascan
                   can be created in any single region that is included in
                   the same dual-region bucket.
                3. If the Cloud Storage bucket is located in a single
                   region, then BigQuery dataset can be in the same single
                   region or any multi-region bucket that includes the same
                   single region. The datascan will be created in the same
                   single region as the bucket.
                4. If the BigQuery dataset is in single region, it must be
                   in the same single region as the datascan.

                For supported values, refer to
                https://cloud.google.com/bigquery/docs/locations#supported_locations.
            project (str):
                Optional. The project of the BigQuery dataset to publish
                BigLake external or non-BigLake external tables to. If not
                specified, the project of the Cloud Storage bucket will be
                used. The format is "projects/{project_id_or_number}".
        """

        class TableType(proto.Enum):
            r"""Determines how discovered tables are published.

            Values:
                TABLE_TYPE_UNSPECIFIED (0):
                    Table type unspecified.
                EXTERNAL (1):
                    Default. Discovered tables are published as
                    BigQuery external tables whose data is accessed
                    using the credentials of the user querying the
                    table.
                BIGLAKE (2):
                    Discovered tables are published as BigLake
                    external tables whose data is accessed using the
                    credentials of the associated BigQuery
                    connection.
            """

            TABLE_TYPE_UNSPECIFIED = 0
            EXTERNAL = 1
            BIGLAKE = 2

        table_type: "DataDiscoverySpec.BigQueryPublishingConfig.TableType" = (
            proto.Field(
                proto.ENUM,
                number=2,
                enum="DataDiscoverySpec.BigQueryPublishingConfig.TableType",
            )
        )
        connection: str = proto.Field(
            proto.STRING,
            number=3,
        )
        location: str = proto.Field(
            proto.STRING,
            number=4,
        )
        project: str = proto.Field(
            proto.STRING,
            number=5,
        )

    class StorageConfig(proto.Message):
        r"""Configurations related to Cloud Storage as the data source.

        Attributes:
            include_patterns (MutableSequence[str]):
                Optional. Defines the data to include during
                discovery when only a subset of the data should
                be considered. Provide a list of patterns that
                identify the data to include. For Cloud Storage
                bucket assets, these patterns are interpreted as
                glob patterns used to match object names. For
                BigQuery dataset assets, these patterns are
                interpreted as patterns to match table names.
            exclude_patterns (MutableSequence[str]):
                Optional. Defines the data to exclude during
                discovery. Provide a list of patterns that
                identify the data to exclude. For Cloud Storage
                bucket assets, these patterns are interpreted as
                glob patterns used to match object names. For
                BigQuery dataset assets, these patterns are
                interpreted as patterns to match table names.
            csv_options (google.cloud.dataplex_v1.types.DataDiscoverySpec.StorageConfig.CsvOptions):
                Optional. Configuration for CSV data.
            json_options (google.cloud.dataplex_v1.types.DataDiscoverySpec.StorageConfig.JsonOptions):
                Optional. Configuration for JSON data.
            unstructured_data_options (google.cloud.dataplex_v1.types.DataDiscoverySpec.StorageConfig.UnstructuredDataOptions):
                Optional. Specifies configuration for
                unstructured data discovery.
        """

        class CsvOptions(proto.Message):
            r"""Describes CSV and similar semi-structured data formats.

            Attributes:
                header_rows (int):
                    Optional. The number of rows to interpret as
                    header rows that should be skipped when reading
                    data rows.
                delimiter (str):
                    Optional. The delimiter that is used to separate values. The
                    default is ``,`` (comma).
                encoding (str):
                    Optional. The character encoding of the data.
                    The default is UTF-8.
                type_inference_disabled (bool):
                    Optional. Whether to disable the inference of
                    data types for CSV data. If true, all columns
                    are registered as strings.
                quote (str):
                    Optional. The character used to quote column values. Accepts
                    ``"`` (double quotation mark) or ``'`` (single quotation
                    mark). If unspecified, defaults to ``"`` (double quotation
                    mark).
            """

            header_rows: int = proto.Field(
                proto.INT32,
                number=1,
            )
            delimiter: str = proto.Field(
                proto.STRING,
                number=2,
            )
            encoding: str = proto.Field(
                proto.STRING,
                number=3,
            )
            type_inference_disabled: bool = proto.Field(
                proto.BOOL,
                number=4,
            )
            quote: str = proto.Field(
                proto.STRING,
                number=5,
            )

        class JsonOptions(proto.Message):
            r"""Describes JSON data format.

            Attributes:
                encoding (str):
                    Optional. The character encoding of the data.
                    The default is UTF-8.
                type_inference_disabled (bool):
                    Optional. Whether to disable the inference of
                    data types for JSON data. If true, all columns
                    are registered as their primitive types
                    (strings, number, or boolean).
            """

            encoding: str = proto.Field(
                proto.STRING,
                number=1,
            )
            type_inference_disabled: bool = proto.Field(
                proto.BOOL,
                number=2,
            )

        class UnstructuredDataOptions(proto.Message):
            r"""Describes options for unstructured data discovery.

            Attributes:
                semantic_inference_enabled (bool):
                    Optional. Specifies whether deeper semantic
                    inference over the objects' contents using GenAI
                    is enabled.
            """

            semantic_inference_enabled: bool = proto.Field(
                proto.BOOL,
                number=2,
            )

        include_patterns: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        exclude_patterns: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        csv_options: "DataDiscoverySpec.StorageConfig.CsvOptions" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="DataDiscoverySpec.StorageConfig.CsvOptions",
        )
        json_options: "DataDiscoverySpec.StorageConfig.JsonOptions" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="DataDiscoverySpec.StorageConfig.JsonOptions",
        )
        unstructured_data_options: "DataDiscoverySpec.StorageConfig.UnstructuredDataOptions" = proto.Field(
            proto.MESSAGE,
            number=5,
            message="DataDiscoverySpec.StorageConfig.UnstructuredDataOptions",
        )

    bigquery_publishing_config: BigQueryPublishingConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=BigQueryPublishingConfig,
    )
    storage_config: StorageConfig = proto.Field(
        proto.MESSAGE,
        number=100,
        oneof="resource_config",
        message=StorageConfig,
    )


class DataDiscoveryResult(proto.Message):
    r"""The output of a data discovery scan.

    Attributes:
        bigquery_publishing (google.cloud.dataplex_v1.types.DataDiscoveryResult.BigQueryPublishing):
            Output only. Configuration for metadata
            publishing.
        scan_statistics (google.cloud.dataplex_v1.types.DataDiscoveryResult.ScanStatistics):
            Output only. Describes result statistics of a
            data scan discovery job.
    """

    class BigQueryPublishing(proto.Message):
        r"""Describes BigQuery publishing configurations.

        Attributes:
            dataset (str):
                Output only. The BigQuery dataset the
                discovered tables are published to.
            location (str):
                Output only. The location of the BigQuery
                publishing dataset.
        """

        dataset: str = proto.Field(
            proto.STRING,
            number=1,
        )
        location: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class ScanStatistics(proto.Message):
        r"""Describes result statistics of a data scan discovery job.

        Attributes:
            scanned_file_count (int):
                The number of files scanned.
            data_processed_bytes (int):
                The data processed in bytes.
            files_excluded (int):
                The number of files excluded.
            tables_created (int):
                The number of tables created.
            tables_deleted (int):
                The number of tables deleted.
            tables_updated (int):
                The number of tables updated.
            filesets_created (int):
                The number of filesets created.
            filesets_deleted (int):
                The number of filesets deleted.
            filesets_updated (int):
                The number of filesets updated.
        """

        scanned_file_count: int = proto.Field(
            proto.INT32,
            number=1,
        )
        data_processed_bytes: int = proto.Field(
            proto.INT64,
            number=2,
        )
        files_excluded: int = proto.Field(
            proto.INT32,
            number=3,
        )
        tables_created: int = proto.Field(
            proto.INT32,
            number=4,
        )
        tables_deleted: int = proto.Field(
            proto.INT32,
            number=5,
        )
        tables_updated: int = proto.Field(
            proto.INT32,
            number=6,
        )
        filesets_created: int = proto.Field(
            proto.INT32,
            number=7,
        )
        filesets_deleted: int = proto.Field(
            proto.INT32,
            number=8,
        )
        filesets_updated: int = proto.Field(
            proto.INT32,
            number=9,
        )

    bigquery_publishing: BigQueryPublishing = proto.Field(
        proto.MESSAGE,
        number=1,
        message=BigQueryPublishing,
    )
    scan_statistics: ScanStatistics = proto.Field(
        proto.MESSAGE,
        number=2,
        message=ScanStatistics,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
