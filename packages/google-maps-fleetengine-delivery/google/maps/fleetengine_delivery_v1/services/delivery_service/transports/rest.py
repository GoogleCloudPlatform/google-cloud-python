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

from google.maps.fleetengine_delivery_v1._compat import transcode_request
from google.maps.fleetengine_delivery_v1.types import (
    delivery_api,
    delivery_vehicles,
    task_tracking_info,
    tasks,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseDeliveryServiceRestTransport

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


class DeliveryServiceRestInterceptor:
    """Interceptor for DeliveryService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the DeliveryServiceRestTransport.

    .. code-block:: python
        class MyCustomDeliveryServiceInterceptor(DeliveryServiceRestInterceptor):
            def pre_batch_create_tasks(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_tasks(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_delivery_vehicle(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_delivery_vehicle(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_task(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_task(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_delivery_vehicle(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_task(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_delivery_vehicle(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_delivery_vehicle(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_task(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_task(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_task_tracking_info(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_task_tracking_info(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_delivery_vehicles(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_delivery_vehicles(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_tasks(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_tasks(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_delivery_vehicle(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_delivery_vehicle(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_task(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_task(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = DeliveryServiceRestTransport(interceptor=MyCustomDeliveryServiceInterceptor())
        client = DeliveryServiceClient(transport=transport)


    """

    def pre_batch_create_tasks(
        self,
        request: delivery_api.BatchCreateTasksRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        delivery_api.BatchCreateTasksRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for batch_create_tasks

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeliveryService server.
        """
        return request, metadata

    def post_batch_create_tasks(
        self, response: delivery_api.BatchCreateTasksResponse
    ) -> delivery_api.BatchCreateTasksResponse:
        """Post-rpc interceptor for batch_create_tasks

        DEPRECATED. Please use the `post_batch_create_tasks_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeliveryService server but before
        it is returned to user code. This `post_batch_create_tasks` interceptor runs
        before the `post_batch_create_tasks_with_metadata` interceptor.
        """
        return response

    def post_batch_create_tasks_with_metadata(
        self,
        response: delivery_api.BatchCreateTasksResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        delivery_api.BatchCreateTasksResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for batch_create_tasks

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeliveryService server but before it is returned to user code.

        We recommend only using this `post_batch_create_tasks_with_metadata`
        interceptor in new development instead of the `post_batch_create_tasks` interceptor.
        When both interceptors are used, this `post_batch_create_tasks_with_metadata` interceptor runs after the
        `post_batch_create_tasks` interceptor. The (possibly modified) response returned by
        `post_batch_create_tasks` will be passed to
        `post_batch_create_tasks_with_metadata`.
        """
        return response, metadata

    def pre_create_delivery_vehicle(
        self,
        request: delivery_api.CreateDeliveryVehicleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        delivery_api.CreateDeliveryVehicleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_delivery_vehicle

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeliveryService server.
        """
        return request, metadata

    def post_create_delivery_vehicle(
        self, response: delivery_vehicles.DeliveryVehicle
    ) -> delivery_vehicles.DeliveryVehicle:
        """Post-rpc interceptor for create_delivery_vehicle

        DEPRECATED. Please use the `post_create_delivery_vehicle_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeliveryService server but before
        it is returned to user code. This `post_create_delivery_vehicle` interceptor runs
        before the `post_create_delivery_vehicle_with_metadata` interceptor.
        """
        return response

    def post_create_delivery_vehicle_with_metadata(
        self,
        response: delivery_vehicles.DeliveryVehicle,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        delivery_vehicles.DeliveryVehicle, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_delivery_vehicle

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeliveryService server but before it is returned to user code.

        We recommend only using this `post_create_delivery_vehicle_with_metadata`
        interceptor in new development instead of the `post_create_delivery_vehicle` interceptor.
        When both interceptors are used, this `post_create_delivery_vehicle_with_metadata` interceptor runs after the
        `post_create_delivery_vehicle` interceptor. The (possibly modified) response returned by
        `post_create_delivery_vehicle` will be passed to
        `post_create_delivery_vehicle_with_metadata`.
        """
        return response, metadata

    def pre_create_task(
        self,
        request: delivery_api.CreateTaskRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[delivery_api.CreateTaskRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_task

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeliveryService server.
        """
        return request, metadata

    def post_create_task(self, response: tasks.Task) -> tasks.Task:
        """Post-rpc interceptor for create_task

        DEPRECATED. Please use the `post_create_task_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeliveryService server but before
        it is returned to user code. This `post_create_task` interceptor runs
        before the `post_create_task_with_metadata` interceptor.
        """
        return response

    def post_create_task_with_metadata(
        self, response: tasks.Task, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[tasks.Task, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_task

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeliveryService server but before it is returned to user code.

        We recommend only using this `post_create_task_with_metadata`
        interceptor in new development instead of the `post_create_task` interceptor.
        When both interceptors are used, this `post_create_task_with_metadata` interceptor runs after the
        `post_create_task` interceptor. The (possibly modified) response returned by
        `post_create_task` will be passed to
        `post_create_task_with_metadata`.
        """
        return response, metadata

    def pre_delete_delivery_vehicle(
        self,
        request: delivery_api.DeleteDeliveryVehicleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        delivery_api.DeleteDeliveryVehicleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_delivery_vehicle

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeliveryService server.
        """
        return request, metadata

    def pre_delete_task(
        self,
        request: delivery_api.DeleteTaskRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[delivery_api.DeleteTaskRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_task

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeliveryService server.
        """
        return request, metadata

    def pre_get_delivery_vehicle(
        self,
        request: delivery_api.GetDeliveryVehicleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        delivery_api.GetDeliveryVehicleRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_delivery_vehicle

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeliveryService server.
        """
        return request, metadata

    def post_get_delivery_vehicle(
        self, response: delivery_vehicles.DeliveryVehicle
    ) -> delivery_vehicles.DeliveryVehicle:
        """Post-rpc interceptor for get_delivery_vehicle

        DEPRECATED. Please use the `post_get_delivery_vehicle_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeliveryService server but before
        it is returned to user code. This `post_get_delivery_vehicle` interceptor runs
        before the `post_get_delivery_vehicle_with_metadata` interceptor.
        """
        return response

    def post_get_delivery_vehicle_with_metadata(
        self,
        response: delivery_vehicles.DeliveryVehicle,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        delivery_vehicles.DeliveryVehicle, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_delivery_vehicle

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeliveryService server but before it is returned to user code.

        We recommend only using this `post_get_delivery_vehicle_with_metadata`
        interceptor in new development instead of the `post_get_delivery_vehicle` interceptor.
        When both interceptors are used, this `post_get_delivery_vehicle_with_metadata` interceptor runs after the
        `post_get_delivery_vehicle` interceptor. The (possibly modified) response returned by
        `post_get_delivery_vehicle` will be passed to
        `post_get_delivery_vehicle_with_metadata`.
        """
        return response, metadata

    def pre_get_task(
        self,
        request: delivery_api.GetTaskRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[delivery_api.GetTaskRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_task

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeliveryService server.
        """
        return request, metadata

    def post_get_task(self, response: tasks.Task) -> tasks.Task:
        """Post-rpc interceptor for get_task

        DEPRECATED. Please use the `post_get_task_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeliveryService server but before
        it is returned to user code. This `post_get_task` interceptor runs
        before the `post_get_task_with_metadata` interceptor.
        """
        return response

    def post_get_task_with_metadata(
        self, response: tasks.Task, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[tasks.Task, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_task

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeliveryService server but before it is returned to user code.

        We recommend only using this `post_get_task_with_metadata`
        interceptor in new development instead of the `post_get_task` interceptor.
        When both interceptors are used, this `post_get_task_with_metadata` interceptor runs after the
        `post_get_task` interceptor. The (possibly modified) response returned by
        `post_get_task` will be passed to
        `post_get_task_with_metadata`.
        """
        return response, metadata

    def pre_get_task_tracking_info(
        self,
        request: delivery_api.GetTaskTrackingInfoRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        delivery_api.GetTaskTrackingInfoRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_task_tracking_info

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeliveryService server.
        """
        return request, metadata

    def post_get_task_tracking_info(
        self, response: task_tracking_info.TaskTrackingInfo
    ) -> task_tracking_info.TaskTrackingInfo:
        """Post-rpc interceptor for get_task_tracking_info

        DEPRECATED. Please use the `post_get_task_tracking_info_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeliveryService server but before
        it is returned to user code. This `post_get_task_tracking_info` interceptor runs
        before the `post_get_task_tracking_info_with_metadata` interceptor.
        """
        return response

    def post_get_task_tracking_info_with_metadata(
        self,
        response: task_tracking_info.TaskTrackingInfo,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        task_tracking_info.TaskTrackingInfo, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_task_tracking_info

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeliveryService server but before it is returned to user code.

        We recommend only using this `post_get_task_tracking_info_with_metadata`
        interceptor in new development instead of the `post_get_task_tracking_info` interceptor.
        When both interceptors are used, this `post_get_task_tracking_info_with_metadata` interceptor runs after the
        `post_get_task_tracking_info` interceptor. The (possibly modified) response returned by
        `post_get_task_tracking_info` will be passed to
        `post_get_task_tracking_info_with_metadata`.
        """
        return response, metadata

    def pre_list_delivery_vehicles(
        self,
        request: delivery_api.ListDeliveryVehiclesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        delivery_api.ListDeliveryVehiclesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_delivery_vehicles

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeliveryService server.
        """
        return request, metadata

    def post_list_delivery_vehicles(
        self, response: delivery_api.ListDeliveryVehiclesResponse
    ) -> delivery_api.ListDeliveryVehiclesResponse:
        """Post-rpc interceptor for list_delivery_vehicles

        DEPRECATED. Please use the `post_list_delivery_vehicles_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeliveryService server but before
        it is returned to user code. This `post_list_delivery_vehicles` interceptor runs
        before the `post_list_delivery_vehicles_with_metadata` interceptor.
        """
        return response

    def post_list_delivery_vehicles_with_metadata(
        self,
        response: delivery_api.ListDeliveryVehiclesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        delivery_api.ListDeliveryVehiclesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_delivery_vehicles

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeliveryService server but before it is returned to user code.

        We recommend only using this `post_list_delivery_vehicles_with_metadata`
        interceptor in new development instead of the `post_list_delivery_vehicles` interceptor.
        When both interceptors are used, this `post_list_delivery_vehicles_with_metadata` interceptor runs after the
        `post_list_delivery_vehicles` interceptor. The (possibly modified) response returned by
        `post_list_delivery_vehicles` will be passed to
        `post_list_delivery_vehicles_with_metadata`.
        """
        return response, metadata

    def pre_list_tasks(
        self,
        request: delivery_api.ListTasksRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[delivery_api.ListTasksRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_tasks

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeliveryService server.
        """
        return request, metadata

    def post_list_tasks(
        self, response: delivery_api.ListTasksResponse
    ) -> delivery_api.ListTasksResponse:
        """Post-rpc interceptor for list_tasks

        DEPRECATED. Please use the `post_list_tasks_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeliveryService server but before
        it is returned to user code. This `post_list_tasks` interceptor runs
        before the `post_list_tasks_with_metadata` interceptor.
        """
        return response

    def post_list_tasks_with_metadata(
        self,
        response: delivery_api.ListTasksResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[delivery_api.ListTasksResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_tasks

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeliveryService server but before it is returned to user code.

        We recommend only using this `post_list_tasks_with_metadata`
        interceptor in new development instead of the `post_list_tasks` interceptor.
        When both interceptors are used, this `post_list_tasks_with_metadata` interceptor runs after the
        `post_list_tasks` interceptor. The (possibly modified) response returned by
        `post_list_tasks` will be passed to
        `post_list_tasks_with_metadata`.
        """
        return response, metadata

    def pre_update_delivery_vehicle(
        self,
        request: delivery_api.UpdateDeliveryVehicleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        delivery_api.UpdateDeliveryVehicleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_delivery_vehicle

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeliveryService server.
        """
        return request, metadata

    def post_update_delivery_vehicle(
        self, response: delivery_vehicles.DeliveryVehicle
    ) -> delivery_vehicles.DeliveryVehicle:
        """Post-rpc interceptor for update_delivery_vehicle

        DEPRECATED. Please use the `post_update_delivery_vehicle_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeliveryService server but before
        it is returned to user code. This `post_update_delivery_vehicle` interceptor runs
        before the `post_update_delivery_vehicle_with_metadata` interceptor.
        """
        return response

    def post_update_delivery_vehicle_with_metadata(
        self,
        response: delivery_vehicles.DeliveryVehicle,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        delivery_vehicles.DeliveryVehicle, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_delivery_vehicle

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeliveryService server but before it is returned to user code.

        We recommend only using this `post_update_delivery_vehicle_with_metadata`
        interceptor in new development instead of the `post_update_delivery_vehicle` interceptor.
        When both interceptors are used, this `post_update_delivery_vehicle_with_metadata` interceptor runs after the
        `post_update_delivery_vehicle` interceptor. The (possibly modified) response returned by
        `post_update_delivery_vehicle` will be passed to
        `post_update_delivery_vehicle_with_metadata`.
        """
        return response, metadata

    def pre_update_task(
        self,
        request: delivery_api.UpdateTaskRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[delivery_api.UpdateTaskRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_task

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DeliveryService server.
        """
        return request, metadata

    def post_update_task(self, response: tasks.Task) -> tasks.Task:
        """Post-rpc interceptor for update_task

        DEPRECATED. Please use the `post_update_task_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DeliveryService server but before
        it is returned to user code. This `post_update_task` interceptor runs
        before the `post_update_task_with_metadata` interceptor.
        """
        return response

    def post_update_task_with_metadata(
        self, response: tasks.Task, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[tasks.Task, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_task

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DeliveryService server but before it is returned to user code.

        We recommend only using this `post_update_task_with_metadata`
        interceptor in new development instead of the `post_update_task` interceptor.
        When both interceptors are used, this `post_update_task_with_metadata` interceptor runs after the
        `post_update_task` interceptor. The (possibly modified) response returned by
        `post_update_task` will be passed to
        `post_update_task_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class DeliveryServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: DeliveryServiceRestInterceptor


class DeliveryServiceRestTransport(_BaseDeliveryServiceRestTransport):
    """REST backend synchronous transport for DeliveryService.

    The Last Mile Delivery service.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "fleetengine.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[DeliveryServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'fleetengine.googleapis.com').
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
            interceptor (Optional[DeliveryServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or DeliveryServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchCreateTasks(
        _BaseDeliveryServiceRestTransport._BaseBatchCreateTasks, DeliveryServiceRestStub
    ):
        def __hash__(self):
            return hash("DeliveryServiceRestTransport.BatchCreateTasks")

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
            request: delivery_api.BatchCreateTasksRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> delivery_api.BatchCreateTasksResponse:
            r"""Call the batch create tasks method over HTTP.

            Args:
                request (~.delivery_api.BatchCreateTasksRequest):
                    The request object. The ``BatchCreateTask`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.delivery_api.BatchCreateTasksResponse:
                    The ``BatchCreateTask`` response message.
            """

            http_options = _BaseDeliveryServiceRestTransport._BaseBatchCreateTasks._get_http_options()
            request, metadata = self._interceptor.pre_batch_create_tasks(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeliveryServiceRestTransport._BaseBatchCreateTasks,
                    "_BaseBatchCreateTasks__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for maps.fleetengine.delivery_v1.DeliveryServiceClient.BatchCreateTasks",
                    extra={
                        "serviceName": "maps.fleetengine.delivery.v1.DeliveryService",
                        "rpcName": "BatchCreateTasks",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeliveryServiceRestTransport._BatchCreateTasks._get_response(
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
            resp = delivery_api.BatchCreateTasksResponse()
            pb_resp = delivery_api.BatchCreateTasksResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_tasks(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_create_tasks_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = delivery_api.BatchCreateTasksResponse.to_json(
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
                    "Received response for maps.fleetengine.delivery_v1.DeliveryServiceClient.batch_create_tasks",
                    extra={
                        "serviceName": "maps.fleetengine.delivery.v1.DeliveryService",
                        "rpcName": "BatchCreateTasks",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateDeliveryVehicle(
        _BaseDeliveryServiceRestTransport._BaseCreateDeliveryVehicle,
        DeliveryServiceRestStub,
    ):
        def __hash__(self):
            return hash("DeliveryServiceRestTransport.CreateDeliveryVehicle")

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
            request: delivery_api.CreateDeliveryVehicleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> delivery_vehicles.DeliveryVehicle:
            r"""Call the create delivery vehicle method over HTTP.

            Args:
                request (~.delivery_api.CreateDeliveryVehicleRequest):
                    The request object. The ``CreateDeliveryVehicle`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.delivery_vehicles.DeliveryVehicle:
                    The ``DeliveryVehicle`` message. A delivery vehicle
                transports shipments from a depot to a delivery
                location, and from a pickup location to the depot. In
                some cases, delivery vehicles also transport shipments
                directly from the pickup location to the delivery
                location.

                Note: gRPC and REST APIs use different field naming
                conventions. For example, the
                ``DeliveryVehicle.current_route_segment`` field in the
                gRPC API and the ``DeliveryVehicle.currentRouteSegment``
                field in the REST API refer to the same field.

            """

            http_options = _BaseDeliveryServiceRestTransport._BaseCreateDeliveryVehicle._get_http_options()
            request, metadata = self._interceptor.pre_create_delivery_vehicle(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeliveryServiceRestTransport._BaseCreateDeliveryVehicle,
                    "_BaseCreateDeliveryVehicle__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for maps.fleetengine.delivery_v1.DeliveryServiceClient.CreateDeliveryVehicle",
                    extra={
                        "serviceName": "maps.fleetengine.delivery.v1.DeliveryService",
                        "rpcName": "CreateDeliveryVehicle",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DeliveryServiceRestTransport._CreateDeliveryVehicle._get_response(
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
            resp = delivery_vehicles.DeliveryVehicle()
            pb_resp = delivery_vehicles.DeliveryVehicle.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_delivery_vehicle(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_delivery_vehicle_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = delivery_vehicles.DeliveryVehicle.to_json(
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
                    "Received response for maps.fleetengine.delivery_v1.DeliveryServiceClient.create_delivery_vehicle",
                    extra={
                        "serviceName": "maps.fleetengine.delivery.v1.DeliveryService",
                        "rpcName": "CreateDeliveryVehicle",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateTask(
        _BaseDeliveryServiceRestTransport._BaseCreateTask, DeliveryServiceRestStub
    ):
        def __hash__(self):
            return hash("DeliveryServiceRestTransport.CreateTask")

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
            request: delivery_api.CreateTaskRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> tasks.Task:
            r"""Call the create task method over HTTP.

            Args:
                request (~.delivery_api.CreateTaskRequest):
                    The request object. The ``CreateTask`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.tasks.Task:
                    A Task in the Delivery API represents a single action to
                track. In general, there is a distinction between
                shipment-related Tasks and break Tasks. A shipment can
                have multiple Tasks associated with it. For example,
                there could be one Task for the pickup, and one for the
                drop-off or transfer. Also, different Tasks for a given
                shipment can be handled by different vehicles. For
                example, one vehicle could handle the pickup, driving
                the shipment to the hub, while another vehicle drives
                the same shipment from the hub to the drop-off location.

                Note: gRPC and REST APIs use different field naming
                conventions. For example, the
                ``Task.journey_sharing_info`` field in the gRPC API and
                the ``Task.journeySharingInfo`` field in the REST API
                refer to the same field.

            """

            http_options = (
                _BaseDeliveryServiceRestTransport._BaseCreateTask._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_task(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeliveryServiceRestTransport._BaseCreateTask,
                    "_BaseCreateTask__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for maps.fleetengine.delivery_v1.DeliveryServiceClient.CreateTask",
                    extra={
                        "serviceName": "maps.fleetengine.delivery.v1.DeliveryService",
                        "rpcName": "CreateTask",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeliveryServiceRestTransport._CreateTask._get_response(
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
            resp = tasks.Task()
            pb_resp = tasks.Task.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_task(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_task_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = tasks.Task.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for maps.fleetengine.delivery_v1.DeliveryServiceClient.create_task",
                    extra={
                        "serviceName": "maps.fleetengine.delivery.v1.DeliveryService",
                        "rpcName": "CreateTask",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteDeliveryVehicle(
        _BaseDeliveryServiceRestTransport._BaseDeleteDeliveryVehicle,
        DeliveryServiceRestStub,
    ):
        def __hash__(self):
            return hash("DeliveryServiceRestTransport.DeleteDeliveryVehicle")

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
            request: delivery_api.DeleteDeliveryVehicleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete delivery vehicle method over HTTP.

            Args:
                request (~.delivery_api.DeleteDeliveryVehicleRequest):
                    The request object. DeleteDeliveryVehicle request
                message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseDeliveryServiceRestTransport._BaseDeleteDeliveryVehicle._get_http_options()
            request, metadata = self._interceptor.pre_delete_delivery_vehicle(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeliveryServiceRestTransport._BaseDeleteDeliveryVehicle,
                    "_BaseDeleteDeliveryVehicle__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for maps.fleetengine.delivery_v1.DeliveryServiceClient.DeleteDeliveryVehicle",
                    extra={
                        "serviceName": "maps.fleetengine.delivery.v1.DeliveryService",
                        "rpcName": "DeleteDeliveryVehicle",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DeliveryServiceRestTransport._DeleteDeliveryVehicle._get_response(
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

    class _DeleteTask(
        _BaseDeliveryServiceRestTransport._BaseDeleteTask, DeliveryServiceRestStub
    ):
        def __hash__(self):
            return hash("DeliveryServiceRestTransport.DeleteTask")

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
            request: delivery_api.DeleteTaskRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete task method over HTTP.

            Args:
                request (~.delivery_api.DeleteTaskRequest):
                    The request object. DeleteTask request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseDeliveryServiceRestTransport._BaseDeleteTask._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_task(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeliveryServiceRestTransport._BaseDeleteTask,
                    "_BaseDeleteTask__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for maps.fleetengine.delivery_v1.DeliveryServiceClient.DeleteTask",
                    extra={
                        "serviceName": "maps.fleetengine.delivery.v1.DeliveryService",
                        "rpcName": "DeleteTask",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeliveryServiceRestTransport._DeleteTask._get_response(
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

    class _GetDeliveryVehicle(
        _BaseDeliveryServiceRestTransport._BaseGetDeliveryVehicle,
        DeliveryServiceRestStub,
    ):
        def __hash__(self):
            return hash("DeliveryServiceRestTransport.GetDeliveryVehicle")

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
            request: delivery_api.GetDeliveryVehicleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> delivery_vehicles.DeliveryVehicle:
            r"""Call the get delivery vehicle method over HTTP.

            Args:
                request (~.delivery_api.GetDeliveryVehicleRequest):
                    The request object. The ``GetDeliveryVehicle`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.delivery_vehicles.DeliveryVehicle:
                    The ``DeliveryVehicle`` message. A delivery vehicle
                transports shipments from a depot to a delivery
                location, and from a pickup location to the depot. In
                some cases, delivery vehicles also transport shipments
                directly from the pickup location to the delivery
                location.

                Note: gRPC and REST APIs use different field naming
                conventions. For example, the
                ``DeliveryVehicle.current_route_segment`` field in the
                gRPC API and the ``DeliveryVehicle.currentRouteSegment``
                field in the REST API refer to the same field.

            """

            http_options = _BaseDeliveryServiceRestTransport._BaseGetDeliveryVehicle._get_http_options()
            request, metadata = self._interceptor.pre_get_delivery_vehicle(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeliveryServiceRestTransport._BaseGetDeliveryVehicle,
                    "_BaseGetDeliveryVehicle__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for maps.fleetengine.delivery_v1.DeliveryServiceClient.GetDeliveryVehicle",
                    extra={
                        "serviceName": "maps.fleetengine.delivery.v1.DeliveryService",
                        "rpcName": "GetDeliveryVehicle",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeliveryServiceRestTransport._GetDeliveryVehicle._get_response(
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
            resp = delivery_vehicles.DeliveryVehicle()
            pb_resp = delivery_vehicles.DeliveryVehicle.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_delivery_vehicle(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_delivery_vehicle_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = delivery_vehicles.DeliveryVehicle.to_json(
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
                    "Received response for maps.fleetengine.delivery_v1.DeliveryServiceClient.get_delivery_vehicle",
                    extra={
                        "serviceName": "maps.fleetengine.delivery.v1.DeliveryService",
                        "rpcName": "GetDeliveryVehicle",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetTask(
        _BaseDeliveryServiceRestTransport._BaseGetTask, DeliveryServiceRestStub
    ):
        def __hash__(self):
            return hash("DeliveryServiceRestTransport.GetTask")

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
            request: delivery_api.GetTaskRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> tasks.Task:
            r"""Call the get task method over HTTP.

            Args:
                request (~.delivery_api.GetTaskRequest):
                    The request object. The ``GetTask`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.tasks.Task:
                    A Task in the Delivery API represents a single action to
                track. In general, there is a distinction between
                shipment-related Tasks and break Tasks. A shipment can
                have multiple Tasks associated with it. For example,
                there could be one Task for the pickup, and one for the
                drop-off or transfer. Also, different Tasks for a given
                shipment can be handled by different vehicles. For
                example, one vehicle could handle the pickup, driving
                the shipment to the hub, while another vehicle drives
                the same shipment from the hub to the drop-off location.

                Note: gRPC and REST APIs use different field naming
                conventions. For example, the
                ``Task.journey_sharing_info`` field in the gRPC API and
                the ``Task.journeySharingInfo`` field in the REST API
                refer to the same field.

            """

            http_options = (
                _BaseDeliveryServiceRestTransport._BaseGetTask._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_task(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeliveryServiceRestTransport._BaseGetTask,
                    "_BaseGetTask__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for maps.fleetengine.delivery_v1.DeliveryServiceClient.GetTask",
                    extra={
                        "serviceName": "maps.fleetengine.delivery.v1.DeliveryService",
                        "rpcName": "GetTask",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeliveryServiceRestTransport._GetTask._get_response(
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
            resp = tasks.Task()
            pb_resp = tasks.Task.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_task(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_task_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = tasks.Task.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for maps.fleetengine.delivery_v1.DeliveryServiceClient.get_task",
                    extra={
                        "serviceName": "maps.fleetengine.delivery.v1.DeliveryService",
                        "rpcName": "GetTask",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetTaskTrackingInfo(
        _BaseDeliveryServiceRestTransport._BaseGetTaskTrackingInfo,
        DeliveryServiceRestStub,
    ):
        def __hash__(self):
            return hash("DeliveryServiceRestTransport.GetTaskTrackingInfo")

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
            request: delivery_api.GetTaskTrackingInfoRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> task_tracking_info.TaskTrackingInfo:
            r"""Call the get task tracking info method over HTTP.

            Args:
                request (~.delivery_api.GetTaskTrackingInfoRequest):
                    The request object. The ``GetTaskTrackingInfoRequest`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.task_tracking_info.TaskTrackingInfo:
                    The ``TaskTrackingInfo`` message. The message contains
                task tracking information which will be used for
                display. If a tracking ID is associated with multiple
                Tasks, Fleet Engine uses a heuristic to decide which
                Task's TaskTrackingInfo to select.

            """

            http_options = _BaseDeliveryServiceRestTransport._BaseGetTaskTrackingInfo._get_http_options()
            request, metadata = self._interceptor.pre_get_task_tracking_info(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeliveryServiceRestTransport._BaseGetTaskTrackingInfo,
                    "_BaseGetTaskTrackingInfo__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for maps.fleetengine.delivery_v1.DeliveryServiceClient.GetTaskTrackingInfo",
                    extra={
                        "serviceName": "maps.fleetengine.delivery.v1.DeliveryService",
                        "rpcName": "GetTaskTrackingInfo",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeliveryServiceRestTransport._GetTaskTrackingInfo._get_response(
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
            resp = task_tracking_info.TaskTrackingInfo()
            pb_resp = task_tracking_info.TaskTrackingInfo.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_task_tracking_info(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_task_tracking_info_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = task_tracking_info.TaskTrackingInfo.to_json(
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
                    "Received response for maps.fleetengine.delivery_v1.DeliveryServiceClient.get_task_tracking_info",
                    extra={
                        "serviceName": "maps.fleetengine.delivery.v1.DeliveryService",
                        "rpcName": "GetTaskTrackingInfo",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDeliveryVehicles(
        _BaseDeliveryServiceRestTransport._BaseListDeliveryVehicles,
        DeliveryServiceRestStub,
    ):
        def __hash__(self):
            return hash("DeliveryServiceRestTransport.ListDeliveryVehicles")

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
            request: delivery_api.ListDeliveryVehiclesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> delivery_api.ListDeliveryVehiclesResponse:
            r"""Call the list delivery vehicles method over HTTP.

            Args:
                request (~.delivery_api.ListDeliveryVehiclesRequest):
                    The request object. The ``ListDeliveryVehicles`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.delivery_api.ListDeliveryVehiclesResponse:
                    The ``ListDeliveryVehicles`` response message.
            """

            http_options = _BaseDeliveryServiceRestTransport._BaseListDeliveryVehicles._get_http_options()
            request, metadata = self._interceptor.pre_list_delivery_vehicles(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeliveryServiceRestTransport._BaseListDeliveryVehicles,
                    "_BaseListDeliveryVehicles__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for maps.fleetengine.delivery_v1.DeliveryServiceClient.ListDeliveryVehicles",
                    extra={
                        "serviceName": "maps.fleetengine.delivery.v1.DeliveryService",
                        "rpcName": "ListDeliveryVehicles",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeliveryServiceRestTransport._ListDeliveryVehicles._get_response(
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
            resp = delivery_api.ListDeliveryVehiclesResponse()
            pb_resp = delivery_api.ListDeliveryVehiclesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_delivery_vehicles(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_delivery_vehicles_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        delivery_api.ListDeliveryVehiclesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for maps.fleetengine.delivery_v1.DeliveryServiceClient.list_delivery_vehicles",
                    extra={
                        "serviceName": "maps.fleetengine.delivery.v1.DeliveryService",
                        "rpcName": "ListDeliveryVehicles",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListTasks(
        _BaseDeliveryServiceRestTransport._BaseListTasks, DeliveryServiceRestStub
    ):
        def __hash__(self):
            return hash("DeliveryServiceRestTransport.ListTasks")

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
            request: delivery_api.ListTasksRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> delivery_api.ListTasksResponse:
            r"""Call the list tasks method over HTTP.

            Args:
                request (~.delivery_api.ListTasksRequest):
                    The request object. The ``ListTasks`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.delivery_api.ListTasksResponse:
                    The ``ListTasks`` response that contains the set of
                Tasks that meet the filter criteria in the
                ``ListTasksRequest``.

            """

            http_options = (
                _BaseDeliveryServiceRestTransport._BaseListTasks._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_tasks(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeliveryServiceRestTransport._BaseListTasks,
                    "_BaseListTasks__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for maps.fleetengine.delivery_v1.DeliveryServiceClient.ListTasks",
                    extra={
                        "serviceName": "maps.fleetengine.delivery.v1.DeliveryService",
                        "rpcName": "ListTasks",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeliveryServiceRestTransport._ListTasks._get_response(
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
            resp = delivery_api.ListTasksResponse()
            pb_resp = delivery_api.ListTasksResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_tasks(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_tasks_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = delivery_api.ListTasksResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for maps.fleetengine.delivery_v1.DeliveryServiceClient.list_tasks",
                    extra={
                        "serviceName": "maps.fleetengine.delivery.v1.DeliveryService",
                        "rpcName": "ListTasks",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDeliveryVehicle(
        _BaseDeliveryServiceRestTransport._BaseUpdateDeliveryVehicle,
        DeliveryServiceRestStub,
    ):
        def __hash__(self):
            return hash("DeliveryServiceRestTransport.UpdateDeliveryVehicle")

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
            request: delivery_api.UpdateDeliveryVehicleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> delivery_vehicles.DeliveryVehicle:
            r"""Call the update delivery vehicle method over HTTP.

            Args:
                request (~.delivery_api.UpdateDeliveryVehicleRequest):
                    The request object. The ``UpdateDeliveryVehicle`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.delivery_vehicles.DeliveryVehicle:
                    The ``DeliveryVehicle`` message. A delivery vehicle
                transports shipments from a depot to a delivery
                location, and from a pickup location to the depot. In
                some cases, delivery vehicles also transport shipments
                directly from the pickup location to the delivery
                location.

                Note: gRPC and REST APIs use different field naming
                conventions. For example, the
                ``DeliveryVehicle.current_route_segment`` field in the
                gRPC API and the ``DeliveryVehicle.currentRouteSegment``
                field in the REST API refer to the same field.

            """

            http_options = _BaseDeliveryServiceRestTransport._BaseUpdateDeliveryVehicle._get_http_options()
            request, metadata = self._interceptor.pre_update_delivery_vehicle(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeliveryServiceRestTransport._BaseUpdateDeliveryVehicle,
                    "_BaseUpdateDeliveryVehicle__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for maps.fleetengine.delivery_v1.DeliveryServiceClient.UpdateDeliveryVehicle",
                    extra={
                        "serviceName": "maps.fleetengine.delivery.v1.DeliveryService",
                        "rpcName": "UpdateDeliveryVehicle",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DeliveryServiceRestTransport._UpdateDeliveryVehicle._get_response(
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
            resp = delivery_vehicles.DeliveryVehicle()
            pb_resp = delivery_vehicles.DeliveryVehicle.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_delivery_vehicle(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_delivery_vehicle_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = delivery_vehicles.DeliveryVehicle.to_json(
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
                    "Received response for maps.fleetengine.delivery_v1.DeliveryServiceClient.update_delivery_vehicle",
                    extra={
                        "serviceName": "maps.fleetengine.delivery.v1.DeliveryService",
                        "rpcName": "UpdateDeliveryVehicle",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateTask(
        _BaseDeliveryServiceRestTransport._BaseUpdateTask, DeliveryServiceRestStub
    ):
        def __hash__(self):
            return hash("DeliveryServiceRestTransport.UpdateTask")

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
            request: delivery_api.UpdateTaskRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> tasks.Task:
            r"""Call the update task method over HTTP.

            Args:
                request (~.delivery_api.UpdateTaskRequest):
                    The request object. The ``UpdateTask`` request message.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.tasks.Task:
                    A Task in the Delivery API represents a single action to
                track. In general, there is a distinction between
                shipment-related Tasks and break Tasks. A shipment can
                have multiple Tasks associated with it. For example,
                there could be one Task for the pickup, and one for the
                drop-off or transfer. Also, different Tasks for a given
                shipment can be handled by different vehicles. For
                example, one vehicle could handle the pickup, driving
                the shipment to the hub, while another vehicle drives
                the same shipment from the hub to the drop-off location.

                Note: gRPC and REST APIs use different field naming
                conventions. For example, the
                ``Task.journey_sharing_info`` field in the gRPC API and
                the ``Task.journeySharingInfo`` field in the REST API
                refer to the same field.

            """

            http_options = (
                _BaseDeliveryServiceRestTransport._BaseUpdateTask._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_task(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDeliveryServiceRestTransport._BaseUpdateTask,
                    "_BaseUpdateTask__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for maps.fleetengine.delivery_v1.DeliveryServiceClient.UpdateTask",
                    extra={
                        "serviceName": "maps.fleetengine.delivery.v1.DeliveryService",
                        "rpcName": "UpdateTask",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DeliveryServiceRestTransport._UpdateTask._get_response(
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
            resp = tasks.Task()
            pb_resp = tasks.Task.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_task(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_task_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = tasks.Task.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for maps.fleetengine.delivery_v1.DeliveryServiceClient.update_task",
                    extra={
                        "serviceName": "maps.fleetengine.delivery.v1.DeliveryService",
                        "rpcName": "UpdateTask",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_create_tasks(
        self,
    ) -> Callable[
        [delivery_api.BatchCreateTasksRequest], delivery_api.BatchCreateTasksResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateTasks(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_delivery_vehicle(
        self,
    ) -> Callable[
        [delivery_api.CreateDeliveryVehicleRequest], delivery_vehicles.DeliveryVehicle
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDeliveryVehicle(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_task(self) -> Callable[[delivery_api.CreateTaskRequest], tasks.Task]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateTask(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_delivery_vehicle(
        self,
    ) -> Callable[[delivery_api.DeleteDeliveryVehicleRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDeliveryVehicle(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_task(
        self,
    ) -> Callable[[delivery_api.DeleteTaskRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteTask(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_delivery_vehicle(
        self,
    ) -> Callable[
        [delivery_api.GetDeliveryVehicleRequest], delivery_vehicles.DeliveryVehicle
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDeliveryVehicle(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_task(self) -> Callable[[delivery_api.GetTaskRequest], tasks.Task]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTask(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_task_tracking_info(
        self,
    ) -> Callable[
        [delivery_api.GetTaskTrackingInfoRequest], task_tracking_info.TaskTrackingInfo
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTaskTrackingInfo(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_delivery_vehicles(
        self,
    ) -> Callable[
        [delivery_api.ListDeliveryVehiclesRequest],
        delivery_api.ListDeliveryVehiclesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDeliveryVehicles(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_tasks(
        self,
    ) -> Callable[[delivery_api.ListTasksRequest], delivery_api.ListTasksResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTasks(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_delivery_vehicle(
        self,
    ) -> Callable[
        [delivery_api.UpdateDeliveryVehicleRequest], delivery_vehicles.DeliveryVehicle
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDeliveryVehicle(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_task(self) -> Callable[[delivery_api.UpdateTaskRequest], tasks.Task]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateTask(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("DeliveryServiceRestTransport",)
