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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.type.interval_pb2 as interval_pb2  # type: ignore
import proto  # type: ignore

from google.backstory.types import entity_risk, udm

__protobuf__ = proto.module(
    package="google.backstory",
    manifest={
        "EntityMetadata",
        "AtiPrioritization",
        "Entity",
        "Relation",
        "Metric",
    },
)


class EntityMetadata(proto.Message):
    r"""Information about the Entity and the product where the entity
    was created.

    Attributes:
        product_entity_id (str):
            A vendor-specific identifier that uniquely
            identifies the entity (e.g. a GUID, LDAP, OID,
            or similar).
        collected_timestamp (google.protobuf.timestamp_pb2.Timestamp):
            GMT timestamp when the entity information was
            collected by the vendor's local collection
            infrastructure.
        creation_timestamp (google.protobuf.timestamp_pb2.Timestamp):
            GMT timestamp when the entity described by the
            product_entity_id was created on the system where data was
            collected.
        interval (google.type.interval_pb2.Interval):
            Valid existence time range for the version of
            the entity represented by this entity data.
        vendor_name (str):
            Vendor name of the product that produced the
            entity information.
        product_name (str):
            Product name that produced the entity
            information.
        feed (str):
            Vendor feed name for a threat indicator feed.
        product_version (str):
            Version of the product that produced the
            entity information.
        entity_type (google.backstory.types.EntityMetadata.EntityType):
            Entity type.
            If an entity has multiple possible types, this
            specifies the most specific type.
        description (str):
            Human-readable description of the entity.
        threat (MutableSequence[google.backstory.types.SecurityResult]):
            Metadata provided by a threat intelligence
            feed that identified the entity as malicious.
        source_type (google.backstory.types.EntityMetadata.SourceType):
            The source of the entity.
        source_labels (MutableSequence[google.backstory.types.Label]):
            Entity source metadata labels.
        event_metadata (google.backstory.types.Metadata):
            Metadata field from the event.
        structured_fields (google.protobuf.struct_pb2.Struct):
            Structured fields extracted from the log.
        extracted (google.protobuf.struct_pb2.Struct):
            Flattened fields extracted from the log.
        ati_prioritization (google.backstory.types.AtiPrioritization):
            Prioritization factors used by ATI curated
            rules.
    """

    class EntityType(proto.Enum):
        r"""Describes the type of entity.
        An unknown event type.

        Values:
            UNKNOWN_ENTITYTYPE (0):
                @hide_from_doc
            ASSET (1):
                An asset, such as workstation, laptop, phone,
                virtual machine, etc.
            USER (10000):
                User.
            GROUP (10001):
                Group.
            RESOURCE (2):
                Resource.
            IP_ADDRESS (3):
                An external IP address.
            CIDR_BLOCK (9):
                A CIDR block.
            FILE (4):
                A file.
            DOMAIN_NAME (5):
                A domain.
            URL (6):
                A url.
            MUTEX (7):
                A mutex.
            METRIC (8):
                A metric.
        """

        UNKNOWN_ENTITYTYPE = 0
        ASSET = 1
        USER = 10000
        GROUP = 10001
        RESOURCE = 2
        IP_ADDRESS = 3
        CIDR_BLOCK = 9
        FILE = 4
        DOMAIN_NAME = 5
        URL = 6
        MUTEX = 7
        METRIC = 8

    class SourceType(proto.Enum):
        r"""Describes the source of an entity.

        Values:
            SOURCE_TYPE_UNSPECIFIED (0):
                Default source type
            ENTITY_CONTEXT (1):
                Entities ingested from customers (e.g. AD_CONTEXT,
                DLP_CONTEXT)
            DERIVED_CONTEXT (2):
                Entities derived from customer data such as
                prevalence, artifact first/last seen, or
                asset/user first seen stats.
            GLOBAL_CONTEXT (3):
                Global contextual entities such as WHOIS or
                Safe Browsing.
        """

        SOURCE_TYPE_UNSPECIFIED = 0
        ENTITY_CONTEXT = 1
        DERIVED_CONTEXT = 2
        GLOBAL_CONTEXT = 3

    product_entity_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    collected_timestamp: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    creation_timestamp: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    interval: interval_pb2.Interval = proto.Field(
        proto.MESSAGE,
        number=9,
        message=interval_pb2.Interval,
    )
    vendor_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    product_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    feed: str = proto.Field(
        proto.STRING,
        number=14,
    )
    product_version: str = proto.Field(
        proto.STRING,
        number=5,
    )
    entity_type: EntityType = proto.Field(
        proto.ENUM,
        number=6,
        enum=EntityType,
    )
    description: str = proto.Field(
        proto.STRING,
        number=7,
    )
    threat: MutableSequence[udm.SecurityResult] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message=udm.SecurityResult,
    )
    source_type: SourceType = proto.Field(
        proto.ENUM,
        number=11,
        enum=SourceType,
    )
    source_labels: MutableSequence[udm.Label] = proto.RepeatedField(
        proto.MESSAGE,
        number=12,
        message=udm.Label,
    )
    event_metadata: udm.Metadata = proto.Field(
        proto.MESSAGE,
        number=13,
        message=udm.Metadata,
    )
    structured_fields: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=15,
        message=struct_pb2.Struct,
    )
    extracted: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=16,
        message=struct_pb2.Struct,
    )
    ati_prioritization: "AtiPrioritization" = proto.Field(
        proto.MESSAGE,
        number=17,
        message="AtiPrioritization",
    )


class AtiPrioritization(proto.Message):
    r"""AtiPrioritization contains various fields used to calculate a
    priority score for an entity identified as a threat.

    Attributes:
        gti_verdict (int):
            The confidence score from "GTI verdict"
            source.
        gti_severity (int):
            The confidence score from "GTI severity"
            source.
        gti_threat_score (int):
            The confidence score from "GTI threat score"
            source.
        mandiant_analyst_confidence (int):
            The confidence score from "Mandiant Analyst
            Intel" source.
        gti_update_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp of the latest update for GTI
            verdict, severity, or threat score.
        active_ir (bool):
            Whether one or more Mandiant incident
            response customers had this indicator in their
            environment.
        active_ir_first_tagged_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp of the first time an active IR
            was applied to this entity.
        global_customer_count (int):
            Global customer count over the last 30 days
        global_hit_count (int):
            Global hit count over the last 30 days
        exclusive (bool):
            Whether the indicator is being used by a
            maximum of one threat actor.
        osint (bool):
            Whether the indicator details are available
            in open source.
        scanner (bool):
            Whether the indicator is a scanner.
        reviewed (bool):
            Whether the indicator verdict has passed
            review.
        attributed_malware (MutableSequence[google.backstory.types.SecurityResult.Association]):
            Malware families associated with this
            indicator.
        attributed_threat_actors (MutableSequence[google.backstory.types.SecurityResult.Association]):
            Threat actors associated with this indicator.
    """

    gti_verdict: int = proto.Field(
        proto.INT32,
        number=1,
    )
    gti_severity: int = proto.Field(
        proto.INT32,
        number=2,
    )
    gti_threat_score: int = proto.Field(
        proto.INT32,
        number=3,
    )
    mandiant_analyst_confidence: int = proto.Field(
        proto.INT32,
        number=4,
    )
    gti_update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    active_ir: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    active_ir_first_tagged_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    global_customer_count: int = proto.Field(
        proto.INT64,
        number=8,
    )
    global_hit_count: int = proto.Field(
        proto.INT64,
        number=9,
    )
    exclusive: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    osint: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    scanner: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    reviewed: bool = proto.Field(
        proto.BOOL,
        number=13,
    )
    attributed_malware: MutableSequence[udm.SecurityResult.Association] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=14,
            message=udm.SecurityResult.Association,
        )
    )
    attributed_threat_actors: MutableSequence[udm.SecurityResult.Association] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=15,
            message=udm.SecurityResult.Association,
        )
    )


class Entity(proto.Message):
    r"""An Entity provides additional context about an item in a UDM event.
    For example, a PROCESS_LAUNCH event describes that user
    'abc@example.corp' launched process 'shady.exe'. The event does not
    include information that user 'abc@example.com' is a recently
    terminated employee who administers a server storing finance data.
    Information stored in one or more Entities can add this additional
    context.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        metadata (google.backstory.types.EntityMetadata):
            Entity metadata such as timestamp, product,
            etc.
        entity (google.backstory.types.Noun):
            Noun in the UDM event that this entity
            represents.
        relations (MutableSequence[google.backstory.types.Relation]):
            One or more relationships between the entity
            (a) and other entities, including the
            relationship type and related entity.
        additional (google.protobuf.struct_pb2.Struct):
            Important entity data that cannot be
            adequately represented within the formal
            sections of the Entity.
        risk_score (google.backstory.types.EntityRisk):
            Stores information related to the entity's
            risk score.

            This field is a member of `oneof`_ ``_risk_score``.
        metric (google.backstory.types.Metric):
            Stores statistical metrics about the entity. Used if
            metadata.entity_type is METRIC.
    """

    metadata: "EntityMetadata" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="EntityMetadata",
    )
    entity: udm.Noun = proto.Field(
        proto.MESSAGE,
        number=2,
        message=udm.Noun,
    )
    relations: MutableSequence["Relation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="Relation",
    )
    additional: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=3,
        message=struct_pb2.Struct,
    )
    risk_score: entity_risk.EntityRisk = proto.Field(
        proto.MESSAGE,
        number=5,
        optional=True,
        message=entity_risk.EntityRisk,
    )
    metric: "Metric" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="Metric",
    )


class Relation(proto.Message):
    r"""Defines the relationship between the entity (a) and another
    entity (b).

    Attributes:
        entity (google.backstory.types.Noun):
            Entity (b) that the primary entity (a) is
            related to.
        entity_type (google.backstory.types.EntityMetadata.EntityType):
            Type of the related entity (b) in this
            relationship.
        relationship (google.backstory.types.Relation.Relationship):
            Type of relationship.
        direction (google.backstory.types.Relation.Directionality):
            Directionality of relationship between
            primary entity (a) and the related entity (b).
        uid (bytes):
            UID of the relationship.
        entity_label (google.backstory.types.Relation.EntityLabel):
            Label to identify the Noun of the relation.
    """

    class Relationship(proto.Enum):
        r"""Type of relationship between the primary entity (a) and
        related entity (b).

        Values:
            RELATIONSHIP_UNSPECIFIED (0):
                Default value
            OWNS (1):
                Related entity is owned by the primary entity
                (e.g. user owns device asset).
            ADMINISTERS (2):
                Related entity is administered by the primary
                entity (e.g. user administers a group).
            MEMBER (3):
                Primary entity is a member of the related
                entity (e.g. user is a member of a group).
            EXECUTES (4):
                Primary entity may have executed the related
                entity.
            DOWNLOADED_FROM (5):
                Primary entity may have been downloaded from
                the related entity.
            CONTACTS (6):
                Primary entity contacts the related entity.
        """

        RELATIONSHIP_UNSPECIFIED = 0
        OWNS = 1
        ADMINISTERS = 2
        MEMBER = 3
        EXECUTES = 4
        DOWNLOADED_FROM = 5
        CONTACTS = 6

    class Directionality(proto.Enum):
        r"""Describes the relationship model as directed or undirected.

        Values:
            DIRECTIONALITY_UNSPECIFIED (0):
                Default value.
            BIDIRECTIONAL (1):
                Modeled in both directions. Primary entity
                (a) to related entity (b) and related entity (b)
                to primary entity (a).
            UNIDIRECTIONAL (2):
                Modeled in a single direction. Primary entity
                (a) to related entity (b).
        """

        DIRECTIONALITY_UNSPECIFIED = 0
        BIDIRECTIONAL = 1
        UNIDIRECTIONAL = 2

    class EntityLabel(proto.Enum):
        r"""Entity label of the relation.

        Values:
            ENTITY_LABEL_UNSPECIFIED (0):
                Default value.
            PRINCIPAL (1):
                The Noun represents a principal type object.
            TARGET (2):
                The Noun represents a target type object.
            OBSERVER (3):
                The Noun represents an observer type object.
            SRC (4):
                The Noun represents src type object.
            NETWORK (5):
                The Noun represents a network type object.
            SECURITY_RESULT (6):
                The Noun represents a SecurityResult object.
            INTERMEDIARY (7):
                The Noun represents an intermediary type
                object.
        """

        ENTITY_LABEL_UNSPECIFIED = 0
        PRINCIPAL = 1
        TARGET = 2
        OBSERVER = 3
        SRC = 4
        NETWORK = 5
        SECURITY_RESULT = 6
        INTERMEDIARY = 7

    entity: udm.Noun = proto.Field(
        proto.MESSAGE,
        number=1,
        message=udm.Noun,
    )
    entity_type: "EntityMetadata.EntityType" = proto.Field(
        proto.ENUM,
        number=2,
        enum="EntityMetadata.EntityType",
    )
    relationship: Relationship = proto.Field(
        proto.ENUM,
        number=3,
        enum=Relationship,
    )
    direction: Directionality = proto.Field(
        proto.ENUM,
        number=4,
        enum=Directionality,
    )
    uid: bytes = proto.Field(
        proto.BYTES,
        number=5,
    )
    entity_label: EntityLabel = proto.Field(
        proto.ENUM,
        number=6,
        enum=EntityLabel,
    )


class Metric(proto.Message):
    r"""Stores precomputed aggregated analytic data for an entity.

    Attributes:
        first_seen (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp of the first time the entity was
            seen in the environment.
        last_seen (google.protobuf.timestamp_pb2.Timestamp):
            Time stamp of the last time last time the
            entity was seen in the environment.
        sum_measure (google.backstory.types.Metric.Measure):
            Sum of all precomputed measures for the given
            metric.
        total_events (int):
            Total number of events used to calculate the
            given precomputed metric.
        metric_name (google.backstory.types.Metric.MetricName):
            Name of the analytic.
        dimensions (MutableSequence[google.backstory.types.Metric.Dimension]):
            All group by clauses used to calculate the
            metric.
        export_window (int):
            Export window for which the metric was
            exported.
        display_name (str):
            Display name of the custom metric.
            Google-authored metrics do not have a display
            name.
        outcome_variables (MutableSequence[google.backstory.types.FindingVariable]):
            List of outcome variables used in the custom
            metric.
        match_variables (MutableSequence[google.backstory.types.FindingVariable]):
            List of match variables used in the custom
            metric.
        time_range (google.type.interval_pb2.Interval):
            Time range for which the custom metric was
            calculated.
    """

    class AggregateFunction(proto.Enum):
        r"""Mathematic function used to calculate the value.

        Values:
            AGGREGATE_FUNCTION_UNSPECIFIED (0):
                Default value.
            MIN (1):
                Minimum.
            MAX (2):
                Maximum.
            COUNT (3):
                Count.
            SUM (4):
                Sum.
            AVG (5):
                Average.
            STDDEV (6):
                Standard Deviation.
        """

        AGGREGATE_FUNCTION_UNSPECIFIED = 0
        MIN = 1
        MAX = 2
        COUNT = 3
        SUM = 4
        AVG = 5
        STDDEV = 6

    class MetricName(proto.Enum):
        r"""The name of the precomputed analytic.

        Values:
            METRIC_NAME_UNSPECIFIED (0):
                Default
            NETWORK_BYTES_INBOUND (1):
                Total received network bytes.
            NETWORK_BYTES_OUTBOUND (2):
                Total network sent bytes.
            NETWORK_BYTES_TOTAL (3):
                Total network sent bytes and received bytes.
            AUTH_ATTEMPTS_SUCCESS (4):
                Successful authentication attempts.
            AUTH_ATTEMPTS_FAIL (5):
                Failed authentication attempts.
            AUTH_ATTEMPTS_TOTAL (6):
                Total authentication attempts.
            DNS_BYTES_OUTBOUND (7):
                Total number of sent bytes for DNS events.
            NETWORK_FLOWS_INBOUND (8):
                Total number of events having non-null
                received bytes.
            NETWORK_FLOWS_OUTBOUND (9):
                Total number of events having non-null sent
                bytes.
            NETWORK_FLOWS_TOTAL (10):
                Total events having non-null sent or received
                bytes.
            DNS_QUERIES_SUCCESS (11):
                DNS query success count - Number of events with
                response_code = 0.
            DNS_QUERIES_FAIL (12):
                Number of events with response_code != 0.
            DNS_QUERIES_TOTAL (13):
                Total number of DNS queries made.
            FILE_EXECUTIONS_SUCCESS (14):
                Number of successfule file executions.
            FILE_EXECUTIONS_FAIL (15):
                Number of failed file executions.
            FILE_EXECUTIONS_TOTAL (16):
                Total number file executions.
            HTTP_QUERIES_SUCCESS (17):
                Number of successful HTTP queries.
            HTTP_QUERIES_FAIL (18):
                Number of failed HTTP queries.
            HTTP_QUERIES_TOTAL (19):
                Total number of HTTP queries.
            WORKSPACE_EMAILS_SENT_TOTAL (20):
                Total number of emails sent in Google
                Workspace.
            WORKSPACE_TOTAL_DOWNLOAD_ACTIONS (21):
                Total number of download actions in Google
                Workspace.
            WORKSPACE_TOTAL_CHANGE_ACTIONS (22):
                Total number of change actions in Google
                Workspace.
            WORKSPACE_AUTH_ATTEMPTS_TOTAL (23):
                Total number of authentication attempts in
                Google Workspace.
            WORKSPACE_NETWORK_BYTES_OUTBOUND (24):
                Number of outbound network bytes (total sent)
                in Google Workspace.
            WORKSPACE_NETWORK_BYTES_TOTAL (25):
                Total number of network bytes (both sent and
                received) in Google Workspace.
            ALERT_EVENT_NAME_COUNT (26):
                Track number of alerts fired by
                EDR/SENTINEL/MICROSOFT_GRAPH.
            RESOURCE_CREATION_TOTAL (27):
                Analytic tracking successful resource
                creations.
            RESOURCE_CREATION_SUCCESS (28):
                Analytic tracking successful resource
                creations.
            RESOURCE_READ_SUCCESS (29):
                Analytic tracking successful resource reads.
            RESOURCE_READ_FAIL (30):
                Analytic tracking failed resource reads.
            RESOURCE_DELETION_SUCCESS (31):
                Analytic tracking successful resource
                deletions.
            RESOURCE_CREATION_FAIL (32):
                Analytic tracking failed resource creations.
            RESOURCE_DELETION_FAIL (33):
                Analytic tracking failed resource deletions.
            RESOURCE_DELETION_TOTAL (34):
                Analytic tracking total resource deletions.
            RESOURCE_READ_TOTAL (35):
                Analytic tracking total resource reads.
            RESOURCE_WRITTEN_FAIL (36):
                Analytic tracking failed resource writes.
            RESOURCE_WRITTEN_SUCCESS (37):
                Analytic tracking successful resource writes.
            RESOURCE_WRITTEN_TOTAL (38):
                Analytic tracking total resource writes.
            UDM_DATA_PRESENCE_SUMMARY (39):
                UDM data summary tracking unique values of
                dimensions.
        """

        METRIC_NAME_UNSPECIFIED = 0
        NETWORK_BYTES_INBOUND = 1
        NETWORK_BYTES_OUTBOUND = 2
        NETWORK_BYTES_TOTAL = 3
        AUTH_ATTEMPTS_SUCCESS = 4
        AUTH_ATTEMPTS_FAIL = 5
        AUTH_ATTEMPTS_TOTAL = 6
        DNS_BYTES_OUTBOUND = 7
        NETWORK_FLOWS_INBOUND = 8
        NETWORK_FLOWS_OUTBOUND = 9
        NETWORK_FLOWS_TOTAL = 10
        DNS_QUERIES_SUCCESS = 11
        DNS_QUERIES_FAIL = 12
        DNS_QUERIES_TOTAL = 13
        FILE_EXECUTIONS_SUCCESS = 14
        FILE_EXECUTIONS_FAIL = 15
        FILE_EXECUTIONS_TOTAL = 16
        HTTP_QUERIES_SUCCESS = 17
        HTTP_QUERIES_FAIL = 18
        HTTP_QUERIES_TOTAL = 19
        WORKSPACE_EMAILS_SENT_TOTAL = 20
        WORKSPACE_TOTAL_DOWNLOAD_ACTIONS = 21
        WORKSPACE_TOTAL_CHANGE_ACTIONS = 22
        WORKSPACE_AUTH_ATTEMPTS_TOTAL = 23
        WORKSPACE_NETWORK_BYTES_OUTBOUND = 24
        WORKSPACE_NETWORK_BYTES_TOTAL = 25
        ALERT_EVENT_NAME_COUNT = 26
        RESOURCE_CREATION_TOTAL = 27
        RESOURCE_CREATION_SUCCESS = 28
        RESOURCE_READ_SUCCESS = 29
        RESOURCE_READ_FAIL = 30
        RESOURCE_DELETION_SUCCESS = 31
        RESOURCE_CREATION_FAIL = 32
        RESOURCE_DELETION_FAIL = 33
        RESOURCE_DELETION_TOTAL = 34
        RESOURCE_READ_TOTAL = 35
        RESOURCE_WRITTEN_FAIL = 36
        RESOURCE_WRITTEN_SUCCESS = 37
        RESOURCE_WRITTEN_TOTAL = 38
        UDM_DATA_PRESENCE_SUMMARY = 39

    class Dimension(proto.Enum):
        r"""Describes field used as the dimension when grouping data to
        calculate the aggregate metric.

        Values:
            DIMENSION_UNSPECIFIED (0):
                Default
            PRINCIPAL_DEVICE (1):
                Principal Device
            TARGET_USER (2):
                Target User
            TARGET_DEVICE (3):
                Target Device
            PRINCIPAL_USER (4):
                Principal User
            TARGET_IP (5):
                Target IP
            PRINCIPAL_FILE_HASH (6):
                Principal File Hash
            PRINCIPAL_COUNTRY (7):
                Principal Country
            SECURITY_CATEGORY (8):
                Security Category
            NETWORK_ASN (9):
                Network ASN
            CLIENT_CERTIFICATE_HASH (10):
                Client Certificate Hash
            DNS_QUERY_TYPE (11):
                DNS Query Type
            DNS_DOMAIN (12):
                DNS Domain
            HTTP_USER_AGENT (13):
                HTTP User Agent
            EVENT_TYPE (14):
                Event Type
            PRODUCT_NAME (15):
                Product Name
            PRODUCT_EVENT_TYPE (16):
                Product Event Type
            PARENT_FOLDER_PATH (17):
                Parent Folder Path
            TARGET_RESOURCE_NAME (18):
                Target resource Name
            PRINCIPAL_APPLICATION (19):
                Principal Application.
            TARGET_APPLICATION (20):
                Target Application.
            EMAIL_TO_ADDRESS (21):
                Email To Address.
            EMAIL_FROM_ADDRESS (22):
                Email From Address.
            MAIL_ID (23):
                Mail Id.
            PRINCIPAL_IP (24):
                Principal IP.
            SECURITY_ACTION (25):
                Security Action.
            SECURITY_RULE_ID (28):
                Security Rule Id.
            TARGET_NETWORK_ORGANIZATION_NAME (29):
                Target Network Organization name.
            PRINCIPAL_NETWORK_ORGANIZATION_NAME (30):
                Principal Network Organization name.
            PRINCIPAL_PROCESS_FILE_PATH (31):
                Principal Process File Path.
            PRINCIPAL_PROCESS_FILE_HASH (32):
                Principal Process File SHA256 Hash.
            SECURITY_RESULT_RULE_NAME (33):
                Security Result rule name.
            TARGET_RESOURCE_LABEL_KEY (34):
                Target Resource label key.
            VENDOR_NAME (35):
                Vendor name.
            TARGET_RESOURCE_TYPE (36):
                Target Resource type.
            TARGET_LOCATION_NAME (37):
                Target Location name.
            LOG_TYPE (38):
                Log type.
            TARGET_HOSTNAME (39):
                Target Hostname.
        """

        DIMENSION_UNSPECIFIED = 0
        PRINCIPAL_DEVICE = 1
        TARGET_USER = 2
        TARGET_DEVICE = 3
        PRINCIPAL_USER = 4
        TARGET_IP = 5
        PRINCIPAL_FILE_HASH = 6
        PRINCIPAL_COUNTRY = 7
        SECURITY_CATEGORY = 8
        NETWORK_ASN = 9
        CLIENT_CERTIFICATE_HASH = 10
        DNS_QUERY_TYPE = 11
        DNS_DOMAIN = 12
        HTTP_USER_AGENT = 13
        EVENT_TYPE = 14
        PRODUCT_NAME = 15
        PRODUCT_EVENT_TYPE = 16
        PARENT_FOLDER_PATH = 17
        TARGET_RESOURCE_NAME = 18
        PRINCIPAL_APPLICATION = 19
        TARGET_APPLICATION = 20
        EMAIL_TO_ADDRESS = 21
        EMAIL_FROM_ADDRESS = 22
        MAIL_ID = 23
        PRINCIPAL_IP = 24
        SECURITY_ACTION = 25
        SECURITY_RULE_ID = 28
        TARGET_NETWORK_ORGANIZATION_NAME = 29
        PRINCIPAL_NETWORK_ORGANIZATION_NAME = 30
        PRINCIPAL_PROCESS_FILE_PATH = 31
        PRINCIPAL_PROCESS_FILE_HASH = 32
        SECURITY_RESULT_RULE_NAME = 33
        TARGET_RESOURCE_LABEL_KEY = 34
        VENDOR_NAME = 35
        TARGET_RESOURCE_TYPE = 36
        TARGET_LOCATION_NAME = 37
        LOG_TYPE = 38
        TARGET_HOSTNAME = 39

    class Measure(proto.Message):
        r"""Describes the precomputed measure.

        Attributes:
            value (float):
                Value of the aggregated measure.
            aggregate_function (google.backstory.types.Metric.AggregateFunction):
                Function used to calculate the aggregated
                measure.
        """

        value: float = proto.Field(
            proto.DOUBLE,
            number=1,
        )
        aggregate_function: "Metric.AggregateFunction" = proto.Field(
            proto.ENUM,
            number=2,
            enum="Metric.AggregateFunction",
        )

    first_seen: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    last_seen: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    sum_measure: Measure = proto.Field(
        proto.MESSAGE,
        number=3,
        message=Measure,
    )
    total_events: int = proto.Field(
        proto.INT64,
        number=4,
    )
    metric_name: MetricName = proto.Field(
        proto.ENUM,
        number=5,
        enum=MetricName,
    )
    dimensions: MutableSequence[Dimension] = proto.RepeatedField(
        proto.ENUM,
        number=6,
        enum=Dimension,
    )
    export_window: int = proto.Field(
        proto.INT64,
        number=7,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=8,
    )
    outcome_variables: MutableSequence[udm.FindingVariable] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=udm.FindingVariable,
    )
    match_variables: MutableSequence[udm.FindingVariable] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message=udm.FindingVariable,
    )
    time_range: interval_pb2.Interval = proto.Field(
        proto.MESSAGE,
        number=11,
        message=interval_pb2.Interval,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
