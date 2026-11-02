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
        "Homepage",
        "GetHomepageRequest",
        "UpdateHomepageRequest",
        "ClaimHomepageRequest",
        "UnclaimHomepageRequest",
    },
)


class Homepage(proto.Message):
    r"""The ``Homepage`` message represents a business's store homepage
    within the system.

    A business's homepage is the primary domain where customers interact
    with their store.

    The homepage can be claimed and verified as a proof of ownership and
    allows the business to unlock features that require a verified
    website. For more information, see `Understanding online store URL
    verification <//support.google.com/merchants/answer/176793>`__.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the store's homepage.
            Format: ``accounts/{account}/homepage``
        uri (str):
            Required. The URI (typically a URL) of the
            store's homepage.

            This field is a member of `oneof`_ ``_uri``.
        claimed (bool):
            Output only. Whether the homepage is claimed.
            See
            https://support.google.com/merchants/answer/176793.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    claimed: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class GetHomepageRequest(proto.Message):
    r"""Request message for the ``GetHomepage`` method.

    Attributes:
        name (str):
            Required. The name of the homepage to retrieve. Format:
            ``accounts/{account}/homepage``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateHomepageRequest(proto.Message):
    r"""Request message for the ``UpdateHomepage`` method.

    Attributes:
        homepage (google.shopping.merchant_accounts_v1.types.Homepage):
            Required. The new version of the homepage.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. List of fields being updated.

            The following fields are supported (in both ``snake_case``
            and ``lowerCamelCase``):

            - ``uri``
    """

    homepage: "Homepage" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Homepage",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class ClaimHomepageRequest(proto.Message):
    r"""Request message for the ``ClaimHomepage`` method.

    Attributes:
        name (str):
            Required. The name of the homepage to claim. Format:
            ``accounts/{account}/homepage``
        overwrite (bool):
            Optional. When set to ``true``, this option removes any
            existing claim on the requested website from any other
            account to the account making the request, effectively
            replacing the previous claim.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    overwrite: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class UnclaimHomepageRequest(proto.Message):
    r"""Request message for the ``UnclaimHomepage`` method.

    Attributes:
        name (str):
            Required. The name of the homepage to unclaim. Format:
            ``accounts/{account}/homepage``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
