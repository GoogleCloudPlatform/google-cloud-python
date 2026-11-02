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

from google.ads.admanager_v1.types import creative_wrapper_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetCreativeWrapperRequest",
        "ListCreativeWrappersRequest",
        "ListCreativeWrappersResponse",
        "CreateCreativeWrapperRequest",
        "BatchCreateCreativeWrappersRequest",
        "BatchCreateCreativeWrappersResponse",
        "UpdateCreativeWrapperRequest",
        "BatchUpdateCreativeWrappersRequest",
        "BatchUpdateCreativeWrappersResponse",
        "BatchActivateCreativeWrappersRequest",
        "BatchActivateCreativeWrappersResponse",
        "BatchDeactivateCreativeWrappersRequest",
        "BatchDeactivateCreativeWrappersResponse",
    },
)


class GetCreativeWrapperRequest(proto.Message):
    r"""Request object for ``GetCreativeWrapper`` method.

    Attributes:
        name (str):
            Required. The resource name of the CreativeWrapper. Format:
            ``networks/{network_code}/creativeWrappers/{creative_wrapper_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListCreativeWrappersRequest(proto.Message):
    r"""Request object for ``ListCreativeWrappers`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            CreativeWrappers. Format: ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of ``CreativeWrappers`` to
            return. The service may return fewer than this value. If
            unspecified, at most 50 ``CreativeWrappers`` will be
            returned. The maximum value is 1000; values greater than
            1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListCreativeWrappers`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListCreativeWrappers`` must match the call that provided
            the page token.
        filter (str):
            Optional. Expression to filter the response. See syntax
            details at
            https://developers.google.com/ad-manager/api/beta/filters

            **Filterable fields:**

            - ``creativeWrapperType``
            - ``label``
            - ``name``
            - ``ordering``
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


class ListCreativeWrappersResponse(proto.Message):
    r"""Response object for ``ListCreativeWrappersRequest`` containing
    matching ``CreativeWrapper`` objects.

    Attributes:
        creative_wrappers (MutableSequence[google.ads.admanager_v1.types.CreativeWrapper]):
            The ``CreativeWrapper`` objects from the specified network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of ``CreativeWrapper`` objects. If a filter was
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

    creative_wrappers: MutableSequence[creative_wrapper_messages.CreativeWrapper] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=creative_wrapper_messages.CreativeWrapper,
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


class CreateCreativeWrapperRequest(proto.Message):
    r"""Request object for ``CreateCreativeWrapper`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this ``CreativeWrapper``
            will be created. Format: ``networks/{network_code}``
        creative_wrapper (google.ads.admanager_v1.types.CreativeWrapper):
            Required. The ``CreativeWrapper`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    creative_wrapper: creative_wrapper_messages.CreativeWrapper = proto.Field(
        proto.MESSAGE,
        number=2,
        message=creative_wrapper_messages.CreativeWrapper,
    )


class BatchCreateCreativeWrappersRequest(proto.Message):
    r"""Request object for ``BatchCreateCreativeWrappers`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``CreativeWrappers``
            will be created. Format: ``networks/{network_code}`` The
            parent field in the CreateCreativeWrapperRequest must match
            this field.
        requests (MutableSequence[google.ads.admanager_v1.types.CreateCreativeWrapperRequest]):
            Required. The ``CreativeWrapper`` objects to create. A
            maximum of 100 objects can be created in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateCreativeWrapperRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateCreativeWrapperRequest",
    )


class BatchCreateCreativeWrappersResponse(proto.Message):
    r"""Response object for ``BatchCreateCreativeWrappers`` method.

    Attributes:
        creative_wrappers (MutableSequence[google.ads.admanager_v1.types.CreativeWrapper]):
            The ``CreativeWrapper`` objects created.
    """

    creative_wrappers: MutableSequence[creative_wrapper_messages.CreativeWrapper] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=creative_wrapper_messages.CreativeWrapper,
        )
    )


class UpdateCreativeWrapperRequest(proto.Message):
    r"""Request object for ``UpdateCreativeWrapper`` method.

    Attributes:
        creative_wrapper (google.ads.admanager_v1.types.CreativeWrapper):
            Required. The ``CreativeWrapper`` to update.

            The ``CreativeWrapper``'s ``name`` is used to identify the
            ``CreativeWrapper`` to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    creative_wrapper: creative_wrapper_messages.CreativeWrapper = proto.Field(
        proto.MESSAGE,
        number=1,
        message=creative_wrapper_messages.CreativeWrapper,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateCreativeWrappersRequest(proto.Message):
    r"""Request object for ``BatchUpdateCreativeWrappers`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``CreativeWrappers``
            will be updated. Format: ``networks/{network_code}`` The
            parent field in the UpdateCreativeWrapperRequest must match
            this field.
        requests (MutableSequence[google.ads.admanager_v1.types.UpdateCreativeWrapperRequest]):
            Required. The ``CreativeWrapper`` objects to update. A
            maximum of 100 objects can be updated in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateCreativeWrapperRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdateCreativeWrapperRequest",
    )


class BatchUpdateCreativeWrappersResponse(proto.Message):
    r"""Response object for ``BatchUpdateCreativeWrappers`` method.

    Attributes:
        creative_wrappers (MutableSequence[google.ads.admanager_v1.types.CreativeWrapper]):
            The ``CreativeWrapper`` objects updated.
    """

    creative_wrappers: MutableSequence[creative_wrapper_messages.CreativeWrapper] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=creative_wrapper_messages.CreativeWrapper,
        )
    )


class BatchActivateCreativeWrappersRequest(proto.Message):
    r"""Request message to activate ``CreativeWrapper`` objects.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the ``CreativeWrapper``
            objects to activate. Format:
            ``networks/{network_code}/creativeWrappers/{creative_wrapper_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchActivateCreativeWrappersResponse(proto.Message):
    r"""Response message for ``BatchActivateCreativeWrappers`` method."""


class BatchDeactivateCreativeWrappersRequest(proto.Message):
    r"""Request message to deactivate ``CreativeWrapper`` objects.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the ``CreativeWrapper``
            objects to deactivate. Format:
            ``networks/{network_code}/creativeWrappers/{creative_wrapper_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchDeactivateCreativeWrappersResponse(proto.Message):
    r"""Response object for ``BatchDeactivateCreativeWrappers`` method."""


__all__ = tuple(sorted(__protobuf__.manifest))
