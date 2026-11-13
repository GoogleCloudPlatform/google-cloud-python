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

import google.api.httpbody_pb2 as httpbody_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.chronicle.v1",
    manifest={
        "URISourceType",
        "SourceDeletionOption",
        "SourceDeletionOptionV2",
        "S3Region",
        "SemanticType",
        "FeedPack",
        "PackLogType",
        "Feed",
        "FeedFailureDetails",
        "FeedServiceAccount",
        "FeedDetails",
        "DummyLogTypeSettings",
        "HttpsPushGoogleCloudPubSubSettings",
        "HttpsPushAmazonKinesisFirehoseSettings",
        "HttpsPushWebhookSettings",
        "SentineloneAlertSettings",
        "QualysScanSettings",
        "PubsubSettings",
        "AmazonKinesisFirehoseSettings",
        "WebhookSettings",
        "AmazonSQSSettings",
        "AnomaliIocSettings",
        "AzureADSettings",
        "AzureADAuditSettings",
        "AzureADContextSettings",
        "CloudPassageSettings",
        "CortexXDRSettings",
        "CrowdStrikeDetectsSettings",
        "CrowdStrikeAlertsSettings",
        "DuoAuthSettings",
        "DuoUserContextSettings",
        "MicrosoftGraphAlertSettings",
        "MicrosoftSecurityCenterAlertSettings",
        "MimecastMailSettings",
        "MimecastMailV2Settings",
        "Office365Settings",
        "ProofpointMailSettings",
        "ProofpointOnDemandSettings",
        "RecordedFutureIocSettings",
        "WorkdaySettings",
        "PanIocSettings",
        "OktaSettings",
        "OktaUserContextSettings",
        "FoxITStixSettings",
        "ThreatConnectIoCSettings",
        "ThreatConnectIoCV3Settings",
        "ServiceNowCMDBSettings",
        "ImpervaWAFSettings",
        "ThinkstCanarySettings",
        "RHIsacIocSettings",
        "Rapid7InsightSettings",
        "SalesforceSettings",
        "MandiantIoCSettings",
        "NetskopeAlertSettings",
        "NetskopeAlertV2Settings",
        "AzureMDMIntuneSettings",
        "WorkspaceUsersSettings",
        "WorkspaceActivitySettings",
        "WorkspaceAlertsSettings",
        "WorkspacePrivilegesSettings",
        "WorkspaceMobileSettings",
        "WorkspaceChromeOSSettings",
        "WorkspaceGroupsSettings",
        "GoogleCloudIdentityDevicesSettings",
        "GoogleCloudIdentityDeviceUsersSettings",
        "SymantecEventExportSettings",
        "QualysVMSettings",
        "PanPrismaCloudSettings",
        "SftpSettings",
        "GoogleCloudStorageSettings",
        "HttpSettings",
        "AmazonS3Settings",
        "AzureBlobStoreSettings",
        "AWSEC2HostsSettings",
        "AWSEC2InstancesSettings",
        "AWSEC2VpcsSettings",
        "AWSIAMSettings",
        "AzureAuth",
        "SQSAuth",
        "SQSAuthV2",
        "SQSV2AwsIamRoleAuth",
        "SQSV2AccessKeySecretAuth",
        "SQSAccessKeySecretAuth",
        "AdditionalS3AccessKeySecretAuth",
        "S3Auth",
        "OAuthRefreshToken",
        "SftpAuth",
        "HttpHeaderAuth",
        "HeaderKeyValue",
        "UsernameSecretAuth",
        "MicrosoftOAuthClientCredentials",
        "OAuthClientCredentials",
        "OAuthPasswordGrantCredentials",
        "PanPrismaAuth",
        "OAuthJWTCredentials",
        "RSCredentials",
        "Claims",
        "SSLClientKeypair",
        "WorkdayAuth",
        "GoogleCloudStorageV2Settings",
        "GoogleCloudStorageEventDrivenSettings",
        "S3AuthV2",
        "S3V2AwsIamRoleAuth",
        "S3V2AccessKeySecretAuth",
        "AmazonS3V2Settings",
        "MssoAuthentication",
        "MimecastV2OAuthClientCredentials",
        "TrellixIAMAuthentication",
        "TrellixLocalAuthentication",
        "TrellixStarXAuthentication",
        "TrellixHxHostsSettings",
        "TrellixHxAlertsSettings",
        "TrellixHxBulkAcqsSettings",
        "AzureEventHubSettings",
        "AmazonSQSV2Settings",
        "AzureBlobStoreV2Settings",
        "AzureV2WorkloadIdentityFederation",
        "AzureAuthV2",
        "FeedSourceTypeSchema",
        "LogTypeSchema",
        "FetchServiceAccountForCustomerRequest",
        "ListFeedSourceTypeSchemasRequest",
        "ListFeedSourceTypeSchemasResponse",
        "ListLogTypeSchemasRequest",
        "ListLogTypeSchemasResponse",
        "ImportPushLogsRequest",
        "UpdateFeedRequest",
        "ListFeedsRequest",
        "ListFeedsResponse",
        "ListFeedPacksRequest",
        "ListFeedPacksResponse",
        "GetFeedPackRequest",
        "CreateFeedRequest",
        "GetFeedRequest",
        "DeleteFeedRequest",
        "EnableFeedRequest",
        "GenerateSecretRequest",
        "GenerateSecretResponse",
        "DisableFeedRequest",
        "CustomAPIHeaderKeyValue",
        "CustomAPIHeaderAuth",
        "CustomAPIQueryKeyValue",
        "CustomAPIQueryAuth",
        "CustomAPINoAuth",
        "CustomAPISettings",
        "CustomAPITransferNode",
        "CustomAPIDependentRequestsConfig",
        "CustomAPIRequestConfig",
        "CustomAPIResponseConfig",
        "CustomAPICheckpointConfig",
        "CustomAPIPagination",
    },
)


class URISourceType(proto.Enum):
    r"""The type of URIs specified in the source URIs.

    Values:
        URI_SOURCE_TYPE_UNSPECIFIED (0):
            If encountered, will throw an ``INVALID_ARGUMENT`` error.
        FILES (1):
            The type of files pointed to by ``source_uris`` are files.
        FOLDERS (2):
            The type of files pointed to by ``source_uris`` are folders
            and Xenon should not descend into subfolders of those
            folders.
        FOLDERS_RECURSIVE (3):
            The type of files pointed to by ``source_uris`` are folders
            and Xenon should descend into subfolders of those folders.
    """

    URI_SOURCE_TYPE_UNSPECIFIED = 0
    FILES = 1
    FOLDERS = 2
    FOLDERS_RECURSIVE = 3


class SourceDeletionOption(proto.Enum):
    r"""Source deletion option controls whether source files should
    be deleted after transferring.

    Values:
        SOURCE_DELETION_OPTION_UNSPECIFIED (0):
            If encountered, will be treated as
            ``SOURCE_DELETION_NEVER``.
        SOURCE_DELETION_NEVER (1):
            Never delete files from the source.
        SOURCE_DELETION_ON_SUCCESS (2):
            After the fetch completes, if there are no
            errors, delete files and any directories made
            empty by the file deletion from the source.
        SOURCE_DELETION_ON_SUCCESS_FILES_ONLY (3):
            After the fetch completes, if there are no
            errors, delete files (leaving any directories)
            from the source.
    """

    SOURCE_DELETION_OPTION_UNSPECIFIED = 0
    SOURCE_DELETION_NEVER = 1
    SOURCE_DELETION_ON_SUCCESS = 2
    SOURCE_DELETION_ON_SUCCESS_FILES_ONLY = 3


class SourceDeletionOptionV2(proto.Enum):
    r"""Source deletion option determines whether source files should
    be deleted after transferring.

    Values:
        SOURCE_DELETION_OPTION_V2_UNSPECIFIED (0):
            If encountered, will be treated as
            ``SOURCE_DELETION_NEVER``.
        NEVER (1):
            Never delete files from the source.
        ON_SUCCESS (2):
            After the fetch completes, if there are no
            errors, delete files and any directories made
            empty by the file deletion from the source.
    """

    SOURCE_DELETION_OPTION_V2_UNSPECIFIED = 0
    NEVER = 1
    ON_SUCCESS = 2


class S3Region(proto.Enum):
    r"""AWS S3 regions:
    https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region.

    Values:
        S3_REGION_UNSPECIFIED (0):
            Unspecified region means Auto detect.
            Auto detect does not successfully detect GOV
            Cloud.
        US_EAST_1 (1):
            US. N. Virginia (previously known as US_STANDARD).
        US_EAST_2 (2):
            Ohio.
        US_WEST_1 (3):
            N. California.
        US_WEST_2 (4):
            Oregon.
        US_GOV_CLOUD (5):
            Not accessible unless AWS US Govt. account.
        US_GOV_EAST_1 (6):
            Not accessible unless AWS US Govt. account.
        EU_WEST_1 (7):
            Europe.
            Ireland.
        EU_WEST_2 (8):
            London.
        EU_WEST_3 (9):
            Paris.
        EU_CENTRAL_1 (10):
            Frankfurt.
        EU_NORTH_1 (11):
            Stockholm.
        EU_SOUTH_1 (21):
            Milan.
        AP_SOUTH_1 (12):
            Asia Pacific
            Mumbai.
        AP_SOUTHEAST_1 (13):
            Singapore.
        AP_SOUTHEAST_2 (14):
            Sydney.
        AP_SOUTHEAST_3 (22):
            Jakarta.
        AP_NORTHEAST_1 (15):
            Tokyo.
        AP_NORTHEAST_2 (16):
            Seoul.
        AP_NORTHEAST_3 (23):
            Osaka.
        AP_EAST_1 (24):
            Hong Kong.
        SA_EAST_1 (17):
            South America.
            Sao Paulo.
        CN_NORTH_1 (18):
            China - Not accessible unless AWS China
            account. China - Beijing.
        CN_NORTHWEST_1 (19):
            China - Ningxia.
        CA_CENTRAL_1 (20):
            Canada.
            Canada Central.
        AF_SOUTH_1 (25):
            Africa.
            Capetown.
        ME_SOUTH_1 (26):
            Middle East.
            Bahrain.
        AP_SOUTH_2 (27):
            Asia Pacific (Hyderabad).
        AP_SOUTHEAST_4 (28):
            Asia Pacific (Melbourne).
        CA_WEST_1 (29):
            Canada West (Calgary).
        EU_SOUTH_2 (30):
            Europe (Spain).
        EU_CENTRAL_2 (31):
            Europe (Zurich).
        IL_CENTRAL_1 (32):
            Israel (Tel Aviv).
        ME_CENTRAL_1 (33):
            Middle East (UAE).
    """

    S3_REGION_UNSPECIFIED = 0
    US_EAST_1 = 1
    US_EAST_2 = 2
    US_WEST_1 = 3
    US_WEST_2 = 4
    US_GOV_CLOUD = 5
    US_GOV_EAST_1 = 6
    EU_WEST_1 = 7
    EU_WEST_2 = 8
    EU_WEST_3 = 9
    EU_CENTRAL_1 = 10
    EU_NORTH_1 = 11
    EU_SOUTH_1 = 21
    AP_SOUTH_1 = 12
    AP_SOUTHEAST_1 = 13
    AP_SOUTHEAST_2 = 14
    AP_SOUTHEAST_3 = 22
    AP_NORTHEAST_1 = 15
    AP_NORTHEAST_2 = 16
    AP_NORTHEAST_3 = 23
    AP_EAST_1 = 24
    SA_EAST_1 = 17
    CN_NORTH_1 = 18
    CN_NORTHWEST_1 = 19
    CA_CENTRAL_1 = 20
    AF_SOUTH_1 = 25
    ME_SOUTH_1 = 26
    AP_SOUTH_2 = 27
    AP_SOUTHEAST_4 = 28
    CA_WEST_1 = 29
    EU_SOUTH_2 = 30
    EU_CENTRAL_2 = 31
    IL_CENTRAL_1 = 32
    ME_CENTRAL_1 = 33


class SemanticType(proto.Enum):
    r"""An enumeration of the possible types of a ``Feed.details`` field,
    where type implies both encoding and semantics. This is used in
    constructing a schema in order to construct a UI for creating well
    formed feeds.

    Values:
        SEMANTIC_TYPE_UNSPECIFIED (0):
            No semantic type. All fields must specify a
            semantic type.
        BOOL (1):
            A boolean (with no special semantics).
        ENUM (2):
            An enum (with no special semantics).
        KEY_VALUE_LIST (3):
            A repeated field with a Message type where the Message
            contains two fields: ``key`` and ``value``.
        MAP_STRING_STRING (4):
            A ``map<string, string>`` (with no special semantics).
        STRING (5):
            A string (with no special semantics).
        STRING_LIST (6):
            A repeated string (with no special
            semantics).
        STRING_MULTILINE (7):
            A string that may contain any whitespace
            characters (with no special semantics).
        STRING_MULTILINE_SECRET (8):
            A string that may contain any whitespace
            characters and that encodes a secret.
        STRING_SECRET (9):
            A string which encodes a secret.
        STRING_URI (10):
            A string which encodes a URI.
        STRING_URI_LIST (11):
            A repeated string which encodes URIs.
    """

    SEMANTIC_TYPE_UNSPECIFIED = 0
    BOOL = 1
    ENUM = 2
    KEY_VALUE_LIST = 3
    MAP_STRING_STRING = 4
    STRING = 5
    STRING_LIST = 6
    STRING_MULTILINE = 7
    STRING_MULTILINE_SECRET = 8
    STRING_SECRET = 9
    STRING_URI = 10
    STRING_URI_LIST = 11


class FeedPack(proto.Message):
    r"""FeedPack is a logical container for related LogTypes for
    which feeds can be configured.

    Attributes:
        name (str):
            Identifier. The resource name of the feed pack. Format:
            projects/{project}/locations/{location}/instances/{instance}/feedPacks/{feed_pack}
        display_name (str):
            Output only. The display name of the feed
            pack.
        description (str):
            Output only. The description of the feed
            pack.
        icon (bytes):
            Output only. The icon image of the content
            pack in base64 in png format.
        categories (MutableSequence[str]):
            Output only. Categories the featured content
            is associated with. In case of product feed
            packs, there will be only one category.
        pack_type (google.cloud.chronicle_v1.types.FeedPack.PackType):
            Output only. Type of pack.
        pack_log_types (MutableSequence[google.cloud.chronicle_v1.types.PackLogType]):
            Output only. Log types featured in the pack.
        hidden (bool):
            Output only. Whether the feed pack should be
            displayed in the Feeds Page.
        pack_documentation (str):
            Output only. Pack specific documentation in
            markdown format.
    """

    class PackType(proto.Enum):
        r"""Type of feed pack. Feeds Page currently only lists PRODUCT_BASED
        packs.

        Values:
            PACK_TYPE_UNSPECIFIED (0):
                Unspecified feed pack type.
            PRODUCT_BASED (1):
                Product based feed pack type.
            USECASE_BASED (2):
                Use case based feed pack type.
            ONBOARDING (3):
                Onboarding feed pack type.
        """

        PACK_TYPE_UNSPECIFIED = 0
        PRODUCT_BASED = 1
        USECASE_BASED = 2
        ONBOARDING = 3

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
    icon: bytes = proto.Field(
        proto.BYTES,
        number=4,
    )
    categories: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    pack_type: PackType = proto.Field(
        proto.ENUM,
        number=6,
        enum=PackType,
    )
    pack_log_types: MutableSequence["PackLogType"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="PackLogType",
    )
    hidden: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    pack_documentation: str = proto.Field(
        proto.STRING,
        number=9,
    )


class PackLogType(proto.Message):
    r"""PackLogtype is a log type featured in the feed pack.

    Attributes:
        log_type (str):
            Log Type featured in the feed pack. Format:
            projects/{project}/locations/{location}/instances/{instance}/logTypes/{log_type}
        required (bool):
            Whether the logtype is required to deploy a
            feed pack.
        has_default_parser (bool):
            Whether a default(prebuilt) parser is
            available for the given log type.
        recommended_source_type (google.cloud.chronicle_v1.types.FeedDetails.FeedSourceType):
            The recommended source type for the log type.
        display_name (str):
            The display name of the log type.
        configuration_documentation (str):
            Documentation to define steps on how to
            configure a log type.
        additional_documentation (str):
            Documentation to share any CTAs for more
            reference.
    """

    log_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    required: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    has_default_parser: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    recommended_source_type: "FeedDetails.FeedSourceType" = proto.Field(
        proto.ENUM,
        number=4,
        enum="FeedDetails.FeedSourceType",
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    configuration_documentation: str = proto.Field(
        proto.STRING,
        number=6,
    )
    additional_documentation: str = proto.Field(
        proto.STRING,
        number=7,
    )


class Feed(proto.Message):
    r"""Feed is a resource that contains feed information needed to
    create a feed.

    Attributes:
        name (str):
            The resource name of the feed.
            Format:

            projects/{project}/locations/{location}/instances/{instance}/feeds/{feed}
        uid (str):
            Output only. Unique identifier for the feed.
        display_name (str):
            Customer-provided feed name.
        details (google.cloud.chronicle_v1.types.FeedDetails):
            Additional details of the feed, these details
            are dynamic and will be different for each of
            the feeds.
        state (google.cloud.chronicle_v1.types.Feed.State):
            Output only. State of the feed.
        failure_msg (str):
            Output only. Details about the most recent
            failure when feed state is FAILED.
        read_only (bool):
            Output only. Whether this feed can be updated
            or deleted.
        last_feed_initiation_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Latest timestamp when the
            transfer was successful for the feed.
        failure_details (google.cloud.chronicle_v1.types.FeedFailureDetails):
            Output only. Failure details for the feed. If
            the feed is in the failure state, this field
            will contain the details of the error cause and
            actions.
        reference_id (str):
            Output only. Reference ID, this field will
            contain the legacy id of the feed.
    """

    class State(proto.Enum):
        r"""List of states a feed can have.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified feed state.
            ACTIVE (1):
                Feed is configured and ready to ingest data.
                Newly created feeds have this state. Once
                ingestion begins the feed will transition out of
                this state and will not transition back.
            INACTIVE (2):
                Feed is Disabled. When a user disables a feed
                it will transition to this state regardless of
                its current state. Once enabled a feed will
                transition to its previous state.
            RUNNING (3):
                Feed is enabled and currently ingesting data.
                A feed will transition to this state from an
                ACTIVE or COMPLETED state when Chronicle has
                begun fetching data for this feed.
            SUCCEEDED (4):
                Feed is enabled and has recently successfully
                ingested data. A feed will transition to this
                state from RUNNING or FAILED once a fetch has
                completed successfully.
            FAILED (5):
                Feed is enabled, but has recently failed to
                ingest data. A feed will transition to this
                state only from RUNNING once a fetch has failed.
                It will remain in this state until a subsequent
                fetch has succeeded.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        INACTIVE = 2
        RUNNING = 3
        SUCCEEDED = 4
        FAILED = 5

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=9,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    details: "FeedDetails" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="FeedDetails",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )
    failure_msg: str = proto.Field(
        proto.STRING,
        number=5,
    )
    read_only: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    last_feed_initiation_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    failure_details: "FeedFailureDetails" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="FeedFailureDetails",
    )
    reference_id: str = proto.Field(
        proto.STRING,
        number=10,
    )


class FeedFailureDetails(proto.Message):
    r"""FeedFailureDetails contains details about the errors thrown
    by chronicle for the feeds. These are user visible details.
    These details help user identify the root cause and take
    appropriate action for the feed errors.

    Attributes:
        error_code (str):
            Output only. error_code contains the error code for the
            feed. The field is populated for the feeds with failed
            status.
        http_error_code (int):
            Output only. http_error_code contains the HTTP error code
            for the feed failure. feed transfer failure may or may not
            result in http error code.
        error_cause (str):
            Output only. error_cause contains the information regarding
            the failure cause.
        error_action (str):
            Output only. error_action contains the user action
            prescribed for remediation of feed error.
    """

    error_code: str = proto.Field(
        proto.STRING,
        number=1,
    )
    http_error_code: int = proto.Field(
        proto.INT32,
        number=2,
    )
    error_cause: str = proto.Field(
        proto.STRING,
        number=3,
    )
    error_action: str = proto.Field(
        proto.STRING,
        number=4,
    )


class FeedServiceAccount(proto.Message):
    r"""FeedServiceAccount is a resource that wraps the feed service
    account's name.

    Attributes:
        name (str):
            The resource name of the feedServiceAccount.
            Format:

            projects/{project}/locations/{location}/instances/{instance}/feedServiceAccounts/{feedserviceaccount}
        subject_id (str):
            Unique identifier for the service account.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    subject_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class FeedDetails(proto.Message):
    r"""Additional details of the feed, these details are dynamic and
    will be different for each of the feeds.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        anomali_settings (google.cloud.chronicle_v1.types.AnomaliIocSettings):
            Anomali IOC settings.

            This field is a member of `oneof`_ ``details``.
        azure_ad_context_settings (google.cloud.chronicle_v1.types.AzureADContextSettings):
            Azure AD Context settings.

            This field is a member of `oneof`_ ``details``.
        cloud_passage_settings (google.cloud.chronicle_v1.types.CloudPassageSettings):
            Cloud Passage settings.

            This field is a member of `oneof`_ ``details``.
        cortex_xdr_settings (google.cloud.chronicle_v1.types.CortexXDRSettings):
            Cortex XDR settings.

            This field is a member of `oneof`_ ``details``.
        duo_auth_settings (google.cloud.chronicle_v1.types.DuoAuthSettings):
            Duo Auth settings.

            This field is a member of `oneof`_ ``details``.
        duo_user_context_settings (google.cloud.chronicle_v1.types.DuoUserContextSettings):
            Duo User Context settings.

            This field is a member of `oneof`_ ``details``.
        microsoft_graph_alert_settings (google.cloud.chronicle_v1.types.MicrosoftGraphAlertSettings):
            Microsoft Graph Alert settings.

            This field is a member of `oneof`_ ``details``.
        microsoft_security_center_alert_settings (google.cloud.chronicle_v1.types.MicrosoftSecurityCenterAlertSettings):
            Microsoft Security center alert settings.

            This field is a member of `oneof`_ ``details``.
        mimecast_mail_settings (google.cloud.chronicle_v1.types.MimecastMailSettings):
            Mimecast mail settings.

            This field is a member of `oneof`_ ``details``.
        office365_settings (google.cloud.chronicle_v1.types.Office365Settings):
            Office 365 settings.

            This field is a member of `oneof`_ ``details``.
        proofpoint_mail_settings (google.cloud.chronicle_v1.types.ProofpointMailSettings):
            Proofpoint mail settings.

            This field is a member of `oneof`_ ``details``.
        recorded_future_ioc_settings (google.cloud.chronicle_v1.types.RecordedFutureIocSettings):
            Recorded Future IOC settings.

            This field is a member of `oneof`_ ``details``.
        workday_settings (google.cloud.chronicle_v1.types.WorkdaySettings):
            Workday settings.

            This field is a member of `oneof`_ ``details``.
        pan_ioc_settings (google.cloud.chronicle_v1.types.PanIocSettings):
            PAN IOC settings.

            This field is a member of `oneof`_ ``details``.
        okta_settings (google.cloud.chronicle_v1.types.OktaSettings):
            Okta settings.

            This field is a member of `oneof`_ ``details``.
        okta_user_context_settings (google.cloud.chronicle_v1.types.OktaUserContextSettings):
            Okta user context settings.

            This field is a member of `oneof`_ ``details``.
        fox_it_stix_settings (google.cloud.chronicle_v1.types.FoxITStixSettings):
            Fox-IT STIX settings.

            This field is a member of `oneof`_ ``details``.
        threat_connect_ioc_settings (google.cloud.chronicle_v1.types.ThreatConnectIoCSettings):
            ThreatConnect IOC settings.

            This field is a member of `oneof`_ ``details``.
        service_now_cmdb_settings (google.cloud.chronicle_v1.types.ServiceNowCMDBSettings):
            ServiceNow CMDB settings.

            This field is a member of `oneof`_ ``details``.
        imperva_waf_settings (google.cloud.chronicle_v1.types.ImpervaWAFSettings):
            Imperva WAF settings.

            This field is a member of `oneof`_ ``details``.
        thinkst_canary_settings (google.cloud.chronicle_v1.types.ThinkstCanarySettings):
            Thinkst Canary settings.

            This field is a member of `oneof`_ ``details``.
        rh_isac_ioc_settings (google.cloud.chronicle_v1.types.RHIsacIocSettings):
            RH-ISAC IOC settings.

            This field is a member of `oneof`_ ``details``.
        rapid7_insight_settings (google.cloud.chronicle_v1.types.Rapid7InsightSettings):
            Rapid7 Insight settings.

            This field is a member of `oneof`_ ``details``.
        salesforce_settings (google.cloud.chronicle_v1.types.SalesforceSettings):
            Salesforce settings.

            This field is a member of `oneof`_ ``details``.
        netskope_alert_settings (google.cloud.chronicle_v1.types.NetskopeAlertSettings):
            Netskope alert settings.

            This field is a member of `oneof`_ ``details``.
        azure_mdm_intune_settings (google.cloud.chronicle_v1.types.AzureMDMIntuneSettings):
            Azure MDM Intune settings.

            This field is a member of `oneof`_ ``details``.
        azure_ad_settings (google.cloud.chronicle_v1.types.AzureADSettings):
            Azure AD settings.

            This field is a member of `oneof`_ ``details``.
        proofpoint_on_demand_settings (google.cloud.chronicle_v1.types.ProofpointOnDemandSettings):
            Proofpoint On-Demand settings.

            This field is a member of `oneof`_ ``details``.
        workspace_users_settings (google.cloud.chronicle_v1.types.WorkspaceUsersSettings):
            Workspace users settings.

            This field is a member of `oneof`_ ``details``.
        workspace_activity_settings (google.cloud.chronicle_v1.types.WorkspaceActivitySettings):
            Workspace activity settings.

            This field is a member of `oneof`_ ``details``.
        workspace_alerts_settings (google.cloud.chronicle_v1.types.WorkspaceAlertsSettings):
            Workspace alerts settings.

            This field is a member of `oneof`_ ``details``.
        workspace_privileges_settings (google.cloud.chronicle_v1.types.WorkspacePrivilegesSettings):
            Workspace privileges settings.

            This field is a member of `oneof`_ ``details``.
        workspace_mobile_settings (google.cloud.chronicle_v1.types.WorkspaceMobileSettings):
            Workspace mobile settings.

            This field is a member of `oneof`_ ``details``.
        workspace_chrome_os_settings (google.cloud.chronicle_v1.types.WorkspaceChromeOSSettings):
            Workspace ChromeOS settings.

            This field is a member of `oneof`_ ``details``.
        workspace_groups_settings (google.cloud.chronicle_v1.types.WorkspaceGroupsSettings):
            Workspace Groups settings.

            This field is a member of `oneof`_ ``details``.
        azure_ad_audit_settings (google.cloud.chronicle_v1.types.AzureADAuditSettings):
            Azure AD Audit settings.

            This field is a member of `oneof`_ ``details``.
        symantec_event_export_settings (google.cloud.chronicle_v1.types.SymantecEventExportSettings):
            Symantec Event Export settings.

            This field is a member of `oneof`_ ``details``.
        qualys_vm_settings (google.cloud.chronicle_v1.types.QualysVMSettings):
            Qualys VM settings

            This field is a member of `oneof`_ ``details``.
        pan_prisma_cloud_settings (google.cloud.chronicle_v1.types.PanPrismaCloudSettings):
            PAN Prisma Cloud settings.

            This field is a member of `oneof`_ ``details``.
        gcs_settings (google.cloud.chronicle_v1.types.GoogleCloudStorageSettings):
            Google Cloud Storage settings.

            This field is a member of `oneof`_ ``details``.
        http_settings (google.cloud.chronicle_v1.types.HttpSettings):
            HTTP settings.

            This field is a member of `oneof`_ ``details``.
        sftp_settings (google.cloud.chronicle_v1.types.SftpSettings):
            SFTP settings.

            This field is a member of `oneof`_ ``details``.
        amazon_s3_settings (google.cloud.chronicle_v1.types.AmazonS3Settings):
            Amazon S3 settings.

            This field is a member of `oneof`_ ``details``.
        azure_blob_store_settings (google.cloud.chronicle_v1.types.AzureBlobStoreSettings):
            Azure Blob Storage settings.

            This field is a member of `oneof`_ ``details``.
        amazon_sqs_settings (google.cloud.chronicle_v1.types.AmazonSQSSettings):
            Amazon SQS settings.

            This field is a member of `oneof`_ ``details``.
        google_cloud_identity_devices_settings (google.cloud.chronicle_v1.types.GoogleCloudIdentityDevicesSettings):
            Google Cloud Identity Devices settings.

            This field is a member of `oneof`_ ``details``.
        google_cloud_identity_device_users_settings (google.cloud.chronicle_v1.types.GoogleCloudIdentityDeviceUsersSettings):
            Google Cloud Identity Device Users settings.

            This field is a member of `oneof`_ ``details``.
        crowdstrike_detects_settings (google.cloud.chronicle_v1.types.CrowdStrikeDetectsSettings):
            CrowdStrike Detects API settings.

            This field is a member of `oneof`_ ``details``.
        mandiant_ioc_settings (google.cloud.chronicle_v1.types.MandiantIoCSettings):
            Mandiant IOC settings.

            This field is a member of `oneof`_ ``details``.
        sentinelone_alert_settings (google.cloud.chronicle_v1.types.SentineloneAlertSettings):
            SentinelOne Alert settings.

            This field is a member of `oneof`_ ``details``.
        qualys_scan_settings (google.cloud.chronicle_v1.types.QualysScanSettings):
            Qualys Scan Settings

            This field is a member of `oneof`_ ``details``.
        pubsub_settings (google.cloud.chronicle_v1.types.PubsubSettings):
            Pub/Sub settings.

            This field is a member of `oneof`_ ``details``.
        amazon_kinesis_firehose_settings (google.cloud.chronicle_v1.types.AmazonKinesisFirehoseSettings):
            Amazon Kinesis Firehose settings.

            This field is a member of `oneof`_ ``details``.
        webhook_settings (google.cloud.chronicle_v1.types.WebhookSettings):
            Webhook settings.

            This field is a member of `oneof`_ ``details``.
        dummy_log_type_settings (google.cloud.chronicle_v1.types.DummyLogTypeSettings):
            DummyLogType Settings.

            This field is a member of `oneof`_ ``details``.
        https_push_google_cloud_pubsub_settings (google.cloud.chronicle_v1.types.HttpsPushGoogleCloudPubSubSettings):
            Https push Google Pub/Sub settings.

            This field is a member of `oneof`_ ``details``.
        https_push_amazon_kinesis_firehose_settings (google.cloud.chronicle_v1.types.HttpsPushAmazonKinesisFirehoseSettings):
            Https push Amazon Kinesis Firehose settings.

            This field is a member of `oneof`_ ``details``.
        https_push_webhook_settings (google.cloud.chronicle_v1.types.HttpsPushWebhookSettings):
            Https push Webhook settings.

            This field is a member of `oneof`_ ``details``.
        aws_ec2_hosts_settings (google.cloud.chronicle_v1.types.AWSEC2HostsSettings):
            AWS EC2 Hosts settings.

            This field is a member of `oneof`_ ``details``.
        aws_ec2_instances_settings (google.cloud.chronicle_v1.types.AWSEC2InstancesSettings):
            AWS EC2 Instances settings.

            This field is a member of `oneof`_ ``details``.
        aws_ec2_vpcs_settings (google.cloud.chronicle_v1.types.AWSEC2VpcsSettings):
            AWS EC2 Vpcs settings.

            This field is a member of `oneof`_ ``details``.
        aws_iam_settings (google.cloud.chronicle_v1.types.AWSIAMSettings):
            AWS IAM settings.

            This field is a member of `oneof`_ ``details``.
        netskope_alert_v2_settings (google.cloud.chronicle_v1.types.NetskopeAlertV2Settings):
            Netskope alert V2 settings.

            This field is a member of `oneof`_ ``details``.
        gcs_v2_settings (google.cloud.chronicle_v1.types.GoogleCloudStorageV2Settings):
            Settings for Google Cloud Storage Omniflow
            feeds.

            This field is a member of `oneof`_ ``details``.
        amazon_s3_v2_settings (google.cloud.chronicle_v1.types.AmazonS3V2Settings):
            Settings for S3 Omniflow feeds.

            This field is a member of `oneof`_ ``details``.
        amazon_sqs_v2_settings (google.cloud.chronicle_v1.types.AmazonSQSV2Settings):
            Settings for SQS Omniflow feeds.

            This field is a member of `oneof`_ ``details``.
        azure_event_hub_settings (google.cloud.chronicle_v1.types.AzureEventHubSettings):
            Settings for Omniflow based native ingestion
            from azure event hub.

            This field is a member of `oneof`_ ``details``.
        trellix_hx_hosts_settings (google.cloud.chronicle_v1.types.TrellixHxHostsSettings):
            Settings for Trellix HX Host Metadata.

            This field is a member of `oneof`_ ``details``.
        azure_blob_store_v2_settings (google.cloud.chronicle_v1.types.AzureBlobStoreV2Settings):
            Settings for Azure Blobstore Omniflow feeds.

            This field is a member of `oneof`_ ``details``.
        trellix_hx_alerts_settings (google.cloud.chronicle_v1.types.TrellixHxAlertsSettings):
            Settings for Trellix HX Alerts Metadata.

            This field is a member of `oneof`_ ``details``.
        google_cloud_storage_event_driven_settings (google.cloud.chronicle_v1.types.GoogleCloudStorageEventDrivenSettings):
            Settings for Omniflow based Google Cloud
            Storage event driven feeds.

            This field is a member of `oneof`_ ``details``.
        crowdstrike_alerts_settings (google.cloud.chronicle_v1.types.CrowdStrikeAlertsSettings):
            CrowdStrike Alerts API settings.

            This field is a member of `oneof`_ ``details``.
        trellix_hx_bulk_acqs_settings (google.cloud.chronicle_v1.types.TrellixHxBulkAcqsSettings):
            Settings for Trellix HX Bulk Acquisitions
            Metadata.

            This field is a member of `oneof`_ ``details``.
        mimecast_mail_v2_settings (google.cloud.chronicle_v1.types.MimecastMailV2Settings):
            Required. Mimecast mail v2 settings.

            This field is a member of `oneof`_ ``details``.
        threat_connect_ioc_v3_settings (google.cloud.chronicle_v1.types.ThreatConnectIoCV3Settings):
            Threat Connect IOC V3 settings.

            This field is a member of `oneof`_ ``details``.
        custom_api_settings (google.cloud.chronicle_v1.types.CustomAPISettings):
            Settings for Custom API (Codeless) Feeds.

            This field is a member of `oneof`_ ``details``.
        feed_source_type (google.cloud.chronicle_v1.types.FeedDetails.FeedSourceType):
            Source Type of the feed.
        log_type (str):
            LogType. Format:
            projects/{project}/locations/{location}/instances/{instance}/logTypes/{log_type}
        asset_namespace (str):
            The asset namespace to apply to all logs
            ingested through this feed.
        labels (MutableMapping[str, str]):
            The ingestion metadata labels to apply to all
            logs ingested through this feed, and the
            resulting normalized data.
        sts_migration_readiness (google.cloud.chronicle_v1.types.FeedDetails.STSMigrationReadiness):
            Optional. The status of the feed's migration
            to STS.
        last_v2_migration_attempt_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The time of the last attempt to
            migrate the feed to STS V2.
    """

    class FeedSourceType(proto.Enum):
        r"""Different types of feed sources.

        Values:
            FEED_SOURCE_TYPE_UNSPECIFIED (0):
                Unspecified feed source type.
            GOOGLE_CLOUD_STORAGE (1):
                Cloud Storage.
            HTTP (2):
                HTTP.
            SFTP (3):
                SFTP.
            AMAZON_S3 (4):
                S3.
            AZURE_BLOBSTORE (5):
                Azure Blobstore.
            API (6):
                API.
            AMAZON_SQS (7):
                SQS.
            PUBSUB (8):
                Pub/Sub.
            AMAZON_KINESIS_FIREHOSE (9):
                AMAZON_KINESIS_FIREHOSE.
            WEBHOOK (10):
                WEBHOOK.
            HTTPS_PUSH_GOOGLE_CLOUD_PUBSUB (11):
                HTTPS GCloud Pub/Sub.
            HTTPS_PUSH_AMAZON_KINESIS_FIREHOSE (12):
                HTTPS Amazon Kinesis Firehose.
            HTTPS_PUSH_WEBHOOK (13):
                HTTPS Webhook.
            AZURE_EVENT_HUB (17):
                Microsoft Azure native ingestion for event
                hub.
            GOOGLE_CLOUD_STORAGE_V2 (18):
                Google Cloud Storage Feed backed by Omniflow
                STS
            AMAZON_S3_V2 (19):
                Amazon S3 Feed backed by Omniflow STS.
            AMAZON_SQS_V2 (20):
                Amazon SQS Feed backed by Omniflow STS.
            AZURE_BLOBSTORE_V2 (21):
                Azure Blobstore Feed backed by Omniflow STS.
            GOOGLE_CLOUD_STORAGE_EVENT_DRIVEN (22):
                Google Cloud Storage Feed backed by Omniflow
                STS driven by pubsub events.
            CUSTOM_API (23):
                A customized, declarative,
                configuration-driven connector for ingesting
                JSON data from third-party REST APIs.
        """

        FEED_SOURCE_TYPE_UNSPECIFIED = 0
        GOOGLE_CLOUD_STORAGE = 1
        HTTP = 2
        SFTP = 3
        AMAZON_S3 = 4
        AZURE_BLOBSTORE = 5
        API = 6
        AMAZON_SQS = 7
        PUBSUB = 8
        AMAZON_KINESIS_FIREHOSE = 9
        WEBHOOK = 10
        HTTPS_PUSH_GOOGLE_CLOUD_PUBSUB = 11
        HTTPS_PUSH_AMAZON_KINESIS_FIREHOSE = 12
        HTTPS_PUSH_WEBHOOK = 13
        AZURE_EVENT_HUB = 17
        GOOGLE_CLOUD_STORAGE_V2 = 18
        AMAZON_S3_V2 = 19
        AMAZON_SQS_V2 = 20
        AZURE_BLOBSTORE_V2 = 21
        GOOGLE_CLOUD_STORAGE_EVENT_DRIVEN = 22
        CUSTOM_API = 23

    class STSMigrationReadiness(proto.Enum):
        r"""Whether the feed is ready for STS migration.

        Values:
            STS_MIGRATION_READINESS_UNSPECIFIED (0):
                Default value. This value is unused.
            NOT_READY (1):
                The feed needs some work for STS migration.
            READY (2):
                The feed is ready for STS migration.
            AUTH_RECONFIG_REQUIRED (3):
                Need to recreate feed with updated auth.
        """

        STS_MIGRATION_READINESS_UNSPECIFIED = 0
        NOT_READY = 1
        READY = 2
        AUTH_RECONFIG_REQUIRED = 3

    anomali_settings: "AnomaliIocSettings" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="details",
        message="AnomaliIocSettings",
    )
    azure_ad_context_settings: "AzureADContextSettings" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="details",
        message="AzureADContextSettings",
    )
    cloud_passage_settings: "CloudPassageSettings" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="details",
        message="CloudPassageSettings",
    )
    cortex_xdr_settings: "CortexXDRSettings" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="details",
        message="CortexXDRSettings",
    )
    duo_auth_settings: "DuoAuthSettings" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="details",
        message="DuoAuthSettings",
    )
    duo_user_context_settings: "DuoUserContextSettings" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="details",
        message="DuoUserContextSettings",
    )
    microsoft_graph_alert_settings: "MicrosoftGraphAlertSettings" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="details",
        message="MicrosoftGraphAlertSettings",
    )
    microsoft_security_center_alert_settings: "MicrosoftSecurityCenterAlertSettings" = (
        proto.Field(
            proto.MESSAGE,
            number=10,
            oneof="details",
            message="MicrosoftSecurityCenterAlertSettings",
        )
    )
    mimecast_mail_settings: "MimecastMailSettings" = proto.Field(
        proto.MESSAGE,
        number=11,
        oneof="details",
        message="MimecastMailSettings",
    )
    office365_settings: "Office365Settings" = proto.Field(
        proto.MESSAGE,
        number=12,
        oneof="details",
        message="Office365Settings",
    )
    proofpoint_mail_settings: "ProofpointMailSettings" = proto.Field(
        proto.MESSAGE,
        number=13,
        oneof="details",
        message="ProofpointMailSettings",
    )
    recorded_future_ioc_settings: "RecordedFutureIocSettings" = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="details",
        message="RecordedFutureIocSettings",
    )
    workday_settings: "WorkdaySettings" = proto.Field(
        proto.MESSAGE,
        number=15,
        oneof="details",
        message="WorkdaySettings",
    )
    pan_ioc_settings: "PanIocSettings" = proto.Field(
        proto.MESSAGE,
        number=16,
        oneof="details",
        message="PanIocSettings",
    )
    okta_settings: "OktaSettings" = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="details",
        message="OktaSettings",
    )
    okta_user_context_settings: "OktaUserContextSettings" = proto.Field(
        proto.MESSAGE,
        number=18,
        oneof="details",
        message="OktaUserContextSettings",
    )
    fox_it_stix_settings: "FoxITStixSettings" = proto.Field(
        proto.MESSAGE,
        number=19,
        oneof="details",
        message="FoxITStixSettings",
    )
    threat_connect_ioc_settings: "ThreatConnectIoCSettings" = proto.Field(
        proto.MESSAGE,
        number=20,
        oneof="details",
        message="ThreatConnectIoCSettings",
    )
    service_now_cmdb_settings: "ServiceNowCMDBSettings" = proto.Field(
        proto.MESSAGE,
        number=21,
        oneof="details",
        message="ServiceNowCMDBSettings",
    )
    imperva_waf_settings: "ImpervaWAFSettings" = proto.Field(
        proto.MESSAGE,
        number=22,
        oneof="details",
        message="ImpervaWAFSettings",
    )
    thinkst_canary_settings: "ThinkstCanarySettings" = proto.Field(
        proto.MESSAGE,
        number=23,
        oneof="details",
        message="ThinkstCanarySettings",
    )
    rh_isac_ioc_settings: "RHIsacIocSettings" = proto.Field(
        proto.MESSAGE,
        number=24,
        oneof="details",
        message="RHIsacIocSettings",
    )
    rapid7_insight_settings: "Rapid7InsightSettings" = proto.Field(
        proto.MESSAGE,
        number=25,
        oneof="details",
        message="Rapid7InsightSettings",
    )
    salesforce_settings: "SalesforceSettings" = proto.Field(
        proto.MESSAGE,
        number=26,
        oneof="details",
        message="SalesforceSettings",
    )
    netskope_alert_settings: "NetskopeAlertSettings" = proto.Field(
        proto.MESSAGE,
        number=27,
        oneof="details",
        message="NetskopeAlertSettings",
    )
    azure_mdm_intune_settings: "AzureMDMIntuneSettings" = proto.Field(
        proto.MESSAGE,
        number=28,
        oneof="details",
        message="AzureMDMIntuneSettings",
    )
    azure_ad_settings: "AzureADSettings" = proto.Field(
        proto.MESSAGE,
        number=29,
        oneof="details",
        message="AzureADSettings",
    )
    proofpoint_on_demand_settings: "ProofpointOnDemandSettings" = proto.Field(
        proto.MESSAGE,
        number=30,
        oneof="details",
        message="ProofpointOnDemandSettings",
    )
    workspace_users_settings: "WorkspaceUsersSettings" = proto.Field(
        proto.MESSAGE,
        number=31,
        oneof="details",
        message="WorkspaceUsersSettings",
    )
    workspace_activity_settings: "WorkspaceActivitySettings" = proto.Field(
        proto.MESSAGE,
        number=32,
        oneof="details",
        message="WorkspaceActivitySettings",
    )
    workspace_alerts_settings: "WorkspaceAlertsSettings" = proto.Field(
        proto.MESSAGE,
        number=33,
        oneof="details",
        message="WorkspaceAlertsSettings",
    )
    workspace_privileges_settings: "WorkspacePrivilegesSettings" = proto.Field(
        proto.MESSAGE,
        number=34,
        oneof="details",
        message="WorkspacePrivilegesSettings",
    )
    workspace_mobile_settings: "WorkspaceMobileSettings" = proto.Field(
        proto.MESSAGE,
        number=35,
        oneof="details",
        message="WorkspaceMobileSettings",
    )
    workspace_chrome_os_settings: "WorkspaceChromeOSSettings" = proto.Field(
        proto.MESSAGE,
        number=36,
        oneof="details",
        message="WorkspaceChromeOSSettings",
    )
    workspace_groups_settings: "WorkspaceGroupsSettings" = proto.Field(
        proto.MESSAGE,
        number=37,
        oneof="details",
        message="WorkspaceGroupsSettings",
    )
    azure_ad_audit_settings: "AzureADAuditSettings" = proto.Field(
        proto.MESSAGE,
        number=38,
        oneof="details",
        message="AzureADAuditSettings",
    )
    symantec_event_export_settings: "SymantecEventExportSettings" = proto.Field(
        proto.MESSAGE,
        number=39,
        oneof="details",
        message="SymantecEventExportSettings",
    )
    qualys_vm_settings: "QualysVMSettings" = proto.Field(
        proto.MESSAGE,
        number=40,
        oneof="details",
        message="QualysVMSettings",
    )
    pan_prisma_cloud_settings: "PanPrismaCloudSettings" = proto.Field(
        proto.MESSAGE,
        number=41,
        oneof="details",
        message="PanPrismaCloudSettings",
    )
    gcs_settings: "GoogleCloudStorageSettings" = proto.Field(
        proto.MESSAGE,
        number=42,
        oneof="details",
        message="GoogleCloudStorageSettings",
    )
    http_settings: "HttpSettings" = proto.Field(
        proto.MESSAGE,
        number=43,
        oneof="details",
        message="HttpSettings",
    )
    sftp_settings: "SftpSettings" = proto.Field(
        proto.MESSAGE,
        number=44,
        oneof="details",
        message="SftpSettings",
    )
    amazon_s3_settings: "AmazonS3Settings" = proto.Field(
        proto.MESSAGE,
        number=45,
        oneof="details",
        message="AmazonS3Settings",
    )
    azure_blob_store_settings: "AzureBlobStoreSettings" = proto.Field(
        proto.MESSAGE,
        number=46,
        oneof="details",
        message="AzureBlobStoreSettings",
    )
    amazon_sqs_settings: "AmazonSQSSettings" = proto.Field(
        proto.MESSAGE,
        number=47,
        oneof="details",
        message="AmazonSQSSettings",
    )
    google_cloud_identity_devices_settings: "GoogleCloudIdentityDevicesSettings" = (
        proto.Field(
            proto.MESSAGE,
            number=48,
            oneof="details",
            message="GoogleCloudIdentityDevicesSettings",
        )
    )
    google_cloud_identity_device_users_settings: "GoogleCloudIdentityDeviceUsersSettings" = proto.Field(
        proto.MESSAGE,
        number=49,
        oneof="details",
        message="GoogleCloudIdentityDeviceUsersSettings",
    )
    crowdstrike_detects_settings: "CrowdStrikeDetectsSettings" = proto.Field(
        proto.MESSAGE,
        number=50,
        oneof="details",
        message="CrowdStrikeDetectsSettings",
    )
    mandiant_ioc_settings: "MandiantIoCSettings" = proto.Field(
        proto.MESSAGE,
        number=53,
        oneof="details",
        message="MandiantIoCSettings",
    )
    sentinelone_alert_settings: "SentineloneAlertSettings" = proto.Field(
        proto.MESSAGE,
        number=54,
        oneof="details",
        message="SentineloneAlertSettings",
    )
    qualys_scan_settings: "QualysScanSettings" = proto.Field(
        proto.MESSAGE,
        number=55,
        oneof="details",
        message="QualysScanSettings",
    )
    pubsub_settings: "PubsubSettings" = proto.Field(
        proto.MESSAGE,
        number=56,
        oneof="details",
        message="PubsubSettings",
    )
    amazon_kinesis_firehose_settings: "AmazonKinesisFirehoseSettings" = proto.Field(
        proto.MESSAGE,
        number=57,
        oneof="details",
        message="AmazonKinesisFirehoseSettings",
    )
    webhook_settings: "WebhookSettings" = proto.Field(
        proto.MESSAGE,
        number=58,
        oneof="details",
        message="WebhookSettings",
    )
    dummy_log_type_settings: "DummyLogTypeSettings" = proto.Field(
        proto.MESSAGE,
        number=59,
        oneof="details",
        message="DummyLogTypeSettings",
    )
    https_push_google_cloud_pubsub_settings: "HttpsPushGoogleCloudPubSubSettings" = (
        proto.Field(
            proto.MESSAGE,
            number=60,
            oneof="details",
            message="HttpsPushGoogleCloudPubSubSettings",
        )
    )
    https_push_amazon_kinesis_firehose_settings: "HttpsPushAmazonKinesisFirehoseSettings" = proto.Field(
        proto.MESSAGE,
        number=61,
        oneof="details",
        message="HttpsPushAmazonKinesisFirehoseSettings",
    )
    https_push_webhook_settings: "HttpsPushWebhookSettings" = proto.Field(
        proto.MESSAGE,
        number=62,
        oneof="details",
        message="HttpsPushWebhookSettings",
    )
    aws_ec2_hosts_settings: "AWSEC2HostsSettings" = proto.Field(
        proto.MESSAGE,
        number=63,
        oneof="details",
        message="AWSEC2HostsSettings",
    )
    aws_ec2_instances_settings: "AWSEC2InstancesSettings" = proto.Field(
        proto.MESSAGE,
        number=64,
        oneof="details",
        message="AWSEC2InstancesSettings",
    )
    aws_ec2_vpcs_settings: "AWSEC2VpcsSettings" = proto.Field(
        proto.MESSAGE,
        number=65,
        oneof="details",
        message="AWSEC2VpcsSettings",
    )
    aws_iam_settings: "AWSIAMSettings" = proto.Field(
        proto.MESSAGE,
        number=66,
        oneof="details",
        message="AWSIAMSettings",
    )
    netskope_alert_v2_settings: "NetskopeAlertV2Settings" = proto.Field(
        proto.MESSAGE,
        number=70,
        oneof="details",
        message="NetskopeAlertV2Settings",
    )
    gcs_v2_settings: "GoogleCloudStorageV2Settings" = proto.Field(
        proto.MESSAGE,
        number=71,
        oneof="details",
        message="GoogleCloudStorageV2Settings",
    )
    amazon_s3_v2_settings: "AmazonS3V2Settings" = proto.Field(
        proto.MESSAGE,
        number=72,
        oneof="details",
        message="AmazonS3V2Settings",
    )
    amazon_sqs_v2_settings: "AmazonSQSV2Settings" = proto.Field(
        proto.MESSAGE,
        number=73,
        oneof="details",
        message="AmazonSQSV2Settings",
    )
    azure_event_hub_settings: "AzureEventHubSettings" = proto.Field(
        proto.MESSAGE,
        number=74,
        oneof="details",
        message="AzureEventHubSettings",
    )
    trellix_hx_hosts_settings: "TrellixHxHostsSettings" = proto.Field(
        proto.MESSAGE,
        number=75,
        oneof="details",
        message="TrellixHxHostsSettings",
    )
    azure_blob_store_v2_settings: "AzureBlobStoreV2Settings" = proto.Field(
        proto.MESSAGE,
        number=76,
        oneof="details",
        message="AzureBlobStoreV2Settings",
    )
    trellix_hx_alerts_settings: "TrellixHxAlertsSettings" = proto.Field(
        proto.MESSAGE,
        number=77,
        oneof="details",
        message="TrellixHxAlertsSettings",
    )
    google_cloud_storage_event_driven_settings: "GoogleCloudStorageEventDrivenSettings" = proto.Field(
        proto.MESSAGE,
        number=78,
        oneof="details",
        message="GoogleCloudStorageEventDrivenSettings",
    )
    crowdstrike_alerts_settings: "CrowdStrikeAlertsSettings" = proto.Field(
        proto.MESSAGE,
        number=79,
        oneof="details",
        message="CrowdStrikeAlertsSettings",
    )
    trellix_hx_bulk_acqs_settings: "TrellixHxBulkAcqsSettings" = proto.Field(
        proto.MESSAGE,
        number=80,
        oneof="details",
        message="TrellixHxBulkAcqsSettings",
    )
    mimecast_mail_v2_settings: "MimecastMailV2Settings" = proto.Field(
        proto.MESSAGE,
        number=82,
        oneof="details",
        message="MimecastMailV2Settings",
    )
    threat_connect_ioc_v3_settings: "ThreatConnectIoCV3Settings" = proto.Field(
        proto.MESSAGE,
        number=83,
        oneof="details",
        message="ThreatConnectIoCV3Settings",
    )
    custom_api_settings: "CustomAPISettings" = proto.Field(
        proto.MESSAGE,
        number=85,
        oneof="details",
        message="CustomAPISettings",
    )
    feed_source_type: FeedSourceType = proto.Field(
        proto.ENUM,
        number=1,
        enum=FeedSourceType,
    )
    log_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    asset_namespace: str = proto.Field(
        proto.STRING,
        number=51,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=52,
    )
    sts_migration_readiness: STSMigrationReadiness = proto.Field(
        proto.ENUM,
        number=81,
        enum=STSMigrationReadiness,
    )
    last_v2_migration_attempt_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=84,
        message=timestamp_pb2.Timestamp,
    )


class DummyLogTypeSettings(proto.Message):
    r"""Settings required by Feeds of DummyLogType(used for testing
    purposes).

    Attributes:
        authentication (google.cloud.chronicle_v1.types.HttpHeaderAuth):
            Input only. Authentication.
        api_endpoint (str):
            Full API Endpoint.
    """

    authentication: "HttpHeaderAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="HttpHeaderAuth",
    )
    api_endpoint: str = proto.Field(
        proto.STRING,
        number=2,
    )


class HttpsPushGoogleCloudPubSubSettings(proto.Message):
    r"""Settings required by Google Cloud Platform Pub/Sub
    Feeds(HTTPS-Push V2).

    Attributes:
        split_delimiter (str):
            Optional. Delimiter to split on for the feed.
    """

    split_delimiter: str = proto.Field(
        proto.STRING,
        number=1,
    )


class HttpsPushAmazonKinesisFirehoseSettings(proto.Message):
    r"""Settings required by Amazon Kinesis Firehose Feeds(HTTPS-Push
    V2).

    Attributes:
        split_delimiter (str):
            Optional. Delimiter to split on for the feed.
    """

    split_delimiter: str = proto.Field(
        proto.STRING,
        number=1,
    )


class HttpsPushWebhookSettings(proto.Message):
    r"""Settings required by Webhook Feeds(HTTPS-Push V2).

    Attributes:
        split_delimiter (str):
            Optional. Delimiter to split on for the feed.
    """

    split_delimiter: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SentineloneAlertSettings(proto.Message):
    r"""SentinelOne Alert settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.HttpHeaderAuth):
            Input only. Authentication.
        hostname (str):
            Hostname of SentinelOne alert settings.
        initial_start_time (str):
            initialStartTime from when to fetch the
            alerts
        is_alert_api_subscribed (bool):
            Is the customer subscribed to Alerts Api
    """

    authentication: "HttpHeaderAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="HttpHeaderAuth",
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=2,
    )
    initial_start_time: str = proto.Field(
        proto.STRING,
        number=3,
    )
    is_alert_api_subscribed: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class QualysScanSettings(proto.Message):
    r"""Qualys Scan settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.UsernameSecretAuth):
            Input only. Authentication
        hostname (str):
            Hostname.
        api_type (google.cloud.chronicle_v1.types.QualysScanSettings.ApiType):
            Supported Qualys Scan api type.
    """

    class ApiType(proto.Enum):
        r"""API Type

        Values:
            API_TYPE_UNSPECIFIED (0):
                Unspecified API Type
            SCAN_SUMMARY_OUTPUT (1):
                Scan Summaries
            SCAN_COMPLIANCE_OUTPUT (2):
                Scan Compliance
            SCAN_COMPLIANCE_CONTROL_OUTPUT (3):
                Scan Compliance Control
        """

        API_TYPE_UNSPECIFIED = 0
        SCAN_SUMMARY_OUTPUT = 1
        SCAN_COMPLIANCE_OUTPUT = 2
        SCAN_COMPLIANCE_CONTROL_OUTPUT = 3

    authentication: "UsernameSecretAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="UsernameSecretAuth",
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=2,
    )
    api_type: ApiType = proto.Field(
        proto.ENUM,
        number=3,
        enum=ApiType,
    )


class PubsubSettings(proto.Message):
    r"""Settings required by Google Cloud Pub/Sub Feeds(HTTP-Push).

    Attributes:
        google_service_account_email (str):
            Google Service Account Email.
    """

    google_service_account_email: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AmazonKinesisFirehoseSettings(proto.Message):
    r"""Settings required by Amazon Kinesis Firehose
    Feeds(HTTP-Push).

    """


class WebhookSettings(proto.Message):
    r"""Settings required by Webhook Feeds(HTTP-Push)."""


class AmazonSQSSettings(proto.Message):
    r"""Amazon SQS settings.

    Attributes:
        region (google.cloud.chronicle_v1.types.S3Region):
            S3 Region.
        queue (str):
            Name of the queue.
        account_number (str):
            Account number of the owner of the queue.
        authentication (google.cloud.chronicle_v1.types.SQSAuth):
            Input only. Authentication.
        source_deletion_option (google.cloud.chronicle_v1.types.SourceDeletionOption):
            Source deletion option.
    """

    region: "S3Region" = proto.Field(
        proto.ENUM,
        number=1,
        enum="S3Region",
    )
    queue: str = proto.Field(
        proto.STRING,
        number=2,
    )
    account_number: str = proto.Field(
        proto.STRING,
        number=3,
    )
    authentication: "SQSAuth" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="SQSAuth",
    )
    source_deletion_option: "SourceDeletionOption" = proto.Field(
        proto.ENUM,
        number=5,
        enum="SourceDeletionOption",
    )


class AnomaliIocSettings(proto.Message):
    r"""Anomali IOC settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.UsernameSecretAuth):
            Input only. Authentication.
        hostname (str):
            Optional. The hostname of the Anomali
            ThreatStream instance.
    """

    authentication: "UsernameSecretAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="UsernameSecretAuth",
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AzureADSettings(proto.Message):
    r"""Azure AD settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.MicrosoftOAuthClientCredentials):
            Input only. Authentication.
        tenant_id (str):
            Tenant ID.
        hostname (str):
            API Hostname.
        auth_endpoint (str):
            API Auth Endpoint.
    """

    authentication: "MicrosoftOAuthClientCredentials" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="MicrosoftOAuthClientCredentials",
    )
    tenant_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=3,
    )
    auth_endpoint: str = proto.Field(
        proto.STRING,
        number=4,
    )


class AzureADAuditSettings(proto.Message):
    r"""Azure AD Audit settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.MicrosoftOAuthClientCredentials):
            Input only. Authentication.
        tenant_id (str):
            Tenant ID.
        hostname (str):
            API Hostname.
        auth_endpoint (str):
            API Auth Endpoint.
    """

    authentication: "MicrosoftOAuthClientCredentials" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="MicrosoftOAuthClientCredentials",
    )
    tenant_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=3,
    )
    auth_endpoint: str = proto.Field(
        proto.STRING,
        number=4,
    )


class AzureADContextSettings(proto.Message):
    r"""Azure AD Context settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.MicrosoftOAuthClientCredentials):
            Input only. Authentication.
        retrieve_devices (bool):
            Whether to retrieve device information in
            user context.
        retrieve_groups (bool):
            Whether to retrieve group information in user
            context.
        tenant_id (str):
            Tenant ID.
        hostname (str):
            API Hostname.
        auth_endpoint (str):
            API Auth Endpoint.
    """

    authentication: "MicrosoftOAuthClientCredentials" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="MicrosoftOAuthClientCredentials",
    )
    retrieve_devices: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    retrieve_groups: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    tenant_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=5,
    )
    auth_endpoint: str = proto.Field(
        proto.STRING,
        number=6,
    )


class CloudPassageSettings(proto.Message):
    r"""CloudPassage settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.UsernameSecretAuth):
            Input only. Authentication.
        event_types (MutableSequence[str]):
            Event types filter for the events API.
    """

    authentication: "UsernameSecretAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="UsernameSecretAuth",
    )
    event_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class CortexXDRSettings(proto.Message):
    r"""PAN Cortex XDR settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.HttpHeaderAuth):
            Input only. Authentication.
        hostname (str):
            API Hostname.
        endpoint (str):
            API Endpoint.
    """

    authentication: "HttpHeaderAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="HttpHeaderAuth",
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=2,
    )
    endpoint: str = proto.Field(
        proto.STRING,
        number=3,
    )


class CrowdStrikeDetectsSettings(proto.Message):
    r"""CrowdStrike Detects settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.OAuthClientCredentials):
            Input only. OAuthClientCredentials.
        hostname (str):
            API Hostname.
        ingestion_type (google.cloud.chronicle_v1.types.CrowdStrikeDetectsSettings.IngestionType):
            Optional. Ingestion Type.
    """

    class IngestionType(proto.Enum):
        r"""Ingestion Type.

        Values:
            INGESTION_TYPE_UNSPECIFIED (0):
                For the feeds in which this field is not set
            BRING_ONLY_NEW_DETECTIONS (1):
                Ingests only new detections to be ingested.
            BRING_ALL_DETECTIONS (2):
                Ingests both new as well as old detections
                which are updated
        """

        INGESTION_TYPE_UNSPECIFIED = 0
        BRING_ONLY_NEW_DETECTIONS = 1
        BRING_ALL_DETECTIONS = 2

    authentication: "OAuthClientCredentials" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="OAuthClientCredentials",
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=2,
    )
    ingestion_type: IngestionType = proto.Field(
        proto.ENUM,
        number=3,
        enum=IngestionType,
    )


class CrowdStrikeAlertsSettings(proto.Message):
    r"""CrowdStrike Alerts settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.OAuthClientCredentials):
            Required. OAuthClientCredentials.
        hostname (str):
            Required. API Hostname.
        ingestion_type (google.cloud.chronicle_v1.types.CrowdStrikeAlertsSettings.IngestionType):
            Optional. Ingestion Type.
    """

    class IngestionType(proto.Enum):
        r"""Ingestion Type.

        Values:
            INGESTION_TYPE_UNSPECIFIED (0):
                For the feeds in which this field is not set
            BRING_ALL_ALERTS (1):
                Ingests both new as well as old alerts which
                are updated
            BRING_ONLY_NEW_ALERTS (2):
                Ingests only new alerts to be ingested.
        """

        INGESTION_TYPE_UNSPECIFIED = 0
        BRING_ALL_ALERTS = 1
        BRING_ONLY_NEW_ALERTS = 2

    authentication: "OAuthClientCredentials" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="OAuthClientCredentials",
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=2,
    )
    ingestion_type: IngestionType = proto.Field(
        proto.ENUM,
        number=3,
        enum=IngestionType,
    )


class DuoAuthSettings(proto.Message):
    r"""Duo Authentication settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.UsernameSecretAuth):
            Input only. Authentication.
        hostname (str):
            API Hostname.
    """

    authentication: "UsernameSecretAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="UsernameSecretAuth",
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DuoUserContextSettings(proto.Message):
    r"""Duo User Context settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.UsernameSecretAuth):
            Input only. Authentication.
        hostname (str):
            API hostname.
    """

    authentication: "UsernameSecretAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="UsernameSecretAuth",
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=2,
    )


class MicrosoftGraphAlertSettings(proto.Message):
    r"""Microsoft Graph Alert settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.MicrosoftOAuthClientCredentials):
            Input only. Authentication.
        tenant_id (str):
            Tenant ID.
        hostname (str):
            API Hostname.
        auth_endpoint (str):
            API Auth Endpoint.
    """

    authentication: "MicrosoftOAuthClientCredentials" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="MicrosoftOAuthClientCredentials",
    )
    tenant_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=3,
    )
    auth_endpoint: str = proto.Field(
        proto.STRING,
        number=4,
    )


class MicrosoftSecurityCenterAlertSettings(proto.Message):
    r"""Microsoft Security Center alert settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.MicrosoftOAuthClientCredentials):
            Input only. Authentication.
        subscription_id (str):
            Subscription ID of the Microsoft security
            center alert settings alert.
        tenant_id (str):
            Tenant ID.
        hostname (str):
            API Hostname.
        auth_endpoint (str):
            API Auth Endpoint.
    """

    authentication: "MicrosoftOAuthClientCredentials" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="MicrosoftOAuthClientCredentials",
    )
    subscription_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    tenant_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=4,
    )
    auth_endpoint: str = proto.Field(
        proto.STRING,
        number=5,
    )


class MimecastMailSettings(proto.Message):
    r"""Mimecast Mail settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.HttpHeaderAuth):
            Input only. Authentication.
        hostname (str):
            API Hostname.
    """

    authentication: "HttpHeaderAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="HttpHeaderAuth",
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=2,
    )


class MimecastMailV2Settings(proto.Message):
    r"""Mimecast Mail V2 Settings.

    Attributes:
        auth_credentials (google.cloud.chronicle_v1.types.MimecastV2OAuthClientCredentials):
            Required. Mimecast OAuthClientCredentials.
    """

    auth_credentials: "MimecastV2OAuthClientCredentials" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="MimecastV2OAuthClientCredentials",
    )


class Office365Settings(proto.Message):
    r"""Office 365 settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.MicrosoftOAuthClientCredentials):
            Input only. Authentication.
        tenant_id (str):
            Tenant ID.
        content_type (google.cloud.chronicle_v1.types.Office365Settings.ContentType):
            Supported office 365 content type.
        hostname (str):
            API Hostname.
        auth_endpoint (str):
            API Auth Endpoint.
    """

    class ContentType(proto.Enum):
        r"""Office 365 supported content types:

        https://docs.microsoft.com/en-us/office/office-365-management-api/office-365-management-activity-api-reference#working-with-the-office-365-management-activity-api

        Values:
            CONTENT_TYPE_UNSPECIFIED (0):
                Unspecified content type.
            AUDIT_AZURE_ACTIVE_DIRECTORY (1):
                Audit.AzureActiveDirectory.
            AUDIT_EXCHANGE (2):
                Audit.Exchange.
            AUDIT_SHARE_POINT (3):
                Audit.SharePoint.
            AUDIT_GENERAL (4):
                Audit.General.
            DLP_ALL (5):
                DLP.All.
        """

        CONTENT_TYPE_UNSPECIFIED = 0
        AUDIT_AZURE_ACTIVE_DIRECTORY = 1
        AUDIT_EXCHANGE = 2
        AUDIT_SHARE_POINT = 3
        AUDIT_GENERAL = 4
        DLP_ALL = 5

    authentication: "MicrosoftOAuthClientCredentials" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="MicrosoftOAuthClientCredentials",
    )
    tenant_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    content_type: ContentType = proto.Field(
        proto.ENUM,
        number=3,
        enum=ContentType,
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=4,
    )
    auth_endpoint: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ProofpointMailSettings(proto.Message):
    r"""Proofpoint Mail settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.UsernameSecretAuth):
            Input only. Authentication.
    """

    authentication: "UsernameSecretAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="UsernameSecretAuth",
    )


class ProofpointOnDemandSettings(proto.Message):
    r"""Proofpoint On-demand settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.HttpHeaderAuth):
            Input only. Authentication.
        cluster_id (str):
            Cluster ID.
    """

    authentication: "HttpHeaderAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="HttpHeaderAuth",
    )
    cluster_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RecordedFutureIocSettings(proto.Message):
    r"""Recorded Future IOC settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.HttpHeaderAuth):
            Input only. Authentication.
    """

    authentication: "HttpHeaderAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="HttpHeaderAuth",
    )


class WorkdaySettings(proto.Message):
    r"""Workday settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.WorkdayAuth):
            Input only. Authentication.
        hostname (str):
            API Hostname.
        tenant_id (str):
            Tenant ID.
    """

    authentication: "WorkdayAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="WorkdayAuth",
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=2,
    )
    tenant_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class PanIocSettings(proto.Message):
    r"""PAN IOC settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.HttpHeaderAuth):
            Input only. Authentication.
        feed_id (str):
            PAN IOC feed ID.
        feed (str):
            PAN IOC feed name.
    """

    authentication: "HttpHeaderAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="HttpHeaderAuth",
    )
    feed_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    feed: str = proto.Field(
        proto.STRING,
        number=3,
    )


class OktaSettings(proto.Message):
    r"""Okta settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.HttpHeaderAuth):
            Input only. Authentication.
        hostname (str):
            API Hostname.
    """

    authentication: "HttpHeaderAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="HttpHeaderAuth",
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=2,
    )


class OktaUserContextSettings(proto.Message):
    r"""Okta user context settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.HttpHeaderAuth):
            Input only. Authentication.
        hostname (str):
            API Hostname.
        manager_id_reference_field (str):
            Manager id reference field.
    """

    authentication: "HttpHeaderAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="HttpHeaderAuth",
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=2,
    )
    manager_id_reference_field: str = proto.Field(
        proto.STRING,
        number=3,
    )


class FoxITStixSettings(proto.Message):
    r"""Fox-IT STIX settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.UsernameSecretAuth):
            Input only. Authentication.
        ssl (google.cloud.chronicle_v1.types.SSLClientKeypair):
            SSL client key pair.
        poll_service_uri (str):
            TAXII poll service URI.
        collection (str):
            Collection available at the poll service.
    """

    authentication: "UsernameSecretAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="UsernameSecretAuth",
    )
    ssl: "SSLClientKeypair" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="SSLClientKeypair",
    )
    poll_service_uri: str = proto.Field(
        proto.STRING,
        number=3,
    )
    collection: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ThreatConnectIoCSettings(proto.Message):
    r"""ThreatConnect IOC Settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.UsernameSecretAuth):
            Input only. Authentication.
        hostname (str):
            API Hostname.
        owners (MutableSequence[str]):
            Owners.
    """

    authentication: "UsernameSecretAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="UsernameSecretAuth",
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=2,
    )
    owners: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class ThreatConnectIoCV3Settings(proto.Message):
    r"""ThreatConnectIoCV3Settings

    Attributes:
        authentication (google.cloud.chronicle_v1.types.UsernameSecretAuth):
            Required. Input only. UsernameSecretAuth.
        hostname (str):
            Required. hostname.
        owners (MutableSequence[str]):
            Required. Owners.
        tql_query (str):
            Optional. ThreatConnect Query Language
            filter.
        fields (MutableSequence[str]):
            Optional. Fields
        schedule (int):
            Optional. Schedule
    """

    authentication: "UsernameSecretAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="UsernameSecretAuth",
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=2,
    )
    owners: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    tql_query: str = proto.Field(
        proto.STRING,
        number=4,
    )
    fields: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    schedule: int = proto.Field(
        proto.INT32,
        number=6,
    )


class ServiceNowCMDBSettings(proto.Message):
    r"""ServiceNow CMDB settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.UsernameSecretAuth):
            Input only. Authentication.
        hostname (str):
            API Hostname.
        feedname (str):
            Feedname.
    """

    authentication: "UsernameSecretAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="UsernameSecretAuth",
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=2,
    )
    feedname: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ImpervaWAFSettings(proto.Message):
    r"""Imperva WAF settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.HttpHeaderAuth):
            Input only. Authentication.
    """

    authentication: "HttpHeaderAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="HttpHeaderAuth",
    )


class ThinkstCanarySettings(proto.Message):
    r"""Thinkst Canary settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.HttpHeaderAuth):
            Input only. Authentication.
        hostname (str):
            API Hostname.
    """

    authentication: "HttpHeaderAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="HttpHeaderAuth",
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RHIsacIocSettings(proto.Message):
    r"""RH-ISAC settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.OAuthClientCredentials):
            Input only. Authentication.
    """

    authentication: "OAuthClientCredentials" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="OAuthClientCredentials",
    )


class Rapid7InsightSettings(proto.Message):
    r"""Rapid7 Insight settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.HttpHeaderAuth):
            Input only. Authentication.
        endpoint (str):
            Rapid7 API endpoint. Should be
            "vulnerabilities" or "assets".
        hostname (str):
            API Hostname.
    """

    authentication: "HttpHeaderAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="HttpHeaderAuth",
    )
    endpoint: str = proto.Field(
        proto.STRING,
        number=2,
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SalesforceSettings(proto.Message):
    r"""Salesforce settings.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        oauth_password_grant_auth (google.cloud.chronicle_v1.types.OAuthPasswordGrantCredentials):
            Input only. OAuthPasswordGrantCredentials
            auth.

            This field is a member of `oneof`_ ``authentication``.
        oauth_jwt_credentials (google.cloud.chronicle_v1.types.OAuthJWTCredentials):
            Input only. OAuthJWTCredentials auth.

            This field is a member of `oneof`_ ``authentication``.
        hostname (str):
            API hostname.
    """

    oauth_password_grant_auth: "OAuthPasswordGrantCredentials" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="authentication",
        message="OAuthPasswordGrantCredentials",
    )
    oauth_jwt_credentials: "OAuthJWTCredentials" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="authentication",
        message="OAuthJWTCredentials",
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=3,
    )


class MandiantIoCSettings(proto.Message):
    r"""Mandiant IOC settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.HttpHeaderAuth):
            Input only. Authentication.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            time since when to start fetching the IOCs
    """

    authentication: "HttpHeaderAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="HttpHeaderAuth",
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class NetskopeAlertSettings(proto.Message):
    r"""Netskope Alert settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.HttpHeaderAuth):
            Input only. Authentication.
        hostname (str):
            API Hostname.
        feedname (str):
            Feedname.
        content_type (str):
            Content type.
    """

    authentication: "HttpHeaderAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="HttpHeaderAuth",
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=2,
    )
    feedname: str = proto.Field(
        proto.STRING,
        number=3,
    )
    content_type: str = proto.Field(
        proto.STRING,
        number=4,
    )


class NetskopeAlertV2Settings(proto.Message):
    r"""Netskope Alert V2 settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.HttpHeaderAuth):
            Input only. Authentication.
        hostname (str):
            API Hostname.
        content_category (str):
            Content Category.
        content_types (MutableSequence[str]):
            Content type.
    """

    authentication: "HttpHeaderAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="HttpHeaderAuth",
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=2,
    )
    content_category: str = proto.Field(
        proto.STRING,
        number=3,
    )
    content_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


class AzureMDMIntuneSettings(proto.Message):
    r"""Azure MDM Intune settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.MicrosoftOAuthClientCredentials):
            Input only. Authentication.
        tenant_id (str):
            Tenant ID.
        hostname (str):
            API Hostname.
        auth_endpoint (str):
            API Auth Endpoint.
    """

    authentication: "MicrosoftOAuthClientCredentials" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="MicrosoftOAuthClientCredentials",
    )
    tenant_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=3,
    )
    auth_endpoint: str = proto.Field(
        proto.STRING,
        number=4,
    )


class WorkspaceUsersSettings(proto.Message):
    r"""Workspace Users settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.OAuthJWTCredentials):
            Input only. Authentication.
        workspace_customer_id (str):
            Customer ID.
        projection_type (google.cloud.chronicle_v1.types.WorkspaceUsersSettings.ProjectionType):
            Optional. Projection Type.
    """

    class ProjectionType(proto.Enum):
        r"""Projection Type.

        Values:
            PROJECTION_TYPE_UNSPECIFIED (0):
                For the feeds in which this field is not set.
            BASIC_PROJECTION (1):
                Do not include any custom fields for the
                user.
            FULL_PROJECTION (2):
                Include both basic and custom fields
                associated with this user.
        """

        PROJECTION_TYPE_UNSPECIFIED = 0
        BASIC_PROJECTION = 1
        FULL_PROJECTION = 2

    authentication: "OAuthJWTCredentials" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="OAuthJWTCredentials",
    )
    workspace_customer_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    projection_type: ProjectionType = proto.Field(
        proto.ENUM,
        number=3,
        enum=ProjectionType,
    )


class WorkspaceActivitySettings(proto.Message):
    r"""Workspace Activity settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.OAuthJWTCredentials):
            Input only. Authentication.
        workspace_customer_id (str):
            Customer ID.
        applications (MutableSequence[str]):
            Applications.
    """

    authentication: "OAuthJWTCredentials" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="OAuthJWTCredentials",
    )
    workspace_customer_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    applications: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class WorkspaceAlertsSettings(proto.Message):
    r"""Workspace Alert settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.OAuthJWTCredentials):
            Input only. Authentication.
        workspace_customer_id (str):
            Customer ID.
    """

    authentication: "OAuthJWTCredentials" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="OAuthJWTCredentials",
    )
    workspace_customer_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class WorkspacePrivilegesSettings(proto.Message):
    r"""Workspace Privileges settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.OAuthJWTCredentials):
            Input only. Authentication.
        workspace_customer_id (str):
            Customer ID.
    """

    authentication: "OAuthJWTCredentials" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="OAuthJWTCredentials",
    )
    workspace_customer_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class WorkspaceMobileSettings(proto.Message):
    r"""Workspace Mobile settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.OAuthJWTCredentials):
            Input only. Authentication.
        workspace_customer_id (str):
            Customer ID.
    """

    authentication: "OAuthJWTCredentials" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="OAuthJWTCredentials",
    )
    workspace_customer_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class WorkspaceChromeOSSettings(proto.Message):
    r"""Workspace Chrome OS settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.OAuthJWTCredentials):
            Input only. Authentication.
        workspace_customer_id (str):
            Customer ID.
    """

    authentication: "OAuthJWTCredentials" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="OAuthJWTCredentials",
    )
    workspace_customer_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class WorkspaceGroupsSettings(proto.Message):
    r"""Workspace Groups settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.OAuthJWTCredentials):
            Input only. Authentication.
        workspace_customer_id (str):
            Customer ID.
    """

    authentication: "OAuthJWTCredentials" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="OAuthJWTCredentials",
    )
    workspace_customer_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GoogleCloudIdentityDevicesSettings(proto.Message):
    r"""Google Cloud Identity Devices settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.OAuthJWTCredentials):
            Input only. Authentication
        api_version (str):
            API Version
    """

    authentication: "OAuthJWTCredentials" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="OAuthJWTCredentials",
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GoogleCloudIdentityDeviceUsersSettings(proto.Message):
    r"""Google Cloud Identity Device Users settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.OAuthJWTCredentials):
            Input only. Authentication.
    """

    authentication: "OAuthJWTCredentials" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="OAuthJWTCredentials",
    )


class SymantecEventExportSettings(proto.Message):
    r"""Symantec Event Export settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.OAuthRefreshToken):
            Input only. Authentication.
    """

    authentication: "OAuthRefreshToken" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="OAuthRefreshToken",
    )


class QualysVMSettings(proto.Message):
    r"""Qualys VM settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.UsernameSecretAuth):
            Input only. Authentication.
        hostname (str):
            API Hostname.
    """

    authentication: "UsernameSecretAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="UsernameSecretAuth",
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=2,
    )


class PanPrismaCloudSettings(proto.Message):
    r"""PAN Prisma Cloud settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.PanPrismaAuth):
            Input only. Authentication.
        hostname (str):
            API Hostname.
    """

    authentication: "PanPrismaAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="PanPrismaAuth",
    )
    hostname: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SftpSettings(proto.Message):
    r"""SFTP settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.SftpAuth):
            Input only. Authentication.
        uri (str):
            SFTP URI.
        source_type (google.cloud.chronicle_v1.types.URISourceType):
            The URI source type.
        source_deletion_option (google.cloud.chronicle_v1.types.SourceDeletionOption):
            Source deletion option.
    """

    authentication: "SftpAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SftpAuth",
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    source_type: "URISourceType" = proto.Field(
        proto.ENUM,
        number=3,
        enum="URISourceType",
    )
    source_deletion_option: "SourceDeletionOption" = proto.Field(
        proto.ENUM,
        number=4,
        enum="SourceDeletionOption",
    )


class GoogleCloudStorageSettings(proto.Message):
    r"""Google Cloud Storage settings.

    Attributes:
        bucket_uri (str):
            Bucket URI.
        source_type (google.cloud.chronicle_v1.types.URISourceType):
            The URI source type.
        source_deletion_option (google.cloud.chronicle_v1.types.SourceDeletionOption):
            Source deletion option.
        chronicle_service_account (str):
            Output only. Service Account Chronicle will
            be using to pull data.
    """

    bucket_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source_type: "URISourceType" = proto.Field(
        proto.ENUM,
        number=2,
        enum="URISourceType",
    )
    source_deletion_option: "SourceDeletionOption" = proto.Field(
        proto.ENUM,
        number=3,
        enum="SourceDeletionOption",
    )
    chronicle_service_account: str = proto.Field(
        proto.STRING,
        number=4,
    )


class HttpSettings(proto.Message):
    r"""HTTP settings.

    Attributes:
        uri (str):
            HTTP URI.
        source_type (google.cloud.chronicle_v1.types.URISourceType):
            The URI source type.
        source_deletion_option (google.cloud.chronicle_v1.types.SourceDeletionOption):
            Source deletion option.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source_type: "URISourceType" = proto.Field(
        proto.ENUM,
        number=2,
        enum="URISourceType",
    )
    source_deletion_option: "SourceDeletionOption" = proto.Field(
        proto.ENUM,
        number=3,
        enum="SourceDeletionOption",
    )


class AmazonS3Settings(proto.Message):
    r"""Amazon S3 settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.S3Auth):
            Input only. Authentication.
        s3_uri (str):
            S3 URI.
        source_type (google.cloud.chronicle_v1.types.URISourceType):
            The URI source type.
        source_deletion_option (google.cloud.chronicle_v1.types.SourceDeletionOption):
            Source deletion option.
    """

    authentication: "S3Auth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="S3Auth",
    )
    s3_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    source_type: "URISourceType" = proto.Field(
        proto.ENUM,
        number=3,
        enum="URISourceType",
    )
    source_deletion_option: "SourceDeletionOption" = proto.Field(
        proto.ENUM,
        number=4,
        enum="SourceDeletionOption",
    )


class AzureBlobStoreSettings(proto.Message):
    r"""Azure Blob Storage settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.AzureAuth):
            Input only. Authentication.
        azure_uri (str):
            Azure URI.
        source_type (google.cloud.chronicle_v1.types.URISourceType):
            The URI source type.
        source_deletion_option (google.cloud.chronicle_v1.types.SourceDeletionOption):
            Source deletion option.
    """

    authentication: "AzureAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="AzureAuth",
    )
    azure_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    source_type: "URISourceType" = proto.Field(
        proto.ENUM,
        number=3,
        enum="URISourceType",
    )
    source_deletion_option: "SourceDeletionOption" = proto.Field(
        proto.ENUM,
        number=4,
        enum="SourceDeletionOption",
    )


class AWSEC2HostsSettings(proto.Message):
    r"""AWS EC2 Hosts Settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.UsernameSecretAuth):
            Input only. UsernameSecretAuth.
    """

    authentication: "UsernameSecretAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="UsernameSecretAuth",
    )


class AWSEC2InstancesSettings(proto.Message):
    r"""AWS EC2 Instances Settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.UsernameSecretAuth):
            Input only. UsernameSecretAuth.
    """

    authentication: "UsernameSecretAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="UsernameSecretAuth",
    )


class AWSEC2VpcsSettings(proto.Message):
    r"""AWS EC2 Vpcs Settings.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.UsernameSecretAuth):
            Input only. UsernameSecretAuth.
    """

    authentication: "UsernameSecretAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="UsernameSecretAuth",
    )


class AWSIAMSettings(proto.Message):
    r"""AWSIAMSettings contains details needed for creating an AWS
    IAM feed.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.UsernameSecretAuth):
            Input only. Authentication
        api_type (google.cloud.chronicle_v1.types.AWSIAMSettings.ApiType):
            Supported AWS IAM api type.
    """

    class ApiType(proto.Enum):
        r"""API Type

        Values:
            API_TYPE_UNSPECIFIED (0):
                API Type Unspecified
            USERS (1):
                Users.
            ROLES (2):
                Roles.
            GROUPS (3):
                Groups.
        """

        API_TYPE_UNSPECIFIED = 0
        USERS = 1
        ROLES = 2
        GROUPS = 3

    authentication: "UsernameSecretAuth" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="UsernameSecretAuth",
    )
    api_type: ApiType = proto.Field(
        proto.ENUM,
        number=3,
        enum=ApiType,
    )


class AzureAuth(proto.Message):
    r"""Azure auth.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        shared_key (str):
            Shared Key.

            This field is a member of `oneof`_ ``auth_type``.
        sas_token (str):
            SAS Token.

            This field is a member of `oneof`_ ``auth_type``.
    """

    shared_key: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="auth_type",
    )
    sas_token: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="auth_type",
    )


class SQSAuth(proto.Message):
    r"""Amazon SQS auth.

    Attributes:
        sqs_access_key_secret_auth (google.cloud.chronicle_v1.types.SQSAccessKeySecretAuth):
            SQS access key secret auth.
        additional_s3_access_key_secret_auth (google.cloud.chronicle_v1.types.AdditionalS3AccessKeySecretAuth):
            Authentication for the S3 bucket referred to
            by the items in the SQS queue. This is only
            required if it is different from the
            authentication for the queue.
    """

    sqs_access_key_secret_auth: "SQSAccessKeySecretAuth" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="SQSAccessKeySecretAuth",
    )
    additional_s3_access_key_secret_auth: "AdditionalS3AccessKeySecretAuth" = (
        proto.Field(
            proto.MESSAGE,
            number=2,
            message="AdditionalS3AccessKeySecretAuth",
        )
    )


class SQSAuthV2(proto.Message):
    r"""A message containing fields used to authenticate with Amazon
    SQS.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        sqs_v2_access_key_secret_auth (google.cloud.chronicle_v1.types.SQSV2AccessKeySecretAuth):
            Required. Auth key and secret for the SQS
            queue.

            This field is a member of `oneof`_ ``auth_type``.
        aws_iam_role_auth (google.cloud.chronicle_v1.types.SQSV2AwsIamRoleAuth):
            Required. AWS IAM Role for Identity
            Federation.

            This field is a member of `oneof`_ ``auth_type``.
    """

    sqs_v2_access_key_secret_auth: "SQSV2AccessKeySecretAuth" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="auth_type",
        message="SQSV2AccessKeySecretAuth",
    )
    aws_iam_role_auth: "SQSV2AwsIamRoleAuth" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="auth_type",
        message="SQSV2AwsIamRoleAuth",
    )


class SQSV2AwsIamRoleAuth(proto.Message):
    r"""AWS IAM Role Auth for SQS V2.

    Attributes:
        aws_iam_role_arn (str):
            AWS IAM Role for Identity Federation.
        subject_id (str):
            Subject ID to use for SQS.
    """

    aws_iam_role_arn: str = proto.Field(
        proto.STRING,
        number=1,
    )
    subject_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SQSV2AccessKeySecretAuth(proto.Message):
    r"""SQS V2 access key and secret auth.

    Attributes:
        access_key_id (str):
            Access key ID of the S3 bucket.  Ex:
            AKIABCDEFGHIJKL.
        secret_access_key (str):
            Secret access key to access the S3 bucket.
    """

    access_key_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    secret_access_key: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SQSAccessKeySecretAuth(proto.Message):
    r"""Amazon SQS access key and secret auth.

    Attributes:
        access_key_id (str):
            Access key ID.
        secret_access_key (str):
            Secret access key.
    """

    access_key_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    secret_access_key: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AdditionalS3AccessKeySecretAuth(proto.Message):
    r"""Additional S3 access key secret auth.

    Attributes:
        access_key_id (str):
            Access key ID.
        secret_access_key (str):
            Secret access key.
    """

    access_key_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    secret_access_key: str = proto.Field(
        proto.STRING,
        number=2,
    )


class S3Auth(proto.Message):
    r"""Amazon S3 auth.

    Attributes:
        access_key_id (str):
            Access key ID. Used when using access key
            auth.
        secret_access_key (str):
            Secret access key. Used when using access key
            auth.
        client_id (str):
            Client ID. Used when using OAuth auth.
        client_secret (str):
            Client secret. Used when using OAuth auth.
        refresh_uri (str):
            Refresh URI. Used when using OAuth auth.
        region (google.cloud.chronicle_v1.types.S3Region):
            S3 Region.
    """

    access_key_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    secret_access_key: str = proto.Field(
        proto.STRING,
        number=2,
    )
    client_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    client_secret: str = proto.Field(
        proto.STRING,
        number=4,
    )
    refresh_uri: str = proto.Field(
        proto.STRING,
        number=5,
    )
    region: "S3Region" = proto.Field(
        proto.ENUM,
        number=6,
        enum="S3Region",
    )


class OAuthRefreshToken(proto.Message):
    r"""OAuth 2.0 refresh token grant. See
    https://tools.ietf.org/html/rfc6749.

    Attributes:
        token_endpoint (str):
            Token endpoint to get the OAuth token from.
        client_id (str):
            Client ID.
        client_secret (str):
            Client secret.
        refresh_token (str):
            Refresh token.
    """

    token_endpoint: str = proto.Field(
        proto.STRING,
        number=1,
    )
    client_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    client_secret: str = proto.Field(
        proto.STRING,
        number=3,
    )
    refresh_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class SftpAuth(proto.Message):
    r"""SFTP Auth.

    Attributes:
        username (str):
            Username. Used for username and password
            authentication.
        password (str):
            Password. Used for username and password
            authentication.
        private_key (str):
            Private key. Used for private key
            authentication.
        private_key_passphrase (str):
            Private key passphrase. Used for private key
            authentication.
    """

    username: str = proto.Field(
        proto.STRING,
        number=1,
    )
    password: str = proto.Field(
        proto.STRING,
        number=2,
    )
    private_key: str = proto.Field(
        proto.STRING,
        number=3,
    )
    private_key_passphrase: str = proto.Field(
        proto.STRING,
        number=4,
    )


class HttpHeaderAuth(proto.Message):
    r"""HTTP header based authentication.

    Attributes:
        header_key_values (MutableSequence[google.cloud.chronicle_v1.types.HeaderKeyValue]):
            Header key-value pairs.
    """

    header_key_values: MutableSequence["HeaderKeyValue"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="HeaderKeyValue",
    )


class HeaderKeyValue(proto.Message):
    r"""Header key-value pairs.

    Attributes:
        key (str):
            Key.
        value (str):
            Value.
    """

    key: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UsernameSecretAuth(proto.Message):
    r"""Info for username and secret based authentication.

    Attributes:
        user (str):
            Username of an identity used for
            authentication.
        secret (str):
            Secret of the account identified by user_name.
    """

    user: str = proto.Field(
        proto.STRING,
        number=1,
    )
    secret: str = proto.Field(
        proto.STRING,
        number=2,
    )


class MicrosoftOAuthClientCredentials(proto.Message):
    r"""Microsoft OAuth 2.0 client credentials grant.

    Attributes:
        client_id (str):
            Client ID.
        client_secret (str):
            Client secret.
    """

    client_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    client_secret: str = proto.Field(
        proto.STRING,
        number=2,
    )


class OAuthClientCredentials(proto.Message):
    r"""OAuth 2.0 client credentials grant. See
    https://tools.ietf.org/html/rfc6749.

    Attributes:
        token_endpoint (str):
            Token endpoint.
        client_id (str):
            Client ID.
        client_secret (str):
            Client secret.
    """

    token_endpoint: str = proto.Field(
        proto.STRING,
        number=1,
    )
    client_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    client_secret: str = proto.Field(
        proto.STRING,
        number=3,
    )


class OAuthPasswordGrantCredentials(proto.Message):
    r"""OAuth 2.0 password grant. See
    https://tools.ietf.org/html/rfc6749.

    Attributes:
        token_endpoint (str):
            Token endpoint to get the OAuth token from.
        client_id (str):
            Client ID.
        client_secret (str):
            Client secret.
        user (str):
            Username.
        password (str):
            Password.
    """

    token_endpoint: str = proto.Field(
        proto.STRING,
        number=1,
    )
    client_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    client_secret: str = proto.Field(
        proto.STRING,
        number=3,
    )
    user: str = proto.Field(
        proto.STRING,
        number=4,
    )
    password: str = proto.Field(
        proto.STRING,
        number=5,
    )


class PanPrismaAuth(proto.Message):
    r"""PAN Prisma Cloud auth.

    Attributes:
        user (str):
            Username.
        password (str):
            Password.
    """

    user: str = proto.Field(
        proto.STRING,
        number=1,
    )
    password: str = proto.Field(
        proto.STRING,
        number=2,
    )


class OAuthJWTCredentials(proto.Message):
    r"""OAuth 2.0 JWT grant. See, https://tools.ietf.org/html/rfc7519

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        rs_credentials (google.cloud.chronicle_v1.types.RSCredentials):
            RS credentials.

            This field is a member of `oneof`_ ``credentials``.
        token_endpoint (str):
            Token endpoint to get the OAuth token from.
        claims (google.cloud.chronicle_v1.types.Claims):
            Claims.
    """

    rs_credentials: "RSCredentials" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="credentials",
        message="RSCredentials",
    )
    token_endpoint: str = proto.Field(
        proto.STRING,
        number=1,
    )
    claims: "Claims" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Claims",
    )


class RSCredentials(proto.Message):
    r"""RS credentials.

    Attributes:
        private_key (str):
            Private key in PEM format.
    """

    private_key: str = proto.Field(
        proto.STRING,
        number=1,
    )


class Claims(proto.Message):
    r"""Claims identifying a specific customer.

    Attributes:
        issuer (str):
            Issuer. Usually the client_id.
        subject (str):
            Subject. Usually the email.
        audience (str):
            Audience.
    """

    issuer: str = proto.Field(
        proto.STRING,
        number=1,
    )
    subject: str = proto.Field(
        proto.STRING,
        number=2,
    )
    audience: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SSLClientKeypair(proto.Message):
    r"""An SSL client certificate keypair.

    Attributes:
        encoded_private_key (str):
            The encoded private key. The string should be
            a private key in PEM format, and should include
            the begin header and end footer lines. It may
            also include newlines.

            Example:

            -----BEGIN RSA PRIVATE KEY-----
            Proc-Type: 4,ENCRYPTED
            DEK-Info: DES-EDE3-CBC,F23074E02CF47304

            <REDACTED>
            -----END RSA PRIVATE KEY-----
        ssl_certificate (str):
            The encoded SSL certificate. The string
            should be an SSL certificate in PEM format, and
            should include the begin header and end footer
            lines. It may also include newlines.

            Example:

            -----BEGIN CERTIFICATE-----
            <REDACTED>
            -----END CERTIFICATE-----
    """

    encoded_private_key: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ssl_certificate: str = proto.Field(
        proto.STRING,
        number=2,
    )


class WorkdayAuth(proto.Message):
    r"""Authentication for Workday.

    Attributes:
        user (str):
            Username. This is unused: Workday feeds were
            originally configured using a username and
            secret authentication method, but only the
            secret field was used, and it was used to supply
            the OAuth access token.
        secret (str):
            The access token used to authenticate against
            Workday. This field is called "secret" to
            maintain backwards compatibility. Workday was
            (only) configured using username (which was
            unused) and secret (which is used as the access
            token). Either this field or all of the other
            OAuth fields below must be specified.
        token_endpoint (str):
            Token endpoint to get the OAuth token from.
        client_id (str):
            Client ID.
        client_secret (str):
            Client Secret.
        refresh_token (str):
            Refresh Token.
    """

    user: str = proto.Field(
        proto.STRING,
        number=1,
    )
    secret: str = proto.Field(
        proto.STRING,
        number=2,
    )
    token_endpoint: str = proto.Field(
        proto.STRING,
        number=3,
    )
    client_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    client_secret: str = proto.Field(
        proto.STRING,
        number=5,
    )
    refresh_token: str = proto.Field(
        proto.STRING,
        number=6,
    )


class GoogleCloudStorageV2Settings(proto.Message):
    r"""GoogleCloudStorageV2Settings is the settings proto for
    Omniflow Google Cloud Storage feeds.

    Attributes:
        bucket_uri (str):
            Required. Google Cloud Storage Bucket URI for
            the feed.
        source_deletion_option (google.cloud.chronicle_v1.types.SourceDeletionOptionV2):
            Optional. Source deletion option determines
            if the data from the source is to be deleted
            after ingestion.
        chronicle_service_account (str):
            Output only. SA that will read data, this is
            Storage Transfer Service SA of Customer's
            Tenancy Project.
        max_lookback_days (int):
            Optional. Maximum File Age to ingest in days.
        include_prefixes (MutableSequence[str]):
            Optional. Optional list of object prefixes to
            include.
    """

    bucket_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source_deletion_option: "SourceDeletionOptionV2" = proto.Field(
        proto.ENUM,
        number=2,
        enum="SourceDeletionOptionV2",
    )
    chronicle_service_account: str = proto.Field(
        proto.STRING,
        number=3,
    )
    max_lookback_days: int = proto.Field(
        proto.INT32,
        number=4,
    )
    include_prefixes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )


class GoogleCloudStorageEventDrivenSettings(proto.Message):
    r"""GoogleCloudStorageEventDrivenSettings is the settings proto
    for Omniflow Google Cloud Storage feeds driven by pubsub events.

    Attributes:
        bucket_uri (str):
            Required. Google Cloud Storage Bucket URI for
            the feed.
        pubsub_subscription (str):
            Required. Subscription name for pubsub topic.
        source_deletion_option (google.cloud.chronicle_v1.types.SourceDeletionOptionV2):
            Optional. Source deletion option determines
            if the data from the source is to be deleted
            after ingestion.
        chronicle_service_account (str):
            Output only. SA that will read data, this is
            Storage Transfer Service SA of Customer's
            Tenancy Project.
        max_lookback_days (int):
            Optional. Maximum File Age to ingest in days.
        include_prefixes (MutableSequence[str]):
            Optional. Optional list of object prefixes to
            include.
    """

    bucket_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    pubsub_subscription: str = proto.Field(
        proto.STRING,
        number=2,
    )
    source_deletion_option: "SourceDeletionOptionV2" = proto.Field(
        proto.ENUM,
        number=3,
        enum="SourceDeletionOptionV2",
    )
    chronicle_service_account: str = proto.Field(
        proto.STRING,
        number=4,
    )
    max_lookback_days: int = proto.Field(
        proto.INT32,
        number=5,
    )
    include_prefixes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )


class S3AuthV2(proto.Message):
    r"""A message containing fields used to authenticate with Amazon
    S3.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        access_key_secret_auth (google.cloud.chronicle_v1.types.S3V2AccessKeySecretAuth):
            Access Key ID and Secret Access Key for an
            AWS account.

            This field is a member of `oneof`_ ``auth_type``.
        aws_iam_role_auth (google.cloud.chronicle_v1.types.S3V2AwsIamRoleAuth):
            AWS IAM Role Auth for Identity Federation.

            This field is a member of `oneof`_ ``auth_type``.
    """

    access_key_secret_auth: "S3V2AccessKeySecretAuth" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="auth_type",
        message="S3V2AccessKeySecretAuth",
    )
    aws_iam_role_auth: "S3V2AwsIamRoleAuth" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="auth_type",
        message="S3V2AwsIamRoleAuth",
    )


class S3V2AwsIamRoleAuth(proto.Message):
    r"""AWS IAM Role Auth for S3 V2.

    Attributes:
        aws_iam_role_arn (str):
            AWS IAM Role for Identity Federation.
        subject_id (str):
            Subject ID to use for S3.
    """

    aws_iam_role_arn: str = proto.Field(
        proto.STRING,
        number=1,
    )
    subject_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class S3V2AccessKeySecretAuth(proto.Message):
    r"""S3 V2 access key and secret auth.

    Attributes:
        access_key_id (str):
            Required. Access Key ID for an AWS account (a
            20-character, alphanumeric string).
        secret_access_key (str):
            Required. Secret Access Key for an AWS
            account (a 40-character string).
    """

    access_key_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    secret_access_key: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AmazonS3V2Settings(proto.Message):
    r"""AmazonS3V2Settings is the settings proto for Omniflow S3
    feeds.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.S3AuthV2):
            Required. Authentication.
        s3_uri (str):
            Required. S3 URI.
        source_deletion_option (google.cloud.chronicle_v1.types.SourceDeletionOptionV2):
            Optional. Source deletion option.
        max_lookback_days (int):
            Optional. Maximum File Age to ingest in days.
        chronicle_service_account (str):
            Output only. SA that will read data, this is
            Storage Transfer Service SA of Customer's
            Tenancy Project.
        include_prefixes (MutableSequence[str]):
            Optional. Optional list of object prefixes to
            include.
    """

    authentication: "S3AuthV2" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="S3AuthV2",
    )
    s3_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    source_deletion_option: "SourceDeletionOptionV2" = proto.Field(
        proto.ENUM,
        number=3,
        enum="SourceDeletionOptionV2",
    )
    max_lookback_days: int = proto.Field(
        proto.INT32,
        number=4,
    )
    chronicle_service_account: str = proto.Field(
        proto.STRING,
        number=5,
    )
    include_prefixes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )


class MssoAuthentication(proto.Message):
    r"""Info for MssoAuthentication using a username, password, and
    login api endpoint.

    Attributes:
        username (str):
            Required. Username for MSSO authentication.
            There are no restrictions on the format of the
            username. It has no default, specifically
            enforced min / max length or character set. The
            username will have been provided by an MSSO
            administrator and it is assumed that they have
            provided a username that is internally
            consistent with MSSO authentication requirements
            / validation.
        password (str):
            Required. Password of the account identified
            by username. There are no restrictions on the
            format of the password. It has no default,
            specifically enforced min / max length or
            character set. The password will have been
            provided by an MSSO administrator and it is
            assumed that they have provided a password that
            is internally consistent with MSSO
            authentication requirements / validation.
        api_endpoint (str):
            Required. The login api endpoint url.
            This must be a valid URL with an http or https
            scheme. It has no default.
    """

    username: str = proto.Field(
        proto.STRING,
        number=1,
    )
    password: str = proto.Field(
        proto.STRING,
        number=2,
    )
    api_endpoint: str = proto.Field(
        proto.STRING,
        number=3,
    )


class MimecastV2OAuthClientCredentials(proto.Message):
    r"""OAuth 2.0 client credentials grant. See
    https://tools.ietf.org/html/rfc6749.

    Attributes:
        client_id (str):
            Required. Client ID.
        client_secret (str):
            Required. Client Secret.
    """

    client_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    client_secret: str = proto.Field(
        proto.STRING,
        number=2,
    )


class TrellixIAMAuthentication(proto.Message):
    r"""Settings for TrellixIAMAuthentication.

    Attributes:
        client_id (str):
            Required. Client ID generated in Trellix IAM.
            This is a unique identifier for the user that is
            generated in Trellix IAM. It has no default,
            specifically enforced min / max length or
            character set. It is assumed that the Client ID
            generated in Trellix IAM is internally
            consistent with Trellix IAM authentication
            requirements / validation.
        client_secret (str):
            Required. Secret associated with the Client
            ID. This is the secret generated in Trellix IAM
            for the Client ID. It has no default,
            specifically enforced min / max length or
            character set. It is assumed that the secret
            generated in Trellix IAM is internally
            consistent with Trellix IAM authentication
            requirements / validation.
        scope (str):
            Required. OAUTH 2 scope to request for the
            authentication token. This is the OAUTH 2 scope
            to request for the authentication token. It has
            no default, specifically enforced min / max
            length or character set. It is assumed that the
            scope provided is internally consistent with
            Trellix IAM authentication requirements /
            validation.
    """

    client_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    client_secret: str = proto.Field(
        proto.STRING,
        number=2,
    )
    scope: str = proto.Field(
        proto.STRING,
        number=3,
    )


class TrellixLocalAuthentication(proto.Message):
    r"""Info for TrellixLocalAuthentication using a username,
    password, endpoint, and header name.

    Attributes:
        username (str):
            Required. Username for Trellix Local
            authentication. This is a unique username for
            the user that is generated on a Trellix device.
            It has no default, specifically enforced min /
            max length, or character set.
        password (str):
            Required. Password of the account identified
            by username. There are no restrictions on the
            format of the password. It has no default,
            specifically enforced min / max length or
            character set. The password will have been
            provided by the Trellix administrator.
        token_endpoint (str):
            Required. The endpoint to fetch the token
            from. This must be a valid URL with an http or
            https scheme. It has no default.
        token_header (str):
            Required. The HTTP header name to use for the
            token for authentcated requests. It varies per
            Trellix product. Refer to the Trellix API
            documentation for the correct value. It has no
            default.
    """

    username: str = proto.Field(
        proto.STRING,
        number=1,
    )
    password: str = proto.Field(
        proto.STRING,
        number=2,
    )
    token_endpoint: str = proto.Field(
        proto.STRING,
        number=3,
    )
    token_header: str = proto.Field(
        proto.STRING,
        number=4,
    )


class TrellixStarXAuthentication(proto.Message):
    r"""TrellixStarXAuthentication contains a oneof with all of the
    authentication types supported by Trellix \*X devices.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        msso (google.cloud.chronicle_v1.types.MssoAuthentication):
            Input only. MssoAuthentication auth type.

            This field is a member of `oneof`_ ``auth_type``.
        trellix_iam (google.cloud.chronicle_v1.types.TrellixIAMAuthentication):
            Input only. TrellixIAMAuthentication auth
            type.

            This field is a member of `oneof`_ ``auth_type``.
        trellix_local (google.cloud.chronicle_v1.types.TrellixLocalAuthentication):
            Input only. TrellixLocalAuthentication auth
            type.

            This field is a member of `oneof`_ ``auth_type``.
    """

    msso: "MssoAuthentication" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="auth_type",
        message="MssoAuthentication",
    )
    trellix_iam: "TrellixIAMAuthentication" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="auth_type",
        message="TrellixIAMAuthentication",
    )
    trellix_local: "TrellixLocalAuthentication" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="auth_type",
        message="TrellixLocalAuthentication",
    )


class TrellixHxHostsSettings(proto.Message):
    r"""Settings required by Feeds of TrellixHxHosts.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.TrellixStarXAuthentication):
            Required. Authentication.
        endpoint (str):
            Required. Trellix HX Device URL.
            This must be a valid URL with an http or https
            scheme. It has no default. Usually a device URL
            is in the form of either:

            https://xxx.trellix.com/hx/id/<hx id>/
             - or -
            https://htapdeviceproxy.md.mandiant.net/dphb/hx/<device
            uuid>/
    """

    authentication: "TrellixStarXAuthentication" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="TrellixStarXAuthentication",
    )
    endpoint: str = proto.Field(
        proto.STRING,
        number=2,
    )


class TrellixHxAlertsSettings(proto.Message):
    r"""Settings required by Feeds of TrellixHxAlerts.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.TrellixStarXAuthentication):
            Required. Authentication.
        endpoint (str):
            Required. Trellix HX Device URL.
            This must be a valid URL with an http or https
            scheme. It has no default. Usually a device URL
            is in the form of either:

            https://xxx.trellix.com/hx/id/<hx id>/
             - or -
            https://htapdeviceproxy.md.mandiant.net/dphb/hx/<device
            uuid>/
    """

    authentication: "TrellixStarXAuthentication" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="TrellixStarXAuthentication",
    )
    endpoint: str = proto.Field(
        proto.STRING,
        number=2,
    )


class TrellixHxBulkAcqsSettings(proto.Message):
    r"""Settings required by Feeds of TrellixHxBulkAcqs.

    Attributes:
        authentication (google.cloud.chronicle_v1.types.TrellixStarXAuthentication):
            Required. Authentication.
        endpoint (str):
            Required. Trellix HX Device URL.
            This must be a valid URL with an http or https
            scheme. It has no default. Usually a device URL
            is in the form of either:

            https://xxx.trellix.com/hx/id/<hx id>/
             - or -
            https://htapdeviceproxy.md.mandiant.net/dphb/hx/<device
            uuid>/
    """

    authentication: "TrellixStarXAuthentication" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="TrellixStarXAuthentication",
    )
    endpoint: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AzureEventHubSettings(proto.Message):
    r"""Settings required by Azure Event Hub Feeds.

    Attributes:
        name (str):
            Required. Event hub to read from.
        consumer_group (str):
            Required. Event hub consumer group to read
            from.
        event_hub_connection_string (str):
            Required. Event hub connection string for
            authentication.
        azure_storage_connection_string (str):
            Optional. Blob store connection string for
            authentication.
        azure_storage_container (str):
            Optional. Blob storage container name.
        azure_sas_token (str):
            Optional. SAS token
        event_hub_namespace (str):
            Output only. Event hub namespace
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    consumer_group: str = proto.Field(
        proto.STRING,
        number=2,
    )
    event_hub_connection_string: str = proto.Field(
        proto.STRING,
        number=3,
    )
    azure_storage_connection_string: str = proto.Field(
        proto.STRING,
        number=4,
    )
    azure_storage_container: str = proto.Field(
        proto.STRING,
        number=5,
    )
    azure_sas_token: str = proto.Field(
        proto.STRING,
        number=6,
    )
    event_hub_namespace: str = proto.Field(
        proto.STRING,
        number=7,
    )


class AmazonSQSV2Settings(proto.Message):
    r"""AmazonSQSV2Settings is the settings proto for Omniflow SQS
    feeds.

    Attributes:
        queue (str):
            Required. Amazon Resource Name(ARN) of the
            queue.
        s3_uri (str):
            Required. S3 URI.
        authentication (google.cloud.chronicle_v1.types.SQSAuthV2):
            Required. Authentication.
        source_deletion_option (google.cloud.chronicle_v1.types.SourceDeletionOptionV2):
            Optional. Source deletion option.
        max_lookback_days (int):
            Optional. Maximum File Age to ingest in days.
        chronicle_service_account (str):
            Output only. SA that will read data, this is
            Storage Transfer Service SA of Customer's
            Tenancy Project.
        include_prefixes (MutableSequence[str]):
            Optional. Optional list of object prefixes to
            include.
    """

    queue: str = proto.Field(
        proto.STRING,
        number=1,
    )
    s3_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    authentication: "SQSAuthV2" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="SQSAuthV2",
    )
    source_deletion_option: "SourceDeletionOptionV2" = proto.Field(
        proto.ENUM,
        number=4,
        enum="SourceDeletionOptionV2",
    )
    max_lookback_days: int = proto.Field(
        proto.INT32,
        number=5,
    )
    chronicle_service_account: str = proto.Field(
        proto.STRING,
        number=6,
    )
    include_prefixes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )


class AzureBlobStoreV2Settings(proto.Message):
    r"""AzureBlobStoreV2Settings is the settings proto for Azure Blob
    Storage feeds.

    Attributes:
        azure_uri (str):
            Required. Azure URI.
        authentication (google.cloud.chronicle_v1.types.AzureAuthV2):
            Required. Authentication.
        source_deletion_option (google.cloud.chronicle_v1.types.SourceDeletionOptionV2):
            Optional. Source deletion option.
        max_lookback_days (int):
            Optional. Maximum File Age to ingest in days.
        chronicle_service_account (str):
            Output only. SA that will read data, this is
            Storage Transfer Service SA of Customer's
            Tenancy Project.
        include_prefixes (MutableSequence[str]):
            Optional. Optional list of object prefixes to
            include.
    """

    azure_uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    authentication: "AzureAuthV2" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AzureAuthV2",
    )
    source_deletion_option: "SourceDeletionOptionV2" = proto.Field(
        proto.ENUM,
        number=4,
        enum="SourceDeletionOptionV2",
    )
    max_lookback_days: int = proto.Field(
        proto.INT32,
        number=5,
    )
    chronicle_service_account: str = proto.Field(
        proto.STRING,
        number=6,
    )
    include_prefixes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )


class AzureV2WorkloadIdentityFederation(proto.Message):
    r"""Azure V2 Workload Identity Federation.

    Attributes:
        client_id (str):
            Required. OAuth client ID.
        tenant_id (str):
            Required. Tenant ID.
        subject_id (str):
            Required. Subject ID of the Azure
            subscription.
    """

    client_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    tenant_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    subject_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class AzureAuthV2(proto.Message):
    r"""A message containing fields used to authenticate with Azure
    Blob Storage.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        access_key (str):
            Required. Access Key also known as shared
            key.

            This field is a member of `oneof`_ ``auth_type``.
        sas_token (str):
            Required. SAS Token.

            This field is a member of `oneof`_ ``auth_type``.
        azure_v2_workload_identity_federation (google.cloud.chronicle_v1.types.AzureV2WorkloadIdentityFederation):
            Required. Azure V2 Workload Identity
            Federation.

            This field is a member of `oneof`_ ``auth_type``.
    """

    access_key: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="auth_type",
    )
    sas_token: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="auth_type",
    )
    azure_v2_workload_identity_federation: "AzureV2WorkloadIdentityFederation" = (
        proto.Field(
            proto.MESSAGE,
            number=3,
            oneof="auth_type",
            message="AzureV2WorkloadIdentityFederation",
        )
    )


class FeedSourceTypeSchema(proto.Message):
    r"""Metadata that pertains to feed source types (see
    Feed.FeedDetails.FeedSourceType) that is useful for building
    interfaces to construct valid Feed messages.

    Attributes:
        name (str):
            The resource name for this FeedSourceTypeSchema. Format:
            "projects/{project}/locations/{location}/instances/{instance}/feedSourceTypeSchemas/{feed_source_type}".
        display_name (str):
            A human-readable name for this feed source
            type.
        description (str):
            A human-readable description for this feed
            source type.
        read_only (bool):
            Whether feeds having this source type, while
            they are expected to exist, should not be
            modified (created, edited, or deleted).
        feed_source_type (google.cloud.chronicle_v1.types.FeedDetails.FeedSourceType):
            The value to be used in the ``details.feed_source_type``
            field in the Feed message.
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
    read_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    feed_source_type: "FeedDetails.FeedSourceType" = proto.Field(
        proto.ENUM,
        number=5,
        enum="FeedDetails.FeedSourceType",
    )


class LogTypeSchema(proto.Message):
    r"""Metadata that pertains to a log type in the context of Feeds,
    and is useful for building interfaces to construct valid Feed
    messages.

    Attributes:
        name (str):
            The resource name. Format:
            "projects/{project}/locations/{location}/instances/{instance}/feedSourceTypeSchemas/{feed_source_type}/logTypeSchemas/{log_type}".
        display_name (str):
            A human-readable name for this log type.
        log_type (str):
            The log type to be used in the ``details.log_type`` field.
        read_only (bool):
            Whether this log type schema represents a
            feed configuration that may exist, but should
            not be modified (created, edited, or deleted).
        supporting_documentation (str):
            A description that is displayed when users
            create or edit feeds.
        details_field_schemas (MutableSequence[google.cloud.chronicle_v1.types.LogTypeSchema.DetailsFieldSchema]):
            The schemas for ``detail`` fields that are compatible with
            this log type and feed source type. All fields for this log
            type and feed source type are either contained here or
            within details_field_schema_alternatives.
        details_field_schema_alternatives (MutableSequence[google.cloud.chronicle_v1.types.LogTypeSchema.DetailsFieldSchemaAlternative]):
            There are sets of fields which represent
            alternatives to one another. A user would only
            fill in one set of fields for any one
            alternative.
    """

    class DetailsFieldSchemaAlternative(proto.Message):
        r"""A collection of ``details`` field schema sets. The user must provide
        values for only one set of fields within an alternative.

        Attributes:
            details_field_schema_sets (MutableSequence[google.cloud.chronicle_v1.types.LogTypeSchema.DetailsFieldSchemaSet]):
                The schemas for each alternative set of
                fields.
        """

        details_field_schema_sets: MutableSequence[
            "LogTypeSchema.DetailsFieldSchemaSet"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="LogTypeSchema.DetailsFieldSchemaSet",
        )

    class DetailsFieldSchemaSet(proto.Message):
        r"""A collection of schemas for related fields within ``details``.

        Attributes:
            display_name (str):
                A human-readable name for this collection of ``details``
                fields.
            description (str):
                A human-readable description for this collection of
                ``details`` fields.
            details_field_schemas (MutableSequence[google.cloud.chronicle_v1.types.LogTypeSchema.DetailsFieldSchema]):
                Schemas for the fields in this set.
        """

        display_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        description: str = proto.Field(
            proto.STRING,
            number=2,
        )
        details_field_schemas: MutableSequence["LogTypeSchema.DetailsFieldSchema"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=3,
                message="LogTypeSchema.DetailsFieldSchema",
            )
        )

    class DetailsFieldSchema(proto.Message):
        r"""A schema for a particular ``details`` field on the Feed proto
        message.

        Attributes:
            field_path (str):
                The protocol buffer field path. For example,
                "details.azure_ad_context_settings.authentication.token_endpoint".
            display_name (str):
                A human-readable name for this field.
            description (str):
                A human-readable description for this field.
            type_ (google.cloud.chronicle_v1.types.SemanticType):
                A type that represents both the encoding and
                the semantics of this field.
            enum_field_schemas (MutableSequence[google.cloud.chronicle_v1.types.LogTypeSchema.EnumFieldSchema]):
                If a field has an enum type, this is the
                schema describing the possible values.
            required (bool):
                Whether this field must be specified to have
                a valid feed configuration.
            example_input (str):
                For those fields with input requirements that
                aren't adequately expressed by the SemanticType
                it is often useful to supply an example input.
            read_only (bool):
                For those fields which are read only.
        """

        field_path: str = proto.Field(
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
        type_: "SemanticType" = proto.Field(
            proto.ENUM,
            number=4,
            enum="SemanticType",
        )
        enum_field_schemas: MutableSequence["LogTypeSchema.EnumFieldSchema"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=5,
                message="LogTypeSchema.EnumFieldSchema",
            )
        )
        required: bool = proto.Field(
            proto.BOOL,
            number=6,
        )
        example_input: str = proto.Field(
            proto.STRING,
            number=7,
        )
        read_only: bool = proto.Field(
            proto.BOOL,
            number=8,
        )

    class EnumFieldSchema(proto.Message):
        r"""A schema for a particular value, for a particular enum ``details``
        field on the Feed proto message.

        Attributes:
            value (str):
                The value to assign to the field.
            display_name (str):
                A human-readable name for this value.
            description (str):
                A human-readable description for this value.
        """

        value: str = proto.Field(
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

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    log_type: str = proto.Field(
        proto.STRING,
        number=3,
    )
    read_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    supporting_documentation: str = proto.Field(
        proto.STRING,
        number=5,
    )
    details_field_schemas: MutableSequence[DetailsFieldSchema] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=DetailsFieldSchema,
    )
    details_field_schema_alternatives: MutableSequence[
        DetailsFieldSchemaAlternative
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=DetailsFieldSchemaAlternative,
    )


class FetchServiceAccountForCustomerRequest(proto.Message):
    r"""Request message for FetchServiceAccountForCustomer.

    Attributes:
        parent (str):
            Required. The parent resource where this
            FeedServiceAccount will be created. Format:

            projects/{project}/locations/{location}/instances/{instance}
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListFeedSourceTypeSchemasRequest(proto.Message):
    r"""ListFeedSourceTypeSchemas request message. Note that Feed
    schemas do not contain customer data, so are not scoped to a
    particular customer.

    Attributes:
        parent (str):
            Required. The parent, which owns this
            collection of FeedSourceTypeSchemas. Format:
            projects/{project}/locations/{location}/instances/{instance}
        page_size (int):
            The maximum number of FeedSourceTypeSchemas
            to return. The service may return fewer than
            this value. If unspecified all
            FeedSourceTypeSchemas will be returned, meaning
            one FeedSourceTypeSchema for each
            FeedDetails.FeedSourceType.
            The maximum value is 100; values above 100 will
            be coerced to 100.
        page_token (str):
            A page token, received from a previous
            ``ListFeedSourceTypeSchemas`` call. Provide this to retrieve
            the subsequent page.
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


class ListFeedSourceTypeSchemasResponse(proto.Message):
    r"""ListFeedSourceTypeSchemas response message.

    Attributes:
        feed_source_type_schemas (MutableSequence[google.cloud.chronicle_v1.types.FeedSourceTypeSchema]):
            Schemas describing each FeedSourceType.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    feed_source_type_schemas: MutableSequence["FeedSourceTypeSchema"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="FeedSourceTypeSchema",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListLogTypeSchemasRequest(proto.Message):
    r"""ListLogTypeSchemas request message. Note that feed schemas do
    not contain customer data, so are not scoped to a particular
    customer.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            LogTypeSchemas. Format: Format:
            projects/{project}/locations/{location}/instances/{instance}/feedSourceTypeSchemas/{feed_source_type}
        page_size (int):
            The maximum number of LogTypeSchemas to
            return. The service may return fewer than this
            value. If unspecified, at most 5000
            LogTypeSchemas will be returned. The maximum
            value is 10000; values above 10000 will be
            coerced to 10000.
        page_token (str):
            A page token, received from a previous
            ``ListLogTypeSchemas`` call. Provide this to retrieve the
            subsequent page.
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


class ListLogTypeSchemasResponse(proto.Message):
    r"""ListLogTypeSchemas response message.

    Attributes:
        log_type_schemas (MutableSequence[google.cloud.chronicle_v1.types.LogTypeSchema]):
            LogTypeSchemas.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    log_type_schemas: MutableSequence["LogTypeSchema"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="LogTypeSchema",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ImportPushLogsRequest(proto.Message):
    r"""ImportPushLogsRequest request message.

    Attributes:
        parent (str):
            Required. The parent, which owns this
            collection of logs. Format:

            projects/{project}/locations/{location}/instances/{instance}/feeds/{feed}
        http_body (google.api.httpbody_pb2.HttpBody):
            Required. The raw HTTP body is bound to this
            field. All log entries must be valid UTF-8. A
            single invalid event will cause the entire
            request to be rejected.
        secret (str):
            Immutable. The secret for the feed.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    http_body: httpbody_pb2.HttpBody = proto.Field(
        proto.MESSAGE,
        number=2,
        message=httpbody_pb2.HttpBody,
    )
    secret: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateFeedRequest(proto.Message):
    r"""Request message for UpdateFeed.

    Attributes:
        feed (google.cloud.chronicle_v1.types.Feed):
            Required. Feed to update. Updates full feed
            object.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Specifies which fields to update. If empty, update
            the full feed. To update the display name, pass only
            ``displayName`` and no other fields. To update other fields,
            pass a comma-separated list of fields to update and omit
            ``displayName``. The update fails if an existing
            ``displayName`` is sent in the update request.
    """

    feed: "Feed" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Feed",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class ListFeedsRequest(proto.Message):
    r"""Request message for ListFeed.

    Attributes:
        parent (str):
            Required. The parent resource where this Feed
            will be created. Format:
            projects/{project}/locations/{location}/instances/{instance}
        page_size (int):
            The maximum number of feeds to return. The
            service may return fewer than this value.
            If unspecified, at most 100 feeds will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            A page token, received from a previous ``ListFeeds`` call.
            Provide this to retrieve the subsequent page.
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


class ListFeedsResponse(proto.Message):
    r"""Response message for ListFeed.

    Attributes:
        feeds (MutableSequence[google.cloud.chronicle_v1.types.Feed]):
            List of feeds.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    feeds: MutableSequence["Feed"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Feed",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListFeedPacksRequest(proto.Message):
    r"""Request message for ListFeedPacks.

    Attributes:
        parent (str):
            Required. The parent resource where this
            content pack will be created. Format:
            projects/{project}/locations/{location}/instances/{instance}
        page_size (int):
            Optional. The maximum number of feed content
            packs to return. The service may return fewer
            than this value. If unspecified, at most 50 feed
            content packs will be returned. The maximum
            value is 1000; values above 1000 will be coerced
            to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListFeedPacks`` call. Provide this to retrieve the
            subsequent page. When paginating, all other parameters
            provided to ``ListFeedPacks`` must match the call that
            provided the page token.
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


class ListFeedPacksResponse(proto.Message):
    r"""Response message for ListFeedPacks.

    Attributes:
        feed_packs (MutableSequence[google.cloud.chronicle_v1.types.FeedPack]):
            List of feeds packs.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    feed_packs: MutableSequence["FeedPack"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="FeedPack",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetFeedPackRequest(proto.Message):
    r"""Request message for GetFeedPack.

    Attributes:
        name (str):
            Required. The ID of the feed pack to
            retrieve. Format:

            projects/{project}/locations/{location}/instances/{instance}/feedPacks/{feedPack}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateFeedRequest(proto.Message):
    r"""Request message for CreateFeed.

    Attributes:
        parent (str):
            Required. The parent resource where this Feed
            will be created. Format:
            projects/{project}/locations/{location}/instances/{instance}
        feed (google.cloud.chronicle_v1.types.Feed):
            Required. Feed to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    feed: "Feed" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Feed",
    )


class GetFeedRequest(proto.Message):
    r"""Request message to retrieve a feed.

    Attributes:
        name (str):
            Required. The ID of the feed to retrieve.
            Format:

            projects/{project}/locations/{location}/instances/{instance}/feeds/{feed}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteFeedRequest(proto.Message):
    r"""Request message to delete a feed.

    Attributes:
        name (str):
            Required. The ID of the feed to retrieve.
            Format:

            projects/{project}/locations/{location}/instances/{instance}/feeds/{feed}
        delete_backlog (bool):
            Optional. If true, delete the uningested
            backlog in OOB retry queue for the feed.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    delete_backlog: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class EnableFeedRequest(proto.Message):
    r"""EnableFeed request message.

    Attributes:
        name (str):
            Required. The name of the feed to enable.
            Format:

            projects/{project}/locations/{location}/instances/{instance}/feeds/{feed}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GenerateSecretRequest(proto.Message):
    r"""GenerateSecret request message.

    Attributes:
        name (str):
            Required. The name of the feed to for which
            to generate secret. Format:

            projects/{project}/locations/{location}/instances/{instance}/feeds/{feed}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GenerateSecretResponse(proto.Message):
    r"""GenerateSecret response message.

    Attributes:
        secret (str):
            The generated secret. Store the secret value
            at a safe place and use it while configuring
            your https push feed.
    """

    secret: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DisableFeedRequest(proto.Message):
    r"""DisableFeed request message.

    Attributes:
        name (str):
            Required. The name of the feed to disable.
            Format:

            projects/{project}/locations/{location}/instances/{instance}/feeds/{feed}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CustomAPIHeaderKeyValue(proto.Message):
    r"""CustomAPIHeaderKeyValue defines dynamic headers key-values
    for Custom API.

    Attributes:
        key (str):
            Required. Enter the name of the HTTP Request
            header (e.g., Authorization or X-API-Key).
        value (str):
            Required. Enter the API Key, Bearer Token, or
            credential value associated with the header.
    """

    key: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CustomAPIHeaderAuth(proto.Message):
    r"""CustomAPIHeaderAuth lists HTTP headers for custom API auth.

    Attributes:
        header_key_values (MutableSequence[google.cloud.chronicle_v1.types.CustomAPIHeaderKeyValue]):
            Optional. Add HTTP request header key-value
            pairs.
    """

    header_key_values: MutableSequence["CustomAPIHeaderKeyValue"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="CustomAPIHeaderKeyValue",
    )


class CustomAPIQueryKeyValue(proto.Message):
    r"""CustomAPIQueryKeyValue defines dynamic query parameters
    key-values for Custom API Auth.

    Attributes:
        key (str):
            Required. Enter the name of the URL Query Parameter (e.g.,
            api_key or token).
        value (str):
            Required. Enter the API Key or credential
            value associated with the query parameter.
    """

    key: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CustomAPIQueryAuth(proto.Message):
    r"""CustomAPIQueryAuth lists URL Query parameters for custom API
    auth.

    Attributes:
        query_key_values (MutableSequence[google.cloud.chronicle_v1.types.CustomAPIQueryKeyValue]):
            Optional. Add URL Query parameter key-value
            pairs.
    """

    query_key_values: MutableSequence["CustomAPIQueryKeyValue"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="CustomAPIQueryKeyValue",
    )


class CustomAPINoAuth(proto.Message):
    r"""Info for No-Authentication custom API feeds."""


class CustomAPISettings(proto.Message):
    r"""Settings required by Feeds of Custom API (Codeless).
    Supports fetching data from third-party APIs with configurable
    pagination, authentication, and response parsing.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        no_auth (google.cloud.chronicle_v1.types.CustomAPINoAuth):
            Authenticate without credentials or secrets.

            This field is a member of `oneof`_ ``authentication``.
        basic_auth (google.cloud.chronicle_v1.types.UsernameSecretAuth):
            Authenticate using Username/Password
            credentials.

            This field is a member of `oneof`_ ``authentication``.
        oauth_client_credentials (google.cloud.chronicle_v1.types.OAuthClientCredentials):
            Authenticate using OAuth 2.0 Client
            Credentials Grant flow.

            This field is a member of `oneof`_ ``authentication``.
        header_auth (google.cloud.chronicle_v1.types.CustomAPIHeaderAuth):
            Authenticate using custom API Keys injected
            into request headers.

            This field is a member of `oneof`_ ``authentication``.
        query_auth (google.cloud.chronicle_v1.types.CustomAPIQueryAuth):
            Authenticate using custom API Keys injected
            into URL query parameters.

            This field is a member of `oneof`_ ``authentication``.
        base_url (str):
            Required. Enter the primary web address of
            the third-party API (e.g.,
            https://api.vendor.com).
        polling_frequency (int):
            Optional. Specify how often the platform
            checks the API for new data in minutes (default
            is 15 minutes).
        primary_request (google.cloud.chronicle_v1.types.CustomAPITransferNode):
            Required. Configure the initial API call used
            to fetch the main list of logs or events.
    """

    no_auth: "CustomAPINoAuth" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="authentication",
        message="CustomAPINoAuth",
    )
    basic_auth: "UsernameSecretAuth" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="authentication",
        message="UsernameSecretAuth",
    )
    oauth_client_credentials: "OAuthClientCredentials" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="authentication",
        message="OAuthClientCredentials",
    )
    header_auth: "CustomAPIHeaderAuth" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="authentication",
        message="CustomAPIHeaderAuth",
    )
    query_auth: "CustomAPIQueryAuth" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="authentication",
        message="CustomAPIQueryAuth",
    )
    base_url: str = proto.Field(
        proto.STRING,
        number=1,
    )
    polling_frequency: int = proto.Field(
        proto.INT32,
        number=2,
    )
    primary_request: "CustomAPITransferNode" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="CustomAPITransferNode",
    )


class CustomAPITransferNode(proto.Message):
    r"""Container for a specific API interaction.

    Attributes:
        request_settings (google.cloud.chronicle_v1.types.CustomAPIRequestConfig):
            Required. Define the technical parameters for
            the outgoing API call, including paths, headers,
            and payloads.
        response_mapping (google.cloud.chronicle_v1.types.CustomAPIResponseConfig):
            Required. Provide rules that tell the
            platform how to locate and extract the relevant
            security data from the API's reply.
        pagination_strategy (google.cloud.chronicle_v1.types.CustomAPIPagination):
            Required. Select how the connector should
            request subsequent pages when the data is too
            large for a single response.
        checkpointing (google.cloud.chronicle_v1.types.CustomAPICheckpointConfig):
            Required. Configure settings that allow the
            connector to remember where it left off in the
            previous poll (e.g., tracking the last fetched
            timestamp).
        dependent_requests_config (google.cloud.chronicle_v1.types.CustomAPIDependentRequestsConfig):
            Optional. Configuration for dependent
            requests (child chaining).
    """

    request_settings: "CustomAPIRequestConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CustomAPIRequestConfig",
    )
    response_mapping: "CustomAPIResponseConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="CustomAPIResponseConfig",
    )
    pagination_strategy: "CustomAPIPagination" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="CustomAPIPagination",
    )
    checkpointing: "CustomAPICheckpointConfig" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="CustomAPICheckpointConfig",
    )
    dependent_requests_config: "CustomAPIDependentRequestsConfig" = proto.Field(
        proto.MESSAGE,
        number=8,
        message="CustomAPIDependentRequestsConfig",
    )


class CustomAPIDependentRequestsConfig(proto.Message):
    r"""Configuration for dependent requests (child chaining).

    Attributes:
        item_id_json_path (str):
            Required. Enter the specific field in the
            response that uniquely identifies an individual
            record or alert.
        item_id_variable (str):
            Optional. Specify a custom variable name to
            hold the extracted ID, which can be linked as a
            placeholder in dependent requests.
        dependent_requests (MutableSequence[google.cloud.chronicle_v1.types.CustomAPITransferNode]):
            Optional. Add follow-up API calls triggered
            for each item found in the primary request
            (e.g., fetching full event details for a list of
            basic alert IDs). Note: In MVP, the child depth
            fan-out limit is capped at 1.
    """

    item_id_json_path: str = proto.Field(
        proto.STRING,
        number=1,
    )
    item_id_variable: str = proto.Field(
        proto.STRING,
        number=2,
    )
    dependent_requests: MutableSequence["CustomAPITransferNode"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="CustomAPITransferNode",
    )


class CustomAPIRequestConfig(proto.Message):
    r"""Configuration for the outgoing API request.

    Attributes:
        endpoint_path (str):
            Required. Enter the specific API route
            appended to the Base URL to fetch the data
            (e.g., /v1/alerts).
        http_method (google.cloud.chronicle_v1.types.CustomAPIRequestConfig.HttpMethod):
            Required. Select the type of action to
            perform on the API endpoint (usually GET to
            retrieve data or POST to submit a query).
        request_body (str):
            Optional. Provide the data payload sent to
            the API to specify what information you want,
            typically formatted in JSON.
        query_parameters (MutableSequence[google.cloud.chronicle_v1.types.HeaderKeyValue]):
            Optional. Add extra filters or settings
            appended to the end of the URL (e.g.,
            ?status=critical).
        custom_headers (MutableSequence[google.cloud.chronicle_v1.types.HeaderKeyValue]):
            Optional. Define specialized key-value pairs
            sent with the request, often used for custom API
            versioning or specific vendor requirements.
        max_requests_per_minute (int):
            Optional. Set a safety limit to ensure the
            connector does not exceed the third-party
            vendor's API rate limits.
    """

    class HttpMethod(proto.Enum):
        r"""HTTPS methods supported.

        Values:
            HTTP_METHOD_UNSPECIFIED (0):
                Unspecified method.
            GET (1):
                HTTP GET method.
            POST (2):
                HTTP POST method.
        """

        HTTP_METHOD_UNSPECIFIED = 0
        GET = 1
        POST = 2

    endpoint_path: str = proto.Field(
        proto.STRING,
        number=1,
    )
    http_method: HttpMethod = proto.Field(
        proto.ENUM,
        number=2,
        enum=HttpMethod,
    )
    request_body: str = proto.Field(
        proto.STRING,
        number=3,
    )
    query_parameters: MutableSequence["HeaderKeyValue"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="HeaderKeyValue",
    )
    custom_headers: MutableSequence["HeaderKeyValue"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="HeaderKeyValue",
    )
    max_requests_per_minute: int = proto.Field(
        proto.INT32,
        number=6,
    )


class CustomAPIResponseConfig(proto.Message):
    r"""Configuration for handling the API response.

    Attributes:
        target_data_path (MutableSequence[str]):
            Required. Enter the exact path in the API's
            response payload where the list of target log
            entries is located.
    """

    target_data_path: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class CustomAPICheckpointConfig(proto.Message):
    r"""Checkpoint configuration to enable sequential (cursor-based)
    polling.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        none_strategy (google.cloud.chronicle_v1.types.CustomAPICheckpointConfig.NoneStrategy):
            Fetch all available data in one go without
            tracking progress.

            This field is a member of `oneof`_ ``strategy``.
        latest_timestamp_strategy (google.cloud.chronicle_v1.types.CustomAPICheckpointConfig.LatestTimestampStrategy):
            Track the timestamp of the newest record to
            fetch newer ones next.

            This field is a member of `oneof`_ ``strategy``.
        latest_record_strategy (google.cloud.chronicle_v1.types.CustomAPICheckpointConfig.LatestRecordStrategy):
            Track the highest record ID to fetch only new
            records next.

            This field is a member of `oneof`_ ``strategy``.
        iterator_strategy (google.cloud.chronicle_v1.types.CustomAPICheckpointConfig.IteratorStrategy):
            Use progress tokens provided by the API.

            This field is a member of `oneof`_ ``strategy``.
    """

    class NoneStrategy(proto.Message):
        r"""Fetch all available data in one go without tracking progress."""

    class LatestTimestampStrategy(proto.Message):
        r"""Track the timestamp of the newest record to fetch newer ones
        next.

        Attributes:
            checkpoint_value_path (str):
                Required. Enter the exact location within a
                log record where the checkpoint value (like a
                timestamp or ID) is found.
            checkpoint_variable (str):
                Required. Specify a custom name you assign to
                store and reference the checkpoint value between
                polling cycles.
        """

        checkpoint_value_path: str = proto.Field(
            proto.STRING,
            number=1,
        )
        checkpoint_variable: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class LatestRecordStrategy(proto.Message):
        r"""Track the highest record ID to fetch only new records next.

        Attributes:
            checkpoint_value_path (str):
                Required. Enter the exact location within a
                log record where the checkpoint value (like a
                timestamp or ID) is found.
            checkpoint_variable (str):
                Required. Specify a custom name you assign to
                store and reference the checkpoint value between
                polling cycles.
        """

        checkpoint_value_path: str = proto.Field(
            proto.STRING,
            number=1,
        )
        checkpoint_variable: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class IteratorStrategy(proto.Message):
        r"""Use progress tokens provided by the API.

        Attributes:
            checkpoint_value_path (str):
                Required. Enter the exact location within a
                log record where the checkpoint value (like a
                timestamp or ID) is found.
            checkpoint_variable (str):
                Required. Specify a custom name you assign to
                store and reference the checkpoint value between
                polling cycles.
        """

        checkpoint_value_path: str = proto.Field(
            proto.STRING,
            number=1,
        )
        checkpoint_variable: str = proto.Field(
            proto.STRING,
            number=2,
        )

    none_strategy: NoneStrategy = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="strategy",
        message=NoneStrategy,
    )
    latest_timestamp_strategy: LatestTimestampStrategy = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="strategy",
        message=LatestTimestampStrategy,
    )
    latest_record_strategy: LatestRecordStrategy = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="strategy",
        message=LatestRecordStrategy,
    )
    iterator_strategy: IteratorStrategy = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="strategy",
        message=IteratorStrategy,
    )


class CustomAPIPagination(proto.Message):
    r"""Pagination strategy for the request.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        none (google.cloud.chronicle_v1.types.CustomAPIPagination.NonePagination):
            Fetch data in a single request without
            paging.

            This field is a member of `oneof`_ ``pagination_strategy``.
        token (google.cloud.chronicle_v1.types.CustomAPIPagination.TokenPagination):
            Use tokens (custom keys) to get the next page
            of data.

            This field is a member of `oneof`_ ``pagination_strategy``.
        link (google.cloud.chronicle_v1.types.CustomAPIPagination.LinkPagination):
            Follow links provided in the response to get
            more data.

            This field is a member of `oneof`_ ``pagination_strategy``.
        offset (google.cloud.chronicle_v1.types.CustomAPIPagination.OffsetPagination):
            Skip a set number of records to get the next
            set.

            This field is a member of `oneof`_ ``pagination_strategy``.
        page_number (google.cloud.chronicle_v1.types.CustomAPIPagination.PageNumberPagination):
            Go to the next page number (e.g., page 2).

            This field is a member of `oneof`_ ``pagination_strategy``.
    """

    class NonePagination(proto.Message):
        r"""Fetch data in a single request without paging."""

    class TokenPagination(proto.Message):
        r"""Use tokens (custom keys) to get the next page of data.

        Attributes:
            next_page_token_json_path (str):
                Required. Enter the field in the API response
                that contains the URL or token needed to fetch
                the next page of data.
            query_param (str):
                Required. Specify the name of the query
                parameter for next page token in request.
        """

        next_page_token_json_path: str = proto.Field(
            proto.STRING,
            number=1,
        )
        query_param: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class LinkPagination(proto.Message):
        r"""Follow links provided in the response to get more data.

        Attributes:
            next_page_link_json_path (str):
                Required. Enter the field in the API response
                that contains the URL or token needed to fetch
                the next page of data.
        """

        next_page_link_json_path: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class OffsetPagination(proto.Message):
        r"""Skip a set number of records to get the next set.

        Attributes:
            offset_query_param (str):
                Required. Specify the name of the query
                parameter for offset in request.
        """

        offset_query_param: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class PageNumberPagination(proto.Message):
        r"""Go to the next page number (e.g., page 2).

        Attributes:
            page_number_query_param (str):
                Required. Specify the name of the query
                parameter for page number in request.
        """

        page_number_query_param: str = proto.Field(
            proto.STRING,
            number=1,
        )

    none: NonePagination = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="pagination_strategy",
        message=NonePagination,
    )
    token: TokenPagination = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="pagination_strategy",
        message=TokenPagination,
    )
    link: LinkPagination = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="pagination_strategy",
        message=LinkPagination,
    )
    offset: OffsetPagination = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="pagination_strategy",
        message=OffsetPagination,
    )
    page_number: PageNumberPagination = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="pagination_strategy",
        message=PageNumberPagination,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
