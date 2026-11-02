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

from google.cloud.websecurityscanner_v1beta.types import crawled_url, finding, scan_run
from google.cloud.websecurityscanner_v1beta.types import (
    finding_type_stats as gcw_finding_type_stats,
)
from google.cloud.websecurityscanner_v1beta.types import scan_config as gcw_scan_config

__protobuf__ = proto.module(
    package="google.cloud.websecurityscanner.v1beta",
    manifest={
        "CreateScanConfigRequest",
        "DeleteScanConfigRequest",
        "GetScanConfigRequest",
        "ListScanConfigsRequest",
        "UpdateScanConfigRequest",
        "ListScanConfigsResponse",
        "StartScanRunRequest",
        "GetScanRunRequest",
        "ListScanRunsRequest",
        "ListScanRunsResponse",
        "StopScanRunRequest",
        "ListCrawledUrlsRequest",
        "ListCrawledUrlsResponse",
        "GetFindingRequest",
        "ListFindingsRequest",
        "ListFindingsResponse",
        "ListFindingTypeStatsRequest",
        "ListFindingTypeStatsResponse",
    },
)


class CreateScanConfigRequest(proto.Message):
    r"""Request for the ``CreateScanConfig`` method.

    Attributes:
        parent (str):
            Required. The parent resource name where the
            scan is created, which should be a project
            resource name in the format
            'projects/{projectId}'.
        scan_config (google.cloud.websecurityscanner_v1beta.types.ScanConfig):
            Required. The ScanConfig to be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    scan_config: gcw_scan_config.ScanConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcw_scan_config.ScanConfig,
    )


class DeleteScanConfigRequest(proto.Message):
    r"""Request for the ``DeleteScanConfig`` method.

    Attributes:
        name (str):
            Required. The resource name of the ScanConfig
            to be deleted. The name follows the format of
            'projects/{projectId}/scanConfigs/{scanConfigId}'.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetScanConfigRequest(proto.Message):
    r"""Request for the ``GetScanConfig`` method.

    Attributes:
        name (str):
            Required. The resource name of the ScanConfig
            to be returned. The name follows the format of
            'projects/{projectId}/scanConfigs/{scanConfigId}'.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListScanConfigsRequest(proto.Message):
    r"""Request for the ``ListScanConfigs`` method.

    Attributes:
        parent (str):
            Required. The parent resource name, which
            should be a project resource name in the format
            'projects/{projectId}'.
        page_token (str):
            A token identifying a page of results to be returned. This
            should be a ``next_page_token`` value returned from a
            previous List request. If unspecified, the first page of
            results is returned.
        page_size (int):
            The maximum number of ScanConfigs to return,
            can be limited by server. If not specified or
            not positive, the implementation will select a
            reasonable value.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class UpdateScanConfigRequest(proto.Message):
    r"""Request for the ``UpdateScanConfigRequest`` method.

    Attributes:
        scan_config (google.cloud.websecurityscanner_v1beta.types.ScanConfig):
            Required. The ScanConfig to be updated. The
            name field must be set to identify the resource
            to be updated. The values of fields not covered
            by the mask will be ignored.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The update mask applies to the resource. For the
            ``FieldMask`` definition, see
            https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask
    """

    scan_config: gcw_scan_config.ScanConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcw_scan_config.ScanConfig,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=3,
        message=field_mask_pb2.FieldMask,
    )


class ListScanConfigsResponse(proto.Message):
    r"""Response for the ``ListScanConfigs`` method.

    Attributes:
        scan_configs (MutableSequence[google.cloud.websecurityscanner_v1beta.types.ScanConfig]):
            The list of ScanConfigs returned.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    scan_configs: MutableSequence[gcw_scan_config.ScanConfig] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcw_scan_config.ScanConfig,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class StartScanRunRequest(proto.Message):
    r"""Request for the ``StartScanRun`` method.

    Attributes:
        name (str):
            Required. The resource name of the ScanConfig
            to be used. The name follows the format of
            'projects/{projectId}/scanConfigs/{scanConfigId}'.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetScanRunRequest(proto.Message):
    r"""Request for the ``GetScanRun`` method.

    Attributes:
        name (str):
            Required. The resource name of the ScanRun to
            be returned. The name follows the format of
            'projects/{projectId}/scanConfigs/{scanConfigId}/scanRuns/{scanRunId}'.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListScanRunsRequest(proto.Message):
    r"""Request for the ``ListScanRuns`` method.

    Attributes:
        parent (str):
            Required. The parent resource name, which
            should be a scan resource name in the format
            'projects/{projectId}/scanConfigs/{scanConfigId}'.
        page_token (str):
            A token identifying a page of results to be returned. This
            should be a ``next_page_token`` value returned from a
            previous List request. If unspecified, the first page of
            results is returned.
        page_size (int):
            The maximum number of ScanRuns to return, can
            be limited by server. If not specified or not
            positive, the implementation will select a
            reasonable value.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class ListScanRunsResponse(proto.Message):
    r"""Response for the ``ListScanRuns`` method.

    Attributes:
        scan_runs (MutableSequence[google.cloud.websecurityscanner_v1beta.types.ScanRun]):
            The list of ScanRuns returned.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    scan_runs: MutableSequence[scan_run.ScanRun] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=scan_run.ScanRun,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class StopScanRunRequest(proto.Message):
    r"""Request for the ``StopScanRun`` method.

    Attributes:
        name (str):
            Required. The resource name of the ScanRun to
            be stopped. The name follows the format of
            'projects/{projectId}/scanConfigs/{scanConfigId}/scanRuns/{scanRunId}'.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListCrawledUrlsRequest(proto.Message):
    r"""Request for the ``ListCrawledUrls`` method.

    Attributes:
        parent (str):
            Required. The parent resource name, which
            should be a scan run resource name in the format
            'projects/{projectId}/scanConfigs/{scanConfigId}/scanRuns/{scanRunId}'.
        page_token (str):
            A token identifying a page of results to be returned. This
            should be a ``next_page_token`` value returned from a
            previous List request. If unspecified, the first page of
            results is returned.
        page_size (int):
            The maximum number of CrawledUrls to return,
            can be limited by server. If not specified or
            not positive, the implementation will select a
            reasonable value.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class ListCrawledUrlsResponse(proto.Message):
    r"""Response for the ``ListCrawledUrls`` method.

    Attributes:
        crawled_urls (MutableSequence[google.cloud.websecurityscanner_v1beta.types.CrawledUrl]):
            The list of CrawledUrls returned.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    crawled_urls: MutableSequence[crawled_url.CrawledUrl] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=crawled_url.CrawledUrl,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetFindingRequest(proto.Message):
    r"""Request for the ``GetFinding`` method.

    Attributes:
        name (str):
            Required. The resource name of the Finding to
            be returned. The name follows the format of
            'projects/{projectId}/scanConfigs/{scanConfigId}/scanRuns/{scanRunId}/findings/{findingId}'.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListFindingsRequest(proto.Message):
    r"""Request for the ``ListFindings`` method.

    Attributes:
        parent (str):
            Required. The parent resource name, which
            should be a scan run resource name in the format
            'projects/{projectId}/scanConfigs/{scanConfigId}/scanRuns/{scanRunId}'.
        filter (str):
            Required. The filter expression. The expression must be in
            the format: . Supported field: 'finding_type'. Supported
            operator: '='.
        page_token (str):
            A token identifying a page of results to be returned. This
            should be a ``next_page_token`` value returned from a
            previous List request. If unspecified, the first page of
            results is returned.
        page_size (int):
            The maximum number of Findings to return, can
            be limited by server. If not specified or not
            positive, the implementation will select a
            reasonable value.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )


class ListFindingsResponse(proto.Message):
    r"""Response for the ``ListFindings`` method.

    Attributes:
        findings (MutableSequence[google.cloud.websecurityscanner_v1beta.types.Finding]):
            The list of Findings returned.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    findings: MutableSequence[finding.Finding] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=finding.Finding,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListFindingTypeStatsRequest(proto.Message):
    r"""Request for the ``ListFindingTypeStats`` method.

    Attributes:
        parent (str):
            Required. The parent resource name, which
            should be a scan run resource name in the format
            'projects/{projectId}/scanConfigs/{scanConfigId}/scanRuns/{scanRunId}'.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListFindingTypeStatsResponse(proto.Message):
    r"""Response for the ``ListFindingTypeStats`` method.

    Attributes:
        finding_type_stats (MutableSequence[google.cloud.websecurityscanner_v1beta.types.FindingTypeStats]):
            The list of FindingTypeStats returned.
    """

    finding_type_stats: MutableSequence[gcw_finding_type_stats.FindingTypeStats] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=gcw_finding_type_stats.FindingTypeStats,
        )
    )


__all__ = tuple(sorted(__protobuf__.manifest))
