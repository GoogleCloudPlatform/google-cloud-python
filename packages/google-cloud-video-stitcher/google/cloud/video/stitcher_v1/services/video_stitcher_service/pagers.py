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
from typing import (
    Any,
    AsyncIterator,
    Awaitable,
    Callable,
    Iterator,
    Optional,
    Sequence,
    Tuple,
    Union,
)

from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.api_core import retry_async as retries_async

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault, None]
    OptionalAsyncRetry = Union[
        retries_async.AsyncRetry, gapic_v1.method._MethodDefault, None
    ]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object, None]  # type: ignore
    OptionalAsyncRetry = Union[retries_async.AsyncRetry, object, None]  # type: ignore

from google.cloud.video.stitcher_v1.types import (
    ad_tag_details,
    cdn_keys,
    live_configs,
    slates,
    stitch_details,
    video_stitcher_service,
    vod_configs,
)


class ListCdnKeysPager:
    """A pager for iterating through ``list_cdn_keys`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.video.stitcher_v1.types.ListCdnKeysResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``cdn_keys`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCdnKeys`` requests and continue to iterate
    through the ``cdn_keys`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.video.stitcher_v1.types.ListCdnKeysResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., video_stitcher_service.ListCdnKeysResponse],
        request: video_stitcher_service.ListCdnKeysRequest,
        response: video_stitcher_service.ListCdnKeysResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.video.stitcher_v1.types.ListCdnKeysRequest):
                The initial request object.
            response (google.cloud.video.stitcher_v1.types.ListCdnKeysResponse):
                The initial response object.
            retry (google.api_core.retry.Retry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = video_stitcher_service.ListCdnKeysRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[video_stitcher_service.ListCdnKeysResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __iter__(self) -> Iterator[cdn_keys.CdnKey]:
        for page in self.pages:
            yield from page.cdn_keys

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListCdnKeysAsyncPager:
    """A pager for iterating through ``list_cdn_keys`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.video.stitcher_v1.types.ListCdnKeysResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``cdn_keys`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCdnKeys`` requests and continue to iterate
    through the ``cdn_keys`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.video.stitcher_v1.types.ListCdnKeysResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[video_stitcher_service.ListCdnKeysResponse]],
        request: video_stitcher_service.ListCdnKeysRequest,
        response: video_stitcher_service.ListCdnKeysResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.video.stitcher_v1.types.ListCdnKeysRequest):
                The initial request object.
            response (google.cloud.video.stitcher_v1.types.ListCdnKeysResponse):
                The initial response object.
            retry (google.api_core.retry.AsyncRetry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = video_stitcher_service.ListCdnKeysRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[video_stitcher_service.ListCdnKeysResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __aiter__(self) -> AsyncIterator[cdn_keys.CdnKey]:
        async def async_generator():
            async for page in self.pages:
                for response in page.cdn_keys:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListVodStitchDetailsPager:
    """A pager for iterating through ``list_vod_stitch_details`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.video.stitcher_v1.types.ListVodStitchDetailsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``vod_stitch_details`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListVodStitchDetails`` requests and continue to iterate
    through the ``vod_stitch_details`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.video.stitcher_v1.types.ListVodStitchDetailsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., video_stitcher_service.ListVodStitchDetailsResponse],
        request: video_stitcher_service.ListVodStitchDetailsRequest,
        response: video_stitcher_service.ListVodStitchDetailsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.video.stitcher_v1.types.ListVodStitchDetailsRequest):
                The initial request object.
            response (google.cloud.video.stitcher_v1.types.ListVodStitchDetailsResponse):
                The initial response object.
            retry (google.api_core.retry.Retry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = video_stitcher_service.ListVodStitchDetailsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[video_stitcher_service.ListVodStitchDetailsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __iter__(self) -> Iterator[stitch_details.VodStitchDetail]:
        for page in self.pages:
            yield from page.vod_stitch_details

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListVodStitchDetailsAsyncPager:
    """A pager for iterating through ``list_vod_stitch_details`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.video.stitcher_v1.types.ListVodStitchDetailsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``vod_stitch_details`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListVodStitchDetails`` requests and continue to iterate
    through the ``vod_stitch_details`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.video.stitcher_v1.types.ListVodStitchDetailsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[video_stitcher_service.ListVodStitchDetailsResponse]
        ],
        request: video_stitcher_service.ListVodStitchDetailsRequest,
        response: video_stitcher_service.ListVodStitchDetailsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.video.stitcher_v1.types.ListVodStitchDetailsRequest):
                The initial request object.
            response (google.cloud.video.stitcher_v1.types.ListVodStitchDetailsResponse):
                The initial response object.
            retry (google.api_core.retry.AsyncRetry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = video_stitcher_service.ListVodStitchDetailsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[video_stitcher_service.ListVodStitchDetailsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __aiter__(self) -> AsyncIterator[stitch_details.VodStitchDetail]:
        async def async_generator():
            async for page in self.pages:
                for response in page.vod_stitch_details:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListVodAdTagDetailsPager:
    """A pager for iterating through ``list_vod_ad_tag_details`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.video.stitcher_v1.types.ListVodAdTagDetailsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``vod_ad_tag_details`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListVodAdTagDetails`` requests and continue to iterate
    through the ``vod_ad_tag_details`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.video.stitcher_v1.types.ListVodAdTagDetailsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., video_stitcher_service.ListVodAdTagDetailsResponse],
        request: video_stitcher_service.ListVodAdTagDetailsRequest,
        response: video_stitcher_service.ListVodAdTagDetailsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.video.stitcher_v1.types.ListVodAdTagDetailsRequest):
                The initial request object.
            response (google.cloud.video.stitcher_v1.types.ListVodAdTagDetailsResponse):
                The initial response object.
            retry (google.api_core.retry.Retry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = video_stitcher_service.ListVodAdTagDetailsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[video_stitcher_service.ListVodAdTagDetailsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __iter__(self) -> Iterator[ad_tag_details.VodAdTagDetail]:
        for page in self.pages:
            yield from page.vod_ad_tag_details

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListVodAdTagDetailsAsyncPager:
    """A pager for iterating through ``list_vod_ad_tag_details`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.video.stitcher_v1.types.ListVodAdTagDetailsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``vod_ad_tag_details`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListVodAdTagDetails`` requests and continue to iterate
    through the ``vod_ad_tag_details`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.video.stitcher_v1.types.ListVodAdTagDetailsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[video_stitcher_service.ListVodAdTagDetailsResponse]
        ],
        request: video_stitcher_service.ListVodAdTagDetailsRequest,
        response: video_stitcher_service.ListVodAdTagDetailsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.video.stitcher_v1.types.ListVodAdTagDetailsRequest):
                The initial request object.
            response (google.cloud.video.stitcher_v1.types.ListVodAdTagDetailsResponse):
                The initial response object.
            retry (google.api_core.retry.AsyncRetry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = video_stitcher_service.ListVodAdTagDetailsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[video_stitcher_service.ListVodAdTagDetailsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __aiter__(self) -> AsyncIterator[ad_tag_details.VodAdTagDetail]:
        async def async_generator():
            async for page in self.pages:
                for response in page.vod_ad_tag_details:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListLiveAdTagDetailsPager:
    """A pager for iterating through ``list_live_ad_tag_details`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.video.stitcher_v1.types.ListLiveAdTagDetailsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``live_ad_tag_details`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListLiveAdTagDetails`` requests and continue to iterate
    through the ``live_ad_tag_details`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.video.stitcher_v1.types.ListLiveAdTagDetailsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., video_stitcher_service.ListLiveAdTagDetailsResponse],
        request: video_stitcher_service.ListLiveAdTagDetailsRequest,
        response: video_stitcher_service.ListLiveAdTagDetailsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.video.stitcher_v1.types.ListLiveAdTagDetailsRequest):
                The initial request object.
            response (google.cloud.video.stitcher_v1.types.ListLiveAdTagDetailsResponse):
                The initial response object.
            retry (google.api_core.retry.Retry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = video_stitcher_service.ListLiveAdTagDetailsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[video_stitcher_service.ListLiveAdTagDetailsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __iter__(self) -> Iterator[ad_tag_details.LiveAdTagDetail]:
        for page in self.pages:
            yield from page.live_ad_tag_details

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListLiveAdTagDetailsAsyncPager:
    """A pager for iterating through ``list_live_ad_tag_details`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.video.stitcher_v1.types.ListLiveAdTagDetailsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``live_ad_tag_details`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListLiveAdTagDetails`` requests and continue to iterate
    through the ``live_ad_tag_details`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.video.stitcher_v1.types.ListLiveAdTagDetailsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[video_stitcher_service.ListLiveAdTagDetailsResponse]
        ],
        request: video_stitcher_service.ListLiveAdTagDetailsRequest,
        response: video_stitcher_service.ListLiveAdTagDetailsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.video.stitcher_v1.types.ListLiveAdTagDetailsRequest):
                The initial request object.
            response (google.cloud.video.stitcher_v1.types.ListLiveAdTagDetailsResponse):
                The initial response object.
            retry (google.api_core.retry.AsyncRetry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = video_stitcher_service.ListLiveAdTagDetailsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[video_stitcher_service.ListLiveAdTagDetailsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __aiter__(self) -> AsyncIterator[ad_tag_details.LiveAdTagDetail]:
        async def async_generator():
            async for page in self.pages:
                for response in page.live_ad_tag_details:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSlatesPager:
    """A pager for iterating through ``list_slates`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.video.stitcher_v1.types.ListSlatesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``slates`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSlates`` requests and continue to iterate
    through the ``slates`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.video.stitcher_v1.types.ListSlatesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., video_stitcher_service.ListSlatesResponse],
        request: video_stitcher_service.ListSlatesRequest,
        response: video_stitcher_service.ListSlatesResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.video.stitcher_v1.types.ListSlatesRequest):
                The initial request object.
            response (google.cloud.video.stitcher_v1.types.ListSlatesResponse):
                The initial response object.
            retry (google.api_core.retry.Retry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = video_stitcher_service.ListSlatesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[video_stitcher_service.ListSlatesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __iter__(self) -> Iterator[slates.Slate]:
        for page in self.pages:
            yield from page.slates

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListSlatesAsyncPager:
    """A pager for iterating through ``list_slates`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.video.stitcher_v1.types.ListSlatesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``slates`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSlates`` requests and continue to iterate
    through the ``slates`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.video.stitcher_v1.types.ListSlatesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[video_stitcher_service.ListSlatesResponse]],
        request: video_stitcher_service.ListSlatesRequest,
        response: video_stitcher_service.ListSlatesResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.video.stitcher_v1.types.ListSlatesRequest):
                The initial request object.
            response (google.cloud.video.stitcher_v1.types.ListSlatesResponse):
                The initial response object.
            retry (google.api_core.retry.AsyncRetry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = video_stitcher_service.ListSlatesRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[video_stitcher_service.ListSlatesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __aiter__(self) -> AsyncIterator[slates.Slate]:
        async def async_generator():
            async for page in self.pages:
                for response in page.slates:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListLiveConfigsPager:
    """A pager for iterating through ``list_live_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.video.stitcher_v1.types.ListLiveConfigsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``live_configs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListLiveConfigs`` requests and continue to iterate
    through the ``live_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.video.stitcher_v1.types.ListLiveConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., video_stitcher_service.ListLiveConfigsResponse],
        request: video_stitcher_service.ListLiveConfigsRequest,
        response: video_stitcher_service.ListLiveConfigsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.video.stitcher_v1.types.ListLiveConfigsRequest):
                The initial request object.
            response (google.cloud.video.stitcher_v1.types.ListLiveConfigsResponse):
                The initial response object.
            retry (google.api_core.retry.Retry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = video_stitcher_service.ListLiveConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[video_stitcher_service.ListLiveConfigsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __iter__(self) -> Iterator[live_configs.LiveConfig]:
        for page in self.pages:
            yield from page.live_configs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListLiveConfigsAsyncPager:
    """A pager for iterating through ``list_live_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.video.stitcher_v1.types.ListLiveConfigsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``live_configs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListLiveConfigs`` requests and continue to iterate
    through the ``live_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.video.stitcher_v1.types.ListLiveConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[
            ..., Awaitable[video_stitcher_service.ListLiveConfigsResponse]
        ],
        request: video_stitcher_service.ListLiveConfigsRequest,
        response: video_stitcher_service.ListLiveConfigsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.video.stitcher_v1.types.ListLiveConfigsRequest):
                The initial request object.
            response (google.cloud.video.stitcher_v1.types.ListLiveConfigsResponse):
                The initial response object.
            retry (google.api_core.retry.AsyncRetry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = video_stitcher_service.ListLiveConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[video_stitcher_service.ListLiveConfigsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __aiter__(self) -> AsyncIterator[live_configs.LiveConfig]:
        async def async_generator():
            async for page in self.pages:
                for response in page.live_configs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListVodConfigsPager:
    """A pager for iterating through ``list_vod_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.video.stitcher_v1.types.ListVodConfigsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``vod_configs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListVodConfigs`` requests and continue to iterate
    through the ``vod_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.video.stitcher_v1.types.ListVodConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., video_stitcher_service.ListVodConfigsResponse],
        request: video_stitcher_service.ListVodConfigsRequest,
        response: video_stitcher_service.ListVodConfigsResponse,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.video.stitcher_v1.types.ListVodConfigsRequest):
                The initial request object.
            response (google.cloud.video.stitcher_v1.types.ListVodConfigsResponse):
                The initial response object.
            retry (google.api_core.retry.Retry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = video_stitcher_service.ListVodConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[video_stitcher_service.ListVodConfigsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __iter__(self) -> Iterator[vod_configs.VodConfig]:
        for page in self.pages:
            yield from page.vod_configs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListVodConfigsAsyncPager:
    """A pager for iterating through ``list_vod_configs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.video.stitcher_v1.types.ListVodConfigsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``vod_configs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListVodConfigs`` requests and continue to iterate
    through the ``vod_configs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.video.stitcher_v1.types.ListVodConfigsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[video_stitcher_service.ListVodConfigsResponse]],
        request: video_stitcher_service.ListVodConfigsRequest,
        response: video_stitcher_service.ListVodConfigsResponse,
        *,
        retry: OptionalAsyncRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.video.stitcher_v1.types.ListVodConfigsRequest):
                The initial request object.
            response (google.cloud.video.stitcher_v1.types.ListVodConfigsResponse):
                The initial response object.
            retry (google.api_core.retry.AsyncRetry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        self._method = method
        self._request = video_stitcher_service.ListVodConfigsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(
        self,
    ) -> AsyncIterator[video_stitcher_service.ListVodConfigsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(
                self._request,
                retry=self._retry,
                timeout=self._timeout,
                metadata=self._metadata,
            )
            yield self._response

    def __aiter__(self) -> AsyncIterator[vod_configs.VodConfig]:
        async def async_generator():
            async for page in self.pages:
                for response in page.vod_configs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
