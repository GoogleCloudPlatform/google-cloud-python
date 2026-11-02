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

import proto  # type: ignore

from google.ads.admanager_v1.types import mobile_device_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetMobileDeviceRequest",
        "ListMobileDevicesRequest",
        "ListMobileDevicesResponse",
    },
)


class GetMobileDeviceRequest(proto.Message):
    r"""Request object for ``GetMobileDevice`` method.

    Attributes:
        name (str):
            Required. The resource name of the MobileDevice. Format:
            ``networks/{network_code}/mobileDevices/{mobile_device_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListMobileDevicesRequest(proto.Message):
    r"""Request object for ``ListMobileDevices`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            MobileDevices. Format: ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of ``MobileDevices`` to return.
            The service may return fewer than this value. If
            unspecified, at most 50 ``MobileDevices`` will be returned.
            The maximum value is 1000; values greater than 1000 will be
            coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListMobileDevices`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListMobileDevices`` must match the call that provided the
            page token.
        filter (str):
            Optional. Expression to filter the response. See syntax
            details at
            https://developers.google.com/ad-manager/api/beta/filters

            **Filterable fields:**

            - ``displayName``
            - ``manufacturer``
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


class ListMobileDevicesResponse(proto.Message):
    r"""Response object for ``ListMobileDevicesRequest`` containing matching
    ``MobileDevice`` objects.

    Attributes:
        mobile_devices (MutableSequence[google.ads.admanager_v1.types.MobileDevice]):
            The ``MobileDevice`` objects from the specified network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of ``MobileDevice`` objects. If a filter was
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

    mobile_devices: MutableSequence[mobile_device_messages.MobileDevice] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=mobile_device_messages.MobileDevice,
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


__all__ = tuple(sorted(__protobuf__.manifest))
