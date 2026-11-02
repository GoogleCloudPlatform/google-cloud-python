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

from google.cloud.monitoring_dashboard_v1.types import dashboard as gmd_dashboard

__protobuf__ = proto.module(
    package="google.monitoring.dashboard.v1",
    manifest={
        "CreateDashboardRequest",
        "ListDashboardsRequest",
        "ListDashboardsResponse",
        "GetDashboardRequest",
        "DeleteDashboardRequest",
        "UpdateDashboardRequest",
    },
)


class CreateDashboardRequest(proto.Message):
    r"""The ``CreateDashboard`` request.

    Attributes:
        parent (str):
            Required. The project on which to execute the request. The
            format is:

            ::

                projects/[PROJECT_ID_OR_NUMBER]

            The ``[PROJECT_ID_OR_NUMBER]`` must match the dashboard
            resource name.
        dashboard (google.cloud.monitoring_dashboard_v1.types.Dashboard):
            Required. The initial dashboard
            specification.
        validate_only (bool):
            If set, validate the request and preview the
            review, but do not actually save it.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dashboard: gmd_dashboard.Dashboard = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gmd_dashboard.Dashboard,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class ListDashboardsRequest(proto.Message):
    r"""The ``ListDashboards`` request.

    Attributes:
        parent (str):
            Required. The scope of the dashboards to list. The format
            is:

            ::

                projects/[PROJECT_ID_OR_NUMBER]
        page_size (int):
            A positive number that is the maximum number
            of results to return. If unspecified, a default
            of 1000 is used.
        page_token (str):
            Optional. If this field is not empty then it must contain
            the ``nextPageToken`` value returned by a previous call to
            this method. Using this field causes the method to return
            additional results from the previous method call.
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


class ListDashboardsResponse(proto.Message):
    r"""The ``ListDashboards`` request.

    Attributes:
        dashboards (MutableSequence[google.cloud.monitoring_dashboard_v1.types.Dashboard]):
            The list of requested dashboards.
        next_page_token (str):
            If there are more results than have been returned, then this
            field is set to a non-empty value. To see the additional
            results, use that value as ``page_token`` in the next call
            to this method.
    """

    @property
    def raw_page(self):
        return self

    dashboards: MutableSequence[gmd_dashboard.Dashboard] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gmd_dashboard.Dashboard,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetDashboardRequest(proto.Message):
    r"""The ``GetDashboard`` request.

    Attributes:
        name (str):
            Required. The resource name of the Dashboard. The format is
            one of:

            - ``dashboards/[DASHBOARD_ID]`` (for system dashboards)
            - ``projects/[PROJECT_ID_OR_NUMBER]/dashboards/[DASHBOARD_ID]``
              (for custom dashboards).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteDashboardRequest(proto.Message):
    r"""The ``DeleteDashboard`` request.

    Attributes:
        name (str):
            Required. The resource name of the Dashboard. The format is:

            ::

                projects/[PROJECT_ID_OR_NUMBER]/dashboards/[DASHBOARD_ID]
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateDashboardRequest(proto.Message):
    r"""The ``UpdateDashboard`` request.

    Attributes:
        dashboard (google.cloud.monitoring_dashboard_v1.types.Dashboard):
            Required. The dashboard that will replace the
            existing dashboard.
        validate_only (bool):
            If set, validate the request and preview the
            review, but do not actually save it.
    """

    dashboard: gmd_dashboard.Dashboard = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gmd_dashboard.Dashboard,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
