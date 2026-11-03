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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.ads.admanager_v1.types import content_enums

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "Content",
        "DaiIngestError",
        "CmsContent",
    },
)


class Content(proto.Message):
    r"""A piece of ``Content`` from a Publisher's CMS.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the ``Content``. Format:
            ``networks/{network_code}/content/{content_id}``
        display_name (str):
            Output only. The name of the ``Content``.

            This field is a member of `oneof`_ ``_display_name``.
        status (google.ads.admanager_v1.types.ContentStatusEnum.ContentStatus):
            Output only. The status of this ``Content``.

            This field is a member of `oneof`_ ``_status``.
        content_status_source (google.ads.admanager_v1.types.ContentStatusSourceEnum.ContentStatusSource):
            Output only. Whether the content status was defined by the
            user, or by the source CMS from which the ``Content`` was
            ingested.

            This field is a member of `oneof`_ ``_content_status_source``.
        hls_ingest_status (google.ads.admanager_v1.types.DaiIngestStatusEnum.DaiIngestStatus):
            Output only. The current DAI ingest status of the HLS media
            for the ``Content``. This attribute is unset if the
            ``Content`` is not eligible for dynamic ad insertion or if
            the ``Content`` does not have HLS media.

            This field is a member of `oneof`_ ``_hls_ingest_status``.
        hls_ingest_errors (MutableSequence[google.ads.admanager_v1.types.DaiIngestError]):
            Output only. The list of any errors that occurred during the
            most recent DAI ingestion process of the HLS media. This
            attribute will be empty if the
            [hlsIngestStatus][google.ads.admanager.v1.Content.hls_ingest_status]
            is
            [DaiIngestStatusEnum.DaiIngestStatus.SUCCESS][google.ads.admanager.v1.DaiIngestStatusEnum.DaiIngestStatus.SUCCESS]
            or if the ``Content`` is not eligible for dynamic ad
            insertion or if the ``Content`` does not have HLS media.
        last_hls_ingest_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp at which this ``Content``'s HLS
            media was last ingested for DAI. This attribute will be
            unset if the ``Content`` is not eligible for dynamic ad
            insertion or if the ``Content`` does not have HLS media.

            This field is a member of `oneof`_ ``_last_hls_ingest_time``.
        dash_ingest_status (google.ads.admanager_v1.types.DaiIngestStatusEnum.DaiIngestStatus):
            Output only. The current DAI ingest status of the DASH media
            for the ``Content``. This attribute is unset if the
            ``Content`` is not eligible for dynamic ad insertion or if
            the ``Content`` does not have DASH media.

            This field is a member of `oneof`_ ``_dash_ingest_status``.
        dash_ingest_errors (MutableSequence[google.ads.admanager_v1.types.DaiIngestError]):
            Output only. The list of any errors that occurred during the
            most recent DAI ingestion process of the DASH media. This
            attribute will be empty if the
            [dashIngestStatus][google.ads.admanager.v1.Content.dash_ingest_status]
            is
            [DaiIngestStatusEnum.DaiIngestStatus.SUCCESS][google.ads.admanager.v1.DaiIngestStatusEnum.DaiIngestStatus.SUCCESS]
            or if the ``Content`` is not eligible for dynamic ad
            insertion or if the ``Content`` does not have DASH media.
        last_dash_ingest_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp at which this ``Content``'s DASH
            media was last ingested for DAI. This attribute will be
            unset if the ``Content`` is not eligible for dynamic ad
            insertion or if the ``Content`` does not have DASH media.

            This field is a member of `oneof`_ ``_last_dash_ingest_time``.
        import_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp at which this ``Content`` was
            published.

            This field is a member of `oneof`_ ``_import_time``.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp at which this ``Content`` was
            last modified. The last modified date time will always be
            updated when a
            [ContentBundle][google.ads.admanager.v1.ContentBundle]
            association is changed, but will not always be updated when
            a
            [CmsMetadataValue][google.ads.admanager.v1.CmsMetadataValue]
            value is changed.

            This field is a member of `oneof`_ ``_update_time``.
        cms_sources (MutableSequence[google.ads.admanager_v1.types.CmsContent]):
            Output only. Information about the ``Content`` from the CMS
            it was ingested from.
        content_bundles (MutableSequence[str]):
            Output only. The resource names of the
            [ContentBundles][google.ads.admanager.v1.ContentBundle] of
            which this ``Content`` is a member.
        cms_metadata_values (MutableSequence[str]):
            Output only. The resource names of the [CmsMetadataValues]
            [google.ads.admanager.v1.CmsMetadataValue] that are
            associated with this ``Content``.
        duration (google.protobuf.duration_pb2.Duration):
            Output only. The duration of the ``Content``.

            This field is a member of `oneof`_ ``_duration``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    status: content_enums.ContentStatusEnum.ContentStatus = proto.Field(
        proto.ENUM,
        number=3,
        optional=True,
        enum=content_enums.ContentStatusEnum.ContentStatus,
    )
    content_status_source: content_enums.ContentStatusSourceEnum.ContentStatusSource = (
        proto.Field(
            proto.ENUM,
            number=4,
            optional=True,
            enum=content_enums.ContentStatusSourceEnum.ContentStatusSource,
        )
    )
    hls_ingest_status: content_enums.DaiIngestStatusEnum.DaiIngestStatus = proto.Field(
        proto.ENUM,
        number=5,
        optional=True,
        enum=content_enums.DaiIngestStatusEnum.DaiIngestStatus,
    )
    hls_ingest_errors: MutableSequence["DaiIngestError"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="DaiIngestError",
    )
    last_hls_ingest_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    dash_ingest_status: content_enums.DaiIngestStatusEnum.DaiIngestStatus = proto.Field(
        proto.ENUM,
        number=8,
        optional=True,
        enum=content_enums.DaiIngestStatusEnum.DaiIngestStatus,
    )
    dash_ingest_errors: MutableSequence["DaiIngestError"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="DaiIngestError",
    )
    last_dash_ingest_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    import_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    cms_sources: MutableSequence["CmsContent"] = proto.RepeatedField(
        proto.MESSAGE,
        number=13,
        message="CmsContent",
    )
    content_bundles: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=14,
    )
    cms_metadata_values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=15,
    )
    duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=16,
        optional=True,
        message=duration_pb2.Duration,
    )


class DaiIngestError(proto.Message):
    r"""Represents an error associated with a Dynamic Ad Insertion (DAI)
    ``Content``'s status.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        reason (google.ads.admanager_v1.types.DaiIngestErrorReasonEnum.DaiIngestErrorReason):
            The error associated with the content.

            This field is a member of `oneof`_ ``_reason``.
        trigger (str):
            Output only. The field, if any, that
            triggered the error.

            This field is a member of `oneof`_ ``_trigger``.
    """

    reason: content_enums.DaiIngestErrorReasonEnum.DaiIngestErrorReason = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum=content_enums.DaiIngestErrorReasonEnum.DaiIngestErrorReason,
    )
    trigger: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )


class CmsContent(proto.Message):
    r"""Contains information about the ``Content`` from the CMS it was
    ingested from.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        content_source (str):
            Output only. The resource name of the
            [ContentSource][google.ads.admanager.v1.ContentSource] this
            content was ingested from.

            This field is a member of `oneof`_ ``_content_source``.
        content_source_display_name (str):
            Output only. The display name of the
            [ContentSource][google.ads.admanager.v1.ContentSource] this
            content was ingested from.

            This field is a member of `oneof`_ ``_content_source_display_name``.
        cms_content_id (str):
            The ID of the ``Content`` in the CMS. This ID will be a 3rd
            party ID, usually the ID of the content in a CMS (Content
            Management System).

            This field is a member of `oneof`_ ``_cms_content_id``.
    """

    content_source: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    content_source_display_name: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    cms_content_id: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
