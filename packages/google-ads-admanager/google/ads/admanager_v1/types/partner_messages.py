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

from google.ads.admanager_v1.types import applied_label, company_enums

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "Partner",
    },
)


class Partner(proto.Message):
    r"""The [Partner][google.ads.admanager.v1.Partner] resource.

    Represents a publishing partner with established agreements to share
    inventory and revenue based on assignments.

    For more information, see [Add publishing partner assignments]
    (https://support.google.com/admanager/answer/7032752).


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the
            [Partner][google.ads.admanager.v1.Partner]. Format:
            ``networks/{network_code}/partners/{partner_id}``
        display_name (str):
            Required. The display name of the
            [Partner][google.ads.admanager.v1.Partner].

            This field is a member of `oneof`_ ``_display_name``.
        address (str):
            Optional. The address for the
            [Partner][google.ads.admanager.v1.Partner].

            This value has a maximum length of 1024 characters.

            This field is a member of `oneof`_ ``_address``.
        email (str):
            Optional. The email for the
            [Partner][google.ads.admanager.v1.Partner].

            This value has a maximum length of 128 characters.

            This field is a member of `oneof`_ ``_email``.
        fax (str):
            Optional. The fax number for the
            [Partner][google.ads.admanager.v1.Partner].

            This value has a maximum length of 63 characters.

            This field is a member of `oneof`_ ``_fax``.
        phone (str):
            Optional. The phone number for the
            [Partner][google.ads.admanager.v1.Partner].

            This value has a maximum length of 63 characters.

            This field is a member of `oneof`_ ``_phone``.
        external_id (str):
            Optional. The external ID for the
            [Partner][google.ads.admanager.v1.Partner].

            This value has a maximum length of 255 characters.

            This field is a member of `oneof`_ ``_external_id``.
        comment (str):
            Optional. Comments about the
            [Partner][google.ads.admanager.v1.Partner].

            This value has a maximum length of 1024 characters.

            This field is a member of `oneof`_ ``_comment``.
        applied_labels (MutableSequence[google.ads.admanager_v1.types.AppliedLabel]):
            Optional. The labels that are directly applied to the
            [Partner][google.ads.admanager.v1.Partner].
        primary_contact (str):
            Optional. The resource names of primary Contact of the
            [Partner][google.ads.admanager.v1.Partner]. Format:
            "networks/{network_code}/contacts/{contact_id}".

            This field is a member of `oneof`_ ``_primary_contact``.
        applied_teams (MutableSequence[str]):
            Optional. The resource names of Teams that are directly
            associated with the
            [Partner][google.ads.admanager.v1.Partner]. Format:
            "networks/{network_code}/teams/{team_id}".
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the
            [Partner][google.ads.admanager.v1.Partner] was last updated.
        credit_status (google.ads.admanager_v1.types.CompanyCreditStatusEnum.CompanyCreditStatus):
            Optional. The credit status of the
            [Partner][google.ads.admanager.v1.Partner].

            This attribute defaults to
            [CompanyCreditStatusEnum.CompanyCreditStatus.ACTIVE][google.ads.admanager.v1.CompanyCreditStatusEnum.CompanyCreditStatus.ACTIVE]
            if basic settings are enabled and
            [CompanyCreditStatusEnum.CompanyCreditStatus.ON_HOLD][google.ads.admanager.v1.CompanyCreditStatusEnum.CompanyCreditStatus.ON_HOLD]
            if advance settings are enabled.

            This field is a member of `oneof`_ ``_credit_status``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    address: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    email: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    fax: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    phone: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )
    external_id: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )
    comment: str = proto.Field(
        proto.STRING,
        number=9,
        optional=True,
    )
    applied_labels: MutableSequence[applied_label.AppliedLabel] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message=applied_label.AppliedLabel,
    )
    primary_contact: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )
    applied_teams: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=13,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=15,
        message=timestamp_pb2.Timestamp,
    )
    credit_status: company_enums.CompanyCreditStatusEnum.CompanyCreditStatus = (
        proto.Field(
            proto.ENUM,
            number=16,
            optional=True,
            enum=company_enums.CompanyCreditStatusEnum.CompanyCreditStatus,
        )
    )


__all__ = tuple(sorted(__protobuf__.manifest))
