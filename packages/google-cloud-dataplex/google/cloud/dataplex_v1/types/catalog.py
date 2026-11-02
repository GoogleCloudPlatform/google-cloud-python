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
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.dataplex.v1",
    manifest={
        "EntryView",
        "TransferStatus",
        "AspectType",
        "EntryGroup",
        "EntryType",
        "Aspect",
        "AspectSource",
        "Entry",
        "EntrySource",
        "CreateEntryGroupRequest",
        "UpdateEntryGroupRequest",
        "DeleteEntryGroupRequest",
        "ListEntryGroupsRequest",
        "ListEntryGroupsResponse",
        "GetEntryGroupRequest",
        "CreateEntryTypeRequest",
        "UpdateEntryTypeRequest",
        "DeleteEntryTypeRequest",
        "ListEntryTypesRequest",
        "ListEntryTypesResponse",
        "GetEntryTypeRequest",
        "CreateAspectTypeRequest",
        "UpdateAspectTypeRequest",
        "DeleteAspectTypeRequest",
        "ListAspectTypesRequest",
        "ListAspectTypesResponse",
        "GetAspectTypeRequest",
        "CreateEntryRequest",
        "UpdateEntryRequest",
        "DeleteEntryRequest",
        "ListEntriesRequest",
        "ListEntriesResponse",
        "GetEntryRequest",
        "LookupEntryRequest",
        "LookupContextRequest",
        "ModifyEntryRequest",
        "LookupContextResponse",
        "SearchEntriesRequest",
        "SearchEntriesResult",
        "SearchEntriesResponse",
        "ImportItem",
        "CreateMetadataJobRequest",
        "GetMetadataJobRequest",
        "ListMetadataJobsRequest",
        "ListMetadataJobsResponse",
        "CancelMetadataJobRequest",
        "MetadataJob",
        "EntryLink",
        "CreateEntryLinkRequest",
        "UpdateEntryLinkRequest",
        "DeleteEntryLinkRequest",
        "LookupEntryLinksRequest",
        "LookupEntryLinksResponse",
        "GetEntryLinkRequest",
        "MetadataFeed",
        "CreateMetadataFeedRequest",
        "GetMetadataFeedRequest",
        "ListMetadataFeedsRequest",
        "ListMetadataFeedsResponse",
        "DeleteMetadataFeedRequest",
        "UpdateMetadataFeedRequest",
    },
)


class EntryView(proto.Enum):
    r"""View for controlling which parts of an entry are to be
    returned.

    Values:
        ENTRY_VIEW_UNSPECIFIED (0):
            Unspecified EntryView. Defaults to FULL.
        BASIC (1):
            Returns entry only, without aspects.
        FULL (2):
            Returns all required aspects as well as the
            keys of all non-required aspects.
        CUSTOM (3):
            Returns aspects matching custom fields in
            GetEntryRequest. If the number of aspects
            exceeds 100, the first 100 will be returned.
        ALL (4):
            Returns all aspects. If the number of aspects
            exceeds 100, the first 100 will be returned.
    """

    ENTRY_VIEW_UNSPECIFIED = 0
    BASIC = 1
    FULL = 2
    CUSTOM = 3
    ALL = 4


class TransferStatus(proto.Enum):
    r"""Denotes the transfer status of a resource. It is unspecified
    for resources created from Dataplex API.

    Values:
        TRANSFER_STATUS_UNSPECIFIED (0):
            The default value. It is set for resources
            that were not subject for migration from Data
            Catalog service.
        TRANSFER_STATUS_MIGRATED (1):
            Indicates that a resource was migrated from
            Data Catalog service but it hasn't been
            transferred yet. In particular the resource
            cannot be updated from Dataplex API.
        TRANSFER_STATUS_TRANSFERRED (2):
            Indicates that a resource was transferred
            from Data Catalog service. The resource can only
            be updated from Dataplex API.
    """

    TRANSFER_STATUS_UNSPECIFIED = 0
    TRANSFER_STATUS_MIGRATED = 1
    TRANSFER_STATUS_TRANSFERRED = 2


class AspectType(proto.Message):
    r"""AspectType is a template for creating Aspects, and represents
    the JSON-schema for a given Entry, for example, BigQuery Table
    Schema.

    Attributes:
        name (str):
            Output only. The relative resource name of the AspectType,
            of the form:
            projects/{project_number}/locations/{location_id}/aspectTypes/{aspect_type_id}.
        uid (str):
            Output only. System generated globally unique
            ID for the AspectType. If you delete and
            recreate the AspectType with the same name, then
            this ID will be different.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the AspectType was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the AspectType was
            last updated.
        description (str):
            Optional. Description of the AspectType.
        display_name (str):
            Optional. User friendly display name.
        labels (MutableMapping[str, str]):
            Optional. User-defined labels for the
            AspectType.
        etag (str):
            The service computes this checksum. The
            client may send it on update and delete requests
            to ensure it has an up-to-date value before
            proceeding.
        data_classification (google.cloud.dataplex_v1.types.AspectType.DataClassification):
            Optional. Immutable. Stores data
            classification of the aspect.
        authorization (google.cloud.dataplex_v1.types.AspectType.Authorization):
            Immutable. Defines the Authorization for this
            type.
        metadata_template (google.cloud.dataplex_v1.types.AspectType.MetadataTemplate):
            Required. MetadataTemplate of the aspect.
        transfer_status (google.cloud.dataplex_v1.types.TransferStatus):
            Output only. Denotes the transfer status of
            the Aspect Type. It is unspecified for Aspect
            Types created from Dataplex API.
    """

    class DataClassification(proto.Enum):
        r"""Classifies the data stored by the aspect.

        Values:
            DATA_CLASSIFICATION_UNSPECIFIED (0):
                Denotes that the aspect contains only
                metadata.
            METADATA_AND_DATA (1):
                Metadata and data classification.
        """

        DATA_CLASSIFICATION_UNSPECIFIED = 0
        METADATA_AND_DATA = 1

    class Authorization(proto.Message):
        r"""Authorization for an AspectType.

        Attributes:
            alternate_use_permission (str):
                Immutable. The IAM permission grantable on
                the EntryGroup to allow access to instantiate
                Aspects of Dataplex Universal Catalog owned
                AspectTypes, only settable for Dataplex
                Universal Catalog owned Types.
        """

        alternate_use_permission: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class MetadataTemplate(proto.Message):
        r"""MetadataTemplate definition for an AspectType.

        Attributes:
            index (int):
                Optional. Index is used to encode Template
                messages. The value of index can range between 1
                and 2,147,483,647. Index must be unique within
                all fields in a Template. (Nested Templates can
                reuse indexes). Once a Template is defined, the
                index cannot be changed, because it identifies
                the field in the actual storage format. Index is
                a mandatory field, but it is optional for top
                level fields, and map/array "values"
                definitions.
            name (str):
                Required. The name of the field.
            type_ (str):
                Required. The datatype of this field. The following values
                are supported:

                Primitive types:

                - string
                - int
                - bool
                - double
                - datetime. Must be of the format RFC3339 UTC "Zulu"
                  (Examples: "2014-10-02T15:01:23Z" and
                  "2014-10-02T15:01:23.045123456Z").

                Complex types:

                - enum
                - array
                - map
                - record
            record_fields (MutableSequence[google.cloud.dataplex_v1.types.AspectType.MetadataTemplate]):
                Optional. Field definition. You must specify
                it if the type is record. It defines the nested
                fields.
            enum_values (MutableSequence[google.cloud.dataplex_v1.types.AspectType.MetadataTemplate.EnumValue]):
                Optional. The list of values for an enum
                type. You must define it if the type is enum.
            map_items (google.cloud.dataplex_v1.types.AspectType.MetadataTemplate):
                Optional. If the type is map, set map_items. map_items can
                refer to a primitive field or a complex (record only) field.
                To specify a primitive field, you only need to set name and
                type in the nested MetadataTemplate. The recommended value
                for the name field is item, as this isn't used in the actual
                payload.
            array_items (google.cloud.dataplex_v1.types.AspectType.MetadataTemplate):
                Optional. If the type is array, set array_items. array_items
                can refer to a primitive field or a complex (record only)
                field. To specify a primitive field, you only need to set
                name and type in the nested MetadataTemplate. The
                recommended value for the name field is item, as this isn't
                used in the actual payload.
            type_id (str):
                Optional. You can use type id if this
                definition of the field needs to be reused
                later. The type id must be unique across the
                entire template. You can only specify it if the
                field type is record.
            type_ref (str):
                Optional. A reference to another field
                definition (not an inline definition). The value
                must be equal to the value of an id field
                defined elsewhere in the MetadataTemplate. Only
                fields with record type can refer to other
                fields.
            constraints (google.cloud.dataplex_v1.types.AspectType.MetadataTemplate.Constraints):
                Optional. Specifies the constraints on this
                field.
            annotations (google.cloud.dataplex_v1.types.AspectType.MetadataTemplate.Annotations):
                Optional. Specifies annotations on this
                field.
        """

        class EnumValue(proto.Message):
            r"""Definition of Enumvalue, to be used for enum fields.

            Attributes:
                index (int):
                    Required. Index for the enum value. It can't
                    be modified.
                name (str):
                    Required. Name of the enumvalue. This is the
                    actual value that the aspect can contain.
                deprecated (str):
                    Optional. You can set this message if you
                    need to deprecate an enum value.
            """

            index: int = proto.Field(
                proto.INT32,
                number=1,
            )
            name: str = proto.Field(
                proto.STRING,
                number=2,
            )
            deprecated: str = proto.Field(
                proto.STRING,
                number=3,
            )

        class Constraints(proto.Message):
            r"""Definition of the constraints of a field.

            Attributes:
                required (bool):
                    Optional. Marks this field as optional or
                    required.
            """

            required: bool = proto.Field(
                proto.BOOL,
                number=1,
            )

        class Annotations(proto.Message):
            r"""Definition of the annotations of a field.

            Attributes:
                deprecated (str):
                    Optional. Marks a field as deprecated. You
                    can include a deprecation message.
                display_name (str):
                    Optional. Display name for a field.
                description (str):
                    Optional. Description for a field.
                display_order (int):
                    Optional. Display order for a field. You can
                    use this to reorder where a field is rendered.
                string_type (str):
                    Optional. You can use String Type annotations to specify
                    special meaning to string fields. The following values are
                    supported:

                    - richText: The field must be interpreted as a rich text
                      field.
                    - url: A fully qualified URL link.
                    - resource: A service qualified resource reference.
                string_values (MutableSequence[str]):
                    Optional. Suggested hints for string fields.
                    You can use them to suggest values to users
                    through console.
            """

            deprecated: str = proto.Field(
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
            display_order: int = proto.Field(
                proto.INT32,
                number=4,
            )
            string_type: str = proto.Field(
                proto.STRING,
                number=6,
            )
            string_values: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=7,
            )

        index: int = proto.Field(
            proto.INT32,
            number=1,
        )
        name: str = proto.Field(
            proto.STRING,
            number=2,
        )
        type_: str = proto.Field(
            proto.STRING,
            number=5,
        )
        record_fields: MutableSequence["AspectType.MetadataTemplate"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=6,
                message="AspectType.MetadataTemplate",
            )
        )
        enum_values: MutableSequence["AspectType.MetadataTemplate.EnumValue"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=8,
                message="AspectType.MetadataTemplate.EnumValue",
            )
        )
        map_items: "AspectType.MetadataTemplate" = proto.Field(
            proto.MESSAGE,
            number=10,
            message="AspectType.MetadataTemplate",
        )
        array_items: "AspectType.MetadataTemplate" = proto.Field(
            proto.MESSAGE,
            number=11,
            message="AspectType.MetadataTemplate",
        )
        type_id: str = proto.Field(
            proto.STRING,
            number=12,
        )
        type_ref: str = proto.Field(
            proto.STRING,
            number=13,
        )
        constraints: "AspectType.MetadataTemplate.Constraints" = proto.Field(
            proto.MESSAGE,
            number=50,
            message="AspectType.MetadataTemplate.Constraints",
        )
        annotations: "AspectType.MetadataTemplate.Annotations" = proto.Field(
            proto.MESSAGE,
            number=51,
            message="AspectType.MetadataTemplate.Annotations",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=8,
    )
    data_classification: DataClassification = proto.Field(
        proto.ENUM,
        number=9,
        enum=DataClassification,
    )
    authorization: Authorization = proto.Field(
        proto.MESSAGE,
        number=52,
        message=Authorization,
    )
    metadata_template: MetadataTemplate = proto.Field(
        proto.MESSAGE,
        number=53,
        message=MetadataTemplate,
    )
    transfer_status: "TransferStatus" = proto.Field(
        proto.ENUM,
        number=202,
        enum="TransferStatus",
    )


class EntryGroup(proto.Message):
    r"""An Entry Group represents a logical grouping of one or more
    Entries.

    Attributes:
        name (str):
            Output only. The relative resource name of the EntryGroup,
            in the format
            projects/{project_id_or_number}/locations/{location_id}/entryGroups/{entry_group_id}.
        uid (str):
            Output only. System generated globally unique
            ID for the EntryGroup. If you delete and
            recreate the EntryGroup with the same name, this
            ID will be different.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the EntryGroup was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the EntryGroup was
            last updated.
        description (str):
            Optional. Description of the EntryGroup.
        display_name (str):
            Optional. User friendly display name.
        labels (MutableMapping[str, str]):
            Optional. User-defined labels for the
            EntryGroup.
        etag (str):
            This checksum is computed by the service, and
            might be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
        transfer_status (google.cloud.dataplex_v1.types.TransferStatus):
            Output only. Denotes the transfer status of
            the Entry Group. It is unspecified for Entry
            Group created from Dataplex API.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=8,
    )
    transfer_status: "TransferStatus" = proto.Field(
        proto.ENUM,
        number=202,
        enum="TransferStatus",
    )


class EntryType(proto.Message):
    r"""Entry Type is a template for creating Entries.

    Attributes:
        name (str):
            Output only. The relative resource name of the EntryType, of
            the form:
            projects/{project_number}/locations/{location_id}/entryTypes/{entry_type_id}.
        uid (str):
            Output only. System generated globally unique
            ID for the EntryType. This ID will be different
            if the EntryType is deleted and re-created with
            the same name.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the EntryType was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the EntryType was
            last updated.
        description (str):
            Optional. Description of the EntryType.
        display_name (str):
            Optional. User friendly display name.
        labels (MutableMapping[str, str]):
            Optional. User-defined labels for the
            EntryType.
        etag (str):
            Optional. This checksum is computed by the
            service, and might be sent on update and delete
            requests to ensure the client has an up-to-date
            value before proceeding.
        type_aliases (MutableSequence[str]):
            Optional. Indicates the classes this Entry
            Type belongs to, for example, TABLE, DATABASE,
            MODEL.
        platform (str):
            Optional. The platform that Entries of this
            type belongs to.
        system (str):
            Optional. The system that Entries of this
            type belongs to. Examples include CloudSQL,
            MariaDB etc
        required_aspects (MutableSequence[google.cloud.dataplex_v1.types.EntryType.AspectInfo]):
            AspectInfo for the entry type.
        authorization (google.cloud.dataplex_v1.types.EntryType.Authorization):
            Immutable. Authorization defined for this
            type.
    """

    class AspectInfo(proto.Message):
        r"""

        Attributes:
            type_ (str):
                Required aspect type for the entry type.
        """

        type_: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class Authorization(proto.Message):
        r"""Authorization for an Entry Type.

        Attributes:
            alternate_use_permission (str):
                Immutable. The IAM permission grantable on
                the Entry Group to allow access to instantiate
                Entries of Dataplex Universal Catalog owned
                Entry Types, only settable for Dataplex
                Universal Catalog owned Types.
        """

        alternate_use_permission: str = proto.Field(
            proto.STRING,
            number=1,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=8,
    )
    type_aliases: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=9,
    )
    platform: str = proto.Field(
        proto.STRING,
        number=10,
    )
    system: str = proto.Field(
        proto.STRING,
        number=11,
    )
    required_aspects: MutableSequence[AspectInfo] = proto.RepeatedField(
        proto.MESSAGE,
        number=50,
        message=AspectInfo,
    )
    authorization: Authorization = proto.Field(
        proto.MESSAGE,
        number=51,
        message=Authorization,
    )


class Aspect(proto.Message):
    r"""Represents a single piece of metadata describing an entry or
    entry link.

    Attributes:
        aspect_type (str):
            Output only. The resource name of the type
            used to create this Aspect.
        path (str):
            Output only. The path in the entry under
            which the aspect is attached.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the Aspect was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the Aspect was
            last updated.
        data (google.protobuf.struct_pb2.Struct):
            Required. The content of the aspect,
            according to its aspect type schema. The maximum
            size of the field is 120KB (encoded as UTF-8).
        aspect_source (google.cloud.dataplex_v1.types.AspectSource):
            Optional. Information related to the source
            system of the aspect.
    """

    aspect_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    path: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    data: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=8,
        message=struct_pb2.Struct,
    )
    aspect_source: "AspectSource" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="AspectSource",
    )


class AspectSource(proto.Message):
    r"""Information related to the source system of the aspect.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the aspect was created in the source
            system.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the aspect was last updated in the
            source system.
        data_version (str):
            The version of the data format used to
            produce this data. This field is used to
            indicated when the underlying data format
            changes (e.g., schema modifications, changes to
            the source URL format definition, etc).
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    data_version: str = proto.Field(
        proto.STRING,
        number=12,
    )


class Entry(proto.Message):
    r"""An entry is a representation of a data resource that can be
    described by various metadata.

    Attributes:
        name (str):
            Identifier. The relative resource name of the entry, in the
            format
            ``projects/{project_id_or_number}/locations/{location_id}/entryGroups/{entry_group_id}/entries/{entry_id}``.
        entry_type (str):
            Required. Immutable. The relative resource name of the entry
            type that was used to create this entry, in the format
            ``projects/{project_id_or_number}/locations/{location_id}/entryTypes/{entry_type_id}``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the entry was
            created in Dataplex Universal Catalog.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the entry was last
            updated in Dataplex Universal Catalog.
        aspects (MutableMapping[str, google.cloud.dataplex_v1.types.Aspect]):
            Optional. The aspects that are attached to the entry.
            Depending on how the aspect is attached to the entry, the
            format of the aspect key can be one of the following:

            - If the aspect is attached directly to the entry:
              ``{project_id_or_number}.{location_id}.{aspect_type_id}``
            - If the aspect is attached to an entry's path:
              ``{project_id_or_number}.{location_id}.{aspect_type_id}@{path}``
        parent_entry (str):
            Optional. Immutable. The resource name of the parent entry,
            in the format
            ``projects/{project_id_or_number}/locations/{location_id}/entryGroups/{entry_group_id}/entries/{entry_id}``.
        fully_qualified_name (str):
            Optional. A name for the entry that can be referenced by an
            external system. For more information, see `Fully qualified
            names <https://cloud.google.com/data-catalog/docs/fully-qualified-names>`__.
            The maximum size of the field is 4000 characters.
        entry_source (google.cloud.dataplex_v1.types.EntrySource):
            Optional. Information related to the source
            system of the data resource that is represented
            by the entry.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    entry_type: str = proto.Field(
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
    aspects: MutableMapping[str, "Aspect"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=9,
        message="Aspect",
    )
    parent_entry: str = proto.Field(
        proto.STRING,
        number=10,
    )
    fully_qualified_name: str = proto.Field(
        proto.STRING,
        number=12,
    )
    entry_source: "EntrySource" = proto.Field(
        proto.MESSAGE,
        number=15,
        message="EntrySource",
    )


class EntrySource(proto.Message):
    r"""Information related to the source system of the data resource
    that is represented by the entry.

    Attributes:
        resource (str):
            The name of the resource in the source
            system. Maximum length is 4,000 characters.
        system (str):
            The name of the source system.
            Maximum length is 64 characters.
        platform (str):
            The platform containing the source system.
            Maximum length is 64 characters.
        display_name (str):
            A user-friendly display name.
            Maximum length is 500 characters.
        description (str):
            A description of the data resource.
            Maximum length is 2,000 characters.
        labels (MutableMapping[str, str]):
            User-defined labels.
            The maximum size of keys and values is 128
            characters each.
        ancestors (MutableSequence[google.cloud.dataplex_v1.types.EntrySource.Ancestor]):
            Immutable. The entries representing the
            ancestors of the data resource in the source
            system.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the resource was created in the
            source system.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the resource was last updated in the source
            system. If the entry exists in the system and its
            ``EntrySource`` has ``update_time`` populated, further
            updates to the ``EntrySource`` of the entry must provide
            incremental updates to its ``update_time``.
        location (str):
            Output only. Location of the resource in the
            source system. You can search the entry by this
            location. By default, this should match the
            location of the entry group containing this
            entry. A different value allows capturing the
            source location for data external to Google
            Cloud.
    """

    class Ancestor(proto.Message):
        r"""Information about individual items in the hierarchy that is
        associated with the data resource.

        Attributes:
            name (str):
                Optional. The name of the ancestor resource.
            type_ (str):
                Optional. The type of the ancestor resource.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        type_: str = proto.Field(
            proto.STRING,
            number=2,
        )

    resource: str = proto.Field(
        proto.STRING,
        number=1,
    )
    system: str = proto.Field(
        proto.STRING,
        number=2,
    )
    platform: str = proto.Field(
        proto.STRING,
        number=3,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    description: str = proto.Field(
        proto.STRING,
        number=6,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    ancestors: MutableSequence[Ancestor] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=Ancestor,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    location: str = proto.Field(
        proto.STRING,
        number=12,
    )


class CreateEntryGroupRequest(proto.Message):
    r"""Create EntryGroup Request.

    Attributes:
        parent (str):
            Required. The resource name of the entryGroup, of the form:
            projects/{project_number}/locations/{location_id} where
            ``location_id`` refers to a Google Cloud region.
        entry_group_id (str):
            Required. EntryGroup identifier.
        entry_group (google.cloud.dataplex_v1.types.EntryGroup):
            Required. EntryGroup Resource.
        validate_only (bool):
            Optional. The service validates the request
            without performing any mutations. The default is
            false.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    entry_group_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    entry_group: "EntryGroup" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="EntryGroup",
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class UpdateEntryGroupRequest(proto.Message):
    r"""Update EntryGroup Request.

    Attributes:
        entry_group (google.cloud.dataplex_v1.types.EntryGroup):
            Required. EntryGroup Resource.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update.
        validate_only (bool):
            Optional. The service validates the request,
            without performing any mutations. The default is
            false.
    """

    entry_group: "EntryGroup" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="EntryGroup",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class DeleteEntryGroupRequest(proto.Message):
    r"""Delete EntryGroup Request.

    Attributes:
        name (str):
            Required. The resource name of the EntryGroup:
            ``projects/{project_number}/locations/{location_id}/entryGroups/{entry_group_id}``.
        etag (str):
            Optional. If the client provided etag value
            does not match the current etag value, the
            DeleteEntryGroupRequest method returns an
            ABORTED error response.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListEntryGroupsRequest(proto.Message):
    r"""List entryGroups request.

    Attributes:
        parent (str):
            Required. The resource name of the entryGroup location, of
            the form:
            ``projects/{project_number}/locations/{location_id}`` where
            ``location_id`` refers to a Google Cloud region.
        page_size (int):
            Optional. Maximum number of EntryGroups to
            return. The service may return fewer than this
            value. If unspecified, the service returns at
            most 10 EntryGroups. The maximum value is 1000;
            values above 1000 will be coerced to 1000.
        page_token (str):
            Optional. Page token received from a previous
            ``ListEntryGroups`` call. Provide this to retrieve the
            subsequent page. When paginating, all other parameters you
            provide to ``ListEntryGroups`` must match the call that
            provided the page token.
        filter (str):
            Optional. Filter request.
        order_by (str):
            Optional. Order by fields for the result.
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


class ListEntryGroupsResponse(proto.Message):
    r"""List entry groups response.

    Attributes:
        entry_groups (MutableSequence[google.cloud.dataplex_v1.types.EntryGroup]):
            Entry groups under the given parent location.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
        unreachable_locations (MutableSequence[str]):
            Locations that the service couldn't reach.
    """

    @property
    def raw_page(self):
        return self

    entry_groups: MutableSequence["EntryGroup"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="EntryGroup",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable_locations: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetEntryGroupRequest(proto.Message):
    r"""Get EntryGroup request.

    Attributes:
        name (str):
            Required. The resource name of the EntryGroup:
            ``projects/{project_number}/locations/{location_id}/entryGroups/{entry_group_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateEntryTypeRequest(proto.Message):
    r"""Create EntryType Request.

    Attributes:
        parent (str):
            Required. The resource name of the EntryType, of the form:
            projects/{project_number}/locations/{location_id} where
            ``location_id`` refers to a Google Cloud region.
        entry_type_id (str):
            Required. EntryType identifier.
        entry_type (google.cloud.dataplex_v1.types.EntryType):
            Required. EntryType Resource.
        validate_only (bool):
            Optional. The service validates the request
            without performing any mutations. The default is
            false.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    entry_type_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    entry_type: "EntryType" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="EntryType",
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class UpdateEntryTypeRequest(proto.Message):
    r"""Update EntryType Request.

    Attributes:
        entry_type (google.cloud.dataplex_v1.types.EntryType):
            Required. EntryType Resource.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update.
        validate_only (bool):
            Optional. The service validates the request
            without performing any mutations. The default is
            false.
    """

    entry_type: "EntryType" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="EntryType",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class DeleteEntryTypeRequest(proto.Message):
    r"""Delete EntryType Request.

    Attributes:
        name (str):
            Required. The resource name of the EntryType:
            ``projects/{project_number}/locations/{location_id}/entryTypes/{entry_type_id}``.
        etag (str):
            Optional. If the client provided etag value
            does not match the current etag value, the
            DeleteEntryTypeRequest method returns an ABORTED
            error response.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListEntryTypesRequest(proto.Message):
    r"""List EntryTypes request

    Attributes:
        parent (str):
            Required. The resource name of the EntryType location, of
            the form:
            ``projects/{project_number}/locations/{location_id}`` where
            ``location_id`` refers to a Google Cloud region.
        page_size (int):
            Optional. Maximum number of EntryTypes to
            return. The service may return fewer than this
            value. If unspecified, the service returns at
            most 10 EntryTypes. The maximum value is 1000;
            values above 1000 will be coerced to 1000.
        page_token (str):
            Optional. Page token received from a previous
            ``ListEntryTypes`` call. Provide this to retrieve the
            subsequent page. When paginating, all other parameters you
            provided to ``ListEntryTypes`` must match the call that
            provided the page token.
        filter (str):
            Optional. Filter request. Filters are case-sensitive. The
            service supports the following formats:

            - labels.key1 = "value1"
            - labels:key1
            - name = "value"

            These restrictions can be conjoined with AND, OR, and NOT
            conjunctions.
        order_by (str):
            Optional. Orders the result by ``name`` or ``create_time``
            fields. If not specified, the ordering is undefined.
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


class ListEntryTypesResponse(proto.Message):
    r"""List EntryTypes response.

    Attributes:
        entry_types (MutableSequence[google.cloud.dataplex_v1.types.EntryType]):
            EntryTypes under the given parent location.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
        unreachable_locations (MutableSequence[str]):
            Locations that the service couldn't reach.
    """

    @property
    def raw_page(self):
        return self

    entry_types: MutableSequence["EntryType"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="EntryType",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable_locations: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetEntryTypeRequest(proto.Message):
    r"""Get EntryType request.

    Attributes:
        name (str):
            Required. The resource name of the EntryType:
            ``projects/{project_number}/locations/{location_id}/entryTypes/{entry_type_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateAspectTypeRequest(proto.Message):
    r"""Create AspectType Request.

    Attributes:
        parent (str):
            Required. The resource name of the AspectType, of the form:
            projects/{project_number}/locations/{location_id} where
            ``location_id`` refers to a Google Cloud region.
        aspect_type_id (str):
            Required. AspectType identifier.
        aspect_type (google.cloud.dataplex_v1.types.AspectType):
            Required. AspectType Resource.
        validate_only (bool):
            Optional. The service validates the request
            without performing any mutations. The default is
            false.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    aspect_type_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    aspect_type: "AspectType" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AspectType",
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class UpdateAspectTypeRequest(proto.Message):
    r"""Update AspectType Request

    Attributes:
        aspect_type (google.cloud.dataplex_v1.types.AspectType):
            Required. AspectType Resource
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update.
        validate_only (bool):
            Optional. Only validate the request, but do
            not perform mutations. The default is false.
    """

    aspect_type: "AspectType" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="AspectType",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class DeleteAspectTypeRequest(proto.Message):
    r"""Delete AspectType Request.

    Attributes:
        name (str):
            Required. The resource name of the AspectType:
            ``projects/{project_number}/locations/{location_id}/aspectTypes/{aspect_type_id}``.
        etag (str):
            Optional. If the client provided etag value
            does not match the current etag value, the
            DeleteAspectTypeRequest method returns an
            ABORTED error response.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListAspectTypesRequest(proto.Message):
    r"""List AspectTypes request.

    Attributes:
        parent (str):
            Required. The resource name of the AspectType location, of
            the form:
            ``projects/{project_number}/locations/{location_id}`` where
            ``location_id`` refers to a Google Cloud region.
        page_size (int):
            Optional. Maximum number of AspectTypes to
            return. The service may return fewer than this
            value. If unspecified, the service returns at
            most 10 AspectTypes. The maximum value is 1000;
            values above 1000 will be coerced to 1000.
        page_token (str):
            Optional. Page token received from a previous
            ``ListAspectTypes`` call. Provide this to retrieve the
            subsequent page. When paginating, all other parameters you
            provide to ``ListAspectTypes`` must match the call that
            provided the page token.
        filter (str):
            Optional. Filter request. Filters are case-sensitive. The
            service supports the following formats:

            - labels.key1 = "value1"
            - labels:key1
            - name = "value"

            These restrictions can be conjoined with AND, OR, and NOT
            conjunctions.
        order_by (str):
            Optional. Orders the result by ``name`` or ``create_time``
            fields. If not specified, the ordering is undefined.
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


class ListAspectTypesResponse(proto.Message):
    r"""List AspectTypes response.

    Attributes:
        aspect_types (MutableSequence[google.cloud.dataplex_v1.types.AspectType]):
            AspectTypes under the given parent location.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
        unreachable_locations (MutableSequence[str]):
            Locations that the service couldn't reach.
    """

    @property
    def raw_page(self):
        return self

    aspect_types: MutableSequence["AspectType"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AspectType",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable_locations: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetAspectTypeRequest(proto.Message):
    r"""Get AspectType request.

    Attributes:
        name (str):
            Required. The resource name of the AspectType:
            ``projects/{project_number}/locations/{location_id}/aspectTypes/{aspect_type_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateEntryRequest(proto.Message):
    r"""Create Entry request.

    Attributes:
        parent (str):
            Required. The resource name of the parent Entry Group:
            ``projects/{project}/locations/{location}/entryGroups/{entry_group}``.
        entry_id (str):
            Required. Entry identifier. It has to be unique within an
            Entry Group.

            Entries corresponding to Google Cloud resources use an Entry
            ID format based on `full resource
            names <https://cloud.google.com/apis/design/resource_names#full_resource_name>`__.
            The format is a full resource name of the resource without
            the prefix double slashes in the API service name part of
            the full resource name. This allows retrieval of entries
            using their associated resource name.

            For example, if the full resource name of a resource is
            ``//library.googleapis.com/shelves/shelf1/books/book2``,
            then the suggested entry_id is
            ``library.googleapis.com/shelves/shelf1/books/book2``.

            It is also suggested to follow the same convention for
            entries corresponding to resources from providers or systems
            other than Google Cloud.

            The maximum size of the field is 4000 characters.
        entry (google.cloud.dataplex_v1.types.Entry):
            Required. Entry resource.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    entry_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    entry: "Entry" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Entry",
    )


class UpdateEntryRequest(proto.Message):
    r"""Update Entry request.

    Attributes:
        entry (google.cloud.dataplex_v1.types.Entry):
            Required. Entry resource.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Mask of fields to update. To update Aspects, the
            update_mask must contain the value "aspects".

            If the update_mask is empty, the service will update all
            modifiable fields present in the request.
        allow_missing (bool):
            Optional. If set to true and the entry
            doesn't exist, the service will create it.
        delete_missing_aspects (bool):
            Optional. If set to true and the aspect_keys specify aspect
            ranges, the service deletes any existing aspects from that
            range that weren't provided in the request.
        aspect_keys (MutableSequence[str]):
            Optional. The map keys of the Aspects which the service
            should modify. It supports the following syntaxes:

            - ``<aspect_type_reference>`` - matches an aspect of the
              given type and empty path.
            - ``<aspect_type_reference>@path`` - matches an aspect of
              the given type and specified path. For example, to attach
              an aspect to a field that is specified by the ``schema``
              aspect, the path should have the format
              ``Schema.<field_name>``.
            - ``<aspect_type_reference>@*`` - matches aspects of the
              given type for all paths.
            - ``*@path`` - matches aspects of all types on the given
              path.

            The service will not remove existing aspects matching the
            syntax unless ``delete_missing_aspects`` is set to true.

            If this field is left empty, the service treats it as
            specifying exactly those Aspects present in the request.
    """

    entry: "Entry" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Entry",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    delete_missing_aspects: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    aspect_keys: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )


class DeleteEntryRequest(proto.Message):
    r"""Delete Entry request.

    Attributes:
        name (str):
            Required. The resource name of the Entry:
            ``projects/{project}/locations/{location}/entryGroups/{entry_group}/entries/{entry}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListEntriesRequest(proto.Message):
    r"""List Entries request.

    Attributes:
        parent (str):
            Required. The resource name of the parent Entry Group:
            ``projects/{project}/locations/{location}/entryGroups/{entry_group}``.
        page_size (int):
            Optional. Number of items to return per page. If there are
            remaining results, the service returns a next_page_token. If
            unspecified, the service returns at most 10 Entries. The
            maximum value is 100; values above 100 will be coerced to
            100.
        page_token (str):
            Optional. Page token received from a previous
            ``ListEntries`` call. Provide this to retrieve the
            subsequent page.
        filter (str):
            Optional. A filter on the entries to return. Filters are
            case-sensitive. You can filter the request by the following
            fields:

            - entry_type
            - entry_source.display_name
            - parent_entry

            The comparison operators are =, !=, <, >, <=, >=. The
            service compares strings according to lexical order.

            You can use the logical operators AND, OR, NOT in the
            filter.

            You can use Wildcard "\*", but for entry_type and
            parent_entry you need to provide the full project id or
            number.

            You cannot use parent_entry in conjunction with other
            fields.

            Example filter expressions:

            - "entry_source.display_name=AnExampleDisplayName"
            - "entry_type=projects/example-project/locations/global/entryTypes/example-entry_type"
            - "entry_type=projects/example-project/locations/us/entryTypes/a\*
              OR entry_type=projects/another-project/locations/\*"
            - "NOT entry_source.display_name=AnotherExampleDisplayName"
            - "parent_entry=projects/example-project/locations/us/entryGroups/example-entry-group/entries/example-entry".
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


class ListEntriesResponse(proto.Message):
    r"""List Entries response.

    Attributes:
        entries (MutableSequence[google.cloud.dataplex_v1.types.Entry]):
            The list of entries under the given parent
            location.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    entries: MutableSequence["Entry"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Entry",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetEntryRequest(proto.Message):
    r"""Get Entry request.

    Attributes:
        name (str):
            Required. The resource name of the Entry:
            ``projects/{project}/locations/{location}/entryGroups/{entry_group}/entries/{entry}``.
        view (google.cloud.dataplex_v1.types.EntryView):
            Optional. View to control which parts of an entry the
            service should return. **Please check the limitations on
            returned aspects in the Entry view documentation. Amount of
            returned aspects depends on the selected Entry View.**
        aspect_types (MutableSequence[str]):
            Optional. Limits the aspects returned to the
            provided aspect types. It only works for CUSTOM
            view.
        paths (MutableSequence[str]):
            Optional. Limits the aspects returned to
            those associated with the provided paths within
            the Entry. It only works for CUSTOM view.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "EntryView" = proto.Field(
        proto.ENUM,
        number=2,
        enum="EntryView",
    )
    aspect_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    paths: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


class LookupEntryRequest(proto.Message):
    r"""Lookup Entry request using permissions in the source system.

    Attributes:
        name (str):
            Required. The project to which the request should be
            attributed in the following form:
            ``projects/{project}/locations/{location}``.
        view (google.cloud.dataplex_v1.types.EntryView):
            Optional. View to control which parts of an entry the
            service should return. **Please check the limitations on
            returned aspects in the Entry view documentation. Amount of
            returned aspects depends on the selected Entry View.**
        aspect_types (MutableSequence[str]):
            Optional. Limits the aspects returned to the
            provided aspect types. It only works for CUSTOM
            view.
        paths (MutableSequence[str]):
            Optional. Limits the aspects returned to
            those associated with the provided paths within
            the Entry. It only works for CUSTOM view.
        entry (str):
            Required. The resource name of the Entry:
            ``projects/{project}/locations/{location}/entryGroups/{entry_group}/entries/{entry}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "EntryView" = proto.Field(
        proto.ENUM,
        number=2,
        enum="EntryView",
    )
    aspect_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    paths: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    entry: str = proto.Field(
        proto.STRING,
        number=5,
    )


class LookupContextRequest(proto.Message):
    r"""Lookup Context using permissions in the source system.

    Attributes:
        name (str):
            Required. The project to which the request should be
            attributed in the following form:
            ``projects/{project}/locations/{location}``.
        resources (MutableSequence[str]):
            Required. The entry names to look up the context for. The
            maximum number of resources for a request is limited to 10.

            Examples:
            ---------

            ``projects/{project}/locations/{location}/entryGroups/{entry_group}/entries/{entry}``
        context (str):
            Optional. The text representing contextual
            information for which metadata context is being
            requested.
        options (MutableMapping[str, str]):
            Optional. Allows to configure the context.

            Supported options:

            - ``format`` - The format of the context (one of ``yaml``,
              ``xml``, ``json``, default is ``yaml``).
            - ``context_budget`` - If provided, the output will be
              intelligently truncated on a best-effort basis to contain
              approximately the desired amount of characters. There is
              no guarantee to achieve the specific amount.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    resources: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    context: str = proto.Field(
        proto.STRING,
        number=3,
    )
    options: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )


class ModifyEntryRequest(proto.Message):
    r"""Modify Entry request using permissions in the source system.

    Attributes:
        name (str):
            Required. The project to which the request should be
            attributed in the following form:
            ``projects/{project}/locations/{location}``.
        entry (google.cloud.dataplex_v1.types.Entry):
            Required. The entry to modify.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Mask of fields to update. To update Aspects, the
            update_mask must contain the value "aspects".

            If the update_mask is empty, the service will update all
            modifiable fields present in the request.
        delete_missing_aspects (bool):
            Optional. If set to true, any aspects not
            specified in the request will be deleted. The
            default is false.
        aspect_keys (MutableSequence[str]):
            Optional. The aspect keys which the service should modify.
            It supports the following syntaxes:

            - ``<aspect_type_reference>`` - matches an aspect of the
              given type and empty path.
            - ``<aspect_type_reference>@path`` - matches an aspect of
              the given type and specified path. For example, to attach
              an aspect to a field that is specified by the ``schema``
              aspect, the path should have the format
              ``Schema.<field_name>``.
            - ``<aspect_type_reference>@*`` - matches aspects of the
              given type for all paths.
            - ``*@path`` - matches aspects of all types on the given
              path.

            The service will not remove existing aspects matching the
            syntax unless ``delete_missing_aspects`` is set to true.

            If this field is left empty, the service treats it as
            specifying exactly those Aspects present in the request.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    entry: "Entry" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Entry",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )
    delete_missing_aspects: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    aspect_keys: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )


class LookupContextResponse(proto.Message):
    r"""Lookup Context response.

    Attributes:
        context (str):
            Pre-formatted block of text containing the
            context for the requested resources.
    """

    context: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SearchEntriesRequest(proto.Message):
    r"""

    Attributes:
        name (str):
            Required. The project to which the request should be
            attributed in the following form:
            ``projects/{project}/locations/global``.
        query (str):
            Required. The query against which entries in scope should be
            matched. The query syntax is defined in `Search syntax for
            Dataplex Universal
            Catalog <https://cloud.google.com/dataplex/docs/search-syntax>`__.
        page_size (int):
            Optional. Number of results in the search page. If <=0, then
            defaults to 10. Max limit for page_size is 1000. Throws an
            invalid argument for page_size > 1000.
        page_token (str):
            Optional. Page token received from a previous
            ``SearchEntries`` call. Provide this to retrieve the
            subsequent page.
        order_by (str):
            Optional. Specifies the ordering of results. Supported
            values are:

            - ``relevance``
            - ``last_modified_timestamp``
            - ``last_modified_timestamp asc``
        scope (str):
            Optional. The scope under which the search should be
            operating. It must either be ``organizations/<org_id>`` or
            ``projects/<project_ref>``. If it is unspecified, it
            defaults to the organization where the project provided in
            ``name`` is located.
        semantic_search (bool):
            Optional. Specifies whether the search should
            understand the meaning and intent behind the
            query, rather than just matching keywords.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    query: str = proto.Field(
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
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )
    scope: str = proto.Field(
        proto.STRING,
        number=7,
    )
    semantic_search: bool = proto.Field(
        proto.BOOL,
        number=11,
    )


class SearchEntriesResult(proto.Message):
    r"""A single result of a SearchEntries request.

    Attributes:
        linked_resource (str):
            Linked resource name.
        dataplex_entry (google.cloud.dataplex_v1.types.Entry):

        snippets (google.cloud.dataplex_v1.types.SearchEntriesResult.Snippets):
            Snippets.
    """

    class Snippets(proto.Message):
        r"""Snippets for the entry, contains HTML-style highlighting for
        matched tokens, will be used in UI.

        Attributes:
            dataplex_entry (google.cloud.dataplex_v1.types.Entry):
                Entry
        """

        dataplex_entry: "Entry" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="Entry",
        )

    linked_resource: str = proto.Field(
        proto.STRING,
        number=8,
    )
    dataplex_entry: "Entry" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="Entry",
    )
    snippets: Snippets = proto.Field(
        proto.MESSAGE,
        number=12,
        message=Snippets,
    )


class SearchEntriesResponse(proto.Message):
    r"""

    Attributes:
        results (MutableSequence[google.cloud.dataplex_v1.types.SearchEntriesResult]):
            The results matching the search query.
        total_size (int):
            The estimated total number of matching
            entries. This number isn't guaranteed to be
            accurate.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
        unreachable (MutableSequence[str]):
            Locations that the service couldn't reach.
            Search results don't include data from these
            locations.
    """

    @property
    def raw_page(self):
        return self

    results: MutableSequence["SearchEntriesResult"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SearchEntriesResult",
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


class ImportItem(proto.Message):
    r"""An object that describes the values that you want to set for an
    entry and its attached aspects when you import metadata. Used when
    you run a metadata import job. See
    [CreateMetadataJob][google.cloud.dataplex.v1.CatalogService.CreateMetadataJob].

    You provide a collection of import items in a metadata import file.
    For more information about how to create a metadata import file, see
    `Metadata import
    file <https://cloud.google.com/dataplex/docs/import-metadata#metadata-import-file>`__.

    Attributes:
        entry (google.cloud.dataplex_v1.types.Entry):
            Information about an entry and its attached
            aspects.
        entry_link (google.cloud.dataplex_v1.types.EntryLink):
            Information about the entry link. User should provide either
            one of the entry or entry_link. While providing entry_link,
            user should not provide update_mask and aspect_keys.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The fields to update, in paths that are relative to the
            ``Entry`` resource. Separate each field with a comma.

            In ``FULL`` entry sync mode, Dataplex Universal Catalog
            includes the paths of all of the fields for an entry that
            can be modified, including aspects. This means that Dataplex
            Universal Catalog replaces the existing entry with the entry
            in the metadata import file. All modifiable fields are
            updated, regardless of the fields that are listed in the
            update mask, and regardless of whether a field is present in
            the ``entry`` object.

            The ``update_mask`` field is ignored when an entry is
            created or re-created.

            In an aspect-only metadata job (when entry sync mode is
            ``NONE``), set this value to ``aspects``.

            Dataplex Universal Catalog also determines which entries and
            aspects to modify by comparing the values and timestamps
            that you provide in the metadata import file with the values
            and timestamps that exist in your project. For more
            information, see `Comparison
            logic <https://cloud.google.com/dataplex/docs/import-metadata#data-modification-logic>`__.
        aspect_keys (MutableSequence[str]):
            The aspects to modify. Supports the following syntaxes:

            - ``{aspect_type_reference}``: matches aspects that belong
              to the specified aspect type and are attached directly to
              the entry.
            - ``{aspect_type_reference}@{path}``: matches aspects that
              belong to the specified aspect type and path.
            - ``{aspect_type_reference}@*`` : matches aspects of the
              given type for all paths.
            - ``*@path`` : matches aspects of all types on the given
              path.

            Replace ``{aspect_type_reference}`` with a reference to the
            aspect type, in the format
            ``{project_id_or_number}.{location_id}.{aspect_type_id}``.

            In ``FULL`` entry sync mode, if you leave this field empty,
            it is treated as specifying exactly those aspects that are
            present within the specified entry. Dataplex Universal
            Catalog implicitly adds the keys for all of the required
            aspects of an entry.
    """

    entry: "Entry" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Entry",
    )
    entry_link: "EntryLink" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="EntryLink",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    aspect_keys: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class CreateMetadataJobRequest(proto.Message):
    r"""Create metadata job request.

    Attributes:
        parent (str):
            Required. The resource name of the parent location, in the
            format
            ``projects/{project_id_or_number}/locations/{location_id}``
        metadata_job (google.cloud.dataplex_v1.types.MetadataJob):
            Required. The metadata job resource.
        metadata_job_id (str):
            Optional. The metadata job ID. If not provided, a unique ID
            is generated with the prefix ``metadata-job-``.
        validate_only (bool):
            Optional. The service validates the request
            without performing any mutations. The default is
            false.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    metadata_job: "MetadataJob" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="MetadataJob",
    )
    metadata_job_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class GetMetadataJobRequest(proto.Message):
    r"""Get metadata job request.

    Attributes:
        name (str):
            Required. The resource name of the metadata job, in the
            format
            ``projects/{project_id_or_number}/locations/{location_id}/metadataJobs/{metadata_job_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListMetadataJobsRequest(proto.Message):
    r"""List metadata jobs request.

    Attributes:
        parent (str):
            Required. The resource name of the parent location, in the
            format
            ``projects/{project_id_or_number}/locations/{location_id}``
        page_size (int):
            Optional. The maximum number of metadata jobs
            to return. The service might return fewer jobs
            than this value. If unspecified, at most 10 jobs
            are returned. The maximum value is 1,000.
        page_token (str):
            Optional. The page token received from a previous
            ``ListMetadataJobs`` call. Provide this token to retrieve
            the subsequent page of results. When paginating, all other
            parameters that are provided to the ``ListMetadataJobs``
            request must match the call that provided the page token.
        filter (str):
            Optional. Filter request. Filters are case-sensitive. The
            service supports the following formats:

            - ``labels.key1 = "value1"``
            - ``labels:key1``
            - ``name = "value"``

            You can combine filters with ``AND``, ``OR``, and ``NOT``
            operators.
        order_by (str):
            Optional. The field to sort the results by, either ``name``
            or ``create_time``. If not specified, the ordering is
            undefined.
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


class ListMetadataJobsResponse(proto.Message):
    r"""List metadata jobs response.

    Attributes:
        metadata_jobs (MutableSequence[google.cloud.dataplex_v1.types.MetadataJob]):
            Metadata jobs under the specified parent
            location.
        next_page_token (str):
            A token to retrieve the next page of results.
            If there are no more results in the list, the
            value is empty.
        unreachable_locations (MutableSequence[str]):
            Locations that the service couldn't reach.
    """

    @property
    def raw_page(self):
        return self

    metadata_jobs: MutableSequence["MetadataJob"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="MetadataJob",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable_locations: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class CancelMetadataJobRequest(proto.Message):
    r"""Cancel metadata job request.

    Attributes:
        name (str):
            Required. The resource name of the job, in the format
            ``projects/{project_id_or_number}/locations/{location_id}/metadataJobs/{metadata_job_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class MetadataJob(proto.Message):
    r"""A metadata job resource.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. Identifier. The name of the resource that the
            configuration is applied to, in the format
            ``projects/{project_number}/locations/{location_id}/metadataJobs/{metadata_job_id}``.
        uid (str):
            Output only. A system-generated, globally
            unique ID for the metadata job. If the metadata
            job is deleted and then re-created with the same
            name, this ID is different.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the metadata job
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the metadata job
            was updated.
        labels (MutableMapping[str, str]):
            Optional. User-defined labels.
        type_ (google.cloud.dataplex_v1.types.MetadataJob.Type):
            Required. Metadata job type.
        import_spec (google.cloud.dataplex_v1.types.MetadataJob.ImportJobSpec):
            Import job specification.

            This field is a member of `oneof`_ ``spec``.
        export_spec (google.cloud.dataplex_v1.types.MetadataJob.ExportJobSpec):
            Export job specification.

            This field is a member of `oneof`_ ``spec``.
        import_result (google.cloud.dataplex_v1.types.MetadataJob.ImportJobResult):
            Output only. Import job result.

            This field is a member of `oneof`_ ``result``.
        export_result (google.cloud.dataplex_v1.types.MetadataJob.ExportJobResult):
            Output only. Export job result.

            This field is a member of `oneof`_ ``result``.
        status (google.cloud.dataplex_v1.types.MetadataJob.Status):
            Output only. Metadata job status.
    """

    class Type(proto.Enum):
        r"""Metadata job type.

        Values:
            TYPE_UNSPECIFIED (0):
                Unspecified.
            IMPORT (1):
                Import job.
            EXPORT (2):
                Export job.
        """

        TYPE_UNSPECIFIED = 0
        IMPORT = 1
        EXPORT = 2

    class ImportJobResult(proto.Message):
        r"""Results from a metadata import job.

        Attributes:
            deleted_entries (int):
                Output only. The total number of entries that
                were deleted.
            updated_entries (int):
                Output only. The total number of entries that
                were updated.
            created_entries (int):
                Output only. The total number of entries that
                were created.
            unchanged_entries (int):
                Output only. The total number of entries that
                were unchanged.
            recreated_entries (int):
                Output only. The total number of entries that
                were recreated.
            update_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. The time when the status was
                updated.
            deleted_entry_links (int):
                Output only. The total number of entry links
                that were successfully deleted.
            created_entry_links (int):
                Output only. The total number of entry links
                that were successfully created.
            unchanged_entry_links (int):
                Output only. The total number of entry links
                that were left unchanged.
        """

        deleted_entries: int = proto.Field(
            proto.INT64,
            number=1,
        )
        updated_entries: int = proto.Field(
            proto.INT64,
            number=2,
        )
        created_entries: int = proto.Field(
            proto.INT64,
            number=3,
        )
        unchanged_entries: int = proto.Field(
            proto.INT64,
            number=4,
        )
        recreated_entries: int = proto.Field(
            proto.INT64,
            number=6,
        )
        update_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=5,
            message=timestamp_pb2.Timestamp,
        )
        deleted_entry_links: int = proto.Field(
            proto.INT64,
            number=7,
        )
        created_entry_links: int = proto.Field(
            proto.INT64,
            number=8,
        )
        unchanged_entry_links: int = proto.Field(
            proto.INT64,
            number=9,
        )

    class ExportJobResult(proto.Message):
        r"""Summary results from a metadata export job. The results are a
        snapshot of the metadata at the time when the job was created.
        The exported entries are saved to a Cloud Storage bucket.

        Attributes:
            exported_entries (int):
                Output only. The number of entries that were
                exported.
            error_message (str):
                Output only. The error message if the
                metadata export job failed.
        """

        exported_entries: int = proto.Field(
            proto.INT64,
            number=1,
        )
        error_message: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class ImportJobSpec(proto.Message):
        r"""Job specification for a metadata import job.

        You can run the following kinds of metadata import jobs:

        - Full sync of entries with incremental import of their aspects.
          Supported for custom entries.
        - Incremental import of aspects only. Supported for aspects that
          belong to custom entries and system entries. For custom entries,
          you can modify both optional aspects and required aspects. For
          system entries, you can modify optional aspects.

        Attributes:
            source_storage_uri (str):
                Optional. The URI of a Cloud Storage bucket or folder
                (beginning with ``gs://`` and ending with ``/``) that
                contains the metadata import files for this job.

                A metadata import file defines the values to set for each of
                the entries and aspects in a metadata import job. For more
                information about how to create a metadata import file and
                the file requirements, see `Metadata import
                file <https://cloud.google.com/dataplex/docs/import-metadata#metadata-import-file>`__.

                You can provide multiple metadata import files in the same
                metadata job. The bucket or folder must contain at least one
                metadata import file, in JSON Lines format (either ``.json``
                or ``.jsonl`` file extension).

                In ``FULL`` entry sync mode, don't save the metadata import
                file in a folder named ``SOURCE_STORAGE_URI/deletions/``.

                **Caution**: If the metadata import file contains no data,
                all entries and aspects that belong to the job's scope are
                deleted.
            source_create_time (google.protobuf.timestamp_pb2.Timestamp):
                Optional. The time when the process that
                created the metadata import files began.
            scope (google.cloud.dataplex_v1.types.MetadataJob.ImportJobSpec.ImportJobScope):
                Required. A boundary on the scope of impact
                that the metadata import job can have.
            entry_sync_mode (google.cloud.dataplex_v1.types.MetadataJob.ImportJobSpec.SyncMode):
                Required. The sync mode for entries.
            aspect_sync_mode (google.cloud.dataplex_v1.types.MetadataJob.ImportJobSpec.SyncMode):
                Required. The sync mode for aspects.
            log_level (google.cloud.dataplex_v1.types.MetadataJob.ImportJobSpec.LogLevel):
                Optional. The level of logs to write to Cloud Logging for
                this job.

                Debug-level logs provide highly-detailed information for
                troubleshooting, but their increased verbosity could incur
                `additional
                costs <https://cloud.google.com/stackdriver/pricing>`__ that
                might not be merited for all jobs.

                If unspecified, defaults to ``INFO``.
        """

        class SyncMode(proto.Enum):
            r"""Specifies how the entries and aspects in a metadata import job are
            updated. For more information, see `Sync
            mode <https://cloud.google.com/dataplex/docs/import-metadata#sync-mode>`__.

            Values:
                SYNC_MODE_UNSPECIFIED (0):
                    Sync mode unspecified.
                FULL (1):
                    All resources in the job's scope are
                    modified. If a resource exists in Dataplex
                    Universal Catalog but isn't included in the
                    metadata import file, the resource is deleted
                    when you run the metadata job. Use this mode to
                    perform a full sync of the set of entries in the
                    job scope.

                    This sync mode is supported for entries.
                INCREMENTAL (2):
                    Only the resources that are explicitly
                    included in the metadata import file are
                    modified. Use this mode to modify a subset of
                    resources while leaving unreferenced resources
                    unchanged.

                    This sync mode is supported for aspects.
                NONE (3):
                    If entry sync mode is ``NONE``, then aspects are modified
                    according to the aspect sync mode. Other metadata that
                    belongs to entries in the job's scope isn't modified.

                    This sync mode is supported for entries.
            """

            SYNC_MODE_UNSPECIFIED = 0
            FULL = 1
            INCREMENTAL = 2
            NONE = 3

        class LogLevel(proto.Enum):
            r"""The level of logs to write to Cloud Logging for this job.

            Values:
                LOG_LEVEL_UNSPECIFIED (0):
                    Log level unspecified.
                DEBUG (1):
                    Debug-level logging. Captures detailed logs for each import
                    item. Use debug-level logging to troubleshoot issues with
                    specific import items. For example, use debug-level logging
                    to identify resources that are missing from the job scope,
                    entries or aspects that don't conform to the associated
                    entry type or aspect type, or other misconfigurations with
                    the metadata import file.

                    Depending on the size of your metadata job and the number of
                    logs that are generated, debug-level logging might incur
                    `additional
                    costs <https://cloud.google.com/stackdriver/pricing>`__.
                INFO (2):
                    Info-level logging. Captures logs at the
                    overall job level. Includes aggregate logs about
                    import items, but doesn't specify which import
                    item has an error.
            """

            LOG_LEVEL_UNSPECIFIED = 0
            DEBUG = 1
            INFO = 2

        class ImportJobScope(proto.Message):
            r"""A boundary on the scope of impact that the metadata import
            job can have.

            Attributes:
                entry_groups (MutableSequence[str]):
                    Required. The entry groups that are in scope for the import
                    job, specified as relative resource names in the format
                    ``projects/{project_number_or_id}/locations/{location_id}/entryGroups/{entry_group_id}``.
                    Only entries and aspects that belong to the specified entry
                    groups are affected by the job.

                    The entry groups and the job must be in the same location.
                entry_types (MutableSequence[str]):
                    Required. The entry types that are in scope for the import
                    job, specified as relative resource names in the format
                    ``projects/{project_number_or_id}/locations/{location_id}/entryTypes/{entry_type_id}``.
                    The job modifies only the entries and aspects that belong to
                    these entry types.

                    If the metadata import file attempts to modify an entry
                    whose type isn't included in this list, the import job is
                    halted before modifying any entries or aspects.

                    The location of an entry type must either match the location
                    of the job, or the entry type must be global.
                aspect_types (MutableSequence[str]):
                    Optional. The aspect types that are in scope for the import
                    job, specified as relative resource names in the format
                    ``projects/{project_number_or_id}/locations/{location_id}/aspectTypes/{aspect_type_id}``.
                    The job modifies only the aspects that belong to these
                    aspect types.

                    This field is required when creating an aspect-only import
                    job.

                    If the metadata import file attempts to modify an aspect
                    whose type isn't included in this list, the import job is
                    halted before modifying any entries or aspects.

                    The location of an aspect type must either match the
                    location of the job, or the aspect type must be global.
                glossaries (MutableSequence[str]):
                    Optional. The glossaries that are in scope for the import
                    job, specified as relative resource names in the format
                    ``projects/{project_number_or_id}/locations/{location_id}/glossaries/{glossary_id}``.

                    While importing Business Glossary entries, the user must
                    provide glossaries. While importing entries, the user does
                    not have to provide glossaries. If the metadata import file
                    attempts to modify Business Glossary entries whose glossary
                    isn't included in this list, the import job will skip those
                    entries.

                    The location of a glossary must either match the location of
                    the job, or the glossary must be global.
                entry_link_types (MutableSequence[str]):
                    Optional. The entry link types that are in scope for the
                    import job, specified as relative resource names in the
                    format
                    ``projects/{project_number_or_id}/locations/{location_id}/entryLinkTypes/{entry_link_type_id}``.
                    The job modifies only the entryLinks that belong to these
                    entry link types.

                    If the metadata import file attempts to create or delete an
                    entry link whose entry link type isn't included in this
                    list, the import job will skip those entry links.
                referenced_entry_scopes (MutableSequence[str]):
                    Optional. Defines the scope of entries that can be
                    referenced in the entry links.

                    Currently, projects are supported as valid scopes. Format:
                    ``projects/{project_number_or_id}``

                    If the metadata import file attempts to create an entry link
                    which references an entry that is not in the scope, the
                    import job will skip that entry link.
            """

            entry_groups: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=1,
            )
            entry_types: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=2,
            )
            aspect_types: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=3,
            )
            glossaries: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=4,
            )
            entry_link_types: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=5,
            )
            referenced_entry_scopes: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=6,
            )

        source_storage_uri: str = proto.Field(
            proto.STRING,
            number=1,
        )
        source_create_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=5,
            message=timestamp_pb2.Timestamp,
        )
        scope: "MetadataJob.ImportJobSpec.ImportJobScope" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="MetadataJob.ImportJobSpec.ImportJobScope",
        )
        entry_sync_mode: "MetadataJob.ImportJobSpec.SyncMode" = proto.Field(
            proto.ENUM,
            number=3,
            enum="MetadataJob.ImportJobSpec.SyncMode",
        )
        aspect_sync_mode: "MetadataJob.ImportJobSpec.SyncMode" = proto.Field(
            proto.ENUM,
            number=4,
            enum="MetadataJob.ImportJobSpec.SyncMode",
        )
        log_level: "MetadataJob.ImportJobSpec.LogLevel" = proto.Field(
            proto.ENUM,
            number=6,
            enum="MetadataJob.ImportJobSpec.LogLevel",
        )

    class ExportJobSpec(proto.Message):
        r"""Job specification for a metadata export job.

        Attributes:
            scope (google.cloud.dataplex_v1.types.MetadataJob.ExportJobSpec.ExportJobScope):
                Required. The scope of the export job.
            output_path (str):
                Required. The root path of the Cloud Storage bucket to
                export the metadata to, in the format ``gs://{bucket}/``.
                You can optionally specify a custom prefix after the bucket
                name, in the format ``gs://{bucket}/{prefix}/``. The maximum
                length of the custom prefix is 128 characters. Dataplex
                Universal Catalog constructs the object path for the
                exported files by using the bucket name and prefix that you
                provide, followed by a system-generated path.

                The bucket must be in the same VPC Service Controls
                perimeter as the job.
        """

        class ExportJobScope(proto.Message):
            r"""The scope of the export job.

            Attributes:
                organization_level (bool):
                    Whether the metadata export job is an organization-level
                    export job.

                    - If ``true``, the job exports the entries from the same
                      organization and VPC Service Controls perimeter as the
                      job. The project that the job belongs to determines the
                      VPC Service Controls perimeter. If you set the job scope
                      to be at the organization level, then don't provide a list
                      of projects or entry groups.
                    - If ``false``, you must specify a list of projects or a
                      list of entry groups whose entries you want to export.

                    The default is ``false``.
                projects (MutableSequence[str]):
                    The projects whose metadata you want to export, in the
                    format ``projects/{project_id_or_number}``. Only the entries
                    from the specified projects are exported.

                    The projects must be in the same organization and VPC
                    Service Controls perimeter as the job.

                    If you set the job scope to be a list of projects, then set
                    the organization-level export flag to false and don't
                    provide a list of entry groups.
                entry_groups (MutableSequence[str]):
                    The entry groups whose metadata you want to export, in the
                    format
                    ``projects/{project_id_or_number}/locations/{location_id}/entryGroups/{entry_group_id}``.
                    Only the entries in the specified entry groups are exported.

                    The entry groups must be in the same location and the same
                    VPC Service Controls perimeter as the job.

                    If you set the job scope to be a list of entry groups, then
                    set the organization-level export flag to false and don't
                    provide a list of projects.
                entry_types (MutableSequence[str]):
                    The entry types that are in scope for the export job,
                    specified as relative resource names in the format
                    ``projects/{project_id_or_number}/locations/{location}/entryTypes/{entry_type_id}``.
                    Only entries that belong to the specified entry types are
                    affected by the job.
                aspect_types (MutableSequence[str]):
                    The aspect types that are in scope for the export job,
                    specified as relative resource names in the format
                    ``projects/{project_id_or_number}/locations/{location}/aspectTypes/{aspect_type_id}``.
                    Only aspects that belong to the specified aspect types are
                    affected by the job.
            """

            organization_level: bool = proto.Field(
                proto.BOOL,
                number=1,
            )
            projects: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=2,
            )
            entry_groups: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=3,
            )
            entry_types: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=4,
            )
            aspect_types: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=5,
            )

        scope: "MetadataJob.ExportJobSpec.ExportJobScope" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="MetadataJob.ExportJobSpec.ExportJobScope",
        )
        output_path: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class Status(proto.Message):
        r"""Metadata job status.

        Attributes:
            state (google.cloud.dataplex_v1.types.MetadataJob.Status.State):
                Output only. State of the metadata job.
            message (str):
                Output only. Message relating to the
                progression of a metadata job.
            completion_percent (int):
                Output only. Progress tracking.
            update_time (google.protobuf.timestamp_pb2.Timestamp):
                Output only. The time when the status was
                updated.
        """

        class State(proto.Enum):
            r"""State of a metadata job.

            Values:
                STATE_UNSPECIFIED (0):
                    State unspecified.
                QUEUED (1):
                    The job is queued.
                RUNNING (2):
                    The job is running.
                CANCELING (3):
                    The job is being canceled.
                CANCELED (4):
                    The job is canceled.
                SUCCEEDED (5):
                    The job succeeded.
                FAILED (6):
                    The job failed.
                SUCCEEDED_WITH_ERRORS (7):
                    The job completed with some errors.
            """

            STATE_UNSPECIFIED = 0
            QUEUED = 1
            RUNNING = 2
            CANCELING = 3
            CANCELED = 4
            SUCCEEDED = 5
            FAILED = 6
            SUCCEEDED_WITH_ERRORS = 7

        state: "MetadataJob.Status.State" = proto.Field(
            proto.ENUM,
            number=1,
            enum="MetadataJob.Status.State",
        )
        message: str = proto.Field(
            proto.STRING,
            number=2,
        )
        completion_percent: int = proto.Field(
            proto.INT32,
            number=3,
        )
        update_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=4,
            message=timestamp_pb2.Timestamp,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=6,
        enum=Type,
    )
    import_spec: ImportJobSpec = proto.Field(
        proto.MESSAGE,
        number=100,
        oneof="spec",
        message=ImportJobSpec,
    )
    export_spec: ExportJobSpec = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="spec",
        message=ExportJobSpec,
    )
    import_result: ImportJobResult = proto.Field(
        proto.MESSAGE,
        number=200,
        oneof="result",
        message=ImportJobResult,
    )
    export_result: ExportJobResult = proto.Field(
        proto.MESSAGE,
        number=201,
        oneof="result",
        message=ExportJobResult,
    )
    status: Status = proto.Field(
        proto.MESSAGE,
        number=7,
        message=Status,
    )


class EntryLink(proto.Message):
    r"""EntryLink represents a link between two Entries.

    Attributes:
        name (str):
            Output only. Immutable. Identifier. The relative resource
            name of the Entry Link, of the form:
            ``projects/{project_id_or_number}/locations/{location_id}/entryGroups/{entry_group_id}/entryLinks/{entry_link_id}``
        entry_link_type (str):
            Required. Immutable. Relative resource name of the Entry
            Link Type used to create this Entry Link. For example:

            - Entry link between synonym terms in a glossary:
              ``projects/dataplex-types/locations/global/entryLinkTypes/synonym``
            - Entry link between related terms in a glossary:
              ``projects/dataplex-types/locations/global/entryLinkTypes/related``
            - Entry link between glossary terms and data assets:
              ``projects/dataplex-types/locations/global/entryLinkTypes/definition``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the Entry Link was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the Entry Link was
            last updated.
        aspects (MutableMapping[str, google.cloud.dataplex_v1.types.Aspect]):
            Optional. The aspects that are attached to the entry link.
            The format of the aspect key has to be the following:
            ``{project_id_or_number}.{location_id}.{aspect_type_id}``
            Currently, only a single aspect of a Dataplex-owned Aspect
            Type is allowed.
        entry_references (MutableSequence[google.cloud.dataplex_v1.types.EntryLink.EntryReference]):
            Required. Immutable. Specifies the Entries
            referenced in the Entry Link. There should be
            exactly two entry references.
    """

    class EntryReference(proto.Message):
        r"""Reference to the Entry that is linked through the Entry Link.

        Attributes:
            name (str):
                Required. Immutable. The relative resource name of the
                referenced Entry, of the form:
                ``projects/{project_id_or_number}/locations/{location_id}/entryGroups/{entry_group_id}/entries/{entry_id}``
            path (str):
                Immutable. The path in the Entry that is
                referenced in the Entry Link. Empty path denotes
                that the Entry itself is referenced in the Entry
                Link.
            type_ (google.cloud.dataplex_v1.types.EntryLink.EntryReference.Type):
                Required. Immutable. The reference type of
                the Entry.
        """

        class Type(proto.Enum):
            r"""Reference type of the Entry.

            Values:
                UNSPECIFIED (0):
                    Unspecified reference type. Implies that the
                    Entry is referenced in a non-directional Entry
                    Link.
                SOURCE (2):
                    The Entry is referenced as the source of the
                    directional Entry Link.
                TARGET (3):
                    The Entry is referenced as the target of the
                    directional Entry Link.
            """

            UNSPECIFIED = 0
            SOURCE = 2
            TARGET = 3

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        path: str = proto.Field(
            proto.STRING,
            number=2,
        )
        type_: "EntryLink.EntryReference.Type" = proto.Field(
            proto.ENUM,
            number=3,
            enum="EntryLink.EntryReference.Type",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    entry_link_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    aspects: MutableMapping[str, "Aspect"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=6,
        message="Aspect",
    )
    entry_references: MutableSequence[EntryReference] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message=EntryReference,
    )


class CreateEntryLinkRequest(proto.Message):
    r"""Request message for CreateEntryLink.

    Attributes:
        parent (str):
            Required. The resource name of the parent Entry Group:
            ``projects/{project_id_or_number}/locations/{location_id}/entryGroups/{entry_group_id}``.
        entry_link_id (str):
            Required. Entry Link identifier

            - Must contain only lowercase letters, numbers and hyphens.
            - Must start with a letter.
            - Must be between 1-63 characters.
            - Must end with a number or a letter.
            - Must be unique within the EntryGroup.
        entry_link (google.cloud.dataplex_v1.types.EntryLink):
            Required. Entry Link resource.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    entry_link_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    entry_link: "EntryLink" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="EntryLink",
    )


class UpdateEntryLinkRequest(proto.Message):
    r"""Request message for UpdateEntryLink method.

    Attributes:
        entry_link (google.cloud.dataplex_v1.types.EntryLink):
            Required. Entry Link resource.
        allow_missing (bool):
            Optional. If set to true and the entry link
            doesn't exist, the service will create it.
        aspect_keys (MutableSequence[str]):
            Optional. The map keys of the Aspects which the service
            should modify. It should be the aspect type reference in the
            format
            ``{project_id_or_number}.{location_id}.{aspect_type_id}``.

            If this field is left empty, the service treats it as
            specifying exactly those Aspects present in the request.
    """

    entry_link: "EntryLink" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="EntryLink",
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    aspect_keys: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )


class DeleteEntryLinkRequest(proto.Message):
    r"""Request message for DeleteEntryLink.

    Attributes:
        name (str):
            Required. The resource name of the Entry Link:
            ``projects/{project_id_or_number}/locations/{location_id}/entryGroups/{entry_group_id}/entryLinks/{entry_link_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class LookupEntryLinksRequest(proto.Message):
    r"""Request message for LookupEntryLinks.

    Attributes:
        name (str):
            Required. The project to which the request should be
            attributed to Format:
            ``projects/{project_id_or_number}/locations/{location_id}``.
        entry (str):
            Required. The resource name of the referred Entry. Format:
            ``projects/{project_id_or_number}/locations/{location_id}/entryGroups/{entry_group_id}/entries/{entry_id}``.
            Entry Links which references this entry will be returned in
            the response.
        entry_mode (google.cloud.dataplex_v1.types.LookupEntryLinksRequest.EntryMode):
            Mode of entry reference.
        entry_link_types (MutableSequence[str]):
            Entry link types to filter the response by.
            If empty, all entry link types will be returned.
            At most 10 entry link types can be specified.
        page_size (int):
            Maximum number of EntryLinks to return. The
            service may return fewer than this value. If
            unspecified, at most 10 EntryLinks will be
            returned. The maximum value is 10; values above
            10 will be coerced to 10.
        page_token (str):
            Page token received from a previous ``LookupEntryLinks``
            call. Provide this to retrieve the subsequent page. When
            paginating, all other parameters that are provided to the
            ``LookupEntryLinks`` request must match the call that
            provided the page token.
    """

    class EntryMode(proto.Enum):
        r"""Mode of entry reference.

        Values:
            ENTRY_MODE_UNSPECIFIED (0):
                Unspecified entry mode. Returns both
                directional and non-directional entry links
                which references the entry.
            SOURCE (1):
                Returns all directed entry links which
                references the entry as source.
            TARGET (2):
                Return all directed entry links which
                references the entry as target.
        """

        ENTRY_MODE_UNSPECIFIED = 0
        SOURCE = 1
        TARGET = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    entry: str = proto.Field(
        proto.STRING,
        number=2,
    )
    entry_mode: EntryMode = proto.Field(
        proto.ENUM,
        number=3,
        enum=EntryMode,
    )
    entry_link_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=5,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=6,
    )


class LookupEntryLinksResponse(proto.Message):
    r"""Response message for LookupEntryLinks.

    Attributes:
        entry_links (MutableSequence[google.cloud.dataplex_v1.types.EntryLink]):
            List of entry links that reference the
            specified entry.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    entry_links: MutableSequence["EntryLink"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="EntryLink",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetEntryLinkRequest(proto.Message):
    r"""Request message for GetEntryLink.

    Attributes:
        name (str):
            Required. The resource name of the Entry Link:
            ``projects/{project_id_or_number}/locations/{location_id}/entryGroups/{entry_group_id}/entryLinks/{entry_link_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class MetadataFeed(proto.Message):
    r"""MetadataFeed contains information related to the metadata
    feed.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the metadata feed, in the
            format
            ``projects/{project_id_or_number}/locations/{location_id}/metadataFeeds/{metadata_feed_id}``.
        uid (str):
            Output only. A system-generated, globally
            unique ID for the metadata job. If the metadata
            job is deleted and then re-created with the same
            name, this ID is different.
        scope (google.cloud.dataplex_v1.types.MetadataFeed.Scope):
            Required. The scope of the metadata feed.
            Only the in scope changes are published.
        filters (google.cloud.dataplex_v1.types.MetadataFeed.Filters):
            Optional. The filters of the metadata feed.
            Only the changes that match the filters are
            published.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the feed was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the feed was
            updated.
        labels (MutableMapping[str, str]):
            Optional. User-defined labels.
        pubsub_topic (str):
            Optional. The pubsub topic that you want the metadata feed
            messages to publish to. Please grant Dataplex service
            account the permission to publish messages to the topic. The
            service account is:
            service-{PROJECT_NUMBER}@gcp-sa-dataplex.iam.gserviceaccount.com.

            This field is a member of `oneof`_ ``endpoint``.
    """

    class Scope(proto.Message):
        r"""Scope defines the scope of the metadata feed.
        Scopes are exclusive. Only one of the scopes can be specified.

        Attributes:
            organization_level (bool):
                Optional. Whether the metadata feed is at the
                organization-level.

                - If ``true``, all changes happened to the entries in the
                  same organization as the feed are published.
                - If ``false``, you must specify a list of projects or a
                  list of entry groups whose entries you want to listen to.

                The default is ``false``.
            projects (MutableSequence[str]):
                Optional. The projects whose entries you want to listen to.
                Must be in the same organization as the feed. Must be in the
                format: ``projects/{project_id_or_number}``.
            entry_groups (MutableSequence[str]):
                Optional. The entry groups whose entries you want to listen
                to. Must be in the format:
                ``projects/{project_id_or_number}/locations/{location_id}/entryGroups/{entry_group_id}``.
        """

        organization_level: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        projects: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        entry_groups: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )

    class Filters(proto.Message):
        r"""Filters defines the type of changes that you want to listen
        to. You can have multiple entry type filters and multiple aspect
        type filters. All of the entry type filters are OR'ed together.
        All of the aspect type filters are OR'ed together.
        All of the entry type filters and aspect type filters are AND'ed
        together.

        Attributes:
            entry_types (MutableSequence[str]):
                Optional. The entry types that you want to listen to,
                specified as relative resource names in the format
                ``projects/{project_id_or_number}/locations/{location}/entryTypes/{entry_type_id}``.
                Only entries that belong to the specified entry types are
                published.
            aspect_types (MutableSequence[str]):
                Optional. The aspect types that you want to listen to.
                Depending on how the aspect is attached to the entry, in the
                format:
                ``projects/{project_id_or_number}/locations/{location}/aspectTypes/{aspect_type_id}``.
            change_types (MutableSequence[google.cloud.dataplex_v1.types.MetadataFeed.Filters.ChangeType]):
                Optional. The type of change that you want to
                listen to. If not specified, all changes are
                published.
        """

        class ChangeType(proto.Enum):
            r"""The type of change that you want to listen to.

            Values:
                CHANGE_TYPE_UNSPECIFIED (0):
                    Unspecified change type. Defaults to
                    UNSPECIFIED.
                CREATE (1):
                    The change is a create event.
                UPDATE (2):
                    The change is an update event.
                DELETE (3):
                    The change is a delete event.
            """

            CHANGE_TYPE_UNSPECIFIED = 0
            CREATE = 1
            UPDATE = 2
            DELETE = 3

        entry_types: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        aspect_types: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        change_types: MutableSequence["MetadataFeed.Filters.ChangeType"] = (
            proto.RepeatedField(
                proto.ENUM,
                number=3,
                enum="MetadataFeed.Filters.ChangeType",
            )
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    scope: Scope = proto.Field(
        proto.MESSAGE,
        number=3,
        message=Scope,
    )
    filters: Filters = proto.Field(
        proto.MESSAGE,
        number=4,
        message=Filters,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )
    pubsub_topic: str = proto.Field(
        proto.STRING,
        number=100,
        oneof="endpoint",
    )


class CreateMetadataFeedRequest(proto.Message):
    r"""Request message for CreateMetadataFeed.

    Attributes:
        parent (str):
            Required. The resource name of the parent location, in the
            format
            ``projects/{project_id_or_number}/locations/{location_id}``
        metadata_feed (google.cloud.dataplex_v1.types.MetadataFeed):
            Required. The metadata job resource.
        metadata_feed_id (str):
            Optional. The metadata job ID. If not provided, a unique ID
            is generated with the prefix ``metadata-job-``.
        validate_only (bool):
            Optional. The service validates the request
            without performing any mutations. The default is
            false.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    metadata_feed: "MetadataFeed" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="MetadataFeed",
    )
    metadata_feed_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class GetMetadataFeedRequest(proto.Message):
    r"""Request message for GetMetadataFeed.

    Attributes:
        name (str):
            Required. The resource name of the metadata feed, in the
            format
            ``projects/{project_id_or_number}/locations/{location_id}/MetadataFeeds/{metadata_feed_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListMetadataFeedsRequest(proto.Message):
    r"""Request message for ListMetadataFeedsRequest.

    Attributes:
        parent (str):
            Required. The resource name of the parent location, in the
            format
            ``projects/{project_id_or_number}/locations/{location_id}``
        page_size (int):
            Optional. The maximum number of metadata
            feeds to return. The service might return fewer
            feeds than this value. If unspecified, at most
            10 feeds are returned. The maximum value is
            1,000.
        page_token (str):
            Optional. The page token received from a previous
            ``ListMetadataFeeds`` call. Provide this token to retrieve
            the subsequent page of results. When paginating, all other
            parameters that are provided to the ``ListMetadataFeeds``
            request must match the call that provided the page token.
        filter (str):
            Optional. Filter request. Filters are case-sensitive. The
            service supports the following formats:

            - ``labels.key1 = "value1"``
            - ``labels:key1``
            - ``name = "value"``

            You can combine filters with ``AND``, ``OR``, and ``NOT``
            operators.
        order_by (str):
            Optional. The field to sort the results by, either ``name``
            or ``create_time``. If not specified, the ordering is
            undefined.
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


class ListMetadataFeedsResponse(proto.Message):
    r"""Response message for ListMetadataFeeds.

    Attributes:
        metadata_feeds (MutableSequence[google.cloud.dataplex_v1.types.MetadataFeed]):
            List of metadata feeds under the specified
            parent location.
        next_page_token (str):
            A token to retrieve the next page of results.
            If there are no more results in the list, the
            value is empty.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that the service
            couldn't reach.
    """

    @property
    def raw_page(self):
        return self

    metadata_feeds: MutableSequence["MetadataFeed"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="MetadataFeed",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class DeleteMetadataFeedRequest(proto.Message):
    r"""Request message for DeleteMetadataFeed.

    Attributes:
        name (str):
            Required. The resource name of the metadata feed, in the
            format
            ``projects/{project_id_or_number}/locations/{location_id}/MetadataFeeds/{metadata_feed_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateMetadataFeedRequest(proto.Message):
    r"""Request message for UpdateMetadataFeed.

    Attributes:
        metadata_feed (google.cloud.dataplex_v1.types.MetadataFeed):
            Required. Update description. Only fields specified in
            ``update_mask`` are updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Mask of fields to update.
        validate_only (bool):
            Optional. Only validate the request, but do
            not perform mutations. The default is false.
    """

    metadata_feed: "MetadataFeed" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="MetadataFeed",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
