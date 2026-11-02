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

from google.ads.admanager_v1.types import content_bundle_enums

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "ContentBundle",
    },
)


class ContentBundle(proto.Message):
    r"""A [ContentBundle][google.ads.admanager.v1.ContentBundle] is a
    grouping of individual [Content][google.ads.admanager.v1.Content]. A
    [ContentBundle][google.ads.admanager.v1.ContentBundle] is defined as
    including the [Content][google.ads.admanager.v1.Content] that match
    certain filter rules along with the option to explicitly include or
    exclude certain Content IDs.

    Attributes:
        name (str):
            Identifier. The resource name of the
            [ContentBundle][google.ads.admanager.v1.ContentBundle].
            Format:
            ``networks/{network_code}/contentBundles/{content_bundle_id}``
        display_name (str):
            Required. The name of the
            [ContentBundle][google.ads.admanager.v1.ContentBundle]. This
            attribute is required and has a maximum length of 255
            characters.
        status (google.ads.admanager_v1.types.ContentBundleStatusEnum.ContentBundleStatus):
            Output only. The ContentBundleStatus of the
            [ContentBundle][google.ads.admanager.v1.ContentBundle]. This
            attribute is read-only and defaults to
            [ContentBundleStatusEnum.ContentBundleStatus.INACTIVE][google.ads.admanager.v1.ContentBundleStatusEnum.ContentBundleStatus.INACTIVE].
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the ``ContentBundle`` was last
            modified.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    status: content_bundle_enums.ContentBundleStatusEnum.ContentBundleStatus = (
        proto.Field(
            proto.ENUM,
            number=4,
            enum=content_bundle_enums.ContentBundleStatusEnum.ContentBundleStatus,
        )
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
