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

from google.apps.meet_v2beta._compat import transcode_request
from google.apps.meet_v2beta.types import resource, service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseSpacesServiceRestTransport

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


class SpacesServiceRestInterceptor:
    """Interceptor for SpacesService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the SpacesServiceRestTransport.

    .. code-block:: python
        class MyCustomSpacesServiceInterceptor(SpacesServiceRestInterceptor):
            def pre_batch_update_members(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_members(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_connect_active_conference(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_connect_active_conference(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_member(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_member(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_space(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_space(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_member(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_end_active_conference(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_member(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_member(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_space(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_space(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_members(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_members(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_member(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_member(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_space(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_space(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = SpacesServiceRestTransport(interceptor=MyCustomSpacesServiceInterceptor())
        client = SpacesServiceClient(transport=transport)


    """

    def pre_batch_update_members(
        self,
        request: service.BatchUpdateMembersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.BatchUpdateMembersRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for batch_update_members

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SpacesService server.
        """
        return request, metadata

    def post_batch_update_members(
        self, response: service.BatchUpdateMembersResponse
    ) -> service.BatchUpdateMembersResponse:
        """Post-rpc interceptor for batch_update_members

        DEPRECATED. Please use the `post_batch_update_members_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SpacesService server but before
        it is returned to user code. This `post_batch_update_members` interceptor runs
        before the `post_batch_update_members_with_metadata` interceptor.
        """
        return response

    def post_batch_update_members_with_metadata(
        self,
        response: service.BatchUpdateMembersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.BatchUpdateMembersResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for batch_update_members

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SpacesService server but before it is returned to user code.

        We recommend only using this `post_batch_update_members_with_metadata`
        interceptor in new development instead of the `post_batch_update_members` interceptor.
        When both interceptors are used, this `post_batch_update_members_with_metadata` interceptor runs after the
        `post_batch_update_members` interceptor. The (possibly modified) response returned by
        `post_batch_update_members` will be passed to
        `post_batch_update_members_with_metadata`.
        """
        return response, metadata

    def pre_connect_active_conference(
        self,
        request: service.ConnectActiveConferenceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ConnectActiveConferenceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for connect_active_conference

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SpacesService server.
        """
        return request, metadata

    def post_connect_active_conference(
        self, response: service.ConnectActiveConferenceResponse
    ) -> service.ConnectActiveConferenceResponse:
        """Post-rpc interceptor for connect_active_conference

        DEPRECATED. Please use the `post_connect_active_conference_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SpacesService server but before
        it is returned to user code. This `post_connect_active_conference` interceptor runs
        before the `post_connect_active_conference_with_metadata` interceptor.
        """
        return response

    def post_connect_active_conference_with_metadata(
        self,
        response: service.ConnectActiveConferenceResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ConnectActiveConferenceResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for connect_active_conference

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SpacesService server but before it is returned to user code.

        We recommend only using this `post_connect_active_conference_with_metadata`
        interceptor in new development instead of the `post_connect_active_conference` interceptor.
        When both interceptors are used, this `post_connect_active_conference_with_metadata` interceptor runs after the
        `post_connect_active_conference` interceptor. The (possibly modified) response returned by
        `post_connect_active_conference` will be passed to
        `post_connect_active_conference_with_metadata`.
        """
        return response, metadata

    def pre_create_member(
        self,
        request: service.CreateMemberRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.CreateMemberRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_member

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SpacesService server.
        """
        return request, metadata

    def post_create_member(self, response: resource.Member) -> resource.Member:
        """Post-rpc interceptor for create_member

        DEPRECATED. Please use the `post_create_member_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SpacesService server but before
        it is returned to user code. This `post_create_member` interceptor runs
        before the `post_create_member_with_metadata` interceptor.
        """
        return response

    def post_create_member_with_metadata(
        self,
        response: resource.Member,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resource.Member, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_member

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SpacesService server but before it is returned to user code.

        We recommend only using this `post_create_member_with_metadata`
        interceptor in new development instead of the `post_create_member` interceptor.
        When both interceptors are used, this `post_create_member_with_metadata` interceptor runs after the
        `post_create_member` interceptor. The (possibly modified) response returned by
        `post_create_member` will be passed to
        `post_create_member_with_metadata`.
        """
        return response, metadata

    def pre_create_space(
        self,
        request: service.CreateSpaceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.CreateSpaceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_space

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SpacesService server.
        """
        return request, metadata

    def post_create_space(self, response: resource.Space) -> resource.Space:
        """Post-rpc interceptor for create_space

        DEPRECATED. Please use the `post_create_space_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SpacesService server but before
        it is returned to user code. This `post_create_space` interceptor runs
        before the `post_create_space_with_metadata` interceptor.
        """
        return response

    def post_create_space_with_metadata(
        self,
        response: resource.Space,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resource.Space, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_space

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SpacesService server but before it is returned to user code.

        We recommend only using this `post_create_space_with_metadata`
        interceptor in new development instead of the `post_create_space` interceptor.
        When both interceptors are used, this `post_create_space_with_metadata` interceptor runs after the
        `post_create_space` interceptor. The (possibly modified) response returned by
        `post_create_space` will be passed to
        `post_create_space_with_metadata`.
        """
        return response, metadata

    def pre_delete_member(
        self,
        request: service.DeleteMemberRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.DeleteMemberRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_member

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SpacesService server.
        """
        return request, metadata

    def pre_end_active_conference(
        self,
        request: service.EndActiveConferenceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.EndActiveConferenceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for end_active_conference

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SpacesService server.
        """
        return request, metadata

    def pre_get_member(
        self,
        request: service.GetMemberRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetMemberRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_member

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SpacesService server.
        """
        return request, metadata

    def post_get_member(self, response: resource.Member) -> resource.Member:
        """Post-rpc interceptor for get_member

        DEPRECATED. Please use the `post_get_member_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SpacesService server but before
        it is returned to user code. This `post_get_member` interceptor runs
        before the `post_get_member_with_metadata` interceptor.
        """
        return response

    def post_get_member_with_metadata(
        self,
        response: resource.Member,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resource.Member, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_member

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SpacesService server but before it is returned to user code.

        We recommend only using this `post_get_member_with_metadata`
        interceptor in new development instead of the `post_get_member` interceptor.
        When both interceptors are used, this `post_get_member_with_metadata` interceptor runs after the
        `post_get_member` interceptor. The (possibly modified) response returned by
        `post_get_member` will be passed to
        `post_get_member_with_metadata`.
        """
        return response, metadata

    def pre_get_space(
        self,
        request: service.GetSpaceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetSpaceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_space

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SpacesService server.
        """
        return request, metadata

    def post_get_space(self, response: resource.Space) -> resource.Space:
        """Post-rpc interceptor for get_space

        DEPRECATED. Please use the `post_get_space_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SpacesService server but before
        it is returned to user code. This `post_get_space` interceptor runs
        before the `post_get_space_with_metadata` interceptor.
        """
        return response

    def post_get_space_with_metadata(
        self,
        response: resource.Space,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resource.Space, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_space

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SpacesService server but before it is returned to user code.

        We recommend only using this `post_get_space_with_metadata`
        interceptor in new development instead of the `post_get_space` interceptor.
        When both interceptors are used, this `post_get_space_with_metadata` interceptor runs after the
        `post_get_space` interceptor. The (possibly modified) response returned by
        `post_get_space` will be passed to
        `post_get_space_with_metadata`.
        """
        return response, metadata

    def pre_list_members(
        self,
        request: service.ListMembersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListMembersRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_members

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SpacesService server.
        """
        return request, metadata

    def post_list_members(
        self, response: service.ListMembersResponse
    ) -> service.ListMembersResponse:
        """Post-rpc interceptor for list_members

        DEPRECATED. Please use the `post_list_members_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SpacesService server but before
        it is returned to user code. This `post_list_members` interceptor runs
        before the `post_list_members_with_metadata` interceptor.
        """
        return response

    def post_list_members_with_metadata(
        self,
        response: service.ListMembersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListMembersResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_members

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SpacesService server but before it is returned to user code.

        We recommend only using this `post_list_members_with_metadata`
        interceptor in new development instead of the `post_list_members` interceptor.
        When both interceptors are used, this `post_list_members_with_metadata` interceptor runs after the
        `post_list_members` interceptor. The (possibly modified) response returned by
        `post_list_members` will be passed to
        `post_list_members_with_metadata`.
        """
        return response, metadata

    def pre_update_member(
        self,
        request: service.UpdateMemberRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.UpdateMemberRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_member

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SpacesService server.
        """
        return request, metadata

    def post_update_member(self, response: resource.Member) -> resource.Member:
        """Post-rpc interceptor for update_member

        DEPRECATED. Please use the `post_update_member_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SpacesService server but before
        it is returned to user code. This `post_update_member` interceptor runs
        before the `post_update_member_with_metadata` interceptor.
        """
        return response

    def post_update_member_with_metadata(
        self,
        response: resource.Member,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resource.Member, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_member

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SpacesService server but before it is returned to user code.

        We recommend only using this `post_update_member_with_metadata`
        interceptor in new development instead of the `post_update_member` interceptor.
        When both interceptors are used, this `post_update_member_with_metadata` interceptor runs after the
        `post_update_member` interceptor. The (possibly modified) response returned by
        `post_update_member` will be passed to
        `post_update_member_with_metadata`.
        """
        return response, metadata

    def pre_update_space(
        self,
        request: service.UpdateSpaceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.UpdateSpaceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_space

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SpacesService server.
        """
        return request, metadata

    def post_update_space(self, response: resource.Space) -> resource.Space:
        """Post-rpc interceptor for update_space

        DEPRECATED. Please use the `post_update_space_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SpacesService server but before
        it is returned to user code. This `post_update_space` interceptor runs
        before the `post_update_space_with_metadata` interceptor.
        """
        return response

    def post_update_space_with_metadata(
        self,
        response: resource.Space,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resource.Space, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_space

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SpacesService server but before it is returned to user code.

        We recommend only using this `post_update_space_with_metadata`
        interceptor in new development instead of the `post_update_space` interceptor.
        When both interceptors are used, this `post_update_space_with_metadata` interceptor runs after the
        `post_update_space` interceptor. The (possibly modified) response returned by
        `post_update_space` will be passed to
        `post_update_space_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class SpacesServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: SpacesServiceRestInterceptor


class SpacesServiceRestTransport(_BaseSpacesServiceRestTransport):
    """REST backend synchronous transport for SpacesService.

    REST API for services dealing with spaces.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "meet.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[SpacesServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'meet.googleapis.com').
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
            interceptor (Optional[SpacesServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or SpacesServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchUpdateMembers(
        _BaseSpacesServiceRestTransport._BaseBatchUpdateMembers, SpacesServiceRestStub
    ):
        def __hash__(self):
            return hash("SpacesServiceRestTransport.BatchUpdateMembers")

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
            request: service.BatchUpdateMembersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.BatchUpdateMembersResponse:
            r"""Call the batch update members method over HTTP.

            Args:
                request (~.service.BatchUpdateMembersRequest):
                    The request object. Request to update members of one
                space within a batch.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.BatchUpdateMembersResponse:
                    Response of batch update members.
            """

            http_options = _BaseSpacesServiceRestTransport._BaseBatchUpdateMembers._get_http_options()
            request, metadata = self._interceptor.pre_batch_update_members(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSpacesServiceRestTransport._BaseBatchUpdateMembers,
                    "_BaseBatchUpdateMembers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.apps.meet_v2beta.SpacesServiceClient.BatchUpdateMembers",
                    extra={
                        "serviceName": "google.apps.meet.v2beta.SpacesService",
                        "rpcName": "BatchUpdateMembers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SpacesServiceRestTransport._BatchUpdateMembers._get_response(
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
            resp = service.BatchUpdateMembersResponse()
            pb_resp = service.BatchUpdateMembersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_members(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_update_members_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.BatchUpdateMembersResponse.to_json(
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
                    "Received response for google.apps.meet_v2beta.SpacesServiceClient.batch_update_members",
                    extra={
                        "serviceName": "google.apps.meet.v2beta.SpacesService",
                        "rpcName": "BatchUpdateMembers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ConnectActiveConference(
        _BaseSpacesServiceRestTransport._BaseConnectActiveConference,
        SpacesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SpacesServiceRestTransport.ConnectActiveConference")

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
            request: service.ConnectActiveConferenceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ConnectActiveConferenceResponse:
            r"""Call the connect active conference method over HTTP.

            Args:
                request (~.service.ConnectActiveConferenceRequest):
                    The request object. Request to establish a WebRTC
                connection to the active conference of a
                space.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ConnectActiveConferenceResponse:
                    Response of ConnectActiveConference method.

                A success response does not indicate the meeting is
                fully joined; further communication must occur across
                WebRTC.

                See `Meet Media API
                overview <https://developers.google.com/workspace/meet/media-api/guides/overview>`__
                for more details about this connection.

            """

            http_options = _BaseSpacesServiceRestTransport._BaseConnectActiveConference._get_http_options()
            request, metadata = self._interceptor.pre_connect_active_conference(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSpacesServiceRestTransport._BaseConnectActiveConference,
                    "_BaseConnectActiveConference__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.apps.meet_v2beta.SpacesServiceClient.ConnectActiveConference",
                    extra={
                        "serviceName": "google.apps.meet.v2beta.SpacesService",
                        "rpcName": "ConnectActiveConference",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SpacesServiceRestTransport._ConnectActiveConference._get_response(
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
            resp = service.ConnectActiveConferenceResponse()
            pb_resp = service.ConnectActiveConferenceResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_connect_active_conference(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_connect_active_conference_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ConnectActiveConferenceResponse.to_json(
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
                    "Received response for google.apps.meet_v2beta.SpacesServiceClient.connect_active_conference",
                    extra={
                        "serviceName": "google.apps.meet.v2beta.SpacesService",
                        "rpcName": "ConnectActiveConference",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateMember(
        _BaseSpacesServiceRestTransport._BaseCreateMember, SpacesServiceRestStub
    ):
        def __hash__(self):
            return hash("SpacesServiceRestTransport.CreateMember")

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
            request: service.CreateMemberRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resource.Member:
            r"""Call the create member method over HTTP.

            Args:
                request (~.service.CreateMemberRequest):
                    The request object. Request to create a member for a
                space.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resource.Member:
                    Users who are configured to have a
                role in the space. These users can join
                the space without knocking.

            """

            http_options = (
                _BaseSpacesServiceRestTransport._BaseCreateMember._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_member(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSpacesServiceRestTransport._BaseCreateMember,
                    "_BaseCreateMember__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.apps.meet_v2beta.SpacesServiceClient.CreateMember",
                    extra={
                        "serviceName": "google.apps.meet.v2beta.SpacesService",
                        "rpcName": "CreateMember",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SpacesServiceRestTransport._CreateMember._get_response(
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
            resp = resource.Member()
            pb_resp = resource.Member.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_member(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_member_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resource.Member.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.apps.meet_v2beta.SpacesServiceClient.create_member",
                    extra={
                        "serviceName": "google.apps.meet.v2beta.SpacesService",
                        "rpcName": "CreateMember",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateSpace(
        _BaseSpacesServiceRestTransport._BaseCreateSpace, SpacesServiceRestStub
    ):
        def __hash__(self):
            return hash("SpacesServiceRestTransport.CreateSpace")

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
            request: service.CreateSpaceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resource.Space:
            r"""Call the create space method over HTTP.

            Args:
                request (~.service.CreateSpaceRequest):
                    The request object. Request to create a space.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resource.Space:
                    Virtual place where conferences are
                held. Only one active conference can be
                held in one space at any given time.

            """

            http_options = (
                _BaseSpacesServiceRestTransport._BaseCreateSpace._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_space(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSpacesServiceRestTransport._BaseCreateSpace,
                    "_BaseCreateSpace__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.apps.meet_v2beta.SpacesServiceClient.CreateSpace",
                    extra={
                        "serviceName": "google.apps.meet.v2beta.SpacesService",
                        "rpcName": "CreateSpace",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SpacesServiceRestTransport._CreateSpace._get_response(
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
            resp = resource.Space()
            pb_resp = resource.Space.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_space(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_space_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resource.Space.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.apps.meet_v2beta.SpacesServiceClient.create_space",
                    extra={
                        "serviceName": "google.apps.meet.v2beta.SpacesService",
                        "rpcName": "CreateSpace",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteMember(
        _BaseSpacesServiceRestTransport._BaseDeleteMember, SpacesServiceRestStub
    ):
        def __hash__(self):
            return hash("SpacesServiceRestTransport.DeleteMember")

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
            request: service.DeleteMemberRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete member method over HTTP.

            Args:
                request (~.service.DeleteMemberRequest):
                    The request object. Request to delete a member from a
                space.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseSpacesServiceRestTransport._BaseDeleteMember._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_member(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSpacesServiceRestTransport._BaseDeleteMember,
                    "_BaseDeleteMember__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.apps.meet_v2beta.SpacesServiceClient.DeleteMember",
                    extra={
                        "serviceName": "google.apps.meet.v2beta.SpacesService",
                        "rpcName": "DeleteMember",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SpacesServiceRestTransport._DeleteMember._get_response(
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

    class _EndActiveConference(
        _BaseSpacesServiceRestTransport._BaseEndActiveConference, SpacesServiceRestStub
    ):
        def __hash__(self):
            return hash("SpacesServiceRestTransport.EndActiveConference")

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
            request: service.EndActiveConferenceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the end active conference method over HTTP.

            Args:
                request (~.service.EndActiveConferenceRequest):
                    The request object. Request to end an ongoing conference
                of a space.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseSpacesServiceRestTransport._BaseEndActiveConference._get_http_options()
            request, metadata = self._interceptor.pre_end_active_conference(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSpacesServiceRestTransport._BaseEndActiveConference,
                    "_BaseEndActiveConference__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.apps.meet_v2beta.SpacesServiceClient.EndActiveConference",
                    extra={
                        "serviceName": "google.apps.meet.v2beta.SpacesService",
                        "rpcName": "EndActiveConference",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SpacesServiceRestTransport._EndActiveConference._get_response(
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

    class _GetMember(
        _BaseSpacesServiceRestTransport._BaseGetMember, SpacesServiceRestStub
    ):
        def __hash__(self):
            return hash("SpacesServiceRestTransport.GetMember")

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
            request: service.GetMemberRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resource.Member:
            r"""Call the get member method over HTTP.

            Args:
                request (~.service.GetMemberRequest):
                    The request object. Request to get a member from a space.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resource.Member:
                    Users who are configured to have a
                role in the space. These users can join
                the space without knocking.

            """

            http_options = (
                _BaseSpacesServiceRestTransport._BaseGetMember._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_member(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSpacesServiceRestTransport._BaseGetMember,
                    "_BaseGetMember__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.apps.meet_v2beta.SpacesServiceClient.GetMember",
                    extra={
                        "serviceName": "google.apps.meet.v2beta.SpacesService",
                        "rpcName": "GetMember",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SpacesServiceRestTransport._GetMember._get_response(
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
            resp = resource.Member()
            pb_resp = resource.Member.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_member(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_member_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resource.Member.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.apps.meet_v2beta.SpacesServiceClient.get_member",
                    extra={
                        "serviceName": "google.apps.meet.v2beta.SpacesService",
                        "rpcName": "GetMember",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSpace(
        _BaseSpacesServiceRestTransport._BaseGetSpace, SpacesServiceRestStub
    ):
        def __hash__(self):
            return hash("SpacesServiceRestTransport.GetSpace")

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
            request: service.GetSpaceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resource.Space:
            r"""Call the get space method over HTTP.

            Args:
                request (~.service.GetSpaceRequest):
                    The request object. Request to get a space.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resource.Space:
                    Virtual place where conferences are
                held. Only one active conference can be
                held in one space at any given time.

            """

            http_options = (
                _BaseSpacesServiceRestTransport._BaseGetSpace._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_space(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSpacesServiceRestTransport._BaseGetSpace,
                    "_BaseGetSpace__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.apps.meet_v2beta.SpacesServiceClient.GetSpace",
                    extra={
                        "serviceName": "google.apps.meet.v2beta.SpacesService",
                        "rpcName": "GetSpace",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SpacesServiceRestTransport._GetSpace._get_response(
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
            resp = resource.Space()
            pb_resp = resource.Space.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_space(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_space_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resource.Space.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.apps.meet_v2beta.SpacesServiceClient.get_space",
                    extra={
                        "serviceName": "google.apps.meet.v2beta.SpacesService",
                        "rpcName": "GetSpace",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListMembers(
        _BaseSpacesServiceRestTransport._BaseListMembers, SpacesServiceRestStub
    ):
        def __hash__(self):
            return hash("SpacesServiceRestTransport.ListMembers")

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
            request: service.ListMembersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListMembersResponse:
            r"""Call the list members method over HTTP.

            Args:
                request (~.service.ListMembersRequest):
                    The request object. Request to list all members of a
                space.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListMembersResponse:
                    Response of list members.
            """

            http_options = (
                _BaseSpacesServiceRestTransport._BaseListMembers._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_members(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSpacesServiceRestTransport._BaseListMembers,
                    "_BaseListMembers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.apps.meet_v2beta.SpacesServiceClient.ListMembers",
                    extra={
                        "serviceName": "google.apps.meet.v2beta.SpacesService",
                        "rpcName": "ListMembers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SpacesServiceRestTransport._ListMembers._get_response(
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
            resp = service.ListMembersResponse()
            pb_resp = service.ListMembersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_members(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_members_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListMembersResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.apps.meet_v2beta.SpacesServiceClient.list_members",
                    extra={
                        "serviceName": "google.apps.meet.v2beta.SpacesService",
                        "rpcName": "ListMembers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateMember(
        _BaseSpacesServiceRestTransport._BaseUpdateMember, SpacesServiceRestStub
    ):
        def __hash__(self):
            return hash("SpacesServiceRestTransport.UpdateMember")

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
            request: service.UpdateMemberRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resource.Member:
            r"""Call the update member method over HTTP.

            Args:
                request (~.service.UpdateMemberRequest):
                    The request object. Request to update a member.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resource.Member:
                    Users who are configured to have a
                role in the space. These users can join
                the space without knocking.

            """

            http_options = (
                _BaseSpacesServiceRestTransport._BaseUpdateMember._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_member(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSpacesServiceRestTransport._BaseUpdateMember,
                    "_BaseUpdateMember__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.apps.meet_v2beta.SpacesServiceClient.UpdateMember",
                    extra={
                        "serviceName": "google.apps.meet.v2beta.SpacesService",
                        "rpcName": "UpdateMember",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SpacesServiceRestTransport._UpdateMember._get_response(
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
            resp = resource.Member()
            pb_resp = resource.Member.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_member(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_member_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resource.Member.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.apps.meet_v2beta.SpacesServiceClient.update_member",
                    extra={
                        "serviceName": "google.apps.meet.v2beta.SpacesService",
                        "rpcName": "UpdateMember",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateSpace(
        _BaseSpacesServiceRestTransport._BaseUpdateSpace, SpacesServiceRestStub
    ):
        def __hash__(self):
            return hash("SpacesServiceRestTransport.UpdateSpace")

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
            request: service.UpdateSpaceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resource.Space:
            r"""Call the update space method over HTTP.

            Args:
                request (~.service.UpdateSpaceRequest):
                    The request object. Request to update a space.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resource.Space:
                    Virtual place where conferences are
                held. Only one active conference can be
                held in one space at any given time.

            """

            http_options = (
                _BaseSpacesServiceRestTransport._BaseUpdateSpace._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_space(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSpacesServiceRestTransport._BaseUpdateSpace,
                    "_BaseUpdateSpace__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.apps.meet_v2beta.SpacesServiceClient.UpdateSpace",
                    extra={
                        "serviceName": "google.apps.meet.v2beta.SpacesService",
                        "rpcName": "UpdateSpace",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SpacesServiceRestTransport._UpdateSpace._get_response(
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
            resp = resource.Space()
            pb_resp = resource.Space.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_space(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_space_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resource.Space.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.apps.meet_v2beta.SpacesServiceClient.update_space",
                    extra={
                        "serviceName": "google.apps.meet.v2beta.SpacesService",
                        "rpcName": "UpdateSpace",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_update_members(
        self,
    ) -> Callable[
        [service.BatchUpdateMembersRequest], service.BatchUpdateMembersResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdateMembers(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def connect_active_conference(
        self,
    ) -> Callable[
        [service.ConnectActiveConferenceRequest],
        service.ConnectActiveConferenceResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ConnectActiveConference(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_member(self) -> Callable[[service.CreateMemberRequest], resource.Member]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateMember(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_space(self) -> Callable[[service.CreateSpaceRequest], resource.Space]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateSpace(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_member(self) -> Callable[[service.DeleteMemberRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteMember(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def end_active_conference(
        self,
    ) -> Callable[[service.EndActiveConferenceRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._EndActiveConference(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_member(self) -> Callable[[service.GetMemberRequest], resource.Member]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetMember(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_space(self) -> Callable[[service.GetSpaceRequest], resource.Space]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSpace(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_members(
        self,
    ) -> Callable[[service.ListMembersRequest], service.ListMembersResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListMembers(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_member(self) -> Callable[[service.UpdateMemberRequest], resource.Member]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateMember(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_space(self) -> Callable[[service.UpdateSpaceRequest], resource.Space]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateSpace(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("SpacesServiceRestTransport",)
