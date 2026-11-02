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

from google.cloud.asset_v1p5beta1.types import assets as gca_assets

__protobuf__ = proto.module(
    package="google.cloud.asset.v1p5beta1",
    manifest={
        "ContentType",
        "ListAssetsRequest",
        "ListAssetsResponse",
    },
)


class ContentType(proto.Enum):
    r"""Asset content type.

    Values:
        CONTENT_TYPE_UNSPECIFIED (0):
            Unspecified content type.
        RESOURCE (1):
            Resource metadata.
        IAM_POLICY (2):
            The actual IAM policy set on a resource.
        ORG_POLICY (4):
            The organization policy set on an asset.
        ACCESS_POLICY (5):
            The Access Context Manager policy set on an
            asset.
    """

    CONTENT_TYPE_UNSPECIFIED = 0
    RESOURCE = 1
    IAM_POLICY = 2
    ORG_POLICY = 4
    ACCESS_POLICY = 5


class ListAssetsRequest(proto.Message):
    r"""ListAssets request.

    Attributes:
        parent (str):
            Required. Name of the organization or project the assets
            belong to. Format: "organizations/[organization-number]"
            (such as "organizations/123"), "projects/[project-id]" (such
            as "projects/my-project-id"), or "projects/[project-number]"
            (such as "projects/12345").
        read_time (google.protobuf.timestamp_pb2.Timestamp):
            Timestamp to take an asset snapshot. This can
            only be set to a timestamp between the current
            time and the current time minus 35 days
            (inclusive). If not specified, the current time
            will be used. Due to delays in resource data
            collection and indexing, there is a volatile
            window during which running the same query may
            get different results.
        asset_types (MutableSequence[str]):
            A list of asset types to take a snapshot for. For example:
            "compute.googleapis.com/Disk".

            Regular expression is also supported. For example:

            - "compute.googleapis.com.\*" snapshots resources whose
              asset type starts with "compute.googleapis.com".
            - ".*Instance" snapshots resources whose asset type ends
              with "Instance".
            - ".\ *Instance.*" snapshots resources whose asset type
              contains "Instance".

            See `RE2 <https://github.com/google/re2/wiki/Syntax>`__ for
            all supported regular expression syntax. If the regular
            expression does not match any supported asset type, an
            INVALID_ARGUMENT error will be returned.

            If specified, only matching assets will be returned,
            otherwise, it will snapshot all asset types. See
            `Introduction to Cloud Asset
            Inventory <https://cloud.google.com/asset-inventory/docs/overview>`__
            for all supported asset types.
        content_type (google.cloud.asset_v1p5beta1.types.ContentType):
            Asset content type. If not specified, no
            content but the asset name will be returned.
        page_size (int):
            The maximum number of assets to be returned
            in a single response. Default is 100, minimum is
            1, and maximum is 1000.
        page_token (str):
            The ``next_page_token`` returned from the previous
            ``ListAssetsResponse``, or unspecified for the first
            ``ListAssetsRequest``. It is a continuation of a prior
            ``ListAssets`` call, and the API should return the next page
            of assets.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    read_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    asset_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    content_type: "ContentType" = proto.Field(
        proto.ENUM,
        number=4,
        enum="ContentType",
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=5,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=6,
    )


class ListAssetsResponse(proto.Message):
    r"""ListAssets response.

    Attributes:
        read_time (google.protobuf.timestamp_pb2.Timestamp):
            Time the snapshot was taken.
        assets (MutableSequence[google.cloud.asset_v1p5beta1.types.Asset]):
            Assets.
        next_page_token (str):
            Token to retrieve the next page of results.
            It expires 72 hours after the page token for the
            first page is generated. Set to empty if there
            are no remaining results.
    """

    @property
    def raw_page(self):
        return self

    read_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    assets: MutableSequence[gca_assets.Asset] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=gca_assets.Asset,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
