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
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.biglake.v1",
    manifest={
        "IcebergCatalog",
        "CreateIcebergCatalogRequest",
        "UpdateIcebergCatalogRequest",
        "GetIcebergCatalogRequest",
        "ListIcebergCatalogsRequest",
        "ListIcebergCatalogsResponse",
        "FailoverIcebergCatalogRequest",
        "FailoverIcebergCatalogResponse",
        "TableIdentifier",
        "IcebergNamespaceUpdate",
        "StorageCredential",
    },
)


class IcebergCatalog(proto.Message):
    r"""The Iceberg REST Catalog information.

    Attributes:
        name (str):
            Identifier. The catalog name,
            ``projects/my-project/catalogs/my-catalog``. This field is
            immutable. This field is ignored for CreateIcebergCatalog.
        credential_mode (google.cloud.biglake_v1.types.IcebergCatalog.CredentialMode):
            Optional. The credential mode for the
            catalog.
        biglake_service_account (str):
            Output only. The service account used for
            credential vending, output only. Might be empty
            if Credential vending was never enabled for the
            catalog. For federated catalogs, the service
            account will be always provisioned and will be
            used to access the remote Iceberg REST Catalog
            using access to Secret Manager secret or
            identity federation.
        biglake_service_account_unique_id (str):
            Output only. The unique ID of the service
            account. This is used for federation scenarios.
        catalog_type (google.cloud.biglake_v1.types.IcebergCatalog.CatalogType):
            Required. The catalog type. Required for
            CreateIcebergCatalog.
        default_location (str):
            Optional. The default storage location for the catalog,
            e.g., ``gs://my-bucket``. For Google Cloud Storage bucket
            catalogs, this is output only.

            For BigLake catalogs, this field must be provided and point
            to a Google Cloud Storage bucket or a path within that
            bucket. This path serves as the base directory for
            constructing the full path to a table's data and metadata
            directories when a location is not specified at the
            namespace or table level. The full path is formed by
            appending the namespace and table identifiers to the default
            location.
        storage_regions (MutableSequence[str]):
            Output only. The GCP region(s) of the default location's
            bucket, e.g. ``us-central1``, ``nam4`` or ``us``. This will
            contain one value for all locations, except for the catalogs
            that are configured to use custom dual region buckets, in
            which case it will contain the two regions of the bucket.
            The region(s) of this field should be in the jurisdiction of
            or nearby the primary location of the catalog.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the catalog was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the catalog was last
            updated.
        replicas (MutableSequence[google.cloud.biglake_v1.types.IcebergCatalog.Replica]):
            Output only. The replicas for the catalog
            metadata.
        description (str):
            Optional. A user-provided description of the
            catalog. The description must be a UTF-8 string
            with a maximum length of 1024 characters.
        restricted_locations_config (google.cloud.biglake_v1.types.IcebergCatalog.RestrictedLocationsConfig):
            Optional. Restricted locations configuration. This field is
            currently only used for BigLake catalogs.

            If this field is unset, or if
            ``restricted_locations_config.restricted_locations`` is
            empty, all accessible locations are allowed. If
            ``restricted_locations_config.restricted_locations`` is not
            empty, only locations in ``default_location`` and
            ``restricted_locations_config.restricted_locations`` are
            allowed.
        federated_catalog_options (google.cloud.biglake_v1.types.IcebergCatalog.FederatedCatalogOptions):
            Optional. Configuration options for federated
            catalogs.
    """

    class CatalogType(proto.Enum):
        r"""Determines the catalog type.

        Values:
            CATALOG_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            CATALOG_TYPE_GCS_BUCKET (1):
                Google Cloud Storage bucket catalog type.
            CATALOG_TYPE_BIGLAKE (3):
                BigLake catalog type.
            CATALOG_TYPE_FEDERATED (4):
                Federated catalog type.
        """

        CATALOG_TYPE_UNSPECIFIED = 0
        CATALOG_TYPE_GCS_BUCKET = 1
        CATALOG_TYPE_BIGLAKE = 3
        CATALOG_TYPE_FEDERATED = 4

    class CredentialMode(proto.Enum):
        r"""The credential mode used for the catalog.

        Values:
            CREDENTIAL_MODE_UNSPECIFIED (0):
                Default value. This value is unused.
            CREDENTIAL_MODE_END_USER (1):
                End user credentials, default. The
                authenticating user must have access to the
                catalog resources and the corresponding Google
                Cloud Storage files.
            CREDENTIAL_MODE_VENDED_CREDENTIALS (2):
                Use credential vending. The authenticating user must have
                access to the catalog resources and the system will provide
                the caller with downscoped credentials to access the Google
                Cloud Storage files. All table operations in this mode would
                require ``X-Iceberg-Access-Delegation`` header with
                ``vended-credentials`` value included. System will generate
                a service account and the catalog administrator must grant
                the service account appropriate permissions.

                See:
                https://github.com/apache/iceberg/blob/931865ecaf40a827f9081dddb675bf1c95c05461/open-api/rest-catalog-open-api.yaml#L1854
                for more details.
        """

        CREDENTIAL_MODE_UNSPECIFIED = 0
        CREDENTIAL_MODE_END_USER = 1
        CREDENTIAL_MODE_VENDED_CREDENTIALS = 2

    class Replica(proto.Message):
        r"""The replica of the Catalog.

        Attributes:
            region (str):
                Output only. The region of the replica. For
                example "us-east1".
            state (google.cloud.biglake_v1.types.IcebergCatalog.Replica.State):
                Output only. The current state of the
                replica.
        """

        class State(proto.Enum):
            r"""If the catalog is replicated to multiple regions, this enum
            describes the current state of the replica.

            Values:
                STATE_UNKNOWN (0):
                    The replica state is unknown.
                STATE_PRIMARY (1):
                    The replica is the writable primary.
                STATE_PRIMARY_IN_PROGRESS (2):
                    The replica has been recently assigned as the
                    primary, but not all namespaces are writeable
                    yet.
                STATE_SECONDARY (3):
                    The replica is a read-only secondary replica.
            """

            STATE_UNKNOWN = 0
            STATE_PRIMARY = 1
            STATE_PRIMARY_IN_PROGRESS = 2
            STATE_SECONDARY = 3

        region: str = proto.Field(
            proto.STRING,
            number=1,
        )
        state: "IcebergCatalog.Replica.State" = proto.Field(
            proto.ENUM,
            number=2,
            enum="IcebergCatalog.Replica.State",
        )

    class RestrictedLocationsConfig(proto.Message):
        r"""Configuration of location restrictions.

        Attributes:
            restricted_locations (MutableSequence[str]):
                Optional. Additional Google Cloud Storage buckets and
                locations (e.g., ``gs://my-other-bucket/...``) that are
                permitted for use by resources within a catalog. This field
                is currently only used for BigLake catalogs.

                If ``restricted_locations`` is empty and unrestricted
                catalog creation is enabled, all accessible locations are
                allowed. Otherwise, only ``default_location`` and locations
                in this list are allowed.
        """

        restricted_locations: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )

    class FederatedCatalogOptions(proto.Message):
        r"""Configuration options for a federated catalog.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            unity_catalog_info (google.cloud.biglake_v1.types.IcebergCatalog.FederatedCatalogOptions.UnityCatalogInfo):
                Optional. Info specific to a Unity Catalog by
                Databricks.

                This field is a member of `oneof`_ ``remote_catalog_info``.
            glue_catalog_info (google.cloud.biglake_v1.types.IcebergCatalog.FederatedCatalogOptions.GlueCatalogInfo):
                Optional. Info specific to an AWS Glue
                Catalog.

                This field is a member of `oneof`_ ``remote_catalog_info``.
            snowflake_catalog_info (google.cloud.biglake_v1.types.IcebergCatalog.FederatedCatalogOptions.SnowflakeCatalogInfo):
                Optional. Info specific to a Snowflake
                Catalog.

                This field is a member of `oneof`_ ``remote_catalog_info``.
            secret_name (str):
                Optional. The secret resource name in Secret Manager, in the
                format
                ``projects/{project_id}/locations/{location}/secrets/{secret_id}``
                or
                ``projects/{project_id}/locations/{location}/secrets/{secret_id}/versions/{version_id}``.

                The project ID must match the catalog's project and location
                must match the catalog's location. If the version is not
                specified, the latest version will be used.

                This field is not used when
                [google.cloud.biglake.v1main.IcebergCatalog.FederatedCatalogOptions.UnityCatalogInfo.service_principal_application_id][google.cloud.biglake.v1main.IcebergCatalog.FederatedCatalogOptions.UnityCatalogInfo.service_principal_application_id]
                or
                [google.cloud.biglake.v1main.IcebergCatalog.FederatedCatalogOptions.SnowflakeCatalogInfo.snowflake_role][google.cloud.biglake.v1main.IcebergCatalog.FederatedCatalogOptions.SnowflakeCatalogInfo.snowflake_role]
                is set.

                This field is a member of `oneof`_ ``_secret_name``.
            service_directory_name (str):
                Optional. The service directory resource name for routing
                traffic over a private network connection through
                Cross-Cloud Interconnect, in the format
                ``projects/{project_id}/locations/{location_id}/namespaces/{namespace_id}/services/{service_id}``.

                This field is a member of `oneof`_ ``_service_directory_name``.
            refresh_options (google.cloud.biglake_v1.types.IcebergCatalog.FederatedCatalogOptions.RefreshOptions):
                Optional. Refresh configuration.
            refresh_status (google.cloud.biglake_v1.types.IcebergCatalog.FederatedCatalogOptions.RefreshStatus):
                Output only. The status of the background
                refresh operations.
        """

        class UnityCatalogInfo(proto.Message):
            r"""Unity Catalog info.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                instance_name (str):
                    Required. The instance name is the first part
                    of the URL when logging into the Databricks
                    deployment. For example, for a Databricks on GCP
                    workspace URL https://1.1.gcp.databricks.com,
                    the instance name is 1.1.gcp.databricks.com.

                    This field is a member of `oneof`_ ``_instance_name``.
                catalog_name (str):
                    Required. The catalog name in Unity Catalog.

                    This field is a member of `oneof`_ ``_catalog_name``.
                service_principal_application_id (str):
                    Optional. The application ID of the
                    Databricks service principal that will be used
                    to access the Unity Catalog in the OIDC
                    authentication flow.

                    This field is a member of `oneof`_ ``_service_principal_application_id``.
            """

            instance_name: str = proto.Field(
                proto.STRING,
                number=1,
                optional=True,
            )
            catalog_name: str = proto.Field(
                proto.STRING,
                number=2,
                optional=True,
            )
            service_principal_application_id: str = proto.Field(
                proto.STRING,
                number=3,
                optional=True,
            )

        class GlueCatalogInfo(proto.Message):
            r"""AWS Glue Catalog info. We support regional AWS Glue default
            account catalog and S3 Table Buckets.


            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                warehouse (str):
                    Required. Immutable. The warehouse to connect to a regional
                    AWS Glue Iceberg REST Catalog. For top level access, use the
                    AWS account ID (e.g. 111222333444). For an S3 table bucket,
                    the warehouse is of the form: 111222333444:s3tablescatalog/.
                    The URL to access catalog will be
                    https://glue.{aws_region}.amazonaws.com/iceberg/v1?warehouse={warehouse}.
                    Must be non-empty and is immutable.

                    This field is a member of `oneof`_ ``_warehouse``.
                aws_region (str):
                    Required. Immutable. The AWS region of the
                    Glue catalog to connect to. The region should be
                    in the same geographical region and jurisdiction
                    as the federated catalog.
                    Must be non-empty and is immutable.

                    This field is a member of `oneof`_ ``_aws_region``.
                aws_role_arn (str):
                    Required. The AWS role ARN of the Glue
                    catalog that the federated catalog will assume
                    to access the catalog. Must be non-empty. Can be
                    updated.

                    This field is a member of `oneof`_ ``_aws_role_arn``.
            """

            warehouse: str = proto.Field(
                proto.STRING,
                number=1,
                optional=True,
            )
            aws_region: str = proto.Field(
                proto.STRING,
                number=2,
                optional=True,
            )
            aws_role_arn: str = proto.Field(
                proto.STRING,
                number=3,
                optional=True,
            )

        class SnowflakeCatalogInfo(proto.Message):
            r"""Snowflake Catalog info.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                account_identifier (str):
                    Required. The account identifier in Snowflake (See:
                    https://docs.snowflake.com/en/user-guide/admin-account-identifier).
                    It is the prefix to log into your Snowflake deployment URL.
                    For example:
                    https://<account_identifier>.snowflakecomputing.com.

                    This field is a member of `oneof`_ ``_account_identifier``.
                warehouse (str):
                    Required. The warehouse to connect to in Snowflake REST
                    Catalog.
                    https://<account_identifier>.snowflakecomputing.com/polaris/api/catalog/v1/config?warehouse=<database_name>.

                    This is the Snowflake database name containing the Iceberg
                    metadata to be federated.

                    Must be non-empty.

                    This field is a member of `oneof`_ ``_warehouse``.
                snowflake_role (str):
                    Optional. The specific Snowflake role name to request in the
                    OAuth token scope (via session:role:$ROLE) for the Iceberg
                    REST Catalog session. This role grants the GCP BigLake
                    service account the necessary permissions to interact with
                    the Iceberg catalog, namespaces, and tables.

                    Note: The role provided here must be the DEFAULT_ROLE or be
                    granted to, the Snowflake service user mapped to the BigLake
                    service account.

                    This field is a member of `oneof`_ ``_snowflake_role``.
            """

            account_identifier: str = proto.Field(
                proto.STRING,
                number=1,
                optional=True,
            )
            warehouse: str = proto.Field(
                proto.STRING,
                number=2,
                optional=True,
            )
            snowflake_role: str = proto.Field(
                proto.STRING,
                number=3,
                optional=True,
            )

        class RefreshSchedule(proto.Message):
            r"""Schedule defines if and when metadata refresh should be
            scheduled.


            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                refresh_interval (google.protobuf.duration_pb2.Duration):
                    Optional. The interval for refreshing
                    metadata from the remote catalog. If unset or if
                    the value is <= 0, the background refresh will
                    be disabled. If this field is updated for an
                    existing federated catalog, the previous
                    background refresh must complete before the new
                    refresh interval will take effect.

                    This field is a member of `oneof`_ ``_refresh_interval``.
            """

            refresh_interval: duration_pb2.Duration = proto.Field(
                proto.MESSAGE,
                number=1,
                optional=True,
                message=duration_pb2.Duration,
            )

        class RefreshScope(proto.Message):
            r"""The scope defines a subset of namespaces to be refreshed.

            Attributes:
                namespace_filters (MutableSequence[str]):
                    Optional. Filters to determine which namespaces are included
                    in the refresh process.

                    - empty list means include all namespaces.
                    - "[namespaces]" means include the specified namespaces.
                      ['ns1', 'ns2'] : Discover only namespaces 'ns1' and 'ns2'.
                      The maximum number of namespace filters allowed is 32.
            """

            namespace_filters: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=1,
            )

        class RefreshOptions(proto.Message):
            r"""Refresh configuration.

            Attributes:
                refresh_schedule (google.cloud.biglake_v1.types.IcebergCatalog.FederatedCatalogOptions.RefreshSchedule):
                    Optional. Schedule defines if and when
                    metadata refresh should be scheduled.
                refresh_scope (google.cloud.biglake_v1.types.IcebergCatalog.FederatedCatalogOptions.RefreshScope):
                    Optional. Refresh scope configurations.
            """

            refresh_schedule: "IcebergCatalog.FederatedCatalogOptions.RefreshSchedule" = proto.Field(
                proto.MESSAGE,
                number=1,
                message="IcebergCatalog.FederatedCatalogOptions.RefreshSchedule",
            )
            refresh_scope: "IcebergCatalog.FederatedCatalogOptions.RefreshScope" = (
                proto.Field(
                    proto.MESSAGE,
                    number=2,
                    message="IcebergCatalog.FederatedCatalogOptions.RefreshScope",
                )
            )

        class RefreshStatus(proto.Message):
            r"""Remote catalog background refresh status.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                start_time (google.protobuf.timestamp_pb2.Timestamp):
                    Output only. When the catalog refresh has
                    started, including in-progress refreshes.

                    This field is a member of `oneof`_ ``_start_time``.
                end_time (google.protobuf.timestamp_pb2.Timestamp):
                    Output only. When the catalog refresh has
                    ended, unset for in-progress refreshes.

                    This field is a member of `oneof`_ ``_end_time``.
                status (google.rpc.status_pb2.Status):
                    Output only. The status of the last
                    background refresh operation, unset for
                    in-progress refreshes.

                    This field is a member of `oneof`_ ``_status``.
            """

            start_time: timestamp_pb2.Timestamp = proto.Field(
                proto.MESSAGE,
                number=1,
                optional=True,
                message=timestamp_pb2.Timestamp,
            )
            end_time: timestamp_pb2.Timestamp = proto.Field(
                proto.MESSAGE,
                number=2,
                optional=True,
                message=timestamp_pb2.Timestamp,
            )
            status: status_pb2.Status = proto.Field(
                proto.MESSAGE,
                number=3,
                optional=True,
                message=status_pb2.Status,
            )

        unity_catalog_info: "IcebergCatalog.FederatedCatalogOptions.UnityCatalogInfo" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="remote_catalog_info",
            message="IcebergCatalog.FederatedCatalogOptions.UnityCatalogInfo",
        )
        glue_catalog_info: "IcebergCatalog.FederatedCatalogOptions.GlueCatalogInfo" = (
            proto.Field(
                proto.MESSAGE,
                number=4,
                oneof="remote_catalog_info",
                message="IcebergCatalog.FederatedCatalogOptions.GlueCatalogInfo",
            )
        )
        snowflake_catalog_info: "IcebergCatalog.FederatedCatalogOptions.SnowflakeCatalogInfo" = proto.Field(
            proto.MESSAGE,
            number=7,
            oneof="remote_catalog_info",
            message="IcebergCatalog.FederatedCatalogOptions.SnowflakeCatalogInfo",
        )
        secret_name: str = proto.Field(
            proto.STRING,
            number=1,
            optional=True,
        )
        service_directory_name: str = proto.Field(
            proto.STRING,
            number=5,
            optional=True,
        )
        refresh_options: "IcebergCatalog.FederatedCatalogOptions.RefreshOptions" = (
            proto.Field(
                proto.MESSAGE,
                number=3,
                message="IcebergCatalog.FederatedCatalogOptions.RefreshOptions",
            )
        )
        refresh_status: "IcebergCatalog.FederatedCatalogOptions.RefreshStatus" = (
            proto.Field(
                proto.MESSAGE,
                number=6,
                message="IcebergCatalog.FederatedCatalogOptions.RefreshStatus",
            )
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    credential_mode: CredentialMode = proto.Field(
        proto.ENUM,
        number=2,
        enum=CredentialMode,
    )
    biglake_service_account: str = proto.Field(
        proto.STRING,
        number=3,
    )
    biglake_service_account_unique_id: str = proto.Field(
        proto.STRING,
        number=14,
    )
    catalog_type: CatalogType = proto.Field(
        proto.ENUM,
        number=4,
        enum=CatalogType,
    )
    default_location: str = proto.Field(
        proto.STRING,
        number=5,
    )
    storage_regions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    replicas: MutableSequence[Replica] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=Replica,
    )
    description: str = proto.Field(
        proto.STRING,
        number=12,
    )
    restricted_locations_config: RestrictedLocationsConfig = proto.Field(
        proto.MESSAGE,
        number=15,
        message=RestrictedLocationsConfig,
    )
    federated_catalog_options: FederatedCatalogOptions = proto.Field(
        proto.MESSAGE,
        number=13,
        message=FederatedCatalogOptions,
    )


class CreateIcebergCatalogRequest(proto.Message):
    r"""The request message for the ``CreateIcebergCatalog`` API.

    Attributes:
        parent (str):
            Required. The parent resource where this catalog will be
            created. Format: projects/{project_id}
        iceberg_catalog_id (str):
            Required. The name of the catalog.
        iceberg_catalog (google.cloud.biglake_v1.types.IcebergCatalog):
            Required. The catalog to create. The required fields for
            creation are:

            - catalog_type. Optionally: credential_mode can be provided,
              if Credential Vending is desired.
        primary_location (str):
            Optional. The primary location where the catalog metadata
            will be stored.

            For Google Cloud Storage bucket catalogs and BigLake
            catalogs, if this is not specified, then the region is
            inferred from the bucket's region (``default_location``
            bucket for BigLake catalogs). If specified, the region must
            be in jurisdiction (near the ``default_location`` bucket's
            region and the ``restricted_locations`` buckets' regions for
            BigLake catalogs).

            For federated catalogs, this must be specified and be a
            Lakehouse-supported location
            (https://docs.cloud.google.com/lakehouse/docs/locations). It
            should be close to the remote catalog's location for the
            best performance and cost.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    iceberg_catalog_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    iceberg_catalog: "IcebergCatalog" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="IcebergCatalog",
    )
    primary_location: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateIcebergCatalogRequest(proto.Message):
    r"""The request message for the ``UpdateIcebergCatalog`` API.

    Attributes:
        iceberg_catalog (google.cloud.biglake_v1.types.IcebergCatalog):
            Required. The catalog to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    iceberg_catalog: "IcebergCatalog" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="IcebergCatalog",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetIcebergCatalogRequest(proto.Message):
    r"""The request message for the ``GetIcebergCatalog`` API.

    Attributes:
        name (str):
            Required. The catalog to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListIcebergCatalogsRequest(proto.Message):
    r"""The request message for the ``ListIcebergCatalogs`` API.

    Attributes:
        parent (str):
            Required. The parent resource where this catalog will be
            created. Format: projects/{project_id}
        view (google.cloud.biglake_v1.types.ListIcebergCatalogsRequest.CatalogView):
            Optional. The view of the catalog to return.
        page_size (int):
            Optional. The maximum number of catalogs to
            return. The service may return fewer than this
            value.
        page_token (str):
            Optional. The page token, received from a previous
            ``ListIcebergCatalogs`` call. Provide this to retrieve the
            subsequent page.
        filter (str):
            Optional. The filter expression. The only parameter
            currently supported is filtering based on the
            ``IcebergCatalog.catalog_type`` field.

            Examples:

            - ``catalog_type = CATALOG_TYPE_BIGLAKE``
            - ``catalog_type != CATALOG_TYPE_GCS_BUCKET``
            - ``catalog_type = CATALOG_TYPE_BIGLAKE OR catalog_type = CATALOG_TYPE_GCS_BUCKET``
            - ``NOT catalog_type = CATALOG_TYPE_GCS_BUCKET``
    """

    class CatalogView(proto.Enum):
        r"""The enumeration of the views that can be returned.

        Values:
            CATALOG_VIEW_UNSPECIFIED (0):
                Default/unset value. Same as BASIC.
            CATALOG_VIEW_BASIC (1):
                Include only the name and catalog type.
            CATALOG_VIEW_FULL (2):
                Include all fields of the catalog.
        """

        CATALOG_VIEW_UNSPECIFIED = 0
        CATALOG_VIEW_BASIC = 1
        CATALOG_VIEW_FULL = 2

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: CatalogView = proto.Field(
        proto.ENUM,
        number=2,
        enum=CatalogView,
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
        number=6,
    )


class ListIcebergCatalogsResponse(proto.Message):
    r"""The response message for the ``ListIcebergCatalogs`` API.

    Attributes:
        iceberg_catalogs (MutableSequence[google.cloud.biglake_v1.types.IcebergCatalog]):
            Output only. The list of iceberg catalogs.
        next_page_token (str):
            Output only. The next page token for
            pagination.
        unreachable (MutableSequence[str]):
            Output only. The list of unreachable cloud
            regions. If non-empty, the result set might be
            incomplete.
    """

    @property
    def raw_page(self):
        return self

    iceberg_catalogs: MutableSequence["IcebergCatalog"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="IcebergCatalog",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class FailoverIcebergCatalogRequest(proto.Message):
    r"""Request message for FailoverIcebergCatalog.

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


class FailoverIcebergCatalogResponse(proto.Message):
    r"""Response message for FailoverIcebergCatalog.

    Attributes:
        replication_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The min timestamp for which all namespaces and
            table metadata have been replicated in the region specified
            as the new primary_replica. Some resources may have been
            replicated more recently than this timestamp. If empty, the
            replica has just been created and has not yet been fully
            initialized. NOTE: When the Cloud Storage replication
            watermark is available, this will represent both catalog
            metadata and Cloud Storage data.
    """

    replication_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )


class TableIdentifier(proto.Message):
    r"""The table identifier.

    Attributes:
        namespace (MutableSequence[str]):
            The namespace of the table. This is always 1
            element, since we don't support nested
            namespaces.
        name (str):
            The table name.
    """

    namespace: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class IcebergNamespaceUpdate(proto.Message):
    r"""The request message for the ``UpdateIcebergNamespace`` API.

    Attributes:
        removals (MutableSequence[str]):
            Optional. Keys of the properties to remove.
        updates (MutableMapping[str, str]):
            Optional. List of properties to update or
            add.
    """

    removals: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    updates: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )


class StorageCredential(proto.Message):
    r"""The storage credential for a path in the table.

    Attributes:
        prefix (str):
            Indicates a storage location prefix where the
            credential is relevant.
        config (MutableMapping[str, str]):
            The credentials for the storage location. The keys that are
            populated are:

            - ``gcs.oauth2.token``
            - ``gcs.oauth2.token_expires_at``
            - ``expiration-time`` (to support federation from Polaris).
    """

    prefix: str = proto.Field(
        proto.STRING,
        number=1,
    )
    config: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
