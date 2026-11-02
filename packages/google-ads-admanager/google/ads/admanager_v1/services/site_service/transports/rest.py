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
from google.ads.admanager_v1.types import site_messages, site_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseSiteServiceRestTransport

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


class SiteServiceRestInterceptor:
    """Interceptor for SiteService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the SiteServiceRestTransport.

    .. code-block:: python
        class MyCustomSiteServiceInterceptor(SiteServiceRestInterceptor):
            def pre_batch_create_sites(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_sites(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_deactivate_sites(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_deactivate_sites(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_submit_sites_for_approval(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_submit_sites_for_approval(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_update_sites(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_sites(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_site(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_site(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_site(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_site(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_sites(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_sites(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_site(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_site(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = SiteServiceRestTransport(interceptor=MyCustomSiteServiceInterceptor())
        client = SiteServiceClient(transport=transport)


    """

    def pre_batch_create_sites(
        self,
        request: site_service.BatchCreateSitesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        site_service.BatchCreateSitesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for batch_create_sites

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SiteService server.
        """
        return request, metadata

    def post_batch_create_sites(
        self, response: site_service.BatchCreateSitesResponse
    ) -> site_service.BatchCreateSitesResponse:
        """Post-rpc interceptor for batch_create_sites

        DEPRECATED. Please use the `post_batch_create_sites_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SiteService server but before
        it is returned to user code. This `post_batch_create_sites` interceptor runs
        before the `post_batch_create_sites_with_metadata` interceptor.
        """
        return response

    def post_batch_create_sites_with_metadata(
        self,
        response: site_service.BatchCreateSitesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        site_service.BatchCreateSitesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for batch_create_sites

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SiteService server but before it is returned to user code.

        We recommend only using this `post_batch_create_sites_with_metadata`
        interceptor in new development instead of the `post_batch_create_sites` interceptor.
        When both interceptors are used, this `post_batch_create_sites_with_metadata` interceptor runs after the
        `post_batch_create_sites` interceptor. The (possibly modified) response returned by
        `post_batch_create_sites` will be passed to
        `post_batch_create_sites_with_metadata`.
        """
        return response, metadata

    def pre_batch_deactivate_sites(
        self,
        request: site_service.BatchDeactivateSitesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        site_service.BatchDeactivateSitesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_deactivate_sites

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SiteService server.
        """
        return request, metadata

    def post_batch_deactivate_sites(
        self, response: site_service.BatchDeactivateSitesResponse
    ) -> site_service.BatchDeactivateSitesResponse:
        """Post-rpc interceptor for batch_deactivate_sites

        DEPRECATED. Please use the `post_batch_deactivate_sites_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SiteService server but before
        it is returned to user code. This `post_batch_deactivate_sites` interceptor runs
        before the `post_batch_deactivate_sites_with_metadata` interceptor.
        """
        return response

    def post_batch_deactivate_sites_with_metadata(
        self,
        response: site_service.BatchDeactivateSitesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        site_service.BatchDeactivateSitesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_deactivate_sites

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SiteService server but before it is returned to user code.

        We recommend only using this `post_batch_deactivate_sites_with_metadata`
        interceptor in new development instead of the `post_batch_deactivate_sites` interceptor.
        When both interceptors are used, this `post_batch_deactivate_sites_with_metadata` interceptor runs after the
        `post_batch_deactivate_sites` interceptor. The (possibly modified) response returned by
        `post_batch_deactivate_sites` will be passed to
        `post_batch_deactivate_sites_with_metadata`.
        """
        return response, metadata

    def pre_batch_submit_sites_for_approval(
        self,
        request: site_service.BatchSubmitSitesForApprovalRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        site_service.BatchSubmitSitesForApprovalRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_submit_sites_for_approval

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SiteService server.
        """
        return request, metadata

    def post_batch_submit_sites_for_approval(
        self, response: site_service.BatchSubmitSitesForApprovalResponse
    ) -> site_service.BatchSubmitSitesForApprovalResponse:
        """Post-rpc interceptor for batch_submit_sites_for_approval

        DEPRECATED. Please use the `post_batch_submit_sites_for_approval_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SiteService server but before
        it is returned to user code. This `post_batch_submit_sites_for_approval` interceptor runs
        before the `post_batch_submit_sites_for_approval_with_metadata` interceptor.
        """
        return response

    def post_batch_submit_sites_for_approval_with_metadata(
        self,
        response: site_service.BatchSubmitSitesForApprovalResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        site_service.BatchSubmitSitesForApprovalResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_submit_sites_for_approval

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SiteService server but before it is returned to user code.

        We recommend only using this `post_batch_submit_sites_for_approval_with_metadata`
        interceptor in new development instead of the `post_batch_submit_sites_for_approval` interceptor.
        When both interceptors are used, this `post_batch_submit_sites_for_approval_with_metadata` interceptor runs after the
        `post_batch_submit_sites_for_approval` interceptor. The (possibly modified) response returned by
        `post_batch_submit_sites_for_approval` will be passed to
        `post_batch_submit_sites_for_approval_with_metadata`.
        """
        return response, metadata

    def pre_batch_update_sites(
        self,
        request: site_service.BatchUpdateSitesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        site_service.BatchUpdateSitesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for batch_update_sites

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SiteService server.
        """
        return request, metadata

    def post_batch_update_sites(
        self, response: site_service.BatchUpdateSitesResponse
    ) -> site_service.BatchUpdateSitesResponse:
        """Post-rpc interceptor for batch_update_sites

        DEPRECATED. Please use the `post_batch_update_sites_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SiteService server but before
        it is returned to user code. This `post_batch_update_sites` interceptor runs
        before the `post_batch_update_sites_with_metadata` interceptor.
        """
        return response

    def post_batch_update_sites_with_metadata(
        self,
        response: site_service.BatchUpdateSitesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        site_service.BatchUpdateSitesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for batch_update_sites

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SiteService server but before it is returned to user code.

        We recommend only using this `post_batch_update_sites_with_metadata`
        interceptor in new development instead of the `post_batch_update_sites` interceptor.
        When both interceptors are used, this `post_batch_update_sites_with_metadata` interceptor runs after the
        `post_batch_update_sites` interceptor. The (possibly modified) response returned by
        `post_batch_update_sites` will be passed to
        `post_batch_update_sites_with_metadata`.
        """
        return response, metadata

    def pre_create_site(
        self,
        request: site_service.CreateSiteRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[site_service.CreateSiteRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_site

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SiteService server.
        """
        return request, metadata

    def post_create_site(self, response: site_messages.Site) -> site_messages.Site:
        """Post-rpc interceptor for create_site

        DEPRECATED. Please use the `post_create_site_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SiteService server but before
        it is returned to user code. This `post_create_site` interceptor runs
        before the `post_create_site_with_metadata` interceptor.
        """
        return response

    def post_create_site_with_metadata(
        self,
        response: site_messages.Site,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[site_messages.Site, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_site

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SiteService server but before it is returned to user code.

        We recommend only using this `post_create_site_with_metadata`
        interceptor in new development instead of the `post_create_site` interceptor.
        When both interceptors are used, this `post_create_site_with_metadata` interceptor runs after the
        `post_create_site` interceptor. The (possibly modified) response returned by
        `post_create_site` will be passed to
        `post_create_site_with_metadata`.
        """
        return response, metadata

    def pre_get_site(
        self,
        request: site_service.GetSiteRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[site_service.GetSiteRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_site

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SiteService server.
        """
        return request, metadata

    def post_get_site(self, response: site_messages.Site) -> site_messages.Site:
        """Post-rpc interceptor for get_site

        DEPRECATED. Please use the `post_get_site_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SiteService server but before
        it is returned to user code. This `post_get_site` interceptor runs
        before the `post_get_site_with_metadata` interceptor.
        """
        return response

    def post_get_site_with_metadata(
        self,
        response: site_messages.Site,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[site_messages.Site, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_site

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SiteService server but before it is returned to user code.

        We recommend only using this `post_get_site_with_metadata`
        interceptor in new development instead of the `post_get_site` interceptor.
        When both interceptors are used, this `post_get_site_with_metadata` interceptor runs after the
        `post_get_site` interceptor. The (possibly modified) response returned by
        `post_get_site` will be passed to
        `post_get_site_with_metadata`.
        """
        return response, metadata

    def pre_list_sites(
        self,
        request: site_service.ListSitesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[site_service.ListSitesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_sites

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SiteService server.
        """
        return request, metadata

    def post_list_sites(
        self, response: site_service.ListSitesResponse
    ) -> site_service.ListSitesResponse:
        """Post-rpc interceptor for list_sites

        DEPRECATED. Please use the `post_list_sites_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SiteService server but before
        it is returned to user code. This `post_list_sites` interceptor runs
        before the `post_list_sites_with_metadata` interceptor.
        """
        return response

    def post_list_sites_with_metadata(
        self,
        response: site_service.ListSitesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[site_service.ListSitesResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_sites

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SiteService server but before it is returned to user code.

        We recommend only using this `post_list_sites_with_metadata`
        interceptor in new development instead of the `post_list_sites` interceptor.
        When both interceptors are used, this `post_list_sites_with_metadata` interceptor runs after the
        `post_list_sites` interceptor. The (possibly modified) response returned by
        `post_list_sites` will be passed to
        `post_list_sites_with_metadata`.
        """
        return response, metadata

    def pre_update_site(
        self,
        request: site_service.UpdateSiteRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[site_service.UpdateSiteRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_site

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SiteService server.
        """
        return request, metadata

    def post_update_site(self, response: site_messages.Site) -> site_messages.Site:
        """Post-rpc interceptor for update_site

        DEPRECATED. Please use the `post_update_site_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SiteService server but before
        it is returned to user code. This `post_update_site` interceptor runs
        before the `post_update_site_with_metadata` interceptor.
        """
        return response

    def post_update_site_with_metadata(
        self,
        response: site_messages.Site,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[site_messages.Site, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_site

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SiteService server but before it is returned to user code.

        We recommend only using this `post_update_site_with_metadata`
        interceptor in new development instead of the `post_update_site` interceptor.
        When both interceptors are used, this `post_update_site_with_metadata` interceptor runs after the
        `post_update_site` interceptor. The (possibly modified) response returned by
        `post_update_site` will be passed to
        `post_update_site_with_metadata`.
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
        before they are sent to the SiteService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the SiteService server but before
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
        before they are sent to the SiteService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the SiteService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class SiteServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: SiteServiceRestInterceptor


class SiteServiceRestTransport(_BaseSiteServiceRestTransport):
    """REST backend synchronous transport for SiteService.

    Provides methods for handling ``Site`` objects.

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
        interceptor: Optional[SiteServiceRestInterceptor] = None,
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
            interceptor (Optional[SiteServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or SiteServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchCreateSites(
        _BaseSiteServiceRestTransport._BaseBatchCreateSites, SiteServiceRestStub
    ):
        def __hash__(self):
            return hash("SiteServiceRestTransport.BatchCreateSites")

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
            request: site_service.BatchCreateSitesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> site_service.BatchCreateSitesResponse:
            r"""Call the batch create sites method over HTTP.

            Args:
                request (~.site_service.BatchCreateSitesRequest):
                    The request object. Request object for ``BatchCreateSites`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.site_service.BatchCreateSitesResponse:
                    Response object for ``BatchCreateSites`` method.
            """

            http_options = (
                _BaseSiteServiceRestTransport._BaseBatchCreateSites._get_http_options()
            )
            request, metadata = self._interceptor.pre_batch_create_sites(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSiteServiceRestTransport._BaseBatchCreateSites,
                    "_BaseBatchCreateSites__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.SiteServiceClient.BatchCreateSites",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SiteService",
                        "rpcName": "BatchCreateSites",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SiteServiceRestTransport._BatchCreateSites._get_response(
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
            resp = site_service.BatchCreateSitesResponse()
            pb_resp = site_service.BatchCreateSitesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_sites(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_create_sites_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = site_service.BatchCreateSitesResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.SiteServiceClient.batch_create_sites",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SiteService",
                        "rpcName": "BatchCreateSites",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchDeactivateSites(
        _BaseSiteServiceRestTransport._BaseBatchDeactivateSites, SiteServiceRestStub
    ):
        def __hash__(self):
            return hash("SiteServiceRestTransport.BatchDeactivateSites")

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
            request: site_service.BatchDeactivateSitesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> site_service.BatchDeactivateSitesResponse:
            r"""Call the batch deactivate sites method over HTTP.

            Args:
                request (~.site_service.BatchDeactivateSitesRequest):
                    The request object. Request message for ``BatchDeactivateSites`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.site_service.BatchDeactivateSitesResponse:
                    Response object for ``BatchDeactivateSites`` method.
            """

            http_options = _BaseSiteServiceRestTransport._BaseBatchDeactivateSites._get_http_options()
            request, metadata = self._interceptor.pre_batch_deactivate_sites(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSiteServiceRestTransport._BaseBatchDeactivateSites,
                    "_BaseBatchDeactivateSites__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.SiteServiceClient.BatchDeactivateSites",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SiteService",
                        "rpcName": "BatchDeactivateSites",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SiteServiceRestTransport._BatchDeactivateSites._get_response(
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
            resp = site_service.BatchDeactivateSitesResponse()
            pb_resp = site_service.BatchDeactivateSitesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_deactivate_sites(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_deactivate_sites_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        site_service.BatchDeactivateSitesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.SiteServiceClient.batch_deactivate_sites",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SiteService",
                        "rpcName": "BatchDeactivateSites",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchSubmitSitesForApproval(
        _BaseSiteServiceRestTransport._BaseBatchSubmitSitesForApproval,
        SiteServiceRestStub,
    ):
        def __hash__(self):
            return hash("SiteServiceRestTransport.BatchSubmitSitesForApproval")

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
            request: site_service.BatchSubmitSitesForApprovalRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> site_service.BatchSubmitSitesForApprovalResponse:
            r"""Call the batch submit sites for
            approval method over HTTP.

                Args:
                    request (~.site_service.BatchSubmitSitesForApprovalRequest):
                        The request object. Request message for ``BatchSubmitSitesForApproval``
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.site_service.BatchSubmitSitesForApprovalResponse:
                        Response object for ``BatchSubmitSitesForApproval``
                    method.

            """

            http_options = _BaseSiteServiceRestTransport._BaseBatchSubmitSitesForApproval._get_http_options()
            request, metadata = self._interceptor.pre_batch_submit_sites_for_approval(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSiteServiceRestTransport._BaseBatchSubmitSitesForApproval,
                    "_BaseBatchSubmitSitesForApproval__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.SiteServiceClient.BatchSubmitSitesForApproval",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SiteService",
                        "rpcName": "BatchSubmitSitesForApproval",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SiteServiceRestTransport._BatchSubmitSitesForApproval._get_response(
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
            resp = site_service.BatchSubmitSitesForApprovalResponse()
            pb_resp = site_service.BatchSubmitSitesForApprovalResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_submit_sites_for_approval(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_batch_submit_sites_for_approval_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        site_service.BatchSubmitSitesForApprovalResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.SiteServiceClient.batch_submit_sites_for_approval",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SiteService",
                        "rpcName": "BatchSubmitSitesForApproval",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchUpdateSites(
        _BaseSiteServiceRestTransport._BaseBatchUpdateSites, SiteServiceRestStub
    ):
        def __hash__(self):
            return hash("SiteServiceRestTransport.BatchUpdateSites")

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
            request: site_service.BatchUpdateSitesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> site_service.BatchUpdateSitesResponse:
            r"""Call the batch update sites method over HTTP.

            Args:
                request (~.site_service.BatchUpdateSitesRequest):
                    The request object. Request object for ``BatchUpdateSites`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.site_service.BatchUpdateSitesResponse:
                    Response object for ``BatchUpdateSites`` method.
            """

            http_options = (
                _BaseSiteServiceRestTransport._BaseBatchUpdateSites._get_http_options()
            )
            request, metadata = self._interceptor.pre_batch_update_sites(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSiteServiceRestTransport._BaseBatchUpdateSites,
                    "_BaseBatchUpdateSites__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.SiteServiceClient.BatchUpdateSites",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SiteService",
                        "rpcName": "BatchUpdateSites",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SiteServiceRestTransport._BatchUpdateSites._get_response(
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
            resp = site_service.BatchUpdateSitesResponse()
            pb_resp = site_service.BatchUpdateSitesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_sites(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_update_sites_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = site_service.BatchUpdateSitesResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.SiteServiceClient.batch_update_sites",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SiteService",
                        "rpcName": "BatchUpdateSites",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateSite(
        _BaseSiteServiceRestTransport._BaseCreateSite, SiteServiceRestStub
    ):
        def __hash__(self):
            return hash("SiteServiceRestTransport.CreateSite")

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
            request: site_service.CreateSiteRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> site_messages.Site:
            r"""Call the create site method over HTTP.

            Args:
                request (~.site_service.CreateSiteRequest):
                    The request object. Request object for ``CreateSite`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.site_messages.Site:
                    A Site represents a domain owned or
                represented by a network. For a parent
                network managing other networks as part
                of Multiple Customer Management "Manage
                Inventory" model, it could be the
                child's domain.

            """

            http_options = (
                _BaseSiteServiceRestTransport._BaseCreateSite._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_site(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSiteServiceRestTransport._BaseCreateSite,
                    "_BaseCreateSite__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.SiteServiceClient.CreateSite",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SiteService",
                        "rpcName": "CreateSite",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SiteServiceRestTransport._CreateSite._get_response(
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
            resp = site_messages.Site()
            pb_resp = site_messages.Site.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_site(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_site_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = site_messages.Site.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.SiteServiceClient.create_site",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SiteService",
                        "rpcName": "CreateSite",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSite(_BaseSiteServiceRestTransport._BaseGetSite, SiteServiceRestStub):
        def __hash__(self):
            return hash("SiteServiceRestTransport.GetSite")

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
            request: site_service.GetSiteRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> site_messages.Site:
            r"""Call the get site method over HTTP.

            Args:
                request (~.site_service.GetSiteRequest):
                    The request object. Request object for ``GetSite`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.site_messages.Site:
                    A Site represents a domain owned or
                represented by a network. For a parent
                network managing other networks as part
                of Multiple Customer Management "Manage
                Inventory" model, it could be the
                child's domain.

            """

            http_options = (
                _BaseSiteServiceRestTransport._BaseGetSite._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_site(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSiteServiceRestTransport._BaseGetSite,
                    "_BaseGetSite__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.SiteServiceClient.GetSite",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SiteService",
                        "rpcName": "GetSite",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SiteServiceRestTransport._GetSite._get_response(
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
            resp = site_messages.Site()
            pb_resp = site_messages.Site.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_site(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_site_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = site_messages.Site.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.SiteServiceClient.get_site",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SiteService",
                        "rpcName": "GetSite",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSites(_BaseSiteServiceRestTransport._BaseListSites, SiteServiceRestStub):
        def __hash__(self):
            return hash("SiteServiceRestTransport.ListSites")

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
            request: site_service.ListSitesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> site_service.ListSitesResponse:
            r"""Call the list sites method over HTTP.

            Args:
                request (~.site_service.ListSitesRequest):
                    The request object. Request object for ``ListSites`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.site_service.ListSitesResponse:
                    Response object for ``ListSitesRequest`` containing
                matching ``Site`` objects.

            """

            http_options = (
                _BaseSiteServiceRestTransport._BaseListSites._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_sites(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSiteServiceRestTransport._BaseListSites,
                    "_BaseListSites__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.SiteServiceClient.ListSites",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SiteService",
                        "rpcName": "ListSites",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SiteServiceRestTransport._ListSites._get_response(
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
            resp = site_service.ListSitesResponse()
            pb_resp = site_service.ListSitesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_sites(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_sites_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = site_service.ListSitesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.SiteServiceClient.list_sites",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SiteService",
                        "rpcName": "ListSites",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateSite(
        _BaseSiteServiceRestTransport._BaseUpdateSite, SiteServiceRestStub
    ):
        def __hash__(self):
            return hash("SiteServiceRestTransport.UpdateSite")

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
            request: site_service.UpdateSiteRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> site_messages.Site:
            r"""Call the update site method over HTTP.

            Args:
                request (~.site_service.UpdateSiteRequest):
                    The request object. Request object for ``UpdateSite`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.site_messages.Site:
                    A Site represents a domain owned or
                represented by a network. For a parent
                network managing other networks as part
                of Multiple Customer Management "Manage
                Inventory" model, it could be the
                child's domain.

            """

            http_options = (
                _BaseSiteServiceRestTransport._BaseUpdateSite._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_site(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSiteServiceRestTransport._BaseUpdateSite,
                    "_BaseUpdateSite__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.SiteServiceClient.UpdateSite",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SiteService",
                        "rpcName": "UpdateSite",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SiteServiceRestTransport._UpdateSite._get_response(
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
            resp = site_messages.Site()
            pb_resp = site_messages.Site.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_site(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_site_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = site_messages.Site.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.SiteServiceClient.update_site",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SiteService",
                        "rpcName": "UpdateSite",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_create_sites(
        self,
    ) -> Callable[
        [site_service.BatchCreateSitesRequest], site_service.BatchCreateSitesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateSites(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_deactivate_sites(
        self,
    ) -> Callable[
        [site_service.BatchDeactivateSitesRequest],
        site_service.BatchDeactivateSitesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchDeactivateSites(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_submit_sites_for_approval(
        self,
    ) -> Callable[
        [site_service.BatchSubmitSitesForApprovalRequest],
        site_service.BatchSubmitSitesForApprovalResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchSubmitSitesForApproval(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_update_sites(
        self,
    ) -> Callable[
        [site_service.BatchUpdateSitesRequest], site_service.BatchUpdateSitesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdateSites(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_site(
        self,
    ) -> Callable[[site_service.CreateSiteRequest], site_messages.Site]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateSite(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_site(self) -> Callable[[site_service.GetSiteRequest], site_messages.Site]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSite(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_sites(
        self,
    ) -> Callable[[site_service.ListSitesRequest], site_service.ListSitesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSites(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_site(
        self,
    ) -> Callable[[site_service.UpdateSiteRequest], site_messages.Site]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateSite(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseSiteServiceRestTransport._BaseCancelOperation, SiteServiceRestStub
    ):
        def __hash__(self):
            return hash("SiteServiceRestTransport.CancelOperation")

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
                _BaseSiteServiceRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSiteServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.ads.admanager_v1.SiteServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SiteService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SiteServiceRestTransport._CancelOperation._get_response(
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
        _BaseSiteServiceRestTransport._BaseGetOperation, SiteServiceRestStub
    ):
        def __hash__(self):
            return hash("SiteServiceRestTransport.GetOperation")

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
                _BaseSiteServiceRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSiteServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.ads.admanager_v1.SiteServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SiteService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SiteServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.ads.admanager_v1.SiteServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.SiteService",
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


__all__ = ("SiteServiceRestTransport",)
