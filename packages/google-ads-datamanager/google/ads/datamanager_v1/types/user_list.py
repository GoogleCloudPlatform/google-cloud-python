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
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.ads.datamanager.v1",
    manifest={
        "DataSourceType",
        "UserList",
        "SizeInfo",
        "TargetNetworkInfo",
        "IngestedUserListInfo",
        "ContactIdInfo",
        "MobileIdInfo",
        "UserIdInfo",
        "PairIdInfo",
        "PartnerAudienceInfo",
        "PseudonymousIdInfo",
    },
)


class DataSourceType(proto.Enum):
    r"""Indicates source of upload data.

    Values:
        DATA_SOURCE_TYPE_UNSPECIFIED (0):
            Not specified.
        DATA_SOURCE_TYPE_FIRST_PARTY (1):
            The uploaded data is first-party data.
        DATA_SOURCE_TYPE_THIRD_PARTY_CREDIT_BUREAU (2):
            The uploaded data is from a third-party
            credit bureau.
        DATA_SOURCE_TYPE_THIRD_PARTY_VOTER_FILE (3):
            The uploaded data is from a third-party voter
            file.
        DATA_SOURCE_TYPE_THIRD_PARTY_PARTNER_DATA (4):
            The uploaded data is third party partner
            data.
    """

    DATA_SOURCE_TYPE_UNSPECIFIED = 0
    DATA_SOURCE_TYPE_FIRST_PARTY = 1
    DATA_SOURCE_TYPE_THIRD_PARTY_CREDIT_BUREAU = 2
    DATA_SOURCE_TYPE_THIRD_PARTY_VOTER_FILE = 3
    DATA_SOURCE_TYPE_THIRD_PARTY_PARTNER_DATA = 4


class UserList(proto.Message):
    r"""A user list resource.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the user list. Format:
            accountTypes/{account_type}/accounts/{account}/userLists/{user_list}
        id (int):
            Output only. The unique ID of the user list.
        read_only (bool):
            Output only. An option that indicates if a
            user may edit a list.
        display_name (str):
            Required. The display name of the user list.

            This field is a member of `oneof`_ ``_display_name``.
        description (str):
            Optional. A description of the user list.

            This field is a member of `oneof`_ ``_description``.
        membership_status (google.ads.datamanager_v1.types.UserList.MembershipStatus):
            Optional. Membership status of this user
            list.

            This field is a member of `oneof`_ ``_membership_status``.
        integration_code (str):
            Optional. An ID from external system. It is
            used by user list sellers to correlate IDs on
            their systems.

            This field is a member of `oneof`_ ``_integration_code``.
        membership_duration (google.protobuf.duration_pb2.Duration):
            Optional. The duration a user remains in the user list.
            Valid durations are exact multiples of 24 hours (86400
            seconds). Providing a value that is not an exact multiple of
            24 hours will result in an INVALID_ARGUMENT error.
        closing_reason (google.ads.datamanager_v1.types.UserList.ClosingReason):
            Output only. The reason why this user list
            membership status is closed.

            This field is a member of `oneof`_ ``_closing_reason``.
        access_reason (google.ads.datamanager_v1.types.UserList.AccessReason):
            Output only. The reason this account has been
            granted access to the list.
        account_access_status (google.ads.datamanager_v1.types.UserList.AccessStatus):
            Optional. Indicates if this share is still enabled. When a
            user list is shared with the account this field is set to
            ``ENABLED``. Later the user list owner can decide to revoke
            the share and make it ``DISABLED``.

            This field is a member of `oneof`_ ``_account_access_status``.
        size_info (google.ads.datamanager_v1.types.SizeInfo):
            Output only. Estimated number of members in
            this user list in different target networks.
        target_network_info (google.ads.datamanager_v1.types.TargetNetworkInfo):
            Optional. Eligibility information for
            different target networks.
        ingested_user_list_info (google.ads.datamanager_v1.types.IngestedUserListInfo):
            Optional. Represents a user list that is
            populated by user ingested data.

            This field is a member of `oneof`_ ``user_list_info``.
    """

    class MembershipStatus(proto.Enum):
        r"""Status of the user list.

        Values:
            MEMBERSHIP_STATUS_UNSPECIFIED (0):
                Not specified.
            OPEN (1):
                Open status - User list is accruing members
                and can be targeted to.
            CLOSED (2):
                Closed status - No new members being added.
        """

        MEMBERSHIP_STATUS_UNSPECIFIED = 0
        OPEN = 1
        CLOSED = 2

    class ClosingReason(proto.Enum):
        r"""Indicates the reason why the user list was closed.
        This enum is only used when a list is auto-closed by the system.

        Values:
            CLOSING_REASON_UNSPECIFIED (0):
                Not specified.
            UNUSED (1):
                The user list was closed because it has not
                been used in targeting recently. See
                https://support.google.com/google-ads/answer/2472738
                for details.
        """

        CLOSING_REASON_UNSPECIFIED = 0
        UNUSED = 1

    class AccessReason(proto.Enum):
        r"""Enum describing possible access reasons.

        Values:
            ACCESS_REASON_UNSPECIFIED (0):
                Not specified.
            OWNED (1):
                The resource is owned by the user.
            SHARED (2):
                The resource is shared to the user.
            LICENSED (3):
                The resource is licensed to the user.
            SUBSCRIBED (4):
                The user subscribed to the resource.
            AFFILIATED (5):
                The resource is accessible to the user.
        """

        ACCESS_REASON_UNSPECIFIED = 0
        OWNED = 1
        SHARED = 2
        LICENSED = 3
        SUBSCRIBED = 4
        AFFILIATED = 5

    class AccessStatus(proto.Enum):
        r"""Indicates if this client still has access to the list.

        Values:
            ACCESS_STATUS_UNSPECIFIED (0):
                Not specified.
            ENABLED (1):
                The access is enabled.
            DISABLED (2):
                The access is disabled.
        """

        ACCESS_STATUS_UNSPECIFIED = 0
        ENABLED = 1
        DISABLED = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    id: int = proto.Field(
        proto.INT64,
        number=2,
    )
    read_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    membership_status: MembershipStatus = proto.Field(
        proto.ENUM,
        number=6,
        optional=True,
        enum=MembershipStatus,
    )
    integration_code: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )
    membership_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=8,
        message=duration_pb2.Duration,
    )
    closing_reason: ClosingReason = proto.Field(
        proto.ENUM,
        number=9,
        optional=True,
        enum=ClosingReason,
    )
    access_reason: AccessReason = proto.Field(
        proto.ENUM,
        number=10,
        enum=AccessReason,
    )
    account_access_status: AccessStatus = proto.Field(
        proto.ENUM,
        number=11,
        optional=True,
        enum=AccessStatus,
    )
    size_info: "SizeInfo" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="SizeInfo",
    )
    target_network_info: "TargetNetworkInfo" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="TargetNetworkInfo",
    )
    ingested_user_list_info: "IngestedUserListInfo" = proto.Field(
        proto.MESSAGE,
        number=14,
        oneof="user_list_info",
        message="IngestedUserListInfo",
    )


class SizeInfo(proto.Message):
    r"""Estimated number of members in this user list in different
    target networks.

    Attributes:
        display_network_members_count (int):
            Output only. Estimated number of members in
            this user list, on the Google Display Network.
        search_network_members_count (int):
            Output only. Estimated number of members in
            this user list in the google.com domain. These
            are the members available for targeting in
            Search campaigns.
        youtube_members_count (int):
            Output only. Estimated number of members in
            this user list on YouTube.
        gmail_members_count (int):
            Output only. Estimated number of members in
            this user list on Gmail.
    """

    display_network_members_count: int = proto.Field(
        proto.INT64,
        number=1,
    )
    search_network_members_count: int = proto.Field(
        proto.INT64,
        number=2,
    )
    youtube_members_count: int = proto.Field(
        proto.INT64,
        number=3,
    )
    gmail_members_count: int = proto.Field(
        proto.INT64,
        number=4,
    )


class TargetNetworkInfo(proto.Message):
    r"""Eligibility information for different target networks.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        eligible_for_display (bool):
            Output only. Indicates this user list is
            eligible for Google Display Network.
        eligible_for_search (bool):
            Optional. Indicates if this user list is
            eligible for Google Search Network.

            This field is a member of `oneof`_ ``_eligible_for_search``.
    """

    eligible_for_display: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    eligible_for_search: bool = proto.Field(
        proto.BOOL,
        number=2,
        optional=True,
    )


class IngestedUserListInfo(proto.Message):
    r"""Represents a user list that is populated by user provided
    data.

    Attributes:
        upload_key_types (MutableSequence[google.ads.datamanager_v1.types.IngestedUserListInfo.UploadKeyType]):
            Required. Immutable. Upload key types of this
            user list.
        contact_id_info (google.ads.datamanager_v1.types.ContactIdInfo):
            Optional. Additional information when ``CONTACT_ID`` is one
            of the ``upload_key_types``.
        mobile_id_info (google.ads.datamanager_v1.types.MobileIdInfo):
            Optional. Additional information when ``MOBILE_ID`` is one
            of the ``upload_key_types``.
        user_id_info (google.ads.datamanager_v1.types.UserIdInfo):
            Optional. Additional information when ``USER_ID`` is one of
            the ``upload_key_types``.
        pair_id_info (google.ads.datamanager_v1.types.PairIdInfo):
            Optional. Additional information when ``PAIR_ID`` is one of
            the ``upload_key_types``.

            This feature is only available to data partners.
        pseudonymous_id_info (google.ads.datamanager_v1.types.PseudonymousIdInfo):
            Optional. Additional information for ``PSEUDONYMOUS_ID`` is
            one of the ``upload_key_types``.
        partner_audience_info (google.ads.datamanager_v1.types.PartnerAudienceInfo):
            Optional. Additional information for partner
            audiences.
            This feature is only available to data partners.
    """

    class UploadKeyType(proto.Enum):
        r"""Enum containing the possible upload key types of a user list.

        Values:
            UPLOAD_KEY_TYPE_UNSPECIFIED (0):
                Not specified.
            CONTACT_ID (1):
                Customer info such as email address, phone
                number or physical address.
            MOBILE_ID (2):
                Mobile advertising ids.
            USER_ID (3):
                Third party provided user ids.
            PAIR_ID (4):
                Publisher advertiser identity reconciliation
                ids.
            PSEUDONYMOUS_ID (5):
                Data Management Platform IDs:

                - Google User ID
                - Partner Provided ID
                - Publisher Provided ID
                - iOS IDFA
                - Android advertising ID
                - Roku ID
                - Amazon Fire TV ID
                - Xbox or Microsoft ID
                - Generic Device ID
        """

        UPLOAD_KEY_TYPE_UNSPECIFIED = 0
        CONTACT_ID = 1
        MOBILE_ID = 2
        USER_ID = 3
        PAIR_ID = 4
        PSEUDONYMOUS_ID = 5

    upload_key_types: MutableSequence[UploadKeyType] = proto.RepeatedField(
        proto.ENUM,
        number=1,
        enum=UploadKeyType,
    )
    contact_id_info: "ContactIdInfo" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ContactIdInfo",
    )
    mobile_id_info: "MobileIdInfo" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="MobileIdInfo",
    )
    user_id_info: "UserIdInfo" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="UserIdInfo",
    )
    pair_id_info: "PairIdInfo" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="PairIdInfo",
    )
    pseudonymous_id_info: "PseudonymousIdInfo" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="PseudonymousIdInfo",
    )
    partner_audience_info: "PartnerAudienceInfo" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="PartnerAudienceInfo",
    )


class ContactIdInfo(proto.Message):
    r"""Additional information when ``CONTACT_ID`` is one of the
    ``upload_key_types``.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        data_source_type (google.ads.datamanager_v1.types.DataSourceType):
            Optional. Immutable. Source of the upload
            data

            This field is a member of `oneof`_ ``_data_source_type``.
        match_rate_percentage (int):
            Output only. Match rate for customer match
            user lists.
    """

    data_source_type: "DataSourceType" = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum="DataSourceType",
    )
    match_rate_percentage: int = proto.Field(
        proto.INT32,
        number=2,
    )


class MobileIdInfo(proto.Message):
    r"""Additional information when ``MOBILE_ID`` is one of the
    ``upload_key_types``.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        data_source_type (google.ads.datamanager_v1.types.DataSourceType):
            Optional. Immutable. Source of the upload
            data.

            This field is a member of `oneof`_ ``_data_source_type``.
        key_space (google.ads.datamanager_v1.types.MobileIdInfo.KeySpace):
            Required. Immutable. The key space of mobile
            IDs.

            This field is a member of `oneof`_ ``_key_space``.
        app_id (str):
            Required. Immutable. A string that uniquely
            identifies a mobile application from which the
            data was collected.

            This field is a member of `oneof`_ ``_app_id``.
    """

    class KeySpace(proto.Enum):
        r"""Key space for mobile ID.

        Values:
            KEY_SPACE_UNSPECIFIED (0):
                Not specified.
            IOS (1):
                The iOS keyspace.
            ANDROID (2):
                The Android keyspace.
        """

        KEY_SPACE_UNSPECIFIED = 0
        IOS = 1
        ANDROID = 2

    data_source_type: "DataSourceType" = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum="DataSourceType",
    )
    key_space: KeySpace = proto.Field(
        proto.ENUM,
        number=2,
        optional=True,
        enum=KeySpace,
    )
    app_id: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )


class UserIdInfo(proto.Message):
    r"""Additional information when ``USER_ID`` is one of the
    ``upload_key_types``.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        data_source_type (google.ads.datamanager_v1.types.DataSourceType):
            Optional. Immutable. Source of the upload
            data.

            This field is a member of `oneof`_ ``_data_source_type``.
    """

    data_source_type: "DataSourceType" = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum="DataSourceType",
    )


class PairIdInfo(proto.Message):
    r"""Additional information when ``PAIR_ID`` is one of the
    ``upload_key_types``.

    This feature is only available to data partners.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        publisher_id (int):
            Required. Immutable. Identifies the publisher
            that the Publisher Advertiser Identity
            Reconciliation user list is reconciled with.
            This field is provided by the cleanroom provider
            and is only unique in the scope of that
            cleanroom. This cannot be used as a global
            identifier across multiple cleanrooms.

            This field is a member of `oneof`_ ``_publisher_id``.
        publisher_name (str):
            Required. Descriptive name of the publisher
            to be displayed in the UI for a better targeting
            experience.

            This field is a member of `oneof`_ ``_publisher_name``.
        match_rate_percentage (int):
            Required. This field denotes the percentage
            of membership match of this user list with the
            corresponding publisher's first party data. Must
            be between 0 and 100 inclusive.

            This field is a member of `oneof`_ ``_match_rate_percentage``.
        advertiser_identifier_count (int):
            Optional. The count of the advertiser's first
            party data records that have been uploaded to a
            clean room provider. This does not signify the
            size of a PAIR user list.

            This field is a member of `oneof`_ ``_advertiser_identifier_count``.
        clean_room_identifier (str):
            Required. Immutable. Identifies a unique
            advertiser to publisher relationship with one
            clean room provider or across multiple clean
            room providers.

            This field is a member of `oneof`_ ``_clean_room_identifier``.
    """

    publisher_id: int = proto.Field(
        proto.INT64,
        number=1,
        optional=True,
    )
    publisher_name: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    match_rate_percentage: int = proto.Field(
        proto.INT32,
        number=3,
        optional=True,
    )
    advertiser_identifier_count: int = proto.Field(
        proto.INT64,
        number=4,
        optional=True,
    )
    clean_room_identifier: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )


class PartnerAudienceInfo(proto.Message):
    r"""Additional information for partner audiences.

    This feature is only available to data partners.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        partner_audience_source (google.ads.datamanager_v1.types.PartnerAudienceInfo.PartnerAudienceSource):
            Required. Immutable. The source of the
            partner audience.

            This field is a member of `oneof`_ ``_partner_audience_source``.
        commerce_partner (str):
            Optional. The commerce partner name. Only allowed if
            ``partner_audience_source`` is ``COMMERCE_AUDIENCE``.

            This field is a member of `oneof`_ ``_commerce_partner``.
    """

    class PartnerAudienceSource(proto.Enum):
        r"""Partner audience source.

        Values:
            PARTNER_AUDIENCE_SOURCE_UNSPECIFIED (0):
                Not specified.
            COMMERCE_AUDIENCE (1):
                Partner Audience source is commerce audience.
            LINEAR_TV_AUDIENCE (2):
                Partner Audience source is linear TV
                audience.
            AGENCY_PROVIDER_AUDIENCE (3):
                Partner Audience source is agency/provider
                audience.
        """

        PARTNER_AUDIENCE_SOURCE_UNSPECIFIED = 0
        COMMERCE_AUDIENCE = 1
        LINEAR_TV_AUDIENCE = 2
        AGENCY_PROVIDER_AUDIENCE = 3

    partner_audience_source: PartnerAudienceSource = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum=PartnerAudienceSource,
    )
    commerce_partner: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )


class PseudonymousIdInfo(proto.Message):
    r"""Additional information when ``PSEUDONYMOUS_ID`` is one of the
    ``upload_key_types``.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        sync_status (google.ads.datamanager_v1.types.PseudonymousIdInfo.SyncStatus):
            Output only. Sync status of the user list.

            This field is a member of `oneof`_ ``_sync_status``.
        billable_record_count (int):
            Optional. Immutable. The number of billable
            records (e.g. uploaded or matched).

            This field is a member of `oneof`_ ``_billable_record_count``.
    """

    class SyncStatus(proto.Enum):
        r"""Sync status of the user list.

        Values:
            SYNC_STATUS_UNSPECIFIED (0):
                Not specified.
            CREATED (1):
                The user list has been created as a
                placeholder. List contents and/or metadata are
                still being synced. The user list is not ready
                for use.
            READY_FOR_USE (2):
                The user list is ready for use. Contents and
                cookies have been synced correctly.
            FAILED (3):
                An error has occurred syncing user list
                contents and/or metadata. The user list cannot
                be used.
        """

        SYNC_STATUS_UNSPECIFIED = 0
        CREATED = 1
        READY_FOR_USE = 2
        FAILED = 3

    sync_status: SyncStatus = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum=SyncStatus,
    )
    billable_record_count: int = proto.Field(
        proto.INT64,
        number=2,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
