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
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.datacatalog_v1.types import (
    bigquery,
    common,
    dataplex_spec,
    search,
    table_spec,
    timestamps,
    usage,
)
from google.cloud.datacatalog_v1.types import data_source as gcd_data_source
from google.cloud.datacatalog_v1.types import gcs_fileset_spec as gcd_gcs_fileset_spec
from google.cloud.datacatalog_v1.types import schema as gcd_schema
from google.cloud.datacatalog_v1.types import tags as gcd_tags

__protobuf__ = proto.module(
    package="google.cloud.datacatalog.v1",
    manifest={
        "EntryType",
        "TagTemplateMigration",
        "CatalogUIExperience",
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
        "DatabaseTableSpec",
        "FilesetSpec",
        "DataSourceConnectionSpec",
        "RoutineSpec",
        "DatasetSpec",
        "SqlDatabaseSystemSpec",
        "LookerSystemSpec",
        "CloudBigtableSystemSpec",
        "CloudBigtableInstanceSpec",
        "ServiceSpec",
        "VertexModelSourceInfo",
        "VertexModelSpec",
        "VertexDatasetSpec",
        "ModelSpec",
        "FeatureOnlineStoreSpec",
        "BusinessContext",
        "EntryOverview",
        "Contacts",
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
        "ReconcileTagsRequest",
        "ReconcileTagsResponse",
        "ReconcileTagsMetadata",
        "ListEntriesRequest",
        "ListEntriesResponse",
        "StarEntryRequest",
        "StarEntryResponse",
        "UnstarEntryRequest",
        "UnstarEntryResponse",
        "ImportEntriesRequest",
        "ImportEntriesResponse",
        "ImportEntriesMetadata",
        "ModifyEntryOverviewRequest",
        "ModifyEntryContactsRequest",
        "SetConfigRequest",
        "RetrieveConfigRequest",
        "RetrieveEffectiveConfigRequest",
        "OrganizationConfig",
        "MigrationConfig",
    },
)


class EntryType(proto.Enum):
    r"""Metadata automatically ingested from Google Cloud resources like
    BigQuery tables or Pub/Sub topics always uses enum values from
    ``EntryType`` as the type of entry.

    Other sources of metadata like Hive or Oracle databases can identify
    the type by either using one of the enum values from ``EntryType``
    (for example, ``FILESET`` for a Cloud Storage fileset) or specifying
    a custom value using the ```Entry`` <#resource:-entry>`__ field
    ``user_specified_type``. For more information, see `Surface files
    from Cloud Storage with fileset
    entries </data-catalog/docs/how-to/filesets>`__ or `Create custom
    entries for your data
    sources </data-catalog/docs/how-to/custom-entries>`__.

    Values:
        ENTRY_TYPE_UNSPECIFIED (0):
            Default unknown type.
        TABLE (2):
            The entry type that has a GoogleSQL schema,
            including logical views.
        MODEL (5):
            The type of models.

            For more information, see `Supported models in BigQuery
            ML </bigquery/docs/bqml-introduction#supported_models>`__.
        DATA_STREAM (3):
            An entry type for streaming entries. For
            example, a Pub/Sub topic.
        FILESET (4):
            An entry type for a set of files or objects.
            For example, a Cloud Storage fileset.
        CLUSTER (6):
            A group of servers that work together. For
            example, a Kafka cluster.
        DATABASE (7):
            A database.
        DATA_SOURCE_CONNECTION (8):
            Connection to a data source. For example, a
            BigQuery connection.
        ROUTINE (9):
            Routine, for example, a BigQuery routine.
        LAKE (10):
            A Dataplex lake.
        ZONE (11):
            A Dataplex zone.
        SERVICE (14):
            A service, for example, a Dataproc Metastore
            service.
        DATABASE_SCHEMA (15):
            Schema within a relational database.
        DASHBOARD (16):
            A Dashboard, for example from Looker.
        EXPLORE (17):
            A Looker Explore.

            For more information, see [Looker Explore API]
            (https://developers.looker.com/api/explorer/4.0/methods/LookmlModel/lookml_model_explore).
        LOOK (18):
            A Looker Look.

            For more information, see [Looker Look API]
            (https://developers.looker.com/api/explorer/4.0/methods/Look).
        FEATURE_ONLINE_STORE (19):
            Feature Online Store resource in Vertex AI
            Feature Store.
        FEATURE_VIEW (20):
            Feature View resource in Vertex AI Feature
            Store.
        FEATURE_GROUP (21):
            Feature Group resource in Vertex AI Feature
            Store.
    """

    ENTRY_TYPE_UNSPECIFIED = 0
    TABLE = 2
    MODEL = 5
    DATA_STREAM = 3
    FILESET = 4
    CLUSTER = 6
    DATABASE = 7
    DATA_SOURCE_CONNECTION = 8
    ROUTINE = 9
    LAKE = 10
    ZONE = 11
    SERVICE = 14
    DATABASE_SCHEMA = 15
    DASHBOARD = 16
    EXPLORE = 17
    LOOK = 18
    FEATURE_ONLINE_STORE = 19
    FEATURE_VIEW = 20
    FEATURE_GROUP = 21


class TagTemplateMigration(proto.Enum):
    r"""Configuration related to the opt-in status for the migration
    of TagTemplates to Dataplex.

    Values:
        TAG_TEMPLATE_MIGRATION_UNSPECIFIED (0):
            Default value. Migration of Tag Templates
            from Data Catalog to Dataplex is not performed.
        TAG_TEMPLATE_MIGRATION_ENABLED (1):
            Migration of Tag Templates from Data Catalog
            to Dataplex is enabled.
        TAG_TEMPLATE_MIGRATION_DISABLED (2):
            Migration of Tag Templates from Data Catalog
            to Dataplex is disabled.
    """

    TAG_TEMPLATE_MIGRATION_UNSPECIFIED = 0
    TAG_TEMPLATE_MIGRATION_ENABLED = 1
    TAG_TEMPLATE_MIGRATION_DISABLED = 2


class CatalogUIExperience(proto.Enum):
    r"""Configuration related to the opt-in status for the UI switch
    to Dataplex.

    Values:
        CATALOG_UI_EXPERIENCE_UNSPECIFIED (0):
            Default value. The default UI is Dataplex.
        CATALOG_UI_EXPERIENCE_ENABLED (1):
            The UI is Dataplex.
        CATALOG_UI_EXPERIENCE_DISABLED (2):
            The UI is Data Catalog.
    """

    CATALOG_UI_EXPERIENCE_UNSPECIFIED = 0
    CATALOG_UI_EXPERIENCE_ENABLED = 1
    CATALOG_UI_EXPERIENCE_DISABLED = 2


class SearchCatalogRequest(proto.Message):
    r"""Request message for
    [SearchCatalog][google.cloud.datacatalog.v1.DataCatalog.SearchCatalog].

    Attributes:
        scope (google.cloud.datacatalog_v1.types.SearchCatalogRequest.Scope):
            Required. The scope of this search request.

            The ``scope`` is invalid if ``include_org_ids``,
            ``include_project_ids`` are empty AND
            ``include_gcp_public_datasets`` is set to ``false``. In this
            case, the request returns an error.
        query (str):
            Optional. The query string with a minimum of 3 characters
            and specific syntax. For more information, see `Data Catalog
            search
            syntax <https://cloud.google.com/data-catalog/docs/how-to/search-reference>`__.

            An empty query string returns all data assets (in the
            specified scope) that you have access to.

            A query string can be a simple ``xyz`` or qualified by
            predicates:

            - ``name:x``
            - ``column:y``
            - ``description:z``
        page_size (int):
            Upper bound on the number of results you can
            get in a single response.
            Can't be negative or 0, defaults to 10 in this
            case. The maximum number is 1000. If exceeded,
            throws an "invalid argument" exception.
        page_token (str):
            Optional. Pagination token that, if specified, returns the
            next page of search results. If empty, returns the first
            page.

            This token is returned in the
            [SearchCatalogResponse.next_page_token][google.cloud.datacatalog.v1.SearchCatalogResponse.next_page_token]
            field of the response to a previous
            [SearchCatalogRequest][google.cloud.datacatalog.v1.DataCatalog.SearchCatalog]
            call.
        order_by (str):
            Specifies the order of results.

            Currently supported case-sensitive values are:

            - ``relevance`` that can only be descending
            - ``last_modified_timestamp [asc|desc]`` with descending
              (``desc``) as default
            - ``default`` that can only be descending

            Search queries don't guarantee full recall. Results that
            match your query might not be returned, even in subsequent
            result pages. Additionally, returned (and not returned)
            results can vary if you repeat search queries. If you are
            experiencing recall issues and you don't have to fetch the
            results in any specific order, consider setting this
            parameter to ``default``.

            If this parameter is omitted, it defaults to the descending
            ``relevance``.
        admin_search (bool):
            Optional. If set, use searchAll permission granted on
            organizations from ``include_org_ids`` and projects from
            ``include_project_ids`` instead of the fine grained per
            resource permissions when filtering the search results. The
            only allowed ``order_by`` criteria for admin_search mode is
            ``default``. Using this flags guarantees a full recall of
            the search results.
    """

    class Scope(proto.Message):
        r"""The criteria that select the subspace used for query
        matching.

        Attributes:
            include_org_ids (MutableSequence[str]):
                The list of organization IDs to search within.

                To find your organization ID, follow the steps from
                [Creating and managing organizations]
                (/resource-manager/docs/creating-managing-organization).
            include_project_ids (MutableSequence[str]):
                The list of project IDs to search within.

                For more information on the distinction between project
                names, IDs, and numbers, see
                `Projects </docs/overview/#projects>`__.
            include_gcp_public_datasets (bool):
                If ``true``, include Google Cloud public datasets in search
                results. By default, they are excluded.

                See `Google Cloud Public Datasets </public-datasets>`__ for
                more information.
            restricted_locations (MutableSequence[str]):
                Optional. The list of locations to search within. If empty,
                all locations are searched.

                Returns an error if any location in the list isn't one of
                the `Supported
                regions <https://cloud.google.com/data-catalog/docs/concepts/regions#supported_regions>`__.

                If a location is unreachable, its name is returned in the
                ``SearchCatalogResponse.unreachable`` field. To get
                additional information on the error, repeat the search
                request and set the location name as the value of this
                parameter.
            starred_only (bool):
                Optional. If ``true``, search only among starred entries.

                By default, all results are returned, starred or not.
            include_public_tag_templates (bool):
                Optional. This field is deprecated. The
                search mechanism for public and private tag
                templates is the same.
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
        starred_only: bool = proto.Field(
            proto.BOOL,
            number=18,
        )
        include_public_tag_templates: bool = proto.Field(
            proto.BOOL,
            number=19,
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
    admin_search: bool = proto.Field(
        proto.BOOL,
        number=17,
    )


class SearchCatalogResponse(proto.Message):
    r"""Response message for
    [SearchCatalog][google.cloud.datacatalog.v1.DataCatalog.SearchCatalog].

    Attributes:
        results (MutableSequence[google.cloud.datacatalog_v1.types.SearchCatalogResult]):
            Search results.
        total_size (int):
            The approximate total number of entries
            matched by the query.
        next_page_token (str):
            Pagination token that can be used in
            subsequent calls to retrieve the next page of
            results.
        unreachable (MutableSequence[str]):
            Unreachable locations. Search results don't include data
            from those locations.

            To get additional information on an error, repeat the search
            request and restrict it to specific locations by setting the
            ``SearchCatalogRequest.scope.restricted_locations``
            parameter.
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
    [CreateEntryGroup][google.cloud.datacatalog.v1.DataCatalog.CreateEntryGroup].

    Attributes:
        parent (str):
            Required. The names of the project and
            location that the new entry group belongs to.

            Note: The entry group itself and its child
            resources might not be stored in the location
            specified in its name.
        entry_group_id (str):
            Required. The ID of the entry group to create.

            The ID must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (\_), and must start with a letter or
            underscore. The maximum size is 64 bytes when encoded in
            UTF-8.
        entry_group (google.cloud.datacatalog_v1.types.EntryGroup):
            The entry group to create. Defaults to empty.
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
    [UpdateEntryGroup][google.cloud.datacatalog.v1.DataCatalog.UpdateEntryGroup].

    Attributes:
        entry_group (google.cloud.datacatalog_v1.types.EntryGroup):
            Required. Updates for the entry group. The ``name`` field
            must be set.
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
    [GetEntryGroup][google.cloud.datacatalog.v1.DataCatalog.GetEntryGroup].

    Attributes:
        name (str):
            Required. The name of the entry group to get.
        read_mask (google.protobuf.field_mask_pb2.FieldMask):
            The fields to return. If empty or omitted,
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
    [DeleteEntryGroup][google.cloud.datacatalog.v1.DataCatalog.DeleteEntryGroup].

    Attributes:
        name (str):
            Required. The name of the entry group to
            delete.
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
    [ListEntryGroups][google.cloud.datacatalog.v1.DataCatalog.ListEntryGroups].

    Attributes:
        parent (str):
            Required. The name of the location that
            contains the entry groups to list.
            Can be provided as a URL.
        page_size (int):
            Optional. The maximum number of items to return.

            Default is 10. Maximum limit is 1000. Throws an invalid
            argument if ``page_size`` is greater than 1000.
        page_token (str):
            Optional. Pagination token that specifies the
            next page to return. If empty, returns the first
            page.
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
    [ListEntryGroups][google.cloud.datacatalog.v1.DataCatalog.ListEntryGroups].

    Attributes:
        entry_groups (MutableSequence[google.cloud.datacatalog_v1.types.EntryGroup]):
            Entry group details.
        next_page_token (str):
            Pagination token to specify in the next call
            to retrieve the next page of results. Empty if
            there are no more items.
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
    [CreateEntry][google.cloud.datacatalog.v1.DataCatalog.CreateEntry].

    Attributes:
        parent (str):
            Required. The name of the entry group this
            entry belongs to.
            Note: The entry itself and its child resources
            might not be stored in the location specified in
            its name.
        entry_id (str):
            Required. The ID of the entry to create.

            The ID must contain only letters (a-z, A-Z), numbers (0-9),
            and underscores (\_). The maximum size is 64 bytes when
            encoded in UTF-8.
        entry (google.cloud.datacatalog_v1.types.Entry):
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
    [UpdateEntry][google.cloud.datacatalog.v1.DataCatalog.UpdateEntry].

    Attributes:
        entry (google.cloud.datacatalog_v1.types.Entry):
            Required. Updates for the entry. The ``name`` field must be
            set.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Names of fields whose values to overwrite on an entry.

            If this parameter is absent or empty, all modifiable fields
            are overwritten. If such fields are non-required and omitted
            in the request body, their values are emptied.

            You can modify only the fields listed below.

            For entries with type ``DATA_STREAM``:

            - ``schema``

            For entries with type ``FILESET``:

            - ``schema``
            - ``display_name``
            - ``description``
            - ``gcs_fileset_spec``
            - ``gcs_fileset_spec.file_patterns``

            For entries with ``user_specified_type``:

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
    [DeleteEntry][google.cloud.datacatalog.v1.DataCatalog.DeleteEntry].

    Attributes:
        name (str):
            Required. The name of the entry to delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetEntryRequest(proto.Message):
    r"""Request message for
    [GetEntry][google.cloud.datacatalog.v1.DataCatalog.GetEntry].

    Attributes:
        name (str):
            Required. The name of the entry to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class LookupEntryRequest(proto.Message):
    r"""Request message for
    [LookupEntry][google.cloud.datacatalog.v1.DataCatalog.LookupEntry].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        linked_resource (str):
            The full name of the Google Cloud Platform resource the Data
            Catalog entry represents. For more information, see [Full
            Resource Name]
            (https://cloud.google.com/apis/design/resource_names#full_resource_name).

            Full names are case-sensitive. For example:

            - ``//bigquery.googleapis.com/projects/{PROJECT_ID}/datasets/{DATASET_ID}/tables/{TABLE_ID}``
            - ``//pubsub.googleapis.com/projects/{PROJECT_ID}/topics/{TOPIC_ID}``

            This field is a member of `oneof`_ ``target_name``.
        sql_resource (str):
            The SQL name of the entry. SQL names are case-sensitive.

            Examples:

            - ``pubsub.topic.{PROJECT_ID}.{TOPIC_ID}``
            - ``pubsub.topic.{PROJECT_ID}.``\ \`\ ``{TOPIC.ID.SEPARATED.WITH.DOTS}``\ \`
            - ``bigquery.table.{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}``
            - ``bigquery.dataset.{PROJECT_ID}.{DATASET_ID}``
            - ``datacatalog.entry.{PROJECT_ID}.{LOCATION_ID}.{ENTRY_GROUP_ID}.{ENTRY_ID}``

            Identifiers (``*_ID``) should comply with the [Lexical
            structure in GoogleSQL]
            (https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical).

            This field is a member of `oneof`_ ``target_name``.
        fully_qualified_name (str):
            `Fully Qualified Name
            (FQN) <https://cloud.google.com//data-catalog/docs/fully-qualified-names>`__
            of the resource.

            FQNs take two forms:

            - For non-regionalized resources:

              ``{SYSTEM}:{PROJECT}.{PATH_TO_RESOURCE_SEPARATED_WITH_DOTS}``

            - For regionalized resources:

              ``{SYSTEM}:{PROJECT}.{LOCATION_ID}.{PATH_TO_RESOURCE_SEPARATED_WITH_DOTS}``

            Example for a DPMS table:

            ``dataproc_metastore:{PROJECT_ID}.{LOCATION_ID}.{INSTANCE_ID}.{DATABASE_ID}.{TABLE_ID}``

            This field is a member of `oneof`_ ``target_name``.
        project (str):
            Project where the lookup should be performed. Required to
            lookup entry that is not a part of ``DPMS`` or ``DATAPLEX``
            ``integrated_system`` using its ``fully_qualified_name``.
            Ignored in other cases.
        location (str):
            Location where the lookup should be performed. Required to
            lookup entry that is not a part of ``DPMS`` or ``DATAPLEX``
            ``integrated_system`` using its ``fully_qualified_name``.
            Ignored in other cases.
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
    fully_qualified_name: str = proto.Field(
        proto.STRING,
        number=5,
        oneof="target_name",
    )
    project: str = proto.Field(
        proto.STRING,
        number=6,
    )
    location: str = proto.Field(
        proto.STRING,
        number=7,
    )


class Entry(proto.Message):
    r"""Entry metadata. A Data Catalog entry represents another resource in
    Google Cloud Platform (such as a BigQuery dataset or a Pub/Sub
    topic) or outside of it. You can use the ``linked_resource`` field
    in the entry resource to refer to the original resource ID of the
    source system.

    An entry resource contains resource details, for example, its
    schema. Additionally, you can attach flexible metadata to an entry
    in the form of a [Tag][google.cloud.datacatalog.v1.Tag].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. Identifier. The resource name of
            an entry in URL format.
            Note: The entry itself and its child resources
            might not be stored in the location specified in
            its name.
        linked_resource (str):
            The resource this metadata entry refers to.

            For Google Cloud Platform resources, ``linked_resource`` is
            the [Full Resource Name]
            (https://cloud.google.com/apis/design/resource_names#full_resource_name).
            For example, the ``linked_resource`` for a table resource
            from BigQuery is:

            ``//bigquery.googleapis.com/projects/{PROJECT_ID}/datasets/{DATASET_ID}/tables/{TABLE_ID}``

            Output only when the entry is one of the types in the
            ``EntryType`` enum.

            For entries with a ``user_specified_type``, this field is
            optional and defaults to an empty string.

            The resource string must contain only letters (a-z, A-Z),
            numbers (0-9), underscores (\_), periods (.), colons (:),
            slashes (/), dashes (-), and hashes (#). The maximum size is
            200 bytes when encoded in UTF-8.
        fully_qualified_name (str):
            `Fully Qualified Name
            (FQN) <https://cloud.google.com//data-catalog/docs/fully-qualified-names>`__
            of the resource. Set automatically for entries representing
            resources from synced systems. Settable only during
            creation, and read-only later. Can be used for search and
            lookup of the entries.
        type_ (google.cloud.datacatalog_v1.types.EntryType):
            The type of the entry.

            For details, see ```EntryType`` <#entrytype>`__.

            This field is a member of `oneof`_ ``entry_type``.
        user_specified_type (str):
            Custom entry type that doesn't match any of the values
            allowed for input and listed in the ``EntryType`` enum.

            When creating an entry, first check the type values in the
            enum. If there are no appropriate types for the new entry,
            provide a custom value, for example, ``my_special_type``.

            The ``user_specified_type`` string has the following
            limitations:

            - Is case insensitive.
            - Must begin with a letter or underscore.
            - Can only contain letters, numbers, and underscores.
            - Must be at least 1 character and at most 64 characters
              long.

            This field is a member of `oneof`_ ``entry_type``.
        integrated_system (google.cloud.datacatalog_v1.types.IntegratedSystem):
            Output only. Indicates the entry's source
            system that Data Catalog integrates with, such
            as BigQuery, Pub/Sub, or Dataproc Metastore.

            This field is a member of `oneof`_ ``system``.
        user_specified_system (str):
            Indicates the entry's source system that Data Catalog
            doesn't automatically integrate with.

            The ``user_specified_system`` string has the following
            limitations:

            - Is case insensitive.
            - Must begin with a letter or underscore.
            - Can only contain letters, numbers, and underscores.
            - Must be at least 1 character and at most 64 characters
              long.

            This field is a member of `oneof`_ ``system``.
        sql_database_system_spec (google.cloud.datacatalog_v1.types.SqlDatabaseSystemSpec):
            Specification that applies to a relational database system.
            Only settable when ``user_specified_system`` is equal to
            ``SQL_DATABASE``

            This field is a member of `oneof`_ ``system_spec``.
        looker_system_spec (google.cloud.datacatalog_v1.types.LookerSystemSpec):
            Specification that applies to Looker sysstem. Only settable
            when ``user_specified_system`` is equal to ``LOOKER``

            This field is a member of `oneof`_ ``system_spec``.
        cloud_bigtable_system_spec (google.cloud.datacatalog_v1.types.CloudBigtableSystemSpec):
            Specification that applies to Cloud Bigtable system. Only
            settable when ``integrated_system`` is equal to
            ``CLOUD_BIGTABLE``

            This field is a member of `oneof`_ ``system_spec``.
        gcs_fileset_spec (google.cloud.datacatalog_v1.types.GcsFilesetSpec):
            Specification that applies to a Cloud Storage fileset. Valid
            only for entries with the ``FILESET`` type.

            This field is a member of `oneof`_ ``type_spec``.
        bigquery_table_spec (google.cloud.datacatalog_v1.types.BigQueryTableSpec):
            Output only. Specification that applies to a BigQuery table.
            Valid only for entries with the ``TABLE`` type.

            This field is a member of `oneof`_ ``type_spec``.
        bigquery_date_sharded_spec (google.cloud.datacatalog_v1.types.BigQueryDateShardedSpec):
            Output only. Specification for a group of BigQuery tables
            with the ``[prefix]YYYYMMDD`` name pattern.

            For more information, see [Introduction to partitioned
            tables]
            (https://cloud.google.com/bigquery/docs/partitioned-tables#partitioning_versus_sharding).

            This field is a member of `oneof`_ ``type_spec``.
        database_table_spec (google.cloud.datacatalog_v1.types.DatabaseTableSpec):
            Specification that applies to a table resource. Valid only
            for entries with the ``TABLE`` or ``EXPLORE`` type.

            This field is a member of `oneof`_ ``spec``.
        data_source_connection_spec (google.cloud.datacatalog_v1.types.DataSourceConnectionSpec):
            Specification that applies to a data source connection.
            Valid only for entries with the ``DATA_SOURCE_CONNECTION``
            type.

            This field is a member of `oneof`_ ``spec``.
        routine_spec (google.cloud.datacatalog_v1.types.RoutineSpec):
            Specification that applies to a user-defined function or
            procedure. Valid only for entries with the ``ROUTINE`` type.

            This field is a member of `oneof`_ ``spec``.
        dataset_spec (google.cloud.datacatalog_v1.types.DatasetSpec):
            Specification that applies to a dataset.

            This field is a member of `oneof`_ ``spec``.
        fileset_spec (google.cloud.datacatalog_v1.types.FilesetSpec):
            Specification that applies to a fileset resource. Valid only
            for entries with the ``FILESET`` type.

            This field is a member of `oneof`_ ``spec``.
        service_spec (google.cloud.datacatalog_v1.types.ServiceSpec):
            Specification that applies to a Service
            resource.

            This field is a member of `oneof`_ ``spec``.
        model_spec (google.cloud.datacatalog_v1.types.ModelSpec):
            Model specification.

            This field is a member of `oneof`_ ``spec``.
        feature_online_store_spec (google.cloud.datacatalog_v1.types.FeatureOnlineStoreSpec):
            FeatureonlineStore spec for Vertex AI Feature
            Store.

            This field is a member of `oneof`_ ``spec``.
        display_name (str):
            Display name of an entry.

            The maximum size is 500 bytes when encoded in
            UTF-8. Default value is an empty string.
        description (str):
            Entry description that can consist of several
            sentences or paragraphs that describe entry
            contents.

            The description must not contain Unicode
            non-characters as well as C0 and C1 control
            codes except tabs (HT), new lines (LF), carriage
            returns (CR), and page breaks (FF).
            The maximum size is 2000 bytes when encoded in
            UTF-8. Default value is an empty string.
        business_context (google.cloud.datacatalog_v1.types.BusinessContext):
            Business Context of the entry. Not supported
            for BigQuery datasets
        schema (google.cloud.datacatalog_v1.types.Schema):
            Schema of the entry. An entry might not have
            any schema attached to it.
        source_system_timestamps (google.cloud.datacatalog_v1.types.SystemTimestamps):
            Timestamps from the underlying resource, not from the Data
            Catalog entry.

            Output only when the entry has a system listed in the
            ``IntegratedSystem`` enum. For entries with
            ``user_specified_system``, this field is optional and
            defaults to an empty timestamp.
        usage_signal (google.cloud.datacatalog_v1.types.UsageSignal):
            Resource usage statistics.
        labels (MutableMapping[str, str]):
            Cloud labels attached to the entry.

            In Data Catalog, you can create and modify
            labels attached only to custom entries. Synced
            entries have unmodifiable labels that come from
            the source system.
        data_source (google.cloud.datacatalog_v1.types.DataSource):
            Output only. Physical location of the entry.
        personal_details (google.cloud.datacatalog_v1.types.PersonalDetails):
            Output only. Additional information related
            to the entry. Private to the current user.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    linked_resource: str = proto.Field(
        proto.STRING,
        number=9,
    )
    fully_qualified_name: str = proto.Field(
        proto.STRING,
        number=29,
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
    sql_database_system_spec: "SqlDatabaseSystemSpec" = proto.Field(
        proto.MESSAGE,
        number=39,
        oneof="system_spec",
        message="SqlDatabaseSystemSpec",
    )
    looker_system_spec: "LookerSystemSpec" = proto.Field(
        proto.MESSAGE,
        number=40,
        oneof="system_spec",
        message="LookerSystemSpec",
    )
    cloud_bigtable_system_spec: "CloudBigtableSystemSpec" = proto.Field(
        proto.MESSAGE,
        number=41,
        oneof="system_spec",
        message="CloudBigtableSystemSpec",
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
    database_table_spec: "DatabaseTableSpec" = proto.Field(
        proto.MESSAGE,
        number=24,
        oneof="spec",
        message="DatabaseTableSpec",
    )
    data_source_connection_spec: "DataSourceConnectionSpec" = proto.Field(
        proto.MESSAGE,
        number=27,
        oneof="spec",
        message="DataSourceConnectionSpec",
    )
    routine_spec: "RoutineSpec" = proto.Field(
        proto.MESSAGE,
        number=28,
        oneof="spec",
        message="RoutineSpec",
    )
    dataset_spec: "DatasetSpec" = proto.Field(
        proto.MESSAGE,
        number=32,
        oneof="spec",
        message="DatasetSpec",
    )
    fileset_spec: "FilesetSpec" = proto.Field(
        proto.MESSAGE,
        number=33,
        oneof="spec",
        message="FilesetSpec",
    )
    service_spec: "ServiceSpec" = proto.Field(
        proto.MESSAGE,
        number=42,
        oneof="spec",
        message="ServiceSpec",
    )
    model_spec: "ModelSpec" = proto.Field(
        proto.MESSAGE,
        number=43,
        oneof="spec",
        message="ModelSpec",
    )
    feature_online_store_spec: "FeatureOnlineStoreSpec" = proto.Field(
        proto.MESSAGE,
        number=45,
        oneof="spec",
        message="FeatureOnlineStoreSpec",
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    business_context: "BusinessContext" = proto.Field(
        proto.MESSAGE,
        number=37,
        message="BusinessContext",
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
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=14,
    )
    data_source: gcd_data_source.DataSource = proto.Field(
        proto.MESSAGE,
        number=20,
        message=gcd_data_source.DataSource,
    )
    personal_details: common.PersonalDetails = proto.Field(
        proto.MESSAGE,
        number=26,
        message=common.PersonalDetails,
    )


class DatabaseTableSpec(proto.Message):
    r"""Specification that applies to a table resource. Valid only for
    entries with the ``TABLE`` type.

    Attributes:
        type_ (google.cloud.datacatalog_v1.types.DatabaseTableSpec.TableType):
            Type of this table.
        dataplex_table (google.cloud.datacatalog_v1.types.DataplexTableSpec):
            Output only. Fields specific to a Dataplex
            table and present only in the Dataplex table
            entries.
        database_view_spec (google.cloud.datacatalog_v1.types.DatabaseTableSpec.DatabaseViewSpec):
            Spec what applies to tables that are actually
            views. Not set for "real" tables.
    """

    class TableType(proto.Enum):
        r"""Type of the table.

        Values:
            TABLE_TYPE_UNSPECIFIED (0):
                Default unknown table type.
            NATIVE (1):
                Native table.
            EXTERNAL (2):
                External table.
        """

        TABLE_TYPE_UNSPECIFIED = 0
        NATIVE = 1
        EXTERNAL = 2

    class DatabaseViewSpec(proto.Message):
        r"""Specification that applies to database view.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            view_type (google.cloud.datacatalog_v1.types.DatabaseTableSpec.DatabaseViewSpec.ViewType):
                Type of this view.
            base_table (str):
                Name of a singular table this view reflects
                one to one.

                This field is a member of `oneof`_ ``source_definition``.
            sql_query (str):
                SQL query used to generate this view.

                This field is a member of `oneof`_ ``source_definition``.
        """

        class ViewType(proto.Enum):
            r"""Concrete type of the view.

            Values:
                VIEW_TYPE_UNSPECIFIED (0):
                    Default unknown view type.
                STANDARD_VIEW (1):
                    Standard view.
                MATERIALIZED_VIEW (2):
                    Materialized view.
            """

            VIEW_TYPE_UNSPECIFIED = 0
            STANDARD_VIEW = 1
            MATERIALIZED_VIEW = 2

        view_type: "DatabaseTableSpec.DatabaseViewSpec.ViewType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="DatabaseTableSpec.DatabaseViewSpec.ViewType",
        )
        base_table: str = proto.Field(
            proto.STRING,
            number=2,
            oneof="source_definition",
        )
        sql_query: str = proto.Field(
            proto.STRING,
            number=3,
            oneof="source_definition",
        )

    type_: TableType = proto.Field(
        proto.ENUM,
        number=1,
        enum=TableType,
    )
    dataplex_table: dataplex_spec.DataplexTableSpec = proto.Field(
        proto.MESSAGE,
        number=2,
        message=dataplex_spec.DataplexTableSpec,
    )
    database_view_spec: DatabaseViewSpec = proto.Field(
        proto.MESSAGE,
        number=3,
        message=DatabaseViewSpec,
    )


class FilesetSpec(proto.Message):
    r"""Specification that applies to a fileset. Valid only for
    entries with the 'FILESET' type.

    Attributes:
        dataplex_fileset (google.cloud.datacatalog_v1.types.DataplexFilesetSpec):
            Fields specific to a Dataplex fileset and
            present only in the Dataplex fileset entries.
    """

    dataplex_fileset: dataplex_spec.DataplexFilesetSpec = proto.Field(
        proto.MESSAGE,
        number=1,
        message=dataplex_spec.DataplexFilesetSpec,
    )


class DataSourceConnectionSpec(proto.Message):
    r"""Specification that applies to a data source connection. Valid only
    for entries with the ``DATA_SOURCE_CONNECTION`` type. Only one of
    internal specs can be set at the time, and cannot be changed later.

    Attributes:
        bigquery_connection_spec (google.cloud.datacatalog_v1.types.BigQueryConnectionSpec):
            Output only. Fields specific to BigQuery
            connections.
    """

    bigquery_connection_spec: bigquery.BigQueryConnectionSpec = proto.Field(
        proto.MESSAGE,
        number=1,
        message=bigquery.BigQueryConnectionSpec,
    )


class RoutineSpec(proto.Message):
    r"""Specification that applies to a routine. Valid only for entries with
    the ``ROUTINE`` type.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        routine_type (google.cloud.datacatalog_v1.types.RoutineSpec.RoutineType):
            The type of the routine.
        language (str):
            The language the routine is written in. The exact value
            depends on the source system. For BigQuery routines,
            possible values are:

            - ``SQL``
            - ``JAVASCRIPT``
        routine_arguments (MutableSequence[google.cloud.datacatalog_v1.types.RoutineSpec.Argument]):
            Arguments of the routine.
        return_type (str):
            Return type of the argument. The exact value
            depends on the source system and the language.
        definition_body (str):
            The body of the routine.
        bigquery_routine_spec (google.cloud.datacatalog_v1.types.BigQueryRoutineSpec):
            Fields specific for BigQuery routines.

            This field is a member of `oneof`_ ``system_spec``.
    """

    class RoutineType(proto.Enum):
        r"""The fine-grained type of the routine.

        Values:
            ROUTINE_TYPE_UNSPECIFIED (0):
                Unspecified type.
            SCALAR_FUNCTION (1):
                Non-builtin permanent scalar function.
            PROCEDURE (2):
                Stored procedure.
        """

        ROUTINE_TYPE_UNSPECIFIED = 0
        SCALAR_FUNCTION = 1
        PROCEDURE = 2

    class Argument(proto.Message):
        r"""Input or output argument of a function or stored procedure.

        Attributes:
            name (str):
                The name of the argument. A return argument
                of a function might not have a name.
            mode (google.cloud.datacatalog_v1.types.RoutineSpec.Argument.Mode):
                Specifies whether the argument is input or
                output.
            type_ (str):
                Type of the argument. The exact value depends
                on the source system and the language.
        """

        class Mode(proto.Enum):
            r"""The input or output mode of the argument.

            Values:
                MODE_UNSPECIFIED (0):
                    Unspecified mode.
                IN (1):
                    The argument is input-only.
                OUT (2):
                    The argument is output-only.
                INOUT (3):
                    The argument is both an input and an output.
            """

            MODE_UNSPECIFIED = 0
            IN = 1
            OUT = 2
            INOUT = 3

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        mode: "RoutineSpec.Argument.Mode" = proto.Field(
            proto.ENUM,
            number=2,
            enum="RoutineSpec.Argument.Mode",
        )
        type_: str = proto.Field(
            proto.STRING,
            number=3,
        )

    routine_type: RoutineType = proto.Field(
        proto.ENUM,
        number=1,
        enum=RoutineType,
    )
    language: str = proto.Field(
        proto.STRING,
        number=2,
    )
    routine_arguments: MutableSequence[Argument] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=Argument,
    )
    return_type: str = proto.Field(
        proto.STRING,
        number=4,
    )
    definition_body: str = proto.Field(
        proto.STRING,
        number=5,
    )
    bigquery_routine_spec: bigquery.BigQueryRoutineSpec = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="system_spec",
        message=bigquery.BigQueryRoutineSpec,
    )


class DatasetSpec(proto.Message):
    r"""Specification that applies to a dataset. Valid only for entries with
    the ``DATASET`` type.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        vertex_dataset_spec (google.cloud.datacatalog_v1.types.VertexDatasetSpec):
            Vertex AI Dataset specific fields

            This field is a member of `oneof`_ ``system_spec``.
    """

    vertex_dataset_spec: "VertexDatasetSpec" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="system_spec",
        message="VertexDatasetSpec",
    )


class SqlDatabaseSystemSpec(proto.Message):
    r"""Specification that applies to entries that are part ``SQL_DATABASE``
    system (user_specified_type)

    Attributes:
        sql_engine (str):
            SQL Database Engine. enum SqlEngine { UNDEFINED = 0; MY_SQL
            = 1; POSTGRE_SQL = 2; SQL_SERVER = 3; } Engine of the
            enclosing database instance.
        database_version (str):
            Version of the database engine.
        instance_host (str):
            Host of the SQL database enum InstanceHost { UNDEFINED = 0;
            SELF_HOSTED = 1; CLOUD_SQL = 2; AMAZON_RDS = 3; AZURE_SQL =
            4; } Host of the enclousing database instance.
    """

    sql_engine: str = proto.Field(
        proto.STRING,
        number=1,
    )
    database_version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    instance_host: str = proto.Field(
        proto.STRING,
        number=3,
    )


class LookerSystemSpec(proto.Message):
    r"""Specification that applies to entries that are part ``LOOKER``
    system (user_specified_type)

    Attributes:
        parent_instance_id (str):
            ID of the parent Looker Instance. Empty if it does not
            exist. Example value: ``someinstance.looker.com``
        parent_instance_display_name (str):
            Name of the parent Looker Instance. Empty if
            it does not exist.
        parent_model_id (str):
            ID of the parent Model. Empty if it does not
            exist.
        parent_model_display_name (str):
            Name of the parent Model. Empty if it does
            not exist.
        parent_view_id (str):
            ID of the parent View. Empty if it does not
            exist.
        parent_view_display_name (str):
            Name of the parent View. Empty if it does not
            exist.
    """

    parent_instance_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    parent_instance_display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    parent_model_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    parent_model_display_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    parent_view_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    parent_view_display_name: str = proto.Field(
        proto.STRING,
        number=6,
    )


class CloudBigtableSystemSpec(proto.Message):
    r"""Specification that applies to all entries that are part of
    ``CLOUD_BIGTABLE`` system (user_specified_type)

    Attributes:
        instance_display_name (str):
            Display name of the Instance. This is user
            specified and different from the resource name.
    """

    instance_display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CloudBigtableInstanceSpec(proto.Message):
    r"""Specification that applies to Instance entries that are part of
    ``CLOUD_BIGTABLE`` system. (user_specified_type)

    Attributes:
        cloud_bigtable_cluster_specs (MutableSequence[google.cloud.datacatalog_v1.types.CloudBigtableInstanceSpec.CloudBigtableClusterSpec]):
            The list of clusters for the Instance.
    """

    class CloudBigtableClusterSpec(proto.Message):
        r"""Spec that applies to clusters of an Instance of Cloud
        Bigtable.

        Attributes:
            display_name (str):
                Name of the cluster.
            location (str):
                Location of the cluster, typically a Cloud
                zone.
            type_ (str):
                Type of the resource. For a cluster this
                would be "CLUSTER".
            linked_resource (str):
                A link back to the parent resource, in this
                case Instance.
        """

        display_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        location: str = proto.Field(
            proto.STRING,
            number=2,
        )
        type_: str = proto.Field(
            proto.STRING,
            number=3,
        )
        linked_resource: str = proto.Field(
            proto.STRING,
            number=4,
        )

    cloud_bigtable_cluster_specs: MutableSequence[CloudBigtableClusterSpec] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=CloudBigtableClusterSpec,
        )
    )


class ServiceSpec(proto.Message):
    r"""Specification that applies to a Service resource. Valid only for
    entries with the ``SERVICE`` type.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        cloud_bigtable_instance_spec (google.cloud.datacatalog_v1.types.CloudBigtableInstanceSpec):
            Specification that applies to Instance entries of
            ``CLOUD_BIGTABLE`` system.

            This field is a member of `oneof`_ ``system_spec``.
    """

    cloud_bigtable_instance_spec: "CloudBigtableInstanceSpec" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="system_spec",
        message="CloudBigtableInstanceSpec",
    )


class VertexModelSourceInfo(proto.Message):
    r"""Detail description of the source information of a Vertex
    model.

    Attributes:
        source_type (google.cloud.datacatalog_v1.types.VertexModelSourceInfo.ModelSourceType):
            Type of the model source.
        copy (bool):
            If this Model is copy of another Model. If true then
            [source_type][google.cloud.datacatalog.v1.VertexModelSourceInfo.source_type]
            pertains to the original.
    """

    class ModelSourceType(proto.Enum):
        r"""Source of the model.

        Values:
            MODEL_SOURCE_TYPE_UNSPECIFIED (0):
                Should not be used.
            AUTOML (1):
                The Model is uploaded by automl training
                pipeline.
            CUSTOM (2):
                The Model is uploaded by user or custom
                training pipeline.
            BQML (3):
                The Model is registered and sync'ed from
                BigQuery ML.
            MODEL_GARDEN (4):
                The Model is saved or tuned from Model
                Garden.
            GENIE (5):
                The Model is saved or tuned from Genie.
            CUSTOM_TEXT_EMBEDDING (6):
                The Model is uploaded by text embedding
                finetuning pipeline.
            MARKETPLACE (7):
                The Model is saved or tuned from Marketplace.
        """

        MODEL_SOURCE_TYPE_UNSPECIFIED = 0
        AUTOML = 1
        CUSTOM = 2
        BQML = 3
        MODEL_GARDEN = 4
        GENIE = 5
        CUSTOM_TEXT_EMBEDDING = 6
        MARKETPLACE = 7

    source_type: ModelSourceType = proto.Field(
        proto.ENUM,
        number=1,
        enum=ModelSourceType,
    )
    copy: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class VertexModelSpec(proto.Message):
    r"""Specification for vertex model resources.

    Attributes:
        version_id (str):
            The version ID of the model.
        version_aliases (MutableSequence[str]):
            User provided version aliases so that a model
            version can be referenced via alias
        version_description (str):
            The description of this version.
        vertex_model_source_info (google.cloud.datacatalog_v1.types.VertexModelSourceInfo):
            Source of a Vertex model.
        container_image_uri (str):
            URI of the Docker image to be used as the
            custom container for serving predictions.
    """

    version_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version_aliases: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    version_description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    vertex_model_source_info: "VertexModelSourceInfo" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="VertexModelSourceInfo",
    )
    container_image_uri: str = proto.Field(
        proto.STRING,
        number=5,
    )


class VertexDatasetSpec(proto.Message):
    r"""Specification for vertex dataset resources.

    Attributes:
        data_item_count (int):
            The number of DataItems in this Dataset. Only
            apply for non-structured Dataset.
        data_type (google.cloud.datacatalog_v1.types.VertexDatasetSpec.DataType):
            Type of the dataset.
    """

    class DataType(proto.Enum):
        r"""Type of data stored in the dataset.

        Values:
            DATA_TYPE_UNSPECIFIED (0):
                Should not be used.
            TABLE (1):
                Structured data dataset.
            IMAGE (2):
                Image dataset which supports
                ImageClassification, ImageObjectDetection and
                ImageSegmentation problems.
            TEXT (3):
                Document dataset which supports
                TextClassification, TextExtraction and
                TextSentiment problems.
            VIDEO (4):
                Video dataset which supports
                VideoClassification, VideoObjectTracking and
                VideoActionRecognition problems.
            CONVERSATION (5):
                Conversation dataset which supports
                conversation problems.
            TIME_SERIES (6):
                TimeSeries dataset.
            DOCUMENT (7):
                Document dataset which supports
                DocumentAnnotation problems.
            TEXT_TO_SPEECH (8):
                TextToSpeech dataset which supports
                TextToSpeech problems.
            TRANSLATION (9):
                Translation dataset which supports
                Translation problems.
            STORE_VISION (10):
                Store Vision dataset which is used for HITL
                integration.
            ENTERPRISE_KNOWLEDGE_GRAPH (11):
                Enterprise Knowledge Graph dataset which is
                used for HITL labeling integration.
            TEXT_PROMPT (12):
                Text prompt dataset which supports Large
                Language Models.
        """

        DATA_TYPE_UNSPECIFIED = 0
        TABLE = 1
        IMAGE = 2
        TEXT = 3
        VIDEO = 4
        CONVERSATION = 5
        TIME_SERIES = 6
        DOCUMENT = 7
        TEXT_TO_SPEECH = 8
        TRANSLATION = 9
        STORE_VISION = 10
        ENTERPRISE_KNOWLEDGE_GRAPH = 11
        TEXT_PROMPT = 12

    data_item_count: int = proto.Field(
        proto.INT64,
        number=1,
    )
    data_type: DataType = proto.Field(
        proto.ENUM,
        number=2,
        enum=DataType,
    )


class ModelSpec(proto.Message):
    r"""Specification that applies to a model. Valid only for entries with
    the ``MODEL`` type.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        vertex_model_spec (google.cloud.datacatalog_v1.types.VertexModelSpec):
            Specification for vertex model resources.

            This field is a member of `oneof`_ ``system_spec``.
    """

    vertex_model_spec: "VertexModelSpec" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="system_spec",
        message="VertexModelSpec",
    )


class FeatureOnlineStoreSpec(proto.Message):
    r"""Detail description of the source information of a Vertex
    Feature Online Store.

    Attributes:
        storage_type (google.cloud.datacatalog_v1.types.FeatureOnlineStoreSpec.StorageType):
            Output only. Type of underlying storage for
            the FeatureOnlineStore.
    """

    class StorageType(proto.Enum):
        r"""Type of underlying storage type.

        Values:
            STORAGE_TYPE_UNSPECIFIED (0):
                Should not be used.
            BIGTABLE (1):
                Underlsying storgae is Bigtable.
            OPTIMIZED (2):
                Underlying is optimized online server
                (Lightning).
        """

        STORAGE_TYPE_UNSPECIFIED = 0
        BIGTABLE = 1
        OPTIMIZED = 2

    storage_type: StorageType = proto.Field(
        proto.ENUM,
        number=1,
        enum=StorageType,
    )


class BusinessContext(proto.Message):
    r"""Business Context of the entry.

    Attributes:
        entry_overview (google.cloud.datacatalog_v1.types.EntryOverview):
            Entry overview fields for rich text
            descriptions of entries.
        contacts (google.cloud.datacatalog_v1.types.Contacts):
            Contact people for the entry.
    """

    entry_overview: "EntryOverview" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="EntryOverview",
    )
    contacts: "Contacts" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Contacts",
    )


class EntryOverview(proto.Message):
    r"""Entry overview fields for rich text descriptions of entries.

    Attributes:
        overview (str):
            Entry overview with support for rich text.

            The overview must only contain Unicode
            characters, and should be formatted using HTML.
            The maximum length is 10 MiB as this value holds
            HTML descriptions including encoded images. The
            maximum length of the text without images is 100
            KiB.
    """

    overview: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Contacts(proto.Message):
    r"""Contact people for the entry.

    Attributes:
        people (MutableSequence[google.cloud.datacatalog_v1.types.Contacts.Person]):
            The list of contact people for the entry.
    """

    class Person(proto.Message):
        r"""A contact person for the entry.

        Attributes:
            designation (str):
                Designation of the person, for example, Data
                Steward.
            email (str):
                Email of the person in the format of ``john.doe@xyz``,
                ``<john.doe@xyz>``, or ``John Doe<john.doe@xyz>``.
        """

        designation: str = proto.Field(
            proto.STRING,
            number=1,
        )
        email: str = proto.Field(
            proto.STRING,
            number=2,
        )

    people: MutableSequence[Person] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=Person,
    )


class EntryGroup(proto.Message):
    r"""Entry group metadata.

    An ``EntryGroup`` resource represents a logical grouping of zero or
    more Data Catalog [Entry][google.cloud.datacatalog.v1.Entry]
    resources.

    Attributes:
        name (str):
            Identifier. The resource name of the entry
            group in URL format.
            Note: The entry group itself and its child
            resources might not be stored in the location
            specified in its name.
        display_name (str):
            A short name to identify the entry group, for
            example, "analytics data - jan 2011". Default
            value is an empty string.
        description (str):
            Entry group description. Can consist of
            several sentences or paragraphs that describe
            the entry group contents. Default value is an
            empty string.
        data_catalog_timestamps (google.cloud.datacatalog_v1.types.SystemTimestamps):
            Output only. Timestamps of the entry group.
            Default value is empty.
        transferred_to_dataplex (bool):
            Optional. When set to [true], it means DataCatalog
            EntryGroup was transferred to Dataplex Catalog Service. It
            makes EntryGroup and its Entries to be read-only in
            DataCatalog. However, new Tags on EntryGroup and its Entries
            can be created. After setting the flag to [true] it cannot
            be unset.
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
    transferred_to_dataplex: bool = proto.Field(
        proto.BOOL,
        number=9,
    )


class CreateTagTemplateRequest(proto.Message):
    r"""Request message for
    [CreateTagTemplate][google.cloud.datacatalog.v1.DataCatalog.CreateTagTemplate].

    Attributes:
        parent (str):
            Required. The name of the project and the template location
            `region <https://cloud.google.com/data-catalog/docs/concepts/regions>`__.
        tag_template_id (str):
            Required. The ID of the tag template to create.

            The ID must contain only lowercase letters (a-z), numbers
            (0-9), or underscores (\_), and must start with a letter or
            underscore. The maximum size is 64 bytes when encoded in
            UTF-8.
        tag_template (google.cloud.datacatalog_v1.types.TagTemplate):
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
    [GetTagTemplate][google.cloud.datacatalog.v1.DataCatalog.GetTagTemplate].

    Attributes:
        name (str):
            Required. The name of the tag template to
            get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateTagTemplateRequest(proto.Message):
    r"""Request message for
    [UpdateTagTemplate][google.cloud.datacatalog.v1.DataCatalog.UpdateTagTemplate].

    Attributes:
        tag_template (google.cloud.datacatalog_v1.types.TagTemplate):
            Required. The template to update. The ``name`` field must be
            set.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Names of fields whose values to overwrite on a tag template.
            Currently, only ``display_name`` and
            ``is_publicly_readable`` can be overwritten.

            If this parameter is absent or empty, all modifiable fields
            are overwritten. If such fields are non-required and omitted
            in the request body, their values are emptied.

            Note: Updating the ``is_publicly_readable`` field may
            require up to 12 hours to take effect in search results.
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
    [DeleteTagTemplate][google.cloud.datacatalog.v1.DataCatalog.DeleteTagTemplate].

    Attributes:
        name (str):
            Required. The name of the tag template to
            delete.
        force (bool):
            Required. If true, deletes all tags that use this template.

            Currently, ``true`` is the only supported value.
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
    [CreateTag][google.cloud.datacatalog.v1.DataCatalog.CreateTag].

    Attributes:
        parent (str):
            Required. The name of the resource to attach
            this tag to.
            Tags can be attached to entries or entry groups.
            An entry can have up to 1000 attached tags.

            Note: The tag and its child resources might not
            be stored in the location specified in its name.
        tag (google.cloud.datacatalog_v1.types.Tag):
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
    [UpdateTag][google.cloud.datacatalog.v1.DataCatalog.UpdateTag].

    Attributes:
        tag (google.cloud.datacatalog_v1.types.Tag):
            Required. The updated tag. The "name" field
            must be set.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
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
    [DeleteTag][google.cloud.datacatalog.v1.DataCatalog.DeleteTag].

    Attributes:
        name (str):
            Required. The name of the tag to delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateTagTemplateFieldRequest(proto.Message):
    r"""Request message for
    [CreateTagTemplateField][google.cloud.datacatalog.v1.DataCatalog.CreateTagTemplateField].

    Attributes:
        parent (str):
            Required. The name of the project and the template location
            `region <https://cloud.google.com/data-catalog/docs/concepts/regions>`__.
        tag_template_field_id (str):
            Required. The ID of the tag template field to create.

            Note: Adding a required field to an existing template is
            *not* allowed.

            Field IDs can contain letters (both uppercase and
            lowercase), numbers (0-9), underscores (\_) and dashes (-).
            Field IDs must be at least 1 character long and at most 128
            characters long. Field IDs must also be unique within their
            template.
        tag_template_field (google.cloud.datacatalog_v1.types.TagTemplateField):
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
    [UpdateTagTemplateField][google.cloud.datacatalog.v1.DataCatalog.UpdateTagTemplateField].

    Attributes:
        name (str):
            Required. The name of the tag template field.
        tag_template_field (google.cloud.datacatalog_v1.types.TagTemplateField):
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
    [RenameTagTemplateField][google.cloud.datacatalog.v1.DataCatalog.RenameTagTemplateField].

    Attributes:
        name (str):
            Required. The name of the tag template field.
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
            Required. The name of the enum field value.
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
    [DeleteTagTemplateField][google.cloud.datacatalog.v1.DataCatalog.DeleteTagTemplateField].

    Attributes:
        name (str):
            Required. The name of the tag template field
            to delete.
        force (bool):
            Required. If true, deletes this field from any tags that use
            it.

            Currently, ``true`` is the only supported value.
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
    [ListTags][google.cloud.datacatalog.v1.DataCatalog.ListTags].

    Attributes:
        parent (str):
            Required. The name of the Data Catalog resource to list the
            tags of.

            The resource can be an
            [Entry][google.cloud.datacatalog.v1.Entry] or an
            [EntryGroup][google.cloud.datacatalog.v1.EntryGroup]
            (without ``/entries/{entries}`` at the end).
        page_size (int):
            The maximum number of tags to return. Default
            is 10. Maximum limit is 1000.
        page_token (str):
            Pagination token that specifies the next page
            to return. If empty, the first page is returned.
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
    [ListTags][google.cloud.datacatalog.v1.DataCatalog.ListTags].

    Attributes:
        tags (MutableSequence[google.cloud.datacatalog_v1.types.Tag]):
            [Tag][google.cloud.datacatalog.v1.Tag] details.
        next_page_token (str):
            Pagination token of the next results page.
            Empty if there are no more items in results.
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


class ReconcileTagsRequest(proto.Message):
    r"""Request message for
    [ReconcileTags][google.cloud.datacatalog.v1.DataCatalog.ReconcileTags].

    Attributes:
        parent (str):
            Required. Name of [Entry][google.cloud.datacatalog.v1.Entry]
            to be tagged.
        tag_template (str):
            Required. The name of the tag template, which
            is used for reconciliation.
        force_delete_missing (bool):
            If set to ``true``, deletes entry tags related to a tag
            template not listed in the tags source from an entry. If set
            to ``false``, unlisted tags are retained.
        tags (MutableSequence[google.cloud.datacatalog_v1.types.Tag]):
            A list of tags to apply to an entry. A tag can specify a tag
            template, which must be the template specified in the
            ``ReconcileTagsRequest``. The sole entry and each of its
            columns must be mentioned at most once.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tag_template: str = proto.Field(
        proto.STRING,
        number=2,
    )
    force_delete_missing: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    tags: MutableSequence[gcd_tags.Tag] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=gcd_tags.Tag,
    )


class ReconcileTagsResponse(proto.Message):
    r"""[Long-running operation][google.longrunning.Operation] response
    message returned by
    [ReconcileTags][google.cloud.datacatalog.v1.DataCatalog.ReconcileTags].

    Attributes:
        created_tags_count (int):
            Number of tags created in the request.
        updated_tags_count (int):
            Number of tags updated in the request.
        deleted_tags_count (int):
            Number of tags deleted in the request.
    """

    created_tags_count: int = proto.Field(
        proto.INT64,
        number=1,
    )
    updated_tags_count: int = proto.Field(
        proto.INT64,
        number=2,
    )
    deleted_tags_count: int = proto.Field(
        proto.INT64,
        number=3,
    )


class ReconcileTagsMetadata(proto.Message):
    r"""[Long-running operation][google.longrunning.Operation] metadata
    message returned by the
    [ReconcileTags][google.cloud.datacatalog.v1.DataCatalog.ReconcileTags].

    Attributes:
        state (google.cloud.datacatalog_v1.types.ReconcileTagsMetadata.ReconciliationState):
            State of the reconciliation operation.
        errors (MutableMapping[str, google.rpc.status_pb2.Status]):
            Maps the name of each tagged column (or empty string for a
            sole entry) to tagging operation
            [status][google.rpc.Status].
    """

    class ReconciliationState(proto.Enum):
        r"""Enum holding possible states of the reconciliation operation.

        Values:
            RECONCILIATION_STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            RECONCILIATION_QUEUED (1):
                The reconciliation has been queued and awaits
                for execution.
            RECONCILIATION_IN_PROGRESS (2):
                The reconciliation is in progress.
            RECONCILIATION_DONE (3):
                The reconciliation has been finished.
        """

        RECONCILIATION_STATE_UNSPECIFIED = 0
        RECONCILIATION_QUEUED = 1
        RECONCILIATION_IN_PROGRESS = 2
        RECONCILIATION_DONE = 3

    state: ReconciliationState = proto.Field(
        proto.ENUM,
        number=1,
        enum=ReconciliationState,
    )
    errors: MutableMapping[str, status_pb2.Status] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=2,
        message=status_pb2.Status,
    )


class ListEntriesRequest(proto.Message):
    r"""Request message for
    [ListEntries][google.cloud.datacatalog.v1.DataCatalog.ListEntries].

    Attributes:
        parent (str):
            Required. The name of the entry group that
            contains the entries to list.
            Can be provided in URL format.
        page_size (int):
            The maximum number of items to return. Default is 10.
            Maximum limit is 1000. Throws an invalid argument if
            ``page_size`` is more than 1000.
        page_token (str):
            Pagination token that specifies the next page
            to return. If empty, the first page is returned.
        read_mask (google.protobuf.field_mask_pb2.FieldMask):
            The fields to return for each entry. If empty or omitted,
            all fields are returned.

            For example, to return a list of entries with only the
            ``name`` field, set ``read_mask`` to only one path with the
            ``name`` value.
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
    [ListEntries][google.cloud.datacatalog.v1.DataCatalog.ListEntries].

    Attributes:
        entries (MutableSequence[google.cloud.datacatalog_v1.types.Entry]):
            Entry details.
        next_page_token (str):
            Pagination token of the next results page.
            Empty if there are no more items in results.
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


class StarEntryRequest(proto.Message):
    r"""Request message for
    [StarEntry][google.cloud.datacatalog.v1.DataCatalog.StarEntry].

    Attributes:
        name (str):
            Required. The name of the entry to mark as
            starred.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class StarEntryResponse(proto.Message):
    r"""Response message for
    [StarEntry][google.cloud.datacatalog.v1.DataCatalog.StarEntry].
    Empty for now

    """


class UnstarEntryRequest(proto.Message):
    r"""Request message for
    [UnstarEntry][google.cloud.datacatalog.v1.DataCatalog.UnstarEntry].

    Attributes:
        name (str):
            Required. The name of the entry to mark as **not** starred.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UnstarEntryResponse(proto.Message):
    r"""Response message for
    [UnstarEntry][google.cloud.datacatalog.v1.DataCatalog.UnstarEntry].
    Empty for now

    """


class ImportEntriesRequest(proto.Message):
    r"""Request message for
    [ImportEntries][google.cloud.datacatalog.v1.DataCatalog.ImportEntries]
    method.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. Target entry group for ingested
            entries.
        gcs_bucket_path (str):
            Path to a Cloud Storage bucket that contains
            a dump ready for ingestion.

            This field is a member of `oneof`_ ``source``.
        job_id (str):
            Optional. (Optional) Dataplex task job id, if
            specified will be used as part of ImportEntries
            LRO ID
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    gcs_bucket_path: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="source",
    )
    job_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ImportEntriesResponse(proto.Message):
    r"""Response message for [long-running
    operation][google.longrunning.Operation] returned by the
    [ImportEntries][google.cloud.datacatalog.v1.DataCatalog.ImportEntries].


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        upserted_entries_count (int):
            Cumulative number of entries created and
            entries updated as a result of import operation.

            This field is a member of `oneof`_ ``_upserted_entries_count``.
        deleted_entries_count (int):
            Number of entries deleted as a result of
            import operation.

            This field is a member of `oneof`_ ``_deleted_entries_count``.
    """

    upserted_entries_count: int = proto.Field(
        proto.INT64,
        number=5,
        optional=True,
    )
    deleted_entries_count: int = proto.Field(
        proto.INT64,
        number=6,
        optional=True,
    )


class ImportEntriesMetadata(proto.Message):
    r"""Metadata message for [long-running
    operation][google.longrunning.Operation] returned by the
    [ImportEntries][google.cloud.datacatalog.v1.DataCatalog.ImportEntries].

    Attributes:
        state (google.cloud.datacatalog_v1.types.ImportEntriesMetadata.ImportState):
            State of the import operation.
        errors (MutableSequence[google.rpc.status_pb2.Status]):
            Partial errors that are encountered during
            the ImportEntries operation. There is no
            guarantee that all the encountered errors are
            reported. However, if no errors are reported, it
            means that no errors were encountered.
    """

    class ImportState(proto.Enum):
        r"""Enum holding possible states of the import operation.

        Values:
            IMPORT_STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            IMPORT_QUEUED (1):
                The dump with entries has been queued for
                import.
            IMPORT_IN_PROGRESS (2):
                The import of entries is in progress.
            IMPORT_DONE (3):
                The import of entries has been finished.
            IMPORT_OBSOLETE (4):
                The import of entries has been abandoned in
                favor of a newer request.
        """

        IMPORT_STATE_UNSPECIFIED = 0
        IMPORT_QUEUED = 1
        IMPORT_IN_PROGRESS = 2
        IMPORT_DONE = 3
        IMPORT_OBSOLETE = 4

    state: ImportState = proto.Field(
        proto.ENUM,
        number=1,
        enum=ImportState,
    )
    errors: MutableSequence[status_pb2.Status] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=status_pb2.Status,
    )


class ModifyEntryOverviewRequest(proto.Message):
    r"""Request message for
    [ModifyEntryOverview][google.cloud.datacatalog.v1.DataCatalog.ModifyEntryOverview].

    Attributes:
        name (str):
            Required. The full resource name of the
            entry.
        entry_overview (google.cloud.datacatalog_v1.types.EntryOverview):
            Required. The new value for the Entry
            Overview.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    entry_overview: "EntryOverview" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="EntryOverview",
    )


class ModifyEntryContactsRequest(proto.Message):
    r"""Request message for
    [ModifyEntryContacts][google.cloud.datacatalog.v1.DataCatalog.ModifyEntryContacts].

    Attributes:
        name (str):
            Required. The full resource name of the
            entry.
        contacts (google.cloud.datacatalog_v1.types.Contacts):
            Required. The new value for the Contacts.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    contacts: "Contacts" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Contacts",
    )


class SetConfigRequest(proto.Message):
    r"""Request message for
    [SetConfig][google.cloud.datacatalog.v1.DataCatalog.SetConfig].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Required. The organization or project whose
            config is being specified.
        tag_template_migration (google.cloud.datacatalog_v1.types.TagTemplateMigration):
            Opt-in status for the migration of Tag
            Templates to Dataplex.

            This field is a member of `oneof`_ ``configuration``.
        catalog_ui_experience (google.cloud.datacatalog_v1.types.CatalogUIExperience):
            Opt-in status for the UI switch to Dataplex.

            This field is a member of `oneof`_ ``configuration``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tag_template_migration: "TagTemplateMigration" = proto.Field(
        proto.ENUM,
        number=2,
        oneof="configuration",
        enum="TagTemplateMigration",
    )
    catalog_ui_experience: "CatalogUIExperience" = proto.Field(
        proto.ENUM,
        number=3,
        oneof="configuration",
        enum="CatalogUIExperience",
    )


class RetrieveConfigRequest(proto.Message):
    r"""Request message for
    [RetrieveConfig][google.cloud.datacatalog.v1.DataCatalog.RetrieveConfig].

    Attributes:
        name (str):
            Required. The organization whose config is
            being retrieved.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RetrieveEffectiveConfigRequest(proto.Message):
    r"""Request message for
    [RetrieveEffectiveConfig][google.cloud.datacatalog.v1.DataCatalog.RetrieveEffectiveConfig].

    Attributes:
        name (str):
            Required. The resource whose effective config
            is being retrieved.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class OrganizationConfig(proto.Message):
    r"""The configuration related to the migration from Data Catalog to
    Dataplex that has been applied to an organization and any projects
    under it. It is the response message for
    [RetrieveConfig][google.cloud.datacatalog.v1.DataCatalog.RetrieveConfig].

    Attributes:
        config (MutableMapping[str, google.cloud.datacatalog_v1.types.MigrationConfig]):
            Map of organizations and project resource names and their
            configuration. The format for the map keys is
            ``organizations/{organizationId}`` or
            ``projects/{projectId}``.
    """

    config: MutableMapping[str, "MigrationConfig"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=1,
        message="MigrationConfig",
    )


class MigrationConfig(proto.Message):
    r"""The configuration related to the migration to Dataplex applied to an
    organization or project. It is the response message for
    [SetConfig][google.cloud.datacatalog.v1.DataCatalog.SetConfig] and
    [RetrieveEffectiveConfig][google.cloud.datacatalog.v1.DataCatalog.RetrieveEffectiveConfig].

    Attributes:
        tag_template_migration (google.cloud.datacatalog_v1.types.TagTemplateMigration):
            Opt-in status for the migration of Tag
            Templates to Dataplex.
        catalog_ui_experience (google.cloud.datacatalog_v1.types.CatalogUIExperience):
            Opt-in status for the UI switch to Dataplex.
        template_migration_enabled_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the Tag Template migration was
            enabled. If the Tag Template migration is not
            enabled, this field is not set.
    """

    tag_template_migration: "TagTemplateMigration" = proto.Field(
        proto.ENUM,
        number=1,
        enum="TagTemplateMigration",
    )
    catalog_ui_experience: "CatalogUIExperience" = proto.Field(
        proto.ENUM,
        number=2,
        enum="CatalogUIExperience",
    )
    template_migration_enabled_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
