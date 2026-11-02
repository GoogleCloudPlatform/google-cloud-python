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

from google.cloud.datacatalog_v1.types import common, physical_schema

__protobuf__ = proto.module(
    package="google.cloud.datacatalog.v1",
    manifest={
        "DataplexSpec",
        "DataplexFilesetSpec",
        "DataplexTableSpec",
        "DataplexExternalTable",
    },
)


class DataplexSpec(proto.Message):
    r"""Common Dataplex fields.

    Attributes:
        asset (str):
            Fully qualified resource name of an asset in
            Dataplex, to which the underlying data source
            (Cloud Storage bucket or BigQuery dataset) of
            the entity is attached.
        data_format (google.cloud.datacatalog_v1.types.PhysicalSchema):
            Format of the data.
        compression_format (str):
            Compression format of the data, e.g., zip,
            gzip etc.
        project_id (str):
            Project ID of the underlying Cloud Storage or
            BigQuery data. Note that this may not be the
            same project as the correspondingly Dataplex
            lake / zone / asset.
    """

    asset: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_format: physical_schema.PhysicalSchema = proto.Field(
        proto.MESSAGE,
        number=2,
        message=physical_schema.PhysicalSchema,
    )
    compression_format: str = proto.Field(
        proto.STRING,
        number=3,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DataplexFilesetSpec(proto.Message):
    r"""Entry specyfication for a Dataplex fileset.

    Attributes:
        dataplex_spec (google.cloud.datacatalog_v1.types.DataplexSpec):
            Common Dataplex fields.
    """

    dataplex_spec: "DataplexSpec" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="DataplexSpec",
    )


class DataplexTableSpec(proto.Message):
    r"""Entry specification for a Dataplex table.

    Attributes:
        external_tables (MutableSequence[google.cloud.datacatalog_v1.types.DataplexExternalTable]):
            List of external tables registered by
            Dataplex in other systems based on the same
            underlying data.

            External tables allow to query this data in
            those systems.
        dataplex_spec (google.cloud.datacatalog_v1.types.DataplexSpec):
            Common Dataplex fields.
        user_managed (bool):
            Indicates if the table schema is managed by
            the user or not.
    """

    external_tables: MutableSequence["DataplexExternalTable"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DataplexExternalTable",
    )
    dataplex_spec: "DataplexSpec" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DataplexSpec",
    )
    user_managed: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class DataplexExternalTable(proto.Message):
    r"""External table registered by Dataplex.
    Dataplex publishes data discovered from an asset into multiple
    other systems (BigQuery, DPMS) in form of tables. We call them
    "external tables". External tables are also synced into the Data
    Catalog.
    This message contains pointers to
    those external tables (fully qualified name, resource name et
    cetera) within the Data Catalog.

    Attributes:
        system (google.cloud.datacatalog_v1.types.IntegratedSystem):
            Service in which the external table is
            registered.
        fully_qualified_name (str):
            Fully qualified name (FQN) of the external
            table.
        google_cloud_resource (str):
            Google Cloud resource name of the external
            table.
        data_catalog_entry (str):
            Name of the Data Catalog entry representing
            the external table.
    """

    system: common.IntegratedSystem = proto.Field(
        proto.ENUM,
        number=1,
        enum=common.IntegratedSystem,
    )
    fully_qualified_name: str = proto.Field(
        proto.STRING,
        number=28,
    )
    google_cloud_resource: str = proto.Field(
        proto.STRING,
        number=3,
    )
    data_catalog_entry: str = proto.Field(
        proto.STRING,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
