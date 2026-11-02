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

from google.cloud.monitoring_dashboard_v1._compat import transcode_request
from google.cloud.monitoring_dashboard_v1.types import dashboard, dashboards_service
from google.cloud.monitoring_dashboard_v1.types import dashboard as gmd_dashboard

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseDashboardsServiceRestTransport

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


class DashboardsServiceRestInterceptor:
    """Interceptor for DashboardsService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the DashboardsServiceRestTransport.

    .. code-block:: python
        class MyCustomDashboardsServiceInterceptor(DashboardsServiceRestInterceptor):
            def pre_create_dashboard(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_dashboard(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_dashboard(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_dashboard(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_dashboard(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_dashboards(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_dashboards(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_dashboard(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_dashboard(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = DashboardsServiceRestTransport(interceptor=MyCustomDashboardsServiceInterceptor())
        client = DashboardsServiceClient(transport=transport)


    """

    def pre_create_dashboard(
        self,
        request: dashboards_service.CreateDashboardRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dashboards_service.CreateDashboardRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_dashboard

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DashboardsService server.
        """
        return request, metadata

    def post_create_dashboard(
        self, response: gmd_dashboard.Dashboard
    ) -> gmd_dashboard.Dashboard:
        """Post-rpc interceptor for create_dashboard

        DEPRECATED. Please use the `post_create_dashboard_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DashboardsService server but before
        it is returned to user code. This `post_create_dashboard` interceptor runs
        before the `post_create_dashboard_with_metadata` interceptor.
        """
        return response

    def post_create_dashboard_with_metadata(
        self,
        response: gmd_dashboard.Dashboard,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gmd_dashboard.Dashboard, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_dashboard

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DashboardsService server but before it is returned to user code.

        We recommend only using this `post_create_dashboard_with_metadata`
        interceptor in new development instead of the `post_create_dashboard` interceptor.
        When both interceptors are used, this `post_create_dashboard_with_metadata` interceptor runs after the
        `post_create_dashboard` interceptor. The (possibly modified) response returned by
        `post_create_dashboard` will be passed to
        `post_create_dashboard_with_metadata`.
        """
        return response, metadata

    def pre_delete_dashboard(
        self,
        request: dashboards_service.DeleteDashboardRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dashboards_service.DeleteDashboardRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_dashboard

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DashboardsService server.
        """
        return request, metadata

    def pre_get_dashboard(
        self,
        request: dashboards_service.GetDashboardRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dashboards_service.GetDashboardRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_dashboard

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DashboardsService server.
        """
        return request, metadata

    def post_get_dashboard(self, response: dashboard.Dashboard) -> dashboard.Dashboard:
        """Post-rpc interceptor for get_dashboard

        DEPRECATED. Please use the `post_get_dashboard_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DashboardsService server but before
        it is returned to user code. This `post_get_dashboard` interceptor runs
        before the `post_get_dashboard_with_metadata` interceptor.
        """
        return response

    def post_get_dashboard_with_metadata(
        self,
        response: dashboard.Dashboard,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dashboard.Dashboard, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_dashboard

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DashboardsService server but before it is returned to user code.

        We recommend only using this `post_get_dashboard_with_metadata`
        interceptor in new development instead of the `post_get_dashboard` interceptor.
        When both interceptors are used, this `post_get_dashboard_with_metadata` interceptor runs after the
        `post_get_dashboard` interceptor. The (possibly modified) response returned by
        `post_get_dashboard` will be passed to
        `post_get_dashboard_with_metadata`.
        """
        return response, metadata

    def pre_list_dashboards(
        self,
        request: dashboards_service.ListDashboardsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dashboards_service.ListDashboardsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_dashboards

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DashboardsService server.
        """
        return request, metadata

    def post_list_dashboards(
        self, response: dashboards_service.ListDashboardsResponse
    ) -> dashboards_service.ListDashboardsResponse:
        """Post-rpc interceptor for list_dashboards

        DEPRECATED. Please use the `post_list_dashboards_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DashboardsService server but before
        it is returned to user code. This `post_list_dashboards` interceptor runs
        before the `post_list_dashboards_with_metadata` interceptor.
        """
        return response

    def post_list_dashboards_with_metadata(
        self,
        response: dashboards_service.ListDashboardsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dashboards_service.ListDashboardsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_dashboards

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DashboardsService server but before it is returned to user code.

        We recommend only using this `post_list_dashboards_with_metadata`
        interceptor in new development instead of the `post_list_dashboards` interceptor.
        When both interceptors are used, this `post_list_dashboards_with_metadata` interceptor runs after the
        `post_list_dashboards` interceptor. The (possibly modified) response returned by
        `post_list_dashboards` will be passed to
        `post_list_dashboards_with_metadata`.
        """
        return response, metadata

    def pre_update_dashboard(
        self,
        request: dashboards_service.UpdateDashboardRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dashboards_service.UpdateDashboardRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_dashboard

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DashboardsService server.
        """
        return request, metadata

    def post_update_dashboard(
        self, response: dashboard.Dashboard
    ) -> dashboard.Dashboard:
        """Post-rpc interceptor for update_dashboard

        DEPRECATED. Please use the `post_update_dashboard_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DashboardsService server but before
        it is returned to user code. This `post_update_dashboard` interceptor runs
        before the `post_update_dashboard_with_metadata` interceptor.
        """
        return response

    def post_update_dashboard_with_metadata(
        self,
        response: dashboard.Dashboard,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dashboard.Dashboard, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_dashboard

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DashboardsService server but before it is returned to user code.

        We recommend only using this `post_update_dashboard_with_metadata`
        interceptor in new development instead of the `post_update_dashboard` interceptor.
        When both interceptors are used, this `post_update_dashboard_with_metadata` interceptor runs after the
        `post_update_dashboard` interceptor. The (possibly modified) response returned by
        `post_update_dashboard` will be passed to
        `post_update_dashboard_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class DashboardsServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: DashboardsServiceRestInterceptor


class DashboardsServiceRestTransport(_BaseDashboardsServiceRestTransport):
    """REST backend synchronous transport for DashboardsService.

    Manages Stackdriver dashboards. A dashboard is an arrangement
    of data display widgets in a specific layout.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "monitoring.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[DashboardsServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'monitoring.googleapis.com').
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
            interceptor (Optional[DashboardsServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or DashboardsServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateDashboard(
        _BaseDashboardsServiceRestTransport._BaseCreateDashboard,
        DashboardsServiceRestStub,
    ):
        def __hash__(self):
            return hash("DashboardsServiceRestTransport.CreateDashboard")

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
            request: dashboards_service.CreateDashboardRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gmd_dashboard.Dashboard:
            r"""Call the create dashboard method over HTTP.

            Args:
                request (~.dashboards_service.CreateDashboardRequest):
                    The request object. The ``CreateDashboard`` request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gmd_dashboard.Dashboard:
                    A Google Stackdriver dashboard.
                Dashboards define the content and layout
                of pages in the Stackdriver web
                application.

            """

            http_options = _BaseDashboardsServiceRestTransport._BaseCreateDashboard._get_http_options()
            request, metadata = self._interceptor.pre_create_dashboard(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDashboardsServiceRestTransport._BaseCreateDashboard,
                    "_BaseCreateDashboard__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.monitoring.dashboard_v1.DashboardsServiceClient.CreateDashboard",
                    extra={
                        "serviceName": "google.monitoring.dashboard.v1.DashboardsService",
                        "rpcName": "CreateDashboard",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DashboardsServiceRestTransport._CreateDashboard._get_response(
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
            resp = gmd_dashboard.Dashboard()
            pb_resp = gmd_dashboard.Dashboard.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_dashboard(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_dashboard_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gmd_dashboard.Dashboard.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.monitoring.dashboard_v1.DashboardsServiceClient.create_dashboard",
                    extra={
                        "serviceName": "google.monitoring.dashboard.v1.DashboardsService",
                        "rpcName": "CreateDashboard",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteDashboard(
        _BaseDashboardsServiceRestTransport._BaseDeleteDashboard,
        DashboardsServiceRestStub,
    ):
        def __hash__(self):
            return hash("DashboardsServiceRestTransport.DeleteDashboard")

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
            request: dashboards_service.DeleteDashboardRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete dashboard method over HTTP.

            Args:
                request (~.dashboards_service.DeleteDashboardRequest):
                    The request object. The ``DeleteDashboard`` request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseDashboardsServiceRestTransport._BaseDeleteDashboard._get_http_options()
            request, metadata = self._interceptor.pre_delete_dashboard(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDashboardsServiceRestTransport._BaseDeleteDashboard,
                    "_BaseDeleteDashboard__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.monitoring.dashboard_v1.DashboardsServiceClient.DeleteDashboard",
                    extra={
                        "serviceName": "google.monitoring.dashboard.v1.DashboardsService",
                        "rpcName": "DeleteDashboard",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DashboardsServiceRestTransport._DeleteDashboard._get_response(
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

    class _GetDashboard(
        _BaseDashboardsServiceRestTransport._BaseGetDashboard, DashboardsServiceRestStub
    ):
        def __hash__(self):
            return hash("DashboardsServiceRestTransport.GetDashboard")

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
            request: dashboards_service.GetDashboardRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dashboard.Dashboard:
            r"""Call the get dashboard method over HTTP.

            Args:
                request (~.dashboards_service.GetDashboardRequest):
                    The request object. The ``GetDashboard`` request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dashboard.Dashboard:
                    A Google Stackdriver dashboard.
                Dashboards define the content and layout
                of pages in the Stackdriver web
                application.

            """

            http_options = _BaseDashboardsServiceRestTransport._BaseGetDashboard._get_http_options()
            request, metadata = self._interceptor.pre_get_dashboard(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDashboardsServiceRestTransport._BaseGetDashboard,
                    "_BaseGetDashboard__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.monitoring.dashboard_v1.DashboardsServiceClient.GetDashboard",
                    extra={
                        "serviceName": "google.monitoring.dashboard.v1.DashboardsService",
                        "rpcName": "GetDashboard",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DashboardsServiceRestTransport._GetDashboard._get_response(
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
            resp = dashboard.Dashboard()
            pb_resp = dashboard.Dashboard.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_dashboard(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_dashboard_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dashboard.Dashboard.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.monitoring.dashboard_v1.DashboardsServiceClient.get_dashboard",
                    extra={
                        "serviceName": "google.monitoring.dashboard.v1.DashboardsService",
                        "rpcName": "GetDashboard",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDashboards(
        _BaseDashboardsServiceRestTransport._BaseListDashboards,
        DashboardsServiceRestStub,
    ):
        def __hash__(self):
            return hash("DashboardsServiceRestTransport.ListDashboards")

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
            request: dashboards_service.ListDashboardsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dashboards_service.ListDashboardsResponse:
            r"""Call the list dashboards method over HTTP.

            Args:
                request (~.dashboards_service.ListDashboardsRequest):
                    The request object. The ``ListDashboards`` request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dashboards_service.ListDashboardsResponse:
                    The ``ListDashboards`` request.
            """

            http_options = _BaseDashboardsServiceRestTransport._BaseListDashboards._get_http_options()
            request, metadata = self._interceptor.pre_list_dashboards(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDashboardsServiceRestTransport._BaseListDashboards,
                    "_BaseListDashboards__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.monitoring.dashboard_v1.DashboardsServiceClient.ListDashboards",
                    extra={
                        "serviceName": "google.monitoring.dashboard.v1.DashboardsService",
                        "rpcName": "ListDashboards",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DashboardsServiceRestTransport._ListDashboards._get_response(
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
            resp = dashboards_service.ListDashboardsResponse()
            pb_resp = dashboards_service.ListDashboardsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_dashboards(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_dashboards_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        dashboards_service.ListDashboardsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.monitoring.dashboard_v1.DashboardsServiceClient.list_dashboards",
                    extra={
                        "serviceName": "google.monitoring.dashboard.v1.DashboardsService",
                        "rpcName": "ListDashboards",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDashboard(
        _BaseDashboardsServiceRestTransport._BaseUpdateDashboard,
        DashboardsServiceRestStub,
    ):
        def __hash__(self):
            return hash("DashboardsServiceRestTransport.UpdateDashboard")

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
            request: dashboards_service.UpdateDashboardRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dashboard.Dashboard:
            r"""Call the update dashboard method over HTTP.

            Args:
                request (~.dashboards_service.UpdateDashboardRequest):
                    The request object. The ``UpdateDashboard`` request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dashboard.Dashboard:
                    A Google Stackdriver dashboard.
                Dashboards define the content and layout
                of pages in the Stackdriver web
                application.

            """

            http_options = _BaseDashboardsServiceRestTransport._BaseUpdateDashboard._get_http_options()
            request, metadata = self._interceptor.pre_update_dashboard(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDashboardsServiceRestTransport._BaseUpdateDashboard,
                    "_BaseUpdateDashboard__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.monitoring.dashboard_v1.DashboardsServiceClient.UpdateDashboard",
                    extra={
                        "serviceName": "google.monitoring.dashboard.v1.DashboardsService",
                        "rpcName": "UpdateDashboard",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DashboardsServiceRestTransport._UpdateDashboard._get_response(
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
            resp = dashboard.Dashboard()
            pb_resp = dashboard.Dashboard.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_dashboard(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_dashboard_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dashboard.Dashboard.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.monitoring.dashboard_v1.DashboardsServiceClient.update_dashboard",
                    extra={
                        "serviceName": "google.monitoring.dashboard.v1.DashboardsService",
                        "rpcName": "UpdateDashboard",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_dashboard(
        self,
    ) -> Callable[[dashboards_service.CreateDashboardRequest], gmd_dashboard.Dashboard]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDashboard(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_dashboard(
        self,
    ) -> Callable[[dashboards_service.DeleteDashboardRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDashboard(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_dashboard(
        self,
    ) -> Callable[[dashboards_service.GetDashboardRequest], dashboard.Dashboard]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDashboard(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_dashboards(
        self,
    ) -> Callable[
        [dashboards_service.ListDashboardsRequest],
        dashboards_service.ListDashboardsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDashboards(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_dashboard(
        self,
    ) -> Callable[[dashboards_service.UpdateDashboardRequest], dashboard.Dashboard]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDashboard(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("DashboardsServiceRestTransport",)
