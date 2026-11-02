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

import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.geminidataanalytics_v1alpha.types import agent_context
from google.cloud.geminidataanalytics_v1alpha.types import (
    credentials as gcg_credentials,
)

__protobuf__ = proto.module(
    package="google.cloud.geminidataanalytics.v1alpha",
    manifest={
        "DataFilterType",
        "DatasourceReferences",
        "BigQueryTableReferences",
        "BigQueryTableReference",
        "BigQueryDatasetReference",
        "SearchScope",
        "StudioDatasourceReferences",
        "StudioDatasourceReference",
        "AlloyDbReference",
        "DatabaseTableReference",
        "AlloyDbDatabaseReference",
        "BigtableReference",
        "BigtableDatabaseReference",
        "FirestoreReference",
        "FirestoreDatabaseReference",
        "SpannerReference",
        "SpannerDatabaseReference",
        "CloudSqlReference",
        "CloudSqlDatabaseReference",
        "LookerExploreReferences",
        "LookerExploreReference",
        "BigQueryPropertyGraphReference",
        "PrivateLookerInstanceInfo",
        "Datasource",
        "Schema",
        "Field",
        "DataFilter",
    },
)


class DataFilterType(proto.Enum):
    r"""The type of filter present on a datasource, such as ALWAYS_FILTER.

    Values:
        DATA_FILTER_TYPE_UNSPECIFIED (0):
            The filter type was not specified.
        ALWAYS_FILTER (1):
            A filter that the user configures, and any
            queries to the Explore will always apply this
            filter by default. Currently only used for
            Looker data sources.
    """

    DATA_FILTER_TYPE_UNSPECIFIED = 0
    ALWAYS_FILTER = 1


class DatasourceReferences(proto.Message):
    r"""A collection of references to datasources.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        bq (google.cloud.geminidataanalytics_v1alpha.types.BigQueryTableReferences):
            References to BigQuery tables.

            This field is a member of `oneof`_ ``references``.
        studio (google.cloud.geminidataanalytics_v1alpha.types.StudioDatasourceReferences):
            References to Looker Studio datasources.

            This field is a member of `oneof`_ ``references``.
        looker (google.cloud.geminidataanalytics_v1alpha.types.LookerExploreReferences):
            References to Looker Explores.

            This field is a member of `oneof`_ ``references``.
        alloydb (google.cloud.geminidataanalytics_v1alpha.types.AlloyDbReference):
            Reference to an AlloyDB database. Only supported for the
            ``QueryData`` method.

            This field is a member of `oneof`_ ``references``.
        spanner_reference (google.cloud.geminidataanalytics_v1alpha.types.SpannerReference):
            Reference to a Spanner database. Only supported for the
            ``QueryData`` method.

            This field is a member of `oneof`_ ``references``.
        cloud_sql_reference (google.cloud.geminidataanalytics_v1alpha.types.CloudSqlReference):
            Reference to a CloudSql database. Only supported for the
            ``QueryData`` method.

            This field is a member of `oneof`_ ``references``.
        bigtable_reference (google.cloud.geminidataanalytics_v1alpha.types.BigtableReference):
            Reference to a Bigtable instance.

            This field is a member of `oneof`_ ``references``.
        firestore_reference (google.cloud.geminidataanalytics_v1alpha.types.FirestoreReference):
            Reference to a Firestore database.

            This field is a member of `oneof`_ ``references``.
    """

    bq: "BigQueryTableReferences" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="references",
        message="BigQueryTableReferences",
    )
    studio: "StudioDatasourceReferences" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="references",
        message="StudioDatasourceReferences",
    )
    looker: "LookerExploreReferences" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="references",
        message="LookerExploreReferences",
    )
    alloydb: "AlloyDbReference" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="references",
        message="AlloyDbReference",
    )
    spanner_reference: "SpannerReference" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="references",
        message="SpannerReference",
    )
    cloud_sql_reference: "CloudSqlReference" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="references",
        message="CloudSqlReference",
    )
    bigtable_reference: "BigtableReference" = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="references",
        message="BigtableReference",
    )
    firestore_reference: "FirestoreReference" = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="references",
        message="FirestoreReference",
    )


class BigQueryTableReferences(proto.Message):
    r"""Message representing references to BigQuery tables and property
    graphs. At least one of ``table_references``,
    ``property_graph_references``, or ``search_scope`` must be
    populated.

    Attributes:
        table_references (MutableSequence[google.cloud.geminidataanalytics_v1alpha.types.BigQueryTableReference]):
            Optional. References to BigQuery tables.
        property_graph_references (MutableSequence[google.cloud.geminidataanalytics_v1alpha.types.BigQueryPropertyGraphReference]):
            Optional. References to BigQuery graphs.

            Note: "property graph" is the former name for
            BigQuery Graph. The field and message names
            retain the original term for backward
            compatibility; both refer to the same resource.
        search_scope (google.cloud.geminidataanalytics_v1alpha.types.SearchScope):
            Optional. Search over BigQuery resources to discover most
            relevant tables to the query.

            When set, at least one of ``include_project_ids`` or
            ``include_dataset_references`` must be populated with
            non-blank identifiers. Matches from the two fields are
            unioned (OR-ed).

            Note: ``search_scope`` is only supported for standalone
            conversations (``ChatRequest.inline_context`` or
            ``ClientManagedResourceContext.inline_context``) and is not
            supported in
            [DataAgent][google.cloud.geminidataanalytics.v1alpha.DataAgent].
        agent_context_reference (google.cloud.geminidataanalytics_v1alpha.types.AgentContextReference):
            Optional. Parameters for retrieving data from
            Agent Context.
    """

    table_references: MutableSequence["BigQueryTableReference"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="BigQueryTableReference",
    )
    property_graph_references: MutableSequence["BigQueryPropertyGraphReference"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="BigQueryPropertyGraphReference",
        )
    )
    search_scope: "SearchScope" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="SearchScope",
    )
    agent_context_reference: agent_context.AgentContextReference = proto.Field(
        proto.MESSAGE,
        number=4,
        message=agent_context.AgentContextReference,
    )


class BigQueryTableReference(proto.Message):
    r"""Message representing a reference to a single BigQuery table.

    Attributes:
        project_id (str):
            Required. The project that the table belongs
            to.
        dataset_id (str):
            Required. The dataset that the table belongs
            to.
        table_id (str):
            Required. The table id.
        schema (google.cloud.geminidataanalytics_v1alpha.types.Schema):
            Optional. The schema of the datasource.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dataset_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    table_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    schema: "Schema" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="Schema",
    )


class BigQueryDatasetReference(proto.Message):
    r"""Message representing a reference to a single BigQuery
    dataset.

    Attributes:
        project_id (str):
            Required. The project ID that the dataset
            belongs to.
        dataset_id (str):
            Required. The dataset ID.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dataset_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SearchScope(proto.Message):
    r"""Message representing filters to apply to search over BigQuery
    tables.

    At least one of ``include_project_ids`` or
    ``include_dataset_references`` must be populated with non-blank
    identifiers. Tables matching either field are included, so the two
    fields are unioned (OR-ed) rather than intersected.

    Note: ``SearchScope`` is only supported for standalone conversations
    (``ChatRequest.inline_context`` or
    ``ClientManagedResourceContext.inline_context``) and is not
    supported in
    [DataAgent][google.cloud.geminidataanalytics.v1alpha.DataAgent].

    Attributes:
        include_project_ids (MutableSequence[str]):
            Optional. The BigQuery project ids to search
            over.
        include_dataset_references (MutableSequence[google.cloud.geminidataanalytics_v1alpha.types.BigQueryDatasetReference]):
            Optional. The BigQuery dataset references to
            search over.
    """

    include_project_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    include_dataset_references: MutableSequence["BigQueryDatasetReference"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="BigQueryDatasetReference",
        )
    )


class StudioDatasourceReferences(proto.Message):
    r"""Message representing references to Looker Studio datasources.

    Attributes:
        studio_references (MutableSequence[google.cloud.geminidataanalytics_v1alpha.types.StudioDatasourceReference]):
            Optional. The references to the studio
            datasources.
    """

    studio_references: MutableSequence["StudioDatasourceReference"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="StudioDatasourceReference",
        )
    )


class StudioDatasourceReference(proto.Message):
    r"""Message representing a reference to a single Looker Studio
    datasource.

    Attributes:
        datasource_id (str):
            Required. The id of the datasource.
    """

    datasource_id: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AlloyDbReference(proto.Message):
    r"""Message representing reference to an AlloyDB database and agent
    context. Only supported for the ``QueryData`` method.

    Attributes:
        database_reference (google.cloud.geminidataanalytics_v1alpha.types.AlloyDbDatabaseReference):
            Required. Singular proto that supports
            specifying which database and tables to include.
        agent_context_reference (google.cloud.geminidataanalytics_v1alpha.types.AgentContextReference):
            Optional. Parameters for retrieving data from
            Agent Context.
    """

    database_reference: "AlloyDbDatabaseReference" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="AlloyDbDatabaseReference",
    )
    agent_context_reference: agent_context.AgentContextReference = proto.Field(
        proto.MESSAGE,
        number=3,
        message=agent_context.AgentContextReference,
    )


class DatabaseTableReference(proto.Message):
    r"""Message representing a table including its schema.

    Attributes:
        table_id (str):
            Required. The name of the table as defined in the database.

            Note: The precise rules for table naming, including valid
            characters, length limits, and case sensitivity, are
            determined by the specific database system.

            Requirements:

            - Exact Match: The provided name must be identical to the
              name stored in the database.
            - Case Sensitivity: Respect the case sensitivity rules of
              the specific database system and how the table was
              created. For example, "Orders" and "orders" may be
              distinct table names.
            - Special Characters/Keywords: If the table name includes
              spaces, special characters, or is a database reserved
              keyword, provide the literal name as it is stored. Do not
              add any database-specific identifier quoting characters
              (e.g., ", \`, []).

            Examples:

            - Simple name: "orders", "UserActivity"
            - Case sensitive: "MyTable"
            - Name with spaces: "Order Details"
            - Name with other special characters: "user/data",
              "order-items"
            - Name that is a keyword: "Group", "Order"

            Permissions: The caller's credentials must have the
            necessary database permissions to access the table's schema
            and data.
        schema (google.cloud.geminidataanalytics_v1alpha.types.Schema):
            Optional. The schema of the table.
    """

    table_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    schema: "Schema" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Schema",
    )


class AlloyDbDatabaseReference(proto.Message):
    r"""Message representing a reference to a single AlloyDB
    database.

    Attributes:
        project_id (str):
            Required. The project the instance belongs
            to.
        region (str):
            Required. The region of the instance.
        cluster_id (str):
            Required. The cluster id.
        instance_id (str):
            Required. The instance id.
        database_id (str):
            Required. The database id.
        table_ids (MutableSequence[str]):
            Optional. The table ids. Denotes all tables
            if unset.
        database_table_references (MutableSequence[google.cloud.geminidataanalytics_v1alpha.types.DatabaseTableReference]):
            Optional. References to tables within the
            database. Each reference specifies a table and
            can optionally include the table's schema to
            provide context for the query.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    region: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cluster_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    database_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    table_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    database_table_references: MutableSequence["DatabaseTableReference"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=7,
            message="DatabaseTableReference",
        )
    )


class BigtableReference(proto.Message):
    r"""Message representing reference to a Bigtable instance and
    agent context.

    Attributes:
        database_reference (google.cloud.geminidataanalytics_v1alpha.types.BigtableDatabaseReference):
            Required. Singular proto that supports
            specifying which database and tables to include.
        agent_context_reference (google.cloud.geminidataanalytics_v1alpha.types.AgentContextReference):
            Optional. Parameters for retrieving data from
            Agent Context.
    """

    database_reference: "BigtableDatabaseReference" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="BigtableDatabaseReference",
    )
    agent_context_reference: agent_context.AgentContextReference = proto.Field(
        proto.MESSAGE,
        number=2,
        message=agent_context.AgentContextReference,
    )


class BigtableDatabaseReference(proto.Message):
    r"""Message representing reference to Bigtable database.

    Attributes:
        project_id (str):
            Required. The project the instance belongs
            to.
        instance_id (str):
            Required. The instance id.
        table_ids (MutableSequence[str]):
            Optional. The table ids. Denotes all tables
            if unset.
        database_table_references (MutableSequence[google.cloud.geminidataanalytics_v1alpha.types.DatabaseTableReference]):
            Optional. References to tables within the
            database. Each reference specifies a table and
            can optionally include the table's schema to
            provide context for the query.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    table_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    database_table_references: MutableSequence["DatabaseTableReference"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message="DatabaseTableReference",
        )
    )


class FirestoreReference(proto.Message):
    r"""Message representing reference to a Firestore database and
    agent context.

    Attributes:
        database_reference (google.cloud.geminidataanalytics_v1alpha.types.FirestoreDatabaseReference):
            Required. Singular proto that supports
            specifying which database and tables to include.
        agent_context_reference (google.cloud.geminidataanalytics_v1alpha.types.AgentContextReference):
            Optional. Parameters for retrieving data from
            Agent Context.
    """

    database_reference: "FirestoreDatabaseReference" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="FirestoreDatabaseReference",
    )
    agent_context_reference: agent_context.AgentContextReference = proto.Field(
        proto.MESSAGE,
        number=2,
        message=agent_context.AgentContextReference,
    )


class FirestoreDatabaseReference(proto.Message):
    r"""Message representing a reference to a single Firestore
    database.

    Attributes:
        project_id (str):
            Required. Project the firestore database
            belongs to.
        database_id (str):
            Required. The database id.
        collection_ids (MutableSequence[str]):
            Optional. The collection ids. Denotes all
            collections if unset.
        database_table_references (MutableSequence[google.cloud.geminidataanalytics_v1alpha.types.DatabaseTableReference]):
            Optional. References to collections within
            the database. Each reference specifies a
            collection and can optionally include the
            collection's schema to provide context for the
            query.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    database_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    collection_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    database_table_references: MutableSequence["DatabaseTableReference"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message="DatabaseTableReference",
        )
    )


class SpannerReference(proto.Message):
    r"""Message representing reference to a Spanner database and agent
    context. Only supported for the ``QueryData`` method.

    Attributes:
        database_reference (google.cloud.geminidataanalytics_v1alpha.types.SpannerDatabaseReference):
            Required. Singular proto that supports
            specifying which database and tables to include.
        agent_context_reference (google.cloud.geminidataanalytics_v1alpha.types.AgentContextReference):
            Optional. Parameters for retrieving data from
            Agent Context.
    """

    database_reference: "SpannerDatabaseReference" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SpannerDatabaseReference",
    )
    agent_context_reference: agent_context.AgentContextReference = proto.Field(
        proto.MESSAGE,
        number=2,
        message=agent_context.AgentContextReference,
    )


class SpannerDatabaseReference(proto.Message):
    r"""Message representing a reference to a single Spanner
    database.

    Attributes:
        engine (google.cloud.geminidataanalytics_v1alpha.types.SpannerDatabaseReference.Engine):
            Required. The engine of the Spanner instance.
        project_id (str):
            Required. The project the instance belongs
            to.
        instance_id (str):
            Required. The instance id.
        database_id (str):
            Required. The database id.
        table_ids (MutableSequence[str]):
            Optional. The table ids. Denotes all tables
            if unset.
        database_table_references (MutableSequence[google.cloud.geminidataanalytics_v1alpha.types.DatabaseTableReference]):
            Optional. References to tables within the
            database. Each reference specifies a table and
            can optionally include the table's schema to
            provide context for the query.
        priority (str):
            Optional. Priority for the queries to
            Spanner. Should be a value supported by Cloud
            Spanner e.g.: LOW, MEDIUM, HIGH. Unsupported
            values will be ignored. See
            https://docs.cloud.google.com/spanner/docs/reference/rest/v1/RequestOptions#Priority
            for complete list.
        request_tag (str):
            Tag to be attached to all queries to Spanner.
            Allows to identify and monitor queries sent to
            Spanner by the GDA service.
        graph_ids (MutableSequence[str]):
            Optional. The graph IDs to query.
    """

    class Engine(proto.Enum):
        r"""The database engine.

        Values:
            ENGINE_UNSPECIFIED (0):
                Engine is not specified.
            GOOGLE_SQL (1):
                Google SQL
            POSTGRESQL (2):
                PostgreSQL
        """

        ENGINE_UNSPECIFIED = 0
        GOOGLE_SQL = 1
        POSTGRESQL = 2

    engine: Engine = proto.Field(
        proto.ENUM,
        number=6,
        enum=Engine,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    database_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    table_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    database_table_references: MutableSequence["DatabaseTableReference"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=7,
            message="DatabaseTableReference",
        )
    )
    priority: str = proto.Field(
        proto.STRING,
        number=8,
    )
    request_tag: str = proto.Field(
        proto.STRING,
        number=9,
    )
    graph_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10,
    )


class CloudSqlReference(proto.Message):
    r"""Message representing reference to a CloudSQL database and agent
    context. Only supported for the ``QueryData`` method.

    Attributes:
        database_reference (google.cloud.geminidataanalytics_v1alpha.types.CloudSqlDatabaseReference):
            Required. Singular proto that supports
            specifying which database and tables to include.
        agent_context_reference (google.cloud.geminidataanalytics_v1alpha.types.AgentContextReference):
            Optional. Parameters for retrieving data from
            Agent Context.
    """

    database_reference: "CloudSqlDatabaseReference" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CloudSqlDatabaseReference",
    )
    agent_context_reference: agent_context.AgentContextReference = proto.Field(
        proto.MESSAGE,
        number=2,
        message=agent_context.AgentContextReference,
    )


class CloudSqlDatabaseReference(proto.Message):
    r"""Message representing a reference to a single CloudSQL
    database.

    Attributes:
        engine (google.cloud.geminidataanalytics_v1alpha.types.CloudSqlDatabaseReference.Engine):
            Required. The engine of the Cloud SQL
            instance.
        project_id (str):
            Required. The project the instance belongs
            to.
        region (str):
            Required. The region of the instance.
        instance_id (str):
            Required. The instance id.
        database_id (str):
            Required. The database id.
        table_ids (MutableSequence[str]):
            Optional. The table ids. Denotes all tables
            if unset.
        database_table_references (MutableSequence[google.cloud.geminidataanalytics_v1alpha.types.DatabaseTableReference]):
            Optional. References to tables within the
            database. Each reference specifies a table and
            can optionally include the table's schema to
            provide context for the query.
    """

    class Engine(proto.Enum):
        r"""The database engine.

        Values:
            ENGINE_UNSPECIFIED (0):
                Engine is not specified.
            POSTGRESQL (1):
                PostgreSQL
            MYSQL (2):
                MySQL
        """

        ENGINE_UNSPECIFIED = 0
        POSTGRESQL = 1
        MYSQL = 2

    engine: Engine = proto.Field(
        proto.ENUM,
        number=1,
        enum=Engine,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    region: str = proto.Field(
        proto.STRING,
        number=3,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    database_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    table_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    database_table_references: MutableSequence["DatabaseTableReference"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=8,
            message="DatabaseTableReference",
        )
    )


class LookerExploreReferences(proto.Message):
    r"""Message representing references to Looker explores.

    Attributes:
        explore_references (MutableSequence[google.cloud.geminidataanalytics_v1alpha.types.LookerExploreReference]):
            Required. References to Looker explores.
        credentials (google.cloud.geminidataanalytics_v1alpha.types.Credentials):
            Optional. Deprecated: Use credentials in ChatRequest. The
            credentials to use when calling the Looker API.

            Currently supports both OAuth token and API key-based
            credentials, as described in `Authentication with an
            SDK <https://cloud.google.com/looker/docs/api-auth#authentication_with_an_sdk>`__.
    """

    explore_references: MutableSequence["LookerExploreReference"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="LookerExploreReference",
    )
    credentials: gcg_credentials.Credentials = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcg_credentials.Credentials,
    )


class LookerExploreReference(proto.Message):
    r"""Message representing a reference to a single Looker explore.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        looker_instance_uri (str):
            Required. The base url of the Looker
            instance.

            This field is a member of `oneof`_ ``instance``.
        private_looker_instance_info (google.cloud.geminidataanalytics_v1alpha.types.PrivateLookerInstanceInfo):
            Private Looker instance info.

            This field is a member of `oneof`_ ``instance``.
        lookml_model (str):
            Required. Looker model, as outlined in `Major LookML
            structures <https://cloud.google.com/looker/docs/lookml-terms-and-concepts#major_lookml_structures>`__.
            Name of the LookML model.
        explore (str):
            Required. Looker Explore, as outlined in `Major LookML
            structures <https://cloud.google.com/looker/docs/lookml-terms-and-concepts#major_lookml_structures>`__.
            Name of the LookML Explore.
        schema (google.cloud.geminidataanalytics_v1alpha.types.Schema):
            Optional. The schema of the datasource.
    """

    looker_instance_uri: str = proto.Field(
        proto.STRING,
        number=9,
        oneof="instance",
    )
    private_looker_instance_info: "PrivateLookerInstanceInfo" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="instance",
        message="PrivateLookerInstanceInfo",
    )
    lookml_model: str = proto.Field(
        proto.STRING,
        number=4,
    )
    explore: str = proto.Field(
        proto.STRING,
        number=5,
    )
    schema: "Schema" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="Schema",
    )


class BigQueryPropertyGraphReference(proto.Message):
    r"""Message representing a reference to a single BigQuery
    property graph.

    Attributes:
        project_id (str):
            Required. The project that the property graph
            belongs to.
        dataset_id (str):
            Required. The dataset that the property graph
            belongs to.
        property_graph_id (str):
            Required. The property graph id.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dataset_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    property_graph_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class PrivateLookerInstanceInfo(proto.Message):
    r"""Message representing a private Looker instance info required
    if the Looker instance is behind a private network.

    Attributes:
        looker_instance_id (str):
            The Looker instance id.
        service_directory_name (str):
            The service directory name of the Looker
            instance.
    """

    looker_instance_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    service_directory_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Datasource(proto.Message):
    r"""A datasource that can be used to answer questions.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        bigquery_table_reference (google.cloud.geminidataanalytics_v1alpha.types.BigQueryTableReference):
            A reference to a BigQuery table.

            This field is a member of `oneof`_ ``reference``.
        studio_datasource_id (str):
            A reference to a Looker Studio datasource.

            This field is a member of `oneof`_ ``reference``.
        looker_explore_reference (google.cloud.geminidataanalytics_v1alpha.types.LookerExploreReference):
            A reference to a Looker explore.

            This field is a member of `oneof`_ ``reference``.
        alloy_db_reference (google.cloud.geminidataanalytics_v1alpha.types.AlloyDbReference):
            A reference to an AlloyDB database.

            This field is a member of `oneof`_ ``reference``.
        spanner_reference (google.cloud.geminidataanalytics_v1alpha.types.SpannerReference):
            A reference to a Spanner database.

            This field is a member of `oneof`_ ``reference``.
        cloud_sql_reference (google.cloud.geminidataanalytics_v1alpha.types.CloudSqlReference):
            A reference to a CloudSQL database.

            This field is a member of `oneof`_ ``reference``.
        bigtable_reference (google.cloud.geminidataanalytics_v1alpha.types.BigtableReference):
            A reference to a Bigtable instance.

            This field is a member of `oneof`_ ``reference``.
        bigquery_property_graph_reference (google.cloud.geminidataanalytics_v1alpha.types.BigQueryPropertyGraphReference):
            A reference to a BigQuery property graph.

            This field is a member of `oneof`_ ``reference``.
        firestore_reference (google.cloud.geminidataanalytics_v1alpha.types.FirestoreReference):
            A reference to a Firestore database.

            This field is a member of `oneof`_ ``reference``.
        schema (google.cloud.geminidataanalytics_v1alpha.types.Schema):
            Optional. The schema of the datasource.
        struct_schema (google.protobuf.struct_pb2.Struct):
            Optional. A struct representation of the schema. This is
            populated for datasources with schemas that cannot be fully
            represented by the strongly-typed ``schema`` field.

            For Looker datasources, this maps to the LookmlModelExplore
            type:
            https://cloud.google.com/looker/docs/reference/looker-api/latest/types/LookmlModelExplore
    """

    bigquery_table_reference: "BigQueryTableReference" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="reference",
        message="BigQueryTableReference",
    )
    studio_datasource_id: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="reference",
    )
    looker_explore_reference: "LookerExploreReference" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="reference",
        message="LookerExploreReference",
    )
    alloy_db_reference: "AlloyDbReference" = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="reference",
        message="AlloyDbReference",
    )
    spanner_reference: "SpannerReference" = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="reference",
        message="SpannerReference",
    )
    cloud_sql_reference: "CloudSqlReference" = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="reference",
        message="CloudSqlReference",
    )
    bigtable_reference: "BigtableReference" = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof="reference",
        message="BigtableReference",
    )
    bigquery_property_graph_reference: "BigQueryPropertyGraphReference" = proto.Field(
        proto.MESSAGE,
        number=16,
        oneof="reference",
        message="BigQueryPropertyGraphReference",
    )
    firestore_reference: "FirestoreReference" = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="reference",
        message="FirestoreReference",
    )
    schema: "Schema" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="Schema",
    )
    struct_schema: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=10,
        message=struct_pb2.Struct,
    )


class Schema(proto.Message):
    r"""The schema of a Datasource or QueryResult instance.

    Attributes:
        fields (MutableSequence[google.cloud.geminidataanalytics_v1alpha.types.Field]):
            Optional. The fields in the schema.
        description (str):
            Optional. A textual description of the
            table's content and purpose. For example:
            "Contains information about customer orders in
            our e-commerce store." Currently only used for
            BigQuery data sources.
        synonyms (MutableSequence[str]):
            Optional. A list of alternative names or synonyms that can
            be used to refer to the table. For example: ["sales",
            "orders", "purchases"]. Currently only used for BigQuery
            data sources.
        tags (MutableSequence[str]):
            Optional. A list of tags or keywords associated with the
            table, used for categorization. For example: ["transaction",
            "revenue", "customer_data"]. Currently only used for
            BigQuery data sources.
        display_name (str):
            Optional. Table display_name (same as label in
            cloud/data_analytics/anarres/data/looker/proto/model_explore.proto),
            not required, currently only Looker has this field.
        filters (MutableSequence[google.cloud.geminidataanalytics_v1alpha.types.DataFilter]):
            Optional. The filters on the datasource's
            underlying data. Currently only used for Looker
            data sources.
    """

    fields: MutableSequence["Field"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Field",
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    synonyms: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    filters: MutableSequence["DataFilter"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="DataFilter",
    )


class Field(proto.Message):
    r"""A field in a schema.

    Attributes:
        name (str):
            Optional. The name of the field.
        type_ (str):
            Optional. The type of the field.
        description (str):
            Optional. A brief description of the field.
        mode (str):
            Optional. The mode of the field (e.g.,
            NULLABLE, REPEATED).
        synonyms (MutableSequence[str]):
            Optional. A list of alternative names or synonyms that can
            be used to refer to this field. For example: ["id",
            "customerid", "cust_id"]. Currently only used for BigQuery
            data sources.
        tags (MutableSequence[str]):
            Optional. A list of tags or keywords associated with the
            field, used for categorization. For example: ["identifier",
            "customer", "pii"]. Currently only used for BigQuery data
            sources.
        display_name (str):
            Optional. Field display_name (same as label in
        subfields (MutableSequence[google.cloud.geminidataanalytics_v1alpha.types.Field]):
            Optional. Recursive property for nested
            schema structures.
        category (str):
            Optional. Field category, not required,
            currently only useful for Looker.
        value_format (str):
            Optional. Looker only. Value format of the
            field. Ref:

            https://cloud.google.com/looker/docs/reference/param-field-value-format
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    mode: str = proto.Field(
        proto.STRING,
        number=4,
    )
    synonyms: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=8,
    )
    subfields: MutableSequence["Field"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="Field",
    )
    category: str = proto.Field(
        proto.STRING,
        number=10,
    )
    value_format: str = proto.Field(
        proto.STRING,
        number=11,
    )


class DataFilter(proto.Message):
    r"""A filter on a datasource's underlying data. Filter syntax
    documentation:
    https://cloud.google.com/looker/docs/filter-expressions

    Attributes:
        field (str):
            Optional. The field to filter on. For example:
            ["event_date", "customer_id", "product_category"]
        value (str):
            Optional. The default value used for this filter if the
            filter is not overridden in a query. For example: ["after
            2024-01-01", "123", "-fashion"]
        type_ (google.cloud.geminidataanalytics_v1alpha.types.DataFilterType):
            Optional. The type of filter present on a datasource, such
            as ALWAYS_FILTER.
    """

    field: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: str = proto.Field(
        proto.STRING,
        number=2,
    )
    type_: "DataFilterType" = proto.Field(
        proto.ENUM,
        number=3,
        enum="DataFilterType",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
