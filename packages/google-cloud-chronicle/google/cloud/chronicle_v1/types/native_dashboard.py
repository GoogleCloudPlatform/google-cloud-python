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
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.chronicle_v1.types import dashboard_chart as gcc_dashboard_chart
from google.cloud.chronicle_v1.types import dashboard_query as gcc_dashboard_query

__protobuf__ = proto.module(
    package="google.cloud.chronicle.v1",
    manifest={
        "DashboardType",
        "DashboardAccess",
        "NativeDashboardView",
        "ExportNativeDashboardsRequest",
        "ExportNativeDashboardsResponse",
        "InlineDestination",
        "NativeDashboardWithChartsAndQueries",
        "ImportNativeDashboardsRequest",
        "ImportNativeDashboardsInlineSource",
        "ImportNativeDashboardsResponse",
        "ImportExportStatus",
        "NativeDashboard",
        "CreateNativeDashboardRequest",
        "GetNativeDashboardRequest",
        "ListNativeDashboardsRequest",
        "ListNativeDashboardsResponse",
        "UpdateNativeDashboardRequest",
        "DuplicateNativeDashboardRequest",
        "DeleteNativeDashboardRequest",
        "AddChartRequest",
        "AddChartResponse",
        "EditChartRequest",
        "EditChartResponse",
        "RemoveChartRequest",
        "DuplicateChartRequest",
        "DuplicateChartResponse",
        "DashboardUserData",
        "DashboardDefinition",
    },
)


class DashboardType(proto.Enum):
    r"""Type of the dashboard.

    Values:
        DASHBOARD_TYPE_UNSPECIFIED (0):
            Default unspecified.
        CURATED (1):
            Out of the box curated dashboards provided by
            Chronicle.
        PRIVATE (2):
            Private dashboards created by
            users/customers.
        PUBLIC (3):
            Public dashboards created by users/customers.
        CUSTOM (4):
            Custom dashboards
        MARKETPLACE (5):
            Marketplace dashboards
    """

    DASHBOARD_TYPE_UNSPECIFIED = 0
    CURATED = 1
    PRIVATE = 2
    PUBLIC = 3
    CUSTOM = 4
    MARKETPLACE = 5


class DashboardAccess(proto.Enum):
    r"""AccessType of the dashboard.

    Values:
        DASHBOARD_ACCESS_UNSPECIFIED (0):
            Default unspecified.
        DASHBOARD_PRIVATE (1):
            Private dashboards created by
            users/customers.
        DASHBOARD_PUBLIC (2):
            Public dashboards created by users/customers.
    """

    DASHBOARD_ACCESS_UNSPECIFIED = 0
    DASHBOARD_PRIVATE = 1
    DASHBOARD_PUBLIC = 2


class NativeDashboardView(proto.Enum):
    r"""NativeDashboardView indicates the scope of fields to populate
    when returning the dashboard resource.

    Values:
        NATIVE_DASHBOARD_VIEW_UNSPECIFIED (0):
            Defaults to basic.
        NATIVE_DASHBOARD_VIEW_BASIC (1):
            Include basic metadata about the dashboard
            without full definition.
        NATIVE_DASHBOARD_VIEW_FULL (2):
            Include everything.
    """

    NATIVE_DASHBOARD_VIEW_UNSPECIFIED = 0
    NATIVE_DASHBOARD_VIEW_BASIC = 1
    NATIVE_DASHBOARD_VIEW_FULL = 2


class ExportNativeDashboardsRequest(proto.Message):
    r"""Request message to export list of dashboard.

    Attributes:
        parent (str):
            Required. The parent resource that the
            dashboards to be exported belong to. Format:
            projects/{project}/locations/{location}/instances/{instance}
        names (MutableSequence[str]):
            Required. The resource names of the
            dashboards to export.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class ExportNativeDashboardsResponse(proto.Message):
    r"""Response message for exporting a dashboard.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        inline_destination (google.cloud.chronicle_v1.types.InlineDestination):
            The data for the exported dashboards included
            directly in the response.

            This field is a member of `oneof`_ ``destination``.
    """

    inline_destination: "InlineDestination" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="destination",
        message="InlineDestination",
    )


class InlineDestination(proto.Message):
    r"""InlineDestination for exporting a dashboard.

    Attributes:
        dashboards (MutableSequence[google.cloud.chronicle_v1.types.NativeDashboardWithChartsAndQueries]):
            Dashboards with charts and queries.
    """

    dashboards: MutableSequence["NativeDashboardWithChartsAndQueries"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="NativeDashboardWithChartsAndQueries",
        )
    )


class NativeDashboardWithChartsAndQueries(proto.Message):
    r"""NativeDashboardWithChartsAndQueries for exporting a
    dashboard.

    Attributes:
        dashboard (google.cloud.chronicle_v1.types.NativeDashboard):
            Optional. Native dashboard.
        dashboard_charts (MutableSequence[google.cloud.chronicle_v1.types.DashboardChart]):
            Optional. Charts in the dashboard.
        dashboard_queries (MutableSequence[google.cloud.chronicle_v1.types.DashboardQuery]):
            Optional. Queries in the dashboard.
    """

    dashboard: "NativeDashboard" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="NativeDashboard",
    )
    dashboard_charts: MutableSequence[gcc_dashboard_chart.DashboardChart] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message=gcc_dashboard_chart.DashboardChart,
        )
    )
    dashboard_queries: MutableSequence[gcc_dashboard_query.DashboardQuery] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message=gcc_dashboard_query.DashboardQuery,
        )
    )


class ImportNativeDashboardsRequest(proto.Message):
    r"""Request message to import dashboards.

    Attributes:
        parent (str):
            Required. The parent resource where this
            dashboard will be created. Format:
            projects/{project}/locations/{location}/instances/{instance}
        source (google.cloud.chronicle_v1.types.ImportNativeDashboardsInlineSource):
            Required. The data will imported from this
            proto.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    source: "ImportNativeDashboardsInlineSource" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ImportNativeDashboardsInlineSource",
    )


class ImportNativeDashboardsInlineSource(proto.Message):
    r"""Inline source for importing dashboards.

    Attributes:
        dashboards (MutableSequence[google.cloud.chronicle_v1.types.NativeDashboardWithChartsAndQueries]):
            Required. Dashboards with charts and queries.
    """

    dashboards: MutableSequence["NativeDashboardWithChartsAndQueries"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="NativeDashboardWithChartsAndQueries",
        )
    )


class ImportNativeDashboardsResponse(proto.Message):
    r"""Response message for importing dashboards.

    Attributes:
        results (MutableSequence[google.cloud.chronicle_v1.types.ImportExportStatus]):
            Output only. Represents the status of an
            import operation for multiple dashboards. Each
            dashboard's import status is tracked. A status
            of OK indicates the dashboard was ready for
            import. Otherwise, an appropriate error code and
            message are provided. Importantly, the import
            process is all-or-nothing: if even one dashboard
            fails to import, the entire import operation is
            aborted, and none of the dashboards are
            imported. The order of the statuses will be the
            same as in the import request.
    """

    results: MutableSequence["ImportExportStatus"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ImportExportStatus",
    )


class ImportExportStatus(proto.Message):
    r"""ImportExportStatus is a wrapper for dashboard name and
    status.

    Attributes:
        dashboard (str):
            The resource name of the dashboard if it was
            supplied in the request.
        status (google.rpc.status_pb2.Status):
            Output only. Status of the import/export
            operation.
    """

    dashboard: str = proto.Field(
        proto.STRING,
        number=1,
    )
    status: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=2,
        message=status_pb2.Status,
    )


class NativeDashboard(proto.Message):
    r"""NativeDashboard resource.

    Attributes:
        name (str):
            Output only. Name of the dashboard.
        display_name (str):
            Required. Dashboard display name/title
            visible to users.
        description (str):
            Optional. Description of the dashboard.
        definition (google.cloud.chronicle_v1.types.DashboardDefinition):
            Optional. Definition of the dashboard like
            metadata, visualization and datasource
            configuration etc.
        type_ (google.cloud.chronicle_v1.types.DashboardType):
            Output only. Whether it's an out of the box
            or custom created dashboard.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Creation time of dashboard.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time the dashboard was last
            edited.
        create_user_id (str):
            Output only. User who created the dashboard.
        update_user_id (str):
            Output only. User who last edited the
            dashboard.
        dashboard_user_data (google.cloud.chronicle_v1.types.DashboardUserData):
            Output only. User Preferences for a dashboard
        etag (str):
            Optional. This checksum is computed by the
            server based on the value of other fields, and
            may be sent on update and delete requests to
            ensure the client has an up-to-date value before
            proceeding.
        access (google.cloud.chronicle_v1.types.DashboardAccess):
            Output only. Access of the dashboard
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    definition: "DashboardDefinition" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="DashboardDefinition",
    )
    type_: "DashboardType" = proto.Field(
        proto.ENUM,
        number=5,
        enum="DashboardType",
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    create_user_id: str = proto.Field(
        proto.STRING,
        number=8,
    )
    update_user_id: str = proto.Field(
        proto.STRING,
        number=9,
    )
    dashboard_user_data: "DashboardUserData" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="DashboardUserData",
    )
    etag: str = proto.Field(
        proto.STRING,
        number=11,
    )
    access: "DashboardAccess" = proto.Field(
        proto.ENUM,
        number=12,
        enum="DashboardAccess",
    )


class CreateNativeDashboardRequest(proto.Message):
    r"""Request message to create a dashboard.

    Attributes:
        parent (str):
            Required. The parent resource where this
            dashboard will be created. Format:
            projects/{project}/locations/{location}/instances/{instance}
        native_dashboard (google.cloud.chronicle_v1.types.NativeDashboard):
            Required. The dashboard to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    native_dashboard: "NativeDashboard" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="NativeDashboard",
    )


class GetNativeDashboardRequest(proto.Message):
    r"""Request message to get a dashboard.

    Attributes:
        name (str):
            Required. The dashboard name to fetch.
            Format:

            projects/{project}/locations/{location}/instances/{instance}/nativeDashboards/{dashboard}
        view (google.cloud.chronicle_v1.types.NativeDashboardView):
            Optional. View indicates the scope of fields
            to populate when returning the dashboard
            resource. If unspecified, defaults to the basic
            view.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "NativeDashboardView" = proto.Field(
        proto.ENUM,
        number=2,
        enum="NativeDashboardView",
    )


class ListNativeDashboardsRequest(proto.Message):
    r"""Request message to list dashboards.

    Attributes:
        parent (str):
            Required. The parent owning this dashboard
            collection. Format:
            projects/{project}/locations/{location}/instances/{instance}
        page_size (int):
            Optional. The maximum number of dashboards to
            return. The service may return fewer than this
            value.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListDashboards`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListDashboards`` must match the call that provided the
            page token.
        view (google.cloud.chronicle_v1.types.NativeDashboardView):
            Optional. View indicates the scope of fields
            to populate when returning the dashboard
            resource. If unspecified, defaults to the basic
            view.
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
    view: "NativeDashboardView" = proto.Field(
        proto.ENUM,
        number=4,
        enum="NativeDashboardView",
    )


class ListNativeDashboardsResponse(proto.Message):
    r"""Response message for listing dashboards.

    Attributes:
        native_dashboards (MutableSequence[google.cloud.chronicle_v1.types.NativeDashboard]):
            The dashboards from the specified chronicle
            instance.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    native_dashboards: MutableSequence["NativeDashboard"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="NativeDashboard",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateNativeDashboardRequest(proto.Message):
    r"""Request message to update a dashboard.

    Attributes:
        native_dashboard (google.cloud.chronicle_v1.types.NativeDashboard):
            Required. The dashboard to update.

            The dashboard's ``name`` field is used to identify the
            dashboard to update. Format:
            projects/{project}/locations/{location}/instances/{instance}/nativeDashboards/{dashboard}
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. LINT.IfChange(update_mask_values) The list of
            fields to update. Supported paths are - display_name
            description definition.filters definition.charts type access
            dashboard_user_data.is_pinned
    """

    native_dashboard: "NativeDashboard" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="NativeDashboard",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DuplicateNativeDashboardRequest(proto.Message):
    r"""Request message to duplicate a dashboard.

    Attributes:
        name (str):
            Required. The dashboard name to duplicate.
            Format:

            projects/{project}/locations/{location}/instances/{instance}/nativeDashboards/{dashboard}
        native_dashboard (google.cloud.chronicle_v1.types.NativeDashboard):
            Required. Any fields that need modification
            can be passed through this like name,
            description etc.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    native_dashboard: "NativeDashboard" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="NativeDashboard",
    )


class DeleteNativeDashboardRequest(proto.Message):
    r"""Request message to delete a dashboard.

    Attributes:
        name (str):
            Required. The dashboard name to delete.
            Format:

            projects/{project}/locations/{location}/instances/{instance}/nativeDashboards/{dashboard}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class AddChartRequest(proto.Message):
    r"""Request message to add chart in a dashboard.

    Attributes:
        name (str):
            Required. The dashboard name to add chart in.
            Format:

            projects/{project}/locations/{location}/instances/{instance}/nativeDashboards/{dashboard}
        dashboard_query (google.cloud.chronicle_v1.types.DashboardQuery):
            Optional. Query used to create the chart.
        dashboard_chart (google.cloud.chronicle_v1.types.DashboardChart):
            Required. Chart to be added to the dashboard.
        chart_layout (google.cloud.chronicle_v1.types.DashboardDefinition.ChartConfig.ChartLayout):
            Required. ChartLayout for newly added chart.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dashboard_query: gcc_dashboard_query.DashboardQuery = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcc_dashboard_query.DashboardQuery,
    )
    dashboard_chart: gcc_dashboard_chart.DashboardChart = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcc_dashboard_chart.DashboardChart,
    )
    chart_layout: "DashboardDefinition.ChartConfig.ChartLayout" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="DashboardDefinition.ChartConfig.ChartLayout",
    )


class AddChartResponse(proto.Message):
    r"""Response message for adding chart in a dashboard.

    Attributes:
        native_dashboard (google.cloud.chronicle_v1.types.NativeDashboard):
            Dashboard with chart added in definition.
        dashboard_chart (google.cloud.chronicle_v1.types.DashboardChart):
            Created chart resource.
    """

    native_dashboard: "NativeDashboard" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="NativeDashboard",
    )
    dashboard_chart: gcc_dashboard_chart.DashboardChart = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcc_dashboard_chart.DashboardChart,
    )


class EditChartRequest(proto.Message):
    r"""Request message to edit chart in a dashboard.

    Attributes:
        name (str):
            Required. The dashboard name to edit chart
            in. Format:

            projects/{project}/locations/{location}/instances/{instance}/nativeDashboards/{dashboard}
        dashboard_query (google.cloud.chronicle_v1.types.DashboardQuery):
            Optional. Query for the edited chart.
        dashboard_chart (google.cloud.chronicle_v1.types.DashboardChart):
            Optional. Edited chart.
        edit_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The list of fields to edit for chart and query.
            Supported paths in chart are - dashboard_chart.display_name
            dashboard_chart.description
            dashboard_chart.chart_datasource.data_sources
            dashboard_chart.visualization
            dashboard_chart.visualization.button
            dashboard_chart.visualization.markdown
            dashboard_chart.drill_down_config Supported paths in query
            are - dashboard_query.query dashboard_query.input
        language_features (MutableSequence[google.cloud.chronicle_v1.types.LanguageFeature]):
            Optional. Language Features present in the
            query.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dashboard_query: gcc_dashboard_query.DashboardQuery = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcc_dashboard_query.DashboardQuery,
    )
    dashboard_chart: gcc_dashboard_chart.DashboardChart = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcc_dashboard_chart.DashboardChart,
    )
    edit_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=4,
        message=field_mask_pb2.FieldMask,
    )
    language_features: MutableSequence[gcc_dashboard_query.LanguageFeature] = (
        proto.RepeatedField(
            proto.ENUM,
            number=5,
            enum=gcc_dashboard_query.LanguageFeature,
        )
    )


class EditChartResponse(proto.Message):
    r"""Response message for editing chart in a dashboard.

    Attributes:
        native_dashboard (google.cloud.chronicle_v1.types.NativeDashboard):
            Edited dashboard.
        dashboard_chart (google.cloud.chronicle_v1.types.DashboardChart):
            Edited chart resource.
    """

    native_dashboard: "NativeDashboard" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="NativeDashboard",
    )
    dashboard_chart: gcc_dashboard_chart.DashboardChart = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcc_dashboard_chart.DashboardChart,
    )


class RemoveChartRequest(proto.Message):
    r"""Request message to remove chart from a dashboard.

    Attributes:
        name (str):
            Required. The dashboard name to remove chart
            from. Format:

            projects/{project}/locations/{location}/instances/{instance}/nativeDashboards/{dashboard}
        dashboard_chart (str):
            Required. The dashboard chart name to remove.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dashboard_chart: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DuplicateChartRequest(proto.Message):
    r"""Request message to duplicate chart in a dashboard.

    Attributes:
        name (str):
            Required. The dashboard name that involves
            chart duplication. Format:

            projects/{project}/locations/{location}/instances/{instance}/nativeDashboards/{dashboard}
        dashboard_chart (str):
            Required. The dashboard chart name to
            duplicate.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dashboard_chart: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DuplicateChartResponse(proto.Message):
    r"""Response message for duplicating chart in a dashboard.

    Attributes:
        native_dashboard (google.cloud.chronicle_v1.types.NativeDashboard):
            Dashboard with chart added in definition.
        dashboard_chart (google.cloud.chronicle_v1.types.DashboardChart):
            Duplicated chart resource.
    """

    native_dashboard: "NativeDashboard" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="NativeDashboard",
    )
    dashboard_chart: gcc_dashboard_chart.DashboardChart = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcc_dashboard_chart.DashboardChart,
    )


class DashboardUserData(proto.Message):
    r"""User Data for Native Dashboard

    Attributes:
        last_viewed_time (google.protobuf.timestamp_pb2.Timestamp):
            time when this dashboard is last viewed
        is_pinned (bool):
            is dashboard pinned by user
    """

    last_viewed_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    is_pinned: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class DashboardDefinition(proto.Message):
    r"""Definition of the dashboard including filters, layout,
    charts' configurations.

    Attributes:
        filters (MutableSequence[google.cloud.chronicle_v1.types.DashboardFilter]):
            Filters for the dashboard.
        fingerprint (str):
            Fingerprint of the dashboard definition.
        charts (MutableSequence[google.cloud.chronicle_v1.types.DashboardDefinition.ChartConfig]):
            Charts in the dashboard.
    """

    class ChartConfig(proto.Message):
        r"""Configuration of the chart including chart reference, layout
        and filters.

        Attributes:
            dashboard_chart (str):

            chart_layout (google.cloud.chronicle_v1.types.DashboardDefinition.ChartConfig.ChartLayout):

            filters_ids (MutableSequence[str]):
                Dashboard filters applied to the chart.
        """

        class ChartLayout(proto.Message):
            r"""Layout of the chart.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                start_x (int):

                    This field is a member of `oneof`_ ``_start_x``.
                span_x (int):

                start_y (int):

                    This field is a member of `oneof`_ ``_start_y``.
                span_y (int):

            """

            start_x: int = proto.Field(
                proto.INT32,
                number=9,
                optional=True,
            )
            span_x: int = proto.Field(
                proto.INT32,
                number=10,
            )
            start_y: int = proto.Field(
                proto.INT32,
                number=11,
                optional=True,
            )
            span_y: int = proto.Field(
                proto.INT32,
                number=12,
            )

        dashboard_chart: str = proto.Field(
            proto.STRING,
            number=1,
        )
        chart_layout: "DashboardDefinition.ChartConfig.ChartLayout" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="DashboardDefinition.ChartConfig.ChartLayout",
        )
        filters_ids: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=4,
        )

    filters: MutableSequence[gcc_dashboard_query.DashboardFilter] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcc_dashboard_query.DashboardFilter,
    )
    fingerprint: str = proto.Field(
        proto.STRING,
        number=2,
    )
    charts: MutableSequence[ChartConfig] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=ChartConfig,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
