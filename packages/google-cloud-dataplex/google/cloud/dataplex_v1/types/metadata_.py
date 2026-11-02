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
    package="google.cloud.dataplex.v1",
    manifest={
        "StorageSystem",
        "CreateEntityRequest",
        "UpdateEntityRequest",
        "DeleteEntityRequest",
        "ListEntitiesRequest",
        "ListEntitiesResponse",
        "GetEntityRequest",
        "ListPartitionsRequest",
        "CreatePartitionRequest",
        "DeletePartitionRequest",
        "ListPartitionsResponse",
        "GetPartitionRequest",
        "Entity",
        "Partition",
        "Schema",
        "StorageFormat",
        "StorageAccess",
    },
)


class StorageSystem(proto.Enum):
    r"""Identifies the cloud system that manages the data storage.

    Values:
        STORAGE_SYSTEM_UNSPECIFIED (0):
            Storage system unspecified.
        CLOUD_STORAGE (1):
            The entity data is contained within a Cloud
            Storage bucket.
        BIGQUERY (2):
            The entity data is contained within a
            BigQuery dataset.
    """

    STORAGE_SYSTEM_UNSPECIFIED = 0
    CLOUD_STORAGE = 1
    BIGQUERY = 2


class CreateEntityRequest(proto.Message):
    r"""Create a metadata entity request.

    Attributes:
        parent (str):
            Required. The resource name of the parent zone:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}``.
        entity (google.cloud.dataplex_v1.types.Entity):
            Required. Entity resource.
        validate_only (bool):
            Optional. Only validate the request, but do
            not perform mutations. The default is false.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    entity: "Entity" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Entity",
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class UpdateEntityRequest(proto.Message):
    r"""Update a metadata entity request.
    The exiting entity will be fully replaced by the entity in the
    request. The entity ID is mutable. To modify the ID, use the
    current entity ID in the request URL and specify the new ID in
    the request body.

    Attributes:
        entity (google.cloud.dataplex_v1.types.Entity):
            Required. Update description.
        validate_only (bool):
            Optional. Only validate the request, but do
            not perform mutations. The default is false.
    """

    entity: "Entity" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Entity",
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class DeleteEntityRequest(proto.Message):
    r"""Delete a metadata entity request.

    Attributes:
        name (str):
            Required. The resource name of the entity:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/entities/{entity_id}``.
        etag (str):
            Required. The etag associated with the entity, which can be
            retrieved with a [GetEntity][] request.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListEntitiesRequest(proto.Message):
    r"""List metadata entities request.

    Attributes:
        parent (str):
            Required. The resource name of the parent zone:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}``.
        view (google.cloud.dataplex_v1.types.ListEntitiesRequest.EntityView):
            Required. Specify the entity view to make a
            partial list request.
        page_size (int):
            Optional. Maximum number of entities to
            return. The service may return fewer than this
            value. If unspecified, 100 entities will be
            returned by default. The maximum value is 500;
            larger values will will be truncated to 500.
        page_token (str):
            Optional. Page token received from a previous
            ``ListEntities`` call. Provide this to retrieve the
            subsequent page. When paginating, all other parameters
            provided to ``ListEntities`` must match the call that
            provided the page token.
        filter (str):
            Optional. The following filter parameters can be added to
            the URL to limit the entities returned by the API:

            - Entity ID: ?filter="id=entityID"
            - Asset ID: ?filter="asset=assetID"
            - Data path ?filter="data_path=gs://my-bucket"
            - Is HIVE compatible: ?filter="hive_compatible=true"
            - Is BigQuery compatible: ?filter="bigquery_compatible=true".
    """

    class EntityView(proto.Enum):
        r"""Entity views.

        Values:
            ENTITY_VIEW_UNSPECIFIED (0):
                The default unset value. Return both table
                and fileset entities if unspecified.
            TABLES (1):
                Only list table entities.
            FILESETS (2):
                Only list fileset entities.
        """

        ENTITY_VIEW_UNSPECIFIED = 0
        TABLES = 1
        FILESETS = 2

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: EntityView = proto.Field(
        proto.ENUM,
        number=2,
        enum=EntityView,
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


class ListEntitiesResponse(proto.Message):
    r"""List metadata entities response.

    Attributes:
        entities (MutableSequence[google.cloud.dataplex_v1.types.Entity]):
            Entities in the specified parent zone.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no remaining results in
            the list.
    """

    @property
    def raw_page(self):
        return self

    entities: MutableSequence["Entity"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Entity",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetEntityRequest(proto.Message):
    r"""Get metadata entity request.

    Attributes:
        name (str):
            Required. The resource name of the entity:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/entities/{entity_id}.``
        view (google.cloud.dataplex_v1.types.GetEntityRequest.EntityView):
            Optional. Used to select the subset of entity information to
            return. Defaults to ``BASIC``.
    """

    class EntityView(proto.Enum):
        r"""Entity views for get entity partial result.

        Values:
            ENTITY_VIEW_UNSPECIFIED (0):
                The API will default to the ``BASIC`` view.
            BASIC (1):
                Minimal view that does not include the
                schema.
            SCHEMA (2):
                Include basic information and schema.
            FULL (4):
                Include everything. Currently, this is the
                same as the SCHEMA view.
        """

        ENTITY_VIEW_UNSPECIFIED = 0
        BASIC = 1
        SCHEMA = 2
        FULL = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: EntityView = proto.Field(
        proto.ENUM,
        number=2,
        enum=EntityView,
    )


class ListPartitionsRequest(proto.Message):
    r"""List metadata partitions request.

    Attributes:
        parent (str):
            Required. The resource name of the parent entity:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/entities/{entity_id}``.
        page_size (int):
            Optional. Maximum number of partitions to
            return. The service may return fewer than this
            value. If unspecified, 100 partitions will be
            returned by default. The maximum page size is
            500; larger values will will be truncated to
            500.
        page_token (str):
            Optional. Page token received from a previous
            ``ListPartitions`` call. Provide this to retrieve the
            subsequent page. When paginating, all other parameters
            provided to ``ListPartitions`` must match the call that
            provided the page token.
        filter (str):
            Optional. Filter the partitions returned to the caller using
            a key value pair expression. Supported operators and syntax:

            - logic operators: AND, OR
            - comparison operators: <, >, >=, <= ,=, !=
            - LIKE operators:

              - The right hand of a LIKE operator supports "." and "\*"
                for wildcard searches, for example "value1 LIKE
                ".\ *oo.*"

            - parenthetical grouping: ( )

            Sample filter expression: \`?filter="key1 < value1 OR key2 >
            value2"

            **Notes:**

            - Keys to the left of operators are case insensitive.
            - Partition results are sorted first by creation time, then
              by lexicographic order.
            - Up to 20 key value filter pairs are allowed, but due to
              performance considerations, only the first 10 will be used
              as a filter.
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


class CreatePartitionRequest(proto.Message):
    r"""Create metadata partition request.

    Attributes:
        parent (str):
            Required. The resource name of the parent zone:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/entities/{entity_id}``.
        partition (google.cloud.dataplex_v1.types.Partition):
            Required. Partition resource.
        validate_only (bool):
            Optional. Only validate the request, but do
            not perform mutations. The default is false.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    partition: "Partition" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Partition",
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class DeletePartitionRequest(proto.Message):
    r"""Delete metadata partition request.

    Attributes:
        name (str):
            Required. The resource name of the partition. format:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/entities/{entity_id}/partitions/{partition_value_path}``.
            The {partition_value_path} segment consists of an ordered
            sequence of partition values separated by "/". All values
            must be provided.
        etag (str):
            Optional. The etag associated with the
            partition.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListPartitionsResponse(proto.Message):
    r"""List metadata partitions response.

    Attributes:
        partitions (MutableSequence[google.cloud.dataplex_v1.types.Partition]):
            Partitions under the specified parent entity.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no remaining results in
            the list.
    """

    @property
    def raw_page(self):
        return self

    partitions: MutableSequence["Partition"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Partition",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetPartitionRequest(proto.Message):
    r"""Get metadata partition request.

    Attributes:
        name (str):
            Required. The resource name of the partition:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/entities/{entity_id}/partitions/{partition_value_path}``.
            The {partition_value_path} segment consists of an ordered
            sequence of partition values separated by "/". All values
            must be provided.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Entity(proto.Message):
    r"""Represents tables and fileset metadata contained within a
    zone.

    Attributes:
        name (str):
            Output only. The resource name of the entity, of the form:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/entities/{id}``.
        display_name (str):
            Optional. Display name must be shorter than
            or equal to 256 characters.
        description (str):
            Optional. User friendly longer description
            text. Must be shorter than or equal to 1024
            characters.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the entity was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the entity was
            last updated.
        id (str):
            Required. A user-provided entity ID. It is
            mutable, and will be used as the published table
            name. Specifying a new ID in an update entity
            request will override the existing value.
            The ID must contain only letters (a-z, A-Z),
            numbers (0-9), and underscores, and consist of
            256 or fewer characters.
        etag (str):
            Optional. The etag associated with the entity, which can be
            retrieved with a [GetEntity][] request. Required for update
            and delete requests.
        type_ (google.cloud.dataplex_v1.types.Entity.Type):
            Required. Immutable. The type of entity.
        asset (str):
            Required. Immutable. The ID of the asset
            associated with the storage location containing
            the entity data. The entity must be with in the
            same zone with the asset.
        data_path (str):
            Required. Immutable. The storage path of the entity data.
            For Cloud Storage data, this is the fully-qualified path to
            the entity, such as ``gs://bucket/path/to/data``. For
            BigQuery data, this is the name of the table resource, such
            as
            ``projects/project_id/datasets/dataset_id/tables/table_id``.
        data_path_pattern (str):
            Optional. The set of items within the data path constituting
            the data in the entity, represented as a glob path. Example:
            ``gs://bucket/path/to/data/**/*.csv``.
        catalog_entry (str):
            Output only. The name of the associated Data
            Catalog entry.
        system (google.cloud.dataplex_v1.types.StorageSystem):
            Required. Immutable. Identifies the storage
            system of the entity data.
        format_ (google.cloud.dataplex_v1.types.StorageFormat):
            Required. Identifies the storage format of
            the entity data. It does not apply to entities
            with data stored in BigQuery.
        compatibility (google.cloud.dataplex_v1.types.Entity.CompatibilityStatus):
            Output only. Metadata stores that the entity
            is compatible with.
        access (google.cloud.dataplex_v1.types.StorageAccess):
            Output only. Identifies the access mechanism
            to the entity. Not user settable.
        uid (str):
            Output only. System generated unique ID for
            the Entity. This ID will be different if the
            Entity is deleted and re-created with the same
            name.
        schema (google.cloud.dataplex_v1.types.Schema):
            Required. The description of the data structure and layout.
            The schema is not included in list responses. It is only
            included in ``SCHEMA`` and ``FULL`` entity views of a
            ``GetEntity`` response.
    """

    class Type(proto.Enum):
        r"""The type of entity.

        Values:
            TYPE_UNSPECIFIED (0):
                Type unspecified.
            TABLE (1):
                Structured and semi-structured data.
            FILESET (2):
                Unstructured data.
        """

        TYPE_UNSPECIFIED = 0
        TABLE = 1
        FILESET = 2

    class CompatibilityStatus(proto.Message):
        r"""Provides compatibility information for various metadata
        stores.

        Attributes:
            hive_metastore (google.cloud.dataplex_v1.types.Entity.CompatibilityStatus.Compatibility):
                Output only. Whether this entity is
                compatible with Hive Metastore.
            bigquery (google.cloud.dataplex_v1.types.Entity.CompatibilityStatus.Compatibility):
                Output only. Whether this entity is
                compatible with BigQuery.
        """

        class Compatibility(proto.Message):
            r"""Provides compatibility information for a specific metadata
            store.

            Attributes:
                compatible (bool):
                    Output only. Whether the entity is compatible
                    and can be represented in the metadata store.
                reason (str):
                    Output only. Provides additional detail if
                    the entity is incompatible with the metadata
                    store.
            """

            compatible: bool = proto.Field(
                proto.BOOL,
                number=1,
            )
            reason: str = proto.Field(
                proto.STRING,
                number=2,
            )

        hive_metastore: "Entity.CompatibilityStatus.Compatibility" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="Entity.CompatibilityStatus.Compatibility",
        )
        bigquery: "Entity.CompatibilityStatus.Compatibility" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="Entity.CompatibilityStatus.Compatibility",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
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
    id: str = proto.Field(
        proto.STRING,
        number=7,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=8,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=10,
        enum=Type,
    )
    asset: str = proto.Field(
        proto.STRING,
        number=11,
    )
    data_path: str = proto.Field(
        proto.STRING,
        number=12,
    )
    data_path_pattern: str = proto.Field(
        proto.STRING,
        number=13,
    )
    catalog_entry: str = proto.Field(
        proto.STRING,
        number=14,
    )
    system: "StorageSystem" = proto.Field(
        proto.ENUM,
        number=15,
        enum="StorageSystem",
    )
    format_: "StorageFormat" = proto.Field(
        proto.MESSAGE,
        number=16,
        message="StorageFormat",
    )
    compatibility: CompatibilityStatus = proto.Field(
        proto.MESSAGE,
        number=19,
        message=CompatibilityStatus,
    )
    access: "StorageAccess" = proto.Field(
        proto.MESSAGE,
        number=21,
        message="StorageAccess",
    )
    uid: str = proto.Field(
        proto.STRING,
        number=22,
    )
    schema: "Schema" = proto.Field(
        proto.MESSAGE,
        number=50,
        message="Schema",
    )


class Partition(proto.Message):
    r"""Represents partition metadata contained within entity
    instances.

    Attributes:
        name (str):
            Output only. Partition values used in the HTTP URL must be
            double encoded. For example,
            ``url_encode(url_encode(value))`` can be used to encode
            "US:CA/CA#Sunnyvale so that the request URL ends with
            "/partitions/US%253ACA/CA%2523Sunnyvale". The name field in
            the response retains the encoded format.
        values (MutableSequence[str]):
            Required. Immutable. The set of values
            representing the partition, which correspond to
            the partition schema defined in the parent
            entity.
        location (str):
            Required. Immutable. The location of the entity data within
            the partition, for example,
            ``gs://bucket/path/to/entity/key1=value1/key2=value2``. Or
            ``projects/<project_id>/datasets/<dataset_id>/tables/<table_id>``
        etag (str):
            Optional. The etag for this partition.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=4,
    )


class Schema(proto.Message):
    r"""Schema information describing the structure and layout of the
    data.

    Attributes:
        user_managed (bool):
            Required. Set to ``true`` if user-managed or ``false`` if
            managed by Dataplex Universal Catalog. The default is
            ``false`` (managed by Dataplex Universal Catalog).

            - Set to ``false``\ to enable Dataplex Universal Catalog
              discovery to update the schema. including new data
              discovery, schema inference, and schema evolution. Users
              retain the ability to input and edit the schema. Dataplex
              Universal Catalog treats schema input by the user as
              though produced by a previous Dataplex Universal Catalog
              discovery operation, and it will evolve the schema and
              take action based on that treatment.

            - Set to ``true`` to fully manage the entity schema. This
              setting guarantees that Dataplex Universal Catalog will
              not change schema fields.
        fields (MutableSequence[google.cloud.dataplex_v1.types.Schema.SchemaField]):
            Optional. The sequence of fields describing data in table
            entities. **Note:** BigQuery SchemaFields are immutable.
        partition_fields (MutableSequence[google.cloud.dataplex_v1.types.Schema.PartitionField]):
            Optional. The sequence of fields describing
            the partition structure in entities. If this
            field is empty, there are no partitions within
            the data.
        partition_style (google.cloud.dataplex_v1.types.Schema.PartitionStyle):
            Optional. The structure of paths containing
            partition data within the entity.
    """

    class Type(proto.Enum):
        r"""Type information for fields in schemas and partition schemas.

        Values:
            TYPE_UNSPECIFIED (0):
                SchemaType unspecified.
            BOOLEAN (1):
                Boolean field.
            BYTE (2):
                Single byte numeric field.
            INT16 (3):
                16-bit numeric field.
            INT32 (4):
                32-bit numeric field.
            INT64 (5):
                64-bit numeric field.
            FLOAT (6):
                Floating point numeric field.
            DOUBLE (7):
                Double precision numeric field.
            DECIMAL (8):
                Real value numeric field.
            STRING (9):
                Sequence of characters field.
            BINARY (10):
                Sequence of bytes field.
            TIMESTAMP (11):
                Date and time field.
            DATE (12):
                Date field.
            TIME (13):
                Time field.
            RECORD (14):
                Structured field. Nested fields that define
                the structure of the map. If all nested fields
                are nullable, this field represents a union.
            NULL (100):
                Null field that does not have values.
        """

        TYPE_UNSPECIFIED = 0
        BOOLEAN = 1
        BYTE = 2
        INT16 = 3
        INT32 = 4
        INT64 = 5
        FLOAT = 6
        DOUBLE = 7
        DECIMAL = 8
        STRING = 9
        BINARY = 10
        TIMESTAMP = 11
        DATE = 12
        TIME = 13
        RECORD = 14
        NULL = 100

    class Mode(proto.Enum):
        r"""Additional qualifiers to define field semantics.

        Values:
            MODE_UNSPECIFIED (0):
                Mode unspecified.
            REQUIRED (1):
                The field has required semantics.
            NULLABLE (2):
                The field has optional semantics, and may be
                null.
            REPEATED (3):
                The field has repeated (0 or more) semantics,
                and is a list of values.
        """

        MODE_UNSPECIFIED = 0
        REQUIRED = 1
        NULLABLE = 2
        REPEATED = 3

    class PartitionStyle(proto.Enum):
        r"""The structure of paths within the entity, which represent
        partitions.

        Values:
            PARTITION_STYLE_UNSPECIFIED (0):
                PartitionStyle unspecified
            HIVE_COMPATIBLE (1):
                Partitions are hive-compatible. Examples:
                ``gs://bucket/path/to/table/dt=2019-10-31/lang=en``,
                ``gs://bucket/path/to/table/dt=2019-10-31/lang=en/late``.
        """

        PARTITION_STYLE_UNSPECIFIED = 0
        HIVE_COMPATIBLE = 1

    class SchemaField(proto.Message):
        r"""Represents a column field within a table schema.

        Attributes:
            name (str):
                Required. The name of the field. Must contain
                only letters, numbers and underscores, with a
                maximum length of 767 characters, and must begin
                with a letter or underscore.
            description (str):
                Optional. User friendly field description.
                Must be less than or equal to 1024 characters.
            type_ (google.cloud.dataplex_v1.types.Schema.Type):
                Required. The type of field.
            mode (google.cloud.dataplex_v1.types.Schema.Mode):
                Required. Additional field semantics.
            fields (MutableSequence[google.cloud.dataplex_v1.types.Schema.SchemaField]):
                Optional. Any nested field for complex types.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        description: str = proto.Field(
            proto.STRING,
            number=2,
        )
        type_: "Schema.Type" = proto.Field(
            proto.ENUM,
            number=3,
            enum="Schema.Type",
        )
        mode: "Schema.Mode" = proto.Field(
            proto.ENUM,
            number=4,
            enum="Schema.Mode",
        )
        fields: MutableSequence["Schema.SchemaField"] = proto.RepeatedField(
            proto.MESSAGE,
            number=10,
            message="Schema.SchemaField",
        )

    class PartitionField(proto.Message):
        r"""Represents a key field within the entity's partition structure. You
        could have up to 20 partition fields, but only the first 10
        partitions have the filtering ability due to performance
        consideration. **Note:** Partition fields are immutable.

        Attributes:
            name (str):
                Required. Partition field name must consist
                of letters, numbers, and underscores only, with
                a maximum of length of 256 characters, and must
                begin with a letter or underscore..
            type_ (google.cloud.dataplex_v1.types.Schema.Type):
                Required. Immutable. The type of field.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        type_: "Schema.Type" = proto.Field(
            proto.ENUM,
            number=2,
            enum="Schema.Type",
        )

    user_managed: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    fields: MutableSequence[SchemaField] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=SchemaField,
    )
    partition_fields: MutableSequence[PartitionField] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=PartitionField,
    )
    partition_style: PartitionStyle = proto.Field(
        proto.ENUM,
        number=4,
        enum=PartitionStyle,
    )


class StorageFormat(proto.Message):
    r"""Describes the format of the data within its storage location.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        format_ (google.cloud.dataplex_v1.types.StorageFormat.Format):
            Output only. The data format associated with
            the stored data, which represents content type
            values. The value is inferred from mime type.
        compression_format (google.cloud.dataplex_v1.types.StorageFormat.CompressionFormat):
            Optional. The compression type associated
            with the stored data. If unspecified, the data
            is uncompressed.
        mime_type (str):
            Required. The mime type descriptor for the
            data. Must match the pattern {type}/{subtype}.
            Supported values:

            - application/x-parquet
            - application/x-avro
            - application/x-orc
            - application/x-tfrecord
            - application/x-parquet+iceberg
            - application/x-avro+iceberg
            - application/x-orc+iceberg
            - application/json
            - application/{subtypes}
            - text/csv
            - text/<subtypes>
            - image/{image subtype}
            - video/{video subtype}
            - audio/{audio subtype}
        csv (google.cloud.dataplex_v1.types.StorageFormat.CsvOptions):
            Optional. Additional information about CSV
            formatted data.

            This field is a member of `oneof`_ ``options``.
        json (google.cloud.dataplex_v1.types.StorageFormat.JsonOptions):
            Optional. Additional information about CSV
            formatted data.

            This field is a member of `oneof`_ ``options``.
        iceberg (google.cloud.dataplex_v1.types.StorageFormat.IcebergOptions):
            Optional. Additional information about
            iceberg tables.

            This field is a member of `oneof`_ ``options``.
    """

    class Format(proto.Enum):
        r"""The specific file format of the data.

        Values:
            FORMAT_UNSPECIFIED (0):
                Format unspecified.
            PARQUET (1):
                Parquet-formatted structured data.
            AVRO (2):
                Avro-formatted structured data.
            ORC (3):
                Orc-formatted structured data.
            CSV (100):
                Csv-formatted semi-structured data.
            JSON (101):
                Json-formatted semi-structured data.
            IMAGE (200):
                Image data formats (such as jpg and png).
            AUDIO (201):
                Audio data formats (such as mp3, and wav).
            VIDEO (202):
                Video data formats (such as mp4 and mpg).
            TEXT (203):
                Textual data formats (such as txt and xml).
            TFRECORD (204):
                TensorFlow record format.
            OTHER (1000):
                Data that doesn't match a specific format.
            UNKNOWN (1001):
                Data of an unknown format.
        """

        FORMAT_UNSPECIFIED = 0
        PARQUET = 1
        AVRO = 2
        ORC = 3
        CSV = 100
        JSON = 101
        IMAGE = 200
        AUDIO = 201
        VIDEO = 202
        TEXT = 203
        TFRECORD = 204
        OTHER = 1000
        UNKNOWN = 1001

    class CompressionFormat(proto.Enum):
        r"""The specific compressed file format of the data.

        Values:
            COMPRESSION_FORMAT_UNSPECIFIED (0):
                CompressionFormat unspecified. Implies
                uncompressed data.
            GZIP (2):
                GZip compressed set of files.
            BZIP2 (3):
                BZip2 compressed set of files.
        """

        COMPRESSION_FORMAT_UNSPECIFIED = 0
        GZIP = 2
        BZIP2 = 3

    class CsvOptions(proto.Message):
        r"""Describes CSV and similar semi-structured data formats.

        Attributes:
            encoding (str):
                Optional. The character encoding of the data.
                Accepts "US-ASCII", "UTF-8", and "ISO-8859-1".
                Defaults to UTF-8 if unspecified.
            header_rows (int):
                Optional. The number of rows to interpret as
                header rows that should be skipped when reading
                data rows. Defaults to 0.
            delimiter (str):
                Optional. The delimiter used to separate
                values. Defaults to ','.
            quote (str):
                Optional. The character used to quote column
                values. Accepts '"' (double quotation mark) or
                ''' (single quotation mark). Defaults to '"'
                (double quotation mark) if unspecified.
        """

        encoding: str = proto.Field(
            proto.STRING,
            number=1,
        )
        header_rows: int = proto.Field(
            proto.INT32,
            number=2,
        )
        delimiter: str = proto.Field(
            proto.STRING,
            number=3,
        )
        quote: str = proto.Field(
            proto.STRING,
            number=4,
        )

    class JsonOptions(proto.Message):
        r"""Describes JSON data format.

        Attributes:
            encoding (str):
                Optional. The character encoding of the data.
                Accepts "US-ASCII", "UTF-8" and "ISO-8859-1".
                Defaults to UTF-8 if not specified.
        """

        encoding: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class IcebergOptions(proto.Message):
        r"""Describes Iceberg data format.

        Attributes:
            metadata_location (str):
                Optional. The location of where the iceberg
                metadata is present, must be within the table
                path
        """

        metadata_location: str = proto.Field(
            proto.STRING,
            number=1,
        )

    format_: Format = proto.Field(
        proto.ENUM,
        number=1,
        enum=Format,
    )
    compression_format: CompressionFormat = proto.Field(
        proto.ENUM,
        number=2,
        enum=CompressionFormat,
    )
    mime_type: str = proto.Field(
        proto.STRING,
        number=3,
    )
    csv: CsvOptions = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="options",
        message=CsvOptions,
    )
    json: JsonOptions = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="options",
        message=JsonOptions,
    )
    iceberg: IcebergOptions = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="options",
        message=IcebergOptions,
    )


class StorageAccess(proto.Message):
    r"""Describes the access mechanism of the data within its storage
    location.

    Attributes:
        read (google.cloud.dataplex_v1.types.StorageAccess.AccessMode):
            Output only. Describes the read access
            mechanism of the data. Not user settable.
    """

    class AccessMode(proto.Enum):
        r"""Access Mode determines how data stored within the Entity is
        read.

        Values:
            ACCESS_MODE_UNSPECIFIED (0):
                Access mode unspecified.
            DIRECT (1):
                Default. Data is accessed directly using
                storage APIs.
            MANAGED (2):
                Data is accessed through a managed interface
                using BigQuery APIs.
        """

        ACCESS_MODE_UNSPECIFIED = 0
        DIRECT = 1
        MANAGED = 2

    read: AccessMode = proto.Field(
        proto.ENUM,
        number=21,
        enum=AccessMode,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
