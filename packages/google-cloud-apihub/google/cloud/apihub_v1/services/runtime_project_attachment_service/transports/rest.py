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

from google.cloud.apihub_v1._compat import transcode_request
from google.cloud.apihub_v1.types import runtime_project_attachment_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseRuntimeProjectAttachmentServiceRestTransport

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


class RuntimeProjectAttachmentServiceRestInterceptor:
    """Interceptor for RuntimeProjectAttachmentService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the RuntimeProjectAttachmentServiceRestTransport.

    .. code-block:: python
        class MyCustomRuntimeProjectAttachmentServiceInterceptor(RuntimeProjectAttachmentServiceRestInterceptor):
            def pre_create_runtime_project_attachment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_runtime_project_attachment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_runtime_project_attachment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_runtime_project_attachment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_runtime_project_attachment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_runtime_project_attachments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_runtime_project_attachments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_lookup_runtime_project_attachment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_lookup_runtime_project_attachment(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = RuntimeProjectAttachmentServiceRestTransport(interceptor=MyCustomRuntimeProjectAttachmentServiceInterceptor())
        client = RuntimeProjectAttachmentServiceClient(transport=transport)


    """

    def pre_create_runtime_project_attachment(
        self,
        request: runtime_project_attachment_service.CreateRuntimeProjectAttachmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        runtime_project_attachment_service.CreateRuntimeProjectAttachmentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_runtime_project_attachment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RuntimeProjectAttachmentService server.
        """
        return request, metadata

    def post_create_runtime_project_attachment(
        self, response: runtime_project_attachment_service.RuntimeProjectAttachment
    ) -> runtime_project_attachment_service.RuntimeProjectAttachment:
        """Post-rpc interceptor for create_runtime_project_attachment

        DEPRECATED. Please use the `post_create_runtime_project_attachment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RuntimeProjectAttachmentService server but before
        it is returned to user code. This `post_create_runtime_project_attachment` interceptor runs
        before the `post_create_runtime_project_attachment_with_metadata` interceptor.
        """
        return response

    def post_create_runtime_project_attachment_with_metadata(
        self,
        response: runtime_project_attachment_service.RuntimeProjectAttachment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        runtime_project_attachment_service.RuntimeProjectAttachment,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for create_runtime_project_attachment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RuntimeProjectAttachmentService server but before it is returned to user code.

        We recommend only using this `post_create_runtime_project_attachment_with_metadata`
        interceptor in new development instead of the `post_create_runtime_project_attachment` interceptor.
        When both interceptors are used, this `post_create_runtime_project_attachment_with_metadata` interceptor runs after the
        `post_create_runtime_project_attachment` interceptor. The (possibly modified) response returned by
        `post_create_runtime_project_attachment` will be passed to
        `post_create_runtime_project_attachment_with_metadata`.
        """
        return response, metadata

    def pre_delete_runtime_project_attachment(
        self,
        request: runtime_project_attachment_service.DeleteRuntimeProjectAttachmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        runtime_project_attachment_service.DeleteRuntimeProjectAttachmentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_runtime_project_attachment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RuntimeProjectAttachmentService server.
        """
        return request, metadata

    def pre_get_runtime_project_attachment(
        self,
        request: runtime_project_attachment_service.GetRuntimeProjectAttachmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        runtime_project_attachment_service.GetRuntimeProjectAttachmentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_runtime_project_attachment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RuntimeProjectAttachmentService server.
        """
        return request, metadata

    def post_get_runtime_project_attachment(
        self, response: runtime_project_attachment_service.RuntimeProjectAttachment
    ) -> runtime_project_attachment_service.RuntimeProjectAttachment:
        """Post-rpc interceptor for get_runtime_project_attachment

        DEPRECATED. Please use the `post_get_runtime_project_attachment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RuntimeProjectAttachmentService server but before
        it is returned to user code. This `post_get_runtime_project_attachment` interceptor runs
        before the `post_get_runtime_project_attachment_with_metadata` interceptor.
        """
        return response

    def post_get_runtime_project_attachment_with_metadata(
        self,
        response: runtime_project_attachment_service.RuntimeProjectAttachment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        runtime_project_attachment_service.RuntimeProjectAttachment,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_runtime_project_attachment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RuntimeProjectAttachmentService server but before it is returned to user code.

        We recommend only using this `post_get_runtime_project_attachment_with_metadata`
        interceptor in new development instead of the `post_get_runtime_project_attachment` interceptor.
        When both interceptors are used, this `post_get_runtime_project_attachment_with_metadata` interceptor runs after the
        `post_get_runtime_project_attachment` interceptor. The (possibly modified) response returned by
        `post_get_runtime_project_attachment` will be passed to
        `post_get_runtime_project_attachment_with_metadata`.
        """
        return response, metadata

    def pre_list_runtime_project_attachments(
        self,
        request: runtime_project_attachment_service.ListRuntimeProjectAttachmentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        runtime_project_attachment_service.ListRuntimeProjectAttachmentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_runtime_project_attachments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RuntimeProjectAttachmentService server.
        """
        return request, metadata

    def post_list_runtime_project_attachments(
        self,
        response: runtime_project_attachment_service.ListRuntimeProjectAttachmentsResponse,
    ) -> runtime_project_attachment_service.ListRuntimeProjectAttachmentsResponse:
        """Post-rpc interceptor for list_runtime_project_attachments

        DEPRECATED. Please use the `post_list_runtime_project_attachments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RuntimeProjectAttachmentService server but before
        it is returned to user code. This `post_list_runtime_project_attachments` interceptor runs
        before the `post_list_runtime_project_attachments_with_metadata` interceptor.
        """
        return response

    def post_list_runtime_project_attachments_with_metadata(
        self,
        response: runtime_project_attachment_service.ListRuntimeProjectAttachmentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        runtime_project_attachment_service.ListRuntimeProjectAttachmentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_runtime_project_attachments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RuntimeProjectAttachmentService server but before it is returned to user code.

        We recommend only using this `post_list_runtime_project_attachments_with_metadata`
        interceptor in new development instead of the `post_list_runtime_project_attachments` interceptor.
        When both interceptors are used, this `post_list_runtime_project_attachments_with_metadata` interceptor runs after the
        `post_list_runtime_project_attachments` interceptor. The (possibly modified) response returned by
        `post_list_runtime_project_attachments` will be passed to
        `post_list_runtime_project_attachments_with_metadata`.
        """
        return response, metadata

    def pre_lookup_runtime_project_attachment(
        self,
        request: runtime_project_attachment_service.LookupRuntimeProjectAttachmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        runtime_project_attachment_service.LookupRuntimeProjectAttachmentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for lookup_runtime_project_attachment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RuntimeProjectAttachmentService server.
        """
        return request, metadata

    def post_lookup_runtime_project_attachment(
        self,
        response: runtime_project_attachment_service.LookupRuntimeProjectAttachmentResponse,
    ) -> runtime_project_attachment_service.LookupRuntimeProjectAttachmentResponse:
        """Post-rpc interceptor for lookup_runtime_project_attachment

        DEPRECATED. Please use the `post_lookup_runtime_project_attachment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the RuntimeProjectAttachmentService server but before
        it is returned to user code. This `post_lookup_runtime_project_attachment` interceptor runs
        before the `post_lookup_runtime_project_attachment_with_metadata` interceptor.
        """
        return response

    def post_lookup_runtime_project_attachment_with_metadata(
        self,
        response: runtime_project_attachment_service.LookupRuntimeProjectAttachmentResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        runtime_project_attachment_service.LookupRuntimeProjectAttachmentResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for lookup_runtime_project_attachment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the RuntimeProjectAttachmentService server but before it is returned to user code.

        We recommend only using this `post_lookup_runtime_project_attachment_with_metadata`
        interceptor in new development instead of the `post_lookup_runtime_project_attachment` interceptor.
        When both interceptors are used, this `post_lookup_runtime_project_attachment_with_metadata` interceptor runs after the
        `post_lookup_runtime_project_attachment` interceptor. The (possibly modified) response returned by
        `post_lookup_runtime_project_attachment` will be passed to
        `post_lookup_runtime_project_attachment_with_metadata`.
        """
        return response, metadata

    def pre_get_location(
        self,
        request: locations_pb2.GetLocationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        locations_pb2.GetLocationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_location

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RuntimeProjectAttachmentService server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the RuntimeProjectAttachmentService server but before
        it is returned to user code.
        """
        return response

    def pre_list_locations(
        self,
        request: locations_pb2.ListLocationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        locations_pb2.ListLocationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_locations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RuntimeProjectAttachmentService server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the RuntimeProjectAttachmentService server but before
        it is returned to user code.
        """
        return response

    def pre_cancel_operation(
        self,
        request: operations_pb2.CancelOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.CancelOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RuntimeProjectAttachmentService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the RuntimeProjectAttachmentService server but before
        it is returned to user code.
        """
        return response

    def pre_delete_operation(
        self,
        request: operations_pb2.DeleteOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.DeleteOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the RuntimeProjectAttachmentService server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the RuntimeProjectAttachmentService server but before
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
        before they are sent to the RuntimeProjectAttachmentService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the RuntimeProjectAttachmentService server but before
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
        before they are sent to the RuntimeProjectAttachmentService server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the RuntimeProjectAttachmentService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class RuntimeProjectAttachmentServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: RuntimeProjectAttachmentServiceRestInterceptor


class RuntimeProjectAttachmentServiceRestTransport(
    _BaseRuntimeProjectAttachmentServiceRestTransport
):
    """REST backend synchronous transport for RuntimeProjectAttachmentService.

    This service is used for managing the runtime project
    attachments.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "apihub.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[RuntimeProjectAttachmentServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'apihub.googleapis.com').
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
            interceptor (Optional[RuntimeProjectAttachmentServiceRestInterceptor]): Interceptor used
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
        self._interceptor = (
            interceptor or RuntimeProjectAttachmentServiceRestInterceptor()
        )
        self._prep_wrapped_messages(client_info)

    class _CreateRuntimeProjectAttachment(
        _BaseRuntimeProjectAttachmentServiceRestTransport._BaseCreateRuntimeProjectAttachment,
        RuntimeProjectAttachmentServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "RuntimeProjectAttachmentServiceRestTransport.CreateRuntimeProjectAttachment"
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
            request: runtime_project_attachment_service.CreateRuntimeProjectAttachmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> runtime_project_attachment_service.RuntimeProjectAttachment:
            r"""Call the create runtime project
            attachment method over HTTP.

                Args:
                    request (~.runtime_project_attachment_service.CreateRuntimeProjectAttachmentRequest):
                        The request object. The
                    [CreateRuntimeProjectAttachment][google.cloud.apihub.v1.RuntimeProjectAttachmentService.CreateRuntimeProjectAttachment]
                    method's request.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.runtime_project_attachment_service.RuntimeProjectAttachment:
                        Runtime project attachment represents
                    an attachment from the runtime project
                    to the host project. Api Hub looks for
                    deployments in the attached runtime
                    projects and creates corresponding
                    resources in Api Hub for the discovered
                    deployments.

            """

            http_options = _BaseRuntimeProjectAttachmentServiceRestTransport._BaseCreateRuntimeProjectAttachment._get_http_options()
            request, metadata = self._interceptor.pre_create_runtime_project_attachment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRuntimeProjectAttachmentServiceRestTransport._BaseCreateRuntimeProjectAttachment,
                    "_BaseCreateRuntimeProjectAttachment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.RuntimeProjectAttachmentServiceClient.CreateRuntimeProjectAttachment",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.RuntimeProjectAttachmentService",
                        "rpcName": "CreateRuntimeProjectAttachment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RuntimeProjectAttachmentServiceRestTransport._CreateRuntimeProjectAttachment._get_response(
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
            resp = runtime_project_attachment_service.RuntimeProjectAttachment()
            pb_resp = runtime_project_attachment_service.RuntimeProjectAttachment.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_runtime_project_attachment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_runtime_project_attachment_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = runtime_project_attachment_service.RuntimeProjectAttachment.to_json(
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
                    "Received response for google.cloud.apihub_v1.RuntimeProjectAttachmentServiceClient.create_runtime_project_attachment",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.RuntimeProjectAttachmentService",
                        "rpcName": "CreateRuntimeProjectAttachment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteRuntimeProjectAttachment(
        _BaseRuntimeProjectAttachmentServiceRestTransport._BaseDeleteRuntimeProjectAttachment,
        RuntimeProjectAttachmentServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "RuntimeProjectAttachmentServiceRestTransport.DeleteRuntimeProjectAttachment"
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
            request: runtime_project_attachment_service.DeleteRuntimeProjectAttachmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete runtime project
            attachment method over HTTP.

                Args:
                    request (~.runtime_project_attachment_service.DeleteRuntimeProjectAttachmentRequest):
                        The request object. The
                    [DeleteRuntimeProjectAttachment][google.cloud.apihub.v1.RuntimeProjectAttachmentService.DeleteRuntimeProjectAttachment]
                    method's request.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.
            """

            http_options = _BaseRuntimeProjectAttachmentServiceRestTransport._BaseDeleteRuntimeProjectAttachment._get_http_options()
            request, metadata = self._interceptor.pre_delete_runtime_project_attachment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRuntimeProjectAttachmentServiceRestTransport._BaseDeleteRuntimeProjectAttachment,
                    "_BaseDeleteRuntimeProjectAttachment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.RuntimeProjectAttachmentServiceClient.DeleteRuntimeProjectAttachment",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.RuntimeProjectAttachmentService",
                        "rpcName": "DeleteRuntimeProjectAttachment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RuntimeProjectAttachmentServiceRestTransport._DeleteRuntimeProjectAttachment._get_response(
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

    class _GetRuntimeProjectAttachment(
        _BaseRuntimeProjectAttachmentServiceRestTransport._BaseGetRuntimeProjectAttachment,
        RuntimeProjectAttachmentServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "RuntimeProjectAttachmentServiceRestTransport.GetRuntimeProjectAttachment"
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
            request: runtime_project_attachment_service.GetRuntimeProjectAttachmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> runtime_project_attachment_service.RuntimeProjectAttachment:
            r"""Call the get runtime project
            attachment method over HTTP.

                Args:
                    request (~.runtime_project_attachment_service.GetRuntimeProjectAttachmentRequest):
                        The request object. The
                    [GetRuntimeProjectAttachment][google.cloud.apihub.v1.RuntimeProjectAttachmentService.GetRuntimeProjectAttachment]
                    method's request.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.runtime_project_attachment_service.RuntimeProjectAttachment:
                        Runtime project attachment represents
                    an attachment from the runtime project
                    to the host project. Api Hub looks for
                    deployments in the attached runtime
                    projects and creates corresponding
                    resources in Api Hub for the discovered
                    deployments.

            """

            http_options = _BaseRuntimeProjectAttachmentServiceRestTransport._BaseGetRuntimeProjectAttachment._get_http_options()
            request, metadata = self._interceptor.pre_get_runtime_project_attachment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRuntimeProjectAttachmentServiceRestTransport._BaseGetRuntimeProjectAttachment,
                    "_BaseGetRuntimeProjectAttachment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.RuntimeProjectAttachmentServiceClient.GetRuntimeProjectAttachment",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.RuntimeProjectAttachmentService",
                        "rpcName": "GetRuntimeProjectAttachment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RuntimeProjectAttachmentServiceRestTransport._GetRuntimeProjectAttachment._get_response(
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
            resp = runtime_project_attachment_service.RuntimeProjectAttachment()
            pb_resp = runtime_project_attachment_service.RuntimeProjectAttachment.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_runtime_project_attachment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_runtime_project_attachment_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = runtime_project_attachment_service.RuntimeProjectAttachment.to_json(
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
                    "Received response for google.cloud.apihub_v1.RuntimeProjectAttachmentServiceClient.get_runtime_project_attachment",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.RuntimeProjectAttachmentService",
                        "rpcName": "GetRuntimeProjectAttachment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListRuntimeProjectAttachments(
        _BaseRuntimeProjectAttachmentServiceRestTransport._BaseListRuntimeProjectAttachments,
        RuntimeProjectAttachmentServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "RuntimeProjectAttachmentServiceRestTransport.ListRuntimeProjectAttachments"
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
            request: runtime_project_attachment_service.ListRuntimeProjectAttachmentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> runtime_project_attachment_service.ListRuntimeProjectAttachmentsResponse:
            r"""Call the list runtime project
            attachments method over HTTP.

                Args:
                    request (~.runtime_project_attachment_service.ListRuntimeProjectAttachmentsRequest):
                        The request object. The
                    [ListRuntimeProjectAttachments][google.cloud.apihub.v1.RuntimeProjectAttachmentService.ListRuntimeProjectAttachments]
                    method's request.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.runtime_project_attachment_service.ListRuntimeProjectAttachmentsResponse:
                        The
                    [ListRuntimeProjectAttachments][google.cloud.apihub.v1.RuntimeProjectAttachmentService.ListRuntimeProjectAttachments]
                    method's response.

            """

            http_options = _BaseRuntimeProjectAttachmentServiceRestTransport._BaseListRuntimeProjectAttachments._get_http_options()
            request, metadata = self._interceptor.pre_list_runtime_project_attachments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRuntimeProjectAttachmentServiceRestTransport._BaseListRuntimeProjectAttachments,
                    "_BaseListRuntimeProjectAttachments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.RuntimeProjectAttachmentServiceClient.ListRuntimeProjectAttachments",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.RuntimeProjectAttachmentService",
                        "rpcName": "ListRuntimeProjectAttachments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RuntimeProjectAttachmentServiceRestTransport._ListRuntimeProjectAttachments._get_response(
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
            resp = runtime_project_attachment_service.ListRuntimeProjectAttachmentsResponse()
            pb_resp = runtime_project_attachment_service.ListRuntimeProjectAttachmentsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_runtime_project_attachments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_runtime_project_attachments_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = runtime_project_attachment_service.ListRuntimeProjectAttachmentsResponse.to_json(
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
                    "Received response for google.cloud.apihub_v1.RuntimeProjectAttachmentServiceClient.list_runtime_project_attachments",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.RuntimeProjectAttachmentService",
                        "rpcName": "ListRuntimeProjectAttachments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _LookupRuntimeProjectAttachment(
        _BaseRuntimeProjectAttachmentServiceRestTransport._BaseLookupRuntimeProjectAttachment,
        RuntimeProjectAttachmentServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "RuntimeProjectAttachmentServiceRestTransport.LookupRuntimeProjectAttachment"
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
            request: runtime_project_attachment_service.LookupRuntimeProjectAttachmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> runtime_project_attachment_service.LookupRuntimeProjectAttachmentResponse:
            r"""Call the lookup runtime project
            attachment method over HTTP.

                Args:
                    request (~.runtime_project_attachment_service.LookupRuntimeProjectAttachmentRequest):
                        The request object. The
                    [LookupRuntimeProjectAttachment][google.cloud.apihub.v1.RuntimeProjectAttachmentService.LookupRuntimeProjectAttachment]
                    method's request.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.runtime_project_attachment_service.LookupRuntimeProjectAttachmentResponse:
                        The
                    [ListRuntimeProjectAttachments][google.cloud.apihub.v1.RuntimeProjectAttachmentService.ListRuntimeProjectAttachments]
                    method's response.

            """

            http_options = _BaseRuntimeProjectAttachmentServiceRestTransport._BaseLookupRuntimeProjectAttachment._get_http_options()
            request, metadata = self._interceptor.pre_lookup_runtime_project_attachment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRuntimeProjectAttachmentServiceRestTransport._BaseLookupRuntimeProjectAttachment,
                    "_BaseLookupRuntimeProjectAttachment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.RuntimeProjectAttachmentServiceClient.LookupRuntimeProjectAttachment",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.RuntimeProjectAttachmentService",
                        "rpcName": "LookupRuntimeProjectAttachment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RuntimeProjectAttachmentServiceRestTransport._LookupRuntimeProjectAttachment._get_response(
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
            resp = runtime_project_attachment_service.LookupRuntimeProjectAttachmentResponse()
            pb_resp = runtime_project_attachment_service.LookupRuntimeProjectAttachmentResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_lookup_runtime_project_attachment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_lookup_runtime_project_attachment_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = runtime_project_attachment_service.LookupRuntimeProjectAttachmentResponse.to_json(
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
                    "Received response for google.cloud.apihub_v1.RuntimeProjectAttachmentServiceClient.lookup_runtime_project_attachment",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.RuntimeProjectAttachmentService",
                        "rpcName": "LookupRuntimeProjectAttachment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_runtime_project_attachment(
        self,
    ) -> Callable[
        [runtime_project_attachment_service.CreateRuntimeProjectAttachmentRequest],
        runtime_project_attachment_service.RuntimeProjectAttachment,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateRuntimeProjectAttachment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_runtime_project_attachment(
        self,
    ) -> Callable[
        [runtime_project_attachment_service.DeleteRuntimeProjectAttachmentRequest],
        empty_pb2.Empty,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteRuntimeProjectAttachment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_runtime_project_attachment(
        self,
    ) -> Callable[
        [runtime_project_attachment_service.GetRuntimeProjectAttachmentRequest],
        runtime_project_attachment_service.RuntimeProjectAttachment,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetRuntimeProjectAttachment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_runtime_project_attachments(
        self,
    ) -> Callable[
        [runtime_project_attachment_service.ListRuntimeProjectAttachmentsRequest],
        runtime_project_attachment_service.ListRuntimeProjectAttachmentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListRuntimeProjectAttachments(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def lookup_runtime_project_attachment(
        self,
    ) -> Callable[
        [runtime_project_attachment_service.LookupRuntimeProjectAttachmentRequest],
        runtime_project_attachment_service.LookupRuntimeProjectAttachmentResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._LookupRuntimeProjectAttachment(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseRuntimeProjectAttachmentServiceRestTransport._BaseGetLocation,
        RuntimeProjectAttachmentServiceRestStub,
    ):
        def __hash__(self):
            return hash("RuntimeProjectAttachmentServiceRestTransport.GetLocation")

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
            request: locations_pb2.GetLocationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> locations_pb2.Location:
            r"""Call the get location method over HTTP.

            Args:
                request (locations_pb2.GetLocationRequest):
                    The request object for GetLocation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                locations_pb2.Location: Response from GetLocation method.
            """

            http_options = _BaseRuntimeProjectAttachmentServiceRestTransport._BaseGetLocation._get_http_options()
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRuntimeProjectAttachmentServiceRestTransport._BaseGetLocation,
                    "_BaseGetLocation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.RuntimeProjectAttachmentServiceClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.RuntimeProjectAttachmentService",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                RuntimeProjectAttachmentServiceRestTransport._GetLocation._get_response(
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

            content = response.content.decode("utf-8")
            resp = locations_pb2.Location()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_location(resp)
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
                    "Received response for google.cloud.apihub_v1.RuntimeProjectAttachmentServiceAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.RuntimeProjectAttachmentService",
                        "rpcName": "GetLocation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_locations(self):
        return self._ListLocations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListLocations(
        _BaseRuntimeProjectAttachmentServiceRestTransport._BaseListLocations,
        RuntimeProjectAttachmentServiceRestStub,
    ):
        def __hash__(self):
            return hash("RuntimeProjectAttachmentServiceRestTransport.ListLocations")

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
            request: locations_pb2.ListLocationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> locations_pb2.ListLocationsResponse:
            r"""Call the list locations method over HTTP.

            Args:
                request (locations_pb2.ListLocationsRequest):
                    The request object for ListLocations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                locations_pb2.ListLocationsResponse: Response from ListLocations method.
            """

            http_options = _BaseRuntimeProjectAttachmentServiceRestTransport._BaseListLocations._get_http_options()
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRuntimeProjectAttachmentServiceRestTransport._BaseListLocations,
                    "_BaseListLocations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.RuntimeProjectAttachmentServiceClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.RuntimeProjectAttachmentService",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RuntimeProjectAttachmentServiceRestTransport._ListLocations._get_response(
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
            resp = locations_pb2.ListLocationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_locations(resp)
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
                    "Received response for google.cloud.apihub_v1.RuntimeProjectAttachmentServiceAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.RuntimeProjectAttachmentService",
                        "rpcName": "ListLocations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseRuntimeProjectAttachmentServiceRestTransport._BaseCancelOperation,
        RuntimeProjectAttachmentServiceRestStub,
    ):
        def __hash__(self):
            return hash("RuntimeProjectAttachmentServiceRestTransport.CancelOperation")

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

            http_options = _BaseRuntimeProjectAttachmentServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRuntimeProjectAttachmentServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.apihub_v1.RuntimeProjectAttachmentServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.RuntimeProjectAttachmentService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RuntimeProjectAttachmentServiceRestTransport._CancelOperation._get_response(
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
    def delete_operation(self):
        return self._DeleteOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _DeleteOperation(
        _BaseRuntimeProjectAttachmentServiceRestTransport._BaseDeleteOperation,
        RuntimeProjectAttachmentServiceRestStub,
    ):
        def __hash__(self):
            return hash("RuntimeProjectAttachmentServiceRestTransport.DeleteOperation")

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
            request: operations_pb2.DeleteOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> None:
            r"""Call the delete operation method over HTTP.

            Args:
                request (operations_pb2.DeleteOperationRequest):
                    The request object for DeleteOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseRuntimeProjectAttachmentServiceRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRuntimeProjectAttachmentServiceRestTransport._BaseDeleteOperation,
                    "_BaseDeleteOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.apihub_v1.RuntimeProjectAttachmentServiceClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.RuntimeProjectAttachmentService",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RuntimeProjectAttachmentServiceRestTransport._DeleteOperation._get_response(
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

            return self._interceptor.post_delete_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseRuntimeProjectAttachmentServiceRestTransport._BaseGetOperation,
        RuntimeProjectAttachmentServiceRestStub,
    ):
        def __hash__(self):
            return hash("RuntimeProjectAttachmentServiceRestTransport.GetOperation")

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

            http_options = _BaseRuntimeProjectAttachmentServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRuntimeProjectAttachmentServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.apihub_v1.RuntimeProjectAttachmentServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.RuntimeProjectAttachmentService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RuntimeProjectAttachmentServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.apihub_v1.RuntimeProjectAttachmentServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.RuntimeProjectAttachmentService",
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
        _BaseRuntimeProjectAttachmentServiceRestTransport._BaseListOperations,
        RuntimeProjectAttachmentServiceRestStub,
    ):
        def __hash__(self):
            return hash("RuntimeProjectAttachmentServiceRestTransport.ListOperations")

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

            http_options = _BaseRuntimeProjectAttachmentServiceRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseRuntimeProjectAttachmentServiceRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.apihub_v1.RuntimeProjectAttachmentServiceClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.RuntimeProjectAttachmentService",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = RuntimeProjectAttachmentServiceRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.apihub_v1.RuntimeProjectAttachmentServiceAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.apihub.v1.RuntimeProjectAttachmentService",
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


__all__ = ("RuntimeProjectAttachmentServiceRestTransport",)
