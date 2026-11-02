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

from google.ads.admanager_v1.types import native_style_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetNativeStyleRequest",
        "ListNativeStylesRequest",
        "ListNativeStylesResponse",
        "CreateNativeStyleRequest",
        "BatchCreateNativeStylesRequest",
        "BatchCreateNativeStylesResponse",
        "UpdateNativeStyleRequest",
        "BatchUpdateNativeStylesRequest",
        "BatchUpdateNativeStylesResponse",
        "BatchActivateNativeStylesRequest",
        "BatchActivateNativeStylesResponse",
        "BatchDeactivateNativeStylesRequest",
        "BatchDeactivateNativeStylesResponse",
        "BatchArchiveNativeStylesRequest",
        "BatchArchiveNativeStylesResponse",
    },
)


class GetNativeStyleRequest(proto.Message):
    r"""Request object for ``GetNativeStyle`` method.

    Attributes:
        name (str):
            Required. The resource name of the NativeStyle. Format:
            ``networks/{network_code}/nativeStyles/{native_style_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListNativeStylesRequest(proto.Message):
    r"""Request object for ``ListNativeStyles`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            NativeStyles. Format: ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of ``NativeStyles`` to return.
            The service may return fewer than this value. If
            unspecified, at most 50 ``NativeStyles`` will be returned.
            The maximum value is 1000; values greater than 1000 will be
            coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListNativeStyles`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListNativeStyles`` must match the call that provided the
            page token.
        filter (str):
            Optional. Expression to filter the response. See syntax
            details at
            https://developers.google.com/ad-manager/api/beta/filters

            **Filterable fields:**

            - ``creativeTemplate``
            - ``displayName``
            - ``name``
            - ``size.canonicalName``
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


class ListNativeStylesResponse(proto.Message):
    r"""Response object for ``ListNativeStylesRequest`` containing matching
    ``NativeStyle`` objects.

    Attributes:
        native_styles (MutableSequence[google.ads.admanager_v1.types.NativeStyle]):
            The ``NativeStyle`` objects from the specified network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of ``NativeStyle`` objects. If a filter was
            included in the request, this reflects the total number
            after the filtering is applied.

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

    native_styles: MutableSequence[native_style_messages.NativeStyle] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=native_style_messages.NativeStyle,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CreateNativeStyleRequest(proto.Message):
    r"""Request object for ``CreateNativeStyle`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this ``NativeStyle``
            will be created. Format: ``networks/{network_code}``
        native_style (google.ads.admanager_v1.types.NativeStyle):
            Required. The ``NativeStyle`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    native_style: native_style_messages.NativeStyle = proto.Field(
        proto.MESSAGE,
        number=2,
        message=native_style_messages.NativeStyle,
    )


class BatchCreateNativeStylesRequest(proto.Message):
    r"""Request object for ``BatchCreateNativeStyles`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``NativeStyles`` will be
            created. Format: ``networks/{network_code}`` The parent
            field in the CreateNativeStyleRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.CreateNativeStyleRequest]):
            Required. The ``NativeStyle`` objects to create. A maximum
            of 100 objects can be created in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateNativeStyleRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateNativeStyleRequest",
    )


class BatchCreateNativeStylesResponse(proto.Message):
    r"""Response object for ``BatchCreateNativeStyles`` method.

    Attributes:
        native_styles (MutableSequence[google.ads.admanager_v1.types.NativeStyle]):
            The ``NativeStyle`` objects created.
    """

    native_styles: MutableSequence[native_style_messages.NativeStyle] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=native_style_messages.NativeStyle,
        )
    )


class UpdateNativeStyleRequest(proto.Message):
    r"""Request object for ``UpdateNativeStyle`` method.

    Attributes:
        native_style (google.ads.admanager_v1.types.NativeStyle):
            Required. The ``NativeStyle`` to update.

            The ``NativeStyle``'s ``name`` is used to identify the
            ``NativeStyle`` to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    native_style: native_style_messages.NativeStyle = proto.Field(
        proto.MESSAGE,
        number=1,
        message=native_style_messages.NativeStyle,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateNativeStylesRequest(proto.Message):
    r"""Request object for ``BatchUpdateNativeStyles`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``NativeStyles`` will be
            updated. Format: ``networks/{network_code}`` The parent
            field in the UpdateNativeStyleRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.UpdateNativeStyleRequest]):
            Required. The ``NativeStyle`` objects to update. A maximum
            of 100 objects can be updated in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateNativeStyleRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdateNativeStyleRequest",
    )


class BatchUpdateNativeStylesResponse(proto.Message):
    r"""Response object for ``BatchUpdateNativeStyles`` method.

    Attributes:
        native_styles (MutableSequence[google.ads.admanager_v1.types.NativeStyle]):
            The ``NativeStyle`` objects updated.
    """

    native_styles: MutableSequence[native_style_messages.NativeStyle] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=native_style_messages.NativeStyle,
        )
    )


class BatchActivateNativeStylesRequest(proto.Message):
    r"""Request object for ``BatchActivateNativeStyles`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. Resource names for the ``NativeStyle``\ s. Format:
            ``networks/{network_code}/nativeStyles/{native_style_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchActivateNativeStylesResponse(proto.Message):
    r"""Response object for ``BatchActivateNativeStyles`` method."""


class BatchDeactivateNativeStylesRequest(proto.Message):
    r"""Request object for ``BatchDeactivateNativeStyles`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. Resource names for the ``NativeStyle``\ s. Format:
            ``networks/{network_code}/nativeStyles/{native_style_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchDeactivateNativeStylesResponse(proto.Message):
    r"""Response object for ``BatchDeactivateNativeStyles`` method."""


class BatchArchiveNativeStylesRequest(proto.Message):
    r"""Request object for ``BatchArchiveNativeStyles`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. Resource names for the ``NativeStyle``\ s. Format:
            ``networks/{network_code}/nativeStyles/{native_style_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchArchiveNativeStylesResponse(proto.Message):
    r"""Response object for ``BatchArchiveNativeStyles`` method."""


__all__ = tuple(sorted(__protobuf__.manifest))
