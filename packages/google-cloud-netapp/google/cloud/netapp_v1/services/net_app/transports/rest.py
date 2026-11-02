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
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.netapp_v1._compat import transcode_request
from google.cloud.netapp_v1.types import (
    active_directory,
    backup,
    backup_policy,
    backup_vault,
    host_group,
    kms,
    ontap,
    quota_rule,
    replication,
    snapshot,
    storage_pool,
    volume,
)
from google.cloud.netapp_v1.types import active_directory as gcn_active_directory
from google.cloud.netapp_v1.types import backup as gcn_backup
from google.cloud.netapp_v1.types import backup_policy as gcn_backup_policy
from google.cloud.netapp_v1.types import backup_vault as gcn_backup_vault
from google.cloud.netapp_v1.types import host_group as gcn_host_group
from google.cloud.netapp_v1.types import quota_rule as gcn_quota_rule
from google.cloud.netapp_v1.types import replication as gcn_replication
from google.cloud.netapp_v1.types import snapshot as gcn_snapshot
from google.cloud.netapp_v1.types import storage_pool as gcn_storage_pool
from google.cloud.netapp_v1.types import volume as gcn_volume

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseNetAppRestTransport

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


class NetAppRestInterceptor:
    """Interceptor for NetApp.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the NetAppRestTransport.

    .. code-block:: python
        class MyCustomNetAppInterceptor(NetAppRestInterceptor):
            def pre_create_active_directory(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_active_directory(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_backup(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_backup(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_backup_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_backup_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_backup_vault(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_backup_vault(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_host_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_host_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_kms_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_kms_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_quota_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_quota_rule(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_replication(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_replication(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_snapshot(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_snapshot(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_storage_pool(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_storage_pool(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_volume(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_volume(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_active_directory(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_active_directory(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_backup(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_backup(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_backup_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_backup_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_backup_vault(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_backup_vault(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_host_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_host_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_kms_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_kms_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_quota_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_quota_rule(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_replication(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_replication(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_snapshot(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_snapshot(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_storage_pool(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_storage_pool(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_volume(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_volume(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_encrypt_volumes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_encrypt_volumes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_establish_peering(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_establish_peering(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_establish_volume_peering(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_establish_volume_peering(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_execute_ontap_delete(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_execute_ontap_delete(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_execute_ontap_get(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_execute_ontap_get(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_execute_ontap_patch(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_execute_ontap_patch(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_execute_ontap_post(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_execute_ontap_post(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_active_directory(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_active_directory(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_backup(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_backup(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_backup_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_backup_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_backup_vault(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_backup_vault(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_host_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_host_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_kms_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_kms_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_quota_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_quota_rule(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_replication(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_replication(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_snapshot(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_snapshot(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_split_status(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_split_status(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_storage_pool(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_storage_pool(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_volume(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_volume(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_active_directories(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_active_directories(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_backup_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_backup_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_backup_policies(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_backup_policies(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_backups(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_backups(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_backup_vaults(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_backup_vaults(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_host_groups(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_host_groups(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_kms_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_kms_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_quota_rules(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_quota_rules(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_replications(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_replications(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_snapshots(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_snapshots(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_storage_pools(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_storage_pools(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_volumes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_volumes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_restore_backup_files(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_restore_backup_files(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_restore_volume(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_restore_volume(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_resume_replication(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_resume_replication(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_reverse_replication_direction(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_reverse_replication_direction(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_revert_volume(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_revert_volume(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_start_split(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_start_split(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_stop_replication(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_stop_replication(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_switch_active_replica_zone(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_switch_active_replica_zone(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_sync_replication(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_sync_replication(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_active_directory(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_active_directory(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_backup(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_backup(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_backup_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_backup_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_backup_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_backup_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_backup_vault(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_backup_vault(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_host_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_host_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_kms_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_kms_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_quota_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_quota_rule(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_replication(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_replication(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_snapshot(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_snapshot(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_storage_pool(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_storage_pool(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_volume(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_volume(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_validate_directory_service(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_validate_directory_service(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_verify_kms_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_verify_kms_config(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = NetAppRestTransport(interceptor=MyCustomNetAppInterceptor())
        client = NetAppClient(transport=transport)


    """

    def pre_create_active_directory(
        self,
        request: gcn_active_directory.CreateActiveDirectoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_active_directory.CreateActiveDirectoryRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_active_directory

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_create_active_directory(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_active_directory

        DEPRECATED. Please use the `post_create_active_directory_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_create_active_directory` interceptor runs
        before the `post_create_active_directory_with_metadata` interceptor.
        """
        return response

    def post_create_active_directory_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_active_directory

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_create_active_directory_with_metadata`
        interceptor in new development instead of the `post_create_active_directory` interceptor.
        When both interceptors are used, this `post_create_active_directory_with_metadata` interceptor runs after the
        `post_create_active_directory` interceptor. The (possibly modified) response returned by
        `post_create_active_directory` will be passed to
        `post_create_active_directory_with_metadata`.
        """
        return response, metadata

    def pre_create_backup(
        self,
        request: gcn_backup.CreateBackupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcn_backup.CreateBackupRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_backup

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_create_backup(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_backup

        DEPRECATED. Please use the `post_create_backup_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
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
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_create_backup_with_metadata`
        interceptor in new development instead of the `post_create_backup` interceptor.
        When both interceptors are used, this `post_create_backup_with_metadata` interceptor runs after the
        `post_create_backup` interceptor. The (possibly modified) response returned by
        `post_create_backup` will be passed to
        `post_create_backup_with_metadata`.
        """
        return response, metadata

    def pre_create_backup_policy(
        self,
        request: gcn_backup_policy.CreateBackupPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_backup_policy.CreateBackupPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_backup_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_create_backup_policy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_backup_policy

        DEPRECATED. Please use the `post_create_backup_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_create_backup_policy` interceptor runs
        before the `post_create_backup_policy_with_metadata` interceptor.
        """
        return response

    def post_create_backup_policy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_backup_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_create_backup_policy_with_metadata`
        interceptor in new development instead of the `post_create_backup_policy` interceptor.
        When both interceptors are used, this `post_create_backup_policy_with_metadata` interceptor runs after the
        `post_create_backup_policy` interceptor. The (possibly modified) response returned by
        `post_create_backup_policy` will be passed to
        `post_create_backup_policy_with_metadata`.
        """
        return response, metadata

    def pre_create_backup_vault(
        self,
        request: gcn_backup_vault.CreateBackupVaultRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_backup_vault.CreateBackupVaultRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_backup_vault

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_create_backup_vault(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_backup_vault

        DEPRECATED. Please use the `post_create_backup_vault_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_create_backup_vault` interceptor runs
        before the `post_create_backup_vault_with_metadata` interceptor.
        """
        return response

    def post_create_backup_vault_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_backup_vault

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_create_backup_vault_with_metadata`
        interceptor in new development instead of the `post_create_backup_vault` interceptor.
        When both interceptors are used, this `post_create_backup_vault_with_metadata` interceptor runs after the
        `post_create_backup_vault` interceptor. The (possibly modified) response returned by
        `post_create_backup_vault` will be passed to
        `post_create_backup_vault_with_metadata`.
        """
        return response, metadata

    def pre_create_host_group(
        self,
        request: gcn_host_group.CreateHostGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_host_group.CreateHostGroupRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_host_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_create_host_group(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_host_group

        DEPRECATED. Please use the `post_create_host_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_create_host_group` interceptor runs
        before the `post_create_host_group_with_metadata` interceptor.
        """
        return response

    def post_create_host_group_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_host_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_create_host_group_with_metadata`
        interceptor in new development instead of the `post_create_host_group` interceptor.
        When both interceptors are used, this `post_create_host_group_with_metadata` interceptor runs after the
        `post_create_host_group` interceptor. The (possibly modified) response returned by
        `post_create_host_group` will be passed to
        `post_create_host_group_with_metadata`.
        """
        return response, metadata

    def pre_create_kms_config(
        self,
        request: kms.CreateKmsConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[kms.CreateKmsConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_kms_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_create_kms_config(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_kms_config

        DEPRECATED. Please use the `post_create_kms_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_create_kms_config` interceptor runs
        before the `post_create_kms_config_with_metadata` interceptor.
        """
        return response

    def post_create_kms_config_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_kms_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_create_kms_config_with_metadata`
        interceptor in new development instead of the `post_create_kms_config` interceptor.
        When both interceptors are used, this `post_create_kms_config_with_metadata` interceptor runs after the
        `post_create_kms_config` interceptor. The (possibly modified) response returned by
        `post_create_kms_config` will be passed to
        `post_create_kms_config_with_metadata`.
        """
        return response, metadata

    def pre_create_quota_rule(
        self,
        request: gcn_quota_rule.CreateQuotaRuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_quota_rule.CreateQuotaRuleRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_quota_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_create_quota_rule(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_quota_rule

        DEPRECATED. Please use the `post_create_quota_rule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_create_quota_rule` interceptor runs
        before the `post_create_quota_rule_with_metadata` interceptor.
        """
        return response

    def post_create_quota_rule_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_quota_rule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_create_quota_rule_with_metadata`
        interceptor in new development instead of the `post_create_quota_rule` interceptor.
        When both interceptors are used, this `post_create_quota_rule_with_metadata` interceptor runs after the
        `post_create_quota_rule` interceptor. The (possibly modified) response returned by
        `post_create_quota_rule` will be passed to
        `post_create_quota_rule_with_metadata`.
        """
        return response, metadata

    def pre_create_replication(
        self,
        request: gcn_replication.CreateReplicationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_replication.CreateReplicationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_replication

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_create_replication(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_replication

        DEPRECATED. Please use the `post_create_replication_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_create_replication` interceptor runs
        before the `post_create_replication_with_metadata` interceptor.
        """
        return response

    def post_create_replication_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_replication

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_create_replication_with_metadata`
        interceptor in new development instead of the `post_create_replication` interceptor.
        When both interceptors are used, this `post_create_replication_with_metadata` interceptor runs after the
        `post_create_replication` interceptor. The (possibly modified) response returned by
        `post_create_replication` will be passed to
        `post_create_replication_with_metadata`.
        """
        return response, metadata

    def pre_create_snapshot(
        self,
        request: gcn_snapshot.CreateSnapshotRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_snapshot.CreateSnapshotRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_snapshot

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_create_snapshot(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_snapshot

        DEPRECATED. Please use the `post_create_snapshot_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_create_snapshot` interceptor runs
        before the `post_create_snapshot_with_metadata` interceptor.
        """
        return response

    def post_create_snapshot_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_snapshot

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_create_snapshot_with_metadata`
        interceptor in new development instead of the `post_create_snapshot` interceptor.
        When both interceptors are used, this `post_create_snapshot_with_metadata` interceptor runs after the
        `post_create_snapshot` interceptor. The (possibly modified) response returned by
        `post_create_snapshot` will be passed to
        `post_create_snapshot_with_metadata`.
        """
        return response, metadata

    def pre_create_storage_pool(
        self,
        request: gcn_storage_pool.CreateStoragePoolRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_storage_pool.CreateStoragePoolRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_storage_pool

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_create_storage_pool(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_storage_pool

        DEPRECATED. Please use the `post_create_storage_pool_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_create_storage_pool` interceptor runs
        before the `post_create_storage_pool_with_metadata` interceptor.
        """
        return response

    def post_create_storage_pool_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_storage_pool

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_create_storage_pool_with_metadata`
        interceptor in new development instead of the `post_create_storage_pool` interceptor.
        When both interceptors are used, this `post_create_storage_pool_with_metadata` interceptor runs after the
        `post_create_storage_pool` interceptor. The (possibly modified) response returned by
        `post_create_storage_pool` will be passed to
        `post_create_storage_pool_with_metadata`.
        """
        return response, metadata

    def pre_create_volume(
        self,
        request: gcn_volume.CreateVolumeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcn_volume.CreateVolumeRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_volume

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_create_volume(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_volume

        DEPRECATED. Please use the `post_create_volume_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_create_volume` interceptor runs
        before the `post_create_volume_with_metadata` interceptor.
        """
        return response

    def post_create_volume_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_volume

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_create_volume_with_metadata`
        interceptor in new development instead of the `post_create_volume` interceptor.
        When both interceptors are used, this `post_create_volume_with_metadata` interceptor runs after the
        `post_create_volume` interceptor. The (possibly modified) response returned by
        `post_create_volume` will be passed to
        `post_create_volume_with_metadata`.
        """
        return response, metadata

    def pre_delete_active_directory(
        self,
        request: active_directory.DeleteActiveDirectoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        active_directory.DeleteActiveDirectoryRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_active_directory

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_delete_active_directory(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_active_directory

        DEPRECATED. Please use the `post_delete_active_directory_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_delete_active_directory` interceptor runs
        before the `post_delete_active_directory_with_metadata` interceptor.
        """
        return response

    def post_delete_active_directory_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_active_directory

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_delete_active_directory_with_metadata`
        interceptor in new development instead of the `post_delete_active_directory` interceptor.
        When both interceptors are used, this `post_delete_active_directory_with_metadata` interceptor runs after the
        `post_delete_active_directory` interceptor. The (possibly modified) response returned by
        `post_delete_active_directory` will be passed to
        `post_delete_active_directory_with_metadata`.
        """
        return response, metadata

    def pre_delete_backup(
        self,
        request: backup.DeleteBackupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[backup.DeleteBackupRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_backup

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_delete_backup(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_backup

        DEPRECATED. Please use the `post_delete_backup_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
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
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_delete_backup_with_metadata`
        interceptor in new development instead of the `post_delete_backup` interceptor.
        When both interceptors are used, this `post_delete_backup_with_metadata` interceptor runs after the
        `post_delete_backup` interceptor. The (possibly modified) response returned by
        `post_delete_backup` will be passed to
        `post_delete_backup_with_metadata`.
        """
        return response, metadata

    def pre_delete_backup_policy(
        self,
        request: backup_policy.DeleteBackupPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backup_policy.DeleteBackupPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_backup_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_delete_backup_policy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_backup_policy

        DEPRECATED. Please use the `post_delete_backup_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_delete_backup_policy` interceptor runs
        before the `post_delete_backup_policy_with_metadata` interceptor.
        """
        return response

    def post_delete_backup_policy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_backup_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_delete_backup_policy_with_metadata`
        interceptor in new development instead of the `post_delete_backup_policy` interceptor.
        When both interceptors are used, this `post_delete_backup_policy_with_metadata` interceptor runs after the
        `post_delete_backup_policy` interceptor. The (possibly modified) response returned by
        `post_delete_backup_policy` will be passed to
        `post_delete_backup_policy_with_metadata`.
        """
        return response, metadata

    def pre_delete_backup_vault(
        self,
        request: backup_vault.DeleteBackupVaultRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backup_vault.DeleteBackupVaultRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_backup_vault

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_delete_backup_vault(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_backup_vault

        DEPRECATED. Please use the `post_delete_backup_vault_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_delete_backup_vault` interceptor runs
        before the `post_delete_backup_vault_with_metadata` interceptor.
        """
        return response

    def post_delete_backup_vault_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_backup_vault

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_delete_backup_vault_with_metadata`
        interceptor in new development instead of the `post_delete_backup_vault` interceptor.
        When both interceptors are used, this `post_delete_backup_vault_with_metadata` interceptor runs after the
        `post_delete_backup_vault` interceptor. The (possibly modified) response returned by
        `post_delete_backup_vault` will be passed to
        `post_delete_backup_vault_with_metadata`.
        """
        return response, metadata

    def pre_delete_host_group(
        self,
        request: host_group.DeleteHostGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        host_group.DeleteHostGroupRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_host_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_delete_host_group(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_host_group

        DEPRECATED. Please use the `post_delete_host_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_delete_host_group` interceptor runs
        before the `post_delete_host_group_with_metadata` interceptor.
        """
        return response

    def post_delete_host_group_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_host_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_delete_host_group_with_metadata`
        interceptor in new development instead of the `post_delete_host_group` interceptor.
        When both interceptors are used, this `post_delete_host_group_with_metadata` interceptor runs after the
        `post_delete_host_group` interceptor. The (possibly modified) response returned by
        `post_delete_host_group` will be passed to
        `post_delete_host_group_with_metadata`.
        """
        return response, metadata

    def pre_delete_kms_config(
        self,
        request: kms.DeleteKmsConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[kms.DeleteKmsConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_kms_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_delete_kms_config(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_kms_config

        DEPRECATED. Please use the `post_delete_kms_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_delete_kms_config` interceptor runs
        before the `post_delete_kms_config_with_metadata` interceptor.
        """
        return response

    def post_delete_kms_config_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_kms_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_delete_kms_config_with_metadata`
        interceptor in new development instead of the `post_delete_kms_config` interceptor.
        When both interceptors are used, this `post_delete_kms_config_with_metadata` interceptor runs after the
        `post_delete_kms_config` interceptor. The (possibly modified) response returned by
        `post_delete_kms_config` will be passed to
        `post_delete_kms_config_with_metadata`.
        """
        return response, metadata

    def pre_delete_quota_rule(
        self,
        request: quota_rule.DeleteQuotaRuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        quota_rule.DeleteQuotaRuleRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_quota_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_delete_quota_rule(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_quota_rule

        DEPRECATED. Please use the `post_delete_quota_rule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_delete_quota_rule` interceptor runs
        before the `post_delete_quota_rule_with_metadata` interceptor.
        """
        return response

    def post_delete_quota_rule_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_quota_rule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_delete_quota_rule_with_metadata`
        interceptor in new development instead of the `post_delete_quota_rule` interceptor.
        When both interceptors are used, this `post_delete_quota_rule_with_metadata` interceptor runs after the
        `post_delete_quota_rule` interceptor. The (possibly modified) response returned by
        `post_delete_quota_rule` will be passed to
        `post_delete_quota_rule_with_metadata`.
        """
        return response, metadata

    def pre_delete_replication(
        self,
        request: replication.DeleteReplicationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        replication.DeleteReplicationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_replication

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_delete_replication(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_replication

        DEPRECATED. Please use the `post_delete_replication_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_delete_replication` interceptor runs
        before the `post_delete_replication_with_metadata` interceptor.
        """
        return response

    def post_delete_replication_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_replication

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_delete_replication_with_metadata`
        interceptor in new development instead of the `post_delete_replication` interceptor.
        When both interceptors are used, this `post_delete_replication_with_metadata` interceptor runs after the
        `post_delete_replication` interceptor. The (possibly modified) response returned by
        `post_delete_replication` will be passed to
        `post_delete_replication_with_metadata`.
        """
        return response, metadata

    def pre_delete_snapshot(
        self,
        request: snapshot.DeleteSnapshotRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[snapshot.DeleteSnapshotRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_snapshot

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_delete_snapshot(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_snapshot

        DEPRECATED. Please use the `post_delete_snapshot_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_delete_snapshot` interceptor runs
        before the `post_delete_snapshot_with_metadata` interceptor.
        """
        return response

    def post_delete_snapshot_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_snapshot

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_delete_snapshot_with_metadata`
        interceptor in new development instead of the `post_delete_snapshot` interceptor.
        When both interceptors are used, this `post_delete_snapshot_with_metadata` interceptor runs after the
        `post_delete_snapshot` interceptor. The (possibly modified) response returned by
        `post_delete_snapshot` will be passed to
        `post_delete_snapshot_with_metadata`.
        """
        return response, metadata

    def pre_delete_storage_pool(
        self,
        request: storage_pool.DeleteStoragePoolRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        storage_pool.DeleteStoragePoolRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_storage_pool

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_delete_storage_pool(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_storage_pool

        DEPRECATED. Please use the `post_delete_storage_pool_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_delete_storage_pool` interceptor runs
        before the `post_delete_storage_pool_with_metadata` interceptor.
        """
        return response

    def post_delete_storage_pool_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_storage_pool

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_delete_storage_pool_with_metadata`
        interceptor in new development instead of the `post_delete_storage_pool` interceptor.
        When both interceptors are used, this `post_delete_storage_pool_with_metadata` interceptor runs after the
        `post_delete_storage_pool` interceptor. The (possibly modified) response returned by
        `post_delete_storage_pool` will be passed to
        `post_delete_storage_pool_with_metadata`.
        """
        return response, metadata

    def pre_delete_volume(
        self,
        request: volume.DeleteVolumeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[volume.DeleteVolumeRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_volume

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_delete_volume(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_volume

        DEPRECATED. Please use the `post_delete_volume_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_delete_volume` interceptor runs
        before the `post_delete_volume_with_metadata` interceptor.
        """
        return response

    def post_delete_volume_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_volume

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_delete_volume_with_metadata`
        interceptor in new development instead of the `post_delete_volume` interceptor.
        When both interceptors are used, this `post_delete_volume_with_metadata` interceptor runs after the
        `post_delete_volume` interceptor. The (possibly modified) response returned by
        `post_delete_volume` will be passed to
        `post_delete_volume_with_metadata`.
        """
        return response, metadata

    def pre_encrypt_volumes(
        self,
        request: kms.EncryptVolumesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[kms.EncryptVolumesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for encrypt_volumes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_encrypt_volumes(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for encrypt_volumes

        DEPRECATED. Please use the `post_encrypt_volumes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_encrypt_volumes` interceptor runs
        before the `post_encrypt_volumes_with_metadata` interceptor.
        """
        return response

    def post_encrypt_volumes_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for encrypt_volumes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_encrypt_volumes_with_metadata`
        interceptor in new development instead of the `post_encrypt_volumes` interceptor.
        When both interceptors are used, this `post_encrypt_volumes_with_metadata` interceptor runs after the
        `post_encrypt_volumes` interceptor. The (possibly modified) response returned by
        `post_encrypt_volumes` will be passed to
        `post_encrypt_volumes_with_metadata`.
        """
        return response, metadata

    def pre_establish_peering(
        self,
        request: replication.EstablishPeeringRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        replication.EstablishPeeringRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for establish_peering

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_establish_peering(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for establish_peering

        DEPRECATED. Please use the `post_establish_peering_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_establish_peering` interceptor runs
        before the `post_establish_peering_with_metadata` interceptor.
        """
        return response

    def post_establish_peering_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for establish_peering

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_establish_peering_with_metadata`
        interceptor in new development instead of the `post_establish_peering` interceptor.
        When both interceptors are used, this `post_establish_peering_with_metadata` interceptor runs after the
        `post_establish_peering` interceptor. The (possibly modified) response returned by
        `post_establish_peering` will be passed to
        `post_establish_peering_with_metadata`.
        """
        return response, metadata

    def pre_establish_volume_peering(
        self,
        request: volume.EstablishVolumePeeringRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        volume.EstablishVolumePeeringRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for establish_volume_peering

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_establish_volume_peering(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for establish_volume_peering

        DEPRECATED. Please use the `post_establish_volume_peering_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_establish_volume_peering` interceptor runs
        before the `post_establish_volume_peering_with_metadata` interceptor.
        """
        return response

    def post_establish_volume_peering_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for establish_volume_peering

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_establish_volume_peering_with_metadata`
        interceptor in new development instead of the `post_establish_volume_peering` interceptor.
        When both interceptors are used, this `post_establish_volume_peering_with_metadata` interceptor runs after the
        `post_establish_volume_peering` interceptor. The (possibly modified) response returned by
        `post_establish_volume_peering` will be passed to
        `post_establish_volume_peering_with_metadata`.
        """
        return response, metadata

    def pre_execute_ontap_delete(
        self,
        request: ontap.ExecuteOntapDeleteRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ontap.ExecuteOntapDeleteRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for execute_ontap_delete

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_execute_ontap_delete(
        self, response: ontap.ExecuteOntapDeleteResponse
    ) -> ontap.ExecuteOntapDeleteResponse:
        """Post-rpc interceptor for execute_ontap_delete

        DEPRECATED. Please use the `post_execute_ontap_delete_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_execute_ontap_delete` interceptor runs
        before the `post_execute_ontap_delete_with_metadata` interceptor.
        """
        return response

    def post_execute_ontap_delete_with_metadata(
        self,
        response: ontap.ExecuteOntapDeleteResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ontap.ExecuteOntapDeleteResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for execute_ontap_delete

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_execute_ontap_delete_with_metadata`
        interceptor in new development instead of the `post_execute_ontap_delete` interceptor.
        When both interceptors are used, this `post_execute_ontap_delete_with_metadata` interceptor runs after the
        `post_execute_ontap_delete` interceptor. The (possibly modified) response returned by
        `post_execute_ontap_delete` will be passed to
        `post_execute_ontap_delete_with_metadata`.
        """
        return response, metadata

    def pre_execute_ontap_get(
        self,
        request: ontap.ExecuteOntapGetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[ontap.ExecuteOntapGetRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for execute_ontap_get

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_execute_ontap_get(
        self, response: ontap.ExecuteOntapGetResponse
    ) -> ontap.ExecuteOntapGetResponse:
        """Post-rpc interceptor for execute_ontap_get

        DEPRECATED. Please use the `post_execute_ontap_get_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_execute_ontap_get` interceptor runs
        before the `post_execute_ontap_get_with_metadata` interceptor.
        """
        return response

    def post_execute_ontap_get_with_metadata(
        self,
        response: ontap.ExecuteOntapGetResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[ontap.ExecuteOntapGetResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for execute_ontap_get

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_execute_ontap_get_with_metadata`
        interceptor in new development instead of the `post_execute_ontap_get` interceptor.
        When both interceptors are used, this `post_execute_ontap_get_with_metadata` interceptor runs after the
        `post_execute_ontap_get` interceptor. The (possibly modified) response returned by
        `post_execute_ontap_get` will be passed to
        `post_execute_ontap_get_with_metadata`.
        """
        return response, metadata

    def pre_execute_ontap_patch(
        self,
        request: ontap.ExecuteOntapPatchRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[ontap.ExecuteOntapPatchRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for execute_ontap_patch

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_execute_ontap_patch(
        self, response: ontap.ExecuteOntapPatchResponse
    ) -> ontap.ExecuteOntapPatchResponse:
        """Post-rpc interceptor for execute_ontap_patch

        DEPRECATED. Please use the `post_execute_ontap_patch_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_execute_ontap_patch` interceptor runs
        before the `post_execute_ontap_patch_with_metadata` interceptor.
        """
        return response

    def post_execute_ontap_patch_with_metadata(
        self,
        response: ontap.ExecuteOntapPatchResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        ontap.ExecuteOntapPatchResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for execute_ontap_patch

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_execute_ontap_patch_with_metadata`
        interceptor in new development instead of the `post_execute_ontap_patch` interceptor.
        When both interceptors are used, this `post_execute_ontap_patch_with_metadata` interceptor runs after the
        `post_execute_ontap_patch` interceptor. The (possibly modified) response returned by
        `post_execute_ontap_patch` will be passed to
        `post_execute_ontap_patch_with_metadata`.
        """
        return response, metadata

    def pre_execute_ontap_post(
        self,
        request: ontap.ExecuteOntapPostRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[ontap.ExecuteOntapPostRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for execute_ontap_post

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_execute_ontap_post(
        self, response: ontap.ExecuteOntapPostResponse
    ) -> ontap.ExecuteOntapPostResponse:
        """Post-rpc interceptor for execute_ontap_post

        DEPRECATED. Please use the `post_execute_ontap_post_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_execute_ontap_post` interceptor runs
        before the `post_execute_ontap_post_with_metadata` interceptor.
        """
        return response

    def post_execute_ontap_post_with_metadata(
        self,
        response: ontap.ExecuteOntapPostResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[ontap.ExecuteOntapPostResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for execute_ontap_post

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_execute_ontap_post_with_metadata`
        interceptor in new development instead of the `post_execute_ontap_post` interceptor.
        When both interceptors are used, this `post_execute_ontap_post_with_metadata` interceptor runs after the
        `post_execute_ontap_post` interceptor. The (possibly modified) response returned by
        `post_execute_ontap_post` will be passed to
        `post_execute_ontap_post_with_metadata`.
        """
        return response, metadata

    def pre_get_active_directory(
        self,
        request: active_directory.GetActiveDirectoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        active_directory.GetActiveDirectoryRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_active_directory

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_get_active_directory(
        self, response: active_directory.ActiveDirectory
    ) -> active_directory.ActiveDirectory:
        """Post-rpc interceptor for get_active_directory

        DEPRECATED. Please use the `post_get_active_directory_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_get_active_directory` interceptor runs
        before the `post_get_active_directory_with_metadata` interceptor.
        """
        return response

    def post_get_active_directory_with_metadata(
        self,
        response: active_directory.ActiveDirectory,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        active_directory.ActiveDirectory, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_active_directory

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_get_active_directory_with_metadata`
        interceptor in new development instead of the `post_get_active_directory` interceptor.
        When both interceptors are used, this `post_get_active_directory_with_metadata` interceptor runs after the
        `post_get_active_directory` interceptor. The (possibly modified) response returned by
        `post_get_active_directory` will be passed to
        `post_get_active_directory_with_metadata`.
        """
        return response, metadata

    def pre_get_backup(
        self,
        request: backup.GetBackupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[backup.GetBackupRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_backup

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_get_backup(self, response: backup.Backup) -> backup.Backup:
        """Post-rpc interceptor for get_backup

        DEPRECATED. Please use the `post_get_backup_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_get_backup` interceptor runs
        before the `post_get_backup_with_metadata` interceptor.
        """
        return response

    def post_get_backup_with_metadata(
        self, response: backup.Backup, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[backup.Backup, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_backup

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_get_backup_with_metadata`
        interceptor in new development instead of the `post_get_backup` interceptor.
        When both interceptors are used, this `post_get_backup_with_metadata` interceptor runs after the
        `post_get_backup` interceptor. The (possibly modified) response returned by
        `post_get_backup` will be passed to
        `post_get_backup_with_metadata`.
        """
        return response, metadata

    def pre_get_backup_policy(
        self,
        request: backup_policy.GetBackupPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backup_policy.GetBackupPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_backup_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_get_backup_policy(
        self, response: backup_policy.BackupPolicy
    ) -> backup_policy.BackupPolicy:
        """Post-rpc interceptor for get_backup_policy

        DEPRECATED. Please use the `post_get_backup_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_get_backup_policy` interceptor runs
        before the `post_get_backup_policy_with_metadata` interceptor.
        """
        return response

    def post_get_backup_policy_with_metadata(
        self,
        response: backup_policy.BackupPolicy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[backup_policy.BackupPolicy, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_backup_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_get_backup_policy_with_metadata`
        interceptor in new development instead of the `post_get_backup_policy` interceptor.
        When both interceptors are used, this `post_get_backup_policy_with_metadata` interceptor runs after the
        `post_get_backup_policy` interceptor. The (possibly modified) response returned by
        `post_get_backup_policy` will be passed to
        `post_get_backup_policy_with_metadata`.
        """
        return response, metadata

    def pre_get_backup_vault(
        self,
        request: backup_vault.GetBackupVaultRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backup_vault.GetBackupVaultRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_backup_vault

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_get_backup_vault(
        self, response: backup_vault.BackupVault
    ) -> backup_vault.BackupVault:
        """Post-rpc interceptor for get_backup_vault

        DEPRECATED. Please use the `post_get_backup_vault_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_get_backup_vault` interceptor runs
        before the `post_get_backup_vault_with_metadata` interceptor.
        """
        return response

    def post_get_backup_vault_with_metadata(
        self,
        response: backup_vault.BackupVault,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[backup_vault.BackupVault, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_backup_vault

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_get_backup_vault_with_metadata`
        interceptor in new development instead of the `post_get_backup_vault` interceptor.
        When both interceptors are used, this `post_get_backup_vault_with_metadata` interceptor runs after the
        `post_get_backup_vault` interceptor. The (possibly modified) response returned by
        `post_get_backup_vault` will be passed to
        `post_get_backup_vault_with_metadata`.
        """
        return response, metadata

    def pre_get_host_group(
        self,
        request: host_group.GetHostGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[host_group.GetHostGroupRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_host_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_get_host_group(
        self, response: host_group.HostGroup
    ) -> host_group.HostGroup:
        """Post-rpc interceptor for get_host_group

        DEPRECATED. Please use the `post_get_host_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_get_host_group` interceptor runs
        before the `post_get_host_group_with_metadata` interceptor.
        """
        return response

    def post_get_host_group_with_metadata(
        self,
        response: host_group.HostGroup,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[host_group.HostGroup, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_host_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_get_host_group_with_metadata`
        interceptor in new development instead of the `post_get_host_group` interceptor.
        When both interceptors are used, this `post_get_host_group_with_metadata` interceptor runs after the
        `post_get_host_group` interceptor. The (possibly modified) response returned by
        `post_get_host_group` will be passed to
        `post_get_host_group_with_metadata`.
        """
        return response, metadata

    def pre_get_kms_config(
        self,
        request: kms.GetKmsConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[kms.GetKmsConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_kms_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_get_kms_config(self, response: kms.KmsConfig) -> kms.KmsConfig:
        """Post-rpc interceptor for get_kms_config

        DEPRECATED. Please use the `post_get_kms_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_get_kms_config` interceptor runs
        before the `post_get_kms_config_with_metadata` interceptor.
        """
        return response

    def post_get_kms_config_with_metadata(
        self, response: kms.KmsConfig, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[kms.KmsConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_kms_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_get_kms_config_with_metadata`
        interceptor in new development instead of the `post_get_kms_config` interceptor.
        When both interceptors are used, this `post_get_kms_config_with_metadata` interceptor runs after the
        `post_get_kms_config` interceptor. The (possibly modified) response returned by
        `post_get_kms_config` will be passed to
        `post_get_kms_config_with_metadata`.
        """
        return response, metadata

    def pre_get_quota_rule(
        self,
        request: quota_rule.GetQuotaRuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[quota_rule.GetQuotaRuleRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_quota_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_get_quota_rule(
        self, response: quota_rule.QuotaRule
    ) -> quota_rule.QuotaRule:
        """Post-rpc interceptor for get_quota_rule

        DEPRECATED. Please use the `post_get_quota_rule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_get_quota_rule` interceptor runs
        before the `post_get_quota_rule_with_metadata` interceptor.
        """
        return response

    def post_get_quota_rule_with_metadata(
        self,
        response: quota_rule.QuotaRule,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[quota_rule.QuotaRule, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_quota_rule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_get_quota_rule_with_metadata`
        interceptor in new development instead of the `post_get_quota_rule` interceptor.
        When both interceptors are used, this `post_get_quota_rule_with_metadata` interceptor runs after the
        `post_get_quota_rule` interceptor. The (possibly modified) response returned by
        `post_get_quota_rule` will be passed to
        `post_get_quota_rule_with_metadata`.
        """
        return response, metadata

    def pre_get_replication(
        self,
        request: replication.GetReplicationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        replication.GetReplicationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_replication

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_get_replication(
        self, response: replication.Replication
    ) -> replication.Replication:
        """Post-rpc interceptor for get_replication

        DEPRECATED. Please use the `post_get_replication_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_get_replication` interceptor runs
        before the `post_get_replication_with_metadata` interceptor.
        """
        return response

    def post_get_replication_with_metadata(
        self,
        response: replication.Replication,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[replication.Replication, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_replication

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_get_replication_with_metadata`
        interceptor in new development instead of the `post_get_replication` interceptor.
        When both interceptors are used, this `post_get_replication_with_metadata` interceptor runs after the
        `post_get_replication` interceptor. The (possibly modified) response returned by
        `post_get_replication` will be passed to
        `post_get_replication_with_metadata`.
        """
        return response, metadata

    def pre_get_snapshot(
        self,
        request: snapshot.GetSnapshotRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[snapshot.GetSnapshotRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_snapshot

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_get_snapshot(self, response: snapshot.Snapshot) -> snapshot.Snapshot:
        """Post-rpc interceptor for get_snapshot

        DEPRECATED. Please use the `post_get_snapshot_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_get_snapshot` interceptor runs
        before the `post_get_snapshot_with_metadata` interceptor.
        """
        return response

    def post_get_snapshot_with_metadata(
        self,
        response: snapshot.Snapshot,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[snapshot.Snapshot, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_snapshot

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_get_snapshot_with_metadata`
        interceptor in new development instead of the `post_get_snapshot` interceptor.
        When both interceptors are used, this `post_get_snapshot_with_metadata` interceptor runs after the
        `post_get_snapshot` interceptor. The (possibly modified) response returned by
        `post_get_snapshot` will be passed to
        `post_get_snapshot_with_metadata`.
        """
        return response, metadata

    def pre_get_split_status(
        self,
        request: volume.GetSplitStatusRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[volume.GetSplitStatusRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_split_status

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_get_split_status(self, response: volume.SplitStatus) -> volume.SplitStatus:
        """Post-rpc interceptor for get_split_status

        DEPRECATED. Please use the `post_get_split_status_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_get_split_status` interceptor runs
        before the `post_get_split_status_with_metadata` interceptor.
        """
        return response

    def post_get_split_status_with_metadata(
        self,
        response: volume.SplitStatus,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[volume.SplitStatus, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_split_status

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_get_split_status_with_metadata`
        interceptor in new development instead of the `post_get_split_status` interceptor.
        When both interceptors are used, this `post_get_split_status_with_metadata` interceptor runs after the
        `post_get_split_status` interceptor. The (possibly modified) response returned by
        `post_get_split_status` will be passed to
        `post_get_split_status_with_metadata`.
        """
        return response, metadata

    def pre_get_storage_pool(
        self,
        request: storage_pool.GetStoragePoolRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        storage_pool.GetStoragePoolRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_storage_pool

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_get_storage_pool(
        self, response: storage_pool.StoragePool
    ) -> storage_pool.StoragePool:
        """Post-rpc interceptor for get_storage_pool

        DEPRECATED. Please use the `post_get_storage_pool_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_get_storage_pool` interceptor runs
        before the `post_get_storage_pool_with_metadata` interceptor.
        """
        return response

    def post_get_storage_pool_with_metadata(
        self,
        response: storage_pool.StoragePool,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[storage_pool.StoragePool, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_storage_pool

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_get_storage_pool_with_metadata`
        interceptor in new development instead of the `post_get_storage_pool` interceptor.
        When both interceptors are used, this `post_get_storage_pool_with_metadata` interceptor runs after the
        `post_get_storage_pool` interceptor. The (possibly modified) response returned by
        `post_get_storage_pool` will be passed to
        `post_get_storage_pool_with_metadata`.
        """
        return response, metadata

    def pre_get_volume(
        self,
        request: volume.GetVolumeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[volume.GetVolumeRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_volume

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_get_volume(self, response: volume.Volume) -> volume.Volume:
        """Post-rpc interceptor for get_volume

        DEPRECATED. Please use the `post_get_volume_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_get_volume` interceptor runs
        before the `post_get_volume_with_metadata` interceptor.
        """
        return response

    def post_get_volume_with_metadata(
        self, response: volume.Volume, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[volume.Volume, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_volume

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_get_volume_with_metadata`
        interceptor in new development instead of the `post_get_volume` interceptor.
        When both interceptors are used, this `post_get_volume_with_metadata` interceptor runs after the
        `post_get_volume` interceptor. The (possibly modified) response returned by
        `post_get_volume` will be passed to
        `post_get_volume_with_metadata`.
        """
        return response, metadata

    def pre_list_active_directories(
        self,
        request: active_directory.ListActiveDirectoriesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        active_directory.ListActiveDirectoriesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_active_directories

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_list_active_directories(
        self, response: active_directory.ListActiveDirectoriesResponse
    ) -> active_directory.ListActiveDirectoriesResponse:
        """Post-rpc interceptor for list_active_directories

        DEPRECATED. Please use the `post_list_active_directories_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_list_active_directories` interceptor runs
        before the `post_list_active_directories_with_metadata` interceptor.
        """
        return response

    def post_list_active_directories_with_metadata(
        self,
        response: active_directory.ListActiveDirectoriesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        active_directory.ListActiveDirectoriesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_active_directories

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_list_active_directories_with_metadata`
        interceptor in new development instead of the `post_list_active_directories` interceptor.
        When both interceptors are used, this `post_list_active_directories_with_metadata` interceptor runs after the
        `post_list_active_directories` interceptor. The (possibly modified) response returned by
        `post_list_active_directories` will be passed to
        `post_list_active_directories_with_metadata`.
        """
        return response, metadata

    def pre_list_backup_configs(
        self,
        request: volume.ListBackupConfigsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        volume.ListBackupConfigsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_backup_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_list_backup_configs(
        self, response: volume.ListBackupConfigsResponse
    ) -> volume.ListBackupConfigsResponse:
        """Post-rpc interceptor for list_backup_configs

        DEPRECATED. Please use the `post_list_backup_configs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_list_backup_configs` interceptor runs
        before the `post_list_backup_configs_with_metadata` interceptor.
        """
        return response

    def post_list_backup_configs_with_metadata(
        self,
        response: volume.ListBackupConfigsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        volume.ListBackupConfigsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_backup_configs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_list_backup_configs_with_metadata`
        interceptor in new development instead of the `post_list_backup_configs` interceptor.
        When both interceptors are used, this `post_list_backup_configs_with_metadata` interceptor runs after the
        `post_list_backup_configs` interceptor. The (possibly modified) response returned by
        `post_list_backup_configs` will be passed to
        `post_list_backup_configs_with_metadata`.
        """
        return response, metadata

    def pre_list_backup_policies(
        self,
        request: backup_policy.ListBackupPoliciesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backup_policy.ListBackupPoliciesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_backup_policies

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_list_backup_policies(
        self, response: backup_policy.ListBackupPoliciesResponse
    ) -> backup_policy.ListBackupPoliciesResponse:
        """Post-rpc interceptor for list_backup_policies

        DEPRECATED. Please use the `post_list_backup_policies_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_list_backup_policies` interceptor runs
        before the `post_list_backup_policies_with_metadata` interceptor.
        """
        return response

    def post_list_backup_policies_with_metadata(
        self,
        response: backup_policy.ListBackupPoliciesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backup_policy.ListBackupPoliciesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_backup_policies

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_list_backup_policies_with_metadata`
        interceptor in new development instead of the `post_list_backup_policies` interceptor.
        When both interceptors are used, this `post_list_backup_policies_with_metadata` interceptor runs after the
        `post_list_backup_policies` interceptor. The (possibly modified) response returned by
        `post_list_backup_policies` will be passed to
        `post_list_backup_policies_with_metadata`.
        """
        return response, metadata

    def pre_list_backups(
        self,
        request: backup.ListBackupsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[backup.ListBackupsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_backups

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_list_backups(
        self, response: backup.ListBackupsResponse
    ) -> backup.ListBackupsResponse:
        """Post-rpc interceptor for list_backups

        DEPRECATED. Please use the `post_list_backups_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_list_backups` interceptor runs
        before the `post_list_backups_with_metadata` interceptor.
        """
        return response

    def post_list_backups_with_metadata(
        self,
        response: backup.ListBackupsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[backup.ListBackupsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_backups

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_list_backups_with_metadata`
        interceptor in new development instead of the `post_list_backups` interceptor.
        When both interceptors are used, this `post_list_backups_with_metadata` interceptor runs after the
        `post_list_backups` interceptor. The (possibly modified) response returned by
        `post_list_backups` will be passed to
        `post_list_backups_with_metadata`.
        """
        return response, metadata

    def pre_list_backup_vaults(
        self,
        request: backup_vault.ListBackupVaultsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backup_vault.ListBackupVaultsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_backup_vaults

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_list_backup_vaults(
        self, response: backup_vault.ListBackupVaultsResponse
    ) -> backup_vault.ListBackupVaultsResponse:
        """Post-rpc interceptor for list_backup_vaults

        DEPRECATED. Please use the `post_list_backup_vaults_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_list_backup_vaults` interceptor runs
        before the `post_list_backup_vaults_with_metadata` interceptor.
        """
        return response

    def post_list_backup_vaults_with_metadata(
        self,
        response: backup_vault.ListBackupVaultsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backup_vault.ListBackupVaultsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_backup_vaults

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_list_backup_vaults_with_metadata`
        interceptor in new development instead of the `post_list_backup_vaults` interceptor.
        When both interceptors are used, this `post_list_backup_vaults_with_metadata` interceptor runs after the
        `post_list_backup_vaults` interceptor. The (possibly modified) response returned by
        `post_list_backup_vaults` will be passed to
        `post_list_backup_vaults_with_metadata`.
        """
        return response, metadata

    def pre_list_host_groups(
        self,
        request: host_group.ListHostGroupsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        host_group.ListHostGroupsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_host_groups

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_list_host_groups(
        self, response: host_group.ListHostGroupsResponse
    ) -> host_group.ListHostGroupsResponse:
        """Post-rpc interceptor for list_host_groups

        DEPRECATED. Please use the `post_list_host_groups_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_list_host_groups` interceptor runs
        before the `post_list_host_groups_with_metadata` interceptor.
        """
        return response

    def post_list_host_groups_with_metadata(
        self,
        response: host_group.ListHostGroupsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        host_group.ListHostGroupsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_host_groups

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_list_host_groups_with_metadata`
        interceptor in new development instead of the `post_list_host_groups` interceptor.
        When both interceptors are used, this `post_list_host_groups_with_metadata` interceptor runs after the
        `post_list_host_groups` interceptor. The (possibly modified) response returned by
        `post_list_host_groups` will be passed to
        `post_list_host_groups_with_metadata`.
        """
        return response, metadata

    def pre_list_kms_configs(
        self,
        request: kms.ListKmsConfigsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[kms.ListKmsConfigsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_kms_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_list_kms_configs(
        self, response: kms.ListKmsConfigsResponse
    ) -> kms.ListKmsConfigsResponse:
        """Post-rpc interceptor for list_kms_configs

        DEPRECATED. Please use the `post_list_kms_configs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_list_kms_configs` interceptor runs
        before the `post_list_kms_configs_with_metadata` interceptor.
        """
        return response

    def post_list_kms_configs_with_metadata(
        self,
        response: kms.ListKmsConfigsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[kms.ListKmsConfigsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_kms_configs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_list_kms_configs_with_metadata`
        interceptor in new development instead of the `post_list_kms_configs` interceptor.
        When both interceptors are used, this `post_list_kms_configs_with_metadata` interceptor runs after the
        `post_list_kms_configs` interceptor. The (possibly modified) response returned by
        `post_list_kms_configs` will be passed to
        `post_list_kms_configs_with_metadata`.
        """
        return response, metadata

    def pre_list_quota_rules(
        self,
        request: quota_rule.ListQuotaRulesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        quota_rule.ListQuotaRulesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_quota_rules

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_list_quota_rules(
        self, response: quota_rule.ListQuotaRulesResponse
    ) -> quota_rule.ListQuotaRulesResponse:
        """Post-rpc interceptor for list_quota_rules

        DEPRECATED. Please use the `post_list_quota_rules_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_list_quota_rules` interceptor runs
        before the `post_list_quota_rules_with_metadata` interceptor.
        """
        return response

    def post_list_quota_rules_with_metadata(
        self,
        response: quota_rule.ListQuotaRulesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        quota_rule.ListQuotaRulesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_quota_rules

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_list_quota_rules_with_metadata`
        interceptor in new development instead of the `post_list_quota_rules` interceptor.
        When both interceptors are used, this `post_list_quota_rules_with_metadata` interceptor runs after the
        `post_list_quota_rules` interceptor. The (possibly modified) response returned by
        `post_list_quota_rules` will be passed to
        `post_list_quota_rules_with_metadata`.
        """
        return response, metadata

    def pre_list_replications(
        self,
        request: replication.ListReplicationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        replication.ListReplicationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_replications

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_list_replications(
        self, response: replication.ListReplicationsResponse
    ) -> replication.ListReplicationsResponse:
        """Post-rpc interceptor for list_replications

        DEPRECATED. Please use the `post_list_replications_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_list_replications` interceptor runs
        before the `post_list_replications_with_metadata` interceptor.
        """
        return response

    def post_list_replications_with_metadata(
        self,
        response: replication.ListReplicationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        replication.ListReplicationsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_replications

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_list_replications_with_metadata`
        interceptor in new development instead of the `post_list_replications` interceptor.
        When both interceptors are used, this `post_list_replications_with_metadata` interceptor runs after the
        `post_list_replications` interceptor. The (possibly modified) response returned by
        `post_list_replications` will be passed to
        `post_list_replications_with_metadata`.
        """
        return response, metadata

    def pre_list_snapshots(
        self,
        request: snapshot.ListSnapshotsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[snapshot.ListSnapshotsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_snapshots

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_list_snapshots(
        self, response: snapshot.ListSnapshotsResponse
    ) -> snapshot.ListSnapshotsResponse:
        """Post-rpc interceptor for list_snapshots

        DEPRECATED. Please use the `post_list_snapshots_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_list_snapshots` interceptor runs
        before the `post_list_snapshots_with_metadata` interceptor.
        """
        return response

    def post_list_snapshots_with_metadata(
        self,
        response: snapshot.ListSnapshotsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[snapshot.ListSnapshotsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_snapshots

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_list_snapshots_with_metadata`
        interceptor in new development instead of the `post_list_snapshots` interceptor.
        When both interceptors are used, this `post_list_snapshots_with_metadata` interceptor runs after the
        `post_list_snapshots` interceptor. The (possibly modified) response returned by
        `post_list_snapshots` will be passed to
        `post_list_snapshots_with_metadata`.
        """
        return response, metadata

    def pre_list_storage_pools(
        self,
        request: storage_pool.ListStoragePoolsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        storage_pool.ListStoragePoolsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_storage_pools

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_list_storage_pools(
        self, response: storage_pool.ListStoragePoolsResponse
    ) -> storage_pool.ListStoragePoolsResponse:
        """Post-rpc interceptor for list_storage_pools

        DEPRECATED. Please use the `post_list_storage_pools_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_list_storage_pools` interceptor runs
        before the `post_list_storage_pools_with_metadata` interceptor.
        """
        return response

    def post_list_storage_pools_with_metadata(
        self,
        response: storage_pool.ListStoragePoolsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        storage_pool.ListStoragePoolsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_storage_pools

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_list_storage_pools_with_metadata`
        interceptor in new development instead of the `post_list_storage_pools` interceptor.
        When both interceptors are used, this `post_list_storage_pools_with_metadata` interceptor runs after the
        `post_list_storage_pools` interceptor. The (possibly modified) response returned by
        `post_list_storage_pools` will be passed to
        `post_list_storage_pools_with_metadata`.
        """
        return response, metadata

    def pre_list_volumes(
        self,
        request: volume.ListVolumesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[volume.ListVolumesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_volumes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_list_volumes(
        self, response: volume.ListVolumesResponse
    ) -> volume.ListVolumesResponse:
        """Post-rpc interceptor for list_volumes

        DEPRECATED. Please use the `post_list_volumes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_list_volumes` interceptor runs
        before the `post_list_volumes_with_metadata` interceptor.
        """
        return response

    def post_list_volumes_with_metadata(
        self,
        response: volume.ListVolumesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[volume.ListVolumesResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_volumes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_list_volumes_with_metadata`
        interceptor in new development instead of the `post_list_volumes` interceptor.
        When both interceptors are used, this `post_list_volumes_with_metadata` interceptor runs after the
        `post_list_volumes` interceptor. The (possibly modified) response returned by
        `post_list_volumes` will be passed to
        `post_list_volumes_with_metadata`.
        """
        return response, metadata

    def pre_restore_backup_files(
        self,
        request: volume.RestoreBackupFilesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        volume.RestoreBackupFilesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for restore_backup_files

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_restore_backup_files(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for restore_backup_files

        DEPRECATED. Please use the `post_restore_backup_files_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_restore_backup_files` interceptor runs
        before the `post_restore_backup_files_with_metadata` interceptor.
        """
        return response

    def post_restore_backup_files_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for restore_backup_files

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_restore_backup_files_with_metadata`
        interceptor in new development instead of the `post_restore_backup_files` interceptor.
        When both interceptors are used, this `post_restore_backup_files_with_metadata` interceptor runs after the
        `post_restore_backup_files` interceptor. The (possibly modified) response returned by
        `post_restore_backup_files` will be passed to
        `post_restore_backup_files_with_metadata`.
        """
        return response, metadata

    def pre_restore_volume(
        self,
        request: volume.RestoreVolumeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[volume.RestoreVolumeRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for restore_volume

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_restore_volume(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for restore_volume

        DEPRECATED. Please use the `post_restore_volume_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_restore_volume` interceptor runs
        before the `post_restore_volume_with_metadata` interceptor.
        """
        return response

    def post_restore_volume_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for restore_volume

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_restore_volume_with_metadata`
        interceptor in new development instead of the `post_restore_volume` interceptor.
        When both interceptors are used, this `post_restore_volume_with_metadata` interceptor runs after the
        `post_restore_volume` interceptor. The (possibly modified) response returned by
        `post_restore_volume` will be passed to
        `post_restore_volume_with_metadata`.
        """
        return response, metadata

    def pre_resume_replication(
        self,
        request: replication.ResumeReplicationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        replication.ResumeReplicationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for resume_replication

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_resume_replication(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for resume_replication

        DEPRECATED. Please use the `post_resume_replication_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_resume_replication` interceptor runs
        before the `post_resume_replication_with_metadata` interceptor.
        """
        return response

    def post_resume_replication_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for resume_replication

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_resume_replication_with_metadata`
        interceptor in new development instead of the `post_resume_replication` interceptor.
        When both interceptors are used, this `post_resume_replication_with_metadata` interceptor runs after the
        `post_resume_replication` interceptor. The (possibly modified) response returned by
        `post_resume_replication` will be passed to
        `post_resume_replication_with_metadata`.
        """
        return response, metadata

    def pre_reverse_replication_direction(
        self,
        request: replication.ReverseReplicationDirectionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        replication.ReverseReplicationDirectionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for reverse_replication_direction

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_reverse_replication_direction(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for reverse_replication_direction

        DEPRECATED. Please use the `post_reverse_replication_direction_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_reverse_replication_direction` interceptor runs
        before the `post_reverse_replication_direction_with_metadata` interceptor.
        """
        return response

    def post_reverse_replication_direction_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for reverse_replication_direction

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_reverse_replication_direction_with_metadata`
        interceptor in new development instead of the `post_reverse_replication_direction` interceptor.
        When both interceptors are used, this `post_reverse_replication_direction_with_metadata` interceptor runs after the
        `post_reverse_replication_direction` interceptor. The (possibly modified) response returned by
        `post_reverse_replication_direction` will be passed to
        `post_reverse_replication_direction_with_metadata`.
        """
        return response, metadata

    def pre_revert_volume(
        self,
        request: volume.RevertVolumeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[volume.RevertVolumeRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for revert_volume

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_revert_volume(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for revert_volume

        DEPRECATED. Please use the `post_revert_volume_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_revert_volume` interceptor runs
        before the `post_revert_volume_with_metadata` interceptor.
        """
        return response

    def post_revert_volume_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for revert_volume

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_revert_volume_with_metadata`
        interceptor in new development instead of the `post_revert_volume` interceptor.
        When both interceptors are used, this `post_revert_volume_with_metadata` interceptor runs after the
        `post_revert_volume` interceptor. The (possibly modified) response returned by
        `post_revert_volume` will be passed to
        `post_revert_volume_with_metadata`.
        """
        return response, metadata

    def pre_start_split(
        self,
        request: volume.StartSplitRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[volume.StartSplitRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for start_split

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_start_split(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for start_split

        DEPRECATED. Please use the `post_start_split_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_start_split` interceptor runs
        before the `post_start_split_with_metadata` interceptor.
        """
        return response

    def post_start_split_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for start_split

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_start_split_with_metadata`
        interceptor in new development instead of the `post_start_split` interceptor.
        When both interceptors are used, this `post_start_split_with_metadata` interceptor runs after the
        `post_start_split` interceptor. The (possibly modified) response returned by
        `post_start_split` will be passed to
        `post_start_split_with_metadata`.
        """
        return response, metadata

    def pre_stop_replication(
        self,
        request: replication.StopReplicationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        replication.StopReplicationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for stop_replication

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_stop_replication(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for stop_replication

        DEPRECATED. Please use the `post_stop_replication_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_stop_replication` interceptor runs
        before the `post_stop_replication_with_metadata` interceptor.
        """
        return response

    def post_stop_replication_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for stop_replication

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_stop_replication_with_metadata`
        interceptor in new development instead of the `post_stop_replication` interceptor.
        When both interceptors are used, this `post_stop_replication_with_metadata` interceptor runs after the
        `post_stop_replication` interceptor. The (possibly modified) response returned by
        `post_stop_replication` will be passed to
        `post_stop_replication_with_metadata`.
        """
        return response, metadata

    def pre_switch_active_replica_zone(
        self,
        request: storage_pool.SwitchActiveReplicaZoneRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        storage_pool.SwitchActiveReplicaZoneRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for switch_active_replica_zone

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_switch_active_replica_zone(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for switch_active_replica_zone

        DEPRECATED. Please use the `post_switch_active_replica_zone_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_switch_active_replica_zone` interceptor runs
        before the `post_switch_active_replica_zone_with_metadata` interceptor.
        """
        return response

    def post_switch_active_replica_zone_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for switch_active_replica_zone

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_switch_active_replica_zone_with_metadata`
        interceptor in new development instead of the `post_switch_active_replica_zone` interceptor.
        When both interceptors are used, this `post_switch_active_replica_zone_with_metadata` interceptor runs after the
        `post_switch_active_replica_zone` interceptor. The (possibly modified) response returned by
        `post_switch_active_replica_zone` will be passed to
        `post_switch_active_replica_zone_with_metadata`.
        """
        return response, metadata

    def pre_sync_replication(
        self,
        request: replication.SyncReplicationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        replication.SyncReplicationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for sync_replication

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_sync_replication(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for sync_replication

        DEPRECATED. Please use the `post_sync_replication_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_sync_replication` interceptor runs
        before the `post_sync_replication_with_metadata` interceptor.
        """
        return response

    def post_sync_replication_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for sync_replication

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_sync_replication_with_metadata`
        interceptor in new development instead of the `post_sync_replication` interceptor.
        When both interceptors are used, this `post_sync_replication_with_metadata` interceptor runs after the
        `post_sync_replication` interceptor. The (possibly modified) response returned by
        `post_sync_replication` will be passed to
        `post_sync_replication_with_metadata`.
        """
        return response, metadata

    def pre_update_active_directory(
        self,
        request: gcn_active_directory.UpdateActiveDirectoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_active_directory.UpdateActiveDirectoryRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_active_directory

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_update_active_directory(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_active_directory

        DEPRECATED. Please use the `post_update_active_directory_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_update_active_directory` interceptor runs
        before the `post_update_active_directory_with_metadata` interceptor.
        """
        return response

    def post_update_active_directory_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_active_directory

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_update_active_directory_with_metadata`
        interceptor in new development instead of the `post_update_active_directory` interceptor.
        When both interceptors are used, this `post_update_active_directory_with_metadata` interceptor runs after the
        `post_update_active_directory` interceptor. The (possibly modified) response returned by
        `post_update_active_directory` will be passed to
        `post_update_active_directory_with_metadata`.
        """
        return response, metadata

    def pre_update_backup(
        self,
        request: gcn_backup.UpdateBackupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcn_backup.UpdateBackupRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_backup

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_update_backup(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_backup

        DEPRECATED. Please use the `post_update_backup_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
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
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_update_backup_with_metadata`
        interceptor in new development instead of the `post_update_backup` interceptor.
        When both interceptors are used, this `post_update_backup_with_metadata` interceptor runs after the
        `post_update_backup` interceptor. The (possibly modified) response returned by
        `post_update_backup` will be passed to
        `post_update_backup_with_metadata`.
        """
        return response, metadata

    def pre_update_backup_config(
        self,
        request: volume.UpdateBackupConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        volume.UpdateBackupConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_backup_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_update_backup_config(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_backup_config

        DEPRECATED. Please use the `post_update_backup_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_update_backup_config` interceptor runs
        before the `post_update_backup_config_with_metadata` interceptor.
        """
        return response

    def post_update_backup_config_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_backup_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_update_backup_config_with_metadata`
        interceptor in new development instead of the `post_update_backup_config` interceptor.
        When both interceptors are used, this `post_update_backup_config_with_metadata` interceptor runs after the
        `post_update_backup_config` interceptor. The (possibly modified) response returned by
        `post_update_backup_config` will be passed to
        `post_update_backup_config_with_metadata`.
        """
        return response, metadata

    def pre_update_backup_policy(
        self,
        request: gcn_backup_policy.UpdateBackupPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_backup_policy.UpdateBackupPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_backup_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_update_backup_policy(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_backup_policy

        DEPRECATED. Please use the `post_update_backup_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_update_backup_policy` interceptor runs
        before the `post_update_backup_policy_with_metadata` interceptor.
        """
        return response

    def post_update_backup_policy_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_backup_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_update_backup_policy_with_metadata`
        interceptor in new development instead of the `post_update_backup_policy` interceptor.
        When both interceptors are used, this `post_update_backup_policy_with_metadata` interceptor runs after the
        `post_update_backup_policy` interceptor. The (possibly modified) response returned by
        `post_update_backup_policy` will be passed to
        `post_update_backup_policy_with_metadata`.
        """
        return response, metadata

    def pre_update_backup_vault(
        self,
        request: gcn_backup_vault.UpdateBackupVaultRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_backup_vault.UpdateBackupVaultRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_backup_vault

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_update_backup_vault(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_backup_vault

        DEPRECATED. Please use the `post_update_backup_vault_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_update_backup_vault` interceptor runs
        before the `post_update_backup_vault_with_metadata` interceptor.
        """
        return response

    def post_update_backup_vault_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_backup_vault

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_update_backup_vault_with_metadata`
        interceptor in new development instead of the `post_update_backup_vault` interceptor.
        When both interceptors are used, this `post_update_backup_vault_with_metadata` interceptor runs after the
        `post_update_backup_vault` interceptor. The (possibly modified) response returned by
        `post_update_backup_vault` will be passed to
        `post_update_backup_vault_with_metadata`.
        """
        return response, metadata

    def pre_update_host_group(
        self,
        request: gcn_host_group.UpdateHostGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_host_group.UpdateHostGroupRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_host_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_update_host_group(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_host_group

        DEPRECATED. Please use the `post_update_host_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_update_host_group` interceptor runs
        before the `post_update_host_group_with_metadata` interceptor.
        """
        return response

    def post_update_host_group_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_host_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_update_host_group_with_metadata`
        interceptor in new development instead of the `post_update_host_group` interceptor.
        When both interceptors are used, this `post_update_host_group_with_metadata` interceptor runs after the
        `post_update_host_group` interceptor. The (possibly modified) response returned by
        `post_update_host_group` will be passed to
        `post_update_host_group_with_metadata`.
        """
        return response, metadata

    def pre_update_kms_config(
        self,
        request: kms.UpdateKmsConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[kms.UpdateKmsConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_kms_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_update_kms_config(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_kms_config

        DEPRECATED. Please use the `post_update_kms_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_update_kms_config` interceptor runs
        before the `post_update_kms_config_with_metadata` interceptor.
        """
        return response

    def post_update_kms_config_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_kms_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_update_kms_config_with_metadata`
        interceptor in new development instead of the `post_update_kms_config` interceptor.
        When both interceptors are used, this `post_update_kms_config_with_metadata` interceptor runs after the
        `post_update_kms_config` interceptor. The (possibly modified) response returned by
        `post_update_kms_config` will be passed to
        `post_update_kms_config_with_metadata`.
        """
        return response, metadata

    def pre_update_quota_rule(
        self,
        request: gcn_quota_rule.UpdateQuotaRuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_quota_rule.UpdateQuotaRuleRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_quota_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_update_quota_rule(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_quota_rule

        DEPRECATED. Please use the `post_update_quota_rule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_update_quota_rule` interceptor runs
        before the `post_update_quota_rule_with_metadata` interceptor.
        """
        return response

    def post_update_quota_rule_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_quota_rule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_update_quota_rule_with_metadata`
        interceptor in new development instead of the `post_update_quota_rule` interceptor.
        When both interceptors are used, this `post_update_quota_rule_with_metadata` interceptor runs after the
        `post_update_quota_rule` interceptor. The (possibly modified) response returned by
        `post_update_quota_rule` will be passed to
        `post_update_quota_rule_with_metadata`.
        """
        return response, metadata

    def pre_update_replication(
        self,
        request: gcn_replication.UpdateReplicationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_replication.UpdateReplicationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_replication

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_update_replication(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_replication

        DEPRECATED. Please use the `post_update_replication_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_update_replication` interceptor runs
        before the `post_update_replication_with_metadata` interceptor.
        """
        return response

    def post_update_replication_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_replication

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_update_replication_with_metadata`
        interceptor in new development instead of the `post_update_replication` interceptor.
        When both interceptors are used, this `post_update_replication_with_metadata` interceptor runs after the
        `post_update_replication` interceptor. The (possibly modified) response returned by
        `post_update_replication` will be passed to
        `post_update_replication_with_metadata`.
        """
        return response, metadata

    def pre_update_snapshot(
        self,
        request: gcn_snapshot.UpdateSnapshotRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_snapshot.UpdateSnapshotRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_snapshot

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_update_snapshot(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_snapshot

        DEPRECATED. Please use the `post_update_snapshot_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_update_snapshot` interceptor runs
        before the `post_update_snapshot_with_metadata` interceptor.
        """
        return response

    def post_update_snapshot_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_snapshot

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_update_snapshot_with_metadata`
        interceptor in new development instead of the `post_update_snapshot` interceptor.
        When both interceptors are used, this `post_update_snapshot_with_metadata` interceptor runs after the
        `post_update_snapshot` interceptor. The (possibly modified) response returned by
        `post_update_snapshot` will be passed to
        `post_update_snapshot_with_metadata`.
        """
        return response, metadata

    def pre_update_storage_pool(
        self,
        request: gcn_storage_pool.UpdateStoragePoolRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcn_storage_pool.UpdateStoragePoolRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_storage_pool

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_update_storage_pool(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_storage_pool

        DEPRECATED. Please use the `post_update_storage_pool_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_update_storage_pool` interceptor runs
        before the `post_update_storage_pool_with_metadata` interceptor.
        """
        return response

    def post_update_storage_pool_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_storage_pool

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_update_storage_pool_with_metadata`
        interceptor in new development instead of the `post_update_storage_pool` interceptor.
        When both interceptors are used, this `post_update_storage_pool_with_metadata` interceptor runs after the
        `post_update_storage_pool` interceptor. The (possibly modified) response returned by
        `post_update_storage_pool` will be passed to
        `post_update_storage_pool_with_metadata`.
        """
        return response, metadata

    def pre_update_volume(
        self,
        request: gcn_volume.UpdateVolumeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcn_volume.UpdateVolumeRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_volume

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_update_volume(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_volume

        DEPRECATED. Please use the `post_update_volume_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_update_volume` interceptor runs
        before the `post_update_volume_with_metadata` interceptor.
        """
        return response

    def post_update_volume_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_volume

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_update_volume_with_metadata`
        interceptor in new development instead of the `post_update_volume` interceptor.
        When both interceptors are used, this `post_update_volume_with_metadata` interceptor runs after the
        `post_update_volume` interceptor. The (possibly modified) response returned by
        `post_update_volume` will be passed to
        `post_update_volume_with_metadata`.
        """
        return response, metadata

    def pre_validate_directory_service(
        self,
        request: storage_pool.ValidateDirectoryServiceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        storage_pool.ValidateDirectoryServiceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for validate_directory_service

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_validate_directory_service(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for validate_directory_service

        DEPRECATED. Please use the `post_validate_directory_service_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_validate_directory_service` interceptor runs
        before the `post_validate_directory_service_with_metadata` interceptor.
        """
        return response

    def post_validate_directory_service_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for validate_directory_service

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_validate_directory_service_with_metadata`
        interceptor in new development instead of the `post_validate_directory_service` interceptor.
        When both interceptors are used, this `post_validate_directory_service_with_metadata` interceptor runs after the
        `post_validate_directory_service` interceptor. The (possibly modified) response returned by
        `post_validate_directory_service` will be passed to
        `post_validate_directory_service_with_metadata`.
        """
        return response, metadata

    def pre_verify_kms_config(
        self,
        request: kms.VerifyKmsConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[kms.VerifyKmsConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for verify_kms_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_verify_kms_config(
        self, response: kms.VerifyKmsConfigResponse
    ) -> kms.VerifyKmsConfigResponse:
        """Post-rpc interceptor for verify_kms_config

        DEPRECATED. Please use the `post_verify_kms_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code. This `post_verify_kms_config` interceptor runs
        before the `post_verify_kms_config_with_metadata` interceptor.
        """
        return response

    def post_verify_kms_config_with_metadata(
        self,
        response: kms.VerifyKmsConfigResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[kms.VerifyKmsConfigResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for verify_kms_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the NetApp server but before it is returned to user code.

        We recommend only using this `post_verify_kms_config_with_metadata`
        interceptor in new development instead of the `post_verify_kms_config` interceptor.
        When both interceptors are used, this `post_verify_kms_config_with_metadata` interceptor runs after the
        `post_verify_kms_config` interceptor. The (possibly modified) response returned by
        `post_verify_kms_config` will be passed to
        `post_verify_kms_config_with_metadata`.
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
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
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
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
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
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
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
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
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
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
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
        before they are sent to the NetApp server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the NetApp server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class NetAppRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: NetAppRestInterceptor


class NetAppRestTransport(_BaseNetAppRestTransport):
    """REST backend synchronous transport for NetApp.

    NetApp Files Google Cloud Service

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "netapp.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[NetAppRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'netapp.googleapis.com').
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
            interceptor (Optional[NetAppRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or NetAppRestInterceptor()
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

    class _CreateActiveDirectory(
        _BaseNetAppRestTransport._BaseCreateActiveDirectory, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.CreateActiveDirectory")

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
            request: gcn_active_directory.CreateActiveDirectoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create active directory method over HTTP.

            Args:
                request (~.gcn_active_directory.CreateActiveDirectoryRequest):
                    The request object. CreateActiveDirectoryRequest for
                creating an active directory.
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
                _BaseNetAppRestTransport._BaseCreateActiveDirectory._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_active_directory(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseCreateActiveDirectory,
                    "_BaseCreateActiveDirectory__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.CreateActiveDirectory",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "CreateActiveDirectory",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._CreateActiveDirectory._get_response(
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

            resp = self._interceptor.post_create_active_directory(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_active_directory_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.create_active_directory",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "CreateActiveDirectory",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateBackup(_BaseNetAppRestTransport._BaseCreateBackup, NetAppRestStub):
        def __hash__(self):
            return hash("NetAppRestTransport.CreateBackup")

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
            request: gcn_backup.CreateBackupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create backup method over HTTP.

            Args:
                request (~.gcn_backup.CreateBackupRequest):
                    The request object. CreateBackupRequest creates a backup.
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
                _BaseNetAppRestTransport._BaseCreateBackup._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_backup(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseCreateBackup,
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.CreateBackup",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "CreateBackup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._CreateBackup._get_response(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.create_backup",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "CreateBackup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateBackupPolicy(
        _BaseNetAppRestTransport._BaseCreateBackupPolicy, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.CreateBackupPolicy")

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
            request: gcn_backup_policy.CreateBackupPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create backup policy method over HTTP.

            Args:
                request (~.gcn_backup_policy.CreateBackupPolicyRequest):
                    The request object. CreateBackupPolicyRequest creates a
                backupPolicy.
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
                _BaseNetAppRestTransport._BaseCreateBackupPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_backup_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseCreateBackupPolicy,
                    "_BaseCreateBackupPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.CreateBackupPolicy",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "CreateBackupPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._CreateBackupPolicy._get_response(
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

            resp = self._interceptor.post_create_backup_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_backup_policy_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.create_backup_policy",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "CreateBackupPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateBackupVault(
        _BaseNetAppRestTransport._BaseCreateBackupVault, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.CreateBackupVault")

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
            request: gcn_backup_vault.CreateBackupVaultRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create backup vault method over HTTP.

            Args:
                request (~.gcn_backup_vault.CreateBackupVaultRequest):
                    The request object. CreateBackupVaultRequest creates a
                backup vault.
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
                _BaseNetAppRestTransport._BaseCreateBackupVault._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_backup_vault(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseCreateBackupVault,
                    "_BaseCreateBackupVault__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.CreateBackupVault",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "CreateBackupVault",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._CreateBackupVault._get_response(
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

            resp = self._interceptor.post_create_backup_vault(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_backup_vault_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.create_backup_vault",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "CreateBackupVault",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateHostGroup(
        _BaseNetAppRestTransport._BaseCreateHostGroup, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.CreateHostGroup")

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
            request: gcn_host_group.CreateHostGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create host group method over HTTP.

            Args:
                request (~.gcn_host_group.CreateHostGroupRequest):
                    The request object. CreateHostGroupRequest for creating a
                host group.
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
                _BaseNetAppRestTransport._BaseCreateHostGroup._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_host_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseCreateHostGroup,
                    "_BaseCreateHostGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.CreateHostGroup",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "CreateHostGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._CreateHostGroup._get_response(
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

            resp = self._interceptor.post_create_host_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_host_group_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.create_host_group",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "CreateHostGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateKmsConfig(
        _BaseNetAppRestTransport._BaseCreateKmsConfig, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.CreateKmsConfig")

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
            request: kms.CreateKmsConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create kms config method over HTTP.

            Args:
                request (~.kms.CreateKmsConfigRequest):
                    The request object. CreateKmsConfigRequest creates a KMS
                Config.
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
                _BaseNetAppRestTransport._BaseCreateKmsConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_kms_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseCreateKmsConfig,
                    "_BaseCreateKmsConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.CreateKmsConfig",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "CreateKmsConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._CreateKmsConfig._get_response(
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

            resp = self._interceptor.post_create_kms_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_kms_config_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.create_kms_config",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "CreateKmsConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateQuotaRule(
        _BaseNetAppRestTransport._BaseCreateQuotaRule, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.CreateQuotaRule")

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
            request: gcn_quota_rule.CreateQuotaRuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create quota rule method over HTTP.

            Args:
                request (~.gcn_quota_rule.CreateQuotaRuleRequest):
                    The request object. CreateQuotaRuleRequest for creating a
                quota rule.
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
                _BaseNetAppRestTransport._BaseCreateQuotaRule._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_quota_rule(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseCreateQuotaRule,
                    "_BaseCreateQuotaRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.CreateQuotaRule",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "CreateQuotaRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._CreateQuotaRule._get_response(
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

            resp = self._interceptor.post_create_quota_rule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_quota_rule_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.create_quota_rule",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "CreateQuotaRule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateReplication(
        _BaseNetAppRestTransport._BaseCreateReplication, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.CreateReplication")

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
            request: gcn_replication.CreateReplicationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create replication method over HTTP.

            Args:
                request (~.gcn_replication.CreateReplicationRequest):
                    The request object. CreateReplicationRequest creates a
                replication.
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
                _BaseNetAppRestTransport._BaseCreateReplication._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_replication(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseCreateReplication,
                    "_BaseCreateReplication__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.CreateReplication",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "CreateReplication",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._CreateReplication._get_response(
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

            resp = self._interceptor.post_create_replication(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_replication_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.create_replication",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "CreateReplication",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateSnapshot(_BaseNetAppRestTransport._BaseCreateSnapshot, NetAppRestStub):
        def __hash__(self):
            return hash("NetAppRestTransport.CreateSnapshot")

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
            request: gcn_snapshot.CreateSnapshotRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create snapshot method over HTTP.

            Args:
                request (~.gcn_snapshot.CreateSnapshotRequest):
                    The request object. CreateSnapshotRequest creates a
                snapshot.
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
                _BaseNetAppRestTransport._BaseCreateSnapshot._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_snapshot(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseCreateSnapshot,
                    "_BaseCreateSnapshot__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.CreateSnapshot",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "CreateSnapshot",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._CreateSnapshot._get_response(
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

            resp = self._interceptor.post_create_snapshot(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_snapshot_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.create_snapshot",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "CreateSnapshot",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateStoragePool(
        _BaseNetAppRestTransport._BaseCreateStoragePool, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.CreateStoragePool")

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
            request: gcn_storage_pool.CreateStoragePoolRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create storage pool method over HTTP.

            Args:
                request (~.gcn_storage_pool.CreateStoragePoolRequest):
                    The request object. CreateStoragePoolRequest creates a
                Storage Pool.
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
                _BaseNetAppRestTransport._BaseCreateStoragePool._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_storage_pool(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseCreateStoragePool,
                    "_BaseCreateStoragePool__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.CreateStoragePool",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "CreateStoragePool",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._CreateStoragePool._get_response(
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

            resp = self._interceptor.post_create_storage_pool(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_storage_pool_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.create_storage_pool",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "CreateStoragePool",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateVolume(_BaseNetAppRestTransport._BaseCreateVolume, NetAppRestStub):
        def __hash__(self):
            return hash("NetAppRestTransport.CreateVolume")

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
            request: gcn_volume.CreateVolumeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create volume method over HTTP.

            Args:
                request (~.gcn_volume.CreateVolumeRequest):
                    The request object. Message for creating a Volume
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
                _BaseNetAppRestTransport._BaseCreateVolume._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_volume(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseCreateVolume,
                    "_BaseCreateVolume__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.CreateVolume",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "CreateVolume",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._CreateVolume._get_response(
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

            resp = self._interceptor.post_create_volume(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_volume_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.create_volume",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "CreateVolume",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteActiveDirectory(
        _BaseNetAppRestTransport._BaseDeleteActiveDirectory, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.DeleteActiveDirectory")

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
            request: active_directory.DeleteActiveDirectoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete active directory method over HTTP.

            Args:
                request (~.active_directory.DeleteActiveDirectoryRequest):
                    The request object. DeleteActiveDirectoryRequest for
                deleting a single active directory.
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
                _BaseNetAppRestTransport._BaseDeleteActiveDirectory._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_active_directory(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseDeleteActiveDirectory,
                    "_BaseDeleteActiveDirectory__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.DeleteActiveDirectory",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "DeleteActiveDirectory",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._DeleteActiveDirectory._get_response(
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

            resp = self._interceptor.post_delete_active_directory(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_active_directory_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.delete_active_directory",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "DeleteActiveDirectory",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteBackup(_BaseNetAppRestTransport._BaseDeleteBackup, NetAppRestStub):
        def __hash__(self):
            return hash("NetAppRestTransport.DeleteBackup")

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
            request: backup.DeleteBackupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete backup method over HTTP.

            Args:
                request (~.backup.DeleteBackupRequest):
                    The request object. DeleteBackupRequest deletes a backup.
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
                _BaseNetAppRestTransport._BaseDeleteBackup._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_backup(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseDeleteBackup,
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.DeleteBackup",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "DeleteBackup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._DeleteBackup._get_response(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.delete_backup",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "DeleteBackup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteBackupPolicy(
        _BaseNetAppRestTransport._BaseDeleteBackupPolicy, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.DeleteBackupPolicy")

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
            request: backup_policy.DeleteBackupPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete backup policy method over HTTP.

            Args:
                request (~.backup_policy.DeleteBackupPolicyRequest):
                    The request object. DeleteBackupPolicyRequest deletes a
                backup policy.
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
                _BaseNetAppRestTransport._BaseDeleteBackupPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_backup_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseDeleteBackupPolicy,
                    "_BaseDeleteBackupPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.DeleteBackupPolicy",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "DeleteBackupPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._DeleteBackupPolicy._get_response(
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

            resp = self._interceptor.post_delete_backup_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_backup_policy_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.delete_backup_policy",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "DeleteBackupPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteBackupVault(
        _BaseNetAppRestTransport._BaseDeleteBackupVault, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.DeleteBackupVault")

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
            request: backup_vault.DeleteBackupVaultRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete backup vault method over HTTP.

            Args:
                request (~.backup_vault.DeleteBackupVaultRequest):
                    The request object. DeleteBackupVaultRequest deletes a
                backupVault.
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
                _BaseNetAppRestTransport._BaseDeleteBackupVault._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_backup_vault(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseDeleteBackupVault,
                    "_BaseDeleteBackupVault__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.DeleteBackupVault",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "DeleteBackupVault",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._DeleteBackupVault._get_response(
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

            resp = self._interceptor.post_delete_backup_vault(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_backup_vault_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.delete_backup_vault",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "DeleteBackupVault",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteHostGroup(
        _BaseNetAppRestTransport._BaseDeleteHostGroup, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.DeleteHostGroup")

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
            request: host_group.DeleteHostGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete host group method over HTTP.

            Args:
                request (~.host_group.DeleteHostGroupRequest):
                    The request object. DeleteHostGroupRequest for deleting a
                single host group.
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
                _BaseNetAppRestTransport._BaseDeleteHostGroup._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_host_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseDeleteHostGroup,
                    "_BaseDeleteHostGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.DeleteHostGroup",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "DeleteHostGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._DeleteHostGroup._get_response(
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

            resp = self._interceptor.post_delete_host_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_host_group_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.delete_host_group",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "DeleteHostGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteKmsConfig(
        _BaseNetAppRestTransport._BaseDeleteKmsConfig, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.DeleteKmsConfig")

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
            request: kms.DeleteKmsConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete kms config method over HTTP.

            Args:
                request (~.kms.DeleteKmsConfigRequest):
                    The request object. DeleteKmsConfigRequest deletes a KMS
                Config.
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
                _BaseNetAppRestTransport._BaseDeleteKmsConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_kms_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseDeleteKmsConfig,
                    "_BaseDeleteKmsConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.DeleteKmsConfig",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "DeleteKmsConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._DeleteKmsConfig._get_response(
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

            resp = self._interceptor.post_delete_kms_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_kms_config_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.delete_kms_config",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "DeleteKmsConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteQuotaRule(
        _BaseNetAppRestTransport._BaseDeleteQuotaRule, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.DeleteQuotaRule")

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
            request: quota_rule.DeleteQuotaRuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete quota rule method over HTTP.

            Args:
                request (~.quota_rule.DeleteQuotaRuleRequest):
                    The request object. DeleteQuotaRuleRequest for deleting a
                single quota rule.
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
                _BaseNetAppRestTransport._BaseDeleteQuotaRule._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_quota_rule(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseDeleteQuotaRule,
                    "_BaseDeleteQuotaRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.DeleteQuotaRule",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "DeleteQuotaRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._DeleteQuotaRule._get_response(
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

            resp = self._interceptor.post_delete_quota_rule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_quota_rule_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.delete_quota_rule",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "DeleteQuotaRule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteReplication(
        _BaseNetAppRestTransport._BaseDeleteReplication, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.DeleteReplication")

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
            request: replication.DeleteReplicationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete replication method over HTTP.

            Args:
                request (~.replication.DeleteReplicationRequest):
                    The request object. DeleteReplicationRequest deletes a
                replication.
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
                _BaseNetAppRestTransport._BaseDeleteReplication._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_replication(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseDeleteReplication,
                    "_BaseDeleteReplication__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.DeleteReplication",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "DeleteReplication",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._DeleteReplication._get_response(
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

            resp = self._interceptor.post_delete_replication(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_replication_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.delete_replication",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "DeleteReplication",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteSnapshot(_BaseNetAppRestTransport._BaseDeleteSnapshot, NetAppRestStub):
        def __hash__(self):
            return hash("NetAppRestTransport.DeleteSnapshot")

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
            request: snapshot.DeleteSnapshotRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete snapshot method over HTTP.

            Args:
                request (~.snapshot.DeleteSnapshotRequest):
                    The request object. DeleteSnapshotRequest deletes a
                snapshot.
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
                _BaseNetAppRestTransport._BaseDeleteSnapshot._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_snapshot(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseDeleteSnapshot,
                    "_BaseDeleteSnapshot__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.DeleteSnapshot",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "DeleteSnapshot",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._DeleteSnapshot._get_response(
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

            resp = self._interceptor.post_delete_snapshot(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_snapshot_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.delete_snapshot",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "DeleteSnapshot",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteStoragePool(
        _BaseNetAppRestTransport._BaseDeleteStoragePool, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.DeleteStoragePool")

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
            request: storage_pool.DeleteStoragePoolRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete storage pool method over HTTP.

            Args:
                request (~.storage_pool.DeleteStoragePoolRequest):
                    The request object. DeleteStoragePoolRequest deletes a
                Storage Pool.
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
                _BaseNetAppRestTransport._BaseDeleteStoragePool._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_storage_pool(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseDeleteStoragePool,
                    "_BaseDeleteStoragePool__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.DeleteStoragePool",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "DeleteStoragePool",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._DeleteStoragePool._get_response(
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

            resp = self._interceptor.post_delete_storage_pool(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_storage_pool_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.delete_storage_pool",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "DeleteStoragePool",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteVolume(_BaseNetAppRestTransport._BaseDeleteVolume, NetAppRestStub):
        def __hash__(self):
            return hash("NetAppRestTransport.DeleteVolume")

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
            request: volume.DeleteVolumeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete volume method over HTTP.

            Args:
                request (~.volume.DeleteVolumeRequest):
                    The request object. Message for deleting a Volume
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
                _BaseNetAppRestTransport._BaseDeleteVolume._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_volume(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseDeleteVolume,
                    "_BaseDeleteVolume__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.DeleteVolume",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "DeleteVolume",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._DeleteVolume._get_response(
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

            resp = self._interceptor.post_delete_volume(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_volume_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.delete_volume",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "DeleteVolume",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _EncryptVolumes(_BaseNetAppRestTransport._BaseEncryptVolumes, NetAppRestStub):
        def __hash__(self):
            return hash("NetAppRestTransport.EncryptVolumes")

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
            request: kms.EncryptVolumesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the encrypt volumes method over HTTP.

            Args:
                request (~.kms.EncryptVolumesRequest):
                    The request object. EncryptVolumesRequest specifies the
                KMS config to encrypt existing volumes.
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
                _BaseNetAppRestTransport._BaseEncryptVolumes._get_http_options()
            )
            request, metadata = self._interceptor.pre_encrypt_volumes(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseEncryptVolumes,
                    "_BaseEncryptVolumes__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.EncryptVolumes",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "EncryptVolumes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._EncryptVolumes._get_response(
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

            resp = self._interceptor.post_encrypt_volumes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_encrypt_volumes_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.encrypt_volumes",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "EncryptVolumes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _EstablishPeering(
        _BaseNetAppRestTransport._BaseEstablishPeering, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.EstablishPeering")

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
            request: replication.EstablishPeeringRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the establish peering method over HTTP.

            Args:
                request (~.replication.EstablishPeeringRequest):
                    The request object. EstablishPeeringRequest establishes
                cluster and svm peerings between the
                source and the destination replications.
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
                _BaseNetAppRestTransport._BaseEstablishPeering._get_http_options()
            )
            request, metadata = self._interceptor.pre_establish_peering(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseEstablishPeering,
                    "_BaseEstablishPeering__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.EstablishPeering",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "EstablishPeering",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._EstablishPeering._get_response(
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

            resp = self._interceptor.post_establish_peering(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_establish_peering_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.establish_peering",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "EstablishPeering",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _EstablishVolumePeering(
        _BaseNetAppRestTransport._BaseEstablishVolumePeering, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.EstablishVolumePeering")

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
            request: volume.EstablishVolumePeeringRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the establish volume peering method over HTTP.

            Args:
                request (~.volume.EstablishVolumePeeringRequest):
                    The request object. EstablishVolumePeeringRequest
                establishes cluster and svm peerings
                between the source and destination
                clusters.
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
                _BaseNetAppRestTransport._BaseEstablishVolumePeering._get_http_options()
            )
            request, metadata = self._interceptor.pre_establish_volume_peering(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseEstablishVolumePeering,
                    "_BaseEstablishVolumePeering__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.EstablishVolumePeering",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "EstablishVolumePeering",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._EstablishVolumePeering._get_response(
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

            resp = self._interceptor.post_establish_volume_peering(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_establish_volume_peering_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.establish_volume_peering",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "EstablishVolumePeering",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ExecuteOntapDelete(
        _BaseNetAppRestTransport._BaseExecuteOntapDelete, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.ExecuteOntapDelete")

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
            request: ontap.ExecuteOntapDeleteRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ontap.ExecuteOntapDeleteResponse:
            r"""Call the execute ontap delete method over HTTP.

            Args:
                request (~.ontap.ExecuteOntapDeleteRequest):
                    The request object. Request message for ``ExecuteOntapDelete`` API.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ontap.ExecuteOntapDeleteResponse:
                    Response message for ``ExecuteOntapDelete`` API.
            """

            http_options = (
                _BaseNetAppRestTransport._BaseExecuteOntapDelete._get_http_options()
            )
            request, metadata = self._interceptor.pre_execute_ontap_delete(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseExecuteOntapDelete,
                    "_BaseExecuteOntapDelete__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.ExecuteOntapDelete",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ExecuteOntapDelete",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._ExecuteOntapDelete._get_response(
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
            resp = ontap.ExecuteOntapDeleteResponse()
            pb_resp = ontap.ExecuteOntapDeleteResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_execute_ontap_delete(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_execute_ontap_delete_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ontap.ExecuteOntapDeleteResponse.to_json(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.execute_ontap_delete",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ExecuteOntapDelete",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ExecuteOntapGet(
        _BaseNetAppRestTransport._BaseExecuteOntapGet, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.ExecuteOntapGet")

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
            request: ontap.ExecuteOntapGetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ontap.ExecuteOntapGetResponse:
            r"""Call the execute ontap get method over HTTP.

            Args:
                request (~.ontap.ExecuteOntapGetRequest):
                    The request object. Request message for ``ExecuteOntapGet`` API.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ontap.ExecuteOntapGetResponse:
                    Response message for ``ExecuteOntapGet`` API.
            """

            http_options = (
                _BaseNetAppRestTransport._BaseExecuteOntapGet._get_http_options()
            )
            request, metadata = self._interceptor.pre_execute_ontap_get(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseExecuteOntapGet,
                    "_BaseExecuteOntapGet__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.ExecuteOntapGet",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ExecuteOntapGet",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._ExecuteOntapGet._get_response(
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
            resp = ontap.ExecuteOntapGetResponse()
            pb_resp = ontap.ExecuteOntapGetResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_execute_ontap_get(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_execute_ontap_get_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ontap.ExecuteOntapGetResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.netapp_v1.NetAppClient.execute_ontap_get",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ExecuteOntapGet",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ExecuteOntapPatch(
        _BaseNetAppRestTransport._BaseExecuteOntapPatch, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.ExecuteOntapPatch")

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
            request: ontap.ExecuteOntapPatchRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ontap.ExecuteOntapPatchResponse:
            r"""Call the execute ontap patch method over HTTP.

            Args:
                request (~.ontap.ExecuteOntapPatchRequest):
                    The request object. Request message for ``ExecuteOntapPatch`` API.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ontap.ExecuteOntapPatchResponse:
                    Response message for ``ExecuteOntapPatch`` API.
            """

            http_options = (
                _BaseNetAppRestTransport._BaseExecuteOntapPatch._get_http_options()
            )
            request, metadata = self._interceptor.pre_execute_ontap_patch(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseExecuteOntapPatch,
                    "_BaseExecuteOntapPatch__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.ExecuteOntapPatch",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ExecuteOntapPatch",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._ExecuteOntapPatch._get_response(
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
            resp = ontap.ExecuteOntapPatchResponse()
            pb_resp = ontap.ExecuteOntapPatchResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_execute_ontap_patch(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_execute_ontap_patch_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ontap.ExecuteOntapPatchResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.netapp_v1.NetAppClient.execute_ontap_patch",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ExecuteOntapPatch",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ExecuteOntapPost(
        _BaseNetAppRestTransport._BaseExecuteOntapPost, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.ExecuteOntapPost")

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
            request: ontap.ExecuteOntapPostRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> ontap.ExecuteOntapPostResponse:
            r"""Call the execute ontap post method over HTTP.

            Args:
                request (~.ontap.ExecuteOntapPostRequest):
                    The request object. Request message for ``ExecuteOntapPost`` API.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.ontap.ExecuteOntapPostResponse:
                    Response message for ``ExecuteOntapPost`` API.
            """

            http_options = (
                _BaseNetAppRestTransport._BaseExecuteOntapPost._get_http_options()
            )
            request, metadata = self._interceptor.pre_execute_ontap_post(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseExecuteOntapPost,
                    "_BaseExecuteOntapPost__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.ExecuteOntapPost",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ExecuteOntapPost",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._ExecuteOntapPost._get_response(
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
            resp = ontap.ExecuteOntapPostResponse()
            pb_resp = ontap.ExecuteOntapPostResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_execute_ontap_post(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_execute_ontap_post_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = ontap.ExecuteOntapPostResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.netapp_v1.NetAppClient.execute_ontap_post",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ExecuteOntapPost",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetActiveDirectory(
        _BaseNetAppRestTransport._BaseGetActiveDirectory, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.GetActiveDirectory")

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
            request: active_directory.GetActiveDirectoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> active_directory.ActiveDirectory:
            r"""Call the get active directory method over HTTP.

            Args:
                request (~.active_directory.GetActiveDirectoryRequest):
                    The request object. GetActiveDirectory for getting a
                single active directory.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.active_directory.ActiveDirectory:
                    ActiveDirectory is the public
                representation of the active directory
                config.

            """

            http_options = (
                _BaseNetAppRestTransport._BaseGetActiveDirectory._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_active_directory(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseGetActiveDirectory,
                    "_BaseGetActiveDirectory__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.GetActiveDirectory",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "GetActiveDirectory",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._GetActiveDirectory._get_response(
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
            resp = active_directory.ActiveDirectory()
            pb_resp = active_directory.ActiveDirectory.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_active_directory(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_active_directory_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = active_directory.ActiveDirectory.to_json(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.get_active_directory",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "GetActiveDirectory",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetBackup(_BaseNetAppRestTransport._BaseGetBackup, NetAppRestStub):
        def __hash__(self):
            return hash("NetAppRestTransport.GetBackup")

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
            request: backup.GetBackupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> backup.Backup:
            r"""Call the get backup method over HTTP.

            Args:
                request (~.backup.GetBackupRequest):
                    The request object. GetBackupRequest gets the state of a
                backup.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.backup.Backup:
                    A NetApp Backup.
            """

            http_options = _BaseNetAppRestTransport._BaseGetBackup._get_http_options()
            request, metadata = self._interceptor.pre_get_backup(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseGetBackup,
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.GetBackup",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "GetBackup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._GetBackup._get_response(
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
            resp = backup.Backup()
            pb_resp = backup.Backup.pb(resp)

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
                    response_payload = backup.Backup.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.netapp_v1.NetAppClient.get_backup",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "GetBackup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetBackupPolicy(
        _BaseNetAppRestTransport._BaseGetBackupPolicy, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.GetBackupPolicy")

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
            request: backup_policy.GetBackupPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> backup_policy.BackupPolicy:
            r"""Call the get backup policy method over HTTP.

            Args:
                request (~.backup_policy.GetBackupPolicyRequest):
                    The request object. GetBackupPolicyRequest gets the state
                of a backupPolicy.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.backup_policy.BackupPolicy:
                    Backup Policy.
            """

            http_options = (
                _BaseNetAppRestTransport._BaseGetBackupPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_backup_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseGetBackupPolicy,
                    "_BaseGetBackupPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.GetBackupPolicy",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "GetBackupPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._GetBackupPolicy._get_response(
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
            resp = backup_policy.BackupPolicy()
            pb_resp = backup_policy.BackupPolicy.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_backup_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_backup_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = backup_policy.BackupPolicy.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.netapp_v1.NetAppClient.get_backup_policy",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "GetBackupPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetBackupVault(_BaseNetAppRestTransport._BaseGetBackupVault, NetAppRestStub):
        def __hash__(self):
            return hash("NetAppRestTransport.GetBackupVault")

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
            request: backup_vault.GetBackupVaultRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> backup_vault.BackupVault:
            r"""Call the get backup vault method over HTTP.

            Args:
                request (~.backup_vault.GetBackupVaultRequest):
                    The request object. GetBackupVaultRequest gets the state
                of a backupVault.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.backup_vault.BackupVault:
                    A NetApp BackupVault.
            """

            http_options = (
                _BaseNetAppRestTransport._BaseGetBackupVault._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_backup_vault(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseGetBackupVault,
                    "_BaseGetBackupVault__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.GetBackupVault",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "GetBackupVault",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._GetBackupVault._get_response(
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
            resp = backup_vault.BackupVault()
            pb_resp = backup_vault.BackupVault.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_backup_vault(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_backup_vault_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = backup_vault.BackupVault.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.netapp_v1.NetAppClient.get_backup_vault",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "GetBackupVault",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetHostGroup(_BaseNetAppRestTransport._BaseGetHostGroup, NetAppRestStub):
        def __hash__(self):
            return hash("NetAppRestTransport.GetHostGroup")

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
            request: host_group.GetHostGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> host_group.HostGroup:
            r"""Call the get host group method over HTTP.

            Args:
                request (~.host_group.GetHostGroupRequest):
                    The request object. GetHostGroupRequest for getting a
                host group.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.host_group.HostGroup:
                    Host group is a collection of hosts
                that can be used for accessing a Block
                Volume.

            """

            http_options = (
                _BaseNetAppRestTransport._BaseGetHostGroup._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_host_group(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseGetHostGroup,
                    "_BaseGetHostGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.GetHostGroup",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "GetHostGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._GetHostGroup._get_response(
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
            resp = host_group.HostGroup()
            pb_resp = host_group.HostGroup.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_host_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_host_group_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = host_group.HostGroup.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.netapp_v1.NetAppClient.get_host_group",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "GetHostGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetKmsConfig(_BaseNetAppRestTransport._BaseGetKmsConfig, NetAppRestStub):
        def __hash__(self):
            return hash("NetAppRestTransport.GetKmsConfig")

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
            request: kms.GetKmsConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> kms.KmsConfig:
            r"""Call the get kms config method over HTTP.

            Args:
                request (~.kms.GetKmsConfigRequest):
                    The request object. GetKmsConfigRequest gets a KMS
                Config.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.kms.KmsConfig:
                    KmsConfig is the customer-managed
                encryption key(CMEK) configuration.

            """

            http_options = (
                _BaseNetAppRestTransport._BaseGetKmsConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_kms_config(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseGetKmsConfig,
                    "_BaseGetKmsConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.GetKmsConfig",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "GetKmsConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._GetKmsConfig._get_response(
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
            resp = kms.KmsConfig()
            pb_resp = kms.KmsConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_kms_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_kms_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = kms.KmsConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.netapp_v1.NetAppClient.get_kms_config",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "GetKmsConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetQuotaRule(_BaseNetAppRestTransport._BaseGetQuotaRule, NetAppRestStub):
        def __hash__(self):
            return hash("NetAppRestTransport.GetQuotaRule")

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
            request: quota_rule.GetQuotaRuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> quota_rule.QuotaRule:
            r"""Call the get quota rule method over HTTP.

            Args:
                request (~.quota_rule.GetQuotaRuleRequest):
                    The request object. GetQuotaRuleRequest for getting a
                quota rule.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.quota_rule.QuotaRule:
                    QuotaRule specifies the maximum disk
                space a user or group can use within a
                volume. They can be used for creating
                default and individual quota rules.

            """

            http_options = (
                _BaseNetAppRestTransport._BaseGetQuotaRule._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_quota_rule(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseGetQuotaRule,
                    "_BaseGetQuotaRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.GetQuotaRule",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "GetQuotaRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._GetQuotaRule._get_response(
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
            resp = quota_rule.QuotaRule()
            pb_resp = quota_rule.QuotaRule.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_quota_rule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_quota_rule_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = quota_rule.QuotaRule.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.netapp_v1.NetAppClient.get_quota_rule",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "GetQuotaRule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetReplication(_BaseNetAppRestTransport._BaseGetReplication, NetAppRestStub):
        def __hash__(self):
            return hash("NetAppRestTransport.GetReplication")

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
            request: replication.GetReplicationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> replication.Replication:
            r"""Call the get replication method over HTTP.

            Args:
                request (~.replication.GetReplicationRequest):
                    The request object. GetReplicationRequest gets the state
                of a replication.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.replication.Replication:
                    Replication is a nested resource
                under Volume, that describes a
                cross-region replication relationship
                between 2 volumes in different regions.

            """

            http_options = (
                _BaseNetAppRestTransport._BaseGetReplication._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_replication(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseGetReplication,
                    "_BaseGetReplication__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.GetReplication",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "GetReplication",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._GetReplication._get_response(
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
            resp = replication.Replication()
            pb_resp = replication.Replication.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_replication(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_replication_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = replication.Replication.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.netapp_v1.NetAppClient.get_replication",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "GetReplication",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSnapshot(_BaseNetAppRestTransport._BaseGetSnapshot, NetAppRestStub):
        def __hash__(self):
            return hash("NetAppRestTransport.GetSnapshot")

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
            request: snapshot.GetSnapshotRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> snapshot.Snapshot:
            r"""Call the get snapshot method over HTTP.

            Args:
                request (~.snapshot.GetSnapshotRequest):
                    The request object. GetSnapshotRequest gets the state of
                a snapshot.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.snapshot.Snapshot:
                    Snapshot is a point-in-time version
                of a Volume's content.

            """

            http_options = _BaseNetAppRestTransport._BaseGetSnapshot._get_http_options()
            request, metadata = self._interceptor.pre_get_snapshot(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseGetSnapshot,
                    "_BaseGetSnapshot__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.GetSnapshot",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "GetSnapshot",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._GetSnapshot._get_response(
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
            resp = snapshot.Snapshot()
            pb_resp = snapshot.Snapshot.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_snapshot(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_snapshot_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = snapshot.Snapshot.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.netapp_v1.NetAppClient.get_snapshot",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "GetSnapshot",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSplitStatus(_BaseNetAppRestTransport._BaseGetSplitStatus, NetAppRestStub):
        def __hash__(self):
            return hash("NetAppRestTransport.GetSplitStatus")

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
            request: volume.GetSplitStatusRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> volume.SplitStatus:
            r"""Call the get split status method over HTTP.

            Args:
                request (~.volume.GetSplitStatusRequest):
                    The request object. Request message for GetSplitStatus.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.volume.SplitStatus:
                    Message for SplitStatus.
            """

            http_options = (
                _BaseNetAppRestTransport._BaseGetSplitStatus._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_split_status(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseGetSplitStatus,
                    "_BaseGetSplitStatus__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.GetSplitStatus",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "GetSplitStatus",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._GetSplitStatus._get_response(
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
            resp = volume.SplitStatus()
            pb_resp = volume.SplitStatus.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_split_status(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_split_status_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = volume.SplitStatus.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.netapp_v1.NetAppClient.get_split_status",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "GetSplitStatus",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetStoragePool(_BaseNetAppRestTransport._BaseGetStoragePool, NetAppRestStub):
        def __hash__(self):
            return hash("NetAppRestTransport.GetStoragePool")

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
            request: storage_pool.GetStoragePoolRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> storage_pool.StoragePool:
            r"""Call the get storage pool method over HTTP.

            Args:
                request (~.storage_pool.GetStoragePoolRequest):
                    The request object. GetStoragePoolRequest gets a Storage
                Pool.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.storage_pool.StoragePool:
                    StoragePool is a container for
                volumes with a service level and
                capacity. Volumes can be created in a
                pool of sufficient available capacity.
                StoragePool capacity is what you are
                billed for.

            """

            http_options = (
                _BaseNetAppRestTransport._BaseGetStoragePool._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_storage_pool(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseGetStoragePool,
                    "_BaseGetStoragePool__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.GetStoragePool",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "GetStoragePool",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._GetStoragePool._get_response(
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
            resp = storage_pool.StoragePool()
            pb_resp = storage_pool.StoragePool.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_storage_pool(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_storage_pool_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = storage_pool.StoragePool.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.netapp_v1.NetAppClient.get_storage_pool",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "GetStoragePool",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetVolume(_BaseNetAppRestTransport._BaseGetVolume, NetAppRestStub):
        def __hash__(self):
            return hash("NetAppRestTransport.GetVolume")

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
            request: volume.GetVolumeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> volume.Volume:
            r"""Call the get volume method over HTTP.

            Args:
                request (~.volume.GetVolumeRequest):
                    The request object. Message for getting a Volume
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.volume.Volume:
                    Volume provides a filesystem that you
                can mount.

            """

            http_options = _BaseNetAppRestTransport._BaseGetVolume._get_http_options()
            request, metadata = self._interceptor.pre_get_volume(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseGetVolume,
                    "_BaseGetVolume__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.GetVolume",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "GetVolume",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._GetVolume._get_response(
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
            resp = volume.Volume()
            pb_resp = volume.Volume.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_volume(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_volume_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = volume.Volume.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.netapp_v1.NetAppClient.get_volume",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "GetVolume",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListActiveDirectories(
        _BaseNetAppRestTransport._BaseListActiveDirectories, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.ListActiveDirectories")

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
            request: active_directory.ListActiveDirectoriesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> active_directory.ListActiveDirectoriesResponse:
            r"""Call the list active directories method over HTTP.

            Args:
                request (~.active_directory.ListActiveDirectoriesRequest):
                    The request object. ListActiveDirectoriesRequest for
                requesting multiple active directories.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.active_directory.ListActiveDirectoriesResponse:
                    ListActiveDirectoriesResponse
                contains all the active directories
                requested.

            """

            http_options = (
                _BaseNetAppRestTransport._BaseListActiveDirectories._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_active_directories(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseListActiveDirectories,
                    "_BaseListActiveDirectories__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.ListActiveDirectories",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ListActiveDirectories",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._ListActiveDirectories._get_response(
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
            resp = active_directory.ListActiveDirectoriesResponse()
            pb_resp = active_directory.ListActiveDirectoriesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_active_directories(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_active_directories_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        active_directory.ListActiveDirectoriesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.netapp_v1.NetAppClient.list_active_directories",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ListActiveDirectories",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListBackupConfigs(
        _BaseNetAppRestTransport._BaseListBackupConfigs, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.ListBackupConfigs")

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
            request: volume.ListBackupConfigsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> volume.ListBackupConfigsResponse:
            r"""Call the list backup configs method over HTTP.

            Args:
                request (~.volume.ListBackupConfigsRequest):
                    The request object. Message for requesting list of
                BackupConfigs in a StoragePool.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.volume.ListBackupConfigsResponse:
                    Message for response to listing
                BackupConfigs in an ONTAP StoragePool.

            """

            http_options = (
                _BaseNetAppRestTransport._BaseListBackupConfigs._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_backup_configs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseListBackupConfigs,
                    "_BaseListBackupConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.ListBackupConfigs",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ListBackupConfigs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._ListBackupConfigs._get_response(
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
            resp = volume.ListBackupConfigsResponse()
            pb_resp = volume.ListBackupConfigsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_backup_configs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_backup_configs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = volume.ListBackupConfigsResponse.to_json(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.list_backup_configs",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ListBackupConfigs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListBackupPolicies(
        _BaseNetAppRestTransport._BaseListBackupPolicies, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.ListBackupPolicies")

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
            request: backup_policy.ListBackupPoliciesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> backup_policy.ListBackupPoliciesResponse:
            r"""Call the list backup policies method over HTTP.

            Args:
                request (~.backup_policy.ListBackupPoliciesRequest):
                    The request object. ListBackupPoliciesRequest for
                requesting multiple backup policies.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.backup_policy.ListBackupPoliciesResponse:
                    ListBackupPoliciesResponse contains
                all the backup policies requested.

            """

            http_options = (
                _BaseNetAppRestTransport._BaseListBackupPolicies._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_backup_policies(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseListBackupPolicies,
                    "_BaseListBackupPolicies__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.ListBackupPolicies",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ListBackupPolicies",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._ListBackupPolicies._get_response(
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
            resp = backup_policy.ListBackupPoliciesResponse()
            pb_resp = backup_policy.ListBackupPoliciesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_backup_policies(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_backup_policies_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = backup_policy.ListBackupPoliciesResponse.to_json(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.list_backup_policies",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ListBackupPolicies",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListBackups(_BaseNetAppRestTransport._BaseListBackups, NetAppRestStub):
        def __hash__(self):
            return hash("NetAppRestTransport.ListBackups")

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
            request: backup.ListBackupsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> backup.ListBackupsResponse:
            r"""Call the list backups method over HTTP.

            Args:
                request (~.backup.ListBackupsRequest):
                    The request object. ListBackupsRequest lists backups.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.backup.ListBackupsResponse:
                    ListBackupsResponse is the result of
                ListBackupsRequest.

            """

            http_options = _BaseNetAppRestTransport._BaseListBackups._get_http_options()
            request, metadata = self._interceptor.pre_list_backups(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseListBackups,
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.ListBackups",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ListBackups",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._ListBackups._get_response(
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
            resp = backup.ListBackupsResponse()
            pb_resp = backup.ListBackupsResponse.pb(resp)

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
                    response_payload = backup.ListBackupsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.netapp_v1.NetAppClient.list_backups",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ListBackups",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListBackupVaults(
        _BaseNetAppRestTransport._BaseListBackupVaults, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.ListBackupVaults")

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
            request: backup_vault.ListBackupVaultsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> backup_vault.ListBackupVaultsResponse:
            r"""Call the list backup vaults method over HTTP.

            Args:
                request (~.backup_vault.ListBackupVaultsRequest):
                    The request object. ListBackupVaultsRequest lists
                backupVaults.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.backup_vault.ListBackupVaultsResponse:
                    ListBackupVaultsResponse is the
                result of ListBackupVaultsRequest.

            """

            http_options = (
                _BaseNetAppRestTransport._BaseListBackupVaults._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_backup_vaults(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseListBackupVaults,
                    "_BaseListBackupVaults__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.ListBackupVaults",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ListBackupVaults",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._ListBackupVaults._get_response(
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
            resp = backup_vault.ListBackupVaultsResponse()
            pb_resp = backup_vault.ListBackupVaultsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_backup_vaults(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_backup_vaults_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = backup_vault.ListBackupVaultsResponse.to_json(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.list_backup_vaults",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ListBackupVaults",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListHostGroups(_BaseNetAppRestTransport._BaseListHostGroups, NetAppRestStub):
        def __hash__(self):
            return hash("NetAppRestTransport.ListHostGroups")

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
            request: host_group.ListHostGroupsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> host_group.ListHostGroupsResponse:
            r"""Call the list host groups method over HTTP.

            Args:
                request (~.host_group.ListHostGroupsRequest):
                    The request object. ListHostGroupsRequest for listing
                host groups.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.host_group.ListHostGroupsResponse:
                    ListHostGroupsResponse is the
                response to a ListHostGroupsRequest.

            """

            http_options = (
                _BaseNetAppRestTransport._BaseListHostGroups._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_host_groups(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseListHostGroups,
                    "_BaseListHostGroups__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.ListHostGroups",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ListHostGroups",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._ListHostGroups._get_response(
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
            resp = host_group.ListHostGroupsResponse()
            pb_resp = host_group.ListHostGroupsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_host_groups(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_host_groups_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = host_group.ListHostGroupsResponse.to_json(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.list_host_groups",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ListHostGroups",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListKmsConfigs(_BaseNetAppRestTransport._BaseListKmsConfigs, NetAppRestStub):
        def __hash__(self):
            return hash("NetAppRestTransport.ListKmsConfigs")

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
            request: kms.ListKmsConfigsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> kms.ListKmsConfigsResponse:
            r"""Call the list kms configs method over HTTP.

            Args:
                request (~.kms.ListKmsConfigsRequest):
                    The request object. ListKmsConfigsRequest lists KMS
                Configs.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.kms.ListKmsConfigsResponse:
                    ListKmsConfigsResponse is the
                response to a ListKmsConfigsRequest.

            """

            http_options = (
                _BaseNetAppRestTransport._BaseListKmsConfigs._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_kms_configs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseListKmsConfigs,
                    "_BaseListKmsConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.ListKmsConfigs",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ListKmsConfigs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._ListKmsConfigs._get_response(
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
            resp = kms.ListKmsConfigsResponse()
            pb_resp = kms.ListKmsConfigsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_kms_configs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_kms_configs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = kms.ListKmsConfigsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.netapp_v1.NetAppClient.list_kms_configs",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ListKmsConfigs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListQuotaRules(_BaseNetAppRestTransport._BaseListQuotaRules, NetAppRestStub):
        def __hash__(self):
            return hash("NetAppRestTransport.ListQuotaRules")

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
            request: quota_rule.ListQuotaRulesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> quota_rule.ListQuotaRulesResponse:
            r"""Call the list quota rules method over HTTP.

            Args:
                request (~.quota_rule.ListQuotaRulesRequest):
                    The request object. ListQuotaRulesRequest for listing
                quota rules.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.quota_rule.ListQuotaRulesResponse:
                    ListQuotaRulesResponse is the
                response to a ListQuotaRulesRequest.

            """

            http_options = (
                _BaseNetAppRestTransport._BaseListQuotaRules._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_quota_rules(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseListQuotaRules,
                    "_BaseListQuotaRules__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.ListQuotaRules",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ListQuotaRules",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._ListQuotaRules._get_response(
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
            resp = quota_rule.ListQuotaRulesResponse()
            pb_resp = quota_rule.ListQuotaRulesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_quota_rules(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_quota_rules_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = quota_rule.ListQuotaRulesResponse.to_json(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.list_quota_rules",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ListQuotaRules",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListReplications(
        _BaseNetAppRestTransport._BaseListReplications, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.ListReplications")

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
            request: replication.ListReplicationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> replication.ListReplicationsResponse:
            r"""Call the list replications method over HTTP.

            Args:
                request (~.replication.ListReplicationsRequest):
                    The request object. ListReplications lists replications.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.replication.ListReplicationsResponse:
                    ListReplicationsResponse is the
                result of ListReplicationsRequest.

            """

            http_options = (
                _BaseNetAppRestTransport._BaseListReplications._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_replications(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseListReplications,
                    "_BaseListReplications__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.ListReplications",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ListReplications",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._ListReplications._get_response(
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
            resp = replication.ListReplicationsResponse()
            pb_resp = replication.ListReplicationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_replications(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_replications_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = replication.ListReplicationsResponse.to_json(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.list_replications",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ListReplications",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSnapshots(_BaseNetAppRestTransport._BaseListSnapshots, NetAppRestStub):
        def __hash__(self):
            return hash("NetAppRestTransport.ListSnapshots")

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
            request: snapshot.ListSnapshotsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> snapshot.ListSnapshotsResponse:
            r"""Call the list snapshots method over HTTP.

            Args:
                request (~.snapshot.ListSnapshotsRequest):
                    The request object. ListSnapshotsRequest lists snapshots.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.snapshot.ListSnapshotsResponse:
                    ListSnapshotsResponse is the result
                of ListSnapshotsRequest.

            """

            http_options = (
                _BaseNetAppRestTransport._BaseListSnapshots._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_snapshots(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseListSnapshots,
                    "_BaseListSnapshots__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.ListSnapshots",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ListSnapshots",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._ListSnapshots._get_response(
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
            resp = snapshot.ListSnapshotsResponse()
            pb_resp = snapshot.ListSnapshotsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_snapshots(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_snapshots_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = snapshot.ListSnapshotsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.netapp_v1.NetAppClient.list_snapshots",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ListSnapshots",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListStoragePools(
        _BaseNetAppRestTransport._BaseListStoragePools, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.ListStoragePools")

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
            request: storage_pool.ListStoragePoolsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> storage_pool.ListStoragePoolsResponse:
            r"""Call the list storage pools method over HTTP.

            Args:
                request (~.storage_pool.ListStoragePoolsRequest):
                    The request object. ListStoragePoolsRequest lists Storage
                Pools.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.storage_pool.ListStoragePoolsResponse:
                    ListStoragePoolsResponse is the
                response to a ListStoragePoolsRequest.

            """

            http_options = (
                _BaseNetAppRestTransport._BaseListStoragePools._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_storage_pools(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseListStoragePools,
                    "_BaseListStoragePools__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.ListStoragePools",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ListStoragePools",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._ListStoragePools._get_response(
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
            resp = storage_pool.ListStoragePoolsResponse()
            pb_resp = storage_pool.ListStoragePoolsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_storage_pools(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_storage_pools_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = storage_pool.ListStoragePoolsResponse.to_json(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.list_storage_pools",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ListStoragePools",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListVolumes(_BaseNetAppRestTransport._BaseListVolumes, NetAppRestStub):
        def __hash__(self):
            return hash("NetAppRestTransport.ListVolumes")

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
            request: volume.ListVolumesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> volume.ListVolumesResponse:
            r"""Call the list volumes method over HTTP.

            Args:
                request (~.volume.ListVolumesRequest):
                    The request object. Message for requesting list of
                Volumes
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.volume.ListVolumesResponse:
                    Message for response to listing
                Volumes

            """

            http_options = _BaseNetAppRestTransport._BaseListVolumes._get_http_options()
            request, metadata = self._interceptor.pre_list_volumes(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseListVolumes,
                    "_BaseListVolumes__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.ListVolumes",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ListVolumes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._ListVolumes._get_response(
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
            resp = volume.ListVolumesResponse()
            pb_resp = volume.ListVolumesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_volumes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_volumes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = volume.ListVolumesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.netapp_v1.NetAppClient.list_volumes",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ListVolumes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RestoreBackupFiles(
        _BaseNetAppRestTransport._BaseRestoreBackupFiles, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.RestoreBackupFiles")

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
            request: volume.RestoreBackupFilesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the restore backup files method over HTTP.

            Args:
                request (~.volume.RestoreBackupFilesRequest):
                    The request object. RestoreBackupFilesRequest restores
                files from a backup to a volume.
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
                _BaseNetAppRestTransport._BaseRestoreBackupFiles._get_http_options()
            )
            request, metadata = self._interceptor.pre_restore_backup_files(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseRestoreBackupFiles,
                    "_BaseRestoreBackupFiles__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.RestoreBackupFiles",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "RestoreBackupFiles",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._RestoreBackupFiles._get_response(
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

            resp = self._interceptor.post_restore_backup_files(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_restore_backup_files_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.restore_backup_files",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "RestoreBackupFiles",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RestoreVolume(_BaseNetAppRestTransport._BaseRestoreVolume, NetAppRestStub):
        def __hash__(self):
            return hash("NetAppRestTransport.RestoreVolume")

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
            request: volume.RestoreVolumeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the restore volume method over HTTP.

            Args:
                request (~.volume.RestoreVolumeRequest):
                    The request object. Request message for ``RestoreVolume`` API.
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
                _BaseNetAppRestTransport._BaseRestoreVolume._get_http_options()
            )
            request, metadata = self._interceptor.pre_restore_volume(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseRestoreVolume,
                    "_BaseRestoreVolume__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.RestoreVolume",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "RestoreVolume",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._RestoreVolume._get_response(
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

            resp = self._interceptor.post_restore_volume(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_restore_volume_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.restore_volume",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "RestoreVolume",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ResumeReplication(
        _BaseNetAppRestTransport._BaseResumeReplication, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.ResumeReplication")

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
            request: replication.ResumeReplicationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the resume replication method over HTTP.

            Args:
                request (~.replication.ResumeReplicationRequest):
                    The request object. ResumeReplicationRequest resumes a
                stopped replication.
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
                _BaseNetAppRestTransport._BaseResumeReplication._get_http_options()
            )
            request, metadata = self._interceptor.pre_resume_replication(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseResumeReplication,
                    "_BaseResumeReplication__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.ResumeReplication",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ResumeReplication",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._ResumeReplication._get_response(
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

            resp = self._interceptor.post_resume_replication(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_resume_replication_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.resume_replication",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ResumeReplication",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ReverseReplicationDirection(
        _BaseNetAppRestTransport._BaseReverseReplicationDirection, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.ReverseReplicationDirection")

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
            request: replication.ReverseReplicationDirectionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the reverse replication
            direction method over HTTP.

                Args:
                    request (~.replication.ReverseReplicationDirectionRequest):
                        The request object. ReverseReplicationDirectionRequest
                    reverses direction of replication.
                    Source becomes destination and
                    destination becomes source.
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

            http_options = _BaseNetAppRestTransport._BaseReverseReplicationDirection._get_http_options()
            request, metadata = self._interceptor.pre_reverse_replication_direction(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseReverseReplicationDirection,
                    "_BaseReverseReplicationDirection__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.ReverseReplicationDirection",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ReverseReplicationDirection",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._ReverseReplicationDirection._get_response(
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

            resp = self._interceptor.post_reverse_replication_direction(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_reverse_replication_direction_with_metadata(
                    resp, response_metadata
                )
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.reverse_replication_direction",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ReverseReplicationDirection",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RevertVolume(_BaseNetAppRestTransport._BaseRevertVolume, NetAppRestStub):
        def __hash__(self):
            return hash("NetAppRestTransport.RevertVolume")

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
            request: volume.RevertVolumeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the revert volume method over HTTP.

            Args:
                request (~.volume.RevertVolumeRequest):
                    The request object. RevertVolumeRequest reverts the given
                volume to the specified snapshot.
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
                _BaseNetAppRestTransport._BaseRevertVolume._get_http_options()
            )
            request, metadata = self._interceptor.pre_revert_volume(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseRevertVolume,
                    "_BaseRevertVolume__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.RevertVolume",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "RevertVolume",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._RevertVolume._get_response(
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

            resp = self._interceptor.post_revert_volume(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_revert_volume_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.revert_volume",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "RevertVolume",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _StartSplit(_BaseNetAppRestTransport._BaseStartSplit, NetAppRestStub):
        def __hash__(self):
            return hash("NetAppRestTransport.StartSplit")

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
            request: volume.StartSplitRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the start split method over HTTP.

            Args:
                request (~.volume.StartSplitRequest):
                    The request object. Request message for splitting a
                volume.
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

            http_options = _BaseNetAppRestTransport._BaseStartSplit._get_http_options()
            request, metadata = self._interceptor.pre_start_split(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseStartSplit,
                    "_BaseStartSplit__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.StartSplit",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "StartSplit",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._StartSplit._get_response(
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

            resp = self._interceptor.post_start_split(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_start_split_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.start_split",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "StartSplit",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _StopReplication(
        _BaseNetAppRestTransport._BaseStopReplication, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.StopReplication")

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
            request: replication.StopReplicationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the stop replication method over HTTP.

            Args:
                request (~.replication.StopReplicationRequest):
                    The request object. StopReplicationRequest stops a
                replication until resumed.
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
                _BaseNetAppRestTransport._BaseStopReplication._get_http_options()
            )
            request, metadata = self._interceptor.pre_stop_replication(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseStopReplication,
                    "_BaseStopReplication__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.StopReplication",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "StopReplication",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._StopReplication._get_response(
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

            resp = self._interceptor.post_stop_replication(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_stop_replication_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.stop_replication",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "StopReplication",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SwitchActiveReplicaZone(
        _BaseNetAppRestTransport._BaseSwitchActiveReplicaZone, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.SwitchActiveReplicaZone")

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
            request: storage_pool.SwitchActiveReplicaZoneRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the switch active replica
            zone method over HTTP.

                Args:
                    request (~.storage_pool.SwitchActiveReplicaZoneRequest):
                        The request object. SwitchActiveReplicaZoneRequest switch
                    the active/replica zone for a regional
                    storagePool.
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

            http_options = _BaseNetAppRestTransport._BaseSwitchActiveReplicaZone._get_http_options()
            request, metadata = self._interceptor.pre_switch_active_replica_zone(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseSwitchActiveReplicaZone,
                    "_BaseSwitchActiveReplicaZone__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.SwitchActiveReplicaZone",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "SwitchActiveReplicaZone",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._SwitchActiveReplicaZone._get_response(
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

            resp = self._interceptor.post_switch_active_replica_zone(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_switch_active_replica_zone_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.switch_active_replica_zone",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "SwitchActiveReplicaZone",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SyncReplication(
        _BaseNetAppRestTransport._BaseSyncReplication, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.SyncReplication")

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
            request: replication.SyncReplicationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the sync replication method over HTTP.

            Args:
                request (~.replication.SyncReplicationRequest):
                    The request object. SyncReplicationRequest syncs the
                replication from source to destination.
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
                _BaseNetAppRestTransport._BaseSyncReplication._get_http_options()
            )
            request, metadata = self._interceptor.pre_sync_replication(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseSyncReplication,
                    "_BaseSyncReplication__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.SyncReplication",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "SyncReplication",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._SyncReplication._get_response(
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

            resp = self._interceptor.post_sync_replication(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_sync_replication_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.sync_replication",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "SyncReplication",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateActiveDirectory(
        _BaseNetAppRestTransport._BaseUpdateActiveDirectory, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.UpdateActiveDirectory")

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
            request: gcn_active_directory.UpdateActiveDirectoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update active directory method over HTTP.

            Args:
                request (~.gcn_active_directory.UpdateActiveDirectoryRequest):
                    The request object. UpdateActiveDirectoryRequest for
                updating an active directory.
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
                _BaseNetAppRestTransport._BaseUpdateActiveDirectory._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_active_directory(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseUpdateActiveDirectory,
                    "_BaseUpdateActiveDirectory__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.UpdateActiveDirectory",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "UpdateActiveDirectory",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._UpdateActiveDirectory._get_response(
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

            resp = self._interceptor.post_update_active_directory(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_active_directory_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.update_active_directory",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "UpdateActiveDirectory",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateBackup(_BaseNetAppRestTransport._BaseUpdateBackup, NetAppRestStub):
        def __hash__(self):
            return hash("NetAppRestTransport.UpdateBackup")

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
            request: gcn_backup.UpdateBackupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update backup method over HTTP.

            Args:
                request (~.gcn_backup.UpdateBackupRequest):
                    The request object. UpdateBackupRequest updates
                description and/or labels for a backup.
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
                _BaseNetAppRestTransport._BaseUpdateBackup._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_backup(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseUpdateBackup,
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.UpdateBackup",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "UpdateBackup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._UpdateBackup._get_response(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.update_backup",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "UpdateBackup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateBackupConfig(
        _BaseNetAppRestTransport._BaseUpdateBackupConfig, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.UpdateBackupConfig")

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
            request: volume.UpdateBackupConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update backup config method over HTTP.

            Args:
                request (~.volume.UpdateBackupConfigRequest):
                    The request object. Request message for
                UpdateBackupConfig
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
                _BaseNetAppRestTransport._BaseUpdateBackupConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_backup_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseUpdateBackupConfig,
                    "_BaseUpdateBackupConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.UpdateBackupConfig",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "UpdateBackupConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._UpdateBackupConfig._get_response(
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

            resp = self._interceptor.post_update_backup_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_backup_config_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.update_backup_config",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "UpdateBackupConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateBackupPolicy(
        _BaseNetAppRestTransport._BaseUpdateBackupPolicy, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.UpdateBackupPolicy")

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
            request: gcn_backup_policy.UpdateBackupPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update backup policy method over HTTP.

            Args:
                request (~.gcn_backup_policy.UpdateBackupPolicyRequest):
                    The request object. UpdateBackupPolicyRequest for
                updating a backup policy.
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
                _BaseNetAppRestTransport._BaseUpdateBackupPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_backup_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseUpdateBackupPolicy,
                    "_BaseUpdateBackupPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.UpdateBackupPolicy",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "UpdateBackupPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._UpdateBackupPolicy._get_response(
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

            resp = self._interceptor.post_update_backup_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_backup_policy_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.update_backup_policy",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "UpdateBackupPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateBackupVault(
        _BaseNetAppRestTransport._BaseUpdateBackupVault, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.UpdateBackupVault")

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
            request: gcn_backup_vault.UpdateBackupVaultRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update backup vault method over HTTP.

            Args:
                request (~.gcn_backup_vault.UpdateBackupVaultRequest):
                    The request object. UpdateBackupVaultRequest updates
                description and/or labels for a
                backupVault.
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
                _BaseNetAppRestTransport._BaseUpdateBackupVault._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_backup_vault(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseUpdateBackupVault,
                    "_BaseUpdateBackupVault__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.UpdateBackupVault",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "UpdateBackupVault",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._UpdateBackupVault._get_response(
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

            resp = self._interceptor.post_update_backup_vault(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_backup_vault_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.update_backup_vault",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "UpdateBackupVault",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateHostGroup(
        _BaseNetAppRestTransport._BaseUpdateHostGroup, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.UpdateHostGroup")

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
            request: gcn_host_group.UpdateHostGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update host group method over HTTP.

            Args:
                request (~.gcn_host_group.UpdateHostGroupRequest):
                    The request object. UpdateHostGroupRequest for updating a
                host group.
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
                _BaseNetAppRestTransport._BaseUpdateHostGroup._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_host_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseUpdateHostGroup,
                    "_BaseUpdateHostGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.UpdateHostGroup",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "UpdateHostGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._UpdateHostGroup._get_response(
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

            resp = self._interceptor.post_update_host_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_host_group_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.update_host_group",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "UpdateHostGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateKmsConfig(
        _BaseNetAppRestTransport._BaseUpdateKmsConfig, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.UpdateKmsConfig")

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
            request: kms.UpdateKmsConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update kms config method over HTTP.

            Args:
                request (~.kms.UpdateKmsConfigRequest):
                    The request object. UpdateKmsConfigRequest updates a KMS
                Config.
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
                _BaseNetAppRestTransport._BaseUpdateKmsConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_kms_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseUpdateKmsConfig,
                    "_BaseUpdateKmsConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.UpdateKmsConfig",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "UpdateKmsConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._UpdateKmsConfig._get_response(
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

            resp = self._interceptor.post_update_kms_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_kms_config_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.update_kms_config",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "UpdateKmsConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateQuotaRule(
        _BaseNetAppRestTransport._BaseUpdateQuotaRule, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.UpdateQuotaRule")

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
            request: gcn_quota_rule.UpdateQuotaRuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update quota rule method over HTTP.

            Args:
                request (~.gcn_quota_rule.UpdateQuotaRuleRequest):
                    The request object. UpdateQuotaRuleRequest for updating a
                quota rule.
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
                _BaseNetAppRestTransport._BaseUpdateQuotaRule._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_quota_rule(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseUpdateQuotaRule,
                    "_BaseUpdateQuotaRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.UpdateQuotaRule",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "UpdateQuotaRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._UpdateQuotaRule._get_response(
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

            resp = self._interceptor.post_update_quota_rule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_quota_rule_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.update_quota_rule",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "UpdateQuotaRule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateReplication(
        _BaseNetAppRestTransport._BaseUpdateReplication, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.UpdateReplication")

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
            request: gcn_replication.UpdateReplicationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update replication method over HTTP.

            Args:
                request (~.gcn_replication.UpdateReplicationRequest):
                    The request object. UpdateReplicationRequest updates
                description and/or labels for a
                replication.
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
                _BaseNetAppRestTransport._BaseUpdateReplication._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_replication(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseUpdateReplication,
                    "_BaseUpdateReplication__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.UpdateReplication",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "UpdateReplication",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._UpdateReplication._get_response(
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

            resp = self._interceptor.post_update_replication(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_replication_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.update_replication",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "UpdateReplication",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateSnapshot(_BaseNetAppRestTransport._BaseUpdateSnapshot, NetAppRestStub):
        def __hash__(self):
            return hash("NetAppRestTransport.UpdateSnapshot")

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
            request: gcn_snapshot.UpdateSnapshotRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update snapshot method over HTTP.

            Args:
                request (~.gcn_snapshot.UpdateSnapshotRequest):
                    The request object. UpdateSnapshotRequest updates
                description and/or labels for a
                snapshot.
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
                _BaseNetAppRestTransport._BaseUpdateSnapshot._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_snapshot(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseUpdateSnapshot,
                    "_BaseUpdateSnapshot__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.UpdateSnapshot",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "UpdateSnapshot",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._UpdateSnapshot._get_response(
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

            resp = self._interceptor.post_update_snapshot(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_snapshot_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.update_snapshot",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "UpdateSnapshot",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateStoragePool(
        _BaseNetAppRestTransport._BaseUpdateStoragePool, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.UpdateStoragePool")

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
            request: gcn_storage_pool.UpdateStoragePoolRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update storage pool method over HTTP.

            Args:
                request (~.gcn_storage_pool.UpdateStoragePoolRequest):
                    The request object. UpdateStoragePoolRequest updates a
                Storage Pool.
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
                _BaseNetAppRestTransport._BaseUpdateStoragePool._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_storage_pool(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseUpdateStoragePool,
                    "_BaseUpdateStoragePool__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.UpdateStoragePool",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "UpdateStoragePool",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._UpdateStoragePool._get_response(
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

            resp = self._interceptor.post_update_storage_pool(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_storage_pool_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.update_storage_pool",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "UpdateStoragePool",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateVolume(_BaseNetAppRestTransport._BaseUpdateVolume, NetAppRestStub):
        def __hash__(self):
            return hash("NetAppRestTransport.UpdateVolume")

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
            request: gcn_volume.UpdateVolumeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update volume method over HTTP.

            Args:
                request (~.gcn_volume.UpdateVolumeRequest):
                    The request object. Message for updating a Volume
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
                _BaseNetAppRestTransport._BaseUpdateVolume._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_volume(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseUpdateVolume,
                    "_BaseUpdateVolume__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.UpdateVolume",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "UpdateVolume",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._UpdateVolume._get_response(
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

            resp = self._interceptor.post_update_volume(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_volume_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.update_volume",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "UpdateVolume",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ValidateDirectoryService(
        _BaseNetAppRestTransport._BaseValidateDirectoryService, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.ValidateDirectoryService")

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
            request: storage_pool.ValidateDirectoryServiceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the validate directory
            service method over HTTP.

                Args:
                    request (~.storage_pool.ValidateDirectoryServiceRequest):
                        The request object. ValidateDirectoryServiceRequest
                    validates the directory service policy
                    attached to the storage pool.
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

            http_options = _BaseNetAppRestTransport._BaseValidateDirectoryService._get_http_options()
            request, metadata = self._interceptor.pre_validate_directory_service(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseValidateDirectoryService,
                    "_BaseValidateDirectoryService__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.ValidateDirectoryService",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ValidateDirectoryService",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._ValidateDirectoryService._get_response(
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

            resp = self._interceptor.post_validate_directory_service(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_validate_directory_service_with_metadata(
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
                    "Received response for google.cloud.netapp_v1.NetAppClient.validate_directory_service",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ValidateDirectoryService",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _VerifyKmsConfig(
        _BaseNetAppRestTransport._BaseVerifyKmsConfig, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.VerifyKmsConfig")

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
            request: kms.VerifyKmsConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> kms.VerifyKmsConfigResponse:
            r"""Call the verify kms config method over HTTP.

            Args:
                request (~.kms.VerifyKmsConfigRequest):
                    The request object. VerifyKmsConfigRequest specifies the
                KMS config to be validated.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.kms.VerifyKmsConfigResponse:
                    VerifyKmsConfigResponse contains the
                information if the config is correctly
                and error message.

            """

            http_options = (
                _BaseNetAppRestTransport._BaseVerifyKmsConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_verify_kms_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseVerifyKmsConfig,
                    "_BaseVerifyKmsConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.VerifyKmsConfig",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "VerifyKmsConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._VerifyKmsConfig._get_response(
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
            resp = kms.VerifyKmsConfigResponse()
            pb_resp = kms.VerifyKmsConfigResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_verify_kms_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_verify_kms_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = kms.VerifyKmsConfigResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.netapp_v1.NetAppClient.verify_kms_config",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "VerifyKmsConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_active_directory(
        self,
    ) -> Callable[
        [gcn_active_directory.CreateActiveDirectoryRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateActiveDirectory(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_backup(
        self,
    ) -> Callable[[gcn_backup.CreateBackupRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateBackup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_backup_policy(
        self,
    ) -> Callable[
        [gcn_backup_policy.CreateBackupPolicyRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateBackupPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_backup_vault(
        self,
    ) -> Callable[
        [gcn_backup_vault.CreateBackupVaultRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateBackupVault(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_host_group(
        self,
    ) -> Callable[[gcn_host_group.CreateHostGroupRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateHostGroup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_kms_config(
        self,
    ) -> Callable[[kms.CreateKmsConfigRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateKmsConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_quota_rule(
        self,
    ) -> Callable[[gcn_quota_rule.CreateQuotaRuleRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateQuotaRule(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_replication(
        self,
    ) -> Callable[[gcn_replication.CreateReplicationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateReplication(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_snapshot(
        self,
    ) -> Callable[[gcn_snapshot.CreateSnapshotRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateSnapshot(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_storage_pool(
        self,
    ) -> Callable[
        [gcn_storage_pool.CreateStoragePoolRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateStoragePool(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_volume(
        self,
    ) -> Callable[[gcn_volume.CreateVolumeRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateVolume(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_active_directory(
        self,
    ) -> Callable[
        [active_directory.DeleteActiveDirectoryRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteActiveDirectory(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_backup(
        self,
    ) -> Callable[[backup.DeleteBackupRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteBackup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_backup_policy(
        self,
    ) -> Callable[[backup_policy.DeleteBackupPolicyRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteBackupPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_backup_vault(
        self,
    ) -> Callable[[backup_vault.DeleteBackupVaultRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteBackupVault(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_host_group(
        self,
    ) -> Callable[[host_group.DeleteHostGroupRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteHostGroup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_kms_config(
        self,
    ) -> Callable[[kms.DeleteKmsConfigRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteKmsConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_quota_rule(
        self,
    ) -> Callable[[quota_rule.DeleteQuotaRuleRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteQuotaRule(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_replication(
        self,
    ) -> Callable[[replication.DeleteReplicationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteReplication(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_snapshot(
        self,
    ) -> Callable[[snapshot.DeleteSnapshotRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteSnapshot(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_storage_pool(
        self,
    ) -> Callable[[storage_pool.DeleteStoragePoolRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteStoragePool(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_volume(
        self,
    ) -> Callable[[volume.DeleteVolumeRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteVolume(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def encrypt_volumes(
        self,
    ) -> Callable[[kms.EncryptVolumesRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._EncryptVolumes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def establish_peering(
        self,
    ) -> Callable[[replication.EstablishPeeringRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._EstablishPeering(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def establish_volume_peering(
        self,
    ) -> Callable[[volume.EstablishVolumePeeringRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._EstablishVolumePeering(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def execute_ontap_delete(
        self,
    ) -> Callable[[ontap.ExecuteOntapDeleteRequest], ontap.ExecuteOntapDeleteResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExecuteOntapDelete(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def execute_ontap_get(
        self,
    ) -> Callable[[ontap.ExecuteOntapGetRequest], ontap.ExecuteOntapGetResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExecuteOntapGet(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def execute_ontap_patch(
        self,
    ) -> Callable[[ontap.ExecuteOntapPatchRequest], ontap.ExecuteOntapPatchResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExecuteOntapPatch(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def execute_ontap_post(
        self,
    ) -> Callable[[ontap.ExecuteOntapPostRequest], ontap.ExecuteOntapPostResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExecuteOntapPost(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_active_directory(
        self,
    ) -> Callable[
        [active_directory.GetActiveDirectoryRequest], active_directory.ActiveDirectory
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetActiveDirectory(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_backup(self) -> Callable[[backup.GetBackupRequest], backup.Backup]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetBackup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_backup_policy(
        self,
    ) -> Callable[[backup_policy.GetBackupPolicyRequest], backup_policy.BackupPolicy]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetBackupPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_backup_vault(
        self,
    ) -> Callable[[backup_vault.GetBackupVaultRequest], backup_vault.BackupVault]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetBackupVault(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_host_group(
        self,
    ) -> Callable[[host_group.GetHostGroupRequest], host_group.HostGroup]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetHostGroup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_kms_config(self) -> Callable[[kms.GetKmsConfigRequest], kms.KmsConfig]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetKmsConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_quota_rule(
        self,
    ) -> Callable[[quota_rule.GetQuotaRuleRequest], quota_rule.QuotaRule]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetQuotaRule(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_replication(
        self,
    ) -> Callable[[replication.GetReplicationRequest], replication.Replication]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetReplication(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_snapshot(
        self,
    ) -> Callable[[snapshot.GetSnapshotRequest], snapshot.Snapshot]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSnapshot(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_split_status(
        self,
    ) -> Callable[[volume.GetSplitStatusRequest], volume.SplitStatus]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSplitStatus(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_storage_pool(
        self,
    ) -> Callable[[storage_pool.GetStoragePoolRequest], storage_pool.StoragePool]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetStoragePool(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_volume(self) -> Callable[[volume.GetVolumeRequest], volume.Volume]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetVolume(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_active_directories(
        self,
    ) -> Callable[
        [active_directory.ListActiveDirectoriesRequest],
        active_directory.ListActiveDirectoriesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListActiveDirectories(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_backup_configs(
        self,
    ) -> Callable[[volume.ListBackupConfigsRequest], volume.ListBackupConfigsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListBackupConfigs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_backup_policies(
        self,
    ) -> Callable[
        [backup_policy.ListBackupPoliciesRequest],
        backup_policy.ListBackupPoliciesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListBackupPolicies(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_backups(
        self,
    ) -> Callable[[backup.ListBackupsRequest], backup.ListBackupsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListBackups(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_backup_vaults(
        self,
    ) -> Callable[
        [backup_vault.ListBackupVaultsRequest], backup_vault.ListBackupVaultsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListBackupVaults(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_host_groups(
        self,
    ) -> Callable[
        [host_group.ListHostGroupsRequest], host_group.ListHostGroupsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListHostGroups(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_kms_configs(
        self,
    ) -> Callable[[kms.ListKmsConfigsRequest], kms.ListKmsConfigsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListKmsConfigs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_quota_rules(
        self,
    ) -> Callable[
        [quota_rule.ListQuotaRulesRequest], quota_rule.ListQuotaRulesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListQuotaRules(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_replications(
        self,
    ) -> Callable[
        [replication.ListReplicationsRequest], replication.ListReplicationsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListReplications(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_snapshots(
        self,
    ) -> Callable[[snapshot.ListSnapshotsRequest], snapshot.ListSnapshotsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSnapshots(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_storage_pools(
        self,
    ) -> Callable[
        [storage_pool.ListStoragePoolsRequest], storage_pool.ListStoragePoolsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListStoragePools(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_volumes(
        self,
    ) -> Callable[[volume.ListVolumesRequest], volume.ListVolumesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListVolumes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def restore_backup_files(
        self,
    ) -> Callable[[volume.RestoreBackupFilesRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RestoreBackupFiles(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def restore_volume(
        self,
    ) -> Callable[[volume.RestoreVolumeRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RestoreVolume(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def resume_replication(
        self,
    ) -> Callable[[replication.ResumeReplicationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ResumeReplication(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def reverse_replication_direction(
        self,
    ) -> Callable[
        [replication.ReverseReplicationDirectionRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ReverseReplicationDirection(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def revert_volume(
        self,
    ) -> Callable[[volume.RevertVolumeRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RevertVolume(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def start_split(
        self,
    ) -> Callable[[volume.StartSplitRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StartSplit(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def stop_replication(
        self,
    ) -> Callable[[replication.StopReplicationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StopReplication(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def switch_active_replica_zone(
        self,
    ) -> Callable[
        [storage_pool.SwitchActiveReplicaZoneRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SwitchActiveReplicaZone(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def sync_replication(
        self,
    ) -> Callable[[replication.SyncReplicationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SyncReplication(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_active_directory(
        self,
    ) -> Callable[
        [gcn_active_directory.UpdateActiveDirectoryRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateActiveDirectory(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_backup(
        self,
    ) -> Callable[[gcn_backup.UpdateBackupRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateBackup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_backup_config(
        self,
    ) -> Callable[[volume.UpdateBackupConfigRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateBackupConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_backup_policy(
        self,
    ) -> Callable[
        [gcn_backup_policy.UpdateBackupPolicyRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateBackupPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_backup_vault(
        self,
    ) -> Callable[
        [gcn_backup_vault.UpdateBackupVaultRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateBackupVault(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_host_group(
        self,
    ) -> Callable[[gcn_host_group.UpdateHostGroupRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateHostGroup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_kms_config(
        self,
    ) -> Callable[[kms.UpdateKmsConfigRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateKmsConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_quota_rule(
        self,
    ) -> Callable[[gcn_quota_rule.UpdateQuotaRuleRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateQuotaRule(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_replication(
        self,
    ) -> Callable[[gcn_replication.UpdateReplicationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateReplication(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_snapshot(
        self,
    ) -> Callable[[gcn_snapshot.UpdateSnapshotRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateSnapshot(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_storage_pool(
        self,
    ) -> Callable[
        [gcn_storage_pool.UpdateStoragePoolRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateStoragePool(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_volume(
        self,
    ) -> Callable[[gcn_volume.UpdateVolumeRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateVolume(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def validate_directory_service(
        self,
    ) -> Callable[
        [storage_pool.ValidateDirectoryServiceRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ValidateDirectoryService(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def verify_kms_config(
        self,
    ) -> Callable[[kms.VerifyKmsConfigRequest], kms.VerifyKmsConfigResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._VerifyKmsConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(_BaseNetAppRestTransport._BaseGetLocation, NetAppRestStub):
        def __hash__(self):
            return hash("NetAppRestTransport.GetLocation")

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

            http_options = _BaseNetAppRestTransport._BaseGetLocation._get_http_options()
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.netapp_v1.NetAppAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "GetLocation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_locations(self):
        return self._ListLocations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListLocations(_BaseNetAppRestTransport._BaseListLocations, NetAppRestStub):
        def __hash__(self):
            return hash("NetAppRestTransport.ListLocations")

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
                _BaseNetAppRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.netapp_v1.NetAppAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
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
        _BaseNetAppRestTransport._BaseCancelOperation, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.CancelOperation")

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

            http_options = (
                _BaseNetAppRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._CancelOperation._get_response(
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
        _BaseNetAppRestTransport._BaseDeleteOperation, NetAppRestStub
    ):
        def __hash__(self):
            return hash("NetAppRestTransport.DeleteOperation")

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
                _BaseNetAppRestTransport._BaseDeleteOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._DeleteOperation._get_response(
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

    class _GetOperation(_BaseNetAppRestTransport._BaseGetOperation, NetAppRestStub):
        def __hash__(self):
            return hash("NetAppRestTransport.GetOperation")

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
                _BaseNetAppRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.netapp_v1.NetAppAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "GetOperation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_operations(self):
        return self._ListOperations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListOperations(_BaseNetAppRestTransport._BaseListOperations, NetAppRestStub):
        def __hash__(self):
            return hash("NetAppRestTransport.ListOperations")

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
                _BaseNetAppRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseNetAppRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.netapp_v1.NetAppClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = NetAppRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.netapp_v1.NetAppAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.netapp.v1.NetApp",
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


__all__ = ("NetAppRestTransport",)
