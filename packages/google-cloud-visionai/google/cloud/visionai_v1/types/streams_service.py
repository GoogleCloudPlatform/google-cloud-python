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

from google.cloud.visionai_v1.types import common, streams_resources

__protobuf__ = proto.module(
    package="google.cloud.visionai.v1",
    manifest={
        "ListClustersRequest",
        "ListClustersResponse",
        "GetClusterRequest",
        "CreateClusterRequest",
        "UpdateClusterRequest",
        "DeleteClusterRequest",
        "ListStreamsRequest",
        "ListStreamsResponse",
        "GetStreamRequest",
        "CreateStreamRequest",
        "UpdateStreamRequest",
        "DeleteStreamRequest",
        "GetStreamThumbnailRequest",
        "GetStreamThumbnailResponse",
        "GenerateStreamHlsTokenRequest",
        "GenerateStreamHlsTokenResponse",
        "ListEventsRequest",
        "ListEventsResponse",
        "GetEventRequest",
        "CreateEventRequest",
        "UpdateEventRequest",
        "DeleteEventRequest",
        "ListSeriesRequest",
        "ListSeriesResponse",
        "GetSeriesRequest",
        "CreateSeriesRequest",
        "UpdateSeriesRequest",
        "DeleteSeriesRequest",
        "MaterializeChannelRequest",
    },
)


class ListClustersRequest(proto.Message):
    r"""Message for requesting list of Clusters.

    Attributes:
        parent (str):
            Required. Parent value for
            ListClustersRequest.
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Filtering results.
        order_by (str):
            Hint for how to order the results.
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


class ListClustersResponse(proto.Message):
    r"""Message for response to listing Clusters.

    Attributes:
        clusters (MutableSequence[google.cloud.visionai_v1.types.Cluster]):
            The list of Cluster.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    clusters: MutableSequence[common.Cluster] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=common.Cluster,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetClusterRequest(proto.Message):
    r"""Message for getting a Cluster.

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateClusterRequest(proto.Message):
    r"""Message for creating a Cluster.

    Attributes:
        parent (str):
            Required. Value for parent.
        cluster_id (str):
            Required. Id of the requesting object.
        cluster (google.cloud.visionai_v1.types.Cluster):
            Required. The resource being created.
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
    cluster_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cluster: common.Cluster = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common.Cluster,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateClusterRequest(proto.Message):
    r"""Message for updating a Cluster.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the Cluster resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        cluster (google.cloud.visionai_v1.types.Cluster):
            Required. The resource being updated
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

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    cluster: common.Cluster = proto.Field(
        proto.MESSAGE,
        number=2,
        message=common.Cluster,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteClusterRequest(proto.Message):
    r"""Message for deleting a Cluster.

    Attributes:
        name (str):
            Required. Name of the resource
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

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

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListStreamsRequest(proto.Message):
    r"""Message for requesting list of Streams.

    Attributes:
        parent (str):
            Required. Parent value for
            ListStreamsRequest.
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Filtering results.
        order_by (str):
            Hint for how to order the results.
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


class ListStreamsResponse(proto.Message):
    r"""Message for response to listing Streams.

    Attributes:
        streams (MutableSequence[google.cloud.visionai_v1.types.Stream]):
            The list of Stream.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    streams: MutableSequence[streams_resources.Stream] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=streams_resources.Stream,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetStreamRequest(proto.Message):
    r"""Message for getting a Stream.

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateStreamRequest(proto.Message):
    r"""Message for creating a Stream.

    Attributes:
        parent (str):
            Required. Value for parent.
        stream_id (str):
            Required. Id of the requesting object.
        stream (google.cloud.visionai_v1.types.Stream):
            Required. The resource being created.
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
    stream_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    stream: streams_resources.Stream = proto.Field(
        proto.MESSAGE,
        number=3,
        message=streams_resources.Stream,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateStreamRequest(proto.Message):
    r"""Message for updating a Stream.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the Stream resource by the update. The fields
            specified in the update_mask are relative to the resource,
            not the full request. A field will be overwritten if it is
            in the mask. If the user does not provide a mask then all
            fields will be overwritten.
        stream (google.cloud.visionai_v1.types.Stream):
            Required. The resource being updated.
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

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    stream: streams_resources.Stream = proto.Field(
        proto.MESSAGE,
        number=2,
        message=streams_resources.Stream,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteStreamRequest(proto.Message):
    r"""Message for deleting a Stream.

    Attributes:
        name (str):
            Required. Name of the resource.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

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

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetStreamThumbnailRequest(proto.Message):
    r"""Message for getting the thumbnail of a Stream.

    Attributes:
        stream (str):
            Required. The name of the stream for to get
            the thumbnail from.
        gcs_object_name (str):
            Required. The name of the GCS object to store
            the thumbnail image.
        event (str):
            Optional. The name of the event. If
            unspecified, the thumbnail will be retrieved
            from the latest event.
        request_id (str):
            Optional. An optional request ID to identify
            the requests. Specify a unique request ID so
            that if you must retry your request, the server
            will know to ignore the request if it has
            already been completed. The server will
            guarantee that for at least 60 minutes since the
            first request.

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

    stream: str = proto.Field(
        proto.STRING,
        number=1,
    )
    gcs_object_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    event: str = proto.Field(
        proto.STRING,
        number=3,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class GetStreamThumbnailResponse(proto.Message):
    r"""Message for the response of GetStreamThumbnail. The empty
    response message indicates the thumbnail image has been uploaded
    to GCS successfully.

    """


class GenerateStreamHlsTokenRequest(proto.Message):
    r"""Request message for getting the auth token to access the
    stream HLS contents.

    Attributes:
        stream (str):
            Required. The name of the stream.
    """

    stream: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GenerateStreamHlsTokenResponse(proto.Message):
    r"""Response message for GenerateStreamHlsToken.

    Attributes:
        token (str):
            The generated JWT token.

            The caller should insert this token to the
            authorization header of the HTTP requests to get
            the HLS playlist manifest and the video chunks.
            eg: curl -H "Authorization: Bearer $TOKEN"
            https://domain.com/test-stream.playback/master.m3u8
        expiration_time (google.protobuf.timestamp_pb2.Timestamp):
            The expiration time of the token.
    """

    token: str = proto.Field(
        proto.STRING,
        number=1,
    )
    expiration_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class ListEventsRequest(proto.Message):
    r"""Message for requesting list of Events.

    Attributes:
        parent (str):
            Required. Parent value for ListEventsRequest.
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Filtering results.
        order_by (str):
            Hint for how to order the results.
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
    r"""Message for response to listing Events.

    Attributes:
        events (MutableSequence[google.cloud.visionai_v1.types.Event]):
            The list of Event.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    events: MutableSequence[streams_resources.Event] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=streams_resources.Event,
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
    r"""Message for getting a Event.

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateEventRequest(proto.Message):
    r"""Message for creating a Event.

    Attributes:
        parent (str):
            Required. Value for parent.
        event_id (str):
            Required. Id of the requesting object.
        event (google.cloud.visionai_v1.types.Event):
            Required. The resource being created.
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
    event_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    event: streams_resources.Event = proto.Field(
        proto.MESSAGE,
        number=3,
        message=streams_resources.Event,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateEventRequest(proto.Message):
    r"""Message for updating a Event.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the Event resource by the update. The fields
            specified in the update_mask are relative to the resource,
            not the full request. A field will be overwritten if it is
            in the mask. If the user does not provide a mask then all
            fields will be overwritten.
        event (google.cloud.visionai_v1.types.Event):
            Required. The resource being updated.
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

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    event: streams_resources.Event = proto.Field(
        proto.MESSAGE,
        number=2,
        message=streams_resources.Event,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteEventRequest(proto.Message):
    r"""Message for deleting a Event.

    Attributes:
        name (str):
            Required. Name of the resource.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

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

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListSeriesRequest(proto.Message):
    r"""Message for requesting list of Series.

    Attributes:
        parent (str):
            Required. Parent value for ListSeriesRequest.
        page_size (int):
            Requested page size. Server may return fewer
            items than requested. If unspecified, server
            will pick an appropriate default.
        page_token (str):
            A token identifying a page of results the
            server should return.
        filter (str):
            Filtering results.
        order_by (str):
            Hint for how to order the results.
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


class ListSeriesResponse(proto.Message):
    r"""Message for response to listing Series.

    Attributes:
        series (MutableSequence[google.cloud.visionai_v1.types.Series]):
            The list of Series.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    series: MutableSequence[streams_resources.Series] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=streams_resources.Series,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetSeriesRequest(proto.Message):
    r"""Message for getting a Series.

    Attributes:
        name (str):
            Required. Name of the resource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateSeriesRequest(proto.Message):
    r"""Message for creating a Series.

    Attributes:
        parent (str):
            Required. Value for parent.
        series_id (str):
            Required. Id of the requesting object.
        series (google.cloud.visionai_v1.types.Series):
            Required. The resource being created.
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
    series_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    series: streams_resources.Series = proto.Field(
        proto.MESSAGE,
        number=3,
        message=streams_resources.Series,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateSeriesRequest(proto.Message):
    r"""Message for updating a Series.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the Series resource by the update. The fields
            specified in the update_mask are relative to the resource,
            not the full request. A field will be overwritten if it is
            in the mask. If the user does not provide a mask then all
            fields will be overwritten.
        series (google.cloud.visionai_v1.types.Series):
            Required. The resource being updated
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

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    series: streams_resources.Series = proto.Field(
        proto.MESSAGE,
        number=2,
        message=streams_resources.Series,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteSeriesRequest(proto.Message):
    r"""Message for deleting a Series.

    Attributes:
        name (str):
            Required. Name of the resource.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

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

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class MaterializeChannelRequest(proto.Message):
    r"""Message for materializing a channel.

    Attributes:
        parent (str):
            Required. Value for parent.
        channel_id (str):
            Required. Id of the channel.
        channel (google.cloud.visionai_v1.types.Channel):
            Required. The resource being created.
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
    channel_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    channel: streams_resources.Channel = proto.Field(
        proto.MESSAGE,
        number=3,
        message=streams_resources.Channel,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
