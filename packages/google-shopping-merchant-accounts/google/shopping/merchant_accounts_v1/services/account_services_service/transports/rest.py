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
from google.shopping.merchant_accounts_v1.types import accountservices

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseAccountServicesServiceRestTransport

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


class AccountServicesServiceRestInterceptor:
    """Interceptor for AccountServicesService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the AccountServicesServiceRestTransport.

    .. code-block:: python
        class MyCustomAccountServicesServiceInterceptor(AccountServicesServiceRestInterceptor):
            def pre_approve_account_service(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_approve_account_service(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_account_service(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_account_service(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_account_services(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_account_services(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_propose_account_service(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_propose_account_service(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_reject_account_service(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

        transport = AccountServicesServiceRestTransport(interceptor=MyCustomAccountServicesServiceInterceptor())
        client = AccountServicesServiceClient(transport=transport)


    """

    def pre_approve_account_service(
        self,
        request: accountservices.ApproveAccountServiceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        accountservices.ApproveAccountServiceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for approve_account_service

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AccountServicesService server.
        """
        return request, metadata

    def post_approve_account_service(
        self, response: accountservices.AccountService
    ) -> accountservices.AccountService:
        """Post-rpc interceptor for approve_account_service

        DEPRECATED. Please use the `post_approve_account_service_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AccountServicesService server but before
        it is returned to user code. This `post_approve_account_service` interceptor runs
        before the `post_approve_account_service_with_metadata` interceptor.
        """
        return response

    def post_approve_account_service_with_metadata(
        self,
        response: accountservices.AccountService,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[accountservices.AccountService, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for approve_account_service

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AccountServicesService server but before it is returned to user code.

        We recommend only using this `post_approve_account_service_with_metadata`
        interceptor in new development instead of the `post_approve_account_service` interceptor.
        When both interceptors are used, this `post_approve_account_service_with_metadata` interceptor runs after the
        `post_approve_account_service` interceptor. The (possibly modified) response returned by
        `post_approve_account_service` will be passed to
        `post_approve_account_service_with_metadata`.
        """
        return response, metadata

    def pre_get_account_service(
        self,
        request: accountservices.GetAccountServiceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        accountservices.GetAccountServiceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_account_service

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AccountServicesService server.
        """
        return request, metadata

    def post_get_account_service(
        self, response: accountservices.AccountService
    ) -> accountservices.AccountService:
        """Post-rpc interceptor for get_account_service

        DEPRECATED. Please use the `post_get_account_service_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AccountServicesService server but before
        it is returned to user code. This `post_get_account_service` interceptor runs
        before the `post_get_account_service_with_metadata` interceptor.
        """
        return response

    def post_get_account_service_with_metadata(
        self,
        response: accountservices.AccountService,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[accountservices.AccountService, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_account_service

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AccountServicesService server but before it is returned to user code.

        We recommend only using this `post_get_account_service_with_metadata`
        interceptor in new development instead of the `post_get_account_service` interceptor.
        When both interceptors are used, this `post_get_account_service_with_metadata` interceptor runs after the
        `post_get_account_service` interceptor. The (possibly modified) response returned by
        `post_get_account_service` will be passed to
        `post_get_account_service_with_metadata`.
        """
        return response, metadata

    def pre_list_account_services(
        self,
        request: accountservices.ListAccountServicesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        accountservices.ListAccountServicesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_account_services

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AccountServicesService server.
        """
        return request, metadata

    def post_list_account_services(
        self, response: accountservices.ListAccountServicesResponse
    ) -> accountservices.ListAccountServicesResponse:
        """Post-rpc interceptor for list_account_services

        DEPRECATED. Please use the `post_list_account_services_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AccountServicesService server but before
        it is returned to user code. This `post_list_account_services` interceptor runs
        before the `post_list_account_services_with_metadata` interceptor.
        """
        return response

    def post_list_account_services_with_metadata(
        self,
        response: accountservices.ListAccountServicesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        accountservices.ListAccountServicesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_account_services

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AccountServicesService server but before it is returned to user code.

        We recommend only using this `post_list_account_services_with_metadata`
        interceptor in new development instead of the `post_list_account_services` interceptor.
        When both interceptors are used, this `post_list_account_services_with_metadata` interceptor runs after the
        `post_list_account_services` interceptor. The (possibly modified) response returned by
        `post_list_account_services` will be passed to
        `post_list_account_services_with_metadata`.
        """
        return response, metadata

    def pre_propose_account_service(
        self,
        request: accountservices.ProposeAccountServiceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        accountservices.ProposeAccountServiceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for propose_account_service

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AccountServicesService server.
        """
        return request, metadata

    def post_propose_account_service(
        self, response: accountservices.AccountService
    ) -> accountservices.AccountService:
        """Post-rpc interceptor for propose_account_service

        DEPRECATED. Please use the `post_propose_account_service_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AccountServicesService server but before
        it is returned to user code. This `post_propose_account_service` interceptor runs
        before the `post_propose_account_service_with_metadata` interceptor.
        """
        return response

    def post_propose_account_service_with_metadata(
        self,
        response: accountservices.AccountService,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[accountservices.AccountService, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for propose_account_service

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AccountServicesService server but before it is returned to user code.

        We recommend only using this `post_propose_account_service_with_metadata`
        interceptor in new development instead of the `post_propose_account_service` interceptor.
        When both interceptors are used, this `post_propose_account_service_with_metadata` interceptor runs after the
        `post_propose_account_service` interceptor. The (possibly modified) response returned by
        `post_propose_account_service` will be passed to
        `post_propose_account_service_with_metadata`.
        """
        return response, metadata

    def pre_reject_account_service(
        self,
        request: accountservices.RejectAccountServiceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        accountservices.RejectAccountServiceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for reject_account_service

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AccountServicesService server.
        """
        return request, metadata


@dataclasses.dataclass
class AccountServicesServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: AccountServicesServiceRestInterceptor


class AccountServicesServiceRestTransport(_BaseAccountServicesServiceRestTransport):
    """REST backend synchronous transport for AccountServicesService.

    Service to support AccountService API.

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
        interceptor: Optional[AccountServicesServiceRestInterceptor] = None,
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
            interceptor (Optional[AccountServicesServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or AccountServicesServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _ApproveAccountService(
        _BaseAccountServicesServiceRestTransport._BaseApproveAccountService,
        AccountServicesServiceRestStub,
    ):
        def __hash__(self):
            return hash("AccountServicesServiceRestTransport.ApproveAccountService")

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
            request: accountservices.ApproveAccountServiceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> accountservices.AccountService:
            r"""Call the approve account service method over HTTP.

            Args:
                request (~.accountservices.ApproveAccountServiceRequest):
                    The request object. Request to approve an account
                service.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.accountservices.AccountService:
                    The ``AccountService`` message represents a specific
                service that a provider account offers to a Merchant
                Center account.

                ``AccountService`` defines the permissions and
                capabilities granted to the provider, allowing for
                operations such as product management or campaign
                management.

                The lifecycle of an ``AccountService`` involves a
                proposal phase, where one party suggests the service,
                and an approval phase, where the other party accepts or
                rejects it. This handshake mechanism ensures mutual
                consent before any access is granted. This mechanism
                safeguards both parties by ensuring that access rights
                are granted appropriately and that both the business and
                provider are aware of the services enabled. In scenarios
                where a user is an admin of both accounts, the approval
                can happen automatically.

                The mutability of a service is also managed through
                ``AccountService``. Some services might be immutable,
                for example, if they were established through other
                systems or APIs, and you cannot alter them through this
                API.

            """

            http_options = _BaseAccountServicesServiceRestTransport._BaseApproveAccountService._get_http_options()
            request, metadata = self._interceptor.pre_approve_account_service(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAccountServicesServiceRestTransport._BaseApproveAccountService,
                    "_BaseApproveAccountService__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1.AccountServicesServiceClient.ApproveAccountService",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.AccountServicesService",
                        "rpcName": "ApproveAccountService",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AccountServicesServiceRestTransport._ApproveAccountService._get_response(
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
            resp = accountservices.AccountService()
            pb_resp = accountservices.AccountService.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_approve_account_service(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_approve_account_service_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = accountservices.AccountService.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.accounts_v1.AccountServicesServiceClient.approve_account_service",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.AccountServicesService",
                        "rpcName": "ApproveAccountService",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAccountService(
        _BaseAccountServicesServiceRestTransport._BaseGetAccountService,
        AccountServicesServiceRestStub,
    ):
        def __hash__(self):
            return hash("AccountServicesServiceRestTransport.GetAccountService")

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
            request: accountservices.GetAccountServiceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> accountservices.AccountService:
            r"""Call the get account service method over HTTP.

            Args:
                request (~.accountservices.GetAccountServiceRequest):
                    The request object. Request to get an account service.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.accountservices.AccountService:
                    The ``AccountService`` message represents a specific
                service that a provider account offers to a Merchant
                Center account.

                ``AccountService`` defines the permissions and
                capabilities granted to the provider, allowing for
                operations such as product management or campaign
                management.

                The lifecycle of an ``AccountService`` involves a
                proposal phase, where one party suggests the service,
                and an approval phase, where the other party accepts or
                rejects it. This handshake mechanism ensures mutual
                consent before any access is granted. This mechanism
                safeguards both parties by ensuring that access rights
                are granted appropriately and that both the business and
                provider are aware of the services enabled. In scenarios
                where a user is an admin of both accounts, the approval
                can happen automatically.

                The mutability of a service is also managed through
                ``AccountService``. Some services might be immutable,
                for example, if they were established through other
                systems or APIs, and you cannot alter them through this
                API.

            """

            http_options = _BaseAccountServicesServiceRestTransport._BaseGetAccountService._get_http_options()
            request, metadata = self._interceptor.pre_get_account_service(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAccountServicesServiceRestTransport._BaseGetAccountService,
                    "_BaseGetAccountService__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1.AccountServicesServiceClient.GetAccountService",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.AccountServicesService",
                        "rpcName": "GetAccountService",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AccountServicesServiceRestTransport._GetAccountService._get_response(
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
            resp = accountservices.AccountService()
            pb_resp = accountservices.AccountService.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_account_service(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_account_service_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = accountservices.AccountService.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.accounts_v1.AccountServicesServiceClient.get_account_service",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.AccountServicesService",
                        "rpcName": "GetAccountService",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAccountServices(
        _BaseAccountServicesServiceRestTransport._BaseListAccountServices,
        AccountServicesServiceRestStub,
    ):
        def __hash__(self):
            return hash("AccountServicesServiceRestTransport.ListAccountServices")

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
            request: accountservices.ListAccountServicesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> accountservices.ListAccountServicesResponse:
            r"""Call the list account services method over HTTP.

            Args:
                request (~.accountservices.ListAccountServicesRequest):
                    The request object. Request to list account services.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.accountservices.ListAccountServicesResponse:
                    Response after trying to list account
                services.

            """

            http_options = _BaseAccountServicesServiceRestTransport._BaseListAccountServices._get_http_options()
            request, metadata = self._interceptor.pre_list_account_services(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAccountServicesServiceRestTransport._BaseListAccountServices,
                    "_BaseListAccountServices__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1.AccountServicesServiceClient.ListAccountServices",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.AccountServicesService",
                        "rpcName": "ListAccountServices",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AccountServicesServiceRestTransport._ListAccountServices._get_response(
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
            resp = accountservices.ListAccountServicesResponse()
            pb_resp = accountservices.ListAccountServicesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_account_services(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_account_services_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        accountservices.ListAccountServicesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.accounts_v1.AccountServicesServiceClient.list_account_services",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.AccountServicesService",
                        "rpcName": "ListAccountServices",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ProposeAccountService(
        _BaseAccountServicesServiceRestTransport._BaseProposeAccountService,
        AccountServicesServiceRestStub,
    ):
        def __hash__(self):
            return hash("AccountServicesServiceRestTransport.ProposeAccountService")

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
            request: accountservices.ProposeAccountServiceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> accountservices.AccountService:
            r"""Call the propose account service method over HTTP.

            Args:
                request (~.accountservices.ProposeAccountServiceRequest):
                    The request object. Request to propose an account
                service.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.accountservices.AccountService:
                    The ``AccountService`` message represents a specific
                service that a provider account offers to a Merchant
                Center account.

                ``AccountService`` defines the permissions and
                capabilities granted to the provider, allowing for
                operations such as product management or campaign
                management.

                The lifecycle of an ``AccountService`` involves a
                proposal phase, where one party suggests the service,
                and an approval phase, where the other party accepts or
                rejects it. This handshake mechanism ensures mutual
                consent before any access is granted. This mechanism
                safeguards both parties by ensuring that access rights
                are granted appropriately and that both the business and
                provider are aware of the services enabled. In scenarios
                where a user is an admin of both accounts, the approval
                can happen automatically.

                The mutability of a service is also managed through
                ``AccountService``. Some services might be immutable,
                for example, if they were established through other
                systems or APIs, and you cannot alter them through this
                API.

            """

            http_options = _BaseAccountServicesServiceRestTransport._BaseProposeAccountService._get_http_options()
            request, metadata = self._interceptor.pre_propose_account_service(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAccountServicesServiceRestTransport._BaseProposeAccountService,
                    "_BaseProposeAccountService__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1.AccountServicesServiceClient.ProposeAccountService",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.AccountServicesService",
                        "rpcName": "ProposeAccountService",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AccountServicesServiceRestTransport._ProposeAccountService._get_response(
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
            resp = accountservices.AccountService()
            pb_resp = accountservices.AccountService.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_propose_account_service(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_propose_account_service_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = accountservices.AccountService.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.accounts_v1.AccountServicesServiceClient.propose_account_service",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.AccountServicesService",
                        "rpcName": "ProposeAccountService",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RejectAccountService(
        _BaseAccountServicesServiceRestTransport._BaseRejectAccountService,
        AccountServicesServiceRestStub,
    ):
        def __hash__(self):
            return hash("AccountServicesServiceRestTransport.RejectAccountService")

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
            request: accountservices.RejectAccountServiceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the reject account service method over HTTP.

            Args:
                request (~.accountservices.RejectAccountServiceRequest):
                    The request object. Request to reject an account service.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseAccountServicesServiceRestTransport._BaseRejectAccountService._get_http_options()
            request, metadata = self._interceptor.pre_reject_account_service(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAccountServicesServiceRestTransport._BaseRejectAccountService,
                    "_BaseRejectAccountService__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1.AccountServicesServiceClient.RejectAccountService",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1.AccountServicesService",
                        "rpcName": "RejectAccountService",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AccountServicesServiceRestTransport._RejectAccountService._get_response(
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
    def approve_account_service(
        self,
    ) -> Callable[
        [accountservices.ApproveAccountServiceRequest], accountservices.AccountService
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ApproveAccountService(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_account_service(
        self,
    ) -> Callable[
        [accountservices.GetAccountServiceRequest], accountservices.AccountService
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAccountService(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_account_services(
        self,
    ) -> Callable[
        [accountservices.ListAccountServicesRequest],
        accountservices.ListAccountServicesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAccountServices(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def propose_account_service(
        self,
    ) -> Callable[
        [accountservices.ProposeAccountServiceRequest], accountservices.AccountService
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ProposeAccountService(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def reject_account_service(
        self,
    ) -> Callable[[accountservices.RejectAccountServiceRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RejectAccountService(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("AccountServicesServiceRestTransport",)
