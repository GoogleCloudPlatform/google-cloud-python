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
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.compute_v1beta._compat import transcode_request
from google.cloud.compute_v1beta.types import compute

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseTargetSslProxiesRestTransport

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


class TargetSslProxiesRestInterceptor:
    """Interceptor for TargetSslProxies.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the TargetSslProxiesRestTransport.

    .. code-block:: python
        class MyCustomTargetSslProxiesInterceptor(TargetSslProxiesRestInterceptor):
            def pre_delete(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_insert(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_insert(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_backend_service(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_backend_service(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_certificate_map(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_certificate_map(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_proxy_header(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_proxy_header(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_ssl_certificates(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_ssl_certificates(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_set_ssl_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_set_ssl_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_test_iam_permissions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_test_iam_permissions(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = TargetSslProxiesRestTransport(interceptor=MyCustomTargetSslProxiesInterceptor())
        client = TargetSslProxiesClient(transport=transport)


    """

    def pre_delete(
        self,
        request: compute.DeleteTargetSslProxyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.DeleteTargetSslProxyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TargetSslProxies server.
        """
        return request, metadata

    def post_delete(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for delete

        DEPRECATED. Please use the `post_delete_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TargetSslProxies server but before
        it is returned to user code. This `post_delete` interceptor runs
        before the `post_delete_with_metadata` interceptor.
        """
        return response

    def post_delete_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TargetSslProxies server but before it is returned to user code.

        We recommend only using this `post_delete_with_metadata`
        interceptor in new development instead of the `post_delete` interceptor.
        When both interceptors are used, this `post_delete_with_metadata` interceptor runs after the
        `post_delete` interceptor. The (possibly modified) response returned by
        `post_delete` will be passed to
        `post_delete_with_metadata`.
        """
        return response, metadata

    def pre_get(
        self,
        request: compute.GetTargetSslProxyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.GetTargetSslProxyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TargetSslProxies server.
        """
        return request, metadata

    def post_get(self, response: compute.TargetSslProxy) -> compute.TargetSslProxy:
        """Post-rpc interceptor for get

        DEPRECATED. Please use the `post_get_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TargetSslProxies server but before
        it is returned to user code. This `post_get` interceptor runs
        before the `post_get_with_metadata` interceptor.
        """
        return response

    def post_get_with_metadata(
        self,
        response: compute.TargetSslProxy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.TargetSslProxy, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TargetSslProxies server but before it is returned to user code.

        We recommend only using this `post_get_with_metadata`
        interceptor in new development instead of the `post_get` interceptor.
        When both interceptors are used, this `post_get_with_metadata` interceptor runs after the
        `post_get` interceptor. The (possibly modified) response returned by
        `post_get` will be passed to
        `post_get_with_metadata`.
        """
        return response, metadata

    def pre_insert(
        self,
        request: compute.InsertTargetSslProxyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.InsertTargetSslProxyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for insert

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TargetSslProxies server.
        """
        return request, metadata

    def post_insert(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for insert

        DEPRECATED. Please use the `post_insert_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TargetSslProxies server but before
        it is returned to user code. This `post_insert` interceptor runs
        before the `post_insert_with_metadata` interceptor.
        """
        return response

    def post_insert_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for insert

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TargetSslProxies server but before it is returned to user code.

        We recommend only using this `post_insert_with_metadata`
        interceptor in new development instead of the `post_insert` interceptor.
        When both interceptors are used, this `post_insert_with_metadata` interceptor runs after the
        `post_insert` interceptor. The (possibly modified) response returned by
        `post_insert` will be passed to
        `post_insert_with_metadata`.
        """
        return response, metadata

    def pre_list(
        self,
        request: compute.ListTargetSslProxiesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.ListTargetSslProxiesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TargetSslProxies server.
        """
        return request, metadata

    def post_list(
        self, response: compute.TargetSslProxyList
    ) -> compute.TargetSslProxyList:
        """Post-rpc interceptor for list

        DEPRECATED. Please use the `post_list_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TargetSslProxies server but before
        it is returned to user code. This `post_list` interceptor runs
        before the `post_list_with_metadata` interceptor.
        """
        return response

    def post_list_with_metadata(
        self,
        response: compute.TargetSslProxyList,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.TargetSslProxyList, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TargetSslProxies server but before it is returned to user code.

        We recommend only using this `post_list_with_metadata`
        interceptor in new development instead of the `post_list` interceptor.
        When both interceptors are used, this `post_list_with_metadata` interceptor runs after the
        `post_list` interceptor. The (possibly modified) response returned by
        `post_list` will be passed to
        `post_list_with_metadata`.
        """
        return response, metadata

    def pre_set_backend_service(
        self,
        request: compute.SetBackendServiceTargetSslProxyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.SetBackendServiceTargetSslProxyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for set_backend_service

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TargetSslProxies server.
        """
        return request, metadata

    def post_set_backend_service(
        self, response: compute.Operation
    ) -> compute.Operation:
        """Post-rpc interceptor for set_backend_service

        DEPRECATED. Please use the `post_set_backend_service_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TargetSslProxies server but before
        it is returned to user code. This `post_set_backend_service` interceptor runs
        before the `post_set_backend_service_with_metadata` interceptor.
        """
        return response

    def post_set_backend_service_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_backend_service

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TargetSslProxies server but before it is returned to user code.

        We recommend only using this `post_set_backend_service_with_metadata`
        interceptor in new development instead of the `post_set_backend_service` interceptor.
        When both interceptors are used, this `post_set_backend_service_with_metadata` interceptor runs after the
        `post_set_backend_service` interceptor. The (possibly modified) response returned by
        `post_set_backend_service` will be passed to
        `post_set_backend_service_with_metadata`.
        """
        return response, metadata

    def pre_set_certificate_map(
        self,
        request: compute.SetCertificateMapTargetSslProxyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.SetCertificateMapTargetSslProxyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for set_certificate_map

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TargetSslProxies server.
        """
        return request, metadata

    def post_set_certificate_map(
        self, response: compute.Operation
    ) -> compute.Operation:
        """Post-rpc interceptor for set_certificate_map

        DEPRECATED. Please use the `post_set_certificate_map_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TargetSslProxies server but before
        it is returned to user code. This `post_set_certificate_map` interceptor runs
        before the `post_set_certificate_map_with_metadata` interceptor.
        """
        return response

    def post_set_certificate_map_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_certificate_map

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TargetSslProxies server but before it is returned to user code.

        We recommend only using this `post_set_certificate_map_with_metadata`
        interceptor in new development instead of the `post_set_certificate_map` interceptor.
        When both interceptors are used, this `post_set_certificate_map_with_metadata` interceptor runs after the
        `post_set_certificate_map` interceptor. The (possibly modified) response returned by
        `post_set_certificate_map` will be passed to
        `post_set_certificate_map_with_metadata`.
        """
        return response, metadata

    def pre_set_proxy_header(
        self,
        request: compute.SetProxyHeaderTargetSslProxyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.SetProxyHeaderTargetSslProxyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for set_proxy_header

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TargetSslProxies server.
        """
        return request, metadata

    def post_set_proxy_header(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for set_proxy_header

        DEPRECATED. Please use the `post_set_proxy_header_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TargetSslProxies server but before
        it is returned to user code. This `post_set_proxy_header` interceptor runs
        before the `post_set_proxy_header_with_metadata` interceptor.
        """
        return response

    def post_set_proxy_header_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_proxy_header

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TargetSslProxies server but before it is returned to user code.

        We recommend only using this `post_set_proxy_header_with_metadata`
        interceptor in new development instead of the `post_set_proxy_header` interceptor.
        When both interceptors are used, this `post_set_proxy_header_with_metadata` interceptor runs after the
        `post_set_proxy_header` interceptor. The (possibly modified) response returned by
        `post_set_proxy_header` will be passed to
        `post_set_proxy_header_with_metadata`.
        """
        return response, metadata

    def pre_set_ssl_certificates(
        self,
        request: compute.SetSslCertificatesTargetSslProxyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.SetSslCertificatesTargetSslProxyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for set_ssl_certificates

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TargetSslProxies server.
        """
        return request, metadata

    def post_set_ssl_certificates(
        self, response: compute.Operation
    ) -> compute.Operation:
        """Post-rpc interceptor for set_ssl_certificates

        DEPRECATED. Please use the `post_set_ssl_certificates_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TargetSslProxies server but before
        it is returned to user code. This `post_set_ssl_certificates` interceptor runs
        before the `post_set_ssl_certificates_with_metadata` interceptor.
        """
        return response

    def post_set_ssl_certificates_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_ssl_certificates

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TargetSslProxies server but before it is returned to user code.

        We recommend only using this `post_set_ssl_certificates_with_metadata`
        interceptor in new development instead of the `post_set_ssl_certificates` interceptor.
        When both interceptors are used, this `post_set_ssl_certificates_with_metadata` interceptor runs after the
        `post_set_ssl_certificates` interceptor. The (possibly modified) response returned by
        `post_set_ssl_certificates` will be passed to
        `post_set_ssl_certificates_with_metadata`.
        """
        return response, metadata

    def pre_set_ssl_policy(
        self,
        request: compute.SetSslPolicyTargetSslProxyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.SetSslPolicyTargetSslProxyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for set_ssl_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TargetSslProxies server.
        """
        return request, metadata

    def post_set_ssl_policy(self, response: compute.Operation) -> compute.Operation:
        """Post-rpc interceptor for set_ssl_policy

        DEPRECATED. Please use the `post_set_ssl_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TargetSslProxies server but before
        it is returned to user code. This `post_set_ssl_policy` interceptor runs
        before the `post_set_ssl_policy_with_metadata` interceptor.
        """
        return response

    def post_set_ssl_policy_with_metadata(
        self,
        response: compute.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[compute.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for set_ssl_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TargetSslProxies server but before it is returned to user code.

        We recommend only using this `post_set_ssl_policy_with_metadata`
        interceptor in new development instead of the `post_set_ssl_policy` interceptor.
        When both interceptors are used, this `post_set_ssl_policy_with_metadata` interceptor runs after the
        `post_set_ssl_policy` interceptor. The (possibly modified) response returned by
        `post_set_ssl_policy` will be passed to
        `post_set_ssl_policy_with_metadata`.
        """
        return response, metadata

    def pre_test_iam_permissions(
        self,
        request: compute.TestIamPermissionsTargetSslProxyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.TestIamPermissionsTargetSslProxyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TargetSslProxies server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: compute.TestPermissionsResponse
    ) -> compute.TestPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        DEPRECATED. Please use the `post_test_iam_permissions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TargetSslProxies server but before
        it is returned to user code. This `post_test_iam_permissions` interceptor runs
        before the `post_test_iam_permissions_with_metadata` interceptor.
        """
        return response

    def post_test_iam_permissions_with_metadata(
        self,
        response: compute.TestPermissionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        compute.TestPermissionsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TargetSslProxies server but before it is returned to user code.

        We recommend only using this `post_test_iam_permissions_with_metadata`
        interceptor in new development instead of the `post_test_iam_permissions` interceptor.
        When both interceptors are used, this `post_test_iam_permissions_with_metadata` interceptor runs after the
        `post_test_iam_permissions` interceptor. The (possibly modified) response returned by
        `post_test_iam_permissions` will be passed to
        `post_test_iam_permissions_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class TargetSslProxiesRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: TargetSslProxiesRestInterceptor


class TargetSslProxiesRestTransport(_BaseTargetSslProxiesRestTransport):
    """REST backend synchronous transport for TargetSslProxies.

    The TargetSslProxies API.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "compute.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[TargetSslProxiesRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        NOTE: This REST transport functionality is currently in a beta
        state (preview). We welcome your feedback via a GitHub issue in
        this library's repository. Thank you!

         Args:
             host (Optional[str]):
                  The hostname to connect to (default: 'compute.googleapis.com').
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
             interceptor (Optional[TargetSslProxiesRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or TargetSslProxiesRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _Delete(
        _BaseTargetSslProxiesRestTransport._BaseDelete, TargetSslProxiesRestStub
    ):
        def __hash__(self):
            return hash("TargetSslProxiesRestTransport.Delete")

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
            request: compute.DeleteTargetSslProxyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the delete method over HTTP.

            Args:
                request (~.compute.DeleteTargetSslProxyRequest):
                    The request object. A request message for
                TargetSslProxies.Delete. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/beta/globalOperations>`__
                - `Regional </compute/docs/reference/rest/beta/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/beta/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = (
                _BaseTargetSslProxiesRestTransport._BaseDelete._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTargetSslProxiesRestTransport._BaseDelete,
                    "_BaseDelete__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1beta.TargetSslProxiesClient.Delete",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.TargetSslProxies",
                        "rpcName": "Delete",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TargetSslProxiesRestTransport._Delete._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1beta.TargetSslProxiesClient.delete",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.TargetSslProxies",
                        "rpcName": "Delete",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Get(_BaseTargetSslProxiesRestTransport._BaseGet, TargetSslProxiesRestStub):
        def __hash__(self):
            return hash("TargetSslProxiesRestTransport.Get")

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
            request: compute.GetTargetSslProxyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.TargetSslProxy:
            r"""Call the get method over HTTP.

            Args:
                request (~.compute.GetTargetSslProxyRequest):
                    The request object. A request message for
                TargetSslProxies.Get. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.TargetSslProxy:
                    Represents a Target SSL Proxy
                resource.
                A target SSL proxy is a component of a
                Proxy Network Load Balancer. The
                forwarding rule references the target
                SSL proxy, and the target proxy then
                references a backend service. For more
                information, readProxy Network Load
                Balancer overview.

            """

            http_options = (
                _BaseTargetSslProxiesRestTransport._BaseGet._get_http_options()
            )
            request, metadata = self._interceptor.pre_get(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTargetSslProxiesRestTransport._BaseGet,
                    "_BaseGet__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1beta.TargetSslProxiesClient.Get",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.TargetSslProxies",
                        "rpcName": "Get",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TargetSslProxiesRestTransport._Get._get_response(
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
            resp = compute.TargetSslProxy()
            pb_resp = compute.TargetSslProxy.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.TargetSslProxy.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1beta.TargetSslProxiesClient.get",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.TargetSslProxies",
                        "rpcName": "Get",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Insert(
        _BaseTargetSslProxiesRestTransport._BaseInsert, TargetSslProxiesRestStub
    ):
        def __hash__(self):
            return hash("TargetSslProxiesRestTransport.Insert")

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
            request: compute.InsertTargetSslProxyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the insert method over HTTP.

            Args:
                request (~.compute.InsertTargetSslProxyRequest):
                    The request object. A request message for
                TargetSslProxies.Insert. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/beta/globalOperations>`__
                - `Regional </compute/docs/reference/rest/beta/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/beta/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = (
                _BaseTargetSslProxiesRestTransport._BaseInsert._get_http_options()
            )
            request, metadata = self._interceptor.pre_insert(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTargetSslProxiesRestTransport._BaseInsert,
                    "_BaseInsert__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1beta.TargetSslProxiesClient.Insert",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.TargetSslProxies",
                        "rpcName": "Insert",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TargetSslProxiesRestTransport._Insert._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_insert(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_insert_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1beta.TargetSslProxiesClient.insert",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.TargetSslProxies",
                        "rpcName": "Insert",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _List(_BaseTargetSslProxiesRestTransport._BaseList, TargetSslProxiesRestStub):
        def __hash__(self):
            return hash("TargetSslProxiesRestTransport.List")

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
            request: compute.ListTargetSslProxiesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.TargetSslProxyList:
            r"""Call the list method over HTTP.

            Args:
                request (~.compute.ListTargetSslProxiesRequest):
                    The request object. A request message for
                TargetSslProxies.List. See the method
                description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.TargetSslProxyList:
                    Contains a list of TargetSslProxy
                resources.

            """

            http_options = (
                _BaseTargetSslProxiesRestTransport._BaseList._get_http_options()
            )
            request, metadata = self._interceptor.pre_list(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTargetSslProxiesRestTransport._BaseList,
                    "_BaseList__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1beta.TargetSslProxiesClient.List",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.TargetSslProxies",
                        "rpcName": "List",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TargetSslProxiesRestTransport._List._get_response(
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
            resp = compute.TargetSslProxyList()
            pb_resp = compute.TargetSslProxyList.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.TargetSslProxyList.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1beta.TargetSslProxiesClient.list",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.TargetSslProxies",
                        "rpcName": "List",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetBackendService(
        _BaseTargetSslProxiesRestTransport._BaseSetBackendService,
        TargetSslProxiesRestStub,
    ):
        def __hash__(self):
            return hash("TargetSslProxiesRestTransport.SetBackendService")

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
            request: compute.SetBackendServiceTargetSslProxyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the set backend service method over HTTP.

            Args:
                request (~.compute.SetBackendServiceTargetSslProxyRequest):
                    The request object. A request message for
                TargetSslProxies.SetBackendService. See
                the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/beta/globalOperations>`__
                - `Regional </compute/docs/reference/rest/beta/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/beta/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = _BaseTargetSslProxiesRestTransport._BaseSetBackendService._get_http_options()
            request, metadata = self._interceptor.pre_set_backend_service(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTargetSslProxiesRestTransport._BaseSetBackendService,
                    "_BaseSetBackendService__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1beta.TargetSslProxiesClient.SetBackendService",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.TargetSslProxies",
                        "rpcName": "SetBackendService",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TargetSslProxiesRestTransport._SetBackendService._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_backend_service(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_backend_service_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1beta.TargetSslProxiesClient.set_backend_service",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.TargetSslProxies",
                        "rpcName": "SetBackendService",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetCertificateMap(
        _BaseTargetSslProxiesRestTransport._BaseSetCertificateMap,
        TargetSslProxiesRestStub,
    ):
        def __hash__(self):
            return hash("TargetSslProxiesRestTransport.SetCertificateMap")

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
            request: compute.SetCertificateMapTargetSslProxyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the set certificate map method over HTTP.

            Args:
                request (~.compute.SetCertificateMapTargetSslProxyRequest):
                    The request object. A request message for
                TargetSslProxies.SetCertificateMap. See
                the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/beta/globalOperations>`__
                - `Regional </compute/docs/reference/rest/beta/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/beta/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = _BaseTargetSslProxiesRestTransport._BaseSetCertificateMap._get_http_options()
            request, metadata = self._interceptor.pre_set_certificate_map(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTargetSslProxiesRestTransport._BaseSetCertificateMap,
                    "_BaseSetCertificateMap__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1beta.TargetSslProxiesClient.SetCertificateMap",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.TargetSslProxies",
                        "rpcName": "SetCertificateMap",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TargetSslProxiesRestTransport._SetCertificateMap._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_certificate_map(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_certificate_map_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1beta.TargetSslProxiesClient.set_certificate_map",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.TargetSslProxies",
                        "rpcName": "SetCertificateMap",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetProxyHeader(
        _BaseTargetSslProxiesRestTransport._BaseSetProxyHeader, TargetSslProxiesRestStub
    ):
        def __hash__(self):
            return hash("TargetSslProxiesRestTransport.SetProxyHeader")

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
            request: compute.SetProxyHeaderTargetSslProxyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the set proxy header method over HTTP.

            Args:
                request (~.compute.SetProxyHeaderTargetSslProxyRequest):
                    The request object. A request message for
                TargetSslProxies.SetProxyHeader. See the
                method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/beta/globalOperations>`__
                - `Regional </compute/docs/reference/rest/beta/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/beta/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = _BaseTargetSslProxiesRestTransport._BaseSetProxyHeader._get_http_options()
            request, metadata = self._interceptor.pre_set_proxy_header(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTargetSslProxiesRestTransport._BaseSetProxyHeader,
                    "_BaseSetProxyHeader__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1beta.TargetSslProxiesClient.SetProxyHeader",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.TargetSslProxies",
                        "rpcName": "SetProxyHeader",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TargetSslProxiesRestTransport._SetProxyHeader._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_proxy_header(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_proxy_header_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1beta.TargetSslProxiesClient.set_proxy_header",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.TargetSslProxies",
                        "rpcName": "SetProxyHeader",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetSslCertificates(
        _BaseTargetSslProxiesRestTransport._BaseSetSslCertificates,
        TargetSslProxiesRestStub,
    ):
        def __hash__(self):
            return hash("TargetSslProxiesRestTransport.SetSslCertificates")

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
            request: compute.SetSslCertificatesTargetSslProxyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the set ssl certificates method over HTTP.

            Args:
                request (~.compute.SetSslCertificatesTargetSslProxyRequest):
                    The request object. A request message for
                TargetSslProxies.SetSslCertificates. See
                the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/beta/globalOperations>`__
                - `Regional </compute/docs/reference/rest/beta/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/beta/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = _BaseTargetSslProxiesRestTransport._BaseSetSslCertificates._get_http_options()
            request, metadata = self._interceptor.pre_set_ssl_certificates(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTargetSslProxiesRestTransport._BaseSetSslCertificates,
                    "_BaseSetSslCertificates__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1beta.TargetSslProxiesClient.SetSslCertificates",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.TargetSslProxies",
                        "rpcName": "SetSslCertificates",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TargetSslProxiesRestTransport._SetSslCertificates._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_ssl_certificates(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_ssl_certificates_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1beta.TargetSslProxiesClient.set_ssl_certificates",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.TargetSslProxies",
                        "rpcName": "SetSslCertificates",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SetSslPolicy(
        _BaseTargetSslProxiesRestTransport._BaseSetSslPolicy, TargetSslProxiesRestStub
    ):
        def __hash__(self):
            return hash("TargetSslProxiesRestTransport.SetSslPolicy")

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
            request: compute.SetSslPolicyTargetSslProxyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.Operation:
            r"""Call the set ssl policy method over HTTP.

            Args:
                request (~.compute.SetSslPolicyTargetSslProxyRequest):
                    The request object. A request message for
                TargetSslProxies.SetSslPolicy. See the
                method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.Operation:
                    Represents an Operation resource.

                Google Compute Engine has three Operation resources:

                - `Global </compute/docs/reference/rest/beta/globalOperations>`__
                - `Regional </compute/docs/reference/rest/beta/regionOperations>`__
                - `Zonal </compute/docs/reference/rest/beta/zoneOperations>`__

                You can use an operation resource to manage asynchronous
                API requests. For more information, readHandling API
                responses.

                Operations can be global, regional or zonal.

                ::

                   - For global operations, use the `globalOperations`
                   resource.
                   - For regional operations, use the
                   `regionOperations` resource.
                   - For zonal operations, use
                   the `zoneOperations` resource.

                For more information, read Global, Regional, and Zonal
                Resources.

                Note that completed Operation resources have a limited
                retention period.

            """

            http_options = (
                _BaseTargetSslProxiesRestTransport._BaseSetSslPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_ssl_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTargetSslProxiesRestTransport._BaseSetSslPolicy,
                    "_BaseSetSslPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1beta.TargetSslProxiesClient.SetSslPolicy",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.TargetSslProxies",
                        "rpcName": "SetSslPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TargetSslProxiesRestTransport._SetSslPolicy._get_response(
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
            resp = compute.Operation()
            pb_resp = compute.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_set_ssl_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_set_ssl_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1beta.TargetSslProxiesClient.set_ssl_policy",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.TargetSslProxies",
                        "rpcName": "SetSslPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _TestIamPermissions(
        _BaseTargetSslProxiesRestTransport._BaseTestIamPermissions,
        TargetSslProxiesRestStub,
    ):
        def __hash__(self):
            return hash("TargetSslProxiesRestTransport.TestIamPermissions")

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
            request: compute.TestIamPermissionsTargetSslProxyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> compute.TestPermissionsResponse:
            r"""Call the test iam permissions method over HTTP.

            Args:
                request (~.compute.TestIamPermissionsTargetSslProxyRequest):
                    The request object. A request message for
                TargetSslProxies.TestIamPermissions. See
                the method description for details.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.compute.TestPermissionsResponse:

            """

            http_options = _BaseTargetSslProxiesRestTransport._BaseTestIamPermissions._get_http_options()
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTargetSslProxiesRestTransport._BaseTestIamPermissions,
                    "_BaseTestIamPermissions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.compute_v1beta.TargetSslProxiesClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.TargetSslProxies",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TargetSslProxiesRestTransport._TestIamPermissions._get_response(
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
            resp = compute.TestPermissionsResponse()
            pb_resp = compute.TestPermissionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_test_iam_permissions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_test_iam_permissions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = compute.TestPermissionsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.compute_v1beta.TargetSslProxiesClient.test_iam_permissions",
                    extra={
                        "serviceName": "google.cloud.compute.v1beta.TargetSslProxies",
                        "rpcName": "TestIamPermissions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def delete(
        self,
    ) -> Callable[[compute.DeleteTargetSslProxyRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Delete(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get(
        self,
    ) -> Callable[[compute.GetTargetSslProxyRequest], compute.TargetSslProxy]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Get(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def insert(
        self,
    ) -> Callable[[compute.InsertTargetSslProxyRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Insert(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list(
        self,
    ) -> Callable[[compute.ListTargetSslProxiesRequest], compute.TargetSslProxyList]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._List(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_backend_service(
        self,
    ) -> Callable[[compute.SetBackendServiceTargetSslProxyRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetBackendService(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_certificate_map(
        self,
    ) -> Callable[[compute.SetCertificateMapTargetSslProxyRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetCertificateMap(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_proxy_header(
        self,
    ) -> Callable[[compute.SetProxyHeaderTargetSslProxyRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetProxyHeader(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_ssl_certificates(
        self,
    ) -> Callable[[compute.SetSslCertificatesTargetSslProxyRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetSslCertificates(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def set_ssl_policy(
        self,
    ) -> Callable[[compute.SetSslPolicyTargetSslProxyRequest], compute.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SetSslPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def test_iam_permissions(
        self,
    ) -> Callable[
        [compute.TestIamPermissionsTargetSslProxyRequest],
        compute.TestPermissionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._TestIamPermissions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("TargetSslProxiesRestTransport",)
