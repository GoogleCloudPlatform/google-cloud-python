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

import google.protobuf.any_pb2 as any_pb2  # type: ignore
import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.showcase.v1beta1',
    manifest={
        'Severity',
        'EchoRequest',
        'EchoResponse',
        'EchoErrorDetailsRequest',
        'EchoErrorDetailsResponse',
        'ErrorWithSingleDetail',
        'ErrorWithMultipleDetails',
        'PoetryError',
        'FailEchoWithDetailsRequest',
        'FailEchoWithDetailsResponse',
        'ExpandRequest',
        'PagedExpandRequest',
        'PagedExpandLegacyRequest',
        'PagedExpandResponse',
        'PagedExpandResponseList',
        'PagedExpandLegacyMappedResponse',
        'WaitRequest',
        'WaitResponse',
        'WaitMetadata',
        'BlockRequest',
        'BlockResponse',
    },
)


class Severity(proto.Enum):
    r"""A severity enum used to test enum capabilities in GAPIC
    surfaces.

    Values:
        UNNECESSARY (0):
            No description available.
        NECESSARY (1):
            No description available.
        URGENT (2):
            No description available.
        CRITICAL (3):
            No description available.
    """
    UNNECESSARY = 0
    NECESSARY = 1
    URGENT = 2
    CRITICAL = 3


class EchoRequest(proto.Message):
    r"""The request message used for the Echo, Collect and Chat
    methods. If content or opt are set in this message then the
    request will succeed. If status is set in this message then the
    status will be returned as an error.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        content (str):
            The content to be echoed by the server.

            This field is a member of `oneof`_ ``response``.
        error (google.rpc.status_pb2.Status):
            The error to be thrown by the server.

            This field is a member of `oneof`_ ``response``.
        severity (google.showcase_v1beta1.types.Severity):
            The severity to be echoed by the server.
        header (str):
            Optional. This field can be set to test the
            routing annotation on the Echo method.
        other_header (str):
            Optional. This field can be set to test the
            routing annotation on the Echo method.
        request_id (str):
            To facilitate testing of
            https://google.aip.dev/client-libraries/4235
        other_request_id (str):
            To facilitate testing of
            https://google.aip.dev/client-libraries/4235

            This field is a member of `oneof`_ ``_other_request_id``.
    """

    content: str = proto.Field(
        proto.STRING,
        number=1,
        oneof='response',
    )
    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof='response',
        message=status_pb2.Status,
    )
    severity: 'Severity' = proto.Field(
        proto.ENUM,
        number=3,
        enum='Severity',
    )
    header: str = proto.Field(
        proto.STRING,
        number=4,
    )
    other_header: str = proto.Field(
        proto.STRING,
        number=5,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=7,
    )
    other_request_id: str = proto.Field(
        proto.STRING,
        number=8,
        optional=True,
    )


class EchoResponse(proto.Message):
    r"""The response message for the Echo methods.

    Attributes:
        content (str):
            The content specified in the request.
        severity (google.showcase_v1beta1.types.Severity):
            The severity specified in the request.
        request_id (str):
            The request ID specified or autopopulated in
            the request.
        other_request_id (str):
            The other request ID specified or
            autopopulated in the request.
    """

    content: str = proto.Field(
        proto.STRING,
        number=1,
    )
    severity: 'Severity' = proto.Field(
        proto.ENUM,
        number=2,
        enum='Severity',
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    other_request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class EchoErrorDetailsRequest(proto.Message):
    r"""The request message used for the EchoErrorDetails method.

    Attributes:
        single_detail_text (str):
            Content to return in a singular ``*.error.details`` field of
            type ``google.protobuf.Any``
        multi_detail_text (MutableSequence[str]):
            Content to return in a repeated ``*.error.details`` field of
            type ``google.protobuf.Any``
    """

    single_detail_text: str = proto.Field(
        proto.STRING,
        number=1,
    )
    multi_detail_text: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class EchoErrorDetailsResponse(proto.Message):
    r"""The response message used for the EchoErrorDetails method.

    Attributes:
        single_detail (google.showcase_v1beta1.types.EchoErrorDetailsResponse.SingleDetail):

        multiple_details (google.showcase_v1beta1.types.EchoErrorDetailsResponse.MultipleDetails):

    """

    class SingleDetail(proto.Message):
        r"""

        Attributes:
            error (google.showcase_v1beta1.types.ErrorWithSingleDetail):

        """

        error: 'ErrorWithSingleDetail' = proto.Field(
            proto.MESSAGE,
            number=1,
            message='ErrorWithSingleDetail',
        )

    class MultipleDetails(proto.Message):
        r"""

        Attributes:
            error (google.showcase_v1beta1.types.ErrorWithMultipleDetails):

        """

        error: 'ErrorWithMultipleDetails' = proto.Field(
            proto.MESSAGE,
            number=1,
            message='ErrorWithMultipleDetails',
        )

    single_detail: SingleDetail = proto.Field(
        proto.MESSAGE,
        number=1,
        message=SingleDetail,
    )
    multiple_details: MultipleDetails = proto.Field(
        proto.MESSAGE,
        number=2,
        message=MultipleDetails,
    )


class ErrorWithSingleDetail(proto.Message):
    r"""

    Attributes:
        details (google.protobuf.any_pb2.Any):

    """

    details: any_pb2.Any = proto.Field(
        proto.MESSAGE,
        number=1,
        message=any_pb2.Any,
    )


class ErrorWithMultipleDetails(proto.Message):
    r"""

    Attributes:
        details (MutableSequence[google.protobuf.any_pb2.Any]):

    """

    details: MutableSequence[any_pb2.Any] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=any_pb2.Any,
    )


class PoetryError(proto.Message):
    r"""The custom error detail to be included in the error response
    from the FailEchoWithDetails method. Client libraries should be
    able to surface this custom error detail.

    Attributes:
        poem (str):

    """

    poem: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FailEchoWithDetailsRequest(proto.Message):
    r"""The request message used for the FailEchoWithDetails method.

    Attributes:
        message (str):
            Optional message to echo back in the
            PoetryError. If empty, a value will be provided.
    """

    message: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FailEchoWithDetailsResponse(proto.Message):
    r"""The response message declared (but never used) for the
    FailEchoWithDetails method.

    """


class ExpandRequest(proto.Message):
    r"""The request message for the Expand method.

    Attributes:
        content (str):
            The content that will be split into words and
            returned on the stream.
        error (google.rpc.status_pb2.Status):
            The error that is thrown after all words are
            sent on the stream.
        stream_wait_time (google.protobuf.duration_pb2.Duration):
            The wait time between each server streaming
            messages
    """

    content: str = proto.Field(
        proto.STRING,
        number=1,
    )
    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=2,
        message=status_pb2.Status,
    )
    stream_wait_time: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )


class PagedExpandRequest(proto.Message):
    r"""The request for the PagedExpand method.

    Attributes:
        content (str):
            The string to expand.
        page_size (int):
            The number of words to returned in each page.
        page_token (str):
            The position of the page to be returned.
    """

    content: str = proto.Field(
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


class PagedExpandLegacyRequest(proto.Message):
    r"""The request for the PagedExpandLegacy method.  This is a
    pattern used by some legacy APIs. New APIs should NOT use this
    pattern, but rather something like PagedExpandRequest which
    conforms to aip.dev/158.

    Attributes:
        content (str):
            The string to expand.
        max_results (int):
            The number of words to returned in each page. (--
            aip.dev/not-precedent: This is a legacy, non-standard
            pattern that violates aip.dev/158. Ordinarily, this should
            be page_size. --)
        page_token (str):
            The position of the page to be returned.
    """

    content: str = proto.Field(
        proto.STRING,
        number=1,
    )
    max_results: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class PagedExpandResponse(proto.Message):
    r"""The response for the PagedExpand method.

    Attributes:
        responses (MutableSequence[google.showcase_v1beta1.types.EchoResponse]):
            The words that were expanded.
        next_page_token (str):
            The next page token.
    """

    @property
    def raw_page(self):
        return self

    responses: MutableSequence['EchoResponse'] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='EchoResponse',
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class PagedExpandResponseList(proto.Message):
    r"""A list of words.

    Attributes:
        words (MutableSequence[str]):

    """

    words: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class PagedExpandLegacyMappedResponse(proto.Message):
    r"""

    Attributes:
        alphabetized (MutableMapping[str, google.showcase_v1beta1.types.PagedExpandResponseList]):
            The words that were expanded, indexed by their initial
            character. (-- aip.dev/not-precedent: This is a legacy,
            non-standard pattern that violates aip.dev/158. Ordinarily,
            this should be a ``repeated`` field, as in
            PagedExpandResponse. --)
        next_page_token (str):
            The next page token.
    """

    @property
    def raw_page(self):
        return self

    alphabetized: MutableMapping[str, 'PagedExpandResponseList'] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=1,
        message='PagedExpandResponseList',
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class WaitRequest(proto.Message):
    r"""The request for Wait method.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time that this operation will complete.

            This field is a member of `oneof`_ ``end``.
        ttl (google.protobuf.duration_pb2.Duration):
            The duration of this operation.

            This field is a member of `oneof`_ ``end``.
        error (google.rpc.status_pb2.Status):
            The error that will be returned by the
            server. If this code is specified to be the OK
            rpc code, an empty response will be returned.

            This field is a member of `oneof`_ ``response``.
        success (google.showcase_v1beta1.types.WaitResponse):
            The response to be returned on operation
            completion.

            This field is a member of `oneof`_ ``response``.
    """

    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof='end',
        message=timestamp_pb2.Timestamp,
    )
    ttl: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof='end',
        message=duration_pb2.Duration,
    )
    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof='response',
        message=status_pb2.Status,
    )
    success: 'WaitResponse' = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof='response',
        message='WaitResponse',
    )


class WaitResponse(proto.Message):
    r"""The result of the Wait operation.

    Attributes:
        content (str):
            This content of the result.
    """

    content: str = proto.Field(
        proto.STRING,
        number=1,
    )


class WaitMetadata(proto.Message):
    r"""The metadata for Wait operation.

    Attributes:
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            The time that this operation will complete.
    """

    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )


class BlockRequest(proto.Message):
    r"""The request for Block method.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        response_delay (google.protobuf.duration_pb2.Duration):
            The amount of time to block before returning
            a response.
        error (google.rpc.status_pb2.Status):
            The error that will be returned by the
            server. If this code is specified to be the OK
            rpc code, an empty response will be returned.

            This field is a member of `oneof`_ ``response``.
        success (google.showcase_v1beta1.types.BlockResponse):
            The response to be returned that will signify
            successful method call.

            This field is a member of `oneof`_ ``response``.
    """

    response_delay: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )
    error: status_pb2.Status = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof='response',
        message=status_pb2.Status,
    )
    success: 'BlockResponse' = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof='response',
        message='BlockResponse',
    )


class BlockResponse(proto.Message):
    r"""The response for Block method.

    Attributes:
        content (str):
            This content can contain anything, the server
            will not depend on a value here.
    """

    content: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
