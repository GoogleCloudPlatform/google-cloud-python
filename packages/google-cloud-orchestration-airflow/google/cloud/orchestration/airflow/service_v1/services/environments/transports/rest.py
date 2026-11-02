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
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.orchestration.airflow.service_v1._compat import transcode_request
from google.cloud.orchestration.airflow.service_v1.types import environments

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseEnvironmentsRestTransport

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


class EnvironmentsRestInterceptor:
    """Interceptor for Environments.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the EnvironmentsRestTransport.

    .. code-block:: python
        class MyCustomEnvironmentsInterceptor(EnvironmentsRestInterceptor):
            def pre_check_upgrade(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_check_upgrade(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_environment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_environment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_user_workloads_config_map(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_user_workloads_config_map(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_user_workloads_secret(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_user_workloads_secret(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_database_failover(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_database_failover(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_environment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_environment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_user_workloads_config_map(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_user_workloads_secret(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_execute_airflow_command(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_execute_airflow_command(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_database_properties(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_database_properties(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_environment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_environment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_user_workloads_config_map(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_user_workloads_config_map(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_user_workloads_secret(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_user_workloads_secret(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_environments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_environments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_user_workloads_config_maps(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_user_workloads_config_maps(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_user_workloads_secrets(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_user_workloads_secrets(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_workloads(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_workloads(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_load_snapshot(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_load_snapshot(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_poll_airflow_command(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_poll_airflow_command(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_save_snapshot(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_save_snapshot(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_stop_airflow_command(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_stop_airflow_command(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_environment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_environment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_user_workloads_config_map(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_user_workloads_config_map(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_user_workloads_secret(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_user_workloads_secret(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = EnvironmentsRestTransport(interceptor=MyCustomEnvironmentsInterceptor())
        client = EnvironmentsClient(transport=transport)


    """

    def pre_check_upgrade(
        self,
        request: environments.CheckUpgradeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.CheckUpgradeRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for check_upgrade

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Environments server.
        """
        return request, metadata

    def post_check_upgrade(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for check_upgrade

        DEPRECATED. Please use the `post_check_upgrade_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Environments server but before
        it is returned to user code. This `post_check_upgrade` interceptor runs
        before the `post_check_upgrade_with_metadata` interceptor.
        """
        return response

    def post_check_upgrade_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for check_upgrade

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Environments server but before it is returned to user code.

        We recommend only using this `post_check_upgrade_with_metadata`
        interceptor in new development instead of the `post_check_upgrade` interceptor.
        When both interceptors are used, this `post_check_upgrade_with_metadata` interceptor runs after the
        `post_check_upgrade` interceptor. The (possibly modified) response returned by
        `post_check_upgrade` will be passed to
        `post_check_upgrade_with_metadata`.
        """
        return response, metadata

    def pre_create_environment(
        self,
        request: environments.CreateEnvironmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.CreateEnvironmentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_environment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Environments server.
        """
        return request, metadata

    def post_create_environment(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_environment

        DEPRECATED. Please use the `post_create_environment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Environments server but before
        it is returned to user code. This `post_create_environment` interceptor runs
        before the `post_create_environment_with_metadata` interceptor.
        """
        return response

    def post_create_environment_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_environment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Environments server but before it is returned to user code.

        We recommend only using this `post_create_environment_with_metadata`
        interceptor in new development instead of the `post_create_environment` interceptor.
        When both interceptors are used, this `post_create_environment_with_metadata` interceptor runs after the
        `post_create_environment` interceptor. The (possibly modified) response returned by
        `post_create_environment` will be passed to
        `post_create_environment_with_metadata`.
        """
        return response, metadata

    def pre_create_user_workloads_config_map(
        self,
        request: environments.CreateUserWorkloadsConfigMapRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.CreateUserWorkloadsConfigMapRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_user_workloads_config_map

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Environments server.
        """
        return request, metadata

    def post_create_user_workloads_config_map(
        self, response: environments.UserWorkloadsConfigMap
    ) -> environments.UserWorkloadsConfigMap:
        """Post-rpc interceptor for create_user_workloads_config_map

        DEPRECATED. Please use the `post_create_user_workloads_config_map_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Environments server but before
        it is returned to user code. This `post_create_user_workloads_config_map` interceptor runs
        before the `post_create_user_workloads_config_map_with_metadata` interceptor.
        """
        return response

    def post_create_user_workloads_config_map_with_metadata(
        self,
        response: environments.UserWorkloadsConfigMap,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.UserWorkloadsConfigMap, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_user_workloads_config_map

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Environments server but before it is returned to user code.

        We recommend only using this `post_create_user_workloads_config_map_with_metadata`
        interceptor in new development instead of the `post_create_user_workloads_config_map` interceptor.
        When both interceptors are used, this `post_create_user_workloads_config_map_with_metadata` interceptor runs after the
        `post_create_user_workloads_config_map` interceptor. The (possibly modified) response returned by
        `post_create_user_workloads_config_map` will be passed to
        `post_create_user_workloads_config_map_with_metadata`.
        """
        return response, metadata

    def pre_create_user_workloads_secret(
        self,
        request: environments.CreateUserWorkloadsSecretRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.CreateUserWorkloadsSecretRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_user_workloads_secret

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Environments server.
        """
        return request, metadata

    def post_create_user_workloads_secret(
        self, response: environments.UserWorkloadsSecret
    ) -> environments.UserWorkloadsSecret:
        """Post-rpc interceptor for create_user_workloads_secret

        DEPRECATED. Please use the `post_create_user_workloads_secret_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Environments server but before
        it is returned to user code. This `post_create_user_workloads_secret` interceptor runs
        before the `post_create_user_workloads_secret_with_metadata` interceptor.
        """
        return response

    def post_create_user_workloads_secret_with_metadata(
        self,
        response: environments.UserWorkloadsSecret,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.UserWorkloadsSecret, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_user_workloads_secret

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Environments server but before it is returned to user code.

        We recommend only using this `post_create_user_workloads_secret_with_metadata`
        interceptor in new development instead of the `post_create_user_workloads_secret` interceptor.
        When both interceptors are used, this `post_create_user_workloads_secret_with_metadata` interceptor runs after the
        `post_create_user_workloads_secret` interceptor. The (possibly modified) response returned by
        `post_create_user_workloads_secret` will be passed to
        `post_create_user_workloads_secret_with_metadata`.
        """
        return response, metadata

    def pre_database_failover(
        self,
        request: environments.DatabaseFailoverRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.DatabaseFailoverRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for database_failover

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Environments server.
        """
        return request, metadata

    def post_database_failover(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for database_failover

        DEPRECATED. Please use the `post_database_failover_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Environments server but before
        it is returned to user code. This `post_database_failover` interceptor runs
        before the `post_database_failover_with_metadata` interceptor.
        """
        return response

    def post_database_failover_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for database_failover

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Environments server but before it is returned to user code.

        We recommend only using this `post_database_failover_with_metadata`
        interceptor in new development instead of the `post_database_failover` interceptor.
        When both interceptors are used, this `post_database_failover_with_metadata` interceptor runs after the
        `post_database_failover` interceptor. The (possibly modified) response returned by
        `post_database_failover` will be passed to
        `post_database_failover_with_metadata`.
        """
        return response, metadata

    def pre_delete_environment(
        self,
        request: environments.DeleteEnvironmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.DeleteEnvironmentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_environment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Environments server.
        """
        return request, metadata

    def post_delete_environment(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_environment

        DEPRECATED. Please use the `post_delete_environment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Environments server but before
        it is returned to user code. This `post_delete_environment` interceptor runs
        before the `post_delete_environment_with_metadata` interceptor.
        """
        return response

    def post_delete_environment_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_environment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Environments server but before it is returned to user code.

        We recommend only using this `post_delete_environment_with_metadata`
        interceptor in new development instead of the `post_delete_environment` interceptor.
        When both interceptors are used, this `post_delete_environment_with_metadata` interceptor runs after the
        `post_delete_environment` interceptor. The (possibly modified) response returned by
        `post_delete_environment` will be passed to
        `post_delete_environment_with_metadata`.
        """
        return response, metadata

    def pre_delete_user_workloads_config_map(
        self,
        request: environments.DeleteUserWorkloadsConfigMapRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.DeleteUserWorkloadsConfigMapRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_user_workloads_config_map

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Environments server.
        """
        return request, metadata

    def pre_delete_user_workloads_secret(
        self,
        request: environments.DeleteUserWorkloadsSecretRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.DeleteUserWorkloadsSecretRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_user_workloads_secret

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Environments server.
        """
        return request, metadata

    def pre_execute_airflow_command(
        self,
        request: environments.ExecuteAirflowCommandRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.ExecuteAirflowCommandRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for execute_airflow_command

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Environments server.
        """
        return request, metadata

    def post_execute_airflow_command(
        self, response: environments.ExecuteAirflowCommandResponse
    ) -> environments.ExecuteAirflowCommandResponse:
        """Post-rpc interceptor for execute_airflow_command

        DEPRECATED. Please use the `post_execute_airflow_command_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Environments server but before
        it is returned to user code. This `post_execute_airflow_command` interceptor runs
        before the `post_execute_airflow_command_with_metadata` interceptor.
        """
        return response

    def post_execute_airflow_command_with_metadata(
        self,
        response: environments.ExecuteAirflowCommandResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.ExecuteAirflowCommandResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for execute_airflow_command

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Environments server but before it is returned to user code.

        We recommend only using this `post_execute_airflow_command_with_metadata`
        interceptor in new development instead of the `post_execute_airflow_command` interceptor.
        When both interceptors are used, this `post_execute_airflow_command_with_metadata` interceptor runs after the
        `post_execute_airflow_command` interceptor. The (possibly modified) response returned by
        `post_execute_airflow_command` will be passed to
        `post_execute_airflow_command_with_metadata`.
        """
        return response, metadata

    def pre_fetch_database_properties(
        self,
        request: environments.FetchDatabasePropertiesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.FetchDatabasePropertiesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for fetch_database_properties

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Environments server.
        """
        return request, metadata

    def post_fetch_database_properties(
        self, response: environments.FetchDatabasePropertiesResponse
    ) -> environments.FetchDatabasePropertiesResponse:
        """Post-rpc interceptor for fetch_database_properties

        DEPRECATED. Please use the `post_fetch_database_properties_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Environments server but before
        it is returned to user code. This `post_fetch_database_properties` interceptor runs
        before the `post_fetch_database_properties_with_metadata` interceptor.
        """
        return response

    def post_fetch_database_properties_with_metadata(
        self,
        response: environments.FetchDatabasePropertiesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.FetchDatabasePropertiesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for fetch_database_properties

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Environments server but before it is returned to user code.

        We recommend only using this `post_fetch_database_properties_with_metadata`
        interceptor in new development instead of the `post_fetch_database_properties` interceptor.
        When both interceptors are used, this `post_fetch_database_properties_with_metadata` interceptor runs after the
        `post_fetch_database_properties` interceptor. The (possibly modified) response returned by
        `post_fetch_database_properties` will be passed to
        `post_fetch_database_properties_with_metadata`.
        """
        return response, metadata

    def pre_get_environment(
        self,
        request: environments.GetEnvironmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.GetEnvironmentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_environment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Environments server.
        """
        return request, metadata

    def post_get_environment(
        self, response: environments.Environment
    ) -> environments.Environment:
        """Post-rpc interceptor for get_environment

        DEPRECATED. Please use the `post_get_environment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Environments server but before
        it is returned to user code. This `post_get_environment` interceptor runs
        before the `post_get_environment_with_metadata` interceptor.
        """
        return response

    def post_get_environment_with_metadata(
        self,
        response: environments.Environment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[environments.Environment, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_environment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Environments server but before it is returned to user code.

        We recommend only using this `post_get_environment_with_metadata`
        interceptor in new development instead of the `post_get_environment` interceptor.
        When both interceptors are used, this `post_get_environment_with_metadata` interceptor runs after the
        `post_get_environment` interceptor. The (possibly modified) response returned by
        `post_get_environment` will be passed to
        `post_get_environment_with_metadata`.
        """
        return response, metadata

    def pre_get_user_workloads_config_map(
        self,
        request: environments.GetUserWorkloadsConfigMapRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.GetUserWorkloadsConfigMapRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_user_workloads_config_map

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Environments server.
        """
        return request, metadata

    def post_get_user_workloads_config_map(
        self, response: environments.UserWorkloadsConfigMap
    ) -> environments.UserWorkloadsConfigMap:
        """Post-rpc interceptor for get_user_workloads_config_map

        DEPRECATED. Please use the `post_get_user_workloads_config_map_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Environments server but before
        it is returned to user code. This `post_get_user_workloads_config_map` interceptor runs
        before the `post_get_user_workloads_config_map_with_metadata` interceptor.
        """
        return response

    def post_get_user_workloads_config_map_with_metadata(
        self,
        response: environments.UserWorkloadsConfigMap,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.UserWorkloadsConfigMap, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_user_workloads_config_map

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Environments server but before it is returned to user code.

        We recommend only using this `post_get_user_workloads_config_map_with_metadata`
        interceptor in new development instead of the `post_get_user_workloads_config_map` interceptor.
        When both interceptors are used, this `post_get_user_workloads_config_map_with_metadata` interceptor runs after the
        `post_get_user_workloads_config_map` interceptor. The (possibly modified) response returned by
        `post_get_user_workloads_config_map` will be passed to
        `post_get_user_workloads_config_map_with_metadata`.
        """
        return response, metadata

    def pre_get_user_workloads_secret(
        self,
        request: environments.GetUserWorkloadsSecretRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.GetUserWorkloadsSecretRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_user_workloads_secret

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Environments server.
        """
        return request, metadata

    def post_get_user_workloads_secret(
        self, response: environments.UserWorkloadsSecret
    ) -> environments.UserWorkloadsSecret:
        """Post-rpc interceptor for get_user_workloads_secret

        DEPRECATED. Please use the `post_get_user_workloads_secret_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Environments server but before
        it is returned to user code. This `post_get_user_workloads_secret` interceptor runs
        before the `post_get_user_workloads_secret_with_metadata` interceptor.
        """
        return response

    def post_get_user_workloads_secret_with_metadata(
        self,
        response: environments.UserWorkloadsSecret,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.UserWorkloadsSecret, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_user_workloads_secret

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Environments server but before it is returned to user code.

        We recommend only using this `post_get_user_workloads_secret_with_metadata`
        interceptor in new development instead of the `post_get_user_workloads_secret` interceptor.
        When both interceptors are used, this `post_get_user_workloads_secret_with_metadata` interceptor runs after the
        `post_get_user_workloads_secret` interceptor. The (possibly modified) response returned by
        `post_get_user_workloads_secret` will be passed to
        `post_get_user_workloads_secret_with_metadata`.
        """
        return response, metadata

    def pre_list_environments(
        self,
        request: environments.ListEnvironmentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.ListEnvironmentsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_environments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Environments server.
        """
        return request, metadata

    def post_list_environments(
        self, response: environments.ListEnvironmentsResponse
    ) -> environments.ListEnvironmentsResponse:
        """Post-rpc interceptor for list_environments

        DEPRECATED. Please use the `post_list_environments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Environments server but before
        it is returned to user code. This `post_list_environments` interceptor runs
        before the `post_list_environments_with_metadata` interceptor.
        """
        return response

    def post_list_environments_with_metadata(
        self,
        response: environments.ListEnvironmentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.ListEnvironmentsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_environments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Environments server but before it is returned to user code.

        We recommend only using this `post_list_environments_with_metadata`
        interceptor in new development instead of the `post_list_environments` interceptor.
        When both interceptors are used, this `post_list_environments_with_metadata` interceptor runs after the
        `post_list_environments` interceptor. The (possibly modified) response returned by
        `post_list_environments` will be passed to
        `post_list_environments_with_metadata`.
        """
        return response, metadata

    def pre_list_user_workloads_config_maps(
        self,
        request: environments.ListUserWorkloadsConfigMapsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.ListUserWorkloadsConfigMapsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_user_workloads_config_maps

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Environments server.
        """
        return request, metadata

    def post_list_user_workloads_config_maps(
        self, response: environments.ListUserWorkloadsConfigMapsResponse
    ) -> environments.ListUserWorkloadsConfigMapsResponse:
        """Post-rpc interceptor for list_user_workloads_config_maps

        DEPRECATED. Please use the `post_list_user_workloads_config_maps_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Environments server but before
        it is returned to user code. This `post_list_user_workloads_config_maps` interceptor runs
        before the `post_list_user_workloads_config_maps_with_metadata` interceptor.
        """
        return response

    def post_list_user_workloads_config_maps_with_metadata(
        self,
        response: environments.ListUserWorkloadsConfigMapsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.ListUserWorkloadsConfigMapsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_user_workloads_config_maps

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Environments server but before it is returned to user code.

        We recommend only using this `post_list_user_workloads_config_maps_with_metadata`
        interceptor in new development instead of the `post_list_user_workloads_config_maps` interceptor.
        When both interceptors are used, this `post_list_user_workloads_config_maps_with_metadata` interceptor runs after the
        `post_list_user_workloads_config_maps` interceptor. The (possibly modified) response returned by
        `post_list_user_workloads_config_maps` will be passed to
        `post_list_user_workloads_config_maps_with_metadata`.
        """
        return response, metadata

    def pre_list_user_workloads_secrets(
        self,
        request: environments.ListUserWorkloadsSecretsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.ListUserWorkloadsSecretsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_user_workloads_secrets

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Environments server.
        """
        return request, metadata

    def post_list_user_workloads_secrets(
        self, response: environments.ListUserWorkloadsSecretsResponse
    ) -> environments.ListUserWorkloadsSecretsResponse:
        """Post-rpc interceptor for list_user_workloads_secrets

        DEPRECATED. Please use the `post_list_user_workloads_secrets_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Environments server but before
        it is returned to user code. This `post_list_user_workloads_secrets` interceptor runs
        before the `post_list_user_workloads_secrets_with_metadata` interceptor.
        """
        return response

    def post_list_user_workloads_secrets_with_metadata(
        self,
        response: environments.ListUserWorkloadsSecretsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.ListUserWorkloadsSecretsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_user_workloads_secrets

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Environments server but before it is returned to user code.

        We recommend only using this `post_list_user_workloads_secrets_with_metadata`
        interceptor in new development instead of the `post_list_user_workloads_secrets` interceptor.
        When both interceptors are used, this `post_list_user_workloads_secrets_with_metadata` interceptor runs after the
        `post_list_user_workloads_secrets` interceptor. The (possibly modified) response returned by
        `post_list_user_workloads_secrets` will be passed to
        `post_list_user_workloads_secrets_with_metadata`.
        """
        return response, metadata

    def pre_list_workloads(
        self,
        request: environments.ListWorkloadsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.ListWorkloadsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_workloads

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Environments server.
        """
        return request, metadata

    def post_list_workloads(
        self, response: environments.ListWorkloadsResponse
    ) -> environments.ListWorkloadsResponse:
        """Post-rpc interceptor for list_workloads

        DEPRECATED. Please use the `post_list_workloads_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Environments server but before
        it is returned to user code. This `post_list_workloads` interceptor runs
        before the `post_list_workloads_with_metadata` interceptor.
        """
        return response

    def post_list_workloads_with_metadata(
        self,
        response: environments.ListWorkloadsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.ListWorkloadsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_workloads

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Environments server but before it is returned to user code.

        We recommend only using this `post_list_workloads_with_metadata`
        interceptor in new development instead of the `post_list_workloads` interceptor.
        When both interceptors are used, this `post_list_workloads_with_metadata` interceptor runs after the
        `post_list_workloads` interceptor. The (possibly modified) response returned by
        `post_list_workloads` will be passed to
        `post_list_workloads_with_metadata`.
        """
        return response, metadata

    def pre_load_snapshot(
        self,
        request: environments.LoadSnapshotRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.LoadSnapshotRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for load_snapshot

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Environments server.
        """
        return request, metadata

    def post_load_snapshot(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for load_snapshot

        DEPRECATED. Please use the `post_load_snapshot_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Environments server but before
        it is returned to user code. This `post_load_snapshot` interceptor runs
        before the `post_load_snapshot_with_metadata` interceptor.
        """
        return response

    def post_load_snapshot_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for load_snapshot

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Environments server but before it is returned to user code.

        We recommend only using this `post_load_snapshot_with_metadata`
        interceptor in new development instead of the `post_load_snapshot` interceptor.
        When both interceptors are used, this `post_load_snapshot_with_metadata` interceptor runs after the
        `post_load_snapshot` interceptor. The (possibly modified) response returned by
        `post_load_snapshot` will be passed to
        `post_load_snapshot_with_metadata`.
        """
        return response, metadata

    def pre_poll_airflow_command(
        self,
        request: environments.PollAirflowCommandRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.PollAirflowCommandRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for poll_airflow_command

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Environments server.
        """
        return request, metadata

    def post_poll_airflow_command(
        self, response: environments.PollAirflowCommandResponse
    ) -> environments.PollAirflowCommandResponse:
        """Post-rpc interceptor for poll_airflow_command

        DEPRECATED. Please use the `post_poll_airflow_command_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Environments server but before
        it is returned to user code. This `post_poll_airflow_command` interceptor runs
        before the `post_poll_airflow_command_with_metadata` interceptor.
        """
        return response

    def post_poll_airflow_command_with_metadata(
        self,
        response: environments.PollAirflowCommandResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.PollAirflowCommandResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for poll_airflow_command

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Environments server but before it is returned to user code.

        We recommend only using this `post_poll_airflow_command_with_metadata`
        interceptor in new development instead of the `post_poll_airflow_command` interceptor.
        When both interceptors are used, this `post_poll_airflow_command_with_metadata` interceptor runs after the
        `post_poll_airflow_command` interceptor. The (possibly modified) response returned by
        `post_poll_airflow_command` will be passed to
        `post_poll_airflow_command_with_metadata`.
        """
        return response, metadata

    def pre_save_snapshot(
        self,
        request: environments.SaveSnapshotRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.SaveSnapshotRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for save_snapshot

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Environments server.
        """
        return request, metadata

    def post_save_snapshot(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for save_snapshot

        DEPRECATED. Please use the `post_save_snapshot_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Environments server but before
        it is returned to user code. This `post_save_snapshot` interceptor runs
        before the `post_save_snapshot_with_metadata` interceptor.
        """
        return response

    def post_save_snapshot_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for save_snapshot

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Environments server but before it is returned to user code.

        We recommend only using this `post_save_snapshot_with_metadata`
        interceptor in new development instead of the `post_save_snapshot` interceptor.
        When both interceptors are used, this `post_save_snapshot_with_metadata` interceptor runs after the
        `post_save_snapshot` interceptor. The (possibly modified) response returned by
        `post_save_snapshot` will be passed to
        `post_save_snapshot_with_metadata`.
        """
        return response, metadata

    def pre_stop_airflow_command(
        self,
        request: environments.StopAirflowCommandRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.StopAirflowCommandRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for stop_airflow_command

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Environments server.
        """
        return request, metadata

    def post_stop_airflow_command(
        self, response: environments.StopAirflowCommandResponse
    ) -> environments.StopAirflowCommandResponse:
        """Post-rpc interceptor for stop_airflow_command

        DEPRECATED. Please use the `post_stop_airflow_command_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Environments server but before
        it is returned to user code. This `post_stop_airflow_command` interceptor runs
        before the `post_stop_airflow_command_with_metadata` interceptor.
        """
        return response

    def post_stop_airflow_command_with_metadata(
        self,
        response: environments.StopAirflowCommandResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.StopAirflowCommandResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for stop_airflow_command

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Environments server but before it is returned to user code.

        We recommend only using this `post_stop_airflow_command_with_metadata`
        interceptor in new development instead of the `post_stop_airflow_command` interceptor.
        When both interceptors are used, this `post_stop_airflow_command_with_metadata` interceptor runs after the
        `post_stop_airflow_command` interceptor. The (possibly modified) response returned by
        `post_stop_airflow_command` will be passed to
        `post_stop_airflow_command_with_metadata`.
        """
        return response, metadata

    def pre_update_environment(
        self,
        request: environments.UpdateEnvironmentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.UpdateEnvironmentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_environment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Environments server.
        """
        return request, metadata

    def post_update_environment(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_environment

        DEPRECATED. Please use the `post_update_environment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Environments server but before
        it is returned to user code. This `post_update_environment` interceptor runs
        before the `post_update_environment_with_metadata` interceptor.
        """
        return response

    def post_update_environment_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_environment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Environments server but before it is returned to user code.

        We recommend only using this `post_update_environment_with_metadata`
        interceptor in new development instead of the `post_update_environment` interceptor.
        When both interceptors are used, this `post_update_environment_with_metadata` interceptor runs after the
        `post_update_environment` interceptor. The (possibly modified) response returned by
        `post_update_environment` will be passed to
        `post_update_environment_with_metadata`.
        """
        return response, metadata

    def pre_update_user_workloads_config_map(
        self,
        request: environments.UpdateUserWorkloadsConfigMapRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.UpdateUserWorkloadsConfigMapRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_user_workloads_config_map

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Environments server.
        """
        return request, metadata

    def post_update_user_workloads_config_map(
        self, response: environments.UserWorkloadsConfigMap
    ) -> environments.UserWorkloadsConfigMap:
        """Post-rpc interceptor for update_user_workloads_config_map

        DEPRECATED. Please use the `post_update_user_workloads_config_map_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Environments server but before
        it is returned to user code. This `post_update_user_workloads_config_map` interceptor runs
        before the `post_update_user_workloads_config_map_with_metadata` interceptor.
        """
        return response

    def post_update_user_workloads_config_map_with_metadata(
        self,
        response: environments.UserWorkloadsConfigMap,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.UserWorkloadsConfigMap, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_user_workloads_config_map

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Environments server but before it is returned to user code.

        We recommend only using this `post_update_user_workloads_config_map_with_metadata`
        interceptor in new development instead of the `post_update_user_workloads_config_map` interceptor.
        When both interceptors are used, this `post_update_user_workloads_config_map_with_metadata` interceptor runs after the
        `post_update_user_workloads_config_map` interceptor. The (possibly modified) response returned by
        `post_update_user_workloads_config_map` will be passed to
        `post_update_user_workloads_config_map_with_metadata`.
        """
        return response, metadata

    def pre_update_user_workloads_secret(
        self,
        request: environments.UpdateUserWorkloadsSecretRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.UpdateUserWorkloadsSecretRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_user_workloads_secret

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Environments server.
        """
        return request, metadata

    def post_update_user_workloads_secret(
        self, response: environments.UserWorkloadsSecret
    ) -> environments.UserWorkloadsSecret:
        """Post-rpc interceptor for update_user_workloads_secret

        DEPRECATED. Please use the `post_update_user_workloads_secret_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Environments server but before
        it is returned to user code. This `post_update_user_workloads_secret` interceptor runs
        before the `post_update_user_workloads_secret_with_metadata` interceptor.
        """
        return response

    def post_update_user_workloads_secret_with_metadata(
        self,
        response: environments.UserWorkloadsSecret,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        environments.UserWorkloadsSecret, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_user_workloads_secret

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Environments server but before it is returned to user code.

        We recommend only using this `post_update_user_workloads_secret_with_metadata`
        interceptor in new development instead of the `post_update_user_workloads_secret` interceptor.
        When both interceptors are used, this `post_update_user_workloads_secret_with_metadata` interceptor runs after the
        `post_update_user_workloads_secret` interceptor. The (possibly modified) response returned by
        `post_update_user_workloads_secret` will be passed to
        `post_update_user_workloads_secret_with_metadata`.
        """
        return response, metadata

    def pre_delete_operation(
        self,
        request: operations_pb2.DeleteOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.DeleteOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Environments server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the Environments server but before
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
        before they are sent to the Environments server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the Environments server but before
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
        before they are sent to the Environments server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the Environments server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class EnvironmentsRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: EnvironmentsRestInterceptor


class EnvironmentsRestTransport(_BaseEnvironmentsRestTransport):
    """REST backend synchronous transport for Environments.

    Managed Apache Airflow Environments.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "composer.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[EnvironmentsRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'composer.googleapis.com').
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
            interceptor (Optional[EnvironmentsRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or EnvironmentsRestInterceptor()
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

    class _CheckUpgrade(
        _BaseEnvironmentsRestTransport._BaseCheckUpgrade, EnvironmentsRestStub
    ):
        def __hash__(self):
            return hash("EnvironmentsRestTransport.CheckUpgrade")

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
            request: environments.CheckUpgradeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the check upgrade method over HTTP.

            Args:
                request (~.environments.CheckUpgradeRequest):
                    The request object. Request to check whether image
                upgrade will succeed.
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
                _BaseEnvironmentsRestTransport._BaseCheckUpgrade._get_http_options()
            )
            request, metadata = self._interceptor.pre_check_upgrade(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnvironmentsRestTransport._BaseCheckUpgrade,
                    "_BaseCheckUpgrade__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.CheckUpgrade",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "CheckUpgrade",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EnvironmentsRestTransport._CheckUpgrade._get_response(
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

            resp = self._interceptor.post_check_upgrade(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_check_upgrade_with_metadata(
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
                    "Received response for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.check_upgrade",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "CheckUpgrade",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateEnvironment(
        _BaseEnvironmentsRestTransport._BaseCreateEnvironment, EnvironmentsRestStub
    ):
        def __hash__(self):
            return hash("EnvironmentsRestTransport.CreateEnvironment")

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
            request: environments.CreateEnvironmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create environment method over HTTP.

            Args:
                request (~.environments.CreateEnvironmentRequest):
                    The request object. Create a new environment.
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

            http_options = _BaseEnvironmentsRestTransport._BaseCreateEnvironment._get_http_options()
            request, metadata = self._interceptor.pre_create_environment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnvironmentsRestTransport._BaseCreateEnvironment,
                    "_BaseCreateEnvironment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.CreateEnvironment",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "CreateEnvironment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EnvironmentsRestTransport._CreateEnvironment._get_response(
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

            resp = self._interceptor.post_create_environment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_environment_with_metadata(
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
                    "Received response for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.create_environment",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "CreateEnvironment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateUserWorkloadsConfigMap(
        _BaseEnvironmentsRestTransport._BaseCreateUserWorkloadsConfigMap,
        EnvironmentsRestStub,
    ):
        def __hash__(self):
            return hash("EnvironmentsRestTransport.CreateUserWorkloadsConfigMap")

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
            request: environments.CreateUserWorkloadsConfigMapRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> environments.UserWorkloadsConfigMap:
            r"""Call the create user workloads
            config map method over HTTP.

                Args:
                    request (~.environments.CreateUserWorkloadsConfigMapRequest):
                        The request object. Create user workloads ConfigMap
                    request.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.environments.UserWorkloadsConfigMap:
                        User workloads ConfigMap used by
                    Airflow tasks that run with Kubernetes
                    executor or KubernetesPodOperator.

            """

            http_options = _BaseEnvironmentsRestTransport._BaseCreateUserWorkloadsConfigMap._get_http_options()
            request, metadata = self._interceptor.pre_create_user_workloads_config_map(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnvironmentsRestTransport._BaseCreateUserWorkloadsConfigMap,
                    "_BaseCreateUserWorkloadsConfigMap__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.CreateUserWorkloadsConfigMap",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "CreateUserWorkloadsConfigMap",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                EnvironmentsRestTransport._CreateUserWorkloadsConfigMap._get_response(
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
            resp = environments.UserWorkloadsConfigMap()
            pb_resp = environments.UserWorkloadsConfigMap.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_user_workloads_config_map(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_user_workloads_config_map_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = environments.UserWorkloadsConfigMap.to_json(
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
                    "Received response for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.create_user_workloads_config_map",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "CreateUserWorkloadsConfigMap",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateUserWorkloadsSecret(
        _BaseEnvironmentsRestTransport._BaseCreateUserWorkloadsSecret,
        EnvironmentsRestStub,
    ):
        def __hash__(self):
            return hash("EnvironmentsRestTransport.CreateUserWorkloadsSecret")

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
            request: environments.CreateUserWorkloadsSecretRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> environments.UserWorkloadsSecret:
            r"""Call the create user workloads
            secret method over HTTP.

                Args:
                    request (~.environments.CreateUserWorkloadsSecretRequest):
                        The request object. Create user workloads Secret request.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.environments.UserWorkloadsSecret:
                        User workloads Secret used by Airflow
                    tasks that run with Kubernetes executor
                    or KubernetesPodOperator.

            """

            http_options = _BaseEnvironmentsRestTransport._BaseCreateUserWorkloadsSecret._get_http_options()
            request, metadata = self._interceptor.pre_create_user_workloads_secret(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnvironmentsRestTransport._BaseCreateUserWorkloadsSecret,
                    "_BaseCreateUserWorkloadsSecret__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.CreateUserWorkloadsSecret",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "CreateUserWorkloadsSecret",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                EnvironmentsRestTransport._CreateUserWorkloadsSecret._get_response(
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
            resp = environments.UserWorkloadsSecret()
            pb_resp = environments.UserWorkloadsSecret.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_user_workloads_secret(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_user_workloads_secret_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = environments.UserWorkloadsSecret.to_json(
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
                    "Received response for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.create_user_workloads_secret",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "CreateUserWorkloadsSecret",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DatabaseFailover(
        _BaseEnvironmentsRestTransport._BaseDatabaseFailover, EnvironmentsRestStub
    ):
        def __hash__(self):
            return hash("EnvironmentsRestTransport.DatabaseFailover")

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
            request: environments.DatabaseFailoverRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the database failover method over HTTP.

            Args:
                request (~.environments.DatabaseFailoverRequest):
                    The request object. Request to trigger database failover
                (only for highly resilient
                environments).
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
                _BaseEnvironmentsRestTransport._BaseDatabaseFailover._get_http_options()
            )
            request, metadata = self._interceptor.pre_database_failover(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnvironmentsRestTransport._BaseDatabaseFailover,
                    "_BaseDatabaseFailover__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.DatabaseFailover",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "DatabaseFailover",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EnvironmentsRestTransport._DatabaseFailover._get_response(
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

            resp = self._interceptor.post_database_failover(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_database_failover_with_metadata(
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
                    "Received response for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.database_failover",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "DatabaseFailover",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteEnvironment(
        _BaseEnvironmentsRestTransport._BaseDeleteEnvironment, EnvironmentsRestStub
    ):
        def __hash__(self):
            return hash("EnvironmentsRestTransport.DeleteEnvironment")

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
            request: environments.DeleteEnvironmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete environment method over HTTP.

            Args:
                request (~.environments.DeleteEnvironmentRequest):
                    The request object. Delete an environment.
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

            http_options = _BaseEnvironmentsRestTransport._BaseDeleteEnvironment._get_http_options()
            request, metadata = self._interceptor.pre_delete_environment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnvironmentsRestTransport._BaseDeleteEnvironment,
                    "_BaseDeleteEnvironment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.DeleteEnvironment",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "DeleteEnvironment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EnvironmentsRestTransport._DeleteEnvironment._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_environment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_environment_with_metadata(
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
                    "Received response for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.delete_environment",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "DeleteEnvironment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteUserWorkloadsConfigMap(
        _BaseEnvironmentsRestTransport._BaseDeleteUserWorkloadsConfigMap,
        EnvironmentsRestStub,
    ):
        def __hash__(self):
            return hash("EnvironmentsRestTransport.DeleteUserWorkloadsConfigMap")

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
            request: environments.DeleteUserWorkloadsConfigMapRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete user workloads
            config map method over HTTP.

                Args:
                    request (~.environments.DeleteUserWorkloadsConfigMapRequest):
                        The request object. Delete user workloads ConfigMap
                    request.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.
            """

            http_options = _BaseEnvironmentsRestTransport._BaseDeleteUserWorkloadsConfigMap._get_http_options()
            request, metadata = self._interceptor.pre_delete_user_workloads_config_map(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnvironmentsRestTransport._BaseDeleteUserWorkloadsConfigMap,
                    "_BaseDeleteUserWorkloadsConfigMap__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.DeleteUserWorkloadsConfigMap",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "DeleteUserWorkloadsConfigMap",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                EnvironmentsRestTransport._DeleteUserWorkloadsConfigMap._get_response(
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

    class _DeleteUserWorkloadsSecret(
        _BaseEnvironmentsRestTransport._BaseDeleteUserWorkloadsSecret,
        EnvironmentsRestStub,
    ):
        def __hash__(self):
            return hash("EnvironmentsRestTransport.DeleteUserWorkloadsSecret")

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
            request: environments.DeleteUserWorkloadsSecretRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete user workloads
            secret method over HTTP.

                Args:
                    request (~.environments.DeleteUserWorkloadsSecretRequest):
                        The request object. Delete user workloads Secret request.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.
            """

            http_options = _BaseEnvironmentsRestTransport._BaseDeleteUserWorkloadsSecret._get_http_options()
            request, metadata = self._interceptor.pre_delete_user_workloads_secret(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnvironmentsRestTransport._BaseDeleteUserWorkloadsSecret,
                    "_BaseDeleteUserWorkloadsSecret__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.DeleteUserWorkloadsSecret",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "DeleteUserWorkloadsSecret",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                EnvironmentsRestTransport._DeleteUserWorkloadsSecret._get_response(
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

    class _ExecuteAirflowCommand(
        _BaseEnvironmentsRestTransport._BaseExecuteAirflowCommand, EnvironmentsRestStub
    ):
        def __hash__(self):
            return hash("EnvironmentsRestTransport.ExecuteAirflowCommand")

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
            request: environments.ExecuteAirflowCommandRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> environments.ExecuteAirflowCommandResponse:
            r"""Call the execute airflow command method over HTTP.

            Args:
                request (~.environments.ExecuteAirflowCommandRequest):
                    The request object. Execute Airflow Command request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.environments.ExecuteAirflowCommandResponse:
                    Response to
                ExecuteAirflowCommandRequest.

            """

            http_options = _BaseEnvironmentsRestTransport._BaseExecuteAirflowCommand._get_http_options()
            request, metadata = self._interceptor.pre_execute_airflow_command(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnvironmentsRestTransport._BaseExecuteAirflowCommand,
                    "_BaseExecuteAirflowCommand__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.ExecuteAirflowCommand",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "ExecuteAirflowCommand",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EnvironmentsRestTransport._ExecuteAirflowCommand._get_response(
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
            resp = environments.ExecuteAirflowCommandResponse()
            pb_resp = environments.ExecuteAirflowCommandResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_execute_airflow_command(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_execute_airflow_command_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        environments.ExecuteAirflowCommandResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.execute_airflow_command",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "ExecuteAirflowCommand",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchDatabaseProperties(
        _BaseEnvironmentsRestTransport._BaseFetchDatabaseProperties,
        EnvironmentsRestStub,
    ):
        def __hash__(self):
            return hash("EnvironmentsRestTransport.FetchDatabaseProperties")

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
            request: environments.FetchDatabasePropertiesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> environments.FetchDatabasePropertiesResponse:
            r"""Call the fetch database properties method over HTTP.

            Args:
                request (~.environments.FetchDatabasePropertiesRequest):
                    The request object. Request to fetch properties of
                environment's database.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.environments.FetchDatabasePropertiesResponse:
                    Response for
                FetchDatabasePropertiesRequest.

            """

            http_options = _BaseEnvironmentsRestTransport._BaseFetchDatabaseProperties._get_http_options()
            request, metadata = self._interceptor.pre_fetch_database_properties(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnvironmentsRestTransport._BaseFetchDatabaseProperties,
                    "_BaseFetchDatabaseProperties__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.FetchDatabaseProperties",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "FetchDatabaseProperties",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EnvironmentsRestTransport._FetchDatabaseProperties._get_response(
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
            resp = environments.FetchDatabasePropertiesResponse()
            pb_resp = environments.FetchDatabasePropertiesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_database_properties(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fetch_database_properties_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        environments.FetchDatabasePropertiesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.fetch_database_properties",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "FetchDatabaseProperties",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetEnvironment(
        _BaseEnvironmentsRestTransport._BaseGetEnvironment, EnvironmentsRestStub
    ):
        def __hash__(self):
            return hash("EnvironmentsRestTransport.GetEnvironment")

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
            request: environments.GetEnvironmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> environments.Environment:
            r"""Call the get environment method over HTTP.

            Args:
                request (~.environments.GetEnvironmentRequest):
                    The request object. Get an environment.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.environments.Environment:
                    An environment for running
                orchestration tasks.

            """

            http_options = (
                _BaseEnvironmentsRestTransport._BaseGetEnvironment._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_environment(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnvironmentsRestTransport._BaseGetEnvironment,
                    "_BaseGetEnvironment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.GetEnvironment",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "GetEnvironment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EnvironmentsRestTransport._GetEnvironment._get_response(
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
            resp = environments.Environment()
            pb_resp = environments.Environment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_environment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_environment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = environments.Environment.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.get_environment",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "GetEnvironment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetUserWorkloadsConfigMap(
        _BaseEnvironmentsRestTransport._BaseGetUserWorkloadsConfigMap,
        EnvironmentsRestStub,
    ):
        def __hash__(self):
            return hash("EnvironmentsRestTransport.GetUserWorkloadsConfigMap")

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
            request: environments.GetUserWorkloadsConfigMapRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> environments.UserWorkloadsConfigMap:
            r"""Call the get user workloads config
            map method over HTTP.

                Args:
                    request (~.environments.GetUserWorkloadsConfigMapRequest):
                        The request object. Get user workloads ConfigMap request.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.environments.UserWorkloadsConfigMap:
                        User workloads ConfigMap used by
                    Airflow tasks that run with Kubernetes
                    executor or KubernetesPodOperator.

            """

            http_options = _BaseEnvironmentsRestTransport._BaseGetUserWorkloadsConfigMap._get_http_options()
            request, metadata = self._interceptor.pre_get_user_workloads_config_map(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnvironmentsRestTransport._BaseGetUserWorkloadsConfigMap,
                    "_BaseGetUserWorkloadsConfigMap__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.GetUserWorkloadsConfigMap",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "GetUserWorkloadsConfigMap",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                EnvironmentsRestTransport._GetUserWorkloadsConfigMap._get_response(
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
            resp = environments.UserWorkloadsConfigMap()
            pb_resp = environments.UserWorkloadsConfigMap.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_user_workloads_config_map(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_user_workloads_config_map_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = environments.UserWorkloadsConfigMap.to_json(
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
                    "Received response for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.get_user_workloads_config_map",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "GetUserWorkloadsConfigMap",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetUserWorkloadsSecret(
        _BaseEnvironmentsRestTransport._BaseGetUserWorkloadsSecret, EnvironmentsRestStub
    ):
        def __hash__(self):
            return hash("EnvironmentsRestTransport.GetUserWorkloadsSecret")

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
            request: environments.GetUserWorkloadsSecretRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> environments.UserWorkloadsSecret:
            r"""Call the get user workloads secret method over HTTP.

            Args:
                request (~.environments.GetUserWorkloadsSecretRequest):
                    The request object. Get user workloads Secret request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.environments.UserWorkloadsSecret:
                    User workloads Secret used by Airflow
                tasks that run with Kubernetes executor
                or KubernetesPodOperator.

            """

            http_options = _BaseEnvironmentsRestTransport._BaseGetUserWorkloadsSecret._get_http_options()
            request, metadata = self._interceptor.pre_get_user_workloads_secret(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnvironmentsRestTransport._BaseGetUserWorkloadsSecret,
                    "_BaseGetUserWorkloadsSecret__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.GetUserWorkloadsSecret",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "GetUserWorkloadsSecret",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EnvironmentsRestTransport._GetUserWorkloadsSecret._get_response(
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
            resp = environments.UserWorkloadsSecret()
            pb_resp = environments.UserWorkloadsSecret.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_user_workloads_secret(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_user_workloads_secret_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = environments.UserWorkloadsSecret.to_json(
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
                    "Received response for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.get_user_workloads_secret",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "GetUserWorkloadsSecret",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListEnvironments(
        _BaseEnvironmentsRestTransport._BaseListEnvironments, EnvironmentsRestStub
    ):
        def __hash__(self):
            return hash("EnvironmentsRestTransport.ListEnvironments")

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
            request: environments.ListEnvironmentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> environments.ListEnvironmentsResponse:
            r"""Call the list environments method over HTTP.

            Args:
                request (~.environments.ListEnvironmentsRequest):
                    The request object. List environments in a project and
                location.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.environments.ListEnvironmentsResponse:
                    The environments in a project and
                location.

            """

            http_options = (
                _BaseEnvironmentsRestTransport._BaseListEnvironments._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_environments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnvironmentsRestTransport._BaseListEnvironments,
                    "_BaseListEnvironments__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.ListEnvironments",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "ListEnvironments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EnvironmentsRestTransport._ListEnvironments._get_response(
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
            resp = environments.ListEnvironmentsResponse()
            pb_resp = environments.ListEnvironmentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_environments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_environments_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = environments.ListEnvironmentsResponse.to_json(
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
                    "Received response for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.list_environments",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "ListEnvironments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListUserWorkloadsConfigMaps(
        _BaseEnvironmentsRestTransport._BaseListUserWorkloadsConfigMaps,
        EnvironmentsRestStub,
    ):
        def __hash__(self):
            return hash("EnvironmentsRestTransport.ListUserWorkloadsConfigMaps")

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
            request: environments.ListUserWorkloadsConfigMapsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> environments.ListUserWorkloadsConfigMapsResponse:
            r"""Call the list user workloads
            config maps method over HTTP.

                Args:
                    request (~.environments.ListUserWorkloadsConfigMapsRequest):
                        The request object. List user workloads ConfigMaps
                    request.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.environments.ListUserWorkloadsConfigMapsResponse:
                        The user workloads ConfigMaps for a
                    given environment.

            """

            http_options = _BaseEnvironmentsRestTransport._BaseListUserWorkloadsConfigMaps._get_http_options()
            request, metadata = self._interceptor.pre_list_user_workloads_config_maps(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnvironmentsRestTransport._BaseListUserWorkloadsConfigMaps,
                    "_BaseListUserWorkloadsConfigMaps__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.ListUserWorkloadsConfigMaps",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "ListUserWorkloadsConfigMaps",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                EnvironmentsRestTransport._ListUserWorkloadsConfigMaps._get_response(
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
            resp = environments.ListUserWorkloadsConfigMapsResponse()
            pb_resp = environments.ListUserWorkloadsConfigMapsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_user_workloads_config_maps(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_user_workloads_config_maps_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        environments.ListUserWorkloadsConfigMapsResponse.to_json(
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
                    "Received response for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.list_user_workloads_config_maps",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "ListUserWorkloadsConfigMaps",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListUserWorkloadsSecrets(
        _BaseEnvironmentsRestTransport._BaseListUserWorkloadsSecrets,
        EnvironmentsRestStub,
    ):
        def __hash__(self):
            return hash("EnvironmentsRestTransport.ListUserWorkloadsSecrets")

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
            request: environments.ListUserWorkloadsSecretsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> environments.ListUserWorkloadsSecretsResponse:
            r"""Call the list user workloads
            secrets method over HTTP.

                Args:
                    request (~.environments.ListUserWorkloadsSecretsRequest):
                        The request object. List user workloads Secrets request.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.environments.ListUserWorkloadsSecretsResponse:
                        The user workloads Secrets for a
                    given environment.

            """

            http_options = _BaseEnvironmentsRestTransport._BaseListUserWorkloadsSecrets._get_http_options()
            request, metadata = self._interceptor.pre_list_user_workloads_secrets(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnvironmentsRestTransport._BaseListUserWorkloadsSecrets,
                    "_BaseListUserWorkloadsSecrets__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.ListUserWorkloadsSecrets",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "ListUserWorkloadsSecrets",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                EnvironmentsRestTransport._ListUserWorkloadsSecrets._get_response(
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
            resp = environments.ListUserWorkloadsSecretsResponse()
            pb_resp = environments.ListUserWorkloadsSecretsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_user_workloads_secrets(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_user_workloads_secrets_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        environments.ListUserWorkloadsSecretsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.list_user_workloads_secrets",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "ListUserWorkloadsSecrets",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListWorkloads(
        _BaseEnvironmentsRestTransport._BaseListWorkloads, EnvironmentsRestStub
    ):
        def __hash__(self):
            return hash("EnvironmentsRestTransport.ListWorkloads")

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
            request: environments.ListWorkloadsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> environments.ListWorkloadsResponse:
            r"""Call the list workloads method over HTTP.

            Args:
                request (~.environments.ListWorkloadsRequest):
                    The request object. Request for listing workloads in a
                Cloud Composer environment.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.environments.ListWorkloadsResponse:
                    Response to ListWorkloadsRequest.
            """

            http_options = (
                _BaseEnvironmentsRestTransport._BaseListWorkloads._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_workloads(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnvironmentsRestTransport._BaseListWorkloads,
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
                    f"Sending request for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.ListWorkloads",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "ListWorkloads",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EnvironmentsRestTransport._ListWorkloads._get_response(
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
            resp = environments.ListWorkloadsResponse()
            pb_resp = environments.ListWorkloadsResponse.pb(resp)

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
                    response_payload = environments.ListWorkloadsResponse.to_json(
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
                    "Received response for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.list_workloads",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "ListWorkloads",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _LoadSnapshot(
        _BaseEnvironmentsRestTransport._BaseLoadSnapshot, EnvironmentsRestStub
    ):
        def __hash__(self):
            return hash("EnvironmentsRestTransport.LoadSnapshot")

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
            request: environments.LoadSnapshotRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the load snapshot method over HTTP.

            Args:
                request (~.environments.LoadSnapshotRequest):
                    The request object. Request to load a snapshot into a
                Cloud Composer environment.
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
                _BaseEnvironmentsRestTransport._BaseLoadSnapshot._get_http_options()
            )
            request, metadata = self._interceptor.pre_load_snapshot(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnvironmentsRestTransport._BaseLoadSnapshot,
                    "_BaseLoadSnapshot__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.LoadSnapshot",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "LoadSnapshot",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EnvironmentsRestTransport._LoadSnapshot._get_response(
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

            resp = self._interceptor.post_load_snapshot(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_load_snapshot_with_metadata(
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
                    "Received response for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.load_snapshot",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "LoadSnapshot",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _PollAirflowCommand(
        _BaseEnvironmentsRestTransport._BasePollAirflowCommand, EnvironmentsRestStub
    ):
        def __hash__(self):
            return hash("EnvironmentsRestTransport.PollAirflowCommand")

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
            request: environments.PollAirflowCommandRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> environments.PollAirflowCommandResponse:
            r"""Call the poll airflow command method over HTTP.

            Args:
                request (~.environments.PollAirflowCommandRequest):
                    The request object. Poll Airflow Command request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.environments.PollAirflowCommandResponse:
                    Response to
                PollAirflowCommandRequest.

            """

            http_options = _BaseEnvironmentsRestTransport._BasePollAirflowCommand._get_http_options()
            request, metadata = self._interceptor.pre_poll_airflow_command(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnvironmentsRestTransport._BasePollAirflowCommand,
                    "_BasePollAirflowCommand__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.PollAirflowCommand",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "PollAirflowCommand",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EnvironmentsRestTransport._PollAirflowCommand._get_response(
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
            resp = environments.PollAirflowCommandResponse()
            pb_resp = environments.PollAirflowCommandResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_poll_airflow_command(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_poll_airflow_command_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = environments.PollAirflowCommandResponse.to_json(
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
                    "Received response for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.poll_airflow_command",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "PollAirflowCommand",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SaveSnapshot(
        _BaseEnvironmentsRestTransport._BaseSaveSnapshot, EnvironmentsRestStub
    ):
        def __hash__(self):
            return hash("EnvironmentsRestTransport.SaveSnapshot")

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
            request: environments.SaveSnapshotRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the save snapshot method over HTTP.

            Args:
                request (~.environments.SaveSnapshotRequest):
                    The request object. Request to create a snapshot of a
                Cloud Composer environment.
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
                _BaseEnvironmentsRestTransport._BaseSaveSnapshot._get_http_options()
            )
            request, metadata = self._interceptor.pre_save_snapshot(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnvironmentsRestTransport._BaseSaveSnapshot,
                    "_BaseSaveSnapshot__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.SaveSnapshot",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "SaveSnapshot",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EnvironmentsRestTransport._SaveSnapshot._get_response(
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

            resp = self._interceptor.post_save_snapshot(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_save_snapshot_with_metadata(
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
                    "Received response for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.save_snapshot",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "SaveSnapshot",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _StopAirflowCommand(
        _BaseEnvironmentsRestTransport._BaseStopAirflowCommand, EnvironmentsRestStub
    ):
        def __hash__(self):
            return hash("EnvironmentsRestTransport.StopAirflowCommand")

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
            request: environments.StopAirflowCommandRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> environments.StopAirflowCommandResponse:
            r"""Call the stop airflow command method over HTTP.

            Args:
                request (~.environments.StopAirflowCommandRequest):
                    The request object. Stop Airflow Command request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.environments.StopAirflowCommandResponse:
                    Response to
                StopAirflowCommandRequest.

            """

            http_options = _BaseEnvironmentsRestTransport._BaseStopAirflowCommand._get_http_options()
            request, metadata = self._interceptor.pre_stop_airflow_command(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnvironmentsRestTransport._BaseStopAirflowCommand,
                    "_BaseStopAirflowCommand__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.StopAirflowCommand",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "StopAirflowCommand",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EnvironmentsRestTransport._StopAirflowCommand._get_response(
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
            resp = environments.StopAirflowCommandResponse()
            pb_resp = environments.StopAirflowCommandResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_stop_airflow_command(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_stop_airflow_command_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = environments.StopAirflowCommandResponse.to_json(
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
                    "Received response for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.stop_airflow_command",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "StopAirflowCommand",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateEnvironment(
        _BaseEnvironmentsRestTransport._BaseUpdateEnvironment, EnvironmentsRestStub
    ):
        def __hash__(self):
            return hash("EnvironmentsRestTransport.UpdateEnvironment")

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
            request: environments.UpdateEnvironmentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update environment method over HTTP.

            Args:
                request (~.environments.UpdateEnvironmentRequest):
                    The request object. Update an environment.
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

            http_options = _BaseEnvironmentsRestTransport._BaseUpdateEnvironment._get_http_options()
            request, metadata = self._interceptor.pre_update_environment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnvironmentsRestTransport._BaseUpdateEnvironment,
                    "_BaseUpdateEnvironment__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.UpdateEnvironment",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "UpdateEnvironment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EnvironmentsRestTransport._UpdateEnvironment._get_response(
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

            resp = self._interceptor.post_update_environment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_environment_with_metadata(
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
                    "Received response for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.update_environment",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "UpdateEnvironment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateUserWorkloadsConfigMap(
        _BaseEnvironmentsRestTransport._BaseUpdateUserWorkloadsConfigMap,
        EnvironmentsRestStub,
    ):
        def __hash__(self):
            return hash("EnvironmentsRestTransport.UpdateUserWorkloadsConfigMap")

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
            request: environments.UpdateUserWorkloadsConfigMapRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> environments.UserWorkloadsConfigMap:
            r"""Call the update user workloads
            config map method over HTTP.

                Args:
                    request (~.environments.UpdateUserWorkloadsConfigMapRequest):
                        The request object. Update user workloads ConfigMap
                    request.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.environments.UserWorkloadsConfigMap:
                        User workloads ConfigMap used by
                    Airflow tasks that run with Kubernetes
                    executor or KubernetesPodOperator.

            """

            http_options = _BaseEnvironmentsRestTransport._BaseUpdateUserWorkloadsConfigMap._get_http_options()
            request, metadata = self._interceptor.pre_update_user_workloads_config_map(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnvironmentsRestTransport._BaseUpdateUserWorkloadsConfigMap,
                    "_BaseUpdateUserWorkloadsConfigMap__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.UpdateUserWorkloadsConfigMap",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "UpdateUserWorkloadsConfigMap",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                EnvironmentsRestTransport._UpdateUserWorkloadsConfigMap._get_response(
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
            resp = environments.UserWorkloadsConfigMap()
            pb_resp = environments.UserWorkloadsConfigMap.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_user_workloads_config_map(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_user_workloads_config_map_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = environments.UserWorkloadsConfigMap.to_json(
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
                    "Received response for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.update_user_workloads_config_map",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "UpdateUserWorkloadsConfigMap",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateUserWorkloadsSecret(
        _BaseEnvironmentsRestTransport._BaseUpdateUserWorkloadsSecret,
        EnvironmentsRestStub,
    ):
        def __hash__(self):
            return hash("EnvironmentsRestTransport.UpdateUserWorkloadsSecret")

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
            request: environments.UpdateUserWorkloadsSecretRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> environments.UserWorkloadsSecret:
            r"""Call the update user workloads
            secret method over HTTP.

                Args:
                    request (~.environments.UpdateUserWorkloadsSecretRequest):
                        The request object. Update user workloads Secret request.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.environments.UserWorkloadsSecret:
                        User workloads Secret used by Airflow
                    tasks that run with Kubernetes executor
                    or KubernetesPodOperator.

            """

            http_options = _BaseEnvironmentsRestTransport._BaseUpdateUserWorkloadsSecret._get_http_options()
            request, metadata = self._interceptor.pre_update_user_workloads_secret(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnvironmentsRestTransport._BaseUpdateUserWorkloadsSecret,
                    "_BaseUpdateUserWorkloadsSecret__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.UpdateUserWorkloadsSecret",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "UpdateUserWorkloadsSecret",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                EnvironmentsRestTransport._UpdateUserWorkloadsSecret._get_response(
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
            resp = environments.UserWorkloadsSecret()
            pb_resp = environments.UserWorkloadsSecret.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_user_workloads_secret(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_user_workloads_secret_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = environments.UserWorkloadsSecret.to_json(
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
                    "Received response for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.update_user_workloads_secret",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "UpdateUserWorkloadsSecret",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def check_upgrade(
        self,
    ) -> Callable[[environments.CheckUpgradeRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CheckUpgrade(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_environment(
        self,
    ) -> Callable[[environments.CreateEnvironmentRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateEnvironment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_user_workloads_config_map(
        self,
    ) -> Callable[
        [environments.CreateUserWorkloadsConfigMapRequest],
        environments.UserWorkloadsConfigMap,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateUserWorkloadsConfigMap(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_user_workloads_secret(
        self,
    ) -> Callable[
        [environments.CreateUserWorkloadsSecretRequest],
        environments.UserWorkloadsSecret,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateUserWorkloadsSecret(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def database_failover(
        self,
    ) -> Callable[[environments.DatabaseFailoverRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DatabaseFailover(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_environment(
        self,
    ) -> Callable[[environments.DeleteEnvironmentRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteEnvironment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_user_workloads_config_map(
        self,
    ) -> Callable[[environments.DeleteUserWorkloadsConfigMapRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteUserWorkloadsConfigMap(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_user_workloads_secret(
        self,
    ) -> Callable[[environments.DeleteUserWorkloadsSecretRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteUserWorkloadsSecret(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def execute_airflow_command(
        self,
    ) -> Callable[
        [environments.ExecuteAirflowCommandRequest],
        environments.ExecuteAirflowCommandResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExecuteAirflowCommand(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def fetch_database_properties(
        self,
    ) -> Callable[
        [environments.FetchDatabasePropertiesRequest],
        environments.FetchDatabasePropertiesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchDatabaseProperties(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_environment(
        self,
    ) -> Callable[[environments.GetEnvironmentRequest], environments.Environment]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetEnvironment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_user_workloads_config_map(
        self,
    ) -> Callable[
        [environments.GetUserWorkloadsConfigMapRequest],
        environments.UserWorkloadsConfigMap,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetUserWorkloadsConfigMap(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_user_workloads_secret(
        self,
    ) -> Callable[
        [environments.GetUserWorkloadsSecretRequest], environments.UserWorkloadsSecret
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetUserWorkloadsSecret(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_environments(
        self,
    ) -> Callable[
        [environments.ListEnvironmentsRequest], environments.ListEnvironmentsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListEnvironments(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_user_workloads_config_maps(
        self,
    ) -> Callable[
        [environments.ListUserWorkloadsConfigMapsRequest],
        environments.ListUserWorkloadsConfigMapsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListUserWorkloadsConfigMaps(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_user_workloads_secrets(
        self,
    ) -> Callable[
        [environments.ListUserWorkloadsSecretsRequest],
        environments.ListUserWorkloadsSecretsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListUserWorkloadsSecrets(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_workloads(
        self,
    ) -> Callable[
        [environments.ListWorkloadsRequest], environments.ListWorkloadsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListWorkloads(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def load_snapshot(
        self,
    ) -> Callable[[environments.LoadSnapshotRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._LoadSnapshot(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def poll_airflow_command(
        self,
    ) -> Callable[
        [environments.PollAirflowCommandRequest],
        environments.PollAirflowCommandResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PollAirflowCommand(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def save_snapshot(
        self,
    ) -> Callable[[environments.SaveSnapshotRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SaveSnapshot(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def stop_airflow_command(
        self,
    ) -> Callable[
        [environments.StopAirflowCommandRequest],
        environments.StopAirflowCommandResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StopAirflowCommand(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_environment(
        self,
    ) -> Callable[[environments.UpdateEnvironmentRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateEnvironment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_user_workloads_config_map(
        self,
    ) -> Callable[
        [environments.UpdateUserWorkloadsConfigMapRequest],
        environments.UserWorkloadsConfigMap,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateUserWorkloadsConfigMap(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_user_workloads_secret(
        self,
    ) -> Callable[
        [environments.UpdateUserWorkloadsSecretRequest],
        environments.UserWorkloadsSecret,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateUserWorkloadsSecret(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_operation(self):
        return self._DeleteOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _DeleteOperation(
        _BaseEnvironmentsRestTransport._BaseDeleteOperation, EnvironmentsRestStub
    ):
        def __hash__(self):
            return hash("EnvironmentsRestTransport.DeleteOperation")

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

            http_options = (
                _BaseEnvironmentsRestTransport._BaseDeleteOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnvironmentsRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EnvironmentsRestTransport._DeleteOperation._get_response(
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
        _BaseEnvironmentsRestTransport._BaseGetOperation, EnvironmentsRestStub
    ):
        def __hash__(self):
            return hash("EnvironmentsRestTransport.GetOperation")

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
                _BaseEnvironmentsRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnvironmentsRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EnvironmentsRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.orchestration.airflow.service_v1.EnvironmentsAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
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
        _BaseEnvironmentsRestTransport._BaseListOperations, EnvironmentsRestStub
    ):
        def __hash__(self):
            return hash("EnvironmentsRestTransport.ListOperations")

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

            http_options = (
                _BaseEnvironmentsRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseEnvironmentsRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.orchestration.airflow.service_v1.EnvironmentsClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = EnvironmentsRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.orchestration.airflow.service_v1.EnvironmentsAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.orchestration.airflow.service.v1.Environments",
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


__all__ = ("EnvironmentsRestTransport",)
