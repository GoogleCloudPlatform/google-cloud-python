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

from google.cloud.chronicle_v1.types import featured_content_metadata
from google.cloud.chronicle_v1.types import native_dashboard as gcc_native_dashboard

__protobuf__ = proto.module(
    package="google.cloud.chronicle.v1",
    manifest={
        "FeaturedContentNativeDashboard",
        "GetFeaturedContentNativeDashboardRequest",
        "ListFeaturedContentNativeDashboardsRequest",
        "ListFeaturedContentNativeDashboardsResponse",
        "InstallFeaturedContentNativeDashboardRequest",
        "InstallFeaturedContentNativeDashboardResponse",
    },
)


class FeaturedContentNativeDashboard(proto.Message):
    r"""FeaturedContentNativeDashboard resource.

    Attributes:
        name (str):
            Identifier. The resource name of the
            FeaturedContentNativeDashboard. Format:
            projects/{project}/locations/{location}/instances/{instance}/contentHub/featuredContentNativeDashboards/{featured_content_native_dashboard}
        content_metadata (google.cloud.chronicle_v1.types.FeaturedContentMetadata):
            Output only. Metadata about the
            FeaturedContentNativeDashboard.
        dashboard_content (google.cloud.chronicle_v1.types.NativeDashboardWithChartsAndQueries):
            Optional. The dashboard content.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    content_metadata: featured_content_metadata.FeaturedContentMetadata = proto.Field(
        proto.MESSAGE,
        number=2,
        message=featured_content_metadata.FeaturedContentMetadata,
    )
    dashboard_content: gcc_native_dashboard.NativeDashboardWithChartsAndQueries = (
        proto.Field(
            proto.MESSAGE,
            number=3,
            message=gcc_native_dashboard.NativeDashboardWithChartsAndQueries,
        )
    )


class GetFeaturedContentNativeDashboardRequest(proto.Message):
    r"""Request message to get a FeaturedContentNativeDashboard.

    Attributes:
        name (str):
            Required. The resource name of the
            FeaturedContentNativeDashboard to retrieve. Format:
            projects/{project}/locations/{location}/instances/{instance}/contentHub/featuredContentNativeDashboards/{featured_content_native_dashboard}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListFeaturedContentNativeDashboardsRequest(proto.Message):
    r"""Request message to list FeaturedContentNativeDashboards.

    Attributes:
        parent (str):
            Required. The parent, which owns this
            collection of FeaturedContentNativeDashboards.
            Format:

            projects/{project}/locations/{location}/instances/{instance}/contentHub
        page_size (int):
            Optional. The maximum number of
            FeaturedContentNativeDashboards to return. The
            service may return fewer than this value. If
            unspecified, at most 100
            FeaturedContentNativeDashboards will be
            returned. The maximum value is 100; values above
            100 will be coerced to 100.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListFeaturedContentNativeDashboards`` call. Provide this
            to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListFeaturedContentNativeDashboards`` must match the call
            that provided the page token.
        filter (str):
            Optional. The filter to apply to list the
            FeaturedContentNativeDashboards.

            The filter syntax follows Google Cloud syntax:
            https://google.aip.dev/160.

            Supported fields for filtering:

            - ``name``: The resource name of the featured content.
            - ``content_metadata.description``: The description of the
              featured content.

            When a literal value is provided without a field, it will
            perform a substring search across both ``name`` and
            ``content_metadata.description``.

            Examples:

            - ``"test"``: Matches featured content where either the name
              or description contains "test" as a substring.
            - ``name="test"``: Matches featured content where the name
              contains "test".
            - ``content_metadata.description="test"``: Matches featured
              content where the description contains "test".
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


class ListFeaturedContentNativeDashboardsResponse(proto.Message):
    r"""Response message for listing FeaturedContentNativeDashboards.

    Attributes:
        featured_content_native_dashboards (MutableSequence[google.cloud.chronicle_v1.types.FeaturedContentNativeDashboard]):
            The list of FeaturedContentNativeDashboards.
            Ordered by name by default.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    featured_content_native_dashboards: MutableSequence[
        "FeaturedContentNativeDashboard"
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="FeaturedContentNativeDashboard",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class InstallFeaturedContentNativeDashboardRequest(proto.Message):
    r"""Request message to install a FeaturedContentNativeDashboard.

    Attributes:
        name (str):
            Required. The resource name of the
            FeaturedContentNativeDashboard to install. Format:
            projects/{project}/locations/{location}/instances/{instance}/contentHub/featuredContentNativeDashboards/{featured_content_native_dashboard}
        featured_content_native_dashboard (google.cloud.chronicle_v1.types.FeaturedContentNativeDashboard):
            Optional. The FeaturedContentNativeDashboard
            to install.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    featured_content_native_dashboard: "FeaturedContentNativeDashboard" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="FeaturedContentNativeDashboard",
    )


class InstallFeaturedContentNativeDashboardResponse(proto.Message):
    r"""Response message for installing a
    FeaturedContentNativeDashboard.

    Attributes:
        native_dashboard (str):
            Optional. The resource name of the NativeDashboard created.
            Format:
            projects/{project}/locations/{location}/instances/{instance}/nativeDashboards/{native_dashboard_id}
    """

    native_dashboard: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
