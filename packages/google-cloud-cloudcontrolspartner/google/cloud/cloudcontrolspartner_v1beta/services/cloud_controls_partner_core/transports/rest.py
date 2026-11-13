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

from google.cloud.cloudcontrolspartner_v1beta._compat import transcode_request
from google.cloud.cloudcontrolspartner_v1beta.types import (
    access_approval_requests,
    customer_workloads,
    customers,
    ekm_connections,
    partner_permissions,
    partners,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseCloudControlsPartnerCoreRestTransport

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


class CloudControlsPartnerCoreRestInterceptor:
    """Interceptor for CloudControlsPartnerCore.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the CloudControlsPartnerCoreRestTransport.

    .. code-block:: python
        class MyCustomCloudControlsPartnerCoreInterceptor(CloudControlsPartnerCoreRestInterceptor):
            def pre_create_customer(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_customer(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_customer(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_customer(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_customer(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_ekm_connections(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_ekm_connections(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_partner(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_partner(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_partner_permissions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_partner_permissions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_workload(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_workload(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_access_approval_requests(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_access_approval_requests(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_customers(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_customers(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_workloads(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_workloads(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_customer(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_customer(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = CloudControlsPartnerCoreRestTransport(interceptor=MyCustomCloudControlsPartnerCoreInterceptor())
        client = CloudControlsPartnerCoreClient(transport=transport)


    """

    def pre_create_customer(
        self,
        request: customers.CreateCustomerRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        customers.CreateCustomerRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_customer

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudControlsPartnerCore server.
        """
        return request, metadata

    def post_create_customer(self, response: customers.Customer) -> customers.Customer:
        """Post-rpc interceptor for create_customer

        DEPRECATED. Please use the `post_create_customer_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudControlsPartnerCore server but before
        it is returned to user code. This `post_create_customer` interceptor runs
        before the `post_create_customer_with_metadata` interceptor.
        """
        return response

    def post_create_customer_with_metadata(
        self,
        response: customers.Customer,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[customers.Customer, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_customer

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudControlsPartnerCore server but before it is returned to user code.

        We recommend only using this `post_create_customer_with_metadata`
        interceptor in new development instead of the `post_create_customer` interceptor.
        When both interceptors are used, this `post_create_customer_with_metadata` interceptor runs after the
        `post_create_customer` interceptor. The (possibly modified) response returned by
        `post_create_customer` will be passed to
        `post_create_customer_with_metadata`.
        """
        return response, metadata

    def pre_delete_customer(
        self,
        request: customers.DeleteCustomerRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        customers.DeleteCustomerRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_customer

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudControlsPartnerCore server.
        """
        return request, metadata

    def pre_get_customer(
        self,
        request: customers.GetCustomerRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[customers.GetCustomerRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_customer

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudControlsPartnerCore server.
        """
        return request, metadata

    def post_get_customer(self, response: customers.Customer) -> customers.Customer:
        """Post-rpc interceptor for get_customer

        DEPRECATED. Please use the `post_get_customer_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudControlsPartnerCore server but before
        it is returned to user code. This `post_get_customer` interceptor runs
        before the `post_get_customer_with_metadata` interceptor.
        """
        return response

    def post_get_customer_with_metadata(
        self,
        response: customers.Customer,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[customers.Customer, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_customer

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudControlsPartnerCore server but before it is returned to user code.

        We recommend only using this `post_get_customer_with_metadata`
        interceptor in new development instead of the `post_get_customer` interceptor.
        When both interceptors are used, this `post_get_customer_with_metadata` interceptor runs after the
        `post_get_customer` interceptor. The (possibly modified) response returned by
        `post_get_customer` will be passed to
        `post_get_customer_with_metadata`.
        """
        return response, metadata

    def pre_get_ekm_connections(
        self,
        request: ekm_connections.GetEkmConnectionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ekm_connections.GetEkmConnectionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_ekm_connections

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudControlsPartnerCore server.
        """
        return request, metadata

    def post_get_ekm_connections(
        self, response: ekm_connections.EkmConnections
    ) -> ekm_connections.EkmConnections:
        """Post-rpc interceptor for get_ekm_connections

        DEPRECATED. Please use the `post_get_ekm_connections_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudControlsPartnerCore server but before
        it is returned to user code. This `post_get_ekm_connections` interceptor runs
        before the `post_get_ekm_connections_with_metadata` interceptor.
        """
        return response

    def post_get_ekm_connections_with_metadata(
        self,
        response: ekm_connections.EkmConnections,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[ekm_connections.EkmConnections, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_ekm_connections

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudControlsPartnerCore server but before it is returned to user code.

        We recommend only using this `post_get_ekm_connections_with_metadata`
        interceptor in new development instead of the `post_get_ekm_connections` interceptor.
        When both interceptors are used, this `post_get_ekm_connections_with_metadata` interceptor runs after the
        `post_get_ekm_connections` interceptor. The (possibly modified) response returned by
        `post_get_ekm_connections` will be passed to
        `post_get_ekm_connections_with_metadata`.
        """
        return response, metadata

    def pre_get_partner(
        self,
        request: partners.GetPartnerRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[partners.GetPartnerRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_partner

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudControlsPartnerCore server.
        """
        return request, metadata

    def post_get_partner(self, response: partners.Partner) -> partners.Partner:
        """Post-rpc interceptor for get_partner

        DEPRECATED. Please use the `post_get_partner_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudControlsPartnerCore server but before
        it is returned to user code. This `post_get_partner` interceptor runs
        before the `post_get_partner_with_metadata` interceptor.
        """
        return response

    def post_get_partner_with_metadata(
        self,
        response: partners.Partner,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[partners.Partner, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_partner

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudControlsPartnerCore server but before it is returned to user code.

        We recommend only using this `post_get_partner_with_metadata`
        interceptor in new development instead of the `post_get_partner` interceptor.
        When both interceptors are used, this `post_get_partner_with_metadata` interceptor runs after the
        `post_get_partner` interceptor. The (possibly modified) response returned by
        `post_get_partner` will be passed to
        `post_get_partner_with_metadata`.
        """
        return response, metadata

    def pre_get_partner_permissions(
        self,
        request: partner_permissions.GetPartnerPermissionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        partner_permissions.GetPartnerPermissionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_partner_permissions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudControlsPartnerCore server.
        """
        return request, metadata

    def post_get_partner_permissions(
        self, response: partner_permissions.PartnerPermissions
    ) -> partner_permissions.PartnerPermissions:
        """Post-rpc interceptor for get_partner_permissions

        DEPRECATED. Please use the `post_get_partner_permissions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudControlsPartnerCore server but before
        it is returned to user code. This `post_get_partner_permissions` interceptor runs
        before the `post_get_partner_permissions_with_metadata` interceptor.
        """
        return response

    def post_get_partner_permissions_with_metadata(
        self,
        response: partner_permissions.PartnerPermissions,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        partner_permissions.PartnerPermissions, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_partner_permissions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudControlsPartnerCore server but before it is returned to user code.

        We recommend only using this `post_get_partner_permissions_with_metadata`
        interceptor in new development instead of the `post_get_partner_permissions` interceptor.
        When both interceptors are used, this `post_get_partner_permissions_with_metadata` interceptor runs after the
        `post_get_partner_permissions` interceptor. The (possibly modified) response returned by
        `post_get_partner_permissions` will be passed to
        `post_get_partner_permissions_with_metadata`.
        """
        return response, metadata

    def pre_get_workload(
        self,
        request: customer_workloads.GetWorkloadRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        customer_workloads.GetWorkloadRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_workload

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudControlsPartnerCore server.
        """
        return request, metadata

    def post_get_workload(
        self, response: customer_workloads.Workload
    ) -> customer_workloads.Workload:
        """Post-rpc interceptor for get_workload

        DEPRECATED. Please use the `post_get_workload_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudControlsPartnerCore server but before
        it is returned to user code. This `post_get_workload` interceptor runs
        before the `post_get_workload_with_metadata` interceptor.
        """
        return response

    def post_get_workload_with_metadata(
        self,
        response: customer_workloads.Workload,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[customer_workloads.Workload, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_workload

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudControlsPartnerCore server but before it is returned to user code.

        We recommend only using this `post_get_workload_with_metadata`
        interceptor in new development instead of the `post_get_workload` interceptor.
        When both interceptors are used, this `post_get_workload_with_metadata` interceptor runs after the
        `post_get_workload` interceptor. The (possibly modified) response returned by
        `post_get_workload` will be passed to
        `post_get_workload_with_metadata`.
        """
        return response, metadata

    def pre_list_access_approval_requests(
        self,
        request: access_approval_requests.ListAccessApprovalRequestsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        access_approval_requests.ListAccessApprovalRequestsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_access_approval_requests

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudControlsPartnerCore server.
        """
        return request, metadata

    def post_list_access_approval_requests(
        self, response: access_approval_requests.ListAccessApprovalRequestsResponse
    ) -> access_approval_requests.ListAccessApprovalRequestsResponse:
        """Post-rpc interceptor for list_access_approval_requests

        DEPRECATED. Please use the `post_list_access_approval_requests_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudControlsPartnerCore server but before
        it is returned to user code. This `post_list_access_approval_requests` interceptor runs
        before the `post_list_access_approval_requests_with_metadata` interceptor.
        """
        return response

    def post_list_access_approval_requests_with_metadata(
        self,
        response: access_approval_requests.ListAccessApprovalRequestsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        access_approval_requests.ListAccessApprovalRequestsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_access_approval_requests

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudControlsPartnerCore server but before it is returned to user code.

        We recommend only using this `post_list_access_approval_requests_with_metadata`
        interceptor in new development instead of the `post_list_access_approval_requests` interceptor.
        When both interceptors are used, this `post_list_access_approval_requests_with_metadata` interceptor runs after the
        `post_list_access_approval_requests` interceptor. The (possibly modified) response returned by
        `post_list_access_approval_requests` will be passed to
        `post_list_access_approval_requests_with_metadata`.
        """
        return response, metadata

    def pre_list_customers(
        self,
        request: customers.ListCustomersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[customers.ListCustomersRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_customers

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudControlsPartnerCore server.
        """
        return request, metadata

    def post_list_customers(
        self, response: customers.ListCustomersResponse
    ) -> customers.ListCustomersResponse:
        """Post-rpc interceptor for list_customers

        DEPRECATED. Please use the `post_list_customers_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudControlsPartnerCore server but before
        it is returned to user code. This `post_list_customers` interceptor runs
        before the `post_list_customers_with_metadata` interceptor.
        """
        return response

    def post_list_customers_with_metadata(
        self,
        response: customers.ListCustomersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        customers.ListCustomersResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_customers

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudControlsPartnerCore server but before it is returned to user code.

        We recommend only using this `post_list_customers_with_metadata`
        interceptor in new development instead of the `post_list_customers` interceptor.
        When both interceptors are used, this `post_list_customers_with_metadata` interceptor runs after the
        `post_list_customers` interceptor. The (possibly modified) response returned by
        `post_list_customers` will be passed to
        `post_list_customers_with_metadata`.
        """
        return response, metadata

    def pre_list_workloads(
        self,
        request: customer_workloads.ListWorkloadsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        customer_workloads.ListWorkloadsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_workloads

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudControlsPartnerCore server.
        """
        return request, metadata

    def post_list_workloads(
        self, response: customer_workloads.ListWorkloadsResponse
    ) -> customer_workloads.ListWorkloadsResponse:
        """Post-rpc interceptor for list_workloads

        DEPRECATED. Please use the `post_list_workloads_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudControlsPartnerCore server but before
        it is returned to user code. This `post_list_workloads` interceptor runs
        before the `post_list_workloads_with_metadata` interceptor.
        """
        return response

    def post_list_workloads_with_metadata(
        self,
        response: customer_workloads.ListWorkloadsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        customer_workloads.ListWorkloadsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_workloads

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudControlsPartnerCore server but before it is returned to user code.

        We recommend only using this `post_list_workloads_with_metadata`
        interceptor in new development instead of the `post_list_workloads` interceptor.
        When both interceptors are used, this `post_list_workloads_with_metadata` interceptor runs after the
        `post_list_workloads` interceptor. The (possibly modified) response returned by
        `post_list_workloads` will be passed to
        `post_list_workloads_with_metadata`.
        """
        return response, metadata

    def pre_update_customer(
        self,
        request: customers.UpdateCustomerRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        customers.UpdateCustomerRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_customer

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudControlsPartnerCore server.
        """
        return request, metadata

    def post_update_customer(self, response: customers.Customer) -> customers.Customer:
        """Post-rpc interceptor for update_customer

        DEPRECATED. Please use the `post_update_customer_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudControlsPartnerCore server but before
        it is returned to user code. This `post_update_customer` interceptor runs
        before the `post_update_customer_with_metadata` interceptor.
        """
        return response

    def post_update_customer_with_metadata(
        self,
        response: customers.Customer,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[customers.Customer, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_customer

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudControlsPartnerCore server but before it is returned to user code.

        We recommend only using this `post_update_customer_with_metadata`
        interceptor in new development instead of the `post_update_customer` interceptor.
        When both interceptors are used, this `post_update_customer_with_metadata` interceptor runs after the
        `post_update_customer` interceptor. The (possibly modified) response returned by
        `post_update_customer` will be passed to
        `post_update_customer_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class CloudControlsPartnerCoreRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: CloudControlsPartnerCoreRestInterceptor


class CloudControlsPartnerCoreRestTransport(_BaseCloudControlsPartnerCoreRestTransport):
    """REST backend synchronous transport for CloudControlsPartnerCore.

    Service describing handlers for resources

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "cloudcontrolspartner.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[CloudControlsPartnerCoreRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'cloudcontrolspartner.googleapis.com').
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
            interceptor (Optional[CloudControlsPartnerCoreRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or CloudControlsPartnerCoreRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateCustomer(
        _BaseCloudControlsPartnerCoreRestTransport._BaseCreateCustomer,
        CloudControlsPartnerCoreRestStub,
    ):
        def __hash__(self):
            return hash("CloudControlsPartnerCoreRestTransport.CreateCustomer")

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
            request: customers.CreateCustomerRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> customers.Customer:
            r"""Call the create customer method over HTTP.

            Args:
                request (~.customers.CreateCustomerRequest):
                    The request object. Request to create a customer
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.customers.Customer:
                    Contains metadata around a Cloud
                Controls Partner Customer

            """

            http_options = _BaseCloudControlsPartnerCoreRestTransport._BaseCreateCustomer._get_http_options()
            request, metadata = self._interceptor.pre_create_customer(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudControlsPartnerCoreRestTransport._BaseCreateCustomer,
                    "_BaseCreateCustomer__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.cloudcontrolspartner_v1beta.CloudControlsPartnerCoreClient.CreateCustomer",
                    extra={
                        "serviceName": "google.cloud.cloudcontrolspartner.v1beta.CloudControlsPartnerCore",
                        "rpcName": "CreateCustomer",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CloudControlsPartnerCoreRestTransport._CreateCustomer._get_response(
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
            resp = customers.Customer()
            pb_resp = customers.Customer.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_customer(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_customer_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = customers.Customer.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.cloudcontrolspartner_v1beta.CloudControlsPartnerCoreClient.create_customer",
                    extra={
                        "serviceName": "google.cloud.cloudcontrolspartner.v1beta.CloudControlsPartnerCore",
                        "rpcName": "CreateCustomer",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteCustomer(
        _BaseCloudControlsPartnerCoreRestTransport._BaseDeleteCustomer,
        CloudControlsPartnerCoreRestStub,
    ):
        def __hash__(self):
            return hash("CloudControlsPartnerCoreRestTransport.DeleteCustomer")

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
            request: customers.DeleteCustomerRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete customer method over HTTP.

            Args:
                request (~.customers.DeleteCustomerRequest):
                    The request object. Message for deleting customer
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseCloudControlsPartnerCoreRestTransport._BaseDeleteCustomer._get_http_options()
            request, metadata = self._interceptor.pre_delete_customer(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudControlsPartnerCoreRestTransport._BaseDeleteCustomer,
                    "_BaseDeleteCustomer__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.cloudcontrolspartner_v1beta.CloudControlsPartnerCoreClient.DeleteCustomer",
                    extra={
                        "serviceName": "google.cloud.cloudcontrolspartner.v1beta.CloudControlsPartnerCore",
                        "rpcName": "DeleteCustomer",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CloudControlsPartnerCoreRestTransport._DeleteCustomer._get_response(
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

    class _GetCustomer(
        _BaseCloudControlsPartnerCoreRestTransport._BaseGetCustomer,
        CloudControlsPartnerCoreRestStub,
    ):
        def __hash__(self):
            return hash("CloudControlsPartnerCoreRestTransport.GetCustomer")

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
            request: customers.GetCustomerRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> customers.Customer:
            r"""Call the get customer method over HTTP.

            Args:
                request (~.customers.GetCustomerRequest):
                    The request object. Message for getting a customer
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.customers.Customer:
                    Contains metadata around a Cloud
                Controls Partner Customer

            """

            http_options = _BaseCloudControlsPartnerCoreRestTransport._BaseGetCustomer._get_http_options()
            request, metadata = self._interceptor.pre_get_customer(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudControlsPartnerCoreRestTransport._BaseGetCustomer,
                    "_BaseGetCustomer__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.cloudcontrolspartner_v1beta.CloudControlsPartnerCoreClient.GetCustomer",
                    extra={
                        "serviceName": "google.cloud.cloudcontrolspartner.v1beta.CloudControlsPartnerCore",
                        "rpcName": "GetCustomer",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudControlsPartnerCoreRestTransport._GetCustomer._get_response(
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
            resp = customers.Customer()
            pb_resp = customers.Customer.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_customer(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_customer_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = customers.Customer.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.cloudcontrolspartner_v1beta.CloudControlsPartnerCoreClient.get_customer",
                    extra={
                        "serviceName": "google.cloud.cloudcontrolspartner.v1beta.CloudControlsPartnerCore",
                        "rpcName": "GetCustomer",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetEkmConnections(
        _BaseCloudControlsPartnerCoreRestTransport._BaseGetEkmConnections,
        CloudControlsPartnerCoreRestStub,
    ):
        def __hash__(self):
            return hash("CloudControlsPartnerCoreRestTransport.GetEkmConnections")

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
            request: ekm_connections.GetEkmConnectionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ekm_connections.EkmConnections:
            r"""Call the get ekm connections method over HTTP.

            Args:
                request (~.ekm_connections.GetEkmConnectionsRequest):
                    The request object. Request for getting the EKM
                connections associated with a workload
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ekm_connections.EkmConnections:
                    The EKM connections associated with a
                workload

            """

            http_options = _BaseCloudControlsPartnerCoreRestTransport._BaseGetEkmConnections._get_http_options()
            request, metadata = self._interceptor.pre_get_ekm_connections(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudControlsPartnerCoreRestTransport._BaseGetEkmConnections,
                    "_BaseGetEkmConnections__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.cloudcontrolspartner_v1beta.CloudControlsPartnerCoreClient.GetEkmConnections",
                    extra={
                        "serviceName": "google.cloud.cloudcontrolspartner.v1beta.CloudControlsPartnerCore",
                        "rpcName": "GetEkmConnections",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CloudControlsPartnerCoreRestTransport._GetEkmConnections._get_response(
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

            # Return the response
            resp = ekm_connections.EkmConnections()
            pb_resp = ekm_connections.EkmConnections.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_ekm_connections(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_ekm_connections_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ekm_connections.EkmConnections.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.cloudcontrolspartner_v1beta.CloudControlsPartnerCoreClient.get_ekm_connections",
                    extra={
                        "serviceName": "google.cloud.cloudcontrolspartner.v1beta.CloudControlsPartnerCore",
                        "rpcName": "GetEkmConnections",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetPartner(
        _BaseCloudControlsPartnerCoreRestTransport._BaseGetPartner,
        CloudControlsPartnerCoreRestStub,
    ):
        def __hash__(self):
            return hash("CloudControlsPartnerCoreRestTransport.GetPartner")

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
            request: partners.GetPartnerRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> partners.Partner:
            r"""Call the get partner method over HTTP.

            Args:
                request (~.partners.GetPartnerRequest):
                    The request object. Message for getting a Partner
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.partners.Partner:
                    Message describing Partner resource
            """

            http_options = _BaseCloudControlsPartnerCoreRestTransport._BaseGetPartner._get_http_options()
            request, metadata = self._interceptor.pre_get_partner(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudControlsPartnerCoreRestTransport._BaseGetPartner,
                    "_BaseGetPartner__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.cloudcontrolspartner_v1beta.CloudControlsPartnerCoreClient.GetPartner",
                    extra={
                        "serviceName": "google.cloud.cloudcontrolspartner.v1beta.CloudControlsPartnerCore",
                        "rpcName": "GetPartner",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudControlsPartnerCoreRestTransport._GetPartner._get_response(
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
            resp = partners.Partner()
            pb_resp = partners.Partner.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_partner(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_partner_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = partners.Partner.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.cloudcontrolspartner_v1beta.CloudControlsPartnerCoreClient.get_partner",
                    extra={
                        "serviceName": "google.cloud.cloudcontrolspartner.v1beta.CloudControlsPartnerCore",
                        "rpcName": "GetPartner",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetPartnerPermissions(
        _BaseCloudControlsPartnerCoreRestTransport._BaseGetPartnerPermissions,
        CloudControlsPartnerCoreRestStub,
    ):
        def __hash__(self):
            return hash("CloudControlsPartnerCoreRestTransport.GetPartnerPermissions")

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
            request: partner_permissions.GetPartnerPermissionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> partner_permissions.PartnerPermissions:
            r"""Call the get partner permissions method over HTTP.

            Args:
                request (~.partner_permissions.GetPartnerPermissionsRequest):
                    The request object. Request for getting the partner
                permissions granted for a workload
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.partner_permissions.PartnerPermissions:
                    The permissions granted to the
                partner for a workload

            """

            http_options = _BaseCloudControlsPartnerCoreRestTransport._BaseGetPartnerPermissions._get_http_options()
            request, metadata = self._interceptor.pre_get_partner_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudControlsPartnerCoreRestTransport._BaseGetPartnerPermissions,
                    "_BaseGetPartnerPermissions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.cloudcontrolspartner_v1beta.CloudControlsPartnerCoreClient.GetPartnerPermissions",
                    extra={
                        "serviceName": "google.cloud.cloudcontrolspartner.v1beta.CloudControlsPartnerCore",
                        "rpcName": "GetPartnerPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudControlsPartnerCoreRestTransport._GetPartnerPermissions._get_response(
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
            resp = partner_permissions.PartnerPermissions()
            pb_resp = partner_permissions.PartnerPermissions.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_partner_permissions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_partner_permissions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = partner_permissions.PartnerPermissions.to_json(
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
                    "Received response for google.cloud.cloudcontrolspartner_v1beta.CloudControlsPartnerCoreClient.get_partner_permissions",
                    extra={
                        "serviceName": "google.cloud.cloudcontrolspartner.v1beta.CloudControlsPartnerCore",
                        "rpcName": "GetPartnerPermissions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetWorkload(
        _BaseCloudControlsPartnerCoreRestTransport._BaseGetWorkload,
        CloudControlsPartnerCoreRestStub,
    ):
        def __hash__(self):
            return hash("CloudControlsPartnerCoreRestTransport.GetWorkload")

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
            request: customer_workloads.GetWorkloadRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> customer_workloads.Workload:
            r"""Call the get workload method over HTTP.

            Args:
                request (~.customer_workloads.GetWorkloadRequest):
                    The request object. Message for getting a customer
                workload.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.customer_workloads.Workload:
                    Contains metadata around the `Workload
                resource <https://cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/Workload>`__
                in the Assured Workloads API.

            """

            http_options = _BaseCloudControlsPartnerCoreRestTransport._BaseGetWorkload._get_http_options()
            request, metadata = self._interceptor.pre_get_workload(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudControlsPartnerCoreRestTransport._BaseGetWorkload,
                    "_BaseGetWorkload__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.cloudcontrolspartner_v1beta.CloudControlsPartnerCoreClient.GetWorkload",
                    extra={
                        "serviceName": "google.cloud.cloudcontrolspartner.v1beta.CloudControlsPartnerCore",
                        "rpcName": "GetWorkload",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudControlsPartnerCoreRestTransport._GetWorkload._get_response(
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
            resp = customer_workloads.Workload()
            pb_resp = customer_workloads.Workload.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_workload(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_workload_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = customer_workloads.Workload.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.cloudcontrolspartner_v1beta.CloudControlsPartnerCoreClient.get_workload",
                    extra={
                        "serviceName": "google.cloud.cloudcontrolspartner.v1beta.CloudControlsPartnerCore",
                        "rpcName": "GetWorkload",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAccessApprovalRequests(
        _BaseCloudControlsPartnerCoreRestTransport._BaseListAccessApprovalRequests,
        CloudControlsPartnerCoreRestStub,
    ):
        def __hash__(self):
            return hash(
                "CloudControlsPartnerCoreRestTransport.ListAccessApprovalRequests"
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
            request: access_approval_requests.ListAccessApprovalRequestsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> access_approval_requests.ListAccessApprovalRequestsResponse:
            r"""Call the list access approval
            requests method over HTTP.

                Args:
                    request (~.access_approval_requests.ListAccessApprovalRequestsRequest):
                        The request object. Request for getting the access
                    requests associated with a workload.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.access_approval_requests.ListAccessApprovalRequestsResponse:
                        Response message for list access
                    requests.

            """

            http_options = _BaseCloudControlsPartnerCoreRestTransport._BaseListAccessApprovalRequests._get_http_options()
            request, metadata = self._interceptor.pre_list_access_approval_requests(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudControlsPartnerCoreRestTransport._BaseListAccessApprovalRequests,
                    "_BaseListAccessApprovalRequests__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.cloudcontrolspartner_v1beta.CloudControlsPartnerCoreClient.ListAccessApprovalRequests",
                    extra={
                        "serviceName": "google.cloud.cloudcontrolspartner.v1beta.CloudControlsPartnerCore",
                        "rpcName": "ListAccessApprovalRequests",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = CloudControlsPartnerCoreRestTransport._ListAccessApprovalRequests._get_response(
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
            resp = access_approval_requests.ListAccessApprovalRequestsResponse()
            pb_resp = access_approval_requests.ListAccessApprovalRequestsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_access_approval_requests(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_access_approval_requests_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = access_approval_requests.ListAccessApprovalRequestsResponse.to_json(
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
                    "Received response for google.cloud.cloudcontrolspartner_v1beta.CloudControlsPartnerCoreClient.list_access_approval_requests",
                    extra={
                        "serviceName": "google.cloud.cloudcontrolspartner.v1beta.CloudControlsPartnerCore",
                        "rpcName": "ListAccessApprovalRequests",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListCustomers(
        _BaseCloudControlsPartnerCoreRestTransport._BaseListCustomers,
        CloudControlsPartnerCoreRestStub,
    ):
        def __hash__(self):
            return hash("CloudControlsPartnerCoreRestTransport.ListCustomers")

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
            request: customers.ListCustomersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> customers.ListCustomersResponse:
            r"""Call the list customers method over HTTP.

            Args:
                request (~.customers.ListCustomersRequest):
                    The request object. Request to list customers
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.customers.ListCustomersResponse:
                    Response message for list customer
                Customers requests

            """

            http_options = _BaseCloudControlsPartnerCoreRestTransport._BaseListCustomers._get_http_options()
            request, metadata = self._interceptor.pre_list_customers(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudControlsPartnerCoreRestTransport._BaseListCustomers,
                    "_BaseListCustomers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.cloudcontrolspartner_v1beta.CloudControlsPartnerCoreClient.ListCustomers",
                    extra={
                        "serviceName": "google.cloud.cloudcontrolspartner.v1beta.CloudControlsPartnerCore",
                        "rpcName": "ListCustomers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CloudControlsPartnerCoreRestTransport._ListCustomers._get_response(
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

            # Return the response
            resp = customers.ListCustomersResponse()
            pb_resp = customers.ListCustomersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_customers(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_customers_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = customers.ListCustomersResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.cloudcontrolspartner_v1beta.CloudControlsPartnerCoreClient.list_customers",
                    extra={
                        "serviceName": "google.cloud.cloudcontrolspartner.v1beta.CloudControlsPartnerCore",
                        "rpcName": "ListCustomers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListWorkloads(
        _BaseCloudControlsPartnerCoreRestTransport._BaseListWorkloads,
        CloudControlsPartnerCoreRestStub,
    ):
        def __hash__(self):
            return hash("CloudControlsPartnerCoreRestTransport.ListWorkloads")

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
            request: customer_workloads.ListWorkloadsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> customer_workloads.ListWorkloadsResponse:
            r"""Call the list workloads method over HTTP.

            Args:
                request (~.customer_workloads.ListWorkloadsRequest):
                    The request object. Request to list customer workloads.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.customer_workloads.ListWorkloadsResponse:
                    Response message for list customer
                workloads requests.

            """

            http_options = _BaseCloudControlsPartnerCoreRestTransport._BaseListWorkloads._get_http_options()
            request, metadata = self._interceptor.pre_list_workloads(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudControlsPartnerCoreRestTransport._BaseListWorkloads,
                    "_BaseListWorkloads__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.cloudcontrolspartner_v1beta.CloudControlsPartnerCoreClient.ListWorkloads",
                    extra={
                        "serviceName": "google.cloud.cloudcontrolspartner.v1beta.CloudControlsPartnerCore",
                        "rpcName": "ListWorkloads",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CloudControlsPartnerCoreRestTransport._ListWorkloads._get_response(
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

            # Return the response
            resp = customer_workloads.ListWorkloadsResponse()
            pb_resp = customer_workloads.ListWorkloadsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_workloads(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_workloads_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = customer_workloads.ListWorkloadsResponse.to_json(
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
                    "Received response for google.cloud.cloudcontrolspartner_v1beta.CloudControlsPartnerCoreClient.list_workloads",
                    extra={
                        "serviceName": "google.cloud.cloudcontrolspartner.v1beta.CloudControlsPartnerCore",
                        "rpcName": "ListWorkloads",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateCustomer(
        _BaseCloudControlsPartnerCoreRestTransport._BaseUpdateCustomer,
        CloudControlsPartnerCoreRestStub,
    ):
        def __hash__(self):
            return hash("CloudControlsPartnerCoreRestTransport.UpdateCustomer")

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
            request: customers.UpdateCustomerRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> customers.Customer:
            r"""Call the update customer method over HTTP.

            Args:
                request (~.customers.UpdateCustomerRequest):
                    The request object. Request to update a customer
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.customers.Customer:
                    Contains metadata around a Cloud
                Controls Partner Customer

            """

            http_options = _BaseCloudControlsPartnerCoreRestTransport._BaseUpdateCustomer._get_http_options()
            request, metadata = self._interceptor.pre_update_customer(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudControlsPartnerCoreRestTransport._BaseUpdateCustomer,
                    "_BaseUpdateCustomer__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.cloudcontrolspartner_v1beta.CloudControlsPartnerCoreClient.UpdateCustomer",
                    extra={
                        "serviceName": "google.cloud.cloudcontrolspartner.v1beta.CloudControlsPartnerCore",
                        "rpcName": "UpdateCustomer",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                CloudControlsPartnerCoreRestTransport._UpdateCustomer._get_response(
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
            resp = customers.Customer()
            pb_resp = customers.Customer.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_customer(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_customer_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = customers.Customer.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.cloudcontrolspartner_v1beta.CloudControlsPartnerCoreClient.update_customer",
                    extra={
                        "serviceName": "google.cloud.cloudcontrolspartner.v1beta.CloudControlsPartnerCore",
                        "rpcName": "UpdateCustomer",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_customer(
        self,
    ) -> Callable[[customers.CreateCustomerRequest], customers.Customer]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateCustomer(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_customer(
        self,
    ) -> Callable[[customers.DeleteCustomerRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteCustomer(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_customer(
        self,
    ) -> Callable[[customers.GetCustomerRequest], customers.Customer]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCustomer(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_ekm_connections(
        self,
    ) -> Callable[
        [ekm_connections.GetEkmConnectionsRequest], ekm_connections.EkmConnections
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetEkmConnections(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_partner(self) -> Callable[[partners.GetPartnerRequest], partners.Partner]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetPartner(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_partner_permissions(
        self,
    ) -> Callable[
        [partner_permissions.GetPartnerPermissionsRequest],
        partner_permissions.PartnerPermissions,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetPartnerPermissions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_workload(
        self,
    ) -> Callable[[customer_workloads.GetWorkloadRequest], customer_workloads.Workload]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetWorkload(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_access_approval_requests(
        self,
    ) -> Callable[
        [access_approval_requests.ListAccessApprovalRequestsRequest],
        access_approval_requests.ListAccessApprovalRequestsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAccessApprovalRequests(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_customers(
        self,
    ) -> Callable[[customers.ListCustomersRequest], customers.ListCustomersResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListCustomers(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_workloads(
        self,
    ) -> Callable[
        [customer_workloads.ListWorkloadsRequest],
        customer_workloads.ListWorkloadsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListWorkloads(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_customer(
        self,
    ) -> Callable[[customers.UpdateCustomerRequest], customers.Customer]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateCustomer(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("CloudControlsPartnerCoreRestTransport",)
