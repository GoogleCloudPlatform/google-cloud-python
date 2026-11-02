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

from google.cloud.accessapproval_v1._compat import transcode_request
from google.cloud.accessapproval_v1.types import accessapproval

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseAccessApprovalRestTransport

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


class AccessApprovalRestInterceptor:
    """Interceptor for AccessApproval.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the AccessApprovalRestTransport.

    .. code-block:: python
        class MyCustomAccessApprovalInterceptor(AccessApprovalRestInterceptor):
            def pre_approve_approval_request(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_approve_approval_request(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_access_approval_settings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_dismiss_approval_request(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_dismiss_approval_request(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_access_approval_service_account(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_access_approval_service_account(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_access_approval_settings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_access_approval_settings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_approval_request(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_approval_request(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_invalidate_approval_request(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_invalidate_approval_request(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_approval_requests(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_approval_requests(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_access_approval_settings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_access_approval_settings(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = AccessApprovalRestTransport(interceptor=MyCustomAccessApprovalInterceptor())
        client = AccessApprovalClient(transport=transport)


    """

    def pre_approve_approval_request(
        self,
        request: accessapproval.ApproveApprovalRequestMessage,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        accessapproval.ApproveApprovalRequestMessage,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for approve_approval_request

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AccessApproval server.
        """
        return request, metadata

    def post_approve_approval_request(
        self, response: accessapproval.ApprovalRequest
    ) -> accessapproval.ApprovalRequest:
        """Post-rpc interceptor for approve_approval_request

        DEPRECATED. Please use the `post_approve_approval_request_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AccessApproval server but before
        it is returned to user code. This `post_approve_approval_request` interceptor runs
        before the `post_approve_approval_request_with_metadata` interceptor.
        """
        return response

    def post_approve_approval_request_with_metadata(
        self,
        response: accessapproval.ApprovalRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[accessapproval.ApprovalRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for approve_approval_request

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AccessApproval server but before it is returned to user code.

        We recommend only using this `post_approve_approval_request_with_metadata`
        interceptor in new development instead of the `post_approve_approval_request` interceptor.
        When both interceptors are used, this `post_approve_approval_request_with_metadata` interceptor runs after the
        `post_approve_approval_request` interceptor. The (possibly modified) response returned by
        `post_approve_approval_request` will be passed to
        `post_approve_approval_request_with_metadata`.
        """
        return response, metadata

    def pre_delete_access_approval_settings(
        self,
        request: accessapproval.DeleteAccessApprovalSettingsMessage,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        accessapproval.DeleteAccessApprovalSettingsMessage,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_access_approval_settings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AccessApproval server.
        """
        return request, metadata

    def pre_dismiss_approval_request(
        self,
        request: accessapproval.DismissApprovalRequestMessage,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        accessapproval.DismissApprovalRequestMessage,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for dismiss_approval_request

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AccessApproval server.
        """
        return request, metadata

    def post_dismiss_approval_request(
        self, response: accessapproval.ApprovalRequest
    ) -> accessapproval.ApprovalRequest:
        """Post-rpc interceptor for dismiss_approval_request

        DEPRECATED. Please use the `post_dismiss_approval_request_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AccessApproval server but before
        it is returned to user code. This `post_dismiss_approval_request` interceptor runs
        before the `post_dismiss_approval_request_with_metadata` interceptor.
        """
        return response

    def post_dismiss_approval_request_with_metadata(
        self,
        response: accessapproval.ApprovalRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[accessapproval.ApprovalRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for dismiss_approval_request

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AccessApproval server but before it is returned to user code.

        We recommend only using this `post_dismiss_approval_request_with_metadata`
        interceptor in new development instead of the `post_dismiss_approval_request` interceptor.
        When both interceptors are used, this `post_dismiss_approval_request_with_metadata` interceptor runs after the
        `post_dismiss_approval_request` interceptor. The (possibly modified) response returned by
        `post_dismiss_approval_request` will be passed to
        `post_dismiss_approval_request_with_metadata`.
        """
        return response, metadata

    def pre_get_access_approval_service_account(
        self,
        request: accessapproval.GetAccessApprovalServiceAccountMessage,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        accessapproval.GetAccessApprovalServiceAccountMessage,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_access_approval_service_account

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AccessApproval server.
        """
        return request, metadata

    def post_get_access_approval_service_account(
        self, response: accessapproval.AccessApprovalServiceAccount
    ) -> accessapproval.AccessApprovalServiceAccount:
        """Post-rpc interceptor for get_access_approval_service_account

        DEPRECATED. Please use the `post_get_access_approval_service_account_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AccessApproval server but before
        it is returned to user code. This `post_get_access_approval_service_account` interceptor runs
        before the `post_get_access_approval_service_account_with_metadata` interceptor.
        """
        return response

    def post_get_access_approval_service_account_with_metadata(
        self,
        response: accessapproval.AccessApprovalServiceAccount,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        accessapproval.AccessApprovalServiceAccount,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_access_approval_service_account

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AccessApproval server but before it is returned to user code.

        We recommend only using this `post_get_access_approval_service_account_with_metadata`
        interceptor in new development instead of the `post_get_access_approval_service_account` interceptor.
        When both interceptors are used, this `post_get_access_approval_service_account_with_metadata` interceptor runs after the
        `post_get_access_approval_service_account` interceptor. The (possibly modified) response returned by
        `post_get_access_approval_service_account` will be passed to
        `post_get_access_approval_service_account_with_metadata`.
        """
        return response, metadata

    def pre_get_access_approval_settings(
        self,
        request: accessapproval.GetAccessApprovalSettingsMessage,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        accessapproval.GetAccessApprovalSettingsMessage,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_access_approval_settings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AccessApproval server.
        """
        return request, metadata

    def post_get_access_approval_settings(
        self, response: accessapproval.AccessApprovalSettings
    ) -> accessapproval.AccessApprovalSettings:
        """Post-rpc interceptor for get_access_approval_settings

        DEPRECATED. Please use the `post_get_access_approval_settings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AccessApproval server but before
        it is returned to user code. This `post_get_access_approval_settings` interceptor runs
        before the `post_get_access_approval_settings_with_metadata` interceptor.
        """
        return response

    def post_get_access_approval_settings_with_metadata(
        self,
        response: accessapproval.AccessApprovalSettings,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        accessapproval.AccessApprovalSettings, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_access_approval_settings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AccessApproval server but before it is returned to user code.

        We recommend only using this `post_get_access_approval_settings_with_metadata`
        interceptor in new development instead of the `post_get_access_approval_settings` interceptor.
        When both interceptors are used, this `post_get_access_approval_settings_with_metadata` interceptor runs after the
        `post_get_access_approval_settings` interceptor. The (possibly modified) response returned by
        `post_get_access_approval_settings` will be passed to
        `post_get_access_approval_settings_with_metadata`.
        """
        return response, metadata

    def pre_get_approval_request(
        self,
        request: accessapproval.GetApprovalRequestMessage,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        accessapproval.GetApprovalRequestMessage,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_approval_request

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AccessApproval server.
        """
        return request, metadata

    def post_get_approval_request(
        self, response: accessapproval.ApprovalRequest
    ) -> accessapproval.ApprovalRequest:
        """Post-rpc interceptor for get_approval_request

        DEPRECATED. Please use the `post_get_approval_request_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AccessApproval server but before
        it is returned to user code. This `post_get_approval_request` interceptor runs
        before the `post_get_approval_request_with_metadata` interceptor.
        """
        return response

    def post_get_approval_request_with_metadata(
        self,
        response: accessapproval.ApprovalRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[accessapproval.ApprovalRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_approval_request

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AccessApproval server but before it is returned to user code.

        We recommend only using this `post_get_approval_request_with_metadata`
        interceptor in new development instead of the `post_get_approval_request` interceptor.
        When both interceptors are used, this `post_get_approval_request_with_metadata` interceptor runs after the
        `post_get_approval_request` interceptor. The (possibly modified) response returned by
        `post_get_approval_request` will be passed to
        `post_get_approval_request_with_metadata`.
        """
        return response, metadata

    def pre_invalidate_approval_request(
        self,
        request: accessapproval.InvalidateApprovalRequestMessage,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        accessapproval.InvalidateApprovalRequestMessage,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for invalidate_approval_request

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AccessApproval server.
        """
        return request, metadata

    def post_invalidate_approval_request(
        self, response: accessapproval.ApprovalRequest
    ) -> accessapproval.ApprovalRequest:
        """Post-rpc interceptor for invalidate_approval_request

        DEPRECATED. Please use the `post_invalidate_approval_request_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AccessApproval server but before
        it is returned to user code. This `post_invalidate_approval_request` interceptor runs
        before the `post_invalidate_approval_request_with_metadata` interceptor.
        """
        return response

    def post_invalidate_approval_request_with_metadata(
        self,
        response: accessapproval.ApprovalRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[accessapproval.ApprovalRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for invalidate_approval_request

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AccessApproval server but before it is returned to user code.

        We recommend only using this `post_invalidate_approval_request_with_metadata`
        interceptor in new development instead of the `post_invalidate_approval_request` interceptor.
        When both interceptors are used, this `post_invalidate_approval_request_with_metadata` interceptor runs after the
        `post_invalidate_approval_request` interceptor. The (possibly modified) response returned by
        `post_invalidate_approval_request` will be passed to
        `post_invalidate_approval_request_with_metadata`.
        """
        return response, metadata

    def pre_list_approval_requests(
        self,
        request: accessapproval.ListApprovalRequestsMessage,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        accessapproval.ListApprovalRequestsMessage,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_approval_requests

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AccessApproval server.
        """
        return request, metadata

    def post_list_approval_requests(
        self, response: accessapproval.ListApprovalRequestsResponse
    ) -> accessapproval.ListApprovalRequestsResponse:
        """Post-rpc interceptor for list_approval_requests

        DEPRECATED. Please use the `post_list_approval_requests_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AccessApproval server but before
        it is returned to user code. This `post_list_approval_requests` interceptor runs
        before the `post_list_approval_requests_with_metadata` interceptor.
        """
        return response

    def post_list_approval_requests_with_metadata(
        self,
        response: accessapproval.ListApprovalRequestsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        accessapproval.ListApprovalRequestsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_approval_requests

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AccessApproval server but before it is returned to user code.

        We recommend only using this `post_list_approval_requests_with_metadata`
        interceptor in new development instead of the `post_list_approval_requests` interceptor.
        When both interceptors are used, this `post_list_approval_requests_with_metadata` interceptor runs after the
        `post_list_approval_requests` interceptor. The (possibly modified) response returned by
        `post_list_approval_requests` will be passed to
        `post_list_approval_requests_with_metadata`.
        """
        return response, metadata

    def pre_update_access_approval_settings(
        self,
        request: accessapproval.UpdateAccessApprovalSettingsMessage,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        accessapproval.UpdateAccessApprovalSettingsMessage,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_access_approval_settings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AccessApproval server.
        """
        return request, metadata

    def post_update_access_approval_settings(
        self, response: accessapproval.AccessApprovalSettings
    ) -> accessapproval.AccessApprovalSettings:
        """Post-rpc interceptor for update_access_approval_settings

        DEPRECATED. Please use the `post_update_access_approval_settings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AccessApproval server but before
        it is returned to user code. This `post_update_access_approval_settings` interceptor runs
        before the `post_update_access_approval_settings_with_metadata` interceptor.
        """
        return response

    def post_update_access_approval_settings_with_metadata(
        self,
        response: accessapproval.AccessApprovalSettings,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        accessapproval.AccessApprovalSettings, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_access_approval_settings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AccessApproval server but before it is returned to user code.

        We recommend only using this `post_update_access_approval_settings_with_metadata`
        interceptor in new development instead of the `post_update_access_approval_settings` interceptor.
        When both interceptors are used, this `post_update_access_approval_settings_with_metadata` interceptor runs after the
        `post_update_access_approval_settings` interceptor. The (possibly modified) response returned by
        `post_update_access_approval_settings` will be passed to
        `post_update_access_approval_settings_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class AccessApprovalRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: AccessApprovalRestInterceptor


class AccessApprovalRestTransport(_BaseAccessApprovalRestTransport):
    """REST backend synchronous transport for AccessApproval.

    This API allows a customer to manage accesses to cloud resources by
    Google personnel. It defines the following resource model:

    - The API has a collection of
      [ApprovalRequest][google.cloud.accessapproval.v1.ApprovalRequest]
      resources, named ``approvalRequests/{approval_request}``
    - The API has top-level settings per Project/Folder/Organization,
      named ``accessApprovalSettings``

    The service also periodically emails a list of recipients, defined
    at the Project/Folder/Organization level in the
    accessApprovalSettings, when there is a pending ApprovalRequest for
    them to act on. The ApprovalRequests can also optionally be
    published to a Pub/Sub topic owned by the customer (contact support
    if you would like to enable Pub/Sub notifications).

    ApprovalRequests can be approved or dismissed. Google personnel can
    only access the indicated resource or resources if the request is
    approved (subject to some exclusions:
    https://cloud.google.com/access-approval/docs/overview#exclusions).

    Note: Using Access Approval functionality will mean that Google may
    not be able to meet the SLAs for your chosen products, as any
    support response times may be dramatically increased. As such the
    SLAs do not apply to any service disruption to the extent impacted
    by Customer's use of Access Approval. Do not enable Access Approval
    for projects where you may require high service availability and
    rapid response by Google Cloud Support.

    After a request is approved or dismissed, no further action may be
    taken on it. Requests with the requested_expiration in the past or
    with no activity for 14 days are considered dismissed. When an
    approval expires, the request is considered dismissed.

    If a request is not approved or dismissed, we call it pending.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "accessapproval.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[AccessApprovalRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'accessapproval.googleapis.com').
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
            interceptor (Optional[AccessApprovalRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or AccessApprovalRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _ApproveApprovalRequest(
        _BaseAccessApprovalRestTransport._BaseApproveApprovalRequest,
        AccessApprovalRestStub,
    ):
        def __hash__(self):
            return hash("AccessApprovalRestTransport.ApproveApprovalRequest")

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
            request: accessapproval.ApproveApprovalRequestMessage,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> accessapproval.ApprovalRequest:
            r"""Call the approve approval request method over HTTP.

            Args:
                request (~.accessapproval.ApproveApprovalRequestMessage):
                    The request object. Request to approve an
                ApprovalRequest.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.accessapproval.ApprovalRequest:
                    A request for the customer to approve
                access to a resource.

            """

            http_options = _BaseAccessApprovalRestTransport._BaseApproveApprovalRequest._get_http_options()
            request, metadata = self._interceptor.pre_approve_approval_request(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAccessApprovalRestTransport._BaseApproveApprovalRequest,
                    "_BaseApproveApprovalRequest__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.accessapproval_v1.AccessApprovalClient.ApproveApprovalRequest",
                    extra={
                        "serviceName": "google.cloud.accessapproval.v1.AccessApproval",
                        "rpcName": "ApproveApprovalRequest",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AccessApprovalRestTransport._ApproveApprovalRequest._get_response(
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
            resp = accessapproval.ApprovalRequest()
            pb_resp = accessapproval.ApprovalRequest.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_approve_approval_request(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_approve_approval_request_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = accessapproval.ApprovalRequest.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.accessapproval_v1.AccessApprovalClient.approve_approval_request",
                    extra={
                        "serviceName": "google.cloud.accessapproval.v1.AccessApproval",
                        "rpcName": "ApproveApprovalRequest",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteAccessApprovalSettings(
        _BaseAccessApprovalRestTransport._BaseDeleteAccessApprovalSettings,
        AccessApprovalRestStub,
    ):
        def __hash__(self):
            return hash("AccessApprovalRestTransport.DeleteAccessApprovalSettings")

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
            request: accessapproval.DeleteAccessApprovalSettingsMessage,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete access approval
            settings method over HTTP.

                Args:
                    request (~.accessapproval.DeleteAccessApprovalSettingsMessage):
                        The request object. Request to delete access approval
                    settings.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.
            """

            http_options = _BaseAccessApprovalRestTransport._BaseDeleteAccessApprovalSettings._get_http_options()
            request, metadata = self._interceptor.pre_delete_access_approval_settings(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAccessApprovalRestTransport._BaseDeleteAccessApprovalSettings,
                    "_BaseDeleteAccessApprovalSettings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.accessapproval_v1.AccessApprovalClient.DeleteAccessApprovalSettings",
                    extra={
                        "serviceName": "google.cloud.accessapproval.v1.AccessApproval",
                        "rpcName": "DeleteAccessApprovalSettings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AccessApprovalRestTransport._DeleteAccessApprovalSettings._get_response(
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

    class _DismissApprovalRequest(
        _BaseAccessApprovalRestTransport._BaseDismissApprovalRequest,
        AccessApprovalRestStub,
    ):
        def __hash__(self):
            return hash("AccessApprovalRestTransport.DismissApprovalRequest")

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
            request: accessapproval.DismissApprovalRequestMessage,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> accessapproval.ApprovalRequest:
            r"""Call the dismiss approval request method over HTTP.

            Args:
                request (~.accessapproval.DismissApprovalRequestMessage):
                    The request object. Request to dismiss an approval
                request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.accessapproval.ApprovalRequest:
                    A request for the customer to approve
                access to a resource.

            """

            http_options = _BaseAccessApprovalRestTransport._BaseDismissApprovalRequest._get_http_options()
            request, metadata = self._interceptor.pre_dismiss_approval_request(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAccessApprovalRestTransport._BaseDismissApprovalRequest,
                    "_BaseDismissApprovalRequest__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.accessapproval_v1.AccessApprovalClient.DismissApprovalRequest",
                    extra={
                        "serviceName": "google.cloud.accessapproval.v1.AccessApproval",
                        "rpcName": "DismissApprovalRequest",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AccessApprovalRestTransport._DismissApprovalRequest._get_response(
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
            resp = accessapproval.ApprovalRequest()
            pb_resp = accessapproval.ApprovalRequest.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_dismiss_approval_request(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_dismiss_approval_request_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = accessapproval.ApprovalRequest.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.accessapproval_v1.AccessApprovalClient.dismiss_approval_request",
                    extra={
                        "serviceName": "google.cloud.accessapproval.v1.AccessApproval",
                        "rpcName": "DismissApprovalRequest",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAccessApprovalServiceAccount(
        _BaseAccessApprovalRestTransport._BaseGetAccessApprovalServiceAccount,
        AccessApprovalRestStub,
    ):
        def __hash__(self):
            return hash("AccessApprovalRestTransport.GetAccessApprovalServiceAccount")

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
            request: accessapproval.GetAccessApprovalServiceAccountMessage,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> accessapproval.AccessApprovalServiceAccount:
            r"""Call the get access approval
            service account method over HTTP.

                Args:
                    request (~.accessapproval.GetAccessApprovalServiceAccountMessage):
                        The request object. Request to get an Access Approval
                    service account.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.accessapproval.AccessApprovalServiceAccount:
                        Access Approval service account
                    related to a
                    project/folder/organization.

            """

            http_options = _BaseAccessApprovalRestTransport._BaseGetAccessApprovalServiceAccount._get_http_options()
            request, metadata = (
                self._interceptor.pre_get_access_approval_service_account(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAccessApprovalRestTransport._BaseGetAccessApprovalServiceAccount,
                    "_BaseGetAccessApprovalServiceAccount__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.accessapproval_v1.AccessApprovalClient.GetAccessApprovalServiceAccount",
                    extra={
                        "serviceName": "google.cloud.accessapproval.v1.AccessApproval",
                        "rpcName": "GetAccessApprovalServiceAccount",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AccessApprovalRestTransport._GetAccessApprovalServiceAccount._get_response(
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
            resp = accessapproval.AccessApprovalServiceAccount()
            pb_resp = accessapproval.AccessApprovalServiceAccount.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_access_approval_service_account(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_access_approval_service_account_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        accessapproval.AccessApprovalServiceAccount.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.accessapproval_v1.AccessApprovalClient.get_access_approval_service_account",
                    extra={
                        "serviceName": "google.cloud.accessapproval.v1.AccessApproval",
                        "rpcName": "GetAccessApprovalServiceAccount",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAccessApprovalSettings(
        _BaseAccessApprovalRestTransport._BaseGetAccessApprovalSettings,
        AccessApprovalRestStub,
    ):
        def __hash__(self):
            return hash("AccessApprovalRestTransport.GetAccessApprovalSettings")

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
            request: accessapproval.GetAccessApprovalSettingsMessage,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> accessapproval.AccessApprovalSettings:
            r"""Call the get access approval
            settings method over HTTP.

                Args:
                    request (~.accessapproval.GetAccessApprovalSettingsMessage):
                        The request object. Request to get access approval
                    settings.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.accessapproval.AccessApprovalSettings:
                        Settings on a
                    Project/Folder/Organization related to
                    Access Approval.

            """

            http_options = _BaseAccessApprovalRestTransport._BaseGetAccessApprovalSettings._get_http_options()
            request, metadata = self._interceptor.pre_get_access_approval_settings(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAccessApprovalRestTransport._BaseGetAccessApprovalSettings,
                    "_BaseGetAccessApprovalSettings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.accessapproval_v1.AccessApprovalClient.GetAccessApprovalSettings",
                    extra={
                        "serviceName": "google.cloud.accessapproval.v1.AccessApproval",
                        "rpcName": "GetAccessApprovalSettings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AccessApprovalRestTransport._GetAccessApprovalSettings._get_response(
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
            resp = accessapproval.AccessApprovalSettings()
            pb_resp = accessapproval.AccessApprovalSettings.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_access_approval_settings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_access_approval_settings_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = accessapproval.AccessApprovalSettings.to_json(
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
                    "Received response for google.cloud.accessapproval_v1.AccessApprovalClient.get_access_approval_settings",
                    extra={
                        "serviceName": "google.cloud.accessapproval.v1.AccessApproval",
                        "rpcName": "GetAccessApprovalSettings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetApprovalRequest(
        _BaseAccessApprovalRestTransport._BaseGetApprovalRequest, AccessApprovalRestStub
    ):
        def __hash__(self):
            return hash("AccessApprovalRestTransport.GetApprovalRequest")

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
            request: accessapproval.GetApprovalRequestMessage,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> accessapproval.ApprovalRequest:
            r"""Call the get approval request method over HTTP.

            Args:
                request (~.accessapproval.GetApprovalRequestMessage):
                    The request object. Request to get an approval request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.accessapproval.ApprovalRequest:
                    A request for the customer to approve
                access to a resource.

            """

            http_options = _BaseAccessApprovalRestTransport._BaseGetApprovalRequest._get_http_options()
            request, metadata = self._interceptor.pre_get_approval_request(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAccessApprovalRestTransport._BaseGetApprovalRequest,
                    "_BaseGetApprovalRequest__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.accessapproval_v1.AccessApprovalClient.GetApprovalRequest",
                    extra={
                        "serviceName": "google.cloud.accessapproval.v1.AccessApproval",
                        "rpcName": "GetApprovalRequest",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AccessApprovalRestTransport._GetApprovalRequest._get_response(
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
            resp = accessapproval.ApprovalRequest()
            pb_resp = accessapproval.ApprovalRequest.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_approval_request(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_approval_request_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = accessapproval.ApprovalRequest.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.accessapproval_v1.AccessApprovalClient.get_approval_request",
                    extra={
                        "serviceName": "google.cloud.accessapproval.v1.AccessApproval",
                        "rpcName": "GetApprovalRequest",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _InvalidateApprovalRequest(
        _BaseAccessApprovalRestTransport._BaseInvalidateApprovalRequest,
        AccessApprovalRestStub,
    ):
        def __hash__(self):
            return hash("AccessApprovalRestTransport.InvalidateApprovalRequest")

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
            request: accessapproval.InvalidateApprovalRequestMessage,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> accessapproval.ApprovalRequest:
            r"""Call the invalidate approval
            request method over HTTP.

                Args:
                    request (~.accessapproval.InvalidateApprovalRequestMessage):
                        The request object. Request to invalidate an existing
                    approval.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.accessapproval.ApprovalRequest:
                        A request for the customer to approve
                    access to a resource.

            """

            http_options = _BaseAccessApprovalRestTransport._BaseInvalidateApprovalRequest._get_http_options()
            request, metadata = self._interceptor.pre_invalidate_approval_request(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAccessApprovalRestTransport._BaseInvalidateApprovalRequest,
                    "_BaseInvalidateApprovalRequest__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.accessapproval_v1.AccessApprovalClient.InvalidateApprovalRequest",
                    extra={
                        "serviceName": "google.cloud.accessapproval.v1.AccessApproval",
                        "rpcName": "InvalidateApprovalRequest",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AccessApprovalRestTransport._InvalidateApprovalRequest._get_response(
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
            resp = accessapproval.ApprovalRequest()
            pb_resp = accessapproval.ApprovalRequest.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_invalidate_approval_request(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_invalidate_approval_request_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = accessapproval.ApprovalRequest.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.accessapproval_v1.AccessApprovalClient.invalidate_approval_request",
                    extra={
                        "serviceName": "google.cloud.accessapproval.v1.AccessApproval",
                        "rpcName": "InvalidateApprovalRequest",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListApprovalRequests(
        _BaseAccessApprovalRestTransport._BaseListApprovalRequests,
        AccessApprovalRestStub,
    ):
        def __hash__(self):
            return hash("AccessApprovalRestTransport.ListApprovalRequests")

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
            request: accessapproval.ListApprovalRequestsMessage,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> accessapproval.ListApprovalRequestsResponse:
            r"""Call the list approval requests method over HTTP.

            Args:
                request (~.accessapproval.ListApprovalRequestsMessage):
                    The request object. Request to list approval requests.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.accessapproval.ListApprovalRequestsResponse:
                    Response to listing of
                ApprovalRequest objects.

            """

            http_options = _BaseAccessApprovalRestTransport._BaseListApprovalRequests._get_http_options()
            request, metadata = self._interceptor.pre_list_approval_requests(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAccessApprovalRestTransport._BaseListApprovalRequests,
                    "_BaseListApprovalRequests__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.accessapproval_v1.AccessApprovalClient.ListApprovalRequests",
                    extra={
                        "serviceName": "google.cloud.accessapproval.v1.AccessApproval",
                        "rpcName": "ListApprovalRequests",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AccessApprovalRestTransport._ListApprovalRequests._get_response(
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
            resp = accessapproval.ListApprovalRequestsResponse()
            pb_resp = accessapproval.ListApprovalRequestsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_approval_requests(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_approval_requests_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        accessapproval.ListApprovalRequestsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.accessapproval_v1.AccessApprovalClient.list_approval_requests",
                    extra={
                        "serviceName": "google.cloud.accessapproval.v1.AccessApproval",
                        "rpcName": "ListApprovalRequests",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateAccessApprovalSettings(
        _BaseAccessApprovalRestTransport._BaseUpdateAccessApprovalSettings,
        AccessApprovalRestStub,
    ):
        def __hash__(self):
            return hash("AccessApprovalRestTransport.UpdateAccessApprovalSettings")

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
            request: accessapproval.UpdateAccessApprovalSettingsMessage,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> accessapproval.AccessApprovalSettings:
            r"""Call the update access approval
            settings method over HTTP.

                Args:
                    request (~.accessapproval.UpdateAccessApprovalSettingsMessage):
                        The request object. Request to update access approval
                    settings.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.accessapproval.AccessApprovalSettings:
                        Settings on a
                    Project/Folder/Organization related to
                    Access Approval.

            """

            http_options = _BaseAccessApprovalRestTransport._BaseUpdateAccessApprovalSettings._get_http_options()
            request, metadata = self._interceptor.pre_update_access_approval_settings(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAccessApprovalRestTransport._BaseUpdateAccessApprovalSettings,
                    "_BaseUpdateAccessApprovalSettings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.accessapproval_v1.AccessApprovalClient.UpdateAccessApprovalSettings",
                    extra={
                        "serviceName": "google.cloud.accessapproval.v1.AccessApproval",
                        "rpcName": "UpdateAccessApprovalSettings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AccessApprovalRestTransport._UpdateAccessApprovalSettings._get_response(
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
            resp = accessapproval.AccessApprovalSettings()
            pb_resp = accessapproval.AccessApprovalSettings.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_access_approval_settings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_access_approval_settings_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = accessapproval.AccessApprovalSettings.to_json(
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
                    "Received response for google.cloud.accessapproval_v1.AccessApprovalClient.update_access_approval_settings",
                    extra={
                        "serviceName": "google.cloud.accessapproval.v1.AccessApproval",
                        "rpcName": "UpdateAccessApprovalSettings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def approve_approval_request(
        self,
    ) -> Callable[
        [accessapproval.ApproveApprovalRequestMessage], accessapproval.ApprovalRequest
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ApproveApprovalRequest(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_access_approval_settings(
        self,
    ) -> Callable[
        [accessapproval.DeleteAccessApprovalSettingsMessage], empty_pb2.Empty
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteAccessApprovalSettings(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def dismiss_approval_request(
        self,
    ) -> Callable[
        [accessapproval.DismissApprovalRequestMessage], accessapproval.ApprovalRequest
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DismissApprovalRequest(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_access_approval_service_account(
        self,
    ) -> Callable[
        [accessapproval.GetAccessApprovalServiceAccountMessage],
        accessapproval.AccessApprovalServiceAccount,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAccessApprovalServiceAccount(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_access_approval_settings(
        self,
    ) -> Callable[
        [accessapproval.GetAccessApprovalSettingsMessage],
        accessapproval.AccessApprovalSettings,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAccessApprovalSettings(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_approval_request(
        self,
    ) -> Callable[
        [accessapproval.GetApprovalRequestMessage], accessapproval.ApprovalRequest
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetApprovalRequest(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def invalidate_approval_request(
        self,
    ) -> Callable[
        [accessapproval.InvalidateApprovalRequestMessage],
        accessapproval.ApprovalRequest,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._InvalidateApprovalRequest(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_approval_requests(
        self,
    ) -> Callable[
        [accessapproval.ListApprovalRequestsMessage],
        accessapproval.ListApprovalRequestsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListApprovalRequests(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_access_approval_settings(
        self,
    ) -> Callable[
        [accessapproval.UpdateAccessApprovalSettingsMessage],
        accessapproval.AccessApprovalSettings,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateAccessApprovalSettings(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("AccessApprovalRestTransport",)
