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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.ads.admanager_v1.types import report_definition, report_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "RunReportRequest",
        "RunReportMetadata",
        "RunReportResponse",
        "GetReportRequest",
        "ListReportsRequest",
        "ListReportsResponse",
        "CreateReportRequest",
        "UpdateReportRequest",
        "FetchReportResultRowsRequest",
        "FetchReportResultRowsResponse",
    },
)


class RunReportRequest(proto.Message):
    r"""Request message for a running a report.

    Attributes:
        name (str):
            Required. The report to run. Format:
            ``networks/{network_code}/reports/{report_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RunReportMetadata(proto.Message):
    r"""``RunReport`` operation metadata.

    Attributes:
        percent_complete (int):
            An estimate of how close this report is to
            being completed. Will always be 100 for failed
            and completed reports.
        report (str):
            The result's parent report.
    """

    percent_complete: int = proto.Field(
        proto.INT32,
        number=2,
    )
    report: str = proto.Field(
        proto.STRING,
        number=4,
    )


class RunReportResponse(proto.Message):
    r"""Response message for a completed ``RunReport`` operation.

    Attributes:
        report_result (str):
            The unique name of the generated result. Use with
            ``FetchReportResultRows`` to retrieve data.
    """

    report_result: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetReportRequest(proto.Message):
    r"""Request object for ``GetReport`` method.

    Attributes:
        name (str):
            Required. The resource name of the report. Format:
            ``networks/{network_code}/reports/{report_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListReportsRequest(proto.Message):
    r"""Request object for ``ListReports`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of reports.
            Format: ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of ``Reports`` to return. The
            service may return fewer than this value. If unspecified, at
            most 50 ``Reports`` will be returned. The maximum value is
            1000; values greater than 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListReports`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListReports`` must match the call that provided the page
            token.
        filter (str):
            Optional. Expression to filter the response.
            See syntax details at
            https://developers.google.com/ad-manager/api/beta/filters
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


class ListReportsResponse(proto.Message):
    r"""Response object for ``ListReportsResponse`` containing matching
    ``Report`` objects.

    Attributes:
        reports (MutableSequence[google.ads.admanager_v1.types.Report]):
            The ``Report`` objects from the specified network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of ``Report`` objects. If a filter was included
            in the request, this reflects the total number after the
            filtering is applied.

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

    reports: MutableSequence[report_messages.Report] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=report_messages.Report,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CreateReportRequest(proto.Message):
    r"""Request object for ``CreateReport`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this ``Report`` will be
            created. Format: ``networks/{network_code}``
        report (google.ads.admanager_v1.types.Report):
            Required. The ``Report`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    report: report_messages.Report = proto.Field(
        proto.MESSAGE,
        number=2,
        message=report_messages.Report,
    )


class UpdateReportRequest(proto.Message):
    r"""Request object for ``UpdateReport`` method.

    Attributes:
        report (google.ads.admanager_v1.types.Report):
            Required. The ``Report`` to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    report: report_messages.Report = proto.Field(
        proto.MESSAGE,
        number=1,
        message=report_messages.Report,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class FetchReportResultRowsRequest(proto.Message):
    r"""The request message for the fetch report result rows
    endpoint.

    Attributes:
        name (str):
            The report result being fetched. Format:
            ``networks/{network_code}/reports/{report_id}/results/{report_result_id}``
        page_size (int):
            Optional. The maximum number of rows to
            return. The service may return fewer than this
            value. If unspecified, at most 1,000 rows will
            be returned. The maximum value is 10,000; values
            greater than 10,000 will be reduced to 10,000.
        page_token (str):
            Optional. A page token, received from a previous
            ``FetchReportResultRows`` call. Provide this to retrieve the
            second and subsequent batches of rows.
    """

    name: str = proto.Field(
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


class FetchReportResultRowsResponse(proto.Message):
    r"""The response message for the fetch report result rows
    endpoint.

    Attributes:
        rows (MutableSequence[google.ads.admanager_v1.types.ReportDataTable.Row]):
            Up to ``page_size`` rows of report data.
        run_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which the report was scheduled to
            run. For non-scheduled reports, this is the time
            at which the report was requested to be run.
        date_ranges (MutableSequence[google.ads.admanager_v1.types.ReportDefinition.DateRange.FixedDateRange]):
            The computed fixed date ranges this report includes. Only
            returned with the first page of results (when page_token is
            not included in the request).
        comparison_date_ranges (MutableSequence[google.ads.admanager_v1.types.ReportDefinition.DateRange.FixedDateRange]):
            The computed comparison fixed date ranges this report
            includes. Only returned with the first page of results (when
            page_token is not included in the request).
        total_row_count (int):
            The total number of rows available from this report. Useful
            for pagination. Only returned with the first page of results
            (when page_token is not included in the request).
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    rows: MutableSequence[report_messages.ReportDataTable.Row] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=report_messages.ReportDataTable.Row,
    )
    run_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    date_ranges: MutableSequence[
        report_definition.ReportDefinition.DateRange.FixedDateRange
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=report_definition.ReportDefinition.DateRange.FixedDateRange,
    )
    comparison_date_ranges: MutableSequence[
        report_definition.ReportDefinition.DateRange.FixedDateRange
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=report_definition.ReportDefinition.DateRange.FixedDateRange,
    )
    total_row_count: int = proto.Field(
        proto.INT32,
        number=5,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=6,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
