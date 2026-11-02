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
from google.api_core import gapic_v1, operations_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.ads.admanager_v1._compat import transcode_request
from google.ads.admanager_v1.types import ad_review_center_ad_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseAdReviewCenterAdServiceRestTransport

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


class AdReviewCenterAdServiceRestInterceptor:
    """Interceptor for AdReviewCenterAdService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the AdReviewCenterAdServiceRestTransport.

    .. code-block:: python
        class MyCustomAdReviewCenterAdServiceInterceptor(AdReviewCenterAdServiceRestInterceptor):
            def pre_batch_allow_ad_review_center_ads(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_allow_ad_review_center_ads(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_apply_ad_review_center_custom_labels(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_apply_ad_review_center_custom_labels(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_block_ad_review_center_ads(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_block_ad_review_center_ads(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_ad_review_center_custom_labels(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_ad_review_center_custom_labels(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_search_ad_review_center_ads(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_search_ad_review_center_ads(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = AdReviewCenterAdServiceRestTransport(interceptor=MyCustomAdReviewCenterAdServiceInterceptor())
        client = AdReviewCenterAdServiceClient(transport=transport)


    """

    def pre_batch_allow_ad_review_center_ads(
        self,
        request: ad_review_center_ad_service.BatchAllowAdReviewCenterAdsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_review_center_ad_service.BatchAllowAdReviewCenterAdsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_allow_ad_review_center_ads

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AdReviewCenterAdService server.
        """
        return request, metadata

    def post_batch_allow_ad_review_center_ads(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for batch_allow_ad_review_center_ads

        DEPRECATED. Please use the `post_batch_allow_ad_review_center_ads_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AdReviewCenterAdService server but before
        it is returned to user code. This `post_batch_allow_ad_review_center_ads` interceptor runs
        before the `post_batch_allow_ad_review_center_ads_with_metadata` interceptor.
        """
        return response

    def post_batch_allow_ad_review_center_ads_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for batch_allow_ad_review_center_ads

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AdReviewCenterAdService server but before it is returned to user code.

        We recommend only using this `post_batch_allow_ad_review_center_ads_with_metadata`
        interceptor in new development instead of the `post_batch_allow_ad_review_center_ads` interceptor.
        When both interceptors are used, this `post_batch_allow_ad_review_center_ads_with_metadata` interceptor runs after the
        `post_batch_allow_ad_review_center_ads` interceptor. The (possibly modified) response returned by
        `post_batch_allow_ad_review_center_ads` will be passed to
        `post_batch_allow_ad_review_center_ads_with_metadata`.
        """
        return response, metadata

    def pre_batch_apply_ad_review_center_custom_labels(
        self,
        request: ad_review_center_ad_service.BatchApplyAdReviewCenterCustomLabelsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_review_center_ad_service.BatchApplyAdReviewCenterCustomLabelsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_apply_ad_review_center_custom_labels

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AdReviewCenterAdService server.
        """
        return request, metadata

    def post_batch_apply_ad_review_center_custom_labels(
        self,
        response: ad_review_center_ad_service.BatchApplyAdReviewCenterCustomLabelsResponse,
    ) -> ad_review_center_ad_service.BatchApplyAdReviewCenterCustomLabelsResponse:
        """Post-rpc interceptor for batch_apply_ad_review_center_custom_labels

        DEPRECATED. Please use the `post_batch_apply_ad_review_center_custom_labels_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AdReviewCenterAdService server but before
        it is returned to user code. This `post_batch_apply_ad_review_center_custom_labels` interceptor runs
        before the `post_batch_apply_ad_review_center_custom_labels_with_metadata` interceptor.
        """
        return response

    def post_batch_apply_ad_review_center_custom_labels_with_metadata(
        self,
        response: ad_review_center_ad_service.BatchApplyAdReviewCenterCustomLabelsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_review_center_ad_service.BatchApplyAdReviewCenterCustomLabelsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_apply_ad_review_center_custom_labels

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AdReviewCenterAdService server but before it is returned to user code.

        We recommend only using this `post_batch_apply_ad_review_center_custom_labels_with_metadata`
        interceptor in new development instead of the `post_batch_apply_ad_review_center_custom_labels` interceptor.
        When both interceptors are used, this `post_batch_apply_ad_review_center_custom_labels_with_metadata` interceptor runs after the
        `post_batch_apply_ad_review_center_custom_labels` interceptor. The (possibly modified) response returned by
        `post_batch_apply_ad_review_center_custom_labels` will be passed to
        `post_batch_apply_ad_review_center_custom_labels_with_metadata`.
        """
        return response, metadata

    def pre_batch_block_ad_review_center_ads(
        self,
        request: ad_review_center_ad_service.BatchBlockAdReviewCenterAdsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_review_center_ad_service.BatchBlockAdReviewCenterAdsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_block_ad_review_center_ads

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AdReviewCenterAdService server.
        """
        return request, metadata

    def post_batch_block_ad_review_center_ads(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for batch_block_ad_review_center_ads

        DEPRECATED. Please use the `post_batch_block_ad_review_center_ads_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AdReviewCenterAdService server but before
        it is returned to user code. This `post_batch_block_ad_review_center_ads` interceptor runs
        before the `post_batch_block_ad_review_center_ads_with_metadata` interceptor.
        """
        return response

    def post_batch_block_ad_review_center_ads_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for batch_block_ad_review_center_ads

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AdReviewCenterAdService server but before it is returned to user code.

        We recommend only using this `post_batch_block_ad_review_center_ads_with_metadata`
        interceptor in new development instead of the `post_batch_block_ad_review_center_ads` interceptor.
        When both interceptors are used, this `post_batch_block_ad_review_center_ads_with_metadata` interceptor runs after the
        `post_batch_block_ad_review_center_ads` interceptor. The (possibly modified) response returned by
        `post_batch_block_ad_review_center_ads` will be passed to
        `post_batch_block_ad_review_center_ads_with_metadata`.
        """
        return response, metadata

    def pre_fetch_ad_review_center_custom_labels(
        self,
        request: ad_review_center_ad_service.FetchAdReviewCenterCustomLabelsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_review_center_ad_service.FetchAdReviewCenterCustomLabelsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for fetch_ad_review_center_custom_labels

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AdReviewCenterAdService server.
        """
        return request, metadata

    def post_fetch_ad_review_center_custom_labels(
        self,
        response: ad_review_center_ad_service.FetchAdReviewCenterCustomLabelsResponse,
    ) -> ad_review_center_ad_service.FetchAdReviewCenterCustomLabelsResponse:
        """Post-rpc interceptor for fetch_ad_review_center_custom_labels

        DEPRECATED. Please use the `post_fetch_ad_review_center_custom_labels_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AdReviewCenterAdService server but before
        it is returned to user code. This `post_fetch_ad_review_center_custom_labels` interceptor runs
        before the `post_fetch_ad_review_center_custom_labels_with_metadata` interceptor.
        """
        return response

    def post_fetch_ad_review_center_custom_labels_with_metadata(
        self,
        response: ad_review_center_ad_service.FetchAdReviewCenterCustomLabelsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_review_center_ad_service.FetchAdReviewCenterCustomLabelsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for fetch_ad_review_center_custom_labels

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AdReviewCenterAdService server but before it is returned to user code.

        We recommend only using this `post_fetch_ad_review_center_custom_labels_with_metadata`
        interceptor in new development instead of the `post_fetch_ad_review_center_custom_labels` interceptor.
        When both interceptors are used, this `post_fetch_ad_review_center_custom_labels_with_metadata` interceptor runs after the
        `post_fetch_ad_review_center_custom_labels` interceptor. The (possibly modified) response returned by
        `post_fetch_ad_review_center_custom_labels` will be passed to
        `post_fetch_ad_review_center_custom_labels_with_metadata`.
        """
        return response, metadata

    def pre_search_ad_review_center_ads(
        self,
        request: ad_review_center_ad_service.SearchAdReviewCenterAdsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_review_center_ad_service.SearchAdReviewCenterAdsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for search_ad_review_center_ads

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AdReviewCenterAdService server.
        """
        return request, metadata

    def post_search_ad_review_center_ads(
        self, response: ad_review_center_ad_service.SearchAdReviewCenterAdsResponse
    ) -> ad_review_center_ad_service.SearchAdReviewCenterAdsResponse:
        """Post-rpc interceptor for search_ad_review_center_ads

        DEPRECATED. Please use the `post_search_ad_review_center_ads_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AdReviewCenterAdService server but before
        it is returned to user code. This `post_search_ad_review_center_ads` interceptor runs
        before the `post_search_ad_review_center_ads_with_metadata` interceptor.
        """
        return response

    def post_search_ad_review_center_ads_with_metadata(
        self,
        response: ad_review_center_ad_service.SearchAdReviewCenterAdsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ad_review_center_ad_service.SearchAdReviewCenterAdsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for search_ad_review_center_ads

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AdReviewCenterAdService server but before it is returned to user code.

        We recommend only using this `post_search_ad_review_center_ads_with_metadata`
        interceptor in new development instead of the `post_search_ad_review_center_ads` interceptor.
        When both interceptors are used, this `post_search_ad_review_center_ads_with_metadata` interceptor runs after the
        `post_search_ad_review_center_ads` interceptor. The (possibly modified) response returned by
        `post_search_ad_review_center_ads` will be passed to
        `post_search_ad_review_center_ads_with_metadata`.
        """
        return response, metadata

    def pre_cancel_operation(
        self,
        request: operations_pb2.CancelOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.CancelOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AdReviewCenterAdService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the AdReviewCenterAdService server but before
        it is returned to user code.
        """
        return response

    def pre_get_operation(
        self,
        request: operations_pb2.GetOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.GetOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AdReviewCenterAdService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the AdReviewCenterAdService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class AdReviewCenterAdServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: AdReviewCenterAdServiceRestInterceptor


class AdReviewCenterAdServiceRestTransport(_BaseAdReviewCenterAdServiceRestTransport):
    """REST backend synchronous transport for AdReviewCenterAdService.

    Provides methods for handling ``AdReviewCenterAd`` objects.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "admanager.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[AdReviewCenterAdServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'admanager.googleapis.com').
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
            interceptor (Optional[AdReviewCenterAdServiceRestInterceptor]): Interceptor used
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
        self._operations_client: Optional[operations_v1.AbstractOperationsClient] = None
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or AdReviewCenterAdServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    @property
    def operations_client(self) -> operations_v1.AbstractOperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Only create a new client if we do not already have one.
        if self._operations_client is None:
            http_options: Dict[str, List[Dict[str, str]]] = {
                "google.longrunning.Operations.CancelOperation": [
                    {
                        "method": "post",
                        "uri": "/v1/{name=networks/*/operations/reports/runs/*}:cancel",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=networks/*/operations/reports/runs/*}",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v1",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _BatchAllowAdReviewCenterAds(
        _BaseAdReviewCenterAdServiceRestTransport._BaseBatchAllowAdReviewCenterAds,
        AdReviewCenterAdServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "AdReviewCenterAdServiceRestTransport.BatchAllowAdReviewCenterAds"
            )

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
            request: ad_review_center_ad_service.BatchAllowAdReviewCenterAdsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the batch allow ad review
            center ads method over HTTP.

                Args:
                    request (~.ad_review_center_ad_service.BatchAllowAdReviewCenterAdsRequest):
                        The request object. Request object for ``BatchAllowAdReviewCenterAds``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.operations_pb2.Operation:
                        This resource represents a
                    long-running operation that is the
                    result of a network API call.

            """

            http_options = _BaseAdReviewCenterAdServiceRestTransport._BaseBatchAllowAdReviewCenterAds._get_http_options()
            request, metadata = self._interceptor.pre_batch_allow_ad_review_center_ads(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdReviewCenterAdServiceRestTransport._BaseBatchAllowAdReviewCenterAds,
                    "_BaseBatchAllowAdReviewCenterAds__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AdReviewCenterAdServiceClient.BatchAllowAdReviewCenterAds",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdReviewCenterAdService",
                        "rpcName": "BatchAllowAdReviewCenterAds",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdReviewCenterAdServiceRestTransport._BatchAllowAdReviewCenterAds._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_allow_ad_review_center_ads(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_allow_ad_review_center_ads_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.AdReviewCenterAdServiceClient.batch_allow_ad_review_center_ads",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdReviewCenterAdService",
                        "rpcName": "BatchAllowAdReviewCenterAds",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchApplyAdReviewCenterCustomLabels(
        _BaseAdReviewCenterAdServiceRestTransport._BaseBatchApplyAdReviewCenterCustomLabels,
        AdReviewCenterAdServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "AdReviewCenterAdServiceRestTransport.BatchApplyAdReviewCenterCustomLabels"
            )

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
            request: ad_review_center_ad_service.BatchApplyAdReviewCenterCustomLabelsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ad_review_center_ad_service.BatchApplyAdReviewCenterCustomLabelsResponse:
            r"""Call the batch apply ad review
            center custom labels method over HTTP.

                Args:
                    request (~.ad_review_center_ad_service.BatchApplyAdReviewCenterCustomLabelsRequest):
                        The request object. Request object for
                    ``BatchApplyAdReviewCenterCustomLabels`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.ad_review_center_ad_service.BatchApplyAdReviewCenterCustomLabelsResponse:
                        Response object for
                    ``BatchApplyAdReviewCenterCustomLabels`` method.

            """

            http_options = _BaseAdReviewCenterAdServiceRestTransport._BaseBatchApplyAdReviewCenterCustomLabels._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_apply_ad_review_center_custom_labels(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdReviewCenterAdServiceRestTransport._BaseBatchApplyAdReviewCenterCustomLabels,
                    "_BaseBatchApplyAdReviewCenterCustomLabels__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AdReviewCenterAdServiceClient.BatchApplyAdReviewCenterCustomLabels",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdReviewCenterAdService",
                        "rpcName": "BatchApplyAdReviewCenterCustomLabels",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdReviewCenterAdServiceRestTransport._BatchApplyAdReviewCenterCustomLabels._get_response(
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
            resp = ad_review_center_ad_service.BatchApplyAdReviewCenterCustomLabelsResponse()
            pb_resp = ad_review_center_ad_service.BatchApplyAdReviewCenterCustomLabelsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_apply_ad_review_center_custom_labels(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_apply_ad_review_center_custom_labels_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ad_review_center_ad_service.BatchApplyAdReviewCenterCustomLabelsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.AdReviewCenterAdServiceClient.batch_apply_ad_review_center_custom_labels",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdReviewCenterAdService",
                        "rpcName": "BatchApplyAdReviewCenterCustomLabels",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchBlockAdReviewCenterAds(
        _BaseAdReviewCenterAdServiceRestTransport._BaseBatchBlockAdReviewCenterAds,
        AdReviewCenterAdServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "AdReviewCenterAdServiceRestTransport.BatchBlockAdReviewCenterAds"
            )

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
            request: ad_review_center_ad_service.BatchBlockAdReviewCenterAdsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the batch block ad review
            center ads method over HTTP.

                Args:
                    request (~.ad_review_center_ad_service.BatchBlockAdReviewCenterAdsRequest):
                        The request object. Request object for ``BatchBlockAdReviewCenterAds``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.operations_pb2.Operation:
                        This resource represents a
                    long-running operation that is the
                    result of a network API call.

            """

            http_options = _BaseAdReviewCenterAdServiceRestTransport._BaseBatchBlockAdReviewCenterAds._get_http_options()
            request, metadata = self._interceptor.pre_batch_block_ad_review_center_ads(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdReviewCenterAdServiceRestTransport._BaseBatchBlockAdReviewCenterAds,
                    "_BaseBatchBlockAdReviewCenterAds__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AdReviewCenterAdServiceClient.BatchBlockAdReviewCenterAds",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdReviewCenterAdService",
                        "rpcName": "BatchBlockAdReviewCenterAds",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdReviewCenterAdServiceRestTransport._BatchBlockAdReviewCenterAds._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_block_ad_review_center_ads(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_block_ad_review_center_ads_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.AdReviewCenterAdServiceClient.batch_block_ad_review_center_ads",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdReviewCenterAdService",
                        "rpcName": "BatchBlockAdReviewCenterAds",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchAdReviewCenterCustomLabels(
        _BaseAdReviewCenterAdServiceRestTransport._BaseFetchAdReviewCenterCustomLabels,
        AdReviewCenterAdServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "AdReviewCenterAdServiceRestTransport.FetchAdReviewCenterCustomLabels"
            )

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
            request: ad_review_center_ad_service.FetchAdReviewCenterCustomLabelsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ad_review_center_ad_service.FetchAdReviewCenterCustomLabelsResponse:
            r"""Call the fetch ad review center
            custom labels method over HTTP.

                Args:
                    request (~.ad_review_center_ad_service.FetchAdReviewCenterCustomLabelsRequest):
                        The request object. Request object for ``FetchAdReviewCenterCustomLabels``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.ad_review_center_ad_service.FetchAdReviewCenterCustomLabelsResponse:
                        Response object for ``FetchAdReviewCenterCustomLabels``
                    method.

            """

            http_options = _BaseAdReviewCenterAdServiceRestTransport._BaseFetchAdReviewCenterCustomLabels._get_http_options()
            request, metadata = (
                self._interceptor.pre_fetch_ad_review_center_custom_labels(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdReviewCenterAdServiceRestTransport._BaseFetchAdReviewCenterCustomLabels,
                    "_BaseFetchAdReviewCenterCustomLabels__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AdReviewCenterAdServiceClient.FetchAdReviewCenterCustomLabels",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdReviewCenterAdService",
                        "rpcName": "FetchAdReviewCenterCustomLabels",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdReviewCenterAdServiceRestTransport._FetchAdReviewCenterCustomLabels._get_response(
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
            resp = ad_review_center_ad_service.FetchAdReviewCenterCustomLabelsResponse()
            pb_resp = (
                ad_review_center_ad_service.FetchAdReviewCenterCustomLabelsResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_ad_review_center_custom_labels(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_fetch_ad_review_center_custom_labels_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ad_review_center_ad_service.FetchAdReviewCenterCustomLabelsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.AdReviewCenterAdServiceClient.fetch_ad_review_center_custom_labels",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdReviewCenterAdService",
                        "rpcName": "FetchAdReviewCenterCustomLabels",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SearchAdReviewCenterAds(
        _BaseAdReviewCenterAdServiceRestTransport._BaseSearchAdReviewCenterAds,
        AdReviewCenterAdServiceRestStub,
    ):
        def __hash__(self):
            return hash("AdReviewCenterAdServiceRestTransport.SearchAdReviewCenterAds")

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
            request: ad_review_center_ad_service.SearchAdReviewCenterAdsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ad_review_center_ad_service.SearchAdReviewCenterAdsResponse:
            r"""Call the search ad review center
            ads method over HTTP.

                Args:
                    request (~.ad_review_center_ad_service.SearchAdReviewCenterAdsRequest):
                        The request object. Request object for ``SearchAdReviewCenterAds`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.ad_review_center_ad_service.SearchAdReviewCenterAdsResponse:
                        Response object for ``SearchAdReviewCenterAds`` method.
            """

            http_options = _BaseAdReviewCenterAdServiceRestTransport._BaseSearchAdReviewCenterAds._get_http_options()
            request, metadata = self._interceptor.pre_search_ad_review_center_ads(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdReviewCenterAdServiceRestTransport._BaseSearchAdReviewCenterAds,
                    "_BaseSearchAdReviewCenterAds__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.AdReviewCenterAdServiceClient.SearchAdReviewCenterAds",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdReviewCenterAdService",
                        "rpcName": "SearchAdReviewCenterAds",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdReviewCenterAdServiceRestTransport._SearchAdReviewCenterAds._get_response(
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
            resp = ad_review_center_ad_service.SearchAdReviewCenterAdsResponse()
            pb_resp = ad_review_center_ad_service.SearchAdReviewCenterAdsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_search_ad_review_center_ads(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_search_ad_review_center_ads_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ad_review_center_ad_service.SearchAdReviewCenterAdsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.AdReviewCenterAdServiceClient.search_ad_review_center_ads",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdReviewCenterAdService",
                        "rpcName": "SearchAdReviewCenterAds",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_allow_ad_review_center_ads(
        self,
    ) -> Callable[
        [ad_review_center_ad_service.BatchAllowAdReviewCenterAdsRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchAllowAdReviewCenterAds(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_apply_ad_review_center_custom_labels(
        self,
    ) -> Callable[
        [ad_review_center_ad_service.BatchApplyAdReviewCenterCustomLabelsRequest],
        ad_review_center_ad_service.BatchApplyAdReviewCenterCustomLabelsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchApplyAdReviewCenterCustomLabels(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_block_ad_review_center_ads(
        self,
    ) -> Callable[
        [ad_review_center_ad_service.BatchBlockAdReviewCenterAdsRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchBlockAdReviewCenterAds(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def fetch_ad_review_center_custom_labels(
        self,
    ) -> Callable[
        [ad_review_center_ad_service.FetchAdReviewCenterCustomLabelsRequest],
        ad_review_center_ad_service.FetchAdReviewCenterCustomLabelsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchAdReviewCenterCustomLabels(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def search_ad_review_center_ads(
        self,
    ) -> Callable[
        [ad_review_center_ad_service.SearchAdReviewCenterAdsRequest],
        ad_review_center_ad_service.SearchAdReviewCenterAdsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SearchAdReviewCenterAds(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseAdReviewCenterAdServiceRestTransport._BaseCancelOperation,
        AdReviewCenterAdServiceRestStub,
    ):
        def __hash__(self):
            return hash("AdReviewCenterAdServiceRestTransport.CancelOperation")

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
            request: operations_pb2.CancelOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> None:
            r"""Call the cancel operation method over HTTP.

            Args:
                request (operations_pb2.CancelOperationRequest):
                    The request object for CancelOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseAdReviewCenterAdServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdReviewCenterAdServiceRestTransport._BaseCancelOperation,
                    "_BaseCancelOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.ads.admanager_v1.AdReviewCenterAdServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdReviewCenterAdService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AdReviewCenterAdServiceRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseAdReviewCenterAdServiceRestTransport._BaseGetOperation,
        AdReviewCenterAdServiceRestStub,
    ):
        def __hash__(self):
            return hash("AdReviewCenterAdServiceRestTransport.GetOperation")

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
            request: operations_pb2.GetOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the get operation method over HTTP.

            Args:
                request (operations_pb2.GetOperationRequest):
                    The request object for GetOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                operations_pb2.Operation: Response from GetOperation method.
            """

            http_options = _BaseAdReviewCenterAdServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAdReviewCenterAdServiceRestTransport._BaseGetOperation,
                    "_BaseGetOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.ads.admanager_v1.AdReviewCenterAdServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdReviewCenterAdService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AdReviewCenterAdServiceRestTransport._GetOperation._get_response(
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

            content = response.content.decode("utf-8")
            resp = operations_pb2.Operation()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_operation(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.AdReviewCenterAdServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.AdReviewCenterAdService",
                        "rpcName": "GetOperation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("AdReviewCenterAdServiceRestTransport",)
