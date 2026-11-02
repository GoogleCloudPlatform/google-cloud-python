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
        "ProcessingErrorReason",
        "ProcessingWarningReason",
        "WarningReason",
        "ErrorInfo",
        "ErrorCount",
        "WarningInfo",
        "WarningCount",
        "FieldWarning",
    },
)


class ProcessingErrorReason(proto.Enum):
    r"""The processing error reason.
    New reasons may be added in the future.

    Values:
        PROCESSING_ERROR_REASON_UNSPECIFIED (0):
            The processing error reason is unknown.
        PROCESSING_ERROR_REASON_INVALID_CUSTOM_VARIABLE (1):
            The custom variable is invalid.
        PROCESSING_ERROR_REASON_CUSTOM_VARIABLE_NOT_ENABLED (2):
            The status of the custom variable is not
            enabled.
        PROCESSING_ERROR_REASON_EVENT_TOO_OLD (3):
            The conversion is older than max supported
            age.
        PROCESSING_ERROR_REASON_DENIED_CONSENT (4):
            The ad user data is denied, either by the
            user or in the advertiser default settings.
        PROCESSING_ERROR_REASON_NO_CONSENT (5):
            Advertiser did not give 3P consent for the
            Ads core platform services.
        PROCESSING_ERROR_REASON_UNKNOWN_CONSENT (6):
            The overall consent (determined from row
            level consent, request level consent, and
            account settings) could not be determined for
            this user
        PROCESSING_ERROR_REASON_DUPLICATE_GCLID (7):
            A conversion with the same GCLID and
            conversion time already exists in the system.
        PROCESSING_ERROR_REASON_DUPLICATE_TRANSACTION_ID (8):
            A conversion with the same order id and
            conversion action combination was already
            uploaded.
        PROCESSING_ERROR_REASON_INVALID_GBRAID (9):
            The gbraid could not be decoded.
        PROCESSING_ERROR_REASON_INVALID_GCLID (10):
            The google click ID could not be decoded.
        PROCESSING_ERROR_REASON_INVALID_MERCHANT_ID (11):
            Merchant id contains non-digit characters.
        PROCESSING_ERROR_REASON_INVALID_WBRAID (12):
            The wbraid could not be decoded.
        PROCESSING_ERROR_REASON_INTERNAL_ERROR (13):
            Internal error.
        PROCESSING_ERROR_REASON_DESTINATION_ACCOUNT_ENHANCED_CONVERSIONS_TERMS_NOT_SIGNED (14):
            Enhanced conversions terms are not signed in
            the destination account.
        PROCESSING_ERROR_REASON_INVALID_EVENT (15):
            The event is invalid.
        PROCESSING_ERROR_REASON_INSUFFICIENT_MATCHED_TRANSACTIONS (16):
            The matched transactions are less than the
            minimum threshold.
        PROCESSING_ERROR_REASON_INSUFFICIENT_TRANSACTIONS (17):
            The transactions are less than the minimum
            threshold.
        PROCESSING_ERROR_REASON_INVALID_FORMAT (18):
            The event has format error.
        PROCESSING_ERROR_REASON_DECRYPTION_ERROR (19):
            The event has a decryption error.
        PROCESSING_ERROR_REASON_DEK_DECRYPTION_ERROR (20):
            The DEK failed to be decrypted.
        PROCESSING_ERROR_REASON_INVALID_WIP (21):
            The WIP is formatted incorrectly or the WIP
            does not exist.
        PROCESSING_ERROR_REASON_INVALID_KEK (22):
            The KEK cannot decrypt data because it is the
            wrong KEK, or it does not exist.
        PROCESSING_ERROR_REASON_WIP_AUTH_FAILED (23):
            The WIP could not be used because it was
            rejected by its attestation condition.
        PROCESSING_ERROR_REASON_KEK_PERMISSION_DENIED (24):
            The system did not have the permissions
            needed to access the KEK.
        PROCESSING_ERROR_REASON_AWS_AUTH_FAILED (27):
            The system failed to authenticate with AWS.
        PROCESSING_ERROR_REASON_USER_IDENTIFIER_DECRYPTION_ERROR (25):
            Failed to decrypt the
            [UserIdentifier][google.ads.datamanager.v1.UserIdentifier]
            data using the DEK.
        PROCESSING_ERROR_OPERATING_ACCOUNT_MISMATCH_FOR_AD_IDENTIFIER (26):
            The user attempted to ingest events with an
            ad identifier that isn't from the operating
            account's ads.
        PROCESSING_ERROR_REASON_ONE_PER_CLICK_CONVERSION_ACTION_NOT_PERMITTED_WITH_BRAID (28):
            One-per-click conversion actions cannot be
            used with BRAIDs.
        PROCESSING_ERROR_REASON_MATCH_ID_NOT_FOUND (29):
            The match ID can not be found.
        PROCESSING_ERROR_REASON_USER_ID_NOT_FOUND_FOR_MATCH_ID (30):
            The user ID can not be found for the match
            ID.
        PROCESSING_ERROR_REASON_USER_ID_NOT_FOUND_FOR_GCLID (31):
            The user ID can not be found for the GCLID.
        PROCESSING_ERROR_REASON_USER_ID_NOT_FOUND_FOR_DCLID (32):
            The user ID can not be found for the DCLID.
        PROCESSING_ERROR_REASON_INVALID_AD_IDENTIFIERS (33):
            There are ad identifiers that are invalid.
        PROCESSING_ERROR_REASON_INVALID_MOBILE_ID_FORMAT (34):
            The mobile ID format is invalid.
        PROCESSING_ERROR_REASON_ORIGINAL_CONVERSIONS_NOT_FOUND (35):
            The original conversions can't be found.
        PROCESSING_ERROR_REASON_EVENT_ID_DECODE_ERROR (36):
            The event ID (dclid or impression ID) cannot
            be decoded.
        PROCESSING_ERROR_REASON_USER_ID_NOT_FOUND_FOR_IMPRESSION_ID (37):
            The user ID cannot be found for the given
            impression ID.
        PROCESSING_ERROR_REASON_USER_ID_NOT_FOUND (38):
            The user ID cannot be found.
        PROCESSING_ERROR_REASON_CONVERSION_PRECEDES_CLICK (39):
            The event timestamp on the event was earlier
            than the associated click.
        PROCESSING_ERROR_REASON_TOO_RECENT_CLICK (40):
            The click occurred too recently.
        PROCESSING_ERROR_REASON_INVALID_CLICK (41):
            The event can't be attributed to a click
            (GCLID). This may be because the click did not
            come from a Google Ads campaign, for example.
        PROCESSING_ERROR_REASON_INVALID_OPERATING_ACCOUNT_FOR_CLICK (42):
            The click from the event isn't associated with the
            [``operating_account``][google.ads.datamanager.v1.Destination.operating_account]
            of the destination.
        PROCESSING_ERROR_REASON_CLICK_NOT_FOUND (43):
            A corresponding click can't be found that
            matches the provided attributes.
        PROCESSING_ERROR_REASON_EXTERNAL_ATTRIBUTION_DATA_MISSING (44):
            External attribution data is missing. Sending
            events to a destination for an external
            attribution conversion action isn't supported.
    """

    PROCESSING_ERROR_REASON_UNSPECIFIED = 0
    PROCESSING_ERROR_REASON_INVALID_CUSTOM_VARIABLE = 1
    PROCESSING_ERROR_REASON_CUSTOM_VARIABLE_NOT_ENABLED = 2
    PROCESSING_ERROR_REASON_EVENT_TOO_OLD = 3
    PROCESSING_ERROR_REASON_DENIED_CONSENT = 4
    PROCESSING_ERROR_REASON_NO_CONSENT = 5
    PROCESSING_ERROR_REASON_UNKNOWN_CONSENT = 6
    PROCESSING_ERROR_REASON_DUPLICATE_GCLID = 7
    PROCESSING_ERROR_REASON_DUPLICATE_TRANSACTION_ID = 8
    PROCESSING_ERROR_REASON_INVALID_GBRAID = 9
    PROCESSING_ERROR_REASON_INVALID_GCLID = 10
    PROCESSING_ERROR_REASON_INVALID_MERCHANT_ID = 11
    PROCESSING_ERROR_REASON_INVALID_WBRAID = 12
    PROCESSING_ERROR_REASON_INTERNAL_ERROR = 13
    PROCESSING_ERROR_REASON_DESTINATION_ACCOUNT_ENHANCED_CONVERSIONS_TERMS_NOT_SIGNED = 14
    PROCESSING_ERROR_REASON_INVALID_EVENT = 15
    PROCESSING_ERROR_REASON_INSUFFICIENT_MATCHED_TRANSACTIONS = 16
    PROCESSING_ERROR_REASON_INSUFFICIENT_TRANSACTIONS = 17
    PROCESSING_ERROR_REASON_INVALID_FORMAT = 18
    PROCESSING_ERROR_REASON_DECRYPTION_ERROR = 19
    PROCESSING_ERROR_REASON_DEK_DECRYPTION_ERROR = 20
    PROCESSING_ERROR_REASON_INVALID_WIP = 21
    PROCESSING_ERROR_REASON_INVALID_KEK = 22
    PROCESSING_ERROR_REASON_WIP_AUTH_FAILED = 23
    PROCESSING_ERROR_REASON_KEK_PERMISSION_DENIED = 24
    PROCESSING_ERROR_REASON_AWS_AUTH_FAILED = 27
    PROCESSING_ERROR_REASON_USER_IDENTIFIER_DECRYPTION_ERROR = 25
    PROCESSING_ERROR_OPERATING_ACCOUNT_MISMATCH_FOR_AD_IDENTIFIER = 26
    PROCESSING_ERROR_REASON_ONE_PER_CLICK_CONVERSION_ACTION_NOT_PERMITTED_WITH_BRAID = (
        28
    )
    PROCESSING_ERROR_REASON_MATCH_ID_NOT_FOUND = 29
    PROCESSING_ERROR_REASON_USER_ID_NOT_FOUND_FOR_MATCH_ID = 30
    PROCESSING_ERROR_REASON_USER_ID_NOT_FOUND_FOR_GCLID = 31
    PROCESSING_ERROR_REASON_USER_ID_NOT_FOUND_FOR_DCLID = 32
    PROCESSING_ERROR_REASON_INVALID_AD_IDENTIFIERS = 33
    PROCESSING_ERROR_REASON_INVALID_MOBILE_ID_FORMAT = 34
    PROCESSING_ERROR_REASON_ORIGINAL_CONVERSIONS_NOT_FOUND = 35
    PROCESSING_ERROR_REASON_EVENT_ID_DECODE_ERROR = 36
    PROCESSING_ERROR_REASON_USER_ID_NOT_FOUND_FOR_IMPRESSION_ID = 37
    PROCESSING_ERROR_REASON_USER_ID_NOT_FOUND = 38
    PROCESSING_ERROR_REASON_CONVERSION_PRECEDES_CLICK = 39
    PROCESSING_ERROR_REASON_TOO_RECENT_CLICK = 40
    PROCESSING_ERROR_REASON_INVALID_CLICK = 41
    PROCESSING_ERROR_REASON_INVALID_OPERATING_ACCOUNT_FOR_CLICK = 42
    PROCESSING_ERROR_REASON_CLICK_NOT_FOUND = 43
    PROCESSING_ERROR_REASON_EXTERNAL_ATTRIBUTION_DATA_MISSING = 44


class ProcessingWarningReason(proto.Enum):
    r"""The processing warning reason.

    Values:
        PROCESSING_WARNING_REASON_UNSPECIFIED (0):
            The processing warning reason is unknown.
        PROCESSING_WARNING_REASON_KEK_PERMISSION_DENIED (1):
            The system did not have the permissions
            needed to access the KEK.
        PROCESSING_WARNING_REASON_DEK_DECRYPTION_ERROR (2):
            The DEK failed to be decrypted.
        PROCESSING_WARNING_REASON_DECRYPTION_ERROR (3):
            The event has a decryption error.
        PROCESSING_WARNING_REASON_WIP_AUTH_FAILED (4):
            The WIP could not be used because it was
            rejected by its attestation condition.
        PROCESSING_WARNING_REASON_INVALID_WIP (5):
            The WIP is formatted incorrectly or the WIP
            does not exist.
        PROCESSING_WARNING_REASON_INVALID_KEK (6):
            The KEK cannot decrypt data because it is the
            wrong KEK, or it does not exist.
        PROCESSING_WARNING_REASON_USER_IDENTIFIER_DECRYPTION_ERROR (7):
            Failed to decrypt the
            [UserIdentifier][google.ads.datamanager.v1.UserIdentifier]
            data using the DEK.
        PROCESSING_WARNING_REASON_INTERNAL_ERROR (8):
            Internal error.
        PROCESSING_WARNING_REASON_AWS_AUTH_FAILED (9):
            The system failed to authenticate with AWS.
    """

    PROCESSING_WARNING_REASON_UNSPECIFIED = 0
    PROCESSING_WARNING_REASON_KEK_PERMISSION_DENIED = 1
    PROCESSING_WARNING_REASON_DEK_DECRYPTION_ERROR = 2
    PROCESSING_WARNING_REASON_DECRYPTION_ERROR = 3
    PROCESSING_WARNING_REASON_WIP_AUTH_FAILED = 4
    PROCESSING_WARNING_REASON_INVALID_WIP = 5
    PROCESSING_WARNING_REASON_INVALID_KEK = 6
    PROCESSING_WARNING_REASON_USER_IDENTIFIER_DECRYPTION_ERROR = 7
    PROCESSING_WARNING_REASON_INTERNAL_ERROR = 8
    PROCESSING_WARNING_REASON_AWS_AUTH_FAILED = 9


class WarningReason(proto.Enum):
    r"""Reasons for non-blocking warnings returned during ingestion.

    Values:
        WARNING_REASON_UNSPECIFIED (0):
            Unspecified warning reason.
        WARNING_REASON_CUSTOM_VARIABLE_NOT_ENABLED (1):
            A custom variable in
            [``custom_variables``][google.ads.datamanager.v1.Event.custom_variables]
            is not enabled in the account.
        WARNING_REASON_CUSTOM_VARIABLE_NOT_PREDEFINED (2):
            A custom variable value in
            [``custom_variables``][google.ads.datamanager.v1.Event.custom_variables]
            is not among the predefined allowed values configured for
            the custom variable on the destination account.
        WARNING_REASON_CART_DATA_NOT_SUPPORTED_WITH_GBRAID_OR_WBRAID (3):
            The
            [``cart_data``][google.ads.datamanager.v1.Event.cart_data]
            is not supported with
            [``gbraid``][google.ads.datamanager.v1.AdIdentifiers.gbraid]
            or
            [``wbraid``][google.ads.datamanager.v1.AdIdentifiers.wbraid].
        WARNING_REASON_CART_DATA_ITEM_MERCHANT_PRODUCT_ID_MISSING (4):
            The
            [``merchant_product_id``][google.ads.datamanager.v1.Item.merchant_product_id]
            is missing in the cart item.
        WARNING_REASON_CART_DATA_ITEM_UNIT_PRICE_MISSING (5):
            The
            [``unit_price``][google.ads.datamanager.v1.Item.unit_price]
            is missing in the cart item.
        WARNING_REASON_GENERIC (6):
            Generic warning reason for issues that do not
            fit into other specific categories.
        WARNING_REASON_INVALID_CLIENT_ID (7):
            The
            [``client_id``][google.ads.datamanager.v1.Event.client_id]
            is invalid.
        WARNING_REASON_INVALID_SUBDIVISION_CODE (8):
            The
            [``subdivision_code``][google.ads.datamanager.v1.EventLocation.subdivision_code]
            is invalid.
        WARNING_REASON_INVALID_REGION_CODE (9):
            The
            [``region_code``][google.ads.datamanager.v1.EventLocation.region_code]
            is invalid.
        WARNING_REASON_INVALID_SUBCONTINENT_CODE (10):
            The
            [``subcontinent_code``][google.ads.datamanager.v1.EventLocation.subcontinent_code]
            is invalid.
        WARNING_REASON_INVALID_CONTINENT_CODE (11):
            The
            [``continent_code``][google.ads.datamanager.v1.EventLocation.continent_code]
            is invalid.
        WARNING_REASON_INVALID_DEVICE_CATEGORY (12):
            The device
            [``category``][google.ads.datamanager.v1.DeviceInfo.category]
            is invalid.
        WARNING_REASON_INVALID_DEVICE_SCREEN_RESOLUTION (13):
            The device
            [``screen_height``][google.ads.datamanager.v1.DeviceInfo.screen_height]
            or
            [``screen_width``][google.ads.datamanager.v1.DeviceInfo.screen_width]
            is invalid.
        WARNING_REASON_INVALID_MERCHANT_ID (14):
            The
            [``merchant_id``][google.ads.datamanager.v1.CartData.merchant_id]
            is invalid.
    """

    WARNING_REASON_UNSPECIFIED = 0
    WARNING_REASON_CUSTOM_VARIABLE_NOT_ENABLED = 1
    WARNING_REASON_CUSTOM_VARIABLE_NOT_PREDEFINED = 2
    WARNING_REASON_CART_DATA_NOT_SUPPORTED_WITH_GBRAID_OR_WBRAID = 3
    WARNING_REASON_CART_DATA_ITEM_MERCHANT_PRODUCT_ID_MISSING = 4
    WARNING_REASON_CART_DATA_ITEM_UNIT_PRICE_MISSING = 5
    WARNING_REASON_GENERIC = 6
    WARNING_REASON_INVALID_CLIENT_ID = 7
    WARNING_REASON_INVALID_SUBDIVISION_CODE = 8
    WARNING_REASON_INVALID_REGION_CODE = 9
    WARNING_REASON_INVALID_SUBCONTINENT_CODE = 10
    WARNING_REASON_INVALID_CONTINENT_CODE = 11
    WARNING_REASON_INVALID_DEVICE_CATEGORY = 12
    WARNING_REASON_INVALID_DEVICE_SCREEN_RESOLUTION = 13
    WARNING_REASON_INVALID_MERCHANT_ID = 14


class ErrorInfo(proto.Message):
    r"""Error counts for each type of error.

    Attributes:
        error_counts (MutableSequence[google.ads.datamanager_v1.types.ErrorCount]):
            A list of errors and counts per error reason.
            May not be populated in all cases.
    """

    error_counts: MutableSequence["ErrorCount"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ErrorCount",
    )


class ErrorCount(proto.Message):
    r"""The error count for a given error reason.

    Attributes:
        record_count (int):
            The count of records that failed to upload
            for a given reason.
        reason (google.ads.datamanager_v1.types.ProcessingErrorReason):
            The error reason of the failed records.
    """

    record_count: int = proto.Field(
        proto.INT64,
        number=1,
    )
    reason: "ProcessingErrorReason" = proto.Field(
        proto.ENUM,
        number=2,
        enum="ProcessingErrorReason",
    )


class WarningInfo(proto.Message):
    r"""Warning counts for each type of warning.

    Attributes:
        warning_counts (MutableSequence[google.ads.datamanager_v1.types.WarningCount]):
            A list of warnings and counts per warning
            reason.
    """

    warning_counts: MutableSequence["WarningCount"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="WarningCount",
    )


class WarningCount(proto.Message):
    r"""The warning count for a given warning reason.

    Attributes:
        record_count (int):
            The count of records that have a warning.
        reason (google.ads.datamanager_v1.types.ProcessingWarningReason):
            The warning reason.
    """

    record_count: int = proto.Field(
        proto.INT64,
        number=1,
    )
    reason: "ProcessingWarningReason" = proto.Field(
        proto.ENUM,
        number=2,
        enum="ProcessingWarningReason",
    )


class FieldWarning(proto.Message):
    r"""Detailed row-level warning with field paths.

    Attributes:
        reason (google.ads.datamanager_v1.types.WarningReason):
            The warning reason.
        description (str):
            The detailed warning message describing the
            issue.
        field (str):
            The field path that triggered the warning. Uses the same
            format as
            [google.rpc.BadRequest.FieldViolation.field][google.rpc.BadRequest.FieldViolation.field].
    """

    reason: "WarningReason" = proto.Field(
        proto.ENUM,
        number=1,
        enum="WarningReason",
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    field: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
