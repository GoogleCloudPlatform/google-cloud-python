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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.shopping.merchant.accounts.v1",
    manifest={
        "EmailPreferences",
        "GetEmailPreferencesRequest",
        "UpdateEmailPreferencesRequest",
    },
)


class EmailPreferences(proto.Message):
    r"""The categories of notifications the user opted into / opted
    out of. The email preferences do not include mandatory
    announcements as users can't opt out of them.

    Attributes:
        name (str):
            Identifier. The name of the EmailPreferences.
            The endpoint is only supported for the
            authenticated user.
        news_and_tips (google.shopping.merchant_accounts_v1.types.EmailPreferences.OptInState):
            Optional. Updates on new features, tips and
            best practices.
    """

    class OptInState(proto.Enum):
        r"""Opt in state of the email preference.

        Values:
            OPT_IN_STATE_UNSPECIFIED (0):
                Opt-in status is not specified.
            OPTED_OUT (1):
                User has opted out of receiving this type of
                email.
            OPTED_IN (2):
                User has opted in to receiving this type of
                email.
            UNCONFIRMED (3):
                User has opted in to receiving this type of
                email and the confirmation email has been sent,
                but user has not yet confirmed the opt in
                (applies only to certain countries).
        """

        OPT_IN_STATE_UNSPECIFIED = 0
        OPTED_OUT = 1
        OPTED_IN = 2
        UNCONFIRMED = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    news_and_tips: OptInState = proto.Field(
        proto.ENUM,
        number=2,
        enum=OptInState,
    )


class GetEmailPreferencesRequest(proto.Message):
    r"""Request message for GetEmailPreferences method.

    Attributes:
        name (str):
            Required. The name of the ``EmailPreferences`` resource.
            Format:
            ``accounts/{account}/users/{email}/emailPreferences``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateEmailPreferencesRequest(proto.Message):
    r"""Request message for UpdateEmailPreferences method.

    Attributes:
        email_preferences (google.shopping.merchant_accounts_v1.types.EmailPreferences):
            Required. Email Preferences to be updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. List of fields being updated.

            The following fields are supported (in both ``snake_case``
            and ``lowerCamelCase``):

            - ``news_and_tips``
    """

    email_preferences: "EmailPreferences" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="EmailPreferences",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
