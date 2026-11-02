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
    package="google.cloud.bigquery.biglake.v1",
    manifest={
        "TableView",
        "Catalog",
        "Database",
        "Table",
        "CreateCatalogRequest",
        "DeleteCatalogRequest",
        "GetCatalogRequest",
        "ListCatalogsRequest",
        "ListCatalogsResponse",
        "CreateDatabaseRequest",
        "DeleteDatabaseRequest",
        "UpdateDatabaseRequest",
        "GetDatabaseRequest",
        "ListDatabasesRequest",
        "ListDatabasesResponse",
        "CreateTableRequest",
        "DeleteTableRequest",
        "UpdateTableRequest",
        "RenameTableRequest",
        "GetTableRequest",
        "ListTablesRequest",
        "ListTablesResponse",
        "HiveDatabaseOptions",
        "HiveTableOptions",
    },
)


class TableView(proto.Enum):
    r"""View on Table. Represents which fields will be populated for
    calls that return Table objects.

    Values:
        TABLE_VIEW_UNSPECIFIED (0):
            Default value. The API will default to the
            BASIC view.
        BASIC (1):
            Include only table names.
            This is the default value.
        FULL (2):
            Include everything.
    """

    TABLE_VIEW_UNSPECIFIED = 0
    BASIC = 1
    FULL = 2


class Catalog(proto.Message):
    r"""Catalog is the container of databases.

    Attributes:
        name (str):
            Output only. The resource name. Format:
            projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time of the
            catalog.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last modification time of
            the catalog.
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The deletion time of the
            catalog. Only set after the catalog is deleted.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when this catalog is
            considered expired. Only set after the catalog
            is deleted.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )


class Database(proto.Message):
    r"""Database is the container of tables.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        hive_options (google.cloud.bigquery_biglake_v1.types.HiveDatabaseOptions):
            Options of a Hive database.

            This field is a member of `oneof`_ ``options``.
        name (str):
            Output only. The resource name. Format:
            projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time of the
            database.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last modification time of
            the database.
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The deletion time of the
            database. Only set after the database is
            deleted.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when this database is
            considered expired. Only set after the database
            is deleted.
        type_ (google.cloud.bigquery_biglake_v1.types.Database.Type):
            The database type.
    """

    class Type(proto.Enum):
        r"""The database type.

        Values:
            TYPE_UNSPECIFIED (0):
                The type is not specified.
            HIVE (1):
                Represents a database storing tables
                compatible with Hive Metastore tables.
        """

        TYPE_UNSPECIFIED = 0
        HIVE = 1

    hive_options: "HiveDatabaseOptions" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="options",
        message="HiveDatabaseOptions",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=6,
        enum=Type,
    )


class Table(proto.Message):
    r"""Represents a table.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        hive_options (google.cloud.bigquery_biglake_v1.types.HiveTableOptions):
            Options of a Hive table.

            This field is a member of `oneof`_ ``options``.
        name (str):
            Output only. The resource name. Format:
            projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id}
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time of the table.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last modification time of
            the table.
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The deletion time of the table.
            Only set after the table is deleted.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when this table is
            considered expired. Only set after the table is
            deleted.
        type_ (google.cloud.bigquery_biglake_v1.types.Table.Type):
            The table type.
        etag (str):
            The checksum of a table object computed by
            the server based on the value of other fields.
            It may be sent on update requests to ensure the
            client has an up-to-date value before
            proceeding. It is only checked for update table
            operations.
    """

    class Type(proto.Enum):
        r"""The table type.

        Values:
            TYPE_UNSPECIFIED (0):
                The type is not specified.
            HIVE (1):
                Represents a table compatible with Hive
                Metastore tables.
        """

        TYPE_UNSPECIFIED = 0
        HIVE = 1

    hive_options: "HiveTableOptions" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="options",
        message="HiveTableOptions",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=6,
        enum=Type,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=8,
    )


class CreateCatalogRequest(proto.Message):
    r"""Request message for the CreateCatalog method.

    Attributes:
        parent (str):
            Required. The parent resource where this catalog will be
            created. Format:
            projects/{project_id_or_number}/locations/{location_id}
        catalog (google.cloud.bigquery_biglake_v1.types.Catalog):
            Required. The catalog to create. The ``name`` field does not
            need to be provided.
        catalog_id (str):
            Required. The ID to use for the catalog,
            which will become the final component of the
            catalog's resource name.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    catalog: "Catalog" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Catalog",
    )
    catalog_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteCatalogRequest(proto.Message):
    r"""Request message for the DeleteCatalog method.

    Attributes:
        name (str):
            Required. The name of the catalog to delete. Format:
            projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetCatalogRequest(proto.Message):
    r"""Request message for the GetCatalog method.

    Attributes:
        name (str):
            Required. The name of the catalog to retrieve. Format:
            projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListCatalogsRequest(proto.Message):
    r"""Request message for the ListCatalogs method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            catalogs. Format:
            projects/{project_id_or_number}/locations/{location_id}
        page_size (int):
            The maximum number of catalogs to return. The
            service may return fewer than this value.
            If unspecified, at most 50 catalogs will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            A page token, received from a previous ``ListCatalogs``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListCatalogs`` must match the call that provided the page
            token.
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


class ListCatalogsResponse(proto.Message):
    r"""Response message for the ListCatalogs method.

    Attributes:
        catalogs (MutableSequence[google.cloud.bigquery_biglake_v1.types.Catalog]):
            The catalogs from the specified project.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    catalogs: MutableSequence["Catalog"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Catalog",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateDatabaseRequest(proto.Message):
    r"""Request message for the CreateDatabase method.

    Attributes:
        parent (str):
            Required. The parent resource where this database will be
            created. Format:
            projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}
        database (google.cloud.bigquery_biglake_v1.types.Database):
            Required. The database to create. The ``name`` field does
            not need to be provided.
        database_id (str):
            Required. The ID to use for the database,
            which will become the final component of the
            database's resource name.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    database: "Database" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Database",
    )
    database_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteDatabaseRequest(proto.Message):
    r"""Request message for the DeleteDatabase method.

    Attributes:
        name (str):
            Required. The name of the database to delete. Format:
            projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateDatabaseRequest(proto.Message):
    r"""Request message for the UpdateDatabase method.

    Attributes:
        database (google.cloud.bigquery_biglake_v1.types.Database):
            Required. The database to update.

            The database's ``name`` field is used to identify the
            database to update. Format:
            projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to update.

            For the ``FieldMask`` definition, see
            https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask
            If not set, defaults to all of the fields that are allowed
            to update.
    """

    database: "Database" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Database",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetDatabaseRequest(proto.Message):
    r"""Request message for the GetDatabase method.

    Attributes:
        name (str):
            Required. The name of the database to retrieve. Format:
            projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDatabasesRequest(proto.Message):
    r"""Request message for the ListDatabases method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            databases. Format:
            projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}
        page_size (int):
            The maximum number of databases to return.
            The service may return fewer than this value. If
            unspecified, at most 50 databases will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            A page token, received from a previous ``ListDatabases``
            call. Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListDatabases`` must match the call that provided the page
            token.
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


class ListDatabasesResponse(proto.Message):
    r"""Response message for the ListDatabases method.

    Attributes:
        databases (MutableSequence[google.cloud.bigquery_biglake_v1.types.Database]):
            The databases from the specified catalog.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    databases: MutableSequence["Database"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Database",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateTableRequest(proto.Message):
    r"""Request message for the CreateTable method.

    Attributes:
        parent (str):
            Required. The parent resource where this table will be
            created. Format:
            projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}
        table (google.cloud.bigquery_biglake_v1.types.Table):
            Required. The table to create. The ``name`` field does not
            need to be provided for the table creation.
        table_id (str):
            Required. The ID to use for the table, which
            will become the final component of the table's
            resource name.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    table: "Table" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Table",
    )
    table_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteTableRequest(proto.Message):
    r"""Request message for the DeleteTable method.

    Attributes:
        name (str):
            Required. The name of the table to delete. Format:
            projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateTableRequest(proto.Message):
    r"""Request message for the UpdateTable method.

    Attributes:
        table (google.cloud.bigquery_biglake_v1.types.Table):
            Required. The table to update.

            The table's ``name`` field is used to identify the table to
            update. Format:
            projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id}
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to update.

            For the ``FieldMask`` definition, see
            https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask
            If not set, defaults to all of the fields that are allowed
            to update.
    """

    table: "Table" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Table",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class RenameTableRequest(proto.Message):
    r"""Request message for the RenameTable method in
    MetastoreService

    Attributes:
        name (str):
            Required. The table's ``name`` field is used to identify the
            table to rename. Format:
            projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id}
        new_name (str):
            Required. The new ``name`` for the specified table, must be
            in the same database. Format:
            projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    new_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetTableRequest(proto.Message):
    r"""Request message for the GetTable method.

    Attributes:
        name (str):
            Required. The name of the table to retrieve. Format:
            projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListTablesRequest(proto.Message):
    r"""Request message for the ListTables method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of tables.
            Format:
            projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}
        page_size (int):
            The maximum number of tables to return. The
            service may return fewer than this value.
            If unspecified, at most 50 tables will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            A page token, received from a previous ``ListTables`` call.
            Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListTables`` must match the call that provided the page
            token.
        view (google.cloud.bigquery_biglake_v1.types.TableView):
            The view for the returned tables.
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
    view: "TableView" = proto.Field(
        proto.ENUM,
        number=4,
        enum="TableView",
    )


class ListTablesResponse(proto.Message):
    r"""Response message for the ListTables method.

    Attributes:
        tables (MutableSequence[google.cloud.bigquery_biglake_v1.types.Table]):
            The tables from the specified database.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    tables: MutableSequence["Table"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Table",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class HiveDatabaseOptions(proto.Message):
    r"""Options of a Hive database.

    Attributes:
        location_uri (str):
            Cloud Storage folder URI where the database
            data is stored, starting with "gs://".
        parameters (MutableMapping[str, str]):
            Stores user supplied Hive database
            parameters.
    """

    location_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    parameters: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )


class HiveTableOptions(proto.Message):
    r"""Options of a Hive table.

    Attributes:
        parameters (MutableMapping[str, str]):
            Stores user supplied Hive table parameters.
        table_type (str):
            Hive table type. For example, MANAGED_TABLE, EXTERNAL_TABLE.
        storage_descriptor (google.cloud.bigquery_biglake_v1.types.HiveTableOptions.StorageDescriptor):
            Stores physical storage information of the
            data.
    """

    class SerDeInfo(proto.Message):
        r"""Serializer and deserializer information.

        Attributes:
            serialization_lib (str):
                The fully qualified Java class name of the
                serialization library.
        """

        serialization_lib: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class StorageDescriptor(proto.Message):
        r"""Stores physical storage information of the data.

        Attributes:
            location_uri (str):
                Cloud Storage folder URI where the table data
                is stored, starting with "gs://".
            input_format (str):
                The fully qualified Java class name of the
                input format.
            output_format (str):
                The fully qualified Java class name of the
                output format.
            serde_info (google.cloud.bigquery_biglake_v1.types.HiveTableOptions.SerDeInfo):
                Serializer and deserializer information.
        """

        location_uri: str = proto.Field(
            proto.STRING,
            number=1,
        )
        input_format: str = proto.Field(
            proto.STRING,
            number=2,
        )
        output_format: str = proto.Field(
            proto.STRING,
            number=3,
        )
        serde_info: "HiveTableOptions.SerDeInfo" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="HiveTableOptions.SerDeInfo",
        )

    parameters: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=1,
    )
    table_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    storage_descriptor: StorageDescriptor = proto.Field(
        proto.MESSAGE,
        number=3,
        message=StorageDescriptor,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
