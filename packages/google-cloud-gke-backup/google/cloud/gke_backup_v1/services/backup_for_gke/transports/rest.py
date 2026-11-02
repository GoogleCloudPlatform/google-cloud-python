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

from google.cloud.gke_backup_v1._compat import transcode_request
from google.cloud.gke_backup_v1.types import (
    backup,
    backup_channel,
    backup_plan,
    backup_plan_binding,
    gkebackup,
    restore,
    restore_channel,
    restore_plan,
    restore_plan_binding,
    volume,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseBackupForGKERestTransport

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


class BackupForGKERestInterceptor:
    """Interceptor for BackupForGKE.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the BackupForGKERestTransport.

    .. code-block:: python
        class MyCustomBackupForGKEInterceptor(BackupForGKERestInterceptor):
            def pre_create_backup(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_backup(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_backup_channel(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_backup_channel(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_backup_plan(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_backup_plan(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_restore(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_restore(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_restore_channel(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_restore_channel(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_restore_plan(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_restore_plan(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_backup(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_backup(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_backup_channel(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_backup_channel(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_backup_plan(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_backup_plan(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_restore(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_restore(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_restore_channel(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_restore_channel(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_restore_plan(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_restore_plan(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_backup(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_backup(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_backup_channel(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_backup_channel(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_backup_index_download_url(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_backup_index_download_url(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_backup_plan(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_backup_plan(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_backup_plan_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_backup_plan_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_restore(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_restore(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_restore_channel(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_restore_channel(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_restore_plan(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_restore_plan(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_restore_plan_binding(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_restore_plan_binding(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_volume_backup(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_volume_backup(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_volume_restore(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_volume_restore(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_backup_channels(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_backup_channels(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_backup_plan_bindings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_backup_plan_bindings(self, response):
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

            def pre_list_restore_channels(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_restore_channels(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_restore_plan_bindings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_restore_plan_bindings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_restore_plans(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_restore_plans(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_restores(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_restores(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_volume_backups(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_volume_backups(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_volume_restores(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_volume_restores(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_backup(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_backup(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_backup_channel(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_backup_channel(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_backup_plan(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_backup_plan(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_restore(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_restore(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_restore_channel(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_restore_channel(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_restore_plan(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_restore_plan(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = BackupForGKERestTransport(interceptor=MyCustomBackupForGKEInterceptor())
        client = BackupForGKEClient(transport=transport)


    """

    def pre_create_backup(
        self,
        request: gkebackup.CreateBackupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gkebackup.CreateBackupRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_backup

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_create_backup(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_backup

        DEPRECATED. Please use the `post_create_backup_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
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
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_create_backup_with_metadata`
        interceptor in new development instead of the `post_create_backup` interceptor.
        When both interceptors are used, this `post_create_backup_with_metadata` interceptor runs after the
        `post_create_backup` interceptor. The (possibly modified) response returned by
        `post_create_backup` will be passed to
        `post_create_backup_with_metadata`.
        """
        return response, metadata

    def pre_create_backup_channel(
        self,
        request: gkebackup.CreateBackupChannelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.CreateBackupChannelRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_backup_channel

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_create_backup_channel(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_backup_channel

        DEPRECATED. Please use the `post_create_backup_channel_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code. This `post_create_backup_channel` interceptor runs
        before the `post_create_backup_channel_with_metadata` interceptor.
        """
        return response

    def post_create_backup_channel_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_backup_channel

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_create_backup_channel_with_metadata`
        interceptor in new development instead of the `post_create_backup_channel` interceptor.
        When both interceptors are used, this `post_create_backup_channel_with_metadata` interceptor runs after the
        `post_create_backup_channel` interceptor. The (possibly modified) response returned by
        `post_create_backup_channel` will be passed to
        `post_create_backup_channel_with_metadata`.
        """
        return response, metadata

    def pre_create_backup_plan(
        self,
        request: gkebackup.CreateBackupPlanRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.CreateBackupPlanRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_backup_plan

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_create_backup_plan(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_backup_plan

        DEPRECATED. Please use the `post_create_backup_plan_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
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
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_create_backup_plan_with_metadata`
        interceptor in new development instead of the `post_create_backup_plan` interceptor.
        When both interceptors are used, this `post_create_backup_plan_with_metadata` interceptor runs after the
        `post_create_backup_plan` interceptor. The (possibly modified) response returned by
        `post_create_backup_plan` will be passed to
        `post_create_backup_plan_with_metadata`.
        """
        return response, metadata

    def pre_create_restore(
        self,
        request: gkebackup.CreateRestoreRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gkebackup.CreateRestoreRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_restore

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_create_restore(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_restore

        DEPRECATED. Please use the `post_create_restore_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code. This `post_create_restore` interceptor runs
        before the `post_create_restore_with_metadata` interceptor.
        """
        return response

    def post_create_restore_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_restore

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_create_restore_with_metadata`
        interceptor in new development instead of the `post_create_restore` interceptor.
        When both interceptors are used, this `post_create_restore_with_metadata` interceptor runs after the
        `post_create_restore` interceptor. The (possibly modified) response returned by
        `post_create_restore` will be passed to
        `post_create_restore_with_metadata`.
        """
        return response, metadata

    def pre_create_restore_channel(
        self,
        request: gkebackup.CreateRestoreChannelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.CreateRestoreChannelRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_restore_channel

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_create_restore_channel(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_restore_channel

        DEPRECATED. Please use the `post_create_restore_channel_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code. This `post_create_restore_channel` interceptor runs
        before the `post_create_restore_channel_with_metadata` interceptor.
        """
        return response

    def post_create_restore_channel_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_restore_channel

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_create_restore_channel_with_metadata`
        interceptor in new development instead of the `post_create_restore_channel` interceptor.
        When both interceptors are used, this `post_create_restore_channel_with_metadata` interceptor runs after the
        `post_create_restore_channel` interceptor. The (possibly modified) response returned by
        `post_create_restore_channel` will be passed to
        `post_create_restore_channel_with_metadata`.
        """
        return response, metadata

    def pre_create_restore_plan(
        self,
        request: gkebackup.CreateRestorePlanRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.CreateRestorePlanRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_restore_plan

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_create_restore_plan(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_restore_plan

        DEPRECATED. Please use the `post_create_restore_plan_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code. This `post_create_restore_plan` interceptor runs
        before the `post_create_restore_plan_with_metadata` interceptor.
        """
        return response

    def post_create_restore_plan_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_restore_plan

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_create_restore_plan_with_metadata`
        interceptor in new development instead of the `post_create_restore_plan` interceptor.
        When both interceptors are used, this `post_create_restore_plan_with_metadata` interceptor runs after the
        `post_create_restore_plan` interceptor. The (possibly modified) response returned by
        `post_create_restore_plan` will be passed to
        `post_create_restore_plan_with_metadata`.
        """
        return response, metadata

    def pre_delete_backup(
        self,
        request: gkebackup.DeleteBackupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gkebackup.DeleteBackupRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_backup

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_delete_backup(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_backup

        DEPRECATED. Please use the `post_delete_backup_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
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
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_delete_backup_with_metadata`
        interceptor in new development instead of the `post_delete_backup` interceptor.
        When both interceptors are used, this `post_delete_backup_with_metadata` interceptor runs after the
        `post_delete_backup` interceptor. The (possibly modified) response returned by
        `post_delete_backup` will be passed to
        `post_delete_backup_with_metadata`.
        """
        return response, metadata

    def pre_delete_backup_channel(
        self,
        request: gkebackup.DeleteBackupChannelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.DeleteBackupChannelRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_backup_channel

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_delete_backup_channel(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_backup_channel

        DEPRECATED. Please use the `post_delete_backup_channel_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code. This `post_delete_backup_channel` interceptor runs
        before the `post_delete_backup_channel_with_metadata` interceptor.
        """
        return response

    def post_delete_backup_channel_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_backup_channel

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_delete_backup_channel_with_metadata`
        interceptor in new development instead of the `post_delete_backup_channel` interceptor.
        When both interceptors are used, this `post_delete_backup_channel_with_metadata` interceptor runs after the
        `post_delete_backup_channel` interceptor. The (possibly modified) response returned by
        `post_delete_backup_channel` will be passed to
        `post_delete_backup_channel_with_metadata`.
        """
        return response, metadata

    def pre_delete_backup_plan(
        self,
        request: gkebackup.DeleteBackupPlanRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.DeleteBackupPlanRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_backup_plan

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_delete_backup_plan(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_backup_plan

        DEPRECATED. Please use the `post_delete_backup_plan_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
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
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_delete_backup_plan_with_metadata`
        interceptor in new development instead of the `post_delete_backup_plan` interceptor.
        When both interceptors are used, this `post_delete_backup_plan_with_metadata` interceptor runs after the
        `post_delete_backup_plan` interceptor. The (possibly modified) response returned by
        `post_delete_backup_plan` will be passed to
        `post_delete_backup_plan_with_metadata`.
        """
        return response, metadata

    def pre_delete_restore(
        self,
        request: gkebackup.DeleteRestoreRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gkebackup.DeleteRestoreRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_restore

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_delete_restore(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_restore

        DEPRECATED. Please use the `post_delete_restore_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code. This `post_delete_restore` interceptor runs
        before the `post_delete_restore_with_metadata` interceptor.
        """
        return response

    def post_delete_restore_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_restore

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_delete_restore_with_metadata`
        interceptor in new development instead of the `post_delete_restore` interceptor.
        When both interceptors are used, this `post_delete_restore_with_metadata` interceptor runs after the
        `post_delete_restore` interceptor. The (possibly modified) response returned by
        `post_delete_restore` will be passed to
        `post_delete_restore_with_metadata`.
        """
        return response, metadata

    def pre_delete_restore_channel(
        self,
        request: gkebackup.DeleteRestoreChannelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.DeleteRestoreChannelRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_restore_channel

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_delete_restore_channel(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_restore_channel

        DEPRECATED. Please use the `post_delete_restore_channel_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code. This `post_delete_restore_channel` interceptor runs
        before the `post_delete_restore_channel_with_metadata` interceptor.
        """
        return response

    def post_delete_restore_channel_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_restore_channel

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_delete_restore_channel_with_metadata`
        interceptor in new development instead of the `post_delete_restore_channel` interceptor.
        When both interceptors are used, this `post_delete_restore_channel_with_metadata` interceptor runs after the
        `post_delete_restore_channel` interceptor. The (possibly modified) response returned by
        `post_delete_restore_channel` will be passed to
        `post_delete_restore_channel_with_metadata`.
        """
        return response, metadata

    def pre_delete_restore_plan(
        self,
        request: gkebackup.DeleteRestorePlanRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.DeleteRestorePlanRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_restore_plan

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_delete_restore_plan(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_restore_plan

        DEPRECATED. Please use the `post_delete_restore_plan_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code. This `post_delete_restore_plan` interceptor runs
        before the `post_delete_restore_plan_with_metadata` interceptor.
        """
        return response

    def post_delete_restore_plan_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_restore_plan

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_delete_restore_plan_with_metadata`
        interceptor in new development instead of the `post_delete_restore_plan` interceptor.
        When both interceptors are used, this `post_delete_restore_plan_with_metadata` interceptor runs after the
        `post_delete_restore_plan` interceptor. The (possibly modified) response returned by
        `post_delete_restore_plan` will be passed to
        `post_delete_restore_plan_with_metadata`.
        """
        return response, metadata

    def pre_get_backup(
        self,
        request: gkebackup.GetBackupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gkebackup.GetBackupRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_backup

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_get_backup(self, response: backup.Backup) -> backup.Backup:
        """Post-rpc interceptor for get_backup

        DEPRECATED. Please use the `post_get_backup_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code. This `post_get_backup` interceptor runs
        before the `post_get_backup_with_metadata` interceptor.
        """
        return response

    def post_get_backup_with_metadata(
        self, response: backup.Backup, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[backup.Backup, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_backup

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_get_backup_with_metadata`
        interceptor in new development instead of the `post_get_backup` interceptor.
        When both interceptors are used, this `post_get_backup_with_metadata` interceptor runs after the
        `post_get_backup` interceptor. The (possibly modified) response returned by
        `post_get_backup` will be passed to
        `post_get_backup_with_metadata`.
        """
        return response, metadata

    def pre_get_backup_channel(
        self,
        request: gkebackup.GetBackupChannelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.GetBackupChannelRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_backup_channel

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_get_backup_channel(
        self, response: backup_channel.BackupChannel
    ) -> backup_channel.BackupChannel:
        """Post-rpc interceptor for get_backup_channel

        DEPRECATED. Please use the `post_get_backup_channel_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code. This `post_get_backup_channel` interceptor runs
        before the `post_get_backup_channel_with_metadata` interceptor.
        """
        return response

    def post_get_backup_channel_with_metadata(
        self,
        response: backup_channel.BackupChannel,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[backup_channel.BackupChannel, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_backup_channel

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_get_backup_channel_with_metadata`
        interceptor in new development instead of the `post_get_backup_channel` interceptor.
        When both interceptors are used, this `post_get_backup_channel_with_metadata` interceptor runs after the
        `post_get_backup_channel` interceptor. The (possibly modified) response returned by
        `post_get_backup_channel` will be passed to
        `post_get_backup_channel_with_metadata`.
        """
        return response, metadata

    def pre_get_backup_index_download_url(
        self,
        request: gkebackup.GetBackupIndexDownloadUrlRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.GetBackupIndexDownloadUrlRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_backup_index_download_url

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_get_backup_index_download_url(
        self, response: gkebackup.GetBackupIndexDownloadUrlResponse
    ) -> gkebackup.GetBackupIndexDownloadUrlResponse:
        """Post-rpc interceptor for get_backup_index_download_url

        DEPRECATED. Please use the `post_get_backup_index_download_url_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code. This `post_get_backup_index_download_url` interceptor runs
        before the `post_get_backup_index_download_url_with_metadata` interceptor.
        """
        return response

    def post_get_backup_index_download_url_with_metadata(
        self,
        response: gkebackup.GetBackupIndexDownloadUrlResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.GetBackupIndexDownloadUrlResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_backup_index_download_url

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_get_backup_index_download_url_with_metadata`
        interceptor in new development instead of the `post_get_backup_index_download_url` interceptor.
        When both interceptors are used, this `post_get_backup_index_download_url_with_metadata` interceptor runs after the
        `post_get_backup_index_download_url` interceptor. The (possibly modified) response returned by
        `post_get_backup_index_download_url` will be passed to
        `post_get_backup_index_download_url_with_metadata`.
        """
        return response, metadata

    def pre_get_backup_plan(
        self,
        request: gkebackup.GetBackupPlanRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gkebackup.GetBackupPlanRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_backup_plan

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_get_backup_plan(
        self, response: backup_plan.BackupPlan
    ) -> backup_plan.BackupPlan:
        """Post-rpc interceptor for get_backup_plan

        DEPRECATED. Please use the `post_get_backup_plan_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code. This `post_get_backup_plan` interceptor runs
        before the `post_get_backup_plan_with_metadata` interceptor.
        """
        return response

    def post_get_backup_plan_with_metadata(
        self,
        response: backup_plan.BackupPlan,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[backup_plan.BackupPlan, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_backup_plan

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_get_backup_plan_with_metadata`
        interceptor in new development instead of the `post_get_backup_plan` interceptor.
        When both interceptors are used, this `post_get_backup_plan_with_metadata` interceptor runs after the
        `post_get_backup_plan` interceptor. The (possibly modified) response returned by
        `post_get_backup_plan` will be passed to
        `post_get_backup_plan_with_metadata`.
        """
        return response, metadata

    def pre_get_backup_plan_binding(
        self,
        request: gkebackup.GetBackupPlanBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.GetBackupPlanBindingRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_backup_plan_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_get_backup_plan_binding(
        self, response: backup_plan_binding.BackupPlanBinding
    ) -> backup_plan_binding.BackupPlanBinding:
        """Post-rpc interceptor for get_backup_plan_binding

        DEPRECATED. Please use the `post_get_backup_plan_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code. This `post_get_backup_plan_binding` interceptor runs
        before the `post_get_backup_plan_binding_with_metadata` interceptor.
        """
        return response

    def post_get_backup_plan_binding_with_metadata(
        self,
        response: backup_plan_binding.BackupPlanBinding,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        backup_plan_binding.BackupPlanBinding, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_backup_plan_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_get_backup_plan_binding_with_metadata`
        interceptor in new development instead of the `post_get_backup_plan_binding` interceptor.
        When both interceptors are used, this `post_get_backup_plan_binding_with_metadata` interceptor runs after the
        `post_get_backup_plan_binding` interceptor. The (possibly modified) response returned by
        `post_get_backup_plan_binding` will be passed to
        `post_get_backup_plan_binding_with_metadata`.
        """
        return response, metadata

    def pre_get_restore(
        self,
        request: gkebackup.GetRestoreRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gkebackup.GetRestoreRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_restore

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_get_restore(self, response: restore.Restore) -> restore.Restore:
        """Post-rpc interceptor for get_restore

        DEPRECATED. Please use the `post_get_restore_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code. This `post_get_restore` interceptor runs
        before the `post_get_restore_with_metadata` interceptor.
        """
        return response

    def post_get_restore_with_metadata(
        self,
        response: restore.Restore,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[restore.Restore, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_restore

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_get_restore_with_metadata`
        interceptor in new development instead of the `post_get_restore` interceptor.
        When both interceptors are used, this `post_get_restore_with_metadata` interceptor runs after the
        `post_get_restore` interceptor. The (possibly modified) response returned by
        `post_get_restore` will be passed to
        `post_get_restore_with_metadata`.
        """
        return response, metadata

    def pre_get_restore_channel(
        self,
        request: gkebackup.GetRestoreChannelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.GetRestoreChannelRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_restore_channel

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_get_restore_channel(
        self, response: restore_channel.RestoreChannel
    ) -> restore_channel.RestoreChannel:
        """Post-rpc interceptor for get_restore_channel

        DEPRECATED. Please use the `post_get_restore_channel_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code. This `post_get_restore_channel` interceptor runs
        before the `post_get_restore_channel_with_metadata` interceptor.
        """
        return response

    def post_get_restore_channel_with_metadata(
        self,
        response: restore_channel.RestoreChannel,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[restore_channel.RestoreChannel, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_restore_channel

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_get_restore_channel_with_metadata`
        interceptor in new development instead of the `post_get_restore_channel` interceptor.
        When both interceptors are used, this `post_get_restore_channel_with_metadata` interceptor runs after the
        `post_get_restore_channel` interceptor. The (possibly modified) response returned by
        `post_get_restore_channel` will be passed to
        `post_get_restore_channel_with_metadata`.
        """
        return response, metadata

    def pre_get_restore_plan(
        self,
        request: gkebackup.GetRestorePlanRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.GetRestorePlanRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_restore_plan

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_get_restore_plan(
        self, response: restore_plan.RestorePlan
    ) -> restore_plan.RestorePlan:
        """Post-rpc interceptor for get_restore_plan

        DEPRECATED. Please use the `post_get_restore_plan_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code. This `post_get_restore_plan` interceptor runs
        before the `post_get_restore_plan_with_metadata` interceptor.
        """
        return response

    def post_get_restore_plan_with_metadata(
        self,
        response: restore_plan.RestorePlan,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[restore_plan.RestorePlan, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_restore_plan

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_get_restore_plan_with_metadata`
        interceptor in new development instead of the `post_get_restore_plan` interceptor.
        When both interceptors are used, this `post_get_restore_plan_with_metadata` interceptor runs after the
        `post_get_restore_plan` interceptor. The (possibly modified) response returned by
        `post_get_restore_plan` will be passed to
        `post_get_restore_plan_with_metadata`.
        """
        return response, metadata

    def pre_get_restore_plan_binding(
        self,
        request: gkebackup.GetRestorePlanBindingRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.GetRestorePlanBindingRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_restore_plan_binding

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_get_restore_plan_binding(
        self, response: restore_plan_binding.RestorePlanBinding
    ) -> restore_plan_binding.RestorePlanBinding:
        """Post-rpc interceptor for get_restore_plan_binding

        DEPRECATED. Please use the `post_get_restore_plan_binding_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code. This `post_get_restore_plan_binding` interceptor runs
        before the `post_get_restore_plan_binding_with_metadata` interceptor.
        """
        return response

    def post_get_restore_plan_binding_with_metadata(
        self,
        response: restore_plan_binding.RestorePlanBinding,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        restore_plan_binding.RestorePlanBinding, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_restore_plan_binding

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_get_restore_plan_binding_with_metadata`
        interceptor in new development instead of the `post_get_restore_plan_binding` interceptor.
        When both interceptors are used, this `post_get_restore_plan_binding_with_metadata` interceptor runs after the
        `post_get_restore_plan_binding` interceptor. The (possibly modified) response returned by
        `post_get_restore_plan_binding` will be passed to
        `post_get_restore_plan_binding_with_metadata`.
        """
        return response, metadata

    def pre_get_volume_backup(
        self,
        request: gkebackup.GetVolumeBackupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.GetVolumeBackupRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_volume_backup

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_get_volume_backup(
        self, response: volume.VolumeBackup
    ) -> volume.VolumeBackup:
        """Post-rpc interceptor for get_volume_backup

        DEPRECATED. Please use the `post_get_volume_backup_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code. This `post_get_volume_backup` interceptor runs
        before the `post_get_volume_backup_with_metadata` interceptor.
        """
        return response

    def post_get_volume_backup_with_metadata(
        self,
        response: volume.VolumeBackup,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[volume.VolumeBackup, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_volume_backup

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_get_volume_backup_with_metadata`
        interceptor in new development instead of the `post_get_volume_backup` interceptor.
        When both interceptors are used, this `post_get_volume_backup_with_metadata` interceptor runs after the
        `post_get_volume_backup` interceptor. The (possibly modified) response returned by
        `post_get_volume_backup` will be passed to
        `post_get_volume_backup_with_metadata`.
        """
        return response, metadata

    def pre_get_volume_restore(
        self,
        request: gkebackup.GetVolumeRestoreRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.GetVolumeRestoreRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_volume_restore

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_get_volume_restore(
        self, response: volume.VolumeRestore
    ) -> volume.VolumeRestore:
        """Post-rpc interceptor for get_volume_restore

        DEPRECATED. Please use the `post_get_volume_restore_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code. This `post_get_volume_restore` interceptor runs
        before the `post_get_volume_restore_with_metadata` interceptor.
        """
        return response

    def post_get_volume_restore_with_metadata(
        self,
        response: volume.VolumeRestore,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[volume.VolumeRestore, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_volume_restore

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_get_volume_restore_with_metadata`
        interceptor in new development instead of the `post_get_volume_restore` interceptor.
        When both interceptors are used, this `post_get_volume_restore_with_metadata` interceptor runs after the
        `post_get_volume_restore` interceptor. The (possibly modified) response returned by
        `post_get_volume_restore` will be passed to
        `post_get_volume_restore_with_metadata`.
        """
        return response, metadata

    def pre_list_backup_channels(
        self,
        request: gkebackup.ListBackupChannelsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.ListBackupChannelsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_backup_channels

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_list_backup_channels(
        self, response: gkebackup.ListBackupChannelsResponse
    ) -> gkebackup.ListBackupChannelsResponse:
        """Post-rpc interceptor for list_backup_channels

        DEPRECATED. Please use the `post_list_backup_channels_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code. This `post_list_backup_channels` interceptor runs
        before the `post_list_backup_channels_with_metadata` interceptor.
        """
        return response

    def post_list_backup_channels_with_metadata(
        self,
        response: gkebackup.ListBackupChannelsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.ListBackupChannelsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_backup_channels

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_list_backup_channels_with_metadata`
        interceptor in new development instead of the `post_list_backup_channels` interceptor.
        When both interceptors are used, this `post_list_backup_channels_with_metadata` interceptor runs after the
        `post_list_backup_channels` interceptor. The (possibly modified) response returned by
        `post_list_backup_channels` will be passed to
        `post_list_backup_channels_with_metadata`.
        """
        return response, metadata

    def pre_list_backup_plan_bindings(
        self,
        request: gkebackup.ListBackupPlanBindingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.ListBackupPlanBindingsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_backup_plan_bindings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_list_backup_plan_bindings(
        self, response: gkebackup.ListBackupPlanBindingsResponse
    ) -> gkebackup.ListBackupPlanBindingsResponse:
        """Post-rpc interceptor for list_backup_plan_bindings

        DEPRECATED. Please use the `post_list_backup_plan_bindings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code. This `post_list_backup_plan_bindings` interceptor runs
        before the `post_list_backup_plan_bindings_with_metadata` interceptor.
        """
        return response

    def post_list_backup_plan_bindings_with_metadata(
        self,
        response: gkebackup.ListBackupPlanBindingsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.ListBackupPlanBindingsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_backup_plan_bindings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_list_backup_plan_bindings_with_metadata`
        interceptor in new development instead of the `post_list_backup_plan_bindings` interceptor.
        When both interceptors are used, this `post_list_backup_plan_bindings_with_metadata` interceptor runs after the
        `post_list_backup_plan_bindings` interceptor. The (possibly modified) response returned by
        `post_list_backup_plan_bindings` will be passed to
        `post_list_backup_plan_bindings_with_metadata`.
        """
        return response, metadata

    def pre_list_backup_plans(
        self,
        request: gkebackup.ListBackupPlansRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.ListBackupPlansRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_backup_plans

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_list_backup_plans(
        self, response: gkebackup.ListBackupPlansResponse
    ) -> gkebackup.ListBackupPlansResponse:
        """Post-rpc interceptor for list_backup_plans

        DEPRECATED. Please use the `post_list_backup_plans_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code. This `post_list_backup_plans` interceptor runs
        before the `post_list_backup_plans_with_metadata` interceptor.
        """
        return response

    def post_list_backup_plans_with_metadata(
        self,
        response: gkebackup.ListBackupPlansResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.ListBackupPlansResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_backup_plans

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupForGKE server but before it is returned to user code.

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
        request: gkebackup.ListBackupsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gkebackup.ListBackupsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_backups

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_list_backups(
        self, response: gkebackup.ListBackupsResponse
    ) -> gkebackup.ListBackupsResponse:
        """Post-rpc interceptor for list_backups

        DEPRECATED. Please use the `post_list_backups_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code. This `post_list_backups` interceptor runs
        before the `post_list_backups_with_metadata` interceptor.
        """
        return response

    def post_list_backups_with_metadata(
        self,
        response: gkebackup.ListBackupsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gkebackup.ListBackupsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_backups

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_list_backups_with_metadata`
        interceptor in new development instead of the `post_list_backups` interceptor.
        When both interceptors are used, this `post_list_backups_with_metadata` interceptor runs after the
        `post_list_backups` interceptor. The (possibly modified) response returned by
        `post_list_backups` will be passed to
        `post_list_backups_with_metadata`.
        """
        return response, metadata

    def pre_list_restore_channels(
        self,
        request: gkebackup.ListRestoreChannelsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.ListRestoreChannelsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_restore_channels

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_list_restore_channels(
        self, response: gkebackup.ListRestoreChannelsResponse
    ) -> gkebackup.ListRestoreChannelsResponse:
        """Post-rpc interceptor for list_restore_channels

        DEPRECATED. Please use the `post_list_restore_channels_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code. This `post_list_restore_channels` interceptor runs
        before the `post_list_restore_channels_with_metadata` interceptor.
        """
        return response

    def post_list_restore_channels_with_metadata(
        self,
        response: gkebackup.ListRestoreChannelsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.ListRestoreChannelsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_restore_channels

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_list_restore_channels_with_metadata`
        interceptor in new development instead of the `post_list_restore_channels` interceptor.
        When both interceptors are used, this `post_list_restore_channels_with_metadata` interceptor runs after the
        `post_list_restore_channels` interceptor. The (possibly modified) response returned by
        `post_list_restore_channels` will be passed to
        `post_list_restore_channels_with_metadata`.
        """
        return response, metadata

    def pre_list_restore_plan_bindings(
        self,
        request: gkebackup.ListRestorePlanBindingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.ListRestorePlanBindingsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_restore_plan_bindings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_list_restore_plan_bindings(
        self, response: gkebackup.ListRestorePlanBindingsResponse
    ) -> gkebackup.ListRestorePlanBindingsResponse:
        """Post-rpc interceptor for list_restore_plan_bindings

        DEPRECATED. Please use the `post_list_restore_plan_bindings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code. This `post_list_restore_plan_bindings` interceptor runs
        before the `post_list_restore_plan_bindings_with_metadata` interceptor.
        """
        return response

    def post_list_restore_plan_bindings_with_metadata(
        self,
        response: gkebackup.ListRestorePlanBindingsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.ListRestorePlanBindingsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_restore_plan_bindings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_list_restore_plan_bindings_with_metadata`
        interceptor in new development instead of the `post_list_restore_plan_bindings` interceptor.
        When both interceptors are used, this `post_list_restore_plan_bindings_with_metadata` interceptor runs after the
        `post_list_restore_plan_bindings` interceptor. The (possibly modified) response returned by
        `post_list_restore_plan_bindings` will be passed to
        `post_list_restore_plan_bindings_with_metadata`.
        """
        return response, metadata

    def pre_list_restore_plans(
        self,
        request: gkebackup.ListRestorePlansRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.ListRestorePlansRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_restore_plans

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_list_restore_plans(
        self, response: gkebackup.ListRestorePlansResponse
    ) -> gkebackup.ListRestorePlansResponse:
        """Post-rpc interceptor for list_restore_plans

        DEPRECATED. Please use the `post_list_restore_plans_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code. This `post_list_restore_plans` interceptor runs
        before the `post_list_restore_plans_with_metadata` interceptor.
        """
        return response

    def post_list_restore_plans_with_metadata(
        self,
        response: gkebackup.ListRestorePlansResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.ListRestorePlansResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_restore_plans

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_list_restore_plans_with_metadata`
        interceptor in new development instead of the `post_list_restore_plans` interceptor.
        When both interceptors are used, this `post_list_restore_plans_with_metadata` interceptor runs after the
        `post_list_restore_plans` interceptor. The (possibly modified) response returned by
        `post_list_restore_plans` will be passed to
        `post_list_restore_plans_with_metadata`.
        """
        return response, metadata

    def pre_list_restores(
        self,
        request: gkebackup.ListRestoresRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gkebackup.ListRestoresRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_restores

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_list_restores(
        self, response: gkebackup.ListRestoresResponse
    ) -> gkebackup.ListRestoresResponse:
        """Post-rpc interceptor for list_restores

        DEPRECATED. Please use the `post_list_restores_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code. This `post_list_restores` interceptor runs
        before the `post_list_restores_with_metadata` interceptor.
        """
        return response

    def post_list_restores_with_metadata(
        self,
        response: gkebackup.ListRestoresResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gkebackup.ListRestoresResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_restores

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_list_restores_with_metadata`
        interceptor in new development instead of the `post_list_restores` interceptor.
        When both interceptors are used, this `post_list_restores_with_metadata` interceptor runs after the
        `post_list_restores` interceptor. The (possibly modified) response returned by
        `post_list_restores` will be passed to
        `post_list_restores_with_metadata`.
        """
        return response, metadata

    def pre_list_volume_backups(
        self,
        request: gkebackup.ListVolumeBackupsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.ListVolumeBackupsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_volume_backups

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_list_volume_backups(
        self, response: gkebackup.ListVolumeBackupsResponse
    ) -> gkebackup.ListVolumeBackupsResponse:
        """Post-rpc interceptor for list_volume_backups

        DEPRECATED. Please use the `post_list_volume_backups_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code. This `post_list_volume_backups` interceptor runs
        before the `post_list_volume_backups_with_metadata` interceptor.
        """
        return response

    def post_list_volume_backups_with_metadata(
        self,
        response: gkebackup.ListVolumeBackupsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.ListVolumeBackupsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_volume_backups

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_list_volume_backups_with_metadata`
        interceptor in new development instead of the `post_list_volume_backups` interceptor.
        When both interceptors are used, this `post_list_volume_backups_with_metadata` interceptor runs after the
        `post_list_volume_backups` interceptor. The (possibly modified) response returned by
        `post_list_volume_backups` will be passed to
        `post_list_volume_backups_with_metadata`.
        """
        return response, metadata

    def pre_list_volume_restores(
        self,
        request: gkebackup.ListVolumeRestoresRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.ListVolumeRestoresRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_volume_restores

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_list_volume_restores(
        self, response: gkebackup.ListVolumeRestoresResponse
    ) -> gkebackup.ListVolumeRestoresResponse:
        """Post-rpc interceptor for list_volume_restores

        DEPRECATED. Please use the `post_list_volume_restores_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code. This `post_list_volume_restores` interceptor runs
        before the `post_list_volume_restores_with_metadata` interceptor.
        """
        return response

    def post_list_volume_restores_with_metadata(
        self,
        response: gkebackup.ListVolumeRestoresResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.ListVolumeRestoresResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_volume_restores

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_list_volume_restores_with_metadata`
        interceptor in new development instead of the `post_list_volume_restores` interceptor.
        When both interceptors are used, this `post_list_volume_restores_with_metadata` interceptor runs after the
        `post_list_volume_restores` interceptor. The (possibly modified) response returned by
        `post_list_volume_restores` will be passed to
        `post_list_volume_restores_with_metadata`.
        """
        return response, metadata

    def pre_update_backup(
        self,
        request: gkebackup.UpdateBackupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gkebackup.UpdateBackupRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_backup

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_update_backup(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_backup

        DEPRECATED. Please use the `post_update_backup_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
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
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_update_backup_with_metadata`
        interceptor in new development instead of the `post_update_backup` interceptor.
        When both interceptors are used, this `post_update_backup_with_metadata` interceptor runs after the
        `post_update_backup` interceptor. The (possibly modified) response returned by
        `post_update_backup` will be passed to
        `post_update_backup_with_metadata`.
        """
        return response, metadata

    def pre_update_backup_channel(
        self,
        request: gkebackup.UpdateBackupChannelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.UpdateBackupChannelRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_backup_channel

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_update_backup_channel(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_backup_channel

        DEPRECATED. Please use the `post_update_backup_channel_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code. This `post_update_backup_channel` interceptor runs
        before the `post_update_backup_channel_with_metadata` interceptor.
        """
        return response

    def post_update_backup_channel_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_backup_channel

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_update_backup_channel_with_metadata`
        interceptor in new development instead of the `post_update_backup_channel` interceptor.
        When both interceptors are used, this `post_update_backup_channel_with_metadata` interceptor runs after the
        `post_update_backup_channel` interceptor. The (possibly modified) response returned by
        `post_update_backup_channel` will be passed to
        `post_update_backup_channel_with_metadata`.
        """
        return response, metadata

    def pre_update_backup_plan(
        self,
        request: gkebackup.UpdateBackupPlanRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.UpdateBackupPlanRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_backup_plan

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_update_backup_plan(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_backup_plan

        DEPRECATED. Please use the `post_update_backup_plan_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
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
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_update_backup_plan_with_metadata`
        interceptor in new development instead of the `post_update_backup_plan` interceptor.
        When both interceptors are used, this `post_update_backup_plan_with_metadata` interceptor runs after the
        `post_update_backup_plan` interceptor. The (possibly modified) response returned by
        `post_update_backup_plan` will be passed to
        `post_update_backup_plan_with_metadata`.
        """
        return response, metadata

    def pre_update_restore(
        self,
        request: gkebackup.UpdateRestoreRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gkebackup.UpdateRestoreRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_restore

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_update_restore(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_restore

        DEPRECATED. Please use the `post_update_restore_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code. This `post_update_restore` interceptor runs
        before the `post_update_restore_with_metadata` interceptor.
        """
        return response

    def post_update_restore_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_restore

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_update_restore_with_metadata`
        interceptor in new development instead of the `post_update_restore` interceptor.
        When both interceptors are used, this `post_update_restore_with_metadata` interceptor runs after the
        `post_update_restore` interceptor. The (possibly modified) response returned by
        `post_update_restore` will be passed to
        `post_update_restore_with_metadata`.
        """
        return response, metadata

    def pre_update_restore_channel(
        self,
        request: gkebackup.UpdateRestoreChannelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.UpdateRestoreChannelRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_restore_channel

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_update_restore_channel(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_restore_channel

        DEPRECATED. Please use the `post_update_restore_channel_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code. This `post_update_restore_channel` interceptor runs
        before the `post_update_restore_channel_with_metadata` interceptor.
        """
        return response

    def post_update_restore_channel_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_restore_channel

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_update_restore_channel_with_metadata`
        interceptor in new development instead of the `post_update_restore_channel` interceptor.
        When both interceptors are used, this `post_update_restore_channel_with_metadata` interceptor runs after the
        `post_update_restore_channel` interceptor. The (possibly modified) response returned by
        `post_update_restore_channel` will be passed to
        `post_update_restore_channel_with_metadata`.
        """
        return response, metadata

    def pre_update_restore_plan(
        self,
        request: gkebackup.UpdateRestorePlanRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gkebackup.UpdateRestorePlanRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_restore_plan

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_update_restore_plan(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_restore_plan

        DEPRECATED. Please use the `post_update_restore_plan_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code. This `post_update_restore_plan` interceptor runs
        before the `post_update_restore_plan_with_metadata` interceptor.
        """
        return response

    def post_update_restore_plan_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_restore_plan

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BackupForGKE server but before it is returned to user code.

        We recommend only using this `post_update_restore_plan_with_metadata`
        interceptor in new development instead of the `post_update_restore_plan` interceptor.
        When both interceptors are used, this `post_update_restore_plan_with_metadata` interceptor runs after the
        `post_update_restore_plan` interceptor. The (possibly modified) response returned by
        `post_update_restore_plan` will be passed to
        `post_update_restore_plan_with_metadata`.
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
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the BackupForGKE server but before
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
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the BackupForGKE server but before
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
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the BackupForGKE server but before
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
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the BackupForGKE server but before
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
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the BackupForGKE server but before
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
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the BackupForGKE server but before
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
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the BackupForGKE server but before
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
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the BackupForGKE server but before
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
        before they are sent to the BackupForGKE server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the BackupForGKE server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class BackupForGKERestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: BackupForGKERestInterceptor


class BackupForGKERestTransport(_BaseBackupForGKERestTransport):
    """REST backend synchronous transport for BackupForGKE.

    BackupForGKE allows Kubernetes administrators to configure,
    execute, and manage backup and restore operations for their GKE
    clusters.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "gkebackup.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[BackupForGKERestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'gkebackup.googleapis.com').
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
            interceptor (Optional[BackupForGKERestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or BackupForGKERestInterceptor()
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

    class _CreateBackup(
        _BaseBackupForGKERestTransport._BaseCreateBackup, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.CreateBackup")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.CreateBackupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create backup method over HTTP.

            Args:
                request (~.gkebackup.CreateBackupRequest):
                    The request object. Request message for CreateBackup.
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
                _BaseBackupForGKERestTransport._BaseCreateBackup._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_backup(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseCreateBackup,
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
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.CreateBackup",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "CreateBackup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._CreateBackup._get_response(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.create_backup",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "CreateBackup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateBackupChannel(
        _BaseBackupForGKERestTransport._BaseCreateBackupChannel, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.CreateBackupChannel")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.CreateBackupChannelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create backup channel method over HTTP.

            Args:
                request (~.gkebackup.CreateBackupChannelRequest):
                    The request object. Request message for
                CreateBackupChannel.
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

            http_options = _BaseBackupForGKERestTransport._BaseCreateBackupChannel._get_http_options()
            request, metadata = self._interceptor.pre_create_backup_channel(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseCreateBackupChannel,
                    "_BaseCreateBackupChannel__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.CreateBackupChannel",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "CreateBackupChannel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._CreateBackupChannel._get_response(
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

            resp = self._interceptor.post_create_backup_channel(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_backup_channel_with_metadata(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.create_backup_channel",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "CreateBackupChannel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateBackupPlan(
        _BaseBackupForGKERestTransport._BaseCreateBackupPlan, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.CreateBackupPlan")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.CreateBackupPlanRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create backup plan method over HTTP.

            Args:
                request (~.gkebackup.CreateBackupPlanRequest):
                    The request object. Request message for CreateBackupPlan.
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
                _BaseBackupForGKERestTransport._BaseCreateBackupPlan._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_backup_plan(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseCreateBackupPlan,
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
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.CreateBackupPlan",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "CreateBackupPlan",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._CreateBackupPlan._get_response(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.create_backup_plan",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "CreateBackupPlan",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateRestore(
        _BaseBackupForGKERestTransport._BaseCreateRestore, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.CreateRestore")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.CreateRestoreRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create restore method over HTTP.

            Args:
                request (~.gkebackup.CreateRestoreRequest):
                    The request object. Request message for CreateRestore.
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
                _BaseBackupForGKERestTransport._BaseCreateRestore._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_restore(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseCreateRestore,
                    "_BaseCreateRestore__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.CreateRestore",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "CreateRestore",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._CreateRestore._get_response(
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

            resp = self._interceptor.post_create_restore(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_restore_with_metadata(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.create_restore",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "CreateRestore",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateRestoreChannel(
        _BaseBackupForGKERestTransport._BaseCreateRestoreChannel, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.CreateRestoreChannel")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.CreateRestoreChannelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create restore channel method over HTTP.

            Args:
                request (~.gkebackup.CreateRestoreChannelRequest):
                    The request object. Request message for
                CreateRestoreChannel.
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

            http_options = _BaseBackupForGKERestTransport._BaseCreateRestoreChannel._get_http_options()
            request, metadata = self._interceptor.pre_create_restore_channel(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseCreateRestoreChannel,
                    "_BaseCreateRestoreChannel__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.CreateRestoreChannel",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "CreateRestoreChannel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._CreateRestoreChannel._get_response(
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

            resp = self._interceptor.post_create_restore_channel(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_restore_channel_with_metadata(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.create_restore_channel",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "CreateRestoreChannel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateRestorePlan(
        _BaseBackupForGKERestTransport._BaseCreateRestorePlan, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.CreateRestorePlan")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.CreateRestorePlanRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create restore plan method over HTTP.

            Args:
                request (~.gkebackup.CreateRestorePlanRequest):
                    The request object. Request message for
                CreateRestorePlan.
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

            http_options = _BaseBackupForGKERestTransport._BaseCreateRestorePlan._get_http_options()
            request, metadata = self._interceptor.pre_create_restore_plan(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseCreateRestorePlan,
                    "_BaseCreateRestorePlan__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.CreateRestorePlan",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "CreateRestorePlan",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._CreateRestorePlan._get_response(
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

            resp = self._interceptor.post_create_restore_plan(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_restore_plan_with_metadata(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.create_restore_plan",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "CreateRestorePlan",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteBackup(
        _BaseBackupForGKERestTransport._BaseDeleteBackup, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.DeleteBackup")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.DeleteBackupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete backup method over HTTP.

            Args:
                request (~.gkebackup.DeleteBackupRequest):
                    The request object. Request message for DeleteBackup.
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
                _BaseBackupForGKERestTransport._BaseDeleteBackup._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_backup(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseDeleteBackup,
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
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.DeleteBackup",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "DeleteBackup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._DeleteBackup._get_response(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.delete_backup",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "DeleteBackup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteBackupChannel(
        _BaseBackupForGKERestTransport._BaseDeleteBackupChannel, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.DeleteBackupChannel")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.DeleteBackupChannelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete backup channel method over HTTP.

            Args:
                request (~.gkebackup.DeleteBackupChannelRequest):
                    The request object. Request message for
                DeleteBackupChannel.
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

            http_options = _BaseBackupForGKERestTransport._BaseDeleteBackupChannel._get_http_options()
            request, metadata = self._interceptor.pre_delete_backup_channel(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseDeleteBackupChannel,
                    "_BaseDeleteBackupChannel__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.DeleteBackupChannel",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "DeleteBackupChannel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._DeleteBackupChannel._get_response(
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

            resp = self._interceptor.post_delete_backup_channel(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_backup_channel_with_metadata(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.delete_backup_channel",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "DeleteBackupChannel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteBackupPlan(
        _BaseBackupForGKERestTransport._BaseDeleteBackupPlan, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.DeleteBackupPlan")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.DeleteBackupPlanRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete backup plan method over HTTP.

            Args:
                request (~.gkebackup.DeleteBackupPlanRequest):
                    The request object. Request message for DeleteBackupPlan.
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
                _BaseBackupForGKERestTransport._BaseDeleteBackupPlan._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_backup_plan(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseDeleteBackupPlan,
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
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.DeleteBackupPlan",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "DeleteBackupPlan",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._DeleteBackupPlan._get_response(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.delete_backup_plan",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "DeleteBackupPlan",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteRestore(
        _BaseBackupForGKERestTransport._BaseDeleteRestore, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.DeleteRestore")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.DeleteRestoreRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete restore method over HTTP.

            Args:
                request (~.gkebackup.DeleteRestoreRequest):
                    The request object. Request message for DeleteRestore.
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
                _BaseBackupForGKERestTransport._BaseDeleteRestore._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_restore(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseDeleteRestore,
                    "_BaseDeleteRestore__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.DeleteRestore",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "DeleteRestore",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._DeleteRestore._get_response(
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

            resp = self._interceptor.post_delete_restore(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_restore_with_metadata(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.delete_restore",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "DeleteRestore",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteRestoreChannel(
        _BaseBackupForGKERestTransport._BaseDeleteRestoreChannel, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.DeleteRestoreChannel")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.DeleteRestoreChannelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete restore channel method over HTTP.

            Args:
                request (~.gkebackup.DeleteRestoreChannelRequest):
                    The request object. Request message for
                DeleteRestoreChannel.
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

            http_options = _BaseBackupForGKERestTransport._BaseDeleteRestoreChannel._get_http_options()
            request, metadata = self._interceptor.pre_delete_restore_channel(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseDeleteRestoreChannel,
                    "_BaseDeleteRestoreChannel__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.DeleteRestoreChannel",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "DeleteRestoreChannel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._DeleteRestoreChannel._get_response(
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

            resp = self._interceptor.post_delete_restore_channel(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_restore_channel_with_metadata(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.delete_restore_channel",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "DeleteRestoreChannel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteRestorePlan(
        _BaseBackupForGKERestTransport._BaseDeleteRestorePlan, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.DeleteRestorePlan")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.DeleteRestorePlanRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete restore plan method over HTTP.

            Args:
                request (~.gkebackup.DeleteRestorePlanRequest):
                    The request object. Request message for
                DeleteRestorePlan.
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

            http_options = _BaseBackupForGKERestTransport._BaseDeleteRestorePlan._get_http_options()
            request, metadata = self._interceptor.pre_delete_restore_plan(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseDeleteRestorePlan,
                    "_BaseDeleteRestorePlan__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.DeleteRestorePlan",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "DeleteRestorePlan",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._DeleteRestorePlan._get_response(
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

            resp = self._interceptor.post_delete_restore_plan(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_restore_plan_with_metadata(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.delete_restore_plan",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "DeleteRestorePlan",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetBackup(
        _BaseBackupForGKERestTransport._BaseGetBackup, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.GetBackup")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.GetBackupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> backup.Backup:
            r"""Call the get backup method over HTTP.

            Args:
                request (~.gkebackup.GetBackupRequest):
                    The request object. Request message for GetBackup.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.backup.Backup:
                    Represents a request to perform a
                single point-in-time capture of some
                portion of the state of a GKE cluster,
                the record of the backup operation
                itself, and an anchor for the underlying
                artifacts that comprise the Backup (the
                config backup and VolumeBackups).

            """

            http_options = (
                _BaseBackupForGKERestTransport._BaseGetBackup._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_backup(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseGetBackup,
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
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.GetBackup",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "GetBackup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._GetBackup._get_response(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.get_backup",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "GetBackup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetBackupChannel(
        _BaseBackupForGKERestTransport._BaseGetBackupChannel, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.GetBackupChannel")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.GetBackupChannelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> backup_channel.BackupChannel:
            r"""Call the get backup channel method over HTTP.

            Args:
                request (~.gkebackup.GetBackupChannelRequest):
                    The request object. Request message for GetBackupChannel.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.backup_channel.BackupChannel:
                    A BackupChannel imposes constraints on where clusters
                can be backed up. The BackupChannel should be in the
                same project and region as the cluster being backed up.
                The backup can be created only in destination_project.

            """

            http_options = (
                _BaseBackupForGKERestTransport._BaseGetBackupChannel._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_backup_channel(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseGetBackupChannel,
                    "_BaseGetBackupChannel__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.GetBackupChannel",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "GetBackupChannel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._GetBackupChannel._get_response(
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
            resp = backup_channel.BackupChannel()
            pb_resp = backup_channel.BackupChannel.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_backup_channel(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_backup_channel_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = backup_channel.BackupChannel.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.get_backup_channel",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "GetBackupChannel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetBackupIndexDownloadUrl(
        _BaseBackupForGKERestTransport._BaseGetBackupIndexDownloadUrl,
        BackupForGKERestStub,
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.GetBackupIndexDownloadUrl")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.GetBackupIndexDownloadUrlRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gkebackup.GetBackupIndexDownloadUrlResponse:
            r"""Call the get backup index download
            url method over HTTP.

                Args:
                    request (~.gkebackup.GetBackupIndexDownloadUrlRequest):
                        The request object. Request message for
                    GetBackupIndexDownloadUrl.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.gkebackup.GetBackupIndexDownloadUrlResponse:
                        Response message for
                    GetBackupIndexDownloadUrl.

            """

            http_options = _BaseBackupForGKERestTransport._BaseGetBackupIndexDownloadUrl._get_http_options()
            request, metadata = self._interceptor.pre_get_backup_index_download_url(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseGetBackupIndexDownloadUrl,
                    "_BaseGetBackupIndexDownloadUrl__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.GetBackupIndexDownloadUrl",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "GetBackupIndexDownloadUrl",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                BackupForGKERestTransport._GetBackupIndexDownloadUrl._get_response(
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
            resp = gkebackup.GetBackupIndexDownloadUrlResponse()
            pb_resp = gkebackup.GetBackupIndexDownloadUrlResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_backup_index_download_url(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_backup_index_download_url_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        gkebackup.GetBackupIndexDownloadUrlResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.get_backup_index_download_url",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "GetBackupIndexDownloadUrl",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetBackupPlan(
        _BaseBackupForGKERestTransport._BaseGetBackupPlan, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.GetBackupPlan")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.GetBackupPlanRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> backup_plan.BackupPlan:
            r"""Call the get backup plan method over HTTP.

            Args:
                request (~.gkebackup.GetBackupPlanRequest):
                    The request object. Request message for GetBackupPlan.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.backup_plan.BackupPlan:
                    Defines the configuration and
                scheduling for a "line" of Backups.

            """

            http_options = (
                _BaseBackupForGKERestTransport._BaseGetBackupPlan._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_backup_plan(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseGetBackupPlan,
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
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.GetBackupPlan",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "GetBackupPlan",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._GetBackupPlan._get_response(
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
            resp = backup_plan.BackupPlan()
            pb_resp = backup_plan.BackupPlan.pb(resp)

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
                    response_payload = backup_plan.BackupPlan.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.get_backup_plan",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "GetBackupPlan",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetBackupPlanBinding(
        _BaseBackupForGKERestTransport._BaseGetBackupPlanBinding, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.GetBackupPlanBinding")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.GetBackupPlanBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> backup_plan_binding.BackupPlanBinding:
            r"""Call the get backup plan binding method over HTTP.

            Args:
                request (~.gkebackup.GetBackupPlanBindingRequest):
                    The request object. Request message for
                GetBackupPlanBinding.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.backup_plan_binding.BackupPlanBinding:
                    A BackupPlanBinding binds a
                BackupPlan with a BackupChannel. This
                resource is created automatically when a
                BackupPlan is created using a
                BackupChannel. This also serves as a
                holder for cross-project fields that
                need to be displayed in the current
                project.

            """

            http_options = _BaseBackupForGKERestTransport._BaseGetBackupPlanBinding._get_http_options()
            request, metadata = self._interceptor.pre_get_backup_plan_binding(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseGetBackupPlanBinding,
                    "_BaseGetBackupPlanBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.GetBackupPlanBinding",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "GetBackupPlanBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._GetBackupPlanBinding._get_response(
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
            resp = backup_plan_binding.BackupPlanBinding()
            pb_resp = backup_plan_binding.BackupPlanBinding.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_backup_plan_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_backup_plan_binding_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = backup_plan_binding.BackupPlanBinding.to_json(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.get_backup_plan_binding",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "GetBackupPlanBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetRestore(
        _BaseBackupForGKERestTransport._BaseGetRestore, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.GetRestore")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.GetRestoreRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> restore.Restore:
            r"""Call the get restore method over HTTP.

            Args:
                request (~.gkebackup.GetRestoreRequest):
                    The request object. Request message for GetRestore.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.restore.Restore:
                    Represents both a request to Restore
                some portion of a Backup into a target
                GKE cluster and a record of the restore
                operation itself.

            """

            http_options = (
                _BaseBackupForGKERestTransport._BaseGetRestore._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_restore(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseGetRestore,
                    "_BaseGetRestore__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.GetRestore",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "GetRestore",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._GetRestore._get_response(
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
            resp = restore.Restore()
            pb_resp = restore.Restore.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_restore(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_restore_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = restore.Restore.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.get_restore",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "GetRestore",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetRestoreChannel(
        _BaseBackupForGKERestTransport._BaseGetRestoreChannel, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.GetRestoreChannel")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.GetRestoreChannelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> restore_channel.RestoreChannel:
            r"""Call the get restore channel method over HTTP.

            Args:
                request (~.gkebackup.GetRestoreChannelRequest):
                    The request object. Request message for
                GetRestoreChannel.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.restore_channel.RestoreChannel:
                    A RestoreChannel imposes constraints on where backups
                can be restored. The RestoreChannel should be in the
                same project and region as the backups. The backups can
                only be restored in the ``destination_project``.

            """

            http_options = _BaseBackupForGKERestTransport._BaseGetRestoreChannel._get_http_options()
            request, metadata = self._interceptor.pre_get_restore_channel(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseGetRestoreChannel,
                    "_BaseGetRestoreChannel__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.GetRestoreChannel",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "GetRestoreChannel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._GetRestoreChannel._get_response(
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
            resp = restore_channel.RestoreChannel()
            pb_resp = restore_channel.RestoreChannel.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_restore_channel(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_restore_channel_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = restore_channel.RestoreChannel.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.get_restore_channel",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "GetRestoreChannel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetRestorePlan(
        _BaseBackupForGKERestTransport._BaseGetRestorePlan, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.GetRestorePlan")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.GetRestorePlanRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> restore_plan.RestorePlan:
            r"""Call the get restore plan method over HTTP.

            Args:
                request (~.gkebackup.GetRestorePlanRequest):
                    The request object. Request message for GetRestorePlan.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.restore_plan.RestorePlan:
                    The configuration of a potential
                series of Restore operations to be
                performed against Backups belong to a
                particular BackupPlan.

            """

            http_options = (
                _BaseBackupForGKERestTransport._BaseGetRestorePlan._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_restore_plan(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseGetRestorePlan,
                    "_BaseGetRestorePlan__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.GetRestorePlan",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "GetRestorePlan",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._GetRestorePlan._get_response(
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
            resp = restore_plan.RestorePlan()
            pb_resp = restore_plan.RestorePlan.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_restore_plan(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_restore_plan_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = restore_plan.RestorePlan.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.get_restore_plan",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "GetRestorePlan",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetRestorePlanBinding(
        _BaseBackupForGKERestTransport._BaseGetRestorePlanBinding, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.GetRestorePlanBinding")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.GetRestorePlanBindingRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> restore_plan_binding.RestorePlanBinding:
            r"""Call the get restore plan binding method over HTTP.

            Args:
                request (~.gkebackup.GetRestorePlanBindingRequest):
                    The request object. Request message for
                GetRestorePlanBinding.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.restore_plan_binding.RestorePlanBinding:
                    A RestorePlanBinding binds a
                RestorePlan with a RestoreChannel. This
                resource is created automatically when a
                RestorePlan is created using a
                RestoreChannel. This also serves as a
                holder for cross-project fields that
                need to be displayed in the current
                project.

            """

            http_options = _BaseBackupForGKERestTransport._BaseGetRestorePlanBinding._get_http_options()
            request, metadata = self._interceptor.pre_get_restore_plan_binding(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseGetRestorePlanBinding,
                    "_BaseGetRestorePlanBinding__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.GetRestorePlanBinding",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "GetRestorePlanBinding",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._GetRestorePlanBinding._get_response(
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
            resp = restore_plan_binding.RestorePlanBinding()
            pb_resp = restore_plan_binding.RestorePlanBinding.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_restore_plan_binding(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_restore_plan_binding_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = restore_plan_binding.RestorePlanBinding.to_json(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.get_restore_plan_binding",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "GetRestorePlanBinding",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetVolumeBackup(
        _BaseBackupForGKERestTransport._BaseGetVolumeBackup, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.GetVolumeBackup")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.GetVolumeBackupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> volume.VolumeBackup:
            r"""Call the get volume backup method over HTTP.

            Args:
                request (~.gkebackup.GetVolumeBackupRequest):
                    The request object. Request message for GetVolumeBackup.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.volume.VolumeBackup:
                    Represents the backup of a specific
                persistent volume as a component of a
                Backup - both the record of the
                operation and a pointer to the
                underlying storage-specific artifacts.

            """

            http_options = (
                _BaseBackupForGKERestTransport._BaseGetVolumeBackup._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_volume_backup(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseGetVolumeBackup,
                    "_BaseGetVolumeBackup__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.GetVolumeBackup",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "GetVolumeBackup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._GetVolumeBackup._get_response(
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
            resp = volume.VolumeBackup()
            pb_resp = volume.VolumeBackup.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_volume_backup(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_volume_backup_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = volume.VolumeBackup.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.get_volume_backup",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "GetVolumeBackup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetVolumeRestore(
        _BaseBackupForGKERestTransport._BaseGetVolumeRestore, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.GetVolumeRestore")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.GetVolumeRestoreRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> volume.VolumeRestore:
            r"""Call the get volume restore method over HTTP.

            Args:
                request (~.gkebackup.GetVolumeRestoreRequest):
                    The request object. Request message for GetVolumeRestore.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.volume.VolumeRestore:
                    Represents the operation of restoring
                a volume from a VolumeBackup.

            """

            http_options = (
                _BaseBackupForGKERestTransport._BaseGetVolumeRestore._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_volume_restore(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseGetVolumeRestore,
                    "_BaseGetVolumeRestore__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.GetVolumeRestore",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "GetVolumeRestore",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._GetVolumeRestore._get_response(
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
            resp = volume.VolumeRestore()
            pb_resp = volume.VolumeRestore.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_volume_restore(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_volume_restore_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = volume.VolumeRestore.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.get_volume_restore",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "GetVolumeRestore",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListBackupChannels(
        _BaseBackupForGKERestTransport._BaseListBackupChannels, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.ListBackupChannels")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.ListBackupChannelsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gkebackup.ListBackupChannelsResponse:
            r"""Call the list backup channels method over HTTP.

            Args:
                request (~.gkebackup.ListBackupChannelsRequest):
                    The request object. Request message for
                ListBackupChannels.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gkebackup.ListBackupChannelsResponse:
                    Response message for
                ListBackupChannels.

            """

            http_options = _BaseBackupForGKERestTransport._BaseListBackupChannels._get_http_options()
            request, metadata = self._interceptor.pre_list_backup_channels(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseListBackupChannels,
                    "_BaseListBackupChannels__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.ListBackupChannels",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "ListBackupChannels",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._ListBackupChannels._get_response(
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
            resp = gkebackup.ListBackupChannelsResponse()
            pb_resp = gkebackup.ListBackupChannelsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_backup_channels(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_backup_channels_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gkebackup.ListBackupChannelsResponse.to_json(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.list_backup_channels",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "ListBackupChannels",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListBackupPlanBindings(
        _BaseBackupForGKERestTransport._BaseListBackupPlanBindings, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.ListBackupPlanBindings")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.ListBackupPlanBindingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gkebackup.ListBackupPlanBindingsResponse:
            r"""Call the list backup plan bindings method over HTTP.

            Args:
                request (~.gkebackup.ListBackupPlanBindingsRequest):
                    The request object. Request message for
                ListBackupPlanBindings.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gkebackup.ListBackupPlanBindingsResponse:
                    Response message for
                ListBackupPlanBindings.

            """

            http_options = _BaseBackupForGKERestTransport._BaseListBackupPlanBindings._get_http_options()
            request, metadata = self._interceptor.pre_list_backup_plan_bindings(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseListBackupPlanBindings,
                    "_BaseListBackupPlanBindings__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.ListBackupPlanBindings",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "ListBackupPlanBindings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._ListBackupPlanBindings._get_response(
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
            resp = gkebackup.ListBackupPlanBindingsResponse()
            pb_resp = gkebackup.ListBackupPlanBindingsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_backup_plan_bindings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_backup_plan_bindings_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gkebackup.ListBackupPlanBindingsResponse.to_json(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.list_backup_plan_bindings",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "ListBackupPlanBindings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListBackupPlans(
        _BaseBackupForGKERestTransport._BaseListBackupPlans, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.ListBackupPlans")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.ListBackupPlansRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gkebackup.ListBackupPlansResponse:
            r"""Call the list backup plans method over HTTP.

            Args:
                request (~.gkebackup.ListBackupPlansRequest):
                    The request object. Request message for ListBackupPlans.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gkebackup.ListBackupPlansResponse:
                    Response message for ListBackupPlans.
            """

            http_options = (
                _BaseBackupForGKERestTransport._BaseListBackupPlans._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_backup_plans(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseListBackupPlans,
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
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.ListBackupPlans",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "ListBackupPlans",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._ListBackupPlans._get_response(
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
            resp = gkebackup.ListBackupPlansResponse()
            pb_resp = gkebackup.ListBackupPlansResponse.pb(resp)

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
                    response_payload = gkebackup.ListBackupPlansResponse.to_json(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.list_backup_plans",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "ListBackupPlans",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListBackups(
        _BaseBackupForGKERestTransport._BaseListBackups, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.ListBackups")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.ListBackupsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gkebackup.ListBackupsResponse:
            r"""Call the list backups method over HTTP.

            Args:
                request (~.gkebackup.ListBackupsRequest):
                    The request object. Request message for ListBackups.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gkebackup.ListBackupsResponse:
                    Response message for ListBackups.
            """

            http_options = (
                _BaseBackupForGKERestTransport._BaseListBackups._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_backups(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseListBackups,
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
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.ListBackups",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "ListBackups",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._ListBackups._get_response(
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
            resp = gkebackup.ListBackupsResponse()
            pb_resp = gkebackup.ListBackupsResponse.pb(resp)

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
                    response_payload = gkebackup.ListBackupsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.list_backups",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "ListBackups",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListRestoreChannels(
        _BaseBackupForGKERestTransport._BaseListRestoreChannels, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.ListRestoreChannels")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.ListRestoreChannelsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gkebackup.ListRestoreChannelsResponse:
            r"""Call the list restore channels method over HTTP.

            Args:
                request (~.gkebackup.ListRestoreChannelsRequest):
                    The request object. Request message for
                ListRestoreChannels.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gkebackup.ListRestoreChannelsResponse:
                    Response message for
                ListRestoreChannels.

            """

            http_options = _BaseBackupForGKERestTransport._BaseListRestoreChannels._get_http_options()
            request, metadata = self._interceptor.pre_list_restore_channels(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseListRestoreChannels,
                    "_BaseListRestoreChannels__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.ListRestoreChannels",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "ListRestoreChannels",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._ListRestoreChannels._get_response(
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
            resp = gkebackup.ListRestoreChannelsResponse()
            pb_resp = gkebackup.ListRestoreChannelsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_restore_channels(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_restore_channels_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gkebackup.ListRestoreChannelsResponse.to_json(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.list_restore_channels",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "ListRestoreChannels",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListRestorePlanBindings(
        _BaseBackupForGKERestTransport._BaseListRestorePlanBindings,
        BackupForGKERestStub,
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.ListRestorePlanBindings")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.ListRestorePlanBindingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gkebackup.ListRestorePlanBindingsResponse:
            r"""Call the list restore plan
            bindings method over HTTP.

                Args:
                    request (~.gkebackup.ListRestorePlanBindingsRequest):
                        The request object. Request message for
                    ListRestorePlanBindings.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.gkebackup.ListRestorePlanBindingsResponse:
                        Response message for
                    ListRestorePlanBindings.

            """

            http_options = _BaseBackupForGKERestTransport._BaseListRestorePlanBindings._get_http_options()
            request, metadata = self._interceptor.pre_list_restore_plan_bindings(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseListRestorePlanBindings,
                    "_BaseListRestorePlanBindings__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.ListRestorePlanBindings",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "ListRestorePlanBindings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._ListRestorePlanBindings._get_response(
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
            resp = gkebackup.ListRestorePlanBindingsResponse()
            pb_resp = gkebackup.ListRestorePlanBindingsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_restore_plan_bindings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_restore_plan_bindings_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        gkebackup.ListRestorePlanBindingsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.list_restore_plan_bindings",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "ListRestorePlanBindings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListRestorePlans(
        _BaseBackupForGKERestTransport._BaseListRestorePlans, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.ListRestorePlans")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.ListRestorePlansRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gkebackup.ListRestorePlansResponse:
            r"""Call the list restore plans method over HTTP.

            Args:
                request (~.gkebackup.ListRestorePlansRequest):
                    The request object. Request message for ListRestorePlans.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gkebackup.ListRestorePlansResponse:
                    Response message for
                ListRestorePlans.

            """

            http_options = (
                _BaseBackupForGKERestTransport._BaseListRestorePlans._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_restore_plans(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseListRestorePlans,
                    "_BaseListRestorePlans__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.ListRestorePlans",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "ListRestorePlans",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._ListRestorePlans._get_response(
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
            resp = gkebackup.ListRestorePlansResponse()
            pb_resp = gkebackup.ListRestorePlansResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_restore_plans(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_restore_plans_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gkebackup.ListRestorePlansResponse.to_json(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.list_restore_plans",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "ListRestorePlans",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListRestores(
        _BaseBackupForGKERestTransport._BaseListRestores, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.ListRestores")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.ListRestoresRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gkebackup.ListRestoresResponse:
            r"""Call the list restores method over HTTP.

            Args:
                request (~.gkebackup.ListRestoresRequest):
                    The request object. Request message for ListRestores.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gkebackup.ListRestoresResponse:
                    Response message for ListRestores.
            """

            http_options = (
                _BaseBackupForGKERestTransport._BaseListRestores._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_restores(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseListRestores,
                    "_BaseListRestores__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.ListRestores",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "ListRestores",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._ListRestores._get_response(
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
            resp = gkebackup.ListRestoresResponse()
            pb_resp = gkebackup.ListRestoresResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_restores(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_restores_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gkebackup.ListRestoresResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.list_restores",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "ListRestores",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListVolumeBackups(
        _BaseBackupForGKERestTransport._BaseListVolumeBackups, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.ListVolumeBackups")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.ListVolumeBackupsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gkebackup.ListVolumeBackupsResponse:
            r"""Call the list volume backups method over HTTP.

            Args:
                request (~.gkebackup.ListVolumeBackupsRequest):
                    The request object. Request message for
                ListVolumeBackups.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gkebackup.ListVolumeBackupsResponse:
                    Response message for
                ListVolumeBackups.

            """

            http_options = _BaseBackupForGKERestTransport._BaseListVolumeBackups._get_http_options()
            request, metadata = self._interceptor.pre_list_volume_backups(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseListVolumeBackups,
                    "_BaseListVolumeBackups__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.ListVolumeBackups",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "ListVolumeBackups",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._ListVolumeBackups._get_response(
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
            resp = gkebackup.ListVolumeBackupsResponse()
            pb_resp = gkebackup.ListVolumeBackupsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_volume_backups(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_volume_backups_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gkebackup.ListVolumeBackupsResponse.to_json(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.list_volume_backups",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "ListVolumeBackups",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListVolumeRestores(
        _BaseBackupForGKERestTransport._BaseListVolumeRestores, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.ListVolumeRestores")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.ListVolumeRestoresRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gkebackup.ListVolumeRestoresResponse:
            r"""Call the list volume restores method over HTTP.

            Args:
                request (~.gkebackup.ListVolumeRestoresRequest):
                    The request object. Request message for
                ListVolumeRestores.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gkebackup.ListVolumeRestoresResponse:
                    Response message for
                ListVolumeRestores.

            """

            http_options = _BaseBackupForGKERestTransport._BaseListVolumeRestores._get_http_options()
            request, metadata = self._interceptor.pre_list_volume_restores(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseListVolumeRestores,
                    "_BaseListVolumeRestores__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.ListVolumeRestores",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "ListVolumeRestores",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._ListVolumeRestores._get_response(
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
            resp = gkebackup.ListVolumeRestoresResponse()
            pb_resp = gkebackup.ListVolumeRestoresResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_volume_restores(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_volume_restores_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gkebackup.ListVolumeRestoresResponse.to_json(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.list_volume_restores",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "ListVolumeRestores",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateBackup(
        _BaseBackupForGKERestTransport._BaseUpdateBackup, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.UpdateBackup")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.UpdateBackupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update backup method over HTTP.

            Args:
                request (~.gkebackup.UpdateBackupRequest):
                    The request object. Request message for UpdateBackup.
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
                _BaseBackupForGKERestTransport._BaseUpdateBackup._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_backup(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseUpdateBackup,
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
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.UpdateBackup",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "UpdateBackup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._UpdateBackup._get_response(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.update_backup",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "UpdateBackup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateBackupChannel(
        _BaseBackupForGKERestTransport._BaseUpdateBackupChannel, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.UpdateBackupChannel")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.UpdateBackupChannelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update backup channel method over HTTP.

            Args:
                request (~.gkebackup.UpdateBackupChannelRequest):
                    The request object. Request message for
                UpdateBackupChannel.
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

            http_options = _BaseBackupForGKERestTransport._BaseUpdateBackupChannel._get_http_options()
            request, metadata = self._interceptor.pre_update_backup_channel(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseUpdateBackupChannel,
                    "_BaseUpdateBackupChannel__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.UpdateBackupChannel",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "UpdateBackupChannel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._UpdateBackupChannel._get_response(
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

            resp = self._interceptor.post_update_backup_channel(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_backup_channel_with_metadata(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.update_backup_channel",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "UpdateBackupChannel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateBackupPlan(
        _BaseBackupForGKERestTransport._BaseUpdateBackupPlan, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.UpdateBackupPlan")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.UpdateBackupPlanRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update backup plan method over HTTP.

            Args:
                request (~.gkebackup.UpdateBackupPlanRequest):
                    The request object. Request message for UpdateBackupPlan.
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
                _BaseBackupForGKERestTransport._BaseUpdateBackupPlan._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_backup_plan(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseUpdateBackupPlan,
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
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.UpdateBackupPlan",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "UpdateBackupPlan",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._UpdateBackupPlan._get_response(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.update_backup_plan",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "UpdateBackupPlan",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateRestore(
        _BaseBackupForGKERestTransport._BaseUpdateRestore, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.UpdateRestore")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.UpdateRestoreRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update restore method over HTTP.

            Args:
                request (~.gkebackup.UpdateRestoreRequest):
                    The request object. Request message for UpdateRestore.
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
                _BaseBackupForGKERestTransport._BaseUpdateRestore._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_restore(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseUpdateRestore,
                    "_BaseUpdateRestore__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.UpdateRestore",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "UpdateRestore",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._UpdateRestore._get_response(
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

            resp = self._interceptor.post_update_restore(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_restore_with_metadata(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.update_restore",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "UpdateRestore",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateRestoreChannel(
        _BaseBackupForGKERestTransport._BaseUpdateRestoreChannel, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.UpdateRestoreChannel")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.UpdateRestoreChannelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update restore channel method over HTTP.

            Args:
                request (~.gkebackup.UpdateRestoreChannelRequest):
                    The request object. Request message for
                UpdateRestoreChannel.
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

            http_options = _BaseBackupForGKERestTransport._BaseUpdateRestoreChannel._get_http_options()
            request, metadata = self._interceptor.pre_update_restore_channel(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseUpdateRestoreChannel,
                    "_BaseUpdateRestoreChannel__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.UpdateRestoreChannel",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "UpdateRestoreChannel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._UpdateRestoreChannel._get_response(
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

            resp = self._interceptor.post_update_restore_channel(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_restore_channel_with_metadata(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.update_restore_channel",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "UpdateRestoreChannel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateRestorePlan(
        _BaseBackupForGKERestTransport._BaseUpdateRestorePlan, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.UpdateRestorePlan")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: gkebackup.UpdateRestorePlanRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update restore plan method over HTTP.

            Args:
                request (~.gkebackup.UpdateRestorePlanRequest):
                    The request object. Request message for
                UpdateRestorePlan.
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

            http_options = _BaseBackupForGKERestTransport._BaseUpdateRestorePlan._get_http_options()
            request, metadata = self._interceptor.pre_update_restore_plan(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseUpdateRestorePlan,
                    "_BaseUpdateRestorePlan__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.UpdateRestorePlan",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "UpdateRestorePlan",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._UpdateRestorePlan._get_response(
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

            resp = self._interceptor.post_update_restore_plan(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_restore_plan_with_metadata(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEClient.update_restore_plan",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "UpdateRestorePlan",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_backup(
        self,
    ) -> Callable[[gkebackup.CreateBackupRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateBackup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_backup_channel(
        self,
    ) -> Callable[[gkebackup.CreateBackupChannelRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateBackupChannel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_backup_plan(
        self,
    ) -> Callable[[gkebackup.CreateBackupPlanRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateBackupPlan(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_restore(
        self,
    ) -> Callable[[gkebackup.CreateRestoreRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateRestore(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_restore_channel(
        self,
    ) -> Callable[[gkebackup.CreateRestoreChannelRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateRestoreChannel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_restore_plan(
        self,
    ) -> Callable[[gkebackup.CreateRestorePlanRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateRestorePlan(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_backup(
        self,
    ) -> Callable[[gkebackup.DeleteBackupRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteBackup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_backup_channel(
        self,
    ) -> Callable[[gkebackup.DeleteBackupChannelRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteBackupChannel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_backup_plan(
        self,
    ) -> Callable[[gkebackup.DeleteBackupPlanRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteBackupPlan(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_restore(
        self,
    ) -> Callable[[gkebackup.DeleteRestoreRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteRestore(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_restore_channel(
        self,
    ) -> Callable[[gkebackup.DeleteRestoreChannelRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteRestoreChannel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_restore_plan(
        self,
    ) -> Callable[[gkebackup.DeleteRestorePlanRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteRestorePlan(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_backup(self) -> Callable[[gkebackup.GetBackupRequest], backup.Backup]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetBackup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_backup_channel(
        self,
    ) -> Callable[[gkebackup.GetBackupChannelRequest], backup_channel.BackupChannel]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetBackupChannel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_backup_index_download_url(
        self,
    ) -> Callable[
        [gkebackup.GetBackupIndexDownloadUrlRequest],
        gkebackup.GetBackupIndexDownloadUrlResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetBackupIndexDownloadUrl(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_backup_plan(
        self,
    ) -> Callable[[gkebackup.GetBackupPlanRequest], backup_plan.BackupPlan]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetBackupPlan(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_backup_plan_binding(
        self,
    ) -> Callable[
        [gkebackup.GetBackupPlanBindingRequest], backup_plan_binding.BackupPlanBinding
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetBackupPlanBinding(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_restore(self) -> Callable[[gkebackup.GetRestoreRequest], restore.Restore]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetRestore(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_restore_channel(
        self,
    ) -> Callable[[gkebackup.GetRestoreChannelRequest], restore_channel.RestoreChannel]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetRestoreChannel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_restore_plan(
        self,
    ) -> Callable[[gkebackup.GetRestorePlanRequest], restore_plan.RestorePlan]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetRestorePlan(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_restore_plan_binding(
        self,
    ) -> Callable[
        [gkebackup.GetRestorePlanBindingRequest],
        restore_plan_binding.RestorePlanBinding,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetRestorePlanBinding(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_volume_backup(
        self,
    ) -> Callable[[gkebackup.GetVolumeBackupRequest], volume.VolumeBackup]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetVolumeBackup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_volume_restore(
        self,
    ) -> Callable[[gkebackup.GetVolumeRestoreRequest], volume.VolumeRestore]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetVolumeRestore(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_backup_channels(
        self,
    ) -> Callable[
        [gkebackup.ListBackupChannelsRequest], gkebackup.ListBackupChannelsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListBackupChannels(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_backup_plan_bindings(
        self,
    ) -> Callable[
        [gkebackup.ListBackupPlanBindingsRequest],
        gkebackup.ListBackupPlanBindingsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListBackupPlanBindings(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_backup_plans(
        self,
    ) -> Callable[
        [gkebackup.ListBackupPlansRequest], gkebackup.ListBackupPlansResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListBackupPlans(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_backups(
        self,
    ) -> Callable[[gkebackup.ListBackupsRequest], gkebackup.ListBackupsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListBackups(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_restore_channels(
        self,
    ) -> Callable[
        [gkebackup.ListRestoreChannelsRequest], gkebackup.ListRestoreChannelsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListRestoreChannels(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_restore_plan_bindings(
        self,
    ) -> Callable[
        [gkebackup.ListRestorePlanBindingsRequest],
        gkebackup.ListRestorePlanBindingsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListRestorePlanBindings(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_restore_plans(
        self,
    ) -> Callable[
        [gkebackup.ListRestorePlansRequest], gkebackup.ListRestorePlansResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListRestorePlans(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_restores(
        self,
    ) -> Callable[[gkebackup.ListRestoresRequest], gkebackup.ListRestoresResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListRestores(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_volume_backups(
        self,
    ) -> Callable[
        [gkebackup.ListVolumeBackupsRequest], gkebackup.ListVolumeBackupsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListVolumeBackups(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_volume_restores(
        self,
    ) -> Callable[
        [gkebackup.ListVolumeRestoresRequest], gkebackup.ListVolumeRestoresResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListVolumeRestores(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_backup(
        self,
    ) -> Callable[[gkebackup.UpdateBackupRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateBackup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_backup_channel(
        self,
    ) -> Callable[[gkebackup.UpdateBackupChannelRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateBackupChannel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_backup_plan(
        self,
    ) -> Callable[[gkebackup.UpdateBackupPlanRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateBackupPlan(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_restore(
        self,
    ) -> Callable[[gkebackup.UpdateRestoreRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateRestore(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_restore_channel(
        self,
    ) -> Callable[[gkebackup.UpdateRestoreChannelRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateRestoreChannel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_restore_plan(
        self,
    ) -> Callable[[gkebackup.UpdateRestorePlanRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateRestorePlan(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseBackupForGKERestTransport._BaseGetLocation, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.GetLocation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseBackupForGKERestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
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
        _BaseBackupForGKERestTransport._BaseListLocations, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.ListLocations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseBackupForGKERestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "ListLocations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def get_iam_policy(self):
        return self._GetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _GetIamPolicy(
        _BaseBackupForGKERestTransport._BaseGetIamPolicy, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.GetIamPolicy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseBackupForGKERestTransport._BaseGetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseGetIamPolicy,
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
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._GetIamPolicy._get_response(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEAsyncClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "GetIamPolicy",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def set_iam_policy(self):
        return self._SetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _SetIamPolicy(
        _BaseBackupForGKERestTransport._BaseSetIamPolicy, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.SetIamPolicy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseBackupForGKERestTransport._BaseSetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseSetIamPolicy,
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
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._SetIamPolicy._get_response(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEAsyncClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
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
        _BaseBackupForGKERestTransport._BaseTestIamPermissions, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.TestIamPermissions")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseBackupForGKERestTransport._BaseTestIamPermissions._get_http_options()
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseTestIamPermissions,
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
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._TestIamPermissions._get_response(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEAsyncClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
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
        _BaseBackupForGKERestTransport._BaseCancelOperation, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.CancelOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseBackupForGKERestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._CancelOperation._get_response(
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
        _BaseBackupForGKERestTransport._BaseDeleteOperation, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.DeleteOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseBackupForGKERestTransport._BaseDeleteOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._DeleteOperation._get_response(
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
        _BaseBackupForGKERestTransport._BaseGetOperation, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.GetOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseBackupForGKERestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
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
        _BaseBackupForGKERestTransport._BaseListOperations, BackupForGKERestStub
    ):
        def __hash__(self):
            return hash("BackupForGKERestTransport.ListOperations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseBackupForGKERestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBackupForGKERestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.gkebackup_v1.BackupForGKEClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BackupForGKERestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.gkebackup_v1.BackupForGKEAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.gkebackup.v1.BackupForGKE",
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


__all__ = ("BackupForGKERestTransport",)
