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

import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.ads.datamanager.v1",
    manifest={
        "ErrorReason",
    },
)


class ErrorReason(proto.Enum):
    r"""Error reasons for Data Manager API.
    NOTE: This enum is not frozen and new values may be added in the
    future.

    Values:
        ERROR_REASON_UNSPECIFIED (0):
            Do not use this default value.
        INTERNAL_ERROR (1):
            An internal error has occurred.
        DEADLINE_EXCEEDED (2):
            The request took too long to respond.
        RESOURCE_EXHAUSTED (3):
            Too many requests.
        NOT_FOUND (4):
            Resource not found.
        PERMISSION_DENIED (5):
            The user does not have permission or the
            resource is not found.
        INVALID_ARGUMENT (6):
            There was a problem with the request.
        REQUIRED_FIELD_MISSING (7):
            Required field is missing.
        INVALID_FORMAT (8):
            Format is invalid.
        INVALID_HEX_ENCODING (9):
            The HEX encoded value is malformed.
        INVALID_BASE64_ENCODING (10):
            The base64 encoded value is malformed.
        INVALID_SHA256_FORMAT (11):
            The SHA256 encoded value is malformed.
        INVALID_POSTAL_CODE (12):
            Postal code is not valid.
        INVALID_COUNTRY_CODE (13):
            Deprecated: Enum is unused in the Data
            Manager API.
        INVALID_ENUM_VALUE (14):
            Enum value cannot be used.
        INVALID_USER_LIST_TYPE (15):
            Type of the user list is not applicable for
            this request.
        INVALID_AUDIENCE_MEMBER (16):
            This audience member is not valid.
        TOO_MANY_AUDIENCE_MEMBERS (17):
            Maximum number of audience members allowed
            per request is 10,000.
        TOO_MANY_USER_IDENTIFIERS (18):
            Maximum number of user identifiers allowed
            per audience member is 10.
        TOO_MANY_DESTINATIONS (19):
            Maximum number of destinations allowed per
            request is 10.
        INVALID_DESTINATION (20):
            This Destination is not valid.
        DATA_PARTNER_USER_LIST_MUTATE_NOT_ALLOWED (21):
            Data Partner does not have access to the
            operating account owned userlist.
        INVALID_MOBILE_ID_FORMAT (22):
            Mobile ID format is not valid.
        INVALID_USER_LIST_ID (23):
            User list is not valid.
        MULTIPLE_DATA_TYPES_NOT_ALLOWED (24):
            Multiple data types are not allowed to be
            ingested in a single request.
        DIFFERENT_LOGIN_ACCOUNTS_NOT_ALLOWED_FOR_DATA_PARTNER (25):
            Destination configs containing a DataPartner
            login account must have the same login account
            across all destination configs.
        TERMS_AND_CONDITIONS_NOT_SIGNED (26):
            Required terms and conditions are not
            accepted.
        INVALID_NUMBER_FORMAT (27):
            Invalid number format.
        INVALID_CONVERSION_ACTION_ID (28):
            Conversion action ID is not valid.
        INVALID_CONVERSION_ACTION_TYPE (29):
            The conversion action type is not valid.
        INVALID_CURRENCY_CODE (30):
            The currency code is not supported.
        INVALID_EVENT (31):
            This event is not valid.
        TOO_MANY_EVENTS (32):
            Maximum number of events allowed per request
            is 10,000.
        DESTINATION_ACCOUNT_NOT_ENABLED_ENHANCED_CONVERSIONS_FOR_LEADS (33):
            The destination account is not enabled for
            enhanced conversions for leads.
        DESTINATION_ACCOUNT_DATA_POLICY_PROHIBITS_ENHANCED_CONVERSIONS (34):
            Enhanced conversions can't be used for the
            destination account because of Google customer
            data policies. Contact your Google
            representative..
        DESTINATION_ACCOUNT_ENHANCED_CONVERSIONS_TERMS_NOT_SIGNED (35):
            The destination account hasn't agreed to the
            terms for enhanced conversions.
        DUPLICATE_DESTINATION_REFERENCE (36):
            Two or more destinations in the request have
            the same reference.
        UNSUPPORTED_OPERATING_ACCOUNT_FOR_DATA_PARTNER (37):
            Unsupported operating account for data
            partner authorization.
        UNSUPPORTED_LINKED_ACCOUNT_FOR_DATA_PARTNER (38):
            Unsupported linked account for data partner
            authorization.
        NO_IDENTIFIERS_PROVIDED (39):
            Events data contains no user identifiers or
            ad identifiers. For Floodlight Event ingestion
            this error indicates requests contains no ad
            identifiers.
        INVALID_PROPERTY_TYPE (40):
            The property type is not supported.
        INVALID_STREAM_TYPE (41):
            The stream type is not supported.
        LINKED_ACCOUNT_ONLY_ALLOWED_WITH_DATA_PARTNER_LOGIN_ACCOUNT (42):
            Linked account is only supported when the login account is a
            ``DATA_PARTNER`` account.
        OPERATING_ACCOUNT_LOGIN_ACCOUNT_MISMATCH (43):
            The login account must be the same as the
            operating account for the given use case.
        EVENT_TIME_INVALID (44):
            Event did not occur within the acceptable
            time window.
        RESERVED_NAME_USED (45):
            Parameter uses a reserved name.
        INVALID_EVENT_NAME (46):
            The event name is not supported.
        NOT_ALLOWLISTED (47):
            The account is not allowlisted for the given
            feature.
        INVALID_REQUEST_ID (48):
            The request ID used to retrieve the status of a request is
            not valid. Status can only be retrieved for requests that
            succeed and don't have ``validate_only=true``.
        MULTIPLE_DESTINATIONS_FOR_GOOGLE_ANALYTICS_EVENT (49):
            An event had 2 or more Google Analytics
            destinations.
        FIELD_VALUE_TOO_LONG (50):
            Length of the field value is too long.
        FIELD_VALUE_TOO_SHORT (106):
            Length of the field value is too short.
        TOO_MANY_ELEMENTS (51):
            Too many elements in a list in the request.
        TOO_FEW_ELEMENTS (105):
            Too few elements in a list in the request.
        ALREADY_EXISTS (52):
            The resource already exists.
        IMMUTABLE_FIELD_FOR_UPDATE (53):
            Attempted to set an immutable field for an
            update request.
        INVALID_RESOURCE_NAME (54):
            The resource name is invalid.
        INVALID_FILTER (55):
            The query filter is invalid.
        INVALID_UPDATE_MASK (56):
            The update mask is invalid.
        INVALID_PAGE_TOKEN (57):
            The page token is invalid.
        CANNOT_UPDATE_DISABLED_LICENSE (58):
            Cannot update a license that has been
            disabled.
        CANNOT_CREATE_LICENSE_FOR_SENSITIVE_USERLIST (59):
            Sensitive user lists cannot be licensed to
            this client.
        INSUFFICIENT_COST (60):
            Cost too low for this license.
        CANNOT_DISABLE_LICENSE (61):
            Reseller license cannot be disabled since it
            is in use.
        INVALID_CLIENT_ACCOUNT_ID (62):
            Invalid client account id.
        PRICING_ONLY_ZERO_COST_ALLOWED (63):
            Non-zero cost not allowed for this client
            account.
        PRICE_TOO_HIGH (64):
            Cost too high for this license.
        CUSTOMER_NOT_ALLOWED_TO_CREATE_LICENSE (65):
            Customer not allowed to create license.
        INVALID_PRICING_END_DATE (66):
            Pricing end date is invalid for this license.
        CANNOT_LICENSE_LOGICAL_LIST_WITH_LICENSED_OR_SHARED_SEGMENT (67):
            Logical user list with shared or licensed
            segment cannot be licensed.
        MISMATCHED_ACCOUNT_TYPE (68):
            Client customer's account type in the request
            does not match the customer's actual account
            type.
        MEDIA_SHARE_COST_NOT_ALLOWED_FOR_LICENSE_TYPE (69):
            License type does not support media share
            cost.
        MEDIA_SHARE_COST_NOT_ALLOWED_FOR_CLIENT_CUSTOMER (70):
            Client customer type does not support media
            share cost.
        INVALID_MEDIA_SHARE_COST (71):
            Invalid media share cost.
        INVALID_COST_TYPE (72):
            Invalid cost type.
        MEDIA_SHARE_COST_NOT_ALLOWED_FOR_NON_COMMERCE_USER_LIST (73):
            UserList type does not support media share
            cost.
        MAX_COST_NOT_ALLOWED (74):
            Max cost is only allowed for cost_type MEDIA_SHARE.
        COMMERCE_AUDIENCE_CAN_ONLY_BE_DIRECTLY_LICENSED (75):
            Commerce audience can only be directly
            licensed.
        INVALID_DESCRIPTION (76):
            The description is not valid.
        INVALID_DISPLAY_NAME (77):
            The display name is not valid.
        DISPLAY_NAME_ALREADY_USED (78):
            The display name is already being used for
            another user list for the account.
        OWNERSHIP_REQUIRED_FOR_UPDATE (79):
            Ownership is required to modify the user
            list.
        USER_LIST_MUTATION_NOT_SUPPORTED (80):
            The user list type is read-only and does not
            support mutation.
        SENSITIVE_USER_LIST_IMMUTABLE (81):
            A user list which is privacy sensitive or
            legal rejected cannot be mutated by external
            users.
        BILLABLE_RECORD_COUNT_IMMUTABLE (82):
            The remarketing user list's billable record
            field cannot be modified once it is set.
        USER_LIST_NAME_RESERVED (83):
            The user list name is reserved for system
            lists.
        ADVERTISER_NOT_ALLOWLISTED_FOR_UPLOADED_DATA (84):
            The advertiser needs to be allowlisted to use
            remarketing lists created from advertiser
            uploaded data.
        UNSUPPORTED_PARTNER_AUDIENCE_SOURCE (85):
            The partner audience source is not supported
            for the user list type.
        COMMERCE_PARTNER_NOT_ALLOWED (86):
            Setting the ``commerce_partner`` field is only supported if
            the ``partner_audience_source`` is ``COMMERCE_AUDIENCE``.
        UNSUPPORTED_PARTNER_AUDIENCE_INFO (87):
            The ``partner_audience_info`` field is not supported for the
            user list type.
        PARTNER_MATCH_FOR_MANAGER_ACCOUNT_DISALLOWED (88):
            Partner Match user lists cannot be created by
            manager accounts.
        DATA_PARTNER_NOT_ALLOWLISTED_FOR_THIRD_PARTY_PARTNER_DATA (89):
            The data partner is not allowlisted for
            THIRD_PARTY_PARTNER_DATA.
        ADVERTISER_TOS_NOT_ACCEPTED (90):
            The advertiser has not accepted the partner's
            terms of service.
        ADVERTISER_NOT_ALLOWLISTED_FOR_THIRD_PARTY_PARTNER_DATA (91):
            The advertiser is not allowlisted for
            THIRD_PARTY_PARTNER_DATA.
        USER_LIST_TYPE_NOT_SUPPORTED_FOR_ACCOUNT (92):
            This user list type is not supported for this
            account.
        INVALID_COMMERCE_PARTNER (93):
            The ``commerce_partner`` field is invalid.
        CUSTOMER_NOT_ALLOWLISTED_FOR_COMMERCE_AUDIENCE (94):
            The data provider is not allowlisted to
            create commerce audiences.
        UNSUPPORTED_USER_LIST_UPLOAD_KEY_TYPES (95):
            The user list upload key types are not
            supported.
        UNSUPPORTED_INGESTED_USER_LIST_INFO_CONFIG (96):
            The ingested user list info config is not
            supported.
        UNSUPPORTED_ACCOUNT_TYPES_FOR_USER_LIST_TYPE (97):
            The account types are not supported for the
            user list type.
        UNSUPPORTED_ACCOUNT_TYPE_FOR_PARTNER_LINK (98):
            The account types are not supported for the
            partner link.
        MEMBERSHIP_DURATION_TOO_LONG (99):
            The user list membership duration is too
            long.
        INVALID_MERCHANT_ID (100):
            The ``merchant_id`` field is not valid.
        EU_POLITICAL_ADVERTISING_DECLARATION_REQUIRED (101):
            The customer contains non-exempt campaigns
            without the EU political advertising
            declaration.
        ACCOUNT_INELIGIBLE_FOR_STORE_SALES (102):
            Account is not eligible for Store Sales.
        INVALID_MERCHANT_FEED_LANGUAGE_CODE (103):
            The merchant feed language code is not valid.
        INVALID_REGION_CODE (104):
            The region code is not valid.
        INVALID_SUBDIVISION_CODE (107):
            The subdivision code is not valid.
        INVALID_SUBCONTINENT_CODE (108):
            The subcontinent code is not valid.
        INVALID_CONTINENT_CODE (109):
            The continent code is not valid.
        INVALID_DEVICE_CATEGORY (110):
            The device category is not valid.
        BOTH_CLIENT_ID_AND_APP_INSTANCE_ID_NOT_ALLOWED (111):
            Both app_instance_id and client_id are set.
        GOOGLE_ANALYTICS_SUBPROPERTY_OR_ROLLUP_PROPERTY_NOT_ALLOWED (112):
            The Google Analytics property is a
            subproperty or rollup property.
        THIRD_PARTY_USER_DATA_NOT_ALLOWED (113):
            Third party user data can only be set by data
            partners.
        INVALID_COUPON_CODE (114):
            The coupon code is not valid.
        EVENT_SOURCE_AND_DESTINATION_MISMATCH (115):
            The event source type does not match the
            destination type.
        DESTINATION_ACCOUNT_TYPE_MISMATCH (116):
            The destination account type does not match
            the specified account id.
        CUSTOM_VARIABLE_VALUE_CONTAINS_PII (117):
            The custom variable value contains personally
            identifiable information (PII).
        CUSTOM_VARIABLE_NOT_ENABLED (118):
            The custom variable is not enabled.
        INVALID_CUSTOM_VARIABLE_VALUE (119):
            The custom variable's value is invalid.
        CUSTOM_VARIABLE_NOT_FOUND (120):
            The destination does not have a custom variable with a name
            that matches the specified ``variable``.
        TOO_MANY_USERS (121):
            Maximum number of users allowed per request
            is 10,000.
        BASELINE_LOCATION_AUTO_DETECTION_FAILED (122):
            The
            [location_auto_detection_enabled][google.ads.datamanager.v1.Baseline.location_auto_detection_enabled]
            field of the request was set to ``true``, but auto detection
            of baseline location failed.
        INSIGHTS_MISSING_FOR_DIMENSION (123):
            Insights missing for this dimension.
        REQUIRED_PREREQUISITE_LINK_MISSING (124):
            A required prerequisite link (such as a
            Google Ads link) must exist for the Google
            Analytics property to perform this operation.
        INVALID_REMOVE_AS_OF_TIME (125):
            The remove as of time must be in the past or
            present. Future timestamps are not permitted for
            removing audience members.
        REQUEST_TOO_OLD (126):
            Request status is only available for
            approximately 50 days after the API receives a
            request.
        CONVERSION_ACTION_TOO_RECENTLY_CREATED (127):
            The conversion action was created too
            recently.
        INVALID_AD_IDENTIFIER_FOR_ACCOUNT (128):
            The ad identifier does not belong to the account.

            For example, the
            [``gclid``][google.ads.datamanager.v1.AdIdentifiers.gclid]
            isn't associated with the
            [``operating_account``][google.ads.datamanager.v1.Destination.operating_account]
            and
            [``product_destination_id``][google.ads.datamanager.v1.Destination.product_destination_id]
            of the destination.
    """

    ERROR_REASON_UNSPECIFIED = 0
    INTERNAL_ERROR = 1
    DEADLINE_EXCEEDED = 2
    RESOURCE_EXHAUSTED = 3
    NOT_FOUND = 4
    PERMISSION_DENIED = 5
    INVALID_ARGUMENT = 6
    REQUIRED_FIELD_MISSING = 7
    INVALID_FORMAT = 8
    INVALID_HEX_ENCODING = 9
    INVALID_BASE64_ENCODING = 10
    INVALID_SHA256_FORMAT = 11
    INVALID_POSTAL_CODE = 12
    INVALID_COUNTRY_CODE = 13
    INVALID_ENUM_VALUE = 14
    INVALID_USER_LIST_TYPE = 15
    INVALID_AUDIENCE_MEMBER = 16
    TOO_MANY_AUDIENCE_MEMBERS = 17
    TOO_MANY_USER_IDENTIFIERS = 18
    TOO_MANY_DESTINATIONS = 19
    INVALID_DESTINATION = 20
    DATA_PARTNER_USER_LIST_MUTATE_NOT_ALLOWED = 21
    INVALID_MOBILE_ID_FORMAT = 22
    INVALID_USER_LIST_ID = 23
    MULTIPLE_DATA_TYPES_NOT_ALLOWED = 24
    DIFFERENT_LOGIN_ACCOUNTS_NOT_ALLOWED_FOR_DATA_PARTNER = 25
    TERMS_AND_CONDITIONS_NOT_SIGNED = 26
    INVALID_NUMBER_FORMAT = 27
    INVALID_CONVERSION_ACTION_ID = 28
    INVALID_CONVERSION_ACTION_TYPE = 29
    INVALID_CURRENCY_CODE = 30
    INVALID_EVENT = 31
    TOO_MANY_EVENTS = 32
    DESTINATION_ACCOUNT_NOT_ENABLED_ENHANCED_CONVERSIONS_FOR_LEADS = 33
    DESTINATION_ACCOUNT_DATA_POLICY_PROHIBITS_ENHANCED_CONVERSIONS = 34
    DESTINATION_ACCOUNT_ENHANCED_CONVERSIONS_TERMS_NOT_SIGNED = 35
    DUPLICATE_DESTINATION_REFERENCE = 36
    UNSUPPORTED_OPERATING_ACCOUNT_FOR_DATA_PARTNER = 37
    UNSUPPORTED_LINKED_ACCOUNT_FOR_DATA_PARTNER = 38
    NO_IDENTIFIERS_PROVIDED = 39
    INVALID_PROPERTY_TYPE = 40
    INVALID_STREAM_TYPE = 41
    LINKED_ACCOUNT_ONLY_ALLOWED_WITH_DATA_PARTNER_LOGIN_ACCOUNT = 42
    OPERATING_ACCOUNT_LOGIN_ACCOUNT_MISMATCH = 43
    EVENT_TIME_INVALID = 44
    RESERVED_NAME_USED = 45
    INVALID_EVENT_NAME = 46
    NOT_ALLOWLISTED = 47
    INVALID_REQUEST_ID = 48
    MULTIPLE_DESTINATIONS_FOR_GOOGLE_ANALYTICS_EVENT = 49
    FIELD_VALUE_TOO_LONG = 50
    FIELD_VALUE_TOO_SHORT = 106
    TOO_MANY_ELEMENTS = 51
    TOO_FEW_ELEMENTS = 105
    ALREADY_EXISTS = 52
    IMMUTABLE_FIELD_FOR_UPDATE = 53
    INVALID_RESOURCE_NAME = 54
    INVALID_FILTER = 55
    INVALID_UPDATE_MASK = 56
    INVALID_PAGE_TOKEN = 57
    CANNOT_UPDATE_DISABLED_LICENSE = 58
    CANNOT_CREATE_LICENSE_FOR_SENSITIVE_USERLIST = 59
    INSUFFICIENT_COST = 60
    CANNOT_DISABLE_LICENSE = 61
    INVALID_CLIENT_ACCOUNT_ID = 62
    PRICING_ONLY_ZERO_COST_ALLOWED = 63
    PRICE_TOO_HIGH = 64
    CUSTOMER_NOT_ALLOWED_TO_CREATE_LICENSE = 65
    INVALID_PRICING_END_DATE = 66
    CANNOT_LICENSE_LOGICAL_LIST_WITH_LICENSED_OR_SHARED_SEGMENT = 67
    MISMATCHED_ACCOUNT_TYPE = 68
    MEDIA_SHARE_COST_NOT_ALLOWED_FOR_LICENSE_TYPE = 69
    MEDIA_SHARE_COST_NOT_ALLOWED_FOR_CLIENT_CUSTOMER = 70
    INVALID_MEDIA_SHARE_COST = 71
    INVALID_COST_TYPE = 72
    MEDIA_SHARE_COST_NOT_ALLOWED_FOR_NON_COMMERCE_USER_LIST = 73
    MAX_COST_NOT_ALLOWED = 74
    COMMERCE_AUDIENCE_CAN_ONLY_BE_DIRECTLY_LICENSED = 75
    INVALID_DESCRIPTION = 76
    INVALID_DISPLAY_NAME = 77
    DISPLAY_NAME_ALREADY_USED = 78
    OWNERSHIP_REQUIRED_FOR_UPDATE = 79
    USER_LIST_MUTATION_NOT_SUPPORTED = 80
    SENSITIVE_USER_LIST_IMMUTABLE = 81
    BILLABLE_RECORD_COUNT_IMMUTABLE = 82
    USER_LIST_NAME_RESERVED = 83
    ADVERTISER_NOT_ALLOWLISTED_FOR_UPLOADED_DATA = 84
    UNSUPPORTED_PARTNER_AUDIENCE_SOURCE = 85
    COMMERCE_PARTNER_NOT_ALLOWED = 86
    UNSUPPORTED_PARTNER_AUDIENCE_INFO = 87
    PARTNER_MATCH_FOR_MANAGER_ACCOUNT_DISALLOWED = 88
    DATA_PARTNER_NOT_ALLOWLISTED_FOR_THIRD_PARTY_PARTNER_DATA = 89
    ADVERTISER_TOS_NOT_ACCEPTED = 90
    ADVERTISER_NOT_ALLOWLISTED_FOR_THIRD_PARTY_PARTNER_DATA = 91
    USER_LIST_TYPE_NOT_SUPPORTED_FOR_ACCOUNT = 92
    INVALID_COMMERCE_PARTNER = 93
    CUSTOMER_NOT_ALLOWLISTED_FOR_COMMERCE_AUDIENCE = 94
    UNSUPPORTED_USER_LIST_UPLOAD_KEY_TYPES = 95
    UNSUPPORTED_INGESTED_USER_LIST_INFO_CONFIG = 96
    UNSUPPORTED_ACCOUNT_TYPES_FOR_USER_LIST_TYPE = 97
    UNSUPPORTED_ACCOUNT_TYPE_FOR_PARTNER_LINK = 98
    MEMBERSHIP_DURATION_TOO_LONG = 99
    INVALID_MERCHANT_ID = 100
    EU_POLITICAL_ADVERTISING_DECLARATION_REQUIRED = 101
    ACCOUNT_INELIGIBLE_FOR_STORE_SALES = 102
    INVALID_MERCHANT_FEED_LANGUAGE_CODE = 103
    INVALID_REGION_CODE = 104
    INVALID_SUBDIVISION_CODE = 107
    INVALID_SUBCONTINENT_CODE = 108
    INVALID_CONTINENT_CODE = 109
    INVALID_DEVICE_CATEGORY = 110
    BOTH_CLIENT_ID_AND_APP_INSTANCE_ID_NOT_ALLOWED = 111
    GOOGLE_ANALYTICS_SUBPROPERTY_OR_ROLLUP_PROPERTY_NOT_ALLOWED = 112
    THIRD_PARTY_USER_DATA_NOT_ALLOWED = 113
    INVALID_COUPON_CODE = 114
    EVENT_SOURCE_AND_DESTINATION_MISMATCH = 115
    DESTINATION_ACCOUNT_TYPE_MISMATCH = 116
    CUSTOM_VARIABLE_VALUE_CONTAINS_PII = 117
    CUSTOM_VARIABLE_NOT_ENABLED = 118
    INVALID_CUSTOM_VARIABLE_VALUE = 119
    CUSTOM_VARIABLE_NOT_FOUND = 120
    TOO_MANY_USERS = 121
    BASELINE_LOCATION_AUTO_DETECTION_FAILED = 122
    INSIGHTS_MISSING_FOR_DIMENSION = 123
    REQUIRED_PREREQUISITE_LINK_MISSING = 124
    INVALID_REMOVE_AS_OF_TIME = 125
    REQUEST_TOO_OLD = 126
    CONVERSION_ACTION_TOO_RECENTLY_CREATED = 127
    INVALID_AD_IDENTIFIER_FOR_ACCOUNT = 128


__all__ = tuple(sorted(__protobuf__.manifest))
