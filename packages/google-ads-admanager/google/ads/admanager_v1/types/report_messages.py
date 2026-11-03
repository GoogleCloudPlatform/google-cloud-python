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

from google.ads.admanager_v1.types import report_definition as gaa_report_definition
from google.ads.admanager_v1.types import (
    report_delivery,
    report_value,
    report_visibility_enum,
)

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "Report",
        "ReportDataTable",
    },
)


class Report(proto.Message):
    r"""The ``Report`` resource.

    Attributes:
        name (str):
            Identifier. The resource name of the report. Report resource
            name have the form:
            ``networks/{network_code}/reports/{report_id}``
        report_id (int):
            Output only. Report ID.
        visibility (google.ads.admanager_v1.types.ReportVisibilityEnum.ReportVisibility):
            Optional. The visibility of a report.
        report_definition (google.ads.admanager_v1.types.ReportDefinition):
            Required. The report definition of the
            report.
        draft_report_definition (google.ads.admanager_v1.types.ReportDefinition):
            Optional. The draft report definition of the
            report.
        display_name (str):
            Optional. Display name for the report.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The instant this report was last
            modified.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The instant this report was
            created.
        locale (str):
            Output only. The locale of this report.
            Locale is set from the user's locale at the time
            of the request. Locale can't be modified.
        schedule_options (google.ads.admanager_v1.types.ScheduleOptions):
            Optional. The schedule options of this
            report.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    report_id: int = proto.Field(
        proto.INT64,
        number=3,
    )
    visibility: report_visibility_enum.ReportVisibilityEnum.ReportVisibility = (
        proto.Field(
            proto.ENUM,
            number=2,
            enum=report_visibility_enum.ReportVisibilityEnum.ReportVisibility,
        )
    )
    report_definition: gaa_report_definition.ReportDefinition = proto.Field(
        proto.MESSAGE,
        number=4,
        message=gaa_report_definition.ReportDefinition,
    )
    draft_report_definition: gaa_report_definition.ReportDefinition = proto.Field(
        proto.MESSAGE,
        number=14,
        message=gaa_report_definition.ReportDefinition,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    locale: str = proto.Field(
        proto.STRING,
        number=8,
    )
    schedule_options: report_delivery.ScheduleOptions = proto.Field(
        proto.MESSAGE,
        number=9,
        message=report_delivery.ScheduleOptions,
    )


class ReportDataTable(proto.Message):
    r"""A table containing report data including dimension and metric
    values.

    """

    class Row(proto.Message):
        r"""A row of report data.

        Attributes:
            dimension_values (MutableSequence[google.ads.admanager_v1.types.ReportValue]):
                The order of the dimension values is the same
                as the order of the dimensions specified in the
                request.
            metric_value_groups (MutableSequence[google.ads.admanager_v1.types.ReportDataTable.MetricValueGroup]):
                The length of the metric_value_groups field will be equal to
                the length of the date_ranges field in the fetch response.
                The metric_value_groups field is ordered such that each
                index corresponds to the date_range at the same index. For
                example, given date_ranges [x, y], metric_value_groups will
                have a length of two. The first entry in metric_value_groups
                represents the metrics for date x and the second entry in
                metric_value_groups represents the metrics for date y.
        """

        dimension_values: MutableSequence[report_value.ReportValue] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message=report_value.ReportValue,
            )
        )
        metric_value_groups: MutableSequence["ReportDataTable.MetricValueGroup"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="ReportDataTable.MetricValueGroup",
            )
        )

    class MetricValueGroup(proto.Message):
        r"""Contains all metric values requested for a single date range
        and set of column dimension values (returned in the columns
        field of the response). The order of the metrics in each field
        corresponds to the order of the metrics specified in the
        request.

        Attributes:
            primary_values (MutableSequence[google.ads.admanager_v1.types.ReportValue]):
                Data for the PRIMARY MetricValueType.
            primary_percent_of_total_values (MutableSequence[google.ads.admanager_v1.types.ReportValue]):
                Data for the PRIMARY_PERCENT_OF_TOTAL MetricValueType.
            comparison_values (MutableSequence[google.ads.admanager_v1.types.ReportValue]):
                Data for the COMPARISON MetricValueType.
            comparison_percent_of_total_values (MutableSequence[google.ads.admanager_v1.types.ReportValue]):
                Data for the COMPARISON_PERCENT_OF_TOTAL MetricValueType.
            absolute_change_values (MutableSequence[google.ads.admanager_v1.types.ReportValue]):
                Data for the ABSOLUTE_CHANGE MetricValueType.
            relative_change_values (MutableSequence[google.ads.admanager_v1.types.ReportValue]):
                Data for the RELATIVE_CHANGE MetricValueType.
            flag_values (MutableSequence[bool]):
                If true, the flag's conditions are met. If false, the flag's
                conditions are not met. flag_values has the same length as
                flags and index i of flag_values represents the flag at
                index i of flags.
        """

        primary_values: MutableSequence[report_value.ReportValue] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=report_value.ReportValue,
        )
        primary_percent_of_total_values: MutableSequence[report_value.ReportValue] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message=report_value.ReportValue,
            )
        )
        comparison_values: MutableSequence[report_value.ReportValue] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=3,
                message=report_value.ReportValue,
            )
        )
        comparison_percent_of_total_values: MutableSequence[
            report_value.ReportValue
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=4,
            message=report_value.ReportValue,
        )
        absolute_change_values: MutableSequence[report_value.ReportValue] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=5,
                message=report_value.ReportValue,
            )
        )
        relative_change_values: MutableSequence[report_value.ReportValue] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=6,
                message=report_value.ReportValue,
            )
        )
        flag_values: MutableSequence[bool] = proto.RepeatedField(
            proto.BOOL,
            number=7,
        )


__all__ = tuple(sorted(__protobuf__.manifest))
