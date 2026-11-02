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

from google.ads.admanager_v1.types import slate_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetSlateRequest",
        "ListSlatesRequest",
        "ListSlatesResponse",
        "CreateSlateRequest",
        "BatchCreateSlatesRequest",
        "BatchCreateSlatesResponse",
        "UpdateSlateRequest",
        "BatchUpdateSlatesRequest",
        "BatchUpdateSlatesResponse",
        "BatchArchiveSlatesRequest",
        "BatchArchiveSlatesResponse",
        "BatchUnarchiveSlatesRequest",
        "BatchUnarchiveSlatesResponse",
    },
)


class GetSlateRequest(proto.Message):
    r"""Request message for ``GetSlate`` method.

    Attributes:
        name (str):
            Required. The resource name of the Slate to retrieve.
            Format: ``networks/{network_code}/slates/{slate_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListSlatesRequest(proto.Message):
    r"""Request message for ``ListSlates`` method.

    Attributes:
        parent (str):
            Required. The parent resource containing the Slates. Format:
            ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of ``Slates`` to return. The
            service may return fewer than this value. If unspecified, at
            most 50 ``Slates`` will be returned. The maximum value is
            1000; values above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListSlates`` call. Provide this to retrieve the subsequent
            page.

            When paginating, all other parameters provided to
            ``ListSlates`` must match the call that provided the page
            token.
        filter (str):
            Optional. Expression to filter the response. See syntax
            details at https://google.aip.dev/160

            **Filterable fields:**

            - ``displayName``
            - ``name``
            - ``status``
        order_by (str):
            Optional. Expression to specify sorting
            order. See syntax details at
            https://google.aip.dev/132#ordering
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


class ListSlatesResponse(proto.Message):
    r"""Response message for ``ListSlates`` method.

    Attributes:
        slates (MutableSequence[google.ads.admanager_v1.types.Slate]):
            The ``Slate`` objects from the specified network.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of ``Slate`` objects. If a filter was included
            in the request, this reflects the total number after
            filtering.

            ``total_size`` will not be returned if ``skip`` is nonzero.
    """

    @property
    def raw_page(self):
        return self

    slates: MutableSequence[slate_messages.Slate] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=slate_messages.Slate,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CreateSlateRequest(proto.Message):
    r"""Request object for ``CreateSlate`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this ``Slate`` will be
            created. Format: ``networks/{network_code}``
        slate (google.ads.admanager_v1.types.Slate):
            Required. The ``Slate`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    slate: slate_messages.Slate = proto.Field(
        proto.MESSAGE,
        number=2,
        message=slate_messages.Slate,
    )


class BatchCreateSlatesRequest(proto.Message):
    r"""Request object for ``BatchCreateSlates`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``Slates`` will be
            created. Format: ``networks/{network_code}`` The parent
            field in the CreateSlateRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.CreateSlateRequest]):
            Required. The ``Slate`` objects to create. A maximum of 100
            objects can be created in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateSlateRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateSlateRequest",
    )


class BatchCreateSlatesResponse(proto.Message):
    r"""Response object for ``BatchCreateSlates`` method.

    Attributes:
        slates (MutableSequence[google.ads.admanager_v1.types.Slate]):
            The ``Slate`` objects created.
    """

    slates: MutableSequence[slate_messages.Slate] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=slate_messages.Slate,
    )


class UpdateSlateRequest(proto.Message):
    r"""Request object for ``UpdateSlate`` method.

    Attributes:
        slate (google.ads.admanager_v1.types.Slate):
            Required. The ``Slate`` to update.

            The ``Slate``'s ``name`` is used to identify the ``Slate``
            to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    slate: slate_messages.Slate = proto.Field(
        proto.MESSAGE,
        number=1,
        message=slate_messages.Slate,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateSlatesRequest(proto.Message):
    r"""Request object for ``BatchUpdateSlates`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``Slates`` will be
            updated. Format: ``networks/{network_code}`` The parent
            field in the UpdateSlateRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.UpdateSlateRequest]):
            Required. The ``Slate`` objects to update. A maximum of 100
            objects can be updated in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateSlateRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdateSlateRequest",
    )


class BatchUpdateSlatesResponse(proto.Message):
    r"""Response object for ``BatchUpdateSlates`` method.

    Attributes:
        slates (MutableSequence[google.ads.admanager_v1.types.Slate]):
            The ``Slate`` objects updated.
    """

    slates: MutableSequence[slate_messages.Slate] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=slate_messages.Slate,
    )


class BatchArchiveSlatesRequest(proto.Message):
    r"""Request message for ``BatchArchiveSlates`` method.

    Attributes:
        parent (str):
            Required. The parent resource containing the slates. Format:
            "networks/{network_code}".
        names (MutableSequence[str]):
            Required. The resource names of the slates to archive.
            Format: "networks/{network_code}/slates/{slate_id}".
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchArchiveSlatesResponse(proto.Message):
    r"""Response message for ``BatchArchiveSlates`` method."""


class BatchUnarchiveSlatesRequest(proto.Message):
    r"""Request message for ``BatchUnarchiveSlates`` method.

    Attributes:
        parent (str):
            Required. The parent resource containing the slates. Format:
            "networks/{network_code}".
        names (MutableSequence[str]):
            Required. The resource names of the slates to unarchive.
            Format: "networks/{network_code}/slates/{slate_id}".
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchUnarchiveSlatesResponse(proto.Message):
    r"""Response message for ``BatchUnarchiveSlates`` method."""


__all__ = tuple(sorted(__protobuf__.manifest))
