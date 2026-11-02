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

from google.ads.admanager_v1.types import break_template_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetBreakTemplateRequest",
        "ListBreakTemplatesRequest",
        "ListBreakTemplatesResponse",
        "CreateBreakTemplateRequest",
        "BatchCreateBreakTemplatesRequest",
        "BatchCreateBreakTemplatesResponse",
        "UpdateBreakTemplateRequest",
        "BatchUpdateBreakTemplatesRequest",
        "BatchUpdateBreakTemplatesResponse",
    },
)


class GetBreakTemplateRequest(proto.Message):
    r"""Request object for ``GetBreakTemplate`` method.

    Attributes:
        name (str):
            Required. The resource name of the ``BreakTemplate``.
            Format:
            ``networks/{network_code}/breakTemplates/{break_template_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListBreakTemplatesRequest(proto.Message):
    r"""Request object for ``ListBreakTemplates`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            ``BreakTemplates``. Format: ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of ``BreakTemplates`` to
            return. The service may return fewer than this value. If
            unspecified, at most 50 ``BreakTemplates`` will be returned.
            The maximum value is 1000; values above 1000 will be coerced
            to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListBreakTemplates`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListBreakTemplates`` must match the call that provided the
            page token.
        filter (str):
            Optional. Expression to filter the response. See syntax
            details at
            https://developers.google.com/ad-manager/api/beta/filters

            **Filterable fields:**

            - ``adBreakOptimizationType``
            - ``adTagName``
            - ``customTemplate``
            - ``displayName``
            - ``fillOrderDirectionType``
            - ``name``
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


class ListBreakTemplatesResponse(proto.Message):
    r"""Response object for ``ListBreakTemplatesRequest`` containing
    matching ``BreakTemplate`` objects.

    Attributes:
        break_templates (MutableSequence[google.ads.admanager_v1.types.BreakTemplate]):
            The ``BreakTemplate`` objects from the specified network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of ``BreakTemplate`` objects. If a filter was
            included in the request, this reflects the total number
            after the filtering is applied.

            ``total_size`` will not be calculated in the response unless
            it has been included in a response field mask. The response
            field mask can be provided to the method by using the URL
            parameter ``$fields`` or ``fields``, or by using the
            HTTP/gRPC header ``X-Goog-FieldMask``.

            For more information, see
            https://developers.google.com/ad-manager/api/beta/field-masks
    """

    @property
    def raw_page(self):
        return self

    break_templates: MutableSequence[break_template_messages.BreakTemplate] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=break_template_messages.BreakTemplate,
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


class CreateBreakTemplateRequest(proto.Message):
    r"""Request object for ``CreateBreakTemplate`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this ``BreakTemplate``
            will be created. Format: ``networks/{network_code}``
        break_template (google.ads.admanager_v1.types.BreakTemplate):
            Required. The ``BreakTemplate`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    break_template: break_template_messages.BreakTemplate = proto.Field(
        proto.MESSAGE,
        number=2,
        message=break_template_messages.BreakTemplate,
    )


class BatchCreateBreakTemplatesRequest(proto.Message):
    r"""Request object for ``BatchCreateBreakTemplates`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``BreakTemplates`` will
            be created. Format: ``networks/{network_code}`` The parent
            field in the ``CreateBreakTemplateRequest`` must match this
            field.
        requests (MutableSequence[google.ads.admanager_v1.types.CreateBreakTemplateRequest]):
            Required. The ``BreakTemplate`` objects to create. A maximum
            of 100 objects can be created in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateBreakTemplateRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateBreakTemplateRequest",
    )


class BatchCreateBreakTemplatesResponse(proto.Message):
    r"""Response object for ``BatchCreateBreakTemplates`` method.

    Attributes:
        break_templates (MutableSequence[google.ads.admanager_v1.types.BreakTemplate]):
            The ``BreakTemplate`` objects created.
    """

    break_templates: MutableSequence[break_template_messages.BreakTemplate] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=break_template_messages.BreakTemplate,
        )
    )


class UpdateBreakTemplateRequest(proto.Message):
    r"""Request object for ``UpdateBreakTemplate`` method.

    Attributes:
        break_template (google.ads.admanager_v1.types.BreakTemplate):
            Required. The ``BreakTemplate`` to update.

            The ``BreakTemplate``'s ``name`` is used to identify the
            ``BreakTemplate`` to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    break_template: break_template_messages.BreakTemplate = proto.Field(
        proto.MESSAGE,
        number=1,
        message=break_template_messages.BreakTemplate,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateBreakTemplatesRequest(proto.Message):
    r"""Request object for ``BatchUpdateBreakTemplates`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``BreakTemplates`` will
            be updated. Format: ``networks/{network_code}`` The parent
            field in the ``UpdateBreakTemplateRequest`` must match this
            field.
        requests (MutableSequence[google.ads.admanager_v1.types.UpdateBreakTemplateRequest]):
            Required. The ``BreakTemplate`` objects to update. A maximum
            of 100 objects can be updated in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateBreakTemplateRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdateBreakTemplateRequest",
    )


class BatchUpdateBreakTemplatesResponse(proto.Message):
    r"""Response object for ``BatchUpdateBreakTemplates`` method.

    Attributes:
        break_templates (MutableSequence[google.ads.admanager_v1.types.BreakTemplate]):
            The ``BreakTemplate`` objects updated.
    """

    break_templates: MutableSequence[break_template_messages.BreakTemplate] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=break_template_messages.BreakTemplate,
        )
    )


__all__ = tuple(sorted(__protobuf__.manifest))
