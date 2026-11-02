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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.analytics.data_v1beta.types import data

__protobuf__ = proto.module(
    package="google.analytics.data.v1beta",
    manifest={
        "CheckCompatibilityRequest",
        "CheckCompatibilityResponse",
        "Metadata",
        "RunReportRequest",
        "RunReportResponse",
        "RunPivotReportRequest",
        "RunPivotReportResponse",
        "BatchRunReportsRequest",
        "BatchRunReportsResponse",
        "BatchRunPivotReportsRequest",
        "BatchRunPivotReportsResponse",
        "GetMetadataRequest",
        "RunRealtimeReportRequest",
        "RunRealtimeReportResponse",
        "GetAudienceExportRequest",
        "ListAudienceExportsRequest",
        "ListAudienceExportsResponse",
        "CreateAudienceExportRequest",
        "AudienceExport",
        "AudienceExportMetadata",
        "QueryAudienceExportRequest",
        "QueryAudienceExportResponse",
        "AudienceRow",
        "AudienceDimension",
        "AudienceDimensionValue",
    },
)


class CheckCompatibilityRequest(proto.Message):
    r"""The request for compatibility information for a report's dimensions
    and metrics. Check compatibility provides a preview of the
    compatibility of a report; fields shared with the ``runReport``
    request should be the same values as in your ``runReport`` request.

    Attributes:
        property (str):
            A Google Analytics property identifier whose events are
            tracked. To learn more, see `where to find your Property
            ID <https://developers.google.com/analytics/devguides/reporting/data/v1/property-id>`__.
            ``property`` should be the same value as in your
            ``runReport`` request.

            Example: properties/1234
        dimensions (MutableSequence[google.analytics.data_v1beta.types.Dimension]):
            The dimensions in this report. ``dimensions`` should be the
            same value as in your ``runReport`` request.
        metrics (MutableSequence[google.analytics.data_v1beta.types.Metric]):
            The metrics in this report. ``metrics`` should be the same
            value as in your ``runReport`` request.
        dimension_filter (google.analytics.data_v1beta.types.FilterExpression):
            The filter clause of dimensions. ``dimensionFilter`` should
            be the same value as in your ``runReport`` request.
        metric_filter (google.analytics.data_v1beta.types.FilterExpression):
            The filter clause of metrics. ``metricFilter`` should be the
            same value as in your ``runReport`` request
        compatibility_filter (google.analytics.data_v1beta.types.Compatibility):
            Filters the dimensions and metrics in the response to just
            this compatibility. Commonly used as
            ``”compatibilityFilter”: “COMPATIBLE”`` to only return
            compatible dimensions & metrics.
    """

    property: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dimensions: MutableSequence[data.Dimension] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=data.Dimension,
    )
    metrics: MutableSequence[data.Metric] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=data.Metric,
    )
    dimension_filter: data.FilterExpression = proto.Field(
        proto.MESSAGE,
        number=4,
        message=data.FilterExpression,
    )
    metric_filter: data.FilterExpression = proto.Field(
        proto.MESSAGE,
        number=5,
        message=data.FilterExpression,
    )
    compatibility_filter: data.Compatibility = proto.Field(
        proto.ENUM,
        number=6,
        enum=data.Compatibility,
    )


class CheckCompatibilityResponse(proto.Message):
    r"""The compatibility response with the compatibility of each
    dimension & metric.

    Attributes:
        dimension_compatibilities (MutableSequence[google.analytics.data_v1beta.types.DimensionCompatibility]):
            The compatibility of each dimension.
        metric_compatibilities (MutableSequence[google.analytics.data_v1beta.types.MetricCompatibility]):
            The compatibility of each metric.
    """

    dimension_compatibilities: MutableSequence[data.DimensionCompatibility] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=data.DimensionCompatibility,
        )
    )
    metric_compatibilities: MutableSequence[data.MetricCompatibility] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message=data.MetricCompatibility,
        )
    )


class Metadata(proto.Message):
    r"""The dimensions, metrics and comparisons currently accepted in
    reporting methods.

    Attributes:
        name (str):
            Resource name of this metadata.
        dimensions (MutableSequence[google.analytics.data_v1beta.types.DimensionMetadata]):
            The dimension descriptions.
        metrics (MutableSequence[google.analytics.data_v1beta.types.MetricMetadata]):
            The metric descriptions.
        comparisons (MutableSequence[google.analytics.data_v1beta.types.ComparisonMetadata]):
            The comparison descriptions.
    """

    name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    dimensions: MutableSequence[data.DimensionMetadata] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=data.DimensionMetadata,
    )
    metrics: MutableSequence[data.MetricMetadata] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=data.MetricMetadata,
    )
    comparisons: MutableSequence[data.ComparisonMetadata] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=data.ComparisonMetadata,
    )


class RunReportRequest(proto.Message):
    r"""The request to generate a report.

    Attributes:
        property (str):
            A Google Analytics property identifier whose events are
            tracked. Specified in the URL path and not the body. To
            learn more, see `where to find your Property
            ID <https://developers.google.com/analytics/devguides/reporting/data/v1/property-id>`__.
            Within a batch request, this property should either be
            unspecified or consistent with the batch-level property.

            Example: properties/1234
        dimensions (MutableSequence[google.analytics.data_v1beta.types.Dimension]):
            The dimensions requested and displayed.
        metrics (MutableSequence[google.analytics.data_v1beta.types.Metric]):
            The metrics requested and displayed.
        date_ranges (MutableSequence[google.analytics.data_v1beta.types.DateRange]):
            Date ranges of data to read. If multiple date ranges are
            requested, each response row will contain a zero based date
            range index. If two date ranges overlap, the event data for
            the overlapping days is included in the response rows for
            both date ranges. In a cohort request, this ``dateRanges``
            must be unspecified.
        dimension_filter (google.analytics.data_v1beta.types.FilterExpression):
            Dimension filters let you ask for only specific dimension
            values in the report. To learn more, see `Fundamentals of
            Dimension
            Filters <https://developers.google.com/analytics/devguides/reporting/data/v1/basics#dimension_filters>`__
            for examples. Metrics cannot be used in this filter.
        metric_filter (google.analytics.data_v1beta.types.FilterExpression):
            The filter clause of metrics. Applied after
            aggregating the report's rows, similar to SQL
            having-clause. Dimensions cannot be used in this
            filter.
        offset (int):
            The row count of the start row. The first row is counted as
            row 0.

            When paging, the first request does not specify offset; or
            equivalently, sets offset to 0; the first request returns
            the first ``limit`` of rows. The second request sets offset
            to the ``limit`` of the first request; the second request
            returns the second ``limit`` of rows.

            To learn more about this pagination parameter, see
            `Pagination <https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination>`__.
        limit (int):
            The number of rows to return. If unspecified, 10,000 rows
            are returned. The API returns a maximum of 250,000 rows per
            request, no matter how many you ask for. ``limit`` must be
            positive.

            The API can also return fewer rows than the requested
            ``limit``, if there aren't as many dimension values as the
            ``limit``. For instance, there are fewer than 300 possible
            values for the dimension ``country``, so when reporting on
            only ``country``, you can't get more than 300 rows, even if
            you set ``limit`` to a higher value.

            To learn more about this pagination parameter, see
            `Pagination <https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination>`__.
        metric_aggregations (MutableSequence[google.analytics.data_v1beta.types.MetricAggregation]):
            Aggregation of metrics. Aggregated metric values will be
            shown in rows where the dimension_values are set to
            "RESERVED\_(MetricAggregation)". Aggregates including both
            comparisons and multiple date ranges will be aggregated
            based on the date ranges.
        order_bys (MutableSequence[google.analytics.data_v1beta.types.OrderBy]):
            Specifies how rows are ordered in the
            response. Requests including both comparisons
            and multiple date ranges will have order bys
            applied on the comparisons.
        currency_code (str):
            A currency code in ISO4217 format, such as
            "AED", "USD", "JPY". If the field is empty, the
            report uses the property's default currency.
        cohort_spec (google.analytics.data_v1beta.types.CohortSpec):
            Cohort group associated with this request. If
            there is a cohort group in the request the
            'cohort' dimension must be present.
        keep_empty_rows (bool):
            If false or unspecified, each row with all metrics equal to
            0 will not be returned. If true, these rows will be returned
            if they are not separately removed by a filter.

            Regardless of this ``keep_empty_rows`` setting, only data
            recorded by the Google Analytics property can be displayed
            in a report.

            For example if a property never logs a ``purchase`` event,
            then a query for the ``eventName`` dimension and
            ``eventCount`` metric will not have a row eventName:
            "purchase" and eventCount: 0.
        return_property_quota (bool):
            Toggles whether to return the current state of this Google
            Analytics property's quota. Quota is returned in
            `PropertyQuota <#PropertyQuota>`__.
        comparisons (MutableSequence[google.analytics.data_v1beta.types.Comparison]):
            Optional. The configuration of comparisons
            requested and displayed. The request only
            requires a comparisons field in order to receive
            a comparison column in the response.
    """

    property: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dimensions: MutableSequence[data.Dimension] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=data.Dimension,
    )
    metrics: MutableSequence[data.Metric] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=data.Metric,
    )
    date_ranges: MutableSequence[data.DateRange] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=data.DateRange,
    )
    dimension_filter: data.FilterExpression = proto.Field(
        proto.MESSAGE,
        number=5,
        message=data.FilterExpression,
    )
    metric_filter: data.FilterExpression = proto.Field(
        proto.MESSAGE,
        number=6,
        message=data.FilterExpression,
    )
    offset: int = proto.Field(
        proto.INT64,
        number=7,
    )
    limit: int = proto.Field(
        proto.INT64,
        number=8,
    )
    metric_aggregations: MutableSequence[data.MetricAggregation] = proto.RepeatedField(
        proto.ENUM,
        number=9,
        enum=data.MetricAggregation,
    )
    order_bys: MutableSequence[data.OrderBy] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message=data.OrderBy,
    )
    currency_code: str = proto.Field(
        proto.STRING,
        number=11,
    )
    cohort_spec: data.CohortSpec = proto.Field(
        proto.MESSAGE,
        number=12,
        message=data.CohortSpec,
    )
    keep_empty_rows: bool = proto.Field(
        proto.BOOL,
        number=13,
    )
    return_property_quota: bool = proto.Field(
        proto.BOOL,
        number=14,
    )
    comparisons: MutableSequence[data.Comparison] = proto.RepeatedField(
        proto.MESSAGE,
        number=15,
        message=data.Comparison,
    )


class RunReportResponse(proto.Message):
    r"""The response report table corresponding to a request.

    Attributes:
        dimension_headers (MutableSequence[google.analytics.data_v1beta.types.DimensionHeader]):
            Describes dimension columns. The number of
            DimensionHeaders and ordering of
            DimensionHeaders matches the dimensions present
            in rows.
        metric_headers (MutableSequence[google.analytics.data_v1beta.types.MetricHeader]):
            Describes metric columns. The number of
            MetricHeaders and ordering of MetricHeaders
            matches the metrics present in rows.
        rows (MutableSequence[google.analytics.data_v1beta.types.Row]):
            Rows of dimension value combinations and
            metric values in the report.
        totals (MutableSequence[google.analytics.data_v1beta.types.Row]):
            If requested, the totaled values of metrics.
        maximums (MutableSequence[google.analytics.data_v1beta.types.Row]):
            If requested, the maximum values of metrics.
        minimums (MutableSequence[google.analytics.data_v1beta.types.Row]):
            If requested, the minimum values of metrics.
        row_count (int):
            The total number of rows in the query result. ``rowCount``
            is independent of the number of rows returned in the
            response, the ``limit`` request parameter, and the
            ``offset`` request parameter. For example if a query returns
            175 rows and includes ``limit`` of 50 in the API request,
            the response will contain ``rowCount`` of 175 but only 50
            rows.

            To learn more about this pagination parameter, see
            `Pagination <https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination>`__.
        metadata (google.analytics.data_v1beta.types.ResponseMetaData):
            Metadata for the report.
        property_quota (google.analytics.data_v1beta.types.PropertyQuota):
            This Google Analytics property's quota state
            including this request.
        kind (str):
            Identifies what kind of resource this message is. This
            ``kind`` is always the fixed string
            "analyticsData#runReport". Useful to distinguish between
            response types in JSON.
    """

    dimension_headers: MutableSequence[data.DimensionHeader] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=data.DimensionHeader,
    )
    metric_headers: MutableSequence[data.MetricHeader] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=data.MetricHeader,
    )
    rows: MutableSequence[data.Row] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=data.Row,
    )
    totals: MutableSequence[data.Row] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=data.Row,
    )
    maximums: MutableSequence[data.Row] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=data.Row,
    )
    minimums: MutableSequence[data.Row] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=data.Row,
    )
    row_count: int = proto.Field(
        proto.INT32,
        number=7,
    )
    metadata: data.ResponseMetaData = proto.Field(
        proto.MESSAGE,
        number=8,
        message=data.ResponseMetaData,
    )
    property_quota: data.PropertyQuota = proto.Field(
        proto.MESSAGE,
        number=9,
        message=data.PropertyQuota,
    )
    kind: str = proto.Field(
        proto.STRING,
        number=10,
    )


class RunPivotReportRequest(proto.Message):
    r"""The request to generate a pivot report.

    Attributes:
        property (str):
            A Google Analytics property identifier whose events are
            tracked. Specified in the URL path and not the body. To
            learn more, see `where to find your Property
            ID <https://developers.google.com/analytics/devguides/reporting/data/v1/property-id>`__.
            Within a batch request, this property should either be
            unspecified or consistent with the batch-level property.

            Example: properties/1234
        dimensions (MutableSequence[google.analytics.data_v1beta.types.Dimension]):
            The dimensions requested. All defined dimensions must be
            used by one of the following: dimension_expression,
            dimension_filter, pivots, order_bys.
        metrics (MutableSequence[google.analytics.data_v1beta.types.Metric]):
            The metrics requested, at least one metric needs to be
            specified. All defined metrics must be used by one of the
            following: metric_expression, metric_filter, order_bys.
        date_ranges (MutableSequence[google.analytics.data_v1beta.types.DateRange]):
            The date range to retrieve event data for the report. If
            multiple date ranges are specified, event data from each
            date range is used in the report. A special dimension with
            field name "dateRange" can be included in a Pivot's field
            names; if included, the report compares between date ranges.
            In a cohort request, this ``dateRanges`` must be
            unspecified.
        pivots (MutableSequence[google.analytics.data_v1beta.types.Pivot]):
            Describes the visual format of the report's
            dimensions in columns or rows. The union of the
            fieldNames (dimension names) in all pivots must
            be a subset of dimension names defined in
            Dimensions. No two pivots can share a dimension.
            A dimension is only visible if it appears in a
            pivot.
        dimension_filter (google.analytics.data_v1beta.types.FilterExpression):
            The filter clause of dimensions. Dimensions
            must be requested to be used in this filter.
            Metrics cannot be used in this filter.
        metric_filter (google.analytics.data_v1beta.types.FilterExpression):
            The filter clause of metrics. Applied at post
            aggregation phase, similar to SQL having-clause.
            Metrics must be requested to be used in this
            filter. Dimensions cannot be used in this
            filter.
        currency_code (str):
            A currency code in ISO4217 format, such as
            "AED", "USD", "JPY". If the field is empty, the
            report uses the property's default currency.
        cohort_spec (google.analytics.data_v1beta.types.CohortSpec):
            Cohort group associated with this request. If
            there is a cohort group in the request the
            'cohort' dimension must be present.
        keep_empty_rows (bool):
            If false or unspecified, each row with all metrics equal to
            0 will not be returned. If true, these rows will be returned
            if they are not separately removed by a filter.

            Regardless of this ``keep_empty_rows`` setting, only data
            recorded by the Google Analytics property can be displayed
            in a report.

            For example if a property never logs a ``purchase`` event,
            then a query for the ``eventName`` dimension and
            ``eventCount`` metric will not have a row eventName:
            "purchase" and eventCount: 0.
        return_property_quota (bool):
            Toggles whether to return the current state of this Google
            Analytics property's quota. Quota is returned in
            `PropertyQuota <#PropertyQuota>`__.
        comparisons (MutableSequence[google.analytics.data_v1beta.types.Comparison]):
            Optional. The configuration of comparisons
            requested and displayed. The request requires
            both a comparisons field and a comparisons
            dimension to receive a comparison column in the
            response.
    """

    property: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dimensions: MutableSequence[data.Dimension] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=data.Dimension,
    )
    metrics: MutableSequence[data.Metric] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=data.Metric,
    )
    date_ranges: MutableSequence[data.DateRange] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=data.DateRange,
    )
    pivots: MutableSequence[data.Pivot] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=data.Pivot,
    )
    dimension_filter: data.FilterExpression = proto.Field(
        proto.MESSAGE,
        number=6,
        message=data.FilterExpression,
    )
    metric_filter: data.FilterExpression = proto.Field(
        proto.MESSAGE,
        number=7,
        message=data.FilterExpression,
    )
    currency_code: str = proto.Field(
        proto.STRING,
        number=8,
    )
    cohort_spec: data.CohortSpec = proto.Field(
        proto.MESSAGE,
        number=9,
        message=data.CohortSpec,
    )
    keep_empty_rows: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    return_property_quota: bool = proto.Field(
        proto.BOOL,
        number=11,
    )
    comparisons: MutableSequence[data.Comparison] = proto.RepeatedField(
        proto.MESSAGE,
        number=12,
        message=data.Comparison,
    )


class RunPivotReportResponse(proto.Message):
    r"""The response pivot report table corresponding to a pivot
    request.

    Attributes:
        pivot_headers (MutableSequence[google.analytics.data_v1beta.types.PivotHeader]):
            Summarizes the columns and rows created by a pivot. Each
            pivot in the request produces one header in the response. If
            we have a request like this:

            ::

                "pivots": [{
                  "fieldNames": ["country",
                    "city"]
                },
                {
                  "fieldNames": "eventName"
                }]

            We will have the following ``pivotHeaders`` in the response:

            ::

                "pivotHeaders" : [{
                  "dimensionHeaders": [{
                    "dimensionValues": [
                       { "value": "United Kingdom" },
                       { "value": "London" }
                     ]
                  },
                  {
                    "dimensionValues": [
                    { "value": "Japan" },
                    { "value": "Osaka" }
                    ]
                  }]
                },
                {
                  "dimensionHeaders": [{
                    "dimensionValues": [{ "value": "session_start" }]
                  },
                  {
                    "dimensionValues": [{ "value": "scroll" }]
                  }]
                }]
        dimension_headers (MutableSequence[google.analytics.data_v1beta.types.DimensionHeader]):
            Describes dimension columns. The number of
            DimensionHeaders and ordering of
            DimensionHeaders matches the dimensions present
            in rows.
        metric_headers (MutableSequence[google.analytics.data_v1beta.types.MetricHeader]):
            Describes metric columns. The number of
            MetricHeaders and ordering of MetricHeaders
            matches the metrics present in rows.
        rows (MutableSequence[google.analytics.data_v1beta.types.Row]):
            Rows of dimension value combinations and
            metric values in the report.
        aggregates (MutableSequence[google.analytics.data_v1beta.types.Row]):
            Aggregation of metric values. Can be totals, minimums, or
            maximums. The returned aggregations are controlled by the
            metric_aggregations in the pivot. The type of aggregation
            returned in each row is shown by the dimension_values which
            are set to "RESERVED\_".
        metadata (google.analytics.data_v1beta.types.ResponseMetaData):
            Metadata for the report.
        property_quota (google.analytics.data_v1beta.types.PropertyQuota):
            This Google Analytics property's quota state
            including this request.
        kind (str):
            Identifies what kind of resource this message is. This
            ``kind`` is always the fixed string
            "analyticsData#runPivotReport". Useful to distinguish
            between response types in JSON.
    """

    pivot_headers: MutableSequence[data.PivotHeader] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=data.PivotHeader,
    )
    dimension_headers: MutableSequence[data.DimensionHeader] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=data.DimensionHeader,
    )
    metric_headers: MutableSequence[data.MetricHeader] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=data.MetricHeader,
    )
    rows: MutableSequence[data.Row] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=data.Row,
    )
    aggregates: MutableSequence[data.Row] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=data.Row,
    )
    metadata: data.ResponseMetaData = proto.Field(
        proto.MESSAGE,
        number=6,
        message=data.ResponseMetaData,
    )
    property_quota: data.PropertyQuota = proto.Field(
        proto.MESSAGE,
        number=7,
        message=data.PropertyQuota,
    )
    kind: str = proto.Field(
        proto.STRING,
        number=8,
    )


class BatchRunReportsRequest(proto.Message):
    r"""The batch request containing multiple report requests.

    Attributes:
        property (str):
            A Google Analytics property identifier whose events are
            tracked. Specified in the URL path and not the body. To
            learn more, see `where to find your Property
            ID <https://developers.google.com/analytics/devguides/reporting/data/v1/property-id>`__.
            This property must be specified for the batch. The property
            within RunReportRequest may either be unspecified or
            consistent with this property.

            Example: properties/1234
        requests (MutableSequence[google.analytics.data_v1beta.types.RunReportRequest]):
            Individual requests. Each request has a
            separate report response. Each batch request is
            allowed up to 5 requests.
    """

    property: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["RunReportRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="RunReportRequest",
    )


class BatchRunReportsResponse(proto.Message):
    r"""The batch response containing multiple reports.

    Attributes:
        reports (MutableSequence[google.analytics.data_v1beta.types.RunReportResponse]):
            Individual responses. Each response has a
            separate report request.
        kind (str):
            Identifies what kind of resource this message is. This
            ``kind`` is always the fixed string
            "analyticsData#batchRunReports". Useful to distinguish
            between response types in JSON.
    """

    reports: MutableSequence["RunReportResponse"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="RunReportResponse",
    )
    kind: str = proto.Field(
        proto.STRING,
        number=2,
    )


class BatchRunPivotReportsRequest(proto.Message):
    r"""The batch request containing multiple pivot report requests.

    Attributes:
        property (str):
            A Google Analytics property identifier whose events are
            tracked. Specified in the URL path and not the body. To
            learn more, see `where to find your Property
            ID <https://developers.google.com/analytics/devguides/reporting/data/v1/property-id>`__.
            This property must be specified for the batch. The property
            within RunPivotReportRequest may either be unspecified or
            consistent with this property.

            Example: properties/1234
        requests (MutableSequence[google.analytics.data_v1beta.types.RunPivotReportRequest]):
            Individual requests. Each request has a
            separate pivot report response. Each batch
            request is allowed up to 5 requests.
    """

    property: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["RunPivotReportRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="RunPivotReportRequest",
    )


class BatchRunPivotReportsResponse(proto.Message):
    r"""The batch response containing multiple pivot reports.

    Attributes:
        pivot_reports (MutableSequence[google.analytics.data_v1beta.types.RunPivotReportResponse]):
            Individual responses. Each response has a
            separate pivot report request.
        kind (str):
            Identifies what kind of resource this message is. This
            ``kind`` is always the fixed string
            "analyticsData#batchRunPivotReports". Useful to distinguish
            between response types in JSON.
    """

    pivot_reports: MutableSequence["RunPivotReportResponse"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="RunPivotReportResponse",
    )
    kind: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetMetadataRequest(proto.Message):
    r"""Request for a property's dimension and metric metadata.

    Attributes:
        name (str):
            Required. The resource name of the metadata to retrieve.
            This name field is specified in the URL path and not URL
            parameters. Property is a numeric Google Analytics property
            identifier. To learn more, see `where to find your Property
            ID <https://developers.google.com/analytics/devguides/reporting/data/v1/property-id>`__.

            Example: properties/1234/metadata

            Set the Property ID to 0 for dimensions and metrics common
            to all properties. In this special mode, this method will
            not return custom dimensions and metrics.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RunRealtimeReportRequest(proto.Message):
    r"""The request to generate a realtime report.

    Attributes:
        property (str):
            A Google Analytics property identifier whose events are
            tracked. Specified in the URL path and not the body. To
            learn more, see `where to find your Property
            ID <https://developers.google.com/analytics/devguides/reporting/data/v1/property-id>`__.

            Example: properties/1234
        dimensions (MutableSequence[google.analytics.data_v1beta.types.Dimension]):
            The dimensions requested and displayed.
        metrics (MutableSequence[google.analytics.data_v1beta.types.Metric]):
            The metrics requested and displayed.
        dimension_filter (google.analytics.data_v1beta.types.FilterExpression):
            The filter clause of dimensions. Metrics
            cannot be used in this filter.
        metric_filter (google.analytics.data_v1beta.types.FilterExpression):
            The filter clause of metrics. Applied at post
            aggregation phase, similar to SQL having-clause.
            Dimensions cannot be used in this filter.
        limit (int):
            The number of rows to return. If unspecified, 10,000 rows
            are returned. The API returns a maximum of 250,000 rows per
            request, no matter how many you ask for. ``limit`` must be
            positive.

            The API can also return fewer rows than the requested
            ``limit``, if there aren't as many dimension values as the
            ``limit``. For instance, there are fewer than 300 possible
            values for the dimension ``country``, so when reporting on
            only ``country``, you can't get more than 300 rows, even if
            you set ``limit`` to a higher value.
        metric_aggregations (MutableSequence[google.analytics.data_v1beta.types.MetricAggregation]):
            Aggregation of metrics. Aggregated metric values will be
            shown in rows where the dimension_values are set to
            "RESERVED\_(MetricAggregation)".
        order_bys (MutableSequence[google.analytics.data_v1beta.types.OrderBy]):
            Specifies how rows are ordered in the
            response.
        return_property_quota (bool):
            Toggles whether to return the current state of this Google
            Analytics property's Realtime quota. Quota is returned in
            `PropertyQuota <#PropertyQuota>`__.
        minute_ranges (MutableSequence[google.analytics.data_v1beta.types.MinuteRange]):
            The minute ranges of event data to read. If
            unspecified, one minute range for the last 30
            minutes will be used. If multiple minute ranges
            are requested, each response row will contain a
            zero based minute range index. If two minute
            ranges overlap, the event data for the
            overlapping minutes is included in the response
            rows for both minute ranges.
    """

    property: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dimensions: MutableSequence[data.Dimension] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=data.Dimension,
    )
    metrics: MutableSequence[data.Metric] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=data.Metric,
    )
    dimension_filter: data.FilterExpression = proto.Field(
        proto.MESSAGE,
        number=4,
        message=data.FilterExpression,
    )
    metric_filter: data.FilterExpression = proto.Field(
        proto.MESSAGE,
        number=5,
        message=data.FilterExpression,
    )
    limit: int = proto.Field(
        proto.INT64,
        number=6,
    )
    metric_aggregations: MutableSequence[data.MetricAggregation] = proto.RepeatedField(
        proto.ENUM,
        number=7,
        enum=data.MetricAggregation,
    )
    order_bys: MutableSequence[data.OrderBy] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message=data.OrderBy,
    )
    return_property_quota: bool = proto.Field(
        proto.BOOL,
        number=9,
    )
    minute_ranges: MutableSequence[data.MinuteRange] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message=data.MinuteRange,
    )


class RunRealtimeReportResponse(proto.Message):
    r"""The response realtime report table corresponding to a
    request.

    Attributes:
        dimension_headers (MutableSequence[google.analytics.data_v1beta.types.DimensionHeader]):
            Describes dimension columns. The number of
            DimensionHeaders and ordering of
            DimensionHeaders matches the dimensions present
            in rows.
        metric_headers (MutableSequence[google.analytics.data_v1beta.types.MetricHeader]):
            Describes metric columns. The number of
            MetricHeaders and ordering of MetricHeaders
            matches the metrics present in rows.
        rows (MutableSequence[google.analytics.data_v1beta.types.Row]):
            Rows of dimension value combinations and
            metric values in the report.
        totals (MutableSequence[google.analytics.data_v1beta.types.Row]):
            If requested, the totaled values of metrics.
        maximums (MutableSequence[google.analytics.data_v1beta.types.Row]):
            If requested, the maximum values of metrics.
        minimums (MutableSequence[google.analytics.data_v1beta.types.Row]):
            If requested, the minimum values of metrics.
        row_count (int):
            The total number of rows in the query result. ``rowCount``
            is independent of the number of rows returned in the
            response and the ``limit`` request parameter. For example if
            a query returns 175 rows and includes ``limit`` of 50 in the
            API request, the response will contain ``rowCount`` of 175
            but only 50 rows.
        property_quota (google.analytics.data_v1beta.types.PropertyQuota):
            This Google Analytics property's Realtime
            quota state including this request.
        kind (str):
            Identifies what kind of resource this message is. This
            ``kind`` is always the fixed string
            "analyticsData#runRealtimeReport". Useful to distinguish
            between response types in JSON.
    """

    dimension_headers: MutableSequence[data.DimensionHeader] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=data.DimensionHeader,
    )
    metric_headers: MutableSequence[data.MetricHeader] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=data.MetricHeader,
    )
    rows: MutableSequence[data.Row] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=data.Row,
    )
    totals: MutableSequence[data.Row] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=data.Row,
    )
    maximums: MutableSequence[data.Row] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message=data.Row,
    )
    minimums: MutableSequence[data.Row] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=data.Row,
    )
    row_count: int = proto.Field(
        proto.INT32,
        number=7,
    )
    property_quota: data.PropertyQuota = proto.Field(
        proto.MESSAGE,
        number=8,
        message=data.PropertyQuota,
    )
    kind: str = proto.Field(
        proto.STRING,
        number=9,
    )


class GetAudienceExportRequest(proto.Message):
    r"""A request to retrieve configuration metadata about a specific
    audience export.

    Attributes:
        name (str):
            Required. The audience export resource name. Format:
            ``properties/{property}/audienceExports/{audience_export}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListAudienceExportsRequest(proto.Message):
    r"""A request to list all audience exports for a property.

    Attributes:
        parent (str):
            Required. All audience exports for this property will be
            listed in the response. Format: ``properties/{property}``
        page_size (int):
            Optional. The maximum number of audience
            exports to return. The service may return fewer
            than this value. If unspecified, at most 200
            audience exports will be returned. The maximum
            value is 1000 (higher values will be coerced to
            the maximum).
        page_token (str):
            Optional. A page token, received from a previous
            ``ListAudienceExports`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListAudienceExports`` must match the call that provided
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


class ListAudienceExportsResponse(proto.Message):
    r"""A list of all audience exports for a property.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        audience_exports (MutableSequence[google.analytics.data_v1beta.types.AudienceExport]):
            Each audience export for a property.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.

            This field is a member of `oneof`_ ``_next_page_token``.
    """

    @property
    def raw_page(self):
        return self

    audience_exports: MutableSequence["AudienceExport"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AudienceExport",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )


class CreateAudienceExportRequest(proto.Message):
    r"""A request to create a new audience export.

    Attributes:
        parent (str):
            Required. The parent resource where this audience export
            will be created. Format: ``properties/{property}``
        audience_export (google.analytics.data_v1beta.types.AudienceExport):
            Required. The audience export to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    audience_export: "AudienceExport" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="AudienceExport",
    )


class AudienceExport(proto.Message):
    r"""An audience export is a list of users in an audience at the
    time of the list's creation. One audience may have multiple
    audience exports created for different days.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. Identifier. The audience export resource name
            assigned during creation. This resource name identifies this
            ``AudienceExport``.

            Format:
            ``properties/{property}/audienceExports/{audience_export}``
        audience (str):
            Required. The audience resource name. This resource name
            identifies the audience being listed and is shared between
            the Analytics Data & Admin APIs.

            Format: ``properties/{property}/audiences/{audience}``
        audience_display_name (str):
            Output only. The descriptive display name for
            this audience. For example, "Purchasers".
        dimensions (MutableSequence[google.analytics.data_v1beta.types.AudienceDimension]):
            Required. The dimensions requested and
            displayed in the query response.
        state (google.analytics.data_v1beta.types.AudienceExport.State):
            Output only. The current state for this
            AudienceExport.

            This field is a member of `oneof`_ ``_state``.
        begin_creating_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when CreateAudienceExport was called
            and the AudienceExport began the ``CREATING`` state.

            This field is a member of `oneof`_ ``_begin_creating_time``.
        creation_quota_tokens_charged (int):
            Output only. The total quota tokens charged during creation
            of the AudienceExport. Because this token count is based on
            activity from the ``CREATING`` state, this tokens charged
            will be fixed once an AudienceExport enters the ``ACTIVE``
            or ``FAILED`` states.
        row_count (int):
            Output only. The total number of rows in the
            AudienceExport result.

            This field is a member of `oneof`_ ``_row_count``.
        error_message (str):
            Output only. Error message is populated when
            an audience export fails during creation. A
            common reason for such a failure is quota
            exhaustion.

            This field is a member of `oneof`_ ``_error_message``.
        percentage_completed (float):
            Output only. The percentage completed for
            this audience export ranging between 0 to 100.

            This field is a member of `oneof`_ ``_percentage_completed``.
    """

    class State(proto.Enum):
        r"""The AudienceExport currently exists in this state.

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified state will never be used.
            CREATING (1):
                The AudienceExport is currently creating and
                will be available in the future. Creating occurs
                immediately after the CreateAudienceExport call.
            ACTIVE (2):
                The AudienceExport is fully created and ready
                for querying. An AudienceExport is updated to
                active asynchronously from a request; this
                occurs some time (for example 15 minutes) after
                the initial create call.
            FAILED (3):
                The AudienceExport failed to be created. It
                is possible that re-requesting this audience
                export will succeed.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        FAILED = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    audience: str = proto.Field(
        proto.STRING,
        number=2,
    )
    audience_display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    dimensions: MutableSequence["AudienceDimension"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="AudienceDimension",
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        optional=True,
        enum=State,
    )
    begin_creating_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    creation_quota_tokens_charged: int = proto.Field(
        proto.INT32,
        number=7,
    )
    row_count: int = proto.Field(
        proto.INT32,
        number=8,
        optional=True,
    )
    error_message: str = proto.Field(
        proto.STRING,
        number=9,
        optional=True,
    )
    percentage_completed: float = proto.Field(
        proto.DOUBLE,
        number=10,
        optional=True,
    )


class AudienceExportMetadata(proto.Message):
    r"""This metadata is currently blank."""


class QueryAudienceExportRequest(proto.Message):
    r"""A request to list users in an audience export.

    Attributes:
        name (str):
            Required. The name of the audience export to retrieve users
            from. Format:
            ``properties/{property}/audienceExports/{audience_export}``
        offset (int):
            Optional. The row count of the start row. The first row is
            counted as row 0.

            When paging, the first request does not specify offset; or
            equivalently, sets offset to 0; the first request returns
            the first ``limit`` of rows. The second request sets offset
            to the ``limit`` of the first request; the second request
            returns the second ``limit`` of rows.

            To learn more about this pagination parameter, see
            `Pagination <https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination>`__.
        limit (int):
            Optional. The number of rows to return. If unspecified,
            10,000 rows are returned. The API returns a maximum of
            250,000 rows per request, no matter how many you ask for.
            ``limit`` must be positive.

            The API can also return fewer rows than the requested
            ``limit``, if there aren't as many dimension values as the
            ``limit``.

            To learn more about this pagination parameter, see
            `Pagination <https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination>`__.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    offset: int = proto.Field(
        proto.INT64,
        number=2,
    )
    limit: int = proto.Field(
        proto.INT64,
        number=3,
    )


class QueryAudienceExportResponse(proto.Message):
    r"""A list of users in an audience export.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        audience_export (google.analytics.data_v1beta.types.AudienceExport):
            Configuration data about AudienceExport being
            queried. Returned to help interpret the audience
            rows in this response. For example, the
            dimensions in this AudienceExport correspond to
            the columns in the AudienceRows.

            This field is a member of `oneof`_ ``_audience_export``.
        audience_rows (MutableSequence[google.analytics.data_v1beta.types.AudienceRow]):
            Rows for each user in an audience export. The
            number of rows in this response will be less
            than or equal to request's page size.
        row_count (int):
            The total number of rows in the AudienceExport result.
            ``rowCount`` is independent of the number of rows returned
            in the response, the ``limit`` request parameter, and the
            ``offset`` request parameter. For example if a query returns
            175 rows and includes ``limit`` of 50 in the API request,
            the response will contain ``rowCount`` of 175 but only 50
            rows.

            To learn more about this pagination parameter, see
            `Pagination <https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination>`__.

            This field is a member of `oneof`_ ``_row_count``.
    """

    audience_export: "AudienceExport" = proto.Field(
        proto.MESSAGE,
        number=1,
        optional=True,
        message="AudienceExport",
    )
    audience_rows: MutableSequence["AudienceRow"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="AudienceRow",
    )
    row_count: int = proto.Field(
        proto.INT32,
        number=3,
        optional=True,
    )


class AudienceRow(proto.Message):
    r"""Dimension value attributes for the audience user row.

    Attributes:
        dimension_values (MutableSequence[google.analytics.data_v1beta.types.AudienceDimensionValue]):
            Each dimension value attribute for an
            audience user. One dimension value will be added
            for each dimension column requested.
    """

    dimension_values: MutableSequence["AudienceDimensionValue"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AudienceDimensionValue",
    )


class AudienceDimension(proto.Message):
    r"""An audience dimension is a user attribute. Specific user attributed
    are requested and then later returned in the
    ``QueryAudienceExportResponse``.

    Attributes:
        dimension_name (str):
            Optional. The API name of the dimension. See the `API
            Dimensions <https://developers.google.com/analytics/devguides/reporting/data/v1/audience-list-api-schema#dimensions>`__
            for the list of dimension names.
    """

    dimension_name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AudienceDimensionValue(proto.Message):
    r"""The value of a dimension.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        value (str):
            Value as a string if the dimension type is a
            string.

            This field is a member of `oneof`_ ``one_value``.
    """

    value: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="one_value",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
