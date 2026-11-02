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
    package="google.cloud.bigquery.migration.v2",
    manifest={
        "TranslationConfigDetails",
        "Dialect",
        "BigQueryDialect",
        "HiveQLDialect",
        "RedshiftDialect",
        "TeradataDialect",
        "OracleDialect",
        "SparkSQLDialect",
        "SnowflakeDialect",
        "NetezzaDialect",
        "AzureSynapseDialect",
        "VerticaDialect",
        "SQLServerDialect",
        "PostgresqlDialect",
        "PrestoDialect",
        "MySQLDialect",
        "DB2Dialect",
        "SQLiteDialect",
        "GreenplumDialect",
        "ObjectNameMappingList",
        "ObjectNameMapping",
        "NameMappingKey",
        "NameMappingValue",
        "SourceEnv",
    },
)


class TranslationConfigDetails(proto.Message):
    r"""The translation config to capture necessary settings for a
    translation task and subtask.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        gcs_source_path (str):
            The Cloud Storage path for a directory of
            files to translate in a task.

            This field is a member of `oneof`_ ``source_location``.
        gcs_target_path (str):
            The Cloud Storage path to write back the
            corresponding input files to.

            This field is a member of `oneof`_ ``target_location``.
        name_mapping_list (google.cloud.bigquery_migration_v2.types.ObjectNameMappingList):
            The mapping of objects to their desired
            output names in list form.

            This field is a member of `oneof`_ ``output_name_mapping``.
        source_dialect (google.cloud.bigquery_migration_v2.types.Dialect):
            The dialect of the input files.
        target_dialect (google.cloud.bigquery_migration_v2.types.Dialect):
            The target dialect for the engine to
            translate the input to.
        source_env (google.cloud.bigquery_migration_v2.types.SourceEnv):
            The default source environment values for the
            translation.
        request_source (str):
            The indicator to show translation request
            initiator.
        target_types (MutableSequence[str]):
            The types of output to generate, e.g. sql,
            metadata etc. If not specified, a default set of
            targets will be generated. Some additional
            target types may be slower to generate. See the
            documentation for the set of available target
            types.
    """

    gcs_source_path: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="source_location",
    )
    gcs_target_path: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="target_location",
    )
    name_mapping_list: "ObjectNameMappingList" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="output_name_mapping",
        message="ObjectNameMappingList",
    )
    source_dialect: "Dialect" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Dialect",
    )
    target_dialect: "Dialect" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="Dialect",
    )
    source_env: "SourceEnv" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="SourceEnv",
    )
    request_source: str = proto.Field(
        proto.STRING,
        number=8,
    )
    target_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=9,
    )


class Dialect(proto.Message):
    r"""The possible dialect options for translation.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        bigquery_dialect (google.cloud.bigquery_migration_v2.types.BigQueryDialect):
            The BigQuery dialect

            This field is a member of `oneof`_ ``dialect_value``.
        hiveql_dialect (google.cloud.bigquery_migration_v2.types.HiveQLDialect):
            The HiveQL dialect

            This field is a member of `oneof`_ ``dialect_value``.
        redshift_dialect (google.cloud.bigquery_migration_v2.types.RedshiftDialect):
            The Redshift dialect

            This field is a member of `oneof`_ ``dialect_value``.
        teradata_dialect (google.cloud.bigquery_migration_v2.types.TeradataDialect):
            The Teradata dialect

            This field is a member of `oneof`_ ``dialect_value``.
        oracle_dialect (google.cloud.bigquery_migration_v2.types.OracleDialect):
            The Oracle dialect

            This field is a member of `oneof`_ ``dialect_value``.
        sparksql_dialect (google.cloud.bigquery_migration_v2.types.SparkSQLDialect):
            The SparkSQL dialect

            This field is a member of `oneof`_ ``dialect_value``.
        snowflake_dialect (google.cloud.bigquery_migration_v2.types.SnowflakeDialect):
            The Snowflake dialect

            This field is a member of `oneof`_ ``dialect_value``.
        netezza_dialect (google.cloud.bigquery_migration_v2.types.NetezzaDialect):
            The Netezza dialect

            This field is a member of `oneof`_ ``dialect_value``.
        azure_synapse_dialect (google.cloud.bigquery_migration_v2.types.AzureSynapseDialect):
            The Azure Synapse dialect

            This field is a member of `oneof`_ ``dialect_value``.
        vertica_dialect (google.cloud.bigquery_migration_v2.types.VerticaDialect):
            The Vertica dialect

            This field is a member of `oneof`_ ``dialect_value``.
        sql_server_dialect (google.cloud.bigquery_migration_v2.types.SQLServerDialect):
            The SQL Server dialect

            This field is a member of `oneof`_ ``dialect_value``.
        postgresql_dialect (google.cloud.bigquery_migration_v2.types.PostgresqlDialect):
            The Postgresql dialect

            This field is a member of `oneof`_ ``dialect_value``.
        presto_dialect (google.cloud.bigquery_migration_v2.types.PrestoDialect):
            The Presto dialect

            This field is a member of `oneof`_ ``dialect_value``.
        mysql_dialect (google.cloud.bigquery_migration_v2.types.MySQLDialect):
            The MySQL dialect

            This field is a member of `oneof`_ ``dialect_value``.
        db2_dialect (google.cloud.bigquery_migration_v2.types.DB2Dialect):
            DB2 dialect

            This field is a member of `oneof`_ ``dialect_value``.
        sqlite_dialect (google.cloud.bigquery_migration_v2.types.SQLiteDialect):
            SQLite dialect

            This field is a member of `oneof`_ ``dialect_value``.
        greenplum_dialect (google.cloud.bigquery_migration_v2.types.GreenplumDialect):
            Greenplum dialect

            This field is a member of `oneof`_ ``dialect_value``.
    """

    bigquery_dialect: "BigQueryDialect" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="dialect_value",
        message="BigQueryDialect",
    )
    hiveql_dialect: "HiveQLDialect" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="dialect_value",
        message="HiveQLDialect",
    )
    redshift_dialect: "RedshiftDialect" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="dialect_value",
        message="RedshiftDialect",
    )
    teradata_dialect: "TeradataDialect" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="dialect_value",
        message="TeradataDialect",
    )
    oracle_dialect: "OracleDialect" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="dialect_value",
        message="OracleDialect",
    )
    sparksql_dialect: "SparkSQLDialect" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="dialect_value",
        message="SparkSQLDialect",
    )
    snowflake_dialect: "SnowflakeDialect" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="dialect_value",
        message="SnowflakeDialect",
    )
    netezza_dialect: "NetezzaDialect" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="dialect_value",
        message="NetezzaDialect",
    )
    azure_synapse_dialect: "AzureSynapseDialect" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="dialect_value",
        message="AzureSynapseDialect",
    )
    vertica_dialect: "VerticaDialect" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="dialect_value",
        message="VerticaDialect",
    )
    sql_server_dialect: "SQLServerDialect" = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="dialect_value",
        message="SQLServerDialect",
    )
    postgresql_dialect: "PostgresqlDialect" = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="dialect_value",
        message="PostgresqlDialect",
    )
    presto_dialect: "PrestoDialect" = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="dialect_value",
        message="PrestoDialect",
    )
    mysql_dialect: "MySQLDialect" = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="dialect_value",
        message="MySQLDialect",
    )
    db2_dialect: "DB2Dialect" = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof="dialect_value",
        message="DB2Dialect",
    )
    sqlite_dialect: "SQLiteDialect" = proto.Field(
        proto.MESSAGE,
        number=16,
        oneof="dialect_value",
        message="SQLiteDialect",
    )
    greenplum_dialect: "GreenplumDialect" = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="dialect_value",
        message="GreenplumDialect",
    )


class BigQueryDialect(proto.Message):
    r"""The dialect definition for BigQuery."""


class HiveQLDialect(proto.Message):
    r"""The dialect definition for HiveQL."""


class RedshiftDialect(proto.Message):
    r"""The dialect definition for Redshift."""


class TeradataDialect(proto.Message):
    r"""The dialect definition for Teradata.

    Attributes:
        mode (google.cloud.bigquery_migration_v2.types.TeradataDialect.Mode):
            Which Teradata sub-dialect mode the user
            specifies.
    """

    class Mode(proto.Enum):
        r"""The sub-dialect options for Teradata.

        Values:
            MODE_UNSPECIFIED (0):
                Unspecified mode.
            SQL (1):
                Teradata SQL mode.
            BTEQ (2):
                BTEQ mode (which includes SQL).
        """

        MODE_UNSPECIFIED = 0
        SQL = 1
        BTEQ = 2

    mode: Mode = proto.Field(
        proto.ENUM,
        number=1,
        enum=Mode,
    )


class OracleDialect(proto.Message):
    r"""The dialect definition for Oracle."""


class SparkSQLDialect(proto.Message):
    r"""The dialect definition for SparkSQL."""


class SnowflakeDialect(proto.Message):
    r"""The dialect definition for Snowflake."""


class NetezzaDialect(proto.Message):
    r"""The dialect definition for Netezza."""


class AzureSynapseDialect(proto.Message):
    r"""The dialect definition for Azure Synapse."""


class VerticaDialect(proto.Message):
    r"""The dialect definition for Vertica."""


class SQLServerDialect(proto.Message):
    r"""The dialect definition for SQL Server."""


class PostgresqlDialect(proto.Message):
    r"""The dialect definition for Postgresql."""


class PrestoDialect(proto.Message):
    r"""The dialect definition for Presto."""


class MySQLDialect(proto.Message):
    r"""The dialect definition for MySQL."""


class DB2Dialect(proto.Message):
    r"""The dialect definition for DB2."""


class SQLiteDialect(proto.Message):
    r"""The dialect definition for SQLite."""


class GreenplumDialect(proto.Message):
    r"""The dialect definition for Greenplum."""


class ObjectNameMappingList(proto.Message):
    r"""Represents a map of name mappings using a list of key:value
    proto messages of existing name to desired output name.

    Attributes:
        name_map (MutableSequence[google.cloud.bigquery_migration_v2.types.ObjectNameMapping]):
            The elements of the object name map.
    """

    name_map: MutableSequence["ObjectNameMapping"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ObjectNameMapping",
    )


class ObjectNameMapping(proto.Message):
    r"""Represents a key-value pair of NameMappingKey to
    NameMappingValue to represent the mapping of SQL names from the
    input value to desired output.

    Attributes:
        source (google.cloud.bigquery_migration_v2.types.NameMappingKey):
            The name of the object in source that is
            being mapped.
        target (google.cloud.bigquery_migration_v2.types.NameMappingValue):
            The desired target name of the object that is
            being mapped.
    """

    source: "NameMappingKey" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="NameMappingKey",
    )
    target: "NameMappingValue" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="NameMappingValue",
    )


class NameMappingKey(proto.Message):
    r"""The potential components of a full name mapping that will be
    mapped during translation in the source data warehouse.

    Attributes:
        type_ (google.cloud.bigquery_migration_v2.types.NameMappingKey.Type):
            The type of object that is being mapped.
        database (str):
            The database name (BigQuery project ID
            equivalent in the source data warehouse).
        schema (str):
            The schema name (BigQuery dataset equivalent
            in the source data warehouse).
        relation (str):
            The relation name (BigQuery table or view
            equivalent in the source data warehouse).
        attribute (str):
            The attribute name (BigQuery column
            equivalent in the source data warehouse).
    """

    class Type(proto.Enum):
        r"""The type of the object that is being mapped.

        Values:
            TYPE_UNSPECIFIED (0):
                Unspecified name mapping type.
            DATABASE (1):
                The object being mapped is a database.
            SCHEMA (2):
                The object being mapped is a schema.
            RELATION (3):
                The object being mapped is a relation.
            ATTRIBUTE (4):
                The object being mapped is an attribute.
            RELATION_ALIAS (5):
                The object being mapped is a relation alias.
            ATTRIBUTE_ALIAS (6):
                The object being mapped is a an attribute
                alias.
            FUNCTION (7):
                The object being mapped is a function.
        """

        TYPE_UNSPECIFIED = 0
        DATABASE = 1
        SCHEMA = 2
        RELATION = 3
        ATTRIBUTE = 4
        RELATION_ALIAS = 5
        ATTRIBUTE_ALIAS = 6
        FUNCTION = 7

    type_: Type = proto.Field(
        proto.ENUM,
        number=1,
        enum=Type,
    )
    database: str = proto.Field(
        proto.STRING,
        number=2,
    )
    schema: str = proto.Field(
        proto.STRING,
        number=3,
    )
    relation: str = proto.Field(
        proto.STRING,
        number=4,
    )
    attribute: str = proto.Field(
        proto.STRING,
        number=5,
    )


class NameMappingValue(proto.Message):
    r"""The potential components of a full name mapping that will be
    mapped during translation in the target data warehouse.

    Attributes:
        database (str):
            The database name (BigQuery project ID
            equivalent in the target data warehouse).
        schema (str):
            The schema name (BigQuery dataset equivalent
            in the target data warehouse).
        relation (str):
            The relation name (BigQuery table or view
            equivalent in the target data warehouse).
        attribute (str):
            The attribute name (BigQuery column
            equivalent in the target data warehouse).
    """

    database: str = proto.Field(
        proto.STRING,
        number=1,
    )
    schema: str = proto.Field(
        proto.STRING,
        number=2,
    )
    relation: str = proto.Field(
        proto.STRING,
        number=3,
    )
    attribute: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SourceEnv(proto.Message):
    r"""Represents the default source environment values for the
    translation.

    Attributes:
        default_database (str):
            The default database name to fully qualify
            SQL objects when their database name is missing.
        schema_search_path (MutableSequence[str]):
            The schema search path. When SQL objects are
            missing schema name, translation engine will
            search through this list to find the value.
        metadata_store_dataset (str):
            Optional. Expects a valid BigQuery dataset ID that exists,
            e.g., project-123.metadata_store_123. If specified,
            translation will search and read the required schema
            information from a metadata store in this dataset. If
            metadata store doesn't exist, translation will parse the
            metadata file and upload the schema info to a temp table in
            the dataset to speed up future translation jobs.
    """

    default_database: str = proto.Field(
        proto.STRING,
        number=1,
    )
    schema_search_path: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    metadata_store_dataset: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
