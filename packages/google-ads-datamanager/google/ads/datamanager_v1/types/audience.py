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

from google.ads.datamanager_v1.types import consent as gad_consent
from google.ads.datamanager_v1.types import user_data as gad_user_data

__protobuf__ = proto.module(
    package="google.ads.datamanager.v1",
    manifest={
        "AudienceMember",
        "PairData",
        "MobileData",
        "UserIdData",
        "PpidData",
        "CompositeData",
        "IpData",
        "GoogleUserIdData",
        "PartnerProvidedIdData",
    },
)


class AudienceMember(proto.Message):
    r"""The audience member to be operated on.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        destination_references (MutableSequence[str]):
            Optional. Defines which
            [Destination][google.ads.datamanager.v1.Destination] to send
            the audience member to.
        user_data (google.ads.datamanager_v1.types.UserData):
            User-provided data that identifies the user.

            This field is a member of `oneof`_ ``data``.
        pair_data (google.ads.datamanager_v1.types.PairData):
            `Publisher Advertiser Identity Reconciliation (PAIR)
            IDs <//support.google.com/admanager/answer/15067908>`__.

            This feature is only available to data partners.

            This field is a member of `oneof`_ ``data``.
        mobile_data (google.ads.datamanager_v1.types.MobileData):
            Data identifying the user's mobile devices.

            This field is a member of `oneof`_ ``data``.
        user_id_data (google.ads.datamanager_v1.types.UserIdData):
            Data related to unique identifiers for a
            user, as defined by the advertiser.

            This field is a member of `oneof`_ ``data``.
        ppid_data (google.ads.datamanager_v1.types.PpidData):
            Data related to publisher provided
            identifiers.
            This feature is only available to data partners.

            This field is a member of `oneof`_ ``data``.
        composite_data (google.ads.datamanager_v1.types.CompositeData):
            Group of multiple identifier types.

            This field is a member of `oneof`_ ``data``.
        google_user_id_data (google.ads.datamanager_v1.types.GoogleUserIdData):
            Encrypted Google User IDs.

            This field is a member of `oneof`_ ``data``.
        partner_provided_id_data (google.ads.datamanager_v1.types.PartnerProvidedIdData):
            Partner-provided identifiers.

            This field is a member of `oneof`_ ``data``.
        consent (google.ads.datamanager_v1.types.Consent):
            Optional. The consent setting for the user.
    """

    destination_references: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    user_data: gad_user_data.UserData = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="data",
        message=gad_user_data.UserData,
    )
    pair_data: "PairData" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="data",
        message="PairData",
    )
    mobile_data: "MobileData" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="data",
        message="MobileData",
    )
    user_id_data: "UserIdData" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="data",
        message="UserIdData",
    )
    ppid_data: "PpidData" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="data",
        message="PpidData",
    )
    composite_data: "CompositeData" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="data",
        message="CompositeData",
    )
    google_user_id_data: "GoogleUserIdData" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="data",
        message="GoogleUserIdData",
    )
    partner_provided_id_data: "PartnerProvidedIdData" = proto.Field(
        proto.MESSAGE,
        number=10,
        oneof="data",
        message="PartnerProvidedIdData",
    )
    consent: gad_consent.Consent = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gad_consent.Consent,
    )


class PairData(proto.Message):
    r"""`PAIR <//support.google.com/admanager/answer/15067908>`__ IDs for
    the audience. At least one PAIR ID is required.

    This feature is only available to data partners.

    Attributes:
        pair_ids (MutableSequence[str]):
            Required. Cleanroom-provided PII data, hashed with SHA256,
            and encrypted with an EC commutative cipher using publisher
            key for the
            `PAIR <(//support.google.com/admanager/answer/15067908)>`__
            user list. At most 10 ``pairIds`` can be provided in a
            single
            [AudienceMember][google.ads.datamanager.v1.AudienceMember].
    """

    pair_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class MobileData(proto.Message):
    r"""Mobile IDs for the audience. At least one mobile ID is
    required.

    Attributes:
        mobile_ids (MutableSequence[str]):
            Required. The list of mobile device IDs (Android advertising
            ID, iOS IDFA for Customer Match user lists and Android
            advertising ID, iOS IDFA, Xbox or Microsoft ID, Amazon Fire
            TV ID, Roku ID, Generic Device ID for basic user lists). At
            most 10 ``mobileIds`` can be provided in a single
            [AudienceMember][google.ads.datamanager.v1.AudienceMember].
    """

    mobile_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class UserIdData(proto.Message):
    r"""User id data holding the user id.

    Attributes:
        user_id (str):
            Required. A unique identifier for a user, as
            defined by the advertiser.
    """

    user_id: str = proto.Field(
        proto.STRING,
        number=1,
    )


class PpidData(proto.Message):
    r"""Publisher provided identifiers data holding the ppids. At
    least one ppid is required.

    This feature is only available to data partners.

    Attributes:
        ppids (MutableSequence[str]):
            Required. The list of publisher provided
            identifiers for a user.
    """

    ppids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class CompositeData(proto.Message):
    r"""Composite data holding identifiers and associated data for a user.
    At least one of ``user_data`` or ``ip_data`` is required.

    Attributes:
        user_data (google.ads.datamanager_v1.types.UserData):
            Optional. User-provided data that identifies
            the user.
        ip_data (MutableSequence[google.ads.datamanager_v1.types.IpData]):
            Optional. IP address data representing
            customer interaction used to build the audience.
    """

    user_data: gad_user_data.UserData = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gad_user_data.UserData,
    )
    ip_data: MutableSequence["IpData"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="IpData",
    )


class IpData(proto.Message):
    r"""IP address information for a user. We recommend including
    observe_start_time and observe_end_time to help improve Customer
    Match match rates.

    Attributes:
        ip_address (str):
            Required. IP address captured at the time of
            customer interaction. Accepts standard string
            formats for both IPv4 and IPv6.
        observe_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. First recorded interaction time
            from this IP address in a session.
        observe_end_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Last recorded interaction time from
            this IP address in a session.
    """

    ip_address: str = proto.Field(
        proto.STRING,
        number=1,
    )
    observe_start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    observe_end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class GoogleUserIdData(proto.Message):
    r"""Google user id data holding encrypted google user IDs. At
    least one google user ID is required.

    Attributes:
        google_user_ids (MutableSequence[str]):
            Required. The list of encrypted google user
            IDs.
    """

    google_user_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class PartnerProvidedIdData(proto.Message):
    r"""Partner-provided data holding the partner-provided
    identifiers. At least one partner-provided identifier is
    required.

    Attributes:
        partner_provided_ids (MutableSequence[str]):
            Required. The list of partner-provided
            identifiers.
    """

    partner_provided_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
