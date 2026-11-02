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

import google.type.phone_number_pb2 as phone_number_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.shopping.merchant.accounts.v1beta",
    manifest={
        "CustomerService",
    },
)


class CustomerService(proto.Message):
    r"""Customer service information.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        uri (str):
            Optional. The URI where customer service may
            be found.

            This field is a member of `oneof`_ ``_uri``.
        email (str):
            Optional. The email address where customer
            service may be reached.

            This field is a member of `oneof`_ ``_email``.
        phone (google.type.phone_number_pb2.PhoneNumber):
            Optional. The phone number where customer
            service may be called.

            This field is a member of `oneof`_ ``_phone``.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    email: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    phone: phone_number_pb2.PhoneNumber = proto.Field(
        proto.MESSAGE,
        number=3,
        optional=True,
        message=phone_number_pb2.PhoneNumber,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
