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

from google.shopping.merchant_accounts_v1beta._compat import transcode_request
from google.shopping.merchant_accounts_v1beta.types import termsofservice

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseTermsOfServiceServiceRestTransport

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


class TermsOfServiceServiceRestInterceptor:
    """Interceptor for TermsOfServiceService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the TermsOfServiceServiceRestTransport.

    .. code-block:: python
        class MyCustomTermsOfServiceServiceInterceptor(TermsOfServiceServiceRestInterceptor):
            def pre_accept_terms_of_service(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_terms_of_service(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_terms_of_service(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_retrieve_latest_terms_of_service(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_retrieve_latest_terms_of_service(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = TermsOfServiceServiceRestTransport(interceptor=MyCustomTermsOfServiceServiceInterceptor())
        client = TermsOfServiceServiceClient(transport=transport)


    """

    def pre_accept_terms_of_service(
        self,
        request: termsofservice.AcceptTermsOfServiceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        termsofservice.AcceptTermsOfServiceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for accept_terms_of_service

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TermsOfServiceService server.
        """
        return request, metadata

    def pre_get_terms_of_service(
        self,
        request: termsofservice.GetTermsOfServiceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        termsofservice.GetTermsOfServiceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_terms_of_service

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TermsOfServiceService server.
        """
        return request, metadata

    def post_get_terms_of_service(
        self, response: termsofservice.TermsOfService
    ) -> termsofservice.TermsOfService:
        """Post-rpc interceptor for get_terms_of_service

        DEPRECATED. Please use the `post_get_terms_of_service_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TermsOfServiceService server but before
        it is returned to user code. This `post_get_terms_of_service` interceptor runs
        before the `post_get_terms_of_service_with_metadata` interceptor.
        """
        return response

    def post_get_terms_of_service_with_metadata(
        self,
        response: termsofservice.TermsOfService,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[termsofservice.TermsOfService, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_terms_of_service

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TermsOfServiceService server but before it is returned to user code.

        We recommend only using this `post_get_terms_of_service_with_metadata`
        interceptor in new development instead of the `post_get_terms_of_service` interceptor.
        When both interceptors are used, this `post_get_terms_of_service_with_metadata` interceptor runs after the
        `post_get_terms_of_service` interceptor. The (possibly modified) response returned by
        `post_get_terms_of_service` will be passed to
        `post_get_terms_of_service_with_metadata`.
        """
        return response, metadata

    def pre_retrieve_latest_terms_of_service(
        self,
        request: termsofservice.RetrieveLatestTermsOfServiceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        termsofservice.RetrieveLatestTermsOfServiceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for retrieve_latest_terms_of_service

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TermsOfServiceService server.
        """
        return request, metadata

    def post_retrieve_latest_terms_of_service(
        self, response: termsofservice.TermsOfService
    ) -> termsofservice.TermsOfService:
        """Post-rpc interceptor for retrieve_latest_terms_of_service

        DEPRECATED. Please use the `post_retrieve_latest_terms_of_service_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TermsOfServiceService server but before
        it is returned to user code. This `post_retrieve_latest_terms_of_service` interceptor runs
        before the `post_retrieve_latest_terms_of_service_with_metadata` interceptor.
        """
        return response

    def post_retrieve_latest_terms_of_service_with_metadata(
        self,
        response: termsofservice.TermsOfService,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[termsofservice.TermsOfService, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for retrieve_latest_terms_of_service

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TermsOfServiceService server but before it is returned to user code.

        We recommend only using this `post_retrieve_latest_terms_of_service_with_metadata`
        interceptor in new development instead of the `post_retrieve_latest_terms_of_service` interceptor.
        When both interceptors are used, this `post_retrieve_latest_terms_of_service_with_metadata` interceptor runs after the
        `post_retrieve_latest_terms_of_service` interceptor. The (possibly modified) response returned by
        `post_retrieve_latest_terms_of_service` will be passed to
        `post_retrieve_latest_terms_of_service_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class TermsOfServiceServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: TermsOfServiceServiceRestInterceptor


class TermsOfServiceServiceRestTransport(_BaseTermsOfServiceServiceRestTransport):
    """REST backend synchronous transport for TermsOfServiceService.

    Service to support ``TermsOfService`` API.

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
        interceptor: Optional[TermsOfServiceServiceRestInterceptor] = None,
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
            interceptor (Optional[TermsOfServiceServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or TermsOfServiceServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _AcceptTermsOfService(
        _BaseTermsOfServiceServiceRestTransport._BaseAcceptTermsOfService,
        TermsOfServiceServiceRestStub,
    ):
        def __hash__(self):
            return hash("TermsOfServiceServiceRestTransport.AcceptTermsOfService")

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
            request: termsofservice.AcceptTermsOfServiceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the accept terms of service method over HTTP.

            Args:
                request (~.termsofservice.AcceptTermsOfServiceRequest):
                    The request object. Request message for the ``AcceptTermsOfService`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseTermsOfServiceServiceRestTransport._BaseAcceptTermsOfService._get_http_options()
            request, metadata = self._interceptor.pre_accept_terms_of_service(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTermsOfServiceServiceRestTransport._BaseAcceptTermsOfService,
                    "_BaseAcceptTermsOfService__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1beta.TermsOfServiceServiceClient.AcceptTermsOfService",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1beta.TermsOfServiceService",
                        "rpcName": "AcceptTermsOfService",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                TermsOfServiceServiceRestTransport._AcceptTermsOfService._get_response(
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

    class _GetTermsOfService(
        _BaseTermsOfServiceServiceRestTransport._BaseGetTermsOfService,
        TermsOfServiceServiceRestStub,
    ):
        def __hash__(self):
            return hash("TermsOfServiceServiceRestTransport.GetTermsOfService")

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
            request: termsofservice.GetTermsOfServiceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> termsofservice.TermsOfService:
            r"""Call the get terms of service method over HTTP.

            Args:
                request (~.termsofservice.GetTermsOfServiceRequest):
                    The request object. Request message for the ``GetTermsOfService`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.termsofservice.TermsOfService:
                    A ``TermsOfService``.
            """

            http_options = _BaseTermsOfServiceServiceRestTransport._BaseGetTermsOfService._get_http_options()
            request, metadata = self._interceptor.pre_get_terms_of_service(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTermsOfServiceServiceRestTransport._BaseGetTermsOfService,
                    "_BaseGetTermsOfService__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1beta.TermsOfServiceServiceClient.GetTermsOfService",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1beta.TermsOfServiceService",
                        "rpcName": "GetTermsOfService",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                TermsOfServiceServiceRestTransport._GetTermsOfService._get_response(
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
            resp = termsofservice.TermsOfService()
            pb_resp = termsofservice.TermsOfService.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_terms_of_service(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_terms_of_service_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = termsofservice.TermsOfService.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.accounts_v1beta.TermsOfServiceServiceClient.get_terms_of_service",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1beta.TermsOfServiceService",
                        "rpcName": "GetTermsOfService",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RetrieveLatestTermsOfService(
        _BaseTermsOfServiceServiceRestTransport._BaseRetrieveLatestTermsOfService,
        TermsOfServiceServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "TermsOfServiceServiceRestTransport.RetrieveLatestTermsOfService"
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
            request: termsofservice.RetrieveLatestTermsOfServiceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> termsofservice.TermsOfService:
            r"""Call the retrieve latest terms of
            service method over HTTP.

                Args:
                    request (~.termsofservice.RetrieveLatestTermsOfServiceRequest):
                        The request object. Request message for the ``RetrieveLatestTermsOfService``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.termsofservice.TermsOfService:
                        A ``TermsOfService``.
            """

            http_options = _BaseTermsOfServiceServiceRestTransport._BaseRetrieveLatestTermsOfService._get_http_options()
            request, metadata = self._interceptor.pre_retrieve_latest_terms_of_service(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTermsOfServiceServiceRestTransport._BaseRetrieveLatestTermsOfService,
                    "_BaseRetrieveLatestTermsOfService__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1beta.TermsOfServiceServiceClient.RetrieveLatestTermsOfService",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1beta.TermsOfServiceService",
                        "rpcName": "RetrieveLatestTermsOfService",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TermsOfServiceServiceRestTransport._RetrieveLatestTermsOfService._get_response(
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
            resp = termsofservice.TermsOfService()
            pb_resp = termsofservice.TermsOfService.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_retrieve_latest_terms_of_service(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_retrieve_latest_terms_of_service_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = termsofservice.TermsOfService.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.accounts_v1beta.TermsOfServiceServiceClient.retrieve_latest_terms_of_service",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1beta.TermsOfServiceService",
                        "rpcName": "RetrieveLatestTermsOfService",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def accept_terms_of_service(
        self,
    ) -> Callable[[termsofservice.AcceptTermsOfServiceRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AcceptTermsOfService(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_terms_of_service(
        self,
    ) -> Callable[
        [termsofservice.GetTermsOfServiceRequest], termsofservice.TermsOfService
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTermsOfService(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def retrieve_latest_terms_of_service(
        self,
    ) -> Callable[
        [termsofservice.RetrieveLatestTermsOfServiceRequest],
        termsofservice.TermsOfService,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RetrieveLatestTermsOfService(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("TermsOfServiceServiceRestTransport",)
