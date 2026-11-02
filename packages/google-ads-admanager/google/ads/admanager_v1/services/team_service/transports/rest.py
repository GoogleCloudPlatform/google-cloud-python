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
from google.ads.admanager_v1.types import team_messages, team_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseTeamServiceRestTransport

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


class TeamServiceRestInterceptor:
    """Interceptor for TeamService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the TeamServiceRestTransport.

    .. code-block:: python
        class MyCustomTeamServiceInterceptor(TeamServiceRestInterceptor):
            def pre_batch_activate_teams(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_activate_teams(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_create_teams(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_teams(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_deactivate_teams(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_deactivate_teams(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_update_teams(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_teams(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_team(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_team(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_team(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_team(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_teams(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_teams(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_team(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_team(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = TeamServiceRestTransport(interceptor=MyCustomTeamServiceInterceptor())
        client = TeamServiceClient(transport=transport)


    """

    def pre_batch_activate_teams(
        self,
        request: team_service.BatchActivateTeamsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        team_service.BatchActivateTeamsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for batch_activate_teams

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TeamService server.
        """
        return request, metadata

    def post_batch_activate_teams(
        self, response: team_service.BatchActivateTeamsResponse
    ) -> team_service.BatchActivateTeamsResponse:
        """Post-rpc interceptor for batch_activate_teams

        DEPRECATED. Please use the `post_batch_activate_teams_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TeamService server but before
        it is returned to user code. This `post_batch_activate_teams` interceptor runs
        before the `post_batch_activate_teams_with_metadata` interceptor.
        """
        return response

    def post_batch_activate_teams_with_metadata(
        self,
        response: team_service.BatchActivateTeamsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        team_service.BatchActivateTeamsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for batch_activate_teams

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TeamService server but before it is returned to user code.

        We recommend only using this `post_batch_activate_teams_with_metadata`
        interceptor in new development instead of the `post_batch_activate_teams` interceptor.
        When both interceptors are used, this `post_batch_activate_teams_with_metadata` interceptor runs after the
        `post_batch_activate_teams` interceptor. The (possibly modified) response returned by
        `post_batch_activate_teams` will be passed to
        `post_batch_activate_teams_with_metadata`.
        """
        return response, metadata

    def pre_batch_create_teams(
        self,
        request: team_service.BatchCreateTeamsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        team_service.BatchCreateTeamsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for batch_create_teams

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TeamService server.
        """
        return request, metadata

    def post_batch_create_teams(
        self, response: team_service.BatchCreateTeamsResponse
    ) -> team_service.BatchCreateTeamsResponse:
        """Post-rpc interceptor for batch_create_teams

        DEPRECATED. Please use the `post_batch_create_teams_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TeamService server but before
        it is returned to user code. This `post_batch_create_teams` interceptor runs
        before the `post_batch_create_teams_with_metadata` interceptor.
        """
        return response

    def post_batch_create_teams_with_metadata(
        self,
        response: team_service.BatchCreateTeamsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        team_service.BatchCreateTeamsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for batch_create_teams

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TeamService server but before it is returned to user code.

        We recommend only using this `post_batch_create_teams_with_metadata`
        interceptor in new development instead of the `post_batch_create_teams` interceptor.
        When both interceptors are used, this `post_batch_create_teams_with_metadata` interceptor runs after the
        `post_batch_create_teams` interceptor. The (possibly modified) response returned by
        `post_batch_create_teams` will be passed to
        `post_batch_create_teams_with_metadata`.
        """
        return response, metadata

    def pre_batch_deactivate_teams(
        self,
        request: team_service.BatchDeactivateTeamsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        team_service.BatchDeactivateTeamsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_deactivate_teams

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TeamService server.
        """
        return request, metadata

    def post_batch_deactivate_teams(
        self, response: team_service.BatchDeactivateTeamsResponse
    ) -> team_service.BatchDeactivateTeamsResponse:
        """Post-rpc interceptor for batch_deactivate_teams

        DEPRECATED. Please use the `post_batch_deactivate_teams_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TeamService server but before
        it is returned to user code. This `post_batch_deactivate_teams` interceptor runs
        before the `post_batch_deactivate_teams_with_metadata` interceptor.
        """
        return response

    def post_batch_deactivate_teams_with_metadata(
        self,
        response: team_service.BatchDeactivateTeamsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        team_service.BatchDeactivateTeamsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_deactivate_teams

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TeamService server but before it is returned to user code.

        We recommend only using this `post_batch_deactivate_teams_with_metadata`
        interceptor in new development instead of the `post_batch_deactivate_teams` interceptor.
        When both interceptors are used, this `post_batch_deactivate_teams_with_metadata` interceptor runs after the
        `post_batch_deactivate_teams` interceptor. The (possibly modified) response returned by
        `post_batch_deactivate_teams` will be passed to
        `post_batch_deactivate_teams_with_metadata`.
        """
        return response, metadata

    def pre_batch_update_teams(
        self,
        request: team_service.BatchUpdateTeamsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        team_service.BatchUpdateTeamsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for batch_update_teams

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TeamService server.
        """
        return request, metadata

    def post_batch_update_teams(
        self, response: team_service.BatchUpdateTeamsResponse
    ) -> team_service.BatchUpdateTeamsResponse:
        """Post-rpc interceptor for batch_update_teams

        DEPRECATED. Please use the `post_batch_update_teams_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TeamService server but before
        it is returned to user code. This `post_batch_update_teams` interceptor runs
        before the `post_batch_update_teams_with_metadata` interceptor.
        """
        return response

    def post_batch_update_teams_with_metadata(
        self,
        response: team_service.BatchUpdateTeamsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        team_service.BatchUpdateTeamsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for batch_update_teams

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TeamService server but before it is returned to user code.

        We recommend only using this `post_batch_update_teams_with_metadata`
        interceptor in new development instead of the `post_batch_update_teams` interceptor.
        When both interceptors are used, this `post_batch_update_teams_with_metadata` interceptor runs after the
        `post_batch_update_teams` interceptor. The (possibly modified) response returned by
        `post_batch_update_teams` will be passed to
        `post_batch_update_teams_with_metadata`.
        """
        return response, metadata

    def pre_create_team(
        self,
        request: team_service.CreateTeamRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[team_service.CreateTeamRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_team

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TeamService server.
        """
        return request, metadata

    def post_create_team(self, response: team_messages.Team) -> team_messages.Team:
        """Post-rpc interceptor for create_team

        DEPRECATED. Please use the `post_create_team_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TeamService server but before
        it is returned to user code. This `post_create_team` interceptor runs
        before the `post_create_team_with_metadata` interceptor.
        """
        return response

    def post_create_team_with_metadata(
        self,
        response: team_messages.Team,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[team_messages.Team, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_team

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TeamService server but before it is returned to user code.

        We recommend only using this `post_create_team_with_metadata`
        interceptor in new development instead of the `post_create_team` interceptor.
        When both interceptors are used, this `post_create_team_with_metadata` interceptor runs after the
        `post_create_team` interceptor. The (possibly modified) response returned by
        `post_create_team` will be passed to
        `post_create_team_with_metadata`.
        """
        return response, metadata

    def pre_get_team(
        self,
        request: team_service.GetTeamRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[team_service.GetTeamRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_team

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TeamService server.
        """
        return request, metadata

    def post_get_team(self, response: team_messages.Team) -> team_messages.Team:
        """Post-rpc interceptor for get_team

        DEPRECATED. Please use the `post_get_team_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TeamService server but before
        it is returned to user code. This `post_get_team` interceptor runs
        before the `post_get_team_with_metadata` interceptor.
        """
        return response

    def post_get_team_with_metadata(
        self,
        response: team_messages.Team,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[team_messages.Team, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_team

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TeamService server but before it is returned to user code.

        We recommend only using this `post_get_team_with_metadata`
        interceptor in new development instead of the `post_get_team` interceptor.
        When both interceptors are used, this `post_get_team_with_metadata` interceptor runs after the
        `post_get_team` interceptor. The (possibly modified) response returned by
        `post_get_team` will be passed to
        `post_get_team_with_metadata`.
        """
        return response, metadata

    def pre_list_teams(
        self,
        request: team_service.ListTeamsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[team_service.ListTeamsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_teams

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TeamService server.
        """
        return request, metadata

    def post_list_teams(
        self, response: team_service.ListTeamsResponse
    ) -> team_service.ListTeamsResponse:
        """Post-rpc interceptor for list_teams

        DEPRECATED. Please use the `post_list_teams_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TeamService server but before
        it is returned to user code. This `post_list_teams` interceptor runs
        before the `post_list_teams_with_metadata` interceptor.
        """
        return response

    def post_list_teams_with_metadata(
        self,
        response: team_service.ListTeamsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[team_service.ListTeamsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_teams

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TeamService server but before it is returned to user code.

        We recommend only using this `post_list_teams_with_metadata`
        interceptor in new development instead of the `post_list_teams` interceptor.
        When both interceptors are used, this `post_list_teams_with_metadata` interceptor runs after the
        `post_list_teams` interceptor. The (possibly modified) response returned by
        `post_list_teams` will be passed to
        `post_list_teams_with_metadata`.
        """
        return response, metadata

    def pre_update_team(
        self,
        request: team_service.UpdateTeamRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[team_service.UpdateTeamRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_team

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TeamService server.
        """
        return request, metadata

    def post_update_team(self, response: team_messages.Team) -> team_messages.Team:
        """Post-rpc interceptor for update_team

        DEPRECATED. Please use the `post_update_team_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TeamService server but before
        it is returned to user code. This `post_update_team` interceptor runs
        before the `post_update_team_with_metadata` interceptor.
        """
        return response

    def post_update_team_with_metadata(
        self,
        response: team_messages.Team,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[team_messages.Team, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_team

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TeamService server but before it is returned to user code.

        We recommend only using this `post_update_team_with_metadata`
        interceptor in new development instead of the `post_update_team` interceptor.
        When both interceptors are used, this `post_update_team_with_metadata` interceptor runs after the
        `post_update_team` interceptor. The (possibly modified) response returned by
        `post_update_team` will be passed to
        `post_update_team_with_metadata`.
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
        before they are sent to the TeamService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the TeamService server but before
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
        before they are sent to the TeamService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the TeamService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class TeamServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: TeamServiceRestInterceptor


class TeamServiceRestTransport(_BaseTeamServiceRestTransport):
    """REST backend synchronous transport for TeamService.

    Provides methods for handling ``Team`` objects.

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
        interceptor: Optional[TeamServiceRestInterceptor] = None,
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
            interceptor (Optional[TeamServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or TeamServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchActivateTeams(
        _BaseTeamServiceRestTransport._BaseBatchActivateTeams, TeamServiceRestStub
    ):
        def __hash__(self):
            return hash("TeamServiceRestTransport.BatchActivateTeams")

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
            request: team_service.BatchActivateTeamsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> team_service.BatchActivateTeamsResponse:
            r"""Call the batch activate teams method over HTTP.

            Args:
                request (~.team_service.BatchActivateTeamsRequest):
                    The request object. Request message for ``BatchActivateTeams`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.team_service.BatchActivateTeamsResponse:
                    Response object for ``BatchActivateTeams`` method.
            """

            http_options = _BaseTeamServiceRestTransport._BaseBatchActivateTeams._get_http_options()
            request, metadata = self._interceptor.pre_batch_activate_teams(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTeamServiceRestTransport._BaseBatchActivateTeams,
                    "_BaseBatchActivateTeams__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.TeamServiceClient.BatchActivateTeams",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TeamService",
                        "rpcName": "BatchActivateTeams",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TeamServiceRestTransport._BatchActivateTeams._get_response(
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
            resp = team_service.BatchActivateTeamsResponse()
            pb_resp = team_service.BatchActivateTeamsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_activate_teams(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_activate_teams_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = team_service.BatchActivateTeamsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.TeamServiceClient.batch_activate_teams",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TeamService",
                        "rpcName": "BatchActivateTeams",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchCreateTeams(
        _BaseTeamServiceRestTransport._BaseBatchCreateTeams, TeamServiceRestStub
    ):
        def __hash__(self):
            return hash("TeamServiceRestTransport.BatchCreateTeams")

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
            request: team_service.BatchCreateTeamsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> team_service.BatchCreateTeamsResponse:
            r"""Call the batch create teams method over HTTP.

            Args:
                request (~.team_service.BatchCreateTeamsRequest):
                    The request object. Request object for ``BatchCreateTeams`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.team_service.BatchCreateTeamsResponse:
                    Response object for ``BatchCreateTeams`` method.
            """

            http_options = (
                _BaseTeamServiceRestTransport._BaseBatchCreateTeams._get_http_options()
            )
            request, metadata = self._interceptor.pre_batch_create_teams(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTeamServiceRestTransport._BaseBatchCreateTeams,
                    "_BaseBatchCreateTeams__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.TeamServiceClient.BatchCreateTeams",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TeamService",
                        "rpcName": "BatchCreateTeams",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TeamServiceRestTransport._BatchCreateTeams._get_response(
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
            resp = team_service.BatchCreateTeamsResponse()
            pb_resp = team_service.BatchCreateTeamsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_teams(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_create_teams_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = team_service.BatchCreateTeamsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.TeamServiceClient.batch_create_teams",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TeamService",
                        "rpcName": "BatchCreateTeams",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchDeactivateTeams(
        _BaseTeamServiceRestTransport._BaseBatchDeactivateTeams, TeamServiceRestStub
    ):
        def __hash__(self):
            return hash("TeamServiceRestTransport.BatchDeactivateTeams")

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
            request: team_service.BatchDeactivateTeamsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> team_service.BatchDeactivateTeamsResponse:
            r"""Call the batch deactivate teams method over HTTP.

            Args:
                request (~.team_service.BatchDeactivateTeamsRequest):
                    The request object. Request message for ``BatchDeactivateTeams`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.team_service.BatchDeactivateTeamsResponse:
                    Response object for ``BatchDeactivateTeams`` method.
            """

            http_options = _BaseTeamServiceRestTransport._BaseBatchDeactivateTeams._get_http_options()
            request, metadata = self._interceptor.pre_batch_deactivate_teams(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTeamServiceRestTransport._BaseBatchDeactivateTeams,
                    "_BaseBatchDeactivateTeams__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.TeamServiceClient.BatchDeactivateTeams",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TeamService",
                        "rpcName": "BatchDeactivateTeams",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TeamServiceRestTransport._BatchDeactivateTeams._get_response(
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
            resp = team_service.BatchDeactivateTeamsResponse()
            pb_resp = team_service.BatchDeactivateTeamsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_deactivate_teams(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_deactivate_teams_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        team_service.BatchDeactivateTeamsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.TeamServiceClient.batch_deactivate_teams",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TeamService",
                        "rpcName": "BatchDeactivateTeams",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchUpdateTeams(
        _BaseTeamServiceRestTransport._BaseBatchUpdateTeams, TeamServiceRestStub
    ):
        def __hash__(self):
            return hash("TeamServiceRestTransport.BatchUpdateTeams")

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
            request: team_service.BatchUpdateTeamsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> team_service.BatchUpdateTeamsResponse:
            r"""Call the batch update teams method over HTTP.

            Args:
                request (~.team_service.BatchUpdateTeamsRequest):
                    The request object. Request object for ``BatchUpdateTeams`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.team_service.BatchUpdateTeamsResponse:
                    Response object for ``BatchUpdateTeams`` method.
            """

            http_options = (
                _BaseTeamServiceRestTransport._BaseBatchUpdateTeams._get_http_options()
            )
            request, metadata = self._interceptor.pre_batch_update_teams(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTeamServiceRestTransport._BaseBatchUpdateTeams,
                    "_BaseBatchUpdateTeams__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.TeamServiceClient.BatchUpdateTeams",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TeamService",
                        "rpcName": "BatchUpdateTeams",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TeamServiceRestTransport._BatchUpdateTeams._get_response(
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
            resp = team_service.BatchUpdateTeamsResponse()
            pb_resp = team_service.BatchUpdateTeamsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_teams(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_update_teams_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = team_service.BatchUpdateTeamsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.TeamServiceClient.batch_update_teams",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TeamService",
                        "rpcName": "BatchUpdateTeams",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateTeam(
        _BaseTeamServiceRestTransport._BaseCreateTeam, TeamServiceRestStub
    ):
        def __hash__(self):
            return hash("TeamServiceRestTransport.CreateTeam")

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
            request: team_service.CreateTeamRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> team_messages.Team:
            r"""Call the create team method over HTTP.

            Args:
                request (~.team_service.CreateTeamRequest):
                    The request object. Request object for ``CreateTeam`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.team_messages.Team:
                    A Team defines a grouping of users
                and what entities they have access to.

            """

            http_options = (
                _BaseTeamServiceRestTransport._BaseCreateTeam._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_team(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTeamServiceRestTransport._BaseCreateTeam,
                    "_BaseCreateTeam__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.TeamServiceClient.CreateTeam",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TeamService",
                        "rpcName": "CreateTeam",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TeamServiceRestTransport._CreateTeam._get_response(
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
            resp = team_messages.Team()
            pb_resp = team_messages.Team.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_team(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_team_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = team_messages.Team.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.TeamServiceClient.create_team",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TeamService",
                        "rpcName": "CreateTeam",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetTeam(_BaseTeamServiceRestTransport._BaseGetTeam, TeamServiceRestStub):
        def __hash__(self):
            return hash("TeamServiceRestTransport.GetTeam")

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
            request: team_service.GetTeamRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> team_messages.Team:
            r"""Call the get team method over HTTP.

            Args:
                request (~.team_service.GetTeamRequest):
                    The request object. Request object for ``GetTeam`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.team_messages.Team:
                    A Team defines a grouping of users
                and what entities they have access to.

            """

            http_options = (
                _BaseTeamServiceRestTransport._BaseGetTeam._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_team(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTeamServiceRestTransport._BaseGetTeam,
                    "_BaseGetTeam__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.TeamServiceClient.GetTeam",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TeamService",
                        "rpcName": "GetTeam",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TeamServiceRestTransport._GetTeam._get_response(
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
            resp = team_messages.Team()
            pb_resp = team_messages.Team.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_team(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_team_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = team_messages.Team.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.TeamServiceClient.get_team",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TeamService",
                        "rpcName": "GetTeam",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListTeams(_BaseTeamServiceRestTransport._BaseListTeams, TeamServiceRestStub):
        def __hash__(self):
            return hash("TeamServiceRestTransport.ListTeams")

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
            request: team_service.ListTeamsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> team_service.ListTeamsResponse:
            r"""Call the list teams method over HTTP.

            Args:
                request (~.team_service.ListTeamsRequest):
                    The request object. Request object for ``ListTeams`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.team_service.ListTeamsResponse:
                    Response object for ``ListTeamsRequest`` containing
                matching ``Team`` objects.

            """

            http_options = (
                _BaseTeamServiceRestTransport._BaseListTeams._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_teams(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTeamServiceRestTransport._BaseListTeams,
                    "_BaseListTeams__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.TeamServiceClient.ListTeams",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TeamService",
                        "rpcName": "ListTeams",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TeamServiceRestTransport._ListTeams._get_response(
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
            resp = team_service.ListTeamsResponse()
            pb_resp = team_service.ListTeamsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_teams(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_teams_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = team_service.ListTeamsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.TeamServiceClient.list_teams",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TeamService",
                        "rpcName": "ListTeams",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateTeam(
        _BaseTeamServiceRestTransport._BaseUpdateTeam, TeamServiceRestStub
    ):
        def __hash__(self):
            return hash("TeamServiceRestTransport.UpdateTeam")

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
            request: team_service.UpdateTeamRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> team_messages.Team:
            r"""Call the update team method over HTTP.

            Args:
                request (~.team_service.UpdateTeamRequest):
                    The request object. Request object for ``UpdateTeam`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.team_messages.Team:
                    A Team defines a grouping of users
                and what entities they have access to.

            """

            http_options = (
                _BaseTeamServiceRestTransport._BaseUpdateTeam._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_team(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTeamServiceRestTransport._BaseUpdateTeam,
                    "_BaseUpdateTeam__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.TeamServiceClient.UpdateTeam",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TeamService",
                        "rpcName": "UpdateTeam",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TeamServiceRestTransport._UpdateTeam._get_response(
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
            resp = team_messages.Team()
            pb_resp = team_messages.Team.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_team(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_team_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = team_messages.Team.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.TeamServiceClient.update_team",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TeamService",
                        "rpcName": "UpdateTeam",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_activate_teams(
        self,
    ) -> Callable[
        [team_service.BatchActivateTeamsRequest],
        team_service.BatchActivateTeamsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchActivateTeams(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_create_teams(
        self,
    ) -> Callable[
        [team_service.BatchCreateTeamsRequest], team_service.BatchCreateTeamsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateTeams(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_deactivate_teams(
        self,
    ) -> Callable[
        [team_service.BatchDeactivateTeamsRequest],
        team_service.BatchDeactivateTeamsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchDeactivateTeams(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_update_teams(
        self,
    ) -> Callable[
        [team_service.BatchUpdateTeamsRequest], team_service.BatchUpdateTeamsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdateTeams(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_team(
        self,
    ) -> Callable[[team_service.CreateTeamRequest], team_messages.Team]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateTeam(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_team(self) -> Callable[[team_service.GetTeamRequest], team_messages.Team]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTeam(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_teams(
        self,
    ) -> Callable[[team_service.ListTeamsRequest], team_service.ListTeamsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTeams(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_team(
        self,
    ) -> Callable[[team_service.UpdateTeamRequest], team_messages.Team]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateTeam(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseTeamServiceRestTransport._BaseCancelOperation, TeamServiceRestStub
    ):
        def __hash__(self):
            return hash("TeamServiceRestTransport.CancelOperation")

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
                _BaseTeamServiceRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTeamServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.ads.admanager_v1.TeamServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TeamService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TeamServiceRestTransport._CancelOperation._get_response(
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
        _BaseTeamServiceRestTransport._BaseGetOperation, TeamServiceRestStub
    ):
        def __hash__(self):
            return hash("TeamServiceRestTransport.GetOperation")

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
                _BaseTeamServiceRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTeamServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.ads.admanager_v1.TeamServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TeamService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TeamServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.ads.admanager_v1.TeamServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.TeamService",
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


__all__ = ("TeamServiceRestTransport",)
