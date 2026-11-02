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
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.retail_v2alpha._compat import transcode_request
from google.cloud.retail_v2alpha.types import project, project_service
from google.cloud.retail_v2alpha.types import project as gcr_project

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseProjectServiceRestTransport

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


class ProjectServiceRestInterceptor:
    """Interceptor for ProjectService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ProjectServiceRestTransport.

    .. code-block:: python
        class MyCustomProjectServiceInterceptor(ProjectServiceRestInterceptor):
            def pre_accept_terms(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_accept_terms(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_enroll_solution(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_enroll_solution(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_alert_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_alert_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_logging_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_logging_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_project(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_project(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_enrolled_solutions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_enrolled_solutions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_alert_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_alert_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_logging_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_logging_config(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ProjectServiceRestTransport(interceptor=MyCustomProjectServiceInterceptor())
        client = ProjectServiceClient(transport=transport)


    """

    def pre_accept_terms(
        self,
        request: project_service.AcceptTermsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        project_service.AcceptTermsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for accept_terms

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProjectService server.
        """
        return request, metadata

    def post_accept_terms(self, response: gcr_project.Project) -> gcr_project.Project:
        """Post-rpc interceptor for accept_terms

        DEPRECATED. Please use the `post_accept_terms_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProjectService server but before
        it is returned to user code. This `post_accept_terms` interceptor runs
        before the `post_accept_terms_with_metadata` interceptor.
        """
        return response

    def post_accept_terms_with_metadata(
        self,
        response: gcr_project.Project,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcr_project.Project, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for accept_terms

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProjectService server but before it is returned to user code.

        We recommend only using this `post_accept_terms_with_metadata`
        interceptor in new development instead of the `post_accept_terms` interceptor.
        When both interceptors are used, this `post_accept_terms_with_metadata` interceptor runs after the
        `post_accept_terms` interceptor. The (possibly modified) response returned by
        `post_accept_terms` will be passed to
        `post_accept_terms_with_metadata`.
        """
        return response, metadata

    def pre_enroll_solution(
        self,
        request: project_service.EnrollSolutionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        project_service.EnrollSolutionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for enroll_solution

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProjectService server.
        """
        return request, metadata

    def post_enroll_solution(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for enroll_solution

        DEPRECATED. Please use the `post_enroll_solution_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProjectService server but before
        it is returned to user code. This `post_enroll_solution` interceptor runs
        before the `post_enroll_solution_with_metadata` interceptor.
        """
        return response

    def post_enroll_solution_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for enroll_solution

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProjectService server but before it is returned to user code.

        We recommend only using this `post_enroll_solution_with_metadata`
        interceptor in new development instead of the `post_enroll_solution` interceptor.
        When both interceptors are used, this `post_enroll_solution_with_metadata` interceptor runs after the
        `post_enroll_solution` interceptor. The (possibly modified) response returned by
        `post_enroll_solution` will be passed to
        `post_enroll_solution_with_metadata`.
        """
        return response, metadata

    def pre_get_alert_config(
        self,
        request: project_service.GetAlertConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        project_service.GetAlertConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_alert_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProjectService server.
        """
        return request, metadata

    def post_get_alert_config(
        self, response: project.AlertConfig
    ) -> project.AlertConfig:
        """Post-rpc interceptor for get_alert_config

        DEPRECATED. Please use the `post_get_alert_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProjectService server but before
        it is returned to user code. This `post_get_alert_config` interceptor runs
        before the `post_get_alert_config_with_metadata` interceptor.
        """
        return response

    def post_get_alert_config_with_metadata(
        self,
        response: project.AlertConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[project.AlertConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_alert_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProjectService server but before it is returned to user code.

        We recommend only using this `post_get_alert_config_with_metadata`
        interceptor in new development instead of the `post_get_alert_config` interceptor.
        When both interceptors are used, this `post_get_alert_config_with_metadata` interceptor runs after the
        `post_get_alert_config` interceptor. The (possibly modified) response returned by
        `post_get_alert_config` will be passed to
        `post_get_alert_config_with_metadata`.
        """
        return response, metadata

    def pre_get_logging_config(
        self,
        request: project_service.GetLoggingConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        project_service.GetLoggingConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_logging_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProjectService server.
        """
        return request, metadata

    def post_get_logging_config(
        self, response: project.LoggingConfig
    ) -> project.LoggingConfig:
        """Post-rpc interceptor for get_logging_config

        DEPRECATED. Please use the `post_get_logging_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProjectService server but before
        it is returned to user code. This `post_get_logging_config` interceptor runs
        before the `post_get_logging_config_with_metadata` interceptor.
        """
        return response

    def post_get_logging_config_with_metadata(
        self,
        response: project.LoggingConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[project.LoggingConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_logging_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProjectService server but before it is returned to user code.

        We recommend only using this `post_get_logging_config_with_metadata`
        interceptor in new development instead of the `post_get_logging_config` interceptor.
        When both interceptors are used, this `post_get_logging_config_with_metadata` interceptor runs after the
        `post_get_logging_config` interceptor. The (possibly modified) response returned by
        `post_get_logging_config` will be passed to
        `post_get_logging_config_with_metadata`.
        """
        return response, metadata

    def pre_get_project(
        self,
        request: project_service.GetProjectRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        project_service.GetProjectRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_project

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProjectService server.
        """
        return request, metadata

    def post_get_project(self, response: project.Project) -> project.Project:
        """Post-rpc interceptor for get_project

        DEPRECATED. Please use the `post_get_project_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProjectService server but before
        it is returned to user code. This `post_get_project` interceptor runs
        before the `post_get_project_with_metadata` interceptor.
        """
        return response

    def post_get_project_with_metadata(
        self,
        response: project.Project,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[project.Project, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_project

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProjectService server but before it is returned to user code.

        We recommend only using this `post_get_project_with_metadata`
        interceptor in new development instead of the `post_get_project` interceptor.
        When both interceptors are used, this `post_get_project_with_metadata` interceptor runs after the
        `post_get_project` interceptor. The (possibly modified) response returned by
        `post_get_project` will be passed to
        `post_get_project_with_metadata`.
        """
        return response, metadata

    def pre_list_enrolled_solutions(
        self,
        request: project_service.ListEnrolledSolutionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        project_service.ListEnrolledSolutionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_enrolled_solutions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProjectService server.
        """
        return request, metadata

    def post_list_enrolled_solutions(
        self, response: project_service.ListEnrolledSolutionsResponse
    ) -> project_service.ListEnrolledSolutionsResponse:
        """Post-rpc interceptor for list_enrolled_solutions

        DEPRECATED. Please use the `post_list_enrolled_solutions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProjectService server but before
        it is returned to user code. This `post_list_enrolled_solutions` interceptor runs
        before the `post_list_enrolled_solutions_with_metadata` interceptor.
        """
        return response

    def post_list_enrolled_solutions_with_metadata(
        self,
        response: project_service.ListEnrolledSolutionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        project_service.ListEnrolledSolutionsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_enrolled_solutions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProjectService server but before it is returned to user code.

        We recommend only using this `post_list_enrolled_solutions_with_metadata`
        interceptor in new development instead of the `post_list_enrolled_solutions` interceptor.
        When both interceptors are used, this `post_list_enrolled_solutions_with_metadata` interceptor runs after the
        `post_list_enrolled_solutions` interceptor. The (possibly modified) response returned by
        `post_list_enrolled_solutions` will be passed to
        `post_list_enrolled_solutions_with_metadata`.
        """
        return response, metadata

    def pre_update_alert_config(
        self,
        request: project_service.UpdateAlertConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        project_service.UpdateAlertConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_alert_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProjectService server.
        """
        return request, metadata

    def post_update_alert_config(
        self, response: project.AlertConfig
    ) -> project.AlertConfig:
        """Post-rpc interceptor for update_alert_config

        DEPRECATED. Please use the `post_update_alert_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProjectService server but before
        it is returned to user code. This `post_update_alert_config` interceptor runs
        before the `post_update_alert_config_with_metadata` interceptor.
        """
        return response

    def post_update_alert_config_with_metadata(
        self,
        response: project.AlertConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[project.AlertConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_alert_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProjectService server but before it is returned to user code.

        We recommend only using this `post_update_alert_config_with_metadata`
        interceptor in new development instead of the `post_update_alert_config` interceptor.
        When both interceptors are used, this `post_update_alert_config_with_metadata` interceptor runs after the
        `post_update_alert_config` interceptor. The (possibly modified) response returned by
        `post_update_alert_config` will be passed to
        `post_update_alert_config_with_metadata`.
        """
        return response, metadata

    def pre_update_logging_config(
        self,
        request: project_service.UpdateLoggingConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        project_service.UpdateLoggingConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_logging_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ProjectService server.
        """
        return request, metadata

    def post_update_logging_config(
        self, response: project.LoggingConfig
    ) -> project.LoggingConfig:
        """Post-rpc interceptor for update_logging_config

        DEPRECATED. Please use the `post_update_logging_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ProjectService server but before
        it is returned to user code. This `post_update_logging_config` interceptor runs
        before the `post_update_logging_config_with_metadata` interceptor.
        """
        return response

    def post_update_logging_config_with_metadata(
        self,
        response: project.LoggingConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[project.LoggingConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_logging_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ProjectService server but before it is returned to user code.

        We recommend only using this `post_update_logging_config_with_metadata`
        interceptor in new development instead of the `post_update_logging_config` interceptor.
        When both interceptors are used, this `post_update_logging_config_with_metadata` interceptor runs after the
        `post_update_logging_config` interceptor. The (possibly modified) response returned by
        `post_update_logging_config` will be passed to
        `post_update_logging_config_with_metadata`.
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
        before they are sent to the ProjectService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the ProjectService server but before
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
        before they are sent to the ProjectService server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the ProjectService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class ProjectServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ProjectServiceRestInterceptor


class ProjectServiceRestTransport(_BaseProjectServiceRestTransport):
    """REST backend synchronous transport for ProjectService.

    Service for settings at Project level.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "retail.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[ProjectServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'retail.googleapis.com').
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
            interceptor (Optional[ProjectServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or ProjectServiceRestInterceptor()
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
                        "uri": "/v2alpha/{name=projects/*/locations/*/catalogs/*/branches/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v2alpha/{name=projects/*/locations/*/catalogs/*/branches/*/places/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v2alpha/{name=projects/*/locations/*/catalogs/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v2alpha/{name=projects/*/locations/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v2alpha/{name=projects/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v2alpha/{name=projects/*/locations/*/catalogs/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v2alpha/{name=projects/*/locations/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v2alpha/{name=projects/*}/operations",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v2alpha",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _AcceptTerms(
        _BaseProjectServiceRestTransport._BaseAcceptTerms, ProjectServiceRestStub
    ):
        def __hash__(self):
            return hash("ProjectServiceRestTransport.AcceptTerms")

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
            request: project_service.AcceptTermsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcr_project.Project:
            r"""Call the accept terms method over HTTP.

            Args:
                request (~.project_service.AcceptTermsRequest):
                    The request object. Request for AcceptTerms method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcr_project.Project:
                    Metadata that describes a Cloud
                Retail Project.

            """

            http_options = (
                _BaseProjectServiceRestTransport._BaseAcceptTerms._get_http_options()
            )
            request, metadata = self._interceptor.pre_accept_terms(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProjectServiceRestTransport._BaseAcceptTerms,
                    "_BaseAcceptTerms__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.retail_v2alpha.ProjectServiceClient.AcceptTerms",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.ProjectService",
                        "rpcName": "AcceptTerms",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProjectServiceRestTransport._AcceptTerms._get_response(
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
            resp = gcr_project.Project()
            pb_resp = gcr_project.Project.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_accept_terms(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_accept_terms_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcr_project.Project.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.retail_v2alpha.ProjectServiceClient.accept_terms",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.ProjectService",
                        "rpcName": "AcceptTerms",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _EnrollSolution(
        _BaseProjectServiceRestTransport._BaseEnrollSolution, ProjectServiceRestStub
    ):
        def __hash__(self):
            return hash("ProjectServiceRestTransport.EnrollSolution")

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
            request: project_service.EnrollSolutionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the enroll solution method over HTTP.

            Args:
                request (~.project_service.EnrollSolutionRequest):
                    The request object. Request for EnrollSolution method.
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
                _BaseProjectServiceRestTransport._BaseEnrollSolution._get_http_options()
            )
            request, metadata = self._interceptor.pre_enroll_solution(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProjectServiceRestTransport._BaseEnrollSolution,
                    "_BaseEnrollSolution__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.retail_v2alpha.ProjectServiceClient.EnrollSolution",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.ProjectService",
                        "rpcName": "EnrollSolution",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProjectServiceRestTransport._EnrollSolution._get_response(
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

            resp = self._interceptor.post_enroll_solution(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_enroll_solution_with_metadata(
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
                    "Received response for google.cloud.retail_v2alpha.ProjectServiceClient.enroll_solution",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.ProjectService",
                        "rpcName": "EnrollSolution",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAlertConfig(
        _BaseProjectServiceRestTransport._BaseGetAlertConfig, ProjectServiceRestStub
    ):
        def __hash__(self):
            return hash("ProjectServiceRestTransport.GetAlertConfig")

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
            request: project_service.GetAlertConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> project.AlertConfig:
            r"""Call the get alert config method over HTTP.

            Args:
                request (~.project_service.GetAlertConfigRequest):
                    The request object. Request for
                [ProjectService.GetAlertConfig][google.cloud.retail.v2alpha.ProjectService.GetAlertConfig]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.project.AlertConfig:
                    Project level alert config.
            """

            http_options = (
                _BaseProjectServiceRestTransport._BaseGetAlertConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_alert_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProjectServiceRestTransport._BaseGetAlertConfig,
                    "_BaseGetAlertConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.retail_v2alpha.ProjectServiceClient.GetAlertConfig",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.ProjectService",
                        "rpcName": "GetAlertConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProjectServiceRestTransport._GetAlertConfig._get_response(
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
            resp = project.AlertConfig()
            pb_resp = project.AlertConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_alert_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_alert_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = project.AlertConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.retail_v2alpha.ProjectServiceClient.get_alert_config",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.ProjectService",
                        "rpcName": "GetAlertConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetLoggingConfig(
        _BaseProjectServiceRestTransport._BaseGetLoggingConfig, ProjectServiceRestStub
    ):
        def __hash__(self):
            return hash("ProjectServiceRestTransport.GetLoggingConfig")

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
            request: project_service.GetLoggingConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> project.LoggingConfig:
            r"""Call the get logging config method over HTTP.

            Args:
                request (~.project_service.GetLoggingConfigRequest):
                    The request object. Request for
                [ProjectService.GetLoggingConfig][google.cloud.retail.v2alpha.ProjectService.GetLoggingConfig]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.project.LoggingConfig:
                    Project level logging config to
                control what level of log will be
                generated and written to Cloud Logging.

            """

            http_options = _BaseProjectServiceRestTransport._BaseGetLoggingConfig._get_http_options()
            request, metadata = self._interceptor.pre_get_logging_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProjectServiceRestTransport._BaseGetLoggingConfig,
                    "_BaseGetLoggingConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.retail_v2alpha.ProjectServiceClient.GetLoggingConfig",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.ProjectService",
                        "rpcName": "GetLoggingConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProjectServiceRestTransport._GetLoggingConfig._get_response(
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
            resp = project.LoggingConfig()
            pb_resp = project.LoggingConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_logging_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_logging_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = project.LoggingConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.retail_v2alpha.ProjectServiceClient.get_logging_config",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.ProjectService",
                        "rpcName": "GetLoggingConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetProject(
        _BaseProjectServiceRestTransport._BaseGetProject, ProjectServiceRestStub
    ):
        def __hash__(self):
            return hash("ProjectServiceRestTransport.GetProject")

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
            request: project_service.GetProjectRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> project.Project:
            r"""Call the get project method over HTTP.

            Args:
                request (~.project_service.GetProjectRequest):
                    The request object. Request for GetProject method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.project.Project:
                    Metadata that describes a Cloud
                Retail Project.

            """

            http_options = (
                _BaseProjectServiceRestTransport._BaseGetProject._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_project(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProjectServiceRestTransport._BaseGetProject,
                    "_BaseGetProject__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.retail_v2alpha.ProjectServiceClient.GetProject",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.ProjectService",
                        "rpcName": "GetProject",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProjectServiceRestTransport._GetProject._get_response(
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
            resp = project.Project()
            pb_resp = project.Project.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_project(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_project_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = project.Project.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.retail_v2alpha.ProjectServiceClient.get_project",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.ProjectService",
                        "rpcName": "GetProject",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListEnrolledSolutions(
        _BaseProjectServiceRestTransport._BaseListEnrolledSolutions,
        ProjectServiceRestStub,
    ):
        def __hash__(self):
            return hash("ProjectServiceRestTransport.ListEnrolledSolutions")

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
            request: project_service.ListEnrolledSolutionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> project_service.ListEnrolledSolutionsResponse:
            r"""Call the list enrolled solutions method over HTTP.

            Args:
                request (~.project_service.ListEnrolledSolutionsRequest):
                    The request object. Request for ListEnrolledSolutions
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.project_service.ListEnrolledSolutionsResponse:
                    Response for ListEnrolledSolutions
                method.

            """

            http_options = _BaseProjectServiceRestTransport._BaseListEnrolledSolutions._get_http_options()
            request, metadata = self._interceptor.pre_list_enrolled_solutions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProjectServiceRestTransport._BaseListEnrolledSolutions,
                    "_BaseListEnrolledSolutions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.retail_v2alpha.ProjectServiceClient.ListEnrolledSolutions",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.ProjectService",
                        "rpcName": "ListEnrolledSolutions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProjectServiceRestTransport._ListEnrolledSolutions._get_response(
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
            resp = project_service.ListEnrolledSolutionsResponse()
            pb_resp = project_service.ListEnrolledSolutionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_enrolled_solutions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_enrolled_solutions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        project_service.ListEnrolledSolutionsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.retail_v2alpha.ProjectServiceClient.list_enrolled_solutions",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.ProjectService",
                        "rpcName": "ListEnrolledSolutions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateAlertConfig(
        _BaseProjectServiceRestTransport._BaseUpdateAlertConfig, ProjectServiceRestStub
    ):
        def __hash__(self):
            return hash("ProjectServiceRestTransport.UpdateAlertConfig")

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
            request: project_service.UpdateAlertConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> project.AlertConfig:
            r"""Call the update alert config method over HTTP.

            Args:
                request (~.project_service.UpdateAlertConfigRequest):
                    The request object. Request for
                [ProjectService.UpdateAlertConfig][google.cloud.retail.v2alpha.ProjectService.UpdateAlertConfig]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.project.AlertConfig:
                    Project level alert config.
            """

            http_options = _BaseProjectServiceRestTransport._BaseUpdateAlertConfig._get_http_options()
            request, metadata = self._interceptor.pre_update_alert_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProjectServiceRestTransport._BaseUpdateAlertConfig,
                    "_BaseUpdateAlertConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.retail_v2alpha.ProjectServiceClient.UpdateAlertConfig",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.ProjectService",
                        "rpcName": "UpdateAlertConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProjectServiceRestTransport._UpdateAlertConfig._get_response(
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
            resp = project.AlertConfig()
            pb_resp = project.AlertConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_alert_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_alert_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = project.AlertConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.retail_v2alpha.ProjectServiceClient.update_alert_config",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.ProjectService",
                        "rpcName": "UpdateAlertConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateLoggingConfig(
        _BaseProjectServiceRestTransport._BaseUpdateLoggingConfig,
        ProjectServiceRestStub,
    ):
        def __hash__(self):
            return hash("ProjectServiceRestTransport.UpdateLoggingConfig")

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
            request: project_service.UpdateLoggingConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> project.LoggingConfig:
            r"""Call the update logging config method over HTTP.

            Args:
                request (~.project_service.UpdateLoggingConfigRequest):
                    The request object. Request for
                [ProjectService.UpdateLoggingConfig][google.cloud.retail.v2alpha.ProjectService.UpdateLoggingConfig]
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.project.LoggingConfig:
                    Project level logging config to
                control what level of log will be
                generated and written to Cloud Logging.

            """

            http_options = _BaseProjectServiceRestTransport._BaseUpdateLoggingConfig._get_http_options()
            request, metadata = self._interceptor.pre_update_logging_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProjectServiceRestTransport._BaseUpdateLoggingConfig,
                    "_BaseUpdateLoggingConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.retail_v2alpha.ProjectServiceClient.UpdateLoggingConfig",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.ProjectService",
                        "rpcName": "UpdateLoggingConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProjectServiceRestTransport._UpdateLoggingConfig._get_response(
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
            resp = project.LoggingConfig()
            pb_resp = project.LoggingConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_logging_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_logging_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = project.LoggingConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.retail_v2alpha.ProjectServiceClient.update_logging_config",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.ProjectService",
                        "rpcName": "UpdateLoggingConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def accept_terms(
        self,
    ) -> Callable[[project_service.AcceptTermsRequest], gcr_project.Project]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AcceptTerms(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def enroll_solution(
        self,
    ) -> Callable[[project_service.EnrollSolutionRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._EnrollSolution(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_alert_config(
        self,
    ) -> Callable[[project_service.GetAlertConfigRequest], project.AlertConfig]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAlertConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_logging_config(
        self,
    ) -> Callable[[project_service.GetLoggingConfigRequest], project.LoggingConfig]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetLoggingConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_project(
        self,
    ) -> Callable[[project_service.GetProjectRequest], project.Project]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetProject(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_enrolled_solutions(
        self,
    ) -> Callable[
        [project_service.ListEnrolledSolutionsRequest],
        project_service.ListEnrolledSolutionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListEnrolledSolutions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_alert_config(
        self,
    ) -> Callable[[project_service.UpdateAlertConfigRequest], project.AlertConfig]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateAlertConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_logging_config(
        self,
    ) -> Callable[[project_service.UpdateLoggingConfigRequest], project.LoggingConfig]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateLoggingConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseProjectServiceRestTransport._BaseGetOperation, ProjectServiceRestStub
    ):
        def __hash__(self):
            return hash("ProjectServiceRestTransport.GetOperation")

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
                _BaseProjectServiceRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProjectServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.retail_v2alpha.ProjectServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.ProjectService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProjectServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.retail_v2alpha.ProjectServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.ProjectService",
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
        _BaseProjectServiceRestTransport._BaseListOperations, ProjectServiceRestStub
    ):
        def __hash__(self):
            return hash("ProjectServiceRestTransport.ListOperations")

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

            http_options = (
                _BaseProjectServiceRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseProjectServiceRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.retail_v2alpha.ProjectServiceClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.ProjectService",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ProjectServiceRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.retail_v2alpha.ProjectServiceAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.retail.v2alpha.ProjectService",
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


__all__ = ("ProjectServiceRestTransport",)
