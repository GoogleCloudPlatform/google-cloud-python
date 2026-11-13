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
from google.ads.admanager_v1.types import slate_messages, slate_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseSlateServiceRestTransport

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


class SlateServiceRestInterceptor:
    """Interceptor for SlateService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the SlateServiceRestTransport.

    .. code-block:: python
        class MyCustomSlateServiceInterceptor(SlateServiceRestInterceptor):
            def pre_batch_archive_slates(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_archive_slates(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_create_slates(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_slates(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_unarchive_slates(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_unarchive_slates(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_update_slates(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_slates(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_slate(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_slate(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_slate(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_slate(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_slates(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_slates(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_slate(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_slate(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = SlateServiceRestTransport(interceptor=MyCustomSlateServiceInterceptor())
        client = SlateServiceClient(transport=transport)


    """

    def pre_batch_archive_slates(
        self,
        request: slate_service.BatchArchiveSlatesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        slate_service.BatchArchiveSlatesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for batch_archive_slates

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SlateService server.
        """
        return request, metadata

    def post_batch_archive_slates(
        self, response: slate_service.BatchArchiveSlatesResponse
    ) -> slate_service.BatchArchiveSlatesResponse:
        """Post-rpc interceptor for batch_archive_slates

        DEPRECATED. Please use the `post_batch_archive_slates_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SlateService server but before
        it is returned to user code. This `post_batch_archive_slates` interceptor runs
        before the `post_batch_archive_slates_with_metadata` interceptor.
        """
        return response

    def post_batch_archive_slates_with_metadata(
        self,
        response: slate_service.BatchArchiveSlatesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        slate_service.BatchArchiveSlatesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_archive_slates

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SlateService server but before it is returned to user code.

        We recommend only using this `post_batch_archive_slates_with_metadata`
        interceptor in new development instead of the `post_batch_archive_slates` interceptor.
        When both interceptors are used, this `post_batch_archive_slates_with_metadata` interceptor runs after the
        `post_batch_archive_slates` interceptor. The (possibly modified) response returned by
        `post_batch_archive_slates` will be passed to
        `post_batch_archive_slates_with_metadata`.
        """
        return response, metadata

    def pre_batch_create_slates(
        self,
        request: slate_service.BatchCreateSlatesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        slate_service.BatchCreateSlatesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for batch_create_slates

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SlateService server.
        """
        return request, metadata

    def post_batch_create_slates(
        self, response: slate_service.BatchCreateSlatesResponse
    ) -> slate_service.BatchCreateSlatesResponse:
        """Post-rpc interceptor for batch_create_slates

        DEPRECATED. Please use the `post_batch_create_slates_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SlateService server but before
        it is returned to user code. This `post_batch_create_slates` interceptor runs
        before the `post_batch_create_slates_with_metadata` interceptor.
        """
        return response

    def post_batch_create_slates_with_metadata(
        self,
        response: slate_service.BatchCreateSlatesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        slate_service.BatchCreateSlatesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for batch_create_slates

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SlateService server but before it is returned to user code.

        We recommend only using this `post_batch_create_slates_with_metadata`
        interceptor in new development instead of the `post_batch_create_slates` interceptor.
        When both interceptors are used, this `post_batch_create_slates_with_metadata` interceptor runs after the
        `post_batch_create_slates` interceptor. The (possibly modified) response returned by
        `post_batch_create_slates` will be passed to
        `post_batch_create_slates_with_metadata`.
        """
        return response, metadata

    def pre_batch_unarchive_slates(
        self,
        request: slate_service.BatchUnarchiveSlatesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        slate_service.BatchUnarchiveSlatesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_unarchive_slates

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SlateService server.
        """
        return request, metadata

    def post_batch_unarchive_slates(
        self, response: slate_service.BatchUnarchiveSlatesResponse
    ) -> slate_service.BatchUnarchiveSlatesResponse:
        """Post-rpc interceptor for batch_unarchive_slates

        DEPRECATED. Please use the `post_batch_unarchive_slates_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SlateService server but before
        it is returned to user code. This `post_batch_unarchive_slates` interceptor runs
        before the `post_batch_unarchive_slates_with_metadata` interceptor.
        """
        return response

    def post_batch_unarchive_slates_with_metadata(
        self,
        response: slate_service.BatchUnarchiveSlatesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        slate_service.BatchUnarchiveSlatesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_unarchive_slates

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SlateService server but before it is returned to user code.

        We recommend only using this `post_batch_unarchive_slates_with_metadata`
        interceptor in new development instead of the `post_batch_unarchive_slates` interceptor.
        When both interceptors are used, this `post_batch_unarchive_slates_with_metadata` interceptor runs after the
        `post_batch_unarchive_slates` interceptor. The (possibly modified) response returned by
        `post_batch_unarchive_slates` will be passed to
        `post_batch_unarchive_slates_with_metadata`.
        """
        return response, metadata

    def pre_batch_update_slates(
        self,
        request: slate_service.BatchUpdateSlatesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        slate_service.BatchUpdateSlatesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for batch_update_slates

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SlateService server.
        """
        return request, metadata

    def post_batch_update_slates(
        self, response: slate_service.BatchUpdateSlatesResponse
    ) -> slate_service.BatchUpdateSlatesResponse:
        """Post-rpc interceptor for batch_update_slates

        DEPRECATED. Please use the `post_batch_update_slates_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SlateService server but before
        it is returned to user code. This `post_batch_update_slates` interceptor runs
        before the `post_batch_update_slates_with_metadata` interceptor.
        """
        return response

    def post_batch_update_slates_with_metadata(
        self,
        response: slate_service.BatchUpdateSlatesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        slate_service.BatchUpdateSlatesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for batch_update_slates

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SlateService server but before it is returned to user code.

        We recommend only using this `post_batch_update_slates_with_metadata`
        interceptor in new development instead of the `post_batch_update_slates` interceptor.
        When both interceptors are used, this `post_batch_update_slates_with_metadata` interceptor runs after the
        `post_batch_update_slates` interceptor. The (possibly modified) response returned by
        `post_batch_update_slates` will be passed to
        `post_batch_update_slates_with_metadata`.
        """
        return response, metadata

    def pre_create_slate(
        self,
        request: slate_service.CreateSlateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        slate_service.CreateSlateRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_slate

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SlateService server.
        """
        return request, metadata

    def post_create_slate(self, response: slate_messages.Slate) -> slate_messages.Slate:
        """Post-rpc interceptor for create_slate

        DEPRECATED. Please use the `post_create_slate_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SlateService server but before
        it is returned to user code. This `post_create_slate` interceptor runs
        before the `post_create_slate_with_metadata` interceptor.
        """
        return response

    def post_create_slate_with_metadata(
        self,
        response: slate_messages.Slate,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[slate_messages.Slate, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_slate

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SlateService server but before it is returned to user code.

        We recommend only using this `post_create_slate_with_metadata`
        interceptor in new development instead of the `post_create_slate` interceptor.
        When both interceptors are used, this `post_create_slate_with_metadata` interceptor runs after the
        `post_create_slate` interceptor. The (possibly modified) response returned by
        `post_create_slate` will be passed to
        `post_create_slate_with_metadata`.
        """
        return response, metadata

    def pre_get_slate(
        self,
        request: slate_service.GetSlateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[slate_service.GetSlateRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_slate

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SlateService server.
        """
        return request, metadata

    def post_get_slate(self, response: slate_messages.Slate) -> slate_messages.Slate:
        """Post-rpc interceptor for get_slate

        DEPRECATED. Please use the `post_get_slate_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SlateService server but before
        it is returned to user code. This `post_get_slate` interceptor runs
        before the `post_get_slate_with_metadata` interceptor.
        """
        return response

    def post_get_slate_with_metadata(
        self,
        response: slate_messages.Slate,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[slate_messages.Slate, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_slate

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SlateService server but before it is returned to user code.

        We recommend only using this `post_get_slate_with_metadata`
        interceptor in new development instead of the `post_get_slate` interceptor.
        When both interceptors are used, this `post_get_slate_with_metadata` interceptor runs after the
        `post_get_slate` interceptor. The (possibly modified) response returned by
        `post_get_slate` will be passed to
        `post_get_slate_with_metadata`.
        """
        return response, metadata

    def pre_list_slates(
        self,
        request: slate_service.ListSlatesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        slate_service.ListSlatesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_slates

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SlateService server.
        """
        return request, metadata

    def post_list_slates(
        self, response: slate_service.ListSlatesResponse
    ) -> slate_service.ListSlatesResponse:
        """Post-rpc interceptor for list_slates

        DEPRECATED. Please use the `post_list_slates_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SlateService server but before
        it is returned to user code. This `post_list_slates` interceptor runs
        before the `post_list_slates_with_metadata` interceptor.
        """
        return response

    def post_list_slates_with_metadata(
        self,
        response: slate_service.ListSlatesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        slate_service.ListSlatesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_slates

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SlateService server but before it is returned to user code.

        We recommend only using this `post_list_slates_with_metadata`
        interceptor in new development instead of the `post_list_slates` interceptor.
        When both interceptors are used, this `post_list_slates_with_metadata` interceptor runs after the
        `post_list_slates` interceptor. The (possibly modified) response returned by
        `post_list_slates` will be passed to
        `post_list_slates_with_metadata`.
        """
        return response, metadata

    def pre_update_slate(
        self,
        request: slate_service.UpdateSlateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        slate_service.UpdateSlateRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_slate

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SlateService server.
        """
        return request, metadata

    def post_update_slate(self, response: slate_messages.Slate) -> slate_messages.Slate:
        """Post-rpc interceptor for update_slate

        DEPRECATED. Please use the `post_update_slate_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SlateService server but before
        it is returned to user code. This `post_update_slate` interceptor runs
        before the `post_update_slate_with_metadata` interceptor.
        """
        return response

    def post_update_slate_with_metadata(
        self,
        response: slate_messages.Slate,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[slate_messages.Slate, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_slate

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SlateService server but before it is returned to user code.

        We recommend only using this `post_update_slate_with_metadata`
        interceptor in new development instead of the `post_update_slate` interceptor.
        When both interceptors are used, this `post_update_slate_with_metadata` interceptor runs after the
        `post_update_slate` interceptor. The (possibly modified) response returned by
        `post_update_slate` will be passed to
        `post_update_slate_with_metadata`.
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
        before they are sent to the SlateService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the SlateService server but before
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
        before they are sent to the SlateService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the SlateService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class SlateServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: SlateServiceRestInterceptor


class SlateServiceRestTransport(_BaseSlateServiceRestTransport):
    """REST backend synchronous transport for SlateService.

    Provides methods for handling ``Slate`` objects.

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
        interceptor: Optional[SlateServiceRestInterceptor] = None,
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
            interceptor (Optional[SlateServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or SlateServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchArchiveSlates(
        _BaseSlateServiceRestTransport._BaseBatchArchiveSlates, SlateServiceRestStub
    ):
        def __hash__(self):
            return hash("SlateServiceRestTransport.BatchArchiveSlates")

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
            request: slate_service.BatchArchiveSlatesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> slate_service.BatchArchiveSlatesResponse:
            r"""Call the batch archive slates method over HTTP.

            Args:
                request (~.slate_service.BatchArchiveSlatesRequest):
                    The request object. Request message for ``BatchArchiveSlates`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.slate_service.BatchArchiveSlatesResponse:
                    Response message for ``BatchArchiveSlates`` method.
            """

            http_options = _BaseSlateServiceRestTransport._BaseBatchArchiveSlates._get_http_options()
            request, metadata = self._interceptor.pre_batch_archive_slates(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSlateServiceRestTransport._BaseBatchArchiveSlates,
                    "_BaseBatchArchiveSlates__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.SlateServiceClient.BatchArchiveSlates",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SlateService",
                        "rpcName": "BatchArchiveSlates",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SlateServiceRestTransport._BatchArchiveSlates._get_response(
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
            resp = slate_service.BatchArchiveSlatesResponse()
            pb_resp = slate_service.BatchArchiveSlatesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_archive_slates(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_archive_slates_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = slate_service.BatchArchiveSlatesResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.SlateServiceClient.batch_archive_slates",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SlateService",
                        "rpcName": "BatchArchiveSlates",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchCreateSlates(
        _BaseSlateServiceRestTransport._BaseBatchCreateSlates, SlateServiceRestStub
    ):
        def __hash__(self):
            return hash("SlateServiceRestTransport.BatchCreateSlates")

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
            request: slate_service.BatchCreateSlatesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> slate_service.BatchCreateSlatesResponse:
            r"""Call the batch create slates method over HTTP.

            Args:
                request (~.slate_service.BatchCreateSlatesRequest):
                    The request object. Request object for ``BatchCreateSlates`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.slate_service.BatchCreateSlatesResponse:
                    Response object for ``BatchCreateSlates`` method.
            """

            http_options = _BaseSlateServiceRestTransport._BaseBatchCreateSlates._get_http_options()
            request, metadata = self._interceptor.pre_batch_create_slates(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSlateServiceRestTransport._BaseBatchCreateSlates,
                    "_BaseBatchCreateSlates__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.SlateServiceClient.BatchCreateSlates",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SlateService",
                        "rpcName": "BatchCreateSlates",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SlateServiceRestTransport._BatchCreateSlates._get_response(
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
            resp = slate_service.BatchCreateSlatesResponse()
            pb_resp = slate_service.BatchCreateSlatesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_slates(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_create_slates_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = slate_service.BatchCreateSlatesResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.SlateServiceClient.batch_create_slates",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SlateService",
                        "rpcName": "BatchCreateSlates",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchUnarchiveSlates(
        _BaseSlateServiceRestTransport._BaseBatchUnarchiveSlates, SlateServiceRestStub
    ):
        def __hash__(self):
            return hash("SlateServiceRestTransport.BatchUnarchiveSlates")

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
            request: slate_service.BatchUnarchiveSlatesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> slate_service.BatchUnarchiveSlatesResponse:
            r"""Call the batch unarchive slates method over HTTP.

            Args:
                request (~.slate_service.BatchUnarchiveSlatesRequest):
                    The request object. Request message for ``BatchUnarchiveSlates`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.slate_service.BatchUnarchiveSlatesResponse:
                    Response message for ``BatchUnarchiveSlates`` method.
            """

            http_options = _BaseSlateServiceRestTransport._BaseBatchUnarchiveSlates._get_http_options()
            request, metadata = self._interceptor.pre_batch_unarchive_slates(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSlateServiceRestTransport._BaseBatchUnarchiveSlates,
                    "_BaseBatchUnarchiveSlates__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.SlateServiceClient.BatchUnarchiveSlates",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SlateService",
                        "rpcName": "BatchUnarchiveSlates",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SlateServiceRestTransport._BatchUnarchiveSlates._get_response(
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
            resp = slate_service.BatchUnarchiveSlatesResponse()
            pb_resp = slate_service.BatchUnarchiveSlatesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_unarchive_slates(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_unarchive_slates_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        slate_service.BatchUnarchiveSlatesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.SlateServiceClient.batch_unarchive_slates",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SlateService",
                        "rpcName": "BatchUnarchiveSlates",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchUpdateSlates(
        _BaseSlateServiceRestTransport._BaseBatchUpdateSlates, SlateServiceRestStub
    ):
        def __hash__(self):
            return hash("SlateServiceRestTransport.BatchUpdateSlates")

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
            request: slate_service.BatchUpdateSlatesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> slate_service.BatchUpdateSlatesResponse:
            r"""Call the batch update slates method over HTTP.

            Args:
                request (~.slate_service.BatchUpdateSlatesRequest):
                    The request object. Request object for ``BatchUpdateSlates`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.slate_service.BatchUpdateSlatesResponse:
                    Response object for ``BatchUpdateSlates`` method.
            """

            http_options = _BaseSlateServiceRestTransport._BaseBatchUpdateSlates._get_http_options()
            request, metadata = self._interceptor.pre_batch_update_slates(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSlateServiceRestTransport._BaseBatchUpdateSlates,
                    "_BaseBatchUpdateSlates__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.SlateServiceClient.BatchUpdateSlates",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SlateService",
                        "rpcName": "BatchUpdateSlates",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SlateServiceRestTransport._BatchUpdateSlates._get_response(
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
            resp = slate_service.BatchUpdateSlatesResponse()
            pb_resp = slate_service.BatchUpdateSlatesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_slates(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_update_slates_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = slate_service.BatchUpdateSlatesResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.SlateServiceClient.batch_update_slates",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SlateService",
                        "rpcName": "BatchUpdateSlates",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateSlate(
        _BaseSlateServiceRestTransport._BaseCreateSlate, SlateServiceRestStub
    ):
        def __hash__(self):
            return hash("SlateServiceRestTransport.CreateSlate")

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
            request: slate_service.CreateSlateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> slate_messages.Slate:
            r"""Call the create slate method over HTTP.

            Args:
                request (~.slate_service.CreateSlateRequest):
                    The request object. Request object for ``CreateSlate`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.slate_messages.Slate:
                    A Slate encapsulates all the
                information necessary to represent a
                Slate entity, the video creative used by
                Dynamic Ad Insertion to fill vacant ad
                slots.

            """

            http_options = (
                _BaseSlateServiceRestTransport._BaseCreateSlate._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_slate(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSlateServiceRestTransport._BaseCreateSlate,
                    "_BaseCreateSlate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.SlateServiceClient.CreateSlate",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SlateService",
                        "rpcName": "CreateSlate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SlateServiceRestTransport._CreateSlate._get_response(
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
            resp = slate_messages.Slate()
            pb_resp = slate_messages.Slate.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_slate(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_slate_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = slate_messages.Slate.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.SlateServiceClient.create_slate",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SlateService",
                        "rpcName": "CreateSlate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSlate(_BaseSlateServiceRestTransport._BaseGetSlate, SlateServiceRestStub):
        def __hash__(self):
            return hash("SlateServiceRestTransport.GetSlate")

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
            request: slate_service.GetSlateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> slate_messages.Slate:
            r"""Call the get slate method over HTTP.

            Args:
                request (~.slate_service.GetSlateRequest):
                    The request object. Request message for ``GetSlate`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.slate_messages.Slate:
                    A Slate encapsulates all the
                information necessary to represent a
                Slate entity, the video creative used by
                Dynamic Ad Insertion to fill vacant ad
                slots.

            """

            http_options = (
                _BaseSlateServiceRestTransport._BaseGetSlate._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_slate(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSlateServiceRestTransport._BaseGetSlate,
                    "_BaseGetSlate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.SlateServiceClient.GetSlate",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SlateService",
                        "rpcName": "GetSlate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SlateServiceRestTransport._GetSlate._get_response(
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
            resp = slate_messages.Slate()
            pb_resp = slate_messages.Slate.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_slate(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_slate_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = slate_messages.Slate.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.SlateServiceClient.get_slate",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SlateService",
                        "rpcName": "GetSlate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSlates(
        _BaseSlateServiceRestTransport._BaseListSlates, SlateServiceRestStub
    ):
        def __hash__(self):
            return hash("SlateServiceRestTransport.ListSlates")

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
            request: slate_service.ListSlatesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> slate_service.ListSlatesResponse:
            r"""Call the list slates method over HTTP.

            Args:
                request (~.slate_service.ListSlatesRequest):
                    The request object. Request message for ``ListSlates`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.slate_service.ListSlatesResponse:
                    Response message for ``ListSlates`` method.
            """

            http_options = (
                _BaseSlateServiceRestTransport._BaseListSlates._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_slates(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSlateServiceRestTransport._BaseListSlates,
                    "_BaseListSlates__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.SlateServiceClient.ListSlates",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SlateService",
                        "rpcName": "ListSlates",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SlateServiceRestTransport._ListSlates._get_response(
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
            resp = slate_service.ListSlatesResponse()
            pb_resp = slate_service.ListSlatesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_slates(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_slates_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = slate_service.ListSlatesResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.SlateServiceClient.list_slates",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SlateService",
                        "rpcName": "ListSlates",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateSlate(
        _BaseSlateServiceRestTransport._BaseUpdateSlate, SlateServiceRestStub
    ):
        def __hash__(self):
            return hash("SlateServiceRestTransport.UpdateSlate")

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
            request: slate_service.UpdateSlateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> slate_messages.Slate:
            r"""Call the update slate method over HTTP.

            Args:
                request (~.slate_service.UpdateSlateRequest):
                    The request object. Request object for ``UpdateSlate`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.slate_messages.Slate:
                    A Slate encapsulates all the
                information necessary to represent a
                Slate entity, the video creative used by
                Dynamic Ad Insertion to fill vacant ad
                slots.

            """

            http_options = (
                _BaseSlateServiceRestTransport._BaseUpdateSlate._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_slate(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSlateServiceRestTransport._BaseUpdateSlate,
                    "_BaseUpdateSlate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.SlateServiceClient.UpdateSlate",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SlateService",
                        "rpcName": "UpdateSlate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SlateServiceRestTransport._UpdateSlate._get_response(
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
            resp = slate_messages.Slate()
            pb_resp = slate_messages.Slate.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_slate(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_slate_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = slate_messages.Slate.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.SlateServiceClient.update_slate",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SlateService",
                        "rpcName": "UpdateSlate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_archive_slates(
        self,
    ) -> Callable[
        [slate_service.BatchArchiveSlatesRequest],
        slate_service.BatchArchiveSlatesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchArchiveSlates(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_create_slates(
        self,
    ) -> Callable[
        [slate_service.BatchCreateSlatesRequest],
        slate_service.BatchCreateSlatesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateSlates(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_unarchive_slates(
        self,
    ) -> Callable[
        [slate_service.BatchUnarchiveSlatesRequest],
        slate_service.BatchUnarchiveSlatesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUnarchiveSlates(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_update_slates(
        self,
    ) -> Callable[
        [slate_service.BatchUpdateSlatesRequest],
        slate_service.BatchUpdateSlatesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdateSlates(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_slate(
        self,
    ) -> Callable[[slate_service.CreateSlateRequest], slate_messages.Slate]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateSlate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_slate(
        self,
    ) -> Callable[[slate_service.GetSlateRequest], slate_messages.Slate]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSlate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_slates(
        self,
    ) -> Callable[[slate_service.ListSlatesRequest], slate_service.ListSlatesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSlates(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_slate(
        self,
    ) -> Callable[[slate_service.UpdateSlateRequest], slate_messages.Slate]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateSlate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseSlateServiceRestTransport._BaseCancelOperation, SlateServiceRestStub
    ):
        def __hash__(self):
            return hash("SlateServiceRestTransport.CancelOperation")

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
                _BaseSlateServiceRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSlateServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.ads.admanager_v1.SlateServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SlateService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SlateServiceRestTransport._CancelOperation._get_response(
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
        _BaseSlateServiceRestTransport._BaseGetOperation, SlateServiceRestStub
    ):
        def __hash__(self):
            return hash("SlateServiceRestTransport.GetOperation")

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
                _BaseSlateServiceRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSlateServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.ads.admanager_v1.SlateServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SlateService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SlateServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.ads.admanager_v1.SlateServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SlateService",
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


__all__ = ("SlateServiceRestTransport",)
