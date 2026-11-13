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

from google.ads.admanager_v1.types import network_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "UpdateNetworkRequest",
        "GetNetworkRequest",
        "ListNetworksRequest",
        "ListNetworksResponse",
        "ProvisionTestNetworkRequest",
        "GetDefaultThirdPartyDataDeclarationRequest",
    },
)


class UpdateNetworkRequest(proto.Message):
    r"""Request for the ``UpdateNetwork`` method.

    Attributes:
        network (google.ads.admanager_v1.types.Network):
            Required. The ``Network`` to update.

            The ``Network``'s ``name`` is used to identify the
            ``Network`` to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    network: network_messages.Network = proto.Field(
        proto.MESSAGE,
        number=1,
        message=network_messages.Network,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetNetworkRequest(proto.Message):
    r"""Request to get Network

    Attributes:
        name (str):
            Required. Resource name of Network. Format:
            networks/{network_code}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListNetworksRequest(proto.Message):
    r"""Request object for ``ListNetworks`` method.

    Attributes:
        page_size (int):
            Optional. The maximum number of ``Network``\ s to return.
            The service may return fewer than this value. If
            unspecified, at most 50 ``Network``\ s will be returned. The
            maximum value is 1000; values greater than 1000 will be
            coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListNetworks`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListNetworks`` must match the call that provided the page
            token.
        skip (int):
            Optional. Number of individual resources to
            skip while paginating.
    """

    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )
    skip: int = proto.Field(
        proto.INT32,
        number=5,
    )


class ListNetworksResponse(proto.Message):
    r"""Response object for ``ListNetworks`` method.

    Attributes:
        networks (MutableSequence[google.ads.admanager_v1.types.Network]):
            The ``Network``\ s a user has access to.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of ``Network``\ s.

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

    networks: MutableSequence[network_messages.Network] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=network_messages.Network,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class ProvisionTestNetworkRequest(proto.Message):
    r"""Request for the ``ProvisionTestNetwork`` method."""


class GetDefaultThirdPartyDataDeclarationRequest(proto.Message):
    r"""Request for the ``GetDefaultThirdPartyDataDeclaration`` method.

    Attributes:
        name (str):
            Required. Resource name of DefaultThirdPartyDataDeclaration.
            Format:
            networks/{network_code}/defaultThirdPartyDataDeclaration
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
