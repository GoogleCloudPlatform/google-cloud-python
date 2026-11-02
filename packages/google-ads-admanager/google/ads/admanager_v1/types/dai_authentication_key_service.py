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

from google.ads.admanager_v1.types import dai_authentication_key_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetDaiAuthenticationKeyRequest",
        "ListDaiAuthenticationKeysRequest",
        "ListDaiAuthenticationKeysResponse",
        "CreateDaiAuthenticationKeyRequest",
        "BatchCreateDaiAuthenticationKeysRequest",
        "BatchCreateDaiAuthenticationKeysResponse",
        "UpdateDaiAuthenticationKeyRequest",
        "BatchUpdateDaiAuthenticationKeysRequest",
        "BatchUpdateDaiAuthenticationKeysResponse",
        "BatchActivateDaiAuthenticationKeysRequest",
        "BatchActivateDaiAuthenticationKeysResponse",
        "BatchDeactivateDaiAuthenticationKeysRequest",
        "BatchDeactivateDaiAuthenticationKeysResponse",
    },
)


class GetDaiAuthenticationKeyRequest(proto.Message):
    r"""Request object for ``GetDaiAuthenticationKey`` method.

    Attributes:
        name (str):
            Required. The resource name of the ``DaiAuthenticationKey``.
            Format:
            ``networks/{network_code}/daiAuthenticationKeys/{dai_authentication_key_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDaiAuthenticationKeysRequest(proto.Message):
    r"""Request object for ``ListDaiAuthenticationKeys`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            DaiAuthenticationKeys. Format: ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of ``DaiAuthenticationKeys`` to
            return. The service may return fewer than this value. If
            unspecified, at most 50 ``DaiAuthenticationKeys`` will be
            returned. The maximum value is 1000; values greater than
            1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListDaiAuthenticationKeys`` call. Provide this to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``ListDaiAuthenticationKeys`` must match the call that
            provided the page token.
        filter (str):
            Optional. Expression to filter the response. See syntax
            details at
            https://developers.google.com/ad-manager/api/beta/filters

            **Filterable fields:**

            - ``displayName``
            - ``name``
            - ``status``
        order_by (str):
            Optional. Expression to specify sorting
            order. See syntax details at
            https://developers.google.com/ad-manager/api/beta/filters#order
        skip (int):
            Optional. Number of individual resources to
            skip while paginating.
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
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )
    skip: int = proto.Field(
        proto.INT32,
        number=6,
    )


class ListDaiAuthenticationKeysResponse(proto.Message):
    r"""Response object for ``ListDaiAuthenticationKeysRequest`` containing
    matching ``DaiAuthenticationKey`` objects.

    Attributes:
        dai_authentication_keys (MutableSequence[google.ads.admanager_v1.types.DaiAuthenticationKey]):
            The ``DaiAuthenticationKey`` objects from the specified
            network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of ``DaiAuthenticationKey`` objects. If a
            filter was included in the request, this reflects the total
            number after the filtering is applied.

            ``total_size`` won't be calculated in the response unless it
            has been included in a response field mask. The response
            field mask can be provided to the method by using the URL
            parameter ``$fields`` or ``fields``, or by using the
            HTTP/gRPC header ``X-Goog-FieldMask``.

            For more information, see
            https://developers.google.com/ad-manager/api/beta/field-masks
    """

    @property
    def raw_page(self):
        return self

    dai_authentication_keys: MutableSequence[
        dai_authentication_key_messages.DaiAuthenticationKey
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=dai_authentication_key_messages.DaiAuthenticationKey,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CreateDaiAuthenticationKeyRequest(proto.Message):
    r"""Request object for ``CreateDaiAuthenticationKey`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this
            ``DaiAuthenticationKey`` will be created. Format:
            ``networks/{network_code}``
        dai_authentication_key (google.ads.admanager_v1.types.DaiAuthenticationKey):
            Required. The ``DaiAuthenticationKey`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dai_authentication_key: dai_authentication_key_messages.DaiAuthenticationKey = (
        proto.Field(
            proto.MESSAGE,
            number=2,
            message=dai_authentication_key_messages.DaiAuthenticationKey,
        )
    )


class BatchCreateDaiAuthenticationKeysRequest(proto.Message):
    r"""Request object for ``BatchCreateDaiAuthenticationKeys`` method.

    Attributes:
        parent (str):
            Required. The parent resource where
            ``DaiAuthenticationKeys`` will be created. Format:
            ``networks/{network_code}`` The parent field in the
            CreateDaiAuthenticationKeyRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.CreateDaiAuthenticationKeyRequest]):
            Required. The ``DaiAuthenticationKey`` objects to create. A
            maximum of 100 objects can be created in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateDaiAuthenticationKeyRequest"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="CreateDaiAuthenticationKeyRequest",
        )
    )


class BatchCreateDaiAuthenticationKeysResponse(proto.Message):
    r"""Response object for ``BatchCreateDaiAuthenticationKeys`` method.

    Attributes:
        dai_authentication_keys (MutableSequence[google.ads.admanager_v1.types.DaiAuthenticationKey]):
            The ``DaiAuthenticationKey`` objects created.
    """

    dai_authentication_keys: MutableSequence[
        dai_authentication_key_messages.DaiAuthenticationKey
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=dai_authentication_key_messages.DaiAuthenticationKey,
    )


class UpdateDaiAuthenticationKeyRequest(proto.Message):
    r"""Request object for ``UpdateDaiAuthenticationKey`` method.

    Attributes:
        dai_authentication_key (google.ads.admanager_v1.types.DaiAuthenticationKey):
            Required. The ``DaiAuthenticationKey`` to update.

            The ``DaiAuthenticationKey``'s ``name`` is used to identify
            the ``DaiAuthenticationKey`` to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    dai_authentication_key: dai_authentication_key_messages.DaiAuthenticationKey = (
        proto.Field(
            proto.MESSAGE,
            number=1,
            message=dai_authentication_key_messages.DaiAuthenticationKey,
        )
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateDaiAuthenticationKeysRequest(proto.Message):
    r"""Request object for ``BatchUpdateDaiAuthenticationKeys`` method.

    Attributes:
        parent (str):
            Required. The parent resource where
            ``DaiAuthenticationKeys`` will be updated. Format:
            ``networks/{network_code}`` The parent field in the
            UpdateDaiAuthenticationKeyRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.UpdateDaiAuthenticationKeyRequest]):
            Required. The ``DaiAuthenticationKey`` objects to update. A
            maximum of 100 objects can be updated in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateDaiAuthenticationKeyRequest"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="UpdateDaiAuthenticationKeyRequest",
        )
    )


class BatchUpdateDaiAuthenticationKeysResponse(proto.Message):
    r"""Response object for ``BatchUpdateDaiAuthenticationKeys`` method.

    Attributes:
        dai_authentication_keys (MutableSequence[google.ads.admanager_v1.types.DaiAuthenticationKey]):
            The ``DaiAuthenticationKey`` objects updated.
    """

    dai_authentication_keys: MutableSequence[
        dai_authentication_key_messages.DaiAuthenticationKey
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=dai_authentication_key_messages.DaiAuthenticationKey,
    )


class BatchActivateDaiAuthenticationKeysRequest(proto.Message):
    r"""Request object for ``BatchPerformDaiAuthenticationKeyAction``
    method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. Resource names for the DaiAuthenticationKey.
            Format:
            ``networks/{network_code}/daiAuthenticationKeys/{dai_authentication_key}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchActivateDaiAuthenticationKeysResponse(proto.Message):
    r"""Response object for ``BatchActivateDaiAuthenticationKeys`` method."""


class BatchDeactivateDaiAuthenticationKeysRequest(proto.Message):
    r"""Request object for ``BatchPerformDaiAuthenticationKeyAction``
    method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. Resource names for the DaiAuthenticationKey.
            Format:
            ``networks/{network_code}/daiAuthenticationKeys/{dai_authentication_key}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchDeactivateDaiAuthenticationKeysResponse(proto.Message):
    r"""Response object for ``BatchDeactivateDaiAuthenticationKeys`` method."""


__all__ = tuple(sorted(__protobuf__.manifest))
