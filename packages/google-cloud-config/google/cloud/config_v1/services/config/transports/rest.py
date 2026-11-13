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

from google.cloud.config_v1._compat import transcode_request
from google.cloud.config_v1.types import config

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseConfigRestTransport

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


class ConfigRestInterceptor:
    """Interceptor for Config.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ConfigRestTransport.

    .. code-block:: python
        class MyCustomConfigInterceptor(ConfigRestInterceptor):
            def pre_create_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_deployment_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_deployment_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_preview(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_preview(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_deployment_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_deployment_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_preview(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_preview(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_statefile(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_deprovision_deployment_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_deprovision_deployment_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_export_deployment_statefile(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export_deployment_statefile(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_export_lock_info(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export_lock_info(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_export_preview_result(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export_preview_result(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_export_revision_statefile(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export_revision_statefile(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_auto_migration_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_auto_migration_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_deployment_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_deployment_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_deployment_group_revision(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_deployment_group_revision(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_preview(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_preview(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_resource(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_resource(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_resource_change(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_resource_change(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_resource_drift(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_resource_drift(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_revision(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_revision(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_terraform_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_terraform_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_import_statefile(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_import_statefile(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_deployment_group_revisions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_deployment_group_revisions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_deployment_groups(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_deployment_groups(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_deployments(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_deployments(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_previews(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_previews(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_resource_changes(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_resource_changes(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_resource_drifts(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_resource_drifts(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_resources(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_resources(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_revisions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_revisions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_terraform_versions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_terraform_versions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_lock_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_lock_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_provision_deployment_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_provision_deployment_group(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_unlock_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_unlock_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_auto_migration_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_auto_migration_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_deployment(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_deployment(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_deployment_group(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_deployment_group(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ConfigRestTransport(interceptor=MyCustomConfigInterceptor())
        client = ConfigClient(transport=transport)


    """

    def pre_create_deployment(
        self,
        request: config.CreateDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.CreateDeploymentRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_create_deployment(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_deployment

        DEPRECATED. Please use the `post_create_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_create_deployment` interceptor runs
        before the `post_create_deployment_with_metadata` interceptor.
        """
        return response

    def post_create_deployment_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_create_deployment_with_metadata`
        interceptor in new development instead of the `post_create_deployment` interceptor.
        When both interceptors are used, this `post_create_deployment_with_metadata` interceptor runs after the
        `post_create_deployment` interceptor. The (possibly modified) response returned by
        `post_create_deployment` will be passed to
        `post_create_deployment_with_metadata`.
        """
        return response, metadata

    def pre_create_deployment_group(
        self,
        request: config.CreateDeploymentGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config.CreateDeploymentGroupRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_deployment_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_create_deployment_group(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_deployment_group

        DEPRECATED. Please use the `post_create_deployment_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_create_deployment_group` interceptor runs
        before the `post_create_deployment_group_with_metadata` interceptor.
        """
        return response

    def post_create_deployment_group_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_deployment_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_create_deployment_group_with_metadata`
        interceptor in new development instead of the `post_create_deployment_group` interceptor.
        When both interceptors are used, this `post_create_deployment_group_with_metadata` interceptor runs after the
        `post_create_deployment_group` interceptor. The (possibly modified) response returned by
        `post_create_deployment_group` will be passed to
        `post_create_deployment_group_with_metadata`.
        """
        return response, metadata

    def pre_create_preview(
        self,
        request: config.CreatePreviewRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.CreatePreviewRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_preview

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_create_preview(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_preview

        DEPRECATED. Please use the `post_create_preview_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_create_preview` interceptor runs
        before the `post_create_preview_with_metadata` interceptor.
        """
        return response

    def post_create_preview_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_preview

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_create_preview_with_metadata`
        interceptor in new development instead of the `post_create_preview` interceptor.
        When both interceptors are used, this `post_create_preview_with_metadata` interceptor runs after the
        `post_create_preview` interceptor. The (possibly modified) response returned by
        `post_create_preview` will be passed to
        `post_create_preview_with_metadata`.
        """
        return response, metadata

    def pre_delete_deployment(
        self,
        request: config.DeleteDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.DeleteDeploymentRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_delete_deployment(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_deployment

        DEPRECATED. Please use the `post_delete_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_delete_deployment` interceptor runs
        before the `post_delete_deployment_with_metadata` interceptor.
        """
        return response

    def post_delete_deployment_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_delete_deployment_with_metadata`
        interceptor in new development instead of the `post_delete_deployment` interceptor.
        When both interceptors are used, this `post_delete_deployment_with_metadata` interceptor runs after the
        `post_delete_deployment` interceptor. The (possibly modified) response returned by
        `post_delete_deployment` will be passed to
        `post_delete_deployment_with_metadata`.
        """
        return response, metadata

    def pre_delete_deployment_group(
        self,
        request: config.DeleteDeploymentGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config.DeleteDeploymentGroupRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_deployment_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_delete_deployment_group(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_deployment_group

        DEPRECATED. Please use the `post_delete_deployment_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_delete_deployment_group` interceptor runs
        before the `post_delete_deployment_group_with_metadata` interceptor.
        """
        return response

    def post_delete_deployment_group_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_deployment_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_delete_deployment_group_with_metadata`
        interceptor in new development instead of the `post_delete_deployment_group` interceptor.
        When both interceptors are used, this `post_delete_deployment_group_with_metadata` interceptor runs after the
        `post_delete_deployment_group` interceptor. The (possibly modified) response returned by
        `post_delete_deployment_group` will be passed to
        `post_delete_deployment_group_with_metadata`.
        """
        return response, metadata

    def pre_delete_preview(
        self,
        request: config.DeletePreviewRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.DeletePreviewRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_preview

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_delete_preview(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_preview

        DEPRECATED. Please use the `post_delete_preview_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_delete_preview` interceptor runs
        before the `post_delete_preview_with_metadata` interceptor.
        """
        return response

    def post_delete_preview_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_preview

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_delete_preview_with_metadata`
        interceptor in new development instead of the `post_delete_preview` interceptor.
        When both interceptors are used, this `post_delete_preview_with_metadata` interceptor runs after the
        `post_delete_preview` interceptor. The (possibly modified) response returned by
        `post_delete_preview` will be passed to
        `post_delete_preview_with_metadata`.
        """
        return response, metadata

    def pre_delete_statefile(
        self,
        request: config.DeleteStatefileRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.DeleteStatefileRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_statefile

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def pre_deprovision_deployment_group(
        self,
        request: config.DeprovisionDeploymentGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config.DeprovisionDeploymentGroupRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for deprovision_deployment_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_deprovision_deployment_group(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for deprovision_deployment_group

        DEPRECATED. Please use the `post_deprovision_deployment_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_deprovision_deployment_group` interceptor runs
        before the `post_deprovision_deployment_group_with_metadata` interceptor.
        """
        return response

    def post_deprovision_deployment_group_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for deprovision_deployment_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_deprovision_deployment_group_with_metadata`
        interceptor in new development instead of the `post_deprovision_deployment_group` interceptor.
        When both interceptors are used, this `post_deprovision_deployment_group_with_metadata` interceptor runs after the
        `post_deprovision_deployment_group` interceptor. The (possibly modified) response returned by
        `post_deprovision_deployment_group` will be passed to
        `post_deprovision_deployment_group_with_metadata`.
        """
        return response, metadata

    def pre_export_deployment_statefile(
        self,
        request: config.ExportDeploymentStatefileRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config.ExportDeploymentStatefileRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for export_deployment_statefile

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_export_deployment_statefile(
        self, response: config.Statefile
    ) -> config.Statefile:
        """Post-rpc interceptor for export_deployment_statefile

        DEPRECATED. Please use the `post_export_deployment_statefile_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_export_deployment_statefile` interceptor runs
        before the `post_export_deployment_statefile_with_metadata` interceptor.
        """
        return response

    def post_export_deployment_statefile_with_metadata(
        self,
        response: config.Statefile,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.Statefile, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for export_deployment_statefile

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_export_deployment_statefile_with_metadata`
        interceptor in new development instead of the `post_export_deployment_statefile` interceptor.
        When both interceptors are used, this `post_export_deployment_statefile_with_metadata` interceptor runs after the
        `post_export_deployment_statefile` interceptor. The (possibly modified) response returned by
        `post_export_deployment_statefile` will be passed to
        `post_export_deployment_statefile_with_metadata`.
        """
        return response, metadata

    def pre_export_lock_info(
        self,
        request: config.ExportLockInfoRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.ExportLockInfoRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for export_lock_info

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_export_lock_info(self, response: config.LockInfo) -> config.LockInfo:
        """Post-rpc interceptor for export_lock_info

        DEPRECATED. Please use the `post_export_lock_info_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_export_lock_info` interceptor runs
        before the `post_export_lock_info_with_metadata` interceptor.
        """
        return response

    def post_export_lock_info_with_metadata(
        self,
        response: config.LockInfo,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.LockInfo, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for export_lock_info

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_export_lock_info_with_metadata`
        interceptor in new development instead of the `post_export_lock_info` interceptor.
        When both interceptors are used, this `post_export_lock_info_with_metadata` interceptor runs after the
        `post_export_lock_info` interceptor. The (possibly modified) response returned by
        `post_export_lock_info` will be passed to
        `post_export_lock_info_with_metadata`.
        """
        return response, metadata

    def pre_export_preview_result(
        self,
        request: config.ExportPreviewResultRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config.ExportPreviewResultRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for export_preview_result

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_export_preview_result(
        self, response: config.ExportPreviewResultResponse
    ) -> config.ExportPreviewResultResponse:
        """Post-rpc interceptor for export_preview_result

        DEPRECATED. Please use the `post_export_preview_result_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_export_preview_result` interceptor runs
        before the `post_export_preview_result_with_metadata` interceptor.
        """
        return response

    def post_export_preview_result_with_metadata(
        self,
        response: config.ExportPreviewResultResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config.ExportPreviewResultResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for export_preview_result

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_export_preview_result_with_metadata`
        interceptor in new development instead of the `post_export_preview_result` interceptor.
        When both interceptors are used, this `post_export_preview_result_with_metadata` interceptor runs after the
        `post_export_preview_result` interceptor. The (possibly modified) response returned by
        `post_export_preview_result` will be passed to
        `post_export_preview_result_with_metadata`.
        """
        return response, metadata

    def pre_export_revision_statefile(
        self,
        request: config.ExportRevisionStatefileRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config.ExportRevisionStatefileRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for export_revision_statefile

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_export_revision_statefile(
        self, response: config.Statefile
    ) -> config.Statefile:
        """Post-rpc interceptor for export_revision_statefile

        DEPRECATED. Please use the `post_export_revision_statefile_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_export_revision_statefile` interceptor runs
        before the `post_export_revision_statefile_with_metadata` interceptor.
        """
        return response

    def post_export_revision_statefile_with_metadata(
        self,
        response: config.Statefile,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.Statefile, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for export_revision_statefile

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_export_revision_statefile_with_metadata`
        interceptor in new development instead of the `post_export_revision_statefile` interceptor.
        When both interceptors are used, this `post_export_revision_statefile_with_metadata` interceptor runs after the
        `post_export_revision_statefile` interceptor. The (possibly modified) response returned by
        `post_export_revision_statefile` will be passed to
        `post_export_revision_statefile_with_metadata`.
        """
        return response, metadata

    def pre_get_auto_migration_config(
        self,
        request: config.GetAutoMigrationConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config.GetAutoMigrationConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_auto_migration_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_get_auto_migration_config(
        self, response: config.AutoMigrationConfig
    ) -> config.AutoMigrationConfig:
        """Post-rpc interceptor for get_auto_migration_config

        DEPRECATED. Please use the `post_get_auto_migration_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_get_auto_migration_config` interceptor runs
        before the `post_get_auto_migration_config_with_metadata` interceptor.
        """
        return response

    def post_get_auto_migration_config_with_metadata(
        self,
        response: config.AutoMigrationConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.AutoMigrationConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_auto_migration_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_get_auto_migration_config_with_metadata`
        interceptor in new development instead of the `post_get_auto_migration_config` interceptor.
        When both interceptors are used, this `post_get_auto_migration_config_with_metadata` interceptor runs after the
        `post_get_auto_migration_config` interceptor. The (possibly modified) response returned by
        `post_get_auto_migration_config` will be passed to
        `post_get_auto_migration_config_with_metadata`.
        """
        return response, metadata

    def pre_get_deployment(
        self,
        request: config.GetDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.GetDeploymentRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_get_deployment(self, response: config.Deployment) -> config.Deployment:
        """Post-rpc interceptor for get_deployment

        DEPRECATED. Please use the `post_get_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_get_deployment` interceptor runs
        before the `post_get_deployment_with_metadata` interceptor.
        """
        return response

    def post_get_deployment_with_metadata(
        self,
        response: config.Deployment,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.Deployment, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_get_deployment_with_metadata`
        interceptor in new development instead of the `post_get_deployment` interceptor.
        When both interceptors are used, this `post_get_deployment_with_metadata` interceptor runs after the
        `post_get_deployment` interceptor. The (possibly modified) response returned by
        `post_get_deployment` will be passed to
        `post_get_deployment_with_metadata`.
        """
        return response, metadata

    def pre_get_deployment_group(
        self,
        request: config.GetDeploymentGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config.GetDeploymentGroupRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_deployment_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_get_deployment_group(
        self, response: config.DeploymentGroup
    ) -> config.DeploymentGroup:
        """Post-rpc interceptor for get_deployment_group

        DEPRECATED. Please use the `post_get_deployment_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_get_deployment_group` interceptor runs
        before the `post_get_deployment_group_with_metadata` interceptor.
        """
        return response

    def post_get_deployment_group_with_metadata(
        self,
        response: config.DeploymentGroup,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.DeploymentGroup, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_deployment_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_get_deployment_group_with_metadata`
        interceptor in new development instead of the `post_get_deployment_group` interceptor.
        When both interceptors are used, this `post_get_deployment_group_with_metadata` interceptor runs after the
        `post_get_deployment_group` interceptor. The (possibly modified) response returned by
        `post_get_deployment_group` will be passed to
        `post_get_deployment_group_with_metadata`.
        """
        return response, metadata

    def pre_get_deployment_group_revision(
        self,
        request: config.GetDeploymentGroupRevisionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config.GetDeploymentGroupRevisionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_deployment_group_revision

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_get_deployment_group_revision(
        self, response: config.DeploymentGroupRevision
    ) -> config.DeploymentGroupRevision:
        """Post-rpc interceptor for get_deployment_group_revision

        DEPRECATED. Please use the `post_get_deployment_group_revision_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_get_deployment_group_revision` interceptor runs
        before the `post_get_deployment_group_revision_with_metadata` interceptor.
        """
        return response

    def post_get_deployment_group_revision_with_metadata(
        self,
        response: config.DeploymentGroupRevision,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.DeploymentGroupRevision, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_deployment_group_revision

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_get_deployment_group_revision_with_metadata`
        interceptor in new development instead of the `post_get_deployment_group_revision` interceptor.
        When both interceptors are used, this `post_get_deployment_group_revision_with_metadata` interceptor runs after the
        `post_get_deployment_group_revision` interceptor. The (possibly modified) response returned by
        `post_get_deployment_group_revision` will be passed to
        `post_get_deployment_group_revision_with_metadata`.
        """
        return response, metadata

    def pre_get_preview(
        self,
        request: config.GetPreviewRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.GetPreviewRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_preview

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_get_preview(self, response: config.Preview) -> config.Preview:
        """Post-rpc interceptor for get_preview

        DEPRECATED. Please use the `post_get_preview_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_get_preview` interceptor runs
        before the `post_get_preview_with_metadata` interceptor.
        """
        return response

    def post_get_preview_with_metadata(
        self,
        response: config.Preview,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.Preview, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_preview

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_get_preview_with_metadata`
        interceptor in new development instead of the `post_get_preview` interceptor.
        When both interceptors are used, this `post_get_preview_with_metadata` interceptor runs after the
        `post_get_preview` interceptor. The (possibly modified) response returned by
        `post_get_preview` will be passed to
        `post_get_preview_with_metadata`.
        """
        return response, metadata

    def pre_get_resource(
        self,
        request: config.GetResourceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.GetResourceRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_resource

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_get_resource(self, response: config.Resource) -> config.Resource:
        """Post-rpc interceptor for get_resource

        DEPRECATED. Please use the `post_get_resource_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_get_resource` interceptor runs
        before the `post_get_resource_with_metadata` interceptor.
        """
        return response

    def post_get_resource_with_metadata(
        self,
        response: config.Resource,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.Resource, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_resource

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_get_resource_with_metadata`
        interceptor in new development instead of the `post_get_resource` interceptor.
        When both interceptors are used, this `post_get_resource_with_metadata` interceptor runs after the
        `post_get_resource` interceptor. The (possibly modified) response returned by
        `post_get_resource` will be passed to
        `post_get_resource_with_metadata`.
        """
        return response, metadata

    def pre_get_resource_change(
        self,
        request: config.GetResourceChangeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config.GetResourceChangeRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_resource_change

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_get_resource_change(
        self, response: config.ResourceChange
    ) -> config.ResourceChange:
        """Post-rpc interceptor for get_resource_change

        DEPRECATED. Please use the `post_get_resource_change_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_get_resource_change` interceptor runs
        before the `post_get_resource_change_with_metadata` interceptor.
        """
        return response

    def post_get_resource_change_with_metadata(
        self,
        response: config.ResourceChange,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.ResourceChange, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_resource_change

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_get_resource_change_with_metadata`
        interceptor in new development instead of the `post_get_resource_change` interceptor.
        When both interceptors are used, this `post_get_resource_change_with_metadata` interceptor runs after the
        `post_get_resource_change` interceptor. The (possibly modified) response returned by
        `post_get_resource_change` will be passed to
        `post_get_resource_change_with_metadata`.
        """
        return response, metadata

    def pre_get_resource_drift(
        self,
        request: config.GetResourceDriftRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.GetResourceDriftRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_resource_drift

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_get_resource_drift(
        self, response: config.ResourceDrift
    ) -> config.ResourceDrift:
        """Post-rpc interceptor for get_resource_drift

        DEPRECATED. Please use the `post_get_resource_drift_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_get_resource_drift` interceptor runs
        before the `post_get_resource_drift_with_metadata` interceptor.
        """
        return response

    def post_get_resource_drift_with_metadata(
        self,
        response: config.ResourceDrift,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.ResourceDrift, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_resource_drift

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_get_resource_drift_with_metadata`
        interceptor in new development instead of the `post_get_resource_drift` interceptor.
        When both interceptors are used, this `post_get_resource_drift_with_metadata` interceptor runs after the
        `post_get_resource_drift` interceptor. The (possibly modified) response returned by
        `post_get_resource_drift` will be passed to
        `post_get_resource_drift_with_metadata`.
        """
        return response, metadata

    def pre_get_revision(
        self,
        request: config.GetRevisionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.GetRevisionRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_revision

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_get_revision(self, response: config.Revision) -> config.Revision:
        """Post-rpc interceptor for get_revision

        DEPRECATED. Please use the `post_get_revision_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_get_revision` interceptor runs
        before the `post_get_revision_with_metadata` interceptor.
        """
        return response

    def post_get_revision_with_metadata(
        self,
        response: config.Revision,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.Revision, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_revision

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_get_revision_with_metadata`
        interceptor in new development instead of the `post_get_revision` interceptor.
        When both interceptors are used, this `post_get_revision_with_metadata` interceptor runs after the
        `post_get_revision` interceptor. The (possibly modified) response returned by
        `post_get_revision` will be passed to
        `post_get_revision_with_metadata`.
        """
        return response, metadata

    def pre_get_terraform_version(
        self,
        request: config.GetTerraformVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config.GetTerraformVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_terraform_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_get_terraform_version(
        self, response: config.TerraformVersion
    ) -> config.TerraformVersion:
        """Post-rpc interceptor for get_terraform_version

        DEPRECATED. Please use the `post_get_terraform_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_get_terraform_version` interceptor runs
        before the `post_get_terraform_version_with_metadata` interceptor.
        """
        return response

    def post_get_terraform_version_with_metadata(
        self,
        response: config.TerraformVersion,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.TerraformVersion, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_terraform_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_get_terraform_version_with_metadata`
        interceptor in new development instead of the `post_get_terraform_version` interceptor.
        When both interceptors are used, this `post_get_terraform_version_with_metadata` interceptor runs after the
        `post_get_terraform_version` interceptor. The (possibly modified) response returned by
        `post_get_terraform_version` will be passed to
        `post_get_terraform_version_with_metadata`.
        """
        return response, metadata

    def pre_import_statefile(
        self,
        request: config.ImportStatefileRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.ImportStatefileRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for import_statefile

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_import_statefile(self, response: config.Statefile) -> config.Statefile:
        """Post-rpc interceptor for import_statefile

        DEPRECATED. Please use the `post_import_statefile_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_import_statefile` interceptor runs
        before the `post_import_statefile_with_metadata` interceptor.
        """
        return response

    def post_import_statefile_with_metadata(
        self,
        response: config.Statefile,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.Statefile, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for import_statefile

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_import_statefile_with_metadata`
        interceptor in new development instead of the `post_import_statefile` interceptor.
        When both interceptors are used, this `post_import_statefile_with_metadata` interceptor runs after the
        `post_import_statefile` interceptor. The (possibly modified) response returned by
        `post_import_statefile` will be passed to
        `post_import_statefile_with_metadata`.
        """
        return response, metadata

    def pre_list_deployment_group_revisions(
        self,
        request: config.ListDeploymentGroupRevisionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config.ListDeploymentGroupRevisionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_deployment_group_revisions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_list_deployment_group_revisions(
        self, response: config.ListDeploymentGroupRevisionsResponse
    ) -> config.ListDeploymentGroupRevisionsResponse:
        """Post-rpc interceptor for list_deployment_group_revisions

        DEPRECATED. Please use the `post_list_deployment_group_revisions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_list_deployment_group_revisions` interceptor runs
        before the `post_list_deployment_group_revisions_with_metadata` interceptor.
        """
        return response

    def post_list_deployment_group_revisions_with_metadata(
        self,
        response: config.ListDeploymentGroupRevisionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config.ListDeploymentGroupRevisionsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_deployment_group_revisions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_list_deployment_group_revisions_with_metadata`
        interceptor in new development instead of the `post_list_deployment_group_revisions` interceptor.
        When both interceptors are used, this `post_list_deployment_group_revisions_with_metadata` interceptor runs after the
        `post_list_deployment_group_revisions` interceptor. The (possibly modified) response returned by
        `post_list_deployment_group_revisions` will be passed to
        `post_list_deployment_group_revisions_with_metadata`.
        """
        return response, metadata

    def pre_list_deployment_groups(
        self,
        request: config.ListDeploymentGroupsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config.ListDeploymentGroupsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_deployment_groups

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_list_deployment_groups(
        self, response: config.ListDeploymentGroupsResponse
    ) -> config.ListDeploymentGroupsResponse:
        """Post-rpc interceptor for list_deployment_groups

        DEPRECATED. Please use the `post_list_deployment_groups_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_list_deployment_groups` interceptor runs
        before the `post_list_deployment_groups_with_metadata` interceptor.
        """
        return response

    def post_list_deployment_groups_with_metadata(
        self,
        response: config.ListDeploymentGroupsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config.ListDeploymentGroupsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_deployment_groups

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_list_deployment_groups_with_metadata`
        interceptor in new development instead of the `post_list_deployment_groups` interceptor.
        When both interceptors are used, this `post_list_deployment_groups_with_metadata` interceptor runs after the
        `post_list_deployment_groups` interceptor. The (possibly modified) response returned by
        `post_list_deployment_groups` will be passed to
        `post_list_deployment_groups_with_metadata`.
        """
        return response, metadata

    def pre_list_deployments(
        self,
        request: config.ListDeploymentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.ListDeploymentsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_deployments

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_list_deployments(
        self, response: config.ListDeploymentsResponse
    ) -> config.ListDeploymentsResponse:
        """Post-rpc interceptor for list_deployments

        DEPRECATED. Please use the `post_list_deployments_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_list_deployments` interceptor runs
        before the `post_list_deployments_with_metadata` interceptor.
        """
        return response

    def post_list_deployments_with_metadata(
        self,
        response: config.ListDeploymentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.ListDeploymentsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_deployments

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_list_deployments_with_metadata`
        interceptor in new development instead of the `post_list_deployments` interceptor.
        When both interceptors are used, this `post_list_deployments_with_metadata` interceptor runs after the
        `post_list_deployments` interceptor. The (possibly modified) response returned by
        `post_list_deployments` will be passed to
        `post_list_deployments_with_metadata`.
        """
        return response, metadata

    def pre_list_previews(
        self,
        request: config.ListPreviewsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.ListPreviewsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_previews

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_list_previews(
        self, response: config.ListPreviewsResponse
    ) -> config.ListPreviewsResponse:
        """Post-rpc interceptor for list_previews

        DEPRECATED. Please use the `post_list_previews_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_list_previews` interceptor runs
        before the `post_list_previews_with_metadata` interceptor.
        """
        return response

    def post_list_previews_with_metadata(
        self,
        response: config.ListPreviewsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.ListPreviewsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_previews

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_list_previews_with_metadata`
        interceptor in new development instead of the `post_list_previews` interceptor.
        When both interceptors are used, this `post_list_previews_with_metadata` interceptor runs after the
        `post_list_previews` interceptor. The (possibly modified) response returned by
        `post_list_previews` will be passed to
        `post_list_previews_with_metadata`.
        """
        return response, metadata

    def pre_list_resource_changes(
        self,
        request: config.ListResourceChangesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config.ListResourceChangesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_resource_changes

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_list_resource_changes(
        self, response: config.ListResourceChangesResponse
    ) -> config.ListResourceChangesResponse:
        """Post-rpc interceptor for list_resource_changes

        DEPRECATED. Please use the `post_list_resource_changes_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_list_resource_changes` interceptor runs
        before the `post_list_resource_changes_with_metadata` interceptor.
        """
        return response

    def post_list_resource_changes_with_metadata(
        self,
        response: config.ListResourceChangesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config.ListResourceChangesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_resource_changes

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_list_resource_changes_with_metadata`
        interceptor in new development instead of the `post_list_resource_changes` interceptor.
        When both interceptors are used, this `post_list_resource_changes_with_metadata` interceptor runs after the
        `post_list_resource_changes` interceptor. The (possibly modified) response returned by
        `post_list_resource_changes` will be passed to
        `post_list_resource_changes_with_metadata`.
        """
        return response, metadata

    def pre_list_resource_drifts(
        self,
        request: config.ListResourceDriftsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config.ListResourceDriftsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_resource_drifts

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_list_resource_drifts(
        self, response: config.ListResourceDriftsResponse
    ) -> config.ListResourceDriftsResponse:
        """Post-rpc interceptor for list_resource_drifts

        DEPRECATED. Please use the `post_list_resource_drifts_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_list_resource_drifts` interceptor runs
        before the `post_list_resource_drifts_with_metadata` interceptor.
        """
        return response

    def post_list_resource_drifts_with_metadata(
        self,
        response: config.ListResourceDriftsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config.ListResourceDriftsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_resource_drifts

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_list_resource_drifts_with_metadata`
        interceptor in new development instead of the `post_list_resource_drifts` interceptor.
        When both interceptors are used, this `post_list_resource_drifts_with_metadata` interceptor runs after the
        `post_list_resource_drifts` interceptor. The (possibly modified) response returned by
        `post_list_resource_drifts` will be passed to
        `post_list_resource_drifts_with_metadata`.
        """
        return response, metadata

    def pre_list_resources(
        self,
        request: config.ListResourcesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.ListResourcesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_resources

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_list_resources(
        self, response: config.ListResourcesResponse
    ) -> config.ListResourcesResponse:
        """Post-rpc interceptor for list_resources

        DEPRECATED. Please use the `post_list_resources_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_list_resources` interceptor runs
        before the `post_list_resources_with_metadata` interceptor.
        """
        return response

    def post_list_resources_with_metadata(
        self,
        response: config.ListResourcesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.ListResourcesResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_resources

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_list_resources_with_metadata`
        interceptor in new development instead of the `post_list_resources` interceptor.
        When both interceptors are used, this `post_list_resources_with_metadata` interceptor runs after the
        `post_list_resources` interceptor. The (possibly modified) response returned by
        `post_list_resources` will be passed to
        `post_list_resources_with_metadata`.
        """
        return response, metadata

    def pre_list_revisions(
        self,
        request: config.ListRevisionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.ListRevisionsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_revisions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_list_revisions(
        self, response: config.ListRevisionsResponse
    ) -> config.ListRevisionsResponse:
        """Post-rpc interceptor for list_revisions

        DEPRECATED. Please use the `post_list_revisions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_list_revisions` interceptor runs
        before the `post_list_revisions_with_metadata` interceptor.
        """
        return response

    def post_list_revisions_with_metadata(
        self,
        response: config.ListRevisionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.ListRevisionsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_revisions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_list_revisions_with_metadata`
        interceptor in new development instead of the `post_list_revisions` interceptor.
        When both interceptors are used, this `post_list_revisions_with_metadata` interceptor runs after the
        `post_list_revisions` interceptor. The (possibly modified) response returned by
        `post_list_revisions` will be passed to
        `post_list_revisions_with_metadata`.
        """
        return response, metadata

    def pre_list_terraform_versions(
        self,
        request: config.ListTerraformVersionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config.ListTerraformVersionsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_terraform_versions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_list_terraform_versions(
        self, response: config.ListTerraformVersionsResponse
    ) -> config.ListTerraformVersionsResponse:
        """Post-rpc interceptor for list_terraform_versions

        DEPRECATED. Please use the `post_list_terraform_versions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_list_terraform_versions` interceptor runs
        before the `post_list_terraform_versions_with_metadata` interceptor.
        """
        return response

    def post_list_terraform_versions_with_metadata(
        self,
        response: config.ListTerraformVersionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config.ListTerraformVersionsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_terraform_versions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_list_terraform_versions_with_metadata`
        interceptor in new development instead of the `post_list_terraform_versions` interceptor.
        When both interceptors are used, this `post_list_terraform_versions_with_metadata` interceptor runs after the
        `post_list_terraform_versions` interceptor. The (possibly modified) response returned by
        `post_list_terraform_versions` will be passed to
        `post_list_terraform_versions_with_metadata`.
        """
        return response, metadata

    def pre_lock_deployment(
        self,
        request: config.LockDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.LockDeploymentRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for lock_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_lock_deployment(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for lock_deployment

        DEPRECATED. Please use the `post_lock_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_lock_deployment` interceptor runs
        before the `post_lock_deployment_with_metadata` interceptor.
        """
        return response

    def post_lock_deployment_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for lock_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_lock_deployment_with_metadata`
        interceptor in new development instead of the `post_lock_deployment` interceptor.
        When both interceptors are used, this `post_lock_deployment_with_metadata` interceptor runs after the
        `post_lock_deployment` interceptor. The (possibly modified) response returned by
        `post_lock_deployment` will be passed to
        `post_lock_deployment_with_metadata`.
        """
        return response, metadata

    def pre_provision_deployment_group(
        self,
        request: config.ProvisionDeploymentGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config.ProvisionDeploymentGroupRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for provision_deployment_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_provision_deployment_group(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for provision_deployment_group

        DEPRECATED. Please use the `post_provision_deployment_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_provision_deployment_group` interceptor runs
        before the `post_provision_deployment_group_with_metadata` interceptor.
        """
        return response

    def post_provision_deployment_group_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for provision_deployment_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_provision_deployment_group_with_metadata`
        interceptor in new development instead of the `post_provision_deployment_group` interceptor.
        When both interceptors are used, this `post_provision_deployment_group_with_metadata` interceptor runs after the
        `post_provision_deployment_group` interceptor. The (possibly modified) response returned by
        `post_provision_deployment_group` will be passed to
        `post_provision_deployment_group_with_metadata`.
        """
        return response, metadata

    def pre_unlock_deployment(
        self,
        request: config.UnlockDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.UnlockDeploymentRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for unlock_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_unlock_deployment(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for unlock_deployment

        DEPRECATED. Please use the `post_unlock_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_unlock_deployment` interceptor runs
        before the `post_unlock_deployment_with_metadata` interceptor.
        """
        return response

    def post_unlock_deployment_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for unlock_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_unlock_deployment_with_metadata`
        interceptor in new development instead of the `post_unlock_deployment` interceptor.
        When both interceptors are used, this `post_unlock_deployment_with_metadata` interceptor runs after the
        `post_unlock_deployment` interceptor. The (possibly modified) response returned by
        `post_unlock_deployment` will be passed to
        `post_unlock_deployment_with_metadata`.
        """
        return response, metadata

    def pre_update_auto_migration_config(
        self,
        request: config.UpdateAutoMigrationConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config.UpdateAutoMigrationConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_auto_migration_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_update_auto_migration_config(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_auto_migration_config

        DEPRECATED. Please use the `post_update_auto_migration_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_update_auto_migration_config` interceptor runs
        before the `post_update_auto_migration_config_with_metadata` interceptor.
        """
        return response

    def post_update_auto_migration_config_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_auto_migration_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_update_auto_migration_config_with_metadata`
        interceptor in new development instead of the `post_update_auto_migration_config` interceptor.
        When both interceptors are used, this `post_update_auto_migration_config_with_metadata` interceptor runs after the
        `post_update_auto_migration_config` interceptor. The (possibly modified) response returned by
        `post_update_auto_migration_config` will be passed to
        `post_update_auto_migration_config_with_metadata`.
        """
        return response, metadata

    def pre_update_deployment(
        self,
        request: config.UpdateDeploymentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[config.UpdateDeploymentRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_deployment

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_update_deployment(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_deployment

        DEPRECATED. Please use the `post_update_deployment_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_update_deployment` interceptor runs
        before the `post_update_deployment_with_metadata` interceptor.
        """
        return response

    def post_update_deployment_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_deployment

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_update_deployment_with_metadata`
        interceptor in new development instead of the `post_update_deployment` interceptor.
        When both interceptors are used, this `post_update_deployment_with_metadata` interceptor runs after the
        `post_update_deployment` interceptor. The (possibly modified) response returned by
        `post_update_deployment` will be passed to
        `post_update_deployment_with_metadata`.
        """
        return response, metadata

    def pre_update_deployment_group(
        self,
        request: config.UpdateDeploymentGroupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        config.UpdateDeploymentGroupRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_deployment_group

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Config server.
        """
        return request, metadata

    def post_update_deployment_group(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for update_deployment_group

        DEPRECATED. Please use the `post_update_deployment_group_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Config server but before
        it is returned to user code. This `post_update_deployment_group` interceptor runs
        before the `post_update_deployment_group_with_metadata` interceptor.
        """
        return response

    def post_update_deployment_group_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_deployment_group

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Config server but before it is returned to user code.

        We recommend only using this `post_update_deployment_group_with_metadata`
        interceptor in new development instead of the `post_update_deployment_group` interceptor.
        When both interceptors are used, this `post_update_deployment_group_with_metadata` interceptor runs after the
        `post_update_deployment_group` interceptor. The (possibly modified) response returned by
        `post_update_deployment_group` will be passed to
        `post_update_deployment_group_with_metadata`.
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
        before they are sent to the Config server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the Config server but before
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
        before they are sent to the Config server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the Config server but before
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
        before they are sent to the Config server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the Config server but before
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
        before they are sent to the Config server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the Config server but before
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
        before they are sent to the Config server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the Config server but before
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
        before they are sent to the Config server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the Config server but before
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
        before they are sent to the Config server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the Config server but before
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
        before they are sent to the Config server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the Config server but before
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
        before they are sent to the Config server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the Config server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class ConfigRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ConfigRestInterceptor


class ConfigRestTransport(_BaseConfigRestTransport):
    """REST backend synchronous transport for Config.

    Infrastructure Manager is a managed service that automates
    the deployment and management of Google Cloud infrastructure
    resources.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "config.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[ConfigRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'config.googleapis.com').
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
            interceptor (Optional[ConfigRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or ConfigRestInterceptor()
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

    class _CreateDeployment(
        _BaseConfigRestTransport._BaseCreateDeployment, ConfigRestStub
    ):
        def __hash__(self):
            return hash("ConfigRestTransport.CreateDeployment")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.CreateDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create deployment method over HTTP.

            Args:
                request (~.config.CreateDeploymentRequest):
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
                _BaseConfigRestTransport._BaseCreateDeployment._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseCreateDeployment,
                    "_BaseCreateDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.CreateDeployment",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "CreateDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._CreateDeployment._get_response(
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

            resp = self._interceptor.post_create_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_deployment_with_metadata(
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
                    "Received response for google.cloud.config_v1.ConfigClient.create_deployment",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "CreateDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateDeploymentGroup(
        _BaseConfigRestTransport._BaseCreateDeploymentGroup, ConfigRestStub
    ):
        def __hash__(self):
            return hash("ConfigRestTransport.CreateDeploymentGroup")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.CreateDeploymentGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create deployment group method over HTTP.

            Args:
                request (~.config.CreateDeploymentGroupRequest):
                    The request object. A request to create a deployment
                group
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
                _BaseConfigRestTransport._BaseCreateDeploymentGroup._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_deployment_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseCreateDeploymentGroup,
                    "_BaseCreateDeploymentGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.CreateDeploymentGroup",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "CreateDeploymentGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._CreateDeploymentGroup._get_response(
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

            resp = self._interceptor.post_create_deployment_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_deployment_group_with_metadata(
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
                    "Received response for google.cloud.config_v1.ConfigClient.create_deployment_group",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "CreateDeploymentGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreatePreview(_BaseConfigRestTransport._BaseCreatePreview, ConfigRestStub):
        def __hash__(self):
            return hash("ConfigRestTransport.CreatePreview")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.CreatePreviewRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create preview method over HTTP.

            Args:
                request (~.config.CreatePreviewRequest):
                    The request object. A request to create a preview.
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
                _BaseConfigRestTransport._BaseCreatePreview._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_preview(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseCreatePreview,
                    "_BaseCreatePreview__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.CreatePreview",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "CreatePreview",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._CreatePreview._get_response(
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

            resp = self._interceptor.post_create_preview(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_preview_with_metadata(
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
                    "Received response for google.cloud.config_v1.ConfigClient.create_preview",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "CreatePreview",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteDeployment(
        _BaseConfigRestTransport._BaseDeleteDeployment, ConfigRestStub
    ):
        def __hash__(self):
            return hash("ConfigRestTransport.DeleteDeployment")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.DeleteDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete deployment method over HTTP.

            Args:
                request (~.config.DeleteDeploymentRequest):
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
                _BaseConfigRestTransport._BaseDeleteDeployment._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseDeleteDeployment,
                    "_BaseDeleteDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.DeleteDeployment",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "DeleteDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._DeleteDeployment._get_response(
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

            resp = self._interceptor.post_delete_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_deployment_with_metadata(
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
                    "Received response for google.cloud.config_v1.ConfigClient.delete_deployment",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "DeleteDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteDeploymentGroup(
        _BaseConfigRestTransport._BaseDeleteDeploymentGroup, ConfigRestStub
    ):
        def __hash__(self):
            return hash("ConfigRestTransport.DeleteDeploymentGroup")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.DeleteDeploymentGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete deployment group method over HTTP.

            Args:
                request (~.config.DeleteDeploymentGroupRequest):
                    The request object. Request message for Delete
                DeploymentGroup
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
                _BaseConfigRestTransport._BaseDeleteDeploymentGroup._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_deployment_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseDeleteDeploymentGroup,
                    "_BaseDeleteDeploymentGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.DeleteDeploymentGroup",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "DeleteDeploymentGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._DeleteDeploymentGroup._get_response(
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

            resp = self._interceptor.post_delete_deployment_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_deployment_group_with_metadata(
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
                    "Received response for google.cloud.config_v1.ConfigClient.delete_deployment_group",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "DeleteDeploymentGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeletePreview(_BaseConfigRestTransport._BaseDeletePreview, ConfigRestStub):
        def __hash__(self):
            return hash("ConfigRestTransport.DeletePreview")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.DeletePreviewRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete preview method over HTTP.

            Args:
                request (~.config.DeletePreviewRequest):
                    The request object. A request to delete a preview.
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
                _BaseConfigRestTransport._BaseDeletePreview._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_preview(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseDeletePreview,
                    "_BaseDeletePreview__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.DeletePreview",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "DeletePreview",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._DeletePreview._get_response(
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

            resp = self._interceptor.post_delete_preview(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_preview_with_metadata(
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
                    "Received response for google.cloud.config_v1.ConfigClient.delete_preview",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "DeletePreview",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteStatefile(
        _BaseConfigRestTransport._BaseDeleteStatefile, ConfigRestStub
    ):
        def __hash__(self):
            return hash("ConfigRestTransport.DeleteStatefile")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.DeleteStatefileRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete statefile method over HTTP.

            Args:
                request (~.config.DeleteStatefileRequest):
                    The request object. A request to delete a state file
                passed to a 'DeleteStatefile' call.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseConfigRestTransport._BaseDeleteStatefile._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_statefile(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseDeleteStatefile,
                    "_BaseDeleteStatefile__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.DeleteStatefile",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "DeleteStatefile",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._DeleteStatefile._get_response(
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

    class _DeprovisionDeploymentGroup(
        _BaseConfigRestTransport._BaseDeprovisionDeploymentGroup, ConfigRestStub
    ):
        def __hash__(self):
            return hash("ConfigRestTransport.DeprovisionDeploymentGroup")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.DeprovisionDeploymentGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the deprovision deployment
            group method over HTTP.

                Args:
                    request (~.config.DeprovisionDeploymentGroupRequest):
                        The request object. The request message for the
                    DeprovisionDeploymentGroup method.
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

            http_options = _BaseConfigRestTransport._BaseDeprovisionDeploymentGroup._get_http_options()
            request, metadata = self._interceptor.pre_deprovision_deployment_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseDeprovisionDeploymentGroup,
                    "_BaseDeprovisionDeploymentGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.DeprovisionDeploymentGroup",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "DeprovisionDeploymentGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._DeprovisionDeploymentGroup._get_response(
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

            resp = self._interceptor.post_deprovision_deployment_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_deprovision_deployment_group_with_metadata(
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
                    "Received response for google.cloud.config_v1.ConfigClient.deprovision_deployment_group",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "DeprovisionDeploymentGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ExportDeploymentStatefile(
        _BaseConfigRestTransport._BaseExportDeploymentStatefile, ConfigRestStub
    ):
        def __hash__(self):
            return hash("ConfigRestTransport.ExportDeploymentStatefile")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.ExportDeploymentStatefileRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config.Statefile:
            r"""Call the export deployment
            statefile method over HTTP.

                Args:
                    request (~.config.ExportDeploymentStatefileRequest):
                        The request object. A request to export a state file
                    passed to a 'ExportDeploymentStatefile'
                    call.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.config.Statefile:
                        Contains info about a Terraform state
                    file

            """

            http_options = _BaseConfigRestTransport._BaseExportDeploymentStatefile._get_http_options()
            request, metadata = self._interceptor.pre_export_deployment_statefile(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseExportDeploymentStatefile,
                    "_BaseExportDeploymentStatefile__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.ExportDeploymentStatefile",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "ExportDeploymentStatefile",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._ExportDeploymentStatefile._get_response(
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
            resp = config.Statefile()
            pb_resp = config.Statefile.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_export_deployment_statefile(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_export_deployment_statefile_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = config.Statefile.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.config_v1.ConfigClient.export_deployment_statefile",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "ExportDeploymentStatefile",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ExportLockInfo(_BaseConfigRestTransport._BaseExportLockInfo, ConfigRestStub):
        def __hash__(self):
            return hash("ConfigRestTransport.ExportLockInfo")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.ExportLockInfoRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config.LockInfo:
            r"""Call the export lock info method over HTTP.

            Args:
                request (~.config.ExportLockInfoRequest):
                    The request object. A request to get a state file lock
                info passed to a 'ExportLockInfo' call.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.config.LockInfo:
                    Details about the lock which locked
                the deployment.

            """

            http_options = (
                _BaseConfigRestTransport._BaseExportLockInfo._get_http_options()
            )
            request, metadata = self._interceptor.pre_export_lock_info(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseExportLockInfo,
                    "_BaseExportLockInfo__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.ExportLockInfo",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "ExportLockInfo",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._ExportLockInfo._get_response(
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
            resp = config.LockInfo()
            pb_resp = config.LockInfo.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_export_lock_info(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_export_lock_info_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = config.LockInfo.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.config_v1.ConfigClient.export_lock_info",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "ExportLockInfo",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ExportPreviewResult(
        _BaseConfigRestTransport._BaseExportPreviewResult, ConfigRestStub
    ):
        def __hash__(self):
            return hash("ConfigRestTransport.ExportPreviewResult")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.ExportPreviewResultRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config.ExportPreviewResultResponse:
            r"""Call the export preview result method over HTTP.

            Args:
                request (~.config.ExportPreviewResultRequest):
                    The request object. A request to export preview results.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.config.ExportPreviewResultResponse:
                    A response to ``ExportPreviewResult`` call. Contains
                preview results.

            """

            http_options = (
                _BaseConfigRestTransport._BaseExportPreviewResult._get_http_options()
            )
            request, metadata = self._interceptor.pre_export_preview_result(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseExportPreviewResult,
                    "_BaseExportPreviewResult__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.ExportPreviewResult",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "ExportPreviewResult",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._ExportPreviewResult._get_response(
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
            resp = config.ExportPreviewResultResponse()
            pb_resp = config.ExportPreviewResultResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_export_preview_result(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_export_preview_result_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = config.ExportPreviewResultResponse.to_json(
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
                    "Received response for google.cloud.config_v1.ConfigClient.export_preview_result",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "ExportPreviewResult",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ExportRevisionStatefile(
        _BaseConfigRestTransport._BaseExportRevisionStatefile, ConfigRestStub
    ):
        def __hash__(self):
            return hash("ConfigRestTransport.ExportRevisionStatefile")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.ExportRevisionStatefileRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config.Statefile:
            r"""Call the export revision statefile method over HTTP.

            Args:
                request (~.config.ExportRevisionStatefileRequest):
                    The request object. A request to export a state file
                passed to a 'ExportRevisionStatefile'
                call.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.config.Statefile:
                    Contains info about a Terraform state
                file

            """

            http_options = _BaseConfigRestTransport._BaseExportRevisionStatefile._get_http_options()
            request, metadata = self._interceptor.pre_export_revision_statefile(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseExportRevisionStatefile,
                    "_BaseExportRevisionStatefile__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.ExportRevisionStatefile",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "ExportRevisionStatefile",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._ExportRevisionStatefile._get_response(
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
            resp = config.Statefile()
            pb_resp = config.Statefile.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_export_revision_statefile(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_export_revision_statefile_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = config.Statefile.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.config_v1.ConfigClient.export_revision_statefile",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "ExportRevisionStatefile",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAutoMigrationConfig(
        _BaseConfigRestTransport._BaseGetAutoMigrationConfig, ConfigRestStub
    ):
        def __hash__(self):
            return hash("ConfigRestTransport.GetAutoMigrationConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.GetAutoMigrationConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config.AutoMigrationConfig:
            r"""Call the get auto migration config method over HTTP.

            Args:
                request (~.config.GetAutoMigrationConfigRequest):
                    The request object. The request message for the
                GetAutoMigrationConfig method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.config.AutoMigrationConfig:
                    AutoMigrationConfig contains the
                automigration configuration for a
                project.

            """

            http_options = (
                _BaseConfigRestTransport._BaseGetAutoMigrationConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_auto_migration_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseGetAutoMigrationConfig,
                    "_BaseGetAutoMigrationConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.GetAutoMigrationConfig",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "GetAutoMigrationConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._GetAutoMigrationConfig._get_response(
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
            resp = config.AutoMigrationConfig()
            pb_resp = config.AutoMigrationConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_auto_migration_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_auto_migration_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = config.AutoMigrationConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.config_v1.ConfigClient.get_auto_migration_config",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "GetAutoMigrationConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDeployment(_BaseConfigRestTransport._BaseGetDeployment, ConfigRestStub):
        def __hash__(self):
            return hash("ConfigRestTransport.GetDeployment")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.GetDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config.Deployment:
            r"""Call the get deployment method over HTTP.

            Args:
                request (~.config.GetDeploymentRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.config.Deployment:
                    A Deployment is a group of resources
                and configs managed and provisioned by
                Infra Manager.

            """

            http_options = (
                _BaseConfigRestTransport._BaseGetDeployment._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_deployment(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseGetDeployment,
                    "_BaseGetDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.GetDeployment",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "GetDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._GetDeployment._get_response(
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
            resp = config.Deployment()
            pb_resp = config.Deployment.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_deployment_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = config.Deployment.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.config_v1.ConfigClient.get_deployment",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "GetDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDeploymentGroup(
        _BaseConfigRestTransport._BaseGetDeploymentGroup, ConfigRestStub
    ):
        def __hash__(self):
            return hash("ConfigRestTransport.GetDeploymentGroup")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.GetDeploymentGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config.DeploymentGroup:
            r"""Call the get deployment group method over HTTP.

            Args:
                request (~.config.GetDeploymentGroupRequest):
                    The request object. The request message for the
                GetDeploymentGroup method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.config.DeploymentGroup:
                    A DeploymentGroup is a collection of
                DeploymentUnits that in a DAG-like
                structure.

            """

            http_options = (
                _BaseConfigRestTransport._BaseGetDeploymentGroup._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_deployment_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseGetDeploymentGroup,
                    "_BaseGetDeploymentGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.GetDeploymentGroup",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "GetDeploymentGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._GetDeploymentGroup._get_response(
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
            resp = config.DeploymentGroup()
            pb_resp = config.DeploymentGroup.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_deployment_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_deployment_group_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = config.DeploymentGroup.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.config_v1.ConfigClient.get_deployment_group",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "GetDeploymentGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDeploymentGroupRevision(
        _BaseConfigRestTransport._BaseGetDeploymentGroupRevision, ConfigRestStub
    ):
        def __hash__(self):
            return hash("ConfigRestTransport.GetDeploymentGroupRevision")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.GetDeploymentGroupRevisionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config.DeploymentGroupRevision:
            r"""Call the get deployment group
            revision method over HTTP.

                Args:
                    request (~.config.GetDeploymentGroupRevisionRequest):
                        The request object. The request message for the
                    GetDeploymentGroupRevision method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.config.DeploymentGroupRevision:
                        A DeploymentGroupRevision represents a snapshot of a
                    [DeploymentGroup][google.cloud.config.v1.DeploymentGroup]
                    at a given point in time, created when a DeploymentGroup
                    is provisioned or deprovisioned.

            """

            http_options = _BaseConfigRestTransport._BaseGetDeploymentGroupRevision._get_http_options()
            request, metadata = self._interceptor.pre_get_deployment_group_revision(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseGetDeploymentGroupRevision,
                    "_BaseGetDeploymentGroupRevision__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.GetDeploymentGroupRevision",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "GetDeploymentGroupRevision",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._GetDeploymentGroupRevision._get_response(
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
            resp = config.DeploymentGroupRevision()
            pb_resp = config.DeploymentGroupRevision.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_deployment_group_revision(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_deployment_group_revision_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = config.DeploymentGroupRevision.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.config_v1.ConfigClient.get_deployment_group_revision",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "GetDeploymentGroupRevision",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetPreview(_BaseConfigRestTransport._BaseGetPreview, ConfigRestStub):
        def __hash__(self):
            return hash("ConfigRestTransport.GetPreview")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.GetPreviewRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config.Preview:
            r"""Call the get preview method over HTTP.

            Args:
                request (~.config.GetPreviewRequest):
                    The request object. A request to get details about a
                preview.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.config.Preview:
                    A preview represents a set of actions
                Infra Manager would perform to move the
                resources towards the desired state as
                specified in the configuration.

            """

            http_options = _BaseConfigRestTransport._BaseGetPreview._get_http_options()
            request, metadata = self._interceptor.pre_get_preview(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseGetPreview,
                    "_BaseGetPreview__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.GetPreview",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "GetPreview",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._GetPreview._get_response(
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
            resp = config.Preview()
            pb_resp = config.Preview.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_preview(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_preview_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = config.Preview.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.config_v1.ConfigClient.get_preview",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "GetPreview",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetResource(_BaseConfigRestTransport._BaseGetResource, ConfigRestStub):
        def __hash__(self):
            return hash("ConfigRestTransport.GetResource")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.GetResourceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config.Resource:
            r"""Call the get resource method over HTTP.

            Args:
                request (~.config.GetResourceRequest):
                    The request object. A request to get a Resource from a
                'GetResource' call.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.config.Resource:
                    Resource represents a Google Cloud
                Platform resource actuated by IM.
                Resources are child resources of
                Revisions.

            """

            http_options = _BaseConfigRestTransport._BaseGetResource._get_http_options()
            request, metadata = self._interceptor.pre_get_resource(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseGetResource,
                    "_BaseGetResource__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.GetResource",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "GetResource",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._GetResource._get_response(
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
            resp = config.Resource()
            pb_resp = config.Resource.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_resource(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_resource_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = config.Resource.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.config_v1.ConfigClient.get_resource",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "GetResource",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetResourceChange(
        _BaseConfigRestTransport._BaseGetResourceChange, ConfigRestStub
    ):
        def __hash__(self):
            return hash("ConfigRestTransport.GetResourceChange")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.GetResourceChangeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config.ResourceChange:
            r"""Call the get resource change method over HTTP.

            Args:
                request (~.config.GetResourceChangeRequest):
                    The request object. The request message for the
                GetResourceChange method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.config.ResourceChange:
                    A resource change represents a change
                to a resource in the state file.

            """

            http_options = (
                _BaseConfigRestTransport._BaseGetResourceChange._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_resource_change(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseGetResourceChange,
                    "_BaseGetResourceChange__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.GetResourceChange",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "GetResourceChange",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._GetResourceChange._get_response(
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
            resp = config.ResourceChange()
            pb_resp = config.ResourceChange.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_resource_change(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_resource_change_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = config.ResourceChange.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.config_v1.ConfigClient.get_resource_change",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "GetResourceChange",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetResourceDrift(
        _BaseConfigRestTransport._BaseGetResourceDrift, ConfigRestStub
    ):
        def __hash__(self):
            return hash("ConfigRestTransport.GetResourceDrift")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.GetResourceDriftRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config.ResourceDrift:
            r"""Call the get resource drift method over HTTP.

            Args:
                request (~.config.GetResourceDriftRequest):
                    The request object. The request message for the
                GetResourceDrift method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.config.ResourceDrift:
                    A resource drift represents a drift
                to a resource in the state file.

            """

            http_options = (
                _BaseConfigRestTransport._BaseGetResourceDrift._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_resource_drift(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseGetResourceDrift,
                    "_BaseGetResourceDrift__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.GetResourceDrift",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "GetResourceDrift",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._GetResourceDrift._get_response(
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
            resp = config.ResourceDrift()
            pb_resp = config.ResourceDrift.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_resource_drift(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_resource_drift_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = config.ResourceDrift.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.config_v1.ConfigClient.get_resource_drift",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "GetResourceDrift",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetRevision(_BaseConfigRestTransport._BaseGetRevision, ConfigRestStub):
        def __hash__(self):
            return hash("ConfigRestTransport.GetRevision")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.GetRevisionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config.Revision:
            r"""Call the get revision method over HTTP.

            Args:
                request (~.config.GetRevisionRequest):
                    The request object. A request to get a Revision from a
                'GetRevision' call.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.config.Revision:
                    A child resource of a Deployment
                generated by a 'CreateDeployment' or
                'UpdateDeployment' call. Each Revision
                contains metadata pertaining to a
                snapshot of a particular Deployment.

            """

            http_options = _BaseConfigRestTransport._BaseGetRevision._get_http_options()
            request, metadata = self._interceptor.pre_get_revision(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseGetRevision,
                    "_BaseGetRevision__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.GetRevision",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "GetRevision",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._GetRevision._get_response(
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
            resp = config.Revision()
            pb_resp = config.Revision.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_revision(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_revision_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = config.Revision.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.config_v1.ConfigClient.get_revision",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "GetRevision",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetTerraformVersion(
        _BaseConfigRestTransport._BaseGetTerraformVersion, ConfigRestStub
    ):
        def __hash__(self):
            return hash("ConfigRestTransport.GetTerraformVersion")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.GetTerraformVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config.TerraformVersion:
            r"""Call the get terraform version method over HTTP.

            Args:
                request (~.config.GetTerraformVersionRequest):
                    The request object. The request message for the
                GetTerraformVersion method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.config.TerraformVersion:
                    A TerraformVersion represents the
                support state the corresponding
                Terraform version.

            """

            http_options = (
                _BaseConfigRestTransport._BaseGetTerraformVersion._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_terraform_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseGetTerraformVersion,
                    "_BaseGetTerraformVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.GetTerraformVersion",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "GetTerraformVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._GetTerraformVersion._get_response(
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
            resp = config.TerraformVersion()
            pb_resp = config.TerraformVersion.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_terraform_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_terraform_version_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = config.TerraformVersion.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.config_v1.ConfigClient.get_terraform_version",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "GetTerraformVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ImportStatefile(
        _BaseConfigRestTransport._BaseImportStatefile, ConfigRestStub
    ):
        def __hash__(self):
            return hash("ConfigRestTransport.ImportStatefile")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.ImportStatefileRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config.Statefile:
            r"""Call the import statefile method over HTTP.

            Args:
                request (~.config.ImportStatefileRequest):
                    The request object. A request to import a state file
                passed to a 'ImportStatefile' call.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.config.Statefile:
                    Contains info about a Terraform state
                file

            """

            http_options = (
                _BaseConfigRestTransport._BaseImportStatefile._get_http_options()
            )
            request, metadata = self._interceptor.pre_import_statefile(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseImportStatefile,
                    "_BaseImportStatefile__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.ImportStatefile",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "ImportStatefile",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._ImportStatefile._get_response(
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
            resp = config.Statefile()
            pb_resp = config.Statefile.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_import_statefile(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_import_statefile_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = config.Statefile.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.config_v1.ConfigClient.import_statefile",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "ImportStatefile",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDeploymentGroupRevisions(
        _BaseConfigRestTransport._BaseListDeploymentGroupRevisions, ConfigRestStub
    ):
        def __hash__(self):
            return hash("ConfigRestTransport.ListDeploymentGroupRevisions")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.ListDeploymentGroupRevisionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config.ListDeploymentGroupRevisionsResponse:
            r"""Call the list deployment group
            revisions method over HTTP.

                Args:
                    request (~.config.ListDeploymentGroupRevisionsRequest):
                        The request object. The request message for the
                    ListDeploymentGroupRevisions method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.config.ListDeploymentGroupRevisionsResponse:
                        The response message for the
                    ListDeploymentGroupRevisions method.

            """

            http_options = _BaseConfigRestTransport._BaseListDeploymentGroupRevisions._get_http_options()
            request, metadata = self._interceptor.pre_list_deployment_group_revisions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseListDeploymentGroupRevisions,
                    "_BaseListDeploymentGroupRevisions__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.ListDeploymentGroupRevisions",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "ListDeploymentGroupRevisions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._ListDeploymentGroupRevisions._get_response(
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
            resp = config.ListDeploymentGroupRevisionsResponse()
            pb_resp = config.ListDeploymentGroupRevisionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_deployment_group_revisions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_deployment_group_revisions_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        config.ListDeploymentGroupRevisionsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.config_v1.ConfigClient.list_deployment_group_revisions",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "ListDeploymentGroupRevisions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDeploymentGroups(
        _BaseConfigRestTransport._BaseListDeploymentGroups, ConfigRestStub
    ):
        def __hash__(self):
            return hash("ConfigRestTransport.ListDeploymentGroups")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.ListDeploymentGroupsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config.ListDeploymentGroupsResponse:
            r"""Call the list deployment groups method over HTTP.

            Args:
                request (~.config.ListDeploymentGroupsRequest):
                    The request object. The request message for the
                ListDeploymentGroups method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.config.ListDeploymentGroupsResponse:
                    The response message for the
                ListDeploymentGroups method.

            """

            http_options = (
                _BaseConfigRestTransport._BaseListDeploymentGroups._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_deployment_groups(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseListDeploymentGroups,
                    "_BaseListDeploymentGroups__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.ListDeploymentGroups",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "ListDeploymentGroups",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._ListDeploymentGroups._get_response(
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
            resp = config.ListDeploymentGroupsResponse()
            pb_resp = config.ListDeploymentGroupsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_deployment_groups(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_deployment_groups_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = config.ListDeploymentGroupsResponse.to_json(
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
                    "Received response for google.cloud.config_v1.ConfigClient.list_deployment_groups",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "ListDeploymentGroups",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDeployments(
        _BaseConfigRestTransport._BaseListDeployments, ConfigRestStub
    ):
        def __hash__(self):
            return hash("ConfigRestTransport.ListDeployments")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.ListDeploymentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config.ListDeploymentsResponse:
            r"""Call the list deployments method over HTTP.

            Args:
                request (~.config.ListDeploymentsRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.config.ListDeploymentsResponse:

            """

            http_options = (
                _BaseConfigRestTransport._BaseListDeployments._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_deployments(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseListDeployments,
                    "_BaseListDeployments__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.ListDeployments",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "ListDeployments",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._ListDeployments._get_response(
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
            resp = config.ListDeploymentsResponse()
            pb_resp = config.ListDeploymentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_deployments(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_deployments_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = config.ListDeploymentsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.config_v1.ConfigClient.list_deployments",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "ListDeployments",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPreviews(_BaseConfigRestTransport._BaseListPreviews, ConfigRestStub):
        def __hash__(self):
            return hash("ConfigRestTransport.ListPreviews")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.ListPreviewsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config.ListPreviewsResponse:
            r"""Call the list previews method over HTTP.

            Args:
                request (~.config.ListPreviewsRequest):
                    The request object. A request to list all previews for a
                given project and location.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.config.ListPreviewsResponse:
                    A response to a ``ListPreviews`` call. Contains a list
                of Previews.

            """

            http_options = (
                _BaseConfigRestTransport._BaseListPreviews._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_previews(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseListPreviews,
                    "_BaseListPreviews__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.ListPreviews",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "ListPreviews",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._ListPreviews._get_response(
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
            resp = config.ListPreviewsResponse()
            pb_resp = config.ListPreviewsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_previews(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_previews_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = config.ListPreviewsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.config_v1.ConfigClient.list_previews",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "ListPreviews",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListResourceChanges(
        _BaseConfigRestTransport._BaseListResourceChanges, ConfigRestStub
    ):
        def __hash__(self):
            return hash("ConfigRestTransport.ListResourceChanges")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.ListResourceChangesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config.ListResourceChangesResponse:
            r"""Call the list resource changes method over HTTP.

            Args:
                request (~.config.ListResourceChangesRequest):
                    The request object. The request message for the
                ListResourceChanges method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.config.ListResourceChangesResponse:
                    A response to a 'ListResourceChanges'
                call. Contains a list of
                ResourceChanges.

            """

            http_options = (
                _BaseConfigRestTransport._BaseListResourceChanges._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_resource_changes(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseListResourceChanges,
                    "_BaseListResourceChanges__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.ListResourceChanges",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "ListResourceChanges",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._ListResourceChanges._get_response(
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
            resp = config.ListResourceChangesResponse()
            pb_resp = config.ListResourceChangesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_resource_changes(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_resource_changes_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = config.ListResourceChangesResponse.to_json(
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
                    "Received response for google.cloud.config_v1.ConfigClient.list_resource_changes",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "ListResourceChanges",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListResourceDrifts(
        _BaseConfigRestTransport._BaseListResourceDrifts, ConfigRestStub
    ):
        def __hash__(self):
            return hash("ConfigRestTransport.ListResourceDrifts")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.ListResourceDriftsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config.ListResourceDriftsResponse:
            r"""Call the list resource drifts method over HTTP.

            Args:
                request (~.config.ListResourceDriftsRequest):
                    The request object. The request message for the
                ListResourceDrifts method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.config.ListResourceDriftsResponse:
                    A response to a 'ListResourceDrifts'
                call. Contains a list of ResourceDrifts.

            """

            http_options = (
                _BaseConfigRestTransport._BaseListResourceDrifts._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_resource_drifts(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseListResourceDrifts,
                    "_BaseListResourceDrifts__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.ListResourceDrifts",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "ListResourceDrifts",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._ListResourceDrifts._get_response(
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
            resp = config.ListResourceDriftsResponse()
            pb_resp = config.ListResourceDriftsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_resource_drifts(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_resource_drifts_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = config.ListResourceDriftsResponse.to_json(
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
                    "Received response for google.cloud.config_v1.ConfigClient.list_resource_drifts",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "ListResourceDrifts",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListResources(_BaseConfigRestTransport._BaseListResources, ConfigRestStub):
        def __hash__(self):
            return hash("ConfigRestTransport.ListResources")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.ListResourcesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config.ListResourcesResponse:
            r"""Call the list resources method over HTTP.

            Args:
                request (~.config.ListResourcesRequest):
                    The request object. A request to list Resources passed to
                a 'ListResources' call.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.config.ListResourcesResponse:
                    A response to a 'ListResources' call.
                Contains a list of Resources.

            """

            http_options = (
                _BaseConfigRestTransport._BaseListResources._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_resources(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseListResources,
                    "_BaseListResources__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.ListResources",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "ListResources",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._ListResources._get_response(
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
            resp = config.ListResourcesResponse()
            pb_resp = config.ListResourcesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_resources(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_resources_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = config.ListResourcesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.config_v1.ConfigClient.list_resources",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "ListResources",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListRevisions(_BaseConfigRestTransport._BaseListRevisions, ConfigRestStub):
        def __hash__(self):
            return hash("ConfigRestTransport.ListRevisions")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.ListRevisionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config.ListRevisionsResponse:
            r"""Call the list revisions method over HTTP.

            Args:
                request (~.config.ListRevisionsRequest):
                    The request object. A request to list Revisions passed to
                a 'ListRevisions' call.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.config.ListRevisionsResponse:
                    A response to a 'ListRevisions' call.
                Contains a list of Revisions.

            """

            http_options = (
                _BaseConfigRestTransport._BaseListRevisions._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_revisions(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseListRevisions,
                    "_BaseListRevisions__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.ListRevisions",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "ListRevisions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._ListRevisions._get_response(
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
            resp = config.ListRevisionsResponse()
            pb_resp = config.ListRevisionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_revisions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_revisions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = config.ListRevisionsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.config_v1.ConfigClient.list_revisions",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "ListRevisions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListTerraformVersions(
        _BaseConfigRestTransport._BaseListTerraformVersions, ConfigRestStub
    ):
        def __hash__(self):
            return hash("ConfigRestTransport.ListTerraformVersions")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.ListTerraformVersionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> config.ListTerraformVersionsResponse:
            r"""Call the list terraform versions method over HTTP.

            Args:
                request (~.config.ListTerraformVersionsRequest):
                    The request object. The request message for the
                ListTerraformVersions method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.config.ListTerraformVersionsResponse:
                    The response message for the ``ListTerraformVersions``
                method.

            """

            http_options = (
                _BaseConfigRestTransport._BaseListTerraformVersions._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_terraform_versions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseListTerraformVersions,
                    "_BaseListTerraformVersions__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.ListTerraformVersions",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "ListTerraformVersions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._ListTerraformVersions._get_response(
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
            resp = config.ListTerraformVersionsResponse()
            pb_resp = config.ListTerraformVersionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_terraform_versions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_terraform_versions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = config.ListTerraformVersionsResponse.to_json(
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
                    "Received response for google.cloud.config_v1.ConfigClient.list_terraform_versions",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "ListTerraformVersions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _LockDeployment(_BaseConfigRestTransport._BaseLockDeployment, ConfigRestStub):
        def __hash__(self):
            return hash("ConfigRestTransport.LockDeployment")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.LockDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the lock deployment method over HTTP.

            Args:
                request (~.config.LockDeploymentRequest):
                    The request object. A request to lock a deployment passed
                to a 'LockDeployment' call.
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
                _BaseConfigRestTransport._BaseLockDeployment._get_http_options()
            )
            request, metadata = self._interceptor.pre_lock_deployment(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseLockDeployment,
                    "_BaseLockDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.LockDeployment",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "LockDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._LockDeployment._get_response(
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

            resp = self._interceptor.post_lock_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_lock_deployment_with_metadata(
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
                    "Received response for google.cloud.config_v1.ConfigClient.lock_deployment",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "LockDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ProvisionDeploymentGroup(
        _BaseConfigRestTransport._BaseProvisionDeploymentGroup, ConfigRestStub
    ):
        def __hash__(self):
            return hash("ConfigRestTransport.ProvisionDeploymentGroup")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.ProvisionDeploymentGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the provision deployment
            group method over HTTP.

                Args:
                    request (~.config.ProvisionDeploymentGroupRequest):
                        The request object. The request message for the
                    ProvisionDeploymentGroup method.
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

            http_options = _BaseConfigRestTransport._BaseProvisionDeploymentGroup._get_http_options()
            request, metadata = self._interceptor.pre_provision_deployment_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseProvisionDeploymentGroup,
                    "_BaseProvisionDeploymentGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.ProvisionDeploymentGroup",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "ProvisionDeploymentGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._ProvisionDeploymentGroup._get_response(
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

            resp = self._interceptor.post_provision_deployment_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_provision_deployment_group_with_metadata(
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
                    "Received response for google.cloud.config_v1.ConfigClient.provision_deployment_group",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "ProvisionDeploymentGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UnlockDeployment(
        _BaseConfigRestTransport._BaseUnlockDeployment, ConfigRestStub
    ):
        def __hash__(self):
            return hash("ConfigRestTransport.UnlockDeployment")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.UnlockDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the unlock deployment method over HTTP.

            Args:
                request (~.config.UnlockDeploymentRequest):
                    The request object. A request to unlock a state file
                passed to a 'UnlockDeployment' call.
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
                _BaseConfigRestTransport._BaseUnlockDeployment._get_http_options()
            )
            request, metadata = self._interceptor.pre_unlock_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseUnlockDeployment,
                    "_BaseUnlockDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.UnlockDeployment",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "UnlockDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._UnlockDeployment._get_response(
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

            resp = self._interceptor.post_unlock_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_unlock_deployment_with_metadata(
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
                    "Received response for google.cloud.config_v1.ConfigClient.unlock_deployment",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "UnlockDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateAutoMigrationConfig(
        _BaseConfigRestTransport._BaseUpdateAutoMigrationConfig, ConfigRestStub
    ):
        def __hash__(self):
            return hash("ConfigRestTransport.UpdateAutoMigrationConfig")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.UpdateAutoMigrationConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update auto migration
            config method over HTTP.

                Args:
                    request (~.config.UpdateAutoMigrationConfigRequest):
                        The request object. The request message for the
                    UpdateAutoMigrationConfig method.
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

            http_options = _BaseConfigRestTransport._BaseUpdateAutoMigrationConfig._get_http_options()
            request, metadata = self._interceptor.pre_update_auto_migration_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseUpdateAutoMigrationConfig,
                    "_BaseUpdateAutoMigrationConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.UpdateAutoMigrationConfig",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "UpdateAutoMigrationConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._UpdateAutoMigrationConfig._get_response(
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

            resp = self._interceptor.post_update_auto_migration_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_auto_migration_config_with_metadata(
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
                    "Received response for google.cloud.config_v1.ConfigClient.update_auto_migration_config",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "UpdateAutoMigrationConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDeployment(
        _BaseConfigRestTransport._BaseUpdateDeployment, ConfigRestStub
    ):
        def __hash__(self):
            return hash("ConfigRestTransport.UpdateDeployment")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.UpdateDeploymentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update deployment method over HTTP.

            Args:
                request (~.config.UpdateDeploymentRequest):
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
                _BaseConfigRestTransport._BaseUpdateDeployment._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_deployment(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseUpdateDeployment,
                    "_BaseUpdateDeployment__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.UpdateDeployment",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "UpdateDeployment",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._UpdateDeployment._get_response(
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

            resp = self._interceptor.post_update_deployment(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_deployment_with_metadata(
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
                    "Received response for google.cloud.config_v1.ConfigClient.update_deployment",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "UpdateDeployment",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDeploymentGroup(
        _BaseConfigRestTransport._BaseUpdateDeploymentGroup, ConfigRestStub
    ):
        def __hash__(self):
            return hash("ConfigRestTransport.UpdateDeploymentGroup")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
            request: config.UpdateDeploymentGroupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the update deployment group method over HTTP.

            Args:
                request (~.config.UpdateDeploymentGroupRequest):
                    The request object. A request message for updating a
                deployment group
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
                _BaseConfigRestTransport._BaseUpdateDeploymentGroup._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_deployment_group(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseUpdateDeploymentGroup,
                    "_BaseUpdateDeploymentGroup__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.config_v1.ConfigClient.UpdateDeploymentGroup",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "UpdateDeploymentGroup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._UpdateDeploymentGroup._get_response(
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

            resp = self._interceptor.post_update_deployment_group(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_deployment_group_with_metadata(
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
                    "Received response for google.cloud.config_v1.ConfigClient.update_deployment_group",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "UpdateDeploymentGroup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_deployment(
        self,
    ) -> Callable[[config.CreateDeploymentRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_deployment_group(
        self,
    ) -> Callable[[config.CreateDeploymentGroupRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDeploymentGroup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_preview(
        self,
    ) -> Callable[[config.CreatePreviewRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreatePreview(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_deployment(
        self,
    ) -> Callable[[config.DeleteDeploymentRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_deployment_group(
        self,
    ) -> Callable[[config.DeleteDeploymentGroupRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDeploymentGroup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_preview(
        self,
    ) -> Callable[[config.DeletePreviewRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeletePreview(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_statefile(
        self,
    ) -> Callable[[config.DeleteStatefileRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteStatefile(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def deprovision_deployment_group(
        self,
    ) -> Callable[[config.DeprovisionDeploymentGroupRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeprovisionDeploymentGroup(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def export_deployment_statefile(
        self,
    ) -> Callable[[config.ExportDeploymentStatefileRequest], config.Statefile]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportDeploymentStatefile(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def export_lock_info(
        self,
    ) -> Callable[[config.ExportLockInfoRequest], config.LockInfo]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportLockInfo(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def export_preview_result(
        self,
    ) -> Callable[
        [config.ExportPreviewResultRequest], config.ExportPreviewResultResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportPreviewResult(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def export_revision_statefile(
        self,
    ) -> Callable[[config.ExportRevisionStatefileRequest], config.Statefile]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportRevisionStatefile(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_auto_migration_config(
        self,
    ) -> Callable[[config.GetAutoMigrationConfigRequest], config.AutoMigrationConfig]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAutoMigrationConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_deployment(
        self,
    ) -> Callable[[config.GetDeploymentRequest], config.Deployment]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_deployment_group(
        self,
    ) -> Callable[[config.GetDeploymentGroupRequest], config.DeploymentGroup]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDeploymentGroup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_deployment_group_revision(
        self,
    ) -> Callable[
        [config.GetDeploymentGroupRevisionRequest], config.DeploymentGroupRevision
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDeploymentGroupRevision(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_preview(self) -> Callable[[config.GetPreviewRequest], config.Preview]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetPreview(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_resource(self) -> Callable[[config.GetResourceRequest], config.Resource]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetResource(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_resource_change(
        self,
    ) -> Callable[[config.GetResourceChangeRequest], config.ResourceChange]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetResourceChange(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_resource_drift(
        self,
    ) -> Callable[[config.GetResourceDriftRequest], config.ResourceDrift]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetResourceDrift(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_revision(self) -> Callable[[config.GetRevisionRequest], config.Revision]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetRevision(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_terraform_version(
        self,
    ) -> Callable[[config.GetTerraformVersionRequest], config.TerraformVersion]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTerraformVersion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def import_statefile(
        self,
    ) -> Callable[[config.ImportStatefileRequest], config.Statefile]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ImportStatefile(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_deployment_group_revisions(
        self,
    ) -> Callable[
        [config.ListDeploymentGroupRevisionsRequest],
        config.ListDeploymentGroupRevisionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDeploymentGroupRevisions(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_deployment_groups(
        self,
    ) -> Callable[
        [config.ListDeploymentGroupsRequest], config.ListDeploymentGroupsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDeploymentGroups(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_deployments(
        self,
    ) -> Callable[[config.ListDeploymentsRequest], config.ListDeploymentsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDeployments(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_previews(
        self,
    ) -> Callable[[config.ListPreviewsRequest], config.ListPreviewsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPreviews(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_resource_changes(
        self,
    ) -> Callable[
        [config.ListResourceChangesRequest], config.ListResourceChangesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListResourceChanges(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_resource_drifts(
        self,
    ) -> Callable[
        [config.ListResourceDriftsRequest], config.ListResourceDriftsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListResourceDrifts(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_resources(
        self,
    ) -> Callable[[config.ListResourcesRequest], config.ListResourcesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListResources(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_revisions(
        self,
    ) -> Callable[[config.ListRevisionsRequest], config.ListRevisionsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListRevisions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_terraform_versions(
        self,
    ) -> Callable[
        [config.ListTerraformVersionsRequest], config.ListTerraformVersionsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTerraformVersions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def lock_deployment(
        self,
    ) -> Callable[[config.LockDeploymentRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._LockDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def provision_deployment_group(
        self,
    ) -> Callable[[config.ProvisionDeploymentGroupRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ProvisionDeploymentGroup(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def unlock_deployment(
        self,
    ) -> Callable[[config.UnlockDeploymentRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UnlockDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_auto_migration_config(
        self,
    ) -> Callable[[config.UpdateAutoMigrationConfigRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateAutoMigrationConfig(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_deployment(
        self,
    ) -> Callable[[config.UpdateDeploymentRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDeployment(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_deployment_group(
        self,
    ) -> Callable[[config.UpdateDeploymentGroupRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDeploymentGroup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(_BaseConfigRestTransport._BaseGetLocation, ConfigRestStub):
        def __hash__(self):
            return hash("ConfigRestTransport.GetLocation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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

            http_options = _BaseConfigRestTransport._BaseGetLocation._get_http_options()
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.config_v1.ConfigClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._GetLocation._get_response(
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
                    "Received response for google.cloud.config_v1.ConfigAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "GetLocation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_locations(self):
        return self._ListLocations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListLocations(_BaseConfigRestTransport._BaseListLocations, ConfigRestStub):
        def __hash__(self):
            return hash("ConfigRestTransport.ListLocations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseConfigRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.config_v1.ConfigClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._ListLocations._get_response(
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
                    "Received response for google.cloud.config_v1.ConfigAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "ListLocations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def get_iam_policy(self):
        return self._GetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _GetIamPolicy(_BaseConfigRestTransport._BaseGetIamPolicy, ConfigRestStub):
        def __hash__(self):
            return hash("ConfigRestTransport.GetIamPolicy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseConfigRestTransport._BaseGetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseGetIamPolicy,
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
                    f"Sending request for google.cloud.config_v1.ConfigClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._GetIamPolicy._get_response(
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
                    "Received response for google.cloud.config_v1.ConfigAsyncClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "GetIamPolicy",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def set_iam_policy(self):
        return self._SetIamPolicy(self._session, self._host, self._interceptor)  # type: ignore

    class _SetIamPolicy(_BaseConfigRestTransport._BaseSetIamPolicy, ConfigRestStub):
        def __hash__(self):
            return hash("ConfigRestTransport.SetIamPolicy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseConfigRestTransport._BaseSetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseSetIamPolicy,
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
                    f"Sending request for google.cloud.config_v1.ConfigClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._SetIamPolicy._get_response(
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
                    "Received response for google.cloud.config_v1.ConfigAsyncClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
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
        _BaseConfigRestTransport._BaseTestIamPermissions, ConfigRestStub
    ):
        def __hash__(self):
            return hash("ConfigRestTransport.TestIamPermissions")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseConfigRestTransport._BaseTestIamPermissions._get_http_options()
            )
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseTestIamPermissions,
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
                    f"Sending request for google.cloud.config_v1.ConfigClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._TestIamPermissions._get_response(
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
                    "Received response for google.cloud.config_v1.ConfigAsyncClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
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
        _BaseConfigRestTransport._BaseCancelOperation, ConfigRestStub
    ):
        def __hash__(self):
            return hash("ConfigRestTransport.CancelOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseConfigRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.config_v1.ConfigClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._CancelOperation._get_response(
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
        _BaseConfigRestTransport._BaseDeleteOperation, ConfigRestStub
    ):
        def __hash__(self):
            return hash("ConfigRestTransport.DeleteOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseConfigRestTransport._BaseDeleteOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.config_v1.ConfigClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._DeleteOperation._get_response(
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

    class _GetOperation(_BaseConfigRestTransport._BaseGetOperation, ConfigRestStub):
        def __hash__(self):
            return hash("ConfigRestTransport.GetOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseConfigRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.config_v1.ConfigClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.config_v1.ConfigAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "GetOperation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_operations(self):
        return self._ListOperations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListOperations(_BaseConfigRestTransport._BaseListOperations, ConfigRestStub):
        def __hash__(self):
            return hash("ConfigRestTransport.ListOperations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
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
                _BaseConfigRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseConfigRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.config_v1.ConfigClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ConfigRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.config_v1.ConfigAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.config.v1.Config",
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


__all__ = ("ConfigRestTransport",)
