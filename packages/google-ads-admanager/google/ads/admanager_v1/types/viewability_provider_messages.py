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

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "ViewabilityProvider",
    },
)


class ViewabilityProvider(proto.Message):
    r"""The
    [ViewabilityProvider][google.ads.admanager.v1.ViewabilityProvider]
    resource.

    Represents a third-party company used to measure creative
    viewability.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the
            [ViewabilityProvider][google.ads.admanager.v1.ViewabilityProvider].
            Format:
            ``networks/{network_code}/viewabilityProviders/{viewability_provider}``
        display_name (str):
            Required. The display name of the
            [ViewabilityProvider][google.ads.admanager.v1.ViewabilityProvider].

            This field is a member of `oneof`_ ``_display_name``.
        vendor_key (str):
            Required. The key for the
            [ViewabilityProvider][google.ads.admanager.v1.ViewabilityProvider].

            This field is a member of `oneof`_ ``_vendor_key``.
        verification_script_url (str):
            Required. The URL that hosts the verification script for the
            [ViewabilityProvider][google.ads.admanager.v1.ViewabilityProvider].

            This field is a member of `oneof`_ ``_verification_script_url``.
        verification_script_url_parameters (str):
            Optional. The URL parameters that will be
            passed to the verification script.

            This field is a member of `oneof`_ ``_verification_script_url_parameters``.
        rejection_tracker_url (str):
            Optional. The URL that should be pinged if
            the verification script cannot be run.

            This field is a member of `oneof`_ ``_rejection_tracker_url``.
        address (str):
            Optional. The address of the
            [ViewabilityProvider][google.ads.admanager.v1.ViewabilityProvider].

            This field is a member of `oneof`_ ``_address``.
        email (str):
            Optional. The email of the
            [ViewabilityProvider][google.ads.admanager.v1.ViewabilityProvider].

            This field is a member of `oneof`_ ``_email``.
        fax (str):
            Optional. The fax number of the
            [ViewabilityProvider][google.ads.admanager.v1.ViewabilityProvider].

            This field is a member of `oneof`_ ``_fax``.
        phone (str):
            Optional. The phone number of the
            [ViewabilityProvider][google.ads.admanager.v1.ViewabilityProvider].

            This field is a member of `oneof`_ ``_phone``.
        external_id (str):
            Optional. The external ID of the
            [ViewabilityProvider][google.ads.admanager.v1.ViewabilityProvider].

            This field is a member of `oneof`_ ``_external_id``.
        comment (str):
            Optional. Comment about the
            [ViewabilityProvider][google.ads.admanager.v1.ViewabilityProvider].

            This field is a member of `oneof`_ ``_comment``.
        primary_contact (str):
            Optional. The resource name of primary Contact of the
            [ViewabilityProvider][google.ads.admanager.v1.ViewabilityProvider].
            Format: "networks/{network_code}/contacts/{contact_id}".

            This field is a member of `oneof`_ ``_primary_contact``.
        applied_teams (MutableSequence[str]):
            Optional. The resource names of Teams that are directly
            associated with the
            [ViewabilityProvider][google.ads.admanager.v1.ViewabilityProvider].
            Format: "networks/{network_code}/teams/{team_id}".
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the
            [ViewabilityProvider][google.ads.admanager.v1.ViewabilityProvider]
            was last updated.
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
    vendor_key: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    verification_script_url: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    verification_script_url_parameters: str = proto.Field(
        proto.STRING,
        number=6,
        optional=True,
    )
    rejection_tracker_url: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )
    address: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )
    email: str = proto.Field(
        proto.STRING,
        number=9,
        optional=True,
    )
    fax: str = proto.Field(
        proto.STRING,
        number=10,
        optional=True,
    )
    phone: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )
    external_id: str = proto.Field(
        proto.STRING,
        number=12,
        optional=True,
    )
    comment: str = proto.Field(
        proto.STRING,
        number=13,
        optional=True,
    )
    primary_contact: str = proto.Field(
        proto.STRING,
        number=14,
        optional=True,
    )
    applied_teams: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=16,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=18,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
