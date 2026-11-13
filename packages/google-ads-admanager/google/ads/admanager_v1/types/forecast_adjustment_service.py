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

from google.ads.admanager_v1.types import forecast_adjustment_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetForecastAdjustmentRequest",
        "ListForecastAdjustmentsRequest",
        "ListForecastAdjustmentsResponse",
        "CreateForecastAdjustmentRequest",
        "BatchCreateForecastAdjustmentsRequest",
        "BatchCreateForecastAdjustmentsResponse",
        "UpdateForecastAdjustmentRequest",
        "BatchUpdateForecastAdjustmentsRequest",
        "BatchUpdateForecastAdjustmentsResponse",
        "BatchActivateForecastAdjustmentsRequest",
        "BatchActivateForecastAdjustmentsResponse",
        "BatchDeactivateForecastAdjustmentsRequest",
        "BatchDeactivateForecastAdjustmentsResponse",
        "CalculateDailyAdOpportunityCountsRequest",
        "CalculateDailyAdOpportunityCountsResponse",
    },
)


class GetForecastAdjustmentRequest(proto.Message):
    r"""Request object for ``GetForecastAdjustment`` method.

    Attributes:
        name (str):
            Required. The resource name of the ForecastAdjustment.
            Format:
            ``networks/{network_code}/forecastAdjustments/{forecastAdjustmentId}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListForecastAdjustmentsRequest(proto.Message):
    r"""Request object for ``ListForecastAdjustments`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            ForecastAdjustments. Format: ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of ``ForecastAdjustments`` to
            return. The service may return fewer than this value. If
            unspecified, at most 50 ``ForecastAdjustments`` will be
            returned. The maximum value is 1000; values above 1000 will
            be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListForecastAdjustments`` call. Provide this to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``ListForecastAdjustments`` must match the call that
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

            - ``dateRange.endDate``
            - ``dateRange.startDate``
            - ``displayName``
            - ``name``
            - ``status``
            - ``trafficForecastSegment``
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


class ListForecastAdjustmentsResponse(proto.Message):
    r"""Response object for ``ListForecastAdjustmentsRequest`` containing
    matching ``ForecastAdjustment`` objects.

    Attributes:
        forecast_adjustments (MutableSequence[google.ads.admanager_v1.types.ForecastAdjustment]):
            The ``ForecastAdjustment`` objects from the specified
            network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of ``ForecastAdjustment`` objects. If a filter
            was included in the request, this reflects the total number
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

    forecast_adjustments: MutableSequence[
        forecast_adjustment_messages.ForecastAdjustment
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=forecast_adjustment_messages.ForecastAdjustment,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CreateForecastAdjustmentRequest(proto.Message):
    r"""Request object for ``CreateForecastAdjustment`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this
            ``ForecastAdjustment`` will be created. Format:
            ``networks/{network_code}``
        forecast_adjustment (google.ads.admanager_v1.types.ForecastAdjustment):
            Required. The ``ForecastAdjustment`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    forecast_adjustment: forecast_adjustment_messages.ForecastAdjustment = proto.Field(
        proto.MESSAGE,
        number=2,
        message=forecast_adjustment_messages.ForecastAdjustment,
    )


class BatchCreateForecastAdjustmentsRequest(proto.Message):
    r"""Request object for ``BatchCreateForecastAdjustments`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``ForecastAdjustments``
            will be created. Format: ``networks/{network_code}`` The
            parent field in the CreateForecastAdjustmentRequest must
            match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.CreateForecastAdjustmentRequest]):
            Required. The ``ForecastAdjustment`` objects to create. A
            maximum of 100 objects can be created in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateForecastAdjustmentRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateForecastAdjustmentRequest",
    )


class BatchCreateForecastAdjustmentsResponse(proto.Message):
    r"""Response object for ``BatchCreateForecastAdjustments`` method.

    Attributes:
        forecast_adjustments (MutableSequence[google.ads.admanager_v1.types.ForecastAdjustment]):
            The ``ForecastAdjustment`` objects created.
    """

    forecast_adjustments: MutableSequence[
        forecast_adjustment_messages.ForecastAdjustment
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=forecast_adjustment_messages.ForecastAdjustment,
    )


class UpdateForecastAdjustmentRequest(proto.Message):
    r"""Request object for ``UpdateForecastAdjustment`` method.

    Attributes:
        forecast_adjustment (google.ads.admanager_v1.types.ForecastAdjustment):
            Required. The ``ForecastAdjustment`` to update.

            The ``ForecastAdjustment``'s ``name`` is used to identify
            the ``ForecastAdjustment`` to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    forecast_adjustment: forecast_adjustment_messages.ForecastAdjustment = proto.Field(
        proto.MESSAGE,
        number=1,
        message=forecast_adjustment_messages.ForecastAdjustment,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateForecastAdjustmentsRequest(proto.Message):
    r"""Request object for ``BatchUpdateForecastAdjustments`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``ForecastAdjustments``
            will be updated. Format: ``networks/{network_code}`` The
            parent field in the UpdateForecastAdjustmentRequest must
            match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.UpdateForecastAdjustmentRequest]):
            Required. The ``ForecastAdjustment`` objects to update. A
            maximum of 100 objects can be updated in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateForecastAdjustmentRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdateForecastAdjustmentRequest",
    )


class BatchUpdateForecastAdjustmentsResponse(proto.Message):
    r"""Response object for ``BatchUpdateForecastAdjustments`` method.

    Attributes:
        forecast_adjustments (MutableSequence[google.ads.admanager_v1.types.ForecastAdjustment]):
            The ``ForecastAdjustment`` objects updated.
    """

    forecast_adjustments: MutableSequence[
        forecast_adjustment_messages.ForecastAdjustment
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=forecast_adjustment_messages.ForecastAdjustment,
    )


class BatchActivateForecastAdjustmentsRequest(proto.Message):
    r"""Request message for ``BatchActivateForecastAdjustments`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the ``ForecastAdjustment``
            objects to activate.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchActivateForecastAdjustmentsResponse(proto.Message):
    r"""Response object for ``BatchActivateForecastAdjustments`` method."""


class BatchDeactivateForecastAdjustmentsRequest(proto.Message):
    r"""Request message for ``BatchDeactivateForecastAdjustments`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the ``ForecastAdjustment``
            objects to deactivate.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchDeactivateForecastAdjustmentsResponse(proto.Message):
    r"""Response object for ``BatchDeactivateForecastAdjustments`` method."""


class CalculateDailyAdOpportunityCountsRequest(proto.Message):
    r"""Request message for ``CalculateDailyAdOpportunityCounts`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this
            ``ForecastAdjustment`` will be calculated. Format:
            ``networks/{network_code}``
        forecast_adjustment (google.ads.admanager_v1.types.ForecastAdjustment):
            Required. The prospective ``ForecastAdjustment`` to
            calculate daily ad opportunity counts for.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    forecast_adjustment: forecast_adjustment_messages.ForecastAdjustment = proto.Field(
        proto.MESSAGE,
        number=2,
        message=forecast_adjustment_messages.ForecastAdjustment,
    )


class CalculateDailyAdOpportunityCountsResponse(proto.Message):
    r"""Response message for ``CalculateDailyAdOpportunityCounts`` method.

    Attributes:
        forecast_adjustment (google.ads.admanager_v1.types.ForecastAdjustment):
            The ``ForecastAdjustment`` with its
            ``calculated_daily_ad_opportunity_counts`` populated.
    """

    forecast_adjustment: forecast_adjustment_messages.ForecastAdjustment = proto.Field(
        proto.MESSAGE,
        number=1,
        message=forecast_adjustment_messages.ForecastAdjustment,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
