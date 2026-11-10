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

from google.ads.admanager_v1.types import traffic_forecast_segment_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetTrafficForecastSegmentRequest",
        "ListTrafficForecastSegmentsRequest",
        "ListTrafficForecastSegmentsResponse",
        "CreateTrafficForecastSegmentRequest",
        "BatchCreateTrafficForecastSegmentsRequest",
        "BatchCreateTrafficForecastSegmentsResponse",
        "UpdateTrafficForecastSegmentRequest",
        "BatchUpdateTrafficForecastSegmentsRequest",
        "BatchUpdateTrafficForecastSegmentsResponse",
    },
)


class GetTrafficForecastSegmentRequest(proto.Message):
    r"""Request object for ``GetTrafficForecastSegment`` method.

    Attributes:
        name (str):
            Required. The resource name of the TrafficForecastSegment.
            Format:
            ``networks/{network_code}/trafficForecastSegments/{trafficForecastSegmentId}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListTrafficForecastSegmentsRequest(proto.Message):
    r"""Request object for ``ListTrafficForecastSegments`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            TrafficForecastSegments. Format: ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of ``TrafficForecastSegments``
            to return. The service may return fewer than this value. If
            unspecified, at most 50 ``TrafficForecastSegments`` will be
            returned. The maximum value is 1000; values greater than
            1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListTrafficForecastSegments`` call. Provide this to
            retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListTrafficForecastSegments`` must match the call that
            provided the page token.
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

            - ``createTime``
            - ``displayName``
            - ``forecastAdjustmentCount``
            - ``name``
            - ``targetedAdUnits``
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


class ListTrafficForecastSegmentsResponse(proto.Message):
    r"""Response object for ``ListTrafficForecastSegmentsRequest``
    containing matching ``TrafficForecastSegment`` objects.

    Attributes:
        traffic_forecast_segments (MutableSequence[google.ads.admanager_v1.types.TrafficForecastSegment]):
            The ``TrafficForecastSegment`` objects from the specified
            network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of ``TrafficForecastSegment`` objects. If a
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

    traffic_forecast_segments: MutableSequence[
        traffic_forecast_segment_messages.TrafficForecastSegment
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=traffic_forecast_segment_messages.TrafficForecastSegment,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CreateTrafficForecastSegmentRequest(proto.Message):
    r"""Request object for ``CreateTrafficForecastSegment`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this
            ``TrafficForecastSegment`` will be created. Format:
            ``networks/{network_code}``
        traffic_forecast_segment (google.ads.admanager_v1.types.TrafficForecastSegment):
            Required. The ``TrafficForecastSegment`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    traffic_forecast_segment: traffic_forecast_segment_messages.TrafficForecastSegment = proto.Field(
        proto.MESSAGE,
        number=2,
        message=traffic_forecast_segment_messages.TrafficForecastSegment,
    )


class BatchCreateTrafficForecastSegmentsRequest(proto.Message):
    r"""Request object for ``BatchCreateTrafficForecastSegments`` method.

    Attributes:
        parent (str):
            Required. The parent resource where
            ``TrafficForecastSegments`` will be created. Format:
            ``networks/{network_code}`` The parent field in the
            CreateTrafficForecastSegmentRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.CreateTrafficForecastSegmentRequest]):
            Required. The ``TrafficForecastSegment`` objects to create.
            A maximum of 100 objects can be created in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateTrafficForecastSegmentRequest"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="CreateTrafficForecastSegmentRequest",
        )
    )


class BatchCreateTrafficForecastSegmentsResponse(proto.Message):
    r"""Response object for ``BatchCreateTrafficForecastSegments`` method.

    Attributes:
        traffic_forecast_segments (MutableSequence[google.ads.admanager_v1.types.TrafficForecastSegment]):
            The ``TrafficForecastSegment`` objects created.
    """

    traffic_forecast_segments: MutableSequence[
        traffic_forecast_segment_messages.TrafficForecastSegment
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=traffic_forecast_segment_messages.TrafficForecastSegment,
    )


class UpdateTrafficForecastSegmentRequest(proto.Message):
    r"""Request object for ``UpdateTrafficForecastSegment`` method.

    Attributes:
        traffic_forecast_segment (google.ads.admanager_v1.types.TrafficForecastSegment):
            Required. The ``TrafficForecastSegment`` to update.

            The ``TrafficForecastSegment``'s ``name`` is used to
            identify the ``TrafficForecastSegment`` to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    traffic_forecast_segment: traffic_forecast_segment_messages.TrafficForecastSegment = proto.Field(
        proto.MESSAGE,
        number=1,
        message=traffic_forecast_segment_messages.TrafficForecastSegment,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateTrafficForecastSegmentsRequest(proto.Message):
    r"""Request object for ``BatchUpdateTrafficForecastSegments`` method.

    Attributes:
        parent (str):
            Required. The parent resource where
            ``TrafficForecastSegments`` will be updated. Format:
            ``networks/{network_code}`` The parent field in the
            UpdateTrafficForecastSegmentRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.UpdateTrafficForecastSegmentRequest]):
            Required. The ``TrafficForecastSegment`` objects to update.
            A maximum of 100 objects can be updated in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateTrafficForecastSegmentRequest"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="UpdateTrafficForecastSegmentRequest",
        )
    )


class BatchUpdateTrafficForecastSegmentsResponse(proto.Message):
    r"""Response object for ``BatchUpdateTrafficForecastSegments`` method.

    Attributes:
        traffic_forecast_segments (MutableSequence[google.ads.admanager_v1.types.TrafficForecastSegment]):
            The ``TrafficForecastSegment`` objects updated.
    """

    traffic_forecast_segments: MutableSequence[
        traffic_forecast_segment_messages.TrafficForecastSegment
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=traffic_forecast_segment_messages.TrafficForecastSegment,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
