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

from google.ads.admanager_v1.types import custom_targeting_value_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetCustomTargetingValueRequest",
        "ListCustomTargetingValuesRequest",
        "ListCustomTargetingValuesResponse",
        "CreateCustomTargetingValueRequest",
        "BatchCreateCustomTargetingValuesRequest",
        "BatchCreateCustomTargetingValuesResponse",
        "UpdateCustomTargetingValueRequest",
        "BatchUpdateCustomTargetingValuesRequest",
        "BatchUpdateCustomTargetingValuesResponse",
        "ActivateCustomTargetingValueRequest",
        "BatchActivateCustomTargetingValuesRequest",
        "BatchActivateCustomTargetingValuesResponse",
        "DeactivateCustomTargetingValueRequest",
        "BatchDeactivateCustomTargetingValuesRequest",
        "BatchDeactivateCustomTargetingValuesResponse",
    },
)


class GetCustomTargetingValueRequest(proto.Message):
    r"""Request object for ``GetCustomTargetingValue`` method.

    Attributes:
        name (str):
            Required. The resource name of the CustomTargetingValue.
            Format:
            ``networks/{network_code}/customTargetingValues/{custom_targeting_value_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListCustomTargetingValuesRequest(proto.Message):
    r"""Request object for ``ListCustomTargetingValues`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            CustomTargetingValues. Format: ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of ``CustomTargetingValues`` to
            return. The service may return fewer than this value. If
            unspecified, at most 50 ``CustomTargetingValues`` will be
            returned. The maximum value is 1000; values above 1000 will
            be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListCustomTargetingValues`` call. Provide this to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``ListCustomTargetingValues`` must match the call that
            provided the page token.
        filter (str):
            Optional. Expression to filter the response. See syntax
            details at
            https://developers.google.com/ad-manager/api/beta/filters

            **Filterable fields:**

            - ``adTagName``
            - ``customTargetingKey``
            - ``displayName``
            - ``matchType``
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


class ListCustomTargetingValuesResponse(proto.Message):
    r"""Response object for ``ListCustomTargetingValuesRequest`` containing
    matching ``CustomTargetingValue`` objects.

    Attributes:
        custom_targeting_values (MutableSequence[google.ads.admanager_v1.types.CustomTargetingValue]):
            The ``CustomTargetingValue`` objects from the specified
            network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of ``CustomTargetingValue`` objects. If a
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

    custom_targeting_values: MutableSequence[
        custom_targeting_value_messages.CustomTargetingValue
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=custom_targeting_value_messages.CustomTargetingValue,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CreateCustomTargetingValueRequest(proto.Message):
    r"""Request object for ``CreateCustomTargetingValue`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            CustomTargetingValues. Format: ``networks/{network_code}``
        custom_targeting_value (google.ads.admanager_v1.types.CustomTargetingValue):
            Required. The ``CustomTargetingValue`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    custom_targeting_value: custom_targeting_value_messages.CustomTargetingValue = (
        proto.Field(
            proto.MESSAGE,
            number=2,
            message=custom_targeting_value_messages.CustomTargetingValue,
        )
    )


class BatchCreateCustomTargetingValuesRequest(proto.Message):
    r"""Request object for ``BatchCreateCustomTargetingValues`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            CustomTargetingValues. Format: ``networks/{network_code}``
        requests (MutableSequence[google.ads.admanager_v1.types.CreateCustomTargetingValueRequest]):
            Required. The ``CustomTargetingValue`` objects to create. A
            maximum of 100 objects can be created in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateCustomTargetingValueRequest"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="CreateCustomTargetingValueRequest",
        )
    )


class BatchCreateCustomTargetingValuesResponse(proto.Message):
    r"""Response object for ``BatchCreateCustomTargetingValues`` method.

    Attributes:
        custom_targeting_values (MutableSequence[google.ads.admanager_v1.types.CustomTargetingValue]):
            The ``CustomTargetingValue`` objects created.
    """

    custom_targeting_values: MutableSequence[
        custom_targeting_value_messages.CustomTargetingValue
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=custom_targeting_value_messages.CustomTargetingValue,
    )


class UpdateCustomTargetingValueRequest(proto.Message):
    r"""Request object for ``UpdateCustomTargetingValue`` method.

    Attributes:
        custom_targeting_value (google.ads.admanager_v1.types.CustomTargetingValue):
            Required. The ``CustomTargetingValue`` to update.

            The ``CustomTargetingValue``'s ``name`` is used to identify
            the ``CustomTargetingValue`` to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    custom_targeting_value: custom_targeting_value_messages.CustomTargetingValue = (
        proto.Field(
            proto.MESSAGE,
            number=1,
            message=custom_targeting_value_messages.CustomTargetingValue,
        )
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateCustomTargetingValuesRequest(proto.Message):
    r"""Request object for ``BatchUpdateCustomTargetingValues`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            CustomTargetingValues. Format: ``networks/{network_code}``
        requests (MutableSequence[google.ads.admanager_v1.types.UpdateCustomTargetingValueRequest]):
            Required. The ``CustomTargetingValue`` objects to update. A
            maximum of 100 objects can be updated in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateCustomTargetingValueRequest"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="UpdateCustomTargetingValueRequest",
        )
    )


class BatchUpdateCustomTargetingValuesResponse(proto.Message):
    r"""Response object for ``BatchUpdateCustomTargetingValues`` method.

    Attributes:
        custom_targeting_values (MutableSequence[google.ads.admanager_v1.types.CustomTargetingValue]):
            The ``CustomTargetingValue`` objects updated.
    """

    custom_targeting_values: MutableSequence[
        custom_targeting_value_messages.CustomTargetingValue
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=custom_targeting_value_messages.CustomTargetingValue,
    )


class ActivateCustomTargetingValueRequest(proto.Message):
    r"""Request message to activate a CustomTargetingValue.

    Attributes:
        name (str):
            Required. The resource name of the CustomTargetingValue.
            Format:
            ``networks/{network_code}/customTargetingValues/{custom_targeting_value_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class BatchActivateCustomTargetingValuesRequest(proto.Message):
    r"""Request object for ``BatchActivateCustomTargetingValues`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            CustomTargetingValues. Format: ``networks/{network_code}``
        requests (MutableSequence[google.ads.admanager_v1.types.ActivateCustomTargetingValueRequest]):
            Required. The ``CustomTargetingValue`` objects to activate.
            A maximum of 100 objects can be activated in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["ActivateCustomTargetingValueRequest"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="ActivateCustomTargetingValueRequest",
        )
    )


class BatchActivateCustomTargetingValuesResponse(proto.Message):
    r"""Response object for ``BatchActivateCustomTargetingValues`` method."""


class DeactivateCustomTargetingValueRequest(proto.Message):
    r"""Request message to deactivate a CustomTargetingValue.

    Attributes:
        name (str):
            Required. The resource name of the CustomTargetingValue.
            Format:
            ``networks/{network_code}/customTargetingValues/{custom_targeting_value_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class BatchDeactivateCustomTargetingValuesRequest(proto.Message):
    r"""Request message for ``BatchDeactivateCustomTargetingValues`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            CustomTargetingValues. Format: ``networks/{network_code}/``
        requests (MutableSequence[google.ads.admanager_v1.types.DeactivateCustomTargetingValueRequest]):
            Required. The ``CustomTargetingValue`` objects to
            deactivate.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["DeactivateCustomTargetingValueRequest"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="DeactivateCustomTargetingValueRequest",
        )
    )


class BatchDeactivateCustomTargetingValuesResponse(proto.Message):
    r"""Response object for ``BatchDeactivateCustomTargetingValues`` method."""


__all__ = tuple(sorted(__protobuf__.manifest))
