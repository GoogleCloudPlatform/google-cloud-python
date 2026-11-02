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

from google.ads.admanager_v1.types import contact_enums

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "Contact",
    },
)


class Contact(proto.Message):
    r"""A contact represents a person who is affiliated with a single
    company. A contact can have a variety of contact information
    associated to it, and can be invited to view their company's
    orders, line items, creatives, and reports.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the ``Contact``. Format:
            ``networks/{network_code}/contacts/{contact_id}``
        display_name (str):
            Required. The name of the contact. This
            attribute has a maximum length of 127
            characters.

            This field is a member of `oneof`_ ``_display_name``.
        company (str):
            Required. Immutable. The resource name of the Company.
            Format: "networks/{network_code}/companies/{company_id}".

            This field is a member of `oneof`_ ``_company``.
        status (google.ads.admanager_v1.types.ContactStatusEnum.ContactStatus):
            Output only. The status of the contact. This
            attribute is assigned by Google.

            This field is a member of `oneof`_ ``_status``.
        address (str):
            Optional. The address of the contact. This
            attribute has a maximum length of 1024
            characters.

            This field is a member of `oneof`_ ``_address``.
        cell_phone (str):
            Optional. The cell phone number where the
            contact can be reached.

            This field is a member of `oneof`_ ``_cell_phone``.
        comment (str):
            Optional. A free-form text comment for the
            contact. This attribute has a maximum length of
            1024 characters.

            This field is a member of `oneof`_ ``_comment``.
        email (str):
            Optional. The e-mail address where the
            contact can be reached. This attribute has a
            maximum length of 128 characters.

            This field is a member of `oneof`_ ``_email``.
        fax (str):
            Optional. The fax number where the contact
            can be reached. This attribute has a maximum
            length of 1024 characters.

            This field is a member of `oneof`_ ``_fax``.
        title (str):
            Optional. The job title of the contact. This
            attribute has a maximum length of 1024
            characters.

            This field is a member of `oneof`_ ``_title``.
        work_phone (str):
            Optional. The work phone number where the
            contact can be reached. This attribute has a
            maximum length of 1024 characters.

            This field is a member of `oneof`_ ``_work_phone``.
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
    company: str = proto.Field(
        proto.STRING,
        number=5,
        optional=True,
    )
    status: contact_enums.ContactStatusEnum.ContactStatus = proto.Field(
        proto.ENUM,
        number=6,
        optional=True,
        enum=contact_enums.ContactStatusEnum.ContactStatus,
    )
    address: str = proto.Field(
        proto.STRING,
        number=7,
        optional=True,
    )
    cell_phone: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )
    comment: str = proto.Field(
        proto.STRING,
        number=9,
        optional=True,
    )
    email: str = proto.Field(
        proto.STRING,
        number=10,
        optional=True,
    )
    fax: str = proto.Field(
        proto.STRING,
        number=11,
        optional=True,
    )
    title: str = proto.Field(
        proto.STRING,
        number=12,
        optional=True,
    )
    work_phone: str = proto.Field(
        proto.STRING,
        number=13,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
