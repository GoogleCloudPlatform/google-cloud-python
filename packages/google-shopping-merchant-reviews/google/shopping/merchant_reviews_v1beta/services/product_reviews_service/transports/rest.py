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
import dataclasses
import json  # type: ignore
import logging
import warnings
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union

import google.protobuf
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.shopping.merchant_reviews_v1beta._compat import transcode_request
from google.shopping.merchant_reviews_v1beta.types import productreviews

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseProductReviewsServiceRestTransport

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object, None]  # type: ignore

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = logging.getLogger(__name__)

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=f"requests@{requests_version}",
)

DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class ProductReviewsServiceRestInterceptor:
    """Interceptor for ProductReviewsService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ProductReviewsServiceRestTransport.

    .. code-block:: python
        class MyCustomProductReviewsServiceInterceptor(ProductReviewsServiceRestInterceptor):
            def pre_delete_product_review(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_product_review(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_product_review(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_insert_product_review(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_insert_product_review(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_product_reviews(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_product_reviews(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ProductReviewsServiceRestTransport(interceptor=MyCustomProductReviewsServiceInterceptor())
        client = ProductReviewsServiceClient(transport=transport)


    """

    def pre_delete_product_review(
        self,
        request: productreviews.DeleteProductReviewRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        productreviews.DeleteProductReviewRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_product_review

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProductReviewsService server.
        """
        return request, metadata

    def pre_get_product_review(
        self,
        request: productreviews.GetProductReviewRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        productreviews.GetProductReviewRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_product_review

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProductReviewsService server.
        """
        return request, metadata

    def post_get_product_review(
        self, response: productreviews.ProductReview
    ) -> productreviews.ProductReview:
        """Post-rpc interceptor for get_product_review

        DEPRECATED. Please use the `post_get_product_review_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProductReviewsService server but before
        it is returned to user code. This `post_get_product_review` interceptor runs
        before the `post_get_product_review_with_metadata` interceptor.
        """
        return response

    def post_get_product_review_with_metadata(
        self,
        response: productreviews.ProductReview,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[productreviews.ProductReview, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_product_review

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProductReviewsService server but before it is returned to user code.

        We recommend only using this `post_get_product_review_with_metadata`
        interceptor in new development instead of the `post_get_product_review` interceptor.
        When both interceptors are used, this `post_get_product_review_with_metadata` interceptor runs after the
        `post_get_product_review` interceptor. The (possibly modified) response returned by
        `post_get_product_review` will be passed to
        `post_get_product_review_with_metadata`.
        """
        return response, metadata

    def pre_insert_product_review(
        self,
        request: productreviews.InsertProductReviewRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        productreviews.InsertProductReviewRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for insert_product_review

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProductReviewsService server.
        """
        return request, metadata

    def post_insert_product_review(
        self, response: productreviews.ProductReview
    ) -> productreviews.ProductReview:
        """Post-rpc interceptor for insert_product_review

        DEPRECATED. Please use the `post_insert_product_review_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProductReviewsService server but before
        it is returned to user code. This `post_insert_product_review` interceptor runs
        before the `post_insert_product_review_with_metadata` interceptor.
        """
        return response

    def post_insert_product_review_with_metadata(
        self,
        response: productreviews.ProductReview,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[productreviews.ProductReview, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for insert_product_review

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProductReviewsService server but before it is returned to user code.

        We recommend only using this `post_insert_product_review_with_metadata`
        interceptor in new development instead of the `post_insert_product_review` interceptor.
        When both interceptors are used, this `post_insert_product_review_with_metadata` interceptor runs after the
        `post_insert_product_review` interceptor. The (possibly modified) response returned by
        `post_insert_product_review` will be passed to
        `post_insert_product_review_with_metadata`.
        """
        return response, metadata

    def pre_list_product_reviews(
        self,
        request: productreviews.ListProductReviewsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        productreviews.ListProductReviewsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_product_reviews

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProductReviewsService server.
        """
        return request, metadata

    def post_list_product_reviews(
        self, response: productreviews.ListProductReviewsResponse
    ) -> productreviews.ListProductReviewsResponse:
        """Post-rpc interceptor for list_product_reviews

        DEPRECATED. Please use the `post_list_product_reviews_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProductReviewsService server but before
        it is returned to user code. This `post_list_product_reviews` interceptor runs
        before the `post_list_product_reviews_with_metadata` interceptor.
        """
        return response

    def post_list_product_reviews_with_metadata(
        self,
        response: productreviews.ListProductReviewsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        productreviews.ListProductReviewsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_product_reviews

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProductReviewsService server but before it is returned to user code.

        We recommend only using this `post_list_product_reviews_with_metadata`
        interceptor in new development instead of the `post_list_product_reviews` interceptor.
        When both interceptors are used, this `post_list_product_reviews_with_metadata` interceptor runs after the
        `post_list_product_reviews` interceptor. The (possibly modified) response returned by
        `post_list_product_reviews` will be passed to
        `post_list_product_reviews_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class ProductReviewsServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ProductReviewsServiceRestInterceptor


class ProductReviewsServiceRestTransport(_BaseProductReviewsServiceRestTransport):
    """REST backend synchronous transport for ProductReviewsService.

    Service to manage product reviews.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "merchantapi.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[ProductReviewsServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'merchantapi.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.

            credentials_file (Optional[str]): Deprecated. A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided. This argument will be
                removed in the next major version of this library.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Callable[[], Tuple[bytes, bytes]]): Client
                certificate to configure mutual TLS HTTP channel. It is ignored
                if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            url_scheme: the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
            interceptor (Optional[ProductReviewsServiceRestInterceptor]): Interceptor used
                to manipulate requests, request metadata, and responses.
            api_audience (Optional[str]): The intended audience for the API calls
                to the service that will be set when using certain 3rd party
                authentication flows. Audience is typically a resource identifier.
                If not set, the host value will be used as a default.
        """
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            url_scheme=url_scheme,
            api_audience=api_audience,
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST
        )
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or ProductReviewsServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _DeleteProductReview(
        _BaseProductReviewsServiceRestTransport._BaseDeleteProductReview,
        ProductReviewsServiceRestStub,
    ):
        def __hash__(self):
            return hash("ProductReviewsServiceRestTransport.DeleteProductReview")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: productreviews.DeleteProductReviewRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete product review method over HTTP.

            Args:
                request (~.productreviews.DeleteProductReviewRequest):
                    The request object. Request message for the ``DeleteProductReview`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseProductReviewsServiceRestTransport._BaseDeleteProductReview._get_http_options()
            request, metadata = self._interceptor.pre_delete_product_review(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProductReviewsServiceRestTransport._BaseDeleteProductReview,
                    "_BaseDeleteProductReview__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.shopping.merchant.reviews_v1beta.ProductReviewsServiceClient.DeleteProductReview",
                    extra={
                        "serviceName": "google.shopping.merchant.reviews.v1beta.ProductReviewsService",
                        "rpcName": "DeleteProductReview",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ProductReviewsServiceRestTransport._DeleteProductReview._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _GetProductReview(
        _BaseProductReviewsServiceRestTransport._BaseGetProductReview,
        ProductReviewsServiceRestStub,
    ):
        def __hash__(self):
            return hash("ProductReviewsServiceRestTransport.GetProductReview")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: productreviews.GetProductReviewRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> productreviews.ProductReview:
            r"""Call the get product review method over HTTP.

            Args:
                request (~.productreviews.GetProductReviewRequest):
                    The request object. Request message for the
                GetProductReview method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.productreviews.ProductReview:
                    A review for a product. For more information, see
                `Introduction to Product Review
                Feeds <https://developers.google.com/product-review-feeds>`__

            """

            http_options = _BaseProductReviewsServiceRestTransport._BaseGetProductReview._get_http_options()
            request, metadata = self._interceptor.pre_get_product_review(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProductReviewsServiceRestTransport._BaseGetProductReview,
                    "_BaseGetProductReview__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.shopping.merchant.reviews_v1beta.ProductReviewsServiceClient.GetProductReview",
                    extra={
                        "serviceName": "google.shopping.merchant.reviews.v1beta.ProductReviewsService",
                        "rpcName": "GetProductReview",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ProductReviewsServiceRestTransport._GetProductReview._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = productreviews.ProductReview()
            pb_resp = productreviews.ProductReview.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_product_review(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_product_review_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = productreviews.ProductReview.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.reviews_v1beta.ProductReviewsServiceClient.get_product_review",
                    extra={
                        "serviceName": "google.shopping.merchant.reviews.v1beta.ProductReviewsService",
                        "rpcName": "GetProductReview",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _InsertProductReview(
        _BaseProductReviewsServiceRestTransport._BaseInsertProductReview,
        ProductReviewsServiceRestStub,
    ):
        def __hash__(self):
            return hash("ProductReviewsServiceRestTransport.InsertProductReview")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: productreviews.InsertProductReviewRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> productreviews.ProductReview:
            r"""Call the insert product review method over HTTP.

            Args:
                request (~.productreviews.InsertProductReviewRequest):
                    The request object. Request message for the ``InsertProductReview`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.productreviews.ProductReview:
                    A review for a product. For more information, see
                `Introduction to Product Review
                Feeds <https://developers.google.com/product-review-feeds>`__

            """

            http_options = _BaseProductReviewsServiceRestTransport._BaseInsertProductReview._get_http_options()
            request, metadata = self._interceptor.pre_insert_product_review(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProductReviewsServiceRestTransport._BaseInsertProductReview,
                    "_BaseInsertProductReview__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.shopping.merchant.reviews_v1beta.ProductReviewsServiceClient.InsertProductReview",
                    extra={
                        "serviceName": "google.shopping.merchant.reviews.v1beta.ProductReviewsService",
                        "rpcName": "InsertProductReview",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ProductReviewsServiceRestTransport._InsertProductReview._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = productreviews.ProductReview()
            pb_resp = productreviews.ProductReview.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_insert_product_review(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_insert_product_review_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = productreviews.ProductReview.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.reviews_v1beta.ProductReviewsServiceClient.insert_product_review",
                    extra={
                        "serviceName": "google.shopping.merchant.reviews.v1beta.ProductReviewsService",
                        "rpcName": "InsertProductReview",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListProductReviews(
        _BaseProductReviewsServiceRestTransport._BaseListProductReviews,
        ProductReviewsServiceRestStub,
    ):
        def __hash__(self):
            return hash("ProductReviewsServiceRestTransport.ListProductReviews")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: productreviews.ListProductReviewsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> productreviews.ListProductReviewsResponse:
            r"""Call the list product reviews method over HTTP.

            Args:
                request (~.productreviews.ListProductReviewsRequest):
                    The request object. Request message for the
                ListProductReviews method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.productreviews.ListProductReviewsResponse:
                    response message for the
                ListProductReviews method.

            """

            http_options = _BaseProductReviewsServiceRestTransport._BaseListProductReviews._get_http_options()
            request, metadata = self._interceptor.pre_list_product_reviews(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProductReviewsServiceRestTransport._BaseListProductReviews,
                    "_BaseListProductReviews__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.shopping.merchant.reviews_v1beta.ProductReviewsServiceClient.ListProductReviews",
                    extra={
                        "serviceName": "google.shopping.merchant.reviews.v1beta.ProductReviewsService",
                        "rpcName": "ListProductReviews",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ProductReviewsServiceRestTransport._ListProductReviews._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = productreviews.ListProductReviewsResponse()
            pb_resp = productreviews.ListProductReviewsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_product_reviews(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_product_reviews_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        productreviews.ListProductReviewsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.reviews_v1beta.ProductReviewsServiceClient.list_product_reviews",
                    extra={
                        "serviceName": "google.shopping.merchant.reviews.v1beta.ProductReviewsService",
                        "rpcName": "ListProductReviews",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def delete_product_review(
        self,
    ) -> Callable[[productreviews.DeleteProductReviewRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteProductReview(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_product_review(
        self,
    ) -> Callable[
        [productreviews.GetProductReviewRequest], productreviews.ProductReview
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetProductReview(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def insert_product_review(
        self,
    ) -> Callable[
        [productreviews.InsertProductReviewRequest], productreviews.ProductReview
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._InsertProductReview(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_product_reviews(
        self,
    ) -> Callable[
        [productreviews.ListProductReviewsRequest],
        productreviews.ListProductReviewsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListProductReviews(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("ProductReviewsServiceRestTransport",)
