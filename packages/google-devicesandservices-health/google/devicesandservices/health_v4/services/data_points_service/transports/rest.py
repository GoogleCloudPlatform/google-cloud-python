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

from google.devicesandservices.health_v4._compat import transcode_request
from google.devicesandservices.health_v4.types import data_points

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseDataPointsServiceRestTransport

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


class DataPointsServiceRestInterceptor:
    """Interceptor for DataPointsService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the DataPointsServiceRestTransport.

    .. code-block:: python
        class MyCustomDataPointsServiceInterceptor(DataPointsServiceRestInterceptor):
            def pre_batch_delete_data_points(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_delete_data_points(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_data_point(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_data_point(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_daily_roll_up_data_points(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_daily_roll_up_data_points(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_export_exercise_tcx(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export_exercise_tcx(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_data_point(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_data_point(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_data_points(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_data_points(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_reconcile_data_points(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_reconcile_data_points(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_roll_up_data_points(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_roll_up_data_points(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_data_point(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_data_point(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = DataPointsServiceRestTransport(interceptor=MyCustomDataPointsServiceInterceptor())
        client = DataPointsServiceClient(transport=transport)


    """

    def pre_batch_delete_data_points(
        self,
        request: data_points.BatchDeleteDataPointsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_points.BatchDeleteDataPointsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_delete_data_points

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataPointsService server.
        """
        return request, metadata

    def post_batch_delete_data_points(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for batch_delete_data_points

        DEPRECATED. Please use the `post_batch_delete_data_points_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataPointsService server but before
        it is returned to user code. This `post_batch_delete_data_points` interceptor runs
        before the `post_batch_delete_data_points_with_metadata` interceptor.
        """
        return response

    def post_batch_delete_data_points_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for batch_delete_data_points

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataPointsService server but before it is returned to user code.

        We recommend only using this `post_batch_delete_data_points_with_metadata`
        interceptor in new development instead of the `post_batch_delete_data_points` interceptor.
        When both interceptors are used, this `post_batch_delete_data_points_with_metadata` interceptor runs after the
        `post_batch_delete_data_points` interceptor. The (possibly modified) response returned by
        `post_batch_delete_data_points` will be passed to
        `post_batch_delete_data_points_with_metadata`.
        """
        return response, metadata

    def pre_create_data_point(
        self,
        request: data_points.CreateDataPointRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_points.CreateDataPointRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_data_point

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataPointsService server.
        """
        return request, metadata

    def post_create_data_point(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_data_point

        DEPRECATED. Please use the `post_create_data_point_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataPointsService server but before
        it is returned to user code. This `post_create_data_point` interceptor runs
        before the `post_create_data_point_with_metadata` interceptor.
        """
        return response

    def post_create_data_point_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_data_point

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataPointsService server but before it is returned to user code.

        We recommend only using this `post_create_data_point_with_metadata`
        interceptor in new development instead of the `post_create_data_point` interceptor.
        When both interceptors are used, this `post_create_data_point_with_metadata` interceptor runs after the
        `post_create_data_point` interceptor. The (possibly modified) response returned by
        `post_create_data_point` will be passed to
        `post_create_data_point_with_metadata`.
        """
        return response, metadata

    def pre_daily_roll_up_data_points(
        self,
        request: data_points.DailyRollUpDataPointsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_points.DailyRollUpDataPointsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for daily_roll_up_data_points

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataPointsService server.
        """
        return request, metadata

    def post_daily_roll_up_data_points(
        self, response: data_points.DailyRollUpDataPointsResponse
    ) -> data_points.DailyRollUpDataPointsResponse:
        """Post-rpc interceptor for daily_roll_up_data_points

        DEPRECATED. Please use the `post_daily_roll_up_data_points_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataPointsService server but before
        it is returned to user code. This `post_daily_roll_up_data_points` interceptor runs
        before the `post_daily_roll_up_data_points_with_metadata` interceptor.
        """
        return response

    def post_daily_roll_up_data_points_with_metadata(
        self,
        response: data_points.DailyRollUpDataPointsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_points.DailyRollUpDataPointsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for daily_roll_up_data_points

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataPointsService server but before it is returned to user code.

        We recommend only using this `post_daily_roll_up_data_points_with_metadata`
        interceptor in new development instead of the `post_daily_roll_up_data_points` interceptor.
        When both interceptors are used, this `post_daily_roll_up_data_points_with_metadata` interceptor runs after the
        `post_daily_roll_up_data_points` interceptor. The (possibly modified) response returned by
        `post_daily_roll_up_data_points` will be passed to
        `post_daily_roll_up_data_points_with_metadata`.
        """
        return response, metadata

    def pre_export_exercise_tcx(
        self,
        request: data_points.ExportExerciseTcxRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_points.ExportExerciseTcxRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for export_exercise_tcx

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataPointsService server.
        """
        return request, metadata

    def post_export_exercise_tcx(
        self, response: data_points.ExportExerciseTcxResponse
    ) -> data_points.ExportExerciseTcxResponse:
        """Post-rpc interceptor for export_exercise_tcx

        DEPRECATED. Please use the `post_export_exercise_tcx_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataPointsService server but before
        it is returned to user code. This `post_export_exercise_tcx` interceptor runs
        before the `post_export_exercise_tcx_with_metadata` interceptor.
        """
        return response

    def post_export_exercise_tcx_with_metadata(
        self,
        response: data_points.ExportExerciseTcxResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_points.ExportExerciseTcxResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for export_exercise_tcx

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataPointsService server but before it is returned to user code.

        We recommend only using this `post_export_exercise_tcx_with_metadata`
        interceptor in new development instead of the `post_export_exercise_tcx` interceptor.
        When both interceptors are used, this `post_export_exercise_tcx_with_metadata` interceptor runs after the
        `post_export_exercise_tcx` interceptor. The (possibly modified) response returned by
        `post_export_exercise_tcx` will be passed to
        `post_export_exercise_tcx_with_metadata`.
        """
        return response, metadata

    def pre_get_data_point(
        self,
        request: data_points.GetDataPointRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_points.GetDataPointRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_data_point

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataPointsService server.
        """
        return request, metadata

    def post_get_data_point(
        self, response: data_points.DataPoint
    ) -> data_points.DataPoint:
        """Post-rpc interceptor for get_data_point

        DEPRECATED. Please use the `post_get_data_point_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataPointsService server but before
        it is returned to user code. This `post_get_data_point` interceptor runs
        before the `post_get_data_point_with_metadata` interceptor.
        """
        return response

    def post_get_data_point_with_metadata(
        self,
        response: data_points.DataPoint,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[data_points.DataPoint, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_data_point

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataPointsService server but before it is returned to user code.

        We recommend only using this `post_get_data_point_with_metadata`
        interceptor in new development instead of the `post_get_data_point` interceptor.
        When both interceptors are used, this `post_get_data_point_with_metadata` interceptor runs after the
        `post_get_data_point` interceptor. The (possibly modified) response returned by
        `post_get_data_point` will be passed to
        `post_get_data_point_with_metadata`.
        """
        return response, metadata

    def pre_list_data_points(
        self,
        request: data_points.ListDataPointsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_points.ListDataPointsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_data_points

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataPointsService server.
        """
        return request, metadata

    def post_list_data_points(
        self, response: data_points.ListDataPointsResponse
    ) -> data_points.ListDataPointsResponse:
        """Post-rpc interceptor for list_data_points

        DEPRECATED. Please use the `post_list_data_points_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataPointsService server but before
        it is returned to user code. This `post_list_data_points` interceptor runs
        before the `post_list_data_points_with_metadata` interceptor.
        """
        return response

    def post_list_data_points_with_metadata(
        self,
        response: data_points.ListDataPointsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_points.ListDataPointsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_data_points

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataPointsService server but before it is returned to user code.

        We recommend only using this `post_list_data_points_with_metadata`
        interceptor in new development instead of the `post_list_data_points` interceptor.
        When both interceptors are used, this `post_list_data_points_with_metadata` interceptor runs after the
        `post_list_data_points` interceptor. The (possibly modified) response returned by
        `post_list_data_points` will be passed to
        `post_list_data_points_with_metadata`.
        """
        return response, metadata

    def pre_reconcile_data_points(
        self,
        request: data_points.ReconcileDataPointsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_points.ReconcileDataPointsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for reconcile_data_points

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataPointsService server.
        """
        return request, metadata

    def post_reconcile_data_points(
        self, response: data_points.ReconcileDataPointsResponse
    ) -> data_points.ReconcileDataPointsResponse:
        """Post-rpc interceptor for reconcile_data_points

        DEPRECATED. Please use the `post_reconcile_data_points_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataPointsService server but before
        it is returned to user code. This `post_reconcile_data_points` interceptor runs
        before the `post_reconcile_data_points_with_metadata` interceptor.
        """
        return response

    def post_reconcile_data_points_with_metadata(
        self,
        response: data_points.ReconcileDataPointsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_points.ReconcileDataPointsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for reconcile_data_points

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataPointsService server but before it is returned to user code.

        We recommend only using this `post_reconcile_data_points_with_metadata`
        interceptor in new development instead of the `post_reconcile_data_points` interceptor.
        When both interceptors are used, this `post_reconcile_data_points_with_metadata` interceptor runs after the
        `post_reconcile_data_points` interceptor. The (possibly modified) response returned by
        `post_reconcile_data_points` will be passed to
        `post_reconcile_data_points_with_metadata`.
        """
        return response, metadata

    def pre_roll_up_data_points(
        self,
        request: data_points.RollUpDataPointsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_points.RollUpDataPointsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for roll_up_data_points

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataPointsService server.
        """
        return request, metadata

    def post_roll_up_data_points(
        self, response: data_points.RollUpDataPointsResponse
    ) -> data_points.RollUpDataPointsResponse:
        """Post-rpc interceptor for roll_up_data_points

        DEPRECATED. Please use the `post_roll_up_data_points_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataPointsService server but before
        it is returned to user code. This `post_roll_up_data_points` interceptor runs
        before the `post_roll_up_data_points_with_metadata` interceptor.
        """
        return response

    def post_roll_up_data_points_with_metadata(
        self,
        response: data_points.RollUpDataPointsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_points.RollUpDataPointsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for roll_up_data_points

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataPointsService server but before it is returned to user code.

        We recommend only using this `post_roll_up_data_points_with_metadata`
        interceptor in new development instead of the `post_roll_up_data_points` interceptor.
        When both interceptors are used, this `post_roll_up_data_points_with_metadata` interceptor runs after the
        `post_roll_up_data_points` interceptor. The (possibly modified) response returned by
        `post_roll_up_data_points` will be passed to
        `post_roll_up_data_points_with_metadata`.
        """
        return response, metadata

    def pre_update_data_point(
        self,
        request: data_points.UpdateDataPointRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_points.UpdateDataPointRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_data_point

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataPointsService server.
        """
        return request, metadata

    def post_update_data_point(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_data_point

        DEPRECATED. Please use the `post_update_data_point_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataPointsService server but before
        it is returned to user code. This `post_update_data_point` interceptor runs
        before the `post_update_data_point_with_metadata` interceptor.
        """
        return response

    def post_update_data_point_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_data_point

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataPointsService server but before it is returned to user code.

        We recommend only using this `post_update_data_point_with_metadata`
        interceptor in new development instead of the `post_update_data_point` interceptor.
        When both interceptors are used, this `post_update_data_point_with_metadata` interceptor runs after the
        `post_update_data_point` interceptor. The (possibly modified) response returned by
        `post_update_data_point` will be passed to
        `post_update_data_point_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class DataPointsServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: DataPointsServiceRestInterceptor


class DataPointsServiceRestTransport(_BaseDataPointsServiceRestTransport):
    """REST backend synchronous transport for DataPointsService.

    Data Points Service exposing the user's health and fitness
    measured and derived data.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "health.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[DataPointsServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'health.googleapis.com').
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
            interceptor (Optional[DataPointsServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or DataPointsServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    @property
    def operations_client(self) -> operations_v1.AbstractOperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Only create a new client if we do not already have one.
        if self._operations_client is None:
            http_options: Dict[str, List[Dict[str, str]]] = {}

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v4",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _BatchDeleteDataPoints(
        _BaseDataPointsServiceRestTransport._BaseBatchDeleteDataPoints,
        DataPointsServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataPointsServiceRestTransport.BatchDeleteDataPoints")

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
            request: data_points.BatchDeleteDataPointsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the batch delete data points method over HTTP.

            Args:
                request (~.data_points.BatchDeleteDataPointsRequest):
                    The request object. Request to delete a batch of
                identifiable data points.
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

            http_options = _BaseDataPointsServiceRestTransport._BaseBatchDeleteDataPoints._get_http_options()
            request, metadata = self._interceptor.pre_batch_delete_data_points(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataPointsServiceRestTransport._BaseBatchDeleteDataPoints,
                    "_BaseBatchDeleteDataPoints__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devicesandservices.health_v4.DataPointsServiceClient.BatchDeleteDataPoints",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.DataPointsService",
                        "rpcName": "BatchDeleteDataPoints",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataPointsServiceRestTransport._BatchDeleteDataPoints._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_delete_data_points(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_delete_data_points_with_metadata(
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
                    "Received response for google.devicesandservices.health_v4.DataPointsServiceClient.batch_delete_data_points",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.DataPointsService",
                        "rpcName": "BatchDeleteDataPoints",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateDataPoint(
        _BaseDataPointsServiceRestTransport._BaseCreateDataPoint,
        DataPointsServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataPointsServiceRestTransport.CreateDataPoint")

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
            request: data_points.CreateDataPointRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create data point method over HTTP.

            Args:
                request (~.data_points.CreateDataPointRequest):
                    The request object. Request to create an identifiable
                data point.
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

            http_options = _BaseDataPointsServiceRestTransport._BaseCreateDataPoint._get_http_options()
            request, metadata = self._interceptor.pre_create_data_point(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataPointsServiceRestTransport._BaseCreateDataPoint,
                    "_BaseCreateDataPoint__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devicesandservices.health_v4.DataPointsServiceClient.CreateDataPoint",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.DataPointsService",
                        "rpcName": "CreateDataPoint",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataPointsServiceRestTransport._CreateDataPoint._get_response(
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

            resp = self._interceptor.post_create_data_point(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_data_point_with_metadata(
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
                    "Received response for google.devicesandservices.health_v4.DataPointsServiceClient.create_data_point",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.DataPointsService",
                        "rpcName": "CreateDataPoint",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DailyRollUpDataPoints(
        _BaseDataPointsServiceRestTransport._BaseDailyRollUpDataPoints,
        DataPointsServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataPointsServiceRestTransport.DailyRollUpDataPoints")

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
            request: data_points.DailyRollUpDataPointsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_points.DailyRollUpDataPointsResponse:
            r"""Call the daily roll up data points method over HTTP.

            Args:
                request (~.data_points.DailyRollUpDataPointsRequest):
                    The request object. Request to roll up data points by
                civil time intervals.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.data_points.DailyRollUpDataPointsResponse:
                    Response containing the list of
                rolled up data points.

            """

            http_options = _BaseDataPointsServiceRestTransport._BaseDailyRollUpDataPoints._get_http_options()
            request, metadata = self._interceptor.pre_daily_roll_up_data_points(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataPointsServiceRestTransport._BaseDailyRollUpDataPoints,
                    "_BaseDailyRollUpDataPoints__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devicesandservices.health_v4.DataPointsServiceClient.DailyRollUpDataPoints",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.DataPointsService",
                        "rpcName": "DailyRollUpDataPoints",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataPointsServiceRestTransport._DailyRollUpDataPoints._get_response(
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
            resp = data_points.DailyRollUpDataPointsResponse()
            pb_resp = data_points.DailyRollUpDataPointsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_daily_roll_up_data_points(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_daily_roll_up_data_points_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        data_points.DailyRollUpDataPointsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devicesandservices.health_v4.DataPointsServiceClient.daily_roll_up_data_points",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.DataPointsService",
                        "rpcName": "DailyRollUpDataPoints",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ExportExerciseTcx(
        _BaseDataPointsServiceRestTransport._BaseExportExerciseTcx,
        DataPointsServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataPointsServiceRestTransport.ExportExerciseTcx")

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
            request: data_points.ExportExerciseTcxRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_points.ExportExerciseTcxResponse:
            r"""Call the export exercise tcx method over HTTP.

            Args:
                request (~.data_points.ExportExerciseTcxRequest):
                    The request object. Represents a request to export
                exercise data in TCX format.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.data_points.ExportExerciseTcxResponse:
                    Represents a Response for exporting
                exercise data in TCX format.

            """

            http_options = _BaseDataPointsServiceRestTransport._BaseExportExerciseTcx._get_http_options()
            request, metadata = self._interceptor.pre_export_exercise_tcx(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataPointsServiceRestTransport._BaseExportExerciseTcx,
                    "_BaseExportExerciseTcx__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devicesandservices.health_v4.DataPointsServiceClient.ExportExerciseTcx",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.DataPointsService",
                        "rpcName": "ExportExerciseTcx",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataPointsServiceRestTransport._ExportExerciseTcx._get_response(
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
            resp = data_points.ExportExerciseTcxResponse()
            pb_resp = data_points.ExportExerciseTcxResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_export_exercise_tcx(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_export_exercise_tcx_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = data_points.ExportExerciseTcxResponse.to_json(
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
                    "Received response for google.devicesandservices.health_v4.DataPointsServiceClient.export_exercise_tcx",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.DataPointsService",
                        "rpcName": "ExportExerciseTcx",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDataPoint(
        _BaseDataPointsServiceRestTransport._BaseGetDataPoint, DataPointsServiceRestStub
    ):
        def __hash__(self):
            return hash("DataPointsServiceRestTransport.GetDataPoint")

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
            request: data_points.GetDataPointRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_points.DataPoint:
            r"""Call the get data point method over HTTP.

            Args:
                request (~.data_points.GetDataPointRequest):
                    The request object. Request for getting a single data
                point
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.data_points.DataPoint:
                    A computed or recorded metric.
            """

            http_options = _BaseDataPointsServiceRestTransport._BaseGetDataPoint._get_http_options()
            request, metadata = self._interceptor.pre_get_data_point(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataPointsServiceRestTransport._BaseGetDataPoint,
                    "_BaseGetDataPoint__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devicesandservices.health_v4.DataPointsServiceClient.GetDataPoint",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.DataPointsService",
                        "rpcName": "GetDataPoint",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataPointsServiceRestTransport._GetDataPoint._get_response(
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
            resp = data_points.DataPoint()
            pb_resp = data_points.DataPoint.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_data_point(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_data_point_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = data_points.DataPoint.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.devicesandservices.health_v4.DataPointsServiceClient.get_data_point",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.DataPointsService",
                        "rpcName": "GetDataPoint",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDataPoints(
        _BaseDataPointsServiceRestTransport._BaseListDataPoints,
        DataPointsServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataPointsServiceRestTransport.ListDataPoints")

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
            request: data_points.ListDataPointsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_points.ListDataPointsResponse:
            r"""Call the list data points method over HTTP.

            Args:
                request (~.data_points.ListDataPointsRequest):
                    The request object. Request for listing raw data points
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.data_points.ListDataPointsResponse:
                    Response containing raw data points
                matching the query

            """

            http_options = _BaseDataPointsServiceRestTransport._BaseListDataPoints._get_http_options()
            request, metadata = self._interceptor.pre_list_data_points(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataPointsServiceRestTransport._BaseListDataPoints,
                    "_BaseListDataPoints__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devicesandservices.health_v4.DataPointsServiceClient.ListDataPoints",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.DataPointsService",
                        "rpcName": "ListDataPoints",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataPointsServiceRestTransport._ListDataPoints._get_response(
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
            resp = data_points.ListDataPointsResponse()
            pb_resp = data_points.ListDataPointsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_data_points(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_data_points_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = data_points.ListDataPointsResponse.to_json(
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
                    "Received response for google.devicesandservices.health_v4.DataPointsServiceClient.list_data_points",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.DataPointsService",
                        "rpcName": "ListDataPoints",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ReconcileDataPoints(
        _BaseDataPointsServiceRestTransport._BaseReconcileDataPoints,
        DataPointsServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataPointsServiceRestTransport.ReconcileDataPoints")

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
            request: data_points.ReconcileDataPointsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_points.ReconcileDataPointsResponse:
            r"""Call the reconcile data points method over HTTP.

            Args:
                request (~.data_points.ReconcileDataPointsRequest):
                    The request object. Request to reconcile data points from
                multiple data sources.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.data_points.ReconcileDataPointsResponse:
                    Response containing the list of
                reconciled DataPoints.

            """

            http_options = _BaseDataPointsServiceRestTransport._BaseReconcileDataPoints._get_http_options()
            request, metadata = self._interceptor.pre_reconcile_data_points(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataPointsServiceRestTransport._BaseReconcileDataPoints,
                    "_BaseReconcileDataPoints__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devicesandservices.health_v4.DataPointsServiceClient.ReconcileDataPoints",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.DataPointsService",
                        "rpcName": "ReconcileDataPoints",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataPointsServiceRestTransport._ReconcileDataPoints._get_response(
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
            resp = data_points.ReconcileDataPointsResponse()
            pb_resp = data_points.ReconcileDataPointsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_reconcile_data_points(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_reconcile_data_points_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = data_points.ReconcileDataPointsResponse.to_json(
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
                    "Received response for google.devicesandservices.health_v4.DataPointsServiceClient.reconcile_data_points",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.DataPointsService",
                        "rpcName": "ReconcileDataPoints",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RollUpDataPoints(
        _BaseDataPointsServiceRestTransport._BaseRollUpDataPoints,
        DataPointsServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataPointsServiceRestTransport.RollUpDataPoints")

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
            request: data_points.RollUpDataPointsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_points.RollUpDataPointsResponse:
            r"""Call the roll up data points method over HTTP.

            Args:
                request (~.data_points.RollUpDataPointsRequest):
                    The request object. Request to roll up data points by
                physical time intervals.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.data_points.RollUpDataPointsResponse:
                    Response containing the list of
                rolled up data points.

            """

            http_options = _BaseDataPointsServiceRestTransport._BaseRollUpDataPoints._get_http_options()
            request, metadata = self._interceptor.pre_roll_up_data_points(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataPointsServiceRestTransport._BaseRollUpDataPoints,
                    "_BaseRollUpDataPoints__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devicesandservices.health_v4.DataPointsServiceClient.RollUpDataPoints",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.DataPointsService",
                        "rpcName": "RollUpDataPoints",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataPointsServiceRestTransport._RollUpDataPoints._get_response(
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
            resp = data_points.RollUpDataPointsResponse()
            pb_resp = data_points.RollUpDataPointsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_roll_up_data_points(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_roll_up_data_points_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = data_points.RollUpDataPointsResponse.to_json(
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
                    "Received response for google.devicesandservices.health_v4.DataPointsServiceClient.roll_up_data_points",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.DataPointsService",
                        "rpcName": "RollUpDataPoints",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDataPoint(
        _BaseDataPointsServiceRestTransport._BaseUpdateDataPoint,
        DataPointsServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataPointsServiceRestTransport.UpdateDataPoint")

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
            request: data_points.UpdateDataPointRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update data point method over HTTP.

            Args:
                request (~.data_points.UpdateDataPointRequest):
                    The request object. Request to update an identifiable
                data point.
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

            http_options = _BaseDataPointsServiceRestTransport._BaseUpdateDataPoint._get_http_options()
            request, metadata = self._interceptor.pre_update_data_point(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataPointsServiceRestTransport._BaseUpdateDataPoint,
                    "_BaseUpdateDataPoint__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.devicesandservices.health_v4.DataPointsServiceClient.UpdateDataPoint",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.DataPointsService",
                        "rpcName": "UpdateDataPoint",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataPointsServiceRestTransport._UpdateDataPoint._get_response(
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

            resp = self._interceptor.post_update_data_point(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_data_point_with_metadata(
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
                    "Received response for google.devicesandservices.health_v4.DataPointsServiceClient.update_data_point",
                    extra={
                        "serviceName": "google.devicesandservices.health.v4.DataPointsService",
                        "rpcName": "UpdateDataPoint",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_delete_data_points(
        self,
    ) -> Callable[[data_points.BatchDeleteDataPointsRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchDeleteDataPoints(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_data_point(
        self,
    ) -> Callable[[data_points.CreateDataPointRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDataPoint(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def daily_roll_up_data_points(
        self,
    ) -> Callable[
        [data_points.DailyRollUpDataPointsRequest],
        data_points.DailyRollUpDataPointsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DailyRollUpDataPoints(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def export_exercise_tcx(
        self,
    ) -> Callable[
        [data_points.ExportExerciseTcxRequest], data_points.ExportExerciseTcxResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportExerciseTcx(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_data_point(
        self,
    ) -> Callable[[data_points.GetDataPointRequest], data_points.DataPoint]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDataPoint(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_data_points(
        self,
    ) -> Callable[
        [data_points.ListDataPointsRequest], data_points.ListDataPointsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDataPoints(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def reconcile_data_points(
        self,
    ) -> Callable[
        [data_points.ReconcileDataPointsRequest],
        data_points.ReconcileDataPointsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ReconcileDataPoints(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def roll_up_data_points(
        self,
    ) -> Callable[
        [data_points.RollUpDataPointsRequest], data_points.RollUpDataPointsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RollUpDataPoints(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_data_point(
        self,
    ) -> Callable[[data_points.UpdateDataPointRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDataPoint(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("DataPointsServiceRestTransport",)
