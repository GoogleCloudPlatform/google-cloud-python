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
import proto  # type: ignore

from google.cloud.datacatalog_v1beta1.types import (
    common,
    search,
    table_spec,
    timestamps,
    usage,
)
from google.cloud.datacatalog_v1beta1.types import (
    gcs_fileset_spec as gcd_gcs_fileset_spec,
)
from google.cloud.datacatalog_v1beta1.types import schema as gcd_schema
from google.cloud.datacatalog_v1beta1.types import tags as gcd_tags

__protobuf__ = proto.module(
    package="google.cloud.datacatalog.v1beta1",
    manifest={
        "EntryType",
        "SearchCatalogRequest",
        "SearchCatalogResponse",
        "CreateEntryGroupRequest",
        "UpdateEntryGroupRequest",
        "GetEntryGroupRequest",
        "DeleteEntryGroupRequest",
        "ListEntryGroupsRequest",
        "ListEntryGroupsResponse",
        "CreateEntryRequest",
        "UpdateEntryRequest",
        "DeleteEntryRequest",
        "GetEntryRequest",
        "LookupEntryRequest",
        "Entry",
        "EntryGroup",
        "CreateTagTemplateRequest",
        "GetTagTemplateRequest",
        "UpdateTagTemplateRequest",
        "DeleteTagTemplateRequest",
        "CreateTagRequest",
        "UpdateTagRequest",
        "DeleteTagRequest",
        "CreateTagTemplateFieldRequest",
        "UpdateTagTemplateFieldRequest",
        "RenameTagTemplateFieldRequest",
        "RenameTagTemplateFieldEnumValueRequest",
        "DeleteTagTemplateFieldRequest",
        "ListTagsRequest",
        "ListTagsResponse",
        "ListEntriesRequest",
        "ListEntriesResponse",
    },
)


class EntryType(proto.Enum):
    r"""Entry resources in Data Catalog can be of different types e.g. a
    BigQuery Table entry is of type ``TABLE``. This enum describes all
    the possible types Data Catalog contains.

    Values:
        ENTRY_TYPE_UNSPECIFIED (0):
            Default unknown type.
        TABLE (2):
            Output only. The type of entry that has a
            GoogleSQL schema, including logical views.
        MODEL (5):
            Output only. The type of models.
            https://cloud.google.com/bigquery-ml/docs/bigqueryml-intro
        DATA_STREAM (3):
            Output only. An entry type which is used for
            streaming entries. Example: Pub/Sub topic.
        FILESET (4):
            An entry type which is a set of files or
            objects. Example: Cloud Storage fileset.
    """

    ENTRY_TYPE_UNSPECIFIED = 0
    TABLE = 2
    MODEL = 5
    DATA_STREAM = 3
    FILESET = 4


class SearchCatalogRequest(proto.Message):
    r"""Request message for
    [SearchCatalog][google.cloud.datacatalog.v1beta1.DataCatalog.SearchCatalog].

    Attributes:
        scope (google.cloud.datacatalog_v1beta1.types.SearchCatalogRequest.Scope):
            Required. The scope of this search request. A ``scope`` that
            has empty ``include_org_ids``, ``include_project_ids`` AND
            false ``include_gcp_public_datasets`` is considered invalid.
            Data Catalog will return an error in such a case.
        query (str):
            Optional. The query string in search query syntax. An empty
            query string will result in all data assets (in the
            specified scope) that the user has access to. Query strings
            can be simple as "x" or more qualified as:

            - name:x
            - column:x
            - description:y

            Note: Query tokens need to have a minimum of 3 characters
            for substring matching to work correctly. See `Data Catalog
            Search
            Syntax <https://cloud.google.com/data-catalog/docs/how-to/search-reference>`__
            for more information.
        page_size (int):
            Number of results in the search page. If <=0 then defaults
            to 10. Max limit for page_size is 1000. Throws an invalid
            argument for page_size > 1000.
        page_token (str):
            Optional. Pagination token returned in an earlier
            [SearchCatalogResponse.next_page_token][google.cloud.datacatalog.v1beta1.SearchCatalogResponse.next_page_token],
            which indicates that this is a continuation of a prior
            [SearchCatalogRequest][google.cloud.datacatalog.v1beta1.DataCatalog.SearchCatalog]
            call, and that the system should return the next page of
            data. If empty, the first page is returned.
        order_by (str):
            Specifies the ordering of results, currently supported
            case-sensitive choices are:

            - ``relevance``, only supports descending
            - ``last_modified_timestamp [asc|desc]``, defaults to
              descending if not specified
            - ``default`` that can only be descending

            If not specified, defaults to ``relevance`` descending.
    """

    class Scope(proto.Message):
        r"""The criteria that select the subspace used for query
        matching.

        Attributes:
            include_org_ids (MutableSequence[str]):
                The list of organization IDs to search
                within. To find your organization ID, follow
                instructions in
                https://cloud.google.com/resource-manager/docs/creating-managing-organization.
            include_project_ids (MutableSequence[str]):
                The list of project IDs to search within. To
                learn more about the distinction between project
                names/IDs/numbers, go to
                https://cloud.google.com/docs/overview/#projects.
            include_gcp_public_datasets (bool):
                If ``true``, include Google Cloud public datasets in the
                search results. Info on Google Cloud public datasets is
                available at https://cloud.google.com/public-datasets/. By
                default, Google Cloud public datasets are excluded.
            restricted_locations (MutableSequence[str]):
                Optional. The list of locations to search within.

                1. If empty, search will be performed in all locations;
                2. If any of the locations are NOT in the valid locations
                   list, error will be returned;
                3. Otherwise, search only the given locations for matching
                   results. Typical usage is to leave this field empty. When
                   a location is unreachable as returned in the
                   ``SearchCatalogResponse.unreachable`` field, users can
                   repeat the search request with this parameter set to get
                   additional information on the error.

                Valid locations:

                - asia-east1
                - asia-east2
                - asia-northeast1
                - asia-northeast2
                - asia-northeast3
                - asia-south1
                - asia-southeast1
                - australia-southeast1
                - eu
                - europe-north1
                - europe-west1
                - europe-west2
                - europe-west3
                - europe-west4
                - europe-west6
                - global
                - northamerica-northeast1
                - southamerica-east1
                - us
                - us-central1
                - us-east1
                - us-east4
                - us-west1
                - us-west2
        """

        include_org_ids: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        include_project_ids: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )
        include_gcp_public_datasets: bool = proto.Field(
            proto.BOOL,
            number=7,
        )
        restricted_locations: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=16,
        )

    scope: Scope = proto.Field(
        proto.MESSAGE,
        number=6,
        message=Scope,
    )
    query: str = proto.Field(
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
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class SearchCatalogResponse(proto.Message):
    r"""Response message for
    [SearchCatalog][google.cloud.datacatalog.v1beta1.DataCatalog.SearchCatalog].

    Attributes:
        results (MutableSequence[google.cloud.datacatalog_v1beta1.types.SearchCatalogResult]):
            Search results.
        total_size (int):
            The approximate total number of entries
            matched by the query.
        next_page_token (str):
            The token that can be used to retrieve the
            next page of results.
        unreachable (MutableSequence[str]):
            Unreachable locations. Search result does not include data
            from those locations. Users can get additional information
            on the error by repeating the search request with a more
            restrictive parameter -- setting the value for
            ``SearchDataCatalogRequest.scope.restricted_locations``.
    """

    @property
    def raw_page(self):
        return self

    results: MutableSequence[search.SearchCatalogResult] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=search.SearchCatalogResult,
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
        number=6,
    )


class CreateEntryGroupRequest(proto.Message):
    r"""Request message for
    [CreateEntryGroup][google.cloud.datacatalog.v1beta1.DataCatalog.CreateEntryGroup].

    Attributes:
        parent (str):
            Required. The name of the project this entry group is in.
            Example:

            - projects/{project_id}/locations/{location}

            Note that this EntryGroup and its child resources may not
            actually be stored in the location in this name.
        entry_group_id (str):
            Required. The id of the entry group to
            create. The id must begin with a letter or
            underscore, contain only English letters,
            numbers and underscores, and be at most 64
            characters.
        entry_group (google.cloud.datacatalog_v1beta1.types.EntryGroup):
            The entry group to create. Defaults to an
            empty entry group.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    entry_group_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    entry_group: "EntryGroup" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="EntryGroup",
    )


class UpdateEntryGroupRequest(proto.Message):
    r"""Request message for
    [UpdateEntryGroup][google.cloud.datacatalog.v1beta1.DataCatalog.UpdateEntryGroup].

    Attributes:
        entry_group (google.cloud.datacatalog_v1beta1.types.EntryGroup):
            Required. The updated entry group. "name"
            field must be set.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Names of fields whose values to overwrite on
            an entry group.
            If this parameter is absent or empty, all
            modifiable fields are overwritten. If such
            fields are non-required and omitted in the
            request body, their values are emptied.
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


class GetEntryGroupRequest(proto.Message):
    r"""Request message for
    [GetEntryGroup][google.cloud.datacatalog.v1beta1.DataCatalog.GetEntryGroup].

    Attributes:
        name (str):
            Required. The name of the entry group. For example,
            ``projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}``.
        read_mask (google.protobuf.field_mask_pb2.FieldMask):
            The fields to return. If not set or empty,
            all fields are returned.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    read_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteEntryGroupRequest(proto.Message):
    r"""Request message for
    [DeleteEntryGroup][google.cloud.datacatalog.v1beta1.DataCatalog.DeleteEntryGroup].

    Attributes:
        name (str):
            Required. The name of the entry group. For example,
            ``projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}``.
        force (bool):
            Optional. If true, deletes all entries in the
            entry group.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class ListEntryGroupsRequest(proto.Message):
    r"""Request message for
    [ListEntryGroups][google.cloud.datacatalog.v1beta1.DataCatalog.ListEntryGroups].

    Attributes:
        parent (str):
            Required. The name of the location that contains the entry
            groups, which can be provided in URL format. Example:

            - projects/{project_id}/locations/{location}
        page_size (int):
            Optional. The maximum number of items to return. Default is
            10. Max limit is 1000. Throws an invalid argument for
            ``page_size > 1000``.
        page_token (str):
            Optional. Token that specifies which page is
            requested. If empty, the first page is returned.
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


class ListEntryGroupsResponse(proto.Message):
    r"""Response message for
    [ListEntryGroups][google.cloud.datacatalog.v1beta1.DataCatalog.ListEntryGroups].

    Attributes:
        entry_groups (MutableSequence[google.cloud.datacatalog_v1beta1.types.EntryGroup]):
            EntryGroup details.
        next_page_token (str):
            Token to retrieve the next page of results.
            It is set to empty if no items remain in
            results.
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


class CreateEntryRequest(proto.Message):
    r"""Request message for
    [CreateEntry][google.cloud.datacatalog.v1beta1.DataCatalog.CreateEntry].

    Attributes:
        parent (str):
            Required. The name of the entry group this entry is in.
            Example:

            - projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}

            Note that this Entry and its child resources may not
            actually be stored in the location in this name.
        entry_id (str):
            Required. The id of the entry to create.
        entry (google.cloud.datacatalog_v1beta1.types.Entry):
            Required. The entry to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    entry_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    entry: "Entry" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Entry",
    )


class UpdateEntryRequest(proto.Message):
    r"""Request message for
    [UpdateEntry][google.cloud.datacatalog.v1beta1.DataCatalog.UpdateEntry].

    Attributes:
        entry (google.cloud.datacatalog_v1beta1.types.Entry):
            Required. The updated entry. The "name" field
            must be set.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Names of fields whose values to overwrite on an entry.

            If this parameter is absent or empty, all modifiable fields
            are overwritten. If such fields are non-required and omitted
            in the request body, their values are emptied.

            The following fields are modifiable:

            - For entries with type ``DATA_STREAM``:

              - ``schema``

            - For entries with type ``FILESET``:

              - ``schema``
              - ``display_name``
              - ``description``
              - ``gcs_fileset_spec``
              - ``gcs_fileset_spec.file_patterns``

            - For entries with ``user_specified_type``:

              - ``schema``
              - ``display_name``
              - ``description``
              - ``user_specified_type``
              - ``user_specified_system``
              - ``linked_resource``
              - ``source_system_timestamps``
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


class DeleteEntryRequest(proto.Message):
    r"""Request message for
    [DeleteEntry][google.cloud.datacatalog.v1beta1.DataCatalog.DeleteEntry].

    Attributes:
        name (str):
            Required. The name of the entry. Example:

            - projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetEntryRequest(proto.Message):
    r"""Request message for
    [GetEntry][google.cloud.datacatalog.v1beta1.DataCatalog.GetEntry].

    Attributes:
        name (str):
            Required. The name of the entry. Example:

            - projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class LookupEntryRequest(proto.Message):
    r"""Request message for
    [LookupEntry][google.cloud.datacatalog.v1beta1.DataCatalog.LookupEntry].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        linked_resource (str):
            The full name of the Google Cloud Platform resource the Data
            Catalog entry represents. See:
            https://cloud.google.com/apis/design/resource_names#full_resource_name.
            Full names are case-sensitive.

            Examples:

            - //bigquery.googleapis.com/projects/projectId/datasets/datasetId/tables/tableId
            - //pubsub.googleapis.com/projects/projectId/topics/topicId

            This field is a member of `oneof`_ ``target_name``.
        sql_resource (str):
            The SQL name of the entry. SQL names are case-sensitive.

            Examples:

            - ``pubsub.project_id.topic_id``
            - :literal:`pubsub.project_id.`topic.id.with.dots\``
            - ``bigquery.table.project_id.dataset_id.table_id``
            - ``bigquery.dataset.project_id.dataset_id``
            - ``datacatalog.entry.project_id.location_id.entry_group_id.entry_id``

            ``*_id``\ s should satisfy the GoogleSQL rules for
            identifiers.
            https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical.

            This field is a member of `oneof`_ ``target_name``.
    """

    linked_resource: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="target_name",
    )
    sql_resource: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="target_name",
    )


class Entry(proto.Message):
    r"""Entry Metadata. A Data Catalog Entry resource represents another
    resource in Google Cloud Platform (such as a BigQuery dataset or a
    Pub/Sub topic), or outside of Google Cloud Platform. Clients can use
    the ``linked_resource`` field in the Entry resource to refer to the
    original resource ID of the source system.

    An Entry resource contains resource details, such as its schema. An
    Entry can also be used to attach flexible metadata, such as a
    [Tag][google.cloud.datacatalog.v1beta1.Tag].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. Identifier. The Data Catalog resource name of
            the entry in URL format. Example:

            - projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id}

            Note that this Entry and its child resources may not
            actually be stored in the location in this name.
        linked_resource (str):
            The resource this metadata entry refers to.

            For Google Cloud Platform resources, ``linked_resource`` is
            the `full name of the
            resource <https://cloud.google.com/apis/design/resource_names#full_resource_name>`__.
            For example, the ``linked_resource`` for a table resource
            from BigQuery is:

            - //bigquery.googleapis.com/projects/projectId/datasets/datasetId/tables/tableId

            Output only when Entry is of type in the EntryType enum. For
            entries with user_specified_type, this field is optional and
            defaults to an empty string.
        type_ (google.cloud.datacatalog_v1beta1.types.EntryType):
            The type of the entry.
            Only used for Entries with types in the
            EntryType enum.

            This field is a member of `oneof`_ ``entry_type``.
        user_specified_type (str):
            Entry type if it does not fit any of the input-allowed
            values listed in ``EntryType`` enum above. When creating an
            entry, users should check the enum values first, if nothing
            matches the entry to be created, then provide a custom
            value, for example "my_special_type".
            ``user_specified_type`` strings must begin with a letter or
            underscore and can only contain letters, numbers, and
            underscores; are case insensitive; must be at least 1
            character and at most 64 characters long.

            Currently, only FILESET enum value is allowed. All other
            entries created through Data Catalog must use
            ``user_specified_type``.

            This field is a member of `oneof`_ ``entry_type``.
        integrated_system (google.cloud.datacatalog_v1beta1.types.IntegratedSystem):
            Output only. This field indicates the entry's
            source system that Data Catalog integrates with,
            such as BigQuery or Pub/Sub.

            This field is a member of `oneof`_ ``system``.
        user_specified_system (str):
            This field indicates the entry's source system that Data
            Catalog does not integrate with. ``user_specified_system``
            strings must begin with a letter or underscore and can only
            contain letters, numbers, and underscores; are case
            insensitive; must be at least 1 character and at most 64
            characters long.

            This field is a member of `oneof`_ ``system``.
        gcs_fileset_spec (google.cloud.datacatalog_v1beta1.types.GcsFilesetSpec):
            Specification that applies to a Cloud Storage
            fileset. This is only valid on entries of type
            FILESET.

            This field is a member of `oneof`_ ``type_spec``.
        bigquery_table_spec (google.cloud.datacatalog_v1beta1.types.BigQueryTableSpec):
            Specification that applies to a BigQuery table. This is only
            valid on entries of type ``TABLE``.

            This field is a member of `oneof`_ ``type_spec``.
        bigquery_date_sharded_spec (google.cloud.datacatalog_v1beta1.types.BigQueryDateShardedSpec):
            Specification for a group of BigQuery tables with name
            pattern ``[prefix]YYYYMMDD``. Context:
            https://cloud.google.com/bigquery/docs/partitioned-tables#partitioning_versus_sharding.

            This field is a member of `oneof`_ ``type_spec``.
        display_name (str):
            Display information such as title and
            description. A short name to identify the entry,
            for example, "Analytics Data - Jan 2011".
            Default value is an empty string.
        description (str):
            Entry description, which can consist of
            several sentences or paragraphs that describe
            entry contents. Default value is an empty
            string.
        schema (google.cloud.datacatalog_v1beta1.types.Schema):
            Schema of the entry. An entry might not have
            any schema attached to it.
        source_system_timestamps (google.cloud.datacatalog_v1beta1.types.SystemTimestamps):
            Output only. Timestamps about the underlying resource, not
            about this Data Catalog entry. Output only when Entry is of
            type in the EntryType enum. For entries with
            user_specified_type, this field is optional and defaults to
            an empty timestamp.
        usage_signal (google.cloud.datacatalog_v1beta1.types.UsageSignal):
            Output only. Statistics on the usage level of
            the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    linked_resource: str = proto.Field(
        proto.STRING,
        number=9,
    )
    type_: "EntryType" = proto.Field(
        proto.ENUM,
        number=2,
        oneof="entry_type",
        enum="EntryType",
    )
    user_specified_type: str = proto.Field(
        proto.STRING,
        number=16,
        oneof="entry_type",
    )
    integrated_system: common.IntegratedSystem = proto.Field(
        proto.ENUM,
        number=17,
        oneof="system",
        enum=common.IntegratedSystem,
    )
    user_specified_system: str = proto.Field(
        proto.STRING,
        number=18,
        oneof="system",
    )
    gcs_fileset_spec: gcd_gcs_fileset_spec.GcsFilesetSpec = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="type_spec",
        message=gcd_gcs_fileset_spec.GcsFilesetSpec,
    )
    bigquery_table_spec: table_spec.BigQueryTableSpec = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="type_spec",
        message=table_spec.BigQueryTableSpec,
    )
    bigquery_date_sharded_spec: table_spec.BigQueryDateShardedSpec = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof="type_spec",
        message=table_spec.BigQueryDateShardedSpec,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    schema: gcd_schema.Schema = proto.Field(
        proto.MESSAGE,
        number=5,
        message=gcd_schema.Schema,
    )
    source_system_timestamps: timestamps.SystemTimestamps = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamps.SystemTimestamps,
    )
    usage_signal: usage.UsageSignal = proto.Field(
        proto.MESSAGE,
        number=13,
        message=usage.UsageSignal,
    )


class EntryGroup(proto.Message):
    r"""EntryGroup Metadata. An EntryGroup resource represents a logical
    grouping of zero or more Data Catalog
    [Entry][google.cloud.datacatalog.v1beta1.Entry] resources.

    Attributes:
        name (str):
            Identifier. The resource name of the entry group in URL
            format. Example:

            - projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}

            Note that this EntryGroup and its child resources may not
            actually be stored in the location in this name.
        display_name (str):
            A short name to identify the entry group, for
            example, "analytics data - jan 2011". Default
            value is an empty string.
        description (str):
            Entry group description, which can consist of
            several sentences or paragraphs that describe
            entry group contents. Default value is an empty
            string.
        data_catalog_timestamps (google.cloud.datacatalog_v1beta1.types.SystemTimestamps):
            Output only. Timestamps about this
            EntryGroup. Default value is empty timestamps.
    """

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
    data_catalog_timestamps: timestamps.SystemTimestamps = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamps.SystemTimestamps,
    )


class CreateTagTemplateRequest(proto.Message):
    r"""Request message for
    [CreateTagTemplate][google.cloud.datacatalog.v1beta1.DataCatalog.CreateTagTemplate].

    Attributes:
        parent (str):
            Required. The name of the project and the template location
            [region](https://cloud.google.com/data-catalog/docs/concepts/regions.

            Example:

            - projects/{project_id}/locations/us-central1
        tag_template_id (str):
            Required. The id of the tag template to
            create.
        tag_template (google.cloud.datacatalog_v1beta1.types.TagTemplate):
            Required. The tag template to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tag_template_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    tag_template: gcd_tags.TagTemplate = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcd_tags.TagTemplate,
    )


class GetTagTemplateRequest(proto.Message):
    r"""Request message for
    [GetTagTemplate][google.cloud.datacatalog.v1beta1.DataCatalog.GetTagTemplate].

    Attributes:
        name (str):
            Required. The name of the tag template. Example:

            - projects/{project_id}/locations/{location}/tagTemplates/{tag_template_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateTagTemplateRequest(proto.Message):
    r"""Request message for
    [UpdateTagTemplate][google.cloud.datacatalog.v1beta1.DataCatalog.UpdateTagTemplate].

    Attributes:
        tag_template (google.cloud.datacatalog_v1beta1.types.TagTemplate):
            Required. The template to update. The "name"
            field must be set.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Names of fields whose values to overwrite on a tag template.
            Currently, only ``display_name`` can be overwritten.

            In general, if this parameter is absent or empty, all
            modifiable fields are overwritten. If such fields are
            non-required and omitted in the request body, their values
            are emptied.
    """

    tag_template: gcd_tags.TagTemplate = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcd_tags.TagTemplate,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteTagTemplateRequest(proto.Message):
    r"""Request message for
    [DeleteTagTemplate][google.cloud.datacatalog.v1beta1.DataCatalog.DeleteTagTemplate].

    Attributes:
        name (str):
            Required. The name of the tag template to delete. Example:

            - projects/{project_id}/locations/{location}/tagTemplates/{tag_template_id}
        force (bool):
            Required. Currently, this field must always be set to
            ``true``. This confirms the deletion of any possible tags
            using this template. ``force = false`` will be supported in
            the future.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class CreateTagRequest(proto.Message):
    r"""Request message for
    [CreateTag][google.cloud.datacatalog.v1beta1.DataCatalog.CreateTag].

    Attributes:
        parent (str):
            Required. The name of the resource to attach this tag to.
            Tags can be attached to Entries. Example:

            - projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id}

            Note that this Tag and its child resources may not actually
            be stored in the location in this name.
        tag (google.cloud.datacatalog_v1beta1.types.Tag):
            Required. The tag to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tag: gcd_tags.Tag = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcd_tags.Tag,
    )


class UpdateTagRequest(proto.Message):
    r"""Request message for
    [UpdateTag][google.cloud.datacatalog.v1beta1.DataCatalog.UpdateTag].

    Attributes:
        tag (google.cloud.datacatalog_v1beta1.types.Tag):
            Required. The updated tag. The "name" field
            must be set.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Note: Currently, this parameter can only take ``"fields"``
            as value.

            Names of fields whose values to overwrite on a tag.
            Currently, a tag has the only modifiable field with the name
            ``fields``.

            In general, if this parameter is absent or empty, all
            modifiable fields are overwritten. If such fields are
            non-required and omitted in the request body, their values
            are emptied.
    """

    tag: gcd_tags.Tag = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcd_tags.Tag,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteTagRequest(proto.Message):
    r"""Request message for
    [DeleteTag][google.cloud.datacatalog.v1beta1.DataCatalog.DeleteTag].

    Attributes:
        name (str):
            Required. The name of the tag to delete. Example:

            - projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id}/tags/{tag_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateTagTemplateFieldRequest(proto.Message):
    r"""Request message for
    [CreateTagTemplateField][google.cloud.datacatalog.v1beta1.DataCatalog.CreateTagTemplateField].

    Attributes:
        parent (str):
            Required. The name of the project and the template location
            `region <https://cloud.google.com/data-catalog/docs/concepts/regions>`__.

            Example:

            - projects/{project_id}/locations/us-central1/tagTemplates/{tag_template_id}
        tag_template_field_id (str):
            Required. The ID of the tag template field to create. Field
            ids can contain letters (both uppercase and lowercase),
            numbers (0-9), underscores (\_) and dashes (-). Field IDs
            must be at least 1 character long and at most 128 characters
            long. Field IDs must also be unique within their template.
        tag_template_field (google.cloud.datacatalog_v1beta1.types.TagTemplateField):
            Required. The tag template field to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tag_template_field_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    tag_template_field: gcd_tags.TagTemplateField = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcd_tags.TagTemplateField,
    )


class UpdateTagTemplateFieldRequest(proto.Message):
    r"""Request message for
    [UpdateTagTemplateField][google.cloud.datacatalog.v1beta1.DataCatalog.UpdateTagTemplateField].

    Attributes:
        name (str):
            Required. The name of the tag template field. Example:

            - projects/{project_id}/locations/{location}/tagTemplates/{tag_template_id}/fields/{tag_template_field_id}
        tag_template_field (google.cloud.datacatalog_v1beta1.types.TagTemplateField):
            Required. The template to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Names of fields whose values to overwrite on an
            individual field of a tag template. The following fields are
            modifiable:

            - ``display_name``
            - ``type.enum_type``
            - ``is_required``

            If this parameter is absent or empty, all modifiable fields
            are overwritten. If such fields are non-required and omitted
            in the request body, their values are emptied with one
            exception: when updating an enum type, the provided values
            are merged with the existing values. Therefore, enum values
            can only be added, existing enum values cannot be deleted or
            renamed.

            Additionally, updating a template field from optional to
            required is *not* allowed.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tag_template_field: gcd_tags.TagTemplateField = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcd_tags.TagTemplateField,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


class RenameTagTemplateFieldRequest(proto.Message):
    r"""Request message for
    [RenameTagTemplateField][google.cloud.datacatalog.v1beta1.DataCatalog.RenameTagTemplateField].

    Attributes:
        name (str):
            Required. The name of the tag template. Example:

            - projects/{project_id}/locations/{location}/tagTemplates/{tag_template_id}/fields/{tag_template_field_id}
        new_tag_template_field_id (str):
            Required. The new ID of this tag template field. For
            example, ``my_new_field``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    new_tag_template_field_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RenameTagTemplateFieldEnumValueRequest(proto.Message):
    r"""Request message for
    [RenameTagTemplateFieldEnumValue][google.cloud.datacatalog.v1.DataCatalog.RenameTagTemplateFieldEnumValue].

    Attributes:
        name (str):
            Required. The name of the enum field value. Example:

            - projects/{project_id}/locations/{location}/tagTemplates/{tag_template_id}/fields/{tag_template_field_id}/enumValues/{enum_value_display_name}
        new_enum_value_display_name (str):
            Required. The new display name of the enum value. For
            example, ``my_new_enum_value``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    new_enum_value_display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteTagTemplateFieldRequest(proto.Message):
    r"""Request message for
    [DeleteTagTemplateField][google.cloud.datacatalog.v1beta1.DataCatalog.DeleteTagTemplateField].

    Attributes:
        name (str):
            Required. The name of the tag template field to delete.
            Example:

            - projects/{project_id}/locations/{location}/tagTemplates/{tag_template_id}/fields/{tag_template_field_id}
        force (bool):
            Required. Currently, this field must always be set to
            ``true``. This confirms the deletion of this field from any
            tags using this field. ``force = false`` will be supported
            in the future.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class ListTagsRequest(proto.Message):
    r"""Request message for
    [ListTags][google.cloud.datacatalog.v1beta1.DataCatalog.ListTags].

    Attributes:
        parent (str):
            Required. The name of the Data Catalog resource to list the
            tags of. The resource could be an
            [Entry][google.cloud.datacatalog.v1beta1.Entry] or an
            [EntryGroup][google.cloud.datacatalog.v1beta1.EntryGroup].

            Examples:

            - projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}
            - projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id}
        page_size (int):
            The maximum number of tags to return. Default
            is 10. Max limit is 1000.
        page_token (str):
            Token that specifies which page is requested.
            If empty, the first page is returned.
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


class ListTagsResponse(proto.Message):
    r"""Response message for
    [ListTags][google.cloud.datacatalog.v1beta1.DataCatalog.ListTags].

    Attributes:
        tags (MutableSequence[google.cloud.datacatalog_v1beta1.types.Tag]):
            [Tag][google.cloud.datacatalog.v1beta1.Tag] details.
        next_page_token (str):
            Token to retrieve the next page of results.
            It is set to empty if no items remain in
            results.
    """

    @property
    def raw_page(self):
        return self

    tags: MutableSequence[gcd_tags.Tag] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcd_tags.Tag,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListEntriesRequest(proto.Message):
    r"""Request message for
    [ListEntries][google.cloud.datacatalog.v1beta1.DataCatalog.ListEntries].

    Attributes:
        parent (str):
            Required. The name of the entry group that contains the
            entries, which can be provided in URL format. Example:

            - projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}
        page_size (int):
            The maximum number of items to return. Default is 10. Max
            limit is 1000. Throws an invalid argument for
            ``page_size > 1000``.
        page_token (str):
            Token that specifies which page is requested.
            If empty, the first page is returned.
        read_mask (google.protobuf.field_mask_pb2.FieldMask):
            The fields to return for each Entry. If not set or empty,
            all fields are returned. For example, setting read_mask to
            contain only one path "name" will cause ListEntries to
            return a list of Entries with only "name" field.
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
    read_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=4,
        message=field_mask_pb2.FieldMask,
    )


class ListEntriesResponse(proto.Message):
    r"""Response message for
    [ListEntries][google.cloud.datacatalog.v1beta1.DataCatalog.ListEntries].

    Attributes:
        entries (MutableSequence[google.cloud.datacatalog_v1beta1.types.Entry]):
            Entry details.
        next_page_token (str):
            Token to retrieve the next page of results.
            It is set to empty if no items remain in
            results.
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


__all__ = tuple(sorted(__protobuf__.manifest))
