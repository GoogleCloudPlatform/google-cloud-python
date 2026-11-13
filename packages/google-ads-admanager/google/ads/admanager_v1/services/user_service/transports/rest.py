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
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.ads.admanager_v1._compat import transcode_request
from google.ads.admanager_v1.types import user_messages, user_service

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
            def pre_batch_activate_users(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_activate_users(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_create_users(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_users(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_deactivate_users(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_deactivate_users(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_update_users(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_users(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_user(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_user(self, response):
                logging.log(f"Received response: {response}")
                return response

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

    def pre_batch_activate_users(
        self,
        request: user_service.BatchActivateUsersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        user_service.BatchActivateUsersRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for batch_activate_users

        Override in a subclass to manipulate the request or metadata
        before they are sent to the UserService server.
        """
        return request, metadata

    def post_batch_activate_users(
        self, response: user_service.BatchActivateUsersResponse
    ) -> user_service.BatchActivateUsersResponse:
        """Post-rpc interceptor for batch_activate_users

        DEPRECATED. Please use the `post_batch_activate_users_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the UserService server but before
        it is returned to user code. This `post_batch_activate_users` interceptor runs
        before the `post_batch_activate_users_with_metadata` interceptor.
        """
        return response

    def post_batch_activate_users_with_metadata(
        self,
        response: user_service.BatchActivateUsersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        user_service.BatchActivateUsersResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for batch_activate_users

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the UserService server but before it is returned to user code.

        We recommend only using this `post_batch_activate_users_with_metadata`
        interceptor in new development instead of the `post_batch_activate_users` interceptor.
        When both interceptors are used, this `post_batch_activate_users_with_metadata` interceptor runs after the
        `post_batch_activate_users` interceptor. The (possibly modified) response returned by
        `post_batch_activate_users` will be passed to
        `post_batch_activate_users_with_metadata`.
        """
        return response, metadata

    def pre_batch_create_users(
        self,
        request: user_service.BatchCreateUsersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        user_service.BatchCreateUsersRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for batch_create_users

        Override in a subclass to manipulate the request or metadata
        before they are sent to the UserService server.
        """
        return request, metadata

    def post_batch_create_users(
        self, response: user_service.BatchCreateUsersResponse
    ) -> user_service.BatchCreateUsersResponse:
        """Post-rpc interceptor for batch_create_users

        DEPRECATED. Please use the `post_batch_create_users_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the UserService server but before
        it is returned to user code. This `post_batch_create_users` interceptor runs
        before the `post_batch_create_users_with_metadata` interceptor.
        """
        return response

    def post_batch_create_users_with_metadata(
        self,
        response: user_service.BatchCreateUsersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        user_service.BatchCreateUsersResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for batch_create_users

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the UserService server but before it is returned to user code.

        We recommend only using this `post_batch_create_users_with_metadata`
        interceptor in new development instead of the `post_batch_create_users` interceptor.
        When both interceptors are used, this `post_batch_create_users_with_metadata` interceptor runs after the
        `post_batch_create_users` interceptor. The (possibly modified) response returned by
        `post_batch_create_users` will be passed to
        `post_batch_create_users_with_metadata`.
        """
        return response, metadata

    def pre_batch_deactivate_users(
        self,
        request: user_service.BatchDeactivateUsersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        user_service.BatchDeactivateUsersRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_deactivate_users

        Override in a subclass to manipulate the request or metadata
        before they are sent to the UserService server.
        """
        return request, metadata

    def post_batch_deactivate_users(
        self, response: user_service.BatchDeactivateUsersResponse
    ) -> user_service.BatchDeactivateUsersResponse:
        """Post-rpc interceptor for batch_deactivate_users

        DEPRECATED. Please use the `post_batch_deactivate_users_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the UserService server but before
        it is returned to user code. This `post_batch_deactivate_users` interceptor runs
        before the `post_batch_deactivate_users_with_metadata` interceptor.
        """
        return response

    def post_batch_deactivate_users_with_metadata(
        self,
        response: user_service.BatchDeactivateUsersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        user_service.BatchDeactivateUsersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_deactivate_users

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the UserService server but before it is returned to user code.

        We recommend only using this `post_batch_deactivate_users_with_metadata`
        interceptor in new development instead of the `post_batch_deactivate_users` interceptor.
        When both interceptors are used, this `post_batch_deactivate_users_with_metadata` interceptor runs after the
        `post_batch_deactivate_users` interceptor. The (possibly modified) response returned by
        `post_batch_deactivate_users` will be passed to
        `post_batch_deactivate_users_with_metadata`.
        """
        return response, metadata

    def pre_batch_update_users(
        self,
        request: user_service.BatchUpdateUsersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        user_service.BatchUpdateUsersRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for batch_update_users

        Override in a subclass to manipulate the request or metadata
        before they are sent to the UserService server.
        """
        return request, metadata

    def post_batch_update_users(
        self, response: user_service.BatchUpdateUsersResponse
    ) -> user_service.BatchUpdateUsersResponse:
        """Post-rpc interceptor for batch_update_users

        DEPRECATED. Please use the `post_batch_update_users_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the UserService server but before
        it is returned to user code. This `post_batch_update_users` interceptor runs
        before the `post_batch_update_users_with_metadata` interceptor.
        """
        return response

    def post_batch_update_users_with_metadata(
        self,
        response: user_service.BatchUpdateUsersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        user_service.BatchUpdateUsersResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for batch_update_users

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the UserService server but before it is returned to user code.

        We recommend only using this `post_batch_update_users_with_metadata`
        interceptor in new development instead of the `post_batch_update_users` interceptor.
        When both interceptors are used, this `post_batch_update_users_with_metadata` interceptor runs after the
        `post_batch_update_users` interceptor. The (possibly modified) response returned by
        `post_batch_update_users` will be passed to
        `post_batch_update_users_with_metadata`.
        """
        return response, metadata

    def pre_create_user(
        self,
        request: user_service.CreateUserRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[user_service.CreateUserRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_user

        Override in a subclass to manipulate the request or metadata
        before they are sent to the UserService server.
        """
        return request, metadata

    def post_create_user(self, response: user_messages.User) -> user_messages.User:
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
        response: user_messages.User,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[user_messages.User, Sequence[Tuple[str, Union[str, bytes]]]]:
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

    def pre_get_user(
        self,
        request: user_service.GetUserRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[user_service.GetUserRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_user

        Override in a subclass to manipulate the request or metadata
        before they are sent to the UserService server.
        """
        return request, metadata

    def post_get_user(self, response: user_messages.User) -> user_messages.User:
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
        self,
        response: user_messages.User,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[user_messages.User, Sequence[Tuple[str, Union[str, bytes]]]]:
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
        request: user_service.ListUsersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[user_service.ListUsersRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_users

        Override in a subclass to manipulate the request or metadata
        before they are sent to the UserService server.
        """
        return request, metadata

    def post_list_users(
        self, response: user_service.ListUsersResponse
    ) -> user_service.ListUsersResponse:
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
        response: user_service.ListUsersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[user_service.ListUsersResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
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
        request: user_service.UpdateUserRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[user_service.UpdateUserRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_user

        Override in a subclass to manipulate the request or metadata
        before they are sent to the UserService server.
        """
        return request, metadata

    def post_update_user(self, response: user_messages.User) -> user_messages.User:
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
        response: user_messages.User,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[user_messages.User, Sequence[Tuple[str, Union[str, bytes]]]]:
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

    def pre_cancel_operation(
        self,
        request: operations_pb2.CancelOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.CancelOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the UserService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the UserService server but before
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
        before they are sent to the UserService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the UserService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class UserServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: UserServiceRestInterceptor


class UserServiceRestTransport(_BaseUserServiceRestTransport):
    """REST backend synchronous transport for UserService.

    Provides methods for handling User objects.

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
        interceptor: Optional[UserServiceRestInterceptor] = None,
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

    class _BatchActivateUsers(
        _BaseUserServiceRestTransport._BaseBatchActivateUsers, UserServiceRestStub
    ):
        def __hash__(self):
            return hash("UserServiceRestTransport.BatchActivateUsers")

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
            request: user_service.BatchActivateUsersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> user_service.BatchActivateUsersResponse:
            r"""Call the batch activate users method over HTTP.

            Args:
                request (~.user_service.BatchActivateUsersRequest):
                    The request object. Request message for ``BatchActivateUsers`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.user_service.BatchActivateUsersResponse:
                    Response object for ``BatchActivateUsers`` method.
            """

            http_options = _BaseUserServiceRestTransport._BaseBatchActivateUsers._get_http_options()
            request, metadata = self._interceptor.pre_batch_activate_users(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseUserServiceRestTransport._BaseBatchActivateUsers,
                    "_BaseBatchActivateUsers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.UserServiceClient.BatchActivateUsers",
                    extra={
                        "serviceName": "google.ads.admanager.v1.UserService",
                        "rpcName": "BatchActivateUsers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = UserServiceRestTransport._BatchActivateUsers._get_response(
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
            resp = user_service.BatchActivateUsersResponse()
            pb_resp = user_service.BatchActivateUsersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_activate_users(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_activate_users_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = user_service.BatchActivateUsersResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.UserServiceClient.batch_activate_users",
                    extra={
                        "serviceName": "google.ads.admanager.v1.UserService",
                        "rpcName": "BatchActivateUsers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchCreateUsers(
        _BaseUserServiceRestTransport._BaseBatchCreateUsers, UserServiceRestStub
    ):
        def __hash__(self):
            return hash("UserServiceRestTransport.BatchCreateUsers")

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
            request: user_service.BatchCreateUsersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> user_service.BatchCreateUsersResponse:
            r"""Call the batch create users method over HTTP.

            Args:
                request (~.user_service.BatchCreateUsersRequest):
                    The request object. Request object for ``BatchCreateUsers`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.user_service.BatchCreateUsersResponse:
                    Response object for ``BatchCreateUsers`` method.
            """

            http_options = (
                _BaseUserServiceRestTransport._BaseBatchCreateUsers._get_http_options()
            )
            request, metadata = self._interceptor.pre_batch_create_users(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseUserServiceRestTransport._BaseBatchCreateUsers,
                    "_BaseBatchCreateUsers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.UserServiceClient.BatchCreateUsers",
                    extra={
                        "serviceName": "google.ads.admanager.v1.UserService",
                        "rpcName": "BatchCreateUsers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = UserServiceRestTransport._BatchCreateUsers._get_response(
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
            resp = user_service.BatchCreateUsersResponse()
            pb_resp = user_service.BatchCreateUsersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_users(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_create_users_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = user_service.BatchCreateUsersResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.UserServiceClient.batch_create_users",
                    extra={
                        "serviceName": "google.ads.admanager.v1.UserService",
                        "rpcName": "BatchCreateUsers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchDeactivateUsers(
        _BaseUserServiceRestTransport._BaseBatchDeactivateUsers, UserServiceRestStub
    ):
        def __hash__(self):
            return hash("UserServiceRestTransport.BatchDeactivateUsers")

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
            request: user_service.BatchDeactivateUsersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> user_service.BatchDeactivateUsersResponse:
            r"""Call the batch deactivate users method over HTTP.

            Args:
                request (~.user_service.BatchDeactivateUsersRequest):
                    The request object. Request message for ``BatchDeactivateUsers`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.user_service.BatchDeactivateUsersResponse:
                    Response object for ``BatchDeactivateUsers`` method.
            """

            http_options = _BaseUserServiceRestTransport._BaseBatchDeactivateUsers._get_http_options()
            request, metadata = self._interceptor.pre_batch_deactivate_users(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseUserServiceRestTransport._BaseBatchDeactivateUsers,
                    "_BaseBatchDeactivateUsers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.UserServiceClient.BatchDeactivateUsers",
                    extra={
                        "serviceName": "google.ads.admanager.v1.UserService",
                        "rpcName": "BatchDeactivateUsers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = UserServiceRestTransport._BatchDeactivateUsers._get_response(
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
            resp = user_service.BatchDeactivateUsersResponse()
            pb_resp = user_service.BatchDeactivateUsersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_deactivate_users(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_deactivate_users_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        user_service.BatchDeactivateUsersResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.UserServiceClient.batch_deactivate_users",
                    extra={
                        "serviceName": "google.ads.admanager.v1.UserService",
                        "rpcName": "BatchDeactivateUsers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchUpdateUsers(
        _BaseUserServiceRestTransport._BaseBatchUpdateUsers, UserServiceRestStub
    ):
        def __hash__(self):
            return hash("UserServiceRestTransport.BatchUpdateUsers")

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
            request: user_service.BatchUpdateUsersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> user_service.BatchUpdateUsersResponse:
            r"""Call the batch update users method over HTTP.

            Args:
                request (~.user_service.BatchUpdateUsersRequest):
                    The request object. Request object for ``BatchUpdateUsers`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.user_service.BatchUpdateUsersResponse:
                    Response object for ``BatchUpdateUsers`` method.
            """

            http_options = (
                _BaseUserServiceRestTransport._BaseBatchUpdateUsers._get_http_options()
            )
            request, metadata = self._interceptor.pre_batch_update_users(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseUserServiceRestTransport._BaseBatchUpdateUsers,
                    "_BaseBatchUpdateUsers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.UserServiceClient.BatchUpdateUsers",
                    extra={
                        "serviceName": "google.ads.admanager.v1.UserService",
                        "rpcName": "BatchUpdateUsers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = UserServiceRestTransport._BatchUpdateUsers._get_response(
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
            resp = user_service.BatchUpdateUsersResponse()
            pb_resp = user_service.BatchUpdateUsersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_users(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_update_users_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = user_service.BatchUpdateUsersResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.UserServiceClient.batch_update_users",
                    extra={
                        "serviceName": "google.ads.admanager.v1.UserService",
                        "rpcName": "BatchUpdateUsers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

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
            request: user_service.CreateUserRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> user_messages.User:
            r"""Call the create user method over HTTP.

            Args:
                request (~.user_service.CreateUserRequest):
                    The request object. Request object for ``CreateUser`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.user_messages.User:
                    The User resource.
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
                    f"Sending request for google.ads.admanager_v1.UserServiceClient.CreateUser",
                    extra={
                        "serviceName": "google.ads.admanager.v1.UserService",
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
            resp = user_messages.User()
            pb_resp = user_messages.User.pb(resp)

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
                    response_payload = user_messages.User.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.UserServiceClient.create_user",
                    extra={
                        "serviceName": "google.ads.admanager.v1.UserService",
                        "rpcName": "CreateUser",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

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
            request: user_service.GetUserRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> user_messages.User:
            r"""Call the get user method over HTTP.

            Args:
                request (~.user_service.GetUserRequest):
                    The request object. Request object for GetUser method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.user_messages.User:
                    The User resource.
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
                    f"Sending request for google.ads.admanager_v1.UserServiceClient.GetUser",
                    extra={
                        "serviceName": "google.ads.admanager.v1.UserService",
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
            resp = user_messages.User()
            pb_resp = user_messages.User.pb(resp)

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
                    response_payload = user_messages.User.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.UserServiceClient.get_user",
                    extra={
                        "serviceName": "google.ads.admanager.v1.UserService",
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
            request: user_service.ListUsersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> user_service.ListUsersResponse:
            r"""Call the list users method over HTTP.

            Args:
                request (~.user_service.ListUsersRequest):
                    The request object. Request object for ListUsers method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.user_service.ListUsersResponse:
                    Response object for ListUsersRequest
                containing matching User resources.

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
                    f"Sending request for google.ads.admanager_v1.UserServiceClient.ListUsers",
                    extra={
                        "serviceName": "google.ads.admanager.v1.UserService",
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
            resp = user_service.ListUsersResponse()
            pb_resp = user_service.ListUsersResponse.pb(resp)

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
                    response_payload = user_service.ListUsersResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.UserServiceClient.list_users",
                    extra={
                        "serviceName": "google.ads.admanager.v1.UserService",
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
            request: user_service.UpdateUserRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> user_messages.User:
            r"""Call the update user method over HTTP.

            Args:
                request (~.user_service.UpdateUserRequest):
                    The request object. Request object for ``UpdateUser`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.user_messages.User:
                    The User resource.
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
                    f"Sending request for google.ads.admanager_v1.UserServiceClient.UpdateUser",
                    extra={
                        "serviceName": "google.ads.admanager.v1.UserService",
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
            resp = user_messages.User()
            pb_resp = user_messages.User.pb(resp)

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
                    response_payload = user_messages.User.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.UserServiceClient.update_user",
                    extra={
                        "serviceName": "google.ads.admanager.v1.UserService",
                        "rpcName": "UpdateUser",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_activate_users(
        self,
    ) -> Callable[
        [user_service.BatchActivateUsersRequest],
        user_service.BatchActivateUsersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchActivateUsers(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_create_users(
        self,
    ) -> Callable[
        [user_service.BatchCreateUsersRequest], user_service.BatchCreateUsersResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateUsers(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_deactivate_users(
        self,
    ) -> Callable[
        [user_service.BatchDeactivateUsersRequest],
        user_service.BatchDeactivateUsersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchDeactivateUsers(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_update_users(
        self,
    ) -> Callable[
        [user_service.BatchUpdateUsersRequest], user_service.BatchUpdateUsersResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdateUsers(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_user(
        self,
    ) -> Callable[[user_service.CreateUserRequest], user_messages.User]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateUser(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_user(self) -> Callable[[user_service.GetUserRequest], user_messages.User]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetUser(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_users(
        self,
    ) -> Callable[[user_service.ListUsersRequest], user_service.ListUsersResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListUsers(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_user(
        self,
    ) -> Callable[[user_service.UpdateUserRequest], user_messages.User]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateUser(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseUserServiceRestTransport._BaseCancelOperation, UserServiceRestStub
    ):
        def __hash__(self):
            return hash("UserServiceRestTransport.CancelOperation")

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

            http_options = (
                _BaseUserServiceRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseUserServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.ads.admanager_v1.UserServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.UserService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = UserServiceRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseUserServiceRestTransport._BaseGetOperation, UserServiceRestStub
    ):
        def __hash__(self):
            return hash("UserServiceRestTransport.GetOperation")

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

            http_options = (
                _BaseUserServiceRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseUserServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.ads.admanager_v1.UserServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.UserService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = UserServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.ads.admanager_v1.UserServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.UserService",
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


__all__ = ("UserServiceRestTransport",)
