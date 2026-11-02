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

from google.cloud.vmmigration_v1._compat import transcode_request
from google.cloud.vmmigration_v1.types import vmmigration

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseVmMigrationRestTransport

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


class VmMigrationRestInterceptor:
    """Interceptor for VmMigration.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the VmMigrationRestTransport.

    .. code-block:: python
        class MyCustomVmMigrationInterceptor(VmMigrationRestInterceptor):
            def pre_add_group_migration(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_add_group_migration(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_cancel_clone_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_cancel_clone_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_cancel_cutover_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_cancel_cutover_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_cancel_disk_migration_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_cancel_disk_migration_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_cancel_image_import_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_cancel_image_import_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_clone_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_clone_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_cutover_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_cutover_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_datacenter_connector(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_datacenter_connector(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_disk_migration_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_disk_migration_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_image_import(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_image_import(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_migrating_vm(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_migrating_vm(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_source(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_source(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_target_project(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_target_project(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_utilization_report(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_utilization_report(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_datacenter_connector(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_datacenter_connector(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_disk_migration_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_disk_migration_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_image_import(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_image_import(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_migrating_vm(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_migrating_vm(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_source(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_source(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_target_project(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_target_project(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_utilization_report(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_utilization_report(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_extend_migration(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_extend_migration(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_inventory(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_inventory(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_storage_inventory(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_storage_inventory(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_finalize_migration(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_finalize_migration(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_clone_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_clone_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_cutover_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_cutover_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_datacenter_connector(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_datacenter_connector(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_disk_migration_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_disk_migration_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_image_import(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_image_import(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_image_import_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_image_import_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_migrating_vm(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_migrating_vm(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_replication_cycle(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_replication_cycle(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_source(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_source(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_target_project(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_target_project(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_utilization_report(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_utilization_report(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_clone_jobs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_clone_jobs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_cutover_jobs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_cutover_jobs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_datacenter_connectors(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_datacenter_connectors(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_disk_migration_jobs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_disk_migration_jobs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_groups(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_groups(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_image_import_jobs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_image_import_jobs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_image_imports(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_image_imports(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_migrating_vms(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_migrating_vms(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_replication_cycles(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_replication_cycles(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_sources(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_sources(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_target_projects(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_target_projects(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_utilization_reports(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_utilization_reports(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_pause_migration(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_pause_migration(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_remove_group_migration(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_remove_group_migration(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_resume_migration(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_resume_migration(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_run_disk_migration_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_run_disk_migration_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_start_migration(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_start_migration(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_disk_migration_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_disk_migration_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_migrating_vm(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_migrating_vm(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_source(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_source(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_target_project(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_target_project(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_upgrade_appliance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_upgrade_appliance(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = VmMigrationRestTransport(interceptor=MyCustomVmMigrationInterceptor())
        client = VmMigrationClient(transport=transport)


    """

    def pre_add_group_migration(
        self,
        request: vmmigration.AddGroupMigrationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.AddGroupMigrationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for add_group_migration

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_add_group_migration(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for add_group_migration

        DEPRECATED. Please use the `post_add_group_migration_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_add_group_migration` interceptor runs
        before the `post_add_group_migration_with_metadata` interceptor.
        """
        return response

    def post_add_group_migration_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for add_group_migration

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_add_group_migration_with_metadata`
        interceptor in new development instead of the `post_add_group_migration` interceptor.
        When both interceptors are used, this `post_add_group_migration_with_metadata` interceptor runs after the
        `post_add_group_migration` interceptor. The (possibly modified) response returned by
        `post_add_group_migration` will be passed to
        `post_add_group_migration_with_metadata`.
        """
        return response, metadata

    def pre_cancel_clone_job(
        self,
        request: vmmigration.CancelCloneJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.CancelCloneJobRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for cancel_clone_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_cancel_clone_job(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for cancel_clone_job

        DEPRECATED. Please use the `post_cancel_clone_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_cancel_clone_job` interceptor runs
        before the `post_cancel_clone_job_with_metadata` interceptor.
        """
        return response

    def post_cancel_clone_job_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for cancel_clone_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_cancel_clone_job_with_metadata`
        interceptor in new development instead of the `post_cancel_clone_job` interceptor.
        When both interceptors are used, this `post_cancel_clone_job_with_metadata` interceptor runs after the
        `post_cancel_clone_job` interceptor. The (possibly modified) response returned by
        `post_cancel_clone_job` will be passed to
        `post_cancel_clone_job_with_metadata`.
        """
        return response, metadata

    def pre_cancel_cutover_job(
        self,
        request: vmmigration.CancelCutoverJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.CancelCutoverJobRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for cancel_cutover_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_cancel_cutover_job(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for cancel_cutover_job

        DEPRECATED. Please use the `post_cancel_cutover_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_cancel_cutover_job` interceptor runs
        before the `post_cancel_cutover_job_with_metadata` interceptor.
        """
        return response

    def post_cancel_cutover_job_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for cancel_cutover_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_cancel_cutover_job_with_metadata`
        interceptor in new development instead of the `post_cancel_cutover_job` interceptor.
        When both interceptors are used, this `post_cancel_cutover_job_with_metadata` interceptor runs after the
        `post_cancel_cutover_job` interceptor. The (possibly modified) response returned by
        `post_cancel_cutover_job` will be passed to
        `post_cancel_cutover_job_with_metadata`.
        """
        return response, metadata

    def pre_cancel_disk_migration_job(
        self,
        request: vmmigration.CancelDiskMigrationJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.CancelDiskMigrationJobRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for cancel_disk_migration_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_cancel_disk_migration_job(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for cancel_disk_migration_job

        DEPRECATED. Please use the `post_cancel_disk_migration_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_cancel_disk_migration_job` interceptor runs
        before the `post_cancel_disk_migration_job_with_metadata` interceptor.
        """
        return response

    def post_cancel_disk_migration_job_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for cancel_disk_migration_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_cancel_disk_migration_job_with_metadata`
        interceptor in new development instead of the `post_cancel_disk_migration_job` interceptor.
        When both interceptors are used, this `post_cancel_disk_migration_job_with_metadata` interceptor runs after the
        `post_cancel_disk_migration_job` interceptor. The (possibly modified) response returned by
        `post_cancel_disk_migration_job` will be passed to
        `post_cancel_disk_migration_job_with_metadata`.
        """
        return response, metadata

    def pre_cancel_image_import_job(
        self,
        request: vmmigration.CancelImageImportJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.CancelImageImportJobRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for cancel_image_import_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_cancel_image_import_job(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for cancel_image_import_job

        DEPRECATED. Please use the `post_cancel_image_import_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_cancel_image_import_job` interceptor runs
        before the `post_cancel_image_import_job_with_metadata` interceptor.
        """
        return response

    def post_cancel_image_import_job_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for cancel_image_import_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_cancel_image_import_job_with_metadata`
        interceptor in new development instead of the `post_cancel_image_import_job` interceptor.
        When both interceptors are used, this `post_cancel_image_import_job_with_metadata` interceptor runs after the
        `post_cancel_image_import_job` interceptor. The (possibly modified) response returned by
        `post_cancel_image_import_job` will be passed to
        `post_cancel_image_import_job_with_metadata`.
        """
        return response, metadata

    def pre_create_clone_job(
        self,
        request: vmmigration.CreateCloneJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.CreateCloneJobRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_clone_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_create_clone_job(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_clone_job

        DEPRECATED. Please use the `post_create_clone_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_create_clone_job` interceptor runs
        before the `post_create_clone_job_with_metadata` interceptor.
        """
        return response

    def post_create_clone_job_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_clone_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_create_clone_job_with_metadata`
        interceptor in new development instead of the `post_create_clone_job` interceptor.
        When both interceptors are used, this `post_create_clone_job_with_metadata` interceptor runs after the
        `post_create_clone_job` interceptor. The (possibly modified) response returned by
        `post_create_clone_job` will be passed to
        `post_create_clone_job_with_metadata`.
        """
        return response, metadata

    def pre_create_cutover_job(
        self,
        request: vmmigration.CreateCutoverJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.CreateCutoverJobRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_cutover_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_create_cutover_job(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_cutover_job

        DEPRECATED. Please use the `post_create_cutover_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_create_cutover_job` interceptor runs
        before the `post_create_cutover_job_with_metadata` interceptor.
        """
        return response

    def post_create_cutover_job_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_cutover_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_create_cutover_job_with_metadata`
        interceptor in new development instead of the `post_create_cutover_job` interceptor.
        When both interceptors are used, this `post_create_cutover_job_with_metadata` interceptor runs after the
        `post_create_cutover_job` interceptor. The (possibly modified) response returned by
        `post_create_cutover_job` will be passed to
        `post_create_cutover_job_with_metadata`.
        """
        return response, metadata

    def pre_create_datacenter_connector(
        self,
        request: vmmigration.CreateDatacenterConnectorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.CreateDatacenterConnectorRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_datacenter_connector

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_create_datacenter_connector(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_datacenter_connector

        DEPRECATED. Please use the `post_create_datacenter_connector_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_create_datacenter_connector` interceptor runs
        before the `post_create_datacenter_connector_with_metadata` interceptor.
        """
        return response

    def post_create_datacenter_connector_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_datacenter_connector

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_create_datacenter_connector_with_metadata`
        interceptor in new development instead of the `post_create_datacenter_connector` interceptor.
        When both interceptors are used, this `post_create_datacenter_connector_with_metadata` interceptor runs after the
        `post_create_datacenter_connector` interceptor. The (possibly modified) response returned by
        `post_create_datacenter_connector` will be passed to
        `post_create_datacenter_connector_with_metadata`.
        """
        return response, metadata

    def pre_create_disk_migration_job(
        self,
        request: vmmigration.CreateDiskMigrationJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.CreateDiskMigrationJobRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_disk_migration_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_create_disk_migration_job(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_disk_migration_job

        DEPRECATED. Please use the `post_create_disk_migration_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_create_disk_migration_job` interceptor runs
        before the `post_create_disk_migration_job_with_metadata` interceptor.
        """
        return response

    def post_create_disk_migration_job_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_disk_migration_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_create_disk_migration_job_with_metadata`
        interceptor in new development instead of the `post_create_disk_migration_job` interceptor.
        When both interceptors are used, this `post_create_disk_migration_job_with_metadata` interceptor runs after the
        `post_create_disk_migration_job` interceptor. The (possibly modified) response returned by
        `post_create_disk_migration_job` will be passed to
        `post_create_disk_migration_job_with_metadata`.
        """
        return response, metadata

    def pre_create_group(
        self,
        request: vmmigration.CreateGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[vmmigration.CreateGroupRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_create_group(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_group

        DEPRECATED. Please use the `post_create_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_create_group` interceptor runs
        before the `post_create_group_with_metadata` interceptor.
        """
        return response

    def post_create_group_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_create_group_with_metadata`
        interceptor in new development instead of the `post_create_group` interceptor.
        When both interceptors are used, this `post_create_group_with_metadata` interceptor runs after the
        `post_create_group` interceptor. The (possibly modified) response returned by
        `post_create_group` will be passed to
        `post_create_group_with_metadata`.
        """
        return response, metadata

    def pre_create_image_import(
        self,
        request: vmmigration.CreateImageImportRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.CreateImageImportRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_image_import

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_create_image_import(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_image_import

        DEPRECATED. Please use the `post_create_image_import_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_create_image_import` interceptor runs
        before the `post_create_image_import_with_metadata` interceptor.
        """
        return response

    def post_create_image_import_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_image_import

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_create_image_import_with_metadata`
        interceptor in new development instead of the `post_create_image_import` interceptor.
        When both interceptors are used, this `post_create_image_import_with_metadata` interceptor runs after the
        `post_create_image_import` interceptor. The (possibly modified) response returned by
        `post_create_image_import` will be passed to
        `post_create_image_import_with_metadata`.
        """
        return response, metadata

    def pre_create_migrating_vm(
        self,
        request: vmmigration.CreateMigratingVmRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.CreateMigratingVmRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_migrating_vm

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_create_migrating_vm(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_migrating_vm

        DEPRECATED. Please use the `post_create_migrating_vm_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_create_migrating_vm` interceptor runs
        before the `post_create_migrating_vm_with_metadata` interceptor.
        """
        return response

    def post_create_migrating_vm_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_migrating_vm

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_create_migrating_vm_with_metadata`
        interceptor in new development instead of the `post_create_migrating_vm` interceptor.
        When both interceptors are used, this `post_create_migrating_vm_with_metadata` interceptor runs after the
        `post_create_migrating_vm` interceptor. The (possibly modified) response returned by
        `post_create_migrating_vm` will be passed to
        `post_create_migrating_vm_with_metadata`.
        """
        return response, metadata

    def pre_create_source(
        self,
        request: vmmigration.CreateSourceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.CreateSourceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_source

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_create_source(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_source

        DEPRECATED. Please use the `post_create_source_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_create_source` interceptor runs
        before the `post_create_source_with_metadata` interceptor.
        """
        return response

    def post_create_source_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_source

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_create_source_with_metadata`
        interceptor in new development instead of the `post_create_source` interceptor.
        When both interceptors are used, this `post_create_source_with_metadata` interceptor runs after the
        `post_create_source` interceptor. The (possibly modified) response returned by
        `post_create_source` will be passed to
        `post_create_source_with_metadata`.
        """
        return response, metadata

    def pre_create_target_project(
        self,
        request: vmmigration.CreateTargetProjectRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.CreateTargetProjectRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_target_project

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_create_target_project(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_target_project

        DEPRECATED. Please use the `post_create_target_project_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_create_target_project` interceptor runs
        before the `post_create_target_project_with_metadata` interceptor.
        """
        return response

    def post_create_target_project_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_target_project

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_create_target_project_with_metadata`
        interceptor in new development instead of the `post_create_target_project` interceptor.
        When both interceptors are used, this `post_create_target_project_with_metadata` interceptor runs after the
        `post_create_target_project` interceptor. The (possibly modified) response returned by
        `post_create_target_project` will be passed to
        `post_create_target_project_with_metadata`.
        """
        return response, metadata

    def pre_create_utilization_report(
        self,
        request: vmmigration.CreateUtilizationReportRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.CreateUtilizationReportRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_utilization_report

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_create_utilization_report(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_utilization_report

        DEPRECATED. Please use the `post_create_utilization_report_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_create_utilization_report` interceptor runs
        before the `post_create_utilization_report_with_metadata` interceptor.
        """
        return response

    def post_create_utilization_report_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_utilization_report

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_create_utilization_report_with_metadata`
        interceptor in new development instead of the `post_create_utilization_report` interceptor.
        When both interceptors are used, this `post_create_utilization_report_with_metadata` interceptor runs after the
        `post_create_utilization_report` interceptor. The (possibly modified) response returned by
        `post_create_utilization_report` will be passed to
        `post_create_utilization_report_with_metadata`.
        """
        return response, metadata

    def pre_delete_datacenter_connector(
        self,
        request: vmmigration.DeleteDatacenterConnectorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.DeleteDatacenterConnectorRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_datacenter_connector

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_delete_datacenter_connector(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_datacenter_connector

        DEPRECATED. Please use the `post_delete_datacenter_connector_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_delete_datacenter_connector` interceptor runs
        before the `post_delete_datacenter_connector_with_metadata` interceptor.
        """
        return response

    def post_delete_datacenter_connector_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_datacenter_connector

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_delete_datacenter_connector_with_metadata`
        interceptor in new development instead of the `post_delete_datacenter_connector` interceptor.
        When both interceptors are used, this `post_delete_datacenter_connector_with_metadata` interceptor runs after the
        `post_delete_datacenter_connector` interceptor. The (possibly modified) response returned by
        `post_delete_datacenter_connector` will be passed to
        `post_delete_datacenter_connector_with_metadata`.
        """
        return response, metadata

    def pre_delete_disk_migration_job(
        self,
        request: vmmigration.DeleteDiskMigrationJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.DeleteDiskMigrationJobRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_disk_migration_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_delete_disk_migration_job(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_disk_migration_job

        DEPRECATED. Please use the `post_delete_disk_migration_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_delete_disk_migration_job` interceptor runs
        before the `post_delete_disk_migration_job_with_metadata` interceptor.
        """
        return response

    def post_delete_disk_migration_job_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_disk_migration_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_delete_disk_migration_job_with_metadata`
        interceptor in new development instead of the `post_delete_disk_migration_job` interceptor.
        When both interceptors are used, this `post_delete_disk_migration_job_with_metadata` interceptor runs after the
        `post_delete_disk_migration_job` interceptor. The (possibly modified) response returned by
        `post_delete_disk_migration_job` will be passed to
        `post_delete_disk_migration_job_with_metadata`.
        """
        return response, metadata

    def pre_delete_group(
        self,
        request: vmmigration.DeleteGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[vmmigration.DeleteGroupRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_delete_group(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_group

        DEPRECATED. Please use the `post_delete_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_delete_group` interceptor runs
        before the `post_delete_group_with_metadata` interceptor.
        """
        return response

    def post_delete_group_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_delete_group_with_metadata`
        interceptor in new development instead of the `post_delete_group` interceptor.
        When both interceptors are used, this `post_delete_group_with_metadata` interceptor runs after the
        `post_delete_group` interceptor. The (possibly modified) response returned by
        `post_delete_group` will be passed to
        `post_delete_group_with_metadata`.
        """
        return response, metadata

    def pre_delete_image_import(
        self,
        request: vmmigration.DeleteImageImportRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.DeleteImageImportRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_image_import

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_delete_image_import(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_image_import

        DEPRECATED. Please use the `post_delete_image_import_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_delete_image_import` interceptor runs
        before the `post_delete_image_import_with_metadata` interceptor.
        """
        return response

    def post_delete_image_import_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_image_import

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_delete_image_import_with_metadata`
        interceptor in new development instead of the `post_delete_image_import` interceptor.
        When both interceptors are used, this `post_delete_image_import_with_metadata` interceptor runs after the
        `post_delete_image_import` interceptor. The (possibly modified) response returned by
        `post_delete_image_import` will be passed to
        `post_delete_image_import_with_metadata`.
        """
        return response, metadata

    def pre_delete_migrating_vm(
        self,
        request: vmmigration.DeleteMigratingVmRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.DeleteMigratingVmRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_migrating_vm

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_delete_migrating_vm(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_migrating_vm

        DEPRECATED. Please use the `post_delete_migrating_vm_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_delete_migrating_vm` interceptor runs
        before the `post_delete_migrating_vm_with_metadata` interceptor.
        """
        return response

    def post_delete_migrating_vm_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_migrating_vm

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_delete_migrating_vm_with_metadata`
        interceptor in new development instead of the `post_delete_migrating_vm` interceptor.
        When both interceptors are used, this `post_delete_migrating_vm_with_metadata` interceptor runs after the
        `post_delete_migrating_vm` interceptor. The (possibly modified) response returned by
        `post_delete_migrating_vm` will be passed to
        `post_delete_migrating_vm_with_metadata`.
        """
        return response, metadata

    def pre_delete_source(
        self,
        request: vmmigration.DeleteSourceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.DeleteSourceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_source

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_delete_source(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_source

        DEPRECATED. Please use the `post_delete_source_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_delete_source` interceptor runs
        before the `post_delete_source_with_metadata` interceptor.
        """
        return response

    def post_delete_source_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_source

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_delete_source_with_metadata`
        interceptor in new development instead of the `post_delete_source` interceptor.
        When both interceptors are used, this `post_delete_source_with_metadata` interceptor runs after the
        `post_delete_source` interceptor. The (possibly modified) response returned by
        `post_delete_source` will be passed to
        `post_delete_source_with_metadata`.
        """
        return response, metadata

    def pre_delete_target_project(
        self,
        request: vmmigration.DeleteTargetProjectRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.DeleteTargetProjectRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_target_project

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_delete_target_project(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_target_project

        DEPRECATED. Please use the `post_delete_target_project_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_delete_target_project` interceptor runs
        before the `post_delete_target_project_with_metadata` interceptor.
        """
        return response

    def post_delete_target_project_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_target_project

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_delete_target_project_with_metadata`
        interceptor in new development instead of the `post_delete_target_project` interceptor.
        When both interceptors are used, this `post_delete_target_project_with_metadata` interceptor runs after the
        `post_delete_target_project` interceptor. The (possibly modified) response returned by
        `post_delete_target_project` will be passed to
        `post_delete_target_project_with_metadata`.
        """
        return response, metadata

    def pre_delete_utilization_report(
        self,
        request: vmmigration.DeleteUtilizationReportRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.DeleteUtilizationReportRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_utilization_report

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_delete_utilization_report(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_utilization_report

        DEPRECATED. Please use the `post_delete_utilization_report_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_delete_utilization_report` interceptor runs
        before the `post_delete_utilization_report_with_metadata` interceptor.
        """
        return response

    def post_delete_utilization_report_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_utilization_report

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_delete_utilization_report_with_metadata`
        interceptor in new development instead of the `post_delete_utilization_report` interceptor.
        When both interceptors are used, this `post_delete_utilization_report_with_metadata` interceptor runs after the
        `post_delete_utilization_report` interceptor. The (possibly modified) response returned by
        `post_delete_utilization_report` will be passed to
        `post_delete_utilization_report_with_metadata`.
        """
        return response, metadata

    def pre_extend_migration(
        self,
        request: vmmigration.ExtendMigrationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.ExtendMigrationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for extend_migration

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_extend_migration(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for extend_migration

        DEPRECATED. Please use the `post_extend_migration_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_extend_migration` interceptor runs
        before the `post_extend_migration_with_metadata` interceptor.
        """
        return response

    def post_extend_migration_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for extend_migration

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_extend_migration_with_metadata`
        interceptor in new development instead of the `post_extend_migration` interceptor.
        When both interceptors are used, this `post_extend_migration_with_metadata` interceptor runs after the
        `post_extend_migration` interceptor. The (possibly modified) response returned by
        `post_extend_migration` will be passed to
        `post_extend_migration_with_metadata`.
        """
        return response, metadata

    def pre_fetch_inventory(
        self,
        request: vmmigration.FetchInventoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.FetchInventoryRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for fetch_inventory

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_fetch_inventory(
        self, response: vmmigration.FetchInventoryResponse
    ) -> vmmigration.FetchInventoryResponse:
        """Post-rpc interceptor for fetch_inventory

        DEPRECATED. Please use the `post_fetch_inventory_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_fetch_inventory` interceptor runs
        before the `post_fetch_inventory_with_metadata` interceptor.
        """
        return response

    def post_fetch_inventory_with_metadata(
        self,
        response: vmmigration.FetchInventoryResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.FetchInventoryResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for fetch_inventory

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_fetch_inventory_with_metadata`
        interceptor in new development instead of the `post_fetch_inventory` interceptor.
        When both interceptors are used, this `post_fetch_inventory_with_metadata` interceptor runs after the
        `post_fetch_inventory` interceptor. The (possibly modified) response returned by
        `post_fetch_inventory` will be passed to
        `post_fetch_inventory_with_metadata`.
        """
        return response, metadata

    def pre_fetch_storage_inventory(
        self,
        request: vmmigration.FetchStorageInventoryRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.FetchStorageInventoryRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for fetch_storage_inventory

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_fetch_storage_inventory(
        self, response: vmmigration.FetchStorageInventoryResponse
    ) -> vmmigration.FetchStorageInventoryResponse:
        """Post-rpc interceptor for fetch_storage_inventory

        DEPRECATED. Please use the `post_fetch_storage_inventory_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_fetch_storage_inventory` interceptor runs
        before the `post_fetch_storage_inventory_with_metadata` interceptor.
        """
        return response

    def post_fetch_storage_inventory_with_metadata(
        self,
        response: vmmigration.FetchStorageInventoryResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.FetchStorageInventoryResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for fetch_storage_inventory

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_fetch_storage_inventory_with_metadata`
        interceptor in new development instead of the `post_fetch_storage_inventory` interceptor.
        When both interceptors are used, this `post_fetch_storage_inventory_with_metadata` interceptor runs after the
        `post_fetch_storage_inventory` interceptor. The (possibly modified) response returned by
        `post_fetch_storage_inventory` will be passed to
        `post_fetch_storage_inventory_with_metadata`.
        """
        return response, metadata

    def pre_finalize_migration(
        self,
        request: vmmigration.FinalizeMigrationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.FinalizeMigrationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for finalize_migration

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_finalize_migration(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for finalize_migration

        DEPRECATED. Please use the `post_finalize_migration_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_finalize_migration` interceptor runs
        before the `post_finalize_migration_with_metadata` interceptor.
        """
        return response

    def post_finalize_migration_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for finalize_migration

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_finalize_migration_with_metadata`
        interceptor in new development instead of the `post_finalize_migration` interceptor.
        When both interceptors are used, this `post_finalize_migration_with_metadata` interceptor runs after the
        `post_finalize_migration` interceptor. The (possibly modified) response returned by
        `post_finalize_migration` will be passed to
        `post_finalize_migration_with_metadata`.
        """
        return response, metadata

    def pre_get_clone_job(
        self,
        request: vmmigration.GetCloneJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[vmmigration.GetCloneJobRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_clone_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_get_clone_job(
        self, response: vmmigration.CloneJob
    ) -> vmmigration.CloneJob:
        """Post-rpc interceptor for get_clone_job

        DEPRECATED. Please use the `post_get_clone_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_get_clone_job` interceptor runs
        before the `post_get_clone_job_with_metadata` interceptor.
        """
        return response

    def post_get_clone_job_with_metadata(
        self,
        response: vmmigration.CloneJob,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[vmmigration.CloneJob, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_clone_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_get_clone_job_with_metadata`
        interceptor in new development instead of the `post_get_clone_job` interceptor.
        When both interceptors are used, this `post_get_clone_job_with_metadata` interceptor runs after the
        `post_get_clone_job` interceptor. The (possibly modified) response returned by
        `post_get_clone_job` will be passed to
        `post_get_clone_job_with_metadata`.
        """
        return response, metadata

    def pre_get_cutover_job(
        self,
        request: vmmigration.GetCutoverJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.GetCutoverJobRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_cutover_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_get_cutover_job(
        self, response: vmmigration.CutoverJob
    ) -> vmmigration.CutoverJob:
        """Post-rpc interceptor for get_cutover_job

        DEPRECATED. Please use the `post_get_cutover_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_get_cutover_job` interceptor runs
        before the `post_get_cutover_job_with_metadata` interceptor.
        """
        return response

    def post_get_cutover_job_with_metadata(
        self,
        response: vmmigration.CutoverJob,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[vmmigration.CutoverJob, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_cutover_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_get_cutover_job_with_metadata`
        interceptor in new development instead of the `post_get_cutover_job` interceptor.
        When both interceptors are used, this `post_get_cutover_job_with_metadata` interceptor runs after the
        `post_get_cutover_job` interceptor. The (possibly modified) response returned by
        `post_get_cutover_job` will be passed to
        `post_get_cutover_job_with_metadata`.
        """
        return response, metadata

    def pre_get_datacenter_connector(
        self,
        request: vmmigration.GetDatacenterConnectorRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.GetDatacenterConnectorRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_datacenter_connector

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_get_datacenter_connector(
        self, response: vmmigration.DatacenterConnector
    ) -> vmmigration.DatacenterConnector:
        """Post-rpc interceptor for get_datacenter_connector

        DEPRECATED. Please use the `post_get_datacenter_connector_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_get_datacenter_connector` interceptor runs
        before the `post_get_datacenter_connector_with_metadata` interceptor.
        """
        return response

    def post_get_datacenter_connector_with_metadata(
        self,
        response: vmmigration.DatacenterConnector,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.DatacenterConnector, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_datacenter_connector

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_get_datacenter_connector_with_metadata`
        interceptor in new development instead of the `post_get_datacenter_connector` interceptor.
        When both interceptors are used, this `post_get_datacenter_connector_with_metadata` interceptor runs after the
        `post_get_datacenter_connector` interceptor. The (possibly modified) response returned by
        `post_get_datacenter_connector` will be passed to
        `post_get_datacenter_connector_with_metadata`.
        """
        return response, metadata

    def pre_get_disk_migration_job(
        self,
        request: vmmigration.GetDiskMigrationJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.GetDiskMigrationJobRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_disk_migration_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_get_disk_migration_job(
        self, response: vmmigration.DiskMigrationJob
    ) -> vmmigration.DiskMigrationJob:
        """Post-rpc interceptor for get_disk_migration_job

        DEPRECATED. Please use the `post_get_disk_migration_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_get_disk_migration_job` interceptor runs
        before the `post_get_disk_migration_job_with_metadata` interceptor.
        """
        return response

    def post_get_disk_migration_job_with_metadata(
        self,
        response: vmmigration.DiskMigrationJob,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[vmmigration.DiskMigrationJob, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_disk_migration_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_get_disk_migration_job_with_metadata`
        interceptor in new development instead of the `post_get_disk_migration_job` interceptor.
        When both interceptors are used, this `post_get_disk_migration_job_with_metadata` interceptor runs after the
        `post_get_disk_migration_job` interceptor. The (possibly modified) response returned by
        `post_get_disk_migration_job` will be passed to
        `post_get_disk_migration_job_with_metadata`.
        """
        return response, metadata

    def pre_get_group(
        self,
        request: vmmigration.GetGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[vmmigration.GetGroupRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_get_group(self, response: vmmigration.Group) -> vmmigration.Group:
        """Post-rpc interceptor for get_group

        DEPRECATED. Please use the `post_get_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_get_group` interceptor runs
        before the `post_get_group_with_metadata` interceptor.
        """
        return response

    def post_get_group_with_metadata(
        self,
        response: vmmigration.Group,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[vmmigration.Group, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_get_group_with_metadata`
        interceptor in new development instead of the `post_get_group` interceptor.
        When both interceptors are used, this `post_get_group_with_metadata` interceptor runs after the
        `post_get_group` interceptor. The (possibly modified) response returned by
        `post_get_group` will be passed to
        `post_get_group_with_metadata`.
        """
        return response, metadata

    def pre_get_image_import(
        self,
        request: vmmigration.GetImageImportRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.GetImageImportRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_image_import

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_get_image_import(
        self, response: vmmigration.ImageImport
    ) -> vmmigration.ImageImport:
        """Post-rpc interceptor for get_image_import

        DEPRECATED. Please use the `post_get_image_import_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_get_image_import` interceptor runs
        before the `post_get_image_import_with_metadata` interceptor.
        """
        return response

    def post_get_image_import_with_metadata(
        self,
        response: vmmigration.ImageImport,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[vmmigration.ImageImport, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_image_import

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_get_image_import_with_metadata`
        interceptor in new development instead of the `post_get_image_import` interceptor.
        When both interceptors are used, this `post_get_image_import_with_metadata` interceptor runs after the
        `post_get_image_import` interceptor. The (possibly modified) response returned by
        `post_get_image_import` will be passed to
        `post_get_image_import_with_metadata`.
        """
        return response, metadata

    def pre_get_image_import_job(
        self,
        request: vmmigration.GetImageImportJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.GetImageImportJobRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_image_import_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_get_image_import_job(
        self, response: vmmigration.ImageImportJob
    ) -> vmmigration.ImageImportJob:
        """Post-rpc interceptor for get_image_import_job

        DEPRECATED. Please use the `post_get_image_import_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_get_image_import_job` interceptor runs
        before the `post_get_image_import_job_with_metadata` interceptor.
        """
        return response

    def post_get_image_import_job_with_metadata(
        self,
        response: vmmigration.ImageImportJob,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[vmmigration.ImageImportJob, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_image_import_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_get_image_import_job_with_metadata`
        interceptor in new development instead of the `post_get_image_import_job` interceptor.
        When both interceptors are used, this `post_get_image_import_job_with_metadata` interceptor runs after the
        `post_get_image_import_job` interceptor. The (possibly modified) response returned by
        `post_get_image_import_job` will be passed to
        `post_get_image_import_job_with_metadata`.
        """
        return response, metadata

    def pre_get_migrating_vm(
        self,
        request: vmmigration.GetMigratingVmRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.GetMigratingVmRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_migrating_vm

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_get_migrating_vm(
        self, response: vmmigration.MigratingVm
    ) -> vmmigration.MigratingVm:
        """Post-rpc interceptor for get_migrating_vm

        DEPRECATED. Please use the `post_get_migrating_vm_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_get_migrating_vm` interceptor runs
        before the `post_get_migrating_vm_with_metadata` interceptor.
        """
        return response

    def post_get_migrating_vm_with_metadata(
        self,
        response: vmmigration.MigratingVm,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[vmmigration.MigratingVm, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_migrating_vm

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_get_migrating_vm_with_metadata`
        interceptor in new development instead of the `post_get_migrating_vm` interceptor.
        When both interceptors are used, this `post_get_migrating_vm_with_metadata` interceptor runs after the
        `post_get_migrating_vm` interceptor. The (possibly modified) response returned by
        `post_get_migrating_vm` will be passed to
        `post_get_migrating_vm_with_metadata`.
        """
        return response, metadata

    def pre_get_replication_cycle(
        self,
        request: vmmigration.GetReplicationCycleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.GetReplicationCycleRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_replication_cycle

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_get_replication_cycle(
        self, response: vmmigration.ReplicationCycle
    ) -> vmmigration.ReplicationCycle:
        """Post-rpc interceptor for get_replication_cycle

        DEPRECATED. Please use the `post_get_replication_cycle_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_get_replication_cycle` interceptor runs
        before the `post_get_replication_cycle_with_metadata` interceptor.
        """
        return response

    def post_get_replication_cycle_with_metadata(
        self,
        response: vmmigration.ReplicationCycle,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[vmmigration.ReplicationCycle, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_replication_cycle

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_get_replication_cycle_with_metadata`
        interceptor in new development instead of the `post_get_replication_cycle` interceptor.
        When both interceptors are used, this `post_get_replication_cycle_with_metadata` interceptor runs after the
        `post_get_replication_cycle` interceptor. The (possibly modified) response returned by
        `post_get_replication_cycle` will be passed to
        `post_get_replication_cycle_with_metadata`.
        """
        return response, metadata

    def pre_get_source(
        self,
        request: vmmigration.GetSourceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[vmmigration.GetSourceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_source

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_get_source(self, response: vmmigration.Source) -> vmmigration.Source:
        """Post-rpc interceptor for get_source

        DEPRECATED. Please use the `post_get_source_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_get_source` interceptor runs
        before the `post_get_source_with_metadata` interceptor.
        """
        return response

    def post_get_source_with_metadata(
        self,
        response: vmmigration.Source,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[vmmigration.Source, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_source

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_get_source_with_metadata`
        interceptor in new development instead of the `post_get_source` interceptor.
        When both interceptors are used, this `post_get_source_with_metadata` interceptor runs after the
        `post_get_source` interceptor. The (possibly modified) response returned by
        `post_get_source` will be passed to
        `post_get_source_with_metadata`.
        """
        return response, metadata

    def pre_get_target_project(
        self,
        request: vmmigration.GetTargetProjectRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.GetTargetProjectRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_target_project

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_get_target_project(
        self, response: vmmigration.TargetProject
    ) -> vmmigration.TargetProject:
        """Post-rpc interceptor for get_target_project

        DEPRECATED. Please use the `post_get_target_project_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_get_target_project` interceptor runs
        before the `post_get_target_project_with_metadata` interceptor.
        """
        return response

    def post_get_target_project_with_metadata(
        self,
        response: vmmigration.TargetProject,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[vmmigration.TargetProject, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_target_project

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_get_target_project_with_metadata`
        interceptor in new development instead of the `post_get_target_project` interceptor.
        When both interceptors are used, this `post_get_target_project_with_metadata` interceptor runs after the
        `post_get_target_project` interceptor. The (possibly modified) response returned by
        `post_get_target_project` will be passed to
        `post_get_target_project_with_metadata`.
        """
        return response, metadata

    def pre_get_utilization_report(
        self,
        request: vmmigration.GetUtilizationReportRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.GetUtilizationReportRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_utilization_report

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_get_utilization_report(
        self, response: vmmigration.UtilizationReport
    ) -> vmmigration.UtilizationReport:
        """Post-rpc interceptor for get_utilization_report

        DEPRECATED. Please use the `post_get_utilization_report_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_get_utilization_report` interceptor runs
        before the `post_get_utilization_report_with_metadata` interceptor.
        """
        return response

    def post_get_utilization_report_with_metadata(
        self,
        response: vmmigration.UtilizationReport,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[vmmigration.UtilizationReport, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_utilization_report

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_get_utilization_report_with_metadata`
        interceptor in new development instead of the `post_get_utilization_report` interceptor.
        When both interceptors are used, this `post_get_utilization_report_with_metadata` interceptor runs after the
        `post_get_utilization_report` interceptor. The (possibly modified) response returned by
        `post_get_utilization_report` will be passed to
        `post_get_utilization_report_with_metadata`.
        """
        return response, metadata

    def pre_list_clone_jobs(
        self,
        request: vmmigration.ListCloneJobsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.ListCloneJobsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_clone_jobs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_list_clone_jobs(
        self, response: vmmigration.ListCloneJobsResponse
    ) -> vmmigration.ListCloneJobsResponse:
        """Post-rpc interceptor for list_clone_jobs

        DEPRECATED. Please use the `post_list_clone_jobs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_list_clone_jobs` interceptor runs
        before the `post_list_clone_jobs_with_metadata` interceptor.
        """
        return response

    def post_list_clone_jobs_with_metadata(
        self,
        response: vmmigration.ListCloneJobsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.ListCloneJobsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_clone_jobs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_list_clone_jobs_with_metadata`
        interceptor in new development instead of the `post_list_clone_jobs` interceptor.
        When both interceptors are used, this `post_list_clone_jobs_with_metadata` interceptor runs after the
        `post_list_clone_jobs` interceptor. The (possibly modified) response returned by
        `post_list_clone_jobs` will be passed to
        `post_list_clone_jobs_with_metadata`.
        """
        return response, metadata

    def pre_list_cutover_jobs(
        self,
        request: vmmigration.ListCutoverJobsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.ListCutoverJobsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_cutover_jobs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_list_cutover_jobs(
        self, response: vmmigration.ListCutoverJobsResponse
    ) -> vmmigration.ListCutoverJobsResponse:
        """Post-rpc interceptor for list_cutover_jobs

        DEPRECATED. Please use the `post_list_cutover_jobs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_list_cutover_jobs` interceptor runs
        before the `post_list_cutover_jobs_with_metadata` interceptor.
        """
        return response

    def post_list_cutover_jobs_with_metadata(
        self,
        response: vmmigration.ListCutoverJobsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.ListCutoverJobsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_cutover_jobs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_list_cutover_jobs_with_metadata`
        interceptor in new development instead of the `post_list_cutover_jobs` interceptor.
        When both interceptors are used, this `post_list_cutover_jobs_with_metadata` interceptor runs after the
        `post_list_cutover_jobs` interceptor. The (possibly modified) response returned by
        `post_list_cutover_jobs` will be passed to
        `post_list_cutover_jobs_with_metadata`.
        """
        return response, metadata

    def pre_list_datacenter_connectors(
        self,
        request: vmmigration.ListDatacenterConnectorsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.ListDatacenterConnectorsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_datacenter_connectors

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_list_datacenter_connectors(
        self, response: vmmigration.ListDatacenterConnectorsResponse
    ) -> vmmigration.ListDatacenterConnectorsResponse:
        """Post-rpc interceptor for list_datacenter_connectors

        DEPRECATED. Please use the `post_list_datacenter_connectors_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_list_datacenter_connectors` interceptor runs
        before the `post_list_datacenter_connectors_with_metadata` interceptor.
        """
        return response

    def post_list_datacenter_connectors_with_metadata(
        self,
        response: vmmigration.ListDatacenterConnectorsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.ListDatacenterConnectorsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_datacenter_connectors

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_list_datacenter_connectors_with_metadata`
        interceptor in new development instead of the `post_list_datacenter_connectors` interceptor.
        When both interceptors are used, this `post_list_datacenter_connectors_with_metadata` interceptor runs after the
        `post_list_datacenter_connectors` interceptor. The (possibly modified) response returned by
        `post_list_datacenter_connectors` will be passed to
        `post_list_datacenter_connectors_with_metadata`.
        """
        return response, metadata

    def pre_list_disk_migration_jobs(
        self,
        request: vmmigration.ListDiskMigrationJobsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.ListDiskMigrationJobsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_disk_migration_jobs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_list_disk_migration_jobs(
        self, response: vmmigration.ListDiskMigrationJobsResponse
    ) -> vmmigration.ListDiskMigrationJobsResponse:
        """Post-rpc interceptor for list_disk_migration_jobs

        DEPRECATED. Please use the `post_list_disk_migration_jobs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_list_disk_migration_jobs` interceptor runs
        before the `post_list_disk_migration_jobs_with_metadata` interceptor.
        """
        return response

    def post_list_disk_migration_jobs_with_metadata(
        self,
        response: vmmigration.ListDiskMigrationJobsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.ListDiskMigrationJobsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_disk_migration_jobs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_list_disk_migration_jobs_with_metadata`
        interceptor in new development instead of the `post_list_disk_migration_jobs` interceptor.
        When both interceptors are used, this `post_list_disk_migration_jobs_with_metadata` interceptor runs after the
        `post_list_disk_migration_jobs` interceptor. The (possibly modified) response returned by
        `post_list_disk_migration_jobs` will be passed to
        `post_list_disk_migration_jobs_with_metadata`.
        """
        return response, metadata

    def pre_list_groups(
        self,
        request: vmmigration.ListGroupsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[vmmigration.ListGroupsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_groups

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_list_groups(
        self, response: vmmigration.ListGroupsResponse
    ) -> vmmigration.ListGroupsResponse:
        """Post-rpc interceptor for list_groups

        DEPRECATED. Please use the `post_list_groups_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_list_groups` interceptor runs
        before the `post_list_groups_with_metadata` interceptor.
        """
        return response

    def post_list_groups_with_metadata(
        self,
        response: vmmigration.ListGroupsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[vmmigration.ListGroupsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_groups

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_list_groups_with_metadata`
        interceptor in new development instead of the `post_list_groups` interceptor.
        When both interceptors are used, this `post_list_groups_with_metadata` interceptor runs after the
        `post_list_groups` interceptor. The (possibly modified) response returned by
        `post_list_groups` will be passed to
        `post_list_groups_with_metadata`.
        """
        return response, metadata

    def pre_list_image_import_jobs(
        self,
        request: vmmigration.ListImageImportJobsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.ListImageImportJobsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_image_import_jobs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_list_image_import_jobs(
        self, response: vmmigration.ListImageImportJobsResponse
    ) -> vmmigration.ListImageImportJobsResponse:
        """Post-rpc interceptor for list_image_import_jobs

        DEPRECATED. Please use the `post_list_image_import_jobs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_list_image_import_jobs` interceptor runs
        before the `post_list_image_import_jobs_with_metadata` interceptor.
        """
        return response

    def post_list_image_import_jobs_with_metadata(
        self,
        response: vmmigration.ListImageImportJobsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.ListImageImportJobsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_image_import_jobs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_list_image_import_jobs_with_metadata`
        interceptor in new development instead of the `post_list_image_import_jobs` interceptor.
        When both interceptors are used, this `post_list_image_import_jobs_with_metadata` interceptor runs after the
        `post_list_image_import_jobs` interceptor. The (possibly modified) response returned by
        `post_list_image_import_jobs` will be passed to
        `post_list_image_import_jobs_with_metadata`.
        """
        return response, metadata

    def pre_list_image_imports(
        self,
        request: vmmigration.ListImageImportsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.ListImageImportsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_image_imports

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_list_image_imports(
        self, response: vmmigration.ListImageImportsResponse
    ) -> vmmigration.ListImageImportsResponse:
        """Post-rpc interceptor for list_image_imports

        DEPRECATED. Please use the `post_list_image_imports_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_list_image_imports` interceptor runs
        before the `post_list_image_imports_with_metadata` interceptor.
        """
        return response

    def post_list_image_imports_with_metadata(
        self,
        response: vmmigration.ListImageImportsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.ListImageImportsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_image_imports

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_list_image_imports_with_metadata`
        interceptor in new development instead of the `post_list_image_imports` interceptor.
        When both interceptors are used, this `post_list_image_imports_with_metadata` interceptor runs after the
        `post_list_image_imports` interceptor. The (possibly modified) response returned by
        `post_list_image_imports` will be passed to
        `post_list_image_imports_with_metadata`.
        """
        return response, metadata

    def pre_list_migrating_vms(
        self,
        request: vmmigration.ListMigratingVmsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.ListMigratingVmsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_migrating_vms

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_list_migrating_vms(
        self, response: vmmigration.ListMigratingVmsResponse
    ) -> vmmigration.ListMigratingVmsResponse:
        """Post-rpc interceptor for list_migrating_vms

        DEPRECATED. Please use the `post_list_migrating_vms_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_list_migrating_vms` interceptor runs
        before the `post_list_migrating_vms_with_metadata` interceptor.
        """
        return response

    def post_list_migrating_vms_with_metadata(
        self,
        response: vmmigration.ListMigratingVmsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.ListMigratingVmsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_migrating_vms

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_list_migrating_vms_with_metadata`
        interceptor in new development instead of the `post_list_migrating_vms` interceptor.
        When both interceptors are used, this `post_list_migrating_vms_with_metadata` interceptor runs after the
        `post_list_migrating_vms` interceptor. The (possibly modified) response returned by
        `post_list_migrating_vms` will be passed to
        `post_list_migrating_vms_with_metadata`.
        """
        return response, metadata

    def pre_list_replication_cycles(
        self,
        request: vmmigration.ListReplicationCyclesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.ListReplicationCyclesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_replication_cycles

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_list_replication_cycles(
        self, response: vmmigration.ListReplicationCyclesResponse
    ) -> vmmigration.ListReplicationCyclesResponse:
        """Post-rpc interceptor for list_replication_cycles

        DEPRECATED. Please use the `post_list_replication_cycles_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_list_replication_cycles` interceptor runs
        before the `post_list_replication_cycles_with_metadata` interceptor.
        """
        return response

    def post_list_replication_cycles_with_metadata(
        self,
        response: vmmigration.ListReplicationCyclesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.ListReplicationCyclesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_replication_cycles

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_list_replication_cycles_with_metadata`
        interceptor in new development instead of the `post_list_replication_cycles` interceptor.
        When both interceptors are used, this `post_list_replication_cycles_with_metadata` interceptor runs after the
        `post_list_replication_cycles` interceptor. The (possibly modified) response returned by
        `post_list_replication_cycles` will be passed to
        `post_list_replication_cycles_with_metadata`.
        """
        return response, metadata

    def pre_list_sources(
        self,
        request: vmmigration.ListSourcesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[vmmigration.ListSourcesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_sources

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_list_sources(
        self, response: vmmigration.ListSourcesResponse
    ) -> vmmigration.ListSourcesResponse:
        """Post-rpc interceptor for list_sources

        DEPRECATED. Please use the `post_list_sources_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_list_sources` interceptor runs
        before the `post_list_sources_with_metadata` interceptor.
        """
        return response

    def post_list_sources_with_metadata(
        self,
        response: vmmigration.ListSourcesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.ListSourcesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_sources

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_list_sources_with_metadata`
        interceptor in new development instead of the `post_list_sources` interceptor.
        When both interceptors are used, this `post_list_sources_with_metadata` interceptor runs after the
        `post_list_sources` interceptor. The (possibly modified) response returned by
        `post_list_sources` will be passed to
        `post_list_sources_with_metadata`.
        """
        return response, metadata

    def pre_list_target_projects(
        self,
        request: vmmigration.ListTargetProjectsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.ListTargetProjectsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_target_projects

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_list_target_projects(
        self, response: vmmigration.ListTargetProjectsResponse
    ) -> vmmigration.ListTargetProjectsResponse:
        """Post-rpc interceptor for list_target_projects

        DEPRECATED. Please use the `post_list_target_projects_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_list_target_projects` interceptor runs
        before the `post_list_target_projects_with_metadata` interceptor.
        """
        return response

    def post_list_target_projects_with_metadata(
        self,
        response: vmmigration.ListTargetProjectsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.ListTargetProjectsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_target_projects

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_list_target_projects_with_metadata`
        interceptor in new development instead of the `post_list_target_projects` interceptor.
        When both interceptors are used, this `post_list_target_projects_with_metadata` interceptor runs after the
        `post_list_target_projects` interceptor. The (possibly modified) response returned by
        `post_list_target_projects` will be passed to
        `post_list_target_projects_with_metadata`.
        """
        return response, metadata

    def pre_list_utilization_reports(
        self,
        request: vmmigration.ListUtilizationReportsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.ListUtilizationReportsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_utilization_reports

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_list_utilization_reports(
        self, response: vmmigration.ListUtilizationReportsResponse
    ) -> vmmigration.ListUtilizationReportsResponse:
        """Post-rpc interceptor for list_utilization_reports

        DEPRECATED. Please use the `post_list_utilization_reports_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_list_utilization_reports` interceptor runs
        before the `post_list_utilization_reports_with_metadata` interceptor.
        """
        return response

    def post_list_utilization_reports_with_metadata(
        self,
        response: vmmigration.ListUtilizationReportsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.ListUtilizationReportsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_utilization_reports

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_list_utilization_reports_with_metadata`
        interceptor in new development instead of the `post_list_utilization_reports` interceptor.
        When both interceptors are used, this `post_list_utilization_reports_with_metadata` interceptor runs after the
        `post_list_utilization_reports` interceptor. The (possibly modified) response returned by
        `post_list_utilization_reports` will be passed to
        `post_list_utilization_reports_with_metadata`.
        """
        return response, metadata

    def pre_pause_migration(
        self,
        request: vmmigration.PauseMigrationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.PauseMigrationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for pause_migration

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_pause_migration(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for pause_migration

        DEPRECATED. Please use the `post_pause_migration_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_pause_migration` interceptor runs
        before the `post_pause_migration_with_metadata` interceptor.
        """
        return response

    def post_pause_migration_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for pause_migration

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_pause_migration_with_metadata`
        interceptor in new development instead of the `post_pause_migration` interceptor.
        When both interceptors are used, this `post_pause_migration_with_metadata` interceptor runs after the
        `post_pause_migration` interceptor. The (possibly modified) response returned by
        `post_pause_migration` will be passed to
        `post_pause_migration_with_metadata`.
        """
        return response, metadata

    def pre_remove_group_migration(
        self,
        request: vmmigration.RemoveGroupMigrationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.RemoveGroupMigrationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for remove_group_migration

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_remove_group_migration(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for remove_group_migration

        DEPRECATED. Please use the `post_remove_group_migration_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_remove_group_migration` interceptor runs
        before the `post_remove_group_migration_with_metadata` interceptor.
        """
        return response

    def post_remove_group_migration_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for remove_group_migration

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_remove_group_migration_with_metadata`
        interceptor in new development instead of the `post_remove_group_migration` interceptor.
        When both interceptors are used, this `post_remove_group_migration_with_metadata` interceptor runs after the
        `post_remove_group_migration` interceptor. The (possibly modified) response returned by
        `post_remove_group_migration` will be passed to
        `post_remove_group_migration_with_metadata`.
        """
        return response, metadata

    def pre_resume_migration(
        self,
        request: vmmigration.ResumeMigrationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.ResumeMigrationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for resume_migration

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_resume_migration(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for resume_migration

        DEPRECATED. Please use the `post_resume_migration_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_resume_migration` interceptor runs
        before the `post_resume_migration_with_metadata` interceptor.
        """
        return response

    def post_resume_migration_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for resume_migration

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_resume_migration_with_metadata`
        interceptor in new development instead of the `post_resume_migration` interceptor.
        When both interceptors are used, this `post_resume_migration_with_metadata` interceptor runs after the
        `post_resume_migration` interceptor. The (possibly modified) response returned by
        `post_resume_migration` will be passed to
        `post_resume_migration_with_metadata`.
        """
        return response, metadata

    def pre_run_disk_migration_job(
        self,
        request: vmmigration.RunDiskMigrationJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.RunDiskMigrationJobRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for run_disk_migration_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_run_disk_migration_job(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for run_disk_migration_job

        DEPRECATED. Please use the `post_run_disk_migration_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_run_disk_migration_job` interceptor runs
        before the `post_run_disk_migration_job_with_metadata` interceptor.
        """
        return response

    def post_run_disk_migration_job_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for run_disk_migration_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_run_disk_migration_job_with_metadata`
        interceptor in new development instead of the `post_run_disk_migration_job` interceptor.
        When both interceptors are used, this `post_run_disk_migration_job_with_metadata` interceptor runs after the
        `post_run_disk_migration_job` interceptor. The (possibly modified) response returned by
        `post_run_disk_migration_job` will be passed to
        `post_run_disk_migration_job_with_metadata`.
        """
        return response, metadata

    def pre_start_migration(
        self,
        request: vmmigration.StartMigrationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.StartMigrationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for start_migration

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_start_migration(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for start_migration

        DEPRECATED. Please use the `post_start_migration_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_start_migration` interceptor runs
        before the `post_start_migration_with_metadata` interceptor.
        """
        return response

    def post_start_migration_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for start_migration

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_start_migration_with_metadata`
        interceptor in new development instead of the `post_start_migration` interceptor.
        When both interceptors are used, this `post_start_migration_with_metadata` interceptor runs after the
        `post_start_migration` interceptor. The (possibly modified) response returned by
        `post_start_migration` will be passed to
        `post_start_migration_with_metadata`.
        """
        return response, metadata

    def pre_update_disk_migration_job(
        self,
        request: vmmigration.UpdateDiskMigrationJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.UpdateDiskMigrationJobRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_disk_migration_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_update_disk_migration_job(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_disk_migration_job

        DEPRECATED. Please use the `post_update_disk_migration_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_update_disk_migration_job` interceptor runs
        before the `post_update_disk_migration_job_with_metadata` interceptor.
        """
        return response

    def post_update_disk_migration_job_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_disk_migration_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_update_disk_migration_job_with_metadata`
        interceptor in new development instead of the `post_update_disk_migration_job` interceptor.
        When both interceptors are used, this `post_update_disk_migration_job_with_metadata` interceptor runs after the
        `post_update_disk_migration_job` interceptor. The (possibly modified) response returned by
        `post_update_disk_migration_job` will be passed to
        `post_update_disk_migration_job_with_metadata`.
        """
        return response, metadata

    def pre_update_group(
        self,
        request: vmmigration.UpdateGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[vmmigration.UpdateGroupRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_update_group(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_group

        DEPRECATED. Please use the `post_update_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_update_group` interceptor runs
        before the `post_update_group_with_metadata` interceptor.
        """
        return response

    def post_update_group_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_update_group_with_metadata`
        interceptor in new development instead of the `post_update_group` interceptor.
        When both interceptors are used, this `post_update_group_with_metadata` interceptor runs after the
        `post_update_group` interceptor. The (possibly modified) response returned by
        `post_update_group` will be passed to
        `post_update_group_with_metadata`.
        """
        return response, metadata

    def pre_update_migrating_vm(
        self,
        request: vmmigration.UpdateMigratingVmRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.UpdateMigratingVmRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_migrating_vm

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_update_migrating_vm(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_migrating_vm

        DEPRECATED. Please use the `post_update_migrating_vm_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_update_migrating_vm` interceptor runs
        before the `post_update_migrating_vm_with_metadata` interceptor.
        """
        return response

    def post_update_migrating_vm_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_migrating_vm

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_update_migrating_vm_with_metadata`
        interceptor in new development instead of the `post_update_migrating_vm` interceptor.
        When both interceptors are used, this `post_update_migrating_vm_with_metadata` interceptor runs after the
        `post_update_migrating_vm` interceptor. The (possibly modified) response returned by
        `post_update_migrating_vm` will be passed to
        `post_update_migrating_vm_with_metadata`.
        """
        return response, metadata

    def pre_update_source(
        self,
        request: vmmigration.UpdateSourceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.UpdateSourceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_source

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_update_source(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_source

        DEPRECATED. Please use the `post_update_source_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_update_source` interceptor runs
        before the `post_update_source_with_metadata` interceptor.
        """
        return response

    def post_update_source_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_source

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_update_source_with_metadata`
        interceptor in new development instead of the `post_update_source` interceptor.
        When both interceptors are used, this `post_update_source_with_metadata` interceptor runs after the
        `post_update_source` interceptor. The (possibly modified) response returned by
        `post_update_source` will be passed to
        `post_update_source_with_metadata`.
        """
        return response, metadata

    def pre_update_target_project(
        self,
        request: vmmigration.UpdateTargetProjectRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.UpdateTargetProjectRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_target_project

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_update_target_project(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_target_project

        DEPRECATED. Please use the `post_update_target_project_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_update_target_project` interceptor runs
        before the `post_update_target_project_with_metadata` interceptor.
        """
        return response

    def post_update_target_project_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_target_project

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_update_target_project_with_metadata`
        interceptor in new development instead of the `post_update_target_project` interceptor.
        When both interceptors are used, this `post_update_target_project_with_metadata` interceptor runs after the
        `post_update_target_project` interceptor. The (possibly modified) response returned by
        `post_update_target_project` will be passed to
        `post_update_target_project_with_metadata`.
        """
        return response, metadata

    def pre_upgrade_appliance(
        self,
        request: vmmigration.UpgradeApplianceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        vmmigration.UpgradeApplianceRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for upgrade_appliance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_upgrade_appliance(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for upgrade_appliance

        DEPRECATED. Please use the `post_upgrade_appliance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code. This `post_upgrade_appliance` interceptor runs
        before the `post_upgrade_appliance_with_metadata` interceptor.
        """
        return response

    def post_upgrade_appliance_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for upgrade_appliance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the VmMigration server but before it is returned to user code.

        We recommend only using this `post_upgrade_appliance_with_metadata`
        interceptor in new development instead of the `post_upgrade_appliance` interceptor.
        When both interceptors are used, this `post_upgrade_appliance_with_metadata` interceptor runs after the
        `post_upgrade_appliance` interceptor. The (possibly modified) response returned by
        `post_upgrade_appliance` will be passed to
        `post_upgrade_appliance_with_metadata`.
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
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the VmMigration server but before
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
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the VmMigration server but before
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
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the VmMigration server but before
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
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the VmMigration server but before
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
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the VmMigration server but before
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
        before they are sent to the VmMigration server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the VmMigration server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class VmMigrationRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: VmMigrationRestInterceptor


class VmMigrationRestTransport(_BaseVmMigrationRestTransport):
    """REST backend synchronous transport for VmMigration.

    VM Migration Service

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "vmmigration.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[VmMigrationRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'vmmigration.googleapis.com').
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
            interceptor (Optional[VmMigrationRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or VmMigrationRestInterceptor()
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

    class _AddGroupMigration(
        _BaseVmMigrationRestTransport._BaseAddGroupMigration, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.AddGroupMigration")

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
            request: vmmigration.AddGroupMigrationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the add group migration method over HTTP.

            Args:
                request (~.vmmigration.AddGroupMigrationRequest):
                    The request object. Request message for
                'AddGroupMigration' request.
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
                _BaseVmMigrationRestTransport._BaseAddGroupMigration._get_http_options()
            )
            request, metadata = self._interceptor.pre_add_group_migration(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseAddGroupMigration,
                    "_BaseAddGroupMigration__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.AddGroupMigration",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "AddGroupMigration",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._AddGroupMigration._get_response(
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

            resp = self._interceptor.post_add_group_migration(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_add_group_migration_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.add_group_migration",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "AddGroupMigration",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CancelCloneJob(
        _BaseVmMigrationRestTransport._BaseCancelCloneJob, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.CancelCloneJob")

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
            request: vmmigration.CancelCloneJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the cancel clone job method over HTTP.

            Args:
                request (~.vmmigration.CancelCloneJobRequest):
                    The request object. Request message for 'CancelCloneJob'
                request.
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
                _BaseVmMigrationRestTransport._BaseCancelCloneJob._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_clone_job(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseCancelCloneJob,
                    "_BaseCancelCloneJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.CancelCloneJob",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "CancelCloneJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._CancelCloneJob._get_response(
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

            resp = self._interceptor.post_cancel_clone_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_cancel_clone_job_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.cancel_clone_job",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "CancelCloneJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CancelCutoverJob(
        _BaseVmMigrationRestTransport._BaseCancelCutoverJob, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.CancelCutoverJob")

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
            request: vmmigration.CancelCutoverJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the cancel cutover job method over HTTP.

            Args:
                request (~.vmmigration.CancelCutoverJobRequest):
                    The request object. Request message for
                'CancelCutoverJob' request.
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
                _BaseVmMigrationRestTransport._BaseCancelCutoverJob._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_cutover_job(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseCancelCutoverJob,
                    "_BaseCancelCutoverJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.CancelCutoverJob",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "CancelCutoverJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._CancelCutoverJob._get_response(
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

            resp = self._interceptor.post_cancel_cutover_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_cancel_cutover_job_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.cancel_cutover_job",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "CancelCutoverJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CancelDiskMigrationJob(
        _BaseVmMigrationRestTransport._BaseCancelDiskMigrationJob, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.CancelDiskMigrationJob")

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
            request: vmmigration.CancelDiskMigrationJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the cancel disk migration job method over HTTP.

            Args:
                request (~.vmmigration.CancelDiskMigrationJobRequest):
                    The request object. Request message for
                'CancelDiskMigrationJob' request.
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

            http_options = _BaseVmMigrationRestTransport._BaseCancelDiskMigrationJob._get_http_options()
            request, metadata = self._interceptor.pre_cancel_disk_migration_job(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseCancelDiskMigrationJob,
                    "_BaseCancelDiskMigrationJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.CancelDiskMigrationJob",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "CancelDiskMigrationJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._CancelDiskMigrationJob._get_response(
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

            resp = self._interceptor.post_cancel_disk_migration_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_cancel_disk_migration_job_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.cancel_disk_migration_job",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "CancelDiskMigrationJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CancelImageImportJob(
        _BaseVmMigrationRestTransport._BaseCancelImageImportJob, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.CancelImageImportJob")

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
            request: vmmigration.CancelImageImportJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the cancel image import job method over HTTP.

            Args:
                request (~.vmmigration.CancelImageImportJobRequest):
                    The request object. Request message for
                'CancelImageImportJob' request.
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

            http_options = _BaseVmMigrationRestTransport._BaseCancelImageImportJob._get_http_options()
            request, metadata = self._interceptor.pre_cancel_image_import_job(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseCancelImageImportJob,
                    "_BaseCancelImageImportJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.CancelImageImportJob",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "CancelImageImportJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._CancelImageImportJob._get_response(
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

            resp = self._interceptor.post_cancel_image_import_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_cancel_image_import_job_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.cancel_image_import_job",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "CancelImageImportJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateCloneJob(
        _BaseVmMigrationRestTransport._BaseCreateCloneJob, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.CreateCloneJob")

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
            request: vmmigration.CreateCloneJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create clone job method over HTTP.

            Args:
                request (~.vmmigration.CreateCloneJobRequest):
                    The request object. Request message for 'CreateCloneJob'
                request.
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
                _BaseVmMigrationRestTransport._BaseCreateCloneJob._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_clone_job(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseCreateCloneJob,
                    "_BaseCreateCloneJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.CreateCloneJob",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "CreateCloneJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._CreateCloneJob._get_response(
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

            resp = self._interceptor.post_create_clone_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_clone_job_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.create_clone_job",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "CreateCloneJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateCutoverJob(
        _BaseVmMigrationRestTransport._BaseCreateCutoverJob, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.CreateCutoverJob")

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
            request: vmmigration.CreateCutoverJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create cutover job method over HTTP.

            Args:
                request (~.vmmigration.CreateCutoverJobRequest):
                    The request object. Request message for
                'CreateCutoverJob' request.
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
                _BaseVmMigrationRestTransport._BaseCreateCutoverJob._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_cutover_job(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseCreateCutoverJob,
                    "_BaseCreateCutoverJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.CreateCutoverJob",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "CreateCutoverJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._CreateCutoverJob._get_response(
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

            resp = self._interceptor.post_create_cutover_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_cutover_job_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.create_cutover_job",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "CreateCutoverJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateDatacenterConnector(
        _BaseVmMigrationRestTransport._BaseCreateDatacenterConnector,
        VmMigrationRestStub,
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.CreateDatacenterConnector")

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
            request: vmmigration.CreateDatacenterConnectorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create datacenter
            connector method over HTTP.

                Args:
                    request (~.vmmigration.CreateDatacenterConnectorRequest):
                        The request object. Request message for
                    'CreateDatacenterConnector' request.
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

            http_options = _BaseVmMigrationRestTransport._BaseCreateDatacenterConnector._get_http_options()
            request, metadata = self._interceptor.pre_create_datacenter_connector(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseCreateDatacenterConnector,
                    "_BaseCreateDatacenterConnector__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.CreateDatacenterConnector",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "CreateDatacenterConnector",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                VmMigrationRestTransport._CreateDatacenterConnector._get_response(
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

            resp = self._interceptor.post_create_datacenter_connector(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_datacenter_connector_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.create_datacenter_connector",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "CreateDatacenterConnector",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateDiskMigrationJob(
        _BaseVmMigrationRestTransport._BaseCreateDiskMigrationJob, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.CreateDiskMigrationJob")

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
            request: vmmigration.CreateDiskMigrationJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create disk migration job method over HTTP.

            Args:
                request (~.vmmigration.CreateDiskMigrationJobRequest):
                    The request object. Request message for
                'CreateDiskMigrationJob' request.
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

            http_options = _BaseVmMigrationRestTransport._BaseCreateDiskMigrationJob._get_http_options()
            request, metadata = self._interceptor.pre_create_disk_migration_job(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseCreateDiskMigrationJob,
                    "_BaseCreateDiskMigrationJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.CreateDiskMigrationJob",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "CreateDiskMigrationJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._CreateDiskMigrationJob._get_response(
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

            resp = self._interceptor.post_create_disk_migration_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_disk_migration_job_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.create_disk_migration_job",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "CreateDiskMigrationJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateGroup(
        _BaseVmMigrationRestTransport._BaseCreateGroup, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.CreateGroup")

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
            request: vmmigration.CreateGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create group method over HTTP.

            Args:
                request (~.vmmigration.CreateGroupRequest):
                    The request object. Request message for 'CreateGroup'
                request.
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
                _BaseVmMigrationRestTransport._BaseCreateGroup._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_group(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseCreateGroup,
                    "_BaseCreateGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.CreateGroup",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "CreateGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._CreateGroup._get_response(
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

            resp = self._interceptor.post_create_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_group_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.create_group",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "CreateGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateImageImport(
        _BaseVmMigrationRestTransport._BaseCreateImageImport, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.CreateImageImport")

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
            request: vmmigration.CreateImageImportRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create image import method over HTTP.

            Args:
                request (~.vmmigration.CreateImageImportRequest):
                    The request object. Request message for
                'CreateImageImport' request.
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
                _BaseVmMigrationRestTransport._BaseCreateImageImport._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_image_import(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseCreateImageImport,
                    "_BaseCreateImageImport__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.CreateImageImport",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "CreateImageImport",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._CreateImageImport._get_response(
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

            resp = self._interceptor.post_create_image_import(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_image_import_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.create_image_import",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "CreateImageImport",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateMigratingVm(
        _BaseVmMigrationRestTransport._BaseCreateMigratingVm, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.CreateMigratingVm")

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
            request: vmmigration.CreateMigratingVmRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create migrating vm method over HTTP.

            Args:
                request (~.vmmigration.CreateMigratingVmRequest):
                    The request object. Request message for
                'CreateMigratingVm' request.
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
                _BaseVmMigrationRestTransport._BaseCreateMigratingVm._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_migrating_vm(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseCreateMigratingVm,
                    "_BaseCreateMigratingVm__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.CreateMigratingVm",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "CreateMigratingVm",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._CreateMigratingVm._get_response(
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

            resp = self._interceptor.post_create_migrating_vm(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_migrating_vm_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.create_migrating_vm",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "CreateMigratingVm",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateSource(
        _BaseVmMigrationRestTransport._BaseCreateSource, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.CreateSource")

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
            request: vmmigration.CreateSourceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create source method over HTTP.

            Args:
                request (~.vmmigration.CreateSourceRequest):
                    The request object. Request message for 'CreateSource'
                request.
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
                _BaseVmMigrationRestTransport._BaseCreateSource._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_source(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseCreateSource,
                    "_BaseCreateSource__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.CreateSource",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "CreateSource",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._CreateSource._get_response(
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

            resp = self._interceptor.post_create_source(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_source_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.create_source",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "CreateSource",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateTargetProject(
        _BaseVmMigrationRestTransport._BaseCreateTargetProject, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.CreateTargetProject")

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
            request: vmmigration.CreateTargetProjectRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create target project method over HTTP.

            Args:
                request (~.vmmigration.CreateTargetProjectRequest):
                    The request object. Request message for
                'CreateTargetProject' request.
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

            http_options = _BaseVmMigrationRestTransport._BaseCreateTargetProject._get_http_options()
            request, metadata = self._interceptor.pre_create_target_project(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseCreateTargetProject,
                    "_BaseCreateTargetProject__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.CreateTargetProject",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "CreateTargetProject",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._CreateTargetProject._get_response(
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

            resp = self._interceptor.post_create_target_project(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_target_project_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.create_target_project",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "CreateTargetProject",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateUtilizationReport(
        _BaseVmMigrationRestTransport._BaseCreateUtilizationReport, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.CreateUtilizationReport")

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
            request: vmmigration.CreateUtilizationReportRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create utilization report method over HTTP.

            Args:
                request (~.vmmigration.CreateUtilizationReportRequest):
                    The request object. Request message for
                'CreateUtilizationReport' request.
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

            http_options = _BaseVmMigrationRestTransport._BaseCreateUtilizationReport._get_http_options()
            request, metadata = self._interceptor.pre_create_utilization_report(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseCreateUtilizationReport,
                    "_BaseCreateUtilizationReport__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.CreateUtilizationReport",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "CreateUtilizationReport",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._CreateUtilizationReport._get_response(
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

            resp = self._interceptor.post_create_utilization_report(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_utilization_report_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.create_utilization_report",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "CreateUtilizationReport",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteDatacenterConnector(
        _BaseVmMigrationRestTransport._BaseDeleteDatacenterConnector,
        VmMigrationRestStub,
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.DeleteDatacenterConnector")

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
            request: vmmigration.DeleteDatacenterConnectorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete datacenter
            connector method over HTTP.

                Args:
                    request (~.vmmigration.DeleteDatacenterConnectorRequest):
                        The request object. Request message for
                    'DeleteDatacenterConnector' request.
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

            http_options = _BaseVmMigrationRestTransport._BaseDeleteDatacenterConnector._get_http_options()
            request, metadata = self._interceptor.pre_delete_datacenter_connector(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseDeleteDatacenterConnector,
                    "_BaseDeleteDatacenterConnector__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.DeleteDatacenterConnector",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "DeleteDatacenterConnector",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                VmMigrationRestTransport._DeleteDatacenterConnector._get_response(
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

            resp = self._interceptor.post_delete_datacenter_connector(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_datacenter_connector_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.delete_datacenter_connector",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "DeleteDatacenterConnector",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteDiskMigrationJob(
        _BaseVmMigrationRestTransport._BaseDeleteDiskMigrationJob, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.DeleteDiskMigrationJob")

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
            request: vmmigration.DeleteDiskMigrationJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete disk migration job method over HTTP.

            Args:
                request (~.vmmigration.DeleteDiskMigrationJobRequest):
                    The request object. Request message for
                'DeleteDiskMigrationJob' request.
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

            http_options = _BaseVmMigrationRestTransport._BaseDeleteDiskMigrationJob._get_http_options()
            request, metadata = self._interceptor.pre_delete_disk_migration_job(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseDeleteDiskMigrationJob,
                    "_BaseDeleteDiskMigrationJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.DeleteDiskMigrationJob",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "DeleteDiskMigrationJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._DeleteDiskMigrationJob._get_response(
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

            resp = self._interceptor.post_delete_disk_migration_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_disk_migration_job_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.delete_disk_migration_job",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "DeleteDiskMigrationJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteGroup(
        _BaseVmMigrationRestTransport._BaseDeleteGroup, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.DeleteGroup")

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
            request: vmmigration.DeleteGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete group method over HTTP.

            Args:
                request (~.vmmigration.DeleteGroupRequest):
                    The request object. Request message for 'DeleteGroup'
                request.
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
                _BaseVmMigrationRestTransport._BaseDeleteGroup._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_group(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseDeleteGroup,
                    "_BaseDeleteGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.DeleteGroup",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "DeleteGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._DeleteGroup._get_response(
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

            resp = self._interceptor.post_delete_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_group_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.delete_group",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "DeleteGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteImageImport(
        _BaseVmMigrationRestTransport._BaseDeleteImageImport, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.DeleteImageImport")

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
            request: vmmigration.DeleteImageImportRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete image import method over HTTP.

            Args:
                request (~.vmmigration.DeleteImageImportRequest):
                    The request object. Request message for
                'DeleteImageImport' request.
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
                _BaseVmMigrationRestTransport._BaseDeleteImageImport._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_image_import(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseDeleteImageImport,
                    "_BaseDeleteImageImport__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.DeleteImageImport",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "DeleteImageImport",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._DeleteImageImport._get_response(
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

            resp = self._interceptor.post_delete_image_import(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_image_import_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.delete_image_import",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "DeleteImageImport",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteMigratingVm(
        _BaseVmMigrationRestTransport._BaseDeleteMigratingVm, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.DeleteMigratingVm")

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
            request: vmmigration.DeleteMigratingVmRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete migrating vm method over HTTP.

            Args:
                request (~.vmmigration.DeleteMigratingVmRequest):
                    The request object. Request message for
                'DeleteMigratingVm' request.
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
                _BaseVmMigrationRestTransport._BaseDeleteMigratingVm._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_migrating_vm(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseDeleteMigratingVm,
                    "_BaseDeleteMigratingVm__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.DeleteMigratingVm",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "DeleteMigratingVm",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._DeleteMigratingVm._get_response(
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

            resp = self._interceptor.post_delete_migrating_vm(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_migrating_vm_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.delete_migrating_vm",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "DeleteMigratingVm",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteSource(
        _BaseVmMigrationRestTransport._BaseDeleteSource, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.DeleteSource")

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
            request: vmmigration.DeleteSourceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete source method over HTTP.

            Args:
                request (~.vmmigration.DeleteSourceRequest):
                    The request object. Request message for 'DeleteSource'
                request.
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
                _BaseVmMigrationRestTransport._BaseDeleteSource._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_source(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseDeleteSource,
                    "_BaseDeleteSource__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.DeleteSource",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "DeleteSource",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._DeleteSource._get_response(
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

            resp = self._interceptor.post_delete_source(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_source_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.delete_source",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "DeleteSource",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteTargetProject(
        _BaseVmMigrationRestTransport._BaseDeleteTargetProject, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.DeleteTargetProject")

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
            request: vmmigration.DeleteTargetProjectRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete target project method over HTTP.

            Args:
                request (~.vmmigration.DeleteTargetProjectRequest):
                    The request object. Request message for
                'DeleteTargetProject' request.
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

            http_options = _BaseVmMigrationRestTransport._BaseDeleteTargetProject._get_http_options()
            request, metadata = self._interceptor.pre_delete_target_project(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseDeleteTargetProject,
                    "_BaseDeleteTargetProject__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.DeleteTargetProject",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "DeleteTargetProject",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._DeleteTargetProject._get_response(
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

            resp = self._interceptor.post_delete_target_project(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_target_project_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.delete_target_project",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "DeleteTargetProject",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteUtilizationReport(
        _BaseVmMigrationRestTransport._BaseDeleteUtilizationReport, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.DeleteUtilizationReport")

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
            request: vmmigration.DeleteUtilizationReportRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete utilization report method over HTTP.

            Args:
                request (~.vmmigration.DeleteUtilizationReportRequest):
                    The request object. Request message for
                'DeleteUtilizationReport' request.
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

            http_options = _BaseVmMigrationRestTransport._BaseDeleteUtilizationReport._get_http_options()
            request, metadata = self._interceptor.pre_delete_utilization_report(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseDeleteUtilizationReport,
                    "_BaseDeleteUtilizationReport__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.DeleteUtilizationReport",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "DeleteUtilizationReport",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._DeleteUtilizationReport._get_response(
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

            resp = self._interceptor.post_delete_utilization_report(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_utilization_report_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.delete_utilization_report",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "DeleteUtilizationReport",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ExtendMigration(
        _BaseVmMigrationRestTransport._BaseExtendMigration, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.ExtendMigration")

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
            request: vmmigration.ExtendMigrationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the extend migration method over HTTP.

            Args:
                request (~.vmmigration.ExtendMigrationRequest):
                    The request object. Request message for
                'ExtendMigrationRequest' request.
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
                _BaseVmMigrationRestTransport._BaseExtendMigration._get_http_options()
            )
            request, metadata = self._interceptor.pre_extend_migration(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseExtendMigration,
                    "_BaseExtendMigration__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.ExtendMigration",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "ExtendMigration",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._ExtendMigration._get_response(
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

            resp = self._interceptor.post_extend_migration(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_extend_migration_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.extend_migration",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "ExtendMigration",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchInventory(
        _BaseVmMigrationRestTransport._BaseFetchInventory, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.FetchInventory")

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
            request: vmmigration.FetchInventoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmmigration.FetchInventoryResponse:
            r"""Call the fetch inventory method over HTTP.

            Args:
                request (~.vmmigration.FetchInventoryRequest):
                    The request object. Request message for
                [fetchInventory][google.cloud.vmmigration.v1.VmMigration.FetchInventory].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmmigration.FetchInventoryResponse:
                    Response message for
                [fetchInventory][google.cloud.vmmigration.v1.VmMigration.FetchInventory].

            """

            http_options = (
                _BaseVmMigrationRestTransport._BaseFetchInventory._get_http_options()
            )
            request, metadata = self._interceptor.pre_fetch_inventory(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseFetchInventory,
                    "_BaseFetchInventory__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.FetchInventory",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "FetchInventory",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._FetchInventory._get_response(
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
            resp = vmmigration.FetchInventoryResponse()
            pb_resp = vmmigration.FetchInventoryResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_inventory(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fetch_inventory_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmmigration.FetchInventoryResponse.to_json(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.fetch_inventory",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "FetchInventory",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchStorageInventory(
        _BaseVmMigrationRestTransport._BaseFetchStorageInventory, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.FetchStorageInventory")

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
            request: vmmigration.FetchStorageInventoryRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmmigration.FetchStorageInventoryResponse:
            r"""Call the fetch storage inventory method over HTTP.

            Args:
                request (~.vmmigration.FetchStorageInventoryRequest):
                    The request object. Request message for
                [fetchStorageInventory][google.cloud.vmmigration.v1.VmMigration.FetchStorageInventory].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmmigration.FetchStorageInventoryResponse:
                    Response message for
                [fetchStorageInventory][google.cloud.vmmigration.v1.VmMigration.FetchStorageInventory].

            """

            http_options = _BaseVmMigrationRestTransport._BaseFetchStorageInventory._get_http_options()
            request, metadata = self._interceptor.pre_fetch_storage_inventory(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseFetchStorageInventory,
                    "_BaseFetchStorageInventory__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.FetchStorageInventory",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "FetchStorageInventory",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._FetchStorageInventory._get_response(
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
            resp = vmmigration.FetchStorageInventoryResponse()
            pb_resp = vmmigration.FetchStorageInventoryResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_storage_inventory(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fetch_storage_inventory_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        vmmigration.FetchStorageInventoryResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.fetch_storage_inventory",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "FetchStorageInventory",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FinalizeMigration(
        _BaseVmMigrationRestTransport._BaseFinalizeMigration, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.FinalizeMigration")

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
            request: vmmigration.FinalizeMigrationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the finalize migration method over HTTP.

            Args:
                request (~.vmmigration.FinalizeMigrationRequest):
                    The request object. Request message for
                'FinalizeMigration' request.
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
                _BaseVmMigrationRestTransport._BaseFinalizeMigration._get_http_options()
            )
            request, metadata = self._interceptor.pre_finalize_migration(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseFinalizeMigration,
                    "_BaseFinalizeMigration__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.FinalizeMigration",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "FinalizeMigration",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._FinalizeMigration._get_response(
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

            resp = self._interceptor.post_finalize_migration(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_finalize_migration_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.finalize_migration",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "FinalizeMigration",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetCloneJob(
        _BaseVmMigrationRestTransport._BaseGetCloneJob, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.GetCloneJob")

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
            request: vmmigration.GetCloneJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmmigration.CloneJob:
            r"""Call the get clone job method over HTTP.

            Args:
                request (~.vmmigration.GetCloneJobRequest):
                    The request object. Request message for 'GetCloneJob'
                request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmmigration.CloneJob:
                    CloneJob describes the process of creating a clone of a
                [MigratingVM][google.cloud.vmmigration.v1.MigratingVm]
                to the requested target based on the latest successful
                uploaded snapshots. While the migration cycles of a
                MigratingVm take place, it is possible to verify the
                uploaded VM can be started in the cloud, by creating a
                clone. The clone can be created without any downtime,
                and it is created using the latest snapshots which are
                already in the cloud. The cloneJob is only responsible
                for its work, not its products, which means once it is
                finished, it will never touch the instance it created.
                It will only delete it in case of the CloneJob being
                cancelled or upon failure to clone.

            """

            http_options = (
                _BaseVmMigrationRestTransport._BaseGetCloneJob._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_clone_job(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseGetCloneJob,
                    "_BaseGetCloneJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.GetCloneJob",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "GetCloneJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._GetCloneJob._get_response(
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
            resp = vmmigration.CloneJob()
            pb_resp = vmmigration.CloneJob.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_clone_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_clone_job_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmmigration.CloneJob.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.get_clone_job",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "GetCloneJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetCutoverJob(
        _BaseVmMigrationRestTransport._BaseGetCutoverJob, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.GetCutoverJob")

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
            request: vmmigration.GetCutoverJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmmigration.CutoverJob:
            r"""Call the get cutover job method over HTTP.

            Args:
                request (~.vmmigration.GetCutoverJobRequest):
                    The request object. Request message for 'GetCutoverJob'
                request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmmigration.CutoverJob:
                    CutoverJob message describes a
                cutover of a migrating VM. The
                CutoverJob is the operation of shutting
                down the VM, creating a snapshot and
                cloning the VM using the replicated
                snapshot.

            """

            http_options = (
                _BaseVmMigrationRestTransport._BaseGetCutoverJob._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_cutover_job(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseGetCutoverJob,
                    "_BaseGetCutoverJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.GetCutoverJob",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "GetCutoverJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._GetCutoverJob._get_response(
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
            resp = vmmigration.CutoverJob()
            pb_resp = vmmigration.CutoverJob.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_cutover_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_cutover_job_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmmigration.CutoverJob.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.get_cutover_job",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "GetCutoverJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDatacenterConnector(
        _BaseVmMigrationRestTransport._BaseGetDatacenterConnector, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.GetDatacenterConnector")

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
            request: vmmigration.GetDatacenterConnectorRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmmigration.DatacenterConnector:
            r"""Call the get datacenter connector method over HTTP.

            Args:
                request (~.vmmigration.GetDatacenterConnectorRequest):
                    The request object. Request message for
                'GetDatacenterConnector' request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmmigration.DatacenterConnector:
                    DatacenterConnector message describes
                a connector between the Source and
                Google Cloud, which is installed on a
                vmware datacenter (an OVA vm installed
                by the user) to connect the Datacenter
                to Google Cloud and support vm migration
                data transfer.

            """

            http_options = _BaseVmMigrationRestTransport._BaseGetDatacenterConnector._get_http_options()
            request, metadata = self._interceptor.pre_get_datacenter_connector(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseGetDatacenterConnector,
                    "_BaseGetDatacenterConnector__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.GetDatacenterConnector",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "GetDatacenterConnector",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._GetDatacenterConnector._get_response(
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
            resp = vmmigration.DatacenterConnector()
            pb_resp = vmmigration.DatacenterConnector.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_datacenter_connector(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_datacenter_connector_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmmigration.DatacenterConnector.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.get_datacenter_connector",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "GetDatacenterConnector",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDiskMigrationJob(
        _BaseVmMigrationRestTransport._BaseGetDiskMigrationJob, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.GetDiskMigrationJob")

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
            request: vmmigration.GetDiskMigrationJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmmigration.DiskMigrationJob:
            r"""Call the get disk migration job method over HTTP.

            Args:
                request (~.vmmigration.GetDiskMigrationJobRequest):
                    The request object. Request message for
                'GetDiskMigrationJob' request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmmigration.DiskMigrationJob:
                    Describes the disk which will be
                migrated from the source environment.
                The source disk has to be unattached.

            """

            http_options = _BaseVmMigrationRestTransport._BaseGetDiskMigrationJob._get_http_options()
            request, metadata = self._interceptor.pre_get_disk_migration_job(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseGetDiskMigrationJob,
                    "_BaseGetDiskMigrationJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.GetDiskMigrationJob",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "GetDiskMigrationJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._GetDiskMigrationJob._get_response(
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
            resp = vmmigration.DiskMigrationJob()
            pb_resp = vmmigration.DiskMigrationJob.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_disk_migration_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_disk_migration_job_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmmigration.DiskMigrationJob.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.get_disk_migration_job",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "GetDiskMigrationJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetGroup(_BaseVmMigrationRestTransport._BaseGetGroup, VmMigrationRestStub):
        def __hash__(self):
            return hash("VmMigrationRestTransport.GetGroup")

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
            request: vmmigration.GetGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmmigration.Group:
            r"""Call the get group method over HTTP.

            Args:
                request (~.vmmigration.GetGroupRequest):
                    The request object. Request message for 'GetGroup'
                request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmmigration.Group:
                    Describes message for 'Group'
                resource. The Group is a collections of
                several MigratingVms.

            """

            http_options = (
                _BaseVmMigrationRestTransport._BaseGetGroup._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_group(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseGetGroup,
                    "_BaseGetGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.GetGroup",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "GetGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._GetGroup._get_response(
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
            resp = vmmigration.Group()
            pb_resp = vmmigration.Group.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_group_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmmigration.Group.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.get_group",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "GetGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetImageImport(
        _BaseVmMigrationRestTransport._BaseGetImageImport, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.GetImageImport")

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
            request: vmmigration.GetImageImportRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmmigration.ImageImport:
            r"""Call the get image import method over HTTP.

            Args:
                request (~.vmmigration.GetImageImportRequest):
                    The request object. Request message for 'GetImageImport'
                call.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmmigration.ImageImport:
                    ImageImport describes the
                configuration of the image import to
                run.

            """

            http_options = (
                _BaseVmMigrationRestTransport._BaseGetImageImport._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_image_import(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseGetImageImport,
                    "_BaseGetImageImport__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.GetImageImport",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "GetImageImport",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._GetImageImport._get_response(
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
            resp = vmmigration.ImageImport()
            pb_resp = vmmigration.ImageImport.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_image_import(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_image_import_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmmigration.ImageImport.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.get_image_import",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "GetImageImport",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetImageImportJob(
        _BaseVmMigrationRestTransport._BaseGetImageImportJob, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.GetImageImportJob")

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
            request: vmmigration.GetImageImportJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmmigration.ImageImportJob:
            r"""Call the get image import job method over HTTP.

            Args:
                request (~.vmmigration.GetImageImportJobRequest):
                    The request object. Request message for
                'GetImageImportJob' call.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmmigration.ImageImportJob:
                    ImageImportJob describes the progress
                and result of an image import.

            """

            http_options = (
                _BaseVmMigrationRestTransport._BaseGetImageImportJob._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_image_import_job(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseGetImageImportJob,
                    "_BaseGetImageImportJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.GetImageImportJob",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "GetImageImportJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._GetImageImportJob._get_response(
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
            resp = vmmigration.ImageImportJob()
            pb_resp = vmmigration.ImageImportJob.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_image_import_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_image_import_job_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmmigration.ImageImportJob.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.get_image_import_job",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "GetImageImportJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetMigratingVm(
        _BaseVmMigrationRestTransport._BaseGetMigratingVm, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.GetMigratingVm")

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
            request: vmmigration.GetMigratingVmRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmmigration.MigratingVm:
            r"""Call the get migrating vm method over HTTP.

            Args:
                request (~.vmmigration.GetMigratingVmRequest):
                    The request object. Request message for 'GetMigratingVm'
                request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmmigration.MigratingVm:
                    MigratingVm describes the VM that
                will be migrated from a Source
                environment and its replication state.

            """

            http_options = (
                _BaseVmMigrationRestTransport._BaseGetMigratingVm._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_migrating_vm(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseGetMigratingVm,
                    "_BaseGetMigratingVm__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.GetMigratingVm",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "GetMigratingVm",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._GetMigratingVm._get_response(
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
            resp = vmmigration.MigratingVm()
            pb_resp = vmmigration.MigratingVm.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_migrating_vm(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_migrating_vm_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmmigration.MigratingVm.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.get_migrating_vm",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "GetMigratingVm",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetReplicationCycle(
        _BaseVmMigrationRestTransport._BaseGetReplicationCycle, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.GetReplicationCycle")

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
            request: vmmigration.GetReplicationCycleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmmigration.ReplicationCycle:
            r"""Call the get replication cycle method over HTTP.

            Args:
                request (~.vmmigration.GetReplicationCycleRequest):
                    The request object. Request message for
                'GetReplicationCycle' request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmmigration.ReplicationCycle:
                    ReplicationCycle contains information
                about the current replication cycle
                status.

            """

            http_options = _BaseVmMigrationRestTransport._BaseGetReplicationCycle._get_http_options()
            request, metadata = self._interceptor.pre_get_replication_cycle(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseGetReplicationCycle,
                    "_BaseGetReplicationCycle__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.GetReplicationCycle",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "GetReplicationCycle",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._GetReplicationCycle._get_response(
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
            resp = vmmigration.ReplicationCycle()
            pb_resp = vmmigration.ReplicationCycle.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_replication_cycle(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_replication_cycle_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmmigration.ReplicationCycle.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.get_replication_cycle",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "GetReplicationCycle",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSource(_BaseVmMigrationRestTransport._BaseGetSource, VmMigrationRestStub):
        def __hash__(self):
            return hash("VmMigrationRestTransport.GetSource")

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
            request: vmmigration.GetSourceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmmigration.Source:
            r"""Call the get source method over HTTP.

            Args:
                request (~.vmmigration.GetSourceRequest):
                    The request object. Request message for 'GetSource'
                request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmmigration.Source:
                    Source message describes a specific
                vm migration Source resource. It
                contains the source environment
                information.

            """

            http_options = (
                _BaseVmMigrationRestTransport._BaseGetSource._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_source(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseGetSource,
                    "_BaseGetSource__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.GetSource",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "GetSource",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._GetSource._get_response(
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
            resp = vmmigration.Source()
            pb_resp = vmmigration.Source.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_source(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_source_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmmigration.Source.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.get_source",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "GetSource",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetTargetProject(
        _BaseVmMigrationRestTransport._BaseGetTargetProject, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.GetTargetProject")

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
            request: vmmigration.GetTargetProjectRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmmigration.TargetProject:
            r"""Call the get target project method over HTTP.

            Args:
                request (~.vmmigration.GetTargetProjectRequest):
                    The request object. Request message for
                'GetTargetProject' call.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmmigration.TargetProject:
                    TargetProject message represents a
                target Compute Engine project for a
                migration or a clone.

            """

            http_options = (
                _BaseVmMigrationRestTransport._BaseGetTargetProject._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_target_project(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseGetTargetProject,
                    "_BaseGetTargetProject__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.GetTargetProject",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "GetTargetProject",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._GetTargetProject._get_response(
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
            resp = vmmigration.TargetProject()
            pb_resp = vmmigration.TargetProject.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_target_project(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_target_project_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmmigration.TargetProject.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.get_target_project",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "GetTargetProject",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetUtilizationReport(
        _BaseVmMigrationRestTransport._BaseGetUtilizationReport, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.GetUtilizationReport")

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
            request: vmmigration.GetUtilizationReportRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmmigration.UtilizationReport:
            r"""Call the get utilization report method over HTTP.

            Args:
                request (~.vmmigration.GetUtilizationReportRequest):
                    The request object. Request message for
                'GetUtilizationReport' request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmmigration.UtilizationReport:
                    Utilization report details the
                utilization (CPU, memory, etc.) of
                selected source VMs.

            """

            http_options = _BaseVmMigrationRestTransport._BaseGetUtilizationReport._get_http_options()
            request, metadata = self._interceptor.pre_get_utilization_report(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseGetUtilizationReport,
                    "_BaseGetUtilizationReport__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.GetUtilizationReport",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "GetUtilizationReport",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._GetUtilizationReport._get_response(
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
            resp = vmmigration.UtilizationReport()
            pb_resp = vmmigration.UtilizationReport.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_utilization_report(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_utilization_report_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmmigration.UtilizationReport.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.get_utilization_report",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "GetUtilizationReport",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListCloneJobs(
        _BaseVmMigrationRestTransport._BaseListCloneJobs, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.ListCloneJobs")

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
            request: vmmigration.ListCloneJobsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmmigration.ListCloneJobsResponse:
            r"""Call the list clone jobs method over HTTP.

            Args:
                request (~.vmmigration.ListCloneJobsRequest):
                    The request object. Request message for
                'ListCloneJobsRequest' request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmmigration.ListCloneJobsResponse:
                    Response message for 'ListCloneJobs'
                request.

            """

            http_options = (
                _BaseVmMigrationRestTransport._BaseListCloneJobs._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_clone_jobs(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseListCloneJobs,
                    "_BaseListCloneJobs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.ListCloneJobs",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "ListCloneJobs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._ListCloneJobs._get_response(
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
            resp = vmmigration.ListCloneJobsResponse()
            pb_resp = vmmigration.ListCloneJobsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_clone_jobs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_clone_jobs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmmigration.ListCloneJobsResponse.to_json(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.list_clone_jobs",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "ListCloneJobs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListCutoverJobs(
        _BaseVmMigrationRestTransport._BaseListCutoverJobs, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.ListCutoverJobs")

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
            request: vmmigration.ListCutoverJobsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmmigration.ListCutoverJobsResponse:
            r"""Call the list cutover jobs method over HTTP.

            Args:
                request (~.vmmigration.ListCutoverJobsRequest):
                    The request object. Request message for
                'ListCutoverJobsRequest' request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmmigration.ListCutoverJobsResponse:
                    Response message for
                'ListCutoverJobs' request.

            """

            http_options = (
                _BaseVmMigrationRestTransport._BaseListCutoverJobs._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_cutover_jobs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseListCutoverJobs,
                    "_BaseListCutoverJobs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.ListCutoverJobs",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "ListCutoverJobs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._ListCutoverJobs._get_response(
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
            resp = vmmigration.ListCutoverJobsResponse()
            pb_resp = vmmigration.ListCutoverJobsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_cutover_jobs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_cutover_jobs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmmigration.ListCutoverJobsResponse.to_json(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.list_cutover_jobs",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "ListCutoverJobs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDatacenterConnectors(
        _BaseVmMigrationRestTransport._BaseListDatacenterConnectors, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.ListDatacenterConnectors")

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
            request: vmmigration.ListDatacenterConnectorsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmmigration.ListDatacenterConnectorsResponse:
            r"""Call the list datacenter
            connectors method over HTTP.

                Args:
                    request (~.vmmigration.ListDatacenterConnectorsRequest):
                        The request object. Request message for
                    'ListDatacenterConnectors' request.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.vmmigration.ListDatacenterConnectorsResponse:
                        Response message for
                    'ListDatacenterConnectors' request.

            """

            http_options = _BaseVmMigrationRestTransport._BaseListDatacenterConnectors._get_http_options()
            request, metadata = self._interceptor.pre_list_datacenter_connectors(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseListDatacenterConnectors,
                    "_BaseListDatacenterConnectors__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.ListDatacenterConnectors",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "ListDatacenterConnectors",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._ListDatacenterConnectors._get_response(
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
            resp = vmmigration.ListDatacenterConnectorsResponse()
            pb_resp = vmmigration.ListDatacenterConnectorsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_datacenter_connectors(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_datacenter_connectors_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        vmmigration.ListDatacenterConnectorsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.list_datacenter_connectors",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "ListDatacenterConnectors",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDiskMigrationJobs(
        _BaseVmMigrationRestTransport._BaseListDiskMigrationJobs, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.ListDiskMigrationJobs")

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
            request: vmmigration.ListDiskMigrationJobsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmmigration.ListDiskMigrationJobsResponse:
            r"""Call the list disk migration jobs method over HTTP.

            Args:
                request (~.vmmigration.ListDiskMigrationJobsRequest):
                    The request object. Request message for
                'ListDiskMigrationJobsRequest' request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmmigration.ListDiskMigrationJobsResponse:
                    Response message for
                'ListDiskMigrationJobs' request.

            """

            http_options = _BaseVmMigrationRestTransport._BaseListDiskMigrationJobs._get_http_options()
            request, metadata = self._interceptor.pre_list_disk_migration_jobs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseListDiskMigrationJobs,
                    "_BaseListDiskMigrationJobs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.ListDiskMigrationJobs",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "ListDiskMigrationJobs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._ListDiskMigrationJobs._get_response(
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
            resp = vmmigration.ListDiskMigrationJobsResponse()
            pb_resp = vmmigration.ListDiskMigrationJobsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_disk_migration_jobs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_disk_migration_jobs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        vmmigration.ListDiskMigrationJobsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.list_disk_migration_jobs",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "ListDiskMigrationJobs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListGroups(
        _BaseVmMigrationRestTransport._BaseListGroups, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.ListGroups")

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
            request: vmmigration.ListGroupsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmmigration.ListGroupsResponse:
            r"""Call the list groups method over HTTP.

            Args:
                request (~.vmmigration.ListGroupsRequest):
                    The request object. Request message for 'ListGroups'
                request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmmigration.ListGroupsResponse:
                    Response message for 'ListGroups'
                request.

            """

            http_options = (
                _BaseVmMigrationRestTransport._BaseListGroups._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_groups(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseListGroups,
                    "_BaseListGroups__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.ListGroups",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "ListGroups",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._ListGroups._get_response(
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
            resp = vmmigration.ListGroupsResponse()
            pb_resp = vmmigration.ListGroupsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_groups(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_groups_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmmigration.ListGroupsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.list_groups",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "ListGroups",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListImageImportJobs(
        _BaseVmMigrationRestTransport._BaseListImageImportJobs, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.ListImageImportJobs")

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
            request: vmmigration.ListImageImportJobsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmmigration.ListImageImportJobsResponse:
            r"""Call the list image import jobs method over HTTP.

            Args:
                request (~.vmmigration.ListImageImportJobsRequest):
                    The request object. Request message for
                'ListImageImportJobs' call.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmmigration.ListImageImportJobsResponse:
                    Response message for
                'ListImageImportJobs' call.

            """

            http_options = _BaseVmMigrationRestTransport._BaseListImageImportJobs._get_http_options()
            request, metadata = self._interceptor.pre_list_image_import_jobs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseListImageImportJobs,
                    "_BaseListImageImportJobs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.ListImageImportJobs",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "ListImageImportJobs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._ListImageImportJobs._get_response(
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
            resp = vmmigration.ListImageImportJobsResponse()
            pb_resp = vmmigration.ListImageImportJobsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_image_import_jobs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_image_import_jobs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmmigration.ListImageImportJobsResponse.to_json(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.list_image_import_jobs",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "ListImageImportJobs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListImageImports(
        _BaseVmMigrationRestTransport._BaseListImageImports, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.ListImageImports")

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
            request: vmmigration.ListImageImportsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmmigration.ListImageImportsResponse:
            r"""Call the list image imports method over HTTP.

            Args:
                request (~.vmmigration.ListImageImportsRequest):
                    The request object. Request message for
                'ListImageImports' call.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmmigration.ListImageImportsResponse:
                    Response message for
                'ListImageImports' call.

            """

            http_options = (
                _BaseVmMigrationRestTransport._BaseListImageImports._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_image_imports(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseListImageImports,
                    "_BaseListImageImports__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.ListImageImports",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "ListImageImports",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._ListImageImports._get_response(
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
            resp = vmmigration.ListImageImportsResponse()
            pb_resp = vmmigration.ListImageImportsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_image_imports(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_image_imports_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmmigration.ListImageImportsResponse.to_json(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.list_image_imports",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "ListImageImports",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListMigratingVms(
        _BaseVmMigrationRestTransport._BaseListMigratingVms, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.ListMigratingVms")

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
            request: vmmigration.ListMigratingVmsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmmigration.ListMigratingVmsResponse:
            r"""Call the list migrating vms method over HTTP.

            Args:
                request (~.vmmigration.ListMigratingVmsRequest):
                    The request object. Request message for
                'LisMigratingVmsRequest' request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmmigration.ListMigratingVmsResponse:
                    Response message for
                'ListMigratingVms' request.

            """

            http_options = (
                _BaseVmMigrationRestTransport._BaseListMigratingVms._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_migrating_vms(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseListMigratingVms,
                    "_BaseListMigratingVms__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.ListMigratingVms",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "ListMigratingVms",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._ListMigratingVms._get_response(
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
            resp = vmmigration.ListMigratingVmsResponse()
            pb_resp = vmmigration.ListMigratingVmsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_migrating_vms(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_migrating_vms_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmmigration.ListMigratingVmsResponse.to_json(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.list_migrating_vms",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "ListMigratingVms",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListReplicationCycles(
        _BaseVmMigrationRestTransport._BaseListReplicationCycles, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.ListReplicationCycles")

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
            request: vmmigration.ListReplicationCyclesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmmigration.ListReplicationCyclesResponse:
            r"""Call the list replication cycles method over HTTP.

            Args:
                request (~.vmmigration.ListReplicationCyclesRequest):
                    The request object. Request message for
                'LisReplicationCyclesRequest' request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmmigration.ListReplicationCyclesResponse:
                    Response message for
                'ListReplicationCycles' request.

            """

            http_options = _BaseVmMigrationRestTransport._BaseListReplicationCycles._get_http_options()
            request, metadata = self._interceptor.pre_list_replication_cycles(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseListReplicationCycles,
                    "_BaseListReplicationCycles__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.ListReplicationCycles",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "ListReplicationCycles",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._ListReplicationCycles._get_response(
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
            resp = vmmigration.ListReplicationCyclesResponse()
            pb_resp = vmmigration.ListReplicationCyclesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_replication_cycles(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_replication_cycles_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        vmmigration.ListReplicationCyclesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.list_replication_cycles",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "ListReplicationCycles",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSources(
        _BaseVmMigrationRestTransport._BaseListSources, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.ListSources")

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
            request: vmmigration.ListSourcesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmmigration.ListSourcesResponse:
            r"""Call the list sources method over HTTP.

            Args:
                request (~.vmmigration.ListSourcesRequest):
                    The request object. Request message for 'ListSources'
                request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmmigration.ListSourcesResponse:
                    Response message for 'ListSources'
                request.

            """

            http_options = (
                _BaseVmMigrationRestTransport._BaseListSources._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_sources(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseListSources,
                    "_BaseListSources__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.ListSources",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "ListSources",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._ListSources._get_response(
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
            resp = vmmigration.ListSourcesResponse()
            pb_resp = vmmigration.ListSourcesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_sources(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_sources_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmmigration.ListSourcesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.list_sources",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "ListSources",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListTargetProjects(
        _BaseVmMigrationRestTransport._BaseListTargetProjects, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.ListTargetProjects")

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
            request: vmmigration.ListTargetProjectsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmmigration.ListTargetProjectsResponse:
            r"""Call the list target projects method over HTTP.

            Args:
                request (~.vmmigration.ListTargetProjectsRequest):
                    The request object. Request message for
                'ListTargetProjects' call.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmmigration.ListTargetProjectsResponse:
                    Response message for
                'ListTargetProjects' call.

            """

            http_options = _BaseVmMigrationRestTransport._BaseListTargetProjects._get_http_options()
            request, metadata = self._interceptor.pre_list_target_projects(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseListTargetProjects,
                    "_BaseListTargetProjects__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.ListTargetProjects",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "ListTargetProjects",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._ListTargetProjects._get_response(
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
            resp = vmmigration.ListTargetProjectsResponse()
            pb_resp = vmmigration.ListTargetProjectsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_target_projects(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_target_projects_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = vmmigration.ListTargetProjectsResponse.to_json(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.list_target_projects",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "ListTargetProjects",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListUtilizationReports(
        _BaseVmMigrationRestTransport._BaseListUtilizationReports, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.ListUtilizationReports")

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
            request: vmmigration.ListUtilizationReportsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> vmmigration.ListUtilizationReportsResponse:
            r"""Call the list utilization reports method over HTTP.

            Args:
                request (~.vmmigration.ListUtilizationReportsRequest):
                    The request object. Request message for
                'ListUtilizationReports' request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.vmmigration.ListUtilizationReportsResponse:
                    Response message for
                'ListUtilizationReports' request.

            """

            http_options = _BaseVmMigrationRestTransport._BaseListUtilizationReports._get_http_options()
            request, metadata = self._interceptor.pre_list_utilization_reports(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseListUtilizationReports,
                    "_BaseListUtilizationReports__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.ListUtilizationReports",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "ListUtilizationReports",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._ListUtilizationReports._get_response(
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
            resp = vmmigration.ListUtilizationReportsResponse()
            pb_resp = vmmigration.ListUtilizationReportsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_utilization_reports(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_utilization_reports_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        vmmigration.ListUtilizationReportsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.list_utilization_reports",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "ListUtilizationReports",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _PauseMigration(
        _BaseVmMigrationRestTransport._BasePauseMigration, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.PauseMigration")

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
            request: vmmigration.PauseMigrationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the pause migration method over HTTP.

            Args:
                request (~.vmmigration.PauseMigrationRequest):
                    The request object. Request message for 'PauseMigration'
                request.
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
                _BaseVmMigrationRestTransport._BasePauseMigration._get_http_options()
            )
            request, metadata = self._interceptor.pre_pause_migration(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BasePauseMigration,
                    "_BasePauseMigration__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.PauseMigration",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "PauseMigration",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._PauseMigration._get_response(
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

            resp = self._interceptor.post_pause_migration(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_pause_migration_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.pause_migration",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "PauseMigration",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RemoveGroupMigration(
        _BaseVmMigrationRestTransport._BaseRemoveGroupMigration, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.RemoveGroupMigration")

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
            request: vmmigration.RemoveGroupMigrationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the remove group migration method over HTTP.

            Args:
                request (~.vmmigration.RemoveGroupMigrationRequest):
                    The request object. Request message for 'RemoveMigration'
                request.
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

            http_options = _BaseVmMigrationRestTransport._BaseRemoveGroupMigration._get_http_options()
            request, metadata = self._interceptor.pre_remove_group_migration(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseRemoveGroupMigration,
                    "_BaseRemoveGroupMigration__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.RemoveGroupMigration",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "RemoveGroupMigration",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._RemoveGroupMigration._get_response(
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

            resp = self._interceptor.post_remove_group_migration(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_remove_group_migration_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.remove_group_migration",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "RemoveGroupMigration",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ResumeMigration(
        _BaseVmMigrationRestTransport._BaseResumeMigration, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.ResumeMigration")

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
            request: vmmigration.ResumeMigrationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the resume migration method over HTTP.

            Args:
                request (~.vmmigration.ResumeMigrationRequest):
                    The request object. Request message for 'ResumeMigration'
                request.
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
                _BaseVmMigrationRestTransport._BaseResumeMigration._get_http_options()
            )
            request, metadata = self._interceptor.pre_resume_migration(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseResumeMigration,
                    "_BaseResumeMigration__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.ResumeMigration",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "ResumeMigration",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._ResumeMigration._get_response(
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

            resp = self._interceptor.post_resume_migration(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_resume_migration_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.resume_migration",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "ResumeMigration",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RunDiskMigrationJob(
        _BaseVmMigrationRestTransport._BaseRunDiskMigrationJob, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.RunDiskMigrationJob")

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
            request: vmmigration.RunDiskMigrationJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the run disk migration job method over HTTP.

            Args:
                request (~.vmmigration.RunDiskMigrationJobRequest):
                    The request object. Request message for
                'RunDiskMigrationJobRequest' request.
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

            http_options = _BaseVmMigrationRestTransport._BaseRunDiskMigrationJob._get_http_options()
            request, metadata = self._interceptor.pre_run_disk_migration_job(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseRunDiskMigrationJob,
                    "_BaseRunDiskMigrationJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.RunDiskMigrationJob",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "RunDiskMigrationJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._RunDiskMigrationJob._get_response(
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

            resp = self._interceptor.post_run_disk_migration_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_run_disk_migration_job_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.run_disk_migration_job",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "RunDiskMigrationJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _StartMigration(
        _BaseVmMigrationRestTransport._BaseStartMigration, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.StartMigration")

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
            request: vmmigration.StartMigrationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the start migration method over HTTP.

            Args:
                request (~.vmmigration.StartMigrationRequest):
                    The request object. Request message for
                'StartMigrationRequest' request.
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
                _BaseVmMigrationRestTransport._BaseStartMigration._get_http_options()
            )
            request, metadata = self._interceptor.pre_start_migration(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseStartMigration,
                    "_BaseStartMigration__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.StartMigration",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "StartMigration",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._StartMigration._get_response(
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

            resp = self._interceptor.post_start_migration(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_start_migration_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.start_migration",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "StartMigration",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDiskMigrationJob(
        _BaseVmMigrationRestTransport._BaseUpdateDiskMigrationJob, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.UpdateDiskMigrationJob")

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
            request: vmmigration.UpdateDiskMigrationJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update disk migration job method over HTTP.

            Args:
                request (~.vmmigration.UpdateDiskMigrationJobRequest):
                    The request object. Request message for
                'UpdateDiskMigrationJob' request.
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

            http_options = _BaseVmMigrationRestTransport._BaseUpdateDiskMigrationJob._get_http_options()
            request, metadata = self._interceptor.pre_update_disk_migration_job(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseUpdateDiskMigrationJob,
                    "_BaseUpdateDiskMigrationJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.UpdateDiskMigrationJob",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "UpdateDiskMigrationJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._UpdateDiskMigrationJob._get_response(
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

            resp = self._interceptor.post_update_disk_migration_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_disk_migration_job_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.update_disk_migration_job",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "UpdateDiskMigrationJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateGroup(
        _BaseVmMigrationRestTransport._BaseUpdateGroup, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.UpdateGroup")

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
            request: vmmigration.UpdateGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update group method over HTTP.

            Args:
                request (~.vmmigration.UpdateGroupRequest):
                    The request object. Update message for 'UpdateGroups'
                request.
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
                _BaseVmMigrationRestTransport._BaseUpdateGroup._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_group(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseUpdateGroup,
                    "_BaseUpdateGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.UpdateGroup",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "UpdateGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._UpdateGroup._get_response(
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

            resp = self._interceptor.post_update_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_group_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.update_group",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "UpdateGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateMigratingVm(
        _BaseVmMigrationRestTransport._BaseUpdateMigratingVm, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.UpdateMigratingVm")

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
            request: vmmigration.UpdateMigratingVmRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update migrating vm method over HTTP.

            Args:
                request (~.vmmigration.UpdateMigratingVmRequest):
                    The request object. Request message for
                'UpdateMigratingVm' request.
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
                _BaseVmMigrationRestTransport._BaseUpdateMigratingVm._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_migrating_vm(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseUpdateMigratingVm,
                    "_BaseUpdateMigratingVm__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.UpdateMigratingVm",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "UpdateMigratingVm",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._UpdateMigratingVm._get_response(
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

            resp = self._interceptor.post_update_migrating_vm(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_migrating_vm_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.update_migrating_vm",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "UpdateMigratingVm",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateSource(
        _BaseVmMigrationRestTransport._BaseUpdateSource, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.UpdateSource")

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
            request: vmmigration.UpdateSourceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update source method over HTTP.

            Args:
                request (~.vmmigration.UpdateSourceRequest):
                    The request object. Update message for 'UpdateSources'
                request.
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
                _BaseVmMigrationRestTransport._BaseUpdateSource._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_source(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseUpdateSource,
                    "_BaseUpdateSource__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.UpdateSource",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "UpdateSource",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._UpdateSource._get_response(
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

            resp = self._interceptor.post_update_source(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_source_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.update_source",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "UpdateSource",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateTargetProject(
        _BaseVmMigrationRestTransport._BaseUpdateTargetProject, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.UpdateTargetProject")

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
            request: vmmigration.UpdateTargetProjectRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update target project method over HTTP.

            Args:
                request (~.vmmigration.UpdateTargetProjectRequest):
                    The request object. Update message for
                'UpdateTargetProject' request.
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

            http_options = _BaseVmMigrationRestTransport._BaseUpdateTargetProject._get_http_options()
            request, metadata = self._interceptor.pre_update_target_project(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseUpdateTargetProject,
                    "_BaseUpdateTargetProject__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.UpdateTargetProject",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "UpdateTargetProject",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._UpdateTargetProject._get_response(
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

            resp = self._interceptor.post_update_target_project(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_target_project_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.update_target_project",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "UpdateTargetProject",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpgradeAppliance(
        _BaseVmMigrationRestTransport._BaseUpgradeAppliance, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.UpgradeAppliance")

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
            request: vmmigration.UpgradeApplianceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the upgrade appliance method over HTTP.

            Args:
                request (~.vmmigration.UpgradeApplianceRequest):
                    The request object. Request message for
                'UpgradeAppliance' request.
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
                _BaseVmMigrationRestTransport._BaseUpgradeAppliance._get_http_options()
            )
            request, metadata = self._interceptor.pre_upgrade_appliance(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseUpgradeAppliance,
                    "_BaseUpgradeAppliance__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.UpgradeAppliance",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "UpgradeAppliance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._UpgradeAppliance._get_response(
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

            resp = self._interceptor.post_upgrade_appliance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_upgrade_appliance_with_metadata(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationClient.upgrade_appliance",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "UpgradeAppliance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def add_group_migration(
        self,
    ) -> Callable[[vmmigration.AddGroupMigrationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AddGroupMigration(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_clone_job(
        self,
    ) -> Callable[[vmmigration.CancelCloneJobRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CancelCloneJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_cutover_job(
        self,
    ) -> Callable[[vmmigration.CancelCutoverJobRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CancelCutoverJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_disk_migration_job(
        self,
    ) -> Callable[
        [vmmigration.CancelDiskMigrationJobRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CancelDiskMigrationJob(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def cancel_image_import_job(
        self,
    ) -> Callable[[vmmigration.CancelImageImportJobRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CancelImageImportJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_clone_job(
        self,
    ) -> Callable[[vmmigration.CreateCloneJobRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateCloneJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_cutover_job(
        self,
    ) -> Callable[[vmmigration.CreateCutoverJobRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateCutoverJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_datacenter_connector(
        self,
    ) -> Callable[
        [vmmigration.CreateDatacenterConnectorRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDatacenterConnector(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_disk_migration_job(
        self,
    ) -> Callable[
        [vmmigration.CreateDiskMigrationJobRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDiskMigrationJob(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_group(
        self,
    ) -> Callable[[vmmigration.CreateGroupRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateGroup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_image_import(
        self,
    ) -> Callable[[vmmigration.CreateImageImportRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateImageImport(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_migrating_vm(
        self,
    ) -> Callable[[vmmigration.CreateMigratingVmRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateMigratingVm(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_source(
        self,
    ) -> Callable[[vmmigration.CreateSourceRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateSource(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_target_project(
        self,
    ) -> Callable[[vmmigration.CreateTargetProjectRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateTargetProject(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_utilization_report(
        self,
    ) -> Callable[
        [vmmigration.CreateUtilizationReportRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateUtilizationReport(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_datacenter_connector(
        self,
    ) -> Callable[
        [vmmigration.DeleteDatacenterConnectorRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDatacenterConnector(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_disk_migration_job(
        self,
    ) -> Callable[
        [vmmigration.DeleteDiskMigrationJobRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDiskMigrationJob(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_group(
        self,
    ) -> Callable[[vmmigration.DeleteGroupRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteGroup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_image_import(
        self,
    ) -> Callable[[vmmigration.DeleteImageImportRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteImageImport(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_migrating_vm(
        self,
    ) -> Callable[[vmmigration.DeleteMigratingVmRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteMigratingVm(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_source(
        self,
    ) -> Callable[[vmmigration.DeleteSourceRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteSource(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_target_project(
        self,
    ) -> Callable[[vmmigration.DeleteTargetProjectRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteTargetProject(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_utilization_report(
        self,
    ) -> Callable[
        [vmmigration.DeleteUtilizationReportRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteUtilizationReport(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def extend_migration(
        self,
    ) -> Callable[[vmmigration.ExtendMigrationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExtendMigration(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def fetch_inventory(
        self,
    ) -> Callable[
        [vmmigration.FetchInventoryRequest], vmmigration.FetchInventoryResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchInventory(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def fetch_storage_inventory(
        self,
    ) -> Callable[
        [vmmigration.FetchStorageInventoryRequest],
        vmmigration.FetchStorageInventoryResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchStorageInventory(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def finalize_migration(
        self,
    ) -> Callable[[vmmigration.FinalizeMigrationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FinalizeMigration(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_clone_job(
        self,
    ) -> Callable[[vmmigration.GetCloneJobRequest], vmmigration.CloneJob]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCloneJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_cutover_job(
        self,
    ) -> Callable[[vmmigration.GetCutoverJobRequest], vmmigration.CutoverJob]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCutoverJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_datacenter_connector(
        self,
    ) -> Callable[
        [vmmigration.GetDatacenterConnectorRequest], vmmigration.DatacenterConnector
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDatacenterConnector(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_disk_migration_job(
        self,
    ) -> Callable[
        [vmmigration.GetDiskMigrationJobRequest], vmmigration.DiskMigrationJob
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDiskMigrationJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_group(self) -> Callable[[vmmigration.GetGroupRequest], vmmigration.Group]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetGroup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_image_import(
        self,
    ) -> Callable[[vmmigration.GetImageImportRequest], vmmigration.ImageImport]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetImageImport(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_image_import_job(
        self,
    ) -> Callable[[vmmigration.GetImageImportJobRequest], vmmigration.ImageImportJob]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetImageImportJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_migrating_vm(
        self,
    ) -> Callable[[vmmigration.GetMigratingVmRequest], vmmigration.MigratingVm]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetMigratingVm(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_replication_cycle(
        self,
    ) -> Callable[
        [vmmigration.GetReplicationCycleRequest], vmmigration.ReplicationCycle
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetReplicationCycle(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_source(
        self,
    ) -> Callable[[vmmigration.GetSourceRequest], vmmigration.Source]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSource(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_target_project(
        self,
    ) -> Callable[[vmmigration.GetTargetProjectRequest], vmmigration.TargetProject]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTargetProject(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_utilization_report(
        self,
    ) -> Callable[
        [vmmigration.GetUtilizationReportRequest], vmmigration.UtilizationReport
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetUtilizationReport(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_clone_jobs(
        self,
    ) -> Callable[
        [vmmigration.ListCloneJobsRequest], vmmigration.ListCloneJobsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListCloneJobs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_cutover_jobs(
        self,
    ) -> Callable[
        [vmmigration.ListCutoverJobsRequest], vmmigration.ListCutoverJobsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListCutoverJobs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_datacenter_connectors(
        self,
    ) -> Callable[
        [vmmigration.ListDatacenterConnectorsRequest],
        vmmigration.ListDatacenterConnectorsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDatacenterConnectors(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_disk_migration_jobs(
        self,
    ) -> Callable[
        [vmmigration.ListDiskMigrationJobsRequest],
        vmmigration.ListDiskMigrationJobsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDiskMigrationJobs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_groups(
        self,
    ) -> Callable[[vmmigration.ListGroupsRequest], vmmigration.ListGroupsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListGroups(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_image_import_jobs(
        self,
    ) -> Callable[
        [vmmigration.ListImageImportJobsRequest],
        vmmigration.ListImageImportJobsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListImageImportJobs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_image_imports(
        self,
    ) -> Callable[
        [vmmigration.ListImageImportsRequest], vmmigration.ListImageImportsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListImageImports(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_migrating_vms(
        self,
    ) -> Callable[
        [vmmigration.ListMigratingVmsRequest], vmmigration.ListMigratingVmsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListMigratingVms(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_replication_cycles(
        self,
    ) -> Callable[
        [vmmigration.ListReplicationCyclesRequest],
        vmmigration.ListReplicationCyclesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListReplicationCycles(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_sources(
        self,
    ) -> Callable[[vmmigration.ListSourcesRequest], vmmigration.ListSourcesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSources(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_target_projects(
        self,
    ) -> Callable[
        [vmmigration.ListTargetProjectsRequest], vmmigration.ListTargetProjectsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTargetProjects(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_utilization_reports(
        self,
    ) -> Callable[
        [vmmigration.ListUtilizationReportsRequest],
        vmmigration.ListUtilizationReportsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListUtilizationReports(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def pause_migration(
        self,
    ) -> Callable[[vmmigration.PauseMigrationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PauseMigration(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def remove_group_migration(
        self,
    ) -> Callable[[vmmigration.RemoveGroupMigrationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RemoveGroupMigration(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def resume_migration(
        self,
    ) -> Callable[[vmmigration.ResumeMigrationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ResumeMigration(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def run_disk_migration_job(
        self,
    ) -> Callable[[vmmigration.RunDiskMigrationJobRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RunDiskMigrationJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def start_migration(
        self,
    ) -> Callable[[vmmigration.StartMigrationRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StartMigration(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_disk_migration_job(
        self,
    ) -> Callable[
        [vmmigration.UpdateDiskMigrationJobRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDiskMigrationJob(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_group(
        self,
    ) -> Callable[[vmmigration.UpdateGroupRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateGroup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_migrating_vm(
        self,
    ) -> Callable[[vmmigration.UpdateMigratingVmRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateMigratingVm(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_source(
        self,
    ) -> Callable[[vmmigration.UpdateSourceRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateSource(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_target_project(
        self,
    ) -> Callable[[vmmigration.UpdateTargetProjectRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateTargetProject(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def upgrade_appliance(
        self,
    ) -> Callable[[vmmigration.UpgradeApplianceRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpgradeAppliance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseVmMigrationRestTransport._BaseGetLocation, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.GetLocation")

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
                _BaseVmMigrationRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
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
        _BaseVmMigrationRestTransport._BaseListLocations, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.ListLocations")

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
                _BaseVmMigrationRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
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
        _BaseVmMigrationRestTransport._BaseCancelOperation, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.CancelOperation")

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
                _BaseVmMigrationRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._CancelOperation._get_response(
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
        _BaseVmMigrationRestTransport._BaseDeleteOperation, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.DeleteOperation")

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
                _BaseVmMigrationRestTransport._BaseDeleteOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._DeleteOperation._get_response(
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
        _BaseVmMigrationRestTransport._BaseGetOperation, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.GetOperation")

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
                _BaseVmMigrationRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
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
        _BaseVmMigrationRestTransport._BaseListOperations, VmMigrationRestStub
    ):
        def __hash__(self):
            return hash("VmMigrationRestTransport.ListOperations")

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
                _BaseVmMigrationRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseVmMigrationRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.vmmigration_v1.VmMigrationClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = VmMigrationRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.vmmigration_v1.VmMigrationAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.vmmigration.v1.VmMigration",
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


__all__ = ("VmMigrationRestTransport",)
