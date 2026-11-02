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

from google.cloud.saasplatform_saasservicemgmt_v1beta1._compat import transcode_request
from google.cloud.saasplatform_saasservicemgmt_v1beta1.types import (
    rollouts_resources,
    rollouts_service,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseSaasRolloutsRestTransport

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


class SaasRolloutsRestInterceptor:
    """Interceptor for SaasRollouts.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the SaasRolloutsRestTransport.

    .. code-block:: python
        class MyCustomSaasRolloutsInterceptor(SaasRolloutsRestInterceptor):
            def pre_create_rollout(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_rollout(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_rollout_kind(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_rollout_kind(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_rollout(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_rollout_kind(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_rollout(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_rollout(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_rollout_kind(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_rollout_kind(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_rollout_kinds(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_rollout_kinds(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_rollouts(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_rollouts(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_rollout(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_rollout(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_rollout_kind(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_rollout_kind(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = SaasRolloutsRestTransport(interceptor=MyCustomSaasRolloutsInterceptor())
        client = SaasRolloutsClient(transport=transport)


    """

    def pre_create_rollout(
        self,
        request: rollouts_service.CreateRolloutRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        rollouts_service.CreateRolloutRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_rollout

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasRollouts server.
        """
        return request, metadata

    def post_create_rollout(
        self, response: rollouts_resources.Rollout
    ) -> rollouts_resources.Rollout:
        """Post-rpc interceptor for create_rollout

        DEPRECATED. Please use the `post_create_rollout_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SaasRollouts server but before
        it is returned to user code. This `post_create_rollout` interceptor runs
        before the `post_create_rollout_with_metadata` interceptor.
        """
        return response

    def post_create_rollout_with_metadata(
        self,
        response: rollouts_resources.Rollout,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[rollouts_resources.Rollout, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_rollout

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SaasRollouts server but before it is returned to user code.

        We recommend only using this `post_create_rollout_with_metadata`
        interceptor in new development instead of the `post_create_rollout` interceptor.
        When both interceptors are used, this `post_create_rollout_with_metadata` interceptor runs after the
        `post_create_rollout` interceptor. The (possibly modified) response returned by
        `post_create_rollout` will be passed to
        `post_create_rollout_with_metadata`.
        """
        return response, metadata

    def pre_create_rollout_kind(
        self,
        request: rollouts_service.CreateRolloutKindRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        rollouts_service.CreateRolloutKindRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_rollout_kind

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasRollouts server.
        """
        return request, metadata

    def post_create_rollout_kind(
        self, response: rollouts_resources.RolloutKind
    ) -> rollouts_resources.RolloutKind:
        """Post-rpc interceptor for create_rollout_kind

        DEPRECATED. Please use the `post_create_rollout_kind_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SaasRollouts server but before
        it is returned to user code. This `post_create_rollout_kind` interceptor runs
        before the `post_create_rollout_kind_with_metadata` interceptor.
        """
        return response

    def post_create_rollout_kind_with_metadata(
        self,
        response: rollouts_resources.RolloutKind,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[rollouts_resources.RolloutKind, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_rollout_kind

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SaasRollouts server but before it is returned to user code.

        We recommend only using this `post_create_rollout_kind_with_metadata`
        interceptor in new development instead of the `post_create_rollout_kind` interceptor.
        When both interceptors are used, this `post_create_rollout_kind_with_metadata` interceptor runs after the
        `post_create_rollout_kind` interceptor. The (possibly modified) response returned by
        `post_create_rollout_kind` will be passed to
        `post_create_rollout_kind_with_metadata`.
        """
        return response, metadata

    def pre_delete_rollout(
        self,
        request: rollouts_service.DeleteRolloutRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        rollouts_service.DeleteRolloutRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_rollout

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasRollouts server.
        """
        return request, metadata

    def pre_delete_rollout_kind(
        self,
        request: rollouts_service.DeleteRolloutKindRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        rollouts_service.DeleteRolloutKindRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_rollout_kind

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasRollouts server.
        """
        return request, metadata

    def pre_get_rollout(
        self,
        request: rollouts_service.GetRolloutRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        rollouts_service.GetRolloutRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_rollout

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasRollouts server.
        """
        return request, metadata

    def post_get_rollout(
        self, response: rollouts_resources.Rollout
    ) -> rollouts_resources.Rollout:
        """Post-rpc interceptor for get_rollout

        DEPRECATED. Please use the `post_get_rollout_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SaasRollouts server but before
        it is returned to user code. This `post_get_rollout` interceptor runs
        before the `post_get_rollout_with_metadata` interceptor.
        """
        return response

    def post_get_rollout_with_metadata(
        self,
        response: rollouts_resources.Rollout,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[rollouts_resources.Rollout, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_rollout

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SaasRollouts server but before it is returned to user code.

        We recommend only using this `post_get_rollout_with_metadata`
        interceptor in new development instead of the `post_get_rollout` interceptor.
        When both interceptors are used, this `post_get_rollout_with_metadata` interceptor runs after the
        `post_get_rollout` interceptor. The (possibly modified) response returned by
        `post_get_rollout` will be passed to
        `post_get_rollout_with_metadata`.
        """
        return response, metadata

    def pre_get_rollout_kind(
        self,
        request: rollouts_service.GetRolloutKindRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        rollouts_service.GetRolloutKindRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_rollout_kind

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasRollouts server.
        """
        return request, metadata

    def post_get_rollout_kind(
        self, response: rollouts_resources.RolloutKind
    ) -> rollouts_resources.RolloutKind:
        """Post-rpc interceptor for get_rollout_kind

        DEPRECATED. Please use the `post_get_rollout_kind_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SaasRollouts server but before
        it is returned to user code. This `post_get_rollout_kind` interceptor runs
        before the `post_get_rollout_kind_with_metadata` interceptor.
        """
        return response

    def post_get_rollout_kind_with_metadata(
        self,
        response: rollouts_resources.RolloutKind,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[rollouts_resources.RolloutKind, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_rollout_kind

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SaasRollouts server but before it is returned to user code.

        We recommend only using this `post_get_rollout_kind_with_metadata`
        interceptor in new development instead of the `post_get_rollout_kind` interceptor.
        When both interceptors are used, this `post_get_rollout_kind_with_metadata` interceptor runs after the
        `post_get_rollout_kind` interceptor. The (possibly modified) response returned by
        `post_get_rollout_kind` will be passed to
        `post_get_rollout_kind_with_metadata`.
        """
        return response, metadata

    def pre_list_rollout_kinds(
        self,
        request: rollouts_service.ListRolloutKindsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        rollouts_service.ListRolloutKindsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_rollout_kinds

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasRollouts server.
        """
        return request, metadata

    def post_list_rollout_kinds(
        self, response: rollouts_service.ListRolloutKindsResponse
    ) -> rollouts_service.ListRolloutKindsResponse:
        """Post-rpc interceptor for list_rollout_kinds

        DEPRECATED. Please use the `post_list_rollout_kinds_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SaasRollouts server but before
        it is returned to user code. This `post_list_rollout_kinds` interceptor runs
        before the `post_list_rollout_kinds_with_metadata` interceptor.
        """
        return response

    def post_list_rollout_kinds_with_metadata(
        self,
        response: rollouts_service.ListRolloutKindsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        rollouts_service.ListRolloutKindsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_rollout_kinds

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SaasRollouts server but before it is returned to user code.

        We recommend only using this `post_list_rollout_kinds_with_metadata`
        interceptor in new development instead of the `post_list_rollout_kinds` interceptor.
        When both interceptors are used, this `post_list_rollout_kinds_with_metadata` interceptor runs after the
        `post_list_rollout_kinds` interceptor. The (possibly modified) response returned by
        `post_list_rollout_kinds` will be passed to
        `post_list_rollout_kinds_with_metadata`.
        """
        return response, metadata

    def pre_list_rollouts(
        self,
        request: rollouts_service.ListRolloutsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        rollouts_service.ListRolloutsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_rollouts

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasRollouts server.
        """
        return request, metadata

    def post_list_rollouts(
        self, response: rollouts_service.ListRolloutsResponse
    ) -> rollouts_service.ListRolloutsResponse:
        """Post-rpc interceptor for list_rollouts

        DEPRECATED. Please use the `post_list_rollouts_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SaasRollouts server but before
        it is returned to user code. This `post_list_rollouts` interceptor runs
        before the `post_list_rollouts_with_metadata` interceptor.
        """
        return response

    def post_list_rollouts_with_metadata(
        self,
        response: rollouts_service.ListRolloutsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        rollouts_service.ListRolloutsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_rollouts

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SaasRollouts server but before it is returned to user code.

        We recommend only using this `post_list_rollouts_with_metadata`
        interceptor in new development instead of the `post_list_rollouts` interceptor.
        When both interceptors are used, this `post_list_rollouts_with_metadata` interceptor runs after the
        `post_list_rollouts` interceptor. The (possibly modified) response returned by
        `post_list_rollouts` will be passed to
        `post_list_rollouts_with_metadata`.
        """
        return response, metadata

    def pre_update_rollout(
        self,
        request: rollouts_service.UpdateRolloutRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        rollouts_service.UpdateRolloutRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_rollout

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasRollouts server.
        """
        return request, metadata

    def post_update_rollout(
        self, response: rollouts_resources.Rollout
    ) -> rollouts_resources.Rollout:
        """Post-rpc interceptor for update_rollout

        DEPRECATED. Please use the `post_update_rollout_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SaasRollouts server but before
        it is returned to user code. This `post_update_rollout` interceptor runs
        before the `post_update_rollout_with_metadata` interceptor.
        """
        return response

    def post_update_rollout_with_metadata(
        self,
        response: rollouts_resources.Rollout,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[rollouts_resources.Rollout, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_rollout

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SaasRollouts server but before it is returned to user code.

        We recommend only using this `post_update_rollout_with_metadata`
        interceptor in new development instead of the `post_update_rollout` interceptor.
        When both interceptors are used, this `post_update_rollout_with_metadata` interceptor runs after the
        `post_update_rollout` interceptor. The (possibly modified) response returned by
        `post_update_rollout` will be passed to
        `post_update_rollout_with_metadata`.
        """
        return response, metadata

    def pre_update_rollout_kind(
        self,
        request: rollouts_service.UpdateRolloutKindRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        rollouts_service.UpdateRolloutKindRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_rollout_kind

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SaasRollouts server.
        """
        return request, metadata

    def post_update_rollout_kind(
        self, response: rollouts_resources.RolloutKind
    ) -> rollouts_resources.RolloutKind:
        """Post-rpc interceptor for update_rollout_kind

        DEPRECATED. Please use the `post_update_rollout_kind_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SaasRollouts server but before
        it is returned to user code. This `post_update_rollout_kind` interceptor runs
        before the `post_update_rollout_kind_with_metadata` interceptor.
        """
        return response

    def post_update_rollout_kind_with_metadata(
        self,
        response: rollouts_resources.RolloutKind,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[rollouts_resources.RolloutKind, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_rollout_kind

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SaasRollouts server but before it is returned to user code.

        We recommend only using this `post_update_rollout_kind_with_metadata`
        interceptor in new development instead of the `post_update_rollout_kind` interceptor.
        When both interceptors are used, this `post_update_rollout_kind_with_metadata` interceptor runs after the
        `post_update_rollout_kind` interceptor. The (possibly modified) response returned by
        `post_update_rollout_kind` will be passed to
        `post_update_rollout_kind_with_metadata`.
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
        before they are sent to the SaasRollouts server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the SaasRollouts server but before
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
        before they are sent to the SaasRollouts server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the SaasRollouts server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class SaasRolloutsRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: SaasRolloutsRestInterceptor


class SaasRolloutsRestTransport(_BaseSaasRolloutsRestTransport):
    """REST backend synchronous transport for SaasRollouts.

    Manages the rollout of SaaS services.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "saasservicemgmt.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[SaasRolloutsRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'saasservicemgmt.googleapis.com').
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
            interceptor (Optional[SaasRolloutsRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or SaasRolloutsRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateRollout(
        _BaseSaasRolloutsRestTransport._BaseCreateRollout, SaasRolloutsRestStub
    ):
        def __hash__(self):
            return hash("SaasRolloutsRestTransport.CreateRollout")

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
            request: rollouts_service.CreateRolloutRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> rollouts_resources.Rollout:
            r"""Call the create rollout method over HTTP.

            Args:
                request (~.rollouts_service.CreateRolloutRequest):
                    The request object. The request structure for the
                CreateRollout method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.rollouts_resources.Rollout:
                    Represents a single rollout execution
                and its results

            """

            http_options = (
                _BaseSaasRolloutsRestTransport._BaseCreateRollout._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_rollout(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasRolloutsRestTransport._BaseCreateRollout,
                    "_BaseCreateRollout__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasRolloutsClient.CreateRollout",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts",
                        "rpcName": "CreateRollout",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasRolloutsRestTransport._CreateRollout._get_response(
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
            resp = rollouts_resources.Rollout()
            pb_resp = rollouts_resources.Rollout.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_rollout(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_rollout_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = rollouts_resources.Rollout.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasRolloutsClient.create_rollout",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts",
                        "rpcName": "CreateRollout",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateRolloutKind(
        _BaseSaasRolloutsRestTransport._BaseCreateRolloutKind, SaasRolloutsRestStub
    ):
        def __hash__(self):
            return hash("SaasRolloutsRestTransport.CreateRolloutKind")

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
            request: rollouts_service.CreateRolloutKindRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> rollouts_resources.RolloutKind:
            r"""Call the create rollout kind method over HTTP.

            Args:
                request (~.rollouts_service.CreateRolloutKindRequest):
                    The request object. The request structure for the
                CreateRolloutKind method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.rollouts_resources.RolloutKind:
                    An object that describes various
                settings of Rollout execution. Includes
                built-in policies across GCP and GDC,
                and customizable policies.

            """

            http_options = _BaseSaasRolloutsRestTransport._BaseCreateRolloutKind._get_http_options()
            request, metadata = self._interceptor.pre_create_rollout_kind(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasRolloutsRestTransport._BaseCreateRolloutKind,
                    "_BaseCreateRolloutKind__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasRolloutsClient.CreateRolloutKind",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts",
                        "rpcName": "CreateRolloutKind",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasRolloutsRestTransport._CreateRolloutKind._get_response(
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
            resp = rollouts_resources.RolloutKind()
            pb_resp = rollouts_resources.RolloutKind.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_rollout_kind(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_rollout_kind_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = rollouts_resources.RolloutKind.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasRolloutsClient.create_rollout_kind",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts",
                        "rpcName": "CreateRolloutKind",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteRollout(
        _BaseSaasRolloutsRestTransport._BaseDeleteRollout, SaasRolloutsRestStub
    ):
        def __hash__(self):
            return hash("SaasRolloutsRestTransport.DeleteRollout")

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
            request: rollouts_service.DeleteRolloutRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete rollout method over HTTP.

            Args:
                request (~.rollouts_service.DeleteRolloutRequest):
                    The request object. The request structure for the
                DeleteRollout method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseSaasRolloutsRestTransport._BaseDeleteRollout._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_rollout(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasRolloutsRestTransport._BaseDeleteRollout,
                    "_BaseDeleteRollout__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasRolloutsClient.DeleteRollout",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts",
                        "rpcName": "DeleteRollout",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasRolloutsRestTransport._DeleteRollout._get_response(
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

    class _DeleteRolloutKind(
        _BaseSaasRolloutsRestTransport._BaseDeleteRolloutKind, SaasRolloutsRestStub
    ):
        def __hash__(self):
            return hash("SaasRolloutsRestTransport.DeleteRolloutKind")

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
            request: rollouts_service.DeleteRolloutKindRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete rollout kind method over HTTP.

            Args:
                request (~.rollouts_service.DeleteRolloutKindRequest):
                    The request object. The request structure for the
                DeleteRolloutKind method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseSaasRolloutsRestTransport._BaseDeleteRolloutKind._get_http_options()
            request, metadata = self._interceptor.pre_delete_rollout_kind(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasRolloutsRestTransport._BaseDeleteRolloutKind,
                    "_BaseDeleteRolloutKind__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasRolloutsClient.DeleteRolloutKind",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts",
                        "rpcName": "DeleteRolloutKind",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasRolloutsRestTransport._DeleteRolloutKind._get_response(
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

    class _GetRollout(
        _BaseSaasRolloutsRestTransport._BaseGetRollout, SaasRolloutsRestStub
    ):
        def __hash__(self):
            return hash("SaasRolloutsRestTransport.GetRollout")

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
            request: rollouts_service.GetRolloutRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> rollouts_resources.Rollout:
            r"""Call the get rollout method over HTTP.

            Args:
                request (~.rollouts_service.GetRolloutRequest):
                    The request object. The request structure for the
                GetRollout method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.rollouts_resources.Rollout:
                    Represents a single rollout execution
                and its results

            """

            http_options = (
                _BaseSaasRolloutsRestTransport._BaseGetRollout._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_rollout(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasRolloutsRestTransport._BaseGetRollout,
                    "_BaseGetRollout__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasRolloutsClient.GetRollout",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts",
                        "rpcName": "GetRollout",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasRolloutsRestTransport._GetRollout._get_response(
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
            resp = rollouts_resources.Rollout()
            pb_resp = rollouts_resources.Rollout.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_rollout(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_rollout_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = rollouts_resources.Rollout.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasRolloutsClient.get_rollout",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts",
                        "rpcName": "GetRollout",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetRolloutKind(
        _BaseSaasRolloutsRestTransport._BaseGetRolloutKind, SaasRolloutsRestStub
    ):
        def __hash__(self):
            return hash("SaasRolloutsRestTransport.GetRolloutKind")

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
            request: rollouts_service.GetRolloutKindRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> rollouts_resources.RolloutKind:
            r"""Call the get rollout kind method over HTTP.

            Args:
                request (~.rollouts_service.GetRolloutKindRequest):
                    The request object. The request structure for the
                GetRolloutKind method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.rollouts_resources.RolloutKind:
                    An object that describes various
                settings of Rollout execution. Includes
                built-in policies across GCP and GDC,
                and customizable policies.

            """

            http_options = (
                _BaseSaasRolloutsRestTransport._BaseGetRolloutKind._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_rollout_kind(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasRolloutsRestTransport._BaseGetRolloutKind,
                    "_BaseGetRolloutKind__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasRolloutsClient.GetRolloutKind",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts",
                        "rpcName": "GetRolloutKind",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasRolloutsRestTransport._GetRolloutKind._get_response(
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
            resp = rollouts_resources.RolloutKind()
            pb_resp = rollouts_resources.RolloutKind.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_rollout_kind(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_rollout_kind_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = rollouts_resources.RolloutKind.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasRolloutsClient.get_rollout_kind",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts",
                        "rpcName": "GetRolloutKind",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListRolloutKinds(
        _BaseSaasRolloutsRestTransport._BaseListRolloutKinds, SaasRolloutsRestStub
    ):
        def __hash__(self):
            return hash("SaasRolloutsRestTransport.ListRolloutKinds")

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
            request: rollouts_service.ListRolloutKindsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> rollouts_service.ListRolloutKindsResponse:
            r"""Call the list rollout kinds method over HTTP.

            Args:
                request (~.rollouts_service.ListRolloutKindsRequest):
                    The request object. The request structure for the
                ListRolloutKinds method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.rollouts_service.ListRolloutKindsResponse:
                    The response structure for the
                ListRolloutKinds method.

            """

            http_options = (
                _BaseSaasRolloutsRestTransport._BaseListRolloutKinds._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_rollout_kinds(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasRolloutsRestTransport._BaseListRolloutKinds,
                    "_BaseListRolloutKinds__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasRolloutsClient.ListRolloutKinds",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts",
                        "rpcName": "ListRolloutKinds",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasRolloutsRestTransport._ListRolloutKinds._get_response(
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
            resp = rollouts_service.ListRolloutKindsResponse()
            pb_resp = rollouts_service.ListRolloutKindsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_rollout_kinds(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_rollout_kinds_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        rollouts_service.ListRolloutKindsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasRolloutsClient.list_rollout_kinds",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts",
                        "rpcName": "ListRolloutKinds",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListRollouts(
        _BaseSaasRolloutsRestTransport._BaseListRollouts, SaasRolloutsRestStub
    ):
        def __hash__(self):
            return hash("SaasRolloutsRestTransport.ListRollouts")

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
            request: rollouts_service.ListRolloutsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> rollouts_service.ListRolloutsResponse:
            r"""Call the list rollouts method over HTTP.

            Args:
                request (~.rollouts_service.ListRolloutsRequest):
                    The request object. The request structure for the
                ListRollouts method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.rollouts_service.ListRolloutsResponse:
                    The response structure for the
                ListRollouts method.

            """

            http_options = (
                _BaseSaasRolloutsRestTransport._BaseListRollouts._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_rollouts(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasRolloutsRestTransport._BaseListRollouts,
                    "_BaseListRollouts__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasRolloutsClient.ListRollouts",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts",
                        "rpcName": "ListRollouts",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasRolloutsRestTransport._ListRollouts._get_response(
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
            resp = rollouts_service.ListRolloutsResponse()
            pb_resp = rollouts_service.ListRolloutsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_rollouts(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_rollouts_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = rollouts_service.ListRolloutsResponse.to_json(
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
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasRolloutsClient.list_rollouts",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts",
                        "rpcName": "ListRollouts",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateRollout(
        _BaseSaasRolloutsRestTransport._BaseUpdateRollout, SaasRolloutsRestStub
    ):
        def __hash__(self):
            return hash("SaasRolloutsRestTransport.UpdateRollout")

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
            request: rollouts_service.UpdateRolloutRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> rollouts_resources.Rollout:
            r"""Call the update rollout method over HTTP.

            Args:
                request (~.rollouts_service.UpdateRolloutRequest):
                    The request object. The request structure for the
                UpdateRollout method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.rollouts_resources.Rollout:
                    Represents a single rollout execution
                and its results

            """

            http_options = (
                _BaseSaasRolloutsRestTransport._BaseUpdateRollout._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_rollout(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasRolloutsRestTransport._BaseUpdateRollout,
                    "_BaseUpdateRollout__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasRolloutsClient.UpdateRollout",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts",
                        "rpcName": "UpdateRollout",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasRolloutsRestTransport._UpdateRollout._get_response(
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
            resp = rollouts_resources.Rollout()
            pb_resp = rollouts_resources.Rollout.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_rollout(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_rollout_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = rollouts_resources.Rollout.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasRolloutsClient.update_rollout",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts",
                        "rpcName": "UpdateRollout",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateRolloutKind(
        _BaseSaasRolloutsRestTransport._BaseUpdateRolloutKind, SaasRolloutsRestStub
    ):
        def __hash__(self):
            return hash("SaasRolloutsRestTransport.UpdateRolloutKind")

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
            request: rollouts_service.UpdateRolloutKindRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> rollouts_resources.RolloutKind:
            r"""Call the update rollout kind method over HTTP.

            Args:
                request (~.rollouts_service.UpdateRolloutKindRequest):
                    The request object. The request structure for the
                UpdateRolloutKind method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.rollouts_resources.RolloutKind:
                    An object that describes various
                settings of Rollout execution. Includes
                built-in policies across GCP and GDC,
                and customizable policies.

            """

            http_options = _BaseSaasRolloutsRestTransport._BaseUpdateRolloutKind._get_http_options()
            request, metadata = self._interceptor.pre_update_rollout_kind(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasRolloutsRestTransport._BaseUpdateRolloutKind,
                    "_BaseUpdateRolloutKind__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasRolloutsClient.UpdateRolloutKind",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts",
                        "rpcName": "UpdateRolloutKind",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasRolloutsRestTransport._UpdateRolloutKind._get_response(
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
            resp = rollouts_resources.RolloutKind()
            pb_resp = rollouts_resources.RolloutKind.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_rollout_kind(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_rollout_kind_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = rollouts_resources.RolloutKind.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasRolloutsClient.update_rollout_kind",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts",
                        "rpcName": "UpdateRolloutKind",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_rollout(
        self,
    ) -> Callable[[rollouts_service.CreateRolloutRequest], rollouts_resources.Rollout]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateRollout(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_rollout_kind(
        self,
    ) -> Callable[
        [rollouts_service.CreateRolloutKindRequest], rollouts_resources.RolloutKind
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateRolloutKind(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_rollout(
        self,
    ) -> Callable[[rollouts_service.DeleteRolloutRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteRollout(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_rollout_kind(
        self,
    ) -> Callable[[rollouts_service.DeleteRolloutKindRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteRolloutKind(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_rollout(
        self,
    ) -> Callable[[rollouts_service.GetRolloutRequest], rollouts_resources.Rollout]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetRollout(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_rollout_kind(
        self,
    ) -> Callable[
        [rollouts_service.GetRolloutKindRequest], rollouts_resources.RolloutKind
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetRolloutKind(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_rollout_kinds(
        self,
    ) -> Callable[
        [rollouts_service.ListRolloutKindsRequest],
        rollouts_service.ListRolloutKindsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListRolloutKinds(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_rollouts(
        self,
    ) -> Callable[
        [rollouts_service.ListRolloutsRequest], rollouts_service.ListRolloutsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListRollouts(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_rollout(
        self,
    ) -> Callable[[rollouts_service.UpdateRolloutRequest], rollouts_resources.Rollout]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateRollout(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_rollout_kind(
        self,
    ) -> Callable[
        [rollouts_service.UpdateRolloutKindRequest], rollouts_resources.RolloutKind
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateRolloutKind(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseSaasRolloutsRestTransport._BaseGetLocation, SaasRolloutsRestStub
    ):
        def __hash__(self):
            return hash("SaasRolloutsRestTransport.GetLocation")

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

            http_options = (
                _BaseSaasRolloutsRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasRolloutsRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasRolloutsClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasRolloutsRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasRolloutsAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts",
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
        _BaseSaasRolloutsRestTransport._BaseListLocations, SaasRolloutsRestStub
    ):
        def __hash__(self):
            return hash("SaasRolloutsRestTransport.ListLocations")

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

            http_options = (
                _BaseSaasRolloutsRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSaasRolloutsRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasRolloutsClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SaasRolloutsRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.saasplatform.saasservicemgmt_v1beta1.SaasRolloutsAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.saasplatform.saasservicemgmt.v1beta1.SaasRollouts",
                        "rpcName": "ListLocations",
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


__all__ = ("SaasRolloutsRestTransport",)
