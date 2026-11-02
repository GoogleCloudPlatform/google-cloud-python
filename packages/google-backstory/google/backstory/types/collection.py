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
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.type.interval_pb2 as interval_pb2  # type: ignore
import proto  # type: ignore

from google.backstory.types import entity as gb_entity
from google.backstory.types import id as gb_id
from google.backstory.types import udm

__protobuf__ = proto.module(
    package="google.backstory",
    manifest={
        "Collection",
        "EntityGraphEnrichment",
        "DataTableRowInfo",
        "LatencyMetrics",
        "Reference",
        "Element",
        "ResponsePlatformInfo",
        "SoarAlertMetadata",
    },
)


class Collection(proto.Message):
    r"""Collection represents a container of objects (such as events,
    entity context metadata, detection finding metadata) and state
    (such as investigation details).

    An example use case for Collection is to model a detection and
    investigation from detection finding metadata to investigative
    state collected in the course of the investigation. For more
    complex investigation and response workflows a Collection could
    represent an incident consisting of multiple child findings or
    incidents. This can be expanded on to model remediation elements
    of a full detection and response workflow.

    Attributes:
        id (str):
            Unique ID for the collection.
            The ID is specific to the type of collection.
            For example, with rule detections this is the
            detection ID.
        type_ (google.backstory.types.Collection.CollectionType):
            What the collection represents.
        id_namespace (google.backstory.types.Id.Namespace):
            The ID namespace used for the Collection.
        created_time (google.protobuf.timestamp_pb2.Timestamp):
            Time the collection was created.
        last_updated_time (google.protobuf.timestamp_pb2.Timestamp):
            Time the collection was last updated.
        time_window (google.type.interval_pb2.Interval):
            Time interval that the collection represents.
        collection_elements (MutableSequence[google.backstory.types.Element]):
            Constituent elements of the collection. Each
            element shares an association that groups it
            together and is a component of the overall
            collection. For example, a detection collection
            may have several constituent elements that each
            share a correlation association that together
            represent a particular pattern or behavior.
        detection (MutableSequence[google.backstory.types.SecurityResult]):
            Detection metadata for findings that
            represent detections, can include rule details,
            machine learning model metadata, and indicators
            implicated in the detection (using the .about
            field).
        detection_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp within the time_window related to the time of the
            collection_elements. For Rule Detections, this timestamp is
            the end of the the time_window for multi-event rules or the
            time of the event for single event rules. For late-arriving
            events that trigger new alerts, the detection_time will be
            the event time of the event.
        investigation (google.backstory.types.Investigation):
            Consolidated investigation details
            (categorization, status, etc) typically for
            collections that begin as detection findings and
            then evolve with analyst action and feedback
            into investigations around the detection output.
        tags (MutableSequence[str]):
            Tags set by UC/DSML/RE for the Finding during
            creation.
        response_platform_info (google.backstory.types.ResponsePlatformInfo):
            Alert related info of this same alert in
            customer's SOAR platform.
        case_name (str):
            The resource name of the Case that this collection belongs
            to. Example: projects/{project
            id}/locations/{region}/chronicle/cases/{internal_case_id}
        soar_alert (bool):
            A boolean field indicating that the alert is
            present in SOAR.
        soar_alert_metadata (google.backstory.types.SoarAlertMetadata):
            Metadata fields of alerts coming from other
            SIEM systems via SOAR.
        data_access_scope (str):
            The resource name of the DataAccessScope of
            this collection.
        detection_timing_details (MutableSequence[google.backstory.types.Collection.DetectionTimingDetails]):
            Detection timing details for the collection.
            These details are used to determine prossible
            causes of latency for the detection. This field
            is only set for detections that are generated by
            rules.
        latency_metrics (google.backstory.types.LatencyMetrics):
            The latency metrics for the specific
            detection. These metrics are calculated from ALL
            of the events that contribute to the detection,
            not just the sampled ones.
        rule_run_frequency (google.backstory.types.Collection.RunFrequency):
            The run frequency of the rule when it
            generated the detection.
        simulated_event_count (int):
            The total number of simulated events that
            contributed to this detection. Simulated events
            are realistic threat sequences (Raw Logs or UDM)
            programmatically delivered into the production
            ingestion pipeline to verify the entire
            detection lifecycle—from identification to
            action.
        simulated_event_names (MutableSequence[str]):
            The set of all values from event ingestion_labels where
            SIMULATED is set as the key, for all simulated events that
            participated in this detection.
    """

    class CollectionType(proto.Enum):
        r"""The type of the collection which will indicate which other
        fields are relevant. For example, detection finding collections
        will populate the detection field. Findings that evolve into
        investigations will populate the investigation field.

        Values:
            COLLECTION_TYPE_UNSPECIFIED (0):
                An unspecified collection type.
            TELEMETRY_ALERT (1):
                An alert reported in customer telemetry.
            GCTI_FINDING (2):
                A finding from the Uppercase team.
            UPPERCASE_ALERT (2):
                No description available.
            RULE_DETECTION (3):
                A detection found by applying a rule.
            MACHINE_INTELLIGENCE_ALERT (4):
                An alert generated by Chronicle machine
                learning models.
            SOAR_ALERT (5):
                An alert coming from other SIEMs via
                Chronicle SOAR.
        """

        _pb_options = {"allow_alias": True}
        COLLECTION_TYPE_UNSPECIFIED = 0
        TELEMETRY_ALERT = 1
        GCTI_FINDING = 2
        UPPERCASE_ALERT = 2
        RULE_DETECTION = 3
        MACHINE_INTELLIGENCE_ALERT = 4
        SOAR_ALERT = 5

    class DetectionTimingDetails(proto.Enum):
        r"""Detection timing details for the collection.

        Values:
            DETECTION_TIMING_DETAILS_UNSPECIFIED (0):
                Detection timing details are unspecified.
            DETECTION_TIMING_DETAILS_REPROCESSING (1):
                Detection is generated by a reprocessing run.
            DETECTION_TIMING_DETAILS_RETROHUNT (2):
                Detection is generated by a retrohunt run.
        """

        DETECTION_TIMING_DETAILS_UNSPECIFIED = 0
        DETECTION_TIMING_DETAILS_REPROCESSING = 1
        DETECTION_TIMING_DETAILS_RETROHUNT = 2

    class RunFrequency(proto.Enum):
        r"""Run frequencies used by rule executions.

        Values:
            RUN_FREQUENCY_UNSPECIFIED (0):
                Unspecified run frequency.
            RUN_FREQUENCY_REALTIME (1):
                Real-time run frequency.
            RUN_FREQUENCY_HOURLY (2):
                Executes once an hour.
            RUN_FREQUENCY_DAILY (3):
                Executes once a day.
        """

        RUN_FREQUENCY_UNSPECIFIED = 0
        RUN_FREQUENCY_REALTIME = 1
        RUN_FREQUENCY_HOURLY = 2
        RUN_FREQUENCY_DAILY = 3

    id: str = proto.Field(
        proto.STRING,
        number=7,
    )
    type_: CollectionType = proto.Field(
        proto.ENUM,
        number=1,
        enum=CollectionType,
    )
    id_namespace: gb_id.Id.Namespace = proto.Field(
        proto.ENUM,
        number=12,
        enum=gb_id.Id.Namespace,
    )
    created_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    last_updated_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    time_window: interval_pb2.Interval = proto.Field(
        proto.MESSAGE,
        number=8,
        message=interval_pb2.Interval,
    )
    collection_elements: MutableSequence["Element"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="Element",
    )
    detection: MutableSequence[udm.SecurityResult] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=udm.SecurityResult,
    )
    detection_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    investigation: udm.Investigation = proto.Field(
        proto.MESSAGE,
        number=4,
        message=udm.Investigation,
    )
    tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=11,
    )
    response_platform_info: "ResponsePlatformInfo" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="ResponsePlatformInfo",
    )
    case_name: str = proto.Field(
        proto.STRING,
        number=14,
    )
    soar_alert: bool = proto.Field(
        proto.BOOL,
        number=17,
    )
    soar_alert_metadata: "SoarAlertMetadata" = proto.Field(
        proto.MESSAGE,
        number=18,
        message="SoarAlertMetadata",
    )
    data_access_scope: str = proto.Field(
        proto.STRING,
        number=19,
    )
    detection_timing_details: MutableSequence[DetectionTimingDetails] = (
        proto.RepeatedField(
            proto.ENUM,
            number=20,
            enum=DetectionTimingDetails,
        )
    )
    latency_metrics: "LatencyMetrics" = proto.Field(
        proto.MESSAGE,
        number=21,
        message="LatencyMetrics",
    )
    rule_run_frequency: RunFrequency = proto.Field(
        proto.ENUM,
        number=22,
        enum=RunFrequency,
    )
    simulated_event_count: int = proto.Field(
        proto.INT64,
        number=23,
    )
    simulated_event_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=24,
    )


class EntityGraphEnrichment(proto.Message):
    r"""EntityGraphEnrichment contains the data table name and the
    enrichment applied to the entity.

    Attributes:
        data_table (str):
            The name of the data table.
        enrichment_type (google.backstory.types.EntityGraphEnrichment.EnrichmentType):
            The type of enrichment.
        overridden_entity (google.backstory.types.Entity):
            The entity which has only the overridden
            fields populated. Only populated if the
            enrichment type is OVERRIDE.
    """

    class EnrichmentType(proto.Enum):
        r"""Type of enrichment.

        Values:
            ENRICHMENT_TYPE_UNSPECIFIED (0):
                Enrichment type is unspecified.
            APPEND (1):
                The data table was appended to the entity
                graph.
            OVERRIDE (2):
                The entity graph was overridden by the data
                table.
        """

        ENRICHMENT_TYPE_UNSPECIFIED = 0
        APPEND = 1
        OVERRIDE = 2

    data_table: str = proto.Field(
        proto.STRING,
        number=1,
    )
    enrichment_type: EnrichmentType = proto.Field(
        proto.ENUM,
        number=3,
        enum=EnrichmentType,
    )
    overridden_entity: gb_entity.Entity = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gb_entity.Entity,
    )


class DataTableRowInfo(proto.Message):
    r"""DataTableRowInfo captures information about a data table row
    including the name of the data table.

    Attributes:
        data_table (str):
            The name of data table.
        row (google.protobuf.struct_pb2.Struct):
            Stores the key value pair for a data table
            row where the key is the name of the column for
            the given value.
        row_id (str):
            The row id of the data table row.
    """

    data_table: str = proto.Field(
        proto.STRING,
        number=1,
    )
    row: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Struct,
    )
    row_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class LatencyMetrics(proto.Message):
    r"""LatencyMetrics contains relevant timestamps for measuring
    latency per event variable. These metrics are calculated from
    ALL of the events that contribute to the detection, not just the
    sampled ones.

    Attributes:
        oldest_ingestion_time (google.protobuf.timestamp_pb2.Timestamp):
            The oldest ingestion timestamp from the
            events used to create the detection.
        newest_ingestion_time (google.protobuf.timestamp_pb2.Timestamp):
            The newest (most recent) ingestion timestamp
            from the events used to create the detection.
        oldest_event_time (google.protobuf.timestamp_pb2.Timestamp):
            The oldest event timestamp from the events
            used to create the detection.
        newest_event_time (google.protobuf.timestamp_pb2.Timestamp):
            The newest (most recent) event timestamp from
            the events used to create the detection.
        ingestion_latency (google.protobuf.duration_pb2.Duration):
            The difference between newest ingestion
            timestamp and newest event timestamp.
    """

    oldest_ingestion_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    newest_ingestion_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    oldest_event_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    newest_event_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    ingestion_latency: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=5,
        message=duration_pb2.Duration,
    )


class Reference(proto.Message):
    r"""Reference to model primatives including event and entity. As
    support is added for fast retrieval of objects by identifiers,
    this will be expanded to include ID references rather than full
    object copies.

    Attributes:
        event (google.backstory.types.UDM):
            Only one of event or entity will be populated
            for a single reference.
            Start one-of
            Event being referenced.
        entity (google.backstory.types.Entity):
            Entity being referenced. In cases where the
            entity graph is overridden by data table, this
            will represent the original entity. End one-of
        joined_data_table_rows (MutableSequence[google.backstory.types.DataTableRowInfo]):
            The data table rows joined with the event.
        graph_enrichment (google.backstory.types.EntityGraphEnrichment):
            The entity graph enrichment details. Only set
            when the reference is an Entity which has been
            overridden by a data table or appended from a
            data table.
        id (google.backstory.types.Id):
            Id being referenced. This field will also be
            populated for both event and entity with the
            event id. For detections, only this field will
            be populated.
        log_batch_token (str):
            The log batch token of the event being
            referenced. This field is used to fetch the raw
            log associated with the event in some legacy
            systems. This field is only populated for
            events/entities.
    """

    event: udm.UDM = proto.Field(
        proto.MESSAGE,
        number=1,
        message=udm.UDM,
    )
    entity: gb_entity.Entity = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gb_entity.Entity,
    )
    joined_data_table_rows: MutableSequence["DataTableRowInfo"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="DataTableRowInfo",
    )
    graph_enrichment: "EntityGraphEnrichment" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="EntityGraphEnrichment",
    )
    id: gb_id.Id = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gb_id.Id,
    )
    log_batch_token: str = proto.Field(
        proto.STRING,
        number=6,
    )


class Element(proto.Message):
    r"""

    Attributes:
        association (google.backstory.types.SecurityResult):
            Metadata that provides the relevant
            association for the references in the element.
            For a detection, this can be the correlated
            aspect of the references that contributed to the
            overall detection. For example, may include
            sub-rule condition, machine learning model
            metadata, and/or indicators implicated in this
            component of the detection (using the .about
            field).
        references (MutableSequence[google.backstory.types.Reference]):
            References to model primatives including
            events and entities that share a common
            association. Even though a reference can have
            both UDM and entity, a collection of references
            (of a single element) will only have one type of
            message in it (either UDM / Entity).
        label (str):
            A name that labels the entire references
            group.
        references_sampled (bool):
            Copied from the detection
            event_sample.too_many_event_samples field. If true, the
            number of references will be capped at the sample limit (set
            at rule service). This is applicable to both UDM references
            and Entity references.
        latency_metrics (google.backstory.types.LatencyMetrics):
            Latency metrics for the specific element.
            These are calculated from all the contributing
            events or entities for a single event variable,
            not just the sampled ones included in
            references. This is currently only populated for
            UDM events.
    """

    association: udm.SecurityResult = proto.Field(
        proto.MESSAGE,
        number=1,
        message=udm.SecurityResult,
    )
    references: MutableSequence["Reference"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Reference",
    )
    label: str = proto.Field(
        proto.STRING,
        number=3,
    )
    references_sampled: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    latency_metrics: "LatencyMetrics" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="LatencyMetrics",
    )


class ResponsePlatformInfo(proto.Message):
    r"""Related info of an Alert in customer's SOAR platform.

    Attributes:
        alert_id (str):
            Id of the alert in SOAR product.
        response_platform_type (google.backstory.types.ResponsePlatformInfo.ResponsePlatformType):
            Type of SOAR product.
    """

    class ResponsePlatformType(proto.Enum):
        r"""Available response platforms.

        Values:
            RESPONSE_PLATFORM_TYPE_UNSPECIFIED (0):
                Response platform not specified.
            RESPONSE_PLATFORM_TYPE_SIEMPLIFY (1):
                Siemplify
        """

        RESPONSE_PLATFORM_TYPE_UNSPECIFIED = 0
        RESPONSE_PLATFORM_TYPE_SIEMPLIFY = 1

    alert_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    response_platform_type: ResponsePlatformType = proto.Field(
        proto.ENUM,
        number=3,
        enum=ResponsePlatformType,
    )


class SoarAlertMetadata(proto.Message):
    r"""Metadata fields of alerts coming from other SIEM systems.

    Attributes:
        alert_id (str):
            Alert ID in the source SIEM system.
        source_rule (str):
            Name of the rule triggering the alert in the
            source SIEM.
        vendor (str):
            Name of the vendor.
        source_system (str):
            Name of the Source SIEM system.
        product (str):
            Name of the product the alert is coming from.
        source_system_ticket_id (str):
            Ticket id for the alert in the source system.
        source_system_uri (str):
            Url to the source SIEM system.
    """

    alert_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source_rule: str = proto.Field(
        proto.STRING,
        number=2,
    )
    vendor: str = proto.Field(
        proto.STRING,
        number=3,
    )
    source_system: str = proto.Field(
        proto.STRING,
        number=4,
    )
    product: str = proto.Field(
        proto.STRING,
        number=5,
    )
    source_system_ticket_id: str = proto.Field(
        proto.STRING,
        number=6,
    )
    source_system_uri: str = proto.Field(
        proto.STRING,
        number=7,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
