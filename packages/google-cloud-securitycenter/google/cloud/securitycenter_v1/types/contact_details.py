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
    package="google.cloud.securitycenter.v1",
    manifest={
        "ContactDetails",
        "Contact",
    },
)


class ContactDetails(proto.Message):
    r"""Details about specific contacts

    Attributes:
        contacts (MutableSequence[google.cloud.securitycenter_v1.types.Contact]):
            A list of contacts
    """

    contacts: MutableSequence["Contact"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Contact",
    )


class Contact(proto.Message):
    r"""The email address of a contact.

    Attributes:
        email (str):
            An email address. For example, "``person123@company.com``".
    """

    email: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
