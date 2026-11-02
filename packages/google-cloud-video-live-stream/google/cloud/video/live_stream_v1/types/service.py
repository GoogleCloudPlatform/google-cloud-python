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

from google.cloud.video.live_stream_v1.types import resources

__protobuf__ = proto.module(
    package="google.cloud.video.livestream.v1",
    manifest={
        "CreateAssetRequest",
        "DeleteAssetRequest",
        "ListAssetsRequest",
        "ListAssetsResponse",
        "GetAssetRequest",
        "CreateChannelRequest",
        "ListChannelsRequest",
        "ListChannelsResponse",
        "GetChannelRequest",
        "DeleteChannelRequest",
        "UpdateChannelRequest",
        "StartChannelRequest",
        "StopChannelRequest",
        "StartDistributionRequest",
        "StopDistributionRequest",
        "CreateInputRequest",
        "ListInputsRequest",
        "ListInputsResponse",
        "GetInputRequest",
        "DeleteInputRequest",
        "UpdateInputRequest",
        "CreateEventRequest",
        "ListEventsRequest",
        "ListEventsResponse",
        "GetEventRequest",
        "DeleteEventRequest",
        "ChannelOperationResponse",
        "ListClipsRequest",
        "ListClipsResponse",
        "GetClipRequest",
        "CreateClipRequest",
        "DeleteClipRequest",
        "ListDvrSessionsRequest",
        "ListDvrSessionsResponse",
        "GetDvrSessionRequest",
        "CreateDvrSessionRequest",
        "DeleteDvrSessionRequest",
        "UpdateDvrSessionRequest",
        "OperationMetadata",
        "GetPoolRequest",
        "UpdatePoolRequest",
        "PreviewInputRequest",
        "PreviewInputResponse",
    },
)


class CreateAssetRequest(proto.Message):
    r"""Request message for "LivestreamService.CreateAsset".

    Attributes:
        parent (str):
            Required. The parent location for the resource, in the form
            of: ``projects/{project}/locations/{location}``.
        asset (google.cloud.video.live_stream_v1.types.Asset):
            Required. The asset resource to be created.
        asset_id (str):
            Required. The ID of the asset resource to be created.

            This value must be 1-63 characters, begin and end with a
            lower-case letter or a number, and consist of only
            lower-case letters, numbers, and hyphens. In other words, it
            must match the following regex:
            ``^[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?$``.
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
    asset: resources.Asset = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.Asset,
    )
    asset_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteAssetRequest(proto.Message):
    r"""Request message for "LivestreamService.DeleteAsset".

    Attributes:
        name (str):
            Required. The name of the asset resource, in the form of:
            ``projects/{project}/locations/{location}/assets/{assetId}``.
        request_id (str):
            A request ID to identify requests. Specify a unique request
            ID so that if you must retry your request, the server will
            know to ignore the request if it has already been completed.
            The server will guarantee that for at least 60 minutes after
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

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListAssetsRequest(proto.Message):
    r"""Request message for "LivestreamService.ListAssets".

    Attributes:
        parent (str):
            Required. The parent location for the resource, in the form
            of: ``projects/{project}/locations/{location}``.
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


class ListAssetsResponse(proto.Message):
    r"""Response message for "LivestreamService.ListAssets".

    Attributes:
        assets (MutableSequence[google.cloud.video.live_stream_v1.types.Asset]):
            The list of Assets
        next_page_token (str):
            The next_page_token value returned from a previous List
            request, if any.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    assets: MutableSequence[resources.Asset] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Asset,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetAssetRequest(proto.Message):
    r"""Request message for "LivestreamService.GetAsset".

    Attributes:
        name (str):
            Required. Name of the resource, in the following form:
            ``projects/{project}/locations/{location}/assets/{asset}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateChannelRequest(proto.Message):
    r"""Request message for "LivestreamService.CreateChannel".

    Attributes:
        parent (str):
            Required. The parent location for the resource, in the form
            of: ``projects/{project}/locations/{location}``.
        channel (google.cloud.video.live_stream_v1.types.Channel):
            Required. The channel resource to be created.
        channel_id (str):
            Required. The ID of the channel resource to be created.

            This value must be 1-63 characters, begin and end with a
            lower-case letter or a number, and consist of only
            lower-case letters, numbers, and hyphens. In other words, it
            must match the following regex:
            ``^[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?$``.
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
    channel: resources.Channel = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.Channel,
    )
    channel_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListChannelsRequest(proto.Message):
    r"""Request message for "LivestreamService.ListChannels".

    Attributes:
        parent (str):
            Required. The parent location for the resource, in the form
            of: ``projects/{project}/locations/{location}``.
        page_size (int):
            The maximum number of items to return. If unspecified,
            server will pick an appropriate default. Server may return
            fewer items than requested. A caller should only rely on
            response's
            [next_page_token][google.cloud.video.livestream.v1.ListChannelsResponse.next_page_token]
            to determine if there are more items left to be queried.
        page_token (str):
            The next_page_token value returned from a previous List
            request, if any.
        filter (str):
            The filter to apply to list results.
        order_by (str):
            Specifies the ordering of results following syntax at
            https://cloud.google.com/apis/design/design_patterns#sorting_order.
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


class ListChannelsResponse(proto.Message):
    r"""Response message for "LivestreamService.ListChannels".

    Attributes:
        channels (MutableSequence[google.cloud.video.live_stream_v1.types.Channel]):
            A list of channels.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    channels: MutableSequence[resources.Channel] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Channel,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetChannelRequest(proto.Message):
    r"""Request message for "LivestreamService.GetChannel".

    Attributes:
        name (str):
            Required. The name of the channel resource, in the form of:
            ``projects/{project}/locations/{location}/channels/{channelId}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteChannelRequest(proto.Message):
    r"""Request message for "LivestreamService.DeleteChannel".

    Attributes:
        name (str):
            Required. The name of the channel resource, in the form of:
            ``projects/{project}/locations/{location}/channels/{channelId}``.
        request_id (str):
            A request ID to identify requests. Specify a unique request
            ID so that if you must retry your request, the server will
            know to ignore the request if it has already been completed.
            The server will guarantee that for at least 60 minutes after
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
        force (bool):
            If the ``force`` field is set to the default value of
            ``false``, you must delete all of a channel's events before
            you can delete the channel itself. If the field is set to
            ``true``, requests to delete a channel also delete
            associated channel events.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class UpdateChannelRequest(proto.Message):
    r"""Request message for "LivestreamService.UpdateChannel".

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Field mask is used to specify the fields to be overwritten
            in the Channel resource by the update. You can only update
            the following fields:

            - ```inputAttachments`` <https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#inputattachment>`__
            - ```inputConfig`` <https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#inputconfig>`__
            - ```output`` <https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#output>`__
            - ```elementaryStreams`` <https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#elementarystream>`__
            - ```muxStreams`` <https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#muxstream>`__
            - ```manifests`` <https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#manifest>`__
            - ```spriteSheets`` <https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#spritesheet>`__
            - ```logConfig`` <https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#logconfig>`__
            - ```timecodeConfig`` <https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#timecodeconfig>`__
            - ```encryptions`` <https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels#encryption>`__

            The fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask.

            If the mask is not present, then each field from the list
            above is updated if the field appears in the request
            payload. To unset a field, add the field to the update mask
            and remove it from the request payload.
        channel (google.cloud.video.live_stream_v1.types.Channel):
            Required. The channel resource to be updated.
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

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    channel: resources.Channel = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.Channel,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class StartChannelRequest(proto.Message):
    r"""Request message for "LivestreamService.StartChannel".

    Attributes:
        name (str):
            Required. The name of the channel resource, in the form of:
            ``projects/{project}/locations/{location}/channels/{channelId}``.
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

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class StopChannelRequest(proto.Message):
    r"""Request message for "LivestreamService.StopChannel".

    Attributes:
        name (str):
            Required. The name of the channel resource, in the form of:
            ``projects/{project}/locations/{location}/channels/{channelId}``.
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

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class StartDistributionRequest(proto.Message):
    r"""Request message for "LivestreamService.StartDistribution".

    Attributes:
        name (str):
            Required. The name of the channel resource, in the form of:
            ``projects/{project}/locations/{location}/channels/{channelId}``.
        distribution_keys (MutableSequence[str]):
            Optional. A list of keys to identify the
            distribution configuration in the channel
            resource. If left empty, all the distributions
            in the channel specification will be started.
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

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    distribution_keys: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class StopDistributionRequest(proto.Message):
    r"""Request message for "LivestreamService.StopDistribution".

    Attributes:
        name (str):
            Required. The name of the channel resource, in the form of:
            ``projects/{project}/locations/{location}/channels/{channelId}``.
        distribution_keys (MutableSequence[str]):
            Optional. A list of key to identify the
            distribution configuration in the channel
            resource. If left empty, all the distributions
            in the channel specification will be stopped.
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

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    distribution_keys: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class CreateInputRequest(proto.Message):
    r"""Request message for "LivestreamService.CreateInput".

    Attributes:
        parent (str):
            Required. The parent location for the resource, in the form
            of: ``projects/{project}/locations/{location}``.
        input (google.cloud.video.live_stream_v1.types.Input):
            Required. The input resource to be created.
        input_id (str):
            Required. The ID of the input resource to be created.

            This value must be 1-63 characters, begin and end with a
            lower-case letter or a number, and consist of only
            lower-case letters, numbers, and hyphens. In other words, it
            must match the following regex:
            ``^[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?$``.
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
    input: resources.Input = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.Input,
    )
    input_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListInputsRequest(proto.Message):
    r"""Request message for "LivestreamService.ListInputs".

    Attributes:
        parent (str):
            Required. The parent location for the resource, in the form
            of: ``projects/{project}/locations/{location}``.
        page_size (int):
            The maximum number of items to return. If unspecified,
            server will pick an appropriate default. Server may return
            fewer items than requested. A caller should only rely on
            response's
            [next_page_token][google.cloud.video.livestream.v1.ListInputsResponse.next_page_token]
            to determine if there are more items left to be queried.
        page_token (str):
            The next_page_token value returned from a previous List
            request, if any.
        filter (str):
            The filter to apply to list results.
        order_by (str):
            Specifies the ordering of results following syntax at
            `Sorting
            Order <https://cloud.google.com/apis/design/design_patterns#sorting_order>`__.
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


class ListInputsResponse(proto.Message):
    r"""Response message for "LivestreamService.ListInputs".

    Attributes:
        inputs (MutableSequence[google.cloud.video.live_stream_v1.types.Input]):
            A list of inputs.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    inputs: MutableSequence[resources.Input] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Input,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetInputRequest(proto.Message):
    r"""Request message for "LivestreamService.GetInput".

    Attributes:
        name (str):
            Required. The name of the input resource, in the form of:
            ``projects/{project}/locations/{location}/inputs/{inputId}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteInputRequest(proto.Message):
    r"""Request message for "LivestreamService.DeleteInput".

    Attributes:
        name (str):
            Required. The name of the input resource, in the form of:
            ``projects/{project}/locations/{location}/inputs/{inputId}``.
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

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateInputRequest(proto.Message):
    r"""Request message for "LivestreamService.UpdateInput".

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Field mask is used to specify the fields to be overwritten
            in the Input resource by the update. You can only update the
            following fields:

            - ```tier`` <https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#Tier>`__
            - ```preprocessingConfig`` <https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#PreprocessingConfig>`__
            - ```securityRules`` <https://cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#SecurityRule>`__

            The fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask.

            If the mask is not present, then each field from the list
            above is updated if the field appears in the request
            payload. To unset a field, add the field to the update mask
            and remove it from the request payload.
        input (google.cloud.video.live_stream_v1.types.Input):
            Required. The input resource to be updated.
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

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    input: resources.Input = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.Input,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class CreateEventRequest(proto.Message):
    r"""Request message for "LivestreamService.CreateEvent".

    Attributes:
        parent (str):
            Required. The parent channel for the resource, in the form
            of:
            ``projects/{project}/locations/{location}/channels/{channelId}``.
        event (google.cloud.video.live_stream_v1.types.Event):
            Required. The event resource to be created.
        event_id (str):
            Required. The ID of the event resource to be created.

            This value must be 1-63 characters, begin and end with a
            lower-case letter or a number, and consist of only
            lower-case letters, numbers, and hyphens. In other words, it
            must match the following regex:
            ``^[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?$``.
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
    event: resources.Event = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.Event,
    )
    event_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListEventsRequest(proto.Message):
    r"""Request message for "LivestreamService.ListEvents".

    Attributes:
        parent (str):
            Required. The parent channel for the resource, in the form
            of:
            ``projects/{project}/locations/{location}/channels/{channelId}``.
        page_size (int):
            The maximum number of items to return. If unspecified,
            server will pick an appropriate default. Server may return
            fewer items than requested. A caller should only rely on
            response's
            [next_page_token][google.cloud.video.livestream.v1.ListEventsResponse.next_page_token]
            to determine if there are more items left to be queried.
        page_token (str):
            The next_page_token value returned from a previous List
            request, if any.
        filter (str):
            The filter to apply to list results.
        order_by (str):
            Specifies the ordering of results following syntax at
            https://cloud.google.com/apis/design/design_patterns#sorting_order.
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


class ListEventsResponse(proto.Message):
    r"""Response message for "LivestreamService.ListEvents".

    Attributes:
        events (MutableSequence[google.cloud.video.live_stream_v1.types.Event]):
            A list of events.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    events: MutableSequence[resources.Event] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Event,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetEventRequest(proto.Message):
    r"""Request message for "LivestreamService.GetEvent".

    Attributes:
        name (str):
            Required. The name of the event resource, in the form of:
            ``projects/{project}/locations/{location}/channels/{channelId}/events/{eventId}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteEventRequest(proto.Message):
    r"""Request message for "LivestreamService.DeleteEvent".

    Attributes:
        name (str):
            Required. The name of the event resource, in the form of:
            ``projects/{project}/locations/{location}/channels/{channelId}/events/{eventId}``.
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

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ChannelOperationResponse(proto.Message):
    r"""Response message for Start/Stop Channel long-running
    operations.

    """


class ListClipsRequest(proto.Message):
    r"""Request message for "LivestreamService.ListClips".

    Attributes:
        parent (str):
            Required. Parent value for ListClipsRequest
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


class ListClipsResponse(proto.Message):
    r"""Response message for "LivestreamService.ListClips".

    Attributes:
        clips (MutableSequence[google.cloud.video.live_stream_v1.types.Clip]):
            The list of Clip
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    clips: MutableSequence[resources.Clip] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Clip,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetClipRequest(proto.Message):
    r"""Request message for "LivestreamService.GetClip".

    Attributes:
        name (str):
            Required. Name of the resource, in the following form:
            ``projects/{project}/locations/{location}/channels/{channel}/clips/{clip}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateClipRequest(proto.Message):
    r"""Request message for "LivestreamService.CreateClip".

    Attributes:
        parent (str):
            Required. The parent resource name, in the following form:
            ``projects/{project}/locations/{location}/channels/{channel}``.
        clip_id (str):
            Required. The ID of the clip resource to be created.

            This value must be 1-63 characters, begin and end with a
            lower-case letter or a number, and consist of only
            lower-case letters, numbers, and hyphens. In other words, it
            must match the following regex:
            ``^[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?$``.
        clip (google.cloud.video.live_stream_v1.types.Clip):
            Required. The resource being created
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    clip_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    clip: resources.Clip = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.Clip,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteClipRequest(proto.Message):
    r"""Request message for "LivestreamService.DeleteClip".

    Attributes:
        name (str):
            Required. The name of the clip resource, in the form of:
            ``projects/{project}/locations/{location}/channels/{channelId}/clips/{clipId}``.
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

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListDvrSessionsRequest(proto.Message):
    r"""Request message for "LivestreamService.ListDvrSessions".

    Attributes:
        parent (str):
            Required. Parent value for
            ListDvrSessionsRequest
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering results
        order_by (str):
            Optional. Hint for how to order the results
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


class ListDvrSessionsResponse(proto.Message):
    r"""Response message for "LivestreamService.ListDvrSessions".

    Attributes:
        dvr_sessions (MutableSequence[google.cloud.video.live_stream_v1.types.DvrSession]):
            The list of DVR sessions
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    dvr_sessions: MutableSequence[resources.DvrSession] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.DvrSession,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetDvrSessionRequest(proto.Message):
    r"""Request message for "LivestreamService.GetDvrSession".

    Attributes:
        name (str):
            Required. Name of the resource, in the following form:
            ``projects/{project}/locations/{location}/channels/{channelId}/dvrSessions/{dvrSessionId}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateDvrSessionRequest(proto.Message):
    r"""Request message for "LivestreamService.CreateDvrSession".

    Attributes:
        parent (str):
            Required. The parent resource name, in the following form:
            ``projects/{project}/locations/{location}/channels/{channelId}``.
        dvr_session_id (str):
            Required. The ID of the DVR session resource to be created.

            This value must be 1-63 characters, begin and end with a
            lower-case letter or a number, and consist of only
            lower-case letters, numbers, and hyphens. In other words, it
            must match the following regex:
            ``^[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?$``.
        dvr_session (google.cloud.video.live_stream_v1.types.DvrSession):
            Required. The resource being created
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dvr_session_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    dvr_session: resources.DvrSession = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.DvrSession,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteDvrSessionRequest(proto.Message):
    r"""Request message for "LivestreamService.DeleteDvrSession".

    Attributes:
        name (str):
            Required. The name of the event resource, in the form of:
            ``projects/{project}/locations/{location}/channels/{channelId}/dvrSessions/{dvrSessionId}``.
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

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateDvrSessionRequest(proto.Message):
    r"""Request message for "LivestreamService.UpdateDvrSession".

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the DvrSession resource by the update. You
            can only update the following fields:

            - ``dvrWindows``

            The fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask.
        dvr_session (google.cloud.video.live_stream_v1.types.DvrSession):
            Required. The DVR session resource to be
            updated.
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

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    dvr_session: resources.DvrSession = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.DvrSession,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class OperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        target (str):
            Output only. Server-defined resource path for
            the target of the operation.
        verb (str):
            Output only. Name of the verb executed by the
            operation.
        requested_cancellation (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have
            successfully been cancelled have
            [google.longrunning.Operation.error][google.longrunning.Operation.error]
            value with a
            [google.rpc.Status.code][google.rpc.Status.code] of 1,
            corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
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
    requested_cancellation: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=6,
    )


class GetPoolRequest(proto.Message):
    r"""Request message for "LivestreamService.GetPool".

    Attributes:
        name (str):
            Required. The name of the pool resource, in the form of:
            ``projects/{project}/locations/{location}/pools/{poolId}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdatePoolRequest(proto.Message):
    r"""Request message for "LivestreamService.UpdatePool".

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Field mask is used to specify the fields to be overwritten
            in the Pool resource by the update. You can only update the
            following fields:

            - ``networkConfig``

            The fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask.
        pool (google.cloud.video.live_stream_v1.types.Pool):
            Required. The pool resource to be updated.
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

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    pool: resources.Pool = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.Pool,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class PreviewInputRequest(proto.Message):
    r"""Request message for "LivestreamService.PreviewInput".

    Attributes:
        name (str):
            Required. The name of the input resource, in the form of:
            ``projects/{project}/locations/{location}/inputs/{inputId}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class PreviewInputResponse(proto.Message):
    r"""Response message for "LivestreamService.PreviewInput".

    Attributes:
        uri (str):
            URI to display the preview content.
        bearer_token (str):
            A bearer token used to authenticate
            connections that display the preview content.
            The token expires after one hour. For HTTP
            connections, this token should be included as a
            bearer token inside the Authorization header.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )
    bearer_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
