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
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.backupdr_v1._compat import transcode_request
from google.cloud.backupdr_v1.types import (
    backupdr,
    backupplan,
    backupplanassociation,
    backupvault,
    datasourcereference,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseBackupDRRestTransport

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


class BackupDRRestInterceptor:
    """Interceptor for BackupDR.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the BackupDRRestTransport.

    .. code-block:: python
        class MyCustomBackupDRInterceptor(BackupDRRestInterceptor):
            def pre_create_backup_plan(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_backup_plan(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_backup_plan_association(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_backup_plan_association(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_backup_vault(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_backup_vault(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_management_server(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_management_server(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_backup(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_backup(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_backup_plan(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_backup_plan(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_backup_plan_association(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_backup_plan_association(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_backup_vault(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_backup_vault(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_management_server(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_management_server(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_backup_plan_associations_for_resource_type(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_backup_plan_associations_for_resource_type(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_backups_for_resource_type(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_backups_for_resource_type(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_data_source_references_for_resource_type(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_data_source_references_for_resource_type(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_usable_backup_vaults(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_usable_backup_vaults(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_backup(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_backup(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_backup_plan(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_backup_plan(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_backup_plan_association(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_backup_plan_association(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_backup_plan_revision(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_backup_plan_revision(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_backup_vault(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_backup_vault(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_data_source(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_data_source(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_data_source_reference(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_data_source_reference(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_management_server(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_management_server(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_initialize_service(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_initialize_service(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_backup_plan_associations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_backup_plan_associations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_backup_plan_revisions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_backup_plan_revisions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_backup_plans(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_backup_plans(self, response):
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

            def pre_list_data_source_references(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_data_source_references(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_data_sources(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_data_sources(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_management_servers(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_management_servers(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_restore_backup(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_restore_backup(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_trigger_backup(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_trigger_backup(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_backup(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_backup(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_backup_plan(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_backup_plan(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_backup_plan_association(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_backup_plan_association(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_backup_vault(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_backup_vault(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_data_source(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_data_source(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = BackupDRRestTransport(interceptor=MyCustomBackupDRInterceptor())
        client = BackupDRClient(transport=transport)


    """

    def pre_create_backup_plan(
        self,
        request: backupplan.CreateBackupPlanRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupplan.CreateBackupPlanRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_backup_plan

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_create_backup_plan(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_backup_plan

        DEPRECATED. Please use the `post_create_backup_plan_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code. This `post_create_backup_plan` interceptor runs
        before the `post_create_backup_plan_with_metadata` interceptor.
        """
        return response

    def post_create_backup_plan_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_backup_plan

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_create_backup_plan_with_metadata`
        interceptor in new development instead of the `post_create_backup_plan` interceptor.
        When both interceptors are used, this `post_create_backup_plan_with_metadata` interceptor runs after the
        `post_create_backup_plan` interceptor. The (possibly modified) response returned by
        `post_create_backup_plan` will be passed to
        `post_create_backup_plan_with_metadata`.
        """
        return response, metadata

    def pre_create_backup_plan_association(
        self,
        request: backupplanassociation.CreateBackupPlanAssociationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupplanassociation.CreateBackupPlanAssociationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_backup_plan_association

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_create_backup_plan_association(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_backup_plan_association

        DEPRECATED. Please use the `post_create_backup_plan_association_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code. This `post_create_backup_plan_association` interceptor runs
        before the `post_create_backup_plan_association_with_metadata` interceptor.
        """
        return response

    def post_create_backup_plan_association_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_backup_plan_association

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_create_backup_plan_association_with_metadata`
        interceptor in new development instead of the `post_create_backup_plan_association` interceptor.
        When both interceptors are used, this `post_create_backup_plan_association_with_metadata` interceptor runs after the
        `post_create_backup_plan_association` interceptor. The (possibly modified) response returned by
        `post_create_backup_plan_association` will be passed to
        `post_create_backup_plan_association_with_metadata`.
        """
        return response, metadata

    def pre_create_backup_vault(
        self,
        request: backupvault.CreateBackupVaultRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupvault.CreateBackupVaultRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_backup_vault

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_create_backup_vault(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_backup_vault

        DEPRECATED. Please use the `post_create_backup_vault_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
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
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_create_backup_vault_with_metadata`
        interceptor in new development instead of the `post_create_backup_vault` interceptor.
        When both interceptors are used, this `post_create_backup_vault_with_metadata` interceptor runs after the
        `post_create_backup_vault` interceptor. The (possibly modified) response returned by
        `post_create_backup_vault` will be passed to
        `post_create_backup_vault_with_metadata`.
        """
        return response, metadata

    def pre_create_management_server(
        self,
        request: backupdr.CreateManagementServerRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupdr.CreateManagementServerRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_management_server

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_create_management_server(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_management_server

        DEPRECATED. Please use the `post_create_management_server_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code. This `post_create_management_server` interceptor runs
        before the `post_create_management_server_with_metadata` interceptor.
        """
        return response

    def post_create_management_server_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_management_server

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_create_management_server_with_metadata`
        interceptor in new development instead of the `post_create_management_server` interceptor.
        When both interceptors are used, this `post_create_management_server_with_metadata` interceptor runs after the
        `post_create_management_server` interceptor. The (possibly modified) response returned by
        `post_create_management_server` will be passed to
        `post_create_management_server_with_metadata`.
        """
        return response, metadata

    def pre_delete_backup(
        self,
        request: backupvault.DeleteBackupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupvault.DeleteBackupRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_backup

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_delete_backup(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_backup

        DEPRECATED. Please use the `post_delete_backup_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
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
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_delete_backup_with_metadata`
        interceptor in new development instead of the `post_delete_backup` interceptor.
        When both interceptors are used, this `post_delete_backup_with_metadata` interceptor runs after the
        `post_delete_backup` interceptor. The (possibly modified) response returned by
        `post_delete_backup` will be passed to
        `post_delete_backup_with_metadata`.
        """
        return response, metadata

    def pre_delete_backup_plan(
        self,
        request: backupplan.DeleteBackupPlanRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupplan.DeleteBackupPlanRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_backup_plan

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_delete_backup_plan(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_backup_plan

        DEPRECATED. Please use the `post_delete_backup_plan_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code. This `post_delete_backup_plan` interceptor runs
        before the `post_delete_backup_plan_with_metadata` interceptor.
        """
        return response

    def post_delete_backup_plan_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_backup_plan

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_delete_backup_plan_with_metadata`
        interceptor in new development instead of the `post_delete_backup_plan` interceptor.
        When both interceptors are used, this `post_delete_backup_plan_with_metadata` interceptor runs after the
        `post_delete_backup_plan` interceptor. The (possibly modified) response returned by
        `post_delete_backup_plan` will be passed to
        `post_delete_backup_plan_with_metadata`.
        """
        return response, metadata

    def pre_delete_backup_plan_association(
        self,
        request: backupplanassociation.DeleteBackupPlanAssociationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupplanassociation.DeleteBackupPlanAssociationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_backup_plan_association

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_delete_backup_plan_association(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_backup_plan_association

        DEPRECATED. Please use the `post_delete_backup_plan_association_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code. This `post_delete_backup_plan_association` interceptor runs
        before the `post_delete_backup_plan_association_with_metadata` interceptor.
        """
        return response

    def post_delete_backup_plan_association_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_backup_plan_association

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_delete_backup_plan_association_with_metadata`
        interceptor in new development instead of the `post_delete_backup_plan_association` interceptor.
        When both interceptors are used, this `post_delete_backup_plan_association_with_metadata` interceptor runs after the
        `post_delete_backup_plan_association` interceptor. The (possibly modified) response returned by
        `post_delete_backup_plan_association` will be passed to
        `post_delete_backup_plan_association_with_metadata`.
        """
        return response, metadata

    def pre_delete_backup_vault(
        self,
        request: backupvault.DeleteBackupVaultRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupvault.DeleteBackupVaultRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_backup_vault

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_delete_backup_vault(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_backup_vault

        DEPRECATED. Please use the `post_delete_backup_vault_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
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
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_delete_backup_vault_with_metadata`
        interceptor in new development instead of the `post_delete_backup_vault` interceptor.
        When both interceptors are used, this `post_delete_backup_vault_with_metadata` interceptor runs after the
        `post_delete_backup_vault` interceptor. The (possibly modified) response returned by
        `post_delete_backup_vault` will be passed to
        `post_delete_backup_vault_with_metadata`.
        """
        return response, metadata

    def pre_delete_management_server(
        self,
        request: backupdr.DeleteManagementServerRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupdr.DeleteManagementServerRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_management_server

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_delete_management_server(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_management_server

        DEPRECATED. Please use the `post_delete_management_server_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code. This `post_delete_management_server` interceptor runs
        before the `post_delete_management_server_with_metadata` interceptor.
        """
        return response

    def post_delete_management_server_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_management_server

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_delete_management_server_with_metadata`
        interceptor in new development instead of the `post_delete_management_server` interceptor.
        When both interceptors are used, this `post_delete_management_server_with_metadata` interceptor runs after the
        `post_delete_management_server` interceptor. The (possibly modified) response returned by
        `post_delete_management_server` will be passed to
        `post_delete_management_server_with_metadata`.
        """
        return response, metadata

    def pre_fetch_backup_plan_associations_for_resource_type(
        self,
        request: backupplanassociation.FetchBackupPlanAssociationsForResourceTypeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupplanassociation.FetchBackupPlanAssociationsForResourceTypeRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for fetch_backup_plan_associations_for_resource_type

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_fetch_backup_plan_associations_for_resource_type(
        self,
        response: backupplanassociation.FetchBackupPlanAssociationsForResourceTypeResponse,
    ) -> backupplanassociation.FetchBackupPlanAssociationsForResourceTypeResponse:
        """Post-rpc interceptor for fetch_backup_plan_associations_for_resource_type

        DEPRECATED. Please use the `post_fetch_backup_plan_associations_for_resource_type_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code. This `post_fetch_backup_plan_associations_for_resource_type` interceptor runs
        before the `post_fetch_backup_plan_associations_for_resource_type_with_metadata` interceptor.
        """
        return response

    def post_fetch_backup_plan_associations_for_resource_type_with_metadata(
        self,
        response: backupplanassociation.FetchBackupPlanAssociationsForResourceTypeResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupplanassociation.FetchBackupPlanAssociationsForResourceTypeResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for fetch_backup_plan_associations_for_resource_type

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_fetch_backup_plan_associations_for_resource_type_with_metadata`
        interceptor in new development instead of the `post_fetch_backup_plan_associations_for_resource_type` interceptor.
        When both interceptors are used, this `post_fetch_backup_plan_associations_for_resource_type_with_metadata` interceptor runs after the
        `post_fetch_backup_plan_associations_for_resource_type` interceptor. The (possibly modified) response returned by
        `post_fetch_backup_plan_associations_for_resource_type` will be passed to
        `post_fetch_backup_plan_associations_for_resource_type_with_metadata`.
        """
        return response, metadata

    def pre_fetch_backups_for_resource_type(
        self,
        request: backupvault.FetchBackupsForResourceTypeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupvault.FetchBackupsForResourceTypeRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for fetch_backups_for_resource_type

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_fetch_backups_for_resource_type(
        self, response: backupvault.FetchBackupsForResourceTypeResponse
    ) -> backupvault.FetchBackupsForResourceTypeResponse:
        """Post-rpc interceptor for fetch_backups_for_resource_type

        DEPRECATED. Please use the `post_fetch_backups_for_resource_type_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code. This `post_fetch_backups_for_resource_type` interceptor runs
        before the `post_fetch_backups_for_resource_type_with_metadata` interceptor.
        """
        return response

    def post_fetch_backups_for_resource_type_with_metadata(
        self,
        response: backupvault.FetchBackupsForResourceTypeResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupvault.FetchBackupsForResourceTypeResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for fetch_backups_for_resource_type

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_fetch_backups_for_resource_type_with_metadata`
        interceptor in new development instead of the `post_fetch_backups_for_resource_type` interceptor.
        When both interceptors are used, this `post_fetch_backups_for_resource_type_with_metadata` interceptor runs after the
        `post_fetch_backups_for_resource_type` interceptor. The (possibly modified) response returned by
        `post_fetch_backups_for_resource_type` will be passed to
        `post_fetch_backups_for_resource_type_with_metadata`.
        """
        return response, metadata

    def pre_fetch_data_source_references_for_resource_type(
        self,
        request: datasourcereference.FetchDataSourceReferencesForResourceTypeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datasourcereference.FetchDataSourceReferencesForResourceTypeRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for fetch_data_source_references_for_resource_type

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_fetch_data_source_references_for_resource_type(
        self,
        response: datasourcereference.FetchDataSourceReferencesForResourceTypeResponse,
    ) -> datasourcereference.FetchDataSourceReferencesForResourceTypeResponse:
        """Post-rpc interceptor for fetch_data_source_references_for_resource_type

        DEPRECATED. Please use the `post_fetch_data_source_references_for_resource_type_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code. This `post_fetch_data_source_references_for_resource_type` interceptor runs
        before the `post_fetch_data_source_references_for_resource_type_with_metadata` interceptor.
        """
        return response

    def post_fetch_data_source_references_for_resource_type_with_metadata(
        self,
        response: datasourcereference.FetchDataSourceReferencesForResourceTypeResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datasourcereference.FetchDataSourceReferencesForResourceTypeResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for fetch_data_source_references_for_resource_type

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_fetch_data_source_references_for_resource_type_with_metadata`
        interceptor in new development instead of the `post_fetch_data_source_references_for_resource_type` interceptor.
        When both interceptors are used, this `post_fetch_data_source_references_for_resource_type_with_metadata` interceptor runs after the
        `post_fetch_data_source_references_for_resource_type` interceptor. The (possibly modified) response returned by
        `post_fetch_data_source_references_for_resource_type` will be passed to
        `post_fetch_data_source_references_for_resource_type_with_metadata`.
        """
        return response, metadata

    def pre_fetch_usable_backup_vaults(
        self,
        request: backupvault.FetchUsableBackupVaultsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupvault.FetchUsableBackupVaultsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for fetch_usable_backup_vaults

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_fetch_usable_backup_vaults(
        self, response: backupvault.FetchUsableBackupVaultsResponse
    ) -> backupvault.FetchUsableBackupVaultsResponse:
        """Post-rpc interceptor for fetch_usable_backup_vaults

        DEPRECATED. Please use the `post_fetch_usable_backup_vaults_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code. This `post_fetch_usable_backup_vaults` interceptor runs
        before the `post_fetch_usable_backup_vaults_with_metadata` interceptor.
        """
        return response

    def post_fetch_usable_backup_vaults_with_metadata(
        self,
        response: backupvault.FetchUsableBackupVaultsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupvault.FetchUsableBackupVaultsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for fetch_usable_backup_vaults

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_fetch_usable_backup_vaults_with_metadata`
        interceptor in new development instead of the `post_fetch_usable_backup_vaults` interceptor.
        When both interceptors are used, this `post_fetch_usable_backup_vaults_with_metadata` interceptor runs after the
        `post_fetch_usable_backup_vaults` interceptor. The (possibly modified) response returned by
        `post_fetch_usable_backup_vaults` will be passed to
        `post_fetch_usable_backup_vaults_with_metadata`.
        """
        return response, metadata

    def pre_get_backup(
        self,
        request: backupvault.GetBackupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[backupvault.GetBackupRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_backup

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_get_backup(self, response: backupvault.Backup) -> backupvault.Backup:
        """Post-rpc interceptor for get_backup

        DEPRECATED. Please use the `post_get_backup_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code. This `post_get_backup` interceptor runs
        before the `post_get_backup_with_metadata` interceptor.
        """
        return response

    def post_get_backup_with_metadata(
        self,
        response: backupvault.Backup,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[backupvault.Backup, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_backup

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_get_backup_with_metadata`
        interceptor in new development instead of the `post_get_backup` interceptor.
        When both interceptors are used, this `post_get_backup_with_metadata` interceptor runs after the
        `post_get_backup` interceptor. The (possibly modified) response returned by
        `post_get_backup` will be passed to
        `post_get_backup_with_metadata`.
        """
        return response, metadata

    def pre_get_backup_plan(
        self,
        request: backupplan.GetBackupPlanRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupplan.GetBackupPlanRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_backup_plan

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_get_backup_plan(
        self, response: backupplan.BackupPlan
    ) -> backupplan.BackupPlan:
        """Post-rpc interceptor for get_backup_plan

        DEPRECATED. Please use the `post_get_backup_plan_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code. This `post_get_backup_plan` interceptor runs
        before the `post_get_backup_plan_with_metadata` interceptor.
        """
        return response

    def post_get_backup_plan_with_metadata(
        self,
        response: backupplan.BackupPlan,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[backupplan.BackupPlan, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_backup_plan

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_get_backup_plan_with_metadata`
        interceptor in new development instead of the `post_get_backup_plan` interceptor.
        When both interceptors are used, this `post_get_backup_plan_with_metadata` interceptor runs after the
        `post_get_backup_plan` interceptor. The (possibly modified) response returned by
        `post_get_backup_plan` will be passed to
        `post_get_backup_plan_with_metadata`.
        """
        return response, metadata

    def pre_get_backup_plan_association(
        self,
        request: backupplanassociation.GetBackupPlanAssociationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupplanassociation.GetBackupPlanAssociationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_backup_plan_association

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_get_backup_plan_association(
        self, response: backupplanassociation.BackupPlanAssociation
    ) -> backupplanassociation.BackupPlanAssociation:
        """Post-rpc interceptor for get_backup_plan_association

        DEPRECATED. Please use the `post_get_backup_plan_association_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code. This `post_get_backup_plan_association` interceptor runs
        before the `post_get_backup_plan_association_with_metadata` interceptor.
        """
        return response

    def post_get_backup_plan_association_with_metadata(
        self,
        response: backupplanassociation.BackupPlanAssociation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupplanassociation.BackupPlanAssociation,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_backup_plan_association

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_get_backup_plan_association_with_metadata`
        interceptor in new development instead of the `post_get_backup_plan_association` interceptor.
        When both interceptors are used, this `post_get_backup_plan_association_with_metadata` interceptor runs after the
        `post_get_backup_plan_association` interceptor. The (possibly modified) response returned by
        `post_get_backup_plan_association` will be passed to
        `post_get_backup_plan_association_with_metadata`.
        """
        return response, metadata

    def pre_get_backup_plan_revision(
        self,
        request: backupplan.GetBackupPlanRevisionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupplan.GetBackupPlanRevisionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_backup_plan_revision

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_get_backup_plan_revision(
        self, response: backupplan.BackupPlanRevision
    ) -> backupplan.BackupPlanRevision:
        """Post-rpc interceptor for get_backup_plan_revision

        DEPRECATED. Please use the `post_get_backup_plan_revision_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code. This `post_get_backup_plan_revision` interceptor runs
        before the `post_get_backup_plan_revision_with_metadata` interceptor.
        """
        return response

    def post_get_backup_plan_revision_with_metadata(
        self,
        response: backupplan.BackupPlanRevision,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[backupplan.BackupPlanRevision, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_backup_plan_revision

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_get_backup_plan_revision_with_metadata`
        interceptor in new development instead of the `post_get_backup_plan_revision` interceptor.
        When both interceptors are used, this `post_get_backup_plan_revision_with_metadata` interceptor runs after the
        `post_get_backup_plan_revision` interceptor. The (possibly modified) response returned by
        `post_get_backup_plan_revision` will be passed to
        `post_get_backup_plan_revision_with_metadata`.
        """
        return response, metadata

    def pre_get_backup_vault(
        self,
        request: backupvault.GetBackupVaultRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupvault.GetBackupVaultRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_backup_vault

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_get_backup_vault(
        self, response: backupvault.BackupVault
    ) -> backupvault.BackupVault:
        """Post-rpc interceptor for get_backup_vault

        DEPRECATED. Please use the `post_get_backup_vault_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code. This `post_get_backup_vault` interceptor runs
        before the `post_get_backup_vault_with_metadata` interceptor.
        """
        return response

    def post_get_backup_vault_with_metadata(
        self,
        response: backupvault.BackupVault,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[backupvault.BackupVault, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_backup_vault

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_get_backup_vault_with_metadata`
        interceptor in new development instead of the `post_get_backup_vault` interceptor.
        When both interceptors are used, this `post_get_backup_vault_with_metadata` interceptor runs after the
        `post_get_backup_vault` interceptor. The (possibly modified) response returned by
        `post_get_backup_vault` will be passed to
        `post_get_backup_vault_with_metadata`.
        """
        return response, metadata

    def pre_get_data_source(
        self,
        request: backupvault.GetDataSourceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupvault.GetDataSourceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_data_source

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_get_data_source(
        self, response: backupvault.DataSource
    ) -> backupvault.DataSource:
        """Post-rpc interceptor for get_data_source

        DEPRECATED. Please use the `post_get_data_source_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code. This `post_get_data_source` interceptor runs
        before the `post_get_data_source_with_metadata` interceptor.
        """
        return response

    def post_get_data_source_with_metadata(
        self,
        response: backupvault.DataSource,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[backupvault.DataSource, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_data_source

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_get_data_source_with_metadata`
        interceptor in new development instead of the `post_get_data_source` interceptor.
        When both interceptors are used, this `post_get_data_source_with_metadata` interceptor runs after the
        `post_get_data_source` interceptor. The (possibly modified) response returned by
        `post_get_data_source` will be passed to
        `post_get_data_source_with_metadata`.
        """
        return response, metadata

    def pre_get_data_source_reference(
        self,
        request: datasourcereference.GetDataSourceReferenceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datasourcereference.GetDataSourceReferenceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_data_source_reference

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_get_data_source_reference(
        self, response: datasourcereference.DataSourceReference
    ) -> datasourcereference.DataSourceReference:
        """Post-rpc interceptor for get_data_source_reference

        DEPRECATED. Please use the `post_get_data_source_reference_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code. This `post_get_data_source_reference` interceptor runs
        before the `post_get_data_source_reference_with_metadata` interceptor.
        """
        return response

    def post_get_data_source_reference_with_metadata(
        self,
        response: datasourcereference.DataSourceReference,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datasourcereference.DataSourceReference, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_data_source_reference

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_get_data_source_reference_with_metadata`
        interceptor in new development instead of the `post_get_data_source_reference` interceptor.
        When both interceptors are used, this `post_get_data_source_reference_with_metadata` interceptor runs after the
        `post_get_data_source_reference` interceptor. The (possibly modified) response returned by
        `post_get_data_source_reference` will be passed to
        `post_get_data_source_reference_with_metadata`.
        """
        return response, metadata

    def pre_get_management_server(
        self,
        request: backupdr.GetManagementServerRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupdr.GetManagementServerRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_management_server

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_get_management_server(
        self, response: backupdr.ManagementServer
    ) -> backupdr.ManagementServer:
        """Post-rpc interceptor for get_management_server

        DEPRECATED. Please use the `post_get_management_server_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code. This `post_get_management_server` interceptor runs
        before the `post_get_management_server_with_metadata` interceptor.
        """
        return response

    def post_get_management_server_with_metadata(
        self,
        response: backupdr.ManagementServer,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[backupdr.ManagementServer, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_management_server

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_get_management_server_with_metadata`
        interceptor in new development instead of the `post_get_management_server` interceptor.
        When both interceptors are used, this `post_get_management_server_with_metadata` interceptor runs after the
        `post_get_management_server` interceptor. The (possibly modified) response returned by
        `post_get_management_server` will be passed to
        `post_get_management_server_with_metadata`.
        """
        return response, metadata

    def pre_initialize_service(
        self,
        request: backupdr.InitializeServiceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupdr.InitializeServiceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for initialize_service

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_initialize_service(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for initialize_service

        DEPRECATED. Please use the `post_initialize_service_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code. This `post_initialize_service` interceptor runs
        before the `post_initialize_service_with_metadata` interceptor.
        """
        return response

    def post_initialize_service_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for initialize_service

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_initialize_service_with_metadata`
        interceptor in new development instead of the `post_initialize_service` interceptor.
        When both interceptors are used, this `post_initialize_service_with_metadata` interceptor runs after the
        `post_initialize_service` interceptor. The (possibly modified) response returned by
        `post_initialize_service` will be passed to
        `post_initialize_service_with_metadata`.
        """
        return response, metadata

    def pre_list_backup_plan_associations(
        self,
        request: backupplanassociation.ListBackupPlanAssociationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupplanassociation.ListBackupPlanAssociationsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_backup_plan_associations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_list_backup_plan_associations(
        self, response: backupplanassociation.ListBackupPlanAssociationsResponse
    ) -> backupplanassociation.ListBackupPlanAssociationsResponse:
        """Post-rpc interceptor for list_backup_plan_associations

        DEPRECATED. Please use the `post_list_backup_plan_associations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code. This `post_list_backup_plan_associations` interceptor runs
        before the `post_list_backup_plan_associations_with_metadata` interceptor.
        """
        return response

    def post_list_backup_plan_associations_with_metadata(
        self,
        response: backupplanassociation.ListBackupPlanAssociationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupplanassociation.ListBackupPlanAssociationsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_backup_plan_associations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_list_backup_plan_associations_with_metadata`
        interceptor in new development instead of the `post_list_backup_plan_associations` interceptor.
        When both interceptors are used, this `post_list_backup_plan_associations_with_metadata` interceptor runs after the
        `post_list_backup_plan_associations` interceptor. The (possibly modified) response returned by
        `post_list_backup_plan_associations` will be passed to
        `post_list_backup_plan_associations_with_metadata`.
        """
        return response, metadata

    def pre_list_backup_plan_revisions(
        self,
        request: backupplan.ListBackupPlanRevisionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupplan.ListBackupPlanRevisionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_backup_plan_revisions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_list_backup_plan_revisions(
        self, response: backupplan.ListBackupPlanRevisionsResponse
    ) -> backupplan.ListBackupPlanRevisionsResponse:
        """Post-rpc interceptor for list_backup_plan_revisions

        DEPRECATED. Please use the `post_list_backup_plan_revisions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code. This `post_list_backup_plan_revisions` interceptor runs
        before the `post_list_backup_plan_revisions_with_metadata` interceptor.
        """
        return response

    def post_list_backup_plan_revisions_with_metadata(
        self,
        response: backupplan.ListBackupPlanRevisionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupplan.ListBackupPlanRevisionsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_backup_plan_revisions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_list_backup_plan_revisions_with_metadata`
        interceptor in new development instead of the `post_list_backup_plan_revisions` interceptor.
        When both interceptors are used, this `post_list_backup_plan_revisions_with_metadata` interceptor runs after the
        `post_list_backup_plan_revisions` interceptor. The (possibly modified) response returned by
        `post_list_backup_plan_revisions` will be passed to
        `post_list_backup_plan_revisions_with_metadata`.
        """
        return response, metadata

    def pre_list_backup_plans(
        self,
        request: backupplan.ListBackupPlansRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupplan.ListBackupPlansRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_backup_plans

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_list_backup_plans(
        self, response: backupplan.ListBackupPlansResponse
    ) -> backupplan.ListBackupPlansResponse:
        """Post-rpc interceptor for list_backup_plans

        DEPRECATED. Please use the `post_list_backup_plans_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code. This `post_list_backup_plans` interceptor runs
        before the `post_list_backup_plans_with_metadata` interceptor.
        """
        return response

    def post_list_backup_plans_with_metadata(
        self,
        response: backupplan.ListBackupPlansResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupplan.ListBackupPlansResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_backup_plans

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_list_backup_plans_with_metadata`
        interceptor in new development instead of the `post_list_backup_plans` interceptor.
        When both interceptors are used, this `post_list_backup_plans_with_metadata` interceptor runs after the
        `post_list_backup_plans` interceptor. The (possibly modified) response returned by
        `post_list_backup_plans` will be passed to
        `post_list_backup_plans_with_metadata`.
        """
        return response, metadata

    def pre_list_backups(
        self,
        request: backupvault.ListBackupsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[backupvault.ListBackupsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_backups

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_list_backups(
        self, response: backupvault.ListBackupsResponse
    ) -> backupvault.ListBackupsResponse:
        """Post-rpc interceptor for list_backups

        DEPRECATED. Please use the `post_list_backups_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code. This `post_list_backups` interceptor runs
        before the `post_list_backups_with_metadata` interceptor.
        """
        return response

    def post_list_backups_with_metadata(
        self,
        response: backupvault.ListBackupsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupvault.ListBackupsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_backups

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupDR server but before it is returned to user code.

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
        request: backupvault.ListBackupVaultsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupvault.ListBackupVaultsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_backup_vaults

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_list_backup_vaults(
        self, response: backupvault.ListBackupVaultsResponse
    ) -> backupvault.ListBackupVaultsResponse:
        """Post-rpc interceptor for list_backup_vaults

        DEPRECATED. Please use the `post_list_backup_vaults_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code. This `post_list_backup_vaults` interceptor runs
        before the `post_list_backup_vaults_with_metadata` interceptor.
        """
        return response

    def post_list_backup_vaults_with_metadata(
        self,
        response: backupvault.ListBackupVaultsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupvault.ListBackupVaultsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_backup_vaults

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_list_backup_vaults_with_metadata`
        interceptor in new development instead of the `post_list_backup_vaults` interceptor.
        When both interceptors are used, this `post_list_backup_vaults_with_metadata` interceptor runs after the
        `post_list_backup_vaults` interceptor. The (possibly modified) response returned by
        `post_list_backup_vaults` will be passed to
        `post_list_backup_vaults_with_metadata`.
        """
        return response, metadata

    def pre_list_data_source_references(
        self,
        request: datasourcereference.ListDataSourceReferencesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datasourcereference.ListDataSourceReferencesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_data_source_references

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_list_data_source_references(
        self, response: datasourcereference.ListDataSourceReferencesResponse
    ) -> datasourcereference.ListDataSourceReferencesResponse:
        """Post-rpc interceptor for list_data_source_references

        DEPRECATED. Please use the `post_list_data_source_references_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code. This `post_list_data_source_references` interceptor runs
        before the `post_list_data_source_references_with_metadata` interceptor.
        """
        return response

    def post_list_data_source_references_with_metadata(
        self,
        response: datasourcereference.ListDataSourceReferencesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        datasourcereference.ListDataSourceReferencesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_data_source_references

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_list_data_source_references_with_metadata`
        interceptor in new development instead of the `post_list_data_source_references` interceptor.
        When both interceptors are used, this `post_list_data_source_references_with_metadata` interceptor runs after the
        `post_list_data_source_references` interceptor. The (possibly modified) response returned by
        `post_list_data_source_references` will be passed to
        `post_list_data_source_references_with_metadata`.
        """
        return response, metadata

    def pre_list_data_sources(
        self,
        request: backupvault.ListDataSourcesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupvault.ListDataSourcesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_data_sources

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_list_data_sources(
        self, response: backupvault.ListDataSourcesResponse
    ) -> backupvault.ListDataSourcesResponse:
        """Post-rpc interceptor for list_data_sources

        DEPRECATED. Please use the `post_list_data_sources_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code. This `post_list_data_sources` interceptor runs
        before the `post_list_data_sources_with_metadata` interceptor.
        """
        return response

    def post_list_data_sources_with_metadata(
        self,
        response: backupvault.ListDataSourcesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupvault.ListDataSourcesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_data_sources

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_list_data_sources_with_metadata`
        interceptor in new development instead of the `post_list_data_sources` interceptor.
        When both interceptors are used, this `post_list_data_sources_with_metadata` interceptor runs after the
        `post_list_data_sources` interceptor. The (possibly modified) response returned by
        `post_list_data_sources` will be passed to
        `post_list_data_sources_with_metadata`.
        """
        return response, metadata

    def pre_list_management_servers(
        self,
        request: backupdr.ListManagementServersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupdr.ListManagementServersRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_management_servers

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_list_management_servers(
        self, response: backupdr.ListManagementServersResponse
    ) -> backupdr.ListManagementServersResponse:
        """Post-rpc interceptor for list_management_servers

        DEPRECATED. Please use the `post_list_management_servers_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code. This `post_list_management_servers` interceptor runs
        before the `post_list_management_servers_with_metadata` interceptor.
        """
        return response

    def post_list_management_servers_with_metadata(
        self,
        response: backupdr.ListManagementServersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupdr.ListManagementServersResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_management_servers

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_list_management_servers_with_metadata`
        interceptor in new development instead of the `post_list_management_servers` interceptor.
        When both interceptors are used, this `post_list_management_servers_with_metadata` interceptor runs after the
        `post_list_management_servers` interceptor. The (possibly modified) response returned by
        `post_list_management_servers` will be passed to
        `post_list_management_servers_with_metadata`.
        """
        return response, metadata

    def pre_restore_backup(
        self,
        request: backupvault.RestoreBackupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupvault.RestoreBackupRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for restore_backup

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_restore_backup(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for restore_backup

        DEPRECATED. Please use the `post_restore_backup_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code. This `post_restore_backup` interceptor runs
        before the `post_restore_backup_with_metadata` interceptor.
        """
        return response

    def post_restore_backup_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for restore_backup

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_restore_backup_with_metadata`
        interceptor in new development instead of the `post_restore_backup` interceptor.
        When both interceptors are used, this `post_restore_backup_with_metadata` interceptor runs after the
        `post_restore_backup` interceptor. The (possibly modified) response returned by
        `post_restore_backup` will be passed to
        `post_restore_backup_with_metadata`.
        """
        return response, metadata

    def pre_trigger_backup(
        self,
        request: backupplanassociation.TriggerBackupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupplanassociation.TriggerBackupRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for trigger_backup

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_trigger_backup(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for trigger_backup

        DEPRECATED. Please use the `post_trigger_backup_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code. This `post_trigger_backup` interceptor runs
        before the `post_trigger_backup_with_metadata` interceptor.
        """
        return response

    def post_trigger_backup_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for trigger_backup

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_trigger_backup_with_metadata`
        interceptor in new development instead of the `post_trigger_backup` interceptor.
        When both interceptors are used, this `post_trigger_backup_with_metadata` interceptor runs after the
        `post_trigger_backup` interceptor. The (possibly modified) response returned by
        `post_trigger_backup` will be passed to
        `post_trigger_backup_with_metadata`.
        """
        return response, metadata

    def pre_update_backup(
        self,
        request: backupvault.UpdateBackupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupvault.UpdateBackupRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_backup

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_update_backup(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_backup

        DEPRECATED. Please use the `post_update_backup_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
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
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_update_backup_with_metadata`
        interceptor in new development instead of the `post_update_backup` interceptor.
        When both interceptors are used, this `post_update_backup_with_metadata` interceptor runs after the
        `post_update_backup` interceptor. The (possibly modified) response returned by
        `post_update_backup` will be passed to
        `post_update_backup_with_metadata`.
        """
        return response, metadata

    def pre_update_backup_plan(
        self,
        request: backupplan.UpdateBackupPlanRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupplan.UpdateBackupPlanRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_backup_plan

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_update_backup_plan(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_backup_plan

        DEPRECATED. Please use the `post_update_backup_plan_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code. This `post_update_backup_plan` interceptor runs
        before the `post_update_backup_plan_with_metadata` interceptor.
        """
        return response

    def post_update_backup_plan_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_backup_plan

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_update_backup_plan_with_metadata`
        interceptor in new development instead of the `post_update_backup_plan` interceptor.
        When both interceptors are used, this `post_update_backup_plan_with_metadata` interceptor runs after the
        `post_update_backup_plan` interceptor. The (possibly modified) response returned by
        `post_update_backup_plan` will be passed to
        `post_update_backup_plan_with_metadata`.
        """
        return response, metadata

    def pre_update_backup_plan_association(
        self,
        request: backupplanassociation.UpdateBackupPlanAssociationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupplanassociation.UpdateBackupPlanAssociationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_backup_plan_association

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_update_backup_plan_association(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_backup_plan_association

        DEPRECATED. Please use the `post_update_backup_plan_association_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code. This `post_update_backup_plan_association` interceptor runs
        before the `post_update_backup_plan_association_with_metadata` interceptor.
        """
        return response

    def post_update_backup_plan_association_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_backup_plan_association

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_update_backup_plan_association_with_metadata`
        interceptor in new development instead of the `post_update_backup_plan_association` interceptor.
        When both interceptors are used, this `post_update_backup_plan_association_with_metadata` interceptor runs after the
        `post_update_backup_plan_association` interceptor. The (possibly modified) response returned by
        `post_update_backup_plan_association` will be passed to
        `post_update_backup_plan_association_with_metadata`.
        """
        return response, metadata

    def pre_update_backup_vault(
        self,
        request: backupvault.UpdateBackupVaultRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupvault.UpdateBackupVaultRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_backup_vault

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_update_backup_vault(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_backup_vault

        DEPRECATED. Please use the `post_update_backup_vault_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
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
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_update_backup_vault_with_metadata`
        interceptor in new development instead of the `post_update_backup_vault` interceptor.
        When both interceptors are used, this `post_update_backup_vault_with_metadata` interceptor runs after the
        `post_update_backup_vault` interceptor. The (possibly modified) response returned by
        `post_update_backup_vault` will be passed to
        `post_update_backup_vault_with_metadata`.
        """
        return response, metadata

    def pre_update_data_source(
        self,
        request: backupvault.UpdateDataSourceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backupvault.UpdateDataSourceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_data_source

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_update_data_source(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_data_source

        DEPRECATED. Please use the `post_update_data_source_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code. This `post_update_data_source` interceptor runs
        before the `post_update_data_source_with_metadata` interceptor.
        """
        return response

    def post_update_data_source_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_data_source

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupDR server but before it is returned to user code.

        We recommend only using this `post_update_data_source_with_metadata`
        interceptor in new development instead of the `post_update_data_source` interceptor.
        When both interceptors are used, this `post_update_data_source_with_metadata` interceptor runs after the
        `post_update_data_source` interceptor. The (possibly modified) response returned by
        `post_update_data_source` will be passed to
        `post_update_data_source_with_metadata`.
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
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the BackupDR server but before
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
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code.
        """
        return response

    def pre_get_iam_policy(
        self,
        request: iam_policy_pb2.GetIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.GetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code.
        """
        return response

    def pre_set_iam_policy(
        self,
        request: iam_policy_pb2.SetIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.SetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code.
        """
        return response

    def pre_test_iam_permissions(
        self,
        request: iam_policy_pb2.TestIamPermissionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.TestIamPermissionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the BackupDR server but before
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
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the BackupDR server but before
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
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the BackupDR server but before
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
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the BackupDR server but before
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
        before they are sent to the BackupDR server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the BackupDR server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class BackupDRRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: BackupDRRestInterceptor


class BackupDRRestTransport(_BaseBackupDRRestTransport):
    """REST backend synchronous transport for BackupDR.

    The BackupDR Service

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "backupdr.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[BackupDRRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'backupdr.googleapis.com').
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
            interceptor (Optional[BackupDRRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or BackupDRRestInterceptor()
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

    class _CreateBackupPlan(
        _BaseBackupDRRestTransport._BaseCreateBackupPlan, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.CreateBackupPlan")

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
            request: backupplan.CreateBackupPlanRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create backup plan method over HTTP.

            Args:
                request (~.backupplan.CreateBackupPlanRequest):
                    The request object. The request message for creating a ``BackupPlan``.
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
                _BaseBackupDRRestTransport._BaseCreateBackupPlan._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_backup_plan(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseCreateBackupPlan,
                    "_BaseCreateBackupPlan__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.CreateBackupPlan",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "CreateBackupPlan",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._CreateBackupPlan._get_response(
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

            resp = self._interceptor.post_create_backup_plan(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_backup_plan_with_metadata(
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
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.create_backup_plan",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "CreateBackupPlan",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateBackupPlanAssociation(
        _BaseBackupDRRestTransport._BaseCreateBackupPlanAssociation, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.CreateBackupPlanAssociation")

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
            request: backupplanassociation.CreateBackupPlanAssociationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create backup plan
            association method over HTTP.

                Args:
                    request (~.backupplanassociation.CreateBackupPlanAssociationRequest):
                        The request object. Request message for creating a backup
                    plan.
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

            http_options = _BaseBackupDRRestTransport._BaseCreateBackupPlanAssociation._get_http_options()
            request, metadata = self._interceptor.pre_create_backup_plan_association(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseCreateBackupPlanAssociation,
                    "_BaseCreateBackupPlanAssociation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.CreateBackupPlanAssociation",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "CreateBackupPlanAssociation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._CreateBackupPlanAssociation._get_response(
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

            resp = self._interceptor.post_create_backup_plan_association(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_backup_plan_association_with_metadata(
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
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.create_backup_plan_association",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "CreateBackupPlanAssociation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateBackupVault(
        _BaseBackupDRRestTransport._BaseCreateBackupVault, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.CreateBackupVault")

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
            request: backupvault.CreateBackupVaultRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create backup vault method over HTTP.

            Args:
                request (~.backupvault.CreateBackupVaultRequest):
                    The request object. Message for creating a BackupVault.
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
                _BaseBackupDRRestTransport._BaseCreateBackupVault._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_backup_vault(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseCreateBackupVault,
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.CreateBackupVault",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "CreateBackupVault",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._CreateBackupVault._get_response(
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
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.create_backup_vault",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "CreateBackupVault",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateManagementServer(
        _BaseBackupDRRestTransport._BaseCreateManagementServer, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.CreateManagementServer")

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
            request: backupdr.CreateManagementServerRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create management server method over HTTP.

            Args:
                request (~.backupdr.CreateManagementServerRequest):
                    The request object. Request message for creating a
                management server instance.
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

            http_options = _BaseBackupDRRestTransport._BaseCreateManagementServer._get_http_options()
            request, metadata = self._interceptor.pre_create_management_server(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseCreateManagementServer,
                    "_BaseCreateManagementServer__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.CreateManagementServer",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "CreateManagementServer",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._CreateManagementServer._get_response(
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

            resp = self._interceptor.post_create_management_server(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_management_server_with_metadata(
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
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.create_management_server",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "CreateManagementServer",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteBackup(_BaseBackupDRRestTransport._BaseDeleteBackup, BackupDRRestStub):
        def __hash__(self):
            return hash("BackupDRRestTransport.DeleteBackup")

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
            request: backupvault.DeleteBackupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete backup method over HTTP.

            Args:
                request (~.backupvault.DeleteBackupRequest):
                    The request object. Message for deleting a Backup.
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
                _BaseBackupDRRestTransport._BaseDeleteBackup._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_backup(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseDeleteBackup,
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.DeleteBackup",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "DeleteBackup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._DeleteBackup._get_response(
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
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.delete_backup",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "DeleteBackup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteBackupPlan(
        _BaseBackupDRRestTransport._BaseDeleteBackupPlan, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.DeleteBackupPlan")

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
            request: backupplan.DeleteBackupPlanRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete backup plan method over HTTP.

            Args:
                request (~.backupplan.DeleteBackupPlanRequest):
                    The request object. The request message for deleting a ``BackupPlan``.
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
                _BaseBackupDRRestTransport._BaseDeleteBackupPlan._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_backup_plan(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseDeleteBackupPlan,
                    "_BaseDeleteBackupPlan__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.DeleteBackupPlan",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "DeleteBackupPlan",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._DeleteBackupPlan._get_response(
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

            resp = self._interceptor.post_delete_backup_plan(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_backup_plan_with_metadata(
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
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.delete_backup_plan",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "DeleteBackupPlan",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteBackupPlanAssociation(
        _BaseBackupDRRestTransport._BaseDeleteBackupPlanAssociation, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.DeleteBackupPlanAssociation")

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
            request: backupplanassociation.DeleteBackupPlanAssociationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete backup plan
            association method over HTTP.

                Args:
                    request (~.backupplanassociation.DeleteBackupPlanAssociationRequest):
                        The request object. Request message for deleting a backup
                    plan association.
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

            http_options = _BaseBackupDRRestTransport._BaseDeleteBackupPlanAssociation._get_http_options()
            request, metadata = self._interceptor.pre_delete_backup_plan_association(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseDeleteBackupPlanAssociation,
                    "_BaseDeleteBackupPlanAssociation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.DeleteBackupPlanAssociation",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "DeleteBackupPlanAssociation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._DeleteBackupPlanAssociation._get_response(
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

            resp = self._interceptor.post_delete_backup_plan_association(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_delete_backup_plan_association_with_metadata(
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
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.delete_backup_plan_association",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "DeleteBackupPlanAssociation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteBackupVault(
        _BaseBackupDRRestTransport._BaseDeleteBackupVault, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.DeleteBackupVault")

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
            request: backupvault.DeleteBackupVaultRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete backup vault method over HTTP.

            Args:
                request (~.backupvault.DeleteBackupVaultRequest):
                    The request object. Message for deleting a BackupVault.
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
                _BaseBackupDRRestTransport._BaseDeleteBackupVault._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_backup_vault(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseDeleteBackupVault,
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.DeleteBackupVault",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "DeleteBackupVault",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._DeleteBackupVault._get_response(
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
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.delete_backup_vault",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "DeleteBackupVault",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteManagementServer(
        _BaseBackupDRRestTransport._BaseDeleteManagementServer, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.DeleteManagementServer")

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
            request: backupdr.DeleteManagementServerRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete management server method over HTTP.

            Args:
                request (~.backupdr.DeleteManagementServerRequest):
                    The request object. Request message for deleting a
                management server instance.
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

            http_options = _BaseBackupDRRestTransport._BaseDeleteManagementServer._get_http_options()
            request, metadata = self._interceptor.pre_delete_management_server(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseDeleteManagementServer,
                    "_BaseDeleteManagementServer__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.DeleteManagementServer",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "DeleteManagementServer",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._DeleteManagementServer._get_response(
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

            resp = self._interceptor.post_delete_management_server(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_management_server_with_metadata(
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
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.delete_management_server",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "DeleteManagementServer",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchBackupPlanAssociationsForResourceType(
        _BaseBackupDRRestTransport._BaseFetchBackupPlanAssociationsForResourceType,
        BackupDRRestStub,
    ):
        def __hash__(self):
            return hash(
                "BackupDRRestTransport.FetchBackupPlanAssociationsForResourceType"
            )

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
            request: backupplanassociation.FetchBackupPlanAssociationsForResourceTypeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> backupplanassociation.FetchBackupPlanAssociationsForResourceTypeResponse:
            r"""Call the fetch backup plan
            associations for resource type method over HTTP.

                Args:
                    request (~.backupplanassociation.FetchBackupPlanAssociationsForResourceTypeRequest):
                        The request object. Request for the
                    FetchBackupPlanAssociationsForResourceType
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.backupplanassociation.FetchBackupPlanAssociationsForResourceTypeResponse:
                        Response for the
                    FetchBackupPlanAssociationsForResourceType
                    method.

            """

            http_options = _BaseBackupDRRestTransport._BaseFetchBackupPlanAssociationsForResourceType._get_http_options()
            request, metadata = (
                self._interceptor.pre_fetch_backup_plan_associations_for_resource_type(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseFetchBackupPlanAssociationsForResourceType,
                    "_BaseFetchBackupPlanAssociationsForResourceType__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.FetchBackupPlanAssociationsForResourceType",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "FetchBackupPlanAssociationsForResourceType",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._FetchBackupPlanAssociationsForResourceType._get_response(
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
            resp = backupplanassociation.FetchBackupPlanAssociationsForResourceTypeResponse()
            pb_resp = backupplanassociation.FetchBackupPlanAssociationsForResourceTypeResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = (
                self._interceptor.post_fetch_backup_plan_associations_for_resource_type(
                    resp
                )
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_fetch_backup_plan_associations_for_resource_type_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = backupplanassociation.FetchBackupPlanAssociationsForResourceTypeResponse.to_json(
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
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.fetch_backup_plan_associations_for_resource_type",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "FetchBackupPlanAssociationsForResourceType",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchBackupsForResourceType(
        _BaseBackupDRRestTransport._BaseFetchBackupsForResourceType, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.FetchBackupsForResourceType")

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
            request: backupvault.FetchBackupsForResourceTypeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> backupvault.FetchBackupsForResourceTypeResponse:
            r"""Call the fetch backups for
            resource type method over HTTP.

                Args:
                    request (~.backupvault.FetchBackupsForResourceTypeRequest):
                        The request object. Request for the
                    FetchBackupsForResourceType method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.backupvault.FetchBackupsForResourceTypeResponse:
                        Response for the
                    FetchBackupsForResourceType method.

            """

            http_options = _BaseBackupDRRestTransport._BaseFetchBackupsForResourceType._get_http_options()
            request, metadata = self._interceptor.pre_fetch_backups_for_resource_type(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseFetchBackupsForResourceType,
                    "_BaseFetchBackupsForResourceType__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.FetchBackupsForResourceType",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "FetchBackupsForResourceType",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._FetchBackupsForResourceType._get_response(
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
            resp = backupvault.FetchBackupsForResourceTypeResponse()
            pb_resp = backupvault.FetchBackupsForResourceTypeResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_backups_for_resource_type(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_fetch_backups_for_resource_type_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        backupvault.FetchBackupsForResourceTypeResponse.to_json(
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
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.fetch_backups_for_resource_type",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "FetchBackupsForResourceType",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchDataSourceReferencesForResourceType(
        _BaseBackupDRRestTransport._BaseFetchDataSourceReferencesForResourceType,
        BackupDRRestStub,
    ):
        def __hash__(self):
            return hash(
                "BackupDRRestTransport.FetchDataSourceReferencesForResourceType"
            )

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
            request: datasourcereference.FetchDataSourceReferencesForResourceTypeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> datasourcereference.FetchDataSourceReferencesForResourceTypeResponse:
            r"""Call the fetch data source
            references for resource type method over HTTP.

                Args:
                    request (~.datasourcereference.FetchDataSourceReferencesForResourceTypeRequest):
                        The request object. Request for the
                    FetchDataSourceReferencesForResourceType
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.datasourcereference.FetchDataSourceReferencesForResourceTypeResponse:
                        Response for the
                    FetchDataSourceReferencesForResourceType
                    method.

            """

            http_options = _BaseBackupDRRestTransport._BaseFetchDataSourceReferencesForResourceType._get_http_options()
            request, metadata = (
                self._interceptor.pre_fetch_data_source_references_for_resource_type(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseFetchDataSourceReferencesForResourceType,
                    "_BaseFetchDataSourceReferencesForResourceType__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.FetchDataSourceReferencesForResourceType",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "FetchDataSourceReferencesForResourceType",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._FetchDataSourceReferencesForResourceType._get_response(
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
            resp = (
                datasourcereference.FetchDataSourceReferencesForResourceTypeResponse()
            )
            pb_resp = (
                datasourcereference.FetchDataSourceReferencesForResourceTypeResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = (
                self._interceptor.post_fetch_data_source_references_for_resource_type(
                    resp
                )
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_fetch_data_source_references_for_resource_type_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = datasourcereference.FetchDataSourceReferencesForResourceTypeResponse.to_json(
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
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.fetch_data_source_references_for_resource_type",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "FetchDataSourceReferencesForResourceType",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchUsableBackupVaults(
        _BaseBackupDRRestTransport._BaseFetchUsableBackupVaults, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.FetchUsableBackupVaults")

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
            request: backupvault.FetchUsableBackupVaultsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> backupvault.FetchUsableBackupVaultsResponse:
            r"""Call the fetch usable backup
            vaults method over HTTP.

                Args:
                    request (~.backupvault.FetchUsableBackupVaultsRequest):
                        The request object. Request message for fetching usable
                    BackupVaults.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.backupvault.FetchUsableBackupVaultsResponse:
                        Response message for fetching usable
                    BackupVaults.

            """

            http_options = _BaseBackupDRRestTransport._BaseFetchUsableBackupVaults._get_http_options()
            request, metadata = self._interceptor.pre_fetch_usable_backup_vaults(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseFetchUsableBackupVaults,
                    "_BaseFetchUsableBackupVaults__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.FetchUsableBackupVaults",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "FetchUsableBackupVaults",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._FetchUsableBackupVaults._get_response(
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
            resp = backupvault.FetchUsableBackupVaultsResponse()
            pb_resp = backupvault.FetchUsableBackupVaultsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_usable_backup_vaults(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fetch_usable_backup_vaults_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        backupvault.FetchUsableBackupVaultsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.fetch_usable_backup_vaults",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "FetchUsableBackupVaults",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetBackup(_BaseBackupDRRestTransport._BaseGetBackup, BackupDRRestStub):
        def __hash__(self):
            return hash("BackupDRRestTransport.GetBackup")

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
            request: backupvault.GetBackupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> backupvault.Backup:
            r"""Call the get backup method over HTTP.

            Args:
                request (~.backupvault.GetBackupRequest):
                    The request object. Request message for getting a Backup.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.backupvault.Backup:
                    Message describing a Backup object.
            """

            http_options = _BaseBackupDRRestTransport._BaseGetBackup._get_http_options()
            request, metadata = self._interceptor.pre_get_backup(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseGetBackup,
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.GetBackup",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "GetBackup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._GetBackup._get_response(
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
            resp = backupvault.Backup()
            pb_resp = backupvault.Backup.pb(resp)

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
                    response_payload = backupvault.Backup.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.get_backup",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "GetBackup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetBackupPlan(
        _BaseBackupDRRestTransport._BaseGetBackupPlan, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.GetBackupPlan")

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
            request: backupplan.GetBackupPlanRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> backupplan.BackupPlan:
            r"""Call the get backup plan method over HTTP.

            Args:
                request (~.backupplan.GetBackupPlanRequest):
                    The request object. The request message for getting a ``BackupPlan``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.backupplan.BackupPlan:
                    A ``BackupPlan`` specifies some common fields, such as
                ``description`` as well as one or more ``BackupRule``
                messages. Each ``BackupRule`` has a retention policy and
                defines a schedule by which the system is to perform
                backup workloads.

            """

            http_options = (
                _BaseBackupDRRestTransport._BaseGetBackupPlan._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_backup_plan(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseGetBackupPlan,
                    "_BaseGetBackupPlan__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.GetBackupPlan",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "GetBackupPlan",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._GetBackupPlan._get_response(
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
            resp = backupplan.BackupPlan()
            pb_resp = backupplan.BackupPlan.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_backup_plan(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_backup_plan_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = backupplan.BackupPlan.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.get_backup_plan",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "GetBackupPlan",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetBackupPlanAssociation(
        _BaseBackupDRRestTransport._BaseGetBackupPlanAssociation, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.GetBackupPlanAssociation")

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
            request: backupplanassociation.GetBackupPlanAssociationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> backupplanassociation.BackupPlanAssociation:
            r"""Call the get backup plan
            association method over HTTP.

                Args:
                    request (~.backupplanassociation.GetBackupPlanAssociationRequest):
                        The request object. Request message for getting a
                    BackupPlanAssociation resource.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.backupplanassociation.BackupPlanAssociation:
                        A BackupPlanAssociation represents a
                    single BackupPlanAssociation which
                    contains details like workload, backup
                    plan etc

            """

            http_options = _BaseBackupDRRestTransport._BaseGetBackupPlanAssociation._get_http_options()
            request, metadata = self._interceptor.pre_get_backup_plan_association(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseGetBackupPlanAssociation,
                    "_BaseGetBackupPlanAssociation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.GetBackupPlanAssociation",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "GetBackupPlanAssociation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._GetBackupPlanAssociation._get_response(
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
            resp = backupplanassociation.BackupPlanAssociation()
            pb_resp = backupplanassociation.BackupPlanAssociation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_backup_plan_association(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_backup_plan_association_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        backupplanassociation.BackupPlanAssociation.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.get_backup_plan_association",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "GetBackupPlanAssociation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetBackupPlanRevision(
        _BaseBackupDRRestTransport._BaseGetBackupPlanRevision, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.GetBackupPlanRevision")

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
            request: backupplan.GetBackupPlanRevisionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> backupplan.BackupPlanRevision:
            r"""Call the get backup plan revision method over HTTP.

            Args:
                request (~.backupplan.GetBackupPlanRevisionRequest):
                    The request object. The request message for getting a
                ``BackupPlanRevision``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.backupplan.BackupPlanRevision:
                    ``BackupPlanRevision`` represents a snapshot of a
                ``BackupPlan`` at a point in time.

            """

            http_options = _BaseBackupDRRestTransport._BaseGetBackupPlanRevision._get_http_options()
            request, metadata = self._interceptor.pre_get_backup_plan_revision(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseGetBackupPlanRevision,
                    "_BaseGetBackupPlanRevision__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.GetBackupPlanRevision",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "GetBackupPlanRevision",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._GetBackupPlanRevision._get_response(
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
            resp = backupplan.BackupPlanRevision()
            pb_resp = backupplan.BackupPlanRevision.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_backup_plan_revision(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_backup_plan_revision_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = backupplan.BackupPlanRevision.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.get_backup_plan_revision",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "GetBackupPlanRevision",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetBackupVault(
        _BaseBackupDRRestTransport._BaseGetBackupVault, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.GetBackupVault")

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
            request: backupvault.GetBackupVaultRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> backupvault.BackupVault:
            r"""Call the get backup vault method over HTTP.

            Args:
                request (~.backupvault.GetBackupVaultRequest):
                    The request object. Request message for getting a
                BackupVault.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.backupvault.BackupVault:
                    Message describing a BackupVault
                object.

            """

            http_options = (
                _BaseBackupDRRestTransport._BaseGetBackupVault._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_backup_vault(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseGetBackupVault,
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.GetBackupVault",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "GetBackupVault",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._GetBackupVault._get_response(
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
            resp = backupvault.BackupVault()
            pb_resp = backupvault.BackupVault.pb(resp)

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
                    response_payload = backupvault.BackupVault.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.get_backup_vault",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "GetBackupVault",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDataSource(
        _BaseBackupDRRestTransport._BaseGetDataSource, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.GetDataSource")

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
            request: backupvault.GetDataSourceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> backupvault.DataSource:
            r"""Call the get data source method over HTTP.

            Args:
                request (~.backupvault.GetDataSourceRequest):
                    The request object. Request message for getting a
                DataSource instance.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.backupvault.DataSource:
                    Message describing a DataSource
                object. Datasource object used to
                represent Datasource details for both
                admin and basic view.

            """

            http_options = (
                _BaseBackupDRRestTransport._BaseGetDataSource._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_data_source(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseGetDataSource,
                    "_BaseGetDataSource__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.GetDataSource",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "GetDataSource",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._GetDataSource._get_response(
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
            resp = backupvault.DataSource()
            pb_resp = backupvault.DataSource.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_data_source(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_data_source_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = backupvault.DataSource.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.get_data_source",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "GetDataSource",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDataSourceReference(
        _BaseBackupDRRestTransport._BaseGetDataSourceReference, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.GetDataSourceReference")

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
            request: datasourcereference.GetDataSourceReferenceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> datasourcereference.DataSourceReference:
            r"""Call the get data source reference method over HTTP.

            Args:
                request (~.datasourcereference.GetDataSourceReferenceRequest):
                    The request object. Request for the
                GetDataSourceReference method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.datasourcereference.DataSourceReference:
                    DataSourceReference is a reference to
                a DataSource resource.

            """

            http_options = _BaseBackupDRRestTransport._BaseGetDataSourceReference._get_http_options()
            request, metadata = self._interceptor.pre_get_data_source_reference(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseGetDataSourceReference,
                    "_BaseGetDataSourceReference__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.GetDataSourceReference",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "GetDataSourceReference",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._GetDataSourceReference._get_response(
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
            resp = datasourcereference.DataSourceReference()
            pb_resp = datasourcereference.DataSourceReference.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_data_source_reference(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_data_source_reference_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = datasourcereference.DataSourceReference.to_json(
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
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.get_data_source_reference",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "GetDataSourceReference",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetManagementServer(
        _BaseBackupDRRestTransport._BaseGetManagementServer, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.GetManagementServer")

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
            request: backupdr.GetManagementServerRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> backupdr.ManagementServer:
            r"""Call the get management server method over HTTP.

            Args:
                request (~.backupdr.GetManagementServerRequest):
                    The request object. Request message for getting a
                management server instance.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.backupdr.ManagementServer:
                    ManagementServer describes a single
                BackupDR ManagementServer instance.

            """

            http_options = (
                _BaseBackupDRRestTransport._BaseGetManagementServer._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_management_server(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseGetManagementServer,
                    "_BaseGetManagementServer__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.GetManagementServer",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "GetManagementServer",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._GetManagementServer._get_response(
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
            resp = backupdr.ManagementServer()
            pb_resp = backupdr.ManagementServer.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_management_server(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_management_server_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = backupdr.ManagementServer.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.get_management_server",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "GetManagementServer",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _InitializeService(
        _BaseBackupDRRestTransport._BaseInitializeService, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.InitializeService")

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
            request: backupdr.InitializeServiceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the initialize service method over HTTP.

            Args:
                request (~.backupdr.InitializeServiceRequest):
                    The request object. Request message for initializing the
                service.
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
                _BaseBackupDRRestTransport._BaseInitializeService._get_http_options()
            )
            request, metadata = self._interceptor.pre_initialize_service(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseInitializeService,
                    "_BaseInitializeService__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.InitializeService",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "InitializeService",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._InitializeService._get_response(
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

            resp = self._interceptor.post_initialize_service(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_initialize_service_with_metadata(
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
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.initialize_service",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "InitializeService",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListBackupPlanAssociations(
        _BaseBackupDRRestTransport._BaseListBackupPlanAssociations, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.ListBackupPlanAssociations")

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
            request: backupplanassociation.ListBackupPlanAssociationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> backupplanassociation.ListBackupPlanAssociationsResponse:
            r"""Call the list backup plan
            associations method over HTTP.

                Args:
                    request (~.backupplanassociation.ListBackupPlanAssociationsRequest):
                        The request object. Request message for List
                    BackupPlanAssociation
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.backupplanassociation.ListBackupPlanAssociationsResponse:
                        Response message for List
                    BackupPlanAssociation

            """

            http_options = _BaseBackupDRRestTransport._BaseListBackupPlanAssociations._get_http_options()
            request, metadata = self._interceptor.pre_list_backup_plan_associations(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseListBackupPlanAssociations,
                    "_BaseListBackupPlanAssociations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.ListBackupPlanAssociations",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "ListBackupPlanAssociations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._ListBackupPlanAssociations._get_response(
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
            resp = backupplanassociation.ListBackupPlanAssociationsResponse()
            pb_resp = backupplanassociation.ListBackupPlanAssociationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_backup_plan_associations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_backup_plan_associations_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = backupplanassociation.ListBackupPlanAssociationsResponse.to_json(
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
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.list_backup_plan_associations",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "ListBackupPlanAssociations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListBackupPlanRevisions(
        _BaseBackupDRRestTransport._BaseListBackupPlanRevisions, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.ListBackupPlanRevisions")

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
            request: backupplan.ListBackupPlanRevisionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> backupplan.ListBackupPlanRevisionsResponse:
            r"""Call the list backup plan
            revisions method over HTTP.

                Args:
                    request (~.backupplan.ListBackupPlanRevisionsRequest):
                        The request object. The request message for getting a list of
                    ``BackupPlanRevision``.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.backupplan.ListBackupPlanRevisionsResponse:
                        The response message for getting a list of
                    ``BackupPlanRevision``.

            """

            http_options = _BaseBackupDRRestTransport._BaseListBackupPlanRevisions._get_http_options()
            request, metadata = self._interceptor.pre_list_backup_plan_revisions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseListBackupPlanRevisions,
                    "_BaseListBackupPlanRevisions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.ListBackupPlanRevisions",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "ListBackupPlanRevisions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._ListBackupPlanRevisions._get_response(
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
            resp = backupplan.ListBackupPlanRevisionsResponse()
            pb_resp = backupplan.ListBackupPlanRevisionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_backup_plan_revisions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_backup_plan_revisions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        backupplan.ListBackupPlanRevisionsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.list_backup_plan_revisions",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "ListBackupPlanRevisions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListBackupPlans(
        _BaseBackupDRRestTransport._BaseListBackupPlans, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.ListBackupPlans")

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
            request: backupplan.ListBackupPlansRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> backupplan.ListBackupPlansResponse:
            r"""Call the list backup plans method over HTTP.

            Args:
                request (~.backupplan.ListBackupPlansRequest):
                    The request object. The request message for getting a list ``BackupPlan``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.backupplan.ListBackupPlansResponse:
                    The response message for getting a list of
                ``BackupPlan``.

            """

            http_options = (
                _BaseBackupDRRestTransport._BaseListBackupPlans._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_backup_plans(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseListBackupPlans,
                    "_BaseListBackupPlans__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.ListBackupPlans",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "ListBackupPlans",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._ListBackupPlans._get_response(
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
            resp = backupplan.ListBackupPlansResponse()
            pb_resp = backupplan.ListBackupPlansResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_backup_plans(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_backup_plans_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = backupplan.ListBackupPlansResponse.to_json(
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
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.list_backup_plans",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "ListBackupPlans",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListBackups(_BaseBackupDRRestTransport._BaseListBackups, BackupDRRestStub):
        def __hash__(self):
            return hash("BackupDRRestTransport.ListBackups")

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
            request: backupvault.ListBackupsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> backupvault.ListBackupsResponse:
            r"""Call the list backups method over HTTP.

            Args:
                request (~.backupvault.ListBackupsRequest):
                    The request object. Request message for listing Backups.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.backupvault.ListBackupsResponse:
                    Response message for listing Backups.
            """

            http_options = (
                _BaseBackupDRRestTransport._BaseListBackups._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_backups(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseListBackups,
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.ListBackups",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "ListBackups",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._ListBackups._get_response(
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
            resp = backupvault.ListBackupsResponse()
            pb_resp = backupvault.ListBackupsResponse.pb(resp)

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
                    response_payload = backupvault.ListBackupsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.list_backups",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "ListBackups",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListBackupVaults(
        _BaseBackupDRRestTransport._BaseListBackupVaults, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.ListBackupVaults")

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
            request: backupvault.ListBackupVaultsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> backupvault.ListBackupVaultsResponse:
            r"""Call the list backup vaults method over HTTP.

            Args:
                request (~.backupvault.ListBackupVaultsRequest):
                    The request object. Request message for listing
                backupvault stores.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.backupvault.ListBackupVaultsResponse:
                    Response message for listing
                BackupVaults.

            """

            http_options = (
                _BaseBackupDRRestTransport._BaseListBackupVaults._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_backup_vaults(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseListBackupVaults,
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.ListBackupVaults",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "ListBackupVaults",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._ListBackupVaults._get_response(
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
            resp = backupvault.ListBackupVaultsResponse()
            pb_resp = backupvault.ListBackupVaultsResponse.pb(resp)

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
                    response_payload = backupvault.ListBackupVaultsResponse.to_json(
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
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.list_backup_vaults",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "ListBackupVaults",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDataSourceReferences(
        _BaseBackupDRRestTransport._BaseListDataSourceReferences, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.ListDataSourceReferences")

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
            request: datasourcereference.ListDataSourceReferencesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> datasourcereference.ListDataSourceReferencesResponse:
            r"""Call the list data source
            references method over HTTP.

                Args:
                    request (~.datasourcereference.ListDataSourceReferencesRequest):
                        The request object. Request for the
                    ListDataSourceReferences method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.datasourcereference.ListDataSourceReferencesResponse:
                        Response for the
                    ListDataSourceReferences method.

            """

            http_options = _BaseBackupDRRestTransport._BaseListDataSourceReferences._get_http_options()
            request, metadata = self._interceptor.pre_list_data_source_references(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseListDataSourceReferences,
                    "_BaseListDataSourceReferences__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.ListDataSourceReferences",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "ListDataSourceReferences",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._ListDataSourceReferences._get_response(
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
            resp = datasourcereference.ListDataSourceReferencesResponse()
            pb_resp = datasourcereference.ListDataSourceReferencesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_data_source_references(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_data_source_references_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        datasourcereference.ListDataSourceReferencesResponse.to_json(
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
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.list_data_source_references",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "ListDataSourceReferences",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDataSources(
        _BaseBackupDRRestTransport._BaseListDataSources, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.ListDataSources")

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
            request: backupvault.ListDataSourcesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> backupvault.ListDataSourcesResponse:
            r"""Call the list data sources method over HTTP.

            Args:
                request (~.backupvault.ListDataSourcesRequest):
                    The request object. Request message for listing
                DataSources.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.backupvault.ListDataSourcesResponse:
                    Response message for listing
                DataSources.

            """

            http_options = (
                _BaseBackupDRRestTransport._BaseListDataSources._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_data_sources(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseListDataSources,
                    "_BaseListDataSources__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.ListDataSources",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "ListDataSources",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._ListDataSources._get_response(
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
            resp = backupvault.ListDataSourcesResponse()
            pb_resp = backupvault.ListDataSourcesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_data_sources(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_data_sources_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = backupvault.ListDataSourcesResponse.to_json(
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
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.list_data_sources",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "ListDataSources",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListManagementServers(
        _BaseBackupDRRestTransport._BaseListManagementServers, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.ListManagementServers")

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
            request: backupdr.ListManagementServersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> backupdr.ListManagementServersResponse:
            r"""Call the list management servers method over HTTP.

            Args:
                request (~.backupdr.ListManagementServersRequest):
                    The request object. Request message for listing
                management servers.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.backupdr.ListManagementServersResponse:
                    Response message for listing
                management servers.

            """

            http_options = _BaseBackupDRRestTransport._BaseListManagementServers._get_http_options()
            request, metadata = self._interceptor.pre_list_management_servers(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseListManagementServers,
                    "_BaseListManagementServers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.ListManagementServers",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "ListManagementServers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._ListManagementServers._get_response(
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
            resp = backupdr.ListManagementServersResponse()
            pb_resp = backupdr.ListManagementServersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_management_servers(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_management_servers_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = backupdr.ListManagementServersResponse.to_json(
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
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.list_management_servers",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "ListManagementServers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RestoreBackup(
        _BaseBackupDRRestTransport._BaseRestoreBackup, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.RestoreBackup")

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
            request: backupvault.RestoreBackupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the restore backup method over HTTP.

            Args:
                request (~.backupvault.RestoreBackupRequest):
                    The request object. Request message for restoring from a
                Backup.
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
                _BaseBackupDRRestTransport._BaseRestoreBackup._get_http_options()
            )
            request, metadata = self._interceptor.pre_restore_backup(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseRestoreBackup,
                    "_BaseRestoreBackup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.RestoreBackup",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "RestoreBackup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._RestoreBackup._get_response(
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

            resp = self._interceptor.post_restore_backup(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_restore_backup_with_metadata(
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
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.restore_backup",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "RestoreBackup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _TriggerBackup(
        _BaseBackupDRRestTransport._BaseTriggerBackup, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.TriggerBackup")

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
            request: backupplanassociation.TriggerBackupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the trigger backup method over HTTP.

            Args:
                request (~.backupplanassociation.TriggerBackupRequest):
                    The request object. Request message for triggering a
                backup.
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
                _BaseBackupDRRestTransport._BaseTriggerBackup._get_http_options()
            )
            request, metadata = self._interceptor.pre_trigger_backup(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseTriggerBackup,
                    "_BaseTriggerBackup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.TriggerBackup",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "TriggerBackup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._TriggerBackup._get_response(
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

            resp = self._interceptor.post_trigger_backup(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_trigger_backup_with_metadata(
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
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.trigger_backup",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "TriggerBackup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateBackup(_BaseBackupDRRestTransport._BaseUpdateBackup, BackupDRRestStub):
        def __hash__(self):
            return hash("BackupDRRestTransport.UpdateBackup")

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
            request: backupvault.UpdateBackupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update backup method over HTTP.

            Args:
                request (~.backupvault.UpdateBackupRequest):
                    The request object. Request message for updating a
                Backup.
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
                _BaseBackupDRRestTransport._BaseUpdateBackup._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_backup(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseUpdateBackup,
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.UpdateBackup",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "UpdateBackup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._UpdateBackup._get_response(
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
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.update_backup",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "UpdateBackup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateBackupPlan(
        _BaseBackupDRRestTransport._BaseUpdateBackupPlan, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.UpdateBackupPlan")

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
            request: backupplan.UpdateBackupPlanRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update backup plan method over HTTP.

            Args:
                request (~.backupplan.UpdateBackupPlanRequest):
                    The request object. Request message for updating a backup
                plan.
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
                _BaseBackupDRRestTransport._BaseUpdateBackupPlan._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_backup_plan(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseUpdateBackupPlan,
                    "_BaseUpdateBackupPlan__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.UpdateBackupPlan",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "UpdateBackupPlan",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._UpdateBackupPlan._get_response(
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

            resp = self._interceptor.post_update_backup_plan(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_backup_plan_with_metadata(
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
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.update_backup_plan",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "UpdateBackupPlan",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateBackupPlanAssociation(
        _BaseBackupDRRestTransport._BaseUpdateBackupPlanAssociation, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.UpdateBackupPlanAssociation")

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
            request: backupplanassociation.UpdateBackupPlanAssociationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update backup plan
            association method over HTTP.

                Args:
                    request (~.backupplanassociation.UpdateBackupPlanAssociationRequest):
                        The request object. Request message for updating a backup
                    plan association.
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

            http_options = _BaseBackupDRRestTransport._BaseUpdateBackupPlanAssociation._get_http_options()
            request, metadata = self._interceptor.pre_update_backup_plan_association(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseUpdateBackupPlanAssociation,
                    "_BaseUpdateBackupPlanAssociation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.UpdateBackupPlanAssociation",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "UpdateBackupPlanAssociation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._UpdateBackupPlanAssociation._get_response(
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

            resp = self._interceptor.post_update_backup_plan_association(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_update_backup_plan_association_with_metadata(
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
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.update_backup_plan_association",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "UpdateBackupPlanAssociation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateBackupVault(
        _BaseBackupDRRestTransport._BaseUpdateBackupVault, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.UpdateBackupVault")

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
            request: backupvault.UpdateBackupVaultRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update backup vault method over HTTP.

            Args:
                request (~.backupvault.UpdateBackupVaultRequest):
                    The request object. Request message for updating a
                BackupVault.
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
                _BaseBackupDRRestTransport._BaseUpdateBackupVault._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_backup_vault(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseUpdateBackupVault,
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.UpdateBackupVault",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "UpdateBackupVault",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._UpdateBackupVault._get_response(
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
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.update_backup_vault",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "UpdateBackupVault",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDataSource(
        _BaseBackupDRRestTransport._BaseUpdateDataSource, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.UpdateDataSource")

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
            request: backupvault.UpdateDataSourceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update data source method over HTTP.

            Args:
                request (~.backupvault.UpdateDataSourceRequest):
                    The request object. Request message for updating a data
                source instance.
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
                _BaseBackupDRRestTransport._BaseUpdateDataSource._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_data_source(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseUpdateDataSource,
                    "_BaseUpdateDataSource__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.UpdateDataSource",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "UpdateDataSource",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._UpdateDataSource._get_response(
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

            resp = self._interceptor.post_update_data_source(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_data_source_with_metadata(
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
                    "Received response for google.cloud.backupdr_v1.BackupDRClient.update_data_source",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "UpdateDataSource",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_backup_plan(
        self,
    ) -> Callable[[backupplan.CreateBackupPlanRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateBackupPlan(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_backup_plan_association(
        self,
    ) -> Callable[
        [backupplanassociation.CreateBackupPlanAssociationRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateBackupPlanAssociation(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_backup_vault(
        self,
    ) -> Callable[[backupvault.CreateBackupVaultRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateBackupVault(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_management_server(
        self,
    ) -> Callable[[backupdr.CreateManagementServerRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateManagementServer(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_backup(
        self,
    ) -> Callable[[backupvault.DeleteBackupRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteBackup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_backup_plan(
        self,
    ) -> Callable[[backupplan.DeleteBackupPlanRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteBackupPlan(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_backup_plan_association(
        self,
    ) -> Callable[
        [backupplanassociation.DeleteBackupPlanAssociationRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteBackupPlanAssociation(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_backup_vault(
        self,
    ) -> Callable[[backupvault.DeleteBackupVaultRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteBackupVault(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_management_server(
        self,
    ) -> Callable[[backupdr.DeleteManagementServerRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteManagementServer(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def fetch_backup_plan_associations_for_resource_type(
        self,
    ) -> Callable[
        [backupplanassociation.FetchBackupPlanAssociationsForResourceTypeRequest],
        backupplanassociation.FetchBackupPlanAssociationsForResourceTypeResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchBackupPlanAssociationsForResourceType(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def fetch_backups_for_resource_type(
        self,
    ) -> Callable[
        [backupvault.FetchBackupsForResourceTypeRequest],
        backupvault.FetchBackupsForResourceTypeResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchBackupsForResourceType(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def fetch_data_source_references_for_resource_type(
        self,
    ) -> Callable[
        [datasourcereference.FetchDataSourceReferencesForResourceTypeRequest],
        datasourcereference.FetchDataSourceReferencesForResourceTypeResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchDataSourceReferencesForResourceType(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def fetch_usable_backup_vaults(
        self,
    ) -> Callable[
        [backupvault.FetchUsableBackupVaultsRequest],
        backupvault.FetchUsableBackupVaultsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchUsableBackupVaults(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_backup(
        self,
    ) -> Callable[[backupvault.GetBackupRequest], backupvault.Backup]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetBackup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_backup_plan(
        self,
    ) -> Callable[[backupplan.GetBackupPlanRequest], backupplan.BackupPlan]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetBackupPlan(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_backup_plan_association(
        self,
    ) -> Callable[
        [backupplanassociation.GetBackupPlanAssociationRequest],
        backupplanassociation.BackupPlanAssociation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetBackupPlanAssociation(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_backup_plan_revision(
        self,
    ) -> Callable[
        [backupplan.GetBackupPlanRevisionRequest], backupplan.BackupPlanRevision
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetBackupPlanRevision(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_backup_vault(
        self,
    ) -> Callable[[backupvault.GetBackupVaultRequest], backupvault.BackupVault]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetBackupVault(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_data_source(
        self,
    ) -> Callable[[backupvault.GetDataSourceRequest], backupvault.DataSource]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDataSource(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_data_source_reference(
        self,
    ) -> Callable[
        [datasourcereference.GetDataSourceReferenceRequest],
        datasourcereference.DataSourceReference,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDataSourceReference(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_management_server(
        self,
    ) -> Callable[[backupdr.GetManagementServerRequest], backupdr.ManagementServer]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetManagementServer(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def initialize_service(
        self,
    ) -> Callable[[backupdr.InitializeServiceRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._InitializeService(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_backup_plan_associations(
        self,
    ) -> Callable[
        [backupplanassociation.ListBackupPlanAssociationsRequest],
        backupplanassociation.ListBackupPlanAssociationsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListBackupPlanAssociations(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_backup_plan_revisions(
        self,
    ) -> Callable[
        [backupplan.ListBackupPlanRevisionsRequest],
        backupplan.ListBackupPlanRevisionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListBackupPlanRevisions(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_backup_plans(
        self,
    ) -> Callable[
        [backupplan.ListBackupPlansRequest], backupplan.ListBackupPlansResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListBackupPlans(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_backups(
        self,
    ) -> Callable[[backupvault.ListBackupsRequest], backupvault.ListBackupsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListBackups(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_backup_vaults(
        self,
    ) -> Callable[
        [backupvault.ListBackupVaultsRequest], backupvault.ListBackupVaultsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListBackupVaults(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_data_source_references(
        self,
    ) -> Callable[
        [datasourcereference.ListDataSourceReferencesRequest],
        datasourcereference.ListDataSourceReferencesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDataSourceReferences(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_data_sources(
        self,
    ) -> Callable[
        [backupvault.ListDataSourcesRequest], backupvault.ListDataSourcesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDataSources(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_management_servers(
        self,
    ) -> Callable[
        [backupdr.ListManagementServersRequest], backupdr.ListManagementServersResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListManagementServers(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def restore_backup(
        self,
    ) -> Callable[[backupvault.RestoreBackupRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RestoreBackup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def trigger_backup(
        self,
    ) -> Callable[
        [backupplanassociation.TriggerBackupRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._TriggerBackup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_backup(
        self,
    ) -> Callable[[backupvault.UpdateBackupRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateBackup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_backup_plan(
        self,
    ) -> Callable[[backupplan.UpdateBackupPlanRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateBackupPlan(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_backup_plan_association(
        self,
    ) -> Callable[
        [backupplanassociation.UpdateBackupPlanAssociationRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateBackupPlanAssociation(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_backup_vault(
        self,
    ) -> Callable[[backupvault.UpdateBackupVaultRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateBackupVault(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_data_source(
        self,
    ) -> Callable[[backupvault.UpdateDataSourceRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDataSource(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(_BaseBackupDRRestTransport._BaseGetLocation, BackupDRRestStub):
        def __hash__(self):
            return hash("BackupDRRestTransport.GetLocation")

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
                _BaseBackupDRRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.backupdr_v1.BackupDRAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
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
        _BaseBackupDRRestTransport._BaseListLocations, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.ListLocations")

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
                _BaseBackupDRRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.backupdr_v1.BackupDRAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "ListLocations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def get_iam_policy(self):
        return self._GetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _GetIamPolicy(_BaseBackupDRRestTransport._BaseGetIamPolicy, BackupDRRestStub):
        def __hash__(self):
            return hash("BackupDRRestTransport.GetIamPolicy")

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
            request: iam_policy_pb2.GetIamPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> policy_pb2.Policy:
            r"""Call the get iam policy method over HTTP.

            Args:
                request (iam_policy_pb2.GetIamPolicyRequest):
                    The request object for GetIamPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                policy_pb2.Policy: Response from GetIamPolicy method.
            """

            http_options = (
                _BaseBackupDRRestTransport._BaseGetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseGetIamPolicy,
                    "_BaseGetIamPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._GetIamPolicy._get_response(
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
            resp = policy_pb2.Policy()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_iam_policy(resp)
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
                    "Received response for google.cloud.backupdr_v1.BackupDRAsyncClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "GetIamPolicy",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def set_iam_policy(self):
        return self._SetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _SetIamPolicy(_BaseBackupDRRestTransport._BaseSetIamPolicy, BackupDRRestStub):
        def __hash__(self):
            return hash("BackupDRRestTransport.SetIamPolicy")

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
            request: iam_policy_pb2.SetIamPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> policy_pb2.Policy:
            r"""Call the set iam policy method over HTTP.

            Args:
                request (iam_policy_pb2.SetIamPolicyRequest):
                    The request object for SetIamPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                policy_pb2.Policy: Response from SetIamPolicy method.
            """

            http_options = (
                _BaseBackupDRRestTransport._BaseSetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseSetIamPolicy,
                    "_BaseSetIamPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._SetIamPolicy._get_response(
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

            content = response.content.decode("utf-8")
            resp = policy_pb2.Policy()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_set_iam_policy(resp)
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
                    "Received response for google.cloud.backupdr_v1.BackupDRAsyncClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "SetIamPolicy",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def test_iam_permissions(self):
        return self._TestIamPermissions(self._session, self._host, self._interceptor)  # type: ignore

    class _TestIamPermissions(
        _BaseBackupDRRestTransport._BaseTestIamPermissions, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.TestIamPermissions")

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
            request: iam_policy_pb2.TestIamPermissionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> iam_policy_pb2.TestIamPermissionsResponse:
            r"""Call the test iam permissions method over HTTP.

            Args:
                request (iam_policy_pb2.TestIamPermissionsRequest):
                    The request object for TestIamPermissions method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                iam_policy_pb2.TestIamPermissionsResponse: Response from TestIamPermissions method.
            """

            http_options = (
                _BaseBackupDRRestTransport._BaseTestIamPermissions._get_http_options()
            )
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseTestIamPermissions,
                    "_BaseTestIamPermissions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._TestIamPermissions._get_response(
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

            content = response.content.decode("utf-8")
            resp = iam_policy_pb2.TestIamPermissionsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_test_iam_permissions(resp)
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
                    "Received response for google.cloud.backupdr_v1.BackupDRAsyncClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "TestIamPermissions",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseBackupDRRestTransport._BaseCancelOperation, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.CancelOperation")

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
                _BaseBackupDRRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._CancelOperation._get_response(
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
        _BaseBackupDRRestTransport._BaseDeleteOperation, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.DeleteOperation")

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
                _BaseBackupDRRestTransport._BaseDeleteOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._DeleteOperation._get_response(
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

    class _GetOperation(_BaseBackupDRRestTransport._BaseGetOperation, BackupDRRestStub):
        def __hash__(self):
            return hash("BackupDRRestTransport.GetOperation")

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
                _BaseBackupDRRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.backupdr_v1.BackupDRAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
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
        _BaseBackupDRRestTransport._BaseListOperations, BackupDRRestStub
    ):
        def __hash__(self):
            return hash("BackupDRRestTransport.ListOperations")

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
                _BaseBackupDRRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupDRRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.backupdr_v1.BackupDRClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupDRRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.backupdr_v1.BackupDRAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.backupdr.v1.BackupDR",
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


__all__ = ("BackupDRRestTransport",)
