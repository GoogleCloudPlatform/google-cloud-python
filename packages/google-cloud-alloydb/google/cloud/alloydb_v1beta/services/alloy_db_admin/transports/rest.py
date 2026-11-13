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
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.alloydb_v1beta._compat import transcode_request
from google.cloud.alloydb_v1beta.types import resources, service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseAlloyDBAdminRestTransport

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


class AlloyDBAdminRestInterceptor:
    """Interceptor for AlloyDBAdmin.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the AlloyDBAdminRestTransport.

    .. code-block:: python
        class MyCustomAlloyDBAdminInterceptor(AlloyDBAdminRestInterceptor):
            def pre_batch_create_instances(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_instances(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_backup(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_backup(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_database(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_database(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_secondary_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_secondary_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_secondary_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_secondary_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_user(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_user(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_backup(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_backup(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_user(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_execute_sql(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_execute_sql(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_export_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_failover_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_failover_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_generate_client_certificate(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_generate_client_certificate(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_backup(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_backup(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_connection_info(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_connection_info(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_user(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_user(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_import_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_import_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_inject_fault(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_inject_fault(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_backups(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_backups(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_clusters(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_clusters(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_databases(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_databases(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_instances(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_instances(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_supported_database_flags(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_supported_database_flags(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_users(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_users(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_promote_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_promote_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_restart_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_restart_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_restore_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_restore_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_switchover_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_switchover_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_backup(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_backup(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_instance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_instance(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_user(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_user(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_upgrade_cluster(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_upgrade_cluster(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = AlloyDBAdminRestTransport(interceptor=MyCustomAlloyDBAdminInterceptor())
        client = AlloyDBAdminClient(transport=transport)


    """

    def pre_batch_create_instances(
        self,
        request: service.BatchCreateInstancesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.BatchCreateInstancesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for batch_create_instances

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_batch_create_instances(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for batch_create_instances

        DEPRECATED. Please use the `post_batch_create_instances_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_batch_create_instances` interceptor runs
        before the `post_batch_create_instances_with_metadata` interceptor.
        """
        return response

    def post_batch_create_instances_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for batch_create_instances

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_batch_create_instances_with_metadata`
        interceptor in new development instead of the `post_batch_create_instances` interceptor.
        When both interceptors are used, this `post_batch_create_instances_with_metadata` interceptor runs after the
        `post_batch_create_instances` interceptor. The (possibly modified) response returned by
        `post_batch_create_instances` will be passed to
        `post_batch_create_instances_with_metadata`.
        """
        return response, metadata

    def pre_create_backup(
        self,
        request: service.CreateBackupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.CreateBackupRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_backup

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_create_backup(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_backup

        DEPRECATED. Please use the `post_create_backup_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_create_backup` interceptor runs
        before the `post_create_backup_with_metadata` interceptor.
        """
        return response

    def post_create_backup_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_backup

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_create_backup_with_metadata`
        interceptor in new development instead of the `post_create_backup` interceptor.
        When both interceptors are used, this `post_create_backup_with_metadata` interceptor runs after the
        `post_create_backup` interceptor. The (possibly modified) response returned by
        `post_create_backup` will be passed to
        `post_create_backup_with_metadata`.
        """
        return response, metadata

    def pre_create_cluster(
        self,
        request: service.CreateClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.CreateClusterRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_create_cluster(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_cluster

        DEPRECATED. Please use the `post_create_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_create_cluster` interceptor runs
        before the `post_create_cluster_with_metadata` interceptor.
        """
        return response

    def post_create_cluster_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_create_cluster_with_metadata`
        interceptor in new development instead of the `post_create_cluster` interceptor.
        When both interceptors are used, this `post_create_cluster_with_metadata` interceptor runs after the
        `post_create_cluster` interceptor. The (possibly modified) response returned by
        `post_create_cluster` will be passed to
        `post_create_cluster_with_metadata`.
        """
        return response, metadata

    def pre_create_database(
        self,
        request: service.CreateDatabaseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.CreateDatabaseRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_database

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_create_database(self, response: resources.Database) -> resources.Database:
        """Post-rpc interceptor for create_database

        DEPRECATED. Please use the `post_create_database_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_create_database` interceptor runs
        before the `post_create_database_with_metadata` interceptor.
        """
        return response

    def post_create_database_with_metadata(
        self,
        response: resources.Database,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Database, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_database

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_create_database_with_metadata`
        interceptor in new development instead of the `post_create_database` interceptor.
        When both interceptors are used, this `post_create_database_with_metadata` interceptor runs after the
        `post_create_database` interceptor. The (possibly modified) response returned by
        `post_create_database` will be passed to
        `post_create_database_with_metadata`.
        """
        return response, metadata

    def pre_create_instance(
        self,
        request: service.CreateInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.CreateInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_create_instance(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_instance

        DEPRECATED. Please use the `post_create_instance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_create_instance` interceptor runs
        before the `post_create_instance_with_metadata` interceptor.
        """
        return response

    def post_create_instance_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_instance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_create_instance_with_metadata`
        interceptor in new development instead of the `post_create_instance` interceptor.
        When both interceptors are used, this `post_create_instance_with_metadata` interceptor runs after the
        `post_create_instance` interceptor. The (possibly modified) response returned by
        `post_create_instance` will be passed to
        `post_create_instance_with_metadata`.
        """
        return response, metadata

    def pre_create_secondary_cluster(
        self,
        request: service.CreateSecondaryClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.CreateSecondaryClusterRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_secondary_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_create_secondary_cluster(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_secondary_cluster

        DEPRECATED. Please use the `post_create_secondary_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_create_secondary_cluster` interceptor runs
        before the `post_create_secondary_cluster_with_metadata` interceptor.
        """
        return response

    def post_create_secondary_cluster_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_secondary_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_create_secondary_cluster_with_metadata`
        interceptor in new development instead of the `post_create_secondary_cluster` interceptor.
        When both interceptors are used, this `post_create_secondary_cluster_with_metadata` interceptor runs after the
        `post_create_secondary_cluster` interceptor. The (possibly modified) response returned by
        `post_create_secondary_cluster` will be passed to
        `post_create_secondary_cluster_with_metadata`.
        """
        return response, metadata

    def pre_create_secondary_instance(
        self,
        request: service.CreateSecondaryInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.CreateSecondaryInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_secondary_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_create_secondary_instance(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_secondary_instance

        DEPRECATED. Please use the `post_create_secondary_instance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_create_secondary_instance` interceptor runs
        before the `post_create_secondary_instance_with_metadata` interceptor.
        """
        return response

    def post_create_secondary_instance_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_secondary_instance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_create_secondary_instance_with_metadata`
        interceptor in new development instead of the `post_create_secondary_instance` interceptor.
        When both interceptors are used, this `post_create_secondary_instance_with_metadata` interceptor runs after the
        `post_create_secondary_instance` interceptor. The (possibly modified) response returned by
        `post_create_secondary_instance` will be passed to
        `post_create_secondary_instance_with_metadata`.
        """
        return response, metadata

    def pre_create_user(
        self,
        request: service.CreateUserRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.CreateUserRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_user

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_create_user(self, response: resources.User) -> resources.User:
        """Post-rpc interceptor for create_user

        DEPRECATED. Please use the `post_create_user_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_create_user` interceptor runs
        before the `post_create_user_with_metadata` interceptor.
        """
        return response

    def post_create_user_with_metadata(
        self,
        response: resources.User,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.User, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_user

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_create_user_with_metadata`
        interceptor in new development instead of the `post_create_user` interceptor.
        When both interceptors are used, this `post_create_user_with_metadata` interceptor runs after the
        `post_create_user` interceptor. The (possibly modified) response returned by
        `post_create_user` will be passed to
        `post_create_user_with_metadata`.
        """
        return response, metadata

    def pre_delete_backup(
        self,
        request: service.DeleteBackupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.DeleteBackupRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_backup

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_delete_backup(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_backup

        DEPRECATED. Please use the `post_delete_backup_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_delete_backup` interceptor runs
        before the `post_delete_backup_with_metadata` interceptor.
        """
        return response

    def post_delete_backup_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_backup

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_delete_backup_with_metadata`
        interceptor in new development instead of the `post_delete_backup` interceptor.
        When both interceptors are used, this `post_delete_backup_with_metadata` interceptor runs after the
        `post_delete_backup` interceptor. The (possibly modified) response returned by
        `post_delete_backup` will be passed to
        `post_delete_backup_with_metadata`.
        """
        return response, metadata

    def pre_delete_cluster(
        self,
        request: service.DeleteClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.DeleteClusterRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_delete_cluster(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_cluster

        DEPRECATED. Please use the `post_delete_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_delete_cluster` interceptor runs
        before the `post_delete_cluster_with_metadata` interceptor.
        """
        return response

    def post_delete_cluster_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_delete_cluster_with_metadata`
        interceptor in new development instead of the `post_delete_cluster` interceptor.
        When both interceptors are used, this `post_delete_cluster_with_metadata` interceptor runs after the
        `post_delete_cluster` interceptor. The (possibly modified) response returned by
        `post_delete_cluster` will be passed to
        `post_delete_cluster_with_metadata`.
        """
        return response, metadata

    def pre_delete_instance(
        self,
        request: service.DeleteInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.DeleteInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_delete_instance(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_instance

        DEPRECATED. Please use the `post_delete_instance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_delete_instance` interceptor runs
        before the `post_delete_instance_with_metadata` interceptor.
        """
        return response

    def post_delete_instance_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_instance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_delete_instance_with_metadata`
        interceptor in new development instead of the `post_delete_instance` interceptor.
        When both interceptors are used, this `post_delete_instance_with_metadata` interceptor runs after the
        `post_delete_instance` interceptor. The (possibly modified) response returned by
        `post_delete_instance` will be passed to
        `post_delete_instance_with_metadata`.
        """
        return response, metadata

    def pre_delete_user(
        self,
        request: service.DeleteUserRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.DeleteUserRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_user

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def pre_execute_sql(
        self,
        request: service.ExecuteSqlRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ExecuteSqlRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for execute_sql

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_execute_sql(
        self, response: service.ExecuteSqlResponse
    ) -> service.ExecuteSqlResponse:
        """Post-rpc interceptor for execute_sql

        DEPRECATED. Please use the `post_execute_sql_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_execute_sql` interceptor runs
        before the `post_execute_sql_with_metadata` interceptor.
        """
        return response

    def post_execute_sql_with_metadata(
        self,
        response: service.ExecuteSqlResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ExecuteSqlResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for execute_sql

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_execute_sql_with_metadata`
        interceptor in new development instead of the `post_execute_sql` interceptor.
        When both interceptors are used, this `post_execute_sql_with_metadata` interceptor runs after the
        `post_execute_sql` interceptor. The (possibly modified) response returned by
        `post_execute_sql` will be passed to
        `post_execute_sql_with_metadata`.
        """
        return response, metadata

    def pre_export_cluster(
        self,
        request: service.ExportClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ExportClusterRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for export_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_export_cluster(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for export_cluster

        DEPRECATED. Please use the `post_export_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_export_cluster` interceptor runs
        before the `post_export_cluster_with_metadata` interceptor.
        """
        return response

    def post_export_cluster_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for export_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_export_cluster_with_metadata`
        interceptor in new development instead of the `post_export_cluster` interceptor.
        When both interceptors are used, this `post_export_cluster_with_metadata` interceptor runs after the
        `post_export_cluster` interceptor. The (possibly modified) response returned by
        `post_export_cluster` will be passed to
        `post_export_cluster_with_metadata`.
        """
        return response, metadata

    def pre_failover_instance(
        self,
        request: service.FailoverInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.FailoverInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for failover_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_failover_instance(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for failover_instance

        DEPRECATED. Please use the `post_failover_instance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_failover_instance` interceptor runs
        before the `post_failover_instance_with_metadata` interceptor.
        """
        return response

    def post_failover_instance_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for failover_instance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_failover_instance_with_metadata`
        interceptor in new development instead of the `post_failover_instance` interceptor.
        When both interceptors are used, this `post_failover_instance_with_metadata` interceptor runs after the
        `post_failover_instance` interceptor. The (possibly modified) response returned by
        `post_failover_instance` will be passed to
        `post_failover_instance_with_metadata`.
        """
        return response, metadata

    def pre_generate_client_certificate(
        self,
        request: service.GenerateClientCertificateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.GenerateClientCertificateRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for generate_client_certificate

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_generate_client_certificate(
        self, response: service.GenerateClientCertificateResponse
    ) -> service.GenerateClientCertificateResponse:
        """Post-rpc interceptor for generate_client_certificate

        DEPRECATED. Please use the `post_generate_client_certificate_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_generate_client_certificate` interceptor runs
        before the `post_generate_client_certificate_with_metadata` interceptor.
        """
        return response

    def post_generate_client_certificate_with_metadata(
        self,
        response: service.GenerateClientCertificateResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.GenerateClientCertificateResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for generate_client_certificate

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_generate_client_certificate_with_metadata`
        interceptor in new development instead of the `post_generate_client_certificate` interceptor.
        When both interceptors are used, this `post_generate_client_certificate_with_metadata` interceptor runs after the
        `post_generate_client_certificate` interceptor. The (possibly modified) response returned by
        `post_generate_client_certificate` will be passed to
        `post_generate_client_certificate_with_metadata`.
        """
        return response, metadata

    def pre_get_backup(
        self,
        request: service.GetBackupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetBackupRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_backup

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_get_backup(self, response: resources.Backup) -> resources.Backup:
        """Post-rpc interceptor for get_backup

        DEPRECATED. Please use the `post_get_backup_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_get_backup` interceptor runs
        before the `post_get_backup_with_metadata` interceptor.
        """
        return response

    def post_get_backup_with_metadata(
        self,
        response: resources.Backup,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Backup, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_backup

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_get_backup_with_metadata`
        interceptor in new development instead of the `post_get_backup` interceptor.
        When both interceptors are used, this `post_get_backup_with_metadata` interceptor runs after the
        `post_get_backup` interceptor. The (possibly modified) response returned by
        `post_get_backup` will be passed to
        `post_get_backup_with_metadata`.
        """
        return response, metadata

    def pre_get_cluster(
        self,
        request: service.GetClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetClusterRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_get_cluster(self, response: resources.Cluster) -> resources.Cluster:
        """Post-rpc interceptor for get_cluster

        DEPRECATED. Please use the `post_get_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_get_cluster` interceptor runs
        before the `post_get_cluster_with_metadata` interceptor.
        """
        return response

    def post_get_cluster_with_metadata(
        self,
        response: resources.Cluster,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Cluster, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_get_cluster_with_metadata`
        interceptor in new development instead of the `post_get_cluster` interceptor.
        When both interceptors are used, this `post_get_cluster_with_metadata` interceptor runs after the
        `post_get_cluster` interceptor. The (possibly modified) response returned by
        `post_get_cluster` will be passed to
        `post_get_cluster_with_metadata`.
        """
        return response, metadata

    def pre_get_connection_info(
        self,
        request: service.GetConnectionInfoRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.GetConnectionInfoRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_connection_info

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_get_connection_info(
        self, response: resources.ConnectionInfo
    ) -> resources.ConnectionInfo:
        """Post-rpc interceptor for get_connection_info

        DEPRECATED. Please use the `post_get_connection_info_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_get_connection_info` interceptor runs
        before the `post_get_connection_info_with_metadata` interceptor.
        """
        return response

    def post_get_connection_info_with_metadata(
        self,
        response: resources.ConnectionInfo,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.ConnectionInfo, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_connection_info

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_get_connection_info_with_metadata`
        interceptor in new development instead of the `post_get_connection_info` interceptor.
        When both interceptors are used, this `post_get_connection_info_with_metadata` interceptor runs after the
        `post_get_connection_info` interceptor. The (possibly modified) response returned by
        `post_get_connection_info` will be passed to
        `post_get_connection_info_with_metadata`.
        """
        return response, metadata

    def pre_get_instance(
        self,
        request: service.GetInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_get_instance(self, response: resources.Instance) -> resources.Instance:
        """Post-rpc interceptor for get_instance

        DEPRECATED. Please use the `post_get_instance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_get_instance` interceptor runs
        before the `post_get_instance_with_metadata` interceptor.
        """
        return response

    def post_get_instance_with_metadata(
        self,
        response: resources.Instance,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Instance, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_instance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_get_instance_with_metadata`
        interceptor in new development instead of the `post_get_instance` interceptor.
        When both interceptors are used, this `post_get_instance_with_metadata` interceptor runs after the
        `post_get_instance` interceptor. The (possibly modified) response returned by
        `post_get_instance` will be passed to
        `post_get_instance_with_metadata`.
        """
        return response, metadata

    def pre_get_user(
        self,
        request: service.GetUserRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.GetUserRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_user

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_get_user(self, response: resources.User) -> resources.User:
        """Post-rpc interceptor for get_user

        DEPRECATED. Please use the `post_get_user_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_get_user` interceptor runs
        before the `post_get_user_with_metadata` interceptor.
        """
        return response

    def post_get_user_with_metadata(
        self,
        response: resources.User,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.User, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_user

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_get_user_with_metadata`
        interceptor in new development instead of the `post_get_user` interceptor.
        When both interceptors are used, this `post_get_user_with_metadata` interceptor runs after the
        `post_get_user` interceptor. The (possibly modified) response returned by
        `post_get_user` will be passed to
        `post_get_user_with_metadata`.
        """
        return response, metadata

    def pre_import_cluster(
        self,
        request: service.ImportClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ImportClusterRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for import_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_import_cluster(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for import_cluster

        DEPRECATED. Please use the `post_import_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_import_cluster` interceptor runs
        before the `post_import_cluster_with_metadata` interceptor.
        """
        return response

    def post_import_cluster_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for import_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_import_cluster_with_metadata`
        interceptor in new development instead of the `post_import_cluster` interceptor.
        When both interceptors are used, this `post_import_cluster_with_metadata` interceptor runs after the
        `post_import_cluster` interceptor. The (possibly modified) response returned by
        `post_import_cluster` will be passed to
        `post_import_cluster_with_metadata`.
        """
        return response, metadata

    def pre_inject_fault(
        self,
        request: service.InjectFaultRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.InjectFaultRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for inject_fault

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_inject_fault(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for inject_fault

        DEPRECATED. Please use the `post_inject_fault_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_inject_fault` interceptor runs
        before the `post_inject_fault_with_metadata` interceptor.
        """
        return response

    def post_inject_fault_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for inject_fault

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_inject_fault_with_metadata`
        interceptor in new development instead of the `post_inject_fault` interceptor.
        When both interceptors are used, this `post_inject_fault_with_metadata` interceptor runs after the
        `post_inject_fault` interceptor. The (possibly modified) response returned by
        `post_inject_fault` will be passed to
        `post_inject_fault_with_metadata`.
        """
        return response, metadata

    def pre_list_backups(
        self,
        request: service.ListBackupsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListBackupsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_backups

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_list_backups(
        self, response: service.ListBackupsResponse
    ) -> service.ListBackupsResponse:
        """Post-rpc interceptor for list_backups

        DEPRECATED. Please use the `post_list_backups_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_list_backups` interceptor runs
        before the `post_list_backups_with_metadata` interceptor.
        """
        return response

    def post_list_backups_with_metadata(
        self,
        response: service.ListBackupsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListBackupsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_backups

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_list_backups_with_metadata`
        interceptor in new development instead of the `post_list_backups` interceptor.
        When both interceptors are used, this `post_list_backups_with_metadata` interceptor runs after the
        `post_list_backups` interceptor. The (possibly modified) response returned by
        `post_list_backups` will be passed to
        `post_list_backups_with_metadata`.
        """
        return response, metadata

    def pre_list_clusters(
        self,
        request: service.ListClustersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListClustersRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_clusters

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_list_clusters(
        self, response: service.ListClustersResponse
    ) -> service.ListClustersResponse:
        """Post-rpc interceptor for list_clusters

        DEPRECATED. Please use the `post_list_clusters_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_list_clusters` interceptor runs
        before the `post_list_clusters_with_metadata` interceptor.
        """
        return response

    def post_list_clusters_with_metadata(
        self,
        response: service.ListClustersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListClustersResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_clusters

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_list_clusters_with_metadata`
        interceptor in new development instead of the `post_list_clusters` interceptor.
        When both interceptors are used, this `post_list_clusters_with_metadata` interceptor runs after the
        `post_list_clusters` interceptor. The (possibly modified) response returned by
        `post_list_clusters` will be passed to
        `post_list_clusters_with_metadata`.
        """
        return response, metadata

    def pre_list_databases(
        self,
        request: service.ListDatabasesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListDatabasesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_databases

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_list_databases(
        self, response: service.ListDatabasesResponse
    ) -> service.ListDatabasesResponse:
        """Post-rpc interceptor for list_databases

        DEPRECATED. Please use the `post_list_databases_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_list_databases` interceptor runs
        before the `post_list_databases_with_metadata` interceptor.
        """
        return response

    def post_list_databases_with_metadata(
        self,
        response: service.ListDatabasesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListDatabasesResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_databases

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_list_databases_with_metadata`
        interceptor in new development instead of the `post_list_databases` interceptor.
        When both interceptors are used, this `post_list_databases_with_metadata` interceptor runs after the
        `post_list_databases` interceptor. The (possibly modified) response returned by
        `post_list_databases` will be passed to
        `post_list_databases_with_metadata`.
        """
        return response, metadata

    def pre_list_instances(
        self,
        request: service.ListInstancesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListInstancesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_instances

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_list_instances(
        self, response: service.ListInstancesResponse
    ) -> service.ListInstancesResponse:
        """Post-rpc interceptor for list_instances

        DEPRECATED. Please use the `post_list_instances_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_list_instances` interceptor runs
        before the `post_list_instances_with_metadata` interceptor.
        """
        return response

    def post_list_instances_with_metadata(
        self,
        response: service.ListInstancesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListInstancesResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_instances

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_list_instances_with_metadata`
        interceptor in new development instead of the `post_list_instances` interceptor.
        When both interceptors are used, this `post_list_instances_with_metadata` interceptor runs after the
        `post_list_instances` interceptor. The (possibly modified) response returned by
        `post_list_instances` will be passed to
        `post_list_instances_with_metadata`.
        """
        return response, metadata

    def pre_list_supported_database_flags(
        self,
        request: service.ListSupportedDatabaseFlagsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListSupportedDatabaseFlagsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_supported_database_flags

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_list_supported_database_flags(
        self, response: service.ListSupportedDatabaseFlagsResponse
    ) -> service.ListSupportedDatabaseFlagsResponse:
        """Post-rpc interceptor for list_supported_database_flags

        DEPRECATED. Please use the `post_list_supported_database_flags_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_list_supported_database_flags` interceptor runs
        before the `post_list_supported_database_flags_with_metadata` interceptor.
        """
        return response

    def post_list_supported_database_flags_with_metadata(
        self,
        response: service.ListSupportedDatabaseFlagsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.ListSupportedDatabaseFlagsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_supported_database_flags

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_list_supported_database_flags_with_metadata`
        interceptor in new development instead of the `post_list_supported_database_flags` interceptor.
        When both interceptors are used, this `post_list_supported_database_flags_with_metadata` interceptor runs after the
        `post_list_supported_database_flags` interceptor. The (possibly modified) response returned by
        `post_list_supported_database_flags` will be passed to
        `post_list_supported_database_flags_with_metadata`.
        """
        return response, metadata

    def pre_list_users(
        self,
        request: service.ListUsersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListUsersRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_users

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_list_users(
        self, response: service.ListUsersResponse
    ) -> service.ListUsersResponse:
        """Post-rpc interceptor for list_users

        DEPRECATED. Please use the `post_list_users_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_list_users` interceptor runs
        before the `post_list_users_with_metadata` interceptor.
        """
        return response

    def post_list_users_with_metadata(
        self,
        response: service.ListUsersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.ListUsersResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_users

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_list_users_with_metadata`
        interceptor in new development instead of the `post_list_users` interceptor.
        When both interceptors are used, this `post_list_users_with_metadata` interceptor runs after the
        `post_list_users` interceptor. The (possibly modified) response returned by
        `post_list_users` will be passed to
        `post_list_users_with_metadata`.
        """
        return response, metadata

    def pre_promote_cluster(
        self,
        request: service.PromoteClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.PromoteClusterRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for promote_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_promote_cluster(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for promote_cluster

        DEPRECATED. Please use the `post_promote_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_promote_cluster` interceptor runs
        before the `post_promote_cluster_with_metadata` interceptor.
        """
        return response

    def post_promote_cluster_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for promote_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_promote_cluster_with_metadata`
        interceptor in new development instead of the `post_promote_cluster` interceptor.
        When both interceptors are used, this `post_promote_cluster_with_metadata` interceptor runs after the
        `post_promote_cluster` interceptor. The (possibly modified) response returned by
        `post_promote_cluster` will be passed to
        `post_promote_cluster_with_metadata`.
        """
        return response, metadata

    def pre_restart_instance(
        self,
        request: service.RestartInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.RestartInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for restart_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_restart_instance(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for restart_instance

        DEPRECATED. Please use the `post_restart_instance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_restart_instance` interceptor runs
        before the `post_restart_instance_with_metadata` interceptor.
        """
        return response

    def post_restart_instance_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for restart_instance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_restart_instance_with_metadata`
        interceptor in new development instead of the `post_restart_instance` interceptor.
        When both interceptors are used, this `post_restart_instance_with_metadata` interceptor runs after the
        `post_restart_instance` interceptor. The (possibly modified) response returned by
        `post_restart_instance` will be passed to
        `post_restart_instance_with_metadata`.
        """
        return response, metadata

    def pre_restore_cluster(
        self,
        request: service.RestoreClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.RestoreClusterRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for restore_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_restore_cluster(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for restore_cluster

        DEPRECATED. Please use the `post_restore_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_restore_cluster` interceptor runs
        before the `post_restore_cluster_with_metadata` interceptor.
        """
        return response

    def post_restore_cluster_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for restore_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_restore_cluster_with_metadata`
        interceptor in new development instead of the `post_restore_cluster` interceptor.
        When both interceptors are used, this `post_restore_cluster_with_metadata` interceptor runs after the
        `post_restore_cluster` interceptor. The (possibly modified) response returned by
        `post_restore_cluster` will be passed to
        `post_restore_cluster_with_metadata`.
        """
        return response, metadata

    def pre_switchover_cluster(
        self,
        request: service.SwitchoverClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        service.SwitchoverClusterRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for switchover_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_switchover_cluster(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for switchover_cluster

        DEPRECATED. Please use the `post_switchover_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_switchover_cluster` interceptor runs
        before the `post_switchover_cluster_with_metadata` interceptor.
        """
        return response

    def post_switchover_cluster_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for switchover_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_switchover_cluster_with_metadata`
        interceptor in new development instead of the `post_switchover_cluster` interceptor.
        When both interceptors are used, this `post_switchover_cluster_with_metadata` interceptor runs after the
        `post_switchover_cluster` interceptor. The (possibly modified) response returned by
        `post_switchover_cluster` will be passed to
        `post_switchover_cluster_with_metadata`.
        """
        return response, metadata

    def pre_update_backup(
        self,
        request: service.UpdateBackupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.UpdateBackupRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_backup

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_update_backup(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_backup

        DEPRECATED. Please use the `post_update_backup_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_update_backup` interceptor runs
        before the `post_update_backup_with_metadata` interceptor.
        """
        return response

    def post_update_backup_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_backup

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_update_backup_with_metadata`
        interceptor in new development instead of the `post_update_backup` interceptor.
        When both interceptors are used, this `post_update_backup_with_metadata` interceptor runs after the
        `post_update_backup` interceptor. The (possibly modified) response returned by
        `post_update_backup` will be passed to
        `post_update_backup_with_metadata`.
        """
        return response, metadata

    def pre_update_cluster(
        self,
        request: service.UpdateClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.UpdateClusterRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_update_cluster(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_cluster

        DEPRECATED. Please use the `post_update_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_update_cluster` interceptor runs
        before the `post_update_cluster_with_metadata` interceptor.
        """
        return response

    def post_update_cluster_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_update_cluster_with_metadata`
        interceptor in new development instead of the `post_update_cluster` interceptor.
        When both interceptors are used, this `post_update_cluster_with_metadata` interceptor runs after the
        `post_update_cluster` interceptor. The (possibly modified) response returned by
        `post_update_cluster` will be passed to
        `post_update_cluster_with_metadata`.
        """
        return response, metadata

    def pre_update_instance(
        self,
        request: service.UpdateInstanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.UpdateInstanceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_instance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_update_instance(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_instance

        DEPRECATED. Please use the `post_update_instance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_update_instance` interceptor runs
        before the `post_update_instance_with_metadata` interceptor.
        """
        return response

    def post_update_instance_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_instance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_update_instance_with_metadata`
        interceptor in new development instead of the `post_update_instance` interceptor.
        When both interceptors are used, this `post_update_instance_with_metadata` interceptor runs after the
        `post_update_instance` interceptor. The (possibly modified) response returned by
        `post_update_instance` will be passed to
        `post_update_instance_with_metadata`.
        """
        return response, metadata

    def pre_update_user(
        self,
        request: service.UpdateUserRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.UpdateUserRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_user

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_update_user(self, response: resources.User) -> resources.User:
        """Post-rpc interceptor for update_user

        DEPRECATED. Please use the `post_update_user_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_update_user` interceptor runs
        before the `post_update_user_with_metadata` interceptor.
        """
        return response

    def post_update_user_with_metadata(
        self,
        response: resources.User,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.User, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_user

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_update_user_with_metadata`
        interceptor in new development instead of the `post_update_user` interceptor.
        When both interceptors are used, this `post_update_user_with_metadata` interceptor runs after the
        `post_update_user` interceptor. The (possibly modified) response returned by
        `post_update_user` will be passed to
        `post_update_user_with_metadata`.
        """
        return response, metadata

    def pre_upgrade_cluster(
        self,
        request: service.UpgradeClusterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[service.UpgradeClusterRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for upgrade_cluster

        Override in a subclass to manipulate the request or metadata
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_upgrade_cluster(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for upgrade_cluster

        DEPRECATED. Please use the `post_upgrade_cluster_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code. This `post_upgrade_cluster` interceptor runs
        before the `post_upgrade_cluster_with_metadata` interceptor.
        """
        return response

    def post_upgrade_cluster_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for upgrade_cluster

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the AlloyDBAdmin server but before it is returned to user code.

        We recommend only using this `post_upgrade_cluster_with_metadata`
        interceptor in new development instead of the `post_upgrade_cluster` interceptor.
        When both interceptors are used, this `post_upgrade_cluster_with_metadata` interceptor runs after the
        `post_upgrade_cluster` interceptor. The (possibly modified) response returned by
        `post_upgrade_cluster` will be passed to
        `post_upgrade_cluster_with_metadata`.
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
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the AlloyDBAdmin server but before
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
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the AlloyDBAdmin server but before
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
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the AlloyDBAdmin server but before
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
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the AlloyDBAdmin server but before
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
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the AlloyDBAdmin server but before
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
        before they are sent to the AlloyDBAdmin server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the AlloyDBAdmin server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class AlloyDBAdminRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: AlloyDBAdminRestInterceptor


class AlloyDBAdminRestTransport(_BaseAlloyDBAdminRestTransport):
    """REST backend synchronous transport for AlloyDBAdmin.

    Service describing handlers for resources

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "alloydb.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[AlloyDBAdminRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'alloydb.googleapis.com').
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
            interceptor (Optional[AlloyDBAdminRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or AlloyDBAdminRestInterceptor()
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
                        "uri": "/v1beta/{name=projects/*/locations/*/operations/*}:cancel",
                    },
                ],
                "google.longrunning.Operations.DeleteOperation": [
                    {
                        "method": "delete",
                        "uri": "/v1beta/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1beta/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v1beta/{name=projects/*/locations/*}/operations",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v1beta",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _BatchCreateInstances(
        _BaseAlloyDBAdminRestTransport._BaseBatchCreateInstances, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.BatchCreateInstances")

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
            request: service.BatchCreateInstancesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the batch create instances method over HTTP.

            Args:
                request (~.service.BatchCreateInstancesRequest):
                    The request object. Message for creating a batch of
                instances under the specified cluster.
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

            http_options = _BaseAlloyDBAdminRestTransport._BaseBatchCreateInstances._get_http_options()
            request, metadata = self._interceptor.pre_batch_create_instances(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseBatchCreateInstances,
                    "_BaseBatchCreateInstances__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.BatchCreateInstances",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "BatchCreateInstances",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._BatchCreateInstances._get_response(
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

            resp = self._interceptor.post_batch_create_instances(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_create_instances_with_metadata(
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
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.batch_create_instances",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "BatchCreateInstances",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateBackup(
        _BaseAlloyDBAdminRestTransport._BaseCreateBackup, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.CreateBackup")

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
            request: service.CreateBackupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create backup method over HTTP.

            Args:
                request (~.service.CreateBackupRequest):
                    The request object. Message for creating a Backup
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
                _BaseAlloyDBAdminRestTransport._BaseCreateBackup._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_backup(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseCreateBackup,
                    "_BaseCreateBackup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.CreateBackup",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "CreateBackup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._CreateBackup._get_response(
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

            resp = self._interceptor.post_create_backup(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_backup_with_metadata(
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
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.create_backup",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "CreateBackup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateCluster(
        _BaseAlloyDBAdminRestTransport._BaseCreateCluster, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.CreateCluster")

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
            request: service.CreateClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create cluster method over HTTP.

            Args:
                request (~.service.CreateClusterRequest):
                    The request object. Message for creating a Cluster
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
                _BaseAlloyDBAdminRestTransport._BaseCreateCluster._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_cluster(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseCreateCluster,
                    "_BaseCreateCluster__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.CreateCluster",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "CreateCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._CreateCluster._get_response(
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

            resp = self._interceptor.post_create_cluster(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_cluster_with_metadata(
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
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.create_cluster",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "CreateCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateDatabase(
        _BaseAlloyDBAdminRestTransport._BaseCreateDatabase, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.CreateDatabase")

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
            request: service.CreateDatabaseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Database:
            r"""Call the create database method over HTTP.

            Args:
                request (~.service.CreateDatabaseRequest):
                    The request object. Message for CreateDatabase request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Database:
                    Message describing Database object.
            """

            http_options = (
                _BaseAlloyDBAdminRestTransport._BaseCreateDatabase._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_database(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseCreateDatabase,
                    "_BaseCreateDatabase__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.CreateDatabase",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "CreateDatabase",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._CreateDatabase._get_response(
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
            resp = resources.Database()
            pb_resp = resources.Database.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_database(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_database_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Database.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.create_database",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "CreateDatabase",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateInstance(
        _BaseAlloyDBAdminRestTransport._BaseCreateInstance, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.CreateInstance")

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
            request: service.CreateInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create instance method over HTTP.

            Args:
                request (~.service.CreateInstanceRequest):
                    The request object. Message for creating a Instance
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
                _BaseAlloyDBAdminRestTransport._BaseCreateInstance._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_instance(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseCreateInstance,
                    "_BaseCreateInstance__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.CreateInstance",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "CreateInstance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._CreateInstance._get_response(
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

            resp = self._interceptor.post_create_instance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_instance_with_metadata(
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
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.create_instance",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "CreateInstance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateSecondaryCluster(
        _BaseAlloyDBAdminRestTransport._BaseCreateSecondaryCluster, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.CreateSecondaryCluster")

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
            request: service.CreateSecondaryClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create secondary cluster method over HTTP.

            Args:
                request (~.service.CreateSecondaryClusterRequest):
                    The request object.
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

            http_options = _BaseAlloyDBAdminRestTransport._BaseCreateSecondaryCluster._get_http_options()
            request, metadata = self._interceptor.pre_create_secondary_cluster(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseCreateSecondaryCluster,
                    "_BaseCreateSecondaryCluster__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.CreateSecondaryCluster",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "CreateSecondaryCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._CreateSecondaryCluster._get_response(
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

            resp = self._interceptor.post_create_secondary_cluster(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_secondary_cluster_with_metadata(
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
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.create_secondary_cluster",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "CreateSecondaryCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateSecondaryInstance(
        _BaseAlloyDBAdminRestTransport._BaseCreateSecondaryInstance,
        AlloyDBAdminRestStub,
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.CreateSecondaryInstance")

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
            request: service.CreateSecondaryInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create secondary instance method over HTTP.

            Args:
                request (~.service.CreateSecondaryInstanceRequest):
                    The request object. Message for creating a Secondary
                Instance
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

            http_options = _BaseAlloyDBAdminRestTransport._BaseCreateSecondaryInstance._get_http_options()
            request, metadata = self._interceptor.pre_create_secondary_instance(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseCreateSecondaryInstance,
                    "_BaseCreateSecondaryInstance__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.CreateSecondaryInstance",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "CreateSecondaryInstance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._CreateSecondaryInstance._get_response(
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

            resp = self._interceptor.post_create_secondary_instance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_secondary_instance_with_metadata(
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
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.create_secondary_instance",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "CreateSecondaryInstance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateUser(
        _BaseAlloyDBAdminRestTransport._BaseCreateUser, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.CreateUser")

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
            request: service.CreateUserRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.User:
            r"""Call the create user method over HTTP.

            Args:
                request (~.service.CreateUserRequest):
                    The request object. Message for creating a User
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.User:
                    Message describing User object.
            """

            http_options = (
                _BaseAlloyDBAdminRestTransport._BaseCreateUser._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_user(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseCreateUser,
                    "_BaseCreateUser__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.CreateUser",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "CreateUser",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._CreateUser._get_response(
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
            resp = resources.User()
            pb_resp = resources.User.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_user(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_user_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.User.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.create_user",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "CreateUser",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteBackup(
        _BaseAlloyDBAdminRestTransport._BaseDeleteBackup, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.DeleteBackup")

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
            request: service.DeleteBackupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete backup method over HTTP.

            Args:
                request (~.service.DeleteBackupRequest):
                    The request object. Message for deleting a Backup
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
                _BaseAlloyDBAdminRestTransport._BaseDeleteBackup._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_backup(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseDeleteBackup,
                    "_BaseDeleteBackup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.DeleteBackup",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "DeleteBackup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._DeleteBackup._get_response(
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

            resp = self._interceptor.post_delete_backup(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_backup_with_metadata(
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
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.delete_backup",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "DeleteBackup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteCluster(
        _BaseAlloyDBAdminRestTransport._BaseDeleteCluster, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.DeleteCluster")

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
            request: service.DeleteClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete cluster method over HTTP.

            Args:
                request (~.service.DeleteClusterRequest):
                    The request object. Message for deleting a Cluster
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
                _BaseAlloyDBAdminRestTransport._BaseDeleteCluster._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_cluster(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseDeleteCluster,
                    "_BaseDeleteCluster__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.DeleteCluster",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "DeleteCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._DeleteCluster._get_response(
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

            resp = self._interceptor.post_delete_cluster(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_cluster_with_metadata(
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
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.delete_cluster",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "DeleteCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteInstance(
        _BaseAlloyDBAdminRestTransport._BaseDeleteInstance, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.DeleteInstance")

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
            request: service.DeleteInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete instance method over HTTP.

            Args:
                request (~.service.DeleteInstanceRequest):
                    The request object. Message for deleting a Instance
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
                _BaseAlloyDBAdminRestTransport._BaseDeleteInstance._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_instance(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseDeleteInstance,
                    "_BaseDeleteInstance__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.DeleteInstance",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "DeleteInstance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._DeleteInstance._get_response(
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

            resp = self._interceptor.post_delete_instance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_instance_with_metadata(
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
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.delete_instance",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "DeleteInstance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteUser(
        _BaseAlloyDBAdminRestTransport._BaseDeleteUser, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.DeleteUser")

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
            request: service.DeleteUserRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete user method over HTTP.

            Args:
                request (~.service.DeleteUserRequest):
                    The request object. Message for deleting a User
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseAlloyDBAdminRestTransport._BaseDeleteUser._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_user(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseDeleteUser,
                    "_BaseDeleteUser__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.DeleteUser",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "DeleteUser",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._DeleteUser._get_response(
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

    class _ExecuteSql(
        _BaseAlloyDBAdminRestTransport._BaseExecuteSql, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.ExecuteSql")

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
            request: service.ExecuteSqlRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ExecuteSqlResponse:
            r"""Call the execute sql method over HTTP.

            Args:
                request (~.service.ExecuteSqlRequest):
                    The request object. Request for ExecuteSql rpc.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ExecuteSqlResponse:
                    Execute a SQL statement response.
            """

            http_options = (
                _BaseAlloyDBAdminRestTransport._BaseExecuteSql._get_http_options()
            )
            request, metadata = self._interceptor.pre_execute_sql(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseExecuteSql,
                    "_BaseExecuteSql__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.ExecuteSql",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "ExecuteSql",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._ExecuteSql._get_response(
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
            resp = service.ExecuteSqlResponse()
            pb_resp = service.ExecuteSqlResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_execute_sql(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_execute_sql_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ExecuteSqlResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.execute_sql",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "ExecuteSql",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ExportCluster(
        _BaseAlloyDBAdminRestTransport._BaseExportCluster, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.ExportCluster")

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
            request: service.ExportClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the export cluster method over HTTP.

            Args:
                request (~.service.ExportClusterRequest):
                    The request object. Export cluster request.
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
                _BaseAlloyDBAdminRestTransport._BaseExportCluster._get_http_options()
            )
            request, metadata = self._interceptor.pre_export_cluster(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseExportCluster,
                    "_BaseExportCluster__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.ExportCluster",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "ExportCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._ExportCluster._get_response(
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

            resp = self._interceptor.post_export_cluster(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_export_cluster_with_metadata(
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
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.export_cluster",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "ExportCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FailoverInstance(
        _BaseAlloyDBAdminRestTransport._BaseFailoverInstance, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.FailoverInstance")

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
            request: service.FailoverInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the failover instance method over HTTP.

            Args:
                request (~.service.FailoverInstanceRequest):
                    The request object. Message for triggering failover on an
                Instance
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
                _BaseAlloyDBAdminRestTransport._BaseFailoverInstance._get_http_options()
            )
            request, metadata = self._interceptor.pre_failover_instance(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseFailoverInstance,
                    "_BaseFailoverInstance__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.FailoverInstance",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "FailoverInstance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._FailoverInstance._get_response(
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

            resp = self._interceptor.post_failover_instance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_failover_instance_with_metadata(
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
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.failover_instance",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "FailoverInstance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GenerateClientCertificate(
        _BaseAlloyDBAdminRestTransport._BaseGenerateClientCertificate,
        AlloyDBAdminRestStub,
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.GenerateClientCertificate")

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
            request: service.GenerateClientCertificateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.GenerateClientCertificateResponse:
            r"""Call the generate client
            certificate method over HTTP.

                Args:
                    request (~.service.GenerateClientCertificateRequest):
                        The request object. Message for requests to generate a
                    client certificate signed by the Cluster
                    CA.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.service.GenerateClientCertificateResponse:
                        Message returned by a
                    GenerateClientCertificate operation.

            """

            http_options = _BaseAlloyDBAdminRestTransport._BaseGenerateClientCertificate._get_http_options()
            request, metadata = self._interceptor.pre_generate_client_certificate(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseGenerateClientCertificate,
                    "_BaseGenerateClientCertificate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.GenerateClientCertificate",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "GenerateClientCertificate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AlloyDBAdminRestTransport._GenerateClientCertificate._get_response(
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
            resp = service.GenerateClientCertificateResponse()
            pb_resp = service.GenerateClientCertificateResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_generate_client_certificate(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_generate_client_certificate_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        service.GenerateClientCertificateResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.generate_client_certificate",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "GenerateClientCertificate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetBackup(
        _BaseAlloyDBAdminRestTransport._BaseGetBackup, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.GetBackup")

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
            request: service.GetBackupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Backup:
            r"""Call the get backup method over HTTP.

            Args:
                request (~.service.GetBackupRequest):
                    The request object. Message for getting a Backup
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Backup:
                    Message describing Backup object
            """

            http_options = (
                _BaseAlloyDBAdminRestTransport._BaseGetBackup._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_backup(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseGetBackup,
                    "_BaseGetBackup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.GetBackup",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "GetBackup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._GetBackup._get_response(
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
            resp = resources.Backup()
            pb_resp = resources.Backup.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_backup(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_backup_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Backup.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.get_backup",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "GetBackup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetCluster(
        _BaseAlloyDBAdminRestTransport._BaseGetCluster, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.GetCluster")

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
            request: service.GetClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Cluster:
            r"""Call the get cluster method over HTTP.

            Args:
                request (~.service.GetClusterRequest):
                    The request object. Message for getting a Cluster
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Cluster:
                    A cluster is a collection of regional
                AlloyDB resources. It can include a
                primary instance and one or more read
                pool instances. All cluster resources
                share a storage layer, which scales as
                needed.

            """

            http_options = (
                _BaseAlloyDBAdminRestTransport._BaseGetCluster._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_cluster(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseGetCluster,
                    "_BaseGetCluster__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.GetCluster",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "GetCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._GetCluster._get_response(
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
            resp = resources.Cluster()
            pb_resp = resources.Cluster.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_cluster(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_cluster_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Cluster.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.get_cluster",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "GetCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetConnectionInfo(
        _BaseAlloyDBAdminRestTransport._BaseGetConnectionInfo, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.GetConnectionInfo")

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
            request: service.GetConnectionInfoRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.ConnectionInfo:
            r"""Call the get connection info method over HTTP.

            Args:
                request (~.service.GetConnectionInfoRequest):
                    The request object. Request message for
                GetConnectionInfo.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.ConnectionInfo:
                    ConnectionInfo singleton resource.
                https://google.aip.dev/156

            """

            http_options = _BaseAlloyDBAdminRestTransport._BaseGetConnectionInfo._get_http_options()
            request, metadata = self._interceptor.pre_get_connection_info(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseGetConnectionInfo,
                    "_BaseGetConnectionInfo__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.GetConnectionInfo",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "GetConnectionInfo",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._GetConnectionInfo._get_response(
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
            resp = resources.ConnectionInfo()
            pb_resp = resources.ConnectionInfo.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_connection_info(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_connection_info_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.ConnectionInfo.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.get_connection_info",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "GetConnectionInfo",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetInstance(
        _BaseAlloyDBAdminRestTransport._BaseGetInstance, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.GetInstance")

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
            request: service.GetInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Instance:
            r"""Call the get instance method over HTTP.

            Args:
                request (~.service.GetInstanceRequest):
                    The request object. Message for getting a Instance
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Instance:
                    An Instance is a computing unit that
                an end customer can connect to. It's the
                main unit of computing resources in
                AlloyDB.

            """

            http_options = (
                _BaseAlloyDBAdminRestTransport._BaseGetInstance._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_instance(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseGetInstance,
                    "_BaseGetInstance__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.GetInstance",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "GetInstance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._GetInstance._get_response(
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
            resp = resources.Instance()
            pb_resp = resources.Instance.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_instance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_instance_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Instance.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.get_instance",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "GetInstance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetUser(_BaseAlloyDBAdminRestTransport._BaseGetUser, AlloyDBAdminRestStub):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.GetUser")

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
            request: service.GetUserRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.User:
            r"""Call the get user method over HTTP.

            Args:
                request (~.service.GetUserRequest):
                    The request object. Message for getting a User
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.User:
                    Message describing User object.
            """

            http_options = (
                _BaseAlloyDBAdminRestTransport._BaseGetUser._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_user(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseGetUser,
                    "_BaseGetUser__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.GetUser",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "GetUser",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._GetUser._get_response(
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
            resp = resources.User()
            pb_resp = resources.User.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_user(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_user_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.User.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.get_user",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "GetUser",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ImportCluster(
        _BaseAlloyDBAdminRestTransport._BaseImportCluster, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.ImportCluster")

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
            request: service.ImportClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the import cluster method over HTTP.

            Args:
                request (~.service.ImportClusterRequest):
                    The request object. Import cluster request.
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
                _BaseAlloyDBAdminRestTransport._BaseImportCluster._get_http_options()
            )
            request, metadata = self._interceptor.pre_import_cluster(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseImportCluster,
                    "_BaseImportCluster__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.ImportCluster",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "ImportCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._ImportCluster._get_response(
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

            resp = self._interceptor.post_import_cluster(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_import_cluster_with_metadata(
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
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.import_cluster",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "ImportCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _InjectFault(
        _BaseAlloyDBAdminRestTransport._BaseInjectFault, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.InjectFault")

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
            request: service.InjectFaultRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the inject fault method over HTTP.

            Args:
                request (~.service.InjectFaultRequest):
                    The request object. Message for triggering fault
                injection on an instance
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
                _BaseAlloyDBAdminRestTransport._BaseInjectFault._get_http_options()
            )
            request, metadata = self._interceptor.pre_inject_fault(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseInjectFault,
                    "_BaseInjectFault__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.InjectFault",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "InjectFault",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._InjectFault._get_response(
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

            resp = self._interceptor.post_inject_fault(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_inject_fault_with_metadata(
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
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.inject_fault",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "InjectFault",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListBackups(
        _BaseAlloyDBAdminRestTransport._BaseListBackups, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.ListBackups")

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
            request: service.ListBackupsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListBackupsResponse:
            r"""Call the list backups method over HTTP.

            Args:
                request (~.service.ListBackupsRequest):
                    The request object. Message for requesting list of
                Backups
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListBackupsResponse:
                    Message for response to listing
                Backups

            """

            http_options = (
                _BaseAlloyDBAdminRestTransport._BaseListBackups._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_backups(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseListBackups,
                    "_BaseListBackups__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.ListBackups",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "ListBackups",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._ListBackups._get_response(
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
            resp = service.ListBackupsResponse()
            pb_resp = service.ListBackupsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_backups(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_backups_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListBackupsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.list_backups",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "ListBackups",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListClusters(
        _BaseAlloyDBAdminRestTransport._BaseListClusters, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.ListClusters")

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
            request: service.ListClustersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListClustersResponse:
            r"""Call the list clusters method over HTTP.

            Args:
                request (~.service.ListClustersRequest):
                    The request object. Message for requesting list of
                Clusters
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListClustersResponse:
                    Message for response to listing
                Clusters

            """

            http_options = (
                _BaseAlloyDBAdminRestTransport._BaseListClusters._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_clusters(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseListClusters,
                    "_BaseListClusters__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.ListClusters",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "ListClusters",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._ListClusters._get_response(
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
            resp = service.ListClustersResponse()
            pb_resp = service.ListClustersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_clusters(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_clusters_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListClustersResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.list_clusters",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "ListClusters",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDatabases(
        _BaseAlloyDBAdminRestTransport._BaseListDatabases, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.ListDatabases")

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
            request: service.ListDatabasesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListDatabasesResponse:
            r"""Call the list databases method over HTTP.

            Args:
                request (~.service.ListDatabasesRequest):
                    The request object. Message for ListDatabases request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListDatabasesResponse:
                    Message for ListDatabases response.
            """

            http_options = (
                _BaseAlloyDBAdminRestTransport._BaseListDatabases._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_databases(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseListDatabases,
                    "_BaseListDatabases__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.ListDatabases",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "ListDatabases",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._ListDatabases._get_response(
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
            resp = service.ListDatabasesResponse()
            pb_resp = service.ListDatabasesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_databases(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_databases_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListDatabasesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.list_databases",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "ListDatabases",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListInstances(
        _BaseAlloyDBAdminRestTransport._BaseListInstances, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.ListInstances")

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
            request: service.ListInstancesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListInstancesResponse:
            r"""Call the list instances method over HTTP.

            Args:
                request (~.service.ListInstancesRequest):
                    The request object. Message for requesting list of
                Instances
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListInstancesResponse:
                    Message for response to listing
                Instances

            """

            http_options = (
                _BaseAlloyDBAdminRestTransport._BaseListInstances._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_instances(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseListInstances,
                    "_BaseListInstances__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.ListInstances",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "ListInstances",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._ListInstances._get_response(
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
            resp = service.ListInstancesResponse()
            pb_resp = service.ListInstancesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_instances(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_instances_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListInstancesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.list_instances",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "ListInstances",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSupportedDatabaseFlags(
        _BaseAlloyDBAdminRestTransport._BaseListSupportedDatabaseFlags,
        AlloyDBAdminRestStub,
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.ListSupportedDatabaseFlags")

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
            request: service.ListSupportedDatabaseFlagsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListSupportedDatabaseFlagsResponse:
            r"""Call the list supported database
            flags method over HTTP.

                Args:
                    request (~.service.ListSupportedDatabaseFlagsRequest):
                        The request object. Message for listing the information
                    about the supported Database flags.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.service.ListSupportedDatabaseFlagsResponse:
                        Message for response to listing
                    SupportedDatabaseFlags.

            """

            http_options = _BaseAlloyDBAdminRestTransport._BaseListSupportedDatabaseFlags._get_http_options()
            request, metadata = self._interceptor.pre_list_supported_database_flags(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseListSupportedDatabaseFlags,
                    "_BaseListSupportedDatabaseFlags__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.ListSupportedDatabaseFlags",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "ListSupportedDatabaseFlags",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                AlloyDBAdminRestTransport._ListSupportedDatabaseFlags._get_response(
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
            resp = service.ListSupportedDatabaseFlagsResponse()
            pb_resp = service.ListSupportedDatabaseFlagsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_supported_database_flags(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_supported_database_flags_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        service.ListSupportedDatabaseFlagsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.list_supported_database_flags",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "ListSupportedDatabaseFlags",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListUsers(
        _BaseAlloyDBAdminRestTransport._BaseListUsers, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.ListUsers")

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
            request: service.ListUsersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> service.ListUsersResponse:
            r"""Call the list users method over HTTP.

            Args:
                request (~.service.ListUsersRequest):
                    The request object. Message for requesting list of Users
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.service.ListUsersResponse:
                    Message for response to listing Users
            """

            http_options = (
                _BaseAlloyDBAdminRestTransport._BaseListUsers._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_users(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseListUsers,
                    "_BaseListUsers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.ListUsers",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "ListUsers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._ListUsers._get_response(
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
            resp = service.ListUsersResponse()
            pb_resp = service.ListUsersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_users(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_users_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = service.ListUsersResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.list_users",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "ListUsers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _PromoteCluster(
        _BaseAlloyDBAdminRestTransport._BasePromoteCluster, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.PromoteCluster")

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
            request: service.PromoteClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the promote cluster method over HTTP.

            Args:
                request (~.service.PromoteClusterRequest):
                    The request object. Message for promoting a Cluster
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
                _BaseAlloyDBAdminRestTransport._BasePromoteCluster._get_http_options()
            )
            request, metadata = self._interceptor.pre_promote_cluster(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BasePromoteCluster,
                    "_BasePromoteCluster__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.PromoteCluster",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "PromoteCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._PromoteCluster._get_response(
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

            resp = self._interceptor.post_promote_cluster(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_promote_cluster_with_metadata(
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
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.promote_cluster",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "PromoteCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RestartInstance(
        _BaseAlloyDBAdminRestTransport._BaseRestartInstance, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.RestartInstance")

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
            request: service.RestartInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the restart instance method over HTTP.

            Args:
                request (~.service.RestartInstanceRequest):
                    The request object.
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
                _BaseAlloyDBAdminRestTransport._BaseRestartInstance._get_http_options()
            )
            request, metadata = self._interceptor.pre_restart_instance(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseRestartInstance,
                    "_BaseRestartInstance__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.RestartInstance",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "RestartInstance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._RestartInstance._get_response(
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

            resp = self._interceptor.post_restart_instance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_restart_instance_with_metadata(
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
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.restart_instance",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "RestartInstance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RestoreCluster(
        _BaseAlloyDBAdminRestTransport._BaseRestoreCluster, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.RestoreCluster")

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
            request: service.RestoreClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the restore cluster method over HTTP.

            Args:
                request (~.service.RestoreClusterRequest):
                    The request object. Message for restoring a Cluster from a backup or another
                cluster at a given point in time. NEXT_ID: 11
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
                _BaseAlloyDBAdminRestTransport._BaseRestoreCluster._get_http_options()
            )
            request, metadata = self._interceptor.pre_restore_cluster(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseRestoreCluster,
                    "_BaseRestoreCluster__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.RestoreCluster",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "RestoreCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._RestoreCluster._get_response(
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

            resp = self._interceptor.post_restore_cluster(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_restore_cluster_with_metadata(
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
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.restore_cluster",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "RestoreCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SwitchoverCluster(
        _BaseAlloyDBAdminRestTransport._BaseSwitchoverCluster, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.SwitchoverCluster")

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
            request: service.SwitchoverClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the switchover cluster method over HTTP.

            Args:
                request (~.service.SwitchoverClusterRequest):
                    The request object. Message for switching over to a
                cluster
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

            http_options = _BaseAlloyDBAdminRestTransport._BaseSwitchoverCluster._get_http_options()
            request, metadata = self._interceptor.pre_switchover_cluster(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseSwitchoverCluster,
                    "_BaseSwitchoverCluster__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.SwitchoverCluster",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "SwitchoverCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._SwitchoverCluster._get_response(
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

            resp = self._interceptor.post_switchover_cluster(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_switchover_cluster_with_metadata(
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
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.switchover_cluster",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "SwitchoverCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateBackup(
        _BaseAlloyDBAdminRestTransport._BaseUpdateBackup, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.UpdateBackup")

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
            request: service.UpdateBackupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update backup method over HTTP.

            Args:
                request (~.service.UpdateBackupRequest):
                    The request object. Message for updating a Backup
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
                _BaseAlloyDBAdminRestTransport._BaseUpdateBackup._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_backup(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseUpdateBackup,
                    "_BaseUpdateBackup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.UpdateBackup",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "UpdateBackup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._UpdateBackup._get_response(
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

            resp = self._interceptor.post_update_backup(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_backup_with_metadata(
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
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.update_backup",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "UpdateBackup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateCluster(
        _BaseAlloyDBAdminRestTransport._BaseUpdateCluster, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.UpdateCluster")

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
            request: service.UpdateClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update cluster method over HTTP.

            Args:
                request (~.service.UpdateClusterRequest):
                    The request object. Message for updating a Cluster
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
                _BaseAlloyDBAdminRestTransport._BaseUpdateCluster._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_cluster(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseUpdateCluster,
                    "_BaseUpdateCluster__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.UpdateCluster",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "UpdateCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._UpdateCluster._get_response(
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

            resp = self._interceptor.post_update_cluster(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_cluster_with_metadata(
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
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.update_cluster",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "UpdateCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateInstance(
        _BaseAlloyDBAdminRestTransport._BaseUpdateInstance, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.UpdateInstance")

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
            request: service.UpdateInstanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update instance method over HTTP.

            Args:
                request (~.service.UpdateInstanceRequest):
                    The request object. Message for updating a Instance
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
                _BaseAlloyDBAdminRestTransport._BaseUpdateInstance._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_instance(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseUpdateInstance,
                    "_BaseUpdateInstance__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.UpdateInstance",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "UpdateInstance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._UpdateInstance._get_response(
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

            resp = self._interceptor.post_update_instance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_instance_with_metadata(
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
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.update_instance",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "UpdateInstance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateUser(
        _BaseAlloyDBAdminRestTransport._BaseUpdateUser, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.UpdateUser")

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
            request: service.UpdateUserRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.User:
            r"""Call the update user method over HTTP.

            Args:
                request (~.service.UpdateUserRequest):
                    The request object. Message for updating a User
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.User:
                    Message describing User object.
            """

            http_options = (
                _BaseAlloyDBAdminRestTransport._BaseUpdateUser._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_user(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseUpdateUser,
                    "_BaseUpdateUser__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.UpdateUser",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "UpdateUser",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._UpdateUser._get_response(
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
            resp = resources.User()
            pb_resp = resources.User.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_user(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_user_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.User.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.update_user",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "UpdateUser",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpgradeCluster(
        _BaseAlloyDBAdminRestTransport._BaseUpgradeCluster, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.UpgradeCluster")

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
            request: service.UpgradeClusterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the upgrade cluster method over HTTP.

            Args:
                request (~.service.UpgradeClusterRequest):
                    The request object. Upgrades a cluster.
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
                _BaseAlloyDBAdminRestTransport._BaseUpgradeCluster._get_http_options()
            )
            request, metadata = self._interceptor.pre_upgrade_cluster(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseUpgradeCluster,
                    "_BaseUpgradeCluster__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.UpgradeCluster",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "UpgradeCluster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._UpgradeCluster._get_response(
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

            resp = self._interceptor.post_upgrade_cluster(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_upgrade_cluster_with_metadata(
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
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminClient.upgrade_cluster",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "UpgradeCluster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_create_instances(
        self,
    ) -> Callable[[service.BatchCreateInstancesRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateInstances(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_backup(
        self,
    ) -> Callable[[service.CreateBackupRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateBackup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_cluster(
        self,
    ) -> Callable[[service.CreateClusterRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateCluster(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_database(
        self,
    ) -> Callable[[service.CreateDatabaseRequest], resources.Database]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDatabase(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_instance(
        self,
    ) -> Callable[[service.CreateInstanceRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateInstance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_secondary_cluster(
        self,
    ) -> Callable[[service.CreateSecondaryClusterRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateSecondaryCluster(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_secondary_instance(
        self,
    ) -> Callable[[service.CreateSecondaryInstanceRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateSecondaryInstance(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_user(self) -> Callable[[service.CreateUserRequest], resources.User]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateUser(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_backup(
        self,
    ) -> Callable[[service.DeleteBackupRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteBackup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_cluster(
        self,
    ) -> Callable[[service.DeleteClusterRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteCluster(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_instance(
        self,
    ) -> Callable[[service.DeleteInstanceRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteInstance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_user(self) -> Callable[[service.DeleteUserRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteUser(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def execute_sql(
        self,
    ) -> Callable[[service.ExecuteSqlRequest], service.ExecuteSqlResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExecuteSql(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def export_cluster(
        self,
    ) -> Callable[[service.ExportClusterRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportCluster(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def failover_instance(
        self,
    ) -> Callable[[service.FailoverInstanceRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FailoverInstance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def generate_client_certificate(
        self,
    ) -> Callable[
        [service.GenerateClientCertificateRequest],
        service.GenerateClientCertificateResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GenerateClientCertificate(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_backup(self) -> Callable[[service.GetBackupRequest], resources.Backup]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetBackup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_cluster(self) -> Callable[[service.GetClusterRequest], resources.Cluster]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCluster(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_connection_info(
        self,
    ) -> Callable[[service.GetConnectionInfoRequest], resources.ConnectionInfo]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetConnectionInfo(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_instance(
        self,
    ) -> Callable[[service.GetInstanceRequest], resources.Instance]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetInstance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_user(self) -> Callable[[service.GetUserRequest], resources.User]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetUser(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def import_cluster(
        self,
    ) -> Callable[[service.ImportClusterRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ImportCluster(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def inject_fault(
        self,
    ) -> Callable[[service.InjectFaultRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._InjectFault(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_backups(
        self,
    ) -> Callable[[service.ListBackupsRequest], service.ListBackupsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListBackups(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_clusters(
        self,
    ) -> Callable[[service.ListClustersRequest], service.ListClustersResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListClusters(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_databases(
        self,
    ) -> Callable[[service.ListDatabasesRequest], service.ListDatabasesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDatabases(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_instances(
        self,
    ) -> Callable[[service.ListInstancesRequest], service.ListInstancesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListInstances(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_supported_database_flags(
        self,
    ) -> Callable[
        [service.ListSupportedDatabaseFlagsRequest],
        service.ListSupportedDatabaseFlagsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSupportedDatabaseFlags(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_users(
        self,
    ) -> Callable[[service.ListUsersRequest], service.ListUsersResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListUsers(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def promote_cluster(
        self,
    ) -> Callable[[service.PromoteClusterRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PromoteCluster(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def restart_instance(
        self,
    ) -> Callable[[service.RestartInstanceRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RestartInstance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def restore_cluster(
        self,
    ) -> Callable[[service.RestoreClusterRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RestoreCluster(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def switchover_cluster(
        self,
    ) -> Callable[[service.SwitchoverClusterRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SwitchoverCluster(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_backup(
        self,
    ) -> Callable[[service.UpdateBackupRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateBackup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_cluster(
        self,
    ) -> Callable[[service.UpdateClusterRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateCluster(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_instance(
        self,
    ) -> Callable[[service.UpdateInstanceRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateInstance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_user(self) -> Callable[[service.UpdateUserRequest], resources.User]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateUser(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def upgrade_cluster(
        self,
    ) -> Callable[[service.UpgradeClusterRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpgradeCluster(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseAlloyDBAdminRestTransport._BaseGetLocation, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.GetLocation")

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

            http_options = (
                _BaseAlloyDBAdminRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
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
        _BaseAlloyDBAdminRestTransport._BaseListLocations, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.ListLocations")

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

            http_options = (
                _BaseAlloyDBAdminRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
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
        _BaseAlloyDBAdminRestTransport._BaseCancelOperation, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.CancelOperation")

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
                _BaseAlloyDBAdminRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._CancelOperation._get_response(
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
    def delete_operation(self):
        return self._DeleteOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _DeleteOperation(
        _BaseAlloyDBAdminRestTransport._BaseDeleteOperation, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.DeleteOperation")

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
                _BaseAlloyDBAdminRestTransport._BaseDeleteOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._DeleteOperation._get_response(
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
        _BaseAlloyDBAdminRestTransport._BaseGetOperation, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.GetOperation")

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
                _BaseAlloyDBAdminRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
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
        _BaseAlloyDBAdminRestTransport._BaseListOperations, AlloyDBAdminRestStub
    ):
        def __hash__(self):
            return hash("AlloyDBAdminRestTransport.ListOperations")

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
                _BaseAlloyDBAdminRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseAlloyDBAdminRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.alloydb_v1beta.AlloyDBAdminClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = AlloyDBAdminRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.alloydb_v1beta.AlloyDBAdminAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.alloydb.v1beta.AlloyDBAdmin",
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


__all__ = ("AlloyDBAdminRestTransport",)
