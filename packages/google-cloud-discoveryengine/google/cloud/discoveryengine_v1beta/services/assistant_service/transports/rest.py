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
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.discoveryengine_v1beta._compat import transcode_request
from google.cloud.discoveryengine_v1beta.types import assistant, assistant_service
from google.cloud.discoveryengine_v1beta.types import assistant as gcd_assistant

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseAssistantServiceRestTransport

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


class AssistantServiceRestInterceptor:
    """Interceptor for AssistantService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the AssistantServiceRestTransport.

    .. code-block:: python
        class MyCustomAssistantServiceInterceptor(AssistantServiceRestInterceptor):
            def pre_create_assistant(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_assistant(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_assistant(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_assistant(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_assistant(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_assistants(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_assistants(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_stream_assist(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_stream_assist(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_assistant(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_assistant(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = AssistantServiceRestTransport(interceptor=MyCustomAssistantServiceInterceptor())
        client = AssistantServiceClient(transport=transport)


    """

    def pre_create_assistant(
        self,
        request: assistant_service.CreateAssistantRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        assistant_service.CreateAssistantRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_assistant

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssistantService server.
        """
        return request, metadata

    def post_create_assistant(
        self, response: assistant.Assistant
    ) -> assistant.Assistant:
        """Post-rpc interceptor for create_assistant

        DEPRECATED. Please use the `post_create_assistant_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AssistantService server but before
        it is returned to user code. This `post_create_assistant` interceptor runs
        before the `post_create_assistant_with_metadata` interceptor.
        """
        return response

    def post_create_assistant_with_metadata(
        self,
        response: assistant.Assistant,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[assistant.Assistant, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_assistant

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AssistantService server but before it is returned to user code.

        We recommend only using this `post_create_assistant_with_metadata`
        interceptor in new development instead of the `post_create_assistant` interceptor.
        When both interceptors are used, this `post_create_assistant_with_metadata` interceptor runs after the
        `post_create_assistant` interceptor. The (possibly modified) response returned by
        `post_create_assistant` will be passed to
        `post_create_assistant_with_metadata`.
        """
        return response, metadata

    def pre_delete_assistant(
        self,
        request: assistant_service.DeleteAssistantRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        assistant_service.DeleteAssistantRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_assistant

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssistantService server.
        """
        return request, metadata

    def pre_get_assistant(
        self,
        request: assistant_service.GetAssistantRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        assistant_service.GetAssistantRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_assistant

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssistantService server.
        """
        return request, metadata

    def post_get_assistant(self, response: assistant.Assistant) -> assistant.Assistant:
        """Post-rpc interceptor for get_assistant

        DEPRECATED. Please use the `post_get_assistant_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AssistantService server but before
        it is returned to user code. This `post_get_assistant` interceptor runs
        before the `post_get_assistant_with_metadata` interceptor.
        """
        return response

    def post_get_assistant_with_metadata(
        self,
        response: assistant.Assistant,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[assistant.Assistant, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_assistant

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AssistantService server but before it is returned to user code.

        We recommend only using this `post_get_assistant_with_metadata`
        interceptor in new development instead of the `post_get_assistant` interceptor.
        When both interceptors are used, this `post_get_assistant_with_metadata` interceptor runs after the
        `post_get_assistant` interceptor. The (possibly modified) response returned by
        `post_get_assistant` will be passed to
        `post_get_assistant_with_metadata`.
        """
        return response, metadata

    def pre_list_assistants(
        self,
        request: assistant_service.ListAssistantsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        assistant_service.ListAssistantsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_assistants

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssistantService server.
        """
        return request, metadata

    def post_list_assistants(
        self, response: assistant_service.ListAssistantsResponse
    ) -> assistant_service.ListAssistantsResponse:
        """Post-rpc interceptor for list_assistants

        DEPRECATED. Please use the `post_list_assistants_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AssistantService server but before
        it is returned to user code. This `post_list_assistants` interceptor runs
        before the `post_list_assistants_with_metadata` interceptor.
        """
        return response

    def post_list_assistants_with_metadata(
        self,
        response: assistant_service.ListAssistantsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        assistant_service.ListAssistantsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_assistants

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AssistantService server but before it is returned to user code.

        We recommend only using this `post_list_assistants_with_metadata`
        interceptor in new development instead of the `post_list_assistants` interceptor.
        When both interceptors are used, this `post_list_assistants_with_metadata` interceptor runs after the
        `post_list_assistants` interceptor. The (possibly modified) response returned by
        `post_list_assistants` will be passed to
        `post_list_assistants_with_metadata`.
        """
        return response, metadata

    def pre_stream_assist(
        self,
        request: assistant_service.StreamAssistRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        assistant_service.StreamAssistRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for stream_assist

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssistantService server.
        """
        return request, metadata

    def post_stream_assist(
        self, response: rest_streaming.ResponseIterator
    ) -> rest_streaming.ResponseIterator:
        """Post-rpc interceptor for stream_assist

        DEPRECATED. Please use the `post_stream_assist_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AssistantService server but before
        it is returned to user code. This `post_stream_assist` interceptor runs
        before the `post_stream_assist_with_metadata` interceptor.
        """
        return response

    def post_stream_assist_with_metadata(
        self,
        response: rest_streaming.ResponseIterator,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        rest_streaming.ResponseIterator, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for stream_assist

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AssistantService server but before it is returned to user code.

        We recommend only using this `post_stream_assist_with_metadata`
        interceptor in new development instead of the `post_stream_assist` interceptor.
        When both interceptors are used, this `post_stream_assist_with_metadata` interceptor runs after the
        `post_stream_assist` interceptor. The (possibly modified) response returned by
        `post_stream_assist` will be passed to
        `post_stream_assist_with_metadata`.
        """
        return response, metadata

    def pre_update_assistant(
        self,
        request: assistant_service.UpdateAssistantRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        assistant_service.UpdateAssistantRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_assistant

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssistantService server.
        """
        return request, metadata

    def post_update_assistant(
        self, response: gcd_assistant.Assistant
    ) -> gcd_assistant.Assistant:
        """Post-rpc interceptor for update_assistant

        DEPRECATED. Please use the `post_update_assistant_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AssistantService server but before
        it is returned to user code. This `post_update_assistant` interceptor runs
        before the `post_update_assistant_with_metadata` interceptor.
        """
        return response

    def post_update_assistant_with_metadata(
        self,
        response: gcd_assistant.Assistant,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcd_assistant.Assistant, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_assistant

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AssistantService server but before it is returned to user code.

        We recommend only using this `post_update_assistant_with_metadata`
        interceptor in new development instead of the `post_update_assistant` interceptor.
        When both interceptors are used, this `post_update_assistant_with_metadata` interceptor runs after the
        `post_update_assistant` interceptor. The (possibly modified) response returned by
        `post_update_assistant` will be passed to
        `post_update_assistant_with_metadata`.
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
        before they are sent to the AssistantService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the AssistantService server but before
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
        before they are sent to the AssistantService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the AssistantService server but before
        it is returned to user code.
        """
        return response

    def pre_list_operations(
        self,
        request: operations_pb2.ListOperationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.ListOperationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_operations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AssistantService server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the AssistantService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class AssistantServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: AssistantServiceRestInterceptor


class AssistantServiceRestTransport(_BaseAssistantServiceRestTransport):
    """REST backend synchronous transport for AssistantService.

    Service for managing Assistant configuration and assisting
    users.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "discoveryengine.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[AssistantServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'discoveryengine.googleapis.com').
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
            interceptor (Optional[AssistantServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or AssistantServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateAssistant(
        _BaseAssistantServiceRestTransport._BaseCreateAssistant,
        AssistantServiceRestStub,
    ):
        def __hash__(self):
            return hash("AssistantServiceRestTransport.CreateAssistant")

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
            request: assistant_service.CreateAssistantRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> assistant.Assistant:
            r"""Call the create assistant method over HTTP.

            Args:
                request (~.assistant_service.CreateAssistantRequest):
                    The request object. Request for the
                [AssistantService.CreateAssistant][google.cloud.discoveryengine.v1beta.AssistantService.CreateAssistant]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.assistant.Assistant:
                    Discovery Engine Assistant resource.
            """

            http_options = _BaseAssistantServiceRestTransport._BaseCreateAssistant._get_http_options()
            request, metadata = self._interceptor.pre_create_assistant(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAssistantServiceRestTransport._BaseCreateAssistant,
                    "_BaseCreateAssistant__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.discoveryengine_v1beta.AssistantServiceClient.CreateAssistant",
                    extra={
                        "serviceName": "google.cloud.discoveryengine.v1beta.AssistantService",
                        "rpcName": "CreateAssistant",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AssistantServiceRestTransport._CreateAssistant._get_response(
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
            resp = assistant.Assistant()
            pb_resp = assistant.Assistant.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_assistant(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_assistant_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = assistant.Assistant.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.discoveryengine_v1beta.AssistantServiceClient.create_assistant",
                    extra={
                        "serviceName": "google.cloud.discoveryengine.v1beta.AssistantService",
                        "rpcName": "CreateAssistant",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteAssistant(
        _BaseAssistantServiceRestTransport._BaseDeleteAssistant,
        AssistantServiceRestStub,
    ):
        def __hash__(self):
            return hash("AssistantServiceRestTransport.DeleteAssistant")

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
            request: assistant_service.DeleteAssistantRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete assistant method over HTTP.

            Args:
                request (~.assistant_service.DeleteAssistantRequest):
                    The request object. Request message for the
                [AssistantService.DeleteAssistant][google.cloud.discoveryengine.v1beta.AssistantService.DeleteAssistant]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseAssistantServiceRestTransport._BaseDeleteAssistant._get_http_options()
            request, metadata = self._interceptor.pre_delete_assistant(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAssistantServiceRestTransport._BaseDeleteAssistant,
                    "_BaseDeleteAssistant__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.discoveryengine_v1beta.AssistantServiceClient.DeleteAssistant",
                    extra={
                        "serviceName": "google.cloud.discoveryengine.v1beta.AssistantService",
                        "rpcName": "DeleteAssistant",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AssistantServiceRestTransport._DeleteAssistant._get_response(
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

    class _GetAssistant(
        _BaseAssistantServiceRestTransport._BaseGetAssistant, AssistantServiceRestStub
    ):
        def __hash__(self):
            return hash("AssistantServiceRestTransport.GetAssistant")

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
            request: assistant_service.GetAssistantRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> assistant.Assistant:
            r"""Call the get assistant method over HTTP.

            Args:
                request (~.assistant_service.GetAssistantRequest):
                    The request object. Request message for the
                [AssistantService.GetAssistant][google.cloud.discoveryengine.v1beta.AssistantService.GetAssistant]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.assistant.Assistant:
                    Discovery Engine Assistant resource.
            """

            http_options = (
                _BaseAssistantServiceRestTransport._BaseGetAssistant._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_assistant(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAssistantServiceRestTransport._BaseGetAssistant,
                    "_BaseGetAssistant__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.discoveryengine_v1beta.AssistantServiceClient.GetAssistant",
                    extra={
                        "serviceName": "google.cloud.discoveryengine.v1beta.AssistantService",
                        "rpcName": "GetAssistant",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AssistantServiceRestTransport._GetAssistant._get_response(
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
            resp = assistant.Assistant()
            pb_resp = assistant.Assistant.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_assistant(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_assistant_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = assistant.Assistant.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.discoveryengine_v1beta.AssistantServiceClient.get_assistant",
                    extra={
                        "serviceName": "google.cloud.discoveryengine.v1beta.AssistantService",
                        "rpcName": "GetAssistant",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAssistants(
        _BaseAssistantServiceRestTransport._BaseListAssistants, AssistantServiceRestStub
    ):
        def __hash__(self):
            return hash("AssistantServiceRestTransport.ListAssistants")

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
            request: assistant_service.ListAssistantsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> assistant_service.ListAssistantsResponse:
            r"""Call the list assistants method over HTTP.

            Args:
                request (~.assistant_service.ListAssistantsRequest):
                    The request object. Request message for the
                [AssistantService.ListAssistants][google.cloud.discoveryengine.v1beta.AssistantService.ListAssistants]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.assistant_service.ListAssistantsResponse:
                    Response message for the
                [AssistantService.ListAssistants][google.cloud.discoveryengine.v1beta.AssistantService.ListAssistants]
                method.

            """

            http_options = _BaseAssistantServiceRestTransport._BaseListAssistants._get_http_options()
            request, metadata = self._interceptor.pre_list_assistants(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAssistantServiceRestTransport._BaseListAssistants,
                    "_BaseListAssistants__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.discoveryengine_v1beta.AssistantServiceClient.ListAssistants",
                    extra={
                        "serviceName": "google.cloud.discoveryengine.v1beta.AssistantService",
                        "rpcName": "ListAssistants",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AssistantServiceRestTransport._ListAssistants._get_response(
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
            resp = assistant_service.ListAssistantsResponse()
            pb_resp = assistant_service.ListAssistantsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_assistants(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_assistants_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = assistant_service.ListAssistantsResponse.to_json(
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
                    "Received response for google.cloud.discoveryengine_v1beta.AssistantServiceClient.list_assistants",
                    extra={
                        "serviceName": "google.cloud.discoveryengine.v1beta.AssistantService",
                        "rpcName": "ListAssistants",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _StreamAssist(
        _BaseAssistantServiceRestTransport._BaseStreamAssist, AssistantServiceRestStub
    ):
        def __hash__(self):
            return hash("AssistantServiceRestTransport.StreamAssist")

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
                stream=True,
            )
            return response

        def __call__(
            self,
            request: assistant_service.StreamAssistRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> rest_streaming.ResponseIterator:
            r"""Call the stream assist method over HTTP.

            Args:
                request (~.assistant_service.StreamAssistRequest):
                    The request object. Request for the
                [AssistantService.StreamAssist][google.cloud.discoveryengine.v1beta.AssistantService.StreamAssist]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.assistant_service.StreamAssistResponse:
                    Response for the
                [AssistantService.StreamAssist][google.cloud.discoveryengine.v1beta.AssistantService.StreamAssist]
                method.

            """

            http_options = (
                _BaseAssistantServiceRestTransport._BaseStreamAssist._get_http_options()
            )
            request, metadata = self._interceptor.pre_stream_assist(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAssistantServiceRestTransport._BaseStreamAssist,
                    "_BaseStreamAssist__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.discoveryengine_v1beta.AssistantServiceClient.StreamAssist",
                    extra={
                        "serviceName": "google.cloud.discoveryengine.v1beta.AssistantService",
                        "rpcName": "StreamAssist",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AssistantServiceRestTransport._StreamAssist._get_response(
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
            resp = rest_streaming.ResponseIterator(
                response, assistant_service.StreamAssistResponse
            )

            resp = self._interceptor.post_stream_assist(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_stream_assist_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                http_response = {
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.discoveryengine_v1beta.AssistantServiceClient.stream_assist",
                    extra={
                        "serviceName": "google.cloud.discoveryengine.v1beta.AssistantService",
                        "rpcName": "StreamAssist",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateAssistant(
        _BaseAssistantServiceRestTransport._BaseUpdateAssistant,
        AssistantServiceRestStub,
    ):
        def __hash__(self):
            return hash("AssistantServiceRestTransport.UpdateAssistant")

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
            request: assistant_service.UpdateAssistantRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcd_assistant.Assistant:
            r"""Call the update assistant method over HTTP.

            Args:
                request (~.assistant_service.UpdateAssistantRequest):
                    The request object. Request message for the
                [AssistantService.UpdateAssistant][google.cloud.discoveryengine.v1beta.AssistantService.UpdateAssistant]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcd_assistant.Assistant:
                    Discovery Engine Assistant resource.
            """

            http_options = _BaseAssistantServiceRestTransport._BaseUpdateAssistant._get_http_options()
            request, metadata = self._interceptor.pre_update_assistant(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAssistantServiceRestTransport._BaseUpdateAssistant,
                    "_BaseUpdateAssistant__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.discoveryengine_v1beta.AssistantServiceClient.UpdateAssistant",
                    extra={
                        "serviceName": "google.cloud.discoveryengine.v1beta.AssistantService",
                        "rpcName": "UpdateAssistant",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AssistantServiceRestTransport._UpdateAssistant._get_response(
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
            resp = gcd_assistant.Assistant()
            pb_resp = gcd_assistant.Assistant.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_assistant(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_assistant_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcd_assistant.Assistant.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.discoveryengine_v1beta.AssistantServiceClient.update_assistant",
                    extra={
                        "serviceName": "google.cloud.discoveryengine.v1beta.AssistantService",
                        "rpcName": "UpdateAssistant",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_assistant(
        self,
    ) -> Callable[[assistant_service.CreateAssistantRequest], assistant.Assistant]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateAssistant(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_assistant(
        self,
    ) -> Callable[[assistant_service.DeleteAssistantRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteAssistant(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_assistant(
        self,
    ) -> Callable[[assistant_service.GetAssistantRequest], assistant.Assistant]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAssistant(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_assistants(
        self,
    ) -> Callable[
        [assistant_service.ListAssistantsRequest],
        assistant_service.ListAssistantsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAssistants(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def stream_assist(
        self,
    ) -> Callable[
        [assistant_service.StreamAssistRequest], assistant_service.StreamAssistResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StreamAssist(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_assistant(
        self,
    ) -> Callable[[assistant_service.UpdateAssistantRequest], gcd_assistant.Assistant]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateAssistant(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseAssistantServiceRestTransport._BaseCancelOperation,
        AssistantServiceRestStub,
    ):
        def __hash__(self):
            return hash("AssistantServiceRestTransport.CancelOperation")

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

            http_options = _BaseAssistantServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAssistantServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.discoveryengine_v1beta.AssistantServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.discoveryengine.v1beta.AssistantService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AssistantServiceRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseAssistantServiceRestTransport._BaseGetOperation, AssistantServiceRestStub
    ):
        def __hash__(self):
            return hash("AssistantServiceRestTransport.GetOperation")

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
                _BaseAssistantServiceRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAssistantServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.discoveryengine_v1beta.AssistantServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.discoveryengine.v1beta.AssistantService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AssistantServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.discoveryengine_v1beta.AssistantServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.discoveryengine.v1beta.AssistantService",
                        "rpcName": "GetOperation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_operations(self):
        return self._ListOperations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListOperations(
        _BaseAssistantServiceRestTransport._BaseListOperations, AssistantServiceRestStub
    ):
        def __hash__(self):
            return hash("AssistantServiceRestTransport.ListOperations")

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
            request: operations_pb2.ListOperationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.ListOperationsResponse:
            r"""Call the list operations method over HTTP.

            Args:
                request (operations_pb2.ListOperationsRequest):
                    The request object for ListOperations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                operations_pb2.ListOperationsResponse: Response from ListOperations method.
            """

            http_options = _BaseAssistantServiceRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAssistantServiceRestTransport._BaseListOperations,
                    "_BaseListOperations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.discoveryengine_v1beta.AssistantServiceClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.discoveryengine.v1beta.AssistantService",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AssistantServiceRestTransport._ListOperations._get_response(
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
            resp = operations_pb2.ListOperationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_operations(resp)
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
                    "Received response for google.cloud.discoveryengine_v1beta.AssistantServiceAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.discoveryengine.v1beta.AssistantService",
                        "rpcName": "ListOperations",
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


__all__ = ("AssistantServiceRestTransport",)
