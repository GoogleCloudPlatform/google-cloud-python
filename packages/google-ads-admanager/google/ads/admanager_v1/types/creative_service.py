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

from google.ads.admanager_v1.types import creative_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetCreativeRequest",
        "ListCreativesRequest",
        "ListCreativesResponse",
        "CreateCreativeRequest",
        "UpdateCreativeRequest",
        "BatchCreateCreativesRequest",
        "BatchCreateCreativesResponse",
        "BatchUpdateCreativesRequest",
        "BatchUpdateCreativesResponse",
        "BatchActivateCreativesRequest",
        "BatchActivateCreativesResponse",
        "BatchDeactivateCreativesRequest",
        "BatchDeactivateCreativesResponse",
    },
)


class GetCreativeRequest(proto.Message):
    r"""Request object for ``GetCreative`` method.

    Attributes:
        name (str):
            Required. The resource name of the Creative. Format:
            ``networks/{network_code}/creatives/{creative_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListCreativesRequest(proto.Message):
    r"""Request object for ``ListCreatives`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            Creatives. Format: networks/{network_code}
        page_size (int):
            Optional. The maximum number of Creatives to
            return. The service may return fewer than this
            value. If unspecified, at most 50 creatives will
            be returned. The maximum value is 1000; values
            greater than 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListCreatives`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListCreatives`` must match the call that provided the page
            token.
        filter (str):
            Optional. Expression to filter the response. See syntax
            details at
            https://developers.google.com/ad-manager/api/beta/filters

            Syntax summary: double-quoted ``"..."`` (never ``'...'``)
            strings and RFC 3339 timestamps, full resource names on
            reference fields (for example,
            ``order = "networks/123/orders/456"``, not ``*Id`` or bare
            IDs), prefix or suffix ``*`` wildcards with ``=``
            (``displayName = "foo*"``), ``:`` for substring or
            repeated-field matching, unquoted enums and booleans,
            uppercase ``AND``/``OR``/``NOT``, and standalone
            ``IN(field, SET(v1, v2))`` (not ``field IN (...)``).

            **Filterable fields:**

            - ``advertiser``
            - ``displayName``
            - ``name``
            - ``thirdPartyDataDeclarationStatus``
            - ``updateTime``
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


class ListCreativesResponse(proto.Message):
    r"""Response object for ``ListCreativesRequest`` containing matching
    ``Creative`` objects.

    Attributes:
        creatives (MutableSequence[google.ads.admanager_v1.types.Creative]):
            The ``Creative`` objects from the specified network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of Creatives. If a filter was included in the
            request, this reflects the total number after the filtering
            is applied.

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

    creatives: MutableSequence[creative_messages.Creative] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=creative_messages.Creative,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CreateCreativeRequest(proto.Message):
    r"""Request object for ``CreateCreative`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this ``Creative`` will
            be created. Format: ``networks/{network_code}``
        creative (google.ads.admanager_v1.types.Creative):
            Required. The ``Creative`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    creative: creative_messages.Creative = proto.Field(
        proto.MESSAGE,
        number=2,
        message=creative_messages.Creative,
    )


class UpdateCreativeRequest(proto.Message):
    r"""Request object for ``UpdateCreative`` method.

    Attributes:
        creative (google.ads.admanager_v1.types.Creative):
            Required. The ``Creative`` to update.

            The ``Creative``'s name is used to identify the ``Creative``
            to update. Format:
            ``networks/{network_code}/creatives/{creative_id}``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    creative: creative_messages.Creative = proto.Field(
        proto.MESSAGE,
        number=1,
        message=creative_messages.Creative,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchCreateCreativesRequest(proto.Message):
    r"""Request object for ``BatchCreateCreatives`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``Creatives`` will be
            created. Format: ``networks/{network_code}`` The parent
            field in the CreateCreativeRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.CreateCreativeRequest]):
            Required. The ``Creative`` objects to create. A maximum of
            100 objects can be created in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateCreativeRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateCreativeRequest",
    )


class BatchCreateCreativesResponse(proto.Message):
    r"""Response object for ``BatchCreateCreatives`` method.

    Attributes:
        creatives (MutableSequence[google.ads.admanager_v1.types.Creative]):
            The ``Creative`` objects created.
    """

    creatives: MutableSequence[creative_messages.Creative] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=creative_messages.Creative,
    )


class BatchUpdateCreativesRequest(proto.Message):
    r"""Request object for ``BatchUpdateCreatives`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``Creatives`` will be
            updated. Format: ``networks/{network_code}`` The parent
            field in the UpdateCreativeRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.UpdateCreativeRequest]):
            Required. The ``Creative`` objects to update. A maximum of
            100 objects can be updated in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateCreativeRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdateCreativeRequest",
    )


class BatchUpdateCreativesResponse(proto.Message):
    r"""Response object for ``BatchUpdateCreatives`` method.

    Attributes:
        creatives (MutableSequence[google.ads.admanager_v1.types.Creative]):
            The ``Creative`` objects updated.
    """

    creatives: MutableSequence[creative_messages.Creative] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=creative_messages.Creative,
    )


class BatchActivateCreativesRequest(proto.Message):
    r"""Request object for ``BatchActivateCreatives`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the ``Creative``\ s to
            activate. Format:
            ``networks/{network_code}/creatives/{creative_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchActivateCreativesResponse(proto.Message):
    r"""Response object for ``BatchActivateCreatives`` method."""


class BatchDeactivateCreativesRequest(proto.Message):
    r"""Request object for ``BatchDeactivateCreatives`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the ``Creative``\ s to
            deactivate. Format:
            ``networks/{network_code}/creatives/{creative_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchDeactivateCreativesResponse(proto.Message):
    r"""Response object for ``BatchDeactivateCreatives`` method."""


__all__ = tuple(sorted(__protobuf__.manifest))
