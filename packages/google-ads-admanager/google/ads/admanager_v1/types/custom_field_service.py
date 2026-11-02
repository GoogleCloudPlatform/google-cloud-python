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

from google.ads.admanager_v1.types import custom_field_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetCustomFieldRequest",
        "ListCustomFieldsRequest",
        "ListCustomFieldsResponse",
        "CreateCustomFieldRequest",
        "BatchCreateCustomFieldsRequest",
        "BatchCreateCustomFieldsResponse",
        "UpdateCustomFieldRequest",
        "BatchUpdateCustomFieldsRequest",
        "BatchUpdateCustomFieldsResponse",
        "BatchActivateCustomFieldsRequest",
        "BatchActivateCustomFieldsResponse",
        "BatchDeactivateCustomFieldsRequest",
        "BatchDeactivateCustomFieldsResponse",
    },
)


class GetCustomFieldRequest(proto.Message):
    r"""Request object for ``GetCustomField`` method.

    Attributes:
        name (str):
            Required. The resource name of the CustomField. Format:
            ``networks/{network_code}/customFields/{custom_field_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListCustomFieldsRequest(proto.Message):
    r"""Request object for ``ListCustomFields`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            CustomFields. Format: ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of ``CustomFields`` to return.
            The service may return fewer than this value. If
            unspecified, at most 50 ``CustomFields`` will be returned.
            The maximum value is 1000; values greater than 1000 will be
            coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListCustomFields`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListCustomFields`` must match the call that provided the
            page token.
        filter (str):
            Optional. Expression to filter the response. See syntax
            details at
            https://developers.google.com/ad-manager/api/beta/filters

            **Filterable fields:**

            - ``dataType``
            - ``description``
            - ``displayName``
            - ``entityType``
            - ``name``
            - ``options.customFieldOptionId``
            - ``options.displayName``
            - ``status``
            - ``visibility``
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


class ListCustomFieldsResponse(proto.Message):
    r"""Response object for ``ListCustomFieldsRequest`` containing matching
    ``CustomField`` objects.

    Attributes:
        custom_fields (MutableSequence[google.ads.admanager_v1.types.CustomField]):
            The ``CustomField`` objects from the specified network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of ``CustomField`` objects. If a filter was
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

    custom_fields: MutableSequence[custom_field_messages.CustomField] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=custom_field_messages.CustomField,
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


class CreateCustomFieldRequest(proto.Message):
    r"""Request object for ``CreateCustomField`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this ``CustomField``
            will be created. Format: ``networks/{network_code}``
        custom_field (google.ads.admanager_v1.types.CustomField):
            Required. The ``CustomField`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    custom_field: custom_field_messages.CustomField = proto.Field(
        proto.MESSAGE,
        number=2,
        message=custom_field_messages.CustomField,
    )


class BatchCreateCustomFieldsRequest(proto.Message):
    r"""Request object for ``BatchCreateCustomFields`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``CustomFields`` will be
            created. Format: ``networks/{network_code}`` The parent
            field in the CreateCustomFieldRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.CreateCustomFieldRequest]):
            Required. The ``CustomField`` objects to create. A maximum
            of 100 objects can be created in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateCustomFieldRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateCustomFieldRequest",
    )


class BatchCreateCustomFieldsResponse(proto.Message):
    r"""Response object for ``BatchCreateCustomFields`` method.

    Attributes:
        custom_fields (MutableSequence[google.ads.admanager_v1.types.CustomField]):
            The ``CustomField`` objects created.
    """

    custom_fields: MutableSequence[custom_field_messages.CustomField] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=custom_field_messages.CustomField,
        )
    )


class UpdateCustomFieldRequest(proto.Message):
    r"""Request object for ``UpdateCustomField`` method.

    Attributes:
        custom_field (google.ads.admanager_v1.types.CustomField):
            Required. The ``CustomField`` to update.

            The ``CustomField``'s ``name`` is used to identify the
            ``CustomField`` to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    custom_field: custom_field_messages.CustomField = proto.Field(
        proto.MESSAGE,
        number=1,
        message=custom_field_messages.CustomField,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateCustomFieldsRequest(proto.Message):
    r"""Request object for ``BatchUpdateCustomFields`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``CustomFields`` will be
            updated. Format: ``networks/{network_code}`` The parent
            field in the UpdateCustomFieldRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.UpdateCustomFieldRequest]):
            Required. The ``CustomField`` objects to update. A maximum
            of 100 objects can be updated in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateCustomFieldRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdateCustomFieldRequest",
    )


class BatchUpdateCustomFieldsResponse(proto.Message):
    r"""Response object for ``BatchUpdateCustomFields`` method.

    Attributes:
        custom_fields (MutableSequence[google.ads.admanager_v1.types.CustomField]):
            The ``CustomField`` objects updated.
    """

    custom_fields: MutableSequence[custom_field_messages.CustomField] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=custom_field_messages.CustomField,
        )
    )


class BatchActivateCustomFieldsRequest(proto.Message):
    r"""Request message for ``BatchActivateCustomFields`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the ``CustomField`` objects
            to activate. Format:
            ``networks/{network_code}/customFields/{custom_field_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class BatchActivateCustomFieldsResponse(proto.Message):
    r"""Response object for ``BatchActivateCustomFields`` method."""


class BatchDeactivateCustomFieldsRequest(proto.Message):
    r"""Request message for ``BatchDeactivateCustomFields`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the ``CustomField`` objects
            to deactivate. Format:
            ``networks/{network_code}/customFields/{custom_field_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class BatchDeactivateCustomFieldsResponse(proto.Message):
    r"""Response object for ``BatchDeactivateCustomFields`` method."""


__all__ = tuple(sorted(__protobuf__.manifest))
