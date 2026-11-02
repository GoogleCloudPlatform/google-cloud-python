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
import google.type.latlng_pb2 as latlng_pb2  # type: ignore
import proto  # type: ignore

from google.backstory.types import data_access
from google.backstory.types import entity_risk as gb_entity_risk
from google.backstory.types import id as gb_id

__protobuf__ = proto.module(
    package="google.backstory",
    manifest={
        "Verdict",
        "Reputation",
        "Status",
        "Priority",
        "Reason",
        "ThreatVerdict",
        "UDM",
        "Metadata",
        "Attribute",
        "Network",
        "ProxyInfo",
        "Extensions",
        "Authentication",
        "LinuxUtmp",
        "WindowsEventLog",
        "ResourceUsage",
        "SystemEventDetails",
        "OutlookMetadata",
        "Srum",
        "UserAssist",
        "Vulnerabilities",
        "Vulnerability",
        "Ftp",
        "Smtp",
        "Email",
        "Process",
        "AnalyticsMetadata",
        "FindingVariable",
        "SecurityResult",
        "PeFileMetadata",
        "FileMetadata",
        "File",
        "NtfsFileMetadata",
        "PrefetchFileMetadata",
        "UsnJournal",
        "AppCompatMetadata",
        "FileMetadataPE",
        "FileMetadataPeResourceInfo",
        "SignatureInfo",
        "FileMetadataSignatureInfo",
        "SignerInfo",
        "FileMetadataCodesign",
        "X509",
        "PDFInfo",
        "StringToInt64MapEntry",
        "FileMetadataSection",
        "FileMetadataImports",
        "ExifInfo",
        "Prevalence",
        "Dns",
        "Dhcp",
        "Certificate",
        "Tls",
        "Http",
        "Browser",
        "Hardware",
        "PlatformSoftware",
        "Software",
        "Asset",
        "User",
        "TimeOff",
        "Permission",
        "Role",
        "Group",
        "Registry",
        "WmiPersistenceItem",
        "Location",
        "ScheduledTask",
        "WindowsScheduledTask",
        "ScheduledCronTask",
        "ScheduledAnacronTask",
        "Volume",
        "Service",
        "Resource",
        "Label",
        "Cloud",
        "Artifact",
        "Tunnels",
        "ArtifactClient",
        "Favicon",
        "DNSRecord",
        "SSLCertificate",
        "PopularityRank",
        "Tracker",
        "Url",
        "Domain",
        "Noun",
        "Investigation",
        "Tags",
        "AttackDetails",
        "BoolSequence",
        "BytesSequence",
        "DoubleSequence",
        "Int64Sequence",
        "Uint64Sequence",
        "StringSequence",
        "GroupedFields",
    },
)


class Verdict(proto.Enum):
    r"""Categorization options for the validity of a finding (for
    example, whether it reflects an actual security incident).

    Values:
        VERDICT_UNSPECIFIED (0):
            An unspecified verdict.
        TRUE_POSITIVE (1):
            A categorization of the finding as a "true
            positive".
        FALSE_POSITIVE (2):
            A categorization of the finding as a "false
            positive".
    """

    VERDICT_UNSPECIFIED = 0
    TRUE_POSITIVE = 1
    FALSE_POSITIVE = 2


class Reputation(proto.Enum):
    r"""Categorization options for the usefulness of a finding.

    Values:
        REPUTATION_UNSPECIFIED (0):
            An unspecified reputation.
        USEFUL (1):
            A categorization of the finding as useful.
        NOT_USEFUL (2):
            A categorization of the finding as not
            useful.
    """

    REPUTATION_UNSPECIFIED = 0
    USEFUL = 1
    NOT_USEFUL = 2


class Status(proto.Enum):
    r"""Describes status of a finding.

    Values:
        STATUS_UNSPECIFIED (0):
            Unspecified finding status.
        NEW (1):
            New finding.
        REVIEWED (2):
            When a finding has feedback.
        CLOSED (3):
            When an analyst closes an finding.
        OPEN (4):
            Open. Used to indicate that a Case / Alert is
            open.
    """

    STATUS_UNSPECIFIED = 0
    NEW = 1
    REVIEWED = 2
    CLOSED = 3
    OPEN = 4


class Priority(proto.Enum):
    r"""Priority that is assigned to a Case or Alert.

    Values:
        PRIORITY_UNSPECIFIED (0):
            Default priority level.
        PRIORITY_INFO (100):
            Informational priority.
        PRIORITY_LOW (200):
            Low priority.
        PRIORITY_MEDIUM (300):
            Medium priority.
        PRIORITY_HIGH (400):
            High priority.
        PRIORITY_CRITICAL (500):
            Critical priority.
    """

    PRIORITY_UNSPECIFIED = 0
    PRIORITY_INFO = 100
    PRIORITY_LOW = 200
    PRIORITY_MEDIUM = 300
    PRIORITY_HIGH = 400
    PRIORITY_CRITICAL = 500


class Reason(proto.Enum):
    r"""Reason for closing an Alert or Case in the SOAR product.

    Values:
        REASON_UNSPECIFIED (0):
            Default reason.
        REASON_NOT_MALICIOUS (1):
            Case or Alert not malicious.
        REASON_MALICIOUS (2):
            Case or Alert is malicious.
        REASON_MAINTENANCE (3):
            Case or Alert is under maintenance.
    """

    REASON_UNSPECIFIED = 0
    REASON_NOT_MALICIOUS = 1
    REASON_MALICIOUS = 2
    REASON_MAINTENANCE = 3


class ThreatVerdict(proto.Enum):
    r"""GCTI threat verdict levels.

    Values:
        THREAT_VERDICT_UNSPECIFIED (0):
            Unspecified threat verdict level.
        UNDETECTED (1):
            Undetected threat verdict level.
        SUSPICIOUS (2):
            Suspicious threat verdict level.
        MALICIOUS (3):
            Malicious threat verdict level.
    """

    THREAT_VERDICT_UNSPECIFIED = 0
    UNDETECTED = 1
    SUSPICIOUS = 2
    MALICIOUS = 3


class UDM(proto.Message):
    r"""A Unified Data Model event.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        metadata (google.backstory.types.Metadata):
            Event metadata such as timestamp, source
            product, etc.
        additional (google.protobuf.struct_pb2.Struct):
            Any important vendor-specific event data that
            cannot be adequately represented within the
            formal sections of the UDM model.
        principal (google.backstory.types.Noun):
            Represents the acting entity that originates
            the activity described in the event. The
            principal must include at least one machine
            detail (hostname, MACs, IPs, port,
            product-specific identifiers like an EDR asset
            ID) or user detail (for example, username), and
            optionally include process details. It must NOT
            include any of the following fields:

            email, files, registry keys or values.
        src (google.backstory.types.Noun):
            Represents a source entity being acted upon
            by the participant along with the device or
            process context for the source object (the
            machine where the source object resides). For
            example, if user U copies file A on machine X to
            file B on machine Y, both file A and machine X
            would be specified in the src portion of the UDM
            event.
        target (google.backstory.types.Noun):
            Represents a target entity being referenced
            by the event or an object on the target entity.
            For example, in a firewall connection from
            device A to device B, A is described as the
            principal and B is described as the target. For
            a process injection by process C into target
            process D, process C is described as the
            principal and process D is described as the
            target.
        intermediary (MutableSequence[google.backstory.types.Noun]):
            Represents details on one or more
            intermediate entities processing activity
            described in the event. This includes device
            details about a proxy server or SMTP relay
            server. If an active event (that has a principal
            and possibly target) passes through any
            intermediaries, they're added here.
            Intermediaries can impact the overall action,
            for example blocking or modifying an ongoing
            request.  A rule of thumb here is that
            'principal', 'target', and description of the
            initial action should be the same regardless of
            the intermediary or its action.  A successful
            network connection from A->B should look the
            same in principal/target/intermediary as one
            blocked by firewall C: principal: A, target: B
            (intermediary: C).
        observer (google.backstory.types.Noun):
            Represents an observer entity (for example, a
            packet sniffer or network-based vulnerability
            scanner), which is not a direct intermediary,
            but which observes and reports on the event in
            question.
        about (MutableSequence[google.backstory.types.Noun]):
            Represents entities referenced by the event that are not
            otherwise described in principal, src, target, intermediary
            or observer. For example, it could be used to track email
            file attachments, domains/URLs/IPs embedded within an email
            body, and DLLs that are loaded during a PROCESS_LAUNCH
            event.
        security_result (MutableSequence[google.backstory.types.SecurityResult]):
            A list of security results.
        network (google.backstory.types.Network):
            All network details go here, including
            sub-messages with details on each protocol (for
            example, DHCP, DNS, or HTTP).
        extensions (google.backstory.types.Extensions):
            All other first-class, event-specific
            metadata goes in this message. Do not place
            protocol metadata in Extensions; put it in
            Network.
        extracted (google.protobuf.struct_pb2.Struct):
            Flattened fields extracted from the log.
        grouped (google.backstory.types.GroupedFields):
            Related UDM fields that are grouped together.

            This field is a member of `oneof`_ ``_grouped``.
    """

    metadata: "Metadata" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Metadata",
    )
    additional: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Struct,
    )
    principal: "Noun" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Noun",
    )
    src: "Noun" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="Noun",
    )
    target: "Noun" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="Noun",
    )
    intermediary: MutableSequence["Noun"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="Noun",
    )
    observer: "Noun" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="Noun",
    )
    about: MutableSequence["Noun"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="Noun",
    )
    security_result: MutableSequence["SecurityResult"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="SecurityResult",
    )
    network: "Network" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="Network",
    )
    extensions: "Extensions" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="Extensions",
    )
    extracted: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=12,
        message=struct_pb2.Struct,
    )
    grouped: "GroupedFields" = proto.Field(
        proto.MESSAGE,
        number=13,
        optional=True,
        message="GroupedFields",
    )


class Metadata(proto.Message):
    r"""General information associated with a UDM event.

    Attributes:
        id (bytes):
            ID of the UDM event. Can be used for raw and
            normalized event retrieval.
        product_log_id (str):
            A vendor-specific event identifier to
            uniquely identify the event (e.g. a GUID).
        event_timestamp (google.protobuf.timestamp_pb2.Timestamp):
            The GMT timestamp when the event was
            generated.
        event_timestamp_attributes (MutableSequence[google.backstory.types.Metadata.EventTimestampAttribute]):
            Attributes associated with event_timestamp. This field is
            used to distinguish between different types of timestamps
            that can be used to represent the event_timestamp.
        collected_timestamp (google.protobuf.timestamp_pb2.Timestamp):
            The GMT timestamp when the event was
            collected by the vendor's local collection
            infrastructure.
        ingested_timestamp (google.protobuf.timestamp_pb2.Timestamp):
            The GMT timestamp when the event was ingested
            (received) by Chronicle.
        event_type (google.backstory.types.Metadata.EventType):
            The event type.
            If an event has multiple possible types, this
            specifies the most specific type.
        vendor_name (str):
            The name of the product vendor.
        product_name (str):
            The name of the product.
        product_version (str):
            The version of the product.
        product_event_type (str):
            A short, descriptive, human-readable, product-specific event
            name or type (e.g. "Scanned X", "User account created",
            "process_start").
        product_deployment_id (str):
            The deployment identifier assigned by the
            vendor for a product deployment.
        description (str):
            A human-readable unparsable description of
            the event.
        url_back_to_product (str):
            A URL that takes the user to the source
            product console for this event.
        ingestion_labels (MutableSequence[google.backstory.types.Label]):
            User-configured ingestion metadata labels.
        tags (google.backstory.types.Tags):
            Tags added by Chronicle after an event is
            parsed. It is an error to populate this field
            from within a parser.
        enrichment_state (google.backstory.types.Metadata.EnrichmentState):
            The enrichment state.
        log_type (str):
            The string value of log type.
        base_labels (google.backstory.types.DataAccessLabels):
            Data access labels on the base event.
        enrichment_labels (google.backstory.types.DataAccessLabels):
            Data access labels from all the contextual
            events used to enrich the base event.
        structured_fields (google.protobuf.struct_pb2.Struct):
            Flattened fields extracted from the log.
        parser_version (str):
            The version of the parser that generated this
            UDM event.
    """

    class EventTimestampAttribute(proto.Enum):
        r"""Enum representing the type of timestamp that the event_timestamp
        field represents.

        Values:
            EVENT_TIMESTAMP_ATTRIBUTE_UNSPECIFIED (0):
                Default event timestamp attribute.
            FILE_LAST_ACCESS_TIME (1):
                Deprecated. Use LAST_ACCESSED instead.
            FILE_LAST_MODIFIED_TIME (2):
                Deprecated. Use LAST_MODIFIED instead.
            FILE_METADATA_LAST_CHANGE_TIME (3):
                Deprecated. Use METADATA_LAST_CHANGED instead.
            FILE_CREATION_TIME (4):
                Deprecated. Use CREATED instead.
            COLLECTED_TIME (5):
                Deprecated. Use COLLECTED instead.
            COLLECTED (6):
                The time when the event was collected by the
                vendor's local collection infrastructure.
            ACCESSED (7):
                The time when the file was accessed.
            CHANGED (8):
                The time when the file was changed.
            CREATED (9):
                The time when the file was first created.
            FILE_NAME_ACCESSED (10):
                The time when the file name was accessed.
            FILE_NAME_CHANGED (11):
                The time when the file name was changed.
            FILE_NAME_CREATED (12):
                The time when the file name was created.
            FILE_NAME_LAST_ACCESSED (13):
                The time when the file name was last
                accessed.
            FILE_NAME_LAST_MODIFIED (14):
                The time when the file name was last
                modified.
            FILE_NAME_METADATA_LAST_CHANGED (15):
                The time when the file name metadata was last
                changed.
            FILE_NAME_MODIFIED (16):
                The time when the file name was modified.
            LAST_ACCESSED (17):
                The time when the file was last accessed.
            LAST_MODIFIED (18):
                The time when the file was last modified.
            METADATA_LAST_CHANGED (19):
                The time when the file metadata was last
                changed.
            MODIFIED (20):
                The time when the file was modified.
            ADDED (21):
                Added Timestamp.
            BACKED_UP (22):
                Backed Up Timestamp.
            LAST_CONNECTED (23):
                Last Connected timestamp.
            DELETED (24):
                Deleted Timestamp.
            ENDED (25):
                Ended Timestamp.
            EXITED (26):
                Exited Timestamp.
            EXPIRED (27):
                Expired Timestamp.
            FIRST_ACCESSED (28):
                First Accessed Timestamp.
            APPEARED (29):
                Appeared Timestamp.
            INSTALLED (30):
                Installed Timestamp.
            LAST_ACTIVE (31):
                Last Active Timestamp.
            LAST_LOGGED_IN (32):
                Last Login Timestamp.
            LAST_LOGIN_ATTEMPT (33):
                Last Login Attempt Timestamp.
            LAST_PASSWORD_SET (34):
                Last Password Set Timestamp.
            LAST_PRINTED (35):
                Last Printed Timestamp.
            LAST_RESUMED (36):
                Last Resumed Timestamp.
            LAST_EXECUTED (37):
                Last Executed Timestamp.
            LAST_SEEN (38):
                Last Seen Timestamp.
            LAST_SHUTDOWN (39):
                Last Shutdown Timestamp.
            LAST_UPDATED (40):
                Last Updated Timestamp.
            LAST_USED (41):
                Last Used Timestamp.
            LAST_VISITED (42):
                Last Visited Timestamp.
            LINKED (43):
                Linked Timestamp.
            METADATA_MODIFIED (44):
                Metadata Modified Timestamp.
            CONTENT_MODIFIED (45):
                Modified Timestamp.
            PURCHASED (46):
                Purchased Timestamp.
            RECORDED (47):
                Recorded Timestamp.
            REQUEST_RECEIVED (48):
                Request Received Timestamp.
            RESPONSE_SENT (49):
                Response Sent Timestamp.
            SCHEDULED_TO_END (50):
                Scheduled to End Timestamp.
            SCHEDULED_TO_START (51):
                Scheduled to Start Timestamp.
            SENT (52):
                Sent Timestamp.
            STARTED (53):
                Started Timestamp.
            UPDATED (54):
                Updated Timestamp.
            VALIDATED (55):
                Validated Timestamp.
            MOST_RECENT_RUN (56):
                Most Recent Run Timestamp.
            NEXT_RUN (57):
                Next Run Timestamp.
            VISITED (58):
                Visited Timestamp.
            TARGET_CREATED (59):
                Target Created Timestamp.
            VOLUME_CREATED (60):
                Volume Created Timestamp.
            POST_CHECKED (61):
                Post Checked Timestamp.
            SYNCHRONIZED (62):
                Synchronized Timestamp.
            ITEM_CREATED (63):
                Item Created Timestamp.
            ITEM_MODIFIED (64):
                Item Modified Timestamp.
            DOCUMENT_LAST_SAVED (65):
                Document Last Saved Timestamp.
            LAST_REGISTERED (66):
                Last Registered Timestamp.
            LAUNCHED (67):
                Launched Timestamp.
            FIRST_VISITED (68):
                First Visited Timestamp.
            FIRST_SEEN (69):
                First Seen Timestamp.
            DOWNLOADED (70):
                Downloaded Timestamp.
        """

        EVENT_TIMESTAMP_ATTRIBUTE_UNSPECIFIED = 0
        FILE_LAST_ACCESS_TIME = 1
        FILE_LAST_MODIFIED_TIME = 2
        FILE_METADATA_LAST_CHANGE_TIME = 3
        FILE_CREATION_TIME = 4
        COLLECTED_TIME = 5
        COLLECTED = 6
        ACCESSED = 7
        CHANGED = 8
        CREATED = 9
        FILE_NAME_ACCESSED = 10
        FILE_NAME_CHANGED = 11
        FILE_NAME_CREATED = 12
        FILE_NAME_LAST_ACCESSED = 13
        FILE_NAME_LAST_MODIFIED = 14
        FILE_NAME_METADATA_LAST_CHANGED = 15
        FILE_NAME_MODIFIED = 16
        LAST_ACCESSED = 17
        LAST_MODIFIED = 18
        METADATA_LAST_CHANGED = 19
        MODIFIED = 20
        ADDED = 21
        BACKED_UP = 22
        LAST_CONNECTED = 23
        DELETED = 24
        ENDED = 25
        EXITED = 26
        EXPIRED = 27
        FIRST_ACCESSED = 28
        APPEARED = 29
        INSTALLED = 30
        LAST_ACTIVE = 31
        LAST_LOGGED_IN = 32
        LAST_LOGIN_ATTEMPT = 33
        LAST_PASSWORD_SET = 34
        LAST_PRINTED = 35
        LAST_RESUMED = 36
        LAST_EXECUTED = 37
        LAST_SEEN = 38
        LAST_SHUTDOWN = 39
        LAST_UPDATED = 40
        LAST_USED = 41
        LAST_VISITED = 42
        LINKED = 43
        METADATA_MODIFIED = 44
        CONTENT_MODIFIED = 45
        PURCHASED = 46
        RECORDED = 47
        REQUEST_RECEIVED = 48
        RESPONSE_SENT = 49
        SCHEDULED_TO_END = 50
        SCHEDULED_TO_START = 51
        SENT = 52
        STARTED = 53
        UPDATED = 54
        VALIDATED = 55
        MOST_RECENT_RUN = 56
        NEXT_RUN = 57
        VISITED = 58
        TARGET_CREATED = 59
        VOLUME_CREATED = 60
        POST_CHECKED = 61
        SYNCHRONIZED = 62
        ITEM_CREATED = 63
        ITEM_MODIFIED = 64
        DOCUMENT_LAST_SAVED = 65
        LAST_REGISTERED = 66
        LAUNCHED = 67
        FIRST_VISITED = 68
        FIRST_SEEN = 69
        DOWNLOADED = 70

    class EventType(proto.Enum):
        r"""An event type. Choose event type not based on the product that
        generated the event but the one that logged the event itself. So,
        for example, an antivirus (AV) scanning email on a client would
        generate an SMTP_PROXY event, not an AV event. A DLP device scanning
        a web upload would generate an HTTP_PROXY event and not a DLP or
        process activity event. Note: In the case of a HTTP_PROXY event, you
        might also include process details if this occurred on an endpoint.
        That would be optional, but there are a certain set of required
        fields and banned fields due to its status as an HTTP_PROXY event.

        Values:
            EVENTTYPE_UNSPECIFIED (0):
                Default event type
            PROCESS_UNCATEGORIZED (10000):
                Activity related to a process which does not
                match any other event types.
            PROCESS_LAUNCH (10001):
                Process launch.
            PROCESS_INJECTION (10002):
                Process injecting into another process.
            PROCESS_PRIVILEGE_ESCALATION (10003):
                Process privilege escalation.
            PROCESS_TERMINATION (10004):
                Process termination.
            PROCESS_OPEN (10005):
                Process being opened.
            PROCESS_MODULE_LOAD (10006):
                Process loading a module.
            REGISTRY_UNCATEGORIZED (11000):
                Registry event which does not match any of
                the other event types.
            REGISTRY_CREATION (11001):
                Registry creation.
            REGISTRY_MODIFICATION (11002):
                Registry modification.
            REGISTRY_DELETION (11003):
                Registry deletion.
            SETTING_UNCATEGORIZED (12000):
                Settings-related event which does not match
                any of the other event types.
            SETTING_CREATION (12001):
                Setting creation.
            SETTING_MODIFICATION (12002):
                Setting modification.
            SETTING_DELETION (12003):
                Setting deletion.
            MUTEX_UNCATEGORIZED (13000):
                Any mutex event other than creation.
            MUTEX_CREATION (13001):
                Mutex creation.
            FILE_UNCATEGORIZED (14000):
                File event which does not match any of the
                other event types.
            FILE_CREATION (14001):
                File created.
            FILE_DELETION (14002):
                File deleted.
            FILE_MODIFICATION (14003):
                File modified.
            FILE_READ (14004):
                File read.
            FILE_COPY (14005):
                File copied.
                Used for file copies, for example, to a thumb
                drive.
            FILE_OPEN (14006):
                File opened.
            FILE_MOVE (14007):
                File moved or renamed.
            FILE_SYNC (14008):
                File synced (for example, Google Drive,
                Dropbox, backup).
            USER_UNCATEGORIZED (15000):
                User activity which does not match any of the
                other event types.
            USER_LOGIN (15001):
                User login.
            USER_LOGOUT (15002):
                User logout.
            USER_CREATION (15003):
                User creation.
            USER_CHANGE_PASSWORD (15004):
                User password change event.
            USER_CHANGE_PERMISSIONS (15005):
                Change in user permissions.
            USER_STATS (15006):
                Deprecated. Used to update user info for an
                LDAP dump.
            USER_BADGE_IN (15007):
                User physically badging into a location.
            USER_DELETION (15008):
                User deletion.
            USER_RESOURCE_CREATION (15009):
                User creating a virtual resource. This is equivalent to
                RESOURCE_CREATION.
            USER_RESOURCE_UPDATE_CONTENT (15010):
                User updating content of a virtual resource. This is
                equivalent to RESOURCE_WRITTEN.
            USER_RESOURCE_UPDATE_PERMISSIONS (15011):
                User updating permissions of a virtual resource. This is
                equivalent to RESOURCE_PERMISSIONS_CHANGE.
            USER_COMMUNICATION (15012):
                User initiating communication through a
                medium (for example, video).
            USER_RESOURCE_ACCESS (15013):
                User accessing a virtual resource. This is equivalent to
                RESOURCE_READ.
            USER_RESOURCE_DELETION (15014):
                User deleting a virtual resource. This is equivalent to
                RESOURCE_DELETION.
            GROUP_UNCATEGORIZED (23000):
                A group activity that does not fall into one
                of the other event types.
            GROUP_CREATION (23001):
                A group creation.
            GROUP_DELETION (23002):
                A group deletion.
            GROUP_MODIFICATION (23003):
                A group modification.
            EMAIL_UNCATEGORIZED (19000):
                Email messages
            EMAIL_TRANSACTION (19001):
                An email transaction.
            EMAIL_URL_CLICK (19002):
                Deprecated: use NETWORK_HTTP instead. An email URL click
                event.
            NETWORK_UNCATEGORIZED (16000):
                A network event that does not fit into one of
                the other event types.
            NETWORK_FLOW (16001):
                Aggregated flow stats like netflow.
            NETWORK_CONNECTION (16002):
                Network connection details like from a FW.
            NETWORK_FTP (16003):
                FTP telemetry.
            NETWORK_DHCP (16004):
                DHCP payload.
            NETWORK_DNS (16005):
                DNS payload.
            NETWORK_HTTP (16006):
                HTTP telemetry.
            NETWORK_SMTP (16007):
                SMTP telemetry.
            STATUS_UNCATEGORIZED (17000):
                A status message that does not fit into one
                of the other event types.
            STATUS_HEARTBEAT (17001):
                Heartbeat indicating product is alive.
            STATUS_STARTUP (17002):
                An agent startup.
            STATUS_SHUTDOWN (17003):
                An agent shutdown.
            STATUS_UPDATE (17004):
                A software or fingerprint update.
            SCAN_UNCATEGORIZED (18000):
                Scan item that does not fit into one of the
                other event types.
            SCAN_FILE (18001):
                A file scan.
            SCAN_PROCESS_BEHAVIORS (18002):
                Scan process behaviors. Please use SCAN_PROCESS instead.
            SCAN_PROCESS (18003):
                Scan process.
            SCAN_HOST (18004):
                Scan results from scanning an entire host
                device for threats/sensitive documents.
            SCAN_VULN_HOST (18005):
                Vulnerability scan logs about host
                vulnerabilities (e.g., out of date software) and
                network vulnerabilities (e.g., unprotected
                service detected via a network scan).
            SCAN_VULN_NETWORK (18006):
                Vulnerability scan logs about network
                vulnerabilities.
            SCAN_NETWORK (18007):
                Scan network for suspicious activity
            SCHEDULED_TASK_UNCATEGORIZED (20000):
                Scheduled task event that does not fall into
                one of the other event types.
            SCHEDULED_TASK_CREATION (20001):
                Scheduled task creation.
            SCHEDULED_TASK_DELETION (20002):
                Scheduled task deletion.
            SCHEDULED_TASK_ENABLE (20003):
                Scheduled task being enabled.
            SCHEDULED_TASK_DISABLE (20004):
                Scheduled task being disabled.
            SCHEDULED_TASK_MODIFICATION (20005):
                Scheduled task being modified.
            SYSTEM_AUDIT_LOG_UNCATEGORIZED (21000):
                A system audit log event that is not a wipe.
            SYSTEM_AUDIT_LOG_WIPE (21001):
                A system audit log wipe.
            SERVICE_UNSPECIFIED (22000):
                Service event that does not fit into one of
                the other event types.
            SERVICE_CREATION (22001):
                A service creation.
            SERVICE_DELETION (22002):
                A service deletion.
            SERVICE_START (22003):
                A service start.
            SERVICE_STOP (22004):
                A service stop.
            SERVICE_MODIFICATION (22005):
                A service modification.
            GENERIC_EVENT (100000):
                Operating system events that are not
                described by any of the other event types. Might
                include uncategorized Microsoft Windows event
                logs.
            RESOURCE_CREATION (1):
                The resource was created/provisioned. This is equivalent to
                USER_RESOURCE_CREATION.
            RESOURCE_DELETION (2):
                The resource was deleted/deprovisioned. This is equivalent
                to USER_RESOURCE_DELETION.
            RESOURCE_PERMISSIONS_CHANGE (3):
                The resource had it's permissions or ACLs updated. This is
                equivalent to USER_RESOURCE_UPDATE_PERMISSIONS.
            RESOURCE_READ (4):
                The resource was read. This is equivalent to
                USER_RESOURCE_ACCESS.
            RESOURCE_WRITTEN (5):
                The resource was written to. This is equivalent to
                USER_RESOURCE_UPDATE_CONTENT.
            DEVICE_FIRMWARE_UPDATE (25000):
                Firmware update.
            DEVICE_CONFIG_UPDATE (25001):
                Configuration update.
            DEVICE_PROGRAM_UPLOAD (25002):
                A program or application uploaded to a
                device.
            DEVICE_PROGRAM_DOWNLOAD (25003):
                A program or application downloaded to a
                device.
            ANALYST_UPDATE_VERDICT (24000):
                Analyst update about the Verdict (such as
                true positive, false positive, or disregard) of
                a finding.
            ANALYST_UPDATE_REPUTATION (24001):
                Analyst update about the Reputation (such as
                useful or not useful) of a finding.
            ANALYST_UPDATE_SEVERITY_SCORE (24002):
                Analyst update about the Severity score
                (0-100) of a finding.
            ANALYST_UPDATE_STATUS (24007):
                Analyst update about the finding status.
            ANALYST_ADD_COMMENT (24008):
                Analyst addition of a comment for a finding.
            ANALYST_UPDATE_PRIORITY (24009):
                Analyst update about the priority (such as
                low, medium, or high) for a finding.
            ANALYST_UPDATE_ROOT_CAUSE (24010):
                Analyst update about the root cause for a
                finding.
            ANALYST_UPDATE_REASON (24011):
                Analyst update about the reason (such as
                malicious or not malicious) for a finding.
            ANALYST_UPDATE_RISK_SCORE (24012):
                Analyst update about the risk score (0-100)
                of a finding.
            ENTITY_RISK_CHANGE (26000):
                An update to an entity risk score. This event
                type is restricted to events published by Google
                Securit Operations Risk Analytics.
            TRIAGE_AGENT_UPDATE_INVESTIGATION (27000):
                Triage Agent has investigated the finding.
        """

        EVENTTYPE_UNSPECIFIED = 0
        PROCESS_UNCATEGORIZED = 10000
        PROCESS_LAUNCH = 10001
        PROCESS_INJECTION = 10002
        PROCESS_PRIVILEGE_ESCALATION = 10003
        PROCESS_TERMINATION = 10004
        PROCESS_OPEN = 10005
        PROCESS_MODULE_LOAD = 10006
        REGISTRY_UNCATEGORIZED = 11000
        REGISTRY_CREATION = 11001
        REGISTRY_MODIFICATION = 11002
        REGISTRY_DELETION = 11003
        SETTING_UNCATEGORIZED = 12000
        SETTING_CREATION = 12001
        SETTING_MODIFICATION = 12002
        SETTING_DELETION = 12003
        MUTEX_UNCATEGORIZED = 13000
        MUTEX_CREATION = 13001
        FILE_UNCATEGORIZED = 14000
        FILE_CREATION = 14001
        FILE_DELETION = 14002
        FILE_MODIFICATION = 14003
        FILE_READ = 14004
        FILE_COPY = 14005
        FILE_OPEN = 14006
        FILE_MOVE = 14007
        FILE_SYNC = 14008
        USER_UNCATEGORIZED = 15000
        USER_LOGIN = 15001
        USER_LOGOUT = 15002
        USER_CREATION = 15003
        USER_CHANGE_PASSWORD = 15004
        USER_CHANGE_PERMISSIONS = 15005
        USER_STATS = 15006
        USER_BADGE_IN = 15007
        USER_DELETION = 15008
        USER_RESOURCE_CREATION = 15009
        USER_RESOURCE_UPDATE_CONTENT = 15010
        USER_RESOURCE_UPDATE_PERMISSIONS = 15011
        USER_COMMUNICATION = 15012
        USER_RESOURCE_ACCESS = 15013
        USER_RESOURCE_DELETION = 15014
        GROUP_UNCATEGORIZED = 23000
        GROUP_CREATION = 23001
        GROUP_DELETION = 23002
        GROUP_MODIFICATION = 23003
        EMAIL_UNCATEGORIZED = 19000
        EMAIL_TRANSACTION = 19001
        EMAIL_URL_CLICK = 19002
        NETWORK_UNCATEGORIZED = 16000
        NETWORK_FLOW = 16001
        NETWORK_CONNECTION = 16002
        NETWORK_FTP = 16003
        NETWORK_DHCP = 16004
        NETWORK_DNS = 16005
        NETWORK_HTTP = 16006
        NETWORK_SMTP = 16007
        STATUS_UNCATEGORIZED = 17000
        STATUS_HEARTBEAT = 17001
        STATUS_STARTUP = 17002
        STATUS_SHUTDOWN = 17003
        STATUS_UPDATE = 17004
        SCAN_UNCATEGORIZED = 18000
        SCAN_FILE = 18001
        SCAN_PROCESS_BEHAVIORS = 18002
        SCAN_PROCESS = 18003
        SCAN_HOST = 18004
        SCAN_VULN_HOST = 18005
        SCAN_VULN_NETWORK = 18006
        SCAN_NETWORK = 18007
        SCHEDULED_TASK_UNCATEGORIZED = 20000
        SCHEDULED_TASK_CREATION = 20001
        SCHEDULED_TASK_DELETION = 20002
        SCHEDULED_TASK_ENABLE = 20003
        SCHEDULED_TASK_DISABLE = 20004
        SCHEDULED_TASK_MODIFICATION = 20005
        SYSTEM_AUDIT_LOG_UNCATEGORIZED = 21000
        SYSTEM_AUDIT_LOG_WIPE = 21001
        SERVICE_UNSPECIFIED = 22000
        SERVICE_CREATION = 22001
        SERVICE_DELETION = 22002
        SERVICE_START = 22003
        SERVICE_STOP = 22004
        SERVICE_MODIFICATION = 22005
        GENERIC_EVENT = 100000
        RESOURCE_CREATION = 1
        RESOURCE_DELETION = 2
        RESOURCE_PERMISSIONS_CHANGE = 3
        RESOURCE_READ = 4
        RESOURCE_WRITTEN = 5
        DEVICE_FIRMWARE_UPDATE = 25000
        DEVICE_CONFIG_UPDATE = 25001
        DEVICE_PROGRAM_UPLOAD = 25002
        DEVICE_PROGRAM_DOWNLOAD = 25003
        ANALYST_UPDATE_VERDICT = 24000
        ANALYST_UPDATE_REPUTATION = 24001
        ANALYST_UPDATE_SEVERITY_SCORE = 24002
        ANALYST_UPDATE_STATUS = 24007
        ANALYST_ADD_COMMENT = 24008
        ANALYST_UPDATE_PRIORITY = 24009
        ANALYST_UPDATE_ROOT_CAUSE = 24010
        ANALYST_UPDATE_REASON = 24011
        ANALYST_UPDATE_RISK_SCORE = 24012
        ENTITY_RISK_CHANGE = 26000
        TRIAGE_AGENT_UPDATE_INVESTIGATION = 27000

    class EnrichmentState(proto.Enum):
        r"""An enrichment state.

        Values:
            ENRICHMENT_STATE_UNSPECIFIED (0):
                Unspecified.
            ENRICHED (1):
                The event has been enriched by Chronicle.
            UNENRICHED (2):
                The event has not been enriched by Chronicle.
        """

        ENRICHMENT_STATE_UNSPECIFIED = 0
        ENRICHED = 1
        UNENRICHED = 2

    id: bytes = proto.Field(
        proto.BYTES,
        number=15,
    )
    product_log_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    event_timestamp: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    event_timestamp_attributes: MutableSequence[EventTimestampAttribute] = (
        proto.RepeatedField(
            proto.ENUM,
            number=21,
            enum=EventTimestampAttribute,
        )
    )
    collected_timestamp: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    ingested_timestamp: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    event_type: EventType = proto.Field(
        proto.ENUM,
        number=4,
        enum=EventType,
    )
    vendor_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    product_name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    product_version: str = proto.Field(
        proto.STRING,
        number=7,
    )
    product_event_type: str = proto.Field(
        proto.STRING,
        number=8,
    )
    product_deployment_id: str = proto.Field(
        proto.STRING,
        number=14,
    )
    description: str = proto.Field(
        proto.STRING,
        number=9,
    )
    url_back_to_product: str = proto.Field(
        proto.STRING,
        number=10,
    )
    ingestion_labels: MutableSequence["Label"] = proto.RepeatedField(
        proto.MESSAGE,
        number=12,
        message="Label",
    )
    tags: "Tags" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="Tags",
    )
    enrichment_state: EnrichmentState = proto.Field(
        proto.ENUM,
        number=16,
        enum=EnrichmentState,
    )
    log_type: str = proto.Field(
        proto.STRING,
        number=17,
    )
    base_labels: data_access.DataAccessLabels = proto.Field(
        proto.MESSAGE,
        number=18,
        message=data_access.DataAccessLabels,
    )
    enrichment_labels: data_access.DataAccessLabels = proto.Field(
        proto.MESSAGE,
        number=19,
        message=data_access.DataAccessLabels,
    )
    structured_fields: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=20,
        message=struct_pb2.Struct,
    )
    parser_version: str = proto.Field(
        proto.STRING,
        number=22,
    )


class Attribute(proto.Message):
    r"""Attribute is a container for generic entity attributes
    including common attributes across core entities (such as, user
    or asset). For example, Cloud is a generic entity attribute
    since it can apply to an asset (for example, a VM) or a user
    (for example, an identity service account).

    Attributes:
        cloud (google.backstory.types.Cloud):
            Cloud metadata attributes such as project ID,
            account ID, or organizational hierarchy.
        labels (MutableSequence[google.backstory.types.Label]):
            Set of labels for the entity. Should only be
            used for product labels (for example, Google
            Cloud resource labels or Azure AD sensitivity
            labels. Should not be used for arbitrary
            key-value mappings.
        permissions (MutableSequence[google.backstory.types.Permission]):
            System permissions for IAM entity
            (human principal, service account, group).
        roles (MutableSequence[google.backstory.types.Role]):
            System IAM roles to be assumed by resources
            to use the role's permissions for access
            control.
        creation_time (google.protobuf.timestamp_pb2.Timestamp):
            Time the resource or entity was created or
            provisioned.
        last_update_time (google.protobuf.timestamp_pb2.Timestamp):
            Time the resource or entity was last updated.
    """

    cloud: "Cloud" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Cloud",
    )
    labels: MutableSequence["Label"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Label",
    )
    permissions: MutableSequence["Permission"] = proto.RepeatedField(
        proto.MESSAGE,
        number=705,
        message="Permission",
    )
    roles: MutableSequence["Role"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="Role",
    )
    creation_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    last_update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )


class Network(proto.Message):
    r"""A network event.

    Attributes:
        sent_bytes (int):
            The number of bytes sent.
        received_bytes (int):
            The number of bytes received.
        total_bytes (int):
            The number of total bytes.
        sent_packets (int):
            The number of packets sent.
        received_packets (int):
            The number of packets received.
        session_duration (google.protobuf.duration_pb2.Duration):
            The duration of the session as the number of seconds and
            nanoseconds. For seconds, network.session_duration.seconds,
            the type is a 64-bit integer. For nanoseconds,
            network.session_duration.nanos, the type is a 32-bit
            integer.
        session_id (str):
            The ID of the network session.
        parent_session_id (str):
            The ID of the parent network session.
        application_protocol_version (str):
            The version of the application protocol. e.g.
            "1.1, 2.0".
        community_id (str):
            Community ID network flow value.
        direction (google.backstory.types.Network.Direction):
            The direction of network traffic.
        ip_protocol (google.backstory.types.Network.IpProtocol):
            The IP protocol.
        ipv6 (bool):
            True if IPv6 is used.
        application_protocol (google.backstory.types.Network.ApplicationProtocol):
            The application protocol.
        ftp (google.backstory.types.Ftp):
            FTP info.
        email (google.backstory.types.Email):
            Email info for the sender/recipient.
        dns (google.backstory.types.Dns):
            DNS info.
        dhcp (google.backstory.types.Dhcp):
            DHCP info.
        http (google.backstory.types.Http):
            HTTP info.
        tls (google.backstory.types.Tls):
            TLS info.
        smtp (google.backstory.types.Smtp):
            SMTP info.
            Store fields specific to SMTP not covered by
            Email.
        asn (str):
            Autonomous system number.
        dns_domain (str):
            DNS domain name.
        carrier_name (str):
            Carrier identification.
        organization_name (str):
            Organization name (e.g Google).
        ip_subnet_range (str):
            Associated human-readable IP subnet range
            (e.g. 10.1.2.0/24).
        is_proxy (bool):
            Whether the IP address is a known proxy.
        proxy_info (google.backstory.types.ProxyInfo):
            Proxy information. Only set if is_proxy is true.
        connection_state (google.backstory.types.Network.ConnectionState):
            The state of the network connection.
    """

    class Direction(proto.Enum):
        r"""A network traffic direction.

        Values:
            UNKNOWN_DIRECTION (0):
                The default direction.
            INBOUND (1):
                An inbound request.
            OUTBOUND (2):
                An outbound request.
            BROADCAST (3):
                A broadcast.
        """

        UNKNOWN_DIRECTION = 0
        INBOUND = 1
        OUTBOUND = 2
        BROADCAST = 3

    class IpProtocol(proto.Enum):
        r"""An IP protocol.

        Values:
            UNKNOWN_IP_PROTOCOL (0):
                The default protocol.
            ICMP (1):
                ICMP.
            IGMP (2):
                IGMP
            TCP (6):
                TCP.
            UDP (17):
                UDP.
            IP6IN4 (41):
                IPv6 Encapsulation
            GRE (47):
                Generic Routing Encapsulation
            ESP (50):
                Encapsulating Security Payload
            ICMP6 (58):
                ICMPv6
            EIGRP (88):
                Enhanced Interior Gateway Routing
            ETHERIP (97):
                Ethernet-within-IP Encapsulation
            PIM (103):
                Protocol Independent Multicast
            VRRP (112):
                Virtual Router Redundancy Protocol
            SCTP (132):
                Stream Control Transmission Protocol
        """

        UNKNOWN_IP_PROTOCOL = 0
        ICMP = 1
        IGMP = 2
        TCP = 6
        UDP = 17
        IP6IN4 = 41
        GRE = 47
        ESP = 50
        ICMP6 = 58
        EIGRP = 88
        ETHERIP = 97
        PIM = 103
        VRRP = 112
        SCTP = 132

    class ApplicationProtocol(proto.Enum):
        r"""A network application protocol.

        Values:
            UNKNOWN_APPLICATION_PROTOCOL (0):
                The default application protocol.
            AFP (1):
                Apple Filing Protocol.
            APPC (2):
                Advanced Program-to-Program Communication.
            AMQP (3):
                Advanced Message Queuing Protocol.
            ATOM (4):
                Publishing Protocol.
            BEEP (5):
                Block Extensible Exchange Protocol.
            BITCOIN (6):
                Crypto currency protocol.
            BIT_TORRENT (7):
                Peer-to-peer file sharing.
            CFDP (8):
                Coherent File Distribution Protocol.
            CIP (67):
                Common Industrial Protocol.
            COAP (9):
                Constrained Application Protocol.
            COTP (68):
                Connection Oriented Transport Protocol.
            DCERPC (66):
                DCE/RPC.
            DDS (10):
                Data Distribution Service.
            DEVICE_NET (11):
                Automation industry protocol.
            DHCP (4000):
                DHCP.
            DICOM (69):
                Digital Imaging and Communications in
                Medicine Protocol.
            DNP3 (70):
                Distributed Network Protocol 3 (DNP3)
            DNS (3000):
                DNS.
            E_DONKEY (12):
                Classic file sharing protocol.
            ENRP (13):
                Endpoint Handlespace Redundancy Protocol.
            FAST_TRACK (14):
                Filesharing peer-to-peer protocol.
            FINGER (15):
                User Information Protocol.
            FREENET (16):
                Censorship resistant peer-to-peer network.
            FTAM (17):
                File Transfer Access and Management.
            GOOSE (71):
                GOOSE Protocol.
            GOPHER (18):
                Gopher protocol.
            GRPC (77):
                gRPC Remote Procedure Call.
            HL7 (19):
                Health Level Seven.
            H323 (20):
                Packet-based multimedia communications
                system.
            HTTP (2000):
                HTTP.
            HTTPS (2001):
                HTTPS.
            IEC104 (72):
                IEC 60870-5-104 (IEC 104) Protocol.
            IRCP (21):
                Internet Relay Chat Protocol.
            KADEMLIA (22):
                Peer-to-peer hashtables.
            KRB5 (65):
                Kerberos 5.
            LDAP (23):
                Lightweight Directory Access Protocol.
            LPD (24):
                Line Printer Daemon Protocol.
            MIME (25):
                Multipurpose Internet Mail Extensions and
                Secure MIME.
            MMS (73):
                Multimedia Messaging Service.
            MODBUS (26):
                Serial communications protocol.
            MQTT (27):
                Message Queuing Telemetry Transport.
            NETCONF (28):
                Network Configuration.
            NFS (29):
                Network File System.
            NIS (30):
                Network Information Service.
            NNTP (31):
                Network News Transfer Protocol.
            NTCIP (32):
                National Transportation Communications for
                Intelligent Transportation System.
            NTP (33):
                Network Time Protocol.
            OSCAR (34):
                AOL Instant Messenger Protocol.
            PNRP (35):
                Peer Name Resolution Protocol.
            PTP (74):
                Precision Time Protocol.
            QUIC (1000):
                QUIC.
            RDP (36):
                Remote Desktop Protocol.
            RELP (37):
                Reliable Event Logging Protocol.
            RIP (38):
                Routing Information Protocol.
            RLOGIN (39):
                Remote Login in UNIX Systems.
            RPC (40):
                Remote Procedure Call.
            RTMP (41):
                Real Time Messaging Protocol.
            RTP (42):
                Real-time Transport Protocol.
            RTPS (43):
                Real Time Publish Subscribe.
            RTSP (44):
                Real Time Streaming Protocol.
            SAP (45):
                Session Announcement Protocol.
            SDP (46):
                Session Description Protocol.
            SIP (47):
                Session Initiation Protocol.
            SLP (48):
                Service Location Protocol.
            SMB (49):
                Server Message Block.
            SMTP (50):
                Simple Mail Transfer Protocol.
            SNMP (75):
                Simple Network Management Protocol.
            SNTP (51):
                Simple Network Time Protocol.
            SSH (52):
                Secure Shell.
            SSMS (53):
                Secure SMS Messaging Protocol.
            STYX (54):
                Styx/9P - Plan 9 from Bell Labs distributed
                file system protocol.
            SV (76):
                Sampled Values Protocol.
            TCAP (55):
                Transaction Capabilities Application Part.
            TDS (56):
                Tabular Data Stream.
            TOR (57):
                Anonymity network.
            TSP (58):
                Time Stamp Protocol.
            VTP (59):
                Virtual Terminal Protocol.
            WHOIS (60):
                Remote Directory Access Protocol.
            WEB_DAV (61):
                Web Distributed Authoring and Versioning.
            X400 (62):
                Message Handling Service Protocol.
            X500 (63):
                Directory Access Protocol (DAP).
            XMPP (64):
                Extensible Messaging and Presence Protocol.
            FTP (78):
                File Transfer Protocol.
        """

        UNKNOWN_APPLICATION_PROTOCOL = 0
        AFP = 1
        APPC = 2
        AMQP = 3
        ATOM = 4
        BEEP = 5
        BITCOIN = 6
        BIT_TORRENT = 7
        CFDP = 8
        CIP = 67
        COAP = 9
        COTP = 68
        DCERPC = 66
        DDS = 10
        DEVICE_NET = 11
        DHCP = 4000
        DICOM = 69
        DNP3 = 70
        DNS = 3000
        E_DONKEY = 12
        ENRP = 13
        FAST_TRACK = 14
        FINGER = 15
        FREENET = 16
        FTAM = 17
        GOOSE = 71
        GOPHER = 18
        GRPC = 77
        HL7 = 19
        H323 = 20
        HTTP = 2000
        HTTPS = 2001
        IEC104 = 72
        IRCP = 21
        KADEMLIA = 22
        KRB5 = 65
        LDAP = 23
        LPD = 24
        MIME = 25
        MMS = 73
        MODBUS = 26
        MQTT = 27
        NETCONF = 28
        NFS = 29
        NIS = 30
        NNTP = 31
        NTCIP = 32
        NTP = 33
        OSCAR = 34
        PNRP = 35
        PTP = 74
        QUIC = 1000
        RDP = 36
        RELP = 37
        RIP = 38
        RLOGIN = 39
        RPC = 40
        RTMP = 41
        RTP = 42
        RTPS = 43
        RTSP = 44
        SAP = 45
        SDP = 46
        SIP = 47
        SLP = 48
        SMB = 49
        SMTP = 50
        SNMP = 75
        SNTP = 51
        SSH = 52
        SSMS = 53
        STYX = 54
        SV = 76
        TCAP = 55
        TDS = 56
        TOR = 57
        TSP = 58
        VTP = 59
        WHOIS = 60
        WEB_DAV = 61
        X400 = 62
        X500 = 63
        XMPP = 64
        FTP = 78

    class ConnectionState(proto.Enum):
        r"""The state of a network connection.

        Values:
            CONNECTION_STATE_UNSPECIFIED (0):
                The default connection state.
            LISTENING (1):
                The port is listening for incoming
                connections.
            ESTABLISHED (2):
                A connection has been established.
            TIME_WAIT (3):
                The connection is waiting for a timeout.
            CLOSE_WAIT (4):
                The connection is waiting for a connection
                termination request from the local application.
            CLOSED (5):
                The connection is closed.
            SYN_SENT (6):
                A connection request has been sent.
            SYN_RECEIVED (7):
                A connection request has been received.
            FIN_WAIT1 (8):
                The connection is waiting for a connection
                termination request from the remote host.
            FIN_WAIT2 (9):
                The connection is waiting for a connection
                termination request from the local application.
            LAST_ACK (10):
                The connection is waiting for an
                acknowledgment of the final connection
                termination request.
        """

        CONNECTION_STATE_UNSPECIFIED = 0
        LISTENING = 1
        ESTABLISHED = 2
        TIME_WAIT = 3
        CLOSE_WAIT = 4
        CLOSED = 5
        SYN_SENT = 6
        SYN_RECEIVED = 7
        FIN_WAIT1 = 8
        FIN_WAIT2 = 9
        LAST_ACK = 10

    sent_bytes: int = proto.Field(
        proto.UINT64,
        number=1,
    )
    received_bytes: int = proto.Field(
        proto.UINT64,
        number=2,
    )
    total_bytes: int = proto.Field(
        proto.INT64,
        number=27,
    )
    sent_packets: int = proto.Field(
        proto.INT64,
        number=22,
    )
    received_packets: int = proto.Field(
        proto.INT64,
        number=23,
    )
    session_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=13,
        message=duration_pb2.Duration,
    )
    session_id: str = proto.Field(
        proto.STRING,
        number=14,
    )
    parent_session_id: str = proto.Field(
        proto.STRING,
        number=20,
    )
    application_protocol_version: str = proto.Field(
        proto.STRING,
        number=21,
    )
    community_id: str = proto.Field(
        proto.STRING,
        number=15,
    )
    direction: Direction = proto.Field(
        proto.ENUM,
        number=12,
        enum=Direction,
    )
    ip_protocol: IpProtocol = proto.Field(
        proto.ENUM,
        number=3,
        enum=IpProtocol,
    )
    ipv6: bool = proto.Field(
        proto.BOOL,
        number=29,
    )
    application_protocol: ApplicationProtocol = proto.Field(
        proto.ENUM,
        number=4,
        enum=ApplicationProtocol,
    )
    ftp: "Ftp" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="Ftp",
    )
    email: "Email" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="Email",
    )
    dns: "Dns" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="Dns",
    )
    dhcp: "Dhcp" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="Dhcp",
    )
    http: "Http" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="Http",
    )
    tls: "Tls" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="Tls",
    )
    smtp: "Smtp" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="Smtp",
    )
    asn: str = proto.Field(
        proto.STRING,
        number=16,
    )
    dns_domain: str = proto.Field(
        proto.STRING,
        number=17,
    )
    carrier_name: str = proto.Field(
        proto.STRING,
        number=18,
    )
    organization_name: str = proto.Field(
        proto.STRING,
        number=19,
    )
    ip_subnet_range: str = proto.Field(
        proto.STRING,
        number=24,
    )
    is_proxy: bool = proto.Field(
        proto.BOOL,
        number=25,
    )
    proxy_info: "ProxyInfo" = proto.Field(
        proto.MESSAGE,
        number=26,
        message="ProxyInfo",
    )
    connection_state: ConnectionState = proto.Field(
        proto.ENUM,
        number=28,
        enum=ConnectionState,
    )


class ProxyInfo(proto.Message):
    r"""Proxy information.

    Attributes:
        anonymous (bool):
            Whether the IP address is anonymous.
        anonymous_vpn (bool):
            Whether the IP address is an anonymous VPN.
        public_proxy (bool):
            Whether the IP address is a public proxy.
        tor_exit_node (bool):
            Whether the IP address is a tor exit node.
        smart_dns_proxy (bool):
            Whether the IP address is a smart DNS proxy.
        hosting_provider (bool):
            Whether the IP address is a hosting provider.
        vpn_datacenter (bool):
            Whether the IP address is a VPN datacenter.
        residential_proxy (bool):
            Whether the IP address is a residential
            proxy.
        vpn_service_name (str):
            The name of the VPN service.
        proxy_over_vpn (bool):
            Whether the IP address is a proxy over VPN.
        relay_proxy (bool):
            Whether the IP address is a relay proxy.
    """

    anonymous: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    anonymous_vpn: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    public_proxy: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    tor_exit_node: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    smart_dns_proxy: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    hosting_provider: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    vpn_datacenter: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    residential_proxy: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    vpn_service_name: str = proto.Field(
        proto.STRING,
        number=9,
    )
    proxy_over_vpn: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    relay_proxy: bool = proto.Field(
        proto.BOOL,
        number=11,
    )


class Extensions(proto.Message):
    r"""Extensions to a UDM event.

    Attributes:
        auth (google.backstory.types.Authentication):
            An authentication extension.
        vulns (google.backstory.types.Vulnerabilities):
            A vulnerability extension.
        entity_risk (google.backstory.types.EntityRisk):
            An entity risk change extension.
        linux_utmp (google.backstory.types.LinuxUtmp):
            A Linux Utmp extension. This captures details
            specific to Linux Utmp events, which record
            login and logout sessions on a Linux system.
        windows_event_log (google.backstory.types.WindowsEventLog):
            A Windows Event Log extension. This captures
            details specific to Windows Event Log events,
            providing structured information from various
            Windows logs.
        resource_usage (google.backstory.types.ResourceUsage):
            A resource usage extension. This captures
            details about what entity (e.g., process, user)
            is using a specific resource.
        system_event_details (google.backstory.types.SystemEventDetails):
            A system event details extension. This
            captures additional details for system-level
            events, such as message type, sender image ID,
            and subsystem.
        outlook_metadata (google.backstory.types.OutlookMetadata):
            A Microsoft Outlook specific metadata
            extension. This includes metadata related to
            Outlook items, such as comments, templates, and
            security flags.
        srum (google.backstory.types.Srum):
            A SRUM extension. This captures details
            specific to Windows System Resource Usage
            Monitor (SRUM) events, providing insights into
            application resource consumption.
        user_assist (google.backstory.types.UserAssist):
            A UserAssist extension. This captures details
            specific to Windows User Assist events, which
            track application usage and execution.
    """

    auth: "Authentication" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Authentication",
    )
    vulns: "Vulnerabilities" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Vulnerabilities",
    )
    entity_risk: gb_entity_risk.EntityRisk = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gb_entity_risk.EntityRisk,
    )
    linux_utmp: "LinuxUtmp" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="LinuxUtmp",
    )
    windows_event_log: "WindowsEventLog" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="WindowsEventLog",
    )
    resource_usage: "ResourceUsage" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="ResourceUsage",
    )
    system_event_details: "SystemEventDetails" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="SystemEventDetails",
    )
    outlook_metadata: "OutlookMetadata" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="OutlookMetadata",
    )
    srum: "Srum" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="Srum",
    )
    user_assist: "UserAssist" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="UserAssist",
    )


class Authentication(proto.Message):
    r"""The Authentication extension captures details specific to
    authentication events. General guidelines for authentication events:

    - Details about the source of the authentication event (for example,
      client IP or hostname), should be captured in principal. The
      principal may be empty if we have no details about the source of
      the login.
    - Details about the target of the authentication event (for example,
      details about the machine that is being logged into or logged out
      of) should be captured in target.
    - Some authentication events may involve a third-party. For example,
      a user logs into a cloud service (for example, Chronicle) via
      their company's SSO (the event is logged by their SSO solution).
      In this case, the principal captures information about the user's
      device, the target captures details about the cloud service they
      logged into, and the intermediary captures details about the SSO
      solution.

    Attributes:
        type_ (google.backstory.types.Authentication.AuthType):
            The type of authentication.
        mechanism (MutableSequence[google.backstory.types.Authentication.Mechanism]):
            The authentication mechanism.
        auth_details (str):
            The vendor defined details of the
            authentication.
        outcome (google.backstory.types.Authentication.Outcome):
            The outcome of the authentication event.
    """

    class AuthType(proto.Enum):
        r"""Type of system the authentication event is associated with.

        Values:
            AUTHTYPE_UNSPECIFIED (0):
                The default type.
            MACHINE (1):
                A machine authentication.
            SSO (2):
                An SSO authentication.
            VPN (3):
                A VPN authentication.
            PHYSICAL (4):
                A Physical authentication (e.g. "Badge
                reader").
            TACACS (5):
                A TACACS family protocol for networked
                systems authentication (e.g. TACACS, TACACS+).
        """

        AUTHTYPE_UNSPECIFIED = 0
        MACHINE = 1
        SSO = 2
        VPN = 3
        PHYSICAL = 4
        TACACS = 5

    class Mechanism(proto.Enum):
        r"""Mechanism(s) used to authenticate.

        Values:
            MECHANISM_UNSPECIFIED (0):
                The default mechanism.
            USERNAME_PASSWORD (1):
                Username + password authentication.
            OTP (2):
                OTP authentication.
            HARDWARE_KEY (3):
                Hardware key authentication.
            LOCAL (4):
                Local authentication.
            REMOTE (5):
                Remote authentication.
            REMOTE_INTERACTIVE (6):
                RDP, Terminal Services, or VNC.
            MECHANISM_OTHER (7):
                Some other mechanism that is not defined
                here.
            BADGE_READER (8):
                Badge reader authentication
            NETWORK (9):
                Network authentication.
            BATCH (10):
                Batch authentication.
            SERVICE (11):
                Service authentication
            UNLOCK (12):
                Direct human-interactive unlock
                authentication.
            NETWORK_CLEAR_TEXT (13):
                Network clear text authentication.
            NEW_CREDENTIALS (14):
                Authentication with new credentials.
            INTERACTIVE (15):
                Interactive authentication.
            CACHED_INTERACTIVE (16):
                Interactive authentication using cached
                credentials.
            CACHED_REMOTE_INTERACTIVE (17):
                Cached Remote Interactive authentication
                using cached credentials.
            CACHED_UNLOCK (18):
                Cached Remote Interactive authentication
                using cached credentials.
            BIOMETRIC (19):
                Biometric device such as a fingerprint
                reader.
            WEARABLE (20):
                Wearable such as an Apple Watch.
        """

        MECHANISM_UNSPECIFIED = 0
        USERNAME_PASSWORD = 1
        OTP = 2
        HARDWARE_KEY = 3
        LOCAL = 4
        REMOTE = 5
        REMOTE_INTERACTIVE = 6
        MECHANISM_OTHER = 7
        BADGE_READER = 8
        NETWORK = 9
        BATCH = 10
        SERVICE = 11
        UNLOCK = 12
        NETWORK_CLEAR_TEXT = 13
        NEW_CREDENTIALS = 14
        INTERACTIVE = 15
        CACHED_INTERACTIVE = 16
        CACHED_REMOTE_INTERACTIVE = 17
        CACHED_UNLOCK = 18
        BIOMETRIC = 19
        WEARABLE = 20

    class AuthenticationStatus(proto.Enum):
        r"""Authentication status, can be used to describe the status of
        authentication for a user or particular credential.

        Values:
            UNKNOWN_AUTHENTICATION_STATUS (0):
                The default authentication status.
            ACTIVE (1):
                The authentication method is in active state.
            SUSPENDED (2):
                The authentication method is in
                suspended/disabled state.
            NO_ACTIVE_CREDENTIALS (3):
                The authentication method has no active
                credentials.
            DELETED (4):
                The authentication method has been deleted.
        """

        UNKNOWN_AUTHENTICATION_STATUS = 0
        ACTIVE = 1
        SUSPENDED = 2
        NO_ACTIVE_CREDENTIALS = 3
        DELETED = 4

    class Outcome(proto.Enum):
        r"""The outcome of the authentication event.

        Values:
            OUTCOME_UNSPECIFIED (0):
                The default outcome.
            SUCCESS (1):
                The authentication was successful.
            FAILURE (2):
                The authentication failed.
        """

        OUTCOME_UNSPECIFIED = 0
        SUCCESS = 1
        FAILURE = 2

    type_: AuthType = proto.Field(
        proto.ENUM,
        number=1,
        enum=AuthType,
    )
    mechanism: MutableSequence[Mechanism] = proto.RepeatedField(
        proto.ENUM,
        number=2,
        enum=Mechanism,
    )
    auth_details: str = proto.Field(
        proto.STRING,
        number=3,
    )
    outcome: Outcome = proto.Field(
        proto.ENUM,
        number=4,
        enum=Outcome,
    )


class LinuxUtmp(proto.Message):
    r"""The LinuxUtmp extension captures details specific to Linux
    Utmp events.

    Attributes:
        record_type (google.backstory.types.LinuxUtmp.RecordType):
            The activity record type.
    """

    class RecordType(proto.Enum):
        r"""The type of activity record from the Utmp file.

        Values:
            RECORD_TYPE_UNSPECIFIED (0):
                The default record type.
            RUN_LVL (1):
                Run-level change.
            BOOT_TIME (2):
                System boot time.
            NEW_TIME (3):
                New time after system clock change.
            OLD_TIME (4):
                Old time before system clock change.
            INIT_PROCESS (5):
                Process spawned by init.
            LOGIN_PROCESS (6):
                Login process.
            USER_PROCESS (7):
                Normal user process (logged-in session).
            DEAD_PROCESS (8):
                Terminated process (session ended).
            ACCOUNTING (9):
                Accounting message.
        """

        RECORD_TYPE_UNSPECIFIED = 0
        RUN_LVL = 1
        BOOT_TIME = 2
        NEW_TIME = 3
        OLD_TIME = 4
        INIT_PROCESS = 5
        LOGIN_PROCESS = 6
        USER_PROCESS = 7
        DEAD_PROCESS = 8
        ACCOUNTING = 9

    record_type: RecordType = proto.Field(
        proto.ENUM,
        number=1,
        enum=RecordType,
    )


class WindowsEventLog(proto.Message):
    r"""The WindowsEventLog extension captures details specific to
    Windows Event Log events.

    Attributes:
        channel (google.backstory.types.WindowsEventLog.Channel):
            The channel of the event.
        event_id (str):
            A unique identifier for a specific type of
            event.
        activity_id (str):
            A GUID (Globally Unique Identifier) used to
            link a sequence of related events together.
    """

    class Channel(proto.Enum):
        r"""The channel specifies the source or category of the event.

        Values:
            CHANNEL_UNSPECIFIED (0):
                Default channel.
            SECURITY (1):
                The security channel.
            SYSTEM (2):
                The system channel.
            APPLICATION (3):
                The application channel.
            SETUP (4):
                The setup channel.
            FORWARDED_EVENTS (5):
                The forwarded events channel.
            OTHER (6):
                The other channel.
        """

        CHANNEL_UNSPECIFIED = 0
        SECURITY = 1
        SYSTEM = 2
        APPLICATION = 3
        SETUP = 4
        FORWARDED_EVENTS = 5
        OTHER = 6

    channel: Channel = proto.Field(
        proto.ENUM,
        number=1,
        enum=Channel,
    )
    event_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    activity_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ResourceUsage(proto.Message):
    r"""The ResourceUsage extension captures details about what is
    using a resource.

    Attributes:
        used_entity (str):
            The name of the entity (e.g., process, user)
            that is using the resource.
        used_entity_id (str):
            A numerical identifier for the entity using
            the resource (e.g., PID, UID).
    """

    used_entity: str = proto.Field(
        proto.STRING,
        number=1,
    )
    used_entity_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SystemEventDetails(proto.Message):
    r"""Captures additional details for system-level events.

    Attributes:
        message_type (str):
            The specific type or category of the message.
        sender_image_id (str):
            An identifier for the image associated with
            the sender of the message.
        subsystem (str):
            The subsystem or component that generated the
            event.
    """

    message_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    sender_image_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    subsystem: str = proto.Field(
        proto.STRING,
        number=3,
    )


class OutlookMetadata(proto.Message):
    r"""Microsoft Outlook specific metadata.

    Attributes:
        comment (str):
            A user-defined comment or note associated
            with the Outlook item.
        template (str):
            The name of the template file used to create
            the Outlook item.
        title (str):
            The title of the Outlook item.
        security_flags_count (int):
            Count of Security-related flags for the
            message, such as encryption or signing status.
    """

    comment: str = proto.Field(
        proto.STRING,
        number=1,
    )
    template: str = proto.Field(
        proto.STRING,
        number=2,
    )
    title: str = proto.Field(
        proto.STRING,
        number=3,
    )
    security_flags_count: int = proto.Field(
        proto.INT32,
        number=4,
    )


class Srum(proto.Message):
    r"""The Srum extension captures details specific to Windows
    System Resource Usage Monitor (SRUM) events.

    Attributes:
        id (str):
            A unique identifier for the SRUM record or
            the application/user being monitored.
        background_bytes_read (int):
            The number of bytes read by the application
            while running in the background.
        background_bytes_written (int):
            The number of bytes written by the
            application while running in the background.
        background_context_switches (int):
            The number of context switches performed by
            the application's threads while in the
            background.
        background_cycle_count (int):
            The amount of CPU cycle time consumed by the
            application in the background, measured in clock
            cycles.
        background_flushes_count (int):
            The number of flush operations performed by
            the application in the background.
        background_read_operations (int):
            The number of read operations performed by
            the application in the background.
        background_write_operations (int):
            The number of write operations performed by
            the application in the background.
        interface_luid (str):
            The Locally Unique Identifier (LUID) for the
            network interface used for data transfer.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    background_bytes_read: int = proto.Field(
        proto.INT64,
        number=2,
    )
    background_bytes_written: int = proto.Field(
        proto.INT64,
        number=3,
    )
    background_context_switches: int = proto.Field(
        proto.INT64,
        number=4,
    )
    background_cycle_count: int = proto.Field(
        proto.INT64,
        number=5,
    )
    background_flushes_count: int = proto.Field(
        proto.INT64,
        number=6,
    )
    background_read_operations: int = proto.Field(
        proto.INT64,
        number=7,
    )
    background_write_operations: int = proto.Field(
        proto.INT64,
        number=8,
    )
    interface_luid: str = proto.Field(
        proto.STRING,
        number=9,
    )


class UserAssist(proto.Message):
    r"""The UserAssist extension captures details specific to Windows
    User Assist events.

    Attributes:
        application_focus_count (int):
            The number of times the application
            associated with the entry gained focus.
        application_focus_duration (google.protobuf.duration_pb2.Duration):
            The total duration the application associated
            with the entry was in focus.
        executions_count (int):
            The number of times the application
            associated with the entry has been executed.
        entry_index (int):
            The index or identifier of the user assist
            entry, unique per user.
    """

    application_focus_count: int = proto.Field(
        proto.INT64,
        number=1,
    )
    application_focus_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    executions_count: int = proto.Field(
        proto.INT64,
        number=3,
    )
    entry_index: int = proto.Field(
        proto.INT64,
        number=4,
    )


class Vulnerabilities(proto.Message):
    r"""The Vulnerabilities extension captures details on
    observed/detected vulnerabilities.

    Attributes:
        vulnerabilities (MutableSequence[google.backstory.types.Vulnerability]):
            A list of vulnerabilities.
    """

    vulnerabilities: MutableSequence["Vulnerability"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Vulnerability",
    )


class Vulnerability(proto.Message):
    r"""A vulnerability.

    Attributes:
        about (google.backstory.types.Noun):
            If the vulnerability is about a specific noun
            (e.g. executable), then add it here.
        name (str):
            Name of the vulnerability (e.g. "Unsupported
            OS Version detected").
        description (str):
            Description of the vulnerability.
        vendor (str):
            Vendor of scan that discovered vulnerability.
        scan_start_time (google.protobuf.timestamp_pb2.Timestamp):
            If the vulnerability was discovered during an
            asset scan, then this field should be populated
            with the time the scan started. This field can
            be left unset if the start time is not available
            or not applicable.
        scan_end_time (google.protobuf.timestamp_pb2.Timestamp):
            If the vulnerability was discovered during an
            asset scan, then this field should be populated
            with the time the scan ended. This field can be
            left unset if the end time is not available or
            not applicable.
        first_found (google.protobuf.timestamp_pb2.Timestamp):
            Products that maintain a history of vuln scans should
            populate first_found with the time that a scan first
            detected the vulnerability on this asset.
        last_found (google.protobuf.timestamp_pb2.Timestamp):
            Products that maintain a history of vuln scans should
            populate last_found with the time that a scan last detected
            the vulnerability on this asset.
        severity (google.backstory.types.Vulnerability.Severity):
            The severity of the vulnerability.
        severity_details (str):
            Vendor-specific severity
        cvss_base_score (float):
            CVSS Base Score in the range of 0.0 to 10.0.
            Useful for sorting.
        cvss_vector (str):
            Vector of CVSS properties (e.g.
            "AV:L/AC:H/Au:N/C:N/I:P/A:C") Can be linked to via:
            https://nvd.nist.gov/vuln-metrics/cvss/v2-calculator
        cvss_version (str):
            Version of CVSS Vector/Score.
        cve_id (str):
            Common Vulnerabilities and Exposures Id.
            https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures
            https://cve.mitre.org/about/faqs.html#what_is_cve_id
        cve_description (str):
            Common Vulnerabilities and Exposures Description.
            https://cve.mitre.org/about/faqs.html#what_is_cve_record
        vendor_vulnerability_id (str):
            Vendor specific vulnerability id (e.g.
            Microsoft security bulletin id).
        vendor_knowledge_base_article_id (str):
            Vendor specific knowledge base article (e.g. "KBXXXXXX" from
            Microsoft).
            https://en.wikipedia.org/wiki/Microsoft_Knowledge_Base
            https://access.redhat.com/knowledgebase
    """

    class Severity(proto.Enum):
        r"""Severity of the vulnerability.

        Values:
            UNKNOWN_SEVERITY (0):
                The default severity level.
            LOW (1):
                Low severity.
            MEDIUM (2):
                Medium severity.
            HIGH (3):
                High severity.
            CRITICAL (4):
                Critical severity.
        """

        UNKNOWN_SEVERITY = 0
        LOW = 1
        MEDIUM = 2
        HIGH = 3
        CRITICAL = 4

    about: "Noun" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Noun",
    )
    name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    vendor: str = proto.Field(
        proto.STRING,
        number=13,
    )
    scan_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    scan_end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    first_found: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    last_found: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    severity: Severity = proto.Field(
        proto.ENUM,
        number=8,
        enum=Severity,
    )
    severity_details: str = proto.Field(
        proto.STRING,
        number=9,
    )
    cvss_base_score: float = proto.Field(
        proto.FLOAT,
        number=10,
    )
    cvss_vector: str = proto.Field(
        proto.STRING,
        number=11,
    )
    cvss_version: str = proto.Field(
        proto.STRING,
        number=12,
    )
    cve_id: str = proto.Field(
        proto.STRING,
        number=14,
    )
    cve_description: str = proto.Field(
        proto.STRING,
        number=15,
    )
    vendor_vulnerability_id: str = proto.Field(
        proto.STRING,
        number=16,
    )
    vendor_knowledge_base_article_id: str = proto.Field(
        proto.STRING,
        number=17,
    )


class Ftp(proto.Message):
    r"""FTP info.

    Attributes:
        command (str):
            The FTP command.
    """

    command: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Smtp(proto.Message):
    r"""SMTP info.  See RFC 2821.

    Attributes:
        helo (str):
            The client's 'HELO'/'EHLO' string.
        mail_from (str):
            The client's 'MAIL FROM' string.
        rcpt_to (MutableSequence[str]):
            The client's 'RCPT TO' string(s).
        server_response (MutableSequence[str]):
            The server's response(s) to the client.
        message_path (str):
            The message's path (extracted from the
            headers).
        is_webmail (bool):
            If the message was sent via a webmail client.
        is_tls (bool):
            If the connection switched to TLS.
    """

    helo: str = proto.Field(
        proto.STRING,
        number=1,
    )
    mail_from: str = proto.Field(
        proto.STRING,
        number=2,
    )
    rcpt_to: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    server_response: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    message_path: str = proto.Field(
        proto.STRING,
        number=5,
    )
    is_webmail: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    is_tls: bool = proto.Field(
        proto.BOOL,
        number=7,
    )


class Email(proto.Message):
    r"""Email info.

    Attributes:
        from_ (str):
            The 'from' address.
        reply_to (str):
            The 'reply to' address.
        to (MutableSequence[str]):
            A list of 'to' addresses.
        cc (MutableSequence[str]):
            A list of 'cc' addresses.
        bcc (MutableSequence[str]):
            A list of 'bcc' addresses.
        mail_id (str):
            The mail (or message) ID.
        subject (MutableSequence[str]):
            The subject line(s) of the email.
        bounce_address (str):
            The envelope from address.
            https://en.wikipedia.org/wiki/Bounce_address
    """

    from_: str = proto.Field(
        proto.STRING,
        number=1,
    )
    reply_to: str = proto.Field(
        proto.STRING,
        number=2,
    )
    to: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    cc: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    bcc: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    mail_id: str = proto.Field(
        proto.STRING,
        number=6,
    )
    subject: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    bounce_address: str = proto.Field(
        proto.STRING,
        number=8,
    )


class Process(proto.Message):
    r"""Information about a process.

    Attributes:
        pid (str):
            The process ID.
            This field can be used as an entity indicator
            for process entities.
        parent_pid (str):
            The ID of the parent process. Deprecated: use
            parent_process.pid instead.
        parent_process (google.backstory.types.Process):
            Information about the parent process.
        file (google.backstory.types.File):
            Information about the file in use by the
            process.
        command_line (str):
            The command line command that created the
            process. This field can be used as an entity
            indicator for process entities.
        command_line_history (MutableSequence[str]):
            The command line history of the process.
        product_specific_process_id (str):
            A product specific process id.
        access_mask (int):
            A bit mask representing the level of access.
        integrity_level_rid (int):
            The Microsoft Windows integrity level
            relative ID (RID) of the process.
        euid (str):
            The effective user ID of the process.
        ruid (str):
            The real user ID of the process.
        egid (str):
            The effective group ID of the process.
        rgid (str):
            The real group ID of the process.
        pgid (str):
            The identifier that points to the process
            group ID leader.
        session_leader_pid (str):
            The process ID of the session leader process.
        tty (str):
            The teletype terminal which the command was
            executed within.
        token_elevation_type (google.backstory.types.Process.TokenElevationType):
            The elevation type of the process on
            Microsoft Windows. This determines if any
            privileges are removed when UAC is enabled.
        product_specific_parent_process_id (str):
            A product specific id for the parent process. Please use
            parent_process.product_specific_process_id instead.
        ipv6 (bool):
            This is used to determine if the process is
            an IPv6 process.
        kernel_duration (google.protobuf.duration_pb2.Duration):
            The kernel time spent in the process.
        user_duration (google.protobuf.duration_pb2.Duration):
            The user time spent in the process.
        real_duration (google.protobuf.duration_pb2.Duration):
            The real time spent in the process. This is
            the sum of the kernel and user time.
        state (google.backstory.types.Process.State):
            The state of the process.
    """

    class TokenElevationType(proto.Enum):
        r"""The elevation type of the process's token. See
        https://learn.microsoft.com/en-us/windows/win32/api/winnt/ne-winnt-token_elevation_type

        Values:
            UNKNOWN (0):
                An undetermined token type.
            TYPE_1 (1):
                A full token with no privileges removed or
                groups disabled.
            TYPE_2 (2):
                An elevated token with no privileges removed
                or groups disabled. Used when running as
                administrator.
            TYPE_3 (3):
                A limited token with administrative
                privileges removed and administrative groups
                disabled.
        """

        UNKNOWN = 0
        TYPE_1 = 1
        TYPE_2 = 2
        TYPE_3 = 3

    class State(proto.Enum):
        r"""The state of the process.
        See
        https://psutil.readthedocs.io/en/stable/#process-status-constants.

        Values:
            STATE_UNSPECIFIED (0):
                Undetermined state.
            RUNNING (1):
                Process is running or runnable.
            SLEEPING (2):
                Process is waiting for an event.
            DISK_SLEEP (3):
                Process is in uninterruptible sleep,
                typically I/O.
            STOPPED (4):
                Process is stopped.
            TRACING_STOP (5):
                Process is stopped by debugger.
            ZOMBIE (6):
                Process is terminated but not reaped by
                parent.
            DEAD (7):
                Process is terminated.
            WAKE_KILL (8):
                Process is woken to be killed.
            WAKING (9):
                Process is waking from sleep.
            PARKED (10):
                Linux specific: process is parked.
            IDLE (11):
                Linux, macOS, and FreeBSD specific: process
                is idle.
            LOCKED (12):
                FreeBSD specific: process is locked.
            WAITING (13):
                FreeBSD specific: process is waiting.
            SUSPENDED (14):
                NetBSD specific: process is suspended.
        """

        STATE_UNSPECIFIED = 0
        RUNNING = 1
        SLEEPING = 2
        DISK_SLEEP = 3
        STOPPED = 4
        TRACING_STOP = 5
        ZOMBIE = 6
        DEAD = 7
        WAKE_KILL = 8
        WAKING = 9
        PARKED = 10
        IDLE = 11
        LOCKED = 12
        WAITING = 13
        SUSPENDED = 14

    pid: str = proto.Field(
        proto.STRING,
        number=1,
    )
    parent_pid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    parent_process: "Process" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="Process",
    )
    file: "File" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="File",
    )
    command_line: str = proto.Field(
        proto.STRING,
        number=4,
    )
    command_line_history: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=9,
    )
    product_specific_process_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    access_mask: int = proto.Field(
        proto.UINT64,
        number=8,
    )
    integrity_level_rid: int = proto.Field(
        proto.UINT64,
        number=11,
    )
    euid: str = proto.Field(
        proto.STRING,
        number=12,
    )
    ruid: str = proto.Field(
        proto.STRING,
        number=13,
    )
    egid: str = proto.Field(
        proto.STRING,
        number=14,
    )
    rgid: str = proto.Field(
        proto.STRING,
        number=15,
    )
    pgid: str = proto.Field(
        proto.STRING,
        number=16,
    )
    session_leader_pid: str = proto.Field(
        proto.STRING,
        number=17,
    )
    tty: str = proto.Field(
        proto.STRING,
        number=18,
    )
    token_elevation_type: TokenElevationType = proto.Field(
        proto.ENUM,
        number=10,
        enum=TokenElevationType,
    )
    product_specific_parent_process_id: str = proto.Field(
        proto.STRING,
        number=6,
    )
    ipv6: bool = proto.Field(
        proto.BOOL,
        number=19,
    )
    kernel_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=20,
        message=duration_pb2.Duration,
    )
    user_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=21,
        message=duration_pb2.Duration,
    )
    real_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=22,
        message=duration_pb2.Duration,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=23,
        enum=State,
    )


class AnalyticsMetadata(proto.Message):
    r"""Stores information about an analytics metric used in a rule.

    Attributes:
        analytic (str):
            Name of the analytic.
    """

    analytic: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FindingVariable(proto.Message):
    r"""A structure that holds the value and associated metadata for
    values extracted while producing a Finding.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        type_ (google.backstory.types.FindingVariable.Type):
            The type of the variable.
        value (str):
            The value in string form.
        source_path (str):
            The UDM field path for the field which this value was
            derived from. Example: ``principal.user.username``
        bool_val (bool):
            The value in boolean format.

            This field is a member of `oneof`_ ``typed_value``.
        bytes_val (bytes):
            The value in bytes format.

            This field is a member of `oneof`_ ``typed_value``.
        double_val (float):
            The value in double format.

            This field is a member of `oneof`_ ``typed_value``.
        int64_val (int):
            The value in int64 format.

            This field is a member of `oneof`_ ``typed_value``.
        uint64_val (int):
            The value in uint64 format.

            This field is a member of `oneof`_ ``typed_value``.
        string_val (str):
            The value in string format.
            Enum values are returned as strings.

            This field is a member of `oneof`_ ``typed_value``.
        timestamp_time (google.protobuf.timestamp_pb2.Timestamp):
            The value in timestamp format.

            This field is a member of `oneof`_ ``typed_value``.
        null_val (bool):
            Whether the value is null.

            This field is a member of `oneof`_ ``typed_value``.
        bool_seq (google.backstory.types.BoolSequence):
            The value in boolsequence format.

            This field is a member of `oneof`_ ``typed_value``.
        bytes_seq (google.backstory.types.BytesSequence):
            The value in bytessequence format.

            This field is a member of `oneof`_ ``typed_value``.
        double_seq (google.backstory.types.DoubleSequence):
            The value in doublesequence format.

            This field is a member of `oneof`_ ``typed_value``.
        int64_seq (google.backstory.types.Int64Sequence):
            The value in int64sequence format.

            This field is a member of `oneof`_ ``typed_value``.
        uint64_seq (google.backstory.types.Uint64Sequence):
            The value in uint64sequence format.

            This field is a member of `oneof`_ ``typed_value``.
        string_seq (google.backstory.types.StringSequence):
            The value in stringsequence format.

            This field is a member of `oneof`_ ``typed_value``.
    """

    class Type(proto.Enum):
        r"""Type options for Finding variables.

        Values:
            TYPE_UNSPECIFIED (0):
                An unspecified variable type.
            MATCH (1):
                A variable coming from the match conditions.
            OUTCOME (2):
                A variable representing significant data that
                was found in the detection logic.
        """

        TYPE_UNSPECIFIED = 0
        MATCH = 1
        OUTCOME = 2

    type_: Type = proto.Field(
        proto.ENUM,
        number=1,
        enum=Type,
    )
    value: str = proto.Field(
        proto.STRING,
        number=2,
    )
    source_path: str = proto.Field(
        proto.STRING,
        number=3,
    )
    bool_val: bool = proto.Field(
        proto.BOOL,
        number=4,
        oneof="typed_value",
    )
    bytes_val: bytes = proto.Field(
        proto.BYTES,
        number=5,
        oneof="typed_value",
    )
    double_val: float = proto.Field(
        proto.DOUBLE,
        number=6,
        oneof="typed_value",
    )
    int64_val: int = proto.Field(
        proto.INT64,
        number=7,
        oneof="typed_value",
    )
    uint64_val: int = proto.Field(
        proto.UINT64,
        number=8,
        oneof="typed_value",
    )
    string_val: str = proto.Field(
        proto.STRING,
        number=9,
        oneof="typed_value",
    )
    timestamp_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="typed_value",
        message=timestamp_pb2.Timestamp,
    )
    null_val: bool = proto.Field(
        proto.BOOL,
        number=10,
        oneof="typed_value",
    )
    bool_seq: "BoolSequence" = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="typed_value",
        message="BoolSequence",
    )
    bytes_seq: "BytesSequence" = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="typed_value",
        message="BytesSequence",
    )
    double_seq: "DoubleSequence" = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="typed_value",
        message="DoubleSequence",
    )
    int64_seq: "Int64Sequence" = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="typed_value",
        message="Int64Sequence",
    )
    uint64_seq: "Uint64Sequence" = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof="typed_value",
        message="Uint64Sequence",
    )
    string_seq: "StringSequence" = proto.Field(
        proto.MESSAGE,
        number=16,
        oneof="typed_value",
        message="StringSequence",
    )


class SecurityResult(proto.Message):
    r"""Security related metadata for the event. A security result might be
    something like "virus detected and quarantined," "malicious
    connection blocked," or "sensitive data included in document
    foo.doc." Each security result, of which there may be more than one,
    may either pertain to the whole event, or to a specific object or
    device referenced in the event (e.g. a malicious file that was
    detected, or a sensitive document sent as an email attachment). For
    security results that apply to a particular object referenced in the
    event, the security_results message MUST contain details about the
    implicated object (such as process, user, IP, domain, URL, IP, or
    email address) in the about field. For security results that apply
    to the entire event (e.g. SPAM found in this email), the about field
    must remain empty.

    Attributes:
        about (google.backstory.types.Noun):
            If the security result is about a specific
            entity (Noun), add it here. This field is not
            populated when the SecurityResult appears in a
            detection.
        category (MutableSequence[google.backstory.types.SecurityResult.SecurityCategory]):
            The security category.
            This field is not populated when the
            SecurityResult appears in a detection.
        category_details (MutableSequence[str]):
            For vendor-specific categories. For web
            categorization, put type in here such as
            "gambling" or "porn". This field is not
            populated when the SecurityResult appears in a
            detection.
        threat_name (str):
            A vendor-assigned classification common
            across multiple customers (for example,
            "W32/File-A", "Slammer"). This field is not
            populated when the SecurityResult appears in a
            detection.
        rule_set (str):
            The curated detection's rule set identifier.
            (for example, "windows-threats")
            This is primarily set in rule-generated
            detections and alerts.
        rule_set_display_name (str):
            The curated detections rule set display name.
            This is primarily set in rule-generated
            detections and alerts.
        ruleset_category_display_name (str):
            The curated detection rule set category display name. (for
            example, if rule_set_display_name is "CDIR SCC Enhanced
            Exfiltration", the rule_set_category is "Cloud Threats").
            This is primarily set in rule-generated detections and
            alerts.
        rule_id (str):
            A vendor-specific ID for a rule, varying by
            observer type (e.g. "08123",
            "5d2b44d0-5ef6-40f5-a704-47d61d3babbe").
        rule_name (str):
            Name of the security rule
            (e.g. "BlockInboundToOracle").
        display_name (str):
            The display name of the security result. This is populated
            from 'name_override' Outcome Variable, if present.
            Otherwise, this field is not set.
        rule_version (str):
            Version of the security rule.
            (e.g. "v1.1", "00001", "1604709794",
            "2020-11-16T23:04:19+00:00"). Note that rule
            versions are source-dependant and lexical
            ordering should not be assumed.
        rule_type (str):
            The type of security rule.
        rule_author (str):
            Author of the security rule.
            This field is not populated when the
            SecurityResult appears in a detection.
        rule_labels (MutableSequence[google.backstory.types.Label]):
            A list of rule labels that can't be captured
            by the other fields in security result
            (e.g. "reference : AnotherRule", "contributor :
            John"). This is primarily set in rule-generated
            detections and alerts.
        alert_state (google.backstory.types.SecurityResult.AlertState):
            The alerting types of this security result.
            This is primarily set for rule-generated
            detections and alerts.
        detection_fields (MutableSequence[google.backstory.types.Label]):
            An ordered list of values, that represent
            fields in detections for a security finding.
            This list represents mapping of names of
            requested entities to their values (the security
            result matched variables).

            For Collection SecurityResults, prefer variables
            instead.
        outcomes (MutableSequence[google.backstory.types.Label]):
            A list of outcomes that represent the results
            of this security finding. This list represents a
            mapping of names of the requested outcomes, to a
            stringified version of their values.

            This is only populated when the SecurityResult
            appears in a detection. This is deprecated. Use
            variables instead.
        variables (MutableMapping[str, google.backstory.types.FindingVariable]):
            A list of outcomes and match variables that
            represent the results of this security finding.
            This list represents a mapping of names of the
            requested outcomes or match variables, to their
            values.

            This is only populated when the SecurityResult
            appears in a detection.
        summary (str):
            A short human-readable summary (e.g. "failed
            login occurred")
        description (str):
            A human-readable description (e.g. "user
            password was wrong"). This can be more detailed
            than the summary.
        action (MutableSequence[google.backstory.types.SecurityResult.Action]):
            Actions taken for this event.
            This field is not populated when the
            SecurityResult appears in a detection.
        action_details (str):
            The detail of the action taken as provided by
            the vendor. This field is not populated when the
            SecurityResult appears in a detection.
        severity (google.backstory.types.SecurityResult.ProductSeverity):
            The severity of the result.
        confidence (google.backstory.types.SecurityResult.ProductConfidence):
            The confidence level of the result as
            estimated by the product. This field is not
            populated when the SecurityResult appears in a
            detection.
        priority (google.backstory.types.SecurityResult.ProductPriority):
            The priority of the result.
            This field is not populated when the
            SecurityResult appears in a detection.
        risk_score (float):
            The risk score of the security result.
        confidence_score (float):
            The confidence score of the security result.
            This field is not populated when the
            SecurityResult appears in a detection.
        analytics_metadata (MutableSequence[google.backstory.types.AnalyticsMetadata]):
            Stores metadata about each risk analytic
            metric the rule uses. This field is not
            populated when the SecurityResult appears in a
            detection.
        severity_details (str):
            Vendor-specific severity.
            This field is not populated when the
            SecurityResult appears in a detection.
        confidence_details (str):
            Additional detail with regards to the
            confidence of a security event as estimated by
            the product vendor. This field is not populated
            when the SecurityResult appears in a detection.
        priority_details (str):
            Vendor-specific information about the
            security result priority. This field is not
            populated when the SecurityResult appears in a
            detection.
        url_back_to_product (str):
            URL that takes the user to the source product
            console for this event. This field is not
            populated when the SecurityResult appears in a
            detection.
        threat_id (str):
            Vendor-specific ID for a threat.
            This field is not populated when the
            SecurityResult appears in a detection.
        threat_feed_name (str):
            Vendor feed name for a threat indicator feed.
            This field is not populated when the
            SecurityResult appears in a detection.
        threat_id_namespace (google.backstory.types.Id.Namespace):
            The attribute threat_id_namespace qualifies threat_id with
            an id namespace to get an unique id. The attribute threat_id
            by itself is not unique across Chronicle as it is a vendor
            specific id. This field is not populated when the
            SecurityResult appears in a detection.
        threat_status (google.backstory.types.SecurityResult.ThreatStatus):
            Current status of the threat
            This field is not populated when the
            SecurityResult appears in a detection.
        attack_details (google.backstory.types.AttackDetails):
            MITRE ATT&CK details.
            This field is not populated when the
            SecurityResult appears in a detection.
        first_discovered_time (google.protobuf.timestamp_pb2.Timestamp):
            First time the IoC threat was discovered in
            the provider. This field is not populated when
            the SecurityResult appears in a detection.
        associations (MutableSequence[google.backstory.types.SecurityResult.Association]):
            Associations related to the threat.
        campaigns (MutableSequence[str]):
            Campaigns using this IOC threat. This is deprecated. Use
            threat_collections instead.
        reports (MutableSequence[str]):
            Reports that reference this IOC threat. These are the report
            IDs. This is deprecated. Use threat_collections instead.
        verdict (google.backstory.types.SecurityResult.Verdict):
            Verdict about the IoC from the provider.
            This field is now deprecated. Use VerdictInfo
            instead.
        last_updated_time (google.protobuf.timestamp_pb2.Timestamp):
            Last time the IoC threat was updated in the
            provider. This field is not populated when the
            SecurityResult appears in a detection.
        verdict_info (MutableSequence[google.backstory.types.SecurityResult.VerdictInfo]):
            Verdict information about the IoC from the
            provider. This field is not populated when the
            SecurityResult appears in a detection.
        threat_verdict (google.backstory.types.ThreatVerdict):
            GCTI threat verdict on the security result
            entity. This field is not populated when the
            SecurityResult appears in a detection.
        last_discovered_time (google.protobuf.timestamp_pb2.Timestamp):
            Last time the IoC was seen in the provider
            data. This field is not populated when the
            SecurityResult appears in a detection.
        detection_depth (int):
            The depth of the detection chain.
            Applies only to composite detections.
        threat_collections (MutableSequence[google.backstory.types.SecurityResult.ThreatCollectionItem]):
            GTI collections associated with the security
            result.
    """

    class VerdictResponse(proto.Enum):
        r"""Represents different verdict types. Used to represent
        Mandiant threat intelligence.

        Values:
            VERDICT_RESPONSE_UNSPECIFIED (0):
                The default verdict response type.
            MALICIOUS (1):
                VerdictResponse resulted a threat as
                malicious.
            BENIGN (2):
                VerdictResponse resulted a threat as benign.
        """

        VERDICT_RESPONSE_UNSPECIFIED = 0
        MALICIOUS = 1
        BENIGN = 2

    class IoCStatsType(proto.Enum):
        r"""Type of IoCStat based on source.

        Values:
            UNSPECIFIED_IOC_STATS_TYPE (0):
                IoCStat source is unidentified.
            MANDIANT_SOURCES (1):
                IoCStat is from a Mandiant Source.
            THIRD_PARTY_SOURCES (2):
                IoCStat is from a third-party source.
            THREAT_INTELLIGENCE_IOC_STATS (3):
                IoCStat is from a threat intelligence feed.
        """

        UNSPECIFIED_IOC_STATS_TYPE = 0
        MANDIANT_SOURCES = 1
        THIRD_PARTY_SOURCES = 2
        THREAT_INTELLIGENCE_IOC_STATS = 3

    class VerdictType(proto.Enum):
        r"""Category of the verdict.

        Values:
            VERDICT_TYPE_UNSPECIFIED (0):
                Verdict category not specified.
            PROVIDER_ML_VERDICT (1):
                MLVerdict result provided from threat
                providers, like Mandiant. These fields are used
                to model Mandiant sources.
            ANALYST_VERDICT (2):
                Verdict provided by the human analyst. These
                fields are used to model Mandiant sources.
        """

        VERDICT_TYPE_UNSPECIFIED = 0
        PROVIDER_ML_VERDICT = 1
        ANALYST_VERDICT = 2

    class SecurityCategory(proto.Enum):
        r"""SecurityCategory is used to standardize security categories
        across products so one event is not categorized as "malware" and
        another as a "virus".

        Values:
            UNKNOWN_CATEGORY (0):
                The default category.
            SOFTWARE_MALICIOUS (10000):
                Malware, spyware, rootkit.
            SOFTWARE_SUSPICIOUS (10100):
                Below the conviction threshold; probably bad.
            SOFTWARE_PUA (10200):
                Potentially Unwanted App (such as adware).
            NETWORK_MALICIOUS (20000):
                Includes C&C or network exploit.
            NETWORK_SUSPICIOUS (20100):
                Suspicious activity, such as potential
                reverse tunnel.
            NETWORK_CATEGORIZED_CONTENT (20200):
                Non-security related: URL has category like
                gambling or porn.
            NETWORK_DENIAL_OF_SERVICE (20300):
                DoS, DDoS.
            NETWORK_RECON (20400):
                Port scan detected by an IDS, probing of web
                app.
            NETWORK_COMMAND_AND_CONTROL (20500):
                If we know this is a C&C channel.
            ACL_VIOLATION (30000):
                Unauthorized access attempted, including
                attempted access to files, web services,
                processes, web objects, etc.
            AUTH_VIOLATION (40000):
                Authentication failed (e.g. bad password or
                bad 2-factor authentication).
            EXPLOIT (50000):
                Exploit: For all manner of exploits including
                attempted overflows, bad protocol encodings,
                ROP, SQL injection, etc. For both network and
                host- based exploits.
            DATA_EXFILTRATION (60000):
                DLP: Sensitive data transmission, copy to
                thumb drive.
            DATA_AT_REST (60100):
                DLP: Sensitive data found at rest in a scan.
            DATA_DESTRUCTION (60200):
                Attempt to destroy/delete data.
            TOR_EXIT_NODE (60300):
                TOR Exit Nodes.
            MAIL_SPAM (70000):
                Spam email, message, etc.
            MAIL_PHISHING (70100):
                Phishing email, chat messages, etc.
            MAIL_SPOOFING (70200):
                Spoofed source email address, etc.
            POLICY_VIOLATION (80000):
                Security-related policy violation (e.g.
                firewall/proxy/HIPS rule violated, NAC block
                action).
            SOCIAL_ENGINEERING (90001):
                Threats which manipulate to break normal
                security procedures.
            PHISHING (90002):
                Phishing pages, pops, https phishing etc.
        """

        UNKNOWN_CATEGORY = 0
        SOFTWARE_MALICIOUS = 10000
        SOFTWARE_SUSPICIOUS = 10100
        SOFTWARE_PUA = 10200
        NETWORK_MALICIOUS = 20000
        NETWORK_SUSPICIOUS = 20100
        NETWORK_CATEGORIZED_CONTENT = 20200
        NETWORK_DENIAL_OF_SERVICE = 20300
        NETWORK_RECON = 20400
        NETWORK_COMMAND_AND_CONTROL = 20500
        ACL_VIOLATION = 30000
        AUTH_VIOLATION = 40000
        EXPLOIT = 50000
        DATA_EXFILTRATION = 60000
        DATA_AT_REST = 60100
        DATA_DESTRUCTION = 60200
        TOR_EXIT_NODE = 60300
        MAIL_SPAM = 70000
        MAIL_PHISHING = 70100
        MAIL_SPOOFING = 70200
        POLICY_VIOLATION = 80000
        SOCIAL_ENGINEERING = 90001
        PHISHING = 90002

    class AlertState(proto.Enum):
        r"""The type of alerting set up for a security result.

        Values:
            UNSPECIFIED (0):
                The security result type is not known.
            NOT_ALERTING (1):
                The security result is not an alert.
            ALERTING (2):
                The security result is an alert.
        """

        UNSPECIFIED = 0
        NOT_ALERTING = 1
        ALERTING = 2

    class Action(proto.Enum):
        r"""Enum representing different possible actions taken by the product
        that created the event. Google SecOps classifies:

        - ALLOW and ALLOW_WITH_MODIFICATION actions as "successful".
        - BLOCK, QUARANTINE, FAIL, and CHALLENGE actions as "failed". This
          includes all corresponding metrics (for example,
          AUTH_ATTEMPTS_FAIL, FILE_EXECUTIONS_FAIL, RESOURCE_READ_FAIL, and
          so on).
        - UNKNOWN_ACTION actions as neither "successful" nor "failed",
          because, for example, logs might not provide information whether a
          login event occurred but some kind of "unknown" error was issued
          nonetheless.

        Values:
            UNKNOWN_ACTION (0):
                The default action.
            ALLOW (1):
                Allowed.
            BLOCK (2):
                Blocked.
            ALLOW_WITH_MODIFICATION (3):
                Strip, modify something
                (e.g. File or email was disinfected or rewritten
                and still forwarded).
            QUARANTINE (4):
                Put somewhere for later analysis (does NOT
                imply block).
            FAIL (5):
                Failed (e.g. the event was allowed but
                failed).
            CHALLENGE (6):
                Challenged (e.g. the user was challenged by a
                Captcha, 2FA).
        """

        UNKNOWN_ACTION = 0
        ALLOW = 1
        BLOCK = 2
        ALLOW_WITH_MODIFICATION = 3
        QUARANTINE = 4
        FAIL = 5
        CHALLENGE = 6

    class ProductSeverity(proto.Enum):
        r"""Defined by the product

        Values:
            UNKNOWN_SEVERITY (0):
                The default severity level.
            INFORMATIONAL (100):
                Info severity.
            ERROR (150):
                An error.
            NONE (101):
                No malicious result.
            LOW (200):
                Low-severity malicious result.
            MEDIUM (300):
                Medium-severity malicious result.
            HIGH (400):
                High-severity malicious result.
            CRITICAL (500):
                Critical-severity malicious result.
        """

        UNKNOWN_SEVERITY = 0
        INFORMATIONAL = 100
        ERROR = 150
        NONE = 101
        LOW = 200
        MEDIUM = 300
        HIGH = 400
        CRITICAL = 500

    class ProductConfidence(proto.Enum):
        r"""A level of confidence in the result.

        Values:
            UNKNOWN_CONFIDENCE (0):
                The default confidence level.
            LOW_CONFIDENCE (200):
                Low confidence.
            MEDIUM_CONFIDENCE (300):
                Medium confidence.
            HIGH_CONFIDENCE (400):
                High confidence.
        """

        UNKNOWN_CONFIDENCE = 0
        LOW_CONFIDENCE = 200
        MEDIUM_CONFIDENCE = 300
        HIGH_CONFIDENCE = 400

    class ProductPriority(proto.Enum):
        r"""A product priority level.

        Values:
            UNKNOWN_PRIORITY (0):
                Default priority level.
            LOW_PRIORITY (200):
                Low priority.
            MEDIUM_PRIORITY (300):
                Medium priority.
            HIGH_PRIORITY (400):
                High priority.
        """

        UNKNOWN_PRIORITY = 0
        LOW_PRIORITY = 200
        MEDIUM_PRIORITY = 300
        HIGH_PRIORITY = 400

    class ThreatStatus(proto.Enum):
        r"""Vendor-specific information about the status of a threat
        (ITW).

        Values:
            THREAT_STATUS_UNSPECIFIED (0):
                Default threat status
            ACTIVE (1):
                Active threat.
            CLEARED (2):
                Cleared threat.
            FALSE_POSITIVE (3):
                False positive.
        """

        THREAT_STATUS_UNSPECIFIED = 0
        ACTIVE = 1
        CLEARED = 2
        FALSE_POSITIVE = 3

    class ThreatCollectionType(proto.Enum):
        r"""Different Types of threat collections currently supported.

        Values:
            THREAT_COLLECTION_TYPE_UNSPECIFIED (0):
                Threat collection type is unspecified.
            CAMPAIGN (1):
                Threat collection type is campaign.
            REPORT (2):
                Threat collection type is report.
        """

        THREAT_COLLECTION_TYPE_UNSPECIFIED = 0
        CAMPAIGN = 1
        REPORT = 2

    class Association(proto.Message):
        r"""Associations represents different metadata about malware and
        threat actors involved with an IoC.

        Attributes:
            id (str):
                Unique association id generated by mandiant.
            country_code (MutableSequence[str]):
                Country from which the threat actor/ malware
                is originated.
            type_ (google.backstory.types.SecurityResult.Association.AssociationType):
                Signifies the type of association.
            name (str):
                Name of the threat actor/malware.
            description (str):
                Human readable description about the
                association.
            role (str):
                Role of the malware. Not applicable for
                threat actor.
            source_country (str):
                Name of the country the threat originated
                from.
            alias (MutableSequence[google.backstory.types.SecurityResult.Association.AssociationAlias]):
                Different aliases of the threat actor given
                by different sources.
            first_reference_time (google.protobuf.timestamp_pb2.Timestamp):
                First time the threat actor was referenced or
                seen.
            last_reference_time (google.protobuf.timestamp_pb2.Timestamp):
                Last time the threat actor was referenced or
                seen.
            industries_affected (MutableSequence[str]):
                List of industries the threat actor affects.
            associated_actors (MutableSequence[google.backstory.types.SecurityResult.Association]):
                List of associated threat actors for a
                malware. Not applicable for threat actors.
            region_code (google.backstory.types.Location):
                Name of the country, the threat is
                originating from.
            sponsor_region (google.backstory.types.Location):
                Sponsor region of the threat actor.
            targeted_regions (MutableSequence[google.backstory.types.Location]):
                Targeted regions.
            tags (MutableSequence[str]):
                Tags.
        """

        class AssociationType(proto.Enum):
            r"""Represents different possible Association types. Can be
            threat or malware. Used to represent Mandiant threat
            intelligence.

            Values:
                ASSOCIATION_TYPE_UNSPECIFIED (0):
                    The default Association Type.
                THREAT_ACTOR (1):
                    Association type Threat actor.
                MALWARE (2):
                    Association type Malware.
                SOFTWARE_TOOLKIT (3):
                    Association type Software toolkit.
            """

            ASSOCIATION_TYPE_UNSPECIFIED = 0
            THREAT_ACTOR = 1
            MALWARE = 2
            SOFTWARE_TOOLKIT = 3

        class AssociationAlias(proto.Message):
            r"""Association Alias used to represent Mandiant Threat
            Intelligence.

            Attributes:
                name (str):
                    Name of the alias.
                company (str):
                    Name of the provider who gave the
                    association's name.
            """

            name: str = proto.Field(
                proto.STRING,
                number=1,
            )
            company: str = proto.Field(
                proto.STRING,
                number=2,
            )

        id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        country_code: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        type_: "SecurityResult.Association.AssociationType" = proto.Field(
            proto.ENUM,
            number=3,
            enum="SecurityResult.Association.AssociationType",
        )
        name: str = proto.Field(
            proto.STRING,
            number=4,
        )
        description: str = proto.Field(
            proto.STRING,
            number=5,
        )
        role: str = proto.Field(
            proto.STRING,
            number=6,
        )
        source_country: str = proto.Field(
            proto.STRING,
            number=7,
        )
        alias: MutableSequence["SecurityResult.Association.AssociationAlias"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=8,
                message="SecurityResult.Association.AssociationAlias",
            )
        )
        first_reference_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=9,
            message=timestamp_pb2.Timestamp,
        )
        last_reference_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=10,
            message=timestamp_pb2.Timestamp,
        )
        industries_affected: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=11,
        )
        associated_actors: MutableSequence["SecurityResult.Association"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=12,
                message="SecurityResult.Association",
            )
        )
        region_code: "Location" = proto.Field(
            proto.MESSAGE,
            number=13,
            message="Location",
        )
        sponsor_region: "Location" = proto.Field(
            proto.MESSAGE,
            number=14,
            message="Location",
        )
        targeted_regions: MutableSequence["Location"] = proto.RepeatedField(
            proto.MESSAGE,
            number=15,
            message="Location",
        )
        tags: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=16,
        )

    class Source(proto.Message):
        r"""Deprecated.
        Information about the threat intelligence source. These fields
        are used to model Mandiant sources.

        Attributes:
            name (str):
                Name of the IoC source.
            benign_count (int):
                Count of responses where this IoC was marked
                benign.
            malicious_count (int):
                Count of responses where this IoC was marked
                malicious.
            quality (google.backstory.types.SecurityResult.ProductConfidence):
                Quality of the IoC mapping extracted from the
                source.
            response_count (int):
                Total response count from this source.
            source_count (int):
                Number of sources from which intelligence was
                extracted.
            threat_intelligence_sources (MutableSequence[google.backstory.types.SecurityResult.Source]):
                Different threat intelligence sources from
                which IoC info was extracted.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        benign_count: int = proto.Field(
            proto.INT32,
            number=2,
        )
        malicious_count: int = proto.Field(
            proto.INT32,
            number=3,
        )
        quality: "SecurityResult.ProductConfidence" = proto.Field(
            proto.ENUM,
            number=4,
            enum="SecurityResult.ProductConfidence",
        )
        response_count: int = proto.Field(
            proto.INT32,
            number=5,
        )
        source_count: int = proto.Field(
            proto.INT32,
            number=6,
        )
        threat_intelligence_sources: MutableSequence["SecurityResult.Source"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=7,
                message="SecurityResult.Source",
            )
        )

    class ProviderMLVerdict(proto.Message):
        r"""Deprecated.
        MLVerdict result provided from threat providers, like Mandiant.
        These fields are used to model Mandiant sources.

        Attributes:
            source_provider (str):
                Source provider giving the ML verdict.
            benign_count (int):
                Count of responses where this IoC was marked
                benign.
            malicious_count (int):
                Count of responses where this IoC was marked
                malicious.
            confidence_score (int):
                Confidence score of the verdict.
            mandiant_sources (MutableSequence[google.backstory.types.SecurityResult.Source]):
                List of mandiant sources from which the
                verdict was generated.
            third_party_sources (MutableSequence[google.backstory.types.SecurityResult.Source]):
                List of third-party sources from which the
                verdict was generated.
        """

        source_provider: str = proto.Field(
            proto.STRING,
            number=1,
        )
        benign_count: int = proto.Field(
            proto.INT32,
            number=2,
        )
        malicious_count: int = proto.Field(
            proto.INT32,
            number=3,
        )
        confidence_score: int = proto.Field(
            proto.INT32,
            number=4,
        )
        mandiant_sources: MutableSequence["SecurityResult.Source"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=5,
                message="SecurityResult.Source",
            )
        )
        third_party_sources: MutableSequence["SecurityResult.Source"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=6,
                message="SecurityResult.Source",
            )
        )

    class AnalystVerdict(proto.Message):
        r"""Verdict provided by the human analyst. These fields are used
        to model Mandiant sources.

        Attributes:
            confidence_score (int):
                Confidence score of the verdict.
            verdict_time (google.protobuf.timestamp_pb2.Timestamp):
                Timestamp at which the verdict was generated.
            verdict_response (google.backstory.types.SecurityResult.VerdictResponse):
                Details of the verdict.
        """

        confidence_score: int = proto.Field(
            proto.INT32,
            number=1,
        )
        verdict_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
        )
        verdict_response: "SecurityResult.VerdictResponse" = proto.Field(
            proto.ENUM,
            number=3,
            enum="SecurityResult.VerdictResponse",
        )

    class IoCStats(proto.Message):
        r"""Information about the threat intelligence source. These
        fields are used to model Mandiant sources.

        Attributes:
            ioc_stats_type (google.backstory.types.SecurityResult.IoCStatsType):
                Describes the source of the IoCStat.
            first_level_source (str):
                Name of first level IoC source, for example
                Mandiant or a third-party.
            second_level_source (str):
                Name of the second-level IoC source, for
                example Crowdsourced Threat Analysis or
                Knowledge Graph.
            benign_count (int):
                Count of responses where the IoC was
                identified as benign.
            quality (google.backstory.types.SecurityResult.ProductConfidence):
                Level of confidence in the IoC mapping
                extracted from the source.
            malicious_count (int):
                Count of responses where the IoC was
                identified as malicious.
            response_count (int):
                Total number of response from the source.
            source_count (int):
                Number of sources from which information was
                extracted.
        """

        ioc_stats_type: "SecurityResult.IoCStatsType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="SecurityResult.IoCStatsType",
        )
        first_level_source: str = proto.Field(
            proto.STRING,
            number=2,
        )
        second_level_source: str = proto.Field(
            proto.STRING,
            number=3,
        )
        benign_count: int = proto.Field(
            proto.INT32,
            number=4,
        )
        quality: "SecurityResult.ProductConfidence" = proto.Field(
            proto.ENUM,
            number=5,
            enum="SecurityResult.ProductConfidence",
        )
        malicious_count: int = proto.Field(
            proto.INT32,
            number=6,
        )
        response_count: int = proto.Field(
            proto.INT32,
            number=7,
        )
        source_count: int = proto.Field(
            proto.INT32,
            number=8,
        )

    class VerdictInfo(proto.Message):
        r"""Describes the threat verdict provided by human analysts and
        machine learning models. These fields are used to model Mandiant
        sources.

        Attributes:
            source_count (int):
                Number of sources from which intelligence was
                extracted.
            response_count (int):
                Total response count across all sources.
            neighbour_influence (str):
                Describes the near neighbor influence of the
                verdict.
            verdict_type (google.backstory.types.SecurityResult.VerdictType):
                Type of verdict.
            source_provider (str):
                Source provider giving the machine learning
                verdict.
            benign_count (int):
                Count of responses where this IoC was marked
                as benign.
            malicious_count (int):
                Count of responses where this IoC was marked
                as malicious.
            confidence_score (int):
                Confidence score of the verdict.
            ioc_stats (MutableSequence[google.backstory.types.SecurityResult.IoCStats]):
                List of IoCStats from which the verdict was
                generated.
            verdict_time (google.protobuf.timestamp_pb2.Timestamp):
                Timestamp when the verdict was generated.
            verdict_response (google.backstory.types.SecurityResult.VerdictResponse):
                Details about the verdict.
            global_customer_count (int):
                Global customer count over the last 30 days
            global_hits_count (int):
                Global hit count over the last 30 days.
            pwn (bool):
                Whether one or more Mandiant incident
                response customers had this indicator in their
                environment.
            category_details (str):
                Tags related to the verdict.
            pwn_first_tagged_time (google.protobuf.timestamp_pb2.Timestamp):
                The timestamp of the first time a pwn was
                associated to this entity.
        """

        source_count: int = proto.Field(
            proto.INT32,
            number=1,
        )
        response_count: int = proto.Field(
            proto.INT32,
            number=2,
        )
        neighbour_influence: str = proto.Field(
            proto.STRING,
            number=3,
        )
        verdict_type: "SecurityResult.VerdictType" = proto.Field(
            proto.ENUM,
            number=4,
            enum="SecurityResult.VerdictType",
        )
        source_provider: str = proto.Field(
            proto.STRING,
            number=5,
        )
        benign_count: int = proto.Field(
            proto.INT32,
            number=6,
        )
        malicious_count: int = proto.Field(
            proto.INT32,
            number=7,
        )
        confidence_score: int = proto.Field(
            proto.INT32,
            number=8,
        )
        ioc_stats: MutableSequence["SecurityResult.IoCStats"] = proto.RepeatedField(
            proto.MESSAGE,
            number=9,
            message="SecurityResult.IoCStats",
        )
        verdict_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=11,
            message=timestamp_pb2.Timestamp,
        )
        verdict_response: "SecurityResult.VerdictResponse" = proto.Field(
            proto.ENUM,
            number=12,
            enum="SecurityResult.VerdictResponse",
        )
        global_customer_count: int = proto.Field(
            proto.INT32,
            number=13,
        )
        global_hits_count: int = proto.Field(
            proto.INT32,
            number=14,
        )
        pwn: bool = proto.Field(
            proto.BOOL,
            number=15,
        )
        category_details: str = proto.Field(
            proto.STRING,
            number=16,
        )
        pwn_first_tagged_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=17,
            message=timestamp_pb2.Timestamp,
        )

    class Verdict(proto.Message):
        r"""Deprecated.
        Encapsulates the threat verdict provided by human analysts and
        ML models. These fields are used to model Mandiant sources.

        Attributes:
            source_count (int):
                Number of sources from which intelligence was
                extracted.
            response_count (int):
                Total response count across all sources.
            neighbour_influence (str):
                Describes the neighbour influence of the
                verdict.
            verdict (google.backstory.types.SecurityResult.ProviderMLVerdict):
                ML Verdict provided by sources like Mandiant.
            analyst_verdict (google.backstory.types.SecurityResult.AnalystVerdict):
                Human analyst verdict provided by sources
                like Mandiant.
        """

        source_count: int = proto.Field(
            proto.INT32,
            number=1,
        )
        response_count: int = proto.Field(
            proto.INT32,
            number=2,
        )
        neighbour_influence: str = proto.Field(
            proto.STRING,
            number=3,
        )
        verdict: "SecurityResult.ProviderMLVerdict" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="SecurityResult.ProviderMLVerdict",
        )
        analyst_verdict: "SecurityResult.AnalystVerdict" = proto.Field(
            proto.MESSAGE,
            number=5,
            message="SecurityResult.AnalystVerdict",
        )

    class ThreatCollectionItem(proto.Message):
        r"""Threat Collection that is either a threat campaign or a
        threat report.

        Attributes:
            id (str):
                The ID of the threat collection.
            type_ (google.backstory.types.SecurityResult.ThreatCollectionType):
                The type of threat collection (e.g.,
                "campaign").
            alt_names (MutableSequence[str]):
                The name of the threat collection.
        """

        id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        type_: "SecurityResult.ThreatCollectionType" = proto.Field(
            proto.ENUM,
            number=2,
            enum="SecurityResult.ThreatCollectionType",
        )
        alt_names: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )

    about: "Noun" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Noun",
    )
    category: MutableSequence[SecurityCategory] = proto.RepeatedField(
        proto.ENUM,
        number=2,
        enum=SecurityCategory,
    )
    category_details: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    threat_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    rule_set: str = proto.Field(
        proto.STRING,
        number=29,
    )
    rule_set_display_name: str = proto.Field(
        proto.STRING,
        number=30,
    )
    ruleset_category_display_name: str = proto.Field(
        proto.STRING,
        number=41,
    )
    rule_id: str = proto.Field(
        proto.STRING,
        number=16,
    )
    rule_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=49,
    )
    rule_version: str = proto.Field(
        proto.STRING,
        number=20,
    )
    rule_type: str = proto.Field(
        proto.STRING,
        number=22,
    )
    rule_author: str = proto.Field(
        proto.STRING,
        number=25,
    )
    rule_labels: MutableSequence["Label"] = proto.RepeatedField(
        proto.MESSAGE,
        number=26,
        message="Label",
    )
    alert_state: AlertState = proto.Field(
        proto.ENUM,
        number=21,
        enum=AlertState,
    )
    detection_fields: MutableSequence["Label"] = proto.RepeatedField(
        proto.MESSAGE,
        number=23,
        message="Label",
    )
    outcomes: MutableSequence["Label"] = proto.RepeatedField(
        proto.MESSAGE,
        number=28,
        message="Label",
    )
    variables: MutableMapping[str, "FindingVariable"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=44,
        message="FindingVariable",
    )
    summary: str = proto.Field(
        proto.STRING,
        number=6,
    )
    description: str = proto.Field(
        proto.STRING,
        number=7,
    )
    action: MutableSequence[Action] = proto.RepeatedField(
        proto.ENUM,
        number=8,
        enum=Action,
    )
    action_details: str = proto.Field(
        proto.STRING,
        number=19,
    )
    severity: ProductSeverity = proto.Field(
        proto.ENUM,
        number=9,
        enum=ProductSeverity,
    )
    confidence: ProductConfidence = proto.Field(
        proto.ENUM,
        number=10,
        enum=ProductConfidence,
    )
    priority: ProductPriority = proto.Field(
        proto.ENUM,
        number=11,
        enum=ProductPriority,
    )
    risk_score: float = proto.Field(
        proto.FLOAT,
        number=31,
    )
    confidence_score: float = proto.Field(
        proto.FLOAT,
        number=42,
    )
    analytics_metadata: MutableSequence["AnalyticsMetadata"] = proto.RepeatedField(
        proto.MESSAGE,
        number=43,
        message="AnalyticsMetadata",
    )
    severity_details: str = proto.Field(
        proto.STRING,
        number=12,
    )
    confidence_details: str = proto.Field(
        proto.STRING,
        number=13,
    )
    priority_details: str = proto.Field(
        proto.STRING,
        number=14,
    )
    url_back_to_product: str = proto.Field(
        proto.STRING,
        number=15,
    )
    threat_id: str = proto.Field(
        proto.STRING,
        number=17,
    )
    threat_feed_name: str = proto.Field(
        proto.STRING,
        number=27,
    )
    threat_id_namespace: gb_id.Id.Namespace = proto.Field(
        proto.ENUM,
        number=24,
        enum=gb_id.Id.Namespace,
    )
    threat_status: ThreatStatus = proto.Field(
        proto.ENUM,
        number=18,
        enum=ThreatStatus,
    )
    attack_details: "AttackDetails" = proto.Field(
        proto.MESSAGE,
        number=32,
        message="AttackDetails",
    )
    first_discovered_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=33,
        message=timestamp_pb2.Timestamp,
    )
    associations: MutableSequence[Association] = proto.RepeatedField(
        proto.MESSAGE,
        number=34,
        message=Association,
    )
    campaigns: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=35,
    )
    reports: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=46,
    )
    verdict: Verdict = proto.Field(
        proto.MESSAGE,
        number=36,
        message=Verdict,
    )
    last_updated_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=37,
        message=timestamp_pb2.Timestamp,
    )
    verdict_info: MutableSequence[VerdictInfo] = proto.RepeatedField(
        proto.MESSAGE,
        number=38,
        message=VerdictInfo,
    )
    threat_verdict: "ThreatVerdict" = proto.Field(
        proto.ENUM,
        number=39,
        enum="ThreatVerdict",
    )
    last_discovered_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=40,
        message=timestamp_pb2.Timestamp,
    )
    detection_depth: int = proto.Field(
        proto.INT64,
        number=47,
    )
    threat_collections: MutableSequence[ThreatCollectionItem] = proto.RepeatedField(
        proto.MESSAGE,
        number=48,
        message=ThreatCollectionItem,
    )


class PeFileMetadata(proto.Message):
    r"""Metadata about a Microsoft Windows Portable Executable.

    Attributes:
        import_hash (str):
            Hash of PE imports.
    """

    import_hash: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FileMetadata(proto.Message):
    r"""Metadata about a file.
    Place metadata about different file types here, for example data
    from the Microsoft Windows VersionInfo block or digital signer
    details. Use a different sub-message per file type.

    Attributes:
        pe (google.backstory.types.PeFileMetadata):
            Metadata for Microsoft Windows PE files.
            Deprecate PeFileMetadata in favor of single File
            proto.
    """

    pe: "PeFileMetadata" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="PeFileMetadata",
    )


class File(proto.Message):
    r"""Information about a file.

    Attributes:
        sha256 (str):
            The SHA256 hash of the file, as a hex-encoded
            string. This field can be used as an entity
            indicator for file entities.
        md5 (str):
            The MD5 hash of the file, as a hex-encoded
            string. This field can be used as an entity
            indicator for file entities.
        sha1 (str):
            The SHA1 hash of the file, as a hex-encoded
            string. This field can be used as an entity
            indicator for file entities.
        size (int):
            The size of the file in bytes.
        full_path (str):
            The full path identifying the location of the
            file on the system. This field can be used as an
            entity indicator for file entities.
        mime_type (str):
            The MIME (Multipurpose Internet Mail
            Extensions) type of the file, for example "PE",
            "PDF", or "powershell script".
        file_metadata (google.backstory.types.FileMetadata):
            Metadata associated with the file.
            Deprecate FileMetadata in favor of using fields
            in File.
        security_result (google.backstory.types.SecurityResult):
            Google Cloud Threat Intelligence (GCTI)
            security result for the file including threat
            context and detection metadata.
        pe_file (google.backstory.types.FileMetadataPE):
            Metadata about the Portable Executable (PE)
            file.
        ssdeep (str):
            Ssdeep of the file
        vhash (str):
            Vhash of the file.
        ahash (str):
            Deprecated. Use authentihash instead.
        authentihash (str):
            Authentihash of the file.
        symhash (str):
            SymHash of the file. Used for Mach-O (e.g.
            MacOS) binaries, to identify similar files based
            on their symbol table.
        prefetch_file_metadata (google.backstory.types.PrefetchFileMetadata):
            Metadata about the prefetch file.
        file_type (google.backstory.types.File.FileType):
            FileType field.
        capabilities_tags (MutableSequence[str]):
            Capabilities tags.
        names (MutableSequence[str]):
            Names fields.
        tags (MutableSequence[str]):
            Tags for the file.
        last_modification_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp when the file was last updated.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp when the file was created.
        last_access_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp when the file was accessed.
        prevalence (google.backstory.types.Prevalence):
            Prevalence of the file hash in the customer's
            environment.
        first_seen_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp the file was first seen in the
            customer's environment.
        last_seen_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp the file was last seen in the
            customer's environment.
        stat_mode (int):
            The mode of the file. A bit string indicating
            the permissions and privileges of the file.
        stat_inode (int):
            The file identifier. Unique identifier of
            object within a file system.
        stat_dev (int):
            The file system identifier to which the
            object belongs.
        stat_nlink (int):
            Number of links to file.
        stat_flags (int):
            User defined flags for file.
        last_analysis_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp the file was last analysed.
        embedded_urls (MutableSequence[str]):
            Embedded urls found in the file.
        embedded_domains (MutableSequence[str]):
            Embedded domains found in the file.
        embedded_ips (MutableSequence[str]):
            Embedded IP addresses found in the file.
        exif_info (google.backstory.types.ExifInfo):
            Exif metadata from different file formats
            extracted by exiftool.
        signature_info (google.backstory.types.SignatureInfo):
            File signature information extracted from
            different tools.
        pdf_info (google.backstory.types.PDFInfo):
            Information about the PDF file structure.
        first_submission_time (google.protobuf.timestamp_pb2.Timestamp):
            First submission time of the file.
        last_submission_time (google.protobuf.timestamp_pb2.Timestamp):
            Last submission time of the file.
        main_icon (google.backstory.types.Favicon):
            Icon's relevant hashes.
        ntfs (google.backstory.types.NtfsFileMetadata):
            NTFS metadata.
        app_compat_cache (google.backstory.types.AppCompatMetadata):
            Windows AppCompatCache (Application
            Compatibility) metadata.
    """

    class FileType(proto.Enum):
        r"""The file type, for example Microsoft Windows executable.

        Values:
            FILE_TYPE_UNSPECIFIED (0):
                File type is UNSPECIFIED.
            FILE_TYPE_PE_EXE (1):
                File type is PE_EXE.
            FILE_TYPE_PE_DLL (2):
                Although DLLs are actually portable executables, this value
                enables the file type to be identified separately. File type
                is PE_DLL.
            FILE_TYPE_MSI (3):
                File type is MSI.
            FILE_TYPE_NE_EXE (10):
                File type is NE_EXE.
            FILE_TYPE_NE_DLL (11):
                File type is NE_DLL.
            FILE_TYPE_DOS_EXE (20):
                File type is DOS_EXE.
            FILE_TYPE_DOS_COM (21):
                File type is DOS_COM.
            FILE_TYPE_COFF (30):
                File type is COFF.
            FILE_TYPE_ELF (31):
                File type is ELF.
            FILE_TYPE_LINUX_KERNEL (32):
                File type is LINUX_KERNEL.
            FILE_TYPE_RPM (33):
                File type is RPM.
            FILE_TYPE_LINUX (34):
                File type is LINUX.
            FILE_TYPE_MACH_O (35):
                File type is MACH_O.
            FILE_TYPE_JAVA_BYTECODE (36):
                File type is JAVA_BYTECODE.
            FILE_TYPE_DMG (37):
                File type is DMG.
            FILE_TYPE_DEB (38):
                File type is DEB.
            FILE_TYPE_PKG (39):
                File type is PKG.
            FILE_TYPE_PYC (40):
                File type is PYC.
            FILE_TYPE_LNK (50):
                File type is LNK.
            FILE_TYPE_DESKTOP_ENTRY (51):
                File type is DESKTOP_ENTRY.
            FILE_TYPE_JPEG (100):
                File type is JPEG.
            FILE_TYPE_TIFF (101):
                File type is TIFF.
            FILE_TYPE_GIF (102):
                File type is GIF.
            FILE_TYPE_PNG (103):
                File type is PNG.
            FILE_TYPE_BMP (104):
                File type is BMP.
            FILE_TYPE_GIMP (105):
                File type is GIMP.
            FILE_TYPE_IN_DESIGN (106):
                File type is Adobe InDesign.
            FILE_TYPE_PSD (107):
                File type is PSD.
                Adobe Photoshop.
            FILE_TYPE_TARGA (108):
                File type is TARGA.
            FILE_TYPE_XWD (109):
                File type is XWD.
            FILE_TYPE_DIB (110):
                File type is DIB.
            FILE_TYPE_JNG (111):
                File type is JNG.
            FILE_TYPE_ICO (112):
                File type is ICO.
            FILE_TYPE_FPX (113):
                File type is FPX.
            FILE_TYPE_EPS (114):
                File type is EPS.
            FILE_TYPE_SVG (115):
                File type is SVG.
            FILE_TYPE_EMF (116):
                File type is EMF.
            FILE_TYPE_WEBP (117):
                File type is WEBP.
            FILE_TYPE_DWG (118):
                File type is DWG.
            FILE_TYPE_DXF (119):
                File type is DXF.
            FILE_TYPE_THREEDS (120):
                File type is 3DS.
            FILE_TYPE_OGG (150):
                File type is OGG.
            FILE_TYPE_FLC (151):
                File type is FLC.
            FILE_TYPE_FLI (152):
                File type is FLI.
            FILE_TYPE_MP3 (153):
                File type is MP3.
            FILE_TYPE_FLAC (154):
                File type is FLAC.
            FILE_TYPE_WAV (155):
                File type is WAV.
            FILE_TYPE_MIDI (156):
                File type is MIDI.
            FILE_TYPE_AVI (157):
                File type is AVI.
            FILE_TYPE_MPEG (158):
                File type is MPEG.
            FILE_TYPE_QUICKTIME (159):
                File type is QUICKTIME.
            FILE_TYPE_ASF (160):
                File type is ASF.
            FILE_TYPE_DIVX (161):
                File type is DIVX.
            FILE_TYPE_FLV (162):
                File type is FLV.
            FILE_TYPE_WMA (163):
                File type is WMA.
            FILE_TYPE_WMV (164):
                File type is WMV.
            FILE_TYPE_RM (165):
                File type is RM.
                RealMedia type.
            FILE_TYPE_MOV (166):
                File type is MOV.
            FILE_TYPE_MP4 (167):
                File type is MP4.
            FILE_TYPE_T3GP (168):
                File type is T3GP.
            FILE_TYPE_WEBM (169):
                File type is WEBM.
            FILE_TYPE_MKV (170):
                File type is MKV.
            FILE_TYPE_PDF (200):
                File type is PDF.
            FILE_TYPE_PS (201):
                File type is PS.
            FILE_TYPE_DOC (202):
                File type is DOC.
            FILE_TYPE_DOCX (203):
                File type is DOCX.
            FILE_TYPE_PPT (204):
                File type is PPT.
            FILE_TYPE_PPTX (205):
                File type is PPTX.
            FILE_TYPE_XLS (206):
                File type is XLS.
            FILE_TYPE_XLSX (207):
                File type is XLSX.
            FILE_TYPE_RTF (208):
                File type is RTF.
            FILE_TYPE_PPSX (209):
                File type is PPSX.
            FILE_TYPE_ODP (250):
                File type is ODP.
            FILE_TYPE_ODS (251):
                File type is ODS.
            FILE_TYPE_ODT (252):
                File type is ODT.
            FILE_TYPE_HWP (253):
                File type is HWP.
            FILE_TYPE_GUL (254):
                File type is GUL.
            FILE_TYPE_ODF (255):
                File type is ODF.
            FILE_TYPE_ODG (256):
                File type is ODG.
            FILE_TYPE_ONE_NOTE (257):
                File type is ONE_NOTE.
            FILE_TYPE_OOXML (258):
                File type is OOXML.
            FILE_TYPE_SLK (259):
                File type is SLK.
            FILE_TYPE_EBOOK (260):
                File type is EBOOK.
            FILE_TYPE_LATEX (261):
                File type is LATEX.
            FILE_TYPE_TTF (262):
                File type is TTF.
            FILE_TYPE_EOT (263):
                File type is EOT.
            FILE_TYPE_WOFF (264):
                File type is WOFF.
            FILE_TYPE_CHM (265):
                File type is CHM.
            FILE_TYPE_ZIP (300):
                File type is ZIP.
            FILE_TYPE_GZIP (301):
                File type is GZIP.
            FILE_TYPE_BZIP (302):
                File type is BZIP.
            FILE_TYPE_RZIP (303):
                File type is RZIP.
            FILE_TYPE_DZIP (304):
                File type is DZIP.
            FILE_TYPE_SEVENZIP (305):
                File type is SEVENZIP.
            FILE_TYPE_CAB (306):
                File type is CAB.
            FILE_TYPE_JAR (307):
                File type is JAR.
            FILE_TYPE_RAR (308):
                File type is RAR.
            FILE_TYPE_MSCOMPRESS (309):
                File type is MSCOMPRESS.
            FILE_TYPE_ACE (310):
                File type is ACE.
            FILE_TYPE_ARC (311):
                File type is ARC.
            FILE_TYPE_ARJ (312):
                File type is ARJ.
            FILE_TYPE_ASD (313):
                File type is ASD.
            FILE_TYPE_BLACKHOLE (314):
                File type is BLACKHOLE.
            FILE_TYPE_KGB (315):
                File type is KGB.
            FILE_TYPE_ZLIB (316):
                File type is ZLIB.
            FILE_TYPE_TAR (317):
                File type is TAR.
            FILE_TYPE_ZST (318):
                File type is ZST.
            FILE_TYPE_LZFSE (319):
                File type is LZFSE.
            FILE_TYPE_PYTHON_WHL (320):
                File type is PYTHON_WHL.
            FILE_TYPE_PYTHON_PKG (321):
                File type is PYTHON_PKG.
            FILE_TYPE_MSIX (322):
                File type is MSIX, new Windows app package
                format.
            FILE_TYPE_TEXT (400):
                File type is TEXT.
            FILE_TYPE_SCRIPT (401):
                File type is SCRIPT.
            FILE_TYPE_PHP (402):
                File type is PHP.
            FILE_TYPE_PYTHON (403):
                File type is PYTHON.
            FILE_TYPE_PERL (404):
                File type is PERL.
            FILE_TYPE_RUBY (405):
                File type is RUBY.
            FILE_TYPE_C (406):
                File type is C.
            FILE_TYPE_CPP (407):
                File type is CPP.
            FILE_TYPE_JAVA (408):
                File type is JAVA.
            FILE_TYPE_SHELLSCRIPT (409):
                File type is SHELLSCRIPT.
            FILE_TYPE_PASCAL (410):
                File type is PASCAL.
            FILE_TYPE_AWK (411):
                File type is AWK.
            FILE_TYPE_DYALOG (412):
                File type is DYALOG.
            FILE_TYPE_FORTRAN (413):
                File type is FORTRAN.
            FILE_TYPE_JAVASCRIPT (414):
                File type is JAVASCRIPT.
            FILE_TYPE_POWERSHELL (415):
                File type is POWERSHELL.
            FILE_TYPE_VBA (416):
                File type is VBA.
            FILE_TYPE_M4 (417):
                File type is M4.
            FILE_TYPE_OBJETIVEC (418):
                File type is OBJETIVEC.
            FILE_TYPE_JMOD (419):
                File type is JMOD.
            FILE_TYPE_MAKEFILE (420):
                File type is MAKEFILE.
            FILE_TYPE_INI (421):
                File type is INI.
            FILE_TYPE_CLJ (422):
                File type is CLJ.
            FILE_TYPE_PDB (425):
                File type is PDB.
            FILE_TYPE_SQL (426):
                File type is SQL.
            FILE_TYPE_NEKO (427):
                File type is NEKO.
            FILE_TYPE_WER (428):
                File type is WER.
            FILE_TYPE_GOLANG (429):
                File type is GOLANG.
            FILE_TYPE_M3U (430):
                File type is M3U.
            FILE_TYPE_BAT (431):
                File type is BAT, Windows .bat/.cmd (old
                files are tagged as SHELLSCRIPT).
            FILE_TYPE_MSC (432):
                File type is MSC, Microsoft Management
                Console (MMC).
            FILE_TYPE_RDP (433):
                File type is RDP, Microsoft Remote Desktop
                Protocol (RDP) file.
            FILE_TYPE_SYMBIAN (500):
                File type is SYMBIAN.
            FILE_TYPE_PALMOS (501):
                File type is PALMOS.
            FILE_TYPE_WINCE (502):
                File type is WINCE.
            FILE_TYPE_ANDROID (503):
                File type is ANDROID.
            FILE_TYPE_IPHONE (504):
                File type is IPHONE.
            FILE_TYPE_HTML (600):
                File type is HTML.
            FILE_TYPE_XML (601):
                File type is XML.
            FILE_TYPE_SWF (602):
                File type is SWF.
            FILE_TYPE_FLA (603):
                File type is FLA.
            FILE_TYPE_COOKIE (604):
                File type is COOKIE.
            FILE_TYPE_TORRENT (605):
                File type is TORRENT.
            FILE_TYPE_EMAIL_TYPE (606):
                File type is EMAIL_TYPE.
            FILE_TYPE_OUTLOOK (607):
                File type is OUTLOOK.
            FILE_TYPE_SGML (608):
                File type is SGML.
            FILE_TYPE_JSON (609):
                File type is JSON.
            FILE_TYPE_CSV (610):
                File type is CSV.
            FILE_TYPE_HTA (611):
                File type is HTA (HTML Application).
            FILE_TYPE_INTERNET_SHORTCUT (612):
                File type is MSHTML .url.
            FILE_TYPE_CAP (700):
                File type is CAP.
            FILE_TYPE_ISOIMAGE (800):
                File type is ISOIMAGE.
            FILE_TYPE_SQUASHFS (801):
                File type is SQUASHFS.
            FILE_TYPE_VHD (802):
                File type is VHD.
            FILE_TYPE_APPLE (1000):
                File type is APPLE.
            FILE_TYPE_MACINTOSH (1001):
                File type is MACINTOSH.
            FILE_TYPE_APPLESINGLE (1002):
                File type is APPLESINGLE.
            FILE_TYPE_APPLEDOUBLE (1003):
                File type is APPLEDOUBLE.
            FILE_TYPE_MACINTOSH_HFS (1004):
                File type is MACINTOSH_HFS.
            FILE_TYPE_APPLE_PLIST (1005):
                File type is APPLE_PLIST.
            FILE_TYPE_MACINTOSH_LIB (1006):
                File type is MACINTOSH_LIB.
            FILE_TYPE_APPLESCRIPT (1007):
                File type is APPLESCRIPT.
            FILE_TYPE_APPLESCRIPT_COMPILED (1008):
                File type is APPLESCRIPT_COMPILED .
            FILE_TYPE_CRX (1100):
                File type is CRX.
            FILE_TYPE_XPI (1101):
                File type is XPI.
            FILE_TYPE_ROM (1200):
                File type is ROM.
            FILE_TYPE_IPS (1201):
                File type is IPS.
            FILE_TYPE_PEM (1300):
                File type is PEM.
            FILE_TYPE_PGP (1301):
                File type is PGP.
            FILE_TYPE_CRT (1302):
                File type is CRT.
        """

        FILE_TYPE_UNSPECIFIED = 0
        FILE_TYPE_PE_EXE = 1
        FILE_TYPE_PE_DLL = 2
        FILE_TYPE_MSI = 3
        FILE_TYPE_NE_EXE = 10
        FILE_TYPE_NE_DLL = 11
        FILE_TYPE_DOS_EXE = 20
        FILE_TYPE_DOS_COM = 21
        FILE_TYPE_COFF = 30
        FILE_TYPE_ELF = 31
        FILE_TYPE_LINUX_KERNEL = 32
        FILE_TYPE_RPM = 33
        FILE_TYPE_LINUX = 34
        FILE_TYPE_MACH_O = 35
        FILE_TYPE_JAVA_BYTECODE = 36
        FILE_TYPE_DMG = 37
        FILE_TYPE_DEB = 38
        FILE_TYPE_PKG = 39
        FILE_TYPE_PYC = 40
        FILE_TYPE_LNK = 50
        FILE_TYPE_DESKTOP_ENTRY = 51
        FILE_TYPE_JPEG = 100
        FILE_TYPE_TIFF = 101
        FILE_TYPE_GIF = 102
        FILE_TYPE_PNG = 103
        FILE_TYPE_BMP = 104
        FILE_TYPE_GIMP = 105
        FILE_TYPE_IN_DESIGN = 106
        FILE_TYPE_PSD = 107
        FILE_TYPE_TARGA = 108
        FILE_TYPE_XWD = 109
        FILE_TYPE_DIB = 110
        FILE_TYPE_JNG = 111
        FILE_TYPE_ICO = 112
        FILE_TYPE_FPX = 113
        FILE_TYPE_EPS = 114
        FILE_TYPE_SVG = 115
        FILE_TYPE_EMF = 116
        FILE_TYPE_WEBP = 117
        FILE_TYPE_DWG = 118
        FILE_TYPE_DXF = 119
        FILE_TYPE_THREEDS = 120
        FILE_TYPE_OGG = 150
        FILE_TYPE_FLC = 151
        FILE_TYPE_FLI = 152
        FILE_TYPE_MP3 = 153
        FILE_TYPE_FLAC = 154
        FILE_TYPE_WAV = 155
        FILE_TYPE_MIDI = 156
        FILE_TYPE_AVI = 157
        FILE_TYPE_MPEG = 158
        FILE_TYPE_QUICKTIME = 159
        FILE_TYPE_ASF = 160
        FILE_TYPE_DIVX = 161
        FILE_TYPE_FLV = 162
        FILE_TYPE_WMA = 163
        FILE_TYPE_WMV = 164
        FILE_TYPE_RM = 165
        FILE_TYPE_MOV = 166
        FILE_TYPE_MP4 = 167
        FILE_TYPE_T3GP = 168
        FILE_TYPE_WEBM = 169
        FILE_TYPE_MKV = 170
        FILE_TYPE_PDF = 200
        FILE_TYPE_PS = 201
        FILE_TYPE_DOC = 202
        FILE_TYPE_DOCX = 203
        FILE_TYPE_PPT = 204
        FILE_TYPE_PPTX = 205
        FILE_TYPE_XLS = 206
        FILE_TYPE_XLSX = 207
        FILE_TYPE_RTF = 208
        FILE_TYPE_PPSX = 209
        FILE_TYPE_ODP = 250
        FILE_TYPE_ODS = 251
        FILE_TYPE_ODT = 252
        FILE_TYPE_HWP = 253
        FILE_TYPE_GUL = 254
        FILE_TYPE_ODF = 255
        FILE_TYPE_ODG = 256
        FILE_TYPE_ONE_NOTE = 257
        FILE_TYPE_OOXML = 258
        FILE_TYPE_SLK = 259
        FILE_TYPE_EBOOK = 260
        FILE_TYPE_LATEX = 261
        FILE_TYPE_TTF = 262
        FILE_TYPE_EOT = 263
        FILE_TYPE_WOFF = 264
        FILE_TYPE_CHM = 265
        FILE_TYPE_ZIP = 300
        FILE_TYPE_GZIP = 301
        FILE_TYPE_BZIP = 302
        FILE_TYPE_RZIP = 303
        FILE_TYPE_DZIP = 304
        FILE_TYPE_SEVENZIP = 305
        FILE_TYPE_CAB = 306
        FILE_TYPE_JAR = 307
        FILE_TYPE_RAR = 308
        FILE_TYPE_MSCOMPRESS = 309
        FILE_TYPE_ACE = 310
        FILE_TYPE_ARC = 311
        FILE_TYPE_ARJ = 312
        FILE_TYPE_ASD = 313
        FILE_TYPE_BLACKHOLE = 314
        FILE_TYPE_KGB = 315
        FILE_TYPE_ZLIB = 316
        FILE_TYPE_TAR = 317
        FILE_TYPE_ZST = 318
        FILE_TYPE_LZFSE = 319
        FILE_TYPE_PYTHON_WHL = 320
        FILE_TYPE_PYTHON_PKG = 321
        FILE_TYPE_MSIX = 322
        FILE_TYPE_TEXT = 400
        FILE_TYPE_SCRIPT = 401
        FILE_TYPE_PHP = 402
        FILE_TYPE_PYTHON = 403
        FILE_TYPE_PERL = 404
        FILE_TYPE_RUBY = 405
        FILE_TYPE_C = 406
        FILE_TYPE_CPP = 407
        FILE_TYPE_JAVA = 408
        FILE_TYPE_SHELLSCRIPT = 409
        FILE_TYPE_PASCAL = 410
        FILE_TYPE_AWK = 411
        FILE_TYPE_DYALOG = 412
        FILE_TYPE_FORTRAN = 413
        FILE_TYPE_JAVASCRIPT = 414
        FILE_TYPE_POWERSHELL = 415
        FILE_TYPE_VBA = 416
        FILE_TYPE_M4 = 417
        FILE_TYPE_OBJETIVEC = 418
        FILE_TYPE_JMOD = 419
        FILE_TYPE_MAKEFILE = 420
        FILE_TYPE_INI = 421
        FILE_TYPE_CLJ = 422
        FILE_TYPE_PDB = 425
        FILE_TYPE_SQL = 426
        FILE_TYPE_NEKO = 427
        FILE_TYPE_WER = 428
        FILE_TYPE_GOLANG = 429
        FILE_TYPE_M3U = 430
        FILE_TYPE_BAT = 431
        FILE_TYPE_MSC = 432
        FILE_TYPE_RDP = 433
        FILE_TYPE_SYMBIAN = 500
        FILE_TYPE_PALMOS = 501
        FILE_TYPE_WINCE = 502
        FILE_TYPE_ANDROID = 503
        FILE_TYPE_IPHONE = 504
        FILE_TYPE_HTML = 600
        FILE_TYPE_XML = 601
        FILE_TYPE_SWF = 602
        FILE_TYPE_FLA = 603
        FILE_TYPE_COOKIE = 604
        FILE_TYPE_TORRENT = 605
        FILE_TYPE_EMAIL_TYPE = 606
        FILE_TYPE_OUTLOOK = 607
        FILE_TYPE_SGML = 608
        FILE_TYPE_JSON = 609
        FILE_TYPE_CSV = 610
        FILE_TYPE_HTA = 611
        FILE_TYPE_INTERNET_SHORTCUT = 612
        FILE_TYPE_CAP = 700
        FILE_TYPE_ISOIMAGE = 800
        FILE_TYPE_SQUASHFS = 801
        FILE_TYPE_VHD = 802
        FILE_TYPE_APPLE = 1000
        FILE_TYPE_MACINTOSH = 1001
        FILE_TYPE_APPLESINGLE = 1002
        FILE_TYPE_APPLEDOUBLE = 1003
        FILE_TYPE_MACINTOSH_HFS = 1004
        FILE_TYPE_APPLE_PLIST = 1005
        FILE_TYPE_MACINTOSH_LIB = 1006
        FILE_TYPE_APPLESCRIPT = 1007
        FILE_TYPE_APPLESCRIPT_COMPILED = 1008
        FILE_TYPE_CRX = 1100
        FILE_TYPE_XPI = 1101
        FILE_TYPE_ROM = 1200
        FILE_TYPE_IPS = 1201
        FILE_TYPE_PEM = 1300
        FILE_TYPE_PGP = 1301
        FILE_TYPE_CRT = 1302

    sha256: str = proto.Field(
        proto.STRING,
        number=1,
    )
    md5: str = proto.Field(
        proto.STRING,
        number=2,
    )
    sha1: str = proto.Field(
        proto.STRING,
        number=3,
    )
    size: int = proto.Field(
        proto.UINT64,
        number=4,
    )
    full_path: str = proto.Field(
        proto.STRING,
        number=5,
    )
    mime_type: str = proto.Field(
        proto.STRING,
        number=6,
    )
    file_metadata: "FileMetadata" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="FileMetadata",
    )
    security_result: "SecurityResult" = proto.Field(
        proto.MESSAGE,
        number=36,
        message="SecurityResult",
    )
    pe_file: "FileMetadataPE" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="FileMetadataPE",
    )
    ssdeep: str = proto.Field(
        proto.STRING,
        number=9,
    )
    vhash: str = proto.Field(
        proto.STRING,
        number=10,
    )
    ahash: str = proto.Field(
        proto.STRING,
        number=11,
    )
    authentihash: str = proto.Field(
        proto.STRING,
        number=20,
    )
    symhash: str = proto.Field(
        proto.STRING,
        number=41,
    )
    prefetch_file_metadata: "PrefetchFileMetadata" = proto.Field(
        proto.MESSAGE,
        number=43,
        message="PrefetchFileMetadata",
    )
    file_type: FileType = proto.Field(
        proto.ENUM,
        number=12,
        enum=FileType,
    )
    capabilities_tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=13,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=14,
    )
    tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=27,
    )
    last_modification_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=15,
        message=timestamp_pb2.Timestamp,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=39,
        message=timestamp_pb2.Timestamp,
    )
    last_access_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=40,
        message=timestamp_pb2.Timestamp,
    )
    prevalence: "Prevalence" = proto.Field(
        proto.MESSAGE,
        number=16,
        message="Prevalence",
    )
    first_seen_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=17,
        message=timestamp_pb2.Timestamp,
    )
    last_seen_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=18,
        message=timestamp_pb2.Timestamp,
    )
    stat_mode: int = proto.Field(
        proto.UINT64,
        number=21,
    )
    stat_inode: int = proto.Field(
        proto.UINT64,
        number=22,
    )
    stat_dev: int = proto.Field(
        proto.UINT64,
        number=23,
    )
    stat_nlink: int = proto.Field(
        proto.UINT64,
        number=24,
    )
    stat_flags: int = proto.Field(
        proto.UINT32,
        number=25,
    )
    last_analysis_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=26,
        message=timestamp_pb2.Timestamp,
    )
    embedded_urls: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=28,
    )
    embedded_domains: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=29,
    )
    embedded_ips: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=30,
    )
    exif_info: "ExifInfo" = proto.Field(
        proto.MESSAGE,
        number=31,
        message="ExifInfo",
    )
    signature_info: "SignatureInfo" = proto.Field(
        proto.MESSAGE,
        number=32,
        message="SignatureInfo",
    )
    pdf_info: "PDFInfo" = proto.Field(
        proto.MESSAGE,
        number=33,
        message="PDFInfo",
    )
    first_submission_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=34,
        message=timestamp_pb2.Timestamp,
    )
    last_submission_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=35,
        message=timestamp_pb2.Timestamp,
    )
    main_icon: "Favicon" = proto.Field(
        proto.MESSAGE,
        number=37,
        message="Favicon",
    )
    ntfs: "NtfsFileMetadata" = proto.Field(
        proto.MESSAGE,
        number=38,
        message="NtfsFileMetadata",
    )
    app_compat_cache: "AppCompatMetadata" = proto.Field(
        proto.MESSAGE,
        number=42,
        message="AppCompatMetadata",
    )


class NtfsFileMetadata(proto.Message):
    r"""NTFS-specific file metadata.

    Attributes:
        change_time (google.protobuf.timestamp_pb2.Timestamp):
            NTFS MFT entry changed timestamp.
        filename_create_time (google.protobuf.timestamp_pb2.Timestamp):
            NTFS $FILE_NAME attribute created timestamp.
        filename_modify_time (google.protobuf.timestamp_pb2.Timestamp):
            NTFS $FILE_NAME attribute modified timestamp.
        filename_access_time (google.protobuf.timestamp_pb2.Timestamp):
            NTFS $FILE_NAME attribute accessed timestamp.
        filename_change_time (google.protobuf.timestamp_pb2.Timestamp):
            NTFS $FILE_NAME attribute changed timestamp.
        usn_journal (MutableSequence[google.backstory.types.UsnJournal]):
            NTFS USN journal.
    """

    change_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    filename_create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    filename_modify_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    filename_access_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    filename_change_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    usn_journal: MutableSequence["UsnJournal"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="UsnJournal",
    )


class PrefetchFileMetadata(proto.Message):
    r"""Windows Prefetch file metadata.

    Attributes:
        run_count (int):
            The number of times the application has been
            run.
        prefetch_hash (str):
            A hash of the executable path used to
            identify the prefetch file.
    """

    run_count: int = proto.Field(
        proto.INT64,
        number=1,
    )
    prefetch_hash: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UsnJournal(proto.Message):
    r"""Information from the NTFS USN Journal.

    Attributes:
        attributes_flag (str):
            File attributes flags from the USN record
            (e.g., "0x20").
        attributes (google.backstory.types.UsnJournal.Attribute):
            Deprecated: Use file_attributes instead. File attributes
            from the USN record.
        file_attributes (MutableSequence[google.backstory.types.UsnJournal.Attribute]):
            File attributes from the USN record.
        allocated (bool):
            Indicates whether the file is allocated in
            the Master File Table (MFT).
        reason (google.backstory.types.UsnJournal.Reason):
            Deprecated: Use reasons instead. Human-readable string
            describing the reason for the USN journal entry. (e.g.,
            "USN_REASON_FILE_CREATE").
        reasons (MutableSequence[google.backstory.types.UsnJournal.Reason]):
            Human-readable string describing the reasons for the USN
            journal entry (e.g., "USN_REASON_FILE_CREATE").
    """

    class Attribute(proto.Enum):
        r"""File attributes from the USN record (e.g., "READ_ONLY, HIDDEN"). See
        https://learn.microsoft.com/en-us/windows/win32/fileio/file-attribute-constants
        for more information about the attributes.

        Values:
            ATTRIBUTE_UNSPECIFIED (0):
                Unspecified attribute.
            READ_ONLY (1):
                A file that is read-only.
            HIDDEN (2):
                The file or directory is hidden.
            SYSTEM (3):
                A file or directory that the operating system
                uses.
            ARCHIVE (4):
                Archive file or directory.
            COMPRESSED (5):
                A file or directory that is compressed.
            ENCRYPTED (6):
                A file or directory that is encrypted.
            DIRECTORY (7):
                The handle that identifies the directory.
            DEVICE (8):
                Reserved for system use.
            NORMAL (9):
                A file that does not have other attributes
                set.
            TEMPORARY (10):
                A file that is being used for temporary
                storage.
            SPARSE_FILE (11):
                A file that is a sparse file.
            REPARSE_POINT (12):
                A file or directory that has an associated
                reparse point.
            OFFLINE (13):
                The data of a file is not available
                immediately.
            NOT_CONTENT_INDEXED (14):
                The file or directory is not to be indexed.
            NON_CONTENT_INDEXED (14):
                Deprecated: Use NOT_CONTENT_INDEXED instead.
            INTEGRITY_STREAM (15):
                The directory or user data stream is
                configured with integrity.
            VIRTUAL (16):
                Reserved for system use.
            NO_SCRUB_DATA (17):
                The user data stream not to be read by the
                background data integrity scanner.
            EA (18):
                A file or directory with extended attributes.
            PINNED (19):
                The file or directory should be kept fully
                present locally.
            UNPINNED (20):
                The file or directory should not be kept
                fully present locally.
            RECALL_ON_OPEN (21):
                The file or directory has no physical
                representation on the local system.
            RECALL_ON_DATA_ACCESS (22):
                The file or directory is not fully present
                locally.
        """

        _pb_options = {"allow_alias": True}
        ATTRIBUTE_UNSPECIFIED = 0
        READ_ONLY = 1
        HIDDEN = 2
        SYSTEM = 3
        ARCHIVE = 4
        COMPRESSED = 5
        ENCRYPTED = 6
        DIRECTORY = 7
        DEVICE = 8
        NORMAL = 9
        TEMPORARY = 10
        SPARSE_FILE = 11
        REPARSE_POINT = 12
        OFFLINE = 13
        NOT_CONTENT_INDEXED = 14
        NON_CONTENT_INDEXED = 14
        INTEGRITY_STREAM = 15
        VIRTUAL = 16
        NO_SCRUB_DATA = 17
        EA = 18
        PINNED = 19
        UNPINNED = 20
        RECALL_ON_OPEN = 21
        RECALL_ON_DATA_ACCESS = 22

    class Reason(proto.Enum):
        r"""The reason for the USN journal entry.

        Values:
            REASON_UNSPECIFIED (0):
                Unspecified reason.
            DATA_OVERWRITE (1):
                Data overwrite reason.
            DATA_EXTEND (2):
                Data extend reason.
            DATA_TRUNCATION (3):
                Data truncation reason.
            NAMED_DATA_OVERWRITE (4):
                Named data overwrite reason.
            NAMED_DATA_EXTEND (5):
                Named data extend reason.
            NAMED_DATA_TRUNCATION (6):
                Named data truncation reason.
            FILE_CREATE (7):
                File create reason.
            FILE_DELETE (8):
                File delete reason.
            EA_CHANGE (9):
                EA change reason.
            SECURITY_CHANGE (10):
                Security change reason.
            RENAME_OLD_NAME (11):
                Rename old name reason.
            RENAME_NEW_NAME (12):
                Rename new name reason.
            INDEXABLE_CHANGE (13):
                Indexable change reason.
            BASIC_INFO_CHANGE (14):
                Basic info change reason.
            HARD_LINK_CHANGE (15):
                Hard link change reason.
            COMPRESSION_CHANGE (16):
                Compression change reason.
            ENCRYPTION_CHANGE (17):
                Encryption change reason.
            OBJECT_ID_CHANGE (18):
                Object ID change reason.
            REPARSE_POINT_CHANGE (19):
                Reparse point change reason.
            STREAM_CHANGE (20):
                Stream change reason.
            TRANSACTED_CHANGE (21):
                Transacted change reason.
            CLOSE (22):
                Close reason.
        """

        REASON_UNSPECIFIED = 0
        DATA_OVERWRITE = 1
        DATA_EXTEND = 2
        DATA_TRUNCATION = 3
        NAMED_DATA_OVERWRITE = 4
        NAMED_DATA_EXTEND = 5
        NAMED_DATA_TRUNCATION = 6
        FILE_CREATE = 7
        FILE_DELETE = 8
        EA_CHANGE = 9
        SECURITY_CHANGE = 10
        RENAME_OLD_NAME = 11
        RENAME_NEW_NAME = 12
        INDEXABLE_CHANGE = 13
        BASIC_INFO_CHANGE = 14
        HARD_LINK_CHANGE = 15
        COMPRESSION_CHANGE = 16
        ENCRYPTION_CHANGE = 17
        OBJECT_ID_CHANGE = 18
        REPARSE_POINT_CHANGE = 19
        STREAM_CHANGE = 20
        TRANSACTED_CHANGE = 21
        CLOSE = 22

    attributes_flag: str = proto.Field(
        proto.STRING,
        number=1,
    )
    attributes: Attribute = proto.Field(
        proto.ENUM,
        number=2,
        enum=Attribute,
    )
    file_attributes: MutableSequence[Attribute] = proto.RepeatedField(
        proto.ENUM,
        number=5,
        enum=Attribute,
    )
    allocated: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    reason: Reason = proto.Field(
        proto.ENUM,
        number=4,
        enum=Reason,
    )
    reasons: MutableSequence[Reason] = proto.RepeatedField(
        proto.ENUM,
        number=6,
        enum=Reason,
    )


class AppCompatMetadata(proto.Message):
    r"""Windows AppCompatCache (Application Compatibility) metadata.

    Attributes:
        sequence (int):
            Indicates the chronological order in which
            the entry was added to the cache.
        executed (bool):
            Indicates whether the file associated with
            the entry was executed.
        control_set (str):
            Indicates which registry Control Set the
            AppCompatCache data belongs to (e.g.,
            "ControlSet001").
    """

    sequence: int = proto.Field(
        proto.INT32,
        number=1,
    )
    executed: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    control_set: str = proto.Field(
        proto.STRING,
        number=3,
    )


class FileMetadataPE(proto.Message):
    r"""Metadata about the Portable Executable (PE) file.

    Attributes:
        imphash (str):
            Imphash of the file.
        entry_point (int):
            info.pe-entry-point.
        entry_point_exiftool (int):
            info.exiftool.EntryPoint.
        compilation_time (google.protobuf.timestamp_pb2.Timestamp):
            info.pe-timestamp.
        compilation_exiftool_time (google.protobuf.timestamp_pb2.Timestamp):
            info.exiftool.TimeStamp.
        section (MutableSequence[google.backstory.types.FileMetadataSection]):
            FilemetadataSection fields.
        imports (MutableSequence[google.backstory.types.FileMetadataImports]):
            FilemetadataImports fields.
        resource (MutableSequence[google.backstory.types.FileMetadataPeResourceInfo]):
            FilemetadataPeResourceInfo fields.
        resources_type_count (MutableSequence[google.backstory.types.StringToInt64MapEntry]):
            Deprecated: use resources_type_count_str.
        resources_language_count (MutableSequence[google.backstory.types.StringToInt64MapEntry]):
            Deprecated: use resources_language_count_str.
        resources_type_count_str (MutableSequence[google.backstory.types.Label]):
            Number of resources by resource type. Example: RT_ICON: 10,
            RT_DIALOG: 5
        resources_language_count_str (MutableSequence[google.backstory.types.Label]):
            Number of resources by language.
            Example: NEUTRAL: 20, ENGLISH US: 10
        signature_info (google.backstory.types.FileMetadataSignatureInfo):
            FilemetadataSignatureInfo field. deprecated, user
            File.signature_info instead.
    """

    imphash: str = proto.Field(
        proto.STRING,
        number=1,
    )
    entry_point: int = proto.Field(
        proto.INT64,
        number=2,
    )
    entry_point_exiftool: int = proto.Field(
        proto.INT64,
        number=9,
    )
    compilation_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    compilation_exiftool_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    section: MutableSequence["FileMetadataSection"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="FileMetadataSection",
    )
    imports: MutableSequence["FileMetadataImports"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="FileMetadataImports",
    )
    resource: MutableSequence["FileMetadataPeResourceInfo"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="FileMetadataPeResourceInfo",
    )
    resources_type_count: MutableSequence["StringToInt64MapEntry"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=6,
            message="StringToInt64MapEntry",
        )
    )
    resources_language_count: MutableSequence["StringToInt64MapEntry"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=7,
            message="StringToInt64MapEntry",
        )
    )
    resources_type_count_str: MutableSequence["Label"] = proto.RepeatedField(
        proto.MESSAGE,
        number=12,
        message="Label",
    )
    resources_language_count_str: MutableSequence["Label"] = proto.RepeatedField(
        proto.MESSAGE,
        number=13,
        message="Label",
    )
    signature_info: "FileMetadataSignatureInfo" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="FileMetadataSignatureInfo",
    )


class FileMetadataPeResourceInfo(proto.Message):
    r"""File metadata for PE resource.

    Attributes:
        sha256_hex (str):
            SHA256_hex field..
        filetype_magic (str):
            Type of resource content, as identified by
            the magic Python module.
        language_code (str):
            Human-readable version of the language and
            sublanguage identifiers, as defined in the
            Microsoft Windows PE specification.
        entropy (float):
            Entropy of the resource.
        file_type (str):
            File type.
            Note that this value may not match any of the
            well-known type identifiers defined in the
            ResourceType enum.
    """

    sha256_hex: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filetype_magic: str = proto.Field(
        proto.STRING,
        number=2,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=4,
    )
    entropy: float = proto.Field(
        proto.DOUBLE,
        number=5,
    )
    file_type: str = proto.Field(
        proto.STRING,
        number=6,
    )


class SignatureInfo(proto.Message):
    r"""File signature information extracted from different tools.

    Attributes:
        sigcheck (google.backstory.types.FileMetadataSignatureInfo):
            Signature information extracted from the
            sigcheck tool.
        codesign (google.backstory.types.FileMetadataCodesign):
            Signature information extracted from the
            codesign utility.
    """

    sigcheck: "FileMetadataSignatureInfo" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="FileMetadataSignatureInfo",
    )
    codesign: "FileMetadataCodesign" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="FileMetadataCodesign",
    )


class FileMetadataSignatureInfo(proto.Message):
    r"""Signature information.

    Attributes:
        verification_message (str):
            Status of the certificate.
            Valid values are "Signed", "Unsigned" or a
            description of the certificate anomaly, if
            found.
        verified (bool):
            True if verification_message == "Signed".
        signer (MutableSequence[str]):
            Deprecated: use signers field.
        signers (MutableSequence[google.backstory.types.SignerInfo]):
            File metadata signer information.
            The order of the signers matters. Each element
            is a higher level authority, being the last the
            root authority.
        x509 (MutableSequence[google.backstory.types.X509]):
            List of certificates.
    """

    verification_message: str = proto.Field(
        proto.STRING,
        number=1,
    )
    verified: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    signer: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    signers: MutableSequence["SignerInfo"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="SignerInfo",
    )
    x509: MutableSequence["X509"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="X509",
    )


class SignerInfo(proto.Message):
    r"""File metadata related to the signer information.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Common name of the signers/certificate.
            The order of the signers matters. Each element
            is a higher level authority, the last being the
            root authority.

            This field is a member of `oneof`_ ``_name``.
        status (str):
            It can say "Valid" or state the problem with
            the certificate if any (e.g. "This certificate
            or one of the certificates in the certificate
            chain is not time valid.").

            This field is a member of `oneof`_ ``_status``.
        valid_usage (str):
            Indicates which situations the certificate is
            valid for (e.g. "Code Signing").

            This field is a member of `oneof`_ ``_valid_usage``.
        cert_issuer (str):
            Company that issued the certificate.

            This field is a member of `oneof`_ ``_cert_issuer``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    status: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    valid_usage: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    cert_issuer: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )


class FileMetadataCodesign(proto.Message):
    r"""File metadata from the codesign utility.

    Attributes:
        id (str):
            Code sign identifier.
        format_ (str):
            Code sign format.
        compilation_time (google.protobuf.timestamp_pb2.Timestamp):
            Code sign timestamp
        team_id (str):
            The assigned team identifier of the developer
            who signed the application.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    format_: str = proto.Field(
        proto.STRING,
        number=2,
    )
    compilation_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    team_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class X509(proto.Message):
    r"""File certificate.

    Attributes:
        name (str):
            Certificate name.
        algorithm (str):
            Certificate algorithm.
        thumbprint (str):
            Certificate thumbprint.
        cert_issuer (str):
            Issuer of the certificate.
        serial_number (str):
            Certificate serial number.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    algorithm: str = proto.Field(
        proto.STRING,
        number=2,
    )
    thumbprint: str = proto.Field(
        proto.STRING,
        number=3,
    )
    cert_issuer: str = proto.Field(
        proto.STRING,
        number=4,
    )
    serial_number: str = proto.Field(
        proto.STRING,
        number=5,
    )


class PDFInfo(proto.Message):
    r"""Information about the PDF file structure. See
    https://developers.virustotal.com/reference/pdf_info

    Attributes:
        js (int):
            Number of /JS tags found in the PDF file.
            Should be the same as javascript field in normal
            scenarios.
        javascript (int):
            Number of /JavaScript tags found in the PDF
            file. Should be the same as the js field in
            normal scenarios.
        launch_action_count (int):
            Number of /Launch tags found in the PDF file.
        object_stream_count (int):
            Number of object streams.
        endobj_count (int):
            Number of object definitions (endobj
            keyword).
        header (str):
            PDF version.
        acroform (int):
            Number of /AcroForm tags found in the PDF.
        autoaction (int):
            Number of /AA tags found in the PDF.
        embedded_file (int):
            Number of /EmbeddedFile tags found in the
            PDF.
        encrypted (int):
            Whether the document is encrypted or not.
            This is defined by the /Encrypt tag.
        flash (int):
            Number of /RichMedia tags found in the PDF.
        jbig2_compression (int):
            Number of /JBIG2Decode tags found in the PDF.
        obj_count (int):
            Number of objects definitions (obj keyword).
        endstream_count (int):
            Number of defined stream objects (stream
            keyword).
        page_count (int):
            Number of pages in the PDF.
        stream_count (int):
            Number of defined stream objects (stream
            keyword).
        openaction (int):
            Number of /OpenAction tags found in the PDF.
        startxref (int):
            Number of startxref keywords in the PDF.
        suspicious_colors (int):
            Number of colors expressed with more than 3
            bytes (CVE-2009-3459).
        trailer (int):
            Number of trailer keywords in the PDF.
        xfa (int):
            Number of \XFA tags found in the PDF.
        xref (int):
            Number of xref keywords in the PDF.
    """

    js: int = proto.Field(
        proto.INT64,
        number=1,
    )
    javascript: int = proto.Field(
        proto.INT64,
        number=2,
    )
    launch_action_count: int = proto.Field(
        proto.INT64,
        number=3,
    )
    object_stream_count: int = proto.Field(
        proto.INT64,
        number=4,
    )
    endobj_count: int = proto.Field(
        proto.INT64,
        number=5,
    )
    header: str = proto.Field(
        proto.STRING,
        number=6,
    )
    acroform: int = proto.Field(
        proto.INT64,
        number=7,
    )
    autoaction: int = proto.Field(
        proto.INT64,
        number=8,
    )
    embedded_file: int = proto.Field(
        proto.INT64,
        number=9,
    )
    encrypted: int = proto.Field(
        proto.INT64,
        number=10,
    )
    flash: int = proto.Field(
        proto.INT64,
        number=11,
    )
    jbig2_compression: int = proto.Field(
        proto.INT64,
        number=12,
    )
    obj_count: int = proto.Field(
        proto.INT64,
        number=13,
    )
    endstream_count: int = proto.Field(
        proto.INT64,
        number=14,
    )
    page_count: int = proto.Field(
        proto.INT64,
        number=15,
    )
    stream_count: int = proto.Field(
        proto.INT64,
        number=16,
    )
    openaction: int = proto.Field(
        proto.INT64,
        number=17,
    )
    startxref: int = proto.Field(
        proto.INT64,
        number=18,
    )
    suspicious_colors: int = proto.Field(
        proto.INT64,
        number=19,
    )
    trailer: int = proto.Field(
        proto.INT64,
        number=20,
    )
    xfa: int = proto.Field(
        proto.INT64,
        number=21,
    )
    xref: int = proto.Field(
        proto.INT64,
        number=22,
    )


class StringToInt64MapEntry(proto.Message):
    r"""

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        key (str):
            Key field.

            This field is a member of `oneof`_ ``_key``.
        value (int):
            Value field.

            This field is a member of `oneof`_ ``_value``.
    """

    key: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    value: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )


class FileMetadataSection(proto.Message):
    r"""File metadata section.

    Attributes:
        name (str):
            Name of the section.
        entropy (float):
            Entropy of the section.
        raw_size_bytes (int):
            Raw file size in bytes.
        virtual_size_bytes (int):
            Virtual file size in bytes.
        md5_hex (str):
            MD5 hex of the file.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    entropy: float = proto.Field(
        proto.DOUBLE,
        number=2,
    )
    raw_size_bytes: int = proto.Field(
        proto.INT64,
        number=3,
    )
    virtual_size_bytes: int = proto.Field(
        proto.INT64,
        number=4,
    )
    md5_hex: str = proto.Field(
        proto.STRING,
        number=5,
    )


class FileMetadataImports(proto.Message):
    r"""File metadata imports.

    Attributes:
        library (str):
            Library field.
        functions (MutableSequence[str]):
            Function field.
    """

    library: str = proto.Field(
        proto.STRING,
        number=1,
    )
    functions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class ExifInfo(proto.Message):
    r"""Exif information.

    Attributes:
        original_file (str):
            original file name.
        product (str):
            product name.
        company (str):
            company name.
        file_description (str):
            description of a file.
        entry_point (int):
            entry point.
        compilation_time (google.protobuf.timestamp_pb2.Timestamp):
            Compilation time.
    """

    original_file: str = proto.Field(
        proto.STRING,
        number=1,
    )
    product: str = proto.Field(
        proto.STRING,
        number=2,
    )
    company: str = proto.Field(
        proto.STRING,
        number=3,
    )
    file_description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    entry_point: int = proto.Field(
        proto.INT64,
        number=5,
    )
    compilation_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )


class Prevalence(proto.Message):
    r"""The prevalence of a resource within the customer's
    environment. This measures how common it is for assets to access
    the resource.

    Attributes:
        rolling_max (int):
            The maximum number of assets per day accessing the resource
            over the trailing day_count days.
        day_count (int):
            The number of days over which rolling_max is calculated.
        rolling_max_sub_domains (int):
            The maximum number of assets per day accessing the domain
            along with sub-domains over the trailing day_count days.
            This field is only valid for domains.
        day_max (int):
            The max prevalence score in a day interval
            window.
        day_max_sub_domains (int):
            The max prevalence score in a day interval
            window across sub-domains. This field is only
            valid for domains.
    """

    rolling_max: int = proto.Field(
        proto.INT32,
        number=1,
    )
    day_count: int = proto.Field(
        proto.INT32,
        number=2,
    )
    rolling_max_sub_domains: int = proto.Field(
        proto.INT32,
        number=3,
    )
    day_max: int = proto.Field(
        proto.INT32,
        number=4,
    )
    day_max_sub_domains: int = proto.Field(
        proto.INT32,
        number=5,
    )


class Dns(proto.Message):
    r"""DNS information.

    Attributes:
        id (int):
            DNS query id.
        response (bool):
            Set to true if the event is a DNS response.
            See QR field from RFC1035.
        opcode (int):
            The DNS OpCode used to specify the type of
            DNS query (for example, QUERY, IQUERY, or
            STATUS).
        authoritative (bool):
            Other DNS header flags. See RFC1035, section
            4.1.1.
        truncated (bool):
            Whether the DNS response was truncated.
        recursion_desired (bool):
            Whether a recursive DNS lookup is desired.
        recursion_available (bool):
            Whether a recursive DNS lookup is available.
        response_code (int):
            Response code. See RCODE from RFC1035.
        questions (MutableSequence[google.backstory.types.Dns.Question]):
            A list of domain protocol message questions.
        answers (MutableSequence[google.backstory.types.Dns.ResourceRecord]):
            A list of answers to the domain name query.
        authority (MutableSequence[google.backstory.types.Dns.ResourceRecord]):
            A list of domain name servers which verified
            the answers to the domain name queries.
        additional (MutableSequence[google.backstory.types.Dns.ResourceRecord]):
            A list of additional domain name servers that
            can be used to verify the answer to the domain.
    """

    class Question(proto.Message):
        r"""DNS Questions. See RFC1035, section 4.1.2.

        Attributes:
            name (str):
                The domain name.
            type_ (int):
                The code specifying the type of the query.
            class_ (int):
                The code specifying the class of the query.
            prevalence (google.backstory.types.Prevalence):
                The prevalence of the domain within the
                customer's environment.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        type_: int = proto.Field(
            proto.UINT32,
            number=2,
        )
        class_: int = proto.Field(
            proto.UINT32,
            number=3,
        )
        prevalence: "Prevalence" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="Prevalence",
        )

    class ResourceRecord(proto.Message):
        r"""DNS Resource Records. See RFC1035, section 4.1.3.

        Attributes:
            name (str):
                The name of the owner of the resource record.
            type_ (int):
                The code specifying the type of the resource
                record.
            class_ (int):
                The code specifying the class of the resource
                record.
            ttl (int):
                The time interval for which the resource
                record can be cached before the source of the
                information should again be queried.
            data (str):
                The payload or response to the DNS question
                for all responses encoded in UTF-8 format
            binary_data (bytes):
                The raw bytes of any non-UTF8 strings that
                might be included as part of a DNS response.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        type_: int = proto.Field(
            proto.UINT32,
            number=2,
        )
        class_: int = proto.Field(
            proto.UINT32,
            number=3,
        )
        ttl: int = proto.Field(
            proto.UINT32,
            number=4,
        )
        data: str = proto.Field(
            proto.STRING,
            number=5,
        )
        binary_data: bytes = proto.Field(
            proto.BYTES,
            number=6,
        )

    id: int = proto.Field(
        proto.UINT32,
        number=6,
    )
    response: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    opcode: int = proto.Field(
        proto.UINT32,
        number=8,
    )
    authoritative: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    truncated: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    recursion_desired: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    recursion_available: bool = proto.Field(
        proto.BOOL,
        number=12,
    )
    response_code: int = proto.Field(
        proto.UINT32,
        number=13,
    )
    questions: MutableSequence[Question] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=Question,
    )
    answers: MutableSequence[ResourceRecord] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=ResourceRecord,
    )
    authority: MutableSequence[ResourceRecord] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=ResourceRecord,
    )
    additional: MutableSequence[ResourceRecord] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=ResourceRecord,
    )


class Dhcp(proto.Message):
    r"""DHCP information.

    Attributes:
        opcode (google.backstory.types.Dhcp.OpCode):
            The BOOTP op code.
        htype (int):
            Hardware address type.
        hlen (int):
            Hardware address length.
        hops (int):
            Hardware ops.
        transaction_id (int):
            Transaction ID.
        seconds (int):
            Seconds elapsed since client began address
            acquisition/renewal process.
        flags (int):
            Flags.
        ciaddr (str):
            Client IP address (ciaddr).
        yiaddr (str):
            Your IP address (yiaddr).
        siaddr (str):
            IP address of the next bootstrap server.
        giaddr (str):
            Relay agent IP address (giaddr).
        chaddr (str):
            Client hardware address (chaddr).
        sname (str):
            Server name that the client wishes to boot
            from.
        file (str):
            Boot image filename.
        options (MutableSequence[google.backstory.types.Dhcp.Option]):
            List of DHCP options.
        type_ (google.backstory.types.Dhcp.MessageType):
            DHCP message type.
        lease_time_seconds (int):
            Lease time in seconds. See RFC2132, section
            9.2.
        client_hostname (str):
            Client hostname. See RFC2132, section 3.14.
        client_identifier (bytes):
            Client identifier. See RFC2132, section 9.14. Note: Make
            sure to update the client_identifier_string field as well if
            you update this field.
        requested_address (str):
            Requested IP address. See RFC2132, section
            9.1.
        client_identifier_string (str):
            Client identifier as string. See RFC2132, section 9.14. This
            field holds the string value of the client_identifier.
    """

    class OpCode(proto.Enum):
        r"""BOOTP op code. See RFC951, section 3.

        Values:
            UNKNOWN_OPCODE (0):
                Default opcode.
            BOOTREQUEST (1):
                Request.
            BOOTREPLY (2):
                Reply.
        """

        UNKNOWN_OPCODE = 0
        BOOTREQUEST = 1
        BOOTREPLY = 2

    class MessageType(proto.Enum):
        r"""DHCP message type. See RFC2131, section 3.1.

        Values:
            UNKNOWN_MESSAGE_TYPE (0):
                Default message type.
            DISCOVER (1):
                DHCPDISCOVER.
            OFFER (2):
                DHCPOFFER.
            REQUEST (3):
                DHCPREQUEST.
            DECLINE (4):
                DHCPDECLINE.
            ACK (5):
                DHCPACK.
            NAK (6):
                DHCPNAK.
            RELEASE (7):
                DHCPRELEASE.
            INFORM (8):
                DHCPINFORM.
            WIN_DELETED (100):
                Microsoft Windows DHCP "lease deleted".
            WIN_EXPIRED (101):
                Microsoft Windows DHCP "lease expired".
        """

        UNKNOWN_MESSAGE_TYPE = 0
        DISCOVER = 1
        OFFER = 2
        REQUEST = 3
        DECLINE = 4
        ACK = 5
        NAK = 6
        RELEASE = 7
        INFORM = 8
        WIN_DELETED = 100
        WIN_EXPIRED = 101

    class Option(proto.Message):
        r"""DHCP options.

        Attributes:
            code (int):
                Code. See RFC1533.
            data (bytes):
                Data.
        """

        code: int = proto.Field(
            proto.UINT32,
            number=1,
        )
        data: bytes = proto.Field(
            proto.BYTES,
            number=2,
        )

    opcode: OpCode = proto.Field(
        proto.ENUM,
        number=1,
        enum=OpCode,
    )
    htype: int = proto.Field(
        proto.UINT32,
        number=2,
    )
    hlen: int = proto.Field(
        proto.UINT32,
        number=3,
    )
    hops: int = proto.Field(
        proto.UINT32,
        number=4,
    )
    transaction_id: int = proto.Field(
        proto.UINT32,
        number=5,
    )
    seconds: int = proto.Field(
        proto.UINT32,
        number=6,
    )
    flags: int = proto.Field(
        proto.UINT32,
        number=7,
    )
    ciaddr: str = proto.Field(
        proto.STRING,
        number=8,
    )
    yiaddr: str = proto.Field(
        proto.STRING,
        number=9,
    )
    siaddr: str = proto.Field(
        proto.STRING,
        number=10,
    )
    giaddr: str = proto.Field(
        proto.STRING,
        number=11,
    )
    chaddr: str = proto.Field(
        proto.STRING,
        number=12,
    )
    sname: str = proto.Field(
        proto.STRING,
        number=13,
    )
    file: str = proto.Field(
        proto.STRING,
        number=14,
    )
    options: MutableSequence[Option] = proto.RepeatedField(
        proto.MESSAGE,
        number=15,
        message=Option,
    )
    type_: MessageType = proto.Field(
        proto.ENUM,
        number=16,
        enum=MessageType,
    )
    lease_time_seconds: int = proto.Field(
        proto.UINT32,
        number=17,
    )
    client_hostname: str = proto.Field(
        proto.STRING,
        number=18,
    )
    client_identifier: bytes = proto.Field(
        proto.BYTES,
        number=19,
    )
    requested_address: str = proto.Field(
        proto.STRING,
        number=20,
    )
    client_identifier_string: str = proto.Field(
        proto.STRING,
        number=21,
    )


class Certificate(proto.Message):
    r"""Certificate information

    Attributes:
        version (str):
            Certificate version.
        serial (str):
            Certificate serial number.
        subject (str):
            Subject of the certificate.
        issuer (str):
            Issuer of the certificate.
        md5 (str):
            The MD5 hash of the certificate, as a
            hex-encoded string.
        sha1 (str):
            The SHA1 hash of the certificate, as a
            hex-encoded string.
        sha256 (str):
            The SHA256 hash of the certificate, as a
            hex-encoded string.
        not_before (google.protobuf.timestamp_pb2.Timestamp):
            Indicates when the certificate is first
            valid.
        not_after (google.protobuf.timestamp_pb2.Timestamp):
            Indicates when the certificate is no longer
            valid.
    """

    version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    serial: str = proto.Field(
        proto.STRING,
        number=2,
    )
    subject: str = proto.Field(
        proto.STRING,
        number=3,
    )
    issuer: str = proto.Field(
        proto.STRING,
        number=4,
    )
    md5: str = proto.Field(
        proto.STRING,
        number=5,
    )
    sha1: str = proto.Field(
        proto.STRING,
        number=6,
    )
    sha256: str = proto.Field(
        proto.STRING,
        number=7,
    )
    not_before: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    not_after: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )


class Tls(proto.Message):
    r"""Transport Layer Security (TLS) information.

    Attributes:
        client (google.backstory.types.Tls.Client):
            Certificate information for the client
            certificate.
        server (google.backstory.types.Tls.Server):
            Certificate information for the server
            certificate.
        cipher (str):
            Cipher used during the connection.
        curve (str):
            Elliptical curve used for a given cipher.
        version (str):
            TLS version.
        version_protocol (str):
            Protocol.
        established (bool):
            Indicates whether the TLS negotiation was
            successful.
        next_protocol (str):
            Protocol to be used for tunnel.
        resumed (bool):
            Indicates whether the TLS connection was
            resumed from a previous TLS negotiation.
    """

    class Client(proto.Message):
        r"""Transport Layer Security (TLS) information associated with
        the client (for example, Certificate or JA3 hash).

        Attributes:
            certificate (google.backstory.types.Certificate):
                Client certificate.
            ja3 (str):
                JA3 hash from the TLS ClientHello, as a
                hex-encoded string.
            server_name (str):
                Host name of the server, that the client is
                connecting to.
            supported_ciphers (MutableSequence[str]):
                Ciphers supported by the client during client
                hello.
            ja4 (str):
                JA4 hash from the TLS ClientHello, as a
                hex-encoded string.
        """

        certificate: "Certificate" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="Certificate",
        )
        ja3: str = proto.Field(
            proto.STRING,
            number=2,
        )
        server_name: str = proto.Field(
            proto.STRING,
            number=3,
        )
        supported_ciphers: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=4,
        )
        ja4: str = proto.Field(
            proto.STRING,
            number=5,
        )

    class Server(proto.Message):
        r"""Transport Layer Security (TLS) information associated with
        the server (for example, Certificate or JA3 hash).

        Attributes:
            certificate (google.backstory.types.Certificate):
                Server certificate.
            ja3s (str):
                JA3 hash from the TLS ServerHello, as a
                hex-encoded string.
            ja4s (str):
                JA4 hash from the TLS ServerHello, as a
                hex-encoded string.
        """

        certificate: "Certificate" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="Certificate",
        )
        ja3s: str = proto.Field(
            proto.STRING,
            number=2,
        )
        ja4s: str = proto.Field(
            proto.STRING,
            number=3,
        )

    client: Client = proto.Field(
        proto.MESSAGE,
        number=1,
        message=Client,
    )
    server: Server = proto.Field(
        proto.MESSAGE,
        number=2,
        message=Server,
    )
    cipher: str = proto.Field(
        proto.STRING,
        number=3,
    )
    curve: str = proto.Field(
        proto.STRING,
        number=4,
    )
    version: str = proto.Field(
        proto.STRING,
        number=5,
    )
    version_protocol: str = proto.Field(
        proto.STRING,
        number=6,
    )
    established: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    next_protocol: str = proto.Field(
        proto.STRING,
        number=8,
    )
    resumed: bool = proto.Field(
        proto.BOOL,
        number=9,
    )


class Http(proto.Message):
    r"""Specify the full URL of the HTTP request within "target".
    Also specify any uploaded or downloaded file information within
    "source" or "target".

    Attributes:
        method (str):
            The HTTP request method
            (e.g. "GET", "POST", "PATCH", "DELETE").
        referral_url (str):
            The URL for the HTTP referer.
        user_agent (str):
            The User-Agent request header which includes
            the application type, operating system, software
            vendor or software version of the requesting
            software user agent.
        response_code (int):
            The response status code, for example
            200, 302, 404, or 500.
    """

    method: str = proto.Field(
        proto.STRING,
        number=1,
    )
    referral_url: str = proto.Field(
        proto.STRING,
        number=2,
    )
    user_agent: str = proto.Field(
        proto.STRING,
        number=3,
    )
    response_code: int = proto.Field(
        proto.INT32,
        number=4,
    )


class Browser(proto.Message):
    r"""Information about an entry in the web browser's local history
    database.

    Attributes:
        browser_type (google.backstory.types.Browser.BrowserType):
            The browser that recorded the history entry
            (e.g. "Chrome", "Firefox", "Safari", etc.).
        browser_version (str):
            The browser version.
        first_visit_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp indicating the initial visit to
            the URL.
        last_visit_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp indicating the most recent
            visit to the URL.
        profile (str):
            The browser profile associated with the
            history entry.
        typed (bool):
            A boolean value indicating if the URL was
            typed by the user.
        visit_type (google.backstory.types.Browser.UrlVisitType):
            Describes the type of navigation or visit
            (e.g., direct, redirect, etc.).
        hidden (bool):
            A boolean value indicating if the history
            entry is hidden.
        request_origin_uri (str):
            Indicates the URI from which the current
            visit originated.
        visit_count (int):
            The total number of times the Url has been
            visited.
        visit_count_criteria (str):
            Describes the criteria used to calculate the visit_count.
        indexed_content (str):
            Represents the textual content of a web page.
            This field should be kept short. Large strings
            may affect latency and payload sizes.
        first_bookmarked_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp indicating the first time the
            URL was bookmarked.
        cookies (MutableSequence[google.backstory.types.Browser.Cookie]):
            Information about the cookies.
        typed_count (int):
            The number of times the URL was visited with
            this specific visit type and visit source.
        visit_source (google.backstory.types.Browser.VisitSource):
            The source of the visit.
    """

    class BrowserType(proto.Enum):
        r"""The name of the browser.

        Values:
            BROWSER_TYPE_UNSPECIFIED (0):
                Default value.
            CHROME (1):
                Chrome.
            FIREFOX (2):
                Firefox.
            SAFARI (3):
                Safari.
            INTERNET_EXPLORER (4):
                Internet Explorer.
            EDGE (5):
                Edge.
            OPERA (6):
                Opera.
        """

        BROWSER_TYPE_UNSPECIFIED = 0
        CHROME = 1
        FIREFOX = 2
        SAFARI = 3
        INTERNET_EXPLORER = 4
        EDGE = 5
        OPERA = 6

    class UrlVisitType(proto.Enum):
        r"""The type of visit to a URL.

        Values:
            URL_VISIT_TYPE_UNSPECIFIED (0):
                Default value.
            LINK (1):
                The user clicked a link.
            TYPED (2):
                The user typed a URL.
            AUTO_BOOKMARK (3):
                The user bookmarked the URL.
            AUTO_SUBFRAME (4):
                Loaded in a nested subframe by the parent
                frame.
            MANUAL_SUBFRAME (5):
                Loaded in a nested subframe by the user.
            GENERATED (6):
                The user clicked on auto generated link in
                browser address bar.
            AUTO_TOPLEVEL (7):
                The page was loaded through command line or
                is the starting page.
            FORM_SUBMIT (8):
                The user submitted a form.
            RELOAD (9):
                The user reloaded the page.
            KEYWORD (10):
                The Url was generated by a keyword search
                configured by user.
            KEYWORD_GENERATED (11):
                Corresponds to a visit generated by a keyword
                search.
            REDIRECT (12):
                The user was redirected to the URL.
        """

        URL_VISIT_TYPE_UNSPECIFIED = 0
        LINK = 1
        TYPED = 2
        AUTO_BOOKMARK = 3
        AUTO_SUBFRAME = 4
        MANUAL_SUBFRAME = 5
        GENERATED = 6
        AUTO_TOPLEVEL = 7
        FORM_SUBMIT = 8
        RELOAD = 9
        KEYWORD = 10
        KEYWORD_GENERATED = 11
        REDIRECT = 12

    class VisitSource(proto.Enum):
        r"""The source of the visit.

        Values:
            VISIT_SOURCE_UNSPECIFIED (0):
                Default value.
            SYNCED (1):
                The visit was synced from another device.
            BROWSER (2):
                The visit was from a browser.
            EXTENSION (3):
                The visit was from an extension.
            IMPORTED (4):
                The visit was imported from another browser
                application.
        """

        VISIT_SOURCE_UNSPECIFIED = 0
        SYNCED = 1
        BROWSER = 2
        EXTENSION = 3
        IMPORTED = 4

    class Cookie(proto.Message):
        r"""Browser cookie.

        Attributes:
            name (str):
                The unique name identifying the cookie.
            value (str):
                The data stored within the cookie.
            domain (str):
                The domain for which the cookie is valid.
            path (str):
                The URL path for which the cookie is valid.
            expiration_time (google.protobuf.timestamp_pb2.Timestamp):
                The date and time when the cookie will
                expire.
            http_only (bool):
                Indicates if the cookie is inaccessible via
                client-side scripts (e.g., JavaScript).
            secure (bool):
                Indicates if the cookie should only be sent
                over secure HTTPS connections.
            max_age (int):
                The maximum age of the cookie in seconds.
            same_site (google.backstory.types.Browser.Cookie.CookieSameSite):
                Affects cross-site request behavior.
            session (bool):
                Indicates if the cookie is persistent.
            partitioned (bool):
                Shows if the cookies is stored using
                partitioned storage.
        """

        class CookieSameSite(proto.Enum):
            r"""The SameSite attribute of a cookie.

            Values:
                COOKIE_SAME_SITE_UNSPECIFIED (0):
                    Default value.
                STRICT (1):
                    Corresponds to SameSite=Strict.
                LAX (2):
                    Corresponds to SameSite=Lax.
                NONE (3):
                    Corresponds to SameSite=None.
            """

            COOKIE_SAME_SITE_UNSPECIFIED = 0
            STRICT = 1
            LAX = 2
            NONE = 3

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        value: str = proto.Field(
            proto.STRING,
            number=2,
        )
        domain: str = proto.Field(
            proto.STRING,
            number=3,
        )
        path: str = proto.Field(
            proto.STRING,
            number=4,
        )
        expiration_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=5,
            message=timestamp_pb2.Timestamp,
        )
        http_only: bool = proto.Field(
            proto.BOOL,
            number=6,
        )
        secure: bool = proto.Field(
            proto.BOOL,
            number=7,
        )
        max_age: int = proto.Field(
            proto.INT64,
            number=8,
        )
        same_site: "Browser.Cookie.CookieSameSite" = proto.Field(
            proto.ENUM,
            number=9,
            enum="Browser.Cookie.CookieSameSite",
        )
        session: bool = proto.Field(
            proto.BOOL,
            number=10,
        )
        partitioned: bool = proto.Field(
            proto.BOOL,
            number=11,
        )

    browser_type: BrowserType = proto.Field(
        proto.ENUM,
        number=1,
        enum=BrowserType,
    )
    browser_version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    first_visit_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    last_visit_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    profile: str = proto.Field(
        proto.STRING,
        number=5,
    )
    typed: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    visit_type: UrlVisitType = proto.Field(
        proto.ENUM,
        number=7,
        enum=UrlVisitType,
    )
    hidden: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    request_origin_uri: str = proto.Field(
        proto.STRING,
        number=9,
    )
    visit_count: int = proto.Field(
        proto.INT64,
        number=10,
    )
    visit_count_criteria: str = proto.Field(
        proto.STRING,
        number=11,
    )
    indexed_content: str = proto.Field(
        proto.STRING,
        number=12,
    )
    first_bookmarked_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=13,
        message=timestamp_pb2.Timestamp,
    )
    cookies: MutableSequence[Cookie] = proto.RepeatedField(
        proto.MESSAGE,
        number=14,
        message=Cookie,
    )
    typed_count: int = proto.Field(
        proto.INT64,
        number=15,
    )
    visit_source: VisitSource = proto.Field(
        proto.ENUM,
        number=16,
        enum=VisitSource,
    )


class Hardware(proto.Message):
    r"""Hardware specification details for a resource, including both
    physical and virtual hardware.

    Attributes:
        serial_number (str):
            Hardware serial number.
        manufacturer (str):
            Hardware manufacturer.
        model (str):
            Hardware model.
        cpu_platform (str):
            Platform of the hardware CPU (e.g. "Intel
            Broadwell").
        cpu_model (str):
            Model description of the hardware CPU
            (e.g. "2.8 GHz Quad-Core Intel Core i5").
        cpu_clock_speed (int):
            Clock speed of the hardware CPU in MHz.
        cpu_max_clock_speed (int):
            Maximum possible clock speed of the hardware
            CPU in MHz.
        cpu_number_cores (int):
            Number of CPU cores.
        ram (int):
            Amount of the hardware ramdom access memory
            (RAM) in Mb.
    """

    serial_number: str = proto.Field(
        proto.STRING,
        number=1,
    )
    manufacturer: str = proto.Field(
        proto.STRING,
        number=2,
    )
    model: str = proto.Field(
        proto.STRING,
        number=3,
    )
    cpu_platform: str = proto.Field(
        proto.STRING,
        number=4,
    )
    cpu_model: str = proto.Field(
        proto.STRING,
        number=5,
    )
    cpu_clock_speed: int = proto.Field(
        proto.UINT64,
        number=6,
    )
    cpu_max_clock_speed: int = proto.Field(
        proto.UINT64,
        number=7,
    )
    cpu_number_cores: int = proto.Field(
        proto.UINT64,
        number=8,
    )
    ram: int = proto.Field(
        proto.UINT64,
        number=9,
    )


class PlatformSoftware(proto.Message):
    r"""Platform software information about an operating system.

    Attributes:
        platform (google.backstory.types.Noun.Platform):
            The platform operating system.
        platform_version (str):
            The platform software version (
            e.g. "Microsoft Windows 1803").
        platform_patch_level (str):
            The platform software patch level (
            e.g. "Build 17134.48", "SP1").
    """

    platform: "Noun.Platform" = proto.Field(
        proto.ENUM,
        number=1,
        enum="Noun.Platform",
    )
    platform_version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    platform_patch_level: str = proto.Field(
        proto.STRING,
        number=3,
    )


class Software(proto.Message):
    r"""Information about a software package or application.

    Attributes:
        name (str):
            The name of the software.
        version (str):
            The version of the software.
        permissions (MutableSequence[google.backstory.types.Permission]):
            System permissions granted to the software. For example,
            "android.permission.WRITE_EXTERNAL_STORAGE".
        description (str):
            The description of the software.
        vendor_name (str):
            The name of the software vendor.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: str = proto.Field(
        proto.STRING,
        number=2,
    )
    permissions: MutableSequence["Permission"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="Permission",
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    vendor_name: str = proto.Field(
        proto.STRING,
        number=5,
    )


class Asset(proto.Message):
    r"""Information about a compute asset such as a workstation,
    laptop, phone, virtual desktop, or VM.

    Attributes:
        product_object_id (str):
            A vendor-specific identifier to uniquely
            identify the entity (a GUID  or similar).
            This field can be used as an entity indicator
            for asset entities.
        hostname (str):
            Asset hostname or domain name field.
            This field can be used as an entity indicator
            for asset entities.
        asset_id (str):
            The asset ID. Value must contain the ':'
            character. For example, cs:abcdd23434.
            This field can be used as an entity indicator
            for asset entities.
        ip (MutableSequence[str]):
            A list of IP addresses associated with an
            asset. This field can be used as an entity
            indicator for asset entities.
        mac (MutableSequence[str]):
            List of MAC addresses associated with an
            asset. This field can be used as an entity
            indicator for asset entities.
        nat_ip (MutableSequence[str]):
            List of NAT IP addresses associated with an
            asset.
        first_seen_time (google.protobuf.timestamp_pb2.Timestamp):
            The first observed time for an asset.
            The value is calculated on the basis of the
            first time the identifier was observed.
        hardware (MutableSequence[google.backstory.types.Hardware]):
            The asset hardware specifications.
        platform_software (google.backstory.types.PlatformSoftware):
            The asset operating system platform software.
        software (MutableSequence[google.backstory.types.Software]):
            The asset software details.
        location (google.backstory.types.Location):
            Location of the asset.
        category (str):
            The category of the asset (e.g. "End User
            Asset", "Workstation", "Server").
        type_ (google.backstory.types.Asset.AssetType):
            The type of the asset (e.g. workstation or
            laptop or server).
        network_domain (str):
            The network domain of the asset (e.g.
            "corp.acme.com")
        creation_time (google.protobuf.timestamp_pb2.Timestamp):
            Time the asset was created or provisioned. Deprecate:
            creation_time should be populated in Attribute as generic
            metadata.
        first_discover_time (google.protobuf.timestamp_pb2.Timestamp):
            Time the asset was first discovered (by asset
            management/discoverability software).
        last_discover_time (google.protobuf.timestamp_pb2.Timestamp):
            Time the asset was last discovered (by asset
            management/discoverability software).
        system_last_update_time (google.protobuf.timestamp_pb2.Timestamp):
            Time the asset system or OS was last updated. For all other
            operations that are not system updates (such as resizing a
            VM), use Attribute.last_update_time.
        last_boot_time (google.protobuf.timestamp_pb2.Timestamp):
            Time the asset was last boot started.
        labels (MutableSequence[google.backstory.types.Label]):
            Metadata labels for the asset.
            Deprecated: labels should be populated in
            Attribute as generic metadata.
        deployment_status (google.backstory.types.Asset.DeploymentStatus):
            The deployment status of the asset for device
            lifecycle purposes.
        vulnerabilities (MutableSequence[google.backstory.types.Vulnerability]):
            Vulnerabilities discovered on asset.
        attribute (google.backstory.types.Attribute):
            Generic entity metadata attributes of the
            asset.
        wmi_persistence_item (google.backstory.types.WmiPersistenceItem):
            Information about a WMI persistence item.
    """

    class AssetType(proto.Enum):
        r"""The role type of the asset.

        Values:
            ROLE_UNSPECIFIED (0):
                Unspecified asset role.
            WORKSTATION (1):
                A workstation or desktop.
            LAPTOP (2):
                A laptop computer.
            IOT (3):
                An IOT asset.
            NETWORK_ATTACHED_STORAGE (4):
                A network attached storage device.
            PRINTER (5):
                A printer.
            SCANNER (6):
                A scanner.
            SERVER (7):
                A server.
            TAPE_LIBRARY (8):
                A tape library device.
            MOBILE (9):
                A mobile device such as a mobile phone or
                PDA.
        """

        ROLE_UNSPECIFIED = 0
        WORKSTATION = 1
        LAPTOP = 2
        IOT = 3
        NETWORK_ATTACHED_STORAGE = 4
        PRINTER = 5
        SCANNER = 6
        SERVER = 7
        TAPE_LIBRARY = 8
        MOBILE = 9

    class DeploymentStatus(proto.Enum):
        r"""Deployment status states.

        Values:
            DEPLOYMENT_STATUS_UNSPECIFIED (0):
                Unspecified deployment status.
            ACTIVE (1):
                Asset is active, functional and deployed.
            PENDING_DECOMISSION (2):
                Asset is pending decommission and no longer
                deployed.
            DECOMISSIONED (3):
                Asset is decommissioned.
        """

        DEPLOYMENT_STATUS_UNSPECIFIED = 0
        ACTIVE = 1
        PENDING_DECOMISSION = 2
        DECOMISSIONED = 3

    product_object_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=2,
    )
    asset_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    ip: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    mac: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    nat_ip: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=22,
    )
    first_seen_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=23,
        message=timestamp_pb2.Timestamp,
    )
    hardware: MutableSequence["Hardware"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="Hardware",
    )
    platform_software: "PlatformSoftware" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="PlatformSoftware",
    )
    software: MutableSequence["Software"] = proto.RepeatedField(
        proto.MESSAGE,
        number=17,
        message="Software",
    )
    location: "Location" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="Location",
    )
    category: str = proto.Field(
        proto.STRING,
        number=9,
    )
    type_: AssetType = proto.Field(
        proto.ENUM,
        number=18,
        enum=AssetType,
    )
    network_domain: str = proto.Field(
        proto.STRING,
        number=10,
    )
    creation_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    first_discover_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        message=timestamp_pb2.Timestamp,
    )
    last_discover_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=13,
        message=timestamp_pb2.Timestamp,
    )
    system_last_update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=14,
        message=timestamp_pb2.Timestamp,
    )
    last_boot_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=15,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableSequence["Label"] = proto.RepeatedField(
        proto.MESSAGE,
        number=16,
        message="Label",
    )
    deployment_status: DeploymentStatus = proto.Field(
        proto.ENUM,
        number=19,
        enum=DeploymentStatus,
    )
    vulnerabilities: MutableSequence["Vulnerability"] = proto.RepeatedField(
        proto.MESSAGE,
        number=21,
        message="Vulnerability",
    )
    attribute: "Attribute" = proto.Field(
        proto.MESSAGE,
        number=20,
        message="Attribute",
    )
    wmi_persistence_item: "WmiPersistenceItem" = proto.Field(
        proto.MESSAGE,
        number=24,
        message="WmiPersistenceItem",
    )


class User(proto.Message):
    r"""Information about a user.

    Attributes:
        product_object_id (str):
            A vendor-specific identifier to uniquely
            identify the entity (e.g. a GUID, LDAP, OID, or
            similar). This field can be used as an entity
            indicator for user entities.
        userid (str):
            The ID of the user.
            This field can be used as an entity indicator
            for user entities.
        user_display_name (str):
            The display name of the user
            (e.g. "John Locke").
        first_name (str):
            First name of the user (e.g. "John").
        middle_name (str):
            Middle name of the user.
        last_name (str):
            Last name of the user (e.g. "Locke").
        phone_numbers (MutableSequence[str]):
            Phone numbers for the user.
        personal_address (google.backstory.types.Location):
            Personal address of the user.
        attribute (google.backstory.types.Attribute):
            Generic entity metadata attributes of the
            user.
        first_seen_time (google.protobuf.timestamp_pb2.Timestamp):
            The first observed time for a user.
            The value is calculated on the basis of the
            first time the identifier was observed.
        account_type (google.backstory.types.User.AccountType):
            Type of user account (for example, service, domain, or
            cloud). This is somewhat aligned to:
            https://attack.mitre.org/techniques/T1078/
        groupid (str):
            The ID of the group that the user belongs to. Deprecated in
            favor of the repeated group_identifiers field.
        group_identifiers (MutableSequence[str]):
            Product object identifiers of the group(s)
            the user belongs to A vendor-specific identifier
            to uniquely identify the group(s) the user
            belongs to (a GUID, LDAP OID, or similar).
        windows_sid (str):
            The Microsoft Windows SID of the user.
            This field can be used as an entity indicator
            for user entities.
        email_addresses (MutableSequence[str]):
            Email addresses of the user.
            This field can be used as an entity indicator
            for user entities.
        employee_id (str):
            Human capital management identifier.
            This field can be used as an entity indicator
            for user entities.
        title (str):
            User job title.
        company_name (str):
            User job company name.
        department (MutableSequence[str]):
            User job department
        office_address (google.backstory.types.Location):
            User job office location.
        managers (MutableSequence[google.backstory.types.User]):
            User job manager(s).
        hire_date (google.protobuf.timestamp_pb2.Timestamp):
            User job employment hire date.
        termination_date (google.protobuf.timestamp_pb2.Timestamp):
            User job employment termination date.
        time_off (MutableSequence[google.backstory.types.TimeOff]):
            User time off leaves from active work.
        last_login_time (google.protobuf.timestamp_pb2.Timestamp):
            User last login timestamp.
        last_password_change_time (google.protobuf.timestamp_pb2.Timestamp):
            User last password change timestamp.
        password_expiration_time (google.protobuf.timestamp_pb2.Timestamp):
            User password expiration timestamp.
        account_expiration_time (google.protobuf.timestamp_pb2.Timestamp):
            User account expiration timestamp.
        account_lockout_time (google.protobuf.timestamp_pb2.Timestamp):
            User account lockout timestamp.
        last_bad_password_attempt_time (google.protobuf.timestamp_pb2.Timestamp):
            User last bad password attempt timestamp.
        user_authentication_status (google.backstory.types.Authentication.AuthenticationStatus):
            System authentication status for user.
        role_name (str):
            System role name for user.
            Deprecated: use attribute.roles.
        role_description (str):
            System role description for user.
            Deprecated: use attribute.roles.
        user_role (google.backstory.types.User.Role):
            System role for user.
            Deprecated: use attribute.roles.
    """

    class AccountType(proto.Enum):
        r"""User Account Type.

        Values:
            ACCOUNT_TYPE_UNSPECIFIED (0):
                Default user account type.
            DOMAIN_ACCOUNT_TYPE (1):
                A human account part of some domain in
                directory services.
            LOCAL_ACCOUNT_TYPE (2):
                A local machine account.
            CLOUD_ACCOUNT_TYPE (3):
                A SaaS service account type (such as Slack or
                GitHub).
            SERVICE_ACCOUNT_TYPE (4):
                A non-human account for data access.
            DEFAULT_ACCOUNT_TYPE (5):
                A system built in default account.
        """

        ACCOUNT_TYPE_UNSPECIFIED = 0
        DOMAIN_ACCOUNT_TYPE = 1
        LOCAL_ACCOUNT_TYPE = 2
        CLOUD_ACCOUNT_TYPE = 3
        SERVICE_ACCOUNT_TYPE = 4
        DEFAULT_ACCOUNT_TYPE = 5

    class Role(proto.Enum):
        r"""User system roles.

        Values:
            UNKNOWN_ROLE (0):
                Default user role.
            ADMINISTRATOR (1):
                Product administrator with elevated
                privileges.
            SERVICE_ACCOUNT (2):
                System service account for automated privilege access.
                Deprecated: not a role, instead set User.account_type.
        """

        UNKNOWN_ROLE = 0
        ADMINISTRATOR = 1
        SERVICE_ACCOUNT = 2

    product_object_id: str = proto.Field(
        proto.STRING,
        number=7,
    )
    userid: str = proto.Field(
        proto.STRING,
        number=1,
    )
    user_display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    first_name: str = proto.Field(
        proto.STRING,
        number=100,
    )
    middle_name: str = proto.Field(
        proto.STRING,
        number=101,
    )
    last_name: str = proto.Field(
        proto.STRING,
        number=102,
    )
    phone_numbers: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=103,
    )
    personal_address: "Location" = proto.Field(
        proto.MESSAGE,
        number=104,
        message="Location",
    )
    attribute: "Attribute" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="Attribute",
    )
    first_seen_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    account_type: AccountType = proto.Field(
        proto.ENUM,
        number=9,
        enum=AccountType,
    )
    groupid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    group_identifiers: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=200,
    )
    windows_sid: str = proto.Field(
        proto.STRING,
        number=4,
    )
    email_addresses: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    employee_id: str = proto.Field(
        proto.STRING,
        number=6,
    )
    title: str = proto.Field(
        proto.STRING,
        number=601,
    )
    company_name: str = proto.Field(
        proto.STRING,
        number=602,
    )
    department: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=603,
    )
    office_address: "Location" = proto.Field(
        proto.MESSAGE,
        number=604,
        message="Location",
    )
    managers: MutableSequence["User"] = proto.RepeatedField(
        proto.MESSAGE,
        number=605,
        message="User",
    )
    hire_date: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=606,
        message=timestamp_pb2.Timestamp,
    )
    termination_date: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=607,
        message=timestamp_pb2.Timestamp,
    )
    time_off: MutableSequence["TimeOff"] = proto.RepeatedField(
        proto.MESSAGE,
        number=608,
        message="TimeOff",
    )
    last_login_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=609,
        message=timestamp_pb2.Timestamp,
    )
    last_password_change_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=610,
        message=timestamp_pb2.Timestamp,
    )
    password_expiration_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=611,
        message=timestamp_pb2.Timestamp,
    )
    account_expiration_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=612,
        message=timestamp_pb2.Timestamp,
    )
    account_lockout_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=613,
        message=timestamp_pb2.Timestamp,
    )
    last_bad_password_attempt_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=614,
        message=timestamp_pb2.Timestamp,
    )
    user_authentication_status: "Authentication.AuthenticationStatus" = proto.Field(
        proto.ENUM,
        number=701,
        enum="Authentication.AuthenticationStatus",
    )
    role_name: str = proto.Field(
        proto.STRING,
        number=702,
    )
    role_description: str = proto.Field(
        proto.STRING,
        number=703,
    )
    user_role: Role = proto.Field(
        proto.ENUM,
        number=704,
        enum=Role,
    )


class TimeOff(proto.Message):
    r"""System record for leave/time-off from a Human Capital
    Management (HCM) system.

    Attributes:
        interval (google.type.interval_pb2.Interval):
            Interval duration of the leave.
        description (str):
            Description of the leave if available (e.g.
            'Vacation').
    """

    interval: interval_pb2.Interval = proto.Field(
        proto.MESSAGE,
        number=1,
        message=interval_pb2.Interval,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Permission(proto.Message):
    r"""System permission for resource access and modification.

    Attributes:
        name (str):
            Name of the permission (e.g.
            chronicle.analyst.updateRule).
        description (str):
            Description of the permission (e.g. 'Ability
            to update detect rules').
        type_ (google.backstory.types.Permission.PermissionType):
            Type of the permission.
    """

    class PermissionType(proto.Enum):
        r"""High level categorizations of permission type.

        Values:
            UNKNOWN_PERMISSION_TYPE (0):
                Default permission type.
            ADMIN_WRITE (1):
                Administrator write permission.
            ADMIN_READ (2):
                Administrator read permission.
            DATA_WRITE (3):
                Data resource access write permission.
            DATA_READ (4):
                Data resource access read permission.
        """

        UNKNOWN_PERMISSION_TYPE = 0
        ADMIN_WRITE = 1
        ADMIN_READ = 2
        DATA_WRITE = 3
        DATA_READ = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    type_: PermissionType = proto.Field(
        proto.ENUM,
        number=3,
        enum=PermissionType,
    )


class Role(proto.Message):
    r"""System role for resource access and modification.

    Attributes:
        name (str):
            System role name for user.
        description (str):
            System role description for user.
        type_ (google.backstory.types.Role.Type):
            System role type for well known roles.
    """

    class Type(proto.Enum):
        r"""Well-known system roles.

        Values:
            TYPE_UNSPECIFIED (0):
                Default user role.
            ADMINISTRATOR (1):
                Product administrator with elevated
                privileges.
            SERVICE_ACCOUNT (2):
                System service account for automated
                privilege access.
        """

        TYPE_UNSPECIFIED = 0
        ADMINISTRATOR = 1
        SERVICE_ACCOUNT = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    type_: Type = proto.Field(
        proto.ENUM,
        number=3,
        enum=Type,
    )


class Group(proto.Message):
    r"""Information about an organizational group.

    Attributes:
        product_object_id (str):
            Product globally unique user object
            identifier, such as an LDAP Object Identifier.
        creation_time (google.protobuf.timestamp_pb2.Timestamp):
            Group creation time. Deprecated: creation_time should be
            populated in Attribute as generic metadata.
        group_display_name (str):
            Group display name. e.g. "Finance".
        attribute (google.backstory.types.Attribute):
            Generic entity metadata attributes of the
            group.
        email_addresses (MutableSequence[str]):
            Email addresses of the group.
        windows_sid (str):
            Microsoft Windows SID of the group.
    """

    product_object_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    creation_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=100,
        message=timestamp_pb2.Timestamp,
    )
    group_display_name: str = proto.Field(
        proto.STRING,
        number=101,
    )
    attribute: "Attribute" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="Attribute",
    )
    email_addresses: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    windows_sid: str = proto.Field(
        proto.STRING,
        number=3,
    )


class Registry(proto.Message):
    r"""Information about a registry key or value.

    Attributes:
        registry_key (str):
            Registry key associated with an application or system
            component (e.g., HKEY\_, HKCU\\Environment...).
        registry_value_name (str):
            Name of the registry value associated with an
            application or system component (e.g. TEMP).
        registry_value_data (str):
            Data associated with a registry value
            (e.g. %USERPROFILE%\Local Settings\Temp).
        registry_value_type (google.backstory.types.Registry.Type):
            Type of the registry value.
        registry_value_binary_data (bytes):
            Binary data associated with a registry value.
            This field is only populated if the registry
            value type is BINARY. This field is not
            populated for other registry value types.
    """

    class Type(proto.Enum):
        r"""Type of the registry value. These values are based on the
        Windows Registry value types:

        https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-value-types

        Values:
            TYPE_UNSPECIFIED (0):
                Default registry value type used when the
                type is unknown.
            NONE (1):
                The registry value is not set and only the
                key exists.
            SZ (2):
                A null-terminated string.
            EXPAND_SZ (3):
                A null-terminated string that contains
                unexpanded references to environment variables
            BINARY (4):
                Binary data in any form.
            DWORD (5):
                A 32-bit number.
            DWORD_LITTLE_ENDIAN (6):
                A 32-bit number in little-endian format.
            DWORD_BIG_ENDIAN (7):
                A 32-bit number in big-endian format.
            LINK (8):
                A null-terminated Unicode string that
                contains the target path of a symbolic link.
            MULTI_SZ (9):
                A sequence of null-terminated strings,
                terminated by an empty string
            RESOURCE_LIST (10):
                A device driver resource list.
            QWORD (11):
                A 64-bit number.
            QWORD_LITTLE_ENDIAN (12):
                A 64-bit number in little-endian format.
        """

        TYPE_UNSPECIFIED = 0
        NONE = 1
        SZ = 2
        EXPAND_SZ = 3
        BINARY = 4
        DWORD = 5
        DWORD_LITTLE_ENDIAN = 6
        DWORD_BIG_ENDIAN = 7
        LINK = 8
        MULTI_SZ = 9
        RESOURCE_LIST = 10
        QWORD = 11
        QWORD_LITTLE_ENDIAN = 12

    registry_key: str = proto.Field(
        proto.STRING,
        number=1,
    )
    registry_value_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    registry_value_data: str = proto.Field(
        proto.STRING,
        number=3,
    )
    registry_value_type: Type = proto.Field(
        proto.ENUM,
        number=4,
        enum=Type,
    )
    registry_value_binary_data: bytes = proto.Field(
        proto.BYTES,
        number=5,
    )


class WmiPersistenceItem(proto.Message):
    r"""Information about a WMI persistence item.

    Attributes:
        caption (str):
            A brief title or caption for the WMI object.
        name (str):
            The name of the WMI object.
        setting_id (str):
            The identifier for the setting.
        derivation (str):
            The base class from which the WMI class is derived (e.g.,
            CIM_Setting).
        property_count (int):
            The number of properties in the WMI object.
        rel_path (str):
            The relative path to the WMI object (e.g.,
            Win32_StartupCommand.Command=''').
        dynasty (str):
            The top-level class in the WMI inheritance hierarchy (e.g.,
            CMI_Setting).
        wmi_super_class (str):
            The immediate parent class in the WMI
            inheritance hierarchy.
        wmi_class (str):
            The name of the WMI class.
        genus (int):
            An integer representing the type or version
            of the WMI object.
    """

    caption: str = proto.Field(
        proto.STRING,
        number=1,
    )
    name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    setting_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    derivation: str = proto.Field(
        proto.STRING,
        number=4,
    )
    property_count: int = proto.Field(
        proto.INT64,
        number=5,
    )
    rel_path: str = proto.Field(
        proto.STRING,
        number=6,
    )
    dynasty: str = proto.Field(
        proto.STRING,
        number=7,
    )
    wmi_super_class: str = proto.Field(
        proto.STRING,
        number=8,
    )
    wmi_class: str = proto.Field(
        proto.STRING,
        number=9,
    )
    genus: int = proto.Field(
        proto.INT64,
        number=10,
    )


class Location(proto.Message):
    r"""Information about a location.

    Attributes:
        city (str):
            The city.
        state (str):
            The state.
        country_or_region (str):
            The country or region.
        name (str):
            Custom location name (e.g. building or site
            name like "London Office"). For cloud
            environments, this is the region (e.g.
            "us-west2").
        desk_name (str):
            Desk name or individual location, typically
            for an employee in an office.
            (e.g. "IN-BLR-BCPC-11-1121D").
        floor_name (str):
            Floor name, number or a combination of the
            two for a building. (e.g. "1-A").
        region_latitude (float):
            Deprecated: use region_coordinates.
        region_longitude (float):
            Deprecated: use region_coordinates.
        region_coordinates (google.type.latlng_pb2.LatLng):
            Coordinates for the associated region. See
            https://cloud.google.com/vision/docs/reference/rest/v1/LatLng
            for a description of the fields.
    """

    city: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: str = proto.Field(
        proto.STRING,
        number=2,
    )
    country_or_region: str = proto.Field(
        proto.STRING,
        number=3,
    )
    name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    desk_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    floor_name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    region_latitude: float = proto.Field(
        proto.FLOAT,
        number=7,
    )
    region_longitude: float = proto.Field(
        proto.FLOAT,
        number=8,
    )
    region_coordinates: latlng_pb2.LatLng = proto.Field(
        proto.MESSAGE,
        number=9,
        message=latlng_pb2.LatLng,
    )


class ScheduledTask(proto.Message):
    r"""Deprecated: use WindowsScheduledTask for Windows scheduled
    tasks or ScheduledCronTask for cron jobs.
    Information about a scheduled task.

    Attributes:
        minute (int):
            The minute of the hour (0-59).
        hour (int):
            The hour of the day (0-23).
        month_day (int):
            The day of the month (1-31).
        month (int):
            The month of the year (1-12).
        week_day (int):
            The day of the week (0-6, Sunday=0).
        comment (str):
            A comment or description for the task.
        author (str):
            The account name that authored or last
            modified the scheduled task.
    """

    minute: int = proto.Field(
        proto.INT32,
        number=1,
    )
    hour: int = proto.Field(
        proto.INT32,
        number=2,
    )
    month_day: int = proto.Field(
        proto.INT32,
        number=3,
    )
    month: int = proto.Field(
        proto.INT32,
        number=4,
    )
    week_day: int = proto.Field(
        proto.INT32,
        number=5,
    )
    comment: str = proto.Field(
        proto.STRING,
        number=6,
    )
    author: str = proto.Field(
        proto.STRING,
        number=7,
    )


class WindowsScheduledTask(proto.Message):
    r"""Information about a Windows scheduled task.

    Attributes:
        author (str):
            The account name that authored or last
            modified the scheduled task.
        virtual_path (str):
            The task's path in the Task Scheduler
            library.
        exit_code (int):
            The result which was returned the last time
            the registered task was run.
        state (google.backstory.types.WindowsScheduledTask.TaskState):
            The operation state of the task.
        logon_type (google.backstory.types.WindowsScheduledTask.TaskLogonType):
            The logon type of the task.
        task_actions (MutableSequence[google.backstory.types.WindowsScheduledTask.TaskAction]):
            The actions of the scheduled task.
        task_triggers (MutableSequence[google.backstory.types.WindowsScheduledTask.TaskTrigger]):
            The triggers of the scheduled task.
    """

    class TaskState(proto.Enum):
        r"""Enum representing the operation state of the task.

        Values:
            TASK_STATE_UNSPECIFIED (0):
                The state of the task is unknown or not
                specified.
            DISABLED (1):
                The task is registered but is disabled and no
                instances of the task are queued or running. The
                task cannot be run until it is enabled.
            QUEUED (2):
                Instances of the task are queued.
            ACTIVE (3):
                The task is ready to be executed, but no
                instances are queued or running.
            RUNNING (4):
                One or more instances of the task are
                running.
        """

        TASK_STATE_UNSPECIFIED = 0
        DISABLED = 1
        QUEUED = 2
        ACTIVE = 3
        RUNNING = 4

    class TaskLogonType(proto.Enum):
        r"""Enum representing the logon type of the task.

        Values:
            TASK_LOGON_TYPE_UNSPECIFIED (0):
                The logon method is not specified. Used for
                non-NT credentials.
            PASSWORD (1):
                Use a password for logging on the user. The
                password must be supplied at registration time.
            S4U (2):
                Use an existing interactive token to run a
                task. The user must log on using a service for
                user (S4U) logon. When an S4U logon is used, no
                password is stored by the system and there is no
                access to either the network or encrypted files.
            INTERACTIVE_TOKEN (3):
                User must already be logged on. The task will
                be run only in an existing interactive session.
            GROUP (4):
                Logon with group credentials.
            SERVICE_ACCOUNT (5):
                Indicates that a Local System, Local Service,
                or Network Service account is being used as a
                security context to run the task.
            INTERACTIVE_TOKEN_OR_PASSWORD (6):
                First use the interactive token. If the user is not logged
                on (no interactive token is available), the password is
                used. The password must be specified when a task is
                registered. This flag is not recommended for new tasks
                because it is less reliable than TASK_LOGON_PASSWORD.
        """

        TASK_LOGON_TYPE_UNSPECIFIED = 0
        PASSWORD = 1
        S4U = 2
        INTERACTIVE_TOKEN = 3
        GROUP = 4
        SERVICE_ACCOUNT = 5
        INTERACTIVE_TOKEN_OR_PASSWORD = 6

    class TaskAction(proto.Message):
        r"""The task action.

        Attributes:
            action_type (google.backstory.types.WindowsScheduledTask.TaskAction.ActionType):
                The action type of the task.
            exec_arguments (MutableSequence[str]):
                The arguments of the task. This field is only
                populated if the task action type is EXEC.
            exec_working_directory (str):
                The executable working directory of the task.
                This field is only populated if the task action
                type is EXEC.
            com_class_id (str):
                The COM class IF the action is COM handler. This field is
                only populated if the task action type is COM_HANDLER.
            com_data (str):
                The data of the task. This field is only populated if the
                task action type is COM_HANDLER.
        """

        class ActionType(proto.Enum):
            r"""Enum representing the action type of the task.

            Values:
                ACTION_TYPE_UNSPECIFIED (0):
                    The action type is not specified.
                EXEC (1):
                    This action performs a command-line
                    operation. For example, the action can run a
                    script, launch an executable, or, if the name of
                    a document is provided, find its associated
                    application and launch the application with the
                    document.
                COM_HANDLER (2):
                    This action fires a handler. This action can only be used if
                    the task Compatibility property is set to
                    TASK_COMPATIBILITY_V2.
                SEND_EMAIL (3):
                    This action sends an email message. This action can only be
                    used if the task Compatibility property is set to
                    TASK_COMPATIBILITY_V2.
                SHOW_MESSAGE (4):
                    This action shows a message box. This action can only be
                    used if the task Compatibility property is set to
                    TASK_COMPATIBILITY_V2.
            """

            ACTION_TYPE_UNSPECIFIED = 0
            EXEC = 1
            COM_HANDLER = 2
            SEND_EMAIL = 3
            SHOW_MESSAGE = 4

        action_type: "WindowsScheduledTask.TaskAction.ActionType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="WindowsScheduledTask.TaskAction.ActionType",
        )
        exec_arguments: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        exec_working_directory: str = proto.Field(
            proto.STRING,
            number=3,
        )
        com_class_id: str = proto.Field(
            proto.STRING,
            number=4,
        )
        com_data: str = proto.Field(
            proto.STRING,
            number=5,
        )

    class TaskTrigger(proto.Message):
        r"""The trigger of the scheduled task.

        Attributes:
            enabled (bool):
                Indicates whether the task trigger is
                enabled.
            duration (google.protobuf.duration_pb2.Duration):
                The duration of the task trigger repetition.
            interval (str):
                The interval between each repetition of the task. The format
                for this string is ``P<days>DT<hours>H<minutes>M<seconds>S``
                (for example, "PT5M" is 5 minutes, "PT1H" is 1 hour, and
                "PT20M" is 20 minutes). The maximum time allowed is 31 days,
                and the minimum time allowed is 1 minute.
            trigger_type (google.backstory.types.WindowsScheduledTask.TaskTrigger.TriggerType):
                The trigger frequency of the task.
        """

        class TriggerType(proto.Enum):
            r"""Enum representing the trigger type of the task. For more details,
            see
            https://learn.microsoft.com/en-us/windows/win32/api/taskschd/ne-taskschd-task_trigger_type2.

            Values:
                TRIGGER_TYPE_UNSPECIFIED (0):
                    The trigger frequency is not specified.
                EVENT (1):
                    Triggers the task when a specific event
                    occurs.
                TIME (2):
                    Triggers the task at a specific time of day.
                DAILY (3):
                    Triggers the task on a daily schedule. For
                    example, the task starts at a specific time
                    every day, every other day, or every third day.
                WEEKLY (4):
                    Triggers the task on a weekly schedule. For
                    example, the task starts at 8:00 AM on a
                    specific day every week or other week.
                MONTHLY (5):
                    Triggers the task on a monthly schedule. For
                    example, the task starts on specific days of
                    specific months.
                MONTHLYDOW (6):
                    Triggers the task on a monthly day-of-week
                    schedule. For example, the task starts on a
                    specific days of the week, weeks of the month,
                    and months of the year.
                IDLE (7):
                    Triggers the task when the computer goes into
                    an idle state.
                REGISTRATION (8):
                    Triggers the task when the task is
                    registered.
                BOOT (9):
                    Triggers the task when the computer boots.
                LOGON (10):
                    Triggers the task when a specific user logs
                    on.
                SESSION_STATE_CHANGE (11):
                    Triggers the task when a specific user
                    session state changes.
                CUSTOM_TRIGGER01 (12):
                    Custom trigger 01.
            """

            TRIGGER_TYPE_UNSPECIFIED = 0
            EVENT = 1
            TIME = 2
            DAILY = 3
            WEEKLY = 4
            MONTHLY = 5
            MONTHLYDOW = 6
            IDLE = 7
            REGISTRATION = 8
            BOOT = 9
            LOGON = 10
            SESSION_STATE_CHANGE = 11
            CUSTOM_TRIGGER01 = 12

        enabled: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        duration: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=2,
            message=duration_pb2.Duration,
        )
        interval: str = proto.Field(
            proto.STRING,
            number=3,
        )
        trigger_type: "WindowsScheduledTask.TaskTrigger.TriggerType" = proto.Field(
            proto.ENUM,
            number=4,
            enum="WindowsScheduledTask.TaskTrigger.TriggerType",
        )

    author: str = proto.Field(
        proto.STRING,
        number=1,
    )
    virtual_path: str = proto.Field(
        proto.STRING,
        number=2,
    )
    exit_code: int = proto.Field(
        proto.INT32,
        number=3,
    )
    state: TaskState = proto.Field(
        proto.ENUM,
        number=4,
        enum=TaskState,
    )
    logon_type: TaskLogonType = proto.Field(
        proto.ENUM,
        number=5,
        enum=TaskLogonType,
    )
    task_actions: MutableSequence[TaskAction] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=TaskAction,
    )
    task_triggers: MutableSequence[TaskTrigger] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=TaskTrigger,
    )


class ScheduledCronTask(proto.Message):
    r"""Information about a scheduled cron task.

    Attributes:
        minute (str):
            Crontab minute field. Value is an integer between 0 and 59
            and can also be a range or list of values (e.g., "0-59",
            "0-59/5", "0,15,30,45") and it // can also be an asterisk
            (\*) to indicate first-last minutes. More on crontab format
            can be found here:
            https://www.linux.org/docs/man5/crontab.html
        hour (str):
            Crontab hour field. Value is an integer between 0 and 23, a
            range or list of values (e.g., "0-6", "*/2", "1,2"), or an
            asterisk (*) to indicate first-last hours.
        month_day (str):
            Crontab day of month field. Value is an integer between 1
            and 31, a range or list of values (e.g., "1-7", "1-31/7",
            "1,15"), or an asterisk (\*) to indicate first-last days of
            month.
        month (str):
            Crontab month field. Value is an integer between 1 and 12 or
            a 3-letter name (e.g., "Jan"), a range or list of values
            (e.g., "1-3", "*/2", "1,6"), or an asterisk (*) to indicate
            first-last months.
        week_day (str):
            Crontab day of week field. Value is an integer between 0 and
            7 (0 or 7 is Sunday) or a 3-letter name (e.g., "Fri"), a
            range or list of values (e.g., "1-5", "0,6"), or an asterisk
            (\*) to indicate first-last days of week.
        comment (str):
            A comment or description for the task.
        author (str):
            The author or creator of the task.
        event (str):
            Crontab special string or event (e.g.,
            "@reboot", "@daily").
        path (str):
            The PATH environment variable defined in the
            crontab file.
    """

    minute: str = proto.Field(
        proto.STRING,
        number=1,
    )
    hour: str = proto.Field(
        proto.STRING,
        number=2,
    )
    month_day: str = proto.Field(
        proto.STRING,
        number=3,
    )
    month: str = proto.Field(
        proto.STRING,
        number=4,
    )
    week_day: str = proto.Field(
        proto.STRING,
        number=5,
    )
    comment: str = proto.Field(
        proto.STRING,
        number=6,
    )
    author: str = proto.Field(
        proto.STRING,
        number=7,
    )
    event: str = proto.Field(
        proto.STRING,
        number=8,
    )
    path: str = proto.Field(
        proto.STRING,
        number=9,
    )


class ScheduledAnacronTask(proto.Message):
    r"""Information about a scheduled anacron task.

    Attributes:
        period (str):
            Anacrontab period field. Value is an integer
            in days, or a string like "@daily", "@weekly",
            or "@monthly".
        delay_minutes (int):
            The delay in minutes before the job is run.
        job_id (str):
            The unique identifier of the job.
        path (str):
            The PATH environment variable defined in the
            anacrontab file.
        source_line (str):
            The original source line from the anacrontab
            file.
    """

    period: str = proto.Field(
        proto.STRING,
        number=1,
    )
    delay_minutes: int = proto.Field(
        proto.INT64,
        number=2,
    )
    job_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    path: str = proto.Field(
        proto.STRING,
        number=4,
    )
    source_line: str = proto.Field(
        proto.STRING,
        number=5,
    )


class Volume(proto.Message):
    r"""Information about a storage volume.

    Attributes:
        file_system (str):
            The name of the file system on the volume
            (e.g., "NTFS", "FAT32").
        mount_point (str):
            The path where the volume is mounted (e.g.,
            "C:", "/mnt/data").
        device_path (str):
            The system path to the device (e.g.,
            "\\.\HarddiskVolume1", "/dev/sda1").
        is_mounted (bool):
            Indicates whether the volume is currently
            mounted.
        is_read_only (bool):
            Indicates whether the volume is mounted as
            read-only.
        name (str):
            The user-assigned label or name for the
            volume.
    """

    file_system: str = proto.Field(
        proto.STRING,
        number=1,
    )
    mount_point: str = proto.Field(
        proto.STRING,
        number=2,
    )
    device_path: str = proto.Field(
        proto.STRING,
        number=3,
    )
    is_mounted: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    is_read_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    name: str = proto.Field(
        proto.STRING,
        number=6,
    )


class Service(proto.Message):
    r"""Information about a Windows service.

    Attributes:
        display_name (str):
            The user-friendly display name of the
            service.
        service_type (google.backstory.types.Service.ServiceType):
            Deprecated: use service_types instead. The type of service.
        service_types (MutableSequence[google.backstory.types.Service.ServiceType]):
            The list of service types.
        startup_type (google.backstory.types.Service.StartupType):
            The startup type of the service.
        state (google.backstory.types.Service.State):
            The status of the service.
    """

    class ServiceType(proto.Enum):
        r"""The type of service.

        Values:
            SERVICE_TYPE_UNSPECIFIED (0):
                Default service type.
            KERNEL_DRIVER (1):
                A kernel driver.
            FILE_SYSTEM_DRIVER (2):
                A file system driver.
            WIN32_OWN_PROCESS (3):
                A process that is owned by the service. This
                is a Windows-specific service type.
            WIN32_SHARE_PROCESS (4):
                A process that is shared by the service. This
                is a Windows-specific service type.
            ADAPTER (5):
                An adapter. This is a Windows-specific
                service type.
            RECOGNIZER_DRIVER (6):
                A recognizer driver. This is a
                Windows-specific service type.
            INTERACTIVE_PROCESS (7):
                An interactive process. This is a
                Windows-specific service type.
        """

        SERVICE_TYPE_UNSPECIFIED = 0
        KERNEL_DRIVER = 1
        FILE_SYSTEM_DRIVER = 2
        WIN32_OWN_PROCESS = 3
        WIN32_SHARE_PROCESS = 4
        ADAPTER = 5
        RECOGNIZER_DRIVER = 6
        INTERACTIVE_PROCESS = 7

    class StartupType(proto.Enum):
        r"""How the service is started.

        Values:
            STARTUP_TYPE_UNSPECIFIED (0):
                Default startup type.
            AUTOMATIC (1):
                The service is started automatically.
            MANUAL (2):
                The service is started manually by a user.
            DISABLED (3):
                The service is disabled and will not start
                automatically.
        """

        STARTUP_TYPE_UNSPECIFIED = 0
        AUTOMATIC = 1
        MANUAL = 2
        DISABLED = 3

    class State(proto.Enum):
        r"""The current status of the service.

        Values:
            STATE_UNSPECIFIED (0):
                Default service status.
            RUNNING (1):
                The service is running.
            STOPPED (2):
                The service is stopped. This is a
                Windows-specific service status.
            PAUSED (3):
                The service is paused. This is a
                Windows-specific service status.
            COMPLETED (4):
                The service is completed.
            START_PENDING (5):
                The service is starting.
            STOP_PENDING (6):
                The service is stopping.
            PAUSE_PENDING (7):
                The service is pausing.
            CONTINUE_PENDING (8):
                The service is continuing.
        """

        STATE_UNSPECIFIED = 0
        RUNNING = 1
        STOPPED = 2
        PAUSED = 3
        COMPLETED = 4
        START_PENDING = 5
        STOP_PENDING = 6
        PAUSE_PENDING = 7
        CONTINUE_PENDING = 8

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    service_type: ServiceType = proto.Field(
        proto.ENUM,
        number=3,
        enum=ServiceType,
    )
    service_types: MutableSequence[ServiceType] = proto.RepeatedField(
        proto.ENUM,
        number=6,
        enum=ServiceType,
    )
    startup_type: StartupType = proto.Field(
        proto.ENUM,
        number=4,
        enum=StartupType,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )


class Resource(proto.Message):
    r"""Information about a resource such as a task, Cloud Storage
    bucket, database, disk, logical policy, or something similar.

    Attributes:
        type_ (str):
            Deprecated: use resource_type instead.
        resource_type (google.backstory.types.Resource.ResourceType):
            Resource type.
        resource_subtype (str):
            Resource sub-type (e.g. "BigQuery",
            "Bigtable").
        id (str):
            Deprecated: Use resource.name or resource.product_object_id.
        name (str):
            The full name of the resource. For example,
            Google Cloud:
            //cloudresourcemanager.googleapis.com/projects/wombat-123,
            and AWS: arn:aws:iam::123456789012:user/johndoe.
        parent (str):
            The parent of the resource. For a database table, the parent
            is the database. For a storage object, the bucket name.
            Deprecated: use resource_ancestors.name.
        product_object_id (str):
            A vendor-specific identifier to uniquely
            identify the entity (a GUID, OID, or similar)
            This field can be used as an entity indicator
            for a Resource entity.
        attribute (google.backstory.types.Attribute):
            Generic entity metadata attributes of the
            resource.
        scheduled_task (google.backstory.types.ScheduledTask):
            DEPRECATED: use windows_scheduled_task for Windows scheduled
            tasks or scheduled_cron_task for cron jobs. Information
            about a scheduled task associated with the resource.
        scheduled_cron_task (google.backstory.types.ScheduledCronTask):
            Information about a scheduled cron task
            associated with the resource.
        scheduled_anacron_task (google.backstory.types.ScheduledAnacronTask):
            Information about a scheduled anacron task
            associated with the resource.
        windows_scheduled_task (google.backstory.types.WindowsScheduledTask):
            Information about a Windows scheduled task
            associated with the resource.
        volume (google.backstory.types.Volume):
            Information about a storage volume associated
            with the resource.
        service (google.backstory.types.Service):
            Information about a Windows service
            associated with the resource.
    """

    class ResourceType(proto.Enum):
        r"""The type of resource.

        Values:
            UNSPECIFIED (0):
                Default type.
            MUTEX (1):
                Mutex.
            TASK (2):
                Task.
            PIPE (3):
                Named pipe.
            DEVICE (4):
                Device.
            FIREWALL_RULE (5):
                Firewall rule.
            MAILBOX_FOLDER (6):
                Mailbox folder.
            VPC_NETWORK (7):
                VPC Network.
            VIRTUAL_MACHINE (8):
                Virtual machine.
            STORAGE_BUCKET (9):
                Storage bucket.
            STORAGE_OBJECT (10):
                Storage object.
            DATABASE (11):
                Database.
            TABLE (12):
                Data table.
            CLOUD_PROJECT (13):
                Cloud project.
            CLOUD_ORGANIZATION (14):
                Cloud organization.
            SERVICE_ACCOUNT (15):
                Service account.
            ACCESS_POLICY (16):
                Access policy.
            CLUSTER (17):
                Cluster.
            SETTING (18):
                Settings.
            DATASET (19):
                Dataset.
            BACKEND_SERVICE (20):
                Endpoint that receive traffic from a load
                balancer or proxy.
            POD (21):
                Pod, which is a collection of containers.
                Often used in Kubernetes.
            CONTAINER (22):
                Container.
            FUNCTION (23):
                Cloud function.
            RUNTIME (24):
                Runtime.
            IP_ADDRESS (25):
                IP address.
            DISK (26):
                Disk.
            VOLUME (27):
                Volume.
            IMAGE (28):
                Machine image.
            SNAPSHOT (29):
                Snapshot.
            REPOSITORY (30):
                Repository.
            CREDENTIAL (31):
                Credential, e.g. access keys, ssh keys,
                tokens, certificates.
            LOAD_BALANCER (32):
                Load balancer.
            GATEWAY (33):
                Gateway.
            SUBNET (34):
                Subnet.
            USER (35):
                User.
            SERVICE (36):
                Service.
        """

        UNSPECIFIED = 0
        MUTEX = 1
        TASK = 2
        PIPE = 3
        DEVICE = 4
        FIREWALL_RULE = 5
        MAILBOX_FOLDER = 6
        VPC_NETWORK = 7
        VIRTUAL_MACHINE = 8
        STORAGE_BUCKET = 9
        STORAGE_OBJECT = 10
        DATABASE = 11
        TABLE = 12
        CLOUD_PROJECT = 13
        CLOUD_ORGANIZATION = 14
        SERVICE_ACCOUNT = 15
        ACCESS_POLICY = 16
        CLUSTER = 17
        SETTING = 18
        DATASET = 19
        BACKEND_SERVICE = 20
        POD = 21
        CONTAINER = 22
        FUNCTION = 23
        RUNTIME = 24
        IP_ADDRESS = 25
        DISK = 26
        VOLUME = 27
        IMAGE = 28
        SNAPSHOT = 29
        REPOSITORY = 30
        CREDENTIAL = 31
        LOAD_BALANCER = 32
        GATEWAY = 33
        SUBNET = 34
        USER = 35
        SERVICE = 36

    type_: str = proto.Field(
        proto.STRING,
        number=1,
    )
    resource_type: ResourceType = proto.Field(
        proto.ENUM,
        number=5,
        enum=ResourceType,
    )
    resource_subtype: str = proto.Field(
        proto.STRING,
        number=6,
    )
    id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=4,
    )
    product_object_id: str = proto.Field(
        proto.STRING,
        number=8,
    )
    attribute: "Attribute" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="Attribute",
    )
    scheduled_task: "ScheduledTask" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="ScheduledTask",
    )
    scheduled_cron_task: "ScheduledCronTask" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="ScheduledCronTask",
    )
    scheduled_anacron_task: "ScheduledAnacronTask" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="ScheduledAnacronTask",
    )
    windows_scheduled_task: "WindowsScheduledTask" = proto.Field(
        proto.MESSAGE,
        number=14,
        message="WindowsScheduledTask",
    )
    volume: "Volume" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="Volume",
    )
    service: "Service" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="Service",
    )


class Label(proto.Message):
    r"""Key value labels.

    Attributes:
        key (str):
            The key.
        value (str):
            The value.
        source (str):
            Where the label is derived from.
        rbac_enabled (bool):
            Indicates whether this label can be used for
            Data RBAC
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
    rbac_enabled: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class Cloud(proto.Message):
    r"""Metadata related to the cloud environment.

    Attributes:
        environment (google.backstory.types.Cloud.CloudEnvironment):
            The Cloud environment.
        vpc (google.backstory.types.Resource):
            The cloud environment VPC.
            Deprecated.
        project (google.backstory.types.Resource):
            The cloud environment project information. Deprecated: Use
            Resource.resource_ancestors
        availability_zone (str):
            The cloud environment availability zone
            (different from region which is location.name).
    """

    class CloudEnvironment(proto.Enum):
        r"""The service provider environment.

        Values:
            UNSPECIFIED_CLOUD_ENVIRONMENT (0):
                Default.
            GOOGLE_CLOUD_PLATFORM (1):
                Google Cloud Platform.
            AMAZON_WEB_SERVICES (2):
                Amazon Web Services.
            MICROSOFT_AZURE (3):
                Microsoft Azure.
        """

        UNSPECIFIED_CLOUD_ENVIRONMENT = 0
        GOOGLE_CLOUD_PLATFORM = 1
        AMAZON_WEB_SERVICES = 2
        MICROSOFT_AZURE = 3

    environment: CloudEnvironment = proto.Field(
        proto.ENUM,
        number=1,
        enum=CloudEnvironment,
    )
    vpc: "Resource" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Resource",
    )
    project: "Resource" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Resource",
    )
    availability_zone: str = proto.Field(
        proto.STRING,
        number=4,
    )


class Artifact(proto.Message):
    r"""Information about an artifact. The artifact can only be an
    IP.

    Attributes:
        ip (str):
            IP address of the artifact.
            This field can be used as an entity indicator
            for an external destination IP entity.
        prevalence (google.backstory.types.Prevalence):
            The prevalence of the artifact within the
            customer's environment.
        first_seen_time (google.protobuf.timestamp_pb2.Timestamp):
            First seen timestamp of the IP in the
            customer's environment.
        last_seen_time (google.protobuf.timestamp_pb2.Timestamp):
            Last seen timestamp of the IP address in the
            customer's environment.
        location (google.backstory.types.Location):
            Location of the Artifact's IP address.
        network (google.backstory.types.Network):
            Network information related to the Artifact's
            IP address.
        as_owner (str):
            Owner of the Autonomous System to which the
            IP address belongs.
        asn (int):
            Autonomous System Number to which the IP
            address belongs.
        jarm (str):
            The JARM hash for the IP address.
            (https://engineering.salesforce.com/easily-identify-malicious-servers-on-the-internet-with-jarm-e095edac525a).
        last_https_certificate (google.backstory.types.SSLCertificate):
            SSL certificate information about the IP
            address.
        last_https_certificate_date (google.protobuf.timestamp_pb2.Timestamp):
            Most recent date for the certificate in
            VirusTotal.
        regional_internet_registry (str):
            RIR (one of the current RIRs: AFRINIC, ARIN,
            APNIC, LACNIC or RIPE NCC).
        tags (MutableSequence[str]):
            Identification attributes
        whois (str):
            WHOIS information as returned from the
            pertinent WHOIS server.
        whois_date (google.protobuf.timestamp_pb2.Timestamp):
            Date of the last update of the WHOIS record
            in VirusTotal.
        tunnels (MutableSequence[google.backstory.types.Tunnels]):
            VPN tunnels.
        anonymous (bool):
            Whether the VPN tunnels are configured for
            anonymous browsing or not.
        artifact_client (google.backstory.types.ArtifactClient):
            Entity or software accessing or utilizing
            network resources.
        risks (MutableSequence[str]):
            This field lists potential risks associated
            with the network activity.
    """

    ip: str = proto.Field(
        proto.STRING,
        number=1,
    )
    prevalence: "Prevalence" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Prevalence",
    )
    first_seen_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    last_seen_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    location: "Location" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="Location",
    )
    network: "Network" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="Network",
    )
    as_owner: str = proto.Field(
        proto.STRING,
        number=7,
    )
    asn: int = proto.Field(
        proto.INT64,
        number=8,
    )
    jarm: str = proto.Field(
        proto.STRING,
        number=9,
    )
    last_https_certificate: "SSLCertificate" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="SSLCertificate",
    )
    last_https_certificate_date: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    regional_internet_registry: str = proto.Field(
        proto.STRING,
        number=12,
    )
    tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=13,
    )
    whois: str = proto.Field(
        proto.STRING,
        number=14,
    )
    whois_date: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=15,
        message=timestamp_pb2.Timestamp,
    )
    tunnels: MutableSequence["Tunnels"] = proto.RepeatedField(
        proto.MESSAGE,
        number=16,
        message="Tunnels",
    )
    anonymous: bool = proto.Field(
        proto.BOOL,
        number=17,
    )
    artifact_client: "ArtifactClient" = proto.Field(
        proto.MESSAGE,
        number=18,
        message="ArtifactClient",
    )
    risks: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=19,
    )


class Tunnels(proto.Message):
    r"""VPN tunnels.

    Attributes:
        provider (str):
            The provider of the VPN tunnels being used.
        type_ (str):
            The type of the VPN tunnels.
    """

    provider: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ArtifactClient(proto.Message):
    r"""Entity or software accessing or utilizing network resources.

    Attributes:
        behaviors (MutableSequence[str]):
            The behaviors of the client accessing the
            network.
        proxies (MutableSequence[str]):
            The type of proxies used by the client.
    """

    behaviors: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    proxies: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class Favicon(proto.Message):
    r"""Difference hash and MD5 hash of the domain's favicon.

    Attributes:
        raw_md5 (str):
            Favicon's MD5 hash.
        dhash (str):
            Difference hash.
    """

    raw_md5: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dhash: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DNSRecord(proto.Message):
    r"""DNS record.

    Attributes:
        type_ (str):
            Type.
        value (str):
            Value.
        ttl (google.protobuf.duration_pb2.Duration):
            Time to live.
        priority (int):
            Priority.
        retry (int):
            Retry.
        refresh (google.protobuf.duration_pb2.Duration):
            Refresh.
        minimum (google.protobuf.duration_pb2.Duration):
            Minimum.
        expire (google.protobuf.duration_pb2.Duration):
            Expire.
        serial (int):
            Serial.
        rname (str):
            Rname.
    """

    type_: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: str = proto.Field(
        proto.STRING,
        number=2,
    )
    ttl: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )
    priority: int = proto.Field(
        proto.INT64,
        number=4,
    )
    retry: int = proto.Field(
        proto.INT64,
        number=5,
    )
    refresh: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=6,
        message=duration_pb2.Duration,
    )
    minimum: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=7,
        message=duration_pb2.Duration,
    )
    expire: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=8,
        message=duration_pb2.Duration,
    )
    serial: int = proto.Field(
        proto.INT64,
        number=9,
    )
    rname: str = proto.Field(
        proto.STRING,
        number=10,
    )


class SSLCertificate(proto.Message):
    r"""SSL certificate.

    Attributes:
        cert_signature (google.backstory.types.SSLCertificate.CertSignature):
            Certificate's signature and algorithm.
        extension (google.backstory.types.SSLCertificate.Extension):
            (DEPRECATED) certificate's extension.
        cert_extensions (google.protobuf.struct_pb2.Struct):
            Certificate's extensions.
        first_seen_time (google.protobuf.timestamp_pb2.Timestamp):
            Date the certificate was first retrieved by
            VirusTotal.
        issuer (google.backstory.types.SSLCertificate.Subject):
            Certificate's issuer data.
        ec (google.backstory.types.SSLCertificate.EC):
            EC public key information.
        serial_number (str):
            Certificate's serial number hexdump.
        signature_algorithm (str):
            Algorithm used for the signature (for
            example, "sha1RSA").
        size (int):
            Certificate content length.
        subject (google.backstory.types.SSLCertificate.Subject):
            Certificate's subject data.
        thumbprint (str):
            Certificate's content SHA1 hash.
        thumbprint_sha256 (str):
            Certificate's content SHA256 hash.
        validity (google.backstory.types.SSLCertificate.Validity):
            Certificate's validity period.
        version (str):
            Certificate version (typically "V1", "V2" or
            "V3").
        public_key (google.backstory.types.SSLCertificate.PublicKey):
            Public key information.
    """

    class CertSignature(proto.Message):
        r"""Certificate's signature and algorithm.

        Attributes:
            signature (str):
                Signature.
            signature_algorithm (str):
                Algorithm.
        """

        signature: str = proto.Field(
            proto.STRING,
            number=1,
        )
        signature_algorithm: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class AuthorityKeyId(proto.Message):
        r"""Identifies the public key to be used to verify the signature
        on this certificate or CRL.

        Attributes:
            keyid (str):
                Key hexdump.
            serial_number (str):
                Serial number hexdump.
        """

        keyid: str = proto.Field(
            proto.STRING,
            number=1,
        )
        serial_number: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class Extension(proto.Message):
        r"""Certificate's extensions.

        Attributes:
            ca (bool):
                Whether the subject acts as a certificate
                authority (CA) or not.
            subject_key_id (str):
                Identifies the public key being certified.
            authority_key_id (google.backstory.types.SSLCertificate.AuthorityKeyId):
                Identifies the public key to be used to
                verify the signature on this certificate or CRL.
            key_usage (str):
                The purpose for which the certified public
                key is used.
            ca_info_access (str):
                Authority information access locations are
                URLs that are added to a certificate in its
                authority information access extension.
            crl_distribution_points (str):
                CRL distribution points to which a
                certificate user should refer to ascertain if
                the certificate has been revoked.
            extended_key_usage (str):
                One or more purposes for which the certified
                public key may be used, in addition to or in
                place of the basic purposes indicated in the key
                usage extension field.
            subject_alternative_name (str):
                Contains one or more alternative names, using
                any of a variety of name forms, for the entity
                that is bound by the CA to the certified public
                key.
            certificate_policies (str):
                Different certificate policies will relate to
                different applications which may use the
                certified key.
            netscape_cert_comment (str):
                Used to include free-form text comments
                inside certificates.
            cert_template_name_dc (str):
                BMP data value "DomainController". See MS
                Q291010.
            netscape_certificate (bool):
                Identify whether the certificate subject is
                an SSL client, an SSL server, or a CA.
            pe_logotype (bool):
                Whether the certificate includes a logotype.
            old_authority_key_id (bool):
                Whether the certificate has an old authority
                key identifier extension.
        """

        ca: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        subject_key_id: str = proto.Field(
            proto.STRING,
            number=2,
        )
        authority_key_id: "SSLCertificate.AuthorityKeyId" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="SSLCertificate.AuthorityKeyId",
        )
        key_usage: str = proto.Field(
            proto.STRING,
            number=6,
        )
        ca_info_access: str = proto.Field(
            proto.STRING,
            number=7,
        )
        crl_distribution_points: str = proto.Field(
            proto.STRING,
            number=8,
        )
        extended_key_usage: str = proto.Field(
            proto.STRING,
            number=9,
        )
        subject_alternative_name: str = proto.Field(
            proto.STRING,
            number=10,
        )
        certificate_policies: str = proto.Field(
            proto.STRING,
            number=11,
        )
        netscape_cert_comment: str = proto.Field(
            proto.STRING,
            number=12,
        )
        cert_template_name_dc: str = proto.Field(
            proto.STRING,
            number=13,
        )
        netscape_certificate: bool = proto.Field(
            proto.BOOL,
            number=14,
        )
        pe_logotype: bool = proto.Field(
            proto.BOOL,
            number=15,
        )
        old_authority_key_id: bool = proto.Field(
            proto.BOOL,
            number=16,
        )

    class Subject(proto.Message):
        r"""Subject data.

        Attributes:
            country_name (str):
                C: Country name.
            common_name (str):
                CN: CommonName.
            locality (str):
                L: Locality.
            organization (str):
                O: Organization.
            organizational_unit (str):
                OU: OrganizationalUnit.
            state_or_province_name (str):
                ST: StateOrProvinceName.
        """

        country_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        common_name: str = proto.Field(
            proto.STRING,
            number=2,
        )
        locality: str = proto.Field(
            proto.STRING,
            number=3,
        )
        organization: str = proto.Field(
            proto.STRING,
            number=4,
        )
        organizational_unit: str = proto.Field(
            proto.STRING,
            number=5,
        )
        state_or_province_name: str = proto.Field(
            proto.STRING,
            number=6,
        )

    class RSA(proto.Message):
        r"""RSA public key information.

        Attributes:
            key_size (int):
                Key size.
            modulus (str):
                Key modulus hexdump.
            exponent (str):
                Key exponent hexdump.
        """

        key_size: int = proto.Field(
            proto.INT64,
            number=1,
        )
        modulus: str = proto.Field(
            proto.STRING,
            number=2,
        )
        exponent: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class EC(proto.Message):
        r"""EC public key information.

        Attributes:
            oid (str):
                Curve name.
            pub (str):
                Public key hexdump.
        """

        oid: str = proto.Field(
            proto.STRING,
            number=1,
        )
        pub: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class PublicKey(proto.Message):
        r"""Subject public key info.

        Attributes:
            algorithm (str):
                Any of "RSA", "DSA" or "EC". Indicates the
                algorithm used to generate the certificate.
            rsa (google.backstory.types.SSLCertificate.RSA):
                RSA public key information.
        """

        algorithm: str = proto.Field(
            proto.STRING,
            number=1,
        )
        rsa: "SSLCertificate.RSA" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="SSLCertificate.RSA",
        )

    class Validity(proto.Message):
        r"""Defines certificate's validity period.

        Attributes:
            expiry_time (google.protobuf.timestamp_pb2.Timestamp):
                Expiry date.
            issue_time (google.protobuf.timestamp_pb2.Timestamp):
                Issue date.
        """

        expiry_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=1,
            message=timestamp_pb2.Timestamp,
        )
        issue_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
        )

    cert_signature: CertSignature = proto.Field(
        proto.MESSAGE,
        number=1,
        message=CertSignature,
    )
    extension: Extension = proto.Field(
        proto.MESSAGE,
        number=2,
        message=Extension,
    )
    cert_extensions: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=14,
        message=struct_pb2.Struct,
    )
    first_seen_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    issuer: Subject = proto.Field(
        proto.MESSAGE,
        number=4,
        message=Subject,
    )
    ec: EC = proto.Field(
        proto.MESSAGE,
        number=5,
        message=EC,
    )
    serial_number: str = proto.Field(
        proto.STRING,
        number=6,
    )
    signature_algorithm: str = proto.Field(
        proto.STRING,
        number=7,
    )
    size: int = proto.Field(
        proto.INT64,
        number=8,
    )
    subject: Subject = proto.Field(
        proto.MESSAGE,
        number=9,
        message=Subject,
    )
    thumbprint: str = proto.Field(
        proto.STRING,
        number=10,
    )
    thumbprint_sha256: str = proto.Field(
        proto.STRING,
        number=11,
    )
    validity: Validity = proto.Field(
        proto.MESSAGE,
        number=12,
        message=Validity,
    )
    version: str = proto.Field(
        proto.STRING,
        number=13,
    )
    public_key: PublicKey = proto.Field(
        proto.MESSAGE,
        number=15,
        message=PublicKey,
    )


class PopularityRank(proto.Message):
    r"""Domain's position in popularity ranks for sources such as
    Alexa, Quantcast, or Statvoo.

    Attributes:
        giver (str):
            Name of the rank serial number hexdump.
        rank (int):
            Rank position.
        ingestion_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp when the rank was ingested.
    """

    giver: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rank: int = proto.Field(
        proto.INT64,
        number=2,
    )
    ingestion_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class Tracker(proto.Message):
    r"""URL Tracker.

    Attributes:
        tracker (str):
            Tracker name.
        id (str):
            Tracker ID, if available.
        timestamp (google.protobuf.timestamp_pb2.Timestamp):
            Tracker ingestion date.
        url (str):
            Tracker script URL.
    """

    tracker: str = proto.Field(
        proto.STRING,
        number=1,
    )
    id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    timestamp: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    url: str = proto.Field(
        proto.STRING,
        number=4,
    )


class Url(proto.Message):
    r"""Url.

    Attributes:
        url (str):
            URL.
        categories (MutableSequence[str]):
            Categorisation done by VirusTotal partners.
        favicon (google.backstory.types.Favicon):
            Difference hash and MD5 hash of the URL's.
        html_meta (google.protobuf.struct_pb2.Struct):
            Meta tags (only for URLs downloading HTML).
        last_final_url (str):
            If the original URL redirects, where does it
            end.
        last_http_response_code (int):
            HTTP response code of the last response.
        last_http_response_content_length (int):
            Length in bytes of the content received.
        last_http_response_content_sha256 (str):
            URL response body's SHA256 hash.
        last_http_response_cookies (google.protobuf.struct_pb2.Struct):
            Website's cookies.
        last_http_response_headers (google.protobuf.struct_pb2.Struct):
            Headers and values of the last HTTP response.
        tags (MutableSequence[str]):
            Tags.
        title (str):
            Webpage title.
        trackers (MutableSequence[google.backstory.types.Tracker]):
            Trackers found in the URL in a historical
            manner.
    """

    url: str = proto.Field(
        proto.STRING,
        number=1,
    )
    categories: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    favicon: "Favicon" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Favicon",
    )
    html_meta: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=4,
        message=struct_pb2.Struct,
    )
    last_final_url: str = proto.Field(
        proto.STRING,
        number=5,
    )
    last_http_response_code: int = proto.Field(
        proto.INT32,
        number=6,
    )
    last_http_response_content_length: int = proto.Field(
        proto.INT64,
        number=7,
    )
    last_http_response_content_sha256: str = proto.Field(
        proto.STRING,
        number=8,
    )
    last_http_response_cookies: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=9,
        message=struct_pb2.Struct,
    )
    last_http_response_headers: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=10,
        message=struct_pb2.Struct,
    )
    tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=11,
    )
    title: str = proto.Field(
        proto.STRING,
        number=12,
    )
    trackers: MutableSequence["Tracker"] = proto.RepeatedField(
        proto.MESSAGE,
        number=13,
        message="Tracker",
    )


class Domain(proto.Message):
    r"""Information about a domain.

    Attributes:
        name (str):
            The domain name.
            This field can be used as an entity indicator
            for Domain entities.
        prevalence (google.backstory.types.Prevalence):
            The prevalence of the domain within the
            customer's environment.
        first_seen_time (google.protobuf.timestamp_pb2.Timestamp):
            First seen timestamp of the domain in the
            customer's environment.
        last_seen_time (google.protobuf.timestamp_pb2.Timestamp):
            Last seen timestamp of the domain in the
            customer's environment.
        registrar (str):
            Registrar name . FOr example, "Wild West
            Domains, Inc. (R120-LROR)", "GoDaddy.com, LLC",
            or "PDR LTD. D/B/A PUBLICDOMAINREGISTRY.COM".
        contact_email (str):
            Contact email address.
        whois_server (str):
            Whois server name.
        name_server (MutableSequence[str]):
            Repeated list of name servers.
        creation_time (google.protobuf.timestamp_pb2.Timestamp):
            Domain creation time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Last updated time.
        expiration_time (google.protobuf.timestamp_pb2.Timestamp):
            Expiration time.
        audit_update_time (google.protobuf.timestamp_pb2.Timestamp):
            Audit updated time.
        status (str):
            Domain status. See
            https://www.icann.org/resources/pages/epp-status-codes-2014-06-16-en
            for meanings of possible values
        registrant (google.backstory.types.User):
            Parsed contact information for the registrant
            of the domain.
        admin (google.backstory.types.User):
            Parsed contact information for the
            administrative contact for the domain.
        tech (google.backstory.types.User):
            Parsed contact information for the technical
            contact for the domain
        billing (google.backstory.types.User):
            Parsed contact information for the billing
            contact of the domain.
        zone (google.backstory.types.User):
            Parsed contact information for the zone.
        whois_record_raw_text (bytes):
            WHOIS raw text.
        registry_data_raw_text (bytes):
            Registry Data raw text.
        iana_registrar_id (int):
            IANA Registrar ID. See
            https://www.iana.org/assignments/registrar-ids/registrar-ids.xhtml
        private_registration (bool):
            Indicates whether the domain appears to be
            using a private registration service to mask the
            owner's contact information.
        categories (MutableSequence[str]):
            Categories assign to the domain as retrieved
            from VirusTotal.
        favicon (google.backstory.types.Favicon):
            Includes difference hash and MD5 hash of the
            domain's favicon.
        jarm (str):
            Domain's JARM hash.
        last_dns_records (MutableSequence[google.backstory.types.DNSRecord]):
            Domain's DNS records from the last scan.
        last_dns_records_time (google.protobuf.timestamp_pb2.Timestamp):
            Date when the DNS records list was retrieved
            by VirusTotal.
        last_https_certificate (google.backstory.types.SSLCertificate):
            SSL certificate object retrieved last time
            the domain was analyzed.
        last_https_certificate_time (google.protobuf.timestamp_pb2.Timestamp):
            When the certificate was retrieved by
            VirusTotal.
        popularity_ranks (MutableSequence[google.backstory.types.PopularityRank]):
            Domain's position in popularity ranks such as
            Alexa, Quantcast, Statvoo, etc
        tags (MutableSequence[str]):
            List of representative attributes.
        whois_time (google.protobuf.timestamp_pb2.Timestamp):
            Date of the last update of the WHOIS record.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    prevalence: "Prevalence" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Prevalence",
    )
    first_seen_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    last_seen_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    registrar: str = proto.Field(
        proto.STRING,
        number=5,
    )
    contact_email: str = proto.Field(
        proto.STRING,
        number=6,
    )
    whois_server: str = proto.Field(
        proto.STRING,
        number=7,
    )
    name_server: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    creation_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    expiration_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    audit_update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        message=timestamp_pb2.Timestamp,
    )
    status: str = proto.Field(
        proto.STRING,
        number=13,
    )
    registrant: "User" = proto.Field(
        proto.MESSAGE,
        number=14,
        message="User",
    )
    admin: "User" = proto.Field(
        proto.MESSAGE,
        number=15,
        message="User",
    )
    tech: "User" = proto.Field(
        proto.MESSAGE,
        number=16,
        message="User",
    )
    billing: "User" = proto.Field(
        proto.MESSAGE,
        number=17,
        message="User",
    )
    zone: "User" = proto.Field(
        proto.MESSAGE,
        number=18,
        message="User",
    )
    whois_record_raw_text: bytes = proto.Field(
        proto.BYTES,
        number=19,
    )
    registry_data_raw_text: bytes = proto.Field(
        proto.BYTES,
        number=20,
    )
    iana_registrar_id: int = proto.Field(
        proto.INT32,
        number=21,
    )
    private_registration: bool = proto.Field(
        proto.BOOL,
        number=22,
    )
    categories: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=23,
    )
    favicon: "Favicon" = proto.Field(
        proto.MESSAGE,
        number=24,
        message="Favicon",
    )
    jarm: str = proto.Field(
        proto.STRING,
        number=25,
    )
    last_dns_records: MutableSequence["DNSRecord"] = proto.RepeatedField(
        proto.MESSAGE,
        number=26,
        message="DNSRecord",
    )
    last_dns_records_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=27,
        message=timestamp_pb2.Timestamp,
    )
    last_https_certificate: "SSLCertificate" = proto.Field(
        proto.MESSAGE,
        number=28,
        message="SSLCertificate",
    )
    last_https_certificate_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=29,
        message=timestamp_pb2.Timestamp,
    )
    popularity_ranks: MutableSequence["PopularityRank"] = proto.RepeatedField(
        proto.MESSAGE,
        number=30,
        message="PopularityRank",
    )
    tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=31,
    )
    whois_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=32,
        message=timestamp_pb2.Timestamp,
    )


class Noun(proto.Message):
    r"""The Noun type is used to represent the different entities in
    an event: principal, src, target, observer, intermediary, and
    about. It stores attributes known about the entity. For example,
    if the entity is a device with multiple IP or MAC addresses, it
    stores the IP and MAC addresses that are relevant to the event.

    Attributes:
        hostname (str):
            Client hostname or domain name field.
            Hostname also doubles as the domain for remote
            entities. This field can be used as an entity
            indicator for asset entities.
        domain (google.backstory.types.Domain):
            Information about the domain.
        artifact (google.backstory.types.Artifact):
            Information about an artifact.
        url_metadata (google.backstory.types.Url):
            Information about the URL.
        browser (google.backstory.types.Browser):
            Information about an entry in the web
            browser's local history database.
        asset_id (str):
            The asset ID.
            This field can be used as an entity indicator
            for asset entities.
        user (google.backstory.types.User):
            Information about the user.
        user_management_chain (MutableSequence[google.backstory.types.User]):
            Information about the user's management chain (reporting
            hierarchy). Note: user_management_chain is only populated
            when data is exported to BigQuery since recursive fields
            (e.g. user.managers) are not supported by BigQuery.
        group (google.backstory.types.Group):
            Information about the group.
        process (google.backstory.types.Process):
            Information about the process.
        process_ancestors (MutableSequence[google.backstory.types.Process]):
            Information about the process's ancestors ordered from
            immediate ancestor (parent process) to root. Note:
            process_ancestors is only populated when data is exported to
            BigQuery since recursive fields (e.g.
            process.parent_process) are not supported by BigQuery.
        asset (google.backstory.types.Asset):
            Information about the asset.
        ip (MutableSequence[str]):
            A list of IP addresses associated with a
            network connection. This field can be used as an
            entity indicator for asset entities.
        nat_ip (MutableSequence[str]):
            A list of NAT translated IP addresses
            associated with a network connection.
        port (int):
            Source or destination network port number
            when a specific network connection is described
            within an event.
        nat_port (int):
            NAT external network port number when a
            specific network connection is described within
            an event.
        mac (MutableSequence[str]):
            List of MAC addresses associated with a
            device. This field can be used as an entity
            indicator for asset entities.
        administrative_domain (str):
            Domain which the device belongs to (for
            example, the Microsoft Windows domain).
        namespace (str):
            Namespace which the device belongs to, such
            as "AD forest". Uses for this field include
            Microsoft Windows AD forest, the name of
            subsidiary, or the name of acquisition.
            This field can be used along with an asset
            indicator to identify an asset.
        url (str):
            The URL.
        file (google.backstory.types.File):
            Information about the file.
        email (str):
            Email address. Only filled in for security_result.about
        registry (google.backstory.types.Registry):
            Registry information.
        application (str):
            The name of an application or service.
            Some SSO solutions only capture the name of a
            target application such as "Atlassian" or
            "Chronicle".
        platform (google.backstory.types.Noun.Platform):
            Platform.
        platform_version (str):
            Platform version. For example,
            "Microsoft Windows 1803".
        platform_patch_level (str):
            Platform patch level.
            For example, "Build 17134.48".
        cloud (google.backstory.types.Cloud):
            Cloud metadata.
            Deprecated: cloud should be populated in entity
            Attribute as generic metadata (e.g.
            asset.attribute.cloud).
        location (google.backstory.types.Location):
            Physical location. For cloud environments,
            set the region in location.name.
        ip_location (MutableSequence[google.backstory.types.Location]):
            Deprecated: use ip_geo_artifact.location instead.
        ip_geo_artifact (MutableSequence[google.backstory.types.Artifact]):
            Enriched geographic information corresponding
            to an IP address. Specifically, location and
            network data.
        resource (google.backstory.types.Resource):
            Information about the resource (e.g.
            scheduled task, calendar entry). This field
            should not be used for files, registry, or
            processes because these objects are already part
            of Noun.
        resource_ancestors (MutableSequence[google.backstory.types.Resource]):
            Information about the resource's ancestors
            ordered from immediate ancestor (starting with
            parent resource).
        labels (MutableSequence[google.backstory.types.Label]):
            Labels are key-value pairs.
            For example: key = "env", value = "prod".
            Deprecated: labels should be populated in entity
            Attribute as generic metadata (e.g.
            user.attribute.labels).
        object_reference (google.backstory.types.Id):
            Finding to which the Analyst updated the
            feedback.
        investigation (google.backstory.types.Investigation):
            Analyst feedback/investigation for alerts.
        network (google.backstory.types.Network):
            Network details, including sub-messages with
            details on each protocol (for example, DHCP,
            DNS, or HTTP).
        security_result (MutableSequence[google.backstory.types.SecurityResult]):
            A list of security results.
    """

    class Platform(proto.Enum):
        r"""Operating system platform.

        Values:
            UNKNOWN_PLATFORM (0):
                Default value.
            WINDOWS (1):
                Microsoft Windows.
            MAC (2):
                macOS.
            LINUX (3):
                Linux.
            GCP (4):
                Deprecated: see cloud.environment.
            AWS (5):
                Deprecated: see cloud.environment.
            AZURE (6):
                Deprecated: see cloud.environment.
            IOS (7):
                IOS
            ANDROID (8):
                Android
            CHROME_OS (9):
                Chrome OS
        """

        UNKNOWN_PLATFORM = 0
        WINDOWS = 1
        MAC = 2
        LINUX = 3
        GCP = 4
        AWS = 5
        AZURE = 6
        IOS = 7
        ANDROID = 8
        CHROME_OS = 9

    hostname: str = proto.Field(
        proto.STRING,
        number=1,
    )
    domain: "Domain" = proto.Field(
        proto.MESSAGE,
        number=30,
        message="Domain",
    )
    artifact: "Artifact" = proto.Field(
        proto.MESSAGE,
        number=32,
        message="Artifact",
    )
    url_metadata: "Url" = proto.Field(
        proto.MESSAGE,
        number=37,
        message="Url",
    )
    browser: "Browser" = proto.Field(
        proto.MESSAGE,
        number=38,
        message="Browser",
    )
    asset_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    user: "User" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="User",
    )
    user_management_chain: MutableSequence["User"] = proto.RepeatedField(
        proto.MESSAGE,
        number=29,
        message="User",
    )
    group: "Group" = proto.Field(
        proto.MESSAGE,
        number=20,
        message="Group",
    )
    process: "Process" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="Process",
    )
    process_ancestors: MutableSequence["Process"] = proto.RepeatedField(
        proto.MESSAGE,
        number=28,
        message="Process",
    )
    asset: "Asset" = proto.Field(
        proto.MESSAGE,
        number=27,
        message="Asset",
    )
    ip: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    nat_ip: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=21,
    )
    port: int = proto.Field(
        proto.INT32,
        number=7,
    )
    nat_port: int = proto.Field(
        proto.INT32,
        number=22,
    )
    mac: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    administrative_domain: str = proto.Field(
        proto.STRING,
        number=9,
    )
    namespace: str = proto.Field(
        proto.STRING,
        number=19,
    )
    url: str = proto.Field(
        proto.STRING,
        number=10,
    )
    file: "File" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="File",
    )
    email: str = proto.Field(
        proto.STRING,
        number=12,
    )
    registry: "Registry" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="Registry",
    )
    application: str = proto.Field(
        proto.STRING,
        number=14,
    )
    platform: Platform = proto.Field(
        proto.ENUM,
        number=5,
        enum=Platform,
    )
    platform_version: str = proto.Field(
        proto.STRING,
        number=15,
    )
    platform_patch_level: str = proto.Field(
        proto.STRING,
        number=16,
    )
    cloud: "Cloud" = proto.Field(
        proto.MESSAGE,
        number=24,
        message="Cloud",
    )
    location: "Location" = proto.Field(
        proto.MESSAGE,
        number=17,
        message="Location",
    )
    ip_location: MutableSequence["Location"] = proto.RepeatedField(
        proto.MESSAGE,
        number=34,
        message="Location",
    )
    ip_geo_artifact: MutableSequence["Artifact"] = proto.RepeatedField(
        proto.MESSAGE,
        number=35,
        message="Artifact",
    )
    resource: "Resource" = proto.Field(
        proto.MESSAGE,
        number=18,
        message="Resource",
    )
    resource_ancestors: MutableSequence["Resource"] = proto.RepeatedField(
        proto.MESSAGE,
        number=31,
        message="Resource",
    )
    labels: MutableSequence["Label"] = proto.RepeatedField(
        proto.MESSAGE,
        number=23,
        message="Label",
    )
    object_reference: gb_id.Id = proto.Field(
        proto.MESSAGE,
        number=25,
        message=gb_id.Id,
    )
    investigation: "Investigation" = proto.Field(
        proto.MESSAGE,
        number=26,
        message="Investigation",
    )
    network: "Network" = proto.Field(
        proto.MESSAGE,
        number=33,
        message="Network",
    )
    security_result: MutableSequence["SecurityResult"] = proto.RepeatedField(
        proto.MESSAGE,
        number=36,
        message="SecurityResult",
    )


class Investigation(proto.Message):
    r"""Represents the aggregated state of an investigation such as
    categorization, severity, and status. Can be expanded to include
    analyst assignment details and more.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        verdict (google.backstory.types.Verdict):
            Describes reason a finding investigation was
            resolved.

            This field is a member of `oneof`_ ``_verdict``.
        reputation (google.backstory.types.Reputation):
            Describes whether a finding was useful or
            not-useful.

            This field is a member of `oneof`_ ``_reputation``.
        severity_score (int):
            Severity score for a finding set by an
            analyst.

            This field is a member of `oneof`_ ``_severity_score``.
        status (google.backstory.types.Status):
            Describes the workflow status of a finding.

            This field is a member of `oneof`_ ``_status``.
        comments (MutableSequence[str]):
            Comment added by the Analyst.
        priority (google.backstory.types.Priority):
            Priority of the Alert or Finding set by
            analyst.

            This field is a member of `oneof`_ ``_priority``.
        root_cause (str):
            Root cause of the Alert or Finding set by
            analyst.

            This field is a member of `oneof`_ ``_root_cause``.
        reason (google.backstory.types.Reason):
            Reason for closing the Case or Alert.

            This field is a member of `oneof`_ ``_reason``.
        risk_score (int):
            Risk score for a finding set by an analyst.

            This field is a member of `oneof`_ ``_risk_score``.
        id (str):
            Identifier for the investigation

            This field is a member of `oneof`_ ``_id``.
    """

    verdict: "Verdict" = proto.Field(
        proto.ENUM,
        number=2,
        optional=True,
        enum="Verdict",
    )
    reputation: "Reputation" = proto.Field(
        proto.ENUM,
        number=3,
        optional=True,
        enum="Reputation",
    )
    severity_score: int = proto.Field(
        proto.UINT32,
        number=4,
        optional=True,
    )
    status: "Status" = proto.Field(
        proto.ENUM,
        number=5,
        optional=True,
        enum="Status",
    )
    comments: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    priority: "Priority" = proto.Field(
        proto.ENUM,
        number=7,
        optional=True,
        enum="Priority",
    )
    root_cause: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )
    reason: "Reason" = proto.Field(
        proto.ENUM,
        number=9,
        optional=True,
        enum="Reason",
    )
    risk_score: int = proto.Field(
        proto.UINT32,
        number=10,
        optional=True,
    )
    id: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )


class Tags(proto.Message):
    r"""Tags are event metadata which is set by examining event contents
    post-parsing. For example, a UDM event may be assigned a tenant_id
    based on certain customer-defined parameters.

    Attributes:
        tenant_id (MutableSequence[bytes]):
            A list of subtenant ids that this event
            belongs to.
        data_tap_config_name (MutableSequence[str]):
            A list of sink name values defined in DataTap
            configurations.
    """

    tenant_id: MutableSequence[bytes] = proto.RepeatedField(
        proto.BYTES,
        number=1,
    )
    data_tap_config_name: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class AttackDetails(proto.Message):
    r"""MITRE ATT&CK details.

    Attributes:
        version (str):
            ATT&CK version (e.g. 12.1).
        tactics (MutableSequence[google.backstory.types.AttackDetails.Tactic]):
            Tactics employed.
        techniques (MutableSequence[google.backstory.types.AttackDetails.Technique]):
            Techniques employed.
    """

    class Tactic(proto.Message):
        r"""Tactic information related to an attack or threat.

        Attributes:
            id (str):
                Tactic ID (e.g. "TA0043").
            name (str):
                Tactic Name (e.g. "Reconnaissance")
        """

        id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        name: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class Technique(proto.Message):
        r"""Technique information related to an attack or threat.

        Attributes:
            id (str):
                Technique ID (e.g. "T1595").
            name (str):
                Technique Name (e.g. "Active Scanning").
            subtechnique_id (str):
                Subtechnique ID (e.g. "T1595.001").
            subtechnique_name (str):
                Subtechnique Name (e.g. "Scanning IP
                Blocks").
        """

        id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        name: str = proto.Field(
            proto.STRING,
            number=2,
        )
        subtechnique_id: str = proto.Field(
            proto.STRING,
            number=3,
        )
        subtechnique_name: str = proto.Field(
            proto.STRING,
            number=4,
        )

    version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tactics: MutableSequence[Tactic] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=Tactic,
    )
    techniques: MutableSequence[Technique] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=Technique,
    )


class BoolSequence(proto.Message):
    r"""BoolSequence represents a sequence of bools.

    Attributes:
        bool_vals (MutableSequence[bool]):
            bool sequence.
    """

    bool_vals: MutableSequence[bool] = proto.RepeatedField(
        proto.BOOL,
        number=1,
    )


class BytesSequence(proto.Message):
    r"""BytesSequence represents a sequence of bytes.

    Attributes:
        bytes_vals (MutableSequence[bytes]):
            bytes sequence.
    """

    bytes_vals: MutableSequence[bytes] = proto.RepeatedField(
        proto.BYTES,
        number=1,
    )


class DoubleSequence(proto.Message):
    r"""DoubleSequence represents a sequence of doubles.

    Attributes:
        double_vals (MutableSequence[float]):
            double sequence.
    """

    double_vals: MutableSequence[float] = proto.RepeatedField(
        proto.DOUBLE,
        number=1,
    )


class Int64Sequence(proto.Message):
    r"""Int64Sequence represents a sequence of int64s.

    Attributes:
        int64_vals (MutableSequence[int]):
            int64 sequence.
    """

    int64_vals: MutableSequence[int] = proto.RepeatedField(
        proto.INT64,
        number=1,
    )


class Uint64Sequence(proto.Message):
    r"""Uint64Sequence represents a sequence of uint64s.

    Attributes:
        uint64_vals (MutableSequence[int]):
            uint64 sequence.
    """

    uint64_vals: MutableSequence[int] = proto.RepeatedField(
        proto.UINT64,
        number=1,
    )


class StringSequence(proto.Message):
    r"""StringSequence represents a sequence of string.

    Attributes:
        string_vals (MutableSequence[str]):
            string sequence.
    """

    string_vals: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class GroupedFields(proto.Message):
    r"""Grouped fields are aliases for groups of related UDM fields.
    All fields grouped together are of type string.

    Attributes:
        ip (MutableSequence[str]):
            IP addresses.
        domain (MutableSequence[str]):
            Domains.
        hostname (MutableSequence[str]):
            Hostnames.
        user (MutableSequence[str]):
            Users.
        email (MutableSequence[str]):
            Emails.
        file_path (MutableSequence[str]):
            File paths.
        hash_ (MutableSequence[str]):
            File Hashes.
        process_id (MutableSequence[str]):
            Process Identifiers.
    """

    ip: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    domain: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    hostname: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    user: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    email: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    file_path: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    hash_: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    process_id: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
