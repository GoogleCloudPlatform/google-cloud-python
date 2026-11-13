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

from google.shopping.merchant_accounts_v1._compat import transcode_request
from google.shopping.merchant_accounts_v1.types import developerregistration

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseDeveloperRegistrationServiceRestTransport

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


class DeveloperRegistrationServiceRestInterceptor:
    """Interceptor for DeveloperRegistrationService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the DeveloperRegistrationServiceRestTransport.

    .. code-block:: python
        class MyCustomDeveloperRegistrationServiceInterceptor(DeveloperRegistrationServiceRestInterceptor):
            def pre_get_account_for_gcp_registration(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_account_for_gcp_registration(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_developer_registration(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_developer_registration(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_register_gcp(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_register_gcp(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_unregister_gcp(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

        transport = DeveloperRegistrationServiceRestTransport(interceptor=MyCustomDeveloperRegistrationServiceInterceptor())
        client = DeveloperRegistrationServiceClient(transport=transport)


    """

    def pre_get_account_for_gcp_registration(
        self,
        request: empty_pb2.Empty,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[empty_pb2.Empty, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_account_for_gcp_registration

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperRegistrationService server.
        """
        return request, metadata

    def post_get_account_for_gcp_registration(
        self, response: developerregistration.GetAccountForGcpRegistrationResponse
    ) -> developerregistration.GetAccountForGcpRegistrationResponse:
        """Post-rpc interceptor for get_account_for_gcp_registration

        DEPRECATED. Please use the `post_get_account_for_gcp_registration_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeveloperRegistrationService server but before
        it is returned to user code. This `post_get_account_for_gcp_registration` interceptor runs
        before the `post_get_account_for_gcp_registration_with_metadata` interceptor.
        """
        return response

    def post_get_account_for_gcp_registration_with_metadata(
        self,
        response: developerregistration.GetAccountForGcpRegistrationResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developerregistration.GetAccountForGcpRegistrationResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_account_for_gcp_registration

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeveloperRegistrationService server but before it is returned to user code.

        We recommend only using this `post_get_account_for_gcp_registration_with_metadata`
        interceptor in new development instead of the `post_get_account_for_gcp_registration` interceptor.
        When both interceptors are used, this `post_get_account_for_gcp_registration_with_metadata` interceptor runs after the
        `post_get_account_for_gcp_registration` interceptor. The (possibly modified) response returned by
        `post_get_account_for_gcp_registration` will be passed to
        `post_get_account_for_gcp_registration_with_metadata`.
        """
        return response, metadata

    def pre_get_developer_registration(
        self,
        request: developerregistration.GetDeveloperRegistrationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developerregistration.GetDeveloperRegistrationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_developer_registration

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperRegistrationService server.
        """
        return request, metadata

    def post_get_developer_registration(
        self, response: developerregistration.DeveloperRegistration
    ) -> developerregistration.DeveloperRegistration:
        """Post-rpc interceptor for get_developer_registration

        DEPRECATED. Please use the `post_get_developer_registration_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeveloperRegistrationService server but before
        it is returned to user code. This `post_get_developer_registration` interceptor runs
        before the `post_get_developer_registration_with_metadata` interceptor.
        """
        return response

    def post_get_developer_registration_with_metadata(
        self,
        response: developerregistration.DeveloperRegistration,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developerregistration.DeveloperRegistration,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_developer_registration

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeveloperRegistrationService server but before it is returned to user code.

        We recommend only using this `post_get_developer_registration_with_metadata`
        interceptor in new development instead of the `post_get_developer_registration` interceptor.
        When both interceptors are used, this `post_get_developer_registration_with_metadata` interceptor runs after the
        `post_get_developer_registration` interceptor. The (possibly modified) response returned by
        `post_get_developer_registration` will be passed to
        `post_get_developer_registration_with_metadata`.
        """
        return response, metadata

    def pre_register_gcp(
        self,
        request: developerregistration.RegisterGcpRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developerregistration.RegisterGcpRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for register_gcp

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperRegistrationService server.
        """
        return request, metadata

    def post_register_gcp(
        self, response: developerregistration.DeveloperRegistration
    ) -> developerregistration.DeveloperRegistration:
        """Post-rpc interceptor for register_gcp

        DEPRECATED. Please use the `post_register_gcp_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeveloperRegistrationService server but before
        it is returned to user code. This `post_register_gcp` interceptor runs
        before the `post_register_gcp_with_metadata` interceptor.
        """
        return response

    def post_register_gcp_with_metadata(
        self,
        response: developerregistration.DeveloperRegistration,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developerregistration.DeveloperRegistration,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for register_gcp

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeveloperRegistrationService server but before it is returned to user code.

        We recommend only using this `post_register_gcp_with_metadata`
        interceptor in new development instead of the `post_register_gcp` interceptor.
        When both interceptors are used, this `post_register_gcp_with_metadata` interceptor runs after the
        `post_register_gcp` interceptor. The (possibly modified) response returned by
        `post_register_gcp` will be passed to
        `post_register_gcp_with_metadata`.
        """
        return response, metadata

    def pre_unregister_gcp(
        self,
        request: developerregistration.UnregisterGcpRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        developerregistration.UnregisterGcpRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for unregister_gcp

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeveloperRegistrationService server.
        """
        return request, metadata


@dataclasses.dataclass
class DeveloperRegistrationServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: DeveloperRegistrationServiceRestInterceptor


class DeveloperRegistrationServiceRestTransport(
    _BaseDeveloperRegistrationServiceRestTransport
):
    """REST backend synchronous transport for DeveloperRegistrationService.

    Service to access Developer Registration.

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
        interceptor: Optional[DeveloperRegistrationServiceRestInterceptor] = None,
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
            interceptor (Optional[DeveloperRegistrationServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or DeveloperRegistrationServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _GetAccountForGcpRegistration(
        _BaseDeveloperRegistrationServiceRestTransport._BaseGetAccountForGcpRegistration,
        DeveloperRegistrationServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "DeveloperRegistrationServiceRestTransport.GetAccountForGcpRegistration"
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
            request: empty_pb2.Empty,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> developerregistration.GetAccountForGcpRegistrationResponse:
            r"""Call the get account for gcp
            registration method over HTTP.

                Args:
                    request (~.empty_pb2.Empty):
                        The request object. A generic empty message that you can
                    re-use to avoid defining duplicated
                    empty messages in your APIs. A typical
                    example is to use it as the request or
                    the response type of an API method. For
                    instance:

                        service Foo {
                          rpc Bar(google.protobuf.Empty)
                    returns (google.protobuf.Empty);     }
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.developerregistration.GetAccountForGcpRegistrationResponse:
                        Response message for the
                    GetAccountForGcpRegistration method.

            """

            http_options = _BaseDeveloperRegistrationServiceRestTransport._BaseGetAccountForGcpRegistration._get_http_options()
            request, metadata = self._interceptor.pre_get_account_for_gcp_registration(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperRegistrationServiceRestTransport._BaseGetAccountForGcpRegistration,
                    "_BaseGetAccountForGcpRegistration__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1.DeveloperRegistrationServiceClient.GetAccountForGcpRegistration",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.DeveloperRegistrationService",
                        "rpcName": "GetAccountForGcpRegistration",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeveloperRegistrationServiceRestTransport._GetAccountForGcpRegistration._get_response(
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
            resp = developerregistration.GetAccountForGcpRegistrationResponse()
            pb_resp = developerregistration.GetAccountForGcpRegistrationResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_account_for_gcp_registration(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_account_for_gcp_registration_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = developerregistration.GetAccountForGcpRegistrationResponse.to_json(
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
                    "Received response for google.shopping.merchant.accounts_v1.DeveloperRegistrationServiceClient.get_account_for_gcp_registration",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.DeveloperRegistrationService",
                        "rpcName": "GetAccountForGcpRegistration",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDeveloperRegistration(
        _BaseDeveloperRegistrationServiceRestTransport._BaseGetDeveloperRegistration,
        DeveloperRegistrationServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "DeveloperRegistrationServiceRestTransport.GetDeveloperRegistration"
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
            request: developerregistration.GetDeveloperRegistrationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> developerregistration.DeveloperRegistration:
            r"""Call the get developer
            registration method over HTTP.

                Args:
                    request (~.developerregistration.GetDeveloperRegistrationRequest):
                        The request object. Request message for the
                    GetDeveloperRegistration method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.developerregistration.DeveloperRegistration:
                        Represents a developer registration
                    owned by a Merchant account.

            """

            http_options = _BaseDeveloperRegistrationServiceRestTransport._BaseGetDeveloperRegistration._get_http_options()
            request, metadata = self._interceptor.pre_get_developer_registration(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperRegistrationServiceRestTransport._BaseGetDeveloperRegistration,
                    "_BaseGetDeveloperRegistration__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1.DeveloperRegistrationServiceClient.GetDeveloperRegistration",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.DeveloperRegistrationService",
                        "rpcName": "GetDeveloperRegistration",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeveloperRegistrationServiceRestTransport._GetDeveloperRegistration._get_response(
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
            resp = developerregistration.DeveloperRegistration()
            pb_resp = developerregistration.DeveloperRegistration.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_developer_registration(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_developer_registration_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        developerregistration.DeveloperRegistration.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.accounts_v1.DeveloperRegistrationServiceClient.get_developer_registration",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.DeveloperRegistrationService",
                        "rpcName": "GetDeveloperRegistration",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RegisterGcp(
        _BaseDeveloperRegistrationServiceRestTransport._BaseRegisterGcp,
        DeveloperRegistrationServiceRestStub,
    ):
        def __hash__(self):
            return hash("DeveloperRegistrationServiceRestTransport.RegisterGcp")

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
            request: developerregistration.RegisterGcpRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> developerregistration.DeveloperRegistration:
            r"""Call the register gcp method over HTTP.

            Args:
                request (~.developerregistration.RegisterGcpRequest):
                    The request object. Request message for the RegisterGCP
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.developerregistration.DeveloperRegistration:
                    Represents a developer registration
                owned by a Merchant account.

            """

            http_options = _BaseDeveloperRegistrationServiceRestTransport._BaseRegisterGcp._get_http_options()
            request, metadata = self._interceptor.pre_register_gcp(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperRegistrationServiceRestTransport._BaseRegisterGcp,
                    "_BaseRegisterGcp__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1.DeveloperRegistrationServiceClient.RegisterGcp",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.DeveloperRegistrationService",
                        "rpcName": "RegisterGcp",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DeveloperRegistrationServiceRestTransport._RegisterGcp._get_response(
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
            resp = developerregistration.DeveloperRegistration()
            pb_resp = developerregistration.DeveloperRegistration.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_register_gcp(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_register_gcp_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        developerregistration.DeveloperRegistration.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.accounts_v1.DeveloperRegistrationServiceClient.register_gcp",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.DeveloperRegistrationService",
                        "rpcName": "RegisterGcp",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UnregisterGcp(
        _BaseDeveloperRegistrationServiceRestTransport._BaseUnregisterGcp,
        DeveloperRegistrationServiceRestStub,
    ):
        def __hash__(self):
            return hash("DeveloperRegistrationServiceRestTransport.UnregisterGcp")

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
            request: developerregistration.UnregisterGcpRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the unregister gcp method over HTTP.

            Args:
                request (~.developerregistration.UnregisterGcpRequest):
                    The request object. Request message for the UnregisterGCP
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseDeveloperRegistrationServiceRestTransport._BaseUnregisterGcp._get_http_options()
            request, metadata = self._interceptor.pre_unregister_gcp(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeveloperRegistrationServiceRestTransport._BaseUnregisterGcp,
                    "_BaseUnregisterGcp__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1.DeveloperRegistrationServiceClient.UnregisterGcp",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.DeveloperRegistrationService",
                        "rpcName": "UnregisterGcp",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DeveloperRegistrationServiceRestTransport._UnregisterGcp._get_response(
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

    @property
    def get_account_for_gcp_registration(
        self,
    ) -> Callable[
        [empty_pb2.Empty], developerregistration.GetAccountForGcpRegistrationResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAccountForGcpRegistration(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_developer_registration(
        self,
    ) -> Callable[
        [developerregistration.GetDeveloperRegistrationRequest],
        developerregistration.DeveloperRegistration,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDeveloperRegistration(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def register_gcp(
        self,
    ) -> Callable[
        [developerregistration.RegisterGcpRequest],
        developerregistration.DeveloperRegistration,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RegisterGcp(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def unregister_gcp(
        self,
    ) -> Callable[[developerregistration.UnregisterGcpRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UnregisterGcp(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("DeveloperRegistrationServiceRestTransport",)
