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

from google.cloud.api_keys_v2._compat import transcode_request
from google.cloud.api_keys_v2.types import apikeys, resources

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseApiKeysRestTransport

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


class ApiKeysRestInterceptor:
    """Interceptor for ApiKeys.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ApiKeysRestTransport.

    .. code-block:: python
        class MyCustomApiKeysInterceptor(ApiKeysRestInterceptor):
            def pre_create_key(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_key(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_key(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_key(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_key(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_key(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_key_string(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_key_string(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_keys(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_keys(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_lookup_key(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_lookup_key(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_undelete_key(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_undelete_key(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_key(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_key(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ApiKeysRestTransport(interceptor=MyCustomApiKeysInterceptor())
        client = ApiKeysClient(transport=transport)


    """

    def pre_create_key(
        self,
        request: apikeys.CreateKeyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[apikeys.CreateKeyRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_key

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiKeys server.
        """
        return request, metadata

    def post_create_key(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_key

        DEPRECATED. Please use the `post_create_key_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiKeys server but before
        it is returned to user code. This `post_create_key` interceptor runs
        before the `post_create_key_with_metadata` interceptor.
        """
        return response

    def post_create_key_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_key

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiKeys server but before it is returned to user code.

        We recommend only using this `post_create_key_with_metadata`
        interceptor in new development instead of the `post_create_key` interceptor.
        When both interceptors are used, this `post_create_key_with_metadata` interceptor runs after the
        `post_create_key` interceptor. The (possibly modified) response returned by
        `post_create_key` will be passed to
        `post_create_key_with_metadata`.
        """
        return response, metadata

    def pre_delete_key(
        self,
        request: apikeys.DeleteKeyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[apikeys.DeleteKeyRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_key

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiKeys server.
        """
        return request, metadata

    def post_delete_key(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_key

        DEPRECATED. Please use the `post_delete_key_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiKeys server but before
        it is returned to user code. This `post_delete_key` interceptor runs
        before the `post_delete_key_with_metadata` interceptor.
        """
        return response

    def post_delete_key_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_key

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiKeys server but before it is returned to user code.

        We recommend only using this `post_delete_key_with_metadata`
        interceptor in new development instead of the `post_delete_key` interceptor.
        When both interceptors are used, this `post_delete_key_with_metadata` interceptor runs after the
        `post_delete_key` interceptor. The (possibly modified) response returned by
        `post_delete_key` will be passed to
        `post_delete_key_with_metadata`.
        """
        return response, metadata

    def pre_get_key(
        self,
        request: apikeys.GetKeyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[apikeys.GetKeyRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_key

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiKeys server.
        """
        return request, metadata

    def post_get_key(self, response: resources.Key) -> resources.Key:
        """Post-rpc interceptor for get_key

        DEPRECATED. Please use the `post_get_key_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiKeys server but before
        it is returned to user code. This `post_get_key` interceptor runs
        before the `post_get_key_with_metadata` interceptor.
        """
        return response

    def post_get_key_with_metadata(
        self, response: resources.Key, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[resources.Key, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_key

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiKeys server but before it is returned to user code.

        We recommend only using this `post_get_key_with_metadata`
        interceptor in new development instead of the `post_get_key` interceptor.
        When both interceptors are used, this `post_get_key_with_metadata` interceptor runs after the
        `post_get_key` interceptor. The (possibly modified) response returned by
        `post_get_key` will be passed to
        `post_get_key_with_metadata`.
        """
        return response, metadata

    def pre_get_key_string(
        self,
        request: apikeys.GetKeyStringRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[apikeys.GetKeyStringRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_key_string

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiKeys server.
        """
        return request, metadata

    def post_get_key_string(
        self, response: apikeys.GetKeyStringResponse
    ) -> apikeys.GetKeyStringResponse:
        """Post-rpc interceptor for get_key_string

        DEPRECATED. Please use the `post_get_key_string_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiKeys server but before
        it is returned to user code. This `post_get_key_string` interceptor runs
        before the `post_get_key_string_with_metadata` interceptor.
        """
        return response

    def post_get_key_string_with_metadata(
        self,
        response: apikeys.GetKeyStringResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[apikeys.GetKeyStringResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_key_string

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiKeys server but before it is returned to user code.

        We recommend only using this `post_get_key_string_with_metadata`
        interceptor in new development instead of the `post_get_key_string` interceptor.
        When both interceptors are used, this `post_get_key_string_with_metadata` interceptor runs after the
        `post_get_key_string` interceptor. The (possibly modified) response returned by
        `post_get_key_string` will be passed to
        `post_get_key_string_with_metadata`.
        """
        return response, metadata

    def pre_list_keys(
        self,
        request: apikeys.ListKeysRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[apikeys.ListKeysRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_keys

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiKeys server.
        """
        return request, metadata

    def post_list_keys(
        self, response: apikeys.ListKeysResponse
    ) -> apikeys.ListKeysResponse:
        """Post-rpc interceptor for list_keys

        DEPRECATED. Please use the `post_list_keys_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiKeys server but before
        it is returned to user code. This `post_list_keys` interceptor runs
        before the `post_list_keys_with_metadata` interceptor.
        """
        return response

    def post_list_keys_with_metadata(
        self,
        response: apikeys.ListKeysResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[apikeys.ListKeysResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_keys

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiKeys server but before it is returned to user code.

        We recommend only using this `post_list_keys_with_metadata`
        interceptor in new development instead of the `post_list_keys` interceptor.
        When both interceptors are used, this `post_list_keys_with_metadata` interceptor runs after the
        `post_list_keys` interceptor. The (possibly modified) response returned by
        `post_list_keys` will be passed to
        `post_list_keys_with_metadata`.
        """
        return response, metadata

    def pre_lookup_key(
        self,
        request: apikeys.LookupKeyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[apikeys.LookupKeyRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for lookup_key

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiKeys server.
        """
        return request, metadata

    def post_lookup_key(
        self, response: apikeys.LookupKeyResponse
    ) -> apikeys.LookupKeyResponse:
        """Post-rpc interceptor for lookup_key

        DEPRECATED. Please use the `post_lookup_key_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiKeys server but before
        it is returned to user code. This `post_lookup_key` interceptor runs
        before the `post_lookup_key_with_metadata` interceptor.
        """
        return response

    def post_lookup_key_with_metadata(
        self,
        response: apikeys.LookupKeyResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[apikeys.LookupKeyResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for lookup_key

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiKeys server but before it is returned to user code.

        We recommend only using this `post_lookup_key_with_metadata`
        interceptor in new development instead of the `post_lookup_key` interceptor.
        When both interceptors are used, this `post_lookup_key_with_metadata` interceptor runs after the
        `post_lookup_key` interceptor. The (possibly modified) response returned by
        `post_lookup_key` will be passed to
        `post_lookup_key_with_metadata`.
        """
        return response, metadata

    def pre_undelete_key(
        self,
        request: apikeys.UndeleteKeyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[apikeys.UndeleteKeyRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for undelete_key

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiKeys server.
        """
        return request, metadata

    def post_undelete_key(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for undelete_key

        DEPRECATED. Please use the `post_undelete_key_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiKeys server but before
        it is returned to user code. This `post_undelete_key` interceptor runs
        before the `post_undelete_key_with_metadata` interceptor.
        """
        return response

    def post_undelete_key_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for undelete_key

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiKeys server but before it is returned to user code.

        We recommend only using this `post_undelete_key_with_metadata`
        interceptor in new development instead of the `post_undelete_key` interceptor.
        When both interceptors are used, this `post_undelete_key_with_metadata` interceptor runs after the
        `post_undelete_key` interceptor. The (possibly modified) response returned by
        `post_undelete_key` will be passed to
        `post_undelete_key_with_metadata`.
        """
        return response, metadata

    def pre_update_key(
        self,
        request: apikeys.UpdateKeyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[apikeys.UpdateKeyRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_key

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiKeys server.
        """
        return request, metadata

    def post_update_key(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_key

        DEPRECATED. Please use the `post_update_key_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApiKeys server but before
        it is returned to user code. This `post_update_key` interceptor runs
        before the `post_update_key_with_metadata` interceptor.
        """
        return response

    def post_update_key_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_key

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApiKeys server but before it is returned to user code.

        We recommend only using this `post_update_key_with_metadata`
        interceptor in new development instead of the `post_update_key` interceptor.
        When both interceptors are used, this `post_update_key_with_metadata` interceptor runs after the
        `post_update_key` interceptor. The (possibly modified) response returned by
        `post_update_key` will be passed to
        `post_update_key_with_metadata`.
        """
        return response, metadata

    def pre_get_operation(
        self,
        request: operations_pb2.GetOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.GetOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApiKeys server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the ApiKeys server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class ApiKeysRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ApiKeysRestInterceptor


class ApiKeysRestTransport(_BaseApiKeysRestTransport):
    """REST backend synchronous transport for ApiKeys.

    Manages the API keys associated with projects.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "apikeys.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[ApiKeysRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'apikeys.googleapis.com').
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
            interceptor (Optional[ApiKeysRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or ApiKeysRestInterceptor()
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
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v2/{name=operations/*}",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v2",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _CreateKey(_BaseApiKeysRestTransport._BaseCreateKey, ApiKeysRestStub):
        def __hash__(self):
            return hash("ApiKeysRestTransport.CreateKey")

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
            request: apikeys.CreateKeyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create key method over HTTP.

            Args:
                request (~.apikeys.CreateKeyRequest):
                    The request object. Request message for ``CreateKey`` method.
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

            http_options = _BaseApiKeysRestTransport._BaseCreateKey._get_http_options()
            request, metadata = self._interceptor.pre_create_key(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiKeysRestTransport._BaseCreateKey,
                    "_BaseCreateKey__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.api.apikeys_v2.ApiKeysClient.CreateKey",
                    extra={
                        "serviceName": "google.api.apikeys.v2.ApiKeys",
                        "rpcName": "CreateKey",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiKeysRestTransport._CreateKey._get_response(
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

            resp = self._interceptor.post_create_key(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_key_with_metadata(
                resp, response_metadata
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
                    "Received response for google.api.apikeys_v2.ApiKeysClient.create_key",
                    extra={
                        "serviceName": "google.api.apikeys.v2.ApiKeys",
                        "rpcName": "CreateKey",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteKey(_BaseApiKeysRestTransport._BaseDeleteKey, ApiKeysRestStub):
        def __hash__(self):
            return hash("ApiKeysRestTransport.DeleteKey")

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
            request: apikeys.DeleteKeyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete key method over HTTP.

            Args:
                request (~.apikeys.DeleteKeyRequest):
                    The request object. Request message for ``DeleteKey`` method.
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

            http_options = _BaseApiKeysRestTransport._BaseDeleteKey._get_http_options()
            request, metadata = self._interceptor.pre_delete_key(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiKeysRestTransport._BaseDeleteKey,
                    "_BaseDeleteKey__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.api.apikeys_v2.ApiKeysClient.DeleteKey",
                    extra={
                        "serviceName": "google.api.apikeys.v2.ApiKeys",
                        "rpcName": "DeleteKey",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiKeysRestTransport._DeleteKey._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_key(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_key_with_metadata(
                resp, response_metadata
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
                    "Received response for google.api.apikeys_v2.ApiKeysClient.delete_key",
                    extra={
                        "serviceName": "google.api.apikeys.v2.ApiKeys",
                        "rpcName": "DeleteKey",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetKey(_BaseApiKeysRestTransport._BaseGetKey, ApiKeysRestStub):
        def __hash__(self):
            return hash("ApiKeysRestTransport.GetKey")

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
            request: apikeys.GetKeyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Key:
            r"""Call the get key method over HTTP.

            Args:
                request (~.apikeys.GetKeyRequest):
                    The request object. Request message for ``GetKey`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Key:
                    The representation of a key managed
                by the API Keys API.

            """

            http_options = _BaseApiKeysRestTransport._BaseGetKey._get_http_options()
            request, metadata = self._interceptor.pre_get_key(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiKeysRestTransport._BaseGetKey,
                    "_BaseGetKey__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.api.apikeys_v2.ApiKeysClient.GetKey",
                    extra={
                        "serviceName": "google.api.apikeys.v2.ApiKeys",
                        "rpcName": "GetKey",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiKeysRestTransport._GetKey._get_response(
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
            resp = resources.Key()
            pb_resp = resources.Key.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_key(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_key_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Key.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.api.apikeys_v2.ApiKeysClient.get_key",
                    extra={
                        "serviceName": "google.api.apikeys.v2.ApiKeys",
                        "rpcName": "GetKey",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetKeyString(_BaseApiKeysRestTransport._BaseGetKeyString, ApiKeysRestStub):
        def __hash__(self):
            return hash("ApiKeysRestTransport.GetKeyString")

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
            request: apikeys.GetKeyStringRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> apikeys.GetKeyStringResponse:
            r"""Call the get key string method over HTTP.

            Args:
                request (~.apikeys.GetKeyStringRequest):
                    The request object. Request message for ``GetKeyString`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.apikeys.GetKeyStringResponse:
                    Response message for ``GetKeyString`` method.
            """

            http_options = (
                _BaseApiKeysRestTransport._BaseGetKeyString._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_key_string(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiKeysRestTransport._BaseGetKeyString,
                    "_BaseGetKeyString__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.api.apikeys_v2.ApiKeysClient.GetKeyString",
                    extra={
                        "serviceName": "google.api.apikeys.v2.ApiKeys",
                        "rpcName": "GetKeyString",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiKeysRestTransport._GetKeyString._get_response(
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
            resp = apikeys.GetKeyStringResponse()
            pb_resp = apikeys.GetKeyStringResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_key_string(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_key_string_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = apikeys.GetKeyStringResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.api.apikeys_v2.ApiKeysClient.get_key_string",
                    extra={
                        "serviceName": "google.api.apikeys.v2.ApiKeys",
                        "rpcName": "GetKeyString",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListKeys(_BaseApiKeysRestTransport._BaseListKeys, ApiKeysRestStub):
        def __hash__(self):
            return hash("ApiKeysRestTransport.ListKeys")

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
            request: apikeys.ListKeysRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> apikeys.ListKeysResponse:
            r"""Call the list keys method over HTTP.

            Args:
                request (~.apikeys.ListKeysRequest):
                    The request object. Request message for ``ListKeys`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.apikeys.ListKeysResponse:
                    Response message for ``ListKeys`` method.
            """

            http_options = _BaseApiKeysRestTransport._BaseListKeys._get_http_options()
            request, metadata = self._interceptor.pre_list_keys(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiKeysRestTransport._BaseListKeys,
                    "_BaseListKeys__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.api.apikeys_v2.ApiKeysClient.ListKeys",
                    extra={
                        "serviceName": "google.api.apikeys.v2.ApiKeys",
                        "rpcName": "ListKeys",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiKeysRestTransport._ListKeys._get_response(
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
            resp = apikeys.ListKeysResponse()
            pb_resp = apikeys.ListKeysResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_keys(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_keys_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = apikeys.ListKeysResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.api.apikeys_v2.ApiKeysClient.list_keys",
                    extra={
                        "serviceName": "google.api.apikeys.v2.ApiKeys",
                        "rpcName": "ListKeys",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _LookupKey(_BaseApiKeysRestTransport._BaseLookupKey, ApiKeysRestStub):
        def __hash__(self):
            return hash("ApiKeysRestTransport.LookupKey")

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
            request: apikeys.LookupKeyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> apikeys.LookupKeyResponse:
            r"""Call the lookup key method over HTTP.

            Args:
                request (~.apikeys.LookupKeyRequest):
                    The request object. Request message for ``LookupKey`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.apikeys.LookupKeyResponse:
                    Response message for ``LookupKey`` method.
            """

            http_options = _BaseApiKeysRestTransport._BaseLookupKey._get_http_options()
            request, metadata = self._interceptor.pre_lookup_key(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiKeysRestTransport._BaseLookupKey,
                    "_BaseLookupKey__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.api.apikeys_v2.ApiKeysClient.LookupKey",
                    extra={
                        "serviceName": "google.api.apikeys.v2.ApiKeys",
                        "rpcName": "LookupKey",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiKeysRestTransport._LookupKey._get_response(
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
            resp = apikeys.LookupKeyResponse()
            pb_resp = apikeys.LookupKeyResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_lookup_key(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_lookup_key_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = apikeys.LookupKeyResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.api.apikeys_v2.ApiKeysClient.lookup_key",
                    extra={
                        "serviceName": "google.api.apikeys.v2.ApiKeys",
                        "rpcName": "LookupKey",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UndeleteKey(_BaseApiKeysRestTransport._BaseUndeleteKey, ApiKeysRestStub):
        def __hash__(self):
            return hash("ApiKeysRestTransport.UndeleteKey")

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
            request: apikeys.UndeleteKeyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the undelete key method over HTTP.

            Args:
                request (~.apikeys.UndeleteKeyRequest):
                    The request object. Request message for ``UndeleteKey`` method.
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

            http_options = (
                _BaseApiKeysRestTransport._BaseUndeleteKey._get_http_options()
            )
            request, metadata = self._interceptor.pre_undelete_key(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiKeysRestTransport._BaseUndeleteKey,
                    "_BaseUndeleteKey__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.api.apikeys_v2.ApiKeysClient.UndeleteKey",
                    extra={
                        "serviceName": "google.api.apikeys.v2.ApiKeys",
                        "rpcName": "UndeleteKey",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiKeysRestTransport._UndeleteKey._get_response(
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

            resp = self._interceptor.post_undelete_key(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_undelete_key_with_metadata(
                resp, response_metadata
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
                    "Received response for google.api.apikeys_v2.ApiKeysClient.undelete_key",
                    extra={
                        "serviceName": "google.api.apikeys.v2.ApiKeys",
                        "rpcName": "UndeleteKey",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateKey(_BaseApiKeysRestTransport._BaseUpdateKey, ApiKeysRestStub):
        def __hash__(self):
            return hash("ApiKeysRestTransport.UpdateKey")

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
            request: apikeys.UpdateKeyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update key method over HTTP.

            Args:
                request (~.apikeys.UpdateKeyRequest):
                    The request object. Request message for ``UpdateKey`` method.
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

            http_options = _BaseApiKeysRestTransport._BaseUpdateKey._get_http_options()
            request, metadata = self._interceptor.pre_update_key(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiKeysRestTransport._BaseUpdateKey,
                    "_BaseUpdateKey__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.api.apikeys_v2.ApiKeysClient.UpdateKey",
                    extra={
                        "serviceName": "google.api.apikeys.v2.ApiKeys",
                        "rpcName": "UpdateKey",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiKeysRestTransport._UpdateKey._get_response(
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

            resp = self._interceptor.post_update_key(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_key_with_metadata(
                resp, response_metadata
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
                    "Received response for google.api.apikeys_v2.ApiKeysClient.update_key",
                    extra={
                        "serviceName": "google.api.apikeys.v2.ApiKeys",
                        "rpcName": "UpdateKey",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_key(
        self,
    ) -> Callable[[apikeys.CreateKeyRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateKey(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_key(
        self,
    ) -> Callable[[apikeys.DeleteKeyRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteKey(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_key(self) -> Callable[[apikeys.GetKeyRequest], resources.Key]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetKey(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_key_string(
        self,
    ) -> Callable[[apikeys.GetKeyStringRequest], apikeys.GetKeyStringResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetKeyString(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_keys(
        self,
    ) -> Callable[[apikeys.ListKeysRequest], apikeys.ListKeysResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListKeys(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def lookup_key(
        self,
    ) -> Callable[[apikeys.LookupKeyRequest], apikeys.LookupKeyResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._LookupKey(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def undelete_key(
        self,
    ) -> Callable[[apikeys.UndeleteKeyRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UndeleteKey(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_key(
        self,
    ) -> Callable[[apikeys.UpdateKeyRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateKey(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(_BaseApiKeysRestTransport._BaseGetOperation, ApiKeysRestStub):
        def __hash__(self):
            return hash("ApiKeysRestTransport.GetOperation")

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
                _BaseApiKeysRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApiKeysRestTransport._BaseGetOperation,
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
                    f"Sending request for google.api.apikeys_v2.ApiKeysClient.GetOperation",
                    extra={
                        "serviceName": "google.api.apikeys.v2.ApiKeys",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApiKeysRestTransport._GetOperation._get_response(
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
                    "Received response for google.api.apikeys_v2.ApiKeysAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.api.apikeys.v2.ApiKeys",
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


__all__ = ("ApiKeysRestTransport",)
