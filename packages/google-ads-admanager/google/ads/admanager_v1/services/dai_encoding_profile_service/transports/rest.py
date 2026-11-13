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
from google.ads.admanager_v1.types import (
    dai_encoding_profile_messages,
    dai_encoding_profile_service,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseDaiEncodingProfileServiceRestTransport

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


class DaiEncodingProfileServiceRestInterceptor:
    """Interceptor for DaiEncodingProfileService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the DaiEncodingProfileServiceRestTransport.

    .. code-block:: python
        class MyCustomDaiEncodingProfileServiceInterceptor(DaiEncodingProfileServiceRestInterceptor):
            def pre_batch_activate_dai_encoding_profiles(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_activate_dai_encoding_profiles(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_archive_dai_encoding_profiles(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_archive_dai_encoding_profiles(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_create_dai_encoding_profiles(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_dai_encoding_profiles(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_update_dai_encoding_profiles(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_dai_encoding_profiles(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_dai_encoding_profile(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_dai_encoding_profile(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_dai_encoding_profile(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_dai_encoding_profile(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_dai_encoding_profiles(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_dai_encoding_profiles(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_dai_encoding_profile(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_dai_encoding_profile(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = DaiEncodingProfileServiceRestTransport(interceptor=MyCustomDaiEncodingProfileServiceInterceptor())
        client = DaiEncodingProfileServiceClient(transport=transport)


    """

    def pre_batch_activate_dai_encoding_profiles(
        self,
        request: dai_encoding_profile_service.BatchActivateDaiEncodingProfilesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dai_encoding_profile_service.BatchActivateDaiEncodingProfilesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_activate_dai_encoding_profiles

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DaiEncodingProfileService server.
        """
        return request, metadata

    def post_batch_activate_dai_encoding_profiles(
        self,
        response: dai_encoding_profile_service.BatchActivateDaiEncodingProfilesResponse,
    ) -> dai_encoding_profile_service.BatchActivateDaiEncodingProfilesResponse:
        """Post-rpc interceptor for batch_activate_dai_encoding_profiles

        DEPRECATED. Please use the `post_batch_activate_dai_encoding_profiles_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DaiEncodingProfileService server but before
        it is returned to user code. This `post_batch_activate_dai_encoding_profiles` interceptor runs
        before the `post_batch_activate_dai_encoding_profiles_with_metadata` interceptor.
        """
        return response

    def post_batch_activate_dai_encoding_profiles_with_metadata(
        self,
        response: dai_encoding_profile_service.BatchActivateDaiEncodingProfilesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dai_encoding_profile_service.BatchActivateDaiEncodingProfilesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_activate_dai_encoding_profiles

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DaiEncodingProfileService server but before it is returned to user code.

        We recommend only using this `post_batch_activate_dai_encoding_profiles_with_metadata`
        interceptor in new development instead of the `post_batch_activate_dai_encoding_profiles` interceptor.
        When both interceptors are used, this `post_batch_activate_dai_encoding_profiles_with_metadata` interceptor runs after the
        `post_batch_activate_dai_encoding_profiles` interceptor. The (possibly modified) response returned by
        `post_batch_activate_dai_encoding_profiles` will be passed to
        `post_batch_activate_dai_encoding_profiles_with_metadata`.
        """
        return response, metadata

    def pre_batch_archive_dai_encoding_profiles(
        self,
        request: dai_encoding_profile_service.BatchArchiveDaiEncodingProfilesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dai_encoding_profile_service.BatchArchiveDaiEncodingProfilesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_archive_dai_encoding_profiles

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DaiEncodingProfileService server.
        """
        return request, metadata

    def post_batch_archive_dai_encoding_profiles(
        self,
        response: dai_encoding_profile_service.BatchArchiveDaiEncodingProfilesResponse,
    ) -> dai_encoding_profile_service.BatchArchiveDaiEncodingProfilesResponse:
        """Post-rpc interceptor for batch_archive_dai_encoding_profiles

        DEPRECATED. Please use the `post_batch_archive_dai_encoding_profiles_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DaiEncodingProfileService server but before
        it is returned to user code. This `post_batch_archive_dai_encoding_profiles` interceptor runs
        before the `post_batch_archive_dai_encoding_profiles_with_metadata` interceptor.
        """
        return response

    def post_batch_archive_dai_encoding_profiles_with_metadata(
        self,
        response: dai_encoding_profile_service.BatchArchiveDaiEncodingProfilesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dai_encoding_profile_service.BatchArchiveDaiEncodingProfilesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_archive_dai_encoding_profiles

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DaiEncodingProfileService server but before it is returned to user code.

        We recommend only using this `post_batch_archive_dai_encoding_profiles_with_metadata`
        interceptor in new development instead of the `post_batch_archive_dai_encoding_profiles` interceptor.
        When both interceptors are used, this `post_batch_archive_dai_encoding_profiles_with_metadata` interceptor runs after the
        `post_batch_archive_dai_encoding_profiles` interceptor. The (possibly modified) response returned by
        `post_batch_archive_dai_encoding_profiles` will be passed to
        `post_batch_archive_dai_encoding_profiles_with_metadata`.
        """
        return response, metadata

    def pre_batch_create_dai_encoding_profiles(
        self,
        request: dai_encoding_profile_service.BatchCreateDaiEncodingProfilesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dai_encoding_profile_service.BatchCreateDaiEncodingProfilesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_create_dai_encoding_profiles

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DaiEncodingProfileService server.
        """
        return request, metadata

    def post_batch_create_dai_encoding_profiles(
        self,
        response: dai_encoding_profile_service.BatchCreateDaiEncodingProfilesResponse,
    ) -> dai_encoding_profile_service.BatchCreateDaiEncodingProfilesResponse:
        """Post-rpc interceptor for batch_create_dai_encoding_profiles

        DEPRECATED. Please use the `post_batch_create_dai_encoding_profiles_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DaiEncodingProfileService server but before
        it is returned to user code. This `post_batch_create_dai_encoding_profiles` interceptor runs
        before the `post_batch_create_dai_encoding_profiles_with_metadata` interceptor.
        """
        return response

    def post_batch_create_dai_encoding_profiles_with_metadata(
        self,
        response: dai_encoding_profile_service.BatchCreateDaiEncodingProfilesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dai_encoding_profile_service.BatchCreateDaiEncodingProfilesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_create_dai_encoding_profiles

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DaiEncodingProfileService server but before it is returned to user code.

        We recommend only using this `post_batch_create_dai_encoding_profiles_with_metadata`
        interceptor in new development instead of the `post_batch_create_dai_encoding_profiles` interceptor.
        When both interceptors are used, this `post_batch_create_dai_encoding_profiles_with_metadata` interceptor runs after the
        `post_batch_create_dai_encoding_profiles` interceptor. The (possibly modified) response returned by
        `post_batch_create_dai_encoding_profiles` will be passed to
        `post_batch_create_dai_encoding_profiles_with_metadata`.
        """
        return response, metadata

    def pre_batch_update_dai_encoding_profiles(
        self,
        request: dai_encoding_profile_service.BatchUpdateDaiEncodingProfilesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dai_encoding_profile_service.BatchUpdateDaiEncodingProfilesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_update_dai_encoding_profiles

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DaiEncodingProfileService server.
        """
        return request, metadata

    def post_batch_update_dai_encoding_profiles(
        self,
        response: dai_encoding_profile_service.BatchUpdateDaiEncodingProfilesResponse,
    ) -> dai_encoding_profile_service.BatchUpdateDaiEncodingProfilesResponse:
        """Post-rpc interceptor for batch_update_dai_encoding_profiles

        DEPRECATED. Please use the `post_batch_update_dai_encoding_profiles_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DaiEncodingProfileService server but before
        it is returned to user code. This `post_batch_update_dai_encoding_profiles` interceptor runs
        before the `post_batch_update_dai_encoding_profiles_with_metadata` interceptor.
        """
        return response

    def post_batch_update_dai_encoding_profiles_with_metadata(
        self,
        response: dai_encoding_profile_service.BatchUpdateDaiEncodingProfilesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dai_encoding_profile_service.BatchUpdateDaiEncodingProfilesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_update_dai_encoding_profiles

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DaiEncodingProfileService server but before it is returned to user code.

        We recommend only using this `post_batch_update_dai_encoding_profiles_with_metadata`
        interceptor in new development instead of the `post_batch_update_dai_encoding_profiles` interceptor.
        When both interceptors are used, this `post_batch_update_dai_encoding_profiles_with_metadata` interceptor runs after the
        `post_batch_update_dai_encoding_profiles` interceptor. The (possibly modified) response returned by
        `post_batch_update_dai_encoding_profiles` will be passed to
        `post_batch_update_dai_encoding_profiles_with_metadata`.
        """
        return response, metadata

    def pre_create_dai_encoding_profile(
        self,
        request: dai_encoding_profile_service.CreateDaiEncodingProfileRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dai_encoding_profile_service.CreateDaiEncodingProfileRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_dai_encoding_profile

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DaiEncodingProfileService server.
        """
        return request, metadata

    def post_create_dai_encoding_profile(
        self, response: dai_encoding_profile_messages.DaiEncodingProfile
    ) -> dai_encoding_profile_messages.DaiEncodingProfile:
        """Post-rpc interceptor for create_dai_encoding_profile

        DEPRECATED. Please use the `post_create_dai_encoding_profile_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DaiEncodingProfileService server but before
        it is returned to user code. This `post_create_dai_encoding_profile` interceptor runs
        before the `post_create_dai_encoding_profile_with_metadata` interceptor.
        """
        return response

    def post_create_dai_encoding_profile_with_metadata(
        self,
        response: dai_encoding_profile_messages.DaiEncodingProfile,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dai_encoding_profile_messages.DaiEncodingProfile,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for create_dai_encoding_profile

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DaiEncodingProfileService server but before it is returned to user code.

        We recommend only using this `post_create_dai_encoding_profile_with_metadata`
        interceptor in new development instead of the `post_create_dai_encoding_profile` interceptor.
        When both interceptors are used, this `post_create_dai_encoding_profile_with_metadata` interceptor runs after the
        `post_create_dai_encoding_profile` interceptor. The (possibly modified) response returned by
        `post_create_dai_encoding_profile` will be passed to
        `post_create_dai_encoding_profile_with_metadata`.
        """
        return response, metadata

    def pre_get_dai_encoding_profile(
        self,
        request: dai_encoding_profile_service.GetDaiEncodingProfileRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dai_encoding_profile_service.GetDaiEncodingProfileRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_dai_encoding_profile

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DaiEncodingProfileService server.
        """
        return request, metadata

    def post_get_dai_encoding_profile(
        self, response: dai_encoding_profile_messages.DaiEncodingProfile
    ) -> dai_encoding_profile_messages.DaiEncodingProfile:
        """Post-rpc interceptor for get_dai_encoding_profile

        DEPRECATED. Please use the `post_get_dai_encoding_profile_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DaiEncodingProfileService server but before
        it is returned to user code. This `post_get_dai_encoding_profile` interceptor runs
        before the `post_get_dai_encoding_profile_with_metadata` interceptor.
        """
        return response

    def post_get_dai_encoding_profile_with_metadata(
        self,
        response: dai_encoding_profile_messages.DaiEncodingProfile,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dai_encoding_profile_messages.DaiEncodingProfile,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_dai_encoding_profile

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DaiEncodingProfileService server but before it is returned to user code.

        We recommend only using this `post_get_dai_encoding_profile_with_metadata`
        interceptor in new development instead of the `post_get_dai_encoding_profile` interceptor.
        When both interceptors are used, this `post_get_dai_encoding_profile_with_metadata` interceptor runs after the
        `post_get_dai_encoding_profile` interceptor. The (possibly modified) response returned by
        `post_get_dai_encoding_profile` will be passed to
        `post_get_dai_encoding_profile_with_metadata`.
        """
        return response, metadata

    def pre_list_dai_encoding_profiles(
        self,
        request: dai_encoding_profile_service.ListDaiEncodingProfilesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dai_encoding_profile_service.ListDaiEncodingProfilesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_dai_encoding_profiles

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DaiEncodingProfileService server.
        """
        return request, metadata

    def post_list_dai_encoding_profiles(
        self, response: dai_encoding_profile_service.ListDaiEncodingProfilesResponse
    ) -> dai_encoding_profile_service.ListDaiEncodingProfilesResponse:
        """Post-rpc interceptor for list_dai_encoding_profiles

        DEPRECATED. Please use the `post_list_dai_encoding_profiles_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DaiEncodingProfileService server but before
        it is returned to user code. This `post_list_dai_encoding_profiles` interceptor runs
        before the `post_list_dai_encoding_profiles_with_metadata` interceptor.
        """
        return response

    def post_list_dai_encoding_profiles_with_metadata(
        self,
        response: dai_encoding_profile_service.ListDaiEncodingProfilesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dai_encoding_profile_service.ListDaiEncodingProfilesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_dai_encoding_profiles

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DaiEncodingProfileService server but before it is returned to user code.

        We recommend only using this `post_list_dai_encoding_profiles_with_metadata`
        interceptor in new development instead of the `post_list_dai_encoding_profiles` interceptor.
        When both interceptors are used, this `post_list_dai_encoding_profiles_with_metadata` interceptor runs after the
        `post_list_dai_encoding_profiles` interceptor. The (possibly modified) response returned by
        `post_list_dai_encoding_profiles` will be passed to
        `post_list_dai_encoding_profiles_with_metadata`.
        """
        return response, metadata

    def pre_update_dai_encoding_profile(
        self,
        request: dai_encoding_profile_service.UpdateDaiEncodingProfileRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dai_encoding_profile_service.UpdateDaiEncodingProfileRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_dai_encoding_profile

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DaiEncodingProfileService server.
        """
        return request, metadata

    def post_update_dai_encoding_profile(
        self, response: dai_encoding_profile_messages.DaiEncodingProfile
    ) -> dai_encoding_profile_messages.DaiEncodingProfile:
        """Post-rpc interceptor for update_dai_encoding_profile

        DEPRECATED. Please use the `post_update_dai_encoding_profile_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DaiEncodingProfileService server but before
        it is returned to user code. This `post_update_dai_encoding_profile` interceptor runs
        before the `post_update_dai_encoding_profile_with_metadata` interceptor.
        """
        return response

    def post_update_dai_encoding_profile_with_metadata(
        self,
        response: dai_encoding_profile_messages.DaiEncodingProfile,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dai_encoding_profile_messages.DaiEncodingProfile,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for update_dai_encoding_profile

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DaiEncodingProfileService server but before it is returned to user code.

        We recommend only using this `post_update_dai_encoding_profile_with_metadata`
        interceptor in new development instead of the `post_update_dai_encoding_profile` interceptor.
        When both interceptors are used, this `post_update_dai_encoding_profile_with_metadata` interceptor runs after the
        `post_update_dai_encoding_profile` interceptor. The (possibly modified) response returned by
        `post_update_dai_encoding_profile` will be passed to
        `post_update_dai_encoding_profile_with_metadata`.
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
        before they are sent to the DaiEncodingProfileService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the DaiEncodingProfileService server but before
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
        before they are sent to the DaiEncodingProfileService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the DaiEncodingProfileService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class DaiEncodingProfileServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: DaiEncodingProfileServiceRestInterceptor


class DaiEncodingProfileServiceRestTransport(
    _BaseDaiEncodingProfileServiceRestTransport
):
    """REST backend synchronous transport for DaiEncodingProfileService.

    Provides methods for handling ``DaiEncodingProfile`` objects.

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
        interceptor: Optional[DaiEncodingProfileServiceRestInterceptor] = None,
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
            interceptor (Optional[DaiEncodingProfileServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or DaiEncodingProfileServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchActivateDaiEncodingProfiles(
        _BaseDaiEncodingProfileServiceRestTransport._BaseBatchActivateDaiEncodingProfiles,
        DaiEncodingProfileServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "DaiEncodingProfileServiceRestTransport.BatchActivateDaiEncodingProfiles"
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
            request: dai_encoding_profile_service.BatchActivateDaiEncodingProfilesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dai_encoding_profile_service.BatchActivateDaiEncodingProfilesResponse:
            r"""Call the batch activate dai
            encoding profiles method over HTTP.

                Args:
                    request (~.dai_encoding_profile_service.BatchActivateDaiEncodingProfilesRequest):
                        The request object. Request object for ``BatchActivateDaiEncodingProfiles``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.dai_encoding_profile_service.BatchActivateDaiEncodingProfilesResponse:
                        Response object for ``BatchActivateDaiEncodingProfiles``
                    method.

            """

            http_options = _BaseDaiEncodingProfileServiceRestTransport._BaseBatchActivateDaiEncodingProfiles._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_activate_dai_encoding_profiles(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDaiEncodingProfileServiceRestTransport._BaseBatchActivateDaiEncodingProfiles,
                    "_BaseBatchActivateDaiEncodingProfiles__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.DaiEncodingProfileServiceClient.BatchActivateDaiEncodingProfiles",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiEncodingProfileService",
                        "rpcName": "BatchActivateDaiEncodingProfiles",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DaiEncodingProfileServiceRestTransport._BatchActivateDaiEncodingProfiles._get_response(
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
            resp = (
                dai_encoding_profile_service.BatchActivateDaiEncodingProfilesResponse()
            )
            pb_resp = dai_encoding_profile_service.BatchActivateDaiEncodingProfilesResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_activate_dai_encoding_profiles(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_activate_dai_encoding_profiles_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dai_encoding_profile_service.BatchActivateDaiEncodingProfilesResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.DaiEncodingProfileServiceClient.batch_activate_dai_encoding_profiles",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiEncodingProfileService",
                        "rpcName": "BatchActivateDaiEncodingProfiles",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchArchiveDaiEncodingProfiles(
        _BaseDaiEncodingProfileServiceRestTransport._BaseBatchArchiveDaiEncodingProfiles,
        DaiEncodingProfileServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "DaiEncodingProfileServiceRestTransport.BatchArchiveDaiEncodingProfiles"
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
            request: dai_encoding_profile_service.BatchArchiveDaiEncodingProfilesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dai_encoding_profile_service.BatchArchiveDaiEncodingProfilesResponse:
            r"""Call the batch archive dai
            encoding profiles method over HTTP.

                Args:
                    request (~.dai_encoding_profile_service.BatchArchiveDaiEncodingProfilesRequest):
                        The request object. Request object for ``BatchArchiveDaiEncodingProfiles``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.dai_encoding_profile_service.BatchArchiveDaiEncodingProfilesResponse:
                        Response object for ``BatchArchiveDaiEncodingProfiles``
                    method.

            """

            http_options = _BaseDaiEncodingProfileServiceRestTransport._BaseBatchArchiveDaiEncodingProfiles._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_archive_dai_encoding_profiles(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDaiEncodingProfileServiceRestTransport._BaseBatchArchiveDaiEncodingProfiles,
                    "_BaseBatchArchiveDaiEncodingProfiles__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.DaiEncodingProfileServiceClient.BatchArchiveDaiEncodingProfiles",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiEncodingProfileService",
                        "rpcName": "BatchArchiveDaiEncodingProfiles",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DaiEncodingProfileServiceRestTransport._BatchArchiveDaiEncodingProfiles._get_response(
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
            resp = (
                dai_encoding_profile_service.BatchArchiveDaiEncodingProfilesResponse()
            )
            pb_resp = (
                dai_encoding_profile_service.BatchArchiveDaiEncodingProfilesResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_archive_dai_encoding_profiles(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_archive_dai_encoding_profiles_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dai_encoding_profile_service.BatchArchiveDaiEncodingProfilesResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.DaiEncodingProfileServiceClient.batch_archive_dai_encoding_profiles",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiEncodingProfileService",
                        "rpcName": "BatchArchiveDaiEncodingProfiles",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchCreateDaiEncodingProfiles(
        _BaseDaiEncodingProfileServiceRestTransport._BaseBatchCreateDaiEncodingProfiles,
        DaiEncodingProfileServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "DaiEncodingProfileServiceRestTransport.BatchCreateDaiEncodingProfiles"
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
            request: dai_encoding_profile_service.BatchCreateDaiEncodingProfilesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dai_encoding_profile_service.BatchCreateDaiEncodingProfilesResponse:
            r"""Call the batch create dai encoding
            profiles method over HTTP.

                Args:
                    request (~.dai_encoding_profile_service.BatchCreateDaiEncodingProfilesRequest):
                        The request object. Request object for ``BatchCreateDaiEncodingProfiles``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.dai_encoding_profile_service.BatchCreateDaiEncodingProfilesResponse:
                        Response object for ``BatchCreateDaiEncodingProfiles``
                    method.

            """

            http_options = _BaseDaiEncodingProfileServiceRestTransport._BaseBatchCreateDaiEncodingProfiles._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_create_dai_encoding_profiles(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDaiEncodingProfileServiceRestTransport._BaseBatchCreateDaiEncodingProfiles,
                    "_BaseBatchCreateDaiEncodingProfiles__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.DaiEncodingProfileServiceClient.BatchCreateDaiEncodingProfiles",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiEncodingProfileService",
                        "rpcName": "BatchCreateDaiEncodingProfiles",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DaiEncodingProfileServiceRestTransport._BatchCreateDaiEncodingProfiles._get_response(
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
            resp = dai_encoding_profile_service.BatchCreateDaiEncodingProfilesResponse()
            pb_resp = (
                dai_encoding_profile_service.BatchCreateDaiEncodingProfilesResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_dai_encoding_profiles(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_create_dai_encoding_profiles_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dai_encoding_profile_service.BatchCreateDaiEncodingProfilesResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.DaiEncodingProfileServiceClient.batch_create_dai_encoding_profiles",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiEncodingProfileService",
                        "rpcName": "BatchCreateDaiEncodingProfiles",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchUpdateDaiEncodingProfiles(
        _BaseDaiEncodingProfileServiceRestTransport._BaseBatchUpdateDaiEncodingProfiles,
        DaiEncodingProfileServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "DaiEncodingProfileServiceRestTransport.BatchUpdateDaiEncodingProfiles"
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
            request: dai_encoding_profile_service.BatchUpdateDaiEncodingProfilesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dai_encoding_profile_service.BatchUpdateDaiEncodingProfilesResponse:
            r"""Call the batch update dai encoding
            profiles method over HTTP.

                Args:
                    request (~.dai_encoding_profile_service.BatchUpdateDaiEncodingProfilesRequest):
                        The request object. Request object for ``BatchUpdateDaiEncodingProfiles``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.dai_encoding_profile_service.BatchUpdateDaiEncodingProfilesResponse:
                        Response object for ``BatchUpdateDaiEncodingProfiles``
                    method.

            """

            http_options = _BaseDaiEncodingProfileServiceRestTransport._BaseBatchUpdateDaiEncodingProfiles._get_http_options()
            request, metadata = (
                self._interceptor.pre_batch_update_dai_encoding_profiles(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDaiEncodingProfileServiceRestTransport._BaseBatchUpdateDaiEncodingProfiles,
                    "_BaseBatchUpdateDaiEncodingProfiles__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.DaiEncodingProfileServiceClient.BatchUpdateDaiEncodingProfiles",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiEncodingProfileService",
                        "rpcName": "BatchUpdateDaiEncodingProfiles",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DaiEncodingProfileServiceRestTransport._BatchUpdateDaiEncodingProfiles._get_response(
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
            resp = dai_encoding_profile_service.BatchUpdateDaiEncodingProfilesResponse()
            pb_resp = (
                dai_encoding_profile_service.BatchUpdateDaiEncodingProfilesResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_dai_encoding_profiles(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_update_dai_encoding_profiles_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dai_encoding_profile_service.BatchUpdateDaiEncodingProfilesResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.DaiEncodingProfileServiceClient.batch_update_dai_encoding_profiles",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiEncodingProfileService",
                        "rpcName": "BatchUpdateDaiEncodingProfiles",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateDaiEncodingProfile(
        _BaseDaiEncodingProfileServiceRestTransport._BaseCreateDaiEncodingProfile,
        DaiEncodingProfileServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "DaiEncodingProfileServiceRestTransport.CreateDaiEncodingProfile"
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
            request: dai_encoding_profile_service.CreateDaiEncodingProfileRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dai_encoding_profile_messages.DaiEncodingProfile:
            r"""Call the create dai encoding
            profile method over HTTP.

                Args:
                    request (~.dai_encoding_profile_service.CreateDaiEncodingProfileRequest):
                        The request object. Request object for ``CreateDaiEncodingProfile`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.dai_encoding_profile_messages.DaiEncodingProfile:
                        A DaiEncodingProfile contains data
                    about a publisher's encoding profiles.
                    Ad Manager Dynamic Ad Insertion (DAI)
                    uses the profile information about the
                    content to select an appropriate ad
                    transcode to play for the particular
                    video.

            """

            http_options = _BaseDaiEncodingProfileServiceRestTransport._BaseCreateDaiEncodingProfile._get_http_options()
            request, metadata = self._interceptor.pre_create_dai_encoding_profile(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDaiEncodingProfileServiceRestTransport._BaseCreateDaiEncodingProfile,
                    "_BaseCreateDaiEncodingProfile__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.DaiEncodingProfileServiceClient.CreateDaiEncodingProfile",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiEncodingProfileService",
                        "rpcName": "CreateDaiEncodingProfile",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DaiEncodingProfileServiceRestTransport._CreateDaiEncodingProfile._get_response(
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
            resp = dai_encoding_profile_messages.DaiEncodingProfile()
            pb_resp = dai_encoding_profile_messages.DaiEncodingProfile.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_dai_encoding_profile(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_dai_encoding_profile_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        dai_encoding_profile_messages.DaiEncodingProfile.to_json(
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
                    "Received response for google.ads.admanager_v1.DaiEncodingProfileServiceClient.create_dai_encoding_profile",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiEncodingProfileService",
                        "rpcName": "CreateDaiEncodingProfile",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDaiEncodingProfile(
        _BaseDaiEncodingProfileServiceRestTransport._BaseGetDaiEncodingProfile,
        DaiEncodingProfileServiceRestStub,
    ):
        def __hash__(self):
            return hash("DaiEncodingProfileServiceRestTransport.GetDaiEncodingProfile")

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
            request: dai_encoding_profile_service.GetDaiEncodingProfileRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dai_encoding_profile_messages.DaiEncodingProfile:
            r"""Call the get dai encoding profile method over HTTP.

            Args:
                request (~.dai_encoding_profile_service.GetDaiEncodingProfileRequest):
                    The request object. Request object for ``GetDaiEncodingProfile`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dai_encoding_profile_messages.DaiEncodingProfile:
                    A DaiEncodingProfile contains data
                about a publisher's encoding profiles.
                Ad Manager Dynamic Ad Insertion (DAI)
                uses the profile information about the
                content to select an appropriate ad
                transcode to play for the particular
                video.

            """

            http_options = _BaseDaiEncodingProfileServiceRestTransport._BaseGetDaiEncodingProfile._get_http_options()
            request, metadata = self._interceptor.pre_get_dai_encoding_profile(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDaiEncodingProfileServiceRestTransport._BaseGetDaiEncodingProfile,
                    "_BaseGetDaiEncodingProfile__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.DaiEncodingProfileServiceClient.GetDaiEncodingProfile",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiEncodingProfileService",
                        "rpcName": "GetDaiEncodingProfile",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DaiEncodingProfileServiceRestTransport._GetDaiEncodingProfile._get_response(
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
            resp = dai_encoding_profile_messages.DaiEncodingProfile()
            pb_resp = dai_encoding_profile_messages.DaiEncodingProfile.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_dai_encoding_profile(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_dai_encoding_profile_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        dai_encoding_profile_messages.DaiEncodingProfile.to_json(
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
                    "Received response for google.ads.admanager_v1.DaiEncodingProfileServiceClient.get_dai_encoding_profile",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiEncodingProfileService",
                        "rpcName": "GetDaiEncodingProfile",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDaiEncodingProfiles(
        _BaseDaiEncodingProfileServiceRestTransport._BaseListDaiEncodingProfiles,
        DaiEncodingProfileServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "DaiEncodingProfileServiceRestTransport.ListDaiEncodingProfiles"
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
            request: dai_encoding_profile_service.ListDaiEncodingProfilesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dai_encoding_profile_service.ListDaiEncodingProfilesResponse:
            r"""Call the list dai encoding
            profiles method over HTTP.

                Args:
                    request (~.dai_encoding_profile_service.ListDaiEncodingProfilesRequest):
                        The request object. Request object for ``ListDaiEncodingProfiles`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.dai_encoding_profile_service.ListDaiEncodingProfilesResponse:
                        Response object for ``ListDaiEncodingProfilesRequest``
                    containing matching ``DaiEncodingProfile`` objects.

            """

            http_options = _BaseDaiEncodingProfileServiceRestTransport._BaseListDaiEncodingProfiles._get_http_options()
            request, metadata = self._interceptor.pre_list_dai_encoding_profiles(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDaiEncodingProfileServiceRestTransport._BaseListDaiEncodingProfiles,
                    "_BaseListDaiEncodingProfiles__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.DaiEncodingProfileServiceClient.ListDaiEncodingProfiles",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiEncodingProfileService",
                        "rpcName": "ListDaiEncodingProfiles",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DaiEncodingProfileServiceRestTransport._ListDaiEncodingProfiles._get_response(
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
            resp = dai_encoding_profile_service.ListDaiEncodingProfilesResponse()
            pb_resp = dai_encoding_profile_service.ListDaiEncodingProfilesResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_dai_encoding_profiles(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_dai_encoding_profiles_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dai_encoding_profile_service.ListDaiEncodingProfilesResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.DaiEncodingProfileServiceClient.list_dai_encoding_profiles",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiEncodingProfileService",
                        "rpcName": "ListDaiEncodingProfiles",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDaiEncodingProfile(
        _BaseDaiEncodingProfileServiceRestTransport._BaseUpdateDaiEncodingProfile,
        DaiEncodingProfileServiceRestStub,
    ):
        def __hash__(self):
            return hash(
                "DaiEncodingProfileServiceRestTransport.UpdateDaiEncodingProfile"
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
            request: dai_encoding_profile_service.UpdateDaiEncodingProfileRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dai_encoding_profile_messages.DaiEncodingProfile:
            r"""Call the update dai encoding
            profile method over HTTP.

                Args:
                    request (~.dai_encoding_profile_service.UpdateDaiEncodingProfileRequest):
                        The request object. Request object for ``UpdateDaiEncodingProfile`` method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.dai_encoding_profile_messages.DaiEncodingProfile:
                        A DaiEncodingProfile contains data
                    about a publisher's encoding profiles.
                    Ad Manager Dynamic Ad Insertion (DAI)
                    uses the profile information about the
                    content to select an appropriate ad
                    transcode to play for the particular
                    video.

            """

            http_options = _BaseDaiEncodingProfileServiceRestTransport._BaseUpdateDaiEncodingProfile._get_http_options()
            request, metadata = self._interceptor.pre_update_dai_encoding_profile(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDaiEncodingProfileServiceRestTransport._BaseUpdateDaiEncodingProfile,
                    "_BaseUpdateDaiEncodingProfile__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.DaiEncodingProfileServiceClient.UpdateDaiEncodingProfile",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiEncodingProfileService",
                        "rpcName": "UpdateDaiEncodingProfile",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DaiEncodingProfileServiceRestTransport._UpdateDaiEncodingProfile._get_response(
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
            resp = dai_encoding_profile_messages.DaiEncodingProfile()
            pb_resp = dai_encoding_profile_messages.DaiEncodingProfile.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_dai_encoding_profile(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_dai_encoding_profile_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        dai_encoding_profile_messages.DaiEncodingProfile.to_json(
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
                    "Received response for google.ads.admanager_v1.DaiEncodingProfileServiceClient.update_dai_encoding_profile",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiEncodingProfileService",
                        "rpcName": "UpdateDaiEncodingProfile",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_activate_dai_encoding_profiles(
        self,
    ) -> Callable[
        [dai_encoding_profile_service.BatchActivateDaiEncodingProfilesRequest],
        dai_encoding_profile_service.BatchActivateDaiEncodingProfilesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchActivateDaiEncodingProfiles(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_archive_dai_encoding_profiles(
        self,
    ) -> Callable[
        [dai_encoding_profile_service.BatchArchiveDaiEncodingProfilesRequest],
        dai_encoding_profile_service.BatchArchiveDaiEncodingProfilesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchArchiveDaiEncodingProfiles(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_create_dai_encoding_profiles(
        self,
    ) -> Callable[
        [dai_encoding_profile_service.BatchCreateDaiEncodingProfilesRequest],
        dai_encoding_profile_service.BatchCreateDaiEncodingProfilesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateDaiEncodingProfiles(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_update_dai_encoding_profiles(
        self,
    ) -> Callable[
        [dai_encoding_profile_service.BatchUpdateDaiEncodingProfilesRequest],
        dai_encoding_profile_service.BatchUpdateDaiEncodingProfilesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdateDaiEncodingProfiles(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_dai_encoding_profile(
        self,
    ) -> Callable[
        [dai_encoding_profile_service.CreateDaiEncodingProfileRequest],
        dai_encoding_profile_messages.DaiEncodingProfile,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDaiEncodingProfile(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_dai_encoding_profile(
        self,
    ) -> Callable[
        [dai_encoding_profile_service.GetDaiEncodingProfileRequest],
        dai_encoding_profile_messages.DaiEncodingProfile,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDaiEncodingProfile(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_dai_encoding_profiles(
        self,
    ) -> Callable[
        [dai_encoding_profile_service.ListDaiEncodingProfilesRequest],
        dai_encoding_profile_service.ListDaiEncodingProfilesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDaiEncodingProfiles(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_dai_encoding_profile(
        self,
    ) -> Callable[
        [dai_encoding_profile_service.UpdateDaiEncodingProfileRequest],
        dai_encoding_profile_messages.DaiEncodingProfile,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDaiEncodingProfile(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseDaiEncodingProfileServiceRestTransport._BaseCancelOperation,
        DaiEncodingProfileServiceRestStub,
    ):
        def __hash__(self):
            return hash("DaiEncodingProfileServiceRestTransport.CancelOperation")

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

            http_options = _BaseDaiEncodingProfileServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDaiEncodingProfileServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.ads.admanager_v1.DaiEncodingProfileServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiEncodingProfileService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DaiEncodingProfileServiceRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseDaiEncodingProfileServiceRestTransport._BaseGetOperation,
        DaiEncodingProfileServiceRestStub,
    ):
        def __hash__(self):
            return hash("DaiEncodingProfileServiceRestTransport.GetOperation")

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

            http_options = _BaseDaiEncodingProfileServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDaiEncodingProfileServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.ads.admanager_v1.DaiEncodingProfileServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiEncodingProfileService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DaiEncodingProfileServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.ads.admanager_v1.DaiEncodingProfileServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.DaiEncodingProfileService",
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


__all__ = ("DaiEncodingProfileServiceRestTransport",)
