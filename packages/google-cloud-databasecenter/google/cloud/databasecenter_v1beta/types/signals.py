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
import google.protobuf.wrappers_pb2 as wrappers_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.databasecenter_v1beta.types import maintenance
from google.cloud.databasecenter_v1beta.types import (
    operation_error_type as gcd_operation_error_type,
)
from google.cloud.databasecenter_v1beta.types import product as gcd_product
from google.cloud.databasecenter_v1beta.types import (
    suspension_reason as gcd_suspension_reason,
)

__protobuf__ = proto.module(
    package="google.cloud.databasecenter.v1beta",
    manifest={
        "SignalStatus",
        "SignalSource",
        "IssueSeverity",
        "SignalType",
        "SignalTypeGroup",
        "SignalFilter",
        "SignalGroup",
        "IssueCount",
        "AdditionalDetail",
        "SubResource",
        "RetentionSettingsInfo",
        "AutomatedBackupPolicyInfo",
        "DeletionProtectionInfo",
        "ResourceSuspensionInfo",
        "BackupRunInfo",
        "InefficientQueryInfo",
        "SCCInfo",
        "RecommendationInfo",
        "RegulatoryStandard",
        "OutdatedMinorVersionInfo",
        "MaintenanceRecommendationInfo",
        "Signal",
    },
)


class SignalStatus(proto.Enum):
    r"""Represents the state of a signal. More enum values are
    expected to be added as needed.

    Values:
        SIGNAL_STATUS_UNSPECIFIED (0):
            Unspecified.
        SIGNAL_STATUS_NOT_APPLICABLE (1):
            Signal is not applicable to the resource.
        SIGNAL_STATUS_OK (2):
            Signal is not an issue.
        SIGNAL_STATUS_ISSUE (3):
            Signal is an issue.
        SIGNAL_STATUS_NOT_ENABLED (4):
            Signal is not enabled for the resource.
    """

    SIGNAL_STATUS_UNSPECIFIED = 0
    SIGNAL_STATUS_NOT_APPLICABLE = 1
    SIGNAL_STATUS_OK = 2
    SIGNAL_STATUS_ISSUE = 3
    SIGNAL_STATUS_NOT_ENABLED = 4


class SignalSource(proto.Enum):
    r"""Represents the source system from where a signal comes from.
    More enum values are expected to be added as needed.

    Values:
        SIGNAL_SOURCE_UNSPECIFIED (0):
            Unspecified.
        SIGNAL_SOURCE_RESOURCE_METADATA (1):
            Signal comes from resource metadata.
        SIGNAL_SOURCE_SECURITY_FINDINGS (2):
            Signal comes from SCC findings.
        SIGNAL_SOURCE_RECOMMENDER (3):
            Signal comes from recommender hub.
        SIGNAL_SOURCE_MODERN_OBSERVABILITY (4):
            Signal comes from modern observability
            platform.
    """

    SIGNAL_SOURCE_UNSPECIFIED = 0
    SIGNAL_SOURCE_RESOURCE_METADATA = 1
    SIGNAL_SOURCE_SECURITY_FINDINGS = 2
    SIGNAL_SOURCE_RECOMMENDER = 3
    SIGNAL_SOURCE_MODERN_OBSERVABILITY = 4


class IssueSeverity(proto.Enum):
    r"""IssueSeverity represents the severity of an issue.

    Values:
        ISSUE_SEVERITY_UNSPECIFIED (0):
            Unspecified.
        ISSUE_SEVERITY_LOW (1):
            Low severity.
        ISSUE_SEVERITY_MEDIUM (2):
            Medium severity.
        ISSUE_SEVERITY_HIGH (3):
            High severity.
        ISSUE_SEVERITY_CRITICAL (4):
            Critical severity.
        ISSUE_SEVERITY_IRRELEVANT (5):
            Irrelevant severity. This means the issue
            should not be surfaced at all.
    """

    ISSUE_SEVERITY_UNSPECIFIED = 0
    ISSUE_SEVERITY_LOW = 1
    ISSUE_SEVERITY_MEDIUM = 2
    ISSUE_SEVERITY_HIGH = 3
    ISSUE_SEVERITY_CRITICAL = 4
    ISSUE_SEVERITY_IRRELEVANT = 5


class SignalType(proto.Enum):
    r"""Represents the type of a signal. More values are expected to
    be added as needed.

    Values:
        SIGNAL_TYPE_UNSPECIFIED (0):
            Unspecified.
        SIGNAL_TYPE_RESOURCE_FAILOVER_PROTECTED (1):
            Represents if a resource is protected by
            automatic failover. Checks for resources that
            are configured to have redundancy within a
            region that enables automatic failover.
        SIGNAL_TYPE_GROUP_MULTIREGIONAL (2):
            Represents if a group is replicating across
            regions. Checks for resources that are
            configured to have redundancy, and ongoing
            replication, across regions.
        SIGNAL_TYPE_NO_AUTOMATED_BACKUP_POLICY (4):
            Represents if a resource has an automated
            backup policy.
        SIGNAL_TYPE_SHORT_BACKUP_RETENTION (5):
            Represents if a resources has a short backup
            retention period.
        SIGNAL_TYPE_LAST_BACKUP_FAILED (6):
            Represents if the last backup of a resource
            failed.
        SIGNAL_TYPE_LAST_BACKUP_OLD (7):
            Represents if the last backup of a resource
            is older than some threshold value.
        SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_2_0 (8):
            Represents if a resource violates CIS Google
            Cloud Platform Foundation 2.0.
        SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_3 (9):
            Represents if a resource violates CIS Google
            Cloud Platform Foundation 1.3.
        SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_2 (10):
            Represents if a resource violates CIS Google
            Cloud Platform Foundation 1.2.
        SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_1 (11):
            Represents if a resource violates CIS Google
            Cloud Platform Foundation 1.1.
        SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_0 (12):
            Represents if a resource violates CIS Google
            Cloud Platform Foundation 1.0.
        SIGNAL_TYPE_VIOLATES_CIS_CONTROLS_V8_0 (76):
            Represents if a resource violates CIS
            Controls 8.0.
        SIGNAL_TYPE_VIOLATES_NIST_800_53 (13):
            Represents if a resource violates NIST
            800-53.
        SIGNAL_TYPE_VIOLATES_NIST_800_53_R5 (69):
            Represents if a resource violates NIST 800-53
            R5.
        SIGNAL_TYPE_VIOLATES_NIST_CYBERSECURITY_FRAMEWORK_V1_0 (72):
            Represents if a resource violates NIST
            Cybersecurity Framework 1.0.
        SIGNAL_TYPE_VIOLATES_ISO_27001 (14):
            Represents if a resource violates ISO-27001.
        SIGNAL_TYPE_VIOLATES_ISO_27001_V2022 (70):
            Represents if a resource violates ISO 27001
            2022.
        SIGNAL_TYPE_VIOLATES_PCI_DSS_V3_2_1 (15):
            Represents if a resource violates PCI-DSS
            v3.2.1.
        SIGNAL_TYPE_VIOLATES_PCI_DSS_V4_0 (71):
            Represents if a resource violates PCI-DSS
            v4.0.
        SIGNAL_TYPE_VIOLATES_CLOUD_CONTROLS_MATRIX_V4 (73):
            Represents if a resource violates Cloud
            Controls Matrix v4.0.
        SIGNAL_TYPE_VIOLATES_HIPAA (74):
            Represents if a resource violates HIPAA.
        SIGNAL_TYPE_VIOLATES_SOC2_V2017 (75):
            Represents if a resource violates SOC2 v2017.
        SIGNAL_TYPE_LOGS_NOT_OPTIMIZED_FOR_TROUBLESHOOTING (16):
            Represents if log_checkpoints database flag for a Cloud SQL
            for PostgreSQL instance is not set to on.
        SIGNAL_TYPE_QUERY_DURATIONS_NOT_LOGGED (17):
            Represents if the log_duration database flag for a Cloud SQL
            for PostgreSQL instance is not set to on.
        SIGNAL_TYPE_VERBOSE_ERROR_LOGGING (18):
            Represents if the log_error_verbosity database flag for a
            Cloud SQL for PostgreSQL instance is not set to default or
            stricter (default or terse).
        SIGNAL_TYPE_QUERY_LOCK_WAITS_NOT_LOGGED (19):
            Represents if the log_lock_waits database flag for a Cloud
            SQL for PostgreSQL instance is not set to on.
        SIGNAL_TYPE_LOGGING_MOST_ERRORS (20):
            Represents if the log_min_error_statement database flag for
            a Cloud SQL for PostgreSQL instance is not set
            appropriately.
        SIGNAL_TYPE_LOGGING_ONLY_CRITICAL_ERRORS (21):
            Represents if the log_min_error_statement database flag for
            a Cloud SQL for PostgreSQL instance does not have an
            appropriate severity level.
        SIGNAL_TYPE_MINIMAL_ERROR_LOGGING (22):
            Represents if the log_min_messages database flag for a Cloud
            SQL for PostgreSQL instance is not set to warning or another
            recommended value.
        SIGNAL_TYPE_QUERY_STATS_LOGGED (23):
            Represents if the databaseFlags property of instance
            metadata for the log_executor_status field is set to on.
        SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_CLIENT_HOSTNAME (24):
            Represents if the log_hostname database flag for a Cloud SQL
            for PostgreSQL instance is not set to off.
        SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_PARSER_STATS (25):
            Represents if the log_parser_stats database flag for a Cloud
            SQL for PostgreSQL instance is not set to off.
        SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_PLANNER_STATS (26):
            Represents if the log_planner_stats database flag for a
            Cloud SQL for PostgreSQL instance is not set to off.
        SIGNAL_TYPE_NOT_LOGGING_ONLY_DDL_STATEMENTS (27):
            Represents if the log_statement database flag for a Cloud
            SQL for PostgreSQL instance is not set to DDL (all data
            definition statements).
        SIGNAL_TYPE_LOGGING_QUERY_STATS (28):
            Represents if the log_statement_stats database flag for a
            Cloud SQL for PostgreSQL instance is not set to off.
        SIGNAL_TYPE_NOT_LOGGING_TEMPORARY_FILES (29):
            Represents if the log_temp_files database flag for a Cloud
            SQL for PostgreSQL instance is not set to "0". (NOTE: 0 =
            ON)
        SIGNAL_TYPE_CONNECTION_MAX_NOT_CONFIGURED (30):
            Represents if the user connections database
            flag for a Cloud SQL for SQL Server instance is
            configured.
        SIGNAL_TYPE_USER_OPTIONS_CONFIGURED (31):
            Represents if the user options database flag
            for Cloud SQL SQL Server instance is configured
            or not.
        SIGNAL_TYPE_EXPOSED_TO_PUBLIC_ACCESS (32):
            Represents if a resource is exposed to public
            access.
        SIGNAL_TYPE_UNENCRYPTED_CONNECTIONS (33):
            Represents if a resources requires all
            incoming connections to use SSL or not.
        SIGNAL_TYPE_NO_ROOT_PASSWORD (34):
            Represents if a Cloud SQL database has a
            password configured for the root account or not.
        SIGNAL_TYPE_WEAK_ROOT_PASSWORD (35):
            Represents if a Cloud SQL database has a weak
            password configured for the root account.
        SIGNAL_TYPE_ENCRYPTION_KEY_NOT_CUSTOMER_MANAGED (36):
            Represents if a SQL database instance is not
            encrypted with customer-managed encryption keys
            (CMEK).
        SIGNAL_TYPE_SERVER_AUTHENTICATION_NOT_REQUIRED (37):
            Represents if The contained database
            authentication database flag for a Cloud SQL for
            SQL Server instance is not set to off.
        SIGNAL_TYPE_EXPOSED_TO_EXTERNAL_SCRIPTS (39):
            Represents if he external scripts enabled
            database flag for a Cloud SQL for SQL Server
            instance is not set to off.
        SIGNAL_TYPE_EXPOSED_TO_LOCAL_DATA_LOADS (40):
            Represents if the local_infile database flag for a Cloud SQL
            for MySQL instance is not set to off.
        SIGNAL_TYPE_CONNECTION_ATTEMPTS_NOT_LOGGED (41):
            Represents if the log_connections database flag for a Cloud
            SQL for PostgreSQL instance is not set to on.
        SIGNAL_TYPE_DISCONNECTIONS_NOT_LOGGED (42):
            Represents if the log_disconnections database flag for a
            Cloud SQL for PostgreSQL instance is not set to on.
        SIGNAL_TYPE_LOGGING_EXCESSIVE_STATEMENT_INFO (43):
            Represents if the log_min_duration_statement database flag
            for a Cloud SQL for PostgreSQL instance is not set to -1.
        SIGNAL_TYPE_EXPOSED_TO_REMOTE_ACCESS (44):
            Represents if the remote access database flag
            for a Cloud SQL for SQL Server instance is not
            set to off.
        SIGNAL_TYPE_DATABASE_NAMES_EXPOSED (45):
            Represents if the skip_show_database database flag for a
            Cloud SQL for MySQL instance is not set to on.
        SIGNAL_TYPE_SENSITIVE_TRACE_INFO_NOT_MASKED (46):
            Represents if the 3625 (trace flag) database
            flag for a Cloud SQL for SQL Server instance is
            not set to on.
        SIGNAL_TYPE_PUBLIC_IP_ENABLED (47):
            Represents if public IP is enabled.
        SIGNAL_TYPE_IDLE (48):
            Represents idle instance helps to reduce
            costs.
        SIGNAL_TYPE_OVERPROVISIONED (49):
            Represents instances that are unnecessarily
            large for given workload.
        SIGNAL_TYPE_HIGH_NUMBER_OF_OPEN_TABLES (50):
            Represents high number of concurrently opened
            tables.
        SIGNAL_TYPE_HIGH_NUMBER_OF_TABLES (51):
            Represents high table count close to SLA
            limit.
        SIGNAL_TYPE_HIGH_TRANSACTION_ID_UTILIZATION (52):
            Represents high number of unvacuumed
            transactions
        SIGNAL_TYPE_UNDERPROVISIONED (53):
            Represents need for more CPU and/or memory
        SIGNAL_TYPE_OUT_OF_DISK (54):
            Represents out of disk.
        SIGNAL_TYPE_SERVER_CERTIFICATE_NEAR_EXPIRY (55):
            Represents server certificate is near expiry.
        SIGNAL_TYPE_DATABASE_AUDITING_DISABLED (56):
            Represents database auditing is disabled.
        SIGNAL_TYPE_RESTRICT_AUTHORIZED_NETWORKS (57):
            Represents not restricted to authorized
            networks.
        SIGNAL_TYPE_VIOLATE_POLICY_RESTRICT_PUBLIC_IP (58):
            Represents violate org policy restrict public
            ip.
        SIGNAL_TYPE_QUOTA_LIMIT (59):
            Cluster nearing quota limit
        SIGNAL_TYPE_NO_PASSWORD_POLICY (60):
            No password policy set on resources
        SIGNAL_TYPE_CONNECTIONS_PERFORMANCE_IMPACT (61):
            Performance impact of connections settings
        SIGNAL_TYPE_TMP_TABLES_PERFORMANCE_IMPACT (62):
            Performance impact of temporary tables
            settings
        SIGNAL_TYPE_TRANS_LOGS_PERFORMANCE_IMPACT (63):
            Performance impact of transaction logs
            settings
        SIGNAL_TYPE_HIGH_JOINS_WITHOUT_INDEXES (64):
            Performance impact of high joins without
            indexes
        SIGNAL_TYPE_SUPERUSER_WRITING_TO_USER_TABLES (65):
            Detects events where a database superuser
            (postgres for PostgreSQL servers or root for
            MySQL users) writes to non-system tables.
        SIGNAL_TYPE_USER_GRANTED_ALL_PERMISSIONS (66):
            Detects events where a database user or role
            has been granted all privileges to a database,
            or to all tables, procedures, or functions in a
            schema.
        SIGNAL_TYPE_DATA_EXPORT_TO_EXTERNAL_CLOUD_STORAGE_BUCKET (67):
            Detects if database instance data exported to
            a Cloud Storage bucket outside of the
            organization.
        SIGNAL_TYPE_DATA_EXPORT_TO_PUBLIC_CLOUD_STORAGE_BUCKET (68):
            Detects if database instance data exported to
            a Cloud Storage bucket that is owned by the
            organization and is publicly accessible.
        SIGNAL_TYPE_WEAK_PASSWORD_HASH_ALGORITHM (77):
            Detects if a database instance is using a
            weak password hash algorithm.
        SIGNAL_TYPE_NO_USER_PASSWORD_POLICY (78):
            Detects if a database instance has no user
            password policy set.
        SIGNAL_TYPE_HOT_NODE (79):
            Detects if a database instance/cluster has a
            hot node.
        SIGNAL_TYPE_NO_DELETION_PROTECTION (80):
            Deletion Protection Disabled for the resource
        SIGNAL_TYPE_NO_POINT_IN_TIME_RECOVERY (81):
            Detects if a database instance has no point
            in time recovery enabled.
        SIGNAL_TYPE_RESOURCE_SUSPENDED (82):
            Detects if a database instance/cluster has
            suspended resources.
        SIGNAL_TYPE_EXPENSIVE_COMMANDS (83):
            Detects that expensive commands are being run
            on a database instance impacting overall
            performance.
        SIGNAL_TYPE_NO_MAINTENANCE_POLICY_CONFIGURED (84):
            Indicates that the instance does not have a
            maintenance policy configured.
        SIGNAL_TYPE_INEFFICIENT_QUERY (85):
            Indicates that the instance has inefficient
            queries detected.
        SIGNAL_TYPE_READ_INTENSIVE_WORKLOAD (86):
            Indicates that the instance has read
            intensive workload.
        SIGNAL_TYPE_MEMORY_LIMIT (87):
            Indicates that the instance is nearing memory
            limit.
        SIGNAL_TYPE_MAX_SERVER_MEMORY (88):
            Indicates that the instance's max server
            memory is configured higher than the recommended
            value.
        SIGNAL_TYPE_LARGE_ROWS (89):
            Indicates that the database has large rows
            beyond the recommended limit.
        SIGNAL_TYPE_HIGH_WRITE_PRESSURE (90):
            Heavy write pressure on the database rows.
        SIGNAL_TYPE_HIGH_READ_PRESSURE (91):
            Heavy read pressure on the database rows.
        SIGNAL_TYPE_ENCRYPTION_ORG_POLICY_NOT_SATISFIED (92):
            Encryption org policy not satisfied.
        SIGNAL_TYPE_LOCATION_ORG_POLICY_NOT_SATISFIED (93):
            Location org policy not satisfied.
        SIGNAL_TYPE_OUTDATED_MINOR_VERSION (94):
            Outdated DB minor version.
        SIGNAL_TYPE_SCHEMA_NOT_OPTIMIZED (95):
            Schema not optimized.
        SIGNAL_TYPE_REPLICATION_LAG (97):
            Replication delay.
        SIGNAL_TYPE_OUTDATED_CLIENT (99):
            Outdated client.
        SIGNAL_TYPE_DATABOOST_DISABLED (100):
            Databoost is disabled.
        SIGNAL_TYPE_RECOMMENDED_MAINTENANCE_POLICIES (101):
            Recommended maintenance policy.
        SIGNAL_TYPE_EXTENDED_SUPPORT (102):
            Resource version is in extended support.
        SIGNAL_TYPE_VERSION_NEARING_END_OF_LIFE (104):
            Represents a database version nearing end of
            life.
    """

    SIGNAL_TYPE_UNSPECIFIED = 0
    SIGNAL_TYPE_RESOURCE_FAILOVER_PROTECTED = 1
    SIGNAL_TYPE_GROUP_MULTIREGIONAL = 2
    SIGNAL_TYPE_NO_AUTOMATED_BACKUP_POLICY = 4
    SIGNAL_TYPE_SHORT_BACKUP_RETENTION = 5
    SIGNAL_TYPE_LAST_BACKUP_FAILED = 6
    SIGNAL_TYPE_LAST_BACKUP_OLD = 7
    SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_2_0 = 8
    SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_3 = 9
    SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_2 = 10
    SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_1 = 11
    SIGNAL_TYPE_VIOLATES_CIS_GCP_FOUNDATION_1_0 = 12
    SIGNAL_TYPE_VIOLATES_CIS_CONTROLS_V8_0 = 76
    SIGNAL_TYPE_VIOLATES_NIST_800_53 = 13
    SIGNAL_TYPE_VIOLATES_NIST_800_53_R5 = 69
    SIGNAL_TYPE_VIOLATES_NIST_CYBERSECURITY_FRAMEWORK_V1_0 = 72
    SIGNAL_TYPE_VIOLATES_ISO_27001 = 14
    SIGNAL_TYPE_VIOLATES_ISO_27001_V2022 = 70
    SIGNAL_TYPE_VIOLATES_PCI_DSS_V3_2_1 = 15
    SIGNAL_TYPE_VIOLATES_PCI_DSS_V4_0 = 71
    SIGNAL_TYPE_VIOLATES_CLOUD_CONTROLS_MATRIX_V4 = 73
    SIGNAL_TYPE_VIOLATES_HIPAA = 74
    SIGNAL_TYPE_VIOLATES_SOC2_V2017 = 75
    SIGNAL_TYPE_LOGS_NOT_OPTIMIZED_FOR_TROUBLESHOOTING = 16
    SIGNAL_TYPE_QUERY_DURATIONS_NOT_LOGGED = 17
    SIGNAL_TYPE_VERBOSE_ERROR_LOGGING = 18
    SIGNAL_TYPE_QUERY_LOCK_WAITS_NOT_LOGGED = 19
    SIGNAL_TYPE_LOGGING_MOST_ERRORS = 20
    SIGNAL_TYPE_LOGGING_ONLY_CRITICAL_ERRORS = 21
    SIGNAL_TYPE_MINIMAL_ERROR_LOGGING = 22
    SIGNAL_TYPE_QUERY_STATS_LOGGED = 23
    SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_CLIENT_HOSTNAME = 24
    SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_PARSER_STATS = 25
    SIGNAL_TYPE_EXCESSIVE_LOGGING_OF_PLANNER_STATS = 26
    SIGNAL_TYPE_NOT_LOGGING_ONLY_DDL_STATEMENTS = 27
    SIGNAL_TYPE_LOGGING_QUERY_STATS = 28
    SIGNAL_TYPE_NOT_LOGGING_TEMPORARY_FILES = 29
    SIGNAL_TYPE_CONNECTION_MAX_NOT_CONFIGURED = 30
    SIGNAL_TYPE_USER_OPTIONS_CONFIGURED = 31
    SIGNAL_TYPE_EXPOSED_TO_PUBLIC_ACCESS = 32
    SIGNAL_TYPE_UNENCRYPTED_CONNECTIONS = 33
    SIGNAL_TYPE_NO_ROOT_PASSWORD = 34
    SIGNAL_TYPE_WEAK_ROOT_PASSWORD = 35
    SIGNAL_TYPE_ENCRYPTION_KEY_NOT_CUSTOMER_MANAGED = 36
    SIGNAL_TYPE_SERVER_AUTHENTICATION_NOT_REQUIRED = 37
    SIGNAL_TYPE_EXPOSED_TO_EXTERNAL_SCRIPTS = 39
    SIGNAL_TYPE_EXPOSED_TO_LOCAL_DATA_LOADS = 40
    SIGNAL_TYPE_CONNECTION_ATTEMPTS_NOT_LOGGED = 41
    SIGNAL_TYPE_DISCONNECTIONS_NOT_LOGGED = 42
    SIGNAL_TYPE_LOGGING_EXCESSIVE_STATEMENT_INFO = 43
    SIGNAL_TYPE_EXPOSED_TO_REMOTE_ACCESS = 44
    SIGNAL_TYPE_DATABASE_NAMES_EXPOSED = 45
    SIGNAL_TYPE_SENSITIVE_TRACE_INFO_NOT_MASKED = 46
    SIGNAL_TYPE_PUBLIC_IP_ENABLED = 47
    SIGNAL_TYPE_IDLE = 48
    SIGNAL_TYPE_OVERPROVISIONED = 49
    SIGNAL_TYPE_HIGH_NUMBER_OF_OPEN_TABLES = 50
    SIGNAL_TYPE_HIGH_NUMBER_OF_TABLES = 51
    SIGNAL_TYPE_HIGH_TRANSACTION_ID_UTILIZATION = 52
    SIGNAL_TYPE_UNDERPROVISIONED = 53
    SIGNAL_TYPE_OUT_OF_DISK = 54
    SIGNAL_TYPE_SERVER_CERTIFICATE_NEAR_EXPIRY = 55
    SIGNAL_TYPE_DATABASE_AUDITING_DISABLED = 56
    SIGNAL_TYPE_RESTRICT_AUTHORIZED_NETWORKS = 57
    SIGNAL_TYPE_VIOLATE_POLICY_RESTRICT_PUBLIC_IP = 58
    SIGNAL_TYPE_QUOTA_LIMIT = 59
    SIGNAL_TYPE_NO_PASSWORD_POLICY = 60
    SIGNAL_TYPE_CONNECTIONS_PERFORMANCE_IMPACT = 61
    SIGNAL_TYPE_TMP_TABLES_PERFORMANCE_IMPACT = 62
    SIGNAL_TYPE_TRANS_LOGS_PERFORMANCE_IMPACT = 63
    SIGNAL_TYPE_HIGH_JOINS_WITHOUT_INDEXES = 64
    SIGNAL_TYPE_SUPERUSER_WRITING_TO_USER_TABLES = 65
    SIGNAL_TYPE_USER_GRANTED_ALL_PERMISSIONS = 66
    SIGNAL_TYPE_DATA_EXPORT_TO_EXTERNAL_CLOUD_STORAGE_BUCKET = 67
    SIGNAL_TYPE_DATA_EXPORT_TO_PUBLIC_CLOUD_STORAGE_BUCKET = 68
    SIGNAL_TYPE_WEAK_PASSWORD_HASH_ALGORITHM = 77
    SIGNAL_TYPE_NO_USER_PASSWORD_POLICY = 78
    SIGNAL_TYPE_HOT_NODE = 79
    SIGNAL_TYPE_NO_DELETION_PROTECTION = 80
    SIGNAL_TYPE_NO_POINT_IN_TIME_RECOVERY = 81
    SIGNAL_TYPE_RESOURCE_SUSPENDED = 82
    SIGNAL_TYPE_EXPENSIVE_COMMANDS = 83
    SIGNAL_TYPE_NO_MAINTENANCE_POLICY_CONFIGURED = 84
    SIGNAL_TYPE_INEFFICIENT_QUERY = 85
    SIGNAL_TYPE_READ_INTENSIVE_WORKLOAD = 86
    SIGNAL_TYPE_MEMORY_LIMIT = 87
    SIGNAL_TYPE_MAX_SERVER_MEMORY = 88
    SIGNAL_TYPE_LARGE_ROWS = 89
    SIGNAL_TYPE_HIGH_WRITE_PRESSURE = 90
    SIGNAL_TYPE_HIGH_READ_PRESSURE = 91
    SIGNAL_TYPE_ENCRYPTION_ORG_POLICY_NOT_SATISFIED = 92
    SIGNAL_TYPE_LOCATION_ORG_POLICY_NOT_SATISFIED = 93
    SIGNAL_TYPE_OUTDATED_MINOR_VERSION = 94
    SIGNAL_TYPE_SCHEMA_NOT_OPTIMIZED = 95
    SIGNAL_TYPE_REPLICATION_LAG = 97
    SIGNAL_TYPE_OUTDATED_CLIENT = 99
    SIGNAL_TYPE_DATABOOST_DISABLED = 100
    SIGNAL_TYPE_RECOMMENDED_MAINTENANCE_POLICIES = 101
    SIGNAL_TYPE_EXTENDED_SUPPORT = 102
    SIGNAL_TYPE_VERSION_NEARING_END_OF_LIFE = 104


class SignalTypeGroup(proto.Message):
    r"""A group of signal types that specifies what the user is interested
    in.

    Used by QueryDatabaseResourceGroups API.

    Example:

    signal_type_group { name = "AVAILABILITY" types =
    [SIGNAL_TYPE_NO_PROMOTABLE_REPLICA] }

    Attributes:
        display_name (str):
            Required. The display name of a signal group.
        signal_types (MutableSequence[google.cloud.databasecenter_v1beta.types.SignalType]):
            Optional. List of signal types present in the
            group.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    signal_types: MutableSequence["SignalType"] = proto.RepeatedField(
        proto.ENUM,
        number=2,
        enum="SignalType",
    )


class SignalFilter(proto.Message):
    r"""A filter for Signals.

    If signal_type is left unset, all signals should be returned. For
    example, the following filter returns all issues. signal_filter: {
    signal_status: SIGNAL_STATUS_ISSUE; }

    Another example, the following filter returns issues of the given
    type: signal_filter: { type: SIGNAL_TYPE_NO_PROMOTABLE_REPLICA
    signal_status: ISSUE }

    If signal_status is left unset or set to SIGNAL_STATE_UNSPECIFIED,
    an error should be returned.

    Attributes:
        signal_type (google.cloud.databasecenter_v1beta.types.SignalType):
            Optional. Represents the type of the Signal
            for which the filter is for.
        signal_status (google.cloud.databasecenter_v1beta.types.SignalStatus):
            Optional. Represents the status of the Signal
            for which the filter is for.
    """

    signal_type: "SignalType" = proto.Field(
        proto.ENUM,
        number=1,
        enum="SignalType",
    )
    signal_status: "SignalStatus" = proto.Field(
        proto.ENUM,
        number=2,
        enum="SignalStatus",
    )


class SignalGroup(proto.Message):
    r"""A group of signals and their counts.

    Attributes:
        display_name (str):
            Title of a signal group corresponding to the
            request.
        issue_count (int):
            When applied to a DatabaseResource represents count of
            issues associated with the resource. A signal is an issue
            when its SignalStatus field is set to SIGNAL_STATUS_ISSUE.
        signals (MutableSequence[google.cloud.databasecenter_v1beta.types.Signal]):
            List of signals present in the group and
            associated with the resource.
            Only applies to a DatabaseResource.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    issue_count: int = proto.Field(
        proto.INT32,
        number=2,
    )
    signals: MutableSequence["Signal"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="Signal",
    )


class IssueCount(proto.Message):
    r"""Count of issues for a group of signals.

    Attributes:
        display_name (str):
            Title of a signal group corresponding to the
            request.
        issue_count (int):
            The count of the number of issues associated with those
            resources that are explicitly filtered in by the filters
            present in the request. A signal is an issue when its
            SignalStatus field is set to SIGNAL_STATUS_ISSUE.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    issue_count: int = proto.Field(
        proto.INT32,
        number=2,
    )


class AdditionalDetail(proto.Message):
    r"""Details related to signal.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        short_backup_retention_info (google.cloud.databasecenter_v1beta.types.RetentionSettingsInfo):
            Short backup retention information applies to signals with
            type SIGNAL_TYPE_SHORT_BACKUP_RETENTION.

            This field is a member of `oneof`_ ``detail``.
        backup_run_info (google.cloud.databasecenter_v1beta.types.BackupRunInfo):
            Backup run information applies to signals with types
            SIGNAL_TYPE_LAST_BACKUP_FAILED and
            SIGNAL_TYPE_LAST_BACKUP_OLD.

            This field is a member of `oneof`_ ``detail``.
        scc_info (google.cloud.databasecenter_v1beta.types.SCCInfo):
            SCC information applies to SCC signals.

            This field is a member of `oneof`_ ``detail``.
        recommendation_info (google.cloud.databasecenter_v1beta.types.RecommendationInfo):
            Recommendation information applies to
            recommendations.

            This field is a member of `oneof`_ ``detail``.
        automated_backup_policy_info (google.cloud.databasecenter_v1beta.types.AutomatedBackupPolicyInfo):
            Automated backup policy information applies to signals with
            type SIGNAL_TYPE_NO_AUTOMATED_BACKUP_POLICY.

            This field is a member of `oneof`_ ``detail``.
        deletion_protection_info (google.cloud.databasecenter_v1beta.types.DeletionProtectionInfo):
            Deletion protection information applies to signals with type
            [SIGNAL_TYPE_NO_DELETION_PROTECTION][google.cloud.databasecenter.v1beta.SignalType.SIGNAL_TYPE_NO_DELETION_PROTECTION]

            This field is a member of `oneof`_ ``detail``.
        resource_suspension_info (google.cloud.databasecenter_v1beta.types.ResourceSuspensionInfo):
            Resource suspension information applies to signals with type
            [SIGNAL_TYPE_RESOURCE_SUSPENDED][google.cloud.databasecenter.v1beta.SignalType.SIGNAL_TYPE_RESOURCE_SUSPENDED].

            This field is a member of `oneof`_ ``detail``.
        inefficient_query_info (google.cloud.databasecenter_v1beta.types.InefficientQueryInfo):
            Inefficient query information applies to signals with type
            [SIGNAL_TYPE_INEFFICIENT_QUERY][google.cloud.databasecenter.v1beta.SignalType.SIGNAL_TYPE_INEFFICIENT_QUERY].

            This field is a member of `oneof`_ ``detail``.
        outdated_minor_version_info (google.cloud.databasecenter_v1beta.types.OutdatedMinorVersionInfo):
            Outdated minor version information applies to signals with
            type SIGNAL_TYPE_OUTDATED_MINOR_VERSION.

            This field is a member of `oneof`_ ``detail``.
        maintenance_recommendation_info (google.cloud.databasecenter_v1beta.types.MaintenanceRecommendationInfo):
            Maintenance recommendation information applies to signals
            with type SIGNAL_TYPE_RECOMMENDED_MAINTENANCE_POLICIES.

            This field is a member of `oneof`_ ``detail``.
        signal_source (google.cloud.databasecenter_v1beta.types.SignalSource):
            Where the signal is coming from.
        signal_type (google.cloud.databasecenter_v1beta.types.SignalType):
            Type of the signal.
        signal_event_time (google.protobuf.timestamp_pb2.Timestamp):
            Event time when signal was recorded by source
            service.
    """

    short_backup_retention_info: "RetentionSettingsInfo" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="detail",
        message="RetentionSettingsInfo",
    )
    backup_run_info: "BackupRunInfo" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="detail",
        message="BackupRunInfo",
    )
    scc_info: "SCCInfo" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="detail",
        message="SCCInfo",
    )
    recommendation_info: "RecommendationInfo" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="detail",
        message="RecommendationInfo",
    )
    automated_backup_policy_info: "AutomatedBackupPolicyInfo" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="detail",
        message="AutomatedBackupPolicyInfo",
    )
    deletion_protection_info: "DeletionProtectionInfo" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="detail",
        message="DeletionProtectionInfo",
    )
    resource_suspension_info: "ResourceSuspensionInfo" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="detail",
        message="ResourceSuspensionInfo",
    )
    inefficient_query_info: "InefficientQueryInfo" = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="detail",
        message="InefficientQueryInfo",
    )
    outdated_minor_version_info: "OutdatedMinorVersionInfo" = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="detail",
        message="OutdatedMinorVersionInfo",
    )
    maintenance_recommendation_info: "MaintenanceRecommendationInfo" = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="detail",
        message="MaintenanceRecommendationInfo",
    )
    signal_source: "SignalSource" = proto.Field(
        proto.ENUM,
        number=1,
        enum="SignalSource",
    )
    signal_type: "SignalType" = proto.Field(
        proto.ENUM,
        number=5,
        enum="SignalType",
    )
    signal_event_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )


class SubResource(proto.Message):
    r"""Sub resource details
    For Spanner/Bigtable instance certain data protection settings
    are at sub resource level like database/table.
    This message is used to capture such sub resource details.

    Attributes:
        resource_type (str):
            Optional. Resource type associated with the
            sub resource where backup settings are
            configured. E.g.
            "spanner.googleapis.com/Database" for Spanner
            where backup retention is configured on database
            within an instance OPTIONAL
        full_resource_name (str):
            Optional. Resource name associated with the
            sub resource where backup settings are
            configured.
            E.g."//spanner.googleapis.com/projects/project1/instances/inst1/databases/db1"
            for Spanner where backup retention is configured
            on database within an instance
            OPTIONAL
        product (google.cloud.databasecenter_v1beta.types.Product):
            Optional. Product information associated with the sub
            resource where backup retention settings are configured.
            e.g.

            ::

               product: {
                type   : PRODUCT_TYPE_SPANNER
                engine : ENGINE_CLOUD_SPANNER_WITH_POSTGRES_DIALECT
               }

            for Spanner where backup is configured on database within an
            instance OPTIONAL
        container (str):
            Specifies where the resource is created. For
            Google Cloud resources, it is the full name of
            the project.
    """

    resource_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    full_resource_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    product: gcd_product.Product = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcd_product.Product,
    )
    container: str = proto.Field(
        proto.STRING,
        number=4,
    )


class RetentionSettingsInfo(proto.Message):
    r"""Metadata about backup retention settings for a database
    resource.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        quantity_based_retention (google.protobuf.wrappers_pb2.Int32Value):
            Number of backups that will be retained.

            This field is a member of `oneof`_ ``retention``.
        duration_based_retention (google.protobuf.duration_pb2.Duration):
            Duration based retention period i.e. 172800
            seconds (2 days)

            This field is a member of `oneof`_ ``retention``.
        timestamp_based_retention_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp based retention period i.e. till
            2024-05-01T00:00:00Z

            This field is a member of `oneof`_ ``retention``.
        sub_resource (google.cloud.databasecenter_v1beta.types.SubResource):
            Optional. Sub resource details associated
            with the backup configuration.
    """

    quantity_based_retention: wrappers_pb2.Int32Value = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="retention",
        message=wrappers_pb2.Int32Value,
    )
    duration_based_retention: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="retention",
        message=duration_pb2.Duration,
    )
    timestamp_based_retention_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="retention",
        message=timestamp_pb2.Timestamp,
    )
    sub_resource: "SubResource" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="SubResource",
    )


class AutomatedBackupPolicyInfo(proto.Message):
    r"""Automated backup policy signal info

    Attributes:
        sub_resource (google.cloud.databasecenter_v1beta.types.SubResource):
            Optional. Sub resource details associated
            with the signal.
        is_enabled (bool):
            Is automated policy enabled.
    """

    sub_resource: "SubResource" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SubResource",
    )
    is_enabled: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class DeletionProtectionInfo(proto.Message):
    r"""Deletion protection signal info for a database resource.

    Attributes:
        sub_resource (google.cloud.databasecenter_v1beta.types.SubResource):
            Optional. Sub resource details associated
            with the signal.
        deletion_protection_enabled (bool):
            Is deletion protection enabled.
    """

    sub_resource: "SubResource" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SubResource",
    )
    deletion_protection_enabled: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class ResourceSuspensionInfo(proto.Message):
    r"""Resource suspension info for a database resource.

    Attributes:
        resource_suspended (bool):
            Is resource suspended.
        suspension_reason (google.cloud.databasecenter_v1beta.types.SuspensionReason):
            Suspension reason for the resource.
    """

    resource_suspended: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    suspension_reason: gcd_suspension_reason.SuspensionReason = proto.Field(
        proto.ENUM,
        number=2,
        enum=gcd_suspension_reason.SuspensionReason,
    )


class BackupRunInfo(proto.Message):
    r"""Metadata about latest backup run state for a database
    resource.

    Attributes:
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the backup operation started.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the backup operation completed.
        state (google.cloud.databasecenter_v1beta.types.BackupRunInfo.State):
            Output only. The state of this run.
        error_message (str):
            Additional information about the error
            encountered.
        operation_error_type (google.cloud.databasecenter_v1beta.types.OperationErrorType):
            Optional. OperationErrorType to expose
            specific error when backup operation of database
            resource failed, that is state is FAILED.
        sub_resource (google.cloud.databasecenter_v1beta.types.SubResource):
            Optional. Sub resource details associated
            with the backup run.
    """

    class State(proto.Enum):
        r"""The status of a backup run.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified.
            SUCCEEDED (1):
                The backup succeeded.
            FAILED (2):
                The backup was unsuccessful.
        """

        STATE_UNSPECIFIED = 0
        SUCCEEDED = 1
        FAILED = 2

    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=2,
        enum=State,
    )
    error_message: str = proto.Field(
        proto.STRING,
        number=3,
    )
    operation_error_type: gcd_operation_error_type.OperationErrorType = proto.Field(
        proto.ENUM,
        number=4,
        enum=gcd_operation_error_type.OperationErrorType,
    )
    sub_resource: "SubResource" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="SubResource",
    )


class InefficientQueryInfo(proto.Message):
    r"""Metadata about inefficient query signal info for a database
    resource.

    Attributes:
        database (str):
            Name of the database where index is required.
            For example, "db1", which is the name of the
            database present in the instance.
        table (str):
            Name of the table where index is required
        sql_index_statement (str):
            SQL statement of the index. Based on the ddl
            type, this will be either CREATE INDEX or DROP
            INDEX.
        storage_cost_bytes (int):
            Cost of additional disk usage in bytes
        impacted_queries_count (int):
            Count of queries to be impacted if index is
            applied
    """

    database: str = proto.Field(
        proto.STRING,
        number=1,
    )
    table: str = proto.Field(
        proto.STRING,
        number=2,
    )
    sql_index_statement: str = proto.Field(
        proto.STRING,
        number=3,
    )
    storage_cost_bytes: int = proto.Field(
        proto.INT64,
        number=4,
    )
    impacted_queries_count: int = proto.Field(
        proto.INT64,
        number=5,
    )


class SCCInfo(proto.Message):
    r"""Info associated with SCC signals.

    Attributes:
        signal (str):
            Name of the signal.
        category (str):
            Name by which SCC calls this signal.
        regulatory_standards (MutableSequence[google.cloud.databasecenter_v1beta.types.RegulatoryStandard]):
            Compliances that are associated with the
            signal.
        external_uri (str):
            External URI which points to a SCC page
            associated with the signal.
    """

    signal: str = proto.Field(
        proto.STRING,
        number=1,
    )
    category: str = proto.Field(
        proto.STRING,
        number=2,
    )
    regulatory_standards: MutableSequence["RegulatoryStandard"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="RegulatoryStandard",
    )
    external_uri: str = proto.Field(
        proto.STRING,
        number=4,
    )


class RecommendationInfo(proto.Message):
    r"""Info associated with recommendation.

    Attributes:
        recommender (str):
            Name of recommendation.
            Examples:

            organizations/1234/locations/us-central1/recommenders/google.cloudsql.instance.PerformanceRecommender/recommendations/9876
        recommender_id (str):
            ID of recommender.
            Examples:
            "google.cloudsql.instance.PerformanceRecommender".
        recommender_subtype (str):
            Contains an identifier for a subtype of recommendations
            produced for the same recommender. Subtype is a function of
            content and impact, meaning a new subtype might be added
            when significant changes to ``content`` or
            ``primary_impact.category`` are introduced. See the
            Recommenders section to see a list of subtypes for a given
            Recommender.

            Examples: For recommender =
            "google.cloudsql.instance.PerformanceRecommender",
            recommender_subtype can be
            "MYSQL_HIGH_NUMBER_OF_OPEN_TABLES_BEST_PRACTICE"/"POSTGRES_HIGH_TRANSACTION_ID_UTILIZATION_BEST_PRACTICE".
    """

    recommender: str = proto.Field(
        proto.STRING,
        number=1,
    )
    recommender_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    recommender_subtype: str = proto.Field(
        proto.STRING,
        number=3,
    )


class RegulatoryStandard(proto.Message):
    r"""Compliances associated with signals.

    Attributes:
        standard (str):
            Name of industry compliance standards, such
            as such as CIS, PCI, and OWASP.
        version (str):
            Version of the standard or benchmark, for
            example, 1.1.
    """

    standard: str = proto.Field(
        proto.STRING,
        number=1,
    )
    version: str = proto.Field(
        proto.STRING,
        number=2,
    )


class OutdatedMinorVersionInfo(proto.Message):
    r"""Info associated with outdated minor version.

    Attributes:
        recommended_minor_version (str):
            Recommended minor version of the underlying
            database engine. Example values: For MySQL, it
            could be "8.0.35", "5.7.25" etc. For PostgreSQL,
            it could be "14.4", "15.5" etc.
    """

    recommended_minor_version: str = proto.Field(
        proto.STRING,
        number=1,
    )


class MaintenanceRecommendationInfo(proto.Message):
    r"""Info associated with maintenance recommendation.

    Attributes:
        resource_maintenance_schedules (MutableSequence[google.cloud.databasecenter_v1beta.types.ResourceMaintenanceSchedule]):
            Optional. List of recommended maintenance
            schedules for the database resource.
    """

    resource_maintenance_schedules: MutableSequence[
        maintenance.ResourceMaintenanceSchedule
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=maintenance.ResourceMaintenanceSchedule,
    )


class Signal(proto.Message):
    r"""Represents a signal.

    Attributes:
        signal_type (google.cloud.databasecenter_v1beta.types.SignalType):
            Type of the signal.
        signal_status (google.cloud.databasecenter_v1beta.types.SignalStatus):
            Status of the signal.
        additional_details (MutableSequence[google.cloud.databasecenter_v1beta.types.AdditionalDetail]):
            Additional information related to the signal.
            In the case of composite signals, this field
            encapsulates details associated with granular
            signals, having a signal status of "ISSUE";
            signals with a status of "OK" are not included.
            For granular signals, it encompasses information
            relevant to the signal, regardless of the signal
            status.
        issue_severity (google.cloud.databasecenter_v1beta.types.IssueSeverity):
            Severity of the issue.
        issue_create_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp when the issue was created (when
            signal status is ISSUE).
    """

    signal_type: "SignalType" = proto.Field(
        proto.ENUM,
        number=1,
        enum="SignalType",
    )
    signal_status: "SignalStatus" = proto.Field(
        proto.ENUM,
        number=2,
        enum="SignalStatus",
    )
    additional_details: MutableSequence["AdditionalDetail"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="AdditionalDetail",
    )
    issue_severity: "IssueSeverity" = proto.Field(
        proto.ENUM,
        number=4,
        enum="IssueSeverity",
    )
    issue_create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
