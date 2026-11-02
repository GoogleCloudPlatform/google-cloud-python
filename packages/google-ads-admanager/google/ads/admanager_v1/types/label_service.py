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

from google.ads.admanager_v1.types import label_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetLabelRequest",
        "ListLabelsRequest",
        "ListLabelsResponse",
        "CreateLabelRequest",
        "BatchCreateLabelsRequest",
        "BatchCreateLabelsResponse",
        "UpdateLabelRequest",
        "BatchUpdateLabelsRequest",
        "BatchUpdateLabelsResponse",
        "BatchActivateLabelsRequest",
        "BatchActivateLabelsResponse",
        "BatchDeactivateLabelsRequest",
        "BatchDeactivateLabelsResponse",
    },
)


class GetLabelRequest(proto.Message):
    r"""Request object for ``GetLabel`` method.

    Attributes:
        name (str):
            Required. The resource name of the Label. Format:
            ``networks/{network_code}/labels/{label_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListLabelsRequest(proto.Message):
    r"""Request object for ``ListLabels`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of Labels.
            Format: ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of ``Labels`` to return. The
            service may return fewer than this value. If unspecified, at
            most 50 ``Labels`` will be returned. The maximum value is
            1000; values greater than 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListLabels`` call. Provide this to retrieve the subsequent
            page.

            When paginating, all other parameters provided to
            ``ListLabels`` must match the call that provided the page
            token.
        filter (str):
            Optional. Expression to filter the response. See syntax
            details at
            https://developers.google.com/ad-manager/api/beta/filters

            **Filterable fields:**

            - ``active``
            - ``description``
            - ``displayName``
            - ``name``
            - ``types``
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


class ListLabelsResponse(proto.Message):
    r"""Response object for ``ListLabelsRequest`` containing matching
    ``Label`` objects.

    Attributes:
        labels (MutableSequence[google.ads.admanager_v1.types.Label]):
            The ``Label`` objects from the specified network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of ``Label`` objects. If a filter was included
            in the request, this reflects the total number after the
            filtering is applied.

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

    labels: MutableSequence[label_messages.Label] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=label_messages.Label,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CreateLabelRequest(proto.Message):
    r"""Request object for ``CreateLabel`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this ``Label`` will be
            created. Format: ``networks/{network_code}``
        label (google.ads.admanager_v1.types.Label):
            Required. The ``Label`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    label: label_messages.Label = proto.Field(
        proto.MESSAGE,
        number=2,
        message=label_messages.Label,
    )


class BatchCreateLabelsRequest(proto.Message):
    r"""Request object for ``BatchCreateLabels`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``Labels`` will be
            created. Format: ``networks/{network_code}`` The parent
            field in the CreateLabelRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.CreateLabelRequest]):
            Required. The ``Label`` objects to create. A maximum of 100
            objects can be created in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateLabelRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateLabelRequest",
    )


class BatchCreateLabelsResponse(proto.Message):
    r"""Response object for ``BatchCreateLabels`` method.

    Attributes:
        labels (MutableSequence[google.ads.admanager_v1.types.Label]):
            The ``Label`` objects created.
    """

    labels: MutableSequence[label_messages.Label] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=label_messages.Label,
    )


class UpdateLabelRequest(proto.Message):
    r"""Request object for ``UpdateLabel`` method.

    Attributes:
        label (google.ads.admanager_v1.types.Label):
            Required. The ``Label`` to update.

            The ``Label``'s ``name`` is used to identify the ``Label``
            to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    label: label_messages.Label = proto.Field(
        proto.MESSAGE,
        number=1,
        message=label_messages.Label,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateLabelsRequest(proto.Message):
    r"""Request object for ``BatchUpdateLabels`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``Labels`` will be
            updated. Format: ``networks/{network_code}`` The parent
            field in the UpdateLabelRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.UpdateLabelRequest]):
            Required. The ``Label`` objects to update. A maximum of 100
            objects can be updated in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateLabelRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdateLabelRequest",
    )


class BatchUpdateLabelsResponse(proto.Message):
    r"""Response object for ``BatchUpdateLabels`` method.

    Attributes:
        labels (MutableSequence[google.ads.admanager_v1.types.Label]):
            The ``Label`` objects updated.
    """

    labels: MutableSequence[label_messages.Label] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=label_messages.Label,
    )


class BatchActivateLabelsRequest(proto.Message):
    r"""Request message for ``BatchActivateLabels`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. Resource names for the Label. Format:
            ``networks/{network_code}/labels/{label_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchActivateLabelsResponse(proto.Message):
    r"""Response message for ``BatchActivateLabels`` method."""


class BatchDeactivateLabelsRequest(proto.Message):
    r"""Request message for ``BatchDeactivateLabels`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. Resource names for the Label. Format:
            ``networks/{network_code}/labels/{label_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchDeactivateLabelsResponse(proto.Message):
    r"""Response message for ``BatchDeactivateLabels`` method."""


__all__ = tuple(sorted(__protobuf__.manifest))
