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
from google.ads.admanager_v1.types import application_messages, application_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseApplicationServiceRestTransport

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


class ApplicationServiceRestInterceptor:
    """Interceptor for ApplicationService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ApplicationServiceRestTransport.

    .. code-block:: python
        class MyCustomApplicationServiceInterceptor(ApplicationServiceRestInterceptor):
            def pre_batch_archive_applications(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_archive_applications(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_create_applications(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_applications(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_unarchive_applications(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_unarchive_applications(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_update_applications(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_applications(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_application(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_application(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_application(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_application(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_applications(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_applications(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_application(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_application(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ApplicationServiceRestTransport(interceptor=MyCustomApplicationServiceInterceptor())
        client = ApplicationServiceClient(transport=transport)


    """

    def pre_batch_archive_applications(
        self,
        request: application_service.BatchArchiveApplicationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        application_service.BatchArchiveApplicationsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_archive_applications

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApplicationService server.
        """
        return request, metadata

    def post_batch_archive_applications(
        self, response: application_service.BatchArchiveApplicationsResponse
    ) -> application_service.BatchArchiveApplicationsResponse:
        """Post-rpc interceptor for batch_archive_applications

        DEPRECATED. Please use the `post_batch_archive_applications_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApplicationService server but before
        it is returned to user code. This `post_batch_archive_applications` interceptor runs
        before the `post_batch_archive_applications_with_metadata` interceptor.
        """
        return response

    def post_batch_archive_applications_with_metadata(
        self,
        response: application_service.BatchArchiveApplicationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        application_service.BatchArchiveApplicationsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_archive_applications

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApplicationService server but before it is returned to user code.

        We recommend only using this `post_batch_archive_applications_with_metadata`
        interceptor in new development instead of the `post_batch_archive_applications` interceptor.
        When both interceptors are used, this `post_batch_archive_applications_with_metadata` interceptor runs after the
        `post_batch_archive_applications` interceptor. The (possibly modified) response returned by
        `post_batch_archive_applications` will be passed to
        `post_batch_archive_applications_with_metadata`.
        """
        return response, metadata

    def pre_batch_create_applications(
        self,
        request: application_service.BatchCreateApplicationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        application_service.BatchCreateApplicationsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_create_applications

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApplicationService server.
        """
        return request, metadata

    def post_batch_create_applications(
        self, response: application_service.BatchCreateApplicationsResponse
    ) -> application_service.BatchCreateApplicationsResponse:
        """Post-rpc interceptor for batch_create_applications

        DEPRECATED. Please use the `post_batch_create_applications_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApplicationService server but before
        it is returned to user code. This `post_batch_create_applications` interceptor runs
        before the `post_batch_create_applications_with_metadata` interceptor.
        """
        return response

    def post_batch_create_applications_with_metadata(
        self,
        response: application_service.BatchCreateApplicationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        application_service.BatchCreateApplicationsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_create_applications

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApplicationService server but before it is returned to user code.

        We recommend only using this `post_batch_create_applications_with_metadata`
        interceptor in new development instead of the `post_batch_create_applications` interceptor.
        When both interceptors are used, this `post_batch_create_applications_with_metadata` interceptor runs after the
        `post_batch_create_applications` interceptor. The (possibly modified) response returned by
        `post_batch_create_applications` will be passed to
        `post_batch_create_applications_with_metadata`.
        """
        return response, metadata

    def pre_batch_unarchive_applications(
        self,
        request: application_service.BatchUnarchiveApplicationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        application_service.BatchUnarchiveApplicationsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_unarchive_applications

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApplicationService server.
        """
        return request, metadata

    def post_batch_unarchive_applications(
        self, response: application_service.BatchUnarchiveApplicationsResponse
    ) -> application_service.BatchUnarchiveApplicationsResponse:
        """Post-rpc interceptor for batch_unarchive_applications

        DEPRECATED. Please use the `post_batch_unarchive_applications_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApplicationService server but before
        it is returned to user code. This `post_batch_unarchive_applications` interceptor runs
        before the `post_batch_unarchive_applications_with_metadata` interceptor.
        """
        return response

    def post_batch_unarchive_applications_with_metadata(
        self,
        response: application_service.BatchUnarchiveApplicationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        application_service.BatchUnarchiveApplicationsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_unarchive_applications

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApplicationService server but before it is returned to user code.

        We recommend only using this `post_batch_unarchive_applications_with_metadata`
        interceptor in new development instead of the `post_batch_unarchive_applications` interceptor.
        When both interceptors are used, this `post_batch_unarchive_applications_with_metadata` interceptor runs after the
        `post_batch_unarchive_applications` interceptor. The (possibly modified) response returned by
        `post_batch_unarchive_applications` will be passed to
        `post_batch_unarchive_applications_with_metadata`.
        """
        return response, metadata

    def pre_batch_update_applications(
        self,
        request: application_service.BatchUpdateApplicationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        application_service.BatchUpdateApplicationsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_update_applications

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApplicationService server.
        """
        return request, metadata

    def post_batch_update_applications(
        self, response: application_service.BatchUpdateApplicationsResponse
    ) -> application_service.BatchUpdateApplicationsResponse:
        """Post-rpc interceptor for batch_update_applications

        DEPRECATED. Please use the `post_batch_update_applications_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApplicationService server but before
        it is returned to user code. This `post_batch_update_applications` interceptor runs
        before the `post_batch_update_applications_with_metadata` interceptor.
        """
        return response

    def post_batch_update_applications_with_metadata(
        self,
        response: application_service.BatchUpdateApplicationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        application_service.BatchUpdateApplicationsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_update_applications

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApplicationService server but before it is returned to user code.

        We recommend only using this `post_batch_update_applications_with_metadata`
        interceptor in new development instead of the `post_batch_update_applications` interceptor.
        When both interceptors are used, this `post_batch_update_applications_with_metadata` interceptor runs after the
        `post_batch_update_applications` interceptor. The (possibly modified) response returned by
        `post_batch_update_applications` will be passed to
        `post_batch_update_applications_with_metadata`.
        """
        return response, metadata

    def pre_create_application(
        self,
        request: application_service.CreateApplicationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        application_service.CreateApplicationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_application

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApplicationService server.
        """
        return request, metadata

    def post_create_application(
        self, response: application_messages.Application
    ) -> application_messages.Application:
        """Post-rpc interceptor for create_application

        DEPRECATED. Please use the `post_create_application_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApplicationService server but before
        it is returned to user code. This `post_create_application` interceptor runs
        before the `post_create_application_with_metadata` interceptor.
        """
        return response

    def post_create_application_with_metadata(
        self,
        response: application_messages.Application,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        application_messages.Application, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_application

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApplicationService server but before it is returned to user code.

        We recommend only using this `post_create_application_with_metadata`
        interceptor in new development instead of the `post_create_application` interceptor.
        When both interceptors are used, this `post_create_application_with_metadata` interceptor runs after the
        `post_create_application` interceptor. The (possibly modified) response returned by
        `post_create_application` will be passed to
        `post_create_application_with_metadata`.
        """
        return response, metadata

    def pre_get_application(
        self,
        request: application_service.GetApplicationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        application_service.GetApplicationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_application

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApplicationService server.
        """
        return request, metadata

    def post_get_application(
        self, response: application_messages.Application
    ) -> application_messages.Application:
        """Post-rpc interceptor for get_application

        DEPRECATED. Please use the `post_get_application_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApplicationService server but before
        it is returned to user code. This `post_get_application` interceptor runs
        before the `post_get_application_with_metadata` interceptor.
        """
        return response

    def post_get_application_with_metadata(
        self,
        response: application_messages.Application,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        application_messages.Application, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_application

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApplicationService server but before it is returned to user code.

        We recommend only using this `post_get_application_with_metadata`
        interceptor in new development instead of the `post_get_application` interceptor.
        When both interceptors are used, this `post_get_application_with_metadata` interceptor runs after the
        `post_get_application` interceptor. The (possibly modified) response returned by
        `post_get_application` will be passed to
        `post_get_application_with_metadata`.
        """
        return response, metadata

    def pre_list_applications(
        self,
        request: application_service.ListApplicationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        application_service.ListApplicationsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_applications

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApplicationService server.
        """
        return request, metadata

    def post_list_applications(
        self, response: application_service.ListApplicationsResponse
    ) -> application_service.ListApplicationsResponse:
        """Post-rpc interceptor for list_applications

        DEPRECATED. Please use the `post_list_applications_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApplicationService server but before
        it is returned to user code. This `post_list_applications` interceptor runs
        before the `post_list_applications_with_metadata` interceptor.
        """
        return response

    def post_list_applications_with_metadata(
        self,
        response: application_service.ListApplicationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        application_service.ListApplicationsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_applications

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApplicationService server but before it is returned to user code.

        We recommend only using this `post_list_applications_with_metadata`
        interceptor in new development instead of the `post_list_applications` interceptor.
        When both interceptors are used, this `post_list_applications_with_metadata` interceptor runs after the
        `post_list_applications` interceptor. The (possibly modified) response returned by
        `post_list_applications` will be passed to
        `post_list_applications_with_metadata`.
        """
        return response, metadata

    def pre_update_application(
        self,
        request: application_service.UpdateApplicationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        application_service.UpdateApplicationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_application

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ApplicationService server.
        """
        return request, metadata

    def post_update_application(
        self, response: application_messages.Application
    ) -> application_messages.Application:
        """Post-rpc interceptor for update_application

        DEPRECATED. Please use the `post_update_application_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ApplicationService server but before
        it is returned to user code. This `post_update_application` interceptor runs
        before the `post_update_application_with_metadata` interceptor.
        """
        return response

    def post_update_application_with_metadata(
        self,
        response: application_messages.Application,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        application_messages.Application, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_application

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ApplicationService server but before it is returned to user code.

        We recommend only using this `post_update_application_with_metadata`
        interceptor in new development instead of the `post_update_application` interceptor.
        When both interceptors are used, this `post_update_application_with_metadata` interceptor runs after the
        `post_update_application` interceptor. The (possibly modified) response returned by
        `post_update_application` will be passed to
        `post_update_application_with_metadata`.
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
        before they are sent to the ApplicationService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the ApplicationService server but before
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
        before they are sent to the ApplicationService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the ApplicationService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class ApplicationServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ApplicationServiceRestInterceptor


class ApplicationServiceRestTransport(_BaseApplicationServiceRestTransport):
    """REST backend synchronous transport for ApplicationService.

    Provides methods for handling ``Application`` objects.

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
        interceptor: Optional[ApplicationServiceRestInterceptor] = None,
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
            interceptor (Optional[ApplicationServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or ApplicationServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchArchiveApplications(
        _BaseApplicationServiceRestTransport._BaseBatchArchiveApplications,
        ApplicationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ApplicationServiceRestTransport.BatchArchiveApplications")

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
            request: application_service.BatchArchiveApplicationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> application_service.BatchArchiveApplicationsResponse:
            r"""Call the batch archive
            applications method over HTTP.

                Args:
                    request (~.application_service.BatchArchiveApplicationsRequest):
                        The request object. Request object for ``BatchArchiveApplications`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.application_service.BatchArchiveApplicationsResponse:
                        Response object for ``BatchArchiveApplications`` method.
            """

            http_options = _BaseApplicationServiceRestTransport._BaseBatchArchiveApplications._get_http_options()
            request, metadata = self._interceptor.pre_batch_archive_applications(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApplicationServiceRestTransport._BaseBatchArchiveApplications,
                    "_BaseBatchArchiveApplications__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ApplicationServiceClient.BatchArchiveApplications",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ApplicationService",
                        "rpcName": "BatchArchiveApplications",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ApplicationServiceRestTransport._BatchArchiveApplications._get_response(
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
            resp = application_service.BatchArchiveApplicationsResponse()
            pb_resp = application_service.BatchArchiveApplicationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_archive_applications(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_archive_applications_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        application_service.BatchArchiveApplicationsResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.ApplicationServiceClient.batch_archive_applications",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ApplicationService",
                        "rpcName": "BatchArchiveApplications",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchCreateApplications(
        _BaseApplicationServiceRestTransport._BaseBatchCreateApplications,
        ApplicationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ApplicationServiceRestTransport.BatchCreateApplications")

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
            request: application_service.BatchCreateApplicationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> application_service.BatchCreateApplicationsResponse:
            r"""Call the batch create applications method over HTTP.

            Args:
                request (~.application_service.BatchCreateApplicationsRequest):
                    The request object. Request object for ``BatchCreateApplications`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.application_service.BatchCreateApplicationsResponse:
                    Response object for ``BatchCreateApplications`` method.
            """

            http_options = _BaseApplicationServiceRestTransport._BaseBatchCreateApplications._get_http_options()
            request, metadata = self._interceptor.pre_batch_create_applications(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApplicationServiceRestTransport._BaseBatchCreateApplications,
                    "_BaseBatchCreateApplications__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ApplicationServiceClient.BatchCreateApplications",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ApplicationService",
                        "rpcName": "BatchCreateApplications",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ApplicationServiceRestTransport._BatchCreateApplications._get_response(
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
            resp = application_service.BatchCreateApplicationsResponse()
            pb_resp = application_service.BatchCreateApplicationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_applications(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_create_applications_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        application_service.BatchCreateApplicationsResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.ApplicationServiceClient.batch_create_applications",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ApplicationService",
                        "rpcName": "BatchCreateApplications",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchUnarchiveApplications(
        _BaseApplicationServiceRestTransport._BaseBatchUnarchiveApplications,
        ApplicationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ApplicationServiceRestTransport.BatchUnarchiveApplications")

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
            request: application_service.BatchUnarchiveApplicationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> application_service.BatchUnarchiveApplicationsResponse:
            r"""Call the batch unarchive
            applications method over HTTP.

                Args:
                    request (~.application_service.BatchUnarchiveApplicationsRequest):
                        The request object. Request object for ``BatchUnarchiveApplications``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.application_service.BatchUnarchiveApplicationsResponse:
                        Response object for ``BatchUnarchiveApplications``
                    method.

            """

            http_options = _BaseApplicationServiceRestTransport._BaseBatchUnarchiveApplications._get_http_options()
            request, metadata = self._interceptor.pre_batch_unarchive_applications(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApplicationServiceRestTransport._BaseBatchUnarchiveApplications,
                    "_BaseBatchUnarchiveApplications__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ApplicationServiceClient.BatchUnarchiveApplications",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ApplicationService",
                        "rpcName": "BatchUnarchiveApplications",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApplicationServiceRestTransport._BatchUnarchiveApplications._get_response(
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
            resp = application_service.BatchUnarchiveApplicationsResponse()
            pb_resp = application_service.BatchUnarchiveApplicationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_unarchive_applications(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_unarchive_applications_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        application_service.BatchUnarchiveApplicationsResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.ApplicationServiceClient.batch_unarchive_applications",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ApplicationService",
                        "rpcName": "BatchUnarchiveApplications",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchUpdateApplications(
        _BaseApplicationServiceRestTransport._BaseBatchUpdateApplications,
        ApplicationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ApplicationServiceRestTransport.BatchUpdateApplications")

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
            request: application_service.BatchUpdateApplicationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> application_service.BatchUpdateApplicationsResponse:
            r"""Call the batch update applications method over HTTP.

            Args:
                request (~.application_service.BatchUpdateApplicationsRequest):
                    The request object. Request object for ``BatchUpdateApplications`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.application_service.BatchUpdateApplicationsResponse:
                    Response object for ``BatchUpdateApplications`` method.
            """

            http_options = _BaseApplicationServiceRestTransport._BaseBatchUpdateApplications._get_http_options()
            request, metadata = self._interceptor.pre_batch_update_applications(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApplicationServiceRestTransport._BaseBatchUpdateApplications,
                    "_BaseBatchUpdateApplications__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ApplicationServiceClient.BatchUpdateApplications",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ApplicationService",
                        "rpcName": "BatchUpdateApplications",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ApplicationServiceRestTransport._BatchUpdateApplications._get_response(
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
            resp = application_service.BatchUpdateApplicationsResponse()
            pb_resp = application_service.BatchUpdateApplicationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_applications(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_update_applications_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        application_service.BatchUpdateApplicationsResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.ApplicationServiceClient.batch_update_applications",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ApplicationService",
                        "rpcName": "BatchUpdateApplications",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateApplication(
        _BaseApplicationServiceRestTransport._BaseCreateApplication,
        ApplicationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ApplicationServiceRestTransport.CreateApplication")

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
            request: application_service.CreateApplicationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> application_messages.Application:
            r"""Call the create application method over HTTP.

            Args:
                request (~.application_service.CreateApplicationRequest):
                    The request object. Request object for ``CreateApplication`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.application_messages.Application:
                    An application that has been added to
                or "claimed" by the network to be used
                for targeting purposes. These mobile
                apps can come from various app stores.

            """

            http_options = _BaseApplicationServiceRestTransport._BaseCreateApplication._get_http_options()
            request, metadata = self._interceptor.pre_create_application(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApplicationServiceRestTransport._BaseCreateApplication,
                    "_BaseCreateApplication__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ApplicationServiceClient.CreateApplication",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ApplicationService",
                        "rpcName": "CreateApplication",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApplicationServiceRestTransport._CreateApplication._get_response(
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
            resp = application_messages.Application()
            pb_resp = application_messages.Application.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_application(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_application_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = application_messages.Application.to_json(
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
                    "Received response for google.ads.admanager_v1.ApplicationServiceClient.create_application",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ApplicationService",
                        "rpcName": "CreateApplication",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetApplication(
        _BaseApplicationServiceRestTransport._BaseGetApplication,
        ApplicationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ApplicationServiceRestTransport.GetApplication")

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
            request: application_service.GetApplicationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> application_messages.Application:
            r"""Call the get application method over HTTP.

            Args:
                request (~.application_service.GetApplicationRequest):
                    The request object. Request object for ``GetApplication`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.application_messages.Application:
                    An application that has been added to
                or "claimed" by the network to be used
                for targeting purposes. These mobile
                apps can come from various app stores.

            """

            http_options = _BaseApplicationServiceRestTransport._BaseGetApplication._get_http_options()
            request, metadata = self._interceptor.pre_get_application(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApplicationServiceRestTransport._BaseGetApplication,
                    "_BaseGetApplication__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ApplicationServiceClient.GetApplication",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ApplicationService",
                        "rpcName": "GetApplication",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApplicationServiceRestTransport._GetApplication._get_response(
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
            resp = application_messages.Application()
            pb_resp = application_messages.Application.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_application(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_application_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = application_messages.Application.to_json(
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
                    "Received response for google.ads.admanager_v1.ApplicationServiceClient.get_application",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ApplicationService",
                        "rpcName": "GetApplication",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListApplications(
        _BaseApplicationServiceRestTransport._BaseListApplications,
        ApplicationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ApplicationServiceRestTransport.ListApplications")

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
            request: application_service.ListApplicationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> application_service.ListApplicationsResponse:
            r"""Call the list applications method over HTTP.

            Args:
                request (~.application_service.ListApplicationsRequest):
                    The request object. Request object for ``ListApplications`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.application_service.ListApplicationsResponse:
                    Response object for ``ListApplicationsRequest``
                containing matching ``Application`` objects.

            """

            http_options = _BaseApplicationServiceRestTransport._BaseListApplications._get_http_options()
            request, metadata = self._interceptor.pre_list_applications(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApplicationServiceRestTransport._BaseListApplications,
                    "_BaseListApplications__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ApplicationServiceClient.ListApplications",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ApplicationService",
                        "rpcName": "ListApplications",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApplicationServiceRestTransport._ListApplications._get_response(
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
            resp = application_service.ListApplicationsResponse()
            pb_resp = application_service.ListApplicationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_applications(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_applications_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        application_service.ListApplicationsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.ApplicationServiceClient.list_applications",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ApplicationService",
                        "rpcName": "ListApplications",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateApplication(
        _BaseApplicationServiceRestTransport._BaseUpdateApplication,
        ApplicationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ApplicationServiceRestTransport.UpdateApplication")

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
            request: application_service.UpdateApplicationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> application_messages.Application:
            r"""Call the update application method over HTTP.

            Args:
                request (~.application_service.UpdateApplicationRequest):
                    The request object. Request object for ``UpdateApplication`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.application_messages.Application:
                    An application that has been added to
                or "claimed" by the network to be used
                for targeting purposes. These mobile
                apps can come from various app stores.

            """

            http_options = _BaseApplicationServiceRestTransport._BaseUpdateApplication._get_http_options()
            request, metadata = self._interceptor.pre_update_application(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApplicationServiceRestTransport._BaseUpdateApplication,
                    "_BaseUpdateApplication__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ApplicationServiceClient.UpdateApplication",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ApplicationService",
                        "rpcName": "UpdateApplication",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApplicationServiceRestTransport._UpdateApplication._get_response(
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
            resp = application_messages.Application()
            pb_resp = application_messages.Application.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_application(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_application_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = application_messages.Application.to_json(
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
                    "Received response for google.ads.admanager_v1.ApplicationServiceClient.update_application",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ApplicationService",
                        "rpcName": "UpdateApplication",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_archive_applications(
        self,
    ) -> Callable[
        [application_service.BatchArchiveApplicationsRequest],
        application_service.BatchArchiveApplicationsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchArchiveApplications(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_create_applications(
        self,
    ) -> Callable[
        [application_service.BatchCreateApplicationsRequest],
        application_service.BatchCreateApplicationsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateApplications(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_unarchive_applications(
        self,
    ) -> Callable[
        [application_service.BatchUnarchiveApplicationsRequest],
        application_service.BatchUnarchiveApplicationsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUnarchiveApplications(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_update_applications(
        self,
    ) -> Callable[
        [application_service.BatchUpdateApplicationsRequest],
        application_service.BatchUpdateApplicationsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdateApplications(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_application(
        self,
    ) -> Callable[
        [application_service.CreateApplicationRequest], application_messages.Application
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateApplication(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_application(
        self,
    ) -> Callable[
        [application_service.GetApplicationRequest], application_messages.Application
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetApplication(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_applications(
        self,
    ) -> Callable[
        [application_service.ListApplicationsRequest],
        application_service.ListApplicationsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListApplications(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_application(
        self,
    ) -> Callable[
        [application_service.UpdateApplicationRequest], application_messages.Application
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateApplication(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseApplicationServiceRestTransport._BaseCancelOperation,
        ApplicationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ApplicationServiceRestTransport.CancelOperation")

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

            http_options = _BaseApplicationServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApplicationServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.ads.admanager_v1.ApplicationServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ApplicationService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApplicationServiceRestTransport._CancelOperation._get_response(
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
        _BaseApplicationServiceRestTransport._BaseGetOperation,
        ApplicationServiceRestStub,
    ):
        def __hash__(self):
            return hash("ApplicationServiceRestTransport.GetOperation")

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

            http_options = _BaseApplicationServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseApplicationServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.ads.admanager_v1.ApplicationServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ApplicationService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ApplicationServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.ads.admanager_v1.ApplicationServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ApplicationService",
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


__all__ = ("ApplicationServiceRestTransport",)
