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

from google.cloud.api_keys_v2.types import resources

__protobuf__ = proto.module(
    package="google.api.apikeys.v2",
    manifest={
        "CreateKeyRequest",
        "ListKeysRequest",
        "ListKeysResponse",
        "GetKeyRequest",
        "GetKeyStringRequest",
        "GetKeyStringResponse",
        "UpdateKeyRequest",
        "DeleteKeyRequest",
        "UndeleteKeyRequest",
        "LookupKeyRequest",
        "LookupKeyResponse",
    },
)


class CreateKeyRequest(proto.Message):
    r"""Request message for ``CreateKey`` method.

    Attributes:
        parent (str):
            Required. The project in which the API key is
            created.
        key (google.cloud.api_keys_v2.types.Key):
            Required. The API key fields to set at creation time. You
            can configure only the ``display_name``, ``restrictions``,
            and ``annotations`` fields.
        key_id (str):
            User specified key id (optional). If specified, it will
            become the final component of the key resource name.

            The id must be unique within the project, must conform with
            RFC-1034, is restricted to lower-cased letters, and has a
            maximum length of 63 characters. In another word, the id
            must match the regular expression:
            ``[a-z]([a-z0-9-]{0,61}[a-z0-9])?``.

            The id must NOT be a UUID-like string.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    key: resources.Key = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.Key,
    )
    key_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListKeysRequest(proto.Message):
    r"""Request message for ``ListKeys`` method.

    Attributes:
        parent (str):
            Required. Lists all API keys associated with
            this project.
        page_size (int):
            Optional. Specifies the maximum number of
            results to be returned at a time.
        page_token (str):
            Optional. Requests a specific page of
            results.
        show_deleted (bool):
            Optional. Indicate that keys deleted in the
            past 30 days should also be returned.
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
    show_deleted: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class ListKeysResponse(proto.Message):
    r"""Response message for ``ListKeys`` method.

    Attributes:
        keys (MutableSequence[google.cloud.api_keys_v2.types.Key]):
            A list of API keys.
        next_page_token (str):
            The pagination token for the next page of
            results.
    """

    @property
    def raw_page(self):
        return self

    keys: MutableSequence[resources.Key] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Key,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetKeyRequest(proto.Message):
    r"""Request message for ``GetKey`` method.

    Attributes:
        name (str):
            Required. The resource name of the API key to
            get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetKeyStringRequest(proto.Message):
    r"""Request message for ``GetKeyString`` method.

    Attributes:
        name (str):
            Required. The resource name of the API key to
            be retrieved.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetKeyStringResponse(proto.Message):
    r"""Response message for ``GetKeyString`` method.

    Attributes:
        key_string (str):
            An encrypted and signed value of the key.
    """

    key_string: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateKeyRequest(proto.Message):
    r"""Request message for ``UpdateKey`` method.

    Attributes:
        key (google.cloud.api_keys_v2.types.Key):
            Required. Set the ``name`` field to the resource name of the
            API key to be updated. You can update only the
            ``display_name``, ``restrictions``, and ``annotations``
            fields.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The field mask specifies which fields to be updated as part
            of this request. All other fields are ignored. Mutable
            fields are: ``display_name``, ``restrictions``, and
            ``annotations``. If an update mask is not provided, the
            service treats it as an implied mask equivalent to all
            allowed fields that are set on the wire. If the field mask
            has a special value "\*", the service treats it equivalent
            to replace all allowed mutable fields.
    """

    key: resources.Key = proto.Field(
        proto.MESSAGE,
        number=1,
        message=resources.Key,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteKeyRequest(proto.Message):
    r"""Request message for ``DeleteKey`` method.

    Attributes:
        name (str):
            Required. The resource name of the API key to
            be deleted.
        etag (str):
            Optional. The etag known to the client for
            the expected state of the key. This is to be
            used for optimistic concurrency.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UndeleteKeyRequest(proto.Message):
    r"""Request message for ``UndeleteKey`` method.

    Attributes:
        name (str):
            Required. The resource name of the API key to
            be undeleted.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class LookupKeyRequest(proto.Message):
    r"""Request message for ``LookupKey`` method.

    Attributes:
        key_string (str):
            Required. Finds the project that owns the key
            string value.
    """

    key_string: str = proto.Field(
        proto.STRING,
        number=1,
    )


class LookupKeyResponse(proto.Message):
    r"""Response message for ``LookupKey`` method.

    Attributes:
        parent (str):
            The project that owns the key with the value
            specified in the request.
        name (str):
            The resource name of the API key. If the API
            key has been purged, resource name is empty.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    name: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
