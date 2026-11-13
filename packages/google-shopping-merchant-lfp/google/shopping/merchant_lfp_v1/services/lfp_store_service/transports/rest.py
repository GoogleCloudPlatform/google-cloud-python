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

from google.shopping.merchant_lfp_v1._compat import transcode_request
from google.shopping.merchant_lfp_v1.types import lfpstore

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseLfpStoreServiceRestTransport

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


class LfpStoreServiceRestInterceptor:
    """Interceptor for LfpStoreService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the LfpStoreServiceRestTransport.

    .. code-block:: python
        class MyCustomLfpStoreServiceInterceptor(LfpStoreServiceRestInterceptor):
            def pre_delete_lfp_store(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_lfp_store(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_lfp_store(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_insert_lfp_store(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_insert_lfp_store(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_lfp_stores(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_lfp_stores(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = LfpStoreServiceRestTransport(interceptor=MyCustomLfpStoreServiceInterceptor())
        client = LfpStoreServiceClient(transport=transport)


    """

    def pre_delete_lfp_store(
        self,
        request: lfpstore.DeleteLfpStoreRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lfpstore.DeleteLfpStoreRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_lfp_store

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LfpStoreService server.
        """
        return request, metadata

    def pre_get_lfp_store(
        self,
        request: lfpstore.GetLfpStoreRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lfpstore.GetLfpStoreRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_lfp_store

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LfpStoreService server.
        """
        return request, metadata

    def post_get_lfp_store(self, response: lfpstore.LfpStore) -> lfpstore.LfpStore:
        """Post-rpc interceptor for get_lfp_store

        DEPRECATED. Please use the `post_get_lfp_store_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LfpStoreService server but before
        it is returned to user code. This `post_get_lfp_store` interceptor runs
        before the `post_get_lfp_store_with_metadata` interceptor.
        """
        return response

    def post_get_lfp_store_with_metadata(
        self,
        response: lfpstore.LfpStore,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lfpstore.LfpStore, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_lfp_store

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LfpStoreService server but before it is returned to user code.

        We recommend only using this `post_get_lfp_store_with_metadata`
        interceptor in new development instead of the `post_get_lfp_store` interceptor.
        When both interceptors are used, this `post_get_lfp_store_with_metadata` interceptor runs after the
        `post_get_lfp_store` interceptor. The (possibly modified) response returned by
        `post_get_lfp_store` will be passed to
        `post_get_lfp_store_with_metadata`.
        """
        return response, metadata

    def pre_insert_lfp_store(
        self,
        request: lfpstore.InsertLfpStoreRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lfpstore.InsertLfpStoreRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for insert_lfp_store

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LfpStoreService server.
        """
        return request, metadata

    def post_insert_lfp_store(self, response: lfpstore.LfpStore) -> lfpstore.LfpStore:
        """Post-rpc interceptor for insert_lfp_store

        DEPRECATED. Please use the `post_insert_lfp_store_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LfpStoreService server but before
        it is returned to user code. This `post_insert_lfp_store` interceptor runs
        before the `post_insert_lfp_store_with_metadata` interceptor.
        """
        return response

    def post_insert_lfp_store_with_metadata(
        self,
        response: lfpstore.LfpStore,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lfpstore.LfpStore, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for insert_lfp_store

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LfpStoreService server but before it is returned to user code.

        We recommend only using this `post_insert_lfp_store_with_metadata`
        interceptor in new development instead of the `post_insert_lfp_store` interceptor.
        When both interceptors are used, this `post_insert_lfp_store_with_metadata` interceptor runs after the
        `post_insert_lfp_store` interceptor. The (possibly modified) response returned by
        `post_insert_lfp_store` will be passed to
        `post_insert_lfp_store_with_metadata`.
        """
        return response, metadata

    def pre_list_lfp_stores(
        self,
        request: lfpstore.ListLfpStoresRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lfpstore.ListLfpStoresRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_lfp_stores

        Override in a subclass to manipulate the request or metadata
        before they are sent to the LfpStoreService server.
        """
        return request, metadata

    def post_list_lfp_stores(
        self, response: lfpstore.ListLfpStoresResponse
    ) -> lfpstore.ListLfpStoresResponse:
        """Post-rpc interceptor for list_lfp_stores

        DEPRECATED. Please use the `post_list_lfp_stores_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the LfpStoreService server but before
        it is returned to user code. This `post_list_lfp_stores` interceptor runs
        before the `post_list_lfp_stores_with_metadata` interceptor.
        """
        return response

    def post_list_lfp_stores_with_metadata(
        self,
        response: lfpstore.ListLfpStoresResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[lfpstore.ListLfpStoresResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_lfp_stores

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the LfpStoreService server but before it is returned to user code.

        We recommend only using this `post_list_lfp_stores_with_metadata`
        interceptor in new development instead of the `post_list_lfp_stores` interceptor.
        When both interceptors are used, this `post_list_lfp_stores_with_metadata` interceptor runs after the
        `post_list_lfp_stores` interceptor. The (possibly modified) response returned by
        `post_list_lfp_stores` will be passed to
        `post_list_lfp_stores_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class LfpStoreServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: LfpStoreServiceRestInterceptor


class LfpStoreServiceRestTransport(_BaseLfpStoreServiceRestTransport):
    """REST backend synchronous transport for LfpStoreService.

    Service for a `LFP
    partner <https://support.google.com/merchants/answer/7676652>`__ to
    submit local stores for a merchant.

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
        interceptor: Optional[LfpStoreServiceRestInterceptor] = None,
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
            interceptor (Optional[LfpStoreServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or LfpStoreServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _DeleteLfpStore(
        _BaseLfpStoreServiceRestTransport._BaseDeleteLfpStore, LfpStoreServiceRestStub
    ):
        def __hash__(self):
            return hash("LfpStoreServiceRestTransport.DeleteLfpStore")

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
            request: lfpstore.DeleteLfpStoreRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete lfp store method over HTTP.

            Args:
                request (~.lfpstore.DeleteLfpStoreRequest):
                    The request object. Request message for the
                DeleteLfpStore method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseLfpStoreServiceRestTransport._BaseDeleteLfpStore._get_http_options()
            request, metadata = self._interceptor.pre_delete_lfp_store(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLfpStoreServiceRestTransport._BaseDeleteLfpStore,
                    "_BaseDeleteLfpStore__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.lfp_v1.LfpStoreServiceClient.DeleteLfpStore",
                    extra={
                        "serviceName": "google.shopping.merchant.lfp.v1.LfpStoreService",
                        "rpcName": "DeleteLfpStore",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LfpStoreServiceRestTransport._DeleteLfpStore._get_response(
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

    class _GetLfpStore(
        _BaseLfpStoreServiceRestTransport._BaseGetLfpStore, LfpStoreServiceRestStub
    ):
        def __hash__(self):
            return hash("LfpStoreServiceRestTransport.GetLfpStore")

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
            request: lfpstore.GetLfpStoreRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> lfpstore.LfpStore:
            r"""Call the get lfp store method over HTTP.

            Args:
                request (~.lfpstore.GetLfpStoreRequest):
                    The request object. Request message for the ``GetLfpStore`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.lfpstore.LfpStore:
                    A store for the merchant. This will
                be used to match to a store under the
                Google Business Profile of the target
                merchant. If a matching store can't be
                found, the inventories or sales
                submitted with the store code will not
                be used.

            """

            http_options = (
                _BaseLfpStoreServiceRestTransport._BaseGetLfpStore._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_lfp_store(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLfpStoreServiceRestTransport._BaseGetLfpStore,
                    "_BaseGetLfpStore__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.lfp_v1.LfpStoreServiceClient.GetLfpStore",
                    extra={
                        "serviceName": "google.shopping.merchant.lfp.v1.LfpStoreService",
                        "rpcName": "GetLfpStore",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LfpStoreServiceRestTransport._GetLfpStore._get_response(
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
            resp = lfpstore.LfpStore()
            pb_resp = lfpstore.LfpStore.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_lfp_store(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_lfp_store_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = lfpstore.LfpStore.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.lfp_v1.LfpStoreServiceClient.get_lfp_store",
                    extra={
                        "serviceName": "google.shopping.merchant.lfp.v1.LfpStoreService",
                        "rpcName": "GetLfpStore",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _InsertLfpStore(
        _BaseLfpStoreServiceRestTransport._BaseInsertLfpStore, LfpStoreServiceRestStub
    ):
        def __hash__(self):
            return hash("LfpStoreServiceRestTransport.InsertLfpStore")

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
            request: lfpstore.InsertLfpStoreRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> lfpstore.LfpStore:
            r"""Call the insert lfp store method over HTTP.

            Args:
                request (~.lfpstore.InsertLfpStoreRequest):
                    The request object. Request message for the
                InsertLfpStore method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.lfpstore.LfpStore:
                    A store for the merchant. This will
                be used to match to a store under the
                Google Business Profile of the target
                merchant. If a matching store can't be
                found, the inventories or sales
                submitted with the store code will not
                be used.

            """

            http_options = _BaseLfpStoreServiceRestTransport._BaseInsertLfpStore._get_http_options()
            request, metadata = self._interceptor.pre_insert_lfp_store(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLfpStoreServiceRestTransport._BaseInsertLfpStore,
                    "_BaseInsertLfpStore__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.lfp_v1.LfpStoreServiceClient.InsertLfpStore",
                    extra={
                        "serviceName": "google.shopping.merchant.lfp.v1.LfpStoreService",
                        "rpcName": "InsertLfpStore",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LfpStoreServiceRestTransport._InsertLfpStore._get_response(
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
            resp = lfpstore.LfpStore()
            pb_resp = lfpstore.LfpStore.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_insert_lfp_store(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_insert_lfp_store_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = lfpstore.LfpStore.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.lfp_v1.LfpStoreServiceClient.insert_lfp_store",
                    extra={
                        "serviceName": "google.shopping.merchant.lfp.v1.LfpStoreService",
                        "rpcName": "InsertLfpStore",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListLfpStores(
        _BaseLfpStoreServiceRestTransport._BaseListLfpStores, LfpStoreServiceRestStub
    ):
        def __hash__(self):
            return hash("LfpStoreServiceRestTransport.ListLfpStores")

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
            request: lfpstore.ListLfpStoresRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> lfpstore.ListLfpStoresResponse:
            r"""Call the list lfp stores method over HTTP.

            Args:
                request (~.lfpstore.ListLfpStoresRequest):
                    The request object. Request message for the ListLfpStores
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.lfpstore.ListLfpStoresResponse:
                    Response message for the
                ListLfpStores method.

            """

            http_options = (
                _BaseLfpStoreServiceRestTransport._BaseListLfpStores._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_lfp_stores(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseLfpStoreServiceRestTransport._BaseListLfpStores,
                    "_BaseListLfpStores__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.lfp_v1.LfpStoreServiceClient.ListLfpStores",
                    extra={
                        "serviceName": "google.shopping.merchant.lfp.v1.LfpStoreService",
                        "rpcName": "ListLfpStores",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = LfpStoreServiceRestTransport._ListLfpStores._get_response(
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
            resp = lfpstore.ListLfpStoresResponse()
            pb_resp = lfpstore.ListLfpStoresResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_lfp_stores(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_lfp_stores_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = lfpstore.ListLfpStoresResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.lfp_v1.LfpStoreServiceClient.list_lfp_stores",
                    extra={
                        "serviceName": "google.shopping.merchant.lfp.v1.LfpStoreService",
                        "rpcName": "ListLfpStores",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def delete_lfp_store(
        self,
    ) -> Callable[[lfpstore.DeleteLfpStoreRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteLfpStore(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_lfp_store(
        self,
    ) -> Callable[[lfpstore.GetLfpStoreRequest], lfpstore.LfpStore]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetLfpStore(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def insert_lfp_store(
        self,
    ) -> Callable[[lfpstore.InsertLfpStoreRequest], lfpstore.LfpStore]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._InsertLfpStore(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_lfp_stores(
        self,
    ) -> Callable[[lfpstore.ListLfpStoresRequest], lfpstore.ListLfpStoresResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListLfpStores(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("LfpStoreServiceRestTransport",)
