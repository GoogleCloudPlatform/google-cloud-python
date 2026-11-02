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
    package="google.cloud.biglake.hive.v1beta",
    manifest={
        "HiveCatalog",
        "CreateHiveCatalogRequest",
        "GetHiveCatalogRequest",
        "ListHiveCatalogsRequest",
        "ListHiveCatalogsResponse",
        "UpdateHiveCatalogRequest",
        "DeleteHiveCatalogRequest",
        "HiveDatabase",
        "CreateHiveDatabaseRequest",
        "GetHiveDatabaseRequest",
        "ListHiveDatabasesRequest",
        "ListHiveDatabasesResponse",
        "UpdateHiveDatabaseRequest",
        "DeleteHiveDatabaseRequest",
        "HiveTable",
        "FieldSchema",
        "StorageDescriptor",
        "SerdeInfo",
        "CreateHiveTableRequest",
        "GetHiveTableRequest",
        "ListHiveTablesRequest",
        "ListHiveTablesResponse",
        "UpdateHiveTableRequest",
        "DeleteHiveTableRequest",
        "Partition",
        "PartitionValues",
        "CreatePartitionRequest",
        "BatchCreatePartitionsRequest",
        "BatchCreatePartitionsResponse",
        "BatchDeletePartitionsRequest",
        "UpdatePartitionRequest",
        "BatchUpdatePartitionsRequest",
        "BatchUpdatePartitionsResponse",
        "ListPartitionsRequest",
        "ListPartitionsResponse",
        "FailoverHiveCatalogRequest",
        "FailoverHiveCatalogResponse",
    },
)


class HiveCatalog(proto.Message):
    r"""The HiveCatalog contains spark/hive databases and tables in
    the BigLake Metastore. While creating resources under a catalog,
    ideally ensure that the storage bucket location, spark / hive
    engine location or any other compute location  match. Catalog
    can be viewed as the destination for migrating an on-prem Hive
    metastore to GCP.

    Attributes:
        name (str):
            Identifier. The resource name. Format:
            projects/{project_id_or_number}/catalogs/{catalog_id}
        description (str):
            Optional. Stores the catalog description.
            The maximum length is 4000 characters.
        location_uri (str):
            Required. The Cloud Storage location path
            where the catalog exists. Format:
            gs://bucket/path/to/catalog The maximum length
            is 4000 characters.
        replicas (MutableSequence[google.cloud.biglake_hive_v1beta.types.HiveCatalog.Replica]):
            Output only. The replicas for the catalog
            metadata.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time of the
            catalog.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The update time of the catalog.
    """

    class Replica(proto.Message):
        r"""The replica of the Catalog.

        Attributes:
            region (str):
                Output only. The region of the replica. For example
                ``us-east1``.
            state (google.cloud.biglake_hive_v1beta.types.HiveCatalog.Replica.State):
                Output only. The current state of the
                replica.
        """

        class State(proto.Enum):
            r"""If the catalog is replicated to multiple regions, this enum
            describes the current state of the replica.

            Values:
                STATE_UNSPECIFIED (0):
                    The replica state is unknown.
                STATE_PRIMARY (1):
                    Indicates the replica is the writable
                    primary.
                STATE_PRIMARY_IN_PROGRESS (2):
                    Indicates the replica has been recently
                    assigned as the primary, but not all databases
                    are writeable yet.
                STATE_SECONDARY (3):
                    Indicates the replica is a read-only
                    secondary replica.
            """

            STATE_UNSPECIFIED = 0
            STATE_PRIMARY = 1
            STATE_PRIMARY_IN_PROGRESS = 2
            STATE_SECONDARY = 3

        region: str = proto.Field(
            proto.STRING,
            number=1,
        )
        state: "HiveCatalog.Replica.State" = proto.Field(
            proto.ENUM,
            number=2,
            enum="HiveCatalog.Replica.State",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )
    replicas: MutableSequence[Replica] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=Replica,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )


class CreateHiveCatalogRequest(proto.Message):
    r"""Request message for the CreateHiveCatalog method.

    Attributes:
        parent (str):
            Required. The parent resource where this catalog will be
            created. Format: projects/{project_id_or_number}
        hive_catalog (google.cloud.biglake_hive_v1beta.types.HiveCatalog):
            Required. The catalog to create. The ``name`` field does not
            need to be provided. Gets copied over from catalog_id.
        hive_catalog_id (str):
            Required. The Hive Catalog ID to use for the
            catalog that will become the final component of
            the catalog's resource name. The maximum length
            is 256 characters.
        primary_location (str):
            Required. The GCP region that specifies where
            the catalog metadata is stored, e.g.
            us-central1, EU, etc.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    hive_catalog: "HiveCatalog" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="HiveCatalog",
    )
    hive_catalog_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    primary_location: str = proto.Field(
        proto.STRING,
        number=4,
    )


class GetHiveCatalogRequest(proto.Message):
    r"""Request message for the GetHiveCatalog method.

    Attributes:
        name (str):
            Required. The name of the catalog to retrieve. Format:
            projects/{project_id_or_number}/catalogs/{catalog_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListHiveCatalogsRequest(proto.Message):
    r"""Request message for the ListHiveCatalogs method.

    Attributes:
        parent (str):
            Required. The project to list catalogs from. Format:
            projects/{project_id_or_number}
        page_size (int):
            Optional. Page size for pagination.
        page_token (str):
            Optional. Page token for pagination.
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


class ListHiveCatalogsResponse(proto.Message):
    r"""Response message for the ListHiveCatalogs method.

    Attributes:
        catalogs (MutableSequence[google.cloud.biglake_hive_v1beta.types.HiveCatalog]):
            Output only. The catalogs from the specified
            project.
        next_page_token (str):
            Output only. A token, which can be sent as ``page_token`` to
            retrieve the next page. If this field is omitted, there are
            no subsequent pages.
        unreachable (MutableSequence[str]):
            Output only. The list of unreachable cloud
            regions. If non-empty, the result set might be
            incomplete.
    """

    @property
    def raw_page(self):
        return self

    catalogs: MutableSequence["HiveCatalog"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="HiveCatalog",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class UpdateHiveCatalogRequest(proto.Message):
    r"""Request message for the UpdateHiveCatalog method.

    Attributes:
        hive_catalog (google.cloud.biglake_hive_v1beta.types.HiveCatalog):
            Required. The hive catalog to update. The name under the
            catalog is used to identify the catalog. Format:
            projects/{project_id_or_number}/catalogs/{catalog_id}
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.

            For the ``FieldMask`` definition, see
            https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask
            If not set, defaults to all of the fields that are allowed
            to update.
    """

    hive_catalog: "HiveCatalog" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="HiveCatalog",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteHiveCatalogRequest(proto.Message):
    r"""Request message for the DeleteHiveCatalog method.

    Attributes:
        name (str):
            Required. The name of the catalog to delete. Format:
            projects/{project_id_or_number}/catalogs/{catalog_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class HiveDatabase(proto.Message):
    r"""Stores the hive database information. It includes the
    database name, description, location and properties associated
    with the database.

    Attributes:
        name (str):
            Identifier. The resource name. Format:
            projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}
        description (str):
            Optional. Stores the database description.
            The maximum length is 4000 characters.
        location_uri (str):
            Optional. The Cloud Storage location path where the database
            exists. Format: ``gs://bucket/path/to/database`` If
            unspecified, the database will be stored in the catalog
            location. The maximum length is 4000 characters.
        parameters (MutableMapping[str, str]):
            Optional. Stores the properties associated
            with the database. The maximum size is 2 MiB.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time of the
            database.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The update time of the database.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )
    parameters: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )


class CreateHiveDatabaseRequest(proto.Message):
    r"""Request message for the CreateHiveDatabase method.

    Attributes:
        parent (str):
            Required. The parent resource where this database will be
            created. Format:
            projects/{project_id_or_number}/catalogs/{catalog_id}
        hive_database (google.cloud.biglake_hive_v1beta.types.HiveDatabase):
            Required. The database to create. The ``name`` field does
            not need to be provided.
        hive_database_id (str):
            Required. The ID to use for the Hive
            Database. The maximum length is 128 characters.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    hive_database: "HiveDatabase" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="HiveDatabase",
    )
    hive_database_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GetHiveDatabaseRequest(proto.Message):
    r"""Request message for the GetHiveDatabase method.

    Attributes:
        name (str):
            Required. The name of the database to retrieve. Format:
            projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListHiveDatabasesRequest(proto.Message):
    r"""Request message for the ListHiveDatabases method.

    Attributes:
        parent (str):
            Required. The hive catalog to list databases from. Format:
            projects/{project_id_or_number}/catalogs/{catalog_id}
        page_size (int):
            Optional. Page size for pagination.
        page_token (str):
            Optional. PageToken for pagination.
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


class ListHiveDatabasesResponse(proto.Message):
    r"""Response message for the ListHiveDatabases method.

    Attributes:
        databases (MutableSequence[google.cloud.biglake_hive_v1beta.types.HiveDatabase]):
            Output only. The databases from the specified
            project and catalog.
        next_page_token (str):
            Output only. A token, which can be sent as ``page_token`` to
            retrieve the next page. If this field is omitted, there are
            no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    databases: MutableSequence["HiveDatabase"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="HiveDatabase",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateHiveDatabaseRequest(proto.Message):
    r"""Request message for the UpdateHiveDatabase method.

    Attributes:
        hive_database (google.cloud.biglake_hive_v1beta.types.HiveDatabase):
            Required. The database to update.

            The database's ``name`` field is used to identify the
            database to update. Format:
            projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    hive_database: "HiveDatabase" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="HiveDatabase",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteHiveDatabaseRequest(proto.Message):
    r"""Request message for the DeleteHiveDatabase method.

    Attributes:
        name (str):
            Required. The name of the database to delete. Format:
            projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class HiveTable(proto.Message):
    r"""Stores the hive table information. It includes the table
    name, schema (column names and types), data location, storage
    format, serde info, etc. This message closely matches the Table
    object in the IMetastoreClient

    Attributes:
        name (str):
            Identifier. The resource name. Format:
            projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id}
        description (str):
            Optional. Description of the table. The
            maximum length is 4000 characters.
        storage_descriptor (google.cloud.biglake_hive_v1beta.types.StorageDescriptor):
            Required. Storage descriptor of the table.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time of the table.
        partition_keys (MutableSequence[google.cloud.biglake_hive_v1beta.types.FieldSchema]):
            Optional. The partition keys of the table.
        parameters (MutableMapping[str, str]):
            Optional. Stores the properties associated
            with the table. The maximum size is 4MiB.
        view_original_text (str):
            Optional. The original view text. Empty for
            non-view. The maximum size is 16MiB.
        view_expanded_text (str):
            Optional. The expanded view text. Empty for
            non-view. The maximum size is 16MiB.
        table_type (str):
            Output only. The type of the table. This is
            EXTERNAL for BigLake hive tables.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The update time of the table.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    storage_descriptor: "StorageDescriptor" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="StorageDescriptor",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    partition_keys: MutableSequence["FieldSchema"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="FieldSchema",
    )
    parameters: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )
    view_original_text: str = proto.Field(
        proto.STRING,
        number=9,
    )
    view_expanded_text: str = proto.Field(
        proto.STRING,
        number=10,
    )
    table_type: str = proto.Field(
        proto.STRING,
        number=11,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        message=timestamp_pb2.Timestamp,
    )


class FieldSchema(proto.Message):
    r"""Field schema information.

    Attributes:
        name (str):
            Required. Name of the field. The maximum
            length is 767 characters.
        type_ (str):
            Required. Type of the field. The maximum
            length is 128 characters.
        comment (str):
            Optional. Comment of the field. The maximum
            length is 256 characters.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=2,
    )
    comment: str = proto.Field(
        proto.STRING,
        number=3,
    )


class StorageDescriptor(proto.Message):
    r"""Contains information about the physical storage of the table
    data.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        columns (MutableSequence[google.cloud.biglake_hive_v1beta.types.FieldSchema]):
            Required. Specifies the columns of the table.
        location_uri (str):
            Optional. The Cloud storage uri where the table is located.
            Defaults to ``<database_location_uri>/<table_name>``. The
            maximum length is 4000 characters.
        input_format (str):
            Optional. The fully qualified Java class name
            of the input format. The maximum length is 4000
            characters.
        output_format (str):
            Optional. The fully qualified Java class name
            of the output format. The maximum length is 4000
            characters.
        compressed (bool):
            Optional. Whether the table is compressed.

            This field is a member of `oneof`_ ``_compressed``.
        num_buckets (int):
            Optional. The number of buckets in the table.

            This field is a member of `oneof`_ ``_num_buckets``.
        serde_info (google.cloud.biglake_hive_v1beta.types.SerdeInfo):
            Optional. Serialization and deserialization
            information.
        bucket_cols (MutableSequence[str]):
            Optional. Reducer grouping columns and
            clustering columns and bucketing columns
        sort_cols (MutableSequence[google.cloud.biglake_hive_v1beta.types.StorageDescriptor.Order]):
            Optional. Sort order of the data in each
            bucket
        parameters (MutableMapping[str, str]):
            Optional. Key-value pairs for the storage
            descriptor. The maximum size is 10Kib.
        skewed_info (google.cloud.biglake_hive_v1beta.types.StorageDescriptor.SkewedInfo):
            Optional. Table data skew information.
        stored_as_sub_dirs (bool):
            Optional. Whether the table is stored as sub
            directories.

            This field is a member of `oneof`_ ``_stored_as_sub_dirs``.
    """

    class Order(proto.Message):
        r"""Sort order of the stored data per column.

        Attributes:
            col (str):
                Required. The column name. The maximum length
                is 767 characters.
            order (int):
                Required. Defines the sort order of the
                column. Ascending if 1, descending if 0.
        """

        col: str = proto.Field(
            proto.STRING,
            number=1,
        )
        order: int = proto.Field(
            proto.INT32,
            number=2,
        )

    class SkewedInfo(proto.Message):
        r"""Stores all the information about skewed table.

        Attributes:
            skewed_col_names (MutableSequence[str]):
                Required. The column names that are skewed.
                The maximum length is 256 characters per column
                name.
            skewed_col_values (MutableSequence[google.cloud.biglake_hive_v1beta.types.StorageDescriptor.SkewedInfo.SkewedColumnValue]):
                Required. The skewed column values.
            skewed_key_values_locations (MutableSequence[google.cloud.biglake_hive_v1beta.types.StorageDescriptor.SkewedInfo.SkewedKeyValuesLocation]):
                Required. The skewed key values locations.
        """

        class SkewedColumnValue(proto.Message):
            r"""The skewed column values.

            Attributes:
                values (MutableSequence[str]):
                    Required. The skewed column values. The
                    maximum length is 256 characters per value.
            """

            values: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=1,
            )

        class SkewedKeyValuesLocation(proto.Message):
            r"""The skewed key values and their corresponding location.

            Attributes:
                values (MutableSequence[str]):
                    Required. The skewed column values. The
                    maximum length is 256 characters per value.
                location (str):
                    Required. The location of the skewed column
                    values. The maximum length is 4000 characters.
            """

            values: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=1,
            )
            location: str = proto.Field(
                proto.STRING,
                number=2,
            )

        skewed_col_names: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        skewed_col_values: MutableSequence[
            "StorageDescriptor.SkewedInfo.SkewedColumnValue"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="StorageDescriptor.SkewedInfo.SkewedColumnValue",
        )
        skewed_key_values_locations: MutableSequence[
            "StorageDescriptor.SkewedInfo.SkewedKeyValuesLocation"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="StorageDescriptor.SkewedInfo.SkewedKeyValuesLocation",
        )

    columns: MutableSequence["FieldSchema"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="FieldSchema",
    )
    location_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    input_format: str = proto.Field(
        proto.STRING,
        number=3,
    )
    output_format: str = proto.Field(
        proto.STRING,
        number=4,
    )
    compressed: bool = proto.Field(
        proto.BOOL,
        number=5,
        optional=True,
    )
    num_buckets: int = proto.Field(
        proto.INT32,
        number=6,
        optional=True,
    )
    serde_info: "SerdeInfo" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="SerdeInfo",
    )
    bucket_cols: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    sort_cols: MutableSequence[Order] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=Order,
    )
    parameters: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=10,
    )
    skewed_info: SkewedInfo = proto.Field(
        proto.MESSAGE,
        number=11,
        message=SkewedInfo,
    )
    stored_as_sub_dirs: bool = proto.Field(
        proto.BOOL,
        number=12,
        optional=True,
    )


class SerdeInfo(proto.Message):
    r"""Serialization and deserialization information.

    Attributes:
        name (str):
            Required. Name of the SerDe. Table name by
            default. The maximum length is 128 characters.
        serialization_lib (str):
            Required. The fully qualified Java class name
            of the serialization library. The maximum length
            is 4000 characters.
        description (str):
            Optional. Description of the serde. The
            maximum length is 4000 characters.
        parameters (MutableMapping[str, str]):
            Optional. Parameters of the serde. The
            maximum size is 10Kib.
        serializer_class (str):
            Optional. The fully qualified Java class name
            of the serializer. The maximum length is 4000
            characters.
        deserializer_class (str):
            Optional. The fully qualified Java class name
            of the deserializer. The maximum length is 4000
            characters.
        serde_type (google.cloud.biglake_hive_v1beta.types.SerdeInfo.SerdeType):
            Optional. The serde type.
    """

    class SerdeType(proto.Enum):
        r"""The serde types.

        Values:
            SERDE_TYPE_UNSPECIFIED (0):
                The serde type is not specified.
            HIVE (1):
                Hive.
            SCHEMA_REGISTRY (2):
                Schema registry.
        """

        SERDE_TYPE_UNSPECIFIED = 0
        HIVE = 1
        SCHEMA_REGISTRY = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    serialization_lib: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    parameters: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    serializer_class: str = proto.Field(
        proto.STRING,
        number=5,
    )
    deserializer_class: str = proto.Field(
        proto.STRING,
        number=6,
    )
    serde_type: SerdeType = proto.Field(
        proto.ENUM,
        number=7,
        enum=SerdeType,
    )


class CreateHiveTableRequest(proto.Message):
    r"""Request message for the CreateHiveTable method.

    Attributes:
        parent (str):
            Required. The parent resource for the table to be created.
            Format:
            projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}
        hive_table (google.cloud.biglake_hive_v1beta.types.HiveTable):
            Required. The Hive Table to create. The ``name`` field does
            not need to be provided.
        hive_table_id (str):
            Required. The Hive Table ID to use for the
            table that will become the final component of
            the table's resource name. The maximum length is
            256 characters.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    hive_table: "HiveTable" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="HiveTable",
    )
    hive_table_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GetHiveTableRequest(proto.Message):
    r"""Request message for the GetHiveTable method.

    Attributes:
        name (str):
            Required. The name of the table to retrieve. Format:
            projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListHiveTablesRequest(proto.Message):
    r"""Request message for the ListHiveTables method.

    Attributes:
        parent (str):
            Required. The database to list tables from. Format:
            projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}
        page_size (int):
            Optional. Page size for pagination.
        page_token (str):
            Optional. PageToken for pagination.
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


class ListHiveTablesResponse(proto.Message):
    r"""Response message for the ListHiveTables method.

    Attributes:
        tables (MutableSequence[google.cloud.biglake_hive_v1beta.types.HiveTable]):
            Output only. The tables from the specified
            project, catalog and database.
        next_page_token (str):
            Output only. A token, which can be sent as ``page_token`` to
            retrieve the next page. If this field is omitted, there are
            no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    tables: MutableSequence["HiveTable"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="HiveTable",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateHiveTableRequest(proto.Message):
    r"""Request message for the UpdateHiveTable method.

    Attributes:
        hive_table (google.cloud.biglake_hive_v1beta.types.HiveTable):
            Required. The table to update.

            The table's ``name`` field is used to identify the table to
            update. Format:
            projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id}
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    hive_table: "HiveTable" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="HiveTable",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteHiveTableRequest(proto.Message):
    r"""Request message for the DeleteHiveTable method.

    Attributes:
        name (str):
            Required. The name of the database to delete. Format:
            projects/{project_id_or_number}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Partition(proto.Message):
    r"""Information about a Hive partition.

    Attributes:
        values (MutableSequence[str]):
            Required. Represents the values of the
            partition keys, where each value corresponds to
            a specific partition key in the order in which
            the keys are defined. Each value is limited to
            1024 characters.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time of the
            partition.
        storage_descriptor (google.cloud.biglake_hive_v1beta.types.StorageDescriptor):
            Optional. Contains information about the
            physical storage of the data in the partition.
        parameters (MutableMapping[str, str]):
            Optional. Additional parameters or metadata
            associated with the partition. Maximum size 10
            KiB.
        fields (MutableSequence[google.cloud.biglake_hive_v1beta.types.FieldSchema]):
            Optional. List of columns.
    """

    values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    storage_descriptor: "StorageDescriptor" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="StorageDescriptor",
    )
    parameters: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    fields: MutableSequence["FieldSchema"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="FieldSchema",
    )


class PartitionValues(proto.Message):
    r"""Represents the values of a partition.

    Attributes:
        values (MutableSequence[str]):
            Required. The values of the partition keys,
            where each value corresponds to a specific
            partition key in the order in which the keys are
            defined.
    """

    values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class CreatePartitionRequest(proto.Message):
    r"""Request message for CreatePartition. The Partition is
    uniquely identified by values, which is an ordered list. Hence,
    there is no separate name or partition id field.

    Attributes:
        parent (str):
            Required. Reference to the table to where the
            partition to be added, in the format of
            projects/{project}/catalogs/{catalogs}/databases/{databases}/tables/{table}.
        partition (google.cloud.biglake_hive_v1beta.types.Partition):
            Required. The partition to be added.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    partition: "Partition" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Partition",
    )


class BatchCreatePartitionsRequest(proto.Message):
    r"""Request message for the BatchCreatePartitions method.

    Attributes:
        parent (str):
            Required. Reference to the table to where the
            partitions to be added, in the format of
            projects/{project}/catalogs/{catalogs}/databases/{database}/tables/{table}.
        requests (MutableSequence[google.cloud.biglake_hive_v1beta.types.CreatePartitionRequest]):
            Required. Requests to add partitions to the
            table.
        skip_existing_partitions (bool):
            Optional. Corresponds to the ``ifNotExists`` flag in the
            Hive Metastore APIs. If the flag is set to false, the server
            will return ALREADY_EXISTS if any partition already exists.
            If the flag is set to true, the server will skip existing
            partitions and insert only the non-existing partitions. A
            maximum of 900 partitions can be inserted in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreatePartitionRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreatePartitionRequest",
    )
    skip_existing_partitions: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class BatchCreatePartitionsResponse(proto.Message):
    r"""Response message for BatchCreatePartitions.

    Attributes:
        partitions (MutableSequence[google.cloud.biglake_hive_v1beta.types.Partition]):
            The list of partitions that have been added.
    """

    partitions: MutableSequence["Partition"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Partition",
    )


class BatchDeletePartitionsRequest(proto.Message):
    r"""Request message for BatchDeletePartitions. The Partition is
    uniquely identified by values, which is an ordered list. Hence,
    there is no separate name or partition id field.

    Attributes:
        parent (str):
            Required. Reference to the table to which
            these partitions belong, in the format of
            projects/{project}/catalogs/{catalogs}/databases/{database}/tables/{table}.
        partition_values (MutableSequence[google.cloud.biglake_hive_v1beta.types.PartitionValues]):
            Required. The list of partitions (identified
            by its values) to be deleted. A maximum of 900
            partitions can be deleted in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    partition_values: MutableSequence["PartitionValues"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="PartitionValues",
    )


class UpdatePartitionRequest(proto.Message):
    r"""Request message for UpdatePartition.

    Attributes:
        partition (google.cloud.biglake_hive_v1beta.types.Partition):
            Required. The partition to be updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    partition: "Partition" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Partition",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdatePartitionsRequest(proto.Message):
    r"""Request message for BatchUpdatePartitions.

    Attributes:
        parent (str):
            Required. Reference to the table to which
            these partitions belong, in the format of
            projects/{project}/catalogs/{catalogs}/databases/{database}/tables/{table}.
        requests (MutableSequence[google.cloud.biglake_hive_v1beta.types.UpdatePartitionRequest]):
            Required. Requests to update partitions in
            the table.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdatePartitionRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdatePartitionRequest",
    )


class BatchUpdatePartitionsResponse(proto.Message):
    r"""Response message for BatchUpdatePartitions.

    Attributes:
        partitions (MutableSequence[google.cloud.biglake_hive_v1beta.types.Partition]):
            The list of partitions that have been
            updated. A maximum of 900 partitions can be
            updated in a batch.
    """

    partitions: MutableSequence["Partition"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Partition",
    )


class ListPartitionsRequest(proto.Message):
    r"""Request message for ListPartitions.

    Attributes:
        parent (str):
            Required. Reference to the table to which
            these partitions belong, in the format of
            projects/{project}/catalogs/{catalogs}/databases/{database}/tables/{table}.
        filter (str):
            Optional. SQL text filtering statement, similar to a
            ``WHERE`` clause in a query. Only supports single-row
            expressions. Aggregate functions are not supported.

            Examples:

            - ``"int_field > 5"``
            - ``"date_field = CAST('2014-9-27' as DATE)"``
            - ``"nullable_field is not NULL"``
            - ``"st_equals(geo_field, st_geofromtext("POINT(2, 2)"))"``
            - ``"numeric_field BETWEEN 1.0 AND 5.0"``

            Restricted to a maximum length of 1 MB.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListPartitionsResponse(proto.Message):
    r"""Response message for ListPartitions.

    Attributes:
        partitions (MutableSequence[google.cloud.biglake_hive_v1beta.types.Partition]):
            Output only. List of partitions.
    """

    partitions: MutableSequence["Partition"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Partition",
    )


class FailoverHiveCatalogRequest(proto.Message):
    r"""Request message for FailoverHiveCatalog.

    Attributes:
        name (str):
            Required. The name of the catalog in the form
            "projects/{project_id}/catalogs/{catalog_id}".
        primary_replica (str):
            Required. The region being assigned as the
            new primary replica region. For example
            "us-east1". This must be one of the replica
            regions in the catalog's list of replicas marked
            as a "secondary".
        validate_only (bool):
            Optional. If set, only validate the request, but do not
            perform the update. This can be used to inspect the
            replication_time at any time, including before performing a
            fail-over.
        conditional_failover_replication_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. If unset, wait for all data from
            the source region to replicate to the new
            primary region before completing the failover,
            with no data loss (also called "soft failover").
            If set, failover immediately, accepting the loss
            of any data committed in the source region after
            this timestamp, that has not yet replicated. If
            any data committed before this time has not
            replicated, the failover will not be performed
            and an error will be returned (also called "hard
            failover").
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    primary_replica: str = proto.Field(
        proto.STRING,
        number=2,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    conditional_failover_replication_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class FailoverHiveCatalogResponse(proto.Message):
    r"""Response message for FailoverHiveCatalog.

    Attributes:
        replication_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The min timestamp for which all namespaces and
            table metadata have been replicated in the region specified
            as the new primary_replica. Some resources may have been
            replicated more recently than this timestamp. If empty, the
            replica has just been created and has not yet been fully
            initialized.
    """

    replication_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
