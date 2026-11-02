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
import proto  # type: ignore

from google.ads.datamanager_v1.types import cart_data as gad_cart_data
from google.ads.datamanager_v1.types import consent as gad_consent
from google.ads.datamanager_v1.types import (
    device_info,
    encrypted_user_id,
    experimental_field,
)
from google.ads.datamanager_v1.types import user_data as gad_user_data
from google.ads.datamanager_v1.types import user_properties as gad_user_properties

__protobuf__ = proto.module(
    package="google.ads.datamanager.v1",
    manifest={
        "EventSource",
        "Event",
        "AdIdentifiers",
        "CustomVariable",
        "EventParameter",
        "EventLocation",
    },
)


class EventSource(proto.Enum):
    r"""The source of the event.

    Values:
        EVENT_SOURCE_UNSPECIFIED (0):
            Unspecified EventSource. Should never be
            used.
        WEB (1):
            The event was generated from a web browser.
        APP (2):
            The event was generated from an app.
        IN_STORE (3):
            The event was generated from an in-store
            transaction.
        PHONE (4):
            The event was generated from a phone call.
        MESSAGE (6):
            The event was generated from a message.
        OTHER (5):
            The event was generated from other sources.
    """

    EVENT_SOURCE_UNSPECIFIED = 0
    WEB = 1
    APP = 2
    IN_STORE = 3
    PHONE = 4
    MESSAGE = 6
    OTHER = 5


class Event(proto.Message):
    r"""An event representing a user interaction with an advertiser's
    website or app.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        destination_references (MutableSequence[str]):
            Optional. Reference string used to determine the
            destination. If empty, the event will be sent to all
            [destinations][google.ads.datamanager.v1.IngestEventsRequest.destinations]
            in the request.
        transaction_id (str):
            Optional. The unique identifier for this
            event. Required for events sent as an additional
            data source for tag conversions.
        event_timestamp (google.protobuf.timestamp_pb2.Timestamp):
            Required. The time the event occurred.
        last_updated_timestamp (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The last time the event was
            updated.
        user_data (google.ads.datamanager_v1.types.UserData):
            Optional. Pieces of user provided data,
            representing the user the event is associated
            with.
        consent (google.ads.datamanager_v1.types.Consent):
            Optional. Information about whether the
            associated user has provided different types of
            consent.
        ad_identifiers (google.ads.datamanager_v1.types.AdIdentifiers):
            Optional. Identifiers and other information
            used to match the conversion event with other
            online activity (such as ad clicks).
        currency (str):
            Optional. The currency code associated with
            all monetary values within this event.
        conversion_value (float):
            Optional. The conversion value associated
            with the event, for value-based conversions.

            This field is a member of `oneof`_ ``_conversion_value``.
        conversion_count (float):
            Optional. The conversion quantity associated
            with the event, for counting-based conversions.

            This field is a member of `oneof`_ ``_conversion_count``.
        event_source (google.ads.datamanager_v1.types.EventSource):
            Optional. Signal for where the event happened
            (web, app, in-store, etc.).
        event_device_info (google.ads.datamanager_v1.types.DeviceInfo):
            Optional. Information gathered about the
            device being used (if any) when the event
            happened.
        cart_data (google.ads.datamanager_v1.types.CartData):
            Optional. Information about the transaction
            and items associated with the event.
        custom_variables (MutableSequence[google.ads.datamanager_v1.types.CustomVariable]):
            Optional. Additional key/value pair
            information to send to the conversion containers
            (conversion action or FL activity).
        experimental_fields (MutableSequence[google.ads.datamanager_v1.types.ExperimentalField]):
            Optional. A list of key/value pairs for
            experimental fields that may eventually be
            promoted to be part of the API.
        user_properties (google.ads.datamanager_v1.types.UserProperties):
            Optional. Advertiser-assessed information
            about the user at the time that the event
            happened.
        event_name (str):
            Optional. The name of the event. Required for
            GA4 events.
        client_id (str):
            Optional. A unique identifier for the user
            instance of a web client for this GA4 web
            stream.
        user_id (str):
            Optional. A unique identifier for a user, as
            defined by the advertiser.
        additional_event_parameters (MutableSequence[google.ads.datamanager_v1.types.EventParameter]):
            Optional. A bucket of any `event
            parameters <https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference/events>`__
            to be included within the event that were not already
            specified using other structured fields.
        third_party_user_data (google.ads.datamanager_v1.types.UserData):
            Optional. The same type of data provided in user_data, but
            explicitly flagged as being provided as owned by a
            third-party and not first-party advertiser data.
        event_location (google.ads.datamanager_v1.types.EventLocation):
            Optional. Information gathered about the
            location of the user when this event occurred.
        app_instance_id (str):
            Optional. A unique identifier for the user
            instance of an app client for this GA4 app
            stream.
    """

    destination_references: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    transaction_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    event_timestamp: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    last_updated_timestamp: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    user_data: gad_user_data.UserData = proto.Field(
        proto.MESSAGE,
        number=5,
        message=gad_user_data.UserData,
    )
    consent: gad_consent.Consent = proto.Field(
        proto.MESSAGE,
        number=6,
        message=gad_consent.Consent,
    )
    ad_identifiers: "AdIdentifiers" = proto.Field(
        proto.MESSAGE,
        number=7,
        message="AdIdentifiers",
    )
    currency: str = proto.Field(
        proto.STRING,
        number=8,
    )
    conversion_value: float = proto.Field(
        proto.DOUBLE,
        number=9,
        optional=True,
    )
    conversion_count: float = proto.Field(
        proto.DOUBLE,
        number=23,
        optional=True,
    )
    event_source: "EventSource" = proto.Field(
        proto.ENUM,
        number=10,
        enum="EventSource",
    )
    event_device_info: device_info.DeviceInfo = proto.Field(
        proto.MESSAGE,
        number=11,
        message=device_info.DeviceInfo,
    )
    cart_data: gad_cart_data.CartData = proto.Field(
        proto.MESSAGE,
        number=12,
        message=gad_cart_data.CartData,
    )
    custom_variables: MutableSequence["CustomVariable"] = proto.RepeatedField(
        proto.MESSAGE,
        number=13,
        message="CustomVariable",
    )
    experimental_fields: MutableSequence[experimental_field.ExperimentalField] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=14,
            message=experimental_field.ExperimentalField,
        )
    )
    user_properties: gad_user_properties.UserProperties = proto.Field(
        proto.MESSAGE,
        number=15,
        message=gad_user_properties.UserProperties,
    )
    event_name: str = proto.Field(
        proto.STRING,
        number=16,
    )
    client_id: str = proto.Field(
        proto.STRING,
        number=17,
    )
    user_id: str = proto.Field(
        proto.STRING,
        number=18,
    )
    additional_event_parameters: MutableSequence["EventParameter"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=19,
            message="EventParameter",
        )
    )
    third_party_user_data: gad_user_data.UserData = proto.Field(
        proto.MESSAGE,
        number=20,
        message=gad_user_data.UserData,
    )
    event_location: "EventLocation" = proto.Field(
        proto.MESSAGE,
        number=21,
        message="EventLocation",
    )
    app_instance_id: str = proto.Field(
        proto.STRING,
        number=22,
    )


class AdIdentifiers(proto.Message):
    r"""Identifiers and other information used to match the
    conversion event with other online activity (such as ad clicks).

    Attributes:
        session_attributes (str):
            Optional. Session attributes for event
            attribution and modeling.
        gclid (str):
            Optional. The Google click ID (gclid)
            associated with this event.
        gbraid (str):
            Optional. The click identifier for clicks
            associated with app events and originating from
            iOS devices starting with iOS14.
        wbraid (str):
            Optional. The click identifier for clicks
            associated with web events and originating from
            iOS devices starting with iOS14.
        landing_page_device_info (google.ads.datamanager_v1.types.DeviceInfo):
            Optional. Information gathered about the
            device being used (if any) at the time of
            landing onto the advertiser’s site after
            interacting with the ad.
        mobile_device_id (str):
            Optional. The mobile identifier for
            advertisers. This would be IDFA on iOS, AdID on
            Android, or other platforms’ identifiers for
            advertisers.
        dclid (str):
            Optional. The display click ID associated
            with this event.
        impression_id (str):
            Optional. The impression ID associated with
            this event.
        match_id (str):
            Optional. The match ID field used to join
            this event with a previous event.
        encrypted_user_ids (MutableSequence[google.ads.datamanager_v1.types.EncryptedUserId]):
            Optional. Any number of encrypted user IDs.
        ppid (str):
            Optional. A unique identifier for an
            authenticated user (signed-in), as defined by
            the publisher.
        visitor_ppid (str):
            Optional. A unique identifier for an
            unauthenticated user (user who is not
            signed-in), as defined by the publisher.
    """

    session_attributes: str = proto.Field(
        proto.STRING,
        number=1,
    )
    gclid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    gbraid: str = proto.Field(
        proto.STRING,
        number=3,
    )
    wbraid: str = proto.Field(
        proto.STRING,
        number=4,
    )
    landing_page_device_info: device_info.DeviceInfo = proto.Field(
        proto.MESSAGE,
        number=5,
        message=device_info.DeviceInfo,
    )
    mobile_device_id: str = proto.Field(
        proto.STRING,
        number=6,
    )
    dclid: str = proto.Field(
        proto.STRING,
        number=7,
    )
    impression_id: str = proto.Field(
        proto.STRING,
        number=8,
    )
    match_id: str = proto.Field(
        proto.STRING,
        number=9,
    )
    encrypted_user_ids: MutableSequence[encrypted_user_id.EncryptedUserId] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=10,
            message=encrypted_user_id.EncryptedUserId,
        )
    )
    ppid: str = proto.Field(
        proto.STRING,
        number=11,
    )
    visitor_ppid: str = proto.Field(
        proto.STRING,
        number=12,
    )


class CustomVariable(proto.Message):
    r"""Custom variable for ads conversions.

    Attributes:
        variable (str):
            Optional. The name of the custom variable to
            set. If the variable is not found for the given
            destination, it will be ignored.
        value (str):
            Optional. The value to store for the custom
            variable.
        destination_references (MutableSequence[str]):
            Optional. Reference string used to determine which of the
            [Event.destination_references][google.ads.datamanager.v1.Event.destination_references]
            the custom variable should be sent to. If empty, the
            [Event.destination_references][google.ads.datamanager.v1.Event.destination_references]
            will be used.
    """

    variable: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: str = proto.Field(
        proto.STRING,
        number=2,
    )
    destination_references: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class EventParameter(proto.Message):
    r"""Event parameter for GA4 events.

    Attributes:
        parameter_name (str):
            Required. The name of the parameter to use.
        value (str):
            Required. The string representation of the
            value of the parameter to set.
    """

    parameter_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: str = proto.Field(
        proto.STRING,
        number=2,
    )


class EventLocation(proto.Message):
    r"""The location where the event occurred.

    Attributes:
        store_id (str):
            Optional. Required for Store Sales. The
            identifier to represent a physical store where
            the event happened.
        city (str):
            Optional. The name of the city where the
            event occurred.
        subdivision_code (str):
            Optional. The ISO 3166-2 subdivision code
            where the event occurred.
        region_code (str):
            Optional. The 2-letter CLDR region code of
            the user's address.
        subcontinent_code (str):
            Optional. The subcontinent code in UN M49
            format where the event occurred.
        continent_code (str):
            Optional. The continent code in UN M49 format
            where the event occurred.
    """

    store_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    city: str = proto.Field(
        proto.STRING,
        number=2,
    )
    subdivision_code: str = proto.Field(
        proto.STRING,
        number=3,
    )
    region_code: str = proto.Field(
        proto.STRING,
        number=4,
    )
    subcontinent_code: str = proto.Field(
        proto.STRING,
        number=5,
    )
    continent_code: str = proto.Field(
        proto.STRING,
        number=6,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
