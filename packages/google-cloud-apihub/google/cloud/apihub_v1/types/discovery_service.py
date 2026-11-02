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

from google.cloud.apihub_v1.types import common_fields

__protobuf__ = proto.module(
    package="google.cloud.apihub.v1",
    manifest={
        "ListDiscoveredApiObservationsRequest",
        "ListDiscoveredApiObservationsResponse",
        "ListDiscoveredApiOperationsRequest",
        "ListDiscoveredApiOperationsResponse",
        "GetDiscoveredApiObservationRequest",
        "GetDiscoveredApiOperationRequest",
    },
)


class ListDiscoveredApiObservationsRequest(proto.Message):
    r"""Message for requesting list of DiscoveredApiObservations

    Attributes:
        parent (str):
            Required. The parent, which owns this
            collection of ApiObservations. Format:

            projects/{project}/locations/{location}
        page_size (int):
            Optional. The maximum number of
            ApiObservations to return. The service may
            return fewer than this value. If unspecified, at
            most 10 ApiObservations will be returned. The
            maximum value is 1000; values above 1000 will be
            coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListApiObservations`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListApiObservations`` must match the call that provided
            the page token.
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


class ListDiscoveredApiObservationsResponse(proto.Message):
    r"""Message for response to listing DiscoveredApiObservations

    Attributes:
        discovered_api_observations (MutableSequence[google.cloud.apihub_v1.types.DiscoveredApiObservation]):
            The DiscoveredApiObservation from the
            specified project and location.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    discovered_api_observations: MutableSequence[
        common_fields.DiscoveredApiObservation
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=common_fields.DiscoveredApiObservation,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListDiscoveredApiOperationsRequest(proto.Message):
    r"""Message for requesting list of DiscoveredApiOperations

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            DiscoveredApiOperations. Format:
            projects/{project}/locations/{location}/discoveredApiObservations/{discovered_api_observation}
        page_size (int):
            Optional. DiscoveredApiOperations will be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListDiscoveredApiApiOperations`` call. Provide this to
            retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListDiscoveredApiApiOperations`` must match the call that
            provided the page token.
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


class ListDiscoveredApiOperationsResponse(proto.Message):
    r"""Message for response to listing DiscoveredApiOperations

    Attributes:
        discovered_api_operations (MutableSequence[google.cloud.apihub_v1.types.DiscoveredApiOperation]):
            The DiscoveredApiOperations from the
            specified project, location and
            DiscoveredApiObservation.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    discovered_api_operations: MutableSequence[common_fields.DiscoveredApiOperation] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=common_fields.DiscoveredApiOperation,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetDiscoveredApiObservationRequest(proto.Message):
    r"""Message for requesting a DiscoveredApiObservation

    Attributes:
        name (str):
            Required. The name of the DiscoveredApiObservation to
            retrieve. Format:
            projects/{project}/locations/{location}/discoveredApiObservations/{discovered_api_observation}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetDiscoveredApiOperationRequest(proto.Message):
    r"""Message for requesting a DiscoveredApiOperation

    Attributes:
        name (str):
            Required. The name of the DiscoveredApiOperation to
            retrieve. Format:
            projects/{project}/locations/{location}/discoveredApiObservations/{discovered_api_observation}/discoveredApiOperations/{discovered_api_operation}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
