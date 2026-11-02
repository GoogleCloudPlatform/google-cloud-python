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

from google.cloud.dataplex_v1.types import datascans_common

__protobuf__ = proto.module(
    package="google.cloud.dataplex.v1",
    manifest={
        "DiscoveryEvent",
        "JobEvent",
        "SessionEvent",
        "GovernanceEvent",
        "DataScanEvent",
        "DataQualityScanRuleResult",
        "BusinessGlossaryEvent",
        "EntryLinkEvent",
    },
)


class DiscoveryEvent(proto.Message):
    r"""The payload associated with Discovery data processing.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        message (str):
            The log message.
        lake_id (str):
            The id of the associated lake.
        zone_id (str):
            The id of the associated zone.
        asset_id (str):
            The id of the associated asset.
        data_location (str):
            The data location associated with the event.
        datascan_id (str):
            The id of the associated datascan for
            standalone discovery.
        type_ (google.cloud.dataplex_v1.types.DiscoveryEvent.EventType):
            The type of the event being logged.
        config (google.cloud.dataplex_v1.types.DiscoveryEvent.ConfigDetails):
            Details about discovery configuration in
            effect.

            This field is a member of `oneof`_ ``details``.
        entity (google.cloud.dataplex_v1.types.DiscoveryEvent.EntityDetails):
            Details about the entity associated with the
            event.

            This field is a member of `oneof`_ ``details``.
        partition (google.cloud.dataplex_v1.types.DiscoveryEvent.PartitionDetails):
            Details about the partition associated with
            the event.

            This field is a member of `oneof`_ ``details``.
        action (google.cloud.dataplex_v1.types.DiscoveryEvent.ActionDetails):
            Details about the action associated with the
            event.

            This field is a member of `oneof`_ ``details``.
        table (google.cloud.dataplex_v1.types.DiscoveryEvent.TableDetails):
            Details about the BigQuery table publishing
            associated with the event.

            This field is a member of `oneof`_ ``details``.
    """

    class EventType(proto.Enum):
        r"""The type of the event.

        Values:
            EVENT_TYPE_UNSPECIFIED (0):
                An unspecified event type.
            CONFIG (1):
                An event representing discovery configuration
                in effect.
            ENTITY_CREATED (2):
                An event representing a metadata entity being
                created.
            ENTITY_UPDATED (3):
                An event representing a metadata entity being
                updated.
            ENTITY_DELETED (4):
                An event representing a metadata entity being
                deleted.
            PARTITION_CREATED (5):
                An event representing a partition being
                created.
            PARTITION_UPDATED (6):
                An event representing a partition being
                updated.
            PARTITION_DELETED (7):
                An event representing a partition being
                deleted.
            TABLE_PUBLISHED (10):
                An event representing a table being
                published.
            TABLE_UPDATED (11):
                An event representing a table being updated.
            TABLE_IGNORED (12):
                An event representing a table being skipped
                in publishing.
            TABLE_DELETED (13):
                An event representing a table being deleted.
        """

        EVENT_TYPE_UNSPECIFIED = 0
        CONFIG = 1
        ENTITY_CREATED = 2
        ENTITY_UPDATED = 3
        ENTITY_DELETED = 4
        PARTITION_CREATED = 5
        PARTITION_UPDATED = 6
        PARTITION_DELETED = 7
        TABLE_PUBLISHED = 10
        TABLE_UPDATED = 11
        TABLE_IGNORED = 12
        TABLE_DELETED = 13

    class EntityType(proto.Enum):
        r"""The type of the entity.

        Values:
            ENTITY_TYPE_UNSPECIFIED (0):
                An unspecified event type.
            TABLE (1):
                Entities representing structured data.
            FILESET (2):
                Entities representing unstructured data.
        """

        ENTITY_TYPE_UNSPECIFIED = 0
        TABLE = 1
        FILESET = 2

    class TableType(proto.Enum):
        r"""The type of the published table.

        Values:
            TABLE_TYPE_UNSPECIFIED (0):
                An unspecified table type.
            EXTERNAL_TABLE (1):
                External table type.
            BIGLAKE_TABLE (2):
                BigLake table type.
            OBJECT_TABLE (3):
                Object table type for unstructured data.
        """

        TABLE_TYPE_UNSPECIFIED = 0
        EXTERNAL_TABLE = 1
        BIGLAKE_TABLE = 2
        OBJECT_TABLE = 3

    class ConfigDetails(proto.Message):
        r"""Details about configuration events.

        Attributes:
            parameters (MutableMapping[str, str]):
                A list of discovery configuration parameters
                in effect. The keys are the field paths within
                DiscoverySpec. Eg. includePatterns,
                excludePatterns,
                csvOptions.disableTypeInference, etc.
        """

        parameters: MutableMapping[str, str] = proto.MapField(
            proto.STRING,
            proto.STRING,
            number=1,
        )

    class EntityDetails(proto.Message):
        r"""Details about the entity.

        Attributes:
            entity (str):
                The name of the entity resource.
                The name is the fully-qualified resource name.
            type_ (google.cloud.dataplex_v1.types.DiscoveryEvent.EntityType):
                The type of the entity resource.
        """

        entity: str = proto.Field(
            proto.STRING,
            number=1,
        )
        type_: "DiscoveryEvent.EntityType" = proto.Field(
            proto.ENUM,
            number=2,
            enum="DiscoveryEvent.EntityType",
        )

    class TableDetails(proto.Message):
        r"""Details about the published table.

        Attributes:
            table (str):
                The fully-qualified resource name of the
                table resource.
            type_ (google.cloud.dataplex_v1.types.DiscoveryEvent.TableType):
                The type of the table resource.
        """

        table: str = proto.Field(
            proto.STRING,
            number=1,
        )
        type_: "DiscoveryEvent.TableType" = proto.Field(
            proto.ENUM,
            number=2,
            enum="DiscoveryEvent.TableType",
        )

    class PartitionDetails(proto.Message):
        r"""Details about the partition.

        Attributes:
            partition (str):
                The name to the partition resource.
                The name is the fully-qualified resource name.
            entity (str):
                The name to the containing entity resource.
                The name is the fully-qualified resource name.
            type_ (google.cloud.dataplex_v1.types.DiscoveryEvent.EntityType):
                The type of the containing entity resource.
            sampled_data_locations (MutableSequence[str]):
                The locations of the data items (e.g., a
                Cloud Storage objects) sampled for metadata
                inference.
        """

        partition: str = proto.Field(
            proto.STRING,
            number=1,
        )
        entity: str = proto.Field(
            proto.STRING,
            number=2,
        )
        type_: "DiscoveryEvent.EntityType" = proto.Field(
            proto.ENUM,
            number=3,
            enum="DiscoveryEvent.EntityType",
        )
        sampled_data_locations: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=4,
        )

    class ActionDetails(proto.Message):
        r"""Details about the action.

        Attributes:
            type_ (str):
                The type of action.
                Eg. IncompatibleDataSchema, InvalidDataFormat
            issue (str):
                The human readable issue associated with the
                action.
        """

        type_: str = proto.Field(
            proto.STRING,
            number=1,
        )
        issue: str = proto.Field(
            proto.STRING,
            number=2,
        )

    message: str = proto.Field(
        proto.STRING,
        number=1,
    )
    lake_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    zone_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    asset_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    data_location: str = proto.Field(
        proto.STRING,
        number=5,
    )
    datascan_id: str = proto.Field(
        proto.STRING,
        number=6,
    )
    type_: EventType = proto.Field(
        proto.ENUM,
        number=10,
        enum=EventType,
    )
    config: ConfigDetails = proto.Field(
        proto.MESSAGE,
        number=20,
        oneof="details",
        message=ConfigDetails,
    )
    entity: EntityDetails = proto.Field(
        proto.MESSAGE,
        number=21,
        oneof="details",
        message=EntityDetails,
    )
    partition: PartitionDetails = proto.Field(
        proto.MESSAGE,
        number=22,
        oneof="details",
        message=PartitionDetails,
    )
    action: ActionDetails = proto.Field(
        proto.MESSAGE,
        number=23,
        oneof="details",
        message=ActionDetails,
    )
    table: TableDetails = proto.Field(
        proto.MESSAGE,
        number=24,
        oneof="details",
        message=TableDetails,
    )


class JobEvent(proto.Message):
    r"""The payload associated with Job logs that contains events
    describing jobs that have run within a Lake.

    Attributes:
        message (str):
            The log message.
        job_id (str):
            The unique id identifying the job.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the job started running.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the job ended running.
        state (google.cloud.dataplex_v1.types.JobEvent.State):
            The job state on completion.
        retries (int):
            The number of retries.
        type_ (google.cloud.dataplex_v1.types.JobEvent.Type):
            The type of the job.
        service (google.cloud.dataplex_v1.types.JobEvent.Service):
            The service used to execute the job.
        service_job (str):
            The reference to the job within the service.
        execution_trigger (google.cloud.dataplex_v1.types.JobEvent.ExecutionTrigger):
            Job execution trigger.
    """

    class Type(proto.Enum):
        r"""The type of the job.

        Values:
            TYPE_UNSPECIFIED (0):
                Unspecified job type.
            SPARK (1):
                Spark jobs.
            NOTEBOOK (2):
                Notebook jobs.
        """

        TYPE_UNSPECIFIED = 0
        SPARK = 1
        NOTEBOOK = 2

    class State(proto.Enum):
        r"""The completion status of the job.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified job state.
            SUCCEEDED (1):
                Job successfully completed.
            FAILED (2):
                Job was unsuccessful.
            CANCELLED (3):
                Job was cancelled by the user.
            ABORTED (4):
                Job was cancelled or aborted via the service
                executing the job.
        """

        STATE_UNSPECIFIED = 0
        SUCCEEDED = 1
        FAILED = 2
        CANCELLED = 3
        ABORTED = 4

    class Service(proto.Enum):
        r"""The service used to execute the job.

        Values:
            SERVICE_UNSPECIFIED (0):
                Unspecified service.
            DATAPROC (1):
                Cloud Dataproc.
        """

        SERVICE_UNSPECIFIED = 0
        DATAPROC = 1

    class ExecutionTrigger(proto.Enum):
        r"""Job Execution trigger.

        Values:
            EXECUTION_TRIGGER_UNSPECIFIED (0):
                The job execution trigger is unspecified.
            TASK_CONFIG (1):
                The job was triggered by Dataplex Universal
                Catalog based on trigger spec from task
                definition.
            RUN_REQUEST (2):
                The job was triggered by the explicit call of
                Task API.
        """

        EXECUTION_TRIGGER_UNSPECIFIED = 0
        TASK_CONFIG = 1
        RUN_REQUEST = 2

    message: str = proto.Field(
        proto.STRING,
        number=1,
    )
    job_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    retries: int = proto.Field(
        proto.INT32,
        number=6,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=7,
        enum=Type,
    )
    service: Service = proto.Field(
        proto.ENUM,
        number=8,
        enum=Service,
    )
    service_job: str = proto.Field(
        proto.STRING,
        number=9,
    )
    execution_trigger: ExecutionTrigger = proto.Field(
        proto.ENUM,
        number=11,
        enum=ExecutionTrigger,
    )


class SessionEvent(proto.Message):
    r"""These messages contain information about sessions within an
    environment. The monitored resource is 'Environment'.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        message (str):
            The log message.
        user_id (str):
            The information about the user that created
            the session. It will be the email address of the
            user.
        session_id (str):
            Unique identifier for the session.
        type_ (google.cloud.dataplex_v1.types.SessionEvent.EventType):
            The type of the event.
        query (google.cloud.dataplex_v1.types.SessionEvent.QueryDetail):
            The execution details of the query.

            This field is a member of `oneof`_ ``detail``.
        event_succeeded (bool):
            The status of the event.
        fast_startup_enabled (bool):
            If the session is associated with an
            environment with fast startup enabled, and was
            created before being assigned to a user.
        unassigned_duration (google.protobuf.duration_pb2.Duration):
            The idle duration of a warm pooled session
            before it is assigned to user.
    """

    class EventType(proto.Enum):
        r"""The type of the event.

        Values:
            EVENT_TYPE_UNSPECIFIED (0):
                An unspecified event type.
            START (1):
                Event when the session is assigned to a user.
            STOP (2):
                Event for stop of a session.
            QUERY (3):
                Query events in the session.
            CREATE (4):
                Event for creation of a cluster. It is not
                yet assigned to a user. This comes before START
                in the sequence
        """

        EVENT_TYPE_UNSPECIFIED = 0
        START = 1
        STOP = 2
        QUERY = 3
        CREATE = 4

    class QueryDetail(proto.Message):
        r"""Execution details of the query.

        Attributes:
            query_id (str):
                The unique Query id identifying the query.
            query_text (str):
                The query text executed.
            engine (google.cloud.dataplex_v1.types.SessionEvent.QueryDetail.Engine):
                Query Execution engine.
            duration (google.protobuf.duration_pb2.Duration):
                Time taken for execution of the query.
            result_size_bytes (int):
                The size of results the query produced.
            data_processed_bytes (int):
                The data processed by the query.
        """

        class Engine(proto.Enum):
            r"""Query Execution engine.

            Values:
                ENGINE_UNSPECIFIED (0):
                    An unspecified Engine type.
                SPARK_SQL (1):
                    Spark-sql engine is specified in Query.
                BIGQUERY (2):
                    BigQuery engine is specified in Query.
            """

            ENGINE_UNSPECIFIED = 0
            SPARK_SQL = 1
            BIGQUERY = 2

        query_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        query_text: str = proto.Field(
            proto.STRING,
            number=2,
        )
        engine: "SessionEvent.QueryDetail.Engine" = proto.Field(
            proto.ENUM,
            number=3,
            enum="SessionEvent.QueryDetail.Engine",
        )
        duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=4,
            message=duration_pb2.Duration,
        )
        result_size_bytes: int = proto.Field(
            proto.INT64,
            number=5,
        )
        data_processed_bytes: int = proto.Field(
            proto.INT64,
            number=6,
        )

    message: str = proto.Field(
        proto.STRING,
        number=1,
    )
    user_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    session_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    type_: EventType = proto.Field(
        proto.ENUM,
        number=4,
        enum=EventType,
    )
    query: QueryDetail = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="detail",
        message=QueryDetail,
    )
    event_succeeded: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    fast_startup_enabled: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    unassigned_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=8,
        message=duration_pb2.Duration,
    )


class GovernanceEvent(proto.Message):
    r"""Payload associated with Governance related log events.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        message (str):
            The log message.
        event_type (google.cloud.dataplex_v1.types.GovernanceEvent.EventType):
            The type of the event.
        entity (google.cloud.dataplex_v1.types.GovernanceEvent.Entity):
            Entity resource information if the log event
            is associated with a specific entity.

            This field is a member of `oneof`_ ``_entity``.
    """

    class EventType(proto.Enum):
        r"""Type of governance log event.

        Values:
            EVENT_TYPE_UNSPECIFIED (0):
                An unspecified event type.
            RESOURCE_IAM_POLICY_UPDATE (1):
                Resource IAM policy update event.
            BIGQUERY_TABLE_CREATE (2):
                BigQuery table create event.
            BIGQUERY_TABLE_UPDATE (3):
                BigQuery table update event.
            BIGQUERY_TABLE_DELETE (4):
                BigQuery table delete event.
            BIGQUERY_CONNECTION_CREATE (5):
                BigQuery connection create event.
            BIGQUERY_CONNECTION_UPDATE (6):
                BigQuery connection update event.
            BIGQUERY_CONNECTION_DELETE (7):
                BigQuery connection delete event.
            BIGQUERY_TAXONOMY_CREATE (10):
                BigQuery taxonomy created.
            BIGQUERY_POLICY_TAG_CREATE (11):
                BigQuery policy tag created.
            BIGQUERY_POLICY_TAG_DELETE (12):
                BigQuery policy tag deleted.
            BIGQUERY_POLICY_TAG_SET_IAM_POLICY (13):
                BigQuery set iam policy for policy tag.
            ACCESS_POLICY_UPDATE (14):
                Access policy update event.
            GOVERNANCE_RULE_MATCHED_RESOURCES (15):
                Number of resources matched with particular
                Query.
            GOVERNANCE_RULE_SEARCH_LIMIT_EXCEEDS (16):
                Rule processing exceeds the allowed limit.
            GOVERNANCE_RULE_ERRORS (17):
                Rule processing errors.
            GOVERNANCE_RULE_PROCESSING (18):
                Governance rule processing Event.
        """

        EVENT_TYPE_UNSPECIFIED = 0
        RESOURCE_IAM_POLICY_UPDATE = 1
        BIGQUERY_TABLE_CREATE = 2
        BIGQUERY_TABLE_UPDATE = 3
        BIGQUERY_TABLE_DELETE = 4
        BIGQUERY_CONNECTION_CREATE = 5
        BIGQUERY_CONNECTION_UPDATE = 6
        BIGQUERY_CONNECTION_DELETE = 7
        BIGQUERY_TAXONOMY_CREATE = 10
        BIGQUERY_POLICY_TAG_CREATE = 11
        BIGQUERY_POLICY_TAG_DELETE = 12
        BIGQUERY_POLICY_TAG_SET_IAM_POLICY = 13
        ACCESS_POLICY_UPDATE = 14
        GOVERNANCE_RULE_MATCHED_RESOURCES = 15
        GOVERNANCE_RULE_SEARCH_LIMIT_EXCEEDS = 16
        GOVERNANCE_RULE_ERRORS = 17
        GOVERNANCE_RULE_PROCESSING = 18

    class Entity(proto.Message):
        r"""Information about Entity resource that the log event is
        associated with.

        Attributes:
            entity (str):
                The Entity resource the log event is associated with.
                Format:
                ``projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/entities/{entity_id}``
            entity_type (google.cloud.dataplex_v1.types.GovernanceEvent.Entity.EntityType):
                Type of entity.
        """

        class EntityType(proto.Enum):
            r"""Type of entity.

            Values:
                ENTITY_TYPE_UNSPECIFIED (0):
                    An unspecified Entity type.
                TABLE (1):
                    Table entity type.
                FILESET (2):
                    Fileset entity type.
            """

            ENTITY_TYPE_UNSPECIFIED = 0
            TABLE = 1
            FILESET = 2

        entity: str = proto.Field(
            proto.STRING,
            number=1,
        )
        entity_type: "GovernanceEvent.Entity.EntityType" = proto.Field(
            proto.ENUM,
            number=2,
            enum="GovernanceEvent.Entity.EntityType",
        )

    message: str = proto.Field(
        proto.STRING,
        number=1,
    )
    event_type: EventType = proto.Field(
        proto.ENUM,
        number=2,
        enum=EventType,
    )
    entity: Entity = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message=Entity,
    )


class DataScanEvent(proto.Message):
    r"""These messages contain information about the execution of a
    datascan. The monitored resource is 'DataScan'

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        data_source (str):
            The data source of the data scan
        job_id (str):
            The identifier of the specific data scan job
            this log entry is for.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the data scan job was created.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the data scan job started to
            run.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when the data scan job finished.
        type_ (google.cloud.dataplex_v1.types.DataScanEvent.ScanType):
            The type of the data scan.
        state (google.cloud.dataplex_v1.types.DataScanEvent.State):
            The status of the data scan job.
        message (str):
            The message describing the data scan job
            event.
        spec_version (str):
            A version identifier of the spec which was
            used to execute this job.
        trigger (google.cloud.dataplex_v1.types.DataScanEvent.Trigger):
            The trigger type of the data scan job.
        scope (google.cloud.dataplex_v1.types.DataScanEvent.Scope):
            The scope of the data scan (e.g. full,
            incremental).
        data_profile (google.cloud.dataplex_v1.types.DataScanEvent.DataProfileResult):
            Data profile result for data profile type
            data scan.

            This field is a member of `oneof`_ ``result``.
        data_quality (google.cloud.dataplex_v1.types.DataScanEvent.DataQualityResult):
            Data quality result for data quality type
            data scan.

            This field is a member of `oneof`_ ``result``.
        data_profile_configs (google.cloud.dataplex_v1.types.DataScanEvent.DataProfileAppliedConfigs):
            Applied configs for data profile type data
            scan.

            This field is a member of `oneof`_ ``appliedConfigs``.
        data_quality_configs (google.cloud.dataplex_v1.types.DataScanEvent.DataQualityAppliedConfigs):
            Applied configs for data quality type data
            scan.

            This field is a member of `oneof`_ ``appliedConfigs``.
        post_scan_actions_result (google.cloud.dataplex_v1.types.DataScanEvent.PostScanActionsResult):
            The result of post scan actions.
        catalog_publishing_status (google.cloud.dataplex_v1.types.DataScanCatalogPublishingStatus):
            The status of publishing the data scan as
            Dataplex Universal Catalog metadata.
    """

    class ScanType(proto.Enum):
        r"""The type of the data scan.

        Values:
            SCAN_TYPE_UNSPECIFIED (0):
                An unspecified data scan type.
            DATA_PROFILE (1):
                Data scan for data profile.
            DATA_QUALITY (2):
                Data scan for data quality.
            DATA_DISCOVERY (4):
                Data scan for data discovery.
        """

        SCAN_TYPE_UNSPECIFIED = 0
        DATA_PROFILE = 1
        DATA_QUALITY = 2
        DATA_DISCOVERY = 4

    class State(proto.Enum):
        r"""The job state of the data scan.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified job state.
            STARTED (1):
                Data scan job started.
            SUCCEEDED (2):
                Data scan job successfully completed.
            FAILED (3):
                Data scan job was unsuccessful.
            CANCELLED (4):
                Data scan job was cancelled.
            CREATED (5):
                Data scan job was created.
        """

        STATE_UNSPECIFIED = 0
        STARTED = 1
        SUCCEEDED = 2
        FAILED = 3
        CANCELLED = 4
        CREATED = 5

    class Trigger(proto.Enum):
        r"""The trigger type for the data scan.

        Values:
            TRIGGER_UNSPECIFIED (0):
                An unspecified trigger type.
            ON_DEMAND (1):
                Data scan triggers on demand.
            SCHEDULE (2):
                Data scan triggers as per schedule.
            ONE_TIME (3):
                Data scan is run one time on creation.
        """

        TRIGGER_UNSPECIFIED = 0
        ON_DEMAND = 1
        SCHEDULE = 2
        ONE_TIME = 3

    class Scope(proto.Enum):
        r"""The scope of job for the data scan.

        Values:
            SCOPE_UNSPECIFIED (0):
                An unspecified scope type.
            FULL (1):
                Data scan runs on all of the data.
            INCREMENTAL (2):
                Data scan runs on incremental data.
        """

        SCOPE_UNSPECIFIED = 0
        FULL = 1
        INCREMENTAL = 2

    class DataProfileResult(proto.Message):
        r"""Data profile result for data scan job.

        Attributes:
            row_count (int):
                The count of rows processed in the data scan
                job.
        """

        row_count: int = proto.Field(
            proto.INT64,
            number=1,
        )

    class DataQualityResult(proto.Message):
        r"""Data quality result for data scan job.

        Attributes:
            row_count (int):
                The count of rows processed in the data scan
                job.
            passed (bool):
                Whether the data quality result was ``pass`` or not.
            dimension_passed (MutableMapping[str, bool]):
                The result of each dimension for data quality result. The
                key of the map is the name of the dimension. The value is
                the bool value depicting whether the dimension result was
                ``pass`` or not.
            score (float):
                The table-level data quality score for the data scan job.

                The data quality score ranges between [0, 100] (up to two
                decimal points).
            dimension_score (MutableMapping[str, float]):
                The score of each dimension for data quality result. The key
                of the map is the name of the dimension. The value is the
                data quality score for the dimension.

                The score ranges between [0, 100] (up to two decimal
                points).
            column_score (MutableMapping[str, float]):
                The score of each column scanned in the data scan job. The
                key of the map is the name of the column. The value is the
                data quality score for the column.

                The score ranges between [0, 100] (up to two decimal
                points).
        """

        row_count: int = proto.Field(
            proto.INT64,
            number=1,
        )
        passed: bool = proto.Field(
            proto.BOOL,
            number=2,
        )
        dimension_passed: MutableMapping[str, bool] = proto.MapField(
            proto.STRING,
            proto.BOOL,
            number=3,
        )
        score: float = proto.Field(
            proto.FLOAT,
            number=4,
        )
        dimension_score: MutableMapping[str, float] = proto.MapField(
            proto.STRING,
            proto.FLOAT,
            number=5,
        )
        column_score: MutableMapping[str, float] = proto.MapField(
            proto.STRING,
            proto.FLOAT,
            number=6,
        )

    class DataProfileAppliedConfigs(proto.Message):
        r"""Applied configs for data profile type data scan job.

        Attributes:
            sampling_percent (float):
                The percentage of the records selected from the dataset for
                DataScan.

                - Value ranges between 0.0 and 100.0.
                - Value 0.0 or 100.0 imply that sampling was not applied.
            row_filter_applied (bool):
                Boolean indicating whether a row filter was
                applied in the DataScan job.
            column_filter_applied (bool):
                Boolean indicating whether a column filter
                was applied in the DataScan job.
        """

        sampling_percent: float = proto.Field(
            proto.FLOAT,
            number=1,
        )
        row_filter_applied: bool = proto.Field(
            proto.BOOL,
            number=2,
        )
        column_filter_applied: bool = proto.Field(
            proto.BOOL,
            number=3,
        )

    class DataQualityAppliedConfigs(proto.Message):
        r"""Applied configs for data quality type data scan job.

        Attributes:
            sampling_percent (float):
                The percentage of the records selected from the dataset for
                DataScan.

                - Value ranges between 0.0 and 100.0.
                - Value 0.0 or 100.0 imply that sampling was not applied.
            row_filter_applied (bool):
                Boolean indicating whether a row filter was
                applied in the DataScan job.
        """

        sampling_percent: float = proto.Field(
            proto.FLOAT,
            number=1,
        )
        row_filter_applied: bool = proto.Field(
            proto.BOOL,
            number=2,
        )

    class PostScanActionsResult(proto.Message):
        r"""Post scan actions result for data scan job.

        Attributes:
            bigquery_export_result (google.cloud.dataplex_v1.types.DataScanEvent.PostScanActionsResult.BigQueryExportResult):
                The result of BigQuery export post scan
                action.
        """

        class BigQueryExportResult(proto.Message):
            r"""The result of BigQuery export post scan action.

            Attributes:
                state (google.cloud.dataplex_v1.types.DataScanEvent.PostScanActionsResult.BigQueryExportResult.State):
                    Execution state for the BigQuery exporting.
                message (str):
                    Additional information about the BigQuery
                    exporting.
            """

            class State(proto.Enum):
                r"""Execution state for the exporting.

                Values:
                    STATE_UNSPECIFIED (0):
                        The exporting state is unspecified.
                    SUCCEEDED (1):
                        The exporting completed successfully.
                    FAILED (2):
                        The exporting is no longer running due to an
                        error.
                    SKIPPED (3):
                        The exporting is skipped due to no valid scan
                        result to export (usually caused by scan
                        failed).
                """

                STATE_UNSPECIFIED = 0
                SUCCEEDED = 1
                FAILED = 2
                SKIPPED = 3

            state: "DataScanEvent.PostScanActionsResult.BigQueryExportResult.State" = proto.Field(
                proto.ENUM,
                number=1,
                enum="DataScanEvent.PostScanActionsResult.BigQueryExportResult.State",
            )
            message: str = proto.Field(
                proto.STRING,
                number=2,
            )

        bigquery_export_result: "DataScanEvent.PostScanActionsResult.BigQueryExportResult" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="DataScanEvent.PostScanActionsResult.BigQueryExportResult",
        )

    data_source: str = proto.Field(
        proto.STRING,
        number=1,
    )
    job_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        message=timestamp_pb2.Timestamp,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    type_: ScanType = proto.Field(
        proto.ENUM,
        number=5,
        enum=ScanType,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=6,
        enum=State,
    )
    message: str = proto.Field(
        proto.STRING,
        number=7,
    )
    spec_version: str = proto.Field(
        proto.STRING,
        number=8,
    )
    trigger: Trigger = proto.Field(
        proto.ENUM,
        number=9,
        enum=Trigger,
    )
    scope: Scope = proto.Field(
        proto.ENUM,
        number=10,
        enum=Scope,
    )
    data_profile: DataProfileResult = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="result",
        message=DataProfileResult,
    )
    data_quality: DataQualityResult = proto.Field(
        proto.MESSAGE,
        number=102,
        oneof="result",
        message=DataQualityResult,
    )
    data_profile_configs: DataProfileAppliedConfigs = proto.Field(
        proto.MESSAGE,
        number=201,
        oneof="appliedConfigs",
        message=DataProfileAppliedConfigs,
    )
    data_quality_configs: DataQualityAppliedConfigs = proto.Field(
        proto.MESSAGE,
        number=202,
        oneof="appliedConfigs",
        message=DataQualityAppliedConfigs,
    )
    post_scan_actions_result: PostScanActionsResult = proto.Field(
        proto.MESSAGE,
        number=11,
        message=PostScanActionsResult,
    )
    catalog_publishing_status: datascans_common.DataScanCatalogPublishingStatus = (
        proto.Field(
            proto.MESSAGE,
            number=13,
            message=datascans_common.DataScanCatalogPublishingStatus,
        )
    )


class DataQualityScanRuleResult(proto.Message):
    r"""Information about the result of a data quality rule for data
    quality scan. The monitored resource is 'DataScan'.

    Attributes:
        job_id (str):
            Identifier of the specific data scan job this
            log entry is for.
        data_source (str):
            The data source of the data scan (e.g.
            BigQuery table name).
        column (str):
            The column which this rule is evaluated
            against.
        rule_name (str):
            The name of the data quality rule.
        rule_type (google.cloud.dataplex_v1.types.DataQualityScanRuleResult.RuleType):
            The type of the data quality rule.
        evalution_type (google.cloud.dataplex_v1.types.DataQualityScanRuleResult.EvaluationType):
            The evaluation type of the data quality rule.
        rule_dimension (str):
            The dimension of the data quality rule.
        threshold_percent (float):
            The passing threshold ([0.0, 100.0]) of the data quality
            rule.
        result (google.cloud.dataplex_v1.types.DataQualityScanRuleResult.Result):
            The result of the data quality rule.
        evaluated_row_count (int):
            The number of rows evaluated against the data quality rule.
            This field is only valid for rules of PER_ROW evaluation
            type.
        passed_row_count (int):
            The number of rows which passed a rule evaluation. This
            field is only valid for rules of PER_ROW evaluation type.
        null_row_count (int):
            The number of rows with null values in the
            specified column.
        assertion_row_count (int):
            The number of rows returned by the SQL
            statement in a SQL assertion rule. This field is
            only valid for SQL assertion rules.
    """

    class RuleType(proto.Enum):
        r"""The type of the data quality rule.

        Values:
            RULE_TYPE_UNSPECIFIED (0):
                An unspecified rule type.
            NON_NULL_EXPECTATION (1):
                See
                [DataQualityRule.NonNullExpectation][google.cloud.dataplex.v1.DataQualityRule.NonNullExpectation].
            RANGE_EXPECTATION (2):
                See
                [DataQualityRule.RangeExpectation][google.cloud.dataplex.v1.DataQualityRule.RangeExpectation].
            REGEX_EXPECTATION (3):
                See
                [DataQualityRule.RegexExpectation][google.cloud.dataplex.v1.DataQualityRule.RegexExpectation].
            ROW_CONDITION_EXPECTATION (4):
                See
                [DataQualityRule.RowConditionExpectation][google.cloud.dataplex.v1.DataQualityRule.RowConditionExpectation].
            SET_EXPECTATION (5):
                See
                [DataQualityRule.SetExpectation][google.cloud.dataplex.v1.DataQualityRule.SetExpectation].
            STATISTIC_RANGE_EXPECTATION (6):
                See
                [DataQualityRule.StatisticRangeExpectation][google.cloud.dataplex.v1.DataQualityRule.StatisticRangeExpectation].
            TABLE_CONDITION_EXPECTATION (7):
                See
                [DataQualityRule.TableConditionExpectation][google.cloud.dataplex.v1.DataQualityRule.TableConditionExpectation].
            UNIQUENESS_EXPECTATION (8):
                See
                [DataQualityRule.UniquenessExpectation][google.cloud.dataplex.v1.DataQualityRule.UniquenessExpectation].
            SQL_ASSERTION (9):
                See
                [DataQualityRule.SqlAssertion][google.cloud.dataplex.v1.DataQualityRule.SqlAssertion].
            TEMPLATE_REFERENCE (10):
                See
                [DataQualityRule.TemplateReference][google.cloud.dataplex.v1.DataQualityRule.TemplateReference].
        """

        RULE_TYPE_UNSPECIFIED = 0
        NON_NULL_EXPECTATION = 1
        RANGE_EXPECTATION = 2
        REGEX_EXPECTATION = 3
        ROW_CONDITION_EXPECTATION = 4
        SET_EXPECTATION = 5
        STATISTIC_RANGE_EXPECTATION = 6
        TABLE_CONDITION_EXPECTATION = 7
        UNIQUENESS_EXPECTATION = 8
        SQL_ASSERTION = 9
        TEMPLATE_REFERENCE = 10

    class EvaluationType(proto.Enum):
        r"""The evaluation type of the data quality rule.

        Values:
            EVALUATION_TYPE_UNSPECIFIED (0):
                An unspecified evaluation type.
            PER_ROW (1):
                The rule evaluation is done at per row level.
            AGGREGATE (2):
                The rule evaluation is done for an aggregate
                of rows.
        """

        EVALUATION_TYPE_UNSPECIFIED = 0
        PER_ROW = 1
        AGGREGATE = 2

    class Result(proto.Enum):
        r"""Whether the data quality rule passed or failed.

        Values:
            RESULT_UNSPECIFIED (0):
                An unspecified result.
            PASSED (1):
                The data quality rule passed.
            FAILED (2):
                The data quality rule failed.
        """

        RESULT_UNSPECIFIED = 0
        PASSED = 1
        FAILED = 2

    job_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_source: str = proto.Field(
        proto.STRING,
        number=2,
    )
    column: str = proto.Field(
        proto.STRING,
        number=3,
    )
    rule_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    rule_type: RuleType = proto.Field(
        proto.ENUM,
        number=5,
        enum=RuleType,
    )
    evalution_type: EvaluationType = proto.Field(
        proto.ENUM,
        number=6,
        enum=EvaluationType,
    )
    rule_dimension: str = proto.Field(
        proto.STRING,
        number=7,
    )
    threshold_percent: float = proto.Field(
        proto.DOUBLE,
        number=8,
    )
    result: Result = proto.Field(
        proto.ENUM,
        number=9,
        enum=Result,
    )
    evaluated_row_count: int = proto.Field(
        proto.INT64,
        number=10,
    )
    passed_row_count: int = proto.Field(
        proto.INT64,
        number=11,
    )
    null_row_count: int = proto.Field(
        proto.INT64,
        number=12,
    )
    assertion_row_count: int = proto.Field(
        proto.INT64,
        number=13,
    )


class BusinessGlossaryEvent(proto.Message):
    r"""Payload associated with Business Glossary related log events.

    Attributes:
        message (str):
            The log message.
        event_type (google.cloud.dataplex_v1.types.BusinessGlossaryEvent.EventType):
            The type of the event.
        resource (str):
            Name of the resource.
    """

    class EventType(proto.Enum):
        r"""Type of glossary log event.

        Values:
            EVENT_TYPE_UNSPECIFIED (0):
                An unspecified event type.
            GLOSSARY_CREATE (1):
                Glossary create event.
            GLOSSARY_UPDATE (2):
                Glossary update event.
            GLOSSARY_DELETE (3):
                Glossary delete event.
            GLOSSARY_CATEGORY_CREATE (4):
                Glossary category create event.
            GLOSSARY_CATEGORY_UPDATE (5):
                Glossary category update event.
            GLOSSARY_CATEGORY_DELETE (6):
                Glossary category delete event.
            GLOSSARY_TERM_CREATE (7):
                Glossary term create event.
            GLOSSARY_TERM_UPDATE (8):
                Glossary term update event.
            GLOSSARY_TERM_DELETE (9):
                Glossary term delete event.
        """

        EVENT_TYPE_UNSPECIFIED = 0
        GLOSSARY_CREATE = 1
        GLOSSARY_UPDATE = 2
        GLOSSARY_DELETE = 3
        GLOSSARY_CATEGORY_CREATE = 4
        GLOSSARY_CATEGORY_UPDATE = 5
        GLOSSARY_CATEGORY_DELETE = 6
        GLOSSARY_TERM_CREATE = 7
        GLOSSARY_TERM_UPDATE = 8
        GLOSSARY_TERM_DELETE = 9

    message: str = proto.Field(
        proto.STRING,
        number=1,
    )
    event_type: EventType = proto.Field(
        proto.ENUM,
        number=2,
        enum=EventType,
    )
    resource: str = proto.Field(
        proto.STRING,
        number=3,
    )


class EntryLinkEvent(proto.Message):
    r"""Payload associated with Entry related log events.

    Attributes:
        message (str):
            The log message.
        event_type (google.cloud.dataplex_v1.types.EntryLinkEvent.EventType):
            The type of the event.
        resource (str):
            Name of the resource.
    """

    class EventType(proto.Enum):
        r"""Type of entry link log event.

        Values:
            EVENT_TYPE_UNSPECIFIED (0):
                An unspecified event type.
            ENTRY_LINK_CREATE (1):
                EntryLink create event.
            ENTRY_LINK_DELETE (2):
                EntryLink delete event.
        """

        EVENT_TYPE_UNSPECIFIED = 0
        ENTRY_LINK_CREATE = 1
        ENTRY_LINK_DELETE = 2

    message: str = proto.Field(
        proto.STRING,
        number=1,
    )
    event_type: EventType = proto.Field(
        proto.ENUM,
        number=2,
        enum=EventType,
    )
    resource: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
