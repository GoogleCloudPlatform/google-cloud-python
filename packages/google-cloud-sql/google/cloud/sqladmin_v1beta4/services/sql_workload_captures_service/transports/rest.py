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
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.sqladmin_v1beta4._compat import transcode_request
from google.cloud.sqladmin_v1beta4.types import (
    cloud_sql_resources,
    cloud_sql_workload_captures,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseSqlWorkloadCapturesServiceRestTransport

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


class SqlWorkloadCapturesServiceRestInterceptor:
    """Interceptor for SqlWorkloadCapturesService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the SqlWorkloadCapturesServiceRestTransport.

    .. code-block:: python
        class MyCustomSqlWorkloadCapturesServiceInterceptor(SqlWorkloadCapturesServiceRestInterceptor):
            def pre_list(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_start(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_start(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_start_replay(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_start_replay(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_stop(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_stop(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_stop_replay(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_stop_replay(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = SqlWorkloadCapturesServiceRestTransport(interceptor=MyCustomSqlWorkloadCapturesServiceInterceptor())
        client = SqlWorkloadCapturesServiceClient(transport=transport)


    """

    def pre_list(
        self,
        request: cloud_sql_workload_captures.SqlWorkloadCapturesListRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql_workload_captures.SqlWorkloadCapturesListRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlWorkloadCapturesService server.
        """
        return request, metadata

    def post_list(
        self, response: cloud_sql_workload_captures.WorkloadCapturesListResponse
    ) -> cloud_sql_workload_captures.WorkloadCapturesListResponse:
        """Post-rpc interceptor for list

        DEPRECATED. Please use the `post_list_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlWorkloadCapturesService server but before
        it is returned to user code. This `post_list` interceptor runs
        before the `post_list_with_metadata` interceptor.
        """
        return response

    def post_list_with_metadata(
        self,
        response: cloud_sql_workload_captures.WorkloadCapturesListResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql_workload_captures.WorkloadCapturesListResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlWorkloadCapturesService server but before it is returned to user code.

        We recommend only using this `post_list_with_metadata`
        interceptor in new development instead of the `post_list` interceptor.
        When both interceptors are used, this `post_list_with_metadata` interceptor runs after the
        `post_list` interceptor. The (possibly modified) response returned by
        `post_list` will be passed to
        `post_list_with_metadata`.
        """
        return response, metadata

    def pre_start(
        self,
        request: cloud_sql_workload_captures.WorkloadCapturesStartRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql_workload_captures.WorkloadCapturesStartRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for start

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlWorkloadCapturesService server.
        """
        return request, metadata

    def post_start(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for start

        DEPRECATED. Please use the `post_start_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlWorkloadCapturesService server but before
        it is returned to user code. This `post_start` interceptor runs
        before the `post_start_with_metadata` interceptor.
        """
        return response

    def post_start_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for start

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlWorkloadCapturesService server but before it is returned to user code.

        We recommend only using this `post_start_with_metadata`
        interceptor in new development instead of the `post_start` interceptor.
        When both interceptors are used, this `post_start_with_metadata` interceptor runs after the
        `post_start` interceptor. The (possibly modified) response returned by
        `post_start` will be passed to
        `post_start_with_metadata`.
        """
        return response, metadata

    def pre_start_replay(
        self,
        request: cloud_sql_workload_captures.WorkloadCapturesStartReplayRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql_workload_captures.WorkloadCapturesStartReplayRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for start_replay

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlWorkloadCapturesService server.
        """
        return request, metadata

    def post_start_replay(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for start_replay

        DEPRECATED. Please use the `post_start_replay_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlWorkloadCapturesService server but before
        it is returned to user code. This `post_start_replay` interceptor runs
        before the `post_start_replay_with_metadata` interceptor.
        """
        return response

    def post_start_replay_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for start_replay

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlWorkloadCapturesService server but before it is returned to user code.

        We recommend only using this `post_start_replay_with_metadata`
        interceptor in new development instead of the `post_start_replay` interceptor.
        When both interceptors are used, this `post_start_replay_with_metadata` interceptor runs after the
        `post_start_replay` interceptor. The (possibly modified) response returned by
        `post_start_replay` will be passed to
        `post_start_replay_with_metadata`.
        """
        return response, metadata

    def pre_stop(
        self,
        request: cloud_sql_workload_captures.WorkloadCapturesStopRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql_workload_captures.WorkloadCapturesStopRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for stop

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlWorkloadCapturesService server.
        """
        return request, metadata

    def post_stop(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for stop

        DEPRECATED. Please use the `post_stop_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlWorkloadCapturesService server but before
        it is returned to user code. This `post_stop` interceptor runs
        before the `post_stop_with_metadata` interceptor.
        """
        return response

    def post_stop_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for stop

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlWorkloadCapturesService server but before it is returned to user code.

        We recommend only using this `post_stop_with_metadata`
        interceptor in new development instead of the `post_stop` interceptor.
        When both interceptors are used, this `post_stop_with_metadata` interceptor runs after the
        `post_stop` interceptor. The (possibly modified) response returned by
        `post_stop` will be passed to
        `post_stop_with_metadata`.
        """
        return response, metadata

    def pre_stop_replay(
        self,
        request: cloud_sql_workload_captures.WorkloadCapturesStopReplayRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql_workload_captures.WorkloadCapturesStopReplayRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for stop_replay

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlWorkloadCapturesService server.
        """
        return request, metadata

    def post_stop_replay(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for stop_replay

        DEPRECATED. Please use the `post_stop_replay_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlWorkloadCapturesService server but before
        it is returned to user code. This `post_stop_replay` interceptor runs
        before the `post_stop_replay_with_metadata` interceptor.
        """
        return response

    def post_stop_replay_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for stop_replay

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlWorkloadCapturesService server but before it is returned to user code.

        We recommend only using this `post_stop_replay_with_metadata`
        interceptor in new development instead of the `post_stop_replay` interceptor.
        When both interceptors are used, this `post_stop_replay_with_metadata` interceptor runs after the
        `post_stop_replay` interceptor. The (possibly modified) response returned by
        `post_stop_replay` will be passed to
        `post_stop_replay_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class SqlWorkloadCapturesServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: SqlWorkloadCapturesServiceRestInterceptor


class SqlWorkloadCapturesServiceRestTransport(
    _BaseSqlWorkloadCapturesServiceRestTransport
):
    """REST backend synchronous transport for SqlWorkloadCapturesService.

    Cloud SQL Workload Captures service.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "sqladmin.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[SqlWorkloadCapturesServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'sqladmin.googleapis.com').
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
            interceptor (Optional[SqlWorkloadCapturesServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or SqlWorkloadCapturesServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _List(
        _BaseSqlWorkloadCapturesServiceRestTransport._BaseList,
        SqlWorkloadCapturesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlWorkloadCapturesServiceRestTransport.List")

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
            request: cloud_sql_workload_captures.SqlWorkloadCapturesListRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_workload_captures.WorkloadCapturesListResponse:
            r"""Call the list method over HTTP.

            Args:
                request (~.cloud_sql_workload_captures.SqlWorkloadCapturesListRequest):
                    The request object. Instance list captured workloads
                request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_workload_captures.WorkloadCapturesListResponse:
                    Instance list captured workloads
                response.

            """

            http_options = _BaseSqlWorkloadCapturesServiceRestTransport._BaseList._get_http_options()
            request, metadata = self._interceptor.pre_list(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlWorkloadCapturesServiceRestTransport._BaseList,
                    "_BaseList__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlWorkloadCapturesServiceClient.List",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlWorkloadCapturesService",
                        "rpcName": "List",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlWorkloadCapturesServiceRestTransport._List._get_response(
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
            resp = cloud_sql_workload_captures.WorkloadCapturesListResponse()
            pb_resp = cloud_sql_workload_captures.WorkloadCapturesListResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_workload_captures.WorkloadCapturesListResponse.to_json(
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
                    "Received response for google.cloud.sql_v1beta4.SqlWorkloadCapturesServiceClient.list",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlWorkloadCapturesService",
                        "rpcName": "List",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Start(
        _BaseSqlWorkloadCapturesServiceRestTransport._BaseStart,
        SqlWorkloadCapturesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlWorkloadCapturesServiceRestTransport.Start")

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
            request: cloud_sql_workload_captures.WorkloadCapturesStartRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the start method over HTTP.

            Args:
                request (~.cloud_sql_workload_captures.WorkloadCapturesStartRequest):
                    The request object. Request to start recording traffic
                from the primary instance (captured
                workload).
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.Operation:
                    An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

            """

            http_options = _BaseSqlWorkloadCapturesServiceRestTransport._BaseStart._get_http_options()
            request, metadata = self._interceptor.pre_start(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlWorkloadCapturesServiceRestTransport._BaseStart,
                    "_BaseStart__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlWorkloadCapturesServiceClient.Start",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlWorkloadCapturesService",
                        "rpcName": "Start",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlWorkloadCapturesServiceRestTransport._Start._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_start(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_start_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlWorkloadCapturesServiceClient.start",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlWorkloadCapturesService",
                        "rpcName": "Start",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _StartReplay(
        _BaseSqlWorkloadCapturesServiceRestTransport._BaseStartReplay,
        SqlWorkloadCapturesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlWorkloadCapturesServiceRestTransport.StartReplay")

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
            request: cloud_sql_workload_captures.WorkloadCapturesStartReplayRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the start replay method over HTTP.

            Args:
                request (~.cloud_sql_workload_captures.WorkloadCapturesStartReplayRequest):
                    The request object. Request to start executing a captured
                workload on a replay instance (the Cloud
                SQL instance where the recorded SQL
                queries are executed).
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.Operation:
                    An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

            """

            http_options = _BaseSqlWorkloadCapturesServiceRestTransport._BaseStartReplay._get_http_options()
            request, metadata = self._interceptor.pre_start_replay(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlWorkloadCapturesServiceRestTransport._BaseStartReplay,
                    "_BaseStartReplay__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlWorkloadCapturesServiceClient.StartReplay",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlWorkloadCapturesService",
                        "rpcName": "StartReplay",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SqlWorkloadCapturesServiceRestTransport._StartReplay._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_start_replay(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_start_replay_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlWorkloadCapturesServiceClient.start_replay",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlWorkloadCapturesService",
                        "rpcName": "StartReplay",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Stop(
        _BaseSqlWorkloadCapturesServiceRestTransport._BaseStop,
        SqlWorkloadCapturesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlWorkloadCapturesServiceRestTransport.Stop")

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
            request: cloud_sql_workload_captures.WorkloadCapturesStopRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the stop method over HTTP.

            Args:
                request (~.cloud_sql_workload_captures.WorkloadCapturesStopRequest):
                    The request object. Request to stop recording traffic
                from the primary instance.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.Operation:
                    An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

            """

            http_options = _BaseSqlWorkloadCapturesServiceRestTransport._BaseStop._get_http_options()
            request, metadata = self._interceptor.pre_stop(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlWorkloadCapturesServiceRestTransport._BaseStop,
                    "_BaseStop__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlWorkloadCapturesServiceClient.Stop",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlWorkloadCapturesService",
                        "rpcName": "Stop",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlWorkloadCapturesServiceRestTransport._Stop._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_stop(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_stop_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlWorkloadCapturesServiceClient.stop",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlWorkloadCapturesService",
                        "rpcName": "Stop",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _StopReplay(
        _BaseSqlWorkloadCapturesServiceRestTransport._BaseStopReplay,
        SqlWorkloadCapturesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlWorkloadCapturesServiceRestTransport.StopReplay")

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
            request: cloud_sql_workload_captures.WorkloadCapturesStopReplayRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the stop replay method over HTTP.

            Args:
                request (~.cloud_sql_workload_captures.WorkloadCapturesStopReplayRequest):
                    The request object. Request to stop an active workload
                replay on a target Cloud SQL replay
                instance.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.Operation:
                    An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

            """

            http_options = _BaseSqlWorkloadCapturesServiceRestTransport._BaseStopReplay._get_http_options()
            request, metadata = self._interceptor.pre_stop_replay(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlWorkloadCapturesServiceRestTransport._BaseStopReplay,
                    "_BaseStopReplay__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlWorkloadCapturesServiceClient.StopReplay",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlWorkloadCapturesService",
                        "rpcName": "StopReplay",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SqlWorkloadCapturesServiceRestTransport._StopReplay._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_stop_replay(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_stop_replay_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlWorkloadCapturesServiceClient.stop_replay",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlWorkloadCapturesService",
                        "rpcName": "StopReplay",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def list(
        self,
    ) -> Callable[
        [cloud_sql_workload_captures.SqlWorkloadCapturesListRequest],
        cloud_sql_workload_captures.WorkloadCapturesListResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._List(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def start(
        self,
    ) -> Callable[
        [cloud_sql_workload_captures.WorkloadCapturesStartRequest],
        cloud_sql_resources.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Start(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def start_replay(
        self,
    ) -> Callable[
        [cloud_sql_workload_captures.WorkloadCapturesStartReplayRequest],
        cloud_sql_resources.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StartReplay(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def stop(
        self,
    ) -> Callable[
        [cloud_sql_workload_captures.WorkloadCapturesStopRequest],
        cloud_sql_resources.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Stop(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def stop_replay(
        self,
    ) -> Callable[
        [cloud_sql_workload_captures.WorkloadCapturesStopReplayRequest],
        cloud_sql_resources.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StopReplay(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("SqlWorkloadCapturesServiceRestTransport",)
