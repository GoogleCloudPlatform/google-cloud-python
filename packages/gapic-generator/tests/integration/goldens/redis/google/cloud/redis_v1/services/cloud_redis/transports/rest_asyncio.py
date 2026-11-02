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

import google.auth
try:
    import aiohttp # type: ignore
    from google.auth.aio.transport.sessions import AsyncAuthorizedSession # type: ignore
    from google.api_core import rest_streaming_async # type: ignore
    from google.api_core.operations_v1 import AsyncOperationsRestClient # type: ignore
except ImportError as e:  # pragma: NO COVER
    raise ImportError("`rest_asyncio` transport requires the library to be installed with the `async_rest` extra. Install the library with the `async_rest` extra using `pip install google-cloud-redis[async_rest]`") from e

from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.aio import credentials as ga_credentials_async  # type: ignore

from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core.client_options import ClientOptions
from google.api_core import operations_v1
from google.cloud.location import locations_pb2 # type: ignore
from google.api_core import retry_async as retries
from google.api_core import rest_helpers
from google.api_core import rest_streaming_async  # type: ignore
from google.cloud.redis_v1._compat import transcode_request, trace_http_request

import google.protobuf

from google.protobuf import json_format
from google.api_core import operations_v1
from google.cloud.location import locations_pb2 # type: ignore

import json  # type: ignore
import dataclasses
from typing import Any, Dict, List, Callable, Tuple, Optional, Sequence, Union


from google.cloud.redis_v1.types import cloud_redis
from google.longrunning import operations_pb2  # type: ignore


from .rest_base import _BaseCloudRedisRestTransport

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO


import logging

try:
    from google.api_core import client_logging  # type: ignore
    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = logging.getLogger(__name__)

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=f"google-auth@{google.auth.__version__}",
)

DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class AsyncCloudRedisRestInterceptor:
    """Asynchronous Interceptor for CloudRedis.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the AsyncCloudRedisRestTransport.

    .. code-block:: python
        class MyCustomCloudRedisInterceptor(CloudRedisRestInterceptor):
            async def pre_create_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_create_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_delete_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_delete_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_export_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_export_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_failover_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_failover_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_get_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_get_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_get_instance_auth_string(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_get_instance_auth_string(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_import_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_import_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_list_instances(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_list_instances(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_reschedule_maintenance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_reschedule_maintenance(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_update_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_update_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            async def pre_upgrade_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            async def post_upgrade_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = AsyncCloudRedisRestTransport(interceptor=MyCustomCloudRedisInterceptor())
        client = async CloudRedisClient(transport=transport)


    """
    async def pre_create_instance(self, request: cloud_redis.CreateInstanceRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[cloud_redis.CreateInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_create_instance(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_instance

        DEPRECATED. Please use the `post_create_instance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code. This `post_create_instance` interceptor runs
        before the `post_create_instance_with_metadata` interceptor.
        """
        return response

    async def post_create_instance_with_metadata(self, response: operations_pb2.Operation, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_instance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudRedis server but before it is returned to user code.

        We recommend only using this `post_create_instance_with_metadata`
        interceptor in new development instead of the `post_create_instance` interceptor.
        When both interceptors are used, this `post_create_instance_with_metadata` interceptor runs after the
        `post_create_instance` interceptor. The (possibly modified) response returned by
        `post_create_instance` will be passed to
        `post_create_instance_with_metadata`.
        """
        return response, metadata

    async def pre_delete_instance(self, request: cloud_redis.DeleteInstanceRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[cloud_redis.DeleteInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_delete_instance(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_instance

        DEPRECATED. Please use the `post_delete_instance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code. This `post_delete_instance` interceptor runs
        before the `post_delete_instance_with_metadata` interceptor.
        """
        return response

    async def post_delete_instance_with_metadata(self, response: operations_pb2.Operation, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_instance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudRedis server but before it is returned to user code.

        We recommend only using this `post_delete_instance_with_metadata`
        interceptor in new development instead of the `post_delete_instance` interceptor.
        When both interceptors are used, this `post_delete_instance_with_metadata` interceptor runs after the
        `post_delete_instance` interceptor. The (possibly modified) response returned by
        `post_delete_instance` will be passed to
        `post_delete_instance_with_metadata`.
        """
        return response, metadata

    async def pre_export_instance(self, request: cloud_redis.ExportInstanceRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[cloud_redis.ExportInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for export_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_export_instance(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for export_instance

        DEPRECATED. Please use the `post_export_instance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code. This `post_export_instance` interceptor runs
        before the `post_export_instance_with_metadata` interceptor.
        """
        return response

    async def post_export_instance_with_metadata(self, response: operations_pb2.Operation, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for export_instance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudRedis server but before it is returned to user code.

        We recommend only using this `post_export_instance_with_metadata`
        interceptor in new development instead of the `post_export_instance` interceptor.
        When both interceptors are used, this `post_export_instance_with_metadata` interceptor runs after the
        `post_export_instance` interceptor. The (possibly modified) response returned by
        `post_export_instance` will be passed to
        `post_export_instance_with_metadata`.
        """
        return response, metadata

    async def pre_failover_instance(self, request: cloud_redis.FailoverInstanceRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[cloud_redis.FailoverInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for failover_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_failover_instance(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for failover_instance

        DEPRECATED. Please use the `post_failover_instance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code. This `post_failover_instance` interceptor runs
        before the `post_failover_instance_with_metadata` interceptor.
        """
        return response

    async def post_failover_instance_with_metadata(self, response: operations_pb2.Operation, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for failover_instance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudRedis server but before it is returned to user code.

        We recommend only using this `post_failover_instance_with_metadata`
        interceptor in new development instead of the `post_failover_instance` interceptor.
        When both interceptors are used, this `post_failover_instance_with_metadata` interceptor runs after the
        `post_failover_instance` interceptor. The (possibly modified) response returned by
        `post_failover_instance` will be passed to
        `post_failover_instance_with_metadata`.
        """
        return response, metadata

    async def pre_get_instance(self, request: cloud_redis.GetInstanceRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[cloud_redis.GetInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_get_instance(self, response: cloud_redis.Instance) -> cloud_redis.Instance:
        """Post-rpc interceptor for get_instance

        DEPRECATED. Please use the `post_get_instance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code. This `post_get_instance` interceptor runs
        before the `post_get_instance_with_metadata` interceptor.
        """
        return response

    async def post_get_instance_with_metadata(self, response: cloud_redis.Instance, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[cloud_redis.Instance, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_instance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudRedis server but before it is returned to user code.

        We recommend only using this `post_get_instance_with_metadata`
        interceptor in new development instead of the `post_get_instance` interceptor.
        When both interceptors are used, this `post_get_instance_with_metadata` interceptor runs after the
        `post_get_instance` interceptor. The (possibly modified) response returned by
        `post_get_instance` will be passed to
        `post_get_instance_with_metadata`.
        """
        return response, metadata

    async def pre_get_instance_auth_string(self, request: cloud_redis.GetInstanceAuthStringRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[cloud_redis.GetInstanceAuthStringRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_instance_auth_string

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_get_instance_auth_string(self, response: cloud_redis.InstanceAuthString) -> cloud_redis.InstanceAuthString:
        """Post-rpc interceptor for get_instance_auth_string

        DEPRECATED. Please use the `post_get_instance_auth_string_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code. This `post_get_instance_auth_string` interceptor runs
        before the `post_get_instance_auth_string_with_metadata` interceptor.
        """
        return response

    async def post_get_instance_auth_string_with_metadata(self, response: cloud_redis.InstanceAuthString, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[cloud_redis.InstanceAuthString, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_instance_auth_string

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudRedis server but before it is returned to user code.

        We recommend only using this `post_get_instance_auth_string_with_metadata`
        interceptor in new development instead of the `post_get_instance_auth_string` interceptor.
        When both interceptors are used, this `post_get_instance_auth_string_with_metadata` interceptor runs after the
        `post_get_instance_auth_string` interceptor. The (possibly modified) response returned by
        `post_get_instance_auth_string` will be passed to
        `post_get_instance_auth_string_with_metadata`.
        """
        return response, metadata

    async def pre_import_instance(self, request: cloud_redis.ImportInstanceRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[cloud_redis.ImportInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for import_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_import_instance(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for import_instance

        DEPRECATED. Please use the `post_import_instance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code. This `post_import_instance` interceptor runs
        before the `post_import_instance_with_metadata` interceptor.
        """
        return response

    async def post_import_instance_with_metadata(self, response: operations_pb2.Operation, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for import_instance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudRedis server but before it is returned to user code.

        We recommend only using this `post_import_instance_with_metadata`
        interceptor in new development instead of the `post_import_instance` interceptor.
        When both interceptors are used, this `post_import_instance_with_metadata` interceptor runs after the
        `post_import_instance` interceptor. The (possibly modified) response returned by
        `post_import_instance` will be passed to
        `post_import_instance_with_metadata`.
        """
        return response, metadata

    async def pre_list_instances(self, request: cloud_redis.ListInstancesRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[cloud_redis.ListInstancesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_instances

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_list_instances(self, response: cloud_redis.ListInstancesResponse) -> cloud_redis.ListInstancesResponse:
        """Post-rpc interceptor for list_instances

        DEPRECATED. Please use the `post_list_instances_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code. This `post_list_instances` interceptor runs
        before the `post_list_instances_with_metadata` interceptor.
        """
        return response

    async def post_list_instances_with_metadata(self, response: cloud_redis.ListInstancesResponse, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[cloud_redis.ListInstancesResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_instances

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudRedis server but before it is returned to user code.

        We recommend only using this `post_list_instances_with_metadata`
        interceptor in new development instead of the `post_list_instances` interceptor.
        When both interceptors are used, this `post_list_instances_with_metadata` interceptor runs after the
        `post_list_instances` interceptor. The (possibly modified) response returned by
        `post_list_instances` will be passed to
        `post_list_instances_with_metadata`.
        """
        return response, metadata

    async def pre_reschedule_maintenance(self, request: cloud_redis.RescheduleMaintenanceRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[cloud_redis.RescheduleMaintenanceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for reschedule_maintenance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_reschedule_maintenance(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for reschedule_maintenance

        DEPRECATED. Please use the `post_reschedule_maintenance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code. This `post_reschedule_maintenance` interceptor runs
        before the `post_reschedule_maintenance_with_metadata` interceptor.
        """
        return response

    async def post_reschedule_maintenance_with_metadata(self, response: operations_pb2.Operation, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for reschedule_maintenance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudRedis server but before it is returned to user code.

        We recommend only using this `post_reschedule_maintenance_with_metadata`
        interceptor in new development instead of the `post_reschedule_maintenance` interceptor.
        When both interceptors are used, this `post_reschedule_maintenance_with_metadata` interceptor runs after the
        `post_reschedule_maintenance` interceptor. The (possibly modified) response returned by
        `post_reschedule_maintenance` will be passed to
        `post_reschedule_maintenance_with_metadata`.
        """
        return response, metadata

    async def pre_update_instance(self, request: cloud_redis.UpdateInstanceRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[cloud_redis.UpdateInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_update_instance(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_instance

        DEPRECATED. Please use the `post_update_instance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code. This `post_update_instance` interceptor runs
        before the `post_update_instance_with_metadata` interceptor.
        """
        return response

    async def post_update_instance_with_metadata(self, response: operations_pb2.Operation, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_instance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudRedis server but before it is returned to user code.

        We recommend only using this `post_update_instance_with_metadata`
        interceptor in new development instead of the `post_update_instance` interceptor.
        When both interceptors are used, this `post_update_instance_with_metadata` interceptor runs after the
        `post_update_instance` interceptor. The (possibly modified) response returned by
        `post_update_instance` will be passed to
        `post_update_instance_with_metadata`.
        """
        return response, metadata

    async def pre_upgrade_instance(self, request: cloud_redis.UpgradeInstanceRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[cloud_redis.UpgradeInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for upgrade_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_upgrade_instance(self, response: operations_pb2.Operation) -> operations_pb2.Operation:
        """Post-rpc interceptor for upgrade_instance

        DEPRECATED. Please use the `post_upgrade_instance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code. This `post_upgrade_instance` interceptor runs
        before the `post_upgrade_instance_with_metadata` interceptor.
        """
        return response

    async def post_upgrade_instance_with_metadata(self, response: operations_pb2.Operation, metadata: Sequence[Tuple[str, Union[str, bytes]]]) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for upgrade_instance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the CloudRedis server but before it is returned to user code.

        We recommend only using this `post_upgrade_instance_with_metadata`
        interceptor in new development instead of the `post_upgrade_instance` interceptor.
        When both interceptors are used, this `post_upgrade_instance_with_metadata` interceptor runs after the
        `post_upgrade_instance` interceptor. The (possibly modified) response returned by
        `post_upgrade_instance` will be passed to
        `post_upgrade_instance_with_metadata`.
        """
        return response, metadata

    async def pre_get_location(
        self, request: locations_pb2.GetLocationRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[locations_pb2.GetLocationRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_location

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code.
        """
        return response

    async def pre_list_locations(
        self, request: locations_pb2.ListLocationsRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[locations_pb2.ListLocationsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_locations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code.
        """
        return response

    async def pre_cancel_operation(
        self, request: operations_pb2.CancelOperationRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[operations_pb2.CancelOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_cancel_operation(
        self, response: None
    ) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code.
        """
        return response

    async def pre_delete_operation(
        self, request: operations_pb2.DeleteOperationRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[operations_pb2.DeleteOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_delete_operation(
        self, response: None
    ) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code.
        """
        return response

    async def pre_get_operation(
        self, request: operations_pb2.GetOperationRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[operations_pb2.GetOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code.
        """
        return response

    async def pre_list_operations(
        self, request: operations_pb2.ListOperationsRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[operations_pb2.ListOperationsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_operations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code.
        """
        return response

    async def pre_wait_operation(
        self, request: operations_pb2.WaitOperationRequest, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[operations_pb2.WaitOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for wait_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the CloudRedis server.
        """
        return request, metadata

    async def post_wait_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for wait_operation

        Override in a subclass to manipulate the response
        after it is returned by the CloudRedis server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class AsyncCloudRedisRestStub:
    _session: AsyncAuthorizedSession
    _host: str
    _interceptor: AsyncCloudRedisRestInterceptor
    _client_options: Optional[ClientOptions] = None

class AsyncCloudRedisRestTransport(_BaseCloudRedisRestTransport):
    """Asynchronous REST backend transport for CloudRedis.

    Configures and manages Cloud Memorystore for Redis instances

    Google Cloud Memorystore for Redis v1

    The ``redis.googleapis.com`` service implements the Google Cloud
    Memorystore for Redis API and defines the following resource model
    for managing Redis instances:

    - The service works with a collection of cloud projects, named:
      ``/projects/*``
    - Each project has a collection of available locations, named:
      ``/locations/*``
    - Each location has a collection of Redis instances, named:
      ``/instances/*``
    - As such, Redis instances are resources of the form:
      ``/projects/{project_id}/locations/{location_id}/instances/{instance_id}``

    Note that location_id must be referring to a GCP ``region``; for
    example:

    - ``projects/redpepper-1290/locations/us-central1/instances/my-redis``

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """
    def __init__(self,
            *,
            host: str = 'redis.googleapis.com',
            credentials: Optional[Union[ga_credentials.Credentials, ga_credentials_async.Credentials]] = None,
            client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
            url_scheme: str = 'https',
            interceptor: Optional[AsyncCloudRedisRestInterceptor] = None,
            client_options: Optional[ClientOptions] = None,
            **kwargs,
            ) -> None:
        """Instantiate the transport.

       NOTE: This async REST transport functionality is currently in a beta
       state (preview). We welcome your feedback via a GitHub issue in
       this library's repository. Thank you!

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'redis.googleapis.com').
            credentials (Optional[Union[google.auth.credentials.Credentials, google.auth.aio.credentials.Credentials]]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            url_scheme (str): the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
            interceptor (Optional[AsyncCloudRedisRestInterceptor]): Interceptor used
                to manipulate requests, request metadata, and responses.
            client_options (Optional[google.api_core.client_options.ClientOptions]):
                Custom options for the client, containing options such as
                custom OpenTelemetry tracer providers.
        """
        # Run the base constructor
        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=False,
            url_scheme=url_scheme,
            api_audience=None,
            client_options=client_options,
            **kwargs,
        )
        self._session = AsyncAuthorizedSession(self._credentials)  # type: ignore
        self._interceptor = interceptor or AsyncCloudRedisRestInterceptor()
        self._prep_wrapped_messages(client_info)
        self._operations_client: Optional[operations_v1.AsyncOperationsRestClient] = None

    def _prep_wrapped_messages(self, client_info):
        """Precompute and cache wrapped methods for async RPC dispatch.

        Overrides the base class method to use asynchronous wrappers and retries.
        """
        self._wrapped_methods = {
            self.list_instances: self._wrap_async_method(
                self.list_instances,
                default_timeout=600.0,
                client_info=client_info,
                method_name="google.cloud.redis.v1.CloudRedis/ListInstances",
            ),
            self.get_instance: self._wrap_async_method(
                self.get_instance,
                default_timeout=600.0,
                client_info=client_info,
                method_name="google.cloud.redis.v1.CloudRedis/GetInstance",
            ),
            self.get_instance_auth_string: self._wrap_async_method(
                self.get_instance_auth_string,
                default_timeout=600.0,
                client_info=client_info,
                method_name="google.cloud.redis.v1.CloudRedis/GetInstanceAuthString",
            ),
            self.create_instance: self._wrap_async_method(
                self.create_instance,
                default_timeout=600.0,
                client_info=client_info,
                method_name="google.cloud.redis.v1.CloudRedis/CreateInstance",
            ),
            self.update_instance: self._wrap_async_method(
                self.update_instance,
                default_timeout=600.0,
                client_info=client_info,
                method_name="google.cloud.redis.v1.CloudRedis/UpdateInstance",
            ),
            self.upgrade_instance: self._wrap_async_method(
                self.upgrade_instance,
                default_timeout=600.0,
                client_info=client_info,
                method_name="google.cloud.redis.v1.CloudRedis/UpgradeInstance",
            ),
            self.import_instance: self._wrap_async_method(
                self.import_instance,
                default_timeout=600.0,
                client_info=client_info,
                method_name="google.cloud.redis.v1.CloudRedis/ImportInstance",
            ),
            self.export_instance: self._wrap_async_method(
                self.export_instance,
                default_timeout=600.0,
                client_info=client_info,
                method_name="google.cloud.redis.v1.CloudRedis/ExportInstance",
            ),
            self.failover_instance: self._wrap_async_method(
                self.failover_instance,
                default_timeout=600.0,
                client_info=client_info,
                method_name="google.cloud.redis.v1.CloudRedis/FailoverInstance",
            ),
            self.delete_instance: self._wrap_async_method(
                self.delete_instance,
                default_timeout=600.0,
                client_info=client_info,
                method_name="google.cloud.redis.v1.CloudRedis/DeleteInstance",
            ),
            self.reschedule_maintenance: self._wrap_async_method(
                self.reschedule_maintenance,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.redis.v1.CloudRedis/RescheduleMaintenance",
            ),
            self.get_location: self._wrap_async_method(
                self.get_location,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.location.Locations/GetLocation",
            ),
            self.list_locations: self._wrap_async_method(
                self.list_locations,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.location.Locations/ListLocations",
            ),
            self.cancel_operation: self._wrap_async_method(
                self.cancel_operation,
                default_timeout=None,
                client_info=client_info,
                method_name="google.longrunning.Operations/CancelOperation",
            ),
            self.delete_operation: self._wrap_async_method(
                self.delete_operation,
                default_timeout=None,
                client_info=client_info,
                method_name="google.longrunning.Operations/DeleteOperation",
            ),
            self.get_operation: self._wrap_async_method(
                self.get_operation,
                default_timeout=None,
                client_info=client_info,
                method_name="google.longrunning.Operations/GetOperation",
            ),
            self.list_operations: self._wrap_async_method(
                self.list_operations,
                default_timeout=None,
                client_info=client_info,
                method_name="google.longrunning.Operations/ListOperations",
            ),
            self.wait_operation: self._wrap_async_method(
                self.wait_operation,
                default_timeout=None,
                client_info=client_info,
                method_name="google.longrunning.Operations/WaitOperation",
            ),
        }

    class _CreateInstance(_BaseCloudRedisRestTransport._BaseCreateInstance, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.CreateInstance")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = await getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                    )
                trace_ctx.record_response(response)
                return response

        async def __call__(self,
                    request: cloud_redis.CreateInstanceRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                    ) -> operations_pb2.Operation:
            r"""Call the create instance method over HTTP.

            Args:
                request (~.cloud_redis.CreateInstanceRequest):
                    The request object. Request for
                [CreateInstance][google.cloud.redis.v1.CloudRedis.CreateInstance].
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
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

            http_options = _BaseCloudRedisRestTransport._BaseCreateInstance._get_http_options()
            request, metadata = await self._interceptor.pre_create_instance(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudRedisRestTransport._BaseCreateInstance,
                    "_BaseCreateInstance__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.cloud.redis_v1.CloudRedisClient.CreateInstance",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "CreateInstance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncCloudRedisRestTransport._CreateInstance._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = operations_pb2.Operation()
            pb_resp = resp
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_create_instance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = await self._interceptor.post_create_instance_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers":  dict(response.headers),
                    "status": "OK", # need to obtain this properly
                }
                _LOGGER.debug(
                    "Received response for google.cloud.redis_v1.CloudRedisAsyncClient.create_instance",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "CreateInstance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )

            return resp

    class _DeleteInstance(_BaseCloudRedisRestTransport._BaseDeleteInstance, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.DeleteInstance")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = await getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    )
                trace_ctx.record_response(response)
                return response

        async def __call__(self,
                    request: cloud_redis.DeleteInstanceRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                    ) -> operations_pb2.Operation:
            r"""Call the delete instance method over HTTP.

            Args:
                request (~.cloud_redis.DeleteInstanceRequest):
                    The request object. Request for
                [DeleteInstance][google.cloud.redis.v1.CloudRedis.DeleteInstance].
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
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

            http_options = _BaseCloudRedisRestTransport._BaseDeleteInstance._get_http_options()
            request, metadata = await self._interceptor.pre_delete_instance(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudRedisRestTransport._BaseDeleteInstance,
                    "_BaseDeleteInstance__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.cloud.redis_v1.CloudRedisClient.DeleteInstance",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "DeleteInstance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncCloudRedisRestTransport._DeleteInstance._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = operations_pb2.Operation()
            pb_resp = resp
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_delete_instance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = await self._interceptor.post_delete_instance_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers":  dict(response.headers),
                    "status": "OK", # need to obtain this properly
                }
                _LOGGER.debug(
                    "Received response for google.cloud.redis_v1.CloudRedisAsyncClient.delete_instance",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "DeleteInstance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )

            return resp

    class _ExportInstance(_BaseCloudRedisRestTransport._BaseExportInstance, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.ExportInstance")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = await getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                    )
                trace_ctx.record_response(response)
                return response

        async def __call__(self,
                    request: cloud_redis.ExportInstanceRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                    ) -> operations_pb2.Operation:
            r"""Call the export instance method over HTTP.

            Args:
                request (~.cloud_redis.ExportInstanceRequest):
                    The request object. Request for
                [Export][google.cloud.redis.v1.CloudRedis.ExportInstance].
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
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

            http_options = _BaseCloudRedisRestTransport._BaseExportInstance._get_http_options()
            request, metadata = await self._interceptor.pre_export_instance(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudRedisRestTransport._BaseExportInstance,
                    "_BaseExportInstance__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.cloud.redis_v1.CloudRedisClient.ExportInstance",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "ExportInstance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncCloudRedisRestTransport._ExportInstance._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = operations_pb2.Operation()
            pb_resp = resp
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_export_instance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = await self._interceptor.post_export_instance_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers":  dict(response.headers),
                    "status": "OK", # need to obtain this properly
                }
                _LOGGER.debug(
                    "Received response for google.cloud.redis_v1.CloudRedisAsyncClient.export_instance",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "ExportInstance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )

            return resp

    class _FailoverInstance(_BaseCloudRedisRestTransport._BaseFailoverInstance, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.FailoverInstance")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = await getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                    )
                trace_ctx.record_response(response)
                return response

        async def __call__(self,
                    request: cloud_redis.FailoverInstanceRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                    ) -> operations_pb2.Operation:
            r"""Call the failover instance method over HTTP.

            Args:
                request (~.cloud_redis.FailoverInstanceRequest):
                    The request object. Request for
                [Failover][google.cloud.redis.v1.CloudRedis.FailoverInstance].
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
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

            http_options = _BaseCloudRedisRestTransport._BaseFailoverInstance._get_http_options()
            request, metadata = await self._interceptor.pre_failover_instance(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudRedisRestTransport._BaseFailoverInstance,
                    "_BaseFailoverInstance__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.cloud.redis_v1.CloudRedisClient.FailoverInstance",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "FailoverInstance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncCloudRedisRestTransport._FailoverInstance._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = operations_pb2.Operation()
            pb_resp = resp
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_failover_instance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = await self._interceptor.post_failover_instance_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers":  dict(response.headers),
                    "status": "OK", # need to obtain this properly
                }
                _LOGGER.debug(
                    "Received response for google.cloud.redis_v1.CloudRedisAsyncClient.failover_instance",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "FailoverInstance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )

            return resp

    class _GetInstance(_BaseCloudRedisRestTransport._BaseGetInstance, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.GetInstance")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = await getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    )
                trace_ctx.record_response(response)
                return response

        async def __call__(self,
                    request: cloud_redis.GetInstanceRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                    ) -> cloud_redis.Instance:
            r"""Call the get instance method over HTTP.

            Args:
                request (~.cloud_redis.GetInstanceRequest):
                    The request object. Request for
                [GetInstance][google.cloud.redis.v1.CloudRedis.GetInstance].
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_redis.Instance:
                    A Memorystore for Redis instance.
            """

            http_options = _BaseCloudRedisRestTransport._BaseGetInstance._get_http_options()
            request, metadata = await self._interceptor.pre_get_instance(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudRedisRestTransport._BaseGetInstance,
                    "_BaseGetInstance__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.cloud.redis_v1.CloudRedisClient.GetInstance",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "GetInstance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncCloudRedisRestTransport._GetInstance._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = cloud_redis.Instance()
            pb_resp = cloud_redis.Instance.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_get_instance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = await self._interceptor.post_get_instance_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = cloud_redis.Instance.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers":  dict(response.headers),
                    "status": "OK", # need to obtain this properly
                }
                _LOGGER.debug(
                    "Received response for google.cloud.redis_v1.CloudRedisAsyncClient.get_instance",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "GetInstance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )

            return resp

    class _GetInstanceAuthString(_BaseCloudRedisRestTransport._BaseGetInstanceAuthString, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.GetInstanceAuthString")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = await getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    )
                trace_ctx.record_response(response)
                return response

        async def __call__(self,
                    request: cloud_redis.GetInstanceAuthStringRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                    ) -> cloud_redis.InstanceAuthString:
            r"""Call the get instance auth string method over HTTP.

            Args:
                request (~.cloud_redis.GetInstanceAuthStringRequest):
                    The request object. Request for
                [GetInstanceAuthString][google.cloud.redis.v1.CloudRedis.GetInstanceAuthString].
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_redis.InstanceAuthString:
                    Instance AUTH string details.
            """

            http_options = _BaseCloudRedisRestTransport._BaseGetInstanceAuthString._get_http_options()
            request, metadata = await self._interceptor.pre_get_instance_auth_string(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudRedisRestTransport._BaseGetInstanceAuthString,
                    "_BaseGetInstanceAuthString__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.cloud.redis_v1.CloudRedisClient.GetInstanceAuthString",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "GetInstanceAuthString",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncCloudRedisRestTransport._GetInstanceAuthString._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = cloud_redis.InstanceAuthString()
            pb_resp = cloud_redis.InstanceAuthString.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_get_instance_auth_string(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = await self._interceptor.post_get_instance_auth_string_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = cloud_redis.InstanceAuthString.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers":  dict(response.headers),
                    "status": "OK", # need to obtain this properly
                }
                _LOGGER.debug(
                    "Received response for google.cloud.redis_v1.CloudRedisAsyncClient.get_instance_auth_string",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "GetInstanceAuthString",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )

            return resp

    class _ImportInstance(_BaseCloudRedisRestTransport._BaseImportInstance, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.ImportInstance")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = await getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                    )
                trace_ctx.record_response(response)
                return response

        async def __call__(self,
                    request: cloud_redis.ImportInstanceRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                    ) -> operations_pb2.Operation:
            r"""Call the import instance method over HTTP.

            Args:
                request (~.cloud_redis.ImportInstanceRequest):
                    The request object. Request for
                [Import][google.cloud.redis.v1.CloudRedis.ImportInstance].
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
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

            http_options = _BaseCloudRedisRestTransport._BaseImportInstance._get_http_options()
            request, metadata = await self._interceptor.pre_import_instance(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudRedisRestTransport._BaseImportInstance,
                    "_BaseImportInstance__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.cloud.redis_v1.CloudRedisClient.ImportInstance",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "ImportInstance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncCloudRedisRestTransport._ImportInstance._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = operations_pb2.Operation()
            pb_resp = resp
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_import_instance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = await self._interceptor.post_import_instance_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers":  dict(response.headers),
                    "status": "OK", # need to obtain this properly
                }
                _LOGGER.debug(
                    "Received response for google.cloud.redis_v1.CloudRedisAsyncClient.import_instance",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "ImportInstance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )

            return resp

    class _ListInstances(_BaseCloudRedisRestTransport._BaseListInstances, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.ListInstances")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = await getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    )
                trace_ctx.record_response(response)
                return response

        async def __call__(self,
                    request: cloud_redis.ListInstancesRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                    ) -> cloud_redis.ListInstancesResponse:
            r"""Call the list instances method over HTTP.

            Args:
                request (~.cloud_redis.ListInstancesRequest):
                    The request object. Request for
                [ListInstances][google.cloud.redis.v1.CloudRedis.ListInstances].
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_redis.ListInstancesResponse:
                    Response for
                [ListInstances][google.cloud.redis.v1.CloudRedis.ListInstances].

            """

            http_options = _BaseCloudRedisRestTransport._BaseListInstances._get_http_options()
            request, metadata = await self._interceptor.pre_list_instances(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudRedisRestTransport._BaseListInstances,
                    "_BaseListInstances__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.cloud.redis_v1.CloudRedisClient.ListInstances",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "ListInstances",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncCloudRedisRestTransport._ListInstances._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = cloud_redis.ListInstancesResponse()
            pb_resp = cloud_redis.ListInstancesResponse.pb(resp)
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_list_instances(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = await self._interceptor.post_list_instances_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = cloud_redis.ListInstancesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers":  dict(response.headers),
                    "status": "OK", # need to obtain this properly
                }
                _LOGGER.debug(
                    "Received response for google.cloud.redis_v1.CloudRedisAsyncClient.list_instances",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "ListInstances",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )

            return resp

    class _RescheduleMaintenance(_BaseCloudRedisRestTransport._BaseRescheduleMaintenance, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.RescheduleMaintenance")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = await getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                    )
                trace_ctx.record_response(response)
                return response

        async def __call__(self,
                    request: cloud_redis.RescheduleMaintenanceRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                    ) -> operations_pb2.Operation:
            r"""Call the reschedule maintenance method over HTTP.

            Args:
                request (~.cloud_redis.RescheduleMaintenanceRequest):
                    The request object. Request for
                [RescheduleMaintenance][google.cloud.redis.v1.CloudRedis.RescheduleMaintenance].
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
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

            http_options = _BaseCloudRedisRestTransport._BaseRescheduleMaintenance._get_http_options()
            request, metadata = await self._interceptor.pre_reschedule_maintenance(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudRedisRestTransport._BaseRescheduleMaintenance,
                    "_BaseRescheduleMaintenance__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.cloud.redis_v1.CloudRedisClient.RescheduleMaintenance",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "RescheduleMaintenance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncCloudRedisRestTransport._RescheduleMaintenance._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = operations_pb2.Operation()
            pb_resp = resp
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_reschedule_maintenance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = await self._interceptor.post_reschedule_maintenance_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers":  dict(response.headers),
                    "status": "OK", # need to obtain this properly
                }
                _LOGGER.debug(
                    "Received response for google.cloud.redis_v1.CloudRedisAsyncClient.reschedule_maintenance",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "RescheduleMaintenance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )

            return resp

    class _UpdateInstance(_BaseCloudRedisRestTransport._BaseUpdateInstance, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.UpdateInstance")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = await getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                    )
                trace_ctx.record_response(response)
                return response

        async def __call__(self,
                    request: cloud_redis.UpdateInstanceRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                    ) -> operations_pb2.Operation:
            r"""Call the update instance method over HTTP.

            Args:
                request (~.cloud_redis.UpdateInstanceRequest):
                    The request object. Request for
                [UpdateInstance][google.cloud.redis.v1.CloudRedis.UpdateInstance].
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
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

            http_options = _BaseCloudRedisRestTransport._BaseUpdateInstance._get_http_options()
            request, metadata = await self._interceptor.pre_update_instance(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudRedisRestTransport._BaseUpdateInstance,
                    "_BaseUpdateInstance__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.cloud.redis_v1.CloudRedisClient.UpdateInstance",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "UpdateInstance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncCloudRedisRestTransport._UpdateInstance._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = operations_pb2.Operation()
            pb_resp = resp
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_update_instance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = await self._interceptor.post_update_instance_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers":  dict(response.headers),
                    "status": "OK", # need to obtain this properly
                }
                _LOGGER.debug(
                    "Received response for google.cloud.redis_v1.CloudRedisAsyncClient.update_instance",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "UpdateInstance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )

            return resp

    class _UpgradeInstance(_BaseCloudRedisRestTransport._BaseUpgradeInstance, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.UpgradeInstance")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = await getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                    )
                trace_ctx.record_response(response)
                return response

        async def __call__(self,
                    request: cloud_redis.UpgradeInstanceRequest, *,
                    retry: OptionalRetry=gapic_v1.method.DEFAULT,
                    timeout: Optional[float]=None,
                    metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
                    ) -> operations_pb2.Operation:
            r"""Call the upgrade instance method over HTTP.

            Args:
                request (~.cloud_redis.UpgradeInstanceRequest):
                    The request object. Request for
                [UpgradeInstance][google.cloud.redis.v1.CloudRedis.UpgradeInstance].
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
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

            http_options = _BaseCloudRedisRestTransport._BaseUpgradeInstance._get_http_options()
            request, metadata = await self._interceptor.pre_upgrade_instance(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudRedisRestTransport._BaseUpgradeInstance,
                    "_BaseUpgradeInstance__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.cloud.redis_v1.CloudRedisClient.UpgradeInstance",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "UpgradeInstance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncCloudRedisRestTransport._UpgradeInstance._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            # Return the response
            resp = operations_pb2.Operation()
            pb_resp = resp
            content = await response.read()
            json_format.Parse(content, pb_resp, ignore_unknown_fields=True)
            resp = await self._interceptor.post_upgrade_instance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = await self._interceptor.post_upgrade_instance_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers":  dict(response.headers),
                    "status": "OK", # need to obtain this properly
                }
                _LOGGER.debug(
                    "Received response for google.cloud.redis_v1.CloudRedisAsyncClient.upgrade_instance",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "UpgradeInstance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )

            return resp

    @property
    def operations_client(self) -> AsyncOperationsRestClient:
        """Create the async client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Only create a new client if we do not already have one.
        if self._operations_client is None:
            http_options: Dict[str, List[Dict[str, str]]] = {
                'google.longrunning.Operations.CancelOperation': [
                    {
                        'method': 'post',
                        'uri': '/v1/{name=projects/*/locations/*/operations/*}:cancel',
                    },
                ],
                'google.longrunning.Operations.DeleteOperation': [
                    {
                        'method': 'delete',
                        'uri': '/v1/{name=projects/*/locations/*/operations/*}',
                    },
                ],
                'google.longrunning.Operations.GetOperation': [
                    {
                        'method': 'get',
                        'uri': '/v1/{name=projects/*/locations/*/operations/*}',
                    },
                ],
                'google.longrunning.Operations.ListOperations': [
                    {
                        'method': 'get',
                        'uri': '/v1/{name=projects/*/locations/*}/operations',
                    },
                ],
                'google.longrunning.Operations.WaitOperation': [
                    {
                        'method': 'post',
                        'uri': '/v2/{name=projects/*/locations/*/operations/*}:wait',
                        'body': '*',
                    },
                ],
            }

            rest_transport = operations_v1.AsyncOperationsRestTransport(  # type: ignore
                    host=self._host,
                    # use the credentials which are saved
                    credentials=self._credentials,  # type: ignore
                    http_options=http_options,
                    path_prefix="v1"
            )

            self._operations_client = AsyncOperationsRestClient(transport=rest_transport)

        # Return the client from cache.
        return self._operations_client

    @property
    def create_instance(self) -> Callable[
            [cloud_redis.CreateInstanceRequest],
            operations_pb2.Operation]:
        return self._CreateInstance(self._session, self._host, self._interceptor, getattr(self, "_client_options", None))  # type: ignore

    @property
    def delete_instance(self) -> Callable[
            [cloud_redis.DeleteInstanceRequest],
            operations_pb2.Operation]:
        return self._DeleteInstance(self._session, self._host, self._interceptor, getattr(self, "_client_options", None))  # type: ignore

    @property
    def export_instance(self) -> Callable[
            [cloud_redis.ExportInstanceRequest],
            operations_pb2.Operation]:
        return self._ExportInstance(self._session, self._host, self._interceptor, getattr(self, "_client_options", None))  # type: ignore

    @property
    def failover_instance(self) -> Callable[
            [cloud_redis.FailoverInstanceRequest],
            operations_pb2.Operation]:
        return self._FailoverInstance(self._session, self._host, self._interceptor, getattr(self, "_client_options", None))  # type: ignore

    @property
    def get_instance(self) -> Callable[
            [cloud_redis.GetInstanceRequest],
            cloud_redis.Instance]:
        return self._GetInstance(self._session, self._host, self._interceptor, getattr(self, "_client_options", None))  # type: ignore

    @property
    def get_instance_auth_string(self) -> Callable[
            [cloud_redis.GetInstanceAuthStringRequest],
            cloud_redis.InstanceAuthString]:
        return self._GetInstanceAuthString(self._session, self._host, self._interceptor, getattr(self, "_client_options", None))  # type: ignore

    @property
    def import_instance(self) -> Callable[
            [cloud_redis.ImportInstanceRequest],
            operations_pb2.Operation]:
        return self._ImportInstance(self._session, self._host, self._interceptor, getattr(self, "_client_options", None))  # type: ignore

    @property
    def list_instances(self) -> Callable[
            [cloud_redis.ListInstancesRequest],
            cloud_redis.ListInstancesResponse]:
        return self._ListInstances(self._session, self._host, self._interceptor, getattr(self, "_client_options", None))  # type: ignore

    @property
    def reschedule_maintenance(self) -> Callable[
            [cloud_redis.RescheduleMaintenanceRequest],
            operations_pb2.Operation]:
        return self._RescheduleMaintenance(self._session, self._host, self._interceptor, getattr(self, "_client_options", None))  # type: ignore

    @property
    def update_instance(self) -> Callable[
            [cloud_redis.UpdateInstanceRequest],
            operations_pb2.Operation]:
        return self._UpdateInstance(self._session, self._host, self._interceptor, getattr(self, "_client_options", None))  # type: ignore

    @property
    def upgrade_instance(self) -> Callable[
            [cloud_redis.UpgradeInstanceRequest],
            operations_pb2.Operation]:
        return self._UpgradeInstance(self._session, self._host, self._interceptor, getattr(self, "_client_options", None))  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    class _GetLocation(_BaseCloudRedisRestTransport._BaseGetLocation, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.GetLocation")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = await getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    )
                trace_ctx.record_response(response)
                return response

        async def __call__(self,
            request: locations_pb2.GetLocationRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
            ) -> locations_pb2.Location:

            r"""Call the get location method over HTTP.

            Args:
                request (locations_pb2.GetLocationRequest):
                    The request object for GetLocation method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                locations_pb2.Location: Response from GetLocation method.
            """

            http_options = _BaseCloudRedisRestTransport._BaseGetLocation._get_http_options()
            request, metadata = await self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudRedisRestTransport._BaseGetLocation,
                    "_BaseGetLocation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.cloud.redis_v1.CloudRedisClient.GetLocation",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncCloudRedisRestTransport._GetLocation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            content = await response.read()
            resp = locations_pb2.Location()
            resp = json_format.Parse(content, resp)
            resp = await self._interceptor.post_get_location(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers":  dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.redis_v1.CloudRedisAsyncClient.GetLocation",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "GetLocation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_locations(self):
        return self._ListLocations(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    class _ListLocations(_BaseCloudRedisRestTransport._BaseListLocations, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.ListLocations")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = await getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    )
                trace_ctx.record_response(response)
                return response

        async def __call__(self,
            request: locations_pb2.ListLocationsRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
            ) -> locations_pb2.ListLocationsResponse:

            r"""Call the list locations method over HTTP.

            Args:
                request (locations_pb2.ListLocationsRequest):
                    The request object for ListLocations method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                locations_pb2.ListLocationsResponse: Response from ListLocations method.
            """

            http_options = _BaseCloudRedisRestTransport._BaseListLocations._get_http_options()
            request, metadata = await self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudRedisRestTransport._BaseListLocations,
                    "_BaseListLocations__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.cloud.redis_v1.CloudRedisClient.ListLocations",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncCloudRedisRestTransport._ListLocations._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            content = await response.read()
            resp = locations_pb2.ListLocationsResponse()
            resp = json_format.Parse(content, resp)
            resp = await self._interceptor.post_list_locations(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers":  dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.redis_v1.CloudRedisAsyncClient.ListLocations",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "ListLocations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    class _CancelOperation(_BaseCloudRedisRestTransport._BaseCancelOperation, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.CancelOperation")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = await getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    )
                trace_ctx.record_response(response)
                return response

        async def __call__(self,
            request: operations_pb2.CancelOperationRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
            ) -> None:

            r"""Call the cancel operation method over HTTP.

            Args:
                request (operations_pb2.CancelOperationRequest):
                    The request object for CancelOperation method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseCloudRedisRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = await self._interceptor.pre_cancel_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudRedisRestTransport._BaseCancelOperation,
                    "_BaseCancelOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.cloud.redis_v1.CloudRedisClient.CancelOperation",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncCloudRedisRestTransport._CancelOperation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            return await self._interceptor.post_cancel_operation(None)

    @property
    def delete_operation(self):
        return self._DeleteOperation(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    class _DeleteOperation(_BaseCloudRedisRestTransport._BaseDeleteOperation, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.DeleteOperation")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = await getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    )
                trace_ctx.record_response(response)
                return response

        async def __call__(self,
            request: operations_pb2.DeleteOperationRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
            ) -> None:

            r"""Call the delete operation method over HTTP.

            Args:
                request (operations_pb2.DeleteOperationRequest):
                    The request object for DeleteOperation method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseCloudRedisRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = await self._interceptor.pre_delete_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudRedisRestTransport._BaseDeleteOperation,
                    "_BaseDeleteOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.cloud.redis_v1.CloudRedisClient.DeleteOperation",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncCloudRedisRestTransport._DeleteOperation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            return await self._interceptor.post_delete_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    class _GetOperation(_BaseCloudRedisRestTransport._BaseGetOperation, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.GetOperation")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = await getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    )
                trace_ctx.record_response(response)
                return response

        async def __call__(self,
            request: operations_pb2.GetOperationRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
            ) -> operations_pb2.Operation:

            r"""Call the get operation method over HTTP.

            Args:
                request (operations_pb2.GetOperationRequest):
                    The request object for GetOperation method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                operations_pb2.Operation: Response from GetOperation method.
            """

            http_options = _BaseCloudRedisRestTransport._BaseGetOperation._get_http_options()
            request, metadata = await self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudRedisRestTransport._BaseGetOperation,
                    "_BaseGetOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.cloud.redis_v1.CloudRedisClient.GetOperation",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncCloudRedisRestTransport._GetOperation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            content = await response.read()
            resp = operations_pb2.Operation()
            resp = json_format.Parse(content, resp)
            resp = await self._interceptor.post_get_operation(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers":  dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.redis_v1.CloudRedisAsyncClient.GetOperation",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "GetOperation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_operations(self):
        return self._ListOperations(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    class _ListOperations(_BaseCloudRedisRestTransport._BaseListOperations, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.ListOperations")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = await getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    )
                trace_ctx.record_response(response)
                return response

        async def __call__(self,
            request: operations_pb2.ListOperationsRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
            ) -> operations_pb2.ListOperationsResponse:

            r"""Call the list operations method over HTTP.

            Args:
                request (operations_pb2.ListOperationsRequest):
                    The request object for ListOperations method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                operations_pb2.ListOperationsResponse: Response from ListOperations method.
            """

            http_options = _BaseCloudRedisRestTransport._BaseListOperations._get_http_options()
            request, metadata = await self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudRedisRestTransport._BaseListOperations,
                    "_BaseListOperations__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.cloud.redis_v1.CloudRedisClient.ListOperations",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncCloudRedisRestTransport._ListOperations._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            content = await response.read()
            resp = operations_pb2.ListOperationsResponse()
            resp = json_format.Parse(content, resp)
            resp = await self._interceptor.post_list_operations(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers":  dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.redis_v1.CloudRedisAsyncClient.ListOperations",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "ListOperations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def wait_operation(self):
        return self._WaitOperation(self._session, self._host, self._interceptor, getattr(self, "_client_options", None)) # type: ignore

    class _WaitOperation(_BaseCloudRedisRestTransport._BaseWaitOperation, AsyncCloudRedisRestStub):
        def __hash__(self):
            return hash("AsyncCloudRedisRestTransport.WaitOperation")

        @staticmethod
        async def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request['uri']
            method = transcoded_request['method']
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = await getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                    )
                trace_ctx.record_response(response)
                return response

        async def __call__(self,
            request: operations_pb2.WaitOperationRequest, *,
            retry: OptionalRetry=gapic_v1.method.DEFAULT,
            timeout: Optional[float]=None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]]=(),
            ) -> operations_pb2.Operation:

            r"""Call the wait operation method over HTTP.

            Args:
                request (operations_pb2.WaitOperationRequest):
                    The request object for WaitOperation method.
                retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                operations_pb2.Operation: Response from WaitOperation method.
            """

            http_options = _BaseCloudRedisRestTransport._BaseWaitOperation._get_http_options()
            request, metadata = await self._interceptor.pre_wait_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseCloudRedisRestTransport._BaseWaitOperation,
                    "_BaseWaitOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
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
                    f"Sending request for google.cloud.redis_v1.CloudRedisClient.WaitOperation",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "WaitOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = await AsyncCloudRedisRestTransport._WaitOperation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                content = await response.read()
                payload = json.loads(content.decode('utf-8'))
                request_url = "{host}{uri}".format(host=self._host, uri=transcoded_request['uri'])
                method = transcoded_request['method']
                raise core_exceptions.format_http_response_error(response, method, request_url, payload)  # type: ignore

            content = await response.read()
            resp = operations_pb2.Operation()
            resp = json_format.Parse(content, resp)
            resp = await self._interceptor.post_wait_operation(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(logging.DEBUG):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers":  dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.redis_v1.CloudRedisAsyncClient.WaitOperation",
                    extra = {
                        "serviceName": "google.cloud.redis.v1.CloudRedis",
                        "rpcName": "WaitOperation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def kind(self) -> str:
        return "rest_asyncio"

    async def close(self):
        await self._session.close()
