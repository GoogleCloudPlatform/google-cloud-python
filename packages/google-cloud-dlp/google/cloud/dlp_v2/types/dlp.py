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
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
import google.type.date_pb2 as date_pb2  # type: ignore
import google.type.dayofweek_pb2 as dayofweek_pb2  # type: ignore
import google.type.timeofday_pb2 as timeofday_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.dlp_v2.types import storage

__protobuf__ = proto.module(
    package="google.privacy.dlp.v2",
    manifest={
        "ContentPolicyVerdict",
        "TransformationResultStatusType",
        "TransformationContainerType",
        "TransformationType",
        "ProfileGeneration",
        "BigQueryTableTypeCollection",
        "BigQueryTableType",
        "DataProfileUpdateFrequency",
        "BigQueryTableModification",
        "BigQuerySchemaModification",
        "RelationalOperator",
        "MatchingType",
        "ContentOption",
        "MetadataType",
        "InfoTypeSupportedBy",
        "DlpJobType",
        "StoredInfoTypeState",
        "ResourceVisibility",
        "EncryptionStatus",
        "NullPercentageLevel",
        "UniquenessScoreLevel",
        "ConnectionState",
        "ExcludeInfoTypes",
        "ExcludeByHotword",
        "ExcludeByImageFindings",
        "ExclusionRule",
        "AdjustByMatchingInfoTypes",
        "AdjustByImageFindings",
        "AdjustmentRule",
        "InspectionRule",
        "InspectionRuleSet",
        "InspectConfig",
        "ByteContentItem",
        "ContentItem",
        "ContentMetadata",
        "Conversation",
        "ConversationMessage",
        "BatchContentItem",
        "StringValueBatch",
        "Table",
        "KeyValueMetadataProperty",
        "FileLabel",
        "InspectResult",
        "Finding",
        "Location",
        "ContentLocation",
        "ConversationLocation",
        "BatchContentLocation",
        "MetadataLocation",
        "StorageMetadataLabel",
        "KeyValueMetadataLabel",
        "DocumentLocation",
        "RecordLocation",
        "TableLocation",
        "Container",
        "Range",
        "ImageLocation",
        "BoundingBox",
        "RedactImageRequest",
        "Color",
        "RedactImageResponse",
        "DeidentifyContentRequest",
        "DeidentifyContentResponse",
        "ReidentifyContentRequest",
        "ReidentifyContentResponse",
        "InspectContentRequest",
        "InspectContentResponse",
        "OutputStorageConfig",
        "InfoTypeStats",
        "InspectDataSourceDetails",
        "DataProfileBigQueryRowSchema",
        "HybridInspectStatistics",
        "ActionDetails",
        "DeidentifyDataSourceStats",
        "DeidentifyDataSourceDetails",
        "LocationSupport",
        "InfoTypeDescription",
        "InfoTypeCategory",
        "VersionDescription",
        "ListInfoTypesRequest",
        "ListInfoTypesResponse",
        "RiskAnalysisJobConfig",
        "QuasiId",
        "StatisticalTable",
        "PrivacyMetric",
        "AnalyzeDataSourceRiskDetails",
        "ValueFrequency",
        "Value",
        "QuoteInfo",
        "DateTime",
        "DeidentifyConfig",
        "ImageTransformations",
        "TransformationErrorHandling",
        "PrimitiveTransformation",
        "TimePartConfig",
        "CryptoHashConfig",
        "CryptoDeterministicConfig",
        "ReplaceValueConfig",
        "ReplaceDictionaryConfig",
        "ReplaceWithInfoTypeConfig",
        "RedactConfig",
        "CharsToIgnore",
        "CharacterMaskConfig",
        "FixedSizeBucketingConfig",
        "BucketingConfig",
        "CryptoReplaceFfxFpeConfig",
        "CryptoKey",
        "TransientCryptoKey",
        "UnwrappedCryptoKey",
        "KmsWrappedCryptoKey",
        "DateShiftConfig",
        "InfoTypeTransformations",
        "FieldTransformation",
        "RecordTransformations",
        "RecordSuppression",
        "RecordCondition",
        "TransformationOverview",
        "TransformationSummary",
        "TransformationDescription",
        "TransformationDetails",
        "TransformationLocation",
        "RecordTransformation",
        "TransformationResultStatus",
        "TransformationDetailsStorageConfig",
        "Schedule",
        "Manual",
        "InspectTemplate",
        "DeidentifyTemplate",
        "Error",
        "JobTrigger",
        "Action",
        "TransformationConfig",
        "CreateInspectTemplateRequest",
        "UpdateInspectTemplateRequest",
        "GetInspectTemplateRequest",
        "ListInspectTemplatesRequest",
        "ListInspectTemplatesResponse",
        "DeleteInspectTemplateRequest",
        "CreateJobTriggerRequest",
        "ActivateJobTriggerRequest",
        "UpdateJobTriggerRequest",
        "GetJobTriggerRequest",
        "CreateDiscoveryConfigRequest",
        "UpdateDiscoveryConfigRequest",
        "GetDiscoveryConfigRequest",
        "ListDiscoveryConfigsRequest",
        "ListDiscoveryConfigsResponse",
        "DeleteDiscoveryConfigRequest",
        "CreateDlpJobRequest",
        "ListJobTriggersRequest",
        "ListJobTriggersResponse",
        "DeleteJobTriggerRequest",
        "InspectJobConfig",
        "DataProfileAction",
        "DataProfileFinding",
        "DataProfileFindingLocation",
        "DataProfileFindingRecordLocation",
        "DataProfileJobConfig",
        "BigQueryRegex",
        "BigQueryRegexes",
        "BigQueryTableTypes",
        "Disabled",
        "DataProfileLocation",
        "DiscoveryConfig",
        "DiscoveryTarget",
        "BigQueryDiscoveryTarget",
        "DiscoveryBigQueryFilter",
        "BigQueryTableCollection",
        "DiscoveryBigQueryConditions",
        "DiscoveryGenerationCadence",
        "DiscoveryTableModifiedCadence",
        "DiscoverySchemaModifiedCadence",
        "DiscoveryInspectTemplateModifiedCadence",
        "CloudSqlDiscoveryTarget",
        "DiscoveryCloudSqlFilter",
        "DatabaseResourceCollection",
        "DatabaseResourceRegexes",
        "DatabaseResourceRegex",
        "AllOtherDatabaseResources",
        "DatabaseResourceReference",
        "DiscoveryCloudSqlConditions",
        "DiscoveryCloudSqlGenerationCadence",
        "SecretsDiscoveryTarget",
        "CloudStorageDiscoveryTarget",
        "DiscoveryCloudStorageFilter",
        "FileStoreCollection",
        "FileStoreRegexes",
        "FileStoreRegex",
        "CloudStorageRegex",
        "CloudStorageResourceReference",
        "DiscoveryCloudStorageGenerationCadence",
        "DiscoveryCloudStorageConditions",
        "DiscoveryFileStoreConditions",
        "OtherCloudDiscoveryTarget",
        "DiscoveryOtherCloudFilter",
        "OtherCloudResourceCollection",
        "OtherCloudResourceRegexes",
        "OtherCloudResourceRegex",
        "AwsAccountRegex",
        "AmazonS3BucketRegex",
        "OtherCloudSingleResourceReference",
        "AwsAccount",
        "AmazonS3Bucket",
        "DiscoveryOtherCloudConditions",
        "AmazonS3BucketConditions",
        "DiscoveryOtherCloudGenerationCadence",
        "DiscoveryStartingLocation",
        "OtherCloudDiscoveryStartingLocation",
        "AllOtherResources",
        "VertexDatasetDiscoveryTarget",
        "DiscoveryVertexDatasetFilter",
        "VertexDatasetCollection",
        "VertexDatasetRegexes",
        "VertexDatasetRegex",
        "VertexDatasetResourceReference",
        "DiscoveryVertexDatasetConditions",
        "DiscoveryVertexDatasetGenerationCadence",
        "DlpJob",
        "GetDlpJobRequest",
        "ListDlpJobsRequest",
        "ListDlpJobsResponse",
        "CancelDlpJobRequest",
        "FinishDlpJobRequest",
        "DeleteDlpJobRequest",
        "CreateDeidentifyTemplateRequest",
        "UpdateDeidentifyTemplateRequest",
        "GetDeidentifyTemplateRequest",
        "ListDeidentifyTemplatesRequest",
        "ListDeidentifyTemplatesResponse",
        "DeleteDeidentifyTemplateRequest",
        "LargeCustomDictionaryConfig",
        "LargeCustomDictionaryStats",
        "StoredInfoTypeConfig",
        "StoredInfoTypeStats",
        "StoredInfoTypeVersion",
        "StoredInfoType",
        "CreateStoredInfoTypeRequest",
        "UpdateStoredInfoTypeRequest",
        "GetStoredInfoTypeRequest",
        "ListStoredInfoTypesRequest",
        "ListStoredInfoTypesResponse",
        "DeleteStoredInfoTypeRequest",
        "HybridInspectJobTriggerRequest",
        "HybridInspectDlpJobRequest",
        "HybridContentItem",
        "HybridFindingDetails",
        "HybridInspectResponse",
        "ImageContainmentType",
        "Overlap",
        "Encloses",
        "FullyInside",
        "ListProjectDataProfilesRequest",
        "ListProjectDataProfilesResponse",
        "ListTableDataProfilesRequest",
        "ListTableDataProfilesResponse",
        "ListColumnDataProfilesRequest",
        "ListColumnDataProfilesResponse",
        "DataRiskLevel",
        "ProjectDataProfile",
        "DataProfileConfigSnapshot",
        "TableDataProfile",
        "ProfileStatus",
        "InfoTypeSummary",
        "OtherInfoTypeSummary",
        "ColumnDataProfile",
        "FileStoreDataProfile",
        "Tag",
        "TagFilters",
        "TagFilter",
        "RelatedResource",
        "FileStoreInfoTypeSummary",
        "FileExtensionInfo",
        "FileClusterSummary",
        "GetProjectDataProfileRequest",
        "GetFileStoreDataProfileRequest",
        "ListFileStoreDataProfilesRequest",
        "ListFileStoreDataProfilesResponse",
        "DeleteFileStoreDataProfileRequest",
        "GetTableDataProfileRequest",
        "GetColumnDataProfileRequest",
        "DataProfilePubSubCondition",
        "DataProfilePubSubMessage",
        "CreateConnectionRequest",
        "GetConnectionRequest",
        "ListConnectionsRequest",
        "SearchConnectionsRequest",
        "ListConnectionsResponse",
        "SearchConnectionsResponse",
        "UpdateConnectionRequest",
        "DeleteConnectionRequest",
        "Connection",
        "SecretManagerCredential",
        "CloudSqlIamCredential",
        "CloudSqlProperties",
        "DeleteTableDataProfileRequest",
        "DataSourceType",
        "FileClusterType",
        "ProcessingLocation",
        "SaveToGcsFindingsOutput",
        "Domain",
        "CreateContentPolicyRequest",
        "GetContentPolicyRequest",
        "ListContentPoliciesRequest",
        "ListContentPoliciesResponse",
        "UpdateContentPolicyRequest",
        "DeleteContentPolicyRequest",
        "ContentPolicy",
    },
)


class ContentPolicyVerdict(proto.Enum):
    r"""Possible results of applying a content policy. This may
    expand to include additional result types in the future.

    Values:
        CONTENT_POLICY_VERDICT_UNSPECIFIED (0):
            Not used.
        ALLOW (1):
            The policy allows the provided content to be
            used.
        BLOCK (2):
            The policy prevents the provided content from
            being used. This should result in a blocked file
            upload, exclusion from training dataset, or
            other similar block action. (specific action
            will depend on the caller).
    """

    CONTENT_POLICY_VERDICT_UNSPECIFIED = 0
    ALLOW = 1
    BLOCK = 2


class TransformationResultStatusType(proto.Enum):
    r"""Enum of possible outcomes of transformations. SUCCESS if
    transformation and storing of transformation was successful,
    otherwise, reason for not transforming.

    Values:
        STATE_TYPE_UNSPECIFIED (0):
            Unused.
        INVALID_TRANSFORM (1):
            This is set when a finding cannot be
            transformed (i.e. outside user set bucket
            range).
        BIGQUERY_MAX_ROW_SIZE_EXCEEDED (2):
            This is set when a transformation is
            successful but cannot be stored in BigQuery
            because the transformed row exceeds BigQuery's
            max row size.
        METADATA_UNRETRIEVABLE (3):
            This is set when there is a finding in the
            custom metadata of a file, but at the write time
            of the transformed file, this key / value pair
            is unretrievable.
        SUCCESS (4):
            This is set when the transformation and its
            storage are successful.
    """

    STATE_TYPE_UNSPECIFIED = 0
    INVALID_TRANSFORM = 1
    BIGQUERY_MAX_ROW_SIZE_EXCEEDED = 2
    METADATA_UNRETRIEVABLE = 3
    SUCCESS = 4


class TransformationContainerType(proto.Enum):
    r"""Describes functionality of a given container in its original
    format.

    Values:
        TRANSFORM_UNKNOWN_CONTAINER (0):
            Unused.
        TRANSFORM_BODY (1):
            Body of a file.
        TRANSFORM_METADATA (2):
            Metadata for a file.
        TRANSFORM_TABLE (3):
            A table.
    """

    TRANSFORM_UNKNOWN_CONTAINER = 0
    TRANSFORM_BODY = 1
    TRANSFORM_METADATA = 2
    TRANSFORM_TABLE = 3


class TransformationType(proto.Enum):
    r"""An enum of rules that can be used to transform a value. Can be a
    record suppression, or one of the transformation rules specified
    under ``PrimitiveTransformation``.

    Values:
        TRANSFORMATION_TYPE_UNSPECIFIED (0):
            Unused
        RECORD_SUPPRESSION (1):
            Record suppression
        REPLACE_VALUE (2):
            Replace value
        REPLACE_DICTIONARY (15):
            Replace value using a dictionary.
        REDACT (3):
            Redact
        CHARACTER_MASK (4):
            Character mask
        CRYPTO_REPLACE_FFX_FPE (5):
            FFX-FPE
        FIXED_SIZE_BUCKETING (6):
            Fixed size bucketing
        BUCKETING (7):
            Bucketing
        REPLACE_WITH_INFO_TYPE (8):
            Replace with info type
        TIME_PART (9):
            Time part
        CRYPTO_HASH (10):
            Crypto hash
        DATE_SHIFT (12):
            Date shift
        CRYPTO_DETERMINISTIC_CONFIG (13):
            Deterministic crypto
        REDACT_IMAGE (14):
            Redact image
    """

    TRANSFORMATION_TYPE_UNSPECIFIED = 0
    RECORD_SUPPRESSION = 1
    REPLACE_VALUE = 2
    REPLACE_DICTIONARY = 15
    REDACT = 3
    CHARACTER_MASK = 4
    CRYPTO_REPLACE_FFX_FPE = 5
    FIXED_SIZE_BUCKETING = 6
    BUCKETING = 7
    REPLACE_WITH_INFO_TYPE = 8
    TIME_PART = 9
    CRYPTO_HASH = 10
    DATE_SHIFT = 12
    CRYPTO_DETERMINISTIC_CONFIG = 13
    REDACT_IMAGE = 14


class ProfileGeneration(proto.Enum):
    r"""Whether a profile being created is the first generation or an
    update.

    Values:
        PROFILE_GENERATION_UNSPECIFIED (0):
            Unused.
        PROFILE_GENERATION_NEW (1):
            The profile is the first profile for the
            resource.
        PROFILE_GENERATION_UPDATE (2):
            The profile is an update to a previous
            profile.
    """

    PROFILE_GENERATION_UNSPECIFIED = 0
    PROFILE_GENERATION_NEW = 1
    PROFILE_GENERATION_UPDATE = 2


class BigQueryTableTypeCollection(proto.Enum):
    r"""Over time new types may be added. Currently VIEW, MATERIALIZED_VIEW,
    and non-BigLake external tables are not supported.

    Values:
        BIG_QUERY_COLLECTION_UNSPECIFIED (0):
            Unused.
        BIG_QUERY_COLLECTION_ALL_TYPES (1):
            Automatically generate profiles for all
            tables, even if the table type is not yet fully
            supported for analysis. Profiles for unsupported
            tables will be generated with errors to indicate
            their partial support. When full support is
            added, the tables will automatically be profiled
            during the next scheduled run.
        BIG_QUERY_COLLECTION_ONLY_SUPPORTED_TYPES (2):
            Only those types fully supported will be
            profiled. Will expand automatically as Cloud DLP
            adds support for new table types. Unsupported
            table types will not have partial profiles
            generated.
    """

    BIG_QUERY_COLLECTION_UNSPECIFIED = 0
    BIG_QUERY_COLLECTION_ALL_TYPES = 1
    BIG_QUERY_COLLECTION_ONLY_SUPPORTED_TYPES = 2


class BigQueryTableType(proto.Enum):
    r"""Over time new types may be added. Currently VIEW, MATERIALIZED_VIEW,
    and non-BigLake external tables are not supported.

    Values:
        BIG_QUERY_TABLE_TYPE_UNSPECIFIED (0):
            Unused.
        BIG_QUERY_TABLE_TYPE_TABLE (1):
            A normal BigQuery table.
        BIG_QUERY_TABLE_TYPE_EXTERNAL_BIG_LAKE (2):
            A table that references data stored in Cloud
            Storage.
        BIG_QUERY_TABLE_TYPE_SNAPSHOT (3):
            A snapshot of a BigQuery table.
    """

    BIG_QUERY_TABLE_TYPE_UNSPECIFIED = 0
    BIG_QUERY_TABLE_TYPE_TABLE = 1
    BIG_QUERY_TABLE_TYPE_EXTERNAL_BIG_LAKE = 2
    BIG_QUERY_TABLE_TYPE_SNAPSHOT = 3


class DataProfileUpdateFrequency(proto.Enum):
    r"""How frequently data profiles can be updated. New options can
    be added at a later time.

    Values:
        UPDATE_FREQUENCY_UNSPECIFIED (0):
            Unspecified.
        UPDATE_FREQUENCY_NEVER (1):
            After the data profile is created, it will
            never be updated.
        UPDATE_FREQUENCY_DAILY (2):
            The data profile can be updated up to once
            every 24 hours.
        UPDATE_FREQUENCY_MONTHLY (4):
            The data profile can be updated up to once
            every 30 days. Default.
    """

    UPDATE_FREQUENCY_UNSPECIFIED = 0
    UPDATE_FREQUENCY_NEVER = 1
    UPDATE_FREQUENCY_DAILY = 2
    UPDATE_FREQUENCY_MONTHLY = 4


class BigQueryTableModification(proto.Enum):
    r"""Attributes evaluated to determine if a table has been
    modified. New values may be added at a later time.

    Values:
        TABLE_MODIFICATION_UNSPECIFIED (0):
            Unused.
        TABLE_MODIFIED_TIMESTAMP (1):
            A table will be considered modified when the
            last_modified_time from BigQuery has been updated.
    """

    TABLE_MODIFICATION_UNSPECIFIED = 0
    TABLE_MODIFIED_TIMESTAMP = 1


class BigQuerySchemaModification(proto.Enum):
    r"""Attributes evaluated to determine if a schema has been
    modified. New values may be added at a later time.

    Values:
        SCHEMA_MODIFICATION_UNSPECIFIED (0):
            Unused
        SCHEMA_NEW_COLUMNS (1):
            Profiles should be regenerated when new
            columns are added to the table. Default.
        SCHEMA_REMOVED_COLUMNS (2):
            Profiles should be regenerated when columns
            are removed from the table.
    """

    SCHEMA_MODIFICATION_UNSPECIFIED = 0
    SCHEMA_NEW_COLUMNS = 1
    SCHEMA_REMOVED_COLUMNS = 2


class RelationalOperator(proto.Enum):
    r"""Operators available for comparing the value of fields.

    Values:
        RELATIONAL_OPERATOR_UNSPECIFIED (0):
            Unused
        EQUAL_TO (1):
            Equal. Attempts to match even with
            incompatible types.
        NOT_EQUAL_TO (2):
            Not equal to. Attempts to match even with
            incompatible types.
        GREATER_THAN (3):
            Greater than.
        LESS_THAN (4):
            Less than.
        GREATER_THAN_OR_EQUALS (5):
            Greater than or equals.
        LESS_THAN_OR_EQUALS (6):
            Less than or equals.
        EXISTS (7):
            Exists
    """

    RELATIONAL_OPERATOR_UNSPECIFIED = 0
    EQUAL_TO = 1
    NOT_EQUAL_TO = 2
    GREATER_THAN = 3
    LESS_THAN = 4
    GREATER_THAN_OR_EQUALS = 5
    LESS_THAN_OR_EQUALS = 6
    EXISTS = 7


class MatchingType(proto.Enum):
    r"""Type of the match which can be applied to different ways of
    matching, like Dictionary, regular expression and intersecting
    with findings of another infoType.

    Values:
        MATCHING_TYPE_UNSPECIFIED (0):
            Invalid.
        MATCHING_TYPE_FULL_MATCH (1):
            Full match.

            - Dictionary: join of Dictionary results matched
              the complete finding quote
            - Regex: all regex matches fill a finding quote
              from start to end
            - Exclude infoType: completely inside affecting
              infoTypes findings
        MATCHING_TYPE_PARTIAL_MATCH (2):
            Partial match.

            - Dictionary: at least one of the tokens in the
              finding matches
            - Regex: substring of the finding matches
            - Exclude infoType: intersects with affecting
              infoTypes findings
        MATCHING_TYPE_INVERSE_MATCH (3):
            Inverse match.

            - Dictionary: no tokens in the finding match the
              dictionary
            - Regex: finding doesn't match the regex
            - Exclude infoType: no intersection with
              affecting infoTypes findings
        MATCHING_TYPE_RULE_SPECIFIC (4):
            Rule-specific match.

            The matching logic is based on the specific rule being used.
            This is required for rules where the matching behavior is
            not a simple string comparison (e.g., image containment).
            This matching type can only be used with the
            ``ExcludeByImageFindings`` rule.

            - Exclude by image findings: The matching logic is defined
              within ``ExcludeByImageFindings`` based on spatial
              relationships between bounding boxes.
    """

    MATCHING_TYPE_UNSPECIFIED = 0
    MATCHING_TYPE_FULL_MATCH = 1
    MATCHING_TYPE_PARTIAL_MATCH = 2
    MATCHING_TYPE_INVERSE_MATCH = 3
    MATCHING_TYPE_RULE_SPECIFIC = 4


class ContentOption(proto.Enum):
    r"""Deprecated and unused.

    Values:
        CONTENT_UNSPECIFIED (0):
            Includes entire content of a file or a data
            stream.
        CONTENT_TEXT (1):
            Text content within the data, excluding any
            metadata.
        CONTENT_IMAGE (2):
            Images found in the data.
    """

    CONTENT_UNSPECIFIED = 0
    CONTENT_TEXT = 1
    CONTENT_IMAGE = 2


class MetadataType(proto.Enum):
    r"""Type of metadata containing the finding.

    Values:
        METADATATYPE_UNSPECIFIED (0):
            Unused
        STORAGE_METADATA (2):
            General file metadata provided by Cloud
            Storage.
        CONTENT_METADATA (3):
            Metadata extracted from the files.
        CLIENT_PROVIDED_METADATA (4):
            Metadata provided by the client.
    """

    METADATATYPE_UNSPECIFIED = 0
    STORAGE_METADATA = 2
    CONTENT_METADATA = 3
    CLIENT_PROVIDED_METADATA = 4


class InfoTypeSupportedBy(proto.Enum):
    r"""Parts of the APIs which use certain infoTypes.

    Values:
        ENUM_TYPE_UNSPECIFIED (0):
            Unused.
        INSPECT (1):
            Supported by the inspect operations.
        RISK_ANALYSIS (2):
            Supported by the risk analysis operations.
    """

    ENUM_TYPE_UNSPECIFIED = 0
    INSPECT = 1
    RISK_ANALYSIS = 2


class DlpJobType(proto.Enum):
    r"""An enum to represent the various types of DLP jobs.

    Values:
        DLP_JOB_TYPE_UNSPECIFIED (0):
            Defaults to INSPECT_JOB.
        INSPECT_JOB (1):
            The job inspected Google Cloud for sensitive
            data.
        RISK_ANALYSIS_JOB (2):
            The job executed a Risk Analysis computation.
    """

    DLP_JOB_TYPE_UNSPECIFIED = 0
    INSPECT_JOB = 1
    RISK_ANALYSIS_JOB = 2


class StoredInfoTypeState(proto.Enum):
    r"""State of a StoredInfoType version.

    Values:
        STORED_INFO_TYPE_STATE_UNSPECIFIED (0):
            Unused
        PENDING (1):
            StoredInfoType version is being created.
        READY (2):
            StoredInfoType version is ready for use.
        FAILED (3):
            StoredInfoType creation failed. All relevant error messages
            are returned in the ``StoredInfoTypeVersion`` message.
        INVALID (4):
            StoredInfoType is no longer valid because artifacts stored
            in user-controlled storage were modified. To fix an invalid
            StoredInfoType, use the ``UpdateStoredInfoType`` method to
            create a new version.
    """

    STORED_INFO_TYPE_STATE_UNSPECIFIED = 0
    PENDING = 1
    READY = 2
    FAILED = 3
    INVALID = 4


class ResourceVisibility(proto.Enum):
    r"""How broadly the data in the resource has been shared. New
    items may be added over time. A higher number means more
    restricted.

    Values:
        RESOURCE_VISIBILITY_UNSPECIFIED (0):
            Unused.
        RESOURCE_VISIBILITY_PUBLIC (10):
            Visible to any user.
        RESOURCE_VISIBILITY_INCONCLUSIVE (15):
            May contain public items.
            For example, if a Cloud Storage bucket has
            uniform bucket level access disabled, some
            objects inside it may be public, but none are
            known yet.
        RESOURCE_VISIBILITY_RESTRICTED (20):
            Visible only to specific users.
    """

    RESOURCE_VISIBILITY_UNSPECIFIED = 0
    RESOURCE_VISIBILITY_PUBLIC = 10
    RESOURCE_VISIBILITY_INCONCLUSIVE = 15
    RESOURCE_VISIBILITY_RESTRICTED = 20


class EncryptionStatus(proto.Enum):
    r"""How a resource is encrypted.

    Values:
        ENCRYPTION_STATUS_UNSPECIFIED (0):
            Unused.
        ENCRYPTION_GOOGLE_MANAGED (1):
            Google manages server-side encryption keys on
            your behalf.
        ENCRYPTION_CUSTOMER_MANAGED (2):
            Customer provides the key.
    """

    ENCRYPTION_STATUS_UNSPECIFIED = 0
    ENCRYPTION_GOOGLE_MANAGED = 1
    ENCRYPTION_CUSTOMER_MANAGED = 2


class NullPercentageLevel(proto.Enum):
    r"""Bucketized nullness percentage levels. A higher level means a
    higher percentage of the column is null.

    Values:
        NULL_PERCENTAGE_LEVEL_UNSPECIFIED (0):
            Unused.
        NULL_PERCENTAGE_VERY_LOW (1):
            Very few null entries.
        NULL_PERCENTAGE_LOW (2):
            Some null entries.
        NULL_PERCENTAGE_MEDIUM (3):
            A few null entries.
        NULL_PERCENTAGE_HIGH (4):
            A lot of null entries.
    """

    NULL_PERCENTAGE_LEVEL_UNSPECIFIED = 0
    NULL_PERCENTAGE_VERY_LOW = 1
    NULL_PERCENTAGE_LOW = 2
    NULL_PERCENTAGE_MEDIUM = 3
    NULL_PERCENTAGE_HIGH = 4


class UniquenessScoreLevel(proto.Enum):
    r"""Bucketized uniqueness score levels. A higher uniqueness score
    is a strong signal that the column may contain a unique
    identifier like user id. A low value indicates that the column
    contains few unique values like booleans or other classifiers.

    Values:
        UNIQUENESS_SCORE_LEVEL_UNSPECIFIED (0):
            Some columns do not have estimated
            uniqueness. Possible reasons include having too
            few values.
        UNIQUENESS_SCORE_LOW (1):
            Low uniqueness, possibly a boolean, enum or
            similiarly typed column.
        UNIQUENESS_SCORE_MEDIUM (2):
            Medium uniqueness.
        UNIQUENESS_SCORE_HIGH (3):
            High uniqueness, possibly a column of free
            text or unique identifiers.
    """

    UNIQUENESS_SCORE_LEVEL_UNSPECIFIED = 0
    UNIQUENESS_SCORE_LOW = 1
    UNIQUENESS_SCORE_MEDIUM = 2
    UNIQUENESS_SCORE_HIGH = 3


class ConnectionState(proto.Enum):
    r"""State of the connection.
    New values may be added over time.

    Values:
        CONNECTION_STATE_UNSPECIFIED (0):
            Unused
        MISSING_CREDENTIALS (1):
            The DLP API automatically created this
            connection during an initial scan, and it is
            awaiting full configuration by a user.
        AVAILABLE (2):
            A configured connection that has not
            encountered any errors.
        ERROR (3):
            A configured connection that encountered
            errors during its last use. It will not be used
            again until it is set to AVAILABLE.

            If the resolution requires external action, then
            the client must send a request to set the status
            to AVAILABLE when the connection is ready for
            use. If the resolution doesn't require external
            action, then any changes to the connection
            properties will automatically mark it as
            AVAILABLE.
    """

    CONNECTION_STATE_UNSPECIFIED = 0
    MISSING_CREDENTIALS = 1
    AVAILABLE = 2
    ERROR = 3


class ExcludeInfoTypes(proto.Message):
    r"""List of excluded infoTypes.

    Attributes:
        info_types (MutableSequence[google.cloud.dlp_v2.types.InfoType]):
            InfoType list in ExclusionRule rule drops a finding when it
            overlaps or contained within with a finding of an infoType
            from this list. For example, for
            ``InspectionRuleSet.info_types`` containing
            "PHONE_NUMBER"``and``\ exclusion_rule\ ``containing``\ exclude_info_types.info_types\`
            with "EMAIL_ADDRESS" the phone number findings are dropped
            if they overlap with EMAIL_ADDRESS finding. That leads to
            "555-222-2222@example.org" to generate only a single
            finding, namely email address.
    """

    info_types: MutableSequence[storage.InfoType] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=storage.InfoType,
    )


class ExcludeByHotword(proto.Message):
    r"""The rule to exclude findings based on a hotword. For record
    inspection of tables, column names are considered hotwords. An
    example of this is to exclude a finding if it belongs to a
    BigQuery column that matches a specific pattern.

    Attributes:
        hotword_regex (google.cloud.dlp_v2.types.CustomInfoType.Regex):
            Regular expression pattern defining what
            qualifies as a hotword.
        proximity (google.cloud.dlp_v2.types.CustomInfoType.DetectionRule.Proximity):
            Range of characters within which the entire
            hotword must reside. The total length of the
            window cannot exceed 1000 characters. The
            windowBefore property in proximity should be set
            to 1 if the hotword needs to be included in a
            column header.
    """

    hotword_regex: storage.CustomInfoType.Regex = proto.Field(
        proto.MESSAGE,
        number=1,
        message=storage.CustomInfoType.Regex,
    )
    proximity: storage.CustomInfoType.DetectionRule.Proximity = proto.Field(
        proto.MESSAGE,
        number=2,
        message=storage.CustomInfoType.DetectionRule.Proximity,
    )


class ExcludeByImageFindings(proto.Message):
    r"""The rule to exclude image findings based on spatial
    relationships with other image findings. For example, exclude an
    image finding if it overlaps with another image finding.
    This rule is silently ignored if the content being inspected is
    not an image.

    Attributes:
        info_types (MutableSequence[google.cloud.dlp_v2.types.InfoType]):
            A list of image-supported infoTypes—excluding `document
            infoTypes <https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference#documents>`__—to
            be used as context for the exclusion rule. A finding is
            excluded if its bounding box has the specified spatial
            relationship (defined by ``image_containment_type``) with a
            finding of an infoType in this list.

            For example, if ``InspectionRuleSet.info_types`` includes
            ``OBJECT_TYPE/PERSON`` and this ``exclusion_rule`` specifies
            ``info_types`` as ``OBJECT_TYPE/PERSON/PASSPORT`` with
            ``image_containment_type`` set to ``encloses``, then
            ``OBJECT_TYPE/PERSON`` findings will be excluded if they are
            fully contained within the bounding box of an
            ``OBJECT_TYPE/PERSON/PASSPORT`` finding.
        image_containment_type (google.cloud.dlp_v2.types.ImageContainmentType):
            Specifies the required spatial relationship
            between the bounding boxes of the target finding
            and the context infoType findings.
    """

    info_types: MutableSequence[storage.InfoType] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=storage.InfoType,
    )
    image_containment_type: "ImageContainmentType" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ImageContainmentType",
    )


class ExclusionRule(proto.Message):
    r"""The rule that specifies conditions when findings of infoTypes
    specified in ``InspectionRuleSet`` are removed from results.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        dictionary (google.cloud.dlp_v2.types.CustomInfoType.Dictionary):
            Dictionary which defines the rule.

            This field is a member of `oneof`_ ``type``.
        regex (google.cloud.dlp_v2.types.CustomInfoType.Regex):
            Regular expression which defines the rule.

            This field is a member of `oneof`_ ``type``.
        exclude_info_types (google.cloud.dlp_v2.types.ExcludeInfoTypes):
            Set of infoTypes for which findings would
            affect this rule.

            This field is a member of `oneof`_ ``type``.
        exclude_by_hotword (google.cloud.dlp_v2.types.ExcludeByHotword):
            Drop if the hotword rule is contained in the
            proximate context. For tabular data, the context
            includes the column name.

            This field is a member of `oneof`_ ``type``.
        exclude_by_image_findings (google.cloud.dlp_v2.types.ExcludeByImageFindings):
            Exclude findings based on image containment
            rules. For example, exclude an image finding if
            it overlaps with another image finding.

            This field is a member of `oneof`_ ``type``.
        matching_type (google.cloud.dlp_v2.types.MatchingType):
            How the rule is applied, see MatchingType
            documentation for details.
    """

    dictionary: storage.CustomInfoType.Dictionary = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="type",
        message=storage.CustomInfoType.Dictionary,
    )
    regex: storage.CustomInfoType.Regex = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="type",
        message=storage.CustomInfoType.Regex,
    )
    exclude_info_types: "ExcludeInfoTypes" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="type",
        message="ExcludeInfoTypes",
    )
    exclude_by_hotword: "ExcludeByHotword" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="type",
        message="ExcludeByHotword",
    )
    exclude_by_image_findings: "ExcludeByImageFindings" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="type",
        message="ExcludeByImageFindings",
    )
    matching_type: "MatchingType" = proto.Field(
        proto.ENUM,
        number=4,
        enum="MatchingType",
    )


class AdjustByMatchingInfoTypes(proto.Message):
    r"""AdjustmentRule condition for matching infoTypes.

    Attributes:
        info_types (MutableSequence[google.cloud.dlp_v2.types.InfoType]):
            Sensitive Data Protection adjusts the likelihood of a
            finding if that finding also matches one of these infoTypes.

            For example, you can create a rule to adjust the likelihood
            of a ``PHONE_NUMBER`` finding if the string is found within
            a document that is classified as
            ``DOCUMENT_TYPE/HR/RESUME``. To configure this, set
            ``PHONE_NUMBER`` in ``InspectionRuleSet.info_types``. Add an
            ``adjustment_rule`` with an
            ``adjust_by_matching_info_types.info_types`` that contains
            ``DOCUMENT_TYPE/HR/RESUME``. In this case, the likelihood of
            the ``PHONE_NUMBER`` finding is adjusted, but the likelihood
            of the ``DOCUMENT_TYPE/HR/RESUME`` finding is not.
        min_likelihood (google.cloud.dlp_v2.types.Likelihood):
            Required. Minimum likelihood of the
            ``adjust_by_matching_info_types.info_types`` finding. If the
            likelihood is lower than this value, Sensitive Data
            Protection doesn't adjust the likelihood of the
            ``InspectionRuleSet.info_types`` finding.
        matching_type (google.cloud.dlp_v2.types.MatchingType):
            How the adjustment rule is applied.

            Only ``MATCHING_TYPE_PARTIAL_MATCH`` is supported:

            - Partial match: adjusts the findings of infoTypes specified
              in the inspection rule when they have a nonempty
              intersection with a finding of an infoType specified in
              this adjustment rule.
    """

    info_types: MutableSequence[storage.InfoType] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=storage.InfoType,
    )
    min_likelihood: storage.Likelihood = proto.Field(
        proto.ENUM,
        number=2,
        enum=storage.Likelihood,
    )
    matching_type: "MatchingType" = proto.Field(
        proto.ENUM,
        number=3,
        enum="MatchingType",
    )


class AdjustByImageFindings(proto.Message):
    r"""AdjustmentRule condition for image findings.
    This rule is silently ignored if the content being inspected is
    not an image.

    Attributes:
        info_types (MutableSequence[google.cloud.dlp_v2.types.InfoType]):
            A list of image-supported infoTypes—excluding `document
            infoTypes <https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference#documents>`__—to
            be used as context for the adjustment rule. Sensitive Data
            Protection adjusts the likelihood of an image finding if its
            bounding box has the specified spatial relationship (defined
            by ``image_containment_type``) with a finding of an infoType
            in this list.

            For example, you can create a rule to adjust the likelihood
            of a ``US_PASSPORT`` finding if it is enclosed by a finding
            of ``OBJECT_TYPE/PERSON/PASSPORT``. To configure this, set
            ``US_PASSPORT`` in ``InspectionRuleSet.info_types``. Add an
            ``adjustment_rule`` with an
            ``adjust_by_image_findings.info_types`` that contains
            ``OBJECT_TYPE/PERSON/PASSPORT`` and
            ``image_containment_type`` set to ``encloses``. In this
            case, the likelihood of the ``US_PASSPORT`` finding is
            adjusted, but the likelihood of the
            ``OBJECT_TYPE/PERSON/PASSPORT`` finding is not.
        min_likelihood (google.cloud.dlp_v2.types.Likelihood):
            Required. Minimum likelihood of the
            ``adjust_by_image_findings.info_types`` finding. If the
            likelihood is lower than this value, Sensitive Data
            Protection doesn't adjust the likelihood of the
            ``InspectionRuleSet.info_types`` finding.
        image_containment_type (google.cloud.dlp_v2.types.ImageContainmentType):
            Specifies the required spatial relationship
            between the bounding boxes of the target finding
            and the context infoType findings.
    """

    info_types: MutableSequence[storage.InfoType] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=storage.InfoType,
    )
    min_likelihood: storage.Likelihood = proto.Field(
        proto.ENUM,
        number=2,
        enum=storage.Likelihood,
    )
    image_containment_type: "ImageContainmentType" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ImageContainmentType",
    )


class AdjustmentRule(proto.Message):
    r"""Rule that specifies conditions when a certain infoType's
    finding details should be adjusted.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        adjust_by_matching_info_types (google.cloud.dlp_v2.types.AdjustByMatchingInfoTypes):
            Set of infoTypes for which findings would
            affect this rule.

            This field is a member of `oneof`_ ``conditions``.
        adjust_by_image_findings (google.cloud.dlp_v2.types.AdjustByImageFindings):
            AdjustmentRule condition for image findings.

            This field is a member of `oneof`_ ``conditions``.
        likelihood_adjustment (google.cloud.dlp_v2.types.CustomInfoType.DetectionRule.LikelihoodAdjustment):
            Likelihood adjustment to apply to the
            infoType.
    """

    adjust_by_matching_info_types: "AdjustByMatchingInfoTypes" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="conditions",
        message="AdjustByMatchingInfoTypes",
    )
    adjust_by_image_findings: "AdjustByImageFindings" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="conditions",
        message="AdjustByImageFindings",
    )
    likelihood_adjustment: storage.CustomInfoType.DetectionRule.LikelihoodAdjustment = (
        proto.Field(
            proto.MESSAGE,
            number=2,
            message=storage.CustomInfoType.DetectionRule.LikelihoodAdjustment,
        )
    )


class InspectionRule(proto.Message):
    r"""A single inspection rule to be applied to infoTypes, specified in
    ``InspectionRuleSet``.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        hotword_rule (google.cloud.dlp_v2.types.CustomInfoType.DetectionRule.HotwordRule):
            Hotword-based detection rule.

            This field is a member of `oneof`_ ``type``.
        exclusion_rule (google.cloud.dlp_v2.types.ExclusionRule):
            Exclusion rule.

            This field is a member of `oneof`_ ``type``.
        adjustment_rule (google.cloud.dlp_v2.types.AdjustmentRule):
            Adjustment rule.

            This field is a member of `oneof`_ ``type``.
    """

    hotword_rule: storage.CustomInfoType.DetectionRule.HotwordRule = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="type",
        message=storage.CustomInfoType.DetectionRule.HotwordRule,
    )
    exclusion_rule: "ExclusionRule" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="type",
        message="ExclusionRule",
    )
    adjustment_rule: "AdjustmentRule" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="type",
        message="AdjustmentRule",
    )


class InspectionRuleSet(proto.Message):
    r"""Rule set for modifying a set of infoTypes to alter behavior
    under certain circumstances, depending on the specific details
    of the rules within the set.

    Attributes:
        info_types (MutableSequence[google.cloud.dlp_v2.types.InfoType]):
            List of infoTypes this rule set is applied
            to.
        rules (MutableSequence[google.cloud.dlp_v2.types.InspectionRule]):
            Set of rules to be applied to infoTypes. The
            rules are applied in order.
    """

    info_types: MutableSequence[storage.InfoType] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=storage.InfoType,
    )
    rules: MutableSequence["InspectionRule"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="InspectionRule",
    )


class InspectConfig(proto.Message):
    r"""Configuration description of the scanning process. When used with
    redactContent only info_types and min_likelihood are currently used.

    Attributes:
        info_types (MutableSequence[google.cloud.dlp_v2.types.InfoType]):
            Restricts what info_types to look for. The values must
            correspond to InfoType values returned by ListInfoTypes or
            listed at
            https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference.

            When no InfoTypes or CustomInfoTypes are specified in a
            request, the system may automatically choose a default list
            of detectors to run, which may change over time.

            If you need precise control and predictability as to what
            detectors are run you should specify specific InfoTypes
            listed in the reference, otherwise a default list will be
            used, which may change over time.
        min_likelihood (google.cloud.dlp_v2.types.Likelihood):
            Only returns findings equal to or above this threshold. The
            default is POSSIBLE.

            In general, the highest likelihood setting yields the fewest
            findings in results and the lowest chance of a false
            positive. For more information, see `Match
            likelihood <https://docs.cloud.google.com/sensitive-data-protection/docs/likelihood>`__.
        min_likelihood_per_info_type (MutableSequence[google.cloud.dlp_v2.types.InspectConfig.InfoTypeLikelihood]):
            Minimum likelihood per infotype. For each infotype, a user
            can specify a minimum likelihood. The system only returns a
            finding if its likelihood is above this threshold. If this
            field is not set, the system uses the InspectConfig
            min_likelihood.
        limits (google.cloud.dlp_v2.types.InspectConfig.FindingLimits):
            Configuration to control the number of findings returned.
            This is not used for data profiling.

            When redacting sensitive data from images, finding limits
            don't apply. They can cause unexpected or inconsistent
            results, where only some data is redacted. Don't include
            finding limits in
            [RedactImage][google.privacy.dlp.v2.DlpService.RedactImage]
            requests. Otherwise, Cloud DLP returns an error.

            When set within an
            [InspectJobConfig][google.privacy.dlp.v2.InspectJobConfig],
            the specified maximum values aren't hard limits. If an
            inspection job reaches these limits, the job ends gradually,
            not abruptly. Therefore, the actual number of findings that
            Cloud DLP returns can be multiple times higher than these
            maximum values.
        include_quote (bool):
            When true, a contextual quote from the data that triggered a
            finding is included in the response; see
            [Finding.quote][google.privacy.dlp.v2.Finding.quote]. This
            is not used for data profiling.
        exclude_info_types (bool):
            When true, excludes type information of the
            findings. This is not used for data profiling.
        custom_info_types (MutableSequence[google.cloud.dlp_v2.types.CustomInfoType]):
            CustomInfoTypes provided by the user. See
            https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes
            to learn more.
        content_options (MutableSequence[google.cloud.dlp_v2.types.ContentOption]):
            Deprecated and unused.
        rule_set (MutableSequence[google.cloud.dlp_v2.types.InspectionRuleSet]):
            Set of rules to apply to the findings for this
            InspectConfig. Exclusion rules, contained in the set are
            executed in the end, other rules are executed in the order
            they are specified for each info type. Not supported for the
            ``metadata_key_value_expression`` CustomInfoType.
    """

    class InfoTypeLikelihood(proto.Message):
        r"""Configuration for setting a minimum likelihood per infotype. Used to
        customize the minimum likelihood level for specific infotypes in the
        request. For example, use this if you want to lower the precision
        for PERSON_NAME without lowering the precision for the other
        infotypes in the request.

        Attributes:
            info_type (google.cloud.dlp_v2.types.InfoType):
                Type of information the likelihood threshold applies to.
                Only one likelihood per info_type should be provided. If
                InfoTypeLikelihood does not have an info_type, the
                configuration fails.
            min_likelihood (google.cloud.dlp_v2.types.Likelihood):
                Only returns findings equal to or above this
                threshold. This field is required or else the
                configuration fails.
        """

        info_type: storage.InfoType = proto.Field(
            proto.MESSAGE,
            number=1,
            message=storage.InfoType,
        )
        min_likelihood: storage.Likelihood = proto.Field(
            proto.ENUM,
            number=2,
            enum=storage.Likelihood,
        )

    class FindingLimits(proto.Message):
        r"""Configuration to control the number of findings returned for
        inspection. This is not used for de-identification or data
        profiling.

        When redacting sensitive data from images, finding limits don't
        apply. They can cause unexpected or inconsistent results, where only
        some data is redacted. Don't include finding limits in
        [RedactImage][google.privacy.dlp.v2.DlpService.RedactImage]
        requests. Otherwise, Cloud DLP returns an error.

        Attributes:
            max_findings_per_item (int):
                Max number of findings that are returned for each item
                scanned.

                When set within an
                [InspectContentRequest][google.privacy.dlp.v2.InspectContentRequest],
                this field is ignored.

                This value isn't a hard limit. If the number of findings for
                an item reaches this limit, the inspection of that item ends
                gradually, not abruptly. Therefore, the actual number of
                findings that Cloud DLP returns for the item can be multiple
                times higher than this value.
            max_findings_per_request (int):
                Max number of findings that are returned per request or job.

                If you set this field in an
                [InspectContentRequest][google.privacy.dlp.v2.InspectContentRequest],
                the resulting maximum value is the value that you set or
                3,000, whichever is lower.

                This value isn't a hard limit. If an inspection reaches this
                limit, the inspection ends gradually, not abruptly.
                Therefore, the actual number of findings that Cloud DLP
                returns can be multiple times higher than this value.
            max_findings_per_info_type (MutableSequence[google.cloud.dlp_v2.types.InspectConfig.FindingLimits.InfoTypeLimit]):
                Configuration of findings limit given for
                specified infoTypes.
        """

        class InfoTypeLimit(proto.Message):
            r"""Max findings configuration per infoType, per content item or
            long running DlpJob.

            Attributes:
                info_type (google.cloud.dlp_v2.types.InfoType):
                    Type of information the findings limit applies to. Only one
                    limit per info_type should be provided. If InfoTypeLimit
                    does not have an info_type, the DLP API applies the limit
                    against all info_types that are found but not specified in
                    another InfoTypeLimit.
                max_findings (int):
                    Max findings limit for the given infoType.
            """

            info_type: storage.InfoType = proto.Field(
                proto.MESSAGE,
                number=1,
                message=storage.InfoType,
            )
            max_findings: int = proto.Field(
                proto.INT32,
                number=2,
            )

        max_findings_per_item: int = proto.Field(
            proto.INT32,
            number=1,
        )
        max_findings_per_request: int = proto.Field(
            proto.INT32,
            number=2,
        )
        max_findings_per_info_type: MutableSequence[
            "InspectConfig.FindingLimits.InfoTypeLimit"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="InspectConfig.FindingLimits.InfoTypeLimit",
        )

    info_types: MutableSequence[storage.InfoType] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=storage.InfoType,
    )
    min_likelihood: storage.Likelihood = proto.Field(
        proto.ENUM,
        number=2,
        enum=storage.Likelihood,
    )
    min_likelihood_per_info_type: MutableSequence[InfoTypeLikelihood] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=11,
            message=InfoTypeLikelihood,
        )
    )
    limits: FindingLimits = proto.Field(
        proto.MESSAGE,
        number=3,
        message=FindingLimits,
    )
    include_quote: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    exclude_info_types: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    custom_info_types: MutableSequence[storage.CustomInfoType] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=storage.CustomInfoType,
    )
    content_options: MutableSequence["ContentOption"] = proto.RepeatedField(
        proto.ENUM,
        number=8,
        enum="ContentOption",
    )
    rule_set: MutableSequence["InspectionRuleSet"] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message="InspectionRuleSet",
    )


class ByteContentItem(proto.Message):
    r"""Container for bytes to inspect or redact.

    Attributes:
        type_ (google.cloud.dlp_v2.types.ByteContentItem.BytesType):
            The type of data stored in the bytes string. Default will be
            TEXT_UTF8.
        data (bytes):
            Content data to inspect or redact.
    """

    class BytesType(proto.Enum):
        r"""The type of data being sent for inspection. To learn more, see
        `Supported file
        types <https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types>`__.

        Only the first frame of each multiframe image is inspected. Metadata
        and other frames aren't inspected.

        Values:
            BYTES_TYPE_UNSPECIFIED (0):
                Unused
            IMAGE (6):
                Any image type.
            IMAGE_JPEG (1):
                jpeg
            IMAGE_BMP (2):
                bmp
            IMAGE_PNG (3):
                png
            IMAGE_SVG (4):
                svg
            TEXT_UTF8 (5):
                plain text
            WORD_DOCUMENT (7):
                docx, docm, dotx, dotm
            PDF (8):
                pdf
            POWERPOINT_DOCUMENT (9):
                pptx, pptm, potx, potm, pot
            EXCEL_DOCUMENT (10):
                xlsx, xlsm, xltx, xltm
            AVRO (11):
                avro
            CSV (12):
                csv
            TSV (13):
                tsv
            AUDIO (15):
                Audio file types. Only used for profiling.
            VIDEO (16):
                Video file types. Only used for profiling.
            EXECUTABLE (17):
                Executable file types. Only used for
                profiling.
            AI_MODEL (18):
                AI model file types. Only used for profiling.
        """

        BYTES_TYPE_UNSPECIFIED = 0
        IMAGE = 6
        IMAGE_JPEG = 1
        IMAGE_BMP = 2
        IMAGE_PNG = 3
        IMAGE_SVG = 4
        TEXT_UTF8 = 5
        WORD_DOCUMENT = 7
        PDF = 8
        POWERPOINT_DOCUMENT = 9
        EXCEL_DOCUMENT = 10
        AVRO = 11
        CSV = 12
        TSV = 13
        AUDIO = 15
        VIDEO = 16
        EXECUTABLE = 17
        AI_MODEL = 18

    type_: BytesType = proto.Field(
        proto.ENUM,
        number=1,
        enum=BytesType,
    )
    data: bytes = proto.Field(
        proto.BYTES,
        number=2,
    )


class ContentItem(proto.Message):
    r"""Type of content to inspect.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        value (str):
            String data to inspect or redact.

            This field is a member of `oneof`_ ``data_item``.
        table (google.cloud.dlp_v2.types.Table):
            Structured content for inspection. See
            https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-text#inspecting_a_table
            to learn more.

            This field is a member of `oneof`_ ``data_item``.
        byte_item (google.cloud.dlp_v2.types.ByteContentItem):
            Content data to inspect or redact. Replaces ``type`` and
            ``data``.

            This field is a member of `oneof`_ ``data_item``.
        conversation (google.cloud.dlp_v2.types.Conversation):
            Represents a conversation (either complete or
            a slice). It is assumed that all included
            messages are contiguous and ordered in
            chronological order.

            This field is a member of `oneof`_ ``data_item``.
        batch_content_item (google.cloud.dlp_v2.types.BatchContentItem):
            Represents a batch of items to inspect.

            This field is a member of `oneof`_ ``data_item``.
        content_metadata (google.cloud.dlp_v2.types.ContentMetadata):
            User provided metadata for the content.
    """

    value: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="data_item",
    )
    table: "Table" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="data_item",
        message="Table",
    )
    byte_item: "ByteContentItem" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="data_item",
        message="ByteContentItem",
    )
    conversation: "Conversation" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="data_item",
        message="Conversation",
    )
    batch_content_item: "BatchContentItem" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="data_item",
        message="BatchContentItem",
    )
    content_metadata: "ContentMetadata" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="ContentMetadata",
    )


class ContentMetadata(proto.Message):
    r"""Metadata on content to be scanned.

    Attributes:
        properties (MutableSequence[google.cloud.dlp_v2.types.KeyValueMetadataProperty]):
            User provided key-value pairs of content
            metadata.
        file_labels (MutableSequence[google.cloud.dlp_v2.types.FileLabel]):
            Optional. The file labels associated with the
            content.
    """

    properties: MutableSequence["KeyValueMetadataProperty"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="KeyValueMetadataProperty",
    )
    file_labels: MutableSequence["FileLabel"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="FileLabel",
    )


class Conversation(proto.Message):
    r"""Complete conversation or slice of a conversation.
    It is assumed that all included messages are contiguous and
    ordered in chronological order.

    Attributes:
        messages (MutableSequence[google.cloud.dlp_v2.types.ConversationMessage]):
            Messages exchanged within this conversation.
            The maximum number of messages allowed is 50k.
            The order of the messages is assumed to be
            chronological and will be used to index findings
            in the response.
    """

    messages: MutableSequence["ConversationMessage"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ConversationMessage",
    )


class ConversationMessage(proto.Message):
    r"""Single message in a conversation.

    Attributes:
        content (str):
            The contents of this message.
        message_type (google.cloud.dlp_v2.types.ConversationMessage.MessageType):
            The type of message.
        participant_id (str):
            Optional. The identifier of the participant, for example
            'test-user' or 'gemini'. The participant ID can contain
            lowercase letters, numbers, and hyphens; that is, it must
            match the regular expression:
            ``^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$``. The maximum length is
            63 characters.
    """

    class MessageType(proto.Enum):
        r"""The type of message.
        New values may be added in the future.

        Values:
            MESSAGE_TYPE_UNSPECIFIED (0):
                Unused.
            CONTENT (1):
                Message contains content to be inspected.
            CONTEXT (2):
                Message contains context only and will not
                have findings reported from it during inspection
                or redacted from it during de-identification.
        """

        MESSAGE_TYPE_UNSPECIFIED = 0
        CONTENT = 1
        CONTEXT = 2

    content: str = proto.Field(
        proto.STRING,
        number=1,
    )
    message_type: MessageType = proto.Field(
        proto.ENUM,
        number=2,
        enum=MessageType,
    )
    participant_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class BatchContentItem(proto.Message):
    r"""Represents a batch of content to inspect or redact.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        string_value_batch (google.cloud.dlp_v2.types.StringValueBatch):
            Optional. Represents a batch of string values
            to inspect or redact.

            This field is a member of `oneof`_ ``batch``.
    """

    string_value_batch: "StringValueBatch" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="batch",
        message="StringValueBatch",
    )


class StringValueBatch(proto.Message):
    r"""Represents a batch of string values to inspect or redact.

    Attributes:
        values (MutableSequence[str]):
            Optional. Represents string data to inspect
            or redact.
    """

    values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class Table(proto.Message):
    r"""Structured content to inspect. Up to 50,000 ``Value``\ s per request
    allowed. See
    https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-structured-text#inspecting_a_table
    to learn more.

    Attributes:
        headers (MutableSequence[google.cloud.dlp_v2.types.FieldId]):
            Headers of the table.
        rows (MutableSequence[google.cloud.dlp_v2.types.Table.Row]):
            Rows of the table.
    """

    class Row(proto.Message):
        r"""Values of the row.

        Attributes:
            values (MutableSequence[google.cloud.dlp_v2.types.Value]):
                Individual cells.
        """

        values: MutableSequence["Value"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="Value",
        )

    headers: MutableSequence[storage.FieldId] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=storage.FieldId,
    )
    rows: MutableSequence[Row] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=Row,
    )


class KeyValueMetadataProperty(proto.Message):
    r"""A key-value pair in the Metadata.

    Attributes:
        key (str):
            The key of the property.
        value (str):
            The value of the property.
    """

    key: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: str = proto.Field(
        proto.STRING,
        number=2,
    )


class FileLabel(proto.Message):
    r"""Represents a file label.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        sensitivity_label (google.cloud.dlp_v2.types.FileLabel.SensitivityLabelMetadata):
            Sensitivity labels published by Microsoft.

            This field is a member of `oneof`_ ``type``.
        google_drive_label (google.cloud.dlp_v2.types.FileLabel.GoogleDriveLabelMetadata):
            Google Drive labels published by Google.

            This field is a member of `oneof`_ ``type``.
    """

    class SensitivityLabelMetadata(proto.Message):
        r"""Sensitivity labels published by Microsoft.

        Attributes:
            guid (str):
                Required. The GUID of the sensitivity label.
        """

        guid: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class GoogleDriveLabelMetadata(proto.Message):
        r"""Google Drive labels published by Google.

        Attributes:
            label_id (str):
                The `label
                ID <https://developers.google.com/workspace/drive/labels/guides/overview>`__
                of the Google Drive label.
            label_fields (MutableSequence[google.cloud.dlp_v2.types.FileLabel.GoogleDriveLabelMetadata.LabelFieldMetadata]):
                The field values of the Google Drive label
        """

        class LabelFieldMetadata(proto.Message):
            r"""The field values of the Google Drive label

            Attributes:
                id (str):
                    The identifier of the Label Field.
                value (google.cloud.dlp_v2.types.Value):
                    The value of the Label Field.
            """

            id: str = proto.Field(
                proto.STRING,
                number=1,
            )
            value: "Value" = proto.Field(
                proto.MESSAGE,
                number=2,
                message="Value",
            )

        label_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        label_fields: MutableSequence[
            "FileLabel.GoogleDriveLabelMetadata.LabelFieldMetadata"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="FileLabel.GoogleDriveLabelMetadata.LabelFieldMetadata",
        )

    sensitivity_label: SensitivityLabelMetadata = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="type",
        message=SensitivityLabelMetadata,
    )
    google_drive_label: GoogleDriveLabelMetadata = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="type",
        message=GoogleDriveLabelMetadata,
    )


class InspectResult(proto.Message):
    r"""All the findings for a single scanned item.

    Attributes:
        findings (MutableSequence[google.cloud.dlp_v2.types.Finding]):
            List of findings for an item.
        findings_truncated (bool):
            If true, then this item might have more
            findings than were returned, and the findings
            returned are an arbitrary subset of all
            findings. The findings list might be truncated
            because the input items were too large, or
            because the server reached the maximum amount of
            resources allowed for a single API call. For
            best results, divide the input into smaller
            batches.
    """

    findings: MutableSequence["Finding"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Finding",
    )
    findings_truncated: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class Finding(proto.Message):
    r"""Represents a piece of potentially sensitive content.

    Attributes:
        name (str):
            Resource name in format
            projects/{project}/locations/{location}/findings/{finding}
            Populated only when viewing persisted findings.
        quote (str):
            The content that was found. Even if the content is not
            textual, it may be converted to a textual representation
            here. Provided if ``include_quote`` is true and the finding
            is less than or equal to 4096 bytes long. If the finding
            exceeds 4096 bytes in length, the quote may be omitted.
        info_type (google.cloud.dlp_v2.types.InfoType):
            The type of content that might have been found. Provided if
            ``excluded_types`` is false.
        likelihood (google.cloud.dlp_v2.types.Likelihood):
            Confidence of how likely it is that the ``info_type`` is
            correct.
        location (google.cloud.dlp_v2.types.Location):
            Where the content was found.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp when finding was detected.
        quote_info (google.cloud.dlp_v2.types.QuoteInfo):
            Contains data parsed from quotes. Only populated if
            include_quote was set to true and a supported infoType was
            requested. Currently supported infoTypes: DATE,
            DATE_OF_BIRTH and TIME.
        resource_name (str):
            The job that stored the finding.
        trigger_name (str):
            Job trigger name, if applicable, for this
            finding.
        labels (MutableMapping[str, str]):
            The labels associated with this ``Finding``.

            Label keys must be between 1 and 63 characters long and must
            conform to the following regular expression:
            ``[a-z]([-a-z0-9]*[a-z0-9])?``.

            Label values must be between 0 and 63 characters long and
            must conform to the regular expression
            ``([a-z]([-a-z0-9]*[a-z0-9])?)?``.

            No more than 10 labels can be associated with a given
            finding.

            Examples:

            - ``"environment" : "production"``
            - ``"pipeline" : "etl"``
        job_create_time (google.protobuf.timestamp_pb2.Timestamp):
            Time the job started that produced this
            finding.
        job_name (str):
            The job that stored the finding.
        finding_id (str):
            The unique finding id.
    """

    name: str = proto.Field(
        proto.STRING,
        number=14,
    )
    quote: str = proto.Field(
        proto.STRING,
        number=1,
    )
    info_type: storage.InfoType = proto.Field(
        proto.MESSAGE,
        number=2,
        message=storage.InfoType,
    )
    likelihood: storage.Likelihood = proto.Field(
        proto.ENUM,
        number=3,
        enum=storage.Likelihood,
    )
    location: "Location" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="Location",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    quote_info: "QuoteInfo" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="QuoteInfo",
    )
    resource_name: str = proto.Field(
        proto.STRING,
        number=8,
    )
    trigger_name: str = proto.Field(
        proto.STRING,
        number=9,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=10,
    )
    job_create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    job_name: str = proto.Field(
        proto.STRING,
        number=13,
    )
    finding_id: str = proto.Field(
        proto.STRING,
        number=15,
    )


class Location(proto.Message):
    r"""Specifies the location of the finding.

    Attributes:
        byte_range (google.cloud.dlp_v2.types.Range):
            Zero-based byte offsets delimiting the
            finding. These are relative to the finding's
            containing element. Note that when the content
            is not textual, this references the UTF-8
            encoded textual representation of the content.
            Omitted if content is an image.
        codepoint_range (google.cloud.dlp_v2.types.Range):
            Unicode character offsets delimiting the
            finding. These are relative to the finding's
            containing element. Provided when the content is
            text.
        content_locations (MutableSequence[google.cloud.dlp_v2.types.ContentLocation]):
            List of nested objects pointing to the
            precise location of the finding within the file
            or record.
        container (google.cloud.dlp_v2.types.Container):
            Information about the container where this
            finding occurred, if available.
    """

    byte_range: "Range" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Range",
    )
    codepoint_range: "Range" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Range",
    )
    content_locations: MutableSequence["ContentLocation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="ContentLocation",
    )
    container: "Container" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="Container",
    )


class ContentLocation(proto.Message):
    r"""Precise location of the finding within a document, record,
    image, or metadata container.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        container_name (str):
            Name of the container where the finding is located. The top
            level name is the source file name or table name. Names of
            some common storage containers are formatted as follows:

            - BigQuery tables: ``{project_id}:{dataset_id}.{table_id}``
            - Cloud Storage files: ``gs://{bucket}/{path}``
            - Datastore namespace: {namespace}

            Nested names could be absent if the embedded object has no
            string identifier (for example, an image contained within a
            document).
        record_location (google.cloud.dlp_v2.types.RecordLocation):
            Location within a row or record of a database
            table.

            This field is a member of `oneof`_ ``location``.
        image_location (google.cloud.dlp_v2.types.ImageLocation):
            Location within an image's pixels.

            This field is a member of `oneof`_ ``location``.
        document_location (google.cloud.dlp_v2.types.DocumentLocation):
            Location data for document files.

            This field is a member of `oneof`_ ``location``.
        metadata_location (google.cloud.dlp_v2.types.MetadataLocation):
            Location within the metadata for inspected
            content.

            This field is a member of `oneof`_ ``location``.
        conversation_location (google.cloud.dlp_v2.types.ConversationLocation):
            Location within a conversation.

            This field is a member of `oneof`_ ``location``.
        batch_content_location (google.cloud.dlp_v2.types.BatchContentLocation):
            Location within a batch of content.

            This field is a member of `oneof`_ ``location``.
        container_timestamp (google.protobuf.timestamp_pb2.Timestamp):
            Finding container modification timestamp, if applicable. For
            Cloud Storage, this field contains the last file
            modification timestamp. For a BigQuery table, this field
            contains the last_modified_time property. For Datastore,
            this field isn't populated.
        container_version (str):
            Finding container version, if available
            ("generation" for Cloud Storage).
    """

    container_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    record_location: "RecordLocation" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="location",
        message="RecordLocation",
    )
    image_location: "ImageLocation" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="location",
        message="ImageLocation",
    )
    document_location: "DocumentLocation" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="location",
        message="DocumentLocation",
    )
    metadata_location: "MetadataLocation" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="location",
        message="MetadataLocation",
    )
    conversation_location: "ConversationLocation" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="location",
        message="ConversationLocation",
    )
    batch_content_location: "BatchContentLocation" = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="location",
        message="BatchContentLocation",
    )
    container_timestamp: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    container_version: str = proto.Field(
        proto.STRING,
        number=7,
    )


class ConversationLocation(proto.Message):
    r"""Location within a conversation.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        message_index (int):
            Matches an index of a message in the
            conversation provided in the request.

            This field is a member of `oneof`_ ``location``.
        all_messages (google.cloud.dlp_v2.types.ConversationLocation.AllMessages):
            If set, indicates that the finding applies to
            all messages in the conversation.

            This field is a member of `oneof`_ ``location``.
    """

    class AllMessages(proto.Message):
        r"""If set, indicates that the finding applies to all messages in
        the conversation.

        """

    message_index: int = proto.Field(
        proto.INT32,
        number=1,
        oneof="location",
    )
    all_messages: AllMessages = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="location",
        message=AllMessages,
    )


class BatchContentLocation(proto.Message):
    r"""Location within a batch of content.

    Attributes:
        item_index (int):
            Matches an index of a batch item in the batch
            provided in the request.
    """

    item_index: int = proto.Field(
        proto.INT32,
        number=1,
    )


class MetadataLocation(proto.Message):
    r"""Metadata Location

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        type_ (google.cloud.dlp_v2.types.MetadataType):
            Type of metadata containing the finding.
        storage_label (google.cloud.dlp_v2.types.StorageMetadataLabel):
            Storage metadata.

            This field is a member of `oneof`_ ``label``.
        key_value_metadata_label (google.cloud.dlp_v2.types.KeyValueMetadataLabel):
            Metadata key that contains the finding.

            This field is a member of `oneof`_ ``label``.
    """

    type_: "MetadataType" = proto.Field(
        proto.ENUM,
        number=1,
        enum="MetadataType",
    )
    storage_label: "StorageMetadataLabel" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="label",
        message="StorageMetadataLabel",
    )
    key_value_metadata_label: "KeyValueMetadataLabel" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="label",
        message="KeyValueMetadataLabel",
    )


class StorageMetadataLabel(proto.Message):
    r"""Storage metadata label to indicate which metadata entry
    contains findings.

    Attributes:
        key (str):
            Label name.
    """

    key: str = proto.Field(
        proto.STRING,
        number=1,
    )


class KeyValueMetadataLabel(proto.Message):
    r"""The metadata key that contains a finding.

    Attributes:
        key (str):
            The metadata key. The format depends on the source of the
            metadata.

            Example:

            - ``MSIP_Label_122709e3-8f6b-4860-985f-7f722a94f61e_Enabled``
              (a Microsoft Purview Information Protection key example)
    """

    key: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DocumentLocation(proto.Message):
    r"""Location of a finding within a document.

    Attributes:
        file_offset (int):
            Offset of the line, from the beginning of the
            file, where the finding is located.
    """

    file_offset: int = proto.Field(
        proto.INT64,
        number=1,
    )


class RecordLocation(proto.Message):
    r"""Location of a finding within a row or record.

    Attributes:
        record_key (google.cloud.dlp_v2.types.RecordKey):
            Key of the finding.
        field_id (google.cloud.dlp_v2.types.FieldId):
            Field id of the field containing the finding.
        table_location (google.cloud.dlp_v2.types.TableLocation):
            Location within a ``ContentItem.Table``.
    """

    record_key: storage.RecordKey = proto.Field(
        proto.MESSAGE,
        number=1,
        message=storage.RecordKey,
    )
    field_id: storage.FieldId = proto.Field(
        proto.MESSAGE,
        number=2,
        message=storage.FieldId,
    )
    table_location: "TableLocation" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="TableLocation",
    )


class TableLocation(proto.Message):
    r"""Location of a finding within a table.

    Attributes:
        row_index (int):
            The zero-based index of the row where the finding is
            located. Only populated for resources that have a natural
            ordering, not BigQuery. In BigQuery, to identify the row a
            finding came from, populate
            BigQueryOptions.identifying_fields with your primary key
            column names and when you store the findings the value of
            those columns will be stored inside of Finding.
    """

    row_index: int = proto.Field(
        proto.INT64,
        number=1,
    )


class Container(proto.Message):
    r"""Represents a container that may contain DLP findings.
    Examples of a container include a file, table, or database
    record.

    Attributes:
        type_ (str):
            Container type, for example BigQuery or Cloud
            Storage.
        project_id (str):
            Project where the finding was found.
            Can be different from the project that owns the
            finding.
        full_path (str):
            A string representation of the full container
            name. Examples:

            - BigQuery: 'Project:DataSetId.TableId'
            - Cloud Storage:
              'gs://Bucket/folders/filename.txt'
        root_path (str):
            The root of the container. Examples:

            - For BigQuery table ``project_id:dataset_id.table_id``, the
              root is ``dataset_id``
            - For Cloud Storage file
              ``gs://bucket/folder/filename.txt``, the root is
              ``gs://bucket``
        relative_path (str):
            The rest of the path after the root. Examples:

            - For BigQuery table ``project_id:dataset_id.table_id``, the
              relative path is ``table_id``
            - For Cloud Storage file
              ``gs://bucket/folder/filename.txt``, the relative path is
              ``folder/filename.txt``
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Findings container modification timestamp, if applicable.
            For Cloud Storage, this field contains the last file
            modification timestamp. For a BigQuery table, this field
            contains the last_modified_time property. For Datastore,
            this field isn't populated.
        version (str):
            Findings container version, if available
            ("generation" for Cloud Storage).
    """

    type_: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    full_path: str = proto.Field(
        proto.STRING,
        number=3,
    )
    root_path: str = proto.Field(
        proto.STRING,
        number=4,
    )
    relative_path: str = proto.Field(
        proto.STRING,
        number=5,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    version: str = proto.Field(
        proto.STRING,
        number=7,
    )


class Range(proto.Message):
    r"""Generic half-open interval [start, end)

    Attributes:
        start (int):
            Index of the first character of the range
            (inclusive).
        end (int):
            Index of the last character of the range
            (exclusive).
    """

    start: int = proto.Field(
        proto.INT64,
        number=1,
    )
    end: int = proto.Field(
        proto.INT64,
        number=2,
    )


class ImageLocation(proto.Message):
    r"""Location of the finding within an image.

    Attributes:
        bounding_boxes (MutableSequence[google.cloud.dlp_v2.types.BoundingBox]):
            Bounding boxes locating the pixels within the
            image containing the finding.
    """

    bounding_boxes: MutableSequence["BoundingBox"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="BoundingBox",
    )


class BoundingBox(proto.Message):
    r"""Bounding box encompassing detected text within an image.
    Coordinates are in pixels and strictly within the image or frame
    bounds.

    Attributes:
        top (int):
            Top coordinate of the bounding box. (0,0) is
            upper left.
        left (int):
            Left coordinate of the bounding box. (0,0) is
            upper left.
        width (int):
            Width of the bounding box in pixels.
        height (int):
            Height of the bounding box in pixels.
    """

    top: int = proto.Field(
        proto.INT32,
        number=1,
    )
    left: int = proto.Field(
        proto.INT32,
        number=2,
    )
    width: int = proto.Field(
        proto.INT32,
        number=3,
    )
    height: int = proto.Field(
        proto.INT32,
        number=4,
    )


class RedactImageRequest(proto.Message):
    r"""Request to search for potentially sensitive info in an image
    and redact it by covering it with a colored rectangle.

    Attributes:
        parent (str):
            Parent resource name.

            The format of this value varies depending on whether you
            have `specified a processing
            location <https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location>`__:

            - Projects scope, location specified:
              ``projects/{project_id}/locations/{location_id}``
            - Projects scope, no location specified (defaults to
              global): ``projects/{project_id}``

            The following example ``parent`` string specifies a parent
            project with the identifier ``example-project``, and
            specifies the ``europe-west3`` location for processing data:

            ::

                parent=projects/example-project/locations/europe-west3
        location_id (str):
            Deprecated. This field has no effect.
        inspect_config (google.cloud.dlp_v2.types.InspectConfig):
            Configuration for the inspector.
        image_redaction_configs (MutableSequence[google.cloud.dlp_v2.types.RedactImageRequest.ImageRedactionConfig]):
            The configuration for specifying what content
            to redact from images.
        include_findings (bool):
            Whether the response should include findings
            along with the redacted image.
        byte_item (google.cloud.dlp_v2.types.ByteContentItem):
            The content must be PNG, JPEG, SVG or BMP.
        inspect_template (str):
            The full resource name of the inspection template to use.
            Settings in the main ``inspect_config`` field override the
            corresponding settings in this inspection template.

            The merge behavior is as follows:

            - Singular field: The main field's value replaces the value
              of the corresponding field in the template.
            - Repeated fields: The field values are appended to the list
              defined in the template.
            - Sub-messages and groups: The fields are recursively
              merged.
        deidentify_template (str):
            The full resource name of the de-identification template to
            use. Settings in the main ``image_redaction_configs`` field
            override the corresponding settings in this
            de-identification template. The request fails if the type of
            the template's deidentify_config is not
            image_transformations.
    """

    class ImageRedactionConfig(proto.Message):
        r"""Configuration for determining how redaction of images should
        occur.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            info_type (google.cloud.dlp_v2.types.InfoType):
                Only one per info_type should be provided per request. If
                not specified, and redact_all_text is false, the DLP API
                will redact all text that it matches against all info_types
                that are found, but not specified in another
                ImageRedactionConfig.

                This field is a member of `oneof`_ ``target``.
            redact_all_text (bool):
                If true, all text found in the image, regardless whether it
                matches an info_type, is redacted. Only one should be
                provided.

                This field is a member of `oneof`_ ``target``.
            redaction_color (google.cloud.dlp_v2.types.Color):
                The color to use when redacting content from
                an image. If not specified, the default is
                black.
        """

        info_type: storage.InfoType = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="target",
            message=storage.InfoType,
        )
        redact_all_text: bool = proto.Field(
            proto.BOOL,
            number=2,
            oneof="target",
        )
        redaction_color: "Color" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="Color",
        )

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    location_id: str = proto.Field(
        proto.STRING,
        number=8,
    )
    inspect_config: "InspectConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="InspectConfig",
    )
    image_redaction_configs: MutableSequence[ImageRedactionConfig] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message=ImageRedactionConfig,
        )
    )
    include_findings: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    byte_item: "ByteContentItem" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="ByteContentItem",
    )
    inspect_template: str = proto.Field(
        proto.STRING,
        number=9,
    )
    deidentify_template: str = proto.Field(
        proto.STRING,
        number=10,
    )


class Color(proto.Message):
    r"""Represents a color in the RGB color space.

    Attributes:
        red (float):
            The amount of red in the color as a value in the interval
            [0, 1].
        green (float):
            The amount of green in the color as a value in the interval
            [0, 1].
        blue (float):
            The amount of blue in the color as a value in the interval
            [0, 1].
    """

    red: float = proto.Field(
        proto.FLOAT,
        number=1,
    )
    green: float = proto.Field(
        proto.FLOAT,
        number=2,
    )
    blue: float = proto.Field(
        proto.FLOAT,
        number=3,
    )


class RedactImageResponse(proto.Message):
    r"""Results of redacting an image.

    Attributes:
        redacted_image (bytes):
            The redacted image. The type will be the same
            as the original image.
        extracted_text (str):
            If an image was being inspected and the InspectConfig's
            include_quote was set to true, then this field will include
            all text, if any, that was found in the image.
        inspect_result (google.cloud.dlp_v2.types.InspectResult):
            The findings. Populated when include_findings in the request
            is true.
    """

    redacted_image: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    extracted_text: str = proto.Field(
        proto.STRING,
        number=2,
    )
    inspect_result: "InspectResult" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="InspectResult",
    )


class DeidentifyContentRequest(proto.Message):
    r"""Request to de-identify a ContentItem.

    Attributes:
        parent (str):
            Parent resource name.

            The format of this value varies depending on whether you
            have `specified a processing
            location <https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location>`__:

            - Projects scope, location specified:
              ``projects/{project_id}/locations/{location_id}``
            - Projects scope, no location specified (defaults to
              global): ``projects/{project_id}``

            The following example ``parent`` string specifies a parent
            project with the identifier ``example-project``, and
            specifies the ``europe-west3`` location for processing data:

            ::

                parent=projects/example-project/locations/europe-west3
        deidentify_config (google.cloud.dlp_v2.types.DeidentifyConfig):
            Configuration for the de-identification of the content item.
            Items specified here will override the template referenced
            by the deidentify_template_name argument.
        inspect_config (google.cloud.dlp_v2.types.InspectConfig):
            Configuration for the inspector. Items specified here will
            override the template referenced by the
            inspect_template_name argument.
        item (google.cloud.dlp_v2.types.ContentItem):
            The item to de-identify. Will be treated as text.

            This value must be of type
            [Table][google.privacy.dlp.v2.Table] if your
            [deidentify_config][google.privacy.dlp.v2.DeidentifyContentRequest.deidentify_config]
            is a
            [RecordTransformations][google.privacy.dlp.v2.RecordTransformations]
            object.
        inspect_template_name (str):
            Template to use. Any configuration directly specified in
            inspect_config will override those set in the template.
            Singular fields that are set in this request will replace
            their corresponding fields in the template. Repeated fields
            are appended. Singular sub-messages and groups are
            recursively merged.
        deidentify_template_name (str):
            Template to use. Any configuration directly specified in
            deidentify_config will override those set in the template.
            Singular fields that are set in this request will replace
            their corresponding fields in the template. Repeated fields
            are appended. Singular sub-messages and groups are
            recursively merged.
        location_id (str):
            Deprecated. This field has no effect.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    deidentify_config: "DeidentifyConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DeidentifyConfig",
    )
    inspect_config: "InspectConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="InspectConfig",
    )
    item: "ContentItem" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="ContentItem",
    )
    inspect_template_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    deidentify_template_name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    location_id: str = proto.Field(
        proto.STRING,
        number=7,
    )


class DeidentifyContentResponse(proto.Message):
    r"""Results of de-identifying a ContentItem.

    Attributes:
        item (google.cloud.dlp_v2.types.ContentItem):
            The de-identified item.
        overview (google.cloud.dlp_v2.types.TransformationOverview):
            An overview of the changes that were made on the ``item``.
    """

    item: "ContentItem" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ContentItem",
    )
    overview: "TransformationOverview" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="TransformationOverview",
    )


class ReidentifyContentRequest(proto.Message):
    r"""Request to re-identify an item.

    Attributes:
        parent (str):
            Required. Parent resource name.

            The format of this value varies depending on whether you
            have `specified a processing
            location <https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location>`__:

            - Projects scope, location specified:
              ``projects/{project_id}/locations/{location_id}``
            - Projects scope, no location specified (defaults to
              global): ``projects/{project_id}``

            The following example ``parent`` string specifies a parent
            project with the identifier ``example-project``, and
            specifies the ``europe-west3`` location for processing data:

            ::

                parent=projects/example-project/locations/europe-west3
        reidentify_config (google.cloud.dlp_v2.types.DeidentifyConfig):
            Configuration for the re-identification of the content item.
            This field shares the same proto message type that is used
            for de-identification, however its usage here is for the
            reversal of the previous de-identification.
            Re-identification is performed by examining the
            transformations used to de-identify the items and executing
            the reverse. This requires that only reversible
            transformations be provided here. The reversible
            transformations are:

            - ``CryptoDeterministicConfig``
            - ``CryptoReplaceFfxFpeConfig``
        inspect_config (google.cloud.dlp_v2.types.InspectConfig):
            Configuration for the inspector.
        item (google.cloud.dlp_v2.types.ContentItem):
            The item to re-identify. Will be treated as
            text.
        inspect_template_name (str):
            Template to use. Any configuration directly specified in
            ``inspect_config`` will override those set in the template.
            Singular fields that are set in this request will replace
            their corresponding fields in the template. Repeated fields
            are appended. Singular sub-messages and groups are
            recursively merged.
        reidentify_template_name (str):
            Template to use. References an instance of
            ``DeidentifyTemplate``. Any configuration directly specified
            in ``reidentify_config`` or ``inspect_config`` will override
            those set in the template. The ``DeidentifyTemplate`` used
            must include only reversible transformations. Singular
            fields that are set in this request will replace their
            corresponding fields in the template. Repeated fields are
            appended. Singular sub-messages and groups are recursively
            merged.
        location_id (str):
            Deprecated. This field has no effect.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    reidentify_config: "DeidentifyConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DeidentifyConfig",
    )
    inspect_config: "InspectConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="InspectConfig",
    )
    item: "ContentItem" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="ContentItem",
    )
    inspect_template_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    reidentify_template_name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    location_id: str = proto.Field(
        proto.STRING,
        number=7,
    )


class ReidentifyContentResponse(proto.Message):
    r"""Results of re-identifying an item.

    Attributes:
        item (google.cloud.dlp_v2.types.ContentItem):
            The re-identified item.
        overview (google.cloud.dlp_v2.types.TransformationOverview):
            An overview of the changes that were made to the ``item``.
    """

    item: "ContentItem" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ContentItem",
    )
    overview: "TransformationOverview" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="TransformationOverview",
    )


class InspectContentRequest(proto.Message):
    r"""Request to search for potentially sensitive info in a
    ContentItem.

    Attributes:
        parent (str):
            Parent resource name.

            The format of this value varies depending on whether you
            have `specified a processing
            location <https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location>`__:

            - Projects scope, location specified:
              ``projects/{project_id}/locations/{location_id}``
            - Projects scope, no location specified (defaults to
              global): ``projects/{project_id}``

            The following example ``parent`` string specifies a parent
            project with the identifier ``example-project``, and
            specifies the ``europe-west3`` location for processing data:

            ::

                parent=projects/example-project/locations/europe-west3
        inspect_config (google.cloud.dlp_v2.types.InspectConfig):
            Configuration for the inspector. What specified here will
            override the template referenced by the
            inspect_template_name argument.
        item (google.cloud.dlp_v2.types.ContentItem):
            The item to inspect.
        inspect_template_name (str):
            Template to use. Any configuration directly specified in
            inspect_config will override those set in the template.
            Singular fields that are set in this request will replace
            their corresponding fields in the template. Repeated fields
            are appended. Singular sub-messages and groups are
            recursively merged.
        location_id (str):
            Deprecated. This field has no effect.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    inspect_config: "InspectConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="InspectConfig",
    )
    item: "ContentItem" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ContentItem",
    )
    inspect_template_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    location_id: str = proto.Field(
        proto.STRING,
        number=5,
    )


class InspectContentResponse(proto.Message):
    r"""Results of inspecting an item.

    Attributes:
        result (google.cloud.dlp_v2.types.InspectResult):
            The findings.
    """

    result: "InspectResult" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="InspectResult",
    )


class OutputStorageConfig(proto.Message):
    r"""Cloud repository for storing output.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        table (google.cloud.dlp_v2.types.BigQueryTable):
            Store findings in an existing table or a new table in an
            existing dataset. If table_id is not set a new one will be
            generated for you with the following format:
            dlp_googleapis_yyyy_mm_dd\_[dlp_job_id]. Pacific time zone
            will be used for generating the date details.

            For Inspect, each column in an existing output table must
            have the same name, type, and mode of a field in the
            ``Finding`` object.

            For Risk, an existing output table should be the output of a
            previous Risk analysis job run on the same source table,
            with the same privacy metric and quasi-identifiers. Risk
            jobs that analyze the same table but compute a different
            privacy metric, or use different sets of quasi-identifiers,
            cannot store their results in the same table.

            This field is a member of `oneof`_ ``type``.
        storage_path (google.cloud.dlp_v2.types.CloudStoragePath):
            Store findings in an existing Cloud Storage bucket. Files
            will be generated with the job ID and file part number as
            the filename and will contain findings in textproto format
            as
            [SaveToGcsFindingsOutput][google.privacy.dlp.v2.SaveToGcsFindingsOutput].
            The filename will follow the naming convention
            ``<job_id>-<shard_number>``. Example: ``my-job-id-2``.

            Supported for [Inspect
            jobs][google.privacy.dlp.v2.InspectJobConfig]. The bucket
            must not be the same as the bucket being inspected. If
            storing findings to Cloud Storage, the output schema field
            should not be set. If set, it will be ignored.

            This field is a member of `oneof`_ ``type``.
        output_schema (google.cloud.dlp_v2.types.OutputStorageConfig.OutputSchema):
            Schema used for writing the findings for Inspect jobs. This
            field is only used for Inspect and must be unspecified for
            Risk jobs. Columns are derived from the ``Finding`` object.
            If appending to an existing table, any columns from the
            predefined schema that are missing will be added. No columns
            in the existing table will be deleted.

            If unspecified, then all available columns will be used for
            a new table or an (existing) table with no schema, and no
            changes will be made to an existing table that has a schema.
            Only for use with external storage.
    """

    class OutputSchema(proto.Enum):
        r"""Predefined schemas for storing findings.
        Only for use with external storage.

        Values:
            OUTPUT_SCHEMA_UNSPECIFIED (0):
                Unused.
            BASIC_COLUMNS (1):
                Basic schema including only ``info_type``, ``quote``,
                ``certainty``, and ``timestamp``.
            GCS_COLUMNS (2):
                Schema tailored to findings from scanning
                Cloud Storage.
            DATASTORE_COLUMNS (3):
                Schema tailored to findings from scanning
                Google Datastore.
            BIG_QUERY_COLUMNS (4):
                Schema tailored to findings from scanning
                Google BigQuery.
            ALL_COLUMNS (5):
                Schema containing all columns.
        """

        OUTPUT_SCHEMA_UNSPECIFIED = 0
        BASIC_COLUMNS = 1
        GCS_COLUMNS = 2
        DATASTORE_COLUMNS = 3
        BIG_QUERY_COLUMNS = 4
        ALL_COLUMNS = 5

    table: storage.BigQueryTable = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="type",
        message=storage.BigQueryTable,
    )
    storage_path: storage.CloudStoragePath = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="type",
        message=storage.CloudStoragePath,
    )
    output_schema: OutputSchema = proto.Field(
        proto.ENUM,
        number=3,
        enum=OutputSchema,
    )


class InfoTypeStats(proto.Message):
    r"""Statistics regarding a specific InfoType.

    Attributes:
        info_type (google.cloud.dlp_v2.types.InfoType):
            The type of finding this stat is for.
        count (int):
            Number of findings for this infoType.
    """

    info_type: storage.InfoType = proto.Field(
        proto.MESSAGE,
        number=1,
        message=storage.InfoType,
    )
    count: int = proto.Field(
        proto.INT64,
        number=2,
    )


class InspectDataSourceDetails(proto.Message):
    r"""The results of an inspect DataSource job.

    Attributes:
        requested_options (google.cloud.dlp_v2.types.InspectDataSourceDetails.RequestedOptions):
            The configuration used for this job.
        result (google.cloud.dlp_v2.types.InspectDataSourceDetails.Result):
            Output only. A summary of the outcome of this
            inspection job.
    """

    class RequestedOptions(proto.Message):
        r"""Snapshot of the inspection configuration.

        Attributes:
            snapshot_inspect_template (google.cloud.dlp_v2.types.InspectTemplate):
                Output only. If run with an InspectTemplate,
                a snapshot of its state at the time of this run.
            job_config (google.cloud.dlp_v2.types.InspectJobConfig):
                Inspect config.
        """

        snapshot_inspect_template: "InspectTemplate" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="InspectTemplate",
        )
        job_config: "InspectJobConfig" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="InspectJobConfig",
        )

    class Result(proto.Message):
        r"""All Result fields are updated while the job is processing.

        Attributes:
            processed_bytes (int):
                Total size in bytes that were processed.
            total_estimated_bytes (int):
                Estimate of the number of bytes to process.
            info_type_stats (MutableSequence[google.cloud.dlp_v2.types.InfoTypeStats]):
                Statistics of how many instances of each info
                type were found during inspect job.
            num_rows_processed (int):
                Number of rows scanned after sampling and
                time filtering (applicable for row based stores
                such as BigQuery).
            hybrid_stats (google.cloud.dlp_v2.types.HybridInspectStatistics):
                Statistics related to the processing of
                hybrid inspect.
        """

        processed_bytes: int = proto.Field(
            proto.INT64,
            number=1,
        )
        total_estimated_bytes: int = proto.Field(
            proto.INT64,
            number=2,
        )
        info_type_stats: MutableSequence["InfoTypeStats"] = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="InfoTypeStats",
        )
        num_rows_processed: int = proto.Field(
            proto.INT64,
            number=5,
        )
        hybrid_stats: "HybridInspectStatistics" = proto.Field(
            proto.MESSAGE,
            number=7,
            message="HybridInspectStatistics",
        )

    requested_options: RequestedOptions = proto.Field(
        proto.MESSAGE,
        number=2,
        message=RequestedOptions,
    )
    result: Result = proto.Field(
        proto.MESSAGE,
        number=3,
        message=Result,
    )


class DataProfileBigQueryRowSchema(proto.Message):
    r"""The schema of data to be saved to the BigQuery table when the
    ``DataProfileAction`` is enabled.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        table_profile (google.cloud.dlp_v2.types.TableDataProfile):
            Table data profile column

            This field is a member of `oneof`_ ``data_profile``.
        column_profile (google.cloud.dlp_v2.types.ColumnDataProfile):
            Column data profile column

            This field is a member of `oneof`_ ``data_profile``.
        file_store_profile (google.cloud.dlp_v2.types.FileStoreDataProfile):
            File store data profile column.

            This field is a member of `oneof`_ ``data_profile``.
    """

    table_profile: "TableDataProfile" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="data_profile",
        message="TableDataProfile",
    )
    column_profile: "ColumnDataProfile" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="data_profile",
        message="ColumnDataProfile",
    )
    file_store_profile: "FileStoreDataProfile" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="data_profile",
        message="FileStoreDataProfile",
    )


class HybridInspectStatistics(proto.Message):
    r"""Statistics related to processing hybrid inspect requests.

    Attributes:
        processed_count (int):
            The number of hybrid inspection requests
            processed within this job.
        aborted_count (int):
            The number of hybrid inspection requests
            aborted because the job ran out of quota or was
            ended before they could be processed.
        pending_count (int):
            The number of hybrid requests currently being processed.
            Only populated when called via method ``getDlpJob``. A burst
            of traffic may cause hybrid inspect requests to be enqueued.
            Processing will take place as quickly as possible, but
            resource limitations may impact how long a request is
            enqueued for.
    """

    processed_count: int = proto.Field(
        proto.INT64,
        number=1,
    )
    aborted_count: int = proto.Field(
        proto.INT64,
        number=2,
    )
    pending_count: int = proto.Field(
        proto.INT64,
        number=3,
    )


class ActionDetails(proto.Message):
    r"""The results of an [Action][google.privacy.dlp.v2.Action].

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        deidentify_details (google.cloud.dlp_v2.types.DeidentifyDataSourceDetails):
            Outcome of a de-identification action.

            This field is a member of `oneof`_ ``details``.
    """

    deidentify_details: "DeidentifyDataSourceDetails" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="details",
        message="DeidentifyDataSourceDetails",
    )


class DeidentifyDataSourceStats(proto.Message):
    r"""Summary of what was modified during a transformation.

    Attributes:
        transformed_bytes (int):
            Total size in bytes that were transformed in
            some way.
        transformation_count (int):
            Number of successfully applied
            transformations.
        transformation_error_count (int):
            Number of errors encountered while trying to
            apply transformations.
    """

    transformed_bytes: int = proto.Field(
        proto.INT64,
        number=1,
    )
    transformation_count: int = proto.Field(
        proto.INT64,
        number=2,
    )
    transformation_error_count: int = proto.Field(
        proto.INT64,
        number=3,
    )


class DeidentifyDataSourceDetails(proto.Message):
    r"""The results of a
    [Deidentify][google.privacy.dlp.v2.Action.Deidentify] action from an
    inspect job.

    Attributes:
        requested_options (google.cloud.dlp_v2.types.DeidentifyDataSourceDetails.RequestedDeidentifyOptions):
            De-identification config used for the
            request.
        deidentify_stats (google.cloud.dlp_v2.types.DeidentifyDataSourceStats):
            Stats about the de-identification operation.
    """

    class RequestedDeidentifyOptions(proto.Message):
        r"""De-identification options.

        Attributes:
            snapshot_deidentify_template (google.cloud.dlp_v2.types.DeidentifyTemplate):
                Snapshot of the state of the ``DeidentifyTemplate`` from the
                [Deidentify][google.privacy.dlp.v2.Action.Deidentify] action
                at the time this job was run.
            snapshot_structured_deidentify_template (google.cloud.dlp_v2.types.DeidentifyTemplate):
                Snapshot of the state of the structured
                ``DeidentifyTemplate`` from the ``Deidentify`` action at the
                time this job was run.
            snapshot_image_redact_template (google.cloud.dlp_v2.types.DeidentifyTemplate):
                Snapshot of the state of the image transformation
                ``DeidentifyTemplate`` from the ``Deidentify`` action at the
                time this job was run.
        """

        snapshot_deidentify_template: "DeidentifyTemplate" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="DeidentifyTemplate",
        )
        snapshot_structured_deidentify_template: "DeidentifyTemplate" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="DeidentifyTemplate",
        )
        snapshot_image_redact_template: "DeidentifyTemplate" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="DeidentifyTemplate",
        )

    requested_options: RequestedDeidentifyOptions = proto.Field(
        proto.MESSAGE,
        number=1,
        message=RequestedDeidentifyOptions,
    )
    deidentify_stats: "DeidentifyDataSourceStats" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DeidentifyDataSourceStats",
    )


class LocationSupport(proto.Message):
    r"""Locations at which a feature can be used.

    Attributes:
        regionalization_scope (google.cloud.dlp_v2.types.LocationSupport.RegionalizationScope):
            The current scope for location on this
            feature. This may expand over time.
        locations (MutableSequence[str]):
            Specific locations where the feature may be used. Examples:
            us-central1, us, asia, global If scope is ANY_LOCATION, no
            regions will be listed.
    """

    class RegionalizationScope(proto.Enum):
        r"""The location scope for a feature.

        Values:
            REGIONALIZATION_SCOPE_UNSPECIFIED (0):
                Invalid.
            REGIONAL (1):
                Feature may be used with one or more regions.
                See locations for details.
            ANY_LOCATION (2):
                Feature may be used anywhere. Default value.
        """

        REGIONALIZATION_SCOPE_UNSPECIFIED = 0
        REGIONAL = 1
        ANY_LOCATION = 2

    regionalization_scope: RegionalizationScope = proto.Field(
        proto.ENUM,
        number=1,
        enum=RegionalizationScope,
    )
    locations: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class InfoTypeDescription(proto.Message):
    r"""InfoType description.

    Attributes:
        name (str):
            Internal name of the infoType.
        display_name (str):
            Human readable form of the infoType name.
        supported_by (MutableSequence[google.cloud.dlp_v2.types.InfoTypeSupportedBy]):
            Which parts of the API supports this
            InfoType.
        description (str):
            Description of the infotype. Translated when
            language is provided in the request.
        location_support (google.cloud.dlp_v2.types.LocationSupport):
            Locations at which this feature can be used.
            May change over time.
        example (str):
            A sample that is a true positive for this
            infoType.
        versions (MutableSequence[google.cloud.dlp_v2.types.VersionDescription]):
            A list of available versions for the
            infotype.
        categories (MutableSequence[google.cloud.dlp_v2.types.InfoTypeCategory]):
            The category of the infoType.
        sensitivity_score (google.cloud.dlp_v2.types.SensitivityScore):
            The default sensitivity of the infoType.
        specific_info_types (MutableSequence[str]):
            If this field is set, this infoType is a general infoType
            and these specific infoTypes are contained within it.
            General infoTypes are infoTypes that encompass multiple
            specific infoTypes. For example, the "GEOGRAPHIC_DATA"
            general infoType would have set for this field "LOCATION",
            "LOCATION_COORDINATES", and "STREET_ADDRESS".
        launch_status (google.cloud.dlp_v2.types.InfoTypeDescription.InfoTypeLaunchStatus):
            The launch status of the infoType.
    """

    class InfoTypeLaunchStatus(proto.Enum):
        r"""The launch status of an infoType.

        Values:
            INFO_TYPE_LAUNCH_STATUS_UNSPECIFIED (0):
                Unspecified.
            GENERAL_AVAILABILITY (1):
                InfoType is generally available.
            PUBLIC_PREVIEW (2):
                InfoType is in public preview.
            PRIVATE_PREVIEW (3):
                InfoType is in private preview.
        """

        INFO_TYPE_LAUNCH_STATUS_UNSPECIFIED = 0
        GENERAL_AVAILABILITY = 1
        PUBLIC_PREVIEW = 2
        PRIVATE_PREVIEW = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    supported_by: MutableSequence["InfoTypeSupportedBy"] = proto.RepeatedField(
        proto.ENUM,
        number=3,
        enum="InfoTypeSupportedBy",
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    location_support: "LocationSupport" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="LocationSupport",
    )
    example: str = proto.Field(
        proto.STRING,
        number=8,
    )
    versions: MutableSequence["VersionDescription"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="VersionDescription",
    )
    categories: MutableSequence["InfoTypeCategory"] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message="InfoTypeCategory",
    )
    sensitivity_score: storage.SensitivityScore = proto.Field(
        proto.MESSAGE,
        number=11,
        message=storage.SensitivityScore,
    )
    specific_info_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=12,
    )
    launch_status: InfoTypeLaunchStatus = proto.Field(
        proto.ENUM,
        number=13,
        enum=InfoTypeLaunchStatus,
    )


class InfoTypeCategory(proto.Message):
    r"""Classification of infoTypes to organize them according to
    geographic location, industry, and data type.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        location_category (google.cloud.dlp_v2.types.InfoTypeCategory.LocationCategory):
            The region or country that issued the ID or
            document represented by the infoType.

            This field is a member of `oneof`_ ``category``.
        industry_category (google.cloud.dlp_v2.types.InfoTypeCategory.IndustryCategory):
            The group of relevant businesses where this
            infoType is commonly used

            This field is a member of `oneof`_ ``category``.
        type_category (google.cloud.dlp_v2.types.InfoTypeCategory.TypeCategory):
            The class of identifiers where this infoType
            belongs

            This field is a member of `oneof`_ ``category``.
    """

    class LocationCategory(proto.Enum):
        r"""Enum of the current locations.
        We might add more locations in the future.

        Values:
            LOCATION_UNSPECIFIED (0):
                Unused location
            GLOBAL (1):
                The infoType is not issued by or tied to a
                specific region, but is used almost everywhere.
            ARGENTINA (2):
                The infoType is typically used in Argentina.
            ARMENIA (51):
                The infoType is typically used in Armenia.
            AUSTRALIA (3):
                The infoType is typically used in Australia.
            AUSTRIA (53):
                The infoType is typically used in Austria.
            AZERBAIJAN (48):
                The infoType is typically used in Azerbaijan.
            BELARUS (50):
                The infoType is typically used in Belarus.
            BELGIUM (4):
                The infoType is typically used in Belgium.
            BRAZIL (5):
                The infoType is typically used in Brazil.
            CANADA (6):
                The infoType is typically used in Canada.
            CHILE (7):
                The infoType is typically used in Chile.
            CHINA (8):
                The infoType is typically used in China.
            COLOMBIA (9):
                The infoType is typically used in Colombia.
            CROATIA (42):
                The infoType is typically used in Croatia.
            CZECHIA (52):
                The infoType is typically used in Czechia.
            DENMARK (10):
                The infoType is typically used in Denmark.
            FRANCE (11):
                The infoType is typically used in France.
            FINLAND (12):
                The infoType is typically used in Finland.
            GERMANY (13):
                The infoType is typically used in Germany.
            HONG_KONG (14):
                The infoType is typically used in Hong Kong.
            INDIA (15):
                The infoType is typically used in India.
            INDONESIA (16):
                The infoType is typically used in Indonesia.
            IRELAND (17):
                The infoType is typically used in Ireland.
            ISRAEL (18):
                The infoType is typically used in Israel.
            ITALY (19):
                The infoType is typically used in Italy.
            JAPAN (20):
                The infoType is typically used in Japan.
            KAZAKHSTAN (47):
                The infoType is typically used in Kazakhstan.
            KOREA (21):
                The infoType is typically used in Korea.
            MEXICO (22):
                The infoType is typically used in Mexico.
            THE_NETHERLANDS (23):
                The infoType is typically used in the
                Netherlands.
            NEW_ZEALAND (41):
                The infoType is typically used in New
                Zealand.
            NORWAY (24):
                The infoType is typically used in Norway.
            PARAGUAY (25):
                The infoType is typically used in Paraguay.
            PERU (26):
                The infoType is typically used in Peru.
            POLAND (27):
                The infoType is typically used in Poland.
            PORTUGAL (28):
                The infoType is typically used in Portugal.
            RUSSIA (44):
                The infoType is typically used in Russia.
            SINGAPORE (29):
                The infoType is typically used in Singapore.
            SOUTH_AFRICA (30):
                The infoType is typically used in South
                Africa.
            SPAIN (31):
                The infoType is typically used in Spain.
            SWEDEN (32):
                The infoType is typically used in Sweden.
            SWITZERLAND (43):
                The infoType is typically used in
                Switzerland.
            TAIWAN (33):
                The infoType is typically used in Taiwan.
            THAILAND (34):
                The infoType is typically used in Thailand.
            TURKEY (35):
                The infoType is typically used in Turkey.
            UKRAINE (45):
                The infoType is typically used in Ukraine.
            UNITED_KINGDOM (36):
                The infoType is typically used in the United
                Kingdom.
            UNITED_STATES (37):
                The infoType is typically used in the United
                States.
            URUGUAY (38):
                The infoType is typically used in Uruguay.
            UZBEKISTAN (46):
                The infoType is typically used in Uzbekistan.
            VENEZUELA (39):
                The infoType is typically used in Venezuela.
            INTERNAL (40):
                The infoType is typically used in Google
                internally.
        """

        LOCATION_UNSPECIFIED = 0
        GLOBAL = 1
        ARGENTINA = 2
        ARMENIA = 51
        AUSTRALIA = 3
        AUSTRIA = 53
        AZERBAIJAN = 48
        BELARUS = 50
        BELGIUM = 4
        BRAZIL = 5
        CANADA = 6
        CHILE = 7
        CHINA = 8
        COLOMBIA = 9
        CROATIA = 42
        CZECHIA = 52
        DENMARK = 10
        FRANCE = 11
        FINLAND = 12
        GERMANY = 13
        HONG_KONG = 14
        INDIA = 15
        INDONESIA = 16
        IRELAND = 17
        ISRAEL = 18
        ITALY = 19
        JAPAN = 20
        KAZAKHSTAN = 47
        KOREA = 21
        MEXICO = 22
        THE_NETHERLANDS = 23
        NEW_ZEALAND = 41
        NORWAY = 24
        PARAGUAY = 25
        PERU = 26
        POLAND = 27
        PORTUGAL = 28
        RUSSIA = 44
        SINGAPORE = 29
        SOUTH_AFRICA = 30
        SPAIN = 31
        SWEDEN = 32
        SWITZERLAND = 43
        TAIWAN = 33
        THAILAND = 34
        TURKEY = 35
        UKRAINE = 45
        UNITED_KINGDOM = 36
        UNITED_STATES = 37
        URUGUAY = 38
        UZBEKISTAN = 46
        VENEZUELA = 39
        INTERNAL = 40

    class IndustryCategory(proto.Enum):
        r"""Enum of the current industries in the category.
        We might add more industries in the future.

        Values:
            INDUSTRY_UNSPECIFIED (0):
                Unused industry
            FINANCE (1):
                The infoType is typically used in the finance
                industry.
            HEALTH (2):
                The infoType is typically used in the health
                industry.
            TELECOMMUNICATIONS (3):
                The infoType is typically used in the
                telecommunications industry.
        """

        INDUSTRY_UNSPECIFIED = 0
        FINANCE = 1
        HEALTH = 2
        TELECOMMUNICATIONS = 3

    class TypeCategory(proto.Enum):
        r"""Enum of the current types in the category.
        We might add more types in the future.

        Values:
            TYPE_UNSPECIFIED (0):
                Unused type
            PII (1):
                Personally identifiable information, for
                example, a name or phone number
            SPII (2):
                Personally identifiable information that is
                especially sensitive, for example, a passport
                number.
            DEMOGRAPHIC (3):
                Attributes that can partially identify
                someone, especially in combination with other
                attributes, like age, height, and gender.
            CREDENTIAL (4):
                Confidential or secret information, for
                example, a password.
            GOVERNMENT_ID (5):
                An identification document issued by a
                government.
            DOCUMENT (6):
                A document, for example, a resume or source
                code.
            CONTEXTUAL_INFORMATION (7):
                Information that is not sensitive on its own,
                but provides details about the circumstances
                surrounding an entity or an event.
            CUSTOM (8):
                Category for ``CustomInfoType`` types.
        """

        TYPE_UNSPECIFIED = 0
        PII = 1
        SPII = 2
        DEMOGRAPHIC = 3
        CREDENTIAL = 4
        GOVERNMENT_ID = 5
        DOCUMENT = 6
        CONTEXTUAL_INFORMATION = 7
        CUSTOM = 8

    location_category: LocationCategory = proto.Field(
        proto.ENUM,
        number=1,
        oneof="category",
        enum=LocationCategory,
    )
    industry_category: IndustryCategory = proto.Field(
        proto.ENUM,
        number=2,
        oneof="category",
        enum=IndustryCategory,
    )
    type_category: TypeCategory = proto.Field(
        proto.ENUM,
        number=3,
        oneof="category",
        enum=TypeCategory,
    )


class VersionDescription(proto.Message):
    r"""Details about each available version for an infotype.

    Attributes:
        version (str):
            Name of the version
        description (str):
            Description of the version.
    """

    version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListInfoTypesRequest(proto.Message):
    r"""Request for the list of infoTypes.

    Attributes:
        parent (str):
            The parent resource name.

            The format of this value is as follows:

            ::

                `locations/{location_id}`
        language_code (str):
            BCP-47 language code for localized infoType
            friendly names. If omitted, or if localized
            strings are not available, en-US strings will be
            returned.
        filter (str):
            filter to only return infoTypes supported by certain parts
            of the API. Defaults to supported_by=INSPECT.
        location_id (str):
            Deprecated. This field has no effect.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=4,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListInfoTypesResponse(proto.Message):
    r"""Response to the ListInfoTypes request.

    Attributes:
        info_types (MutableSequence[google.cloud.dlp_v2.types.InfoTypeDescription]):
            Set of sensitive infoTypes.
    """

    info_types: MutableSequence["InfoTypeDescription"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="InfoTypeDescription",
    )


class RiskAnalysisJobConfig(proto.Message):
    r"""Configuration for a risk analysis job. See
    https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-risk-analysis
    to learn more.

    Attributes:
        privacy_metric (google.cloud.dlp_v2.types.PrivacyMetric):
            Privacy metric to compute.
        source_table (google.cloud.dlp_v2.types.BigQueryTable):
            Input dataset to compute metrics over.
        actions (MutableSequence[google.cloud.dlp_v2.types.Action]):
            Actions to execute at the completion of the
            job. Are executed in the order provided.
    """

    privacy_metric: "PrivacyMetric" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="PrivacyMetric",
    )
    source_table: storage.BigQueryTable = proto.Field(
        proto.MESSAGE,
        number=2,
        message=storage.BigQueryTable,
    )
    actions: MutableSequence["Action"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="Action",
    )


class QuasiId(proto.Message):
    r"""A column with a semantic tag attached.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        field (google.cloud.dlp_v2.types.FieldId):
            Required. Identifies the column.
        info_type (google.cloud.dlp_v2.types.InfoType):
            A column can be tagged with a InfoType to use the relevant
            public dataset as a statistical model of population, if
            available. We currently support US ZIP codes, region codes,
            ages and genders. To programmatically obtain the list of
            supported InfoTypes, use ListInfoTypes with the
            supported_by=RISK_ANALYSIS filter.

            This field is a member of `oneof`_ ``tag``.
        custom_tag (str):
            A column can be tagged with a custom tag. In
            this case, the user must indicate an auxiliary
            table that contains statistical information on
            the possible values of this column.

            This field is a member of `oneof`_ ``tag``.
        inferred (google.protobuf.empty_pb2.Empty):
            If no semantic tag is indicated, we infer the
            statistical model from the distribution of
            values in the input data

            This field is a member of `oneof`_ ``tag``.
    """

    field: storage.FieldId = proto.Field(
        proto.MESSAGE,
        number=1,
        message=storage.FieldId,
    )
    info_type: storage.InfoType = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="tag",
        message=storage.InfoType,
    )
    custom_tag: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="tag",
    )
    inferred: empty_pb2.Empty = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="tag",
        message=empty_pb2.Empty,
    )


class StatisticalTable(proto.Message):
    r"""An auxiliary table containing statistical information on the
    relative frequency of different quasi-identifiers values. It has
    one or several quasi-identifiers columns, and one column that
    indicates the relative frequency of each quasi-identifier tuple.
    If a tuple is present in the data but not in the auxiliary
    table, the corresponding relative frequency is assumed to be
    zero (and thus, the tuple is highly reidentifiable).

    Attributes:
        table (google.cloud.dlp_v2.types.BigQueryTable):
            Required. Auxiliary table location.
        quasi_ids (MutableSequence[google.cloud.dlp_v2.types.StatisticalTable.QuasiIdentifierField]):
            Required. Quasi-identifier columns.
        relative_frequency (google.cloud.dlp_v2.types.FieldId):
            Required. The relative frequency column must
            contain a floating-point number between 0 and 1
            (inclusive). Null values are assumed to be zero.
    """

    class QuasiIdentifierField(proto.Message):
        r"""A quasi-identifier column has a custom_tag, used to know which
        column in the data corresponds to which column in the statistical
        model.

        Attributes:
            field (google.cloud.dlp_v2.types.FieldId):
                Identifies the column.
            custom_tag (str):
                A column can be tagged with a custom tag. In
                this case, the user must indicate an auxiliary
                table that contains statistical information on
                the possible values of this column.
        """

        field: storage.FieldId = proto.Field(
            proto.MESSAGE,
            number=1,
            message=storage.FieldId,
        )
        custom_tag: str = proto.Field(
            proto.STRING,
            number=2,
        )

    table: storage.BigQueryTable = proto.Field(
        proto.MESSAGE,
        number=3,
        message=storage.BigQueryTable,
    )
    quasi_ids: MutableSequence[QuasiIdentifierField] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=QuasiIdentifierField,
    )
    relative_frequency: storage.FieldId = proto.Field(
        proto.MESSAGE,
        number=2,
        message=storage.FieldId,
    )


class PrivacyMetric(proto.Message):
    r"""Privacy metric to compute for reidentification risk analysis.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        numerical_stats_config (google.cloud.dlp_v2.types.PrivacyMetric.NumericalStatsConfig):
            Numerical stats

            This field is a member of `oneof`_ ``type``.
        categorical_stats_config (google.cloud.dlp_v2.types.PrivacyMetric.CategoricalStatsConfig):
            Categorical stats

            This field is a member of `oneof`_ ``type``.
        k_anonymity_config (google.cloud.dlp_v2.types.PrivacyMetric.KAnonymityConfig):
            K-anonymity

            This field is a member of `oneof`_ ``type``.
        l_diversity_config (google.cloud.dlp_v2.types.PrivacyMetric.LDiversityConfig):
            l-diversity

            This field is a member of `oneof`_ ``type``.
        k_map_estimation_config (google.cloud.dlp_v2.types.PrivacyMetric.KMapEstimationConfig):
            k-map

            This field is a member of `oneof`_ ``type``.
        delta_presence_estimation_config (google.cloud.dlp_v2.types.PrivacyMetric.DeltaPresenceEstimationConfig):
            delta-presence

            This field is a member of `oneof`_ ``type``.
    """

    class NumericalStatsConfig(proto.Message):
        r"""Compute numerical stats over an individual column, including
        min, max, and quantiles.

        Attributes:
            field (google.cloud.dlp_v2.types.FieldId):
                Field to compute numerical stats on.
                Supported types are integer, float, date,
                datetime, timestamp, time.
        """

        field: storage.FieldId = proto.Field(
            proto.MESSAGE,
            number=1,
            message=storage.FieldId,
        )

    class CategoricalStatsConfig(proto.Message):
        r"""Compute numerical stats over an individual column, including
        number of distinct values and value count distribution.

        Attributes:
            field (google.cloud.dlp_v2.types.FieldId):
                Field to compute categorical stats on. All
                column types are supported except for arrays and
                structs. However, it may be more informative to
                use NumericalStats when the field type is
                supported, depending on the data.
        """

        field: storage.FieldId = proto.Field(
            proto.MESSAGE,
            number=1,
            message=storage.FieldId,
        )

    class KAnonymityConfig(proto.Message):
        r"""k-anonymity metric, used for analysis of reidentification
        risk.

        Attributes:
            quasi_ids (MutableSequence[google.cloud.dlp_v2.types.FieldId]):
                Set of fields to compute k-anonymity over.
                When multiple fields are specified, they are
                considered a single composite key. Structs and
                repeated data types are not supported; however,
                nested fields are supported so long as they are
                not structs themselves or nested within a
                repeated field.
            entity_id (google.cloud.dlp_v2.types.EntityId):
                Message indicating that multiple rows might be associated to
                a single individual. If the same entity_id is associated to
                multiple quasi-identifier tuples over distinct rows, we
                consider the entire collection of tuples as the composite
                quasi-identifier. This collection is a multiset: the order
                in which the different tuples appear in the dataset is
                ignored, but their frequency is taken into account.

                Important note: a maximum of 1000 rows can be associated to
                a single entity ID. If more rows are associated with the
                same entity ID, some might be ignored.
        """

        quasi_ids: MutableSequence[storage.FieldId] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=storage.FieldId,
        )
        entity_id: storage.EntityId = proto.Field(
            proto.MESSAGE,
            number=2,
            message=storage.EntityId,
        )

    class LDiversityConfig(proto.Message):
        r"""l-diversity metric, used for analysis of reidentification
        risk.

        Attributes:
            quasi_ids (MutableSequence[google.cloud.dlp_v2.types.FieldId]):
                Set of quasi-identifiers indicating how
                equivalence classes are defined for the
                l-diversity computation. When multiple fields
                are specified, they are considered a single
                composite key.
            sensitive_attribute (google.cloud.dlp_v2.types.FieldId):
                Sensitive field for computing the l-value.
        """

        quasi_ids: MutableSequence[storage.FieldId] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=storage.FieldId,
        )
        sensitive_attribute: storage.FieldId = proto.Field(
            proto.MESSAGE,
            number=2,
            message=storage.FieldId,
        )

    class KMapEstimationConfig(proto.Message):
        r"""Reidentifiability metric. This corresponds to a risk model
        similar to what is called "journalist risk" in the literature,
        except the attack dataset is statistically modeled instead of
        being perfectly known. This can be done using publicly available
        data (like the US Census), or using a custom statistical model
        (indicated as one or several BigQuery tables), or by
        extrapolating from the distribution of values in the input
        dataset.

        Attributes:
            quasi_ids (MutableSequence[google.cloud.dlp_v2.types.PrivacyMetric.KMapEstimationConfig.TaggedField]):
                Required. Fields considered to be
                quasi-identifiers. No two columns can have the
                same tag.
            region_code (str):
                ISO 3166-1 alpha-2 region code to use in the statistical
                modeling. Set if no column is tagged with a region-specific
                InfoType (like US_ZIP_5) or a region code.
            auxiliary_tables (MutableSequence[google.cloud.dlp_v2.types.PrivacyMetric.KMapEstimationConfig.AuxiliaryTable]):
                Several auxiliary tables can be used in the analysis. Each
                custom_tag used to tag a quasi-identifiers column must
                appear in exactly one column of one auxiliary table.
        """

        class TaggedField(proto.Message):
            r"""A column with a semantic tag attached.

            This message has `oneof`_ fields (mutually exclusive fields).
            For each oneof, at most one member field can be set at the same time.
            Setting any member of the oneof automatically clears all other
            members.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                field (google.cloud.dlp_v2.types.FieldId):
                    Required. Identifies the column.
                info_type (google.cloud.dlp_v2.types.InfoType):
                    A column can be tagged with a InfoType to use the relevant
                    public dataset as a statistical model of population, if
                    available. We currently support US ZIP codes, region codes,
                    ages and genders. To programmatically obtain the list of
                    supported InfoTypes, use ListInfoTypes with the
                    supported_by=RISK_ANALYSIS filter.

                    This field is a member of `oneof`_ ``tag``.
                custom_tag (str):
                    A column can be tagged with a custom tag. In
                    this case, the user must indicate an auxiliary
                    table that contains statistical information on
                    the possible values of this column.

                    This field is a member of `oneof`_ ``tag``.
                inferred (google.protobuf.empty_pb2.Empty):
                    If no semantic tag is indicated, we infer the
                    statistical model from the distribution of
                    values in the input data

                    This field is a member of `oneof`_ ``tag``.
            """

            field: storage.FieldId = proto.Field(
                proto.MESSAGE,
                number=1,
                message=storage.FieldId,
            )
            info_type: storage.InfoType = proto.Field(
                proto.MESSAGE,
                number=2,
                oneof="tag",
                message=storage.InfoType,
            )
            custom_tag: str = proto.Field(
                proto.STRING,
                number=3,
                oneof="tag",
            )
            inferred: empty_pb2.Empty = proto.Field(
                proto.MESSAGE,
                number=4,
                oneof="tag",
                message=empty_pb2.Empty,
            )

        class AuxiliaryTable(proto.Message):
            r"""An auxiliary table contains statistical information on the
            relative frequency of different quasi-identifiers values. It has
            one or several quasi-identifiers columns, and one column that
            indicates the relative frequency of each quasi-identifier tuple.
            If a tuple is present in the data but not in the auxiliary
            table, the corresponding relative frequency is assumed to be
            zero (and thus, the tuple is highly reidentifiable).

            Attributes:
                table (google.cloud.dlp_v2.types.BigQueryTable):
                    Required. Auxiliary table location.
                quasi_ids (MutableSequence[google.cloud.dlp_v2.types.PrivacyMetric.KMapEstimationConfig.AuxiliaryTable.QuasiIdField]):
                    Required. Quasi-identifier columns.
                relative_frequency (google.cloud.dlp_v2.types.FieldId):
                    Required. The relative frequency column must
                    contain a floating-point number between 0 and 1
                    (inclusive). Null values are assumed to be zero.
            """

            class QuasiIdField(proto.Message):
                r"""A quasi-identifier column has a custom_tag, used to know which
                column in the data corresponds to which column in the statistical
                model.

                Attributes:
                    field (google.cloud.dlp_v2.types.FieldId):
                        Identifies the column.
                    custom_tag (str):
                        A auxiliary field.
                """

                field: storage.FieldId = proto.Field(
                    proto.MESSAGE,
                    number=1,
                    message=storage.FieldId,
                )
                custom_tag: str = proto.Field(
                    proto.STRING,
                    number=2,
                )

            table: storage.BigQueryTable = proto.Field(
                proto.MESSAGE,
                number=3,
                message=storage.BigQueryTable,
            )
            quasi_ids: MutableSequence[
                "PrivacyMetric.KMapEstimationConfig.AuxiliaryTable.QuasiIdField"
            ] = proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="PrivacyMetric.KMapEstimationConfig.AuxiliaryTable.QuasiIdField",
            )
            relative_frequency: storage.FieldId = proto.Field(
                proto.MESSAGE,
                number=2,
                message=storage.FieldId,
            )

        quasi_ids: MutableSequence["PrivacyMetric.KMapEstimationConfig.TaggedField"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="PrivacyMetric.KMapEstimationConfig.TaggedField",
            )
        )
        region_code: str = proto.Field(
            proto.STRING,
            number=2,
        )
        auxiliary_tables: MutableSequence[
            "PrivacyMetric.KMapEstimationConfig.AuxiliaryTable"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="PrivacyMetric.KMapEstimationConfig.AuxiliaryTable",
        )

    class DeltaPresenceEstimationConfig(proto.Message):
        r"""δ-presence metric, used to estimate how likely it is for an
        attacker to figure out that one given individual appears in a
        de-identified dataset. Similarly to the k-map metric, we cannot
        compute δ-presence exactly without knowing the attack dataset,
        so we use a statistical model instead.

        Attributes:
            quasi_ids (MutableSequence[google.cloud.dlp_v2.types.QuasiId]):
                Required. Fields considered to be
                quasi-identifiers. No two fields can have the
                same tag.
            region_code (str):
                ISO 3166-1 alpha-2 region code to use in the statistical
                modeling. Set if no column is tagged with a region-specific
                InfoType (like US_ZIP_5) or a region code.
            auxiliary_tables (MutableSequence[google.cloud.dlp_v2.types.StatisticalTable]):
                Several auxiliary tables can be used in the analysis. Each
                custom_tag used to tag a quasi-identifiers field must appear
                in exactly one field of one auxiliary table.
        """

        quasi_ids: MutableSequence["QuasiId"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="QuasiId",
        )
        region_code: str = proto.Field(
            proto.STRING,
            number=2,
        )
        auxiliary_tables: MutableSequence["StatisticalTable"] = proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="StatisticalTable",
        )

    numerical_stats_config: NumericalStatsConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="type",
        message=NumericalStatsConfig,
    )
    categorical_stats_config: CategoricalStatsConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="type",
        message=CategoricalStatsConfig,
    )
    k_anonymity_config: KAnonymityConfig = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="type",
        message=KAnonymityConfig,
    )
    l_diversity_config: LDiversityConfig = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="type",
        message=LDiversityConfig,
    )
    k_map_estimation_config: KMapEstimationConfig = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="type",
        message=KMapEstimationConfig,
    )
    delta_presence_estimation_config: DeltaPresenceEstimationConfig = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="type",
        message=DeltaPresenceEstimationConfig,
    )


class AnalyzeDataSourceRiskDetails(proto.Message):
    r"""Result of a risk analysis operation request.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        requested_privacy_metric (google.cloud.dlp_v2.types.PrivacyMetric):
            Privacy metric to compute.
        requested_source_table (google.cloud.dlp_v2.types.BigQueryTable):
            Input dataset to compute metrics over.
        numerical_stats_result (google.cloud.dlp_v2.types.AnalyzeDataSourceRiskDetails.NumericalStatsResult):
            Output only. Numerical stats result

            This field is a member of `oneof`_ ``result``.
        categorical_stats_result (google.cloud.dlp_v2.types.AnalyzeDataSourceRiskDetails.CategoricalStatsResult):
            Output only. Categorical stats result

            This field is a member of `oneof`_ ``result``.
        k_anonymity_result (google.cloud.dlp_v2.types.AnalyzeDataSourceRiskDetails.KAnonymityResult):
            Output only. K-anonymity result

            This field is a member of `oneof`_ ``result``.
        l_diversity_result (google.cloud.dlp_v2.types.AnalyzeDataSourceRiskDetails.LDiversityResult):
            Output only. L-divesity result

            This field is a member of `oneof`_ ``result``.
        k_map_estimation_result (google.cloud.dlp_v2.types.AnalyzeDataSourceRiskDetails.KMapEstimationResult):
            Output only. K-map result

            This field is a member of `oneof`_ ``result``.
        delta_presence_estimation_result (google.cloud.dlp_v2.types.AnalyzeDataSourceRiskDetails.DeltaPresenceEstimationResult):
            Output only. Delta-presence result

            This field is a member of `oneof`_ ``result``.
        requested_options (google.cloud.dlp_v2.types.AnalyzeDataSourceRiskDetails.RequestedRiskAnalysisOptions):
            The configuration used for this job.
    """

    class NumericalStatsResult(proto.Message):
        r"""Result of the numerical stats computation.

        Attributes:
            min_value (google.cloud.dlp_v2.types.Value):
                Minimum value appearing in the column.
            max_value (google.cloud.dlp_v2.types.Value):
                Maximum value appearing in the column.
            quantile_values (MutableSequence[google.cloud.dlp_v2.types.Value]):
                List of 99 values that partition the set of
                field values into 100 equal sized buckets.
        """

        min_value: "Value" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="Value",
        )
        max_value: "Value" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="Value",
        )
        quantile_values: MutableSequence["Value"] = proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message="Value",
        )

    class CategoricalStatsResult(proto.Message):
        r"""Result of the categorical stats computation.

        Attributes:
            value_frequency_histogram_buckets (MutableSequence[google.cloud.dlp_v2.types.AnalyzeDataSourceRiskDetails.CategoricalStatsResult.CategoricalStatsHistogramBucket]):
                Histogram of value frequencies in the column.
        """

        class CategoricalStatsHistogramBucket(proto.Message):
            r"""Histogram of value frequencies in the column.

            Attributes:
                value_frequency_lower_bound (int):
                    Lower bound on the value frequency of the
                    values in this bucket.
                value_frequency_upper_bound (int):
                    Upper bound on the value frequency of the
                    values in this bucket.
                bucket_size (int):
                    Total number of values in this bucket.
                bucket_values (MutableSequence[google.cloud.dlp_v2.types.ValueFrequency]):
                    Sample of value frequencies in this bucket.
                    The total number of values returned per bucket
                    is capped at 20.
                bucket_value_count (int):
                    Total number of distinct values in this
                    bucket.
            """

            value_frequency_lower_bound: int = proto.Field(
                proto.INT64,
                number=1,
            )
            value_frequency_upper_bound: int = proto.Field(
                proto.INT64,
                number=2,
            )
            bucket_size: int = proto.Field(
                proto.INT64,
                number=3,
            )
            bucket_values: MutableSequence["ValueFrequency"] = proto.RepeatedField(
                proto.MESSAGE,
                number=4,
                message="ValueFrequency",
            )
            bucket_value_count: int = proto.Field(
                proto.INT64,
                number=5,
            )

        value_frequency_histogram_buckets: MutableSequence[
            "AnalyzeDataSourceRiskDetails.CategoricalStatsResult.CategoricalStatsHistogramBucket"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message="AnalyzeDataSourceRiskDetails.CategoricalStatsResult.CategoricalStatsHistogramBucket",
        )

    class KAnonymityResult(proto.Message):
        r"""Result of the k-anonymity computation.

        Attributes:
            equivalence_class_histogram_buckets (MutableSequence[google.cloud.dlp_v2.types.AnalyzeDataSourceRiskDetails.KAnonymityResult.KAnonymityHistogramBucket]):
                Histogram of k-anonymity equivalence classes.
        """

        class KAnonymityEquivalenceClass(proto.Message):
            r"""The set of columns' values that share the same ldiversity
            value

            Attributes:
                quasi_ids_values (MutableSequence[google.cloud.dlp_v2.types.Value]):
                    Set of values defining the equivalence class.
                    One value per quasi-identifier column in the
                    original KAnonymity metric message. The order is
                    always the same as the original request.
                equivalence_class_size (int):
                    Size of the equivalence class, for example
                    number of rows with the above set of values.
            """

            quasi_ids_values: MutableSequence["Value"] = proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="Value",
            )
            equivalence_class_size: int = proto.Field(
                proto.INT64,
                number=2,
            )

        class KAnonymityHistogramBucket(proto.Message):
            r"""Histogram of k-anonymity equivalence classes.

            Attributes:
                equivalence_class_size_lower_bound (int):
                    Lower bound on the size of the equivalence
                    classes in this bucket.
                equivalence_class_size_upper_bound (int):
                    Upper bound on the size of the equivalence
                    classes in this bucket.
                bucket_size (int):
                    Total number of equivalence classes in this
                    bucket.
                bucket_values (MutableSequence[google.cloud.dlp_v2.types.AnalyzeDataSourceRiskDetails.KAnonymityResult.KAnonymityEquivalenceClass]):
                    Sample of equivalence classes in this bucket.
                    The total number of classes returned per bucket
                    is capped at 20.
                bucket_value_count (int):
                    Total number of distinct equivalence classes
                    in this bucket.
            """

            equivalence_class_size_lower_bound: int = proto.Field(
                proto.INT64,
                number=1,
            )
            equivalence_class_size_upper_bound: int = proto.Field(
                proto.INT64,
                number=2,
            )
            bucket_size: int = proto.Field(
                proto.INT64,
                number=3,
            )
            bucket_values: MutableSequence[
                "AnalyzeDataSourceRiskDetails.KAnonymityResult.KAnonymityEquivalenceClass"
            ] = proto.RepeatedField(
                proto.MESSAGE,
                number=4,
                message="AnalyzeDataSourceRiskDetails.KAnonymityResult.KAnonymityEquivalenceClass",
            )
            bucket_value_count: int = proto.Field(
                proto.INT64,
                number=5,
            )

        equivalence_class_histogram_buckets: MutableSequence[
            "AnalyzeDataSourceRiskDetails.KAnonymityResult.KAnonymityHistogramBucket"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message="AnalyzeDataSourceRiskDetails.KAnonymityResult.KAnonymityHistogramBucket",
        )

    class LDiversityResult(proto.Message):
        r"""Result of the l-diversity computation.

        Attributes:
            sensitive_value_frequency_histogram_buckets (MutableSequence[google.cloud.dlp_v2.types.AnalyzeDataSourceRiskDetails.LDiversityResult.LDiversityHistogramBucket]):
                Histogram of l-diversity equivalence class
                sensitive value frequencies.
        """

        class LDiversityEquivalenceClass(proto.Message):
            r"""The set of columns' values that share the same ldiversity
            value.

            Attributes:
                quasi_ids_values (MutableSequence[google.cloud.dlp_v2.types.Value]):
                    Quasi-identifier values defining the
                    k-anonymity equivalence class. The order is
                    always the same as the original request.
                equivalence_class_size (int):
                    Size of the k-anonymity equivalence class.
                num_distinct_sensitive_values (int):
                    Number of distinct sensitive values in this
                    equivalence class.
                top_sensitive_values (MutableSequence[google.cloud.dlp_v2.types.ValueFrequency]):
                    Estimated frequencies of top sensitive
                    values.
            """

            quasi_ids_values: MutableSequence["Value"] = proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="Value",
            )
            equivalence_class_size: int = proto.Field(
                proto.INT64,
                number=2,
            )
            num_distinct_sensitive_values: int = proto.Field(
                proto.INT64,
                number=3,
            )
            top_sensitive_values: MutableSequence["ValueFrequency"] = (
                proto.RepeatedField(
                    proto.MESSAGE,
                    number=4,
                    message="ValueFrequency",
                )
            )

        class LDiversityHistogramBucket(proto.Message):
            r"""Histogram of l-diversity equivalence class sensitive value
            frequencies.

            Attributes:
                sensitive_value_frequency_lower_bound (int):
                    Lower bound on the sensitive value
                    frequencies of the equivalence classes in this
                    bucket.
                sensitive_value_frequency_upper_bound (int):
                    Upper bound on the sensitive value
                    frequencies of the equivalence classes in this
                    bucket.
                bucket_size (int):
                    Total number of equivalence classes in this
                    bucket.
                bucket_values (MutableSequence[google.cloud.dlp_v2.types.AnalyzeDataSourceRiskDetails.LDiversityResult.LDiversityEquivalenceClass]):
                    Sample of equivalence classes in this bucket.
                    The total number of classes returned per bucket
                    is capped at 20.
                bucket_value_count (int):
                    Total number of distinct equivalence classes
                    in this bucket.
            """

            sensitive_value_frequency_lower_bound: int = proto.Field(
                proto.INT64,
                number=1,
            )
            sensitive_value_frequency_upper_bound: int = proto.Field(
                proto.INT64,
                number=2,
            )
            bucket_size: int = proto.Field(
                proto.INT64,
                number=3,
            )
            bucket_values: MutableSequence[
                "AnalyzeDataSourceRiskDetails.LDiversityResult.LDiversityEquivalenceClass"
            ] = proto.RepeatedField(
                proto.MESSAGE,
                number=4,
                message="AnalyzeDataSourceRiskDetails.LDiversityResult.LDiversityEquivalenceClass",
            )
            bucket_value_count: int = proto.Field(
                proto.INT64,
                number=5,
            )

        sensitive_value_frequency_histogram_buckets: MutableSequence[
            "AnalyzeDataSourceRiskDetails.LDiversityResult.LDiversityHistogramBucket"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message="AnalyzeDataSourceRiskDetails.LDiversityResult.LDiversityHistogramBucket",
        )

    class KMapEstimationResult(proto.Message):
        r"""Result of the reidentifiability analysis. Note that these
        results are an estimation, not exact values.

        Attributes:
            k_map_estimation_histogram (MutableSequence[google.cloud.dlp_v2.types.AnalyzeDataSourceRiskDetails.KMapEstimationResult.KMapEstimationHistogramBucket]):
                The intervals [min_anonymity, max_anonymity] do not overlap.
                If a value doesn't correspond to any such interval, the
                associated frequency is zero. For example, the following
                records: {min_anonymity: 1, max_anonymity: 1, frequency: 17}
                {min_anonymity: 2, max_anonymity: 3, frequency: 42}
                {min_anonymity: 5, max_anonymity: 10, frequency: 99} mean
                that there are no record with an estimated anonymity of 4,
                5, or larger than 10.
        """

        class KMapEstimationQuasiIdValues(proto.Message):
            r"""A tuple of values for the quasi-identifier columns.

            Attributes:
                quasi_ids_values (MutableSequence[google.cloud.dlp_v2.types.Value]):
                    The quasi-identifier values.
                estimated_anonymity (int):
                    The estimated anonymity for these
                    quasi-identifier values.
            """

            quasi_ids_values: MutableSequence["Value"] = proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="Value",
            )
            estimated_anonymity: int = proto.Field(
                proto.INT64,
                number=2,
            )

        class KMapEstimationHistogramBucket(proto.Message):
            r"""A KMapEstimationHistogramBucket message with the following values:
            min_anonymity: 3 max_anonymity: 5 frequency: 42 means that there are
            42 records whose quasi-identifier values correspond to 3, 4 or 5
            people in the overlying population. An important particular case is
            when min_anonymity = max_anonymity = 1: the frequency field then
            corresponds to the number of uniquely identifiable records.

            Attributes:
                min_anonymity (int):
                    Always positive.
                max_anonymity (int):
                    Always greater than or equal to min_anonymity.
                bucket_size (int):
                    Number of records within these anonymity
                    bounds.
                bucket_values (MutableSequence[google.cloud.dlp_v2.types.AnalyzeDataSourceRiskDetails.KMapEstimationResult.KMapEstimationQuasiIdValues]):
                    Sample of quasi-identifier tuple values in
                    this bucket. The total number of classes
                    returned per bucket is capped at 20.
                bucket_value_count (int):
                    Total number of distinct quasi-identifier
                    tuple values in this bucket.
            """

            min_anonymity: int = proto.Field(
                proto.INT64,
                number=1,
            )
            max_anonymity: int = proto.Field(
                proto.INT64,
                number=2,
            )
            bucket_size: int = proto.Field(
                proto.INT64,
                number=5,
            )
            bucket_values: MutableSequence[
                "AnalyzeDataSourceRiskDetails.KMapEstimationResult.KMapEstimationQuasiIdValues"
            ] = proto.RepeatedField(
                proto.MESSAGE,
                number=6,
                message="AnalyzeDataSourceRiskDetails.KMapEstimationResult.KMapEstimationQuasiIdValues",
            )
            bucket_value_count: int = proto.Field(
                proto.INT64,
                number=7,
            )

        k_map_estimation_histogram: MutableSequence[
            "AnalyzeDataSourceRiskDetails.KMapEstimationResult.KMapEstimationHistogramBucket"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="AnalyzeDataSourceRiskDetails.KMapEstimationResult.KMapEstimationHistogramBucket",
        )

    class DeltaPresenceEstimationResult(proto.Message):
        r"""Result of the δ-presence computation. Note that these results
        are an estimation, not exact values.

        Attributes:
            delta_presence_estimation_histogram (MutableSequence[google.cloud.dlp_v2.types.AnalyzeDataSourceRiskDetails.DeltaPresenceEstimationResult.DeltaPresenceEstimationHistogramBucket]):
                The intervals [min_probability, max_probability) do not
                overlap. If a value doesn't correspond to any such interval,
                the associated frequency is zero. For example, the following
                records: {min_probability: 0, max_probability: 0.1,
                frequency: 17} {min_probability: 0.2, max_probability: 0.3,
                frequency: 42} {min_probability: 0.3, max_probability: 0.4,
                frequency: 99} mean that there are no record with an
                estimated probability in [0.1, 0.2) nor larger or equal to
                0.4.
        """

        class DeltaPresenceEstimationQuasiIdValues(proto.Message):
            r"""A tuple of values for the quasi-identifier columns.

            Attributes:
                quasi_ids_values (MutableSequence[google.cloud.dlp_v2.types.Value]):
                    The quasi-identifier values.
                estimated_probability (float):
                    The estimated probability that a given individual sharing
                    these quasi-identifier values is in the dataset. This value,
                    typically called δ, is the ratio between the number of
                    records in the dataset with these quasi-identifier values,
                    and the total number of individuals (inside *and* outside
                    the dataset) with these quasi-identifier values. For
                    example, if there are 15 individuals in the dataset who
                    share the same quasi-identifier values, and an estimated 100
                    people in the entire population with these values, then δ is
                    0.15.
            """

            quasi_ids_values: MutableSequence["Value"] = proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="Value",
            )
            estimated_probability: float = proto.Field(
                proto.DOUBLE,
                number=2,
            )

        class DeltaPresenceEstimationHistogramBucket(proto.Message):
            r"""A DeltaPresenceEstimationHistogramBucket message with the following
            values: min_probability: 0.1 max_probability: 0.2 frequency: 42
            means that there are 42 records for which δ is in [0.1, 0.2). An
            important particular case is when min_probability = max_probability
            = 1: then, every individual who shares this quasi-identifier
            combination is in the dataset.

            Attributes:
                min_probability (float):
                    Between 0 and 1.
                max_probability (float):
                    Always greater than or equal to min_probability.
                bucket_size (int):
                    Number of records within these probability
                    bounds.
                bucket_values (MutableSequence[google.cloud.dlp_v2.types.AnalyzeDataSourceRiskDetails.DeltaPresenceEstimationResult.DeltaPresenceEstimationQuasiIdValues]):
                    Sample of quasi-identifier tuple values in
                    this bucket. The total number of classes
                    returned per bucket is capped at 20.
                bucket_value_count (int):
                    Total number of distinct quasi-identifier
                    tuple values in this bucket.
            """

            min_probability: float = proto.Field(
                proto.DOUBLE,
                number=1,
            )
            max_probability: float = proto.Field(
                proto.DOUBLE,
                number=2,
            )
            bucket_size: int = proto.Field(
                proto.INT64,
                number=5,
            )
            bucket_values: MutableSequence[
                "AnalyzeDataSourceRiskDetails.DeltaPresenceEstimationResult.DeltaPresenceEstimationQuasiIdValues"
            ] = proto.RepeatedField(
                proto.MESSAGE,
                number=6,
                message="AnalyzeDataSourceRiskDetails.DeltaPresenceEstimationResult.DeltaPresenceEstimationQuasiIdValues",
            )
            bucket_value_count: int = proto.Field(
                proto.INT64,
                number=7,
            )

        delta_presence_estimation_histogram: MutableSequence[
            "AnalyzeDataSourceRiskDetails.DeltaPresenceEstimationResult.DeltaPresenceEstimationHistogramBucket"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="AnalyzeDataSourceRiskDetails.DeltaPresenceEstimationResult.DeltaPresenceEstimationHistogramBucket",
        )

    class RequestedRiskAnalysisOptions(proto.Message):
        r"""Risk analysis options.

        Attributes:
            job_config (google.cloud.dlp_v2.types.RiskAnalysisJobConfig):
                The job config for the risk job.
        """

        job_config: "RiskAnalysisJobConfig" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="RiskAnalysisJobConfig",
        )

    requested_privacy_metric: "PrivacyMetric" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="PrivacyMetric",
    )
    requested_source_table: storage.BigQueryTable = proto.Field(
        proto.MESSAGE,
        number=2,
        message=storage.BigQueryTable,
    )
    numerical_stats_result: NumericalStatsResult = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="result",
        message=NumericalStatsResult,
    )
    categorical_stats_result: CategoricalStatsResult = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="result",
        message=CategoricalStatsResult,
    )
    k_anonymity_result: KAnonymityResult = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="result",
        message=KAnonymityResult,
    )
    l_diversity_result: LDiversityResult = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="result",
        message=LDiversityResult,
    )
    k_map_estimation_result: KMapEstimationResult = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="result",
        message=KMapEstimationResult,
    )
    delta_presence_estimation_result: DeltaPresenceEstimationResult = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="result",
        message=DeltaPresenceEstimationResult,
    )
    requested_options: RequestedRiskAnalysisOptions = proto.Field(
        proto.MESSAGE,
        number=10,
        message=RequestedRiskAnalysisOptions,
    )


class ValueFrequency(proto.Message):
    r"""A value of a field, including its frequency.

    Attributes:
        value (google.cloud.dlp_v2.types.Value):
            A value contained in the field in question.
        count (int):
            How many times the value is contained in the
            field.
    """

    value: "Value" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Value",
    )
    count: int = proto.Field(
        proto.INT64,
        number=2,
    )


class Value(proto.Message):
    r"""Set of primitive values supported by the system. Note that for the
    purposes of inspection or transformation, the number of bytes
    considered to comprise a 'Value' is based on its representation as a
    UTF-8 encoded string. For example, if 'integer_value' is set to
    123456789, the number of bytes would be counted as 9, even though an
    int64 only holds up to 8 bytes of data.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        integer_value (int):
            integer

            This field is a member of `oneof`_ ``type``.
        float_value (float):
            float

            This field is a member of `oneof`_ ``type``.
        string_value (str):
            string

            This field is a member of `oneof`_ ``type``.
        boolean_value (bool):
            boolean

            This field is a member of `oneof`_ ``type``.
        timestamp_value (google.protobuf.timestamp_pb2.Timestamp):
            timestamp

            This field is a member of `oneof`_ ``type``.
        time_value (google.type.timeofday_pb2.TimeOfDay):
            time of day

            This field is a member of `oneof`_ ``type``.
        date_value (google.type.date_pb2.Date):
            date

            This field is a member of `oneof`_ ``type``.
        day_of_week_value (google.type.dayofweek_pb2.DayOfWeek):
            day of week

            This field is a member of `oneof`_ ``type``.
    """

    integer_value: int = proto.Field(
        proto.INT64,
        number=1,
        oneof="type",
    )
    float_value: float = proto.Field(
        proto.DOUBLE,
        number=2,
        oneof="type",
    )
    string_value: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="type",
    )
    boolean_value: bool = proto.Field(
        proto.BOOL,
        number=4,
        oneof="type",
    )
    timestamp_value: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="type",
        message=timestamp_pb2.Timestamp,
    )
    time_value: timeofday_pb2.TimeOfDay = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="type",
        message=timeofday_pb2.TimeOfDay,
    )
    date_value: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="type",
        message=date_pb2.Date,
    )
    day_of_week_value: dayofweek_pb2.DayOfWeek = proto.Field(
        proto.ENUM,
        number=8,
        oneof="type",
        enum=dayofweek_pb2.DayOfWeek,
    )


class QuoteInfo(proto.Message):
    r"""Message for infoType-dependent details parsed from quote.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        date_time (google.cloud.dlp_v2.types.DateTime):
            The date time indicated by the quote.

            This field is a member of `oneof`_ ``parsed_quote``.
    """

    date_time: "DateTime" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="parsed_quote",
        message="DateTime",
    )


class DateTime(proto.Message):
    r"""Message for a date time object.
    e.g. 2018-01-01, 5th August.

    Attributes:
        date (google.type.date_pb2.Date):
            One or more of the following must be set.
            Must be a valid date or time value.
        day_of_week (google.type.dayofweek_pb2.DayOfWeek):
            Day of week
        time (google.type.timeofday_pb2.TimeOfDay):
            Time of day
        time_zone (google.cloud.dlp_v2.types.DateTime.TimeZone):
            Time zone
    """

    class TimeZone(proto.Message):
        r"""Time zone of the date time object.

        Attributes:
            offset_minutes (int):
                Set only if the offset can be determined.
                Positive for time ahead of UTC. E.g. For
                "UTC-9", this value is -540.
        """

        offset_minutes: int = proto.Field(
            proto.INT32,
            number=1,
        )

    date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=1,
        message=date_pb2.Date,
    )
    day_of_week: dayofweek_pb2.DayOfWeek = proto.Field(
        proto.ENUM,
        number=2,
        enum=dayofweek_pb2.DayOfWeek,
    )
    time: timeofday_pb2.TimeOfDay = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timeofday_pb2.TimeOfDay,
    )
    time_zone: TimeZone = proto.Field(
        proto.MESSAGE,
        number=4,
        message=TimeZone,
    )


class DeidentifyConfig(proto.Message):
    r"""The configuration that controls how the data will change.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        info_type_transformations (google.cloud.dlp_v2.types.InfoTypeTransformations):
            Treat the dataset as free-form text and apply
            the same free text transformation everywhere.

            This field is a member of `oneof`_ ``transformation``.
        record_transformations (google.cloud.dlp_v2.types.RecordTransformations):
            Treat the dataset as structured.
            Transformations can be applied to specific
            locations within structured datasets, such as
            transforming a column within a table.

            This field is a member of `oneof`_ ``transformation``.
        image_transformations (google.cloud.dlp_v2.types.ImageTransformations):
            Treat the dataset as an image and redact.

            This field is a member of `oneof`_ ``transformation``.
        transformation_error_handling (google.cloud.dlp_v2.types.TransformationErrorHandling):
            Mode for handling transformation errors. If left
            unspecified, the default mode is
            ``TransformationErrorHandling.ThrowError``.
    """

    info_type_transformations: "InfoTypeTransformations" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="transformation",
        message="InfoTypeTransformations",
    )
    record_transformations: "RecordTransformations" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="transformation",
        message="RecordTransformations",
    )
    image_transformations: "ImageTransformations" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="transformation",
        message="ImageTransformations",
    )
    transformation_error_handling: "TransformationErrorHandling" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="TransformationErrorHandling",
    )


class ImageTransformations(proto.Message):
    r"""A type of transformation that is applied over images.

    Attributes:
        transforms (MutableSequence[google.cloud.dlp_v2.types.ImageTransformations.ImageTransformation]):
            List of transforms to make.
    """

    class ImageTransformation(proto.Message):
        r"""Configuration for determining how redaction of images should
        occur.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            selected_info_types (google.cloud.dlp_v2.types.ImageTransformations.ImageTransformation.SelectedInfoTypes):
                Apply transformation to the selected info_types.

                This field is a member of `oneof`_ ``target``.
            all_info_types (google.cloud.dlp_v2.types.ImageTransformations.ImageTransformation.AllInfoTypes):
                Apply transformation to all findings not specified in other
                ImageTransformation's selected_info_types. Only one instance
                is allowed within the ImageTransformations message.

                This field is a member of `oneof`_ ``target``.
            all_text (google.cloud.dlp_v2.types.ImageTransformations.ImageTransformation.AllText):
                Apply transformation to all text that doesn't
                match an infoType. Only one instance is allowed
                within the ImageTransformations message.

                This field is a member of `oneof`_ ``target``.
            redaction_color (google.cloud.dlp_v2.types.Color):
                The color to use when redacting content from
                an image. If not specified, the default is
                black.
        """

        class SelectedInfoTypes(proto.Message):
            r"""Apply transformation to the selected info_types.

            Attributes:
                info_types (MutableSequence[google.cloud.dlp_v2.types.InfoType]):
                    Required. InfoTypes to apply the
                    transformation to. Required. Provided InfoType
                    must be unique within the ImageTransformations
                    message.
            """

            info_types: MutableSequence[storage.InfoType] = proto.RepeatedField(
                proto.MESSAGE,
                number=5,
                message=storage.InfoType,
            )

        class AllInfoTypes(proto.Message):
            r"""Apply transformation to all findings."""

        class AllText(proto.Message):
            r"""Apply to all text."""

        selected_info_types: "ImageTransformations.ImageTransformation.SelectedInfoTypes" = proto.Field(
            proto.MESSAGE,
            number=4,
            oneof="target",
            message="ImageTransformations.ImageTransformation.SelectedInfoTypes",
        )
        all_info_types: "ImageTransformations.ImageTransformation.AllInfoTypes" = (
            proto.Field(
                proto.MESSAGE,
                number=5,
                oneof="target",
                message="ImageTransformations.ImageTransformation.AllInfoTypes",
            )
        )
        all_text: "ImageTransformations.ImageTransformation.AllText" = proto.Field(
            proto.MESSAGE,
            number=6,
            oneof="target",
            message="ImageTransformations.ImageTransformation.AllText",
        )
        redaction_color: "Color" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="Color",
        )

    transforms: MutableSequence[ImageTransformation] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=ImageTransformation,
    )


class TransformationErrorHandling(proto.Message):
    r"""How to handle transformation errors during de-identification. A
    transformation error occurs when the requested transformation is
    incompatible with the data. For example, trying to de-identify an IP
    address using a ``DateShift`` transformation would result in a
    transformation error, since date info cannot be extracted from an IP
    address. Information about any incompatible transformations, and how
    they were handled, is returned in the response as part of the
    ``TransformationOverviews``.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        throw_error (google.cloud.dlp_v2.types.TransformationErrorHandling.ThrowError):
            Throw an error

            This field is a member of `oneof`_ ``mode``.
        leave_untransformed (google.cloud.dlp_v2.types.TransformationErrorHandling.LeaveUntransformed):
            Ignore errors

            This field is a member of `oneof`_ ``mode``.
    """

    class ThrowError(proto.Message):
        r"""Throw an error and fail the request when a transformation
        error occurs.

        """

    class LeaveUntransformed(proto.Message):
        r"""Skips the data without modifying it if the requested transformation
        would cause an error. For example, if a ``DateShift`` transformation
        were applied an an IP address, this mode would leave the IP address
        unchanged in the response.

        """

    throw_error: ThrowError = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="mode",
        message=ThrowError,
    )
    leave_untransformed: LeaveUntransformed = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="mode",
        message=LeaveUntransformed,
    )


class PrimitiveTransformation(proto.Message):
    r"""A rule for transforming a value.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        replace_config (google.cloud.dlp_v2.types.ReplaceValueConfig):
            Replace with a specified value.

            This field is a member of `oneof`_ ``transformation``.
        redact_config (google.cloud.dlp_v2.types.RedactConfig):
            Redact

            This field is a member of `oneof`_ ``transformation``.
        character_mask_config (google.cloud.dlp_v2.types.CharacterMaskConfig):
            Mask

            This field is a member of `oneof`_ ``transformation``.
        crypto_replace_ffx_fpe_config (google.cloud.dlp_v2.types.CryptoReplaceFfxFpeConfig):
            Ffx-Fpe. Strongly discouraged, consider using
            CryptoDeterministicConfig instead. Fpe is
            computationally expensive incurring latency
            costs.

            This field is a member of `oneof`_ ``transformation``.
        fixed_size_bucketing_config (google.cloud.dlp_v2.types.FixedSizeBucketingConfig):
            Fixed size bucketing

            This field is a member of `oneof`_ ``transformation``.
        bucketing_config (google.cloud.dlp_v2.types.BucketingConfig):
            Bucketing

            This field is a member of `oneof`_ ``transformation``.
        replace_with_info_type_config (google.cloud.dlp_v2.types.ReplaceWithInfoTypeConfig):
            Replace with infotype

            This field is a member of `oneof`_ ``transformation``.
        time_part_config (google.cloud.dlp_v2.types.TimePartConfig):
            Time extraction

            This field is a member of `oneof`_ ``transformation``.
        crypto_hash_config (google.cloud.dlp_v2.types.CryptoHashConfig):
            Crypto

            This field is a member of `oneof`_ ``transformation``.
        date_shift_config (google.cloud.dlp_v2.types.DateShiftConfig):
            Date Shift

            This field is a member of `oneof`_ ``transformation``.
        crypto_deterministic_config (google.cloud.dlp_v2.types.CryptoDeterministicConfig):
            Deterministic Crypto

            This field is a member of `oneof`_ ``transformation``.
        replace_dictionary_config (google.cloud.dlp_v2.types.ReplaceDictionaryConfig):
            Replace with a value randomly drawn (with
            replacement) from a dictionary.

            This field is a member of `oneof`_ ``transformation``.
    """

    replace_config: "ReplaceValueConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="transformation",
        message="ReplaceValueConfig",
    )
    redact_config: "RedactConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="transformation",
        message="RedactConfig",
    )
    character_mask_config: "CharacterMaskConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="transformation",
        message="CharacterMaskConfig",
    )
    crypto_replace_ffx_fpe_config: "CryptoReplaceFfxFpeConfig" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="transformation",
        message="CryptoReplaceFfxFpeConfig",
    )
    fixed_size_bucketing_config: "FixedSizeBucketingConfig" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="transformation",
        message="FixedSizeBucketingConfig",
    )
    bucketing_config: "BucketingConfig" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="transformation",
        message="BucketingConfig",
    )
    replace_with_info_type_config: "ReplaceWithInfoTypeConfig" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="transformation",
        message="ReplaceWithInfoTypeConfig",
    )
    time_part_config: "TimePartConfig" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="transformation",
        message="TimePartConfig",
    )
    crypto_hash_config: "CryptoHashConfig" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="transformation",
        message="CryptoHashConfig",
    )
    date_shift_config: "DateShiftConfig" = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="transformation",
        message="DateShiftConfig",
    )
    crypto_deterministic_config: "CryptoDeterministicConfig" = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="transformation",
        message="CryptoDeterministicConfig",
    )
    replace_dictionary_config: "ReplaceDictionaryConfig" = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="transformation",
        message="ReplaceDictionaryConfig",
    )


class TimePartConfig(proto.Message):
    r"""For use with ``Date``, ``Timestamp``, and ``TimeOfDay``, extract or
    preserve a portion of the value.

    Attributes:
        part_to_extract (google.cloud.dlp_v2.types.TimePartConfig.TimePart):
            The part of the time to keep.
    """

    class TimePart(proto.Enum):
        r"""Components that make up time.

        Values:
            TIME_PART_UNSPECIFIED (0):
                Unused
            YEAR (1):
                [0-9999]
            MONTH (2):
                [1-12]
            DAY_OF_MONTH (3):
                [1-31]
            DAY_OF_WEEK (4):
                [1-7]
            WEEK_OF_YEAR (5):
                [1-53]
            HOUR_OF_DAY (6):
                [0-23]
        """

        TIME_PART_UNSPECIFIED = 0
        YEAR = 1
        MONTH = 2
        DAY_OF_MONTH = 3
        DAY_OF_WEEK = 4
        WEEK_OF_YEAR = 5
        HOUR_OF_DAY = 6

    part_to_extract: TimePart = proto.Field(
        proto.ENUM,
        number=1,
        enum=TimePart,
    )


class CryptoHashConfig(proto.Message):
    r"""Pseudonymization method that generates surrogates via
    cryptographic hashing. Uses SHA-256.
    The key size must be either 32 or 64 bytes.
    Outputs a base64 encoded representation of the hashed output
    (for example, L7k0BHmF1ha5U3NfGykjro4xWi1MPVQPjhMAZbSV9mM=).
    Currently, only string and integer values can be hashed. See
    https://docs.cloud.google.com/sensitive-data-protection/docs/pseudonymization
    to learn more.

    Attributes:
        crypto_key (google.cloud.dlp_v2.types.CryptoKey):
            The key used by the hash function.
    """

    crypto_key: "CryptoKey" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CryptoKey",
    )


class CryptoDeterministicConfig(proto.Message):
    r"""Pseudonymization method that generates deterministic
    encryption for the given input. Outputs a base64 encoded
    representation of the encrypted output. Uses AES-SIV based on
    the RFC https://tools.ietf.org/html/rfc5297.

    Attributes:
        crypto_key (google.cloud.dlp_v2.types.CryptoKey):
            The key used by the encryption function. For
            deterministic encryption using AES-SIV, the
            provided key is internally expanded to 64 bytes
            prior to use.
        surrogate_info_type (google.cloud.dlp_v2.types.InfoType):
            The custom info type to annotate the surrogate with. This
            annotation will be applied to the surrogate by prefixing it
            with the name of the custom info type followed by the number
            of characters comprising the surrogate. The following scheme
            defines the format: {info type name}({surrogate character
            count}):{surrogate}

            For example, if the name of custom info type is
            'MY_TOKEN_INFO_TYPE' and the surrogate is 'abc', the full
            replacement value will be: 'MY_TOKEN_INFO_TYPE(3):abc'

            This annotation identifies the surrogate when inspecting
            content using the custom info type 'Surrogate'. This
            facilitates reversal of the surrogate when it occurs in free
            text.

            Note: For record transformations where the entire cell in a
            table is being transformed, surrogates are not mandatory.
            Surrogates are used to denote the location of the token and
            are necessary for re-identification in free form text.

            In order for inspection to work properly, the name of this
            info type must not occur naturally anywhere in your data;
            otherwise, inspection may either

            - reverse a surrogate that does not correspond to an actual
              identifier
            - be unable to parse the surrogate and result in an error

            Therefore, choose your custom info type name carefully after
            considering what your data looks like. One way to select a
            name that has a high chance of yielding reliable detection
            is to include one or more unicode characters that are highly
            improbable to exist in your data. For example, assuming your
            data is entered from a regular ASCII keyboard, the symbol
            with the hex code point 29DD might be used like so:
            ⧝MY_TOKEN_TYPE.
        context (google.cloud.dlp_v2.types.FieldId):
            A context may be used for higher security and maintaining
            referential integrity such that the same identifier in two
            different contexts will be given a distinct surrogate. The
            context is appended to plaintext value being encrypted. On
            decryption the provided context is validated against the
            value used during encryption. If a context was provided
            during encryption, same context must be provided during
            decryption as well.

            If the context is not set, plaintext would be used as is for
            encryption. If the context is set but:

            1. there is no record present when transforming a given
               value or
            2. the field is not present when transforming a given value,

            plaintext would be used as is for encryption.

            Note that case (1) is expected when an
            ``InfoTypeTransformation`` is applied to both structured and
            unstructured ``ContentItem``\ s.
    """

    crypto_key: "CryptoKey" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CryptoKey",
    )
    surrogate_info_type: storage.InfoType = proto.Field(
        proto.MESSAGE,
        number=2,
        message=storage.InfoType,
    )
    context: storage.FieldId = proto.Field(
        proto.MESSAGE,
        number=3,
        message=storage.FieldId,
    )


class ReplaceValueConfig(proto.Message):
    r"""Replace each input value with a given ``Value``.

    Attributes:
        new_value (google.cloud.dlp_v2.types.Value):
            Value to replace it with.
    """

    new_value: "Value" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Value",
    )


class ReplaceDictionaryConfig(proto.Message):
    r"""Replace each input value with a value randomly selected from
    the dictionary.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        word_list (google.cloud.dlp_v2.types.CustomInfoType.Dictionary.WordList):
            A list of words to select from for random replacement. The
            `limits <https://docs.cloud.google.com/sensitive-data-protection/limits>`__
            page contains details about the size limits of dictionaries.

            This field is a member of `oneof`_ ``type``.
    """

    word_list: storage.CustomInfoType.Dictionary.WordList = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="type",
        message=storage.CustomInfoType.Dictionary.WordList,
    )


class ReplaceWithInfoTypeConfig(proto.Message):
    r"""Replace each matching finding with the name of the info_type."""


class RedactConfig(proto.Message):
    r"""Redact a given value. For example, if used with an
    ``InfoTypeTransformation`` transforming PHONE_NUMBER, and input 'My
    phone number is 206-555-0123', the output would be 'My phone number
    is '.

    """


class CharsToIgnore(proto.Message):
    r"""Characters to skip when doing deidentification of a value.
    These will be left alone and skipped.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        characters_to_skip (str):
            Characters to not transform when masking.

            This field is a member of `oneof`_ ``characters``.
        common_characters_to_ignore (google.cloud.dlp_v2.types.CharsToIgnore.CommonCharsToIgnore):
            Common characters to not transform when
            masking. Useful to avoid removing punctuation.

            This field is a member of `oneof`_ ``characters``.
    """

    class CommonCharsToIgnore(proto.Enum):
        r"""Convenience enum for indicating common characters to not
        transform.

        Values:
            COMMON_CHARS_TO_IGNORE_UNSPECIFIED (0):
                Unused.
            NUMERIC (1):
                0-9
            ALPHA_UPPER_CASE (2):
                A-Z
            ALPHA_LOWER_CASE (3):
                a-z
            PUNCTUATION (4):
                US Punctuation, one of !"#$%&'()*+,-./:;<=>?@[]^\_`{\|}~
            WHITESPACE (5):
                Whitespace character, one of [ \\t\\n\\x0B\\f\\r]
        """

        COMMON_CHARS_TO_IGNORE_UNSPECIFIED = 0
        NUMERIC = 1
        ALPHA_UPPER_CASE = 2
        ALPHA_LOWER_CASE = 3
        PUNCTUATION = 4
        WHITESPACE = 5

    characters_to_skip: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="characters",
    )
    common_characters_to_ignore: CommonCharsToIgnore = proto.Field(
        proto.ENUM,
        number=2,
        oneof="characters",
        enum=CommonCharsToIgnore,
    )


class CharacterMaskConfig(proto.Message):
    r"""Partially mask a string by replacing a given number of characters
    with a fixed character. Masking can start from the beginning or end
    of the string. This can be used on data of any type (numbers, longs,
    and so on) and when de-identifying structured data we'll attempt to
    preserve the original data's type. (This allows you to take a long
    like 123 and modify it to a string like \**3.

    Attributes:
        masking_character (str):
            Character to use to mask the sensitive values—for example,
            ``*`` for an alphabetic string such as a name, or ``0`` for
            a numeric string such as ZIP code or credit card number.
            This string must have a length of 1. If not supplied, this
            value defaults to ``*`` for strings, and ``0`` for digits.
        number_to_mask (int):
            Number of characters to mask. If not set, all matching chars
            will be masked. Skipped characters do not count towards this
            tally.

            If ``number_to_mask`` is negative, this denotes inverse
            masking. Cloud DLP masks all but a number of characters. For
            example, suppose you have the following values:

            - ``masking_character`` is ``*``
            - ``number_to_mask`` is ``-4``
            - ``reverse_order`` is ``false``
            - ``CharsToIgnore`` includes ``-``
            - Input string is ``1234-5678-9012-3456``

            The resulting de-identified string is
            ``****-****-****-3456``. Cloud DLP masks all but the last
            four characters. If ``reverse_order`` is ``true``, all but
            the first four characters are masked as
            ``1234-****-****-****``.
        reverse_order (bool):
            Mask characters in reverse order. For example, if
            ``masking_character`` is ``0``, ``number_to_mask`` is
            ``14``, and ``reverse_order`` is ``false``, then the input
            string ``1234-5678-9012-3456`` is masked as
            ``00000000000000-3456``. If ``masking_character`` is ``*``,
            ``number_to_mask`` is ``3``, and ``reverse_order`` is
            ``true``, then the string ``12345`` is masked as ``12***``.
        characters_to_ignore (MutableSequence[google.cloud.dlp_v2.types.CharsToIgnore]):
            When masking a string, items in this list will be skipped
            when replacing characters. For example, if the input string
            is ``555-555-5555`` and you instruct Cloud DLP to skip ``-``
            and mask 5 characters with ``*``, Cloud DLP returns
            ``***-**5-5555``.
    """

    masking_character: str = proto.Field(
        proto.STRING,
        number=1,
    )
    number_to_mask: int = proto.Field(
        proto.INT32,
        number=2,
    )
    reverse_order: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    characters_to_ignore: MutableSequence["CharsToIgnore"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="CharsToIgnore",
    )


class FixedSizeBucketingConfig(proto.Message):
    r"""Buckets values based on fixed size ranges. The Bucketing
    transformation can provide all of this functionality, but requires
    more configuration. This message is provided as a convenience to the
    user for simple bucketing strategies.

    The transformed value will be a hyphenated string of
    {lower_bound}-{upper_bound}. For example, if lower_bound = 10 and
    upper_bound = 20, all values that are within this bucket will be
    replaced with "10-20".

    This can be used on data of type: double, long.

    If the bound Value type differs from the type of data being
    transformed, we will first attempt converting the type of the data
    to be transformed to match the type of the bound before comparing.

    See
    https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-bucketing
    to learn more.

    Attributes:
        lower_bound (google.cloud.dlp_v2.types.Value):
            Required. Lower bound value of buckets. All values less than
            ``lower_bound`` are grouped together into a single bucket;
            for example if ``lower_bound`` = 10, then all values less
            than 10 are replaced with the value "-10".
        upper_bound (google.cloud.dlp_v2.types.Value):
            Required. Upper bound value of buckets. All values greater
            than upper_bound are grouped together into a single bucket;
            for example if ``upper_bound`` = 89, then all values greater
            than 89 are replaced with the value "89+".
        bucket_size (float):
            Required. Size of each bucket (except for minimum and
            maximum buckets). So if ``lower_bound`` = 10,
            ``upper_bound`` = 89, and ``bucket_size`` = 10, then the
            following buckets would be used: -10, 10-20, 20-30, 30-40,
            40-50, 50-60, 60-70, 70-80, 80-89, 89+. Precision up to 2
            decimals works.
    """

    lower_bound: "Value" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Value",
    )
    upper_bound: "Value" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Value",
    )
    bucket_size: float = proto.Field(
        proto.DOUBLE,
        number=3,
    )


class BucketingConfig(proto.Message):
    r"""Generalization function that buckets values based on ranges. The
    ranges and replacement values are dynamically provided by the user
    for custom behavior, such as 1-30 -> LOW, 31-65 -> MEDIUM, 66-100 ->
    HIGH.

    This can be used on data of type: number, long, string, timestamp.

    If the bound ``Value`` type differs from the type of data being
    transformed, we will first attempt converting the type of the data
    to be transformed to match the type of the bound before comparing.
    See
    https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-bucketing
    to learn more.

    Attributes:
        buckets (MutableSequence[google.cloud.dlp_v2.types.BucketingConfig.Bucket]):
            Set of buckets. Ranges must be
            non-overlapping.
    """

    class Bucket(proto.Message):
        r"""Bucket is represented as a range, along with replacement
        values.

        Attributes:
            min_ (google.cloud.dlp_v2.types.Value):
                Lower bound of the range, inclusive. Type
                should be the same as max if used.
            max_ (google.cloud.dlp_v2.types.Value):
                Upper bound of the range, exclusive; type
                must match min.
            replacement_value (google.cloud.dlp_v2.types.Value):
                Required. Replacement value for this bucket.
        """

        min_: "Value" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="Value",
        )
        max_: "Value" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="Value",
        )
        replacement_value: "Value" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="Value",
        )

    buckets: MutableSequence[Bucket] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=Bucket,
    )


class CryptoReplaceFfxFpeConfig(proto.Message):
    r"""Replaces an identifier with a surrogate using Format Preserving
    Encryption (FPE) with the FFX mode of operation; however when used
    in the ``ReidentifyContent`` API method, it serves the opposite
    function by reversing the surrogate back into the original
    identifier. The identifier must be encoded as ASCII. For a given
    crypto key and context, the same identifier will be replaced with
    the same surrogate. Identifiers must be at least two characters
    long. In the case that the identifier is the empty string, it will
    be skipped. See
    https://docs.cloud.google.com/sensitive-data-protection/docs/pseudonymization
    to learn more.

    Note: We recommend using CryptoDeterministicConfig for all use cases
    which do not require preserving the input alphabet space and size,
    plus warrant referential integrity. FPE incurs significant latency
    costs.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        crypto_key (google.cloud.dlp_v2.types.CryptoKey):
            Required. The key used by the encryption
            algorithm.
        context (google.cloud.dlp_v2.types.FieldId):
            The 'tweak', a context may be used for higher security since
            the same identifier in two different contexts won't be given
            the same surrogate. If the context is not set, a default
            tweak will be used.

            If the context is set but:

            1. there is no record present when transforming a given
               value or
            2. the field is not present when transforming a given value,

            a default tweak will be used.

            Note that case (1) is expected when an
            ``InfoTypeTransformation`` is applied to both structured and
            unstructured ``ContentItem``\ s. Currently, the referenced
            field may be of value type integer or string.

            The tweak is constructed as a sequence of bytes in big
            endian byte order such that:

            - a 64 bit integer is encoded followed by a single byte of
              value 1
            - a string is encoded in UTF-8 format followed by a single
              byte of value 2
        common_alphabet (google.cloud.dlp_v2.types.CryptoReplaceFfxFpeConfig.FfxCommonNativeAlphabet):
            Common alphabets.

            This field is a member of `oneof`_ ``alphabet``.
        custom_alphabet (str):
            This is supported by mapping these to the alphanumeric
            characters that the FFX mode natively supports. This happens
            before/after encryption/decryption. Each character listed
            must appear only once. Number of characters must be in the
            range [2, 95]. This must be encoded as ASCII. The order of
            characters does not matter. The full list of allowed
            characters is:
            :literal:`0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz~\`!@#$%^&*()\_-+={[}]|\\:;"'<,>.?/`

            This field is a member of `oneof`_ ``alphabet``.
        radix (int):
            The native way to select the alphabet. Must be in the range
            [2, 95].

            This field is a member of `oneof`_ ``alphabet``.
        surrogate_info_type (google.cloud.dlp_v2.types.InfoType):
            The custom infoType to annotate the surrogate with. This
            annotation will be applied to the surrogate by prefixing it
            with the name of the custom infoType followed by the number
            of characters comprising the surrogate. The following scheme
            defines the format:
            info_type_name(surrogate_character_count):surrogate

            For example, if the name of custom infoType is
            'MY_TOKEN_INFO_TYPE' and the surrogate is 'abc', the full
            replacement value will be: 'MY_TOKEN_INFO_TYPE(3):abc'

            This annotation identifies the surrogate when inspecting
            content using the custom infoType
            ```SurrogateType`` <https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#surrogatetype>`__.
            This facilitates reversal of the surrogate when it occurs in
            free text.

            In order for inspection to work properly, the name of this
            infoType must not occur naturally anywhere in your data;
            otherwise, inspection may find a surrogate that does not
            correspond to an actual identifier. Therefore, choose your
            custom infoType name carefully after considering what your
            data looks like. One way to select a name that has a high
            chance of yielding reliable detection is to include one or
            more unicode characters that are highly improbable to exist
            in your data. For example, assuming your data is entered
            from a regular ASCII keyboard, the symbol with the hex code
            point 29DD might be used like so: ⧝MY_TOKEN_TYPE
    """

    class FfxCommonNativeAlphabet(proto.Enum):
        r"""These are commonly used subsets of the alphabet that the FFX
        mode natively supports. In the algorithm, the alphabet is
        selected using the "radix". Therefore each corresponds to a
        particular radix.

        Values:
            FFX_COMMON_NATIVE_ALPHABET_UNSPECIFIED (0):
                Unused.
            NUMERIC (1):
                ``[0-9]`` (radix of 10)
            HEXADECIMAL (2):
                ``[0-9A-F]`` (radix of 16)
            UPPER_CASE_ALPHA_NUMERIC (3):
                ``[0-9A-Z]`` (radix of 36)
            ALPHA_NUMERIC (4):
                ``[0-9A-Za-z]`` (radix of 62)
        """

        FFX_COMMON_NATIVE_ALPHABET_UNSPECIFIED = 0
        NUMERIC = 1
        HEXADECIMAL = 2
        UPPER_CASE_ALPHA_NUMERIC = 3
        ALPHA_NUMERIC = 4

    crypto_key: "CryptoKey" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CryptoKey",
    )
    context: storage.FieldId = proto.Field(
        proto.MESSAGE,
        number=2,
        message=storage.FieldId,
    )
    common_alphabet: FfxCommonNativeAlphabet = proto.Field(
        proto.ENUM,
        number=4,
        oneof="alphabet",
        enum=FfxCommonNativeAlphabet,
    )
    custom_alphabet: str = proto.Field(
        proto.STRING,
        number=5,
        oneof="alphabet",
    )
    radix: int = proto.Field(
        proto.INT32,
        number=6,
        oneof="alphabet",
    )
    surrogate_info_type: storage.InfoType = proto.Field(
        proto.MESSAGE,
        number=8,
        message=storage.InfoType,
    )


class CryptoKey(proto.Message):
    r"""This is a data encryption key (DEK) (as opposed to
    a key encryption key (KEK) stored by Cloud Key Management
    Service (Cloud KMS).
    When using Cloud KMS to wrap or unwrap a DEK, be sure to set an
    appropriate IAM policy on the KEK to ensure an attacker cannot
    unwrap the DEK.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        transient (google.cloud.dlp_v2.types.TransientCryptoKey):
            Transient crypto key

            This field is a member of `oneof`_ ``source``.
        unwrapped (google.cloud.dlp_v2.types.UnwrappedCryptoKey):
            Unwrapped crypto key

            This field is a member of `oneof`_ ``source``.
        kms_wrapped (google.cloud.dlp_v2.types.KmsWrappedCryptoKey):
            Key wrapped using Cloud KMS

            This field is a member of `oneof`_ ``source``.
    """

    transient: "TransientCryptoKey" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="source",
        message="TransientCryptoKey",
    )
    unwrapped: "UnwrappedCryptoKey" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="source",
        message="UnwrappedCryptoKey",
    )
    kms_wrapped: "KmsWrappedCryptoKey" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="source",
        message="KmsWrappedCryptoKey",
    )


class TransientCryptoKey(proto.Message):
    r"""Use this to have a random data crypto key generated.
    It will be discarded after the request finishes.

    Attributes:
        name (str):
            Required. Name of the key. This is an arbitrary string used
            to differentiate different keys. A unique key is generated
            per name: two separate ``TransientCryptoKey`` protos share
            the same generated key if their names are the same. When the
            data crypto key is generated, this name is not used in any
            way (repeating the api call will result in a different key
            being generated).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UnwrappedCryptoKey(proto.Message):
    r"""Using raw keys is prone to security risks due to accidentally
    leaking the key. Choose another type of key if possible.

    Attributes:
        key (bytes):
            Required. A 128/192/256 bit key.
    """

    key: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )


class KmsWrappedCryptoKey(proto.Message):
    r"""Include to use an existing data crypto key wrapped by KMS. The
    wrapped key must be a 128-, 192-, or 256-bit key. Authorization
    requires the following IAM permissions when sending a request to
    perform a crypto transformation using a KMS-wrapped crypto key:
    dlp.kms.encrypt

    For more information, see [Creating a wrapped key]
    (https://docs.cloud.google.com/sensitive-data-protection/docs/create-wrapped-key).

    Note: When you use Cloud KMS for cryptographic operations, `charges
    apply <https://cloud.google.com/kms/pricing>`__.

    Attributes:
        wrapped_key (bytes):
            Required. The wrapped data crypto key.
        crypto_key_name (str):
            Required. The resource name of the KMS
            CryptoKey to use for unwrapping.
    """

    wrapped_key: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    crypto_key_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DateShiftConfig(proto.Message):
    r"""Shifts dates by random number of days, with option to be
    consistent for the same context. See
    https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-date-shifting
    to learn more.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        upper_bound_days (int):
            Required. Range of shift in days. Actual
            shift will be selected at random within this
            range (inclusive ends). Negative means shift to
            earlier in time. Must not be more than 365250
            days (1000 years) each direction.

            For example, 3 means shift date to at most 3
            days into the future.
        lower_bound_days (int):
            Required. For example, -5 means shift date to
            at most 5 days back in the past.
        context (google.cloud.dlp_v2.types.FieldId):
            Points to the field that contains the
            context, for example, an entity id. If set, must
            also set cryptoKey. If set, shift will be
            consistent for the given context.
        crypto_key (google.cloud.dlp_v2.types.CryptoKey):
            Causes the shift to be computed based on this key and the
            context. This results in the same shift for the same context
            and crypto_key. If set, must also set context. Can only be
            applied to table items.

            This field is a member of `oneof`_ ``method``.
    """

    upper_bound_days: int = proto.Field(
        proto.INT32,
        number=1,
    )
    lower_bound_days: int = proto.Field(
        proto.INT32,
        number=2,
    )
    context: storage.FieldId = proto.Field(
        proto.MESSAGE,
        number=3,
        message=storage.FieldId,
    )
    crypto_key: "CryptoKey" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="method",
        message="CryptoKey",
    )


class InfoTypeTransformations(proto.Message):
    r"""A type of transformation that will scan unstructured text and apply
    various ``PrimitiveTransformation``\ s to each finding, where the
    transformation is applied to only values that were identified as a
    specific info_type.

    Attributes:
        transformations (MutableSequence[google.cloud.dlp_v2.types.InfoTypeTransformations.InfoTypeTransformation]):
            Required. Transformation for each infoType.
            Cannot specify more than one for a given
            infoType.
    """

    class InfoTypeTransformation(proto.Message):
        r"""A transformation to apply to text that is identified as a specific
        info_type.

        Attributes:
            info_types (MutableSequence[google.cloud.dlp_v2.types.InfoType]):
                InfoTypes to apply the transformation to. An empty list will
                cause this transformation to apply to all findings that
                correspond to infoTypes that were requested in
                ``InspectConfig``.
            primitive_transformation (google.cloud.dlp_v2.types.PrimitiveTransformation):
                Required. Primitive transformation to apply
                to the infoType.
        """

        info_types: MutableSequence[storage.InfoType] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=storage.InfoType,
        )
        primitive_transformation: "PrimitiveTransformation" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="PrimitiveTransformation",
        )

    transformations: MutableSequence[InfoTypeTransformation] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=InfoTypeTransformation,
    )


class FieldTransformation(proto.Message):
    r"""The transformation to apply to the field.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        fields (MutableSequence[google.cloud.dlp_v2.types.FieldId]):
            Required. Input field(s) to apply the transformation to.
            When you have columns that reference their position within a
            list, omit the index from the FieldId. FieldId name matching
            ignores the index. For example, instead of
            "contact.nums[0].type", use "contact.nums.type".
        condition (google.cloud.dlp_v2.types.RecordCondition):
            Only apply the transformation if the condition evaluates to
            true for the given ``RecordCondition``. The conditions are
            allowed to reference fields that are not used in the actual
            transformation.

            Example Use Cases:

            - Apply a different bucket transformation to an age column
              if the zip code column for the same record is within a
              specific range.
            - Redact a field if the date of birth field is greater than
              85.
        primitive_transformation (google.cloud.dlp_v2.types.PrimitiveTransformation):
            Apply the transformation to the entire field.

            This field is a member of `oneof`_ ``transformation``.
        info_type_transformations (google.cloud.dlp_v2.types.InfoTypeTransformations):
            Treat the contents of the field as free text, and
            selectively transform content that matches an ``InfoType``.

            This field is a member of `oneof`_ ``transformation``.
    """

    fields: MutableSequence[storage.FieldId] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=storage.FieldId,
    )
    condition: "RecordCondition" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="RecordCondition",
    )
    primitive_transformation: "PrimitiveTransformation" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="transformation",
        message="PrimitiveTransformation",
    )
    info_type_transformations: "InfoTypeTransformations" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="transformation",
        message="InfoTypeTransformations",
    )


class RecordTransformations(proto.Message):
    r"""A type of transformation that is applied over structured data
    such as a table.

    Attributes:
        field_transformations (MutableSequence[google.cloud.dlp_v2.types.FieldTransformation]):
            Transform the record by applying various
            field transformations.
        record_suppressions (MutableSequence[google.cloud.dlp_v2.types.RecordSuppression]):
            Configuration defining which records get
            suppressed entirely. Records that match any
            suppression rule are omitted from the output.
    """

    field_transformations: MutableSequence["FieldTransformation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="FieldTransformation",
    )
    record_suppressions: MutableSequence["RecordSuppression"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="RecordSuppression",
    )


class RecordSuppression(proto.Message):
    r"""Configuration to suppress records whose suppression
    conditions evaluate to true.

    Attributes:
        condition (google.cloud.dlp_v2.types.RecordCondition):
            A condition that when it evaluates to true
            will result in the record being evaluated to be
            suppressed from the transformed content.
    """

    condition: "RecordCondition" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="RecordCondition",
    )


class RecordCondition(proto.Message):
    r"""A condition for determining whether a transformation should
    be applied to a field.

    Attributes:
        expressions (google.cloud.dlp_v2.types.RecordCondition.Expressions):
            An expression.
    """

    class Condition(proto.Message):
        r"""The field type of ``value`` and ``field`` do not need to match to be
        considered equal, but not all comparisons are possible. EQUAL_TO and
        NOT_EQUAL_TO attempt to compare even with incompatible types, but
        all other comparisons are invalid with incompatible types. A
        ``value`` of type:

        - ``string`` can be compared against all other types
        - ``boolean`` can only be compared against other booleans
        - ``integer`` can be compared against doubles or a string if the
          string value can be parsed as an integer.
        - ``double`` can be compared against integers or a string if the
          string can be parsed as a double.
        - ``Timestamp`` can be compared against strings in RFC 3339 date
          string format.
        - ``TimeOfDay`` can be compared against timestamps and strings in
          the format of 'HH:mm:ss'.

        If we fail to compare do to type mismatch, a warning will be given
        and the condition will evaluate to false.

        Attributes:
            field (google.cloud.dlp_v2.types.FieldId):
                Required. Field within the record this
                condition is evaluated against.
            operator (google.cloud.dlp_v2.types.RelationalOperator):
                Required. Operator used to compare the field
                or infoType to the value.
            value (google.cloud.dlp_v2.types.Value):
                Value to compare against. [Mandatory, except for ``EXISTS``
                tests.]
        """

        field: storage.FieldId = proto.Field(
            proto.MESSAGE,
            number=1,
            message=storage.FieldId,
        )
        operator: "RelationalOperator" = proto.Field(
            proto.ENUM,
            number=3,
            enum="RelationalOperator",
        )
        value: "Value" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="Value",
        )

    class Conditions(proto.Message):
        r"""A collection of conditions.

        Attributes:
            conditions (MutableSequence[google.cloud.dlp_v2.types.RecordCondition.Condition]):
                A collection of conditions.
        """

        conditions: MutableSequence["RecordCondition.Condition"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="RecordCondition.Condition",
        )

    class Expressions(proto.Message):
        r"""An expression, consisting of an operator and conditions.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            logical_operator (google.cloud.dlp_v2.types.RecordCondition.Expressions.LogicalOperator):
                The operator to apply to the result of conditions. Default
                and currently only supported value is ``AND``.
            conditions (google.cloud.dlp_v2.types.RecordCondition.Conditions):
                Conditions to apply to the expression.

                This field is a member of `oneof`_ ``type``.
        """

        class LogicalOperator(proto.Enum):
            r"""Logical operators for conditional checks.

            Values:
                LOGICAL_OPERATOR_UNSPECIFIED (0):
                    Unused
                AND (1):
                    Conditional AND
            """

            LOGICAL_OPERATOR_UNSPECIFIED = 0
            AND = 1

        logical_operator: "RecordCondition.Expressions.LogicalOperator" = proto.Field(
            proto.ENUM,
            number=1,
            enum="RecordCondition.Expressions.LogicalOperator",
        )
        conditions: "RecordCondition.Conditions" = proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="type",
            message="RecordCondition.Conditions",
        )

    expressions: Expressions = proto.Field(
        proto.MESSAGE,
        number=3,
        message=Expressions,
    )


class TransformationOverview(proto.Message):
    r"""Overview of the modifications that occurred.

    Attributes:
        transformed_bytes (int):
            Total size in bytes that were transformed in
            some way.
        transformation_summaries (MutableSequence[google.cloud.dlp_v2.types.TransformationSummary]):
            Transformations applied to the dataset.
    """

    transformed_bytes: int = proto.Field(
        proto.INT64,
        number=2,
    )
    transformation_summaries: MutableSequence["TransformationSummary"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="TransformationSummary",
        )
    )


class TransformationSummary(proto.Message):
    r"""Summary of a single transformation. Only one of 'transformation',
    'field_transformation', or 'record_suppress' will be set.

    Attributes:
        info_type (google.cloud.dlp_v2.types.InfoType):
            Set if the transformation was limited to a
            specific InfoType.
        field (google.cloud.dlp_v2.types.FieldId):
            Set if the transformation was limited to a
            specific FieldId.
        transformation (google.cloud.dlp_v2.types.PrimitiveTransformation):
            The specific transformation these stats apply
            to.
        field_transformations (MutableSequence[google.cloud.dlp_v2.types.FieldTransformation]):
            The field transformation that was applied.
            If multiple field transformations are requested
            for a single field, this list will contain all
            of them; otherwise, only one is supplied.
        record_suppress (google.cloud.dlp_v2.types.RecordSuppression):
            The specific suppression option these stats
            apply to.
        results (MutableSequence[google.cloud.dlp_v2.types.TransformationSummary.SummaryResult]):
            Collection of all transformations that took
            place or had an error.
        transformed_bytes (int):
            Total size in bytes that were transformed in
            some way.
    """

    class TransformationResultCode(proto.Enum):
        r"""Possible outcomes of transformations.

        Values:
            TRANSFORMATION_RESULT_CODE_UNSPECIFIED (0):
                Unused
            SUCCESS (1):
                Transformation completed without an error.
            ERROR (2):
                Transformation had an error.
        """

        TRANSFORMATION_RESULT_CODE_UNSPECIFIED = 0
        SUCCESS = 1
        ERROR = 2

    class SummaryResult(proto.Message):
        r"""A collection that informs the user the number of times a particular
        ``TransformationResultCode`` and error details occurred.

        Attributes:
            count (int):
                Number of transformations counted by this
                result.
            code (google.cloud.dlp_v2.types.TransformationSummary.TransformationResultCode):
                Outcome of the transformation.
            details (str):
                A place for warnings or errors to show up if
                a transformation didn't work as expected.
        """

        count: int = proto.Field(
            proto.INT64,
            number=1,
        )
        code: "TransformationSummary.TransformationResultCode" = proto.Field(
            proto.ENUM,
            number=2,
            enum="TransformationSummary.TransformationResultCode",
        )
        details: str = proto.Field(
            proto.STRING,
            number=3,
        )

    info_type: storage.InfoType = proto.Field(
        proto.MESSAGE,
        number=1,
        message=storage.InfoType,
    )
    field: storage.FieldId = proto.Field(
        proto.MESSAGE,
        number=2,
        message=storage.FieldId,
    )
    transformation: "PrimitiveTransformation" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="PrimitiveTransformation",
    )
    field_transformations: MutableSequence["FieldTransformation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="FieldTransformation",
    )
    record_suppress: "RecordSuppression" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="RecordSuppression",
    )
    results: MutableSequence[SummaryResult] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=SummaryResult,
    )
    transformed_bytes: int = proto.Field(
        proto.INT64,
        number=7,
    )


class TransformationDescription(proto.Message):
    r"""A flattened description of a ``PrimitiveTransformation`` or
    ``RecordSuppression``.

    Attributes:
        type_ (google.cloud.dlp_v2.types.TransformationType):
            The transformation type.
        description (str):
            A description of the transformation. This is empty for a
            RECORD_SUPPRESSION, or is the output of calling toString()
            on the ``PrimitiveTransformation`` protocol buffer message
            for any other type of transformation.
        condition (str):
            A human-readable string representation of the
            ``RecordCondition`` corresponding to this transformation.
            Set if a ``RecordCondition`` was used to determine whether
            or not to apply this transformation.

            Examples: \* (age_field > 85) \* (age_field <= 18) \*
            (zip_field exists) \* (zip_field == 01234) && (city_field !=
            "Springville") \* (zip_field == 01234) && (age_field <= 18)
            && (city_field exists)
        info_type (google.cloud.dlp_v2.types.InfoType):
            Set if the transformation was limited to a specific
            ``InfoType``.
    """

    type_: "TransformationType" = proto.Field(
        proto.ENUM,
        number=1,
        enum="TransformationType",
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    condition: str = proto.Field(
        proto.STRING,
        number=3,
    )
    info_type: storage.InfoType = proto.Field(
        proto.MESSAGE,
        number=4,
        message=storage.InfoType,
    )


class TransformationDetails(proto.Message):
    r"""Details about a single transformation. This object contains a
    description of the transformation, information about whether the
    transformation was successfully applied, and the precise
    location where the transformation occurred. These details are
    stored in a user-specified BigQuery table.

    Attributes:
        resource_name (str):
            The name of the job that completed the
            transformation.
        container_name (str):
            The top level name of the container where the
            transformation is located (this will be the
            source file name or table name).
        transformation (MutableSequence[google.cloud.dlp_v2.types.TransformationDescription]):
            Description of transformation. This would only contain more
            than one element if there were multiple matching
            transformations and which one to apply was ambiguous. Not
            set for states that contain no transformation, currently
            only state that contains no transformation is
            TransformationResultStateType.METADATA_UNRETRIEVABLE.
        status_details (google.cloud.dlp_v2.types.TransformationResultStatus):
            Status of the transformation, if
            transformation was not successful, this will
            specify what caused it to fail, otherwise it
            will show that the transformation was
            successful.
        transformed_bytes (int):
            The number of bytes that were transformed. If
            transformation was unsuccessful or did not take
            place because there was no content to transform,
            this will be zero.
        transformation_location (google.cloud.dlp_v2.types.TransformationLocation):
            The precise location of the transformed
            content in the original container.
    """

    resource_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    container_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    transformation: MutableSequence["TransformationDescription"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="TransformationDescription",
    )
    status_details: "TransformationResultStatus" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="TransformationResultStatus",
    )
    transformed_bytes: int = proto.Field(
        proto.INT64,
        number=5,
    )
    transformation_location: "TransformationLocation" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="TransformationLocation",
    )


class TransformationLocation(proto.Message):
    r"""Specifies the location of a transformation.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        finding_id (str):
            For infotype transformations, link to the
            corresponding findings ID so that location
            information does not need to be duplicated. Each
            findings ID correlates to an entry in the
            findings output table, this table only gets
            created when users specify to save findings (add
            the save findings action to the request).

            This field is a member of `oneof`_ ``location_type``.
        record_transformation (google.cloud.dlp_v2.types.RecordTransformation):
            For record transformations, provide a field
            and container information.

            This field is a member of `oneof`_ ``location_type``.
        container_type (google.cloud.dlp_v2.types.TransformationContainerType):
            Information about the functionality of the
            container where this finding occurred, if
            available.
    """

    finding_id: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="location_type",
    )
    record_transformation: "RecordTransformation" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="location_type",
        message="RecordTransformation",
    )
    container_type: "TransformationContainerType" = proto.Field(
        proto.ENUM,
        number=3,
        enum="TransformationContainerType",
    )


class RecordTransformation(proto.Message):
    r"""The field in a record to transform.

    Attributes:
        field_id (google.cloud.dlp_v2.types.FieldId):
            For record transformations, provide a field.
        container_timestamp (google.protobuf.timestamp_pb2.Timestamp):
            Findings container modification timestamp, if
            applicable.
        container_version (str):
            Container version, if available ("generation"
            for Cloud Storage).
    """

    field_id: storage.FieldId = proto.Field(
        proto.MESSAGE,
        number=1,
        message=storage.FieldId,
    )
    container_timestamp: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    container_version: str = proto.Field(
        proto.STRING,
        number=3,
    )


class TransformationResultStatus(proto.Message):
    r"""The outcome of a transformation.

    Attributes:
        result_status_type (google.cloud.dlp_v2.types.TransformationResultStatusType):
            Transformation result status type, this will
            be either SUCCESS, or it will be the reason for
            why the transformation was not completely
            successful.
        details (google.rpc.status_pb2.Status):
            Detailed error codes and messages
    """

    result_status_type: "TransformationResultStatusType" = proto.Field(
        proto.ENUM,
        number=1,
        enum="TransformationResultStatusType",
    )
    details: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=2,
        message=status_pb2.Status,
    )


class TransformationDetailsStorageConfig(proto.Message):
    r"""Config for storing transformation details.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        table (google.cloud.dlp_v2.types.BigQueryTable):
            The BigQuery table in which to store the output. This may be
            an existing table or in a new table in an existing dataset.
            If table_id is not set a new one will be generated for you
            with the following format:
            dlp_googleapis_transformation_details_yyyy_mm_dd\_[dlp_job_id].
            Pacific time zone will be used for generating the date
            details.

            This field is a member of `oneof`_ ``type``.
    """

    table: storage.BigQueryTable = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="type",
        message=storage.BigQueryTable,
    )


class Schedule(proto.Message):
    r"""Schedule for inspect job triggers.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        recurrence_period_duration (google.protobuf.duration_pb2.Duration):
            With this option a job is started on a
            regular periodic basis. For example: every day
            (86400 seconds).

            A scheduled start time will be skipped if the
            previous execution has not ended when its
            scheduled time occurs.

            This value must be set to a time duration
            greater than or equal to 1 day and can be no
            longer than 60 days.

            This field is a member of `oneof`_ ``option``.
    """

    recurrence_period_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="option",
        message=duration_pb2.Duration,
    )


class Manual(proto.Message):
    r"""Job trigger option for hybrid jobs. Jobs must be manually
    created and finished.

    """


class InspectTemplate(proto.Message):
    r"""The inspectTemplate contains a configuration (set of types of
    sensitive data to be detected) to be used anywhere you otherwise
    would normally specify InspectConfig. See
    https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-templates
    to learn more.

    Attributes:
        name (str):
            Output only. The template name.

            The template will have one of the following formats:
            ``projects/PROJECT_ID/inspectTemplates/TEMPLATE_ID`` OR
            ``organizations/ORGANIZATION_ID/inspectTemplates/TEMPLATE_ID``;
        display_name (str):
            Display name (max 256 chars).
        description (str):
            Short description (max 256 chars).
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation timestamp of an
            inspectTemplate.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last update timestamp of an
            inspectTemplate.
        inspect_config (google.cloud.dlp_v2.types.InspectConfig):
            The core content of the template.
            Configuration of the scanning process.
        allow_limited_availability_info_types (bool):
            Optional. Enables the use of `limited-availability built-in
            infoTypes <https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference#limited-availability-infotypes>`__
            in inspect_config. These infoTypes are supported only in
            specific regions and can cause scanning errors if used
            elsewhere.
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
    inspect_config: "InspectConfig" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="InspectConfig",
    )
    allow_limited_availability_info_types: bool = proto.Field(
        proto.BOOL,
        number=8,
    )


class DeidentifyTemplate(proto.Message):
    r"""DeidentifyTemplates contains instructions on how to
    de-identify content. See
    https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-templates
    to learn more.

    Attributes:
        name (str):
            Output only. The template name.

            The template will have one of the following formats:
            ``projects/PROJECT_ID/deidentifyTemplates/TEMPLATE_ID`` OR
            ``organizations/ORGANIZATION_ID/deidentifyTemplates/TEMPLATE_ID``
        display_name (str):
            Display name (max 256 chars).
        description (str):
            Short description (max 256 chars).
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation timestamp of an
            inspectTemplate.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last update timestamp of an
            inspectTemplate.
        deidentify_config (google.cloud.dlp_v2.types.DeidentifyConfig):
            The core content of the template.
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
    deidentify_config: "DeidentifyConfig" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="DeidentifyConfig",
    )


class Error(proto.Message):
    r"""Details information about an error encountered during job
    execution or the results of an unsuccessful activation of the
    JobTrigger.

    Attributes:
        details (google.rpc.status_pb2.Status):
            Detailed error codes and messages.
        timestamps (MutableSequence[google.protobuf.timestamp_pb2.Timestamp]):
            The times the error occurred. List includes
            the oldest timestamp and the last 9 timestamps.
        extra_info (google.cloud.dlp_v2.types.Error.ErrorExtraInfo):
            Additional information about the error.
    """

    class ErrorExtraInfo(proto.Enum):
        r"""Additional information about the error.

        Values:
            ERROR_INFO_UNSPECIFIED (0):
                Unused.
            IMAGE_SCAN_UNAVAILABLE_IN_REGION (1):
                Image scan is not available in the region.
            FILE_STORE_CLUSTER_UNSUPPORTED (2):
                File store cluster is not supported for
                profile generation.
        """

        ERROR_INFO_UNSPECIFIED = 0
        IMAGE_SCAN_UNAVAILABLE_IN_REGION = 1
        FILE_STORE_CLUSTER_UNSUPPORTED = 2

    details: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=1,
        message=status_pb2.Status,
    )
    timestamps: MutableSequence[timestamp_pb2.Timestamp] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    extra_info: ErrorExtraInfo = proto.Field(
        proto.ENUM,
        number=4,
        enum=ErrorExtraInfo,
    )


class JobTrigger(proto.Message):
    r"""Contains a configuration to make API calls on a repeating
    basis. See
    https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-job-triggers
    to learn more.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. Unique resource name for the triggeredJob,
            assigned by the service when the triggeredJob is created,
            for example
            ``projects/dlp-test-project/jobTriggers/53234423``.
        display_name (str):
            Display name (max 100 chars)
        description (str):
            User provided description (max 256 chars)
        inspect_job (google.cloud.dlp_v2.types.InspectJobConfig):
            For inspect jobs, a snapshot of the
            configuration.

            This field is a member of `oneof`_ ``job``.
        triggers (MutableSequence[google.cloud.dlp_v2.types.JobTrigger.Trigger]):
            A list of triggers which will be OR'ed
            together. Only one in the list needs to trigger
            for a job to be started. The list may contain
            only a single Schedule trigger and must have at
            least one object.
        errors (MutableSequence[google.cloud.dlp_v2.types.Error]):
            Output only. A stream of errors encountered
            when the trigger was activated. Repeated errors
            may result in the JobTrigger automatically being
            paused. Will return the last 100 errors.
            Whenever the JobTrigger is modified this list
            will be cleared.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation timestamp of a
            triggeredJob.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last update timestamp of a
            triggeredJob.
        last_run_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp of the last time
            this trigger executed.
        status (google.cloud.dlp_v2.types.JobTrigger.Status):
            Required. A status for this trigger.
    """

    class Status(proto.Enum):
        r"""Whether the trigger is currently active. If PAUSED or
        CANCELLED, no jobs will be created with this configuration. The
        service may automatically pause triggers experiencing frequent
        errors. To restart a job, set the status to HEALTHY after
        correcting user errors.

        Values:
            STATUS_UNSPECIFIED (0):
                Unused.
            HEALTHY (1):
                Trigger is healthy.
            PAUSED (2):
                Trigger is temporarily paused.
            CANCELLED (3):
                Trigger is cancelled and can not be resumed.
        """

        STATUS_UNSPECIFIED = 0
        HEALTHY = 1
        PAUSED = 2
        CANCELLED = 3

    class Trigger(proto.Message):
        r"""What event needs to occur for a new job to be started.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            schedule (google.cloud.dlp_v2.types.Schedule):
                Create a job on a repeating basis based on
                the elapse of time.

                This field is a member of `oneof`_ ``trigger``.
            manual (google.cloud.dlp_v2.types.Manual):
                For use with hybrid jobs. Jobs must be
                manually created and finished.

                This field is a member of `oneof`_ ``trigger``.
        """

        schedule: "Schedule" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="trigger",
            message="Schedule",
        )
        manual: "Manual" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="trigger",
            message="Manual",
        )

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
    inspect_job: "InspectJobConfig" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="job",
        message="InspectJobConfig",
    )
    triggers: MutableSequence[Trigger] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=Trigger,
    )
    errors: MutableSequence["Error"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="Error",
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
    last_run_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    status: Status = proto.Field(
        proto.ENUM,
        number=10,
        enum=Status,
    )


class Action(proto.Message):
    r"""A task to execute on the completion of a job.
    See
    https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-actions
    to learn more.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        save_findings (google.cloud.dlp_v2.types.Action.SaveFindings):
            Save resulting findings in a provided
            location.

            This field is a member of `oneof`_ ``action``.
        pub_sub (google.cloud.dlp_v2.types.Action.PublishToPubSub):
            Publish a notification to a Pub/Sub topic.

            This field is a member of `oneof`_ ``action``.
        publish_summary_to_cscc (google.cloud.dlp_v2.types.Action.PublishSummaryToCscc):
            Publish summary to Cloud Security Command
            Center (Alpha).

            This field is a member of `oneof`_ ``action``.
        publish_findings_to_cloud_data_catalog (google.cloud.dlp_v2.types.Action.PublishFindingsToCloudDataCatalog):
            Deprecated because Data Catalog is being turned down. Use
            publish_findings_to_dataplex_catalog to publish findings to
            Dataplex Universal Catalog.

            This field is a member of `oneof`_ ``action``.
        publish_findings_to_dataplex_catalog (google.cloud.dlp_v2.types.Action.PublishFindingsToDataplexCatalog):
            Publish findings as an aspect to Dataplex
            Universal Catalog.

            This field is a member of `oneof`_ ``action``.
        deidentify (google.cloud.dlp_v2.types.Action.Deidentify):
            Create a de-identified copy of the input
            data.

            This field is a member of `oneof`_ ``action``.
        job_notification_emails (google.cloud.dlp_v2.types.Action.JobNotificationEmails):
            Sends an email when the job completes. The email goes to IAM
            project owners and technical `Essential
            Contacts <https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts>`__.

            This field is a member of `oneof`_ ``action``.
        publish_to_stackdriver (google.cloud.dlp_v2.types.Action.PublishToStackdriver):
            Enable Stackdriver metric dlp.googleapis.com/finding_count.

            This field is a member of `oneof`_ ``action``.
    """

    class SaveFindings(proto.Message):
        r"""If set, the detailed findings will be persisted to the
        specified OutputStorageConfig. Only a single instance of this
        action can be specified.
        Compatible with: Inspect, Risk

        Attributes:
            output_config (google.cloud.dlp_v2.types.OutputStorageConfig):
                Location to store findings outside of DLP.
        """

        output_config: "OutputStorageConfig" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="OutputStorageConfig",
        )

    class PublishToPubSub(proto.Message):
        r"""Publish a message into a given Pub/Sub topic when DlpJob has
        completed. The message contains a single field, ``DlpJobName``,
        which is equal to the finished job's
        ```DlpJob.name`` <https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs#DlpJob>`__.
        Compatible with: Inspect, Risk

        Attributes:
            topic (str):
                Cloud Pub/Sub topic to send notifications to.
                The topic must have given publishing access
                rights to the DLP API service account executing
                the long running DlpJob sending the
                notifications. Format is
                projects/{project}/topics/{topic}.
        """

        topic: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class PublishSummaryToCscc(proto.Message):
        r"""Publish the result summary of a DlpJob to `Security Command
        Center <https://cloud.google.com/security-command-center>`__. This
        action is available for only projects that belong to an
        organization. This action publishes the count of finding instances
        and their infoTypes. The summary of findings are persisted in
        Security Command Center and are governed by `service-specific
        policies for Security Command
        Center <https://cloud.google.com/terms/service-terms>`__. Only a
        single instance of this action can be specified. Compatible with:
        Inspect

        """

    class PublishFindingsToCloudDataCatalog(proto.Message):
        r"""Publish findings of a DlpJob to Data Catalog. In Data Catalog, tag
        templates are applied to the resource that Cloud DLP scanned. Data
        Catalog tag templates are stored in the same project and region
        where the BigQuery table exists. For Cloud DLP to create and apply
        the tag template, the Cloud DLP service agent must have the
        ``roles/datacatalog.tagTemplateOwner`` permission on the project.
        The tag template contains fields summarizing the results of the
        DlpJob. Any field values previously written by another DlpJob are
        deleted. [InfoType naming patterns][google.privacy.dlp.v2.InfoType]
        are strictly enforced when using this feature.

        Findings are persisted in Data Catalog storage and are governed by
        service-specific policies for Data Catalog. For more information,
        see `Service Specific
        Terms <https://cloud.google.com/terms/service-terms>`__.

        Only a single instance of this action can be specified. This action
        is allowed only if all resources being scanned are BigQuery tables.
        Compatible with: Inspect

        """

    class PublishFindingsToDataplexCatalog(proto.Message):
        r"""Publish findings of a DlpJob to Dataplex Universal Catalog as a
        ``sensitive-data-protection-job-result`` aspect. For more
        information, see `Send inspection results to Dataplex Universal
        Catalog as
        aspects <https://docs.cloud.google.com/sensitive-data-protection/docs/add-aspects-inspection-job>`__.

        Aspects are stored in Dataplex Universal Catalog storage and are
        governed by service-specific policies for Dataplex Universal
        Catalog. For more information, see `Service Specific
        Terms <https://cloud.google.com/terms/service-terms>`__.

        Only a single instance of this action can be specified. This action
        is allowed only if all resources being scanned are BigQuery tables.
        Compatible with: Inspect

        """

    class Deidentify(proto.Message):
        r"""Create a de-identified copy of a storage bucket. Only
        compatible with Cloud Storage buckets.

        A TransformationDetail will be created for each transformation.

        Compatible with: Inspection of Cloud Storage


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            transformation_config (google.cloud.dlp_v2.types.TransformationConfig):
                User specified deidentify templates and
                configs for structured, unstructured, and image
                files.
            transformation_details_storage_config (google.cloud.dlp_v2.types.TransformationDetailsStorageConfig):
                Config for storing transformation details.

                This field specifies the configuration for storing detailed
                metadata about each transformation performed during a
                de-identification process. The metadata is stored separately
                from the de-identified content itself and provides a
                granular record of both successful transformations and any
                failures that occurred.

                Enabling this configuration is essential for users who need
                to access comprehensive information about the status,
                outcome, and specifics of each transformation. The details
                are captured in the
                [TransformationDetails][google.privacy.dlp.v2.TransformationDetails]
                message for each operation.

                Key use cases:

                - **Auditing and compliance**

                  - Provides a verifiable audit trail of de-identification
                    activities, which is crucial for meeting regulatory
                    requirements and internal data governance policies.
                  - Logs what data was transformed, what transformations
                    were applied, when they occurred, and their success
                    status. This helps demonstrate accountability and due
                    diligence in protecting sensitive data.

                - **Troubleshooting and debugging**

                  - Offers detailed error messages and context if a
                    transformation fails. This information is useful for
                    diagnosing and resolving issues in the de-identification
                    pipeline.
                  - Helps pinpoint the exact location and nature of
                    failures, speeding up the debugging process.

                - **Process verification and quality assurance**

                  - Allows users to confirm that de-identification rules and
                    transformations were applied correctly and consistently
                    across the dataset as intended.
                  - Helps in verifying the effectiveness of the chosen
                    de-identification strategies.

                - **Data lineage and impact analysis**

                  - Creates a record of how data elements were modified,
                    contributing to data lineage. This is useful for
                    understanding the provenance of de-identified data.
                  - Aids in assessing the potential impact of
                    de-identification choices on downstream analytical
                    processes or data usability.

                - **Reporting and operational insights**

                  - You can analyze the metadata stored in a queryable
                    BigQuery table to generate reports on transformation
                    success rates, common error types, processing volumes
                    (e.g., transformedBytes), and the types of
                    transformations applied.
                  - These insights can inform optimization of
                    de-identification configurations and resource planning.

                To take advantage of these benefits, set this configuration.
                The stored details include a description of the
                transformation, success or error codes, error messages, the
                number of bytes transformed, the location of the transformed
                content, and identifiers for the job and source data.
            cloud_storage_output (str):
                Required. User settable Cloud Storage bucket
                and folders to store de-identified files. This
                field must be set for Cloud Storage
                deidentification. The output Cloud Storage
                bucket must be different from the input bucket.
                De-identified files will overwrite files in the
                output path.

                Form of: gs://bucket/folder/ or gs://bucket

                This field is a member of `oneof`_ ``output``.
            file_types_to_transform (MutableSequence[google.cloud.dlp_v2.types.FileType]):
                List of user-specified file type groups to transform. If
                specified, only the files with these file types are
                transformed. If empty, all supported files are transformed.
                Supported types may be automatically added over time. Any
                unsupported file types that are set in this field are
                excluded from de-identification. An error is recorded for
                each unsupported file in the TransformationDetails output
                table. Currently the only file types supported are: IMAGES,
                TEXT_FILES, CSV, TSV.
        """

        transformation_config: "TransformationConfig" = proto.Field(
            proto.MESSAGE,
            number=7,
            message="TransformationConfig",
        )
        transformation_details_storage_config: "TransformationDetailsStorageConfig" = (
            proto.Field(
                proto.MESSAGE,
                number=3,
                message="TransformationDetailsStorageConfig",
            )
        )
        cloud_storage_output: str = proto.Field(
            proto.STRING,
            number=9,
            oneof="output",
        )
        file_types_to_transform: MutableSequence[storage.FileType] = (
            proto.RepeatedField(
                proto.ENUM,
                number=8,
                enum=storage.FileType,
            )
        )

    class JobNotificationEmails(proto.Message):
        r"""Sends an email when the job completes. The email goes to IAM project
        owners and technical `Essential
        Contacts <https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts>`__.

        """

    class PublishToStackdriver(proto.Message):
        r"""Enable Stackdriver metric dlp.googleapis.com/finding_count. This
        will publish a metric to stack driver on each infotype requested and
        how many findings were found for it. CustomDetectors will be
        bucketed as 'Custom' under the Stackdriver label 'info_type'.

        """

    save_findings: SaveFindings = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="action",
        message=SaveFindings,
    )
    pub_sub: PublishToPubSub = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="action",
        message=PublishToPubSub,
    )
    publish_summary_to_cscc: PublishSummaryToCscc = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="action",
        message=PublishSummaryToCscc,
    )
    publish_findings_to_cloud_data_catalog: PublishFindingsToCloudDataCatalog = (
        proto.Field(
            proto.MESSAGE,
            number=5,
            oneof="action",
            message=PublishFindingsToCloudDataCatalog,
        )
    )
    publish_findings_to_dataplex_catalog: PublishFindingsToDataplexCatalog = (
        proto.Field(
            proto.MESSAGE,
            number=10,
            oneof="action",
            message=PublishFindingsToDataplexCatalog,
        )
    )
    deidentify: Deidentify = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="action",
        message=Deidentify,
    )
    job_notification_emails: JobNotificationEmails = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="action",
        message=JobNotificationEmails,
    )
    publish_to_stackdriver: PublishToStackdriver = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="action",
        message=PublishToStackdriver,
    )


class TransformationConfig(proto.Message):
    r"""User specified templates and configs for how to deidentify
    structured, unstructures, and image files. User must provide
    either a unstructured deidentify template or at least one redact
    image config.

    Attributes:
        deidentify_template (str):
            De-identify template. If this template is specified, it will
            serve as the default de-identify template. This template
            cannot contain ``record_transformations`` since it can be
            used for unstructured content such as free-form text files.
            If this template is not set, a default
            ``ReplaceWithInfoTypeConfig`` will be used to de-identify
            unstructured content.
        structured_deidentify_template (str):
            Structured de-identify template. If this template is
            specified, it will serve as the de-identify template for
            structured content such as delimited files and tables. If
            this template is not set but the ``deidentify_template`` is
            set, then ``deidentify_template`` will also apply to the
            structured content. If neither template is set, a default
            ``ReplaceWithInfoTypeConfig`` will be used to de-identify
            structured content.
        image_redact_template (str):
            Image redact template.
            If this template is specified, it will serve as
            the de-identify template for images. If this
            template is not set, all findings in the image
            will be redacted with a black box.
    """

    deidentify_template: str = proto.Field(
        proto.STRING,
        number=1,
    )
    structured_deidentify_template: str = proto.Field(
        proto.STRING,
        number=2,
    )
    image_redact_template: str = proto.Field(
        proto.STRING,
        number=4,
    )


class CreateInspectTemplateRequest(proto.Message):
    r"""Request message for CreateInspectTemplate.

    Attributes:
        parent (str):
            Required. Parent resource name.

            The format of this value varies depending on the scope of
            the request (project or organization) and whether you have
            `specified a processing
            location <https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location>`__:

            - Projects scope, location specified:
              ``projects/{project_id}/locations/{location_id}``
            - Projects scope, no location specified (defaults to
              global): ``projects/{project_id}``
            - Organizations scope, location specified:
              ``organizations/{org_id}/locations/{location_id}``
            - Organizations scope, no location specified (defaults to
              global): ``organizations/{org_id}``

            The following example ``parent`` string specifies a parent
            project with the identifier ``example-project``, and
            specifies the ``europe-west3`` location for processing data:

            ::

                parent=projects/example-project/locations/europe-west3
        inspect_template (google.cloud.dlp_v2.types.InspectTemplate):
            Required. The InspectTemplate to create.
        template_id (str):
            The template id can contain uppercase and lowercase letters,
            numbers, and hyphens; that is, it must match the regular
            expression: ``[a-zA-Z\d-_]+``. The maximum length is 100
            characters. Can be empty to allow the system to generate
            one.
        location_id (str):
            Deprecated. This field has no effect.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    inspect_template: "InspectTemplate" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="InspectTemplate",
    )
    template_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    location_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateInspectTemplateRequest(proto.Message):
    r"""Request message for UpdateInspectTemplate.

    Attributes:
        name (str):
            Required. Resource name of organization and inspectTemplate
            to be updated, for example
            ``organizations/433245324/inspectTemplates/432452342`` or
            projects/project-id/inspectTemplates/432452342.
        inspect_template (google.cloud.dlp_v2.types.InspectTemplate):
            New InspectTemplate value.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Mask to control which fields get updated.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    inspect_template: "InspectTemplate" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="InspectTemplate",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


class GetInspectTemplateRequest(proto.Message):
    r"""Request message for GetInspectTemplate.

    Attributes:
        name (str):
            Required. Resource name of the organization and
            inspectTemplate to be read, for example
            ``organizations/433245324/inspectTemplates/432452342`` or
            projects/project-id/inspectTemplates/432452342.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListInspectTemplatesRequest(proto.Message):
    r"""Request message for ListInspectTemplates.

    Attributes:
        parent (str):
            Required. Parent resource name.

            The format of this value varies depending on the scope of
            the request (project or organization) and whether you have
            `specified a processing
            location <https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location>`__:

            - Projects scope, location specified:
              ``projects/{project_id}/locations/{location_id}``
            - Projects scope, no location specified (defaults to
              global): ``projects/{project_id}``
            - Organizations scope, location specified:
              ``organizations/{org_id}/locations/{location_id}``
            - Organizations scope, no location specified (defaults to
              global): ``organizations/{org_id}``

            The following example ``parent`` string specifies a parent
            project with the identifier ``example-project``, and
            specifies the ``europe-west3`` location for processing data:

            ::

                parent=projects/example-project/locations/europe-west3
        page_token (str):
            Page token to continue retrieval. Comes from the previous
            call to ``ListInspectTemplates``.
        page_size (int):
            Size of the page. This value can be limited
            by the server. If zero server returns a page of
            max size 100.
        order_by (str):
            Comma-separated list of fields to order by, followed by
            ``asc`` or ``desc`` postfix. This list is case insensitive.
            The default sorting order is ascending. Redundant space
            characters are insignificant.

            Example: ``name asc,update_time, create_time desc``

            Supported fields are:

            - ``create_time``: corresponds to the time the template was
              created.
            - ``update_time``: corresponds to the time the template was
              last updated.
            - ``name``: corresponds to the template's name.
            - ``display_name``: corresponds to the template's display
              name.
        location_id (str):
            Deprecated. This field has no effect.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=4,
    )
    location_id: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListInspectTemplatesResponse(proto.Message):
    r"""Response message for ListInspectTemplates.

    Attributes:
        inspect_templates (MutableSequence[google.cloud.dlp_v2.types.InspectTemplate]):
            List of inspectTemplates, up to page_size in
            ListInspectTemplatesRequest.
        next_page_token (str):
            If the next page is available then the next
            page token to be used in the following
            ListInspectTemplates request.
    """

    @property
    def raw_page(self):
        return self

    inspect_templates: MutableSequence["InspectTemplate"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="InspectTemplate",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteInspectTemplateRequest(proto.Message):
    r"""Request message for DeleteInspectTemplate.

    Attributes:
        name (str):
            Required. Resource name of the organization and
            inspectTemplate to be deleted, for example
            ``organizations/433245324/inspectTemplates/432452342`` or
            projects/project-id/inspectTemplates/432452342.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateJobTriggerRequest(proto.Message):
    r"""Request message for CreateJobTrigger.

    Attributes:
        parent (str):
            Required. Parent resource name.

            The format of this value varies depending on whether you
            have `specified a processing
            location <https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location>`__:

            - Projects scope, location specified:
              ``projects/{project_id}/locations/{location_id}``
            - Projects scope, no location specified (defaults to
              global): ``projects/{project_id}``

            The following example ``parent`` string specifies a parent
            project with the identifier ``example-project``, and
            specifies the ``europe-west3`` location for processing data:

            ::

                parent=projects/example-project/locations/europe-west3
        job_trigger (google.cloud.dlp_v2.types.JobTrigger):
            Required. The JobTrigger to create.
        trigger_id (str):
            The trigger id can contain uppercase and lowercase letters,
            numbers, and hyphens; that is, it must match the regular
            expression: ``[a-zA-Z\d-_]+``. The maximum length is 100
            characters. Can be empty to allow the system to generate
            one.
        location_id (str):
            Deprecated. This field has no effect.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    job_trigger: "JobTrigger" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="JobTrigger",
    )
    trigger_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    location_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ActivateJobTriggerRequest(proto.Message):
    r"""Request message for ActivateJobTrigger.

    Attributes:
        name (str):
            Required. Resource name of the trigger to activate, for
            example ``projects/dlp-test-project/jobTriggers/53234423``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateJobTriggerRequest(proto.Message):
    r"""Request message for UpdateJobTrigger.

    Attributes:
        name (str):
            Required. Resource name of the project and the triggeredJob,
            for example
            ``projects/dlp-test-project/jobTriggers/53234423``.
        job_trigger (google.cloud.dlp_v2.types.JobTrigger):
            New JobTrigger value.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Mask to control which fields get updated.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    job_trigger: "JobTrigger" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="JobTrigger",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


class GetJobTriggerRequest(proto.Message):
    r"""Request message for GetJobTrigger.

    Attributes:
        name (str):
            Required. Resource name of the project and the triggeredJob,
            for example
            ``projects/dlp-test-project/jobTriggers/53234423``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateDiscoveryConfigRequest(proto.Message):
    r"""Request message for CreateDiscoveryConfig.

    Attributes:
        parent (str):
            Required. Parent resource name.

            The format of this value varies depending on the scope of
            the request (project or organization):

            - Projects scope:
              ``projects/{project_id}/locations/{location_id}``
            - Organizations scope:
              ``organizations/{org_id}/locations/{location_id}``

            The following example ``parent`` string specifies a parent
            project with the identifier ``example-project``, and
            specifies the ``europe-west3`` location for processing data:

            ::

                parent=projects/example-project/locations/europe-west3
        discovery_config (google.cloud.dlp_v2.types.DiscoveryConfig):
            Required. The DiscoveryConfig to create.
        config_id (str):
            The config ID can contain uppercase and lowercase letters,
            numbers, and hyphens; that is, it must match the regular
            expression: ``[a-zA-Z\d-_]+``. The maximum length is 100
            characters. Can be empty to allow the system to generate
            one.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    discovery_config: "DiscoveryConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DiscoveryConfig",
    )
    config_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateDiscoveryConfigRequest(proto.Message):
    r"""Request message for UpdateDiscoveryConfig.

    Attributes:
        name (str):
            Required. Resource name of the project and the
            configuration, for example
            ``projects/dlp-test-project/discoveryConfigs/53234423``.
        discovery_config (google.cloud.dlp_v2.types.DiscoveryConfig):
            Required. New DiscoveryConfig value.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Mask to control which fields get updated.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    discovery_config: "DiscoveryConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DiscoveryConfig",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


class GetDiscoveryConfigRequest(proto.Message):
    r"""Request message for GetDiscoveryConfig.

    Attributes:
        name (str):
            Required. Resource name of the project and the
            configuration, for example
            ``projects/dlp-test-project/discoveryConfigs/53234423``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDiscoveryConfigsRequest(proto.Message):
    r"""Request message for ListDiscoveryConfigs.

    Attributes:
        parent (str):
            Required. Parent resource name.

            The format of this value is as follows:
            ``projects/{project_id}/locations/{location_id}``

            The following example ``parent`` string specifies a parent
            project with the identifier ``example-project``, and
            specifies the ``europe-west3`` location for processing data:

            ::

                parent=projects/example-project/locations/europe-west3
        page_token (str):
            Page token to continue retrieval. Comes from the previous
            call to ListDiscoveryConfigs. ``order_by`` field must not
            change for subsequent calls.
        page_size (int):
            Size of the page. This value can be limited
            by a server.
        order_by (str):
            Comma-separated list of config fields to order by, followed
            by ``asc`` or ``desc`` postfix. This list is case
            insensitive. The default sorting order is ascending.
            Redundant space characters are insignificant.

            Example: ``name asc,update_time, create_time desc``

            Supported fields are:

            - ``last_run_time``: corresponds to the last time the
              DiscoveryConfig ran.
            - ``name``: corresponds to the DiscoveryConfig's name.
            - ``status``: corresponds to DiscoveryConfig's status.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListDiscoveryConfigsResponse(proto.Message):
    r"""Response message for ListDiscoveryConfigs.

    Attributes:
        discovery_configs (MutableSequence[google.cloud.dlp_v2.types.DiscoveryConfig]):
            List of configs, up to page_size in
            ListDiscoveryConfigsRequest.
        next_page_token (str):
            If the next page is available then this value
            is the next page token to be used in the
            following ListDiscoveryConfigs request.
    """

    @property
    def raw_page(self):
        return self

    discovery_configs: MutableSequence["DiscoveryConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DiscoveryConfig",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteDiscoveryConfigRequest(proto.Message):
    r"""Request message for DeleteDiscoveryConfig.

    Attributes:
        name (str):
            Required. Resource name of the project and the config, for
            example
            ``projects/dlp-test-project/discoveryConfigs/53234423``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateDlpJobRequest(proto.Message):
    r"""Request message for CreateDlpJobRequest. Used to initiate
    long running jobs such as calculating risk metrics or inspecting
    Google Cloud Storage.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. Parent resource name.

            The format of this value varies depending on whether you
            have `specified a processing
            location <https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location>`__:

            - Projects scope, location specified:
              ``projects/{project_id}/locations/{location_id}``
            - Projects scope, no location specified (defaults to
              global): ``projects/{project_id}``

            The following example ``parent`` string specifies a parent
            project with the identifier ``example-project``, and
            specifies the ``europe-west3`` location for processing data:

            ::

                parent=projects/example-project/locations/europe-west3
        inspect_job (google.cloud.dlp_v2.types.InspectJobConfig):
            An inspection job scans a storage repository
            for InfoTypes.

            This field is a member of `oneof`_ ``job``.
        risk_job (google.cloud.dlp_v2.types.RiskAnalysisJobConfig):
            A risk analysis job calculates
            re-identification risk metrics for a BigQuery
            table.

            This field is a member of `oneof`_ ``job``.
        job_id (str):
            The job id can contain uppercase and lowercase letters,
            numbers, and hyphens; that is, it must match the regular
            expression: ``[a-zA-Z\d-_]+``. The maximum length is 100
            characters. Can be empty to allow the system to generate
            one.
        location_id (str):
            Deprecated. This field has no effect.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    inspect_job: "InspectJobConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="job",
        message="InspectJobConfig",
    )
    risk_job: "RiskAnalysisJobConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="job",
        message="RiskAnalysisJobConfig",
    )
    job_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    location_id: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListJobTriggersRequest(proto.Message):
    r"""Request message for ListJobTriggers.

    Attributes:
        parent (str):
            Required. Parent resource name.

            The format of this value varies depending on whether you
            have `specified a processing
            location <https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location>`__:

            - Projects scope, location specified:
              ``projects/{project_id}/locations/{location_id}``
            - Projects scope, no location specified (defaults to
              global): ``projects/{project_id}``

            The following example ``parent`` string specifies a parent
            project with the identifier ``example-project``, and
            specifies the ``europe-west3`` location for processing data:

            ::

                parent=projects/example-project/locations/europe-west3
        page_token (str):
            Page token to continue retrieval. Comes from the previous
            call to ListJobTriggers. ``order_by`` field must not change
            for subsequent calls.
        page_size (int):
            Size of the page. This value can be limited
            by a server.
        order_by (str):
            Comma-separated list of triggeredJob fields to order by,
            followed by ``asc`` or ``desc`` postfix. This list is case
            insensitive. The default sorting order is ascending.
            Redundant space characters are insignificant.

            Example: ``name asc,update_time, create_time desc``

            Supported fields are:

            - ``create_time``: corresponds to the time the JobTrigger
              was created.
            - ``update_time``: corresponds to the time the JobTrigger
              was last updated.
            - ``last_run_time``: corresponds to the last time the
              JobTrigger ran.
            - ``name``: corresponds to the JobTrigger's name.
            - ``display_name``: corresponds to the JobTrigger's display
              name.
            - ``status``: corresponds to JobTrigger's status.
        filter (str):
            Allows filtering.

            Supported syntax:

            - Filter expressions are made up of one or more
              restrictions.
            - Restrictions can be combined by ``AND`` or ``OR`` logical
              operators. A sequence of restrictions implicitly uses
              ``AND``.
            - A restriction has the form of
              ``{field} {operator} {value}``.
            - Supported fields/values for inspect triggers:

              - ``status`` - HEALTHY|PAUSED|CANCELLED
              - ``inspected_storage`` - DATASTORE|CLOUD_STORAGE|BIGQUERY
              - 'last_run_time\` - RFC 3339 formatted timestamp,
                surrounded by quotation marks. Nanoseconds are ignored.
              - 'error_count' - Number of errors that have occurred
                while running.

            - The operator must be ``=`` or ``!=`` for status and
              inspected_storage.

            The syntax is based on https://google.aip.dev/160.

            Examples:

            - inspected_storage = cloud_storage AND status = HEALTHY
            - inspected_storage = cloud_storage OR inspected_storage =
              bigquery
            - inspected_storage = cloud_storage AND (state = PAUSED OR
              state = HEALTHY)
            - last_run_time > "2017-12-12T00:00:00+00:00"

            The length of this field should be no more than 500
            characters.
        type_ (google.cloud.dlp_v2.types.DlpJobType):
            The type of jobs. Will use ``DlpJobType.INSPECT`` if not
            set.
        location_id (str):
            Deprecated. This field has no effect.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=4,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )
    type_: "DlpJobType" = proto.Field(
        proto.ENUM,
        number=6,
        enum="DlpJobType",
    )
    location_id: str = proto.Field(
        proto.STRING,
        number=7,
    )


class ListJobTriggersResponse(proto.Message):
    r"""Response message for ListJobTriggers.

    Attributes:
        job_triggers (MutableSequence[google.cloud.dlp_v2.types.JobTrigger]):
            List of triggeredJobs, up to page_size in
            ListJobTriggersRequest.
        next_page_token (str):
            If the next page is available then this value
            is the next page token to be used in the
            following ListJobTriggers request.
    """

    @property
    def raw_page(self):
        return self

    job_triggers: MutableSequence["JobTrigger"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="JobTrigger",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteJobTriggerRequest(proto.Message):
    r"""Request message for DeleteJobTrigger.

    Attributes:
        name (str):
            Required. Resource name of the project and the triggeredJob,
            for example
            ``projects/dlp-test-project/jobTriggers/53234423``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class InspectJobConfig(proto.Message):
    r"""Controls what and how to inspect for findings.

    Attributes:
        storage_config (google.cloud.dlp_v2.types.StorageConfig):
            The data to scan.
        inspect_config (google.cloud.dlp_v2.types.InspectConfig):
            How and what to scan for.
        inspect_template_name (str):
            If provided, will be used as the default for all values in
            InspectConfig. ``inspect_config`` will be merged into the
            values persisted as part of the template.
        actions (MutableSequence[google.cloud.dlp_v2.types.Action]):
            Actions to execute at the completion of the
            job.
    """

    storage_config: storage.StorageConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=storage.StorageConfig,
    )
    inspect_config: "InspectConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="InspectConfig",
    )
    inspect_template_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    actions: MutableSequence["Action"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="Action",
    )


class DataProfileAction(proto.Message):
    r"""A task to execute when a data profile has been generated.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        export_data (google.cloud.dlp_v2.types.DataProfileAction.Export):
            Export data profiles into a provided
            location.

            This field is a member of `oneof`_ ``action``.
        pub_sub_notification (google.cloud.dlp_v2.types.DataProfileAction.PubSubNotification):
            Publish a message into the Pub/Sub topic.

            This field is a member of `oneof`_ ``action``.
        publish_to_chronicle (google.cloud.dlp_v2.types.DataProfileAction.PublishToChronicle):
            Publishes generated data profiles to Google Security
            Operations. For more information, see `Use Sensitive Data
            Protection data in context-aware
            analytics <https://docs.cloud.google.com/chronicle/docs/detection/usecase-dlp-high-risk-user-download>`__.

            This field is a member of `oneof`_ ``action``.
        publish_to_scc (google.cloud.dlp_v2.types.DataProfileAction.PublishToSecurityCommandCenter):
            Publishes findings to Security Command Center
            for each data profile.

            This field is a member of `oneof`_ ``action``.
        tag_resources (google.cloud.dlp_v2.types.DataProfileAction.TagResources):
            Tags the profiled resources with the
            specified tag values.

            This field is a member of `oneof`_ ``action``.
        publish_to_dataplex_catalog (google.cloud.dlp_v2.types.DataProfileAction.PublishToDataplexCatalog):
            Publishes a portion of each profile to
            Dataplex Universal Catalog with the aspect type
            Sensitive Data Protection Profile.

            This field is a member of `oneof`_ ``action``.
    """

    class EventType(proto.Enum):
        r"""Types of event that can trigger an action.

        Values:
            EVENT_TYPE_UNSPECIFIED (0):
                Unused.
            NEW_PROFILE (1):
                New profile (not a re-profile).
            CHANGED_PROFILE (2):
                One of the following profile metrics changed:
                Data risk score, Sensitivity score, Resource
                visibility, Encryption type, Predicted
                infoTypes, Other infoTypes
            SCORE_INCREASED (3):
                Table data risk score or sensitivity score
                increased.
            ERROR_CHANGED (4):
                A user (non-internal) error occurred.
        """

        EVENT_TYPE_UNSPECIFIED = 0
        NEW_PROFILE = 1
        CHANGED_PROFILE = 2
        SCORE_INCREASED = 3
        ERROR_CHANGED = 4

    class Export(proto.Message):
        r"""If set, the detailed data profiles will be persisted to the
        location of your choice whenever updated.

        Attributes:
            profile_table (google.cloud.dlp_v2.types.BigQueryTable):
                Store all profiles to BigQuery.

                - The system will create a new dataset and table for you if
                  none are are provided. The dataset will be named
                  ``sensitive_data_protection_discovery`` and table will be
                  named ``discovery_profiles``. This table will be placed in
                  the same project as the container project running the
                  scan. After the first profile is generated and the dataset
                  and table are created, the discovery scan configuration
                  will be updated with the dataset and table names.
                - See `Analyze data profiles stored in
                  BigQuery <https://docs.cloud.google.com/sensitive-data-protection/docs/analyze-data-profiles>`__.
                - See `Sample queries for your BigQuery
                  table <https://docs.cloud.google.com/sensitive-data-protection/docs/analyze-data-profiles#sample_sql_queries>`__.
                - Data is inserted using `streaming
                  insert <https://cloud.google.com/blog/products/bigquery/life-of-a-bigquery-streaming-insert>`__
                  and so data may be in the buffer for a period of time
                  after the profile has finished.
                - The Pub/Sub notification is sent before the streaming
                  buffer is guaranteed to be written, so data may not be
                  instantly visible to queries by the time your topic
                  receives the Pub/Sub notification.
                - The best practice is to use the same table for an entire
                  organization so that you can take advantage of the
                  `provided Data Studio
                  reports <https://docs.cloud.google.com/sensitive-data-protection/docs/analyze-data-profiles#use_a_premade_report>`__.
                  If you use VPC Service Controls to define security
                  perimeters, then you must use a separate table for each
                  boundary.
            sample_findings_table (google.cloud.dlp_v2.types.BigQueryTable):
                Store sample [data profile
                findings][google.privacy.dlp.v2.DataProfileFinding] in an
                existing table or a new table in an existing dataset. Each
                regeneration will result in new rows in BigQuery. Data is
                inserted using `streaming
                insert <https://cloud.google.com/blog/products/bigquery/life-of-a-bigquery-streaming-insert>`__
                and so data may be in the buffer for a period of time after
                the profile has finished.
        """

        profile_table: storage.BigQueryTable = proto.Field(
            proto.MESSAGE,
            number=1,
            message=storage.BigQueryTable,
        )
        sample_findings_table: storage.BigQueryTable = proto.Field(
            proto.MESSAGE,
            number=2,
            message=storage.BigQueryTable,
        )

    class PubSubNotification(proto.Message):
        r"""Send a Pub/Sub message into the given Pub/Sub topic to connect other
        systems to data profile generation. The message payload data will be
        the byte serialization of ``DataProfilePubSubMessage``.

        Attributes:
            topic (str):
                Cloud Pub/Sub topic to send notifications to.
                Format is projects/{project}/topics/{topic}.
            event (google.cloud.dlp_v2.types.DataProfileAction.EventType):
                The type of event that triggers a Pub/Sub. At most one
                ``PubSubNotification`` per EventType is permitted.
            pubsub_condition (google.cloud.dlp_v2.types.DataProfilePubSubCondition):
                Conditions (e.g., data risk or sensitivity
                level) for triggering a Pub/Sub.
            detail_of_message (google.cloud.dlp_v2.types.DataProfileAction.PubSubNotification.DetailLevel):
                How much data to include in the Pub/Sub message. If the user
                wishes to limit the size of the message, they can use
                resource_name and fetch the profile fields they wish to. Per
                table profile (not per column).
        """

        class DetailLevel(proto.Enum):
            r"""The levels of detail that can be included in the Pub/Sub
            message.

            Values:
                DETAIL_LEVEL_UNSPECIFIED (0):
                    Unused.
                TABLE_PROFILE (1):
                    The full table data profile.
                RESOURCE_NAME (2):
                    The name of the profiled resource.
                FILE_STORE_PROFILE (3):
                    The full file store data profile.
            """

            DETAIL_LEVEL_UNSPECIFIED = 0
            TABLE_PROFILE = 1
            RESOURCE_NAME = 2
            FILE_STORE_PROFILE = 3

        topic: str = proto.Field(
            proto.STRING,
            number=1,
        )
        event: "DataProfileAction.EventType" = proto.Field(
            proto.ENUM,
            number=2,
            enum="DataProfileAction.EventType",
        )
        pubsub_condition: "DataProfilePubSubCondition" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="DataProfilePubSubCondition",
        )
        detail_of_message: "DataProfileAction.PubSubNotification.DetailLevel" = (
            proto.Field(
                proto.ENUM,
                number=4,
                enum="DataProfileAction.PubSubNotification.DetailLevel",
            )
        )

    class PublishToChronicle(proto.Message):
        r"""Message expressing intention to publish to Google Security
        Operations.

        """

    class PublishToSecurityCommandCenter(proto.Message):
        r"""If set, a summary finding will be created or updated in
        Security Command Center for each profile.

        """

    class PublishToDataplexCatalog(proto.Message):
        r"""Create Dataplex Universal Catalog aspects for profiled
        resources with the aspect type Sensitive Data Protection
        Profile. To learn more about aspects, see
        https://docs.cloud.google.com/sensitive-data-protection/docs/add-aspects.

        Attributes:
            lower_data_risk_to_low (bool):
                Whether creating a Dataplex Universal Catalog
                aspect for a profiled resource should lower the
                risk of the profile for that resource. This also
                lowers the data risk of resources at the lower
                levels of the resource hierarchy. For example,
                reducing the data risk of a table data profile
                also reduces the data risk of the constituent
                column data profiles.
        """

        lower_data_risk_to_low: bool = proto.Field(
            proto.BOOL,
            number=1,
        )

    class TagResources(proto.Message):
        r"""If set, attaches the [tags]
        (https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview)
        provided to profiled resources. Tags support `access
        control <https://docs.cloud.google.com/iam/docs/tags-access-control>`__.
        You can conditionally grant or deny access to a resource based on
        whether the resource has a specific tag.

        Attributes:
            tag_conditions (MutableSequence[google.cloud.dlp_v2.types.DataProfileAction.TagResources.TagCondition]):
                The tags to associate with different
                conditions.
            profile_generations_to_tag (MutableSequence[google.cloud.dlp_v2.types.ProfileGeneration]):
                The profile generations for which the tag should be attached
                to resources. If you attach a tag to only new profiles, then
                if the sensitivity score of a profile subsequently changes,
                its tag doesn't change. By default, this field includes only
                new profiles. To include both new and updated profiles for
                tagging, this field should explicitly include both
                ``PROFILE_GENERATION_NEW`` and
                ``PROFILE_GENERATION_UPDATE``.
            lower_data_risk_to_low (bool):
                Whether applying a tag to a resource should lower the risk
                of the profile for that resource. For example, in
                conjunction with an `IAM deny
                policy <https://docs.cloud.google.com/iam/docs/deny-overview>`__,
                you can deny all principals a permission if a tag value is
                present, mitigating the risk of the resource. This also
                lowers the data risk of resources at the lower levels of the
                resource hierarchy. For example, reducing the data risk of a
                table data profile also reduces the data risk of the
                constituent column data profiles.
        """

        class TagCondition(proto.Message):
            r"""The tag to attach to profiles matching the condition. At most one
            ``TagCondition`` can be specified per sensitivity level.


            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                tag (google.cloud.dlp_v2.types.DataProfileAction.TagResources.TagValue):
                    The tag value to attach to resources.
                sensitivity_score (google.cloud.dlp_v2.types.SensitivityScore):
                    Conditions attaching the tag to a resource on
                    its profile having this sensitivity score.

                    This field is a member of `oneof`_ ``type``.
            """

            tag: "DataProfileAction.TagResources.TagValue" = proto.Field(
                proto.MESSAGE,
                number=1,
                message="DataProfileAction.TagResources.TagValue",
            )
            sensitivity_score: storage.SensitivityScore = proto.Field(
                proto.MESSAGE,
                number=2,
                oneof="type",
                message=storage.SensitivityScore,
            )

        class TagValue(proto.Message):
            r"""A value of a tag.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                namespaced_value (str):
                    The namespaced name for the tag value to attach to
                    resources. Must be in the format
                    ``{parent_id}/{tag_key_short_name}/{short_name}``, for
                    example, "123456/environment/prod" for an organization
                    parent, or "my-project/environment/prod" for a project
                    parent.

                    This field is a member of `oneof`_ ``format``.
            """

            namespaced_value: str = proto.Field(
                proto.STRING,
                number=1,
                oneof="format",
            )

        tag_conditions: MutableSequence[
            "DataProfileAction.TagResources.TagCondition"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="DataProfileAction.TagResources.TagCondition",
        )
        profile_generations_to_tag: MutableSequence["ProfileGeneration"] = (
            proto.RepeatedField(
                proto.ENUM,
                number=2,
                enum="ProfileGeneration",
            )
        )
        lower_data_risk_to_low: bool = proto.Field(
            proto.BOOL,
            number=3,
        )

    export_data: Export = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="action",
        message=Export,
    )
    pub_sub_notification: PubSubNotification = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="action",
        message=PubSubNotification,
    )
    publish_to_chronicle: PublishToChronicle = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="action",
        message=PublishToChronicle,
    )
    publish_to_scc: PublishToSecurityCommandCenter = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="action",
        message=PublishToSecurityCommandCenter,
    )
    tag_resources: TagResources = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="action",
        message=TagResources,
    )
    publish_to_dataplex_catalog: PublishToDataplexCatalog = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="action",
        message=PublishToDataplexCatalog,
    )


class DataProfileFinding(proto.Message):
    r"""Details about a piece of potentially sensitive information
    that was detected when the data resource was profiled.

    Attributes:
        quote (str):
            The content that was found. Even if the
            content is not textual, it may be converted to a
            textual representation here. If the finding
            exceeds 4096 bytes in length, the quote may be
            omitted.
        infotype (google.cloud.dlp_v2.types.InfoType):
            The `type of
            content <https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference>`__
            that might have been found.
        quote_info (google.cloud.dlp_v2.types.QuoteInfo):
            Contains data parsed from quotes. Currently supported
            infoTypes: DATE, DATE_OF_BIRTH, and TIME.
        data_profile_resource_name (str):
            Resource name of the data profile associated
            with the finding.
        finding_id (str):
            A unique identifier for the finding.
        timestamp (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp when the finding was detected.
        location (google.cloud.dlp_v2.types.DataProfileFindingLocation):
            Where the content was found.
        resource_visibility (google.cloud.dlp_v2.types.ResourceVisibility):
            How broadly a resource has been shared.
        full_resource_name (str):
            The `full resource
            name <https://cloud.google.com/apis/design/resource_names#full_resource_name>`__
            of the resource profiled for this finding.
        data_source_type (google.cloud.dlp_v2.types.DataSourceType):
            The type of the resource that was profiled.
    """

    quote: str = proto.Field(
        proto.STRING,
        number=1,
    )
    infotype: storage.InfoType = proto.Field(
        proto.MESSAGE,
        number=2,
        message=storage.InfoType,
    )
    quote_info: "QuoteInfo" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="QuoteInfo",
    )
    data_profile_resource_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    finding_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    timestamp: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    location: "DataProfileFindingLocation" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="DataProfileFindingLocation",
    )
    resource_visibility: "ResourceVisibility" = proto.Field(
        proto.ENUM,
        number=8,
        enum="ResourceVisibility",
    )
    full_resource_name: str = proto.Field(
        proto.STRING,
        number=9,
    )
    data_source_type: "DataSourceType" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="DataSourceType",
    )


class DataProfileFindingLocation(proto.Message):
    r"""Location of a data profile finding within a resource.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        container_name (str):
            Name of the container where the finding is located. The
            top-level name is the source file name or table name. Names
            of some common storage containers are formatted as follows:

            - BigQuery tables: ``{project_id}:{dataset_id}.{table_id}``
            - Cloud Storage files: ``gs://{bucket}/{path}``
        data_profile_finding_record_location (google.cloud.dlp_v2.types.DataProfileFindingRecordLocation):
            Location of a finding within a resource that
            produces a table data profile.

            This field is a member of `oneof`_ ``location_extra_details``.
    """

    container_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_profile_finding_record_location: "DataProfileFindingRecordLocation" = (
        proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="location_extra_details",
            message="DataProfileFindingRecordLocation",
        )
    )


class DataProfileFindingRecordLocation(proto.Message):
    r"""Location of a finding within a resource that produces a table
    data profile.

    Attributes:
        field (google.cloud.dlp_v2.types.FieldId):
            Field ID of the column containing the
            finding.
    """

    field: storage.FieldId = proto.Field(
        proto.MESSAGE,
        number=1,
        message=storage.FieldId,
    )


class DataProfileJobConfig(proto.Message):
    r"""Configuration for setting up a job to scan resources for profile
    generation. Only one data profile configuration may exist per
    organization, folder, or project.

    The generated data profiles are retained according to the [data
    retention policy]
    (https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#retention).

    Attributes:
        location (google.cloud.dlp_v2.types.DataProfileLocation):
            The data to scan.
        project_id (str):
            The project that will run the scan. The DLP
            service account that exists within this project
            must have access to all resources that are
            profiled, and the DLP API must be enabled.
        other_cloud_starting_location (google.cloud.dlp_v2.types.OtherCloudDiscoveryStartingLocation):
            Must be set only when scanning other clouds.
        inspect_templates (MutableSequence[str]):
            Detection logic for profile generation.

            Not all template features are used by profiles.
            FindingLimits, include_quote and exclude_info_types have no
            impact on data profiling.

            Multiple templates may be provided if there is data in
            multiple regions. At most one template must be specified
            per-region (including "global"). Each region is scanned
            using the applicable template. If no region-specific
            template is specified, but a "global" template is specified,
            it will be copied to that region and used instead. If no
            global or region-specific template is provided for a region
            with data, that region's data will not be scanned.

            For more information, see
            https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#data-residency.
        data_profile_actions (MutableSequence[google.cloud.dlp_v2.types.DataProfileAction]):
            Actions to execute at the completion of the
            job.
    """

    location: "DataProfileLocation" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="DataProfileLocation",
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=5,
    )
    other_cloud_starting_location: "OtherCloudDiscoveryStartingLocation" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="OtherCloudDiscoveryStartingLocation",
    )
    inspect_templates: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    data_profile_actions: MutableSequence["DataProfileAction"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="DataProfileAction",
    )


class BigQueryRegex(proto.Message):
    r"""A pattern to match against one or more tables, datasets, or projects
    that contain BigQuery tables. At least one pattern must be
    specified. Regular expressions use RE2
    `syntax <https://github.com/google/re2/wiki/Syntax>`__; a guide can
    be found under the google/re2 repository on GitHub.

    Attributes:
        project_id_regex (str):
            For organizations, if unset, will match all
            projects. Has no effect for data profile
            configurations created within a project.
        dataset_id_regex (str):
            If unset, this property matches all datasets.
        table_id_regex (str):
            If unset, this property matches all tables.
    """

    project_id_regex: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dataset_id_regex: str = proto.Field(
        proto.STRING,
        number=2,
    )
    table_id_regex: str = proto.Field(
        proto.STRING,
        number=3,
    )


class BigQueryRegexes(proto.Message):
    r"""A collection of regular expressions to determine what tables
    to match against.

    Attributes:
        patterns (MutableSequence[google.cloud.dlp_v2.types.BigQueryRegex]):
            A single BigQuery regular expression pattern
            to match against one or more tables, datasets,
            or projects that contain BigQuery tables.
    """

    patterns: MutableSequence["BigQueryRegex"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="BigQueryRegex",
    )


class BigQueryTableTypes(proto.Message):
    r"""The types of BigQuery tables supported by Cloud DLP.

    Attributes:
        types (MutableSequence[google.cloud.dlp_v2.types.BigQueryTableType]):
            A set of BigQuery table types.
    """

    types: MutableSequence["BigQueryTableType"] = proto.RepeatedField(
        proto.ENUM,
        number=1,
        enum="BigQueryTableType",
    )


class Disabled(proto.Message):
    r"""Do not profile the tables."""


class DataProfileLocation(proto.Message):
    r"""The data that will be profiled.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        organization_id (int):
            The ID of an organization to scan.

            This field is a member of `oneof`_ ``location``.
        folder_id (int):
            The ID of the folder within an organization
            to scan.

            This field is a member of `oneof`_ ``location``.
    """

    organization_id: int = proto.Field(
        proto.INT64,
        number=1,
        oneof="location",
    )
    folder_id: int = proto.Field(
        proto.INT64,
        number=2,
        oneof="location",
    )


class DiscoveryConfig(proto.Message):
    r"""Configuration for discovery to scan resources for profile
    generation. Only one discovery configuration may exist per
    organization, folder, or project.

    The generated data profiles are retained according to the [data
    retention policy]
    (https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#retention).

    Attributes:
        name (str):
            Output only. Unique resource name for the DiscoveryConfig,
            assigned by the service when the DiscoveryConfig is created,
            for example
            ``projects/dlp-test-project/locations/global/discoveryConfigs/53234423``.
        display_name (str):
            Display name (max 100 chars)
        org_config (google.cloud.dlp_v2.types.DiscoveryConfig.OrgConfig):
            Only set when the parent is an org.
        other_cloud_starting_location (google.cloud.dlp_v2.types.OtherCloudDiscoveryStartingLocation):
            Must be set only when scanning other clouds.
        inspect_templates (MutableSequence[str]):
            Detection logic for profile generation.

            Not all template features are used by Discovery.
            FindingLimits, include_quote and exclude_info_types have no
            impact on Discovery.

            Multiple templates may be provided if there is data in
            multiple regions. At most one template must be specified
            per-region (including "global"). Each region is scanned
            using the applicable template. If no region-specific
            template is specified, but a "global" template is specified,
            it will be copied to that region and used instead. If no
            global or region-specific template is provided for a region
            with data, that region's data will not be scanned.

            For more information, see
            https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#data-residency.
        actions (MutableSequence[google.cloud.dlp_v2.types.DataProfileAction]):
            Actions to execute at the completion of
            scanning.
        targets (MutableSequence[google.cloud.dlp_v2.types.DiscoveryTarget]):
            Target to match against for determining what
            to scan and how frequently.
        errors (MutableSequence[google.cloud.dlp_v2.types.Error]):
            Output only. A stream of errors encountered
            when the config was activated. Repeated errors
            may result in the config automatically being
            paused. Output only field. Will return the last
            100 errors. Whenever the config is modified this
            list will be cleared.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation timestamp of a
            DiscoveryConfig.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last update timestamp of a
            DiscoveryConfig.
        last_run_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp of the last time
            this config was executed.
        status (google.cloud.dlp_v2.types.DiscoveryConfig.Status):
            Required. A status for this configuration.
        processing_location (google.cloud.dlp_v2.types.ProcessingLocation):
            Optional. Processing location configuration. Vertex AI
            dataset scanning will set
            processing_location.image_fallback_type to
            MultiRegionProcessing by default.
    """

    class Status(proto.Enum):
        r"""Whether the discovery config is currently active. New options
        may be added at a later time.

        Values:
            STATUS_UNSPECIFIED (0):
                Unused
            RUNNING (1):
                The discovery config is currently active.
            PAUSED (2):
                The discovery config is paused temporarily.
        """

        STATUS_UNSPECIFIED = 0
        RUNNING = 1
        PAUSED = 2

    class OrgConfig(proto.Message):
        r"""Project and scan location information. Only set when the
        parent is an org.

        Attributes:
            location (google.cloud.dlp_v2.types.DiscoveryStartingLocation):
                The data to scan: folder, org, or project
            project_id (str):
                The project that will run the scan. The DLP
                service account that exists within this project
                must have access to all resources that are
                profiled, and the DLP API must be enabled.
        """

        location: "DiscoveryStartingLocation" = proto.Field(
            proto.MESSAGE,
            number=1,
            message="DiscoveryStartingLocation",
        )
        project_id: str = proto.Field(
            proto.STRING,
            number=2,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=11,
    )
    org_config: OrgConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=OrgConfig,
    )
    other_cloud_starting_location: "OtherCloudDiscoveryStartingLocation" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="OtherCloudDiscoveryStartingLocation",
    )
    inspect_templates: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    actions: MutableSequence["DataProfileAction"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="DataProfileAction",
    )
    targets: MutableSequence["DiscoveryTarget"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="DiscoveryTarget",
    )
    errors: MutableSequence["Error"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="Error",
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
    last_run_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    status: Status = proto.Field(
        proto.ENUM,
        number=10,
        enum=Status,
    )
    processing_location: "ProcessingLocation" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="ProcessingLocation",
    )


class DiscoveryTarget(proto.Message):
    r"""Target used to match against for Discovery.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        big_query_target (google.cloud.dlp_v2.types.BigQueryDiscoveryTarget):
            BigQuery target for Discovery. The first
            target to match a table will be the one applied.

            This field is a member of `oneof`_ ``target``.
        cloud_sql_target (google.cloud.dlp_v2.types.CloudSqlDiscoveryTarget):
            Cloud SQL target for Discovery. The first
            target to match a table will be the one applied.

            This field is a member of `oneof`_ ``target``.
        secrets_target (google.cloud.dlp_v2.types.SecretsDiscoveryTarget):
            Discovery target that looks for credentials
            and secrets stored in cloud resource metadata
            and reports them as vulnerabilities to Security
            Command Center. Only one target of this type is
            allowed.

            This field is a member of `oneof`_ ``target``.
        cloud_storage_target (google.cloud.dlp_v2.types.CloudStorageDiscoveryTarget):
            Cloud Storage target for Discovery. The first
            target to match a table will be the one applied.

            This field is a member of `oneof`_ ``target``.
        other_cloud_target (google.cloud.dlp_v2.types.OtherCloudDiscoveryTarget):
            Other clouds target for discovery. The first
            target to match a resource will be the one
            applied.

            This field is a member of `oneof`_ ``target``.
        vertex_dataset_target (google.cloud.dlp_v2.types.VertexDatasetDiscoveryTarget):
            Vertex AI dataset target for Discovery. The first target to
            match a dataset will be the one applied. Note that discovery
            for Vertex AI can incur Cloud Storage Class B operation
            charges for storage.objects.get operations and retrieval
            fees. For more information, see `Cloud Storage
            pricing <https://cloud.google.com/storage/pricing#price-tables>`__.
            Note that discovery for Vertex AI dataset will not be able
            to scan images unless
            DiscoveryConfig.processing_location.image_fallback_location
            has multi_region_processing or global_processing configured.

            This field is a member of `oneof`_ ``target``.
    """

    big_query_target: "BigQueryDiscoveryTarget" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="target",
        message="BigQueryDiscoveryTarget",
    )
    cloud_sql_target: "CloudSqlDiscoveryTarget" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="target",
        message="CloudSqlDiscoveryTarget",
    )
    secrets_target: "SecretsDiscoveryTarget" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="target",
        message="SecretsDiscoveryTarget",
    )
    cloud_storage_target: "CloudStorageDiscoveryTarget" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="target",
        message="CloudStorageDiscoveryTarget",
    )
    other_cloud_target: "OtherCloudDiscoveryTarget" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="target",
        message="OtherCloudDiscoveryTarget",
    )
    vertex_dataset_target: "VertexDatasetDiscoveryTarget" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="target",
        message="VertexDatasetDiscoveryTarget",
    )


class BigQueryDiscoveryTarget(proto.Message):
    r"""Target used to match against for discovery with BigQuery
    tables

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        filter (google.cloud.dlp_v2.types.DiscoveryBigQueryFilter):
            Required. The tables the discovery cadence
            applies to. The first target with a matching
            filter will be the one to apply to a table.
        conditions (google.cloud.dlp_v2.types.DiscoveryBigQueryConditions):
            In addition to matching the filter, these
            conditions must be true before a profile is
            generated.
        cadence (google.cloud.dlp_v2.types.DiscoveryGenerationCadence):
            How often and when to update profiles. New
            tables that match both the filter and conditions
            are scanned as quickly as possible depending on
            system capacity.

            This field is a member of `oneof`_ ``frequency``.
        disabled (google.cloud.dlp_v2.types.Disabled):
            Tables that match this filter will not have
            profiles created.

            This field is a member of `oneof`_ ``frequency``.
    """

    filter: "DiscoveryBigQueryFilter" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="DiscoveryBigQueryFilter",
    )
    conditions: "DiscoveryBigQueryConditions" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DiscoveryBigQueryConditions",
    )
    cadence: "DiscoveryGenerationCadence" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="frequency",
        message="DiscoveryGenerationCadence",
    )
    disabled: "Disabled" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="frequency",
        message="Disabled",
    )


class DiscoveryBigQueryFilter(proto.Message):
    r"""Determines what tables will have profiles generated within an
    organization or project. Includes the ability to filter by
    regular expression patterns on project ID, dataset ID, and table
    ID.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        tables (google.cloud.dlp_v2.types.BigQueryTableCollection):
            A specific set of tables for this filter to
            apply to. A table collection must be specified
            in only one filter per config. If a table id or
            dataset is empty, Cloud DLP assumes all tables
            in that collection must be profiled. Must
            specify a project ID.

            This field is a member of `oneof`_ ``filter``.
        other_tables (google.cloud.dlp_v2.types.DiscoveryBigQueryFilter.AllOtherBigQueryTables):
            Catch-all. This should always be the last
            filter in the list because anything above it
            will apply first. Should only appear once in a
            configuration. If none is specified, a default
            one will be added automatically.

            This field is a member of `oneof`_ ``filter``.
        table_reference (google.cloud.dlp_v2.types.TableReference):
            The table to scan. Discovery configurations
            including this can only include one
            DiscoveryTarget (the DiscoveryTarget with this
            TableReference).

            This field is a member of `oneof`_ ``filter``.
    """

    class AllOtherBigQueryTables(proto.Message):
        r"""Catch-all for all other tables not specified by other
        filters. Should always be last, except for single-table
        configurations, which will only have a TableReference target.

        """

    tables: "BigQueryTableCollection" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="filter",
        message="BigQueryTableCollection",
    )
    other_tables: AllOtherBigQueryTables = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="filter",
        message=AllOtherBigQueryTables,
    )
    table_reference: storage.TableReference = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="filter",
        message=storage.TableReference,
    )


class BigQueryTableCollection(proto.Message):
    r"""Specifies a collection of BigQuery tables. Used for
    Discovery.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        include_regexes (google.cloud.dlp_v2.types.BigQueryRegexes):
            A collection of regular expressions to match
            a BigQuery table against.

            This field is a member of `oneof`_ ``pattern``.
    """

    include_regexes: "BigQueryRegexes" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="pattern",
        message="BigQueryRegexes",
    )


class DiscoveryBigQueryConditions(proto.Message):
    r"""Requirements that must be true before a table is scanned in
    discovery for the first time. There is an AND relationship
    between the top-level attributes. Additionally, minimum
    conditions with an OR relationship that must be met before Cloud
    DLP scans a table can be set (like a minimum row count or a
    minimum table age).

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        created_after (google.protobuf.timestamp_pb2.Timestamp):
            BigQuery table must have been created after
            this date. Used to avoid backfilling.
        types (google.cloud.dlp_v2.types.BigQueryTableTypes):
            Restrict discovery to specific table types.

            This field is a member of `oneof`_ ``included_types``.
        type_collection (google.cloud.dlp_v2.types.BigQueryTableTypeCollection):
            Restrict discovery to categories of table
            types.

            This field is a member of `oneof`_ ``included_types``.
        or_conditions (google.cloud.dlp_v2.types.DiscoveryBigQueryConditions.OrConditions):
            At least one of the conditions must be true
            for a table to be scanned.
    """

    class OrConditions(proto.Message):
        r"""There is an OR relationship between these attributes. They
        are used to determine if a table should be scanned or not in
        Discovery.

        Attributes:
            min_row_count (int):
                Minimum number of rows that should be present
                before Cloud DLP profiles a table
            min_age (google.protobuf.duration_pb2.Duration):
                Minimum age a table must have before Cloud
                DLP can profile it. Value must be 1 hour or
                greater.
        """

        min_row_count: int = proto.Field(
            proto.INT32,
            number=1,
        )
        min_age: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=2,
            message=duration_pb2.Duration,
        )

    created_after: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    types: "BigQueryTableTypes" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="included_types",
        message="BigQueryTableTypes",
    )
    type_collection: "BigQueryTableTypeCollection" = proto.Field(
        proto.ENUM,
        number=3,
        oneof="included_types",
        enum="BigQueryTableTypeCollection",
    )
    or_conditions: OrConditions = proto.Field(
        proto.MESSAGE,
        number=4,
        message=OrConditions,
    )


class DiscoveryGenerationCadence(proto.Message):
    r"""What must take place for a profile to be updated and how
    frequently it should occur.
    New tables are scanned as quickly as possible depending on
    system capacity.

    Attributes:
        schema_modified_cadence (google.cloud.dlp_v2.types.DiscoverySchemaModifiedCadence):
            Governs when to update data profiles when a
            schema is modified.
        table_modified_cadence (google.cloud.dlp_v2.types.DiscoveryTableModifiedCadence):
            Governs when to update data profiles when a
            table is modified.
        inspect_template_modified_cadence (google.cloud.dlp_v2.types.DiscoveryInspectTemplateModifiedCadence):
            Governs when to update data profiles when the inspection
            rules defined by the ``InspectTemplate`` change. If not set,
            changing the template will not cause a data profile to
            update.
        refresh_frequency (google.cloud.dlp_v2.types.DataProfileUpdateFrequency):
            Frequency at which profiles should be
            updated, regardless of whether the underlying
            resource has changed. Defaults to never.
    """

    schema_modified_cadence: "DiscoverySchemaModifiedCadence" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="DiscoverySchemaModifiedCadence",
    )
    table_modified_cadence: "DiscoveryTableModifiedCadence" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DiscoveryTableModifiedCadence",
    )
    inspect_template_modified_cadence: "DiscoveryInspectTemplateModifiedCadence" = (
        proto.Field(
            proto.MESSAGE,
            number=3,
            message="DiscoveryInspectTemplateModifiedCadence",
        )
    )
    refresh_frequency: "DataProfileUpdateFrequency" = proto.Field(
        proto.ENUM,
        number=4,
        enum="DataProfileUpdateFrequency",
    )


class DiscoveryTableModifiedCadence(proto.Message):
    r"""The cadence at which to update data profiles when a table is
    modified.

    Attributes:
        types (MutableSequence[google.cloud.dlp_v2.types.BigQueryTableModification]):
            The type of events to consider when deciding if the table
            has been modified and should have the profile updated.
            Defaults to MODIFIED_TIMESTAMP.
        frequency (google.cloud.dlp_v2.types.DataProfileUpdateFrequency):
            How frequently data profiles can be updated
            when tables are modified. Defaults to never.
    """

    types: MutableSequence["BigQueryTableModification"] = proto.RepeatedField(
        proto.ENUM,
        number=1,
        enum="BigQueryTableModification",
    )
    frequency: "DataProfileUpdateFrequency" = proto.Field(
        proto.ENUM,
        number=2,
        enum="DataProfileUpdateFrequency",
    )


class DiscoverySchemaModifiedCadence(proto.Message):
    r"""The cadence at which to update data profiles when a schema is
    modified.

    Attributes:
        types (MutableSequence[google.cloud.dlp_v2.types.BigQuerySchemaModification]):
            The type of events to consider when deciding if the table's
            schema has been modified and should have the profile
            updated. Defaults to NEW_COLUMNS.
        frequency (google.cloud.dlp_v2.types.DataProfileUpdateFrequency):
            How frequently profiles may be updated when
            schemas are modified. Defaults to monthly.
    """

    types: MutableSequence["BigQuerySchemaModification"] = proto.RepeatedField(
        proto.ENUM,
        number=1,
        enum="BigQuerySchemaModification",
    )
    frequency: "DataProfileUpdateFrequency" = proto.Field(
        proto.ENUM,
        number=2,
        enum="DataProfileUpdateFrequency",
    )


class DiscoveryInspectTemplateModifiedCadence(proto.Message):
    r"""The cadence at which to update data profiles when the inspection
    rules defined by the ``InspectTemplate`` change.

    Attributes:
        frequency (google.cloud.dlp_v2.types.DataProfileUpdateFrequency):
            How frequently data profiles can be updated
            when the template is modified. Defaults to
            never.
    """

    frequency: "DataProfileUpdateFrequency" = proto.Field(
        proto.ENUM,
        number=1,
        enum="DataProfileUpdateFrequency",
    )


class CloudSqlDiscoveryTarget(proto.Message):
    r"""Target used to match against for discovery with Cloud SQL
    tables.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        filter (google.cloud.dlp_v2.types.DiscoveryCloudSqlFilter):
            Required. The tables the discovery cadence
            applies to. The first target with a matching
            filter will be the one to apply to a table.
        conditions (google.cloud.dlp_v2.types.DiscoveryCloudSqlConditions):
            In addition to matching the filter, these
            conditions must be true before a profile is
            generated.
        generation_cadence (google.cloud.dlp_v2.types.DiscoveryCloudSqlGenerationCadence):
            How often and when to update profiles. New
            tables that match both the filter and conditions
            are scanned as quickly as possible depending on
            system capacity.

            This field is a member of `oneof`_ ``cadence``.
        disabled (google.cloud.dlp_v2.types.Disabled):
            Disable profiling for database resources that
            match this filter.

            This field is a member of `oneof`_ ``cadence``.
    """

    filter: "DiscoveryCloudSqlFilter" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="DiscoveryCloudSqlFilter",
    )
    conditions: "DiscoveryCloudSqlConditions" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DiscoveryCloudSqlConditions",
    )
    generation_cadence: "DiscoveryCloudSqlGenerationCadence" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="cadence",
        message="DiscoveryCloudSqlGenerationCadence",
    )
    disabled: "Disabled" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="cadence",
        message="Disabled",
    )


class DiscoveryCloudSqlFilter(proto.Message):
    r"""Determines what tables will have profiles generated within an
    organization or project. Includes the ability to filter by
    regular expression patterns on project ID, location, instance,
    database, and database resource name.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        collection (google.cloud.dlp_v2.types.DatabaseResourceCollection):
            A specific set of database resources for this
            filter to apply to.

            This field is a member of `oneof`_ ``filter``.
        others (google.cloud.dlp_v2.types.AllOtherDatabaseResources):
            Catch-all. This should always be the last
            target in the list because anything above it
            will apply first. Should only appear once in a
            configuration. If none is specified, a default
            one will be added automatically.

            This field is a member of `oneof`_ ``filter``.
        database_resource_reference (google.cloud.dlp_v2.types.DatabaseResourceReference):
            The database resource to scan. Targets
            including this can only include one target (the
            target with this database resource reference).

            This field is a member of `oneof`_ ``filter``.
    """

    collection: "DatabaseResourceCollection" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="filter",
        message="DatabaseResourceCollection",
    )
    others: "AllOtherDatabaseResources" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="filter",
        message="AllOtherDatabaseResources",
    )
    database_resource_reference: "DatabaseResourceReference" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="filter",
        message="DatabaseResourceReference",
    )


class DatabaseResourceCollection(proto.Message):
    r"""Match database resources using regex filters. Examples of
    database resources are tables, views, and stored procedures.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        include_regexes (google.cloud.dlp_v2.types.DatabaseResourceRegexes):
            A collection of regular expressions to match
            a database resource against.

            This field is a member of `oneof`_ ``pattern``.
    """

    include_regexes: "DatabaseResourceRegexes" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="pattern",
        message="DatabaseResourceRegexes",
    )


class DatabaseResourceRegexes(proto.Message):
    r"""A collection of regular expressions to determine what
    database resources to match against.

    Attributes:
        patterns (MutableSequence[google.cloud.dlp_v2.types.DatabaseResourceRegex]):
            A group of regular expression patterns to
            match against one or more database resources.
            Maximum of 100 entries. The sum of all regular
            expression's length can't exceed 10 KiB.
    """

    patterns: MutableSequence["DatabaseResourceRegex"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DatabaseResourceRegex",
    )


class DatabaseResourceRegex(proto.Message):
    r"""A pattern to match against one or more database resources. At least
    one pattern must be specified. Regular expressions use RE2
    `syntax <https://github.com/google/re2/wiki/Syntax>`__; a guide can
    be found under the google/re2 repository on GitHub.

    Attributes:
        project_id_regex (str):
            For organizations, if unset, will match all
            projects. Has no effect for configurations
            created within a project.
        instance_regex (str):
            Regex to test the instance name against. If
            empty, all instances match.
        database_regex (str):
            Regex to test the database name against. If
            empty, all databases match.
        database_resource_name_regex (str):
            Regex to test the database resource's name
            against. An example of a database resource name
            is a table's name. Other database resource names
            like view names could be included in the future.
            If empty, all database resources match.
    """

    project_id_regex: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_regex: str = proto.Field(
        proto.STRING,
        number=2,
    )
    database_regex: str = proto.Field(
        proto.STRING,
        number=3,
    )
    database_resource_name_regex: str = proto.Field(
        proto.STRING,
        number=4,
    )


class AllOtherDatabaseResources(proto.Message):
    r"""Match database resources not covered by any other filter."""


class DatabaseResourceReference(proto.Message):
    r"""Identifies a single database resource, like a table within a
    database.

    Attributes:
        project_id (str):
            Required. If within a project-level config,
            then this must match the config's project ID.
        instance (str):
            Required. The instance where this resource is
            located. For example: Cloud SQL instance ID.
        database (str):
            Required. Name of a database within the
            instance.
        database_resource (str):
            Required. Name of a database resource, for
            example, a table within the database.
    """

    project_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance: str = proto.Field(
        proto.STRING,
        number=2,
    )
    database: str = proto.Field(
        proto.STRING,
        number=3,
    )
    database_resource: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DiscoveryCloudSqlConditions(proto.Message):
    r"""Requirements that must be true before a table is profiled for
    the first time.

    Attributes:
        database_engines (MutableSequence[google.cloud.dlp_v2.types.DiscoveryCloudSqlConditions.DatabaseEngine]):
            Optional. Database engines that should be profiled.
            Optional. Defaults to ALL_SUPPORTED_DATABASE_ENGINES if
            unspecified.
        types (MutableSequence[google.cloud.dlp_v2.types.DiscoveryCloudSqlConditions.DatabaseResourceType]):
            Data profiles will only be generated for the database
            resource types specified in this field. If not specified,
            defaults to [DATABASE_RESOURCE_TYPE_ALL_SUPPORTED_TYPES].
    """

    class DatabaseEngine(proto.Enum):
        r"""The database engines that should be profiled.

        Values:
            DATABASE_ENGINE_UNSPECIFIED (0):
                Unused.
            ALL_SUPPORTED_DATABASE_ENGINES (1):
                Include all supported database engines.
            MYSQL (2):
                MySQL database.
            POSTGRES (3):
                PostgreSQL database.
        """

        DATABASE_ENGINE_UNSPECIFIED = 0
        ALL_SUPPORTED_DATABASE_ENGINES = 1
        MYSQL = 2
        POSTGRES = 3

    class DatabaseResourceType(proto.Enum):
        r"""Cloud SQL database resource types. New values can be added at
        a later time.

        Values:
            DATABASE_RESOURCE_TYPE_UNSPECIFIED (0):
                Unused.
            DATABASE_RESOURCE_TYPE_ALL_SUPPORTED_TYPES (1):
                Includes database resource types that become
                supported at a later time.
            DATABASE_RESOURCE_TYPE_TABLE (2):
                Tables.
        """

        DATABASE_RESOURCE_TYPE_UNSPECIFIED = 0
        DATABASE_RESOURCE_TYPE_ALL_SUPPORTED_TYPES = 1
        DATABASE_RESOURCE_TYPE_TABLE = 2

    database_engines: MutableSequence[DatabaseEngine] = proto.RepeatedField(
        proto.ENUM,
        number=1,
        enum=DatabaseEngine,
    )
    types: MutableSequence[DatabaseResourceType] = proto.RepeatedField(
        proto.ENUM,
        number=3,
        enum=DatabaseResourceType,
    )


class DiscoveryCloudSqlGenerationCadence(proto.Message):
    r"""How often existing tables should have their profiles
    refreshed. New tables are scanned as quickly as possible
    depending on system capacity.

    Attributes:
        schema_modified_cadence (google.cloud.dlp_v2.types.DiscoveryCloudSqlGenerationCadence.SchemaModifiedCadence):
            When to reprofile if the schema has changed.
        refresh_frequency (google.cloud.dlp_v2.types.DataProfileUpdateFrequency):
            Data changes (non-schema changes) in Cloud
            SQL tables can't trigger reprofiling. If you set
            this field, profiles are refreshed at this
            frequency regardless of whether the underlying
            tables have changed. Defaults to never.
        inspect_template_modified_cadence (google.cloud.dlp_v2.types.DiscoveryInspectTemplateModifiedCadence):
            Governs when to update data profiles when the inspection
            rules defined by the ``InspectTemplate`` change. If not set,
            changing the template will not cause a data profile to
            update.
    """

    class SchemaModifiedCadence(proto.Message):
        r"""How frequently to modify the profile when the table's schema
        is modified.

        Attributes:
            types (MutableSequence[google.cloud.dlp_v2.types.DiscoveryCloudSqlGenerationCadence.SchemaModifiedCadence.CloudSqlSchemaModification]):
                The types of schema modifications to consider. Defaults to
                NEW_COLUMNS.
            frequency (google.cloud.dlp_v2.types.DataProfileUpdateFrequency):
                Frequency to regenerate data profiles when
                the schema is modified. Defaults to monthly.
        """

        class CloudSqlSchemaModification(proto.Enum):
            r"""The type of modification that causes a profile update.

            Values:
                SQL_SCHEMA_MODIFICATION_UNSPECIFIED (0):
                    Unused.
                NEW_COLUMNS (1):
                    New columns have appeared.
                REMOVED_COLUMNS (2):
                    Columns have been removed from the table.
            """

            SQL_SCHEMA_MODIFICATION_UNSPECIFIED = 0
            NEW_COLUMNS = 1
            REMOVED_COLUMNS = 2

        types: MutableSequence[
            "DiscoveryCloudSqlGenerationCadence.SchemaModifiedCadence.CloudSqlSchemaModification"
        ] = proto.RepeatedField(
            proto.ENUM,
            number=1,
            enum="DiscoveryCloudSqlGenerationCadence.SchemaModifiedCadence.CloudSqlSchemaModification",
        )
        frequency: "DataProfileUpdateFrequency" = proto.Field(
            proto.ENUM,
            number=2,
            enum="DataProfileUpdateFrequency",
        )

    schema_modified_cadence: SchemaModifiedCadence = proto.Field(
        proto.MESSAGE,
        number=1,
        message=SchemaModifiedCadence,
    )
    refresh_frequency: "DataProfileUpdateFrequency" = proto.Field(
        proto.ENUM,
        number=2,
        enum="DataProfileUpdateFrequency",
    )
    inspect_template_modified_cadence: "DiscoveryInspectTemplateModifiedCadence" = (
        proto.Field(
            proto.MESSAGE,
            number=3,
            message="DiscoveryInspectTemplateModifiedCadence",
        )
    )


class SecretsDiscoveryTarget(proto.Message):
    r"""Discovery target for credentials and secrets in cloud resource
    metadata.

    This target does not include any filtering or frequency controls.
    Cloud DLP will scan cloud resource metadata for secrets daily.

    No inspect template should be included in the discovery config for a
    security benchmarks scan. Instead, the built-in list of secrets and
    credentials infoTypes will be used (see
    https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference#credentials_and_secrets).

    Credentials and secrets discovered will be reported as
    vulnerabilities to Security Command Center.

    """


class CloudStorageDiscoveryTarget(proto.Message):
    r"""Target used to match against for discovery with Cloud Storage
    buckets.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        filter (google.cloud.dlp_v2.types.DiscoveryCloudStorageFilter):
            Required. The buckets the generation_cadence applies to. The
            first target with a matching filter will be the one to apply
            to a bucket.
        conditions (google.cloud.dlp_v2.types.DiscoveryFileStoreConditions):
            Optional. In addition to matching the filter,
            these conditions must be true before a profile
            is generated.
        generation_cadence (google.cloud.dlp_v2.types.DiscoveryCloudStorageGenerationCadence):
            Optional. How often and when to update
            profiles. New buckets that match both the filter
            and conditions are scanned as quickly as
            possible depending on system capacity.

            This field is a member of `oneof`_ ``cadence``.
        disabled (google.cloud.dlp_v2.types.Disabled):
            Optional. Disable profiling for buckets that
            match this filter.

            This field is a member of `oneof`_ ``cadence``.
    """

    filter: "DiscoveryCloudStorageFilter" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="DiscoveryCloudStorageFilter",
    )
    conditions: "DiscoveryFileStoreConditions" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="DiscoveryFileStoreConditions",
    )
    generation_cadence: "DiscoveryCloudStorageGenerationCadence" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="cadence",
        message="DiscoveryCloudStorageGenerationCadence",
    )
    disabled: "Disabled" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="cadence",
        message="Disabled",
    )


class DiscoveryCloudStorageFilter(proto.Message):
    r"""Determines which buckets will have profiles generated within
    an organization or project. Includes the ability to filter by
    regular expression patterns on project ID and bucket name.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        collection (google.cloud.dlp_v2.types.FileStoreCollection):
            Optional. A specific set of buckets for this
            filter to apply to.

            This field is a member of `oneof`_ ``filter``.
        cloud_storage_resource_reference (google.cloud.dlp_v2.types.CloudStorageResourceReference):
            Optional. The bucket to scan. Targets
            including this can only include one target (the
            target with this bucket). This enables profiling
            the contents of a single bucket, while the other
            options allow for easy profiling of many bucets
            within a project or an organization.

            This field is a member of `oneof`_ ``filter``.
        others (google.cloud.dlp_v2.types.AllOtherResources):
            Optional. Catch-all. This should always be
            the last target in the list because anything
            above it will apply first. Should only appear
            once in a configuration. If none is specified, a
            default one will be added automatically.

            This field is a member of `oneof`_ ``filter``.
    """

    collection: "FileStoreCollection" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="filter",
        message="FileStoreCollection",
    )
    cloud_storage_resource_reference: "CloudStorageResourceReference" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="filter",
        message="CloudStorageResourceReference",
    )
    others: "AllOtherResources" = proto.Field(
        proto.MESSAGE,
        number=100,
        oneof="filter",
        message="AllOtherResources",
    )


class FileStoreCollection(proto.Message):
    r"""Match file stores (e.g. buckets) using filters.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        include_regexes (google.cloud.dlp_v2.types.FileStoreRegexes):
            Optional. A collection of regular expressions
            to match a file store against.

            This field is a member of `oneof`_ ``pattern``.
        include_tags (google.cloud.dlp_v2.types.TagFilters):
            Optional. To be included in the collection, a resource must
            meet all of the following requirements:

            - If tag filters are provided, match all provided tag
              filters.
            - If one or more patterns are specified, match at least one
              pattern.

            For a resource to match the tag filters, the resource must
            have all of the provided tags attached. Tags refer to
            Resource Manager tags bound to the resource or its
            ancestors. For more information, see `Manage
            schedules <https://docs.cloud.google.com/sensitive-data-protection/docs/profile-project-cloud-storage#manage-schedules>`__.
    """

    include_regexes: "FileStoreRegexes" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="pattern",
        message="FileStoreRegexes",
    )
    include_tags: "TagFilters" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="TagFilters",
    )


class FileStoreRegexes(proto.Message):
    r"""A collection of regular expressions to determine what file
    store to match against.

    Attributes:
        patterns (MutableSequence[google.cloud.dlp_v2.types.FileStoreRegex]):
            Required. The group of regular expression
            patterns to match against one or more file
            stores. Maximum of 100 entries. The sum of all
            regular expression's length can't exceed 10 KiB.
    """

    patterns: MutableSequence["FileStoreRegex"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="FileStoreRegex",
    )


class FileStoreRegex(proto.Message):
    r"""A pattern to match against one or more file stores.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        cloud_storage_regex (google.cloud.dlp_v2.types.CloudStorageRegex):
            Optional. Regex for Cloud Storage.

            This field is a member of `oneof`_ ``resource_regex``.
    """

    cloud_storage_regex: "CloudStorageRegex" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="resource_regex",
        message="CloudStorageRegex",
    )


class CloudStorageRegex(proto.Message):
    r"""A pattern to match against one or more file stores. At least one
    pattern must be specified. Regular expressions use RE2
    `syntax <https://github.com/google/re2/wiki/Syntax>`__; a guide can
    be found under the google/re2 repository on GitHub.

    Attributes:
        project_id_regex (str):
            Optional. For organizations, if unset, will
            match all projects.
        bucket_name_regex (str):
            Optional. Regex to test the bucket name
            against. If empty, all buckets match. Example:
            "marketing2021" or "(marketing)\d{4}" will both
            match the bucket gs://marketing2021
    """

    project_id_regex: str = proto.Field(
        proto.STRING,
        number=1,
    )
    bucket_name_regex: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CloudStorageResourceReference(proto.Message):
    r"""Identifies a single Cloud Storage bucket.

    Attributes:
        bucket_name (str):
            Required. The bucket to scan.
        project_id (str):
            Required. If within a project-level config,
            then this must match the config's project id.
    """

    bucket_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DiscoveryCloudStorageGenerationCadence(proto.Message):
    r"""How often existing buckets should have their profiles
    refreshed. New buckets are scanned as quickly as possible
    depending on system capacity.

    Attributes:
        refresh_frequency (google.cloud.dlp_v2.types.DataProfileUpdateFrequency):
            Optional. Data changes in Cloud Storage can't
            trigger reprofiling. If you set this field,
            profiles are refreshed at this frequency
            regardless of whether the underlying buckets
            have changed. Defaults to never.
        inspect_template_modified_cadence (google.cloud.dlp_v2.types.DiscoveryInspectTemplateModifiedCadence):
            Optional. Governs when to update data profiles when the
            inspection rules defined by the ``InspectTemplate`` change.
            If not set, changing the template will not cause a data
            profile to update.
    """

    refresh_frequency: "DataProfileUpdateFrequency" = proto.Field(
        proto.ENUM,
        number=1,
        enum="DataProfileUpdateFrequency",
    )
    inspect_template_modified_cadence: "DiscoveryInspectTemplateModifiedCadence" = (
        proto.Field(
            proto.MESSAGE,
            number=2,
            message="DiscoveryInspectTemplateModifiedCadence",
        )
    )


class DiscoveryCloudStorageConditions(proto.Message):
    r"""Requirements that must be true before a Cloud Storage bucket
    or object is scanned in discovery for the first time. There is
    an AND relationship between the top-level attributes.

    Attributes:
        included_object_attributes (MutableSequence[google.cloud.dlp_v2.types.DiscoveryCloudStorageConditions.CloudStorageObjectAttribute]):
            Required. Only objects with the specified attributes will be
            scanned. If an object has one of the specified attributes
            but is inside an excluded bucket, it will not be scanned.
            Defaults to [ALL_SUPPORTED_OBJECTS]. A profile will be
            created even if no objects match the
            included_object_attributes.
        included_bucket_attributes (MutableSequence[google.cloud.dlp_v2.types.DiscoveryCloudStorageConditions.CloudStorageBucketAttribute]):
            Required. Only objects with the specified attributes will be
            scanned. Defaults to [ALL_SUPPORTED_BUCKETS] if unset.
    """

    class CloudStorageObjectAttribute(proto.Enum):
        r"""The attribute of an object. See
        https://docs.cloud.google.com/storage/docs/storage-classes for
        more information on storage classes.

        Values:
            CLOUD_STORAGE_OBJECT_ATTRIBUTE_UNSPECIFIED (0):
                Unused.
            ALL_SUPPORTED_OBJECTS (1):
                Scan objects regardless of the attribute.
            STANDARD (2):
                Scan objects with the standard storage class.
            NEARLINE (3):
                Scan objects with the nearline storage class.
                This will incur retrieval fees.
            COLDLINE (4):
                Scan objects with the coldline storage class.
                This will incur retrieval fees.
            ARCHIVE (5):
                Scan objects with the archive storage class.
                This will incur retrieval fees.
            REGIONAL (6):
                Scan objects with the regional storage class.
            MULTI_REGIONAL (7):
                Scan objects with the multi-regional storage
                class.
            DURABLE_REDUCED_AVAILABILITY (8):
                Scan objects with the dual-regional storage
                class. This will incur retrieval fees.
        """

        CLOUD_STORAGE_OBJECT_ATTRIBUTE_UNSPECIFIED = 0
        ALL_SUPPORTED_OBJECTS = 1
        STANDARD = 2
        NEARLINE = 3
        COLDLINE = 4
        ARCHIVE = 5
        REGIONAL = 6
        MULTI_REGIONAL = 7
        DURABLE_REDUCED_AVAILABILITY = 8

    class CloudStorageBucketAttribute(proto.Enum):
        r"""The attribute of a bucket.

        Values:
            CLOUD_STORAGE_BUCKET_ATTRIBUTE_UNSPECIFIED (0):
                Unused.
            ALL_SUPPORTED_BUCKETS (1):
                Scan buckets regardless of the attribute.
            AUTOCLASS_DISABLED (2):
                Buckets with
                `Autoclass <https://docs.cloud.google.com/storage/docs/autoclass>`__
                disabled. Only one of AUTOCLASS_DISABLED or
                AUTOCLASS_ENABLED should be set.
            AUTOCLASS_ENABLED (3):
                Buckets with
                `Autoclass <https://docs.cloud.google.com/storage/docs/autoclass>`__
                enabled. Only one of AUTOCLASS_DISABLED or AUTOCLASS_ENABLED
                should be set. Scanning Autoclass-enabled buckets can affect
                object storage classes.
        """

        CLOUD_STORAGE_BUCKET_ATTRIBUTE_UNSPECIFIED = 0
        ALL_SUPPORTED_BUCKETS = 1
        AUTOCLASS_DISABLED = 2
        AUTOCLASS_ENABLED = 3

    included_object_attributes: MutableSequence[CloudStorageObjectAttribute] = (
        proto.RepeatedField(
            proto.ENUM,
            number=1,
            enum=CloudStorageObjectAttribute,
        )
    )
    included_bucket_attributes: MutableSequence[CloudStorageBucketAttribute] = (
        proto.RepeatedField(
            proto.ENUM,
            number=2,
            enum=CloudStorageBucketAttribute,
        )
    )


class DiscoveryFileStoreConditions(proto.Message):
    r"""Requirements that must be true before a file store is scanned
    in discovery for the first time. There is an AND relationship
    between the top-level attributes.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        created_after (google.protobuf.timestamp_pb2.Timestamp):
            Optional. File store must have been created
            after this date. Used to avoid backfilling.
        min_age (google.protobuf.duration_pb2.Duration):
            Optional. Minimum age a file store must have.
            If set, the value must be 1 hour or greater.
        cloud_storage_conditions (google.cloud.dlp_v2.types.DiscoveryCloudStorageConditions):
            Optional. Cloud Storage conditions.

            This field is a member of `oneof`_ ``conditions``.
    """

    created_after: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    min_age: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    cloud_storage_conditions: "DiscoveryCloudStorageConditions" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="conditions",
        message="DiscoveryCloudStorageConditions",
    )


class OtherCloudDiscoveryTarget(proto.Message):
    r"""Target used to match against for discovery of resources from other
    clouds. An `AWS connector in Security Command Center
    (Enterprise <https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws>`__
    is required to use this feature.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        data_source_type (google.cloud.dlp_v2.types.DataSourceType):
            Required. The type of data profiles generated by this
            discovery target. Supported values are:

            - aws/s3/bucket
        filter (google.cloud.dlp_v2.types.DiscoveryOtherCloudFilter):
            Required. The resources that the discovery
            cadence applies to. The first target with a
            matching filter will be the one to apply to a
            resource.
        conditions (google.cloud.dlp_v2.types.DiscoveryOtherCloudConditions):
            Optional. In addition to matching the filter,
            these conditions must be true before a profile
            is generated.
        generation_cadence (google.cloud.dlp_v2.types.DiscoveryOtherCloudGenerationCadence):
            How often and when to update data profiles.
            New resources that match both the filter and
            conditions are scanned as quickly as possible
            depending on system capacity.

            This field is a member of `oneof`_ ``cadence``.
        disabled (google.cloud.dlp_v2.types.Disabled):
            Disable profiling for resources that match
            this filter.

            This field is a member of `oneof`_ ``cadence``.
    """

    data_source_type: "DataSourceType" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="DataSourceType",
    )
    filter: "DiscoveryOtherCloudFilter" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DiscoveryOtherCloudFilter",
    )
    conditions: "DiscoveryOtherCloudConditions" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DiscoveryOtherCloudConditions",
    )
    generation_cadence: "DiscoveryOtherCloudGenerationCadence" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="cadence",
        message="DiscoveryOtherCloudGenerationCadence",
    )
    disabled: "Disabled" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="cadence",
        message="Disabled",
    )


class DiscoveryOtherCloudFilter(proto.Message):
    r"""Determines which resources from the other cloud will have
    profiles generated. Includes the ability to filter by resource
    names.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        collection (google.cloud.dlp_v2.types.OtherCloudResourceCollection):
            A collection of resources for this filter to
            apply to.

            This field is a member of `oneof`_ ``filter``.
        single_resource (google.cloud.dlp_v2.types.OtherCloudSingleResourceReference):
            The resource to scan. Configs using this
            filter can only have one target (the target with
            this single resource reference).

            This field is a member of `oneof`_ ``filter``.
        others (google.cloud.dlp_v2.types.AllOtherResources):
            Optional. Catch-all. This should always be
            the last target in the list because anything
            above it will apply first. Should only appear
            once in a configuration. If none is specified, a
            default one will be added automatically.

            This field is a member of `oneof`_ ``filter``.
    """

    collection: "OtherCloudResourceCollection" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="filter",
        message="OtherCloudResourceCollection",
    )
    single_resource: "OtherCloudSingleResourceReference" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="filter",
        message="OtherCloudSingleResourceReference",
    )
    others: "AllOtherResources" = proto.Field(
        proto.MESSAGE,
        number=100,
        oneof="filter",
        message="AllOtherResources",
    )


class OtherCloudResourceCollection(proto.Message):
    r"""Match resources using regex filters.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        include_regexes (google.cloud.dlp_v2.types.OtherCloudResourceRegexes):
            A collection of regular expressions to match
            a resource against.

            This field is a member of `oneof`_ ``pattern``.
    """

    include_regexes: "OtherCloudResourceRegexes" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="pattern",
        message="OtherCloudResourceRegexes",
    )


class OtherCloudResourceRegexes(proto.Message):
    r"""A collection of regular expressions to determine what
    resources to match against.

    Attributes:
        patterns (MutableSequence[google.cloud.dlp_v2.types.OtherCloudResourceRegex]):
            A group of regular expression patterns to
            match against one or more resources.
            Maximum of 100 entries. The sum of all regular
            expression's length can't exceed 10 KiB.
    """

    patterns: MutableSequence["OtherCloudResourceRegex"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="OtherCloudResourceRegex",
    )


class OtherCloudResourceRegex(proto.Message):
    r"""A pattern to match against one or more resources. At least one
    pattern must be specified. Regular expressions use RE2
    `syntax <https://github.com/google/re2/wiki/Syntax>`__; a guide can
    be found under the google/re2 repository on GitHub.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        amazon_s3_bucket_regex (google.cloud.dlp_v2.types.AmazonS3BucketRegex):
            Regex for Amazon S3 buckets.

            This field is a member of `oneof`_ ``resource_regex``.
    """

    amazon_s3_bucket_regex: "AmazonS3BucketRegex" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="resource_regex",
        message="AmazonS3BucketRegex",
    )


class AwsAccountRegex(proto.Message):
    r"""AWS account regex.

    Attributes:
        account_id_regex (str):
            Optional. Regex to test the AWS account ID
            against. If empty, all accounts match.
    """

    account_id_regex: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AmazonS3BucketRegex(proto.Message):
    r"""Amazon S3 bucket regex.

    Attributes:
        aws_account_regex (google.cloud.dlp_v2.types.AwsAccountRegex):
            The AWS account regex.
        bucket_name_regex (str):
            Optional. Regex to test the bucket name
            against. If empty, all buckets match.
    """

    aws_account_regex: "AwsAccountRegex" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="AwsAccountRegex",
    )
    bucket_name_regex: str = proto.Field(
        proto.STRING,
        number=2,
    )


class OtherCloudSingleResourceReference(proto.Message):
    r"""Identifies a single resource, like a single Amazon S3 bucket.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        amazon_s3_bucket (google.cloud.dlp_v2.types.AmazonS3Bucket):
            Amazon S3 bucket.

            This field is a member of `oneof`_ ``resource``.
    """

    amazon_s3_bucket: "AmazonS3Bucket" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="resource",
        message="AmazonS3Bucket",
    )


class AwsAccount(proto.Message):
    r"""AWS account.

    Attributes:
        account_id (str):
            Required. AWS account ID.
    """

    account_id: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AmazonS3Bucket(proto.Message):
    r"""Amazon S3 bucket.

    Attributes:
        aws_account (google.cloud.dlp_v2.types.AwsAccount):
            The AWS account.
        bucket_name (str):
            Required. The bucket name.
    """

    aws_account: "AwsAccount" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="AwsAccount",
    )
    bucket_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DiscoveryOtherCloudConditions(proto.Message):
    r"""Requirements that must be true before a resource is profiled
    for the first time.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        min_age (google.protobuf.duration_pb2.Duration):
            Minimum age a resource must be before Cloud
            DLP can profile it. Value must be 1 hour or
            greater.
        amazon_s3_bucket_conditions (google.cloud.dlp_v2.types.AmazonS3BucketConditions):
            Amazon S3 bucket conditions.

            This field is a member of `oneof`_ ``conditions``.
    """

    min_age: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )
    amazon_s3_bucket_conditions: "AmazonS3BucketConditions" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="conditions",
        message="AmazonS3BucketConditions",
    )


class AmazonS3BucketConditions(proto.Message):
    r"""Amazon S3 bucket conditions.

    Attributes:
        bucket_types (MutableSequence[google.cloud.dlp_v2.types.AmazonS3BucketConditions.BucketType]):
            Optional. Bucket types that should be profiled. Optional.
            Defaults to TYPE_ALL_SUPPORTED if unspecified.
        object_storage_classes (MutableSequence[google.cloud.dlp_v2.types.AmazonS3BucketConditions.ObjectStorageClass]):
            Optional. Object classes that should be profiled. Optional.
            Defaults to ALL_SUPPORTED_CLASSES if unspecified.
    """

    class BucketType(proto.Enum):
        r"""Supported Amazon S3 bucket types. Defaults to TYPE_ALL_SUPPORTED.

        Values:
            TYPE_UNSPECIFIED (0):
                Unused.
            TYPE_ALL_SUPPORTED (1):
                All supported classes.
            TYPE_GENERAL_PURPOSE (2):
                A general purpose Amazon S3 bucket.
        """

        TYPE_UNSPECIFIED = 0
        TYPE_ALL_SUPPORTED = 1
        TYPE_GENERAL_PURPOSE = 2

    class ObjectStorageClass(proto.Enum):
        r"""Supported Amazon S3 object storage classes. Defaults to
        ALL_SUPPORTED_CLASSES.

        Values:
            UNSPECIFIED (0):
                Unused.
            ALL_SUPPORTED_CLASSES (1):
                All supported classes.
            STANDARD (2):
                Standard object class.
            STANDARD_INFREQUENT_ACCESS (4):
                Standard - infrequent access object class.
            GLACIER_INSTANT_RETRIEVAL (6):
                Glacier - instant retrieval object class.
            INTELLIGENT_TIERING (7):
                Objects in the S3 Intelligent-Tiering access
                tiers.
        """

        UNSPECIFIED = 0
        ALL_SUPPORTED_CLASSES = 1
        STANDARD = 2
        STANDARD_INFREQUENT_ACCESS = 4
        GLACIER_INSTANT_RETRIEVAL = 6
        INTELLIGENT_TIERING = 7

    bucket_types: MutableSequence[BucketType] = proto.RepeatedField(
        proto.ENUM,
        number=1,
        enum=BucketType,
    )
    object_storage_classes: MutableSequence[ObjectStorageClass] = proto.RepeatedField(
        proto.ENUM,
        number=2,
        enum=ObjectStorageClass,
    )


class DiscoveryOtherCloudGenerationCadence(proto.Message):
    r"""How often existing resources should have their profiles
    refreshed. New resources are scanned as quickly as possible
    depending on system capacity.

    Attributes:
        refresh_frequency (google.cloud.dlp_v2.types.DataProfileUpdateFrequency):
            Optional. Frequency to update profiles
            regardless of whether the underlying resource
            has changes. Defaults to never.
        inspect_template_modified_cadence (google.cloud.dlp_v2.types.DiscoveryInspectTemplateModifiedCadence):
            Optional. Governs when to update data profiles when the
            inspection rules defined by the ``InspectTemplate`` change.
            If not set, changing the template will not cause a data
            profile to update.
    """

    refresh_frequency: "DataProfileUpdateFrequency" = proto.Field(
        proto.ENUM,
        number=1,
        enum="DataProfileUpdateFrequency",
    )
    inspect_template_modified_cadence: "DiscoveryInspectTemplateModifiedCadence" = (
        proto.Field(
            proto.MESSAGE,
            number=2,
            message="DiscoveryInspectTemplateModifiedCadence",
        )
    )


class DiscoveryStartingLocation(proto.Message):
    r"""The location to begin a discovery scan. Denotes an
    organization ID or folder ID within an organization.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        organization_id (int):
            The ID of an organization to scan.

            This field is a member of `oneof`_ ``location``.
        folder_id (int):
            The ID of the folder within an organization
            to be scanned.

            This field is a member of `oneof`_ ``location``.
    """

    organization_id: int = proto.Field(
        proto.INT64,
        number=1,
        oneof="location",
    )
    folder_id: int = proto.Field(
        proto.INT64,
        number=2,
        oneof="location",
    )


class OtherCloudDiscoveryStartingLocation(proto.Message):
    r"""The other cloud starting location for discovery.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        aws_location (google.cloud.dlp_v2.types.OtherCloudDiscoveryStartingLocation.AwsDiscoveryStartingLocation):
            The AWS starting location for discovery.

            This field is a member of `oneof`_ ``location``.
    """

    class AwsDiscoveryStartingLocation(proto.Message):
        r"""The AWS starting location for discovery.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            account_id (str):
                The AWS account ID that this discovery config applies to.
                Within an AWS organization, you can find the AWS account ID
                inside an AWS account ARN. Example:
                arn:{partition}:organizations::{management_account_id}:account/{org_id}/{account_id}

                This field is a member of `oneof`_ ``scope``.
            all_asset_inventory_assets (bool):
                All AWS assets stored in Asset Inventory that
                didn't match other AWS discovery configs.

                This field is a member of `oneof`_ ``scope``.
        """

        account_id: str = proto.Field(
            proto.STRING,
            number=2,
            oneof="scope",
        )
        all_asset_inventory_assets: bool = proto.Field(
            proto.BOOL,
            number=3,
            oneof="scope",
        )

    aws_location: AwsDiscoveryStartingLocation = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="location",
        message=AwsDiscoveryStartingLocation,
    )


class AllOtherResources(proto.Message):
    r"""Match discovery resources not covered by any other filter."""


class VertexDatasetDiscoveryTarget(proto.Message):
    r"""Target used to match against for discovery with Vertex AI
    datasets.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        filter (google.cloud.dlp_v2.types.DiscoveryVertexDatasetFilter):
            Required. The datasets the discovery cadence
            applies to. The first target with a matching
            filter will be the one to apply to a dataset.
        conditions (google.cloud.dlp_v2.types.DiscoveryVertexDatasetConditions):
            In addition to matching the filter, these
            conditions must be true before a profile is
            generated.
        generation_cadence (google.cloud.dlp_v2.types.DiscoveryVertexDatasetGenerationCadence):
            How often and when to update profiles. New
            datasets that match both the filter and
            conditions are scanned as quickly as possible
            depending on system capacity.

            This field is a member of `oneof`_ ``cadence``.
        disabled (google.cloud.dlp_v2.types.Disabled):
            Disable profiling for datasets that match
            this filter.

            This field is a member of `oneof`_ ``cadence``.
    """

    filter: "DiscoveryVertexDatasetFilter" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="DiscoveryVertexDatasetFilter",
    )
    conditions: "DiscoveryVertexDatasetConditions" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DiscoveryVertexDatasetConditions",
    )
    generation_cadence: "DiscoveryVertexDatasetGenerationCadence" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="cadence",
        message="DiscoveryVertexDatasetGenerationCadence",
    )
    disabled: "Disabled" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="cadence",
        message="Disabled",
    )


class DiscoveryVertexDatasetFilter(proto.Message):
    r"""Determines what datasets will have profiles generated within
    an organization or project. Includes the ability to filter by
    regular expression patterns on project ID or dataset regex.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        collection (google.cloud.dlp_v2.types.VertexDatasetCollection):
            A specific set of Vertex AI datasets for this
            filter to apply to.

            This field is a member of `oneof`_ ``filter``.
        vertex_dataset_resource_reference (google.cloud.dlp_v2.types.VertexDatasetResourceReference):
            The dataset resource to scan. Targets
            including this can only include one target (the
            target with this dataset resource reference).

            This field is a member of `oneof`_ ``filter``.
        others (google.cloud.dlp_v2.types.AllOtherResources):
            Catch-all. This should always be the last
            target in the list because anything above it
            will apply first. Should only appear once in a
            configuration. If none is specified, a default
            one will be added automatically.

            This field is a member of `oneof`_ ``filter``.
    """

    collection: "VertexDatasetCollection" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="filter",
        message="VertexDatasetCollection",
    )
    vertex_dataset_resource_reference: "VertexDatasetResourceReference" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="filter",
        message="VertexDatasetResourceReference",
    )
    others: "AllOtherResources" = proto.Field(
        proto.MESSAGE,
        number=100,
        oneof="filter",
        message="AllOtherResources",
    )


class VertexDatasetCollection(proto.Message):
    r"""Match dataset resources using regex filters.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        vertex_dataset_regexes (google.cloud.dlp_v2.types.VertexDatasetRegexes):
            The regex used to filter dataset resources.

            This field is a member of `oneof`_ ``pattern``.
    """

    vertex_dataset_regexes: "VertexDatasetRegexes" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="pattern",
        message="VertexDatasetRegexes",
    )


class VertexDatasetRegexes(proto.Message):
    r"""A collection of regular expressions to determine what
    datasets to match against.

    Attributes:
        patterns (MutableSequence[google.cloud.dlp_v2.types.VertexDatasetRegex]):
            Required. The group of regular expression
            patterns to match against one or more datasets.
            Maximum of 100 entries. The sum of the lengths
            of all regular expressions can't exceed 10 KiB.
    """

    patterns: MutableSequence["VertexDatasetRegex"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="VertexDatasetRegex",
    )


class VertexDatasetRegex(proto.Message):
    r"""A pattern to match against one or more dataset resources.

    Attributes:
        project_id_regex (str):
            For organizations, if unset, will match all
            projects. Has no effect for configurations
            created within a project.
    """

    project_id_regex: str = proto.Field(
        proto.STRING,
        number=1,
    )


class VertexDatasetResourceReference(proto.Message):
    r"""Identifies a single Vertex AI resource. Only datasets are
    supported.

    Attributes:
        dataset_resource_name (str):
            Required. The name of the Vertex AI resource. If set within
            a project-level configuration, the specified resource must
            be within the project. Examples:

            - ``projects/{project}/locations/{location}/datasets/{dataset}``
    """

    dataset_resource_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DiscoveryVertexDatasetConditions(proto.Message):
    r"""Requirements that must be true before a dataset is profiled
    for the first time.

    Attributes:
        created_after (google.protobuf.timestamp_pb2.Timestamp):
            Vertex AI dataset must have been created
            after this date. Used to avoid backfilling.
        min_age (google.protobuf.duration_pb2.Duration):
            Minimum age a Vertex AI dataset must have. If
            set, the value must be 1 hour or greater.
    """

    created_after: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    min_age: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )


class DiscoveryVertexDatasetGenerationCadence(proto.Message):
    r"""How often existing datasets should have their profiles
    refreshed. New datasets are scanned as quickly as possible
    depending on system capacity.

    Attributes:
        refresh_frequency (google.cloud.dlp_v2.types.DataProfileUpdateFrequency):
            If you set this field, profiles are refreshed
            at this frequency regardless of whether the
            underlying datasets have changed. Defaults to
            never.
        inspect_template_modified_cadence (google.cloud.dlp_v2.types.DiscoveryInspectTemplateModifiedCadence):
            Governs when to update data profiles when the inspection
            rules defined by the ``InspectTemplate`` change. If not set,
            changing the template will not cause a data profile to be
            updated.
    """

    refresh_frequency: "DataProfileUpdateFrequency" = proto.Field(
        proto.ENUM,
        number=1,
        enum="DataProfileUpdateFrequency",
    )
    inspect_template_modified_cadence: "DiscoveryInspectTemplateModifiedCadence" = (
        proto.Field(
            proto.MESSAGE,
            number=2,
            message="DiscoveryInspectTemplateModifiedCadence",
        )
    )


class DlpJob(proto.Message):
    r"""Combines all of the information about a DLP job.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. The server-assigned name.
        type_ (google.cloud.dlp_v2.types.DlpJobType):
            The type of job.
        state (google.cloud.dlp_v2.types.DlpJob.JobState):
            Output only. State of a job.
        risk_details (google.cloud.dlp_v2.types.AnalyzeDataSourceRiskDetails):
            Results from analyzing risk of a data source.

            This field is a member of `oneof`_ ``details``.
        inspect_details (google.cloud.dlp_v2.types.InspectDataSourceDetails):
            Results from inspecting a data source.

            This field is a member of `oneof`_ ``details``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the job was created.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the job started.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the job finished.
        last_modified (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the job was last
            modified by the system.
        job_trigger_name (str):
            Output only. If created by a job trigger, the
            resource name of the trigger that instantiated
            the job.
        errors (MutableSequence[google.cloud.dlp_v2.types.Error]):
            Output only. A stream of errors encountered
            running the job.
        action_details (MutableSequence[google.cloud.dlp_v2.types.ActionDetails]):
            Output only. Events that should occur after
            the job has completed.
    """

    class JobState(proto.Enum):
        r"""Possible states of a job. New items may be added.

        Values:
            JOB_STATE_UNSPECIFIED (0):
                Unused.
            PENDING (1):
                The job has not yet started.
            RUNNING (2):
                The job is currently running. Once a job has
                finished it will transition to FAILED or DONE.
            DONE (3):
                The job is no longer running.
            CANCELED (4):
                The job was canceled before it could be
                completed.
            FAILED (5):
                The job had an error and did not complete.
            ACTIVE (6):
                The job is currently accepting findings via
                hybridInspect. A hybrid job in ACTIVE state may
                continue to have findings added to it through
                the calling of hybridInspect. After the job has
                finished no more calls to hybridInspect may be
                made. ACTIVE jobs can transition to DONE.
        """

        JOB_STATE_UNSPECIFIED = 0
        PENDING = 1
        RUNNING = 2
        DONE = 3
        CANCELED = 4
        FAILED = 5
        ACTIVE = 6

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: "DlpJobType" = proto.Field(
        proto.ENUM,
        number=2,
        enum="DlpJobType",
    )
    state: JobState = proto.Field(
        proto.ENUM,
        number=3,
        enum=JobState,
    )
    risk_details: "AnalyzeDataSourceRiskDetails" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="details",
        message="AnalyzeDataSourceRiskDetails",
    )
    inspect_details: "InspectDataSourceDetails" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="details",
        message="InspectDataSourceDetails",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    last_modified: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=15,
        message=timestamp_pb2.Timestamp,
    )
    job_trigger_name: str = proto.Field(
        proto.STRING,
        number=10,
    )
    errors: MutableSequence["Error"] = proto.RepeatedField(
        proto.MESSAGE,
        number=11,
        message="Error",
    )
    action_details: MutableSequence["ActionDetails"] = proto.RepeatedField(
        proto.MESSAGE,
        number=12,
        message="ActionDetails",
    )


class GetDlpJobRequest(proto.Message):
    r"""The request message for
    [GetDlpJob][google.privacy.dlp.v2.DlpService.GetDlpJob].

    Attributes:
        name (str):
            Required. The name of the DlpJob resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDlpJobsRequest(proto.Message):
    r"""The request message for listing DLP jobs.

    Attributes:
        parent (str):
            Required. Parent resource name.

            The format of this value varies depending on whether you
            have `specified a processing
            location <https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location>`__:

            - Projects scope, location specified:
              ``projects/{project_id}/locations/{location_id}``
            - Projects scope, no location specified (defaults to
              global): ``projects/{project_id}``

            The following example ``parent`` string specifies a parent
            project with the identifier ``example-project``, and
            specifies the ``europe-west3`` location for processing data:

            ::

                parent=projects/example-project/locations/europe-west3
        filter (str):
            Allows filtering.

            Supported syntax:

            - Filter expressions are made up of one or more
              restrictions.
            - Restrictions can be combined by ``AND`` or ``OR`` logical
              operators. A sequence of restrictions implicitly uses
              ``AND``.
            - A restriction has the form of
              ``{field} {operator} {value}``.
            - Supported fields/values for inspect jobs:

              - ``state`` - PENDING|RUNNING|CANCELED|FINISHED|FAILED
              - ``inspected_storage`` - DATASTORE|CLOUD_STORAGE|BIGQUERY
              - ``trigger_name`` - The name of the trigger that created
                the job.
              - 'end_time\` - Corresponds to the time the job finished.
              - 'start_time\` - Corresponds to the time the job
                finished.

            - Supported fields for risk analysis jobs:

              - ``state`` - RUNNING|CANCELED|FINISHED|FAILED
              - 'end_time\` - Corresponds to the time the job finished.
              - 'start_time\` - Corresponds to the time the job
                finished.

            - The operator must be ``=`` or ``!=``.

            The syntax is based on https://google.aip.dev/160.

            Examples:

            - inspected_storage = cloud_storage AND state = done
            - inspected_storage = cloud_storage OR inspected_storage =
              bigquery
            - inspected_storage = cloud_storage AND (state = done OR
              state = canceled)
            - end_time > "2017-12-12T00:00:00+00:00"

            The length of this field should be no more than 500
            characters.
        page_size (int):
            The standard list page size.
        page_token (str):
            The standard list page token.
        type_ (google.cloud.dlp_v2.types.DlpJobType):
            The type of job. Defaults to ``DlpJobType.INSPECT``
        order_by (str):
            Comma-separated list of fields to order by, followed by
            ``asc`` or ``desc`` postfix. This list is case insensitive.
            The default sorting order is ascending. Redundant space
            characters are insignificant.

            Example: ``name asc, end_time asc, create_time desc``

            Supported fields are:

            - ``create_time``: corresponds to the time the job was
              created.
            - ``end_time``: corresponds to the time the job ended.
            - ``name``: corresponds to the job's name.
            - ``state``: corresponds to ``state``
        location_id (str):
            Deprecated. This field has no effect.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=4,
    )
    filter: str = proto.Field(
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
    type_: "DlpJobType" = proto.Field(
        proto.ENUM,
        number=5,
        enum="DlpJobType",
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=6,
    )
    location_id: str = proto.Field(
        proto.STRING,
        number=7,
    )


class ListDlpJobsResponse(proto.Message):
    r"""The response message for listing DLP jobs.

    Attributes:
        jobs (MutableSequence[google.cloud.dlp_v2.types.DlpJob]):
            A list of DlpJobs that matches the specified
            filter in the request.
        next_page_token (str):
            The standard List next-page token.
    """

    @property
    def raw_page(self):
        return self

    jobs: MutableSequence["DlpJob"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DlpJob",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CancelDlpJobRequest(proto.Message):
    r"""The request message for canceling a DLP job.

    Attributes:
        name (str):
            Required. The name of the DlpJob resource to
            be cancelled.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FinishDlpJobRequest(proto.Message):
    r"""The request message for finishing a DLP hybrid job.

    Attributes:
        name (str):
            Required. The name of the DlpJob resource to
            be finished.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteDlpJobRequest(proto.Message):
    r"""The request message for deleting a DLP job.

    Attributes:
        name (str):
            Required. The name of the DlpJob resource to
            be deleted.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateDeidentifyTemplateRequest(proto.Message):
    r"""Request message for CreateDeidentifyTemplate.

    Attributes:
        parent (str):
            Required. Parent resource name.

            The format of this value varies depending on the scope of
            the request (project or organization) and whether you have
            `specified a processing
            location <https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location>`__:

            - Projects scope, location specified:
              ``projects/{project_id}/locations/{location_id}``
            - Projects scope, no location specified (defaults to
              global): ``projects/{project_id}``
            - Organizations scope, location specified:
              ``organizations/{org_id}/locations/{location_id}``
            - Organizations scope, no location specified (defaults to
              global): ``organizations/{org_id}``

            The following example ``parent`` string specifies a parent
            project with the identifier ``example-project``, and
            specifies the ``europe-west3`` location for processing data:

            ::

                parent=projects/example-project/locations/europe-west3
        deidentify_template (google.cloud.dlp_v2.types.DeidentifyTemplate):
            Required. The DeidentifyTemplate to create.
        template_id (str):
            The template id can contain uppercase and lowercase letters,
            numbers, and hyphens; that is, it must match the regular
            expression: ``[a-zA-Z\d-_]+``. The maximum length is 100
            characters. Can be empty to allow the system to generate
            one.
        location_id (str):
            Deprecated. This field has no effect.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    deidentify_template: "DeidentifyTemplate" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DeidentifyTemplate",
    )
    template_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    location_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateDeidentifyTemplateRequest(proto.Message):
    r"""Request message for UpdateDeidentifyTemplate.

    Attributes:
        name (str):
            Required. Resource name of organization and deidentify
            template to be updated, for example
            ``organizations/433245324/deidentifyTemplates/432452342`` or
            projects/project-id/deidentifyTemplates/432452342.
        deidentify_template (google.cloud.dlp_v2.types.DeidentifyTemplate):
            New DeidentifyTemplate value.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Mask to control which fields get updated.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    deidentify_template: "DeidentifyTemplate" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DeidentifyTemplate",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


class GetDeidentifyTemplateRequest(proto.Message):
    r"""Request message for GetDeidentifyTemplate.

    Attributes:
        name (str):
            Required. Resource name of the organization and deidentify
            template to be read, for example
            ``organizations/433245324/deidentifyTemplates/432452342`` or
            projects/project-id/deidentifyTemplates/432452342.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDeidentifyTemplatesRequest(proto.Message):
    r"""Request message for ListDeidentifyTemplates.

    Attributes:
        parent (str):
            Required. Parent resource name.

            The format of this value varies depending on the scope of
            the request (project or organization) and whether you have
            `specified a processing
            location <https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location>`__:

            - Projects scope, location specified:
              ``projects/{project_id}/locations/{location_id}``
            - Projects scope, no location specified (defaults to
              global): ``projects/{project_id}``
            - Organizations scope, location specified:
              ``organizations/{org_id}/locations/{location_id}``
            - Organizations scope, no location specified (defaults to
              global): ``organizations/{org_id}``

            The following example ``parent`` string specifies a parent
            project with the identifier ``example-project``, and
            specifies the ``europe-west3`` location for processing data:

            ::

                parent=projects/example-project/locations/europe-west3
        page_token (str):
            Page token to continue retrieval. Comes from the previous
            call to ``ListDeidentifyTemplates``.
        page_size (int):
            Size of the page. This value can be limited
            by the server. If zero server returns a page of
            max size 100.
        order_by (str):
            Comma-separated list of fields to order by, followed by
            ``asc`` or ``desc`` postfix. This list is case insensitive.
            The default sorting order is ascending. Redundant space
            characters are insignificant.

            Example: ``name asc,update_time, create_time desc``

            Supported fields are:

            - ``create_time``: corresponds to the time the template was
              created.
            - ``update_time``: corresponds to the time the template was
              last updated.
            - ``name``: corresponds to the template's name.
            - ``display_name``: corresponds to the template's display
              name.
        location_id (str):
            Deprecated. This field has no effect.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=4,
    )
    location_id: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListDeidentifyTemplatesResponse(proto.Message):
    r"""Response message for ListDeidentifyTemplates.

    Attributes:
        deidentify_templates (MutableSequence[google.cloud.dlp_v2.types.DeidentifyTemplate]):
            List of deidentify templates, up to page_size in
            ListDeidentifyTemplatesRequest.
        next_page_token (str):
            If the next page is available then the next
            page token to be used in the following
            ListDeidentifyTemplates request.
    """

    @property
    def raw_page(self):
        return self

    deidentify_templates: MutableSequence["DeidentifyTemplate"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DeidentifyTemplate",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteDeidentifyTemplateRequest(proto.Message):
    r"""Request message for DeleteDeidentifyTemplate.

    Attributes:
        name (str):
            Required. Resource name of the organization and deidentify
            template to be deleted, for example
            ``organizations/433245324/deidentifyTemplates/432452342`` or
            projects/project-id/deidentifyTemplates/432452342.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class LargeCustomDictionaryConfig(proto.Message):
    r"""Configuration for a custom dictionary created from a data source of
    any size up to the maximum size defined in the
    `limits <https://docs.cloud.google.com/sensitive-data-protection/limits>`__
    page. The artifacts of dictionary creation are stored in the
    specified Cloud Storage location. Consider using
    ``CustomInfoType.Dictionary`` for smaller dictionaries that satisfy
    the size requirements.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        output_path (google.cloud.dlp_v2.types.CloudStoragePath):
            Location to store dictionary artifacts in
            Cloud Storage. These files will only be
            accessible by project owners and the DLP API. If
            any of these artifacts are modified, the
            dictionary is considered invalid and can no
            longer be used.
        cloud_storage_file_set (google.cloud.dlp_v2.types.CloudStorageFileSet):
            Set of files containing newline-delimited
            lists of dictionary phrases.

            This field is a member of `oneof`_ ``source``.
        big_query_field (google.cloud.dlp_v2.types.BigQueryField):
            Field in a BigQuery table where each cell
            represents a dictionary phrase.

            This field is a member of `oneof`_ ``source``.
    """

    output_path: storage.CloudStoragePath = proto.Field(
        proto.MESSAGE,
        number=1,
        message=storage.CloudStoragePath,
    )
    cloud_storage_file_set: storage.CloudStorageFileSet = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="source",
        message=storage.CloudStorageFileSet,
    )
    big_query_field: storage.BigQueryField = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="source",
        message=storage.BigQueryField,
    )


class LargeCustomDictionaryStats(proto.Message):
    r"""Summary statistics of a custom dictionary.

    Attributes:
        approx_num_phrases (int):
            Approximate number of distinct phrases in the
            dictionary.
    """

    approx_num_phrases: int = proto.Field(
        proto.INT64,
        number=1,
    )


class StoredInfoTypeConfig(proto.Message):
    r"""Configuration for stored infoTypes. All fields and subfield
    are provided by the user. For more information, see
    https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        display_name (str):
            Display name of the StoredInfoType (max 256
            characters).
        description (str):
            Description of the StoredInfoType (max 256
            characters).
        large_custom_dictionary (google.cloud.dlp_v2.types.LargeCustomDictionaryConfig):
            StoredInfoType where findings are defined by
            a dictionary of phrases.

            This field is a member of `oneof`_ ``type``.
        dictionary (google.cloud.dlp_v2.types.CustomInfoType.Dictionary):
            Store dictionary-based CustomInfoType.

            This field is a member of `oneof`_ ``type``.
        regex (google.cloud.dlp_v2.types.CustomInfoType.Regex):
            Store regular expression-based
            StoredInfoType.

            This field is a member of `oneof`_ ``type``.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    large_custom_dictionary: "LargeCustomDictionaryConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="type",
        message="LargeCustomDictionaryConfig",
    )
    dictionary: storage.CustomInfoType.Dictionary = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="type",
        message=storage.CustomInfoType.Dictionary,
    )
    regex: storage.CustomInfoType.Regex = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="type",
        message=storage.CustomInfoType.Regex,
    )


class StoredInfoTypeStats(proto.Message):
    r"""Statistics for a StoredInfoType.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        large_custom_dictionary (google.cloud.dlp_v2.types.LargeCustomDictionaryStats):
            StoredInfoType where findings are defined by
            a dictionary of phrases.

            This field is a member of `oneof`_ ``type``.
    """

    large_custom_dictionary: "LargeCustomDictionaryStats" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="type",
        message="LargeCustomDictionaryStats",
    )


class StoredInfoTypeVersion(proto.Message):
    r"""Version of a StoredInfoType, including the configuration used
    to build it, create timestamp, and current state.

    Attributes:
        config (google.cloud.dlp_v2.types.StoredInfoTypeConfig):
            StoredInfoType configuration.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create timestamp of the version.
            Read-only, determined by the system when the
            version is created.
        state (google.cloud.dlp_v2.types.StoredInfoTypeState):
            Output only. Stored info type version state.
            Read-only, updated by the system during
            dictionary creation.
        errors (MutableSequence[google.cloud.dlp_v2.types.Error]):
            Output only. Errors that occurred when creating this
            storedInfoType version, or anomalies detected in the
            storedInfoType data that render it unusable. Only the five
            most recent errors will be displayed, with the most recent
            error appearing first.

            For example, some of the data for stored custom dictionaries
            is put in the user's Cloud Storage bucket, and if this data
            is modified or deleted by the user or another system, the
            dictionary becomes invalid.

            If any errors occur, fix the problem indicated by the error
            message and use the UpdateStoredInfoType API method to
            create another version of the storedInfoType to continue
            using it, reusing the same ``config`` if it was not the
            source of the error.
        stats (google.cloud.dlp_v2.types.StoredInfoTypeStats):
            Output only. Statistics about this
            storedInfoType version.
    """

    config: "StoredInfoTypeConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="StoredInfoTypeConfig",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    state: "StoredInfoTypeState" = proto.Field(
        proto.ENUM,
        number=3,
        enum="StoredInfoTypeState",
    )
    errors: MutableSequence["Error"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="Error",
    )
    stats: "StoredInfoTypeStats" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="StoredInfoTypeStats",
    )


class StoredInfoType(proto.Message):
    r"""StoredInfoType resource message that contains information
    about the current version and any pending updates.

    Attributes:
        name (str):
            Output only. Resource name.
        current_version (google.cloud.dlp_v2.types.StoredInfoTypeVersion):
            Current version of the stored info type.
        pending_versions (MutableSequence[google.cloud.dlp_v2.types.StoredInfoTypeVersion]):
            Pending versions of the stored info type.
            Empty if no versions are pending.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    current_version: "StoredInfoTypeVersion" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="StoredInfoTypeVersion",
    )
    pending_versions: MutableSequence["StoredInfoTypeVersion"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="StoredInfoTypeVersion",
    )


class CreateStoredInfoTypeRequest(proto.Message):
    r"""Request message for CreateStoredInfoType.

    Attributes:
        parent (str):
            Required. Parent resource name.

            The format of this value varies depending on the scope of
            the request (project or organization) and whether you have
            `specified a processing
            location <https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location>`__:

            - Projects scope, location specified:
              ``projects/{project_id}/locations/{location_id}``
            - Projects scope, no location specified (defaults to
              global): ``projects/{project_id}``
            - Organizations scope, location specified:
              ``organizations/{org_id}/locations/{location_id}``
            - Organizations scope, no location specified (defaults to
              global): ``organizations/{org_id}``

            The following example ``parent`` string specifies a parent
            project with the identifier ``example-project``, and
            specifies the ``europe-west3`` location for processing data:

            ::

                parent=projects/example-project/locations/europe-west3
        config (google.cloud.dlp_v2.types.StoredInfoTypeConfig):
            Required. Configuration of the storedInfoType
            to create.
        stored_info_type_id (str):
            The storedInfoType ID can contain uppercase and lowercase
            letters, numbers, and hyphens; that is, it must match the
            regular expression: ``[a-zA-Z\d-_]+``. The maximum length is
            100 characters. Can be empty to allow the system to generate
            one.
        location_id (str):
            Deprecated. This field has no effect.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    config: "StoredInfoTypeConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="StoredInfoTypeConfig",
    )
    stored_info_type_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    location_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateStoredInfoTypeRequest(proto.Message):
    r"""Request message for UpdateStoredInfoType.

    Attributes:
        name (str):
            Required. Resource name of organization and storedInfoType
            to be updated, for example
            ``organizations/433245324/storedInfoTypes/432452342`` or
            projects/project-id/storedInfoTypes/432452342.
        config (google.cloud.dlp_v2.types.StoredInfoTypeConfig):
            Updated configuration for the storedInfoType.
            If not provided, a new version of the
            storedInfoType will be created with the existing
            configuration.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Mask to control which fields get updated.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    config: "StoredInfoTypeConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="StoredInfoTypeConfig",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


class GetStoredInfoTypeRequest(proto.Message):
    r"""Request message for GetStoredInfoType.

    Attributes:
        name (str):
            Required. Resource name of the organization and
            storedInfoType to be read, for example
            ``organizations/433245324/storedInfoTypes/432452342`` or
            projects/project-id/storedInfoTypes/432452342.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListStoredInfoTypesRequest(proto.Message):
    r"""Request message for ListStoredInfoTypes.

    Attributes:
        parent (str):
            Required. Parent resource name.

            The format of this value varies depending on the scope of
            the request (project or organization) and whether you have
            `specified a processing
            location <https://docs.cloud.google.com/sensitive-data-protection/docs/specifying-location>`__:

            - Projects scope, location specified:
              ``projects/{project_id}/locations/{location_id}``
            - Projects scope, no location specified (defaults to
              global): ``projects/{project_id}``

            The following example ``parent`` string specifies a parent
            project with the identifier ``example-project``, and
            specifies the ``europe-west3`` location for processing data:

            ::

                parent=projects/example-project/locations/europe-west3
        page_token (str):
            Page token to continue retrieval. Comes from the previous
            call to ``ListStoredInfoTypes``.
        page_size (int):
            Size of the page. This value can be limited
            by the server. If zero server returns a page of
            max size 100.
        order_by (str):
            Comma-separated list of fields to order by, followed by
            ``asc`` or ``desc`` postfix. This list is case insensitive.
            The default sorting order is ascending. Redundant space
            characters are insignificant.

            Example: ``name asc, display_name, create_time desc``

            Supported fields are:

            - ``create_time``: corresponds to the time the most recent
              version of the resource was created.
            - ``state``: corresponds to the state of the resource.
            - ``name``: corresponds to resource name.
            - ``display_name``: corresponds to info type's display name.
        location_id (str):
            Deprecated. This field has no effect.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=4,
    )
    location_id: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListStoredInfoTypesResponse(proto.Message):
    r"""Response message for ListStoredInfoTypes.

    Attributes:
        stored_info_types (MutableSequence[google.cloud.dlp_v2.types.StoredInfoType]):
            List of storedInfoTypes, up to page_size in
            ListStoredInfoTypesRequest.
        next_page_token (str):
            If the next page is available then the next
            page token to be used in the following
            ListStoredInfoTypes request.
    """

    @property
    def raw_page(self):
        return self

    stored_info_types: MutableSequence["StoredInfoType"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="StoredInfoType",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteStoredInfoTypeRequest(proto.Message):
    r"""Request message for DeleteStoredInfoType.

    Attributes:
        name (str):
            Required. Resource name of the organization and
            storedInfoType to be deleted, for example
            ``organizations/433245324/storedInfoTypes/432452342`` or
            projects/project-id/storedInfoTypes/432452342.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class HybridInspectJobTriggerRequest(proto.Message):
    r"""Request to search for potentially sensitive info in a custom
    location.

    Attributes:
        name (str):
            Required. Resource name of the trigger to execute a hybrid
            inspect on, for example
            ``projects/dlp-test-project/jobTriggers/53234423``.
        hybrid_item (google.cloud.dlp_v2.types.HybridContentItem):
            The item to inspect.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    hybrid_item: "HybridContentItem" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="HybridContentItem",
    )


class HybridInspectDlpJobRequest(proto.Message):
    r"""Request to search for potentially sensitive info in a custom
    location.

    Attributes:
        name (str):
            Required. Resource name of the job to execute a hybrid
            inspect on, for example
            ``projects/dlp-test-project/dlpJob/53234423``.
        hybrid_item (google.cloud.dlp_v2.types.HybridContentItem):
            The item to inspect.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    hybrid_item: "HybridContentItem" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="HybridContentItem",
    )


class HybridContentItem(proto.Message):
    r"""An individual hybrid item to inspect. Will be stored
    temporarily during processing.

    Attributes:
        item (google.cloud.dlp_v2.types.ContentItem):
            The item to inspect.
        finding_details (google.cloud.dlp_v2.types.HybridFindingDetails):
            Supplementary information that will be added
            to each finding.
    """

    item: "ContentItem" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ContentItem",
    )
    finding_details: "HybridFindingDetails" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="HybridFindingDetails",
    )


class HybridFindingDetails(proto.Message):
    r"""Populate to associate additional data with each finding.

    Attributes:
        container_details (google.cloud.dlp_v2.types.Container):
            Details about the container where the content
            being inspected is from.
        file_offset (int):
            Offset in bytes of the line, from the
            beginning of the file, where the finding  is
            located. Populate if the item being scanned is
            only part of a bigger item, such as a shard of a
            file and you want to track the absolute position
            of the finding.
        row_offset (int):
            Offset of the row for tables. Populate if the
            row(s) being scanned are part of a bigger
            dataset and you want to keep track of their
            absolute position.
        table_options (google.cloud.dlp_v2.types.TableOptions):
            If the container is a table, additional information to make
            findings meaningful such as the columns that are primary
            keys. If not known ahead of time, can also be set within
            each inspect hybrid call and the two will be merged. Note
            that identifying_fields will only be stored to BigQuery, and
            only if the BigQuery action has been included.
        labels (MutableMapping[str, str]):
            Labels to represent user provided metadata about the data
            being inspected. If configured by the job, some key values
            may be required. The labels associated with ``Finding``'s
            produced by hybrid inspection.

            Label keys must be between 1 and 63 characters long and must
            conform to the following regular expression:
            ``[a-z]([-a-z0-9]*[a-z0-9])?``.

            Label values must be between 0 and 63 characters long and
            must conform to the regular expression
            ``([a-z]([-a-z0-9]*[a-z0-9])?)?``.

            No more than 10 labels can be associated with a given
            finding.

            Examples:

            - ``"environment" : "production"``
            - ``"pipeline" : "etl"``
    """

    container_details: "Container" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Container",
    )
    file_offset: int = proto.Field(
        proto.INT64,
        number=2,
    )
    row_offset: int = proto.Field(
        proto.INT64,
        number=3,
    )
    table_options: storage.TableOptions = proto.Field(
        proto.MESSAGE,
        number=4,
        message=storage.TableOptions,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )


class HybridInspectResponse(proto.Message):
    r"""Quota exceeded errors will be thrown once quota has been met."""


class ImageContainmentType(proto.Message):
    r"""Specifies the relationship between bounding boxes for image
    findings.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        encloses (google.cloud.dlp_v2.types.Encloses):
            The context finding's bounding box must fully
            contain the target finding's bounding box.

            This field is a member of `oneof`_ ``type``.
        fully_inside (google.cloud.dlp_v2.types.FullyInside):
            The context finding's bounding box must be
            fully inside the target finding's bounding box.

            This field is a member of `oneof`_ ``type``.
        overlaps (google.cloud.dlp_v2.types.Overlap):
            The context finding's bounding box and the
            target finding's bounding box must have a
            non-zero intersection.

            This field is a member of `oneof`_ ``type``.
    """

    encloses: "Encloses" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="type",
        message="Encloses",
    )
    fully_inside: "FullyInside" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="type",
        message="FullyInside",
    )
    overlaps: "Overlap" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="type",
        message="Overlap",
    )


class Overlap(proto.Message):
    r"""Defines a condition for overlapping bounding boxes."""


class Encloses(proto.Message):
    r"""Defines a condition where one bounding box encloses another."""


class FullyInside(proto.Message):
    r"""Defines a condition where one bounding box is fully inside
    another.

    """


class ListProjectDataProfilesRequest(proto.Message):
    r"""Request to list the profiles generated for a given
    organization or project.

    Attributes:
        parent (str):
            Required. organizations/{org_id}/locations/{loc_id}
        page_token (str):
            Page token to continue retrieval.
        page_size (int):
            Size of the page. This value can be limited
            by the server. If zero, server returns a page of
            max size 100.
        order_by (str):
            Comma-separated list of fields to order by, followed by
            ``asc`` or ``desc`` postfix. This list is case insensitive.
            The default sorting order is ascending. Redundant space
            characters are insignificant. Only one order field at a time
            is allowed.

            Examples:

            - ``project_id``
            - ``sensitivity_level desc``

            Supported fields:

            - ``project_id``: Google Cloud project ID
            - ``sensitivity_level``: How sensitive the data in a project
              is, at most
            - ``data_risk_level``: How much risk is associated with this
              data
            - ``profile_last_generated``: Date and time (in epoch
              seconds) the profile was last generated
        filter (str):
            Allows filtering.

            Supported syntax:

            - Filter expressions are made up of one or more
              restrictions.
            - Restrictions can be combined by ``AND`` or ``OR`` logical
              operators. A sequence of restrictions implicitly uses
              ``AND``.
            - A restriction has the form of
              ``{field} {operator} {value}``.
            - Supported fields:

              - ``project_id``: the Google Cloud project ID
              - ``sensitivity_level``: HIGH|MODERATE|LOW
              - ``data_risk_level``: HIGH|MODERATE|LOW
              - ``status_code``: an RPC status code as defined in
                https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto
              - ``profile_last_generated``: Date and time the profile
                was last generated

            - The operator must be ``=`` or ``!=``. The
              ``profile_last_generated`` filter also supports ``<`` and
              ``>``.

            The syntax is based on https://google.aip.dev/160.

            Examples:

            - ``project_id = 12345 AND status_code = 1``
            - ``project_id = 12345 AND sensitivity_level = HIGH``
            - ``profile_last_generated < "2025-01-01T00:00:00.000Z"``

            The length of this field should be no more than 500
            characters.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=4,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListProjectDataProfilesResponse(proto.Message):
    r"""List of profiles generated for a given organization or
    project.

    Attributes:
        project_data_profiles (MutableSequence[google.cloud.dlp_v2.types.ProjectDataProfile]):
            List of data profiles.
        next_page_token (str):
            The next page token.
    """

    @property
    def raw_page(self):
        return self

    project_data_profiles: MutableSequence["ProjectDataProfile"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ProjectDataProfile",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListTableDataProfilesRequest(proto.Message):
    r"""Request to list the profiles generated for a given
    organization or project.

    Attributes:
        parent (str):
            Required. Resource name of the organization or project, for
            example ``organizations/433245324/locations/europe`` or
            ``projects/project-id/locations/asia``.
        page_token (str):
            Page token to continue retrieval.
        page_size (int):
            Size of the page. This value can be limited
            by the server. If zero, server returns a page of
            max size 100.
        order_by (str):
            Comma-separated list of fields to order by, followed by
            ``asc`` or ``desc`` postfix. This list is case insensitive.
            The default sorting order is ascending. Redundant space
            characters are insignificant. Only one order field at a time
            is allowed.

            Examples:

            - ``project_id asc``
            - ``table_id``
            - ``sensitivity_level desc``

            Supported fields are:

            - ``project_id``: The Google Cloud project ID.
            - ``dataset_id``: The ID of a BigQuery dataset.
            - ``table_id``: The ID of a BigQuery table.
            - ``sensitivity_level``: How sensitive the data in a table
              is, at most.
            - ``data_risk_level``: How much risk is associated with this
              data.
            - ``profile_last_generated``: When the profile was last
              updated in epoch seconds.
            - ``last_modified``: The last time the resource was
              modified.
            - ``resource_visibility``: Visibility restriction for this
              resource.
            - ``row_count``: Number of rows in this resource.
        filter (str):
            Allows filtering.

            Supported syntax:

            - Filter expressions are made up of one or more
              restrictions.

            - Restrictions can be combined by ``AND`` or ``OR`` logical
              operators. A sequence of restrictions implicitly uses
              ``AND``.

            - A restriction has the form of
              ``{field} {operator} {value}``.

            - Supported fields:

              - ``project_id``: The Google Cloud project ID
              - ``dataset_id``: The BigQuery dataset ID
              - ``table_id``: The ID of the BigQuery table
              - ``sensitivity_level``: HIGH|MODERATE|LOW
              - ``data_risk_level``: HIGH|MODERATE|LOW
              - ``resource_visibility``: PUBLIC|RESTRICTED
              - ``status_code``: an RPC status code as defined in
                https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto
              - ``profile_last_generated``: Date and time the profile
                was last generated

            - The operator must be ``=`` or ``!=``. The
              ``profile_last_generated`` filter also supports ``<`` and
              ``>``.

            The syntax is based on https://google.aip.dev/160.

            Examples:

            - ``project_id = 12345 AND status_code = 1``
            - ``project_id = 12345 AND sensitivity_level = HIGH``
            - ``project_id = 12345 AND resource_visibility = PUBLIC``
            - ``profile_last_generated < "2025-01-01T00:00:00.000Z"``

            The length of this field should be no more than 500
            characters.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=4,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListTableDataProfilesResponse(proto.Message):
    r"""List of profiles generated for a given organization or
    project.

    Attributes:
        table_data_profiles (MutableSequence[google.cloud.dlp_v2.types.TableDataProfile]):
            List of data profiles.
        next_page_token (str):
            The next page token.
    """

    @property
    def raw_page(self):
        return self

    table_data_profiles: MutableSequence["TableDataProfile"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="TableDataProfile",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListColumnDataProfilesRequest(proto.Message):
    r"""Request to list the profiles generated for a given
    organization or project.

    Attributes:
        parent (str):
            Required. Resource name of the organization or project, for
            example ``organizations/433245324/locations/europe`` or
            ``projects/project-id/locations/asia``.
        page_token (str):
            Page token to continue retrieval.
        page_size (int):
            Size of the page. This value can be limited
            by the server. If zero, server returns a page of
            max size 100.
        order_by (str):
            Comma-separated list of fields to order by, followed by
            ``asc`` or ``desc`` postfix. This list is case insensitive.
            The default sorting order is ascending. Redundant space
            characters are insignificant. Only one order field at a time
            is allowed.

            Examples:

            - ``project_id asc``
            - ``table_id``
            - ``sensitivity_level desc``

            Supported fields are:

            - ``project_id``: The Google Cloud project ID.
            - ``dataset_id``: The ID of a BigQuery dataset.
            - ``table_id``: The ID of a BigQuery table.
            - ``sensitivity_level``: How sensitive the data in a column
              is, at most.
            - ``data_risk_level``: How much risk is associated with this
              data.
            - ``profile_last_generated``: When the profile was last
              updated in epoch seconds.
        filter (str):
            Allows filtering.

            Supported syntax:

            - Filter expressions are made up of one or more
              restrictions.
            - Restrictions can be combined by ``AND`` or ``OR`` logical
              operators. A sequence of restrictions implicitly uses
              ``AND``.
            - A restriction has the form of
              ``{field} {operator} {value}``.
            - Supported fields:

              - ``table_data_profile_name``: The name of the related
                table data profile
              - ``project_id``: The Google Cloud project ID (REQUIRED)
              - ``dataset_id``: The BigQuery dataset ID (REQUIRED)
              - ``table_id``: The BigQuery table ID (REQUIRED)
              - ``field_id``: The ID of the BigQuery field
              - ``info_type``: The infotype detected in the resource
              - ``sensitivity_level``: HIGH|MEDIUM|LOW
              - ``data_risk_level``: How much risk is associated with
                this data
              - ``status_code``: An RPC status code as defined in
                https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto
              - ``profile_last_generated``: Date and time the profile
                was last generated

            - The operator must be ``=`` for project_id, dataset_id, and
              table_id. Other filters also support ``!=``. The
              ``profile_last_generated`` filter also supports ``<`` and
              ``>``.

            The syntax is based on https://google.aip.dev/160.

            Examples:

            - project_id = 12345 AND status_code = 1
            - project_id = 12345 AND sensitivity_level = HIGH
            - project_id = 12345 AND info_type = STREET_ADDRESS
            - profile_last_generated < "2025-01-01T00:00:00.000Z"

            The length of this field should be no more than 500
            characters.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=4,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListColumnDataProfilesResponse(proto.Message):
    r"""List of profiles generated for a given organization or
    project.

    Attributes:
        column_data_profiles (MutableSequence[google.cloud.dlp_v2.types.ColumnDataProfile]):
            List of data profiles.
        next_page_token (str):
            The next page token.
    """

    @property
    def raw_page(self):
        return self

    column_data_profiles: MutableSequence["ColumnDataProfile"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ColumnDataProfile",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DataRiskLevel(proto.Message):
    r"""Score is a summary of all elements in the data profile.
    A higher number means more risk.

    Attributes:
        score (google.cloud.dlp_v2.types.DataRiskLevel.DataRiskLevelScore):
            The score applied to the resource.
    """

    class DataRiskLevelScore(proto.Enum):
        r"""Various score levels for resources.

        Values:
            RISK_SCORE_UNSPECIFIED (0):
                Unused.
            RISK_LOW (10):
                Low risk - Lower indication of sensitive data
                that appears to have additional access
                restrictions in place or no indication of
                sensitive data found.
            RISK_UNKNOWN (12):
                Unable to determine risk.
            RISK_MODERATE (20):
                Medium risk - Sensitive data may be present
                but additional access or fine grain access
                restrictions appear to be present.  Consider
                limiting access even further or transform data
                to mask.
            RISK_HIGH (30):
                High risk – SPII may be present. Access
                controls may include public ACLs. Exfiltration
                of data may lead to user data loss.
                Re-identification of users may be possible.
                Consider limiting usage and or removing SPII.
        """

        RISK_SCORE_UNSPECIFIED = 0
        RISK_LOW = 10
        RISK_UNKNOWN = 12
        RISK_MODERATE = 20
        RISK_HIGH = 30

    score: DataRiskLevelScore = proto.Field(
        proto.ENUM,
        number=1,
        enum=DataRiskLevelScore,
    )


class ProjectDataProfile(proto.Message):
    r"""An aggregated profile for this project, based on the
    resources profiled within it.

    Attributes:
        name (str):
            The resource name of the profile.
        project_id (str):
            Project ID or account that was profiled.
        profile_last_generated (google.protobuf.timestamp_pb2.Timestamp):
            The last time the profile was generated.
        sensitivity_score (google.cloud.dlp_v2.types.SensitivityScore):
            The sensitivity score of this project.
        data_risk_level (google.cloud.dlp_v2.types.DataRiskLevel):
            The data risk level of this project.
        profile_status (google.cloud.dlp_v2.types.ProfileStatus):
            Success or error status of the last attempt
            to profile the project.
        table_data_profile_count (int):
            The number of table data profiles generated
            for this project.
        file_store_data_profile_count (int):
            The number of file store data profiles
            generated for this project.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    profile_last_generated: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    sensitivity_score: storage.SensitivityScore = proto.Field(
        proto.MESSAGE,
        number=4,
        message=storage.SensitivityScore,
    )
    data_risk_level: "DataRiskLevel" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="DataRiskLevel",
    )
    profile_status: "ProfileStatus" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="ProfileStatus",
    )
    table_data_profile_count: int = proto.Field(
        proto.INT64,
        number=9,
    )
    file_store_data_profile_count: int = proto.Field(
        proto.INT64,
        number=10,
    )


class DataProfileConfigSnapshot(proto.Message):
    r"""Snapshot of the configurations used to generate the profile.

    Attributes:
        inspect_config (google.cloud.dlp_v2.types.InspectConfig):
            A copy of the inspection config used to generate this
            profile. This is a copy of the inspect_template specified in
            ``DataProfileJobConfig``.
        data_profile_job (google.cloud.dlp_v2.types.DataProfileJobConfig):
            A copy of the configuration used to generate
            this profile. This is deprecated, and the
            DiscoveryConfig field is preferred moving
            forward. DataProfileJobConfig will still be
            written here for Discovery in BigQuery for
            backwards compatibility, but will not be updated
            with new fields, while DiscoveryConfig will.
        discovery_config (google.cloud.dlp_v2.types.DiscoveryConfig):
            A copy of the configuration used to generate
            this profile.
        inspect_template_name (str):
            Name of the inspection template used to
            generate this profile
        inspect_template_modified_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp when the template was modified
    """

    inspect_config: "InspectConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="InspectConfig",
    )
    data_profile_job: "DataProfileJobConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DataProfileJobConfig",
    )
    discovery_config: "DiscoveryConfig" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="DiscoveryConfig",
    )
    inspect_template_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    inspect_template_modified_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )


class TableDataProfile(proto.Message):
    r"""The profile for a scanned table.

    Attributes:
        name (str):
            The name of the profile.
        data_source_type (google.cloud.dlp_v2.types.DataSourceType):
            The resource type that was profiled.
        project_data_profile (str):
            The resource name of the project data profile
            for this table.
        dataset_project_id (str):
            The Google Cloud project ID that owns the
            resource.
        dataset_location (str):
            If supported, the location where the
            dataset's data is stored. See
            https://docs.cloud.google.com/bigquery/docs/locations
            for supported locations.
        dataset_id (str):
            If the resource is BigQuery, the dataset ID.
        table_id (str):
            The table ID.
        full_resource (str):
            The Cloud Asset Inventory resource that was profiled in
            order to generate this TableDataProfile.
            https://cloud.google.com/apis/design/resource_names#full_resource_name
        profile_status (google.cloud.dlp_v2.types.ProfileStatus):
            Success or error status from the most recent
            profile generation attempt. May be empty if the
            profile is still being generated.
        state (google.cloud.dlp_v2.types.TableDataProfile.State):
            State of a profile. This will always be set
            to DONE when the table data profile is written
            to another service like BigQuery or Pub/Sub.
        sensitivity_score (google.cloud.dlp_v2.types.SensitivityScore):
            The sensitivity score of this table.
        data_risk_level (google.cloud.dlp_v2.types.DataRiskLevel):
            The data risk level of this table.
        predicted_info_types (MutableSequence[google.cloud.dlp_v2.types.InfoTypeSummary]):
            The infoTypes predicted from this table's
            data.
        other_info_types (MutableSequence[google.cloud.dlp_v2.types.OtherInfoTypeSummary]):
            Other infoTypes found in this table's data.
        config_snapshot (google.cloud.dlp_v2.types.DataProfileConfigSnapshot):
            The snapshot of the configurations used to
            generate the profile.
        last_modified_time (google.protobuf.timestamp_pb2.Timestamp):
            The time when this table was last modified
        expiration_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The time when this table expires.
        scanned_column_count (int):
            The number of columns profiled in the table.
        failed_column_count (int):
            The number of columns skipped in the table
            because of an error.
        table_size_bytes (int):
            The size of the table when the profile was
            generated.
        row_count (int):
            Number of rows in the table when the profile
            was generated. This will not be populated for
            BigLake tables.
        encryption_status (google.cloud.dlp_v2.types.EncryptionStatus):
            How the table is encrypted.
        resource_visibility (google.cloud.dlp_v2.types.ResourceVisibility):
            How broadly a resource has been shared.
        profile_last_generated (google.protobuf.timestamp_pb2.Timestamp):
            The last time the profile was generated.
        resource_labels (MutableMapping[str, str]):
            The labels applied to the resource at the
            time the profile was generated.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which the table was created.
        sample_findings_table (google.cloud.dlp_v2.types.BigQueryTable):
            The BigQuery table to which the sample
            findings are written.
        tags (MutableSequence[google.cloud.dlp_v2.types.Tag]):
            The tags attached to the table, including any
            tags attached during profiling. Because tags are
            attached to Cloud SQL instances rather than
            Cloud SQL tables, this field is empty for Cloud
            SQL table profiles.
        related_resources (MutableSequence[google.cloud.dlp_v2.types.RelatedResource]):
            Resources related to this profile.
        domains (MutableSequence[google.cloud.dlp_v2.types.Domain]):
            Domains associated with the profile.
    """

    class State(proto.Enum):
        r"""Possible states of a profile. New items may be added.

        Values:
            STATE_UNSPECIFIED (0):
                Unused.
            RUNNING (1):
                The profile is currently running. Once a
                profile has finished it will transition to DONE.
            DONE (2):
                The profile is no longer generating. If
                profile_status.status.code is 0, the profile succeeded,
                otherwise, it failed.
        """

        STATE_UNSPECIFIED = 0
        RUNNING = 1
        DONE = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_source_type: "DataSourceType" = proto.Field(
        proto.MESSAGE,
        number=36,
        message="DataSourceType",
    )
    project_data_profile: str = proto.Field(
        proto.STRING,
        number=2,
    )
    dataset_project_id: str = proto.Field(
        proto.STRING,
        number=24,
    )
    dataset_location: str = proto.Field(
        proto.STRING,
        number=29,
    )
    dataset_id: str = proto.Field(
        proto.STRING,
        number=25,
    )
    table_id: str = proto.Field(
        proto.STRING,
        number=26,
    )
    full_resource: str = proto.Field(
        proto.STRING,
        number=3,
    )
    profile_status: "ProfileStatus" = proto.Field(
        proto.MESSAGE,
        number=21,
        message="ProfileStatus",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=22,
        enum=State,
    )
    sensitivity_score: storage.SensitivityScore = proto.Field(
        proto.MESSAGE,
        number=5,
        message=storage.SensitivityScore,
    )
    data_risk_level: "DataRiskLevel" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="DataRiskLevel",
    )
    predicted_info_types: MutableSequence["InfoTypeSummary"] = proto.RepeatedField(
        proto.MESSAGE,
        number=27,
        message="InfoTypeSummary",
    )
    other_info_types: MutableSequence["OtherInfoTypeSummary"] = proto.RepeatedField(
        proto.MESSAGE,
        number=28,
        message="OtherInfoTypeSummary",
    )
    config_snapshot: "DataProfileConfigSnapshot" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="DataProfileConfigSnapshot",
    )
    last_modified_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    expiration_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    scanned_column_count: int = proto.Field(
        proto.INT64,
        number=10,
    )
    failed_column_count: int = proto.Field(
        proto.INT64,
        number=11,
    )
    table_size_bytes: int = proto.Field(
        proto.INT64,
        number=12,
    )
    row_count: int = proto.Field(
        proto.INT64,
        number=13,
    )
    encryption_status: "EncryptionStatus" = proto.Field(
        proto.ENUM,
        number=14,
        enum="EncryptionStatus",
    )
    resource_visibility: "ResourceVisibility" = proto.Field(
        proto.ENUM,
        number=15,
        enum="ResourceVisibility",
    )
    profile_last_generated: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=16,
        message=timestamp_pb2.Timestamp,
    )
    resource_labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=17,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=23,
        message=timestamp_pb2.Timestamp,
    )
    sample_findings_table: storage.BigQueryTable = proto.Field(
        proto.MESSAGE,
        number=37,
        message=storage.BigQueryTable,
    )
    tags: MutableSequence["Tag"] = proto.RepeatedField(
        proto.MESSAGE,
        number=39,
        message="Tag",
    )
    related_resources: MutableSequence["RelatedResource"] = proto.RepeatedField(
        proto.MESSAGE,
        number=41,
        message="RelatedResource",
    )
    domains: MutableSequence["Domain"] = proto.RepeatedField(
        proto.MESSAGE,
        number=47,
        message="Domain",
    )


class ProfileStatus(proto.Message):
    r"""Success or errors for the profile generation.

    Attributes:
        status (google.rpc.status_pb2.Status):
            Profiling status code and optional message. The
            ``status.code`` value is 0 (default value) for OK.
        timestamp (google.protobuf.timestamp_pb2.Timestamp):
            Time when the profile generation status was
            updated
    """

    status: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=1,
        message=status_pb2.Status,
    )
    timestamp: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class InfoTypeSummary(proto.Message):
    r"""The infoType details for this column.

    Attributes:
        info_type (google.cloud.dlp_v2.types.InfoType):
            The infoType.
        estimated_prevalence (int):
            Not populated for predicted infotypes.
    """

    info_type: storage.InfoType = proto.Field(
        proto.MESSAGE,
        number=1,
        message=storage.InfoType,
    )
    estimated_prevalence: int = proto.Field(
        proto.INT32,
        number=2,
    )


class OtherInfoTypeSummary(proto.Message):
    r"""Infotype details for other infoTypes found within a column.

    Attributes:
        info_type (google.cloud.dlp_v2.types.InfoType):
            The other infoType.
        estimated_prevalence (int):
            Approximate percentage of non-null rows that
            contained data detected by this infotype.
        excluded_from_analysis (bool):
            Whether this infoType was excluded from
            sensitivity and risk analysis due to factors
            such as low prevalence (subject to change).
    """

    info_type: storage.InfoType = proto.Field(
        proto.MESSAGE,
        number=1,
        message=storage.InfoType,
    )
    estimated_prevalence: int = proto.Field(
        proto.INT32,
        number=2,
    )
    excluded_from_analysis: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class ColumnDataProfile(proto.Message):
    r"""The profile for a scanned column within a table.

    Attributes:
        name (str):
            The name of the profile.
        profile_status (google.cloud.dlp_v2.types.ProfileStatus):
            Success or error status from the most recent
            profile generation attempt. May be empty if the
            profile is still being generated.
        state (google.cloud.dlp_v2.types.ColumnDataProfile.State):
            State of a profile.
        profile_last_generated (google.protobuf.timestamp_pb2.Timestamp):
            The last time the profile was generated.
        table_data_profile (str):
            The resource name of the table data profile.
        table_full_resource (str):
            The resource name of the resource this column
            is within.
        dataset_project_id (str):
            The Google Cloud project ID that owns the
            profiled resource.
        dataset_location (str):
            If supported, the location where the
            dataset's data is stored. See
            https://docs.cloud.google.com/bigquery/docs/locations
            for supported BigQuery locations.
        dataset_id (str):
            The BigQuery dataset ID, if the resource
            profiled is a BigQuery table.
        table_id (str):
            The table ID.
        column (str):
            The name of the column.
        sensitivity_score (google.cloud.dlp_v2.types.SensitivityScore):
            The sensitivity of this column.
        data_risk_level (google.cloud.dlp_v2.types.DataRiskLevel):
            The data risk level for this column.
        column_info_type (google.cloud.dlp_v2.types.InfoTypeSummary):
            If it's been determined this column can be
            identified as a single type, this will be set.
            Otherwise the column either has unidentifiable
            content or mixed types.
        other_matches (MutableSequence[google.cloud.dlp_v2.types.OtherInfoTypeSummary]):
            Other types found within this column. List
            will be unordered.
        estimated_null_percentage (google.cloud.dlp_v2.types.NullPercentageLevel):
            Approximate percentage of entries being null
            in the column.
        estimated_uniqueness_score (google.cloud.dlp_v2.types.UniquenessScoreLevel):
            Approximate uniqueness of the column.
        free_text_score (float):
            The likelihood that this column contains
            free-form text. A value close to 1 may indicate
            the column is likely to contain free-form or
            natural language text.
            Range in 0-1.
        column_type (google.cloud.dlp_v2.types.ColumnDataProfile.ColumnDataType):
            The data type of a given column.
        policy_state (google.cloud.dlp_v2.types.ColumnDataProfile.ColumnPolicyState):
            Indicates if a policy tag has been applied to
            the column.
    """

    class State(proto.Enum):
        r"""Possible states of a profile. New items may be added.

        Values:
            STATE_UNSPECIFIED (0):
                Unused.
            RUNNING (1):
                The profile is currently running. Once a
                profile has finished it will transition to DONE.
            DONE (2):
                The profile is no longer generating. If
                profile_status.status.code is 0, the profile succeeded,
                otherwise, it failed.
        """

        STATE_UNSPECIFIED = 0
        RUNNING = 1
        DONE = 2

    class ColumnDataType(proto.Enum):
        r"""Data types of the data in a column. Types may be added over
        time.

        Values:
            COLUMN_DATA_TYPE_UNSPECIFIED (0):
                Invalid type.
            TYPE_INT64 (1):
                Encoded as a string in decimal format.
            TYPE_BOOL (2):
                Encoded as a boolean "false" or "true".
            TYPE_FLOAT64 (3):
                Encoded as a number, or string "NaN",
                "Infinity" or "-Infinity".
            TYPE_STRING (4):
                Encoded as a string value.
            TYPE_BYTES (5):
                Encoded as a base64 string per RFC 4648,
                section 4.
            TYPE_TIMESTAMP (6):
                Encoded as an RFC 3339 timestamp with
                mandatory "Z" time zone string:
                1985-04-12T23:20:50.52Z
            TYPE_DATE (7):
                Encoded as RFC 3339 full-date format string:
                1985-04-12
            TYPE_TIME (8):
                Encoded as RFC 3339 partial-time format
                string: 23:20:50.52
            TYPE_DATETIME (9):
                Encoded as RFC 3339 full-date "T"
                partial-time: 1985-04-12T23:20:50.52
            TYPE_GEOGRAPHY (10):
                Encoded as WKT
            TYPE_NUMERIC (11):
                Encoded as a decimal string.
            TYPE_RECORD (12):
                Container of ordered fields, each with a type
                and field name.
            TYPE_BIGNUMERIC (13):
                Decimal type.
            TYPE_JSON (14):
                Json type.
            TYPE_INTERVAL (15):
                Interval type.
            TYPE_RANGE_DATE (16):
                ``Range<Date>`` type.
            TYPE_RANGE_DATETIME (17):
                ``Range<Datetime>`` type.
            TYPE_RANGE_TIMESTAMP (18):
                ``Range<Timestamp>`` type.
        """

        COLUMN_DATA_TYPE_UNSPECIFIED = 0
        TYPE_INT64 = 1
        TYPE_BOOL = 2
        TYPE_FLOAT64 = 3
        TYPE_STRING = 4
        TYPE_BYTES = 5
        TYPE_TIMESTAMP = 6
        TYPE_DATE = 7
        TYPE_TIME = 8
        TYPE_DATETIME = 9
        TYPE_GEOGRAPHY = 10
        TYPE_NUMERIC = 11
        TYPE_RECORD = 12
        TYPE_BIGNUMERIC = 13
        TYPE_JSON = 14
        TYPE_INTERVAL = 15
        TYPE_RANGE_DATE = 16
        TYPE_RANGE_DATETIME = 17
        TYPE_RANGE_TIMESTAMP = 18

    class ColumnPolicyState(proto.Enum):
        r"""The possible policy states for a column.

        Values:
            COLUMN_POLICY_STATE_UNSPECIFIED (0):
                No policy tags.
            COLUMN_POLICY_TAGGED (1):
                Column has policy tag applied.
        """

        COLUMN_POLICY_STATE_UNSPECIFIED = 0
        COLUMN_POLICY_TAGGED = 1

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    profile_status: "ProfileStatus" = proto.Field(
        proto.MESSAGE,
        number=17,
        message="ProfileStatus",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=18,
        enum=State,
    )
    profile_last_generated: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    table_data_profile: str = proto.Field(
        proto.STRING,
        number=4,
    )
    table_full_resource: str = proto.Field(
        proto.STRING,
        number=5,
    )
    dataset_project_id: str = proto.Field(
        proto.STRING,
        number=19,
    )
    dataset_location: str = proto.Field(
        proto.STRING,
        number=20,
    )
    dataset_id: str = proto.Field(
        proto.STRING,
        number=21,
    )
    table_id: str = proto.Field(
        proto.STRING,
        number=22,
    )
    column: str = proto.Field(
        proto.STRING,
        number=6,
    )
    sensitivity_score: storage.SensitivityScore = proto.Field(
        proto.MESSAGE,
        number=7,
        message=storage.SensitivityScore,
    )
    data_risk_level: "DataRiskLevel" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="DataRiskLevel",
    )
    column_info_type: "InfoTypeSummary" = proto.Field(
        proto.MESSAGE,
        number=9,
        message="InfoTypeSummary",
    )
    other_matches: MutableSequence["OtherInfoTypeSummary"] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message="OtherInfoTypeSummary",
    )
    estimated_null_percentage: "NullPercentageLevel" = proto.Field(
        proto.ENUM,
        number=23,
        enum="NullPercentageLevel",
    )
    estimated_uniqueness_score: "UniquenessScoreLevel" = proto.Field(
        proto.ENUM,
        number=24,
        enum="UniquenessScoreLevel",
    )
    free_text_score: float = proto.Field(
        proto.DOUBLE,
        number=13,
    )
    column_type: ColumnDataType = proto.Field(
        proto.ENUM,
        number=14,
        enum=ColumnDataType,
    )
    policy_state: ColumnPolicyState = proto.Field(
        proto.ENUM,
        number=15,
        enum=ColumnPolicyState,
    )


class FileStoreDataProfile(proto.Message):
    r"""The profile for a file store.

    - Cloud Storage: maps 1:1 with a bucket.
    - Amazon S3: maps 1:1 with a bucket.

    Attributes:
        name (str):
            The name of the profile.
        data_source_type (google.cloud.dlp_v2.types.DataSourceType):
            The resource type that was profiled.
        project_data_profile (str):
            The resource name of the project data profile
            for this file store.
        project_id (str):
            The Google Cloud project ID that owns the
            resource. For Amazon S3 buckets, this is the AWS
            Account Id.
        file_store_location (str):
            The location of the file store.

            - Cloud Storage:
              https://docs.cloud.google.com/storage/docs/locations#available-locations
            - Amazon S3:
              https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints
        data_storage_locations (MutableSequence[str]):
            For resources that have multiple storage locations, these
            are those regions. For Cloud Storage this is the list of
            regions chosen for dual-region storage.
            ``file_store_location`` will normally be the corresponding
            multi-region for the list of individual locations. The first
            region is always picked as the processing and storage
            location for the data profile.
        location_type (str):
            The location type of the file store (region, dual-region,
            multi-region, etc). If dual-region, expect
            data_storage_locations to be populated.
        file_store_path (str):
            The file store path.

            - Cloud Storage: ``gs://{bucket}``
            - Amazon S3: ``s3://{bucket}``
            - Vertex AI dataset:
              ``projects/{project_number}/locations/{location}/datasets/{dataset_id}``
        full_resource (str):
            The resource name of the resource profiled.
            https://cloud.google.com/apis/design/resource_names#full_resource_name

            Example format of an S3 bucket full resource name:
            ``//cloudasset.googleapis.com/organizations/{org_id}/otherCloudConnections/aws/arn:aws:s3:::{bucket_name}``
        config_snapshot (google.cloud.dlp_v2.types.DataProfileConfigSnapshot):
            The snapshot of the configurations used to
            generate the profile.
        profile_status (google.cloud.dlp_v2.types.ProfileStatus):
            Success or error status from the most recent
            profile generation attempt. May be empty if the
            profile is still being generated.
        state (google.cloud.dlp_v2.types.FileStoreDataProfile.State):
            State of a profile.
        profile_last_generated (google.protobuf.timestamp_pb2.Timestamp):
            The last time the profile was generated.
        resource_visibility (google.cloud.dlp_v2.types.ResourceVisibility):
            How broadly a resource has been shared.
        sensitivity_score (google.cloud.dlp_v2.types.SensitivityScore):
            The sensitivity score of this resource.
        data_risk_level (google.cloud.dlp_v2.types.DataRiskLevel):
            The data risk level of this resource.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the file store was first created.
        last_modified_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the file store was last modified.
        file_cluster_summaries (MutableSequence[google.cloud.dlp_v2.types.FileClusterSummary]):
            FileClusterSummary per each cluster.
        resource_attributes (MutableMapping[str, google.cloud.dlp_v2.types.Value]):
            Attributes of the resource being profiled. Currently used
            attributes:

            - customer_managed_encryption: boolean

              - true: the resource is encrypted with a customer-managed
                key.
              - false: the resource is encrypted with a provider-managed
                key.
        resource_labels (MutableMapping[str, str]):
            The labels applied to the resource at the
            time the profile was generated.
        file_store_info_type_summaries (MutableSequence[google.cloud.dlp_v2.types.FileStoreInfoTypeSummary]):
            InfoTypes detected in this file store.
        sample_findings_table (google.cloud.dlp_v2.types.BigQueryTable):
            The BigQuery table to which the sample
            findings are written.
        file_store_is_empty (bool):
            The file store does not have any files. If
            the profiling operation failed, this is false.
        tags (MutableSequence[google.cloud.dlp_v2.types.Tag]):
            The tags attached to the resource, including
            any tags attached during profiling.
        related_resources (MutableSequence[google.cloud.dlp_v2.types.RelatedResource]):
            Resources related to this profile.
        domains (MutableSequence[google.cloud.dlp_v2.types.Domain]):
            Domains associated with the profile.
    """

    class State(proto.Enum):
        r"""Possible states of a profile. New items may be added.

        Values:
            STATE_UNSPECIFIED (0):
                Unused.
            RUNNING (1):
                The profile is currently running. Once a
                profile has finished it will transition to DONE.
            DONE (2):
                The profile is no longer generating. If
                profile_status.status.code is 0, the profile succeeded,
                otherwise, it failed.
        """

        STATE_UNSPECIFIED = 0
        RUNNING = 1
        DONE = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_source_type: "DataSourceType" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DataSourceType",
    )
    project_data_profile: str = proto.Field(
        proto.STRING,
        number=3,
    )
    project_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    file_store_location: str = proto.Field(
        proto.STRING,
        number=5,
    )
    data_storage_locations: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=19,
    )
    location_type: str = proto.Field(
        proto.STRING,
        number=20,
    )
    file_store_path: str = proto.Field(
        proto.STRING,
        number=6,
    )
    full_resource: str = proto.Field(
        proto.STRING,
        number=24,
    )
    config_snapshot: "DataProfileConfigSnapshot" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="DataProfileConfigSnapshot",
    )
    profile_status: "ProfileStatus" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="ProfileStatus",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=9,
        enum=State,
    )
    profile_last_generated: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    resource_visibility: "ResourceVisibility" = proto.Field(
        proto.ENUM,
        number=11,
        enum="ResourceVisibility",
    )
    sensitivity_score: storage.SensitivityScore = proto.Field(
        proto.MESSAGE,
        number=12,
        message=storage.SensitivityScore,
    )
    data_risk_level: "DataRiskLevel" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="DataRiskLevel",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=14,
        message=timestamp_pb2.Timestamp,
    )
    last_modified_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=15,
        message=timestamp_pb2.Timestamp,
    )
    file_cluster_summaries: MutableSequence["FileClusterSummary"] = proto.RepeatedField(
        proto.MESSAGE,
        number=16,
        message="FileClusterSummary",
    )
    resource_attributes: MutableMapping[str, "Value"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=17,
        message="Value",
    )
    resource_labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=18,
    )
    file_store_info_type_summaries: MutableSequence["FileStoreInfoTypeSummary"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=21,
            message="FileStoreInfoTypeSummary",
        )
    )
    sample_findings_table: storage.BigQueryTable = proto.Field(
        proto.MESSAGE,
        number=22,
        message=storage.BigQueryTable,
    )
    file_store_is_empty: bool = proto.Field(
        proto.BOOL,
        number=23,
    )
    tags: MutableSequence["Tag"] = proto.RepeatedField(
        proto.MESSAGE,
        number=25,
        message="Tag",
    )
    related_resources: MutableSequence["RelatedResource"] = proto.RepeatedField(
        proto.MESSAGE,
        number=26,
        message="RelatedResource",
    )
    domains: MutableSequence["Domain"] = proto.RepeatedField(
        proto.MESSAGE,
        number=27,
        message="Domain",
    )


class Tag(proto.Message):
    r"""A tag associated with a resource.

    Attributes:
        namespaced_tag_value (str):
            The namespaced name for the tag value to attach to Google
            Cloud resources. Must be in the format
            ``{parent_id}/{tag_key_short_name}/{short_name}``, for
            example, "123456/environment/prod" for an organization
            parent, or "my-project/environment/prod" for a project
            parent. This is only set for Google Cloud resources.
        key (str):
            The key of a tag key-value pair. For Google
            Cloud resources, this is the resource name of
            the key, for example, "tagKeys/123456".
        value (str):
            The value of a tag key-value pair. For Google
            Cloud resources, this is the resource name of
            the value, for example, "tagValues/123456".
    """

    namespaced_tag_value: str = proto.Field(
        proto.STRING,
        number=1,
    )
    key: str = proto.Field(
        proto.STRING,
        number=2,
    )
    value: str = proto.Field(
        proto.STRING,
        number=3,
    )


class TagFilters(proto.Message):
    r"""Tags to match against for filtering.

    Attributes:
        tag_filters (MutableSequence[google.cloud.dlp_v2.types.TagFilter]):
            Required. A resource must match ALL of the
            specified tag filters to be included in the
            collection.
    """

    tag_filters: MutableSequence["TagFilter"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="TagFilter",
    )


class TagFilter(proto.Message):
    r"""A single tag to filter against.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        namespaced_tag_value (str):
            The namespaced name for the tag value. Must be in the format
            ``{parent_id}/{tag_key_short_name}/{short_name}``, for
            example, "123456/environment/prod" for an organization
            parent, or "my-project/environment/prod" for a project
            parent.

            This field is a member of `oneof`_ ``format``.
        namespaced_tag_key (str):
            The namespaced name for the tag key. Must be in the format
            ``{parent_id}/{tag_key_short_name}``, for example,
            "123456/sensitive" for an organization parent, or
            "my-project/sensitive" for a project parent.

            This field is a member of `oneof`_ ``format``.
    """

    namespaced_tag_value: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="format",
    )
    namespaced_tag_key: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="format",
    )


class RelatedResource(proto.Message):
    r"""A related resource. Examples:

    - The source BigQuery table for a Vertex AI dataset.
    - The source Cloud Storage bucket for a Vertex AI dataset.

    Attributes:
        full_resource (str):
            The full resource name of the related
            resource.
    """

    full_resource: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FileStoreInfoTypeSummary(proto.Message):
    r"""Information regarding the discovered InfoType.

    Attributes:
        info_type (google.cloud.dlp_v2.types.InfoType):
            The InfoType seen.
    """

    info_type: storage.InfoType = proto.Field(
        proto.MESSAGE,
        number=1,
        message=storage.InfoType,
    )


class FileExtensionInfo(proto.Message):
    r"""Information regarding the discovered file extension.

    Attributes:
        file_extension (str):
            The file extension if set. (aka .pdf, .jpg,
            .txt)
    """

    file_extension: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FileClusterSummary(proto.Message):
    r"""The file cluster summary.

    Attributes:
        file_cluster_type (google.cloud.dlp_v2.types.FileClusterType):
            The file cluster type.
        file_store_info_type_summaries (MutableSequence[google.cloud.dlp_v2.types.FileStoreInfoTypeSummary]):
            InfoTypes detected in this cluster.
        sensitivity_score (google.cloud.dlp_v2.types.SensitivityScore):
            The sensitivity score of this cluster. The score will be
            SENSITIVITY_LOW if nothing has been scanned.
        data_risk_level (google.cloud.dlp_v2.types.DataRiskLevel):
            The data risk level of this cluster. RISK_LOW if nothing has
            been scanned.
        errors (MutableSequence[google.cloud.dlp_v2.types.Error]):
            A list of errors detected while scanning this
            cluster. The list is truncated to 10 per
            cluster.
        file_extensions_scanned (MutableSequence[google.cloud.dlp_v2.types.FileExtensionInfo]):
            A sample of file types scanned in this
            cluster. Empty if no files were scanned. File
            extensions can be derived from the file name or
            the file content.
        file_extensions_seen (MutableSequence[google.cloud.dlp_v2.types.FileExtensionInfo]):
            A sample of file types seen in this cluster.
            Empty if no files were seen. File extensions can
            be derived from the file name or the file
            content.
        no_files_exist (bool):
            True if no files exist in this cluster. If the file store
            had more files than could be listed, this will be false even
            if no files for this cluster were seen and
            file_extensions_seen is empty.
    """

    file_cluster_type: "FileClusterType" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="FileClusterType",
    )
    file_store_info_type_summaries: MutableSequence["FileStoreInfoTypeSummary"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="FileStoreInfoTypeSummary",
        )
    )
    sensitivity_score: storage.SensitivityScore = proto.Field(
        proto.MESSAGE,
        number=3,
        message=storage.SensitivityScore,
    )
    data_risk_level: "DataRiskLevel" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="DataRiskLevel",
    )
    errors: MutableSequence["Error"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="Error",
    )
    file_extensions_scanned: MutableSequence["FileExtensionInfo"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="FileExtensionInfo",
    )
    file_extensions_seen: MutableSequence["FileExtensionInfo"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="FileExtensionInfo",
    )
    no_files_exist: bool = proto.Field(
        proto.BOOL,
        number=9,
    )


class GetProjectDataProfileRequest(proto.Message):
    r"""Request to get a project data profile.

    Attributes:
        name (str):
            Required. Resource name, for example
            ``organizations/12345/locations/us/projectDataProfiles/53234423``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetFileStoreDataProfileRequest(proto.Message):
    r"""Request to get a file store data profile.

    Attributes:
        name (str):
            Required. Resource name, for example
            ``organizations/12345/locations/us/fileStoreDataProfiles/53234423``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListFileStoreDataProfilesRequest(proto.Message):
    r"""Request to list the file store profiles generated for a given
    organization or project.

    Attributes:
        parent (str):
            Required. Resource name of the organization or project, for
            example ``organizations/433245324/locations/europe`` or
            ``projects/project-id/locations/asia``.
        page_token (str):
            Optional. Page token to continue retrieval.
        page_size (int):
            Optional. Size of the page. This value can be
            limited by the server. If zero, server returns a
            page of max size 100.
        order_by (str):
            Optional. Comma-separated list of fields to order by,
            followed by ``asc`` or ``desc`` postfix. This list is case
            insensitive. The default sorting order is ascending.
            Redundant space characters are insignificant. Only one order
            field at a time is allowed.

            Examples:

            - ``project_id asc``
            - ``name``
            - ``sensitivity_level desc``

            Supported fields are:

            - ``project_id``: The Google Cloud project ID.
            - ``sensitivity_level``: How sensitive the data in a table
              is, at most.
            - ``data_risk_level``: How much risk is associated with this
              data.
            - ``profile_last_generated``: When the profile was last
              updated in epoch seconds.
            - ``last_modified``: The last time the resource was
              modified.
            - ``resource_visibility``: Visibility restriction for this
              resource.
            - ``name``: The name of the profile.
            - ``create_time``: The time the file store was first
              created.
        filter (str):
            Optional. Allows filtering.

            Supported syntax:

            - Filter expressions are made up of one or more
              restrictions.

            - Restrictions can be combined by ``AND`` or ``OR`` logical
              operators. A sequence of restrictions implicitly uses
              ``AND``.

            - A restriction has the form of
              ``{field} {operator} {value}``.

            - Supported fields:

              - ``project_id``: The Google Cloud project ID
              - ``account_id``: The AWS account ID
              - ``file_store_path``: The path like "gs://bucket"
              - ``data_source_type``: The profile's data source type,
                like "google/storage/bucket"
              - ``data_storage_location``: The location where the file
                store's data is stored, like "us-central1"
              - ``sensitivity_level``: HIGH|MODERATE|LOW
              - ``data_risk_level``: HIGH|MODERATE|LOW
              - ``resource_visibility``: PUBLIC|RESTRICTED
              - ``status_code``: an RPC status code as defined in
                https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto
              - ``profile_last_generated``: Date and time the profile
                was last generated

            - The operator must be ``=`` or ``!=``. The
              ``profile_last_generated`` filter also supports ``<`` and
              ``>``.

            The syntax is based on https://google.aip.dev/160.

            Examples:

            - ``project_id = 12345 AND status_code = 1``
            - ``project_id = 12345 AND sensitivity_level = HIGH``
            - ``project_id = 12345 AND resource_visibility = PUBLIC``
            - ``file_store_path = "gs://mybucket"``
            - ``profile_last_generated < "2025-01-01T00:00:00.000Z"``

            The length of this field should be no more than 500
            characters.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=4,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListFileStoreDataProfilesResponse(proto.Message):
    r"""List of file store data profiles generated for a given
    organization or project.

    Attributes:
        file_store_data_profiles (MutableSequence[google.cloud.dlp_v2.types.FileStoreDataProfile]):
            List of data profiles.
        next_page_token (str):
            The next page token.
    """

    @property
    def raw_page(self):
        return self

    file_store_data_profiles: MutableSequence["FileStoreDataProfile"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="FileStoreDataProfile",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteFileStoreDataProfileRequest(proto.Message):
    r"""Request message for DeleteFileStoreProfile.

    Attributes:
        name (str):
            Required. Resource name of the file store
            data profile.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetTableDataProfileRequest(proto.Message):
    r"""Request to get a table data profile.

    Attributes:
        name (str):
            Required. Resource name, for example
            ``organizations/12345/locations/us/tableDataProfiles/53234423``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetColumnDataProfileRequest(proto.Message):
    r"""Request to get a column data profile.

    Attributes:
        name (str):
            Required. Resource name, for example
            ``organizations/12345/locations/us/columnDataProfiles/53234423``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DataProfilePubSubCondition(proto.Message):
    r"""A condition for determining whether a Pub/Sub should be
    triggered.

    Attributes:
        expressions (google.cloud.dlp_v2.types.DataProfilePubSubCondition.PubSubExpressions):
            An expression.
    """

    class ProfileScoreBucket(proto.Enum):
        r"""Various score levels for resources.

        Values:
            PROFILE_SCORE_BUCKET_UNSPECIFIED (0):
                Unused.
            HIGH (1):
                High risk/sensitivity detected.
            MEDIUM_OR_HIGH (2):
                Medium or high risk/sensitivity detected.
        """

        PROFILE_SCORE_BUCKET_UNSPECIFIED = 0
        HIGH = 1
        MEDIUM_OR_HIGH = 2

    class PubSubCondition(proto.Message):
        r"""A condition consisting of a value.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            minimum_risk_score (google.cloud.dlp_v2.types.DataProfilePubSubCondition.ProfileScoreBucket):
                The minimum data risk score that triggers the
                condition.

                This field is a member of `oneof`_ ``value``.
            minimum_sensitivity_score (google.cloud.dlp_v2.types.DataProfilePubSubCondition.ProfileScoreBucket):
                The minimum sensitivity level that triggers
                the condition.

                This field is a member of `oneof`_ ``value``.
        """

        minimum_risk_score: "DataProfilePubSubCondition.ProfileScoreBucket" = (
            proto.Field(
                proto.ENUM,
                number=1,
                oneof="value",
                enum="DataProfilePubSubCondition.ProfileScoreBucket",
            )
        )
        minimum_sensitivity_score: "DataProfilePubSubCondition.ProfileScoreBucket" = (
            proto.Field(
                proto.ENUM,
                number=2,
                oneof="value",
                enum="DataProfilePubSubCondition.ProfileScoreBucket",
            )
        )

    class PubSubExpressions(proto.Message):
        r"""An expression, consisting of an operator and conditions.

        Attributes:
            logical_operator (google.cloud.dlp_v2.types.DataProfilePubSubCondition.PubSubExpressions.PubSubLogicalOperator):
                The operator to apply to the collection of
                conditions.
            conditions (MutableSequence[google.cloud.dlp_v2.types.DataProfilePubSubCondition.PubSubCondition]):
                Conditions to apply to the expression.
        """

        class PubSubLogicalOperator(proto.Enum):
            r"""Logical operators for conditional checks.

            Values:
                LOGICAL_OPERATOR_UNSPECIFIED (0):
                    Unused.
                OR (1):
                    Conditional OR.
                AND (2):
                    Conditional AND.
            """

            LOGICAL_OPERATOR_UNSPECIFIED = 0
            OR = 1
            AND = 2

        logical_operator: "DataProfilePubSubCondition.PubSubExpressions.PubSubLogicalOperator" = proto.Field(
            proto.ENUM,
            number=1,
            enum="DataProfilePubSubCondition.PubSubExpressions.PubSubLogicalOperator",
        )
        conditions: MutableSequence["DataProfilePubSubCondition.PubSubCondition"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="DataProfilePubSubCondition.PubSubCondition",
            )
        )

    expressions: PubSubExpressions = proto.Field(
        proto.MESSAGE,
        number=1,
        message=PubSubExpressions,
    )


class DataProfilePubSubMessage(proto.Message):
    r"""Pub/Sub topic message for a
    DataProfileAction.PubSubNotification event. To receive a message
    of protocol buffer schema type, convert the message data to an
    object of this proto class.

    Attributes:
        profile (google.cloud.dlp_v2.types.TableDataProfile):
            If ``DetailLevel`` is ``TABLE_PROFILE`` this will be fully
            populated. Otherwise, if ``DetailLevel`` is
            ``RESOURCE_NAME``, then only ``name`` and ``full_resource``
            will be populated.
        file_store_profile (google.cloud.dlp_v2.types.FileStoreDataProfile):
            If ``DetailLevel`` is ``FILE_STORE_PROFILE`` this will be
            fully populated. Otherwise, if ``DetailLevel`` is
            ``RESOURCE_NAME``, then only ``name`` and
            ``file_store_path`` will be populated.
        event (google.cloud.dlp_v2.types.DataProfileAction.EventType):
            The event that caused the Pub/Sub message to
            be sent.
    """

    profile: "TableDataProfile" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="TableDataProfile",
    )
    file_store_profile: "FileStoreDataProfile" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="FileStoreDataProfile",
    )
    event: "DataProfileAction.EventType" = proto.Field(
        proto.ENUM,
        number=2,
        enum="DataProfileAction.EventType",
    )


class CreateConnectionRequest(proto.Message):
    r"""Request message for CreateConnection.

    Attributes:
        parent (str):
            Required. Parent resource name.

            The format of this value varies depending on the scope of
            the request (project or organization):

            - Projects scope:
              ``projects/{project_id}/locations/{location_id}``
            - Organizations scope:
              ``organizations/{org_id}/locations/{location_id}``
        connection (google.cloud.dlp_v2.types.Connection):
            Required. The connection resource.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    connection: "Connection" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Connection",
    )


class GetConnectionRequest(proto.Message):
    r"""Request message for GetConnection.

    Attributes:
        name (str):
            Required. Resource name in the format:
            ``projects/{project}/locations/{location}/connections/{connection}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListConnectionsRequest(proto.Message):
    r"""Request message for ListConnections.

    Attributes:
        parent (str):
            Required. Resource name of the organization or project, for
            example, ``organizations/433245324/locations/europe`` or
            ``projects/project-id/locations/asia``.
        page_size (int):
            Optional. Number of results per page, max
            1000.
        page_token (str):
            Optional. Page token from a previous page to
            return the next set of results. If set, all
            other request fields must match the original
            request.
        filter (str):
            Optional. Supported field/value: ``state`` -
            MISSING|AVAILABLE|ERROR

            The syntax is based on https://google.aip.dev/160.
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SearchConnectionsRequest(proto.Message):
    r"""Request message for SearchConnections.

    Attributes:
        parent (str):
            Required. Resource name of the organization or project with
            a wildcard location, for example,
            ``organizations/433245324/locations/-`` or
            ``projects/project-id/locations/-``.
        page_size (int):
            Optional. Number of results per page, max
            1000.
        page_token (str):
            Optional. Page token from a previous page to
            return the next set of results. If set, all
            other request fields must match the original
            request.
        filter (str):
            Optional. Supported field/value: - ``state`` -
            MISSING|AVAILABLE|ERROR

            The syntax is based on https://google.aip.dev/160.
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListConnectionsResponse(proto.Message):
    r"""Response message for ListConnections.

    Attributes:
        connections (MutableSequence[google.cloud.dlp_v2.types.Connection]):
            List of connections.
        next_page_token (str):
            Token to retrieve the next page of results.
            An empty value means there are no more results.
    """

    @property
    def raw_page(self):
        return self

    connections: MutableSequence["Connection"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Connection",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SearchConnectionsResponse(proto.Message):
    r"""Response message for SearchConnections.

    Attributes:
        connections (MutableSequence[google.cloud.dlp_v2.types.Connection]):
            List of connections that match the search
            query. Note that only a subset of the fields
            will be populated, and only "name" is guaranteed
            to be set. For full details of a Connection,
            call GetConnection with the name.
        next_page_token (str):
            Token to retrieve the next page of results.
            An empty value means there are no more results.
    """

    @property
    def raw_page(self):
        return self

    connections: MutableSequence["Connection"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Connection",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateConnectionRequest(proto.Message):
    r"""Request message for UpdateConnection.

    Attributes:
        name (str):
            Required. Resource name in the format:
            ``projects/{project}/locations/{location}/connections/{connection}``.
        connection (google.cloud.dlp_v2.types.Connection):
            Required. The connection with new values for
            the relevant fields.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Mask to control which fields get
            updated.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    connection: "Connection" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Connection",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


class DeleteConnectionRequest(proto.Message):
    r"""Request message for DeleteConnection.

    Attributes:
        name (str):
            Required. Resource name of the Connection to be deleted, in
            the format:
            ``projects/{project}/locations/{location}/connections/{connection}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Connection(proto.Message):
    r"""A data connection to allow the DLP API to profile data in
    locations that require additional configuration.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. Name of the connection:
            ``projects/{project}/locations/{location}/connections/{name}``.
        state (google.cloud.dlp_v2.types.ConnectionState):
            Required. The connection's state in its
            lifecycle.
        errors (MutableSequence[google.cloud.dlp_v2.types.Error]):
            Output only. Set if status == ERROR, to
            provide additional details. Will store the last
            10 errors sorted with the most recent first.
        cloud_sql (google.cloud.dlp_v2.types.CloudSqlProperties):
            Connect to a Cloud SQL instance.

            This field is a member of `oneof`_ ``properties``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: "ConnectionState" = proto.Field(
        proto.ENUM,
        number=2,
        enum="ConnectionState",
    )
    errors: MutableSequence["Error"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="Error",
    )
    cloud_sql: "CloudSqlProperties" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="properties",
        message="CloudSqlProperties",
    )


class SecretManagerCredential(proto.Message):
    r"""A credential consisting of a username and password, where the
    password is stored in a Secret Manager resource. Note: Secret
    Manager `charges
    apply <https://cloud.google.com/secret-manager/pricing>`__.

    Attributes:
        username (str):
            Required. The username.
        password_secret_version_name (str):
            Required. The name of the Secret Manager resource that
            stores the password, in the form
            ``projects/project-id/secrets/secret-name/versions/version``.
    """

    username: str = proto.Field(
        proto.STRING,
        number=1,
    )
    password_secret_version_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CloudSqlIamCredential(proto.Message):
    r"""Use IAM authentication to connect. This requires the Cloud
    SQL IAM feature to be enabled on the instance, which is not the
    default for Cloud SQL. See
    https://docs.cloud.google.com/sql/docs/postgres/authentication
    and https://docs.cloud.google.com/sql/docs/mysql/authentication.

    """


class CloudSqlProperties(proto.Message):
    r"""Cloud SQL connection properties.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        connection_name (str):
            Optional. Immutable. The Cloud SQL instance for which the
            connection is defined. Only one connection per instance is
            allowed. This can only be set at creation time, and cannot
            be updated.

            It is an error to use a connection_name from different
            project or region than the one that holds the connection.
            For example, a Connection resource for Cloud SQL
            connection_name ``project-id:us-central1:sql-instance`` must
            be created under the parent
            ``projects/project-id/locations/us-central1``
        username_password (google.cloud.dlp_v2.types.SecretManagerCredential):
            A username and password stored in Secret
            Manager.

            This field is a member of `oneof`_ ``credential``.
        cloud_sql_iam (google.cloud.dlp_v2.types.CloudSqlIamCredential):
            Built-in IAM authentication (must be
            configured in Cloud SQL).

            This field is a member of `oneof`_ ``credential``.
        max_connections (int):
            Required. The DLP API will limit its connections to
            max_connections. Must be 2 or greater.
        database_engine (google.cloud.dlp_v2.types.CloudSqlProperties.DatabaseEngine):
            Required. The database engine used by the
            Cloud SQL instance that this connection
            configures.
    """

    class DatabaseEngine(proto.Enum):
        r"""Database engine of a Cloud SQL instance.
        New values may be added over time.

        Values:
            DATABASE_ENGINE_UNKNOWN (0):
                An engine that is not currently supported by
                Sensitive Data Protection.
            DATABASE_ENGINE_MYSQL (1):
                Cloud SQL for MySQL instance.
            DATABASE_ENGINE_POSTGRES (2):
                Cloud SQL for PostgreSQL instance.
        """

        DATABASE_ENGINE_UNKNOWN = 0
        DATABASE_ENGINE_MYSQL = 1
        DATABASE_ENGINE_POSTGRES = 2

    connection_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    username_password: "SecretManagerCredential" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="credential",
        message="SecretManagerCredential",
    )
    cloud_sql_iam: "CloudSqlIamCredential" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="credential",
        message="CloudSqlIamCredential",
    )
    max_connections: int = proto.Field(
        proto.INT32,
        number=4,
    )
    database_engine: DatabaseEngine = proto.Field(
        proto.ENUM,
        number=7,
        enum=DatabaseEngine,
    )


class DeleteTableDataProfileRequest(proto.Message):
    r"""Request message for DeleteTableProfile.

    Attributes:
        name (str):
            Required. Resource name of the table data
            profile.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DataSourceType(proto.Message):
    r"""Message used to identify the type of resource being profiled.

    Attributes:
        data_source (str):
            A string that identifies the type of resource being
            profiled. Current values:

            - google/bigquery/table
            - google/project
            - google/sql/table
            - google/gcs/bucket
    """

    data_source: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FileClusterType(proto.Message):
    r"""Message used to identify file cluster type being profiled.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        cluster (google.cloud.dlp_v2.types.FileClusterType.Cluster):
            Cluster type.

            This field is a member of `oneof`_ ``file_cluster_type``.
    """

    class Cluster(proto.Enum):
        r"""Cluster type. Each cluster corresponds to a set of file
        types. Over time, new types may be added and files may move
        between clusters.

        Values:
            CLUSTER_UNSPECIFIED (0):
                Unused.
            CLUSTER_UNKNOWN (1):
                Unsupported files.
            CLUSTER_TEXT (2):
                Plain text.
            CLUSTER_STRUCTURED_DATA (3):
                Structured data like CSV, TSV etc.
            CLUSTER_SOURCE_CODE (4):
                Source code.
            CLUSTER_RICH_DOCUMENT (5):
                Rich document like docx, xlsx etc.
            CLUSTER_IMAGE (6):
                Images like jpeg, bmp.
            CLUSTER_ARCHIVE (7):
                Archives and containers like .zip, .tar etc.
            CLUSTER_MULTIMEDIA (8):
                Multimedia like .mp4, .avi etc.
            CLUSTER_EXECUTABLE (9):
                Executable files like .exe, .class, .apk etc.
            CLUSTER_AI_MODEL (10):
                AI models like .tflite etc.
        """

        CLUSTER_UNSPECIFIED = 0
        CLUSTER_UNKNOWN = 1
        CLUSTER_TEXT = 2
        CLUSTER_STRUCTURED_DATA = 3
        CLUSTER_SOURCE_CODE = 4
        CLUSTER_RICH_DOCUMENT = 5
        CLUSTER_IMAGE = 6
        CLUSTER_ARCHIVE = 7
        CLUSTER_MULTIMEDIA = 8
        CLUSTER_EXECUTABLE = 9
        CLUSTER_AI_MODEL = 10

    cluster: Cluster = proto.Field(
        proto.ENUM,
        number=1,
        oneof="file_cluster_type",
        enum=Cluster,
    )


class ProcessingLocation(proto.Message):
    r"""Configure processing location for discovery and inspection.
    For example, image OCR is only provided in limited regions but
    configuring ProcessingLocation will redirect OCR to a location
    where OCR is provided.

    Attributes:
        image_fallback_location (google.cloud.dlp_v2.types.ProcessingLocation.ImageFallbackLocation):
            Image processing falls back using this
            configuration.
        document_fallback_location (google.cloud.dlp_v2.types.ProcessingLocation.DocumentFallbackLocation):
            Document processing falls back using this
            configuration.
    """

    class MultiRegionProcessing(proto.Message):
        r"""Processing occurs in a multi-region that contains the current
        region if available.

        """

    class GlobalProcessing(proto.Message):
        r"""Processing occurs in the global region."""

    class ImageFallbackLocation(proto.Message):
        r"""Configure image processing to fall back to any of the
        following processing options if image processing is unavailable
        in the original request location.

        Attributes:
            multi_region_processing (google.cloud.dlp_v2.types.ProcessingLocation.MultiRegionProcessing):
                Processing occurs in a multi-region that
                contains the current region if available.
            global_processing (google.cloud.dlp_v2.types.ProcessingLocation.GlobalProcessing):
                Processing occurs in the global region.
        """

        multi_region_processing: "ProcessingLocation.MultiRegionProcessing" = (
            proto.Field(
                proto.MESSAGE,
                number=100,
                message="ProcessingLocation.MultiRegionProcessing",
            )
        )
        global_processing: "ProcessingLocation.GlobalProcessing" = proto.Field(
            proto.MESSAGE,
            number=200,
            message="ProcessingLocation.GlobalProcessing",
        )

    class DocumentFallbackLocation(proto.Message):
        r"""Configure document processing to fall back to any of the
        following processing options if document processing is
        unavailable in the original request location.

        Attributes:
            multi_region_processing (google.cloud.dlp_v2.types.ProcessingLocation.MultiRegionProcessing):
                Processing occurs in a multi-region that
                contains the current region if available.
            global_processing (google.cloud.dlp_v2.types.ProcessingLocation.GlobalProcessing):
                Processing occurs in the global region.
        """

        multi_region_processing: "ProcessingLocation.MultiRegionProcessing" = (
            proto.Field(
                proto.MESSAGE,
                number=100,
                message="ProcessingLocation.MultiRegionProcessing",
            )
        )
        global_processing: "ProcessingLocation.GlobalProcessing" = proto.Field(
            proto.MESSAGE,
            number=200,
            message="ProcessingLocation.GlobalProcessing",
        )

    image_fallback_location: ImageFallbackLocation = proto.Field(
        proto.MESSAGE,
        number=1,
        message=ImageFallbackLocation,
    )
    document_fallback_location: DocumentFallbackLocation = proto.Field(
        proto.MESSAGE,
        number=2,
        message=DocumentFallbackLocation,
    )


class SaveToGcsFindingsOutput(proto.Message):
    r"""Collection of findings saved to a Cloud Storage bucket. This
    is used as the proto schema for textproto files created when
    specifying a cloud storage path to save Inspect findings.

    Attributes:
        findings (MutableSequence[google.cloud.dlp_v2.types.Finding]):
            List of findings.
    """

    findings: MutableSequence["Finding"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Finding",
    )


class Domain(proto.Message):
    r"""A domain represents a thematic category that a data profile
    can fall under.

    Attributes:
        category (google.cloud.dlp_v2.types.Domain.Category):
            A domain category that this profile is
            related to.
        signals (MutableSequence[google.cloud.dlp_v2.types.Domain.Signal]):
            The collection of signals that influenced
            selection of the category.
    """

    class Category(proto.Enum):
        r"""This enum defines the various domain categories a data
        profile can fall under.

        Values:
            CATEGORY_UNSPECIFIED (0):
                Category unspecified.
            AI (1):
                Indicates that the data profile is related to artificial
                intelligence. When set, all findings stored to Security
                Command Center will set the corresponding AI domain field of
                ``Finding`` objects.
            CODE (2):
                Indicates that the data profile is related to
                code.
        """

        CATEGORY_UNSPECIFIED = 0
        AI = 1
        CODE = 2

    class Signal(proto.Enum):
        r"""The signal used to determine the category.
        New values may be added in the future.

        Values:
            SIGNAL_UNSPECIFIED (0):
                Unused.
            MODEL (1):
                One or more machine learning models are
                present.
            TEXT_EMBEDDING (2):
                A table appears to contain text embeddings.
            EMBEDDING (7):
                A table appears to contain embeddings of any type (for
                example, text, image, multimodal). The ``TEXT_EMBEDDING``
                signal might also be present if the table contains text
                embeddings.
            VERTEX_PLUGIN (3):
                The `Cloud SQL Vertex
                AI <https://docs.cloud.google.com/sql/docs/postgres/integrate-cloud-sql-with-vertex-ai>`__
                plugin is installed on the database.
            VECTOR_PLUGIN (4):
                Support for `Cloud SQL vector
                embeddings <https://docs.cloud.google.com/sql/docs/mysql/enable-vector-search>`__
                is enabled on the database.
            SOURCE_CODE (5):
                Source code is present.
            SERVICE (6):
                If the service determines the category type. For example,
                Vertex AI assets would always have a ``Category`` of ``AI``.
        """

        SIGNAL_UNSPECIFIED = 0
        MODEL = 1
        TEXT_EMBEDDING = 2
        EMBEDDING = 7
        VERTEX_PLUGIN = 3
        VECTOR_PLUGIN = 4
        SOURCE_CODE = 5
        SERVICE = 6

    category: Category = proto.Field(
        proto.ENUM,
        number=1,
        enum=Category,
    )
    signals: MutableSequence[Signal] = proto.RepeatedField(
        proto.ENUM,
        number=2,
        enum=Signal,
    )


class CreateContentPolicyRequest(proto.Message):
    r"""Request message for CreateContentPolicy.

    Attributes:
        parent (str):
            Required. Parent resource name.

            The format of this value varies depending on the scope of
            the request (project):

            - Projects scope:
              ``projects/{project_id}/locations/{location_id}``
        content_policy (google.cloud.dlp_v2.types.ContentPolicy):
            Required. The content_policy resource.
        content_policy_id (str):
            Optional. The content policy ID can contain uppercase and
            lowercase letters, numbers, and hyphens; that is, it must
            match the regular expression: ``[a-zA-Z\d-_]+``. The maximum
            length is 100 characters. If empty, the system will generate
            a random id.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    content_policy: "ContentPolicy" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ContentPolicy",
    )
    content_policy_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GetContentPolicyRequest(proto.Message):
    r"""Request message for GetContentPolicy.

    Attributes:
        name (str):
            Required. Resource name in the format:
            ``projects/{project}/locations/{location}/contentPolicies/{content_policy}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListContentPoliciesRequest(proto.Message):
    r"""Request message for ListContentPolicies.

    Attributes:
        parent (str):
            Required. Resource name of the project, for example,
            ``projects/project-id/locations/asia``.
        page_size (int):
            Optional. Number of results per page, max
            1000.
        page_token (str):
            Optional. Page token from a previous page to
            return the next set of results. If set, all
            other request fields must match the original
            request.
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


class ListContentPoliciesResponse(proto.Message):
    r"""Response message for ListContentPolicies.

    Attributes:
        content_policies (MutableSequence[google.cloud.dlp_v2.types.ContentPolicy]):
            List of content policies.
        next_page_token (str):
            Token to retrieve the next page of results.
            An empty value means there are no more results.
    """

    @property
    def raw_page(self):
        return self

    content_policies: MutableSequence["ContentPolicy"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ContentPolicy",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateContentPolicyRequest(proto.Message):
    r"""Request message for UpdateContentPolicy.

    Attributes:
        name (str):
            Required. Resource name in the format:
            ``projects/{project}/locations/{location}/contentPolicies/{content_policy}``.
        content_policy (google.cloud.dlp_v2.types.ContentPolicy):
            Required. The content_policy with new values for the
            relevant fields.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Mask to control which fields get
            updated.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    content_policy: "ContentPolicy" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ContentPolicy",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


class DeleteContentPolicyRequest(proto.Message):
    r"""Request message for DeleteContentPolicy.

    Attributes:
        name (str):
            Required. Resource name of the ContentPolicy to be deleted,
            in the format:
            ``projects/{project}/locations/{location}/contentPolicies/{content_policy}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ContentPolicy(proto.Message):
    r"""A policy to apply to content based on its inspection
    findings.

    Attributes:
        name (str):
            Output only. Resource name of the policy.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation timestamp of a
            contentPolicy; output-only field.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last update timestamp of a
            contentPolicy; output-only field.
        display_name (str):
            Optional. Display name (max 63 chars)
        inspect_config (google.cloud.dlp_v2.types.InspectConfig):
            Optional. InspectConfig to use to produce
            findings.
        rules (MutableSequence[google.cloud.dlp_v2.types.ContentPolicy.PolicyRule]):
            Required. Policies to apply, based on the
            findings returned by inspection. The first rule
            to match applies.
        unsupported_file_type (google.cloud.dlp_v2.types.ContentPolicy.PolicyAction):
            Optional. Action to take if the content is an
            unsupported file type.
        input_too_large (google.cloud.dlp_v2.types.ContentPolicy.PolicyAction):
            Optional. Action to take if the content is a
            supported file type but is too large to be
            scanned.
        failed_to_scan_supported_file_type (google.cloud.dlp_v2.types.ContentPolicy.PolicyAction):
            Optional. Action to take if the content is a
            supported file type and size but fails to be
            scanned, for example because the file is
            encrypted or corrupted.
        default_action (google.cloud.dlp_v2.types.ContentPolicy.PolicyAction):
            Action to take if the content is scanned and
            no rules match. Defaults to returning an ALLOW
            verdict if not set.
        logging_configs (MutableSequence[google.cloud.dlp_v2.types.ContentPolicy.LoggingConfig]):
            Optional. Log the actions taken by the
            content policy to external systems.
        errors (MutableSequence[google.cloud.dlp_v2.types.Error]):
            Output only. A stream of errors encountered
            when the policy was applied. Output only field.
            Will return the last 100 errors. Whenever the
            policy is modified this list will be cleared.
    """

    class PolicyAction(proto.Message):
        r"""A possible action to take when applying a content policy.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            return_verdict (google.cloud.dlp_v2.types.ContentPolicyVerdict):
                Optional. If set, the verdict will be
                returned to the user.

                This field is a member of `oneof`_ ``action``.
        """

        return_verdict: "ContentPolicyVerdict" = proto.Field(
            proto.ENUM,
            number=1,
            oneof="action",
            enum="ContentPolicyVerdict",
        )

    class PolicyRule(proto.Message):
        r"""A single policy rule. The first rule to match from the list
        above controls the result.

        Attributes:
            conditions (MutableSequence[google.cloud.dlp_v2.types.ContentPolicy.PolicyRule.PolicyCondition]):
                Optional. Conditions that must match for this rule to apply.
                All conditions must match (``AND``). For ``OR`` conditions,
                use multiple rules.
            action (google.cloud.dlp_v2.types.ContentPolicy.PolicyAction):
                Required. Action to take if this rule
                applies.
        """

        class PolicyCondition(proto.Message):
            r"""A condition that must match for this rule to apply.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                info_type_condition (google.cloud.dlp_v2.types.ContentPolicy.PolicyRule.PolicyCondition.InfoTypeCondition):
                    A condition based on info types.

                    This field is a member of `oneof`_ ``condition``.
            """

            class InfoTypeCondition(proto.Message):
                r"""A info type based condition.

                This message has `oneof`_ fields (mutually exclusive fields).
                For each oneof, at most one member field can be set at the same time.
                Setting any member of the oneof automatically clears all other
                members.

                .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

                Attributes:
                    min_count (int):
                        Optional. The minimum total number of
                        findings of all matching info types required for
                        this condition to evaluate to true. Defaults to
                        1 if unset.
                    info_types (google.cloud.dlp_v2.types.ContentPolicy.PolicyRule.PolicyCondition.InfoTypeCondition.InfoTypes):
                        match any of these info types.

                        This field is a member of `oneof`_ ``info_type_condition``.
                    any_info_type (google.protobuf.empty_pb2.Empty):
                        match any info types.

                        This field is a member of `oneof`_ ``info_type_condition``.
                """

                class InfoTypes(proto.Message):
                    r"""Info types to match.

                    Attributes:
                        info_type_names (MutableSequence[str]):
                            Required. A list of info types to match.
                    """

                    info_type_names: MutableSequence[str] = proto.RepeatedField(
                        proto.STRING,
                        number=1,
                    )

                min_count: int = proto.Field(
                    proto.INT64,
                    number=3,
                )
                info_types: "ContentPolicy.PolicyRule.PolicyCondition.InfoTypeCondition.InfoTypes" = proto.Field(
                    proto.MESSAGE,
                    number=1,
                    oneof="info_type_condition",
                    message="ContentPolicy.PolicyRule.PolicyCondition.InfoTypeCondition.InfoTypes",
                )
                any_info_type: empty_pb2.Empty = proto.Field(
                    proto.MESSAGE,
                    number=2,
                    oneof="info_type_condition",
                    message=empty_pb2.Empty,
                )

            info_type_condition: "ContentPolicy.PolicyRule.PolicyCondition.InfoTypeCondition" = proto.Field(
                proto.MESSAGE,
                number=1,
                oneof="condition",
                message="ContentPolicy.PolicyRule.PolicyCondition.InfoTypeCondition",
            )

        conditions: MutableSequence["ContentPolicy.PolicyRule.PolicyCondition"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="ContentPolicy.PolicyRule.PolicyCondition",
            )
        )
        action: "ContentPolicy.PolicyAction" = proto.Field(
            proto.MESSAGE,
            number=5,
            message="ContentPolicy.PolicyAction",
        )

    class LoggingConfig(proto.Message):
        r"""A single logging configuration.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            log_to_big_query (google.cloud.dlp_v2.types.ContentPolicy.LoggingConfig.LogToBigQuery):
                Optional. Log the actions taken to a BigQuery
                table.

                This field is a member of `oneof`_ ``destination``.
        """

        class LogToBigQuery(proto.Message):
            r"""Configuration for logging content policy actions to BigQuery.

            Attributes:
                project_id (str):
                    Required. The ID of the project containing
                    the BigQuery table to write to.
                dataset_id (str):
                    Required. The ID of the dataset containing
                    the BigQuery table to write to.
                table_id (str):
                    Required. The ID of the BigQuery table to
                    write to.
            """

            project_id: str = proto.Field(
                proto.STRING,
                number=1,
            )
            dataset_id: str = proto.Field(
                proto.STRING,
                number=2,
            )
            table_id: str = proto.Field(
                proto.STRING,
                number=3,
            )

        log_to_big_query: "ContentPolicy.LoggingConfig.LogToBigQuery" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="destination",
            message="ContentPolicy.LoggingConfig.LogToBigQuery",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=13,
        message=timestamp_pb2.Timestamp,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    inspect_config: "InspectConfig" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="InspectConfig",
    )
    rules: MutableSequence[PolicyRule] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=PolicyRule,
    )
    unsupported_file_type: PolicyAction = proto.Field(
        proto.MESSAGE,
        number=8,
        message=PolicyAction,
    )
    input_too_large: PolicyAction = proto.Field(
        proto.MESSAGE,
        number=9,
        message=PolicyAction,
    )
    failed_to_scan_supported_file_type: PolicyAction = proto.Field(
        proto.MESSAGE,
        number=10,
        message=PolicyAction,
    )
    default_action: PolicyAction = proto.Field(
        proto.MESSAGE,
        number=11,
        message=PolicyAction,
    )
    logging_configs: MutableSequence[LoggingConfig] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=LoggingConfig,
    )
    errors: MutableSequence["Error"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="Error",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
