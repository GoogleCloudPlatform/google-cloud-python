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
        "UserData",
        "UserIdentifier",
        "AddressInfo",
    },
)


class UserData(proto.Message):
    r"""Data that identifies the user. At least one identifier is
    required.

    Attributes:
        user_identifiers (MutableSequence[google.ads.datamanager_v1.types.UserIdentifier]):
            Required. The identifiers for the user. It's possible to
            provide multiple instances of the same type of data (for
            example, multiple email addresses). To increase the
            likelihood of a match, provide as many identifiers as
            possible. At most 10 ``userIdentifiers`` can be provided in
            a single
            [AudienceMember][google.ads.datamanager.v1.AudienceMember]
            or [Event][google.ads.datamanager.v1.Event].
    """

    user_identifiers: MutableSequence["UserIdentifier"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="UserIdentifier",
    )


class UserIdentifier(proto.Message):
    r"""A single identifier for the user.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        email_address (str):
            Hashed email address using SHA-256 hash
            function after normalization.

            This field is a member of `oneof`_ ``identifier``.
        phone_number (str):
            Hashed phone number using SHA-256 hash
            function after normalization (E164 standard).

            This field is a member of `oneof`_ ``identifier``.
        address (google.ads.datamanager_v1.types.AddressInfo):
            The known components of a user's address.
            Holds a grouping of identifiers that are matched
            all at once.

            This field is a member of `oneof`_ ``identifier``.
    """

    email_address: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="identifier",
    )
    phone_number: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="identifier",
    )
    address: "AddressInfo" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="identifier",
        message="AddressInfo",
    )


class AddressInfo(proto.Message):
    r"""Address information for the user.

    Attributes:
        given_name (str):
            Required. Given (first) name of the user, all
            lowercase, with no punctuation, no leading or
            trailing whitespace, and hashed as SHA-256.
        family_name (str):
            Required. Family (last) name of the user, all
            lowercase, with no punctuation, no leading or
            trailing whitespace, and hashed as SHA-256.
        region_code (str):
            Required. The 2-letter region code in
            ISO-3166-1 alpha-2 of the user's address.
        postal_code (str):
            Required. The postal code of the user's
            address.
        address_line (str):
            Optional. The street and number of the user's
            address. Used only for Google Analytics. This
            field is hashed and possibly encrypted.

            Normalize the value before hashing:

            - Remove symbol characters
            - Convert to lowercase
            - Remove leading and trailing whitespace
        city (str):
            Optional. The city of the user's address.
            Used only for Google Analytics.
            The value should be normalized as such:

            - Remove symbol characters
            - Convert to lowercase
            - Remove leading and trailing whitespace
        administrative_area (str):
            Optional. The administrative area
            (state/province) of the user's address. Used
            only for Google Analytics.

            The value should be normalized as such:

            - Remove symbol characters
            - Convert to lowercase
            - Remove leading and trailing whitespace
    """

    given_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    family_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    region_code: str = proto.Field(
        proto.STRING,
        number=3,
    )
    postal_code: str = proto.Field(
        proto.STRING,
        number=4,
    )
    address_line: str = proto.Field(
        proto.STRING,
        number=5,
    )
    city: str = proto.Field(
        proto.STRING,
        number=6,
    )
    administrative_area: str = proto.Field(
        proto.STRING,
        number=7,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
