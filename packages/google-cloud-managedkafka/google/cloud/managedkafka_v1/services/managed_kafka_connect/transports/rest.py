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
from google.api_core import gapic_v1, operations_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.managedkafka_v1._compat import transcode_request
from google.cloud.managedkafka_v1.types import managed_kafka_connect, resources

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseManagedKafkaConnectRestTransport

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


class ManagedKafkaConnectRestInterceptor:
    """Interceptor for ManagedKafkaConnect.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ManagedKafkaConnectRestTransport.

    .. code-block:: python
        class MyCustomManagedKafkaConnectInterceptor(ManagedKafkaConnectRestInterceptor):
            def pre_create_connect_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_connect_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_connector(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_connector(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_connect_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_connect_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_connector(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_connect_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_connect_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_connector(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_connector(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_connect_clusters(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_connect_clusters(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_connectors(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_connectors(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_pause_connector(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_pause_connector(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_restart_connector(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_restart_connector(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_resume_connector(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_resume_connector(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_stop_connector(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_stop_connector(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_connect_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_connect_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_connector(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_connector(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ManagedKafkaConnectRestTransport(interceptor=MyCustomManagedKafkaConnectInterceptor())
        client = ManagedKafkaConnectClient(transport=transport)


    """

    def pre_create_connect_cluster(
        self,
        request: managed_kafka_connect.CreateConnectClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        managed_kafka_connect.CreateConnectClusterRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_connect_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedKafkaConnect server.
        """
        return request, metadata

    def post_create_connect_cluster(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_connect_cluster

        DEPRECATED. Please use the `post_create_connect_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedKafkaConnect server but before
        it is returned to user code. This `post_create_connect_cluster` interceptor runs
        before the `post_create_connect_cluster_with_metadata` interceptor.
        """
        return response

    def post_create_connect_cluster_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_connect_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedKafkaConnect server but before it is returned to user code.

        We recommend only using this `post_create_connect_cluster_with_metadata`
        interceptor in new development instead of the `post_create_connect_cluster` interceptor.
        When both interceptors are used, this `post_create_connect_cluster_with_metadata` interceptor runs after the
        `post_create_connect_cluster` interceptor. The (possibly modified) response returned by
        `post_create_connect_cluster` will be passed to
        `post_create_connect_cluster_with_metadata`.
        """
        return response, metadata

    def pre_create_connector(
        self,
        request: managed_kafka_connect.CreateConnectorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        managed_kafka_connect.CreateConnectorRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_connector

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedKafkaConnect server.
        """
        return request, metadata

    def post_create_connector(
        self, response: resources.Connector
    ) -> resources.Connector:
        """Post-rpc interceptor for create_connector

        DEPRECATED. Please use the `post_create_connector_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedKafkaConnect server but before
        it is returned to user code. This `post_create_connector` interceptor runs
        before the `post_create_connector_with_metadata` interceptor.
        """
        return response

    def post_create_connector_with_metadata(
        self,
        response: resources.Connector,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Connector, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_connector

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedKafkaConnect server but before it is returned to user code.

        We recommend only using this `post_create_connector_with_metadata`
        interceptor in new development instead of the `post_create_connector` interceptor.
        When both interceptors are used, this `post_create_connector_with_metadata` interceptor runs after the
        `post_create_connector` interceptor. The (possibly modified) response returned by
        `post_create_connector` will be passed to
        `post_create_connector_with_metadata`.
        """
        return response, metadata

    def pre_delete_connect_cluster(
        self,
        request: managed_kafka_connect.DeleteConnectClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        managed_kafka_connect.DeleteConnectClusterRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_connect_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedKafkaConnect server.
        """
        return request, metadata

    def post_delete_connect_cluster(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_connect_cluster

        DEPRECATED. Please use the `post_delete_connect_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedKafkaConnect server but before
        it is returned to user code. This `post_delete_connect_cluster` interceptor runs
        before the `post_delete_connect_cluster_with_metadata` interceptor.
        """
        return response

    def post_delete_connect_cluster_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_connect_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedKafkaConnect server but before it is returned to user code.

        We recommend only using this `post_delete_connect_cluster_with_metadata`
        interceptor in new development instead of the `post_delete_connect_cluster` interceptor.
        When both interceptors are used, this `post_delete_connect_cluster_with_metadata` interceptor runs after the
        `post_delete_connect_cluster` interceptor. The (possibly modified) response returned by
        `post_delete_connect_cluster` will be passed to
        `post_delete_connect_cluster_with_metadata`.
        """
        return response, metadata

    def pre_delete_connector(
        self,
        request: managed_kafka_connect.DeleteConnectorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        managed_kafka_connect.DeleteConnectorRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_connector

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedKafkaConnect server.
        """
        return request, metadata

    def pre_get_connect_cluster(
        self,
        request: managed_kafka_connect.GetConnectClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        managed_kafka_connect.GetConnectClusterRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_connect_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedKafkaConnect server.
        """
        return request, metadata

    def post_get_connect_cluster(
        self, response: resources.ConnectCluster
    ) -> resources.ConnectCluster:
        """Post-rpc interceptor for get_connect_cluster

        DEPRECATED. Please use the `post_get_connect_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedKafkaConnect server but before
        it is returned to user code. This `post_get_connect_cluster` interceptor runs
        before the `post_get_connect_cluster_with_metadata` interceptor.
        """
        return response

    def post_get_connect_cluster_with_metadata(
        self,
        response: resources.ConnectCluster,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.ConnectCluster, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_connect_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedKafkaConnect server but before it is returned to user code.

        We recommend only using this `post_get_connect_cluster_with_metadata`
        interceptor in new development instead of the `post_get_connect_cluster` interceptor.
        When both interceptors are used, this `post_get_connect_cluster_with_metadata` interceptor runs after the
        `post_get_connect_cluster` interceptor. The (possibly modified) response returned by
        `post_get_connect_cluster` will be passed to
        `post_get_connect_cluster_with_metadata`.
        """
        return response, metadata

    def pre_get_connector(
        self,
        request: managed_kafka_connect.GetConnectorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        managed_kafka_connect.GetConnectorRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_connector

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedKafkaConnect server.
        """
        return request, metadata

    def post_get_connector(self, response: resources.Connector) -> resources.Connector:
        """Post-rpc interceptor for get_connector

        DEPRECATED. Please use the `post_get_connector_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedKafkaConnect server but before
        it is returned to user code. This `post_get_connector` interceptor runs
        before the `post_get_connector_with_metadata` interceptor.
        """
        return response

    def post_get_connector_with_metadata(
        self,
        response: resources.Connector,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Connector, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_connector

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedKafkaConnect server but before it is returned to user code.

        We recommend only using this `post_get_connector_with_metadata`
        interceptor in new development instead of the `post_get_connector` interceptor.
        When both interceptors are used, this `post_get_connector_with_metadata` interceptor runs after the
        `post_get_connector` interceptor. The (possibly modified) response returned by
        `post_get_connector` will be passed to
        `post_get_connector_with_metadata`.
        """
        return response, metadata

    def pre_list_connect_clusters(
        self,
        request: managed_kafka_connect.ListConnectClustersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        managed_kafka_connect.ListConnectClustersRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_connect_clusters

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedKafkaConnect server.
        """
        return request, metadata

    def post_list_connect_clusters(
        self, response: managed_kafka_connect.ListConnectClustersResponse
    ) -> managed_kafka_connect.ListConnectClustersResponse:
        """Post-rpc interceptor for list_connect_clusters

        DEPRECATED. Please use the `post_list_connect_clusters_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedKafkaConnect server but before
        it is returned to user code. This `post_list_connect_clusters` interceptor runs
        before the `post_list_connect_clusters_with_metadata` interceptor.
        """
        return response

    def post_list_connect_clusters_with_metadata(
        self,
        response: managed_kafka_connect.ListConnectClustersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        managed_kafka_connect.ListConnectClustersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_connect_clusters

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedKafkaConnect server but before it is returned to user code.

        We recommend only using this `post_list_connect_clusters_with_metadata`
        interceptor in new development instead of the `post_list_connect_clusters` interceptor.
        When both interceptors are used, this `post_list_connect_clusters_with_metadata` interceptor runs after the
        `post_list_connect_clusters` interceptor. The (possibly modified) response returned by
        `post_list_connect_clusters` will be passed to
        `post_list_connect_clusters_with_metadata`.
        """
        return response, metadata

    def pre_list_connectors(
        self,
        request: managed_kafka_connect.ListConnectorsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        managed_kafka_connect.ListConnectorsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_connectors

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedKafkaConnect server.
        """
        return request, metadata

    def post_list_connectors(
        self, response: managed_kafka_connect.ListConnectorsResponse
    ) -> managed_kafka_connect.ListConnectorsResponse:
        """Post-rpc interceptor for list_connectors

        DEPRECATED. Please use the `post_list_connectors_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedKafkaConnect server but before
        it is returned to user code. This `post_list_connectors` interceptor runs
        before the `post_list_connectors_with_metadata` interceptor.
        """
        return response

    def post_list_connectors_with_metadata(
        self,
        response: managed_kafka_connect.ListConnectorsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        managed_kafka_connect.ListConnectorsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_connectors

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedKafkaConnect server but before it is returned to user code.

        We recommend only using this `post_list_connectors_with_metadata`
        interceptor in new development instead of the `post_list_connectors` interceptor.
        When both interceptors are used, this `post_list_connectors_with_metadata` interceptor runs after the
        `post_list_connectors` interceptor. The (possibly modified) response returned by
        `post_list_connectors` will be passed to
        `post_list_connectors_with_metadata`.
        """
        return response, metadata

    def pre_pause_connector(
        self,
        request: managed_kafka_connect.PauseConnectorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        managed_kafka_connect.PauseConnectorRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for pause_connector

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedKafkaConnect server.
        """
        return request, metadata

    def post_pause_connector(
        self, response: managed_kafka_connect.PauseConnectorResponse
    ) -> managed_kafka_connect.PauseConnectorResponse:
        """Post-rpc interceptor for pause_connector

        DEPRECATED. Please use the `post_pause_connector_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedKafkaConnect server but before
        it is returned to user code. This `post_pause_connector` interceptor runs
        before the `post_pause_connector_with_metadata` interceptor.
        """
        return response

    def post_pause_connector_with_metadata(
        self,
        response: managed_kafka_connect.PauseConnectorResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        managed_kafka_connect.PauseConnectorResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for pause_connector

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedKafkaConnect server but before it is returned to user code.

        We recommend only using this `post_pause_connector_with_metadata`
        interceptor in new development instead of the `post_pause_connector` interceptor.
        When both interceptors are used, this `post_pause_connector_with_metadata` interceptor runs after the
        `post_pause_connector` interceptor. The (possibly modified) response returned by
        `post_pause_connector` will be passed to
        `post_pause_connector_with_metadata`.
        """
        return response, metadata

    def pre_restart_connector(
        self,
        request: managed_kafka_connect.RestartConnectorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        managed_kafka_connect.RestartConnectorRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for restart_connector

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedKafkaConnect server.
        """
        return request, metadata

    def post_restart_connector(
        self, response: managed_kafka_connect.RestartConnectorResponse
    ) -> managed_kafka_connect.RestartConnectorResponse:
        """Post-rpc interceptor for restart_connector

        DEPRECATED. Please use the `post_restart_connector_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedKafkaConnect server but before
        it is returned to user code. This `post_restart_connector` interceptor runs
        before the `post_restart_connector_with_metadata` interceptor.
        """
        return response

    def post_restart_connector_with_metadata(
        self,
        response: managed_kafka_connect.RestartConnectorResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        managed_kafka_connect.RestartConnectorResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for restart_connector

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedKafkaConnect server but before it is returned to user code.

        We recommend only using this `post_restart_connector_with_metadata`
        interceptor in new development instead of the `post_restart_connector` interceptor.
        When both interceptors are used, this `post_restart_connector_with_metadata` interceptor runs after the
        `post_restart_connector` interceptor. The (possibly modified) response returned by
        `post_restart_connector` will be passed to
        `post_restart_connector_with_metadata`.
        """
        return response, metadata

    def pre_resume_connector(
        self,
        request: managed_kafka_connect.ResumeConnectorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        managed_kafka_connect.ResumeConnectorRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for resume_connector

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedKafkaConnect server.
        """
        return request, metadata

    def post_resume_connector(
        self, response: managed_kafka_connect.ResumeConnectorResponse
    ) -> managed_kafka_connect.ResumeConnectorResponse:
        """Post-rpc interceptor for resume_connector

        DEPRECATED. Please use the `post_resume_connector_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedKafkaConnect server but before
        it is returned to user code. This `post_resume_connector` interceptor runs
        before the `post_resume_connector_with_metadata` interceptor.
        """
        return response

    def post_resume_connector_with_metadata(
        self,
        response: managed_kafka_connect.ResumeConnectorResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        managed_kafka_connect.ResumeConnectorResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for resume_connector

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedKafkaConnect server but before it is returned to user code.

        We recommend only using this `post_resume_connector_with_metadata`
        interceptor in new development instead of the `post_resume_connector` interceptor.
        When both interceptors are used, this `post_resume_connector_with_metadata` interceptor runs after the
        `post_resume_connector` interceptor. The (possibly modified) response returned by
        `post_resume_connector` will be passed to
        `post_resume_connector_with_metadata`.
        """
        return response, metadata

    def pre_stop_connector(
        self,
        request: managed_kafka_connect.StopConnectorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        managed_kafka_connect.StopConnectorRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for stop_connector

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedKafkaConnect server.
        """
        return request, metadata

    def post_stop_connector(
        self, response: managed_kafka_connect.StopConnectorResponse
    ) -> managed_kafka_connect.StopConnectorResponse:
        """Post-rpc interceptor for stop_connector

        DEPRECATED. Please use the `post_stop_connector_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedKafkaConnect server but before
        it is returned to user code. This `post_stop_connector` interceptor runs
        before the `post_stop_connector_with_metadata` interceptor.
        """
        return response

    def post_stop_connector_with_metadata(
        self,
        response: managed_kafka_connect.StopConnectorResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        managed_kafka_connect.StopConnectorResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for stop_connector

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedKafkaConnect server but before it is returned to user code.

        We recommend only using this `post_stop_connector_with_metadata`
        interceptor in new development instead of the `post_stop_connector` interceptor.
        When both interceptors are used, this `post_stop_connector_with_metadata` interceptor runs after the
        `post_stop_connector` interceptor. The (possibly modified) response returned by
        `post_stop_connector` will be passed to
        `post_stop_connector_with_metadata`.
        """
        return response, metadata

    def pre_update_connect_cluster(
        self,
        request: managed_kafka_connect.UpdateConnectClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        managed_kafka_connect.UpdateConnectClusterRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_connect_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedKafkaConnect server.
        """
        return request, metadata

    def post_update_connect_cluster(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_connect_cluster

        DEPRECATED. Please use the `post_update_connect_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedKafkaConnect server but before
        it is returned to user code. This `post_update_connect_cluster` interceptor runs
        before the `post_update_connect_cluster_with_metadata` interceptor.
        """
        return response

    def post_update_connect_cluster_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_connect_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedKafkaConnect server but before it is returned to user code.

        We recommend only using this `post_update_connect_cluster_with_metadata`
        interceptor in new development instead of the `post_update_connect_cluster` interceptor.
        When both interceptors are used, this `post_update_connect_cluster_with_metadata` interceptor runs after the
        `post_update_connect_cluster` interceptor. The (possibly modified) response returned by
        `post_update_connect_cluster` will be passed to
        `post_update_connect_cluster_with_metadata`.
        """
        return response, metadata

    def pre_update_connector(
        self,
        request: managed_kafka_connect.UpdateConnectorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        managed_kafka_connect.UpdateConnectorRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_connector

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedKafkaConnect server.
        """
        return request, metadata

    def post_update_connector(
        self, response: resources.Connector
    ) -> resources.Connector:
        """Post-rpc interceptor for update_connector

        DEPRECATED. Please use the `post_update_connector_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ManagedKafkaConnect server but before
        it is returned to user code. This `post_update_connector` interceptor runs
        before the `post_update_connector_with_metadata` interceptor.
        """
        return response

    def post_update_connector_with_metadata(
        self,
        response: resources.Connector,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Connector, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_connector

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ManagedKafkaConnect server but before it is returned to user code.

        We recommend only using this `post_update_connector_with_metadata`
        interceptor in new development instead of the `post_update_connector` interceptor.
        When both interceptors are used, this `post_update_connector_with_metadata` interceptor runs after the
        `post_update_connector` interceptor. The (possibly modified) response returned by
        `post_update_connector` will be passed to
        `post_update_connector_with_metadata`.
        """
        return response, metadata

    def pre_get_location(
        self,
        request: locations_pb2.GetLocationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        locations_pb2.GetLocationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_location

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedKafkaConnect server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the ManagedKafkaConnect server but before
        it is returned to user code.
        """
        return response

    def pre_list_locations(
        self,
        request: locations_pb2.ListLocationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        locations_pb2.ListLocationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_locations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedKafkaConnect server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the ManagedKafkaConnect server but before
        it is returned to user code.
        """
        return response

    def pre_cancel_operation(
        self,
        request: operations_pb2.CancelOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.CancelOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedKafkaConnect server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the ManagedKafkaConnect server but before
        it is returned to user code.
        """
        return response

    def pre_delete_operation(
        self,
        request: operations_pb2.DeleteOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.DeleteOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedKafkaConnect server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the ManagedKafkaConnect server but before
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
        before they are sent to the ManagedKafkaConnect server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the ManagedKafkaConnect server but before
        it is returned to user code.
        """
        return response

    def pre_list_operations(
        self,
        request: operations_pb2.ListOperationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.ListOperationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_operations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ManagedKafkaConnect server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the ManagedKafkaConnect server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class ManagedKafkaConnectRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ManagedKafkaConnectRestInterceptor


class ManagedKafkaConnectRestTransport(_BaseManagedKafkaConnectRestTransport):
    """REST backend synchronous transport for ManagedKafkaConnect.

    The service that a client application uses to manage Apache
    Kafka Connect clusters and connectors.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "managedkafka.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[ManagedKafkaConnectRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'managedkafka.googleapis.com').
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
            interceptor (Optional[ManagedKafkaConnectRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or ManagedKafkaConnectRestInterceptor()
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
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}:cancel",
                        "body": "*",
                    },
                ],
                "google.longrunning.Operations.DeleteOperation": [
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*}/operations",
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

    class _CreateConnectCluster(
        _BaseManagedKafkaConnectRestTransport._BaseCreateConnectCluster,
        ManagedKafkaConnectRestStub,
    ):
        def __hash__(self):
            return hash("ManagedKafkaConnectRestTransport.CreateConnectCluster")

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
            request: managed_kafka_connect.CreateConnectClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create connect cluster method over HTTP.

            Args:
                request (~.managed_kafka_connect.CreateConnectClusterRequest):
                    The request object. Request for CreateConnectCluster.
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

            http_options = _BaseManagedKafkaConnectRestTransport._BaseCreateConnectCluster._get_http_options()
            request, metadata = self._interceptor.pre_create_connect_cluster(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedKafkaConnectRestTransport._BaseCreateConnectCluster,
                    "_BaseCreateConnectCluster__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.managedkafka_v1.ManagedKafkaConnectClient.CreateConnectCluster",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "CreateConnectCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ManagedKafkaConnectRestTransport._CreateConnectCluster._get_response(
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

            resp = self._interceptor.post_create_connect_cluster(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_connect_cluster_with_metadata(
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
                    "Received response for google.cloud.managedkafka_v1.ManagedKafkaConnectClient.create_connect_cluster",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "CreateConnectCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateConnector(
        _BaseManagedKafkaConnectRestTransport._BaseCreateConnector,
        ManagedKafkaConnectRestStub,
    ):
        def __hash__(self):
            return hash("ManagedKafkaConnectRestTransport.CreateConnector")

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
            request: managed_kafka_connect.CreateConnectorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Connector:
            r"""Call the create connector method over HTTP.

            Args:
                request (~.managed_kafka_connect.CreateConnectorRequest):
                    The request object. Request for CreateConnector.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Connector:
                    A Kafka Connect connector in a given
                ConnectCluster.

            """

            http_options = _BaseManagedKafkaConnectRestTransport._BaseCreateConnector._get_http_options()
            request, metadata = self._interceptor.pre_create_connector(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedKafkaConnectRestTransport._BaseCreateConnector,
                    "_BaseCreateConnector__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.managedkafka_v1.ManagedKafkaConnectClient.CreateConnector",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "CreateConnector",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ManagedKafkaConnectRestTransport._CreateConnector._get_response(
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
            resp = resources.Connector()
            pb_resp = resources.Connector.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_connector(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_connector_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Connector.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.managedkafka_v1.ManagedKafkaConnectClient.create_connector",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "CreateConnector",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteConnectCluster(
        _BaseManagedKafkaConnectRestTransport._BaseDeleteConnectCluster,
        ManagedKafkaConnectRestStub,
    ):
        def __hash__(self):
            return hash("ManagedKafkaConnectRestTransport.DeleteConnectCluster")

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
            request: managed_kafka_connect.DeleteConnectClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete connect cluster method over HTTP.

            Args:
                request (~.managed_kafka_connect.DeleteConnectClusterRequest):
                    The request object. Request for DeleteConnectCluster.
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

            http_options = _BaseManagedKafkaConnectRestTransport._BaseDeleteConnectCluster._get_http_options()
            request, metadata = self._interceptor.pre_delete_connect_cluster(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedKafkaConnectRestTransport._BaseDeleteConnectCluster,
                    "_BaseDeleteConnectCluster__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.managedkafka_v1.ManagedKafkaConnectClient.DeleteConnectCluster",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "DeleteConnectCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ManagedKafkaConnectRestTransport._DeleteConnectCluster._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_connect_cluster(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_connect_cluster_with_metadata(
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
                    "Received response for google.cloud.managedkafka_v1.ManagedKafkaConnectClient.delete_connect_cluster",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "DeleteConnectCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteConnector(
        _BaseManagedKafkaConnectRestTransport._BaseDeleteConnector,
        ManagedKafkaConnectRestStub,
    ):
        def __hash__(self):
            return hash("ManagedKafkaConnectRestTransport.DeleteConnector")

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
            request: managed_kafka_connect.DeleteConnectorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete connector method over HTTP.

            Args:
                request (~.managed_kafka_connect.DeleteConnectorRequest):
                    The request object. Request for DeleteConnector.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseManagedKafkaConnectRestTransport._BaseDeleteConnector._get_http_options()
            request, metadata = self._interceptor.pre_delete_connector(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedKafkaConnectRestTransport._BaseDeleteConnector,
                    "_BaseDeleteConnector__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.managedkafka_v1.ManagedKafkaConnectClient.DeleteConnector",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "DeleteConnector",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ManagedKafkaConnectRestTransport._DeleteConnector._get_response(
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

    class _GetConnectCluster(
        _BaseManagedKafkaConnectRestTransport._BaseGetConnectCluster,
        ManagedKafkaConnectRestStub,
    ):
        def __hash__(self):
            return hash("ManagedKafkaConnectRestTransport.GetConnectCluster")

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
            request: managed_kafka_connect.GetConnectClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.ConnectCluster:
            r"""Call the get connect cluster method over HTTP.

            Args:
                request (~.managed_kafka_connect.GetConnectClusterRequest):
                    The request object. Request for GetConnectCluster.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.ConnectCluster:
                    An Apache Kafka Connect cluster
                deployed in a location.

            """

            http_options = _BaseManagedKafkaConnectRestTransport._BaseGetConnectCluster._get_http_options()
            request, metadata = self._interceptor.pre_get_connect_cluster(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedKafkaConnectRestTransport._BaseGetConnectCluster,
                    "_BaseGetConnectCluster__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.managedkafka_v1.ManagedKafkaConnectClient.GetConnectCluster",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "GetConnectCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ManagedKafkaConnectRestTransport._GetConnectCluster._get_response(
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
            resp = resources.ConnectCluster()
            pb_resp = resources.ConnectCluster.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_connect_cluster(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_connect_cluster_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.ConnectCluster.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.managedkafka_v1.ManagedKafkaConnectClient.get_connect_cluster",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "GetConnectCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetConnector(
        _BaseManagedKafkaConnectRestTransport._BaseGetConnector,
        ManagedKafkaConnectRestStub,
    ):
        def __hash__(self):
            return hash("ManagedKafkaConnectRestTransport.GetConnector")

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
            request: managed_kafka_connect.GetConnectorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Connector:
            r"""Call the get connector method over HTTP.

            Args:
                request (~.managed_kafka_connect.GetConnectorRequest):
                    The request object. Request for GetConnector.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Connector:
                    A Kafka Connect connector in a given
                ConnectCluster.

            """

            http_options = _BaseManagedKafkaConnectRestTransport._BaseGetConnector._get_http_options()
            request, metadata = self._interceptor.pre_get_connector(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedKafkaConnectRestTransport._BaseGetConnector,
                    "_BaseGetConnector__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.managedkafka_v1.ManagedKafkaConnectClient.GetConnector",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "GetConnector",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ManagedKafkaConnectRestTransport._GetConnector._get_response(
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
            resp = resources.Connector()
            pb_resp = resources.Connector.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_connector(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_connector_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Connector.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.managedkafka_v1.ManagedKafkaConnectClient.get_connector",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "GetConnector",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListConnectClusters(
        _BaseManagedKafkaConnectRestTransport._BaseListConnectClusters,
        ManagedKafkaConnectRestStub,
    ):
        def __hash__(self):
            return hash("ManagedKafkaConnectRestTransport.ListConnectClusters")

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
            request: managed_kafka_connect.ListConnectClustersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> managed_kafka_connect.ListConnectClustersResponse:
            r"""Call the list connect clusters method over HTTP.

            Args:
                request (~.managed_kafka_connect.ListConnectClustersRequest):
                    The request object. Request for ListConnectClusters.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.managed_kafka_connect.ListConnectClustersResponse:
                    Response for ListConnectClusters.
            """

            http_options = _BaseManagedKafkaConnectRestTransport._BaseListConnectClusters._get_http_options()
            request, metadata = self._interceptor.pre_list_connect_clusters(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedKafkaConnectRestTransport._BaseListConnectClusters,
                    "_BaseListConnectClusters__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.managedkafka_v1.ManagedKafkaConnectClient.ListConnectClusters",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "ListConnectClusters",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ManagedKafkaConnectRestTransport._ListConnectClusters._get_response(
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
            resp = managed_kafka_connect.ListConnectClustersResponse()
            pb_resp = managed_kafka_connect.ListConnectClustersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_connect_clusters(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_connect_clusters_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        managed_kafka_connect.ListConnectClustersResponse.to_json(
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
                    "Received response for google.cloud.managedkafka_v1.ManagedKafkaConnectClient.list_connect_clusters",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "ListConnectClusters",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListConnectors(
        _BaseManagedKafkaConnectRestTransport._BaseListConnectors,
        ManagedKafkaConnectRestStub,
    ):
        def __hash__(self):
            return hash("ManagedKafkaConnectRestTransport.ListConnectors")

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
            request: managed_kafka_connect.ListConnectorsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> managed_kafka_connect.ListConnectorsResponse:
            r"""Call the list connectors method over HTTP.

            Args:
                request (~.managed_kafka_connect.ListConnectorsRequest):
                    The request object. Request for ListConnectors.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.managed_kafka_connect.ListConnectorsResponse:
                    Response for ListConnectors.
            """

            http_options = _BaseManagedKafkaConnectRestTransport._BaseListConnectors._get_http_options()
            request, metadata = self._interceptor.pre_list_connectors(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedKafkaConnectRestTransport._BaseListConnectors,
                    "_BaseListConnectors__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.managedkafka_v1.ManagedKafkaConnectClient.ListConnectors",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "ListConnectors",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ManagedKafkaConnectRestTransport._ListConnectors._get_response(
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
            resp = managed_kafka_connect.ListConnectorsResponse()
            pb_resp = managed_kafka_connect.ListConnectorsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_connectors(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_connectors_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        managed_kafka_connect.ListConnectorsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.managedkafka_v1.ManagedKafkaConnectClient.list_connectors",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "ListConnectors",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _PauseConnector(
        _BaseManagedKafkaConnectRestTransport._BasePauseConnector,
        ManagedKafkaConnectRestStub,
    ):
        def __hash__(self):
            return hash("ManagedKafkaConnectRestTransport.PauseConnector")

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
            request: managed_kafka_connect.PauseConnectorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> managed_kafka_connect.PauseConnectorResponse:
            r"""Call the pause connector method over HTTP.

            Args:
                request (~.managed_kafka_connect.PauseConnectorRequest):
                    The request object. Request for PauseConnector.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.managed_kafka_connect.PauseConnectorResponse:
                    Response for PauseConnector.
            """

            http_options = _BaseManagedKafkaConnectRestTransport._BasePauseConnector._get_http_options()
            request, metadata = self._interceptor.pre_pause_connector(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedKafkaConnectRestTransport._BasePauseConnector,
                    "_BasePauseConnector__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.managedkafka_v1.ManagedKafkaConnectClient.PauseConnector",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "PauseConnector",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ManagedKafkaConnectRestTransport._PauseConnector._get_response(
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
            resp = managed_kafka_connect.PauseConnectorResponse()
            pb_resp = managed_kafka_connect.PauseConnectorResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_pause_connector(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_pause_connector_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        managed_kafka_connect.PauseConnectorResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.managedkafka_v1.ManagedKafkaConnectClient.pause_connector",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "PauseConnector",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RestartConnector(
        _BaseManagedKafkaConnectRestTransport._BaseRestartConnector,
        ManagedKafkaConnectRestStub,
    ):
        def __hash__(self):
            return hash("ManagedKafkaConnectRestTransport.RestartConnector")

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
            request: managed_kafka_connect.RestartConnectorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> managed_kafka_connect.RestartConnectorResponse:
            r"""Call the restart connector method over HTTP.

            Args:
                request (~.managed_kafka_connect.RestartConnectorRequest):
                    The request object. Request for RestartConnector.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.managed_kafka_connect.RestartConnectorResponse:
                    Response for RestartConnector.
            """

            http_options = _BaseManagedKafkaConnectRestTransport._BaseRestartConnector._get_http_options()
            request, metadata = self._interceptor.pre_restart_connector(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedKafkaConnectRestTransport._BaseRestartConnector,
                    "_BaseRestartConnector__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.managedkafka_v1.ManagedKafkaConnectClient.RestartConnector",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "RestartConnector",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ManagedKafkaConnectRestTransport._RestartConnector._get_response(
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
            resp = managed_kafka_connect.RestartConnectorResponse()
            pb_resp = managed_kafka_connect.RestartConnectorResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_restart_connector(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_restart_connector_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        managed_kafka_connect.RestartConnectorResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.managedkafka_v1.ManagedKafkaConnectClient.restart_connector",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "RestartConnector",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ResumeConnector(
        _BaseManagedKafkaConnectRestTransport._BaseResumeConnector,
        ManagedKafkaConnectRestStub,
    ):
        def __hash__(self):
            return hash("ManagedKafkaConnectRestTransport.ResumeConnector")

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
            request: managed_kafka_connect.ResumeConnectorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> managed_kafka_connect.ResumeConnectorResponse:
            r"""Call the resume connector method over HTTP.

            Args:
                request (~.managed_kafka_connect.ResumeConnectorRequest):
                    The request object. Request for ResumeConnector.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.managed_kafka_connect.ResumeConnectorResponse:
                    Response for ResumeConnector.
            """

            http_options = _BaseManagedKafkaConnectRestTransport._BaseResumeConnector._get_http_options()
            request, metadata = self._interceptor.pre_resume_connector(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedKafkaConnectRestTransport._BaseResumeConnector,
                    "_BaseResumeConnector__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.managedkafka_v1.ManagedKafkaConnectClient.ResumeConnector",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "ResumeConnector",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ManagedKafkaConnectRestTransport._ResumeConnector._get_response(
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
            resp = managed_kafka_connect.ResumeConnectorResponse()
            pb_resp = managed_kafka_connect.ResumeConnectorResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_resume_connector(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_resume_connector_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        managed_kafka_connect.ResumeConnectorResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.managedkafka_v1.ManagedKafkaConnectClient.resume_connector",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "ResumeConnector",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _StopConnector(
        _BaseManagedKafkaConnectRestTransport._BaseStopConnector,
        ManagedKafkaConnectRestStub,
    ):
        def __hash__(self):
            return hash("ManagedKafkaConnectRestTransport.StopConnector")

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
            request: managed_kafka_connect.StopConnectorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> managed_kafka_connect.StopConnectorResponse:
            r"""Call the stop connector method over HTTP.

            Args:
                request (~.managed_kafka_connect.StopConnectorRequest):
                    The request object. Request for StopConnector.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.managed_kafka_connect.StopConnectorResponse:
                    Response for StopConnector.
            """

            http_options = _BaseManagedKafkaConnectRestTransport._BaseStopConnector._get_http_options()
            request, metadata = self._interceptor.pre_stop_connector(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedKafkaConnectRestTransport._BaseStopConnector,
                    "_BaseStopConnector__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.managedkafka_v1.ManagedKafkaConnectClient.StopConnector",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "StopConnector",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ManagedKafkaConnectRestTransport._StopConnector._get_response(
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
            resp = managed_kafka_connect.StopConnectorResponse()
            pb_resp = managed_kafka_connect.StopConnectorResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_stop_connector(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_stop_connector_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        managed_kafka_connect.StopConnectorResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.managedkafka_v1.ManagedKafkaConnectClient.stop_connector",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "StopConnector",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateConnectCluster(
        _BaseManagedKafkaConnectRestTransport._BaseUpdateConnectCluster,
        ManagedKafkaConnectRestStub,
    ):
        def __hash__(self):
            return hash("ManagedKafkaConnectRestTransport.UpdateConnectCluster")

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
            request: managed_kafka_connect.UpdateConnectClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update connect cluster method over HTTP.

            Args:
                request (~.managed_kafka_connect.UpdateConnectClusterRequest):
                    The request object. Request for UpdateConnectCluster.
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

            http_options = _BaseManagedKafkaConnectRestTransport._BaseUpdateConnectCluster._get_http_options()
            request, metadata = self._interceptor.pre_update_connect_cluster(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedKafkaConnectRestTransport._BaseUpdateConnectCluster,
                    "_BaseUpdateConnectCluster__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.managedkafka_v1.ManagedKafkaConnectClient.UpdateConnectCluster",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "UpdateConnectCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ManagedKafkaConnectRestTransport._UpdateConnectCluster._get_response(
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

            resp = self._interceptor.post_update_connect_cluster(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_connect_cluster_with_metadata(
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
                    "Received response for google.cloud.managedkafka_v1.ManagedKafkaConnectClient.update_connect_cluster",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "UpdateConnectCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateConnector(
        _BaseManagedKafkaConnectRestTransport._BaseUpdateConnector,
        ManagedKafkaConnectRestStub,
    ):
        def __hash__(self):
            return hash("ManagedKafkaConnectRestTransport.UpdateConnector")

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
            request: managed_kafka_connect.UpdateConnectorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Connector:
            r"""Call the update connector method over HTTP.

            Args:
                request (~.managed_kafka_connect.UpdateConnectorRequest):
                    The request object. Request for UpdateConnector.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Connector:
                    A Kafka Connect connector in a given
                ConnectCluster.

            """

            http_options = _BaseManagedKafkaConnectRestTransport._BaseUpdateConnector._get_http_options()
            request, metadata = self._interceptor.pre_update_connector(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedKafkaConnectRestTransport._BaseUpdateConnector,
                    "_BaseUpdateConnector__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.managedkafka_v1.ManagedKafkaConnectClient.UpdateConnector",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "UpdateConnector",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ManagedKafkaConnectRestTransport._UpdateConnector._get_response(
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
            resp = resources.Connector()
            pb_resp = resources.Connector.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_connector(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_connector_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Connector.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.managedkafka_v1.ManagedKafkaConnectClient.update_connector",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "UpdateConnector",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_connect_cluster(
        self,
    ) -> Callable[
        [managed_kafka_connect.CreateConnectClusterRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateConnectCluster(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_connector(
        self,
    ) -> Callable[[managed_kafka_connect.CreateConnectorRequest], resources.Connector]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateConnector(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_connect_cluster(
        self,
    ) -> Callable[
        [managed_kafka_connect.DeleteConnectClusterRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteConnectCluster(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_connector(
        self,
    ) -> Callable[[managed_kafka_connect.DeleteConnectorRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteConnector(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_connect_cluster(
        self,
    ) -> Callable[
        [managed_kafka_connect.GetConnectClusterRequest], resources.ConnectCluster
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetConnectCluster(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_connector(
        self,
    ) -> Callable[[managed_kafka_connect.GetConnectorRequest], resources.Connector]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetConnector(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_connect_clusters(
        self,
    ) -> Callable[
        [managed_kafka_connect.ListConnectClustersRequest],
        managed_kafka_connect.ListConnectClustersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListConnectClusters(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_connectors(
        self,
    ) -> Callable[
        [managed_kafka_connect.ListConnectorsRequest],
        managed_kafka_connect.ListConnectorsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListConnectors(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def pause_connector(
        self,
    ) -> Callable[
        [managed_kafka_connect.PauseConnectorRequest],
        managed_kafka_connect.PauseConnectorResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PauseConnector(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def restart_connector(
        self,
    ) -> Callable[
        [managed_kafka_connect.RestartConnectorRequest],
        managed_kafka_connect.RestartConnectorResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RestartConnector(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def resume_connector(
        self,
    ) -> Callable[
        [managed_kafka_connect.ResumeConnectorRequest],
        managed_kafka_connect.ResumeConnectorResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ResumeConnector(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def stop_connector(
        self,
    ) -> Callable[
        [managed_kafka_connect.StopConnectorRequest],
        managed_kafka_connect.StopConnectorResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StopConnector(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_connect_cluster(
        self,
    ) -> Callable[
        [managed_kafka_connect.UpdateConnectClusterRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateConnectCluster(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_connector(
        self,
    ) -> Callable[[managed_kafka_connect.UpdateConnectorRequest], resources.Connector]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateConnector(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseManagedKafkaConnectRestTransport._BaseGetLocation,
        ManagedKafkaConnectRestStub,
    ):
        def __hash__(self):
            return hash("ManagedKafkaConnectRestTransport.GetLocation")

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
            request: locations_pb2.GetLocationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> locations_pb2.Location:
            r"""Call the get location method over HTTP.

            Args:
                request (locations_pb2.GetLocationRequest):
                    The request object for GetLocation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                locations_pb2.Location: Response from GetLocation method.
            """

            http_options = _BaseManagedKafkaConnectRestTransport._BaseGetLocation._get_http_options()
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedKafkaConnectRestTransport._BaseGetLocation,
                    "_BaseGetLocation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.managedkafka_v1.ManagedKafkaConnectClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ManagedKafkaConnectRestTransport._GetLocation._get_response(
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
            resp = locations_pb2.Location()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_location(resp)
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
                    "Received response for google.cloud.managedkafka_v1.ManagedKafkaConnectAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "GetLocation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_locations(self):
        return self._ListLocations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListLocations(
        _BaseManagedKafkaConnectRestTransport._BaseListLocations,
        ManagedKafkaConnectRestStub,
    ):
        def __hash__(self):
            return hash("ManagedKafkaConnectRestTransport.ListLocations")

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
            request: locations_pb2.ListLocationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> locations_pb2.ListLocationsResponse:
            r"""Call the list locations method over HTTP.

            Args:
                request (locations_pb2.ListLocationsRequest):
                    The request object for ListLocations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                locations_pb2.ListLocationsResponse: Response from ListLocations method.
            """

            http_options = _BaseManagedKafkaConnectRestTransport._BaseListLocations._get_http_options()
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedKafkaConnectRestTransport._BaseListLocations,
                    "_BaseListLocations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.managedkafka_v1.ManagedKafkaConnectClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ManagedKafkaConnectRestTransport._ListLocations._get_response(
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
            resp = locations_pb2.ListLocationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_locations(resp)
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
                    "Received response for google.cloud.managedkafka_v1.ManagedKafkaConnectAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "ListLocations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseManagedKafkaConnectRestTransport._BaseCancelOperation,
        ManagedKafkaConnectRestStub,
    ):
        def __hash__(self):
            return hash("ManagedKafkaConnectRestTransport.CancelOperation")

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

            http_options = _BaseManagedKafkaConnectRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedKafkaConnectRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.managedkafka_v1.ManagedKafkaConnectClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ManagedKafkaConnectRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def delete_operation(self):
        return self._DeleteOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _DeleteOperation(
        _BaseManagedKafkaConnectRestTransport._BaseDeleteOperation,
        ManagedKafkaConnectRestStub,
    ):
        def __hash__(self):
            return hash("ManagedKafkaConnectRestTransport.DeleteOperation")

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
            request: operations_pb2.DeleteOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> None:
            r"""Call the delete operation method over HTTP.

            Args:
                request (operations_pb2.DeleteOperationRequest):
                    The request object for DeleteOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseManagedKafkaConnectRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedKafkaConnectRestTransport._BaseDeleteOperation,
                    "_BaseDeleteOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.managedkafka_v1.ManagedKafkaConnectClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ManagedKafkaConnectRestTransport._DeleteOperation._get_response(
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

            return self._interceptor.post_delete_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseManagedKafkaConnectRestTransport._BaseGetOperation,
        ManagedKafkaConnectRestStub,
    ):
        def __hash__(self):
            return hash("ManagedKafkaConnectRestTransport.GetOperation")

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

            http_options = _BaseManagedKafkaConnectRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedKafkaConnectRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.managedkafka_v1.ManagedKafkaConnectClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ManagedKafkaConnectRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.managedkafka_v1.ManagedKafkaConnectAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "GetOperation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_operations(self):
        return self._ListOperations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListOperations(
        _BaseManagedKafkaConnectRestTransport._BaseListOperations,
        ManagedKafkaConnectRestStub,
    ):
        def __hash__(self):
            return hash("ManagedKafkaConnectRestTransport.ListOperations")

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
            request: operations_pb2.ListOperationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.ListOperationsResponse:
            r"""Call the list operations method over HTTP.

            Args:
                request (operations_pb2.ListOperationsRequest):
                    The request object for ListOperations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                operations_pb2.ListOperationsResponse: Response from ListOperations method.
            """

            http_options = _BaseManagedKafkaConnectRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseManagedKafkaConnectRestTransport._BaseListOperations,
                    "_BaseListOperations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.managedkafka_v1.ManagedKafkaConnectClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ManagedKafkaConnectRestTransport._ListOperations._get_response(
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
            resp = operations_pb2.ListOperationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_operations(resp)
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
                    "Received response for google.cloud.managedkafka_v1.ManagedKafkaConnectAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.managedkafka.v1.ManagedKafkaConnect",
                        "rpcName": "ListOperations",
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


__all__ = ("ManagedKafkaConnectRestTransport",)
