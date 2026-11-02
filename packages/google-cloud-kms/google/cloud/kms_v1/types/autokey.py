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
    package="google.cloud.kms.v1",
    manifest={
        "CreateKeyHandleRequest",
        "GetKeyHandleRequest",
        "KeyHandle",
        "CreateKeyHandleMetadata",
        "ListKeyHandlesRequest",
        "ListKeyHandlesResponse",
    },
)


class CreateKeyHandleRequest(proto.Message):
    r"""Request message for
    [Autokey.CreateKeyHandle][google.cloud.kms.v1.Autokey.CreateKeyHandle].

    Attributes:
        parent (str):
            Required. Name of the resource project and location to
            create the [KeyHandle][google.cloud.kms.v1.KeyHandle] in,
            e.g. ``projects/{PROJECT_ID}/locations/{LOCATION}``.
        key_handle_id (str):
            Optional. Id of the
            [KeyHandle][google.cloud.kms.v1.KeyHandle]. Must be unique
            to the resource project and location. If not provided by the
            caller, a new UUID is used.
        key_handle (google.cloud.kms_v1.types.KeyHandle):
            Required. [KeyHandle][google.cloud.kms.v1.KeyHandle] to
            create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    key_handle_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    key_handle: "KeyHandle" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="KeyHandle",
    )


class GetKeyHandleRequest(proto.Message):
    r"""Request message for
    [GetKeyHandle][google.cloud.kms.v1.Autokey.GetKeyHandle].

    Attributes:
        name (str):
            Required. Name of the
            [KeyHandle][google.cloud.kms.v1.KeyHandle] resource, e.g.
            ``projects/{PROJECT_ID}/locations/{LOCATION}/keyHandles/{KEY_HANDLE_ID}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class KeyHandle(proto.Message):
    r"""Resource-oriented representation of a request to Cloud KMS Autokey
    and the resulting provisioning of a
    [CryptoKey][google.cloud.kms.v1.CryptoKey].

    Attributes:
        name (str):
            Identifier. Name of the
            [KeyHandle][google.cloud.kms.v1.KeyHandle] resource, e.g.
            ``projects/{PROJECT_ID}/locations/{LOCATION}/keyHandles/{KEY_HANDLE_ID}``.
        kms_key (str):
            Output only. Name of a
            [CryptoKey][google.cloud.kms.v1.CryptoKey] that has been
            provisioned for Customer Managed Encryption Key (CMEK) use
            in the [KeyHandle][google.cloud.kms.v1.KeyHandle] project
            and location for the requested resource type. The
            [CryptoKey][google.cloud.kms.v1.CryptoKey] project will
            reflect the value configured in the
            [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig] on the
            resource project's ancestor folder at the time of the
            [KeyHandle][google.cloud.kms.v1.KeyHandle] creation. If more
            than one ancestor folder has a configured
            [AutokeyConfig][google.cloud.kms.v1.AutokeyConfig], the
            nearest of these configurations is used.
        resource_type_selector (str):
            Required. Indicates the resource type that the resulting
            [CryptoKey][google.cloud.kms.v1.CryptoKey] is meant to
            protect, e.g. ``{SERVICE}.googleapis.com/{TYPE}``. See
            documentation for supported resource types.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    kms_key: str = proto.Field(
        proto.STRING,
        number=3,
    )
    resource_type_selector: str = proto.Field(
        proto.STRING,
        number=4,
    )


class CreateKeyHandleMetadata(proto.Message):
    r"""Metadata message for
    [CreateKeyHandle][google.cloud.kms.v1.Autokey.CreateKeyHandle]
    long-running operation response.

    """


class ListKeyHandlesRequest(proto.Message):
    r"""Request message for
    [Autokey.ListKeyHandles][google.cloud.kms.v1.Autokey.ListKeyHandles].

    Attributes:
        parent (str):
            Required. Name of the resource project and location from
            which to list [KeyHandles][google.cloud.kms.v1.KeyHandle],
            e.g. ``projects/{PROJECT_ID}/locations/{LOCATION}``.
        page_size (int):
            Optional. Optional limit on the number of
            [KeyHandles][google.cloud.kms.v1.KeyHandle] to include in
            the response. The service may return fewer than this value.
            Further [KeyHandles][google.cloud.kms.v1.KeyHandle] can
            subsequently be obtained by including the
            [ListKeyHandlesResponse.next_page_token][google.cloud.kms.v1.ListKeyHandlesResponse.next_page_token]
            in a subsequent request. If unspecified, at most 100
            [KeyHandles][google.cloud.kms.v1.KeyHandle] will be
            returned.
        page_token (str):
            Optional. Optional pagination token, returned earlier via
            [ListKeyHandlesResponse.next_page_token][google.cloud.kms.v1.ListKeyHandlesResponse.next_page_token].
        filter (str):
            Optional. Filter to apply when listing
            [KeyHandles][google.cloud.kms.v1.KeyHandle], e.g.
            ``resource_type_selector="{SERVICE}.googleapis.com/{TYPE}"``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListKeyHandlesResponse(proto.Message):
    r"""Response message for
    [Autokey.ListKeyHandles][google.cloud.kms.v1.Autokey.ListKeyHandles].

    Attributes:
        key_handles (MutableSequence[google.cloud.kms_v1.types.KeyHandle]):
            Resulting [KeyHandles][google.cloud.kms.v1.KeyHandle].
        next_page_token (str):
            A token to retrieve next page of results. Pass this value in
            [ListKeyHandlesRequest.page_token][google.cloud.kms.v1.ListKeyHandlesRequest.page_token]
            to retrieve the next page of results.
    """

    @property
    def raw_page(self):
        return self

    key_handles: MutableSequence["KeyHandle"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="KeyHandle",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
