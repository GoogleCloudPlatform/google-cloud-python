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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.protobuf.wrappers_pb2 as wrappers_pb2  # type: ignore
import google.type.date_pb2 as date_pb2  # type: ignore
import proto  # type: ignore

from google.analytics.admin_v1alpha.types import audience as gaa_audience
from google.analytics.admin_v1alpha.types import channel_group as gaa_channel_group
from google.analytics.admin_v1alpha.types import event_create_and_edit
from google.analytics.admin_v1alpha.types import (
    expanded_data_set as gaa_expanded_data_set,
)

__protobuf__ = proto.module(
    package="google.analytics.admin.v1alpha",
    manifest={
        "IndustryCategory",
        "ServiceLevel",
        "ActorType",
        "ActionType",
        "ChangeHistoryResourceType",
        "GoogleSignalsState",
        "GoogleSignalsConsent",
        "LinkProposalInitiatingProduct",
        "LinkProposalState",
        "PropertyType",
        "CoarseValue",
        "Account",
        "Property",
        "DataStream",
        "FirebaseLink",
        "GlobalSiteTag",
        "GoogleAdsLink",
        "DataSharingSettings",
        "AccountSummary",
        "PropertySummary",
        "MeasurementProtocolSecret",
        "SKAdNetworkConversionValueSchema",
        "PostbackWindow",
        "ConversionValues",
        "EventMapping",
        "ChangeHistoryEvent",
        "ChangeHistoryChange",
        "DisplayVideo360AdvertiserLink",
        "DisplayVideo360AdvertiserLinkProposal",
        "SearchAds360Link",
        "LinkProposalStatusDetails",
        "ConversionEvent",
        "KeyEvent",
        "GoogleSignalsSettings",
        "CustomDimension",
        "CustomMetric",
        "CalculatedMetric",
        "DataRetentionSettings",
        "AttributionSettings",
        "AccessBinding",
        "BigQueryLink",
        "EnhancedMeasurementSettings",
        "DataRedactionSettings",
        "AdSenseLink",
        "RollupPropertySourceLink",
        "ReportingDataAnnotation",
        "SubpropertySyncConfig",
        "ReportingIdentitySettings",
        "UserProvidedDataSettings",
    },
)


class IndustryCategory(proto.Enum):
    r"""The category selected for this property, used for industry
    benchmarking.

    Values:
        INDUSTRY_CATEGORY_UNSPECIFIED (0):
            Industry category unspecified
        AUTOMOTIVE (1):
            Automotive
        BUSINESS_AND_INDUSTRIAL_MARKETS (2):
            Business and industrial markets
        FINANCE (3):
            Finance
        HEALTHCARE (4):
            Healthcare
        TECHNOLOGY (5):
            Technology
        TRAVEL (6):
            Travel
        OTHER (7):
            Other
        ARTS_AND_ENTERTAINMENT (8):
            Arts and entertainment
        BEAUTY_AND_FITNESS (9):
            Beauty and fitness
        BOOKS_AND_LITERATURE (10):
            Books and literature
        FOOD_AND_DRINK (11):
            Food and drink
        GAMES (12):
            Games
        HOBBIES_AND_LEISURE (13):
            Hobbies and leisure
        HOME_AND_GARDEN (14):
            Home and garden
        INTERNET_AND_TELECOM (15):
            Internet and telecom
        LAW_AND_GOVERNMENT (16):
            Law and government
        NEWS (17):
            News
        ONLINE_COMMUNITIES (18):
            Online communities
        PEOPLE_AND_SOCIETY (19):
            People and society
        PETS_AND_ANIMALS (20):
            Pets and animals
        REAL_ESTATE (21):
            Real estate
        REFERENCE (22):
            Reference
        SCIENCE (23):
            Science
        SPORTS (24):
            Sports
        JOBS_AND_EDUCATION (25):
            Jobs and education
        SHOPPING (26):
            Shopping
    """

    INDUSTRY_CATEGORY_UNSPECIFIED = 0
    AUTOMOTIVE = 1
    BUSINESS_AND_INDUSTRIAL_MARKETS = 2
    FINANCE = 3
    HEALTHCARE = 4
    TECHNOLOGY = 5
    TRAVEL = 6
    OTHER = 7
    ARTS_AND_ENTERTAINMENT = 8
    BEAUTY_AND_FITNESS = 9
    BOOKS_AND_LITERATURE = 10
    FOOD_AND_DRINK = 11
    GAMES = 12
    HOBBIES_AND_LEISURE = 13
    HOME_AND_GARDEN = 14
    INTERNET_AND_TELECOM = 15
    LAW_AND_GOVERNMENT = 16
    NEWS = 17
    ONLINE_COMMUNITIES = 18
    PEOPLE_AND_SOCIETY = 19
    PETS_AND_ANIMALS = 20
    REAL_ESTATE = 21
    REFERENCE = 22
    SCIENCE = 23
    SPORTS = 24
    JOBS_AND_EDUCATION = 25
    SHOPPING = 26


class ServiceLevel(proto.Enum):
    r"""Various levels of service for Google Analytics.

    Values:
        SERVICE_LEVEL_UNSPECIFIED (0):
            Service level not specified or invalid.
        GOOGLE_ANALYTICS_STANDARD (1):
            The standard version of Google Analytics.
        GOOGLE_ANALYTICS_360 (2):
            The paid, premium version of Google
            Analytics.
    """

    SERVICE_LEVEL_UNSPECIFIED = 0
    GOOGLE_ANALYTICS_STANDARD = 1
    GOOGLE_ANALYTICS_360 = 2


class ActorType(proto.Enum):
    r"""Different kinds of actors that can make changes to Google
    Analytics resources.

    Values:
        ACTOR_TYPE_UNSPECIFIED (0):
            Unknown or unspecified actor type.
        USER (1):
            Changes made by the user specified in actor_email.
        SYSTEM (2):
            Changes made by the Google Analytics system.
        SUPPORT (3):
            Changes made by Google Analytics support team
            staff.
    """

    ACTOR_TYPE_UNSPECIFIED = 0
    USER = 1
    SYSTEM = 2
    SUPPORT = 3


class ActionType(proto.Enum):
    r"""Types of actions that may change a resource.

    Values:
        ACTION_TYPE_UNSPECIFIED (0):
            Action type unknown or not specified.
        CREATED (1):
            Resource was created in this change.
        UPDATED (2):
            Resource was updated in this change.
        DELETED (3):
            Resource was deleted in this change.
    """

    ACTION_TYPE_UNSPECIFIED = 0
    CREATED = 1
    UPDATED = 2
    DELETED = 3


class ChangeHistoryResourceType(proto.Enum):
    r"""Types of resources whose changes may be returned from change
    history.

    Values:
        CHANGE_HISTORY_RESOURCE_TYPE_UNSPECIFIED (0):
            Resource type unknown or not specified.
        ACCOUNT (1):
            Account resource
        PROPERTY (2):
            Property resource
        FIREBASE_LINK (6):
            FirebaseLink resource
        GOOGLE_ADS_LINK (7):
            GoogleAdsLink resource
        GOOGLE_SIGNALS_SETTINGS (8):
            GoogleSignalsSettings resource
        CONVERSION_EVENT (9):
            ConversionEvent resource
        MEASUREMENT_PROTOCOL_SECRET (10):
            MeasurementProtocolSecret resource
        CUSTOM_DIMENSION (11):
            CustomDimension resource
        CUSTOM_METRIC (12):
            CustomMetric resource
        DATA_RETENTION_SETTINGS (13):
            DataRetentionSettings resource
        DISPLAY_VIDEO_360_ADVERTISER_LINK (14):
            DisplayVideo360AdvertiserLink resource
        DISPLAY_VIDEO_360_ADVERTISER_LINK_PROPOSAL (15):
            DisplayVideo360AdvertiserLinkProposal
            resource
        SEARCH_ADS_360_LINK (16):
            SearchAds360Link resource
        DATA_STREAM (18):
            DataStream resource
        ATTRIBUTION_SETTINGS (20):
            AttributionSettings resource
        EXPANDED_DATA_SET (21):
            ExpandedDataSet resource
        CHANNEL_GROUP (22):
            ChannelGroup resource
        BIGQUERY_LINK (23):
            BigQuery link resource
        ENHANCED_MEASUREMENT_SETTINGS (24):
            EnhancedMeasurementSettings resource
        DATA_REDACTION_SETTINGS (25):
            DataRedactionSettings resource
        SKADNETWORK_CONVERSION_VALUE_SCHEMA (26):
            SKAdNetworkConversionValueSchema resource
        ADSENSE_LINK (27):
            AdSenseLink resource
        AUDIENCE (28):
            Audience resource
        EVENT_CREATE_RULE (29):
            EventCreateRule resource
        KEY_EVENT (30):
            KeyEvent resource
        CALCULATED_METRIC (31):
            CalculatedMetric resource
        REPORTING_DATA_ANNOTATION (32):
            ReportingDataAnnotation resource
        SUBPROPERTY_SYNC_CONFIG (33):
            SubpropertySyncConfig resource
        REPORTING_IDENTITY_SETTINGS (34):
            ReportingIdentitySettings resource
        USER_PROVIDED_DATA_SETTINGS (35):
            UserProvidedDataSettings resource
    """

    CHANGE_HISTORY_RESOURCE_TYPE_UNSPECIFIED = 0
    ACCOUNT = 1
    PROPERTY = 2
    FIREBASE_LINK = 6
    GOOGLE_ADS_LINK = 7
    GOOGLE_SIGNALS_SETTINGS = 8
    CONVERSION_EVENT = 9
    MEASUREMENT_PROTOCOL_SECRET = 10
    CUSTOM_DIMENSION = 11
    CUSTOM_METRIC = 12
    DATA_RETENTION_SETTINGS = 13
    DISPLAY_VIDEO_360_ADVERTISER_LINK = 14
    DISPLAY_VIDEO_360_ADVERTISER_LINK_PROPOSAL = 15
    SEARCH_ADS_360_LINK = 16
    DATA_STREAM = 18
    ATTRIBUTION_SETTINGS = 20
    EXPANDED_DATA_SET = 21
    CHANNEL_GROUP = 22
    BIGQUERY_LINK = 23
    ENHANCED_MEASUREMENT_SETTINGS = 24
    DATA_REDACTION_SETTINGS = 25
    SKADNETWORK_CONVERSION_VALUE_SCHEMA = 26
    ADSENSE_LINK = 27
    AUDIENCE = 28
    EVENT_CREATE_RULE = 29
    KEY_EVENT = 30
    CALCULATED_METRIC = 31
    REPORTING_DATA_ANNOTATION = 32
    SUBPROPERTY_SYNC_CONFIG = 33
    REPORTING_IDENTITY_SETTINGS = 34
    USER_PROVIDED_DATA_SETTINGS = 35


class GoogleSignalsState(proto.Enum):
    r"""Status of the Google Signals settings.

    Values:
        GOOGLE_SIGNALS_STATE_UNSPECIFIED (0):
            Google Signals status defaults to
            GOOGLE_SIGNALS_STATE_UNSPECIFIED to represent that the user
            has not made an explicit choice.
        GOOGLE_SIGNALS_ENABLED (1):
            Google Signals is enabled.
        GOOGLE_SIGNALS_DISABLED (2):
            Google Signals is disabled.
    """

    GOOGLE_SIGNALS_STATE_UNSPECIFIED = 0
    GOOGLE_SIGNALS_ENABLED = 1
    GOOGLE_SIGNALS_DISABLED = 2


class GoogleSignalsConsent(proto.Enum):
    r"""Consent field of the Google Signals settings.

    Values:
        GOOGLE_SIGNALS_CONSENT_UNSPECIFIED (0):
            Google Signals consent value defaults to
            GOOGLE_SIGNALS_CONSENT_UNSPECIFIED. This will be treated as
            GOOGLE_SIGNALS_CONSENT_NOT_CONSENTED.
        GOOGLE_SIGNALS_CONSENT_CONSENTED (2):
            Terms of service have been accepted
        GOOGLE_SIGNALS_CONSENT_NOT_CONSENTED (1):
            Terms of service have not been accepted
    """

    GOOGLE_SIGNALS_CONSENT_UNSPECIFIED = 0
    GOOGLE_SIGNALS_CONSENT_CONSENTED = 2
    GOOGLE_SIGNALS_CONSENT_NOT_CONSENTED = 1


class LinkProposalInitiatingProduct(proto.Enum):
    r"""An indication of which product the user initiated a link
    proposal from.

    Values:
        LINK_PROPOSAL_INITIATING_PRODUCT_UNSPECIFIED (0):
            Unspecified product.
        GOOGLE_ANALYTICS (1):
            This proposal was created by a user from
            Google Analytics.
        LINKED_PRODUCT (2):
            This proposal was created by a user from a
            linked product (not Google Analytics).
    """

    LINK_PROPOSAL_INITIATING_PRODUCT_UNSPECIFIED = 0
    GOOGLE_ANALYTICS = 1
    LINKED_PRODUCT = 2


class LinkProposalState(proto.Enum):
    r"""The state of a link proposal resource.

    Values:
        LINK_PROPOSAL_STATE_UNSPECIFIED (0):
            Unspecified state
        AWAITING_REVIEW_FROM_GOOGLE_ANALYTICS (1):
            This proposal is awaiting review from a
            Google Analytics user. This proposal will
            automatically expire after some time.
        AWAITING_REVIEW_FROM_LINKED_PRODUCT (2):
            This proposal is awaiting review from a user
            of a linked product. This proposal will
            automatically expire after some time.
        WITHDRAWN (3):
            This proposal has been withdrawn by an admin
            on the initiating product. This proposal will be
            automatically deleted after some time.
        DECLINED (4):
            This proposal has been declined by an admin
            on the receiving product. This proposal will be
            automatically deleted after some time.
        EXPIRED (5):
            This proposal expired due to lack of response
            from an admin on the receiving product. This
            proposal will be automatically deleted after
            some time.
        OBSOLETE (6):
            This proposal has become obsolete because a
            link was directly created to the same external
            product resource that this proposal specifies.
            This proposal will be automatically deleted
            after some time.
    """

    LINK_PROPOSAL_STATE_UNSPECIFIED = 0
    AWAITING_REVIEW_FROM_GOOGLE_ANALYTICS = 1
    AWAITING_REVIEW_FROM_LINKED_PRODUCT = 2
    WITHDRAWN = 3
    DECLINED = 4
    EXPIRED = 5
    OBSOLETE = 6


class PropertyType(proto.Enum):
    r"""Types of ``Property`` resources.

    Values:
        PROPERTY_TYPE_UNSPECIFIED (0):
            Unknown or unspecified property type
        PROPERTY_TYPE_ORDINARY (1):
            Ordinary Google Analytics property
        PROPERTY_TYPE_SUBPROPERTY (2):
            Google Analytics subproperty
        PROPERTY_TYPE_ROLLUP (3):
            Google Analytics rollup property
    """

    PROPERTY_TYPE_UNSPECIFIED = 0
    PROPERTY_TYPE_ORDINARY = 1
    PROPERTY_TYPE_SUBPROPERTY = 2
    PROPERTY_TYPE_ROLLUP = 3


class CoarseValue(proto.Enum):
    r"""The coarse conversion value set on the updatePostbackConversionValue
    SDK call when a ConversionValues.event_mappings conditions are
    satisfied. For more information, see
    `SKAdNetwork.CoarseConversionValue <https://developer.apple.com/documentation/storekit/skadnetwork/coarseconversionvalue>`__.

    Values:
        COARSE_VALUE_UNSPECIFIED (0):
            Coarse value not specified.
        COARSE_VALUE_LOW (1):
            Coarse value of low.
        COARSE_VALUE_MEDIUM (2):
            Coarse value of medium.
        COARSE_VALUE_HIGH (3):
            Coarse value of high.
    """

    COARSE_VALUE_UNSPECIFIED = 0
    COARSE_VALUE_LOW = 1
    COARSE_VALUE_MEDIUM = 2
    COARSE_VALUE_HIGH = 3


class Account(proto.Message):
    r"""A resource message representing a Google Analytics account.

    Attributes:
        name (str):
            Identifier. Resource name of this account.
            Format: accounts/{account}
            Example: "accounts/100".
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when this account was
            originally created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when account payload fields
            were last updated.
        display_name (str):
            Required. Human-readable display name for
            this account.
        region_code (str):
            Country of business. Must be a Unicode CLDR
            region code.
        deleted (bool):
            Output only. Indicates whether this Account
            is soft-deleted or not. Deleted accounts are
            excluded from List results unless specifically
            requested.
        gmp_organization (str):
            Output only. The URI for a Google Marketing Platform
            organization resource. Only set when this account is
            connected to a GMP organization. Format:
            marketingplatformadmin.googleapis.com/organizations/{org_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    region_code: str = proto.Field(
        proto.STRING,
        number=5,
    )
    deleted: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    gmp_organization: str = proto.Field(
        proto.STRING,
        number=7,
    )


class Property(proto.Message):
    r"""A resource message representing a Google Analytics property.

    Attributes:
        name (str):
            Identifier. Resource name of this property. Format:
            properties/{property_id} Example: "properties/1000".
        property_type (google.analytics.admin_v1alpha.types.PropertyType):
            Immutable. The property type for this Property resource.
            When creating a property, if the type is
            "PROPERTY_TYPE_UNSPECIFIED", then "ORDINARY_PROPERTY" will
            be implied.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the entity was
            originally created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when entity payload fields
            were last updated.
        parent (str):
            Immutable. Resource name of this property's
            logical parent.
            Note: The Property-Moving UI can be used to
            change the parent. Format: accounts/{account},
            properties/{property} Example: "accounts/100",
            "properties/101".
        display_name (str):
            Required. Human-readable display name for
            this property.
            The max allowed display name length is 100
            UTF-16 code units.
        industry_category (google.analytics.admin_v1alpha.types.IndustryCategory):
            Industry associated with this property Example: AUTOMOTIVE,
            FOOD_AND_DRINK
        time_zone (str):
            Required. Reporting Time Zone, used as the day boundary for
            reports, regardless of where the data originates. If the
            time zone honors DST, Analytics will automatically adjust
            for the changes.

            NOTE: Changing the time zone only affects data going
            forward, and is not applied retroactively.

            Format: https://www.iana.org/time-zones Example:
            "America/Los_Angeles".
        currency_code (str):
            The currency type used in reports involving monetary values.

            Format: https://en.wikipedia.org/wiki/ISO_4217 Examples:
            "USD", "EUR", "JPY".
        service_level (google.analytics.admin_v1alpha.types.ServiceLevel):
            Output only. The Google Analytics service
            level that applies to this property.
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. If set, the time at which this
            property was trashed. If not set, then this
            property is not currently in the trash can.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. If set, the time at which this
            trashed property will be permanently deleted. If
            not set, then this property is not currently in
            the trash can and is not slated to be deleted.
        account (str):
            Immutable. The resource name of the parent account Format:
            accounts/{account_id} Example: "accounts/123".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    property_type: "PropertyType" = proto.Field(
        proto.ENUM,
        number=14,
        enum="PropertyType",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    industry_category: "IndustryCategory" = proto.Field(
        proto.ENUM,
        number=6,
        enum="IndustryCategory",
    )
    time_zone: str = proto.Field(
        proto.STRING,
        number=7,
    )
    currency_code: str = proto.Field(
        proto.STRING,
        number=8,
    )
    service_level: "ServiceLevel" = proto.Field(
        proto.ENUM,
        number=10,
        enum="ServiceLevel",
    )
    delete_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        message=timestamp_pb2.Timestamp,
    )
    account: str = proto.Field(
        proto.STRING,
        number=13,
    )


class DataStream(proto.Message):
    r"""A resource message representing a data stream.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        web_stream_data (google.analytics.admin_v1alpha.types.DataStream.WebStreamData):
            Data specific to web streams. Must be populated if type is
            WEB_DATA_STREAM.

            This field is a member of `oneof`_ ``stream_data``.
        android_app_stream_data (google.analytics.admin_v1alpha.types.DataStream.AndroidAppStreamData):
            Data specific to Android app streams. Must be populated if
            type is ANDROID_APP_DATA_STREAM.

            This field is a member of `oneof`_ ``stream_data``.
        ios_app_stream_data (google.analytics.admin_v1alpha.types.DataStream.IosAppStreamData):
            Data specific to iOS app streams. Must be populated if type
            is IOS_APP_DATA_STREAM.

            This field is a member of `oneof`_ ``stream_data``.
        name (str):
            Identifier. Resource name of this Data Stream. Format:
            properties/{property_id}/dataStreams/{stream_id} Example:
            "properties/1000/dataStreams/2000".
        type_ (google.analytics.admin_v1alpha.types.DataStream.DataStreamType):
            Required. Immutable. The type of this
            DataStream resource.
        display_name (str):
            Human-readable display name for the Data
            Stream.
            Required for web data streams.

            The max allowed display name length is 255
            UTF-16 code units.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when this stream was
            originally created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when stream payload fields
            were last updated.
    """

    class DataStreamType(proto.Enum):
        r"""The type of the data stream.

        Values:
            DATA_STREAM_TYPE_UNSPECIFIED (0):
                Type unknown or not specified.
            WEB_DATA_STREAM (1):
                Web data stream.
            ANDROID_APP_DATA_STREAM (2):
                Android app data stream.
            IOS_APP_DATA_STREAM (3):
                iOS app data stream.
        """

        DATA_STREAM_TYPE_UNSPECIFIED = 0
        WEB_DATA_STREAM = 1
        ANDROID_APP_DATA_STREAM = 2
        IOS_APP_DATA_STREAM = 3

    class WebStreamData(proto.Message):
        r"""Data specific to web streams.

        Attributes:
            measurement_id (str):
                Output only. Analytics Measurement ID.

                Example: "G-1A2BCD345E".
            firebase_app_id (str):
                Output only. ID of the corresponding web app
                in Firebase, if any. This ID can change if the
                web app is deleted and recreated.
            default_uri (str):
                Domain name of the web app being measured, or
                empty. Example: "http://www.google.com",
                "https://www.google.com".
        """

        measurement_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        firebase_app_id: str = proto.Field(
            proto.STRING,
            number=2,
        )
        default_uri: str = proto.Field(
            proto.STRING,
            number=3,
        )

    class AndroidAppStreamData(proto.Message):
        r"""Data specific to Android app streams.

        Attributes:
            firebase_app_id (str):
                Output only. ID of the corresponding Android
                app in Firebase, if any. This ID can change if
                the Android app is deleted and recreated.
            package_name (str):
                Immutable. The package name for the app being
                measured. Example: "com.example.myandroidapp".
        """

        firebase_app_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        package_name: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class IosAppStreamData(proto.Message):
        r"""Data specific to iOS app streams.

        Attributes:
            firebase_app_id (str):
                Output only. ID of the corresponding iOS app
                in Firebase, if any. This ID can change if the
                iOS app is deleted and recreated.
            bundle_id (str):
                Required. Immutable. The Apple App Store
                Bundle ID for the app Example:
                "com.example.myiosapp".
        """

        firebase_app_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        bundle_id: str = proto.Field(
            proto.STRING,
            number=2,
        )

    web_stream_data: WebStreamData = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="stream_data",
        message=WebStreamData,
    )
    android_app_stream_data: AndroidAppStreamData = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="stream_data",
        message=AndroidAppStreamData,
    )
    ios_app_stream_data: IosAppStreamData = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="stream_data",
        message=IosAppStreamData,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: DataStreamType = proto.Field(
        proto.ENUM,
        number=2,
        enum=DataStreamType,
    )
    display_name: str = proto.Field(
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


class FirebaseLink(proto.Message):
    r"""A link between a Google Analytics property and a Firebase
    project.

    Attributes:
        name (str):
            Identifier. Example format:
            properties/1234/firebaseLinks/5678
        project (str):
            Immutable. Firebase project resource name. When creating a
            FirebaseLink, you may provide this resource name using
            either a project number or project ID. Once this resource
            has been created, returned FirebaseLinks will always have a
            project_name that contains a project number.

            Format: 'projects/{project number}' Example: 'projects/1234'
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when this FirebaseLink was
            originally created.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class GlobalSiteTag(proto.Message):
    r"""Read-only resource with the tag for sending data from a
    website to a DataStream. Only present for web DataStream
    resources.

    Attributes:
        name (str):
            Identifier. Resource name for this GlobalSiteTag resource.
            Format:
            properties/{property_id}/dataStreams/{stream_id}/globalSiteTag
            Example: "properties/123/dataStreams/456/globalSiteTag".
        snippet (str):
            Immutable. JavaScript code snippet to be
            pasted as the first item into the head tag of
            every webpage to measure.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    snippet: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GoogleAdsLink(proto.Message):
    r"""A link between a Google Analytics property and a Google Ads
    account.

    Attributes:
        name (str):
            Identifier. Format:

            properties/{propertyId}/googleAdsLinks/{googleAdsLinkId}

            Note: googleAdsLinkId is not the Google Ads
            customer ID.
        customer_id (str):
            Immutable. Google Ads customer ID.
        can_manage_clients (bool):
            Output only. If true, this link is for a
            Google Ads manager account.
        ads_personalization_enabled (google.protobuf.wrappers_pb2.BoolValue):
            Enable personalized advertising features with
            this integration. Automatically publish my
            Google Analytics audience lists and Google
            Analytics remarketing events/parameters to the
            linked Google Ads account. If this field is not
            set on create/update, it will be defaulted to
            true.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when this link was
            originally created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when this link was last
            updated.
        creator_email_address (str):
            Output only. Email address of the user that
            created the link. An empty string will be
            returned if the email address can't be
            retrieved.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    customer_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    can_manage_clients: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    ads_personalization_enabled: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=5,
        message=wrappers_pb2.BoolValue,
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
    creator_email_address: str = proto.Field(
        proto.STRING,
        number=9,
    )


class DataSharingSettings(proto.Message):
    r"""A resource message representing data sharing settings of a
    Google Analytics account.

    Attributes:
        name (str):
            Identifier. Resource name.
            Format: accounts/{account}/dataSharingSettings
            Example: "accounts/1000/dataSharingSettings".
        sharing_with_google_support_enabled (bool):
            Allows Google technical support
            representatives access to your Google Analytics
            data and account when necessary to provide
            service and find solutions to technical issues.

            This field maps to the "Technical support" field
            in the Google Analytics Admin UI.
        sharing_with_google_assigned_sales_enabled (bool):
            Allows Google access to your Google Analytics
            account data, including account usage and
            configuration data, product spending, and users
            associated with your Google Analytics account,
            so that Google can help you make the most of
            Google products, providing you with insights,
            offers, recommendations, and optimization tips
            across Google Analytics and other Google
            products for business.

            This field maps to the "Recommendations for your
            business" field in the Google Analytics Admin
            UI.
        sharing_with_google_any_sales_enabled (bool):
            Deprecated. This field is no longer used and
            always returns false.
        sharing_with_google_products_enabled (bool):
            Allows Google to use the data to improve
            other Google products or services.
            This fields maps to the "Google products &
            services" field in the Google Analytics Admin
            UI.
        sharing_with_others_enabled (bool):
            Enable features like predictions, modeled
            data, and benchmarking that can provide you with
            richer business insights when you contribute
            aggregated measurement data. The data you share
            (including information about the property from
            which it is shared) is aggregated and
            de-identified before being used to generate
            business insights.

            This field maps to the "Modeling contributions &
            business insights" field in the Google Analytics
            Admin UI.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    sharing_with_google_support_enabled: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    sharing_with_google_assigned_sales_enabled: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    sharing_with_google_any_sales_enabled: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    sharing_with_google_products_enabled: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    sharing_with_others_enabled: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class AccountSummary(proto.Message):
    r"""A virtual resource representing an overview of an account and
    all its child Google Analytics properties.

    Attributes:
        name (str):
            Identifier. Resource name for this account summary. Format:
            accountSummaries/{account_id} Example:
            "accountSummaries/1000".
        account (str):
            Resource name of account referred to by this account summary
            Format: accounts/{account_id} Example: "accounts/1000".
        display_name (str):
            Display name for the account referred to in
            this account summary.
        property_summaries (MutableSequence[google.analytics.admin_v1alpha.types.PropertySummary]):
            List of summaries for child accounts of this
            account.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    account: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    property_summaries: MutableSequence["PropertySummary"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="PropertySummary",
    )


class PropertySummary(proto.Message):
    r"""A virtual resource representing metadata for a Google
    Analytics property.

    Attributes:
        property (str):
            Resource name of property referred to by this property
            summary Format: properties/{property_id} Example:
            "properties/1000".
        display_name (str):
            Display name for the property referred to in
            this property summary.
        property_type (google.analytics.admin_v1alpha.types.PropertyType):
            The property's property type.
        parent (str):
            Resource name of this property's logical
            parent.
            Note: The Property-Moving UI can be used to
            change the parent. Format: accounts/{account},
            properties/{property} Example: "accounts/100",
            "properties/200".
        can_edit (bool):
            If true, then the user has a Google Analytics
            role that permits them to edit the property.
    """

    property: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    property_type: "PropertyType" = proto.Field(
        proto.ENUM,
        number=3,
        enum="PropertyType",
    )
    parent: str = proto.Field(
        proto.STRING,
        number=4,
    )
    can_edit: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class MeasurementProtocolSecret(proto.Message):
    r"""A secret value used for sending hits to Measurement Protocol.

    Attributes:
        name (str):
            Identifier. Resource name of this secret.
            This secret may be a child of any type of
            stream. Format:

            properties/{property}/dataStreams/{dataStream}/measurementProtocolSecrets/{measurementProtocolSecret}
        display_name (str):
            Required. Human-readable display name for
            this secret.
        secret_value (str):
            Output only. The measurement protocol secret value. Pass
            this value to the api_secret field of the Measurement
            Protocol API when sending hits to this secret's parent
            property.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    secret_value: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SKAdNetworkConversionValueSchema(proto.Message):
    r"""SKAdNetwork conversion value schema of an iOS stream.

    Attributes:
        name (str):
            Identifier. Resource name of the schema. This
            will be child of ONLY an iOS stream, and there
            can be at most one such child under an iOS
            stream. Format:

            properties/{property}/dataStreams/{dataStream}/sKAdNetworkConversionValueSchema
        postback_window_one (google.analytics.admin_v1alpha.types.PostbackWindow):
            Required. The conversion value settings for
            the first postback window. These differ from
            values for postback window two and three in that
            they contain a "Fine" grained conversion value
            (a numeric value).

            Conversion values for this postback window must
            be set.  The other windows are optional and may
            inherit this window's settings if unset or
            disabled.
        postback_window_two (google.analytics.admin_v1alpha.types.PostbackWindow):
            The conversion value settings for the second postback
            window.

            This field should only be configured if there is a need to
            define different conversion values for this postback window.

            If enable_postback_window_settings is set to false for this
            postback window, the values from postback_window_one will be
            used.
        postback_window_three (google.analytics.admin_v1alpha.types.PostbackWindow):
            The conversion value settings for the third postback window.

            This field should only be set if the user chose to define
            different conversion values for this postback window. It is
            allowed to configure window 3 without setting window 2. In
            case window 1 & 2 settings are set and
            enable_postback_window_settings for this postback window is
            set to false, the schema will inherit settings from
            postback_window_two.
        apply_conversion_values (bool):
            If enabled, the GA SDK will set conversion
            values using this schema definition, and schema
            will be exported to any Google Ads accounts
            linked to this property. If disabled, the GA SDK
            will not automatically set conversion values,
            and also the schema will not be exported to Ads.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    postback_window_one: "PostbackWindow" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="PostbackWindow",
    )
    postback_window_two: "PostbackWindow" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="PostbackWindow",
    )
    postback_window_three: "PostbackWindow" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="PostbackWindow",
    )
    apply_conversion_values: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class PostbackWindow(proto.Message):
    r"""Settings for a SKAdNetwork conversion postback window.

    Attributes:
        conversion_values (MutableSequence[google.analytics.admin_v1alpha.types.ConversionValues]):
            Ordering of the repeated field will be used to prioritize
            the conversion value settings. Lower indexed entries are
            prioritized higher. The first conversion value setting that
            evaluates to true will be selected. It must have at least
            one entry if enable_postback_window_settings is set to true.
            It can have maximum of 128 entries.
        postback_window_settings_enabled (bool):
            If enable_postback_window_settings is true,
            conversion_values must be populated and will be used for
            determining when and how to set the Conversion Value on a
            client device and exporting schema to linked Ads accounts.
            If false, the settings are not used, but are retained in
            case they may be used in the future. This must always be
            true for postback_window_one.
    """

    conversion_values: MutableSequence["ConversionValues"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ConversionValues",
    )
    postback_window_settings_enabled: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class ConversionValues(proto.Message):
    r"""Conversion value settings for a postback window for
    SKAdNetwork conversion value schema.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        display_name (str):
            Display name of the SKAdNetwork conversion
            value. The max allowed display name length is 50
            UTF-16 code units.
        fine_value (int):
            The fine-grained conversion value. This is applicable only
            to the first postback window. Its valid values are [0,63],
            both inclusive. It must be set for postback window 1, and
            must not be set for postback window 2 & 3. This value is not
            guaranteed to be unique.

            If the configuration for the first postback window is
            re-used for second or third postback windows this field has
            no effect.

            This field is a member of `oneof`_ ``_fine_value``.
        coarse_value (google.analytics.admin_v1alpha.types.CoarseValue):
            Required. A coarse grained conversion value.

            This value is not guaranteed to be unique.
        event_mappings (MutableSequence[google.analytics.admin_v1alpha.types.EventMapping]):
            Event conditions that must be met for this
            Conversion Value to be achieved. The conditions
            in this list are ANDed together. It must have
            minimum of 1 entry and maximum of 3 entries, if
            the postback window is enabled.
        lock_enabled (bool):
            If true, the SDK should lock to this
            conversion value for the current postback
            window.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    fine_value: int = proto.Field(
        proto.INT32,
        number=2,
        optional=True,
    )
    coarse_value: "CoarseValue" = proto.Field(
        proto.ENUM,
        number=3,
        enum="CoarseValue",
    )
    event_mappings: MutableSequence["EventMapping"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="EventMapping",
    )
    lock_enabled: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class EventMapping(proto.Message):
    r"""Event setting conditions to match an event.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        event_name (str):
            Required. Name of the Google Analytics event.
            It must always be set. The max allowed display
            name length is 40 UTF-16 code units.
        min_event_count (int):
            At least one of the following four min/max
            values must be set. The values set will be ANDed
            together to qualify an event. The minimum number
            of times the event occurred. If not set, minimum
            event count won't be checked.

            This field is a member of `oneof`_ ``_min_event_count``.
        max_event_count (int):
            The maximum number of times the event
            occurred. If not set, maximum event count won't
            be checked.

            This field is a member of `oneof`_ ``_max_event_count``.
        min_event_value (float):
            The minimum revenue generated due to the
            event. Revenue currency will be defined at the
            property level. If not set, minimum event value
            won't be checked.

            This field is a member of `oneof`_ ``_min_event_value``.
        max_event_value (float):
            The maximum revenue generated due to the
            event. Revenue currency will be defined at the
            property level. If not set, maximum event value
            won't be checked.

            This field is a member of `oneof`_ ``_max_event_value``.
    """

    event_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    min_event_count: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )
    max_event_count: int = proto.Field(
        proto.INT64,
        number=3,
        optional=True,
    )
    min_event_value: float = proto.Field(
        proto.DOUBLE,
        number=4,
        optional=True,
    )
    max_event_value: float = proto.Field(
        proto.DOUBLE,
        number=5,
        optional=True,
    )


class ChangeHistoryEvent(proto.Message):
    r"""A set of changes within a Google Analytics account or its
    child properties that resulted from the same cause. Common
    causes would be updates made in the Google Analytics UI, changes
    from customer support, or automatic Google Analytics system
    changes.

    Attributes:
        id (str):
            ID of this change history event. This ID is
            unique across Google Analytics.
        change_time (google.protobuf.timestamp_pb2.Timestamp):
            Time when change was made.
        actor_type (google.analytics.admin_v1alpha.types.ActorType):
            The type of actor that made this change.
        user_actor_email (str):
            Email address of the Google account that made
            the change. This will be a valid email address
            if the actor field is set to USER, and empty
            otherwise. Google accounts that have been
            deleted will cause an error.
        changes_filtered (bool):
            If true, then the list of changes returned
            was filtered, and does not represent all changes
            that occurred in this event.
        changes (MutableSequence[google.analytics.admin_v1alpha.types.ChangeHistoryChange]):
            A list of changes made in this change history
            event that fit the filters specified in
            SearchChangeHistoryEventsRequest.
    """

    id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    change_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    actor_type: "ActorType" = proto.Field(
        proto.ENUM,
        number=3,
        enum="ActorType",
    )
    user_actor_email: str = proto.Field(
        proto.STRING,
        number=4,
    )
    changes_filtered: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    changes: MutableSequence["ChangeHistoryChange"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="ChangeHistoryChange",
    )


class ChangeHistoryChange(proto.Message):
    r"""A description of a change to a single Google Analytics
    resource.

    Attributes:
        resource (str):
            Resource name of the resource whose changes
            are described by this entry.
        action (google.analytics.admin_v1alpha.types.ActionType):
            The type of action that changed this
            resource.
        resource_before_change (google.analytics.admin_v1alpha.types.ChangeHistoryChange.ChangeHistoryResource):
            Resource contents from before the change was
            made. If this resource was created in this
            change, this field will be missing.
        resource_after_change (google.analytics.admin_v1alpha.types.ChangeHistoryChange.ChangeHistoryResource):
            Resource contents from after the change was
            made. If this resource was deleted in this
            change, this field will be missing.
    """

    class ChangeHistoryResource(proto.Message):
        r"""A snapshot of a resource as before or after the result of a
        change in change history.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            account (google.analytics.admin_v1alpha.types.Account):
                A snapshot of an Account resource in change
                history.

                This field is a member of `oneof`_ ``resource``.
            property (google.analytics.admin_v1alpha.types.Property):
                A snapshot of a Property resource in change
                history.

                This field is a member of `oneof`_ ``resource``.
            firebase_link (google.analytics.admin_v1alpha.types.FirebaseLink):
                A snapshot of a FirebaseLink resource in
                change history.

                This field is a member of `oneof`_ ``resource``.
            google_ads_link (google.analytics.admin_v1alpha.types.GoogleAdsLink):
                A snapshot of a GoogleAdsLink resource in
                change history.

                This field is a member of `oneof`_ ``resource``.
            google_signals_settings (google.analytics.admin_v1alpha.types.GoogleSignalsSettings):
                A snapshot of a GoogleSignalsSettings
                resource in change history.

                This field is a member of `oneof`_ ``resource``.
            display_video_360_advertiser_link (google.analytics.admin_v1alpha.types.DisplayVideo360AdvertiserLink):
                A snapshot of a DisplayVideo360AdvertiserLink
                resource in change history.

                This field is a member of `oneof`_ ``resource``.
            display_video_360_advertiser_link_proposal (google.analytics.admin_v1alpha.types.DisplayVideo360AdvertiserLinkProposal):
                A snapshot of a
                DisplayVideo360AdvertiserLinkProposal resource
                in change history.

                This field is a member of `oneof`_ ``resource``.
            conversion_event (google.analytics.admin_v1alpha.types.ConversionEvent):
                A snapshot of a ConversionEvent resource in
                change history.

                This field is a member of `oneof`_ ``resource``.
            measurement_protocol_secret (google.analytics.admin_v1alpha.types.MeasurementProtocolSecret):
                A snapshot of a MeasurementProtocolSecret
                resource in change history.

                This field is a member of `oneof`_ ``resource``.
            custom_dimension (google.analytics.admin_v1alpha.types.CustomDimension):
                A snapshot of a CustomDimension resource in
                change history.

                This field is a member of `oneof`_ ``resource``.
            custom_metric (google.analytics.admin_v1alpha.types.CustomMetric):
                A snapshot of a CustomMetric resource in
                change history.

                This field is a member of `oneof`_ ``resource``.
            data_retention_settings (google.analytics.admin_v1alpha.types.DataRetentionSettings):
                A snapshot of a data retention settings
                resource in change history.

                This field is a member of `oneof`_ ``resource``.
            search_ads_360_link (google.analytics.admin_v1alpha.types.SearchAds360Link):
                A snapshot of a SearchAds360Link resource in
                change history.

                This field is a member of `oneof`_ ``resource``.
            data_stream (google.analytics.admin_v1alpha.types.DataStream):
                A snapshot of a DataStream resource in change
                history.

                This field is a member of `oneof`_ ``resource``.
            attribution_settings (google.analytics.admin_v1alpha.types.AttributionSettings):
                A snapshot of AttributionSettings resource in
                change history.

                This field is a member of `oneof`_ ``resource``.
            expanded_data_set (google.analytics.admin_v1alpha.types.ExpandedDataSet):
                A snapshot of an ExpandedDataSet resource in
                change history.

                This field is a member of `oneof`_ ``resource``.
            channel_group (google.analytics.admin_v1alpha.types.ChannelGroup):
                A snapshot of a ChannelGroup resource in
                change history.

                This field is a member of `oneof`_ ``resource``.
            bigquery_link (google.analytics.admin_v1alpha.types.BigQueryLink):
                A snapshot of a BigQuery link resource in
                change history.

                This field is a member of `oneof`_ ``resource``.
            enhanced_measurement_settings (google.analytics.admin_v1alpha.types.EnhancedMeasurementSettings):
                A snapshot of EnhancedMeasurementSettings
                resource in change history.

                This field is a member of `oneof`_ ``resource``.
            data_redaction_settings (google.analytics.admin_v1alpha.types.DataRedactionSettings):
                A snapshot of DataRedactionSettings resource
                in change history.

                This field is a member of `oneof`_ ``resource``.
            skadnetwork_conversion_value_schema (google.analytics.admin_v1alpha.types.SKAdNetworkConversionValueSchema):
                A snapshot of
                SKAdNetworkConversionValueSchema resource in
                change history.

                This field is a member of `oneof`_ ``resource``.
            adsense_link (google.analytics.admin_v1alpha.types.AdSenseLink):
                A snapshot of an AdSenseLink resource in
                change history.

                This field is a member of `oneof`_ ``resource``.
            audience (google.analytics.admin_v1alpha.types.Audience):
                A snapshot of an Audience resource in change
                history.

                This field is a member of `oneof`_ ``resource``.
            event_create_rule (google.analytics.admin_v1alpha.types.EventCreateRule):
                A snapshot of an EventCreateRule resource in
                change history.

                This field is a member of `oneof`_ ``resource``.
            key_event (google.analytics.admin_v1alpha.types.KeyEvent):
                A snapshot of a KeyEvent resource in change
                history.

                This field is a member of `oneof`_ ``resource``.
            calculated_metric (google.analytics.admin_v1alpha.types.CalculatedMetric):
                A snapshot of a CalculatedMetric resource in
                change history.

                This field is a member of `oneof`_ ``resource``.
            reporting_data_annotation (google.analytics.admin_v1alpha.types.ReportingDataAnnotation):
                A snapshot of a ReportingDataAnnotation
                resource in change history.

                This field is a member of `oneof`_ ``resource``.
            subproperty_sync_config (google.analytics.admin_v1alpha.types.SubpropertySyncConfig):
                A snapshot of a SubpropertySyncConfig
                resource in change history.

                This field is a member of `oneof`_ ``resource``.
            reporting_identity_settings (google.analytics.admin_v1alpha.types.ReportingIdentitySettings):
                A snapshot of a ReportingIdentitySettings
                resource in change history.

                This field is a member of `oneof`_ ``resource``.
            user_provided_data_settings (google.analytics.admin_v1alpha.types.UserProvidedDataSettings):
                A snapshot of a UserProvidedDataSettings
                resource in change history.

                This field is a member of `oneof`_ ``resource``.
        """

        account: "Account" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="resource",
            message="Account",
        )
        property: "Property" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="resource",
            message="Property",
        )
        firebase_link: "FirebaseLink" = proto.Field(
            proto.MESSAGE,
            number=6,
            oneof="resource",
            message="FirebaseLink",
        )
        google_ads_link: "GoogleAdsLink" = proto.Field(
            proto.MESSAGE,
            number=7,
            oneof="resource",
            message="GoogleAdsLink",
        )
        google_signals_settings: "GoogleSignalsSettings" = proto.Field(
            proto.MESSAGE,
            number=8,
            oneof="resource",
            message="GoogleSignalsSettings",
        )
        display_video_360_advertiser_link: "DisplayVideo360AdvertiserLink" = (
            proto.Field(
                proto.MESSAGE,
                number=9,
                oneof="resource",
                message="DisplayVideo360AdvertiserLink",
            )
        )
        display_video_360_advertiser_link_proposal: "DisplayVideo360AdvertiserLinkProposal" = proto.Field(
            proto.MESSAGE,
            number=10,
            oneof="resource",
            message="DisplayVideo360AdvertiserLinkProposal",
        )
        conversion_event: "ConversionEvent" = proto.Field(
            proto.MESSAGE,
            number=11,
            oneof="resource",
            message="ConversionEvent",
        )
        measurement_protocol_secret: "MeasurementProtocolSecret" = proto.Field(
            proto.MESSAGE,
            number=12,
            oneof="resource",
            message="MeasurementProtocolSecret",
        )
        custom_dimension: "CustomDimension" = proto.Field(
            proto.MESSAGE,
            number=13,
            oneof="resource",
            message="CustomDimension",
        )
        custom_metric: "CustomMetric" = proto.Field(
            proto.MESSAGE,
            number=14,
            oneof="resource",
            message="CustomMetric",
        )
        data_retention_settings: "DataRetentionSettings" = proto.Field(
            proto.MESSAGE,
            number=15,
            oneof="resource",
            message="DataRetentionSettings",
        )
        search_ads_360_link: "SearchAds360Link" = proto.Field(
            proto.MESSAGE,
            number=16,
            oneof="resource",
            message="SearchAds360Link",
        )
        data_stream: "DataStream" = proto.Field(
            proto.MESSAGE,
            number=18,
            oneof="resource",
            message="DataStream",
        )
        attribution_settings: "AttributionSettings" = proto.Field(
            proto.MESSAGE,
            number=20,
            oneof="resource",
            message="AttributionSettings",
        )
        expanded_data_set: gaa_expanded_data_set.ExpandedDataSet = proto.Field(
            proto.MESSAGE,
            number=21,
            oneof="resource",
            message=gaa_expanded_data_set.ExpandedDataSet,
        )
        channel_group: gaa_channel_group.ChannelGroup = proto.Field(
            proto.MESSAGE,
            number=22,
            oneof="resource",
            message=gaa_channel_group.ChannelGroup,
        )
        bigquery_link: "BigQueryLink" = proto.Field(
            proto.MESSAGE,
            number=23,
            oneof="resource",
            message="BigQueryLink",
        )
        enhanced_measurement_settings: "EnhancedMeasurementSettings" = proto.Field(
            proto.MESSAGE,
            number=24,
            oneof="resource",
            message="EnhancedMeasurementSettings",
        )
        data_redaction_settings: "DataRedactionSettings" = proto.Field(
            proto.MESSAGE,
            number=25,
            oneof="resource",
            message="DataRedactionSettings",
        )
        skadnetwork_conversion_value_schema: "SKAdNetworkConversionValueSchema" = (
            proto.Field(
                proto.MESSAGE,
                number=26,
                oneof="resource",
                message="SKAdNetworkConversionValueSchema",
            )
        )
        adsense_link: "AdSenseLink" = proto.Field(
            proto.MESSAGE,
            number=27,
            oneof="resource",
            message="AdSenseLink",
        )
        audience: gaa_audience.Audience = proto.Field(
            proto.MESSAGE,
            number=28,
            oneof="resource",
            message=gaa_audience.Audience,
        )
        event_create_rule: event_create_and_edit.EventCreateRule = proto.Field(
            proto.MESSAGE,
            number=29,
            oneof="resource",
            message=event_create_and_edit.EventCreateRule,
        )
        key_event: "KeyEvent" = proto.Field(
            proto.MESSAGE,
            number=30,
            oneof="resource",
            message="KeyEvent",
        )
        calculated_metric: "CalculatedMetric" = proto.Field(
            proto.MESSAGE,
            number=31,
            oneof="resource",
            message="CalculatedMetric",
        )
        reporting_data_annotation: "ReportingDataAnnotation" = proto.Field(
            proto.MESSAGE,
            number=32,
            oneof="resource",
            message="ReportingDataAnnotation",
        )
        subproperty_sync_config: "SubpropertySyncConfig" = proto.Field(
            proto.MESSAGE,
            number=33,
            oneof="resource",
            message="SubpropertySyncConfig",
        )
        reporting_identity_settings: "ReportingIdentitySettings" = proto.Field(
            proto.MESSAGE,
            number=34,
            oneof="resource",
            message="ReportingIdentitySettings",
        )
        user_provided_data_settings: "UserProvidedDataSettings" = proto.Field(
            proto.MESSAGE,
            number=35,
            oneof="resource",
            message="UserProvidedDataSettings",
        )

    resource: str = proto.Field(
        proto.STRING,
        number=1,
    )
    action: "ActionType" = proto.Field(
        proto.ENUM,
        number=2,
        enum="ActionType",
    )
    resource_before_change: ChangeHistoryResource = proto.Field(
        proto.MESSAGE,
        number=3,
        message=ChangeHistoryResource,
    )
    resource_after_change: ChangeHistoryResource = proto.Field(
        proto.MESSAGE,
        number=4,
        message=ChangeHistoryResource,
    )


class DisplayVideo360AdvertiserLink(proto.Message):
    r"""A link between a Google Analytics property and a Display &
    Video 360 advertiser.

    Attributes:
        name (str):
            Identifier. The resource name for this
            DisplayVideo360AdvertiserLink resource. Format:

            properties/{propertyId}/displayVideo360AdvertiserLinks/{linkId}

            Note: linkId is not the Display & Video 360
            Advertiser ID
        advertiser_id (str):
            Immutable. The Display & Video 360
            Advertiser's advertiser ID.
        advertiser_display_name (str):
            Output only. The display name of the Display
            & Video 360 Advertiser.
        ads_personalization_enabled (google.protobuf.wrappers_pb2.BoolValue):
            Enables personalized advertising features
            with this integration. If this field is not set
            on create/update, it will be defaulted to true.
        campaign_data_sharing_enabled (google.protobuf.wrappers_pb2.BoolValue):
            Immutable. Enables the import of campaign
            data from Display & Video 360 into the Google
            Analytics property. After link creation, this
            can only be updated from the Display & Video 360
            product. If this field is not set on create, it
            will be defaulted to true.
        cost_data_sharing_enabled (google.protobuf.wrappers_pb2.BoolValue):
            Immutable. Enables the import of cost data from Display &
            Video 360 into the Google Analytics property. This can only
            be enabled if ``campaign_data_sharing_enabled`` is true.
            After link creation, this can only be updated from the
            Display & Video 360 product. If this field is not set on
            create, it will be defaulted to true.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    advertiser_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    advertiser_display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    ads_personalization_enabled: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=4,
        message=wrappers_pb2.BoolValue,
    )
    campaign_data_sharing_enabled: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=5,
        message=wrappers_pb2.BoolValue,
    )
    cost_data_sharing_enabled: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=6,
        message=wrappers_pb2.BoolValue,
    )


class DisplayVideo360AdvertiserLinkProposal(proto.Message):
    r"""A proposal for a link between a Google Analytics property and
    a Display & Video 360 advertiser.

    A proposal is converted to a DisplayVideo360AdvertiserLink once
    approved. Google Analytics admins approve inbound proposals
    while Display & Video 360 admins approve outbound proposals.

    Attributes:
        name (str):
            Identifier. The resource name for this
            DisplayVideo360AdvertiserLinkProposal resource.
            Format:

            properties/{propertyId}/displayVideo360AdvertiserLinkProposals/{proposalId}

            Note: proposalId is not the Display & Video 360
            Advertiser ID
        advertiser_id (str):
            Immutable. The Display & Video 360
            Advertiser's advertiser ID.
        link_proposal_status_details (google.analytics.admin_v1alpha.types.LinkProposalStatusDetails):
            Output only. The status information for this
            link proposal.
        advertiser_display_name (str):
            Output only. The display name of the Display
            & Video Advertiser. Only populated for proposals
            that originated from Display & Video 360.
        validation_email (str):
            Input only. On a proposal being sent to
            Display & Video 360, this field must be set to
            the email address of an admin on the target
            advertiser. This is used to verify that the
            Google Analytics admin is aware of at least one
            admin on the Display & Video 360 Advertiser.
            This does not restrict approval of the proposal
            to a single user. Any admin on the Display &
            Video 360 Advertiser may approve the proposal.
        ads_personalization_enabled (google.protobuf.wrappers_pb2.BoolValue):
            Immutable. Enables personalized advertising
            features with this integration. If this field is
            not set on create, it will be defaulted to true.
        campaign_data_sharing_enabled (google.protobuf.wrappers_pb2.BoolValue):
            Immutable. Enables the import of campaign
            data from Display & Video 360. If this field is
            not set on create, it will be defaulted to true.
        cost_data_sharing_enabled (google.protobuf.wrappers_pb2.BoolValue):
            Immutable. Enables the import of cost data from Display &
            Video 360. This can only be enabled if
            campaign_data_sharing_enabled is enabled. If this field is
            not set on create, it will be defaulted to true.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    advertiser_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    link_proposal_status_details: "LinkProposalStatusDetails" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="LinkProposalStatusDetails",
    )
    advertiser_display_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    validation_email: str = proto.Field(
        proto.STRING,
        number=5,
    )
    ads_personalization_enabled: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=6,
        message=wrappers_pb2.BoolValue,
    )
    campaign_data_sharing_enabled: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=7,
        message=wrappers_pb2.BoolValue,
    )
    cost_data_sharing_enabled: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=8,
        message=wrappers_pb2.BoolValue,
    )


class SearchAds360Link(proto.Message):
    r"""A link between a Google Analytics property and a Search Ads
    360 entity.

    Attributes:
        name (str):
            Identifier. The resource name for this
            SearchAds360Link resource. Format:
            properties/{propertyId}/searchAds360Links/{linkId}

            Note: linkId is not the Search Ads 360
            advertiser ID
        advertiser_id (str):
            Immutable. This field represents the
            Advertiser ID of the Search Ads 360 Advertiser.
            that has been linked.
        campaign_data_sharing_enabled (google.protobuf.wrappers_pb2.BoolValue):
            Immutable. Enables the import of campaign
            data from Search Ads 360 into the Google
            Analytics property. After link creation, this
            can only be updated from the Search Ads 360
            product. If this field is not set on create, it
            will be defaulted to true.
        cost_data_sharing_enabled (google.protobuf.wrappers_pb2.BoolValue):
            Immutable. Enables the import of cost data from Search Ads
            360 to the Google Analytics property. This can only be
            enabled if campaign_data_sharing_enabled is enabled. After
            link creation, this can only be updated from the Search Ads
            360 product. If this field is not set on create, it will be
            defaulted to true.
        advertiser_display_name (str):
            Output only. The display name of the Search
            Ads 360 Advertiser. Allows users to easily
            identify the linked resource.
        ads_personalization_enabled (google.protobuf.wrappers_pb2.BoolValue):
            Enables personalized advertising features
            with this integration. If this field is not set
            on create, it will be defaulted to true.
        site_stats_sharing_enabled (google.protobuf.wrappers_pb2.BoolValue):
            Enables export of site stats with this
            integration. If this field is not set on create,
            it will be defaulted to true.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    advertiser_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    campaign_data_sharing_enabled: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=3,
        message=wrappers_pb2.BoolValue,
    )
    cost_data_sharing_enabled: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=4,
        message=wrappers_pb2.BoolValue,
    )
    advertiser_display_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    ads_personalization_enabled: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=6,
        message=wrappers_pb2.BoolValue,
    )
    site_stats_sharing_enabled: wrappers_pb2.BoolValue = proto.Field(
        proto.MESSAGE,
        number=7,
        message=wrappers_pb2.BoolValue,
    )


class LinkProposalStatusDetails(proto.Message):
    r"""Status information for a link proposal.

    Attributes:
        link_proposal_initiating_product (google.analytics.admin_v1alpha.types.LinkProposalInitiatingProduct):
            Output only. The source of this proposal.
        requestor_email (str):
            Output only. The email address of the user
            that proposed this linkage.
        link_proposal_state (google.analytics.admin_v1alpha.types.LinkProposalState):
            Output only. The state of this proposal.
    """

    link_proposal_initiating_product: "LinkProposalInitiatingProduct" = proto.Field(
        proto.ENUM,
        number=1,
        enum="LinkProposalInitiatingProduct",
    )
    requestor_email: str = proto.Field(
        proto.STRING,
        number=2,
    )
    link_proposal_state: "LinkProposalState" = proto.Field(
        proto.ENUM,
        number=3,
        enum="LinkProposalState",
    )


class ConversionEvent(proto.Message):
    r"""A conversion event in a Google Analytics property.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. Resource name of this conversion event. Format:
            properties/{property}/conversionEvents/{conversion_event}
        event_name (str):
            Immutable. The event name for this conversion
            event. Examples: 'click', 'purchase'
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when this conversion event
            was created in the property.
        deletable (bool):
            Output only. If set, this event can currently
            be deleted with DeleteConversionEvent.
        custom (bool):
            Output only. If set to true, this conversion
            event refers to a custom event.  If set to
            false, this conversion event refers to a default
            event in GA. Default events typically have
            special meaning in GA. Default events are
            usually created for you by the GA system, but in
            some cases can be created by property admins.
            Custom events count towards the maximum number
            of custom conversion events that may be created
            per property.
        counting_method (google.analytics.admin_v1alpha.types.ConversionEvent.ConversionCountingMethod):
            Optional. The method by which conversions will be counted
            across multiple events within a session. If this value is
            not provided, it will be set to ``ONCE_PER_EVENT``.
        default_conversion_value (google.analytics.admin_v1alpha.types.ConversionEvent.DefaultConversionValue):
            Optional. Defines a default value/currency
            for a conversion event.

            This field is a member of `oneof`_ ``_default_conversion_value``.
    """

    class ConversionCountingMethod(proto.Enum):
        r"""The method by which conversions will be counted across
        multiple events within a session.

        Values:
            CONVERSION_COUNTING_METHOD_UNSPECIFIED (0):
                Counting method not specified.
            ONCE_PER_EVENT (1):
                Each Event instance is considered a
                Conversion.
            ONCE_PER_SESSION (2):
                An Event instance is considered a Conversion
                at most once per session per user.
        """

        CONVERSION_COUNTING_METHOD_UNSPECIFIED = 0
        ONCE_PER_EVENT = 1
        ONCE_PER_SESSION = 2

    class DefaultConversionValue(proto.Message):
        r"""Defines a default value/currency for a conversion event. Both
        value and currency must be provided.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            value (float):
                This value will be used to populate the value for all
                conversions of the specified event_name where the event
                "value" parameter is unset.

                This field is a member of `oneof`_ ``_value``.
            currency_code (str):
                When a conversion event for this event_name has no set
                currency, this currency will be applied as the default. Must
                be in ISO 4217 currency code format. See
                https://en.wikipedia.org/wiki/ISO_4217 for more information.

                This field is a member of `oneof`_ ``_currency_code``.
        """

        value: float = proto.Field(
            proto.DOUBLE,
            number=1,
            optional=True,
        )
        currency_code: str = proto.Field(
            proto.STRING,
            number=2,
            optional=True,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    event_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    deletable: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    custom: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    counting_method: ConversionCountingMethod = proto.Field(
        proto.ENUM,
        number=6,
        enum=ConversionCountingMethod,
    )
    default_conversion_value: DefaultConversionValue = proto.Field(
        proto.MESSAGE,
        number=7,
        optional=True,
        message=DefaultConversionValue,
    )


class KeyEvent(proto.Message):
    r"""A key event in a Google Analytics property.

    Attributes:
        name (str):
            Output only. Resource name of this key event. Format:
            properties/{property}/keyEvents/{key_event}
        event_name (str):
            Immutable. The event name for this key event.
            Examples: 'click', 'purchase'
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when this key event was
            created in the property.
        deletable (bool):
            Output only. If set to true, this event can
            be deleted.
        custom (bool):
            Output only. If set to true, this key event
            refers to a custom event.  If set to false, this
            key event refers to a default event in GA.
            Default events typically have special meaning in
            GA. Default events are usually created for you
            by the GA system, but in some cases can be
            created by property admins. Custom events count
            towards the maximum number of custom key events
            that may be created per property.
        counting_method (google.analytics.admin_v1alpha.types.KeyEvent.CountingMethod):
            Required. The method by which Key Events will
            be counted across multiple events within a
            session.
        default_value (google.analytics.admin_v1alpha.types.KeyEvent.DefaultValue):
            Optional. Defines a default value/currency
            for a key event.
    """

    class CountingMethod(proto.Enum):
        r"""The method by which Key Events will be counted across
        multiple events within a session.

        Values:
            COUNTING_METHOD_UNSPECIFIED (0):
                Counting method not specified.
            ONCE_PER_EVENT (1):
                Each Event instance is considered a Key
                Event.
            ONCE_PER_SESSION (2):
                An Event instance is considered a Key Event
                at most once per session per user.
        """

        COUNTING_METHOD_UNSPECIFIED = 0
        ONCE_PER_EVENT = 1
        ONCE_PER_SESSION = 2

    class DefaultValue(proto.Message):
        r"""Defines a default value/currency for a key event.

        Attributes:
            numeric_value (float):
                Required. This will be used to populate the "value"
                parameter for all occurrences of this Key Event (specified
                by event_name) where that parameter is unset.
            currency_code (str):
                Required. When an occurrence of this Key Event (specified by
                event_name) has no set currency this currency will be
                applied as the default. Must be in ISO 4217 currency code
                format.

                See https://en.wikipedia.org/wiki/ISO_4217 for more
                information.
        """

        numeric_value: float = proto.Field(
            proto.DOUBLE,
            number=1,
        )
        currency_code: str = proto.Field(
            proto.STRING,
            number=2,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    event_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    deletable: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    custom: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    counting_method: CountingMethod = proto.Field(
        proto.ENUM,
        number=6,
        enum=CountingMethod,
    )
    default_value: DefaultValue = proto.Field(
        proto.MESSAGE,
        number=7,
        message=DefaultValue,
    )


class GoogleSignalsSettings(proto.Message):
    r"""Settings values for Google Signals.  This is a singleton
    resource.

    Attributes:
        name (str):
            Output only. Resource name of this setting. Format:
            properties/{property_id}/googleSignalsSettings Example:
            "properties/1000/googleSignalsSettings".
        state (google.analytics.admin_v1alpha.types.GoogleSignalsState):
            Status of this setting.
        consent (google.analytics.admin_v1alpha.types.GoogleSignalsConsent):
            Output only. Terms of Service acceptance.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    state: "GoogleSignalsState" = proto.Field(
        proto.ENUM,
        number=3,
        enum="GoogleSignalsState",
    )
    consent: "GoogleSignalsConsent" = proto.Field(
        proto.ENUM,
        number=4,
        enum="GoogleSignalsConsent",
    )


class CustomDimension(proto.Message):
    r"""A definition for a CustomDimension.

    Attributes:
        name (str):
            Identifier. Resource name for this
            CustomDimension resource. Format:
            properties/{property}/customDimensions/{customDimension}
        parameter_name (str):
            Required. Immutable. Tagging parameter name
            for this custom dimension.
            If this is a user-scoped dimension, then this is
            the user property name. If this is an
            event-scoped dimension, then this is the event
            parameter name.

            If this is an item-scoped dimension, then this
            is the parameter name found in the eCommerce
            items array.

            May only contain alphanumeric and underscore
            characters, starting with a letter. Max length
            of 24 characters for user-scoped dimensions, 40
            characters for event-scoped dimensions.
        display_name (str):
            Required. Display name for this custom
            dimension as shown in the Analytics UI. Max
            length of 82 characters, alphanumeric plus space
            and underscore starting with a letter. Legacy
            system-generated display names may contain
            square brackets, but updates to this field will
            never permit square brackets.
        description (str):
            Optional. Description for this custom
            dimension. Max length of 150 characters.
        scope (google.analytics.admin_v1alpha.types.CustomDimension.DimensionScope):
            Required. Immutable. The scope of this
            dimension.
        disallow_ads_personalization (bool):
            Optional. If set to true, sets this dimension
            as NPA and excludes it from ads personalization.

            This is currently only supported by user-scoped
            custom dimensions.
    """

    class DimensionScope(proto.Enum):
        r"""Valid values for the scope of this dimension.

        Values:
            DIMENSION_SCOPE_UNSPECIFIED (0):
                Scope unknown or not specified.
            EVENT (1):
                Dimension scoped to an event.
            USER (2):
                Dimension scoped to a user.
            ITEM (3):
                Dimension scoped to eCommerce items
        """

        DIMENSION_SCOPE_UNSPECIFIED = 0
        EVENT = 1
        USER = 2
        ITEM = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    parameter_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    scope: DimensionScope = proto.Field(
        proto.ENUM,
        number=5,
        enum=DimensionScope,
    )
    disallow_ads_personalization: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class CustomMetric(proto.Message):
    r"""A definition for a custom metric.

    Attributes:
        name (str):
            Identifier. Resource name for this
            CustomMetric resource. Format:
            properties/{property}/customMetrics/{customMetric}
        parameter_name (str):
            Required. Immutable. Tagging name for this
            custom metric.
            If this is an event-scoped metric, then this is
            the event parameter name.

            May only contain alphanumeric and underscore
            charactes, starting with a letter. Max length of
            40 characters for event-scoped metrics.
        display_name (str):
            Required. Display name for this custom metric
            as shown in the Analytics UI. Max length of 82
            characters, alphanumeric plus space and
            underscore starting with a letter. Legacy
            system-generated display names may contain
            square brackets, but updates to this field will
            never permit square brackets.
        description (str):
            Optional. Description for this custom
            dimension. Max length of 150 characters.
        measurement_unit (google.analytics.admin_v1alpha.types.CustomMetric.MeasurementUnit):
            Required. The type for the custom metric's
            value.
        scope (google.analytics.admin_v1alpha.types.CustomMetric.MetricScope):
            Required. Immutable. The scope of this custom
            metric.
        restricted_metric_type (MutableSequence[google.analytics.admin_v1alpha.types.CustomMetric.RestrictedMetricType]):
            Optional. Types of restricted data that this
            metric may contain. Required for metrics with
            CURRENCY measurement unit. Must be empty for
            metrics with a non-CURRENCY measurement unit.
    """

    class MeasurementUnit(proto.Enum):
        r"""Possible types of representing the custom metric's value.

        Currency representation may change in the future, requiring a
        breaking API change.

        Values:
            MEASUREMENT_UNIT_UNSPECIFIED (0):
                MeasurementUnit unspecified or missing.
            STANDARD (1):
                This metric uses default units.
            CURRENCY (2):
                This metric measures a currency.
            FEET (3):
                This metric measures feet.
            METERS (4):
                This metric measures meters.
            KILOMETERS (5):
                This metric measures kilometers.
            MILES (6):
                This metric measures miles.
            MILLISECONDS (7):
                This metric measures milliseconds.
            SECONDS (8):
                This metric measures seconds.
            MINUTES (9):
                This metric measures minutes.
            HOURS (10):
                This metric measures hours.
        """

        MEASUREMENT_UNIT_UNSPECIFIED = 0
        STANDARD = 1
        CURRENCY = 2
        FEET = 3
        METERS = 4
        KILOMETERS = 5
        MILES = 6
        MILLISECONDS = 7
        SECONDS = 8
        MINUTES = 9
        HOURS = 10

    class MetricScope(proto.Enum):
        r"""The scope of this metric.

        Values:
            METRIC_SCOPE_UNSPECIFIED (0):
                Scope unknown or not specified.
            EVENT (1):
                Metric scoped to an event.
        """

        METRIC_SCOPE_UNSPECIFIED = 0
        EVENT = 1

    class RestrictedMetricType(proto.Enum):
        r"""Labels that mark the data in this custom metric as data that
        should be restricted to specific users.

        Values:
            RESTRICTED_METRIC_TYPE_UNSPECIFIED (0):
                Type unknown or unspecified.
            COST_DATA (1):
                Metric reports cost data.
            REVENUE_DATA (2):
                Metric reports revenue data.
        """

        RESTRICTED_METRIC_TYPE_UNSPECIFIED = 0
        COST_DATA = 1
        REVENUE_DATA = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    parameter_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    measurement_unit: MeasurementUnit = proto.Field(
        proto.ENUM,
        number=5,
        enum=MeasurementUnit,
    )
    scope: MetricScope = proto.Field(
        proto.ENUM,
        number=6,
        enum=MetricScope,
    )
    restricted_metric_type: MutableSequence[RestrictedMetricType] = proto.RepeatedField(
        proto.ENUM,
        number=8,
        enum=RestrictedMetricType,
    )


class CalculatedMetric(proto.Message):
    r"""A definition for a calculated metric.

    Attributes:
        name (str):
            Identifier. Resource name for this CalculatedMetric. Format:
            'properties/{property_id}/calculatedMetrics/{calculated_metric_id}'
        description (str):
            Optional. Description for this calculated
            metric. Max length of 4096 characters.
        display_name (str):
            Required. Display name for this calculated
            metric as shown in the Google Analytics UI. Max
            length 82 characters.
        calculated_metric_id (str):
            Output only. The ID to use for the calculated metric. In the
            UI, this is referred to as the "API name."

            The calculated_metric_id is used when referencing this
            calculated metric from external APIs. For example,
            "calcMetric:{calculated_metric_id}".
        metric_unit (google.analytics.admin_v1alpha.types.CalculatedMetric.MetricUnit):
            Required. The type for the calculated
            metric's value.
        restricted_metric_type (MutableSequence[google.analytics.admin_v1alpha.types.CalculatedMetric.RestrictedMetricType]):
            Output only. Types of restricted data that
            this metric contains.
        formula (str):
            Required. The calculated metric's definition. Maximum number
            of unique referenced custom metrics is 5. Formulas supports
            the following operations:

            - (addition), - (subtraction), - (negative), \*
              (multiplication), / (division), () (parenthesis). Any
              valid real numbers are acceptable that fit in a Long
              (64bit integer) or a Double (64 bit floating point
              number). Example formula: "( customEvent:parameter_name +
              cartPurchaseQuantity ) / 2.0".
        invalid_metric_reference (bool):
            Output only. If true, this calculated metric has a invalid
            metric reference. Anything using a calculated metric with
            invalid_metric_reference set to true may fail, produce
            warnings, or produce unexpected results.
    """

    class MetricUnit(proto.Enum):
        r"""Possible types of representing the calculated metric's value.

        Values:
            METRIC_UNIT_UNSPECIFIED (0):
                MetricUnit unspecified or missing.
            STANDARD (1):
                This metric uses default units.
            CURRENCY (2):
                This metric measures a currency.
            FEET (3):
                This metric measures feet.
            MILES (4):
                This metric measures miles.
            METERS (5):
                This metric measures meters.
            KILOMETERS (6):
                This metric measures kilometers.
            MILLISECONDS (7):
                This metric measures milliseconds.
            SECONDS (8):
                This metric measures seconds.
            MINUTES (9):
                This metric measures minutes.
            HOURS (10):
                This metric measures hours.
        """

        METRIC_UNIT_UNSPECIFIED = 0
        STANDARD = 1
        CURRENCY = 2
        FEET = 3
        MILES = 4
        METERS = 5
        KILOMETERS = 6
        MILLISECONDS = 7
        SECONDS = 8
        MINUTES = 9
        HOURS = 10

    class RestrictedMetricType(proto.Enum):
        r"""Labels that mark the data in calculated metric used in
        conjunction with user roles that restrict access to cost and/or
        revenue metrics.

        Values:
            RESTRICTED_METRIC_TYPE_UNSPECIFIED (0):
                Type unknown or unspecified.
            COST_DATA (1):
                Metric reports cost data.
            REVENUE_DATA (2):
                Metric reports revenue data.
        """

        RESTRICTED_METRIC_TYPE_UNSPECIFIED = 0
        COST_DATA = 1
        REVENUE_DATA = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    calculated_metric_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    metric_unit: MetricUnit = proto.Field(
        proto.ENUM,
        number=5,
        enum=MetricUnit,
    )
    restricted_metric_type: MutableSequence[RestrictedMetricType] = proto.RepeatedField(
        proto.ENUM,
        number=6,
        enum=RestrictedMetricType,
    )
    formula: str = proto.Field(
        proto.STRING,
        number=7,
    )
    invalid_metric_reference: bool = proto.Field(
        proto.BOOL,
        number=9,
    )


class DataRetentionSettings(proto.Message):
    r"""Settings values for data retention. This is a singleton
    resource.

    Attributes:
        name (str):
            Identifier. Resource name for this
            DataRetentionSetting resource. Format:
            properties/{property}/dataRetentionSettings
        event_data_retention (google.analytics.admin_v1alpha.types.DataRetentionSettings.RetentionDuration):
            Required. The length of time that event-level
            data is retained.
        user_data_retention (google.analytics.admin_v1alpha.types.DataRetentionSettings.RetentionDuration):
            Required. The length of time that user-level
            data is retained.
        reset_user_data_on_new_activity (bool):
            If true, reset the retention period for the
            user identifier with every event from that user.
    """

    class RetentionDuration(proto.Enum):
        r"""Valid values for the data retention duration.

        Values:
            RETENTION_DURATION_UNSPECIFIED (0):
                Data retention time duration is not
                specified.
            TWO_MONTHS (1):
                The data retention time duration is 2 months.
            FOURTEEN_MONTHS (3):
                The data retention time duration is 14
                months.
            TWENTY_SIX_MONTHS (4):
                The data retention time duration is 26
                months. Available to 360 properties only.
                Available for event data only.
            THIRTY_EIGHT_MONTHS (5):
                The data retention time duration is 38
                months. Available to 360 properties only.
                Available for event data only.
            FIFTY_MONTHS (6):
                The data retention time duration is 50
                months. Available to 360 properties only.
                Available for event data only.
        """

        RETENTION_DURATION_UNSPECIFIED = 0
        TWO_MONTHS = 1
        FOURTEEN_MONTHS = 3
        TWENTY_SIX_MONTHS = 4
        THIRTY_EIGHT_MONTHS = 5
        FIFTY_MONTHS = 6

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    event_data_retention: RetentionDuration = proto.Field(
        proto.ENUM,
        number=2,
        enum=RetentionDuration,
    )
    user_data_retention: RetentionDuration = proto.Field(
        proto.ENUM,
        number=4,
        enum=RetentionDuration,
    )
    reset_user_data_on_new_activity: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class AttributionSettings(proto.Message):
    r"""The attribution settings used for a given property. This is a
    singleton resource.

    Attributes:
        name (str):
            Output only. Resource name of this attribution settings
            resource. Format:
            properties/{property_id}/attributionSettings Example:
            "properties/1000/attributionSettings".
        acquisition_conversion_event_lookback_window (google.analytics.admin_v1alpha.types.AttributionSettings.AcquisitionConversionEventLookbackWindow):
            Required. The lookback window configuration
            for acquisition conversion events. The default
            window size is 30 days.
        other_conversion_event_lookback_window (google.analytics.admin_v1alpha.types.AttributionSettings.OtherConversionEventLookbackWindow):
            Required. The lookback window for all other,
            non-acquisition conversion events. The default
            window size is 90 days.
        reporting_attribution_model (google.analytics.admin_v1alpha.types.AttributionSettings.ReportingAttributionModel):
            Required. The reporting attribution model
            used to calculate conversion credit in this
            property's reports.

            Changing the attribution model will apply to
            both historical and future data. These changes
            will be reflected in reports with conversion and
            revenue data. User and session data will be
            unaffected.
        ads_web_conversion_data_export_scope (google.analytics.admin_v1alpha.types.AttributionSettings.AdsWebConversionDataExportScope):
            Required. The Conversion Export Scope for
            data exported to linked Ads Accounts.
    """

    class AcquisitionConversionEventLookbackWindow(proto.Enum):
        r"""How far back in time events should be considered for
        inclusion in a converting path which leads to the first install
        of an app or the first visit to a site.

        Values:
            ACQUISITION_CONVERSION_EVENT_LOOKBACK_WINDOW_UNSPECIFIED (0):
                Lookback window size unspecified.
            ACQUISITION_CONVERSION_EVENT_LOOKBACK_WINDOW_7_DAYS (1):
                7-day lookback window.
            ACQUISITION_CONVERSION_EVENT_LOOKBACK_WINDOW_30_DAYS (2):
                30-day lookback window.
        """

        ACQUISITION_CONVERSION_EVENT_LOOKBACK_WINDOW_UNSPECIFIED = 0
        ACQUISITION_CONVERSION_EVENT_LOOKBACK_WINDOW_7_DAYS = 1
        ACQUISITION_CONVERSION_EVENT_LOOKBACK_WINDOW_30_DAYS = 2

    class OtherConversionEventLookbackWindow(proto.Enum):
        r"""How far back in time events should be considered for
        inclusion in a converting path for all conversions other than
        first app install/first site visit.

        Values:
            OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_UNSPECIFIED (0):
                Lookback window size unspecified.
            OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_30_DAYS (1):
                30-day lookback window.
            OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_60_DAYS (2):
                60-day lookback window.
            OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_90_DAYS (3):
                90-day lookback window.
        """

        OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_UNSPECIFIED = 0
        OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_30_DAYS = 1
        OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_60_DAYS = 2
        OTHER_CONVERSION_EVENT_LOOKBACK_WINDOW_90_DAYS = 3

    class ReportingAttributionModel(proto.Enum):
        r"""The reporting attribution model used to calculate conversion
        credit in this property's reports.

        Values:
            REPORTING_ATTRIBUTION_MODEL_UNSPECIFIED (0):
                Reporting attribution model unspecified.
            PAID_AND_ORGANIC_CHANNELS_DATA_DRIVEN (1):
                Data-driven attribution distributes credit for the
                conversion based on data for each conversion event. Each
                Data-driven model is specific to each advertiser and each
                conversion event. Previously CROSS_CHANNEL_DATA_DRIVEN
            PAID_AND_ORGANIC_CHANNELS_LAST_CLICK (2):
                Ignores direct traffic and attributes 100% of the conversion
                value to the last channel that the customer clicked through
                (or engaged view through for YouTube) before converting.
                Previously CROSS_CHANNEL_LAST_CLICK
            GOOGLE_PAID_CHANNELS_LAST_CLICK (7):
                Attributes 100% of the conversion value to the last Google
                Paid channel that the customer clicked through before
                converting. Previously ADS_PREFERRED_LAST_CLICK
        """

        REPORTING_ATTRIBUTION_MODEL_UNSPECIFIED = 0
        PAID_AND_ORGANIC_CHANNELS_DATA_DRIVEN = 1
        PAID_AND_ORGANIC_CHANNELS_LAST_CLICK = 2
        GOOGLE_PAID_CHANNELS_LAST_CLICK = 7

    class AdsWebConversionDataExportScope(proto.Enum):
        r"""The Conversion Export Scope for data exported to linked Ads
        Accounts.

        Values:
            ADS_WEB_CONVERSION_DATA_EXPORT_SCOPE_UNSPECIFIED (0):
                Default value. This value is unused.
            NOT_SELECTED_YET (1):
                No data export scope selected yet.
                Export scope can never be changed back to this
                value.
            PAID_AND_ORGANIC_CHANNELS (2):
                Paid and organic channels are eligible to receive conversion
                credit, but only credit assigned to Google Ads channels will
                appear in your Ads accounts. To learn more, see `Paid and
                Organic
                channels <https://support.google.com/analytics/answer/10632359>`__.
            GOOGLE_PAID_CHANNELS (3):
                Only Google Ads paid channels are eligible to receive
                conversion credit. To learn more, see `Google Paid
                channels <https://support.google.com/analytics/answer/10632359>`__.
        """

        ADS_WEB_CONVERSION_DATA_EXPORT_SCOPE_UNSPECIFIED = 0
        NOT_SELECTED_YET = 1
        PAID_AND_ORGANIC_CHANNELS = 2
        GOOGLE_PAID_CHANNELS = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    acquisition_conversion_event_lookback_window: AcquisitionConversionEventLookbackWindow = proto.Field(
        proto.ENUM,
        number=2,
        enum=AcquisitionConversionEventLookbackWindow,
    )
    other_conversion_event_lookback_window: OtherConversionEventLookbackWindow = (
        proto.Field(
            proto.ENUM,
            number=3,
            enum=OtherConversionEventLookbackWindow,
        )
    )
    reporting_attribution_model: ReportingAttributionModel = proto.Field(
        proto.ENUM,
        number=4,
        enum=ReportingAttributionModel,
    )
    ads_web_conversion_data_export_scope: AdsWebConversionDataExportScope = proto.Field(
        proto.ENUM,
        number=5,
        enum=AdsWebConversionDataExportScope,
    )


class AccessBinding(proto.Message):
    r"""A binding of a user to a set of roles.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        user (str):
            If set, the email address of the user to set
            roles for. Format: "someuser@gmail.com".

            This field is a member of `oneof`_ ``access_target``.
        name (str):
            Output only. Resource name of this binding.

            Format: accounts/{account}/accessBindings/{access_binding}
            or properties/{property}/accessBindings/{access_binding}

            Example: "accounts/100/accessBindings/200".
        roles (MutableSequence[str]):
            A list of roles for to grant to the parent
            resource.
            Valid values:

            predefinedRoles/viewer
            predefinedRoles/analyst
            predefinedRoles/editor
            predefinedRoles/admin
            predefinedRoles/no-cost-data
            predefinedRoles/no-revenue-data

            For users, if an empty list of roles is set,
            this AccessBinding will be deleted.
    """

    user: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="access_target",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    roles: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class BigQueryLink(proto.Message):
    r"""A link between a Google Analytics property and BigQuery
    project.

    Attributes:
        name (str):
            Output only. Resource name of this BigQuery link. Format:
            'properties/{property_id}/bigQueryLinks/{bigquery_link_id}'
            Format: 'properties/1234/bigQueryLinks/abc567'
        project (str):
            Immutable. The linked Google Cloud project.
            When creating a BigQueryLink, you may provide
            this resource name using either a project number
            or project ID. Once this resource has been
            created, the returned project will always have a
            project that contains a project number. Format:
            'projects/{project number}'
            Example: 'projects/1234'
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the link was created.
        daily_export_enabled (bool):
            If set true, enables daily data export to the
            linked Google Cloud project.
        streaming_export_enabled (bool):
            If set true, enables streaming export to the
            linked Google Cloud project.
        fresh_daily_export_enabled (bool):
            If set true, enables fresh daily export to
            the linked Google Cloud project.
        include_advertising_id (bool):
            If set true, exported data will include
            advertising identifiers for mobile app streams.
        export_streams (MutableSequence[str]):
            The list of streams under the parent property for which data
            will be exported. Format:
            properties/{property_id}/dataStreams/{stream_id} Example:
            ['properties/1000/dataStreams/2000']
        excluded_events (MutableSequence[str]):
            The list of event names that will be excluded
            from exports.
        dataset_location (str):
            Required. Immutable. The geographic location
            where the created BigQuery dataset should
            reside. See
            https://cloud.google.com/bigquery/docs/locations
            for supported locations.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    daily_export_enabled: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    streaming_export_enabled: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    fresh_daily_export_enabled: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    include_advertising_id: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    export_streams: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    excluded_events: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    dataset_location: str = proto.Field(
        proto.STRING,
        number=10,
    )


class EnhancedMeasurementSettings(proto.Message):
    r"""Singleton resource under a web DataStream, configuring
    measurement of additional site interactions and content.

    Attributes:
        name (str):
            Output only. Resource name of the Enhanced Measurement
            Settings. Format:
            properties/{property_id}/dataStreams/{data_stream}/enhancedMeasurementSettings
            Example:
            "properties/1000/dataStreams/2000/enhancedMeasurementSettings".
        stream_enabled (bool):
            Indicates whether Enhanced Measurement
            Settings will be used to automatically measure
            interactions and content on this web stream.

            Changing this value does not affect the settings
            themselves, but determines whether they are
            respected.
        scrolls_enabled (bool):
            If enabled, capture scroll events each time a
            visitor gets to the bottom of a page.
        outbound_clicks_enabled (bool):
            If enabled, capture an outbound click event
            each time a visitor clicks a link that leads
            them away from your domain.
        site_search_enabled (bool):
            If enabled, capture a view search results
            event each time a visitor performs a search on
            your site (based on a query parameter).
        video_engagement_enabled (bool):
            If enabled, capture video play, progress, and
            complete events as visitors view embedded videos
            on your site.
        file_downloads_enabled (bool):
            If enabled, capture a file download event
            each time a link is clicked with a common
            document, compressed file, application, video,
            or audio extension.
        page_changes_enabled (bool):
            If enabled, capture a page view event each
            time the website changes the browser history
            state.
        form_interactions_enabled (bool):
            If enabled, capture a form interaction event
            each time a visitor interacts with a form on
            your website. False by default.
        search_query_parameter (str):
            Required. URL query parameters to interpret
            as site search parameters. Max length is 1024
            characters. Must not be empty.
        uri_query_parameter (str):
            Additional URL query parameters.
            Max length is 1024 characters.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    stream_enabled: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    scrolls_enabled: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    outbound_clicks_enabled: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    site_search_enabled: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    video_engagement_enabled: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    file_downloads_enabled: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    page_changes_enabled: bool = proto.Field(
        proto.BOOL,
        number=8,
    )
    form_interactions_enabled: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    search_query_parameter: str = proto.Field(
        proto.STRING,
        number=10,
    )
    uri_query_parameter: str = proto.Field(
        proto.STRING,
        number=11,
    )


class DataRedactionSettings(proto.Message):
    r"""Settings for client-side data redaction. Singleton resource
    under a Web Stream.

    Attributes:
        name (str):
            Output only. Name of this Data Redaction Settings resource.
            Format:
            properties/{property_id}/dataStreams/{data_stream}/dataRedactionSettings
            Example:
            "properties/1000/dataStreams/2000/dataRedactionSettings".
        email_redaction_enabled (bool):
            If enabled, any event parameter or user
            property values that look like an email will be
            redacted.
        query_parameter_redaction_enabled (bool):
            Query Parameter redaction removes the key and value portions
            of a query parameter if it is in the configured set of query
            parameters.

            If enabled, URL query replacement logic will be run for the
            Stream. Any query parameters defined in query_parameter_keys
            will be redacted.
        query_parameter_keys (MutableSequence[str]):
            The query parameter keys to apply redaction logic to if
            present in the URL. Query parameter matching is
            case-insensitive.

            Must contain at least one element if
            query_parameter_replacement_enabled is true. Keys cannot
            contain commas.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    email_redaction_enabled: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    query_parameter_redaction_enabled: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    query_parameter_keys: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


class AdSenseLink(proto.Message):
    r"""A link between a Google Analytics property and an AdSense for
    Content ad client.

    Attributes:
        name (str):
            Output only. The resource name for this
            AdSense Link resource. Format:
            properties/{propertyId}/adSenseLinks/{linkId}
            Example: properties/1234/adSenseLinks/6789
        ad_client_code (str):
            Immutable. The AdSense ad client code that
            the Google Analytics property is linked to.
            Example format: "ca-pub-1234567890".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ad_client_code: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RollupPropertySourceLink(proto.Message):
    r"""A link that references a source property under the parent
    rollup property.

    Attributes:
        name (str):
            Output only. Resource name of this RollupPropertySourceLink.
            Format:
            'properties/{property_id}/rollupPropertySourceLinks/{rollup_property_source_link}'
            Format: 'properties/123/rollupPropertySourceLinks/456'
        source_property (str):
            Immutable. Resource name of the source property. Format:
            properties/{property_id} Example: "properties/789".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source_property: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ReportingDataAnnotation(proto.Message):
    r"""A Reporting Data Annotation is a comment connected to certain
    dates for reporting data.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        annotation_date (google.type.date_pb2.Date):
            If set, the Reporting Data Annotation is for
            a specific date represented by this field. The
            date must be a valid date with year, month and
            day set. The date may be in the past, present,
            or future.

            This field is a member of `oneof`_ ``target``.
        annotation_date_range (google.analytics.admin_v1alpha.types.ReportingDataAnnotation.DateRange):
            If set, the Reporting Data Annotation is for
            a range of dates represented by this field.

            This field is a member of `oneof`_ ``target``.
        name (str):
            Required. Identifier. Resource name of this Reporting Data
            Annotation. Format:
            'properties/{property_id}/reportingDataAnnotations/{reporting_data_annotation}'
            Format: 'properties/123/reportingDataAnnotations/456'
        title (str):
            Required. Human-readable title for this
            Reporting Data Annotation.
        description (str):
            Optional. Description for this Reporting Data
            Annotation.
        color (google.analytics.admin_v1alpha.types.ReportingDataAnnotation.Color):
            Required. The color used for display of this
            Reporting Data Annotation.
        system_generated (bool):
            Output only. If true, this annotation was
            generated by the Google Analytics system.
            System-generated annotations cannot be updated
            or deleted.
    """

    class Color(proto.Enum):
        r"""Colors that may be used for this Reporting Data Annotation

        Values:
            COLOR_UNSPECIFIED (0):
                Color unknown or not specified.
            PURPLE (1):
                Purple color.
            BROWN (2):
                Brown color.
            BLUE (3):
                Blue color.
            GREEN (4):
                Green color.
            RED (5):
                Red color.
            CYAN (6):
                Cyan color.
            ORANGE (7):
                Orange color. (Only used for system-generated
                annotations)
        """

        COLOR_UNSPECIFIED = 0
        PURPLE = 1
        BROWN = 2
        BLUE = 3
        GREEN = 4
        RED = 5
        CYAN = 6
        ORANGE = 7

    class DateRange(proto.Message):
        r"""Represents a Reporting Data Annotation's date range, both
        start and end dates are inclusive. Time zones are based on the
        parent property.

        Attributes:
            start_date (google.type.date_pb2.Date):
                Required. The start date for this range. Must
                be a valid date with year, month, and day set.
                The date may be in the past, present, or future.
            end_date (google.type.date_pb2.Date):
                Required. The end date for this range. Must
                be a valid date with year, month, and day set.
                This date must be greater than or equal to the
                start date.
        """

        start_date: date_pb2.Date = proto.Field(
            proto.MESSAGE,
            number=1,
            message=date_pb2.Date,
        )
        end_date: date_pb2.Date = proto.Field(
            proto.MESSAGE,
            number=2,
            message=date_pb2.Date,
        )

    annotation_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="target",
        message=date_pb2.Date,
    )
    annotation_date_range: DateRange = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="target",
        message=DateRange,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    title: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    color: Color = proto.Field(
        proto.ENUM,
        number=6,
        enum=Color,
    )
    system_generated: bool = proto.Field(
        proto.BOOL,
        number=7,
    )


class SubpropertySyncConfig(proto.Message):
    r"""Subproperty synchronization configuration controls how
    ordinary property configurations are synchronized to
    subproperties. This resource is provisioned automatically for
    each subproperty.

    Attributes:
        name (str):
            Output only. Identifier. Format:
            properties/{ordinary_property_id}/subpropertySyncConfigs/{subproperty_id}
            Example: properties/1234/subpropertySyncConfigs/5678
        apply_to_property (str):
            Output only. Immutable. Resource name of the
            subproperty that these settings apply to.
        custom_dimension_and_metric_sync_mode (google.analytics.admin_v1alpha.types.SubpropertySyncConfig.SynchronizationMode):
            Required. Specifies the Custom Dimension /
            Metric synchronization mode for the subproperty.

            If set to ALL, Custom Dimension / Metric
            synchronization will be immediately enabled.
            Local configuration of Custom Dimensions /
            Metrics will not be allowed on the subproperty
            so long as the synchronization mode is set to
            ALL.

            If set to NONE, Custom Dimensions / Metric
            synchronization is disabled. Custom Dimensions /
            Metrics must be configured explicitly on the
            Subproperty.
    """

    class SynchronizationMode(proto.Enum):
        r"""Synchronization modes for a subproperty

        Values:
            SYNCHRONIZATION_MODE_UNSPECIFIED (0):
                Synchronization mode unknown or not
                specified.
            NONE (1):
                Entities are not synchronized.
                Local edits are allowed on the subproperty.
            ALL (2):
                Entities are synchronized from parent
                property. Local mutations are not allowed on the
                subproperty (Create / Update / Delete)
        """

        SYNCHRONIZATION_MODE_UNSPECIFIED = 0
        NONE = 1
        ALL = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    apply_to_property: str = proto.Field(
        proto.STRING,
        number=2,
    )
    custom_dimension_and_metric_sync_mode: SynchronizationMode = proto.Field(
        proto.ENUM,
        number=3,
        enum=SynchronizationMode,
    )


class ReportingIdentitySettings(proto.Message):
    r"""A resource containing settings related to reporting identity.

    Attributes:
        name (str):
            Output only. Identifier. Resource name for this reporting
            identity settings singleton resource. Format:
            properties/{property_id}/reportingIdentitySettings Example:
            "properties/1234/reportingIdentitySettings".
        reporting_identity (google.analytics.admin_v1alpha.types.ReportingIdentitySettings.ReportingIdentity):
            The strategy used for identifying user
            identities in reports.
    """

    class ReportingIdentity(proto.Enum):
        r"""Various strategies for identifying user identities in
        reports.

        Values:
            IDENTITY_BLENDING_STRATEGY_UNSPECIFIED (0):
                Unspecified blending strategy.
            BLENDED (1):
                Blended reporting identity strategy.
            OBSERVED (2):
                Observed reporting identity strategy.
            DEVICE_BASED (3):
                Device-based reporting identity strategy.
        """

        IDENTITY_BLENDING_STRATEGY_UNSPECIFIED = 0
        BLENDED = 1
        OBSERVED = 2
        DEVICE_BASED = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    reporting_identity: ReportingIdentity = proto.Field(
        proto.ENUM,
        number=2,
        enum=ReportingIdentity,
    )


class UserProvidedDataSettings(proto.Message):
    r"""Configuration for user-provided data collection. This is a
    singleton resource for a Google Analytics property.

    Attributes:
        name (str):
            Identifier. Resource name of this setting.
            Format:
            properties/{property}/userProvidedDataSettings
            Example:
            "properties/1000/userProvidedDataSettings".
        user_provided_data_collection_enabled (bool):
            Optional. Whether this property accepts
            user-provided data sent to it.
        automatically_detected_data_collection_enabled (bool):
            Optional. Whether this property allows a Google Tag to
            automatically collect user-provided data from your website.
            This setting only takes effect if
            ``user_provided_data_collection_enabled`` is also true.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    user_provided_data_collection_enabled: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    automatically_detected_data_collection_enabled: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
