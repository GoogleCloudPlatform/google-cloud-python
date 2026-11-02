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
    package="google.ads.admanager.v1",
    manifest={
        "User",
    },
)


class User(proto.Message):
    r"""The User resource.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the User. Format:
            ``networks/{network_code}/users/{user_id}``
        user_id (int):
            Output only. Deprecated: ``User`` ID.

            This field is a member of `oneof`_ ``_user_id``.
        display_name (str):
            Required. The name of the User. It has a
            maximum length of 128 characters.

            This field is a member of `oneof`_ ``_display_name``.
        email (str):
            Required. The email or login of the User. In
            order to create a new user, you must already
            have a Google Account.

            This field is a member of `oneof`_ ``_email``.
        role (str):
            Required. The unique Role ID of the User.
            Roles that are created by Google will have
            negative IDs.

            This field is a member of `oneof`_ ``_role``.
        active (bool):
            Output only. Specifies whether or not the
            User is active. An inactive user cannot log in
            to the system or perform any operations.

            This field is a member of `oneof`_ ``_active``.
        external_id (str):
            Optional. An identifier for the User that is
            meaningful to the publisher. This attribute has
            a maximum length of 255 characters.

            This field is a member of `oneof`_ ``_external_id``.
        service_account (bool):
            Output only. Whether the user is an OAuth2
            service account user. Service account users can
            only be added through the UI.

            This field is a member of `oneof`_ ``_service_account``.
        orders_ui_local_time_zone (str):
            Optional. The IANA Time Zone Database time zone, e.g.
            "America/New_York", used in the orders and line items UI for
            this User. If not provided, the UI then defaults to using
            the Network's timezone. This setting only affects the UI for
            this user and does not affect the timezone of any dates and
            times returned in API responses.

            This field is a member of `oneof`_ ``_orders_ui_local_time_zone``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    user_id: int = proto.Field(
        proto.INT64,
        number=10,
        optional=True,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    email: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    role: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    active: bool = proto.Field(
        proto.BOOL,
        number=6,
        optional=True,
    )
    external_id: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )
    service_account: bool = proto.Field(
        proto.BOOL,
        number=8,
        optional=True,
    )
    orders_ui_local_time_zone: str = proto.Field(
        proto.STRING,
        number=9,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
