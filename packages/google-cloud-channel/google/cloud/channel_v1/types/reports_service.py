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
import google.type.date_pb2 as date_pb2  # type: ignore
import google.type.datetime_pb2 as datetime_pb2  # type: ignore
import google.type.decimal_pb2 as decimal_pb2  # type: ignore
import google.type.money_pb2 as money_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.channel.v1",
    manifest={
        "RunReportJobRequest",
        "RunReportJobResponse",
        "FetchReportResultsRequest",
        "FetchReportResultsResponse",
        "ListReportsRequest",
        "ListReportsResponse",
        "ReportJob",
        "ReportResultsMetadata",
        "Column",
        "DateRange",
        "Row",
        "ReportValue",
        "ReportStatus",
        "Report",
    },
)


class RunReportJobRequest(proto.Message):
    r"""Request message for
    [CloudChannelReportsService.RunReportJob][google.cloud.channel.v1.CloudChannelReportsService.RunReportJob].

    Attributes:
        name (str):
            Required. The report's resource name. Specifies the account
            and report used to generate report data. The report_id
            identifier is a UID (for example, ``613bf59q``). Name uses
            the format: accounts/{account_id}/reports/{report_id}
        date_range (google.cloud.channel_v1.types.DateRange):
            Optional. The range of usage or invoice dates
            to include in the result.
        filter (str):
            Optional. A structured string that defines conditions on
            dimension columns to restrict the report output.

            Filters support logical operators (AND, OR, NOT) and
            conditional operators (=, !=, <, >, <=, and >=) using
            ``column_id`` as keys.

            For example:
            ``(customer:"accounts/C123abc/customers/S456def" OR customer:"accounts/C123abc/customers/S789ghi") AND invoice_start_date.year >= 2022``
        language_code (str):
            Optional. The BCP-47 language code, such as
            "en-US".  If specified, the response is
            localized to the corresponding language code if
            the original data sources support it.
            Default is "en-US".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    date_range: "DateRange" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DateRange",
    )
    filter: str = proto.Field(
        proto.STRING,
        number=3,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=4,
    )


class RunReportJobResponse(proto.Message):
    r"""Response message for
    [CloudChannelReportsService.RunReportJob][google.cloud.channel.v1.CloudChannelReportsService.RunReportJob].

    Attributes:
        report_job (google.cloud.channel_v1.types.ReportJob):
            Pass ``report_job.name`` to
            [FetchReportResultsRequest.report_job][google.cloud.channel.v1.FetchReportResultsRequest.report_job]
            to retrieve the report's results.
        report_metadata (google.cloud.channel_v1.types.ReportResultsMetadata):
            The metadata for the report's results
            (display name, columns, row count, and date
            range). If you view this before the operation
            finishes, you may see incomplete data.
    """

    report_job: "ReportJob" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ReportJob",
    )
    report_metadata: "ReportResultsMetadata" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ReportResultsMetadata",
    )


class FetchReportResultsRequest(proto.Message):
    r"""Request message for
    [CloudChannelReportsService.FetchReportResults][google.cloud.channel.v1.CloudChannelReportsService.FetchReportResults].

    Attributes:
        report_job (str):
            Required. The report job created by
            [CloudChannelReportsService.RunReportJob][google.cloud.channel.v1.CloudChannelReportsService.RunReportJob].
            Report_job uses the format:
            accounts/{account_id}/reportJobs/{report_job_id}
        page_size (int):
            Optional. Requested page size of the report.
            The server may return fewer results than
            requested. If you don't specify a page size, the
            server uses a sensible default (may change over
            time).

            The maximum value is 30,000; the server will
            change larger values to 30,000.
        page_token (str):
            Optional. A token that specifies a page of results beyond
            the first page. Obtained through
            [FetchReportResultsResponse.next_page_token][google.cloud.channel.v1.FetchReportResultsResponse.next_page_token]
            of the previous
            [CloudChannelReportsService.FetchReportResults][google.cloud.channel.v1.CloudChannelReportsService.FetchReportResults]
            call.
        partition_keys (MutableSequence[str]):
            Optional. List of keys specifying which
            report partitions to return. If empty, returns
            all partitions.
    """

    report_job: str = proto.Field(
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
    partition_keys: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


class FetchReportResultsResponse(proto.Message):
    r"""Response message for
    [CloudChannelReportsService.FetchReportResults][google.cloud.channel.v1.CloudChannelReportsService.FetchReportResults].
    Contains a tabular representation of the report results.

    Attributes:
        report_metadata (google.cloud.channel_v1.types.ReportResultsMetadata):
            The metadata for the report results (display
            name, columns, row count, and date ranges).
        rows (MutableSequence[google.cloud.channel_v1.types.Row]):
            The report's lists of values. Each row follows the settings
            and ordering of the columns from ``report_metadata``.
        next_page_token (str):
            Pass this token to
            [FetchReportResultsRequest.page_token][google.cloud.channel.v1.FetchReportResultsRequest.page_token]
            to retrieve the next page of results.
    """

    @property
    def raw_page(self):
        return self

    report_metadata: "ReportResultsMetadata" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="ReportResultsMetadata",
    )
    rows: MutableSequence["Row"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Row",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListReportsRequest(proto.Message):
    r"""Request message for
    [CloudChannelReportsService.ListReports][google.cloud.channel.v1.CloudChannelReportsService.ListReports].

    Attributes:
        parent (str):
            Required. The resource name of the partner account to list
            available reports for. Parent uses the format:
            accounts/{account_id}
        page_size (int):
            Optional. Requested page size of the report.
            The server might return fewer results than
            requested. If unspecified, returns 20 reports.
            The maximum value is 100.
        page_token (str):
            Optional. A token that specifies a page of results beyond
            the first page. Obtained through
            [ListReportsResponse.next_page_token][google.cloud.channel.v1.ListReportsResponse.next_page_token]
            of the previous
            [CloudChannelReportsService.ListReports][google.cloud.channel.v1.CloudChannelReportsService.ListReports]
            call.
        language_code (str):
            Optional. The BCP-47 language code, such as
            "en-US".  If specified, the response is
            localized to the corresponding language code if
            the original data sources support it.
            Default is "en-US".
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
    language_code: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListReportsResponse(proto.Message):
    r"""Response message for
    [CloudChannelReportsService.ListReports][google.cloud.channel.v1.CloudChannelReportsService.ListReports].

    Attributes:
        reports (MutableSequence[google.cloud.channel_v1.types.Report]):
            The reports available to the partner.
        next_page_token (str):
            Pass this token to
            [FetchReportResultsRequest.page_token][google.cloud.channel.v1.FetchReportResultsRequest.page_token]
            to retrieve the next page of results.
    """

    @property
    def raw_page(self):
        return self

    reports: MutableSequence["Report"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Report",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ReportJob(proto.Message):
    r"""The result of a [RunReportJob][] operation. Contains the name to use
    in
    [FetchReportResultsRequest.report_job][google.cloud.channel.v1.FetchReportResultsRequest.report_job]
    and the status of the operation.

    Attributes:
        name (str):
            Required. The resource name of a report job. Name uses the
            format: ``accounts/{account_id}/reportJobs/{report_job_id}``
        report_status (google.cloud.channel_v1.types.ReportStatus):
            The current status of report generation.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    report_status: "ReportStatus" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ReportStatus",
    )


class ReportResultsMetadata(proto.Message):
    r"""The features describing the data. Returned by
    [CloudChannelReportsService.RunReportJob][google.cloud.channel.v1.CloudChannelReportsService.RunReportJob]
    and
    [CloudChannelReportsService.FetchReportResults][google.cloud.channel.v1.CloudChannelReportsService.FetchReportResults].

    Attributes:
        report (google.cloud.channel_v1.types.Report):
            Details of the completed report.
        row_count (int):
            The total number of rows of data in the final
            report.
        date_range (google.cloud.channel_v1.types.DateRange):
            The date range of reported usage.
        preceding_date_range (google.cloud.channel_v1.types.DateRange):
            The usage dates immediately preceding ``date_range`` with
            the same duration. Use this to calculate trending usage and
            costs. This is only populated if you request trending data.

            For example, if ``date_range`` is July 1-15,
            ``preceding_date_range`` will be June 16-30.
    """

    report: "Report" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Report",
    )
    row_count: int = proto.Field(
        proto.INT64,
        number=2,
    )
    date_range: "DateRange" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DateRange",
    )
    preceding_date_range: "DateRange" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="DateRange",
    )


class Column(proto.Message):
    r"""The definition of a report column. Specifies the data
    properties in the corresponding position of the report rows.

    Attributes:
        column_id (str):
            The unique name of the column (for example, customer_domain,
            channel_partner, customer_cost). You can use column IDs in
            [RunReportJobRequest.filter][google.cloud.channel.v1.RunReportJobRequest.filter].
            To see all reports and their columns, call
            [CloudChannelReportsService.ListReports][google.cloud.channel.v1.CloudChannelReportsService.ListReports].
        display_name (str):
            The column's display name.
        data_type (google.cloud.channel_v1.types.Column.DataType):
            The type of the values for this column.
    """

    class DataType(proto.Enum):
        r"""Available data types for columns. Corresponds to the fields in the
        ReportValue ``oneof`` field.

        Values:
            DATA_TYPE_UNSPECIFIED (0):
                Not used.
            STRING (1):
                ReportValues for this column will use string_value.
            INT (2):
                ReportValues for this column will use int_value.
            DECIMAL (3):
                ReportValues for this column will use decimal_value.
            MONEY (4):
                ReportValues for this column will use money_value.
            DATE (5):
                ReportValues for this column will use date_value.
            DATE_TIME (6):
                ReportValues for this column will use date_time_value.
        """

        DATA_TYPE_UNSPECIFIED = 0
        STRING = 1
        INT = 2
        DECIMAL = 3
        MONEY = 4
        DATE = 5
        DATE_TIME = 6

    column_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    data_type: DataType = proto.Field(
        proto.ENUM,
        number=3,
        enum=DataType,
    )


class DateRange(proto.Message):
    r"""A representation of usage or invoice date ranges.

    Attributes:
        usage_start_date_time (google.type.datetime_pb2.DateTime):
            The earliest usage date time (inclusive).

            If you use time groupings (daily, weekly, etc), each group
            uses midnight to midnight (Pacific time). The usage start
            date is rounded down to include all usage from the specified
            date. We recommend that clients pass
            ``usage_start_date_time`` in Pacific time.
        usage_end_date_time (google.type.datetime_pb2.DateTime):
            The latest usage date time (exclusive).

            If you use time groupings (daily, weekly, etc), each group
            uses midnight to midnight (Pacific time). The usage end date
            is rounded down to include all usage from the specified
            date. We recommend that clients pass
            ``usage_start_date_time`` in Pacific time.
        invoice_start_date (google.type.date_pb2.Date):
            The earliest invoice date (inclusive).

            If this value is not the first day of a month,
            this will move it back to the first day of the
            given month.
        invoice_end_date (google.type.date_pb2.Date):
            The latest invoice date (inclusive).

            If this value is not the last day of a month,
            this will move it forward to the last day of the
            given month.
    """

    usage_start_date_time: datetime_pb2.DateTime = proto.Field(
        proto.MESSAGE,
        number=1,
        message=datetime_pb2.DateTime,
    )
    usage_end_date_time: datetime_pb2.DateTime = proto.Field(
        proto.MESSAGE,
        number=2,
        message=datetime_pb2.DateTime,
    )
    invoice_start_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=3,
        message=date_pb2.Date,
    )
    invoice_end_date: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=4,
        message=date_pb2.Date,
    )


class Row(proto.Message):
    r"""A row of report values.

    Attributes:
        values (MutableSequence[google.cloud.channel_v1.types.ReportValue]):
            The list of values in the row.
        partition_key (str):
            The key for the partition this row belongs
            to. This field is empty if the report is not
            partitioned.
    """

    values: MutableSequence["ReportValue"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ReportValue",
    )
    partition_key: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ReportValue(proto.Message):
    r"""A single report value.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        string_value (str):
            A value of type ``string``.

            This field is a member of `oneof`_ ``value``.
        int_value (int):
            A value of type ``int``.

            This field is a member of `oneof`_ ``value``.
        decimal_value (google.type.decimal_pb2.Decimal):
            A value of type ``google.type.Decimal``, representing
            non-integer numeric values.

            This field is a member of `oneof`_ ``value``.
        money_value (google.type.money_pb2.Money):
            A value of type ``google.type.Money`` (currency code, whole
            units, decimal units).

            This field is a member of `oneof`_ ``value``.
        date_value (google.type.date_pb2.Date):
            A value of type ``google.type.Date`` (year, month, day).

            This field is a member of `oneof`_ ``value``.
        date_time_value (google.type.datetime_pb2.DateTime):
            A value of type ``google.type.DateTime`` (year, month, day,
            hour, minute, second, and UTC offset or timezone.)

            This field is a member of `oneof`_ ``value``.
    """

    string_value: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="value",
    )
    int_value: int = proto.Field(
        proto.INT64,
        number=2,
        oneof="value",
    )
    decimal_value: decimal_pb2.Decimal = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="value",
        message=decimal_pb2.Decimal,
    )
    money_value: money_pb2.Money = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="value",
        message=money_pb2.Money,
    )
    date_value: date_pb2.Date = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="value",
        message=date_pb2.Date,
    )
    date_time_value: datetime_pb2.DateTime = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="value",
        message=datetime_pb2.DateTime,
    )


class ReportStatus(proto.Message):
    r"""Status of a report generation process.

    Attributes:
        state (google.cloud.channel_v1.types.ReportStatus.State):
            The current state of the report generation
            process.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The report generation's start time.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The report generation's completion time.
    """

    class State(proto.Enum):
        r"""Available states of report generation.

        Values:
            STATE_UNSPECIFIED (0):
                Not used.
            STARTED (1):
                Report processing started.
            WRITING (2):
                Data generated from the report is being
                staged.
            AVAILABLE (3):
                Report data is available for access.
            FAILED (4):
                Report failed.
        """

        STATE_UNSPECIFIED = 0
        STARTED = 1
        WRITING = 2
        AVAILABLE = 3
        FAILED = 4

    state: State = proto.Field(
        proto.ENUM,
        number=1,
        enum=State,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )


class Report(proto.Message):
    r"""The ID and description of a report that was used to generate
    report data. For example, "Google Cloud Daily Spend", "Google
    Workspace License Activity", etc.

    Attributes:
        name (str):
            Required. The report's resource name. Specifies the account
            and report used to generate report data. The report_id
            identifier is a UID (for example, ``613bf59q``).

            Name uses the format:
            accounts/{account_id}/reports/{report_id}
        display_name (str):
            A human-readable name for this report.
        columns (MutableSequence[google.cloud.channel_v1.types.Column]):
            The list of columns included in the report.
            This defines the schema of the report results.
        description (str):
            A description of other aspects of the report,
            such as the products it supports.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    columns: MutableSequence["Column"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="Column",
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
