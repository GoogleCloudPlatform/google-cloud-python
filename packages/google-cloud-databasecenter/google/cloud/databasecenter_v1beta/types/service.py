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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.type.date_pb2 as date_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.databasecenter_v1beta.types import (
    affiliation,
    maintenance,
    metric_data,
    signals,
)
from google.cloud.databasecenter_v1beta.types import (
    machine_config as gcd_machine_config,
)
from google.cloud.databasecenter_v1beta.types import product as gcd_product

__protobuf__ = proto.module(
    package="google.cloud.databasecenter.v1beta",
    manifest={
        "Edition",
        "SubResourceType",
        "ManagementType",
        "ResourceCategory",
        "QueryProductsRequest",
        "QueryProductsResponse",
        "QueryDatabaseResourceGroupsRequest",
        "QueryDatabaseResourceGroupsResponse",
        "DatabaseResourceGroup",
        "DatabaseResource",
        "AggregateIssueStatsRequest",
        "AggregateQueryStatsRequest",
        "AggregateQueryStatsResponse",
        "AggregateIssueStatsResponse",
        "IssueGroupStats",
        "IssueStats",
        "Label",
        "AggregateFleetRequest",
        "QueryStatsInfo",
        "ResourceId",
        "QueryStats",
        "QueryMetrics",
        "AggregateFleetResponse",
        "AggregateFleetRow",
        "Dimension",
        "BackupDRConfig",
        "QueryIssuesRequest",
        "SignalProductsFilters",
        "QueryIssuesResponse",
        "DatabaseResourceIssue",
        "Tag",
        "ResourceDetails",
        "DeltaDetails",
    },
)


class Edition(proto.Enum):
    r"""Represents the edition of a database resource.

    Values:
        EDITION_UNSPECIFIED (0):
            Default, to make it consistent with instance
            edition enum.
        EDITION_ENTERPRISE (1):
            Represents the enterprise edition.
        EDITION_ENTERPRISE_PLUS (2):
            Represents the enterprise plus edition.
        EDITION_STANDARD (3):
            Represents the standard edition.
    """

    EDITION_UNSPECIFIED = 0
    EDITION_ENTERPRISE = 1
    EDITION_ENTERPRISE_PLUS = 2
    EDITION_STANDARD = 3


class SubResourceType(proto.Enum):
    r"""SubResourceType refers to the sub-type of database resource.

    Values:
        SUB_RESOURCE_TYPE_UNSPECIFIED (0):
            Unspecified.
        SUB_RESOURCE_TYPE_PRIMARY (1):
            A resource acting as a primary.
        SUB_RESOURCE_TYPE_SECONDARY (2):
            A resource acting as a secondary.
        SUB_RESOURCE_TYPE_READ_REPLICA (3):
            A resource acting as a read-replica.
        SUB_RESOURCE_TYPE_EXTERNAL_PRIMARY (5):
            A resource acting as an external primary.
        SUB_RESOURCE_TYPE_READ_POOL (6):
            A resource acting as a read pool.
        SUB_RESOURCE_TYPE_RESERVATION (7):
            Represents a reservation resource.
        SUB_RESOURCE_TYPE_DATASET (8):
            Represents a dataset resource.
        SUB_RESOURCE_TYPE_OTHER (4):
            For the rest of the categories.
    """

    SUB_RESOURCE_TYPE_UNSPECIFIED = 0
    SUB_RESOURCE_TYPE_PRIMARY = 1
    SUB_RESOURCE_TYPE_SECONDARY = 2
    SUB_RESOURCE_TYPE_READ_REPLICA = 3
    SUB_RESOURCE_TYPE_EXTERNAL_PRIMARY = 5
    SUB_RESOURCE_TYPE_READ_POOL = 6
    SUB_RESOURCE_TYPE_RESERVATION = 7
    SUB_RESOURCE_TYPE_DATASET = 8
    SUB_RESOURCE_TYPE_OTHER = 4


class ManagementType(proto.Enum):
    r"""The management type of the resource.

    Values:
        MANAGEMENT_TYPE_UNSPECIFIED (0):
            Unspecified.
        MANAGEMENT_TYPE_GCP_MANAGED (1):
            Google-managed resource.
        MANAGEMENT_TYPE_SELF_MANAGED (2):
            Self-managed resource.
    """

    MANAGEMENT_TYPE_UNSPECIFIED = 0
    MANAGEMENT_TYPE_GCP_MANAGED = 1
    MANAGEMENT_TYPE_SELF_MANAGED = 2


class ResourceCategory(proto.Enum):
    r"""The enum value corresponds to 'type' suffix in the resource_type
    field.

    Values:
        RESOURCE_CATEGORY_UNSPECIFIED (0):
            Unspecified.
        INSTANCE (1):
            A resource that is an Instance.
        CLUSTER (2):
            A resource that is a Cluster.
        DATABASE (3):
            A resource that is a Database.
        DATASET (4):
            A resource that is a Dataset.
        RESERVATION (5):
            A resource that is a Reservation.
    """

    RESOURCE_CATEGORY_UNSPECIFIED = 0
    INSTANCE = 1
    CLUSTER = 2
    DATABASE = 3
    DATASET = 4
    RESERVATION = 5


class QueryProductsRequest(proto.Message):
    r"""QueryProductsRequest is the request to get a list of
    products.

    Attributes:
        parent (str):
            Required. Parent can be a project, a folder, or an
            organization.

            The allowed values are:

            - projects/{PROJECT_ID}/locations/{LOCATION}
              (e.g.,"projects/foo-bar/locations/us-central1")
            - projects/{PROJECT_NUMBER}/locations/{LOCATION}
              (e.g.,"projects/12345678/locations/us-central1")
            - folders/{FOLDER_NUMBER}/locations/{LOCATION}
              (e.g.,"folders/1234567/locations/us-central1")
            - organizations/{ORGANIZATION_NUMBER}/locations/{LOCATION}
              (e.g.,"organizations/123456/locations/us-central1")
            - projects/{PROJECT_ID} (e.g., "projects/foo-bar")
            - projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
            - folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
            - organizations/{ORGANIZATION_NUMBER} (e.g.,
              "organizations/123456")
        page_size (int):
            Optional. If unspecified, at most 50 products
            will be returned. The maximum value is 1000;
            values above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListLocations`` call. Provide this to retrieve the
            subsequent page. All other parameters except page size
            should match the call that provided the page page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=3,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class QueryProductsResponse(proto.Message):
    r"""QueryProductsResponse represents the response containing a
    list of products.

    Attributes:
        products (MutableSequence[google.cloud.databasecenter_v1beta.types.Product]):
            List of database products returned.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages
        unreachable (MutableSequence[str]):
            Unordered list. List of unreachable regions
            from where data could not be retrieved.
    """

    @property
    def raw_page(self):
        return self

    products: MutableSequence[gcd_product.Product] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcd_product.Product,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class QueryDatabaseResourceGroupsRequest(proto.Message):
    r"""QueryDatabaseResourceGroupsRequest is the request to get a
    list of database groups.

    Attributes:
        parent (str):
            Required. Parent can be a project, a folder, or an
            organization. The search is limited to the resources within
            the ``scope``.

            The allowed values are:

            - projects/{PROJECT_ID} (e.g., "projects/foo-bar")
            - projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
            - folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
            - organizations/{ORGANIZATION_NUMBER} (e.g.,
              "organizations/123456")
        filter (str):
            Optional. The expression to filter resources.

            The following fields are filterable:

            - full_resource_name
            - resource_type
            - container
            - product.type
            - product.engine
            - product.version
            - location
            - labels
            - resource_category
            - machine_config.cpu_count
            - machine_config.memory_size_bytes
            - machine_config.shard_count
            - resource_name
            - tags
            - backupdr_config.backupdr_managed
            - edition

            The expression is a list of zero or more restrictions
            combined via logical operators ``AND`` and ``OR``. When
            ``AND`` and ``OR`` are both used in the expression,
            parentheses must be appropriately used to group the
            combinations.

            Example: ``location="us-east1"`` Example:
            ``container="projects/123" OR container="projects/456"``
            Example:
            ``(container="projects/123" OR container="projects/456") AND location="us-east1"``
            Example: ``full_resource_name=~"test"`` Example:
            ``full_resource_name=~"test.*master"``
        signal_type_groups (MutableSequence[google.cloud.databasecenter_v1beta.types.SignalTypeGroup]):
            Optional. Groups of signal types that are
            requested.
        signal_filters (MutableSequence[google.cloud.databasecenter_v1beta.types.SignalFilter]):
            Optional. Filters based on signals. The list will be ORed
            together and then ANDed with the ``filters`` field above.
        order_by (str):
            Optional. A field that specifies the sort order of the
            results.

            The following fields are sortable:

            - full_resource_name
            - product.type
            - product.engine
            - product.version
            - container
            - issue_count
            - machine_config.vcpu_count
            - machine_config.memory_size_bytes
            - machine_config.shard_count
            - resource_name
            - issue_severity
            - signal_type
            - location
            - resource_type
            - instance_type
            - edition
            - metrics.p99_cpu_utilization
            - metrics.p95_cpu_utilization
            - metrics.current_storage_used_bytes
            - metrics.node_count
            - metrics.processing_unit_count
            - metrics.current_memory_used_bytes
            - metrics.peak_storage_utilization
            - metrics.peak_number_connections
            - metrics.peak_memory_utilization

            The default order is ascending. Add "DESC" after the field
            name to indicate descending order. Add "ASC" after the field
            name to indicate ascending order. It only supports a single
            field at a time.

            For example: ``order_by = "full_resource_name"`` sorts
            response in ascending order
            ``order_by = "full_resource_name DESC"`` sorts response in
            descending order ``order_by = "issue_count DESC"`` sorts
            response in descending order of count of all issues
            associated with a resource.

            More explicitly,
            ``order_by = "full_resource_name, product"`` is not
            supported.
        page_size (int):
            Optional. If unspecified, at most 50 resource
            groups will be returned. The maximum value is
            1000; values above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``QueryDatabaseResourceGroupsRequest`` call. Provide this to
            retrieve the subsequent page. All parameters except
            page_token should match the parameters in the call that
            provided the page page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    signal_type_groups: MutableSequence[signals.SignalTypeGroup] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=signals.SignalTypeGroup,
    )
    signal_filters: MutableSequence[signals.SignalFilter] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=signals.SignalFilter,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=6,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=7,
    )


class QueryDatabaseResourceGroupsResponse(proto.Message):
    r"""QueryDatabaseResourceGroupsResponse represents the response
    message containing a list of resource groups.

    Attributes:
        resource_groups (MutableSequence[google.cloud.databasecenter_v1beta.types.DatabaseResourceGroup]):
            List of database resource groups that pass
            the filter.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Unordered list. List of unreachable regions
            from where data could not be retrieved.
    """

    @property
    def raw_page(self):
        return self

    resource_groups: MutableSequence["DatabaseResourceGroup"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DatabaseResourceGroup",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class DatabaseResourceGroup(proto.Message):
    r"""DatabaseResourceGroup represents all resources that serve a
    common data set. It is considered notionally as a single entity,
    powered by any number of units of compute and storage.

    Attributes:
        root_resources (MutableSequence[google.cloud.databasecenter_v1beta.types.DatabaseResource]):
            A database resource that serves as a root of
            the group of database resources. It is repeated
            just in case we have the concept of multiple
            roots in the future, however, it will only be
            populated with a single value for now.
        signal_groups (MutableSequence[google.cloud.databasecenter_v1beta.types.IssueCount]):
            The filtered signal groups and the count of
            issues associated with the resources that have
            been filtered in.
    """

    root_resources: MutableSequence["DatabaseResource"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DatabaseResource",
    )
    signal_groups: MutableSequence[signals.IssueCount] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=signals.IssueCount,
    )


class DatabaseResource(proto.Message):
    r"""DatabaseResource represents every individually configured
    database unit representing compute and/or storage.

    Attributes:
        child_resources (MutableSequence[google.cloud.databasecenter_v1beta.types.DatabaseResource]):
            List of children associated with a database
            group.
        full_resource_name (str):
            The full resource name, based on CAIS resource name format
            https://cloud.google.com/asset-inventory/docs/resource-name-format

            Example:

            ``//cloudsql.googleapis.com/projects/project-number/instances/mysql-1``
            ``//cloudsql.googleapis.com/projects/project-number/instances/postgres-1``
            ``//spanner.googleapis.com/projects/project-number/instances/spanner-instance-1``
            ``//alloydb.googleapis.com/projects/project-number/locations/us-central1/clusters/c1``
            ``//alloydb.googleapis.com/projects/project-number/locations/us-central1/clusters/c1/instances/i1``
        container (str):
            Specifies where the resource is created. For
            Google Cloud resources, it is the full name of
            the project.
        product (google.cloud.databasecenter_v1beta.types.Product):
            The product this resource represents.
        location (str):
            The location of the resources. It supports
            returning only regional locations in Google
            Cloud. These are of the form: "us-central1",
            "us-east1", etc. See
            https://cloud.google.com/about/locations for a
            list of such regions.
        labels (MutableSequence[google.cloud.databasecenter_v1beta.types.Label]):
            Labels applied on the resource. The
            requirements for labels assigned to Google Cloud
            resources may be found at
            https://cloud.google.com/resource-manager/docs/labels-overview#requirements
        tags (MutableSequence[google.cloud.databasecenter_v1beta.types.Tag]):
            Tags applied on the resource. The
            requirements for tags assigned to Google Cloud
            resources may be found at
            https://cloud.google.com/resource-manager/docs/tags/tags-overview
        resource_type (str):
            The type of resource defined according to the
            pattern: {Service Name}/{Type}. Ex:

            sqladmin.googleapis.com/Instance
            alloydb.googleapis.com/Cluster
            alloydb.googleapis.com/Instance
            spanner.googleapis.com/Instance
        sub_resource_type (google.cloud.databasecenter_v1beta.types.SubResourceType):
            Subtype of the resource specified at creation
            time.
        machine_config (google.cloud.databasecenter_v1beta.types.MachineConfig):
            Machine configuration like CPU, memory, etc
            for the resource.
        signal_groups (MutableSequence[google.cloud.databasecenter_v1beta.types.SignalGroup]):
            The list of signal groups and count of issues
            related to the resource. Only those signals
            which have been requested would be included.
        metrics (google.cloud.databasecenter_v1beta.types.Metrics):
            Observable metrics for the resource e.g. CPU
            utilization, memory utilization, etc.
        resource_category (google.cloud.databasecenter_v1beta.types.ResourceCategory):
            The category of the resource.
        resource_name (str):
            The name of the resource(The last part of the full resource
            name). Example: For full resource name -
            ``//cloudsql.googleapis.com/projects/project-number/instances/mysql-1``,
            resource name - ``mysql-1`` For full resource name -
            ``//cloudsql.googleapis.com/projects/project-number/instances/postgres-1``
            , resource name - ``postgres-1`` Note: In some cases, there
            might be more than one resource with the same resource name.
        backupdr_config (google.cloud.databasecenter_v1beta.types.BackupDRConfig):
            Optional. Backup and disaster recovery
            details for the resource.
        edition (google.cloud.databasecenter_v1beta.types.Edition):
            The edition of the resource.
        maintenance_info (google.cloud.databasecenter_v1beta.types.MaintenanceInfo):
            Optional. The maintenance information of the
            resource.
        affiliations (MutableSequence[google.cloud.databasecenter_v1beta.types.Affiliation]):
            Optional. Affiliation details of the
            resource.
    """

    child_resources: MutableSequence["DatabaseResource"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DatabaseResource",
    )
    full_resource_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    container: str = proto.Field(
        proto.STRING,
        number=4,
    )
    product: gcd_product.Product = proto.Field(
        proto.MESSAGE,
        number=5,
        message=gcd_product.Product,
    )
    location: str = proto.Field(
        proto.STRING,
        number=6,
    )
    labels: MutableSequence["Label"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="Label",
    )
    tags: MutableSequence["Tag"] = proto.RepeatedField(
        proto.MESSAGE,
        number=16,
        message="Tag",
    )
    resource_type: str = proto.Field(
        proto.STRING,
        number=8,
    )
    sub_resource_type: "SubResourceType" = proto.Field(
        proto.ENUM,
        number=9,
        enum="SubResourceType",
    )
    machine_config: gcd_machine_config.MachineConfig = proto.Field(
        proto.MESSAGE,
        number=12,
        message=gcd_machine_config.MachineConfig,
    )
    signal_groups: MutableSequence[signals.SignalGroup] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message=signals.SignalGroup,
    )
    metrics: metric_data.Metrics = proto.Field(
        proto.MESSAGE,
        number=13,
        message=metric_data.Metrics,
    )
    resource_category: "ResourceCategory" = proto.Field(
        proto.ENUM,
        number=14,
        enum="ResourceCategory",
    )
    resource_name: str = proto.Field(
        proto.STRING,
        number=15,
    )
    backupdr_config: "BackupDRConfig" = proto.Field(
        proto.MESSAGE,
        number=17,
        message="BackupDRConfig",
    )
    edition: "Edition" = proto.Field(
        proto.ENUM,
        number=18,
        enum="Edition",
    )
    maintenance_info: maintenance.MaintenanceInfo = proto.Field(
        proto.MESSAGE,
        number=19,
        message=maintenance.MaintenanceInfo,
    )
    affiliations: MutableSequence[affiliation.Affiliation] = proto.RepeatedField(
        proto.MESSAGE,
        number=20,
        message=affiliation.Affiliation,
    )


class AggregateIssueStatsRequest(proto.Message):
    r"""AggregateIssueStatsRequest represents the input to the
    AggregateIssueStats method.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. Parent can be a project, a folder, or an
            organization. The search is limited to the resources within
            the ``scope``.

            The allowed values are:

            - projects/{PROJECT_ID} (e.g., "projects/foo-bar")
            - projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
            - folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
            - organizations/{ORGANIZATION_NUMBER} (e.g.,
              "organizations/123456")
        filter (str):
            Optional. The expression to filter resources.

            Supported fields are: ``full_resource_name``,
            ``resource_type``, ``container``, ``product.type``,
            ``product.engine``, ``product.version``, ``location``,
            ``labels``, ``issues``, fields of availability_info,
            data_protection_info,'resource_name', etc.

            The expression is a list of zero or more restrictions
            combined via logical operators ``AND`` and ``OR``. When
            ``AND`` and ``OR`` are both used in the expression,
            parentheses must be appropriately used to group the
            combinations.

            Example: ``location="us-east1"`` Example:
            ``container="projects/123" OR container="projects/456"``
            Example:
            ``(container="projects/123" OR container="projects/456") AND location="us-east1"``
        signal_type_groups (MutableSequence[google.cloud.databasecenter_v1beta.types.SignalTypeGroup]):
            Optional. Lists of signal types that are
            issues.
        baseline_date (google.type.date_pb2.Date):
            Optional. The baseline date w.r.t. which the
            delta counts are calculated. If not set, delta
            counts are not included in the response and the
            response indicates the current state of the
            fleet.

            This field is a member of `oneof`_ ``_baseline_date``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    signal_type_groups: MutableSequence[signals.SignalTypeGroup] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=signals.SignalTypeGroup,
    )
    baseline_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message=date_pb2.Date,
    )


class AggregateQueryStatsRequest(proto.Message):
    r"""AggregateQueryStatsRequest represents the input to the
    AggregateQueryStats method.

    Attributes:
        parent (str):
            Required. Parent can be a project, a folder, or an
            organization. The search is limited to the resources within
            the ``parent``.

            The allowed values are:

            - projects/{PROJECT_ID} (e.g., "projects/foo-bar")
            - projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
            - folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
            - organizations/{ORGANIZATION_NUMBER} (e.g.,
              "organizations/123456")
        order_by (str):
            Optional. The expression to order the results by. Example:
            ``order_by="execution_count"`` Example:
            ``order_by="execution_count desc"`` Supported order by
            fields are ``execution_count``, ``rows_processed``,
            ``total_cpu_time``, ``avg_cpu_time``.
        filter (str):
            Optional. The expression to filter resources.

            Supported fields are: ``full_resource_name``,
            ``resource_type``, ``container``, ``product.type``,
            ``product.engine``, ``product.version``, ``location``,
            ``labels``, ``issues``, fields of availability_info,
            data_protection_info,'resource_name', etc.

            The expression is a list of zero or more restrictions
            combined via logical operators ``AND`` and ``OR``. When
            ``AND`` and ``OR`` are both used in the expression,
            parentheses must be appropriately used to group the
            combinations.

            Example: ``location="us-east1"`` Example:
            ``container="projects/123" OR container="projects/456"``
            Example:
            ``(container="projects/123" OR container="projects/456") AND location="us-east1"``
            Additional specific fields for query stats are:
            ``metric_window``, ``query_hash``, ``normalized_query``.
            Example: ``metric_window="LAST_ONE_DAY"`` (Possible values
            for ``metric_window`` are: ``LAST_ONE_DAY``,
            ``LAST_ONE_WEEK``, ``LAST_TWO_WEEKS``) Example:
            ``query_hash="12345678"`` Example:
            ``normalized_query="SELECT * FROM table"``
        page_size (int):
            Optional. If unspecified, at most 100 query
            stats will be returned. The maximum value is
            1000; values above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``AggregateQueryStatsRequest`` call. Provide this to
            retrieve the subsequent page. All parameters except
            page_token should match the parameters in the call that
            provided the page token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=2,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=3,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=5,
    )


class AggregateQueryStatsResponse(proto.Message):
    r"""The response message containing relevant query stats
    for database resources.

    Attributes:
        query_stats (MutableSequence[google.cloud.databasecenter_v1beta.types.QueryStatsInfo]):
            List of query stats where each group contains
            stats for resources having a particular
            combination of relevant query stats.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Unordered list. List of unreachable regions
            from where data could not be retrieved.
    """

    @property
    def raw_page(self):
        return self

    query_stats: MutableSequence["QueryStatsInfo"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="QueryStatsInfo",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class AggregateIssueStatsResponse(proto.Message):
    r"""The response message containing one of more group of relevant
    health issues for database resources.

    Attributes:
        issue_group_stats (MutableSequence[google.cloud.databasecenter_v1beta.types.IssueGroupStats]):
            List of issue group stats where each group
            contains stats for resources having a particular
            combination of relevant issues.
        total_resources_count (int):
            Total count of the resources filtered in
            based on the user given filter.
        total_resource_groups_count (int):
            Total count of the resource filtered in based
            on the user given filter.
        unreachable (MutableSequence[str]):
            Unordered list. List of unreachable regions
            from where data could not be retrieved.
    """

    issue_group_stats: MutableSequence["IssueGroupStats"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="IssueGroupStats",
    )
    total_resources_count: int = proto.Field(
        proto.INT32,
        number=2,
    )
    total_resource_groups_count: int = proto.Field(
        proto.INT32,
        number=3,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


class IssueGroupStats(proto.Message):
    r"""IssueGroupStats refers to stats for a particulare combination
    of relevant health issues of database resources.

    Attributes:
        display_name (str):
            Database resource level health card name.
            This will corresponds to one of the requested
            input group names.
        resource_groups_count (int):
            Total count of the groups of resources
            returned by the filter that also have one or
            more resources for which any of the specified
            issues are applicable.
        resources_count (int):
            Total count of resources returned by the
            filter for which any of the specified issues are
            applicable.
        healthy_resource_groups_count (int):
            The number of resource groups from the total
            groups as defined above that are healthy with
            respect to all of the specified issues.
        healthy_resources_count (int):
            The number of resources from the total defined above in
            field total_resources_count that are healthy with respect to
            all of the specified issues.
        issue_stats (MutableSequence[google.cloud.databasecenter_v1beta.types.IssueStats]):
            List of issues stats containing count of
            resources having particular issue category.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    resource_groups_count: int = proto.Field(
        proto.INT32,
        number=2,
    )
    resources_count: int = proto.Field(
        proto.INT32,
        number=3,
    )
    healthy_resource_groups_count: int = proto.Field(
        proto.INT32,
        number=4,
    )
    healthy_resources_count: int = proto.Field(
        proto.INT32,
        number=5,
    )
    issue_stats: MutableSequence["IssueStats"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="IssueStats",
    )


class IssueStats(proto.Message):
    r"""IssueStats holds stats for a particular signal category.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        signal_type (google.cloud.databasecenter_v1beta.types.SignalType):
            Type of signal which is an issue.
        resource_count (int):
            Number of resources having issues of a given
            type.
        delta_details (google.cloud.databasecenter_v1beta.types.DeltaDetails):
            Optional. Delta counts and details of
            resources for which issue was raised or fixed.

            This field is a member of `oneof`_ ``_delta_details``.
        issue_severity (google.cloud.databasecenter_v1beta.types.IssueSeverity):
            Severity of the issue.

            This field is a member of `oneof`_ ``_issue_severity``.
    """

    signal_type: signals.SignalType = proto.Field(
        proto.ENUM,
        number=1,
        enum=signals.SignalType,
    )
    resource_count: int = proto.Field(
        proto.INT32,
        number=2,
    )
    delta_details: "DeltaDetails" = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message="DeltaDetails",
    )
    issue_severity: signals.IssueSeverity = proto.Field(
        proto.ENUM,
        number=4,
        optional=True,
        enum=signals.IssueSeverity,
    )


class Label(proto.Message):
    r"""Label is a key value pair applied to a resource.

    Attributes:
        key (str):
            The key part of the label.
        value (str):
            The value part of the label.
        source (str):
            The source of the Label. Source is empty if
            the label is directly attached to the resource
            and not inherited.
    """

    key: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: str = proto.Field(
        proto.STRING,
        number=2,
    )
    source: str = proto.Field(
        proto.STRING,
        number=3,
    )


class AggregateFleetRequest(proto.Message):
    r"""The request message to aggregate fleet which are grouped by a
    field.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. Parent can be a project, a folder, or an
            organization. The search is limited to the resources within
            the ``scope``.

            The allowed values are:

            - projects/{PROJECT_ID} (e.g., "projects/foo-bar")
            - projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
            - folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
            - organizations/{ORGANIZATION_NUMBER} (e.g.,
              "organizations/123456")
        filter (str):
            Optional. The expression to filter resources.

            Supported fields are: ``full_resource_name``,
            ``resource_type``, ``container``, ``product.type``,
            ``product.engine``, ``product.version``, ``location``,
            ``labels``, ``issues``, fields of availability_info,
            data_protection_info, 'resource_name', etc.

            The expression is a list of zero or more restrictions
            combined via logical operators ``AND`` and ``OR``. When
            ``AND`` and ``OR`` are both used in the expression,
            parentheses must be appropriately used to group the
            combinations.

            Example: ``location="us-east1"`` Example:
            ``container="projects/123" OR container="projects/456"``
            Example:
            ``(container="projects/123" OR container="projects/456") AND location="us-east1"``
        group_by (str):
            Optional. A field that statistics are grouped by. Valid
            values are any combination of the following:

            - container
            - product.type
            - product.engine
            - product.version
            - location
            - sub_resource_type
            - management_type
            - tag.key
            - tag.value
            - tag.source
            - tag.inherited
            - label.key
            - label.value
            - label.source
            - has_maintenance_schedule
            - has_deny_maintenance_schedules Comma separated list.
        order_by (str):
            Optional. Valid values to order by are:

            - resource_groups_count
            - resources_count
            - and all fields supported by ``group_by`` The default order
              is ascending. Add "DESC" after the field name to indicate
              descending order. Add "ASC" after the field name to
              indicate ascending order. It supports ordering using
              multiple fields. For example:
              ``order_by = "resource_groups_count"`` sorts response in
              ascending order
              ``order_by = "resource_groups_count DESC"`` sorts response
              in descending order
              ``order_by = "product.type, product.version DESC, location"``
              orders by type in ascending order, version in descending
              order and location in ascending order
        page_size (int):
            Optional. If unspecified, at most 50 items
            will be returned. The maximum value is 1000;
            values above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``AggregateFleet`` call. Provide this to retrieve the
            subsequent page. All other parameters should match the
            parameters in the call that provided the page token except
            for page_size which can be different.
        baseline_date (google.type.date_pb2.Date):
            Optional. The baseline date w.r.t. which the
            delta counts are calculated. If not set, delta
            counts are not included in the response and the
            response indicates the current state of the
            fleet.

            This field is a member of `oneof`_ ``_baseline_date``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    group_by: str = proto.Field(
        proto.STRING,
        number=3,
    )
    order_by: str = proto.Field(
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
    baseline_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=7,
        optional=True,
        message=date_pb2.Date,
    )


class QueryStatsInfo(proto.Message):
    r"""QueryStatsInfo contains the aggregated and detailed query
    stats for a particular combination of relevant query stats for
    queries having same normalized query.

    Attributes:
        aggregated_query_stats (google.cloud.databasecenter_v1beta.types.QueryStats):
            Aggregated query stats for the resources for
            same normalized query.
        query_stats (MutableSequence[google.cloud.databasecenter_v1beta.types.QueryStats]):
            List of query stats for the resources in the
            group. This stats is stats at resource level for
            the resources having same normalized query.
    """

    aggregated_query_stats: "QueryStats" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="QueryStats",
    )
    query_stats: MutableSequence["QueryStats"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="QueryStats",
    )


class ResourceId(proto.Message):
    r"""ResourceId contains the identifier for a database resource,
    including the full resource name, resource type, and product.

    Attributes:
        full_resource_name (str):
            The full resource name of the resource.
        resource_type (str):
            The type of the resource.
            sqladmin.googleapis.com/Instance
            alloydb.googleapis.com/Cluster
            alloydb.googleapis.com/Instance
        product (google.cloud.databasecenter_v1beta.types.Product):
            The product of the resource, including the
            type, engine, and version.
    """

    full_resource_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    resource_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    product: gcd_product.Product = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcd_product.Product,
    )


class QueryStats(proto.Message):
    r"""QueryStats contains the stats for a particular combination of
    query_hash, query_string and resource_type.

    Attributes:
        query_hash (str):
            The query hash of the query.
        normalized_query (str):
            The query string is normalized query without
            any PII data.
        resource_type (str):
            The type of the resource.
            sqladmin.googleapis.com/Instance
            alloydb.googleapis.com/Cluster
            alloydb.googleapis.com/Instance
        resource_ids (MutableSequence[google.cloud.databasecenter_v1beta.types.ResourceId]):
            The resource ids for which the query stats
            are collected.
        query_metrics (google.cloud.databasecenter_v1beta.types.QueryMetrics):
            Metrics related to the query performance.
        inefficient_query_info (google.cloud.databasecenter_v1beta.types.InefficientQueryInfo):
            Information about inefficient query.
    """

    query_hash: str = proto.Field(
        proto.STRING,
        number=1,
    )
    normalized_query: str = proto.Field(
        proto.STRING,
        number=2,
    )
    resource_type: str = proto.Field(
        proto.STRING,
        number=4,
    )
    resource_ids: MutableSequence["ResourceId"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="ResourceId",
    )
    query_metrics: "QueryMetrics" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="QueryMetrics",
    )
    inefficient_query_info: signals.InefficientQueryInfo = proto.Field(
        proto.MESSAGE,
        number=7,
        message=signals.InefficientQueryInfo,
    )


class QueryMetrics(proto.Message):
    r"""QueryMetrics contains the metrics related to the query
    execution.

    Attributes:
        execution_count (int):
            The number of times the query was executed.
        avg_cpu_time (google.protobuf.duration_pb2.Duration):
            The average execution period of the query
            across all runs.
        total_cpu_time (google.protobuf.duration_pb2.Duration):
            The total CPU time consumed by the query
            across all runs.
        rows_processed (int):
            The average number of rows processed by the
            query across all runs.
        metrics_window (google.cloud.databasecenter_v1beta.types.QueryMetrics.MetricsWindow):
            The window over which the metrics are
            aggregated.
    """

    class MetricsWindow(proto.Enum):
        r"""Enum to represent the window over which the metrics are
        aggregated.

        Values:
            METRICS_WINDOW_UNSPECIFIED (0):
                Unspecified. Default value.
            LAST_ONE_DAY (1):
                Metrics are aggregated over the last 1 day.
            LAST_ONE_WEEK (2):
                Metrics are aggregated over the last 7 days.
            LAST_TWO_WEEKS (3):
                Metrics are aggregated over the last 14 days.
        """

        METRICS_WINDOW_UNSPECIFIED = 0
        LAST_ONE_DAY = 1
        LAST_ONE_WEEK = 2
        LAST_TWO_WEEKS = 3

    execution_count: int = proto.Field(
        proto.INT64,
        number=1,
    )
    avg_cpu_time: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    total_cpu_time: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )
    rows_processed: int = proto.Field(
        proto.INT64,
        number=4,
    )
    metrics_window: MetricsWindow = proto.Field(
        proto.ENUM,
        number=5,
        enum=MetricsWindow,
    )


class AggregateFleetResponse(proto.Message):
    r"""The response message to aggregate a fleet by some group by
    fields.

    Attributes:
        rows (MutableSequence[google.cloud.databasecenter_v1beta.types.AggregateFleetRow]):
            Represents a row grouped by the fields in the
            input.
        resource_groups_total_count (int):
            Count of all resource groups in the fleet.
            This includes counts from all pages.
        resource_total_count (int):
            Count of all resources in the fleet. This
            includes counts from all pages.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Unordered list. List of unreachable regions
            from where data could not be retrieved.
    """

    @property
    def raw_page(self):
        return self

    rows: MutableSequence["AggregateFleetRow"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AggregateFleetRow",
    )
    resource_groups_total_count: int = proto.Field(
        proto.INT32,
        number=2,
    )
    resource_total_count: int = proto.Field(
        proto.INT32,
        number=3,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )


class AggregateFleetRow(proto.Message):
    r"""Individual row grouped by a particular dimension.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        dimension (MutableSequence[google.cloud.databasecenter_v1beta.types.Dimension]):
            Group by dimension.
        resource_groups_count (int):
            Number of resource groups that have a
            particular dimension.
        resources_count (int):
            Number of resources that have a particular
            dimension.
        delta_details (google.cloud.databasecenter_v1beta.types.DeltaDetails):
            Optional. Delta counts and details of
            resources which were added to/deleted from
            fleet.

            This field is a member of `oneof`_ ``_delta_details``.
    """

    dimension: MutableSequence["Dimension"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Dimension",
    )
    resource_groups_count: int = proto.Field(
        proto.INT32,
        number=2,
    )
    resources_count: int = proto.Field(
        proto.INT32,
        number=3,
    )
    delta_details: "DeltaDetails" = proto.Field(
        proto.MESSAGE,
        number=4,
        optional=True,
        message="DeltaDetails",
    )


class Dimension(proto.Message):
    r"""Dimension used to aggregate the fleet.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        container (str):
            Specifies where the resource is created. For
            Google Cloud resources, it is the full name of
            the project.

            This field is a member of `oneof`_ ``dimension``.
        product_type (google.cloud.databasecenter_v1beta.types.ProductType):
            Type to identify a product

            This field is a member of `oneof`_ ``dimension``.
        product_engine (google.cloud.databasecenter_v1beta.types.Engine):
            Engine refers to underlying database binary
            running in an instance.

            This field is a member of `oneof`_ ``dimension``.
        product_version (str):
            Version of the underlying database engine

            This field is a member of `oneof`_ ``dimension``.
        location (str):
            The location of the resources. It supports
            returning only regional locations in Google
            Cloud.

            This field is a member of `oneof`_ ``dimension``.
        resource_type (str):
            The type of resource defined according to the
            pattern: {Service Name}/{Type}. Ex:

            sqladmin.googleapis.com/Instance
            alloydb.googleapis.com/Cluster
            alloydb.googleapis.com/Instance
            spanner.googleapis.com/Instance

            This field is a member of `oneof`_ ``dimension``.
        sub_resource_type (google.cloud.databasecenter_v1beta.types.SubResourceType):
            Subtype of the resource specified at creation
            time.

            This field is a member of `oneof`_ ``dimension``.
        resource_category (google.cloud.databasecenter_v1beta.types.ResourceCategory):
            The category of the resource.

            This field is a member of `oneof`_ ``dimension``.
        management_type (google.cloud.databasecenter_v1beta.types.ManagementType):
            The management type of the resource.

            This field is a member of `oneof`_ ``dimension``.
        edition (google.cloud.databasecenter_v1beta.types.Edition):
            The edition of the resource.

            This field is a member of `oneof`_ ``dimension``.
        tag_key (str):
            Tag key of the resource.

            This field is a member of `oneof`_ ``dimension``.
        tag_value (str):
            Tag value of the resource.

            This field is a member of `oneof`_ ``dimension``.
        tag_source (str):
            Tag source of the resource.

            This field is a member of `oneof`_ ``dimension``.
        tag_inherited (bool):
            Tag inheritance value of the resource.

            This field is a member of `oneof`_ ``dimension``.
        label_key (str):
            Label key of the resource.

            This field is a member of `oneof`_ ``dimension``.
        label_value (str):
            Label value of the resource.

            This field is a member of `oneof`_ ``dimension``.
        label_source (str):
            Label source of the resource.

            This field is a member of `oneof`_ ``dimension``.
        has_maintenance_schedule (bool):
            Whether the resource has a maintenance
            schedule.

            This field is a member of `oneof`_ ``dimension``.
        has_deny_maintenance_schedules (bool):
            Whether the resource has deny maintenance
            schedules.

            This field is a member of `oneof`_ ``dimension``.
    """

    container: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="dimension",
    )
    product_type: gcd_product.ProductType = proto.Field(
        proto.ENUM,
        number=3,
        oneof="dimension",
        enum=gcd_product.ProductType,
    )
    product_engine: gcd_product.Engine = proto.Field(
        proto.ENUM,
        number=4,
        oneof="dimension",
        enum=gcd_product.Engine,
    )
    product_version: str = proto.Field(
        proto.STRING,
        number=5,
        oneof="dimension",
    )
    location: str = proto.Field(
        proto.STRING,
        number=6,
        oneof="dimension",
    )
    resource_type: str = proto.Field(
        proto.STRING,
        number=7,
        oneof="dimension",
    )
    sub_resource_type: "SubResourceType" = proto.Field(
        proto.ENUM,
        number=8,
        oneof="dimension",
        enum="SubResourceType",
    )
    resource_category: "ResourceCategory" = proto.Field(
        proto.ENUM,
        number=9,
        oneof="dimension",
        enum="ResourceCategory",
    )
    management_type: "ManagementType" = proto.Field(
        proto.ENUM,
        number=10,
        oneof="dimension",
        enum="ManagementType",
    )
    edition: "Edition" = proto.Field(
        proto.ENUM,
        number=11,
        oneof="dimension",
        enum="Edition",
    )
    tag_key: str = proto.Field(
        proto.STRING,
        number=12,
        oneof="dimension",
    )
    tag_value: str = proto.Field(
        proto.STRING,
        number=13,
        oneof="dimension",
    )
    tag_source: str = proto.Field(
        proto.STRING,
        number=14,
        oneof="dimension",
    )
    tag_inherited: bool = proto.Field(
        proto.BOOL,
        number=15,
        oneof="dimension",
    )
    label_key: str = proto.Field(
        proto.STRING,
        number=16,
        oneof="dimension",
    )
    label_value: str = proto.Field(
        proto.STRING,
        number=17,
        oneof="dimension",
    )
    label_source: str = proto.Field(
        proto.STRING,
        number=18,
        oneof="dimension",
    )
    has_maintenance_schedule: bool = proto.Field(
        proto.BOOL,
        number=19,
        oneof="dimension",
    )
    has_deny_maintenance_schedules: bool = proto.Field(
        proto.BOOL,
        number=20,
        oneof="dimension",
    )


class BackupDRConfig(proto.Message):
    r"""BackupDRConfig to capture the backup and disaster recovery
    details of database resource.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        backupdr_managed (bool):
            Indicates if the resource is managed by
            BackupDR.

            This field is a member of `oneof`_ ``_backupdr_managed``.
    """

    backupdr_managed: bool = proto.Field(
        proto.BOOL,
        number=1,
        optional=True,
    )


class QueryIssuesRequest(proto.Message):
    r"""QueryIssuesRequest is the request to get a list of issues.

    Attributes:
        parent (str):
            Required. Parent can be a project, a folder, or an
            organization. The list is limited to the one attached to
            resources within the ``scope`` that a user has access to.

            The allowed values are:

            - projects/{PROJECT_ID} (e.g., "projects/foo-bar")
            - projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
            - folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
            - organizations/{ORGANIZATION_NUMBER} (e.g.,
              "organizations/123456")
        filter (str):
            Optional. Supported fields are: 'product', ``location``,
            ``issue_severity``, 'tags', 'labels',
        signal_products_filters (MutableSequence[google.cloud.databasecenter_v1beta.types.SignalProductsFilters]):
            Optional. Filters based on signal and
            product. The filter list will be ORed across
            pairs and ANDed within a signal and products
            pair.
        order_by (str):
            Optional. Following fields are sortable:

            SignalType
            Product
            Location
            IssueSeverity

            The default order is ascending. Add "DESC" after
            the field name to indicate descending order. Add
            "ASC" after the field name to indicate ascending
            order. It only supports a single field at a
            time.
        page_size (int):
            Optional. If unspecified, at most 50 issues
            will be returned. The maximum value is 1000;
            values above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``QueryIssues`` call. Provide this to retrieve the
            subsequent page. All parameters except page size should
            match the parameters used in the call that provided the page
            token.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    signal_products_filters: MutableSequence["SignalProductsFilters"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="SignalProductsFilters",
        )
    )
    order_by: str = proto.Field(
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


class SignalProductsFilters(proto.Message):
    r"""SignalProductsFilters represents a signal and list of
    supported products.

    Attributes:
        signal_type (google.cloud.databasecenter_v1beta.types.SignalType):
            Optional. The type of signal.
        products (MutableSequence[google.cloud.databasecenter_v1beta.types.Product]):
            Optional. Product type of the resource. The
            version of the product will be ignored in
            filtering.
    """

    signal_type: signals.SignalType = proto.Field(
        proto.ENUM,
        number=1,
        enum=signals.SignalType,
    )
    products: MutableSequence[gcd_product.Product] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=gcd_product.Product,
    )


class QueryIssuesResponse(proto.Message):
    r"""QueryIssuesResponse is the response containing a list of
    issues.

    Attributes:
        resource_issues (MutableSequence[google.cloud.databasecenter_v1beta.types.DatabaseResourceIssue]):
            List of issues and resource details.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Unordered list. List of unreachable regions
            from where data could not be retrieved.
    """

    @property
    def raw_page(self):
        return self

    resource_issues: MutableSequence["DatabaseResourceIssue"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DatabaseResourceIssue",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class DatabaseResourceIssue(proto.Message):
    r"""DatabaseResource and Issue associated with it.

    Attributes:
        signal (google.cloud.databasecenter_v1beta.types.Signal):
            Signal associated with the issue.
        resource (google.cloud.databasecenter_v1beta.types.DatabaseResource):
            Resource associated with the issue.
    """

    signal: signals.Signal = proto.Field(
        proto.MESSAGE,
        number=1,
        message=signals.Signal,
    )
    resource: "DatabaseResource" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DatabaseResource",
    )


class Tag(proto.Message):
    r"""Tag is a key value pair attached to a resource.

    Attributes:
        key (str):

        value (str):
            The value part of the tag.
        source (str):
            The source of the tag. According to
            https://cloud.google.com/resource-manager/docs/tags/tags-overview#tags_and_labels,
            tags can be created only at the project or organization
            level. Tags can be inherited from different project as well
            not just the current project where the database resource is
            present. Format: "projects/{PROJECT_ID}",
            "projects/{PROJECT_NUMBER}",
            "organizations/{ORGANIZATION_ID}".
        inherited (bool):
            Indicates the inheritance status of a tag
            value attached to the given resource. If the tag
            value is inherited from one of the resource's
            ancestors, inherited will be true. If false,
            then the tag value is directly attached to the
            resource.
    """

    key: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: str = proto.Field(
        proto.STRING,
        number=2,
    )
    source: str = proto.Field(
        proto.STRING,
        number=3,
    )
    inherited: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class ResourceDetails(proto.Message):
    r"""Capture the resource details for resources that are included
    in the delta counts.

    Attributes:
        full_resource_name (str):
            Full resource name of the resource.
        container (str):
            Specifies where the resource is created. For
            Google Cloud resources, it is the full name of
            the project.
        product (google.cloud.databasecenter_v1beta.types.Product):
            Product type of the resource.
        location (str):
            Location of the resource.
    """

    full_resource_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    container: str = proto.Field(
        proto.STRING,
        number=2,
    )
    product: gcd_product.Product = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcd_product.Product,
    )
    location: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeltaDetails(proto.Message):
    r"""Captures the details of items that have increased or
    decreased in some bucket when compared to some point in history.
    It is currently used to capture the delta of resources that have
    been added or removed in the fleet as well as to capture the
    resources that have a change in Issue/Signal status.

    Attributes:
        increased_resources (MutableSequence[google.cloud.databasecenter_v1beta.types.ResourceDetails]):
            Details of resources that have increased.
        decreased_resources (MutableSequence[google.cloud.databasecenter_v1beta.types.ResourceDetails]):
            Details of resources that have decreased.
    """

    increased_resources: MutableSequence["ResourceDetails"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ResourceDetails",
    )
    decreased_resources: MutableSequence["ResourceDetails"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="ResourceDetails",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
