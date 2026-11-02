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

import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.appoptimize.v1beta",
    manifest={
        "CreateReportRequest",
        "Report",
        "Scope",
        "GetReportRequest",
        "ListReportsRequest",
        "ListReportsResponse",
        "DeleteReportRequest",
        "ReadReportRequest",
        "ReadReportResponse",
        "Column",
        "OperationMetadata",
    },
)


class CreateReportRequest(proto.Message):
    r"""Request message for the ``CreateReport`` method.

    Attributes:
        parent (str):
            Required. The parent Google Cloud project that will own the
            report.

            This value does not define the scope of the report data. See
            ``Report.scope`` for setting the data scope.

            Format: ``projects/{project}/locations/{location}``.
        report_id (str):
            Required. The ID to use for this report. This
            ID must be unique within the parent project and
            should comply with RFC 1034 restrictions
            (letters, numbers, and hyphen, with the first
            character a letter, the last a letter or a
            number, and a 63 character maximum).
        report (google.cloud.appoptimize_v1beta.types.Report):
            Required. The report resource to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    report_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    report: "Report" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Report",
    )


class Report(proto.Message):
    r"""A configuration that defines the parameters for the data
    represented by a report.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp in UTC of when this
            report expires. Once the report expires, it will
            no longer be accessible and the report's
            underlying data will be deleted.

            This field is a member of `oneof`_ ``expiration``.
        name (str):
            Identifier. The name of this report.
        dimensions (MutableSequence[str]):
            Required. A list of dimensions to include in the report.
            Supported values:

            - ``project``
            - ``application``
            - ``service_or_workload``
            - ``resource``
            - ``resource_type``
            - ``location``
            - ``product_display_name``
            - ``sku``
            - ``month``
            - ``day``
            - ``hour``

            To aggregate results by time, specify at least one time
            dimension (``month``, ``day``, or ``hour``). All time
            dimensions use Pacific Time, respect Daylight Saving Time
            (DST), and follow these ISO 8601 formats:

            - ``month``: ``YYYY-MM`` (e.g., ``2024-01``)
            - ``day``: ``YYYY-MM-DD`` (e.g., ``2024-01-10``)
            - ``hour``: ``YYYY-MM-DDTHH`` (e.g., ``2024-01-10T00``)

            If the time range filter does not align with the selected
            time dimension, the range is expanded to encompass the full
            period of the finest-grained time dimension.

            For example, if the filter is ``2026-01-10`` through
            ``2026-01-12`` and the ``month`` dimension is selected, the
            effective time range expands to include all of January
            (``2026-01-01`` to ``2026-02-01``).
        metrics (MutableSequence[str]):
            Required. A list of metrics to include in the report.
            Supported values:

            - ``cost``
            - ``cpu_mean_utilization``
            - ``cpu_usage_core_seconds``
            - ``cpu_allocation_core_seconds``
            - ``cpu_p95_utilization``
            - ``memory_mean_utilization``
            - ``memory_usage_byte_seconds``
            - ``memory_allocation_byte_seconds``
            - ``memory_p95_utilization``
        scopes (MutableSequence[google.cloud.appoptimize_v1beta.types.Scope]):
            Optional. The resource containers for which
            to fetch data. Default is the project specified
            in the report's parent.
        filter (str):
            Optional. A Common Expression Language (CEL) expression used
            to filter the data for the report.

            Predicates may refer to any dimension. Filtering must
            conform to these constraints:

            - All string field predicates must use exact string matches.
            - Multiple predicates referring to the same string field
              must be joined using the logical OR operator ('\|\|').
            - All other predicates must be joined using the logical AND
              operator (``&&``).
            - A predicate on a time dimension (e.g., ``day``) specifying
              the start time must use a greater-than-or-equal-to
              comparison (``>=``).
            - A predicate on a time dimension specifying the end time
              must use a less-than comparison (``<``).

            Examples:

            1. Filter by a specific resource type:
               ``"resource_type == 'compute.googleapis.com/Instance'"``

            2. Filter data points that fall within a specific absolute
               time interval:
               ``"hour >= timestamp('2024-01-01T00:00:00Z') && hour < timestamp('2024-02-01T00:00:00Z')"``

            3. Filter data points that fall within the past 72 hours:
               ``"hour >= now - duration('72h')"``

            4. Combine string predicate with time interval predicate:
               ``"(location == 'us-east1' || location == 'us-west1') && hour >= timestamp('2023-12-01T00:00:00Z') && hour < timestamp('2024-02-01T00:00:00Z')"``

            If the filter omits time dimensions (``month``, ``day``,
            ``hour``), the report defaults to a 7-day range ending at
            the previous Pacific Time midnight, with Daylight Saving
            Time (DST) applied.

            For example, if the current Pacific Time is
            ``2026-01-05T12:00:00``, the default range is
            ``2025-12-29T00:00:00`` to ``2026-01-05T00:00:00`` Pacific
            time.
    """

    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="expiration",
        message=timestamp_pb2.Timestamp,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dimensions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    metrics: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    scopes: MutableSequence["Scope"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="Scope",
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )


class Scope(proto.Message):
    r"""Specifies the report scope.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        project (str):
            Required. A Google Cloud Platform project to fetch data
            from.

            Format: ``"projects/{project}"``.

            This field is a member of `oneof`_ ``scope``.
        application (str):
            Required. An App Hub Application to fetch data from.

            Format:
            ``"projects/{project}/locations/{location}/applications/{application}"``.

            This field is a member of `oneof`_ ``scope``.
    """

    project: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="scope",
    )
    application: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="scope",
    )


class GetReportRequest(proto.Message):
    r"""Request message for the ``GetReport`` method.

    Attributes:
        name (str):
            Required. The name of the report to retrieve.

            Format:
            ``projects/{project}/locations/{location}/reports/{report_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListReportsRequest(proto.Message):
    r"""Request message for the ``ListReports`` method.

    Attributes:
        parent (str):
            Required. The parent project whose reports are to be listed.

            Format: ``projects/{project}/locations/{location}``.
        page_size (int):
            Optional. The maximum number of reports to
            return. The service may return fewer than this
            value. If unspecified, the server will determine
            the number of results to return.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListReports`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListReports`` must match the call that provided the page
            token.
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


class ListReportsResponse(proto.Message):
    r"""Response message for the ``ListReports`` method.

    Attributes:
        reports (MutableSequence[google.cloud.appoptimize_v1beta.types.Report]):
            The list of reports.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is empty, there are no subsequent
            pages.
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


class DeleteReportRequest(proto.Message):
    r"""Request message for the ``DeleteReport`` method.

    Attributes:
        name (str):
            Required. The name of the report to delete.

            Format:
            ``projects/{project}/locations/{location}/reports/{report_id}``.
        allow_missing (bool):
            Optional. If set to true, and the report is
            not found, the request will succeed but no
            action will be taken on the server.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    allow_missing: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class ReadReportRequest(proto.Message):
    r"""Request message for the ``ReadReport`` method.

    Attributes:
        name (str):
            Required. The resource name of the report to query.

            Format:
            ``projects/{project}/locations/{location}/reports/{report_id}``.
        page_size (int):
            Optional. The maximum number of rows to
            return. The service may return fewer than this
            value. If unspecified, at most 10,000 rows will
            be returned per page. The maximum allowed value
            is 25,000; values above 25,000 are coerced to
            25,000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ReadReport`` call, to retrieve the subsequent page of
            results. When ``page_token`` is specified, ``job_reference``
            must also be provided from the previous response, and the
            ``statement`` field must not be set.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ReadReportResponse(proto.Message):
    r"""Response message for the ``ReadReport`` method.

    Attributes:
        rows (MutableSequence[google.protobuf.struct_pb2.ListValue]):
            A list of rows, where each row represents a
            record from the report.
        columns (MutableSequence[google.cloud.appoptimize_v1beta.types.Column]):
            The columns describing the structure of the data in the
            ``rows`` field.
        next_page_token (str):
            A token that can be sent as ``page_token`` in a subsequent
            ``ReadReport`` request to retrieve the next page of results.
            If this field is empty, there are no further pages.
    """

    @property
    def raw_page(self):
        return self

    rows: MutableSequence[struct_pb2.ListValue] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=struct_pb2.ListValue,
    )
    columns: MutableSequence["Column"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="Column",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class Column(proto.Message):
    r"""Describes a single column within ``Columns``.

    Attributes:
        name (str):
            The name of the column.

            This field:

            - Contains only letters (a-z, A-Z), numbers (0-9), or
              underscores (\_);
            - Start with a letter or underscore; and
            - Has a maximum length is 128 characters.
        type_ (str):
            The data type of the column.

            Supported values include:

            - ``STRING``
            - ``INT64``
            - ``FLOAT64``
            - ``BOOLEAN``
            - ``TIMESTAMP``
            - ``RECORD``

            ``RECORD`` indicates that the field contains a nested
            schema, described in the ``columns`` property of this
            ``Column``.
        mode (str):
            The mode of the column, indicating if it is nullable,
            required, or repeated.

            Possible values:

            - ``NULLABLE``: The column allows NULL values.
            - ``REQUIRED``: The column does not allow NULL values.
            - ``REPEATED``: The column contains an array of values.
        columns (MutableSequence[google.cloud.appoptimize_v1beta.types.Column]):
            If the ``type`` of this column is ``RECORD``, this sub-field
            describes the nested structure.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=2,
    )
    mode: str = proto.Field(
        proto.STRING,
        number=3,
    )
    columns: MutableSequence["Column"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="Column",
    )


class OperationMetadata(proto.Message):
    r"""Represents metadata related to the creation of a Report. This value
    is embedded in the Operation object returned by ``CreateReport``.

    """


__all__ = tuple(sorted(__protobuf__.manifest))
