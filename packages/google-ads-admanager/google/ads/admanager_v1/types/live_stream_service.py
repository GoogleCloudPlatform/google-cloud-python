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

from google.ads.admanager_v1.types import live_stream_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetLiveStreamRequest",
        "ListLiveStreamsRequest",
        "ListLiveStreamsResponse",
        "CreateLiveStreamRequest",
        "BatchCreateLiveStreamsRequest",
        "BatchCreateLiveStreamsResponse",
        "UpdateLiveStreamRequest",
        "BatchUpdateLiveStreamsRequest",
        "BatchUpdateLiveStreamsResponse",
        "BatchActivateLiveStreamsRequest",
        "BatchActivateLiveStreamsResponse",
        "BatchPauseLiveStreamsRequest",
        "BatchPauseLiveStreamsResponse",
        "BatchArchiveLiveStreamsRequest",
        "BatchArchiveLiveStreamsResponse",
        "BatchPauseAdsLiveStreamsRequest",
        "BatchPauseAdsLiveStreamsResponse",
        "BatchRefreshMasterPlaylistsRequest",
        "BatchRefreshMasterPlaylistsResponse",
    },
)


class GetLiveStreamRequest(proto.Message):
    r"""Request object for ``GetLiveStream`` method.

    Attributes:
        name (str):
            Required. The resource name of the LiveStream. Format:
            ``networks/{network_code}/liveStreams/{live_stream_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListLiveStreamsRequest(proto.Message):
    r"""Request object for ``ListLiveStreams`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            LiveStreams. Format: ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of ``LiveStreams`` to return.
            The service may return fewer than this value. If
            unspecified, at most 50 ``LiveStreams`` will be returned.
            The maximum value is 1000; values greater than 1000 will be
            coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListLiveStreams`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListLiveStreams`` must match the call that provided the
            page token.
        filter (str):
            Optional. Expression to filter the response. See syntax
            details at
            https://developers.google.com/ad-manager/api/beta/filters

            **Filterable fields:**

            - ``assetKey``
            - ``createTime``
            - ``customAssetKey``
            - ``daiAuthenticationKeys``
            - ``daiEncodingProfiles``
            - ``displayName``
            - ``dynamicAdInsertionType``
            - ``effectiveAssetKey``
            - ``endTime``
            - ``segmentUrlAuthenticationKeys``
            - ``slate``
            - ``sourceContentConfigurations``
            - ``startTime``
            - ``status``
            - ``streamingFormat``
            - ``updateTime``
        order_by (str):
            Optional. Expression to specify sorting
            order. See syntax details at
            https://developers.google.com/ad-manager/api/beta/filters#order
        skip (int):
            Optional. Number of individual resources to
            skip while paginating.
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
    skip: int = proto.Field(
        proto.INT32,
        number=6,
    )


class ListLiveStreamsResponse(proto.Message):
    r"""Response object for ``ListLiveStreamsRequest`` containing matching
    ``LiveStream`` objects.

    Attributes:
        live_streams (MutableSequence[google.ads.admanager_v1.types.LiveStream]):
            The ``LiveStream`` objects from the specified network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of ``LiveStream`` objects. If a filter was
            included in the request, this reflects the total number
            after the filtering is applied.

            ``total_size`` won't be calculated in the response unless it
            has been included in a response field mask. The response
            field mask can be provided to the method by using the URL
            parameter ``$fields`` or ``fields``, or by using the
            HTTP/gRPC header ``X-Goog-FieldMask``.

            For more information, see
            https://developers.google.com/ad-manager/api/beta/field-masks
    """

    @property
    def raw_page(self):
        return self

    live_streams: MutableSequence[live_stream_messages.LiveStream] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=live_stream_messages.LiveStream,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CreateLiveStreamRequest(proto.Message):
    r"""Request object for ``CreateLiveStream`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this ``LiveStream`` will
            be created. Format: ``networks/{network_code}``
        live_stream (google.ads.admanager_v1.types.LiveStream):
            Required. The ``LiveStream`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    live_stream: live_stream_messages.LiveStream = proto.Field(
        proto.MESSAGE,
        number=2,
        message=live_stream_messages.LiveStream,
    )


class BatchCreateLiveStreamsRequest(proto.Message):
    r"""Request object for ``BatchCreateLiveStreams`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``LiveStreams`` will be
            created. Format: ``networks/{network_code}`` The parent
            field in the CreateLiveStreamRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.CreateLiveStreamRequest]):
            Required. The ``LiveStream`` objects to create. A maximum of
            100 objects can be created in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateLiveStreamRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateLiveStreamRequest",
    )


class BatchCreateLiveStreamsResponse(proto.Message):
    r"""Response object for ``BatchCreateLiveStreams`` method.

    Attributes:
        live_streams (MutableSequence[google.ads.admanager_v1.types.LiveStream]):
            The ``LiveStream`` objects created.
    """

    live_streams: MutableSequence[live_stream_messages.LiveStream] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=live_stream_messages.LiveStream,
        )
    )


class UpdateLiveStreamRequest(proto.Message):
    r"""Request object for ``UpdateLiveStream`` method.

    Attributes:
        live_stream (google.ads.admanager_v1.types.LiveStream):
            Required. The ``LiveStream`` to update.

            The ``LiveStream``'s ``name`` is used to identify the
            ``LiveStream`` to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    live_stream: live_stream_messages.LiveStream = proto.Field(
        proto.MESSAGE,
        number=1,
        message=live_stream_messages.LiveStream,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateLiveStreamsRequest(proto.Message):
    r"""Request object for ``BatchUpdateLiveStreams`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``LiveStreams`` will be
            updated. Format: ``networks/{network_code}`` The parent
            field in the UpdateLiveStreamRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.UpdateLiveStreamRequest]):
            Required. The ``LiveStream`` objects to update. A maximum of
            100 objects can be updated in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateLiveStreamRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdateLiveStreamRequest",
    )


class BatchUpdateLiveStreamsResponse(proto.Message):
    r"""Response object for ``BatchUpdateLiveStreams`` method.

    Attributes:
        live_streams (MutableSequence[google.ads.admanager_v1.types.LiveStream]):
            The ``LiveStream`` objects updated.
    """

    live_streams: MutableSequence[live_stream_messages.LiveStream] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=live_stream_messages.LiveStream,
        )
    )


class BatchActivateLiveStreamsRequest(proto.Message):
    r"""Request object for ``BatchActivateLiveStreams`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the ``LiveStream``\ s to
            activate. Format:
            ``networks/{network_code}/liveStreams/{live_stream_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchActivateLiveStreamsResponse(proto.Message):
    r"""Response object for ``BatchActivateLiveStreams`` method."""


class BatchPauseLiveStreamsRequest(proto.Message):
    r"""Request object for ``BatchPauseLiveStreams`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the ``LiveStream``\ s to
            pause. Format:
            ``networks/{network_code}/liveStreams/{live_stream_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchPauseLiveStreamsResponse(proto.Message):
    r"""Response object for ``BatchPauseLiveStreams`` method."""


class BatchArchiveLiveStreamsRequest(proto.Message):
    r"""Request object for ``BatchArchiveLiveStreams`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the ``LiveStream``\ s to
            archive. Format:
            ``networks/{network_code}/liveStreams/{live_stream_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchArchiveLiveStreamsResponse(proto.Message):
    r"""Response object for ``BatchArchiveLiveStreams`` method."""


class BatchPauseAdsLiveStreamsRequest(proto.Message):
    r"""Request object for ``BatchPauseAdsLiveStreams`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the ``LiveStream``\ s to
            pause ads on. Format:
            ``networks/{network_code}/liveStreams/{live_stream_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchPauseAdsLiveStreamsResponse(proto.Message):
    r"""Response object for ``BatchPauseAdsLiveStreams`` method."""


class BatchRefreshMasterPlaylistsRequest(proto.Message):
    r"""Request object for ``BatchRefreshMasterPlaylists`` method.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the ``LiveStream``\ s to
            refresh master playlists on. Format:
            ``networks/{network_code}/liveStreams/{live_stream_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchRefreshMasterPlaylistsResponse(proto.Message):
    r"""Response object for ``BatchRefreshMasterPlaylists`` method."""


__all__ = tuple(sorted(__protobuf__.manifest))
