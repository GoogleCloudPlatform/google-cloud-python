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
from google.shopping.merchant_accounts_v1beta.types import user
from google.shopping.merchant_accounts_v1beta.types import user as gsma_user

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseUserServiceRestTransport

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


class UserServiceRestInterceptor:
    """Interceptor for UserService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the UserServiceRestTransport.

    .. code-block:: python
        class MyCustomUserServiceInterceptor(UserServiceRestInterceptor):
            def pre_create_user(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_user(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_user(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_user(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_user(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_users(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_users(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_user(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_user(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = UserServiceRestTransport(interceptor=MyCustomUserServiceInterceptor())
        client = UserServiceClient(transport=transport)


    """

    def pre_create_user(
        self,
        request: gsma_user.CreateUserRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gsma_user.CreateUserRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_user

        Override in a subclass to manipulate the request or metadata
        before they are sent to the UserService server.
        """
        return request, metadata

    def post_create_user(self, response: gsma_user.User) -> gsma_user.User:
        """Post-rpc interceptor for create_user

        DEPRECATED. Please use the `post_create_user_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the UserService server but before
        it is returned to user code. This `post_create_user` interceptor runs
        before the `post_create_user_with_metadata` interceptor.
        """
        return response

    def post_create_user_with_metadata(
        self,
        response: gsma_user.User,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gsma_user.User, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_user

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the UserService server but before it is returned to user code.

        We recommend only using this `post_create_user_with_metadata`
        interceptor in new development instead of the `post_create_user` interceptor.
        When both interceptors are used, this `post_create_user_with_metadata` interceptor runs after the
        `post_create_user` interceptor. The (possibly modified) response returned by
        `post_create_user` will be passed to
        `post_create_user_with_metadata`.
        """
        return response, metadata

    def pre_delete_user(
        self,
        request: user.DeleteUserRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[user.DeleteUserRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_user

        Override in a subclass to manipulate the request or metadata
        before they are sent to the UserService server.
        """
        return request, metadata

    def pre_get_user(
        self,
        request: user.GetUserRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[user.GetUserRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_user

        Override in a subclass to manipulate the request or metadata
        before they are sent to the UserService server.
        """
        return request, metadata

    def post_get_user(self, response: user.User) -> user.User:
        """Post-rpc interceptor for get_user

        DEPRECATED. Please use the `post_get_user_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the UserService server but before
        it is returned to user code. This `post_get_user` interceptor runs
        before the `post_get_user_with_metadata` interceptor.
        """
        return response

    def post_get_user_with_metadata(
        self, response: user.User, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[user.User, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_user

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the UserService server but before it is returned to user code.

        We recommend only using this `post_get_user_with_metadata`
        interceptor in new development instead of the `post_get_user` interceptor.
        When both interceptors are used, this `post_get_user_with_metadata` interceptor runs after the
        `post_get_user` interceptor. The (possibly modified) response returned by
        `post_get_user` will be passed to
        `post_get_user_with_metadata`.
        """
        return response, metadata

    def pre_list_users(
        self,
        request: user.ListUsersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[user.ListUsersRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_users

        Override in a subclass to manipulate the request or metadata
        before they are sent to the UserService server.
        """
        return request, metadata

    def post_list_users(
        self, response: user.ListUsersResponse
    ) -> user.ListUsersResponse:
        """Post-rpc interceptor for list_users

        DEPRECATED. Please use the `post_list_users_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the UserService server but before
        it is returned to user code. This `post_list_users` interceptor runs
        before the `post_list_users_with_metadata` interceptor.
        """
        return response

    def post_list_users_with_metadata(
        self,
        response: user.ListUsersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[user.ListUsersResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_users

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the UserService server but before it is returned to user code.

        We recommend only using this `post_list_users_with_metadata`
        interceptor in new development instead of the `post_list_users` interceptor.
        When both interceptors are used, this `post_list_users_with_metadata` interceptor runs after the
        `post_list_users` interceptor. The (possibly modified) response returned by
        `post_list_users` will be passed to
        `post_list_users_with_metadata`.
        """
        return response, metadata

    def pre_update_user(
        self,
        request: gsma_user.UpdateUserRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gsma_user.UpdateUserRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_user

        Override in a subclass to manipulate the request or metadata
        before they are sent to the UserService server.
        """
        return request, metadata

    def post_update_user(self, response: gsma_user.User) -> gsma_user.User:
        """Post-rpc interceptor for update_user

        DEPRECATED. Please use the `post_update_user_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the UserService server but before
        it is returned to user code. This `post_update_user` interceptor runs
        before the `post_update_user_with_metadata` interceptor.
        """
        return response

    def post_update_user_with_metadata(
        self,
        response: gsma_user.User,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gsma_user.User, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_user

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the UserService server but before it is returned to user code.

        We recommend only using this `post_update_user_with_metadata`
        interceptor in new development instead of the `post_update_user` interceptor.
        When both interceptors are used, this `post_update_user_with_metadata` interceptor runs after the
        `post_update_user` interceptor. The (possibly modified) response returned by
        `post_update_user` will be passed to
        `post_update_user_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class UserServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: UserServiceRestInterceptor


class UserServiceRestTransport(_BaseUserServiceRestTransport):
    """REST backend synchronous transport for UserService.

    Service to support user API.

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
        interceptor: Optional[UserServiceRestInterceptor] = None,
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
            interceptor (Optional[UserServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or UserServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateUser(
        _BaseUserServiceRestTransport._BaseCreateUser, UserServiceRestStub
    ):
        def __hash__(self):
            return hash("UserServiceRestTransport.CreateUser")

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
            request: gsma_user.CreateUserRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gsma_user.User:
            r"""Call the create user method over HTTP.

            Args:
                request (~.gsma_user.CreateUserRequest):
                    The request object. Request message for the ``CreateUser`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gsma_user.User:
                    A
                `user <https://support.google.com/merchants/answer/12160472>`__.

            """

            http_options = (
                _BaseUserServiceRestTransport._BaseCreateUser._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_user(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseUserServiceRestTransport._BaseCreateUser,
                    "_BaseCreateUser__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1beta.UserServiceClient.CreateUser",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1beta.UserService",
                        "rpcName": "CreateUser",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = UserServiceRestTransport._CreateUser._get_response(
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
            resp = gsma_user.User()
            pb_resp = gsma_user.User.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_user(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_user_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gsma_user.User.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.accounts_v1beta.UserServiceClient.create_user",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1beta.UserService",
                        "rpcName": "CreateUser",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteUser(
        _BaseUserServiceRestTransport._BaseDeleteUser, UserServiceRestStub
    ):
        def __hash__(self):
            return hash("UserServiceRestTransport.DeleteUser")

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
            request: user.DeleteUserRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete user method over HTTP.

            Args:
                request (~.user.DeleteUserRequest):
                    The request object. Request message for the ``DeleteUser`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseUserServiceRestTransport._BaseDeleteUser._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_user(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseUserServiceRestTransport._BaseDeleteUser,
                    "_BaseDeleteUser__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1beta.UserServiceClient.DeleteUser",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1beta.UserService",
                        "rpcName": "DeleteUser",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = UserServiceRestTransport._DeleteUser._get_response(
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

    class _GetUser(_BaseUserServiceRestTransport._BaseGetUser, UserServiceRestStub):
        def __hash__(self):
            return hash("UserServiceRestTransport.GetUser")

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
            request: user.GetUserRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> user.User:
            r"""Call the get user method over HTTP.

            Args:
                request (~.user.GetUserRequest):
                    The request object. Request message for the ``GetUser`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.user.User:
                    A
                `user <https://support.google.com/merchants/answer/12160472>`__.

            """

            http_options = (
                _BaseUserServiceRestTransport._BaseGetUser._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_user(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseUserServiceRestTransport._BaseGetUser,
                    "_BaseGetUser__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1beta.UserServiceClient.GetUser",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1beta.UserService",
                        "rpcName": "GetUser",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = UserServiceRestTransport._GetUser._get_response(
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
            resp = user.User()
            pb_resp = user.User.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_user(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_user_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = user.User.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.accounts_v1beta.UserServiceClient.get_user",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1beta.UserService",
                        "rpcName": "GetUser",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListUsers(_BaseUserServiceRestTransport._BaseListUsers, UserServiceRestStub):
        def __hash__(self):
            return hash("UserServiceRestTransport.ListUsers")

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
            request: user.ListUsersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> user.ListUsersResponse:
            r"""Call the list users method over HTTP.

            Args:
                request (~.user.ListUsersRequest):
                    The request object. Request message for the ``ListUsers`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.user.ListUsersResponse:
                    Response message for the ``ListUsers`` method.
            """

            http_options = (
                _BaseUserServiceRestTransport._BaseListUsers._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_users(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseUserServiceRestTransport._BaseListUsers,
                    "_BaseListUsers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1beta.UserServiceClient.ListUsers",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1beta.UserService",
                        "rpcName": "ListUsers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = UserServiceRestTransport._ListUsers._get_response(
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
            resp = user.ListUsersResponse()
            pb_resp = user.ListUsersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_users(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_users_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = user.ListUsersResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.accounts_v1beta.UserServiceClient.list_users",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1beta.UserService",
                        "rpcName": "ListUsers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateUser(
        _BaseUserServiceRestTransport._BaseUpdateUser, UserServiceRestStub
    ):
        def __hash__(self):
            return hash("UserServiceRestTransport.UpdateUser")

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
            request: gsma_user.UpdateUserRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gsma_user.User:
            r"""Call the update user method over HTTP.

            Args:
                request (~.gsma_user.UpdateUserRequest):
                    The request object. Request message for the ``UpdateUser`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gsma_user.User:
                    A
                `user <https://support.google.com/merchants/answer/12160472>`__.

            """

            http_options = (
                _BaseUserServiceRestTransport._BaseUpdateUser._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_user(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseUserServiceRestTransport._BaseUpdateUser,
                    "_BaseUpdateUser__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.shopping.merchant.accounts_v1beta.UserServiceClient.UpdateUser",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1beta.UserService",
                        "rpcName": "UpdateUser",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = UserServiceRestTransport._UpdateUser._get_response(
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
            resp = gsma_user.User()
            pb_resp = gsma_user.User.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_user(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_user_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gsma_user.User.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.shopping.merchant.accounts_v1beta.UserServiceClient.update_user",
                    extra={
                        "serviceName": "google.shopping.merchant.accounts.v1beta.UserService",
                        "rpcName": "UpdateUser",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_user(self) -> Callable[[gsma_user.CreateUserRequest], gsma_user.User]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateUser(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_user(self) -> Callable[[user.DeleteUserRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteUser(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_user(self) -> Callable[[user.GetUserRequest], user.User]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetUser(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_users(self) -> Callable[[user.ListUsersRequest], user.ListUsersResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListUsers(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_user(self) -> Callable[[gsma_user.UpdateUserRequest], gsma_user.User]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateUser(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("UserServiceRestTransport",)
