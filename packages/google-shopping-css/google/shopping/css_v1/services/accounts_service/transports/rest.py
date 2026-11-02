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

from google.shopping.css_v1._compat import transcode_request
from google.shopping.css_v1.types import accounts

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseAccountsServiceRestTransport

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


class AccountsServiceRestInterceptor:
    """Interceptor for AccountsService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the AccountsServiceRestTransport.

    .. code-block:: python
        class MyCustomAccountsServiceInterceptor(AccountsServiceRestInterceptor):
            def pre_get_account(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_account(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_child_accounts(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_child_accounts(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_labels(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_labels(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = AccountsServiceRestTransport(interceptor=MyCustomAccountsServiceInterceptor())
        client = AccountsServiceClient(transport=transport)


    """

    def pre_get_account(
        self,
        request: accounts.GetAccountRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[accounts.GetAccountRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_account

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AccountsService server.
        """
        return request, metadata

    def post_get_account(self, response: accounts.Account) -> accounts.Account:
        """Post-rpc interceptor for get_account

        DEPRECATED. Please use the `post_get_account_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AccountsService server but before
        it is returned to user code. This `post_get_account` interceptor runs
        before the `post_get_account_with_metadata` interceptor.
        """
        return response

    def post_get_account_with_metadata(
        self,
        response: accounts.Account,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[accounts.Account, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_account

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AccountsService server but before it is returned to user code.

        We recommend only using this `post_get_account_with_metadata`
        interceptor in new development instead of the `post_get_account` interceptor.
        When both interceptors are used, this `post_get_account_with_metadata` interceptor runs after the
        `post_get_account` interceptor. The (possibly modified) response returned by
        `post_get_account` will be passed to
        `post_get_account_with_metadata`.
        """
        return response, metadata

    def pre_list_child_accounts(
        self,
        request: accounts.ListChildAccountsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        accounts.ListChildAccountsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_child_accounts

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AccountsService server.
        """
        return request, metadata

    def post_list_child_accounts(
        self, response: accounts.ListChildAccountsResponse
    ) -> accounts.ListChildAccountsResponse:
        """Post-rpc interceptor for list_child_accounts

        DEPRECATED. Please use the `post_list_child_accounts_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AccountsService server but before
        it is returned to user code. This `post_list_child_accounts` interceptor runs
        before the `post_list_child_accounts_with_metadata` interceptor.
        """
        return response

    def post_list_child_accounts_with_metadata(
        self,
        response: accounts.ListChildAccountsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        accounts.ListChildAccountsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_child_accounts

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AccountsService server but before it is returned to user code.

        We recommend only using this `post_list_child_accounts_with_metadata`
        interceptor in new development instead of the `post_list_child_accounts` interceptor.
        When both interceptors are used, this `post_list_child_accounts_with_metadata` interceptor runs after the
        `post_list_child_accounts` interceptor. The (possibly modified) response returned by
        `post_list_child_accounts` will be passed to
        `post_list_child_accounts_with_metadata`.
        """
        return response, metadata

    def pre_update_labels(
        self,
        request: accounts.UpdateAccountLabelsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        accounts.UpdateAccountLabelsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_labels

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AccountsService server.
        """
        return request, metadata

    def post_update_labels(self, response: accounts.Account) -> accounts.Account:
        """Post-rpc interceptor for update_labels

        DEPRECATED. Please use the `post_update_labels_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AccountsService server but before
        it is returned to user code. This `post_update_labels` interceptor runs
        before the `post_update_labels_with_metadata` interceptor.
        """
        return response

    def post_update_labels_with_metadata(
        self,
        response: accounts.Account,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[accounts.Account, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_labels

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AccountsService server but before it is returned to user code.

        We recommend only using this `post_update_labels_with_metadata`
        interceptor in new development instead of the `post_update_labels` interceptor.
        When both interceptors are used, this `post_update_labels_with_metadata` interceptor runs after the
        `post_update_labels` interceptor. The (possibly modified) response returned by
        `post_update_labels` will be passed to
        `post_update_labels_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class AccountsServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: AccountsServiceRestInterceptor


class AccountsServiceRestTransport(_BaseAccountsServiceRestTransport):
    """REST backend synchronous transport for AccountsService.

    Service for managing CSS/MC account information.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "css.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[AccountsServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'css.googleapis.com').
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
            interceptor (Optional[AccountsServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or AccountsServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _GetAccount(
        _BaseAccountsServiceRestTransport._BaseGetAccount, AccountsServiceRestStub
    ):
        def __hash__(self):
            return hash("AccountsServiceRestTransport.GetAccount")

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
            request: accounts.GetAccountRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> accounts.Account:
            r"""Call the get account method over HTTP.

            Args:
                request (~.accounts.GetAccountRequest):
                    The request object. The request message for the ``GetAccount`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.accounts.Account:
                    Information about CSS/MC account.
            """

            http_options = (
                _BaseAccountsServiceRestTransport._BaseGetAccount._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_account(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAccountsServiceRestTransport._BaseGetAccount,
                    "_BaseGetAccount__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.css_v1.AccountsServiceClient.GetAccount",
                    extra={
                        "serviceName": "google.shopping.css.v1.AccountsService",
                        "rpcName": "GetAccount",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AccountsServiceRestTransport._GetAccount._get_response(
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
            resp = accounts.Account()
            pb_resp = accounts.Account.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_account(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_account_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = accounts.Account.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.css_v1.AccountsServiceClient.get_account",
                    extra={
                        "serviceName": "google.shopping.css.v1.AccountsService",
                        "rpcName": "GetAccount",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListChildAccounts(
        _BaseAccountsServiceRestTransport._BaseListChildAccounts,
        AccountsServiceRestStub,
    ):
        def __hash__(self):
            return hash("AccountsServiceRestTransport.ListChildAccounts")

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
            request: accounts.ListChildAccountsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> accounts.ListChildAccountsResponse:
            r"""Call the list child accounts method over HTTP.

            Args:
                request (~.accounts.ListChildAccountsRequest):
                    The request object. The request message for the ``ListChildAccounts``
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.accounts.ListChildAccountsResponse:
                    Response message for the ``ListChildAccounts`` method.
            """

            http_options = _BaseAccountsServiceRestTransport._BaseListChildAccounts._get_http_options()
            request, metadata = self._interceptor.pre_list_child_accounts(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAccountsServiceRestTransport._BaseListChildAccounts,
                    "_BaseListChildAccounts__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.css_v1.AccountsServiceClient.ListChildAccounts",
                    extra={
                        "serviceName": "google.shopping.css.v1.AccountsService",
                        "rpcName": "ListChildAccounts",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AccountsServiceRestTransport._ListChildAccounts._get_response(
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
            resp = accounts.ListChildAccountsResponse()
            pb_resp = accounts.ListChildAccountsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_child_accounts(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_child_accounts_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = accounts.ListChildAccountsResponse.to_json(
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
                    "Received response for google.shopping.css_v1.AccountsServiceClient.list_child_accounts",
                    extra={
                        "serviceName": "google.shopping.css.v1.AccountsService",
                        "rpcName": "ListChildAccounts",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateLabels(
        _BaseAccountsServiceRestTransport._BaseUpdateLabels, AccountsServiceRestStub
    ):
        def __hash__(self):
            return hash("AccountsServiceRestTransport.UpdateLabels")

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
            request: accounts.UpdateAccountLabelsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> accounts.Account:
            r"""Call the update labels method over HTTP.

            Args:
                request (~.accounts.UpdateAccountLabelsRequest):
                    The request object. The request message for the ``UpdateLabels`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.accounts.Account:
                    Information about CSS/MC account.
            """

            http_options = (
                _BaseAccountsServiceRestTransport._BaseUpdateLabels._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_labels(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAccountsServiceRestTransport._BaseUpdateLabels,
                    "_BaseUpdateLabels__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.css_v1.AccountsServiceClient.UpdateLabels",
                    extra={
                        "serviceName": "google.shopping.css.v1.AccountsService",
                        "rpcName": "UpdateLabels",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AccountsServiceRestTransport._UpdateLabels._get_response(
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
            resp = accounts.Account()
            pb_resp = accounts.Account.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_labels(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_labels_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = accounts.Account.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.css_v1.AccountsServiceClient.update_labels",
                    extra={
                        "serviceName": "google.shopping.css.v1.AccountsService",
                        "rpcName": "UpdateLabels",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def get_account(self) -> Callable[[accounts.GetAccountRequest], accounts.Account]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAccount(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_child_accounts(
        self,
    ) -> Callable[
        [accounts.ListChildAccountsRequest], accounts.ListChildAccountsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListChildAccounts(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_labels(
        self,
    ) -> Callable[[accounts.UpdateAccountLabelsRequest], accounts.Account]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateLabels(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("AccountsServiceRestTransport",)
