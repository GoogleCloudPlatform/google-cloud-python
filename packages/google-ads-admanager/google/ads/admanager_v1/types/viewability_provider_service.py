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

from google.ads.admanager_v1.types import viewability_provider_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetViewabilityProviderRequest",
        "ListViewabilityProvidersRequest",
        "ListViewabilityProvidersResponse",
        "CreateViewabilityProviderRequest",
        "BatchCreateViewabilityProvidersRequest",
        "BatchCreateViewabilityProvidersResponse",
        "UpdateViewabilityProviderRequest",
        "BatchUpdateViewabilityProvidersRequest",
        "BatchUpdateViewabilityProvidersResponse",
    },
)


class GetViewabilityProviderRequest(proto.Message):
    r"""Request object for ``GetViewabilityProvider`` method.

    Attributes:
        name (str):
            Required. The resource name of the
            [ViewabilityProvider][google.ads.admanager.v1.ViewabilityProvider].
            Format:
            ``networks/{network_code}/viewabilityProviders/{viewability_provider}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListViewabilityProvidersRequest(proto.Message):
    r"""Request object for ``ListViewabilityProviders`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            [ViewabilityProviders][google.ads.admanager.v1.ViewabilityProvider].
            Format: ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of
            [ViewabilityProviders][google.ads.admanager.v1.ViewabilityProvider]
            to return. The service may return fewer than this value. If
            unspecified, at most 50
            [ViewabilityProviders][google.ads.admanager.v1.ViewabilityProvider]
            will be returned. The maximum value is 1000; values above
            1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListViewabilityProviders`` call. Provide this to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``ListViewabilityProviders`` must match the call that
            provided the page token.
        filter (str):
            Optional. Expression to filter the response. See syntax
            details at
            https://developers.google.com/ad-manager/api/beta/filters

            **Filterable fields:**

            - ``address``
            - ``comment``
            - ``displayName``
            - ``email``
            - ``externalId``
            - ``fax``
            - ``name``
            - ``phone``
            - ``primaryContact``
            - ``rejectionTrackerUrl``
            - ``vendorKey``
            - ``verificationScriptUrl``
            - ``verificationScriptUrlParameters``
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


class ListViewabilityProvidersResponse(proto.Message):
    r"""Response object for ``ListViewabilityProviders`` containing matching
    [ViewabilityProvider][google.ads.admanager.v1.ViewabilityProvider]
    objects.

    Attributes:
        viewability_providers (MutableSequence[google.ads.admanager_v1.types.ViewabilityProvider]):
            The
            [ViewabilityProvider][google.ads.admanager.v1.ViewabilityProvider]
            objects from the specified network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of
            [ViewabilityProvider][google.ads.admanager.v1.ViewabilityProvider]
            objects. If a filter was included in the request, this
            reflects the total number after the filtering is applied.

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

    viewability_providers: MutableSequence[
        viewability_provider_messages.ViewabilityProvider
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=viewability_provider_messages.ViewabilityProvider,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CreateViewabilityProviderRequest(proto.Message):
    r"""Request object for ``CreateViewabilityProvider`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this
            [ViewabilityProvider][google.ads.admanager.v1.ViewabilityProvider]
            will be created. Format: ``networks/{network_code}``
        viewability_provider (google.ads.admanager_v1.types.ViewabilityProvider):
            Required. The
            [ViewabilityProvider][google.ads.admanager.v1.ViewabilityProvider]
            to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    viewability_provider: viewability_provider_messages.ViewabilityProvider = (
        proto.Field(
            proto.MESSAGE,
            number=2,
            message=viewability_provider_messages.ViewabilityProvider,
        )
    )


class BatchCreateViewabilityProvidersRequest(proto.Message):
    r"""Request object for ``BatchCreateViewabilityProviders`` method.

    Attributes:
        parent (str):
            Required. The parent resource where
            [ViewabilityProviders][google.ads.admanager.v1.ViewabilityProvider]
            will be created. Format: ``networks/{network_code}`` The
            parent field in the CreateViewabilityProviderRequest must
            match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.CreateViewabilityProviderRequest]):
            Required. The
            [ViewabilityProvider][google.ads.admanager.v1.ViewabilityProvider]
            objects to create. A maximum of 100 objects can be created
            in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateViewabilityProviderRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateViewabilityProviderRequest",
    )


class BatchCreateViewabilityProvidersResponse(proto.Message):
    r"""Response object for ``BatchCreateViewabilityProviders`` method.

    Attributes:
        viewability_providers (MutableSequence[google.ads.admanager_v1.types.ViewabilityProvider]):
            The
            [ViewabilityProvider][google.ads.admanager.v1.ViewabilityProvider]
            objects created.
    """

    viewability_providers: MutableSequence[
        viewability_provider_messages.ViewabilityProvider
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=viewability_provider_messages.ViewabilityProvider,
    )


class UpdateViewabilityProviderRequest(proto.Message):
    r"""Request object for ``UpdateViewabilityProvider`` method.

    Attributes:
        viewability_provider (google.ads.admanager_v1.types.ViewabilityProvider):
            Required. The
            [ViewabilityProvider][google.ads.admanager.v1.ViewabilityProvider]
            to update.

            The
            [ViewabilityProvider][google.ads.admanager.v1.ViewabilityProvider]'s
            ``name`` is used to identify the
            [ViewabilityProvider][google.ads.admanager.v1.ViewabilityProvider]
            to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    viewability_provider: viewability_provider_messages.ViewabilityProvider = (
        proto.Field(
            proto.MESSAGE,
            number=1,
            message=viewability_provider_messages.ViewabilityProvider,
        )
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateViewabilityProvidersRequest(proto.Message):
    r"""Request object for ``BatchUpdateViewabilityProviders`` method.

    Attributes:
        parent (str):
            Required. The parent resource where
            [ViewabilityProviders][google.ads.admanager.v1.ViewabilityProvider]
            will be updated. Format: ``networks/{network_code}`` The
            parent field in the UpdateViewabilityProviderRequest must
            match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.UpdateViewabilityProviderRequest]):
            Required. The
            [ViewabilityProvider][google.ads.admanager.v1.ViewabilityProvider]
            objects to update. A maximum of 100 objects can be updated
            in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateViewabilityProviderRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdateViewabilityProviderRequest",
    )


class BatchUpdateViewabilityProvidersResponse(proto.Message):
    r"""Response object for ``BatchUpdateViewabilityProviders`` method.

    Attributes:
        viewability_providers (MutableSequence[google.ads.admanager_v1.types.ViewabilityProvider]):
            The
            [ViewabilityProvider][google.ads.admanager.v1.ViewabilityProvider]
            objects updated.
    """

    viewability_providers: MutableSequence[
        viewability_provider_messages.ViewabilityProvider
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=viewability_provider_messages.ViewabilityProvider,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
