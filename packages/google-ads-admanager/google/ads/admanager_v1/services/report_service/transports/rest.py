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
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.ads.admanager_v1._compat import transcode_request
from google.ads.admanager_v1.types import report_messages, report_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseReportServiceRestTransport

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


class ReportServiceRestInterceptor:
    """Interceptor for ReportService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ReportServiceRestTransport.

    .. code-block:: python
        class MyCustomReportServiceInterceptor(ReportServiceRestInterceptor):
            def pre_create_report(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_report(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_report_result_rows(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_report_result_rows(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_report(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_report(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_reports(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_reports(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_run_report(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_run_report(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_report(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_report(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ReportServiceRestTransport(interceptor=MyCustomReportServiceInterceptor())
        client = ReportServiceClient(transport=transport)


    """

    def pre_create_report(
        self,
        request: report_service.CreateReportRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        report_service.CreateReportRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_report

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ReportService server.
        """
        return request, metadata

    def post_create_report(
        self, response: report_messages.Report
    ) -> report_messages.Report:
        """Post-rpc interceptor for create_report

        DEPRECATED. Please use the `post_create_report_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ReportService server but before
        it is returned to user code. This `post_create_report` interceptor runs
        before the `post_create_report_with_metadata` interceptor.
        """
        return response

    def post_create_report_with_metadata(
        self,
        response: report_messages.Report,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[report_messages.Report, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_report

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ReportService server but before it is returned to user code.

        We recommend only using this `post_create_report_with_metadata`
        interceptor in new development instead of the `post_create_report` interceptor.
        When both interceptors are used, this `post_create_report_with_metadata` interceptor runs after the
        `post_create_report` interceptor. The (possibly modified) response returned by
        `post_create_report` will be passed to
        `post_create_report_with_metadata`.
        """
        return response, metadata

    def pre_fetch_report_result_rows(
        self,
        request: report_service.FetchReportResultRowsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        report_service.FetchReportResultRowsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for fetch_report_result_rows

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ReportService server.
        """
        return request, metadata

    def post_fetch_report_result_rows(
        self, response: report_service.FetchReportResultRowsResponse
    ) -> report_service.FetchReportResultRowsResponse:
        """Post-rpc interceptor for fetch_report_result_rows

        DEPRECATED. Please use the `post_fetch_report_result_rows_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ReportService server but before
        it is returned to user code. This `post_fetch_report_result_rows` interceptor runs
        before the `post_fetch_report_result_rows_with_metadata` interceptor.
        """
        return response

    def post_fetch_report_result_rows_with_metadata(
        self,
        response: report_service.FetchReportResultRowsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        report_service.FetchReportResultRowsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for fetch_report_result_rows

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ReportService server but before it is returned to user code.

        We recommend only using this `post_fetch_report_result_rows_with_metadata`
        interceptor in new development instead of the `post_fetch_report_result_rows` interceptor.
        When both interceptors are used, this `post_fetch_report_result_rows_with_metadata` interceptor runs after the
        `post_fetch_report_result_rows` interceptor. The (possibly modified) response returned by
        `post_fetch_report_result_rows` will be passed to
        `post_fetch_report_result_rows_with_metadata`.
        """
        return response, metadata

    def pre_get_report(
        self,
        request: report_service.GetReportRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        report_service.GetReportRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_report

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ReportService server.
        """
        return request, metadata

    def post_get_report(
        self, response: report_messages.Report
    ) -> report_messages.Report:
        """Post-rpc interceptor for get_report

        DEPRECATED. Please use the `post_get_report_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ReportService server but before
        it is returned to user code. This `post_get_report` interceptor runs
        before the `post_get_report_with_metadata` interceptor.
        """
        return response

    def post_get_report_with_metadata(
        self,
        response: report_messages.Report,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[report_messages.Report, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_report

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ReportService server but before it is returned to user code.

        We recommend only using this `post_get_report_with_metadata`
        interceptor in new development instead of the `post_get_report` interceptor.
        When both interceptors are used, this `post_get_report_with_metadata` interceptor runs after the
        `post_get_report` interceptor. The (possibly modified) response returned by
        `post_get_report` will be passed to
        `post_get_report_with_metadata`.
        """
        return response, metadata

    def pre_list_reports(
        self,
        request: report_service.ListReportsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        report_service.ListReportsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_reports

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ReportService server.
        """
        return request, metadata

    def post_list_reports(
        self, response: report_service.ListReportsResponse
    ) -> report_service.ListReportsResponse:
        """Post-rpc interceptor for list_reports

        DEPRECATED. Please use the `post_list_reports_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ReportService server but before
        it is returned to user code. This `post_list_reports` interceptor runs
        before the `post_list_reports_with_metadata` interceptor.
        """
        return response

    def post_list_reports_with_metadata(
        self,
        response: report_service.ListReportsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        report_service.ListReportsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_reports

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ReportService server but before it is returned to user code.

        We recommend only using this `post_list_reports_with_metadata`
        interceptor in new development instead of the `post_list_reports` interceptor.
        When both interceptors are used, this `post_list_reports_with_metadata` interceptor runs after the
        `post_list_reports` interceptor. The (possibly modified) response returned by
        `post_list_reports` will be passed to
        `post_list_reports_with_metadata`.
        """
        return response, metadata

    def pre_run_report(
        self,
        request: report_service.RunReportRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        report_service.RunReportRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for run_report

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ReportService server.
        """
        return request, metadata

    def post_run_report(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for run_report

        DEPRECATED. Please use the `post_run_report_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ReportService server but before
        it is returned to user code. This `post_run_report` interceptor runs
        before the `post_run_report_with_metadata` interceptor.
        """
        return response

    def post_run_report_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for run_report

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ReportService server but before it is returned to user code.

        We recommend only using this `post_run_report_with_metadata`
        interceptor in new development instead of the `post_run_report` interceptor.
        When both interceptors are used, this `post_run_report_with_metadata` interceptor runs after the
        `post_run_report` interceptor. The (possibly modified) response returned by
        `post_run_report` will be passed to
        `post_run_report_with_metadata`.
        """
        return response, metadata

    def pre_update_report(
        self,
        request: report_service.UpdateReportRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        report_service.UpdateReportRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_report

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ReportService server.
        """
        return request, metadata

    def post_update_report(
        self, response: report_messages.Report
    ) -> report_messages.Report:
        """Post-rpc interceptor for update_report

        DEPRECATED. Please use the `post_update_report_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ReportService server but before
        it is returned to user code. This `post_update_report` interceptor runs
        before the `post_update_report_with_metadata` interceptor.
        """
        return response

    def post_update_report_with_metadata(
        self,
        response: report_messages.Report,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[report_messages.Report, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_report

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ReportService server but before it is returned to user code.

        We recommend only using this `post_update_report_with_metadata`
        interceptor in new development instead of the `post_update_report` interceptor.
        When both interceptors are used, this `post_update_report_with_metadata` interceptor runs after the
        `post_update_report` interceptor. The (possibly modified) response returned by
        `post_update_report` will be passed to
        `post_update_report_with_metadata`.
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
        before they are sent to the ReportService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the ReportService server but before
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
        before they are sent to the ReportService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the ReportService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class ReportServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ReportServiceRestInterceptor


class ReportServiceRestTransport(_BaseReportServiceRestTransport):
    """REST backend synchronous transport for ReportService.

    Provides methods for interacting with reports.

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
        interceptor: Optional[ReportServiceRestInterceptor] = None,
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
            interceptor (Optional[ReportServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or ReportServiceRestInterceptor()
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
                "google.longrunning.Operations.CancelOperation": [
                    {
                        "method": "post",
                        "uri": "/v1/{name=networks/*/operations/reports/runs/*}:cancel",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=networks/*/operations/reports/runs/*}",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v1",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _CreateReport(
        _BaseReportServiceRestTransport._BaseCreateReport, ReportServiceRestStub
    ):
        def __hash__(self):
            return hash("ReportServiceRestTransport.CreateReport")

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
            request: report_service.CreateReportRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> report_messages.Report:
            r"""Call the create report method over HTTP.

            Args:
                request (~.report_service.CreateReportRequest):
                    The request object. Request object for ``CreateReport`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.report_messages.Report:
                    The ``Report`` resource.
            """

            http_options = (
                _BaseReportServiceRestTransport._BaseCreateReport._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_report(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReportServiceRestTransport._BaseCreateReport,
                    "_BaseCreateReport__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ReportServiceClient.CreateReport",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ReportService",
                        "rpcName": "CreateReport",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ReportServiceRestTransport._CreateReport._get_response(
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
            resp = report_messages.Report()
            pb_resp = report_messages.Report.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_report(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_report_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = report_messages.Report.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.ReportServiceClient.create_report",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ReportService",
                        "rpcName": "CreateReport",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchReportResultRows(
        _BaseReportServiceRestTransport._BaseFetchReportResultRows,
        ReportServiceRestStub,
    ):
        def __hash__(self):
            return hash("ReportServiceRestTransport.FetchReportResultRows")

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
            request: report_service.FetchReportResultRowsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> report_service.FetchReportResultRowsResponse:
            r"""Call the fetch report result rows method over HTTP.

            Args:
                request (~.report_service.FetchReportResultRowsRequest):
                    The request object. The request message for the fetch
                report result rows endpoint.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.report_service.FetchReportResultRowsResponse:
                    The response message for the fetch
                report result rows endpoint.

            """

            http_options = _BaseReportServiceRestTransport._BaseFetchReportResultRows._get_http_options()
            request, metadata = self._interceptor.pre_fetch_report_result_rows(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReportServiceRestTransport._BaseFetchReportResultRows,
                    "_BaseFetchReportResultRows__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ReportServiceClient.FetchReportResultRows",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ReportService",
                        "rpcName": "FetchReportResultRows",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ReportServiceRestTransport._FetchReportResultRows._get_response(
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
            resp = report_service.FetchReportResultRowsResponse()
            pb_resp = report_service.FetchReportResultRowsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_report_result_rows(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fetch_report_result_rows_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        report_service.FetchReportResultRowsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.ReportServiceClient.fetch_report_result_rows",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ReportService",
                        "rpcName": "FetchReportResultRows",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetReport(
        _BaseReportServiceRestTransport._BaseGetReport, ReportServiceRestStub
    ):
        def __hash__(self):
            return hash("ReportServiceRestTransport.GetReport")

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
            request: report_service.GetReportRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> report_messages.Report:
            r"""Call the get report method over HTTP.

            Args:
                request (~.report_service.GetReportRequest):
                    The request object. Request object for ``GetReport`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.report_messages.Report:
                    The ``Report`` resource.
            """

            http_options = (
                _BaseReportServiceRestTransport._BaseGetReport._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_report(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReportServiceRestTransport._BaseGetReport,
                    "_BaseGetReport__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ReportServiceClient.GetReport",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ReportService",
                        "rpcName": "GetReport",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ReportServiceRestTransport._GetReport._get_response(
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
            resp = report_messages.Report()
            pb_resp = report_messages.Report.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_report(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_report_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = report_messages.Report.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.ReportServiceClient.get_report",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ReportService",
                        "rpcName": "GetReport",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListReports(
        _BaseReportServiceRestTransport._BaseListReports, ReportServiceRestStub
    ):
        def __hash__(self):
            return hash("ReportServiceRestTransport.ListReports")

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
            request: report_service.ListReportsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> report_service.ListReportsResponse:
            r"""Call the list reports method over HTTP.

            Args:
                request (~.report_service.ListReportsRequest):
                    The request object. Request object for ``ListReports`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.report_service.ListReportsResponse:
                    Response object for ``ListReportsResponse`` containing
                matching ``Report`` objects.

            """

            http_options = (
                _BaseReportServiceRestTransport._BaseListReports._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_reports(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReportServiceRestTransport._BaseListReports,
                    "_BaseListReports__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ReportServiceClient.ListReports",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ReportService",
                        "rpcName": "ListReports",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ReportServiceRestTransport._ListReports._get_response(
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
            resp = report_service.ListReportsResponse()
            pb_resp = report_service.ListReportsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_reports(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_reports_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = report_service.ListReportsResponse.to_json(
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
                    "Received response for google.ads.admanager_v1.ReportServiceClient.list_reports",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ReportService",
                        "rpcName": "ListReports",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RunReport(
        _BaseReportServiceRestTransport._BaseRunReport, ReportServiceRestStub
    ):
        def __hash__(self):
            return hash("ReportServiceRestTransport.RunReport")

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
            request: report_service.RunReportRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the run report method over HTTP.

            Args:
                request (~.report_service.RunReportRequest):
                    The request object. Request message for a running a
                report.
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
                _BaseReportServiceRestTransport._BaseRunReport._get_http_options()
            )
            request, metadata = self._interceptor.pre_run_report(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReportServiceRestTransport._BaseRunReport,
                    "_BaseRunReport__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ReportServiceClient.RunReport",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ReportService",
                        "rpcName": "RunReport",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ReportServiceRestTransport._RunReport._get_response(
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

            resp = self._interceptor.post_run_report(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_run_report_with_metadata(
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
                    "Received response for google.ads.admanager_v1.ReportServiceClient.run_report",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ReportService",
                        "rpcName": "RunReport",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateReport(
        _BaseReportServiceRestTransport._BaseUpdateReport, ReportServiceRestStub
    ):
        def __hash__(self):
            return hash("ReportServiceRestTransport.UpdateReport")

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
            request: report_service.UpdateReportRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> report_messages.Report:
            r"""Call the update report method over HTTP.

            Args:
                request (~.report_service.UpdateReportRequest):
                    The request object. Request object for ``UpdateReport`` method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.report_messages.Report:
                    The ``Report`` resource.
            """

            http_options = (
                _BaseReportServiceRestTransport._BaseUpdateReport._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_report(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReportServiceRestTransport._BaseUpdateReport,
                    "_BaseUpdateReport__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.ads.admanager_v1.ReportServiceClient.UpdateReport",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ReportService",
                        "rpcName": "UpdateReport",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ReportServiceRestTransport._UpdateReport._get_response(
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
            resp = report_messages.Report()
            pb_resp = report_messages.Report.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_report(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_report_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = report_messages.Report.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.ads.admanager_v1.ReportServiceClient.update_report",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ReportService",
                        "rpcName": "UpdateReport",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_report(
        self,
    ) -> Callable[[report_service.CreateReportRequest], report_messages.Report]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateReport(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def fetch_report_result_rows(
        self,
    ) -> Callable[
        [report_service.FetchReportResultRowsRequest],
        report_service.FetchReportResultRowsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchReportResultRows(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_report(
        self,
    ) -> Callable[[report_service.GetReportRequest], report_messages.Report]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetReport(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_reports(
        self,
    ) -> Callable[
        [report_service.ListReportsRequest], report_service.ListReportsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListReports(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def run_report(
        self,
    ) -> Callable[[report_service.RunReportRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RunReport(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_report(
        self,
    ) -> Callable[[report_service.UpdateReportRequest], report_messages.Report]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateReport(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseReportServiceRestTransport._BaseCancelOperation, ReportServiceRestStub
    ):
        def __hash__(self):
            return hash("ReportServiceRestTransport.CancelOperation")

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
                _BaseReportServiceRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReportServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.ads.admanager_v1.ReportServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ReportService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ReportServiceRestTransport._CancelOperation._get_response(
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
        _BaseReportServiceRestTransport._BaseGetOperation, ReportServiceRestStub
    ):
        def __hash__(self):
            return hash("ReportServiceRestTransport.GetOperation")

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
                _BaseReportServiceRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseReportServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.ads.admanager_v1.ReportServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ReportService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ReportServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.ads.admanager_v1.ReportServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.ads.admanager.v1.ReportService",
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


__all__ = ("ReportServiceRestTransport",)
