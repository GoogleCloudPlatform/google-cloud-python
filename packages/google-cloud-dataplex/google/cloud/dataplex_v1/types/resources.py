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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.dataplex.v1",
    manifest={
        "State",
        "Lake",
        "AssetStatus",
        "Zone",
        "Action",
        "Asset",
    },
)


class State(proto.Enum):
    r"""State of a resource.

    Values:
        STATE_UNSPECIFIED (0):
            State is not specified.
        ACTIVE (1):
            Resource is active, i.e., ready to use.
        CREATING (2):
            Resource is under creation.
        DELETING (3):
            Resource is under deletion.
        ACTION_REQUIRED (4):
            Resource is active but has unresolved
            actions.
    """

    STATE_UNSPECIFIED = 0
    ACTIVE = 1
    CREATING = 2
    DELETING = 3
    ACTION_REQUIRED = 4


class Lake(proto.Message):
    r"""A lake is a centralized repository for managing enterprise
    data across the organization distributed across many cloud
    projects, and stored in a variety of storage services such as
    Google Cloud Storage and BigQuery. The resources attached to a
    lake are referred to as managed resources. Data within these
    managed resources can be structured or unstructured. A lake
    provides data admins with tools to organize, secure and manage
    their data at scale, and provides data scientists and data
    engineers an integrated experience to easily search, discover,
    analyze and transform data and associated metadata.

    Attributes:
        name (str):
            Output only. The relative resource name of the lake, of the
            form:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}``.
        display_name (str):
            Optional. User friendly display name.
        uid (str):
            Output only. System generated globally unique
            ID for the lake. This ID will be different if
            the lake is deleted and re-created with the same
            name.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the lake was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the lake was last
            updated.
        labels (MutableMapping[str, str]):
            Optional. User-defined labels for the lake.
        description (str):
            Optional. Description of the lake.
        state (google.cloud.dataplex_v1.types.State):
            Output only. Current state of the lake.
        service_account (str):
            Output only. Service account associated with
            this lake. This service account must be
            authorized to access or operate on resources
            managed by the lake.
        metastore (google.cloud.dataplex_v1.types.Lake.Metastore):
            Optional. Settings to manage lake and
            Dataproc Metastore service instance association.
        asset_status (google.cloud.dataplex_v1.types.AssetStatus):
            Output only. Aggregated status of the
            underlying assets of the lake.
        metastore_status (google.cloud.dataplex_v1.types.Lake.MetastoreStatus):
            Output only. Metastore status of the lake.
    """

    class Metastore(proto.Message):
        r"""Settings to manage association of Dataproc Metastore with a
        lake.

        Attributes:
            service (str):
                Optional. A relative reference to the Dataproc Metastore
                (https://cloud.google.com/dataproc-metastore/docs) service
                associated with the lake:
                ``projects/{project_id}/locations/{location_id}/services/{service_id}``
        """

        service: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class MetastoreStatus(proto.Message):
        r"""Status of Lake and Dataproc Metastore service instance
        association.

        Attributes:
            state (google.cloud.dataplex_v1.types.Lake.MetastoreStatus.State):
                Current state of association.
            message (str):
                Additional information about the current
                status.
            update_time (google.protobuf.timestamp_pb2.Timestamp):
                Last update time of the metastore status of
                the lake.
            endpoint (str):
                The URI of the endpoint used to access the
                Metastore service.
        """

        class State(proto.Enum):
            r"""Current state of association.

            Values:
                STATE_UNSPECIFIED (0):
                    Unspecified.
                NONE (1):
                    A Metastore service instance is not
                    associated with the lake.
                READY (2):
                    A Metastore service instance is attached to
                    the lake.
                UPDATING (3):
                    Attach/detach is in progress.
                ERROR (4):
                    Attach/detach could not be done due to
                    errors.
            """

            STATE_UNSPECIFIED = 0
            NONE = 1
            READY = 2
            UPDATING = 3
            ERROR = 4

        state: "Lake.MetastoreStatus.State" = proto.Field(
            proto.ENUM,
            number=1,
            enum="Lake.MetastoreStatus.State",
        )
        message: str = proto.Field(
            proto.STRING,
            number=2,
        )
        update_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=3,
            message=timestamp_pb2.Timestamp,
        )
        endpoint: str = proto.Field(
            proto.STRING,
            number=4,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    description: str = proto.Field(
        proto.STRING,
        number=7,
    )
    state: "State" = proto.Field(
        proto.ENUM,
        number=8,
        enum="State",
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=9,
    )
    metastore: Metastore = proto.Field(
        proto.MESSAGE,
        number=102,
        message=Metastore,
    )
    asset_status: "AssetStatus" = proto.Field(
        proto.MESSAGE,
        number=103,
        message="AssetStatus",
    )
    metastore_status: MetastoreStatus = proto.Field(
        proto.MESSAGE,
        number=104,
        message=MetastoreStatus,
    )


class AssetStatus(proto.Message):
    r"""Aggregated status of the underlying assets of a lake or zone.

    Attributes:
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Last update time of the status.
        active_assets (int):
            Number of active assets.
        security_policy_applying_assets (int):
            Number of assets that are in process of
            updating the security policy on attached
            resources.
    """

    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    active_assets: int = proto.Field(
        proto.INT32,
        number=2,
    )
    security_policy_applying_assets: int = proto.Field(
        proto.INT32,
        number=3,
    )


class Zone(proto.Message):
    r"""A zone represents a logical group of related assets within a
    lake. A zone can be used to map to organizational structure or
    represent stages of data readiness from raw to curated. It
    provides managing behavior that is shared or inherited by all
    contained assets.

    Attributes:
        name (str):
            Output only. The relative resource name of the zone, of the
            form:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}``.
        display_name (str):
            Optional. User friendly display name.
        uid (str):
            Output only. System generated globally unique
            ID for the zone. This ID will be different if
            the zone is deleted and re-created with the same
            name.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the zone was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the zone was last
            updated.
        labels (MutableMapping[str, str]):
            Optional. User defined labels for the zone.
        description (str):
            Optional. Description of the zone.
        state (google.cloud.dataplex_v1.types.State):
            Output only. Current state of the zone.
        type_ (google.cloud.dataplex_v1.types.Zone.Type):
            Required. Immutable. The type of the zone.
        discovery_spec (google.cloud.dataplex_v1.types.Zone.DiscoverySpec):
            Optional. Specification of the discovery
            feature applied to data in this zone.
        resource_spec (google.cloud.dataplex_v1.types.Zone.ResourceSpec):
            Required. Specification of the resources that
            are referenced by the assets within this zone.
        asset_status (google.cloud.dataplex_v1.types.AssetStatus):
            Output only. Aggregated status of the
            underlying assets of the zone.
    """

    class Type(proto.Enum):
        r"""Type of zone.

        Values:
            TYPE_UNSPECIFIED (0):
                Zone type not specified.
            RAW (1):
                A zone that contains data that needs further
                processing before it is considered generally
                ready for consumption and analytics workloads.
            CURATED (2):
                A zone that contains data that is considered
                to be ready for broader consumption and
                analytics workloads. Curated structured data
                stored in Cloud Storage must conform to certain
                file formats (parquet, avro and orc) and
                organized in a hive-compatible directory layout.
        """

        TYPE_UNSPECIFIED = 0
        RAW = 1
        CURATED = 2

    class ResourceSpec(proto.Message):
        r"""Settings for resources attached as assets within a zone.

        Attributes:
            location_type (google.cloud.dataplex_v1.types.Zone.ResourceSpec.LocationType):
                Required. Immutable. The location type of the
                resources that are allowed to be attached to the
                assets within this zone.
        """

        class LocationType(proto.Enum):
            r"""Location type of the resources attached to a zone.

            Values:
                LOCATION_TYPE_UNSPECIFIED (0):
                    Unspecified location type.
                SINGLE_REGION (1):
                    Resources that are associated with a single
                    region.
                MULTI_REGION (2):
                    Resources that are associated with a
                    multi-region location.
            """

            LOCATION_TYPE_UNSPECIFIED = 0
            SINGLE_REGION = 1
            MULTI_REGION = 2

        location_type: "Zone.ResourceSpec.LocationType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="Zone.ResourceSpec.LocationType",
        )

    class DiscoverySpec(proto.Message):
        r"""Settings to manage the metadata discovery and publishing in a
        zone.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            enabled (bool):
                Required. Whether discovery is enabled.
            include_patterns (MutableSequence[str]):
                Optional. The list of patterns to apply for
                selecting data to include during discovery if
                only a subset of the data should considered. For
                Cloud Storage bucket assets, these are
                interpreted as glob patterns used to match
                object names. For BigQuery dataset assets, these
                are interpreted as patterns to match table
                names.
            exclude_patterns (MutableSequence[str]):
                Optional. The list of patterns to apply for
                selecting data to exclude during discovery.  For
                Cloud Storage bucket assets, these are
                interpreted as glob patterns used to match
                object names. For BigQuery dataset assets, these
                are interpreted as patterns to match table
                names.
            csv_options (google.cloud.dataplex_v1.types.Zone.DiscoverySpec.CsvOptions):
                Optional. Configuration for CSV data.
            json_options (google.cloud.dataplex_v1.types.Zone.DiscoverySpec.JsonOptions):
                Optional. Configuration for Json data.
            schedule (str):
                Optional. Cron schedule (https://en.wikipedia.org/wiki/Cron)
                for running discovery periodically. Successive discovery
                runs must be scheduled at least 60 minutes apart. The
                default value is to run discovery every 60 minutes.

                To explicitly set a timezone to the cron tab, apply a prefix
                in the cron tab: "CRON_TZ=${IANA_TIME_ZONE}" or
                TZ=${IANA_TIME_ZONE}". The ${IANA_TIME_ZONE} may only be a
                valid string from IANA time zone database. For example,
                ``CRON_TZ=America/New_York 1 * * * *``, or
                ``TZ=America/New_York 1 * * * *``.

                This field is a member of `oneof`_ ``trigger``.
        """

        class CsvOptions(proto.Message):
            r"""Describe CSV and similar semi-structured data formats.

            Attributes:
                header_rows (int):
                    Optional. The number of rows to interpret as
                    header rows that should be skipped when reading
                    data rows.
                delimiter (str):
                    Optional. The delimiter being used to
                    separate values. This defaults to ','.
                encoding (str):
                    Optional. The character encoding of the data.
                    The default is UTF-8.
                disable_type_inference (bool):
                    Optional. Whether to disable the inference of
                    data type for CSV data. If true, all columns
                    will be registered as strings.
            """

            header_rows: int = proto.Field(
                proto.INT32,
                number=1,
            )
            delimiter: str = proto.Field(
                proto.STRING,
                number=2,
            )
            encoding: str = proto.Field(
                proto.STRING,
                number=3,
            )
            disable_type_inference: bool = proto.Field(
                proto.BOOL,
                number=4,
            )

        class JsonOptions(proto.Message):
            r"""Describe JSON data format.

            Attributes:
                encoding (str):
                    Optional. The character encoding of the data.
                    The default is UTF-8.
                disable_type_inference (bool):
                    Optional. Whether to disable the inference of
                    data type for Json data. If true, all columns
                    will be registered as their primitive types
                    (strings, number or boolean).
            """

            encoding: str = proto.Field(
                proto.STRING,
                number=1,
            )
            disable_type_inference: bool = proto.Field(
                proto.BOOL,
                number=2,
            )

        enabled: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        include_patterns: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        exclude_patterns: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )
        csv_options: "Zone.DiscoverySpec.CsvOptions" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="Zone.DiscoverySpec.CsvOptions",
        )
        json_options: "Zone.DiscoverySpec.JsonOptions" = proto.Field(
            proto.MESSAGE,
            number=5,
            message="Zone.DiscoverySpec.JsonOptions",
        )
        schedule: str = proto.Field(
            proto.STRING,
            number=10,
            oneof="trigger",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    description: str = proto.Field(
        proto.STRING,
        number=7,
    )
    state: "State" = proto.Field(
        proto.ENUM,
        number=8,
        enum="State",
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=9,
        enum=Type,
    )
    discovery_spec: DiscoverySpec = proto.Field(
        proto.MESSAGE,
        number=103,
        message=DiscoverySpec,
    )
    resource_spec: ResourceSpec = proto.Field(
        proto.MESSAGE,
        number=104,
        message=ResourceSpec,
    )
    asset_status: "AssetStatus" = proto.Field(
        proto.MESSAGE,
        number=105,
        message="AssetStatus",
    )


class Action(proto.Message):
    r"""Action represents an issue requiring administrator action for
    resolution.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        category (google.cloud.dataplex_v1.types.Action.Category):
            The category of issue associated with the
            action.
        issue (str):
            Detailed description of the issue requiring
            action.
        detect_time (google.protobuf.timestamp_pb2.Timestamp):
            The time that the issue was detected.
        name (str):
            Output only. The relative resource name of the action, of
            the form:
            ``projects/{project}/locations/{location}/lakes/{lake}/actions/{action}``
            ``projects/{project}/locations/{location}/lakes/{lake}/zones/{zone}/actions/{action}``
            ``projects/{project}/locations/{location}/lakes/{lake}/zones/{zone}/assets/{asset}/actions/{action}``.
        lake (str):
            Output only. The relative resource name of the lake, of the
            form:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}``.
        zone (str):
            Output only. The relative resource name of the zone, of the
            form:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}``.
        asset (str):
            Output only. The relative resource name of the asset, of the
            form:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/assets/{asset_id}``.
        data_locations (MutableSequence[str]):
            The list of data locations associated with this action.
            Cloud Storage locations are represented as URI paths(E.g.
            ``gs://bucket/table1/year=2020/month=Jan/``). BigQuery
            locations refer to resource names(E.g.
            ``bigquery.googleapis.com/projects/project-id/datasets/dataset-id``).
        invalid_data_format (google.cloud.dataplex_v1.types.Action.InvalidDataFormat):
            Details for issues related to invalid or
            unsupported data formats.

            This field is a member of `oneof`_ ``details``.
        incompatible_data_schema (google.cloud.dataplex_v1.types.Action.IncompatibleDataSchema):
            Details for issues related to incompatible
            schemas detected within data.

            This field is a member of `oneof`_ ``details``.
        invalid_data_partition (google.cloud.dataplex_v1.types.Action.InvalidDataPartition):
            Details for issues related to invalid or
            unsupported data partition structure.

            This field is a member of `oneof`_ ``details``.
        missing_data (google.cloud.dataplex_v1.types.Action.MissingData):
            Details for issues related to absence of data
            within managed resources.

            This field is a member of `oneof`_ ``details``.
        missing_resource (google.cloud.dataplex_v1.types.Action.MissingResource):
            Details for issues related to absence of a
            managed resource.

            This field is a member of `oneof`_ ``details``.
        unauthorized_resource (google.cloud.dataplex_v1.types.Action.UnauthorizedResource):
            Details for issues related to lack of
            permissions to access data resources.

            This field is a member of `oneof`_ ``details``.
        failed_security_policy_apply (google.cloud.dataplex_v1.types.Action.FailedSecurityPolicyApply):
            Details for issues related to applying
            security policy.

            This field is a member of `oneof`_ ``details``.
        invalid_data_organization (google.cloud.dataplex_v1.types.Action.InvalidDataOrganization):
            Details for issues related to invalid data
            arrangement.

            This field is a member of `oneof`_ ``details``.
    """

    class Category(proto.Enum):
        r"""The category of issues.

        Values:
            CATEGORY_UNSPECIFIED (0):
                Unspecified category.
            RESOURCE_MANAGEMENT (1):
                Resource management related issues.
            SECURITY_POLICY (2):
                Security policy related issues.
            DATA_DISCOVERY (3):
                Data and discovery related issues.
        """

        CATEGORY_UNSPECIFIED = 0
        RESOURCE_MANAGEMENT = 1
        SECURITY_POLICY = 2
        DATA_DISCOVERY = 3

    class MissingResource(proto.Message):
        r"""Action details for resource references in assets that cannot
        be located.

        """

    class UnauthorizedResource(proto.Message):
        r"""Action details for unauthorized resource issues raised to
        indicate that the service account associated with the lake
        instance is not authorized to access or manage the resource
        associated with an asset.

        """

    class FailedSecurityPolicyApply(proto.Message):
        r"""Failed to apply security policy to the managed resource(s)
        under a lake, zone or an asset. For a lake or zone resource, one
        or more underlying assets has a failure applying security policy
        to the associated managed resource.

        Attributes:
            asset (str):
                Resource name of one of the assets with
                failing security policy application. Populated
                for a lake or zone resource only.
        """

        asset: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class InvalidDataFormat(proto.Message):
        r"""Action details for invalid or unsupported data files detected
        by discovery.

        Attributes:
            sampled_data_locations (MutableSequence[str]):
                The list of data locations sampled and used
                for format/schema inference.
            expected_format (str):
                The expected data format of the entity.
            new_format (str):
                The new unexpected data format within the
                entity.
        """

        sampled_data_locations: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        expected_format: str = proto.Field(
            proto.STRING,
            number=2,
        )
        new_format: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class IncompatibleDataSchema(proto.Message):
        r"""Action details for incompatible schemas detected by
        discovery.

        Attributes:
            table (str):
                The name of the table containing invalid
                data.
            existing_schema (str):
                The existing and expected schema of the
                table. The schema is provided as a JSON
                formatted structure listing columns and data
                types.
            new_schema (str):
                The new and incompatible schema within the
                table. The schema is provided as a JSON
                formatted structured listing columns and data
                types.
            sampled_data_locations (MutableSequence[str]):
                The list of data locations sampled and used
                for format/schema inference.
            schema_change (google.cloud.dataplex_v1.types.Action.IncompatibleDataSchema.SchemaChange):
                Whether the action relates to a schema that
                is incompatible or modified.
        """

        class SchemaChange(proto.Enum):
            r"""Whether the action relates to a schema that is incompatible
            or modified.

            Values:
                SCHEMA_CHANGE_UNSPECIFIED (0):
                    Schema change unspecified.
                INCOMPATIBLE (1):
                    Newly discovered schema is incompatible with
                    existing schema.
                MODIFIED (2):
                    Newly discovered schema has changed from
                    existing schema for data in a curated zone.
            """

            SCHEMA_CHANGE_UNSPECIFIED = 0
            INCOMPATIBLE = 1
            MODIFIED = 2

        table: str = proto.Field(
            proto.STRING,
            number=1,
        )
        existing_schema: str = proto.Field(
            proto.STRING,
            number=2,
        )
        new_schema: str = proto.Field(
            proto.STRING,
            number=3,
        )
        sampled_data_locations: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=4,
        )
        schema_change: "Action.IncompatibleDataSchema.SchemaChange" = proto.Field(
            proto.ENUM,
            number=5,
            enum="Action.IncompatibleDataSchema.SchemaChange",
        )

    class InvalidDataPartition(proto.Message):
        r"""Action details for invalid or unsupported partitions detected
        by discovery.

        Attributes:
            expected_structure (google.cloud.dataplex_v1.types.Action.InvalidDataPartition.PartitionStructure):
                The issue type of InvalidDataPartition.
        """

        class PartitionStructure(proto.Enum):
            r"""The expected partition structure.

            Values:
                PARTITION_STRUCTURE_UNSPECIFIED (0):
                    PartitionStructure unspecified.
                CONSISTENT_KEYS (1):
                    Consistent hive-style partition definition
                    (both raw and curated zone).
                HIVE_STYLE_KEYS (2):
                    Hive style partition definition (curated zone
                    only).
            """

            PARTITION_STRUCTURE_UNSPECIFIED = 0
            CONSISTENT_KEYS = 1
            HIVE_STYLE_KEYS = 2

        expected_structure: "Action.InvalidDataPartition.PartitionStructure" = (
            proto.Field(
                proto.ENUM,
                number=1,
                enum="Action.InvalidDataPartition.PartitionStructure",
            )
        )

    class MissingData(proto.Message):
        r"""Action details for absence of data detected by discovery."""

    class InvalidDataOrganization(proto.Message):
        r"""Action details for invalid data arrangement."""

    category: Category = proto.Field(
        proto.ENUM,
        number=1,
        enum=Category,
    )
    issue: str = proto.Field(
        proto.STRING,
        number=2,
    )
    detect_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    lake: str = proto.Field(
        proto.STRING,
        number=6,
    )
    zone: str = proto.Field(
        proto.STRING,
        number=7,
    )
    asset: str = proto.Field(
        proto.STRING,
        number=8,
    )
    data_locations: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=9,
    )
    invalid_data_format: InvalidDataFormat = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="details",
        message=InvalidDataFormat,
    )
    incompatible_data_schema: IncompatibleDataSchema = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="details",
        message=IncompatibleDataSchema,
    )
    invalid_data_partition: InvalidDataPartition = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="details",
        message=InvalidDataPartition,
    )
    missing_data: MissingData = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="details",
        message=MissingData,
    )
    missing_resource: MissingResource = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="details",
        message=MissingResource,
    )
    unauthorized_resource: UnauthorizedResource = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof="details",
        message=UnauthorizedResource,
    )
    failed_security_policy_apply: FailedSecurityPolicyApply = proto.Field(
        proto.MESSAGE,
        number=21,
        oneof="details",
        message=FailedSecurityPolicyApply,
    )
    invalid_data_organization: InvalidDataOrganization = proto.Field(
        proto.MESSAGE,
        number=22,
        oneof="details",
        message=InvalidDataOrganization,
    )


class Asset(proto.Message):
    r"""An asset represents a cloud resource that is being managed
    within a lake as a member of a zone.

    Attributes:
        name (str):
            Output only. The relative resource name of the asset, of the
            form:
            ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/assets/{asset_id}``.
        display_name (str):
            Optional. User friendly display name.
        uid (str):
            Output only. System generated globally unique
            ID for the asset. This ID will be different if
            the asset is deleted and re-created with the
            same name.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the asset was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the asset was last
            updated.
        labels (MutableMapping[str, str]):
            Optional. User defined labels for the asset.
        description (str):
            Optional. Description of the asset.
        state (google.cloud.dataplex_v1.types.State):
            Output only. Current state of the asset.
        resource_spec (google.cloud.dataplex_v1.types.Asset.ResourceSpec):
            Required. Specification of the resource that
            is referenced by this asset.
        resource_status (google.cloud.dataplex_v1.types.Asset.ResourceStatus):
            Output only. Status of the resource
            referenced by this asset.
        security_status (google.cloud.dataplex_v1.types.Asset.SecurityStatus):
            Output only. Status of the security policy
            applied to resource referenced by this asset.
        discovery_spec (google.cloud.dataplex_v1.types.Asset.DiscoverySpec):
            Optional. Specification of the discovery
            feature applied to data referenced by this
            asset. When this spec is left unset, the asset
            will use the spec set on the parent zone.
        discovery_status (google.cloud.dataplex_v1.types.Asset.DiscoveryStatus):
            Output only. Status of the discovery feature
            applied to data referenced by this asset.
    """

    class SecurityStatus(proto.Message):
        r"""Security policy status of the asset. Data security policy,
        i.e., readers, writers & owners, should be specified in the
        lake/zone/asset IAM policy.

        Attributes:
            state (google.cloud.dataplex_v1.types.Asset.SecurityStatus.State):
                The current state of the security policy
                applied to the attached resource.
            message (str):
                Additional information about the current
                state.
            update_time (google.protobuf.timestamp_pb2.Timestamp):
                Last update time of the status.
        """

        class State(proto.Enum):
            r"""The state of the security policy.

            Values:
                STATE_UNSPECIFIED (0):
                    State unspecified.
                READY (1):
                    Security policy has been successfully applied
                    to the attached resource.
                APPLYING (2):
                    Security policy is in the process of being
                    applied to the attached resource.
                ERROR (3):
                    Security policy could not be applied to the
                    attached resource due to errors.
            """

            STATE_UNSPECIFIED = 0
            READY = 1
            APPLYING = 2
            ERROR = 3

        state: "Asset.SecurityStatus.State" = proto.Field(
            proto.ENUM,
            number=1,
            enum="Asset.SecurityStatus.State",
        )
        message: str = proto.Field(
            proto.STRING,
            number=2,
        )
        update_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=3,
            message=timestamp_pb2.Timestamp,
        )

    class DiscoverySpec(proto.Message):
        r"""Settings to manage the metadata discovery and publishing for
        an asset.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            enabled (bool):
                Optional. Whether discovery is enabled.
            include_patterns (MutableSequence[str]):
                Optional. The list of patterns to apply for
                selecting data to include during discovery if
                only a subset of the data should considered.
                For Cloud Storage bucket assets, these are
                interpreted as glob patterns used to match
                object names. For BigQuery dataset assets, these
                are interpreted as patterns to match table
                names.
            exclude_patterns (MutableSequence[str]):
                Optional. The list of patterns to apply for
                selecting data to exclude during discovery.  For
                Cloud Storage bucket assets, these are
                interpreted as glob patterns used to match
                object names. For BigQuery dataset assets, these
                are interpreted as patterns to match table
                names.
            csv_options (google.cloud.dataplex_v1.types.Asset.DiscoverySpec.CsvOptions):
                Optional. Configuration for CSV data.
            json_options (google.cloud.dataplex_v1.types.Asset.DiscoverySpec.JsonOptions):
                Optional. Configuration for Json data.
            schedule (str):
                Optional. Cron schedule (https://en.wikipedia.org/wiki/Cron)
                for running discovery periodically. Successive discovery
                runs must be scheduled at least 60 minutes apart. The
                default value is to run discovery every 60 minutes.

                To explicitly set a timezone to the cron tab, apply a prefix
                in the cron tab: "CRON_TZ=${IANA_TIME_ZONE}" or
                TZ=${IANA_TIME_ZONE}". The ${IANA_TIME_ZONE} may only be a
                valid string from IANA time zone database. For example,
                ``CRON_TZ=America/New_York 1 * * * *``, or
                ``TZ=America/New_York 1 * * * *``.

                This field is a member of `oneof`_ ``trigger``.
        """

        class CsvOptions(proto.Message):
            r"""Describe CSV and similar semi-structured data formats.

            Attributes:
                header_rows (int):
                    Optional. The number of rows to interpret as
                    header rows that should be skipped when reading
                    data rows.
                delimiter (str):
                    Optional. The delimiter being used to
                    separate values. This defaults to ','.
                encoding (str):
                    Optional. The character encoding of the data.
                    The default is UTF-8.
                disable_type_inference (bool):
                    Optional. Whether to disable the inference of
                    data type for CSV data. If true, all columns
                    will be registered as strings.
            """

            header_rows: int = proto.Field(
                proto.INT32,
                number=1,
            )
            delimiter: str = proto.Field(
                proto.STRING,
                number=2,
            )
            encoding: str = proto.Field(
                proto.STRING,
                number=3,
            )
            disable_type_inference: bool = proto.Field(
                proto.BOOL,
                number=4,
            )

        class JsonOptions(proto.Message):
            r"""Describe JSON data format.

            Attributes:
                encoding (str):
                    Optional. The character encoding of the data.
                    The default is UTF-8.
                disable_type_inference (bool):
                    Optional. Whether to disable the inference of
                    data type for Json data. If true, all columns
                    will be registered as their primitive types
                    (strings, number or boolean).
            """

            encoding: str = proto.Field(
                proto.STRING,
                number=1,
            )
            disable_type_inference: bool = proto.Field(
                proto.BOOL,
                number=2,
            )

        enabled: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        include_patterns: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        exclude_patterns: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )
        csv_options: "Asset.DiscoverySpec.CsvOptions" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="Asset.DiscoverySpec.CsvOptions",
        )
        json_options: "Asset.DiscoverySpec.JsonOptions" = proto.Field(
            proto.MESSAGE,
            number=5,
            message="Asset.DiscoverySpec.JsonOptions",
        )
        schedule: str = proto.Field(
            proto.STRING,
            number=10,
            oneof="trigger",
        )

    class ResourceSpec(proto.Message):
        r"""Identifies the cloud resource that is referenced by this
        asset.

        Attributes:
            name (str):
                Immutable. Relative name of the cloud resource that contains
                the data that is being managed within a lake. For example:
                ``projects/{project_number}/buckets/{bucket_id}``
                ``projects/{project_number}/datasets/{dataset_id}``
            type_ (google.cloud.dataplex_v1.types.Asset.ResourceSpec.Type):
                Required. Immutable. Type of resource.
            read_access_mode (google.cloud.dataplex_v1.types.Asset.ResourceSpec.AccessMode):
                Optional. Determines how read permissions are
                handled for each asset and their associated
                tables. Only available to storage buckets
                assets.
        """

        class Type(proto.Enum):
            r"""Type of resource.

            Values:
                TYPE_UNSPECIFIED (0):
                    Type not specified.
                STORAGE_BUCKET (1):
                    Cloud Storage bucket.
                BIGQUERY_DATASET (2):
                    BigQuery dataset.
            """

            TYPE_UNSPECIFIED = 0
            STORAGE_BUCKET = 1
            BIGQUERY_DATASET = 2

        class AccessMode(proto.Enum):
            r"""Access Mode determines how data stored within the resource is
            read. This is only applicable to storage bucket assets.

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

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        type_: "Asset.ResourceSpec.Type" = proto.Field(
            proto.ENUM,
            number=2,
            enum="Asset.ResourceSpec.Type",
        )
        read_access_mode: "Asset.ResourceSpec.AccessMode" = proto.Field(
            proto.ENUM,
            number=5,
            enum="Asset.ResourceSpec.AccessMode",
        )

    class ResourceStatus(proto.Message):
        r"""Status of the resource referenced by an asset.

        Attributes:
            state (google.cloud.dataplex_v1.types.Asset.ResourceStatus.State):
                The current state of the managed resource.
            message (str):
                Additional information about the current
                state.
            update_time (google.protobuf.timestamp_pb2.Timestamp):
                Last update time of the status.
            managed_access_identity (str):
                Output only. Service account associated with
                the BigQuery Connection.
        """

        class State(proto.Enum):
            r"""The state of a resource.

            Values:
                STATE_UNSPECIFIED (0):
                    State unspecified.
                READY (1):
                    Resource does not have any errors.
                ERROR (2):
                    Resource has errors.
            """

            STATE_UNSPECIFIED = 0
            READY = 1
            ERROR = 2

        state: "Asset.ResourceStatus.State" = proto.Field(
            proto.ENUM,
            number=1,
            enum="Asset.ResourceStatus.State",
        )
        message: str = proto.Field(
            proto.STRING,
            number=2,
        )
        update_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=3,
            message=timestamp_pb2.Timestamp,
        )
        managed_access_identity: str = proto.Field(
            proto.STRING,
            number=4,
        )

    class DiscoveryStatus(proto.Message):
        r"""Status of discovery for an asset.

        Attributes:
            state (google.cloud.dataplex_v1.types.Asset.DiscoveryStatus.State):
                The current status of the discovery feature.
            message (str):
                Additional information about the current
                state.
            update_time (google.protobuf.timestamp_pb2.Timestamp):
                Last update time of the status.
            last_run_time (google.protobuf.timestamp_pb2.Timestamp):
                The start time of the last discovery run.
            stats (google.cloud.dataplex_v1.types.Asset.DiscoveryStatus.Stats):
                Data Stats of the asset reported by
                discovery.
            last_run_duration (google.protobuf.duration_pb2.Duration):
                The duration of the last discovery run.
        """

        class State(proto.Enum):
            r"""Current state of discovery.

            Values:
                STATE_UNSPECIFIED (0):
                    State is unspecified.
                SCHEDULED (1):
                    Discovery for the asset is scheduled.
                IN_PROGRESS (2):
                    Discovery for the asset is running.
                PAUSED (3):
                    Discovery for the asset is currently paused
                    (e.g. due to a lack of available resources). It
                    will be automatically resumed.
                DISABLED (5):
                    Discovery for the asset is disabled.
            """

            STATE_UNSPECIFIED = 0
            SCHEDULED = 1
            IN_PROGRESS = 2
            PAUSED = 3
            DISABLED = 5

        class Stats(proto.Message):
            r"""The aggregated data statistics for the asset reported by
            discovery.

            Attributes:
                data_items (int):
                    The count of data items within the referenced
                    resource.
                data_size (int):
                    The number of stored data bytes within the
                    referenced resource.
                tables (int):
                    The count of table entities within the
                    referenced resource.
                filesets (int):
                    The count of fileset entities within the
                    referenced resource.
            """

            data_items: int = proto.Field(
                proto.INT64,
                number=1,
            )
            data_size: int = proto.Field(
                proto.INT64,
                number=2,
            )
            tables: int = proto.Field(
                proto.INT64,
                number=3,
            )
            filesets: int = proto.Field(
                proto.INT64,
                number=4,
            )

        state: "Asset.DiscoveryStatus.State" = proto.Field(
            proto.ENUM,
            number=1,
            enum="Asset.DiscoveryStatus.State",
        )
        message: str = proto.Field(
            proto.STRING,
            number=2,
        )
        update_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=3,
            message=timestamp_pb2.Timestamp,
        )
        last_run_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=4,
            message=timestamp_pb2.Timestamp,
        )
        stats: "Asset.DiscoveryStatus.Stats" = proto.Field(
            proto.MESSAGE,
            number=6,
            message="Asset.DiscoveryStatus.Stats",
        )
        last_run_duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=7,
            message=duration_pb2.Duration,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=3,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    description: str = proto.Field(
        proto.STRING,
        number=7,
    )
    state: "State" = proto.Field(
        proto.ENUM,
        number=8,
        enum="State",
    )
    resource_spec: ResourceSpec = proto.Field(
        proto.MESSAGE,
        number=100,
        message=ResourceSpec,
    )
    resource_status: ResourceStatus = proto.Field(
        proto.MESSAGE,
        number=101,
        message=ResourceStatus,
    )
    security_status: SecurityStatus = proto.Field(
        proto.MESSAGE,
        number=103,
        message=SecurityStatus,
    )
    discovery_spec: DiscoverySpec = proto.Field(
        proto.MESSAGE,
        number=106,
        message=DiscoverySpec,
    )
    discovery_status: DiscoveryStatus = proto.Field(
        proto.MESSAGE,
        number=107,
        message=DiscoveryStatus,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
