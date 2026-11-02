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
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.shopping.merchant_promotions_v1._compat import transcode_request
from google.shopping.merchant_promotions_v1.types import promotions

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BasePromotionsServiceRestTransport

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


class PromotionsServiceRestInterceptor:
    """Interceptor for PromotionsService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the PromotionsServiceRestTransport.

    .. code-block:: python
        class MyCustomPromotionsServiceInterceptor(PromotionsServiceRestInterceptor):
            def pre_get_promotion(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_promotion(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_insert_promotion(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_insert_promotion(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_promotions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_promotions(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = PromotionsServiceRestTransport(interceptor=MyCustomPromotionsServiceInterceptor())
        client = PromotionsServiceClient(transport=transport)


    """

    def pre_get_promotion(
        self,
        request: promotions.GetPromotionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[promotions.GetPromotionRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_promotion

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PromotionsService server.
        """
        return request, metadata

    def post_get_promotion(
        self, response: promotions.Promotion
    ) -> promotions.Promotion:
        """Post-rpc interceptor for get_promotion

        DEPRECATED. Please use the `post_get_promotion_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the PromotionsService server but before
        it is returned to user code. This `post_get_promotion` interceptor runs
        before the `post_get_promotion_with_metadata` interceptor.
        """
        return response

    def post_get_promotion_with_metadata(
        self,
        response: promotions.Promotion,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[promotions.Promotion, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_promotion

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the PromotionsService server but before it is returned to user code.

        We recommend only using this `post_get_promotion_with_metadata`
        interceptor in new development instead of the `post_get_promotion` interceptor.
        When both interceptors are used, this `post_get_promotion_with_metadata` interceptor runs after the
        `post_get_promotion` interceptor. The (possibly modified) response returned by
        `post_get_promotion` will be passed to
        `post_get_promotion_with_metadata`.
        """
        return response, metadata

    def pre_insert_promotion(
        self,
        request: promotions.InsertPromotionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        promotions.InsertPromotionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for insert_promotion

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PromotionsService server.
        """
        return request, metadata

    def post_insert_promotion(
        self, response: promotions.Promotion
    ) -> promotions.Promotion:
        """Post-rpc interceptor for insert_promotion

        DEPRECATED. Please use the `post_insert_promotion_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the PromotionsService server but before
        it is returned to user code. This `post_insert_promotion` interceptor runs
        before the `post_insert_promotion_with_metadata` interceptor.
        """
        return response

    def post_insert_promotion_with_metadata(
        self,
        response: promotions.Promotion,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[promotions.Promotion, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for insert_promotion

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the PromotionsService server but before it is returned to user code.

        We recommend only using this `post_insert_promotion_with_metadata`
        interceptor in new development instead of the `post_insert_promotion` interceptor.
        When both interceptors are used, this `post_insert_promotion_with_metadata` interceptor runs after the
        `post_insert_promotion` interceptor. The (possibly modified) response returned by
        `post_insert_promotion` will be passed to
        `post_insert_promotion_with_metadata`.
        """
        return response, metadata

    def pre_list_promotions(
        self,
        request: promotions.ListPromotionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        promotions.ListPromotionsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_promotions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the PromotionsService server.
        """
        return request, metadata

    def post_list_promotions(
        self, response: promotions.ListPromotionsResponse
    ) -> promotions.ListPromotionsResponse:
        """Post-rpc interceptor for list_promotions

        DEPRECATED. Please use the `post_list_promotions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the PromotionsService server but before
        it is returned to user code. This `post_list_promotions` interceptor runs
        before the `post_list_promotions_with_metadata` interceptor.
        """
        return response

    def post_list_promotions_with_metadata(
        self,
        response: promotions.ListPromotionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        promotions.ListPromotionsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_promotions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the PromotionsService server but before it is returned to user code.

        We recommend only using this `post_list_promotions_with_metadata`
        interceptor in new development instead of the `post_list_promotions` interceptor.
        When both interceptors are used, this `post_list_promotions_with_metadata` interceptor runs after the
        `post_list_promotions` interceptor. The (possibly modified) response returned by
        `post_list_promotions` will be passed to
        `post_list_promotions_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class PromotionsServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: PromotionsServiceRestInterceptor


class PromotionsServiceRestTransport(_BasePromotionsServiceRestTransport):
    """REST backend synchronous transport for PromotionsService.

    Service to manage promotions for products.

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
        interceptor: Optional[PromotionsServiceRestInterceptor] = None,
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
            interceptor (Optional[PromotionsServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or PromotionsServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _GetPromotion(
        _BasePromotionsServiceRestTransport._BaseGetPromotion, PromotionsServiceRestStub
    ):
        def __hash__(self):
            return hash("PromotionsServiceRestTransport.GetPromotion")

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
            request: promotions.GetPromotionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> promotions.Promotion:
            r"""Call the get promotion method over HTTP.

            Args:
                request (~.promotions.GetPromotionRequest):
                    The request object. Request message for the ``GetPromotion`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.promotions.Promotion:
                    Represents a promotion. See the following articles for
                more details.

                Required promotion input attributes to pass data
                validation checks are primarily defined below:

                - `Promotions data
                  specification <https://support.google.com/merchants/answer/2906014>`__
                - `Local promotions data
                  specification <https://support.google.com/merchants/answer/10146130>`__

                After inserting, updating a promotion input, it may take
                several minutes before the final promotion can be
                retrieved.

            """

            http_options = _BasePromotionsServiceRestTransport._BaseGetPromotion._get_http_options()
            request, metadata = self._interceptor.pre_get_promotion(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePromotionsServiceRestTransport._BaseGetPromotion,
                    "_BaseGetPromotion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.promotions_v1.PromotionsServiceClient.GetPromotion",
                    extra={
                        "serviceName": "google.shopping.merchant.promotions.v1.PromotionsService",
                        "rpcName": "GetPromotion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PromotionsServiceRestTransport._GetPromotion._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = promotions.Promotion()
            pb_resp = promotions.Promotion.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_promotion(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_promotion_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = promotions.Promotion.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.promotions_v1.PromotionsServiceClient.get_promotion",
                    extra={
                        "serviceName": "google.shopping.merchant.promotions.v1.PromotionsService",
                        "rpcName": "GetPromotion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _InsertPromotion(
        _BasePromotionsServiceRestTransport._BaseInsertPromotion,
        PromotionsServiceRestStub,
    ):
        def __hash__(self):
            return hash("PromotionsServiceRestTransport.InsertPromotion")

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
            request: promotions.InsertPromotionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> promotions.Promotion:
            r"""Call the insert promotion method over HTTP.

            Args:
                request (~.promotions.InsertPromotionRequest):
                    The request object. Request message for the ``InsertPromotion`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.promotions.Promotion:
                    Represents a promotion. See the following articles for
                more details.

                Required promotion input attributes to pass data
                validation checks are primarily defined below:

                - `Promotions data
                  specification <https://support.google.com/merchants/answer/2906014>`__
                - `Local promotions data
                  specification <https://support.google.com/merchants/answer/10146130>`__

                After inserting, updating a promotion input, it may take
                several minutes before the final promotion can be
                retrieved.

            """

            http_options = _BasePromotionsServiceRestTransport._BaseInsertPromotion._get_http_options()
            request, metadata = self._interceptor.pre_insert_promotion(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePromotionsServiceRestTransport._BaseInsertPromotion,
                    "_BaseInsertPromotion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.promotions_v1.PromotionsServiceClient.InsertPromotion",
                    extra={
                        "serviceName": "google.shopping.merchant.promotions.v1.PromotionsService",
                        "rpcName": "InsertPromotion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PromotionsServiceRestTransport._InsertPromotion._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = promotions.Promotion()
            pb_resp = promotions.Promotion.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_insert_promotion(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_insert_promotion_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = promotions.Promotion.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.promotions_v1.PromotionsServiceClient.insert_promotion",
                    extra={
                        "serviceName": "google.shopping.merchant.promotions.v1.PromotionsService",
                        "rpcName": "InsertPromotion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPromotions(
        _BasePromotionsServiceRestTransport._BaseListPromotions,
        PromotionsServiceRestStub,
    ):
        def __hash__(self):
            return hash("PromotionsServiceRestTransport.ListPromotions")

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
            request: promotions.ListPromotionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> promotions.ListPromotionsResponse:
            r"""Call the list promotions method over HTTP.

            Args:
                request (~.promotions.ListPromotionsRequest):
                    The request object. Request message for the ``ListPromotions`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.promotions.ListPromotionsResponse:
                    Response message for the ``ListPromotions`` method.
            """

            http_options = _BasePromotionsServiceRestTransport._BaseListPromotions._get_http_options()
            request, metadata = self._interceptor.pre_list_promotions(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePromotionsServiceRestTransport._BaseListPromotions,
                    "_BaseListPromotions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.promotions_v1.PromotionsServiceClient.ListPromotions",
                    extra={
                        "serviceName": "google.shopping.merchant.promotions.v1.PromotionsService",
                        "rpcName": "ListPromotions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PromotionsServiceRestTransport._ListPromotions._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = promotions.ListPromotionsResponse()
            pb_resp = promotions.ListPromotionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_promotions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_promotions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = promotions.ListPromotionsResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.promotions_v1.PromotionsServiceClient.list_promotions",
                    extra={
                        "serviceName": "google.shopping.merchant.promotions.v1.PromotionsService",
                        "rpcName": "ListPromotions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def get_promotion(
        self,
    ) -> Callable[[promotions.GetPromotionRequest], promotions.Promotion]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetPromotion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def insert_promotion(
        self,
    ) -> Callable[[promotions.InsertPromotionRequest], promotions.Promotion]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._InsertPromotion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_promotions(
        self,
    ) -> Callable[
        [promotions.ListPromotionsRequest], promotions.ListPromotionsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPromotions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("PromotionsServiceRestTransport",)
