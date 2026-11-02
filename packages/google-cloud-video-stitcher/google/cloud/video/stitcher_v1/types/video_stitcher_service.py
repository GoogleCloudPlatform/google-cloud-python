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
import proto  # type: ignore

from google.cloud.video.stitcher_v1.types import (
    ad_tag_details,
    sessions,
    stitch_details,
)
from google.cloud.video.stitcher_v1.types import cdn_keys as gcvs_cdn_keys
from google.cloud.video.stitcher_v1.types import live_configs as gcvs_live_configs
from google.cloud.video.stitcher_v1.types import slates as gcvs_slates
from google.cloud.video.stitcher_v1.types import vod_configs as gcvs_vod_configs

__protobuf__ = proto.module(
    package="google.cloud.video.stitcher.v1",
    manifest={
        "CreateCdnKeyRequest",
        "ListCdnKeysRequest",
        "ListCdnKeysResponse",
        "GetCdnKeyRequest",
        "DeleteCdnKeyRequest",
        "UpdateCdnKeyRequest",
        "CreateVodSessionRequest",
        "GetVodSessionRequest",
        "ListVodStitchDetailsRequest",
        "ListVodStitchDetailsResponse",
        "GetVodStitchDetailRequest",
        "ListVodAdTagDetailsRequest",
        "ListVodAdTagDetailsResponse",
        "GetVodAdTagDetailRequest",
        "ListLiveAdTagDetailsRequest",
        "ListLiveAdTagDetailsResponse",
        "GetLiveAdTagDetailRequest",
        "CreateSlateRequest",
        "GetSlateRequest",
        "ListSlatesRequest",
        "ListSlatesResponse",
        "UpdateSlateRequest",
        "DeleteSlateRequest",
        "CreateLiveSessionRequest",
        "GetLiveSessionRequest",
        "CreateLiveConfigRequest",
        "ListLiveConfigsRequest",
        "ListLiveConfigsResponse",
        "GetLiveConfigRequest",
        "DeleteLiveConfigRequest",
        "UpdateLiveConfigRequest",
        "CreateVodConfigRequest",
        "ListVodConfigsRequest",
        "ListVodConfigsResponse",
        "GetVodConfigRequest",
        "DeleteVodConfigRequest",
        "UpdateVodConfigRequest",
        "OperationMetadata",
    },
)


class CreateCdnKeyRequest(proto.Message):
    r"""Request message for VideoStitcherService.createCdnKey.

    Attributes:
        parent (str):
            Required. The project in which the CDN key should be
            created, in the form of
            ``projects/{project_number}/locations/{location}``.
        cdn_key (google.cloud.video.stitcher_v1.types.CdnKey):
            Required. The CDN key resource to create.
        cdn_key_id (str):
            Required. The ID to use for the CDN key,
            which will become the final component of the CDN
            key's resource name.

            This value should conform to RFC-1034, which
            restricts to lower-case letters, numbers, and
            hyphen, with the first character a letter, the
            last a letter or a number, and a 63 character
            maximum.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cdn_key: gcvs_cdn_keys.CdnKey = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcvs_cdn_keys.CdnKey,
    )
    cdn_key_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListCdnKeysRequest(proto.Message):
    r"""Request message for VideoStitcherService.listCdnKeys.

    Attributes:
        parent (str):
            Required. The project that contains the list of CDN keys, in
            the form of
            ``projects/{project_number}/locations/{location}``.
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Filtering results
        order_by (str):
            Hint for how to order the results
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
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListCdnKeysResponse(proto.Message):
    r"""Response message for VideoStitcher.ListCdnKeys.

    Attributes:
        cdn_keys (MutableSequence[google.cloud.video.stitcher_v1.types.CdnKey]):
            List of CDN keys.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    cdn_keys: MutableSequence[gcvs_cdn_keys.CdnKey] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcvs_cdn_keys.CdnKey,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetCdnKeyRequest(proto.Message):
    r"""Request message for VideoStitcherService.getCdnKey.

    Attributes:
        name (str):
            Required. The name of the CDN key to be retrieved, in the
            form of
            ``projects/{project}/locations/{location}/cdnKeys/{id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteCdnKeyRequest(proto.Message):
    r"""Request message for VideoStitcherService.deleteCdnKey.

    Attributes:
        name (str):
            Required. The name of the CDN key to be deleted, in the form
            of
            ``projects/{project_number}/locations/{location}/cdnKeys/{id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateCdnKeyRequest(proto.Message):
    r"""Request message for VideoStitcherService.updateCdnKey.

    Attributes:
        cdn_key (google.cloud.video.stitcher_v1.types.CdnKey):
            Required. The CDN key resource which replaces
            the resource on the server.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The update mask applies to the resource. For the
            ``FieldMask`` definition, see
            https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask
    """

    cdn_key: gcvs_cdn_keys.CdnKey = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcvs_cdn_keys.CdnKey,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class CreateVodSessionRequest(proto.Message):
    r"""Request message for VideoStitcherService.createVodSession

    Attributes:
        parent (str):
            Required. The project and location in which the VOD session
            should be created, in the form of
            ``projects/{project_number}/locations/{location}``.
        vod_session (google.cloud.video.stitcher_v1.types.VodSession):
            Required. Parameters for creating a session.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    vod_session: sessions.VodSession = proto.Field(
        proto.MESSAGE,
        number=2,
        message=sessions.VodSession,
    )


class GetVodSessionRequest(proto.Message):
    r"""Request message for VideoStitcherService.getVodSession

    Attributes:
        name (str):
            Required. The name of the VOD session to be retrieved, in
            the form of
            ``projects/{project_number}/locations/{location}/vodSessions/{id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListVodStitchDetailsRequest(proto.Message):
    r"""Request message for
    VideoStitcherService.listVodStitchDetails.

    Attributes:
        parent (str):
            Required. The VOD session where the stitch details belong
            to, in the form of
            ``projects/{project}/locations/{location}/vodSessions/{id}``.
        page_size (int):
            The maximum number of items to return.
        page_token (str):
            The next_page_token value returned from a previous List
            request, if any.
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


class ListVodStitchDetailsResponse(proto.Message):
    r"""Response message for
    VideoStitcherService.listVodStitchDetails.

    Attributes:
        vod_stitch_details (MutableSequence[google.cloud.video.stitcher_v1.types.VodStitchDetail]):
            A List of stitch Details.
        next_page_token (str):
            The pagination token.
    """

    @property
    def raw_page(self):
        return self

    vod_stitch_details: MutableSequence[stitch_details.VodStitchDetail] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=stitch_details.VodStitchDetail,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetVodStitchDetailRequest(proto.Message):
    r"""Request message for VideoStitcherService.getVodStitchDetail.

    Attributes:
        name (str):
            Required. The name of the stitch detail in the specified VOD
            session, in the form of
            ``projects/{project}/locations/{location}/vodSessions/{vod_session_id}/vodStitchDetails/{id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListVodAdTagDetailsRequest(proto.Message):
    r"""Request message for VideoStitcherService.listVodAdTagDetails.

    Attributes:
        parent (str):
            Required. The VOD session which the ad tag details belong
            to, in the form of
            ``projects/{project}/locations/{location}/vodSessions/{vod_session_id}``.
        page_size (int):
            The maximum number of items to return.
        page_token (str):
            The next_page_token value returned from a previous List
            request, if any.
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


class ListVodAdTagDetailsResponse(proto.Message):
    r"""Response message for
    VideoStitcherService.listVodAdTagDetails.

    Attributes:
        vod_ad_tag_details (MutableSequence[google.cloud.video.stitcher_v1.types.VodAdTagDetail]):
            A List of ad tag details.
        next_page_token (str):
            The pagination token.
    """

    @property
    def raw_page(self):
        return self

    vod_ad_tag_details: MutableSequence[ad_tag_details.VodAdTagDetail] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=ad_tag_details.VodAdTagDetail,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetVodAdTagDetailRequest(proto.Message):
    r"""Request message for VideoStitcherService.getVodAdTagDetail

    Attributes:
        name (str):
            Required. The name of the ad tag detail for the specified
            VOD session, in the form of
            ``projects/{project}/locations/{location}/vodSessions/{vod_session_id}/vodAdTagDetails/{vod_ad_tag_detail}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListLiveAdTagDetailsRequest(proto.Message):
    r"""Request message for
    VideoStitcherService.listLiveAdTagDetails.

    Attributes:
        parent (str):
            Required. The resource parent in the form of
            ``projects/{project}/locations/{location}/liveSessions/{live_session}``.
        page_size (int):
            The maximum number of items to return.
        page_token (str):
            The pagination token returned from a previous
            List request.
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


class ListLiveAdTagDetailsResponse(proto.Message):
    r"""Response message for
    VideoStitcherService.listLiveAdTagDetails.

    Attributes:
        live_ad_tag_details (MutableSequence[google.cloud.video.stitcher_v1.types.LiveAdTagDetail]):
            A list of live session ad tag details.
        next_page_token (str):
            The pagination token.
    """

    @property
    def raw_page(self):
        return self

    live_ad_tag_details: MutableSequence[ad_tag_details.LiveAdTagDetail] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=ad_tag_details.LiveAdTagDetail,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetLiveAdTagDetailRequest(proto.Message):
    r"""Request message for VideoStitcherService.getLiveAdTagDetail

    Attributes:
        name (str):
            Required. The resource name in the form of
            ``projects/{project}/locations/{location}/liveSessions/{live_session}/liveAdTagDetails/{live_ad_tag_detail}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateSlateRequest(proto.Message):
    r"""Request message for VideoStitcherService.createSlate.

    Attributes:
        parent (str):
            Required. The project in which the slate should be created,
            in the form of
            ``projects/{project_number}/locations/{location}``.
        slate_id (str):
            Required. The unique identifier for the
            slate. This value should conform to RFC-1034,
            which restricts to lower-case letters, numbers,
            and hyphen, with the first character a letter,
            the last a letter or a number, and a 63
            character maximum.
        slate (google.cloud.video.stitcher_v1.types.Slate):
            Required. The slate to create.
        request_id (str):
            A request ID to identify requests. Specify a unique request
            ID so that if you must retry your request, the server will
            know to ignore the request if it has already been completed.
            The server will guarantee that for at least 60 minutes since
            the first request.

            For example, consider a situation where you make an initial
            request and the request times out. If you make the request
            again with the same request ID, the server can check if
            original operation with the same request ID was received,
            and if so, will ignore the second request. This prevents
            clients from accidentally creating duplicate commitments.

            The request ID must be a valid UUID with the exception that
            zero UUID is not supported
            ``(00000000-0000-0000-0000-000000000000)``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    slate_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    slate: gcvs_slates.Slate = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcvs_slates.Slate,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class GetSlateRequest(proto.Message):
    r"""Request message for VideoStitcherService.getSlate.

    Attributes:
        name (str):
            Required. The name of the slate to be retrieved, of the
            slate, in the form of
            ``projects/{project_number}/locations/{location}/slates/{id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListSlatesRequest(proto.Message):
    r"""Request message for VideoStitcherService.listSlates.

    Attributes:
        parent (str):
            Required. The project to list slates, in the form of
            ``projects/{project_number}/locations/{location}``.
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Filtering results
        order_by (str):
            Hint for how to order the results
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
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListSlatesResponse(proto.Message):
    r"""Response message for VideoStitcherService.listSlates.

    Attributes:
        slates (MutableSequence[google.cloud.video.stitcher_v1.types.Slate]):
            The list of slates
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    slates: MutableSequence[gcvs_slates.Slate] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcvs_slates.Slate,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class UpdateSlateRequest(proto.Message):
    r"""Request message for VideoStitcherService.updateSlate.

    Attributes:
        slate (google.cloud.video.stitcher_v1.types.Slate):
            Required. The resource with updated fields.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The update mask which specifies
            fields which should be updated.
    """

    slate: gcvs_slates.Slate = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcvs_slates.Slate,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteSlateRequest(proto.Message):
    r"""Request message for VideoStitcherService.deleteSlate.

    Attributes:
        name (str):
            Required. The name of the slate to be deleted, in the form
            of
            ``projects/{project_number}/locations/{location}/slates/{id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateLiveSessionRequest(proto.Message):
    r"""Request message for VideoStitcherService.createLiveSession.

    Attributes:
        parent (str):
            Required. The project and location in which the live session
            should be created, in the form of
            ``projects/{project_number}/locations/{location}``.
        live_session (google.cloud.video.stitcher_v1.types.LiveSession):
            Required. Parameters for creating a live
            session.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    live_session: sessions.LiveSession = proto.Field(
        proto.MESSAGE,
        number=2,
        message=sessions.LiveSession,
    )


class GetLiveSessionRequest(proto.Message):
    r"""Request message for VideoStitcherService.getSession.

    Attributes:
        name (str):
            Required. The name of the live session, in the form of
            ``projects/{project_number}/locations/{location}/liveSessions/{id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateLiveConfigRequest(proto.Message):
    r"""Request message for VideoStitcherService.createLiveConfig

    Attributes:
        parent (str):
            Required. The project in which the live config should be
            created, in the form of
            ``projects/{project_number}/locations/{location}``.
        live_config_id (str):
            Required. The unique identifier ID to use for
            the live config.
        live_config (google.cloud.video.stitcher_v1.types.LiveConfig):
            Required. The live config resource to create.
        request_id (str):
            A request ID to identify requests. Specify a unique request
            ID so that if you must retry your request, the server will
            know to ignore the request if it has already been completed.
            The server will guarantee that for at least 60 minutes since
            the first request.

            For example, consider a situation where you make an initial
            request and the request times out. If you make the request
            again with the same request ID, the server can check if
            original operation with the same request ID was received,
            and if so, will ignore the second request. This prevents
            clients from accidentally creating duplicate commitments.

            The request ID must be a valid UUID with the exception that
            zero UUID is not supported
            ``(00000000-0000-0000-0000-000000000000)``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    live_config_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    live_config: gcvs_live_configs.LiveConfig = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcvs_live_configs.LiveConfig,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListLiveConfigsRequest(proto.Message):
    r"""Request message for VideoStitcherService.listLiveConfig.

    Attributes:
        parent (str):
            Required. The project that contains the list of live
            configs, in the form of
            ``projects/{project_number}/locations/{location}``.
        page_size (int):
            The maximum number of items to return.
        page_token (str):
            The next_page_token value returned from a previous List
            request, if any.
        filter (str):
            Optional. The filter to apply to list results (see
            `Filtering <https://google.aip.dev/160>`__).
        order_by (str):
            Optional. Specifies the ordering of results following `Cloud
            API
            syntax <https://cloud.google.com/apis/design/design_patterns#sorting_order>`__.
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
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListLiveConfigsResponse(proto.Message):
    r"""Response message for VideoStitcher.ListLiveConfig.

    Attributes:
        live_configs (MutableSequence[google.cloud.video.stitcher_v1.types.LiveConfig]):
            List of live configs.
        next_page_token (str):
            The pagination token.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    live_configs: MutableSequence[gcvs_live_configs.LiveConfig] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcvs_live_configs.LiveConfig,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetLiveConfigRequest(proto.Message):
    r"""Request message for VideoStitcherService.getLiveConfig.

    Attributes:
        name (str):
            Required. The name of the live config to be retrieved, in
            the form of
            ``projects/{project_number}/locations/{location}/liveConfigs/{id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteLiveConfigRequest(proto.Message):
    r"""Request message for VideoStitcherService.deleteLiveConfig.

    Attributes:
        name (str):
            Required. The name of the live config to be deleted, in the
            form of
            ``projects/{project_number}/locations/{location}/liveConfigs/{id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateLiveConfigRequest(proto.Message):
    r"""Request message for VideoStitcherService.updateLiveConfig.

    Attributes:
        live_config (google.cloud.video.stitcher_v1.types.LiveConfig):
            Required. The LiveConfig resource which
            replaces the resource on the server.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The update mask applies to the resource. For the
            ``FieldMask`` definition, see
            https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask
    """

    live_config: gcvs_live_configs.LiveConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcvs_live_configs.LiveConfig,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class CreateVodConfigRequest(proto.Message):
    r"""Request message for VideoStitcherService.createVodConfig

    Attributes:
        parent (str):
            Required. The project in which the VOD config should be
            created, in the form of
            ``projects/{project_number}/locations/{location}``.
        vod_config_id (str):
            Required. The unique identifier ID to use for
            the VOD config.
        vod_config (google.cloud.video.stitcher_v1.types.VodConfig):
            Required. The VOD config resource to create.
        request_id (str):
            Optional. A request ID to identify requests. Specify a
            unique request ID so that if you must retry your request,
            the server will know to ignore the request if it has already
            been completed. The server will guarantee that for at least
            60 minutes since the first request.

            For example, consider a situation where you make an initial
            request and the request times out. If you make the request
            again with the same request ID, the server can check if
            original operation with the same request ID was received,
            and if so, will ignore the second request. This prevents
            clients from accidentally creating duplicate commitments.

            The request ID must be a valid UUID with the exception that
            zero UUID is not supported
            ``(00000000-0000-0000-0000-000000000000)``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    vod_config_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    vod_config: gcvs_vod_configs.VodConfig = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcvs_vod_configs.VodConfig,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListVodConfigsRequest(proto.Message):
    r"""Request message for VideoStitcherService.listVodConfig.

    Attributes:
        parent (str):
            Required. The project that contains the list of VOD configs,
            in the form of
            ``projects/{project_number}/locations/{location}``.
        page_size (int):
            Optional. The maximum number of items to
            return.
        page_token (str):
            Optional. The next_page_token value returned from a previous
            List request, if any.
        filter (str):
            Optional. The filter to apply to list results (see
            `Filtering <https://google.aip.dev/160>`__).
        order_by (str):
            Optional. Specifies the ordering of results following `Cloud
            API
            syntax <https://cloud.google.com/apis/design/design_patterns#sorting_order>`__.
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
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListVodConfigsResponse(proto.Message):
    r"""Response message for VideoStitcher.ListVodConfig.

    Attributes:
        vod_configs (MutableSequence[google.cloud.video.stitcher_v1.types.VodConfig]):
            List of VOD configs.
        next_page_token (str):
            The pagination token.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    vod_configs: MutableSequence[gcvs_vod_configs.VodConfig] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcvs_vod_configs.VodConfig,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetVodConfigRequest(proto.Message):
    r"""Request message for VideoStitcherService.getVodConfig.

    Attributes:
        name (str):
            Required. The name of the VOD config to be retrieved, in the
            form of
            ``projects/{project_number}/locations/{location}/vodConfigs/{id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteVodConfigRequest(proto.Message):
    r"""Request message for VideoStitcherService.deleteVodConfig.

    Attributes:
        name (str):
            Required. The name of the VOD config to be deleted, in the
            form of
            ``projects/{project_number}/locations/{location}/vodConfigs/{id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateVodConfigRequest(proto.Message):
    r"""Request message for VideoStitcherService.updateVodConfig.

    Attributes:
        vod_config (google.cloud.video.stitcher_v1.types.VodConfig):
            Required. The VOD config resource which
            replaces the resource on the server.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The update mask applies to the resource. For the
            ``FieldMask`` definition, see
            https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask
    """

    vod_config: gcvs_vod_configs.VodConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcvs_vod_configs.VodConfig,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class OperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the operation was created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time the operation finished running.
        target (str):
            Server-defined resource path for the target
            of the operation.
        verb (str):
            Name of the verb executed by the operation.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    target: str = proto.Field(
        proto.STRING,
        number=3,
    )
    verb: str = proto.Field(
        proto.STRING,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
