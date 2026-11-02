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
    package="google.cloud.datacatalog.v1",
    manifest={
        "TableSourceType",
        "BigQueryTableSpec",
        "ViewSpec",
        "TableSpec",
        "BigQueryDateShardedSpec",
    },
)


class TableSourceType(proto.Enum):
    r"""Table source type.

    Values:
        TABLE_SOURCE_TYPE_UNSPECIFIED (0):
            Default unknown type.
        BIGQUERY_VIEW (2):
            Table view.
        BIGQUERY_TABLE (5):
            BigQuery native table.
        BIGQUERY_MATERIALIZED_VIEW (7):
            BigQuery materialized view.
    """

    TABLE_SOURCE_TYPE_UNSPECIFIED = 0
    BIGQUERY_VIEW = 2
    BIGQUERY_TABLE = 5
    BIGQUERY_MATERIALIZED_VIEW = 7


class BigQueryTableSpec(proto.Message):
    r"""Describes a BigQuery table.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        table_source_type (google.cloud.datacatalog_v1.types.TableSourceType):
            Output only. The table source type.
        view_spec (google.cloud.datacatalog_v1.types.ViewSpec):
            Table view specification. Populated only if the
            ``table_source_type`` is ``BIGQUERY_VIEW``.

            This field is a member of `oneof`_ ``type_spec``.
        table_spec (google.cloud.datacatalog_v1.types.TableSpec):
            Specification of a BigQuery table. Populated only if the
            ``table_source_type`` is ``BIGQUERY_TABLE``.

            This field is a member of `oneof`_ ``type_spec``.
    """

    table_source_type: "TableSourceType" = proto.Field(
        proto.ENUM,
        number=1,
        enum="TableSourceType",
    )
    view_spec: "ViewSpec" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="type_spec",
        message="ViewSpec",
    )
    table_spec: "TableSpec" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="type_spec",
        message="TableSpec",
    )


class ViewSpec(proto.Message):
    r"""Table view specification.

    Attributes:
        view_query (str):
            Output only. The query that defines the table
            view.
    """

    view_query: str = proto.Field(
        proto.STRING,
        number=1,
    )


class TableSpec(proto.Message):
    r"""Normal BigQuery table specification.

    Attributes:
        grouped_entry (str):
            Output only. If the table is date-sharded, that is, it
            matches the ``[prefix]YYYYMMDD`` name pattern, this field is
            the Data Catalog resource name of the date-sharded grouped
            entry. For example:

            ``projects/{PROJECT_ID}/locations/{LOCATION}/entrygroups/{ENTRY_GROUP_ID}/entries/{ENTRY_ID}``.

            Otherwise, ``grouped_entry`` is empty.
    """

    grouped_entry: str = proto.Field(
        proto.STRING,
        number=1,
    )


class BigQueryDateShardedSpec(proto.Message):
    r"""Specification for a group of BigQuery tables with the
    ``[prefix]YYYYMMDD`` name pattern.

    For more information, see [Introduction to partitioned tables]
    (https://cloud.google.com/bigquery/docs/partitioned-tables#partitioning_versus_sharding).

    Attributes:
        dataset (str):
            Output only. The Data Catalog resource name of the dataset
            entry the current table belongs to. For example:

            ``projects/{PROJECT_ID}/locations/{LOCATION}/entrygroups/{ENTRY_GROUP_ID}/entries/{ENTRY_ID}``.
        table_prefix (str):
            Output only. The table name prefix of the shards.

            The name of any given shard is ``[table_prefix]YYYYMMDD``.
            For example, for the ``MyTable20180101`` shard, the
            ``table_prefix`` is ``MyTable``.
        shard_count (int):
            Output only. Total number of shards.
        latest_shard_resource (str):
            Output only. BigQuery resource name of the
            latest shard.
    """

    dataset: str = proto.Field(
        proto.STRING,
        number=1,
    )
    table_prefix: str = proto.Field(
        proto.STRING,
        number=2,
    )
    shard_count: int = proto.Field(
        proto.INT64,
        number=3,
    )
    latest_shard_resource: str = proto.Field(
        proto.STRING,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
